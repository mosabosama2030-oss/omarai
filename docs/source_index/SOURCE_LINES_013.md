# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **013**
- سجلات الأسطر: **800**
- النطاق: SRC-1AE03B9EC3-L000487 إلى SRC-1AE03B9EC3-L001286
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-1AE03B9EC3 — [agents/web_agent.py](../../agents/web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1AE03B9EC3-L000487](../../agents/web_agent.py#L487) | 487 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000488](../../agents/web_agent.py#L488) | 488 | `""` | — |
| [SRC-1AE03B9EC3-L000489](../../agents/web_agent.py#L489) | 489 | `"def _public_ip_literals(host: str) -> list[str] \| None:"` | — |
| [SRC-1AE03B9EC3-L000490](../../agents/web_agent.py#L490) | 490 | `"    \"\"\"Resolve host and return its public addresses."` | — |
| [SRC-1AE03B9EC3-L000491](../../agents/web_agent.py#L491) | 491 | `""` | — |
| [SRC-1AE03B9EC3-L000492](../../agents/web_agent.py#L492) | 492 | `"    Returns None when resolution fails or any answer is not a global address."` | — |
| [SRC-1AE03B9EC3-L000493](../../agents/web_agent.py#L493) | 493 | `"    Callers must open the TCP connection to one of these literals. A second DNS"` | — |
| [SRC-1AE03B9EC3-L000494](../../agents/web_agent.py#L494) | 494 | `"    lookup is not equivalent: the name can be rebound to a private address"` | — |
| [SRC-1AE03B9EC3-L000495](../../agents/web_agent.py#L495) | 495 | `"    between the check and the connection (DNS rebinding / TOCTOU)."` | — |
| [SRC-1AE03B9EC3-L000496](../../agents/web_agent.py#L496) | 496 | `"    \"\"\""` | — |
| [SRC-1AE03B9EC3-L000497](../../agents/web_agent.py#L497) | 497 | `"    if not host:"` | — |
| [SRC-1AE03B9EC3-L000498](../../agents/web_agent.py#L498) | 498 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000499](../../agents/web_agent.py#L499) | 499 | `"    try:"` | — |
| [SRC-1AE03B9EC3-L000500](../../agents/web_agent.py#L500) | 500 | `"        answers = socket.getaddrinfo(host, None, type=socket.SOCK_STREAM)"` | — |
| [SRC-1AE03B9EC3-L000501](../../agents/web_agent.py#L501) | 501 | `"    except (OSError, socket.gaierror):"` | — |
| [SRC-1AE03B9EC3-L000502](../../agents/web_agent.py#L502) | 502 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000503](../../agents/web_agent.py#L503) | 503 | `"    if not answers:"` | — |
| [SRC-1AE03B9EC3-L000504](../../agents/web_agent.py#L504) | 504 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000505](../../agents/web_agent.py#L505) | 505 | `"    literals: list[str] = []"` | — |
| [SRC-1AE03B9EC3-L000506](../../agents/web_agent.py#L506) | 506 | `"    for answer in answers:"` | — |
| [SRC-1AE03B9EC3-L000507](../../agents/web_agent.py#L507) | 507 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L000508](../../agents/web_agent.py#L508) | 508 | `"            address = ipaddress.ip_address(answer[4][0])"` | — |
| [SRC-1AE03B9EC3-L000509](../../agents/web_agent.py#L509) | 509 | `"        except ValueError:"` | — |
| [SRC-1AE03B9EC3-L000510](../../agents/web_agent.py#L510) | 510 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L000511](../../agents/web_agent.py#L511) | 511 | `"        if not address.is_global:"` | — |
| [SRC-1AE03B9EC3-L000512](../../agents/web_agent.py#L512) | 512 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L000513](../../agents/web_agent.py#L513) | 513 | `"        literal = str(address)"` | — |
| [SRC-1AE03B9EC3-L000514](../../agents/web_agent.py#L514) | 514 | `"        if literal not in literals:"` | — |
| [SRC-1AE03B9EC3-L000515](../../agents/web_agent.py#L515) | 515 | `"            literals.append(literal)"` | — |
| [SRC-1AE03B9EC3-L000516](../../agents/web_agent.py#L516) | 516 | `"    return literals or None"` | — |
| [SRC-1AE03B9EC3-L000517](../../agents/web_agent.py#L517) | 517 | `""` | — |
| [SRC-1AE03B9EC3-L000518](../../agents/web_agent.py#L518) | 518 | `"def _host_resolves_publicly(host: str) -> bool:"` | — |
| [SRC-1AE03B9EC3-L000519](../../agents/web_agent.py#L519) | 519 | `"    \"\"\"Reject local/private destinations before fetching a third-party page.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000520](../../agents/web_agent.py#L520) | 520 | `"    return _public_ip_literals(host) is not None"` | — |
| [SRC-1AE03B9EC3-L000521](../../agents/web_agent.py#L521) | 521 | `""` | — |
| [SRC-1AE03B9EC3-L000522](../../agents/web_agent.py#L522) | 522 | `"def _pinned_connect_url(logical_url: str, ip: str) -> str \| None:"` | — |
| [SRC-1AE03B9EC3-L000523](../../agents/web_agent.py#L523) | 523 | `"    \"\"\"Rewrite a validated public URL so the connection target is a checked IP.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000524](../../agents/web_agent.py#L524) | 524 | `"    parsed = urllib.parse.urlparse(logical_url)"` | — |
| [SRC-1AE03B9EC3-L000525](../../agents/web_agent.py#L525) | 525 | `"    if parsed.port not in (None, 80, 443):"` | — |
| [SRC-1AE03B9EC3-L000526](../../agents/web_agent.py#L526) | 526 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000527](../../agents/web_agent.py#L527) | 527 | `"    literal = f\"[{ip}]\" if \":\" in ip else ip"` | — |
| [SRC-1AE03B9EC3-L000528](../../agents/web_agent.py#L528) | 528 | `"    netloc = literal if parsed.port is None else f\"{literal}:{parsed.port}\""` | — |
| [SRC-1AE03B9EC3-L000529](../../agents/web_agent.py#L529) | 529 | `"    return urllib.parse.urlunparse(parsed._replace(netloc=netloc))"` | — |
| [SRC-1AE03B9EC3-L000530](../../agents/web_agent.py#L530) | 530 | `""` | — |
| [SRC-1AE03B9EC3-L000531](../../agents/web_agent.py#L531) | 531 | `"def _fallback_answer(sources: list[dict[str, Any]], reason: str) -> str:"` | — |
| [SRC-1AE03B9EC3-L000532](../../agents/web_agent.py#L532) | 532 | `"    lines = [reason]"` | — |
| [SRC-1AE03B9EC3-L000533](../../agents/web_agent.py#L533) | 533 | `"    usable = [source for source in sources if source.get(\"snippet\")]"` | — |
| [SRC-1AE03B9EC3-L000534](../../agents/web_agent.py#L534) | 534 | `"    for index, source in enumerate(usable[:5], 1):"` | — |
| [SRC-1AE03B9EC3-L000535](../../agents/web_agent.py#L535) | 535 | `"        lines.append("` | — |
| [SRC-1AE03B9EC3-L000536](../../agents/web_agent.py#L536) | 536 | `"            f\"{index}. {source.get('title', 'نتيجة ويب')}: \""` | — |
| [SRC-1AE03B9EC3-L000537](../../agents/web_agent.py#L537) | 537 | `"            f\"{source['snippet']} (المصدر: {source['url']})\""` | — |
| [SRC-1AE03B9EC3-L000538](../../agents/web_agent.py#L538) | 538 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000539](../../agents/web_agent.py#L539) | 539 | `"    if not usable:"` | — |
| [SRC-1AE03B9EC3-L000540](../../agents/web_agent.py#L540) | 540 | `"        lines.append(\"لم أتمكن من استخراج مقتطفات كافية من نتائج الويب.\")"` | — |
| [SRC-1AE03B9EC3-L000541](../../agents/web_agent.py#L541) | 541 | `"    return \"\\n\\n\".join(lines)"` | — |
| [SRC-1AE03B9EC3-L000542](../../agents/web_agent.py#L542) | 542 | `""` | — |
| [SRC-1AE03B9EC3-L000543](../../agents/web_agent.py#L543) | 543 | `"def _fallback_lead_answer(sources: list[dict[str, Any]]) -> str:"` | — |
| [SRC-1AE03B9EC3-L000544](../../agents/web_agent.py#L544) | 544 | `"    \"\"\"Present only already-qualified public demand signals when synthesis is unavailable.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000545](../../agents/web_agent.py#L545) | 545 | `"    eligible = ["` | — |
| [SRC-1AE03B9EC3-L000546](../../agents/web_agent.py#L546) | 546 | `"        source for source in sources"` | — |
| [SRC-1AE03B9EC3-L000547](../../agents/web_agent.py#L547) | 547 | `"        if isinstance(source, dict)"` | — |
| [SRC-1AE03B9EC3-L000548](../../agents/web_agent.py#L548) | 548 | `"        and source.get(\"lead_qualification\") == \"public_demand_signal\""` | — |
| [SRC-1AE03B9EC3-L000549](../../agents/web_agent.py#L549) | 549 | `"        and isinstance(source.get(\"url\"), str)"` | — |
| [SRC-1AE03B9EC3-L000550](../../agents/web_agent.py#L550) | 550 | `"        and source.get(\"url\")"` | — |
| [SRC-1AE03B9EC3-L000551](../../agents/web_agent.py#L551) | 551 | `"    ]"` | — |
| [SRC-1AE03B9EC3-L000552](../../agents/web_agent.py#L552) | 552 | `"    lines = ["` | — |
| [SRC-1AE03B9EC3-L000553](../../agents/web_agent.py#L553) | 553 | `"        f\"تعذر توليد التحليل اللغوي في هذه المحاولة، لكن عُثر على {len(eligible)} إشارة طلب علنية مرشحة.\","` | — |
| [SRC-1AE03B9EC3-L000554](../../agents/web_agent.py#L554) | 554 | `"        \"هذه إشارات أولية وليست تأكيدًا لهوية صاحب المنشور أو استمرار حاجته أو ملاءمة المنتج. راجع المنشور الأصلي وتاريخه قبل التواصل.\","` | — |
| [SRC-1AE03B9EC3-L000555](../../agents/web_agent.py#L555) | 555 | `"    ]"` | — |
| [SRC-1AE03B9EC3-L000556](../../agents/web_agent.py#L556) | 556 | `"    for index, source in enumerate(eligible[:10], 1):"` | — |
| [SRC-1AE03B9EC3-L000557](../../agents/web_agent.py#L557) | 557 | `"        signal = source.get(\"lead_intent_evidence\")"` | — |
| [SRC-1AE03B9EC3-L000558](../../agents/web_agent.py#L558) | 558 | `"        phrase = signal.get(\"phrase\") if isinstance(signal, dict) else \"\""` | — |
| [SRC-1AE03B9EC3-L000559](../../agents/web_agent.py#L559) | 559 | `"        snippet = _clean_text(source.get(\"snippet\") or source.get(\"page_text\") or \"\", 700)"` | — |
| [SRC-1AE03B9EC3-L000560](../../agents/web_agent.py#L560) | 560 | `"        title = _clean_text(source.get(\"title\") or \"منشور عام محتمل\", 300)"` | — |
| [SRC-1AE03B9EC3-L000561](../../agents/web_agent.py#L561) | 561 | `"        lines.append("` | — |
| [SRC-1AE03B9EC3-L000562](../../agents/web_agent.py#L562) | 562 | `"            f\"{index}. {title}\\n\""` | — |
| [SRC-1AE03B9EC3-L000563](../../agents/web_agent.py#L563) | 563 | `"            f\"   عبارة المطابقة بعد التطبيع: {phrase or 'إشارة طلب صريحة'}\\n\""` | — |
| [SRC-1AE03B9EC3-L000564](../../agents/web_agent.py#L564) | 564 | `"            f\"   المقتطف: {snippet or 'لا يتوفر مقتطف مقروء؛ راجع الصفحة الأصلية.'}\\n\""` | — |
| [SRC-1AE03B9EC3-L000565](../../agents/web_agent.py#L565) | 565 | `"            f\"   المصدر: {source['url']}\\n\""` | — |
| [SRC-1AE03B9EC3-L000566](../../agents/web_agent.py#L566) | 566 | `"            \"   الحالة: مرشح يحتاج إلى تحقق يدوي من السياق والحداثة.\""` | — |
| [SRC-1AE03B9EC3-L000567](../../agents/web_agent.py#L567) | 567 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000568](../../agents/web_agent.py#L568) | 568 | `"    return \"\\n\\n\".join(lines)"` | — |
| [SRC-1AE03B9EC3-L000569](../../agents/web_agent.py#L569) | 569 | `""` | — |
| [SRC-1AE03B9EC3-L000570](../../agents/web_agent.py#L570) | 570 | `""` | — |
| [SRC-1AE03B9EC3-L000571](../../agents/web_agent.py#L571) | 571 | `"class PageFetchResult(tuple):"` | — |
| [SRC-1AE03B9EC3-L000572](../../agents/web_agent.py#L572) | 572 | `"    \"\"\"Two-item tuple compatible with legacy callers, with structured extraction status.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000573](../../agents/web_agent.py#L573) | 573 | `""` | — |
| [SRC-1AE03B9EC3-L000574](../../agents/web_agent.py#L574) | 574 | `"    def __new__("` | — |
| [SRC-1AE03B9EC3-L000575](../../agents/web_agent.py#L575) | 575 | `"        cls,"` | — |
| [SRC-1AE03B9EC3-L000576](../../agents/web_agent.py#L576) | 576 | `"        title: str = \"\","` | — |
| [SRC-1AE03B9EC3-L000577](../../agents/web_agent.py#L577) | 577 | `"        page_text: str = \"\","` | — |
| [SRC-1AE03B9EC3-L000578](../../agents/web_agent.py#L578) | 578 | `"        status: str = \"unknown\","` | — |
| [SRC-1AE03B9EC3-L000579](../../agents/web_agent.py#L579) | 579 | `"        error_class: str \| None = None,"` | — |
| [SRC-1AE03B9EC3-L000580](../../agents/web_agent.py#L580) | 580 | `"    ):"` | — |
| [SRC-1AE03B9EC3-L000581](../../agents/web_agent.py#L581) | 581 | `"        value = super().__new__(cls, (title, page_text))"` | — |
| [SRC-1AE03B9EC3-L000582](../../agents/web_agent.py#L582) | 582 | `"        value.status = status"` | — |
| [SRC-1AE03B9EC3-L000583](../../agents/web_agent.py#L583) | 583 | `"        value.error_class = error_class"` | — |
| [SRC-1AE03B9EC3-L000584](../../agents/web_agent.py#L584) | 584 | `"        return value"` | — |
| [SRC-1AE03B9EC3-L000585](../../agents/web_agent.py#L585) | 585 | `""` | — |
| [SRC-1AE03B9EC3-L000586](../../agents/web_agent.py#L586) | 586 | `"def enforce_aspect_answer_completeness(result: dict[str, Any]) -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L000587](../../agents/web_agent.py#L587) | 587 | `"    \"\"\"Withhold a final answer if any explicit axis lacks a text candidate."` | — |
| [SRC-1AE03B9EC3-L000588](../../agents/web_agent.py#L588) | 588 | `""` | — |
| [SRC-1AE03B9EC3-L000589](../../agents/web_agent.py#L589) | 589 | `"    Lexical coverage is only a conservative evidence-presence check, not semantic"` | — |
| [SRC-1AE03B9EC3-L000590](../../agents/web_agent.py#L590) | 590 | `"    verification. A missing candidate therefore blocks a *complete* answer rather"` | — |
| [SRC-1AE03B9EC3-L000591](../../agents/web_agent.py#L591) | 591 | `"    than asserting the underlying fact is unavailable everywhere."` | — |
| [SRC-1AE03B9EC3-L000592](../../agents/web_agent.py#L592) | 592 | `"    \"\"\""` | — |
| [SRC-1AE03B9EC3-L000593](../../agents/web_agent.py#L593) | 593 | `"    search_report = result.get(\"search_report\")"` | — |
| [SRC-1AE03B9EC3-L000594](../../agents/web_agent.py#L594) | 594 | `"    if not isinstance(search_report, dict):"` | — |
| [SRC-1AE03B9EC3-L000595](../../agents/web_agent.py#L595) | 595 | `"        return result"` | — |
| [SRC-1AE03B9EC3-L000596](../../agents/web_agent.py#L596) | 596 | `"    prior_ledger = search_report.get(\"evidence_ledger\")"` | — |
| [SRC-1AE03B9EC3-L000597](../../agents/web_agent.py#L597) | 597 | `"    if not isinstance(prior_ledger, dict):"` | — |
| [SRC-1AE03B9EC3-L000598](../../agents/web_agent.py#L598) | 598 | `"        return result"` | — |
| [SRC-1AE03B9EC3-L000599](../../agents/web_agent.py#L599) | 599 | `"    aspects = prior_ledger.get(\"aspects\")"` | — |
| [SRC-1AE03B9EC3-L000600](../../agents/web_agent.py#L600) | 600 | `"    if not isinstance(aspects, list) or not aspects:"` | — |
| [SRC-1AE03B9EC3-L000601](../../agents/web_agent.py#L601) | 601 | `"        return result"` | — |
| [SRC-1AE03B9EC3-L000602](../../agents/web_agent.py#L602) | 602 | `"    targets = ["` | — |
| [SRC-1AE03B9EC3-L000603](../../agents/web_agent.py#L603) | 603 | `"        item[:120]"` | — |
| [SRC-1AE03B9EC3-L000604](../../agents/web_agent.py#L604) | 604 | `"        for item in aspects"` | — |
| [SRC-1AE03B9EC3-L000605](../../agents/web_agent.py#L605) | 605 | `"        if isinstance(item, str) and item.strip()"` | — |
| [SRC-1AE03B9EC3-L000606](../../agents/web_agent.py#L606) | 606 | `"    ][:8]"` | — |
| [SRC-1AE03B9EC3-L000607](../../agents/web_agent.py#L607) | 607 | `"    if not targets:"` | — |
| [SRC-1AE03B9EC3-L000608](../../agents/web_agent.py#L608) | 608 | `"        return result"` | — |
| [SRC-1AE03B9EC3-L000609](../../agents/web_agent.py#L609) | 609 | `""` | — |
| [SRC-1AE03B9EC3-L000610](../../agents/web_agent.py#L610) | 610 | `"    raw_sources = result.get(\"sources\")"` | — |
| [SRC-1AE03B9EC3-L000611](../../agents/web_agent.py#L611) | 611 | `"    sources = ("` | — |
| [SRC-1AE03B9EC3-L000612](../../agents/web_agent.py#L612) | 612 | `"        [item for item in raw_sources if isinstance(item, dict)]"` | — |
| [SRC-1AE03B9EC3-L000613](../../agents/web_agent.py#L613) | 613 | `"        if isinstance(raw_sources, list)"` | — |
| [SRC-1AE03B9EC3-L000614](../../agents/web_agent.py#L614) | 614 | `"        else []"` | — |
| [SRC-1AE03B9EC3-L000615](../../agents/web_agent.py#L615) | 615 | `"    )"` | — |
| [SRC-1AE03B9EC3-L000616](../../agents/web_agent.py#L616) | 616 | `"    ledger = build_evidence_ledger(targets, sources)"` | — |
| [SRC-1AE03B9EC3-L000617](../../agents/web_agent.py#L617) | 617 | `"    search_report[\"evidence_ledger\"] = ledger"` | — |
| [SRC-1AE03B9EC3-L000618](../../agents/web_agent.py#L618) | 618 | `"    search_report[\"aspects\"] = targets"` | — |
| [SRC-1AE03B9EC3-L000619](../../agents/web_agent.py#L619) | 619 | `"    search_report[\"aspect_diagnostics_ar\"] = arabic_aspect_diagnostics(ledger)"` | — |
| [SRC-1AE03B9EC3-L000620](../../agents/web_agent.py#L620) | 620 | `"    search_report[\"aspect_evidence_gaps\"] = list(ledger.get(\"missing\") or [])"` | — |
| [SRC-1AE03B9EC3-L000621](../../agents/web_agent.py#L621) | 621 | `"    search_report[\"aspect_coverage_lexical_ratio\"] = ledger.get(\"coverage_ratio\")"` | — |
| [SRC-1AE03B9EC3-L000622](../../agents/web_agent.py#L622) | 622 | `"    search_report[\"aspect_coverage_is_not_truth_score\"] = True"` | — |
| [SRC-1AE03B9EC3-L000623](../../agents/web_agent.py#L623) | 623 | `""` | — |
| [SRC-1AE03B9EC3-L000624](../../agents/web_agent.py#L624) | 624 | `"    result[\"aspects\"] = targets"` | — |
| [SRC-1AE03B9EC3-L000625](../../agents/web_agent.py#L625) | 625 | `"    result[\"aspect_evidence_gaps\"] = list(ledger.get(\"missing\") or [])"` | — |
| [SRC-1AE03B9EC3-L000626](../../agents/web_agent.py#L626) | 626 | `"    result[\"aspect_diagnostics_ar\"] = list(search_report[\"aspect_diagnostics_ar\"])"` | — |
| [SRC-1AE03B9EC3-L000627](../../agents/web_agent.py#L627) | 627 | `"    result[\"aspect_coverage_lexical_ratio\"] = ledger.get(\"coverage_ratio\")"` | — |
| [SRC-1AE03B9EC3-L000628](../../agents/web_agent.py#L628) | 628 | `"    result[\"aspect_coverage_is_not_truth_score\"] = True"` | — |
| [SRC-1AE03B9EC3-L000629](../../agents/web_agent.py#L629) | 629 | `""` | — |
| [SRC-1AE03B9EC3-L000630](../../agents/web_agent.py#L630) | 630 | `"    missing = list(ledger.get(\"missing\") or [])"` | — |
| [SRC-1AE03B9EC3-L000631](../../agents/web_agent.py#L631) | 631 | `"    if missing:"` | — |
| [SRC-1AE03B9EC3-L000632](../../agents/web_agent.py#L632) | 632 | `"        result[\"answer\"] = ("` | — |
| [SRC-1AE03B9EC3-L000633](../../agents/web_agent.py#L633) | 633 | `"            \"لم أقدّم إجابة نهائية؛ لأن نتائج البحث المتاحة لا تتضمن مرشحًا نصيًا كافيًا \""` | — |
| [SRC-1AE03B9EC3-L000634](../../agents/web_agent.py#L634) | 634 | `"            \"لكل المحاور المطلوبة. المحاور التي تحتاج إلى دليل إضافي: \""` | — |
| [SRC-1AE03B9EC3-L000635](../../agents/web_agent.py#L635) | 635 | `"            + \"، \".join(str(item) for item in missing)"` | — |
| [SRC-1AE03B9EC3-L000636](../../agents/web_agent.py#L636) | 636 | `"            + \". لن أعرض مسودة جزئية على أنها إجابة مكتملة. وهذا النقص يصف النتائج التي جُمعت \""` | — |
| [SRC-1AE03B9EC3-L000637](../../agents/web_agent.py#L637) | 637 | `"            \"فقط، ولا يثبت عدم وجود معلومات عنها خارجها.\""` | — |
| [SRC-1AE03B9EC3-L000638](../../agents/web_agent.py#L638) | 638 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000639](../../agents/web_agent.py#L639) | 639 | `"        result[\"answer_was_withheld\"] = True"` | — |
| [SRC-1AE03B9EC3-L000640](../../agents/web_agent.py#L640) | 640 | `"        result[\"answer_completeness_status\"] = \"incomplete_evidence_withheld\""` | — |
| [SRC-1AE03B9EC3-L000641](../../agents/web_agent.py#L641) | 641 | `"        result[\"final_answer_status\"] = \"incomplete_evidence_withheld\""` | — |
| [SRC-1AE03B9EC3-L000642](../../agents/web_agent.py#L642) | 642 | `"        result[\"task_fulfillment_status\"] = \"possible_gap_detected\""` | — |
| [SRC-1AE03B9EC3-L000643](../../agents/web_agent.py#L643) | 643 | `"        search_report[\"task_fulfillment_status\"] = \"possible_gap_detected\""` | — |
| [SRC-1AE03B9EC3-L000644](../../agents/web_agent.py#L644) | 644 | `"        answer_coverage = result.get(\"answer_coverage\")"` | — |
| [SRC-1AE03B9EC3-L000645](../../agents/web_agent.py#L645) | 645 | `"        if isinstance(answer_coverage, dict):"` | — |
| [SRC-1AE03B9EC3-L000646](../../agents/web_agent.py#L646) | 646 | `"            answer_coverage[\"task_fulfillment_status\"] = \"possible_gap_detected\""` | — |
| [SRC-1AE03B9EC3-L000647](../../agents/web_agent.py#L647) | 647 | `"        warning = \"حُجبت الإجابة النهائية لوجود محاور مطلوبة بلا مرشح نصي كافٍ.\""` | — |
| [SRC-1AE03B9EC3-L000648](../../agents/web_agent.py#L648) | 648 | `"        warnings = result.setdefault(\"warnings\", [])"` | — |
| [SRC-1AE03B9EC3-L000649](../../agents/web_agent.py#L649) | 649 | `"        if isinstance(warnings, list) and warning not in warnings:"` | — |
| [SRC-1AE03B9EC3-L000650](../../agents/web_agent.py#L650) | 650 | `"            warnings.append(warning)"` | — |
| [SRC-1AE03B9EC3-L000651](../../agents/web_agent.py#L651) | 651 | `"    else:"` | — |
| [SRC-1AE03B9EC3-L000652](../../agents/web_agent.py#L652) | 652 | `"        result[\"answer_was_withheld\"] = False"` | — |
| [SRC-1AE03B9EC3-L000653](../../agents/web_agent.py#L653) | 653 | `"        result[\"answer_completeness_status\"] = ("` | — |
| [SRC-1AE03B9EC3-L000654](../../agents/web_agent.py#L654) | 654 | `"            \"no_lexical_gaps_detected_semantic_completeness_not_proven\""` | — |
| [SRC-1AE03B9EC3-L000655](../../agents/web_agent.py#L655) | 655 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000656](../../agents/web_agent.py#L656) | 656 | `"    return result"` | — |
| [SRC-1AE03B9EC3-L000657](../../agents/web_agent.py#L657) | 657 | `""` | — |
| [SRC-1AE03B9EC3-L000658](../../agents/web_agent.py#L658) | 658 | `"class WebAgent:"` | — |
| [SRC-1AE03B9EC3-L000659](../../agents/web_agent.py#L659) | 659 | `"    \"\"\"Search, inspect, and synthesize web evidence for open-ended questions.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000660](../../agents/web_agent.py#L660) | 660 | `""` | — |
| [SRC-1AE03B9EC3-L000661](../../agents/web_agent.py#L661) | 661 | `"    def __init__(self) -> None:"` | — |
| [SRC-1AE03B9EC3-L000662](../../agents/web_agent.py#L662) | 662 | `"        generic_api_key = ("` | — |
| [SRC-1AE03B9EC3-L000663](../../agents/web_agent.py#L663) | 663 | `"            os.getenv(\"OMARAI_LLM_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000664](../../agents/web_agent.py#L664) | 664 | `"            or os.getenv(\"OPENROUTER_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000665](../../agents/web_agent.py#L665) | 665 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000666](../../agents/web_agent.py#L666) | 666 | `"        gemini_api_key = os.getenv(\"GEMINI_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000667](../../agents/web_agent.py#L667) | 667 | `"        mistral_api_key = os.getenv(\"MISTRAL_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000668](../../agents/web_agent.py#L668) | 668 | `"        configured_base_url = os.getenv("` | — |
| [SRC-1AE03B9EC3-L000669](../../agents/web_agent.py#L669) | 669 | `"            \"OMARAI_LLM_BASE_URL\", \"https://openrouter.ai/api/v1\""` | — |
| [SRC-1AE03B9EC3-L000670](../../agents/web_agent.py#L670) | 670 | `"        ).strip().rstrip(\"/\")"` | — |
| [SRC-1AE03B9EC3-L000671](../../agents/web_agent.py#L671) | 671 | `"        global_model = os.getenv(\"OMARAI_LLM_MODEL\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000672](../../agents/web_agent.py#L672) | 672 | `""` | — |
| [SRC-1AE03B9EC3-L000673](../../agents/web_agent.py#L673) | 673 | `"        if generic_api_key:"` | — |
| [SRC-1AE03B9EC3-L000674](../../agents/web_agent.py#L674) | 674 | `"            host = (urllib.parse.urlsplit(configured_base_url).hostname or \"\").lower().rstrip(\".\")"` | — |
| [SRC-1AE03B9EC3-L000675](../../agents/web_agent.py#L675) | 675 | `"            primary_provider = \"openrouter\" if host == \"openrouter.ai\" else \"custom\""` | — |
| [SRC-1AE03B9EC3-L000676](../../agents/web_agent.py#L676) | 676 | `"            primary_api_key, primary_base_url = generic_api_key, configured_base_url"` | — |
| [SRC-1AE03B9EC3-L000677](../../agents/web_agent.py#L677) | 677 | `"            default_answer_model = \"google/gemma-4-31b-it:free\""` | — |
| [SRC-1AE03B9EC3-L000678](../../agents/web_agent.py#L678) | 678 | `"        elif gemini_api_key:"` | — |
| [SRC-1AE03B9EC3-L000679](../../agents/web_agent.py#L679) | 679 | `"            primary_provider, primary_api_key = \"gemini\", gemini_api_key"` | — |
| [SRC-1AE03B9EC3-L000680](../../agents/web_agent.py#L680) | 680 | `"            primary_base_url = \"https://generativelanguage.googleapis.com/v1beta/openai\""` | — |
| [SRC-1AE03B9EC3-L000681](../../agents/web_agent.py#L681) | 681 | `"            default_answer_model = ("` | — |
| [SRC-1AE03B9EC3-L000682](../../agents/web_agent.py#L682) | 682 | `"                os.getenv(\"OMARAI_GEMINI_MODEL\", \"\").strip() or \"gemini-3.1-flash-lite\""` | — |
| [SRC-1AE03B9EC3-L000683](../../agents/web_agent.py#L683) | 683 | `"            )"` | — |
| [SRC-1AE03B9EC3-L000684](../../agents/web_agent.py#L684) | 684 | `"        elif mistral_api_key:"` | — |
| [SRC-1AE03B9EC3-L000685](../../agents/web_agent.py#L685) | 685 | `"            primary_provider, primary_api_key = \"mistral\", mistral_api_key"` | — |
| [SRC-1AE03B9EC3-L000686](../../agents/web_agent.py#L686) | 686 | `"            primary_base_url = \"https://api.mistral.ai/v1\""` | — |
| [SRC-1AE03B9EC3-L000687](../../agents/web_agent.py#L687) | 687 | `"            default_answer_model = ("` | — |
| [SRC-1AE03B9EC3-L000688](../../agents/web_agent.py#L688) | 688 | `"                os.getenv(\"OMARAI_MISTRAL_MODEL\", \"\").strip() or \"mistral-small-latest\""` | — |
| [SRC-1AE03B9EC3-L000689](../../agents/web_agent.py#L689) | 689 | `"            )"` | — |
| [SRC-1AE03B9EC3-L000690](../../agents/web_agent.py#L690) | 690 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L000691](../../agents/web_agent.py#L691) | 691 | `"            primary_provider, primary_api_key = \"openrouter\", \"\""` | — |
| [SRC-1AE03B9EC3-L000692](../../agents/web_agent.py#L692) | 692 | `"            primary_base_url = configured_base_url"` | — |
| [SRC-1AE03B9EC3-L000693](../../agents/web_agent.py#L693) | 693 | `"            default_answer_model = \"google/gemma-4-31b-it:free\""` | — |
| [SRC-1AE03B9EC3-L000694](../../agents/web_agent.py#L694) | 694 | `""` | — |
| [SRC-1AE03B9EC3-L000695](../../agents/web_agent.py#L695) | 695 | `"        self.primary_provider = primary_provider"` | — |
| [SRC-1AE03B9EC3-L000696](../../agents/web_agent.py#L696) | 696 | `"        self.api_key, self.base_url = primary_api_key, primary_base_url"` | — |
| [SRC-1AE03B9EC3-L000697](../../agents/web_agent.py#L697) | 697 | `"        # Legacy research keeps its current connector policy; structured workspace"` | — |
| [SRC-1AE03B9EC3-L000698](../../agents/web_agent.py#L698) | 698 | `"        # discovery can disable optional providers per request."` | — |
| [SRC-1AE03B9EC3-L000699](../../agents/web_agent.py#L699) | 699 | `"        self.allow_optional_providers = True"` | — |
| [SRC-1AE03B9EC3-L000700](../../agents/web_agent.py#L700) | 700 | `"        self.answer_model = os.getenv("` | — |
| [SRC-1AE03B9EC3-L000701](../../agents/web_agent.py#L701) | 701 | `"            \"OMARAI_ANSWER_MODEL\", global_model or default_answer_model"` | — |
| [SRC-1AE03B9EC3-L000702](../../agents/web_agent.py#L702) | 702 | `"        ).strip()"` | — |
| [SRC-1AE03B9EC3-L000703](../../agents/web_agent.py#L703) | 703 | `"        planner_default = ("` | — |
| [SRC-1AE03B9EC3-L000704](../../agents/web_agent.py#L704) | 704 | `"            \"nvidia/nemotron-3-ultra-550b-a55b:free\""` | — |
| [SRC-1AE03B9EC3-L000705](../../agents/web_agent.py#L705) | 705 | `"            if primary_provider in {\"openrouter\", \"custom\"}"` | — |
| [SRC-1AE03B9EC3-L000706](../../agents/web_agent.py#L706) | 706 | `"            else self.answer_model"` | — |
| [SRC-1AE03B9EC3-L000707](../../agents/web_agent.py#L707) | 707 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000708](../../agents/web_agent.py#L708) | 708 | `"        self.planner_model = os.getenv("` | — |
| [SRC-1AE03B9EC3-L000709](../../agents/web_agent.py#L709) | 709 | `"            \"OMARAI_PLANNER_MODEL\", global_model or planner_default"` | — |
| [SRC-1AE03B9EC3-L000710](../../agents/web_agent.py#L710) | 710 | `"        ).strip()"` | — |
| [SRC-1AE03B9EC3-L000711](../../agents/web_agent.py#L711) | 711 | `"        self.review_model = os.getenv(\"OMARAI_REVIEW_MODEL\", self.answer_model).strip()"` | — |
| [SRC-1AE03B9EC3-L000712](../../agents/web_agent.py#L712) | 712 | `"        verifier_default = ("` | — |
| [SRC-1AE03B9EC3-L000713](../../agents/web_agent.py#L713) | 713 | `"            \"nvidia/nemotron-3-ultra-550b-a55b:free\""` | — |
| [SRC-1AE03B9EC3-L000714](../../agents/web_agent.py#L714) | 714 | `"            if primary_provider in {\"openrouter\", \"custom\"}"` | — |
| [SRC-1AE03B9EC3-L000715](../../agents/web_agent.py#L715) | 715 | `"            else self.answer_model"` | — |
| [SRC-1AE03B9EC3-L000716](../../agents/web_agent.py#L716) | 716 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000717](../../agents/web_agent.py#L717) | 717 | `"        self.verifier_model = os.getenv("` | — |
| [SRC-1AE03B9EC3-L000718](../../agents/web_agent.py#L718) | 718 | `"            \"OMARAI_VERIFIER_MODEL\", verifier_default"` | — |
| [SRC-1AE03B9EC3-L000719](../../agents/web_agent.py#L719) | 719 | `"        ).strip()"` | — |
| [SRC-1AE03B9EC3-L000720](../../agents/web_agent.py#L720) | 720 | `"        fallback_default = \"openrouter/free\" if primary_provider == \"openrouter\" else \"\""` | — |
| [SRC-1AE03B9EC3-L000721](../../agents/web_agent.py#L721) | 721 | `"        self.fallback_model = os.getenv("` | — |
| [SRC-1AE03B9EC3-L000722](../../agents/web_agent.py#L722) | 722 | `"            \"OMARAI_LLM_FALLBACK_MODEL\", fallback_default"` | — |
| [SRC-1AE03B9EC3-L000723](../../agents/web_agent.py#L723) | 723 | `"        ).strip()"` | — |
| [SRC-1AE03B9EC3-L000724](../../agents/web_agent.py#L724) | 724 | `""` | — |
| [SRC-1AE03B9EC3-L000725](../../agents/web_agent.py#L725) | 725 | `"        self.model_providers: list[dict[str, str]] = []"` | — |
| [SRC-1AE03B9EC3-L000726](../../agents/web_agent.py#L726) | 726 | `"        if primary_api_key:"` | — |
| [SRC-1AE03B9EC3-L000727](../../agents/web_agent.py#L727) | 727 | `"            self.model_providers.append({"` | — |
| [SRC-1AE03B9EC3-L000728](../../agents/web_agent.py#L728) | 728 | `"                \"name\": primary_provider,"` | — |
| [SRC-1AE03B9EC3-L000729](../../agents/web_agent.py#L729) | 729 | `"                \"api_key\": primary_api_key,"` | — |
| [SRC-1AE03B9EC3-L000730](../../agents/web_agent.py#L730) | 730 | `"                \"base_url\": primary_base_url,"` | — |
| [SRC-1AE03B9EC3-L000731](../../agents/web_agent.py#L731) | 731 | `"                \"model\": self.answer_model,"` | — |
| [SRC-1AE03B9EC3-L000732](../../agents/web_agent.py#L732) | 732 | `"            })"` | — |
| [SRC-1AE03B9EC3-L000733](../../agents/web_agent.py#L733) | 733 | `"        if gemini_api_key and primary_provider != \"gemini\":"` | — |
| [SRC-1AE03B9EC3-L000734](../../agents/web_agent.py#L734) | 734 | `"            self.model_providers.append({"` | — |
| [SRC-1AE03B9EC3-L000735](../../agents/web_agent.py#L735) | 735 | `"                \"name\": \"gemini\","` | — |
| [SRC-1AE03B9EC3-L000736](../../agents/web_agent.py#L736) | 736 | `"                \"api_key\": gemini_api_key,"` | — |
| [SRC-1AE03B9EC3-L000737](../../agents/web_agent.py#L737) | 737 | `"                \"base_url\": \"https://generativelanguage.googleapis.com/v1beta/openai\","` | — |
| [SRC-1AE03B9EC3-L000738](../../agents/web_agent.py#L738) | 738 | `"                \"model\": os.getenv(\"OMARAI_GEMINI_MODEL\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000739](../../agents/web_agent.py#L739) | 739 | `"                or \"gemini-3.1-flash-lite\","` | — |
| [SRC-1AE03B9EC3-L000740](../../agents/web_agent.py#L740) | 740 | `"            })"` | — |
| [SRC-1AE03B9EC3-L000741](../../agents/web_agent.py#L741) | 741 | `"        if mistral_api_key and primary_provider != \"mistral\":"` | — |
| [SRC-1AE03B9EC3-L000742](../../agents/web_agent.py#L742) | 742 | `"            self.model_providers.append({"` | — |
| [SRC-1AE03B9EC3-L000743](../../agents/web_agent.py#L743) | 743 | `"                \"name\": \"mistral\","` | — |
| [SRC-1AE03B9EC3-L000744](../../agents/web_agent.py#L744) | 744 | `"                \"api_key\": mistral_api_key,"` | — |
| [SRC-1AE03B9EC3-L000745](../../agents/web_agent.py#L745) | 745 | `"                \"base_url\": \"https://api.mistral.ai/v1\","` | — |
| [SRC-1AE03B9EC3-L000746](../../agents/web_agent.py#L746) | 746 | `"                \"model\": os.getenv(\"OMARAI_MISTRAL_MODEL\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000747](../../agents/web_agent.py#L747) | 747 | `"                or \"mistral-small-latest\","` | — |
| [SRC-1AE03B9EC3-L000748](../../agents/web_agent.py#L748) | 748 | `"            })"` | — |
| [SRC-1AE03B9EC3-L000749](../../agents/web_agent.py#L749) | 749 | `""` | — |
| [SRC-1AE03B9EC3-L000750](../../agents/web_agent.py#L750) | 750 | `"        self.model = self.answer_model  # Backwards-compatible alias."` | — |
| [SRC-1AE03B9EC3-L000751](../../agents/web_agent.py#L751) | 751 | `"        self.model_usage: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L000752](../../agents/web_agent.py#L752) | 752 | `"        # Per-answer, bounded diagnostics contain only model identifiers and status metadata."` | — |
| [SRC-1AE03B9EC3-L000753](../../agents/web_agent.py#L753) | 753 | `"        # They intentionally exclude prompts, generated text, and provider response bodies."` | — |
| [SRC-1AE03B9EC3-L000754](../../agents/web_agent.py#L754) | 754 | `"        self.generation_diagnostics: list[dict[str, str]] = []"` | — |
| [SRC-1AE03B9EC3-L000755](../../agents/web_agent.py#L755) | 755 | `"        self.server_search_sources: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L000756](../../agents/web_agent.py#L756) | 756 | `"        self._provider_diagnostics: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L000757](../../agents/web_agent.py#L757) | 757 | `"        self._provider_diagnostics_lock = threading.Lock()"` | — |
| [SRC-1AE03B9EC3-L000758](../../agents/web_agent.py#L758) | 758 | `"        self._deepseek_budget_lock = threading.Lock()"` | — |
| [SRC-1AE03B9EC3-L000759](../../agents/web_agent.py#L759) | 759 | `"        self._deepseek_search_requests_reserved = 0"` | — |
| [SRC-1AE03B9EC3-L000760](../../agents/web_agent.py#L760) | 760 | `"        self.openrouter_web_search_enabled = ("` | — |
| [SRC-1AE03B9EC3-L000761](../../agents/web_agent.py#L761) | 761 | `"            os.getenv(\"OMARAI_OPENROUTER_WEB_SEARCH\", \"\").strip() == \"1\""` | — |
| [SRC-1AE03B9EC3-L000762](../../agents/web_agent.py#L762) | 762 | `"            and (urllib.parse.urlsplit(self.base_url).hostname or \"\").lower().rstrip(\".\")"` | — |
| [SRC-1AE03B9EC3-L000763](../../agents/web_agent.py#L763) | 763 | `"            == \"openrouter.ai\""` | — |
| [SRC-1AE03B9EC3-L000764](../../agents/web_agent.py#L764) | 764 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000765](../../agents/web_agent.py#L765) | 765 | `"        self.timeout = max("` | — |
| [SRC-1AE03B9EC3-L000766](../../agents/web_agent.py#L766) | 766 | `"            5, min(int(os.getenv(\"OMARAI_LLM_TIMEOUT\", str(LLM_TIMEOUT_SECONDS))), 60)"` | — |
| [SRC-1AE03B9EC3-L000767](../../agents/web_agent.py#L767) | 767 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000768](../../agents/web_agent.py#L768) | 768 | `"        self._request_budget: RequestBudget \| None = None"` | — |
| [SRC-1AE03B9EC3-L000769](../../agents/web_agent.py#L769) | 769 | `""` | — |
| [SRC-1AE03B9EC3-L000770](../../agents/web_agent.py#L770) | 770 | `"    def _effective_timeout(self, configured_seconds: float) -> float:"` | — |
| [SRC-1AE03B9EC3-L000771](../../agents/web_agent.py#L771) | 771 | `"        \"\"\"Limit one outbound operation to the remaining per-answer time budget.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000772](../../agents/web_agent.py#L772) | 772 | `"        budget = getattr(self, \"_request_budget\", None)"` | — |
| [SRC-1AE03B9EC3-L000773](../../agents/web_agent.py#L773) | 773 | `"        if budget is None:"` | — |
| [SRC-1AE03B9EC3-L000774](../../agents/web_agent.py#L774) | 774 | `"            return float(configured_seconds)"` | — |
| [SRC-1AE03B9EC3-L000775](../../agents/web_agent.py#L775) | 775 | `"        return budget.timeout_for(configured_seconds)"` | — |
| [SRC-1AE03B9EC3-L000776](../../agents/web_agent.py#L776) | 776 | `""` | — |
| [SRC-1AE03B9EC3-L000777](../../agents/web_agent.py#L777) | 777 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000778](../../agents/web_agent.py#L778) | 778 | `"    def status() -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L000779](../../agents/web_agent.py#L779) | 779 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L000780](../../agents/web_agent.py#L780) | 780 | `"            import bs4  # noqa: F401"` | — |
| [SRC-1AE03B9EC3-L000781](../../agents/web_agent.py#L781) | 781 | `"            import httpx  # noqa: F401"` | — |
| [SRC-1AE03B9EC3-L000782](../../agents/web_agent.py#L782) | 782 | `"            search_ready = True"` | — |
| [SRC-1AE03B9EC3-L000783](../../agents/web_agent.py#L783) | 783 | `"        except ImportError:"` | — |
| [SRC-1AE03B9EC3-L000784](../../agents/web_agent.py#L784) | 784 | `"            search_ready = False"` | — |
| [SRC-1AE03B9EC3-L000785](../../agents/web_agent.py#L785) | 785 | `""` | — |
| [SRC-1AE03B9EC3-L000786](../../agents/web_agent.py#L786) | 786 | `"        generic_api_key = ("` | — |
| [SRC-1AE03B9EC3-L000787](../../agents/web_agent.py#L787) | 787 | `"            os.getenv(\"OMARAI_LLM_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000788](../../agents/web_agent.py#L788) | 788 | `"            or os.getenv(\"OPENROUTER_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000789](../../agents/web_agent.py#L789) | 789 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000790](../../agents/web_agent.py#L790) | 790 | `"        gemini_api_key = os.getenv(\"GEMINI_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000791](../../agents/web_agent.py#L791) | 791 | `"        mistral_api_key = os.getenv(\"MISTRAL_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000792](../../agents/web_agent.py#L792) | 792 | `"        configured_base_url = os.getenv("` | — |
| [SRC-1AE03B9EC3-L000793](../../agents/web_agent.py#L793) | 793 | `"            \"OMARAI_LLM_BASE_URL\", \"https://openrouter.ai/api/v1\""` | — |
| [SRC-1AE03B9EC3-L000794](../../agents/web_agent.py#L794) | 794 | `"        ).strip().rstrip(\"/\")"` | — |
| [SRC-1AE03B9EC3-L000795](../../agents/web_agent.py#L795) | 795 | `"        global_model = os.getenv(\"OMARAI_LLM_MODEL\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000796](../../agents/web_agent.py#L796) | 796 | `""` | — |
| [SRC-1AE03B9EC3-L000797](../../agents/web_agent.py#L797) | 797 | `"        if generic_api_key:"` | — |
| [SRC-1AE03B9EC3-L000798](../../agents/web_agent.py#L798) | 798 | `"            host = (urllib.parse.urlsplit(configured_base_url).hostname or \"\").lower().rstrip(\".\")"` | — |
| [SRC-1AE03B9EC3-L000799](../../agents/web_agent.py#L799) | 799 | `"            primary_provider = \"openrouter\" if host == \"openrouter.ai\" else \"custom\""` | — |
| [SRC-1AE03B9EC3-L000800](../../agents/web_agent.py#L800) | 800 | `"            primary_base_url = configured_base_url"` | — |
| [SRC-1AE03B9EC3-L000801](../../agents/web_agent.py#L801) | 801 | `"            default_answer_model = \"google/gemma-4-31b-it:free\""` | — |
| [SRC-1AE03B9EC3-L000802](../../agents/web_agent.py#L802) | 802 | `"        elif gemini_api_key:"` | — |
| [SRC-1AE03B9EC3-L000803](../../agents/web_agent.py#L803) | 803 | `"            primary_provider = \"gemini\""` | — |
| [SRC-1AE03B9EC3-L000804](../../agents/web_agent.py#L804) | 804 | `"            primary_base_url = \"https://generativelanguage.googleapis.com/v1beta/openai\""` | — |
| [SRC-1AE03B9EC3-L000805](../../agents/web_agent.py#L805) | 805 | `"            default_answer_model = ("` | — |
| [SRC-1AE03B9EC3-L000806](../../agents/web_agent.py#L806) | 806 | `"                os.getenv(\"OMARAI_GEMINI_MODEL\", \"\").strip() or \"gemini-3.1-flash-lite\""` | — |
| [SRC-1AE03B9EC3-L000807](../../agents/web_agent.py#L807) | 807 | `"            )"` | — |
| [SRC-1AE03B9EC3-L000808](../../agents/web_agent.py#L808) | 808 | `"        elif mistral_api_key:"` | — |
| [SRC-1AE03B9EC3-L000809](../../agents/web_agent.py#L809) | 809 | `"            primary_provider = \"mistral\""` | — |
| [SRC-1AE03B9EC3-L000810](../../agents/web_agent.py#L810) | 810 | `"            primary_base_url = \"https://api.mistral.ai/v1\""` | — |
| [SRC-1AE03B9EC3-L000811](../../agents/web_agent.py#L811) | 811 | `"            default_answer_model = ("` | — |
| [SRC-1AE03B9EC3-L000812](../../agents/web_agent.py#L812) | 812 | `"                os.getenv(\"OMARAI_MISTRAL_MODEL\", \"\").strip() or \"mistral-small-latest\""` | — |
| [SRC-1AE03B9EC3-L000813](../../agents/web_agent.py#L813) | 813 | `"            )"` | — |
| [SRC-1AE03B9EC3-L000814](../../agents/web_agent.py#L814) | 814 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L000815](../../agents/web_agent.py#L815) | 815 | `"            primary_provider = \"openrouter\""` | — |
| [SRC-1AE03B9EC3-L000816](../../agents/web_agent.py#L816) | 816 | `"            primary_base_url = configured_base_url"` | — |
| [SRC-1AE03B9EC3-L000817](../../agents/web_agent.py#L817) | 817 | `"            default_answer_model = \"google/gemma-4-31b-it:free\""` | — |
| [SRC-1AE03B9EC3-L000818](../../agents/web_agent.py#L818) | 818 | `""` | — |
| [SRC-1AE03B9EC3-L000819](../../agents/web_agent.py#L819) | 819 | `"        answer_model = ("` | — |
| [SRC-1AE03B9EC3-L000820](../../agents/web_agent.py#L820) | 820 | `"            os.getenv(\"OMARAI_ANSWER_MODEL\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000821](../../agents/web_agent.py#L821) | 821 | `"            or global_model"` | — |
| [SRC-1AE03B9EC3-L000822](../../agents/web_agent.py#L822) | 822 | `"            or default_answer_model"` | — |
| [SRC-1AE03B9EC3-L000823](../../agents/web_agent.py#L823) | 823 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000824](../../agents/web_agent.py#L824) | 824 | `"        planner_default = ("` | — |
| [SRC-1AE03B9EC3-L000825](../../agents/web_agent.py#L825) | 825 | `"            \"nvidia/nemotron-3-ultra-550b-a55b:free\""` | — |
| [SRC-1AE03B9EC3-L000826](../../agents/web_agent.py#L826) | 826 | `"            if primary_provider in {\"openrouter\", \"custom\"}"` | — |
| [SRC-1AE03B9EC3-L000827](../../agents/web_agent.py#L827) | 827 | `"            else answer_model"` | — |
| [SRC-1AE03B9EC3-L000828](../../agents/web_agent.py#L828) | 828 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000829](../../agents/web_agent.py#L829) | 829 | `"        planner_model = ("` | — |
| [SRC-1AE03B9EC3-L000830](../../agents/web_agent.py#L830) | 830 | `"            os.getenv(\"OMARAI_PLANNER_MODEL\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000831](../../agents/web_agent.py#L831) | 831 | `"            or global_model"` | — |
| [SRC-1AE03B9EC3-L000832](../../agents/web_agent.py#L832) | 832 | `"            or planner_default"` | — |
| [SRC-1AE03B9EC3-L000833](../../agents/web_agent.py#L833) | 833 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000834](../../agents/web_agent.py#L834) | 834 | `"        review_model = os.getenv(\"OMARAI_REVIEW_MODEL\", \"\").strip() or answer_model"` | — |
| [SRC-1AE03B9EC3-L000835](../../agents/web_agent.py#L835) | 835 | `"        verifier_default = ("` | — |
| [SRC-1AE03B9EC3-L000836](../../agents/web_agent.py#L836) | 836 | `"            \"nvidia/nemotron-3-ultra-550b-a55b:free\""` | — |
| [SRC-1AE03B9EC3-L000837](../../agents/web_agent.py#L837) | 837 | `"            if primary_provider in {\"openrouter\", \"custom\"}"` | — |
| [SRC-1AE03B9EC3-L000838](../../agents/web_agent.py#L838) | 838 | `"            else answer_model"` | — |
| [SRC-1AE03B9EC3-L000839](../../agents/web_agent.py#L839) | 839 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000840](../../agents/web_agent.py#L840) | 840 | `"        verifier_model = ("` | — |
| [SRC-1AE03B9EC3-L000841](../../agents/web_agent.py#L841) | 841 | `"            os.getenv(\"OMARAI_VERIFIER_MODEL\", \"\").strip() or verifier_default"` | — |
| [SRC-1AE03B9EC3-L000842](../../agents/web_agent.py#L842) | 842 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000843](../../agents/web_agent.py#L843) | 843 | `"        fallback_default = \"openrouter/free\" if primary_provider == \"openrouter\" else \"\""` | — |
| [SRC-1AE03B9EC3-L000844](../../agents/web_agent.py#L844) | 844 | `"        fallback_model = ("` | — |
| [SRC-1AE03B9EC3-L000845](../../agents/web_agent.py#L845) | 845 | `"            os.getenv(\"OMARAI_LLM_FALLBACK_MODEL\", \"\").strip() or fallback_default"` | — |
| [SRC-1AE03B9EC3-L000846](../../agents/web_agent.py#L846) | 846 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000847](../../agents/web_agent.py#L847) | 847 | `""` | — |
| [SRC-1AE03B9EC3-L000848](../../agents/web_agent.py#L848) | 848 | `"        provider_status: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L000849](../../agents/web_agent.py#L849) | 849 | `"        if generic_api_key:"` | — |
| [SRC-1AE03B9EC3-L000850](../../agents/web_agent.py#L850) | 850 | `"            provider_status.append({"` | — |
| [SRC-1AE03B9EC3-L000851](../../agents/web_agent.py#L851) | 851 | `"                \"name\": primary_provider,"` | — |
| [SRC-1AE03B9EC3-L000852](../../agents/web_agent.py#L852) | 852 | `"                \"configured\": True,"` | — |
| [SRC-1AE03B9EC3-L000853](../../agents/web_agent.py#L853) | 853 | `"                \"model\": answer_model,"` | — |
| [SRC-1AE03B9EC3-L000854](../../agents/web_agent.py#L854) | 854 | `"            })"` | — |
| [SRC-1AE03B9EC3-L000855](../../agents/web_agent.py#L855) | 855 | `"        if gemini_api_key and primary_provider != \"gemini\":"` | — |
| [SRC-1AE03B9EC3-L000856](../../agents/web_agent.py#L856) | 856 | `"            provider_status.append({"` | — |
| [SRC-1AE03B9EC3-L000857](../../agents/web_agent.py#L857) | 857 | `"                \"name\": \"gemini\","` | — |
| [SRC-1AE03B9EC3-L000858](../../agents/web_agent.py#L858) | 858 | `"                \"configured\": True,"` | — |
| [SRC-1AE03B9EC3-L000859](../../agents/web_agent.py#L859) | 859 | `"                \"model\": os.getenv(\"OMARAI_GEMINI_MODEL\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000860](../../agents/web_agent.py#L860) | 860 | `"                or \"gemini-3.1-flash-lite\","` | — |
| [SRC-1AE03B9EC3-L000861](../../agents/web_agent.py#L861) | 861 | `"            })"` | — |
| [SRC-1AE03B9EC3-L000862](../../agents/web_agent.py#L862) | 862 | `"        elif gemini_api_key:"` | — |
| [SRC-1AE03B9EC3-L000863](../../agents/web_agent.py#L863) | 863 | `"            provider_status.append({"` | — |
| [SRC-1AE03B9EC3-L000864](../../agents/web_agent.py#L864) | 864 | `"                \"name\": \"gemini\","` | — |
| [SRC-1AE03B9EC3-L000865](../../agents/web_agent.py#L865) | 865 | `"                \"configured\": True,"` | — |
| [SRC-1AE03B9EC3-L000866](../../agents/web_agent.py#L866) | 866 | `"                \"model\": answer_model,"` | — |
| [SRC-1AE03B9EC3-L000867](../../agents/web_agent.py#L867) | 867 | `"            })"` | — |
| [SRC-1AE03B9EC3-L000868](../../agents/web_agent.py#L868) | 868 | `"        if mistral_api_key and primary_provider != \"mistral\":"` | — |
| [SRC-1AE03B9EC3-L000869](../../agents/web_agent.py#L869) | 869 | `"            provider_status.append({"` | — |
| [SRC-1AE03B9EC3-L000870](../../agents/web_agent.py#L870) | 870 | `"                \"name\": \"mistral\","` | — |
| [SRC-1AE03B9EC3-L000871](../../agents/web_agent.py#L871) | 871 | `"                \"configured\": True,"` | — |
| [SRC-1AE03B9EC3-L000872](../../agents/web_agent.py#L872) | 872 | `"                \"model\": os.getenv(\"OMARAI_MISTRAL_MODEL\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000873](../../agents/web_agent.py#L873) | 873 | `"                or \"mistral-small-latest\","` | — |
| [SRC-1AE03B9EC3-L000874](../../agents/web_agent.py#L874) | 874 | `"            })"` | — |
| [SRC-1AE03B9EC3-L000875](../../agents/web_agent.py#L875) | 875 | `"        elif mistral_api_key:"` | — |
| [SRC-1AE03B9EC3-L000876](../../agents/web_agent.py#L876) | 876 | `"            provider_status.append({"` | — |
| [SRC-1AE03B9EC3-L000877](../../agents/web_agent.py#L877) | 877 | `"                \"name\": \"mistral\","` | — |
| [SRC-1AE03B9EC3-L000878](../../agents/web_agent.py#L878) | 878 | `"                \"configured\": True,"` | — |
| [SRC-1AE03B9EC3-L000879](../../agents/web_agent.py#L879) | 879 | `"                \"model\": answer_model,"` | — |
| [SRC-1AE03B9EC3-L000880](../../agents/web_agent.py#L880) | 880 | `"            })"` | — |
| [SRC-1AE03B9EC3-L000881](../../agents/web_agent.py#L881) | 881 | `""` | — |
| [SRC-1AE03B9EC3-L000882](../../agents/web_agent.py#L882) | 882 | `"        return {"` | — |
| [SRC-1AE03B9EC3-L000883](../../agents/web_agent.py#L883) | 883 | `"            \"web_search_ready\": search_ready,"` | — |
| [SRC-1AE03B9EC3-L000884](../../agents/web_agent.py#L884) | 884 | `"            \"language_model_configured\": bool("` | — |
| [SRC-1AE03B9EC3-L000885](../../agents/web_agent.py#L885) | 885 | `"                generic_api_key or gemini_api_key or mistral_api_key"` | — |
| [SRC-1AE03B9EC3-L000886](../../agents/web_agent.py#L886) | 886 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L000887](../../agents/web_agent.py#L887) | 887 | `"            \"language_model_provider\": _safe_model_provider_label(primary_base_url),"` | — |
| [SRC-1AE03B9EC3-L000888](../../agents/web_agent.py#L888) | 888 | `"            \"model_providers\": provider_status,"` | — |
| [SRC-1AE03B9EC3-L000889](../../agents/web_agent.py#L889) | 889 | `"            \"default_model\": answer_model,"` | — |
| [SRC-1AE03B9EC3-L000890](../../agents/web_agent.py#L890) | 890 | `"            \"planner_model\": planner_model,"` | — |
| [SRC-1AE03B9EC3-L000891](../../agents/web_agent.py#L891) | 891 | `"            \"answer_model\": answer_model,"` | — |
| [SRC-1AE03B9EC3-L000892](../../agents/web_agent.py#L892) | 892 | `"            \"review_model\": review_model,"` | — |
| [SRC-1AE03B9EC3-L000893](../../agents/web_agent.py#L893) | 893 | `"            \"semantic_verifier_model\": verifier_model,"` | — |
| [SRC-1AE03B9EC3-L000894](../../agents/web_agent.py#L894) | 894 | `"            \"semantic_verifier_distinct_from_answer_model\": bool("` | — |
| [SRC-1AE03B9EC3-L000895](../../agents/web_agent.py#L895) | 895 | `"                verifier_model and verifier_model.casefold() != answer_model.casefold()"` | — |
| [SRC-1AE03B9EC3-L000896](../../agents/web_agent.py#L896) | 896 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L000897](../../agents/web_agent.py#L897) | 897 | `"            \"semantic_verifier_scope\": ("` | — |
| [SRC-1AE03B9EC3-L000898](../../agents/web_agent.py#L898) | 898 | `"                \"distinct_model_id_same_configured_provider_not_ground_truth\""` | — |
| [SRC-1AE03B9EC3-L000899](../../agents/web_agent.py#L899) | 899 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L000900](../../agents/web_agent.py#L900) | 900 | `"            \"fallback_model\": fallback_model,"` | — |
| [SRC-1AE03B9EC3-L000901](../../agents/web_agent.py#L901) | 901 | `"            \"model_selection_mode\": \"role_specific_with_configured_provider_failover\","` | — |
| [SRC-1AE03B9EC3-L000902](../../agents/web_agent.py#L902) | 902 | `"            \"external_model_privacy_notice\": ("` | — |
| [SRC-1AE03B9EC3-L000903](../../agents/web_agent.py#L903) | 903 | `"                \"Prompts and selected page excerpts are sent to the configured external model provider. \""` | — |
| [SRC-1AE03B9EC3-L000904](../../agents/web_agent.py#L904) | 904 | `"                \"After a failed attempt, they may also be sent to other configured fallback providers. \""` | — |
| [SRC-1AE03B9EC3-L000905](../../agents/web_agent.py#L905) | 905 | `"                \"Do not submit secrets or personal/confidential customer data. The default free NVIDIA \""` | — |
| [SRC-1AE03B9EC3-L000906](../../agents/web_agent.py#L906) | 906 | `"                \"Nemotron endpoint states that sessions may be logged for security and product improvement.\""` | — |
| [SRC-1AE03B9EC3-L000907](../../agents/web_agent.py#L907) | 907 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L000908](../../agents/web_agent.py#L908) | 908 | `"            \"search_providers\": ["` | — |
| [SRC-1AE03B9EC3-L000909](../../agents/web_agent.py#L909) | 909 | `"                \"DuckDuckGo HTML\","` | — |
| [SRC-1AE03B9EC3-L000910](../../agents/web_agent.py#L910) | 910 | `"                \"Bing RSS\","` | — |
| [SRC-1AE03B9EC3-L000911](../../agents/web_agent.py#L911) | 911 | `"                \"Google News RSS for fresh queries\","` | — |
| [SRC-1AE03B9EC3-L000912](../../agents/web_agent.py#L912) | 912 | `"                \"DeepSeek Search API when DEEPSEEK_SEARCH_API_KEY is configured (optional; may incur charges)\","` | — |
| [SRC-1AE03B9EC3-L000913](../../agents/web_agent.py#L913) | 913 | `"                \"OpenRouter server-side live web search when OMARAI_OPENROUTER_WEB_SEARCH=1\","` | — |
| [SRC-1AE03B9EC3-L000914](../../agents/web_agent.py#L914) | 914 | `"                \"Brave Search API when BRAVE_SEARCH_API_KEY is configured\","` | — |
| [SRC-1AE03B9EC3-L000915](../../agents/web_agent.py#L915) | 915 | `"                \"Tavily Search API when TAVILY_API_KEY is configured\","` | — |
| [SRC-1AE03B9EC3-L000916](../../agents/web_agent.py#L916) | 916 | `"            ],"` | — |
| [SRC-1AE03B9EC3-L000917](../../agents/web_agent.py#L917) | 917 | `"            \"brave_search_api_configured\": bool(os.getenv(\"BRAVE_SEARCH_API_KEY\", \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L000918](../../agents/web_agent.py#L918) | 918 | `"            \"deepseek_search_api_configured\": bool("` | — |
| [SRC-1AE03B9EC3-L000919](../../agents/web_agent.py#L919) | 919 | `"                os.getenv(\"DEEPSEEK_SEARCH_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000920](../../agents/web_agent.py#L920) | 920 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L000921](../../agents/web_agent.py#L921) | 921 | `"            \"tavily_search_api_configured\": bool(os.getenv(\"TAVILY_API_KEY\", \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L000922](../../agents/web_agent.py#L922) | 922 | `"            \"openrouter_web_search_enabled\": ("` | — |
| [SRC-1AE03B9EC3-L000923](../../agents/web_agent.py#L923) | 923 | `"                os.getenv(\"OMARAI_OPENROUTER_WEB_SEARCH\", \"\").strip() == \"1\""` | — |
| [SRC-1AE03B9EC3-L000924](../../agents/web_agent.py#L924) | 924 | `"                and (urllib.parse.urlsplit(primary_base_url).hostname or \"\").lower().rstrip(\".\")"` | — |
| [SRC-1AE03B9EC3-L000925](../../agents/web_agent.py#L925) | 925 | `"                == \"openrouter.ai\""` | — |
| [SRC-1AE03B9EC3-L000926](../../agents/web_agent.py#L926) | 926 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L000927](../../agents/web_agent.py#L927) | 927 | `"            \"public_social_sources\": ["` | — |
| [SRC-1AE03B9EC3-L000928](../../agents/web_agent.py#L928) | 928 | `"                \"Reddit public RSS and optional authorized Reddit OAuth search\","` | — |
| [SRC-1AE03B9EC3-L000929](../../agents/web_agent.py#L929) | 929 | `"                \"Bluesky public search\","` | — |
| [SRC-1AE03B9EC3-L000930](../../agents/web_agent.py#L930) | 930 | `"                \"indexed public pages from Facebook, Instagram, X, TikTok, LinkedIn, Threads and YouTube\","` | — |
| [SRC-1AE03B9EC3-L000931](../../agents/web_agent.py#L931) | 931 | `"                \"official Instagram public hashtag media when an authorized Graph API token is configured\","` | — |
| [SRC-1AE03B9EC3-L000932](../../agents/web_agent.py#L932) | 932 | `"                \"configured Facebook Pages when a valid authorized page token is configured\","` | — |
| [SRC-1AE03B9EC3-L000933](../../agents/web_agent.py#L933) | 933 | `"                \"official X recent-post API when X_BEARER_TOKEN is configured\","` | — |
| [SRC-1AE03B9EC3-L000934](../../agents/web_agent.py#L934) | 934 | `"            ],"` | — |
| [SRC-1AE03B9EC3-L000935](../../agents/web_agent.py#L935) | 935 | `"            \"reddit_oauth_configured\": bool("` | — |
| [SRC-1AE03B9EC3-L000936](../../agents/web_agent.py#L936) | 936 | `"                os.getenv(\"REDDIT_CLIENT_ID\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000937](../../agents/web_agent.py#L937) | 937 | `"                and os.getenv(\"REDDIT_CLIENT_SECRET\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000938](../../agents/web_agent.py#L938) | 938 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L000939](../../agents/web_agent.py#L939) | 939 | `"            \"facebook_pages_api_configured\": bool("` | — |
| [SRC-1AE03B9EC3-L000940](../../agents/web_agent.py#L940) | 940 | `"                os.getenv(\"FACEBOOK_PAGE_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000941](../../agents/web_agent.py#L941) | 941 | `"                and os.getenv(\"FACEBOOK_PAGE_IDS\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000942](../../agents/web_agent.py#L942) | 942 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L000943](../../agents/web_agent.py#L943) | 943 | `"            \"x_api_configured\": bool(os.getenv(\"X_BEARER_TOKEN\", \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L000944](../../agents/web_agent.py#L944) | 944 | `"            \"instagram_graph_api_configured\": bool("` | — |
| [SRC-1AE03B9EC3-L000945](../../agents/web_agent.py#L945) | 945 | `"                os.getenv(\"INSTAGRAM_USER_ID\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000946](../../agents/web_agent.py#L946) | 946 | `"                and os.getenv(\"INSTAGRAM_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000947](../../agents/web_agent.py#L947) | 947 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L000948](../../agents/web_agent.py#L948) | 948 | `"            \"meta_graph_version\": os.getenv(\"META_GRAPH_VERSION\", \"v25.0\").strip(),"` | — |
| [SRC-1AE03B9EC3-L000949](../../agents/web_agent.py#L949) | 949 | `"            \"youtube_api_configured\": bool(os.getenv(\"YOUTUBE_API_KEY\", \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L000950](../../agents/web_agent.py#L950) | 950 | `"            \"youtube_direct_api\": bool(os.getenv(\"YOUTUBE_API_KEY\", \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L000951](../../agents/web_agent.py#L951) | 951 | `"            \"verification_scope\": {"` | — |
| [SRC-1AE03B9EC3-L000952](../../agents/web_agent.py#L952) | 952 | `"                \"kind\": \"configuration_snapshot\","` | — |
| [SRC-1AE03B9EC3-L000953](../../agents/web_agent.py#L953) | 953 | `"                \"live_network_checks_performed\": False,"` | — |
| [SRC-1AE03B9EC3-L000954](../../agents/web_agent.py#L954) | 954 | `"                \"web_search_ready_means\": \"dependencies_importable_not_provider_connectivity\","` | — |
| [SRC-1AE03B9EC3-L000955](../../agents/web_agent.py#L955) | 955 | `"                \"language_model_configured_means\": \"credential_present_not_successful_completion\","` | — |
| [SRC-1AE03B9EC3-L000956](../../agents/web_agent.py#L956) | 956 | `"                \"search_providers_means\": \"supported_or_conditionally_configured_not_live_verified\","` | — |
| [SRC-1AE03B9EC3-L000957](../../agents/web_agent.py#L957) | 957 | `"                \"direct_social_api_flags_mean\": \"credentials_present_not_permissions_or_connectivity_verified\","` | — |
| [SRC-1AE03B9EC3-L000958](../../agents/web_agent.py#L958) | 958 | `"                \"live_diagnostics_endpoint\": \"POST /api/diagnostics\","` | — |
| [SRC-1AE03B9EC3-L000959](../../agents/web_agent.py#L959) | 959 | `"            },"` | — |
| [SRC-1AE03B9EC3-L000960](../../agents/web_agent.py#L960) | 960 | `"        }"` | — |
| [SRC-1AE03B9EC3-L000961](../../agents/web_agent.py#L961) | 961 | `""` | — |
| [SRC-1AE03B9EC3-L000962](../../agents/web_agent.py#L962) | 962 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000963](../../agents/web_agent.py#L963) | 963 | `"    def _unwrap_search_url(value: str) -> str:"` | — |
| [SRC-1AE03B9EC3-L000964](../../agents/web_agent.py#L964) | 964 | `"        if value.startswith(\"//\"):"` | — |
| [SRC-1AE03B9EC3-L000965](../../agents/web_agent.py#L965) | 965 | `"            value = \"https:\" + value"` | — |
| [SRC-1AE03B9EC3-L000966](../../agents/web_agent.py#L966) | 966 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L000967](../../agents/web_agent.py#L967) | 967 | `"            parsed = urllib.parse.urlparse(value)"` | — |
| [SRC-1AE03B9EC3-L000968](../../agents/web_agent.py#L968) | 968 | `"            host = (parsed.hostname or \"\").lower()"` | — |
| [SRC-1AE03B9EC3-L000969](../../agents/web_agent.py#L969) | 969 | `"            if host.endswith(\"duckduckgo.com\") and parsed.path.startswith(\"/l/\"):"` | — |
| [SRC-1AE03B9EC3-L000970](../../agents/web_agent.py#L970) | 970 | `"                target = urllib.parse.parse_qs(parsed.query).get(\"uddg\", [\"\"])[0]"` | — |
| [SRC-1AE03B9EC3-L000971](../../agents/web_agent.py#L971) | 971 | `"                return urllib.parse.unquote(target) if target else \"\""` | — |
| [SRC-1AE03B9EC3-L000972](../../agents/web_agent.py#L972) | 972 | `"        except (ValueError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L000973](../../agents/web_agent.py#L973) | 973 | `"            return \"\""` | — |
| [SRC-1AE03B9EC3-L000974](../../agents/web_agent.py#L974) | 974 | `"        return value"` | — |
| [SRC-1AE03B9EC3-L000975](../../agents/web_agent.py#L975) | 975 | `""` | — |
| [SRC-1AE03B9EC3-L000976](../../agents/web_agent.py#L976) | 976 | `"    def _record_provider_diagnostic("` | — |
| [SRC-1AE03B9EC3-L000977](../../agents/web_agent.py#L977) | 977 | `"        self, provider: str, query: str, status: str, result_count: int = 0,"` | — |
| [SRC-1AE03B9EC3-L000978](../../agents/web_agent.py#L978) | 978 | `"        rejected_count: int = 0, error: str \| None = None,"` | — |
| [SRC-1AE03B9EC3-L000979](../../agents/web_agent.py#L979) | 979 | `"        accepted_count: int \| None = None,"` | — |
| [SRC-1AE03B9EC3-L000980](../../agents/web_agent.py#L980) | 980 | `"        rejection_counts: dict[str, int] \| None = None,"` | — |
| [SRC-1AE03B9EC3-L000981](../../agents/web_agent.py#L981) | 981 | `"    ) -> None:"` | — |
| [SRC-1AE03B9EC3-L000982](../../agents/web_agent.py#L982) | 982 | `"        def redact(value: Any, limit: int) -> str:"` | — |
| [SRC-1AE03B9EC3-L000983](../../agents/web_agent.py#L983) | 983 | `"            safe = _clean_text(str(value or \"\"), limit)"` | — |
| [SRC-1AE03B9EC3-L000984](../../agents/web_agent.py#L984) | 984 | `"            safe = re.sub("` | — |
| [SRC-1AE03B9EC3-L000985](../../agents/web_agent.py#L985) | 985 | `"                r\"(?i)(bearer\\s+)[A-Za-z0-9._~+/-]+=*\","` | — |
| [SRC-1AE03B9EC3-L000986](../../agents/web_agent.py#L986) | 986 | `"                r\"\\1[REDACTED]\","` | — |
| [SRC-1AE03B9EC3-L000987](../../agents/web_agent.py#L987) | 987 | `"                safe,"` | — |
| [SRC-1AE03B9EC3-L000988](../../agents/web_agent.py#L988) | 988 | `"            )"` | — |
| [SRC-1AE03B9EC3-L000989](../../agents/web_agent.py#L989) | 989 | `"            safe = re.sub("` | — |
| [SRC-1AE03B9EC3-L000990](../../agents/web_agent.py#L990) | 990 | `"                r\"(?i)\\b(api[_-]?key\|access[_-]?token\|refresh[_-]?token\|token\|secret\|password)\\s*[:=]\\s*[^\\s,;]+\","` | — |
| [SRC-1AE03B9EC3-L000991](../../agents/web_agent.py#L991) | 991 | `"                r\"\\1=[REDACTED]\","` | — |
| [SRC-1AE03B9EC3-L000992](../../agents/web_agent.py#L992) | 992 | `"                safe,"` | — |
| [SRC-1AE03B9EC3-L000993](../../agents/web_agent.py#L993) | 993 | `"            )"` | — |
| [SRC-1AE03B9EC3-L000994](../../agents/web_agent.py#L994) | 994 | `"            safe = re.sub("` | — |
| [SRC-1AE03B9EC3-L000995](../../agents/web_agent.py#L995) | 995 | `"                r\"(?i)([?&](?:api[_-]?key\|access[_-]?token\|token\|key)=)[^&\\s]+\","` | — |
| [SRC-1AE03B9EC3-L000996](../../agents/web_agent.py#L996) | 996 | `"                r\"\\1[REDACTED]\","` | — |
| [SRC-1AE03B9EC3-L000997](../../agents/web_agent.py#L997) | 997 | `"                safe,"` | — |
| [SRC-1AE03B9EC3-L000998](../../agents/web_agent.py#L998) | 998 | `"            )"` | — |
| [SRC-1AE03B9EC3-L000999](../../agents/web_agent.py#L999) | 999 | `"            return safe[:limit]"` | — |
| [SRC-1AE03B9EC3-L001000](../../agents/web_agent.py#L1000) | 1000 | `""` | — |
| [SRC-1AE03B9EC3-L001001](../../agents/web_agent.py#L1001) | 1001 | `"        record = {"` | — |
| [SRC-1AE03B9EC3-L001002](../../agents/web_agent.py#L1002) | 1002 | `"            \"provider\": provider,"` | — |
| [SRC-1AE03B9EC3-L001003](../../agents/web_agent.py#L1003) | 1003 | `"            \"query\": redact(query, 220),"` | — |
| [SRC-1AE03B9EC3-L001004](../../agents/web_agent.py#L1004) | 1004 | `"            \"status\": status,"` | — |
| [SRC-1AE03B9EC3-L001005](../../agents/web_agent.py#L1005) | 1005 | `"            \"result_count\": int(result_count),"` | — |
| [SRC-1AE03B9EC3-L001006](../../agents/web_agent.py#L1006) | 1006 | `"            \"accepted_count\": int(result_count if accepted_count is None else accepted_count),"` | — |
| [SRC-1AE03B9EC3-L001007](../../agents/web_agent.py#L1007) | 1007 | `"            \"rejected_count\": int(rejected_count),"` | — |
| [SRC-1AE03B9EC3-L001008](../../agents/web_agent.py#L1008) | 1008 | `"        }"` | — |
| [SRC-1AE03B9EC3-L001009](../../agents/web_agent.py#L1009) | 1009 | `"        if isinstance(rejection_counts, dict):"` | — |
| [SRC-1AE03B9EC3-L001010](../../agents/web_agent.py#L1010) | 1010 | `"            safe_counts: dict[str, int] = {}"` | — |
| [SRC-1AE03B9EC3-L001011](../../agents/web_agent.py#L1011) | 1011 | `"            for reason in _PROVIDER_REJECTION_REASONS:"` | — |
| [SRC-1AE03B9EC3-L001012](../../agents/web_agent.py#L1012) | 1012 | `"                try:"` | — |
| [SRC-1AE03B9EC3-L001013](../../agents/web_agent.py#L1013) | 1013 | `"                    safe_counts[reason] = max(0, int(rejection_counts.get(reason, 0) or 0))"` | — |
| [SRC-1AE03B9EC3-L001014](../../agents/web_agent.py#L1014) | 1014 | `"                except (TypeError, ValueError, OverflowError):"` | — |
| [SRC-1AE03B9EC3-L001015](../../agents/web_agent.py#L1015) | 1015 | `"                    safe_counts[reason] = 0"` | — |
| [SRC-1AE03B9EC3-L001016](../../agents/web_agent.py#L1016) | 1016 | `"            record[\"rejection_counts\"] = safe_counts"` | — |
| [SRC-1AE03B9EC3-L001017](../../agents/web_agent.py#L1017) | 1017 | `"        if error:"` | — |
| [SRC-1AE03B9EC3-L001018](../../agents/web_agent.py#L1018) | 1018 | `"            record[\"error\"] = redact(error, 180)"` | — |
| [SRC-1AE03B9EC3-L001019](../../agents/web_agent.py#L1019) | 1019 | `"        with self._provider_diagnostics_lock:"` | — |
| [SRC-1AE03B9EC3-L001020](../../agents/web_agent.py#L1020) | 1020 | `"            self._provider_diagnostics.append(record)"` | — |
| [SRC-1AE03B9EC3-L001021](../../agents/web_agent.py#L1021) | 1021 | `"            # Bound memory when the instance serves many user requests."` | — |
| [SRC-1AE03B9EC3-L001022](../../agents/web_agent.py#L1022) | 1022 | `"            self._provider_diagnostics = self._provider_diagnostics[-160:]"` | — |
| [SRC-1AE03B9EC3-L001023](../../agents/web_agent.py#L1023) | 1023 | `""` | — |
| [SRC-1AE03B9EC3-L001024](../../agents/web_agent.py#L1024) | 1024 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L001025](../../agents/web_agent.py#L1025) | 1025 | `"    def _source_matches_query(query: str, source: dict[str, Any]) -> bool:"` | — |
| [SRC-1AE03B9EC3-L001026](../../agents/web_agent.py#L1026) | 1026 | `"        if \"user_supplied_url\" in source.get(\"providers\", []):"` | — |
| [SRC-1AE03B9EC3-L001027](../../agents/web_agent.py#L1027) | 1027 | `"            return True"` | — |
| [SRC-1AE03B9EC3-L001028](../../agents/web_agent.py#L1028) | 1028 | `"        evidence = \" \".join("` | — |
| [SRC-1AE03B9EC3-L001029](../../agents/web_agent.py#L1029) | 1029 | `"            str(source.get(key) or \"\")"` | — |
| [SRC-1AE03B9EC3-L001030](../../agents/web_agent.py#L1030) | 1030 | `"            for key in (\"title\", \"snippet\", \"page_text\")"` | — |
| [SRC-1AE03B9EC3-L001031](../../agents/web_agent.py#L1031) | 1031 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001032](../../agents/web_agent.py#L1032) | 1032 | `"        return _relevance_ratio(query, evidence) >= 0.20"` | — |
| [SRC-1AE03B9EC3-L001033](../../agents/web_agent.py#L1033) | 1033 | `""` | — |
| [SRC-1AE03B9EC3-L001034](../../agents/web_agent.py#L1034) | 1034 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L001035](../../agents/web_agent.py#L1035) | 1035 | `"    def _normalized_source_url_key(value: Any) -> str:"` | — |
| [SRC-1AE03B9EC3-L001036](../../agents/web_agent.py#L1036) | 1036 | `"        \"\"\"Normalize a public HTTP(S) URL for duplicate detection across search rounds.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001037](../../agents/web_agent.py#L1037) | 1037 | `"        if not isinstance(value, str) or not value.strip():"` | — |
| [SRC-1AE03B9EC3-L001038](../../agents/web_agent.py#L1038) | 1038 | `"            return \"\""` | — |
| [SRC-1AE03B9EC3-L001039](../../agents/web_agent.py#L1039) | 1039 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L001040](../../agents/web_agent.py#L1040) | 1040 | `"            parsed = urllib.parse.urlsplit(value.strip())"` | — |
| [SRC-1AE03B9EC3-L001041](../../agents/web_agent.py#L1041) | 1041 | `"            scheme = parsed.scheme.lower()"` | — |
| [SRC-1AE03B9EC3-L001042](../../agents/web_agent.py#L1042) | 1042 | `"            if scheme not in {\"http\", \"https\"} or not parsed.hostname:"` | — |
| [SRC-1AE03B9EC3-L001043](../../agents/web_agent.py#L1043) | 1043 | `"                return \"\""` | — |
| [SRC-1AE03B9EC3-L001044](../../agents/web_agent.py#L1044) | 1044 | `"            host = parsed.hostname.lower().rstrip(\".\")"` | — |
| [SRC-1AE03B9EC3-L001045](../../agents/web_agent.py#L1045) | 1045 | `"            port = parsed.port"` | — |
| [SRC-1AE03B9EC3-L001046](../../agents/web_agent.py#L1046) | 1046 | `"            if (scheme == \"https\" and port == 443) or (scheme == \"http\" and port == 80):"` | — |
| [SRC-1AE03B9EC3-L001047](../../agents/web_agent.py#L1047) | 1047 | `"                port = None"` | — |
| [SRC-1AE03B9EC3-L001048](../../agents/web_agent.py#L1048) | 1048 | `"            host_for_url = f\"[{host}]\" if \":\" in host else host"` | — |
| [SRC-1AE03B9EC3-L001049](../../agents/web_agent.py#L1049) | 1049 | `"            netloc = host_for_url + (f\":{port}\" if port is not None else \"\")"` | — |
| [SRC-1AE03B9EC3-L001050](../../agents/web_agent.py#L1050) | 1050 | `"            path = parsed.path.rstrip(\"/\") or \"/\""` | — |
| [SRC-1AE03B9EC3-L001051](../../agents/web_agent.py#L1051) | 1051 | `"            tracking_keys = {\"fbclid\", \"gclid\", \"ref\", \"source\"}"` | — |
| [SRC-1AE03B9EC3-L001052](../../agents/web_agent.py#L1052) | 1052 | `"            query_items = ["` | — |
| [SRC-1AE03B9EC3-L001053](../../agents/web_agent.py#L1053) | 1053 | `"                (key, item)"` | — |
| [SRC-1AE03B9EC3-L001054](../../agents/web_agent.py#L1054) | 1054 | `"                for key, item in urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)"` | — |
| [SRC-1AE03B9EC3-L001055](../../agents/web_agent.py#L1055) | 1055 | `"                if not key.lower().startswith(\"utm_\") and key.lower() not in tracking_keys"` | — |
| [SRC-1AE03B9EC3-L001056](../../agents/web_agent.py#L1056) | 1056 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L001057](../../agents/web_agent.py#L1057) | 1057 | `"            query = urllib.parse.urlencode(query_items, doseq=True)"` | — |
| [SRC-1AE03B9EC3-L001058](../../agents/web_agent.py#L1058) | 1058 | `"            return urllib.parse.urlunsplit((scheme, netloc, path, query, \"\"))"` | — |
| [SRC-1AE03B9EC3-L001059](../../agents/web_agent.py#L1059) | 1059 | `"        except (TypeError, ValueError):"` | — |
| [SRC-1AE03B9EC3-L001060](../../agents/web_agent.py#L1060) | 1060 | `"            return \"\""` | — |
| [SRC-1AE03B9EC3-L001061](../../agents/web_agent.py#L1061) | 1061 | `""` | — |
| [SRC-1AE03B9EC3-L001062](../../agents/web_agent.py#L1062) | 1062 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L001063](../../agents/web_agent.py#L1063) | 1063 | `"    def _question_coverage_targets(question: str) -> list[str]:"` | — |
| [SRC-1AE03B9EC3-L001064](../../agents/web_agent.py#L1064) | 1064 | `"        \"\"\"Use the richer aspect parser, then the shared deterministic fallback.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001065](../../agents/web_agent.py#L1065) | 1065 | `"        enhanced_targets = extract_aspects(question)"` | — |
| [SRC-1AE03B9EC3-L001066](../../agents/web_agent.py#L1066) | 1066 | `"        if enhanced_targets:"` | — |
| [SRC-1AE03B9EC3-L001067](../../agents/web_agent.py#L1067) | 1067 | `"            return enhanced_targets[:8]"` | — |
| [SRC-1AE03B9EC3-L001068](../../agents/web_agent.py#L1068) | 1068 | `"        return extract_question_coverage_targets(question)"` | — |
| [SRC-1AE03B9EC3-L001069](../../agents/web_agent.py#L1069) | 1069 | `""` | — |
| [SRC-1AE03B9EC3-L001070](../../agents/web_agent.py#L1070) | 1070 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L001071](../../agents/web_agent.py#L1071) | 1071 | `"    def _is_current_search_status_question(question: str) -> bool:"` | — |
| [SRC-1AE03B9EC3-L001072](../../agents/web_agent.py#L1072) | 1072 | `"        \"\"\"Recognize a question about whether this answer already used web search.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001073](../../agents/web_agent.py#L1073) | 1073 | `"        value = _normalize_search_query(question).casefold()"` | — |
| [SRC-1AE03B9EC3-L001074](../../agents/web_agent.py#L1074) | 1074 | `"        asks_if_searched = any("` | — |
| [SRC-1AE03B9EC3-L001075](../../agents/web_agent.py#L1075) | 1075 | `"            term in value"` | — |
| [SRC-1AE03B9EC3-L001076](../../agents/web_agent.py#L1076) | 1076 | `"            for term in (\"بحثت\", \"اجريت بحث\", \"قمت بالبحث\", \"عملت بحث\", \"did you search\", \"did you browse\")"` | — |
| [SRC-1AE03B9EC3-L001077](../../agents/web_agent.py#L1077) | 1077 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001078](../../agents/web_agent.py#L1078) | 1078 | `"        references_web = any("` | — |
| [SRC-1AE03B9EC3-L001079](../../agents/web_agent.py#L1079) | 1079 | `"            term in value for term in (\"انترنت\", \"النت\", \"الويب\", \"ويب\", \"the web\", \"online\")"` | — |
| [SRC-1AE03B9EC3-L001080](../../agents/web_agent.py#L1080) | 1080 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001081](../../agents/web_agent.py#L1081) | 1081 | `"        references_current_answer = any("` | — |
| [SRC-1AE03B9EC3-L001082](../../agents/web_agent.py#L1082) | 1082 | `"            term in value"` | — |
| [SRC-1AE03B9EC3-L001083](../../agents/web_agent.py#L1083) | 1083 | `"            for term in ("` | — |
| [SRC-1AE03B9EC3-L001084](../../agents/web_agent.py#L1084) | 1084 | `"                \"اجاب\", \"الرد الحالي\", \"هذا السؤال\", \"هذه الاجابه\","` | — |
| [SRC-1AE03B9EC3-L001085](../../agents/web_agent.py#L1085) | 1085 | `"                \"this answer\", \"this response\","` | — |
| [SRC-1AE03B9EC3-L001086](../../agents/web_agent.py#L1086) | 1086 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001087](../../agents/web_agent.py#L1087) | 1087 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001088](../../agents/web_agent.py#L1088) | 1088 | `"        return asks_if_searched and references_web and references_current_answer"` | — |
| [SRC-1AE03B9EC3-L001089](../../agents/web_agent.py#L1089) | 1089 | `""` | — |
| [SRC-1AE03B9EC3-L001090](../../agents/web_agent.py#L1090) | 1090 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L001091](../../agents/web_agent.py#L1091) | 1091 | `"    def _is_self_question(question: str) -> bool:"` | — |
| [SRC-1AE03B9EC3-L001092](../../agents/web_agent.py#L1092) | 1092 | `"        \"\"\"Recognize questions about Omarai itself so they do not need web search.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001093](../../agents/web_agent.py#L1093) | 1093 | `"        value = _normalize_search_query(question).casefold()"` | — |
| [SRC-1AE03B9EC3-L001094](../../agents/web_agent.py#L1094) | 1094 | `"        # Do not mistake a capability-flavoured request with a concrete subject"` | — |
| [SRC-1AE03B9EC3-L001095](../../agents/web_agent.py#L1095) | 1095 | `"        # for a question about Omarai's capabilities (e.g. \"can you search for X?\")."` | — |
| [SRC-1AE03B9EC3-L001096](../../agents/web_agent.py#L1096) | 1096 | `"        if re.search("` | — |
| [SRC-1AE03B9EC3-L001097](../../agents/web_agent.py#L1097) | 1097 | `"            r\"(?:هل\\s+)?(?:تستطيع\|يمكنك\|تقدر)\\s+(?:ان\\s+)?(?:تبحث\|البحث)\\s+عن\\s+\\w{2,}\","` | — |
| [SRC-1AE03B9EC3-L001098](../../agents/web_agent.py#L1098) | 1098 | `"            value,"` | — |
| [SRC-1AE03B9EC3-L001099](../../agents/web_agent.py#L1099) | 1099 | `"        ) or re.search("` | — |
| [SRC-1AE03B9EC3-L001100](../../agents/web_agent.py#L1100) | 1100 | `"            r\"\\b(?:can\|could)\\s+you\\s+(?:search\\s+for\|look\\s+up\|find)\\s+\\w{2,}\\b\","` | — |
| [SRC-1AE03B9EC3-L001101](../../agents/web_agent.py#L1101) | 1101 | `"            value,"` | — |
| [SRC-1AE03B9EC3-L001102](../../agents/web_agent.py#L1102) | 1102 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L001103](../../agents/web_agent.py#L1103) | 1103 | `"            return False"` | — |
| [SRC-1AE03B9EC3-L001104](../../agents/web_agent.py#L1104) | 1104 | `"        capability_phrases = ("` | — |
| [SRC-1AE03B9EC3-L001105](../../agents/web_agent.py#L1105) | 1105 | `"            \"كيف تستطيع مساعدتي\", \"ازاي تقدر تساعدني\", \"ازاي ممكن تساعدني\","` | — |
| [SRC-1AE03B9EC3-L001106](../../agents/web_agent.py#L1106) | 1106 | `"            \"ماذا تستطيع ان تفعل\", \"ما الذي تستطيع فعله\", \"ايه اللي تقدر تعمله\","` | — |
| [SRC-1AE03B9EC3-L001107](../../agents/web_agent.py#L1107) | 1107 | `"            \"what can you do\", \"how can you help me\","` | — |
| [SRC-1AE03B9EC3-L001108](../../agents/web_agent.py#L1108) | 1108 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001109](../../agents/web_agent.py#L1109) | 1109 | `"        search_phrases = ("` | — |
| [SRC-1AE03B9EC3-L001110](../../agents/web_agent.py#L1110) | 1110 | `"            \"كيف تبحث انت\", \"ازاي بتبحث\", \"كيف يعمل البحث عندك\","` | — |
| [SRC-1AE03B9EC3-L001111](../../agents/web_agent.py#L1111) | 1111 | `"            \"ما المواقع التي تستخدمها\", \"ما محركات البحث التي تستخدمها\","` | — |
| [SRC-1AE03B9EC3-L001112](../../agents/web_agent.py#L1112) | 1112 | `"            \"ما المواقع التي قدرت\", \"كيف تبحث على الانترنت\","` | — |
| [SRC-1AE03B9EC3-L001113](../../agents/web_agent.py#L1113) | 1113 | `"            \"هل تستطيع البحث\", \"هل يمكنك البحث\", \"هل تقدر تبحث\","` | — |
| [SRC-1AE03B9EC3-L001114](../../agents/web_agent.py#L1114) | 1114 | `"            \"هل تستطيع الوصول\", \"هل يمكنك الوصول\","` | — |
| [SRC-1AE03B9EC3-L001115](../../agents/web_agent.py#L1115) | 1115 | `"            \"هل عندك اتصال بالانترنت\", \"هل عندك اتصال بالانترنيت\","` | — |
| [SRC-1AE03B9EC3-L001116](../../agents/web_agent.py#L1116) | 1116 | `"            \"هل عندك انترنت\","` | — |
| [SRC-1AE03B9EC3-L001117](../../agents/web_agent.py#L1117) | 1117 | `"            \"هل بحثت في الانترنت للاجابه الحاليه\","` | — |
| [SRC-1AE03B9EC3-L001118](../../agents/web_agent.py#L1118) | 1118 | `"            \"هل بحثت علي الانترنت للاجابه الحاليه\","` | — |
| [SRC-1AE03B9EC3-L001119](../../agents/web_agent.py#L1119) | 1119 | `"            \"هل بحثت في الانترنت لهذا السؤال\","` | — |
| [SRC-1AE03B9EC3-L001120](../../agents/web_agent.py#L1120) | 1120 | `"            \"هل بحثت في النت للرد ده\","` | — |
| [SRC-1AE03B9EC3-L001121](../../agents/web_agent.py#L1121) | 1121 | `"            \"did you search the web for this answer\","` | — |
| [SRC-1AE03B9EC3-L001122](../../agents/web_agent.py#L1122) | 1122 | `"            \"did you browse for this response\","` | — |
| [SRC-1AE03B9EC3-L001123](../../agents/web_agent.py#L1123) | 1123 | `"            \"how do you search\", \"which search engines\", \"what sites do you use\","` | — |
| [SRC-1AE03B9EC3-L001124](../../agents/web_agent.py#L1124) | 1124 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001125](../../agents/web_agent.py#L1125) | 1125 | `"        return ("` | — |
| [SRC-1AE03B9EC3-L001126](../../agents/web_agent.py#L1126) | 1126 | `"            any(phrase in value for phrase in capability_phrases + search_phrases)"` | — |
| [SRC-1AE03B9EC3-L001127](../../agents/web_agent.py#L1127) | 1127 | `"            or WebAgent._is_current_search_status_question(question)"` | — |
| [SRC-1AE03B9EC3-L001128](../../agents/web_agent.py#L1128) | 1128 | `"            or ("` | — |
| [SRC-1AE03B9EC3-L001129](../../agents/web_agent.py#L1129) | 1129 | `"                \"omarai\" in value"` | — |
| [SRC-1AE03B9EC3-L001130](../../agents/web_agent.py#L1130) | 1130 | `"                and any(token in value for token in (\"بحث\", \"موقع\", \"تستطيع\", \"تقدر\", \"تعمل\"))"` | — |
| [SRC-1AE03B9EC3-L001131](../../agents/web_agent.py#L1131) | 1131 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001132](../../agents/web_agent.py#L1132) | 1132 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001133](../../agents/web_agent.py#L1133) | 1133 | `""` | — |
| [SRC-1AE03B9EC3-L001134](../../agents/web_agent.py#L1134) | 1134 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L001135](../../agents/web_agent.py#L1135) | 1135 | `"    def _is_navigation_request(question: str) -> bool:"` | — |
| [SRC-1AE03B9EC3-L001136](../../agents/web_agent.py#L1136) | 1136 | `"        \"\"\"A link-finding task can be useful with one clearly labelled candidate result.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001137](../../agents/web_agent.py#L1137) | 1137 | `"        value = _normalize_search_query(question).casefold()"` | — |
| [SRC-1AE03B9EC3-L001138](../../agents/web_agent.py#L1138) | 1138 | `"        explicit_web_terms = ("` | — |
| [SRC-1AE03B9EC3-L001139](../../agents/web_agent.py#L1139) | 1139 | `"            \"رابط\", \"لينك\", \"الموقع الرسمي\", \"الصفحة الرسمية\", \"رابط الموقع\","` | — |
| [SRC-1AE03B9EC3-L001140](../../agents/web_agent.py#L1140) | 1140 | `"            \"لينك الموقع\", \"موقع الانترنت\", \"موقع الويب\", \"موقع الكتروني\","` | — |
| [SRC-1AE03B9EC3-L001141](../../agents/web_agent.py#L1141) | 1141 | `"            \"الموقع الالكتروني\", \"official website\", \"website\", \"homepage\","` | — |
| [SRC-1AE03B9EC3-L001142](../../agents/web_agent.py#L1142) | 1142 | `"            \"web page\", \"webpage\", \"link to\","` | — |
| [SRC-1AE03B9EC3-L001143](../../agents/web_agent.py#L1143) | 1143 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001144](../../agents/web_agent.py#L1144) | 1144 | `"        if any(term in value for term in explicit_web_terms):"` | — |
| [SRC-1AE03B9EC3-L001145](../../agents/web_agent.py#L1145) | 1145 | `"            return True"` | — |
| [SRC-1AE03B9EC3-L001146](../../agents/web_agent.py#L1146) | 1146 | `"        geographic_terms = ("` | — |
| [SRC-1AE03B9EC3-L001147](../../agents/web_agent.py#L1147) | 1147 | `"            \"جغرافيا\", \"جغرافي\", \"على الخريطه\", \"اين تقع\", \"اين يقع\","` | — |
| [SRC-1AE03B9EC3-L001148](../../agents/web_agent.py#L1148) | 1148 | `"            \"جغرافيه\", \"geographic location\", \"geographical location\","` | — |
| [SRC-1AE03B9EC3-L001149](../../agents/web_agent.py#L1149) | 1149 | `"            \"geographically\", \"where is located\","` | — |
| [SRC-1AE03B9EC3-L001150](../../agents/web_agent.py#L1150) | 1150 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001151](../../agents/web_agent.py#L1151) | 1151 | `"        if any(term in value for term in geographic_terms):"` | — |
| [SRC-1AE03B9EC3-L001152](../../agents/web_agent.py#L1152) | 1152 | `"            return False"` | — |
| [SRC-1AE03B9EC3-L001153](../../agents/web_agent.py#L1153) | 1153 | `"        # Bare \"موقع\" is ambiguous in Arabic. Keep the useful candidate-result"` | — |
| [SRC-1AE03B9EC3-L001154](../../agents/web_agent.py#L1154) | 1154 | `"        # exception only when the wording asks us to find/open a website."` | — |
| [SRC-1AE03B9EC3-L001155](../../agents/web_agent.py#L1155) | 1155 | `"        website_actions = ("` | — |
| [SRC-1AE03B9EC3-L001156](../../agents/web_agent.py#L1156) | 1156 | `"            \"ابحث عن موقع\", \"ابحث عن الموقع\", \"دور على موقع\", \"دورلي على موقع\","` | — |
| [SRC-1AE03B9EC3-L001157](../../agents/web_agent.py#L1157) | 1157 | `"            \"هات موقع\", \"هاتلي موقع\", \"اعطني موقع\", \"عايز موقع\", \"عاوز موقع\","` | — |
| [SRC-1AE03B9EC3-L001158](../../agents/web_agent.py#L1158) | 1158 | `"            \"محتاج موقع\", \"افتح موقع\","` | — |
| [SRC-1AE03B9EC3-L001159](../../agents/web_agent.py#L1159) | 1159 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001160](../../agents/web_agent.py#L1160) | 1160 | `"        return any(term in value for term in website_actions)"` | — |
| [SRC-1AE03B9EC3-L001161](../../agents/web_agent.py#L1161) | 1161 | `""` | — |
| [SRC-1AE03B9EC3-L001162](../../agents/web_agent.py#L1162) | 1162 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L001163](../../agents/web_agent.py#L1163) | 1163 | `"    def _is_lead_search(question: str) -> bool:"` | — |
| [SRC-1AE03B9EC3-L001164](../../agents/web_agent.py#L1164) | 1164 | `"        \"\"\"Keep lead discovery distinct from listing searches and generic explanations.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001165](../../agents/web_agent.py#L1165) | 1165 | `"        return route_intent(question).get(\"route\") == \"LEAD_GENERATION\""` | — |
| [SRC-1AE03B9EC3-L001166](../../agents/web_agent.py#L1166) | 1166 | `""` | — |
| [SRC-1AE03B9EC3-L001167](../../agents/web_agent.py#L1167) | 1167 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L001168](../../agents/web_agent.py#L1168) | 1168 | `"    def _lead_entity_categories(value: str) -> set[str]:"` | — |
| [SRC-1AE03B9EC3-L001169](../../agents/web_agent.py#L1169) | 1169 | `"        \"\"\"Classify explicit property and vehicle terms for conservative lead isolation.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001170](../../agents/web_agent.py#L1170) | 1170 | `"        normalized = _normalize_search_query(value).casefold()"` | — |
| [SRC-1AE03B9EC3-L001171](../../agents/web_agent.py#L1171) | 1171 | `"        property_terms = ("` | — |
| [SRC-1AE03B9EC3-L001172](../../agents/web_agent.py#L1172) | 1172 | `"            \"شقه\", \"شقق\", \"عقار\", \"عقارات\", \"فيلا\", \"فلل\","` | — |
| [SRC-1AE03B9EC3-L001173](../../agents/web_agent.py#L1173) | 1173 | `"            \"وحده سكنيه\", \"وحدات سكنيه\", \"apartment\", \"apartments\","` | — |
| [SRC-1AE03B9EC3-L001174](../../agents/web_agent.py#L1174) | 1174 | `"            \"flat\", \"flats\", \"property\", \"properties\", \"house\", \"houses\","` | — |
| [SRC-1AE03B9EC3-L001175](../../agents/web_agent.py#L1175) | 1175 | `"            \"villa\", \"villas\", \"real estate\","` | — |
| [SRC-1AE03B9EC3-L001176](../../agents/web_agent.py#L1176) | 1176 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001177](../../agents/web_agent.py#L1177) | 1177 | `"        vehicle_terms = ("` | — |
| [SRC-1AE03B9EC3-L001178](../../agents/web_agent.py#L1178) | 1178 | `"            \"سياره\", \"سيارات\", \"عربيه\", \"عربيات\", \"مركبه\", \"مركبات\","` | — |
| [SRC-1AE03B9EC3-L001179](../../agents/web_agent.py#L1179) | 1179 | `"            \"car\", \"cars\", \"vehicle\", \"vehicles\", \"automobile\", \"automobiles\","` | — |
| [SRC-1AE03B9EC3-L001180](../../agents/web_agent.py#L1180) | 1180 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001181](../../agents/web_agent.py#L1181) | 1181 | `""` | — |
| [SRC-1AE03B9EC3-L001182](../../agents/web_agent.py#L1182) | 1182 | `"        def contains(term: str) -> bool:"` | — |
| [SRC-1AE03B9EC3-L001183](../../agents/web_agent.py#L1183) | 1183 | `"            normalized_term = _normalize_search_query(term).casefold()"` | — |
| [SRC-1AE03B9EC3-L001184](../../agents/web_agent.py#L1184) | 1184 | `"            if re.search(r\"[a-z]\", normalized_term):"` | — |
| [SRC-1AE03B9EC3-L001185](../../agents/web_agent.py#L1185) | 1185 | `"                return bool(re.search("` | — |
| [SRC-1AE03B9EC3-L001186](../../agents/web_agent.py#L1186) | 1186 | `"                    r\"(?<![a-z0-9])\" + re.escape(normalized_term) + r\"(?![a-z0-9])\","` | — |
| [SRC-1AE03B9EC3-L001187](../../agents/web_agent.py#L1187) | 1187 | `"                    normalized,"` | — |
| [SRC-1AE03B9EC3-L001188](../../agents/web_agent.py#L1188) | 1188 | `"                ))"` | — |
| [SRC-1AE03B9EC3-L001189](../../agents/web_agent.py#L1189) | 1189 | `"            return normalized_term in normalized"` | — |
| [SRC-1AE03B9EC3-L001190](../../agents/web_agent.py#L1190) | 1190 | `""` | — |
| [SRC-1AE03B9EC3-L001191](../../agents/web_agent.py#L1191) | 1191 | `"        categories: set[str] = set()"` | — |
| [SRC-1AE03B9EC3-L001192](../../agents/web_agent.py#L1192) | 1192 | `"        if any(contains(term) for term in property_terms):"` | — |
| [SRC-1AE03B9EC3-L001193](../../agents/web_agent.py#L1193) | 1193 | `"            categories.add(\"property\")"` | — |
| [SRC-1AE03B9EC3-L001194](../../agents/web_agent.py#L1194) | 1194 | `"        if any(contains(term) for term in vehicle_terms):"` | — |
| [SRC-1AE03B9EC3-L001195](../../agents/web_agent.py#L1195) | 1195 | `"            categories.add(\"vehicle\")"` | — |
| [SRC-1AE03B9EC3-L001196](../../agents/web_agent.py#L1196) | 1196 | `"        return categories"` | — |
| [SRC-1AE03B9EC3-L001197](../../agents/web_agent.py#L1197) | 1197 | `""` | — |
| [SRC-1AE03B9EC3-L001198](../../agents/web_agent.py#L1198) | 1198 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L001199](../../agents/web_agent.py#L1199) | 1199 | `"    def _lead_intent_evidence("` | — |
| [SRC-1AE03B9EC3-L001200](../../agents/web_agent.py#L1200) | 1200 | `"        source: dict[str, Any], question: str \| None = None"` | — |
| [SRC-1AE03B9EC3-L001201](../../agents/web_agent.py#L1201) | 1201 | `"    ) -> dict[str, str] \| None:"` | — |
| [SRC-1AE03B9EC3-L001202](../../agents/web_agent.py#L1202) | 1202 | `"        \"\"\"Extract explicit public demand type without inferring identity or product fit.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001203](../../agents/web_agent.py#L1203) | 1203 | `"        evidence_fields = ("` | — |
| [SRC-1AE03B9EC3-L001204](../../agents/web_agent.py#L1204) | 1204 | `"            (\"page_text\", \"page_text\"),"` | — |
| [SRC-1AE03B9EC3-L001205](../../agents/web_agent.py#L1205) | 1205 | `"            (\"title\", \"title\"),"` | — |
| [SRC-1AE03B9EC3-L001206](../../agents/web_agent.py#L1206) | 1206 | `"            (\"snippet\", \"search_snippet\"),"` | — |
| [SRC-1AE03B9EC3-L001207](../../agents/web_agent.py#L1207) | 1207 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001208](../../agents/web_agent.py#L1208) | 1208 | `"        combined_text = \" \".join("` | — |
| [SRC-1AE03B9EC3-L001209](../../agents/web_agent.py#L1209) | 1209 | `"            str(source.get(field) or \"\") for field, _basis in evidence_fields"` | — |
| [SRC-1AE03B9EC3-L001210](../../agents/web_agent.py#L1210) | 1210 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001211](../../agents/web_agent.py#L1211) | 1211 | `"        requested_categories = WebAgent._lead_entity_categories(question or \"\")"` | — |
| [SRC-1AE03B9EC3-L001212](../../agents/web_agent.py#L1212) | 1212 | `"        observed_categories = WebAgent._lead_entity_categories(combined_text)"` | — |
| [SRC-1AE03B9EC3-L001213](../../agents/web_agent.py#L1213) | 1213 | `"        if ("` | — |
| [SRC-1AE03B9EC3-L001214](../../agents/web_agent.py#L1214) | 1214 | `"            len(requested_categories) == 1"` | — |
| [SRC-1AE03B9EC3-L001215](../../agents/web_agent.py#L1215) | 1215 | `"            and requested_categories.isdisjoint(observed_categories)"` | — |
| [SRC-1AE03B9EC3-L001216](../../agents/web_agent.py#L1216) | 1216 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L001217](../../agents/web_agent.py#L1217) | 1217 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L001218](../../agents/web_agent.py#L1218) | 1218 | `""` | — |
| [SRC-1AE03B9EC3-L001219](../../agents/web_agent.py#L1219) | 1219 | `"        signal_phrases = ("` | — |
| [SRC-1AE03B9EC3-L001220](../../agents/web_agent.py#L1220) | 1220 | `"            ("` | — |
| [SRC-1AE03B9EC3-L001221](../../agents/web_agent.py#L1221) | 1221 | `"                \"direct_purchase_request\","` | — |
| [SRC-1AE03B9EC3-L001222](../../agents/web_agent.py#L1222) | 1222 | `"                ("` | — |
| [SRC-1AE03B9EC3-L001223](../../agents/web_agent.py#L1223) | 1223 | `"                    \"مطلوب شقه تمليك\", \"مطلوب شقه للشراء\", \"مطلوب شراء شقه\","` | — |
| [SRC-1AE03B9EC3-L001224](../../agents/web_agent.py#L1224) | 1224 | `"                    \"مطلوب عقار للشراء\", \"مطلوب فيلا للشراء\","` | — |
| [SRC-1AE03B9EC3-L001225](../../agents/web_agent.py#L1225) | 1225 | `"                    \"بدور على شقه تمليك\", \"بدور على شقه للشراء\","` | — |
| [SRC-1AE03B9EC3-L001226](../../agents/web_agent.py#L1226) | 1226 | `"                    \"ابحث عن شقه للشراء\", \"عايز اشتري شقه\", \"عاوز اشتري شقه\","` | — |
| [SRC-1AE03B9EC3-L001227](../../agents/web_agent.py#L1227) | 1227 | `"                    \"عايز اشتري عقار\", \"عاوز اشتري عقار\", \"اريد شراء شقه\","` | — |
| [SRC-1AE03B9EC3-L001228](../../agents/web_agent.py#L1228) | 1228 | `"                    \"ارغب في شراء شقه\", \"اريد شراء عقار\", \"ارغب في شراء عقار\","` | — |
| [SRC-1AE03B9EC3-L001229](../../agents/web_agent.py#L1229) | 1229 | `"                    \"مطلوب شراء\", \"عايز اشتري\", \"عاوز اشتري\", \"اريد شراء\","` | — |
| [SRC-1AE03B9EC3-L001230](../../agents/web_agent.py#L1230) | 1230 | `"                    \"ارغب في شراء\", \"نرغب في شراء\", \"نرغب بشراء\", \"محتاج اشتري\","` | — |
| [SRC-1AE03B9EC3-L001231](../../agents/web_agent.py#L1231) | 1231 | `"                    \"looking to buy\", \"looking to purchase\", \"want to buy\","` | — |
| [SRC-1AE03B9EC3-L001232](../../agents/web_agent.py#L1232) | 1232 | `"                    \"wants to buy\", \"want to purchase\", \"wants to purchase\","` | — |
| [SRC-1AE03B9EC3-L001233](../../agents/web_agent.py#L1233) | 1233 | `"                    \"seeking to buy\", \"seeking to purchase\", \"interested in buying\","` | — |
| [SRC-1AE03B9EC3-L001234](../../agents/web_agent.py#L1234) | 1234 | `"                    \"interested in purchasing\", \"buyer looking to buy\","` | — |
| [SRC-1AE03B9EC3-L001235](../../agents/web_agent.py#L1235) | 1235 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L001236](../../agents/web_agent.py#L1236) | 1236 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L001237](../../agents/web_agent.py#L1237) | 1237 | `"            ("` | — |
| [SRC-1AE03B9EC3-L001238](../../agents/web_agent.py#L1238) | 1238 | `"                \"request_for_quotation\","` | — |
| [SRC-1AE03B9EC3-L001239](../../agents/web_agent.py#L1239) | 1239 | `"                ("` | — |
| [SRC-1AE03B9EC3-L001240](../../agents/web_agent.py#L1240) | 1240 | `"                    \"طلب عرض سعر\", \"مطلوب عرض سعر\", \"اطلب عرض سعر\","` | — |
| [SRC-1AE03B9EC3-L001241](../../agents/web_agent.py#L1241) | 1241 | `"                    \"request for quotation\", \"request a quote\","` | — |
| [SRC-1AE03B9EC3-L001242](../../agents/web_agent.py#L1242) | 1242 | `"                    \"request for quote\", \"seeking quotations\","` | — |
| [SRC-1AE03B9EC3-L001243](../../agents/web_agent.py#L1243) | 1243 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L001244](../../agents/web_agent.py#L1244) | 1244 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L001245](../../agents/web_agent.py#L1245) | 1245 | `"            ("` | — |
| [SRC-1AE03B9EC3-L001246](../../agents/web_agent.py#L1246) | 1246 | `"                \"stated_need\","` | — |
| [SRC-1AE03B9EC3-L001247](../../agents/web_agent.py#L1247) | 1247 | `"                ("` | — |
| [SRC-1AE03B9EC3-L001248](../../agents/web_agent.py#L1248) | 1248 | `"                    \"بدور على\", \"ابحث عن\", \"أبحث عن\", \"محتاج\", \"محتاجين\","` | — |
| [SRC-1AE03B9EC3-L001249](../../agents/web_agent.py#L1249) | 1249 | `"                    \"looking for\", \"in need of\", \"need a supplier\","` | — |
| [SRC-1AE03B9EC3-L001250](../../agents/web_agent.py#L1250) | 1250 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L001251](../../agents/web_agent.py#L1251) | 1251 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L001252](../../agents/web_agent.py#L1252) | 1252 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001253](../../agents/web_agent.py#L1253) | 1253 | `"        negations = ("` | — |
| [SRC-1AE03B9EC3-L001254](../../agents/web_agent.py#L1254) | 1254 | `"            \"not looking to buy\", \"not interested in buying\","` | — |
| [SRC-1AE03B9EC3-L001255](../../agents/web_agent.py#L1255) | 1255 | `"            \"not interested in purchasing\", \"no longer looking to buy\","` | — |
| [SRC-1AE03B9EC3-L001256](../../agents/web_agent.py#L1256) | 1256 | `"            \"do not want to buy\", \"don't want to buy\","` | — |
| [SRC-1AE03B9EC3-L001257](../../agents/web_agent.py#L1257) | 1257 | `"            \"looking for a buyer\", \"looking for buyers\", \"seeking a buyer\","` | — |
| [SRC-1AE03B9EC3-L001258](../../agents/web_agent.py#L1258) | 1258 | `"            \"need a buyer\", \"buyer wanted\", \"buyers wanted\","` | — |
| [SRC-1AE03B9EC3-L001259](../../agents/web_agent.py#L1259) | 1259 | `"            \"نبحث عن مشتري\", \"نبحث عن مشترين\", \"ابحث عن مشتري\","` | — |
| [SRC-1AE03B9EC3-L001260](../../agents/web_agent.py#L1260) | 1260 | `"            \"مطلوب مشتري\", \"مطلوب مشترين\", \"نبحث عن عميل\", \"نبحث عن عملاء\","` | — |
| [SRC-1AE03B9EC3-L001261](../../agents/web_agent.py#L1261) | 1261 | `"            \"مش بدور على\", \"مش عايز اشتري\", \"مش عاوز اشتري\","` | — |
| [SRC-1AE03B9EC3-L001262](../../agents/web_agent.py#L1262) | 1262 | `"            \"لا اريد شراء\", \"لا ارغب في شراء\", \"مش محتاج اشتري\","` | — |
| [SRC-1AE03B9EC3-L001263](../../agents/web_agent.py#L1263) | 1263 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001264](../../agents/web_agent.py#L1264) | 1264 | `"        for field, basis in evidence_fields:"` | — |
| [SRC-1AE03B9EC3-L001265](../../agents/web_agent.py#L1265) | 1265 | `"            raw = source.get(field)"` | — |
| [SRC-1AE03B9EC3-L001266](../../agents/web_agent.py#L1266) | 1266 | `"            if not isinstance(raw, str) or not raw.strip():"` | — |
| [SRC-1AE03B9EC3-L001267](../../agents/web_agent.py#L1267) | 1267 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001268](../../agents/web_agent.py#L1268) | 1268 | `"            normalized = _normalize_search_query(raw).casefold()"` | — |
| [SRC-1AE03B9EC3-L001269](../../agents/web_agent.py#L1269) | 1269 | `"            if any(_normalize_search_query(term).casefold() in normalized for term in negations):"` | — |
| [SRC-1AE03B9EC3-L001270](../../agents/web_agent.py#L1270) | 1270 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001271](../../agents/web_agent.py#L1271) | 1271 | `"            for signal_type, phrases in signal_phrases:"` | — |
| [SRC-1AE03B9EC3-L001272](../../agents/web_agent.py#L1272) | 1272 | `"                for phrase in phrases:"` | — |
| [SRC-1AE03B9EC3-L001273](../../agents/web_agent.py#L1273) | 1273 | `"                    needle = _normalize_search_query(phrase).casefold()"` | — |
| [SRC-1AE03B9EC3-L001274](../../agents/web_agent.py#L1274) | 1274 | `"                    if needle and needle in normalized:"` | — |
| [SRC-1AE03B9EC3-L001275](../../agents/web_agent.py#L1275) | 1275 | `"                        return {"` | — |
| [SRC-1AE03B9EC3-L001276](../../agents/web_agent.py#L1276) | 1276 | `"                            \"phrase\": phrase,"` | — |
| [SRC-1AE03B9EC3-L001277](../../agents/web_agent.py#L1277) | 1277 | `"                            \"basis\": basis,"` | — |
| [SRC-1AE03B9EC3-L001278](../../agents/web_agent.py#L1278) | 1278 | `"                            \"signal_type\": signal_type,"` | — |
| [SRC-1AE03B9EC3-L001279](../../agents/web_agent.py#L1279) | 1279 | `"                            \"product_fit\": \"unassessed\","` | — |
| [SRC-1AE03B9EC3-L001280](../../agents/web_agent.py#L1280) | 1280 | `"                        }"` | — |
| [SRC-1AE03B9EC3-L001281](../../agents/web_agent.py#L1281) | 1281 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L001282](../../agents/web_agent.py#L1282) | 1282 | `""` | — |
| [SRC-1AE03B9EC3-L001283](../../agents/web_agent.py#L1283) | 1283 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L001284](../../agents/web_agent.py#L1284) | 1284 | `"    def _lead_generation_queries("` | — |
| [SRC-1AE03B9EC3-L001285](../../agents/web_agent.py#L1285) | 1285 | `"        question: str, existing_queries: list[str] \| None = None"` | — |
| [SRC-1AE03B9EC3-L001286](../../agents/web_agent.py#L1286) | 1286 | `"    ) -> list[str]:"` | — |
