# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **004**
- سجلات الأسطر: **800**
- النطاق: SRC-59CF4B7DE8-L000708 إلى SRC-1AE03B9EC3-L000644
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-59CF4B7DE8 — [agents/research.py](../../agents/research.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-59CF4B7DE8-L000708](../../agents/research.py#L708) | 708 | `"            warnings.append(\"لا تتوفر تواريخ نشر قابلة للتحليل؛ حداثة النتائج غير مؤكدة.\")"` | — |
| [SRC-59CF4B7DE8-L000709](../../agents/research.py#L709) | 709 | `"        elif recent_count == 0:"` | — |
| [SRC-59CF4B7DE8-L000710](../../agents/research.py#L710) | 710 | `"            warnings.append(f\"لم يُعثر على مصدر مؤرخ خلال آخر {recent_days} يومًا ضمن التواريخ القابلة للتحليل.\")"` | — |
| [SRC-59CF4B7DE8-L000711](../../agents/research.py#L711) | 711 | `"    if future_dates:"` | — |
| [SRC-59CF4B7DE8-L000712](../../agents/research.py#L712) | 712 | `"        warnings.append(\"توجد تواريخ مستقبلية غير متوقعة؛ يجب مراجعتها يدويًا.\")"` | — |
| [SRC-59CF4B7DE8-L000713](../../agents/research.py#L713) | 713 | `"    if social_count and primary_count == 0:"` | — |
| [SRC-59CF4B7DE8-L000714](../../agents/research.py#L714) | 714 | `"        warnings.append(\"المصادر اجتماعية فقط دون مصدر رسمي/أكاديمي؛ تعامل معها كآراء أو إشارات لا كحقائق مثبتة.\")"` | — |
| [SRC-59CF4B7DE8-L000715](../../agents/research.py#L715) | 715 | `"    return {"` | — |
| [SRC-59CF4B7DE8-L000716](../../agents/research.py#L716) | 716 | `"        \"unique_sources\": unique_sources,"` | — |
| [SRC-59CF4B7DE8-L000717](../../agents/research.py#L717) | 717 | `"        \"unique_domains\": len(domains),"` | — |
| [SRC-59CF4B7DE8-L000718](../../agents/research.py#L718) | 718 | `"        \"providers_count\": len(providers),"` | — |
| [SRC-59CF4B7DE8-L000719](../../agents/research.py#L719) | 719 | `"        \"providers\": sorted(providers),"` | — |
| [SRC-59CF4B7DE8-L000720](../../agents/research.py#L720) | 720 | `"        \"pages_read\": pages_read,"` | — |
| [SRC-59CF4B7DE8-L000721](../../agents/research.py#L721) | 721 | `"        \"primary_sources\": primary_count,"` | — |
| [SRC-59CF4B7DE8-L000722](../../agents/research.py#L722) | 722 | `"        \"news_sources\": news_count,"` | — |
| [SRC-59CF4B7DE8-L000723](../../agents/research.py#L723) | 723 | `"        \"social_sources\": social_count,"` | — |
| [SRC-59CF4B7DE8-L000724](../../agents/research.py#L724) | 724 | `"        \"dated_sources\": len(dates),"` | — |
| [SRC-59CF4B7DE8-L000725](../../agents/research.py#L725) | 725 | `"        \"recent_sources\": recent_count,"` | — |
| [SRC-59CF4B7DE8-L000726](../../agents/research.py#L726) | 726 | `"        \"undated_sources\": max(0, unique_sources - len(dates)),"` | — |
| [SRC-59CF4B7DE8-L000727](../../agents/research.py#L727) | 727 | `"        \"date_coverage_percent\": round(100 * len(dates) / unique_sources) if unique_sources else 0,"` | — |
| [SRC-59CF4B7DE8-L000728](../../agents/research.py#L728) | 728 | `"        \"coverage_score\": coverage_score,"` | — |
| [SRC-59CF4B7DE8-L000729](../../agents/research.py#L729) | 729 | `"        \"coverage_level\": coverage_level,"` | — |
| [SRC-59CF4B7DE8-L000730](../../agents/research.py#L730) | 730 | `"        \"score_meaning\": \"مؤشر تغطية وتنوع الأدلة، وليس احتمال صحة الإجابة.\","` | — |
| [SRC-59CF4B7DE8-L000731](../../agents/research.py#L731) | 731 | `"        \"warnings\": warnings,"` | — |
| [SRC-59CF4B7DE8-L000732](../../agents/research.py#L732) | 732 | `"    }"` | — |
| [SRC-59CF4B7DE8-L000733](../../agents/research.py#L733) | 733 | `""` | — |
| [SRC-59CF4B7DE8-L000734](../../agents/research.py#L734) | 734 | `""` | — |
| [SRC-59CF4B7DE8-L000735](../../agents/research.py#L735) | 735 | `""` | — |
| [SRC-59CF4B7DE8-L000736](../../agents/research.py#L736) | 736 | `"# ---------------------------------------------------------------------------"` | — |
| [SRC-59CF4B7DE8-L000737](../../agents/research.py#L737) | 737 | `"# Evidence-aware helpers"` | — |
| [SRC-59CF4B7DE8-L000738](../../agents/research.py#L738) | 738 | `"# ---------------------------------------------------------------------------"` | — |
| [SRC-59CF4B7DE8-L000739](../../agents/research.py#L739) | 739 | `""` | — |
| [SRC-59CF4B7DE8-L000740](../../agents/research.py#L740) | 740 | `"_RELEVANCE_STOPWORDS = {"` | — |
| [SRC-59CF4B7DE8-L000741](../../agents/research.py#L741) | 741 | `"    \"the\", \"a\", \"an\", \"of\", \"in\", \"on\", \"at\", \"to\", \"for\","` | — |
| [SRC-59CF4B7DE8-L000742](../../agents/research.py#L742) | 742 | `"    \"is\", \"are\", \"was\", \"were\", \"be\", \"been\", \"being\","` | — |
| [SRC-59CF4B7DE8-L000743](../../agents/research.py#L743) | 743 | `"    \"and\", \"or\", \"but\", \"not\", \"with\", \"without\","` | — |
| [SRC-59CF4B7DE8-L000744](../../agents/research.py#L744) | 744 | `"    \"this\", \"that\", \"these\", \"those\", \"it\", \"its\","` | — |
| [SRC-59CF4B7DE8-L000745](../../agents/research.py#L745) | 745 | `"}"` | — |
| [SRC-59CF4B7DE8-L000746](../../agents/research.py#L746) | 746 | `""` | — |
| [SRC-59CF4B7DE8-L000747](../../agents/research.py#L747) | 747 | `"_OFFICIAL_CLASSES = {\"government\", \"education\", \"official\"}"` | — |
| [SRC-59CF4B7DE8-L000748](../../agents/research.py#L748) | 748 | `""` | — |
| [SRC-59CF4B7DE8-L000749](../../agents/research.py#L749) | 749 | `""` | — |
| [SRC-59CF4B7DE8-L000750](../../agents/research.py#L750) | 750 | `"def _tokenize(text: str) -> set:"` | — |
| [SRC-59CF4B7DE8-L000751](../../agents/research.py#L751) | 751 | `"    if not text:"` | — |
| [SRC-59CF4B7DE8-L000752](../../agents/research.py#L752) | 752 | `"        return set()"` | — |
| [SRC-59CF4B7DE8-L000753](../../agents/research.py#L753) | 753 | `"    norm = _normalize_arabic(text.casefold())"` | — |
| [SRC-59CF4B7DE8-L000754](../../agents/research.py#L754) | 754 | `"    tokens = re.findall(r\"\\w+\", norm, flags=re.UNICODE)"` | — |
| [SRC-59CF4B7DE8-L000755](../../agents/research.py#L755) | 755 | `"    return {t for t in tokens if len(t) >= 3 and t not in _RELEVANCE_STOPWORDS}"` | — |
| [SRC-59CF4B7DE8-L000756](../../agents/research.py#L756) | 756 | `""` | — |
| [SRC-59CF4B7DE8-L000757](../../agents/research.py#L757) | 757 | `""` | — |
| [SRC-59CF4B7DE8-L000758](../../agents/research.py#L758) | 758 | `"def source_relevance_score(src, query: str) -> dict:"` | — |
| [SRC-59CF4B7DE8-L000759](../../agents/research.py#L759) | 759 | `"    if not isinstance(src, dict):"` | — |
| [SRC-59CF4B7DE8-L000760](../../agents/research.py#L760) | 760 | `"        return {\"accepted\": False, \"score\": 0, \"reason\": \"malformed\"}"` | — |
| [SRC-59CF4B7DE8-L000761](../../agents/research.py#L761) | 761 | `""` | — |
| [SRC-59CF4B7DE8-L000762](../../agents/research.py#L762) | 762 | `"    title = str(src.get(\"title\") or \"\")"` | — |
| [SRC-59CF4B7DE8-L000763](../../agents/research.py#L763) | 763 | `"    snippet = str(src.get(\"snippet\") or \"\")"` | — |
| [SRC-59CF4B7DE8-L000764](../../agents/research.py#L764) | 764 | `"    page_text = str(src.get(\"page_text\") or \"\")"` | — |
| [SRC-59CF4B7DE8-L000765](../../agents/research.py#L765) | 765 | `"    source_class = str(src.get(\"source_class\") or \"general\").lower()"` | — |
| [SRC-59CF4B7DE8-L000766](../../agents/research.py#L766) | 766 | `""` | — |
| [SRC-59CF4B7DE8-L000767](../../agents/research.py#L767) | 767 | `"    q_tokens = _tokenize(query)"` | — |
| [SRC-59CF4B7DE8-L000768](../../agents/research.py#L768) | 768 | `"    if not q_tokens:"` | — |
| [SRC-59CF4B7DE8-L000769](../../agents/research.py#L769) | 769 | `"        return {\"accepted\": False, \"score\": 0, \"reason\": \"no_query_tokens\"}"` | — |
| [SRC-59CF4B7DE8-L000770](../../agents/research.py#L770) | 770 | `""` | — |
| [SRC-59CF4B7DE8-L000771](../../agents/research.py#L771) | 771 | `"    t_tokens = _tokenize(title)"` | — |
| [SRC-59CF4B7DE8-L000772](../../agents/research.py#L772) | 772 | `"    s_tokens = _tokenize(snippet)"` | — |
| [SRC-59CF4B7DE8-L000773](../../agents/research.py#L773) | 773 | `"    p_tokens = _tokenize(page_text[:3000])"` | — |
| [SRC-59CF4B7DE8-L000774](../../agents/research.py#L774) | 774 | `""` | — |
| [SRC-59CF4B7DE8-L000775](../../agents/research.py#L775) | 775 | `"    title_ratio = len(q_tokens & t_tokens) / max(len(q_tokens), 1)"` | — |
| [SRC-59CF4B7DE8-L000776](../../agents/research.py#L776) | 776 | `"    snippet_ratio = len(q_tokens & s_tokens) / max(len(q_tokens), 1)"` | — |
| [SRC-59CF4B7DE8-L000777](../../agents/research.py#L777) | 777 | `"    page_ratio = len(q_tokens & p_tokens) / max(len(q_tokens), 1)"` | — |
| [SRC-59CF4B7DE8-L000778](../../agents/research.py#L778) | 778 | `""` | — |
| [SRC-59CF4B7DE8-L000779](../../agents/research.py#L779) | 779 | `"    score = int(title_ratio * 15 + snippet_ratio * 20 + page_ratio * 5)"` | — |
| [SRC-59CF4B7DE8-L000780](../../agents/research.py#L780) | 780 | `""` | — |
| [SRC-59CF4B7DE8-L000781](../../agents/research.py#L781) | 781 | `"    if source_class in _OFFICIAL_CLASSES:"` | — |
| [SRC-59CF4B7DE8-L000782](../../agents/research.py#L782) | 782 | `"        if score >= 5:"` | — |
| [SRC-59CF4B7DE8-L000783](../../agents/research.py#L783) | 783 | `"            return {\"accepted\": True, \"score\": score, \"reason\": \"accepted\"}"` | — |
| [SRC-59CF4B7DE8-L000784](../../agents/research.py#L784) | 784 | `"        return {\"accepted\": True, \"score\": score,"` | — |
| [SRC-59CF4B7DE8-L000785](../../agents/research.py#L785) | 785 | `"                \"reason\": \"kept_official_despite_low_overlap\"}"` | — |
| [SRC-59CF4B7DE8-L000786](../../agents/research.py#L786) | 786 | `""` | — |
| [SRC-59CF4B7DE8-L000787](../../agents/research.py#L787) | 787 | `"    if score >= 18:"` | — |
| [SRC-59CF4B7DE8-L000788](../../agents/research.py#L788) | 788 | `"        return {\"accepted\": True, \"score\": score, \"reason\": \"accepted\"}"` | — |
| [SRC-59CF4B7DE8-L000789](../../agents/research.py#L789) | 789 | `"    return {\"accepted\": False, \"score\": score, \"reason\": \"low_overlap\"}"` | — |
| [SRC-59CF4B7DE8-L000790](../../agents/research.py#L790) | 790 | `""` | — |
| [SRC-59CF4B7DE8-L000791](../../agents/research.py#L791) | 791 | `""` | — |
| [SRC-59CF4B7DE8-L000792](../../agents/research.py#L792) | 792 | `"def filter_relevant_sources(sources, query: str, extra_queries=None):"` | — |
| [SRC-59CF4B7DE8-L000793](../../agents/research.py#L793) | 793 | `"    kept = []"` | — |
| [SRC-59CF4B7DE8-L000794](../../agents/research.py#L794) | 794 | `"    diag = []"` | — |
| [SRC-59CF4B7DE8-L000795](../../agents/research.py#L795) | 795 | `"    seen_urls = set()"` | — |
| [SRC-59CF4B7DE8-L000796](../../agents/research.py#L796) | 796 | `"    seen_titles = set()"` | — |
| [SRC-59CF4B7DE8-L000797](../../agents/research.py#L797) | 797 | `"    combined = \" \".join([query] + list(extra_queries or []))"` | — |
| [SRC-59CF4B7DE8-L000798](../../agents/research.py#L798) | 798 | `""` | — |
| [SRC-59CF4B7DE8-L000799](../../agents/research.py#L799) | 799 | `"    for src in sources or []:"` | — |
| [SRC-59CF4B7DE8-L000800](../../agents/research.py#L800) | 800 | `"        if not isinstance(src, dict):"` | — |
| [SRC-59CF4B7DE8-L000801](../../agents/research.py#L801) | 801 | `"            diag.append({\"reason\": \"malformed\", \"url\": \"\"})"` | — |
| [SRC-59CF4B7DE8-L000802](../../agents/research.py#L802) | 802 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000803](../../agents/research.py#L803) | 803 | `"        url = str(src.get(\"url\") or \"\")"` | — |
| [SRC-59CF4B7DE8-L000804](../../agents/research.py#L804) | 804 | `"        domain = str(src.get(\"domain\") or \"\").lower()"` | — |
| [SRC-59CF4B7DE8-L000805](../../agents/research.py#L805) | 805 | `"        title = str(src.get(\"title\") or \"\").strip()"` | — |
| [SRC-59CF4B7DE8-L000806](../../agents/research.py#L806) | 806 | `"        url_key = url.rstrip(\"/\").lower()"` | — |
| [SRC-59CF4B7DE8-L000807](../../agents/research.py#L807) | 807 | `"        title_key = title.lower() + \"\|\" + domain"` | — |
| [SRC-59CF4B7DE8-L000808](../../agents/research.py#L808) | 808 | `""` | — |
| [SRC-59CF4B7DE8-L000809](../../agents/research.py#L809) | 809 | `"        if url_key and url_key in seen_urls:"` | — |
| [SRC-59CF4B7DE8-L000810](../../agents/research.py#L810) | 810 | `"            diag.append({\"reason\": \"duplicate_url\", \"url\": url})"` | — |
| [SRC-59CF4B7DE8-L000811](../../agents/research.py#L811) | 811 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000812](../../agents/research.py#L812) | 812 | `"        if title and title_key in seen_titles:"` | — |
| [SRC-59CF4B7DE8-L000813](../../agents/research.py#L813) | 813 | `"            diag.append({\"reason\": \"duplicate_title_domain\", \"url\": url})"` | — |
| [SRC-59CF4B7DE8-L000814](../../agents/research.py#L814) | 814 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000815](../../agents/research.py#L815) | 815 | `""` | — |
| [SRC-59CF4B7DE8-L000816](../../agents/research.py#L816) | 816 | `"        rel = source_relevance_score(src, combined)"` | — |
| [SRC-59CF4B7DE8-L000817](../../agents/research.py#L817) | 817 | `"        if not rel[\"accepted\"]:"` | — |
| [SRC-59CF4B7DE8-L000818](../../agents/research.py#L818) | 818 | `"            diag.append({\"reason\": rel[\"reason\"], \"url\": url, \"score\": rel[\"score\"]})"` | — |
| [SRC-59CF4B7DE8-L000819](../../agents/research.py#L819) | 819 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000820](../../agents/research.py#L820) | 820 | `""` | — |
| [SRC-59CF4B7DE8-L000821](../../agents/research.py#L821) | 821 | `"        kept.append(src)"` | — |
| [SRC-59CF4B7DE8-L000822](../../agents/research.py#L822) | 822 | `"        if url_key:"` | — |
| [SRC-59CF4B7DE8-L000823](../../agents/research.py#L823) | 823 | `"            seen_urls.add(url_key)"` | — |
| [SRC-59CF4B7DE8-L000824](../../agents/research.py#L824) | 824 | `"        if title:"` | — |
| [SRC-59CF4B7DE8-L000825](../../agents/research.py#L825) | 825 | `"            seen_titles.add(title_key)"` | — |
| [SRC-59CF4B7DE8-L000826](../../agents/research.py#L826) | 826 | `"    return kept, diag"` | — |
| [SRC-59CF4B7DE8-L000827](../../agents/research.py#L827) | 827 | `""` | — |
| [SRC-59CF4B7DE8-L000828](../../agents/research.py#L828) | 828 | `""` | — |
| [SRC-59CF4B7DE8-L000829](../../agents/research.py#L829) | 829 | `"def decide_evidence_status(sources, pages_read: int = 0,"` | — |
| [SRC-59CF4B7DE8-L000830](../../agents/research.py#L830) | 830 | `"                           provider_failures: int = 0,"` | — |
| [SRC-59CF4B7DE8-L000831](../../agents/research.py#L831) | 831 | `"                           search_attempted: bool = True) -> dict:"` | — |
| [SRC-59CF4B7DE8-L000832](../../agents/research.py#L832) | 832 | `"    if not search_attempted:"` | — |
| [SRC-59CF4B7DE8-L000833](../../agents/research.py#L833) | 833 | `"        return {\"evidence_status\": \"failed\", \"should_abstain\": True}"` | — |
| [SRC-59CF4B7DE8-L000834](../../agents/research.py#L834) | 834 | `""` | — |
| [SRC-59CF4B7DE8-L000835](../../agents/research.py#L835) | 835 | `"    domains = set()"` | — |
| [SRC-59CF4B7DE8-L000836](../../agents/research.py#L836) | 836 | `"    has_official = False"` | — |
| [SRC-59CF4B7DE8-L000837](../../agents/research.py#L837) | 837 | `"    for s in sources or []:"` | — |
| [SRC-59CF4B7DE8-L000838](../../agents/research.py#L838) | 838 | `"        if not isinstance(s, dict):"` | — |
| [SRC-59CF4B7DE8-L000839](../../agents/research.py#L839) | 839 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000840](../../agents/research.py#L840) | 840 | `"        d = str(s.get(\"domain\") or \"\").lower()"` | — |
| [SRC-59CF4B7DE8-L000841](../../agents/research.py#L841) | 841 | `"        if not d:"` | — |
| [SRC-59CF4B7DE8-L000842](../../agents/research.py#L842) | 842 | `"            url = str(s.get(\"url\") or \"\")"` | — |
| [SRC-59CF4B7DE8-L000843](../../agents/research.py#L843) | 843 | `"            if url:"` | — |
| [SRC-59CF4B7DE8-L000844](../../agents/research.py#L844) | 844 | `"                try:"` | — |
| [SRC-59CF4B7DE8-L000845](../../agents/research.py#L845) | 845 | `"                    from urllib.parse import urlparse"` | — |
| [SRC-59CF4B7DE8-L000846](../../agents/research.py#L846) | 846 | `"                    d = urlparse(url).netloc.lower()"` | — |
| [SRC-59CF4B7DE8-L000847](../../agents/research.py#L847) | 847 | `"                except Exception:"` | — |
| [SRC-59CF4B7DE8-L000848](../../agents/research.py#L848) | 848 | `"                    d = \"\""` | — |
| [SRC-59CF4B7DE8-L000849](../../agents/research.py#L849) | 849 | `"        if d:"` | — |
| [SRC-59CF4B7DE8-L000850](../../agents/research.py#L850) | 850 | `"            domains.add(d)"` | — |
| [SRC-59CF4B7DE8-L000851](../../agents/research.py#L851) | 851 | `"        if str(s.get(\"source_class\") or \"\").lower() in _OFFICIAL_CLASSES:"` | — |
| [SRC-59CF4B7DE8-L000852](../../agents/research.py#L852) | 852 | `"            has_official = True"` | — |
| [SRC-59CF4B7DE8-L000853](../../agents/research.py#L853) | 853 | `""` | — |
| [SRC-59CF4B7DE8-L000854](../../agents/research.py#L854) | 854 | `"    if not sources:"` | — |
| [SRC-59CF4B7DE8-L000855](../../agents/research.py#L855) | 855 | `"        if provider_failures > 0:"` | — |
| [SRC-59CF4B7DE8-L000856](../../agents/research.py#L856) | 856 | `"            return {\"evidence_status\": \"failed\", \"should_abstain\": True}"` | — |
| [SRC-59CF4B7DE8-L000857](../../agents/research.py#L857) | 857 | `"        return {\"evidence_status\": \"insufficient\", \"should_abstain\": True}"` | — |
| [SRC-59CF4B7DE8-L000858](../../agents/research.py#L858) | 858 | `""` | — |
| [SRC-59CF4B7DE8-L000859](../../agents/research.py#L859) | 859 | `"    if len(domains) >= 2 or has_official:"` | — |
| [SRC-59CF4B7DE8-L000860](../../agents/research.py#L860) | 860 | `"        return {\"evidence_status\": \"adequate\", \"should_abstain\": False}"` | — |
| [SRC-59CF4B7DE8-L000861](../../agents/research.py#L861) | 861 | `"    if len(domains) >= 1:"` | — |
| [SRC-59CF4B7DE8-L000862](../../agents/research.py#L862) | 862 | `"        return {\"evidence_status\": \"partial\", \"should_abstain\": False}"` | — |
| [SRC-59CF4B7DE8-L000863](../../agents/research.py#L863) | 863 | `"    return {\"evidence_status\": \"insufficient\", \"should_abstain\": True}"` | — |
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
| [SRC-1AE03B9EC3-L000025](../../agents/web_agent.py#L25) | 25 | `"from agents.answer_validation import audit_answer_integrity, build_requirement_evidence_ledger"` | — |
| [SRC-1AE03B9EC3-L000026](../../agents/web_agent.py#L26) | 26 | `"from agents.request_budget import RequestBudget, RequestBudgetExceeded"` | — |
| [SRC-1AE03B9EC3-L000027](../../agents/web_agent.py#L27) | 27 | `"from agents.research import ("` | — |
| [SRC-1AE03B9EC3-L000028](../../agents/web_agent.py#L28) | 28 | `"    MAX_PLAN_QUERIES,"` | — |
| [SRC-1AE03B9EC3-L000029](../../agents/web_agent.py#L29) | 29 | `"    SOCIAL_DOMAINS,"` | — |
| [SRC-1AE03B9EC3-L000030](../../agents/web_agent.py#L30) | 30 | `"    compact_search_query,"` | — |
| [SRC-1AE03B9EC3-L000031](../../agents/web_agent.py#L31) | 31 | `"    evidence_signal_report,"` | — |
| [SRC-1AE03B9EC3-L000032](../../agents/web_agent.py#L32) | 32 | `"    fallback_plan,"` | — |
| [SRC-1AE03B9EC3-L000033](../../agents/web_agent.py#L33) | 33 | `"    fuse_ranked_results,"` | — |
| [SRC-1AE03B9EC3-L000034](../../agents/web_agent.py#L34) | 34 | `"    registrable_domain,"` | — |
| [SRC-1AE03B9EC3-L000035](../../agents/web_agent.py#L35) | 35 | `"    extract_question_coverage_targets,"` | — |
| [SRC-1AE03B9EC3-L000036](../../agents/web_agent.py#L36) | 36 | `"    validate_plan,"` | — |
| [SRC-1AE03B9EC3-L000037](../../agents/web_agent.py#L37) | 37 | `")"` | — |
| [SRC-1AE03B9EC3-L000038](../../agents/web_agent.py#L38) | 38 | `""` | — |
| [SRC-1AE03B9EC3-L000039](../../agents/web_agent.py#L39) | 39 | `"MAX_QUESTION_CHARS = 4000"` | — |
| [SRC-1AE03B9EC3-L000040](../../agents/web_agent.py#L40) | 40 | `"MAX_HISTORY_ITEMS = 8"` | — |
| [SRC-1AE03B9EC3-L000041](../../agents/web_agent.py#L41) | 41 | `"MAX_HISTORY_CHARS = 4000"` | — |
| [SRC-1AE03B9EC3-L000042](../../agents/web_agent.py#L42) | 42 | `"MAX_SEARCH_RESULTS = 18"` | — |
| [SRC-1AE03B9EC3-L000043](../../agents/web_agent.py#L43) | 43 | `"MAX_PROVIDER_RESULTS = 6"` | — |
| [SRC-1AE03B9EC3-L000044](../../agents/web_agent.py#L44) | 44 | `"MAX_FETCHED_PAGES = 8"` | — |
| [SRC-1AE03B9EC3-L000045](../../agents/web_agent.py#L45) | 45 | `"MAX_LLM_CITED_SOURCES = 12"` | — |
| [SRC-1AE03B9EC3-L000046](../../agents/web_agent.py#L46) | 46 | `"MAX_RESEARCH_WORKERS = 8"` | — |
| [SRC-1AE03B9EC3-L000047](../../agents/web_agent.py#L47) | 47 | `"MAX_PAGE_BYTES = 1_000_000"` | — |
| [SRC-1AE03B9EC3-L000048](../../agents/web_agent.py#L48) | 48 | `"MAX_PAGE_TEXT_CHARS = 12_000"` | — |
| [SRC-1AE03B9EC3-L000049](../../agents/web_agent.py#L49) | 49 | `"LLM_TIMEOUT_SECONDS = 35"` | — |
| [SRC-1AE03B9EC3-L000050](../../agents/web_agent.py#L50) | 50 | `""` | — |
| [SRC-1AE03B9EC3-L000051](../../agents/web_agent.py#L51) | 51 | `"# Only completed connector result-processing states positively confirm an attempt."` | — |
| [SRC-1AE03B9EC3-L000052](../../agents/web_agent.py#L52) | 52 | `"# A generic \"failed\" or timeout diagnostic may occur before a network request is sent."` | — |
| [SRC-1AE03B9EC3-L000053](../../agents/web_agent.py#L53) | 53 | `"_SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES = frozenset({\"ok\", \"no_results\", \"filtered_all\"})"` | — |
| [SRC-1AE03B9EC3-L000054](../../agents/web_agent.py#L54) | 54 | `"_RESEARCH_ERROR_OUTCOMES = frozenset({\"attempted_research_error\", \"unknown_after_research_error\"})"` | — |
| [SRC-1AE03B9EC3-L000055](../../agents/web_agent.py#L55) | 55 | `"_PROVIDER_REJECTION_REASONS = ("` | — |
| [SRC-1AE03B9EC3-L000056](../../agents/web_agent.py#L56) | 56 | `"    \"malformed_candidate\","` | — |
| [SRC-1AE03B9EC3-L000057](../../agents/web_agent.py#L57) | 57 | `"    \"invalid_url_or_unsafe_target\","` | — |
| [SRC-1AE03B9EC3-L000058](../../agents/web_agent.py#L58) | 58 | `"    \"blocked_domain\","` | — |
| [SRC-1AE03B9EC3-L000059](../../agents/web_agent.py#L59) | 59 | `"    \"relevance_below_threshold\","` | — |
| [SRC-1AE03B9EC3-L000060](../../agents/web_agent.py#L60) | 60 | `")"` | — |
| [SRC-1AE03B9EC3-L000061](../../agents/web_agent.py#L61) | 61 | `""` | — |
| [SRC-1AE03B9EC3-L000062](../../agents/web_agent.py#L62) | 62 | `""` | — |
| [SRC-1AE03B9EC3-L000063](../../agents/web_agent.py#L63) | 63 | `"_ARABIC_SEARCH_TRANSLATION = str.maketrans({"` | — |
| [SRC-1AE03B9EC3-L000064](../../agents/web_agent.py#L64) | 64 | `"    \"أ\": \"ا\", \"إ\": \"ا\", \"آ\": \"ا\", \"ٱ\": \"ا\", \"ى\": \"ي\","` | — |
| [SRC-1AE03B9EC3-L000065](../../agents/web_agent.py#L65) | 65 | `"    \"ؤ\": \"و\", \"ئ\": \"ي\", \"ة\": \"ه\", \"ـ\": \"\","` | — |
| [SRC-1AE03B9EC3-L000066](../../agents/web_agent.py#L66) | 66 | `"})"` | — |
| [SRC-1AE03B9EC3-L000067](../../agents/web_agent.py#L67) | 67 | `"_ARABIC_DIACRITICS_RE = re.compile(r\"[\\u0610-\\u061A\\u064B-\\u065F\\u0670\\u06D6-\\u06ED]\")"` | — |
| [SRC-1AE03B9EC3-L000068](../../agents/web_agent.py#L68) | 68 | `"_SEARCH_STOPWORDS = frozenset({"` | — |
| [SRC-1AE03B9EC3-L000069](../../agents/web_agent.py#L69) | 69 | `"    \"ما\", \"ماذا\", \"من\", \"في\", \"على\", \"عن\", \"الى\", \"إلى\", \"و\", \"او\", \"أو\","` | — |
| [SRC-1AE03B9EC3-L000070](../../agents/web_agent.py#L70) | 70 | `"    \"هل\", \"هو\", \"هي\", \"هذا\", \"هذه\", \"ذلك\", \"تلك\", \"التي\", \"الذي\", \"مع\","` | — |
| [SRC-1AE03B9EC3-L000071](../../agents/web_agent.py#L71) | 71 | `"    \"بين\", \"كيف\", \"لماذا\", \"كم\", \"كان\", \"كانت\", \"يكون\", \"تكون\", \"لي\","` | — |
| [SRC-1AE03B9EC3-L000072](../../agents/web_agent.py#L72) | 72 | `"    \"the\", \"a\", \"an\", \"and\", \"or\", \"in\", \"on\", \"of\", \"to\", \"for\", \"with\","` | — |
| [SRC-1AE03B9EC3-L000073](../../agents/web_agent.py#L73) | 73 | `"    \"is\", \"are\", \"was\", \"were\", \"what\", \"which\", \"who\", \"how\", \"why\", \"when\","` | — |
| [SRC-1AE03B9EC3-L000074](../../agents/web_agent.py#L74) | 74 | `"    \"where\", \"compare\", \"comparison\", \"please\", \"show\", \"find\", \"latest\","` | — |
| [SRC-1AE03B9EC3-L000075](../../agents/web_agent.py#L75) | 75 | `"    \"news\", \"official\", \"sources\", \"source\", \"reports\", \"report\", \"analysis\","` | — |
| [SRC-1AE03B9EC3-L000076](../../agents/web_agent.py#L76) | 76 | `"    \"site\", \"com\", \"org\", \"net\", \"www\","` | — |
| [SRC-1AE03B9EC3-L000077](../../agents/web_agent.py#L77) | 77 | `"    # Arabic request/format words are not useful topic concepts for matching search snippets."` | — |
| [SRC-1AE03B9EC3-L000078](../../agents/web_agent.py#L78) | 78 | `"    \"اذكر\", \"مصدر\", \"مصادر\", \"موثوق\", \"موثوقة\", \"رابط\", \"روابط\", \"مباشر\","` | — |
| [SRC-1AE03B9EC3-L000079](../../agents/web_agent.py#L79) | 79 | `"    \"مباشرة\", \"اجب\", \"بالعربية\", \"العربية\", \"بايجاز\", \"بالايجاز\", \"ايجاز\","` | — |
| [SRC-1AE03B9EC3-L000080](../../agents/web_agent.py#L80) | 80 | `"    \"باختصار\", \"اختصار\", \"استخدم\", \"اعرض\", \"وضح\", \"حلل\", \"قارن\", \"متعددة\","` | — |
| [SRC-1AE03B9EC3-L000081](../../agents/web_agent.py#L81) | 81 | `"    \"اهم\", \"الحقائق\", \"حقائق\", \"استنتاج\", \"استنتاجات\", \"الاستنتاجات\","` | — |
| [SRC-1AE03B9EC3-L000082](../../agents/web_agent.py#L82) | 82 | `"    \"تواريخ\", \"تاريخ\", \"الاخبار\", \"اخبار\", \"المصادر\", \"معلومات\", \"قديمة\","` | — |
| [SRC-1AE03B9EC3-L000083](../../agents/web_agent.py#L83) | 83 | `"    \"قديمه\", \"جديدة\", \"جديده\", \"خلال\", \"الايام\", \"ايام\", \"السبعة\", \"سبعة\","` | — |
| [SRC-1AE03B9EC3-L000084](../../agents/web_agent.py#L84) | 84 | `"    \"الماضية\", \"ماضية\", \"الاسبوع\", \"حاليا\", \"الان\", \"احدث\", \"ولا\","` | — |
| [SRC-1AE03B9EC3-L000085](../../agents/web_agent.py#L85) | 85 | `"    \"تعرض\", \"باعتبارها\","` | — |
| [SRC-1AE03B9EC3-L000086](../../agents/web_agent.py#L86) | 86 | `"})"` | — |
| [SRC-1AE03B9EC3-L000087](../../agents/web_agent.py#L87) | 87 | `"# Search-expansion modifiers are useful after a real topic, but must not stand in"` | — |
| [SRC-1AE03B9EC3-L000088](../../agents/web_agent.py#L88) | 88 | `"# for a topic if a future planner/expansion path loses its subject."` | — |
| [SRC-1AE03B9EC3-L000089](../../agents/web_agent.py#L89) | 89 | `"_GENERIC_QUERY_MODIFIER_TOKENS = frozenset({"` | — |
| [SRC-1AE03B9EC3-L000090](../../agents/web_agent.py#L90) | 90 | `"    \"risk\", \"risks\", \"limitation\", \"limitations\", \"alternative\", \"alternatives\","` | — |
| [SRC-1AE03B9EC3-L000091](../../agents/web_agent.py#L91) | 91 | `"    \"recent\", \"data\", \"review\", \"reviews\", \"comparison\", \"compare\", \"official\","` | — |
| [SRC-1AE03B9EC3-L000092](../../agents/web_agent.py#L92) | 92 | `"    \"primary\", \"source\", \"sources\", \"evidence\", \"report\", \"reports\", \"case\", \"cases\","` | — |
| [SRC-1AE03B9EC3-L000093](../../agents/web_agent.py#L93) | 93 | `"    \"study\", \"studies\", \"analysis\", \"latest\", \"news\", \"update\", \"updates\","` | — |
| [SRC-1AE03B9EC3-L000094](../../agents/web_agent.py#L94) | 94 | `"    \"announcement\", \"announcements\", \"comprehensive\", \"research\", \"statistic\","` | — |
| [SRC-1AE03B9EC3-L000095](../../agents/web_agent.py#L95) | 95 | `"    \"statistics\", \"trend\", \"trends\","` | — |
| [SRC-1AE03B9EC3-L000096](../../agents/web_agent.py#L96) | 96 | `"})"` | — |
| [SRC-1AE03B9EC3-L000097](../../agents/web_agent.py#L97) | 97 | `"_SEARCH_SYNONYMS = {"` | — |
| [SRC-1AE03B9EC3-L000098](../../agents/web_agent.py#L98) | 98 | `"    \"استراليا\": {\"australia\"}, \"عاصمة\": {\"capital\"}, \"مصر\": {\"egypt\"},"` | — |
| [SRC-1AE03B9EC3-L000099](../../agents/web_agent.py#L99) | 99 | `"    \"المصري\": {\"egyptian\", \"egypt\"}, \"مركزي\": {\"central\"},"` | — |
| [SRC-1AE03B9EC3-L000100](../../agents/web_agent.py#L100) | 100 | `"    \"المركزي\": {\"central\"}, \"بنك\": {\"bank\"}, \"البنك\": {\"bank\"},"` | — |
| [SRC-1AE03B9EC3-L000101](../../agents/web_agent.py#L101) | 101 | `"    \"قرار\": {\"decision\"}, \"قرارات\": {\"decision\", \"decisions\"},"` | — |
| [SRC-1AE03B9EC3-L000102](../../agents/web_agent.py#L102) | 102 | `"    \"سعر\": {\"price\"}, \"اسعار\": {\"prices\"}, \"استضافة\": {\"hosting\"},"` | — |
| [SRC-1AE03B9EC3-L000103](../../agents/web_agent.py#L103) | 103 | `"    \"شركة\": {\"company\"}, \"شركه\": {\"company\"}, \"ناشئة\": {\"startup\"},"` | — |
| [SRC-1AE03B9EC3-L000104](../../agents/web_agent.py#L104) | 104 | `"    \"صعيد\": {\"upper\"}, \"مقارنة\": {\"compare\", \"comparison\"},"` | — |
| [SRC-1AE03B9EC3-L000105](../../agents/web_agent.py#L105) | 105 | `"    \"تقنية\": {\"technology\"}, \"تقنيات\": {\"technology\"},"` | — |
| [SRC-1AE03B9EC3-L000106](../../agents/web_agent.py#L106) | 106 | `"    \"ميكروسوفت\": {\"microsoft\"}, \"مايكروسوفت\": {\"microsoft\"},"` | — |
| [SRC-1AE03B9EC3-L000107](../../agents/web_agent.py#L107) | 107 | `"    \"microsoft\": {\"ميكروسوفت\", \"مايكروسوفت\"},"` | — |
| [SRC-1AE03B9EC3-L000108](../../agents/web_agent.py#L108) | 108 | `"    \"جمهورية\": {\"republic\"}, \"republic\": {\"جمهورية\"},"` | — |
| [SRC-1AE03B9EC3-L000109](../../agents/web_agent.py#L109) | 109 | `"    \"الرقمية\": {\"digital\"}, \"رقمية\": {\"digital\"},"` | — |
| [SRC-1AE03B9EC3-L000110](../../agents/web_agent.py#L110) | 110 | `"    \"الرقميه\": {\"digital\"}, \"رقميه\": {\"digital\"},"` | — |
| [SRC-1AE03B9EC3-L000111](../../agents/web_agent.py#L111) | 111 | `"    \"موقع\": {\"website\", \"portal\"}, \"مواقع\": {\"websites\", \"portals\"},"` | — |
| [SRC-1AE03B9EC3-L000112](../../agents/web_agent.py#L112) | 112 | `"    \"التجمع\": {\"settlement\"}, \"تجمع\": {\"settlement\"},"` | — |
| [SRC-1AE03B9EC3-L000113](../../agents/web_agent.py#L113) | 113 | `"    \"الخامس\": {\"fifth\", \"5th\"}, \"خامس\": {\"fifth\", \"5th\"},"` | — |
| [SRC-1AE03B9EC3-L000114](../../agents/web_agent.py#L114) | 114 | `"    \"شقة\": {\"apartment\", \"flat\"}, \"شقق\": {\"apartments\", \"flats\"},"` | — |
| [SRC-1AE03B9EC3-L000115](../../agents/web_agent.py#L115) | 115 | `"    \"عميل\": {\"customer\", \"buyer\"}, \"عملاء\": {\"customers\", \"buyers\"},"` | — |
| [SRC-1AE03B9EC3-L000116](../../agents/web_agent.py#L116) | 116 | `"    \"شراء\": {\"buy\", \"purchase\"}, \"مشتري\": {\"buyer\"},"` | — |
| [SRC-1AE03B9EC3-L000117](../../agents/web_agent.py#L117) | 117 | `"    # Small, explicit Arabic-English topic vocabulary; this helps Arabic prompts"` | — |
| [SRC-1AE03B9EC3-L000118](../../agents/web_agent.py#L118) | 118 | `"    # match English-indexed results without relaxing URL or destination safety."` | — |
| [SRC-1AE03B9EC3-L000119](../../agents/web_agent.py#L119) | 119 | `"    \"سيارة\": {\"car\", \"vehicle\"}, \"السيارة\": {\"car\", \"vehicle\"},"` | — |
| [SRC-1AE03B9EC3-L000120](../../agents/web_agent.py#L120) | 120 | `"    \"سيارات\": {\"cars\", \"vehicles\"}, \"السيارات\": {\"cars\", \"vehicles\"},"` | — |
| [SRC-1AE03B9EC3-L000121](../../agents/web_agent.py#L121) | 121 | `"    \"كهربائي\": {\"electric\"}, \"كهربائية\": {\"electric\"},"` | — |
| [SRC-1AE03B9EC3-L000122](../../agents/web_agent.py#L122) | 122 | `"    \"الكهربائي\": {\"electric\"}, \"الكهربائية\": {\"electric\"},"` | — |
| [SRC-1AE03B9EC3-L000123](../../agents/web_agent.py#L123) | 123 | `"    \"شحن\": {\"charging\", \"charge\"}, \"الشحن\": {\"charging\", \"charge\"},"` | — |
| [SRC-1AE03B9EC3-L000124](../../agents/web_agent.py#L124) | 124 | `"    \"شاحن\": {\"charger\"}, \"بطارية\": {\"battery\"}, \"بطاريات\": {\"batteries\"},"` | — |
| [SRC-1AE03B9EC3-L000125](../../agents/web_agent.py#L125) | 125 | `"    \"تكلفة\": {\"cost\", \"costs\"}, \"التكلفة\": {\"cost\", \"costs\"},"` | — |
| [SRC-1AE03B9EC3-L000126](../../agents/web_agent.py#L126) | 126 | `"    \"البنية\": {\"infrastructure\"}, \"التحتية\": {\"infrastructure\"},"` | — |
| [SRC-1AE03B9EC3-L000127](../../agents/web_agent.py#L127) | 127 | `"    \"تحدي\": {\"challenge\"}, \"تحديات\": {\"challenges\"}, \"التحديات\": {\"challenges\"},"` | — |
| [SRC-1AE03B9EC3-L000128](../../agents/web_agent.py#L128) | 128 | `"    \"وكيل\": {\"agent\"}, \"الوكيل\": {\"agent\"},"` | — |
| [SRC-1AE03B9EC3-L000129](../../agents/web_agent.py#L129) | 129 | `"    \"وكلاء\": {\"agents\"}, \"الوكلاء\": {\"agents\"},"` | — |
| [SRC-1AE03B9EC3-L000130](../../agents/web_agent.py#L130) | 130 | `"    # Bilingual vocabulary for AI use-case searches. Keep the relevance floor"` | — |
| [SRC-1AE03B9EC3-L000131](../../agents/web_agent.py#L131) | 131 | `"    # unchanged; expand only concepts that commonly appear in Arabic news titles."` | — |
| [SRC-1AE03B9EC3-L000132](../../agents/web_agent.py#L132) | 132 | `"    \"استخدام\": {\"use\", \"usage\", \"application\", \"applications\"},"` | — |
| [SRC-1AE03B9EC3-L000133](../../agents/web_agent.py#L133) | 133 | `"    \"استخدامات\": {\"use\", \"usage\", \"application\", \"applications\"},"` | — |
| [SRC-1AE03B9EC3-L000134](../../agents/web_agent.py#L134) | 134 | `"    \"استعمال\": {\"use\", \"usage\", \"application\"},"` | — |
| [SRC-1AE03B9EC3-L000135](../../agents/web_agent.py#L135) | 135 | `"    \"استعمالات\": {\"use\", \"usage\", \"applications\"},"` | — |
| [SRC-1AE03B9EC3-L000136](../../agents/web_agent.py#L136) | 136 | `"    \"حالة\": {\"case\"}, \"حالات\": {\"cases\", \"case\"},"` | — |
| [SRC-1AE03B9EC3-L000137](../../agents/web_agent.py#L137) | 137 | `"    \"اعمال\": {\"business\", \"businesses\", \"work\"},"` | — |
| [SRC-1AE03B9EC3-L000138](../../agents/web_agent.py#L138) | 138 | `"    \"الاعمال\": {\"business\", \"businesses\", \"work\"},"` | — |
| [SRC-1AE03B9EC3-L000139](../../agents/web_agent.py#L139) | 139 | `"    \"للاعمال\": {\"business\", \"businesses\", \"work\"},"` | — |
| [SRC-1AE03B9EC3-L000140](../../agents/web_agent.py#L140) | 140 | `"    \"شركات\": {\"company\", \"companies\", \"business\", \"businesses\"},"` | — |
| [SRC-1AE03B9EC3-L000141](../../agents/web_agent.py#L141) | 141 | `"    \"الشركات\": {\"company\", \"companies\", \"business\", \"businesses\"},"` | — |
| [SRC-1AE03B9EC3-L000142](../../agents/web_agent.py#L142) | 142 | `"    \"صغير\": {\"small\"}, \"صغيرة\": {\"small\"}, \"الصغير\": {\"small\"}, \"الصغيرة\": {\"small\"},"` | — |
| [SRC-1AE03B9EC3-L000143](../../agents/web_agent.py#L143) | 143 | `"    \"ذكاء\": {\"intelligence\", \"ai\"}, \"الذكاء\": {\"intelligence\", \"ai\"},"` | — |
| [SRC-1AE03B9EC3-L000144](../../agents/web_agent.py#L144) | 144 | `"    \"اصطناعي\": {\"artificial\", \"ai\"}, \"الاصطناعي\": {\"artificial\", \"ai\"},"` | — |
| [SRC-1AE03B9EC3-L000145](../../agents/web_agent.py#L145) | 145 | `"    \"تطور\": {\"development\", \"advance\"}, \"تطورات\": {\"developments\", \"advances\", \"updates\", \"latest\"},"` | — |
| [SRC-1AE03B9EC3-L000146](../../agents/web_agent.py#L146) | 146 | `"    \"التطورات\": {\"developments\", \"advances\", \"updates\", \"latest\"},"` | — |
| [SRC-1AE03B9EC3-L000147](../../agents/web_agent.py#L147) | 147 | `"    \"اراء\": {\"opinions\", \"views\"}, \"تجربة\": {\"experience\"}, \"تجارب\": {\"experiences\", \"reviews\"},"` | — |
| [SRC-1AE03B9EC3-L000148](../../agents/web_agent.py#L148) | 148 | `"    \"مستخدم\": {\"user\"}, \"المستخدم\": {\"user\"}, \"مستخدمين\": {\"users\"},"` | — |
| [SRC-1AE03B9EC3-L000149](../../agents/web_agent.py#L149) | 149 | `"    \"المستخدمين\": {\"users\"}, \"مالكون\": {\"owners\"}, \"المالكون\": {\"owners\"},"` | — |
| [SRC-1AE03B9EC3-L000150](../../agents/web_agent.py#L150) | 150 | `"}"` | — |
| [SRC-1AE03B9EC3-L000151](../../agents/web_agent.py#L151) | 151 | `"_CALENDAR_MONTHS = ("` | — |
| [SRC-1AE03B9EC3-L000152](../../agents/web_agent.py#L152) | 152 | `"    \"يناير\", \"فبراير\", \"مارس\", \"ابريل\", \"أبريل\", \"مايو\", \"يونيو\","` | — |
| [SRC-1AE03B9EC3-L000153](../../agents/web_agent.py#L153) | 153 | `"    \"يوليو\", \"اغسطس\", \"أغسطس\", \"سبتمبر\", \"اكتوبر\", \"أكتوبر\","` | — |
| [SRC-1AE03B9EC3-L000154](../../agents/web_agent.py#L154) | 154 | `"    \"نوفمبر\", \"ديسمبر\", \"january\", \"february\", \"march\", \"april\","` | — |
| [SRC-1AE03B9EC3-L000155](../../agents/web_agent.py#L155) | 155 | `"    \"may\", \"june\", \"july\", \"august\", \"september\", \"october\","` | — |
| [SRC-1AE03B9EC3-L000156](../../agents/web_agent.py#L156) | 156 | `"    \"november\", \"december\","` | — |
| [SRC-1AE03B9EC3-L000157](../../agents/web_agent.py#L157) | 157 | `")"` | — |
| [SRC-1AE03B9EC3-L000158](../../agents/web_agent.py#L158) | 158 | `"_BLOCKED_SOURCE_DOMAINS = frozenset({"` | — |
| [SRC-1AE03B9EC3-L000159](../../agents/web_agent.py#L159) | 159 | `"    \"translate.google.com\", \"translate.googleusercontent.com\","` | — |
| [SRC-1AE03B9EC3-L000160](../../agents/web_agent.py#L160) | 160 | `"})"` | — |
| [SRC-1AE03B9EC3-L000161](../../agents/web_agent.py#L161) | 161 | `""` | — |
| [SRC-1AE03B9EC3-L000162](../../agents/web_agent.py#L162) | 162 | `""` | — |
| [SRC-1AE03B9EC3-L000163](../../agents/web_agent.py#L163) | 163 | `"def _normalize_search_query(value: str) -> str:"` | — |
| [SRC-1AE03B9EC3-L000164](../../agents/web_agent.py#L164) | 164 | `"    \"\"\"Normalize Arabic letters/diacritics while preserving search operators and dates.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000165](../../agents/web_agent.py#L165) | 165 | `"    value = unicodedata.normalize(\"NFKC\", value or \"\")"` | — |
| [SRC-1AE03B9EC3-L000166](../../agents/web_agent.py#L166) | 166 | `"    value = _ARABIC_DIACRITICS_RE.sub(\"\", value).translate(_ARABIC_SEARCH_TRANSLATION)"` | — |
| [SRC-1AE03B9EC3-L000167](../../agents/web_agent.py#L167) | 167 | `"    return re.sub(r\"\\s+\", \" \", value).strip()"` | — |
| [SRC-1AE03B9EC3-L000168](../../agents/web_agent.py#L168) | 168 | `""` | — |
| [SRC-1AE03B9EC3-L000169](../../agents/web_agent.py#L169) | 169 | `""` | — |
| [SRC-1AE03B9EC3-L000170](../../agents/web_agent.py#L170) | 170 | `"# Normalize stop words too: otherwise Arabic letter normalization (e.g. ة→ه, أ→ا)"` | — |
| [SRC-1AE03B9EC3-L000171](../../agents/web_agent.py#L171) | 171 | `"# can leave request-format wording in the token set and distort relevance scores."` | — |
| [SRC-1AE03B9EC3-L000172](../../agents/web_agent.py#L172) | 172 | `"_NORMALIZED_SEARCH_STOPWORDS = frozenset("` | — |
| [SRC-1AE03B9EC3-L000173](../../agents/web_agent.py#L173) | 173 | `"    _normalize_search_query(word).casefold() for word in _SEARCH_STOPWORDS"` | — |
| [SRC-1AE03B9EC3-L000174](../../agents/web_agent.py#L174) | 174 | `")"` | — |
| [SRC-1AE03B9EC3-L000175](../../agents/web_agent.py#L175) | 175 | `""` | — |
| [SRC-1AE03B9EC3-L000176](../../agents/web_agent.py#L176) | 176 | `""` | — |
| [SRC-1AE03B9EC3-L000177](../../agents/web_agent.py#L177) | 177 | `"# Normalize synonym keys and values by the same rules as search text. This avoids"` | — |
| [SRC-1AE03B9EC3-L000178](../../agents/web_agent.py#L178) | 178 | `"# Arabic ta-marbuta/alif variants silently disabling Arabic-to-English matching."` | — |
| [SRC-1AE03B9EC3-L000179](../../agents/web_agent.py#L179) | 179 | `"_NORMALIZED_SEARCH_SYNONYMS: dict[str, set[str]] = {}"` | — |
| [SRC-1AE03B9EC3-L000180](../../agents/web_agent.py#L180) | 180 | `"for _synonym_key, _synonym_values in _SEARCH_SYNONYMS.items():"` | — |
| [SRC-1AE03B9EC3-L000181](../../agents/web_agent.py#L181) | 181 | `"    _normalized_key = _normalize_search_query(_synonym_key).casefold()"` | — |
| [SRC-1AE03B9EC3-L000182](../../agents/web_agent.py#L182) | 182 | `"    _NORMALIZED_SEARCH_SYNONYMS.setdefault(_normalized_key, set()).update("` | — |
| [SRC-1AE03B9EC3-L000183](../../agents/web_agent.py#L183) | 183 | `"        _normalize_search_query(value).casefold() for value in _synonym_values"` | — |
| [SRC-1AE03B9EC3-L000184](../../agents/web_agent.py#L184) | 184 | `"    )"` | — |
| [SRC-1AE03B9EC3-L000185](../../agents/web_agent.py#L185) | 185 | `""` | — |
| [SRC-1AE03B9EC3-L000186](../../agents/web_agent.py#L186) | 186 | `""` | — |
| [SRC-1AE03B9EC3-L000187](../../agents/web_agent.py#L187) | 187 | `"def _search_tokens(value: str) -> set[str]:"` | — |
| [SRC-1AE03B9EC3-L000188](../../agents/web_agent.py#L188) | 188 | `"    \"\"\"Tokenize Arabic/English text and expand a small bilingual vocabulary.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000189](../../agents/web_agent.py#L189) | 189 | `"    value = _normalize_search_query(value).casefold()"` | — |
| [SRC-1AE03B9EC3-L000190](../../agents/web_agent.py#L190) | 190 | `"    value = re.sub(r\"(?i)\\bsite\\s*:\\s*\\S+\", \" \", value)"` | — |
| [SRC-1AE03B9EC3-L000191](../../agents/web_agent.py#L191) | 191 | `"    tokens = re.findall(r\"[a-z0-9]+\|[\\u0620-\\u064A\\u066E-\\u06D3]+\", value)"` | — |
| [SRC-1AE03B9EC3-L000192](../../agents/web_agent.py#L192) | 192 | `"    result: set[str] = set()"` | — |
| [SRC-1AE03B9EC3-L000193](../../agents/web_agent.py#L193) | 193 | `"    for token in tokens:"` | — |
| [SRC-1AE03B9EC3-L000194](../../agents/web_agent.py#L194) | 194 | `"        if token in _NORMALIZED_SEARCH_STOPWORDS or len(token) < 2:"` | — |
| [SRC-1AE03B9EC3-L000195](../../agents/web_agent.py#L195) | 195 | `"            continue"` | — |
| [SRC-1AE03B9EC3-L000196](../../agents/web_agent.py#L196) | 196 | `"        forms = {token}"` | — |
| [SRC-1AE03B9EC3-L000197](../../agents/web_agent.py#L197) | 197 | `"        if token.startswith(\"ال\") and len(token) > 4:"` | — |
| [SRC-1AE03B9EC3-L000198](../../agents/web_agent.py#L198) | 198 | `"            forms.add(token[2:])"` | — |
| [SRC-1AE03B9EC3-L000199](../../agents/web_agent.py#L199) | 199 | `"        forms.update(_NORMALIZED_SEARCH_SYNONYMS.get(token, set()))"` | — |
| [SRC-1AE03B9EC3-L000200](../../agents/web_agent.py#L200) | 200 | `"        # Reverse-map common English equivalents so Arabic and English results can match."` | — |
| [SRC-1AE03B9EC3-L000201](../../agents/web_agent.py#L201) | 201 | `"        for arabic, english in _NORMALIZED_SEARCH_SYNONYMS.items():"` | — |
| [SRC-1AE03B9EC3-L000202](../../agents/web_agent.py#L202) | 202 | `"            if token in english:"` | — |
| [SRC-1AE03B9EC3-L000203](../../agents/web_agent.py#L203) | 203 | `"                forms.add(arabic)"` | — |
| [SRC-1AE03B9EC3-L000204](../../agents/web_agent.py#L204) | 204 | `"                if arabic.startswith(\"ال\") and len(arabic) > 4:"` | — |
| [SRC-1AE03B9EC3-L000205](../../agents/web_agent.py#L205) | 205 | `"                    forms.add(arabic[2:])"` | — |
| [SRC-1AE03B9EC3-L000206](../../agents/web_agent.py#L206) | 206 | `"        result.update(forms)"` | — |
| [SRC-1AE03B9EC3-L000207](../../agents/web_agent.py#L207) | 207 | `"    return result"` | — |
| [SRC-1AE03B9EC3-L000208](../../agents/web_agent.py#L208) | 208 | `""` | — |
| [SRC-1AE03B9EC3-L000209](../../agents/web_agent.py#L209) | 209 | `""` | — |
| [SRC-1AE03B9EC3-L000210](../../agents/web_agent.py#L210) | 210 | `"def _relevance_query_tokens(query: str) -> set[str]:"` | — |
| [SRC-1AE03B9EC3-L000211](../../agents/web_agent.py#L211) | 211 | `"    \"\"\"Return topic concepts after removing answer-format and query-expansion wording.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000212](../../agents/web_agent.py#L212) | 212 | `"    query = compact_search_query(query)"` | — |
| [SRC-1AE03B9EC3-L000213](../../agents/web_agent.py#L213) | 213 | `"    if not query:"` | — |
| [SRC-1AE03B9EC3-L000214](../../agents/web_agent.py#L214) | 214 | `"        return set()"` | — |
| [SRC-1AE03B9EC3-L000215](../../agents/web_agent.py#L215) | 215 | `"    query_text = _normalize_search_query(query).casefold()"` | — |
| [SRC-1AE03B9EC3-L000216](../../agents/web_agent.py#L216) | 216 | `"    query_text = re.sub(r\"(?i)\\bsite\\s*:\\s*\\S+\", \" \", query_text)"` | — |
| [SRC-1AE03B9EC3-L000217](../../agents/web_agent.py#L217) | 217 | `"    return {"` | — |
| [SRC-1AE03B9EC3-L000218](../../agents/web_agent.py#L218) | 218 | `"        token for token in re.findall(r\"[a-z0-9]+\|[\\u0620-\\u064A\\u066E-\\u06D3]+\", query_text)"` | — |
| [SRC-1AE03B9EC3-L000219](../../agents/web_agent.py#L219) | 219 | `"        if ("` | — |
| [SRC-1AE03B9EC3-L000220](../../agents/web_agent.py#L220) | 220 | `"            token not in _NORMALIZED_SEARCH_STOPWORDS"` | — |
| [SRC-1AE03B9EC3-L000221](../../agents/web_agent.py#L221) | 221 | `"            and token not in _GENERIC_QUERY_MODIFIER_TOKENS"` | — |
| [SRC-1AE03B9EC3-L000222](../../agents/web_agent.py#L222) | 222 | `"            and len(token) >= 2"` | — |
| [SRC-1AE03B9EC3-L000223](../../agents/web_agent.py#L223) | 223 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000224](../../agents/web_agent.py#L224) | 224 | `"    }"` | — |
| [SRC-1AE03B9EC3-L000225](../../agents/web_agent.py#L225) | 225 | `""` | — |
| [SRC-1AE03B9EC3-L000226](../../agents/web_agent.py#L226) | 226 | `""` | — |
| [SRC-1AE03B9EC3-L000227](../../agents/web_agent.py#L227) | 227 | `"def _minimum_relevance_ratio(_query: str) -> float:"` | — |
| [SRC-1AE03B9EC3-L000228](../../agents/web_agent.py#L228) | 228 | `"    \"\"\"Keep the established 20% relevance floor after query normalization and token cleanup.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000229](../../agents/web_agent.py#L229) | 229 | `"    return 0.20"` | — |
| [SRC-1AE03B9EC3-L000230](../../agents/web_agent.py#L230) | 230 | `""` | — |
| [SRC-1AE03B9EC3-L000231](../../agents/web_agent.py#L231) | 231 | `""` | — |
| [SRC-1AE03B9EC3-L000232](../../agents/web_agent.py#L232) | 232 | `"def _relevance_ratio(query: str, evidence: str) -> float:"` | — |
| [SRC-1AE03B9EC3-L000233](../../agents/web_agent.py#L233) | 233 | `"    \"\"\"Fraction of meaningful query concepts present in a candidate's title/snippet.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000234](../../agents/web_agent.py#L234) | 234 | `"    query_tokens = _relevance_query_tokens(query)"` | — |
| [SRC-1AE03B9EC3-L000235](../../agents/web_agent.py#L235) | 235 | `"    if not query_tokens:"` | — |
| [SRC-1AE03B9EC3-L000236](../../agents/web_agent.py#L236) | 236 | `"        # Relevance cannot be established from an instruction-only query."` | — |
| [SRC-1AE03B9EC3-L000237](../../agents/web_agent.py#L237) | 237 | `"        return 0.0"` | — |
| [SRC-1AE03B9EC3-L000238](../../agents/web_agent.py#L238) | 238 | `"    expanded_evidence = _search_tokens(evidence)"` | — |
| [SRC-1AE03B9EC3-L000239](../../agents/web_agent.py#L239) | 239 | `"    matched = sum("` | — |
| [SRC-1AE03B9EC3-L000240](../../agents/web_agent.py#L240) | 240 | `"        1 for token in query_tokens"` | — |
| [SRC-1AE03B9EC3-L000241](../../agents/web_agent.py#L241) | 241 | `"        if token in expanded_evidence"` | — |
| [SRC-1AE03B9EC3-L000242](../../agents/web_agent.py#L242) | 242 | `"        or (token.startswith(\"ال\") and token[2:] in expanded_evidence)"` | — |
| [SRC-1AE03B9EC3-L000243](../../agents/web_agent.py#L243) | 243 | `"        or bool(_NORMALIZED_SEARCH_SYNONYMS.get(token, set()) & expanded_evidence)"` | — |
| [SRC-1AE03B9EC3-L000244](../../agents/web_agent.py#L244) | 244 | `"    )"` | — |
| [SRC-1AE03B9EC3-L000245](../../agents/web_agent.py#L245) | 245 | `"    ratio = matched / len(query_tokens)"` | — |
| [SRC-1AE03B9EC3-L000246](../../agents/web_agent.py#L246) | 246 | `"    # On longer questions, two matching topic concepts are required; request wording"` | — |
| [SRC-1AE03B9EC3-L000247](../../agents/web_agent.py#L247) | 247 | `"    # should not silently raise that floor to three or four concepts."` | — |
| [SRC-1AE03B9EC3-L000248](../../agents/web_agent.py#L248) | 248 | `"    if len(query_tokens) >= 4 and matched < 2:"` | — |
| [SRC-1AE03B9EC3-L000249](../../agents/web_agent.py#L249) | 249 | `"        return 0.0"` | — |
| [SRC-1AE03B9EC3-L000250](../../agents/web_agent.py#L250) | 250 | `"    return ratio"` | — |
| [SRC-1AE03B9EC3-L000251](../../agents/web_agent.py#L251) | 251 | `""` | — |
| [SRC-1AE03B9EC3-L000252](../../agents/web_agent.py#L252) | 252 | `"def _blocked_source_url(url: str) -> bool:"` | — |
| [SRC-1AE03B9EC3-L000253](../../agents/web_agent.py#L253) | 253 | `"    try:"` | — |
| [SRC-1AE03B9EC3-L000254](../../agents/web_agent.py#L254) | 254 | `"        host = (urllib.parse.urlparse(url).hostname or \"\").lower().rstrip(\".\")"` | — |
| [SRC-1AE03B9EC3-L000255](../../agents/web_agent.py#L255) | 255 | `"        return any(host == domain or host.endswith(\".\" + domain) for domain in _BLOCKED_SOURCE_DOMAINS)"` | — |
| [SRC-1AE03B9EC3-L000256](../../agents/web_agent.py#L256) | 256 | `"    except (TypeError, ValueError):"` | — |
| [SRC-1AE03B9EC3-L000257](../../agents/web_agent.py#L257) | 257 | `"        return True"` | — |
| [SRC-1AE03B9EC3-L000258](../../agents/web_agent.py#L258) | 258 | `""` | — |
| [SRC-1AE03B9EC3-L000259](../../agents/web_agent.py#L259) | 259 | `""` | — |
| [SRC-1AE03B9EC3-L000260](../../agents/web_agent.py#L260) | 260 | `"class AgentDependencyError(RuntimeError):"` | — |
| [SRC-1AE03B9EC3-L000261](../../agents/web_agent.py#L261) | 261 | `"    \"\"\"A required optional runtime dependency is unavailable.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000262](../../agents/web_agent.py#L262) | 262 | `""` | — |
| [SRC-1AE03B9EC3-L000263](../../agents/web_agent.py#L263) | 263 | `""` | — |
| [SRC-1AE03B9EC3-L000264](../../agents/web_agent.py#L264) | 264 | `"def _clean_text(value: Any, limit: int) -> str:"` | — |
| [SRC-1AE03B9EC3-L000265](../../agents/web_agent.py#L265) | 265 | `"    if not isinstance(value, str):"` | — |
| [SRC-1AE03B9EC3-L000266](../../agents/web_agent.py#L266) | 266 | `"        return \"\""` | — |
| [SRC-1AE03B9EC3-L000267](../../agents/web_agent.py#L267) | 267 | `"    return \" \".join(value.replace(\"\\x00\", \" \").split())[:limit]"` | — |
| [SRC-1AE03B9EC3-L000268](../../agents/web_agent.py#L268) | 268 | `""` | — |
| [SRC-1AE03B9EC3-L000269](../../agents/web_agent.py#L269) | 269 | `""` | — |
| [SRC-1AE03B9EC3-L000270](../../agents/web_agent.py#L270) | 270 | `"def _public_http_url(value: Any) -> str \| None:"` | — |
| [SRC-1AE03B9EC3-L000271](../../agents/web_agent.py#L271) | 271 | `"    \"\"\"Lexically validate an HTTP URL before using it as a search source.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000272](../../agents/web_agent.py#L272) | 272 | `"    if not isinstance(value, str) or len(value) > 2048:"` | — |
| [SRC-1AE03B9EC3-L000273](../../agents/web_agent.py#L273) | 273 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000274](../../agents/web_agent.py#L274) | 274 | `"    try:"` | — |
| [SRC-1AE03B9EC3-L000275](../../agents/web_agent.py#L275) | 275 | `"        parsed = urllib.parse.urlparse(value.strip())"` | — |
| [SRC-1AE03B9EC3-L000276](../../agents/web_agent.py#L276) | 276 | `"        if parsed.scheme not in {\"http\", \"https\"}:"` | — |
| [SRC-1AE03B9EC3-L000277](../../agents/web_agent.py#L277) | 277 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L000278](../../agents/web_agent.py#L278) | 278 | `"        if not parsed.hostname or parsed.username is not None or parsed.password is not None:"` | — |
| [SRC-1AE03B9EC3-L000279](../../agents/web_agent.py#L279) | 279 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L000280](../../agents/web_agent.py#L280) | 280 | `"        if parsed.port not in (None, 80, 443):"` | — |
| [SRC-1AE03B9EC3-L000281](../../agents/web_agent.py#L281) | 281 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L000282](../../agents/web_agent.py#L282) | 282 | `"        host = parsed.hostname.rstrip(\".\").lower()"` | — |
| [SRC-1AE03B9EC3-L000283](../../agents/web_agent.py#L283) | 283 | `"        if not host or host in {\"localhost\"} or host.endswith((\".local\", \".internal\", \".localhost\")):"` | — |
| [SRC-1AE03B9EC3-L000284](../../agents/web_agent.py#L284) | 284 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L000285](../../agents/web_agent.py#L285) | 285 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L000286](../../agents/web_agent.py#L286) | 286 | `"            ip = ipaddress.ip_address(host)"` | — |
| [SRC-1AE03B9EC3-L000287](../../agents/web_agent.py#L287) | 287 | `"        except ValueError:"` | — |
| [SRC-1AE03B9EC3-L000288](../../agents/web_agent.py#L288) | 288 | `"            pass"` | — |
| [SRC-1AE03B9EC3-L000289](../../agents/web_agent.py#L289) | 289 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L000290](../../agents/web_agent.py#L290) | 290 | `"            if not ip.is_global:"` | — |
| [SRC-1AE03B9EC3-L000291](../../agents/web_agent.py#L291) | 291 | `"                return None"` | — |
| [SRC-1AE03B9EC3-L000292](../../agents/web_agent.py#L292) | 292 | `"        return urllib.parse.urlunparse(parsed._replace(fragment=\"\"))"` | — |
| [SRC-1AE03B9EC3-L000293](../../agents/web_agent.py#L293) | 293 | `"    except (ValueError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L000294](../../agents/web_agent.py#L294) | 294 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000295](../../agents/web_agent.py#L295) | 295 | `""` | — |
| [SRC-1AE03B9EC3-L000296](../../agents/web_agent.py#L296) | 296 | `""` | — |
| [SRC-1AE03B9EC3-L000297](../../agents/web_agent.py#L297) | 297 | `"def _public_ip_literals(host: str) -> list[str] \| None:"` | — |
| [SRC-1AE03B9EC3-L000298](../../agents/web_agent.py#L298) | 298 | `"    \"\"\"Resolve host and return its public addresses."` | — |
| [SRC-1AE03B9EC3-L000299](../../agents/web_agent.py#L299) | 299 | `""` | — |
| [SRC-1AE03B9EC3-L000300](../../agents/web_agent.py#L300) | 300 | `"    Returns None when resolution fails or any answer is not a global address."` | — |
| [SRC-1AE03B9EC3-L000301](../../agents/web_agent.py#L301) | 301 | `"    Callers must open the TCP connection to one of these literals. A second DNS"` | — |
| [SRC-1AE03B9EC3-L000302](../../agents/web_agent.py#L302) | 302 | `"    lookup is not equivalent: the name can be rebound to a private address"` | — |
| [SRC-1AE03B9EC3-L000303](../../agents/web_agent.py#L303) | 303 | `"    between the check and the connection (DNS rebinding / TOCTOU)."` | — |
| [SRC-1AE03B9EC3-L000304](../../agents/web_agent.py#L304) | 304 | `"    \"\"\""` | — |
| [SRC-1AE03B9EC3-L000305](../../agents/web_agent.py#L305) | 305 | `"    if not host:"` | — |
| [SRC-1AE03B9EC3-L000306](../../agents/web_agent.py#L306) | 306 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000307](../../agents/web_agent.py#L307) | 307 | `"    try:"` | — |
| [SRC-1AE03B9EC3-L000308](../../agents/web_agent.py#L308) | 308 | `"        answers = socket.getaddrinfo(host, None, type=socket.SOCK_STREAM)"` | — |
| [SRC-1AE03B9EC3-L000309](../../agents/web_agent.py#L309) | 309 | `"    except (OSError, socket.gaierror):"` | — |
| [SRC-1AE03B9EC3-L000310](../../agents/web_agent.py#L310) | 310 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000311](../../agents/web_agent.py#L311) | 311 | `"    if not answers:"` | — |
| [SRC-1AE03B9EC3-L000312](../../agents/web_agent.py#L312) | 312 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000313](../../agents/web_agent.py#L313) | 313 | `"    literals: list[str] = []"` | — |
| [SRC-1AE03B9EC3-L000314](../../agents/web_agent.py#L314) | 314 | `"    for answer in answers:"` | — |
| [SRC-1AE03B9EC3-L000315](../../agents/web_agent.py#L315) | 315 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L000316](../../agents/web_agent.py#L316) | 316 | `"            address = ipaddress.ip_address(answer[4][0])"` | — |
| [SRC-1AE03B9EC3-L000317](../../agents/web_agent.py#L317) | 317 | `"        except ValueError:"` | — |
| [SRC-1AE03B9EC3-L000318](../../agents/web_agent.py#L318) | 318 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L000319](../../agents/web_agent.py#L319) | 319 | `"        if not address.is_global:"` | — |
| [SRC-1AE03B9EC3-L000320](../../agents/web_agent.py#L320) | 320 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L000321](../../agents/web_agent.py#L321) | 321 | `"        literal = str(address)"` | — |
| [SRC-1AE03B9EC3-L000322](../../agents/web_agent.py#L322) | 322 | `"        if literal not in literals:"` | — |
| [SRC-1AE03B9EC3-L000323](../../agents/web_agent.py#L323) | 323 | `"            literals.append(literal)"` | — |
| [SRC-1AE03B9EC3-L000324](../../agents/web_agent.py#L324) | 324 | `"    return literals or None"` | — |
| [SRC-1AE03B9EC3-L000325](../../agents/web_agent.py#L325) | 325 | `""` | — |
| [SRC-1AE03B9EC3-L000326](../../agents/web_agent.py#L326) | 326 | `""` | — |
| [SRC-1AE03B9EC3-L000327](../../agents/web_agent.py#L327) | 327 | `"def _host_resolves_publicly(host: str) -> bool:"` | — |
| [SRC-1AE03B9EC3-L000328](../../agents/web_agent.py#L328) | 328 | `"    \"\"\"Reject local/private destinations before fetching a third-party page.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000329](../../agents/web_agent.py#L329) | 329 | `"    return _public_ip_literals(host) is not None"` | — |
| [SRC-1AE03B9EC3-L000330](../../agents/web_agent.py#L330) | 330 | `""` | — |
| [SRC-1AE03B9EC3-L000331](../../agents/web_agent.py#L331) | 331 | `""` | — |
| [SRC-1AE03B9EC3-L000332](../../agents/web_agent.py#L332) | 332 | `"def _pinned_connect_url(logical_url: str, ip: str) -> str \| None:"` | — |
| [SRC-1AE03B9EC3-L000333](../../agents/web_agent.py#L333) | 333 | `"    \"\"\"Rewrite a validated public URL so the connection target is a checked IP.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000334](../../agents/web_agent.py#L334) | 334 | `"    parsed = urllib.parse.urlparse(logical_url)"` | — |
| [SRC-1AE03B9EC3-L000335](../../agents/web_agent.py#L335) | 335 | `"    if parsed.port not in (None, 80, 443):"` | — |
| [SRC-1AE03B9EC3-L000336](../../agents/web_agent.py#L336) | 336 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000337](../../agents/web_agent.py#L337) | 337 | `"    literal = f\"[{ip}]\" if \":\" in ip else ip"` | — |
| [SRC-1AE03B9EC3-L000338](../../agents/web_agent.py#L338) | 338 | `"    netloc = literal if parsed.port is None else f\"{literal}:{parsed.port}\""` | — |
| [SRC-1AE03B9EC3-L000339](../../agents/web_agent.py#L339) | 339 | `"    return urllib.parse.urlunparse(parsed._replace(netloc=netloc))"` | — |
| [SRC-1AE03B9EC3-L000340](../../agents/web_agent.py#L340) | 340 | `""` | — |
| [SRC-1AE03B9EC3-L000341](../../agents/web_agent.py#L341) | 341 | `""` | — |
| [SRC-1AE03B9EC3-L000342](../../agents/web_agent.py#L342) | 342 | `"def _fallback_answer(sources: list[dict[str, Any]], reason: str) -> str:"` | — |
| [SRC-1AE03B9EC3-L000343](../../agents/web_agent.py#L343) | 343 | `"    lines = [reason]"` | — |
| [SRC-1AE03B9EC3-L000344](../../agents/web_agent.py#L344) | 344 | `"    usable = [source for source in sources if source.get(\"snippet\")]"` | — |
| [SRC-1AE03B9EC3-L000345](../../agents/web_agent.py#L345) | 345 | `"    for index, source in enumerate(usable[:5], 1):"` | — |
| [SRC-1AE03B9EC3-L000346](../../agents/web_agent.py#L346) | 346 | `"        lines.append("` | — |
| [SRC-1AE03B9EC3-L000347](../../agents/web_agent.py#L347) | 347 | `"            f\"{index}. {source.get('title', 'نتيجة ويب')}: \""` | — |
| [SRC-1AE03B9EC3-L000348](../../agents/web_agent.py#L348) | 348 | `"            f\"{source['snippet']} (المصدر: {source['url']})\""` | — |
| [SRC-1AE03B9EC3-L000349](../../agents/web_agent.py#L349) | 349 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000350](../../agents/web_agent.py#L350) | 350 | `"    if not usable:"` | — |
| [SRC-1AE03B9EC3-L000351](../../agents/web_agent.py#L351) | 351 | `"        lines.append(\"لم أتمكن من استخراج مقتطفات كافية من نتائج الويب.\")"` | — |
| [SRC-1AE03B9EC3-L000352](../../agents/web_agent.py#L352) | 352 | `"    return \"\\n\\n\".join(lines)"` | — |
| [SRC-1AE03B9EC3-L000353](../../agents/web_agent.py#L353) | 353 | `""` | — |
| [SRC-1AE03B9EC3-L000354](../../agents/web_agent.py#L354) | 354 | `""` | — |
| [SRC-1AE03B9EC3-L000355](../../agents/web_agent.py#L355) | 355 | `"class PageFetchResult(tuple):"` | — |
| [SRC-1AE03B9EC3-L000356](../../agents/web_agent.py#L356) | 356 | `"    \"\"\"Two-item tuple compatible with legacy callers, with structured extraction status.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000357](../../agents/web_agent.py#L357) | 357 | `""` | — |
| [SRC-1AE03B9EC3-L000358](../../agents/web_agent.py#L358) | 358 | `"    def __new__("` | — |
| [SRC-1AE03B9EC3-L000359](../../agents/web_agent.py#L359) | 359 | `"        cls,"` | — |
| [SRC-1AE03B9EC3-L000360](../../agents/web_agent.py#L360) | 360 | `"        title: str = \"\","` | — |
| [SRC-1AE03B9EC3-L000361](../../agents/web_agent.py#L361) | 361 | `"        page_text: str = \"\","` | — |
| [SRC-1AE03B9EC3-L000362](../../agents/web_agent.py#L362) | 362 | `"        status: str = \"unknown\","` | — |
| [SRC-1AE03B9EC3-L000363](../../agents/web_agent.py#L363) | 363 | `"        error_class: str \| None = None,"` | — |
| [SRC-1AE03B9EC3-L000364](../../agents/web_agent.py#L364) | 364 | `"    ):"` | — |
| [SRC-1AE03B9EC3-L000365](../../agents/web_agent.py#L365) | 365 | `"        value = super().__new__(cls, (title, page_text))"` | — |
| [SRC-1AE03B9EC3-L000366](../../agents/web_agent.py#L366) | 366 | `"        value.status = status"` | — |
| [SRC-1AE03B9EC3-L000367](../../agents/web_agent.py#L367) | 367 | `"        value.error_class = error_class"` | — |
| [SRC-1AE03B9EC3-L000368](../../agents/web_agent.py#L368) | 368 | `"        return value"` | — |
| [SRC-1AE03B9EC3-L000369](../../agents/web_agent.py#L369) | 369 | `""` | — |
| [SRC-1AE03B9EC3-L000370](../../agents/web_agent.py#L370) | 370 | `""` | — |
| [SRC-1AE03B9EC3-L000371](../../agents/web_agent.py#L371) | 371 | `"class WebAgent:"` | — |
| [SRC-1AE03B9EC3-L000372](../../agents/web_agent.py#L372) | 372 | `"    \"\"\"Search, inspect, and synthesize web evidence for open-ended questions.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000373](../../agents/web_agent.py#L373) | 373 | `""` | — |
| [SRC-1AE03B9EC3-L000374](../../agents/web_agent.py#L374) | 374 | `"    def __init__(self) -> None:"` | — |
| [SRC-1AE03B9EC3-L000375](../../agents/web_agent.py#L375) | 375 | `"        self.api_key = ("` | — |
| [SRC-1AE03B9EC3-L000376](../../agents/web_agent.py#L376) | 376 | `"            os.getenv(\"OMARAI_LLM_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000377](../../agents/web_agent.py#L377) | 377 | `"            or os.getenv(\"OPENROUTER_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000378](../../agents/web_agent.py#L378) | 378 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000379](../../agents/web_agent.py#L379) | 379 | `"        self.base_url = os.getenv("` | — |
| [SRC-1AE03B9EC3-L000380](../../agents/web_agent.py#L380) | 380 | `"            \"OMARAI_LLM_BASE_URL\", \"https://openrouter.ai/api/v1\""` | — |
| [SRC-1AE03B9EC3-L000381](../../agents/web_agent.py#L381) | 381 | `"        ).strip().rstrip(\"/\")"` | — |
| [SRC-1AE03B9EC3-L000382](../../agents/web_agent.py#L382) | 382 | `"        # Pin explicit role models for more consistent behaviour than a random free router."` | — |
| [SRC-1AE03B9EC3-L000383](../../agents/web_agent.py#L383) | 383 | `"        # OMARAI_LLM_MODEL remains a global override for users who want one model everywhere."` | — |
| [SRC-1AE03B9EC3-L000384](../../agents/web_agent.py#L384) | 384 | `"        global_model = os.getenv(\"OMARAI_LLM_MODEL\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000385](../../agents/web_agent.py#L385) | 385 | `"        self.answer_model = os.getenv("` | — |
| [SRC-1AE03B9EC3-L000386](../../agents/web_agent.py#L386) | 386 | `"            \"OMARAI_ANSWER_MODEL\", global_model or \"google/gemma-4-31b-it:free\""` | — |
| [SRC-1AE03B9EC3-L000387](../../agents/web_agent.py#L387) | 387 | `"        ).strip()"` | — |
| [SRC-1AE03B9EC3-L000388](../../agents/web_agent.py#L388) | 388 | `"        self.planner_model = os.getenv("` | — |
| [SRC-1AE03B9EC3-L000389](../../agents/web_agent.py#L389) | 389 | `"            \"OMARAI_PLANNER_MODEL\","` | — |
| [SRC-1AE03B9EC3-L000390](../../agents/web_agent.py#L390) | 390 | `"            global_model or \"nvidia/nemotron-3-ultra-550b-a55b:free\","` | — |
| [SRC-1AE03B9EC3-L000391](../../agents/web_agent.py#L391) | 391 | `"        ).strip()"` | — |
| [SRC-1AE03B9EC3-L000392](../../agents/web_agent.py#L392) | 392 | `"        self.review_model = os.getenv("` | — |
| [SRC-1AE03B9EC3-L000393](../../agents/web_agent.py#L393) | 393 | `"            \"OMARAI_REVIEW_MODEL\", self.answer_model"` | — |
| [SRC-1AE03B9EC3-L000394](../../agents/web_agent.py#L394) | 394 | `"        ).strip()"` | — |
| [SRC-1AE03B9EC3-L000395](../../agents/web_agent.py#L395) | 395 | `"        self.fallback_model = os.getenv("` | — |
| [SRC-1AE03B9EC3-L000396](../../agents/web_agent.py#L396) | 396 | `"            \"OMARAI_LLM_FALLBACK_MODEL\", \"openrouter/free\""` | — |
| [SRC-1AE03B9EC3-L000397](../../agents/web_agent.py#L397) | 397 | `"        ).strip()"` | — |
| [SRC-1AE03B9EC3-L000398](../../agents/web_agent.py#L398) | 398 | `"        self.model = self.answer_model  # Backwards-compatible alias."` | — |
| [SRC-1AE03B9EC3-L000399](../../agents/web_agent.py#L399) | 399 | `"        self.model_usage: list[dict[str, str]] = []"` | — |
| [SRC-1AE03B9EC3-L000400](../../agents/web_agent.py#L400) | 400 | `"        # Per-answer, bounded diagnostics contain only model identifiers and status metadata."` | — |
| [SRC-1AE03B9EC3-L000401](../../agents/web_agent.py#L401) | 401 | `"        # They intentionally exclude prompts, generated text, and provider response bodies."` | — |
| [SRC-1AE03B9EC3-L000402](../../agents/web_agent.py#L402) | 402 | `"        self.generation_diagnostics: list[dict[str, str]] = []"` | — |
| [SRC-1AE03B9EC3-L000403](../../agents/web_agent.py#L403) | 403 | `"        self.server_search_sources: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L000404](../../agents/web_agent.py#L404) | 404 | `"        self._provider_diagnostics: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L000405](../../agents/web_agent.py#L405) | 405 | `"        self._provider_diagnostics_lock = threading.Lock()"` | — |
| [SRC-1AE03B9EC3-L000406](../../agents/web_agent.py#L406) | 406 | `"        self._deepseek_budget_lock = threading.Lock()"` | — |
| [SRC-1AE03B9EC3-L000407](../../agents/web_agent.py#L407) | 407 | `"        self._deepseek_search_requests_reserved = 0"` | — |
| [SRC-1AE03B9EC3-L000408](../../agents/web_agent.py#L408) | 408 | `"        self.openrouter_web_search_enabled = ("` | — |
| [SRC-1AE03B9EC3-L000409](../../agents/web_agent.py#L409) | 409 | `"            os.getenv(\"OMARAI_OPENROUTER_WEB_SEARCH\", \"\").strip() == \"1\""` | — |
| [SRC-1AE03B9EC3-L000410](../../agents/web_agent.py#L410) | 410 | `"            and \"openrouter.ai\" in self.base_url.lower()"` | — |
| [SRC-1AE03B9EC3-L000411](../../agents/web_agent.py#L411) | 411 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000412](../../agents/web_agent.py#L412) | 412 | `"        self.timeout = max("` | — |
| [SRC-1AE03B9EC3-L000413](../../agents/web_agent.py#L413) | 413 | `"            5, min(int(os.getenv(\"OMARAI_LLM_TIMEOUT\", str(LLM_TIMEOUT_SECONDS))), 60)"` | — |
| [SRC-1AE03B9EC3-L000414](../../agents/web_agent.py#L414) | 414 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000415](../../agents/web_agent.py#L415) | 415 | `"        self._request_budget: RequestBudget \| None = None"` | — |
| [SRC-1AE03B9EC3-L000416](../../agents/web_agent.py#L416) | 416 | `""` | — |
| [SRC-1AE03B9EC3-L000417](../../agents/web_agent.py#L417) | 417 | `"    def _effective_timeout(self, configured_seconds: float) -> float:"` | — |
| [SRC-1AE03B9EC3-L000418](../../agents/web_agent.py#L418) | 418 | `"        \"\"\"Limit one outbound operation to the remaining per-answer time budget.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000419](../../agents/web_agent.py#L419) | 419 | `"        budget = getattr(self, \"_request_budget\", None)"` | — |
| [SRC-1AE03B9EC3-L000420](../../agents/web_agent.py#L420) | 420 | `"        if budget is None:"` | — |
| [SRC-1AE03B9EC3-L000421](../../agents/web_agent.py#L421) | 421 | `"            return float(configured_seconds)"` | — |
| [SRC-1AE03B9EC3-L000422](../../agents/web_agent.py#L422) | 422 | `"        return budget.timeout_for(configured_seconds)"` | — |
| [SRC-1AE03B9EC3-L000423](../../agents/web_agent.py#L423) | 423 | `""` | — |
| [SRC-1AE03B9EC3-L000424](../../agents/web_agent.py#L424) | 424 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000425](../../agents/web_agent.py#L425) | 425 | `"    def status() -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L000426](../../agents/web_agent.py#L426) | 426 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L000427](../../agents/web_agent.py#L427) | 427 | `"            import bs4  # noqa: F401"` | — |
| [SRC-1AE03B9EC3-L000428](../../agents/web_agent.py#L428) | 428 | `"            import httpx  # noqa: F401"` | — |
| [SRC-1AE03B9EC3-L000429](../../agents/web_agent.py#L429) | 429 | `"            search_ready = True"` | — |
| [SRC-1AE03B9EC3-L000430](../../agents/web_agent.py#L430) | 430 | `"        except ImportError:"` | — |
| [SRC-1AE03B9EC3-L000431](../../agents/web_agent.py#L431) | 431 | `"            search_ready = False"` | — |
| [SRC-1AE03B9EC3-L000432](../../agents/web_agent.py#L432) | 432 | `""` | — |
| [SRC-1AE03B9EC3-L000433](../../agents/web_agent.py#L433) | 433 | `"        global_model = os.getenv(\"OMARAI_LLM_MODEL\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000434](../../agents/web_agent.py#L434) | 434 | `"        answer_model = ("` | — |
| [SRC-1AE03B9EC3-L000435](../../agents/web_agent.py#L435) | 435 | `"            os.getenv(\"OMARAI_ANSWER_MODEL\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000436](../../agents/web_agent.py#L436) | 436 | `"            or global_model"` | — |
| [SRC-1AE03B9EC3-L000437](../../agents/web_agent.py#L437) | 437 | `"            or \"google/gemma-4-31b-it:free\""` | — |
| [SRC-1AE03B9EC3-L000438](../../agents/web_agent.py#L438) | 438 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000439](../../agents/web_agent.py#L439) | 439 | `"        planner_model = ("` | — |
| [SRC-1AE03B9EC3-L000440](../../agents/web_agent.py#L440) | 440 | `"            os.getenv(\"OMARAI_PLANNER_MODEL\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000441](../../agents/web_agent.py#L441) | 441 | `"            or global_model"` | — |
| [SRC-1AE03B9EC3-L000442](../../agents/web_agent.py#L442) | 442 | `"            or \"nvidia/nemotron-3-ultra-550b-a55b:free\""` | — |
| [SRC-1AE03B9EC3-L000443](../../agents/web_agent.py#L443) | 443 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000444](../../agents/web_agent.py#L444) | 444 | `"        review_model = os.getenv(\"OMARAI_REVIEW_MODEL\", \"\").strip() or answer_model"` | — |
| [SRC-1AE03B9EC3-L000445](../../agents/web_agent.py#L445) | 445 | `"        fallback_model = ("` | — |
| [SRC-1AE03B9EC3-L000446](../../agents/web_agent.py#L446) | 446 | `"            os.getenv(\"OMARAI_LLM_FALLBACK_MODEL\", \"\").strip() or \"openrouter/free\""` | — |
| [SRC-1AE03B9EC3-L000447](../../agents/web_agent.py#L447) | 447 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000448](../../agents/web_agent.py#L448) | 448 | `"        return {"` | — |
| [SRC-1AE03B9EC3-L000449](../../agents/web_agent.py#L449) | 449 | `"            \"web_search_ready\": search_ready,"` | — |
| [SRC-1AE03B9EC3-L000450](../../agents/web_agent.py#L450) | 450 | `"            \"language_model_configured\": bool("` | — |
| [SRC-1AE03B9EC3-L000451](../../agents/web_agent.py#L451) | 451 | `"                os.getenv(\"OMARAI_LLM_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000452](../../agents/web_agent.py#L452) | 452 | `"                or os.getenv(\"OPENROUTER_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000453](../../agents/web_agent.py#L453) | 453 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L000454](../../agents/web_agent.py#L454) | 454 | `"            \"language_model_provider\": os.getenv("` | — |
| [SRC-1AE03B9EC3-L000455](../../agents/web_agent.py#L455) | 455 | `"                \"OMARAI_LLM_BASE_URL\", \"https://openrouter.ai/api/v1\""` | — |
| [SRC-1AE03B9EC3-L000456](../../agents/web_agent.py#L456) | 456 | `"            ).strip().rstrip(\"/\"),"` | — |
| [SRC-1AE03B9EC3-L000457](../../agents/web_agent.py#L457) | 457 | `"            \"default_model\": answer_model,"` | — |
| [SRC-1AE03B9EC3-L000458](../../agents/web_agent.py#L458) | 458 | `"            \"planner_model\": planner_model,"` | — |
| [SRC-1AE03B9EC3-L000459](../../agents/web_agent.py#L459) | 459 | `"            \"answer_model\": answer_model,"` | — |
| [SRC-1AE03B9EC3-L000460](../../agents/web_agent.py#L460) | 460 | `"            \"review_model\": review_model,"` | — |
| [SRC-1AE03B9EC3-L000461](../../agents/web_agent.py#L461) | 461 | `"            \"fallback_model\": fallback_model,"` | — |
| [SRC-1AE03B9EC3-L000462](../../agents/web_agent.py#L462) | 462 | `"            \"model_selection_mode\": \"role_specific_with_fallback\","` | — |
| [SRC-1AE03B9EC3-L000463](../../agents/web_agent.py#L463) | 463 | `"            \"external_model_privacy_notice\": ("` | — |
| [SRC-1AE03B9EC3-L000464](../../agents/web_agent.py#L464) | 464 | `"                \"Prompts and selected page excerpts are sent to the configured external model provider. \""` | — |
| [SRC-1AE03B9EC3-L000465](../../agents/web_agent.py#L465) | 465 | `"                \"Do not submit secrets or personal/confidential customer data. The default free NVIDIA \""` | — |
| [SRC-1AE03B9EC3-L000466](../../agents/web_agent.py#L466) | 466 | `"                \"Nemotron endpoint states that sessions may be logged for security and product improvement.\""` | — |
| [SRC-1AE03B9EC3-L000467](../../agents/web_agent.py#L467) | 467 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L000468](../../agents/web_agent.py#L468) | 468 | `"            \"search_providers\": ["` | — |
| [SRC-1AE03B9EC3-L000469](../../agents/web_agent.py#L469) | 469 | `"                \"DuckDuckGo HTML\","` | — |
| [SRC-1AE03B9EC3-L000470](../../agents/web_agent.py#L470) | 470 | `"                \"Bing RSS\","` | — |
| [SRC-1AE03B9EC3-L000471](../../agents/web_agent.py#L471) | 471 | `"                \"Google News RSS for fresh queries\","` | — |
| [SRC-1AE03B9EC3-L000472](../../agents/web_agent.py#L472) | 472 | `"                \"DeepSeek Search API when DEEPSEEK_SEARCH_API_KEY is configured (optional; may incur charges)\","` | — |
| [SRC-1AE03B9EC3-L000473](../../agents/web_agent.py#L473) | 473 | `"                \"OpenRouter server-side live web search when OMARAI_OPENROUTER_WEB_SEARCH=1\","` | — |
| [SRC-1AE03B9EC3-L000474](../../agents/web_agent.py#L474) | 474 | `"                \"Brave Search API when BRAVE_SEARCH_API_KEY is configured\","` | — |
| [SRC-1AE03B9EC3-L000475](../../agents/web_agent.py#L475) | 475 | `"                \"Tavily Search API when TAVILY_API_KEY is configured\","` | — |
| [SRC-1AE03B9EC3-L000476](../../agents/web_agent.py#L476) | 476 | `"            ],"` | — |
| [SRC-1AE03B9EC3-L000477](../../agents/web_agent.py#L477) | 477 | `"            \"brave_search_api_configured\": bool(os.getenv(\"BRAVE_SEARCH_API_KEY\", \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L000478](../../agents/web_agent.py#L478) | 478 | `"            \"deepseek_search_api_configured\": bool("` | — |
| [SRC-1AE03B9EC3-L000479](../../agents/web_agent.py#L479) | 479 | `"                os.getenv(\"DEEPSEEK_SEARCH_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000480](../../agents/web_agent.py#L480) | 480 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L000481](../../agents/web_agent.py#L481) | 481 | `"            \"tavily_search_api_configured\": bool(os.getenv(\"TAVILY_API_KEY\", \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L000482](../../agents/web_agent.py#L482) | 482 | `"            \"openrouter_web_search_enabled\": ("` | — |
| [SRC-1AE03B9EC3-L000483](../../agents/web_agent.py#L483) | 483 | `"                os.getenv(\"OMARAI_OPENROUTER_WEB_SEARCH\", \"\").strip() == \"1\""` | — |
| [SRC-1AE03B9EC3-L000484](../../agents/web_agent.py#L484) | 484 | `"                and \"openrouter.ai\" in os.getenv("` | — |
| [SRC-1AE03B9EC3-L000485](../../agents/web_agent.py#L485) | 485 | `"                    \"OMARAI_LLM_BASE_URL\", \"https://openrouter.ai/api/v1\""` | — |
| [SRC-1AE03B9EC3-L000486](../../agents/web_agent.py#L486) | 486 | `"                ).lower()"` | — |
| [SRC-1AE03B9EC3-L000487](../../agents/web_agent.py#L487) | 487 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L000488](../../agents/web_agent.py#L488) | 488 | `"            \"public_social_sources\": ["` | — |
| [SRC-1AE03B9EC3-L000489](../../agents/web_agent.py#L489) | 489 | `"                \"Reddit public RSS and optional authorized Reddit OAuth search\","` | — |
| [SRC-1AE03B9EC3-L000490](../../agents/web_agent.py#L490) | 490 | `"                \"Bluesky public search\","` | — |
| [SRC-1AE03B9EC3-L000491](../../agents/web_agent.py#L491) | 491 | `"                \"indexed public pages from Facebook, Instagram, X, TikTok, LinkedIn, Threads and YouTube\","` | — |
| [SRC-1AE03B9EC3-L000492](../../agents/web_agent.py#L492) | 492 | `"                \"official Instagram public hashtag media when an authorized Graph API token is configured\","` | — |
| [SRC-1AE03B9EC3-L000493](../../agents/web_agent.py#L493) | 493 | `"                \"configured Facebook Pages when a valid authorized page token is configured\","` | — |
| [SRC-1AE03B9EC3-L000494](../../agents/web_agent.py#L494) | 494 | `"                \"official X recent-post API when X_BEARER_TOKEN is configured\","` | — |
| [SRC-1AE03B9EC3-L000495](../../agents/web_agent.py#L495) | 495 | `"            ],"` | — |
| [SRC-1AE03B9EC3-L000496](../../agents/web_agent.py#L496) | 496 | `"            \"reddit_oauth_configured\": bool("` | — |
| [SRC-1AE03B9EC3-L000497](../../agents/web_agent.py#L497) | 497 | `"                os.getenv(\"REDDIT_CLIENT_ID\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000498](../../agents/web_agent.py#L498) | 498 | `"                and os.getenv(\"REDDIT_CLIENT_SECRET\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000499](../../agents/web_agent.py#L499) | 499 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L000500](../../agents/web_agent.py#L500) | 500 | `"            \"facebook_pages_api_configured\": bool("` | — |
| [SRC-1AE03B9EC3-L000501](../../agents/web_agent.py#L501) | 501 | `"                os.getenv(\"FACEBOOK_PAGE_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000502](../../agents/web_agent.py#L502) | 502 | `"                and os.getenv(\"FACEBOOK_PAGE_IDS\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000503](../../agents/web_agent.py#L503) | 503 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L000504](../../agents/web_agent.py#L504) | 504 | `"            \"x_api_configured\": bool(os.getenv(\"X_BEARER_TOKEN\", \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L000505](../../agents/web_agent.py#L505) | 505 | `"            \"instagram_graph_api_configured\": bool("` | — |
| [SRC-1AE03B9EC3-L000506](../../agents/web_agent.py#L506) | 506 | `"                os.getenv(\"INSTAGRAM_USER_ID\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000507](../../agents/web_agent.py#L507) | 507 | `"                and os.getenv(\"INSTAGRAM_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000508](../../agents/web_agent.py#L508) | 508 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L000509](../../agents/web_agent.py#L509) | 509 | `"            \"meta_graph_version\": os.getenv(\"META_GRAPH_VERSION\", \"v25.0\").strip(),"` | — |
| [SRC-1AE03B9EC3-L000510](../../agents/web_agent.py#L510) | 510 | `"            \"youtube_api_configured\": bool(os.getenv(\"YOUTUBE_API_KEY\", \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L000511](../../agents/web_agent.py#L511) | 511 | `"            \"youtube_direct_api\": bool(os.getenv(\"YOUTUBE_API_KEY\", \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L000512](../../agents/web_agent.py#L512) | 512 | `"            \"verification_scope\": {"` | — |
| [SRC-1AE03B9EC3-L000513](../../agents/web_agent.py#L513) | 513 | `"                \"kind\": \"configuration_snapshot\","` | — |
| [SRC-1AE03B9EC3-L000514](../../agents/web_agent.py#L514) | 514 | `"                \"live_network_checks_performed\": False,"` | — |
| [SRC-1AE03B9EC3-L000515](../../agents/web_agent.py#L515) | 515 | `"                \"web_search_ready_means\": \"dependencies_importable_not_provider_connectivity\","` | — |
| [SRC-1AE03B9EC3-L000516](../../agents/web_agent.py#L516) | 516 | `"                \"language_model_configured_means\": \"credential_present_not_successful_completion\","` | — |
| [SRC-1AE03B9EC3-L000517](../../agents/web_agent.py#L517) | 517 | `"                \"search_providers_means\": \"supported_or_conditionally_configured_not_live_verified\","` | — |
| [SRC-1AE03B9EC3-L000518](../../agents/web_agent.py#L518) | 518 | `"                \"direct_social_api_flags_mean\": \"credentials_present_not_permissions_or_connectivity_verified\","` | — |
| [SRC-1AE03B9EC3-L000519](../../agents/web_agent.py#L519) | 519 | `"                \"live_diagnostics_endpoint\": \"POST /api/diagnostics\","` | — |
| [SRC-1AE03B9EC3-L000520](../../agents/web_agent.py#L520) | 520 | `"            },"` | — |
| [SRC-1AE03B9EC3-L000521](../../agents/web_agent.py#L521) | 521 | `"        }"` | — |
| [SRC-1AE03B9EC3-L000522](../../agents/web_agent.py#L522) | 522 | `""` | — |
| [SRC-1AE03B9EC3-L000523](../../agents/web_agent.py#L523) | 523 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000524](../../agents/web_agent.py#L524) | 524 | `"    def _unwrap_search_url(value: str) -> str:"` | — |
| [SRC-1AE03B9EC3-L000525](../../agents/web_agent.py#L525) | 525 | `"        if value.startswith(\"//\"):"` | — |
| [SRC-1AE03B9EC3-L000526](../../agents/web_agent.py#L526) | 526 | `"            value = \"https:\" + value"` | — |
| [SRC-1AE03B9EC3-L000527](../../agents/web_agent.py#L527) | 527 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L000528](../../agents/web_agent.py#L528) | 528 | `"            parsed = urllib.parse.urlparse(value)"` | — |
| [SRC-1AE03B9EC3-L000529](../../agents/web_agent.py#L529) | 529 | `"            host = (parsed.hostname or \"\").lower()"` | — |
| [SRC-1AE03B9EC3-L000530](../../agents/web_agent.py#L530) | 530 | `"            if host.endswith(\"duckduckgo.com\") and parsed.path.startswith(\"/l/\"):"` | — |
| [SRC-1AE03B9EC3-L000531](../../agents/web_agent.py#L531) | 531 | `"                target = urllib.parse.parse_qs(parsed.query).get(\"uddg\", [\"\"])[0]"` | — |
| [SRC-1AE03B9EC3-L000532](../../agents/web_agent.py#L532) | 532 | `"                return urllib.parse.unquote(target) if target else \"\""` | — |
| [SRC-1AE03B9EC3-L000533](../../agents/web_agent.py#L533) | 533 | `"        except (ValueError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L000534](../../agents/web_agent.py#L534) | 534 | `"            return \"\""` | — |
| [SRC-1AE03B9EC3-L000535](../../agents/web_agent.py#L535) | 535 | `"        return value"` | — |
| [SRC-1AE03B9EC3-L000536](../../agents/web_agent.py#L536) | 536 | `""` | — |
| [SRC-1AE03B9EC3-L000537](../../agents/web_agent.py#L537) | 537 | `"    def _record_provider_diagnostic("` | — |
| [SRC-1AE03B9EC3-L000538](../../agents/web_agent.py#L538) | 538 | `"        self, provider: str, query: str, status: str, result_count: int = 0,"` | — |
| [SRC-1AE03B9EC3-L000539](../../agents/web_agent.py#L539) | 539 | `"        rejected_count: int = 0, error: str \| None = None,"` | — |
| [SRC-1AE03B9EC3-L000540](../../agents/web_agent.py#L540) | 540 | `"        accepted_count: int \| None = None,"` | — |
| [SRC-1AE03B9EC3-L000541](../../agents/web_agent.py#L541) | 541 | `"        rejection_counts: dict[str, int] \| None = None,"` | — |
| [SRC-1AE03B9EC3-L000542](../../agents/web_agent.py#L542) | 542 | `"    ) -> None:"` | — |
| [SRC-1AE03B9EC3-L000543](../../agents/web_agent.py#L543) | 543 | `"        def redact(value: Any, limit: int) -> str:"` | — |
| [SRC-1AE03B9EC3-L000544](../../agents/web_agent.py#L544) | 544 | `"            safe = _clean_text(str(value or \"\"), limit)"` | — |
| [SRC-1AE03B9EC3-L000545](../../agents/web_agent.py#L545) | 545 | `"            safe = re.sub("` | — |
| [SRC-1AE03B9EC3-L000546](../../agents/web_agent.py#L546) | 546 | `"                r\"(?i)(bearer\\s+)[A-Za-z0-9._~+/-]+=*\","` | — |
| [SRC-1AE03B9EC3-L000547](../../agents/web_agent.py#L547) | 547 | `"                r\"\\1[REDACTED]\","` | — |
| [SRC-1AE03B9EC3-L000548](../../agents/web_agent.py#L548) | 548 | `"                safe,"` | — |
| [SRC-1AE03B9EC3-L000549](../../agents/web_agent.py#L549) | 549 | `"            )"` | — |
| [SRC-1AE03B9EC3-L000550](../../agents/web_agent.py#L550) | 550 | `"            safe = re.sub("` | — |
| [SRC-1AE03B9EC3-L000551](../../agents/web_agent.py#L551) | 551 | `"                r\"(?i)\\b(api[_-]?key\|access[_-]?token\|refresh[_-]?token\|token\|secret\|password)\\s*[:=]\\s*[^\\s,;]+\","` | — |
| [SRC-1AE03B9EC3-L000552](../../agents/web_agent.py#L552) | 552 | `"                r\"\\1=[REDACTED]\","` | — |
| [SRC-1AE03B9EC3-L000553](../../agents/web_agent.py#L553) | 553 | `"                safe,"` | — |
| [SRC-1AE03B9EC3-L000554](../../agents/web_agent.py#L554) | 554 | `"            )"` | — |
| [SRC-1AE03B9EC3-L000555](../../agents/web_agent.py#L555) | 555 | `"            safe = re.sub("` | — |
| [SRC-1AE03B9EC3-L000556](../../agents/web_agent.py#L556) | 556 | `"                r\"(?i)([?&](?:api[_-]?key\|access[_-]?token\|token\|key)=)[^&\\s]+\","` | — |
| [SRC-1AE03B9EC3-L000557](../../agents/web_agent.py#L557) | 557 | `"                r\"\\1[REDACTED]\","` | — |
| [SRC-1AE03B9EC3-L000558](../../agents/web_agent.py#L558) | 558 | `"                safe,"` | — |
| [SRC-1AE03B9EC3-L000559](../../agents/web_agent.py#L559) | 559 | `"            )"` | — |
| [SRC-1AE03B9EC3-L000560](../../agents/web_agent.py#L560) | 560 | `"            return safe[:limit]"` | — |
| [SRC-1AE03B9EC3-L000561](../../agents/web_agent.py#L561) | 561 | `""` | — |
| [SRC-1AE03B9EC3-L000562](../../agents/web_agent.py#L562) | 562 | `"        record = {"` | — |
| [SRC-1AE03B9EC3-L000563](../../agents/web_agent.py#L563) | 563 | `"            \"provider\": provider,"` | — |
| [SRC-1AE03B9EC3-L000564](../../agents/web_agent.py#L564) | 564 | `"            \"query\": redact(query, 220),"` | — |
| [SRC-1AE03B9EC3-L000565](../../agents/web_agent.py#L565) | 565 | `"            \"status\": status,"` | — |
| [SRC-1AE03B9EC3-L000566](../../agents/web_agent.py#L566) | 566 | `"            \"result_count\": int(result_count),"` | — |
| [SRC-1AE03B9EC3-L000567](../../agents/web_agent.py#L567) | 567 | `"            \"accepted_count\": int(result_count if accepted_count is None else accepted_count),"` | — |
| [SRC-1AE03B9EC3-L000568](../../agents/web_agent.py#L568) | 568 | `"            \"rejected_count\": int(rejected_count),"` | — |
| [SRC-1AE03B9EC3-L000569](../../agents/web_agent.py#L569) | 569 | `"        }"` | — |
| [SRC-1AE03B9EC3-L000570](../../agents/web_agent.py#L570) | 570 | `"        if isinstance(rejection_counts, dict):"` | — |
| [SRC-1AE03B9EC3-L000571](../../agents/web_agent.py#L571) | 571 | `"            safe_counts: dict[str, int] = {}"` | — |
| [SRC-1AE03B9EC3-L000572](../../agents/web_agent.py#L572) | 572 | `"            for reason in _PROVIDER_REJECTION_REASONS:"` | — |
| [SRC-1AE03B9EC3-L000573](../../agents/web_agent.py#L573) | 573 | `"                try:"` | — |
| [SRC-1AE03B9EC3-L000574](../../agents/web_agent.py#L574) | 574 | `"                    safe_counts[reason] = max(0, int(rejection_counts.get(reason, 0) or 0))"` | — |
| [SRC-1AE03B9EC3-L000575](../../agents/web_agent.py#L575) | 575 | `"                except (TypeError, ValueError, OverflowError):"` | — |
| [SRC-1AE03B9EC3-L000576](../../agents/web_agent.py#L576) | 576 | `"                    safe_counts[reason] = 0"` | — |
| [SRC-1AE03B9EC3-L000577](../../agents/web_agent.py#L577) | 577 | `"            record[\"rejection_counts\"] = safe_counts"` | — |
| [SRC-1AE03B9EC3-L000578](../../agents/web_agent.py#L578) | 578 | `"        if error:"` | — |
| [SRC-1AE03B9EC3-L000579](../../agents/web_agent.py#L579) | 579 | `"            record[\"error\"] = redact(error, 180)"` | — |
| [SRC-1AE03B9EC3-L000580](../../agents/web_agent.py#L580) | 580 | `"        with self._provider_diagnostics_lock:"` | — |
| [SRC-1AE03B9EC3-L000581](../../agents/web_agent.py#L581) | 581 | `"            self._provider_diagnostics.append(record)"` | — |
| [SRC-1AE03B9EC3-L000582](../../agents/web_agent.py#L582) | 582 | `"            # Bound memory when the instance serves many user requests."` | — |
| [SRC-1AE03B9EC3-L000583](../../agents/web_agent.py#L583) | 583 | `"            self._provider_diagnostics = self._provider_diagnostics[-160:]"` | — |
| [SRC-1AE03B9EC3-L000584](../../agents/web_agent.py#L584) | 584 | `""` | — |
| [SRC-1AE03B9EC3-L000585](../../agents/web_agent.py#L585) | 585 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000586](../../agents/web_agent.py#L586) | 586 | `"    def _source_matches_query(query: str, source: dict[str, Any]) -> bool:"` | — |
| [SRC-1AE03B9EC3-L000587](../../agents/web_agent.py#L587) | 587 | `"        if \"user_supplied_url\" in source.get(\"providers\", []):"` | — |
| [SRC-1AE03B9EC3-L000588](../../agents/web_agent.py#L588) | 588 | `"            return True"` | — |
| [SRC-1AE03B9EC3-L000589](../../agents/web_agent.py#L589) | 589 | `"        evidence = \" \".join("` | — |
| [SRC-1AE03B9EC3-L000590](../../agents/web_agent.py#L590) | 590 | `"            str(source.get(key) or \"\")"` | — |
| [SRC-1AE03B9EC3-L000591](../../agents/web_agent.py#L591) | 591 | `"            for key in (\"title\", \"snippet\", \"page_text\")"` | — |
| [SRC-1AE03B9EC3-L000592](../../agents/web_agent.py#L592) | 592 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000593](../../agents/web_agent.py#L593) | 593 | `"        return _relevance_ratio(query, evidence) >= 0.20"` | — |
| [SRC-1AE03B9EC3-L000594](../../agents/web_agent.py#L594) | 594 | `""` | — |
| [SRC-1AE03B9EC3-L000595](../../agents/web_agent.py#L595) | 595 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000596](../../agents/web_agent.py#L596) | 596 | `"    def _normalized_source_url_key(value: Any) -> str:"` | — |
| [SRC-1AE03B9EC3-L000597](../../agents/web_agent.py#L597) | 597 | `"        \"\"\"Normalize a public HTTP(S) URL for duplicate detection across search rounds.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000598](../../agents/web_agent.py#L598) | 598 | `"        if not isinstance(value, str) or not value.strip():"` | — |
| [SRC-1AE03B9EC3-L000599](../../agents/web_agent.py#L599) | 599 | `"            return \"\""` | — |
| [SRC-1AE03B9EC3-L000600](../../agents/web_agent.py#L600) | 600 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L000601](../../agents/web_agent.py#L601) | 601 | `"            parsed = urllib.parse.urlsplit(value.strip())"` | — |
| [SRC-1AE03B9EC3-L000602](../../agents/web_agent.py#L602) | 602 | `"            scheme = parsed.scheme.lower()"` | — |
| [SRC-1AE03B9EC3-L000603](../../agents/web_agent.py#L603) | 603 | `"            if scheme not in {\"http\", \"https\"} or not parsed.hostname:"` | — |
| [SRC-1AE03B9EC3-L000604](../../agents/web_agent.py#L604) | 604 | `"                return \"\""` | — |
| [SRC-1AE03B9EC3-L000605](../../agents/web_agent.py#L605) | 605 | `"            host = parsed.hostname.lower().rstrip(\".\")"` | — |
| [SRC-1AE03B9EC3-L000606](../../agents/web_agent.py#L606) | 606 | `"            port = parsed.port"` | — |
| [SRC-1AE03B9EC3-L000607](../../agents/web_agent.py#L607) | 607 | `"            if (scheme == \"https\" and port == 443) or (scheme == \"http\" and port == 80):"` | — |
| [SRC-1AE03B9EC3-L000608](../../agents/web_agent.py#L608) | 608 | `"                port = None"` | — |
| [SRC-1AE03B9EC3-L000609](../../agents/web_agent.py#L609) | 609 | `"            host_for_url = f\"[{host}]\" if \":\" in host else host"` | — |
| [SRC-1AE03B9EC3-L000610](../../agents/web_agent.py#L610) | 610 | `"            netloc = host_for_url + (f\":{port}\" if port is not None else \"\")"` | — |
| [SRC-1AE03B9EC3-L000611](../../agents/web_agent.py#L611) | 611 | `"            path = parsed.path.rstrip(\"/\") or \"/\""` | — |
| [SRC-1AE03B9EC3-L000612](../../agents/web_agent.py#L612) | 612 | `"            tracking_keys = {\"fbclid\", \"gclid\", \"ref\", \"source\"}"` | — |
| [SRC-1AE03B9EC3-L000613](../../agents/web_agent.py#L613) | 613 | `"            query_items = ["` | — |
| [SRC-1AE03B9EC3-L000614](../../agents/web_agent.py#L614) | 614 | `"                (key, item)"` | — |
| [SRC-1AE03B9EC3-L000615](../../agents/web_agent.py#L615) | 615 | `"                for key, item in urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)"` | — |
| [SRC-1AE03B9EC3-L000616](../../agents/web_agent.py#L616) | 616 | `"                if not key.lower().startswith(\"utm_\") and key.lower() not in tracking_keys"` | — |
| [SRC-1AE03B9EC3-L000617](../../agents/web_agent.py#L617) | 617 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L000618](../../agents/web_agent.py#L618) | 618 | `"            query = urllib.parse.urlencode(query_items, doseq=True)"` | — |
| [SRC-1AE03B9EC3-L000619](../../agents/web_agent.py#L619) | 619 | `"            return urllib.parse.urlunsplit((scheme, netloc, path, query, \"\"))"` | — |
| [SRC-1AE03B9EC3-L000620](../../agents/web_agent.py#L620) | 620 | `"        except (TypeError, ValueError):"` | — |
| [SRC-1AE03B9EC3-L000621](../../agents/web_agent.py#L621) | 621 | `"            return \"\""` | — |
| [SRC-1AE03B9EC3-L000622](../../agents/web_agent.py#L622) | 622 | `""` | — |
| [SRC-1AE03B9EC3-L000623](../../agents/web_agent.py#L623) | 623 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000624](../../agents/web_agent.py#L624) | 624 | `"    def _question_coverage_targets(question: str) -> list[str]:"` | — |
| [SRC-1AE03B9EC3-L000625](../../agents/web_agent.py#L625) | 625 | `"        \"\"\"Compatibility wrapper for the shared deterministic requirement extractor.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000626](../../agents/web_agent.py#L626) | 626 | `"        return extract_question_coverage_targets(question)"` | — |
| [SRC-1AE03B9EC3-L000627](../../agents/web_agent.py#L627) | 627 | `""` | — |
| [SRC-1AE03B9EC3-L000628](../../agents/web_agent.py#L628) | 628 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000629](../../agents/web_agent.py#L629) | 629 | `"    def _is_current_search_status_question(question: str) -> bool:"` | — |
| [SRC-1AE03B9EC3-L000630](../../agents/web_agent.py#L630) | 630 | `"        \"\"\"Recognize a question about whether this answer already used web search.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000631](../../agents/web_agent.py#L631) | 631 | `"        value = _normalize_search_query(question).casefold()"` | — |
| [SRC-1AE03B9EC3-L000632](../../agents/web_agent.py#L632) | 632 | `"        asks_if_searched = any("` | — |
| [SRC-1AE03B9EC3-L000633](../../agents/web_agent.py#L633) | 633 | `"            term in value"` | — |
| [SRC-1AE03B9EC3-L000634](../../agents/web_agent.py#L634) | 634 | `"            for term in (\"بحثت\", \"اجريت بحث\", \"قمت بالبحث\", \"عملت بحث\", \"did you search\", \"did you browse\")"` | — |
| [SRC-1AE03B9EC3-L000635](../../agents/web_agent.py#L635) | 635 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000636](../../agents/web_agent.py#L636) | 636 | `"        references_web = any("` | — |
| [SRC-1AE03B9EC3-L000637](../../agents/web_agent.py#L637) | 637 | `"            term in value for term in (\"انترنت\", \"النت\", \"الويب\", \"ويب\", \"the web\", \"online\")"` | — |
| [SRC-1AE03B9EC3-L000638](../../agents/web_agent.py#L638) | 638 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000639](../../agents/web_agent.py#L639) | 639 | `"        references_current_answer = any("` | — |
| [SRC-1AE03B9EC3-L000640](../../agents/web_agent.py#L640) | 640 | `"            term in value"` | — |
| [SRC-1AE03B9EC3-L000641](../../agents/web_agent.py#L641) | 641 | `"            for term in ("` | — |
| [SRC-1AE03B9EC3-L000642](../../agents/web_agent.py#L642) | 642 | `"                \"اجاب\", \"الرد الحالي\", \"هذا السؤال\", \"هذه الاجابه\","` | — |
| [SRC-1AE03B9EC3-L000643](../../agents/web_agent.py#L643) | 643 | `"                \"this answer\", \"this response\","` | — |
| [SRC-1AE03B9EC3-L000644](../../agents/web_agent.py#L644) | 644 | `"            )"` | — |
