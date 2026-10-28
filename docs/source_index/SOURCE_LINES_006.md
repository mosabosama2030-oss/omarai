# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **006**
- سجلات الأسطر: **800**
- النطاق: SRC-686F71AA50-L000324 إلى SRC-1AE03B9EC3-L000073
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-686F71AA50 — [agents/task_understanding.py](../../agents/task_understanding.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-686F71AA50-L000324](../../agents/task_understanding.py#L324) | 324 | `"        (\"الولايات المتحدة\", (\"الولايات المتحدة\", \"united states\", \"the us\")),"` | — |
| [SRC-686F71AA50-L000325](../../agents/task_understanding.py#L325) | 325 | `"    )"` | — |
| [SRC-686F71AA50-L000326](../../agents/task_understanding.py#L326) | 326 | `"    result: list[str] = []"` | — |
| [SRC-686F71AA50-L000327](../../agents/task_understanding.py#L327) | 327 | `"    for canonical, cues in known:"` | — |
| [SRC-686F71AA50-L000328](../../agents/task_understanding.py#L328) | 328 | `"        if any(_contains(normalized, (cue,)) for cue in cues):"` | — |
| [SRC-686F71AA50-L000329](../../agents/task_understanding.py#L329) | 329 | `"            result.append(canonical)"` | — |
| [SRC-686F71AA50-L000330](../../agents/task_understanding.py#L330) | 330 | `"    return result"` | — |
| [SRC-686F71AA50-L000331](../../agents/task_understanding.py#L331) | 331 | `""` | — |
| [SRC-686F71AA50-L000332](../../agents/task_understanding.py#L332) | 332 | `""` | — |
| [SRC-686F71AA50-L000333](../../agents/task_understanding.py#L333) | 333 | `"def _language_profile(question: str) -> str:"` | — |
| [SRC-686F71AA50-L000334](../../agents/task_understanding.py#L334) | 334 | `"    arabic = len(re.findall(r\"[\\u0600-\\u06FF]\", question))"` | — |
| [SRC-686F71AA50-L000335](../../agents/task_understanding.py#L335) | 335 | `"    latin = len(re.findall(r\"[A-Za-z]\", question))"` | — |
| [SRC-686F71AA50-L000336](../../agents/task_understanding.py#L336) | 336 | `"    if arabic and latin:"` | — |
| [SRC-686F71AA50-L000337](../../agents/task_understanding.py#L337) | 337 | `"        return \"mixed\""` | — |
| [SRC-686F71AA50-L000338](../../agents/task_understanding.py#L338) | 338 | `"    if arabic:"` | — |
| [SRC-686F71AA50-L000339](../../agents/task_understanding.py#L339) | 339 | `"        return \"ar\""` | — |
| [SRC-686F71AA50-L000340](../../agents/task_understanding.py#L340) | 340 | `"    if latin:"` | — |
| [SRC-686F71AA50-L000341](../../agents/task_understanding.py#L341) | 341 | `"        return \"en\""` | — |
| [SRC-686F71AA50-L000342](../../agents/task_understanding.py#L342) | 342 | `"    return \"und\""` | — |
| [SRC-686F71AA50-L000343](../../agents/task_understanding.py#L343) | 343 | `""` | — |
| [SRC-686F71AA50-L000344](../../agents/task_understanding.py#L344) | 344 | `""` | — |
| [SRC-686F71AA50-L000345](../../agents/task_understanding.py#L345) | 345 | `"def _primary_family(matches: dict[str, list[str]], mode: str, route: str, normalized: str) -> str:"` | — |
| [SRC-686F71AA50-L000346](../../agents/task_understanding.py#L346) | 346 | `"    # An explicit official-destination request is different from a request for an"` | — |
| [SRC-686F71AA50-L000347](../../agents/task_understanding.py#L347) | 347 | `"    # article mentioning the organization; government verification is a separate slot."` | — |
| [SRC-686F71AA50-L000348](../../agents/task_understanding.py#L348) | 348 | `"    if matches[\"official_site_lookup\"]:"` | — |
| [SRC-686F71AA50-L000349](../../agents/task_understanding.py#L349) | 349 | `"        return \"official_site_lookup\""` | — |
| [SRC-686F71AA50-L000350](../../agents/task_understanding.py#L350) | 350 | `"    for family in ("` | — |
| [SRC-686F71AA50-L000351](../../agents/task_understanding.py#L351) | 351 | `"        \"social_opinions\", \"summarize\", \"troubleshoot\", \"compare\","` | — |
| [SRC-686F71AA50-L000352](../../agents/task_understanding.py#L352) | 352 | `"        \"medical_information\", \"legal_information\", \"coding_or_technical_design\","` | — |
| [SRC-686F71AA50-L000353](../../agents/task_understanding.py#L353) | 353 | `"        \"data_analysis\", \"translation\", \"calculation\", \"planning\","` | — |
| [SRC-686F71AA50-L000354](../../agents/task_understanding.py#L354) | 354 | `"        \"writing_or_editing\", \"creative_generation\", \"lead_generation\","` | — |
| [SRC-686F71AA50-L000355](../../agents/task_understanding.py#L355) | 355 | `"        \"how_to\", \"recommendation\", \"current_information\", \"find_or_discover\","` | — |
| [SRC-686F71AA50-L000356](../../agents/task_understanding.py#L356) | 356 | `"        \"explain_or_define\", \"general_research\","` | — |
| [SRC-686F71AA50-L000357](../../agents/task_understanding.py#L357) | 357 | `"    ):"` | — |
| [SRC-686F71AA50-L000358](../../agents/task_understanding.py#L358) | 358 | `"        if matches.get(family):"` | — |
| [SRC-686F71AA50-L000359](../../agents/task_understanding.py#L359) | 359 | `"            return family"` | — |
| [SRC-686F71AA50-L000360](../../agents/task_understanding.py#L360) | 360 | `"    if route == \"CLARIFY\":"` | — |
| [SRC-686F71AA50-L000361](../../agents/task_understanding.py#L361) | 361 | `"        return \"ambiguous_or_incomplete\""` | — |
| [SRC-686F71AA50-L000362](../../agents/task_understanding.py#L362) | 362 | `"    if route in {\"WEB_SIMPLE\", \"WEB_DEEP\", \"LEAD_GENERATION\"} or mode != \"auto\":"` | — |
| [SRC-686F71AA50-L000363](../../agents/task_understanding.py#L363) | 363 | `"        return \"web_research\""` | — |
| [SRC-686F71AA50-L000364](../../agents/task_understanding.py#L364) | 364 | `"    return \"general_question\""` | — |
| [SRC-686F71AA50-L000365](../../agents/task_understanding.py#L365) | 365 | `""` | — |
| [SRC-686F71AA50-L000366](../../agents/task_understanding.py#L366) | 366 | `""` | — |
| [SRC-686F71AA50-L000367](../../agents/task_understanding.py#L367) | 367 | `"def build_task_spec("` | — |
| [SRC-686F71AA50-L000368](../../agents/task_understanding.py#L368) | 368 | `"    question: str,"` | — |
| [SRC-686F71AA50-L000369](../../agents/task_understanding.py#L369) | 369 | `"    *,"` | — |
| [SRC-686F71AA50-L000370](../../agents/task_understanding.py#L370) | 370 | `"    mode: str = \"auto\","` | — |
| [SRC-686F71AA50-L000371](../../agents/task_understanding.py#L371) | 371 | `"    intent_route: str = \"\","` | — |
| [SRC-686F71AA50-L000372](../../agents/task_understanding.py#L372) | 372 | `"    plan: dict[str, Any] \| None = None,"` | — |
| [SRC-686F71AA50-L000373](../../agents/task_understanding.py#L373) | 373 | `"    dialogue_context: dict[str, Any] \| None = None,"` | — |
| [SRC-686F71AA50-L000374](../../agents/task_understanding.py#L374) | 374 | `") -> dict[str, Any]:"` | — |
| [SRC-686F71AA50-L000375](../../agents/task_understanding.py#L375) | 375 | `"    \"\"\"Build a bounded task specification, interpretation hypotheses, and test matrix.\"\"\""` | — |
| [SRC-686F71AA50-L000376](../../agents/task_understanding.py#L376) | 376 | `"    raw = question if isinstance(question, str) else \"\""` | — |
| [SRC-686F71AA50-L000377](../../agents/task_understanding.py#L377) | 377 | `"    raw = raw[:MAX_TASK_CHARS]"` | — |
| [SRC-686F71AA50-L000378](../../agents/task_understanding.py#L378) | 378 | `"    normalized = normalize_text(raw)"` | — |
| [SRC-686F71AA50-L000379](../../agents/task_understanding.py#L379) | 379 | `"    clean_mode = mode.strip().lower() if isinstance(mode, str) else \"auto\""` | — |
| [SRC-686F71AA50-L000380](../../agents/task_understanding.py#L380) | 380 | `"    if clean_mode not in SUPPORTED_MODES:"` | — |
| [SRC-686F71AA50-L000381](../../agents/task_understanding.py#L381) | 381 | `"        clean_mode = \"auto\""` | — |
| [SRC-686F71AA50-L000382](../../agents/task_understanding.py#L382) | 382 | `"    matches = {"` | — |
| [SRC-686F71AA50-L000383](../../agents/task_understanding.py#L383) | 383 | `"        family: _contains(normalized, phrases)"` | — |
| [SRC-686F71AA50-L000384](../../agents/task_understanding.py#L384) | 384 | `"        for family, phrases in _PATTERNS.items()"` | — |
| [SRC-686F71AA50-L000385](../../agents/task_understanding.py#L385) | 385 | `"        if not family.startswith(\"output_\")"` | — |
| [SRC-686F71AA50-L000386](../../agents/task_understanding.py#L386) | 386 | `"    }"` | — |
| [SRC-686F71AA50-L000387](../../agents/task_understanding.py#L387) | 387 | `"    output_matches = {"` | — |
| [SRC-686F71AA50-L000388](../../agents/task_understanding.py#L388) | 388 | `"        family: _contains(normalized, phrases)"` | — |
| [SRC-686F71AA50-L000389](../../agents/task_understanding.py#L389) | 389 | `"        for family, phrases in _PATTERNS.items()"` | — |
| [SRC-686F71AA50-L000390](../../agents/task_understanding.py#L390) | 390 | `"        if family.startswith(\"output_\")"` | — |
| [SRC-686F71AA50-L000391](../../agents/task_understanding.py#L391) | 391 | `"    }"` | — |
| [SRC-686F71AA50-L000392](../../agents/task_understanding.py#L392) | 392 | `"    aspect_values: list[str] = []"` | — |
| [SRC-686F71AA50-L000393](../../agents/task_understanding.py#L393) | 393 | `"    try:"` | — |
| [SRC-686F71AA50-L000394](../../agents/task_understanding.py#L394) | 394 | `"        from agents.aspect_planning import extract_aspects"` | — |
| [SRC-686F71AA50-L000395](../../agents/task_understanding.py#L395) | 395 | `"        aspect_values = extract_aspects(raw)[:MAX_TASK_ASPECTS]"` | — |
| [SRC-686F71AA50-L000396](../../agents/task_understanding.py#L396) | 396 | `"    except (ImportError, TypeError, ValueError):"` | — |
| [SRC-686F71AA50-L000397](../../agents/task_understanding.py#L397) | 397 | `"        aspect_values = []"` | — |
| [SRC-686F71AA50-L000398](../../agents/task_understanding.py#L398) | 398 | `""` | — |
| [SRC-686F71AA50-L000399](../../agents/task_understanding.py#L399) | 399 | `"    official_destination = bool(matches[\"official_site_lookup\"])"` | — |
| [SRC-686F71AA50-L000400](../../agents/task_understanding.py#L400) | 400 | `"    government_official_site = bool("` | — |
| [SRC-686F71AA50-L000401](../../agents/task_understanding.py#L401) | 401 | `"        official_destination"` | — |
| [SRC-686F71AA50-L000402](../../agents/task_understanding.py#L402) | 402 | `"        and bool(_contains(normalized, _OFFICIAL_WORDS))"` | — |
| [SRC-686F71AA50-L000403](../../agents/task_understanding.py#L403) | 403 | `"    )"` | — |
| [SRC-686F71AA50-L000404](../../agents/task_understanding.py#L404) | 404 | `"    navigation = official_destination or bool("` | — |
| [SRC-686F71AA50-L000405](../../agents/task_understanding.py#L405) | 405 | `"        _URL_RE.search(raw)"` | — |
| [SRC-686F71AA50-L000406](../../agents/task_understanding.py#L406) | 406 | `"        or any(normalize_text(term) in normalized for term in (\"هات رابط\", \"website\", \"homepage\"))"` | — |
| [SRC-686F71AA50-L000407](../../agents/task_understanding.py#L407) | 407 | `"    )"` | — |
| [SRC-686F71AA50-L000408](../../agents/task_understanding.py#L408) | 408 | `"    explicit_freshness = bool(_contains(normalized, _FRESHNESS_CUES))"` | — |
| [SRC-686F71AA50-L000409](../../agents/task_understanding.py#L409) | 409 | `"    current_required = (clean_mode == \"latest\" or explicit_freshness) and not navigation"` | — |
| [SRC-686F71AA50-L000410](../../agents/task_understanding.py#L410) | 410 | `"    social_required = clean_mode == \"social\" or bool(matches[\"social_opinions\"])"` | — |
| [SRC-686F71AA50-L000411](../../agents/task_understanding.py#L411) | 411 | `"    family = _primary_family(matches, clean_mode, intent_route, normalized)"` | — |
| [SRC-686F71AA50-L000412](../../agents/task_understanding.py#L412) | 412 | `""` | — |
| [SRC-686F71AA50-L000413](../../agents/task_understanding.py#L413) | 413 | `"    if family == \"official_site_lookup\":"` | — |
| [SRC-686F71AA50-L000414](../../agents/task_understanding.py#L414) | 414 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000415](../../agents/task_understanding.py#L415) | 415 | `"            \"target_entity_match\","` | — |
| [SRC-686F71AA50-L000416](../../agents/task_understanding.py#L416) | 416 | `"            \"official_domain_or_independently_linked_official_destination\","` | — |
| [SRC-686F71AA50-L000417](../../agents/task_understanding.py#L417) | 417 | `"            \"never_substitute_an_article_or_unrelated_directory\","` | — |
| [SRC-686F71AA50-L000418](../../agents/task_understanding.py#L418) | 418 | `"        ]"` | — |
| [SRC-686F71AA50-L000419](../../agents/task_understanding.py#L419) | 419 | `"        query_strategies = [\"exact_entity\", \"official_domain\", \"government_portal_cross_check\"]"` | — |
| [SRC-686F71AA50-L000420](../../agents/task_understanding.py#L420) | 420 | `"    elif family == \"social_opinions\":"` | — |
| [SRC-686F71AA50-L000421](../../agents/task_understanding.py#L421) | 421 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000422](../../agents/task_understanding.py#L422) | 422 | `"            \"public_social_platform_url\","` | — |
| [SRC-686F71AA50-L000423](../../agents/task_understanding.py#L423) | 423 | `"            \"original_post_or_readable_post_content_when_available\","` | — |
| [SRC-686F71AA50-L000424](../../agents/task_understanding.py#L424) | 424 | `"            \"heuristic_classification_is_not_identity_or_truth_verification\","` | — |
| [SRC-686F71AA50-L000425](../../agents/task_understanding.py#L425) | 425 | `"        ]"` | — |
| [SRC-686F71AA50-L000426](../../agents/task_understanding.py#L426) | 426 | `"        query_strategies = [\"topic_platform\", \"personal_experience\", \"discussion\", \"commercial_exclusion\"]"` | — |
| [SRC-686F71AA50-L000427](../../agents/task_understanding.py#L427) | 427 | `"    elif family == \"summarize\":"` | — |
| [SRC-686F71AA50-L000428](../../agents/task_understanding.py#L428) | 428 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000429](../../agents/task_understanding.py#L429) | 429 | `"            \"read_the_requested_text_or_page\","` | — |
| [SRC-686F71AA50-L000430](../../agents/task_understanding.py#L430) | 430 | `"            \"do_not_summarize_unread_content_from_title_only\","` | — |
| [SRC-686F71AA50-L000431](../../agents/task_understanding.py#L431) | 431 | `"            \"preserve_source_scope_and_important_qualifiers\","` | — |
| [SRC-686F71AA50-L000432](../../agents/task_understanding.py#L432) | 432 | `"        ]"` | — |
| [SRC-686F71AA50-L000433](../../agents/task_understanding.py#L433) | 433 | `"        query_strategies = [\"exact_url_or_supplied_text\", \"page_read\", \"scope_preserving_summary\"]"` | — |
| [SRC-686F71AA50-L000434](../../agents/task_understanding.py#L434) | 434 | `"    elif family == \"troubleshoot\":"` | — |
| [SRC-686F71AA50-L000435](../../agents/task_understanding.py#L435) | 435 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000436](../../agents/task_understanding.py#L436) | 436 | `"            \"preserve_error_message_and_environment\","` | — |
| [SRC-686F71AA50-L000437](../../agents/task_understanding.py#L437) | 437 | `"            \"prefer_manual_or_primary_technical_source\","` | — |
| [SRC-686F71AA50-L000438](../../agents/task_understanding.py#L438) | 438 | `"            \"separate_diagnosis_hypotheses_from_confirmed_cause\","` | — |
| [SRC-686F71AA50-L000439](../../agents/task_understanding.py#L439) | 439 | `"        ]"` | — |
| [SRC-686F71AA50-L000440](../../agents/task_understanding.py#L440) | 440 | `"        query_strategies = [\"symptom_exact_text\", \"cause_hypotheses\", \"official_manual\", \"safe_remedy\"]"` | — |
| [SRC-686F71AA50-L000441](../../agents/task_understanding.py#L441) | 441 | `"    elif family == \"compare\":"` | — |
| [SRC-686F71AA50-L000442](../../agents/task_understanding.py#L442) | 442 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000443](../../agents/task_understanding.py#L443) | 443 | `"            \"preserve_each_explicit_comparison_criterion\","` | — |
| [SRC-686F71AA50-L000444](../../agents/task_understanding.py#L444) | 444 | `"            \"source_support_for_each_material_comparison\","` | — |
| [SRC-686F71AA50-L000445](../../agents/task_understanding.py#L445) | 445 | `"            \"distinguish_primary_specs_from_individual_experience\","` | — |
| [SRC-686F71AA50-L000446](../../agents/task_understanding.py#L446) | 446 | `"        ]"` | — |
| [SRC-686F71AA50-L000447](../../agents/task_understanding.py#L447) | 447 | `"        query_strategies = [\"topic_baseline\", \"one_query_per_criterion\", \"primary_specification\", \"independent_comparison\"]"` | — |
| [SRC-686F71AA50-L000448](../../agents/task_understanding.py#L448) | 448 | `"    elif family == \"how_to\":"` | — |
| [SRC-686F71AA50-L000449](../../agents/task_understanding.py#L449) | 449 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000450](../../agents/task_understanding.py#L450) | 450 | `"            \"ordered_actionable_steps\","` | — |
| [SRC-686F71AA50-L000451](../../agents/task_understanding.py#L451) | 451 | `"            \"surface prerequisites and safety constraints\","` | — |
| [SRC-686F71AA50-L000452](../../agents/task_understanding.py#L452) | 452 | `"            \"distinguish general guidance from product-specific instructions\","` | — |
| [SRC-686F71AA50-L000453](../../agents/task_understanding.py#L453) | 453 | `"        ]"` | — |
| [SRC-686F71AA50-L000454](../../agents/task_understanding.py#L454) | 454 | `"        query_strategies = [\"goal_exact_match\", \"official_guide\", \"stepwise_method\"]"` | — |
| [SRC-686F71AA50-L000455](../../agents/task_understanding.py#L455) | 455 | `"    elif family == \"lead_generation\":"` | — |
| [SRC-686F71AA50-L000456](../../agents/task_understanding.py#L456) | 456 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000457](../../agents/task_understanding.py#L457) | 457 | `"            \"public_buyer_intent_signal\","` | — |
| [SRC-686F71AA50-L000458](../../agents/task_understanding.py#L458) | 458 | `"            \"do_not_treat_listing_or_ad_as_a_buyer\","` | — |
| [SRC-686F71AA50-L000459](../../agents/task_understanding.py#L459) | 459 | `"            \"identity_not_verified_without_separate_evidence\","` | — |
| [SRC-686F71AA50-L000460](../../agents/task_understanding.py#L460) | 460 | `"        ]"` | — |
| [SRC-686F71AA50-L000461](../../agents/task_understanding.py#L461) | 461 | `"        query_strategies = [\"buyer_intent_phrase\", \"public_discussion\", \"recent_signal\"]"` | — |
| [SRC-686F71AA50-L000462](../../agents/task_understanding.py#L462) | 462 | `"    elif family == \"recommendation\":"` | — |
| [SRC-686F71AA50-L000463](../../agents/task_understanding.py#L463) | 463 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000464](../../agents/task_understanding.py#L464) | 464 | `"            \"preserve_budget_location_and_use_case_if_explicit\","` | — |
| [SRC-686F71AA50-L000465](../../agents/task_understanding.py#L465) | 465 | `"            \"compare_alternatives\","` | — |
| [SRC-686F71AA50-L000466](../../agents/task_understanding.py#L466) | 466 | `"            \"make_tradeoffs_and_missing_information_visible\","` | — |
| [SRC-686F71AA50-L000467](../../agents/task_understanding.py#L467) | 467 | `"        ]"` | — |
| [SRC-686F71AA50-L000468](../../agents/task_understanding.py#L468) | 468 | `"        query_strategies = [\"use_case\", \"budget_and_location\", \"pros_cons\", \"alternatives\"]"` | — |
| [SRC-686F71AA50-L000469](../../agents/task_understanding.py#L469) | 469 | `"    elif family == \"medical_information\":"` | — |
| [SRC-686F71AA50-L000470](../../agents/task_understanding.py#L470) | 470 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000471](../../agents/task_understanding.py#L471) | 471 | `"            \"distinguish_general_health_information_from_personal_diagnosis\","` | — |
| [SRC-686F71AA50-L000472](../../agents/task_understanding.py#L472) | 472 | `"            \"prefer_current_authoritative_health_sources_when_research_is_requested\","` | — |
| [SRC-686F71AA50-L000473](../../agents/task_understanding.py#L473) | 473 | `"            \"preserve_units_dosage_context_and_uncertainty\","` | — |
| [SRC-686F71AA50-L000474](../../agents/task_understanding.py#L474) | 474 | `"            \"escalate_urgent_or_emergency_symptoms_to_appropriate_care\","` | — |
| [SRC-686F71AA50-L000475](../../agents/task_understanding.py#L475) | 475 | `"        ]"` | — |
| [SRC-686F71AA50-L000476](../../agents/task_understanding.py#L476) | 476 | `"        query_strategies = [\"authoritative_health_source\", \"symptom_context\", \"limitations_and_urgency\"]"` | — |
| [SRC-686F71AA50-L000477](../../agents/task_understanding.py#L477) | 477 | `"    elif family == \"legal_information\":"` | — |
| [SRC-686F71AA50-L000478](../../agents/task_understanding.py#L478) | 478 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000479](../../agents/task_understanding.py#L479) | 479 | `"            \"identify_jurisdiction_and_effective_date_if_relevant\","` | — |
| [SRC-686F71AA50-L000480](../../agents/task_understanding.py#L480) | 480 | `"            \"prefer_primary_law_or_official_regulatory_text\","` | — |
| [SRC-686F71AA50-L000481](../../agents/task_understanding.py#L481) | 481 | `"            \"distinguish_general_information_from_legal_advice\","` | — |
| [SRC-686F71AA50-L000482](../../agents/task_understanding.py#L482) | 482 | `"        ]"` | — |
| [SRC-686F71AA50-L000483](../../agents/task_understanding.py#L483) | 483 | `"        query_strategies = [\"official_law_text\", \"jurisdiction_and_date\", \"interpretive_context\"]"` | — |
| [SRC-686F71AA50-L000484](../../agents/task_understanding.py#L484) | 484 | `"    elif family == \"coding_or_technical_design\":"` | — |
| [SRC-686F71AA50-L000485](../../agents/task_understanding.py#L485) | 485 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000486](../../agents/task_understanding.py#L486) | 486 | `"            \"preserve_language_version_runtime_and_error_text_if_supplied\","` | — |
| [SRC-686F71AA50-L000487](../../agents/task_understanding.py#L487) | 487 | `"            \"separate_observed_failure_from_cause_hypotheses\","` | — |
| [SRC-686F71AA50-L000488](../../agents/task_understanding.py#L488) | 488 | `"            \"provide_testable_changes_and_regression_tests\","` | — |
| [SRC-686F71AA50-L000489](../../agents/task_understanding.py#L489) | 489 | `"        ]"` | — |
| [SRC-686F71AA50-L000490](../../agents/task_understanding.py#L490) | 490 | `"        query_strategies = [\"minimal_reproducer\", \"documentation_or_api_reference\", \"test_and_verify\"]"` | — |
| [SRC-686F71AA50-L000491](../../agents/task_understanding.py#L491) | 491 | `"    elif family == \"data_analysis\":"` | — |
| [SRC-686F71AA50-L000492](../../agents/task_understanding.py#L492) | 492 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000493](../../agents/task_understanding.py#L493) | 493 | `"            \"preserve_dataset_grain_and_metric_definition\","` | — |
| [SRC-686F71AA50-L000494](../../agents/task_understanding.py#L494) | 494 | `"            \"inspect_missingness_duplicates_outliers_and_time_coverage\","` | — |
| [SRC-686F71AA50-L000495](../../agents/task_understanding.py#L495) | 495 | `"            \"separate_observed_association_from_causal_explanation\","` | — |
| [SRC-686F71AA50-L000496](../../agents/task_understanding.py#L496) | 496 | `"        ]"` | — |
| [SRC-686F71AA50-L000497](../../agents/task_understanding.py#L497) | 497 | `"        query_strategies = [\"schema_and_grain\", \"data_quality\", \"metric_and_segment_checks\"]"` | — |
| [SRC-686F71AA50-L000498](../../agents/task_understanding.py#L498) | 498 | `"    elif family == \"calculation\":"` | — |
| [SRC-686F71AA50-L000499](../../agents/task_understanding.py#L499) | 499 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000500](../../agents/task_understanding.py#L500) | 500 | `"            \"show_formula_and_units_when_useful\","` | — |
| [SRC-686F71AA50-L000501](../../agents/task_understanding.py#L501) | 501 | `"            \"validate_input_units_and_rounding\","` | — |
| [SRC-686F71AA50-L000502](../../agents/task_understanding.py#L502) | 502 | `"            \"distinguish_exact_result_from_assumption_based_estimate\","` | — |
| [SRC-686F71AA50-L000503](../../agents/task_understanding.py#L503) | 503 | `"        ]"` | — |
| [SRC-686F71AA50-L000504](../../agents/task_understanding.py#L504) | 504 | `"        query_strategies = [\"formula\", \"unit_validation\", \"independent_arithmetic_check\"]"` | — |
| [SRC-686F71AA50-L000505](../../agents/task_understanding.py#L505) | 505 | `"    elif family == \"translation\":"` | — |
| [SRC-686F71AA50-L000506](../../agents/task_understanding.py#L506) | 506 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000507](../../agents/task_understanding.py#L507) | 507 | `"            \"preserve_meaning_tone_and_named_entities\","` | — |
| [SRC-686F71AA50-L000508](../../agents/task_understanding.py#L508) | 508 | `"            \"surface_ambiguous_source_phrasing_instead_of_silently_inventing_meaning\","` | — |
| [SRC-686F71AA50-L000509](../../agents/task_understanding.py#L509) | 509 | `"            \"respect_explicit_target_language_and_script\","` | — |
| [SRC-686F71AA50-L000510](../../agents/task_understanding.py#L510) | 510 | `"        ]"` | — |
| [SRC-686F71AA50-L000511](../../agents/task_understanding.py#L511) | 511 | `"        query_strategies = [\"source_text\", \"target_language\", \"terminology_and_tone\"]"` | — |
| [SRC-686F71AA50-L000512](../../agents/task_understanding.py#L512) | 512 | `"    elif family == \"writing_or_editing\":"` | — |
| [SRC-686F71AA50-L000513](../../agents/task_understanding.py#L513) | 513 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000514](../../agents/task_understanding.py#L514) | 514 | `"            \"follow_requested_audience_tone_and_format\","` | — |
| [SRC-686F71AA50-L000515](../../agents/task_understanding.py#L515) | 515 | `"            \"preserve_user_provided_facts_without_adding_unverified_claims\","` | — |
| [SRC-686F71AA50-L000516](../../agents/task_understanding.py#L516) | 516 | `"            \"distinguish_rewrite_from_fact_check\","` | — |
| [SRC-686F71AA50-L000517](../../agents/task_understanding.py#L517) | 517 | `"        ]"` | — |
| [SRC-686F71AA50-L000518](../../agents/task_understanding.py#L518) | 518 | `"        query_strategies = [\"audience_and_purpose\", \"tone_and_format\", \"fact_preservation\"]"` | — |
| [SRC-686F71AA50-L000519](../../agents/task_understanding.py#L519) | 519 | `"    elif family == \"planning\":"` | — |
| [SRC-686F71AA50-L000520](../../agents/task_understanding.py#L520) | 520 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000521](../../agents/task_understanding.py#L521) | 521 | `"            \"preserve_goal_constraints_dependencies_and_deadline\","` | — |
| [SRC-686F71AA50-L000522](../../agents/task_understanding.py#L522) | 522 | `"            \"make_assumptions_and_unavailable_resources_explicit\","` | — |
| [SRC-686F71AA50-L000523](../../agents/task_understanding.py#L523) | 523 | `"            \"separate_proposed_steps_from_completed_actions\","` | — |
| [SRC-686F71AA50-L000524](../../agents/task_understanding.py#L524) | 524 | `"        ]"` | — |
| [SRC-686F71AA50-L000525](../../agents/task_understanding.py#L525) | 525 | `"        query_strategies = [\"goal_and_constraints\", \"dependency_order\", \"risks_and_fallbacks\"]"` | — |
| [SRC-686F71AA50-L000526](../../agents/task_understanding.py#L526) | 526 | `"    elif family == \"creative_generation\":"` | — |
| [SRC-686F71AA50-L000527](../../agents/task_understanding.py#L527) | 527 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000528](../../agents/task_understanding.py#L528) | 528 | `"            \"follow_requested_genre_voice_and_constraints\","` | — |
| [SRC-686F71AA50-L000529](../../agents/task_understanding.py#L529) | 529 | `"            \"do_not_present_invented_story_details_as_real_facts\","` | — |
| [SRC-686F71AA50-L000530](../../agents/task_understanding.py#L530) | 530 | `"            \"preserve_explicit_content_boundaries\","` | — |
| [SRC-686F71AA50-L000531](../../agents/task_understanding.py#L531) | 531 | `"        ]"` | — |
| [SRC-686F71AA50-L000532](../../agents/task_understanding.py#L532) | 532 | `"        query_strategies = [\"genre_and_voice\", \"creative_constraints\", \"revision_options\"]"` | — |
| [SRC-686F71AA50-L000533](../../agents/task_understanding.py#L533) | 533 | `"    else:"` | — |
| [SRC-686F71AA50-L000534](../../agents/task_understanding.py#L534) | 534 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000535](../../agents/task_understanding.py#L535) | 535 | `"            \"match_sources_to_the_question\","` | — |
| [SRC-686F71AA50-L000536](../../agents/task_understanding.py#L536) | 536 | `"            \"distinguish_search_snippet_from_read_page\","` | — |
| [SRC-686F71AA50-L000537](../../agents/task_understanding.py#L537) | 537 | `"            \"cite_material_web_claims\","` | — |
| [SRC-686F71AA50-L000538](../../agents/task_understanding.py#L538) | 538 | `"        ]"` | — |
| [SRC-686F71AA50-L000539](../../agents/task_understanding.py#L539) | 539 | `"        query_strategies = [\"exact_topic\", \"primary_source\", \"cross_check_if_needed\"]"` | — |
| [SRC-686F71AA50-L000540](../../agents/task_understanding.py#L540) | 540 | `""` | — |
| [SRC-686F71AA50-L000541](../../agents/task_understanding.py#L541) | 541 | `"    # Source freshness, requested officiality, and social evidence are orthogonal"` | — |
| [SRC-686F71AA50-L000542](../../agents/task_understanding.py#L542) | 542 | `"    # constraints. Preserve them even when another intent is the primary family."` | — |
| [SRC-686F71AA50-L000543](../../agents/task_understanding.py#L543) | 543 | `"    if current_required and not official_destination:"` | — |
| [SRC-686F71AA50-L000544](../../agents/task_understanding.py#L544) | 544 | `"        evidence_requirements.extend(["` | — |
| [SRC-686F71AA50-L000545](../../agents/task_understanding.py#L545) | 545 | `"            \"publication_or_update_date\","` | — |
| [SRC-686F71AA50-L000546](../../agents/task_understanding.py#L546) | 546 | `"            \"page_text_successfully_read\","` | — |
| [SRC-686F71AA50-L000547](../../agents/task_understanding.py#L547) | 547 | `"            \"prefer_primary_current_source\","` | — |
| [SRC-686F71AA50-L000548](../../agents/task_understanding.py#L548) | 548 | `"            \"do_not_use_stale_page_as_current_proof\","` | — |
| [SRC-686F71AA50-L000549](../../agents/task_understanding.py#L549) | 549 | `"        ])"` | — |
| [SRC-686F71AA50-L000550](../../agents/task_understanding.py#L550) | 550 | `"        query_strategies.extend([\"recent_official_update\", \"primary_source\", \"date_check\"])"` | — |
| [SRC-686F71AA50-L000551](../../agents/task_understanding.py#L551) | 551 | `"    if social_required and family != \"social_opinions\":"` | — |
| [SRC-686F71AA50-L000552](../../agents/task_understanding.py#L552) | 552 | `"        evidence_requirements.extend(["` | — |
| [SRC-686F71AA50-L000553](../../agents/task_understanding.py#L553) | 553 | `"            \"public_social_platform_url\","` | — |
| [SRC-686F71AA50-L000554](../../agents/task_understanding.py#L554) | 554 | `"            \"separate_personal_experience_from_promotion\","` | — |
| [SRC-686F71AA50-L000555](../../agents/task_understanding.py#L555) | 555 | `"            \"heuristic_classification_is_not_identity_or_truth_verification\","` | — |
| [SRC-686F71AA50-L000556](../../agents/task_understanding.py#L556) | 556 | `"        ])"` | — |
| [SRC-686F71AA50-L000557](../../agents/task_understanding.py#L557) | 557 | `"        query_strategies.extend([\"personal_experience\", \"discussion\", \"commercial_exclusion\"])"` | — |
| [SRC-686F71AA50-L000558](../../agents/task_understanding.py#L558) | 558 | `"    if official_destination and family != \"official_site_lookup\":"` | — |
| [SRC-686F71AA50-L000559](../../agents/task_understanding.py#L559) | 559 | `"        evidence_requirements.extend(["` | — |
| [SRC-686F71AA50-L000560](../../agents/task_understanding.py#L560) | 560 | `"            \"distinguish_official_destination_from_mentions_or_articles\","` | — |
| [SRC-686F71AA50-L000561](../../agents/task_understanding.py#L561) | 561 | `"            \"do_not_claim_domain_ownership_without_independent_evidence\","` | — |
| [SRC-686F71AA50-L000562](../../agents/task_understanding.py#L562) | 562 | `"        ])"` | — |
| [SRC-686F71AA50-L000563](../../agents/task_understanding.py#L563) | 563 | `"        query_strategies.extend([\"official_domain\", \"government_portal_cross_check\"])"` | — |
| [SRC-686F71AA50-L000564](../../agents/task_understanding.py#L564) | 564 | `"    if \"compare\" in matches and family != \"compare\":"` | — |
| [SRC-686F71AA50-L000565](../../agents/task_understanding.py#L565) | 565 | `"        evidence_requirements.extend(["` | — |
| [SRC-686F71AA50-L000566](../../agents/task_understanding.py#L566) | 566 | `"            \"preserve_explicit_comparison_criteria\","` | — |
| [SRC-686F71AA50-L000567](../../agents/task_understanding.py#L567) | 567 | `"            \"do_not_collapse_multiple_dimensions_into_one_generic_answer\","` | — |
| [SRC-686F71AA50-L000568](../../agents/task_understanding.py#L568) | 568 | `"        ])"` | — |
| [SRC-686F71AA50-L000569](../../agents/task_understanding.py#L569) | 569 | `"        query_strategies.extend([\"one_query_per_criterion\", \"independent_comparison\"])"` | — |
| [SRC-686F71AA50-L000570](../../agents/task_understanding.py#L570) | 570 | `"    if len(explicit_aspects := aspect_values) > 1:"` | — |
| [SRC-686F71AA50-L000571](../../agents/task_understanding.py#L571) | 571 | `"        evidence_requirements.append(\"track_evidence_coverage_per_explicit_aspect\")"` | — |
| [SRC-686F71AA50-L000572](../../agents/task_understanding.py#L572) | 572 | `"        query_strategies.append(\"one_query_per_criterion\")"` | — |
| [SRC-686F71AA50-L000573](../../agents/task_understanding.py#L573) | 573 | `"    query_strategies = list(dict.fromkeys(query_strategies))"` | — |
| [SRC-686F71AA50-L000574](../../agents/task_understanding.py#L574) | 574 | `"    evidence_requirements = list(dict.fromkeys(evidence_requirements))"` | — |
| [SRC-686F71AA50-L000575](../../agents/task_understanding.py#L575) | 575 | `""` | — |
| [SRC-686F71AA50-L000576](../../agents/task_understanding.py#L576) | 576 | `"    location = _extract_explicit_locations(raw)"` | — |
| [SRC-686F71AA50-L000577](../../agents/task_understanding.py#L577) | 577 | `"    years = list(dict.fromkeys(_YEAR_RE.findall(raw)))"` | — |
| [SRC-686F71AA50-L000578](../../agents/task_understanding.py#L578) | 578 | `"    dates = list(dict.fromkeys(_DATE_RE.findall(raw)))"` | — |
| [SRC-686F71AA50-L000579](../../agents/task_understanding.py#L579) | 579 | `"    budgets = [m.group(0).strip()[:100] for m in _BUDGET_RE.finditer(raw)]"` | — |
| [SRC-686F71AA50-L000580](../../agents/task_understanding.py#L580) | 580 | `"    urls = list(dict.fromkeys(_URL_RE.findall(raw)))[:5]"` | — |
| [SRC-686F71AA50-L000581](../../agents/task_understanding.py#L581) | 581 | `"    inline_summary_text = _has_inline_summary_text(raw)"` | — |
| [SRC-686F71AA50-L000582](../../agents/task_understanding.py#L582) | 582 | `"    unresolved_followup = any(normalize_text(cue) in normalized for cue in _FOLLOWUP_CUES)"` | — |
| [SRC-686F71AA50-L000583](../../agents/task_understanding.py#L583) | 583 | `"    missing_required_inputs: list[str] = []"` | — |
| [SRC-686F71AA50-L000584](../../agents/task_understanding.py#L584) | 584 | `"    if intent_route == \"CLARIFY\":"` | — |
| [SRC-686F71AA50-L000585](../../agents/task_understanding.py#L585) | 585 | `"        missing_required_inputs.append(\"unresolved_referent_or_incomplete_request\")"` | — |
| [SRC-686F71AA50-L000586](../../agents/task_understanding.py#L586) | 586 | `"    if official_destination and not _has_official_site_target(raw):"` | — |
| [SRC-686F71AA50-L000587](../../agents/task_understanding.py#L587) | 587 | `"        missing_required_inputs.append(\"official_destination_target_entity\")"` | — |
| [SRC-686F71AA50-L000588](../../agents/task_understanding.py#L588) | 588 | `"    if family == \"summarize\" and not urls and not inline_summary_text:"` | — |
| [SRC-686F71AA50-L000589](../../agents/task_understanding.py#L589) | 589 | `"        missing_required_inputs.append(\"summary_source_url_or_pasted_text\")"` | — |
| [SRC-686F71AA50-L000590](../../agents/task_understanding.py#L590) | 590 | `"    context = dialogue_context if isinstance(dialogue_context, dict) else {}"` | — |
| [SRC-686F71AA50-L000591](../../agents/task_understanding.py#L591) | 591 | `"    explicit_aspects = list(dict.fromkeys(aspect_values))[:MAX_TASK_ASPECTS]"` | — |
| [SRC-686F71AA50-L000592](../../agents/task_understanding.py#L592) | 592 | `""` | — |
| [SRC-686F71AA50-L000593](../../agents/task_understanding.py#L593) | 593 | `"    # Hypotheses are alternatives considered by the deterministic classifier. Counts"` | — |
| [SRC-686F71AA50-L000594](../../agents/task_understanding.py#L594) | 594 | `"    # are matched lexical signals, not calibrated confidence or probability."` | — |
| [SRC-686F71AA50-L000595](../../agents/task_understanding.py#L595) | 595 | `"    hypothesis_rows: list[dict[str, Any]] = []"` | — |
| [SRC-686F71AA50-L000596](../../agents/task_understanding.py#L596) | 596 | `"    for candidate_family, signals in matches.items():"` | — |
| [SRC-686F71AA50-L000597](../../agents/task_understanding.py#L597) | 597 | `"        if signals:"` | — |
| [SRC-686F71AA50-L000598](../../agents/task_understanding.py#L598) | 598 | `"            hypothesis_rows.append({"` | — |
| [SRC-686F71AA50-L000599](../../agents/task_understanding.py#L599) | 599 | `"                \"family\": candidate_family,"` | — |
| [SRC-686F71AA50-L000600](../../agents/task_understanding.py#L600) | 600 | `"                \"matched_signal_count\": len(signals),"` | — |
| [SRC-686F71AA50-L000601](../../agents/task_understanding.py#L601) | 601 | `"                \"signals\": signals[:4],"` | — |
| [SRC-686F71AA50-L000602](../../agents/task_understanding.py#L602) | 602 | `"                \"status\": \"candidate_interpretation\","` | — |
| [SRC-686F71AA50-L000603](../../agents/task_understanding.py#L603) | 603 | `"            })"` | — |
| [SRC-686F71AA50-L000604](../../agents/task_understanding.py#L604) | 604 | `"    hypothesis_rows.sort("` | — |
| [SRC-686F71AA50-L000605](../../agents/task_understanding.py#L605) | 605 | `"        key=lambda item: (-item[\"matched_signal_count\"], item[\"family\"])"` | — |
| [SRC-686F71AA50-L000606](../../agents/task_understanding.py#L606) | 606 | `"    )"` | — |
| [SRC-686F71AA50-L000607](../../agents/task_understanding.py#L607) | 607 | `"    for item in hypothesis_rows:"` | — |
| [SRC-686F71AA50-L000608](../../agents/task_understanding.py#L608) | 608 | `"        item[\"selected\"] = item[\"family\"] == family"` | — |
| [SRC-686F71AA50-L000609](../../agents/task_understanding.py#L609) | 609 | `"    if len(hypothesis_rows) > 8:"` | — |
| [SRC-686F71AA50-L000610](../../agents/task_understanding.py#L610) | 610 | `"        hypothesis_rows = hypothesis_rows[:8]"` | — |
| [SRC-686F71AA50-L000611](../../agents/task_understanding.py#L611) | 611 | `""` | — |
| [SRC-686F71AA50-L000612](../../agents/task_understanding.py#L612) | 612 | `"    # A conflict is a reason to preserve alternatives in diagnostics, not a reason to"` | — |
| [SRC-686F71AA50-L000613](../../agents/task_understanding.py#L613) | 613 | `"    # invent certainty. High ambiguity is limited to unresolved references or a"` | — |
| [SRC-686F71AA50-L000614](../../agents/task_understanding.py#L614) | 614 | `"    # short fragment explicitly marked as contextual."` | — |
| [SRC-686F71AA50-L000615](../../agents/task_understanding.py#L615) | 615 | `"    unresolved = bool(missing_required_inputs) or bool(context.get(\"needs_clarification\")) or ("` | — |
| [SRC-686F71AA50-L000616](../../agents/task_understanding.py#L616) | 616 | `"        len(raw.strip()) <= 28 and unresolved_followup"` | — |
| [SRC-686F71AA50-L000617](../../agents/task_understanding.py#L617) | 617 | `"        and not context.get(\"resolved_question\")"` | — |
| [SRC-686F71AA50-L000618](../../agents/task_understanding.py#L618) | 618 | `"    )"` | — |
| [SRC-686F71AA50-L000619](../../agents/task_understanding.py#L619) | 619 | `"    if unresolved:"` | — |
| [SRC-686F71AA50-L000620](../../agents/task_understanding.py#L620) | 620 | `"        ambiguity_status = \"needs_clarification\""` | — |
| [SRC-686F71AA50-L000621](../../agents/task_understanding.py#L621) | 621 | `"    elif len(hypothesis_rows) >= 3:"` | — |
| [SRC-686F71AA50-L000622](../../agents/task_understanding.py#L622) | 622 | `"        ambiguity_status = \"multiple_overlapping_signals\""` | — |
| [SRC-686F71AA50-L000623](../../agents/task_understanding.py#L623) | 623 | `"    elif len(hypothesis_rows) == 2:"` | — |
| [SRC-686F71AA50-L000624](../../agents/task_understanding.py#L624) | 624 | `"        ambiguity_status = \"some_intent_overlap\""` | — |
| [SRC-686F71AA50-L000625](../../agents/task_understanding.py#L625) | 625 | `"    else:"` | — |
| [SRC-686F71AA50-L000626](../../agents/task_understanding.py#L626) | 626 | `"        ambiguity_status = \"no_strong_lexical_conflict_detected\""` | — |
| [SRC-686F71AA50-L000627](../../agents/task_understanding.py#L627) | 627 | `""` | — |
| [SRC-686F71AA50-L000628](../../agents/task_understanding.py#L628) | 628 | `"    # Tool requirements are advisory planning metadata, not executable permission."` | — |
| [SRC-686F71AA50-L000629](../../agents/task_understanding.py#L629) | 629 | `"    # A clarification route is a hard stop even when the UI has a research mode selected."` | — |
| [SRC-686F71AA50-L000630](../../agents/task_understanding.py#L630) | 630 | `"    route_is_clarification = intent_route == \"CLARIFY\""` | — |
| [SRC-686F71AA50-L000631](../../agents/task_understanding.py#L631) | 631 | `"    route_is_local = intent_route == \"LOCAL\""` | — |
| [SRC-686F71AA50-L000632](../../agents/task_understanding.py#L632) | 632 | `"    search_requested = ("` | — |
| [SRC-686F71AA50-L000633](../../agents/task_understanding.py#L633) | 633 | `"        intent_route in {\"WEB_SIMPLE\", \"WEB_DEEP\", \"LEAD_GENERATION\"}"` | — |
| [SRC-686F71AA50-L000634](../../agents/task_understanding.py#L634) | 634 | `"        or ("` | — |
| [SRC-686F71AA50-L000635](../../agents/task_understanding.py#L635) | 635 | `"            intent_route == \"deterministic_fallback\""` | — |
| [SRC-686F71AA50-L000636](../../agents/task_understanding.py#L636) | 636 | `"            and isinstance(plan, dict)"` | — |
| [SRC-686F71AA50-L000637](../../agents/task_understanding.py#L637) | 637 | `"            and bool(plan.get(\"queries\"))"` | — |
| [SRC-686F71AA50-L000638](../../agents/task_understanding.py#L638) | 638 | `"        )"` | — |
| [SRC-686F71AA50-L000639](../../agents/task_understanding.py#L639) | 639 | `"        or ("` | — |
| [SRC-686F71AA50-L000640](../../agents/task_understanding.py#L640) | 640 | `"            intent_route not in {\"LOCAL\", \"CLARIFY\", \"BUDGET_EXHAUSTED\"}"` | — |
| [SRC-686F71AA50-L000641](../../agents/task_understanding.py#L641) | 641 | `"            and ("` | — |
| [SRC-686F71AA50-L000642](../../agents/task_understanding.py#L642) | 642 | `"                social_required"` | — |
| [SRC-686F71AA50-L000643](../../agents/task_understanding.py#L643) | 643 | `"                or official_destination"` | — |
| [SRC-686F71AA50-L000644](../../agents/task_understanding.py#L644) | 644 | `"                or current_required"` | — |
| [SRC-686F71AA50-L000645](../../agents/task_understanding.py#L645) | 645 | `"                or family in {\"find_or_discover\", \"lead_generation\", \"general_research\"}"` | — |
| [SRC-686F71AA50-L000646](../../agents/task_understanding.py#L646) | 646 | `"                or ("` | — |
| [SRC-686F71AA50-L000647](../../agents/task_understanding.py#L647) | 647 | `"                    family == \"compare\""` | — |
| [SRC-686F71AA50-L000648](../../agents/task_understanding.py#L648) | 648 | `"                    and not inline_summary_text"` | — |
| [SRC-686F71AA50-L000649](../../agents/task_understanding.py#L649) | 649 | `"                )"` | — |
| [SRC-686F71AA50-L000650](../../agents/task_understanding.py#L650) | 650 | `"            )"` | — |
| [SRC-686F71AA50-L000651](../../agents/task_understanding.py#L651) | 651 | `"        )"` | — |
| [SRC-686F71AA50-L000652](../../agents/task_understanding.py#L652) | 652 | `"        or ("` | — |
| [SRC-686F71AA50-L000653](../../agents/task_understanding.py#L653) | 653 | `"            clean_mode != \"auto\""` | — |
| [SRC-686F71AA50-L000654](../../agents/task_understanding.py#L654) | 654 | `"            and not route_is_clarification"` | — |
| [SRC-686F71AA50-L000655](../../agents/task_understanding.py#L655) | 655 | `"            and not route_is_local"` | — |
| [SRC-686F71AA50-L000656](../../agents/task_understanding.py#L656) | 656 | `"        )"` | — |
| [SRC-686F71AA50-L000657](../../agents/task_understanding.py#L657) | 657 | `"    )"` | — |
| [SRC-686F71AA50-L000658](../../agents/task_understanding.py#L658) | 658 | `"    page_fetch_requested = bool(urls) or ("` | — |
| [SRC-686F71AA50-L000659](../../agents/task_understanding.py#L659) | 659 | `"        family == \"summarize\""` | — |
| [SRC-686F71AA50-L000660](../../agents/task_understanding.py#L660) | 660 | `"        and not inline_summary_text"` | — |
| [SRC-686F71AA50-L000661](../../agents/task_understanding.py#L661) | 661 | `"        and not route_is_clarification"` | — |
| [SRC-686F71AA50-L000662](../../agents/task_understanding.py#L662) | 662 | `"    )"` | — |
| [SRC-686F71AA50-L000663](../../agents/task_understanding.py#L663) | 663 | `"    tools: list[str] = []"` | — |
| [SRC-686F71AA50-L000664](../../agents/task_understanding.py#L664) | 664 | `"    if search_requested and not route_is_clarification:"` | — |
| [SRC-686F71AA50-L000665](../../agents/task_understanding.py#L665) | 665 | `"        tools.append(\"web_search\")"` | — |
| [SRC-686F71AA50-L000666](../../agents/task_understanding.py#L666) | 666 | `"    if page_fetch_requested and not route_is_clarification:"` | — |
| [SRC-686F71AA50-L000667](../../agents/task_understanding.py#L667) | 667 | `"        tools.append(\"page_fetch\")"` | — |
| [SRC-686F71AA50-L000668](../../agents/task_understanding.py#L668) | 668 | `"    if social_required and not route_is_clarification:"` | — |
| [SRC-686F71AA50-L000669](../../agents/task_understanding.py#L669) | 669 | `"        tools.append(\"public_social_search_if_configured\")"` | — |
| [SRC-686F71AA50-L000670](../../agents/task_understanding.py#L670) | 670 | `"    if ("` | — |
| [SRC-686F71AA50-L000671](../../agents/task_understanding.py#L671) | 671 | `"        intent_route in {\"MODEL_ONLY\", \"WEB_SIMPLE\", \"WEB_DEEP\", \"LEAD_GENERATION\", \"deterministic_fallback\"}"` | — |
| [SRC-686F71AA50-L000672](../../agents/task_understanding.py#L672) | 672 | `"        or (clean_mode != \"auto\" and not route_is_clarification and not route_is_local)"` | — |
| [SRC-686F71AA50-L000673](../../agents/task_understanding.py#L673) | 673 | `"    ):"` | — |
| [SRC-686F71AA50-L000674](../../agents/task_understanding.py#L674) | 674 | `"        tools.append(\"language_model_generation_if_configured\")"` | — |
| [SRC-686F71AA50-L000675](../../agents/task_understanding.py#L675) | 675 | `"    if tools and (\"web_search\" in tools or social_required) and not route_is_clarification:"` | — |
| [SRC-686F71AA50-L000676](../../agents/task_understanding.py#L676) | 676 | `"        tools.append(\"claim_review_if_configured\")"` | — |
| [SRC-686F71AA50-L000677](../../agents/task_understanding.py#L677) | 677 | `"    constraints = {"` | — |
| [SRC-686F71AA50-L000678](../../agents/task_understanding.py#L678) | 678 | `"        \"explicit_locations\": location,"` | — |
| [SRC-686F71AA50-L000679](../../agents/task_understanding.py#L679) | 679 | `"        \"explicit_years\": years,"` | — |
| [SRC-686F71AA50-L000680](../../agents/task_understanding.py#L680) | 680 | `"        \"explicit_dates\": dates,"` | — |
| [SRC-686F71AA50-L000681](../../agents/task_understanding.py#L681) | 681 | `"        \"explicit_budgets\": budgets,"` | — |
| [SRC-686F71AA50-L000682](../../agents/task_understanding.py#L682) | 682 | `"        \"explicit_urls\": urls,"` | — |
| [SRC-686F71AA50-L000683](../../agents/task_understanding.py#L683) | 683 | `"        \"explicit_aspects\": explicit_aspects,"` | — |
| [SRC-686F71AA50-L000684](../../agents/task_understanding.py#L684) | 684 | `"        \"inline_text_supplied_for_summary\": inline_summary_text,"` | — |
| [SRC-686F71AA50-L000685](../../agents/task_understanding.py#L685) | 685 | `"        \"time_sensitive_request\": current_required,"` | — |
| [SRC-686F71AA50-L000686](../../agents/task_understanding.py#L686) | 686 | `"        \"official_site_required\": government_official_site,"` | — |
| [SRC-686F71AA50-L000687](../../agents/task_understanding.py#L687) | 687 | `"        \"official_destination_required\": official_destination,"` | — |
| [SRC-686F71AA50-L000688](../../agents/task_understanding.py#L688) | 688 | `"        \"social_evidence_requested\": social_required,"` | — |
| [SRC-686F71AA50-L000689](../../agents/task_understanding.py#L689) | 689 | `"        \"language_profile\": _language_profile(raw),"` | — |
| [SRC-686F71AA50-L000690](../../agents/task_understanding.py#L690) | 690 | `"        \"source_policy\": ("` | — |
| [SRC-686F71AA50-L000691](../../agents/task_understanding.py#L691) | 691 | `"            \"government_official_destination\" if government_official_site"` | — |
| [SRC-686F71AA50-L000692](../../agents/task_understanding.py#L692) | 692 | `"            else \"official_destination\" if official_destination"` | — |
| [SRC-686F71AA50-L000693](../../agents/task_understanding.py#L693) | 693 | `"            else \"current_read_page\" if current_required"` | — |
| [SRC-686F71AA50-L000694](../../agents/task_understanding.py#L694) | 694 | `"            else \"public_social_content\" if social_required"` | — |
| [SRC-686F71AA50-L000695](../../agents/task_understanding.py#L695) | 695 | `"            else \"task_relevant_sources\""` | — |
| [SRC-686F71AA50-L000696](../../agents/task_understanding.py#L696) | 696 | `"        ),"` | — |
| [SRC-686F71AA50-L000697](../../agents/task_understanding.py#L697) | 697 | `"        \"source_policies\": list(dict.fromkeys("` | — |
| [SRC-686F71AA50-L000698](../../agents/task_understanding.py#L698) | 698 | `"            ([\"government_official_destination\"] if government_official_site else [])"` | — |
| [SRC-686F71AA50-L000699](../../agents/task_understanding.py#L699) | 699 | `"            + ([\"official_destination\"] if official_destination else [])"` | — |
| [SRC-686F71AA50-L000700](../../agents/task_understanding.py#L700) | 700 | `"            + ([\"current_read_page\"] if current_required else [])"` | — |
| [SRC-686F71AA50-L000701](../../agents/task_understanding.py#L701) | 701 | `"            + ([\"public_social_content\"] if social_required else [])"` | — |
| [SRC-686F71AA50-L000702](../../agents/task_understanding.py#L702) | 702 | `"            + ([\"task_relevant_sources\"] if not (government_official_site or official_destination or current_required or social_required) else [])"` | — |
| [SRC-686F71AA50-L000703](../../agents/task_understanding.py#L703) | 703 | `"        )),"` | — |
| [SRC-686F71AA50-L000704](../../agents/task_understanding.py#L704) | 704 | `"    }"` | — |
| [SRC-686F71AA50-L000705](../../agents/task_understanding.py#L705) | 705 | `"    spec = {"` | — |
| [SRC-686F71AA50-L000706](../../agents/task_understanding.py#L706) | 706 | `"        \"schema\": \"omarai.task_spec.v1\","` | — |
| [SRC-686F71AA50-L000707](../../agents/task_understanding.py#L707) | 707 | `"        \"task_family\": family,"` | — |
| [SRC-686F71AA50-L000708](../../agents/task_understanding.py#L708) | 708 | `"        \"mode\": clean_mode,"` | — |
| [SRC-686F71AA50-L000709](../../agents/task_understanding.py#L709) | 709 | `"        \"intent_route\": intent_route or \"unassessed\","` | — |
| [SRC-686F71AA50-L000710](../../agents/task_understanding.py#L710) | 710 | `"        \"normalization\": \"unicode_nfkc_arabic_diacritic_and_letter_normalization\","` | — |
| [SRC-686F71AA50-L000711](../../agents/task_understanding.py#L711) | 711 | `"        \"classification_method\": \"deterministic_multi_pattern_hypotheses\","` | — |
| [SRC-686F71AA50-L000712](../../agents/task_understanding.py#L712) | 712 | `"        \"classification_is_probability\": False,"` | — |
| [SRC-686F71AA50-L000713](../../agents/task_understanding.py#L713) | 713 | `"        \"ambiguity_status\": ambiguity_status,"` | — |
| [SRC-686F71AA50-L000714](../../agents/task_understanding.py#L714) | 714 | `"        \"missing_required_inputs\": list(dict.fromkeys(missing_required_inputs)),"` | — |
| [SRC-686F71AA50-L000715](../../agents/task_understanding.py#L715) | 715 | `"        \"requires_clarification\": ambiguity_status == \"needs_clarification\","` | — |
| [SRC-686F71AA50-L000716](../../agents/task_understanding.py#L716) | 716 | `"        \"clarification_reason\": ("` | — |
| [SRC-686F71AA50-L000717](../../agents/task_understanding.py#L717) | 717 | `"            \"missing_required_input\""` | — |
| [SRC-686F71AA50-L000718](../../agents/task_understanding.py#L718) | 718 | `"            if missing_required_inputs"` | — |
| [SRC-686F71AA50-L000719](../../agents/task_understanding.py#L719) | 719 | `"            else \"no_strong_lexical_conflict_detected\""` | — |
| [SRC-686F71AA50-L000720](../../agents/task_understanding.py#L720) | 720 | `"        ),"` | — |
| [SRC-686F71AA50-L000721](../../agents/task_understanding.py#L721) | 721 | `"        \"hypothesis_interpretations\": hypothesis_rows,"` | — |
| [SRC-686F71AA50-L000722](../../agents/task_understanding.py#L722) | 722 | `"        \"constraints\": constraints,"` | — |
| [SRC-686F71AA50-L000723](../../agents/task_understanding.py#L723) | 723 | `"        \"output_preferences\": {"` | — |
| [SRC-686F71AA50-L000724](../../agents/task_understanding.py#L724) | 724 | `"            \"concise\": bool(output_matches[\"output_concise\"]),"` | — |
| [SRC-686F71AA50-L000725](../../agents/task_understanding.py#L725) | 725 | `"            \"detailed\": bool(output_matches[\"output_detailed\"]),"` | — |
| [SRC-686F71AA50-L000726](../../agents/task_understanding.py#L726) | 726 | `"            \"examples_requested\": bool(output_matches[\"output_examples\"]),"` | — |
| [SRC-686F71AA50-L000727](../../agents/task_understanding.py#L727) | 727 | `"            \"table_requested\": bool(output_matches[\"output_table\"]),"` | — |
| [SRC-686F71AA50-L000728](../../agents/task_understanding.py#L728) | 728 | `"            \"bullets_or_checklist_requested\": bool(output_matches[\"output_bullets\"]),"` | — |
| [SRC-686F71AA50-L000729](../../agents/task_understanding.py#L729) | 729 | `"        },"` | — |
| [SRC-686F71AA50-L000730](../../agents/task_understanding.py#L730) | 730 | `"        \"evidence_requirements\": evidence_requirements,"` | — |
| [SRC-686F71AA50-L000731](../../agents/task_understanding.py#L731) | 731 | `"        \"query_strategies\": query_strategies,"` | — |
| [SRC-686F71AA50-L000732](../../agents/task_understanding.py#L732) | 732 | `"        \"tool_requirements\": list(dict.fromkeys(tools)),"` | — |
| [SRC-686F71AA50-L000733](../../agents/task_understanding.py#L733) | 733 | `"        \"decision_checks\": ["` | — |
| [SRC-686F71AA50-L000734](../../agents/task_understanding.py#L734) | 734 | `"            \"resolve_context_without_carrying_stale_topic\","` | — |
| [SRC-686F71AA50-L000735](../../agents/task_understanding.py#L735) | 735 | `"            \"preserve_explicit_entities_and_constraints\","` | — |
| [SRC-686F71AA50-L000736](../../agents/task_understanding.py#L736) | 736 | `"            \"validate_topic_relevance\","` | — |
| [SRC-686F71AA50-L000737](../../agents/task_understanding.py#L737) | 737 | `"            \"apply_mode_specific_source_guardrails\","` | — |
| [SRC-686F71AA50-L000738](../../agents/task_understanding.py#L738) | 738 | `"            \"distinguish_search_result_snippet_from_read_page\","` | — |
| [SRC-686F71AA50-L000739](../../agents/task_understanding.py#L739) | 739 | `"            \"report_each_failed_stage\","` | — |
| [SRC-686F71AA50-L000740](../../agents/task_understanding.py#L740) | 740 | `"            \"cite_claims_or_abstain_when_evidence_is_insufficient\","` | — |
| [SRC-686F71AA50-L000741](../../agents/task_understanding.py#L741) | 741 | `"        ],"` | — |
| [SRC-686F71AA50-L000742](../../agents/task_understanding.py#L742) | 742 | `"        \"limits\": {"` | — |
| [SRC-686F71AA50-L000743](../../agents/task_understanding.py#L743) | 743 | `"            \"max_question_chars\": MAX_TASK_CHARS,"` | — |
| [SRC-686F71AA50-L000744](../../agents/task_understanding.py#L744) | 744 | `"            \"max_aspects\": MAX_TASK_ASPECTS,"` | — |
| [SRC-686F71AA50-L000745](../../agents/task_understanding.py#L745) | 745 | `"            \"max_query_strategies\": MAX_STRATEGY_QUERIES,"` | — |
| [SRC-686F71AA50-L000746](../../agents/task_understanding.py#L746) | 746 | `"        },"` | — |
| [SRC-686F71AA50-L000747](../../agents/task_understanding.py#L747) | 747 | `"        \"claim\": \"task planning metadata only; not semantic certainty or factual verification\","` | — |
| [SRC-686F71AA50-L000748](../../agents/task_understanding.py#L748) | 748 | `"    }"` | — |
| [SRC-686F71AA50-L000749](../../agents/task_understanding.py#L749) | 749 | `"    if plan and isinstance(plan, dict):"` | — |
| [SRC-686F71AA50-L000750](../../agents/task_understanding.py#L750) | 750 | `"        spec[\"planner_freshness\"] = str(plan.get(\"freshness\") or \"unknown\")"` | — |
| [SRC-686F71AA50-L000751](../../agents/task_understanding.py#L751) | 751 | `"        spec[\"planner_depth\"] = str(plan.get(\"depth\") or \"unknown\")"` | — |
| [SRC-686F71AA50-L000752](../../agents/task_understanding.py#L752) | 752 | `"    return spec"` | — |
| [SRC-686F71AA50-L000753](../../agents/task_understanding.py#L753) | 753 | `""` | — |
| [SRC-686F71AA50-L000754](../../agents/task_understanding.py#L754) | 754 | `""` | — |
| [SRC-686F71AA50-L000755](../../agents/task_understanding.py#L755) | 755 | `"def _query_key(value: str) -> str:"` | — |
| [SRC-686F71AA50-L000756](../../agents/task_understanding.py#L756) | 756 | `"    return normalize_text(value)"` | — |
| [SRC-686F71AA50-L000757](../../agents/task_understanding.py#L757) | 757 | `""` | — |
| [SRC-686F71AA50-L000758](../../agents/task_understanding.py#L758) | 758 | `""` | — |
| [SRC-686F71AA50-L000759](../../agents/task_understanding.py#L759) | 759 | `"def _generated_strategy_candidates(topic: str, spec: dict[str, Any]) -> list[tuple[str, str, str]]:"` | — |
| [SRC-686F71AA50-L000760](../../agents/task_understanding.py#L760) | 760 | `"    family = str(spec.get(\"task_family\") or \"\")"` | — |
| [SRC-686F71AA50-L000761](../../agents/task_understanding.py#L761) | 761 | `"    constraints = spec.get(\"constraints\") if isinstance(spec.get(\"constraints\"), dict) else {}"` | — |
| [SRC-686F71AA50-L000762](../../agents/task_understanding.py#L762) | 762 | `"    aspects = constraints.get(\"explicit_aspects\") if isinstance(constraints.get(\"explicit_aspects\"), list) else []"` | — |
| [SRC-686F71AA50-L000763](../../agents/task_understanding.py#L763) | 763 | `"    candidates: list[tuple[str, str, str]] = []"` | — |
| [SRC-686F71AA50-L000764](../../agents/task_understanding.py#L764) | 764 | `"    if not topic.strip():"` | — |
| [SRC-686F71AA50-L000765](../../agents/task_understanding.py#L765) | 765 | `"        return candidates"` | — |
| [SRC-686F71AA50-L000766](../../agents/task_understanding.py#L766) | 766 | `"    locations = constraints.get(\"explicit_locations\") or []"` | — |
| [SRC-686F71AA50-L000767](../../agents/task_understanding.py#L767) | 767 | `"    location_suffix = \" \".join(str(item) for item in locations[:2])"` | — |
| [SRC-686F71AA50-L000768](../../agents/task_understanding.py#L768) | 768 | `"    hypotheses = spec.get(\"hypothesis_interpretations\")"` | — |
| [SRC-686F71AA50-L000769](../../agents/task_understanding.py#L769) | 769 | `"    hypothesis_families = {"` | — |
| [SRC-686F71AA50-L000770](../../agents/task_understanding.py#L770) | 770 | `"        str(item.get(\"family\"))"` | — |
| [SRC-686F71AA50-L000771](../../agents/task_understanding.py#L771) | 771 | `"        for item in hypotheses"` | — |
| [SRC-686F71AA50-L000772](../../agents/task_understanding.py#L772) | 772 | `"        if isinstance(item, dict) and item.get(\"family\")"` | — |
| [SRC-686F71AA50-L000773](../../agents/task_understanding.py#L773) | 773 | `"    } if isinstance(hypotheses, list) else set()"` | — |
| [SRC-686F71AA50-L000774](../../agents/task_understanding.py#L774) | 774 | `"    if family == \"official_site_lookup\" or constraints.get(\"official_destination_required\"):"` | — |
| [SRC-686F71AA50-L000775](../../agents/task_understanding.py#L775) | 775 | `"        candidates.extend(["` | — |
| [SRC-686F71AA50-L000776](../../agents/task_understanding.py#L776) | 776 | `"            (f\"{topic} الموقع الرسمي\", \"official_destination\", \"exact official-site discovery\"),"` | — |
| [SRC-686F71AA50-L000777](../../agents/task_understanding.py#L777) | 777 | `"            (f\"{topic} official website government portal\", \"official_domain\", \"cross-language destination discovery\"),"` | — |
| [SRC-686F71AA50-L000778](../../agents/task_understanding.py#L778) | 778 | `"        ])"` | — |
| [SRC-686F71AA50-L000779](../../agents/task_understanding.py#L779) | 779 | `"    if constraints.get(\"time_sensitive_request\"):"` | — |
| [SRC-686F71AA50-L000780](../../agents/task_understanding.py#L780) | 780 | `"        candidates.extend(["` | — |
| [SRC-686F71AA50-L000781](../../agents/task_understanding.py#L781) | 781 | `"            (f\"{topic} تحديث رسمي حديث {location_suffix}\".strip(), \"recent_official_update\", \"current-state fact requires fresh primary evidence\"),"` | — |
| [SRC-686F71AA50-L000782](../../agents/task_understanding.py#L782) | 782 | `"            (f\"{topic} latest official update {location_suffix}\".strip(), \"recent_official_update_en\", \"alternate language and source wording\"),"` | — |
| [SRC-686F71AA50-L000783](../../agents/task_understanding.py#L783) | 783 | `"        ])"` | — |
| [SRC-686F71AA50-L000784](../../agents/task_understanding.py#L784) | 784 | `"    if family == \"social_opinions\" or constraints.get(\"social_evidence_requested\"):"` | — |
| [SRC-686F71AA50-L000785](../../agents/task_understanding.py#L785) | 785 | `"        candidates.extend(["` | — |
| [SRC-686F71AA50-L000786](../../agents/task_understanding.py#L786) | 786 | `"            (f\"{topic} تجارب مستخدمين آراء الملاك {location_suffix}\".strip(), \"personal_experience_ar\", \"search for first-person experience rather than generic product mentions\"),"` | — |
| [SRC-686F71AA50-L000787](../../agents/task_understanding.py#L787) | 787 | `"            (f\"{topic} owner experience review {location_suffix}\".strip(), \"personal_experience_en\", \"cross-language owner-experience discovery\"),"` | — |
| [SRC-686F71AA50-L000788](../../agents/task_understanding.py#L788) | 788 | `"            (f\"{topic} common complaints discussion\", \"discussion_and_complaints\", \"look for contrasting experiences and discussions\"),"` | — |
| [SRC-686F71AA50-L000789](../../agents/task_understanding.py#L789) | 789 | `"        ])"` | — |
| [SRC-686F71AA50-L000790](../../agents/task_understanding.py#L790) | 790 | `"    if family == \"compare\" or \"compare\" in hypothesis_families:"` | — |
| [SRC-686F71AA50-L000791](../../agents/task_understanding.py#L791) | 791 | `"        for aspect in aspects[:MAX_TASK_ASPECTS]:"` | — |
| [SRC-686F71AA50-L000792](../../agents/task_understanding.py#L792) | 792 | `"            candidates.append((f\"{topic} {aspect}\", \"explicit_criterion\", f\"separate evidence retrieval for criterion: {aspect}\"))"` | — |
| [SRC-686F71AA50-L000793](../../agents/task_understanding.py#L793) | 793 | `"        candidates.extend(["` | — |
| [SRC-686F71AA50-L000794](../../agents/task_understanding.py#L794) | 794 | `"            (f\"{topic} official specifications\", \"primary_specification\", \"separate technical specifications from opinion\"),"` | — |
| [SRC-686F71AA50-L000795](../../agents/task_understanding.py#L795) | 795 | `"            (f\"{topic} independent comparison pros cons\", \"independent_comparison\", \"seek comparative analysis and trade-offs\"),"` | — |
| [SRC-686F71AA50-L000796](../../agents/task_understanding.py#L796) | 796 | `"        ])"` | — |
| [SRC-686F71AA50-L000797](../../agents/task_understanding.py#L797) | 797 | `"    if family == \"troubleshoot\" or \"troubleshoot\" in hypothesis_families:"` | — |
| [SRC-686F71AA50-L000798](../../agents/task_understanding.py#L798) | 798 | `"        candidates.extend(["` | — |
| [SRC-686F71AA50-L000799](../../agents/task_understanding.py#L799) | 799 | `"            (f\"{topic} الأعطال الشائعة الأسباب والحلول\", \"failure_modes_ar\", \"search causes and remedies without treating hypotheses as confirmed\"),"` | — |
| [SRC-686F71AA50-L000800](../../agents/task_understanding.py#L800) | 800 | `"            (f\"{topic} troubleshooting common failures official manual\", \"failure_modes_en\", \"technical cross-language search and primary manual\"),"` | — |
| [SRC-686F71AA50-L000801](../../agents/task_understanding.py#L801) | 801 | `"        ])"` | — |
| [SRC-686F71AA50-L000802](../../agents/task_understanding.py#L802) | 802 | `"    if family == \"how_to\" or \"how_to\" in hypothesis_families:"` | — |
| [SRC-686F71AA50-L000803](../../agents/task_understanding.py#L803) | 803 | `"        candidates.extend(["` | — |
| [SRC-686F71AA50-L000804](../../agents/task_understanding.py#L804) | 804 | `"            (f\"{topic} خطوات شرح دليل رسمي\", \"procedural_guide_ar\", \"seek stepwise procedure and applicable prerequisites\"),"` | — |
| [SRC-686F71AA50-L000805](../../agents/task_understanding.py#L805) | 805 | `"            (f\"{topic} official guide steps\", \"procedural_guide_en\", \"cross-language guide discovery\"),"` | — |
| [SRC-686F71AA50-L000806](../../agents/task_understanding.py#L806) | 806 | `"        ])"` | — |
| [SRC-686F71AA50-L000807](../../agents/task_understanding.py#L807) | 807 | `"    if family == \"recommendation\" or \"recommendation\" in hypothesis_families:"` | — |
| [SRC-686F71AA50-L000808](../../agents/task_understanding.py#L808) | 808 | `"        candidates.extend(["` | — |
| [SRC-686F71AA50-L000809](../../agents/task_understanding.py#L809) | 809 | `"            (f\"{topic} المميزات العيوب البدائل\", \"tradeoffs_ar\", \"compare trade-offs and alternatives\"),"` | — |
| [SRC-686F71AA50-L000810](../../agents/task_understanding.py#L810) | 810 | `"            (f\"{topic} pros cons alternatives review\", \"tradeoffs_en\", \"cross-language alternatives discovery\"),"` | — |
| [SRC-686F71AA50-L000811](../../agents/task_understanding.py#L811) | 811 | `"        ])"` | — |
| [SRC-686F71AA50-L000812](../../agents/task_understanding.py#L812) | 812 | `"    if family == \"lead_generation\" or \"lead_generation\" in hypothesis_families:"` | — |
| [SRC-686F71AA50-L000813](../../agents/task_understanding.py#L813) | 813 | `"        candidates.extend(["` | — |
| [SRC-686F71AA50-L000814](../../agents/task_understanding.py#L814) | 814 | `"            (f\"{topic} شخص يبحث عن شراء تجربة سؤال\", \"buyer_intent_ar\", \"distinguish explicit buyer intent from product advertisements\"),"` | — |
| [SRC-686F71AA50-L000815](../../agents/task_understanding.py#L815) | 815 | `"            (f\"{topic} looking to buy seeking recommendations\", \"buyer_intent_en\", \"search public discussions for intent signals\"),"` | — |
| [SRC-686F71AA50-L000816](../../agents/task_understanding.py#L816) | 816 | `"        ])"` | — |
| [SRC-686F71AA50-L000817](../../agents/task_understanding.py#L817) | 817 | `"    normalized_topic = normalize_text(topic)"` | — |
| [SRC-686F71AA50-L000818](../../agents/task_understanding.py#L818) | 818 | `"    property_topic = any("` | — |
| [SRC-686F71AA50-L000819](../../agents/task_understanding.py#L819) | 819 | `"        cue in normalized_topic"` | — |
| [SRC-686F71AA50-L000820](../../agents/task_understanding.py#L820) | 820 | `"        for cue in (\"شقه\", \"شقق\", \"عقار\", \"عقارات\", \"عقاري\", \"real estate\", \"apartment\", \"property\")"` | — |
| [SRC-686F71AA50-L000821](../../agents/task_understanding.py#L821) | 821 | `"    )"` | — |
| [SRC-686F71AA50-L000822](../../agents/task_understanding.py#L822) | 822 | `"    if family == \"find_or_discover\" and property_topic:"` | — |
| [SRC-686F71AA50-L000823](../../agents/task_understanding.py#L823) | 823 | `"        candidates.extend(["` | — |
| [SRC-686F71AA50-L000824](../../agents/task_understanding.py#L824) | 824 | `"            (f\"{topic} إعلانات عقارية\", \"property_listings\", \"discover relevant listings without treating ads as independent price evidence\"),"` | — |
| [SRC-686F71AA50-L000825](../../agents/task_understanding.py#L825) | 825 | `"            (f\"{topic} متوسط أسعار السوق للمتر\", \"property_market_price_per_meter\", \"compare asking prices against market-level context\"),"` | — |
| [SRC-686F71AA50-L000826](../../agents/task_understanding.py#L826) | 826 | `"            (f\"{topic} أسعار البيع الفعلية والتقييم العقاري\", \"property_transaction_price_check\", \"distinguish asking prices from completed transaction prices\"),"` | — |
| [SRC-686F71AA50-L000827](../../agents/task_understanding.py#L827) | 827 | `"        ])"` | — |
| [SRC-686F71AA50-L000828](../../agents/task_understanding.py#L828) | 828 | `"    if ("` | — |
| [SRC-686F71AA50-L000829](../../agents/task_understanding.py#L829) | 829 | `"        family in {\"general_research\", \"web_research\", \"find_or_discover\"}"` | — |
| [SRC-686F71AA50-L000830](../../agents/task_understanding.py#L830) | 830 | `"        and ("` | — |
| [SRC-686F71AA50-L000831](../../agents/task_understanding.py#L831) | 831 | `"            spec.get(\"mode\") in {\"deep\", \"latest\", \"social\"}"` | — |
| [SRC-686F71AA50-L000832](../../agents/task_understanding.py#L832) | 832 | `"            or constraints.get(\"time_sensitive_request\")"` | — |
| [SRC-686F71AA50-L000833](../../agents/task_understanding.py#L833) | 833 | `"            or spec.get(\"planner_depth\") == \"deep\""` | — |
| [SRC-686F71AA50-L000834](../../agents/task_understanding.py#L834) | 834 | `"            or spec.get(\"intent_route\") in {\"WEB_DEEP\", \"LEAD_GENERATION\"}"` | — |
| [SRC-686F71AA50-L000835](../../agents/task_understanding.py#L835) | 835 | `"        )"` | — |
| [SRC-686F71AA50-L000836](../../agents/task_understanding.py#L836) | 836 | `"    ):"` | — |
| [SRC-686F71AA50-L000837](../../agents/task_understanding.py#L837) | 837 | `"        candidates.extend(["` | — |
| [SRC-686F71AA50-L000838](../../agents/task_understanding.py#L838) | 838 | `"            (f\"{topic} مصدر رسمي\", \"primary_source_ar\", \"prefer an original or primary source when appropriate\"),"` | — |
| [SRC-686F71AA50-L000839](../../agents/task_understanding.py#L839) | 839 | `"            (f\"{topic} official source report\", \"primary_source_en\", \"alternate source-oriented search wording\"),"` | — |
| [SRC-686F71AA50-L000840](../../agents/task_understanding.py#L840) | 840 | `"            (f\"{topic} limitations risks independent analysis\", \"independent_analysis\", \"seek counterevidence and limitations\"),"` | — |
| [SRC-686F71AA50-L000841](../../agents/task_understanding.py#L841) | 841 | `"        ])"` | — |
| [SRC-686F71AA50-L000842](../../agents/task_understanding.py#L842) | 842 | `"    if ("` | — |
| [SRC-686F71AA50-L000843](../../agents/task_understanding.py#L843) | 843 | `"        not candidates"` | — |
| [SRC-686F71AA50-L000844](../../agents/task_understanding.py#L844) | 844 | `"        and family not in {\"general_question\", \"ambiguous_or_incomplete\"}"` | — |
| [SRC-686F71AA50-L000845](../../agents/task_understanding.py#L845) | 845 | `"        and ("` | — |
| [SRC-686F71AA50-L000846](../../agents/task_understanding.py#L846) | 846 | `"            spec.get(\"mode\") in {\"deep\", \"latest\", \"social\"}"` | — |
| [SRC-686F71AA50-L000847](../../agents/task_understanding.py#L847) | 847 | `"            or spec.get(\"intent_route\") in {\"WEB_DEEP\", \"LEAD_GENERATION\"}"` | — |
| [SRC-686F71AA50-L000848](../../agents/task_understanding.py#L848) | 848 | `"        )"` | — |
| [SRC-686F71AA50-L000849](../../agents/task_understanding.py#L849) | 849 | `"    ):"` | — |
| [SRC-686F71AA50-L000850](../../agents/task_understanding.py#L850) | 850 | `"        candidates.append("` | — |
| [SRC-686F71AA50-L000851](../../agents/task_understanding.py#L851) | 851 | `"            (f\"{topic} مصدر موثوق\", \"source_oriented_alternative\", \"search wording is a hypothesis, not evidence\")"` | — |
| [SRC-686F71AA50-L000852](../../agents/task_understanding.py#L852) | 852 | `"        )"` | — |
| [SRC-686F71AA50-L000853](../../agents/task_understanding.py#L853) | 853 | `"    return candidates"` | — |
| [SRC-686F71AA50-L000854](../../agents/task_understanding.py#L854) | 854 | `""` | — |
| [SRC-686F71AA50-L000855](../../agents/task_understanding.py#L855) | 855 | `""` | — |
| [SRC-686F71AA50-L000856](../../agents/task_understanding.py#L856) | 856 | `"def _label_existing_query(query: str, index: int, spec: dict[str, Any]) -> tuple[str, str]:"` | — |
| [SRC-686F71AA50-L000857](../../agents/task_understanding.py#L857) | 857 | `"    \"\"\"Classify query wording for diagnostics; this is not a retrieval-success claim.\"\"\""` | — |
| [SRC-686F71AA50-L000858](../../agents/task_understanding.py#L858) | 858 | `"    normalized = normalize_text(query)"` | — |
| [SRC-686F71AA50-L000859](../../agents/task_understanding.py#L859) | 859 | `"    constraints = spec.get(\"constraints\") if isinstance(spec.get(\"constraints\"), dict) else {}"` | — |
| [SRC-686F71AA50-L000860](../../agents/task_understanding.py#L860) | 860 | `"    if re.search(r\"\\bsite\\s*:\", query, flags=re.IGNORECASE):"` | — |
| [SRC-686F71AA50-L000861](../../agents/task_understanding.py#L861) | 861 | `"        return \"platform_scoped\", \"query explicitly scopes a public site or platform\""` | — |
| [SRC-686F71AA50-L000862](../../agents/task_understanding.py#L862) | 862 | `"    if constraints.get(\"official_destination_required\") and any("` | — |
| [SRC-686F71AA50-L000863](../../agents/task_understanding.py#L863) | 863 | `"        marker in normalized for marker in (\"الموقع الرسمي\", \"official website\", \"official site\")"` | — |
| [SRC-686F71AA50-L000864](../../agents/task_understanding.py#L864) | 864 | `"    ):"` | — |
| [SRC-686F71AA50-L000865](../../agents/task_understanding.py#L865) | 865 | `"        return \"official_destination\", \"query wording seeks an official destination\""` | — |
| [SRC-686F71AA50-L000866](../../agents/task_understanding.py#L866) | 866 | `"    if constraints.get(\"time_sensitive_request\") and any("` | — |
| [SRC-686F71AA50-L000867](../../agents/task_understanding.py#L867) | 867 | `"        marker in normalized for marker in (\"latest\", \"recent\", \"today\", \"تحديث\", \"حديث\", \"احدث\", \"اخر\")"` | — |
| [SRC-686F71AA50-L000868](../../agents/task_understanding.py#L868) | 868 | `"    ):"` | — |
| [SRC-686F71AA50-L000869](../../agents/task_understanding.py#L869) | 869 | `"        return \"recent_information\", \"query wording seeks current information; dates and page readability still require validation\""` | — |
| [SRC-686F71AA50-L000870](../../agents/task_understanding.py#L870) | 870 | `"    if any(marker in normalized for marker in (\"تجارب\", \"اراء\", \"تجربه\", \"experience\", \"owner review\", \"user review\")):"` | — |
| [SRC-686F71AA50-L000871](../../agents/task_understanding.py#L871) | 871 | `"        return \"personal_experience\", \"query wording targets user experience; the author's identity and truth remain unverified\""` | — |
| [SRC-686F71AA50-L000872](../../agents/task_understanding.py#L872) | 872 | `"    if any(marker in normalized for marker in (\"اعطال\", \"الاسباب\", \"الحلول\", \"troubleshooting\", \"common failures\")):"` | — |
| [SRC-686F71AA50-L000873](../../agents/task_understanding.py#L873) | 873 | `"        return \"troubleshooting\", \"query wording targets symptoms, causes, or remedies\""` | — |
| [SRC-686F71AA50-L000874](../../agents/task_understanding.py#L874) | 874 | `"    if any(marker in normalized for marker in (\"المقارنة\", \"مقارنة\", \"قارن\", \"comparison\", \"versus\", \"pros cons\", \"trade offs\")):"` | — |
| [SRC-686F71AA50-L000875](../../agents/task_understanding.py#L875) | 875 | `"        return \"comparison\", \"query wording targets a comparison or trade-off analysis\""` | — |
| [SRC-686F71AA50-L000876](../../agents/task_understanding.py#L876) | 876 | `"    if any(marker in normalized for marker in (\"مصدر رسمي\", \"official source\", \"manual\", \"specifications\", \"مواصفات\")):"` | — |
| [SRC-686F71AA50-L000877](../../agents/task_understanding.py#L877) | 877 | `"        return \"primary_source\", \"query wording seeks a primary or technical source\""` | — |
| [SRC-686F71AA50-L000878](../../agents/task_understanding.py#L878) | 878 | `"    if index == 0:"` | — |
| [SRC-686F71AA50-L000879](../../agents/task_understanding.py#L879) | 879 | `"        return \"planner_seed\", \"initial planner query; relevance and source quality are validated later\""` | — |
| [SRC-686F71AA50-L000880](../../agents/task_understanding.py#L880) | 880 | `"    return \"planner_alternative\", \"alternate planner query; label is inferred from wording/position\""` | — |
| [SRC-686F71AA50-L000881](../../agents/task_understanding.py#L881) | 881 | `""` | — |
| [SRC-686F71AA50-L000882](../../agents/task_understanding.py#L882) | 882 | `""` | — |
| [SRC-686F71AA50-L000883](../../agents/task_understanding.py#L883) | 883 | `"def build_query_strategy_matrix("` | — |
| [SRC-686F71AA50-L000884](../../agents/task_understanding.py#L884) | 884 | `"    question: str,"` | — |
| [SRC-686F71AA50-L000885](../../agents/task_understanding.py#L885) | 885 | `"    task_spec: dict[str, Any],"` | — |
| [SRC-686F71AA50-L000886](../../agents/task_understanding.py#L886) | 886 | `"    existing_queries: Any,"` | — |
| [SRC-686F71AA50-L000887](../../agents/task_understanding.py#L887) | 887 | `"    *,"` | — |
| [SRC-686F71AA50-L000888](../../agents/task_understanding.py#L888) | 888 | `"    limit: int = MAX_STRATEGY_QUERIES,"` | — |
| [SRC-686F71AA50-L000889](../../agents/task_understanding.py#L889) | 889 | `"    compact_fn: Any = None,"` | — |
| [SRC-686F71AA50-L000890](../../agents/task_understanding.py#L890) | 890 | `") -> list[dict[str, str]]:"` | — |
| [SRC-686F71AA50-L000891](../../agents/task_understanding.py#L891) | 891 | `"    \"\"\"Return bounded query candidates, prioritizing task-specific evidence strategies."` | — |
| [SRC-686F71AA50-L000892](../../agents/task_understanding.py#L892) | 892 | `""` | — |
| [SRC-686F71AA50-L000893](../../agents/task_understanding.py#L893) | 893 | `"    The first existing planner query anchors the topic. Task-aware queries are then"` | — |
| [SRC-686F71AA50-L000894](../../agents/task_understanding.py#L894) | 894 | `"    considered before secondary planner queries, so generic alternatives cannot consume"` | — |
| [SRC-686F71AA50-L000895](../../agents/task_understanding.py#L895) | 895 | `"    the whole budget and crowd out explicit user criteria."` | — |
| [SRC-686F71AA50-L000896](../../agents/task_understanding.py#L896) | 896 | `"    \"\"\""` | — |
| [SRC-686F71AA50-L000897](../../agents/task_understanding.py#L897) | 897 | `"    maximum = max(1, min(int(limit), MAX_STRATEGY_QUERIES))"` | — |
| [SRC-686F71AA50-L000898](../../agents/task_understanding.py#L898) | 898 | `"    spec = task_spec if isinstance(task_spec, dict) else {}"` | — |
| [SRC-686F71AA50-L000899](../../agents/task_understanding.py#L899) | 899 | `"    queries = existing_queries if isinstance(existing_queries, list) else []"` | — |
| [SRC-686F71AA50-L000900](../../agents/task_understanding.py#L900) | 900 | `"    rows: list[dict[str, str]] = []"` | — |
| [SRC-686F71AA50-L000901](../../agents/task_understanding.py#L901) | 901 | `"    seen: set[str] = set()"` | — |
| [SRC-686F71AA50-L000902](../../agents/task_understanding.py#L902) | 902 | `""` | — |
| [SRC-686F71AA50-L000903](../../agents/task_understanding.py#L903) | 903 | `"    def add(query: Any, strategy: str, rationale: str, *, enforce_topic: bool = True) -> None:"` | — |
| [SRC-686F71AA50-L000904](../../agents/task_understanding.py#L904) | 904 | `"        if not isinstance(query, str) or not query.strip() or len(rows) >= maximum:"` | — |
| [SRC-686F71AA50-L000905](../../agents/task_understanding.py#L905) | 905 | `"            return"` | — |
| [SRC-686F71AA50-L000906](../../agents/task_understanding.py#L906) | 906 | `"        candidate = query.strip()"` | — |
| [SRC-686F71AA50-L000907](../../agents/task_understanding.py#L907) | 907 | `"        if compact_fn is not None:"` | — |
| [SRC-686F71AA50-L000908](../../agents/task_understanding.py#L908) | 908 | `"            try:"` | — |
| [SRC-686F71AA50-L000909](../../agents/task_understanding.py#L909) | 909 | `"                candidate = compact_fn(candidate) or \"\""` | — |
| [SRC-686F71AA50-L000910](../../agents/task_understanding.py#L910) | 910 | `"            except (TypeError, ValueError):"` | — |
| [SRC-686F71AA50-L000911](../../agents/task_understanding.py#L911) | 911 | `"                candidate = \"\""` | — |
| [SRC-686F71AA50-L000912](../../agents/task_understanding.py#L912) | 912 | `"        candidate = _SPACE.sub(\" \", candidate).strip()[:240]"` | — |
| [SRC-686F71AA50-L000913](../../agents/task_understanding.py#L913) | 913 | `"        key = _query_key(candidate)"` | — |
| [SRC-686F71AA50-L000914](../../agents/task_understanding.py#L914) | 914 | `"        if not candidate or not key or key in seen:"` | — |
| [SRC-686F71AA50-L000915](../../agents/task_understanding.py#L915) | 915 | `"            return"` | — |
| [SRC-686F71AA50-L000916](../../agents/task_understanding.py#L916) | 916 | `"        # Search modifications must preserve a subject anchor. Existing planner"` | — |
| [SRC-686F71AA50-L000917](../../agents/task_understanding.py#L917) | 917 | `"        # queries are retained because they may already contain resolved context."` | — |
| [SRC-686F71AA50-L000918](../../agents/task_understanding.py#L918) | 918 | `"        anchor_query = str(queries[0]).strip() if queries and isinstance(queries[0], str) else str(question or \"\")"` | — |
| [SRC-686F71AA50-L000919](../../agents/task_understanding.py#L919) | 919 | `"        topic_tokens = _TOKEN_RE.findall(_query_key(anchor_query))"` | — |
| [SRC-686F71AA50-L000920](../../agents/task_understanding.py#L920) | 920 | `"        query_tokens = _TOKEN_RE.findall(key)"` | — |
| [SRC-686F71AA50-L000921](../../agents/task_understanding.py#L921) | 921 | `"        if enforce_topic and len(topic_tokens) >= 2 and not any("` | — |
| [SRC-686F71AA50-L000922](../../agents/task_understanding.py#L922) | 922 | `"            token in query_tokens for token in topic_tokens[:3]"` | — |
| [SRC-686F71AA50-L000923](../../agents/task_understanding.py#L923) | 923 | `"        ):"` | — |
| [SRC-686F71AA50-L000924](../../agents/task_understanding.py#L924) | 924 | `"            return"` | — |
| [SRC-686F71AA50-L000925](../../agents/task_understanding.py#L925) | 925 | `"        seen.add(key)"` | — |
| [SRC-686F71AA50-L000926](../../agents/task_understanding.py#L926) | 926 | `"        rows.append({\"query\": candidate, \"strategy\": strategy, \"rationale\": rationale})"` | — |
| [SRC-686F71AA50-L000927](../../agents/task_understanding.py#L927) | 927 | `""` | — |
| [SRC-686F71AA50-L000928](../../agents/task_understanding.py#L928) | 928 | `"    constraints = spec.get(\"constraints\") if isinstance(spec.get(\"constraints\"), dict) else {}"` | — |
| [SRC-686F71AA50-L000929](../../agents/task_understanding.py#L929) | 929 | `"    explicit_aspects = ("` | — |
| [SRC-686F71AA50-L000930](../../agents/task_understanding.py#L930) | 930 | `"        constraints.get(\"explicit_aspects\")"` | — |
| [SRC-686F71AA50-L000931](../../agents/task_understanding.py#L931) | 931 | `"        if isinstance(constraints.get(\"explicit_aspects\"), list)"` | — |
| [SRC-686F71AA50-L000932](../../agents/task_understanding.py#L932) | 932 | `"        else []"` | — |
| [SRC-686F71AA50-L000933](../../agents/task_understanding.py#L933) | 933 | `"    )"` | — |
| [SRC-686F71AA50-L000934](../../agents/task_understanding.py#L934) | 934 | `"    # Use the dedicated aspect extractor as a second deterministic pass. This"` | — |
| [SRC-686F71AA50-L000935](../../agents/task_understanding.py#L935) | 935 | `"    # guards against a classifier losing the final criterion in a long list."` | — |
| [SRC-686F71AA50-L000936](../../agents/task_understanding.py#L936) | 936 | `"    try:"` | — |
| [SRC-686F71AA50-L000937](../../agents/task_understanding.py#L937) | 937 | `"        from agents.aspect_planning import extract_aspects"` | — |
| [SRC-686F71AA50-L000938](../../agents/task_understanding.py#L938) | 938 | `"        independently_extracted = extract_aspects(question)"` | — |
| [SRC-686F71AA50-L000939](../../agents/task_understanding.py#L939) | 939 | `"    except (ImportError, TypeError, ValueError):"` | — |
| [SRC-686F71AA50-L000940](../../agents/task_understanding.py#L940) | 940 | `"        independently_extracted = []"` | — |
| [SRC-686F71AA50-L000941](../../agents/task_understanding.py#L941) | 941 | `"    merged_aspects: list[str] = []"` | — |
| [SRC-686F71AA50-L000942](../../agents/task_understanding.py#L942) | 942 | `"    aspect_keys: set[str] = set()"` | — |
| [SRC-686F71AA50-L000943](../../agents/task_understanding.py#L943) | 943 | `"    for aspect in [*explicit_aspects, *independently_extracted]:"` | — |
| [SRC-686F71AA50-L000944](../../agents/task_understanding.py#L944) | 944 | `"        if not isinstance(aspect, str) or not aspect.strip():"` | — |
| [SRC-686F71AA50-L000945](../../agents/task_understanding.py#L945) | 945 | `"            continue"` | — |
| [SRC-686F71AA50-L000946](../../agents/task_understanding.py#L946) | 946 | `"        key = _query_key(aspect)"` | — |
| [SRC-686F71AA50-L000947](../../agents/task_understanding.py#L947) | 947 | `"        if key and key not in aspect_keys:"` | — |
| [SRC-686F71AA50-L000948](../../agents/task_understanding.py#L948) | 948 | `"            aspect_keys.add(key)"` | — |
| [SRC-686F71AA50-L000949](../../agents/task_understanding.py#L949) | 949 | `"            merged_aspects.append(aspect.strip())"` | — |
| [SRC-686F71AA50-L000950](../../agents/task_understanding.py#L950) | 950 | `"        if len(merged_aspects) >= MAX_TASK_ASPECTS:"` | — |
| [SRC-686F71AA50-L000951](../../agents/task_understanding.py#L951) | 951 | `"            break"` | — |
| [SRC-686F71AA50-L000952](../../agents/task_understanding.py#L952) | 952 | `"    explicit_aspects = merged_aspects"` | — |
| [SRC-686F71AA50-L000953](../../agents/task_understanding.py#L953) | 953 | `"    spec_for_candidates = dict(spec)"` | — |
| [SRC-686F71AA50-L000954](../../agents/task_understanding.py#L954) | 954 | `"    candidate_constraints = dict(constraints)"` | — |
| [SRC-686F71AA50-L000955](../../agents/task_understanding.py#L955) | 955 | `"    candidate_constraints[\"explicit_aspects\"] = explicit_aspects"` | — |
| [SRC-686F71AA50-L000956](../../agents/task_understanding.py#L956) | 956 | `"    spec_for_candidates[\"constraints\"] = candidate_constraints"` | — |
| [SRC-686F71AA50-L000957](../../agents/task_understanding.py#L957) | 957 | `"    # If every query slot is needed to represent explicit comparison criteria,"` | — |
| [SRC-686F71AA50-L000958](../../agents/task_understanding.py#L958) | 958 | `"    # spend the budget on those criteria rather than a generic planner seed."` | — |
| [SRC-686F71AA50-L000959](../../agents/task_understanding.py#L959) | 959 | `"    reserve_all_slots_for_criteria = ("` | — |
| [SRC-686F71AA50-L000960](../../agents/task_understanding.py#L960) | 960 | `"        spec.get(\"task_family\") == \"compare\""` | — |
| [SRC-686F71AA50-L000961](../../agents/task_understanding.py#L961) | 961 | `"        and len(explicit_aspects) >= maximum"` | — |
| [SRC-686F71AA50-L000962](../../agents/task_understanding.py#L962) | 962 | `"    )"` | — |
| [SRC-686F71AA50-L000963](../../agents/task_understanding.py#L963) | 963 | `"    if queries and not reserve_all_slots_for_criteria:"` | — |
| [SRC-686F71AA50-L000964](../../agents/task_understanding.py#L964) | 964 | `"        seed = queries[0]"` | — |
| [SRC-686F71AA50-L000965](../../agents/task_understanding.py#L965) | 965 | `"        strategy, rationale = ("` | — |
| [SRC-686F71AA50-L000966](../../agents/task_understanding.py#L966) | 966 | `"            _label_existing_query(seed, 0, spec)"` | — |
| [SRC-686F71AA50-L000967](../../agents/task_understanding.py#L967) | 967 | `"            if isinstance(seed, str)"` | — |
| [SRC-686F71AA50-L000968](../../agents/task_understanding.py#L968) | 968 | `"            else (\"malformed\", \"planner seed is not a string\")"` | — |
| [SRC-686F71AA50-L000969](../../agents/task_understanding.py#L969) | 969 | `"        )"` | — |
| [SRC-686F71AA50-L000970](../../agents/task_understanding.py#L970) | 970 | `"        add(seed, strategy, rationale, enforce_topic=False)"` | — |
| [SRC-686F71AA50-L000971](../../agents/task_understanding.py#L971) | 971 | `""` | — |
| [SRC-686F71AA50-L000972](../../agents/task_understanding.py#L972) | 972 | `"    if not rows and ("` | — |
| [SRC-686F71AA50-L000973](../../agents/task_understanding.py#L973) | 973 | `"        spec.get(\"ambiguity_status\") == \"needs_clarification\""` | — |
| [SRC-686F71AA50-L000974](../../agents/task_understanding.py#L974) | 974 | `"        or spec.get(\"task_family\") == \"ambiguous_or_incomplete\""` | — |
| [SRC-686F71AA50-L000975](../../agents/task_understanding.py#L975) | 975 | `"    ):"` | — |
| [SRC-686F71AA50-L000976](../../agents/task_understanding.py#L976) | 976 | `"        return rows"` | — |
| [SRC-686F71AA50-L000977](../../agents/task_understanding.py#L977) | 977 | `""` | — |
| [SRC-686F71AA50-L000978](../../agents/task_understanding.py#L978) | 978 | `"    base = str(queries[0]).strip() if queries and isinstance(queries[0], str) else \"\""` | — |
| [SRC-686F71AA50-L000979](../../agents/task_understanding.py#L979) | 979 | `"    if not base:"` | — |
| [SRC-686F71AA50-L000980](../../agents/task_understanding.py#L980) | 980 | `"        base = re.sub("` | — |
| [SRC-686F71AA50-L000981](../../agents/task_understanding.py#L981) | 981 | `"            r\"^(?:من فضلك\|لو سمحت\|ابحث لي\|ابحث\|دورلي\|دور\|اعثر على\|please\|search for\|find\|look up)\\s*\","` | — |
| [SRC-686F71AA50-L000982](../../agents/task_understanding.py#L982) | 982 | `"            \"\", str(question or \"\").strip(), flags=re.IGNORECASE,"` | — |
| [SRC-686F71AA50-L000983](../../agents/task_understanding.py#L983) | 983 | `"        )"` | — |
| [SRC-686F71AA50-L000984](../../agents/task_understanding.py#L984) | 984 | `"    base = _QUERY_STOP.sub(\"\", base).strip(\" \\t\\r\\n-،,؛;\")"` | — |
| [SRC-686F71AA50-L000985](../../agents/task_understanding.py#L985) | 985 | `"    if not base:"` | — |
| [SRC-686F71AA50-L000986](../../agents/task_understanding.py#L986) | 986 | `"        return rows"` | — |
| [SRC-686F71AA50-L000987](../../agents/task_understanding.py#L987) | 987 | `""` | — |
| [SRC-686F71AA50-L000988](../../agents/task_understanding.py#L988) | 988 | `"    candidates = _generated_strategy_candidates(base, spec_for_candidates)"` | — |
| [SRC-686F71AA50-L000989](../../agents/task_understanding.py#L989) | 989 | `"    preserve_planner_alternatives_early = ("` | — |
| [SRC-686F71AA50-L000990](../../agents/task_understanding.py#L990) | 990 | `"        spec.get(\"task_family\") == \"find_or_discover\""` | — |
| [SRC-686F71AA50-L000991](../../agents/task_understanding.py#L991) | 991 | `"        and bool(constraints.get(\"explicit_budgets\"))"` | — |
| [SRC-686F71AA50-L000992](../../agents/task_understanding.py#L992) | 992 | `"        and not constraints.get(\"social_evidence_requested\")"` | — |
| [SRC-686F71AA50-L000993](../../agents/task_understanding.py#L993) | 993 | `"        and not constraints.get(\"time_sensitive_request\")"` | — |
| [SRC-686F71AA50-L000994](../../agents/task_understanding.py#L994) | 994 | `"        and not constraints.get(\"official_destination_required\")"` | — |
| [SRC-686F71AA50-L000995](../../agents/task_understanding.py#L995) | 995 | `"    )"` | — |
| [SRC-686F71AA50-L000996](../../agents/task_understanding.py#L996) | 996 | `"    if preserve_planner_alternatives_early:"` | — |
| [SRC-686F71AA50-L000997](../../agents/task_understanding.py#L997) | 997 | `"        for index, query in enumerate(queries[1:], start=1):"` | — |
| [SRC-686F71AA50-L000998](../../agents/task_understanding.py#L998) | 998 | `"            if len(rows) >= maximum:"` | — |
| [SRC-686F71AA50-L000999](../../agents/task_understanding.py#L999) | 999 | `"                break"` | — |
| [SRC-686F71AA50-L001000](../../agents/task_understanding.py#L1000) | 1000 | `"            if isinstance(query, str):"` | — |
| [SRC-686F71AA50-L001001](../../agents/task_understanding.py#L1001) | 1001 | `"                strategy, rationale = _label_existing_query(query, index, spec)"` | — |
| [SRC-686F71AA50-L001002](../../agents/task_understanding.py#L1002) | 1002 | `"                add(query, strategy, rationale, enforce_topic=False)"` | — |
| [SRC-686F71AA50-L001003](../../agents/task_understanding.py#L1003) | 1003 | `""` | — |
| [SRC-686F71AA50-L001004](../../agents/task_understanding.py#L1004) | 1004 | `"    for query, strategy, rationale in candidates:"` | — |
| [SRC-686F71AA50-L001005](../../agents/task_understanding.py#L1005) | 1005 | `"        add(query, strategy, rationale)"` | — |
| [SRC-686F71AA50-L001006](../../agents/task_understanding.py#L1006) | 1006 | `"        if len(rows) >= maximum:"` | — |
| [SRC-686F71AA50-L001007](../../agents/task_understanding.py#L1007) | 1007 | `"            break"` | — |
| [SRC-686F71AA50-L001008](../../agents/task_understanding.py#L1008) | 1008 | `""` | — |
| [SRC-686F71AA50-L001009](../../agents/task_understanding.py#L1009) | 1009 | `"    # Preserve other planner alternatives only after task-targeted candidates."` | — |
| [SRC-686F71AA50-L001010](../../agents/task_understanding.py#L1010) | 1010 | `"    for index, query in enumerate(queries[1:], start=1):"` | — |
| [SRC-686F71AA50-L001011](../../agents/task_understanding.py#L1011) | 1011 | `"        if len(rows) >= maximum:"` | — |
| [SRC-686F71AA50-L001012](../../agents/task_understanding.py#L1012) | 1012 | `"            break"` | — |
| [SRC-686F71AA50-L001013](../../agents/task_understanding.py#L1013) | 1013 | `"        if isinstance(query, str):"` | — |
| [SRC-686F71AA50-L001014](../../agents/task_understanding.py#L1014) | 1014 | `"            strategy, rationale = _label_existing_query(query, index, spec)"` | — |
| [SRC-686F71AA50-L001015](../../agents/task_understanding.py#L1015) | 1015 | `"        else:"` | — |
| [SRC-686F71AA50-L001016](../../agents/task_understanding.py#L1016) | 1016 | `"            strategy, rationale = \"malformed\", \"planner alternative is not a string\""` | — |
| [SRC-686F71AA50-L001017](../../agents/task_understanding.py#L1017) | 1017 | `"        add(query, strategy, rationale, enforce_topic=False)"` | — |
| [SRC-686F71AA50-L001018](../../agents/task_understanding.py#L1018) | 1018 | `"    return rows"` | — |
| [SRC-686F71AA50-L001019](../../agents/task_understanding.py#L1019) | 1019 | `""` | — |
| [SRC-686F71AA50-L001020](../../agents/task_understanding.py#L1020) | 1020 | `"def validate_task_spec(value: Any) -> dict[str, Any]:"` | — |
| [SRC-686F71AA50-L001021](../../agents/task_understanding.py#L1021) | 1021 | `"    \"\"\"Return a safe bounded public representation of TaskSpec-like input.\"\"\""` | — |
| [SRC-686F71AA50-L001022](../../agents/task_understanding.py#L1022) | 1022 | `"    if not isinstance(value, dict) or value.get(\"schema\") != \"omarai.task_spec.v1\":"` | — |
| [SRC-686F71AA50-L001023](../../agents/task_understanding.py#L1023) | 1023 | `"        return {"` | — |
| [SRC-686F71AA50-L001024](../../agents/task_understanding.py#L1024) | 1024 | `"            \"schema\": \"omarai.task_spec.v1\","` | — |
| [SRC-686F71AA50-L001025](../../agents/task_understanding.py#L1025) | 1025 | `"            \"status\": \"not_available\","` | — |
| [SRC-686F71AA50-L001026](../../agents/task_understanding.py#L1026) | 1026 | `"            \"claim\": \"no validated task specification supplied\","` | — |
| [SRC-686F71AA50-L001027](../../agents/task_understanding.py#L1027) | 1027 | `"        }"` | — |
| [SRC-686F71AA50-L001028](../../agents/task_understanding.py#L1028) | 1028 | `"    # Rebuild via the allowlisted JSON-friendly fields rather than passing arbitrary"` | — |
| [SRC-686F71AA50-L001029](../../agents/task_understanding.py#L1029) | 1029 | `"    # planner/model content through the diagnostics surface."` | — |
| [SRC-686F71AA50-L001030](../../agents/task_understanding.py#L1030) | 1030 | `"    spec = {"` | — |
| [SRC-686F71AA50-L001031](../../agents/task_understanding.py#L1031) | 1031 | `"        \"schema\": \"omarai.task_spec.v1\","` | — |
| [SRC-686F71AA50-L001032](../../agents/task_understanding.py#L1032) | 1032 | `"        \"task_family\": str(value.get(\"task_family\") or \"general_question\")[:80],"` | — |
| [SRC-686F71AA50-L001033](../../agents/task_understanding.py#L1033) | 1033 | `"        \"mode\": str(value.get(\"mode\") or \"auto\")[:20],"` | — |
| [SRC-686F71AA50-L001034](../../agents/task_understanding.py#L1034) | 1034 | `"        \"intent_route\": str(value.get(\"intent_route\") or \"unassessed\")[:40],"` | — |
| [SRC-686F71AA50-L001035](../../agents/task_understanding.py#L1035) | 1035 | `"        \"classification_method\": str(value.get(\"classification_method\") or \"\")[:100],"` | — |
| [SRC-686F71AA50-L001036](../../agents/task_understanding.py#L1036) | 1036 | `"        \"classification_is_probability\": False,"` | — |
| [SRC-686F71AA50-L001037](../../agents/task_understanding.py#L1037) | 1037 | `"        \"ambiguity_status\": str(value.get(\"ambiguity_status\") or \"unassessed\")[:80],"` | — |
| [SRC-686F71AA50-L001038](../../agents/task_understanding.py#L1038) | 1038 | `"        \"missing_required_inputs\": value.get(\"missing_required_inputs\") if isinstance(value.get(\"missing_required_inputs\"), list) else [],"` | — |
| [SRC-686F71AA50-L001039](../../agents/task_understanding.py#L1039) | 1039 | `"        \"requires_clarification\": value.get(\"requires_clarification\") is True,"` | — |
| [SRC-686F71AA50-L001040](../../agents/task_understanding.py#L1040) | 1040 | `"        \"clarification_reason\": str(value.get(\"clarification_reason\") or \"unassessed\")[:80],"` | — |
| [SRC-686F71AA50-L001041](../../agents/task_understanding.py#L1041) | 1041 | `"        \"constraints\": value.get(\"constraints\") if isinstance(value.get(\"constraints\"), dict) else {},"` | — |
| [SRC-686F71AA50-L001042](../../agents/task_understanding.py#L1042) | 1042 | `"        \"output_preferences\": value.get(\"output_preferences\") if isinstance(value.get(\"output_preferences\"), dict) else {},"` | — |
| [SRC-686F71AA50-L001043](../../agents/task_understanding.py#L1043) | 1043 | `"        \"evidence_requirements\": value.get(\"evidence_requirements\") if isinstance(value.get(\"evidence_requirements\"), list) else [],"` | — |
| [SRC-686F71AA50-L001044](../../agents/task_understanding.py#L1044) | 1044 | `"        \"query_strategies\": value.get(\"query_strategies\") if isinstance(value.get(\"query_strategies\"), list) else [],"` | — |
| [SRC-686F71AA50-L001045](../../agents/task_understanding.py#L1045) | 1045 | `"        \"tool_requirements\": value.get(\"tool_requirements\") if isinstance(value.get(\"tool_requirements\"), list) else [],"` | — |
| [SRC-686F71AA50-L001046](../../agents/task_understanding.py#L1046) | 1046 | `"        \"decision_checks\": value.get(\"decision_checks\") if isinstance(value.get(\"decision_checks\"), list) else [],"` | — |
| [SRC-686F71AA50-L001047](../../agents/task_understanding.py#L1047) | 1047 | `"        \"hypothesis_interpretations\": value.get(\"hypothesis_interpretations\") if isinstance(value.get(\"hypothesis_interpretations\"), list) else [],"` | — |
| [SRC-686F71AA50-L001048](../../agents/task_understanding.py#L1048) | 1048 | `"        \"claim\": \"task planning metadata only; not semantic certainty or factual verification\","` | — |
| [SRC-686F71AA50-L001049](../../agents/task_understanding.py#L1049) | 1049 | `"    }"` | — |
| [SRC-686F71AA50-L001050](../../agents/task_understanding.py#L1050) | 1050 | `"    return spec"` | — |
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
| [SRC-1AE03B9EC3-L000051](../../agents/web_agent.py#L51) | 51 | `"from agents.task_understanding import build_query_strategy_matrix, build_task_spec"` | — |
| [SRC-1AE03B9EC3-L000052](../../agents/web_agent.py#L52) | 52 | `""` | — |
| [SRC-1AE03B9EC3-L000053](../../agents/web_agent.py#L53) | 53 | `"MAX_QUESTION_CHARS = 4000"` | — |
| [SRC-1AE03B9EC3-L000054](../../agents/web_agent.py#L54) | 54 | `"MAX_HISTORY_ITEMS = 8"` | — |
| [SRC-1AE03B9EC3-L000055](../../agents/web_agent.py#L55) | 55 | `"MAX_HISTORY_CHARS = 4000"` | — |
| [SRC-1AE03B9EC3-L000056](../../agents/web_agent.py#L56) | 56 | `"MAX_SEARCH_RESULTS = 18"` | — |
| [SRC-1AE03B9EC3-L000057](../../agents/web_agent.py#L57) | 57 | `"MAX_PROVIDER_RESULTS = 6"` | — |
| [SRC-1AE03B9EC3-L000058](../../agents/web_agent.py#L58) | 58 | `"MAX_FETCHED_PAGES = 8"` | — |
| [SRC-1AE03B9EC3-L000059](../../agents/web_agent.py#L59) | 59 | `"MAX_LLM_CITED_SOURCES = 12"` | — |
| [SRC-1AE03B9EC3-L000060](../../agents/web_agent.py#L60) | 60 | `"MAX_RESEARCH_WORKERS = 8"` | — |
| [SRC-1AE03B9EC3-L000061](../../agents/web_agent.py#L61) | 61 | `"MAX_PAGE_BYTES = 1_000_000"` | — |
| [SRC-1AE03B9EC3-L000062](../../agents/web_agent.py#L62) | 62 | `"MAX_PAGE_TEXT_CHARS = 12_000"` | — |
| [SRC-1AE03B9EC3-L000063](../../agents/web_agent.py#L63) | 63 | `"LLM_TIMEOUT_SECONDS = 35"` | — |
| [SRC-1AE03B9EC3-L000064](../../agents/web_agent.py#L64) | 64 | `""` | — |
| [SRC-1AE03B9EC3-L000065](../../agents/web_agent.py#L65) | 65 | `"# Only completed connector result-processing states positively confirm an attempt."` | — |
| [SRC-1AE03B9EC3-L000066](../../agents/web_agent.py#L66) | 66 | `"# A generic \"failed\" or timeout diagnostic may occur before a network request is sent."` | — |
| [SRC-1AE03B9EC3-L000067](../../agents/web_agent.py#L67) | 67 | `"_SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES = frozenset({\"ok\", \"no_results\", \"filtered_all\"})"` | — |
| [SRC-1AE03B9EC3-L000068](../../agents/web_agent.py#L68) | 68 | `"_RESEARCH_ERROR_OUTCOMES = frozenset({\"attempted_research_error\", \"unknown_after_research_error\"})"` | — |
| [SRC-1AE03B9EC3-L000069](../../agents/web_agent.py#L69) | 69 | `"_PROVIDER_REJECTION_REASONS = ("` | — |
| [SRC-1AE03B9EC3-L000070](../../agents/web_agent.py#L70) | 70 | `"    \"malformed_candidate\","` | — |
| [SRC-1AE03B9EC3-L000071](../../agents/web_agent.py#L71) | 71 | `"    \"invalid_url_or_unsafe_target\","` | — |
| [SRC-1AE03B9EC3-L000072](../../agents/web_agent.py#L72) | 72 | `"    \"blocked_domain\","` | — |
| [SRC-1AE03B9EC3-L000073](../../agents/web_agent.py#L73) | 73 | `"    \"relevance_below_threshold\","` | — |
