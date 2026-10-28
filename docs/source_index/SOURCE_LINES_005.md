# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **005**
- سجلات الأسطر: **800**
- النطاق: SRC-59CF4B7DE8-L000533 إلى SRC-6E58A660BC-L000124
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-59CF4B7DE8 — [agents/research.py](../../agents/research.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-59CF4B7DE8-L000533](../../agents/research.py#L533) | 533 | `""` | — |
| [SRC-59CF4B7DE8-L000534](../../agents/research.py#L534) | 534 | `"def evidence_signal_report("` | — |
| [SRC-59CF4B7DE8-L000535](../../agents/research.py#L535) | 535 | `"    sources: list[dict[str, Any]],"` | — |
| [SRC-59CF4B7DE8-L000536](../../agents/research.py#L536) | 536 | `"    freshness: str = \"any\","` | — |
| [SRC-59CF4B7DE8-L000537](../../agents/research.py#L537) | 537 | `"    now: datetime \| None = None,"` | — |
| [SRC-59CF4B7DE8-L000538](../../agents/research.py#L538) | 538 | `") -> dict[str, Any]:"` | — |
| [SRC-59CF4B7DE8-L000539](../../agents/research.py#L539) | 539 | `"    \"\"\"Summarize research coverage; signals describe evidence coverage, not factual truth.\"\"\""` | — |
| [SRC-59CF4B7DE8-L000540](../../agents/research.py#L540) | 540 | `"    current = now or datetime.now(UTC)"` | — |
| [SRC-59CF4B7DE8-L000541](../../agents/research.py#L541) | 541 | `"    valid_sources = [source for source in sources if isinstance(source, dict) and source.get(\"url\")]"` | — |
| [SRC-59CF4B7DE8-L000542](../../agents/research.py#L542) | 542 | `"    domains = {"` | — |
| [SRC-59CF4B7DE8-L000543](../../agents/research.py#L543) | 543 | `"        registrable_domain("` | — |
| [SRC-59CF4B7DE8-L000544](../../agents/research.py#L544) | 544 | `"            source.get(\"domain\") or urlparse(str(source.get(\"url\") or \"\")).hostname or \"\""` | — |
| [SRC-59CF4B7DE8-L000545](../../agents/research.py#L545) | 545 | `"        )"` | — |
| [SRC-59CF4B7DE8-L000546](../../agents/research.py#L546) | 546 | `"        for source in valid_sources"` | — |
| [SRC-59CF4B7DE8-L000547](../../agents/research.py#L547) | 547 | `"        if source.get(\"domain\") or source.get(\"url\")"` | — |
| [SRC-59CF4B7DE8-L000548](../../agents/research.py#L548) | 548 | `"    }"` | — |
| [SRC-59CF4B7DE8-L000549](../../agents/research.py#L549) | 549 | `"    domains.discard(\"\")"` | — |
| [SRC-59CF4B7DE8-L000550](../../agents/research.py#L550) | 550 | `"    providers: set[str] = set()"` | — |
| [SRC-59CF4B7DE8-L000551](../../agents/research.py#L551) | 551 | `"    for source in valid_sources:"` | — |
| [SRC-59CF4B7DE8-L000552](../../agents/research.py#L552) | 552 | `"        candidate_providers = source.get(\"providers\", [])"` | — |
| [SRC-59CF4B7DE8-L000553](../../agents/research.py#L553) | 553 | `"        if isinstance(candidate_providers, list):"` | — |
| [SRC-59CF4B7DE8-L000554](../../agents/research.py#L554) | 554 | `"            providers.update(str(item) for item in candidate_providers if item)"` | — |
| [SRC-59CF4B7DE8-L000555](../../agents/research.py#L555) | 555 | `"        elif source.get(\"provider\"):"` | — |
| [SRC-59CF4B7DE8-L000556](../../agents/research.py#L556) | 556 | `"            providers.add(str(source[\"provider\"]))"` | — |
| [SRC-59CF4B7DE8-L000557](../../agents/research.py#L557) | 557 | `"    classes = [str(source.get(\"source_class\") or \"general\") for source in valid_sources]"` | — |
| [SRC-59CF4B7DE8-L000558](../../agents/research.py#L558) | 558 | `"    primary_count = sum(item in {\"government\", \"academic\", \"official\"} for item in classes)"` | — |
| [SRC-59CF4B7DE8-L000559](../../agents/research.py#L559) | 559 | `"    news_count = sum(item == \"news\" for item in classes)"` | — |
| [SRC-59CF4B7DE8-L000560](../../agents/research.py#L560) | 560 | `"    social_count = sum(item == \"social\" for item in classes)"` | — |
| [SRC-59CF4B7DE8-L000561](../../agents/research.py#L561) | 561 | `"    pages_read = sum(bool(source.get(\"page_fetched\")) for source in valid_sources)"` | — |
| [SRC-59CF4B7DE8-L000562](../../agents/research.py#L562) | 562 | `"    dates = ["` | — |
| [SRC-59CF4B7DE8-L000563](../../agents/research.py#L563) | 563 | `"        parsed"` | — |
| [SRC-59CF4B7DE8-L000564](../../agents/research.py#L564) | 564 | `"        for source in valid_sources"` | — |
| [SRC-59CF4B7DE8-L000565](../../agents/research.py#L565) | 565 | `"        if (parsed := _parse_publication_date(source.get(\"published_at\"), current)) is not None"` | — |
| [SRC-59CF4B7DE8-L000566](../../agents/research.py#L566) | 566 | `"    ]"` | — |
| [SRC-59CF4B7DE8-L000567](../../agents/research.py#L567) | 567 | `"    recent_days = 7 if freshness == \"current\" else 30"` | — |
| [SRC-59CF4B7DE8-L000568](../../agents/research.py#L568) | 568 | `"    recent_count = sum((current - parsed).total_seconds() >= 0 and"` | — |
| [SRC-59CF4B7DE8-L000569](../../agents/research.py#L569) | 569 | `"                       (current - parsed) <= timedelta(days=recent_days) for parsed in dates)"` | — |
| [SRC-59CF4B7DE8-L000570](../../agents/research.py#L570) | 570 | `"    future_dates = sum(parsed > current + timedelta(days=1) for parsed in dates)"` | — |
| [SRC-59CF4B7DE8-L000571](../../agents/research.py#L571) | 571 | `"    unique_sources = len(valid_sources)"` | — |
| [SRC-59CF4B7DE8-L000572](../../agents/research.py#L572) | 572 | `"    # Evidence coverage uses several independent dimensions and is deliberately not a"` | — |
| [SRC-59CF4B7DE8-L000573](../../agents/research.py#L573) | 573 | `"    # probability that any factual claim is true."` | — |
| [SRC-59CF4B7DE8-L000574](../../agents/research.py#L574) | 574 | `"    coverage_points = 0"` | — |
| [SRC-59CF4B7DE8-L000575](../../agents/research.py#L575) | 575 | `"    coverage_points += min(unique_sources, 10) * 3"` | — |
| [SRC-59CF4B7DE8-L000576](../../agents/research.py#L576) | 576 | `"    coverage_points += min(len(domains), 8) * 4"` | — |
| [SRC-59CF4B7DE8-L000577](../../agents/research.py#L577) | 577 | `"    coverage_points += min(len(providers), 4) * 5"` | — |
| [SRC-59CF4B7DE8-L000578](../../agents/research.py#L578) | 578 | `"    coverage_points += min(pages_read, 8) * 3"` | — |
| [SRC-59CF4B7DE8-L000579](../../agents/research.py#L579) | 579 | `"    coverage_points += min(primary_count, 4) * 4"` | — |
| [SRC-59CF4B7DE8-L000580](../../agents/research.py#L580) | 580 | `"    coverage_points += min(len(dates), 8) * 2"` | — |
| [SRC-59CF4B7DE8-L000581](../../agents/research.py#L581) | 581 | `"    coverage_score = min(100, coverage_points)"` | — |
| [SRC-59CF4B7DE8-L000582](../../agents/research.py#L582) | 582 | `"    if unique_sources >= 8 and len(domains) >= 5 and len(providers) >= 2 and pages_read >= 3:"` | — |
| [SRC-59CF4B7DE8-L000583](../../agents/research.py#L583) | 583 | `"        coverage_level = \"متعدد المصادر\""` | — |
| [SRC-59CF4B7DE8-L000584](../../agents/research.py#L584) | 584 | `"    elif unique_sources >= 4 and len(domains) >= 3 and len(providers) >= 1:"` | — |
| [SRC-59CF4B7DE8-L000585](../../agents/research.py#L585) | 585 | `"        coverage_level = \"متوسط\""` | — |
| [SRC-59CF4B7DE8-L000586](../../agents/research.py#L586) | 586 | `"    else:"` | — |
| [SRC-59CF4B7DE8-L000587](../../agents/research.py#L587) | 587 | `"        coverage_level = \"محدود\""` | — |
| [SRC-59CF4B7DE8-L000588](../../agents/research.py#L588) | 588 | `""` | — |
| [SRC-59CF4B7DE8-L000589](../../agents/research.py#L589) | 589 | `"    warnings: list[str] = []"` | — |
| [SRC-59CF4B7DE8-L000590](../../agents/research.py#L590) | 590 | `"    if unique_sources == 0:"` | — |
| [SRC-59CF4B7DE8-L000591](../../agents/research.py#L591) | 591 | `"        warnings.append(\"لا توجد مصادر قابلة للاستشهاد؛ لا تستنتج حقائق من عدم وجود نتائج.\")"` | — |
| [SRC-59CF4B7DE8-L000592](../../agents/research.py#L592) | 592 | `"    if len(domains) < 3:"` | — |
| [SRC-59CF4B7DE8-L000593](../../agents/research.py#L593) | 593 | `"        warnings.append(\"تنوع النطاقات محدود؛ لا تعتبر تكرار النتيجة تأكيدًا مستقلًا.\")"` | — |
| [SRC-59CF4B7DE8-L000594](../../agents/research.py#L594) | 594 | `"    if pages_read < 2 and unique_sources:"` | — |
| [SRC-59CF4B7DE8-L000595](../../agents/research.py#L595) | 595 | `"        warnings.append(\"تمت قراءة أقل من صفحتين مباشرة؛ بعض الأدلة مقتطفات من محركات البحث فقط.\")"` | — |
| [SRC-59CF4B7DE8-L000596](../../agents/research.py#L596) | 596 | `"    if freshness == \"current\":"` | — |
| [SRC-59CF4B7DE8-L000597](../../agents/research.py#L597) | 597 | `"        if not dates:"` | — |
| [SRC-59CF4B7DE8-L000598](../../agents/research.py#L598) | 598 | `"            warnings.append(\"لا تتوفر تواريخ نشر قابلة للتحليل؛ حداثة النتائج غير مؤكدة.\")"` | — |
| [SRC-59CF4B7DE8-L000599](../../agents/research.py#L599) | 599 | `"        elif recent_count == 0:"` | — |
| [SRC-59CF4B7DE8-L000600](../../agents/research.py#L600) | 600 | `"            warnings.append(f\"لم يُعثر على مصدر مؤرخ خلال آخر {recent_days} يومًا ضمن التواريخ القابلة للتحليل.\")"` | — |
| [SRC-59CF4B7DE8-L000601](../../agents/research.py#L601) | 601 | `"    if future_dates:"` | — |
| [SRC-59CF4B7DE8-L000602](../../agents/research.py#L602) | 602 | `"        warnings.append(\"توجد تواريخ مستقبلية غير متوقعة؛ يجب مراجعتها يدويًا.\")"` | — |
| [SRC-59CF4B7DE8-L000603](../../agents/research.py#L603) | 603 | `"    if social_count and primary_count == 0:"` | — |
| [SRC-59CF4B7DE8-L000604](../../agents/research.py#L604) | 604 | `"        warnings.append(\"المصادر اجتماعية فقط دون مصدر رسمي/أكاديمي؛ تعامل معها كآراء أو إشارات لا كحقائق مثبتة.\")"` | — |
| [SRC-59CF4B7DE8-L000605](../../agents/research.py#L605) | 605 | `"    return {"` | — |
| [SRC-59CF4B7DE8-L000606](../../agents/research.py#L606) | 606 | `"        \"unique_sources\": unique_sources,"` | — |
| [SRC-59CF4B7DE8-L000607](../../agents/research.py#L607) | 607 | `"        \"unique_domains\": len(domains),"` | — |
| [SRC-59CF4B7DE8-L000608](../../agents/research.py#L608) | 608 | `"        \"providers_count\": len(providers),"` | — |
| [SRC-59CF4B7DE8-L000609](../../agents/research.py#L609) | 609 | `"        \"providers\": sorted(providers),"` | — |
| [SRC-59CF4B7DE8-L000610](../../agents/research.py#L610) | 610 | `"        \"pages_read\": pages_read,"` | — |
| [SRC-59CF4B7DE8-L000611](../../agents/research.py#L611) | 611 | `"        \"primary_sources\": primary_count,"` | — |
| [SRC-59CF4B7DE8-L000612](../../agents/research.py#L612) | 612 | `"        \"news_sources\": news_count,"` | — |
| [SRC-59CF4B7DE8-L000613](../../agents/research.py#L613) | 613 | `"        \"social_sources\": social_count,"` | — |
| [SRC-59CF4B7DE8-L000614](../../agents/research.py#L614) | 614 | `"        \"dated_sources\": len(dates),"` | — |
| [SRC-59CF4B7DE8-L000615](../../agents/research.py#L615) | 615 | `"        \"recent_sources\": recent_count,"` | — |
| [SRC-59CF4B7DE8-L000616](../../agents/research.py#L616) | 616 | `"        \"undated_sources\": max(0, unique_sources - len(dates)),"` | — |
| [SRC-59CF4B7DE8-L000617](../../agents/research.py#L617) | 617 | `"        \"date_coverage_percent\": round(100 * len(dates) / unique_sources) if unique_sources else 0,"` | — |
| [SRC-59CF4B7DE8-L000618](../../agents/research.py#L618) | 618 | `"        \"coverage_score\": coverage_score,"` | — |
| [SRC-59CF4B7DE8-L000619](../../agents/research.py#L619) | 619 | `"        \"coverage_level\": coverage_level,"` | — |
| [SRC-59CF4B7DE8-L000620](../../agents/research.py#L620) | 620 | `"        \"score_meaning\": \"مؤشر تغطية وتنوع الأدلة، وليس احتمال صحة الإجابة.\","` | — |
| [SRC-59CF4B7DE8-L000621](../../agents/research.py#L621) | 621 | `"        \"warnings\": warnings,"` | — |
| [SRC-59CF4B7DE8-L000622](../../agents/research.py#L622) | 622 | `"    }"` | — |
| [SRC-59CF4B7DE8-L000623](../../agents/research.py#L623) | 623 | `""` | — |
| [SRC-59CF4B7DE8-L000624](../../agents/research.py#L624) | 624 | `""` | — |
| [SRC-59CF4B7DE8-L000625](../../agents/research.py#L625) | 625 | `""` | — |
| [SRC-59CF4B7DE8-L000626](../../agents/research.py#L626) | 626 | `"# ---------------------------------------------------------------------------"` | — |
| [SRC-59CF4B7DE8-L000627](../../agents/research.py#L627) | 627 | `"# Evidence-aware helpers"` | — |
| [SRC-59CF4B7DE8-L000628](../../agents/research.py#L628) | 628 | `"# ---------------------------------------------------------------------------"` | — |
| [SRC-59CF4B7DE8-L000629](../../agents/research.py#L629) | 629 | `""` | — |
| [SRC-59CF4B7DE8-L000630](../../agents/research.py#L630) | 630 | `"_RELEVANCE_STOPWORDS = {"` | — |
| [SRC-59CF4B7DE8-L000631](../../agents/research.py#L631) | 631 | `"    \"the\", \"a\", \"an\", \"of\", \"in\", \"on\", \"at\", \"to\", \"for\","` | — |
| [SRC-59CF4B7DE8-L000632](../../agents/research.py#L632) | 632 | `"    \"is\", \"are\", \"was\", \"were\", \"be\", \"been\", \"being\","` | — |
| [SRC-59CF4B7DE8-L000633](../../agents/research.py#L633) | 633 | `"    \"and\", \"or\", \"but\", \"not\", \"with\", \"without\","` | — |
| [SRC-59CF4B7DE8-L000634](../../agents/research.py#L634) | 634 | `"    \"this\", \"that\", \"these\", \"those\", \"it\", \"its\","` | — |
| [SRC-59CF4B7DE8-L000635](../../agents/research.py#L635) | 635 | `"}"` | — |
| [SRC-59CF4B7DE8-L000636](../../agents/research.py#L636) | 636 | `""` | — |
| [SRC-59CF4B7DE8-L000637](../../agents/research.py#L637) | 637 | `"_OFFICIAL_CLASSES = {\"government\", \"education\", \"official\"}"` | — |
| [SRC-59CF4B7DE8-L000638](../../agents/research.py#L638) | 638 | `""` | — |
| [SRC-59CF4B7DE8-L000639](../../agents/research.py#L639) | 639 | `""` | — |
| [SRC-59CF4B7DE8-L000640](../../agents/research.py#L640) | 640 | `"def _tokenize(text: str) -> set:"` | — |
| [SRC-59CF4B7DE8-L000641](../../agents/research.py#L641) | 641 | `"    if not text:"` | — |
| [SRC-59CF4B7DE8-L000642](../../agents/research.py#L642) | 642 | `"        return set()"` | — |
| [SRC-59CF4B7DE8-L000643](../../agents/research.py#L643) | 643 | `"    norm = _normalize_arabic(text.casefold())"` | — |
| [SRC-59CF4B7DE8-L000644](../../agents/research.py#L644) | 644 | `"    tokens = re.findall(r\"\\w+\", norm, flags=re.UNICODE)"` | — |
| [SRC-59CF4B7DE8-L000645](../../agents/research.py#L645) | 645 | `"    return {t for t in tokens if len(t) >= 3 and t not in _RELEVANCE_STOPWORDS}"` | — |
| [SRC-59CF4B7DE8-L000646](../../agents/research.py#L646) | 646 | `""` | — |
| [SRC-59CF4B7DE8-L000647](../../agents/research.py#L647) | 647 | `""` | — |
| [SRC-59CF4B7DE8-L000648](../../agents/research.py#L648) | 648 | `"def source_relevance_score(src, query: str) -> dict:"` | — |
| [SRC-59CF4B7DE8-L000649](../../agents/research.py#L649) | 649 | `"    if not isinstance(src, dict):"` | — |
| [SRC-59CF4B7DE8-L000650](../../agents/research.py#L650) | 650 | `"        return {\"accepted\": False, \"score\": 0, \"reason\": \"malformed\"}"` | — |
| [SRC-59CF4B7DE8-L000651](../../agents/research.py#L651) | 651 | `""` | — |
| [SRC-59CF4B7DE8-L000652](../../agents/research.py#L652) | 652 | `"    title = str(src.get(\"title\") or \"\")"` | — |
| [SRC-59CF4B7DE8-L000653](../../agents/research.py#L653) | 653 | `"    snippet = str(src.get(\"snippet\") or \"\")"` | — |
| [SRC-59CF4B7DE8-L000654](../../agents/research.py#L654) | 654 | `"    page_text = str(src.get(\"page_text\") or \"\")"` | — |
| [SRC-59CF4B7DE8-L000655](../../agents/research.py#L655) | 655 | `"    source_class = str(src.get(\"source_class\") or \"general\").lower()"` | — |
| [SRC-59CF4B7DE8-L000656](../../agents/research.py#L656) | 656 | `""` | — |
| [SRC-59CF4B7DE8-L000657](../../agents/research.py#L657) | 657 | `"    q_tokens = _tokenize(query)"` | — |
| [SRC-59CF4B7DE8-L000658](../../agents/research.py#L658) | 658 | `"    if not q_tokens:"` | — |
| [SRC-59CF4B7DE8-L000659](../../agents/research.py#L659) | 659 | `"        return {\"accepted\": False, \"score\": 0, \"reason\": \"no_query_tokens\"}"` | — |
| [SRC-59CF4B7DE8-L000660](../../agents/research.py#L660) | 660 | `""` | — |
| [SRC-59CF4B7DE8-L000661](../../agents/research.py#L661) | 661 | `"    t_tokens = _tokenize(title)"` | — |
| [SRC-59CF4B7DE8-L000662](../../agents/research.py#L662) | 662 | `"    s_tokens = _tokenize(snippet)"` | — |
| [SRC-59CF4B7DE8-L000663](../../agents/research.py#L663) | 663 | `"    p_tokens = _tokenize(page_text[:3000])"` | — |
| [SRC-59CF4B7DE8-L000664](../../agents/research.py#L664) | 664 | `""` | — |
| [SRC-59CF4B7DE8-L000665](../../agents/research.py#L665) | 665 | `"    title_ratio = len(q_tokens & t_tokens) / max(len(q_tokens), 1)"` | — |
| [SRC-59CF4B7DE8-L000666](../../agents/research.py#L666) | 666 | `"    snippet_ratio = len(q_tokens & s_tokens) / max(len(q_tokens), 1)"` | — |
| [SRC-59CF4B7DE8-L000667](../../agents/research.py#L667) | 667 | `"    page_ratio = len(q_tokens & p_tokens) / max(len(q_tokens), 1)"` | — |
| [SRC-59CF4B7DE8-L000668](../../agents/research.py#L668) | 668 | `""` | — |
| [SRC-59CF4B7DE8-L000669](../../agents/research.py#L669) | 669 | `"    score = int(title_ratio * 15 + snippet_ratio * 20 + page_ratio * 5)"` | — |
| [SRC-59CF4B7DE8-L000670](../../agents/research.py#L670) | 670 | `""` | — |
| [SRC-59CF4B7DE8-L000671](../../agents/research.py#L671) | 671 | `"    if source_class in _OFFICIAL_CLASSES:"` | — |
| [SRC-59CF4B7DE8-L000672](../../agents/research.py#L672) | 672 | `"        if score >= 5:"` | — |
| [SRC-59CF4B7DE8-L000673](../../agents/research.py#L673) | 673 | `"            return {\"accepted\": True, \"score\": score, \"reason\": \"accepted\"}"` | — |
| [SRC-59CF4B7DE8-L000674](../../agents/research.py#L674) | 674 | `"        return {\"accepted\": True, \"score\": score,"` | — |
| [SRC-59CF4B7DE8-L000675](../../agents/research.py#L675) | 675 | `"                \"reason\": \"kept_official_despite_low_overlap\"}"` | — |
| [SRC-59CF4B7DE8-L000676](../../agents/research.py#L676) | 676 | `""` | — |
| [SRC-59CF4B7DE8-L000677](../../agents/research.py#L677) | 677 | `"    if score >= 18:"` | — |
| [SRC-59CF4B7DE8-L000678](../../agents/research.py#L678) | 678 | `"        return {\"accepted\": True, \"score\": score, \"reason\": \"accepted\"}"` | — |
| [SRC-59CF4B7DE8-L000679](../../agents/research.py#L679) | 679 | `"    return {\"accepted\": False, \"score\": score, \"reason\": \"low_overlap\"}"` | — |
| [SRC-59CF4B7DE8-L000680](../../agents/research.py#L680) | 680 | `""` | — |
| [SRC-59CF4B7DE8-L000681](../../agents/research.py#L681) | 681 | `""` | — |
| [SRC-59CF4B7DE8-L000682](../../agents/research.py#L682) | 682 | `"def filter_relevant_sources(sources, query: str, extra_queries=None):"` | — |
| [SRC-59CF4B7DE8-L000683](../../agents/research.py#L683) | 683 | `"    kept = []"` | — |
| [SRC-59CF4B7DE8-L000684](../../agents/research.py#L684) | 684 | `"    diag = []"` | — |
| [SRC-59CF4B7DE8-L000685](../../agents/research.py#L685) | 685 | `"    seen_urls = set()"` | — |
| [SRC-59CF4B7DE8-L000686](../../agents/research.py#L686) | 686 | `"    seen_titles = set()"` | — |
| [SRC-59CF4B7DE8-L000687](../../agents/research.py#L687) | 687 | `"    combined = \" \".join([query] + list(extra_queries or []))"` | — |
| [SRC-59CF4B7DE8-L000688](../../agents/research.py#L688) | 688 | `""` | — |
| [SRC-59CF4B7DE8-L000689](../../agents/research.py#L689) | 689 | `"    for src in sources or []:"` | — |
| [SRC-59CF4B7DE8-L000690](../../agents/research.py#L690) | 690 | `"        if not isinstance(src, dict):"` | — |
| [SRC-59CF4B7DE8-L000691](../../agents/research.py#L691) | 691 | `"            diag.append({\"reason\": \"malformed\", \"url\": \"\"})"` | — |
| [SRC-59CF4B7DE8-L000692](../../agents/research.py#L692) | 692 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000693](../../agents/research.py#L693) | 693 | `"        url = str(src.get(\"url\") or \"\")"` | — |
| [SRC-59CF4B7DE8-L000694](../../agents/research.py#L694) | 694 | `"        domain = str(src.get(\"domain\") or \"\").lower()"` | — |
| [SRC-59CF4B7DE8-L000695](../../agents/research.py#L695) | 695 | `"        title = str(src.get(\"title\") or \"\").strip()"` | — |
| [SRC-59CF4B7DE8-L000696](../../agents/research.py#L696) | 696 | `"        url_key = url.rstrip(\"/\").lower()"` | — |
| [SRC-59CF4B7DE8-L000697](../../agents/research.py#L697) | 697 | `"        title_key = title.lower() + \"\|\" + domain"` | — |
| [SRC-59CF4B7DE8-L000698](../../agents/research.py#L698) | 698 | `""` | — |
| [SRC-59CF4B7DE8-L000699](../../agents/research.py#L699) | 699 | `"        if url_key and url_key in seen_urls:"` | — |
| [SRC-59CF4B7DE8-L000700](../../agents/research.py#L700) | 700 | `"            diag.append({\"reason\": \"duplicate_url\", \"url\": url})"` | — |
| [SRC-59CF4B7DE8-L000701](../../agents/research.py#L701) | 701 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000702](../../agents/research.py#L702) | 702 | `"        if title and title_key in seen_titles:"` | — |
| [SRC-59CF4B7DE8-L000703](../../agents/research.py#L703) | 703 | `"            diag.append({\"reason\": \"duplicate_title_domain\", \"url\": url})"` | — |
| [SRC-59CF4B7DE8-L000704](../../agents/research.py#L704) | 704 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000705](../../agents/research.py#L705) | 705 | `""` | — |
| [SRC-59CF4B7DE8-L000706](../../agents/research.py#L706) | 706 | `"        rel = source_relevance_score(src, combined)"` | — |
| [SRC-59CF4B7DE8-L000707](../../agents/research.py#L707) | 707 | `"        if not rel[\"accepted\"]:"` | — |
| [SRC-59CF4B7DE8-L000708](../../agents/research.py#L708) | 708 | `"            diag.append({\"reason\": rel[\"reason\"], \"url\": url, \"score\": rel[\"score\"]})"` | — |
| [SRC-59CF4B7DE8-L000709](../../agents/research.py#L709) | 709 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000710](../../agents/research.py#L710) | 710 | `""` | — |
| [SRC-59CF4B7DE8-L000711](../../agents/research.py#L711) | 711 | `"        kept.append(src)"` | — |
| [SRC-59CF4B7DE8-L000712](../../agents/research.py#L712) | 712 | `"        if url_key:"` | — |
| [SRC-59CF4B7DE8-L000713](../../agents/research.py#L713) | 713 | `"            seen_urls.add(url_key)"` | — |
| [SRC-59CF4B7DE8-L000714](../../agents/research.py#L714) | 714 | `"        if title:"` | — |
| [SRC-59CF4B7DE8-L000715](../../agents/research.py#L715) | 715 | `"            seen_titles.add(title_key)"` | — |
| [SRC-59CF4B7DE8-L000716](../../agents/research.py#L716) | 716 | `"    return kept, diag"` | — |
| [SRC-59CF4B7DE8-L000717](../../agents/research.py#L717) | 717 | `""` | — |
| [SRC-59CF4B7DE8-L000718](../../agents/research.py#L718) | 718 | `""` | — |
| [SRC-59CF4B7DE8-L000719](../../agents/research.py#L719) | 719 | `"def decide_evidence_status(sources, pages_read: int = 0,"` | — |
| [SRC-59CF4B7DE8-L000720](../../agents/research.py#L720) | 720 | `"                           provider_failures: int = 0,"` | — |
| [SRC-59CF4B7DE8-L000721](../../agents/research.py#L721) | 721 | `"                           search_attempted: bool = True) -> dict:"` | — |
| [SRC-59CF4B7DE8-L000722](../../agents/research.py#L722) | 722 | `"    if not search_attempted:"` | — |
| [SRC-59CF4B7DE8-L000723](../../agents/research.py#L723) | 723 | `"        return {\"evidence_status\": \"failed\", \"should_abstain\": True}"` | — |
| [SRC-59CF4B7DE8-L000724](../../agents/research.py#L724) | 724 | `""` | — |
| [SRC-59CF4B7DE8-L000725](../../agents/research.py#L725) | 725 | `"    domains = set()"` | — |
| [SRC-59CF4B7DE8-L000726](../../agents/research.py#L726) | 726 | `"    has_official = False"` | — |
| [SRC-59CF4B7DE8-L000727](../../agents/research.py#L727) | 727 | `"    for s in sources or []:"` | — |
| [SRC-59CF4B7DE8-L000728](../../agents/research.py#L728) | 728 | `"        if not isinstance(s, dict):"` | — |
| [SRC-59CF4B7DE8-L000729](../../agents/research.py#L729) | 729 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000730](../../agents/research.py#L730) | 730 | `"        d = str(s.get(\"domain\") or \"\").lower()"` | — |
| [SRC-59CF4B7DE8-L000731](../../agents/research.py#L731) | 731 | `"        if not d:"` | — |
| [SRC-59CF4B7DE8-L000732](../../agents/research.py#L732) | 732 | `"            url = str(s.get(\"url\") or \"\")"` | — |
| [SRC-59CF4B7DE8-L000733](../../agents/research.py#L733) | 733 | `"            if url:"` | — |
| [SRC-59CF4B7DE8-L000734](../../agents/research.py#L734) | 734 | `"                try:"` | — |
| [SRC-59CF4B7DE8-L000735](../../agents/research.py#L735) | 735 | `"                    from urllib.parse import urlparse"` | — |
| [SRC-59CF4B7DE8-L000736](../../agents/research.py#L736) | 736 | `"                    d = urlparse(url).netloc.lower()"` | — |
| [SRC-59CF4B7DE8-L000737](../../agents/research.py#L737) | 737 | `"                except Exception:"` | — |
| [SRC-59CF4B7DE8-L000738](../../agents/research.py#L738) | 738 | `"                    d = \"\""` | — |
| [SRC-59CF4B7DE8-L000739](../../agents/research.py#L739) | 739 | `"        if d:"` | — |
| [SRC-59CF4B7DE8-L000740](../../agents/research.py#L740) | 740 | `"            domains.add(d)"` | — |
| [SRC-59CF4B7DE8-L000741](../../agents/research.py#L741) | 741 | `"        if str(s.get(\"source_class\") or \"\").lower() in _OFFICIAL_CLASSES:"` | — |
| [SRC-59CF4B7DE8-L000742](../../agents/research.py#L742) | 742 | `"            has_official = True"` | — |
| [SRC-59CF4B7DE8-L000743](../../agents/research.py#L743) | 743 | `""` | — |
| [SRC-59CF4B7DE8-L000744](../../agents/research.py#L744) | 744 | `"    if not sources:"` | — |
| [SRC-59CF4B7DE8-L000745](../../agents/research.py#L745) | 745 | `"        if provider_failures > 0:"` | — |
| [SRC-59CF4B7DE8-L000746](../../agents/research.py#L746) | 746 | `"            return {\"evidence_status\": \"failed\", \"should_abstain\": True}"` | — |
| [SRC-59CF4B7DE8-L000747](../../agents/research.py#L747) | 747 | `"        return {\"evidence_status\": \"insufficient\", \"should_abstain\": True}"` | — |
| [SRC-59CF4B7DE8-L000748](../../agents/research.py#L748) | 748 | `""` | — |
| [SRC-59CF4B7DE8-L000749](../../agents/research.py#L749) | 749 | `"    if len(domains) >= 2 or has_official:"` | — |
| [SRC-59CF4B7DE8-L000750](../../agents/research.py#L750) | 750 | `"        return {\"evidence_status\": \"adequate\", \"should_abstain\": False}"` | — |
| [SRC-59CF4B7DE8-L000751](../../agents/research.py#L751) | 751 | `"    if len(domains) >= 1:"` | — |
| [SRC-59CF4B7DE8-L000752](../../agents/research.py#L752) | 752 | `"        return {\"evidence_status\": \"partial\", \"should_abstain\": False}"` | — |
| [SRC-59CF4B7DE8-L000753](../../agents/research.py#L753) | 753 | `"    return {\"evidence_status\": \"insufficient\", \"should_abstain\": True}"` | — |
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
| [SRC-3AA6165B18-L000024](../../agents/research_guardrails.py#L24) | 24 | `"_OFFICIAL_WORDS = ("` | — |
| [SRC-3AA6165B18-L000025](../../agents/research_guardrails.py#L25) | 25 | `"    \"الموقع الرسمي\", \"موقع رسمي\", \"الصفحة الرسمية\", \"الموقع الحكومي\","` | — |
| [SRC-3AA6165B18-L000026](../../agents/research_guardrails.py#L26) | 26 | `"    \"official website\", \"official site\", \"official homepage\","` | — |
| [SRC-3AA6165B18-L000027](../../agents/research_guardrails.py#L27) | 27 | `")"` | — |
| [SRC-3AA6165B18-L000028](../../agents/research_guardrails.py#L28) | 28 | `"_GOVERNMENT_ENTITY_WORDS = ("` | — |
| [SRC-3AA6165B18-L000029](../../agents/research_guardrails.py#L29) | 29 | `"    \"وزارة\", \"الوزارة\", \"وزاره\", \"هيئة حكومية\", \"جهة حكومية\", \"مصلحة حكومية\","` | — |
| [SRC-3AA6165B18-L000030](../../agents/research_guardrails.py#L30) | 30 | `"    \"ministry\", \"government agency\", \"government ministry\", \"department of\","` | — |
| [SRC-3AA6165B18-L000031](../../agents/research_guardrails.py#L31) | 31 | `")"` | — |
| [SRC-3AA6165B18-L000032](../../agents/research_guardrails.py#L32) | 32 | `"_TODAY_WORDS = ("` | — |
| [SRC-3AA6165B18-L000033](../../agents/research_guardrails.py#L33) | 33 | `"    \"اليوم\", \"النهارده\", \"النهاردة\", \"دلوقتي\", \"الآن\", \"حاليا\","` | — |
| [SRC-3AA6165B18-L000034](../../agents/research_guardrails.py#L34) | 34 | `"    \"today\", \"right now\", \"currently\", \"current hours\","` | — |
| [SRC-3AA6165B18-L000035](../../agents/research_guardrails.py#L35) | 35 | `")"` | — |
| [SRC-3AA6165B18-L000036](../../agents/research_guardrails.py#L36) | 36 | `"_PROMOTION_TERMS = ("` | — |
| [SRC-3AA6165B18-L000037](../../agents/research_guardrails.py#L37) | 37 | `"    \"للبيع\", \"للايجار\", \"للإيجار\", \"تواصل معنا\", \"اتصل الآن\", \"واتساب\","` | — |
| [SRC-3AA6165B18-L000038](../../agents/research_guardrails.py#L38) | 38 | `"    \"للحجز\", \"اشتر الآن\", \"اطلب الآن\", \"خصم\", \"عرض خاص\", \"السعر يبدأ\","` | — |
| [SRC-3AA6165B18-L000039](../../agents/research_guardrails.py#L39) | 39 | `"    \"for sale\", \"contact us\", \"call now\", \"whatsapp\", \"buy now\", \"shop now\","` | — |
| [SRC-3AA6165B18-L000040](../../agents/research_guardrails.py#L40) | 40 | `"    \"special offer\", \"discount\", \"sponsored\", \"affiliate\","` | — |
| [SRC-3AA6165B18-L000041](../../agents/research_guardrails.py#L41) | 41 | `")"` | — |
| [SRC-3AA6165B18-L000042](../../agents/research_guardrails.py#L42) | 42 | `"_PERSONAL_EXPERIENCE_TERMS = ("` | — |
| [SRC-3AA6165B18-L000043](../../agents/research_guardrails.py#L43) | 43 | `"    \"أنا امتلك\", \"انا امتلك\", \"أنا أملك\", \"انا املك\", \"عندي\", \"معايا\","` | — |
| [SRC-3AA6165B18-L000044](../../agents/research_guardrails.py#L44) | 44 | `"    \"جربت\", \"استخدمت\", \"اشتريت\", \"امتلكت\", \"تجربتي\", \"عن تجربتي\","` | — |
| [SRC-3AA6165B18-L000045](../../agents/research_guardrails.py#L45) | 45 | `"    \"بقالى\", \"بقالي\", \"I own\", \"I bought\", \"I have owned\", \"my experience\","` | — |
| [SRC-3AA6165B18-L000046](../../agents/research_guardrails.py#L46) | 46 | `"    \"I've had\", \"i have had\", \"I use\", \"I drove\", \"in my experience\","` | — |
| [SRC-3AA6165B18-L000047](../../agents/research_guardrails.py#L47) | 47 | `")"` | — |
| [SRC-3AA6165B18-L000048](../../agents/research_guardrails.py#L48) | 48 | `"_DISCUSSION_TERMS = ("` | — |
| [SRC-3AA6165B18-L000049](../../agents/research_guardrails.py#L49) | 49 | `"    \"حد جرب\", \"هل جرب\", \"مين جرب\", \"ما رأيكم\", \"ايه رأيكم\", \"ماذا تظنون\","` | — |
| [SRC-3AA6165B18-L000050](../../agents/research_guardrails.py#L50) | 50 | `"    \"anyone tried\", \"has anyone\", \"what do you think\", \"looking for opinions\","` | — |
| [SRC-3AA6165B18-L000051](../../agents/research_guardrails.py#L51) | 51 | `")"` | — |
| [SRC-3AA6165B18-L000052](../../agents/research_guardrails.py#L52) | 52 | `""` | — |
| [SRC-3AA6165B18-L000053](../../agents/research_guardrails.py#L53) | 53 | `""` | — |
| [SRC-3AA6165B18-L000054](../../agents/research_guardrails.py#L54) | 54 | `"def _normalized(value: Any) -> str:"` | — |
| [SRC-3AA6165B18-L000055](../../agents/research_guardrails.py#L55) | 55 | `"    return re.sub(r\"\\s+\", \" \", str(value or \"\")).strip().casefold()"` | — |
| [SRC-3AA6165B18-L000056](../../agents/research_guardrails.py#L56) | 56 | `""` | — |
| [SRC-3AA6165B18-L000057](../../agents/research_guardrails.py#L57) | 57 | `""` | — |
| [SRC-3AA6165B18-L000058](../../agents/research_guardrails.py#L58) | 58 | `"def _host(value: Any) -> str:"` | — |
| [SRC-3AA6165B18-L000059](../../agents/research_guardrails.py#L59) | 59 | `"    try:"` | — |
| [SRC-3AA6165B18-L000060](../../agents/research_guardrails.py#L60) | 60 | `"        return (urlsplit(str(value or \"\").strip()).hostname or \"\").rstrip(\".\").lower()"` | — |
| [SRC-3AA6165B18-L000061](../../agents/research_guardrails.py#L61) | 61 | `"    except (TypeError, ValueError):"` | — |
| [SRC-3AA6165B18-L000062](../../agents/research_guardrails.py#L62) | 62 | `"        return \"\""` | — |
| [SRC-3AA6165B18-L000063](../../agents/research_guardrails.py#L63) | 63 | `""` | — |
| [SRC-3AA6165B18-L000064](../../agents/research_guardrails.py#L64) | 64 | `""` | — |
| [SRC-3AA6165B18-L000065](../../agents/research_guardrails.py#L65) | 65 | `"def is_social_platform_url(url: Any) -> bool:"` | — |
| [SRC-3AA6165B18-L000066](../../agents/research_guardrails.py#L66) | 66 | `"    \"\"\"Return whether a URL belongs to a recognized public social platform.\"\"\""` | — |
| [SRC-3AA6165B18-L000067](../../agents/research_guardrails.py#L67) | 67 | `"    host = _host(url)"` | — |
| [SRC-3AA6165B18-L000068](../../agents/research_guardrails.py#L68) | 68 | `"    if not host:"` | — |
| [SRC-3AA6165B18-L000069](../../agents/research_guardrails.py#L69) | 69 | `"        return False"` | — |
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
