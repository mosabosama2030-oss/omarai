# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **018**
- سجلات الأسطر: **800**
- النطاق: SRC-E599346ABE-L000822 إلى SRC-E599346ABE-L001621
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## وثائق وفهرسة

### FILE-E599346ABE — [docs/generate_index.py](../generate_index.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-E599346ABE-L000822](../generate_index.py#L822) | 822 | `""` | — |
| [SRC-E599346ABE-L000823](../generate_index.py#L823) | 823 | `"    function_variable_locations: set[tuple[str, int]] = set()"` | — |
| [SRC-E599346ABE-L000824](../generate_index.py#L824) | 824 | `"    for pattern in (JS_ARROW_ASSIGNMENT_RE, JS_FUNCTION_ASSIGNMENT_RE):"` | — |
| [SRC-E599346ABE-L000825](../generate_index.py#L825) | 825 | `"        for match in pattern.finditer(source):"` | — |
| [SRC-E599346ABE-L000826](../generate_index.py#L826) | 826 | `"            line = _line_at(source, match.start(), base_line)"` | — |
| [SRC-E599346ABE-L000827](../generate_index.py#L827) | 827 | `"            name = match.group(1)"` | — |
| [SRC-E599346ABE-L000828](../generate_index.py#L828) | 828 | `"            function_variable_locations.add((name, line))"` | — |
| [SRC-E599346ABE-L000829](../generate_index.py#L829) | 829 | `"            _add_marker("` | — |
| [SRC-E599346ABE-L000830](../generate_index.py#L830) | 830 | `"                markers,"` | — |
| [SRC-E599346ABE-L000831](../generate_index.py#L831) | 831 | `"                seen,"` | — |
| [SRC-E599346ABE-L000832](../generate_index.py#L832) | 832 | `"                relative_file,"` | — |
| [SRC-E599346ABE-L000833](../generate_index.py#L833) | 833 | `"                name,"` | — |
| [SRC-E599346ABE-L000834](../generate_index.py#L834) | 834 | `"                \"دالة JavaScript/TypeScript\","` | — |
| [SRC-E599346ABE-L000835](../generate_index.py#L835) | 835 | `"                line,"` | — |
| [SRC-E599346ABE-L000836](../generate_index.py#L836) | 836 | `"            )"` | — |
| [SRC-E599346ABE-L000837](../generate_index.py#L837) | 837 | `""` | — |
| [SRC-E599346ABE-L000838](../generate_index.py#L838) | 838 | `"    for match in JS_VARIABLE_RE.finditer(source):"` | — |
| [SRC-E599346ABE-L000839](../generate_index.py#L839) | 839 | `"        line = _line_at(source, match.start(), base_line)"` | — |
| [SRC-E599346ABE-L000840](../generate_index.py#L840) | 840 | `"        name = match.group(1)"` | — |
| [SRC-E599346ABE-L000841](../generate_index.py#L841) | 841 | `"        if (name, line) in function_variable_locations:"` | — |
| [SRC-E599346ABE-L000842](../generate_index.py#L842) | 842 | `"            continue"` | — |
| [SRC-E599346ABE-L000843](../generate_index.py#L843) | 843 | `"        _add_marker("` | — |
| [SRC-E599346ABE-L000844](../generate_index.py#L844) | 844 | `"            markers,"` | — |
| [SRC-E599346ABE-L000845](../generate_index.py#L845) | 845 | `"            seen,"` | — |
| [SRC-E599346ABE-L000846](../generate_index.py#L846) | 846 | `"            relative_file,"` | — |
| [SRC-E599346ABE-L000847](../generate_index.py#L847) | 847 | `"            name,"` | — |
| [SRC-E599346ABE-L000848](../generate_index.py#L848) | 848 | `"            \"متغير JavaScript/TypeScript\","` | — |
| [SRC-E599346ABE-L000849](../generate_index.py#L849) | 849 | `"            line,"` | — |
| [SRC-E599346ABE-L000850](../generate_index.py#L850) | 850 | `"        )"` | — |
| [SRC-E599346ABE-L000851](../generate_index.py#L851) | 851 | `""` | — |
| [SRC-E599346ABE-L000852](../generate_index.py#L852) | 852 | `""` | — |
| [SRC-E599346ABE-L000853](../generate_index.py#L853) | 853 | `"def _scan_css("` | — |
| [SRC-E599346ABE-L000854](../generate_index.py#L854) | 854 | `"    source: str,"` | — |
| [SRC-E599346ABE-L000855](../generate_index.py#L855) | 855 | `"    relative_file: str,"` | — |
| [SRC-E599346ABE-L000856](../generate_index.py#L856) | 856 | `"    markers: list[IndexedMarker],"` | — |
| [SRC-E599346ABE-L000857](../generate_index.py#L857) | 857 | `"    seen: set[tuple[str, str, str]],"` | — |
| [SRC-E599346ABE-L000858](../generate_index.py#L858) | 858 | `"    base_line: int = 1,"` | — |
| [SRC-E599346ABE-L000859](../generate_index.py#L859) | 859 | `") -> None:"` | — |
| [SRC-E599346ABE-L000860](../generate_index.py#L860) | 860 | `"    \"\"\"Extract CSS class/id selectors and custom properties; this is not a full CSS parser.\"\"\""` | — |
| [SRC-E599346ABE-L000861](../generate_index.py#L861) | 861 | `"    cleaned = CSS_COMMENT_RE.sub("` | — |
| [SRC-E599346ABE-L000862](../generate_index.py#L862) | 862 | `"        lambda match: \"\".join(\"\\n\" if char == \"\\n\" else \" \" for char in match.group(0)),"` | — |
| [SRC-E599346ABE-L000863](../generate_index.py#L863) | 863 | `"        source,"` | — |
| [SRC-E599346ABE-L000864](../generate_index.py#L864) | 864 | `"    )"` | — |
| [SRC-E599346ABE-L000865](../generate_index.py#L865) | 865 | `"    patterns = ("` | — |
| [SRC-E599346ABE-L000866](../generate_index.py#L866) | 866 | `"        (CSS_CUSTOM_PROPERTY_RE, \"متغير CSS مخصص\"),"` | — |
| [SRC-E599346ABE-L000867](../generate_index.py#L867) | 867 | `"        (CSS_CLASS_RE, \"محدد class في CSS\"),"` | — |
| [SRC-E599346ABE-L000868](../generate_index.py#L868) | 868 | `"        (CSS_ID_RE, \"محدد id في CSS\"),"` | — |
| [SRC-E599346ABE-L000869](../generate_index.py#L869) | 869 | `"    )"` | — |
| [SRC-E599346ABE-L000870](../generate_index.py#L870) | 870 | `"    for pattern, kind in patterns:"` | — |
| [SRC-E599346ABE-L000871](../generate_index.py#L871) | 871 | `"        for match in pattern.finditer(cleaned):"` | — |
| [SRC-E599346ABE-L000872](../generate_index.py#L872) | 872 | `"            _add_marker("` | — |
| [SRC-E599346ABE-L000873](../generate_index.py#L873) | 873 | `"                markers,"` | — |
| [SRC-E599346ABE-L000874](../generate_index.py#L874) | 874 | `"                seen,"` | — |
| [SRC-E599346ABE-L000875](../generate_index.py#L875) | 875 | `"                relative_file,"` | — |
| [SRC-E599346ABE-L000876](../generate_index.py#L876) | 876 | `"                match.group(1),"` | — |
| [SRC-E599346ABE-L000877](../generate_index.py#L877) | 877 | `"                kind,"` | — |
| [SRC-E599346ABE-L000878](../generate_index.py#L878) | 878 | `"                _line_at(cleaned, match.start(), base_line),"` | — |
| [SRC-E599346ABE-L000879](../generate_index.py#L879) | 879 | `"            )"` | — |
| [SRC-E599346ABE-L000880](../generate_index.py#L880) | 880 | `""` | — |
| [SRC-E599346ABE-L000881](../generate_index.py#L881) | 881 | `""` | — |
| [SRC-E599346ABE-L000882](../generate_index.py#L882) | 882 | `"def _scan_html("` | — |
| [SRC-E599346ABE-L000883](../generate_index.py#L883) | 883 | `"    source: str,"` | — |
| [SRC-E599346ABE-L000884](../generate_index.py#L884) | 884 | `"    relative_file: str,"` | — |
| [SRC-E599346ABE-L000885](../generate_index.py#L885) | 885 | `"    markers: list[IndexedMarker],"` | — |
| [SRC-E599346ABE-L000886](../generate_index.py#L886) | 886 | `"    seen: set[tuple[str, str, str]],"` | — |
| [SRC-E599346ABE-L000887](../generate_index.py#L887) | 887 | `") -> None:"` | — |
| [SRC-E599346ABE-L000888](../generate_index.py#L888) | 888 | `"    \"\"\"Extract HTML navigation attributes plus embedded JS and CSS declarations.\"\"\""` | — |
| [SRC-E599346ABE-L000889](../generate_index.py#L889) | 889 | `"    for match in HTML_ATTRIBUTE_RE.finditer(source):"` | — |
| [SRC-E599346ABE-L000890](../generate_index.py#L890) | 890 | `"        attribute = match.group(1).lower()"` | — |
| [SRC-E599346ABE-L000891](../generate_index.py#L891) | 891 | `"        raw_value = match.group(3).strip()"` | — |
| [SRC-E599346ABE-L000892](../generate_index.py#L892) | 892 | `"        for value in raw_value.split() if attribute == \"data-testid\" else [raw_value]:"` | — |
| [SRC-E599346ABE-L000893](../generate_index.py#L893) | 893 | `"            _add_marker("` | — |
| [SRC-E599346ABE-L000894](../generate_index.py#L894) | 894 | `"                markers,"` | — |
| [SRC-E599346ABE-L000895](../generate_index.py#L895) | 895 | `"                seen,"` | — |
| [SRC-E599346ABE-L000896](../generate_index.py#L896) | 896 | `"                relative_file,"` | — |
| [SRC-E599346ABE-L000897](../generate_index.py#L897) | 897 | `"                value,"` | — |
| [SRC-E599346ABE-L000898](../generate_index.py#L898) | 898 | `"                f\"قيمة سمة HTML ({attribute})\","` | — |
| [SRC-E599346ABE-L000899](../generate_index.py#L899) | 899 | `"                _line_at(source, match.start()),"` | — |
| [SRC-E599346ABE-L000900](../generate_index.py#L900) | 900 | `"            )"` | — |
| [SRC-E599346ABE-L000901](../generate_index.py#L901) | 901 | `""` | — |
| [SRC-E599346ABE-L000902](../generate_index.py#L902) | 902 | `"    for match in HTML_SCRIPT_RE.finditer(source):"` | — |
| [SRC-E599346ABE-L000903](../generate_index.py#L903) | 903 | `"        script = match.group(1)"` | — |
| [SRC-E599346ABE-L000904](../generate_index.py#L904) | 904 | `"        base_line = _line_at(source, match.start(1))"` | — |
| [SRC-E599346ABE-L000905](../generate_index.py#L905) | 905 | `"        _scan_javascript(script, relative_file, markers, seen, base_line)"` | — |
| [SRC-E599346ABE-L000906](../generate_index.py#L906) | 906 | `"    for match in HTML_STYLE_RE.finditer(source):"` | — |
| [SRC-E599346ABE-L000907](../generate_index.py#L907) | 907 | `"        style = match.group(1)"` | — |
| [SRC-E599346ABE-L000908](../generate_index.py#L908) | 908 | `"        base_line = _line_at(source, match.start(1))"` | — |
| [SRC-E599346ABE-L000909](../generate_index.py#L909) | 909 | `"        _scan_css(style, relative_file, markers, seen, base_line)"` | — |
| [SRC-E599346ABE-L000910](../generate_index.py#L910) | 910 | `""` | — |
| [SRC-E599346ABE-L000911](../generate_index.py#L911) | 911 | `""` | — |
| [SRC-E599346ABE-L000912](../generate_index.py#L912) | 912 | `"def _scan_config_keys("` | — |
| [SRC-E599346ABE-L000913](../generate_index.py#L913) | 913 | `"    source: str,"` | — |
| [SRC-E599346ABE-L000914](../generate_index.py#L914) | 914 | `"    suffix: str,"` | — |
| [SRC-E599346ABE-L000915](../generate_index.py#L915) | 915 | `"    relative_file: str,"` | — |
| [SRC-E599346ABE-L000916](../generate_index.py#L916) | 916 | `"    markers: list[IndexedMarker],"` | — |
| [SRC-E599346ABE-L000917](../generate_index.py#L917) | 917 | `"    seen: set[tuple[str, str, str]],"` | — |
| [SRC-E599346ABE-L000918](../generate_index.py#L918) | 918 | `") -> None:"` | — |
| [SRC-E599346ABE-L000919](../generate_index.py#L919) | 919 | `"    \"\"\"Extract configuration keys/sections without evaluating or loading configuration.\"\"\""` | — |
| [SRC-E599346ABE-L000920](../generate_index.py#L920) | 920 | `"    if suffix in {\".yml\", \".yaml\"}:"` | — |
| [SRC-E599346ABE-L000921](../generate_index.py#L921) | 921 | `"        patterns = ((YAML_KEY_RE, \"مفتاح إعداد YAML\"),)"` | — |
| [SRC-E599346ABE-L000922](../generate_index.py#L922) | 922 | `"    elif suffix == \".toml\":"` | — |
| [SRC-E599346ABE-L000923](../generate_index.py#L923) | 923 | `"        patterns = ("` | — |
| [SRC-E599346ABE-L000924](../generate_index.py#L924) | 924 | `"            (TOML_SECTION_RE, \"قسم TOML\"),"` | — |
| [SRC-E599346ABE-L000925](../generate_index.py#L925) | 925 | `"            (TOML_KEY_RE, \"مفتاح إعداد TOML\"),"` | — |
| [SRC-E599346ABE-L000926](../generate_index.py#L926) | 926 | `"        )"` | — |
| [SRC-E599346ABE-L000927](../generate_index.py#L927) | 927 | `"    elif suffix == \".json\":"` | — |
| [SRC-E599346ABE-L000928](../generate_index.py#L928) | 928 | `"        patterns = ((JSON_KEY_RE, \"مفتاح JSON\"),)"` | — |
| [SRC-E599346ABE-L000929](../generate_index.py#L929) | 929 | `"    elif suffix in {\".ini\", \".cfg\"}:"` | — |
| [SRC-E599346ABE-L000930](../generate_index.py#L930) | 930 | `"        patterns = ("` | — |
| [SRC-E599346ABE-L000931](../generate_index.py#L931) | 931 | `"            (INI_SECTION_RE, \"قسم إعداد\"),"` | — |
| [SRC-E599346ABE-L000932](../generate_index.py#L932) | 932 | `"            (INI_KEY_RE, \"مفتاح إعداد\"),"` | — |
| [SRC-E599346ABE-L000933](../generate_index.py#L933) | 933 | `"        )"` | — |
| [SRC-E599346ABE-L000934](../generate_index.py#L934) | 934 | `"    else:"` | — |
| [SRC-E599346ABE-L000935](../generate_index.py#L935) | 935 | `"        patterns = ()"` | — |
| [SRC-E599346ABE-L000936](../generate_index.py#L936) | 936 | `"    for pattern, kind in patterns:"` | — |
| [SRC-E599346ABE-L000937](../generate_index.py#L937) | 937 | `"        for match in pattern.finditer(source):"` | — |
| [SRC-E599346ABE-L000938](../generate_index.py#L938) | 938 | `"            _add_marker("` | — |
| [SRC-E599346ABE-L000939](../generate_index.py#L939) | 939 | `"                markers,"` | — |
| [SRC-E599346ABE-L000940](../generate_index.py#L940) | 940 | `"                seen,"` | — |
| [SRC-E599346ABE-L000941](../generate_index.py#L941) | 941 | `"                relative_file,"` | — |
| [SRC-E599346ABE-L000942](../generate_index.py#L942) | 942 | `"                match.group(1),"` | — |
| [SRC-E599346ABE-L000943](../generate_index.py#L943) | 943 | `"                kind,"` | — |
| [SRC-E599346ABE-L000944](../generate_index.py#L944) | 944 | `"                _line_at(source, match.start()),"` | — |
| [SRC-E599346ABE-L000945](../generate_index.py#L945) | 945 | `"            )"` | — |
| [SRC-E599346ABE-L000946](../generate_index.py#L946) | 946 | `""` | — |
| [SRC-E599346ABE-L000947](../generate_index.py#L947) | 947 | `""` | — |
| [SRC-E599346ABE-L000948](../generate_index.py#L948) | 948 | `"def scan_static_symbols(root: Path, inventory: list[IndexedFile]) -> list[IndexedMarker]:"` | — |
| [SRC-E599346ABE-L000949](../generate_index.py#L949) | 949 | `"    \"\"\"Extract supplementary navigational symbols from frontend, docs, config and scripts.\"\"\""` | — |
| [SRC-E599346ABE-L000950](../generate_index.py#L950) | 950 | `"    markers: list[IndexedMarker] = []"` | — |
| [SRC-E599346ABE-L000951](../generate_index.py#L951) | 951 | `"    seen: set[tuple[str, str, str]] = set()"` | — |
| [SRC-E599346ABE-L000952](../generate_index.py#L952) | 952 | `"    for indexed_file in inventory:"` | — |
| [SRC-E599346ABE-L000953](../generate_index.py#L953) | 953 | `"        path = root / indexed_file.file"` | — |
| [SRC-E599346ABE-L000954](../generate_index.py#L954) | 954 | `"        suffix = path.suffix.lower()"` | — |
| [SRC-E599346ABE-L000955](../generate_index.py#L955) | 955 | `"        file_name = path.name.lower()"` | — |
| [SRC-E599346ABE-L000956](../generate_index.py#L956) | 956 | `"        is_example_env = file_name == \".env.example\""` | — |
| [SRC-E599346ABE-L000957](../generate_index.py#L957) | 957 | `"        if suffix not in TEXT_SCAN_EXTENSIONS and not is_example_env and file_name not in {"` | — |
| [SRC-E599346ABE-L000958](../generate_index.py#L958) | 958 | `"            \"dockerfile\","` | — |
| [SRC-E599346ABE-L000959](../generate_index.py#L959) | 959 | `"            \"makefile\","` | — |
| [SRC-E599346ABE-L000960](../generate_index.py#L960) | 960 | `"            \"procfile\","` | — |
| [SRC-E599346ABE-L000961](../generate_index.py#L961) | 961 | `"        }:"` | — |
| [SRC-E599346ABE-L000962](../generate_index.py#L962) | 962 | `"            continue"` | — |
| [SRC-E599346ABE-L000963](../generate_index.py#L963) | 963 | `""` | — |
| [SRC-E599346ABE-L000964](../generate_index.py#L964) | 964 | `"        source = _read_text_bounded(path)"` | — |
| [SRC-E599346ABE-L000965](../generate_index.py#L965) | 965 | `"        if source is None:"` | — |
| [SRC-E599346ABE-L000966](../generate_index.py#L966) | 966 | `"            continue"` | — |
| [SRC-E599346ABE-L000967](../generate_index.py#L967) | 967 | `""` | — |
| [SRC-E599346ABE-L000968](../generate_index.py#L968) | 968 | `"        if suffix in JAVASCRIPT_EXTENSIONS:"` | — |
| [SRC-E599346ABE-L000969](../generate_index.py#L969) | 969 | `"            _scan_javascript(source, indexed_file.file, markers, seen)"` | — |
| [SRC-E599346ABE-L000970](../generate_index.py#L970) | 970 | `"        elif suffix in CSS_EXTENSIONS:"` | — |
| [SRC-E599346ABE-L000971](../generate_index.py#L971) | 971 | `"            _scan_css(source, indexed_file.file, markers, seen)"` | — |
| [SRC-E599346ABE-L000972](../generate_index.py#L972) | 972 | `"        elif suffix in {\".html\", \".htm\"}:"` | — |
| [SRC-E599346ABE-L000973](../generate_index.py#L973) | 973 | `"            _scan_html(source, indexed_file.file, markers, seen)"` | — |
| [SRC-E599346ABE-L000974](../generate_index.py#L974) | 974 | `"        elif suffix == \".md\":"` | — |
| [SRC-E599346ABE-L000975](../generate_index.py#L975) | 975 | `"            for match in MARKDOWN_HEADING_RE.finditer(source):"` | — |
| [SRC-E599346ABE-L000976](../generate_index.py#L976) | 976 | `"                heading = match.group(2).strip()"` | — |
| [SRC-E599346ABE-L000977](../generate_index.py#L977) | 977 | `"                _add_marker("` | — |
| [SRC-E599346ABE-L000978](../generate_index.py#L978) | 978 | `"                    markers,"` | — |
| [SRC-E599346ABE-L000979](../generate_index.py#L979) | 979 | `"                    seen,"` | — |
| [SRC-E599346ABE-L000980](../generate_index.py#L980) | 980 | `"                    indexed_file.file,"` | — |
| [SRC-E599346ABE-L000981](../generate_index.py#L981) | 981 | `"                    heading,"` | — |
| [SRC-E599346ABE-L000982](../generate_index.py#L982) | 982 | `"                    f\"عنوان Markdown (H{len(match.group(1))})\","` | — |
| [SRC-E599346ABE-L000983](../generate_index.py#L983) | 983 | `"                    _line_at(source, match.start()),"` | — |
| [SRC-E599346ABE-L000984](../generate_index.py#L984) | 984 | `"                )"` | — |
| [SRC-E599346ABE-L000985](../generate_index.py#L985) | 985 | `"        elif suffix == \".sh\":"` | — |
| [SRC-E599346ABE-L000986](../generate_index.py#L986) | 986 | `"            for match in SHELL_FUNCTION_RE.finditer(source):"` | — |
| [SRC-E599346ABE-L000987](../generate_index.py#L987) | 987 | `"                _add_marker("` | — |
| [SRC-E599346ABE-L000988](../generate_index.py#L988) | 988 | `"                    markers,"` | — |
| [SRC-E599346ABE-L000989](../generate_index.py#L989) | 989 | `"                    seen,"` | — |
| [SRC-E599346ABE-L000990](../generate_index.py#L990) | 990 | `"                    indexed_file.file,"` | — |
| [SRC-E599346ABE-L000991](../generate_index.py#L991) | 991 | `"                    match.group(1),"` | — |
| [SRC-E599346ABE-L000992](../generate_index.py#L992) | 992 | `"                    \"دالة Shell\","` | — |
| [SRC-E599346ABE-L000993](../generate_index.py#L993) | 993 | `"                    _line_at(source, match.start()),"` | — |
| [SRC-E599346ABE-L000994](../generate_index.py#L994) | 994 | `"                )"` | — |
| [SRC-E599346ABE-L000995](../generate_index.py#L995) | 995 | `"        elif suffix in CONFIG_EXTENSIONS:"` | — |
| [SRC-E599346ABE-L000996](../generate_index.py#L996) | 996 | `"            _scan_config_keys(source, suffix, indexed_file.file, markers, seen)"` | — |
| [SRC-E599346ABE-L000997](../generate_index.py#L997) | 997 | `""` | — |
| [SRC-E599346ABE-L000998](../generate_index.py#L998) | 998 | `"        if suffix in TEXT_SCAN_EXTENSIONS or is_example_env or file_name in {"` | — |
| [SRC-E599346ABE-L000999](../generate_index.py#L999) | 999 | `"            \"dockerfile\","` | — |
| [SRC-E599346ABE-L001000](../generate_index.py#L1000) | 1000 | `"            \"makefile\","` | — |
| [SRC-E599346ABE-L001001](../generate_index.py#L1001) | 1001 | `"            \"procfile\","` | — |
| [SRC-E599346ABE-L001002](../generate_index.py#L1002) | 1002 | `"        }:"` | — |
| [SRC-E599346ABE-L001003](../generate_index.py#L1003) | 1003 | `"            for match in UPPER_SNAKE_RE.finditer(source):"` | — |
| [SRC-E599346ABE-L001004](../generate_index.py#L1004) | 1004 | `"                _add_marker("` | — |
| [SRC-E599346ABE-L001005](../generate_index.py#L1005) | 1005 | `"                    markers,"` | — |
| [SRC-E599346ABE-L001006](../generate_index.py#L1006) | 1006 | `"                    seen,"` | — |
| [SRC-E599346ABE-L001007](../generate_index.py#L1007) | 1007 | `"                    indexed_file.file,"` | — |
| [SRC-E599346ABE-L001008](../generate_index.py#L1008) | 1008 | `"                    match.group(0),"` | — |
| [SRC-E599346ABE-L001009](../generate_index.py#L1009) | 1009 | `"                    \"اسم ثابت/إعداد بصيغة UPPER_SNAKE_CASE\","` | — |
| [SRC-E599346ABE-L001010](../generate_index.py#L1010) | 1010 | `"                    _line_at(source, match.start()),"` | — |
| [SRC-E599346ABE-L001011](../generate_index.py#L1011) | 1011 | `"                )"` | — |
| [SRC-E599346ABE-L001012](../generate_index.py#L1012) | 1012 | `""` | — |
| [SRC-E599346ABE-L001013](../generate_index.py#L1013) | 1013 | `"        if suffix in PYTHON_EXTENSIONS \| JAVASCRIPT_EXTENSIONS \| {\".html\", \".htm\"}:"` | — |
| [SRC-E599346ABE-L001014](../generate_index.py#L1014) | 1014 | `"            for match in API_PATH_RE.finditer(source):"` | — |
| [SRC-E599346ABE-L001015](../generate_index.py#L1015) | 1015 | `"                _add_marker("` | — |
| [SRC-E599346ABE-L001016](../generate_index.py#L1016) | 1016 | `"                    markers,"` | — |
| [SRC-E599346ABE-L001017](../generate_index.py#L1017) | 1017 | `"                    seen,"` | — |
| [SRC-E599346ABE-L001018](../generate_index.py#L1018) | 1018 | `"                    indexed_file.file,"` | — |
| [SRC-E599346ABE-L001019](../generate_index.py#L1019) | 1019 | `"                    match.group(1),"` | — |
| [SRC-E599346ABE-L001020](../generate_index.py#L1020) | 1020 | `"                    \"مسار API/واجهة محتمل\","` | — |
| [SRC-E599346ABE-L001021](../generate_index.py#L1021) | 1021 | `"                    _line_at(source, match.start()),"` | — |
| [SRC-E599346ABE-L001022](../generate_index.py#L1022) | 1022 | `"                )"` | — |
| [SRC-E599346ABE-L001023](../generate_index.py#L1023) | 1023 | `""` | — |
| [SRC-E599346ABE-L001024](../generate_index.py#L1024) | 1024 | `"    markers.sort("` | — |
| [SRC-E599346ABE-L001025](../generate_index.py#L1025) | 1025 | `"        key=lambda marker: ("` | — |
| [SRC-E599346ABE-L001026](../generate_index.py#L1026) | 1026 | `"            marker.file.casefold(),"` | — |
| [SRC-E599346ABE-L001027](../generate_index.py#L1027) | 1027 | `"            marker.line,"` | — |
| [SRC-E599346ABE-L001028](../generate_index.py#L1028) | 1028 | `"            marker.kind.casefold(),"` | — |
| [SRC-E599346ABE-L001029](../generate_index.py#L1029) | 1029 | `"            marker.name.casefold(),"` | — |
| [SRC-E599346ABE-L001030](../generate_index.py#L1030) | 1030 | `"        )"` | — |
| [SRC-E599346ABE-L001031](../generate_index.py#L1031) | 1031 | `"    )"` | — |
| [SRC-E599346ABE-L001032](../generate_index.py#L1032) | 1032 | `"    return markers"` | — |
| [SRC-E599346ABE-L001033](../generate_index.py#L1033) | 1033 | `""` | — |
| [SRC-E599346ABE-L001034](../generate_index.py#L1034) | 1034 | `""` | — |
| [SRC-E599346ABE-L001035](../generate_index.py#L1035) | 1035 | `"def _source_file_href("` | — |
| [SRC-E599346ABE-L001036](../generate_index.py#L1036) | 1036 | `"    relative_file: str,"` | — |
| [SRC-E599346ABE-L001037](../generate_index.py#L1037) | 1037 | `"    line: int = 1,"` | — |
| [SRC-E599346ABE-L001038](../generate_index.py#L1038) | 1038 | `"    index_directory: str = \"docs\","` | — |
| [SRC-E599346ABE-L001039](../generate_index.py#L1039) | 1039 | `") -> str:"` | — |
| [SRC-E599346ABE-L001040](../generate_index.py#L1040) | 1040 | `"    \"\"\"Return a relative source link from a generated index page to the original file.\"\"\""` | — |
| [SRC-E599346ABE-L001041](../generate_index.py#L1041) | 1041 | `"    normalized = relative_file.replace(\"\\\\\", \"/\")"` | — |
| [SRC-E599346ABE-L001042](../generate_index.py#L1042) | 1042 | `"    target = posixpath.relpath(normalized, index_directory)"` | — |
| [SRC-E599346ABE-L001043](../generate_index.py#L1043) | 1043 | `"    return f\"{quote(target, safe='/._-')}#L{max(line, 1)}\""` | — |
| [SRC-E599346ABE-L001044](../generate_index.py#L1044) | 1044 | `""` | — |
| [SRC-E599346ABE-L001045](../generate_index.py#L1045) | 1045 | `""` | — |
| [SRC-E599346ABE-L001046](../generate_index.py#L1046) | 1046 | `"def _source_line_id(relative_file: str, line: int) -> str:"` | — |
| [SRC-E599346ABE-L001047](../generate_index.py#L1047) | 1047 | `"    \"\"\"Return a consistent line code wherever a symbol, finding, or source line is shown.\"\"\""` | — |
| [SRC-E599346ABE-L001048](../generate_index.py#L1048) | 1048 | `"    file_hash = _stable_file_id(relative_file).removeprefix(\"FILE-\")"` | — |
| [SRC-E599346ABE-L001049](../generate_index.py#L1049) | 1049 | `"    return f\"SRC-{file_hash}-L{line:06d}\""` | — |
| [SRC-E599346ABE-L001050](../generate_index.py#L1050) | 1050 | `""` | — |
| [SRC-E599346ABE-L001051](../generate_index.py#L1051) | 1051 | `""` | — |
| [SRC-E599346ABE-L001052](../generate_index.py#L1052) | 1052 | `"def _markdown_cell(value: str) -> str:"` | — |
| [SRC-E599346ABE-L001053](../generate_index.py#L1053) | 1053 | `"    \"\"\"Normalize text and escape Markdown table delimiters.\"\"\""` | — |
| [SRC-E599346ABE-L001054](../generate_index.py#L1054) | 1054 | `"    return \" \".join(value.replace(\"\\r\", \" \").replace(\"\\n\", \" \").split()).replace("` | — |
| [SRC-E599346ABE-L001055](../generate_index.py#L1055) | 1055 | `"        \"\|\", r\"\\\|\""` | — |
| [SRC-E599346ABE-L001056](../generate_index.py#L1056) | 1056 | `"    )"` | — |
| [SRC-E599346ABE-L001057](../generate_index.py#L1057) | 1057 | `""` | — |
| [SRC-E599346ABE-L001058](../generate_index.py#L1058) | 1058 | `""` | — |
| [SRC-E599346ABE-L001059](../generate_index.py#L1059) | 1059 | `"def scan_source_lines(root: Path, inventory: list[IndexedFile]) -> list[IndexedLine]:"` | — |
| [SRC-E599346ABE-L001060](../generate_index.py#L1060) | 1060 | `"    \"\"\"Index every logical line of each eligible text file readable within the size bound.\"\"\""` | — |
| [SRC-E599346ABE-L001061](../generate_index.py#L1061) | 1061 | `"    indexed_lines: list[IndexedLine] = []"` | — |
| [SRC-E599346ABE-L001062](../generate_index.py#L1062) | 1062 | `"    for item in inventory:"` | — |
| [SRC-E599346ABE-L001063](../generate_index.py#L1063) | 1063 | `"        source = _read_text_bounded(root / item.file)"` | — |
| [SRC-E599346ABE-L001064](../generate_index.py#L1064) | 1064 | `"        if source is None:"` | — |
| [SRC-E599346ABE-L001065](../generate_index.py#L1065) | 1065 | `"            continue"` | — |
| [SRC-E599346ABE-L001066](../generate_index.py#L1066) | 1066 | `"        for line_number, content in enumerate(source.splitlines(), start=1):"` | — |
| [SRC-E599346ABE-L001067](../generate_index.py#L1067) | 1067 | `"            indexed_lines.append("` | — |
| [SRC-E599346ABE-L001068](../generate_index.py#L1068) | 1068 | `"                IndexedLine("` | — |
| [SRC-E599346ABE-L001069](../generate_index.py#L1069) | 1069 | `"                    file=item.file,"` | — |
| [SRC-E599346ABE-L001070](../generate_index.py#L1070) | 1070 | `"                    file_id=item.file_id,"` | — |
| [SRC-E599346ABE-L001071](../generate_index.py#L1071) | 1071 | `"                    line_id=_source_line_id(item.file, line_number),"` | — |
| [SRC-E599346ABE-L001072](../generate_index.py#L1072) | 1072 | `"                    category=item.category,"` | — |
| [SRC-E599346ABE-L001073](../generate_index.py#L1073) | 1073 | `"                    line=line_number,"` | — |
| [SRC-E599346ABE-L001074](../generate_index.py#L1074) | 1074 | `"                    content=content,"` | — |
| [SRC-E599346ABE-L001075](../generate_index.py#L1075) | 1075 | `"                )"` | — |
| [SRC-E599346ABE-L001076](../generate_index.py#L1076) | 1076 | `"            )"` | — |
| [SRC-E599346ABE-L001077](../generate_index.py#L1077) | 1077 | `"    indexed_lines.sort(key=lambda item: (item.file.casefold(), item.line))"` | — |
| [SRC-E599346ABE-L001078](../generate_index.py#L1078) | 1078 | `"    return indexed_lines"` | — |
| [SRC-E599346ABE-L001079](../generate_index.py#L1079) | 1079 | `""` | — |
| [SRC-E599346ABE-L001080](../generate_index.py#L1080) | 1080 | `""` | — |
| [SRC-E599346ABE-L001081](../generate_index.py#L1081) | 1081 | `"def _append_comment_text("` | — |
| [SRC-E599346ABE-L001082](../generate_index.py#L1082) | 1082 | `"    comments: dict[int, list[str]],"` | — |
| [SRC-E599346ABE-L001083](../generate_index.py#L1083) | 1083 | `"    starting_line: int,"` | — |
| [SRC-E599346ABE-L001084](../generate_index.py#L1084) | 1084 | `"    text: str,"` | — |
| [SRC-E599346ABE-L001085](../generate_index.py#L1085) | 1085 | `") -> None:"` | — |
| [SRC-E599346ABE-L001086](../generate_index.py#L1086) | 1086 | `"    \"\"\"Map comment text fragments onto original 1-based source lines.\"\"\""` | — |
| [SRC-E599346ABE-L001087](../generate_index.py#L1087) | 1087 | `"    for offset, line_text in enumerate(text.splitlines() or [text]):"` | — |
| [SRC-E599346ABE-L001088](../generate_index.py#L1088) | 1088 | `"        comments.setdefault(starting_line + offset, []).append(line_text)"` | — |
| [SRC-E599346ABE-L001089](../generate_index.py#L1089) | 1089 | `""` | — |
| [SRC-E599346ABE-L001090](../generate_index.py#L1090) | 1090 | `""` | — |
| [SRC-E599346ABE-L001091](../generate_index.py#L1091) | 1091 | `"def _python_comment_map(source: str) -> dict[int, list[str]]:"` | — |
| [SRC-E599346ABE-L001092](../generate_index.py#L1092) | 1092 | `"    \"\"\"Return real Python comment tokens, excluding strings and docstrings.\"\"\""` | — |
| [SRC-E599346ABE-L001093](../generate_index.py#L1093) | 1093 | `"    comments: dict[int, list[str]] = {}"` | — |
| [SRC-E599346ABE-L001094](../generate_index.py#L1094) | 1094 | `"    try:"` | — |
| [SRC-E599346ABE-L001095](../generate_index.py#L1095) | 1095 | `"        for token in tokenize.generate_tokens(StringIO(source).readline):"` | — |
| [SRC-E599346ABE-L001096](../generate_index.py#L1096) | 1096 | `"            if token.type == tokenize.COMMENT:"` | — |
| [SRC-E599346ABE-L001097](../generate_index.py#L1097) | 1097 | `"                _append_comment_text(comments, token.start[0], token.string[1:])"` | — |
| [SRC-E599346ABE-L001098](../generate_index.py#L1098) | 1098 | `"    except (tokenize.TokenError, IndentationError, SyntaxError, StopIteration):"` | — |
| [SRC-E599346ABE-L001099](../generate_index.py#L1099) | 1099 | `"        return comments"` | — |
| [SRC-E599346ABE-L001100](../generate_index.py#L1100) | 1100 | `"    return comments"` | — |
| [SRC-E599346ABE-L001101](../generate_index.py#L1101) | 1101 | `""` | — |
| [SRC-E599346ABE-L001102](../generate_index.py#L1102) | 1102 | `""` | — |
| [SRC-E599346ABE-L001103](../generate_index.py#L1103) | 1103 | `"def _c_style_comment_map(source: str, *, hash_comments: bool = False) -> dict[int, list[str]]:"` | — |
| [SRC-E599346ABE-L001104](../generate_index.py#L1104) | 1104 | `"    \"\"\"Extract C-style or hash comments while skipping quoted strings.\"\"\""` | — |
| [SRC-E599346ABE-L001105](../generate_index.py#L1105) | 1105 | `"    comments: dict[int, list[str]] = {}"` | — |
| [SRC-E599346ABE-L001106](../generate_index.py#L1106) | 1106 | `"    lines = source.splitlines(keepends=True)"` | — |
| [SRC-E599346ABE-L001107](../generate_index.py#L1107) | 1107 | `"    if not lines and source:"` | — |
| [SRC-E599346ABE-L001108](../generate_index.py#L1108) | 1108 | `"        lines = [source]"` | — |
| [SRC-E599346ABE-L001109](../generate_index.py#L1109) | 1109 | `"    quote: str \| None = None"` | — |
| [SRC-E599346ABE-L001110](../generate_index.py#L1110) | 1110 | `"    in_block = False"` | — |
| [SRC-E599346ABE-L001111](../generate_index.py#L1111) | 1111 | `""` | — |
| [SRC-E599346ABE-L001112](../generate_index.py#L1112) | 1112 | `"    for line_number, line in enumerate(lines, start=1):"` | — |
| [SRC-E599346ABE-L001113](../generate_index.py#L1113) | 1113 | `"        i = 0"` | — |
| [SRC-E599346ABE-L001114](../generate_index.py#L1114) | 1114 | `"        while i < len(line):"` | — |
| [SRC-E599346ABE-L001115](../generate_index.py#L1115) | 1115 | `"            if in_block:"` | — |
| [SRC-E599346ABE-L001116](../generate_index.py#L1116) | 1116 | `"                end = line.find(\"*/\", i)"` | — |
| [SRC-E599346ABE-L001117](../generate_index.py#L1117) | 1117 | `"                if end < 0:"` | — |
| [SRC-E599346ABE-L001118](../generate_index.py#L1118) | 1118 | `"                    _append_comment_text(comments, line_number, line[i:])"` | — |
| [SRC-E599346ABE-L001119](../generate_index.py#L1119) | 1119 | `"                    i = len(line)"` | — |
| [SRC-E599346ABE-L001120](../generate_index.py#L1120) | 1120 | `"                else:"` | — |
| [SRC-E599346ABE-L001121](../generate_index.py#L1121) | 1121 | `"                    _append_comment_text(comments, line_number, line[i:end])"` | — |
| [SRC-E599346ABE-L001122](../generate_index.py#L1122) | 1122 | `"                    i = end + 2"` | — |
| [SRC-E599346ABE-L001123](../generate_index.py#L1123) | 1123 | `"                    in_block = False"` | — |
| [SRC-E599346ABE-L001124](../generate_index.py#L1124) | 1124 | `"                continue"` | — |
| [SRC-E599346ABE-L001125](../generate_index.py#L1125) | 1125 | `""` | — |
| [SRC-E599346ABE-L001126](../generate_index.py#L1126) | 1126 | `"            ch = line[i]"` | — |
| [SRC-E599346ABE-L001127](../generate_index.py#L1127) | 1127 | `"            if quote is not None:"` | — |
| [SRC-E599346ABE-L001128](../generate_index.py#L1128) | 1128 | `"                if ch == \"\\\\\":"` | — |
| [SRC-E599346ABE-L001129](../generate_index.py#L1129) | 1129 | `"                    i += 2"` | — |
| [SRC-E599346ABE-L001130](../generate_index.py#L1130) | 1130 | `"                    continue"` | — |
| [SRC-E599346ABE-L001131](../generate_index.py#L1131) | 1131 | `"                if ch == quote:"` | — |
| [SRC-E599346ABE-L001132](../generate_index.py#L1132) | 1132 | `"                    quote = None"` | — |
| [SRC-E599346ABE-L001133](../generate_index.py#L1133) | 1133 | `"                i += 1"` | — |
| [SRC-E599346ABE-L001134](../generate_index.py#L1134) | 1134 | `"                continue"` | — |
| [SRC-E599346ABE-L001135](../generate_index.py#L1135) | 1135 | `""` | — |
| [SRC-E599346ABE-L001136](../generate_index.py#L1136) | 1136 | `"            if ch in (\"'\", '\"', chr(96)):"` | — |
| [SRC-E599346ABE-L001137](../generate_index.py#L1137) | 1137 | `"                quote = ch"` | — |
| [SRC-E599346ABE-L001138](../generate_index.py#L1138) | 1138 | `"                i += 1"` | — |
| [SRC-E599346ABE-L001139](../generate_index.py#L1139) | 1139 | `"                continue"` | — |
| [SRC-E599346ABE-L001140](../generate_index.py#L1140) | 1140 | `""` | — |
| [SRC-E599346ABE-L001141](../generate_index.py#L1141) | 1141 | `"            if line.startswith(\"//\", i):"` | — |
| [SRC-E599346ABE-L001142](../generate_index.py#L1142) | 1142 | `"                _append_comment_text(comments, line_number, line[i + 2:].rstrip(\"\\r\\n\"))"` | — |
| [SRC-E599346ABE-L001143](../generate_index.py#L1143) | 1143 | `"                break"` | — |
| [SRC-E599346ABE-L001144](../generate_index.py#L1144) | 1144 | `"            if line.startswith(\"/*\", i):"` | — |
| [SRC-E599346ABE-L001145](../generate_index.py#L1145) | 1145 | `"                in_block = True"` | — |
| [SRC-E599346ABE-L001146](../generate_index.py#L1146) | 1146 | `"                i += 2"` | — |
| [SRC-E599346ABE-L001147](../generate_index.py#L1147) | 1147 | `"                continue"` | — |
| [SRC-E599346ABE-L001148](../generate_index.py#L1148) | 1148 | `""` | — |
| [SRC-E599346ABE-L001149](../generate_index.py#L1149) | 1149 | `"            if hash_comments and ch == \"#\" and (i == 0 or line[i - 1].isspace()):"` | — |
| [SRC-E599346ABE-L001150](../generate_index.py#L1150) | 1150 | `"                _append_comment_text(comments, line_number, line[i + 1:].rstrip(\"\\r\\n\"))"` | — |
| [SRC-E599346ABE-L001151](../generate_index.py#L1151) | 1151 | `"                break"` | — |
| [SRC-E599346ABE-L001152](../generate_index.py#L1152) | 1152 | `"            i += 1"` | — |
| [SRC-E599346ABE-L001153](../generate_index.py#L1153) | 1153 | `""` | — |
| [SRC-E599346ABE-L001154](../generate_index.py#L1154) | 1154 | `"        if quote in (\"'\", '\"') and not line.rstrip(\"\\r\\n\").endswith(\"\\\\\"):"` | — |
| [SRC-E599346ABE-L001155](../generate_index.py#L1155) | 1155 | `"            quote = None"` | — |
| [SRC-E599346ABE-L001156](../generate_index.py#L1156) | 1156 | `""` | — |
| [SRC-E599346ABE-L001157](../generate_index.py#L1157) | 1157 | `"    return comments"` | — |
| [SRC-E599346ABE-L001158](../generate_index.py#L1158) | 1158 | `""` | — |
| [SRC-E599346ABE-L001159](../generate_index.py#L1159) | 1159 | `""` | — |
| [SRC-E599346ABE-L001160](../generate_index.py#L1160) | 1160 | `"def _html_comment_map(source: str) -> dict[int, list[str]]:"` | — |
| [SRC-E599346ABE-L001161](../generate_index.py#L1161) | 1161 | `"    \"\"\"Return HTML comments while ignoring HTML-looking text inside script/style blocks.\"\"\""` | — |
| [SRC-E599346ABE-L001162](../generate_index.py#L1162) | 1162 | `"    comments: dict[int, list[str]] = {}"` | — |
| [SRC-E599346ABE-L001163](../generate_index.py#L1163) | 1163 | `"    masked_chars = list(source)"` | — |
| [SRC-E599346ABE-L001164](../generate_index.py#L1164) | 1164 | `"    for pattern in (HTML_SCRIPT_RE, HTML_STYLE_RE):"` | — |
| [SRC-E599346ABE-L001165](../generate_index.py#L1165) | 1165 | `"        for match in pattern.finditer(source):"` | — |
| [SRC-E599346ABE-L001166](../generate_index.py#L1166) | 1166 | `"            for position in range(match.start(), match.end()):"` | — |
| [SRC-E599346ABE-L001167](../generate_index.py#L1167) | 1167 | `"                if masked_chars[position] != \"\\\\n\":"` | — |
| [SRC-E599346ABE-L001168](../generate_index.py#L1168) | 1168 | `"                    masked_chars[position] = \" \""` | — |
| [SRC-E599346ABE-L001169](../generate_index.py#L1169) | 1169 | `"    masked_source = \"\".join(masked_chars)"` | — |
| [SRC-E599346ABE-L001170](../generate_index.py#L1170) | 1170 | `"    comment_re = re.compile(r\"<!--(.*?)-->\", re.DOTALL)"` | — |
| [SRC-E599346ABE-L001171](../generate_index.py#L1171) | 1171 | `"    for match in comment_re.finditer(masked_source):"` | — |
| [SRC-E599346ABE-L001172](../generate_index.py#L1172) | 1172 | `"        starting_line = _line_at(source, match.start(1))"` | — |
| [SRC-E599346ABE-L001173](../generate_index.py#L1173) | 1173 | `"        _append_comment_text("` | — |
| [SRC-E599346ABE-L001174](../generate_index.py#L1174) | 1174 | `"            comments,"` | — |
| [SRC-E599346ABE-L001175](../generate_index.py#L1175) | 1175 | `"            starting_line,"` | — |
| [SRC-E599346ABE-L001176](../generate_index.py#L1176) | 1176 | `"            source[match.start(1):match.end(1)],"` | — |
| [SRC-E599346ABE-L001177](../generate_index.py#L1177) | 1177 | `"        )"` | — |
| [SRC-E599346ABE-L001178](../generate_index.py#L1178) | 1178 | `"    return comments"` | — |
| [SRC-E599346ABE-L001179](../generate_index.py#L1179) | 1179 | `""` | — |
| [SRC-E599346ABE-L001180](../generate_index.py#L1180) | 1180 | `""` | — |
| [SRC-E599346ABE-L001181](../generate_index.py#L1181) | 1181 | `"def _markdown_annotation_map(source: str) -> dict[int, list[str]]:"` | — |
| [SRC-E599346ABE-L001182](../generate_index.py#L1182) | 1182 | `"    \"\"\"Accept explicit annotations at the start of Markdown prose, skipping fenced code.\"\"\""` | — |
| [SRC-E599346ABE-L001183](../generate_index.py#L1183) | 1183 | `"    comments: dict[int, list[str]] = {}"` | — |
| [SRC-E599346ABE-L001184](../generate_index.py#L1184) | 1184 | `"    in_fence = False"` | — |
| [SRC-E599346ABE-L001185](../generate_index.py#L1185) | 1185 | `"    fence_character = \"\""` | — |
| [SRC-E599346ABE-L001186](../generate_index.py#L1186) | 1186 | `"    fence_width = 0"` | — |
| [SRC-E599346ABE-L001187](../generate_index.py#L1187) | 1187 | `"    marker_start_re = re.compile("` | — |
| [SRC-E599346ABE-L001188](../generate_index.py#L1188) | 1188 | `"        rf\"^\\s*(?:(?:[-*+]\|>)\\s*)?({_FINDING_MARKER_ALTERNATION})\\s*:\\s*(.*)$\""` | — |
| [SRC-E599346ABE-L001189](../generate_index.py#L1189) | 1189 | `"    )"` | — |
| [SRC-E599346ABE-L001190](../generate_index.py#L1190) | 1190 | `"    for line_number, line in enumerate(source.splitlines(), start=1):"` | — |
| [SRC-E599346ABE-L001191](../generate_index.py#L1191) | 1191 | `"        fence_match = re.match(r\"^\\s*(~{3,})\", line) or re.match("` | — |
| [SRC-E599346ABE-L001192](../generate_index.py#L1192) | 1192 | `"            r\"^\\s*(\" + re.escape(chr(96)) + \"{3,})\", line"` | — |
| [SRC-E599346ABE-L001193](../generate_index.py#L1193) | 1193 | `"        )"` | — |
| [SRC-E599346ABE-L001194](../generate_index.py#L1194) | 1194 | `"        if fence_match:"` | — |
| [SRC-E599346ABE-L001195](../generate_index.py#L1195) | 1195 | `"            fence = fence_match.group(1)"` | — |
| [SRC-E599346ABE-L001196](../generate_index.py#L1196) | 1196 | `"            if not in_fence:"` | — |
| [SRC-E599346ABE-L001197](../generate_index.py#L1197) | 1197 | `"                in_fence = True"` | — |
| [SRC-E599346ABE-L001198](../generate_index.py#L1198) | 1198 | `"                fence_character = fence[0]"` | — |
| [SRC-E599346ABE-L001199](../generate_index.py#L1199) | 1199 | `"                fence_width = len(fence)"` | — |
| [SRC-E599346ABE-L001200](../generate_index.py#L1200) | 1200 | `"            elif fence[0] == fence_character and len(fence) >= fence_width:"` | — |
| [SRC-E599346ABE-L001201](../generate_index.py#L1201) | 1201 | `"                in_fence = False"` | — |
| [SRC-E599346ABE-L001202](../generate_index.py#L1202) | 1202 | `"            continue"` | — |
| [SRC-E599346ABE-L001203](../generate_index.py#L1203) | 1203 | `"        if in_fence:"` | — |
| [SRC-E599346ABE-L001204](../generate_index.py#L1204) | 1204 | `"            continue"` | — |
| [SRC-E599346ABE-L001205](../generate_index.py#L1205) | 1205 | `"        match = marker_start_re.match(line)"` | — |
| [SRC-E599346ABE-L001206](../generate_index.py#L1206) | 1206 | `"        if match:"` | — |
| [SRC-E599346ABE-L001207](../generate_index.py#L1207) | 1207 | `"            comments.setdefault(line_number, []).append("` | — |
| [SRC-E599346ABE-L001208](../generate_index.py#L1208) | 1208 | `"                f\"{match.group(1)}: {match.group(2)}\""` | — |
| [SRC-E599346ABE-L001209](../generate_index.py#L1209) | 1209 | `"            )"` | — |
| [SRC-E599346ABE-L001210](../generate_index.py#L1210) | 1210 | `"    return comments"` | — |
| [SRC-E599346ABE-L001211](../generate_index.py#L1211) | 1211 | `""` | — |
| [SRC-E599346ABE-L001212](../generate_index.py#L1212) | 1212 | `""` | — |
| [SRC-E599346ABE-L001213](../generate_index.py#L1213) | 1213 | `"def _finding_comments_by_file(relative_file: str, source: str) -> dict[int, list[str]]:"` | — |
| [SRC-E599346ABE-L001214](../generate_index.py#L1214) | 1214 | `"    \"\"\"Extract intended comment/prose annotations by file type, not arbitrary tokens.\"\"\""` | — |
| [SRC-E599346ABE-L001215](../generate_index.py#L1215) | 1215 | `"    path = Path(relative_file)"` | — |
| [SRC-E599346ABE-L001216](../generate_index.py#L1216) | 1216 | `"    suffix = path.suffix.lower()"` | — |
| [SRC-E599346ABE-L001217](../generate_index.py#L1217) | 1217 | `"    name = path.name.lower()"` | — |
| [SRC-E599346ABE-L001218](../generate_index.py#L1218) | 1218 | `"    if suffix == \".py\":"` | — |
| [SRC-E599346ABE-L001219](../generate_index.py#L1219) | 1219 | `"        return _python_comment_map(source)"` | — |
| [SRC-E599346ABE-L001220](../generate_index.py#L1220) | 1220 | `"    if suffix in JAVASCRIPT_EXTENSIONS \| CSS_EXTENSIONS:"` | — |
| [SRC-E599346ABE-L001221](../generate_index.py#L1221) | 1221 | `"        return _c_style_comment_map(source, hash_comments=suffix == \".scss\")"` | — |
| [SRC-E599346ABE-L001222](../generate_index.py#L1222) | 1222 | `"    if suffix in {\".html\", \".htm\"}:"` | — |
| [SRC-E599346ABE-L001223](../generate_index.py#L1223) | 1223 | `"        comments = _html_comment_map(source)"` | — |
| [SRC-E599346ABE-L001224](../generate_index.py#L1224) | 1224 | `"        for pattern in (HTML_SCRIPT_RE, HTML_STYLE_RE):"` | — |
| [SRC-E599346ABE-L001225](../generate_index.py#L1225) | 1225 | `"            for match in pattern.finditer(source):"` | — |
| [SRC-E599346ABE-L001226](../generate_index.py#L1226) | 1226 | `"                embedded = match.group(1)"` | — |
| [SRC-E599346ABE-L001227](../generate_index.py#L1227) | 1227 | `"                local_comments = _c_style_comment_map(embedded)"` | — |
| [SRC-E599346ABE-L001228](../generate_index.py#L1228) | 1228 | `"                base_line = _line_at(source, match.start(1))"` | — |
| [SRC-E599346ABE-L001229](../generate_index.py#L1229) | 1229 | `"                for local_line, fragments in local_comments.items():"` | — |
| [SRC-E599346ABE-L001230](../generate_index.py#L1230) | 1230 | `"                    for fragment in fragments:"` | — |
| [SRC-E599346ABE-L001231](../generate_index.py#L1231) | 1231 | `"                        comments.setdefault(base_line + local_line - 1, []).append(fragment)"` | — |
| [SRC-E599346ABE-L001232](../generate_index.py#L1232) | 1232 | `"        return comments"` | — |
| [SRC-E599346ABE-L001233](../generate_index.py#L1233) | 1233 | `"    if suffix in {\".md\", \".rst\"}:"` | — |
| [SRC-E599346ABE-L001234](../generate_index.py#L1234) | 1234 | `"        return _markdown_annotation_map(source)"` | — |
| [SRC-E599346ABE-L001235](../generate_index.py#L1235) | 1235 | `"    if suffix in {\".yml\", \".yaml\", \".toml\", \".ini\", \".cfg\", \".sh\"} or name in {"` | — |
| [SRC-E599346ABE-L001236](../generate_index.py#L1236) | 1236 | `"        \"dockerfile\","` | — |
| [SRC-E599346ABE-L001237](../generate_index.py#L1237) | 1237 | `"        \"makefile\","` | — |
| [SRC-E599346ABE-L001238](../generate_index.py#L1238) | 1238 | `"        \"procfile\","` | — |
| [SRC-E599346ABE-L001239](../generate_index.py#L1239) | 1239 | `"    }:"` | — |
| [SRC-E599346ABE-L001240](../generate_index.py#L1240) | 1240 | `"        return _c_style_comment_map(source, hash_comments=True)"` | — |
| [SRC-E599346ABE-L001241](../generate_index.py#L1241) | 1241 | `"    if suffix == \".txt\":"` | — |
| [SRC-E599346ABE-L001242](../generate_index.py#L1242) | 1242 | `"        return _markdown_annotation_map(source)"` | — |
| [SRC-E599346ABE-L001243](../generate_index.py#L1243) | 1243 | `"    return {}"` | — |
| [SRC-E599346ABE-L001244](../generate_index.py#L1244) | 1244 | `""` | — |
| [SRC-E599346ABE-L001245](../generate_index.py#L1245) | 1245 | `""` | — |
| [SRC-E599346ABE-L001246](../generate_index.py#L1246) | 1246 | `"def scan_finding_annotations(source_lines: list[IndexedLine]) -> list[IndexedFinding]:"` | — |
| [SRC-E599346ABE-L001247](../generate_index.py#L1247) | 1247 | `"    \"\"\"Index explicit comments/prose annotations, not incidental words in source code.\"\"\""` | — |
| [SRC-E599346ABE-L001248](../generate_index.py#L1248) | 1248 | `"    findings: list[IndexedFinding] = []"` | — |
| [SRC-E599346ABE-L001249](../generate_index.py#L1249) | 1249 | `"    by_file: dict[str, list[IndexedLine]] = {}"` | — |
| [SRC-E599346ABE-L001250](../generate_index.py#L1250) | 1250 | `"    for source_line in source_lines:"` | — |
| [SRC-E599346ABE-L001251](../generate_index.py#L1251) | 1251 | `"        by_file.setdefault(source_line.file, []).append(source_line)"` | — |
| [SRC-E599346ABE-L001252](../generate_index.py#L1252) | 1252 | `""` | — |
| [SRC-E599346ABE-L001253](../generate_index.py#L1253) | 1253 | `"    for relative_file, records in by_file.items():"` | — |
| [SRC-E599346ABE-L001254](../generate_index.py#L1254) | 1254 | `"        records.sort(key=lambda item: item.line)"` | — |
| [SRC-E599346ABE-L001255](../generate_index.py#L1255) | 1255 | `"        source = \"\\n\".join(item.content for item in records)"` | — |
| [SRC-E599346ABE-L001256](../generate_index.py#L1256) | 1256 | `"        comments = _finding_comments_by_file(relative_file, source)"` | — |
| [SRC-E599346ABE-L001257](../generate_index.py#L1257) | 1257 | `"        record_by_line = {item.line: item for item in records}"` | — |
| [SRC-E599346ABE-L001258](../generate_index.py#L1258) | 1258 | `""` | — |
| [SRC-E599346ABE-L001259](../generate_index.py#L1259) | 1259 | `"        for line_number, fragments in comments.items():"` | — |
| [SRC-E599346ABE-L001260](../generate_index.py#L1260) | 1260 | `"            source_line = record_by_line.get(line_number)"` | — |
| [SRC-E599346ABE-L001261](../generate_index.py#L1261) | 1261 | `"            if source_line is None:"` | — |
| [SRC-E599346ABE-L001262](../generate_index.py#L1262) | 1262 | `"                continue"` | — |
| [SRC-E599346ABE-L001263](../generate_index.py#L1263) | 1263 | `"            matches = ["` | — |
| [SRC-E599346ABE-L001264](../generate_index.py#L1264) | 1264 | `"                match"` | — |
| [SRC-E599346ABE-L001265](../generate_index.py#L1265) | 1265 | `"                for fragment in fragments"` | — |
| [SRC-E599346ABE-L001266](../generate_index.py#L1266) | 1266 | `"                for match in FINDING_MARKER_RE.finditer("` | — |
| [SRC-E599346ABE-L001267](../generate_index.py#L1267) | 1267 | `"                    fragment.lstrip().lstrip(\"*\").strip()"` | — |
| [SRC-E599346ABE-L001268](../generate_index.py#L1268) | 1268 | `"                )"` | — |
| [SRC-E599346ABE-L001269](../generate_index.py#L1269) | 1269 | `"            ]"` | — |
| [SRC-E599346ABE-L001270](../generate_index.py#L1270) | 1270 | `"            if not matches:"` | — |
| [SRC-E599346ABE-L001271](../generate_index.py#L1271) | 1271 | `"                continue"` | — |
| [SRC-E599346ABE-L001272](../generate_index.py#L1272) | 1272 | `"            totals: dict[str, int] = {}"` | — |
| [SRC-E599346ABE-L001273](../generate_index.py#L1273) | 1273 | `"            for match in matches:"` | — |
| [SRC-E599346ABE-L001274](../generate_index.py#L1274) | 1274 | `"                marker = match.group(1)"` | — |
| [SRC-E599346ABE-L001275](../generate_index.py#L1275) | 1275 | `"                totals[marker] = totals.get(marker, 0) + 1"` | — |
| [SRC-E599346ABE-L001276](../generate_index.py#L1276) | 1276 | `"            occurrences: dict[str, int] = {}"` | — |
| [SRC-E599346ABE-L001277](../generate_index.py#L1277) | 1277 | `"            for match in matches:"` | — |
| [SRC-E599346ABE-L001278](../generate_index.py#L1278) | 1278 | `"                marker = match.group(1)"` | — |
| [SRC-E599346ABE-L001279](../generate_index.py#L1279) | 1279 | `"                occurrences[marker] = occurrences.get(marker, 0) + 1"` | — |
| [SRC-E599346ABE-L001280](../generate_index.py#L1280) | 1280 | `"                detail = (match.group(2) or \"\").strip()"` | — |
| [SRC-E599346ABE-L001281](../generate_index.py#L1281) | 1281 | `"                description = marker if not detail else f\"{marker}: {detail}\""` | — |
| [SRC-E599346ABE-L001282](../generate_index.py#L1282) | 1282 | `"                finding_id = ("` | — |
| [SRC-E599346ABE-L001283](../generate_index.py#L1283) | 1283 | `"                    f\"FND-{marker}-{source_line.file_id.removeprefix('FILE-')}\""` | — |
| [SRC-E599346ABE-L001284](../generate_index.py#L1284) | 1284 | `"                    f\"-L{source_line.line:06d}\""` | — |
| [SRC-E599346ABE-L001285](../generate_index.py#L1285) | 1285 | `"                )"` | — |
| [SRC-E599346ABE-L001286](../generate_index.py#L1286) | 1286 | `"                if totals[marker] > 1:"` | — |
| [SRC-E599346ABE-L001287](../generate_index.py#L1287) | 1287 | `"                    finding_id += f\"-M{occurrences[marker]:02d}\""` | — |
| [SRC-E599346ABE-L001288](../generate_index.py#L1288) | 1288 | `"                findings.append("` | — |
| [SRC-E599346ABE-L001289](../generate_index.py#L1289) | 1289 | `"                    IndexedFinding("` | — |
| [SRC-E599346ABE-L001290](../generate_index.py#L1290) | 1290 | `"                        finding_id=finding_id,"` | — |
| [SRC-E599346ABE-L001291](../generate_index.py#L1291) | 1291 | `"                        file=source_line.file,"` | — |
| [SRC-E599346ABE-L001292](../generate_index.py#L1292) | 1292 | `"                        line_id=source_line.line_id,"` | — |
| [SRC-E599346ABE-L001293](../generate_index.py#L1293) | 1293 | `"                        marker=marker,"` | — |
| [SRC-E599346ABE-L001294](../generate_index.py#L1294) | 1294 | `"                        description=description,"` | — |
| [SRC-E599346ABE-L001295](../generate_index.py#L1295) | 1295 | `"                    )"` | — |
| [SRC-E599346ABE-L001296](../generate_index.py#L1296) | 1296 | `"                )"` | — |
| [SRC-E599346ABE-L001297](../generate_index.py#L1297) | 1297 | `"    findings.sort("` | — |
| [SRC-E599346ABE-L001298](../generate_index.py#L1298) | 1298 | `"        key=lambda item: (item.marker, item.file.casefold(), item.line_id, item.finding_id)"` | — |
| [SRC-E599346ABE-L001299](../generate_index.py#L1299) | 1299 | `"    )"` | — |
| [SRC-E599346ABE-L001300](../generate_index.py#L1300) | 1300 | `"    return findings"` | — |
| [SRC-E599346ABE-L001301](../generate_index.py#L1301) | 1301 | `""` | — |
| [SRC-E599346ABE-L001302](../generate_index.py#L1302) | 1302 | `""` | — |
| [SRC-E599346ABE-L001303](../generate_index.py#L1303) | 1303 | `"def _markdown_code_span(value: str) -> str:"` | — |
| [SRC-E599346ABE-L001304](../generate_index.py#L1304) | 1304 | `"    \"\"\"Render a Markdown inline-code span safely, including backticks in source text.\"\"\""` | — |
| [SRC-E599346ABE-L001305](../generate_index.py#L1305) | 1305 | `"    tick = chr(96)"` | — |
| [SRC-E599346ABE-L001306](../generate_index.py#L1306) | 1306 | `"    longest = max("` | — |
| [SRC-E599346ABE-L001307](../generate_index.py#L1307) | 1307 | `"        (len(match.group(0)) for match in re.finditer(r\"\\u0060+\", value)),"` | — |
| [SRC-E599346ABE-L001308](../generate_index.py#L1308) | 1308 | `"        default=0,"` | — |
| [SRC-E599346ABE-L001309](../generate_index.py#L1309) | 1309 | `"    )"` | — |
| [SRC-E599346ABE-L001310](../generate_index.py#L1310) | 1310 | `"    fence = tick * (longest + 1)"` | — |
| [SRC-E599346ABE-L001311](../generate_index.py#L1311) | 1311 | `"    content = f\" {value} \" if value.startswith(tick) or value.endswith(tick) else value"` | — |
| [SRC-E599346ABE-L001312](../generate_index.py#L1312) | 1312 | `"    return f\"{fence}{content}{fence}\""` | — |
| [SRC-E599346ABE-L001313](../generate_index.py#L1313) | 1313 | `""` | — |
| [SRC-E599346ABE-L001314](../generate_index.py#L1314) | 1314 | `""` | — |
| [SRC-E599346ABE-L001315](../generate_index.py#L1315) | 1315 | `"def render_source_line_pages("` | — |
| [SRC-E599346ABE-L001316](../generate_index.py#L1316) | 1316 | `"    source_lines: list[IndexedLine],"` | — |
| [SRC-E599346ABE-L001317](../generate_index.py#L1317) | 1317 | `"    inventory: list[IndexedFile],"` | — |
| [SRC-E599346ABE-L001318](../generate_index.py#L1318) | 1318 | `"    findings: list[IndexedFinding],"` | — |
| [SRC-E599346ABE-L001319](../generate_index.py#L1319) | 1319 | `") -> tuple[dict[str, str], dict[str, list[str]]]:"` | — |
| [SRC-E599346ABE-L001320](../generate_index.py#L1320) | 1320 | `"    \"\"\"Split line-level records into deterministic small pages and map each file to its pages.\"\"\""` | — |
| [SRC-E599346ABE-L001321](../generate_index.py#L1321) | 1321 | `"    pages: dict[str, str] = {}"` | — |
| [SRC-E599346ABE-L001322](../generate_index.py#L1322) | 1322 | `"    pages_by_file: dict[str, list[str]] = {}"` | — |
| [SRC-E599346ABE-L001323](../generate_index.py#L1323) | 1323 | `"    inventory_by_path = {item.file: item for item in inventory}"` | — |
| [SRC-E599346ABE-L001324](../generate_index.py#L1324) | 1324 | `"    findings_by_line: dict[str, list[IndexedFinding]] = {}"` | — |
| [SRC-E599346ABE-L001325](../generate_index.py#L1325) | 1325 | `"    for finding in findings:"` | — |
| [SRC-E599346ABE-L001326](../generate_index.py#L1326) | 1326 | `"        findings_by_line.setdefault(finding.line_id, []).append(finding)"` | — |
| [SRC-E599346ABE-L001327](../generate_index.py#L1327) | 1327 | `""` | — |
| [SRC-E599346ABE-L001328](../generate_index.py#L1328) | 1328 | `"    for page_number, start in enumerate("` | — |
| [SRC-E599346ABE-L001329](../generate_index.py#L1329) | 1329 | `"        range(0, len(source_lines), SOURCE_LINES_PAGE_SIZE),"` | — |
| [SRC-E599346ABE-L001330](../generate_index.py#L1330) | 1330 | `"        start=1,"` | — |
| [SRC-E599346ABE-L001331](../generate_index.py#L1331) | 1331 | `"    ):"` | — |
| [SRC-E599346ABE-L001332](../generate_index.py#L1332) | 1332 | `"        chunk = source_lines[start : start + SOURCE_LINES_PAGE_SIZE]"` | — |
| [SRC-E599346ABE-L001333](../generate_index.py#L1333) | 1333 | `"        page_path = f\"{SOURCE_LINES_PAGES_DIR}/SOURCE_LINES_{page_number:03d}.md\""` | — |
| [SRC-E599346ABE-L001334](../generate_index.py#L1334) | 1334 | `"        lines = ["` | — |
| [SRC-E599346ABE-L001335](../generate_index.py#L1335) | 1335 | `"            \"# Omarai Source Lines\","` | — |
| [SRC-E599346ABE-L001336](../generate_index.py#L1336) | 1336 | `"            \"\","` | — |
| [SRC-E599346ABE-L001337](../generate_index.py#L1337) | 1337 | `"            \"<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->\","` | — |
| [SRC-E599346ABE-L001338](../generate_index.py#L1338) | 1338 | `"            \"\","` | — |
| [SRC-E599346ABE-L001339](../generate_index.py#L1339) | 1339 | `"            f\"- الصفحة: **{page_number:03d}**\","` | — |
| [SRC-E599346ABE-L001340](../generate_index.py#L1340) | 1340 | `"            f\"- سجلات الأسطر: **{len(chunk)}**\","` | — |
| [SRC-E599346ABE-L001341](../generate_index.py#L1341) | 1341 | `"            f\"- النطاق: {chunk[0].line_id} إلى {chunk[-1].line_id}\","` | — |
| [SRC-E599346ABE-L001342](../generate_index.py#L1342) | 1342 | `"            \"- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)\","` | — |
| [SRC-E599346ABE-L001343](../generate_index.py#L1343) | 1343 | `"            \"\","` | — |
| [SRC-E599346ABE-L001344](../generate_index.py#L1344) | 1344 | `"        ]"` | — |
| [SRC-E599346ABE-L001345](../generate_index.py#L1345) | 1345 | `"        current_file: str \| None = None"` | — |
| [SRC-E599346ABE-L001346](../generate_index.py#L1346) | 1346 | `"        for source_line in chunk:"` | — |
| [SRC-E599346ABE-L001347](../generate_index.py#L1347) | 1347 | `"            item = inventory_by_path[source_line.file]"` | — |
| [SRC-E599346ABE-L001348](../generate_index.py#L1348) | 1348 | `"            if source_line.file != current_file:"` | — |
| [SRC-E599346ABE-L001349](../generate_index.py#L1349) | 1349 | `"                current_file = source_line.file"` | — |
| [SRC-E599346ABE-L001350](../generate_index.py#L1350) | 1350 | `"                lines.extend("` | — |
| [SRC-E599346ABE-L001351](../generate_index.py#L1351) | 1351 | `"                    ["` | — |
| [SRC-E599346ABE-L001352](../generate_index.py#L1352) | 1352 | `"                        f\"## {item.category}\","` | — |
| [SRC-E599346ABE-L001353](../generate_index.py#L1353) | 1353 | `"                        \"\","` | — |
| [SRC-E599346ABE-L001354](../generate_index.py#L1354) | 1354 | `"                        f\"### {item.file_id} — [{_markdown_cell(item.file)}]({_source_file_href(item.file, index_directory=SOURCE_LINES_PAGES_DIR)})\","` | — |
| [SRC-E599346ABE-L001355](../generate_index.py#L1355) | 1355 | `"                        \"\","` | — |
| [SRC-E599346ABE-L001356](../generate_index.py#L1356) | 1356 | `"                        f\"- النوع: **{item.file_type}**\","` | — |
| [SRC-E599346ABE-L001357](../generate_index.py#L1357) | 1357 | `"                        f\"- نطاق الفهرسة: {_markdown_cell(item.indexing_scope)}\","` | — |
| [SRC-E599346ABE-L001358](../generate_index.py#L1358) | 1358 | `"                        \"\","` | — |
| [SRC-E599346ABE-L001359](../generate_index.py#L1359) | 1359 | `"                        \"\| كود السطر \| السطر \| النص الكامل للسطر \| كود الوسم \|\","` | — |
| [SRC-E599346ABE-L001360](../generate_index.py#L1360) | 1360 | `"                        \"\|---\|---:\|---\|---\|\","` | — |
| [SRC-E599346ABE-L001361](../generate_index.py#L1361) | 1361 | `"                    ]"` | — |
| [SRC-E599346ABE-L001362](../generate_index.py#L1362) | 1362 | `"                )"` | — |
| [SRC-E599346ABE-L001363](../generate_index.py#L1363) | 1363 | `"            line_findings = findings_by_line.get(source_line.line_id, [])"` | — |
| [SRC-E599346ABE-L001364](../generate_index.py#L1364) | 1364 | `"            finding_code = \", \".join(item.finding_id for item in line_findings) or \"—\""` | — |
| [SRC-E599346ABE-L001365](../generate_index.py#L1365) | 1365 | `"            exact_text = json.dumps(source_line.content, ensure_ascii=False)"` | — |
| [SRC-E599346ABE-L001366](../generate_index.py#L1366) | 1366 | `"            escaped_text = exact_text.replace(\"\|\", r\"\\\|\")"` | — |
| [SRC-E599346ABE-L001367](../generate_index.py#L1367) | 1367 | `"            href = _source_file_href("` | — |
| [SRC-E599346ABE-L001368](../generate_index.py#L1368) | 1368 | `"                source_line.file,"` | — |
| [SRC-E599346ABE-L001369](../generate_index.py#L1369) | 1369 | `"                source_line.line,"` | — |
| [SRC-E599346ABE-L001370](../generate_index.py#L1370) | 1370 | `"                index_directory=SOURCE_LINES_PAGES_DIR,"` | — |
| [SRC-E599346ABE-L001371](../generate_index.py#L1371) | 1371 | `"            )"` | — |
| [SRC-E599346ABE-L001372](../generate_index.py#L1372) | 1372 | `"            line_code = f\"[{source_line.line_id}]({href})\""` | — |
| [SRC-E599346ABE-L001373](../generate_index.py#L1373) | 1373 | `"            lines.append("` | — |
| [SRC-E599346ABE-L001374](../generate_index.py#L1374) | 1374 | `"                \"\| \""` | — |
| [SRC-E599346ABE-L001375](../generate_index.py#L1375) | 1375 | `"                + \" \| \".join("` | — |
| [SRC-E599346ABE-L001376](../generate_index.py#L1376) | 1376 | `"                    ("` | — |
| [SRC-E599346ABE-L001377](../generate_index.py#L1377) | 1377 | `"                        line_code,"` | — |
| [SRC-E599346ABE-L001378](../generate_index.py#L1378) | 1378 | `"                        str(source_line.line),"` | — |
| [SRC-E599346ABE-L001379](../generate_index.py#L1379) | 1379 | `"                        _markdown_code_span(escaped_text),"` | — |
| [SRC-E599346ABE-L001380](../generate_index.py#L1380) | 1380 | `"                        finding_code,"` | — |
| [SRC-E599346ABE-L001381](../generate_index.py#L1381) | 1381 | `"                    )"` | — |
| [SRC-E599346ABE-L001382](../generate_index.py#L1382) | 1382 | `"                )"` | — |
| [SRC-E599346ABE-L001383](../generate_index.py#L1383) | 1383 | `"                + \" \|\""` | — |
| [SRC-E599346ABE-L001384](../generate_index.py#L1384) | 1384 | `"            )"` | — |
| [SRC-E599346ABE-L001385](../generate_index.py#L1385) | 1385 | `"            refs = pages_by_file.setdefault(source_line.file, [])"` | — |
| [SRC-E599346ABE-L001386](../generate_index.py#L1386) | 1386 | `"            if page_path not in refs:"` | — |
| [SRC-E599346ABE-L001387](../generate_index.py#L1387) | 1387 | `"                refs.append(page_path)"` | — |
| [SRC-E599346ABE-L001388](../generate_index.py#L1388) | 1388 | `"        pages[page_path] = \"\\n\".join(lines) + \"\\n\""` | — |
| [SRC-E599346ABE-L001389](../generate_index.py#L1389) | 1389 | `""` | — |
| [SRC-E599346ABE-L001390](../generate_index.py#L1390) | 1390 | `"    return pages, pages_by_file"` | — |
| [SRC-E599346ABE-L001391](../generate_index.py#L1391) | 1391 | `""` | — |
| [SRC-E599346ABE-L001392](../generate_index.py#L1392) | 1392 | `""` | — |
| [SRC-E599346ABE-L001393](../generate_index.py#L1393) | 1393 | `"def render_source_lines_markdown("` | — |
| [SRC-E599346ABE-L001394](../generate_index.py#L1394) | 1394 | `"    source_lines: list[IndexedLine],"` | — |
| [SRC-E599346ABE-L001395](../generate_index.py#L1395) | 1395 | `"    inventory: list[IndexedFile],"` | — |
| [SRC-E599346ABE-L001396](../generate_index.py#L1396) | 1396 | `"    findings: list[IndexedFinding],"` | — |
| [SRC-E599346ABE-L001397](../generate_index.py#L1397) | 1397 | `"    pages_by_file: dict[str, list[str]] \| None = None,"` | — |
| [SRC-E599346ABE-L001398](../generate_index.py#L1398) | 1398 | `"    source_pages: dict[str, str] \| None = None,"` | — |
| [SRC-E599346ABE-L001399](../generate_index.py#L1399) | 1399 | `") -> str:"` | — |
| [SRC-E599346ABE-L001400](../generate_index.py#L1400) | 1400 | `"    \"\"\"Render a compact table of contents for the sharded full source-line index.\"\"\""` | — |
| [SRC-E599346ABE-L001401](../generate_index.py#L1401) | 1401 | `"    assigned_pages = pages_by_file or {}"` | — |
| [SRC-E599346ABE-L001402](../generate_index.py#L1402) | 1402 | `"    rendered_pages = source_pages or {}"` | — |
| [SRC-E599346ABE-L001403](../generate_index.py#L1403) | 1403 | `"    files_with_lines = sum(item.line_count is not None for item in inventory)"` | — |
| [SRC-E599346ABE-L001404](../generate_index.py#L1404) | 1404 | `"    lines = ["` | — |
| [SRC-E599346ABE-L001405](../generate_index.py#L1405) | 1405 | `"        \"# SOURCE LINES INDEX — Omarai\","` | — |
| [SRC-E599346ABE-L001406](../generate_index.py#L1406) | 1406 | `"        \"\","` | — |
| [SRC-E599346ABE-L001407](../generate_index.py#L1407) | 1407 | `"        \"<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->\","` | — |
| [SRC-E599346ABE-L001408](../generate_index.py#L1408) | 1408 | `"        \"\","` | — |
| [SRC-E599346ABE-L001409](../generate_index.py#L1409) | 1409 | `"        \"> هذا دليل الوصول إلى فهرس الأسطر الكامل. يحتوي كل سطر في الملفات النصية المؤهلة على كود SRC- ورقم السطر ونص السطر كاملًا.\","` | — |
| [SRC-E599346ABE-L001410](../generate_index.py#L1410) | 1410 | `"        \"> قُسّم المحتوى إلى صفحات صغيرة حتى تظل كل صفحة قابلة للفتح والبحث بسرعة من الهاتف والمتصفح.\","` | — |
| [SRC-E599346ABE-L001411](../generate_index.py#L1411) | 1411 | `"        \"> ابدأ من [MASTER INDEX](MASTER_INDEX.md) للعثور حسب اسم الملف أو الدالة أو الكلاس أو وسم المراجعة.\","` | — |
| [SRC-E599346ABE-L001412](../generate_index.py#L1412) | 1412 | `"        \"> راجع [INDEX COVERAGE AUDIT](INDEX_COVERAGE_AUDIT.md) للاطلاع على نسبة التغطية وأسباب الاستبعاد.\","` | — |
| [SRC-E599346ABE-L001413](../generate_index.py#L1413) | 1413 | `"        \"\","` | — |
| [SRC-E599346ABE-L001414](../generate_index.py#L1414) | 1414 | `"        \"## ملخص التغطية\","` | — |
| [SRC-E599346ABE-L001415](../generate_index.py#L1415) | 1415 | `"        \"\","` | — |
| [SRC-E599346ABE-L001416](../generate_index.py#L1416) | 1416 | `"        f\"- الملفات في جرد المستودع: **{len(inventory)}**\","` | — |
| [SRC-E599346ABE-L001417](../generate_index.py#L1417) | 1417 | `"        f\"- الملفات النصية المفهرسة سطرًا بسطر: **{files_with_lines}**\","` | — |
| [SRC-E599346ABE-L001418](../generate_index.py#L1418) | 1418 | `"        f\"- الأسطر المفهرسة: **{len(source_lines)}**\","` | — |
| [SRC-E599346ABE-L001419](../generate_index.py#L1419) | 1419 | `"        f\"- وسوم المراجعة/الإصلاح المسجلة: **{len(findings)}**\","` | — |
| [SRC-E599346ABE-L001420](../generate_index.py#L1420) | 1420 | `"        f\"- صفحات الأسطر: **{len(rendered_pages)}**\","` | — |
| [SRC-E599346ABE-L001421](../generate_index.py#L1421) | 1421 | `"        \"\","` | — |
| [SRC-E599346ABE-L001422](../generate_index.py#L1422) | 1422 | `"        \"## صفحات الأسطر\","` | — |
| [SRC-E599346ABE-L001423](../generate_index.py#L1423) | 1423 | `"        \"\","` | — |
| [SRC-E599346ABE-L001424](../generate_index.py#L1424) | 1424 | `"        \"\| الصفحة \| عدد السجلات \| من كود \| إلى كود \|\","` | — |
| [SRC-E599346ABE-L001425](../generate_index.py#L1425) | 1425 | `"        \"\|---\|---:\|---\|---\|\","` | — |
| [SRC-E599346ABE-L001426](../generate_index.py#L1426) | 1426 | `"    ]"` | — |
| [SRC-E599346ABE-L001427](../generate_index.py#L1427) | 1427 | `"    for page_path, page_content in rendered_pages.items():"` | — |
| [SRC-E599346ABE-L001428](../generate_index.py#L1428) | 1428 | `"        count = sum(1 for line in page_content.splitlines() if line.startswith(\"\| [SRC-\"))"` | — |
| [SRC-E599346ABE-L001429](../generate_index.py#L1429) | 1429 | `"        ids = re.findall(r\"\\bSRC-[A-F0-9]+-L\\d{6}\\b\", page_content)"` | — |
| [SRC-E599346ABE-L001430](../generate_index.py#L1430) | 1430 | `"        label = Path(page_path).stem"` | — |
| [SRC-E599346ABE-L001431](../generate_index.py#L1431) | 1431 | `"        lines.append("` | — |
| [SRC-E599346ABE-L001432](../generate_index.py#L1432) | 1432 | `"            f\"\| [{label}]({Path(page_path).relative_to('docs').as_posix()}) \| \""` | — |
| [SRC-E599346ABE-L001433](../generate_index.py#L1433) | 1433 | `"            f\"{count} \| {ids[0] if ids else '—'} \| {ids[-1] if ids else '—'} \|\""` | — |
| [SRC-E599346ABE-L001434](../generate_index.py#L1434) | 1434 | `"        )"` | — |
| [SRC-E599346ABE-L001435](../generate_index.py#L1435) | 1435 | `"    lines.extend("` | — |
| [SRC-E599346ABE-L001436](../generate_index.py#L1436) | 1436 | `"        ["` | — |
| [SRC-E599346ABE-L001437](../generate_index.py#L1437) | 1437 | `"            \"\","` | — |
| [SRC-E599346ABE-L001438](../generate_index.py#L1438) | 1438 | `"            \"## جرد الملفات والوصول حسب الاسم\","` | — |
| [SRC-E599346ABE-L001439](../generate_index.py#L1439) | 1439 | `"            \"\","` | — |
| [SRC-E599346ABE-L001440](../generate_index.py#L1440) | 1440 | `"            \"\| معرّف الملف \| التصنيف \| الملف \| الأسطر \| صفحات الفهرسة \|\","` | — |
| [SRC-E599346ABE-L001441](../generate_index.py#L1441) | 1441 | `"            \"\|---\|---\|---\|---:\|---\|\","` | — |
| [SRC-E599346ABE-L001442](../generate_index.py#L1442) | 1442 | `"        ]"` | — |
| [SRC-E599346ABE-L001443](../generate_index.py#L1443) | 1443 | `"    )"` | — |
| [SRC-E599346ABE-L001444](../generate_index.py#L1444) | 1444 | `"    for item in sorted(inventory, key=lambda entry: (entry.category, entry.file.casefold())):"` | — |
| [SRC-E599346ABE-L001445](../generate_index.py#L1445) | 1445 | `"        if item.line_count is None:"` | — |
| [SRC-E599346ABE-L001446](../generate_index.py#L1446) | 1446 | `"            line_count = \"بيانات وصفية فقط\""` | — |
| [SRC-E599346ABE-L001447](../generate_index.py#L1447) | 1447 | `"        else:"` | — |
| [SRC-E599346ABE-L001448](../generate_index.py#L1448) | 1448 | `"            line_count = str(item.line_count)"` | — |
| [SRC-E599346ABE-L001449](../generate_index.py#L1449) | 1449 | `"        page_links = assigned_pages.get(item.file, [])"` | — |
| [SRC-E599346ABE-L001450](../generate_index.py#L1450) | 1450 | `"        if page_links:"` | — |
| [SRC-E599346ABE-L001451](../generate_index.py#L1451) | 1451 | `"            link_text = \", \".join("` | — |
| [SRC-E599346ABE-L001452](../generate_index.py#L1452) | 1452 | `"                f\"[{Path(page_path).stem}]({Path(page_path).relative_to('docs').as_posix()})\""` | — |
| [SRC-E599346ABE-L001453](../generate_index.py#L1453) | 1453 | `"                for page_path in page_links"` | — |
| [SRC-E599346ABE-L001454](../generate_index.py#L1454) | 1454 | `"            )"` | — |
| [SRC-E599346ABE-L001455](../generate_index.py#L1455) | 1455 | `"        elif item.line_count == 0:"` | — |
| [SRC-E599346ABE-L001456](../generate_index.py#L1456) | 1456 | `"            link_text = \"ملف نصي فارغ\""` | — |
| [SRC-E599346ABE-L001457](../generate_index.py#L1457) | 1457 | `"        elif item.line_count is None:"` | — |
| [SRC-E599346ABE-L001458](../generate_index.py#L1458) | 1458 | `"            link_text = \"غير مفهرس سطرًا بسطر\""` | — |
| [SRC-E599346ABE-L001459](../generate_index.py#L1459) | 1459 | `"        else:"` | — |
| [SRC-E599346ABE-L001460](../generate_index.py#L1460) | 1460 | `"            link_text = \"لا توجد سجلات\""` | — |
| [SRC-E599346ABE-L001461](../generate_index.py#L1461) | 1461 | `"        target = _source_file_href(item.file, index_directory=\"docs\")"` | — |
| [SRC-E599346ABE-L001462](../generate_index.py#L1462) | 1462 | `"        lines.append("` | — |
| [SRC-E599346ABE-L001463](../generate_index.py#L1463) | 1463 | `"            f\"\| {item.file_id} \| {_markdown_cell(item.category)} \| \""` | — |
| [SRC-E599346ABE-L001464](../generate_index.py#L1464) | 1464 | `"            f\"[{_markdown_cell(item.file)}]({target}) \| {line_count} \| {link_text} \|\""` | — |
| [SRC-E599346ABE-L001465](../generate_index.py#L1465) | 1465 | `"        )"` | — |
| [SRC-E599346ABE-L001466](../generate_index.py#L1466) | 1466 | `"    lines.extend("` | — |
| [SRC-E599346ABE-L001467](../generate_index.py#L1467) | 1467 | `"        ["` | — |
| [SRC-E599346ABE-L001468](../generate_index.py#L1468) | 1468 | `"            \"\","` | — |
| [SRC-E599346ABE-L001469](../generate_index.py#L1469) | 1469 | `"            \"## سجل وسوم المراجعة والإصلاح\","` | — |
| [SRC-E599346ABE-L001470](../generate_index.py#L1470) | 1470 | `"            \"\","` | — |
| [SRC-E599346ABE-L001471](../generate_index.py#L1471) | 1471 | `"            \"كل كود FND- في MASTER INDEX يحدد وسمًا صريحًا ويشير إلى كود السطر في إحدى صفحات هذا الفهرس.\","` | — |
| [SRC-E599346ABE-L001472](../generate_index.py#L1472) | 1472 | `"            \"الوسوم المعروفة: TODO وFIXME وBUG وHACK وXXX وREVIEW وSECURITY وDEPRECATED وISSUE وDEFECT وREGRESSION وRISK وGAP وERROR وWARNING وPERF وPRIVACY وDATA_LOSS وACCESSIBILITY.\","` | — |
| [SRC-E599346ABE-L001473](../generate_index.py#L1473) | 1473 | `"            \"\","` | — |
| [SRC-E599346ABE-L001474](../generate_index.py#L1474) | 1474 | `"            \"## الاستثناءات وحدود التغطية\","` | — |
| [SRC-E599346ABE-L001475](../generate_index.py#L1475) | 1475 | `"            \"\","` | — |
| [SRC-E599346ABE-L001476](../generate_index.py#L1476) | 1476 | `"            \"- ملفات الفهرسة المولّدة نفسها مستثناة لمنع الحلقة الذاتية.\","` | — |
| [SRC-E599346ABE-L001477](../generate_index.py#L1477) | 1477 | `"            \"- تُفهرس سطور كل ملف نصي قابل للقراءة وحجمه حتى 2 MiB؛ الملفات الثنائية أو الأكبر أو غير القابلة للقراءة تظهر في جرد الملفات فقط.\","` | — |
| [SRC-E599346ABE-L001478](../generate_index.py#L1478) | 1478 | `"            \"- الملفات الحساسة المعروفة وقواعد البيانات والبيئات المحلية ومجلدات البناء والاعتماديات مستثناة عمدًا.\","` | — |
| [SRC-E599346ABE-L001479](../generate_index.py#L1479) | 1479 | `"            \"- أكواد الأسطر مشتقة من مسار الملف ورقم السطر؛ يتغير رقم الكود عند تحرك السطر بسبب تغييرات سابقة في الملف.\","` | — |
| [SRC-E599346ABE-L001480](../generate_index.py#L1480) | 1480 | `"            \"- وسوم المراجعة ليست تشخيصًا آليًا لكل عيب منطقي؛ الفهرس يسهل العثور على الكود لكنه لا يستطيع إثبات خلوه من الأخطاء.\","` | — |
| [SRC-E599346ABE-L001481](../generate_index.py#L1481) | 1481 | `"            \"\","` | — |
| [SRC-E599346ABE-L001482](../generate_index.py#L1482) | 1482 | `"        ]"` | — |
| [SRC-E599346ABE-L001483](../generate_index.py#L1483) | 1483 | `"    )"` | — |
| [SRC-E599346ABE-L001484](../generate_index.py#L1484) | 1484 | `"    return \"\\n\".join(lines) + \"\\n\""` | — |
| [SRC-E599346ABE-L001485](../generate_index.py#L1485) | 1485 | `""` | — |
| [SRC-E599346ABE-L001486](../generate_index.py#L1486) | 1486 | `""` | — |
| [SRC-E599346ABE-L001487](../generate_index.py#L1487) | 1487 | `"def render_coverage_audit_markdown("` | — |
| [SRC-E599346ABE-L001488](../generate_index.py#L1488) | 1488 | `"    root: Path,"` | — |
| [SRC-E599346ABE-L001489](../generate_index.py#L1489) | 1489 | `"    inventory: list[IndexedFile],"` | — |
| [SRC-E599346ABE-L001490](../generate_index.py#L1490) | 1490 | `"    source_lines: list[IndexedLine],"` | — |
| [SRC-E599346ABE-L001491](../generate_index.py#L1491) | 1491 | `"    excluded_paths: list[tuple[str, str]],"` | — |
| [SRC-E599346ABE-L001492](../generate_index.py#L1492) | 1492 | `") -> str:"` | — |
| [SRC-E599346ABE-L001493](../generate_index.py#L1493) | 1493 | `"    \"\"\"Render a generated coverage ledger with exact line-index coverage and exclusions.\"\"\""` | — |
| [SRC-E599346ABE-L001494](../generate_index.py#L1494) | 1494 | `"    indexed_files = [item for item in inventory if item.line_count is not None]"` | — |
| [SRC-E599346ABE-L001495](../generate_index.py#L1495) | 1495 | `"    metadata_only = [item for item in inventory if item.line_count is None]"` | — |
| [SRC-E599346ABE-L001496](../generate_index.py#L1496) | 1496 | `"    expected_line_count = sum(item.line_count or 0 for item in indexed_files)"` | — |
| [SRC-E599346ABE-L001497](../generate_index.py#L1497) | 1497 | `"    actual_line_count = len(source_lines)"` | — |
| [SRC-E599346ABE-L001498](../generate_index.py#L1498) | 1498 | `"    coverage_ok = expected_line_count == actual_line_count"` | — |
| [SRC-E599346ABE-L001499](../generate_index.py#L1499) | 1499 | `"    lines = ["` | — |
| [SRC-E599346ABE-L001500](../generate_index.py#L1500) | 1500 | `"        \"# OMARAI INDEX COVERAGE AUDIT\","` | — |
| [SRC-E599346ABE-L001501](../generate_index.py#L1501) | 1501 | `"        \"\","` | — |
| [SRC-E599346ABE-L001502](../generate_index.py#L1502) | 1502 | `"        \"<!-- هذا الملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->\","` | — |
| [SRC-E599346ABE-L001503](../generate_index.py#L1503) | 1503 | `"        \"\","` | — |
| [SRC-E599346ABE-L001504](../generate_index.py#L1504) | 1504 | `"        \"> سجل أدلة تغطية الفهرس وحدوده، وليس ادعاءً باكتشاف كل عيب منطقي في البرنامج.\","` | — |
| [SRC-E599346ABE-L001505](../generate_index.py#L1505) | 1505 | `"        \"\","` | — |
| [SRC-E599346ABE-L001506](../generate_index.py#L1506) | 1506 | `"        \"## نتيجة تغطية السطور\","` | — |
| [SRC-E599346ABE-L001507](../generate_index.py#L1507) | 1507 | `"        \"\","` | — |
| [SRC-E599346ABE-L001508](../generate_index.py#L1508) | 1508 | `"        f\"- ملفات المستودع المؤهلة في الجرد: **{len(inventory)}**\","` | — |
| [SRC-E599346ABE-L001509](../generate_index.py#L1509) | 1509 | `"        f\"- الملفات المفهرسة سطرًا بسطر: **{len(indexed_files)}**\","` | — |
| [SRC-E599346ABE-L001510](../generate_index.py#L1510) | 1510 | `"        f\"- الملفات الوصفية فقط التي لا تتوفر سطورها: **{len(metadata_only)}**\","` | — |
| [SRC-E599346ABE-L001511](../generate_index.py#L1511) | 1511 | `"        f\"- السطور المتوقع فهرستها من عدادات الملفات: **{expected_line_count}**\","` | — |
| [SRC-E599346ABE-L001512](../generate_index.py#L1512) | 1512 | `"        f\"- سجلات السطور الفعلية: **{actual_line_count}**\","` | — |
| [SRC-E599346ABE-L001513](../generate_index.py#L1513) | 1513 | `"        f\"- تحقق العدد الإجمالي: **{'PASS' if coverage_ok else 'FAIL'}**\","` | — |
| [SRC-E599346ABE-L001514](../generate_index.py#L1514) | 1514 | `"        f\"- نسبة التغطية الحسابية ضمن الملفات المؤهلة القابلة للقراءة: **{(100.0 if coverage_ok and expected_line_count == actual_line_count else (actual_line_count / expected_line_count * 100 if expected_line_count else 100.0)):.2f}%**\","` | — |
| [SRC-E599346ABE-L001515](../generate_index.py#L1515) | 1515 | `"        \"\","` | — |
| [SRC-E599346ABE-L001516](../generate_index.py#L1516) | 1516 | `"        \"يتحقق المولد كذلك من أن أرقام السطور متتابعة لكل ملف ومن عدم تكرار معرّفات SRC؛ أي فشل يمنع نشر الفهرس.\","` | — |
| [SRC-E599346ABE-L001517](../generate_index.py#L1517) | 1517 | `"        \"\","` | — |
| [SRC-E599346ABE-L001518](../generate_index.py#L1518) | 1518 | `"        \"## الملفات التي لا تُفهرس سطورها\","` | — |
| [SRC-E599346ABE-L001519](../generate_index.py#L1519) | 1519 | `"        \"\","` | — |
| [SRC-E599346ABE-L001520](../generate_index.py#L1520) | 1520 | `"        \"هذه الملفات تظل ظاهرة في جرد MASTER INDEX مع سبب الاستثناء. لا يُدرج التقرير محتوياتها.\","` | — |
| [SRC-E599346ABE-L001521](../generate_index.py#L1521) | 1521 | `"        \"\","` | — |
| [SRC-E599346ABE-L001522](../generate_index.py#L1522) | 1522 | `"        \"\| معرّف الملف \| المسار \| الحجم بالبايت \| السبب \|\","` | — |
| [SRC-E599346ABE-L001523](../generate_index.py#L1523) | 1523 | `"        \"\|---\|---\|---:\|---\|\","` | — |
| [SRC-E599346ABE-L001524](../generate_index.py#L1524) | 1524 | `"    ]"` | — |
| [SRC-E599346ABE-L001525](../generate_index.py#L1525) | 1525 | `""` | — |
| [SRC-E599346ABE-L001526](../generate_index.py#L1526) | 1526 | `"    if metadata_only:"` | — |
| [SRC-E599346ABE-L001527](../generate_index.py#L1527) | 1527 | `"        for item in metadata_only:"` | — |
| [SRC-E599346ABE-L001528](../generate_index.py#L1528) | 1528 | `"            reason = _text_index_skip_reason(root / item.file)"` | — |
| [SRC-E599346ABE-L001529](../generate_index.py#L1529) | 1529 | `"            lines.append("` | — |
| [SRC-E599346ABE-L001530](../generate_index.py#L1530) | 1530 | `"                \"\| \""` | — |
| [SRC-E599346ABE-L001531](../generate_index.py#L1531) | 1531 | `"                + \" \| \".join("` | — |
| [SRC-E599346ABE-L001532](../generate_index.py#L1532) | 1532 | `"                    ("` | — |
| [SRC-E599346ABE-L001533](../generate_index.py#L1533) | 1533 | `"                        item.file_id,"` | — |
| [SRC-E599346ABE-L001534](../generate_index.py#L1534) | 1534 | `"                        _markdown_code_span(item.file),"` | — |
| [SRC-E599346ABE-L001535](../generate_index.py#L1535) | 1535 | `"                        str(item.size_bytes),"` | — |
| [SRC-E599346ABE-L001536](../generate_index.py#L1536) | 1536 | `"                        _markdown_cell(reason),"` | — |
| [SRC-E599346ABE-L001537](../generate_index.py#L1537) | 1537 | `"                    )"` | — |
| [SRC-E599346ABE-L001538](../generate_index.py#L1538) | 1538 | `"                )"` | — |
| [SRC-E599346ABE-L001539](../generate_index.py#L1539) | 1539 | `"                + \" \|\""` | — |
| [SRC-E599346ABE-L001540](../generate_index.py#L1540) | 1540 | `"            )"` | — |
| [SRC-E599346ABE-L001541](../generate_index.py#L1541) | 1541 | `"    else:"` | — |
| [SRC-E599346ABE-L001542](../generate_index.py#L1542) | 1542 | `"        lines.append(\"\| — \| — \| — \| لا توجد ملفات مؤهلة بالجرد الوصفي فقط. \|\")"` | — |
| [SRC-E599346ABE-L001543](../generate_index.py#L1543) | 1543 | `""` | — |
| [SRC-E599346ABE-L001544](../generate_index.py#L1544) | 1544 | `"    lines.extend("` | — |
| [SRC-E599346ABE-L001545](../generate_index.py#L1545) | 1545 | `"        ["` | — |
| [SRC-E599346ABE-L001546](../generate_index.py#L1546) | 1546 | `"            \"\","` | — |
| [SRC-E599346ABE-L001547](../generate_index.py#L1547) | 1547 | `"            \"## المسارات المستبعدة عمدًا\","` | — |
| [SRC-E599346ABE-L001548](../generate_index.py#L1548) | 1548 | `"            \"\","` | — |
| [SRC-E599346ABE-L001549](../generate_index.py#L1549) | 1549 | `"            \"يحتوي هذا السجل أسماء المسارات وأسباب الاستثناء فقط، ولا يقرأ محتوى الأسرار أو قواعد البيانات أو المجلدات المستبعدة.\","` | — |
| [SRC-E599346ABE-L001550](../generate_index.py#L1550) | 1550 | `"            \"\","` | — |
| [SRC-E599346ABE-L001551](../generate_index.py#L1551) | 1551 | `"            \"\| المسار المستبعد \| السبب \|\","` | — |
| [SRC-E599346ABE-L001552](../generate_index.py#L1552) | 1552 | `"            \"\|---\|---\|\","` | — |
| [SRC-E599346ABE-L001553](../generate_index.py#L1553) | 1553 | `"        ]"` | — |
| [SRC-E599346ABE-L001554](../generate_index.py#L1554) | 1554 | `"    )"` | — |
| [SRC-E599346ABE-L001555](../generate_index.py#L1555) | 1555 | `"    if excluded_paths:"` | — |
| [SRC-E599346ABE-L001556](../generate_index.py#L1556) | 1556 | `"        for excluded_path, reason in excluded_paths:"` | — |
| [SRC-E599346ABE-L001557](../generate_index.py#L1557) | 1557 | `"            lines.append(f\"\| {_markdown_code_span(excluded_path)} \| {_markdown_cell(reason)} \|\")"` | — |
| [SRC-E599346ABE-L001558](../generate_index.py#L1558) | 1558 | `"    else:"` | — |
| [SRC-E599346ABE-L001559](../generate_index.py#L1559) | 1559 | `"        lines.append(\"\| — \| لا توجد مسارات مستبعدة مكتشفة. \|\")"` | — |
| [SRC-E599346ABE-L001560](../generate_index.py#L1560) | 1560 | `""` | — |
| [SRC-E599346ABE-L001561](../generate_index.py#L1561) | 1561 | `"    lines.extend("` | — |
| [SRC-E599346ABE-L001562](../generate_index.py#L1562) | 1562 | `"        ["` | — |
| [SRC-E599346ABE-L001563](../generate_index.py#L1563) | 1563 | `"            \"\","` | — |
| [SRC-E599346ABE-L001564](../generate_index.py#L1564) | 1564 | `"            \"## ما تعنيه النتيجة وما لا تعنيه\","` | — |
| [SRC-E599346ABE-L001565](../generate_index.py#L1565) | 1565 | `"            \"\","` | — |
| [SRC-E599346ABE-L001566](../generate_index.py#L1566) | 1566 | `"            \"- التغطية بنسبة 100% تعني أن كل سطر منطقي في كل ملف نصي مؤهل وقابل للقراءة ضمن حد الحجم له سجل SRC فريد ورقم سطر مطابق.\","` | — |
| [SRC-E599346ABE-L001567](../generate_index.py#L1567) | 1567 | `"            \"- لا تعني أن كل مسار مستبعد أو كل ملف ثنائي/كبير مفهرس سطرًا بسطر؛ أسباب الاستبعاد مسجلة أعلاه.\","` | — |
| [SRC-E599346ABE-L001568](../generate_index.py#L1568) | 1568 | `"            \"- لا تعني اكتشاف كل عيب برمجي أو أمني أو منطقي. العيوب المعروفة التي يوسمها المطور صراحة تظهر في سجل FND داخل MASTER INDEX.\","` | — |
| [SRC-E599346ABE-L001569](../generate_index.py#L1569) | 1569 | `"            \"- الرموز غير Python مستخرجة بقواعد ساكنة تقريبية؛ استخدم فهرس السطور للوصول إلى النص الأصلي والتحقق يدويًا.\","` | — |
| [SRC-E599346ABE-L001570](../generate_index.py#L1570) | 1570 | `"            \"- المولد لا يعدّل كود التطبيق ولا يدمج الفروع؛ وظيفته بناء الأدلة والفهرس والتحقق من اتساقهما.\","` | — |
| [SRC-E599346ABE-L001571](../generate_index.py#L1571) | 1571 | `"            \"\","` | — |
| [SRC-E599346ABE-L001572](../generate_index.py#L1572) | 1572 | `"            \"[افتح MASTER INDEX](MASTER_INDEX.md) \| [افتح SOURCE LINES INDEX](SOURCE_LINES_INDEX.md)\","` | — |
| [SRC-E599346ABE-L001573](../generate_index.py#L1573) | 1573 | `"            \"\","` | — |
| [SRC-E599346ABE-L001574](../generate_index.py#L1574) | 1574 | `"        ]"` | — |
| [SRC-E599346ABE-L001575](../generate_index.py#L1575) | 1575 | `"    )"` | — |
| [SRC-E599346ABE-L001576](../generate_index.py#L1576) | 1576 | `"    return \"\\n\".join(lines)"` | — |
| [SRC-E599346ABE-L001577](../generate_index.py#L1577) | 1577 | `""` | — |
| [SRC-E599346ABE-L001578](../generate_index.py#L1578) | 1578 | `""` | — |
| [SRC-E599346ABE-L001579](../generate_index.py#L1579) | 1579 | `"def render_markdown("` | — |
| [SRC-E599346ABE-L001580](../generate_index.py#L1580) | 1580 | `"    symbols: list[IndexedSymbol],"` | — |
| [SRC-E599346ABE-L001581](../generate_index.py#L1581) | 1581 | `"    files_scanned: int,"` | — |
| [SRC-E599346ABE-L001582](../generate_index.py#L1582) | 1582 | `"    inventory: list[IndexedFile] \| None = None,"` | — |
| [SRC-E599346ABE-L001583](../generate_index.py#L1583) | 1583 | `"    static_symbols: list[IndexedMarker] \| None = None,"` | — |
| [SRC-E599346ABE-L001584](../generate_index.py#L1584) | 1584 | `"    source_lines: list[IndexedLine] \| None = None,"` | — |
| [SRC-E599346ABE-L001585](../generate_index.py#L1585) | 1585 | `"    findings: list[IndexedFinding] \| None = None,"` | — |
| [SRC-E599346ABE-L001586](../generate_index.py#L1586) | 1586 | `") -> str:"` | — |
| [SRC-E599346ABE-L001587](../generate_index.py#L1587) | 1587 | `"    \"\"\"Render the repository file, symbol, explicit-review-marker, and line-index overview.\"\"\""` | — |
| [SRC-E599346ABE-L001588](../generate_index.py#L1588) | 1588 | `"    file_inventory = inventory or []"` | — |
| [SRC-E599346ABE-L001589](../generate_index.py#L1589) | 1589 | `"    marker_inventory = static_symbols or []"` | — |
| [SRC-E599346ABE-L001590](../generate_index.py#L1590) | 1590 | `"    line_inventory = source_lines or []"` | — |
| [SRC-E599346ABE-L001591](../generate_index.py#L1591) | 1591 | `"    finding_inventory = findings or []"` | — |
| [SRC-E599346ABE-L001592](../generate_index.py#L1592) | 1592 | `"    documented_count = sum(symbol.documented is True for symbol in symbols)"` | — |
| [SRC-E599346ABE-L001593](../generate_index.py#L1593) | 1593 | `"    missing_count = sum(symbol.documented is False for symbol in symbols)"` | — |
| [SRC-E599346ABE-L001594](../generate_index.py#L1594) | 1594 | `"    not_applicable_count = sum(symbol.documented is None for symbol in symbols)"` | — |
| [SRC-E599346ABE-L001595](../generate_index.py#L1595) | 1595 | `"    lines = ["` | — |
| [SRC-E599346ABE-L001596](../generate_index.py#L1596) | 1596 | `"        \"# MASTER INDEX — Omarai\","` | — |
| [SRC-E599346ABE-L001597](../generate_index.py#L1597) | 1597 | `"        \"\","` | — |
| [SRC-E599346ABE-L001598](../generate_index.py#L1598) | 1598 | `"        \"<!-- هذا الملف مُولَّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->\","` | — |
| [SRC-E599346ABE-L001599](../generate_index.py#L1599) | 1599 | `"        \"\","` | — |
| [SRC-E599346ABE-L001600](../generate_index.py#L1600) | 1600 | `"        \"> MASTER INDEX يجمع جرد الملفات والتعريفات المسماة ووسوم المراجعة؛ SOURCE LINES INDEX يحتوي الأسطر الكاملة\","` | — |
| [SRC-E599346ABE-L001601](../generate_index.py#L1601) | 1601 | `"        \"> لكل ملف نصي مؤهل قابل للقراءة، مع معرّف سطر ورقم السطر الأصلي.\","` | — |
| [SRC-E599346ABE-L001602](../generate_index.py#L1602) | 1602 | `"        \"> استخراج الرموز غير Python تقريبي؛ أما فهرسة الأسطر فمخصصة للوصول إلى النص الموجود وليست حكمًا على صحته.\","` | — |
| [SRC-E599346ABE-L001603](../generate_index.py#L1603) | 1603 | `"        \"\","` | — |
| [SRC-E599346ABE-L001604](../generate_index.py#L1604) | 1604 | `"        \"## ملخص الفهرسة\","` | — |
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
