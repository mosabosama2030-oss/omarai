# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **003**
- سجلات الأسطر: **800**
- النطاق: SRC-59CF4B7DE8-L000222 إلى SRC-1AE03B9EC3-L000344
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-59CF4B7DE8 — [agents/research.py](../../agents/research.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-59CF4B7DE8-L000222](../../agents/research.py#L222) | 222 | `"    if social_focus:"` | — |
| [SRC-59CF4B7DE8-L000223](../../agents/research.py#L223) | 223 | `"        selected = platforms or [\"facebook\", \"instagram\", \"reddit\"]"` | — |
| [SRC-59CF4B7DE8-L000224](../../agents/research.py#L224) | 224 | `"        for platform in selected[:3]:"` | — |
| [SRC-59CF4B7DE8-L000225](../../agents/research.py#L225) | 225 | `"            domain = SOCIAL_DOMAINS[platform]"` | — |
| [SRC-59CF4B7DE8-L000226](../../agents/research.py#L226) | 226 | `"            site_query = _compact(f\"site:{domain} {base}\", 500)"` | — |
| [SRC-59CF4B7DE8-L000227](../../agents/research.py#L227) | 227 | `"            if site_query not in queries:"` | — |
| [SRC-59CF4B7DE8-L000228](../../agents/research.py#L228) | 228 | `"                queries.append(site_query)"` | — |
| [SRC-59CF4B7DE8-L000229](../../agents/research.py#L229) | 229 | `""` | — |
| [SRC-59CF4B7DE8-L000230](../../agents/research.py#L230) | 230 | `"    if deep and not social_focus and len(queries) < MAX_PLAN_QUERIES:"` | — |
| [SRC-59CF4B7DE8-L000231](../../agents/research.py#L231) | 231 | `"        queries.append(_compact(base + \" مصادر موثوقة تقارير إحصاءات\", 500))"` | — |
| [SRC-59CF4B7DE8-L000232](../../agents/research.py#L232) | 232 | `""` | — |
| [SRC-59CF4B7DE8-L000233](../../agents/research.py#L233) | 233 | `"    unique: list[str] = []"` | — |
| [SRC-59CF4B7DE8-L000234](../../agents/research.py#L234) | 234 | `"    seen: set[str] = set()"` | — |
| [SRC-59CF4B7DE8-L000235](../../agents/research.py#L235) | 235 | `"    for query in queries:"` | — |
| [SRC-59CF4B7DE8-L000236](../../agents/research.py#L236) | 236 | `"        value = _compact(query, 500)"` | — |
| [SRC-59CF4B7DE8-L000237](../../agents/research.py#L237) | 237 | `"        key = value.casefold()"` | — |
| [SRC-59CF4B7DE8-L000238](../../agents/research.py#L238) | 238 | `"        if value and key not in seen:"` | — |
| [SRC-59CF4B7DE8-L000239](../../agents/research.py#L239) | 239 | `"            unique.append(value)"` | — |
| [SRC-59CF4B7DE8-L000240](../../agents/research.py#L240) | 240 | `"            seen.add(key)"` | — |
| [SRC-59CF4B7DE8-L000241](../../agents/research.py#L241) | 241 | `"        if len(unique) >= MAX_PLAN_QUERIES:"` | — |
| [SRC-59CF4B7DE8-L000242](../../agents/research.py#L242) | 242 | `"            break"` | — |
| [SRC-59CF4B7DE8-L000243](../../agents/research.py#L243) | 243 | `""` | — |
| [SRC-59CF4B7DE8-L000244](../../agents/research.py#L244) | 244 | `"    return {"` | — |
| [SRC-59CF4B7DE8-L000245](../../agents/research.py#L245) | 245 | `"        \"queries\": unique or [base],"` | — |
| [SRC-59CF4B7DE8-L000246](../../agents/research.py#L246) | 246 | `"        \"direct_urls\": direct_urls,"` | — |
| [SRC-59CF4B7DE8-L000247](../../agents/research.py#L247) | 247 | `"        \"social_focus\": social_focus,"` | — |
| [SRC-59CF4B7DE8-L000248](../../agents/research.py#L248) | 248 | `"        \"freshness\": \"current\" if fresh else \"any\","` | — |
| [SRC-59CF4B7DE8-L000249](../../agents/research.py#L249) | 249 | `"        \"depth\": detected_depth,"` | — |
| [SRC-59CF4B7DE8-L000250](../../agents/research.py#L250) | 250 | `"        \"platforms\": platforms,"` | — |
| [SRC-59CF4B7DE8-L000251](../../agents/research.py#L251) | 251 | `"        \"planning_method\": \"deterministic_fallback\","` | — |
| [SRC-59CF4B7DE8-L000252](../../agents/research.py#L252) | 252 | `"    }"` | — |
| [SRC-59CF4B7DE8-L000253](../../agents/research.py#L253) | 253 | `""` | — |
| [SRC-59CF4B7DE8-L000254](../../agents/research.py#L254) | 254 | `""` | — |
| [SRC-59CF4B7DE8-L000255](../../agents/research.py#L255) | 255 | `"def validate_plan("` | — |
| [SRC-59CF4B7DE8-L000256](../../agents/research.py#L256) | 256 | `"    candidate: Any, question: str, history: list[dict[str, str]] \| None = None"` | — |
| [SRC-59CF4B7DE8-L000257](../../agents/research.py#L257) | 257 | `") -> dict[str, Any]:"` | — |
| [SRC-59CF4B7DE8-L000258](../../agents/research.py#L258) | 258 | `"    fallback = fallback_plan(question, history)"` | — |
| [SRC-59CF4B7DE8-L000259](../../agents/research.py#L259) | 259 | `"    if not isinstance(candidate, dict):"` | — |
| [SRC-59CF4B7DE8-L000260](../../agents/research.py#L260) | 260 | `"        return fallback"` | — |
| [SRC-59CF4B7DE8-L000261](../../agents/research.py#L261) | 261 | `"    raw_queries = candidate.get(\"queries\", [])"` | — |
| [SRC-59CF4B7DE8-L000262](../../agents/research.py#L262) | 262 | `"    if not isinstance(raw_queries, list):"` | — |
| [SRC-59CF4B7DE8-L000263](../../agents/research.py#L263) | 263 | `"        return fallback"` | — |
| [SRC-59CF4B7DE8-L000264](../../agents/research.py#L264) | 264 | `"    queries: list[str] = []"` | — |
| [SRC-59CF4B7DE8-L000265](../../agents/research.py#L265) | 265 | `"    seen: set[str] = set()"` | — |
| [SRC-59CF4B7DE8-L000266](../../agents/research.py#L266) | 266 | `"    for item in raw_queries:"` | — |
| [SRC-59CF4B7DE8-L000267](../../agents/research.py#L267) | 267 | `"        query = _compact(item, 500)"` | — |
| [SRC-59CF4B7DE8-L000268](../../agents/research.py#L268) | 268 | `"        # Never accept prompt-like multi-line payloads as search-query instructions."` | — |
| [SRC-59CF4B7DE8-L000269](../../agents/research.py#L269) | 269 | `"        query = query.replace(\"\\n\", \" \").replace(\"\\r\", \" \")"` | — |
| [SRC-59CF4B7DE8-L000270](../../agents/research.py#L270) | 270 | `"        if len(query) < 2:"` | — |
| [SRC-59CF4B7DE8-L000271](../../agents/research.py#L271) | 271 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000272](../../agents/research.py#L272) | 272 | `"        if query.casefold() not in seen:"` | — |
| [SRC-59CF4B7DE8-L000273](../../agents/research.py#L273) | 273 | `"            seen.add(query.casefold())"` | — |
| [SRC-59CF4B7DE8-L000274](../../agents/research.py#L274) | 274 | `"            queries.append(query)"` | — |
| [SRC-59CF4B7DE8-L000275](../../agents/research.py#L275) | 275 | `"        if len(queries) >= MAX_PLAN_QUERIES:"` | — |
| [SRC-59CF4B7DE8-L000276](../../agents/research.py#L276) | 276 | `"            break"` | — |
| [SRC-59CF4B7DE8-L000277](../../agents/research.py#L277) | 277 | `"    if not queries:"` | — |
| [SRC-59CF4B7DE8-L000278](../../agents/research.py#L278) | 278 | `"        return fallback"` | — |
| [SRC-59CF4B7DE8-L000279](../../agents/research.py#L279) | 279 | `"    base = fallback_plan(question, history)"` | — |
| [SRC-59CF4B7DE8-L000280](../../agents/research.py#L280) | 280 | `"    platforms = candidate.get(\"platforms\")"` | — |
| [SRC-59CF4B7DE8-L000281](../../agents/research.py#L281) | 281 | `"    if not isinstance(platforms, list):"` | — |
| [SRC-59CF4B7DE8-L000282](../../agents/research.py#L282) | 282 | `"        platforms = base[\"platforms\"]"` | — |
| [SRC-59CF4B7DE8-L000283](../../agents/research.py#L283) | 283 | `"    safe_platforms = [p for p in platforms if isinstance(p, str) and p in SOCIAL_DOMAINS]"` | — |
| [SRC-59CF4B7DE8-L000284](../../agents/research.py#L284) | 284 | `"    return {"` | — |
| [SRC-59CF4B7DE8-L000285](../../agents/research.py#L285) | 285 | `"        \"queries\": queries,"` | — |
| [SRC-59CF4B7DE8-L000286](../../agents/research.py#L286) | 286 | `"        \"direct_urls\": fallback[\"direct_urls\"],"` | — |
| [SRC-59CF4B7DE8-L000287](../../agents/research.py#L287) | 287 | `"        \"social_focus\": bool(candidate.get(\"social_focus\", base[\"social_focus\"])),"` | — |
| [SRC-59CF4B7DE8-L000288](../../agents/research.py#L288) | 288 | `"        \"freshness\": \"current\" if candidate.get(\"freshness\") == \"current\" else base[\"freshness\"],"` | — |
| [SRC-59CF4B7DE8-L000289](../../agents/research.py#L289) | 289 | `"        \"depth\": \"deep\" if candidate.get(\"depth\") == \"deep\" else base[\"depth\"],"` | — |
| [SRC-59CF4B7DE8-L000290](../../agents/research.py#L290) | 290 | `"        \"platforms\": list(dict.fromkeys(safe_platforms))[:5],"` | — |
| [SRC-59CF4B7DE8-L000291](../../agents/research.py#L291) | 291 | `"        \"planning_method\": \"language_model\","` | — |
| [SRC-59CF4B7DE8-L000292](../../agents/research.py#L292) | 292 | `"    }"` | — |
| [SRC-59CF4B7DE8-L000293](../../agents/research.py#L293) | 293 | `""` | — |
| [SRC-59CF4B7DE8-L000294](../../agents/research.py#L294) | 294 | `""` | — |
| [SRC-59CF4B7DE8-L000295](../../agents/research.py#L295) | 295 | `"def _canonical_result_url(url: str) -> str:"` | — |
| [SRC-59CF4B7DE8-L000296](../../agents/research.py#L296) | 296 | `"    try:"` | — |
| [SRC-59CF4B7DE8-L000297](../../agents/research.py#L297) | 297 | `"        parsed = urlparse(url)"` | — |
| [SRC-59CF4B7DE8-L000298](../../agents/research.py#L298) | 298 | `"        host = (parsed.hostname or \"\").lower().removeprefix(\"www.\")"` | — |
| [SRC-59CF4B7DE8-L000299](../../agents/research.py#L299) | 299 | `"        # Drop fragments and common tracking query parameters before deduplication."` | — |
| [SRC-59CF4B7DE8-L000300](../../agents/research.py#L300) | 300 | `"        parts = []"` | — |
| [SRC-59CF4B7DE8-L000301](../../agents/research.py#L301) | 301 | `"        for part in parsed.query.split(\"&\"):"` | — |
| [SRC-59CF4B7DE8-L000302](../../agents/research.py#L302) | 302 | `"            key = part.split(\"=\", 1)[0].lower()"` | — |
| [SRC-59CF4B7DE8-L000303](../../agents/research.py#L303) | 303 | `"            if key.startswith(\"utm_\") or key in {\"fbclid\", \"gclid\", \"ref\", \"ref_src\"}:"` | — |
| [SRC-59CF4B7DE8-L000304](../../agents/research.py#L304) | 304 | `"                continue"` | — |
| [SRC-59CF4B7DE8-L000305](../../agents/research.py#L305) | 305 | `"            if part:"` | — |
| [SRC-59CF4B7DE8-L000306](../../agents/research.py#L306) | 306 | `"                parts.append(part)"` | — |
| [SRC-59CF4B7DE8-L000307](../../agents/research.py#L307) | 307 | `"        query = \"&\".join(sorted(parts))"` | — |
| [SRC-59CF4B7DE8-L000308](../../agents/research.py#L308) | 308 | `"        path = parsed.path.rstrip(\"/\") or \"/\""` | — |
| [SRC-59CF4B7DE8-L000309](../../agents/research.py#L309) | 309 | `"        return f\"{parsed.scheme.lower()}://{host}{path}\" + (f\"?{query}\" if query else \"\")"` | — |
| [SRC-59CF4B7DE8-L000310](../../agents/research.py#L310) | 310 | `"    except (ValueError, TypeError):"` | — |
| [SRC-59CF4B7DE8-L000311](../../agents/research.py#L311) | 311 | `"        return url"` | — |
| [SRC-59CF4B7DE8-L000312](../../agents/research.py#L312) | 312 | `""` | — |
| [SRC-59CF4B7DE8-L000313](../../agents/research.py#L313) | 313 | `""` | — |
| [SRC-59CF4B7DE8-L000314](../../agents/research.py#L314) | 314 | `"def classify_source(url: str) -> dict[str, str]:"` | — |
| [SRC-59CF4B7DE8-L000315](../../agents/research.py#L315) | 315 | `"    host = (urlparse(url).hostname or \"\").lower().removeprefix(\"www.\")"` | — |
| [SRC-59CF4B7DE8-L000316](../../agents/research.py#L316) | 316 | `"    platform = \"web\""` | — |
| [SRC-59CF4B7DE8-L000317](../../agents/research.py#L317) | 317 | `"    mapping = {"` | — |
| [SRC-59CF4B7DE8-L000318](../../agents/research.py#L318) | 318 | `"        \"reddit.com\": \"reddit\", \"old.reddit.com\": \"reddit\","` | — |
| [SRC-59CF4B7DE8-L000319](../../agents/research.py#L319) | 319 | `"        \"youtube.com\": \"youtube\", \"youtu.be\": \"youtube\","` | — |
| [SRC-59CF4B7DE8-L000320](../../agents/research.py#L320) | 320 | `"        \"facebook.com\": \"facebook\", \"instagram.com\": \"instagram\","` | — |
| [SRC-59CF4B7DE8-L000321](../../agents/research.py#L321) | 321 | `"        \"x.com\": \"x\", \"twitter.com\": \"x\", \"tiktok.com\": \"tiktok\","` | — |
| [SRC-59CF4B7DE8-L000322](../../agents/research.py#L322) | 322 | `"        \"linkedin.com\": \"linkedin\", \"threads.net\": \"threads\","` | — |
| [SRC-59CF4B7DE8-L000323](../../agents/research.py#L323) | 323 | `"        \"bsky.app\": \"bluesky\","` | — |
| [SRC-59CF4B7DE8-L000324](../../agents/research.py#L324) | 324 | `"    }"` | — |
| [SRC-59CF4B7DE8-L000325](../../agents/research.py#L325) | 325 | `"    for domain, label in mapping.items():"` | — |
| [SRC-59CF4B7DE8-L000326](../../agents/research.py#L326) | 326 | `"        if host == domain or host.endswith(\".\" + domain):"` | — |
| [SRC-59CF4B7DE8-L000327](../../agents/research.py#L327) | 327 | `"            platform = label"` | — |
| [SRC-59CF4B7DE8-L000328](../../agents/research.py#L328) | 328 | `"            break"` | — |
| [SRC-59CF4B7DE8-L000329](../../agents/research.py#L329) | 329 | `"    trust = \"general\""` | — |
| [SRC-59CF4B7DE8-L000330](../../agents/research.py#L330) | 330 | `"    if host.endswith((\".gov\", \".gov.eg\", \".gov.uk\")):"` | — |
| [SRC-59CF4B7DE8-L000331](../../agents/research.py#L331) | 331 | `"        trust = \"government\""` | — |
| [SRC-59CF4B7DE8-L000332](../../agents/research.py#L332) | 332 | `"    elif host.endswith((\".edu\", \".ac.uk\", \".edu.eg\")):"` | — |
| [SRC-59CF4B7DE8-L000333](../../agents/research.py#L333) | 333 | `"        trust = \"academic\""` | — |
| [SRC-59CF4B7DE8-L000334](../../agents/research.py#L334) | 334 | `"    elif host == \"news.google.com\" or any("` | — |
| [SRC-59CF4B7DE8-L000335](../../agents/research.py#L335) | 335 | `"        name in host"` | — |
| [SRC-59CF4B7DE8-L000336](../../agents/research.py#L336) | 336 | `"        for name in ("` | — |
| [SRC-59CF4B7DE8-L000337](../../agents/research.py#L337) | 337 | `"            \"reuters.com\", \"apnews.com\", \"bbc.com\", \"bbc.co.uk\","` | — |
| [SRC-59CF4B7DE8-L000338](../../agents/research.py#L338) | 338 | `"            \"ft.com\", \"nytimes.com\", \"theguardian.com\","` | — |
| [SRC-59CF4B7DE8-L000339](../../agents/research.py#L339) | 339 | `"        )"` | — |
| [SRC-59CF4B7DE8-L000340](../../agents/research.py#L340) | 340 | `"    ):"` | — |
| [SRC-59CF4B7DE8-L000341](../../agents/research.py#L341) | 341 | `"        trust = \"news\""` | — |
| [SRC-59CF4B7DE8-L000342](../../agents/research.py#L342) | 342 | `"    elif platform != \"web\":"` | — |
| [SRC-59CF4B7DE8-L000343](../../agents/research.py#L343) | 343 | `"        trust = \"social\""` | — |
| [SRC-59CF4B7DE8-L000344](../../agents/research.py#L344) | 344 | `"    return {\"domain\": host, \"platform\": platform, \"source_class\": trust}"` | — |
| [SRC-59CF4B7DE8-L000345](../../agents/research.py#L345) | 345 | `""` | — |
| [SRC-59CF4B7DE8-L000346](../../agents/research.py#L346) | 346 | `""` | — |
| [SRC-59CF4B7DE8-L000347](../../agents/research.py#L347) | 347 | `"def fuse_ranked_results("` | — |
| [SRC-59CF4B7DE8-L000348](../../agents/research.py#L348) | 348 | `"    batches: list[dict[str, Any]], limit: int = MAX_FUSED_RESULTS"` | — |
| [SRC-59CF4B7DE8-L000349](../../agents/research.py#L349) | 349 | `") -> list[dict[str, Any]]:"` | — |
| [SRC-59CF4B7DE8-L000350](../../agents/research.py#L350) | 350 | `"    \"\"\"Reciprocal-rank-fuse result sets across queries/providers and dedupe URLs.\"\"\""` | — |
| [SRC-59CF4B7DE8-L000351](../../agents/research.py#L351) | 351 | `"    accumulated: dict[str, dict[str, Any]] = {}"` | — |
| [SRC-59CF4B7DE8-L000352](../../agents/research.py#L352) | 352 | `"    for batch in batches:"` | — |
| [SRC-59CF4B7DE8-L000353](../../agents/research.py#L353) | 353 | `"        query = _compact(batch.get(\"query\", \"\"), 500)"` | — |
| [SRC-59CF4B7DE8-L000354](../../agents/research.py#L354) | 354 | `"        provider = _compact(batch.get(\"provider\", \"search\"), 80)"` | — |
| [SRC-59CF4B7DE8-L000355](../../agents/research.py#L355) | 355 | `"        results = batch.get(\"results\", [])"` | — |
| [SRC-59CF4B7DE8-L000356](../../agents/research.py#L356) | 356 | `"        if not isinstance(results, list):"` | — |
| [SRC-59CF4B7DE8-L000357](../../agents/research.py#L357) | 357 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000358](../../agents/research.py#L358) | 358 | `"        for position, source in enumerate(results, 1):"` | — |
| [SRC-59CF4B7DE8-L000359](../../agents/research.py#L359) | 359 | `"            if not isinstance(source, dict) or not source.get(\"url\"):"` | — |
| [SRC-59CF4B7DE8-L000360](../../agents/research.py#L360) | 360 | `"                continue"` | — |
| [SRC-59CF4B7DE8-L000361](../../agents/research.py#L361) | 361 | `"            url = _canonical_result_url(str(source[\"url\"]))"` | — |
| [SRC-59CF4B7DE8-L000362](../../agents/research.py#L362) | 362 | `"            if not url.startswith((\"https://\", \"http://\")):"` | — |
| [SRC-59CF4B7DE8-L000363](../../agents/research.py#L363) | 363 | `"                continue"` | — |
| [SRC-59CF4B7DE8-L000364](../../agents/research.py#L364) | 364 | `"            entry = accumulated.get(url)"` | — |
| [SRC-59CF4B7DE8-L000365](../../agents/research.py#L365) | 365 | `"            if entry is None:"` | — |
| [SRC-59CF4B7DE8-L000366](../../agents/research.py#L366) | 366 | `"                publisher_url = _compact(source.get(\"publisher_url\") or \"\", 2048)"` | — |
| [SRC-59CF4B7DE8-L000367](../../agents/research.py#L367) | 367 | `"                source_identity_url = publisher_url or str(source[\"url\"])"` | — |
| [SRC-59CF4B7DE8-L000368](../../agents/research.py#L368) | 368 | `"                entry = {"` | — |
| [SRC-59CF4B7DE8-L000369](../../agents/research.py#L369) | 369 | `"                    \"title\": _compact(source.get(\"title\") or \"نتيجة ويب\", 300),"` | — |
| [SRC-59CF4B7DE8-L000370](../../agents/research.py#L370) | 370 | `"                    \"url\": str(source[\"url\"]),"` | — |
| [SRC-59CF4B7DE8-L000371](../../agents/research.py#L371) | 371 | `"                    \"snippet\": _compact(source.get(\"snippet\") or \"\", 1800),"` | — |
| [SRC-59CF4B7DE8-L000372](../../agents/research.py#L372) | 372 | `"                    \"page_text\": _compact(source.get(\"page_text\") or \"\", 12_000),"` | — |
| [SRC-59CF4B7DE8-L000373](../../agents/research.py#L373) | 373 | `"                    \"page_fetched\": bool(source.get(\"page_fetched\")),"` | — |
| [SRC-59CF4B7DE8-L000374](../../agents/research.py#L374) | 374 | `"                    \"providers\": [],"` | — |
| [SRC-59CF4B7DE8-L000375](../../agents/research.py#L375) | 375 | `"                    \"queries\": [],"` | — |
| [SRC-59CF4B7DE8-L000376](../../agents/research.py#L376) | 376 | `"                    \"rank_score\": 0.0,"` | — |
| [SRC-59CF4B7DE8-L000377](../../agents/research.py#L377) | 377 | `"                    \"best_raw_rank\": position,"` | — |
| [SRC-59CF4B7DE8-L000378](../../agents/research.py#L378) | 378 | `"                    \"published_at\": _compact(source.get(\"published_at\") or \"\", 100),"` | — |
| [SRC-59CF4B7DE8-L000379](../../agents/research.py#L379) | 379 | `"                    \"publisher_name\": _compact(source.get(\"publisher_name\") or \"\", 200),"` | — |
| [SRC-59CF4B7DE8-L000380](../../agents/research.py#L380) | 380 | `"                    \"publisher_url\": publisher_url,"` | — |
| [SRC-59CF4B7DE8-L000381](../../agents/research.py#L381) | 381 | `"                    \"publisher_domain\": _compact(source.get(\"publisher_domain\") or \"\", 300),"` | — |
| [SRC-59CF4B7DE8-L000382](../../agents/research.py#L382) | 382 | `"                }"` | — |
| [SRC-59CF4B7DE8-L000383](../../agents/research.py#L383) | 383 | `"                entry.update(classify_source(source_identity_url))"` | — |
| [SRC-59CF4B7DE8-L000384](../../agents/research.py#L384) | 384 | `"                accumulated[url] = entry"` | — |
| [SRC-59CF4B7DE8-L000385](../../agents/research.py#L385) | 385 | `"            elif source.get(\"publisher_url\") and not entry.get(\"publisher_url\"):"` | — |
| [SRC-59CF4B7DE8-L000386](../../agents/research.py#L386) | 386 | `"                entry[\"publisher_url\"] = _compact(source.get(\"publisher_url\"), 2048)"` | — |
| [SRC-59CF4B7DE8-L000387](../../agents/research.py#L387) | 387 | `"                entry[\"publisher_name\"] = _compact(source.get(\"publisher_name\") or \"\", 200)"` | — |
| [SRC-59CF4B7DE8-L000388](../../agents/research.py#L388) | 388 | `"                entry[\"publisher_domain\"] = _compact(source.get(\"publisher_domain\") or \"\", 300)"` | — |
| [SRC-59CF4B7DE8-L000389](../../agents/research.py#L389) | 389 | `"                entry.update(classify_source(entry[\"publisher_url\"]))"` | — |
| [SRC-59CF4B7DE8-L000390](../../agents/research.py#L390) | 390 | `"            entry[\"rank_score\"] += 1.0 / (60 + position)"` | — |
| [SRC-59CF4B7DE8-L000391](../../agents/research.py#L391) | 391 | `"            entry[\"best_raw_rank\"] = min(entry[\"best_raw_rank\"], position)"` | — |
| [SRC-59CF4B7DE8-L000392](../../agents/research.py#L392) | 392 | `"            if provider and provider not in entry[\"providers\"]:"` | — |
| [SRC-59CF4B7DE8-L000393](../../agents/research.py#L393) | 393 | `"                entry[\"providers\"].append(provider)"` | — |
| [SRC-59CF4B7DE8-L000394](../../agents/research.py#L394) | 394 | `"            if query and query not in entry[\"queries\"]:"` | — |
| [SRC-59CF4B7DE8-L000395](../../agents/research.py#L395) | 395 | `"                entry[\"queries\"].append(query)"` | — |
| [SRC-59CF4B7DE8-L000396](../../agents/research.py#L396) | 396 | `"            if len(str(source.get(\"snippet\") or \"\")) > len(entry[\"snippet\"]):"` | — |
| [SRC-59CF4B7DE8-L000397](../../agents/research.py#L397) | 397 | `"                entry[\"snippet\"] = _compact(source.get(\"snippet\"), 1800)"` | — |
| [SRC-59CF4B7DE8-L000398](../../agents/research.py#L398) | 398 | `"            if source.get(\"published_at\") and not entry.get(\"published_at\"):"` | — |
| [SRC-59CF4B7DE8-L000399](../../agents/research.py#L399) | 399 | `"                entry[\"published_at\"] = _compact(source[\"published_at\"], 100)"` | — |
| [SRC-59CF4B7DE8-L000400](../../agents/research.py#L400) | 400 | `"            if source.get(\"page_text\") and not entry[\"page_text\"]:"` | — |
| [SRC-59CF4B7DE8-L000401](../../agents/research.py#L401) | 401 | `"                entry[\"page_text\"] = _compact(source[\"page_text\"], 12_000)"` | — |
| [SRC-59CF4B7DE8-L000402](../../agents/research.py#L402) | 402 | `"                entry[\"page_fetched\"] = True"` | — |
| [SRC-59CF4B7DE8-L000403](../../agents/research.py#L403) | 403 | `"    # A cross-query result gets a modest consensus bonus; official/academic sources"` | — |
| [SRC-59CF4B7DE8-L000404](../../agents/research.py#L404) | 404 | `"    # get a small prior, never enough to override actual query relevance."` | — |
| [SRC-59CF4B7DE8-L000405](../../agents/research.py#L405) | 405 | `"    for entry in accumulated.values():"` | — |
| [SRC-59CF4B7DE8-L000406](../../agents/research.py#L406) | 406 | `"        entry[\"rank_score\"] += min(len(entry[\"queries\"]), 4) * 0.00015"` | — |
| [SRC-59CF4B7DE8-L000407](../../agents/research.py#L407) | 407 | `"        if entry[\"source_class\"] in {\"government\", \"academic\"}:"` | — |
| [SRC-59CF4B7DE8-L000408](../../agents/research.py#L408) | 408 | `"            entry[\"rank_score\"] += 0.0001"` | — |
| [SRC-59CF4B7DE8-L000409](../../agents/research.py#L409) | 409 | `"        if \"user_supplied_url\" in entry[\"providers\"]:"` | — |
| [SRC-59CF4B7DE8-L000410](../../agents/research.py#L410) | 410 | `"            entry[\"rank_score\"] += 0.5"` | — |
| [SRC-59CF4B7DE8-L000411](../../agents/research.py#L411) | 411 | `"    ranked = sorted(accumulated.values(), key=lambda item: item[\"rank_score\"], reverse=True)"` | — |
| [SRC-59CF4B7DE8-L000412](../../agents/research.py#L412) | 412 | `"    return ranked[:max(1, min(int(limit), MAX_FUSED_RESULTS))]"` | — |
| [SRC-59CF4B7DE8-L000413](../../agents/research.py#L413) | 413 | `""` | — |
| [SRC-59CF4B7DE8-L000414](../../agents/research.py#L414) | 414 | `""` | — |
| [SRC-59CF4B7DE8-L000415](../../agents/research.py#L415) | 415 | `""` | — |
| [SRC-59CF4B7DE8-L000416](../../agents/research.py#L416) | 416 | `"def _parse_publication_date(value: Any, now: datetime \| None = None) -> datetime \| None:"` | — |
| [SRC-59CF4B7DE8-L000417](../../agents/research.py#L417) | 417 | `"    \"\"\"Parse common search/RSS publication dates without guessing missing dates.\"\"\""` | — |
| [SRC-59CF4B7DE8-L000418](../../agents/research.py#L418) | 418 | `"    if not isinstance(value, str) or not value.strip():"` | — |
| [SRC-59CF4B7DE8-L000419](../../agents/research.py#L419) | 419 | `"        return None"` | — |
| [SRC-59CF4B7DE8-L000420](../../agents/research.py#L420) | 420 | `"    raw = value.strip()"` | — |
| [SRC-59CF4B7DE8-L000421](../../agents/research.py#L421) | 421 | `"    current = now or datetime.now(UTC)"` | — |
| [SRC-59CF4B7DE8-L000422](../../agents/research.py#L422) | 422 | `"    try:"` | — |
| [SRC-59CF4B7DE8-L000423](../../agents/research.py#L423) | 423 | `"        parsed = parsedate_to_datetime(raw)"` | — |
| [SRC-59CF4B7DE8-L000424](../../agents/research.py#L424) | 424 | `"        if parsed:"` | — |
| [SRC-59CF4B7DE8-L000425](../../agents/research.py#L425) | 425 | `"            return parsed.replace(tzinfo=parsed.tzinfo or UTC).astimezone(UTC)"` | — |
| [SRC-59CF4B7DE8-L000426](../../agents/research.py#L426) | 426 | `"    except (TypeError, ValueError, OverflowError):"` | — |
| [SRC-59CF4B7DE8-L000427](../../agents/research.py#L427) | 427 | `"        pass"` | — |
| [SRC-59CF4B7DE8-L000428](../../agents/research.py#L428) | 428 | `"    iso_value = raw.replace(\"Z\", \"+00:00\")"` | — |
| [SRC-59CF4B7DE8-L000429](../../agents/research.py#L429) | 429 | `"    try:"` | — |
| [SRC-59CF4B7DE8-L000430](../../agents/research.py#L430) | 430 | `"        parsed = datetime.fromisoformat(iso_value)"` | — |
| [SRC-59CF4B7DE8-L000431](../../agents/research.py#L431) | 431 | `"        return parsed.replace(tzinfo=parsed.tzinfo or UTC).astimezone(UTC)"` | — |
| [SRC-59CF4B7DE8-L000432](../../agents/research.py#L432) | 432 | `"    except (TypeError, ValueError, OverflowError):"` | — |
| [SRC-59CF4B7DE8-L000433](../../agents/research.py#L433) | 433 | `"        pass"` | — |
| [SRC-59CF4B7DE8-L000434](../../agents/research.py#L434) | 434 | `"    for date_format in (\"%b %d, %Y\", \"%B %d, %Y\", \"%Y/%m/%d\", \"%d %b %Y\"):"` | — |
| [SRC-59CF4B7DE8-L000435](../../agents/research.py#L435) | 435 | `"        try:"` | — |
| [SRC-59CF4B7DE8-L000436](../../agents/research.py#L436) | 436 | `"            return datetime.strptime(raw, date_format).replace(tzinfo=UTC)"` | — |
| [SRC-59CF4B7DE8-L000437](../../agents/research.py#L437) | 437 | `"        except ValueError:"` | — |
| [SRC-59CF4B7DE8-L000438](../../agents/research.py#L438) | 438 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000439](../../agents/research.py#L439) | 439 | `"    match = re.search(r\"(\\d+)\\s+(hour\|day\|week\|month\|year)s?\\s+ago\", raw, re.IGNORECASE)"` | — |
| [SRC-59CF4B7DE8-L000440](../../agents/research.py#L440) | 440 | `"    if match:"` | — |
| [SRC-59CF4B7DE8-L000441](../../agents/research.py#L441) | 441 | `"        amount = int(match.group(1))"` | — |
| [SRC-59CF4B7DE8-L000442](../../agents/research.py#L442) | 442 | `"        unit = match.group(2).lower()"` | — |
| [SRC-59CF4B7DE8-L000443](../../agents/research.py#L443) | 443 | `"        durations = {"` | — |
| [SRC-59CF4B7DE8-L000444](../../agents/research.py#L444) | 444 | `"            \"hour\": timedelta(hours=amount),"` | — |
| [SRC-59CF4B7DE8-L000445](../../agents/research.py#L445) | 445 | `"            \"day\": timedelta(days=amount),"` | — |
| [SRC-59CF4B7DE8-L000446](../../agents/research.py#L446) | 446 | `"            \"week\": timedelta(days=7 * amount),"` | — |
| [SRC-59CF4B7DE8-L000447](../../agents/research.py#L447) | 447 | `"            \"month\": timedelta(days=30 * amount),"` | — |
| [SRC-59CF4B7DE8-L000448](../../agents/research.py#L448) | 448 | `"            \"year\": timedelta(days=365 * amount),"` | — |
| [SRC-59CF4B7DE8-L000449](../../agents/research.py#L449) | 449 | `"        }"` | — |
| [SRC-59CF4B7DE8-L000450](../../agents/research.py#L450) | 450 | `"        return current - durations[unit]"` | — |
| [SRC-59CF4B7DE8-L000451](../../agents/research.py#L451) | 451 | `"    if raw.lower() in {\"today\", \"just now\", \"now\"}:"` | — |
| [SRC-59CF4B7DE8-L000452](../../agents/research.py#L452) | 452 | `"        return current"` | — |
| [SRC-59CF4B7DE8-L000453](../../agents/research.py#L453) | 453 | `"    if raw.lower() == \"yesterday\":"` | — |
| [SRC-59CF4B7DE8-L000454](../../agents/research.py#L454) | 454 | `"        return current - timedelta(days=1)"` | — |
| [SRC-59CF4B7DE8-L000455](../../agents/research.py#L455) | 455 | `"    return None"` | — |
| [SRC-59CF4B7DE8-L000456](../../agents/research.py#L456) | 456 | `""` | — |
| [SRC-59CF4B7DE8-L000457](../../agents/research.py#L457) | 457 | `""` | — |
| [SRC-59CF4B7DE8-L000458](../../agents/research.py#L458) | 458 | `"def evidence_signal_report("` | — |
| [SRC-59CF4B7DE8-L000459](../../agents/research.py#L459) | 459 | `"    sources: list[dict[str, Any]],"` | — |
| [SRC-59CF4B7DE8-L000460](../../agents/research.py#L460) | 460 | `"    freshness: str = \"any\","` | — |
| [SRC-59CF4B7DE8-L000461](../../agents/research.py#L461) | 461 | `"    now: datetime \| None = None,"` | — |
| [SRC-59CF4B7DE8-L000462](../../agents/research.py#L462) | 462 | `") -> dict[str, Any]:"` | — |
| [SRC-59CF4B7DE8-L000463](../../agents/research.py#L463) | 463 | `"    \"\"\"Summarize research coverage; signals describe evidence coverage, not factual truth.\"\"\""` | — |
| [SRC-59CF4B7DE8-L000464](../../agents/research.py#L464) | 464 | `"    current = now or datetime.now(UTC)"` | — |
| [SRC-59CF4B7DE8-L000465](../../agents/research.py#L465) | 465 | `"    valid_sources = [source for source in sources if isinstance(source, dict) and source.get(\"url\")]"` | — |
| [SRC-59CF4B7DE8-L000466](../../agents/research.py#L466) | 466 | `"    domains = {"` | — |
| [SRC-59CF4B7DE8-L000467](../../agents/research.py#L467) | 467 | `"        registrable_domain("` | — |
| [SRC-59CF4B7DE8-L000468](../../agents/research.py#L468) | 468 | `"            source.get(\"domain\") or urlparse(str(source.get(\"url\") or \"\")).hostname or \"\""` | — |
| [SRC-59CF4B7DE8-L000469](../../agents/research.py#L469) | 469 | `"        )"` | — |
| [SRC-59CF4B7DE8-L000470](../../agents/research.py#L470) | 470 | `"        for source in valid_sources"` | — |
| [SRC-59CF4B7DE8-L000471](../../agents/research.py#L471) | 471 | `"        if source.get(\"domain\") or source.get(\"url\")"` | — |
| [SRC-59CF4B7DE8-L000472](../../agents/research.py#L472) | 472 | `"    }"` | — |
| [SRC-59CF4B7DE8-L000473](../../agents/research.py#L473) | 473 | `"    domains.discard(\"\")"` | — |
| [SRC-59CF4B7DE8-L000474](../../agents/research.py#L474) | 474 | `"    providers: set[str] = set()"` | — |
| [SRC-59CF4B7DE8-L000475](../../agents/research.py#L475) | 475 | `"    for source in valid_sources:"` | — |
| [SRC-59CF4B7DE8-L000476](../../agents/research.py#L476) | 476 | `"        candidate_providers = source.get(\"providers\", [])"` | — |
| [SRC-59CF4B7DE8-L000477](../../agents/research.py#L477) | 477 | `"        if isinstance(candidate_providers, list):"` | — |
| [SRC-59CF4B7DE8-L000478](../../agents/research.py#L478) | 478 | `"            providers.update(str(item) for item in candidate_providers if item)"` | — |
| [SRC-59CF4B7DE8-L000479](../../agents/research.py#L479) | 479 | `"        elif source.get(\"provider\"):"` | — |
| [SRC-59CF4B7DE8-L000480](../../agents/research.py#L480) | 480 | `"            providers.add(str(source[\"provider\"]))"` | — |
| [SRC-59CF4B7DE8-L000481](../../agents/research.py#L481) | 481 | `"    classes = [str(source.get(\"source_class\") or \"general\") for source in valid_sources]"` | — |
| [SRC-59CF4B7DE8-L000482](../../agents/research.py#L482) | 482 | `"    primary_count = sum(item in {\"government\", \"academic\", \"official\"} for item in classes)"` | — |
| [SRC-59CF4B7DE8-L000483](../../agents/research.py#L483) | 483 | `"    news_count = sum(item == \"news\" for item in classes)"` | — |
| [SRC-59CF4B7DE8-L000484](../../agents/research.py#L484) | 484 | `"    social_count = sum(item == \"social\" for item in classes)"` | — |
| [SRC-59CF4B7DE8-L000485](../../agents/research.py#L485) | 485 | `"    pages_read = sum(bool(source.get(\"page_fetched\")) for source in valid_sources)"` | — |
| [SRC-59CF4B7DE8-L000486](../../agents/research.py#L486) | 486 | `"    dates = ["` | — |
| [SRC-59CF4B7DE8-L000487](../../agents/research.py#L487) | 487 | `"        parsed"` | — |
| [SRC-59CF4B7DE8-L000488](../../agents/research.py#L488) | 488 | `"        for source in valid_sources"` | — |
| [SRC-59CF4B7DE8-L000489](../../agents/research.py#L489) | 489 | `"        if (parsed := _parse_publication_date(source.get(\"published_at\"), current)) is not None"` | — |
| [SRC-59CF4B7DE8-L000490](../../agents/research.py#L490) | 490 | `"    ]"` | — |
| [SRC-59CF4B7DE8-L000491](../../agents/research.py#L491) | 491 | `"    recent_days = 7 if freshness == \"current\" else 30"` | — |
| [SRC-59CF4B7DE8-L000492](../../agents/research.py#L492) | 492 | `"    recent_count = sum((current - parsed).total_seconds() >= 0 and"` | — |
| [SRC-59CF4B7DE8-L000493](../../agents/research.py#L493) | 493 | `"                       (current - parsed) <= timedelta(days=recent_days) for parsed in dates)"` | — |
| [SRC-59CF4B7DE8-L000494](../../agents/research.py#L494) | 494 | `"    future_dates = sum(parsed > current + timedelta(days=1) for parsed in dates)"` | — |
| [SRC-59CF4B7DE8-L000495](../../agents/research.py#L495) | 495 | `"    unique_sources = len(valid_sources)"` | — |
| [SRC-59CF4B7DE8-L000496](../../agents/research.py#L496) | 496 | `"    # Evidence coverage uses several independent dimensions and is deliberately not a"` | — |
| [SRC-59CF4B7DE8-L000497](../../agents/research.py#L497) | 497 | `"    # probability that any factual claim is true."` | — |
| [SRC-59CF4B7DE8-L000498](../../agents/research.py#L498) | 498 | `"    coverage_points = 0"` | — |
| [SRC-59CF4B7DE8-L000499](../../agents/research.py#L499) | 499 | `"    coverage_points += min(unique_sources, 10) * 3"` | — |
| [SRC-59CF4B7DE8-L000500](../../agents/research.py#L500) | 500 | `"    coverage_points += min(len(domains), 8) * 4"` | — |
| [SRC-59CF4B7DE8-L000501](../../agents/research.py#L501) | 501 | `"    coverage_points += min(len(providers), 4) * 5"` | — |
| [SRC-59CF4B7DE8-L000502](../../agents/research.py#L502) | 502 | `"    coverage_points += min(pages_read, 8) * 3"` | — |
| [SRC-59CF4B7DE8-L000503](../../agents/research.py#L503) | 503 | `"    coverage_points += min(primary_count, 4) * 4"` | — |
| [SRC-59CF4B7DE8-L000504](../../agents/research.py#L504) | 504 | `"    coverage_points += min(len(dates), 8) * 2"` | — |
| [SRC-59CF4B7DE8-L000505](../../agents/research.py#L505) | 505 | `"    coverage_score = min(100, coverage_points)"` | — |
| [SRC-59CF4B7DE8-L000506](../../agents/research.py#L506) | 506 | `"    if unique_sources >= 8 and len(domains) >= 5 and len(providers) >= 2 and pages_read >= 3:"` | — |
| [SRC-59CF4B7DE8-L000507](../../agents/research.py#L507) | 507 | `"        coverage_level = \"متعدد المصادر\""` | — |
| [SRC-59CF4B7DE8-L000508](../../agents/research.py#L508) | 508 | `"    elif unique_sources >= 4 and len(domains) >= 3 and len(providers) >= 1:"` | — |
| [SRC-59CF4B7DE8-L000509](../../agents/research.py#L509) | 509 | `"        coverage_level = \"متوسط\""` | — |
| [SRC-59CF4B7DE8-L000510](../../agents/research.py#L510) | 510 | `"    else:"` | — |
| [SRC-59CF4B7DE8-L000511](../../agents/research.py#L511) | 511 | `"        coverage_level = \"محدود\""` | — |
| [SRC-59CF4B7DE8-L000512](../../agents/research.py#L512) | 512 | `""` | — |
| [SRC-59CF4B7DE8-L000513](../../agents/research.py#L513) | 513 | `"    warnings: list[str] = []"` | — |
| [SRC-59CF4B7DE8-L000514](../../agents/research.py#L514) | 514 | `"    if unique_sources == 0:"` | — |
| [SRC-59CF4B7DE8-L000515](../../agents/research.py#L515) | 515 | `"        warnings.append(\"لا توجد مصادر قابلة للاستشهاد؛ لا تستنتج حقائق من عدم وجود نتائج.\")"` | — |
| [SRC-59CF4B7DE8-L000516](../../agents/research.py#L516) | 516 | `"    if len(domains) < 3:"` | — |
| [SRC-59CF4B7DE8-L000517](../../agents/research.py#L517) | 517 | `"        warnings.append(\"تنوع النطاقات محدود؛ لا تعتبر تكرار النتيجة تأكيدًا مستقلًا.\")"` | — |
| [SRC-59CF4B7DE8-L000518](../../agents/research.py#L518) | 518 | `"    if pages_read < 2 and unique_sources:"` | — |
| [SRC-59CF4B7DE8-L000519](../../agents/research.py#L519) | 519 | `"        warnings.append(\"تمت قراءة أقل من صفحتين مباشرة؛ بعض الأدلة مقتطفات من محركات البحث فقط.\")"` | — |
| [SRC-59CF4B7DE8-L000520](../../agents/research.py#L520) | 520 | `"    if freshness == \"current\":"` | — |
| [SRC-59CF4B7DE8-L000521](../../agents/research.py#L521) | 521 | `"        if not dates:"` | — |
| [SRC-59CF4B7DE8-L000522](../../agents/research.py#L522) | 522 | `"            warnings.append(\"لا تتوفر تواريخ نشر قابلة للتحليل؛ حداثة النتائج غير مؤكدة.\")"` | — |
| [SRC-59CF4B7DE8-L000523](../../agents/research.py#L523) | 523 | `"        elif recent_count == 0:"` | — |
| [SRC-59CF4B7DE8-L000524](../../agents/research.py#L524) | 524 | `"            warnings.append(f\"لم يُعثر على مصدر مؤرخ خلال آخر {recent_days} يومًا ضمن التواريخ القابلة للتحليل.\")"` | — |
| [SRC-59CF4B7DE8-L000525](../../agents/research.py#L525) | 525 | `"    if future_dates:"` | — |
| [SRC-59CF4B7DE8-L000526](../../agents/research.py#L526) | 526 | `"        warnings.append(\"توجد تواريخ مستقبلية غير متوقعة؛ يجب مراجعتها يدويًا.\")"` | — |
| [SRC-59CF4B7DE8-L000527](../../agents/research.py#L527) | 527 | `"    if social_count and primary_count == 0:"` | — |
| [SRC-59CF4B7DE8-L000528](../../agents/research.py#L528) | 528 | `"        warnings.append(\"المصادر اجتماعية فقط دون مصدر رسمي/أكاديمي؛ تعامل معها كآراء أو إشارات لا كحقائق مثبتة.\")"` | — |
| [SRC-59CF4B7DE8-L000529](../../agents/research.py#L529) | 529 | `"    return {"` | — |
| [SRC-59CF4B7DE8-L000530](../../agents/research.py#L530) | 530 | `"        \"unique_sources\": unique_sources,"` | — |
| [SRC-59CF4B7DE8-L000531](../../agents/research.py#L531) | 531 | `"        \"unique_domains\": len(domains),"` | — |
| [SRC-59CF4B7DE8-L000532](../../agents/research.py#L532) | 532 | `"        \"providers_count\": len(providers),"` | — |
| [SRC-59CF4B7DE8-L000533](../../agents/research.py#L533) | 533 | `"        \"providers\": sorted(providers),"` | — |
| [SRC-59CF4B7DE8-L000534](../../agents/research.py#L534) | 534 | `"        \"pages_read\": pages_read,"` | — |
| [SRC-59CF4B7DE8-L000535](../../agents/research.py#L535) | 535 | `"        \"primary_sources\": primary_count,"` | — |
| [SRC-59CF4B7DE8-L000536](../../agents/research.py#L536) | 536 | `"        \"news_sources\": news_count,"` | — |
| [SRC-59CF4B7DE8-L000537](../../agents/research.py#L537) | 537 | `"        \"social_sources\": social_count,"` | — |
| [SRC-59CF4B7DE8-L000538](../../agents/research.py#L538) | 538 | `"        \"dated_sources\": len(dates),"` | — |
| [SRC-59CF4B7DE8-L000539](../../agents/research.py#L539) | 539 | `"        \"recent_sources\": recent_count,"` | — |
| [SRC-59CF4B7DE8-L000540](../../agents/research.py#L540) | 540 | `"        \"undated_sources\": max(0, unique_sources - len(dates)),"` | — |
| [SRC-59CF4B7DE8-L000541](../../agents/research.py#L541) | 541 | `"        \"date_coverage_percent\": round(100 * len(dates) / unique_sources) if unique_sources else 0,"` | — |
| [SRC-59CF4B7DE8-L000542](../../agents/research.py#L542) | 542 | `"        \"coverage_score\": coverage_score,"` | — |
| [SRC-59CF4B7DE8-L000543](../../agents/research.py#L543) | 543 | `"        \"coverage_level\": coverage_level,"` | — |
| [SRC-59CF4B7DE8-L000544](../../agents/research.py#L544) | 544 | `"        \"score_meaning\": \"مؤشر تغطية وتنوع الأدلة، وليس احتمال صحة الإجابة.\","` | — |
| [SRC-59CF4B7DE8-L000545](../../agents/research.py#L545) | 545 | `"        \"warnings\": warnings,"` | — |
| [SRC-59CF4B7DE8-L000546](../../agents/research.py#L546) | 546 | `"    }"` | — |
| [SRC-59CF4B7DE8-L000547](../../agents/research.py#L547) | 547 | `""` | — |
| [SRC-59CF4B7DE8-L000548](../../agents/research.py#L548) | 548 | `""` | — |
| [SRC-59CF4B7DE8-L000549](../../agents/research.py#L549) | 549 | `""` | — |
| [SRC-59CF4B7DE8-L000550](../../agents/research.py#L550) | 550 | `"# ---------------------------------------------------------------------------"` | — |
| [SRC-59CF4B7DE8-L000551](../../agents/research.py#L551) | 551 | `"# Evidence-aware helpers"` | — |
| [SRC-59CF4B7DE8-L000552](../../agents/research.py#L552) | 552 | `"# ---------------------------------------------------------------------------"` | — |
| [SRC-59CF4B7DE8-L000553](../../agents/research.py#L553) | 553 | `""` | — |
| [SRC-59CF4B7DE8-L000554](../../agents/research.py#L554) | 554 | `"_RELEVANCE_STOPWORDS = {"` | — |
| [SRC-59CF4B7DE8-L000555](../../agents/research.py#L555) | 555 | `"    \"the\", \"a\", \"an\", \"of\", \"in\", \"on\", \"at\", \"to\", \"for\","` | — |
| [SRC-59CF4B7DE8-L000556](../../agents/research.py#L556) | 556 | `"    \"is\", \"are\", \"was\", \"were\", \"be\", \"been\", \"being\","` | — |
| [SRC-59CF4B7DE8-L000557](../../agents/research.py#L557) | 557 | `"    \"and\", \"or\", \"but\", \"not\", \"with\", \"without\","` | — |
| [SRC-59CF4B7DE8-L000558](../../agents/research.py#L558) | 558 | `"    \"this\", \"that\", \"these\", \"those\", \"it\", \"its\","` | — |
| [SRC-59CF4B7DE8-L000559](../../agents/research.py#L559) | 559 | `"}"` | — |
| [SRC-59CF4B7DE8-L000560](../../agents/research.py#L560) | 560 | `""` | — |
| [SRC-59CF4B7DE8-L000561](../../agents/research.py#L561) | 561 | `"_OFFICIAL_CLASSES = {\"government\", \"education\", \"official\"}"` | — |
| [SRC-59CF4B7DE8-L000562](../../agents/research.py#L562) | 562 | `""` | — |
| [SRC-59CF4B7DE8-L000563](../../agents/research.py#L563) | 563 | `""` | — |
| [SRC-59CF4B7DE8-L000564](../../agents/research.py#L564) | 564 | `"def _tokenize(text: str) -> set:"` | — |
| [SRC-59CF4B7DE8-L000565](../../agents/research.py#L565) | 565 | `"    if not text:"` | — |
| [SRC-59CF4B7DE8-L000566](../../agents/research.py#L566) | 566 | `"        return set()"` | — |
| [SRC-59CF4B7DE8-L000567](../../agents/research.py#L567) | 567 | `"    norm = _normalize_arabic(text.casefold())"` | — |
| [SRC-59CF4B7DE8-L000568](../../agents/research.py#L568) | 568 | `"    tokens = re.findall(r\"\\w+\", norm, flags=re.UNICODE)"` | — |
| [SRC-59CF4B7DE8-L000569](../../agents/research.py#L569) | 569 | `"    return {t for t in tokens if len(t) >= 3 and t not in _RELEVANCE_STOPWORDS}"` | — |
| [SRC-59CF4B7DE8-L000570](../../agents/research.py#L570) | 570 | `""` | — |
| [SRC-59CF4B7DE8-L000571](../../agents/research.py#L571) | 571 | `""` | — |
| [SRC-59CF4B7DE8-L000572](../../agents/research.py#L572) | 572 | `"def source_relevance_score(src, query: str) -> dict:"` | — |
| [SRC-59CF4B7DE8-L000573](../../agents/research.py#L573) | 573 | `"    if not isinstance(src, dict):"` | — |
| [SRC-59CF4B7DE8-L000574](../../agents/research.py#L574) | 574 | `"        return {\"accepted\": False, \"score\": 0, \"reason\": \"malformed\"}"` | — |
| [SRC-59CF4B7DE8-L000575](../../agents/research.py#L575) | 575 | `""` | — |
| [SRC-59CF4B7DE8-L000576](../../agents/research.py#L576) | 576 | `"    title = str(src.get(\"title\") or \"\")"` | — |
| [SRC-59CF4B7DE8-L000577](../../agents/research.py#L577) | 577 | `"    snippet = str(src.get(\"snippet\") or \"\")"` | — |
| [SRC-59CF4B7DE8-L000578](../../agents/research.py#L578) | 578 | `"    page_text = str(src.get(\"page_text\") or \"\")"` | — |
| [SRC-59CF4B7DE8-L000579](../../agents/research.py#L579) | 579 | `"    source_class = str(src.get(\"source_class\") or \"general\").lower()"` | — |
| [SRC-59CF4B7DE8-L000580](../../agents/research.py#L580) | 580 | `""` | — |
| [SRC-59CF4B7DE8-L000581](../../agents/research.py#L581) | 581 | `"    q_tokens = _tokenize(query)"` | — |
| [SRC-59CF4B7DE8-L000582](../../agents/research.py#L582) | 582 | `"    if not q_tokens:"` | — |
| [SRC-59CF4B7DE8-L000583](../../agents/research.py#L583) | 583 | `"        return {\"accepted\": False, \"score\": 0, \"reason\": \"no_query_tokens\"}"` | — |
| [SRC-59CF4B7DE8-L000584](../../agents/research.py#L584) | 584 | `""` | — |
| [SRC-59CF4B7DE8-L000585](../../agents/research.py#L585) | 585 | `"    t_tokens = _tokenize(title)"` | — |
| [SRC-59CF4B7DE8-L000586](../../agents/research.py#L586) | 586 | `"    s_tokens = _tokenize(snippet)"` | — |
| [SRC-59CF4B7DE8-L000587](../../agents/research.py#L587) | 587 | `"    p_tokens = _tokenize(page_text[:3000])"` | — |
| [SRC-59CF4B7DE8-L000588](../../agents/research.py#L588) | 588 | `""` | — |
| [SRC-59CF4B7DE8-L000589](../../agents/research.py#L589) | 589 | `"    title_ratio = len(q_tokens & t_tokens) / max(len(q_tokens), 1)"` | — |
| [SRC-59CF4B7DE8-L000590](../../agents/research.py#L590) | 590 | `"    snippet_ratio = len(q_tokens & s_tokens) / max(len(q_tokens), 1)"` | — |
| [SRC-59CF4B7DE8-L000591](../../agents/research.py#L591) | 591 | `"    page_ratio = len(q_tokens & p_tokens) / max(len(q_tokens), 1)"` | — |
| [SRC-59CF4B7DE8-L000592](../../agents/research.py#L592) | 592 | `""` | — |
| [SRC-59CF4B7DE8-L000593](../../agents/research.py#L593) | 593 | `"    score = int(title_ratio * 15 + snippet_ratio * 20 + page_ratio * 5)"` | — |
| [SRC-59CF4B7DE8-L000594](../../agents/research.py#L594) | 594 | `""` | — |
| [SRC-59CF4B7DE8-L000595](../../agents/research.py#L595) | 595 | `"    if source_class in _OFFICIAL_CLASSES:"` | — |
| [SRC-59CF4B7DE8-L000596](../../agents/research.py#L596) | 596 | `"        if score >= 5:"` | — |
| [SRC-59CF4B7DE8-L000597](../../agents/research.py#L597) | 597 | `"            return {\"accepted\": True, \"score\": score, \"reason\": \"accepted\"}"` | — |
| [SRC-59CF4B7DE8-L000598](../../agents/research.py#L598) | 598 | `"        return {\"accepted\": True, \"score\": score,"` | — |
| [SRC-59CF4B7DE8-L000599](../../agents/research.py#L599) | 599 | `"                \"reason\": \"kept_official_despite_low_overlap\"}"` | — |
| [SRC-59CF4B7DE8-L000600](../../agents/research.py#L600) | 600 | `""` | — |
| [SRC-59CF4B7DE8-L000601](../../agents/research.py#L601) | 601 | `"    if score >= 18:"` | — |
| [SRC-59CF4B7DE8-L000602](../../agents/research.py#L602) | 602 | `"        return {\"accepted\": True, \"score\": score, \"reason\": \"accepted\"}"` | — |
| [SRC-59CF4B7DE8-L000603](../../agents/research.py#L603) | 603 | `"    return {\"accepted\": False, \"score\": score, \"reason\": \"low_overlap\"}"` | — |
| [SRC-59CF4B7DE8-L000604](../../agents/research.py#L604) | 604 | `""` | — |
| [SRC-59CF4B7DE8-L000605](../../agents/research.py#L605) | 605 | `""` | — |
| [SRC-59CF4B7DE8-L000606](../../agents/research.py#L606) | 606 | `"def filter_relevant_sources(sources, query: str, extra_queries=None):"` | — |
| [SRC-59CF4B7DE8-L000607](../../agents/research.py#L607) | 607 | `"    kept = []"` | — |
| [SRC-59CF4B7DE8-L000608](../../agents/research.py#L608) | 608 | `"    diag = []"` | — |
| [SRC-59CF4B7DE8-L000609](../../agents/research.py#L609) | 609 | `"    seen_urls = set()"` | — |
| [SRC-59CF4B7DE8-L000610](../../agents/research.py#L610) | 610 | `"    seen_titles = set()"` | — |
| [SRC-59CF4B7DE8-L000611](../../agents/research.py#L611) | 611 | `"    combined = \" \".join([query] + list(extra_queries or []))"` | — |
| [SRC-59CF4B7DE8-L000612](../../agents/research.py#L612) | 612 | `""` | — |
| [SRC-59CF4B7DE8-L000613](../../agents/research.py#L613) | 613 | `"    for src in sources or []:"` | — |
| [SRC-59CF4B7DE8-L000614](../../agents/research.py#L614) | 614 | `"        if not isinstance(src, dict):"` | — |
| [SRC-59CF4B7DE8-L000615](../../agents/research.py#L615) | 615 | `"            diag.append({\"reason\": \"malformed\", \"url\": \"\"})"` | — |
| [SRC-59CF4B7DE8-L000616](../../agents/research.py#L616) | 616 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000617](../../agents/research.py#L617) | 617 | `"        url = str(src.get(\"url\") or \"\")"` | — |
| [SRC-59CF4B7DE8-L000618](../../agents/research.py#L618) | 618 | `"        domain = str(src.get(\"domain\") or \"\").lower()"` | — |
| [SRC-59CF4B7DE8-L000619](../../agents/research.py#L619) | 619 | `"        title = str(src.get(\"title\") or \"\").strip()"` | — |
| [SRC-59CF4B7DE8-L000620](../../agents/research.py#L620) | 620 | `"        url_key = url.rstrip(\"/\").lower()"` | — |
| [SRC-59CF4B7DE8-L000621](../../agents/research.py#L621) | 621 | `"        title_key = title.lower() + \"\|\" + domain"` | — |
| [SRC-59CF4B7DE8-L000622](../../agents/research.py#L622) | 622 | `""` | — |
| [SRC-59CF4B7DE8-L000623](../../agents/research.py#L623) | 623 | `"        if url_key and url_key in seen_urls:"` | — |
| [SRC-59CF4B7DE8-L000624](../../agents/research.py#L624) | 624 | `"            diag.append({\"reason\": \"duplicate_url\", \"url\": url})"` | — |
| [SRC-59CF4B7DE8-L000625](../../agents/research.py#L625) | 625 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000626](../../agents/research.py#L626) | 626 | `"        if title and title_key in seen_titles:"` | — |
| [SRC-59CF4B7DE8-L000627](../../agents/research.py#L627) | 627 | `"            diag.append({\"reason\": \"duplicate_title_domain\", \"url\": url})"` | — |
| [SRC-59CF4B7DE8-L000628](../../agents/research.py#L628) | 628 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000629](../../agents/research.py#L629) | 629 | `""` | — |
| [SRC-59CF4B7DE8-L000630](../../agents/research.py#L630) | 630 | `"        rel = source_relevance_score(src, combined)"` | — |
| [SRC-59CF4B7DE8-L000631](../../agents/research.py#L631) | 631 | `"        if not rel[\"accepted\"]:"` | — |
| [SRC-59CF4B7DE8-L000632](../../agents/research.py#L632) | 632 | `"            diag.append({\"reason\": rel[\"reason\"], \"url\": url, \"score\": rel[\"score\"]})"` | — |
| [SRC-59CF4B7DE8-L000633](../../agents/research.py#L633) | 633 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000634](../../agents/research.py#L634) | 634 | `""` | — |
| [SRC-59CF4B7DE8-L000635](../../agents/research.py#L635) | 635 | `"        kept.append(src)"` | — |
| [SRC-59CF4B7DE8-L000636](../../agents/research.py#L636) | 636 | `"        if url_key:"` | — |
| [SRC-59CF4B7DE8-L000637](../../agents/research.py#L637) | 637 | `"            seen_urls.add(url_key)"` | — |
| [SRC-59CF4B7DE8-L000638](../../agents/research.py#L638) | 638 | `"        if title:"` | — |
| [SRC-59CF4B7DE8-L000639](../../agents/research.py#L639) | 639 | `"            seen_titles.add(title_key)"` | — |
| [SRC-59CF4B7DE8-L000640](../../agents/research.py#L640) | 640 | `"    return kept, diag"` | — |
| [SRC-59CF4B7DE8-L000641](../../agents/research.py#L641) | 641 | `""` | — |
| [SRC-59CF4B7DE8-L000642](../../agents/research.py#L642) | 642 | `""` | — |
| [SRC-59CF4B7DE8-L000643](../../agents/research.py#L643) | 643 | `"def decide_evidence_status(sources, pages_read: int = 0,"` | — |
| [SRC-59CF4B7DE8-L000644](../../agents/research.py#L644) | 644 | `"                           provider_failures: int = 0,"` | — |
| [SRC-59CF4B7DE8-L000645](../../agents/research.py#L645) | 645 | `"                           search_attempted: bool = True) -> dict:"` | — |
| [SRC-59CF4B7DE8-L000646](../../agents/research.py#L646) | 646 | `"    if not search_attempted:"` | — |
| [SRC-59CF4B7DE8-L000647](../../agents/research.py#L647) | 647 | `"        return {\"evidence_status\": \"failed\", \"should_abstain\": True}"` | — |
| [SRC-59CF4B7DE8-L000648](../../agents/research.py#L648) | 648 | `""` | — |
| [SRC-59CF4B7DE8-L000649](../../agents/research.py#L649) | 649 | `"    domains = set()"` | — |
| [SRC-59CF4B7DE8-L000650](../../agents/research.py#L650) | 650 | `"    has_official = False"` | — |
| [SRC-59CF4B7DE8-L000651](../../agents/research.py#L651) | 651 | `"    for s in sources or []:"` | — |
| [SRC-59CF4B7DE8-L000652](../../agents/research.py#L652) | 652 | `"        if not isinstance(s, dict):"` | — |
| [SRC-59CF4B7DE8-L000653](../../agents/research.py#L653) | 653 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000654](../../agents/research.py#L654) | 654 | `"        d = str(s.get(\"domain\") or \"\").lower()"` | — |
| [SRC-59CF4B7DE8-L000655](../../agents/research.py#L655) | 655 | `"        if not d:"` | — |
| [SRC-59CF4B7DE8-L000656](../../agents/research.py#L656) | 656 | `"            url = str(s.get(\"url\") or \"\")"` | — |
| [SRC-59CF4B7DE8-L000657](../../agents/research.py#L657) | 657 | `"            if url:"` | — |
| [SRC-59CF4B7DE8-L000658](../../agents/research.py#L658) | 658 | `"                try:"` | — |
| [SRC-59CF4B7DE8-L000659](../../agents/research.py#L659) | 659 | `"                    from urllib.parse import urlparse"` | — |
| [SRC-59CF4B7DE8-L000660](../../agents/research.py#L660) | 660 | `"                    d = urlparse(url).netloc.lower()"` | — |
| [SRC-59CF4B7DE8-L000661](../../agents/research.py#L661) | 661 | `"                except Exception:"` | — |
| [SRC-59CF4B7DE8-L000662](../../agents/research.py#L662) | 662 | `"                    d = \"\""` | — |
| [SRC-59CF4B7DE8-L000663](../../agents/research.py#L663) | 663 | `"        if d:"` | — |
| [SRC-59CF4B7DE8-L000664](../../agents/research.py#L664) | 664 | `"            domains.add(d)"` | — |
| [SRC-59CF4B7DE8-L000665](../../agents/research.py#L665) | 665 | `"        if str(s.get(\"source_class\") or \"\").lower() in _OFFICIAL_CLASSES:"` | — |
| [SRC-59CF4B7DE8-L000666](../../agents/research.py#L666) | 666 | `"            has_official = True"` | — |
| [SRC-59CF4B7DE8-L000667](../../agents/research.py#L667) | 667 | `""` | — |
| [SRC-59CF4B7DE8-L000668](../../agents/research.py#L668) | 668 | `"    if not sources:"` | — |
| [SRC-59CF4B7DE8-L000669](../../agents/research.py#L669) | 669 | `"        if provider_failures > 0:"` | — |
| [SRC-59CF4B7DE8-L000670](../../agents/research.py#L670) | 670 | `"            return {\"evidence_status\": \"failed\", \"should_abstain\": True}"` | — |
| [SRC-59CF4B7DE8-L000671](../../agents/research.py#L671) | 671 | `"        return {\"evidence_status\": \"insufficient\", \"should_abstain\": True}"` | — |
| [SRC-59CF4B7DE8-L000672](../../agents/research.py#L672) | 672 | `""` | — |
| [SRC-59CF4B7DE8-L000673](../../agents/research.py#L673) | 673 | `"    if len(domains) >= 2 or has_official:"` | — |
| [SRC-59CF4B7DE8-L000674](../../agents/research.py#L674) | 674 | `"        return {\"evidence_status\": \"adequate\", \"should_abstain\": False}"` | — |
| [SRC-59CF4B7DE8-L000675](../../agents/research.py#L675) | 675 | `"    if len(domains) >= 1:"` | — |
| [SRC-59CF4B7DE8-L000676](../../agents/research.py#L676) | 676 | `"        return {\"evidence_status\": \"partial\", \"should_abstain\": False}"` | — |
| [SRC-59CF4B7DE8-L000677](../../agents/research.py#L677) | 677 | `"    return {\"evidence_status\": \"insufficient\", \"should_abstain\": True}"` | — |
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
| [SRC-1AE03B9EC3-L000024](../../agents/web_agent.py#L24) | 24 | `"from agents.intent_router import route_intent"` | — |
| [SRC-1AE03B9EC3-L000025](../../agents/web_agent.py#L25) | 25 | `"from agents.answer_validation import audit_answer_integrity"` | — |
| [SRC-1AE03B9EC3-L000026](../../agents/web_agent.py#L26) | 26 | `"from agents.request_budget import RequestBudget, RequestBudgetExceeded"` | — |
| [SRC-1AE03B9EC3-L000027](../../agents/web_agent.py#L27) | 27 | `"from agents.research import ("` | — |
| [SRC-1AE03B9EC3-L000028](../../agents/web_agent.py#L28) | 28 | `"    MAX_PLAN_QUERIES,"` | — |
| [SRC-1AE03B9EC3-L000029](../../agents/web_agent.py#L29) | 29 | `"    SOCIAL_DOMAINS,"` | — |
| [SRC-1AE03B9EC3-L000030](../../agents/web_agent.py#L30) | 30 | `"    evidence_signal_report,"` | — |
| [SRC-1AE03B9EC3-L000031](../../agents/web_agent.py#L31) | 31 | `"    fallback_plan,"` | — |
| [SRC-1AE03B9EC3-L000032](../../agents/web_agent.py#L32) | 32 | `"    fuse_ranked_results,"` | — |
| [SRC-1AE03B9EC3-L000033](../../agents/web_agent.py#L33) | 33 | `"    registrable_domain,"` | — |
| [SRC-1AE03B9EC3-L000034](../../agents/web_agent.py#L34) | 34 | `"    validate_plan,"` | — |
| [SRC-1AE03B9EC3-L000035](../../agents/web_agent.py#L35) | 35 | `")"` | — |
| [SRC-1AE03B9EC3-L000036](../../agents/web_agent.py#L36) | 36 | `""` | — |
| [SRC-1AE03B9EC3-L000037](../../agents/web_agent.py#L37) | 37 | `"MAX_QUESTION_CHARS = 4000"` | — |
| [SRC-1AE03B9EC3-L000038](../../agents/web_agent.py#L38) | 38 | `"MAX_HISTORY_ITEMS = 8"` | — |
| [SRC-1AE03B9EC3-L000039](../../agents/web_agent.py#L39) | 39 | `"MAX_HISTORY_CHARS = 4000"` | — |
| [SRC-1AE03B9EC3-L000040](../../agents/web_agent.py#L40) | 40 | `"MAX_SEARCH_RESULTS = 18"` | — |
| [SRC-1AE03B9EC3-L000041](../../agents/web_agent.py#L41) | 41 | `"MAX_PROVIDER_RESULTS = 6"` | — |
| [SRC-1AE03B9EC3-L000042](../../agents/web_agent.py#L42) | 42 | `"MAX_FETCHED_PAGES = 8"` | — |
| [SRC-1AE03B9EC3-L000043](../../agents/web_agent.py#L43) | 43 | `"MAX_LLM_CITED_SOURCES = 12"` | — |
| [SRC-1AE03B9EC3-L000044](../../agents/web_agent.py#L44) | 44 | `"MAX_RESEARCH_WORKERS = 8"` | — |
| [SRC-1AE03B9EC3-L000045](../../agents/web_agent.py#L45) | 45 | `"MAX_PAGE_BYTES = 1_000_000"` | — |
| [SRC-1AE03B9EC3-L000046](../../agents/web_agent.py#L46) | 46 | `"MAX_PAGE_TEXT_CHARS = 12_000"` | — |
| [SRC-1AE03B9EC3-L000047](../../agents/web_agent.py#L47) | 47 | `"LLM_TIMEOUT_SECONDS = 35"` | — |
| [SRC-1AE03B9EC3-L000048](../../agents/web_agent.py#L48) | 48 | `""` | — |
| [SRC-1AE03B9EC3-L000049](../../agents/web_agent.py#L49) | 49 | `"# Only completed connector result-processing states positively confirm an attempt."` | — |
| [SRC-1AE03B9EC3-L000050](../../agents/web_agent.py#L50) | 50 | `"# A generic \"failed\" or timeout diagnostic may occur before a network request is sent."` | — |
| [SRC-1AE03B9EC3-L000051](../../agents/web_agent.py#L51) | 51 | `"_SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES = frozenset({\"ok\", \"no_results\", \"filtered_all\"})"` | — |
| [SRC-1AE03B9EC3-L000052](../../agents/web_agent.py#L52) | 52 | `"_RESEARCH_ERROR_OUTCOMES = frozenset({\"attempted_research_error\", \"unknown_after_research_error\"})"` | — |
| [SRC-1AE03B9EC3-L000053](../../agents/web_agent.py#L53) | 53 | `""` | — |
| [SRC-1AE03B9EC3-L000054](../../agents/web_agent.py#L54) | 54 | `""` | — |
| [SRC-1AE03B9EC3-L000055](../../agents/web_agent.py#L55) | 55 | `"_ARABIC_SEARCH_TRANSLATION = str.maketrans({"` | — |
| [SRC-1AE03B9EC3-L000056](../../agents/web_agent.py#L56) | 56 | `"    \"أ\": \"ا\", \"إ\": \"ا\", \"آ\": \"ا\", \"ٱ\": \"ا\", \"ى\": \"ي\","` | — |
| [SRC-1AE03B9EC3-L000057](../../agents/web_agent.py#L57) | 57 | `"    \"ؤ\": \"و\", \"ئ\": \"ي\", \"ة\": \"ه\", \"ـ\": \"\","` | — |
| [SRC-1AE03B9EC3-L000058](../../agents/web_agent.py#L58) | 58 | `"})"` | — |
| [SRC-1AE03B9EC3-L000059](../../agents/web_agent.py#L59) | 59 | `"_ARABIC_DIACRITICS_RE = re.compile(r\"[\\u0610-\\u061A\\u064B-\\u065F\\u0670\\u06D6-\\u06ED]\")"` | — |
| [SRC-1AE03B9EC3-L000060](../../agents/web_agent.py#L60) | 60 | `"_SEARCH_STOPWORDS = frozenset({"` | — |
| [SRC-1AE03B9EC3-L000061](../../agents/web_agent.py#L61) | 61 | `"    \"ما\", \"ماذا\", \"من\", \"في\", \"على\", \"عن\", \"الى\", \"إلى\", \"و\", \"او\", \"أو\","` | — |
| [SRC-1AE03B9EC3-L000062](../../agents/web_agent.py#L62) | 62 | `"    \"هل\", \"هو\", \"هي\", \"هذا\", \"هذه\", \"ذلك\", \"تلك\", \"التي\", \"الذي\", \"مع\","` | — |
| [SRC-1AE03B9EC3-L000063](../../agents/web_agent.py#L63) | 63 | `"    \"بين\", \"كيف\", \"لماذا\", \"كم\", \"كان\", \"كانت\", \"يكون\", \"تكون\", \"لي\","` | — |
| [SRC-1AE03B9EC3-L000064](../../agents/web_agent.py#L64) | 64 | `"    \"the\", \"a\", \"an\", \"and\", \"or\", \"in\", \"on\", \"of\", \"to\", \"for\", \"with\","` | — |
| [SRC-1AE03B9EC3-L000065](../../agents/web_agent.py#L65) | 65 | `"    \"is\", \"are\", \"was\", \"were\", \"what\", \"which\", \"who\", \"how\", \"why\", \"when\","` | — |
| [SRC-1AE03B9EC3-L000066](../../agents/web_agent.py#L66) | 66 | `"    \"where\", \"compare\", \"comparison\", \"please\", \"show\", \"find\", \"latest\","` | — |
| [SRC-1AE03B9EC3-L000067](../../agents/web_agent.py#L67) | 67 | `"    \"news\", \"official\", \"sources\", \"source\", \"reports\", \"report\", \"analysis\","` | — |
| [SRC-1AE03B9EC3-L000068](../../agents/web_agent.py#L68) | 68 | `"    \"site\", \"com\", \"org\", \"net\", \"www\","` | — |
| [SRC-1AE03B9EC3-L000069](../../agents/web_agent.py#L69) | 69 | `"})"` | — |
| [SRC-1AE03B9EC3-L000070](../../agents/web_agent.py#L70) | 70 | `"_SEARCH_SYNONYMS = {"` | — |
| [SRC-1AE03B9EC3-L000071](../../agents/web_agent.py#L71) | 71 | `"    \"استراليا\": {\"australia\"}, \"عاصمة\": {\"capital\"}, \"مصر\": {\"egypt\"},"` | — |
| [SRC-1AE03B9EC3-L000072](../../agents/web_agent.py#L72) | 72 | `"    \"المصري\": {\"egyptian\", \"egypt\"}, \"مركزي\": {\"central\"},"` | — |
| [SRC-1AE03B9EC3-L000073](../../agents/web_agent.py#L73) | 73 | `"    \"المركزي\": {\"central\"}, \"بنك\": {\"bank\"}, \"البنك\": {\"bank\"},"` | — |
| [SRC-1AE03B9EC3-L000074](../../agents/web_agent.py#L74) | 74 | `"    \"قرار\": {\"decision\"}, \"قرارات\": {\"decision\", \"decisions\"},"` | — |
| [SRC-1AE03B9EC3-L000075](../../agents/web_agent.py#L75) | 75 | `"    \"سعر\": {\"price\"}, \"اسعار\": {\"prices\"}, \"استضافة\": {\"hosting\"},"` | — |
| [SRC-1AE03B9EC3-L000076](../../agents/web_agent.py#L76) | 76 | `"    \"شركة\": {\"company\"}, \"شركه\": {\"company\"}, \"ناشئة\": {\"startup\"},"` | — |
| [SRC-1AE03B9EC3-L000077](../../agents/web_agent.py#L77) | 77 | `"    \"صعيد\": {\"upper\"}, \"مقارنة\": {\"compare\", \"comparison\"},"` | — |
| [SRC-1AE03B9EC3-L000078](../../agents/web_agent.py#L78) | 78 | `"    \"تقنية\": {\"technology\"}, \"تقنيات\": {\"technology\"},"` | — |
| [SRC-1AE03B9EC3-L000079](../../agents/web_agent.py#L79) | 79 | `"    \"ميكروسوفت\": {\"microsoft\"}, \"مايكروسوفت\": {\"microsoft\"},"` | — |
| [SRC-1AE03B9EC3-L000080](../../agents/web_agent.py#L80) | 80 | `"    \"microsoft\": {\"ميكروسوفت\", \"مايكروسوفت\"},"` | — |
| [SRC-1AE03B9EC3-L000081](../../agents/web_agent.py#L81) | 81 | `"    \"جمهورية\": {\"republic\"}, \"republic\": {\"جمهورية\"},"` | — |
| [SRC-1AE03B9EC3-L000082](../../agents/web_agent.py#L82) | 82 | `"    \"الرقمية\": {\"digital\"}, \"رقمية\": {\"digital\"},"` | — |
| [SRC-1AE03B9EC3-L000083](../../agents/web_agent.py#L83) | 83 | `"    \"الرقميه\": {\"digital\"}, \"رقميه\": {\"digital\"},"` | — |
| [SRC-1AE03B9EC3-L000084](../../agents/web_agent.py#L84) | 84 | `"    \"موقع\": {\"website\", \"portal\"}, \"مواقع\": {\"websites\", \"portals\"},"` | — |
| [SRC-1AE03B9EC3-L000085](../../agents/web_agent.py#L85) | 85 | `"    \"التجمع\": {\"settlement\"}, \"تجمع\": {\"settlement\"},"` | — |
| [SRC-1AE03B9EC3-L000086](../../agents/web_agent.py#L86) | 86 | `"    \"الخامس\": {\"fifth\", \"5th\"}, \"خامس\": {\"fifth\", \"5th\"},"` | — |
| [SRC-1AE03B9EC3-L000087](../../agents/web_agent.py#L87) | 87 | `"    \"شقة\": {\"apartment\", \"flat\"}, \"شقق\": {\"apartments\", \"flats\"},"` | — |
| [SRC-1AE03B9EC3-L000088](../../agents/web_agent.py#L88) | 88 | `"    \"عميل\": {\"customer\", \"buyer\"}, \"عملاء\": {\"customers\", \"buyers\"},"` | — |
| [SRC-1AE03B9EC3-L000089](../../agents/web_agent.py#L89) | 89 | `"    \"شراء\": {\"buy\", \"purchase\"}, \"مشتري\": {\"buyer\"},"` | — |
| [SRC-1AE03B9EC3-L000090](../../agents/web_agent.py#L90) | 90 | `"}"` | — |
| [SRC-1AE03B9EC3-L000091](../../agents/web_agent.py#L91) | 91 | `"_CALENDAR_MONTHS = ("` | — |
| [SRC-1AE03B9EC3-L000092](../../agents/web_agent.py#L92) | 92 | `"    \"يناير\", \"فبراير\", \"مارس\", \"ابريل\", \"أبريل\", \"مايو\", \"يونيو\","` | — |
| [SRC-1AE03B9EC3-L000093](../../agents/web_agent.py#L93) | 93 | `"    \"يوليو\", \"اغسطس\", \"أغسطس\", \"سبتمبر\", \"اكتوبر\", \"أكتوبر\","` | — |
| [SRC-1AE03B9EC3-L000094](../../agents/web_agent.py#L94) | 94 | `"    \"نوفمبر\", \"ديسمبر\", \"january\", \"february\", \"march\", \"april\","` | — |
| [SRC-1AE03B9EC3-L000095](../../agents/web_agent.py#L95) | 95 | `"    \"may\", \"june\", \"july\", \"august\", \"september\", \"october\","` | — |
| [SRC-1AE03B9EC3-L000096](../../agents/web_agent.py#L96) | 96 | `"    \"november\", \"december\","` | — |
| [SRC-1AE03B9EC3-L000097](../../agents/web_agent.py#L97) | 97 | `")"` | — |
| [SRC-1AE03B9EC3-L000098](../../agents/web_agent.py#L98) | 98 | `"_BLOCKED_SOURCE_DOMAINS = frozenset({"` | — |
| [SRC-1AE03B9EC3-L000099](../../agents/web_agent.py#L99) | 99 | `"    \"translate.google.com\", \"translate.googleusercontent.com\","` | — |
| [SRC-1AE03B9EC3-L000100](../../agents/web_agent.py#L100) | 100 | `"})"` | — |
| [SRC-1AE03B9EC3-L000101](../../agents/web_agent.py#L101) | 101 | `""` | — |
| [SRC-1AE03B9EC3-L000102](../../agents/web_agent.py#L102) | 102 | `""` | — |
| [SRC-1AE03B9EC3-L000103](../../agents/web_agent.py#L103) | 103 | `"def _normalize_search_query(value: str) -> str:"` | — |
| [SRC-1AE03B9EC3-L000104](../../agents/web_agent.py#L104) | 104 | `"    \"\"\"Normalize Arabic letters/diacritics while preserving search operators and dates.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000105](../../agents/web_agent.py#L105) | 105 | `"    value = unicodedata.normalize(\"NFKC\", value or \"\")"` | — |
| [SRC-1AE03B9EC3-L000106](../../agents/web_agent.py#L106) | 106 | `"    value = _ARABIC_DIACRITICS_RE.sub(\"\", value).translate(_ARABIC_SEARCH_TRANSLATION)"` | — |
| [SRC-1AE03B9EC3-L000107](../../agents/web_agent.py#L107) | 107 | `"    return re.sub(r\"\\s+\", \" \", value).strip()"` | — |
| [SRC-1AE03B9EC3-L000108](../../agents/web_agent.py#L108) | 108 | `""` | — |
| [SRC-1AE03B9EC3-L000109](../../agents/web_agent.py#L109) | 109 | `""` | — |
| [SRC-1AE03B9EC3-L000110](../../agents/web_agent.py#L110) | 110 | `"# Normalize synonym keys and values by the same rules as search text. This avoids"` | — |
| [SRC-1AE03B9EC3-L000111](../../agents/web_agent.py#L111) | 111 | `"# Arabic ta-marbuta/alif variants silently disabling Arabic-to-English matching."` | — |
| [SRC-1AE03B9EC3-L000112](../../agents/web_agent.py#L112) | 112 | `"_NORMALIZED_SEARCH_SYNONYMS: dict[str, set[str]] = {}"` | — |
| [SRC-1AE03B9EC3-L000113](../../agents/web_agent.py#L113) | 113 | `"for _synonym_key, _synonym_values in _SEARCH_SYNONYMS.items():"` | — |
| [SRC-1AE03B9EC3-L000114](../../agents/web_agent.py#L114) | 114 | `"    _normalized_key = _normalize_search_query(_synonym_key).casefold()"` | — |
| [SRC-1AE03B9EC3-L000115](../../agents/web_agent.py#L115) | 115 | `"    _NORMALIZED_SEARCH_SYNONYMS.setdefault(_normalized_key, set()).update("` | — |
| [SRC-1AE03B9EC3-L000116](../../agents/web_agent.py#L116) | 116 | `"        _normalize_search_query(value).casefold() for value in _synonym_values"` | — |
| [SRC-1AE03B9EC3-L000117](../../agents/web_agent.py#L117) | 117 | `"    )"` | — |
| [SRC-1AE03B9EC3-L000118](../../agents/web_agent.py#L118) | 118 | `""` | — |
| [SRC-1AE03B9EC3-L000119](../../agents/web_agent.py#L119) | 119 | `""` | — |
| [SRC-1AE03B9EC3-L000120](../../agents/web_agent.py#L120) | 120 | `"def _search_tokens(value: str) -> set[str]:"` | — |
| [SRC-1AE03B9EC3-L000121](../../agents/web_agent.py#L121) | 121 | `"    \"\"\"Tokenize Arabic/English text and expand a small bilingual vocabulary.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000122](../../agents/web_agent.py#L122) | 122 | `"    value = _normalize_search_query(value).casefold()"` | — |
| [SRC-1AE03B9EC3-L000123](../../agents/web_agent.py#L123) | 123 | `"    value = re.sub(r\"(?i)\\bsite\\s*:\\s*\\S+\", \" \", value)"` | — |
| [SRC-1AE03B9EC3-L000124](../../agents/web_agent.py#L124) | 124 | `"    tokens = re.findall(r\"[a-z0-9]+\|[\\u0600-\\u06FF]+\", value)"` | — |
| [SRC-1AE03B9EC3-L000125](../../agents/web_agent.py#L125) | 125 | `"    result: set[str] = set()"` | — |
| [SRC-1AE03B9EC3-L000126](../../agents/web_agent.py#L126) | 126 | `"    for token in tokens:"` | — |
| [SRC-1AE03B9EC3-L000127](../../agents/web_agent.py#L127) | 127 | `"        if token in _SEARCH_STOPWORDS or len(token) < 2:"` | — |
| [SRC-1AE03B9EC3-L000128](../../agents/web_agent.py#L128) | 128 | `"            continue"` | — |
| [SRC-1AE03B9EC3-L000129](../../agents/web_agent.py#L129) | 129 | `"        forms = {token}"` | — |
| [SRC-1AE03B9EC3-L000130](../../agents/web_agent.py#L130) | 130 | `"        if token.startswith(\"ال\") and len(token) > 4:"` | — |
| [SRC-1AE03B9EC3-L000131](../../agents/web_agent.py#L131) | 131 | `"            forms.add(token[2:])"` | — |
| [SRC-1AE03B9EC3-L000132](../../agents/web_agent.py#L132) | 132 | `"        forms.update(_NORMALIZED_SEARCH_SYNONYMS.get(token, set()))"` | — |
| [SRC-1AE03B9EC3-L000133](../../agents/web_agent.py#L133) | 133 | `"        # Reverse-map common English equivalents so Arabic and English results can match."` | — |
| [SRC-1AE03B9EC3-L000134](../../agents/web_agent.py#L134) | 134 | `"        for arabic, english in _NORMALIZED_SEARCH_SYNONYMS.items():"` | — |
| [SRC-1AE03B9EC3-L000135](../../agents/web_agent.py#L135) | 135 | `"            if token in english:"` | — |
| [SRC-1AE03B9EC3-L000136](../../agents/web_agent.py#L136) | 136 | `"                forms.add(arabic)"` | — |
| [SRC-1AE03B9EC3-L000137](../../agents/web_agent.py#L137) | 137 | `"                if arabic.startswith(\"ال\") and len(arabic) > 4:"` | — |
| [SRC-1AE03B9EC3-L000138](../../agents/web_agent.py#L138) | 138 | `"                    forms.add(arabic[2:])"` | — |
| [SRC-1AE03B9EC3-L000139](../../agents/web_agent.py#L139) | 139 | `"        result.update(forms)"` | — |
| [SRC-1AE03B9EC3-L000140](../../agents/web_agent.py#L140) | 140 | `"    return result"` | — |
| [SRC-1AE03B9EC3-L000141](../../agents/web_agent.py#L141) | 141 | `""` | — |
| [SRC-1AE03B9EC3-L000142](../../agents/web_agent.py#L142) | 142 | `""` | — |
| [SRC-1AE03B9EC3-L000143](../../agents/web_agent.py#L143) | 143 | `"def _relevance_ratio(query: str, evidence: str) -> float:"` | — |
| [SRC-1AE03B9EC3-L000144](../../agents/web_agent.py#L144) | 144 | `"    \"\"\"Fraction of meaningful query concepts present in a candidate's title/snippet.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000145](../../agents/web_agent.py#L145) | 145 | `"    query_text = _normalize_search_query(query).casefold()"` | — |
| [SRC-1AE03B9EC3-L000146](../../agents/web_agent.py#L146) | 146 | `"    query_text = re.sub(r\"(?i)\\bsite\\s*:\\s*\\S+\", \" \", query_text)"` | — |
| [SRC-1AE03B9EC3-L000147](../../agents/web_agent.py#L147) | 147 | `"    query_tokens = {"` | — |
| [SRC-1AE03B9EC3-L000148](../../agents/web_agent.py#L148) | 148 | `"        token for token in re.findall(r\"[a-z0-9]+\|[\\u0600-\\u06FF]+\", query_text)"` | — |
| [SRC-1AE03B9EC3-L000149](../../agents/web_agent.py#L149) | 149 | `"        if token not in _SEARCH_STOPWORDS and len(token) >= 2"` | — |
| [SRC-1AE03B9EC3-L000150](../../agents/web_agent.py#L150) | 150 | `"    }"` | — |
| [SRC-1AE03B9EC3-L000151](../../agents/web_agent.py#L151) | 151 | `"    if not query_tokens:"` | — |
| [SRC-1AE03B9EC3-L000152](../../agents/web_agent.py#L152) | 152 | `"        return 1.0"` | — |
| [SRC-1AE03B9EC3-L000153](../../agents/web_agent.py#L153) | 153 | `"    expanded_evidence = _search_tokens(evidence)"` | — |
| [SRC-1AE03B9EC3-L000154](../../agents/web_agent.py#L154) | 154 | `"    matched = sum("` | — |
| [SRC-1AE03B9EC3-L000155](../../agents/web_agent.py#L155) | 155 | `"        1 for token in query_tokens"` | — |
| [SRC-1AE03B9EC3-L000156](../../agents/web_agent.py#L156) | 156 | `"        if token in expanded_evidence"` | — |
| [SRC-1AE03B9EC3-L000157](../../agents/web_agent.py#L157) | 157 | `"        or (token.startswith(\"ال\") and token[2:] in expanded_evidence)"` | — |
| [SRC-1AE03B9EC3-L000158](../../agents/web_agent.py#L158) | 158 | `"        or bool(_NORMALIZED_SEARCH_SYNONYMS.get(token, set()) & expanded_evidence)"` | — |
| [SRC-1AE03B9EC3-L000159](../../agents/web_agent.py#L159) | 159 | `"    )"` | — |
| [SRC-1AE03B9EC3-L000160](../../agents/web_agent.py#L160) | 160 | `"    ratio = matched / len(query_tokens)"` | — |
| [SRC-1AE03B9EC3-L000161](../../agents/web_agent.py#L161) | 161 | `"    # A single generic overlap is not enough for a longer query."` | — |
| [SRC-1AE03B9EC3-L000162](../../agents/web_agent.py#L162) | 162 | `"    if len(query_tokens) >= 4 and matched < 2:"` | — |
| [SRC-1AE03B9EC3-L000163](../../agents/web_agent.py#L163) | 163 | `"        return 0.0"` | — |
| [SRC-1AE03B9EC3-L000164](../../agents/web_agent.py#L164) | 164 | `"    return ratio"` | — |
| [SRC-1AE03B9EC3-L000165](../../agents/web_agent.py#L165) | 165 | `""` | — |
| [SRC-1AE03B9EC3-L000166](../../agents/web_agent.py#L166) | 166 | `""` | — |
| [SRC-1AE03B9EC3-L000167](../../agents/web_agent.py#L167) | 167 | `"def _blocked_source_url(url: str) -> bool:"` | — |
| [SRC-1AE03B9EC3-L000168](../../agents/web_agent.py#L168) | 168 | `"    try:"` | — |
| [SRC-1AE03B9EC3-L000169](../../agents/web_agent.py#L169) | 169 | `"        host = (urllib.parse.urlparse(url).hostname or \"\").lower().rstrip(\".\")"` | — |
| [SRC-1AE03B9EC3-L000170](../../agents/web_agent.py#L170) | 170 | `"        return any(host == domain or host.endswith(\".\" + domain) for domain in _BLOCKED_SOURCE_DOMAINS)"` | — |
| [SRC-1AE03B9EC3-L000171](../../agents/web_agent.py#L171) | 171 | `"    except (TypeError, ValueError):"` | — |
| [SRC-1AE03B9EC3-L000172](../../agents/web_agent.py#L172) | 172 | `"        return True"` | — |
| [SRC-1AE03B9EC3-L000173](../../agents/web_agent.py#L173) | 173 | `""` | — |
| [SRC-1AE03B9EC3-L000174](../../agents/web_agent.py#L174) | 174 | `""` | — |
| [SRC-1AE03B9EC3-L000175](../../agents/web_agent.py#L175) | 175 | `"class AgentDependencyError(RuntimeError):"` | — |
| [SRC-1AE03B9EC3-L000176](../../agents/web_agent.py#L176) | 176 | `"    \"\"\"A required optional runtime dependency is unavailable.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000177](../../agents/web_agent.py#L177) | 177 | `""` | — |
| [SRC-1AE03B9EC3-L000178](../../agents/web_agent.py#L178) | 178 | `""` | — |
| [SRC-1AE03B9EC3-L000179](../../agents/web_agent.py#L179) | 179 | `"def _clean_text(value: Any, limit: int) -> str:"` | — |
| [SRC-1AE03B9EC3-L000180](../../agents/web_agent.py#L180) | 180 | `"    if not isinstance(value, str):"` | — |
| [SRC-1AE03B9EC3-L000181](../../agents/web_agent.py#L181) | 181 | `"        return \"\""` | — |
| [SRC-1AE03B9EC3-L000182](../../agents/web_agent.py#L182) | 182 | `"    return \" \".join(value.replace(\"\\x00\", \" \").split())[:limit]"` | — |
| [SRC-1AE03B9EC3-L000183](../../agents/web_agent.py#L183) | 183 | `""` | — |
| [SRC-1AE03B9EC3-L000184](../../agents/web_agent.py#L184) | 184 | `""` | — |
| [SRC-1AE03B9EC3-L000185](../../agents/web_agent.py#L185) | 185 | `"def _public_http_url(value: Any) -> str \| None:"` | — |
| [SRC-1AE03B9EC3-L000186](../../agents/web_agent.py#L186) | 186 | `"    \"\"\"Lexically validate an HTTP URL before using it as a search source.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000187](../../agents/web_agent.py#L187) | 187 | `"    if not isinstance(value, str) or len(value) > 2048:"` | — |
| [SRC-1AE03B9EC3-L000188](../../agents/web_agent.py#L188) | 188 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000189](../../agents/web_agent.py#L189) | 189 | `"    try:"` | — |
| [SRC-1AE03B9EC3-L000190](../../agents/web_agent.py#L190) | 190 | `"        parsed = urllib.parse.urlparse(value.strip())"` | — |
| [SRC-1AE03B9EC3-L000191](../../agents/web_agent.py#L191) | 191 | `"        if parsed.scheme not in {\"http\", \"https\"}:"` | — |
| [SRC-1AE03B9EC3-L000192](../../agents/web_agent.py#L192) | 192 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L000193](../../agents/web_agent.py#L193) | 193 | `"        if not parsed.hostname or parsed.username is not None or parsed.password is not None:"` | — |
| [SRC-1AE03B9EC3-L000194](../../agents/web_agent.py#L194) | 194 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L000195](../../agents/web_agent.py#L195) | 195 | `"        if parsed.port not in (None, 80, 443):"` | — |
| [SRC-1AE03B9EC3-L000196](../../agents/web_agent.py#L196) | 196 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L000197](../../agents/web_agent.py#L197) | 197 | `"        host = parsed.hostname.rstrip(\".\").lower()"` | — |
| [SRC-1AE03B9EC3-L000198](../../agents/web_agent.py#L198) | 198 | `"        if not host or host in {\"localhost\"} or host.endswith((\".local\", \".internal\", \".localhost\")):"` | — |
| [SRC-1AE03B9EC3-L000199](../../agents/web_agent.py#L199) | 199 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L000200](../../agents/web_agent.py#L200) | 200 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L000201](../../agents/web_agent.py#L201) | 201 | `"            ip = ipaddress.ip_address(host)"` | — |
| [SRC-1AE03B9EC3-L000202](../../agents/web_agent.py#L202) | 202 | `"        except ValueError:"` | — |
| [SRC-1AE03B9EC3-L000203](../../agents/web_agent.py#L203) | 203 | `"            pass"` | — |
| [SRC-1AE03B9EC3-L000204](../../agents/web_agent.py#L204) | 204 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L000205](../../agents/web_agent.py#L205) | 205 | `"            if not ip.is_global:"` | — |
| [SRC-1AE03B9EC3-L000206](../../agents/web_agent.py#L206) | 206 | `"                return None"` | — |
| [SRC-1AE03B9EC3-L000207](../../agents/web_agent.py#L207) | 207 | `"        return urllib.parse.urlunparse(parsed._replace(fragment=\"\"))"` | — |
| [SRC-1AE03B9EC3-L000208](../../agents/web_agent.py#L208) | 208 | `"    except (ValueError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L000209](../../agents/web_agent.py#L209) | 209 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000210](../../agents/web_agent.py#L210) | 210 | `""` | — |
| [SRC-1AE03B9EC3-L000211](../../agents/web_agent.py#L211) | 211 | `""` | — |
| [SRC-1AE03B9EC3-L000212](../../agents/web_agent.py#L212) | 212 | `"def _public_ip_literals(host: str) -> list[str] \| None:"` | — |
| [SRC-1AE03B9EC3-L000213](../../agents/web_agent.py#L213) | 213 | `"    \"\"\"Resolve host and return its public addresses."` | — |
| [SRC-1AE03B9EC3-L000214](../../agents/web_agent.py#L214) | 214 | `""` | — |
| [SRC-1AE03B9EC3-L000215](../../agents/web_agent.py#L215) | 215 | `"    Returns None when resolution fails or any answer is not a global address."` | — |
| [SRC-1AE03B9EC3-L000216](../../agents/web_agent.py#L216) | 216 | `"    Callers must open the TCP connection to one of these literals. A second DNS"` | — |
| [SRC-1AE03B9EC3-L000217](../../agents/web_agent.py#L217) | 217 | `"    lookup is not equivalent: the name can be rebound to a private address"` | — |
| [SRC-1AE03B9EC3-L000218](../../agents/web_agent.py#L218) | 218 | `"    between the check and the connection (DNS rebinding / TOCTOU)."` | — |
| [SRC-1AE03B9EC3-L000219](../../agents/web_agent.py#L219) | 219 | `"    \"\"\""` | — |
| [SRC-1AE03B9EC3-L000220](../../agents/web_agent.py#L220) | 220 | `"    if not host:"` | — |
| [SRC-1AE03B9EC3-L000221](../../agents/web_agent.py#L221) | 221 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000222](../../agents/web_agent.py#L222) | 222 | `"    try:"` | — |
| [SRC-1AE03B9EC3-L000223](../../agents/web_agent.py#L223) | 223 | `"        answers = socket.getaddrinfo(host, None, type=socket.SOCK_STREAM)"` | — |
| [SRC-1AE03B9EC3-L000224](../../agents/web_agent.py#L224) | 224 | `"    except (OSError, socket.gaierror):"` | — |
| [SRC-1AE03B9EC3-L000225](../../agents/web_agent.py#L225) | 225 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000226](../../agents/web_agent.py#L226) | 226 | `"    if not answers:"` | — |
| [SRC-1AE03B9EC3-L000227](../../agents/web_agent.py#L227) | 227 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000228](../../agents/web_agent.py#L228) | 228 | `"    literals: list[str] = []"` | — |
| [SRC-1AE03B9EC3-L000229](../../agents/web_agent.py#L229) | 229 | `"    for answer in answers:"` | — |
| [SRC-1AE03B9EC3-L000230](../../agents/web_agent.py#L230) | 230 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L000231](../../agents/web_agent.py#L231) | 231 | `"            address = ipaddress.ip_address(answer[4][0])"` | — |
| [SRC-1AE03B9EC3-L000232](../../agents/web_agent.py#L232) | 232 | `"        except ValueError:"` | — |
| [SRC-1AE03B9EC3-L000233](../../agents/web_agent.py#L233) | 233 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L000234](../../agents/web_agent.py#L234) | 234 | `"        if not address.is_global:"` | — |
| [SRC-1AE03B9EC3-L000235](../../agents/web_agent.py#L235) | 235 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L000236](../../agents/web_agent.py#L236) | 236 | `"        literal = str(address)"` | — |
| [SRC-1AE03B9EC3-L000237](../../agents/web_agent.py#L237) | 237 | `"        if literal not in literals:"` | — |
| [SRC-1AE03B9EC3-L000238](../../agents/web_agent.py#L238) | 238 | `"            literals.append(literal)"` | — |
| [SRC-1AE03B9EC3-L000239](../../agents/web_agent.py#L239) | 239 | `"    return literals or None"` | — |
| [SRC-1AE03B9EC3-L000240](../../agents/web_agent.py#L240) | 240 | `""` | — |
| [SRC-1AE03B9EC3-L000241](../../agents/web_agent.py#L241) | 241 | `""` | — |
| [SRC-1AE03B9EC3-L000242](../../agents/web_agent.py#L242) | 242 | `"def _host_resolves_publicly(host: str) -> bool:"` | — |
| [SRC-1AE03B9EC3-L000243](../../agents/web_agent.py#L243) | 243 | `"    \"\"\"Reject local/private destinations before fetching a third-party page.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000244](../../agents/web_agent.py#L244) | 244 | `"    return _public_ip_literals(host) is not None"` | — |
| [SRC-1AE03B9EC3-L000245](../../agents/web_agent.py#L245) | 245 | `""` | — |
| [SRC-1AE03B9EC3-L000246](../../agents/web_agent.py#L246) | 246 | `""` | — |
| [SRC-1AE03B9EC3-L000247](../../agents/web_agent.py#L247) | 247 | `"def _pinned_connect_url(logical_url: str, ip: str) -> str \| None:"` | — |
| [SRC-1AE03B9EC3-L000248](../../agents/web_agent.py#L248) | 248 | `"    \"\"\"Rewrite a validated public URL so the connection target is a checked IP.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000249](../../agents/web_agent.py#L249) | 249 | `"    parsed = urllib.parse.urlparse(logical_url)"` | — |
| [SRC-1AE03B9EC3-L000250](../../agents/web_agent.py#L250) | 250 | `"    if parsed.port not in (None, 80, 443):"` | — |
| [SRC-1AE03B9EC3-L000251](../../agents/web_agent.py#L251) | 251 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000252](../../agents/web_agent.py#L252) | 252 | `"    literal = f\"[{ip}]\" if \":\" in ip else ip"` | — |
| [SRC-1AE03B9EC3-L000253](../../agents/web_agent.py#L253) | 253 | `"    netloc = literal if parsed.port is None else f\"{literal}:{parsed.port}\""` | — |
| [SRC-1AE03B9EC3-L000254](../../agents/web_agent.py#L254) | 254 | `"    return urllib.parse.urlunparse(parsed._replace(netloc=netloc))"` | — |
| [SRC-1AE03B9EC3-L000255](../../agents/web_agent.py#L255) | 255 | `""` | — |
| [SRC-1AE03B9EC3-L000256](../../agents/web_agent.py#L256) | 256 | `""` | — |
| [SRC-1AE03B9EC3-L000257](../../agents/web_agent.py#L257) | 257 | `"def _fallback_answer(sources: list[dict[str, Any]], reason: str) -> str:"` | — |
| [SRC-1AE03B9EC3-L000258](../../agents/web_agent.py#L258) | 258 | `"    lines = [reason]"` | — |
| [SRC-1AE03B9EC3-L000259](../../agents/web_agent.py#L259) | 259 | `"    usable = [source for source in sources if source.get(\"snippet\")]"` | — |
| [SRC-1AE03B9EC3-L000260](../../agents/web_agent.py#L260) | 260 | `"    for index, source in enumerate(usable[:5], 1):"` | — |
| [SRC-1AE03B9EC3-L000261](../../agents/web_agent.py#L261) | 261 | `"        lines.append("` | — |
| [SRC-1AE03B9EC3-L000262](../../agents/web_agent.py#L262) | 262 | `"            f\"{index}. {source.get('title', 'نتيجة ويب')}: \""` | — |
| [SRC-1AE03B9EC3-L000263](../../agents/web_agent.py#L263) | 263 | `"            f\"{source['snippet']} (المصدر: {source['url']})\""` | — |
| [SRC-1AE03B9EC3-L000264](../../agents/web_agent.py#L264) | 264 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000265](../../agents/web_agent.py#L265) | 265 | `"    if not usable:"` | — |
| [SRC-1AE03B9EC3-L000266](../../agents/web_agent.py#L266) | 266 | `"        lines.append(\"لم أتمكن من استخراج مقتطفات كافية من نتائج الويب.\")"` | — |
| [SRC-1AE03B9EC3-L000267](../../agents/web_agent.py#L267) | 267 | `"    return \"\\n\\n\".join(lines)"` | — |
| [SRC-1AE03B9EC3-L000268](../../agents/web_agent.py#L268) | 268 | `""` | — |
| [SRC-1AE03B9EC3-L000269](../../agents/web_agent.py#L269) | 269 | `""` | — |
| [SRC-1AE03B9EC3-L000270](../../agents/web_agent.py#L270) | 270 | `"class WebAgent:"` | — |
| [SRC-1AE03B9EC3-L000271](../../agents/web_agent.py#L271) | 271 | `"    \"\"\"Search, inspect, and synthesize web evidence for open-ended questions.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000272](../../agents/web_agent.py#L272) | 272 | `""` | — |
| [SRC-1AE03B9EC3-L000273](../../agents/web_agent.py#L273) | 273 | `"    def __init__(self) -> None:"` | — |
| [SRC-1AE03B9EC3-L000274](../../agents/web_agent.py#L274) | 274 | `"        self.api_key = ("` | — |
| [SRC-1AE03B9EC3-L000275](../../agents/web_agent.py#L275) | 275 | `"            os.getenv(\"OMARAI_LLM_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000276](../../agents/web_agent.py#L276) | 276 | `"            or os.getenv(\"OPENROUTER_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000277](../../agents/web_agent.py#L277) | 277 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000278](../../agents/web_agent.py#L278) | 278 | `"        self.base_url = os.getenv("` | — |
| [SRC-1AE03B9EC3-L000279](../../agents/web_agent.py#L279) | 279 | `"            \"OMARAI_LLM_BASE_URL\", \"https://openrouter.ai/api/v1\""` | — |
| [SRC-1AE03B9EC3-L000280](../../agents/web_agent.py#L280) | 280 | `"        ).strip().rstrip(\"/\")"` | — |
| [SRC-1AE03B9EC3-L000281](../../agents/web_agent.py#L281) | 281 | `"        # Pin explicit role models for more consistent behaviour than a random free router."` | — |
| [SRC-1AE03B9EC3-L000282](../../agents/web_agent.py#L282) | 282 | `"        # OMARAI_LLM_MODEL remains a global override for users who want one model everywhere."` | — |
| [SRC-1AE03B9EC3-L000283](../../agents/web_agent.py#L283) | 283 | `"        global_model = os.getenv(\"OMARAI_LLM_MODEL\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000284](../../agents/web_agent.py#L284) | 284 | `"        self.answer_model = os.getenv("` | — |
| [SRC-1AE03B9EC3-L000285](../../agents/web_agent.py#L285) | 285 | `"            \"OMARAI_ANSWER_MODEL\", global_model or \"google/gemma-4-31b-it:free\""` | — |
| [SRC-1AE03B9EC3-L000286](../../agents/web_agent.py#L286) | 286 | `"        ).strip()"` | — |
| [SRC-1AE03B9EC3-L000287](../../agents/web_agent.py#L287) | 287 | `"        self.planner_model = os.getenv("` | — |
| [SRC-1AE03B9EC3-L000288](../../agents/web_agent.py#L288) | 288 | `"            \"OMARAI_PLANNER_MODEL\","` | — |
| [SRC-1AE03B9EC3-L000289](../../agents/web_agent.py#L289) | 289 | `"            global_model or \"nvidia/nemotron-3-ultra-550b-a55b:free\","` | — |
| [SRC-1AE03B9EC3-L000290](../../agents/web_agent.py#L290) | 290 | `"        ).strip()"` | — |
| [SRC-1AE03B9EC3-L000291](../../agents/web_agent.py#L291) | 291 | `"        self.review_model = os.getenv("` | — |
| [SRC-1AE03B9EC3-L000292](../../agents/web_agent.py#L292) | 292 | `"            \"OMARAI_REVIEW_MODEL\", self.answer_model"` | — |
| [SRC-1AE03B9EC3-L000293](../../agents/web_agent.py#L293) | 293 | `"        ).strip()"` | — |
| [SRC-1AE03B9EC3-L000294](../../agents/web_agent.py#L294) | 294 | `"        self.fallback_model = os.getenv("` | — |
| [SRC-1AE03B9EC3-L000295](../../agents/web_agent.py#L295) | 295 | `"            \"OMARAI_LLM_FALLBACK_MODEL\", \"openrouter/free\""` | — |
| [SRC-1AE03B9EC3-L000296](../../agents/web_agent.py#L296) | 296 | `"        ).strip()"` | — |
| [SRC-1AE03B9EC3-L000297](../../agents/web_agent.py#L297) | 297 | `"        self.model = self.answer_model  # Backwards-compatible alias."` | — |
| [SRC-1AE03B9EC3-L000298](../../agents/web_agent.py#L298) | 298 | `"        self.model_usage: list[dict[str, str]] = []"` | — |
| [SRC-1AE03B9EC3-L000299](../../agents/web_agent.py#L299) | 299 | `"        # Per-answer, bounded diagnostics contain only model identifiers and status metadata."` | — |
| [SRC-1AE03B9EC3-L000300](../../agents/web_agent.py#L300) | 300 | `"        # They intentionally exclude prompts, generated text, and provider response bodies."` | — |
| [SRC-1AE03B9EC3-L000301](../../agents/web_agent.py#L301) | 301 | `"        self.generation_diagnostics: list[dict[str, str]] = []"` | — |
| [SRC-1AE03B9EC3-L000302](../../agents/web_agent.py#L302) | 302 | `"        self.server_search_sources: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L000303](../../agents/web_agent.py#L303) | 303 | `"        self._provider_diagnostics: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L000304](../../agents/web_agent.py#L304) | 304 | `"        self._provider_diagnostics_lock = threading.Lock()"` | — |
| [SRC-1AE03B9EC3-L000305](../../agents/web_agent.py#L305) | 305 | `"        self._deepseek_budget_lock = threading.Lock()"` | — |
| [SRC-1AE03B9EC3-L000306](../../agents/web_agent.py#L306) | 306 | `"        self._deepseek_search_requests_reserved = 0"` | — |
| [SRC-1AE03B9EC3-L000307](../../agents/web_agent.py#L307) | 307 | `"        self.openrouter_web_search_enabled = ("` | — |
| [SRC-1AE03B9EC3-L000308](../../agents/web_agent.py#L308) | 308 | `"            os.getenv(\"OMARAI_OPENROUTER_WEB_SEARCH\", \"\").strip() == \"1\""` | — |
| [SRC-1AE03B9EC3-L000309](../../agents/web_agent.py#L309) | 309 | `"            and \"openrouter.ai\" in self.base_url.lower()"` | — |
| [SRC-1AE03B9EC3-L000310](../../agents/web_agent.py#L310) | 310 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000311](../../agents/web_agent.py#L311) | 311 | `"        self.timeout = max("` | — |
| [SRC-1AE03B9EC3-L000312](../../agents/web_agent.py#L312) | 312 | `"            5, min(int(os.getenv(\"OMARAI_LLM_TIMEOUT\", str(LLM_TIMEOUT_SECONDS))), 60)"` | — |
| [SRC-1AE03B9EC3-L000313](../../agents/web_agent.py#L313) | 313 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000314](../../agents/web_agent.py#L314) | 314 | `"        self._request_budget: RequestBudget \| None = None"` | — |
| [SRC-1AE03B9EC3-L000315](../../agents/web_agent.py#L315) | 315 | `""` | — |
| [SRC-1AE03B9EC3-L000316](../../agents/web_agent.py#L316) | 316 | `"    def _effective_timeout(self, configured_seconds: float) -> float:"` | — |
| [SRC-1AE03B9EC3-L000317](../../agents/web_agent.py#L317) | 317 | `"        \"\"\"Limit one outbound operation to the remaining per-answer time budget.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000318](../../agents/web_agent.py#L318) | 318 | `"        budget = getattr(self, \"_request_budget\", None)"` | — |
| [SRC-1AE03B9EC3-L000319](../../agents/web_agent.py#L319) | 319 | `"        if budget is None:"` | — |
| [SRC-1AE03B9EC3-L000320](../../agents/web_agent.py#L320) | 320 | `"            return float(configured_seconds)"` | — |
| [SRC-1AE03B9EC3-L000321](../../agents/web_agent.py#L321) | 321 | `"        return budget.timeout_for(configured_seconds)"` | — |
| [SRC-1AE03B9EC3-L000322](../../agents/web_agent.py#L322) | 322 | `""` | — |
| [SRC-1AE03B9EC3-L000323](../../agents/web_agent.py#L323) | 323 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000324](../../agents/web_agent.py#L324) | 324 | `"    def status() -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L000325](../../agents/web_agent.py#L325) | 325 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L000326](../../agents/web_agent.py#L326) | 326 | `"            import bs4  # noqa: F401"` | — |
| [SRC-1AE03B9EC3-L000327](../../agents/web_agent.py#L327) | 327 | `"            import httpx  # noqa: F401"` | — |
| [SRC-1AE03B9EC3-L000328](../../agents/web_agent.py#L328) | 328 | `"            search_ready = True"` | — |
| [SRC-1AE03B9EC3-L000329](../../agents/web_agent.py#L329) | 329 | `"        except ImportError:"` | — |
| [SRC-1AE03B9EC3-L000330](../../agents/web_agent.py#L330) | 330 | `"            search_ready = False"` | — |
| [SRC-1AE03B9EC3-L000331](../../agents/web_agent.py#L331) | 331 | `""` | — |
| [SRC-1AE03B9EC3-L000332](../../agents/web_agent.py#L332) | 332 | `"        global_model = os.getenv(\"OMARAI_LLM_MODEL\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000333](../../agents/web_agent.py#L333) | 333 | `"        answer_model = ("` | — |
| [SRC-1AE03B9EC3-L000334](../../agents/web_agent.py#L334) | 334 | `"            os.getenv(\"OMARAI_ANSWER_MODEL\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000335](../../agents/web_agent.py#L335) | 335 | `"            or global_model"` | — |
| [SRC-1AE03B9EC3-L000336](../../agents/web_agent.py#L336) | 336 | `"            or \"google/gemma-4-31b-it:free\""` | — |
| [SRC-1AE03B9EC3-L000337](../../agents/web_agent.py#L337) | 337 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000338](../../agents/web_agent.py#L338) | 338 | `"        planner_model = ("` | — |
| [SRC-1AE03B9EC3-L000339](../../agents/web_agent.py#L339) | 339 | `"            os.getenv(\"OMARAI_PLANNER_MODEL\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000340](../../agents/web_agent.py#L340) | 340 | `"            or global_model"` | — |
| [SRC-1AE03B9EC3-L000341](../../agents/web_agent.py#L341) | 341 | `"            or \"nvidia/nemotron-3-ultra-550b-a55b:free\""` | — |
| [SRC-1AE03B9EC3-L000342](../../agents/web_agent.py#L342) | 342 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000343](../../agents/web_agent.py#L343) | 343 | `"        review_model = os.getenv(\"OMARAI_REVIEW_MODEL\", \"\").strip() or answer_model"` | — |
| [SRC-1AE03B9EC3-L000344](../../agents/web_agent.py#L344) | 344 | `"        fallback_model = ("` | — |
