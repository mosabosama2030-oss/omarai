# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **035**
- سجلات الأسطر: **800**
- النطاق: SRC-69F3587825-L000016 إلى SRC-6B9B9ABE27-L000011
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## وثائق وفهرسة

### FILE-69F3587825 — [docs/search_code.py](../search_code.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-69F3587825-L000016](../search_code.py#L16) | 16 | `"import sys"` | — |
| [SRC-69F3587825-L000017](../search_code.py#L17) | 17 | `"from collections.abc import Sequence"` | — |
| [SRC-69F3587825-L000018](../search_code.py#L18) | 18 | `"from dataclasses import dataclass"` | — |
| [SRC-69F3587825-L000019](../search_code.py#L19) | 19 | `"from pathlib import Path"` | — |
| [SRC-69F3587825-L000020](../search_code.py#L20) | 20 | `"from urllib.parse import quote"` | — |
| [SRC-69F3587825-L000021](../search_code.py#L21) | 21 | `""` | — |
| [SRC-69F3587825-L000022](../search_code.py#L22) | 22 | `""` | — |
| [SRC-69F3587825-L000023](../search_code.py#L23) | 23 | `"EXCLUDED_DIRECTORIES = frozenset("` | — |
| [SRC-69F3587825-L000024](../search_code.py#L24) | 24 | `"    {"` | — |
| [SRC-69F3587825-L000025](../search_code.py#L25) | 25 | `"        \".git\","` | — |
| [SRC-69F3587825-L000026](../search_code.py#L26) | 26 | `"        \".hg\","` | — |
| [SRC-69F3587825-L000027](../search_code.py#L27) | 27 | `"        \".svn\","` | — |
| [SRC-69F3587825-L000028](../search_code.py#L28) | 28 | `"        \".venv\","` | — |
| [SRC-69F3587825-L000029](../search_code.py#L29) | 29 | `"        \"venv\","` | — |
| [SRC-69F3587825-L000030](../search_code.py#L30) | 30 | `"        \"env\","` | — |
| [SRC-69F3587825-L000031](../search_code.py#L31) | 31 | `"        \"virtualenv\","` | — |
| [SRC-69F3587825-L000032](../search_code.py#L32) | 32 | `"        \"__pycache__\","` | — |
| [SRC-69F3587825-L000033](../search_code.py#L33) | 33 | `"        \".pytest_cache\","` | — |
| [SRC-69F3587825-L000034](../search_code.py#L34) | 34 | `"        \".ruff_cache\","` | — |
| [SRC-69F3587825-L000035](../search_code.py#L35) | 35 | `"        \".mypy_cache\","` | — |
| [SRC-69F3587825-L000036](../search_code.py#L36) | 36 | `"        \".tox\","` | — |
| [SRC-69F3587825-L000037](../search_code.py#L37) | 37 | `"        \".nox\","` | — |
| [SRC-69F3587825-L000038](../search_code.py#L38) | 38 | `"        \"node_modules\","` | — |
| [SRC-69F3587825-L000039](../search_code.py#L39) | 39 | `"        \"site-packages\","` | — |
| [SRC-69F3587825-L000040](../search_code.py#L40) | 40 | `"        \"build\","` | — |
| [SRC-69F3587825-L000041](../search_code.py#L41) | 41 | `"        \"dist\","` | — |
| [SRC-69F3587825-L000042](../search_code.py#L42) | 42 | `"        \".tmp\","` | — |
| [SRC-69F3587825-L000043](../search_code.py#L43) | 43 | `"        \".idea\","` | — |
| [SRC-69F3587825-L000044](../search_code.py#L44) | 44 | `"        \".vscode\","` | — |
| [SRC-69F3587825-L000045](../search_code.py#L45) | 45 | `"        \".aws\","` | — |
| [SRC-69F3587825-L000046](../search_code.py#L46) | 46 | `"        \".secrets\","` | — |
| [SRC-69F3587825-L000047](../search_code.py#L47) | 47 | `"        \".ssh\","` | — |
| [SRC-69F3587825-L000048](../search_code.py#L48) | 48 | `"        \"credentials\","` | — |
| [SRC-69F3587825-L000049](../search_code.py#L49) | 49 | `"        \"secrets\","` | — |
| [SRC-69F3587825-L000050](../search_code.py#L50) | 50 | `"    }"` | — |
| [SRC-69F3587825-L000051](../search_code.py#L51) | 51 | `")"` | — |
| [SRC-69F3587825-L000052](../search_code.py#L52) | 52 | `"SECRET_BASENAMES = frozenset("` | — |
| [SRC-69F3587825-L000053](../search_code.py#L53) | 53 | `"    {"` | — |
| [SRC-69F3587825-L000054](../search_code.py#L54) | 54 | `"        \".env\","` | — |
| [SRC-69F3587825-L000055](../search_code.py#L55) | 55 | `"        \".env.local\","` | — |
| [SRC-69F3587825-L000056](../search_code.py#L56) | 56 | `"        \".env.production\","` | — |
| [SRC-69F3587825-L000057](../search_code.py#L57) | 57 | `"        \".env.staging\","` | — |
| [SRC-69F3587825-L000058](../search_code.py#L58) | 58 | `"        \".netrc\","` | — |
| [SRC-69F3587825-L000059](../search_code.py#L59) | 59 | `"        \".npmrc\","` | — |
| [SRC-69F3587825-L000060](../search_code.py#L60) | 60 | `"        \".pypirc\","` | — |
| [SRC-69F3587825-L000061](../search_code.py#L61) | 61 | `"        \"authorized_keys\","` | — |
| [SRC-69F3587825-L000062](../search_code.py#L62) | 62 | `"        \"client_secret.json\","` | — |
| [SRC-69F3587825-L000063](../search_code.py#L63) | 63 | `"        \"client_secrets.json\","` | — |
| [SRC-69F3587825-L000064](../search_code.py#L64) | 64 | `"        \"credentials\","` | — |
| [SRC-69F3587825-L000065](../search_code.py#L65) | 65 | `"        \"credentials.json\","` | — |
| [SRC-69F3587825-L000066](../search_code.py#L66) | 66 | `"        \"credentials.yaml\","` | — |
| [SRC-69F3587825-L000067](../search_code.py#L67) | 67 | `"        \"credentials.yml\","` | — |
| [SRC-69F3587825-L000068](../search_code.py#L68) | 68 | `"        \"id_dsa\","` | — |
| [SRC-69F3587825-L000069](../search_code.py#L69) | 69 | `"        \"id_ecdsa\","` | — |
| [SRC-69F3587825-L000070](../search_code.py#L70) | 70 | `"        \"id_ed25519\","` | — |
| [SRC-69F3587825-L000071](../search_code.py#L71) | 71 | `"        \"id_rsa\","` | — |
| [SRC-69F3587825-L000072](../search_code.py#L72) | 72 | `"        \"secrets.json\","` | — |
| [SRC-69F3587825-L000073](../search_code.py#L73) | 73 | `"        \"secrets.yaml\","` | — |
| [SRC-69F3587825-L000074](../search_code.py#L74) | 74 | `"        \"secrets.yml\","` | — |
| [SRC-69F3587825-L000075](../search_code.py#L75) | 75 | `"        \"service-account.json\","` | — |
| [SRC-69F3587825-L000076](../search_code.py#L76) | 76 | `"        \"token.json\","` | — |
| [SRC-69F3587825-L000077](../search_code.py#L77) | 77 | `"    }"` | — |
| [SRC-69F3587825-L000078](../search_code.py#L78) | 78 | `")"` | — |
| [SRC-69F3587825-L000079](../search_code.py#L79) | 79 | `"SENSITIVE_NAME_RE = re.compile("` | — |
| [SRC-69F3587825-L000080](../search_code.py#L80) | 80 | `"    r\"(?:^\|[._-])(?:secret\|secrets\|credential\|credentials\|password\|passwords\|token\|tokens\|private[_-]?key)(?:[._-]\|$)\","` | — |
| [SRC-69F3587825-L000081](../search_code.py#L81) | 81 | `"    re.IGNORECASE,"` | — |
| [SRC-69F3587825-L000082](../search_code.py#L82) | 82 | `")"` | — |
| [SRC-69F3587825-L000083](../search_code.py#L83) | 83 | `"SENSITIVE_CONFIG_SUFFIXES = frozenset("` | — |
| [SRC-69F3587825-L000084](../search_code.py#L84) | 84 | `"    {\".cfg\", \".conf\", \".ini\", \".json\", \".properties\", \".toml\", \".txt\", \".xml\", \".yaml\", \".yml\"}"` | — |
| [SRC-69F3587825-L000085](../search_code.py#L85) | 85 | `")"` | — |
| [SRC-69F3587825-L000086](../search_code.py#L86) | 86 | `"MAX_SEARCH_FILE_BYTES = 2 * 1024 * 1024"` | — |
| [SRC-69F3587825-L000087](../search_code.py#L87) | 87 | `""` | — |
| [SRC-69F3587825-L000088](../search_code.py#L88) | 88 | `""` | — |
| [SRC-69F3587825-L000089](../search_code.py#L89) | 89 | `"def _is_sensitive_path(path: Path) -> bool:"` | — |
| [SRC-69F3587825-L000090](../search_code.py#L90) | 90 | `"    \"\"\"Return whether a local path appears to contain credentials or private runtime data.\"\"\""` | — |
| [SRC-69F3587825-L000091](../search_code.py#L91) | 91 | `"    name = path.name.lower()"` | — |
| [SRC-69F3587825-L000092](../search_code.py#L92) | 92 | `"    parent_names = {part.lower() for part in path.parts[:-1]}"` | — |
| [SRC-69F3587825-L000093](../search_code.py#L93) | 93 | `"    if name in SECRET_BASENAMES or parent_names & EXCLUDED_DIRECTORIES:"` | — |
| [SRC-69F3587825-L000094](../search_code.py#L94) | 94 | `"        return True"` | — |
| [SRC-69F3587825-L000095](../search_code.py#L95) | 95 | `"    if name.startswith(\".env\") and name != \".env.example\":"` | — |
| [SRC-69F3587825-L000096](../search_code.py#L96) | 96 | `"        return True"` | — |
| [SRC-69F3587825-L000097](../search_code.py#L97) | 97 | `"    if name.endswith((\".example\", \".sample\", \".template\")):"` | — |
| [SRC-69F3587825-L000098](../search_code.py#L98) | 98 | `"        return False"` | — |
| [SRC-69F3587825-L000099](../search_code.py#L99) | 99 | `"    if SENSITIVE_NAME_RE.search(name) and path.suffix.lower() in SENSITIVE_CONFIG_SUFFIXES:"` | — |
| [SRC-69F3587825-L000100](../search_code.py#L100) | 100 | `"        return True"` | — |
| [SRC-69F3587825-L000101](../search_code.py#L101) | 101 | `"    return path.suffix.lower() in {\".db\", \".sqlite\", \".sqlite3\", \".pem\", \".key\", \".p12\", \".pfx\"}"` | — |
| [SRC-69F3587825-L000102](../search_code.py#L102) | 102 | `"DEFAULT_EXTENSIONS = frozenset("` | — |
| [SRC-69F3587825-L000103](../search_code.py#L103) | 103 | `"    {"` | — |
| [SRC-69F3587825-L000104](../search_code.py#L104) | 104 | `"        \".py\","` | — |
| [SRC-69F3587825-L000105](../search_code.py#L105) | 105 | `"        \".md\","` | — |
| [SRC-69F3587825-L000106](../search_code.py#L106) | 106 | `"        \".html\","` | — |
| [SRC-69F3587825-L000107](../search_code.py#L107) | 107 | `"        \".htm\","` | — |
| [SRC-69F3587825-L000108](../search_code.py#L108) | 108 | `"        \".js\","` | — |
| [SRC-69F3587825-L000109](../search_code.py#L109) | 109 | `"        \".css\","` | — |
| [SRC-69F3587825-L000110](../search_code.py#L110) | 110 | `"        \".json\","` | — |
| [SRC-69F3587825-L000111](../search_code.py#L111) | 111 | `"        \".yml\","` | — |
| [SRC-69F3587825-L000112](../search_code.py#L112) | 112 | `"        \".yaml\","` | — |
| [SRC-69F3587825-L000113](../search_code.py#L113) | 113 | `"        \".toml\","` | — |
| [SRC-69F3587825-L000114](../search_code.py#L114) | 114 | `"        \".txt\","` | — |
| [SRC-69F3587825-L000115](../search_code.py#L115) | 115 | `"        \".sh\","` | — |
| [SRC-69F3587825-L000116](../search_code.py#L116) | 116 | `"        \".example\","` | — |
| [SRC-69F3587825-L000117](../search_code.py#L117) | 117 | `"    }"` | — |
| [SRC-69F3587825-L000118](../search_code.py#L118) | 118 | `")"` | — |
| [SRC-69F3587825-L000119](../search_code.py#L119) | 119 | `"GITHUB_BLOB_BASE = \"https://github.com/mosabosama2030-oss/omarai/blob\""` | — |
| [SRC-69F3587825-L000120](../search_code.py#L120) | 120 | `""` | — |
| [SRC-69F3587825-L000121](../search_code.py#L121) | 121 | `""` | — |
| [SRC-69F3587825-L000122](../search_code.py#L122) | 122 | `"def default_repository_ref(root: Path) -> str:"` | — |
| [SRC-69F3587825-L000123](../search_code.py#L123) | 123 | `"    \"\"\"Choose an exact revision for source links, with an explicit operator override.\"\"\""` | — |
| [SRC-69F3587825-L000124](../search_code.py#L124) | 124 | `"    configured = os.getenv(\"OMARAI_GITHUB_REF\", \"\").strip()"` | — |
| [SRC-69F3587825-L000125](../search_code.py#L125) | 125 | `"    if configured:"` | — |
| [SRC-69F3587825-L000126](../search_code.py#L126) | 126 | `"        return configured"` | — |
| [SRC-69F3587825-L000127](../search_code.py#L127) | 127 | `"    action_sha = os.getenv(\"GITHUB_SHA\", \"\").strip()"` | — |
| [SRC-69F3587825-L000128](../search_code.py#L128) | 128 | `"    if re.fullmatch(r\"[0-9a-fA-F]{40}\", action_sha):"` | — |
| [SRC-69F3587825-L000129](../search_code.py#L129) | 129 | `"        return action_sha.lower()"` | — |
| [SRC-69F3587825-L000130](../search_code.py#L130) | 130 | `"    try:"` | — |
| [SRC-69F3587825-L000131](../search_code.py#L131) | 131 | `"        result = subprocess.run("` | — |
| [SRC-69F3587825-L000132](../search_code.py#L132) | 132 | `"            [\"git\", \"rev-parse\", \"HEAD\"],"` | — |
| [SRC-69F3587825-L000133](../search_code.py#L133) | 133 | `"            cwd=root,"` | — |
| [SRC-69F3587825-L000134](../search_code.py#L134) | 134 | `"            check=True,"` | — |
| [SRC-69F3587825-L000135](../search_code.py#L135) | 135 | `"            capture_output=True,"` | — |
| [SRC-69F3587825-L000136](../search_code.py#L136) | 136 | `"            text=True,"` | — |
| [SRC-69F3587825-L000137](../search_code.py#L137) | 137 | `"            timeout=2,"` | — |
| [SRC-69F3587825-L000138](../search_code.py#L138) | 138 | `"        )"` | — |
| [SRC-69F3587825-L000139](../search_code.py#L139) | 139 | `"    except (OSError, subprocess.SubprocessError):"` | — |
| [SRC-69F3587825-L000140](../search_code.py#L140) | 140 | `"        return \"main\""` | — |
| [SRC-69F3587825-L000141](../search_code.py#L141) | 141 | `"    revision = result.stdout.strip()"` | — |
| [SRC-69F3587825-L000142](../search_code.py#L142) | 142 | `"    return revision.lower() if re.fullmatch(r\"[0-9a-fA-F]{40}\", revision) else \"main\""` | — |
| [SRC-69F3587825-L000143](../search_code.py#L143) | 143 | `""` | — |
| [SRC-69F3587825-L000144](../search_code.py#L144) | 144 | `""` | — |
| [SRC-69F3587825-L000145](../search_code.py#L145) | 145 | `"@dataclass(frozen=True, slots=True)"` | — |
| [SRC-69F3587825-L000146](../search_code.py#L146) | 146 | `"class SearchHit:"` | — |
| [SRC-69F3587825-L000147](../search_code.py#L147) | 147 | `"    file: str"` | — |
| [SRC-69F3587825-L000148](../search_code.py#L148) | 148 | `"    line: int"` | — |
| [SRC-69F3587825-L000149](../search_code.py#L149) | 149 | `"    text: str"` | — |
| [SRC-69F3587825-L000150](../search_code.py#L150) | 150 | `"    context_before: str"` | — |
| [SRC-69F3587825-L000151](../search_code.py#L151) | 151 | `"    context_after: str"` | — |
| [SRC-69F3587825-L000152](../search_code.py#L152) | 152 | `"    repository_ref: str = \"main\""` | — |
| [SRC-69F3587825-L000153](../search_code.py#L153) | 153 | `""` | — |
| [SRC-69F3587825-L000154](../search_code.py#L154) | 154 | `"    @property"` | — |
| [SRC-69F3587825-L000155](../search_code.py#L155) | 155 | `"    def link(self) -> str:"` | — |
| [SRC-69F3587825-L000156](../search_code.py#L156) | 156 | `"        revision = quote(self.repository_ref, safe=\"/-._~\")"` | — |
| [SRC-69F3587825-L000157](../search_code.py#L157) | 157 | `"        path = quote(self.file, safe=\"/-._~\")"` | — |
| [SRC-69F3587825-L000158](../search_code.py#L158) | 158 | `"        return f\"{GITHUB_BLOB_BASE}/{revision}/{path}#L{self.line}\""` | — |
| [SRC-69F3587825-L000159](../search_code.py#L159) | 159 | `""` | — |
| [SRC-69F3587825-L000160](../search_code.py#L160) | 160 | `""` | — |
| [SRC-69F3587825-L000161](../search_code.py#L161) | 161 | `"def discover_text_files(root: Path, extensions: frozenset[str]) -> list[Path]:"` | — |
| [SRC-69F3587825-L000162](../search_code.py#L162) | 162 | `"    discovered: list[Path] = []"` | — |
| [SRC-69F3587825-L000163](../search_code.py#L163) | 163 | `"    for current_directory, directory_names, file_names in os.walk("` | — |
| [SRC-69F3587825-L000164](../search_code.py#L164) | 164 | `"        root, topdown=True, followlinks=False"` | — |
| [SRC-69F3587825-L000165](../search_code.py#L165) | 165 | `"    ):"` | — |
| [SRC-69F3587825-L000166](../search_code.py#L166) | 166 | `"        directory_names[:] = sorted("` | — |
| [SRC-69F3587825-L000167](../search_code.py#L167) | 167 | `"            name"` | — |
| [SRC-69F3587825-L000168](../search_code.py#L168) | 168 | `"            for name in directory_names"` | — |
| [SRC-69F3587825-L000169](../search_code.py#L169) | 169 | `"            if name not in EXCLUDED_DIRECTORIES"` | — |
| [SRC-69F3587825-L000170](../search_code.py#L170) | 170 | `"            and not (Path(current_directory) / name).is_symlink()"` | — |
| [SRC-69F3587825-L000171](../search_code.py#L171) | 171 | `"        )"` | — |
| [SRC-69F3587825-L000172](../search_code.py#L172) | 172 | `"        for file_name in sorted(file_names):"` | — |
| [SRC-69F3587825-L000173](../search_code.py#L173) | 173 | `"            candidate = Path(current_directory) / file_name"` | — |
| [SRC-69F3587825-L000174](../search_code.py#L174) | 174 | `"            if candidate.is_symlink() or _is_sensitive_path(candidate.relative_to(root)):"` | — |
| [SRC-69F3587825-L000175](../search_code.py#L175) | 175 | `"                continue"` | — |
| [SRC-69F3587825-L000176](../search_code.py#L176) | 176 | `"            suffix = candidate.suffix.lower()"` | — |
| [SRC-69F3587825-L000177](../search_code.py#L177) | 177 | `"            if ("` | — |
| [SRC-69F3587825-L000178](../search_code.py#L178) | 178 | `"                suffix not in extensions"` | — |
| [SRC-69F3587825-L000179](../search_code.py#L179) | 179 | `"                and not file_name.endswith(\".example\")"` | — |
| [SRC-69F3587825-L000180](../search_code.py#L180) | 180 | `"                and file_name not in {\".gitignore\", \".dockerignore\", \"Dockerfile\", \"LICENSE\"}"` | — |
| [SRC-69F3587825-L000181](../search_code.py#L181) | 181 | `"            ):"` | — |
| [SRC-69F3587825-L000182](../search_code.py#L182) | 182 | `"                continue"` | — |
| [SRC-69F3587825-L000183](../search_code.py#L183) | 183 | `"            discovered.append(candidate)"` | — |
| [SRC-69F3587825-L000184](../search_code.py#L184) | 184 | `"    return sorted(discovered, key=lambda p: p.relative_to(root).as_posix().casefold())"` | — |
| [SRC-69F3587825-L000185](../search_code.py#L185) | 185 | `""` | — |
| [SRC-69F3587825-L000186](../search_code.py#L186) | 186 | `""` | — |
| [SRC-69F3587825-L000187](../search_code.py#L187) | 187 | `"def search_repository("` | — |
| [SRC-69F3587825-L000188](../search_code.py#L188) | 188 | `"    root: Path,"` | — |
| [SRC-69F3587825-L000189](../search_code.py#L189) | 189 | `"    query: str,"` | — |
| [SRC-69F3587825-L000190](../search_code.py#L190) | 190 | `"    *,"` | — |
| [SRC-69F3587825-L000191](../search_code.py#L191) | 191 | `"    use_regex: bool = False,"` | — |
| [SRC-69F3587825-L000192](../search_code.py#L192) | 192 | `"    case_sensitive: bool = False,"` | — |
| [SRC-69F3587825-L000193](../search_code.py#L193) | 193 | `"    extensions: frozenset[str] = DEFAULT_EXTENSIONS,"` | — |
| [SRC-69F3587825-L000194](../search_code.py#L194) | 194 | `"    repository_ref: str = \"main\","` | — |
| [SRC-69F3587825-L000195](../search_code.py#L195) | 195 | `"    max_results: int = 50,"` | — |
| [SRC-69F3587825-L000196](../search_code.py#L196) | 196 | `"    context: int = 1,"` | — |
| [SRC-69F3587825-L000197](../search_code.py#L197) | 197 | `") -> list[SearchHit]:"` | — |
| [SRC-69F3587825-L000198](../search_code.py#L198) | 198 | `"    \"\"\"Return ordered text matches with short context.\"\"\""` | — |
| [SRC-69F3587825-L000199](../search_code.py#L199) | 199 | `"    if not query:"` | — |
| [SRC-69F3587825-L000200](../search_code.py#L200) | 200 | `"        raise ValueError(\"استعلام البحث فارغ.\")"` | — |
| [SRC-69F3587825-L000201](../search_code.py#L201) | 201 | `"    if max_results < 1:"` | — |
| [SRC-69F3587825-L000202](../search_code.py#L202) | 202 | `"        raise ValueError(\"max_results يجب أن يكون 1 أو أكبر.\")"` | — |
| [SRC-69F3587825-L000203](../search_code.py#L203) | 203 | `"    if context < 0:"` | — |
| [SRC-69F3587825-L000204](../search_code.py#L204) | 204 | `"        raise ValueError(\"context لا يمكن أن يكون سالبًا.\")"` | — |
| [SRC-69F3587825-L000205](../search_code.py#L205) | 205 | `""` | — |
| [SRC-69F3587825-L000206](../search_code.py#L206) | 206 | `"    flags = 0 if case_sensitive else re.IGNORECASE"` | — |
| [SRC-69F3587825-L000207](../search_code.py#L207) | 207 | `"    if use_regex:"` | — |
| [SRC-69F3587825-L000208](../search_code.py#L208) | 208 | `"        pattern = re.compile(query, flags)"` | — |
| [SRC-69F3587825-L000209](../search_code.py#L209) | 209 | `"    else:"` | — |
| [SRC-69F3587825-L000210](../search_code.py#L210) | 210 | `"        pattern = re.compile(re.escape(query), flags)"` | — |
| [SRC-69F3587825-L000211](../search_code.py#L211) | 211 | `""` | — |
| [SRC-69F3587825-L000212](../search_code.py#L212) | 212 | `"    hits: list[SearchHit] = []"` | — |
| [SRC-69F3587825-L000213](../search_code.py#L213) | 213 | `"    for path in discover_text_files(root, extensions):"` | — |
| [SRC-69F3587825-L000214](../search_code.py#L214) | 214 | `"        relative = path.relative_to(root).as_posix()"` | — |
| [SRC-69F3587825-L000215](../search_code.py#L215) | 215 | `"        try:"` | — |
| [SRC-69F3587825-L000216](../search_code.py#L216) | 216 | `"            if path.stat().st_size > MAX_SEARCH_FILE_BYTES:"` | — |
| [SRC-69F3587825-L000217](../search_code.py#L217) | 217 | `"                continue"` | — |
| [SRC-69F3587825-L000218](../search_code.py#L218) | 218 | `"            text = path.read_text(encoding=\"utf-8\")"` | — |
| [SRC-69F3587825-L000219](../search_code.py#L219) | 219 | `"        except (OSError, UnicodeDecodeError):"` | — |
| [SRC-69F3587825-L000220](../search_code.py#L220) | 220 | `"            continue"` | — |
| [SRC-69F3587825-L000221](../search_code.py#L221) | 221 | `"        lines = text.splitlines()"` | — |
| [SRC-69F3587825-L000222](../search_code.py#L222) | 222 | `"        for index, line in enumerate(lines):"` | — |
| [SRC-69F3587825-L000223](../search_code.py#L223) | 223 | `"            if pattern.search(line):"` | — |
| [SRC-69F3587825-L000224](../search_code.py#L224) | 224 | `"                before = \"\\n\".join(lines[max(0, index - context) : index]) if context else \"\""` | — |
| [SRC-69F3587825-L000225](../search_code.py#L225) | 225 | `"                after = ("` | — |
| [SRC-69F3587825-L000226](../search_code.py#L226) | 226 | `"                    \"\\n\".join(lines[index + 1 : min(len(lines), index + 1 + context)])"` | — |
| [SRC-69F3587825-L000227](../search_code.py#L227) | 227 | `"                    if context"` | — |
| [SRC-69F3587825-L000228](../search_code.py#L228) | 228 | `"                    else \"\""` | — |
| [SRC-69F3587825-L000229](../search_code.py#L229) | 229 | `"                )"` | — |
| [SRC-69F3587825-L000230](../search_code.py#L230) | 230 | `"                hits.append("` | — |
| [SRC-69F3587825-L000231](../search_code.py#L231) | 231 | `"                    SearchHit("` | — |
| [SRC-69F3587825-L000232](../search_code.py#L232) | 232 | `"                        file=relative,"` | — |
| [SRC-69F3587825-L000233](../search_code.py#L233) | 233 | `"                        line=index + 1,"` | — |
| [SRC-69F3587825-L000234](../search_code.py#L234) | 234 | `"                        text=line.rstrip(),"` | — |
| [SRC-69F3587825-L000235](../search_code.py#L235) | 235 | `"                        context_before=before.rstrip(),"` | — |
| [SRC-69F3587825-L000236](../search_code.py#L236) | 236 | `"                        context_after=after.rstrip(),"` | — |
| [SRC-69F3587825-L000237](../search_code.py#L237) | 237 | `"                        repository_ref=repository_ref,"` | — |
| [SRC-69F3587825-L000238](../search_code.py#L238) | 238 | `"                    )"` | — |
| [SRC-69F3587825-L000239](../search_code.py#L239) | 239 | `"                )"` | — |
| [SRC-69F3587825-L000240](../search_code.py#L240) | 240 | `"                if len(hits) >= max_results:"` | — |
| [SRC-69F3587825-L000241](../search_code.py#L241) | 241 | `"                    return hits"` | — |
| [SRC-69F3587825-L000242](../search_code.py#L242) | 242 | `"    return hits"` | — |
| [SRC-69F3587825-L000243](../search_code.py#L243) | 243 | `""` | — |
| [SRC-69F3587825-L000244](../search_code.py#L244) | 244 | `""` | — |
| [SRC-69F3587825-L000245](../search_code.py#L245) | 245 | `"def format_hits(hits: list[SearchHit]) -> str:"` | — |
| [SRC-69F3587825-L000246](../search_code.py#L246) | 246 | `"    if not hits:"` | — |
| [SRC-69F3587825-L000247](../search_code.py#L247) | 247 | `"        return \"لا توجد نتائج.\""` | — |
| [SRC-69F3587825-L000248](../search_code.py#L248) | 248 | `"    blocks: list[str] = []"` | — |
| [SRC-69F3587825-L000249](../search_code.py#L249) | 249 | `"    for hit in hits:"` | — |
| [SRC-69F3587825-L000250](../search_code.py#L250) | 250 | `"        blocks.append("` | — |
| [SRC-69F3587825-L000251](../search_code.py#L251) | 251 | `"            f\"{hit.file}:{hit.line}\\n\""` | — |
| [SRC-69F3587825-L000252](../search_code.py#L252) | 252 | `"            f\"  {hit.text}\\n\""` | — |
| [SRC-69F3587825-L000253](../search_code.py#L253) | 253 | `"            f\"  → {hit.link}\""` | — |
| [SRC-69F3587825-L000254](../search_code.py#L254) | 254 | `"        )"` | — |
| [SRC-69F3587825-L000255](../search_code.py#L255) | 255 | `"        if hit.context_before:"` | — |
| [SRC-69F3587825-L000256](../search_code.py#L256) | 256 | `"            blocks[-1] += \"\\n\" + \"\\n\".join("` | — |
| [SRC-69F3587825-L000257](../search_code.py#L257) | 257 | `"                f\"  · {line}\" for line in hit.context_before.splitlines()"` | — |
| [SRC-69F3587825-L000258](../search_code.py#L258) | 258 | `"            )"` | — |
| [SRC-69F3587825-L000259](../search_code.py#L259) | 259 | `"        if hit.context_after:"` | — |
| [SRC-69F3587825-L000260](../search_code.py#L260) | 260 | `"            blocks[-1] += \"\\n\" + \"\\n\".join("` | — |
| [SRC-69F3587825-L000261](../search_code.py#L261) | 261 | `"                f\"  · {line}\" for line in hit.context_after.splitlines()"` | — |
| [SRC-69F3587825-L000262](../search_code.py#L262) | 262 | `"            )"` | — |
| [SRC-69F3587825-L000263](../search_code.py#L263) | 263 | `"    return \"\\n\\n\".join(blocks)"` | — |
| [SRC-69F3587825-L000264](../search_code.py#L264) | 264 | `""` | — |
| [SRC-69F3587825-L000265](../search_code.py#L265) | 265 | `""` | — |
| [SRC-69F3587825-L000266](../search_code.py#L266) | 266 | `"def main(argv: Sequence[str] \| None = None) -> int:"` | — |
| [SRC-69F3587825-L000267](../search_code.py#L267) | 267 | `"    parser = argparse.ArgumentParser("` | — |
| [SRC-69F3587825-L000268](../search_code.py#L268) | 268 | `"        description=\"بحث نصي داخل ملفات مستودع Omarai (بدون خدمات خارجية).\""` | — |
| [SRC-69F3587825-L000269](../search_code.py#L269) | 269 | `"    )"` | — |
| [SRC-69F3587825-L000270](../search_code.py#L270) | 270 | `"    parser.add_argument(\"query\", help=\"النص أو التعبير المنتظم للبحث.\")"` | — |
| [SRC-69F3587825-L000271](../search_code.py#L271) | 271 | `"    parser.add_argument("` | — |
| [SRC-69F3587825-L000272](../search_code.py#L272) | 272 | `"        \"--root\","` | — |
| [SRC-69F3587825-L000273](../search_code.py#L273) | 273 | `"        type=Path,"` | — |
| [SRC-69F3587825-L000274](../search_code.py#L274) | 274 | `"        default=Path(__file__).resolve().parents[1],"` | — |
| [SRC-69F3587825-L000275](../search_code.py#L275) | 275 | `"        help=\"جذر المستودع.\","` | — |
| [SRC-69F3587825-L000276](../search_code.py#L276) | 276 | `"    )"` | — |
| [SRC-69F3587825-L000277](../search_code.py#L277) | 277 | `"    parser.add_argument(\"--regex\", action=\"store_true\", help=\"تفسير الاستعلام كتعبير منتظم.\")"` | — |
| [SRC-69F3587825-L000278](../search_code.py#L278) | 278 | `"    parser.add_argument(\"--case-sensitive\", action=\"store_true\", help=\"مطابقة حساسة لحالة الأحرف.\")"` | — |
| [SRC-69F3587825-L000279](../search_code.py#L279) | 279 | `"    parser.add_argument("` | — |
| [SRC-69F3587825-L000280](../search_code.py#L280) | 280 | `"        \"--ext\","` | — |
| [SRC-69F3587825-L000281](../search_code.py#L281) | 281 | `"        action=\"append\","` | — |
| [SRC-69F3587825-L000282](../search_code.py#L282) | 282 | `"        default=[],"` | — |
| [SRC-69F3587825-L000283](../search_code.py#L283) | 283 | `"        help=\"امتداد ملف للبحث (يمكن تكراره)، مثل: --ext py --ext html\","` | — |
| [SRC-69F3587825-L000284](../search_code.py#L284) | 284 | `"    )"` | — |
| [SRC-69F3587825-L000285](../search_code.py#L285) | 285 | `"    parser.add_argument(\"--max\", type=int, default=50, help=\"أقصى عدد نتائج (افتراضي 50).\")"` | — |
| [SRC-69F3587825-L000286](../search_code.py#L286) | 286 | `"    parser.add_argument("` | — |
| [SRC-69F3587825-L000287](../search_code.py#L287) | 287 | `"        \"--context\","` | — |
| [SRC-69F3587825-L000288](../search_code.py#L288) | 288 | `"        type=int,"` | — |
| [SRC-69F3587825-L000289](../search_code.py#L289) | 289 | `"        default=0,"` | — |
| [SRC-69F3587825-L000290](../search_code.py#L290) | 290 | `"        help=\"عدد أسطر السياق قبل/بعد.\","` | — |
| [SRC-69F3587825-L000291](../search_code.py#L291) | 291 | `"    )"` | — |
| [SRC-69F3587825-L000292](../search_code.py#L292) | 292 | `"    parser.add_argument("` | — |
| [SRC-69F3587825-L000293](../search_code.py#L293) | 293 | `"        \"--ref\","` | — |
| [SRC-69F3587825-L000294](../search_code.py#L294) | 294 | `"        default=None,"` | — |
| [SRC-69F3587825-L000295](../search_code.py#L295) | 295 | `"        help=\"مرجع GitHub للروابط (SHA أو فرع). افتراضيًا يُستخدم SHA المحلي/بيئة CI ثم main كخيار أخير.\","` | — |
| [SRC-69F3587825-L000296](../search_code.py#L296) | 296 | `"    )"` | — |
| [SRC-69F3587825-L000297](../search_code.py#L297) | 297 | `"    args = parser.parse_args(argv)"` | — |
| [SRC-69F3587825-L000298](../search_code.py#L298) | 298 | `""` | — |
| [SRC-69F3587825-L000299](../search_code.py#L299) | 299 | `"    try:"` | — |
| [SRC-69F3587825-L000300](../search_code.py#L300) | 300 | `"        root = args.root.resolve(strict=True)"` | — |
| [SRC-69F3587825-L000301](../search_code.py#L301) | 301 | `"        extensions = ("` | — |
| [SRC-69F3587825-L000302](../search_code.py#L302) | 302 | `"            frozenset(f\".{ext.lstrip('.')}\" for ext in args.ext)"` | — |
| [SRC-69F3587825-L000303](../search_code.py#L303) | 303 | `"            if args.ext"` | — |
| [SRC-69F3587825-L000304](../search_code.py#L304) | 304 | `"            else DEFAULT_EXTENSIONS"` | — |
| [SRC-69F3587825-L000305](../search_code.py#L305) | 305 | `"        )"` | — |
| [SRC-69F3587825-L000306](../search_code.py#L306) | 306 | `"        repository_ref = args.ref.strip() if isinstance(args.ref, str) and args.ref.strip() else default_repository_ref(root)"` | — |
| [SRC-69F3587825-L000307](../search_code.py#L307) | 307 | `"        hits = search_repository("` | — |
| [SRC-69F3587825-L000308](../search_code.py#L308) | 308 | `"            root,"` | — |
| [SRC-69F3587825-L000309](../search_code.py#L309) | 309 | `"            args.query,"` | — |
| [SRC-69F3587825-L000310](../search_code.py#L310) | 310 | `"            use_regex=args.regex,"` | — |
| [SRC-69F3587825-L000311](../search_code.py#L311) | 311 | `"            case_sensitive=args.case_sensitive,"` | — |
| [SRC-69F3587825-L000312](../search_code.py#L312) | 312 | `"            extensions=extensions,"` | — |
| [SRC-69F3587825-L000313](../search_code.py#L313) | 313 | `"            repository_ref=repository_ref,"` | — |
| [SRC-69F3587825-L000314](../search_code.py#L314) | 314 | `"            max_results=max(1, args.max),"` | — |
| [SRC-69F3587825-L000315](../search_code.py#L315) | 315 | `"            context=max(0, args.context),"` | — |
| [SRC-69F3587825-L000316](../search_code.py#L316) | 316 | `"        )"` | — |
| [SRC-69F3587825-L000317](../search_code.py#L317) | 317 | `"    except (OSError, ValueError, re.error) as exc:"` | — |
| [SRC-69F3587825-L000318](../search_code.py#L318) | 318 | `"        print(f\"خطأ في البحث: {exc}\", file=sys.stderr)"` | — |
| [SRC-69F3587825-L000319](../search_code.py#L319) | 319 | `"        return 1"` | — |
| [SRC-69F3587825-L000320](../search_code.py#L320) | 320 | `""` | — |
| [SRC-69F3587825-L000321](../search_code.py#L321) | 321 | `"    print(format_hits(hits))"` | — |
| [SRC-69F3587825-L000322](../search_code.py#L322) | 322 | `"    print(f\"\\n# عدد النتائج: {len(hits)}\")"` | — |
| [SRC-69F3587825-L000323](../search_code.py#L323) | 323 | `"    return 0"` | — |
| [SRC-69F3587825-L000324](../search_code.py#L324) | 324 | `""` | — |
| [SRC-69F3587825-L000325](../search_code.py#L325) | 325 | `""` | — |
| [SRC-69F3587825-L000326](../search_code.py#L326) | 326 | `"if __name__ == \"__main__\":"` | — |
| [SRC-69F3587825-L000327](../search_code.py#L327) | 327 | `"    raise SystemExit(main())"` | — |
## وثائق وفهرسة

### FILE-BBB7222984 — [docs/superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-BBB7222984-L000001](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L1) | 1 | `"# Unified Hybrid Research Pipeline Implementation Plan"` | — |
| [SRC-BBB7222984-L000002](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L2) | 2 | `""` | — |
| [SRC-BBB7222984-L000003](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L3) | 3 | ``"> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking."`` | — |
| [SRC-BBB7222984-L000004](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L4) | 4 | `""` | — |
| [SRC-BBB7222984-L000005](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L5) | 5 | `"**Goal:** Route Omarai's context, intent, task interpretation, aspect extraction, query planning, and evidence matching through one bounded, auditable orchestration function."` | — |
| [SRC-BBB7222984-L000006](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L6) | 6 | `""` | — |
| [SRC-BBB7222984-L000007](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L7) | 7 | ``"**Architecture:** Add `agents/research_pipeline.py` as a coordinator over existing modules. Reuse the same coordinator from `research.py` and `web_agent.py`; keep the optional semantic scorer injected and disabled unless explicitly supplied, while retaining current source/claim guardrails."`` | — |
| [SRC-BBB7222984-L000008](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L8) | 8 | `""` | — |
| [SRC-BBB7222984-L000009](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L9) | 9 | `"**Tech Stack:** Python 3.11+, existing stdlib and Omarai modules, pytest, Ruff."` | — |
| [SRC-BBB7222984-L000010](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L10) | 10 | `""` | — |
| [SRC-BBB7222984-L000011](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L11) | 11 | ``"**Spec:** `docs/superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md`"`` | — |
| [SRC-BBB7222984-L000012](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L12) | 12 | `""` | — |
| [SRC-BBB7222984-L000013](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L13) | 13 | `"## Global Constraints"` | — |
| [SRC-BBB7222984-L000014](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L14) | 14 | `"- No new runtime dependencies."` | — |
| [SRC-BBB7222984-L000015](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L15) | 15 | `"- Maximum 8 aspects and 8 planned queries."` | — |
| [SRC-BBB7222984-L000016](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L16) | 16 | `"- No additional LLM/provider calls or paid services."` | — |
| [SRC-BBB7222984-L000017](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L17) | 17 | `"- No change to API, database, secrets, hosting, or deployment."` | — |
| [SRC-BBB7222984-L000018](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L18) | 18 | `"- Lexical and semantic relevance are candidate-ranking signals, never proof of claim truth."` | — |
| [SRC-BBB7222984-L000019](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L19) | 19 | `"- Preserve existing request budgets, source guardrails, citation validation, and clarification behavior."` | — |
| [SRC-BBB7222984-L000020](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L20) | 20 | `""` | — |
| [SRC-BBB7222984-L000021](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L21) | 21 | `"## Review Focus"` | — |
| [SRC-BBB7222984-L000022](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L22) | 22 | `"- Ambiguous follow-up without an anchor must remain CLARIFY and produce no search queries."` | — |
| [SRC-BBB7222984-L000023](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L23) | 23 | `"- A chained follow-up must preserve the latest substantive topic without reviving stale topics."` | — |
| [SRC-BBB7222984-L000024](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L24) | 24 | `"- Arabic compound questions with multiple criteria must keep each explicit aspect within the query cap."` | — |
| [SRC-BBB7222984-L000025](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L25) | 25 | `"- Empty/malformed sources and malformed optional semantic scores must fail closed without exceptions."` | — |
| [SRC-BBB7222984-L000026](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L26) | 26 | `"- Missing semantic scorer must be explicitly marked unassessed, not as a successful semantic match."` | — |
| [SRC-BBB7222984-L000027](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L27) | 27 | `""` | — |
| [SRC-BBB7222984-L000028](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L28) | 28 | `"---"` | — |
| [SRC-BBB7222984-L000029](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L29) | 29 | `""` | — |
| [SRC-BBB7222984-L000030](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L30) | 30 | `"### Task 1: Add the unified orchestration contract"` | — |
| [SRC-BBB7222984-L000031](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L31) | 31 | `""` | — |
| [SRC-BBB7222984-L000032](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L32) | 32 | `"**Files:**"` | — |
| [SRC-BBB7222984-L000033](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L33) | 33 | ``"- Create: `agents/research_pipeline.py`"`` | — |
| [SRC-BBB7222984-L000034](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L34) | 34 | ``"- Test: `tests/test_research_pipeline.py`"`` | — |
| [SRC-BBB7222984-L000035](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L35) | 35 | `""` | — |
| [SRC-BBB7222984-L000036](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L36) | 36 | `"**Interfaces:**"` | — |
| [SRC-BBB7222984-L000037](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L37) | 37 | ``"- `build_research_pipeline(question, plan=None, *, history=None, mode=\"auto\", intent_route=\"\", dialogue_context=None, sources=None, compact_fn=None, semantic_matcher=None) -> dict[str, Any]`"`` | — |
| [SRC-BBB7222984-L000038](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L38) | 38 | ``"- Returns bounded `contextual_question`, `intent`, `task_spec`, `aspects`, `query_strategy_matrix`, `queries`, `evidence_ledger`, and stage-status diagnostics."`` | — |
| [SRC-BBB7222984-L000039](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L39) | 39 | `""` | — |
| [SRC-BBB7222984-L000040](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L40) | 40 | `"- [ ] Write tests for explicit aspect preservation, clarification without a referent, evidence-ledger semantics, and safe optional-scorer fallback."` | — |
| [SRC-BBB7222984-L000041](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L41) | 41 | `"- [ ] Run targeted tests and observe failure before implementation."` | — |
| [SRC-BBB7222984-L000042](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L42) | 42 | `"- [ ] Implement the coordinator using existing modules only."` | — |
| [SRC-BBB7222984-L000043](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L43) | 43 | `"- [ ] Run targeted tests and Ruff."` | — |
| [SRC-BBB7222984-L000044](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L44) | 44 | `""` | — |
| [SRC-BBB7222984-L000045](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L45) | 45 | `"### Task 2: Integrate plan construction"` | — |
| [SRC-BBB7222984-L000046](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L46) | 46 | `""` | — |
| [SRC-BBB7222984-L000047](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L47) | 47 | `"**Files:**"` | — |
| [SRC-BBB7222984-L000048](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L48) | 48 | ``"- Modify: `agents/research.py::_attach_task_understanding`"`` | — |
| [SRC-BBB7222984-L000049](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L49) | 49 | ``"- Modify: `agents/web_agent.py` planning block around TaskSpec and query strategy construction."`` | — |
| [SRC-BBB7222984-L000050](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L50) | 50 | ``"- Test: `tests/test_research.py`, `tests/test_web_agent.py`, `tests/test_research_pipeline.py`"`` | — |
| [SRC-BBB7222984-L000051](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L51) | 51 | `""` | — |
| [SRC-BBB7222984-L000052](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L52) | 52 | `"- [ ] Add regression coverage proving both fallback and WebAgent plans use the shared pipeline."` | — |
| [SRC-BBB7222984-L000053](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L53) | 53 | `"- [ ] Replace duplicated TaskSpec/matrix assembly with the coordinator."` | — |
| [SRC-BBB7222984-L000054](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L54) | 54 | `"- [ ] Preserve the existing query budget and mode-specific prioritization."` | — |
| [SRC-BBB7222984-L000055](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L55) | 55 | `"- [ ] Run targeted integration tests."` | — |
| [SRC-BBB7222984-L000056](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L56) | 56 | `""` | — |
| [SRC-BBB7222984-L000057](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L57) | 57 | `"### Task 3: Integrate post-retrieval matching diagnostics"` | — |
| [SRC-BBB7222984-L000058](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L58) | 58 | `""` | — |
| [SRC-BBB7222984-L000059](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L59) | 59 | `"**Files:**"` | — |
| [SRC-BBB7222984-L000060](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L60) | 60 | ``"- Modify: `agents/web_agent.py` after source collection and before answer generation."`` | — |
| [SRC-BBB7222984-L000061](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L61) | 61 | ``"- Test: `tests/test_research_pipeline.py`, `tests/test_web_agent.py`"`` | — |
| [SRC-BBB7222984-L000062](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L62) | 62 | `""` | — |
| [SRC-BBB7222984-L000063](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L63) | 63 | `"- [ ] Add a test showing each explicit aspect gets a lexical evidence ledger entry and missing aspects remain visible."` | — |
| [SRC-BBB7222984-L000064](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L64) | 64 | `"- [ ] Attach pipeline evidence diagnostics to the existing research report without changing source acceptance or claim-verification rules."` | — |
| [SRC-BBB7222984-L000065](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L65) | 65 | ``"- [ ] Ensure semantic status remains `not_configured` unless an injected scorer returns validated bounded scores."`` | — |
| [SRC-BBB7222984-L000066](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L66) | 66 | `"- [ ] Run the full relevant test set."` | — |
| [SRC-BBB7222984-L000067](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L67) | 67 | `""` | — |
| [SRC-BBB7222984-L000068](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L68) | 68 | `"### Task 4: Verify and document"` | — |
| [SRC-BBB7222984-L000069](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L69) | 69 | `""` | — |
| [SRC-BBB7222984-L000070](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L70) | 70 | `"**Files:**"` | — |
| [SRC-BBB7222984-L000071](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L71) | 71 | ``"- Update: `docs/OMARAI_REMEDIATION_REGISTER_AR.md` only if its current structure supports a non-duplicative entry."`` | — |
| [SRC-BBB7222984-L000072](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L72) | 72 | `"- Update: this design/plan with actual evidence."` | — |
| [SRC-BBB7222984-L000073](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L73) | 73 | `""` | — |
| [SRC-BBB7222984-L000074](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L74) | 74 | `"- [ ] Run CI on the final PR head."` | — |
| [SRC-BBB7222984-L000075](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L75) | 75 | `"- [ ] Inspect the complete PR diff and workflow results."` | — |
| [SRC-BBB7222984-L000076](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L76) | 76 | `"- [ ] Record untested hosted behavior as NOT_RUN."` | — |
| [SRC-BBB7222984-L000077](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L77) | 77 | `"- [ ] Leave PR open and unmerged for Human Director review."` | — |
| [SRC-BBB7222984-L000078](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L78) | 78 | `""` | — |
| [SRC-BBB7222984-L000079](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L79) | 79 | `""` | — |
| [SRC-BBB7222984-L000080](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L80) | 80 | `"## تنفيذ موثق — 2026-10-30"` | — |
| [SRC-BBB7222984-L000081](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L81) | 81 | `""` | — |
| [SRC-BBB7222984-L000082](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L82) | 82 | ``"- **RED:** GitHub Actions run [41055101051](https://github.com/mosabosama2030-oss/omarai/actions/runs/41055101051) فشل أثناء جمع الاختبارات بسبب غياب `agents.research_pipeline` قبل تنفيذ الوحدة، كما هو متوقع من اختبار العقد الأولي."`` | — |
| [SRC-BBB7222984-L000083](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L83) | 83 | ``"- **تصحيح أثناء التنفيذ:** ظهر Ruff أن `build_task_spec` و`build_query_strategy_matrix` ما زالا مستخدمين في مسارات أخرى داخل `web_agent.py`؛ أُعيد الاحتفاظ بالاستيراد هناك، وحُذفت الاستيرادات غير المستخدمة من `research.py`. فشل آخر في الاختبار كشف أن اختبار مهلة المقيّم لم يستخرج محاور متعددة، ثم صُحح الاختبار ليستخدم سؤالًا مركبًا. وبعدها صحح عدد الاستثناءات المتوقع ليتناسب مع عدد المحاور."`` | — |
| [SRC-BBB7222984-L000084](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L84) | 84 | ``"- **GREEN / CI:** run [41056403423](https://github.com/mosabosama2030-oss/omarai/actions/runs/41056403423) على code SHA `c68595cb0f38b3d1d64add600eb0172209980dea` نجح:"`` | — |
| [SRC-BBB7222984-L000085](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L85) | 85 | `"  - Python 3.11: **623 passed**."` | — |
| [SRC-BBB7222984-L000086](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L86) | 86 | `"  - Python 3.12: **623 passed**."` | — |
| [SRC-BBB7222984-L000087](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L87) | 87 | `"  - Ruff: All checks passed."` | — |
| [SRC-BBB7222984-L000088](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L88) | 88 | `"  - Generated-index verification: success."` | — |
| [SRC-BBB7222984-L000089](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L89) | 89 | `"  - Production container build + protected API smoke: success."` | — |
| [SRC-BBB7222984-L000090](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L90) | 90 | ``"- رأس PR الحالي بعد أتمتة الفهرسة: `c10dcf63420b57365d10fdeda0a5be7aaaa4b84c`. المقارنة من code-tested SHA تُظهر تغييرات فهرسة مولدة فقط، دون تغييرات runtime أو tests."`` | — |
| [SRC-BBB7222984-L000091](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L91) | 91 | ``"- **الحد المتبقي:** لا يوجد semantic scorer موصول افتراضيًا في WebAgent؛ يسجل المسار `not_configured`. واجهة المقيّم الاختيارية موجودة ومختبرة للفشل، لكن لا ندّعي مطابقة دلالية حية أو تحسينًا مقاسًا. لا hosted acceptance أو بحث حي أو استدعاءات مدفوعة."`` | — |
| [SRC-BBB7222984-L000092](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L92) | 92 | `"- **الحالة:** PR #132 Draft/Open/Not merged؛ لا دمج ولا نشر."` | — |
| [SRC-BBB7222984-L000093](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L93) | 93 | `""` | — |
| [SRC-BBB7222984-L000094](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L94) | 94 | `""` | — |
| [SRC-BBB7222984-L000095](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L95) | 95 | `"### مراجعة نهائية بعد إعادة بناء TaskSpec — 2026-10-30"` | — |
| [SRC-BBB7222984-L000096](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L96) | 96 | ``"- أظهرت مراجعة الكود أن إعادة استخدام TaskSpec المسبق بعد توليد الخطة قد تُسقط `planner_depth` و`planner_freshness`. أُلغي هذا الاختصار، وأُبقي بناء TaskSpec النهائي داخل المنسق بعد توفر بيانات الخطة، مع بقاء preflight يمر عبر المنسق نفسه."`` | — |
| [SRC-BBB7222984-L000097](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L97) | 97 | `"- اختبار انحدار جديد يثبت حفظ بيانات عمق وحداثة خطة البحث."` | — |
| [SRC-BBB7222984-L000098](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L98) | 98 | ``"- **التحقق النهائي للكود:** run [41056744662](https://github.com/mosabosama2030-oss/omarai/actions/runs/41056744662) على SHA `b72168a6fbf360f5fc088fe125a4ad9623fdb958`:"`` | — |
| [SRC-BBB7222984-L000099](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L99) | 99 | `"  - Python 3.11: **623 passed**."` | — |
| [SRC-BBB7222984-L000100](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L100) | 100 | `"  - Python 3.12: **623 passed**."` | — |
| [SRC-BBB7222984-L000101](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L101) | 101 | `"  - Ruff: All checks passed."` | — |
| [SRC-BBB7222984-L000102](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L102) | 102 | `"  - Docker build وProtected API Smoke: success."` | — |
| [SRC-BBB7222984-L000103](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L103) | 103 | ``"- PR head بعد تحديث الفهارس والوثائق: `ce7e32f11b0612c3519f89f670eee0a143e94fc8`. التغييرات بعد SHA المختبر هي ملفات الفهرسة المولدة فقط؛ لا تغييرات كود أو اختبارات بعد التشغيل الناجح."`` | — |
| [SRC-BBB7222984-L000104](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L104) | 104 | `""` | — |
| [SRC-BBB7222984-L000105](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L105) | 105 | `""` | — |
| [SRC-BBB7222984-L000106](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L106) | 106 | `"### بوابة التوضيح الإلزامي — 2026-10-30"` | — |
| [SRC-BBB7222984-L000107](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L107) | 107 | ``"- أُضيف منع لتخطيط/تنفيذ الاستعلامات عندما يقرر TaskSpec أن مدخلًا إلزاميًا مفقود، حتى إذا وصل مسار بحث upstream مثل `WEB_SIMPLE`."`` | — |
| [SRC-BBB7222984-L000108](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L108) | 108 | ``"- اختبار `هات الموقع الرسمي` دون اسم جهة يثبت أن الاستيضاح يوقف الاستعلامات."`` | — |
| [SRC-BBB7222984-L000109](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L109) | 109 | ``"- **آخر تحقق للكود:** run [41057068443](https://github.com/mosabosama2030-oss/omarai/actions/runs/41057068443) على SHA `6ebcb720a6ef1166fdd2ef672a00c4e01ba4cfda`:"`` | — |
| [SRC-BBB7222984-L000110](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L110) | 110 | `"  - Python 3.11: **624 passed**."` | — |
| [SRC-BBB7222984-L000111](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L111) | 111 | `"  - Python 3.12: **624 passed**."` | — |
| [SRC-BBB7222984-L000112](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L112) | 112 | `"  - Ruff: All checks passed."` | — |
| [SRC-BBB7222984-L000113](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L113) | 113 | `"  - Docker build + Protected API Smoke: success."` | — |
| [SRC-BBB7222984-L000114](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L114) | 114 | ``"- رأس PR بعد أتمتة الفهرسة: `51c459d329239b6386d2f79529a046e2759d5dad`; الفارق عن SHA المختبر يقتصر على ملفات الفهرسة المولدة."`` | — |
| [SRC-BBB7222984-L000115](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L115) | 115 | `""` | — |
| [SRC-BBB7222984-L000116](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L116) | 116 | `"### تدقيق دعم الاستشهادات وحالة الإكمال — 2026-10-30"` | — |
| [SRC-BBB7222984-L000117](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L117) | 117 | `""` | — |
| [SRC-BBB7222984-L000118](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L118) | 118 | ``"- **السبب الجذري:** `build_research_completion` كان يسمح بحالة `answer_generated_citations_range_checked_semantic_support_unverified` حتى عند وجود إشارات تحذير من فحص دعم الاستشهاد، مثل رقم لا يظهر في المصدر المشار إليه أو تداخل لفظي ضعيف. كما أن بعض مسارات بناء النتائج المبكرة كانت تحتفظ بـ`pipeline_completion_status=completed` رغم أن التدقيق النهائي رصد تحذيرًا في دعم الاستشهاد."`` | — |
| [SRC-BBB7222984-L000119](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L119) | 119 | ``"- **التعديل:** تُجمع مؤشرات الأرقام غير المدعومة (العامة وبحسب المصدر المشار إليه) والتداخل اللفظي الضعيف في `citation_support_warning_count` مع تجنب احتساب الرقم نفسه مرتين. تؤدي هذه الإشارات إلى حالة إكمال جزئية، وتظهر أعدادها ومرحلة فحصها في `research_completion`."`` | — |
| [SRC-BBB7222984-L000120](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L120) | 120 | ``"- **اتساق الحالة:** بعد التدقيق النهائي، يزامن `WebAgent.answer` الحالة العامة وتقرير البحث إلى `partial` عند وجود تحذير فعلي من فحص دعم الاستشهاد، أو عند غياب علامات الاستشهاد الصالحة. لا يُخفض الحالة بسبب إشارات تغطية أخرى لا تعني وحدها وجود ضعف في الاستشهاد."`` | — |
| [SRC-BBB7222984-L000121](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L121) | 121 | `"- **TDD RED:** الاختبار الجديد كشف أن التحذير لا يمنع حالة الإكمال السابقة: run [41088936951](https://github.com/mosabosama2030-oss/omarai/actions/runs/41088936951)، **1 failed / 628 passed** على Python 3.11 و3.12."` | — |
| [SRC-BBB7222984-L000122](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L122) | 122 | ``"- **TDD GREEN والتحقق النهائي للكود:** run [41089965289](https://github.com/mosabosama2030-oss/omarai/actions/runs/41089965289) على SHA `4f18f27999b3dfab3995d086a171313941960609`:"`` | — |
| [SRC-BBB7222984-L000123](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L123) | 123 | `"  - Python 3.11: **629 passed**."` | — |
| [SRC-BBB7222984-L000124](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L124) | 124 | `"  - Python 3.12: **629 passed**."` | — |
| [SRC-BBB7222984-L000125](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L125) | 125 | `"  - Ruff: All checks passed."` | — |
| [SRC-BBB7222984-L000126](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L126) | 126 | `"  - Container build: success."` | — |
| [SRC-BBB7222984-L000127](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L127) | 127 | `"  - Protected API Smoke: success."` | — |
| [SRC-BBB7222984-L000128](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L128) | 128 | `"- **مراجعة الانحدار:** أُبقي اختبار النجاح الإيجابي بمصدر يتطابق نصيًا مع الجملة المستشهد بها، واختبار التحذير يغطي رقمًا غير مدعوم واستشهادًا ضعيف التداخل. هذه الإشارات فحوص لفظية تحفظية وليست إثباتًا دلاليًا."` | — |
| [SRC-BBB7222984-L000129](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L129) | 129 | ``"- **الحدود:** `semantic_verification` ما زالت `not_performed`؛ لم نضف نموذج تحقق دلالي مستقلًا، ولم نختبر الاستضافة الحية أو محركات البحث الحية."`` | — |
| [SRC-BBB7222984-L000130](../superpowers/plans/2026-10-30-unified-hybrid-research-pipeline.md#L130) | 130 | `"- **الحالة:** PR #132 ما زال Draft/Open/Not merged؛ لم يحدث دمج أو نشر."` | — |
## وثائق وفهرسة

### FILE-002F33CFDC — [docs/superpowers/plans/2026-11-05-default-workspace-home.md](../superpowers/plans/2026-11-05-default-workspace-home.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-002F33CFDC-L000001](../superpowers/plans/2026-11-05-default-workspace-home.md#L1) | 1 | `"# Make Omarai Sales Workspace the Default Home — Implementation Plan"` | — |
| [SRC-002F33CFDC-L000002](../superpowers/plans/2026-11-05-default-workspace-home.md#L2) | 2 | `""` | — |
| [SRC-002F33CFDC-L000003](../superpowers/plans/2026-11-05-default-workspace-home.md#L3) | 3 | ``"**Goal:** Serve the approved Arabic RTL Neon Command sales workspace at `/` while preserving the research agent at `/agent` and the legacy lead page at `/leads`."`` | — |
| [SRC-002F33CFDC-L000004](../superpowers/plans/2026-11-05-default-workspace-home.md#L4) | 4 | `""` | — |
| [SRC-002F33CFDC-L000005](../superpowers/plans/2026-11-05-default-workspace-home.md#L5) | 5 | ``"**Architecture:** Reuse the existing `web/workspace.html` and its existing authenticated APIs. Change only route selection and navigation/documentation; do not add backend capabilities, storage models, providers, or database migrations."`` | — |
| [SRC-002F33CFDC-L000006](../superpowers/plans/2026-11-05-default-workspace-home.md#L6) | 6 | `""` | — |
| [SRC-002F33CFDC-L000007](../superpowers/plans/2026-11-05-default-workspace-home.md#L7) | 7 | `"**Tech Stack:** Python 3.12 stdlib HTTP server, static HTML/CSS/JavaScript, pytest, existing GitHub Actions workflows."` | — |
| [SRC-002F33CFDC-L000008](../superpowers/plans/2026-11-05-default-workspace-home.md#L8) | 8 | `""` | — |
| [SRC-002F33CFDC-L000009](../superpowers/plans/2026-11-05-default-workspace-home.md#L9) | 9 | ``"**Spec:** Existing approved workspace in `web/workspace.html`, current sales-intelligence architecture, and repository instructions in `AGENTS.md`."`` | — |
| [SRC-002F33CFDC-L000010](../superpowers/plans/2026-11-05-default-workspace-home.md#L10) | 10 | `""` | — |
| [SRC-002F33CFDC-L000011](../superpowers/plans/2026-11-05-default-workspace-home.md#L11) | 11 | `"## Global Constraints"` | — |
| [SRC-002F33CFDC-L000012](../superpowers/plans/2026-11-05-default-workspace-home.md#L12) | 12 | ``"- Keep `/api/session`, `/api/leads`, `/api/analyze`, `/api/health`, and logout contracts unchanged."`` | — |
| [SRC-002F33CFDC-L000013](../superpowers/plans/2026-11-05-default-workspace-home.md#L13) | 13 | ``"- Keep `/workspace` as a backward-compatible alias."`` | — |
| [SRC-002F33CFDC-L000014](../superpowers/plans/2026-11-05-default-workspace-home.md#L14) | 14 | ``"- Preserve `/agent` as the general web-research interface and `/leads` as the legacy lead UI."`` | — |
| [SRC-002F33CFDC-L000015](../superpowers/plans/2026-11-05-default-workspace-home.md#L15) | 15 | `"- Do not enable menu modules that do not have real server-side contracts."` | — |
| [SRC-002F33CFDC-L000016](../superpowers/plans/2026-11-05-default-workspace-home.md#L16) | 16 | `"- Keep same-origin HttpOnly browser sessions; never persist access tokens in localStorage or sessionStorage."` | — |
| [SRC-002F33CFDC-L000017](../superpowers/plans/2026-11-05-default-workspace-home.md#L17) | 17 | `"- No production deployment, secret changes, provider calls, database changes, or PR merge."` | — |
| [SRC-002F33CFDC-L000018](../superpowers/plans/2026-11-05-default-workspace-home.md#L18) | 18 | `""` | — |
| [SRC-002F33CFDC-L000019](../superpowers/plans/2026-11-05-default-workspace-home.md#L19) | 19 | `"## Review Focus"` | — |
| [SRC-002F33CFDC-L000020](../superpowers/plans/2026-11-05-default-workspace-home.md#L20) | 20 | `"- Root page must not silently remove access to the general research agent."` | — |
| [SRC-002F33CFDC-L000021](../superpowers/plans/2026-11-05-default-workspace-home.md#L21) | 21 | `"- Workspace's \"وكيل البحث\" navigation must not link back to the new root page."` | — |
| [SRC-002F33CFDC-L000022](../superpowers/plans/2026-11-05-default-workspace-home.md#L22) | 22 | `"- Existing workspace API/session and legacy lead paths must remain reachable."` | — |
| [SRC-002F33CFDC-L000023](../superpowers/plans/2026-11-05-default-workspace-home.md#L23) | 23 | `"- UI-only modules without backend contracts must remain explicitly unavailable."` | — |
| [SRC-002F33CFDC-L000024](../superpowers/plans/2026-11-05-default-workspace-home.md#L24) | 24 | `"- The root route must return Arabic RTL HTML and not a stale redirect."` | — |
| [SRC-002F33CFDC-L000025](../superpowers/plans/2026-11-05-default-workspace-home.md#L25) | 25 | `""` | — |
| [SRC-002F33CFDC-L000026](../superpowers/plans/2026-11-05-default-workspace-home.md#L26) | 26 | `"---"` | — |
| [SRC-002F33CFDC-L000027](../superpowers/plans/2026-11-05-default-workspace-home.md#L27) | 27 | `""` | — |
| [SRC-002F33CFDC-L000028](../superpowers/plans/2026-11-05-default-workspace-home.md#L28) | 28 | `"### Task 1: Pin the intended route behavior"` | — |
| [SRC-002F33CFDC-L000029](../superpowers/plans/2026-11-05-default-workspace-home.md#L29) | 29 | `""` | — |
| [SRC-002F33CFDC-L000030](../superpowers/plans/2026-11-05-default-workspace-home.md#L30) | 30 | `"**Files:**"` | — |
| [SRC-002F33CFDC-L000031](../superpowers/plans/2026-11-05-default-workspace-home.md#L31) | 31 | ``"- Modify: `tests/test_api.py`"`` | — |
| [SRC-002F33CFDC-L000032](../superpowers/plans/2026-11-05-default-workspace-home.md#L32) | 32 | `""` | — |
| [SRC-002F33CFDC-L000033](../superpowers/plans/2026-11-05-default-workspace-home.md#L33) | 33 | `"**Interfaces:**"` | — |
| [SRC-002F33CFDC-L000034](../superpowers/plans/2026-11-05-default-workspace-home.md#L34) | 34 | ``"- `GET /` and `GET /workspace` return the same sales-workspace HTML."`` | — |
| [SRC-002F33CFDC-L000035](../superpowers/plans/2026-11-05-default-workspace-home.md#L35) | 35 | ``"- `GET /agent` returns the existing research-agent HTML."`` | — |
| [SRC-002F33CFDC-L000036](../superpowers/plans/2026-11-05-default-workspace-home.md#L36) | 36 | ``"- `GET /leads` returns the existing legacy lead HTML."`` | — |
| [SRC-002F33CFDC-L000037](../superpowers/plans/2026-11-05-default-workspace-home.md#L37) | 37 | `""` | — |
| [SRC-002F33CFDC-L000038](../superpowers/plans/2026-11-05-default-workspace-home.md#L38) | 38 | `"- [ ] Rewrite the existing route integration test to assert the new home contract and preserve all three secondary paths."` | — |
| [SRC-002F33CFDC-L000039](../superpowers/plans/2026-11-05-default-workspace-home.md#L39) | 39 | `"- [ ] Commit the test first and inspect GitHub Actions for the expected RED result against the old route behavior."` | — |
| [SRC-002F33CFDC-L000040](../superpowers/plans/2026-11-05-default-workspace-home.md#L40) | 40 | `""` | — |
| [SRC-002F33CFDC-L000041](../superpowers/plans/2026-11-05-default-workspace-home.md#L41) | 41 | `"### Task 2: Route the home page to the approved workspace"` | — |
| [SRC-002F33CFDC-L000042](../superpowers/plans/2026-11-05-default-workspace-home.md#L42) | 42 | `""` | — |
| [SRC-002F33CFDC-L000043](../superpowers/plans/2026-11-05-default-workspace-home.md#L43) | 43 | `"**Files:**"` | — |
| [SRC-002F33CFDC-L000044](../superpowers/plans/2026-11-05-default-workspace-home.md#L44) | 44 | ``"- Modify: `api/omarai.py`"`` | — |
| [SRC-002F33CFDC-L000045](../superpowers/plans/2026-11-05-default-workspace-home.md#L45) | 45 | ``"- Modify: `web/workspace.html`"`` | — |
| [SRC-002F33CFDC-L000046](../superpowers/plans/2026-11-05-default-workspace-home.md#L46) | 46 | `""` | — |
| [SRC-002F33CFDC-L000047](../superpowers/plans/2026-11-05-default-workspace-home.md#L47) | 47 | ``"- [ ] Serve `/agent` from `agent.html` only."`` | — |
| [SRC-002F33CFDC-L000048](../superpowers/plans/2026-11-05-default-workspace-home.md#L48) | 48 | ``"- [ ] Serve both `/` and `/workspace` from `workspace.html`."`` | — |
| [SRC-002F33CFDC-L000049](../superpowers/plans/2026-11-05-default-workspace-home.md#L49) | 49 | ``"- [ ] Point the workspace's \"وكيل البحث\" link to `/agent`."`` | — |
| [SRC-002F33CFDC-L000050](../superpowers/plans/2026-11-05-default-workspace-home.md#L50) | 50 | `"- [ ] Preserve all API and authorization behavior."` | — |
| [SRC-002F33CFDC-L000051](../superpowers/plans/2026-11-05-default-workspace-home.md#L51) | 51 | `""` | — |
| [SRC-002F33CFDC-L000052](../superpowers/plans/2026-11-05-default-workspace-home.md#L52) | 52 | `"### Task 3: Align documentation and handoff"` | — |
| [SRC-002F33CFDC-L000053](../superpowers/plans/2026-11-05-default-workspace-home.md#L53) | 53 | `""` | — |
| [SRC-002F33CFDC-L000054](../superpowers/plans/2026-11-05-default-workspace-home.md#L54) | 54 | `"**Files:**"` | — |
| [SRC-002F33CFDC-L000055](../superpowers/plans/2026-11-05-default-workspace-home.md#L55) | 55 | ``"- Modify: `README.md`"`` | — |
| [SRC-002F33CFDC-L000056](../superpowers/plans/2026-11-05-default-workspace-home.md#L56) | 56 | ``"- Modify: `docs/IMPLEMENTATION_SCOPE.md`"`` | — |
| [SRC-002F33CFDC-L000057](../superpowers/plans/2026-11-05-default-workspace-home.md#L57) | 57 | `""` | — |
| [SRC-002F33CFDC-L000058](../superpowers/plans/2026-11-05-default-workspace-home.md#L58) | 58 | `"- [ ] Document the sales workspace as the default home and the research/legacy pages as retained routes."` | — |
| [SRC-002F33CFDC-L000059](../superpowers/plans/2026-11-05-default-workspace-home.md#L59) | 59 | `"- [ ] State clearly that modules without server-side contracts remain unavailable."` | — |
| [SRC-002F33CFDC-L000060](../superpowers/plans/2026-11-05-default-workspace-home.md#L60) | 60 | `""` | — |
| [SRC-002F33CFDC-L000061](../superpowers/plans/2026-11-05-default-workspace-home.md#L61) | 61 | `"### Task 4: Verify"` | — |
| [SRC-002F33CFDC-L000062](../superpowers/plans/2026-11-05-default-workspace-home.md#L62) | 62 | `""` | — |
| [SRC-002F33CFDC-L000063](../superpowers/plans/2026-11-05-default-workspace-home.md#L63) | 63 | ``"- [ ] Run `pytest tests/test_api.py tests/test_dashboard_security.py -q`."`` | — |
| [SRC-002F33CFDC-L000064](../superpowers/plans/2026-11-05-default-workspace-home.md#L64) | 64 | ``"- [ ] Run the full `pytest -q` suite and `ruff check .` where available."`` | — |
| [SRC-002F33CFDC-L000065](../superpowers/plans/2026-11-05-default-workspace-home.md#L65) | 65 | `"- [ ] Confirm GitHub Actions on the final branch SHA."` | — |
| [SRC-002F33CFDC-L000066](../superpowers/plans/2026-11-05-default-workspace-home.md#L66) | 66 | ``"- [ ] Review the full diff, create a PR against `main`, and leave merge/deploy to the Human Director."`` | — |
## وثائق وفهرسة

### FILE-676B69CB6C — [docs/superpowers/plans/2026-11-06-workspace-demand-discovery.md](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-676B69CB6C-L000001](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L1) | 1 | `"# Workspace Product Profile & Demand Discovery Implementation Plan"` | — |
| [SRC-676B69CB6C-L000002](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L2) | 2 | `""` | — |
| [SRC-676B69CB6C-L000003](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L3) | 3 | `"> **For agentic workers:** Use the repository's TDD workflow task-by-task. Steps use checkbox syntax."` | — |
| [SRC-676B69CB6C-L000004](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L4) | 4 | `""` | — |
| [SRC-676B69CB6C-L000005](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L5) | 5 | `"**Goal:** Connect the new Arabic RTL workspace to a tenant-scoped product profile, real buyer-intent discovery, persisted discovery evidence, and human-reviewed signal saving."` | — |
| [SRC-676B69CB6C-L000006](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L6) | 6 | `""` | — |
| [SRC-676B69CB6C-L000007](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L7) | 7 | ``"**Architecture:** Add small tenant-scoped SQLite records and protected endpoints, reuse the existing `sales_domain` and `WebAgent` pipeline, and expose the workflow through the existing workspace. Do not duplicate search logic or enable paid/optional providers by default."`` | — |
| [SRC-676B69CB6C-L000008](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L8) | 8 | `""` | — |
| [SRC-676B69CB6C-L000009](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L9) | 9 | `"**Tech Stack:** Python 3.12, stdlib HTTP server, SQLite, static HTML/JavaScript, pytest, GitHub Actions."` | — |
| [SRC-676B69CB6C-L000010](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L10) | 10 | `""` | — |
| [SRC-676B69CB6C-L000011](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L11) | 11 | ``"**Spec:** `docs/superpowers/specs/2026-11-06-workspace-demand-discovery-design.md` and `docs/OMARAI_SALES_INTELLIGENCE_ARCHITECTURE_AR.md`."`` | — |
| [SRC-676B69CB6C-L000012](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L12) | 12 | `""` | — |
| [SRC-676B69CB6C-L000013](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L13) | 13 | `"## Global Constraints"` | — |
| [SRC-676B69CB6C-L000014](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L14) | 14 | ``"- Work only on `feat/workspace-demand-discovery-2026-11-06`, based on current main SHA `a297abd271d48f459effad083a9f424a1499cd39`."`` | — |
| [SRC-676B69CB6C-L000015](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L15) | 15 | ``"- Never trust a client-supplied `tenant_id`; use the authenticated principal."`` | — |
| [SRC-676B69CB6C-L000016](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L16) | 16 | `"- Viewer is read-only and cannot run discovery or write product data."` | — |
| [SRC-676B69CB6C-L000017](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L17) | 17 | `"- Paid/optional search providers must stay disabled by default in this workflow."` | — |
| [SRC-676B69CB6C-L000018](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L18) | 18 | ``"- Save a source as a demand signal only when the server-side stored run labels it `public_demand_signal`."`` | — |
| [SRC-676B69CB6C-L000019](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L19) | 19 | `"- Preserve publication date, event date, and observation time as distinct/unknown where not supplied."` | — |
| [SRC-676B69CB6C-L000020](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L20) | 20 | `"- No secrets, hosting configuration changes, production deployment, or PR merge."` | — |
| [SRC-676B69CB6C-L000021](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L21) | 21 | `"- Do not activate UI modules without real API contracts."` | — |
| [SRC-676B69CB6C-L000022](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L22) | 22 | `""` | — |
| [SRC-676B69CB6C-L000023](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L23) | 23 | `"## Review Focus"` | — |
| [SRC-676B69CB6C-L000024](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L24) | 24 | `"- Cross-tenant product-profile/run access using guessed IDs."` | — |
| [SRC-676B69CB6C-L000025](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L25) | 25 | `"- Viewer attempts to create profiles, discover, or save a signal."` | — |
| [SRC-676B69CB6C-L000026](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L26) | 26 | `"- Malformed arrays, oversized product text, invalid locale, empty query plan, and duplicate product profiles."` | — |
| [SRC-676B69CB6C-L000027](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L27) | 27 | `"- Optional connectors with configured API keys but no explicit per-run owner approval."` | — |
| [SRC-676B69CB6C-L000028](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L28) | 28 | `"- Discovery results containing related listings, negative intent, or no qualified buyer signal."` | — |
| [SRC-676B69CB6C-L000029](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L29) | 29 | `"- Browser attempting to save an unrelated result or alter a server-side qualification label."` | — |
| [SRC-676B69CB6C-L000030](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L30) | 30 | `""` | — |
| [SRC-676B69CB6C-L000031](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L31) | 31 | `"---"` | — |
| [SRC-676B69CB6C-L000032](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L32) | 32 | `""` | — |
| [SRC-676B69CB6C-L000033](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L33) | 33 | `"### Task 1: Pin storage and API contracts with failing tests"` | — |
| [SRC-676B69CB6C-L000034](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L34) | 34 | `""` | — |
| [SRC-676B69CB6C-L000035](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L35) | 35 | `"**Files:**"` | — |
| [SRC-676B69CB6C-L000036](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L36) | 36 | ``"- Modify: `tests/test_api.py`"`` | — |
| [SRC-676B69CB6C-L000037](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L37) | 37 | ``"- Modify: `tests/test_sales_domain.py`"`` | — |
| [SRC-676B69CB6C-L000038](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L38) | 38 | ``"- Create: `tests/test_workspace_discovery.py`"`` | — |
| [SRC-676B69CB6C-L000039](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L39) | 39 | `""` | — |
| [SRC-676B69CB6C-L000040](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L40) | 40 | `"**Interfaces:**"` | — |
| [SRC-676B69CB6C-L000041](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L41) | 41 | ``"- Product profile data uses `ProductProfile` plus `MarketProfile` serialization."`` | — |
| [SRC-676B69CB6C-L000042](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L42) | 42 | `"- API response records are tenant-scoped and never accept a tenant identifier from the browser."` | — |
| [SRC-676B69CB6C-L000043](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L43) | 43 | ``"- Save endpoint accepts a stored `run_id` and source index, not a client-supplied source payload."`` | — |
| [SRC-676B69CB6C-L000044](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L44) | 44 | `""` | — |
| [SRC-676B69CB6C-L000045](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L45) | 45 | `"- [x] Add tests for tenant-scoped create/list/get of product profiles."` | — |
| [SRC-676B69CB6C-L000046](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L46) | 46 | `"- [x] Add tests for discovery run creation/list/get and tenant isolation."` | — |
| [SRC-676B69CB6C-L000047](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L47) | 47 | ``"- [x] Add tests proving only a stored source marked `public_demand_signal` can be saved."`` | — |
| [SRC-676B69CB6C-L000048](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L48) | 48 | `"- [x] Add tests for viewer denial, unauthenticated denial in public mode, invalid profile values, and duplicate profile behavior."` | — |
| [SRC-676B69CB6C-L000049](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L49) | 49 | `"- [x] Run focused tests to verify expected RED (missing contracts)."` | — |
| [SRC-676B69CB6C-L000050](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L50) | 50 | `""` | — |
| [SRC-676B69CB6C-L000051](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L51) | 51 | `"### Task 2: Add tenant-scoped storage"` | — |
| [SRC-676B69CB6C-L000052](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L52) | 52 | `""` | — |
| [SRC-676B69CB6C-L000053](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L53) | 53 | `"**Files:**"` | — |
| [SRC-676B69CB6C-L000054](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L54) | 54 | ``"- Modify: `agents/omarai.py`"`` | — |
| [SRC-676B69CB6C-L000055](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L55) | 55 | ``"- Modify: `tests/test_workspace_discovery.py`"`` | — |
| [SRC-676B69CB6C-L000056](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L56) | 56 | `""` | — |
| [SRC-676B69CB6C-L000057](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L57) | 57 | `"**Interfaces:**"` | — |
| [SRC-676B69CB6C-L000058](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L58) | 58 | ``"- `LeadStore.save_product_profile(profile: dict, *, tenant_id: str) -> dict`"`` | — |
| [SRC-676B69CB6C-L000059](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L59) | 59 | ``"- `LeadStore.list_product_profiles(*, tenant_id: str) -> list[dict]`"`` | — |
| [SRC-676B69CB6C-L000060](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L60) | 60 | ``"- `LeadStore.get_product_profile(profile_id: str, *, tenant_id: str) -> dict \| None`"`` | — |
| [SRC-676B69CB6C-L000061](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L61) | 61 | ``"- `LeadStore.save_discovery_run(profile_id: str, run: dict, *, tenant_id: str) -> dict`"`` | — |
| [SRC-676B69CB6C-L000062](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L62) | 62 | ``"- `LeadStore.list_discovery_runs(*, tenant_id: str, limit: int = 50) -> list[dict]`"`` | — |
| [SRC-676B69CB6C-L000063](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L63) | 63 | ``"- `LeadStore.get_discovery_run(run_id: str, *, tenant_id: str) -> dict \| None`"`` | — |
| [SRC-676B69CB6C-L000064](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L64) | 64 | ``"- `LeadStore.save_discovery_signal(run_id: str, source_index: int, *, tenant_id: str) -> tuple[dict, bool] \| None`"`` | — |
| [SRC-676B69CB6C-L000065](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L65) | 65 | `""` | — |
| [SRC-676B69CB6C-L000066](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L66) | 66 | ``"- [x] Add `product_profiles` table with tenant-scoped uniqueness and index."`` | — |
| [SRC-676B69CB6C-L000067](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L67) | 67 | ``"- [x] Add `discovery_runs` table with tenant-scoped profile foreign key and index."`` | — |
| [SRC-676B69CB6C-L000068](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L68) | 68 | `"- [x] Store only bounded public response fields; never model prompts or secrets."` | — |
| [SRC-676B69CB6C-L000069](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L69) | 69 | `"- [x] Save leads only by loading the source from the stored run and verifying its server-side qualification label."` | — |
| [SRC-676B69CB6C-L000070](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L70) | 70 | `"- [x] Run storage tests and existing LeadStore tests."` | — |
| [SRC-676B69CB6C-L000071](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L71) | 71 | `""` | — |
| [SRC-676B69CB6C-L000072](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L72) | 72 | `"### Task 3: Connect structured buyer discovery to WebAgent"` | — |
| [SRC-676B69CB6C-L000073](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L73) | 73 | `""` | — |
| [SRC-676B69CB6C-L000074](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L74) | 74 | `"**Files:**"` | — |
| [SRC-676B69CB6C-L000075](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L75) | 75 | ``"- Modify: `agents/web_agent.py`"`` | — |
| [SRC-676B69CB6C-L000076](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L76) | 76 | ``"- Create/modify: `tests/test_workspace_discovery.py`"`` | — |
| [SRC-676B69CB6C-L000077](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L77) | 77 | `""` | — |
| [SRC-676B69CB6C-L000078](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L78) | 78 | `"**Interfaces:**"` | — |
| [SRC-676B69CB6C-L000079](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L79) | 79 | ``"- Extend `WebAgent.answer(..., buyer_queries: list[str] \| None = None)`."`` | — |
| [SRC-676B69CB6C-L000080](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L80) | 80 | ``"- Extend internal `_answer_with_budget(..., buyer_queries: list[str] \| None = None)`."`` | — |
| [SRC-676B69CB6C-L000081](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L81) | 81 | ``"- Preserve existing callers when `buyer_queries` is omitted."`` | — |
| [SRC-676B69CB6C-L000082](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L82) | 82 | ``"- Add per-instance `allow_optional_providers` control, defaulting to existing behavior for legacy routes."`` | — |
| [SRC-676B69CB6C-L000083](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L83) | 83 | `""` | — |
| [SRC-676B69CB6C-L000084](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L84) | 84 | `"- [x] Force the lead-generation route only when structured buyer queries are supplied by the new discovery endpoint."` | — |
| [SRC-676B69CB6C-L000085](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L85) | 85 | `"- [x] Validate and cap buyer query count/length (1–8 queries, max 500 characters each)."` | — |
| [SRC-676B69CB6C-L000086](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L86) | 86 | ``"- [x] Prefer structured queries over prose-derived `_lead_generation_queries`."`` | — |
| [SRC-676B69CB6C-L000087](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L87) | 87 | `"- [x] Gate DeepSeek, Brave, Tavily, and optional social APIs when the per-instance control is false."` | — |
| [SRC-676B69CB6C-L000088](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L88) | 88 | `"- [x] Keep DDG/Bing/Google News and public no-key social retrieval under existing bounded controls."` | — |
| [SRC-676B69CB6C-L000089](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L89) | 89 | `"- [x] Add tests that structured product/location queries reach the lead-generation path and optional providers are not invoked by default."` | — |
| [SRC-676B69CB6C-L000090](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L90) | 90 | `""` | — |
| [SRC-676B69CB6C-L000091](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L91) | 91 | `"### Task 4: Implement protected API contracts"` | — |
| [SRC-676B69CB6C-L000092](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L92) | 92 | `""` | — |
| [SRC-676B69CB6C-L000093](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L93) | 93 | `"**Files:**"` | — |
| [SRC-676B69CB6C-L000094](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L94) | 94 | ``"- Modify: `api/omarai.py`"`` | — |
| [SRC-676B69CB6C-L000095](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L95) | 95 | ``"- Modify: `tests/test_api.py`"`` | — |
| [SRC-676B69CB6C-L000096](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L96) | 96 | `""` | — |
| [SRC-676B69CB6C-L000097](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L97) | 97 | `"**Interfaces:**"` | — |
| [SRC-676B69CB6C-L000098](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L98) | 98 | ``"- `GET /api/product-profiles`"`` | — |
| [SRC-676B69CB6C-L000099](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L99) | 99 | ``"- `POST /api/product-profiles`"`` | — |
| [SRC-676B69CB6C-L000100](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L100) | 100 | ``"- `GET /api/discoveries`"`` | — |
| [SRC-676B69CB6C-L000101](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L101) | 101 | ``"- `GET /api/discoveries/{run_id}`"`` | — |
| [SRC-676B69CB6C-L000102](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L102) | 102 | ``"- `POST /api/discoveries`"`` | — |
| [SRC-676B69CB6C-L000103](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L103) | 103 | ``"- `POST /api/discoveries/{run_id}/signals/{source_index}/save`"`` | — |
| [SRC-676B69CB6C-L000104](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L104) | 104 | `""` | — |
| [SRC-676B69CB6C-L000105](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L105) | 105 | ``"- [x] Validate request JSON arrays and bounded field sizes through `ProductProfile` and `MarketProfile`."`` | — |
| [SRC-676B69CB6C-L000106](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L106) | 106 | ``"- [x] Derive all tenant scope from `self._authenticated_principal`."`` | — |
| [SRC-676B69CB6C-L000107](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L107) | 107 | `"- [x] Require a non-viewer role to create profiles or run discovery."` | — |
| [SRC-676B69CB6C-L000108](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L108) | 108 | ``"- [x] Require owner role plus explicit `allow_optional_providers=true` to enable optional providers."`` | — |
| [SRC-676B69CB6C-L000109](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L109) | 109 | ``"- [x] Build a product-anchored prompt and queries through `build_buyer_queries`."`` | — |
| [SRC-676B69CB6C-L000110](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L110) | 110 | `"- [x] Persist the bounded discovery response and return its run ID."` | — |
| [SRC-676B69CB6C-L000111](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L111) | 111 | `"- [x] Return 404 for run/profile IDs outside the current tenant."` | — |
| [SRC-676B69CB6C-L000112](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L112) | 112 | ``"- [x] Route save requests through `LeadStore.save_discovery_signal`; never trust browser-provided source qualification."`` | — |
| [SRC-676B69CB6C-L000113](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L113) | 113 | `"- [x] Run API integration/security tests."` | — |
| [SRC-676B69CB6C-L000114](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L114) | 114 | `""` | — |
| [SRC-676B69CB6C-L000115](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L115) | 115 | `"### Task 5: Connect the RTL workspace"` | — |
| [SRC-676B69CB6C-L000116](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L116) | 116 | `""` | — |
| [SRC-676B69CB6C-L000117](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L117) | 117 | `"**Files:**"` | — |
| [SRC-676B69CB6C-L000118](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L118) | 118 | ``"- Modify: `web/workspace.html`"`` | — |
| [SRC-676B69CB6C-L000119](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L119) | 119 | ``"- Modify: `tests/test_dashboard_security.py`"`` | — |
| [SRC-676B69CB6C-L000120](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L120) | 120 | ``"- Modify: `tests/test_api.py` (if static-route contract coverage is located here)"`` | — |
| [SRC-676B69CB6C-L000121](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L121) | 121 | `""` | — |
| [SRC-676B69CB6C-L000122](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L122) | 122 | `"**Interfaces:**"` | — |
| [SRC-676B69CB6C-L000123](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L123) | 123 | ``"- Activate `offer` (Product Profile) and `campaign` (Demand Discovery) only."`` | — |
| [SRC-676B69CB6C-L000124](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L124) | 124 | `"- Read product profiles and discovery runs from their authenticated APIs."` | — |
| [SRC-676B69CB6C-L000125](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L125) | 125 | `"- Save selected qualified signals using the stored discovery run ID and source index."` | — |
| [SRC-676B69CB6C-L000126](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L126) | 126 | `""` | — |
| [SRC-676B69CB6C-L000127](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L127) | 127 | `"- [x] Add product profile editor with aliases, use cases, problems solved, locations, industries, customer types, decision roles, and exclusions."` | — |
| [SRC-676B69CB6C-L000128](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L128) | 128 | `"- [x] Add discovery screen to choose a saved profile, run search, show prior run history, and inspect evidence."` | — |
| [SRC-676B69CB6C-L000129](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L129) | 129 | `"- [x] Display qualified buyer signals separately from related-but-unqualified results."` | — |
| [SRC-676B69CB6C-L000130](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L130) | 130 | `"- [x] Show evidence phrase, evidence basis (snippet/page text/title), source link, and publication-date unknown states."` | — |
| [SRC-676B69CB6C-L000131](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L131) | 131 | `"- [x] Add explicit unchecked opt-in for optional providers; owner-only on the server with cost/quota disclosure."` | — |
| [SRC-676B69CB6C-L000132](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L132) | 132 | `"- [x] Add save action only for server-qualified public demand signals; then refresh leads and pipeline."` | — |
| [SRC-676B69CB6C-L000133](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L133) | 133 | ``"- [x] Fix the placeholder's general research navigation to `/agent`."`` | — |
| [SRC-676B69CB6C-L000134](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L134) | 134 | `"- [x] Keep all other unimplemented modules visibly unavailable."` | — |
| [SRC-676B69CB6C-L000135](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L135) | 135 | `"- [x] Run workspace static/security tests."` | — |
| [SRC-676B69CB6C-L000136](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L136) | 136 | `""` | — |
| [SRC-676B69CB6C-L000137](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L137) | 137 | `"### Task 6: Documentation, CI, review, and handoff"` | — |
| [SRC-676B69CB6C-L000138](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L138) | 138 | `""` | — |
| [SRC-676B69CB6C-L000139](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L139) | 139 | `"**Files:**"` | — |
| [SRC-676B69CB6C-L000140](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L140) | 140 | ``"- Modify: `docs/IMPLEMENTATION_SCOPE.md`"`` | — |
| [SRC-676B69CB6C-L000141](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L141) | 141 | ``"- Modify: `README.md` only if current product capabilities description needs updating."`` | — |
| [SRC-676B69CB6C-L000142](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L142) | 142 | ``"- Modify: `docs/OMARAI_REQUIREMENTS_REGISTER.md` for material requirement status/evidence, if exact owners can be identified without rewriting the historical baseline."`` | — |
| [SRC-676B69CB6C-L000143](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L143) | 143 | `""` | — |
| [SRC-676B69CB6C-L000144](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L144) | 144 | `"- [x] Verify full pytest, Ruff on Python 3.11/3.12, Docker build, public-startup credential gate, and protected API smoke through GitHub Actions."` | — |
| [SRC-676B69CB6C-L000145](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L145) | 145 | `"- [x] Inspect the 11-file PR diff and scan it for common secret/token patterns; no matches or generated-index changes were found."` | — |
| [SRC-676B69CB6C-L000146](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L146) | 146 | `"- [x] Record live provider tests, post-deploy hosted acceptance, browser E2E, and persistence on SnapDeploy as NOT_RUN/UNKNOWN."` | — |
| [SRC-676B69CB6C-L000147](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L147) | 147 | ``"- [x] Open PR #155 against `main`; leave merge and SnapDeploy deployment to the Human Director."`` | — |
| [SRC-676B69CB6C-L000148](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L148) | 148 | `""` | — |
| [SRC-676B69CB6C-L000149](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L149) | 149 | `"## Expected delivery boundary"` | — |
| [SRC-676B69CB6C-L000150](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L150) | 150 | `""` | — |
| [SRC-676B69CB6C-L000151](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L151) | 151 | `"This plan enables a first real vertical slice: saved product/market profile → buyer-intent search → persisted evidence results → human-reviewed qualified signal → existing leads pipeline. It does **not** claim that company profiles, market analytics, scheduled monitoring, outbound messaging, audit center, or the remaining disabled modules are complete."` | — |
| [SRC-676B69CB6C-L000152](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L152) | 152 | `""` | — |
| [SRC-676B69CB6C-L000153](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L153) | 153 | `""` | — |
| [SRC-676B69CB6C-L000154](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L154) | 154 | `"## Final execution and verification note"` | — |
| [SRC-676B69CB6C-L000155](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L155) | 155 | `""` | — |
| [SRC-676B69CB6C-L000156](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L156) | 156 | ``"- Final code head (before the documentation-only evidence refresh): `1f30370a0808d9ac52b75f630544c1041d5d5fca`."`` | — |
| [SRC-676B69CB6C-L000157](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L157) | 157 | ``"- TDD regression was observed: run [42190588227](https://github.com/mosabosama2030-oss/omarai/actions/runs/42190588227) reported **866 passed, 1 failed**; the only failure was the new assertion that bootstrap must use `Promise.allSettled`."`` | — |
| [SRC-676B69CB6C-L000158](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L158) | 158 | ``"- Implemented the fix in `web/workspace.html`: verify the session separately, load three data resources with `Promise.allSettled`, reset failed resource state to avoid stale data, preserve the authenticated workspace on non-auth data failures, and surface a partial-data warning. A 401 still reopens the login gate."`` | — |
| [SRC-676B69CB6C-L000159](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L159) | 159 | ``"- Successful CI [42190782142](https://github.com/mosabosama2030-oss/omarai/actions/runs/42190782142) on `1f30370a0808d9ac52b75f630544c1041d5d5fca`: **867 passed on Python 3.11 (45.17s)**, **867 passed on Python 3.12 (43.61s)**, Ruff passed on both, generated-index checks passed, Docker build passed, public-container credential gate passed, and protected API smoke passed."`` | — |
| [SRC-676B69CB6C-L000160](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L160) | 160 | `"- No local pytest command, live search/model call, paid provider usage, SnapDeploy deployment, browser E2E, or hosted acceptance was run."` | — |
| [SRC-676B69CB6C-L000161](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L161) | 161 | `"- PR: [#155 — feat(workspace): connect product profiles and buyer-intent discovery](https://github.com/mosabosama2030-oss/omarai/pull/155). Open for Human Director review; not merged."` | — |
## وثائق وفهرسة

### FILE-8524B08F5D — [docs/superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-8524B08F5D-L000001](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L1) | 1 | `"# تصميم خط المعالجة الهجين الموحد للبحث والفهم"` | — |
| [SRC-8524B08F5D-L000002](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L2) | 2 | `""` | — |
| [SRC-8524B08F5D-L000003](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L3) | 3 | `"**التاريخ:** 2026-10-30  "` | — |
| [SRC-8524B08F5D-L000004](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L4) | 4 | `"**الحالة:** تصميم تنفيذ ضمن فرع مراجعة؛ لا دمج ولا نشر."` | — |
| [SRC-8524B08F5D-L000005](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L5) | 5 | `""` | — |
| [SRC-8524B08F5D-L000006](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L6) | 6 | `"## الهدف"` | — |
| [SRC-8524B08F5D-L000007](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L7) | 7 | `"ربط فهم السؤال والنية والسياق وتفكيك المحاور وتخطيط الاستعلامات ومطابقة المصادر وتغطية الأدلة في مسار واحد قابل للتفسير والاختبار، مع إبقاء القرار النهائي حول صحة الادعاءات في طبقة التحقق الحالية."` | — |
| [SRC-8524B08F5D-L000008](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L8) | 8 | `""` | — |
| [SRC-8524B08F5D-L000009](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L9) | 9 | `"## الحالة الحالية المثبتة"` | — |
| [SRC-8524B08F5D-L000010](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L10) | 10 | ``"- `intent_router.py` يحل توجيه النية والمتابعات."`` | — |
| [SRC-8524B08F5D-L000011](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L11) | 11 | ``"- `task_understanding.py` ينتج TaskSpec ومصفوفة استراتيجيات البحث."`` | — |
| [SRC-8524B08F5D-L000012](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L12) | 12 | ``"- `aspect_planning.py` يستخرج المحاور ويبني سجل مرشحات لفظية للأدلة."`` | — |
| [SRC-8524B08F5D-L000013](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L13) | 13 | ``"- `research.py` يبني الخطط الاحتياطية ويصنف/يرتب نتائج البحث."`` | — |
| [SRC-8524B08F5D-L000014](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L14) | 14 | ``"- `web_agent.py` يستدعي هذه الوحدات بصورة متفرقة ثم يجري فحوص صلة وتغطية أخرى. المطابقة اللفظية ليست تحققًا دلاليًا ولا إثباتًا لصحة الادعاء."`` | — |
| [SRC-8524B08F5D-L000015](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L15) | 15 | `""` | — |
| [SRC-8524B08F5D-L000016](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L16) | 16 | `"## القرار المعماري"` | — |
| [SRC-8524B08F5D-L000017](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L17) | 17 | ``"إضافة وحدة تنسيق صغيرة `agents/research_pipeline.py` تستدعي الوحدات الحالية ولا تستبدلها:"`` | — |
| [SRC-8524B08F5D-L000018](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L18) | 18 | `"1. **Context:** حل المتابعة إلى موضوع حديث واضح، دون إحياء موضوع قديم بعد انتهاء السياق."` | — |
| [SRC-8524B08F5D-L000019](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L19) | 19 | `"2. **Intent:** استخدام قرار المسار القادم من WebAgent؛ وعند غيابه فقط، استخدام الموجّه الحتمي."` | — |
| [SRC-8524B08F5D-L000020](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L20) | 20 | `"3. **Task understanding:** بناء TaskSpec للهدف والقيود والمخرجات وسياسات الأدلة."` | — |
| [SRC-8524B08F5D-L000021](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L21) | 21 | `"4. **Aspect decomposition:** دمج المحاور الصريحة من TaskSpec مع استخراج مستقل ثانٍ، وإزالة التكرار ضمن سقف 8 محاور."` | — |
| [SRC-8524B08F5D-L000022](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L22) | 22 | `"5. **Query planning:** بناء مصفوفة استعلامات محدودة بحد 8، مع الحفاظ على موضوع السؤال وأولوية المحاور."` | — |
| [SRC-8524B08F5D-L000023](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L23) | 23 | `"6. **Evidence matching:** إنشاء سجل مرشحات لكل محور من المصادر المسترجعة، مع توضيح أن التطابق اللفظي مرشح فقط."` | — |
| [SRC-8524B08F5D-L000024](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L24) | 24 | ``"7. **Semantic stage:** واجهة اختيارية محدودة لمقيّم دلالي يحقنه المستدعي عند توافر مقيّم آمن؛ لا ينشئ هذا التغيير استدعاء نموذج إضافيًا ولا يستخدم خدمة مدفوعة. عند غيابه يسجل `not_configured` ولا يرفع المرشحات اللفظية إلى تحقق دلالي."`` | — |
| [SRC-8524B08F5D-L000025](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L25) | 25 | `"8. **Verification:** إبقاء حواجز المصادر والتحقق من الادعاءات والاستشهادات الموجودة كما هي؛ لا تغطية ولا تشابه كلمات يثبتان صحة المعلومة."` | — |
| [SRC-8524B08F5D-L000026](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L26) | 26 | `""` | — |
| [SRC-8524B08F5D-L000027](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L27) | 27 | `"## التكامل"` | — |
| [SRC-8524B08F5D-L000028](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L28) | 28 | ``"- `research.py::_attach_task_understanding` يستخدم المنسق الموحد بدل بناء TaskSpec والمصفوفة كلًا على حدة."`` | — |
| [SRC-8524B08F5D-L000029](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L29) | 29 | ``"- `web_agent.py` يستخدم المنسق نفسه قبل تنفيذ الاستعلامات، ثم يضيف سجل الأدلة بعد جمع المصادر إلى تقرير البحث."`` | — |
| [SRC-8524B08F5D-L000030](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L30) | 30 | `"- لا تغيير في عقود API أو قاعدة البيانات أو الموصلات أو إعدادات الاستضافة."` | — |
| [SRC-8524B08F5D-L000031](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L31) | 31 | `""` | — |
| [SRC-8524B08F5D-L000032](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L32) | 32 | `"## الحدود"` | — |
| [SRC-8524B08F5D-L000033](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L33) | 33 | `"- لا ذاكرة دلالية دائمة، ولا embeddings أو مكتبات جديدة."` | — |
| [SRC-8524B08F5D-L000034](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L34) | 34 | `"- لا استدعاء LLM إضافي ولا استهلاك مدفوع."` | — |
| [SRC-8524B08F5D-L000035](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L35) | 35 | `"- المقيّم الدلالي الاختياري لا يثبت صحة الادعاءات؛ لا يمكنه إلا ترتيب مرشحات الصلة."` | — |
| [SRC-8524B08F5D-L000036](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L36) | 36 | `"- لا تخفيف من SSRF أو صلة البحث أو حدود الوقت والميزانية أو حواجز المصادر."` | — |
| [SRC-8524B08F5D-L000037](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L37) | 37 | `"- لا دمج PR أو نشر."` | — |
| [SRC-8524B08F5D-L000038](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L38) | 38 | `""` | — |
| [SRC-8524B08F5D-L000039](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L39) | 39 | `"## النجاح"` | — |
| [SRC-8524B08F5D-L000040](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L40) | 40 | `"اختبارات وحدات وانحدار تثبت: الحفاظ على سياق المتابعة الصحيح، طلب التوضيح عند غياب المرجع، استخراج المحاور، حد الاستعلامات، ربط كل محور بسجل مرشحاته، التمييز بين المرشح اللفظي والتحقق الدلالي، وسلامة الرجوع عند فشل المقيّم الاختياري."` | — |
| [SRC-8524B08F5D-L000041](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L41) | 41 | `""` | — |
| [SRC-8524B08F5D-L000042](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L42) | 42 | `""` | — |
| [SRC-8524B08F5D-L000043](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L43) | 43 | `"## نتيجة التنفيذ وحدود المرحلة الحالية"` | — |
| [SRC-8524B08F5D-L000044](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L44) | 44 | `"- تحقق ربط المراحل الحتمية وتكاملها مع مخرجات مخطط البحث اللغوي الموجود."` | — |
| [SRC-8524B08F5D-L000045](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L45) | 45 | `"- المطابقة اللفظية تنتج مرشحات لكل محور، وتبقى منفصلة عن تحقق الادعاء."` | — |
| [SRC-8524B08F5D-L000046](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L46) | 46 | ``"- مقيّم الصلة الدلالية الاختياري له واجهة bounded واختبارات رفض الدرجات غير الصالحة والتدهور عند الاستثناء؛ لكنه غير موصول افتراضيًا بمسار WebAgent، لذلك الحالة التشغيلية المعلنة هي `not_configured`."`` | — |
| [SRC-8524B08F5D-L000047](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L47) | 47 | ``"- لا يُسمح بتحويل حالة `not_configured` إلى `evaluated` إلا بعد توفير مقيّم دلالي فعلي مضبوط بميزانية/مهلة واختبارات قبول مستقلة."`` | — |
## وثائق وفهرسة

### FILE-BFCEEA0374 — [docs/superpowers/specs/2026-11-06-workspace-demand-discovery-design.md](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-BFCEEA0374-L000001](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L1) | 1 | `"# تصميم ربط ملف المنتج واكتشاف الطلب بمساحة عمل Omarai"` | — |
| [SRC-BFCEEA0374-L000002](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L2) | 2 | `""` | — |
| [SRC-BFCEEA0374-L000003](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L3) | 3 | `"**التاريخ:** 6 نوفمبر 2026  "` | — |
| [SRC-BFCEEA0374-L000004](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L4) | 4 | ``"**المرجع:** `main` عند `a297abd271d48f459effad083a9f424a1499cd39`  "`` | — |
| [SRC-BFCEEA0374-L000005](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L5) | 5 | `"**الحالة:** تصميم تنفيذ ضمن فرع مستقل؛ لا يغيّر الإنتاج ولا يدمج تلقائيًا."` | — |
| [SRC-BFCEEA0374-L000006](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L6) | 6 | `""` | — |
| [SRC-BFCEEA0374-L000007](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L7) | 7 | `"## المشكلة"` | — |
| [SRC-BFCEEA0374-L000008](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L8) | 8 | `""` | — |
| [SRC-BFCEEA0374-L000009](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L9) | 9 | ``"مساحة العمل تعرض أربعة أقسام فقط متصلة بواجهات فعلية. نموذج الإشارة الحالي يدعم الإدخال اليدوي والتحليل القواعدي، لكنه لا يشغل بحث المشترين. محرك البحث الحالي يملك بالفعل مسار `LEAD_GENERATION`، ونماذج `ProductProfile` و`MarketProfile` وبناء استعلامات مشتري مرتبطة بالمنتج، لكن الواجهة لا تمرر هذه البيانات إليه ولا تحفظ نتائج التشغيل كسجل مستقل."`` | — |
| [SRC-BFCEEA0374-L000010](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L10) | 10 | `""` | — |
| [SRC-BFCEEA0374-L000011](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L11) | 11 | `"## الهدف"` | — |
| [SRC-BFCEEA0374-L000012](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L12) | 12 | `""` | — |
| [SRC-BFCEEA0374-L000013](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L13) | 13 | `"إنشاء مسار عربي RTL قابل للاستخدام من داخل الواجهة:"` | — |
| [SRC-BFCEEA0374-L000014](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L14) | 14 | `"1. حفظ ملف منتج/خدمة وسوق مستهدف تحت المستأجر الحالي."` | — |
| [SRC-BFCEEA0374-L000015](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L15) | 15 | `"2. تشغيل بحث اكتشاف مرتبط بالملف باستخدام محرك البحث وإشارات نية الشراء الموجودة."` | — |
| [SRC-BFCEEA0374-L000016](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L16) | 16 | `"3. حفظ سجل تشغيل ونتائجه العامة القابلة للمراجعة تحت المستأجر نفسه."` | — |
| [SRC-BFCEEA0374-L000017](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L17) | 17 | ``"4. فصل الإشارات المصنفة `public_demand_signal` عن النتائج المرتبطة بالموضوع فقط."`` | — |
| [SRC-BFCEEA0374-L000018](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L18) | 18 | `"5. السماح بحفظ الإشارة المؤهلة إلى صندوق الإشارات بعد مراجعة المستخدم، مع الاحتفاظ بمصدرها وعبارة الدليل ونوعه في الملاحظة."` | — |
| [SRC-BFCEEA0374-L000019](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L19) | 19 | `"6. إظهار الاستعلامات، حالة التنفيذ، ومحدودية الدليل بصدق."` | — |
| [SRC-BFCEEA0374-L000020](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L20) | 20 | `""` | — |
| [SRC-BFCEEA0374-L000021](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L21) | 21 | `"## البدائل"` | — |
| [SRC-BFCEEA0374-L000022](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L22) | 22 | `""` | — |
| [SRC-BFCEEA0374-L000023](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L23) | 23 | ``"- **A — ربط الواجهة مباشرة بـ`/api/agent`:** أسرع، لكنه يرسل سؤالًا حرًا ولا يفرض عقد ProductProfile/MarketProfile أو سياسة حفظ نتائج مبيعات واضحة."`` | — |
| [SRC-BFCEEA0374-L000024](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L24) | 24 | `"- **B — تكرار محرك بحث للمبيعات:** يمنح تخصيصًا ظاهريًا لكنه يكرر البحث والتصفية والميزانيات وحواجز URL، ويخلق اختلافًا في السلوك."` | — |
| [SRC-BFCEEA0374-L000025](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L25) | 25 | `"- **C — endpoint تجاري منظم يعيد استخدام WebAgent وsales_domain:** يفرض ملفًا منظمًا، ويعيد استخدام محرك البحث وتصنيف نية الشراء، مع تخزين tenant-scoped للملفات وعمليات الاكتشاف. **هذا هو الاختيار** لأنه يحقق مسارًا متصلًا دون محرك ثانٍ."` | — |
| [SRC-BFCEEA0374-L000026](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L26) | 26 | `""` | — |
| [SRC-BFCEEA0374-L000027](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L27) | 27 | `"## النطاق"` | — |
| [SRC-BFCEEA0374-L000028](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L28) | 28 | `""` | — |
| [SRC-BFCEEA0374-L000029](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L29) | 29 | `"- إضافة تخزين tenant-scoped لملفات المنتج/السوق وسجلات عمليات الاكتشاف."` | — |
| [SRC-BFCEEA0374-L000030](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L30) | 30 | `"- إضافة عقود API محمية لقراءة/حفظ الملفات، تشغيل الاكتشاف، قراءة سجل التشغيل، وحفظ إشارة من تشغيل محفوظ."` | — |
| [SRC-BFCEEA0374-L000031](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L31) | 31 | ``"- تمرير استعلامات `build_buyer_queries` مباشرة إلى WebAgent بدل إعادة استخراج المنتج من نص حر."`` | — |
| [SRC-BFCEEA0374-L000032](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L32) | 32 | `"- إبقاء الموصلات الاختيارية التي قد تستهلك حصصًا/تكلفة معطلة افتراضيًا في مسار الاكتشاف؛ لا يسمح بتفعيلها إلا بطلب صريح من المالك في نفس التشغيل."` | — |
| [SRC-BFCEEA0374-L000033](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L33) | 33 | `"- تفعيل شاشتي ملف المنتج والاكتشاف فقط بعد ربطهما بعقود حقيقية."` | — |
| [SRC-BFCEEA0374-L000034](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L34) | 34 | `"- إبقاء الوحدات الأخرى غير المنفذة معطلة."` | — |
| [SRC-BFCEEA0374-L000035](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L35) | 35 | `"- حفظ الإشارة المؤهلة بعد فعل صريح من المستخدم فقط؛ لا تواصل آلي."` | — |
| [SRC-BFCEEA0374-L000036](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L36) | 36 | `""` | — |
| [SRC-BFCEEA0374-L000037](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L37) | 37 | `"## خارج النطاق"` | — |
| [SRC-BFCEEA0374-L000038](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L38) | 38 | `""` | — |
| [SRC-BFCEEA0374-L000039](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L39) | 39 | `"- إنشاء CRM كامل أو ملفات شركات أو حملات مجدولة أو تنبيهات أو مهام خلفية."` | — |
| [SRC-BFCEEA0374-L000040](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L40) | 40 | `"- الادعاء بأن كل المصادر والمنصات متاحة أو أن نتائج البحث تمثل كل السوق."` | — |
| [SRC-BFCEEA0374-L000041](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L41) | 41 | `"- بناء محرك بحث جديد أو تفعيل Firecrawl؛ PR #153 منفصل ومفتوح على خط الأساس الحالي."` | — |
| [SRC-BFCEEA0374-L000042](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L42) | 42 | `"- إرسال رسائل أو جمع بيانات اتصال خاصة."` | — |
| [SRC-BFCEEA0374-L000043](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L43) | 43 | `"- تغيير أسرار SnapDeploy أو مفاتيح المزودين أو النشر أو الدمج."` | — |
| [SRC-BFCEEA0374-L000044](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L44) | 44 | `""` | — |
| [SRC-BFCEEA0374-L000045](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L45) | 45 | `"## البيانات والأمان"` | — |
| [SRC-BFCEEA0374-L000046](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L46) | 46 | `""` | — |
| [SRC-BFCEEA0374-L000047](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L47) | 47 | ``"- كل ملف منتج وكل تشغيل وكل مصدر محفوظ يقيّد بـ`tenant_id` المستمد من principal موثوق على الخادم، وليس من body أو query."`` | — |
| [SRC-BFCEEA0374-L000048](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L48) | 48 | `"- يجب أن تشمل المفاتيح والقيود الفريدة نطاق المستأجر."` | — |
| [SRC-BFCEEA0374-L000049](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L49) | 49 | ``"- استرجاع الإشارة للحفظ يكون بواسطة `run_id + source_index + tenant_id` من سجل محفوظ في الخادم؛ لا يثق الخادم في تصنيف يرسله المتصفح."`` | — |
| [SRC-BFCEEA0374-L000050](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L50) | 50 | ``"- لا تُحفظ نتيجة غير مصنفة `public_demand_signal` كإشارة شراء من إجراء الحفظ الخاص بالتشغيل."`` | — |
| [SRC-BFCEEA0374-L000051](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L51) | 51 | `"- لا يعرض النظام هوية الكاتب أو قناة اتصال إلا إذا كانت موجودة ومتحققًا منها في المصدر. لا تستنتجها."` | — |
| [SRC-BFCEEA0374-L000052](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L52) | 52 | `"- النص والمقتطفات والصفحات بيانات غير موثوقة."` | — |
| [SRC-BFCEEA0374-L000053](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L53) | 53 | `"- لا تُشغّل DeepSeek/Brave/Tavily أو موصلات اختيارية ذات حصص/تكلفة تلقائيًا في مسار الاكتشاف. التفعيل صريح ومن المالك فقط."` | — |
| [SRC-BFCEEA0374-L000054](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L54) | 54 | `"- لا تُعرض درجة التحليل القواعدي الحالية كاحتمال شراء."` | — |
| [SRC-BFCEEA0374-L000055](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L55) | 55 | `""` | — |
| [SRC-BFCEEA0374-L000056](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L56) | 56 | `"## معيار القبول"` | — |
| [SRC-BFCEEA0374-L000057](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L57) | 57 | `""` | — |
| [SRC-BFCEEA0374-L000058](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L58) | 58 | `"- يمكن حفظ ملفين بمنتجين مختلفين لنفس المستأجر، واسترجاعهما؛ ولا يستطيع مستأجر آخر قراءتهما."` | — |
| [SRC-BFCEEA0374-L000059](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L59) | 59 | `"- يرفض الخادم viewer من الكتابة أو تشغيل الاكتشاف."` | — |
| [SRC-BFCEEA0374-L000060](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L60) | 60 | `"- يولد البحث استعلامات من أسماء/مرادفات المنتج والموقع، دون تسرب عبارات عقارية إلى المنتجات غير العقارية."` | — |
| [SRC-BFCEEA0374-L000061](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L61) | 61 | `"- يستدعي endpoint محرك WebAgent الحالي بعقد buyer queries منظمة، لا بمحرك ثانٍ."` | — |
| [SRC-BFCEEA0374-L000062](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L62) | 62 | `"- لا تُستدعى الموصلات الاختيارية عند ترك خيار الاستخدام الاختياري مغلقًا."` | — |
| [SRC-BFCEEA0374-L000063](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L63) | 63 | `"- يحفظ سجل تشغيل مع مصادره وحالاتها تحت المستأجر."` | — |
| [SRC-BFCEEA0374-L000064](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L64) | 64 | ``"- لا يقبل endpoint الحفظ مصدرًا غير مصنف `public_demand_signal`، ولا يقبل معرف تشغيل تابعًا لمستأجر آخر."`` | — |
| [SRC-BFCEEA0374-L000065](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L65) | 65 | `"- الواجهة تعرض الدليل والمصدر ونوع النص/أساسه والحدود، وتسمح بحفظ الإشارة المؤهلة يدويًا فقط."` | — |
| [SRC-BFCEEA0374-L000066](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L66) | 66 | `"- جميع الاختبارات الآلية وCI ذات الصلة ناجحة؛ قبول الاستضافة بعد النشر يبقى منفصلًا ويتطلب إجراء Human Director."` | — |
| [SRC-BFCEEA0374-L000067](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L67) | 67 | `""` | — |
| [SRC-BFCEEA0374-L000068](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L68) | 68 | `"## القرارات التنفيذية"` | — |
| [SRC-BFCEEA0374-L000069](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L69) | 69 | `""` | — |
| [SRC-BFCEEA0374-L000070](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L70) | 70 | ``"- إعادة استخدام `agents.sales_domain` و`WebAgent` و`LeadStore` بدل إنشاء محرك مستقل."`` | — |
| [SRC-BFCEEA0374-L000071](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L71) | 71 | ``"- تخزين ملفات المنتج وتشغيلات الاكتشاف في SQLite مع migration آمن عبر `CREATE TABLE IF NOT EXISTS` وفهارس tenant-scoped."`` | — |
| [SRC-BFCEEA0374-L000072](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L72) | 72 | `"- عدم تغيير أي مفتاح أو إعداد استضافة."` | — |
| [SRC-BFCEEA0374-L000073](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L73) | 73 | `"- لا دمج ولا نشر ضمن هذا العمل."` | — |
## وثائق وفهرسة

### FILE-6B9B9ABE27 — [docs/ui-directions/README.md](../ui-directions/README.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-6B9B9ABE27-L000001](../ui-directions/README.md#L1) | 1 | `"# Omarai — Three Glass UI Directions"` | — |
| [SRC-6B9B9ABE27-L000002](../ui-directions/README.md#L2) | 2 | `""` | — |
| [SRC-6B9B9ABE27-L000003](../ui-directions/README.md#L3) | 3 | `"**Status:** Visual proposals for Human Director selection only. No direction is implemented or connected to production APIs."` | — |
| [SRC-6B9B9ABE27-L000004](../ui-directions/README.md#L4) | 4 | `""` | — |
| [SRC-6B9B9ABE27-L000005](../ui-directions/README.md#L5) | 5 | `"Design project: https://design.agent-native.com/design/sGSw7-l6baKesddSGTdvl?editorView=overview"` | — |
| [SRC-6B9B9ABE27-L000006](../ui-directions/README.md#L6) | 6 | `""` | — |
| [SRC-6B9B9ABE27-L000007](../ui-directions/README.md#L7) | 7 | `"## Option 01 — Aurora Glass"` | — |
| [SRC-6B9B9ABE27-L000008](../ui-directions/README.md#L8) | 8 | `"- Expressive frosted surfaces with teal/cyan/violet ambient glow."` | — |
| [SRC-6B9B9ABE27-L000009](../ui-directions/README.md#L9) | 9 | `"- Futuristic, colorful Android-inspired atmosphere with restrained layering."` | — |
| [SRC-6B9B9ABE27-L000010](../ui-directions/README.md#L10) | 10 | `"- Best when the product should feel distinctly modern and visually memorable."` | — |
| [SRC-6B9B9ABE27-L000011](../ui-directions/README.md#L11) | 11 | `"- Preview: [variant-01-aurora-glass.html](variant-01-aurora-glass.html)"` | — |
