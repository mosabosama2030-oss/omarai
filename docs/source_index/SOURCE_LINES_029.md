# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **029**
- سجلات الأسطر: **800**
- النطاق: SRC-D911B73392-L000128 إلى SRC-70795F4B61-L000020
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## وثائق وفهرسة

### FILE-D911B73392 — [docs/RESEARCH_CONNECTORS_AR.md](../RESEARCH_CONNECTORS_AR.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-D911B73392-L000128](../RESEARCH_CONNECTORS_AR.md#L128) | 128 | `"- المنشور أو التعليق قد يكون ساخرًا أو قديمًا أو ترويجيًا أو خارج السياق. يوضح Omarai المصدر والنص المتاح، لكنه لا يثبت هوية الكاتب أو صحة كلامه."` | — |
| [SRC-D911B73392-L000129](../RESEARCH_CONNECTORS_AR.md#L129) | 129 | `"- لا تستخدم بيانات شخصية غير لازمة، ولا تجمع محتوى خاصًا أو تتجاوز شروط أي منصة."` | — |
| [SRC-D911B73392-L000130](../RESEARCH_CONNECTORS_AR.md#L130) | 130 | `"- لا يرسل Omarai رسائل أو يتواصل مع أصحاب الحسابات تلقائيًا. أي تواصل أو إجراء خارجي يجب أن يبقى بقرار بشري ومراجعة منفصلة."` | — |
## وثائق وفهرسة

### FILE-69F3587825 — [docs/search_code.py](../search_code.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-69F3587825-L000001](../search_code.py#L1) | 1 | `"\"\"\"Text search across Omarai repository source files (no external AI required)."` | — |
| [SRC-69F3587825-L000002](../search_code.py#L2) | 2 | `""` | — |
| [SRC-69F3587825-L000003](../search_code.py#L3) | 3 | `"Examples:"` | — |
| [SRC-69F3587825-L000004](../search_code.py#L4) | 4 | `"  python docs/search_code.py \"def analyze\""` | — |
| [SRC-69F3587825-L000005](../search_code.py#L5) | 5 | `"  python docs/search_code.py --regex \"OMARAI_[A-Z_]+\" --ext py"` | — |
| [SRC-69F3587825-L000006](../search_code.py#L6) | 6 | `"  python docs/search_code.py \"access token\" --max 20"` | — |
| [SRC-69F3587825-L000007](../search_code.py#L7) | 7 | `"  python docs/search_code.py --root /path/to/omarai \"do_POST\""` | — |
| [SRC-69F3587825-L000008](../search_code.py#L8) | 8 | `"\"\"\""` | — |
| [SRC-69F3587825-L000009](../search_code.py#L9) | 9 | `""` | — |
| [SRC-69F3587825-L000010](../search_code.py#L10) | 10 | `"from __future__ import annotations"` | — |
| [SRC-69F3587825-L000011](../search_code.py#L11) | 11 | `""` | — |
| [SRC-69F3587825-L000012](../search_code.py#L12) | 12 | `"import argparse"` | — |
| [SRC-69F3587825-L000013](../search_code.py#L13) | 13 | `"import os"` | — |
| [SRC-69F3587825-L000014](../search_code.py#L14) | 14 | `"import re"` | — |
| [SRC-69F3587825-L000015](../search_code.py#L15) | 15 | `"import subprocess"` | — |
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
## ملفات أخرى

### FILE-C693279643 — [LICENSE](../../LICENSE#L1)

- النوع: **بدون امتداد**
- نطاق الفهرسة: جرد ملف نصي فقط

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-C693279643-L000001](../../LICENSE#L1) | 1 | `"MIT License"` | — |
| [SRC-C693279643-L000002](../../LICENSE#L2) | 2 | `""` | — |
| [SRC-C693279643-L000003](../../LICENSE#L3) | 3 | `"Copyright (c) 2026 Omarai contributors"` | — |
| [SRC-C693279643-L000004](../../LICENSE#L4) | 4 | `""` | — |
| [SRC-C693279643-L000005](../../LICENSE#L5) | 5 | `"Permission is hereby granted, free of charge, to any person obtaining a copy"` | — |
| [SRC-C693279643-L000006](../../LICENSE#L6) | 6 | `"of this software and associated documentation files (the \"Software\"), to deal"` | — |
| [SRC-C693279643-L000007](../../LICENSE#L7) | 7 | `"in the Software without restriction, including without limitation the rights"` | — |
| [SRC-C693279643-L000008](../../LICENSE#L8) | 8 | `"to use, copy, modify, merge, publish, distribute, sublicense, and/or sell"` | — |
| [SRC-C693279643-L000009](../../LICENSE#L9) | 9 | `"copies of the Software, and to permit persons to whom the Software is"` | — |
| [SRC-C693279643-L000010](../../LICENSE#L10) | 10 | `"furnished to do so, subject to the following conditions:"` | — |
| [SRC-C693279643-L000011](../../LICENSE#L11) | 11 | `""` | — |
| [SRC-C693279643-L000012](../../LICENSE#L12) | 12 | `"The above copyright notice and this permission notice shall be included in all"` | — |
| [SRC-C693279643-L000013](../../LICENSE#L13) | 13 | `"copies or substantial portions of the Software."` | — |
| [SRC-C693279643-L000014](../../LICENSE#L14) | 14 | `""` | — |
| [SRC-C693279643-L000015](../../LICENSE#L15) | 15 | `"THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR"` | — |
| [SRC-C693279643-L000016](../../LICENSE#L16) | 16 | `"IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,"` | — |
| [SRC-C693279643-L000017](../../LICENSE#L17) | 17 | `"FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE"` | — |
| [SRC-C693279643-L000018](../../LICENSE#L18) | 18 | `"AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER"` | — |
| [SRC-C693279643-L000019](../../LICENSE#L19) | 19 | `"LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,"` | — |
| [SRC-C693279643-L000020](../../LICENSE#L20) | 20 | `"OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE"` | — |
| [SRC-C693279643-L000021](../../LICENSE#L21) | 21 | `"SOFTWARE."` | — |
## إعدادات وتشغيل

### FILE-50C86B7ED8 — [pyproject.toml](../../pyproject.toml#L1)

- النوع: **TOML**
- نطاق الفهرسة: جرد الملف + مفاتيح إعداد ساكنة

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-50C86B7ED8-L000001](../../pyproject.toml#L1) | 1 | `"[build-system]"` | — |
| [SRC-50C86B7ED8-L000002](../../pyproject.toml#L2) | 2 | `"requires = [\"setuptools>=68\"]"` | — |
| [SRC-50C86B7ED8-L000003](../../pyproject.toml#L3) | 3 | `"build-backend = \"setuptools.build_meta\""` | — |
| [SRC-50C86B7ED8-L000004](../../pyproject.toml#L4) | 4 | `""` | — |
| [SRC-50C86B7ED8-L000005](../../pyproject.toml#L5) | 5 | `"[project]"` | — |
| [SRC-50C86B7ED8-L000006](../../pyproject.toml#L6) | 6 | `"name = \"omarai-agent\""` | — |
| [SRC-50C86B7ED8-L000007](../../pyproject.toml#L7) | 7 | `"version = \"0.2.0\""` | — |
| [SRC-50C86B7ED8-L000008](../../pyproject.toml#L8) | 8 | `"description = \"Arabic-first web research and generative Q&A agent with lead workspace\""` | — |
| [SRC-50C86B7ED8-L000009](../../pyproject.toml#L9) | 9 | `"readme = \"README.md\""` | — |
| [SRC-50C86B7ED8-L000010](../../pyproject.toml#L10) | 10 | `"requires-python = \">=3.11\""` | — |
| [SRC-50C86B7ED8-L000011](../../pyproject.toml#L11) | 11 | `"license = { text = \"MIT\" }"` | — |
| [SRC-50C86B7ED8-L000012](../../pyproject.toml#L12) | 12 | `"dependencies = ["` | — |
| [SRC-50C86B7ED8-L000013](../../pyproject.toml#L13) | 13 | `"  \"beautifulsoup4>=4.12,<5\","` | — |
| [SRC-50C86B7ED8-L000014](../../pyproject.toml#L14) | 14 | `"  \"httpx>=0.27,<1\","` | — |
| [SRC-50C86B7ED8-L000015](../../pyproject.toml#L15) | 15 | `"  \"tldextract>=5.3,<6\","` | — |
| [SRC-50C86B7ED8-L000016](../../pyproject.toml#L16) | 16 | `"]"` | — |
| [SRC-50C86B7ED8-L000017](../../pyproject.toml#L17) | 17 | `""` | — |
| [SRC-50C86B7ED8-L000018](../../pyproject.toml#L18) | 18 | `"[project.optional-dependencies]"` | — |
| [SRC-50C86B7ED8-L000019](../../pyproject.toml#L19) | 19 | `"dev = [\"pytest>=8.0\", \"ruff>=0.5\"]"` | — |
| [SRC-50C86B7ED8-L000020](../../pyproject.toml#L20) | 20 | `""` | — |
| [SRC-50C86B7ED8-L000021](../../pyproject.toml#L21) | 21 | `"[tool.pytest.ini_options]"` | — |
| [SRC-50C86B7ED8-L000022](../../pyproject.toml#L22) | 22 | `"testpaths = [\"tests\"]"` | — |
| [SRC-50C86B7ED8-L000023](../../pyproject.toml#L23) | 23 | `""` | — |
| [SRC-50C86B7ED8-L000024](../../pyproject.toml#L24) | 24 | `"[tool.setuptools.packages.find]"` | — |
| [SRC-50C86B7ED8-L000025](../../pyproject.toml#L25) | 25 | `"include = [\"agents*\", \"api*\", \"cli*\"]"` | — |
| [SRC-50C86B7ED8-L000026](../../pyproject.toml#L26) | 26 | `"exclude = [\"tests*\", \"web*\"]"` | — |
| [SRC-50C86B7ED8-L000027](../../pyproject.toml#L27) | 27 | `""` | — |
| [SRC-50C86B7ED8-L000028](../../pyproject.toml#L28) | 28 | `"[tool.ruff]"` | — |
| [SRC-50C86B7ED8-L000029](../../pyproject.toml#L29) | 29 | `"line-length = 100"` | — |
| [SRC-50C86B7ED8-L000030](../../pyproject.toml#L30) | 30 | `"target-version = \"py311\""` | — |
| [SRC-50C86B7ED8-L000031](../../pyproject.toml#L31) | 31 | `""` | — |
| [SRC-50C86B7ED8-L000032](../../pyproject.toml#L32) | 32 | `"[tool.ruff.lint]"` | — |
| [SRC-50C86B7ED8-L000033](../../pyproject.toml#L33) | 33 | `"# Keep default rules; ignore only patterns intentional in this codebase."` | — |
| [SRC-50C86B7ED8-L000034](../../pyproject.toml#L34) | 34 | `"# BLE001: broad except at API boundary to avoid leaking internals"` | — |
| [SRC-50C86B7ED8-L000035](../../pyproject.toml#L35) | 35 | `"# E501: long Arabic/English diagnostic strings"` | — |
| [SRC-50C86B7ED8-L000036](../../pyproject.toml#L36) | 36 | `"# I001: historical import order; do not block CI on style alone"` | — |
| [SRC-50C86B7ED8-L000037](../../pyproject.toml#L37) | 37 | `"# F841: unused assignment kept for clarity in some tests"` | — |
| [SRC-50C86B7ED8-L000038](../../pyproject.toml#L38) | 38 | `"# RUF100: residual noqa:BLE001 comments after BLE001 is ignored globally"` | — |
| [SRC-50C86B7ED8-L000039](../../pyproject.toml#L39) | 39 | `"ignore = [\"BLE001\", \"E501\", \"I001\", \"F841\", \"RUF100\"]"` | — |
## إعدادات وتشغيل

### FILE-115C2027D9 — [railway.json](../../railway.json#L1)

- النوع: **JSON**
- نطاق الفهرسة: جرد الملف + مفاتيح إعداد ساكنة

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-115C2027D9-L000001](../../railway.json#L1) | 1 | `"{"` | — |
| [SRC-115C2027D9-L000002](../../railway.json#L2) | 2 | `"  \"$schema\": \"https://railway.com/railway.schema.json\","` | — |
| [SRC-115C2027D9-L000003](../../railway.json#L3) | 3 | `"  \"build\": {"` | — |
| [SRC-115C2027D9-L000004](../../railway.json#L4) | 4 | `"    \"builder\": \"DOCKERFILE\","` | — |
| [SRC-115C2027D9-L000005](../../railway.json#L5) | 5 | `"    \"dockerfilePath\": \"Dockerfile\""` | — |
| [SRC-115C2027D9-L000006](../../railway.json#L6) | 6 | `"  },"` | — |
| [SRC-115C2027D9-L000007](../../railway.json#L7) | 7 | `"  \"deploy\": {"` | — |
| [SRC-115C2027D9-L000008](../../railway.json#L8) | 8 | `"    \"startCommand\": \"sh -c 'python -m cli.omarai serve --host 0.0.0.0 --port ${PORT:-8000}'\","` | — |
| [SRC-115C2027D9-L000009](../../railway.json#L9) | 9 | `"    \"healthcheckPath\": \"/api/health\","` | — |
| [SRC-115C2027D9-L000010](../../railway.json#L10) | 10 | `"    \"healthcheckTimeout\": 120,"` | — |
| [SRC-115C2027D9-L000011](../../railway.json#L11) | 11 | `"    \"restartPolicyType\": \"ON_FAILURE\","` | — |
| [SRC-115C2027D9-L000012](../../railway.json#L12) | 12 | `"    \"restartPolicyMaxRetries\": 5"` | — |
| [SRC-115C2027D9-L000013](../../railway.json#L13) | 13 | `"  }"` | — |
| [SRC-115C2027D9-L000014](../../railway.json#L14) | 14 | `"}"` | — |
## وثائق ونصوص

### FILE-B335630551 — [README.md](../../README.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-B335630551-L000001](../../README.md#L1) | 1 | `"# Omarai — Web Research & Generative Q&A Agent"` | — |
| [SRC-B335630551-L000002](../../README.md#L2) | 2 | `""` | — |
| [SRC-B335630551-L000003](../../README.md#L3) | 3 | `"> **Foundational engineering requirements:** mandatory contributor/agent rules are in [AGENTS.md](AGENTS.md). The core architecture and security charter is [OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md](docs/OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md); the expanded platform practices across reliability, security, privacy, data, SRE, AI, accessibility, supply chain, and cost are in [OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md](docs/OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md); and the requirement IDs, expert-review lenses, evidence model, risk priorities, maturity stages, and release gates are in [OMARAI_REQUIREMENTS_TRACEABILITY_AND_MATURITY_MODEL_AR.md](docs/OMARAI_REQUIREMENTS_TRACEABILITY_AND_MATURITY_MODEL_AR.md). The initial foundational requirements checklist is [OMARAI_REQUIREMENTS_REGISTER.md](docs/OMARAI_REQUIREMENTS_REGISTER.md). These documents define required direction; they do not prove every control is implemented or tested. Use the [documentation index](docs/README.md) to find the current source of truth for each topic."` | — |
| [SRC-B335630551-L000004](../../README.md#L4) | 4 | `""` | — |
| [SRC-B335630551-L000005](../../README.md#L5) | 5 | `"Omarai is an Arabic-first web research agent with a responsive RTL chat UI. You can ask open-ended questions in natural language, search the public web, extract text from accessible pages, compare and summarize findings, ask follow-up questions, and inspect the source links."` | — |
| [SRC-B335630551-L000006](../../README.md#L6) | 6 | `""` | — |
| [SRC-B335630551-L000007](../../README.md#L7) | 7 | `"## What this version does"` | — |
| [SRC-B335630551-L000008](../../README.md#L8) | 8 | `""` | — |
| [SRC-B335630551-L000009](../../README.md#L9) | 9 | `"- Plans up to eight search queries from a natural-language question with a dedicated reasoning/planning model, and uses a deterministic multi-query fallback when the model is unavailable."` | — |
| [SRC-B335630551-L000010](../../README.md#L10) | 10 | `"- Uses separate model roles by default: NVIDIA Nemotron 3 Ultra (free) for query planning and Google Gemma 4 31B Instruct (free) for answer synthesis and the second-pass consistency review; retries with OpenRouter's free-model router if a chosen model fails."` | — |
| [SRC-B335630551-L000011](../../README.md#L11) | 11 | `"- Runs DuckDuckGo HTML and Bing RSS independently for every planned query; can add official Brave Search API and Tavily Search API result indexes when their environment keys are configured; uses Google News RSS for queries judged time-sensitive."` | — |
| [SRC-B335630551-L000012](../../README.md#L12) | 12 | `"- Fuses duplicate results across queries and engines using reciprocal-rank fusion, preserving provider, query, domain, platform, publication-date and page-extraction provenance."` | — |
| [SRC-B335630551-L000013](../../README.md#L13) | 13 | `"- Extracts text from up to eight accessible public pages per question with request-size and timeout bounds, following at most three individually validated public redirects."` | — |
| [SRC-B335630551-L000014](../../README.md#L14) | 14 | ``"- Searches public Reddit RSS and the Bluesky public search endpoint when social discussion is relevant; can use Reddit's OAuth API when `REDDIT_CLIENT_ID` and `REDDIT_CLIENT_SECRET` are provided."`` | — |
| [SRC-B335630551-L000015](../../README.md#L15) | 15 | `"- Searches indexed public pages on Facebook, Instagram, X, TikTok, LinkedIn, Threads and YouTube through the general web engines."` | — |
| [SRC-B335630551-L000016](../../README.md#L16) | 16 | `"- Can use the official Meta Graph API to read posts and a small sample of public comments from explicitly configured Facebook Pages when the token has suitable permissions."` | — |
| [SRC-B335630551-L000017](../../README.md#L17) | 17 | ``"- Can use Instagram Graph API hashtag search to read public hashtag media when `INSTAGRAM_USER_ID` and `INSTAGRAM_ACCESS_TOKEN` have the required permissions. It is not a global Instagram search and has platform quotas."`` | — |
| [SRC-B335630551-L000018](../../README.md#L18) | 18 | ``"- Can use the official X recent-post endpoint when `X_BEARER_TOKEN` is configured and the account/API tier permits the request; can use the official YouTube Data API when `YOUTUBE_API_KEY` is configured."`` | — |
| [SRC-B335630551-L000019](../../README.md#L19) | 19 | `"- Generates an evidence-grounded answer in the user's language, showing source links, query plan, provider coverage, direct page reads, platform mix, source/domain diversity, date coverage, and evidence-coverage warnings. Coverage indicators describe breadth and inspectability; they are not probabilities that the answer is true."` | — |
| [SRC-B335630551-L000020](../../README.md#L20) | 20 | `"- Carries up to eight recent chat messages from the current browser session into follow-up questions."` | — |
| [SRC-B335630551-L000021](../../README.md#L21) | 21 | ``"- Keeps the existing local SQLite lead workspace at `/leads`."`` | — |
| [SRC-B335630551-L000022](../../README.md#L22) | 22 | `"- Binds to loopback by default; it is not a public production deployment."` | — |
| [SRC-B335630551-L000023](../../README.md#L23) | 23 | `""` | — |
| [SRC-B335630551-L000024](../../README.md#L24) | 24 | ``"**Verification semantics:** `GET /api/health` is a configuration/dependency snapshot, not proof that search providers or the model are reachable. Check the `agent.verification_scope` field to see what is and is not verified. Use the protected `POST /api/diagnostics` endpoint for explicit live search/model probes; a passed diagnostic only verifies the specific probes run at that time, not every optional connector or answer quality."`` | — |
| [SRC-B335630551-L000025](../../README.md#L25) | 25 | `""` | — |
| [SRC-B335630551-L000026](../../README.md#L26) | 26 | `"This is a tool-using research agent built around existing language models, not a foundation model trained from scratch. The role-specific defaults aim for more consistent behaviour than using a router that selects a different free model at random on each call. Exact availability and response quality still depend on OpenRouter/provider conditions. **Privacy warning:** the user's question, conversation context and selected web excerpts are sent to the configured external language-model provider for planning/synthesis/review. OpenRouter's NVIDIA Nemotron free endpoint states that session data may be logged for security and product improvement; do not send passwords, API keys, private information or personal/confidential customer data through the free endpoint. See the [NVIDIA Nemotron free-endpoint privacy notice](https://openrouter.ai/nvidia/nemotron-3-ultra-550b-a55b:free). Its language-model planner decides how to search, but query count, URLs and result shapes are validated by deterministic code. Cross-engine agreement improves discovery and ranking but is not independent fact verification. Public social pages that require login, blocked pages and private profiles are not fetched; social search cannot promise complete coverage of any platform. Direct official-platform access varies: Reddit API access requires approved app credentials and is subject to Reddit's terms; Facebook Pages reads require a valid token, page identifiers and correct permissions; Instagram hashtag search requires a professional Instagram account token and the specific supported permissions; X API access requires an authorized bearer token and suitable access; YouTube direct API search requires a Google API key. These APIs do not grant universal access to all content, accounts or comments. Review each platform's terms, quotas and permitted use before using the agent commercially. The agent never bypasses login, paywall or access controls and does not send messages or make automated contact with people."` | — |
| [SRC-B335630551-L000027](../../README.md#L27) | 27 | `""` | — |
| [SRC-B335630551-L000028](../../README.md#L28) | 28 | `""` | — |
| [SRC-B335630551-L000029](../../README.md#L29) | 29 | `"## Living repository index"` | — |
| [SRC-B335630551-L000030](../../README.md#L30) | 30 | `""` | — |
| [SRC-B335630551-L000031](../../README.md#L31) | 31 | `"**Current delivery gate (Arabic):** [OMARAI HANDOFF CHECKLIST](docs/OMARAI_HANDOFF_CHECKLIST_AR.md) — current release blockers, required evidence, and operator actions. The central [remediation register](docs/OMARAI_REMEDIATION_REGISTER_AR.md) remains the detailed issue history."` | — |
| [SRC-B335630551-L000032](../../README.md#L32) | 32 | `""` | — |
| [SRC-B335630551-L000033](../../README.md#L33) | 33 | `"Omarai maintains a categorized master index and a paginated, line-by-line source index:"` | — |
| [SRC-B335630551-L000034](../../README.md#L34) | 34 | `""` | — |
| [SRC-B335630551-L000035](../../README.md#L35) | 35 | ``"- [MASTER INDEX](docs/MASTER_INDEX.md): file inventory with stable file IDs, Python AST definitions, static frontend/configuration symbols, and explicitly marked TODO/FIXME/BUG/HACK/XXX/REVIEW/SECURITY/DEPRECATED/ISSUE/DEFECT/REGRESSION/RISK/GAP/ERROR/WARNING/PERF/PRIVACY/DATA_LOSS/ACCESSIBILITY entries. Each review marker has an `FND-...` code and a link to the exact source line."`` | — |
| [SRC-B335630551-L000036](../../README.md#L36) | 36 | `"- [SOURCE LINES INDEX](docs/SOURCE_LINES_INDEX.md): search-friendly directory of files, page links, per-file line counts, and links to each source line."` | — |
| [SRC-B335630551-L000037](../../README.md#L37) | 37 | `"- [INDEX COVERAGE AUDIT](docs/INDEX_COVERAGE_AUDIT.md): generated evidence of line-count consistency, metadata-only files, excluded path names and their reasons, and the exact scope of any “100%” coverage statement."` | — |
| [SRC-B335630551-L000038](../../README.md#L38) | 38 | ``"- [Source line pages](docs/source_index/): small generated pages containing every logical line from eligible readable text files. Each line has a `SRC-<FILEHASH>-L000001` code, exact JSON-escaped text, and a link back to the source file at the matching line. Pages are capped at 800 line records to remain navigable on mobile and in GitHub's web view."`` | — |
| [SRC-B335630551-L000039](../../README.md#L39) | 39 | `"- [Local source search](docs/search_code.py): offline text/regex search with file, line, nearby context, and GitHub line links. It excludes common secret/configuration files, databases, key files, symlinks, and runtime directories; it does not detect every secret or replace a security audit."` | — |
| [SRC-B335630551-L000040](../../README.md#L40) | 40 | `""` | — |
| [SRC-B335630551-L000041](../../README.md#L41) | 41 | ``"Example: `python docs/search_code.py \"resolve_followup_query\" --ext py --context 2`."`` | — |
| [SRC-B335630551-L000042](../../README.md#L42) | 42 | `""` | — |
| [SRC-B335630551-L000043](../../README.md#L43) | 43 | ``"The generator now refuses to publish indexes if any eligible file has missing, duplicated, or misnumbered source-line records. It still cannot infer every unmarked logical/programming defect; known issues should be recorded explicitly with a supported marker (for example, `# BUG: explain the defect`) so the generated `FND-...` register can point to the corresponding `SRC-...` line."`` | — |
| [SRC-B335630551-L000044](../../README.md#L44) | 44 | `""` | — |
| [SRC-B335630551-L000045](../../README.md#L45) | 45 | `"Regenerate and verify the indexes locally:"` | — |
| [SRC-B335630551-L000046](../../README.md#L46) | 46 | `""` | — |
| [SRC-B335630551-L000047](../../README.md#L47) | 47 | ````"```bash"```` | — |
| [SRC-B335630551-L000048](../../README.md#L48) | 48 | `"python docs/generate_index.py"` | — |
| [SRC-B335630551-L000049](../../README.md#L49) | 49 | `"python docs/generate_index.py --check"` | — |
| [SRC-B335630551-L000050](../../README.md#L50) | 50 | ````"```"```` | — |
| [SRC-B335630551-L000051](../../README.md#L51) | 51 | `""` | — |
| [SRC-B335630551-L000052](../../README.md#L52) | 52 | ``"GitHub Actions validates the generator on Python 3.11 and 3.12. The publishing workflow runs on pushes to `main` and the `feat/**`, `fix/**`, and `feature/**` branches. It regenerates and commits all indexes and generated pages only when output changes; obsolete generated pages are removed, while generated-index-only commits are ignored to avoid loops. Documentation-only and repository-hygiene branches are still tested with indexes regenerated in the isolated test workspace, but do not carry a large generated-page diff solely because documentation lines moved; after merge, the publisher refreshes the committed indexes on `main`. If direct publication to `main` is rejected, it opens a pull request instead of force-updating a branch or auto-merging."`` | — |
| [SRC-B335630551-L000053](../../README.md#L53) | 53 | `""` | — |
| [SRC-B335630551-L000054](../../README.md#L54) | 54 | ``"When a known code issue is found, add a source comment using one supported marker name (TODO, FIXME, BUG, HACK, XXX, REVIEW, SECURITY, DEPRECATED, ISSUE, DEFECT, REGRESSION, RISK, GAP, ERROR, WARNING, PERF, PRIVACY, DATA_LOSS, or ACCESSIBILITY), followed by a colon and a concise description. The index assigns an `FND-...` code and links it to the exact `SRC-...` source-line record; removing or editing that source annotation updates the generated register on the next index run. Coverage includes every logical line in eligible readable text files up to 2 MiB. Known local secrets, runtime databases, dependency/build directories, binary/unreadable files and oversized files are excluded from line-level indexing by design but listed by metadata where eligible. Static review markers help track explicit findings; no source index can prove that every arbitrary logic bug has been detected or that all code is correct."`` | — |
| [SRC-B335630551-L000055](../../README.md#L55) | 55 | `""` | — |
| [SRC-B335630551-L000056](../../README.md#L56) | 56 | `"## Per-request resource budget"` | — |
| [SRC-B335630551-L000057](../../README.md#L57) | 57 | `""` | — |
| [SRC-B335630551-L000058](../../README.md#L58) | 58 | ``"Each `POST /api/agent` answer includes a `request_budget` object with elapsed and remaining time, reserved resource counts, and configured limits. The current defaults are a 90-second cooperative deadline, at most 8 search queries, 32 provider search calls, 8 model HTTP attempts, 8 page fetches, and up to 3 optional server-side search-tool calls per request. Operator limits may be lowered or raised only within hard caps: `OMARAI_REQUEST_BUDGET_SECONDS` (10–120), `OMARAI_REQUEST_MAX_SEARCH_QUERIES` (1–8), `OMARAI_REQUEST_MAX_SEARCH_CALLS` (1–40), `OMARAI_REQUEST_MAX_MODEL_CALLS` (1–12), `OMARAI_REQUEST_MAX_PAGE_FETCHES` (1–8), and `OMARAI_REQUEST_MAX_TOOL_CALLS` (0–3). Invalid numeric values fall back to the defaults; out-of-range values are clamped."`` | — |
| [SRC-B335630551-L000059](../../README.md#L59) | 59 | `""` | — |
| [SRC-B335630551-L000060](../../README.md#L60) | 60 | `"The deadline caps the timeout passed to outbound operations and prevents new work from being reserved after the deadline or a resource cap is exhausted. It is **cooperative, not hard cancellation**: a network call already in progress may overrun slightly while its client unwinds. Do not interpret this metadata as a load test, a throughput guarantee, or proof that any live provider is reachable. CI tests for budget logic are separate from live-provider validation."` | — |
| [SRC-B335630551-L000061](../../README.md#L61) | 61 | `""` | — |
| [SRC-B335630551-L000062](../../README.md#L62) | 62 | ``"The HTTP ingress caps active handler connections at 32 per process by default through `OMARAI_MAX_CONCURRENT_HTTP_CONNECTIONS` (bounded to 1–128). When all slots are occupied, excess sockets receive HTTP 503 with `Retry-After: 5` before a handler thread is created. The in-memory rate limiter also caps client buckets at 4,096 per process; new identities beyond that ceiling share a conservative overflow quota. Separately, expensive `/api/agent` and `/api/diagnostics` operations remain limited to at most 4 concurrent operations per process by default; configure `OMARAI_MAX_CONCURRENT_AGENT_REQUESTS` from 1 to 8. These are **process-local** controls, not distributed limits across workers or replicas, and they are not throughput/load-test claims."`` | — |
| [SRC-B335630551-L000063](../../README.md#L63) | 63 | `""` | — |
| [SRC-B335630551-L000064](../../README.md#L64) | 64 | `"## Experimental DeepSeek Search provider"` | — |
| [SRC-B335630551-L000065](../../README.md#L65) | 65 | `""` | — |
| [SRC-B335630551-L000066](../../README.md#L66) | 66 | `"Omarai can optionally compare results from DeepSeek's Search API when"` | — |
| [SRC-B335630551-L000067](../../README.md#L67) | 67 | ``"`DEEPSEEK_SEARCH_API_KEY` is configured in the host's secret settings. It is"`` | — |
| [SRC-B335630551-L000068](../../README.md#L68) | 68 | `"**disabled by default**; DuckDuckGo and Bing remain configured as before."` | — |
| [SRC-B335630551-L000069](../../README.md#L69) | 69 | `"To limit possible spend when opted in, the request budget defaults to **one"` | — |
| [SRC-B335630551-L000070](../../README.md#L70) | 70 | `"DeepSeek Search call per answer/diagnostic operation**. It can be set from 0 to 3"` | — |
| [SRC-B335630551-L000071](../../README.md#L71) | 71 | ``"using `OMARAI_DEEPSEEK_SEARCH_REQUEST_BUDGET`; invalid values fall back to 1."`` | — |
| [SRC-B335630551-L000072](../../README.md#L72) | 72 | `"DeepSeek Search is billed per successful request (currently documented at"` | — |
| [SRC-B335630551-L000073](../../README.md#L73) | 73 | `"US$0.75 per 1,000 successful searches); review the"` | — |
| [SRC-B335630551-L000074](../../README.md#L74) | 74 | `"[official Search & Fetch guide](https://api-docs.deepseek.com/guides/search/)"` | — |
| [SRC-B335630551-L000075](../../README.md#L75) | 75 | `"before enabling it. Unit tests use a mocked response; this repository change"` | — |
| [SRC-B335630551-L000076](../../README.md#L76) | 76 | `"does not claim live DeepSeek connectivity or answer-quality improvement."` | — |
| [SRC-B335630551-L000077](../../README.md#L77) | 77 | `""` | — |
| [SRC-B335630551-L000078](../../README.md#L78) | 78 | `"## Hosting and live acceptance"` | — |
| [SRC-B335630551-L000079](../../README.md#L79) | 79 | `""` | — |
| [SRC-B335630551-L000080](../../README.md#L80) | 80 | `"Omarai includes several **alternative** hosting paths. Choose one provider; the presence of a config file is not proof that a service exists or has passed acceptance."` | — |
| [SRC-B335630551-L000081](../../README.md#L81) | 81 | `""` | — |
| [SRC-B335630551-L000082](../../README.md#L82) | 82 | ``"- **Railway:** [Arabic deployment guide](docs/DEPLOY_RAILWAY_AR.md), using `railway.json`."`` | — |
| [SRC-B335630551-L000083](../../README.md#L83) | 83 | `"- **SnapDeploy:** [free-demo guide](docs/DEPLOY_SNAPDEPLOY_AR.md). Confirm current quotas and terms before use; ephemeral storage means it is not a durable lead database."` | — |
| [SRC-B335630551-L000084](../../README.md#L84) | 84 | ``"- **Render:** [optional alternative guide](docs/DEPLOY_RENDER_AR.md), using `render.yaml`. Use it only if the provider/account is available to you."`` | — |
| [SRC-B335630551-L000085](../../README.md#L85) | 85 | `""` | — |
| [SRC-B335630551-L000086](../../README.md#L86) | 86 | ``"All providers share the same acceptance rules. The API reports a validated source revision at `/api/health`: it prefers image-baked `BUILD_SHA`, then documented platform Git metadata where supported. For another Docker host, pass `--build-arg OMARAI_BUILD_SHA=\"$(git rev-parse HEAD)\"`. A local/container build is not evidence of a live deployment; compare the reported SHA with the exact intended commit."`` | — |
| [SRC-B335630551-L000087](../../README.md#L87) | 87 | `""` | — |
| [SRC-B335630551-L000088](../../README.md#L88) | 88 | `"**Single-operator limit:** the current bearer token is shared application access, not individual identity or a tenant boundary. The lead workspace does not provide confirmed per-customer data isolation. Keep a hosted instance private to one operator; do not store confidential records for multiple customers. Concurrency and rate-limit state are process-local, not distributed. The new HTTP handler and client-bucket ceilings bound per-process growth, but do not establish production load capacity or per-tenant isolation."` | — |
| [SRC-B335630551-L000089](../../README.md#L89) | 89 | `""` | — |
| [SRC-B335630551-L000090](../../README.md#L90) | 90 | ``"For a public-bound instance, set `OMARAI_PUBLIC_DEPLOYMENT=1` and a separate random `OMARAI_ACCESS_TOKEN` of at least 32 characters. The app refuses public binding without both. Configure `OPENROUTER_API_KEY` or `OMARAI_LLM_API_KEY` only in the provider's secret store. If the UI is on another origin, set `OMARAI_ALLOWED_ORIGINS` to the exact trusted origins (scheme, host, optional port; no path or wildcard). The built-in UI served from the same host usually needs no extra origin entry. Public API routes require the bearer token and apply a default in-memory per-client IP limit of 20 requests per minute. The browser stores only the app access token in local storage, not the provider API key."`` | — |
| [SRC-B335630551-L000091](../../README.md#L91) | 91 | `""` | — |
| [SRC-B335630551-L000092](../../README.md#L92) | 92 | ``"Before accepting any host, follow the [go-live checklist](docs/GO_LIVE_CHECKLIST_AR.md) and run the manually triggered [hosted acceptance smoke workflow](.github/workflows/hosted-smoke.yml) only after setting GitHub Actions secrets `OMARAI_ACCESS_TOKEN` and `OMARAI_BASE_URL` to the authorized service. The workflow makes real model/search calls and may incur usage charges; do not run it without human approval. On hosts with a genuinely persistent mounted volume, set `OMARAI_DB_PATH` to a file inside the mount (for example, `/data/omarai.sqlite3`). This setting selects a path; it does not create storage or replace backups and a tested restore. Keep the lead workspace disabled for important records until persistence across restart/redeploy and restore are verified on the actual host."`` | — |
| [SRC-B335630551-L000093](../../README.md#L93) | 93 | `""` | — |
| [SRC-B335630551-L000094](../../README.md#L94) | 94 | `"## Run on Android / Termux"` | — |
| [SRC-B335630551-L000095](../../README.md#L95) | 95 | `""` | — |
| [SRC-B335630551-L000096](../../README.md#L96) | 96 | `"From the repository directory:"` | — |
| [SRC-B335630551-L000097](../../README.md#L97) | 97 | `""` | — |
| [SRC-B335630551-L000098](../../README.md#L98) | 98 | ````"```bash"```` | — |
| [SRC-B335630551-L000099](../../README.md#L99) | 99 | `"python -m pip install -e ."` | — |
| [SRC-B335630551-L000100](../../README.md#L100) | 100 | ````"```"```` | — |
| [SRC-B335630551-L000101](../../README.md#L101) | 101 | `""` | — |
| [SRC-B335630551-L000102](../../README.md#L102) | 102 | ``"The default language-model configuration uses OpenRouter: Nemotron 3 Ultra (free) plans queries, Gemma 4 31B Instruct (free) writes the answer and performs the optional second-pass review, and `openrouter/free` is the fallback if a selected model fails. Create an OpenRouter API key, then enter it without putting the secret into a command-history entry. The model key enables both search planning and generative synthesis; general web search can still run without it, but results will not be turned into a full language-model analysis:"`` | — |
| [SRC-B335630551-L000103](../../README.md#L103) | 103 | `""` | — |
| [SRC-B335630551-L000104](../../README.md#L104) | 104 | ````"```bash"```` | — |
| [SRC-B335630551-L000105](../../README.md#L105) | 105 | `"read -r -s -p \"OpenRouter API key: \" OPENROUTER_API_KEY"` | — |
| [SRC-B335630551-L000106](../../README.md#L106) | 106 | `"printf '\\n'"` | — |
| [SRC-B335630551-L000107](../../README.md#L107) | 107 | `"export OPENROUTER_API_KEY"` | — |
| [SRC-B335630551-L000108](../../README.md#L108) | 108 | `"python -m cli.omarai serve"` | — |
| [SRC-B335630551-L000109](../../README.md#L109) | 109 | ````"```"```` | — |
| [SRC-B335630551-L000110](../../README.md#L110) | 110 | `""` | — |
| [SRC-B335630551-L000111](../../README.md#L111) | 111 | `"Keep this Termux session running and open **http://127.0.0.1:8765** in the phone's browser. The agent chat is the home screen. The existing lead workspace remains available at **http://127.0.0.1:8765/leads**."` | — |
| [SRC-B335630551-L000112](../../README.md#L112) | 112 | `""` | — |
| [SRC-B335630551-L000113](../../README.md#L113) | 113 | `"The key is held in the current shell environment and is not written into the repository. Enter it again in a new Termux session. Never commit API keys or paste them into public issues or chat."` | — |
| [SRC-B335630551-L000114](../../README.md#L114) | 114 | `""` | — |
| [SRC-B335630551-L000115](../../README.md#L115) | 115 | `"### Optional configuration"` | — |
| [SRC-B335630551-L000116](../../README.md#L116) | 116 | `""` | — |
| [SRC-B335630551-L000117](../../README.md#L117) | 117 | `"For additional live web-search indexes, configure either official search API. These keys are optional: the built-in public engines are still attempted, and each API may have its own account, quota, rate limit or cost. Do not assume an API is free or that a configured key is valid until you run the live diagnostics."` | — |
| [SRC-B335630551-L000118](../../README.md#L118) | 118 | `""` | — |
| [SRC-B335630551-L000119](../../README.md#L119) | 119 | ````"```bash"```` | — |
| [SRC-B335630551-L000120](../../README.md#L120) | 120 | `"read -r -s -p \"Brave Search API key: \" BRAVE_SEARCH_API_KEY; printf '\\\\n'; export BRAVE_SEARCH_API_KEY"` | — |
| [SRC-B335630551-L000121](../../README.md#L121) | 121 | `"read -r -s -p \"Tavily API key: \" TAVILY_API_KEY; printf '\\\\n'; export TAVILY_API_KEY"` | — |
| [SRC-B335630551-L000122](../../README.md#L122) | 122 | ````"```"```` | — |
| [SRC-B335630551-L000123](../../README.md#L123) | 123 | `""` | — |
| [SRC-B335630551-L000124](../../README.md#L124) | 124 | `""` | — |
| [SRC-B335630551-L000125](../../README.md#L125) | 125 | `"For a different OpenAI-compatible endpoint or model, set these environment variables before starting the server:"` | — |
| [SRC-B335630551-L000126](../../README.md#L126) | 126 | `""` | — |
| [SRC-B335630551-L000127](../../README.md#L127) | 127 | ````"```bash"```` | — |
| [SRC-B335630551-L000128](../../README.md#L128) | 128 | `"export OMARAI_LLM_BASE_URL=\"https://openrouter.ai/api/v1\""` | — |
| [SRC-B335630551-L000129](../../README.md#L129) | 129 | `"export OMARAI_LLM_MODEL=\"openrouter/free\""` | — |
| [SRC-B335630551-L000130](../../README.md#L130) | 130 | ````"```"```` | — |
| [SRC-B335630551-L000131](../../README.md#L131) | 131 | `""` | — |
| [SRC-B335630551-L000132](../../README.md#L132) | 132 | ``"Use `OMARAI_LLM_API_KEY` instead of `OPENROUTER_API_KEY` when you want a separate environment variable. `OMARAI_LLM_TIMEOUT` accepts a timeout in seconds from 5 to 60. To customize model roles, set `OMARAI_PLANNER_MODEL`, `OMARAI_ANSWER_MODEL`, and/or `OMARAI_REVIEW_MODEL`; `OMARAI_LLM_MODEL` remains a global override for all roles that have no role-specific override. `OMARAI_LLM_FALLBACK_MODEL` changes the default `openrouter/free` fallback. Provider pricing, model availability and rate limits can change; check the chosen provider before using a paid model. Optional social credentials may be configured in the same Termux session before starting the server: `REDDIT_CLIENT_ID` + `REDDIT_CLIENT_SECRET` (official OAuth access), `X_BEARER_TOKEN`, `YOUTUBE_API_KEY`, `INSTAGRAM_USER_ID` + `INSTAGRAM_ACCESS_TOKEN` + optional `META_GRAPH_VERSION`, and `FACEBOOK_PAGE_ACCESS_TOKEN` + `FACEBOOK_PAGE_IDS` (comma-separated Page IDs that the authorized token can access). Use `read -r -s` to enter secrets privately rather than saving them in shell history. Do not store keys in source files, HTML, commits or chat messages."`` | — |
| [SRC-B335630551-L000133](../../README.md#L133) | 133 | `""` | — |
| [SRC-B335630551-L000134](../../README.md#L134) | 134 | `"If no language-model key is configured, Omarai can still attempt web search and show source snippets, but it cannot provide the full generative understanding/synthesis layer. If search providers are temporarily unavailable, the agent reports the limitation rather than pretending that a search succeeded."` | — |
| [SRC-B335630551-L000135](../../README.md#L135) | 135 | `""` | — |
| [SRC-B335630551-L000136](../../README.md#L136) | 136 | `"For the platform boundaries, optional credentials and safe Termux setup for social connectors, see the [Arabic research connectors guide](docs/RESEARCH_CONNECTORS_AR.md)."` | — |
| [SRC-B335630551-L000137](../../README.md#L137) | 137 | `""` | — |
| [SRC-B335630551-L000138](../../README.md#L138) | 138 | `"## API"` | — |
| [SRC-B335630551-L000139](../../README.md#L139) | 139 | `""` | — |
| [SRC-B335630551-L000140](../../README.md#L140) | 140 | ``"- `GET /` — web-research chat"`` | — |
| [SRC-B335630551-L000141](../../README.md#L141) | 141 | ``"- `GET /leads` — existing lead workspace"`` | — |
| [SRC-B335630551-L000142](../../README.md#L142) | 142 | ``"- `GET /api/health` — setup and dependency status (never returns the API key)"`` | — |
| [SRC-B335630551-L000143](../../README.md#L143) | 143 | ``"- `POST /api/diagnostics` — opt-in live checks for web search and the language model; set `test_social: true` to also probe public/authorized social connectors"`` | — |
| [SRC-B335630551-L000144](../../README.md#L144) | 144 | ``"- `POST /api/agent` — open-ended question plus optional recent `history`"`` | — |
| [SRC-B335630551-L000145](../../README.md#L145) | 145 | ``"- `POST /api/analyze` — existing rule-based lead-text assessment"`` | — |
| [SRC-B335630551-L000146](../../README.md#L146) | 146 | ``"- `GET/POST /api/leads` — existing local lead records"`` | — |
| [SRC-B335630551-L000147](../../README.md#L147) | 147 | `""` | — |
| [SRC-B335630551-L000148](../../README.md#L148) | 148 | `"Example request:"` | — |
| [SRC-B335630551-L000149](../../README.md#L149) | 149 | `""` | — |
| [SRC-B335630551-L000150](../../README.md#L150) | 150 | ````"```json"```` | — |
| [SRC-B335630551-L000151](../../README.md#L151) | 151 | `"{"` | — |
| [SRC-B335630551-L000152](../../README.md#L152) | 152 | `"  \"question\": \"Compare the latest public information about two technologies\","` | — |
| [SRC-B335630551-L000153](../../README.md#L153) | 153 | `"  \"history\": []"` | — |
| [SRC-B335630551-L000154](../../README.md#L154) | 154 | `"}"` | — |
| [SRC-B335630551-L000155](../../README.md#L155) | 155 | ````"```"```` | — |
| [SRC-B335630551-L000156](../../README.md#L156) | 156 | `""` | — |
| [SRC-B335630551-L000157](../../README.md#L157) | 157 | ``"The `/api/diagnostics` response reports pass/fail/degraded states, returned result counts, provider counts, elapsed time, and the model that actually answered (including fallback use). The Arabic web UI offers automatic, deep, latest-information, and public-social research modes, plus a live-test button. The model check sends one small completion request; optional social checks perform real public/API requests and can take longer. The response from `/api/agent` includes `answer`, `sources`, `search_queries`, `research_plan`, `search_report`, `used_web_search`, `used_social_search`, `used_language_model`, and any warnings. The request can pass `mode` as `auto`, `deep`, `latest`, or `social`. The report records planned and attempted queries, unique result count, pages read, providers, platform breakdown, citation-range checks and whether an optional second-pass consistency review completed. That second pass uses the same configured model/provider and is not independent fact verification. URL syntax and resolved private/local addresses are checked before page fetches; public redirects are followed only through a small bounded loop with each destination revalidated. Search engines may still return inaccessible, stale or noisy results, which the agent must disclose."`` | — |
| [SRC-B335630551-L000158](../../README.md#L158) | 158 | `""` | — |
| [SRC-B335630551-L000159](../../README.md#L159) | 159 | `"## Existing lead workspace"` | — |
| [SRC-B335630551-L000160](../../README.md#L160) | 160 | `""` | — |
| [SRC-B335630551-L000161](../../README.md#L161) | 161 | ``"The previous local lead-intent tool is preserved at `/leads`. It stores data locally in `~/.omarai/omarai.sqlite3`. Its transparent rule score is not a statistical probability of a purchase. Process only public/authorized data, minimize personal information, and manually review business decisions."`` | — |
| [SRC-B335630551-L000162](../../README.md#L162) | 162 | `""` | — |
| [SRC-B335630551-L000163](../../README.md#L163) | 163 | `"Analyze text from the CLI:"` | — |
| [SRC-B335630551-L000164](../../README.md#L164) | 164 | `""` | — |
| [SRC-B335630551-L000165](../../README.md#L165) | 165 | ````"```bash"```` | — |
| [SRC-B335630551-L000166](../../README.md#L166) | 166 | `"python -m cli.omarai analyze --text \"بدور على شقة في التجمع الخامس وممكن معاينة\" --product \"شقة,عقار\" --location \"التجمع الخامس\""` | — |
| [SRC-B335630551-L000167](../../README.md#L167) | 167 | ````"```"```` | — |
| [SRC-B335630551-L000168](../../README.md#L168) | 168 | `""` | — |
| [SRC-B335630551-L000169](../../README.md#L169) | 169 | ``"CSV import requires `text,source_url,platform` columns:"`` | — |
| [SRC-B335630551-L000170](../../README.md#L170) | 170 | `""` | — |
| [SRC-B335630551-L000171](../../README.md#L171) | 171 | ````"```bash"```` | — |
| [SRC-B335630551-L000172](../../README.md#L172) | 172 | `"python -m cli.omarai import-csv --file leads.csv"` | — |
| [SRC-B335630551-L000173](../../README.md#L173) | 173 | `"python -m cli.omarai list --limit 50"` | — |
| [SRC-B335630551-L000174](../../README.md#L174) | 174 | `"python -m cli.omarai export-csv --file leads-export.csv"` | — |
| [SRC-B335630551-L000175](../../README.md#L175) | 175 | ````"```"```` | — |
| [SRC-B335630551-L000176](../../README.md#L176) | 176 | `""` | — |
| [SRC-B335630551-L000177](../../README.md#L177) | 177 | `"## Checks"` | — |
| [SRC-B335630551-L000178](../../README.md#L178) | 178 | `""` | — |
| [SRC-B335630551-L000179](../../README.md#L179) | 179 | ````"```bash"```` | — |
| [SRC-B335630551-L000180](../../README.md#L180) | 180 | `"python -m pip install -e \".[dev]\""` | — |
| [SRC-B335630551-L000181](../../README.md#L181) | 181 | `"ruff check agents api cli tests"` | — |
| [SRC-B335630551-L000182](../../README.md#L182) | 182 | `"python -m pytest -q"` | — |
| [SRC-B335630551-L000183](../../README.md#L183) | 183 | ````"```"```` | — |
## إعدادات وتشغيل

### FILE-A64CF250B4 — [render.yaml](../../render.yaml#L1)

- النوع: **YAML**
- نطاق الفهرسة: جرد الملف + مفاتيح إعداد ساكنة

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-A64CF250B4-L000001](../../render.yaml#L1) | 1 | `"services:"` | — |
| [SRC-A64CF250B4-L000002](../../render.yaml#L2) | 2 | `"  - type: web"` | — |
| [SRC-A64CF250B4-L000003](../../render.yaml#L3) | 3 | `"    name: omarai"` | — |
| [SRC-A64CF250B4-L000004](../../render.yaml#L4) | 4 | `"    runtime: docker"` | — |
| [SRC-A64CF250B4-L000005](../../render.yaml#L5) | 5 | `"    plan: free"` | — |
| [SRC-A64CF250B4-L000006](../../render.yaml#L6) | 6 | `"    region: frankfurt"` | — |
| [SRC-A64CF250B4-L000007](../../render.yaml#L7) | 7 | `"    dockerfilePath: ./Dockerfile"` | — |
| [SRC-A64CF250B4-L000008](../../render.yaml#L8) | 8 | `"    healthCheckPath: /api/health"` | — |
| [SRC-A64CF250B4-L000009](../../render.yaml#L9) | 9 | `"    envVars:"` | — |
| [SRC-A64CF250B4-L000010](../../render.yaml#L10) | 10 | `"      - key: OMARAI_PUBLIC_DEPLOYMENT"` | — |
| [SRC-A64CF250B4-L000011](../../render.yaml#L11) | 11 | `"        value: \"1\""` | — |
| [SRC-A64CF250B4-L000012](../../render.yaml#L12) | 12 | `"      - key: OMARAI_ACCESS_TOKEN"` | — |
| [SRC-A64CF250B4-L000013](../../render.yaml#L13) | 13 | `"        sync: false"` | — |
| [SRC-A64CF250B4-L000014](../../render.yaml#L14) | 14 | `"      - key: OPENROUTER_API_KEY"` | — |
| [SRC-A64CF250B4-L000015](../../render.yaml#L15) | 15 | `"        sync: false"` | — |
## ملفات أخرى

### FILE-64EDD7FC2B — [scripts/__init__.py](../../scripts/__init__.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-64EDD7FC2B-L000001](../../scripts/__init__.py#L1) | 1 | `"\"\"\"Operational helper scripts for Omarai.\"\"\""` | — |
## ملفات أخرى

### FILE-70795F4B61 — [scripts/compare_answer_quality_runs.py](../../scripts/compare_answer_quality_runs.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-70795F4B61-L000001](../../scripts/compare_answer_quality_runs.py#L1) | 1 | `"\"\"\"Compare two Omarai benchmark runs without inventing quality or cost measurements."` | — |
| [SRC-70795F4B61-L000002](../../scripts/compare_answer_quality_runs.py#L2) | 2 | `""` | — |
| [SRC-70795F4B61-L000003](../../scripts/compare_answer_quality_runs.py#L3) | 3 | `"Runtime measurements come from explicit run telemetry. Factual accuracy, retrieval"` | — |
| [SRC-70795F4B61-L000004](../../scripts/compare_answer_quality_runs.py#L4) | 4 | `"precision/recall, faithfulness, citation support, and writing quality require matching"` | — |
| [SRC-70795F4B61-L000005](../../scripts/compare_answer_quality_runs.py#L5) | 5 | `"human-review files; missing annotations remain unscored. The comparator is offline."` | — |
| [SRC-70795F4B61-L000006](../../scripts/compare_answer_quality_runs.py#L6) | 6 | `"\"\"\""` | — |
| [SRC-70795F4B61-L000007](../../scripts/compare_answer_quality_runs.py#L7) | 7 | `"from __future__ import annotations"` | — |
| [SRC-70795F4B61-L000008](../../scripts/compare_answer_quality_runs.py#L8) | 8 | `""` | — |
| [SRC-70795F4B61-L000009](../../scripts/compare_answer_quality_runs.py#L9) | 9 | `"import argparse"` | — |
| [SRC-70795F4B61-L000010](../../scripts/compare_answer_quality_runs.py#L10) | 10 | `"import importlib.util"` | — |
| [SRC-70795F4B61-L000011](../../scripts/compare_answer_quality_runs.py#L11) | 11 | `"import json"` | — |
| [SRC-70795F4B61-L000012](../../scripts/compare_answer_quality_runs.py#L12) | 12 | `"import math"` | — |
| [SRC-70795F4B61-L000013](../../scripts/compare_answer_quality_runs.py#L13) | 13 | `"import re"` | — |
| [SRC-70795F4B61-L000014](../../scripts/compare_answer_quality_runs.py#L14) | 14 | `"import sys"` | — |
| [SRC-70795F4B61-L000015](../../scripts/compare_answer_quality_runs.py#L15) | 15 | `"from pathlib import Path"` | — |
| [SRC-70795F4B61-L000016](../../scripts/compare_answer_quality_runs.py#L16) | 16 | `"from typing import Any"` | — |
| [SRC-70795F4B61-L000017](../../scripts/compare_answer_quality_runs.py#L17) | 17 | `""` | — |
| [SRC-70795F4B61-L000018](../../scripts/compare_answer_quality_runs.py#L18) | 18 | `"ROOT = Path(__file__).resolve().parents[1]"` | — |
| [SRC-70795F4B61-L000019](../../scripts/compare_answer_quality_runs.py#L19) | 19 | `"DEFAULT_CORPUS = ROOT / \"tests\" / \"fixtures\" / \"answer_quality_cases.json\""` | — |
| [SRC-70795F4B61-L000020](../../scripts/compare_answer_quality_runs.py#L20) | 20 | `"REQUIRED_RUN_FIELDS = {\"benchmark_id\", \"benchmark_version\", \"results\"}"` | — |
