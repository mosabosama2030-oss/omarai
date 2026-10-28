# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **020**
- سجلات الأسطر: **800**
- النطاق: SRC-E599346ABE-L001804 إلى SRC-E73001D9AC-L000304
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## وثائق وفهرسة

### FILE-E599346ABE — [docs/generate_index.py](../generate_index.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
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
| [SRC-C8EA754D73-L000003](../IMPLEMENTATION_SCOPE.md#L3) | 3 | ``"**الرأس المرجعي لـ `main` الذي تحققنا منه:** `00a3ede039922c0c24097e89f653e6d3c984435d`؛ commit فهرسة مولد بعد دمج PR #81 في `9f6674abf8679a0630d95b269b54a7ef8629c3bf`.  "`` | — |
| [SRC-C8EA754D73-L000004](../IMPLEMENTATION_SCOPE.md#L4) | 4 | `"**حالة PR #81:** مدمج. غيّر إعدادات اختبارات CI وثلاث وثائق؛ لم يغيّر منطق البحث أو موصلاته.  "` | — |
| [SRC-C8EA754D73-L000005](../IMPLEMENTATION_SCOPE.md#L5) | 5 | ``"**حدّ التحقق:** تشغيل CI على رأس PR قبل الدمج [#39955767221](https://github.com/mosabosama2030-oss/omarai/actions/runs/39955767221) نجح؛ لم أتمكن من إثبات تشغيل push مستقل على رأس `main` الحالي من بيانات التشغيل التي يعيدها موصل GitHub المتاح. هذا `NOT_CONFIRMED` وليس دليل فشل.  "`` | — |
| [SRC-C8EA754D73-L000006](../IMPLEMENTATION_SCOPE.md#L6) | 6 | `"**حدود الوثيقة:** تصف الشفرة الحالية وما تثبته الأدلة؛ ليست شهادة امتثال أو تأكيدًا على وجود خدمة مستضافة."` | — |
| [SRC-C8EA754D73-L000007](../IMPLEMENTATION_SCOPE.md#L7) | 7 | `""` | — |
| [SRC-C8EA754D73-L000008](../IMPLEMENTATION_SCOPE.md#L8) | 8 | `"## الحالة التنفيذية الحالية"` | — |
| [SRC-C8EA754D73-L000009](../IMPLEMENTATION_SCOPE.md#L9) | 9 | `""` | — |
| [SRC-C8EA754D73-L000010](../IMPLEMENTATION_SCOPE.md#L10) | 10 | `"- **التوجيه والمتابعة — VERIFIED ضمن الاختبارات الآلية:** كشف الأسئلة المرجعية الغامضة وتوحيد حل المتابعة وحدود السياق."` | — |
| [SRC-C8EA754D73-L000011](../IMPLEMENTATION_SCOPE.md#L11) | 11 | ``"- **عرض الأدلة وعمق البحث — VERIFIED ضمن الاختبارات الآلية:** لا تُعرض تغطية الأدلة على أنها احتمال صحة؛ واختيار العمق يقارن قيمة `deep` صراحةً."`` | — |
| [SRC-C8EA754D73-L000012](../IMPLEMENTATION_SCOPE.md#L12) | 12 | `"- **سلامة البحث وجلب الصفحات — VERIFIED ضمن الاختبارات المحددة:** حالات جلب مهيكلة، وتشخيصات موصلات، وحدود واضحة لفشل الجلب، ومنع التحويل التلقائي في الموصلات المغطاة بالاختبارات."` | — |
| [SRC-C8EA754D73-L000013](../IMPLEMENTATION_SCOPE.md#L13) | 13 | `"- **حماية API والمتصفح — VERIFIED ضمن الاختبارات المحددة:** رؤوس حماية وسياسة CSP واختبارات انحدار؛ هذا لا يغني عن تدقيق أمني شامل أو red-team مستقل."` | — |
| [SRC-C8EA754D73-L000014](../IMPLEMENTATION_SCOPE.md#L14) | 14 | ``"- **هوية البناء — CODE PATH TESTED:** صورة Docker تتيح SHA للبناء ويعرضه `/api/health`، ويقارن Hosted smoke SHA المتوقع بالمعلن. الاختبار الحي ضد خدمة مستضافة **NOT_RUN**."`` | — |
| [SRC-C8EA754D73-L000015](../IMPLEMENTATION_SCOPE.md#L15) | 15 | ``"- **الفهرسة والبحث المحلي — VERIFIED ضمن اختبارات المولد والبحث:** `docs/generate_index.py` يبني جرد الملفات والرموز وصفحات الأسطر؛ `docs/search_code.py` يتيح البحث محليًا دون API."`` | — |
| [SRC-C8EA754D73-L000016](../IMPLEMENTATION_SCOPE.md#L16) | 16 | ``"- **مسار SQLite — VERIFIED في الكود والاختبارات المحلية:** `OMARAI_DB_PATH` يحدد المسار؛ لا ينشئ Volume ولا يثبت استمرار البيانات لدى مزود استضافة."`` | — |
| [SRC-C8EA754D73-L000017](../IMPLEMENTATION_SCOPE.md#L17) | 17 | `""` | — |
| [SRC-C8EA754D73-L000018](../IMPLEMENTATION_SCOPE.md#L18) | 18 | `"## أدلة الاختبار وحدودها"` | — |
| [SRC-C8EA754D73-L000019](../IMPLEMENTATION_SCOPE.md#L19) | 19 | `""` | — |
| [SRC-C8EA754D73-L000020](../IMPLEMENTATION_SCOPE.md#L20) | 20 | `"- **CI على رأس PR #81 قبل الدمج:** [run #39955767221](https://github.com/mosabosama2030-oss/omarai/actions/runs/39955767221) نجح بالكامل: 384 اختبارًا على Python 3.11 و384 على Python 3.12، وRuff، وتصنيف مسارات الفهرسة، وتوليد الفهرس والتحقق منه، وبناء الحاوية واختبار API المحمي."` | — |
| [SRC-C8EA754D73-L000021](../IMPLEMENTATION_SCOPE.md#L21) | 21 | ``"- **دمج PR #81:** الالتزام `9f6674abf8679a0630d95b269b54a7ef8629c3bf`. رأس `main` الذي تحققنا من مطابقته هو `00a3ede039922c0c24097e89f653e6d3c984435d`؛ المقارنة بين `main` وهذا الالتزام أعادت `identical`."`` | — |
| [SRC-C8EA754D73-L000022](../IMPLEMENTATION_SCOPE.md#L22) | 22 | `"- **الإصلاح:** سباق الفهرس عولج في [PR #81](https://github.com/mosabosama2030-oss/omarai/pull/81): يختبر CI تصنيف المسارات، ويعيد توليد الفهرس في مساحة اختبار معزولة للتغييرات المختلطة، مع الإبقاء على الفحص الصارم عند تغييرات الفهرسة وحدها."` | — |
| [SRC-C8EA754D73-L000023](../IMPLEMENTATION_SCOPE.md#L23) | 23 | ``"- **CI على رأس main النهائي:** `NOT_CONFIRMED` في هذه المراجعة؛ نتيجة #39955767221 تخص رأس PR قبل الدمج، وواجهة التشغيل المتاحة هنا لا تكشف تشغيلات push على نحو يسمح بتأكيد تشغيل مستقل على `00a3ede...`. هذا ليس دليل فشل؛ يلزم فحص GitHub Actions مباشرة."`` | — |
| [SRC-C8EA754D73-L000024](../IMPLEMENTATION_SCOPE.md#L24) | 24 | ``"- اختبارات الاستضافة والموصلات الحية وجودة الإجابات الدلالية والنسخ/الاستعادة والحمل تبقى `NOT_RUN/UNKNOWN` حتى وجود أدلة مباشرة."`` | — |
| [SRC-C8EA754D73-L000025](../IMPLEMENTATION_SCOPE.md#L25) | 25 | `""` | — |
| [SRC-C8EA754D73-L000026](../IMPLEMENTATION_SCOPE.md#L26) | 26 | `"## غير مثبت أو خارج النطاق الحالي"` | — |
| [SRC-C8EA754D73-L000027](../IMPLEMENTATION_SCOPE.md#L27) | 27 | `""` | — |
| [SRC-C8EA754D73-L000028](../IMPLEMENTATION_SCOPE.md#L28) | 28 | ``"- **المزودون الأحياء والاستضافة:** `UNKNOWN / NOT_RUN` حتى اختبار كل موفر وخدمة مستهدفة فعليًا."`` | — |
| [SRC-C8EA754D73-L000029](../IMPLEMENTATION_SCOPE.md#L29) | 29 | `"- **جودة الإجابات الدلالية:** لا يثبت وجود استشهاد أو تشابه ألفاظ أن المصدر يستلزم الادعاء؛ التحقق الدلالي المستقل الشامل غير مثبت."` | — |
| [SRC-C8EA754D73-L000030](../IMPLEMENTATION_SCOPE.md#L30) | 30 | ``"- **SQLite والنسخ والاستعادة على المضيف:** `NOT_RUN` حتى يثبت بقاء البيانات بعد إعادة التشغيل/النشر ثم نجاح استعادة نسخة احتياطية."`` | — |
| [SRC-C8EA754D73-L000031](../IMPLEMENTATION_SCOPE.md#L31) | 31 | ``"- **الحمل والسعة:** `NOT_RUN`; semaphore ومحدد معدل العملية لا يثبتان throughput إنتاجيًا ولا تنسيقًا موزعًا."`` | — |
| [SRC-C8EA754D73-L000032](../IMPLEMENTATION_SCOPE.md#L32) | 32 | `"- **تعدد المستأجرين:** غير مدعوم بالنطاق الحالي؛ الرمز مشترك ومساحة البيانات لا تثبت عزلًا لكل عميل. لا يُستخدم كخدمة متعددة العملاء قبل الهوية والتفويض والعزل واختباراتها."` | — |
| [SRC-C8EA754D73-L000033](../IMPLEMENTATION_SCOPE.md#L33) | 33 | `"- **Android/RTL:** القبول اليدوي لا يُغلق بنتائج Pytest فقط."` | — |
| [SRC-C8EA754D73-L000034](../IMPLEMENTATION_SCOPE.md#L34) | 34 | `"- **المراجعة الأمنية المستقلة:** لا تعتبر مكتملة دون تقرير فعلي مرتبط بـSHA وأدلة قابلة للمراجعة."` | — |
| [SRC-C8EA754D73-L000035](../IMPLEMENTATION_SCOPE.md#L35) | 35 | `""` | — |
| [SRC-C8EA754D73-L000036](../IMPLEMENTATION_SCOPE.md#L36) | 36 | `"## مصادر الحقيقة حسب الغرض"` | — |
| [SRC-C8EA754D73-L000037](../IMPLEMENTATION_SCOPE.md#L37) | 37 | `""` | — |
| [SRC-C8EA754D73-L000038](../IMPLEMENTATION_SCOPE.md#L38) | 38 | `"- تفاصيل العيوب والمعرّفات ومعايير الإغلاق: [سجل المعالجة المركزي](OMARAI_REMEDIATION_REGISTER_AR.md)."` | — |
| [SRC-C8EA754D73-L000039](../IMPLEMENTATION_SCOPE.md#L39) | 39 | `"- نتيجة ما بعد الدمج وحدود الأدلة: [تقرير التحقق بعد الدمج](OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md)."` | — |
| [SRC-C8EA754D73-L000040](../IMPLEMENTATION_SCOPE.md#L40) | 40 | `"- أنواع الاختبار والنتائج التاريخية وحدودها: [مصفوفة أدلة الاختبار](OMARAI_TEST_EVIDENCE_MATRIX_AR.md)."` | — |
| [SRC-C8EA754D73-L000041](../IMPLEMENTATION_SCOPE.md#L41) | 41 | `"- قواعد المساهمة وتنظيم المستودع: [AGENTS.md](../AGENTS.md) و[دليل الوثائق](README.md)."` | — |
| [SRC-C8EA754D73-L000042](../IMPLEMENTATION_SCOPE.md#L42) | 42 | `""` | — |
| [SRC-C8EA754D73-L000043](../IMPLEMENTATION_SCOPE.md#L43) | 43 | ``"لا تُرقَّ حالة إلى `VERIFIED` دون اختبار محدد على SHA/بيئة واضحة. لا تُحوَّل `NOT_RUN` أو `UNKNOWN` إلى نجاح لمجرد وجود كود أو إعداد أو ملف توثيق."`` | — |
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
| [SRC-21D5D044E2-L000039](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L39) | 39 | `"- **الانتهاء/إعادة النظر:** قبل أي عرض عام لعدة مستخدمين، أو تخزين بيانات مستقلة لجهات مختلفة."` | — |
| [SRC-21D5D044E2-L000040](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L40) | 40 | ``"- **الحالة:** `PROPOSED — تنتظر الموافقة`."`` | — |
| [SRC-21D5D044E2-L000041](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L41) | 41 | `""` | — |
| [SRC-21D5D044E2-L000042](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L42) | 42 | `"### EX-PROP-002 — استمرارية البيانات في بيئة تجريبية قابلة للفقد"` | — |
| [SRC-21D5D044E2-L000043](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L43) | 43 | `""` | — |
| [SRC-21D5D044E2-L000044](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L44) | 44 | ``"- **المتطلبات:** `REL-005` و`EXT-002` و`DAT-002` بحسب انطباقها على البيانات المخزنة."`` | — |
| [SRC-21D5D044E2-L000045](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L45) | 45 | `"- **المقترح:** السماح بتجربة لا تعتمد على حفظ بيانات مهمة فقط إذا كانت كل بياناتها اصطناعية أو قابلة لإعادة الإنشاء، مع إبقاء النسخ والاستعادة الدائمة خارج نطاق هذه التجربة."` | — |
| [SRC-21D5D044E2-L000046](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L46) | 46 | `"- **السبب:** النسخ الاحتياطي والاستعادة ودوام تخزين SQLite على مضيف محدد لم تثبت هنا."` | — |
| [SRC-21D5D044E2-L000047](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L47) | 47 | `"- **المخاطر:** فقدان البيانات بعد إعادة إنشاء الحاوية أو تغيير المضيف أو تلف ملف قاعدة البيانات."` | — |
| [SRC-21D5D044E2-L000048](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L48) | 48 | `"- **التعويضات المطلوبة إذا وافق المدير:** عدم إدخال بيانات لا يمكن تعويضها، والتصريح بأن الاستمرارية غير مثبتة."` | — |
| [SRC-21D5D044E2-L000049](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L49) | 49 | `"- **صاحب القرار:** مدير المشروع البشري."` | — |
| [SRC-21D5D044E2-L000050](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L50) | 50 | `"- **الانتهاء/إعادة النظر:** قبل تخزين أي بيانات عمل حقيقية يُعتمد عليها."` | — |
| [SRC-21D5D044E2-L000051](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L51) | 51 | ``"- **الحالة:** `PROPOSED — تنتظر الموافقة`."`` | — |
| [SRC-21D5D044E2-L000052](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L52) | 52 | `""` | — |
| [SRC-21D5D044E2-L000053](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L53) | 53 | `"### EX-PROP-003 — عدم إعلان سعة/توافر غير مقاس"` | — |
| [SRC-21D5D044E2-L000054](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L54) | 54 | `""` | — |
| [SRC-21D5D044E2-L000055](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L55) | 55 | ``"- **المتطلبات:** `PER-004` و`REL-006`، وأي ادعاء أداء أو توافر في `PRD-001`."`` | — |
| [SRC-21D5D044E2-L000056](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L56) | 56 | `"- **المقترح:** عدم نشر أرقام عن throughput أو عدد مستخدمين مدعوم أو نسبة توافر، إلى أن تتوفر قياسات ممثلة."` | — |
| [SRC-21D5D044E2-L000057](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L57) | 57 | `"- **الطبيعة:** هذا في الأساس قيد على الادعاءات، وليس إذنًا بتجاهل ضوابط الأمان أو حدود الموارد."` | — |
| [SRC-21D5D044E2-L000058](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L58) | 58 | `"- **المخاطر:** توقعات غير واقعية من المستخدمين أو توقف الخدمة تحت ضغط لم يُختبر."` | — |
| [SRC-21D5D044E2-L000059](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L59) | 59 | `"- **التعويض:** الإفصاح أن السعة والتوافر غير معروفين، وعدم إعطاء وعود تشغيلية رقمية."` | — |
| [SRC-21D5D044E2-L000060](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L60) | 60 | `"- **صاحب القرار:** مدير المشروع البشري."` | — |
| [SRC-21D5D044E2-L000061](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L61) | 61 | `"- **الانتهاء/إعادة النظر:** عند إجراء اختبار حمل موثق أو تقديم التزام تشغيلي."` | — |
| [SRC-21D5D044E2-L000062](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L62) | 62 | ``"- **الحالة:** `PROPOSED — تنتظر الموافقة`."`` | — |
| [SRC-21D5D044E2-L000063](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L63) | 63 | `""` | — |
| [SRC-21D5D044E2-L000064](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L64) | 64 | `"### EX-PROP-004 — الموصلات الاختيارية غير المتحققة"` | — |
| [SRC-21D5D044E2-L000065](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L65) | 65 | `""` | — |
| [SRC-21D5D044E2-L000066](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L66) | 66 | ``"- **المتطلبات:** `SRH-001` و`TST-005` و`PRD-001`."`` | — |
| [SRC-21D5D044E2-L000067](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L67) | 67 | `"- **المقترح:** عدم إعلان موصل اختياري على أنه يعمل حيًا ما لم ينجح اختبار اتصال فعلي به في بيئة محددة. يكفي توثيقه كقدرة مشروطة بتهيئة صحيحة."` | — |
| [SRC-21D5D044E2-L000068](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L68) | 68 | `"- **الطبيعة:** هذا ليس إعفاء من ضرورة الصدق؛ بل قاعدة لتحديد الادعاء المسموح."` | — |
| [SRC-21D5D044E2-L000069](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L69) | 69 | ``"- **التعويض:** عرض الحالة `NOT_RUN` أو `UNKNOWN` إلى حين إجراء الاختبار."`` | — |
| [SRC-21D5D044E2-L000070](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L70) | 70 | `"- **صاحب القرار:** مدير المشروع البشري عند اعتماد نطاق المنتج."` | — |
| [SRC-21D5D044E2-L000071](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L71) | 71 | `"- **الانتهاء/إعادة النظر:** عند تفعيل الموصل أو الإعلان عنه كقدرة متحققة."` | — |
| [SRC-21D5D044E2-L000072](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L72) | 72 | ``"- **الحالة:** `PROPOSED — تنتظر المراجعة`."`` | — |
| [SRC-21D5D044E2-L000073](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L73) | 73 | `""` | — |
| [SRC-21D5D044E2-L000074](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L74) | 74 | `"## 4. متطلبات لا يجوز اعتبارها مستثناة بهذا السجل"` | — |
| [SRC-21D5D044E2-L000075](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L75) | 75 | `""` | — |
| [SRC-21D5D044E2-L000076](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L76) | 76 | `"لا يمثل أي مقترح أعلاه موافقة على تجاوز:"` | — |
| [SRC-21D5D044E2-L000077](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L77) | 77 | `"- حماية SSRF والحدود الشبكية."` | — |
| [SRC-21D5D044E2-L000078](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L78) | 78 | `"- حماية الطلبات والمهلات الأساسية في API المعرض للإنترنت."` | — |
| [SRC-21D5D044E2-L000079](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L79) | 79 | `"- منع حقن التعليمات من تجاوز سياسة التطبيق أو تسريب الأسرار."` | — |
| [SRC-21D5D044E2-L000080](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L80) | 80 | `"- التحقق من المصادقة والتفويض الملائمين لنطاق الاستخدام."` | — |
| [SRC-21D5D044E2-L000081](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L81) | 81 | `"- الصدق في الاستشهادات وبيان عدم اليقين."` | — |
| [SRC-21D5D044E2-L000082](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L82) | 82 | `"- فحص الأسرار وحماية إعدادات CI/CD."` | — |
| [SRC-21D5D044E2-L000083](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L83) | 83 | `"- اختبار النشر الفعلي قبل الإعلان عن تشغيله."` | — |
| [SRC-21D5D044E2-L000084](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L84) | 84 | `"- اختبار النسخ والاستعادة قبل الاعتماد على بيانات لا يمكن تعويضها."` | — |
| [SRC-21D5D044E2-L000085](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L85) | 85 | `""` | — |
| [SRC-21D5D044E2-L000086](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L86) | 86 | ``"لا يستخدم `NOT APPLICABLE` بدل `UNKNOWN`، ولا يجوز ترقية `PROPOSED` إلى `WAIVED` دون موافقة صريحة قابلة للمراجعة."`` | — |
| [SRC-21D5D044E2-L000087](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L87) | 87 | `""` | — |
| [SRC-21D5D044E2-L000088](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L88) | 88 | `"## 5. سجل قرارات المدير"` | — |
| [SRC-21D5D044E2-L000089](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L89) | 89 | `""` | — |
| [SRC-21D5D044E2-L000090](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L90) | 90 | `"لم تُسجل موافقات في هذا الملف حتى تاريخ الإنشاء. تُضاف الموافقة فقط بعد صدورها صراحة، ويجب أن تتضمن معرف الاستثناء الذي وافق المدير عليه ونطاقه وشروطه. لن يُستنتج القبول من الصمت أو من اعتماد مهام التطوير."` | — |
| [SRC-21D5D044E2-L000091](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L91) | 91 | `""` | — |
| [SRC-21D5D044E2-L000092](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L92) | 92 | `"## 6. مراجعة دورية وإغلاق"` | — |
| [SRC-21D5D044E2-L000093](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L93) | 93 | `""` | — |
| [SRC-21D5D044E2-L000094](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L94) | 94 | `"عند انتهاء كل استثناء أو تغير النطاق:"` | — |
| [SRC-21D5D044E2-L000095](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L95) | 95 | `"1. أعد تشغيل اختبار القبول المناسب."` | — |
| [SRC-21D5D044E2-L000096](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L96) | 96 | `"2. سجل الدليل الجديد وربطه بالـSHA والبيئة."` | — |
| [SRC-21D5D044E2-L000097](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L97) | 97 | `"3. حدّد هل أُغلق الاستثناء أم يحتاج تجديدًا بموافقة جديدة."` | — |
| [SRC-21D5D044E2-L000098](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L98) | 98 | `"4. لا تمدد الاستثناء تلقائيًا."` | — |
| [SRC-21D5D044E2-L000099](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L99) | 99 | `"5. احتفظ بسجل القرار السابق بدل محوه."` | — |
## وثائق وفهرسة

### FILE-E73001D9AC — [docs/OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-E73001D9AC-L000001](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L1) | 1 | `"# Omarai — الدستور التأسيسي للهندسة والموثوقية والأمان والذكاء"` | — |
| [SRC-E73001D9AC-L000002](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L2) | 2 | `""` | — |
| [SRC-E73001D9AC-L000003](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L3) | 3 | `"**معرّف الوثيقة:** OMARAI-FOUNDATION-CHARTER-001  "` | — |
| [SRC-E73001D9AC-L000004](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L4) | 4 | `"**الإصدار:** 1.2.0  "` | — |
| [SRC-E73001D9AC-L000005](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L5) | 5 | `"**الحالة:** متطلب تأسيسي مقترح للإقرار والمراجعة؛ بعد اعتماد المالك يصبح مرجعًا حاكمًا للتطوير  "` | — |
| [SRC-E73001D9AC-L000006](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L6) | 6 | `"**النطاق:** جميع مكونات Omarai البرمجية والتشغيلية، وواجهات API، والواجهة العربية، ومحركات البحث، والنماذج، والأدوات، والبيانات، والاستضافة، وسير التطوير والاختبار  "` | — |
| [SRC-E73001D9AC-L000007](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L7) | 7 | `"**الأولوية:** مرجع تصميم وحوكمة؛ لا يثبت بمفرده أن أي قدرة نُفّذت أو اختُبرت  "` | — |
| [SRC-E73001D9AC-L000008](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L8) | 8 | `"**اللغة:** العربية هي لغة الشرح الأساسية، مع استخدام أسماء المصطلحات التقنية الإنجليزية لتوحيد التنفيذ والمراجعة"` | — |
| [SRC-E73001D9AC-L000009](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L9) | 9 | `""` | — |
| [SRC-E73001D9AC-L000010](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L10) | 10 | `"> **القاعدة العليا:** Omarai لا يدّعي قدرة غير مثبتة. كل قدرة مهمة يجب أن تقابلها آلية تنفيذ محددة واختبار قابل لإعادة التشغيل ودليل ناتج عن بيئة معروفة. الاختبارات والقياسات الفعلية مقدّمة على الأوصاف والوعود."` | — |
| [SRC-E73001D9AC-L000011](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L11) | 11 | `""` | — |
| [SRC-E73001D9AC-L000012](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L12) | 12 | `"---"` | — |
| [SRC-E73001D9AC-L000013](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L13) | 13 | `""` | — |
| [SRC-E73001D9AC-L000014](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L14) | 14 | `"> **مراجع مكملة للمراجعات الواسعة:** تُقرأ هذه الوثيقة مع [خط الأساس الهندسي للمنصات العالمية واسعة النطاق](OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md)، ومع [سجل المتطلبات والتتبع والنضج وبوابات الاعتماد](OMARAI_REQUIREMENTS_TRACEABILITY_AND_MATURITY_MODEL_AR.md)، ومع [سجل المتطلبات الأساسية الأولي](OMARAI_REQUIREMENTS_REGISTER.md). وتُقرأ أيضًا مع [المعمارية الحاكمة للقدرات والمهارات وسير العمل والوكلاء](OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md)، التي تفصل مسار التوسع من النواة إلى المهارات وسير العمل والوكلاء. هذه الوثائق مكملة بعضها لبعض وليست بدائل متنافسة؛ لا تثبت أي وثيقة وحدها أن الضوابط نُفذت."` | — |
| [SRC-E73001D9AC-L000015](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L15) | 15 | `""` | — |
| [SRC-E73001D9AC-L000016](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L16) | 16 | `"## 0. كيف تُقرأ هذه الوثيقة؟"` | — |
| [SRC-E73001D9AC-L000017](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L17) | 17 | `""` | — |
| [SRC-E73001D9AC-L000018](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L18) | 18 | `"تستخدم الوثيقة الكلمات التالية بدقة:"` | — |
| [SRC-E73001D9AC-L000019](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L19) | 19 | `""` | — |
| [SRC-E73001D9AC-L000020](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L20) | 20 | `"- **MUST / إلزامي:** شرط لا يجوز تجاوزه في التنفيذ المستهدف أو الإصدار الذي يدّعي استيفاءه."` | — |
| [SRC-E73001D9AC-L000021](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L21) | 21 | `"- **SHOULD / مطلوب افتراضيًا:** يُطبّق ما لم يوجد سبب موثق ومراجع لاستثناء محدود."` | — |
| [SRC-E73001D9AC-L000022](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L22) | 22 | `"- **MAY / اختياري:** يُطبّق عندما يحقق قيمة مثبتة ولا يضيف مخاطر غير مقبولة."` | — |
| [SRC-E73001D9AC-L000023](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L23) | 23 | `"- **VERIFIED / متحقق:** تؤيده نتيجة فحص أو اختبار أو قياس محدد يمكن الرجوع إليه."` | — |
| [SRC-E73001D9AC-L000024](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L24) | 24 | `"- **INFERRED / مستنتج:** تفسير مرجح مبني على الأدلة المتاحة، وليس حقيقة اختبارية."` | — |
| [SRC-E73001D9AC-L000025](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L25) | 25 | `"- **PROPOSED / مقترح:** قرار تصميم أو هدف لم يُثبت تنفيذه بعد."` | — |
| [SRC-E73001D9AC-L000026](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L26) | 26 | `"- **UNKNOWN / غير معلوم:** لا تتوفر أدلة كافية للحكم."` | — |
| [SRC-E73001D9AC-L000027](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L27) | 27 | `""` | — |
| [SRC-E73001D9AC-L000028](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L28) | 28 | `"هذه الوثيقة **متطلبات مستقبلية ومعيار مراجعة**، وليست إعلانًا بأن المستودع الحالي يحققها. يجب أن يُسجّل لكل بند مهم: حالته، والدليل، والمخاطر المفتوحة، وخطة المعالجة، والمسؤول عن التحقق. لا تُحوّل كلمة PROPOSED إلى VERIFIED إلا بدليل فعلي."` | — |
| [SRC-E73001D9AC-L000029](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L29) | 29 | `""` | — |
| [SRC-E73001D9AC-L000030](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L30) | 30 | `"---"` | — |
| [SRC-E73001D9AC-L000031](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L31) | 31 | `""` | — |
| [SRC-E73001D9AC-L000032](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L32) | 32 | `"# الجزء الأول — الرسالة العليا ومبادئ التصميم"` | — |
| [SRC-E73001D9AC-L000033](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L33) | 33 | `""` | — |
| [SRC-E73001D9AC-L000034](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L34) | 34 | `"## 1. الرؤية"` | — |
| [SRC-E73001D9AC-L000035](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L35) | 35 | `""` | — |
| [SRC-E73001D9AC-L000036](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L36) | 36 | `"بناء Omarai كنواة ذكاء اصطناعي عربية عملية تستطيع استقبال الأسئلة والمهام، وفهمها، والبحث عند الحاجة، واستخدام الأدوات التي ثبت عملها، وتوليد إجابات مستندة إلى الأدلة، وإظهار حدود المعرفة بوضوح؛ مع هندسة تتيح النمو من نموذج أولي محدود إلى خدمة إنتاجية موثوقة عندما تسمح الموارد والاستضافة بذلك."` | — |
| [SRC-E73001D9AC-L000037](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L37) | 37 | `""` | — |
| [SRC-E73001D9AC-L000038](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L38) | 38 | `"الطموح هو بلوغ مستوى احترافي في الاعتمادية والأمان والكفاءة، مع الاستفادة من الممارسات الصناعية المعروفة. لا يعني ذلك ادعاء التكافؤ مع المنصات العالمية قبل وجود بنية تشغيلية وميزانية واختبارات وتدقيق خارجي مناسب."` | — |
| [SRC-E73001D9AC-L000039](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L39) | 39 | `""` | — |
| [SRC-E73001D9AC-L000040](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L40) | 40 | `"## 2. المبادئ الحاكمة غير القابلة للتفاوض"` | — |
| [SRC-E73001D9AC-L000041](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L41) | 41 | `""` | — |
| [SRC-E73001D9AC-L000042](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L42) | 42 | `"1. **Evidence over assertion:** لا نعلن نجاحًا بلا دليل."` | — |
| [SRC-E73001D9AC-L000043](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L43) | 43 | `"2. **Security by design:** الأمن جزء من التصميم ودورة التطوير، لا طبقة تجميلية لاحقة."` | — |
| [SRC-E73001D9AC-L000044](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L44) | 44 | `"3. **Reliability before feature growth:** لا نضيف قدرات تُضعف الاستقرار أو تفتح صلاحيات غير مضبوطة."` | — |
| [SRC-E73001D9AC-L000045](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L45) | 45 | `"4. **Least privilege:** أقل صلاحية لازمة لكل مستخدم ومكوّن وأداة."` | — |
| [SRC-E73001D9AC-L000046](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L46) | 46 | `"5. **Fail safely, degrade gracefully:** تعطل مكوّن لا ينبغي أن يسقط النظام كله، والفشل يجب أن يكون محدود الأثر وواضحًا."` | — |
| [SRC-E73001D9AC-L000047](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L47) | 47 | `"6. **Bound every expensive operation:** كل بحث أو استدعاء نموذج أو جلب صفحة أو حلقة تخطيط أو إعادة محاولة له حدود زمنية وكمية وتكلفة."` | — |
| [SRC-E73001D9AC-L000048](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L48) | 48 | `"7. **Simple path first:** السؤال البسيط يسلك المسار الأقصر؛ لا نستدعي التخطيط العميق أو الإنترنت بلا حاجة."` | — |
| [SRC-E73001D9AC-L000049](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L49) | 49 | `"8. **Independent verification:** لا نعتبر مراجعة النموذج لنفسه تحققًا مستقلًا، ولا نعتبر اتفاق محركات البحث إثباتًا للحقيقة."` | — |
| [SRC-E73001D9AC-L000050](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L50) | 50 | `"9. **Privacy by default:** نجمع أقل بيانات لازمة، ونوضح ما يغادر النظام إلى مزودي الخدمة."` | — |
| [SRC-E73001D9AC-L000051](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L51) | 51 | `"10. **Separation of concerns:** حدود واضحة بين الطلبات، والتخطيط، والبحث، وتنفيذ الأدوات، والتحقق، والبيانات، والمراقبة."` | — |
| [SRC-E73001D9AC-L000052](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L52) | 52 | `"11. **Observable behavior:** يجب أن يمكن قياس النجاح والفشل والبطء والاستهلاك، مع حماية الخصوصية."` | — |
| [SRC-E73001D9AC-L000053](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L53) | 53 | `"12. **Reversible decisions:** التغييرات الهندسية الكبيرة تمر عبر قرارات موثقة ويمكن التراجع عنها."` | — |
| [SRC-E73001D9AC-L000054](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L54) | 54 | `"13. **Human control for consequential actions:** لا تمنح النماذج استقلالًا مفتوحًا لإجراء تغييرات حساسة أو آثار خارجية."` | — |
| [SRC-E73001D9AC-L000055](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L55) | 55 | `"14. **No “security by obscurity”:** الحماية تعتمد على ضوابط واختبارات وصلاحيات، لا على إخفاء تفاصيل التصميم."` | — |
| [SRC-E73001D9AC-L000056](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L56) | 56 | `"15. **Cost-aware engineering:** نختار التعقيد والاعتماديات وفق منفعة مقاسة وتكلفة ومخاطر حقيقية، لا لمجرد أن المعمارية تبدو أكبر."` | — |
| [SRC-E73001D9AC-L000057](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L57) | 57 | `"16. **Arabic-first quality:** دعم العربية واتجاه RTL وجودة البحث والاستشهادات جزء من الجودة الأساسية، وليس تحسينًا ثانويًا."` | — |
| [SRC-E73001D9AC-L000058](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L58) | 58 | `"17. **No false universality:** لا نقول إن الأداة تعمل دائمًا، أو إن كل موقع قابل للاستخراج، أو إن كل سؤال يمكن الإجابة عنه يقينًا."` | — |
| [SRC-E73001D9AC-L000059](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L59) | 59 | `"18. **Owner-controlled release:** لا يتم دمج تغييرات جوهرية أو إطلاقها باعتبارها معتمدة نهائيًا دون قرار صاحب المشروع."` | — |
| [SRC-E73001D9AC-L000060](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L60) | 60 | `""` | — |
| [SRC-E73001D9AC-L000061](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L61) | 61 | `"## 3. الطموح الأقصى لا يعني تعقيدًا أقصى"` | — |
| [SRC-E73001D9AC-L000062](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L62) | 62 | `""` | — |
| [SRC-E73001D9AC-L000063](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L63) | 63 | `"يُراجع Omarai بأوسع تغطية تخصصية ممكنة، لكن لا تُنشأ طبقات تشغيلية أو خدمات مستقلة لمجرد زيادة العدد. المقصود هو **أقصى تغطية مفيدة للمخاطر والتخصصات، وأقل تعقيد تشغيلي يحققها**. يبدأ المشروع بوحدات منطقية واضحة؛ ثم تُفصل الخدمات أو تُضاف البنية الموزعة عندما تثبت اختبارات الحمل أو حدود العزل أو التوافر الحاجة إلى ذلك."` | — |
| [SRC-E73001D9AC-L000064](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L64) | 64 | `""` | — |
| [SRC-E73001D9AC-L000065](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L65) | 65 | `"### 3.1 قاعدة حاكمة لتنظيم القدرات والمهارات والوكلاء"` | — |
| [SRC-E73001D9AC-L000066](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L66) | 66 | `""` | — |
| [SRC-E73001D9AC-L000067](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L67) | 67 | `"**[PROPOSED — اعتماد بشري مطلوب]** يكون الاتجاه الافتراضي لتطور القدرات هو: نواة موثوقة ← أدوات وقدرات بعقود وصلاحيات واضحة ← مهارات قابلة لإعادة الاستخدام ← سير عمل محدود وقابل للاختبار ← سياق تنفيذ مؤقت لكل مهمة ← وكلاء يُنشؤون عند ثبوت الحاجة. ولا يُنشأ وكيل مستقل لكل سؤال أو تخصص تلقائيًا."` | — |
| [SRC-E73001D9AC-L000068](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L68) | 68 | `""` | — |
| [SRC-E73001D9AC-L000069](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L69) | 69 | `"- الأداة تنفذ عملية بعقد معلوم؛ والقدرة تحدد ما يُسمح به؛ والمهارة تجمع منطقًا قابلًا لإعادة الاستخدام؛ وسير العمل يحدد ترتيب الخطوات وشروط التوقف؛ وملف تعريف الوكيل وصفة لإعادة الاستخدام، لا برنامج حر."` | — |
| [SRC-E73001D9AC-L000070](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L70) | 70 | `"- الخطة التي يقترحها النموذج بيانات غير موثوقة حتى تُفحص بنيتها وصلاحياتها وميزانيتها؛ لا تمنح أي خطة أو مهارة أو ملف تعريف صلاحيات لنفسه."` | — |
| [SRC-E73001D9AC-L000071](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L71) | 71 | `"- يكون سياق التشغيل مؤقتًا ومعزولًا افتراضيًا. لا تُضاف ذاكرة دائمة أو وكيل دائم إلا لمطلب واضح وسياسة احتفاظ وصلاحيات واختبارات مناسبة."` | — |
| [SRC-E73001D9AC-L000072](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L72) | 72 | `"- تُفصل إدارة المسودات والتعريفات والاعتماد منطقيًا عن تشغيل المهام. لا يستطيع النموذج أو Meta-Agent اعتماد نفسه أو تعديل سقف صلاحيات المنصة."` | — |
| [SRC-E73001D9AC-L000073](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L73) | 73 | `"- لا يُنشأ Meta-Agent ولا يُسمح بتوليد كود تنفيذي في المسار الأساسي قبل إثبات الحاجة بفحوص وقياسات؛ وإذا أضيف Meta-Agent مستقبلًا، يبدأ بإنتاج مسودات تعريفية فقط، تمر بالتحقق والاختبارات والموافقة."` | — |
| [SRC-E73001D9AC-L000074](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L74) | 74 | `"- تبقى مهام البحث والأدلة والأمان والتحقق في الدستور قائمة وواجبة؛ لا يستبدل التنظيم الجديد للقدرات هذه الضوابط."` | — |
| [SRC-E73001D9AC-L000075](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L75) | 75 | `""` | — |
| [SRC-E73001D9AC-L000076](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L76) | 76 | `"التفصيل التنفيذي وبوابات الانتقال موضح في [المعمارية الحاكمة للقدرات والمهارات وسير العمل والوكلاء](OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md). هذا توجيه معماري مستهدف، وليس ادعاءً بأن مكوناته كلها منفذة."` | — |
| [SRC-E73001D9AC-L000077](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L77) | 77 | `""` | — |
| [SRC-E73001D9AC-L000078](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L78) | 78 | `"---"` | — |
| [SRC-E73001D9AC-L000079](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L79) | 79 | `""` | — |
| [SRC-E73001D9AC-L000080](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L80) | 80 | `"# الجزء الثاني — حوكمة الخبراء والمراجعة متعددة التخصصات"` | — |
| [SRC-E73001D9AC-L000081](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L81) | 81 | `""` | — |
| [SRC-E73001D9AC-L000082](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L82) | 82 | `"## 4. مجالات الخبرة التي يجب تغطيتها"` | — |
| [SRC-E73001D9AC-L000083](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L83) | 83 | `""` | — |
| [SRC-E73001D9AC-L000084](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L84) | 84 | `"في القرارات المعمارية والأمنية عالية التأثير، تُراجع الآثار من زوايا التخصصات المناسبة التالية. هذه قائمة تغطية للمراجعة، وليست ادعاءً بأن مجموعة خبراء أو وكلاء آليين تعمل حاليًا داخل المستودع."` | — |
| [SRC-E73001D9AC-L000085](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L85) | 85 | `""` | — |
| [SRC-E73001D9AC-L000086](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L86) | 86 | `"1. هندسة البرمجيات والمعمارية."` | — |
| [SRC-E73001D9AC-L000087](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L87) | 87 | `"2. هندسة الأنظمة والتزامن وإدارة الموارد."` | — |
| [SRC-E73001D9AC-L000088](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L88) | 88 | `"3. SRE والاعتمادية والتعافي من الأعطال."` | — |
| [SRC-E73001D9AC-L000089](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L89) | 89 | `"4. الأمن السيبراني وهندسة التهديدات."` | — |
| [SRC-E73001D9AC-L000090](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L90) | 90 | `"5. أمن تطبيقات الويب وواجهات API."` | — |
| [SRC-E73001D9AC-L000091](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L91) | 91 | `"6. أمن تطبيقات LLM والوكلاء ومقاومة حقن التعليمات."` | — |
| [SRC-E73001D9AC-L000092](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L92) | 92 | `"7. أمن الشبكات والـ DNS وقيود الخروج إلى الإنترنت."` | — |
| [SRC-E73001D9AC-L000093](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L93) | 93 | `"8. هندسة الأداء واختبارات الحمل."` | — |
| [SRC-E73001D9AC-L000094](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L94) | 94 | `"9. هندسة البيانات وقواعد البيانات والمخططات والترحيلات."` | — |
| [SRC-E73001D9AC-L000095](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L95) | 95 | `"10. هندسة البحث والاسترجاع وترتيب النتائج."` | — |
| [SRC-E73001D9AC-L000096](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L96) | 96 | `"11. تقييم النماذج والهلوسة والتحقق من الادعاءات."` | — |
| [SRC-E73001D9AC-L000097](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L97) | 97 | `"12. الخصوصية وحوكمة البيانات والاحتفاظ بها."` | — |
| [SRC-E73001D9AC-L000098](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L98) | 98 | `"13. DevOps وسير CI/CD والتوزيع والتراجع."` | — |
| [SRC-E73001D9AC-L000099](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L99) | 99 | `"14. أمن سلسلة التوريد البرمجية والاعتماديات."` | — |
| [SRC-E73001D9AC-L000100](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L100) | 100 | `"15. ضمان الجودة والاختبارات الآلية واختبارات الفشل."` | — |
| [SRC-E73001D9AC-L000101](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L101) | 101 | `"16. التصميم وتجربة المستخدم وإمكانية الوصول وRTL."` | — |
| [SRC-E73001D9AC-L000102](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L102) | 102 | `"17. جودة اللغة العربية والتوطين واتجاهات النصوص."` | — |
| [SRC-E73001D9AC-L000103](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L103) | 103 | `"18. التكلفة والقيود التشغيلية واستهلاك حصص الخدمات المجانية."` | — |
| [SRC-E73001D9AC-L000104](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L104) | 104 | `"19. إدارة الحوادث والاستجابة الأمنية والتعافي من الكوارث."` | — |
| [SRC-E73001D9AC-L000105](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L105) | 105 | `"20. الحوكمة والتوثيق وإدارة التغيير."` | — |
| [SRC-E73001D9AC-L000106](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L106) | 106 | `""` | — |
| [SRC-E73001D9AC-L000107](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L107) | 107 | `"### 4.1 قاعدة المراجعة"` | — |
| [SRC-E73001D9AC-L000108](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L108) | 108 | `""` | — |
| [SRC-E73001D9AC-L000109](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L109) | 109 | `"- التغييرات الصغيرة منخفضة المخاطر تخضع لاختبارات الوحدة والمراجعة المعتادة."` | — |
| [SRC-E73001D9AC-L000110](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L110) | 110 | `"- التغييرات التي تمس الإنترنت أو الصلاحيات أو الذاكرة المشتركة أو التخزين أو تنفيذ الأدوات تخضع لمراجعة أمنية واختبارات فشل مناسبة."` | — |
| [SRC-E73001D9AC-L000111](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L111) | 111 | `"- التغييرات التي تمس المعمارية أو التوسع أو حدود الثقة تخضع لمراجعة معمارية، وتهديدات، وأداء، وتشغيل، وتوثيق قرار."` | — |
| [SRC-E73001D9AC-L000112](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L112) | 112 | `"- عند تعارض آراء المراجعين، يُسجّل التعارض والأدلة والبدائل والمخاطر بدل إخفائه خلف تصويت عددي أو إجابة نموذج لغوي واحدة."` | — |
| [SRC-E73001D9AC-L000113](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L113) | 113 | `"- لا تُستخدم أسماء خبراء أو مراجعات آلية مزعومة كدليل. يُذكر ما إذا كانت المراجعة بشرية أو آلية أو مجرد قائمة تحقق."` | — |
| [SRC-E73001D9AC-L000114](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L114) | 114 | `""` | — |
| [SRC-E73001D9AC-L000115](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L115) | 115 | `"---"` | — |
| [SRC-E73001D9AC-L000116](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L116) | 116 | `""` | — |
| [SRC-E73001D9AC-L000117](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L117) | 117 | `"# الجزء الثالث — المعمارية المنطقية المستهدفة"` | — |
| [SRC-E73001D9AC-L000118](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L118) | 118 | `""` | — |
| [SRC-E73001D9AC-L000119](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L119) | 119 | `"## 5. طبقات النظام وحدود الثقة"` | — |
| [SRC-E73001D9AC-L000120](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L120) | 120 | `""` | — |
| [SRC-E73001D9AC-L000121](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L121) | 121 | `"التقسيم التالي **خريطة منطقية مرجعية**. يجوز دمج طبقات عدة داخل تطبيق واحد في المراحل الأولى، بشرط الحفاظ على حدود المسؤوليات واختبارها. ولا يُشترط أن تتحول كل طبقة إلى خدمة مستقلة."` | — |
| [SRC-E73001D9AC-L000122](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L122) | 122 | `""` | — |
| [SRC-E73001D9AC-L000123](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L123) | 123 | `"### الطبقة 1 — واجهة المستخدم وقنوات الإدخال"` | — |
| [SRC-E73001D9AC-L000124](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L124) | 124 | `"- واجهة عربية RTL واضحة ومتجاوبة."` | — |
| [SRC-E73001D9AC-L000125](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L125) | 125 | `"- تمييز حالة الطلب: مستلم، قيد التنفيذ، مكتمل، متدهور، فشل."` | — |
| [SRC-E73001D9AC-L000126](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L126) | 126 | `"- عرض المصادر والتحذيرات وحدود المعرفة عند الحاجة."` | — |
| [SRC-E73001D9AC-L000127](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L127) | 127 | `"- عدم وضع مفاتيح أو أسرار أو صلاحيات خادم في كود المتصفح."` | — |
| [SRC-E73001D9AC-L000128](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L128) | 128 | `"- عدم اعتبار إخفاء زر في الواجهة وسيلة لتطبيق الصلاحيات؛ يجب فرض الصلاحيات في الخادم."` | — |
| [SRC-E73001D9AC-L000129](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L129) | 129 | `""` | — |
| [SRC-E73001D9AC-L000130](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L130) | 130 | `"### الطبقة 2 — حافة الخدمة وواجهة API"` | — |
| [SRC-E73001D9AC-L000131](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L131) | 131 | `"- التحقق الصارم من بنية الطلب وأنواعه وأحجامه."` | — |
| [SRC-E73001D9AC-L000132](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L132) | 132 | `"- حدود حجم الجسم والمهلات والاتصالات ومعدل الطلبات."` | — |
| [SRC-E73001D9AC-L000133](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L133) | 133 | `"- أخطاء واضحة لا تكشف تفاصيل داخلية أو مسارات ملفات أو أسرارًا."` | — |
| [SRC-E73001D9AC-L000134](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L134) | 134 | `"- سياسة CORS مقيدة بالنطاقات المعتمدة."` | — |
| [SRC-E73001D9AC-L000135](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L135) | 135 | `"- عند استخدام ملفات تعريف الارتباط للمصادقة، تُراجع حماية CSRF وخصائص Secure وHttpOnly وSameSite بحسب تصميم الجلسة."` | — |
| [SRC-E73001D9AC-L000136](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L136) | 136 | `"- واجهات التشخيص والإدارة لا تُعرض للعامة دون حماية مناسبة."` | — |
| [SRC-E73001D9AC-L000137](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L137) | 137 | `""` | — |
| [SRC-E73001D9AC-L000138](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L138) | 138 | `"### الطبقة 3 — الهوية والمستأجرون والصلاحيات"` | — |
| [SRC-E73001D9AC-L000139](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L139) | 139 | `"- لكل مستخدم أو جلسة أو مهمة معرف واضح ونطاق صلاحيات."` | — |
| [SRC-E73001D9AC-L000140](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L140) | 140 | `"- فصل تام بين سياق الطلبات المتزامنة ومنع مشاركة المتغيرات القابلة للتغيير بين المستخدمين."` | — |
| [SRC-E73001D9AC-L000141](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L141) | 141 | `"- تحقق من ملكية كل سجل قبل قراءته أو تعديله أو تصديره."` | — |
| [SRC-E73001D9AC-L000142](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L142) | 142 | `"- لا يكفي تخمين معرف غير قابل للتسلسل لمنع الوصول غير المصرح به؛ يجب التحقق من الصلاحية على الخادم."` | — |
| [SRC-E73001D9AC-L000143](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L143) | 143 | `"- يظل وضع الحلقة المحلية أو الاستخدام الشخصي مختلفًا عن وضع خدمة عامة متعددة المستخدمين، ويجب توثيق الوضع الفعلي لكل نشر."` | — |
| [SRC-E73001D9AC-L000144](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L144) | 144 | `""` | — |
| [SRC-E73001D9AC-L000145](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L145) | 145 | `"### الطبقة 4 — بوابة السياسات وإساءة الاستخدام"` | — |
| [SRC-E73001D9AC-L000146](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L146) | 146 | `"- تحديد أحجام الإدخال والتاريخ المرفق وعدد المصادر والصفحات وعمق المهام."` | — |
| [SRC-E73001D9AC-L000147](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L147) | 147 | `"- تحديد معدل الطلبات وفق الهوية وعنوان المصدر عند ملاءمة ذلك، مع مراعاة NAT والخصوصية."` | — |
| [SRC-E73001D9AC-L000148](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L148) | 148 | `"- فرض ميزانيات للوقت والموارد واستهلاك النموذج والبحث."` | — |
| [SRC-E73001D9AC-L000149](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L149) | 149 | `"- إرجاع 429 عند تجاوز حدود المعدل و503 عند العجز المؤقت عن القبول، مع Retry-After عند ملاءمته."` | — |
| [SRC-E73001D9AC-L000150](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L150) | 150 | `"- حماية الخدمة من حلقات الوكيل غير المنتهية، والطلبات المتضخمة، وإساءة استخدام العمليات المكلفة."` | — |
| [SRC-E73001D9AC-L000151](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L151) | 151 | `"- إضافة CAPTCHA أو تحديات إضافية فقط عند وجود دليل على إساءة استخدام، لا كبديل عن حدود موارد صحيحة."` | — |
| [SRC-E73001D9AC-L000152](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L152) | 152 | `""` | — |
| [SRC-E73001D9AC-L000153](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L153) | 153 | `"### الطبقة 5 — منسق الطلبات (Request Orchestrator)"` | — |
| [SRC-E73001D9AC-L000154](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L154) | 154 | `"- إنشاء سياق مستقل لكل طلب يتضمن deadline وميزانيات محددة وإشارة إلغاء."` | — |
| [SRC-E73001D9AC-L000155](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L155) | 155 | `"- الحفاظ على حدود واضحة لعدد خطوات التخطيط واستدعاءات الأدوات واستدعاءات النماذج والصفحات."` | — |
| [SRC-E73001D9AC-L000156](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L156) | 156 | `"- إنهاء الطلب عند بلوغ الميزانية بدل الاستمرار غير المحدود."` | — |
| [SRC-E73001D9AC-L000157](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L157) | 157 | `"- تمييز الإلغاء بسبب المستخدم من انتهاء الوقت ومن رفض السياسة ومن تعطل المزود."` | — |
| [SRC-E73001D9AC-L000158](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L158) | 158 | `"- تمكين إلغاء المهام التابعة عند إلغاء الطلب الأصلي."` | — |
| [SRC-E73001D9AC-L000159](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L159) | 159 | `"- الحفاظ على معرف تتبع واحد عبر مراحل الطلب، دون وضع أسرار أو بيانات حساسة في المعرف."` | — |
| [SRC-E73001D9AC-L000160](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L160) | 160 | `""` | — |
| [SRC-E73001D9AC-L000161](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L161) | 161 | `"ملاحظة تنفيذية حاكمة: يُنشأ سياق وميزانية منفصلان لكل طلب، ويستخدم المنسق أبسط مسار كافٍ للمهمة. تكون مطابقة المهارات وسير العمل المسجلين هي الخيار الأول قبل إنشاء تعريف وكيل جديد. لا يلزم أن يكون التخطيط مكوّنًا مستقلًا أو خدمة خارجية؛ تحفظ الواجهة والعقد وحدود الصلاحيات حتى لو نُفذت داخل وحدة واحدة."` | — |
| [SRC-E73001D9AC-L000162](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L162) | 162 | `""` | — |
| [SRC-E73001D9AC-L000163](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L163) | 163 | `"### الطبقة 6 — فهم النية والتخطيط"` | — |
| [SRC-E73001D9AC-L000164](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L164) | 164 | `"- مسار مباشر للأسئلة البسيطة التي لا تحتاج إلى بحث."` | — |
| [SRC-E73001D9AC-L000165](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L165) | 165 | `"- مسار بحث للأسئلة التي تتطلب معلومات حديثة أو مصادر."` | — |
| [SRC-E73001D9AC-L000166](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L166) | 166 | `"- مسار متعدد الخطوات للمهام المعقدة فقط."` | — |
| [SRC-E73001D9AC-L000167](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L167) | 167 | `"- مخطط بيانات صارم لخطة النموذج، مع التحقق من كل حقل قبل التنفيذ."` | — |
| [SRC-E73001D9AC-L000168](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L168) | 168 | `"- الخطة التي يصدرها النموذج اقتراح غير موثوق، وليست إذنًا لتنفيذ عملية."` | — |
| [SRC-E73001D9AC-L000169](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L169) | 169 | `"- لا يُسمح للخطة بزيادة الميزانية أو تجاوز الصلاحيات أو تعديل سياسات الأمان."` | — |
| [SRC-E73001D9AC-L000170](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L170) | 170 | `"- الحد من إعادة التخطيط وعدد الخطوات وتكرار الأدوات."` | — |
| [SRC-E73001D9AC-L000171](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L171) | 171 | `"- عند عدم الحاجة إلى بحث جديد، يُعاد استخدام سياق صالح ومحدد العمر بدل إعادة كل العمليات."` | — |
| [SRC-E73001D9AC-L000172](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L172) | 172 | `""` | — |
| [SRC-E73001D9AC-L000173](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L173) | 173 | `"تظل مخرجات التخطيط التي ينتجها النموذج **اقتراحات غير موثوقة**. عند الحاجة إلى تمثيل منظم للمهمة، تستخدم TaskSpec بمدخلات ومخرجات وقيود ومعايير قبول وقدرات مطلوبة؛ لا تمنح المواصفة صلاحيات. تُتحقق الخطة حتميًا قبل التنفيذ، وتُرفض الخطوات غير المعروفة أو المتجاوزة للحدود. الخطط المتكررة والحساسة تُفضّل لها مسارات Workflow محددة يمكن اختبارها، مع إبقاء المسار المباشر للأسئلة البسيطة."` | — |
| [SRC-E73001D9AC-L000174](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L174) | 174 | `""` | — |
| [SRC-E73001D9AC-L000175](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L175) | 175 | `"### الطبقة 7 — طبقة البحث وجلب الصفحات"` | — |
| [SRC-E73001D9AC-L000176](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L176) | 176 | `"- فصل موصلات البحث عن محرك التخطيط وعن منطق الإجابة."` | — |
| [SRC-E73001D9AC-L000177](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L177) | 177 | `"- تحديد timeout وconcurrency وresponse-size وresult-count لكل موصل."` | — |
| [SRC-E73001D9AC-L000178](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L178) | 178 | `"- عزل فشل موصل واحد؛ لا يمنع بقية المصادر من العمل إذا كان المسار يسمح بذلك."` | — |
| [SRC-E73001D9AC-L000179](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L179) | 179 | `"- تحديد تاريخ النتائج ومصدرها ووقت الاسترجاع والطلب الذي جلبها."` | — |
| [SRC-E73001D9AC-L000180](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L180) | 180 | `"- جلب المحتوى العام المسموح فقط؛ لا تجاوز لتسجيل الدخول أو paywall أو ضوابط الوصول."` | — |
| [SRC-E73001D9AC-L000181](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L181) | 181 | `"- احترام شروط استخدام المصادر وحدود الطلبات المسموحة."` | — |
| [SRC-E73001D9AC-L000182](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L182) | 182 | `"- تخزين النتائج مؤقتًا فقط مع سياسة صلاحية وتحديث وحذف مناسبة."` | — |
| [SRC-E73001D9AC-L000183](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L183) | 183 | `"- عدم افتراض استقلال المصادر لمجرد أن النتائج ظهرت في أكثر من محرك."` | — |
| [SRC-E73001D9AC-L000184](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L184) | 184 | `""` | — |
| [SRC-E73001D9AC-L000185](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L185) | 185 | `"### الطبقة 8 — بوابة الأدوات وسجل قدراتها"` | — |
| [SRC-E73001D9AC-L000186](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L186) | 186 | `"كل أداة مسجلة بوصف قابل للتحقق يشمل:"` | — |
| [SRC-E73001D9AC-L000187](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L187) | 187 | `"- الاسم والإصدار والجهة المالكة."` | — |
| [SRC-E73001D9AC-L000188](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L188) | 188 | `"- المدخلات والمخرجات والمخطط المتوقع."` | — |
| [SRC-E73001D9AC-L000189](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L189) | 189 | `"- الصلاحيات التي تحتاجها."` | — |
| [SRC-E73001D9AC-L000190](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L190) | 190 | `"- مهلة التنفيذ والميزانية والحدود القصوى."` | — |
| [SRC-E73001D9AC-L000191](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L191) | 191 | `"- ما إذا كانت للقراءة فقط أم ذات أثر خارجي."` | — |
| [SRC-E73001D9AC-L000192](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L192) | 192 | `"- طريقة فحص صحتها، وحدود الفحص، ووقت آخر تحقق."` | — |
| [SRC-E73001D9AC-L000193](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L193) | 193 | `"- مخاطرها وطريقة تعطيلها."` | — |
| [SRC-E73001D9AC-L000194](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L194) | 194 | `"- اختبارات النجاح والفشل والسلوك عند انقطاع الاتصال."` | — |
| [SRC-E73001D9AC-L000195](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L195) | 195 | `""` | — |
| [SRC-E73001D9AC-L000196](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L196) | 196 | `"لا تُظهر المنظومة الأداة على أنها جاهزة لمجرد وجود مفتاح إعداد لها. إعداد المفتاح يثبت وجود إعداد فقط، ولا يثبت الوصول أو الصلاحيات أو النجاح الفعلي."` | — |
| [SRC-E73001D9AC-L000197](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L197) | 197 | `""` | — |
| [SRC-E73001D9AC-L000198](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L198) | 198 | `"لا تساوي حالة الأداة المسجلة حالة الأداة المختبرة أو المهيأة أو المتاحة لحظيًا أو الناجحة في الطلب الحالي. يجب أن تعرض التشخيصات الحالة الدقيقة، ولا تمنح قيمة إعداد أو وجود دالة وحدهما دليلًا على نجاح التكامل."` | — |
| [SRC-E73001D9AC-L000199](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L199) | 199 | `""` | — |
| [SRC-E73001D9AC-L000200](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L200) | 200 | `"### الطبقة 9 — تنفيذ الأدوات والعزل"` | — |
| [SRC-E73001D9AC-L000201](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L201) | 201 | `"- رفض تنفيذ الأوامر الحرة التي يقدمها النموذج."` | — |
| [SRC-E73001D9AC-L000202](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L202) | 202 | `"- استخدام واجهات معرفة ومتحقق منها بدل منح النموذج وصولًا عامًا للنظام أو الشبكة أو قاعدة البيانات."` | — |
| [SRC-E73001D9AC-L000203](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L203) | 203 | `"- تطبيق allowlist للوجهات والأوامر حيث ينطبق ذلك."` | — |
| [SRC-E73001D9AC-L000204](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L204) | 204 | `"- الحد من الاتصالات الخارجة، وعدم السماح للأداة بتجاوز القيود عبر إعادة توجيه أو اسم DNS بديل."` | — |
| [SRC-E73001D9AC-L000205](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L205) | 205 | `"- عزل أدوات المعالجة غير الموثوقة عن أسرار الخدمة والملفات الحساسة."` | — |
| [SRC-E73001D9AC-L000206](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L206) | 206 | `"- إذا استُخدم sandbox في مرحلة مستقبلية، يجب اختبار حدوده وموارده ومنافذ الهروب؛ الاسم وحده لا يثبت العزل."` | — |
| [SRC-E73001D9AC-L000207](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L207) | 207 | `"- القراءة فقط هي الوضع الافتراضي."` | — |
| [SRC-E73001D9AC-L000208](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L208) | 208 | `"- أي فعل خارجي مؤثر أو غير قابل للعكس يحتاج إلى تفويض وصلاحيات وتأكيد واضح وفق مستوى المخاطر."` | — |
| [SRC-E73001D9AC-L000209](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L209) | 209 | `"- مفاتيح الخدمات لا تُمرر إلى النموذج أو المحتوى المسترجع."` | — |
| [SRC-E73001D9AC-L000210](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L210) | 210 | `"- نتائج الأدوات بيانات غير موثوقة إلى أن تتحقق سلامتها وبنيتها."` | — |
| [SRC-E73001D9AC-L000211](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L211) | 211 | `""` | — |
| [SRC-E73001D9AC-L000212](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L212) | 212 | `"تُمرّر استدعاءات الأدوات عبر بوابة أو وسيط تنفيذ مركزي يطبق قائمة السماح والتحقق من المدخلات والهوية والحدود والميزانية وسجل النتيجة. الصلاحيات الفعلية لا تستمد من system prompt أو ملف تعريف وحده. يمنع التنفيذ العام للكود المولّد، وتُعزل الموصلات التي تلمس الشبكة أو بيانات خاصة بما يتناسب مع خطرها. لا يلزم أن يكون الوسيط خدمة مستقلة في المرحلة الأولى؛ المطلوب حدّ إنفاذ يمكن اختباره."` | — |
| [SRC-E73001D9AC-L000213](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L213) | 213 | `""` | — |
| [SRC-E73001D9AC-L000214](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L214) | 214 | `"### الطبقة 10 — توحيد الأدلة والمصادر (Evidence Ledger)"` | — |
| [SRC-E73001D9AC-L000215](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L215) | 215 | `"- حفظ الرابط واسم المصدر وتوقيت الوصول والبيانات الوصفية اللازمة للتحقق."` | — |
| [SRC-E73001D9AC-L000216](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L216) | 216 | `"- تمييز الاقتباس أو المعلومة المستخرجة عن استنتاج النموذج."` | — |
| [SRC-E73001D9AC-L000217](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L217) | 217 | `"- ربط الادعاءات المهمة بمصادرها كلما أمكن."` | — |
| [SRC-E73001D9AC-L000218](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L218) | 218 | `"- اكتشاف الاقتباسات غير المدعومة أو المراجع المفقودة."` | — |
| [SRC-E73001D9AC-L000219](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L219) | 219 | `"- عرض فشل الوصول والتعارض بين المصادر وتضارب التواريخ عند تأثيره على النتيجة."` | — |
| [SRC-E73001D9AC-L000220](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L220) | 220 | `"- عدم تقديم مؤشرات اتساع التغطية على أنها احتمال إحصائي لصحة الإجابة."` | — |
| [SRC-E73001D9AC-L000221](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L221) | 221 | `"- عدم الادعاء بأن كل مصدر أصلي أو محدث دون فحص قابل للإثبات."` | — |
| [SRC-E73001D9AC-L000222](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L222) | 222 | `""` | — |
| [SRC-E73001D9AC-L000223](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L223) | 223 | `"### الطبقة 11 — التحقق من الإجابة والنتائج"` | — |
| [SRC-E73001D9AC-L000224](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L224) | 224 | `"- التحقق من شكل البيانات والمخرجات قبل عرضها أو تمريرها إلى أداة أخرى."` | — |
| [SRC-E73001D9AC-L000225](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L225) | 225 | `"- استخدام قواعد حتمية أو استعلامات مباشرة أو مصدر مستقل للتحقق عندما يكون ذلك ممكنًا."` | — |
| [SRC-E73001D9AC-L000226](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L226) | 226 | `"- المراجعة اللغوية من النموذج نفسه قد تحسن الوضوح، لكنها ليست تحققًا مستقلًا من الحقيقة."` | — |
| [SRC-E73001D9AC-L000227](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L227) | 227 | `"- عند تعارض الأدلة، يوضح Omarai التعارض بدل اختيار إجابة بثقة زائفة."` | — |
| [SRC-E73001D9AC-L000228](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L228) | 228 | `"- عند نقص الأدلة، يصرّح بما لم يتمكن من إثباته."` | — |
| [SRC-E73001D9AC-L000229](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L229) | 229 | `"- لا يُعاد البحث أو استخدام نموذج إضافي إلا عندما تكون القيمة المتوقعة أكبر من كلفته ومخاطره."` | — |
| [SRC-E73001D9AC-L000230](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L230) | 230 | `"- العمليات ذات الأثر الخارجي لا تُعتبر ناجحة لمجرد أن النموذج قال إنها نجحت؛ يجب قراءة نتيجة الأداة والتحقق منها."` | — |
| [SRC-E73001D9AC-L000231](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L231) | 231 | `""` | — |
| [SRC-E73001D9AC-L000232](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L232) | 232 | `"### الطبقة 12 — الذاكرة والتخزين المؤقت"` | — |
| [SRC-E73001D9AC-L000233](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L233) | 233 | `"- فصل ذاكرة المحادثة المؤقتة عن بيانات المستخدم الدائمة وعن cache النتائج العامة."` | — |
| [SRC-E73001D9AC-L000234](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L234) | 234 | `"- تضمين tenant/user/session في مفاتيح التخزين المناسبة لمنع التسريب بين المستخدمين."` | — |
| [SRC-E73001D9AC-L000235](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L235) | 235 | `"- عدم وضع أسرار أو بيانات شخصية في cache مشترك بلا داعٍ."` | — |
| [SRC-E73001D9AC-L000236](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L236) | 236 | `"- تحديد TTL وسبب التخزين وشروط الإبطال وتغيّر المصدر."` | — |
| [SRC-E73001D9AC-L000237](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L237) | 237 | `"- لا تُخزن إجابات حساسة في cache عام."` | — |
| [SRC-E73001D9AC-L000238](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L238) | 238 | `"- لا تُستخدم ذاكرة قديمة للإجابة عن سؤال يتطلب وضعًا حديثًا."` | — |
| [SRC-E73001D9AC-L000239](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L239) | 239 | `"- عمليات الكتابة والترحيل لها مخطط واضح، وأقفال أو معاملات عند الحاجة، وخطة استعادة."` | — |
| [SRC-E73001D9AC-L000240](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L240) | 240 | `"- الالتزام بمبدأ تقليل البيانات وسياسة احتفاظ وحذف موثقة."` | — |
| [SRC-E73001D9AC-L000241](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L241) | 241 | `"- لا يُفترض أن SQLite أو أي مخزن محلي يناسب جميع مستويات التوسع؛ يُقاس الاستخدام أولًا ويُحدد حد التحول إلى تخزين مناسب عند الحاجة."` | — |
| [SRC-E73001D9AC-L000242](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L242) | 242 | `""` | — |
| [SRC-E73001D9AC-L000243](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L243) | 243 | `"### الطبقة 13 — الطوابير والعمال والمهام الطويلة"` | — |
| [SRC-E73001D9AC-L000244](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L244) | 244 | `"- تُستخدم عندما يكون طول المهمة أو الحمل أو قيود دورة الطلب تبررها؛ ليست شرطًا لكل سؤال."` | — |
| [SRC-E73001D9AC-L000245](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L245) | 245 | `"- طوابير محدودة الحجم مع سياسة رفض أو تأخير صريحة؛ لا طوابير غير محدودة."` | — |
| [SRC-E73001D9AC-L000246](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L246) | 246 | `"- حدود تزامن مستقلة للمزودات البطيئة أو المكلفة."` | — |
| [SRC-E73001D9AC-L000247](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L247) | 247 | `"- مفاتيح idempotency أو سجل حالة للعمليات التي لا يجوز تكرار آثارها."` | — |
| [SRC-E73001D9AC-L000248](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L248) | 248 | `"- فصل حالة المهمة عن اتصال المستخدم، بحيث لا يؤدي قطع المتصفح وحده إلى فساد الحالة."` | — |
| [SRC-E73001D9AC-L000249](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L249) | 249 | `"- استرداد المهام بعد إعادة تشغيل العامل، مع تجنب تنفيذ الأثر الخارجي مرتين."` | — |
| [SRC-E73001D9AC-L000250](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L250) | 250 | `"- تحديد مدة صلاحية الرسائل وعدد محاولات المعالجة والرسائل الميتة (dead-letter) عند استخدام وسيط يدعمها."` | — |
| [SRC-E73001D9AC-L000251](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L251) | 251 | `"- حماية نظام الطوابير نفسه بالمصادقة والحدود ومراقبة التراكم."` | — |
| [SRC-E73001D9AC-L000252](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L252) | 252 | `""` | — |
| [SRC-E73001D9AC-L000253](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L253) | 253 | `"### الطبقة 14 — المراقبة والتدقيق والاستجابة للحوادث"` | — |
| [SRC-E73001D9AC-L000254](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L254) | 254 | `"- قياس latency وthroughput وerror rate وtimeouts وqueue depth وprovider failures وresource use."` | — |
| [SRC-E73001D9AC-L000255](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L255) | 255 | `"- استخدام سجلات منظمة ومعرفات ارتباط عبر مراحل الطلب."` | — |
| [SRC-E73001D9AC-L000256](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L256) | 256 | `"- عدم تسجيل مفاتيح API أو رموز جلسات أو نصوص مستخدم حساسة افتراضيًا."` | — |
| [SRC-E73001D9AC-L000257](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L257) | 257 | `"- تنقيح السجلات قبل تخزينها؛ وتحديد صلاحية الوصول إليها ومدة احتفاظها."` | — |
| [SRC-E73001D9AC-L000258](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L258) | 258 | `"- فصل readiness عن liveness، وعدم جعل فشل مزود خارجي واحد يعني بالضرورة أن الخادم لا يمكنه تقديم أي استجابة."` | — |
| [SRC-E73001D9AC-L000259](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L259) | 259 | `"- وجود إجراءات استجابة للحوادث: تحديد النطاق، العزل، تدوير الأسرار، الاستعادة، مراجعة السبب الجذري، ومنع تكرار الحادث."` | — |
| [SRC-E73001D9AC-L000260](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L260) | 260 | `"- إجراء اختبارات استعادة النسخ الاحتياطية؛ وجود ملف نسخ احتياطي لا يثبت إمكانية استعادته."` | — |
| [SRC-E73001D9AC-L000261](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L261) | 261 | `"- الإشعارات والتنبيهات يجب أن تميز بين خطأ عابر وتدهور مستمر وحادث أمني."` | — |
| [SRC-E73001D9AC-L000262](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L262) | 262 | `""` | — |
| [SRC-E73001D9AC-L000263](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L263) | 263 | `"### الطبقة 15 — التكوين والأسرار وسلسلة التوريد"` | — |
| [SRC-E73001D9AC-L000264](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L264) | 264 | `"- إدارة البيئة والإعدادات بشكل منفصل عن كود التطبيق."` | — |
| [SRC-E73001D9AC-L000265](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L265) | 265 | `"- عدم حفظ مفاتيح أو رموز أو كلمات مرور في Git، أو السجلات، أو رسائل الخطأ، أو كود الواجهة."` | — |
| [SRC-E73001D9AC-L000266](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L266) | 266 | `"- منع تسريب ملف .env الحقيقي وأسرار الاختبار إلى المستودع العام."` | — |
| [SRC-E73001D9AC-L000267](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L267) | 267 | `"- توفير .env.example بقيم وهمية فقط."` | — |
| [SRC-E73001D9AC-L000268](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L268) | 268 | `"- تدوير الأسرار عند احتمال تسربها، وإلغاء الأسرار غير الضرورية."` | — |
| [SRC-E73001D9AC-L000269](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L269) | 269 | `"- تثبيت الاعتماديات وقيود إصداراتها ضمن سياسة قابلة للصيانة، ومراجعة التنبيهات الأمنية."` | — |
| [SRC-E73001D9AC-L000270](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L270) | 270 | `"- فحص الأسرار والاعتماديات والـ license ومصدر الحزم ضمن CI بقدر ما تسمح الأدوات المتاحة."` | — |
| [SRC-E73001D9AC-L000271](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L271) | 271 | `"- إنشاء SBOM عندما يكون ذلك عمليًا وملائمًا لطبيعة الإصدار."` | — |
| [SRC-E73001D9AC-L000272](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L272) | 272 | `"- قصر صلاحيات رموز CI على الحد اللازم، وحماية فروع الإصدار ومراجعاتها."` | — |
| [SRC-E73001D9AC-L000273](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L273) | 273 | `"- لا يُستخدم dependency أو action جديد لمجرد الحداثة؛ تُراجع موثوقيته وصلاحياته وضرورة إضافته."` | — |
| [SRC-E73001D9AC-L000274](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L274) | 274 | `""` | — |
| [SRC-E73001D9AC-L000275](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L275) | 275 | `"---"` | — |
| [SRC-E73001D9AC-L000276](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L276) | 276 | `""` | — |
| [SRC-E73001D9AC-L000277](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L277) | 277 | `"# الجزء الرابع — الأمن السيبراني ونموذج التهديدات"` | — |
| [SRC-E73001D9AC-L000278](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L278) | 278 | `""` | — |
| [SRC-E73001D9AC-L000279](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L279) | 279 | `"## 6. نموذج التهديد (Threat Model)"` | — |
| [SRC-E73001D9AC-L000280](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L280) | 280 | `""` | — |
| [SRC-E73001D9AC-L000281](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L281) | 281 | `"يجب تحديث نموذج التهديد عند تغيير مسار البيانات أو صلاحيات الأدوات أو واجهات التعرض العامة. يشمل المهاجمين المحتملين: مستخدمًا مسيئًا، وعميلًا آليًا، ومصدر محتوى خبيثًا، وموردًا خارجيًا معطلًا أو مخترقًا، ومستخدمًا يحاول الوصول إلى بيانات غيره، وخطأ إعداد أو اعتماديات معرضة للخطر."` | — |
| [SRC-E73001D9AC-L000282](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L282) | 282 | `""` | — |
| [SRC-E73001D9AC-L000283](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L283) | 283 | `"### 6.1 حماية الطلبات وواجهات API"` | — |
| [SRC-E73001D9AC-L000284](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L284) | 284 | `"- تحقق من الأنواع والأطوال والقيم المسموح بها والحقول غير المتوقعة."` | — |
| [SRC-E73001D9AC-L000285](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L285) | 285 | `"- تحديد حدود واضحة للجسم والعمق وعدد عناصر القوائم والسجل التاريخي."` | — |
| [SRC-E73001D9AC-L000286](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L286) | 286 | `"- استخدام استعلامات parameterized عندما توجد قاعدة SQL."` | — |
| [SRC-E73001D9AC-L000287](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L287) | 287 | `"- ترميز مخرجات العرض حسب السياق ومنع تفسير المحتوى غير الموثوق على أنه HTML أو JavaScript."` | — |
| [SRC-E73001D9AC-L000288](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L288) | 288 | `"- المصادقة والصلاحيات تطبّقان من جانب الخادم."` | — |
| [SRC-E73001D9AC-L000289](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L289) | 289 | `"- ضبط CORS على الأصول المطلوبة فقط، مع عدم اعتبار CORS نظام مصادقة."` | — |
| [SRC-E73001D9AC-L000290](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L290) | 290 | `"- وضع حد للطلبات المكلفة، وليس فقط عدد الطلبات العامة."` | — |
| [SRC-E73001D9AC-L000291](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L291) | 291 | `"- ألا تُكشف stack traces أو الأسرار أو إعدادات التشغيل أو المسارات الداخلية في الاستجابة العامة."` | — |
| [SRC-E73001D9AC-L000292](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L292) | 292 | `""` | — |
| [SRC-E73001D9AC-L000293](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L293) | 293 | `"### 6.2 حماية وكيل البحث من SSRF والوصول إلى الشبكة الداخلية"` | — |
| [SRC-E73001D9AC-L000294](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L294) | 294 | `"لأن Omarai قد يجلب روابط من الإنترنت، تعد هذه المنطقة عالية الخطورة:"` | — |
| [SRC-E73001D9AC-L000295](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L295) | 295 | `"- السماح ببروتوكولات HTTP وHTTPS فقط بحسب الحاجة."` | — |
| [SRC-E73001D9AC-L000296](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L296) | 296 | `"- رفض localhost والشبكات الخاصة والمحجوزة وعناوين link-local وعناوين metadata الحساسة، بما يشمل IPv4 وIPv6 وصيغ العناوين الممثلة أو الملتبسة."` | — |
| [SRC-E73001D9AC-L000297](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L297) | 297 | `"- حل DNS والتحقق من جميع العناوين الناتجة، ثم منع إعادة التوجيه إلى وجهة محظورة."` | — |
| [SRC-E73001D9AC-L000298](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L298) | 298 | `"- إعادة التحقق من كل عنوان وجهة في كل خطوة تحويل؛ لا يُوثق بالعنوان الأول وحده."` | — |
| [SRC-E73001D9AC-L000299](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L299) | 299 | `"- الحماية من DNS rebinding واختلاف نتيجة DNS بين التحقق والاتصال، واستخدام ضوابط شبكة خروج عند توفرها."` | — |
| [SRC-E73001D9AC-L000300](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L300) | 300 | `"- رفض userinfo الملتبس في URL، والمنافذ غير المطلوبة، والصيغ غير القياسية التي قد تتجاوز التحقق."` | — |
| [SRC-E73001D9AC-L000301](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L301) | 301 | `"- وضع سقف لحجم البيانات بعد فك الضغط، وعدد التحويلات، ووقت القراءة، وحجم النص المستخرج."` | — |
| [SRC-E73001D9AC-L000302](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L302) | 302 | `"- التحقق من نوع المحتوى والتعامل الآمن مع HTML وXML والملفات غير المتوقعة."` | — |
| [SRC-E73001D9AC-L000303](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L303) | 303 | `"- عدم السماح لجلب الصفحة بالوصول إلى ملفات محلية أو بروتوكولات داخلية."` | — |
| [SRC-E73001D9AC-L000304](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L304) | 304 | `"- اختبار المتجهات الأمنية باستخدام خادم محلي وهمي واختبارات مضبوطة؛ لا يُنفذ اختبار هجومي ضد طرف خارجي غير مصرح به."` | — |
