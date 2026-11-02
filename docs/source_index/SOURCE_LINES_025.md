# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **025**
- سجلات الأسطر: **800**
- النطاق: SRC-E599346ABE-L001605 إلى SRC-21D5D044E2-L000038
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## وثائق وفهرسة

### FILE-E599346ABE — [docs/generate_index.py](../generate_index.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-E599346ABE-L001605](../generate_index.py#L1605) | 1605 | `"        \"\","` | — |
| [SRC-E599346ABE-L001606](../generate_index.py#L1606) | 1606 | `"        f\"- ملفات المستودع في الجرد: **{len(file_inventory)}**\","` | — |
| [SRC-E599346ABE-L001607](../generate_index.py#L1607) | 1607 | `"        f\"- ملفات Python المحللة: **{files_scanned}**\","` | — |
| [SRC-E599346ABE-L001608](../generate_index.py#L1608) | 1608 | `"        f\"- تعريفات Python المفهرسة: **{len(symbols)}**\","` | — |
| [SRC-E599346ABE-L001609](../generate_index.py#L1609) | 1609 | `"        f\"- تعريفات Python موثقة بوجود Docstring: **{documented_count}**\","` | — |
| [SRC-E599346ABE-L001610](../generate_index.py#L1610) | 1610 | `"        f\"- تعريفات Python بلا Docstring: **{missing_count}**\","` | — |
| [SRC-E599346ABE-L001611](../generate_index.py#L1611) | 1611 | `"        f\"- تعريفات لا ينطبق عليها Docstring: **{not_applicable_count}**\","` | — |
| [SRC-E599346ABE-L001612](../generate_index.py#L1612) | 1612 | `"        f\"- الرموز الساكنة الإضافية: **{len(marker_inventory)}**\","` | — |
| [SRC-E599346ABE-L001613](../generate_index.py#L1613) | 1613 | `"        f\"- الأسطر النصية المفهرسة حرفيًا: **{len(line_inventory)}**\","` | — |
| [SRC-E599346ABE-L001614](../generate_index.py#L1614) | 1614 | `"        f\"- وسوم المراجعة/الإصلاح المسجلة: **{len(finding_inventory)}**\","` | — |
| [SRC-E599346ABE-L001615](../generate_index.py#L1615) | 1615 | `"        \"\","` | — |
| [SRC-E599346ABE-L001616](../generate_index.py#L1616) | 1616 | `"        \"- فهرس الأسطر الكامل: [SOURCE LINES INDEX](SOURCE_LINES_INDEX.md)\","` | — |
| [SRC-E599346ABE-L001617](../generate_index.py#L1617) | 1617 | `"        \"- تدقيق التغطية والاستثناءات: [INDEX COVERAGE AUDIT](INDEX_COVERAGE_AUDIT.md)\","` | — |
| [SRC-E599346ABE-L001618](../generate_index.py#L1618) | 1618 | `"        \"- كل سجل سطر يحمل معرّفًا من الشكل SRC-<FILEHASH>-L000001.\","` | — |
| [SRC-E599346ABE-L001619](../generate_index.py#L1619) | 1619 | `"        \"\","` | — |
| [SRC-E599346ABE-L001620](../generate_index.py#L1620) | 1620 | `"        \"## جرد ملفات المستودع\","` | — |
| [SRC-E599346ABE-L001621](../generate_index.py#L1621) | 1621 | `"        \"\","` | — |
| [SRC-E599346ABE-L001622](../generate_index.py#L1622) | 1622 | `"        (\"يشمل الملفات المؤهلة من الشفرة والواجهة والاختبارات والوثائق والإعدادات وCI. \""` | — |
| [SRC-E599346ABE-L001623](../generate_index.py#L1623) | 1623 | `"        \"يُستثنى ملف الفهرس المولّد نفسه لتجنب الحلقة الذاتية، كما تُستثنى المجلدات المولّدة \""` | — |
| [SRC-E599346ABE-L001624](../generate_index.py#L1624) | 1624 | `"        \"والبيئات والملفات المحلية الحساسة وقواعد البيانات والمفاتيح المعروفة.\"),"` | — |
| [SRC-E599346ABE-L001625](../generate_index.py#L1625) | 1625 | `"        \"\","` | — |
| [SRC-E599346ABE-L001626](../generate_index.py#L1626) | 1626 | `"        \"\| معرّف الملف \| التصنيف \| الملف \| النوع \| الحجم (بايت) \| عدد الأسطر \| نطاق الفهرسة \|\","` | — |
| [SRC-E599346ABE-L001627](../generate_index.py#L1627) | 1627 | `"        \"\|---\|---\|---\|---\|---:\|---:\|---\|\","` | — |
| [SRC-E599346ABE-L001628](../generate_index.py#L1628) | 1628 | `"    ]"` | — |
| [SRC-E599346ABE-L001629](../generate_index.py#L1629) | 1629 | `""` | — |
| [SRC-E599346ABE-L001630](../generate_index.py#L1630) | 1630 | `"    if file_inventory:"` | — |
| [SRC-E599346ABE-L001631](../generate_index.py#L1631) | 1631 | `"        for item in file_inventory:"` | — |
| [SRC-E599346ABE-L001632](../generate_index.py#L1632) | 1632 | `"            line_count = str(item.line_count) if item.line_count is not None else \"غير متاح\""` | — |
| [SRC-E599346ABE-L001633](../generate_index.py#L1633) | 1633 | `"            lines.append("` | — |
| [SRC-E599346ABE-L001634](../generate_index.py#L1634) | 1634 | `"                \"\| \""` | — |
| [SRC-E599346ABE-L001635](../generate_index.py#L1635) | 1635 | `"                + \" \| \".join("` | — |
| [SRC-E599346ABE-L001636](../generate_index.py#L1636) | 1636 | `"                    ("` | — |
| [SRC-E599346ABE-L001637](../generate_index.py#L1637) | 1637 | `"                        item.file_id,"` | — |
| [SRC-E599346ABE-L001638](../generate_index.py#L1638) | 1638 | `"                        _markdown_cell(item.category),"` | — |
| [SRC-E599346ABE-L001639](../generate_index.py#L1639) | 1639 | `"                        f\"[{_markdown_cell(item.file)}]({_source_file_href(item.file)})\","` | — |
| [SRC-E599346ABE-L001640](../generate_index.py#L1640) | 1640 | `"                        _markdown_cell(item.file_type),"` | — |
| [SRC-E599346ABE-L001641](../generate_index.py#L1641) | 1641 | `"                        str(item.size_bytes),"` | — |
| [SRC-E599346ABE-L001642](../generate_index.py#L1642) | 1642 | `"                        line_count,"` | — |
| [SRC-E599346ABE-L001643](../generate_index.py#L1643) | 1643 | `"                        _markdown_cell(item.indexing_scope),"` | — |
| [SRC-E599346ABE-L001644](../generate_index.py#L1644) | 1644 | `"                    )"` | — |
| [SRC-E599346ABE-L001645](../generate_index.py#L1645) | 1645 | `"                )"` | — |
| [SRC-E599346ABE-L001646](../generate_index.py#L1646) | 1646 | `"                + \" \|\""` | — |
| [SRC-E599346ABE-L001647](../generate_index.py#L1647) | 1647 | `"            )"` | — |
| [SRC-E599346ABE-L001648](../generate_index.py#L1648) | 1648 | `"    else:"` | — |
| [SRC-E599346ABE-L001649](../generate_index.py#L1649) | 1649 | `"        lines.append(\"\| — \| — \| — \| — \| — \| — \| لم يُمرر جرد ملفات إلى المولّد. \|\")"` | — |
| [SRC-E599346ABE-L001650](../generate_index.py#L1650) | 1650 | `""` | — |
| [SRC-E599346ABE-L001651](../generate_index.py#L1651) | 1651 | `"    lines.extend("` | — |
| [SRC-E599346ABE-L001652](../generate_index.py#L1652) | 1652 | `"        ["` | — |
| [SRC-E599346ABE-L001653](../generate_index.py#L1653) | 1653 | `"            \"\","` | — |
| [SRC-E599346ABE-L001654](../generate_index.py#L1654) | 1654 | `"            \"## تعريفات Python من AST\","` | — |
| [SRC-E599346ABE-L001655](../generate_index.py#L1655) | 1655 | `"            \"\","` | — |
| [SRC-E599346ABE-L001656](../generate_index.py#L1656) | 1656 | `"            (\"> تُحسب حالة Docstring للدوال والكلاسات فقط. المتغيرات والثوابت لا تُصنّف \""` | — |
| [SRC-E599346ABE-L001657](../generate_index.py#L1657) | 1657 | `"            \"على أنها موثقة أو ناقصة Docstring.\"),"` | — |
| [SRC-E599346ABE-L001658](../generate_index.py#L1658) | 1658 | `"            \"\","` | — |
| [SRC-E599346ABE-L001659](../generate_index.py#L1659) | 1659 | `"            \"\| الملف \| النوع \| الاسم المؤهل \| الوصف \| حالة Docstring \| السطر \| كود السطر للوصول المباشر \|\","` | — |
| [SRC-E599346ABE-L001660](../generate_index.py#L1660) | 1660 | `"            \"\|---\|---\|---\|---\|---\|---:\|---\|\","` | — |
| [SRC-E599346ABE-L001661](../generate_index.py#L1661) | 1661 | `"        ]"` | — |
| [SRC-E599346ABE-L001662](../generate_index.py#L1662) | 1662 | `"    )"` | — |
| [SRC-E599346ABE-L001663](../generate_index.py#L1663) | 1663 | `""` | — |
| [SRC-E599346ABE-L001664](../generate_index.py#L1664) | 1664 | `"    if not symbols:"` | — |
| [SRC-E599346ABE-L001665](../generate_index.py#L1665) | 1665 | `"        lines.append(\"\| — \| — \| — \| لا توجد تعريفات Python في الملفات المؤهلة. \| — \| — \| — \|\")"` | — |
| [SRC-E599346ABE-L001666](../generate_index.py#L1666) | 1666 | `"    else:"` | — |
| [SRC-E599346ABE-L001667](../generate_index.py#L1667) | 1667 | `"        for symbol in symbols:"` | — |
| [SRC-E599346ABE-L001668](../generate_index.py#L1668) | 1668 | `"            if symbol.documented is True:"` | — |
| [SRC-E599346ABE-L001669](../generate_index.py#L1669) | 1669 | `"                status = \"موثق\""` | — |
| [SRC-E599346ABE-L001670](../generate_index.py#L1670) | 1670 | `"            elif symbol.documented is False:"` | — |
| [SRC-E599346ABE-L001671](../generate_index.py#L1671) | 1671 | `"                status = \"ناقص\""` | — |
| [SRC-E599346ABE-L001672](../generate_index.py#L1672) | 1672 | `"            else:"` | — |
| [SRC-E599346ABE-L001673](../generate_index.py#L1673) | 1673 | `"                status = \"لا ينطبق\""` | — |
| [SRC-E599346ABE-L001674](../generate_index.py#L1674) | 1674 | `"            lines.append("` | — |
| [SRC-E599346ABE-L001675](../generate_index.py#L1675) | 1675 | `"                \"\| \""` | — |
| [SRC-E599346ABE-L001676](../generate_index.py#L1676) | 1676 | `"                + \" \| \".join("` | — |
| [SRC-E599346ABE-L001677](../generate_index.py#L1677) | 1677 | `"                    ("` | — |
| [SRC-E599346ABE-L001678](../generate_index.py#L1678) | 1678 | `"                        f\"[{_markdown_cell(symbol.file)}]({_source_file_href(symbol.file, symbol.line)})\","` | — |
| [SRC-E599346ABE-L001679](../generate_index.py#L1679) | 1679 | `"                        _markdown_cell(symbol.kind),"` | — |
| [SRC-E599346ABE-L001680](../generate_index.py#L1680) | 1680 | `"                        _markdown_cell(symbol.name),"` | — |
| [SRC-E599346ABE-L001681](../generate_index.py#L1681) | 1681 | `"                        _markdown_cell(symbol.description),"` | — |
| [SRC-E599346ABE-L001682](../generate_index.py#L1682) | 1682 | `"                        status,"` | — |
| [SRC-E599346ABE-L001683](../generate_index.py#L1683) | 1683 | `"                        str(symbol.line),"` | — |
| [SRC-E599346ABE-L001684](../generate_index.py#L1684) | 1684 | `"                        f\"[{_source_line_id(symbol.file, symbol.line)}]({_source_file_href(symbol.file, symbol.line)})\","` | — |
| [SRC-E599346ABE-L001685](../generate_index.py#L1685) | 1685 | `"                    )"` | — |
| [SRC-E599346ABE-L001686](../generate_index.py#L1686) | 1686 | `"                )"` | — |
| [SRC-E599346ABE-L001687](../generate_index.py#L1687) | 1687 | `"                + \" \|\""` | — |
| [SRC-E599346ABE-L001688](../generate_index.py#L1688) | 1688 | `"            )"` | — |
| [SRC-E599346ABE-L001689](../generate_index.py#L1689) | 1689 | `""` | — |
| [SRC-E599346ABE-L001690](../generate_index.py#L1690) | 1690 | `"    lines.extend("` | — |
| [SRC-E599346ABE-L001691](../generate_index.py#L1691) | 1691 | `"        ["` | — |
| [SRC-E599346ABE-L001692](../generate_index.py#L1692) | 1692 | `"            \"\","` | — |
| [SRC-E599346ABE-L001693](../generate_index.py#L1693) | 1693 | `"            \"## الرموز الساكنة الإضافية\","` | — |
| [SRC-E599346ABE-L001694](../generate_index.py#L1694) | 1694 | `"            \"\","` | — |
| [SRC-E599346ABE-L001695](../generate_index.py#L1695) | 1695 | `"            (\"هذا القسم للمساعدة في الوصول إلى الواجهة والإعدادات والوثائق؛ \""` | — |
| [SRC-E599346ABE-L001696](../generate_index.py#L1696) | 1696 | `"            \"استخراج الرموز غير المحللة بـAST استدلالي وقد لا يساوي تحليلًا كاملًا للغة.\"),"` | — |
| [SRC-E599346ABE-L001697](../generate_index.py#L1697) | 1697 | `"            \"\","` | — |
| [SRC-E599346ABE-L001698](../generate_index.py#L1698) | 1698 | `"            \"\| الملف \| نوع الرمز \| الاسم/القيمة \| السطر \| كود السطر للوصول المباشر \|\","` | — |
| [SRC-E599346ABE-L001699](../generate_index.py#L1699) | 1699 | `"            \"\|---\|---\|---\|---:\|---\|\","` | — |
| [SRC-E599346ABE-L001700](../generate_index.py#L1700) | 1700 | `"        ]"` | — |
| [SRC-E599346ABE-L001701](../generate_index.py#L1701) | 1701 | `"    )"` | — |
| [SRC-E599346ABE-L001702](../generate_index.py#L1702) | 1702 | `"    if marker_inventory:"` | — |
| [SRC-E599346ABE-L001703](../generate_index.py#L1703) | 1703 | `"        for marker in marker_inventory:"` | — |
| [SRC-E599346ABE-L001704](../generate_index.py#L1704) | 1704 | `"            lines.append("` | — |
| [SRC-E599346ABE-L001705](../generate_index.py#L1705) | 1705 | `"                \"\| \""` | — |
| [SRC-E599346ABE-L001706](../generate_index.py#L1706) | 1706 | `"                + \" \| \".join("` | — |
| [SRC-E599346ABE-L001707](../generate_index.py#L1707) | 1707 | `"                    ("` | — |
| [SRC-E599346ABE-L001708](../generate_index.py#L1708) | 1708 | `"                        f\"[{_markdown_cell(marker.file)}]({_source_file_href(marker.file, marker.line)})\","` | — |
| [SRC-E599346ABE-L001709](../generate_index.py#L1709) | 1709 | `"                        _markdown_cell(marker.kind),"` | — |
| [SRC-E599346ABE-L001710](../generate_index.py#L1710) | 1710 | `"                        _markdown_cell(marker.name),"` | — |
| [SRC-E599346ABE-L001711](../generate_index.py#L1711) | 1711 | `"                        str(marker.line),"` | — |
| [SRC-E599346ABE-L001712](../generate_index.py#L1712) | 1712 | `"                        f\"[{_source_line_id(marker.file, marker.line)}]({_source_file_href(marker.file, marker.line)})\","` | — |
| [SRC-E599346ABE-L001713](../generate_index.py#L1713) | 1713 | `"                    )"` | — |
| [SRC-E599346ABE-L001714](../generate_index.py#L1714) | 1714 | `"                )"` | — |
| [SRC-E599346ABE-L001715](../generate_index.py#L1715) | 1715 | `"                + \" \|\""` | — |
| [SRC-E599346ABE-L001716](../generate_index.py#L1716) | 1716 | `"            )"` | — |
| [SRC-E599346ABE-L001717](../generate_index.py#L1717) | 1717 | `"    else:"` | — |
| [SRC-E599346ABE-L001718](../generate_index.py#L1718) | 1718 | `"        lines.append(\"\| — \| — \| — \| لم تُكتشف رموز ساكنة إضافية. \| — \|\")"` | — |
| [SRC-E599346ABE-L001719](../generate_index.py#L1719) | 1719 | `""` | — |
| [SRC-E599346ABE-L001720](../generate_index.py#L1720) | 1720 | `"    lines.extend("` | — |
| [SRC-E599346ABE-L001721](../generate_index.py#L1721) | 1721 | `"        ["` | — |
| [SRC-E599346ABE-L001722](../generate_index.py#L1722) | 1722 | `"            \"\","` | — |
| [SRC-E599346ABE-L001723](../generate_index.py#L1723) | 1723 | `"            \"## سجل وسوم المراجعة والإصلاح\","` | — |
| [SRC-E599346ABE-L001724](../generate_index.py#L1724) | 1724 | `"            \"\","` | — |
| [SRC-E599346ABE-L001725](../generate_index.py#L1725) | 1725 | `"            \"هذه قائمة بالوسوم الصريحة التي تستدعي المتابعة. وجود الوسم ليس إثباتًا آليًا أن السطر معيب؛ افتح الملف عند رقم السطر وراجع السياق.\","` | — |
| [SRC-E599346ABE-L001726](../generate_index.py#L1726) | 1726 | `"            \"\","` | — |
| [SRC-E599346ABE-L001727](../generate_index.py#L1727) | 1727 | `"            \"\| كود الهفوة/الوسم \| النوع \| الملف \| السطر \| وصف الوسم \| كود السطر \| نص السطر \|\","` | — |
| [SRC-E599346ABE-L001728](../generate_index.py#L1728) | 1728 | `"            \"\|---\|---\|---\|---:\|---\|---\|---\|\","` | — |
| [SRC-E599346ABE-L001729](../generate_index.py#L1729) | 1729 | `"        ]"` | — |
| [SRC-E599346ABE-L001730](../generate_index.py#L1730) | 1730 | `"    )"` | — |
| [SRC-E599346ABE-L001731](../generate_index.py#L1731) | 1731 | `"    if finding_inventory:"` | — |
| [SRC-E599346ABE-L001732](../generate_index.py#L1732) | 1732 | `"        line_map = {source_line.line_id: source_line for source_line in line_inventory}"` | — |
| [SRC-E599346ABE-L001733](../generate_index.py#L1733) | 1733 | `"        for finding in finding_inventory:"` | — |
| [SRC-E599346ABE-L001734](../generate_index.py#L1734) | 1734 | `"            source_line = line_map.get(finding.line_id)"` | — |
| [SRC-E599346ABE-L001735](../generate_index.py#L1735) | 1735 | `"            lines.append("` | — |
| [SRC-E599346ABE-L001736](../generate_index.py#L1736) | 1736 | `"                \"\| \""` | — |
| [SRC-E599346ABE-L001737](../generate_index.py#L1737) | 1737 | `"                + \" \| \".join("` | — |
| [SRC-E599346ABE-L001738](../generate_index.py#L1738) | 1738 | `"                    ("` | — |
| [SRC-E599346ABE-L001739](../generate_index.py#L1739) | 1739 | `"                        finding.finding_id,"` | — |
| [SRC-E599346ABE-L001740](../generate_index.py#L1740) | 1740 | `"                        finding.marker,"` | — |
| [SRC-E599346ABE-L001741](../generate_index.py#L1741) | 1741 | `"                        f\"[{_markdown_cell(finding.file)}]({_source_file_href(finding.file, source_line.line if source_line else 1)})\","` | — |
| [SRC-E599346ABE-L001742](../generate_index.py#L1742) | 1742 | `"                        str(source_line.line if source_line else \"غير متاح\"),"` | — |
| [SRC-E599346ABE-L001743](../generate_index.py#L1743) | 1743 | `"                        _markdown_cell(finding.description),"` | — |
| [SRC-E599346ABE-L001744](../generate_index.py#L1744) | 1744 | `"                        f\"[{finding.line_id}]({_source_file_href(finding.file, source_line.line if source_line else 1)})\","` | — |
| [SRC-E599346ABE-L001745](../generate_index.py#L1745) | 1745 | `"                        _markdown_code_span(json.dumps(source_line.content, ensure_ascii=False).replace(\"\|\", r\"\\\|\")) if source_line else \"غير متاح\","` | — |
| [SRC-E599346ABE-L001746](../generate_index.py#L1746) | 1746 | `"                    )"` | — |
| [SRC-E599346ABE-L001747](../generate_index.py#L1747) | 1747 | `"                )"` | — |
| [SRC-E599346ABE-L001748](../generate_index.py#L1748) | 1748 | `"                + \" \|\""` | — |
| [SRC-E599346ABE-L001749](../generate_index.py#L1749) | 1749 | `"            )"` | — |
| [SRC-E599346ABE-L001750](../generate_index.py#L1750) | 1750 | `"    else:"` | — |
| [SRC-E599346ABE-L001751](../generate_index.py#L1751) | 1751 | `"        lines.append(\"\| — \| — \| — \| — \| لم تُكتشف وسوم صريحة من الأنواع المعروفة. \| — \| — \|\")"` | — |
| [SRC-E599346ABE-L001752](../generate_index.py#L1752) | 1752 | `""` | — |
| [SRC-E599346ABE-L001753](../generate_index.py#L1753) | 1753 | `"    lines.extend("` | — |
| [SRC-E599346ABE-L001754](../generate_index.py#L1754) | 1754 | `"        ["` | — |
| [SRC-E599346ABE-L001755](../generate_index.py#L1755) | 1755 | `"            \"\","` | — |
| [SRC-E599346ABE-L001756](../generate_index.py#L1756) | 1756 | `"            \"---\","` | — |
| [SRC-E599346ABE-L001757](../generate_index.py#L1757) | 1757 | `"            \"\","` | — |
| [SRC-E599346ABE-L001758](../generate_index.py#L1758) | 1758 | `"            \"## حدود الفهرسة\","` | — |
| [SRC-E599346ABE-L001759](../generate_index.py#L1759) | 1759 | `"            \"\","` | — |
| [SRC-E599346ABE-L001760](../generate_index.py#L1760) | 1760 | `"            \"- كل الأسطر المنطقية للملفات النصية المؤهلة القابلة للقراءة مفهرسة في SOURCE LINES INDEX، لا في هذا الجدول المختصر.\","` | — |
| [SRC-E599346ABE-L001761](../generate_index.py#L1761) | 1761 | `"            \"- الملفات الأكبر من 2 MiB أو غير القابلة للقراءة أو الثنائية تبقى ضمن الجرد الوصفي، دون فهرسة سطورها.\","` | — |
| [SRC-E599346ABE-L001762](../generate_index.py#L1762) | 1762 | `"            \"- لا تُفحص محتويات البيئة الافتراضية والاعتماديات والمجلدات المولدة.\","` | — |
| [SRC-E599346ABE-L001763](../generate_index.py#L1763) | 1763 | `"            \"- لا تُقرأ ملفات البيئة المحلية وقواعد البيانات والمفاتيح المعروفة.\","` | — |
| [SRC-E599346ABE-L001764](../generate_index.py#L1764) | 1764 | `"            \"- تحليل Python يرفض إنشاء فهرس جزئي عند وجود خطأ نحوي في أي ملف Python مؤهل.\","` | — |
| [SRC-E599346ABE-L001765](../generate_index.py#L1765) | 1765 | `"            (\"- يُحدّث هذا الفهرس آليًا عبر GitHub Actions عند دفع تغيير إلى main؛ \""` | — |
| [SRC-E599346ABE-L001766](../generate_index.py#L1766) | 1766 | `"            \"وتظل تغييرات المصدر قيد المراجعة حتى تُدمج وفق سياسة المستودع.\"),"` | — |
| [SRC-E599346ABE-L001767](../generate_index.py#L1767) | 1767 | `"            \"\","` | — |
| [SRC-E599346ABE-L001768](../generate_index.py#L1768) | 1768 | `"        ]"` | — |
| [SRC-E599346ABE-L001769](../generate_index.py#L1769) | 1769 | `"    )"` | — |
| [SRC-E599346ABE-L001770](../generate_index.py#L1770) | 1770 | `"    return \"\\n\".join(lines)"` | — |
| [SRC-E599346ABE-L001771](../generate_index.py#L1771) | 1771 | `""` | — |
| [SRC-E599346ABE-L001772](../generate_index.py#L1772) | 1772 | `""` | — |
| [SRC-E599346ABE-L001773](../generate_index.py#L1773) | 1773 | `"def write_if_changed(output_path: Path, content: str) -> bool:"` | — |
| [SRC-E599346ABE-L001774](../generate_index.py#L1774) | 1774 | `"    \"\"\"Write atomically only when the generated index differs from the existing file.\"\"\""` | — |
| [SRC-E599346ABE-L001775](../generate_index.py#L1775) | 1775 | `"    output_path.parent.mkdir(parents=True, exist_ok=True)"` | — |
| [SRC-E599346ABE-L001776](../generate_index.py#L1776) | 1776 | `"    try:"` | — |
| [SRC-E599346ABE-L001777](../generate_index.py#L1777) | 1777 | `"        if output_path.read_text(encoding=\"utf-8\") == content:"` | — |
| [SRC-E599346ABE-L001778](../generate_index.py#L1778) | 1778 | `"            return False"` | — |
| [SRC-E599346ABE-L001779](../generate_index.py#L1779) | 1779 | `"    except FileNotFoundError:"` | — |
| [SRC-E599346ABE-L001780](../generate_index.py#L1780) | 1780 | `"        pass"` | — |
| [SRC-E599346ABE-L001781](../generate_index.py#L1781) | 1781 | `""` | — |
| [SRC-E599346ABE-L001782](../generate_index.py#L1782) | 1782 | `"    temporary_path: Path \| None = None"` | — |
| [SRC-E599346ABE-L001783](../generate_index.py#L1783) | 1783 | `"    try:"` | — |
| [SRC-E599346ABE-L001784](../generate_index.py#L1784) | 1784 | `"        with tempfile.NamedTemporaryFile("` | — |
| [SRC-E599346ABE-L001785](../generate_index.py#L1785) | 1785 | `"            mode=\"w\","` | — |
| [SRC-E599346ABE-L001786](../generate_index.py#L1786) | 1786 | `"            encoding=\"utf-8\","` | — |
| [SRC-E599346ABE-L001787](../generate_index.py#L1787) | 1787 | `"            newline=\"\\n\","` | — |
| [SRC-E599346ABE-L001788](../generate_index.py#L1788) | 1788 | `"            dir=output_path.parent,"` | — |
| [SRC-E599346ABE-L001789](../generate_index.py#L1789) | 1789 | `"            prefix=f\".{output_path.name}.\","` | — |
| [SRC-E599346ABE-L001790](../generate_index.py#L1790) | 1790 | `"            suffix=\".tmp\","` | — |
| [SRC-E599346ABE-L001791](../generate_index.py#L1791) | 1791 | `"            delete=False,"` | — |
| [SRC-E599346ABE-L001792](../generate_index.py#L1792) | 1792 | `"        ) as temporary_file:"` | — |
| [SRC-E599346ABE-L001793](../generate_index.py#L1793) | 1793 | `"            temporary_file.write(content)"` | — |
| [SRC-E599346ABE-L001794](../generate_index.py#L1794) | 1794 | `"            temporary_path = Path(temporary_file.name)"` | — |
| [SRC-E599346ABE-L001795](../generate_index.py#L1795) | 1795 | `"        temporary_path.replace(output_path)"` | — |
| [SRC-E599346ABE-L001796](../generate_index.py#L1796) | 1796 | `"    finally:"` | — |
| [SRC-E599346ABE-L001797](../generate_index.py#L1797) | 1797 | `"        if temporary_path is not None and temporary_path.exists():"` | — |
| [SRC-E599346ABE-L001798](../generate_index.py#L1798) | 1798 | `"            temporary_path.unlink()"` | — |
| [SRC-E599346ABE-L001799](../generate_index.py#L1799) | 1799 | `"    return True"` | — |
| [SRC-E599346ABE-L001800](../generate_index.py#L1800) | 1800 | `""` | — |
| [SRC-E599346ABE-L001801](../generate_index.py#L1801) | 1801 | `""` | — |
| [SRC-E599346ABE-L001802](../generate_index.py#L1802) | 1802 | `"def _generate("` | — |
| [SRC-E599346ABE-L001803](../generate_index.py#L1803) | 1803 | `"    root: Path,"` | — |
| [SRC-E599346ABE-L001804](../generate_index.py#L1804) | 1804 | `") -> tuple[str, str, str, dict[str, str], int, int, int, int, int, int, int]:"` | — |
| [SRC-E599346ABE-L001805](../generate_index.py#L1805) | 1805 | `"    \"\"\"Create deterministic overview, source-line pages, and all counts without writing.\"\"\""` | — |
| [SRC-E599346ABE-L001806](../generate_index.py#L1806) | 1806 | `"    inventory = build_file_inventory(root)"` | — |
| [SRC-E599346ABE-L001807](../generate_index.py#L1807) | 1807 | `"    symbols, python_file_count = scan_repository(root)"` | — |
| [SRC-E599346ABE-L001808](../generate_index.py#L1808) | 1808 | `"    static_symbols = scan_static_symbols(root, inventory)"` | — |
| [SRC-E599346ABE-L001809](../generate_index.py#L1809) | 1809 | `"    source_lines = scan_source_lines(root, inventory)"` | — |
| [SRC-E599346ABE-L001810](../generate_index.py#L1810) | 1810 | `"    validate_source_line_coverage(root, inventory, source_lines)"` | — |
| [SRC-E599346ABE-L001811](../generate_index.py#L1811) | 1811 | `"    findings = scan_finding_annotations(source_lines)"` | — |
| [SRC-E599346ABE-L001812](../generate_index.py#L1812) | 1812 | `"    excluded_paths = discover_excluded_paths(root)"` | — |
| [SRC-E599346ABE-L001813](../generate_index.py#L1813) | 1813 | `"    coverage_audit_markdown = render_coverage_audit_markdown("` | — |
| [SRC-E599346ABE-L001814](../generate_index.py#L1814) | 1814 | `"        root, inventory, source_lines, excluded_paths"` | — |
| [SRC-E599346ABE-L001815](../generate_index.py#L1815) | 1815 | `"    )"` | — |
| [SRC-E599346ABE-L001816](../generate_index.py#L1816) | 1816 | `"    source_pages, pages_by_file = render_source_line_pages("` | — |
| [SRC-E599346ABE-L001817](../generate_index.py#L1817) | 1817 | `"        source_lines, inventory, findings"` | — |
| [SRC-E599346ABE-L001818](../generate_index.py#L1818) | 1818 | `"    )"` | — |
| [SRC-E599346ABE-L001819](../generate_index.py#L1819) | 1819 | `"    markdown = render_markdown("` | — |
| [SRC-E599346ABE-L001820](../generate_index.py#L1820) | 1820 | `"        symbols, python_file_count, inventory, static_symbols, source_lines, findings"` | — |
| [SRC-E599346ABE-L001821](../generate_index.py#L1821) | 1821 | `"    )"` | — |
| [SRC-E599346ABE-L001822](../generate_index.py#L1822) | 1822 | `"    source_lines_markdown = render_source_lines_markdown("` | — |
| [SRC-E599346ABE-L001823](../generate_index.py#L1823) | 1823 | `"        source_lines, inventory, findings, pages_by_file, source_pages"` | — |
| [SRC-E599346ABE-L001824](../generate_index.py#L1824) | 1824 | `"    )"` | — |
| [SRC-E599346ABE-L001825](../generate_index.py#L1825) | 1825 | `"    return ("` | — |
| [SRC-E599346ABE-L001826](../generate_index.py#L1826) | 1826 | `"        markdown,"` | — |
| [SRC-E599346ABE-L001827](../generate_index.py#L1827) | 1827 | `"        source_lines_markdown,"` | — |
| [SRC-E599346ABE-L001828](../generate_index.py#L1828) | 1828 | `"        coverage_audit_markdown,"` | — |
| [SRC-E599346ABE-L001829](../generate_index.py#L1829) | 1829 | `"        source_pages,"` | — |
| [SRC-E599346ABE-L001830](../generate_index.py#L1830) | 1830 | `"        python_file_count,"` | — |
| [SRC-E599346ABE-L001831](../generate_index.py#L1831) | 1831 | `"        len(inventory),"` | — |
| [SRC-E599346ABE-L001832](../generate_index.py#L1832) | 1832 | `"        len(symbols),"` | — |
| [SRC-E599346ABE-L001833](../generate_index.py#L1833) | 1833 | `"        len(source_lines),"` | — |
| [SRC-E599346ABE-L001834](../generate_index.py#L1834) | 1834 | `"        len(findings),"` | — |
| [SRC-E599346ABE-L001835](../generate_index.py#L1835) | 1835 | `"        sum(symbol.documented is True for symbol in symbols),"` | — |
| [SRC-E599346ABE-L001836](../generate_index.py#L1836) | 1836 | `"        sum(symbol.documented is False for symbol in symbols),"` | — |
| [SRC-E599346ABE-L001837](../generate_index.py#L1837) | 1837 | `"    )"` | — |
| [SRC-E599346ABE-L001838](../generate_index.py#L1838) | 1838 | `""` | — |
| [SRC-E599346ABE-L001839](../generate_index.py#L1839) | 1839 | `""` | — |
| [SRC-E599346ABE-L001840](../generate_index.py#L1840) | 1840 | `"def main(argv: Sequence[str] \| None = None) -> int:"` | — |
| [SRC-E599346ABE-L001841](../generate_index.py#L1841) | 1841 | `"    \"\"\"Generate the living repository index or check that the committed copy is current.\"\"\""` | — |
| [SRC-E599346ABE-L001842](../generate_index.py#L1842) | 1842 | `"    parser = argparse.ArgumentParser("` | — |
| [SRC-E599346ABE-L001843](../generate_index.py#L1843) | 1843 | `"        description=\"إنشاء/فحص فهرس مستودع Omarai وملفات الشفرة والرموز الساكنة.\""` | — |
| [SRC-E599346ABE-L001844](../generate_index.py#L1844) | 1844 | `"    )"` | — |
| [SRC-E599346ABE-L001845](../generate_index.py#L1845) | 1845 | `"    parser.add_argument("` | — |
| [SRC-E599346ABE-L001846](../generate_index.py#L1846) | 1846 | `"        \"--root\","` | — |
| [SRC-E599346ABE-L001847](../generate_index.py#L1847) | 1847 | `"        type=Path,"` | — |
| [SRC-E599346ABE-L001848](../generate_index.py#L1848) | 1848 | `"        default=Path(__file__).resolve().parents[1],"` | — |
| [SRC-E599346ABE-L001849](../generate_index.py#L1849) | 1849 | `"        help=\"مسار جذر المستودع (الافتراضي: جذر مشروع Omarai).\","` | — |
| [SRC-E599346ABE-L001850](../generate_index.py#L1850) | 1850 | `"    )"` | — |
| [SRC-E599346ABE-L001851](../generate_index.py#L1851) | 1851 | `"    parser.add_argument("` | — |
| [SRC-E599346ABE-L001852](../generate_index.py#L1852) | 1852 | `"        \"--check\","` | — |
| [SRC-E599346ABE-L001853](../generate_index.py#L1853) | 1853 | `"        action=\"store_true\","` | — |
| [SRC-E599346ABE-L001854](../generate_index.py#L1854) | 1854 | `"        help=\"لا تكتب ملفات؛ أعد حالة فشل إذا كان أي فهرس مولّد قديمًا أو مفقودًا.\","` | — |
| [SRC-E599346ABE-L001855](../generate_index.py#L1855) | 1855 | `"    )"` | — |
| [SRC-E599346ABE-L001856](../generate_index.py#L1856) | 1856 | `"    arguments = parser.parse_args(argv)"` | — |
| [SRC-E599346ABE-L001857](../generate_index.py#L1857) | 1857 | `""` | — |
| [SRC-E599346ABE-L001858](../generate_index.py#L1858) | 1858 | `"    try:"` | — |
| [SRC-E599346ABE-L001859](../generate_index.py#L1859) | 1859 | `"        root = arguments.root.resolve(strict=True)"` | — |
| [SRC-E599346ABE-L001860](../generate_index.py#L1860) | 1860 | `"        if not root.is_dir():"` | — |
| [SRC-E599346ABE-L001861](../generate_index.py#L1861) | 1861 | `"            raise ValueError(f\"المسار المحدد ليس مجلدًا: {root}\")"` | — |
| [SRC-E599346ABE-L001862](../generate_index.py#L1862) | 1862 | `"        ("` | — |
| [SRC-E599346ABE-L001863](../generate_index.py#L1863) | 1863 | `"            markdown,"` | — |
| [SRC-E599346ABE-L001864](../generate_index.py#L1864) | 1864 | `"            source_lines_markdown,"` | — |
| [SRC-E599346ABE-L001865](../generate_index.py#L1865) | 1865 | `"            coverage_audit_markdown,"` | — |
| [SRC-E599346ABE-L001866](../generate_index.py#L1866) | 1866 | `"            source_pages,"` | — |
| [SRC-E599346ABE-L001867](../generate_index.py#L1867) | 1867 | `"            python_file_count,"` | — |
| [SRC-E599346ABE-L001868](../generate_index.py#L1868) | 1868 | `"            repository_file_count,"` | — |
| [SRC-E599346ABE-L001869](../generate_index.py#L1869) | 1869 | `"            symbol_count,"` | — |
| [SRC-E599346ABE-L001870](../generate_index.py#L1870) | 1870 | `"            source_line_count,"` | — |
| [SRC-E599346ABE-L001871](../generate_index.py#L1871) | 1871 | `"            finding_count,"` | — |
| [SRC-E599346ABE-L001872](../generate_index.py#L1872) | 1872 | `"            documented_count,"` | — |
| [SRC-E599346ABE-L001873](../generate_index.py#L1873) | 1873 | `"            missing_count,"` | — |
| [SRC-E599346ABE-L001874](../generate_index.py#L1874) | 1874 | `"        ) = _generate(root)"` | — |
| [SRC-E599346ABE-L001875](../generate_index.py#L1875) | 1875 | `"        output_path = root / INDEX_RELATIVE_PATH"` | — |
| [SRC-E599346ABE-L001876](../generate_index.py#L1876) | 1876 | `"        source_lines_output_path = root / SOURCE_LINES_INDEX_RELATIVE_PATH"` | — |
| [SRC-E599346ABE-L001877](../generate_index.py#L1877) | 1877 | `"        generated_outputs = {"` | — |
| [SRC-E599346ABE-L001878](../generate_index.py#L1878) | 1878 | `"            INDEX_RELATIVE_PATH: markdown,"` | — |
| [SRC-E599346ABE-L001879](../generate_index.py#L1879) | 1879 | `"            SOURCE_LINES_INDEX_RELATIVE_PATH: source_lines_markdown,"` | — |
| [SRC-E599346ABE-L001880](../generate_index.py#L1880) | 1880 | `"            COVERAGE_AUDIT_RELATIVE_PATH: coverage_audit_markdown,"` | — |
| [SRC-E599346ABE-L001881](../generate_index.py#L1881) | 1881 | `"            **source_pages,"` | — |
| [SRC-E599346ABE-L001882](../generate_index.py#L1882) | 1882 | `"        }"` | — |
| [SRC-E599346ABE-L001883](../generate_index.py#L1883) | 1883 | `""` | — |
| [SRC-E599346ABE-L001884](../generate_index.py#L1884) | 1884 | `"        if arguments.check:"` | — |
| [SRC-E599346ABE-L001885](../generate_index.py#L1885) | 1885 | `"            for relative_path, expected_content in generated_outputs.items():"` | — |
| [SRC-E599346ABE-L001886](../generate_index.py#L1886) | 1886 | `"                generated_path = root / relative_path"` | — |
| [SRC-E599346ABE-L001887](../generate_index.py#L1887) | 1887 | `"                try:"` | — |
| [SRC-E599346ABE-L001888](../generate_index.py#L1888) | 1888 | `"                    current_content = generated_path.read_text(encoding=\"utf-8\")"` | — |
| [SRC-E599346ABE-L001889](../generate_index.py#L1889) | 1889 | `"                except FileNotFoundError:"` | — |
| [SRC-E599346ABE-L001890](../generate_index.py#L1890) | 1890 | `"                    print("` | — |
| [SRC-E599346ABE-L001891](../generate_index.py#L1891) | 1891 | `"                        f\"فهرس مولّد مفقود: {generated_path}. \""` | — |
| [SRC-E599346ABE-L001892](../generate_index.py#L1892) | 1892 | `"                        \"شغّل python docs/generate_index.py.\","` | — |
| [SRC-E599346ABE-L001893](../generate_index.py#L1893) | 1893 | `"                        file=sys.stderr,"` | — |
| [SRC-E599346ABE-L001894](../generate_index.py#L1894) | 1894 | `"                    )"` | — |
| [SRC-E599346ABE-L001895](../generate_index.py#L1895) | 1895 | `"                    return 1"` | — |
| [SRC-E599346ABE-L001896](../generate_index.py#L1896) | 1896 | `"                if current_content != expected_content:"` | — |
| [SRC-E599346ABE-L001897](../generate_index.py#L1897) | 1897 | `"                    if relative_path == INDEX_RELATIVE_PATH:"` | — |
| [SRC-E599346ABE-L001898](../generate_index.py#L1898) | 1898 | `"                        message = \"الفهرس قديم (الرئيسي)\""` | — |
| [SRC-E599346ABE-L001899](../generate_index.py#L1899) | 1899 | `"                    elif relative_path == SOURCE_LINES_INDEX_RELATIVE_PATH:"` | — |
| [SRC-E599346ABE-L001900](../generate_index.py#L1900) | 1900 | `"                        message = \"فهرس الأسطر قديم\""` | — |
| [SRC-E599346ABE-L001901](../generate_index.py#L1901) | 1901 | `"                    else:"` | — |
| [SRC-E599346ABE-L001902](../generate_index.py#L1902) | 1902 | `"                        message = \"فهرس تغطية الفهرسة قديم\""` | — |
| [SRC-E599346ABE-L001903](../generate_index.py#L1903) | 1903 | `"                    print("` | — |
| [SRC-E599346ABE-L001904](../generate_index.py#L1904) | 1904 | `"                        f\"{message}: {generated_path}. \""` | — |
| [SRC-E599346ABE-L001905](../generate_index.py#L1905) | 1905 | `"                        \"شغّل python docs/generate_index.py.\","` | — |
| [SRC-E599346ABE-L001906](../generate_index.py#L1906) | 1906 | `"                        file=sys.stderr,"` | — |
| [SRC-E599346ABE-L001907](../generate_index.py#L1907) | 1907 | `"                    )"` | — |
| [SRC-E599346ABE-L001908](../generate_index.py#L1908) | 1908 | `"                    return 1"` | — |
| [SRC-E599346ABE-L001909](../generate_index.py#L1909) | 1909 | `""` | — |
| [SRC-E599346ABE-L001910](../generate_index.py#L1910) | 1910 | `"            pages_directory = root / SOURCE_LINES_PAGES_DIR"` | — |
| [SRC-E599346ABE-L001911](../generate_index.py#L1911) | 1911 | `"            expected_page_names = {"` | — |
| [SRC-E599346ABE-L001912](../generate_index.py#L1912) | 1912 | `"                Path(relative_path).name"` | — |
| [SRC-E599346ABE-L001913](../generate_index.py#L1913) | 1913 | `"                for relative_path in source_pages"` | — |
| [SRC-E599346ABE-L001914](../generate_index.py#L1914) | 1914 | `"            }"` | — |
| [SRC-E599346ABE-L001915](../generate_index.py#L1915) | 1915 | `"            if pages_directory.exists():"` | — |
| [SRC-E599346ABE-L001916](../generate_index.py#L1916) | 1916 | `"                actual_page_names = {"` | — |
| [SRC-E599346ABE-L001917](../generate_index.py#L1917) | 1917 | `"                    path.name"` | — |
| [SRC-E599346ABE-L001918](../generate_index.py#L1918) | 1918 | `"                    for path in pages_directory.iterdir()"` | — |
| [SRC-E599346ABE-L001919](../generate_index.py#L1919) | 1919 | `"                    if path.is_file() and SOURCE_LINES_PAGE_RE.fullmatch(path.name)"` | — |
| [SRC-E599346ABE-L001920](../generate_index.py#L1920) | 1920 | `"                }"` | — |
| [SRC-E599346ABE-L001921](../generate_index.py#L1921) | 1921 | `"                stale_pages = actual_page_names - expected_page_names"` | — |
| [SRC-E599346ABE-L001922](../generate_index.py#L1922) | 1922 | `"                if stale_pages:"` | — |
| [SRC-E599346ABE-L001923](../generate_index.py#L1923) | 1923 | `"                    print("` | — |
| [SRC-E599346ABE-L001924](../generate_index.py#L1924) | 1924 | `"                        \"صفحات فهرس قديمة يجب حذفها بإعادة التوليد: \""` | — |
| [SRC-E599346ABE-L001925](../generate_index.py#L1925) | 1925 | `"                        + \", \".join(sorted(stale_pages)),"` | — |
| [SRC-E599346ABE-L001926](../generate_index.py#L1926) | 1926 | `"                        file=sys.stderr,"` | — |
| [SRC-E599346ABE-L001927](../generate_index.py#L1927) | 1927 | `"                    )"` | — |
| [SRC-E599346ABE-L001928](../generate_index.py#L1928) | 1928 | `"                    return 1"` | — |
| [SRC-E599346ABE-L001929](../generate_index.py#L1929) | 1929 | `"            changed = False"` | — |
| [SRC-E599346ABE-L001930](../generate_index.py#L1930) | 1930 | `"        else:"` | — |
| [SRC-E599346ABE-L001931](../generate_index.py#L1931) | 1931 | `"            changed = False"` | — |
| [SRC-E599346ABE-L001932](../generate_index.py#L1932) | 1932 | `"            for relative_path, generated_content in generated_outputs.items():"` | — |
| [SRC-E599346ABE-L001933](../generate_index.py#L1933) | 1933 | `"                if write_if_changed(root / relative_path, generated_content):"` | — |
| [SRC-E599346ABE-L001934](../generate_index.py#L1934) | 1934 | `"                    changed = True"` | — |
| [SRC-E599346ABE-L001935](../generate_index.py#L1935) | 1935 | `""` | — |
| [SRC-E599346ABE-L001936](../generate_index.py#L1936) | 1936 | `"            pages_directory = root / SOURCE_LINES_PAGES_DIR"` | — |
| [SRC-E599346ABE-L001937](../generate_index.py#L1937) | 1937 | `"            if pages_directory.exists():"` | — |
| [SRC-E599346ABE-L001938](../generate_index.py#L1938) | 1938 | `"                expected_page_names = {"` | — |
| [SRC-E599346ABE-L001939](../generate_index.py#L1939) | 1939 | `"                    Path(relative_path).name"` | — |
| [SRC-E599346ABE-L001940](../generate_index.py#L1940) | 1940 | `"                    for relative_path in source_pages"` | — |
| [SRC-E599346ABE-L001941](../generate_index.py#L1941) | 1941 | `"                }"` | — |
| [SRC-E599346ABE-L001942](../generate_index.py#L1942) | 1942 | `"                for path in pages_directory.iterdir():"` | — |
| [SRC-E599346ABE-L001943](../generate_index.py#L1943) | 1943 | `"                    if ("` | — |
| [SRC-E599346ABE-L001944](../generate_index.py#L1944) | 1944 | `"                        path.is_file()"` | — |
| [SRC-E599346ABE-L001945](../generate_index.py#L1945) | 1945 | `"                        and SOURCE_LINES_PAGE_RE.fullmatch(path.name)"` | — |
| [SRC-E599346ABE-L001946](../generate_index.py#L1946) | 1946 | `"                        and path.name not in expected_page_names"` | — |
| [SRC-E599346ABE-L001947](../generate_index.py#L1947) | 1947 | `"                    ):"` | — |
| [SRC-E599346ABE-L001948](../generate_index.py#L1948) | 1948 | `"                        path.unlink()"` | — |
| [SRC-E599346ABE-L001949](../generate_index.py#L1949) | 1949 | `"                        changed = True"` | — |
| [SRC-E599346ABE-L001950](../generate_index.py#L1950) | 1950 | `"    except (IndexGenerationError, OSError, ValueError) as exc:"` | — |
| [SRC-E599346ABE-L001951](../generate_index.py#L1951) | 1951 | `"        print(f\"خطأ في إنشاء فهرس Omarai: {exc}\", file=sys.stderr)"` | — |
| [SRC-E599346ABE-L001952](../generate_index.py#L1952) | 1952 | `"        return 1"` | — |
| [SRC-E599346ABE-L001953](../generate_index.py#L1953) | 1953 | `""` | — |
| [SRC-E599346ABE-L001954](../generate_index.py#L1954) | 1954 | `"    if arguments.check:"` | — |
| [SRC-E599346ABE-L001955](../generate_index.py#L1955) | 1955 | `"        action = \"الفهرس محدث والتحقق ناجح\""` | — |
| [SRC-E599346ABE-L001956](../generate_index.py#L1956) | 1956 | `"    else:"` | — |
| [SRC-E599346ABE-L001957](../generate_index.py#L1957) | 1957 | `"        action = \"تم تحديث\" if changed else \"الفهرس محدث بالفعل\""` | — |
| [SRC-E599346ABE-L001958](../generate_index.py#L1958) | 1958 | `"    print("` | — |
| [SRC-E599346ABE-L001959](../generate_index.py#L1959) | 1959 | `"        f\"{action}: {output_path} \| \""` | — |
| [SRC-E599346ABE-L001960](../generate_index.py#L1960) | 1960 | `"        f\"ملفات المستودع: {repository_file_count} \| \""` | — |
| [SRC-E599346ABE-L001961](../generate_index.py#L1961) | 1961 | `"        f\"ملفات Python: {python_file_count} \| \""` | — |
| [SRC-E599346ABE-L001962](../generate_index.py#L1962) | 1962 | `"        f\"تعريفات Python: {symbol_count} \| \""` | — |
| [SRC-E599346ABE-L001963](../generate_index.py#L1963) | 1963 | `"        f\"أسطر مفهرسة: {source_line_count} \| \""` | — |
| [SRC-E599346ABE-L001964](../generate_index.py#L1964) | 1964 | `"        f\"صفحات أسطر: {len(source_pages)} \| \""` | — |
| [SRC-E599346ABE-L001965](../generate_index.py#L1965) | 1965 | `"        f\"وسوم مراجعة: {finding_count} \| \""` | — |
| [SRC-E599346ABE-L001966](../generate_index.py#L1966) | 1966 | `"        f\"موثق: {documented_count} \| \""` | — |
| [SRC-E599346ABE-L001967](../generate_index.py#L1967) | 1967 | `"        f\"ناقص Docstring: {missing_count}\""` | — |
| [SRC-E599346ABE-L001968](../generate_index.py#L1968) | 1968 | `"    )"` | — |
| [SRC-E599346ABE-L001969](../generate_index.py#L1969) | 1969 | `"    return 0"` | — |
| [SRC-E599346ABE-L001970](../generate_index.py#L1970) | 1970 | `""` | — |
| [SRC-E599346ABE-L001971](../generate_index.py#L1971) | 1971 | `""` | — |
| [SRC-E599346ABE-L001972](../generate_index.py#L1972) | 1972 | `"if __name__ == \"__main__\":"` | — |
| [SRC-E599346ABE-L001973](../generate_index.py#L1973) | 1973 | `"    raise SystemExit(main())"` | — |
## وثائق وفهرسة

### FILE-6E35221BFA — [docs/GO_LIVE_CHECKLIST_AR.md](../GO_LIVE_CHECKLIST_AR.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-6E35221BFA-L000001](../GO_LIVE_CHECKLIST_AR.md#L1) | 1 | `"# قائمة قبول Omarai قبل التشغيل العام"` | — |
| [SRC-6E35221BFA-L000002](../GO_LIVE_CHECKLIST_AR.md#L2) | 2 | `""` | — |
| [SRC-6E35221BFA-L000003](../GO_LIVE_CHECKLIST_AR.md#L3) | 3 | `"تفصل هذه القائمة بين نجاح البناء وبين إثبات أن الوكيل يعمل على عنوان استضافة فعلي. استخدام الملف لا يعني وجود خدمة منشورة."` | — |
| [SRC-6E35221BFA-L000004](../GO_LIVE_CHECKLIST_AR.md#L4) | 4 | `""` | — |
| [SRC-6E35221BFA-L000005](../GO_LIVE_CHECKLIST_AR.md#L5) | 5 | `"مصادر الحالة الحالية: [نطاق التنفيذ](IMPLEMENTATION_SCOPE.md)، [سجل المعالجة المركزي](OMARAI_REMEDIATION_REGISTER_AR.md)، و[مصفوفة أدلة الاختبار](OMARAI_TEST_EVIDENCE_MATRIX_AR.md)."` | — |
| [SRC-6E35221BFA-L000006](../GO_LIVE_CHECKLIST_AR.md#L6) | 6 | `""` | — |
| [SRC-6E35221BFA-L000007](../GO_LIVE_CHECKLIST_AR.md#L7) | 7 | `"## 1. اختر مسار استضافة واحدًا"` | — |
| [SRC-6E35221BFA-L000008](../GO_LIVE_CHECKLIST_AR.md#L8) | 8 | `""` | — |
| [SRC-6E35221BFA-L000009](../GO_LIVE_CHECKLIST_AR.md#L9) | 9 | ``"- [Railway](DEPLOY_RAILWAY_AR.md) — دليل إعداد `railway.json`."`` | — |
| [SRC-6E35221BFA-L000010](../GO_LIVE_CHECKLIST_AR.md#L10) | 10 | `"- [SnapDeploy](DEPLOY_SNAPDEPLOY_AR.md) — مسار عرض/اختبار مجاني؛ تحقق من الحدود الحالية ولا تعتمد على التخزين لبيانات دائمة."` | — |
| [SRC-6E35221BFA-L000011](../GO_LIVE_CHECKLIST_AR.md#L11) | 11 | `"- [Render](DEPLOY_RENDER_AR.md) — بديل اختياري عند توافر الحساب والخدمة."` | — |
| [SRC-6E35221BFA-L000012](../GO_LIVE_CHECKLIST_AR.md#L12) | 12 | `""` | — |
| [SRC-6E35221BFA-L000013](../GO_LIVE_CHECKLIST_AR.md#L13) | 13 | ``"لا تخلط إعدادات مزودين مختلفين. وجود `Dockerfile` أو ملف Blueprint لا يثبت أن الخدمة أُنشئت أو تعمل."`` | — |
| [SRC-6E35221BFA-L000014](../GO_LIVE_CHECKLIST_AR.md#L14) | 14 | `""` | — |
| [SRC-6E35221BFA-L000015](../GO_LIVE_CHECKLIST_AR.md#L15) | 15 | `"## 2. إعداد آمن"` | — |
| [SRC-6E35221BFA-L000016](../GO_LIVE_CHECKLIST_AR.md#L16) | 16 | `""` | — |
| [SRC-6E35221BFA-L000017](../GO_LIVE_CHECKLIST_AR.md#L17) | 17 | ``"1. اربط المستودع `mosabosama2030-oss/omarai` والفرع `main` بمزود الاستضافة المختار وفق دليله."`` | — |
| [SRC-6E35221BFA-L000018](../GO_LIVE_CHECKLIST_AR.md#L18) | 18 | ``"2. اضبط الأسرار في لوحة المزود فقط: `OMARAI_PUBLIC_DEPLOYMENT=1`، ورمز عشوائي `OMARAI_ACCESS_TOKEN` بطول 32 حرفًا على الأقل، ومفتاح النموذج `OPENROUTER_API_KEY` أو `OMARAI_LLM_API_KEY`."`` | — |
| [SRC-6E35221BFA-L000019](../GO_LIVE_CHECKLIST_AR.md#L19) | 19 | ``"3. لا تفعّل `OMARAI_OPENROUTER_WEB_SEARCH` قبل مراجعة تكلفته والموافقة عليه."`` | — |
| [SRC-6E35221BFA-L000020](../GO_LIVE_CHECKLIST_AR.md#L20) | 20 | ``"4. استخدم نطاق HTTPS تملكه أو تتحكم فيه. لا تضف نطاقًا إلى `OMARAI_ALLOWED_ORIGINS` إلا إذا كان موثوقًا وتحتاجه فعلًا."`` | — |
| [SRC-6E35221BFA-L000021](../GO_LIVE_CHECKLIST_AR.md#L21) | 21 | ``"5. في مضيف Docker يسمح بوسيط بناء مباشر، مرّر `--build-arg OMARAI_BUILD_SHA=\"$(git rev-parse HEAD)\"`. على SnapDeploy، اضبط متغير البيئة غير السري `PUBLIC_OMARAI_BUILD_SHA` على SHA الكامل لالتزام الإصدار قبل إعادة البناء؛ المنصة تمرر متغيرات `PUBLIC_*` إلى بناء Docker. لا تستخدمه لأي سر، ولا تعتبر هوية البناء مثبتة إذا كانت `build.sha` تساوي `unknown`."`` | — |
| [SRC-6E35221BFA-L000022](../GO_LIVE_CHECKLIST_AR.md#L22) | 22 | `""` | — |
| [SRC-6E35221BFA-L000023](../GO_LIVE_CHECKLIST_AR.md#L23) | 23 | `"## 3. قبول النسخة المنشورة"` | — |
| [SRC-6E35221BFA-L000024](../GO_LIVE_CHECKLIST_AR.md#L24) | 24 | `""` | — |
| [SRC-6E35221BFA-L000025](../GO_LIVE_CHECKLIST_AR.md#L25) | 25 | ``"شغّل [Hosted acceptance smoke workflow](../.github/workflows/hosted-smoke.yml) يدويًا بعد ضبط أسرار GitHub Actions `OMARAI_ACCESS_TOKEN` و`OMARAI_BASE_URL` بقيم معتمدة. يجب أن يكون `OMARAI_BASE_URL` أصل HTTPS للخدمة دون مسار. يرسل الاختبار طلبات فعلية إلى البحث والنموذج وقد يستهلك حصة أو تكلفة؛ **لا تشغله قبل الموافقة البشرية على المضيف والتكلفة**."`` | — |
| [SRC-6E35221BFA-L000026](../GO_LIVE_CHECKLIST_AR.md#L26) | 26 | `""` | — |
| [SRC-6E35221BFA-L000027](../GO_LIVE_CHECKLIST_AR.md#L27) | 27 | `"معايير القبول:"` | — |
| [SRC-6E35221BFA-L000028](../GO_LIVE_CHECKLIST_AR.md#L28) | 28 | ``"- `/api/health` يعيد HTTP 200؛ و`build.sha` يطابق SHA الكامل المستهدف."`` | — |
| [SRC-6E35221BFA-L000029](../GO_LIVE_CHECKLIST_AR.md#L29) | 29 | ``"- طلب `POST /api/agent` دون رمز يرجع HTTP 401."`` | — |
| [SRC-6E35221BFA-L000030](../GO_LIVE_CHECKLIST_AR.md#L30) | 30 | `"- التشخيص الحي يثبت اتصال البحث واستجابة النموذج للموفرين المطلوب اختبارهم."` | — |
| [SRC-6E35221BFA-L000031](../GO_LIVE_CHECKLIST_AR.md#L31) | 31 | `"- السؤال التجريبي يعيد إجابة ومصادر، وتُراجع الإجابة مقابل مصادرها يدويًا."` | — |
| [SRC-6E35221BFA-L000032](../GO_LIVE_CHECKLIST_AR.md#L32) | 32 | `"- لا يظهر رمز وصول أو مفتاح API في التقرير أو السجلات."` | — |
| [SRC-6E35221BFA-L000033](../GO_LIVE_CHECKLIST_AR.md#L33) | 33 | `""` | — |
| [SRC-6E35221BFA-L000034](../GO_LIVE_CHECKLIST_AR.md#L34) | 34 | `"## 4. تخزين البيانات وحدود الاستخدام"` | — |
| [SRC-6E35221BFA-L000035](../GO_LIVE_CHECKLIST_AR.md#L35) | 35 | `""` | — |
| [SRC-6E35221BFA-L000036](../GO_LIVE_CHECKLIST_AR.md#L36) | 36 | `"- الرمز الحالي مشترك للتطبيق كله، وليس هوية لكل عميل. لا تعرض النسخة كخدمة متعددة المستأجرين ولا تخزن بيانات سرية لعملاء مختلفين."` | — |
| [SRC-6E35221BFA-L000037](../GO_LIVE_CHECKLIST_AR.md#L37) | 37 | `"- حدود التزامن ومعدل الطلبات محلية داخل العملية؛ لم تثبت سعة إنتاجية أو حدود موزعة."` | — |
| [SRC-6E35221BFA-L000038](../GO_LIVE_CHECKLIST_AR.md#L38) | 38 | ``"- إذا كان المضيف يوفر Volume دائمًا، اربطه فعليًا واضبط `OMARAI_DB_PATH` لمسار داخل Volume مثل `/data/omarai.sqlite3`."`` | — |
| [SRC-6E35221BFA-L000039](../GO_LIVE_CHECKLIST_AR.md#L39) | 39 | `"- أنشئ نسخة احتياطية خارج قرص الخدمة واستعدها إلى قاعدة اختبار منفصلة. أعد تشغيل/نشر الخدمة وأثبت بقاء سجل تجريبي قبل الاعتماد على التخزين."` | — |
| [SRC-6E35221BFA-L000040](../GO_LIVE_CHECKLIST_AR.md#L40) | 40 | `"- إذا لم ينجح اختبار الديمومة والاستعادة، استخدم بيانات اصطناعية قابلة للفقد فقط."` | — |
| [SRC-6E35221BFA-L000041](../GO_LIVE_CHECKLIST_AR.md#L41) | 41 | `""` | — |
| [SRC-6E35221BFA-L000042](../GO_LIVE_CHECKLIST_AR.md#L42) | 42 | `"## 5. قبول واجهة الهاتف"` | — |
| [SRC-6E35221BFA-L000043](../GO_LIVE_CHECKLIST_AR.md#L43) | 43 | `""` | — |
| [SRC-6E35221BFA-L000044](../GO_LIVE_CHECKLIST_AR.md#L44) | 44 | `"بعد نجاح الفحص الآلي، اختبر يدويًا على Android ومتصفح ضيق العرض: RTL، والتحميل، والنجاح، والفشل، وإعادة المحاولة، وفتح المصادر، والرفض برمز خاطئ، وعدم بقاء إجابة قديمة بعد خطأ. لا تستخدم بيانات عملاء حقيقية في الاختبار."` | — |
| [SRC-6E35221BFA-L000045](../GO_LIVE_CHECKLIST_AR.md#L45) | 45 | `""` | — |
| [SRC-6E35221BFA-L000046](../GO_LIVE_CHECKLIST_AR.md#L46) | 46 | `"## حدود الإثبات"` | — |
| [SRC-6E35221BFA-L000047](../GO_LIVE_CHECKLIST_AR.md#L47) | 47 | `""` | — |
| [SRC-6E35221BFA-L000048](../GO_LIVE_CHECKLIST_AR.md#L48) | 48 | ``"نجاح Pytest أو Ruff أو بناء Docker لا يثبت عمل المضيف، أو توافر كل موفر خارجي، أو صحة كل إجابة، أو استمرار SQLite، أو سعة التحمل. سجّل كل فحص غير منفذ بوصفه `NOT_RUN` أو `UNKNOWN` ولا تعلن قبول النشر قبل توفر دليله المباشر."`` | — |
## وثائق وفهرسة

### FILE-C8EA754D73 — [docs/IMPLEMENTATION_SCOPE.md](../IMPLEMENTATION_SCOPE.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-C8EA754D73-L000001](../IMPLEMENTATION_SCOPE.md#L1) | 1 | `"# Omarai — نطاق التنفيذ الفعلي وحدود الإثبات"` | — |
| [SRC-C8EA754D73-L000002](../IMPLEMENTATION_SCOPE.md#L2) | 2 | `""` | — |
| [SRC-C8EA754D73-L000003](../IMPLEMENTATION_SCOPE.md#L3) | 3 | ``"> **تحديث 1 نوفمبر 2026 — تنبيه خط الأساس:** المحتوى التفصيلي أدناه لقطة تاريخية أقدم، ولا يصف وحده الحالة الحالية. فُحص `main` عند `63b7dd01889de4aadd66acea90a2415b33376e2e`؛ وحزمة الإغلاق المقترحة موجودة في PR #145 على الفرع `fix/p0-core-consolidated-2026-11-01`، ولم تُدمج بعد. راجع [تقرير المعمارية والأمن](OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md)، [سجل المعالجة](OMARAI_REMEDIATION_REGISTER_AR.md)، و[PR #145](https://github.com/mosabosama2030-oss/omarai/pull/145) قبل اعتبار أي بند منفذًا على `main`."`` | — |
| [SRC-C8EA754D73-L000004](../IMPLEMENTATION_SCOPE.md#L4) | 4 | `""` | — |
| [SRC-C8EA754D73-L000005](../IMPLEMENTATION_SCOPE.md#L5) | 5 | `""` | — |
| [SRC-C8EA754D73-L000006](../IMPLEMENTATION_SCOPE.md#L6) | 6 | ``"**الرأس المرجعي لـ `main` الذي تحققنا منه:** `00a3ede039922c0c24097e89f653e6d3c984435d`؛ commit فهرسة مولد بعد دمج PR #81 في `9f6674abf8679a0630d95b269b54a7ef8629c3bf`.  "`` | — |
| [SRC-C8EA754D73-L000007](../IMPLEMENTATION_SCOPE.md#L7) | 7 | `"**حالة PR #81:** مدمج. غيّر إعدادات اختبارات CI وثلاث وثائق؛ لم يغيّر منطق البحث أو موصلاته.  "` | — |
| [SRC-C8EA754D73-L000008](../IMPLEMENTATION_SCOPE.md#L8) | 8 | ``"**حدّ التحقق:** تشغيل CI على رأس PR قبل الدمج [#39955767221](https://github.com/mosabosama2030-oss/omarai/actions/runs/39955767221) نجح؛ لم أتمكن من إثبات تشغيل push مستقل على رأس `main` الحالي من بيانات التشغيل التي يعيدها موصل GitHub المتاح. هذا `NOT_CONFIRMED` وليس دليل فشل.  "`` | — |
| [SRC-C8EA754D73-L000009](../IMPLEMENTATION_SCOPE.md#L9) | 9 | `"**حدود الوثيقة:** تصف الشفرة الحالية وما تثبته الأدلة؛ ليست شهادة امتثال أو تأكيدًا على وجود خدمة مستضافة."` | — |
| [SRC-C8EA754D73-L000010](../IMPLEMENTATION_SCOPE.md#L10) | 10 | `""` | — |
| [SRC-C8EA754D73-L000011](../IMPLEMENTATION_SCOPE.md#L11) | 11 | `"## الحالة التنفيذية الحالية"` | — |
| [SRC-C8EA754D73-L000012](../IMPLEMENTATION_SCOPE.md#L12) | 12 | `""` | — |
| [SRC-C8EA754D73-L000013](../IMPLEMENTATION_SCOPE.md#L13) | 13 | `"- **التوجيه والمتابعة — VERIFIED ضمن الاختبارات الآلية:** كشف الأسئلة المرجعية الغامضة وتوحيد حل المتابعة وحدود السياق."` | — |
| [SRC-C8EA754D73-L000014](../IMPLEMENTATION_SCOPE.md#L14) | 14 | ``"- **عرض الأدلة وعمق البحث — VERIFIED ضمن الاختبارات الآلية:** لا تُعرض تغطية الأدلة على أنها احتمال صحة؛ واختيار العمق يقارن قيمة `deep` صراحةً."`` | — |
| [SRC-C8EA754D73-L000015](../IMPLEMENTATION_SCOPE.md#L15) | 15 | `"- **سلامة البحث وجلب الصفحات — VERIFIED ضمن الاختبارات المحددة:** حالات جلب مهيكلة، وتشخيصات موصلات، وحدود واضحة لفشل الجلب، ومنع التحويل التلقائي في الموصلات المغطاة بالاختبارات."` | — |
| [SRC-C8EA754D73-L000016](../IMPLEMENTATION_SCOPE.md#L16) | 16 | `"- **حماية API والمتصفح — VERIFIED ضمن الاختبارات المحددة:** رؤوس حماية وسياسة CSP واختبارات انحدار؛ هذا لا يغني عن تدقيق أمني شامل أو red-team مستقل."` | — |
| [SRC-C8EA754D73-L000017](../IMPLEMENTATION_SCOPE.md#L17) | 17 | ``"- **هوية البناء — CODE PATH TESTED:** صورة Docker تتيح SHA للبناء ويعرضه `/api/health`، ويقارن Hosted smoke SHA المتوقع بالمعلن. الاختبار الحي ضد خدمة مستضافة **NOT_RUN**."`` | — |
| [SRC-C8EA754D73-L000018](../IMPLEMENTATION_SCOPE.md#L18) | 18 | ``"- **الفهرسة والبحث المحلي — VERIFIED ضمن اختبارات المولد والبحث:** `docs/generate_index.py` يبني جرد الملفات والرموز وصفحات الأسطر؛ `docs/search_code.py` يتيح البحث محليًا دون API."`` | — |
| [SRC-C8EA754D73-L000019](../IMPLEMENTATION_SCOPE.md#L19) | 19 | ``"- **مسار SQLite — VERIFIED في الكود والاختبارات المحلية:** `OMARAI_DB_PATH` يحدد المسار؛ لا ينشئ Volume ولا يثبت استمرار البيانات لدى مزود استضافة."`` | — |
| [SRC-C8EA754D73-L000020](../IMPLEMENTATION_SCOPE.md#L20) | 20 | `""` | — |
| [SRC-C8EA754D73-L000021](../IMPLEMENTATION_SCOPE.md#L21) | 21 | `"## أدلة الاختبار وحدودها"` | — |
| [SRC-C8EA754D73-L000022](../IMPLEMENTATION_SCOPE.md#L22) | 22 | `""` | — |
| [SRC-C8EA754D73-L000023](../IMPLEMENTATION_SCOPE.md#L23) | 23 | `"- **CI على رأس PR #81 قبل الدمج:** [run #39955767221](https://github.com/mosabosama2030-oss/omarai/actions/runs/39955767221) نجح بالكامل: 384 اختبارًا على Python 3.11 و384 على Python 3.12، وRuff، وتصنيف مسارات الفهرسة، وتوليد الفهرس والتحقق منه، وبناء الحاوية واختبار API المحمي."` | — |
| [SRC-C8EA754D73-L000024](../IMPLEMENTATION_SCOPE.md#L24) | 24 | ``"- **دمج PR #81:** الالتزام `9f6674abf8679a0630d95b269b54a7ef8629c3bf`. رأس `main` الذي تحققنا من مطابقته هو `00a3ede039922c0c24097e89f653e6d3c984435d`؛ المقارنة بين `main` وهذا الالتزام أعادت `identical`."`` | — |
| [SRC-C8EA754D73-L000025](../IMPLEMENTATION_SCOPE.md#L25) | 25 | `"- **الإصلاح:** سباق الفهرس عولج في [PR #81](https://github.com/mosabosama2030-oss/omarai/pull/81): يختبر CI تصنيف المسارات، ويعيد توليد الفهرس في مساحة اختبار معزولة للتغييرات المختلطة، مع الإبقاء على الفحص الصارم عند تغييرات الفهرسة وحدها."` | — |
| [SRC-C8EA754D73-L000026](../IMPLEMENTATION_SCOPE.md#L26) | 26 | ``"- **CI على رأس main النهائي:** `NOT_CONFIRMED` في هذه المراجعة؛ نتيجة #39955767221 تخص رأس PR قبل الدمج، وواجهة التشغيل المتاحة هنا لا تكشف تشغيلات push على نحو يسمح بتأكيد تشغيل مستقل على `00a3ede...`. هذا ليس دليل فشل؛ يلزم فحص GitHub Actions مباشرة."`` | — |
| [SRC-C8EA754D73-L000027](../IMPLEMENTATION_SCOPE.md#L27) | 27 | ``"- اختبارات الاستضافة والموصلات الحية وجودة الإجابات الدلالية والنسخ/الاستعادة والحمل تبقى `NOT_RUN/UNKNOWN` حتى وجود أدلة مباشرة."`` | — |
| [SRC-C8EA754D73-L000028](../IMPLEMENTATION_SCOPE.md#L28) | 28 | `""` | — |
| [SRC-C8EA754D73-L000029](../IMPLEMENTATION_SCOPE.md#L29) | 29 | `"## غير مثبت أو خارج النطاق الحالي"` | — |
| [SRC-C8EA754D73-L000030](../IMPLEMENTATION_SCOPE.md#L30) | 30 | `""` | — |
| [SRC-C8EA754D73-L000031](../IMPLEMENTATION_SCOPE.md#L31) | 31 | ``"- **المزودون الأحياء والاستضافة:** `UNKNOWN / NOT_RUN` حتى اختبار كل موفر وخدمة مستهدفة فعليًا."`` | — |
| [SRC-C8EA754D73-L000032](../IMPLEMENTATION_SCOPE.md#L32) | 32 | `"- **جودة الإجابات الدلالية:** لا يثبت وجود استشهاد أو تشابه ألفاظ أن المصدر يستلزم الادعاء؛ التحقق الدلالي المستقل الشامل غير مثبت."` | — |
| [SRC-C8EA754D73-L000033](../IMPLEMENTATION_SCOPE.md#L33) | 33 | ``"- **SQLite والنسخ والاستعادة على المضيف:** `NOT_RUN` حتى يثبت بقاء البيانات بعد إعادة التشغيل/النشر ثم نجاح استعادة نسخة احتياطية."`` | — |
| [SRC-C8EA754D73-L000034](../IMPLEMENTATION_SCOPE.md#L34) | 34 | ``"- **الحمل والسعة:** `NOT_RUN`; semaphore ومحدد معدل العملية لا يثبتان throughput إنتاجيًا ولا تنسيقًا موزعًا."`` | — |
| [SRC-C8EA754D73-L000035](../IMPLEMENTATION_SCOPE.md#L35) | 35 | ``"- **تعدد المستأجرين — حالة فرع PR #145:** نواة tenant/user/membership/token/session وعزل CRUD/list/import/export موجودة ومجتازة لاختبارات CI على فرع PR #145؛ التشغيل المستهدف أولًا لشركة واحدة مع بنية متعددة المستأجرين. هذا غير موجود على `main` قبل الدمج، ولا توجد واجهة self-service لإدارة المستخدمين/العضويات، ولا قبول مستضاف أو اختبار backup/restore. لا يُعلن جاهزًا لتشغيل SaaS متعدد العملاء قبل استكمال provisioning واختبار الاستضافة ومراجعة الأدوار."`` | — |
| [SRC-C8EA754D73-L000036](../IMPLEMENTATION_SCOPE.md#L36) | 36 | `"- **Android/RTL:** القبول اليدوي لا يُغلق بنتائج Pytest فقط."` | — |
| [SRC-C8EA754D73-L000037](../IMPLEMENTATION_SCOPE.md#L37) | 37 | `"- **المراجعة الأمنية المستقلة:** لا تعتبر مكتملة دون تقرير فعلي مرتبط بـSHA وأدلة قابلة للمراجعة."` | — |
| [SRC-C8EA754D73-L000038](../IMPLEMENTATION_SCOPE.md#L38) | 38 | `""` | — |
| [SRC-C8EA754D73-L000039](../IMPLEMENTATION_SCOPE.md#L39) | 39 | `"## مصادر الحقيقة حسب الغرض"` | — |
| [SRC-C8EA754D73-L000040](../IMPLEMENTATION_SCOPE.md#L40) | 40 | `""` | — |
| [SRC-C8EA754D73-L000041](../IMPLEMENTATION_SCOPE.md#L41) | 41 | `"- تفاصيل العيوب والمعرّفات ومعايير الإغلاق: [سجل المعالجة المركزي](OMARAI_REMEDIATION_REGISTER_AR.md)."` | — |
| [SRC-C8EA754D73-L000042](../IMPLEMENTATION_SCOPE.md#L42) | 42 | `"- نتيجة ما بعد الدمج وحدود الأدلة: [تقرير التحقق بعد الدمج](OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md)."` | — |
| [SRC-C8EA754D73-L000043](../IMPLEMENTATION_SCOPE.md#L43) | 43 | `"- أنواع الاختبار والنتائج التاريخية وحدودها: [مصفوفة أدلة الاختبار](OMARAI_TEST_EVIDENCE_MATRIX_AR.md)."` | — |
| [SRC-C8EA754D73-L000044](../IMPLEMENTATION_SCOPE.md#L44) | 44 | `"- قواعد المساهمة وتنظيم المستودع: [AGENTS.md](../AGENTS.md) و[دليل الوثائق](README.md)."` | — |
| [SRC-C8EA754D73-L000045](../IMPLEMENTATION_SCOPE.md#L45) | 45 | `""` | — |
| [SRC-C8EA754D73-L000046](../IMPLEMENTATION_SCOPE.md#L46) | 46 | ``"لا تُرقَّ حالة إلى `VERIFIED` دون اختبار محدد على SHA/بيئة واضحة. لا تُحوَّل `NOT_RUN` أو `UNKNOWN` إلى نجاح لمجرد وجود كود أو إعداد أو ملف توثيق."`` | — |
## وثائق وفهرسة

### FILE-53E640B937 — [docs/OMARAI_AGENTIC_RAG_ROADMAP_AR.md](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-53E640B937-L000001](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L1) | 1 | `"# خطة تنفيذ RAG الوكيلي وسلامة الأدلة في Omarai"` | — |
| [SRC-53E640B937-L000002](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L2) | 2 | `""` | — |
| [SRC-53E640B937-L000003](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L3) | 3 | ``"**تاريخ الحالة:** 28 أكتوبر 2026. يبدأ هذا العمل من رأس `main` بعد دمج PR #113. نجاح الاختبارات الآلية لا يُعد قبولًا حيًا ولا إثباتًا لصحة الإجابات."`` | — |
| [SRC-53E640B937-L000004](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L4) | 4 | `""` | — |
| [SRC-53E640B937-L000005](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L5) | 5 | `"## تعريف النظام المستهدف"` | — |
| [SRC-53E640B937-L000006](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L6) | 6 | `""` | — |
| [SRC-53E640B937-L000007](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L7) | 7 | `"يستقبل Omarai سؤالًا، يحدد المقصد والسياق، يقرر الحاجة إلى الاسترجاع، يفكك الطلب المركب إلى محاور، يخطط لاستعلامات محدودة، يسترجع مصادر عامة آمنة أو معرفة محلية متاحة، يقرأ الصفحات، يربط المقاطع المرشحة بالاستشهادات، يصوغ الإجابة ويراجعها، ثم يكشف النقص أو يمتنع عنه. يجب أن تبقى هذه المراحل قابلة للفحص ومحدودة الزمن والموارد."` | — |
| [SRC-53E640B937-L000008](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L8) | 8 | `""` | — |
| [SRC-53E640B937-L000009](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L9) | 9 | `"## سجل البنود وحالتها"` | — |
| [SRC-53E640B937-L000010](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L10) | 10 | `""` | — |
| [SRC-53E640B937-L000011](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L11) | 11 | `"\| البند \| الحالة \| الدليل والحد المتبقي \|"` | — |
| [SRC-53E640B937-L000012](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L12) | 12 | `"\|---\|---\|---\|"` | — |
| [SRC-53E640B937-L000013](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L13) | 13 | ``"\| نموذج لغوي داخل غلاف تنفيذي \| **PARTIAL** \| `WebAgent` يضبط المهلة والميزانية والتشخيصات. وجود الاعتماديات لا يثبت أن مزود النموذج حي. \|"`` | — |
| [SRC-53E640B937-L000014](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L14) | 14 | ``"\| فهم المقصد والمتابعة والسياق \| **FIXED_AND_TESTED ضمن نطاق CI** \| `intent_router.py` و`dialogue_state.py` وحل المتابعة؛ لا توجد ذاكرة دلالية دائمة عابرة للجلسات مثبتة. \|"`` | — |
| [SRC-53E640B937-L000015](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L15) | 15 | `"\| تفكيك الأسئلة المركبة \| **FIXED_AND_TESTED على PR #113 المدمج** \| محاور المقارنة والطلبات المركبة وتخطيط استعلامات؛ المطابقة اللفظية ليست فهمًا دلاليًا كاملًا. \|"` | — |
| [SRC-53E640B937-L000016](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L16) | 16 | ``"\| RAG كأداة داخل حلقة قرار \| **PARTIAL** \| `_search_web` و`_collect_research`؛ الاسترجاع الحالي بحث ويب عام، لا قاعدة معرفة خاصة مفهرسة. \|"`` | — |
| [SRC-53E640B937-L000017](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L17) | 17 | `"\| الاسترجاع التكراري الموجه \| **ADDED IN THIS PR; CI PENDING** \| حجز عدد صغير من الاستعلامات لمحاور بلا مرشحات نصية أولية، وإعادة البحث ضمن سقف الاستعلامات والميزانية الحاليين. \|"` | — |
| [SRC-53E640B937-L000018](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L18) | 18 | `"\| سلامة الموصلات والروابط \| **EXISTING / TESTED IN CI SCOPE** \| فحوص URL العام وSSRF وقائمة الحظر والمهل والميزانية. لا يثبت CI توافر كل مزود حيًا. \|"` | — |
| [SRC-53E640B937-L000019](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L19) | 19 | ``"\| سجل مقطع ← استشهاد ← مصدر \| **ADDED IN THIS PR; CI PENDING** \| `agents/claim_evidence.py` يربط كل مقطع مرشح بالاستشهادات وعناوين المصادر وروابطها ونوع النص، ويكشف الاستشهاد الغائب أو خارج النطاق. \|"`` | — |
| [SRC-53E640B937-L000020](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L20) | 20 | `"\| الاستشهادات الإلزامية والتوليد المقيد \| **PARTIAL** \| إزالة المؤشرات خارج نطاق المصدر ومراجعة النموذج والفحص اللفظي؛ لا يثبت أي منها الاستلزام الدلالي. \|"` | — |
| [SRC-53E640B937-L000021](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L21) | 21 | `"\| كشف الهلوسة والتحقق الدلالي \| **PARTIAL / NOT INDEPENDENTLY VERIFIED** \| مراجعة بمساعدة نموذج وفحوص حتمية. لا توجد هنا مراجعة مستقلة لكل ادعاء ببيانات مرجعية. \|"` | — |
| [SRC-53E640B937-L000022](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L22) | 22 | `"\| قواعد الكتابة والطلاقة \| **IMPROVED IN THIS PR; CI PENDING** \| إضافة قواعد للإجابة المباشرة، والجمل القصيرة، وتغطية الأجزاء، والاستشهاد من المصادر المتاحة، وإظهار المجهول. أمثلة few-shot معتمدة لم تُضف بعد. \|"` | — |
| [SRC-53E640B937-L000023](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L23) | 23 | `"\| الذاكرة \| **PARTIAL** \| تاريخ محادثة محدود ومنقّى داخل الطلب؛ مخزن دائم بصلاحيات ومدة احتفاظ غير مثبت. \|"` | — |
| [SRC-53E640B937-L000024](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L24) | 24 | `"\| الوكلاء المتخصصون \| **PIPELINE STAGES EXIST** \| التوجيه والتخطيط والاسترجاع والتوليد والمراجعة مراحل/وظائف قابلة للاختبار، لا وكلاء دائمون أو Meta-Agent. \|"` | — |
| [SRC-53E640B937-L000025](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L25) | 25 | `"\| تقييم مستمر \| **PARTIAL** \| corpus من 45 حالة ومدقق بنية ومشغّل حي لا يمنح PASS تلقائيًا. الصحة الدلالية تحتاج مرجعًا ذهبيًا/تحكيمًا بشريًا. \|"` | — |
| [SRC-53E640B937-L000026](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L26) | 26 | `"\| الاسترجاع/الأمانة/الصحة/الطلاقة \| **NOT FULLY MEASURED** \| المؤشرات الحالية تقنية/لفظية. لا تُسمى دقة أو Faithfulness دلالية ولا أرقام RAGAS دون بيانات تسميات. \|"` | — |
| [SRC-53E640B937-L000027](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L27) | 27 | `"\| الضبط الدقيق SFT/RL \| **NOT RUN / DEFERRED** \| لا توجد مجموعة تدريب بشرية منقحة وتجربة مقارنة وميزانية تدريب مثبتة. \|"` | — |
| [SRC-53E640B937-L000028](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L28) | 28 | `"\| قاعدة معرفة داخلية \| **NOT IMPLEMENTED BY THIS PR** \| يلزم تحديد الوثائق المسموح بها وحدودها وتقسيمها وفهرستها وتحديثها وصلاحياتها. \|"` | — |
| [SRC-53E640B937-L000029](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L29) | 29 | `"\| اختبار الاستضافة الحي \| **NOT RUN** \| يتطلب مصادقة في البيئة، وتطابق SHA المنشور، وموافقة مستقلة؛ لم نغيّر إعداد الاستضافة. \|"` | — |
| [SRC-53E640B937-L000030](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L30) | 30 | `""` | — |
| [SRC-53E640B937-L000031](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L31) | 31 | `"## السلوك المضاف"` | — |
| [SRC-53E640B937-L000032](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L32) | 32 | `""` | — |
| [SRC-53E640B937-L000033](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L33) | 33 | `"### حلقة استرجاع محكومة"` | — |
| [SRC-53E640B937-L000034](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L34) | 34 | `""` | — |
| [SRC-53E640B937-L000035](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L35) | 35 | `"1. يقرأ المسار سقف الاستعلامات المحدد."` | — |
| [SRC-53E640B937-L000036](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L36) | 36 | `"2. يحجز حتى ثلاثة استعلامات بحسب عدد المحاور والسقف لإعادة البحث."` | — |
| [SRC-53E640B937-L000037](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L37) | 37 | `"3. يبحث أوليًا ويحسب المحاور التي لا يظهر لها أي مرشح لفظي في المصادر المبدئية."` | — |
| [SRC-53E640B937-L000038](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L38) | 38 | `"4. يعطي استعلامات إصلاح تلك المحاور الأولوية، ثم يسمح بتوسعة عامة فقط في البحث العميق وعند بقاء سعة."` | — |
| [SRC-53E640B937-L000039](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L39) | 39 | `"5. يجمع النتائج ويعيد تكوين سجل الأدلة ضمن سقف الطلب."` | — |
| [SRC-53E640B937-L000040](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L40) | 40 | `"6. إن ظلت الفجوة، تظهر للمستخدم ولا تتحول إلى تخمين."` | — |
| [SRC-53E640B937-L000041](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L41) | 41 | `""` | — |
| [SRC-53E640B937-L000042](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L42) | 42 | `"### سجل الأدلة"` | — |
| [SRC-53E640B937-L000043](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L43) | 43 | `""` | — |
| [SRC-53E640B937-L000044](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L44) | 44 | ``"لكل مقطع نصي محدود: رقم المقطع، النص، فهارس الاستشهاد، عنوان المصدر والرابط ونوع النص (صفحة مستخرجة، مقتطف، عنوان فقط)، وناتج الفحص اللفظي عند توفره. وحدة السجل «مقطع مرشح» وليست ادعاءً مصنفًا دلاليًا. يعرض السجل صراحةً `semantic_verification=false` و`claim_entailment=not_checked`."`` | — |
| [SRC-53E640B937-L000045](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L45) | 45 | `""` | — |
| [SRC-53E640B937-L000046](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L46) | 46 | `"### قواعد التوليد"` | — |
| [SRC-53E640B937-L000047](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L47) | 47 | `""` | — |
| [SRC-53E640B937-L000048](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L48) | 48 | `"النتيجة أولًا، جمل قصيرة، تقسيم الإجابة بحسب محاور الطلب، عدم إسقاط محور بصمت، الاستشهاد من قائمة المسترجع فقط، إظهار النقص وعدم اختلاق روابط أو أرقام أو تواريخ، والتعامل مع نصوص الويب باعتبارها بيانات لا تعليمات."` | — |
| [SRC-53E640B937-L000049](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L49) | 49 | `""` | — |
| [SRC-53E640B937-L000050](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L50) | 50 | `"## بوابات القبول"` | — |
| [SRC-53E640B937-L000051](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L51) | 51 | `""` | — |
| [SRC-53E640B937-L000052](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L52) | 52 | `"- **A — CI:** Ruff، واختبارات Python 3.11/3.12، واختبار الإصلاح الموجه، وسجل الادعاء/الاستشهاد، وعرض الواجهة، وبناء الحاوية وAPI smoke."` | — |
| [SRC-53E640B937-L000053](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L53) | 53 | `"- **B — Review:** مراجعة بشرية للكود والنتائج قبل اعتماد PR."` | — |
| [SRC-53E640B937-L000054](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L54) | 54 | ``"- **C — Semantic benchmark:** أسئلة حقيقية مع مصادر مرجعية؛ تسميات صلة الاسترجاع وأحكام لكل ادعاء للأمانة والصحة والأسلوب. ما لم يُختبر يبقى `NOT_TESTED`."`` | — |
| [SRC-53E640B937-L000055](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L55) | 55 | `"- **D — Hosted acceptance:** موافقة منفصلة، اختبار محدود، وعدم كشف الأسرار، وتسجيل SHA المنشور."` | — |
| [SRC-53E640B937-L000056](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L56) | 56 | `"- **E — Fine-tuning / RAGAS:** لا يبدأ قبل إعداد بيانات مرجعية وخط أساس وميزانية قابلة للقياس."` | — |
| [SRC-53E640B937-L000057](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L57) | 57 | `""` | — |
| [SRC-53E640B937-L000058](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L58) | 58 | `"## قواعد لا نتجاوزها"` | — |
| [SRC-53E640B937-L000059](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L59) | 59 | `""` | — |
| [SRC-53E640B937-L000060](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L60) | 60 | `"- لا يرفع الملف أو وجود الدالة حالة بند إلى VERIFIED وحده."` | — |
| [SRC-53E640B937-L000061](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L61) | 61 | `"- لا تُعرض تغطية المحاور على أنها نسبة ثقة."` | — |
| [SRC-53E640B937-L000062](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L62) | 62 | `"- لا يعد وجود الاستشهاد دليلًا على صحته."` | — |
| [SRC-53E640B937-L000063](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L63) | 63 | `"- لا تتجاوز الحلقة ميزانية الاستعلامات والوقت."` | — |
| [SRC-53E640B937-L000064](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L64) | 64 | `"- لا تُسجل الأسرار."` | — |
| [SRC-53E640B937-L000065](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L65) | 65 | `"- لا دمج ولا نشر مستضاف من دون قرار المدير البشري."` | — |
| [SRC-53E640B937-L000066](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L66) | 66 | `""` | — |
| [SRC-53E640B937-L000067](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L67) | 67 | `""` | — |
| [SRC-53E640B937-L000068](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L68) | 68 | `"## إضافة تالية لنظام التقييم — 28 أكتوبر 2026"` | — |
| [SRC-53E640B937-L000069](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L69) | 69 | `""` | — |
| [SRC-53E640B937-L000070](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L70) | 70 | ``"أضيف إلى الفرع سكربت محلي دون اتصال باسم `scripts/score_answer_quality_reviews.py` لاشتقاق:"`` | — |
| [SRC-53E640B937-L000071](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L71) | 71 | `"- Retrieval Precision وRecall من عدّ مرشحين ذوي صلة ومجموع المرشحين والمصادر/الحقائق ذات الصلة المتاحة."` | — |
| [SRC-53E640B937-L000072](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L72) | 72 | `"- Faithfulness من عدد الادعاءات التي حكم المراجع بأنها مسندة إلى دليل وعدد الادعاءات التي راجعها."` | — |
| [SRC-53E640B937-L000073](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L73) | 73 | `"- Correctness من الحقائق التي حكم المراجع بصحتها من مجموع الحقائق التي راجعها."` | — |
| [SRC-53E640B937-L000074](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L74) | 74 | `"- Citation Support من الاستشهادات التي وجد المراجع أنها تسند الجملة من الاستشهادات التي فحصها."` | — |
| [SRC-53E640B937-L000075](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L75) | 75 | `"- جودة الكتابة من تقييم بشري من 1 إلى 5."` | — |
| [SRC-53E640B937-L000076](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L76) | 76 | `""` | — |
| [SRC-53E640B937-L000077](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L77) | 77 | ``"يقبل السكربت أحكامًا صريحة فقط، ويرفض معرفات الحالات المجهولة والقيم غير المتسقة، ويبقي كل حالة غير مراجعة في `NOT_TESTED`. المقاييس تجميعية من تعليقات بشرية وليست درجات RAGAS أو تقييمًا آليًا. لا تُملأ أي نتائج تجريبية نيابة عن المراجع."`` | — |
| [SRC-53E640B937-L000078](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L78) | 78 | `""` | — |
| [SRC-53E640B937-L000079](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L79) | 79 | `""` | — |
| [SRC-53E640B937-L000080](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L80) | 80 | `"### قاعدة أمثلة أسلوبية موجهة"` | — |
| [SRC-53E640B937-L000081](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L81) | 81 | `"تتضمن مطالبة التوليد الآن مثالين قصيرين: استشهاد مضبوط بحدود ما يقوله المصدر، وامتناع صريح عندما لا تتضمن النتائج دليلًا كافيًا. المثال معلن على أنه توضيحي ولا يجوز نقل وقائعه للإجابة الحالية ما لم تؤيدها المصادر الفعلية؛ أضيف اختبار وحدات للتحقق من وصول القاعدة إلى مطالبة التوليد."` | — |
| [SRC-53E640B937-L000082](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L82) | 82 | `""` | — |
| [SRC-53E640B937-L000083](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L83) | 83 | `""` | — |
| [SRC-53E640B937-L000084](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L84) | 84 | `"### تشغيل التقييم البشري القابل للتكرار"` | — |
| [SRC-53E640B937-L000085](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L85) | 85 | `""` | — |
| [SRC-53E640B937-L000086](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L86) | 86 | `"أداة تجميع المقاييس لا تستدعي النموذج ولا تزعم تقييمًا تلقائيًا. ينشئ المراجع ملف JSON مستقلًا مثل المثال التالي؛ **الأرقام توضيحية وهمية لشرح المخطط فقط وليست نتائج Omarai**:"` | — |
| [SRC-53E640B937-L000087](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L87) | 87 | `""` | — |
| [SRC-53E640B937-L000088](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L88) | 88 | ````"```json"```` | — |
| [SRC-53E640B937-L000089](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L89) | 89 | `"{"` | — |
| [SRC-53E640B937-L000090](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L90) | 90 | `"  \"schema_version\": \"1.0\","` | — |
| [SRC-53E640B937-L000091](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L91) | 91 | `"  \"reviews\": ["` | — |
| [SRC-53E640B937-L000092](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L92) | 92 | `"    {"` | — |
| [SRC-53E640B937-L000093](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L93) | 93 | `"      \"case_id\": \"AQ-007\","` | — |
| [SRC-53E640B937-L000094](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L94) | 94 | `"      \"status\": \"REVIEWED\","` | — |
| [SRC-53E640B937-L000095](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L95) | 95 | `"      \"retrieval\": {"` | — |
| [SRC-53E640B937-L000096](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L96) | 96 | `"        \"relevant_retrieved\": 3,"` | — |
| [SRC-53E640B937-L000097](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L97) | 97 | `"        \"retrieved_count\": 5,"` | — |
| [SRC-53E640B937-L000098](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L98) | 98 | `"        \"relevant_available\": 4"` | — |
| [SRC-53E640B937-L000099](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L99) | 99 | `"      },"` | — |
| [SRC-53E640B937-L000100](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L100) | 100 | `"      \"faithfulness\": {"` | — |
| [SRC-53E640B937-L000101](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L101) | 101 | `"        \"supported_claims\": 4,"` | — |
| [SRC-53E640B937-L000102](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L102) | 102 | `"        \"reviewed_claims\": 5"` | — |
| [SRC-53E640B937-L000103](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L103) | 103 | `"      },"` | — |
| [SRC-53E640B937-L000104](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L104) | 104 | `"      \"correctness\": {"` | — |
| [SRC-53E640B937-L000105](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L105) | 105 | `"        \"correct_facts\": 4,"` | — |
| [SRC-53E640B937-L000106](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L106) | 106 | `"        \"reviewed_facts\": 5"` | — |
| [SRC-53E640B937-L000107](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L107) | 107 | `"      },"` | — |
| [SRC-53E640B937-L000108](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L108) | 108 | `"      \"citations\": {"` | — |
| [SRC-53E640B937-L000109](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L109) | 109 | `"        \"supported_citations\": 3,"` | — |
| [SRC-53E640B937-L000110](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L110) | 110 | `"        \"reviewed_citations\": 4"` | — |
| [SRC-53E640B937-L000111](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L111) | 111 | `"      },"` | — |
| [SRC-53E640B937-L000112](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L112) | 112 | `"      \"writing_quality\": 4"` | — |
| [SRC-53E640B937-L000113](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L113) | 113 | `"    },"` | — |
| [SRC-53E640B937-L000114](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L114) | 114 | `"    {"` | — |
| [SRC-53E640B937-L000115](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L115) | 115 | `"      \"case_id\": \"AQ-008\","` | — |
| [SRC-53E640B937-L000116](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L116) | 116 | `"      \"status\": \"NOT_TESTED\","` | — |
| [SRC-53E640B937-L000117](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L117) | 117 | `"      \"notes\": \"لم يراجع بشر الإجابة حتى الآن.\""` | — |
| [SRC-53E640B937-L000118](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L118) | 118 | `"    }"` | — |
| [SRC-53E640B937-L000119](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L119) | 119 | `"  ]"` | — |
| [SRC-53E640B937-L000120](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L120) | 120 | `"}"` | — |
| [SRC-53E640B937-L000121](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L121) | 121 | ````"```"```` | — |
| [SRC-53E640B937-L000122](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L122) | 122 | `""` | — |
| [SRC-53E640B937-L000123](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L123) | 123 | `"ثم يحسب الملخص:"` | — |
| [SRC-53E640B937-L000124](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L124) | 124 | `""` | — |
| [SRC-53E640B937-L000125](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L125) | 125 | ````"```bash"```` | — |
| [SRC-53E640B937-L000126](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L126) | 126 | `"python scripts/score_answer_quality_reviews.py --reviews reviews.json --corpus tests/fixtures/answer_quality_cases.json --out scorecard.json"` | — |
| [SRC-53E640B937-L000127](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L127) | 127 | ````"```"```` | — |
| [SRC-53E640B937-L000128](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L128) | 128 | `""` | — |
| [SRC-53E640B937-L000129](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L129) | 129 | `"- **Precision:** عدد عناصر الاسترجاع التي حكم المراجع بصِلتها ÷ إجمالي العناصر المسترجعة بعد إزالة التكرار."` | — |
| [SRC-53E640B937-L000130](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L130) | 130 | `"- **Recall:** عدد العناصر ذات الصلة المسترجعة ÷ إجمالي العناصر ذات الصلة المعروفة في مجموعة مرجعية محددة؛ إن لم يتوفر هذا المقام تبقى النتيجة غير قابلة للقياس."` | — |
| [SRC-53E640B937-L000131](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L131) | 131 | `"- **Faithfulness:** الادعاءات التي حكم المراجع بأنها مسندة إلى الدليل ÷ الادعاءات التي فحصها."` | — |
| [SRC-53E640B937-L000132](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L132) | 132 | `"- **Correctness:** الحقائق الصحيحة وفق مرجع موثوق ÷ الحقائق التي فُحصت."` | — |
| [SRC-53E640B937-L000133](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L133) | 133 | `"- **Citation Support:** الاستشهادات التي يسند مصدرها الجملة وفق المراجع ÷ الاستشهادات التي فُحصت."` | — |
| [SRC-53E640B937-L000134](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L134) | 134 | `"- **Writing quality:** متوسط تقدير بشري من 1 إلى 5."` | — |
| [SRC-53E640B937-L000135](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L135) | 135 | `""` | — |
| [SRC-53E640B937-L000136](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L136) | 136 | ``"يجب مراجعة النص الأصلي للمصدر لا عنوانه فقط. يفضل أن يراجع شخصان عينة مشتركة وأن تتم تسوية اختلافاتهما قبل المقارنة بين الإصدارات. حالة `NOT_TESTED` لا تدخل في أي بسط أو مقام ولا تتحول إلى PASS. هذه المقاييس مراجعات بشرية مجمعة وليست تطبيقًا لـRAGAS."`` | — |
## وثائق وفهرسة

### FILE-BA40E88B07 — [docs/OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-BA40E88B07-L000001](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L1) | 1 | `"# تدقيق معمارية Omarai والخيارات التقنية والممارسات الأمنية"` | — |
| [SRC-BA40E88B07-L000002](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L2) | 2 | `"**التاريخ:** 1 نوفمبر 2026  "` | — |
| [SRC-BA40E88B07-L000003](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L3) | 3 | ``"**خط الأساس:** `main` عند `63b7dd01889de4aadd66acea90a2415b33376e2e`  "`` | — |
| [SRC-BA40E88B07-L000004](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L4) | 4 | ``"**فرع الإصلاح:** `fix/p0-core-consolidated-2026-11-01`  "`` | — |
| [SRC-BA40E88B07-L000005](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L5) | 5 | `"**حالة الوثيقة:** مراجعة مصدرية؛ تغييرات الفرع غير مدمجة."` | — |
| [SRC-BA40E88B07-L000006](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L6) | 6 | `""` | — |
| [SRC-BA40E88B07-L000007](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L7) | 7 | `"## 1. الخلاصة التنفيذية"` | — |
| [SRC-BA40E88B07-L000008](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L8) | 8 | `""` | — |
| [SRC-BA40E88B07-L000009](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L9) | 9 | `"**VERIFIED:** Omarai تطبيق Python modular monolith بواجهة HTTP مخصصة، ومحرك بحث/إجابة، وSQLite لتخزين العملاء، وموصلات بحث، وحدود للطلبات والموارد، واختبارات CI على Python 3.11 و3.12."` | — |
| [SRC-BA40E88B07-L000010](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L10) | 10 | `""` | — |
| [SRC-BA40E88B07-L000011](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L11) | 11 | `"**VERIFIED:** توجد آليات SSRF قوية نسبيًا في جلب الصفحات: رفض الوجهات المحلية، حل DNS والتحقق من كل عنوان، الاتصال بعنوان IP مثبت بدل إعادة حل الاسم، تعطيل proxy من البيئة، وعدم اتباع redirects تلقائيًا؛ كل redirect يدوي يعاد التحقق منه."` | — |
| [SRC-BA40E88B07-L000012](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L12) | 12 | `""` | — |
| [SRC-BA40E88B07-L000013](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L13) | 13 | ``"**VERIFIED:** عزل العملاء يُبنى على هوية مستخرجة من credential موثوق، وليس على `tenant_id` المرسل في جسم الطلب. استعلامات leads الأساسية scoped بالـtenant، مع اختبارات تمنع تزوير tenant_id والوصول المتبادل."`` | — |
| [SRC-BA40E88B07-L000014](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L14) | 14 | `""` | — |
| [SRC-BA40E88B07-L000015](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L15) | 15 | `"**VERIFIED:** كان المتصفح يحتفظ برمز API في Web Storage. أزيل هذا المسار في الفرع واستُبدل بجلسات opaque خادمية، مع cookie محمي وCSRF Origin check. هذه خطوة أمنية مهمة، لكنها تحتاج اعتماد CI النهائي ومراجعة بشرية قبل الدمج."` | — |
| [SRC-BA40E88B07-L000016](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L16) | 16 | `""` | — |
| [SRC-BA40E88B07-L000017](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L17) | 17 | `"**INFERRED:** أفضل خيار حالي هو الإبقاء على modular monolith منضبط بدل تفكيك الخدمات. لا توجد أدلة حمل أو فرق تشغيل أو حدود ملكية بيانات تبرر microservices الآن."` | — |
| [SRC-BA40E88B07-L000018](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L18) | 18 | `""` | — |
| [SRC-BA40E88B07-L000019](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L19) | 19 | `"**UNKNOWN:** القبول الحي على الاستضافة، استمرار قاعدة البيانات بعد إعادة إنشاء الحاوية، النسخ الاحتياطي والاستعادة، الحمل متعدد العمليات، واتصال مزودي النماذج الفعلي."` | — |
| [SRC-BA40E88B07-L000020](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L20) | 20 | `""` | — |
| [SRC-BA40E88B07-L000021](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L21) | 21 | `"## 2. المعمارية المرصودة"` | — |
| [SRC-BA40E88B07-L000022](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L22) | 22 | `""` | — |
| [SRC-BA40E88B07-L000023](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L23) | 23 | ``"- `web/`: واجهتا Agent وDashboard."`` | — |
| [SRC-BA40E88B07-L000024](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L24) | 24 | ``"- `api/omarai.py`: HTTP ingress، المصادقة، Origin/CORS، تحديد المعدل، حدود الجسم والمهلة، وتوجيه API."`` | — |
| [SRC-BA40E88B07-L000025](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L25) | 25 | ``"- `agents/web_agent.py`: تنسيق البحث، جلب الصفحات، توليد الإجابة، تسجيل الأدلة، وطلبات النماذج."`` | — |
| [SRC-BA40E88B07-L000026](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L26) | 26 | ``"- `agents/omarai.py`: تحليل أولي لإشارات الشراء وLeadStore وtenant/user/membership/token/session storage."`` | — |
| [SRC-BA40E88B07-L000027](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L27) | 27 | ``"- `agents/semantic_claim_verifier.py`: تقييم دعم الادعاء من المصدر المحدد."`` | — |
| [SRC-BA40E88B07-L000028](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L28) | 28 | ``"- `RequestBudget` ومحددات التزامن: ميزانية للطلب وعمليات البحث/النماذج وجلب الصفحات."`` | — |
| [SRC-BA40E88B07-L000029](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L29) | 29 | ``"- `tests/`: اختبارات وحدات وتكامل وأمن وعقود قبول."`` | — |
| [SRC-BA40E88B07-L000030](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L30) | 30 | `""` | — |
| [SRC-BA40E88B07-L000031](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L31) | 31 | `"هذا **تطبيق أحادي العملية متعدد الوحدات**، وليس مجموعة microservices. يجب الحفاظ على حدود الوحدات وعقودها قبل التفكير في توزيعها."` | — |
| [SRC-BA40E88B07-L000032](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L32) | 32 | `""` | — |
| [SRC-BA40E88B07-L000033](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L33) | 33 | `"## 3. قرارات الخيارات التقنية"` | — |
| [SRC-BA40E88B07-L000034](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L34) | 34 | `""` | — |
| [SRC-BA40E88B07-L000035](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L35) | 35 | `"### 3.1 Modular Monolith مقابل Microservices"` | — |
| [SRC-BA40E88B07-L000036](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L36) | 36 | `""` | — |
| [SRC-BA40E88B07-L000037](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L37) | 37 | `"**القرار — PROPOSED/اعتماد هذا المسار:** Modular monolith مع حدود واضحة بين API والسياسة ومحرك البحث والموصلات والتخزين والتحقق."` | — |
| [SRC-BA40E88B07-L000038](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L38) | 38 | `""` | — |
| [SRC-BA40E88B07-L000039](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L39) | 39 | `"الأسباب:"` | — |
| [SRC-BA40E88B07-L000040](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L40) | 40 | `"- التطبيق الحالي يعتمد على SQLite وعمليات Python متزامنة؛ توزيع الوحدات الآن يضيف اتصالات شبكية ومصادقة بين الخدمات وتناسقًا موزعًا دون دليل أن ذلك يحل اختناقًا مثبتًا."` | — |
| [SRC-BA40E88B07-L000041](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L41) | 41 | `"- اختبارات الوحدة والتكامل الحالية تتيح تغييرًا صغيرًا وقابلًا للمراجعة."` | — |
| [SRC-BA40E88B07-L000042](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L42) | 42 | `"- لا تنشأ وكلاء دائمون أو Meta-Agent أو توليد ذاتي للكود قبل استقرار السياسات والعقود."` | — |
| [SRC-BA40E88B07-L000043](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L43) | 43 | `""` | — |
| [SRC-BA40E88B07-L000044](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L44) | 44 | `"### 3.2 HTTP Runtime"` | — |
| [SRC-BA40E88B07-L000045](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L45) | 45 | `""` | — |
| [SRC-BA40E88B07-L000046](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L46) | 46 | ``"**VERIFIED:** الخادم يستخدم `http.server` / `BaseHTTPRequestHandler` مع طبقات حماية مخصصة: حدود حجم الطلب، deadline للقراءة، حد اتصالات متزامنة، معدل لكل IP، headers، وفحص Origin."`` | — |
| [SRC-BA40E88B07-L000047](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L47) | 47 | `""` | — |
| [SRC-BA40E88B07-L000048](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L48) | 48 | ``"**تحذير رسمي:** وثائق Python تقول إن `http.server` ليس موصى به للإنتاج، ويطبق فحوصات أمنية أساسية فقط. وجود hardening في التطبيق لا يحول مكتبة الاختبار/الخدمة البسيطة تلقائيًا إلى خادم إنتاج مدعوم."`` | — |
| [SRC-BA40E88B07-L000049](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L49) | 49 | `""` | — |
| [SRC-BA40E88B07-L000050](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L50) | 50 | `"**PROPOSED — P1:** تقييم انتقال محدود إلى WSGI/ASGI runtime مدعوم (مثل Waitress أو Uvicorn) مع إبقاء عقود API الحالية واختبارات قبول HTTP. لا أنصح بترحيل واسع داخل حزمة P0 الحالية؛ يجب أن يكون له PR مستقل ومقارنة أداء وتوافق وTimeout/Concurrency tests."` | — |
| [SRC-BA40E88B07-L000051](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L51) | 51 | `""` | — |
| [SRC-BA40E88B07-L000052](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L52) | 52 | `"### 3.3 SQLite مقابل PostgreSQL"` | — |
| [SRC-BA40E88B07-L000053](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L53) | 53 | `""` | — |
| [SRC-BA40E88B07-L000054](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L54) | 54 | `"**VERIFIED:**"` | — |
| [SRC-BA40E88B07-L000055](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L55) | 55 | `"- SQLite مناسب كبداية لنسخة واحدة وقاعدة محلية دائمة."` | — |
| [SRC-BA40E88B07-L000056](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L56) | 56 | ``"- كل اتصال يفعّل `PRAGMA foreign_keys=ON`."`` | — |
| [SRC-BA40E88B07-L000057](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L57) | 57 | ``"- `sqlite3.connect(timeout=10)` يحدد انتظار القفل، وأضيف wrapper يغلق الاتصال دائمًا بعد commit/rollback."`` | — |
| [SRC-BA40E88B07-L000058](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L58) | 58 | `"- الجلسات والرموز وعضويات المستخدمين والـleads مرتبطة بمفاتيح وعلاقات tenant."` | — |
| [SRC-BA40E88B07-L000059](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L59) | 59 | `""` | — |
| [SRC-BA40E88B07-L000060](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L60) | 60 | `"**PROPOSED:**"` | — |
| [SRC-BA40E88B07-L000061](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L61) | 61 | `"- الاستمرار على SQLite للتشغيل الأولي أحادي النسخة، مع volume دائم ونسخ احتياطي/استعادة مجربين."` | — |
| [SRC-BA40E88B07-L000062](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L62) | 62 | `"- عدم تفعيل WAL أو تغيير journal mode دون اختبار backup/restore والتزامن على نفس volume."` | — |
| [SRC-BA40E88B07-L000063](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L63) | 63 | `"- الانتقال إلى PostgreSQL قبل تشغيل عدة replicas أو الحاجة إلى كتابة متزامنة موزعة أو إدارة مركزية لقاعدة مشتركة. SQLite لا يقدم حدًا موزعًا لمحددات المعدل أو التزامن."` | — |
| [SRC-BA40E88B07-L000064](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L64) | 64 | `""` | — |
| [SRC-BA40E88B07-L000065](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L65) | 65 | `"### 3.4 المصادقة والجلسات وعزل المستأجرين"` | — |
| [SRC-BA40E88B07-L000066](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L66) | 66 | `""` | — |
| [SRC-BA40E88B07-L000067](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L67) | 67 | `"**VERIFIED في فرع الإصلاح:**"` | — |
| [SRC-BA40E88B07-L000068](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L68) | 68 | ``"- bearer token لا يُخزن في `localStorage` أو `sessionStorage`."`` | — |
| [SRC-BA40E88B07-L000069](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L69) | 69 | ``"- POST `/api/session` يتحقق من API token ثم ينشئ session ID عشوائيًا."`` | — |
| [SRC-BA40E88B07-L000070](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L70) | 70 | ``"- لا يُخزن session ID خامًا؛ تحفظ بصمته SHA-256 في `web_sessions`."`` | — |
| [SRC-BA40E88B07-L000071](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L71) | 71 | ``"- cookie العام يستخدم `__Host-` مع `Secure; HttpOnly; SameSite=Strict; Path=/` ومدة 8 ساعات."`` | — |
| [SRC-BA40E88B07-L000072](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L72) | 72 | `"- انتهاء الجلسة مفروض على الخادم، وليس اعتمادًا على Max-Age في المتصفح فقط."` | — |
| [SRC-BA40E88B07-L000073](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L73) | 73 | `"- الجلسة مرتبطة ببصمة API token؛ الإبطال/الانتهاء/تغيير shared token يبطل الجلسة."` | — |
| [SRC-BA40E88B07-L000074](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L74) | 74 | `"- logout يبطل سجل الجلسة."` | — |
| [SRC-BA40E88B07-L000075](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L75) | 75 | `"- POST المعتمد على cookie يتطلب Origin موثوقًا."` | — |
| [SRC-BA40E88B07-L000076](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L76) | 76 | `"- لا يُقبل tenant_id من جسم الطلب كمرجع صلاحية؛ الهوية والـtenant يأتيان من principal موثوق."` | — |
| [SRC-BA40E88B07-L000077](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L77) | 77 | `""` | — |
| [SRC-BA40E88B07-L000078](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L78) | 78 | `"**حدود باقية:**"` | — |
| [SRC-BA40E88B07-L000079](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L79) | 79 | `"- واجهة إنشاء tenants/users/memberships/tokens وإدارة الأدوار الذاتية غير مكتملة؛ provisioning برمجي."` | — |
| [SRC-BA40E88B07-L000080](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L80) | 80 | `"- viewer للقراءة فقط، وowner مطلوب لتشخيصات المزودين؛ يجب اعتماد مصفوفة أدق لأدوار admin/manager/sales_agent قبل فتح إدارة الفرق."` | — |
| [SRC-BA40E88B07-L000081](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L81) | 81 | `"- HttpOnly يمنع JavaScript من قراءة session ID، لكنه لا يمنع XSS من تنفيذ طلبات باسم المستخدم؛ تبقى CSP ومخرجات DOM الآمنة ومراجعة XSS مطلوبة."` | — |
| [SRC-BA40E88B07-L000082](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L82) | 82 | `"- لا يوجد بعد تنظيف دوري لسجلات الجلسات المنتهية؛ لا يؤثر ذلك في التحقق، لكنه دين صيانة."` | — |
| [SRC-BA40E88B07-L000083](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L83) | 83 | `""` | — |
| [SRC-BA40E88B07-L000084](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L84) | 84 | `"### 3.5 موفرو النماذج وFailover"` | — |
| [SRC-BA40E88B07-L000085](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L85) | 85 | `""` | — |
| [SRC-BA40E88B07-L000086](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L86) | 86 | `"**VERIFIED في الكود/الاختبارات:**"` | — |
| [SRC-BA40E88B07-L000087](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L87) | 87 | `"- موفر OpenAI-compatible أساسي (OpenRouter أو base URL مخصص)."` | — |
| [SRC-BA40E88B07-L000088](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L88) | 88 | `"- Gemini وMistral موفران اختياريان احتياطيان عند توافر مفاتيحهما."` | — |
| [SRC-BA40E88B07-L000089](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L89) | 89 | `"- التسلسل: النموذج المطلوب في المزود الأساسي، ثم fallback الخاص به إن ضُبط، ثم النموذج الافتراضي للمزود التالي."` | — |
| [SRC-BA40E88B07-L000090](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L90) | 90 | ``"- فشل 429 يصنف `rate_limited`، و401/403 يصنف `unauthorized`؛ لا يُسجل جسم رد المزود."`` | — |
| [SRC-BA40E88B07-L000091](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L91) | 91 | ``"- طلب semantic verifier يستخدم `allow_fallback=False` لمنع إرسال مطالبة التحقق إلى مزود آخر بصمت."`` | — |
| [SRC-BA40E88B07-L000092](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L92) | 92 | `"- OpenRouter web search لا يرسل إلى Gemini/Mistral، ويظل opt-in."` | — |
| [SRC-BA40E88B07-L000093](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L93) | 93 | `""` | — |
| [SRC-BA40E88B07-L000094](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L94) | 94 | `"**VERIFIED من وثائق الموردين:**"` | — |
| [SRC-BA40E88B07-L000095](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L95) | 95 | ``"- Google Gemini يوفر OpenAI-compatible endpoint؛ النموذج الافتراضي في الفرع `gemini-3.1-flash-lite`."`` | — |
| [SRC-BA40E88B07-L000096](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L96) | 96 | ``"- Mistral Small 4 يعلن API names `mistral-small-2603` و`mistral-small-latest`؛ الافتراضي `mistral-small-latest`."`` | — |
| [SRC-BA40E88B07-L000097](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L97) | 97 | `""` | — |
| [SRC-BA40E88B07-L000098](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L98) | 98 | `"**UNKNOWN:** صلاحية مفاتيح المستخدم الفعلية، quota، latency، أسعار الحساب، والاتصال الحي. لم تُنفذ أي مكالمة مزود حية أو مدفوعة. قد تنتقل المطالبات والمقتطفات إلى مزود احتياطي عند فشل الأساسي؛ يجب إبلاغ المستخدم بذلك وعدم إرسال أسرار أو بيانات عملاء سرية."` | — |
| [SRC-BA40E88B07-L000099](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L99) | 99 | `""` | — |
| [SRC-BA40E88B07-L000100](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L100) | 100 | `"**حد الاستقلال:** عند استخدام Gemini أو Mistral فقط، النموذج الافتراضي لمراجع الادعاءات يساوي نموذج الإجابة؛ لذلك لا توجد مراجعة مستقلة بنموذج مختلف ما لم يضبط المستخدم نموذجًا صالحًا لذلك المزود. وحتى عند اختلاف model ID، يبقى ذلك تقييم دعم من نموذج وليس إثبات حقيقة خارجية."` | — |
| [SRC-BA40E88B07-L000101](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L101) | 101 | `""` | — |
| [SRC-BA40E88B07-L000102](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L102) | 102 | `"### 3.6 البحث وSSRF وPrompt Injection"` | — |
| [SRC-BA40E88B07-L000103](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L103) | 103 | `""` | — |
| [SRC-BA40E88B07-L000104](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L104) | 104 | `"**VERIFIED في الكود:**"` | — |
| [SRC-BA40E88B07-L000105](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L105) | 105 | `"- قبول HTTP(S) فقط، رفض userinfo والمنافذ غير المعتمدة وعناوين localhost/private."` | — |
| [SRC-BA40E88B07-L000106](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L106) | 106 | `"- حل DNS والتحقق من كل العناوين العامة، ثم الاتصال بـIP مثبت مع Host/SNI الأصليين لتقليل DNS rebinding/TOCTOU."` | — |
| [SRC-BA40E88B07-L000107](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L107) | 107 | ``"- `trust_env=False` يمنع proxy غير مقصود من البيئة، و`follow_redirects=False` يمنع اتباع redirect تلقائيًا؛ كل redirect يدوي يعاد فحص وجهته."`` | — |
| [SRC-BA40E88B07-L000108](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L108) | 108 | `"- طلبات مزودي النماذج لا تتبع redirects حتى لا تنتقل Authorization إلى origin آخر."` | — |
| [SRC-BA40E88B07-L000109](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L109) | 109 | `"- محتوى الصفحات والنتائج الخارجية بيانات غير موثوقة، ولا ينبغي أن يغير تعليمات النظام أو صلاحيات الأدوات."` | — |
| [SRC-BA40E88B07-L000110](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L110) | 110 | `""` | — |
| [SRC-BA40E88B07-L000111](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L111) | 111 | `"**المتبقي:** اختبارات SSRF لا تغطي كل بيئة DNS/IPv6/proxy فعلية؛ يلزم red-team واختبار hosted network policy."` | — |
| [SRC-BA40E88B07-L000112](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L112) | 112 | `""` | — |
| [SRC-BA40E88B07-L000113](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L113) | 113 | `"### 3.7 GitHub Actions وسلسلة التوريد"` | — |
| [SRC-BA40E88B07-L000114](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L114) | 114 | `""` | — |
| [SRC-BA40E88B07-L000115](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L115) | 115 | `"**VERIFIED:** Workflow الأساسي يستخدم Python 3.11 و3.12، lint، الاختبارات، Docker build، وprotected API smoke. Actions المستخدمة في المسارات التي فُحصت مثبتة على commit SHAs، وصلاحيات الاختبار محدودة إلى القراءة حيث لا يلزم الكتابة."` | — |
| [SRC-BA40E88B07-L000116](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L116) | 116 | `""` | — |
| [SRC-BA40E88B07-L000117](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L117) | 117 | ``"**PROPOSED:** استمرار مراجعة كل workflow جديد بحثًا عن `pull_request_target`، أو أسرار في PR من fork، أو صلاحيات `contents: write` غير ضرورية. لا تستخدم secrets في اختبار pull request غير موثوق."`` | — |
| [SRC-BA40E88B07-L000118](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L118) | 118 | `""` | — |
| [SRC-BA40E88B07-L000119](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L119) | 119 | `"## 4. الإصلاحات التي نُقلت إلى حزمة #145"` | — |
| [SRC-BA40E88B07-L000120](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L120) | 120 | `""` | — |
| [SRC-BA40E88B07-L000121](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L121) | 121 | `"\| المجال \| الإصلاح \| الاختبار المضاف \|"` | — |
| [SRC-BA40E88B07-L000122](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L122) | 122 | `"\|---\|---\|---\|"` | — |
| [SRC-BA40E88B07-L000123](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L123) | 123 | `"\| SQLite \| إغلاق كل اتصال بعد transaction \| اتصال مغلق بعد النجاح والفشل + rollback \|"` | — |
| [SRC-BA40E88B07-L000124](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L124) | 124 | `"\| Browser auth \| opaque server-side sessions \| expiry، revoke، rotation، logout، cookie flags، CSRF Origin \|"` | — |
| [SRC-BA40E88B07-L000125](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L125) | 125 | `"\| Dashboard \| قبول معرف lead من 24 hex \| Regression لاختبار handler \|"` | — |
| [SRC-BA40E88B07-L000126](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L126) | 126 | `"\| Intent \| إزالة تعريفات المتابعة المكررة \| اختبار عدد التعريفات \|"` | — |
| [SRC-BA40E88B07-L000127](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L127) | 127 | `"\| Search relevance \| حد مفهومين لاستعلام من 3 مفاهيم وإزالة كلمات التنقل من topic score \| mixed official/unrelated results \|"` | — |
| [SRC-BA40E88B07-L000128](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L128) | 128 | `"\| Provider errors \| تصنيف 429 و401/403 وإخفاء body \| fallback bounded/redacted \|"` | — |
| [SRC-BA40E88B07-L000129](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L129) | 129 | `"\| Provider failover \| Gemini/Mistral defaults وfailover \| mock provider selection, failover, verifier isolation \|"` | — |
| [SRC-BA40E88B07-L000130](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L130) | 130 | `"\| Diagnostics \| إبقاء الموافقة الصريحة والـowner gate \| اختبارات HTTP موجودة \|"` | — |
| [SRC-BA40E88B07-L000131](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L131) | 131 | `"\| Tenant isolation \| tenant scope وroles وtoken revocation \| اختبارات multi-tenant الحالية \|"` | — |
| [SRC-BA40E88B07-L000132](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L132) | 132 | `""` | — |
| [SRC-BA40E88B07-L000133](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L133) | 133 | `"## 5. أولويات ما بعد هذه الحزمة"` | — |
| [SRC-BA40E88B07-L000134](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L134) | 134 | `""` | — |
| [SRC-BA40E88B07-L000135](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L135) | 135 | `"1. **P1 — HTTP runtime:** اختبار انتقال إلى WSGI/ASGI دون تغيير API."` | — |
| [SRC-BA40E88B07-L000136](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L136) | 136 | `"2. **P1 — Role matrix:** تعريف صلاحيات admin/manager/sales_agent على العمليات والموارد."` | — |
| [SRC-BA40E88B07-L000137](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L137) | 137 | `"3. **P1 — Provisioning:** أداة إدارية آمنة لإنشاء المستخدمين والعضويات والرموز، دون إظهار الأسرار في السجلات."` | — |
| [SRC-BA40E88B07-L000138](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L138) | 138 | `"4. **P1 — Hosted acceptance:** اختبار هوية البناء، volume، session cookie عبر HTTPS reverse proxy، وlogout/token revocation."` | — |
| [SRC-BA40E88B07-L000139](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L139) | 139 | `"5. **P2 — Data store:** backup/restore مجرب، ثم قرار PostgreSQL عند ظهور متطلبات multi-instance."` | — |
| [SRC-BA40E88B07-L000140](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L140) | 140 | `"6. **P2 — Model evaluation:** corpus عربي/إنجليزي موسوم بشريًا، مقارنة موفري النماذج، وقياس false positives/abstention/latency/cost."` | — |
| [SRC-BA40E88B07-L000141](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L141) | 141 | `"7. **P3 — Operations:** load/concurrency/failure tests، distributed rate limits عند تعدد النسخ، ومراقبة منزوعة الأسرار."` | — |
| [SRC-BA40E88B07-L000142](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L142) | 142 | `""` | — |
| [SRC-BA40E88B07-L000143](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L143) | 143 | `"## 6. حالة التنفيذ"` | — |
| [SRC-BA40E88B07-L000144](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L144) | 144 | `""` | — |
| [SRC-BA40E88B07-L000145](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L145) | 145 | `"- **VERIFIED:** الملفات والتغييرات موجودة في فرع الإصلاح، ولا توجد تعديلات على main."` | — |
| [SRC-BA40E88B07-L000146](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L146) | 146 | `"- **FIXED_AND_TESTED:** لا يُثبت إلا بعد نجاح CI النهائي على رأس الفرع بعد آخر تعديل."` | — |
| [SRC-BA40E88B07-L000147](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L147) | 147 | `"- **NOT_RUN:** hosted acceptance، live provider calls، paid quota checks، load test، backup/restore، independent red-team."` | — |
| [SRC-BA40E88B07-L000148](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L148) | 148 | `"- **UNKNOWN:** سلوك الاستضافة الحالي ومفاتيح الموردين الفعلية."` | — |
| [SRC-BA40E88B07-L000149](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L149) | 149 | `""` | — |
| [SRC-BA40E88B07-L000150](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L150) | 150 | `"## 7. المراجع الرسمية"` | — |
| [SRC-BA40E88B07-L000151](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L151) | 151 | `""` | — |
| [SRC-BA40E88B07-L000152](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L152) | 152 | `"- [Python 3.12 — http.server security warning](https://docs.python.org/3.12/library/http.server.html)"` | — |
| [SRC-BA40E88B07-L000153](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L153) | 153 | `"- [Python 3.12 — sqlite3 connection context manager](https://docs.python.org/3.12/library/sqlite3.html#how-to-use-the-connection-context-manager)"` | — |
| [SRC-BA40E88B07-L000154](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L154) | 154 | `"- [SQLite — foreign_keys pragma](https://www.sqlite.org/pragma.html#pragma_foreign_keys)"` | — |
| [SRC-BA40E88B07-L000155](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L155) | 155 | `"- [SQLite — busy_timeout pragma](https://www.sqlite.org/pragma.html#pragma_busy_timeout)"` | — |
| [SRC-BA40E88B07-L000156](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L156) | 156 | `"- [OWASP — Multi-Tenant Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Multi_Tenant_Security_Cheat_Sheet.html)"` | — |
| [SRC-BA40E88B07-L000157](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L157) | 157 | `"- [OWASP — Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)"` | — |
| [SRC-BA40E88B07-L000158](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L158) | 158 | `"- [OWASP — Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)"` | — |
| [SRC-BA40E88B07-L000159](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L159) | 159 | `"- [OWASP — SSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html)"` | — |
| [SRC-BA40E88B07-L000160](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L160) | 160 | `"- [GitHub — Security hardening for GitHub Actions](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions)"` | — |
| [SRC-BA40E88B07-L000161](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L161) | 161 | `"- [Google — Gemini OpenAI compatibility](https://ai.google.dev/gemini-api/docs/openai)"` | — |
| [SRC-BA40E88B07-L000162](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L162) | 162 | `"- [Google — Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite)"` | — |
| [SRC-BA40E88B07-L000163](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L163) | 163 | `"- [Mistral — Mistral Small 4 model card](https://docs.mistral.ai/models/mistral-small-4-0-26-03)"` | — |
## وثائق وفهرسة

### FILE-21D5D044E2 — [docs/OMARAI_EXCEPTIONS_REGISTER_AR.md](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-21D5D044E2-L000001](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L1) | 1 | `"# Omarai — سجل الاستثناءات والقرارات المؤجلة"` | — |
| [SRC-21D5D044E2-L000002](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L2) | 2 | `""` | — |
| [SRC-21D5D044E2-L000003](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L3) | 3 | `"**المعرف:** OMARAI-EXCEPTIONS-REGISTER-001  "` | — |
| [SRC-21D5D044E2-L000004](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L4) | 4 | `"**التاريخ:** 2026-10-19  "` | — |
| [SRC-21D5D044E2-L000005](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L5) | 5 | `"**الحالة:** مقترح للمراجعة — لم يُعتمد أي استثناء بموجب هذا الملف.  "` | — |
| [SRC-21D5D044E2-L000006](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L6) | 6 | `"**المسؤول عن القرار:** مدير المشروع البشري  "` | — |
| [SRC-21D5D044E2-L000007](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L7) | 7 | ``"**مرجع الحوكمة:** `GOV-003` و`GOV-004` و`GOV-005`"`` | — |
| [SRC-21D5D044E2-L000008](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L8) | 8 | `""` | — |
| [SRC-21D5D044E2-L000009](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L9) | 9 | `"## 1. الغرض وقواعد الاستخدام"` | — |
| [SRC-21D5D044E2-L000010](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L10) | 10 | `""` | — |
| [SRC-21D5D044E2-L000011](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L11) | 11 | ``"يوثق هذا السجل أي استثناء مطلوب من متطلب إلزامي `MUST` أو قرار بتحديد نطاق الإصدار. إعداد هذا السجل أو دمجه لا يعني قبول المخاطر المدرجة."`` | — |
| [SRC-21D5D044E2-L000012](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L12) | 12 | `""` | — |
| [SRC-21D5D044E2-L000013](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L13) | 13 | `"يجب أن يحتوي كل استثناء معتمد على: معرف المتطلب، السبب، النطاق، المخاطر والبيانات/القدرات المتأثرة، البديل التعويضي، صاحب صلاحية الموافقة، تاريخ أو شرط الانتهاء، ودليل إعادة النظر والإغلاق."` | — |
| [SRC-21D5D044E2-L000014](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L14) | 14 | `""` | — |
| [SRC-21D5D044E2-L000015](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L15) | 15 | ``"- `PROPOSED`: مقترح ينتظر قرارًا بشريًا صريحًا."`` | — |
| [SRC-21D5D044E2-L000016](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L16) | 16 | ``"- `WAIVED`: استثناء وافق عليه صاحب الصلاحية، بنطاق وحدود وموعد/شرط انتهاء."`` | — |
| [SRC-21D5D044E2-L000017](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L17) | 17 | ``"- `NOT APPLICABLE`: المتطلب لا ينطبق على نطاق محدد حاليًا مع السبب وشرط إعادة النظر."`` | — |
| [SRC-21D5D044E2-L000018](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L18) | 18 | ``"- `UNKNOWN`: الأدلة لا تكفي للحكم؛ لا يجوز استخدام استثناء لتغطية هذه الحالة."`` | — |
| [SRC-21D5D044E2-L000019](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L19) | 19 | ``"- `NOT RUN`: اختبار مطلوب لم يُنفذ."`` | — |
| [SRC-21D5D044E2-L000020](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L20) | 20 | `""` | — |
| [SRC-21D5D044E2-L000021](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L21) | 21 | `"لا توجد في هذا السجل موافقات بشرية مختلقة أو استثناءات مفتوحة إلى أجل غير محدد. **لا يُسجل أي عنصر كـWAIVED إلا بعد توثيق موافقتك الصريحة.**"` | — |
| [SRC-21D5D044E2-L000022](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L22) | 22 | `""` | — |
| [SRC-21D5D044E2-L000023](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L23) | 23 | `"## 2. سجل الاستثناءات المعتمدة"` | — |
| [SRC-21D5D044E2-L000024](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L24) | 24 | `""` | — |
| [SRC-21D5D044E2-L000025](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L25) | 25 | `"\| معرف الاستثناء \| المتطلب \| النطاق \| الموافِق \| الحالة \| الانتهاء/إعادة النظر \| دليل القرار \|"` | — |
| [SRC-21D5D044E2-L000026](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L26) | 26 | `"\|---\|---\|---\|---\|---\|---\|---\|"` | — |
| [SRC-21D5D044E2-L000027](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L27) | 27 | `"\| — \| — \| لا يوجد استثناء معتمد مسجل في هذا الملف حتى تاريخ اللقطة. \| — \| لا توجد موافقات مسجلة هنا \| — \| لا يثبت ذلك غياب قرار أو موافقة خارج المستودع. \|"` | — |
| [SRC-21D5D044E2-L000028](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L28) | 28 | `""` | — |
| [SRC-21D5D044E2-L000029](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L29) | 29 | `"## 3. مقترحات للمراجعة — ليست استثناءات معتمدة"` | — |
| [SRC-21D5D044E2-L000030](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L30) | 30 | `""` | — |
| [SRC-21D5D044E2-L000031](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L31) | 31 | `"### EX-PROP-001 — حصر النسخة على مشغّل واحد"` | — |
| [SRC-21D5D044E2-L000032](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L32) | 32 | `""` | — |
| [SRC-21D5D044E2-L000033](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L33) | 33 | ``"- **المتطلبات:** `IDN-001` و`IDN-003` ومتطلبات تعدد المستأجرين المشروطة."`` | — |
| [SRC-21D5D044E2-L000034](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L34) | 34 | `"- **المقترح:** تحديد نطاق النسخة التجريبية على أنها خدمة خاصة بمشغّل واحد بدل تقديمها كمنصة متعددة المستخدمين."` | — |
| [SRC-21D5D044E2-L000035](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L35) | 35 | `"- **السبب:** التنفيذ الحالي يستخدم رمز Bearer مشتركًا ومخزن leads مشتركًا؛ لا تظهر هوية فردية أو عزل كامل لبيانات كل مستخدم."` | — |
| [SRC-21D5D044E2-L000036](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L36) | 36 | `"- **المخاطر:** من يحصل على الرمز يحصل على الصلاحيات الممنوحة له؛ قد تختلط بيانات عدة مستخدمين إذا استُخدم النظام على نحو غير مقصود."` | — |
| [SRC-21D5D044E2-L000037](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L37) | 37 | `"- **التعويضات المطلوبة إذا وافق المدير:** إبقاء الخدمة خاصة، استخدام رمز قوي وسري، عدم مشاركة الرمز كأنه حساب مستقل، وعدم إدخال بيانات عملاء مستقلين أو بيانات حساسة."` | — |
| [SRC-21D5D044E2-L000038](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L38) | 38 | `"- **صاحب القرار:** مدير المشروع البشري."` | — |
