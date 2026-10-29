# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **028**
- سجلات الأسطر: **800**
- النطاق: SRC-69F3587825-L000091 إلى SRC-70795F4B61-L000290
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## وثائق وفهرسة

### FILE-69F3587825 — [docs/search_code.py](../search_code.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
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
| [SRC-B335630551-L000062](../../README.md#L62) | 62 | ``"The HTTP API also limits expensive `/api/agent` and `/api/diagnostics` operations to at most 4 concurrent operations per process by default. Configure `OMARAI_MAX_CONCURRENT_AGENT_REQUESTS` from 1 to 8. If all slots are occupied, the API returns HTTP 503 with a short retry hint instead of queueing unlimited expensive work. This is a **process-local** cap, not a distributed semaphore across multiple workers or replicas, and it is not a throughput/load-test claim."`` | — |
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
| [SRC-B335630551-L000088](../../README.md#L88) | 88 | `"**Single-operator limit:** the current bearer token is shared application access, not individual identity or a tenant boundary. The lead workspace does not provide confirmed per-customer data isolation. Keep a hosted instance private to one operator; do not store confidential records for multiple customers. Concurrency and rate-limit state are process-local, not distributed, and production load capacity has not been established."` | — |
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
| [SRC-70795F4B61-L000021](../../scripts/compare_answer_quality_runs.py#L21) | 21 | `""` | — |
| [SRC-70795F4B61-L000022](../../scripts/compare_answer_quality_runs.py#L22) | 22 | `""` | — |
| [SRC-70795F4B61-L000023](../../scripts/compare_answer_quality_runs.py#L23) | 23 | `"def load_json_object(path: Path) -> dict[str, Any]:"` | — |
| [SRC-70795F4B61-L000024](../../scripts/compare_answer_quality_runs.py#L24) | 24 | `"    if not path.is_file():"` | — |
| [SRC-70795F4B61-L000025](../../scripts/compare_answer_quality_runs.py#L25) | 25 | `"        raise FileNotFoundError(\"Input file not found: \" + str(path))"` | — |
| [SRC-70795F4B61-L000026](../../scripts/compare_answer_quality_runs.py#L26) | 26 | `"    data = json.loads(path.read_text(encoding=\"utf-8\"))"` | — |
| [SRC-70795F4B61-L000027](../../scripts/compare_answer_quality_runs.py#L27) | 27 | `"    if not isinstance(data, dict):"` | — |
| [SRC-70795F4B61-L000028](../../scripts/compare_answer_quality_runs.py#L28) | 28 | `"        raise TypeError(\"JSON root must be an object: \" + str(path))"` | — |
| [SRC-70795F4B61-L000029](../../scripts/compare_answer_quality_runs.py#L29) | 29 | `"    return data"` | — |
| [SRC-70795F4B61-L000030](../../scripts/compare_answer_quality_runs.py#L30) | 30 | `""` | — |
| [SRC-70795F4B61-L000031](../../scripts/compare_answer_quality_runs.py#L31) | 31 | `""` | — |
| [SRC-70795F4B61-L000032](../../scripts/compare_answer_quality_runs.py#L32) | 32 | `"def _finite_nonnegative(value: Any) -> float \| None:"` | — |
| [SRC-70795F4B61-L000033](../../scripts/compare_answer_quality_runs.py#L33) | 33 | `"    if isinstance(value, bool) or not isinstance(value, (int, float)):"` | — |
| [SRC-70795F4B61-L000034](../../scripts/compare_answer_quality_runs.py#L34) | 34 | `"        return None"` | — |
| [SRC-70795F4B61-L000035](../../scripts/compare_answer_quality_runs.py#L35) | 35 | `"    number = float(value)"` | — |
| [SRC-70795F4B61-L000036](../../scripts/compare_answer_quality_runs.py#L36) | 36 | `"    if not math.isfinite(number) or number < 0:"` | — |
| [SRC-70795F4B61-L000037](../../scripts/compare_answer_quality_runs.py#L37) | 37 | `"        return None"` | — |
| [SRC-70795F4B61-L000038](../../scripts/compare_answer_quality_runs.py#L38) | 38 | `"    return number"` | — |
| [SRC-70795F4B61-L000039](../../scripts/compare_answer_quality_runs.py#L39) | 39 | `""` | — |
| [SRC-70795F4B61-L000040](../../scripts/compare_answer_quality_runs.py#L40) | 40 | `""` | — |
| [SRC-70795F4B61-L000041](../../scripts/compare_answer_quality_runs.py#L41) | 41 | `"def validate_run(run: dict[str, Any], label: str) -> list[str]:"` | — |
| [SRC-70795F4B61-L000042](../../scripts/compare_answer_quality_runs.py#L42) | 42 | `"    problems: list[str] = []"` | — |
| [SRC-70795F4B61-L000043](../../scripts/compare_answer_quality_runs.py#L43) | 43 | `"    missing = REQUIRED_RUN_FIELDS - set(run)"` | — |
| [SRC-70795F4B61-L000044](../../scripts/compare_answer_quality_runs.py#L44) | 44 | `"    if missing:"` | — |
| [SRC-70795F4B61-L000045](../../scripts/compare_answer_quality_runs.py#L45) | 45 | `"        problems.append(f\"{label}: missing run fields {sorted(missing)}\")"` | — |
| [SRC-70795F4B61-L000046](../../scripts/compare_answer_quality_runs.py#L46) | 46 | `"    results = run.get(\"results\")"` | — |
| [SRC-70795F4B61-L000047](../../scripts/compare_answer_quality_runs.py#L47) | 47 | `"    if not isinstance(results, list) or not results:"` | — |
| [SRC-70795F4B61-L000048](../../scripts/compare_answer_quality_runs.py#L48) | 48 | `"        problems.append(f\"{label}: results must be a non-empty array\")"` | — |
| [SRC-70795F4B61-L000049](../../scripts/compare_answer_quality_runs.py#L49) | 49 | `"        return problems"` | — |
| [SRC-70795F4B61-L000050](../../scripts/compare_answer_quality_runs.py#L50) | 50 | `"    seen: set[str] = set()"` | — |
| [SRC-70795F4B61-L000051](../../scripts/compare_answer_quality_runs.py#L51) | 51 | `"    for index, record in enumerate(results):"` | — |
| [SRC-70795F4B61-L000052](../../scripts/compare_answer_quality_runs.py#L52) | 52 | `"        if not isinstance(record, dict):"` | — |
| [SRC-70795F4B61-L000053](../../scripts/compare_answer_quality_runs.py#L53) | 53 | `"            problems.append(f\"{label}: results[{index}] must be an object\")"` | — |
| [SRC-70795F4B61-L000054](../../scripts/compare_answer_quality_runs.py#L54) | 54 | `"            continue"` | — |
| [SRC-70795F4B61-L000055](../../scripts/compare_answer_quality_runs.py#L55) | 55 | `"        case_id = record.get(\"case_id\")"` | — |
| [SRC-70795F4B61-L000056](../../scripts/compare_answer_quality_runs.py#L56) | 56 | `"        if not isinstance(case_id, str) or not case_id.strip():"` | — |
| [SRC-70795F4B61-L000057](../../scripts/compare_answer_quality_runs.py#L57) | 57 | `"            problems.append(f\"{label}: results[{index}] has no case_id\")"` | — |
| [SRC-70795F4B61-L000058](../../scripts/compare_answer_quality_runs.py#L58) | 58 | `"            continue"` | — |
| [SRC-70795F4B61-L000059](../../scripts/compare_answer_quality_runs.py#L59) | 59 | `"        prompt = record.get(\"prompt\")"` | — |
| [SRC-70795F4B61-L000060](../../scripts/compare_answer_quality_runs.py#L60) | 60 | `"        if not isinstance(prompt, str) or not prompt.strip():"` | — |
| [SRC-70795F4B61-L000061](../../scripts/compare_answer_quality_runs.py#L61) | 61 | `"            problems.append(f\"{label}/{case_id}: prompt must be a non-empty string\")"` | — |
| [SRC-70795F4B61-L000062](../../scripts/compare_answer_quality_runs.py#L62) | 62 | `"        if case_id in seen:"` | — |
| [SRC-70795F4B61-L000063](../../scripts/compare_answer_quality_runs.py#L63) | 63 | `"            problems.append(f\"{label}: duplicate case_id {case_id}\")"` | — |
| [SRC-70795F4B61-L000064](../../scripts/compare_answer_quality_runs.py#L64) | 64 | `"        seen.add(case_id)"` | — |
| [SRC-70795F4B61-L000065](../../scripts/compare_answer_quality_runs.py#L65) | 65 | `"        if \"elapsed_ms\" in record and _finite_nonnegative(record[\"elapsed_ms\"]) is None:"` | — |
| [SRC-70795F4B61-L000066](../../scripts/compare_answer_quality_runs.py#L66) | 66 | `"            problems.append(f\"{label}/{case_id}: elapsed_ms must be finite and non-negative\")"` | — |
| [SRC-70795F4B61-L000067](../../scripts/compare_answer_quality_runs.py#L67) | 67 | `"    return problems"` | — |
| [SRC-70795F4B61-L000068](../../scripts/compare_answer_quality_runs.py#L68) | 68 | `""` | — |
| [SRC-70795F4B61-L000069](../../scripts/compare_answer_quality_runs.py#L69) | 69 | `""` | — |
| [SRC-70795F4B61-L000070](../../scripts/compare_answer_quality_runs.py#L70) | 70 | `"def _percentile_nearest_rank(values: list[float], percentile: float) -> float \| None:"` | — |
| [SRC-70795F4B61-L000071](../../scripts/compare_answer_quality_runs.py#L71) | 71 | `"    if not values:"` | — |
| [SRC-70795F4B61-L000072](../../scripts/compare_answer_quality_runs.py#L72) | 72 | `"        return None"` | — |
| [SRC-70795F4B61-L000073](../../scripts/compare_answer_quality_runs.py#L73) | 73 | `"    ordered = sorted(values)"` | — |
| [SRC-70795F4B61-L000074](../../scripts/compare_answer_quality_runs.py#L74) | 74 | `"    index = max(0, math.ceil(percentile * len(ordered)) - 1)"` | — |
| [SRC-70795F4B61-L000075](../../scripts/compare_answer_quality_runs.py#L75) | 75 | `"    return round(ordered[index], 2)"` | — |
| [SRC-70795F4B61-L000076](../../scripts/compare_answer_quality_runs.py#L76) | 76 | `""` | — |
| [SRC-70795F4B61-L000077](../../scripts/compare_answer_quality_runs.py#L77) | 77 | `""` | — |
| [SRC-70795F4B61-L000078](../../scripts/compare_answer_quality_runs.py#L78) | 78 | `"def _rate(numerator: int, denominator: int) -> dict[str, Any]:"` | — |
| [SRC-70795F4B61-L000079](../../scripts/compare_answer_quality_runs.py#L79) | 79 | `"    return {"` | — |
| [SRC-70795F4B61-L000080](../../scripts/compare_answer_quality_runs.py#L80) | 80 | `"        \"score\": round(numerator / denominator, 4) if denominator else None,"` | — |
| [SRC-70795F4B61-L000081](../../scripts/compare_answer_quality_runs.py#L81) | 81 | `"        \"numerator\": numerator,"` | — |
| [SRC-70795F4B61-L000082](../../scripts/compare_answer_quality_runs.py#L82) | 82 | `"        \"denominator\": denominator,"` | — |
| [SRC-70795F4B61-L000083](../../scripts/compare_answer_quality_runs.py#L83) | 83 | `"        \"status\": \"SCORED\" if denominator else \"NOT_SCORABLE_NO_DENOMINATOR\","` | — |
| [SRC-70795F4B61-L000084](../../scripts/compare_answer_quality_runs.py#L84) | 84 | `"    }"` | — |
| [SRC-70795F4B61-L000085](../../scripts/compare_answer_quality_runs.py#L85) | 85 | `""` | — |
| [SRC-70795F4B61-L000086](../../scripts/compare_answer_quality_runs.py#L86) | 86 | `""` | — |
| [SRC-70795F4B61-L000087](../../scripts/compare_answer_quality_runs.py#L87) | 87 | `"def run_metrics(run: dict[str, Any]) -> dict[str, Any]:"` | — |
| [SRC-70795F4B61-L000088](../../scripts/compare_answer_quality_runs.py#L88) | 88 | `"    results = run[\"results\"]"` | — |
| [SRC-70795F4B61-L000089](../../scripts/compare_answer_quality_runs.py#L89) | 89 | `"    transport_ok = [r for r in results if r.get(\"transport_ok\") is True]"` | — |
| [SRC-70795F4B61-L000090](../../scripts/compare_answer_quality_runs.py#L90) | 90 | `"    elapsed = ["` | — |
| [SRC-70795F4B61-L000091](../../scripts/compare_answer_quality_runs.py#L91) | 91 | `"        float(value)"` | — |
| [SRC-70795F4B61-L000092](../../scripts/compare_answer_quality_runs.py#L92) | 92 | `"        for record in results"` | — |
| [SRC-70795F4B61-L000093](../../scripts/compare_answer_quality_runs.py#L93) | 93 | `"        if (value := _finite_nonnegative(record.get(\"elapsed_ms\"))) is not None"` | — |
| [SRC-70795F4B61-L000094](../../scripts/compare_answer_quality_runs.py#L94) | 94 | `"    ]"` | — |
| [SRC-70795F4B61-L000095](../../scripts/compare_answer_quality_runs.py#L95) | 95 | `"    search_cases = [r for r in results if r.get(\"expected_strategy\") == \"web_search\"]"` | — |
| [SRC-70795F4B61-L000096](../../scripts/compare_answer_quality_runs.py#L96) | 96 | `"    search_attempted = ["` | — |
| [SRC-70795F4B61-L000097](../../scripts/compare_answer_quality_runs.py#L97) | 97 | `"        r for r in search_cases"` | — |
| [SRC-70795F4B61-L000098](../../scripts/compare_answer_quality_runs.py#L98) | 98 | `"        if r.get(\"search_outcome\") not in (None, \"\", \"unknown\", \"not_attempted\")"` | — |
| [SRC-70795F4B61-L000099](../../scripts/compare_answer_quality_runs.py#L99) | 99 | `"    ]"` | — |
| [SRC-70795F4B61-L000100](../../scripts/compare_answer_quality_runs.py#L100) | 100 | `"    usable = [r for r in search_cases if r.get(\"tool_status\") == \"SUCCESS_WITH_USABLE_RESULTS\"]"` | — |
| [SRC-70795F4B61-L000101](../../scripts/compare_answer_quality_runs.py#L101) | 101 | `"    tool_failed = [r for r in search_cases if r.get(\"tool_status\") == \"TOOL_FAILED\"]"` | — |
| [SRC-70795F4B61-L000102](../../scripts/compare_answer_quality_runs.py#L102) | 102 | `"    no_usable = [r for r in search_cases if r.get(\"tool_status\") == \"ATTEMPTED_NO_USABLE_RESULTS\"]"` | — |
| [SRC-70795F4B61-L000103](../../scripts/compare_answer_quality_runs.py#L103) | 103 | `"    costs = ["` | — |
| [SRC-70795F4B61-L000104](../../scripts/compare_answer_quality_runs.py#L104) | 104 | `"        float(value)"` | — |
| [SRC-70795F4B61-L000105](../../scripts/compare_answer_quality_runs.py#L105) | 105 | `"        for record in results"` | — |
| [SRC-70795F4B61-L000106](../../scripts/compare_answer_quality_runs.py#L106) | 106 | `"        if (value := _finite_nonnegative(record.get(\"provider_reported_model_cost_usd\"))) is not None"` | — |
| [SRC-70795F4B61-L000107](../../scripts/compare_answer_quality_runs.py#L107) | 107 | `"    ]"` | — |
| [SRC-70795F4B61-L000108](../../scripts/compare_answer_quality_runs.py#L108) | 108 | `"    complete_cost_cases = sum("` | — |
| [SRC-70795F4B61-L000109](../../scripts/compare_answer_quality_runs.py#L109) | 109 | `"        1 for r in results"` | — |
| [SRC-70795F4B61-L000110](../../scripts/compare_answer_quality_runs.py#L110) | 110 | `"        if r.get(\"provider_reported_model_cost_status\") == \"COMPLETE_FOR_RETURNED_MODEL_CALLS\""` | — |
| [SRC-70795F4B61-L000111](../../scripts/compare_answer_quality_runs.py#L111) | 111 | `"    )"` | — |
| [SRC-70795F4B61-L000112](../../scripts/compare_answer_quality_runs.py#L112) | 112 | `"    reconciled_request_costs = ["` | — |
| [SRC-70795F4B61-L000113](../../scripts/compare_answer_quality_runs.py#L113) | 113 | `"        float(value)"` | — |
| [SRC-70795F4B61-L000114](../../scripts/compare_answer_quality_runs.py#L114) | 114 | `"        for record in results"` | — |
| [SRC-70795F4B61-L000115](../../scripts/compare_answer_quality_runs.py#L115) | 115 | `"        if record.get(\"request_cost_status\") == \"RECONCILED_COMPLETE_REQUEST_COST\""` | — |
| [SRC-70795F4B61-L000116](../../scripts/compare_answer_quality_runs.py#L116) | 116 | `"        and (value := _finite_nonnegative(record.get(\"request_cost_usd\"))) is not None"` | — |
| [SRC-70795F4B61-L000117](../../scripts/compare_answer_quality_runs.py#L117) | 117 | `"    ]"` | — |
| [SRC-70795F4B61-L000118](../../scripts/compare_answer_quality_runs.py#L118) | 118 | `"    complete_request_cost_count = len(reconciled_request_costs)"` | — |
| [SRC-70795F4B61-L000119](../../scripts/compare_answer_quality_runs.py#L119) | 119 | `"    request_cost_complete = complete_request_cost_count == len(results)"` | — |
| [SRC-70795F4B61-L000120](../../scripts/compare_answer_quality_runs.py#L120) | 120 | `"    return {"` | — |
| [SRC-70795F4B61-L000121](../../scripts/compare_answer_quality_runs.py#L121) | 121 | `"        \"case_count\": len(results),"` | — |
| [SRC-70795F4B61-L000122](../../scripts/compare_answer_quality_runs.py#L122) | 122 | `"        \"transport_success_rate\": _rate(len(transport_ok), len(results)),"` | — |
| [SRC-70795F4B61-L000123](../../scripts/compare_answer_quality_runs.py#L123) | 123 | `"        \"latency_ms\": {"` | — |
| [SRC-70795F4B61-L000124](../../scripts/compare_answer_quality_runs.py#L124) | 124 | `"            \"sample_count\": len(elapsed),"` | — |
| [SRC-70795F4B61-L000125](../../scripts/compare_answer_quality_runs.py#L125) | 125 | `"            \"mean\": round(sum(elapsed) / len(elapsed), 2) if elapsed else None,"` | — |
| [SRC-70795F4B61-L000126](../../scripts/compare_answer_quality_runs.py#L126) | 126 | `"            \"p50\": _percentile_nearest_rank(elapsed, 0.50),"` | — |
| [SRC-70795F4B61-L000127](../../scripts/compare_answer_quality_runs.py#L127) | 127 | `"            \"p95\": _percentile_nearest_rank(elapsed, 0.95),"` | — |
| [SRC-70795F4B61-L000128](../../scripts/compare_answer_quality_runs.py#L128) | 128 | `"            \"max\": round(max(elapsed), 2) if elapsed else None,"` | — |
| [SRC-70795F4B61-L000129](../../scripts/compare_answer_quality_runs.py#L129) | 129 | `"            \"status\": \"SCORED\" if elapsed else \"NOT_MEASURED\","` | — |
| [SRC-70795F4B61-L000130](../../scripts/compare_answer_quality_runs.py#L130) | 130 | `"            \"semantics\": \"Sequential end-to-end HTTP request time; not a concurrency/load test.\","` | — |
| [SRC-70795F4B61-L000131](../../scripts/compare_answer_quality_runs.py#L131) | 131 | `"        },"` | — |
| [SRC-70795F4B61-L000132](../../scripts/compare_answer_quality_runs.py#L132) | 132 | `"        \"tool_usage\": {"` | — |
| [SRC-70795F4B61-L000133](../../scripts/compare_answer_quality_runs.py#L133) | 133 | `"            \"web_search_case_count\": len(search_cases),"` | — |
| [SRC-70795F4B61-L000134](../../scripts/compare_answer_quality_runs.py#L134) | 134 | `"            \"search_attempt_rate\": _rate(len(search_attempted), len(search_cases)),"` | — |
| [SRC-70795F4B61-L000135](../../scripts/compare_answer_quality_runs.py#L135) | 135 | `"            \"usable_result_rate\": _rate(len(usable), len(search_cases)),"` | — |
| [SRC-70795F4B61-L000136](../../scripts/compare_answer_quality_runs.py#L136) | 136 | `"            \"tool_error_rate_among_search_cases\": _rate(len(tool_failed), len(search_cases)),"` | — |
| [SRC-70795F4B61-L000137](../../scripts/compare_answer_quality_runs.py#L137) | 137 | `"            \"attempted_without_usable_results\": len(no_usable),"` | — |
| [SRC-70795F4B61-L000138](../../scripts/compare_answer_quality_runs.py#L138) | 138 | `"            \"unknown_tool_outcome_count\": sum("` | — |
| [SRC-70795F4B61-L000139](../../scripts/compare_answer_quality_runs.py#L139) | 139 | `"                1 for r in search_cases"` | — |
| [SRC-70795F4B61-L000140](../../scripts/compare_answer_quality_runs.py#L140) | 140 | `"                if r.get(\"tool_status\") in (None, \"\", \"UNKNOWN\")"` | — |
| [SRC-70795F4B61-L000141](../../scripts/compare_answer_quality_runs.py#L141) | 141 | `"            ),"` | — |
| [SRC-70795F4B61-L000142](../../scripts/compare_answer_quality_runs.py#L142) | 142 | `"        },"` | — |
| [SRC-70795F4B61-L000143](../../scripts/compare_answer_quality_runs.py#L143) | 143 | `"        \"provider_reported_model_cost\": {"` | — |
| [SRC-70795F4B61-L000144](../../scripts/compare_answer_quality_runs.py#L144) | 144 | `"            \"reported_sum_usd\": round(sum(costs), 10) if costs else None,"` | — |
| [SRC-70795F4B61-L000145](../../scripts/compare_answer_quality_runs.py#L145) | 145 | `"            \"cases_with_any_reported_cost\": len(costs),"` | — |
| [SRC-70795F4B61-L000146](../../scripts/compare_answer_quality_runs.py#L146) | 146 | `"            \"cases_complete_for_returned_model_calls\": complete_cost_cases,"` | — |
| [SRC-70795F4B61-L000147](../../scripts/compare_answer_quality_runs.py#L147) | 147 | `"            \"status\": ("` | — |
| [SRC-70795F4B61-L000148](../../scripts/compare_answer_quality_runs.py#L148) | 148 | `"                \"PARTIAL_OR_PROVIDER_REPORTED_ONLY\""` | — |
| [SRC-70795F4B61-L000149](../../scripts/compare_answer_quality_runs.py#L149) | 149 | `"                if costs"` | — |
| [SRC-70795F4B61-L000150](../../scripts/compare_answer_quality_runs.py#L150) | 150 | `"                else \"NOT_MEASURED_NO_PROVIDER_COST_REPORTED\""` | — |
| [SRC-70795F4B61-L000151](../../scripts/compare_answer_quality_runs.py#L151) | 151 | `"            ),"` | — |
| [SRC-70795F4B61-L000152](../../scripts/compare_answer_quality_runs.py#L152) | 152 | `"            \"complete_request_cost_usd\": ("` | — |
| [SRC-70795F4B61-L000153](../../scripts/compare_answer_quality_runs.py#L153) | 153 | `"                round(sum(reconciled_request_costs), 10) if request_cost_complete else None"` | — |
| [SRC-70795F4B61-L000154](../../scripts/compare_answer_quality_runs.py#L154) | 154 | `"            ),"` | — |
| [SRC-70795F4B61-L000155](../../scripts/compare_answer_quality_runs.py#L155) | 155 | `"            \"complete_request_cost_status\": ("` | — |
| [SRC-70795F4B61-L000156](../../scripts/compare_answer_quality_runs.py#L156) | 156 | `"                \"RECONCILED_COMPLETE_REQUEST_COST\""` | — |
| [SRC-70795F4B61-L000157](../../scripts/compare_answer_quality_runs.py#L157) | 157 | `"                if request_cost_complete"` | — |
| [SRC-70795F4B61-L000158](../../scripts/compare_answer_quality_runs.py#L158) | 158 | `"                else ("` | — |
| [SRC-70795F4B61-L000159](../../scripts/compare_answer_quality_runs.py#L159) | 159 | `"                    \"PARTIAL_EXTERNAL_COST_RECONCILIATION\""` | — |
| [SRC-70795F4B61-L000160](../../scripts/compare_answer_quality_runs.py#L160) | 160 | `"                    if complete_request_cost_count"` | — |
| [SRC-70795F4B61-L000161](../../scripts/compare_answer_quality_runs.py#L161) | 161 | `"                    else \"NOT_MEASURED_TOTAL_CONNECTOR_COSTS_NOT_EXPOSED\""` | — |
| [SRC-70795F4B61-L000162](../../scripts/compare_answer_quality_runs.py#L162) | 162 | `"                )"` | — |
| [SRC-70795F4B61-L000163](../../scripts/compare_answer_quality_runs.py#L163) | 163 | `"            ),"` | — |
| [SRC-70795F4B61-L000164](../../scripts/compare_answer_quality_runs.py#L164) | 164 | `"            \"complete_request_cost_case_count\": complete_request_cost_count,"` | — |
| [SRC-70795F4B61-L000165](../../scripts/compare_answer_quality_runs.py#L165) | 165 | `"        },"` | — |
| [SRC-70795F4B61-L000166](../../scripts/compare_answer_quality_runs.py#L166) | 166 | `"    }"` | — |
| [SRC-70795F4B61-L000167](../../scripts/compare_answer_quality_runs.py#L167) | 167 | `""` | — |
| [SRC-70795F4B61-L000168](../../scripts/compare_answer_quality_runs.py#L168) | 168 | `""` | — |
| [SRC-70795F4B61-L000169](../../scripts/compare_answer_quality_runs.py#L169) | 169 | `"def _load_review_scorer():"` | — |
| [SRC-70795F4B61-L000170](../../scripts/compare_answer_quality_runs.py#L170) | 170 | `"    path = ROOT / \"scripts\" / \"score_answer_quality_reviews.py\""` | — |
| [SRC-70795F4B61-L000171](../../scripts/compare_answer_quality_runs.py#L171) | 171 | `"    spec = importlib.util.spec_from_file_location(\"omarai_review_scorecard\", path)"` | — |
| [SRC-70795F4B61-L000172](../../scripts/compare_answer_quality_runs.py#L172) | 172 | `"    if spec is None or spec.loader is None:"` | — |
| [SRC-70795F4B61-L000173](../../scripts/compare_answer_quality_runs.py#L173) | 173 | `"        raise RuntimeError(\"Unable to load existing review scorecard: \" + str(path))"` | — |
| [SRC-70795F4B61-L000174](../../scripts/compare_answer_quality_runs.py#L174) | 174 | `"    module = importlib.util.module_from_spec(spec)"` | — |
| [SRC-70795F4B61-L000175](../../scripts/compare_answer_quality_runs.py#L175) | 175 | `"    spec.loader.exec_module(module)"` | — |
| [SRC-70795F4B61-L000176](../../scripts/compare_answer_quality_runs.py#L176) | 176 | `"    return module"` | — |
| [SRC-70795F4B61-L000177](../../scripts/compare_answer_quality_runs.py#L177) | 177 | `""` | — |
| [SRC-70795F4B61-L000178](../../scripts/compare_answer_quality_runs.py#L178) | 178 | `""` | — |
| [SRC-70795F4B61-L000179](../../scripts/compare_answer_quality_runs.py#L179) | 179 | `"def _reviewed_case_ids(review_data: dict[str, Any]) -> set[str]:"` | — |
| [SRC-70795F4B61-L000180](../../scripts/compare_answer_quality_runs.py#L180) | 180 | `"    reviews = review_data.get(\"reviews\")"` | — |
| [SRC-70795F4B61-L000181](../../scripts/compare_answer_quality_runs.py#L181) | 181 | `"    if not isinstance(reviews, list):"` | — |
| [SRC-70795F4B61-L000182](../../scripts/compare_answer_quality_runs.py#L182) | 182 | `"        raise ValueError(\"review file must contain a reviews array\")"` | — |
| [SRC-70795F4B61-L000183](../../scripts/compare_answer_quality_runs.py#L183) | 183 | `"    return {"` | — |
| [SRC-70795F4B61-L000184](../../scripts/compare_answer_quality_runs.py#L184) | 184 | `"        item[\"case_id\"]"` | — |
| [SRC-70795F4B61-L000185](../../scripts/compare_answer_quality_runs.py#L185) | 185 | `"        for item in reviews"` | — |
| [SRC-70795F4B61-L000186](../../scripts/compare_answer_quality_runs.py#L186) | 186 | `"        if isinstance(item, dict) and item.get(\"status\") == \"REVIEWED\""` | — |
| [SRC-70795F4B61-L000187](../../scripts/compare_answer_quality_runs.py#L187) | 187 | `"        and isinstance(item.get(\"case_id\"), str)"` | — |
| [SRC-70795F4B61-L000188](../../scripts/compare_answer_quality_runs.py#L188) | 188 | `"    }"` | — |
| [SRC-70795F4B61-L000189](../../scripts/compare_answer_quality_runs.py#L189) | 189 | `""` | — |
| [SRC-70795F4B61-L000190](../../scripts/compare_answer_quality_runs.py#L190) | 190 | `""` | — |
| [SRC-70795F4B61-L000191](../../scripts/compare_answer_quality_runs.py#L191) | 191 | `"def review_comparison("` | — |
| [SRC-70795F4B61-L000192](../../scripts/compare_answer_quality_runs.py#L192) | 192 | `"    baseline_reviews: dict[str, Any],"` | — |
| [SRC-70795F4B61-L000193](../../scripts/compare_answer_quality_runs.py#L193) | 193 | `"    candidate_reviews: dict[str, Any],"` | — |
| [SRC-70795F4B61-L000194](../../scripts/compare_answer_quality_runs.py#L194) | 194 | `"    corpus: dict[str, Any],"` | — |
| [SRC-70795F4B61-L000195](../../scripts/compare_answer_quality_runs.py#L195) | 195 | `") -> dict[str, Any]:"` | — |
| [SRC-70795F4B61-L000196](../../scripts/compare_answer_quality_runs.py#L196) | 196 | `"    baseline_ids = _reviewed_case_ids(baseline_reviews)"` | — |
| [SRC-70795F4B61-L000197](../../scripts/compare_answer_quality_runs.py#L197) | 197 | `"    candidate_ids = _reviewed_case_ids(candidate_reviews)"` | — |
| [SRC-70795F4B61-L000198](../../scripts/compare_answer_quality_runs.py#L198) | 198 | `"    if not baseline_ids or not candidate_ids:"` | — |
| [SRC-70795F4B61-L000199](../../scripts/compare_answer_quality_runs.py#L199) | 199 | `"        raise ValueError(\"both review files need explicitly REVIEWED cases\")"` | — |
| [SRC-70795F4B61-L000200](../../scripts/compare_answer_quality_runs.py#L200) | 200 | `"    if baseline_ids != candidate_ids:"` | — |
| [SRC-70795F4B61-L000201](../../scripts/compare_answer_quality_runs.py#L201) | 201 | `"        raise ValueError("` | — |
| [SRC-70795F4B61-L000202](../../scripts/compare_answer_quality_runs.py#L202) | 202 | `"            \"incomparable review coverage: REVIEWED case IDs differ between baseline and candidate\""` | — |
| [SRC-70795F4B61-L000203](../../scripts/compare_answer_quality_runs.py#L203) | 203 | `"        )"` | — |
| [SRC-70795F4B61-L000204](../../scripts/compare_answer_quality_runs.py#L204) | 204 | `"    corpus_cases = corpus.get(\"cases\")"` | — |
| [SRC-70795F4B61-L000205](../../scripts/compare_answer_quality_runs.py#L205) | 205 | `"    if not isinstance(corpus_cases, list) or not corpus_cases:"` | — |
| [SRC-70795F4B61-L000206](../../scripts/compare_answer_quality_runs.py#L206) | 206 | `"        raise ValueError(\"corpus must contain a non-empty cases array for full-coverage acceptance\")"` | — |
| [SRC-70795F4B61-L000207](../../scripts/compare_answer_quality_runs.py#L207) | 207 | `"    corpus_ids = {"` | — |
| [SRC-70795F4B61-L000208](../../scripts/compare_answer_quality_runs.py#L208) | 208 | `"        item.get(\"case_id\")"` | — |
| [SRC-70795F4B61-L000209](../../scripts/compare_answer_quality_runs.py#L209) | 209 | `"        for item in corpus_cases"` | — |
| [SRC-70795F4B61-L000210](../../scripts/compare_answer_quality_runs.py#L210) | 210 | `"        if isinstance(item, dict) and isinstance(item.get(\"case_id\"), str)"` | — |
| [SRC-70795F4B61-L000211](../../scripts/compare_answer_quality_runs.py#L211) | 211 | `"    }"` | — |
| [SRC-70795F4B61-L000212](../../scripts/compare_answer_quality_runs.py#L212) | 212 | `"    if baseline_ids != corpus_ids:"` | — |
| [SRC-70795F4B61-L000213](../../scripts/compare_answer_quality_runs.py#L213) | 213 | `"        missing = sorted(corpus_ids - baseline_ids)"` | — |
| [SRC-70795F4B61-L000214](../../scripts/compare_answer_quality_runs.py#L214) | 214 | `"        extra = sorted(baseline_ids - corpus_ids)"` | — |
| [SRC-70795F4B61-L000215](../../scripts/compare_answer_quality_runs.py#L215) | 215 | `"        raise ValueError("` | — |
| [SRC-70795F4B61-L000216](../../scripts/compare_answer_quality_runs.py#L216) | 216 | `"            f\"incomplete human review coverage: missing={missing}; unknown={extra}\""` | — |
| [SRC-70795F4B61-L000217](../../scripts/compare_answer_quality_runs.py#L217) | 217 | `"        )"` | — |
| [SRC-70795F4B61-L000218](../../scripts/compare_answer_quality_runs.py#L218) | 218 | `"    scorer = _load_review_scorer()"` | — |
| [SRC-70795F4B61-L000219](../../scripts/compare_answer_quality_runs.py#L219) | 219 | `"    baseline = scorer.summarize_reviews(baseline_reviews, corpus)"` | — |
| [SRC-70795F4B61-L000220](../../scripts/compare_answer_quality_runs.py#L220) | 220 | `"    candidate = scorer.summarize_reviews(candidate_reviews, corpus)"` | — |
| [SRC-70795F4B61-L000221](../../scripts/compare_answer_quality_runs.py#L221) | 221 | `"    aliases = {"` | — |
| [SRC-70795F4B61-L000222](../../scripts/compare_answer_quality_runs.py#L222) | 222 | `"        \"retrieval_precision\": \"retrieval_precision\","` | — |
| [SRC-70795F4B61-L000223](../../scripts/compare_answer_quality_runs.py#L223) | 223 | `"        \"retrieval_recall\": \"retrieval_recall\","` | — |
| [SRC-70795F4B61-L000224](../../scripts/compare_answer_quality_runs.py#L224) | 224 | `"        \"factual_accuracy\": \"correctness\","` | — |
| [SRC-70795F4B61-L000225](../../scripts/compare_answer_quality_runs.py#L225) | 225 | `"        \"faithfulness\": \"faithfulness\","` | — |
| [SRC-70795F4B61-L000226](../../scripts/compare_answer_quality_runs.py#L226) | 226 | `"        \"citation_support\": \"citation_support\","` | — |
| [SRC-70795F4B61-L000227](../../scripts/compare_answer_quality_runs.py#L227) | 227 | `"        \"writing_quality_1_to_5\": \"writing_quality_1_to_5\","` | — |
| [SRC-70795F4B61-L000228](../../scripts/compare_answer_quality_runs.py#L228) | 228 | `"    }"` | — |
| [SRC-70795F4B61-L000229](../../scripts/compare_answer_quality_runs.py#L229) | 229 | `"    metrics: dict[str, Any] = {}"` | — |
| [SRC-70795F4B61-L000230](../../scripts/compare_answer_quality_runs.py#L230) | 230 | `"    for output_name, score_name in aliases.items():"` | — |
| [SRC-70795F4B61-L000231](../../scripts/compare_answer_quality_runs.py#L231) | 231 | `"        before = baseline[\"metrics\"][score_name][\"score\"]"` | — |
| [SRC-70795F4B61-L000232](../../scripts/compare_answer_quality_runs.py#L232) | 232 | `"        after = candidate[\"metrics\"][score_name][\"score\"]"` | — |
| [SRC-70795F4B61-L000233](../../scripts/compare_answer_quality_runs.py#L233) | 233 | `"        metrics[output_name] = {"` | — |
| [SRC-70795F4B61-L000234](../../scripts/compare_answer_quality_runs.py#L234) | 234 | `"            \"baseline\": before,"` | — |
| [SRC-70795F4B61-L000235](../../scripts/compare_answer_quality_runs.py#L235) | 235 | `"            \"candidate\": after,"` | — |
| [SRC-70795F4B61-L000236](../../scripts/compare_answer_quality_runs.py#L236) | 236 | `"            \"delta\": round(after - before, 4) if before is not None and after is not None else None,"` | — |
| [SRC-70795F4B61-L000237](../../scripts/compare_answer_quality_runs.py#L237) | 237 | `"            \"status\": ("` | — |
| [SRC-70795F4B61-L000238](../../scripts/compare_answer_quality_runs.py#L238) | 238 | `"                \"COMPARED\" if before is not None and after is not None"` | — |
| [SRC-70795F4B61-L000239](../../scripts/compare_answer_quality_runs.py#L239) | 239 | `"                else \"NOT_SCORABLE_MISSING_ANNOTATED_DENOMINATOR\""` | — |
| [SRC-70795F4B61-L000240](../../scripts/compare_answer_quality_runs.py#L240) | 240 | `"            ),"` | — |
| [SRC-70795F4B61-L000241](../../scripts/compare_answer_quality_runs.py#L241) | 241 | `"            \"source\": \"explicit_human_review\","` | — |
| [SRC-70795F4B61-L000242](../../scripts/compare_answer_quality_runs.py#L242) | 242 | `"        }"` | — |
| [SRC-70795F4B61-L000243](../../scripts/compare_answer_quality_runs.py#L243) | 243 | `"    return {"` | — |
| [SRC-70795F4B61-L000244](../../scripts/compare_answer_quality_runs.py#L244) | 244 | `"        \"reviewed_case_count\": len(baseline_ids),"` | — |
| [SRC-70795F4B61-L000245](../../scripts/compare_answer_quality_runs.py#L245) | 245 | `"        \"baseline_review_coverage\": baseline[\"reviewed_case_coverage\"],"` | — |
| [SRC-70795F4B61-L000246](../../scripts/compare_answer_quality_runs.py#L246) | 246 | `"        \"candidate_review_coverage\": candidate[\"reviewed_case_coverage\"],"` | — |
| [SRC-70795F4B61-L000247](../../scripts/compare_answer_quality_runs.py#L247) | 247 | `"        \"metrics\": metrics,"` | — |
| [SRC-70795F4B61-L000248](../../scripts/compare_answer_quality_runs.py#L248) | 248 | `"        \"automatic_answer_grading\": False,"` | — |
| [SRC-70795F4B61-L000249](../../scripts/compare_answer_quality_runs.py#L249) | 249 | `"        \"limitations\": ["` | — |
| [SRC-70795F4B61-L000250](../../scripts/compare_answer_quality_runs.py#L250) | 250 | `"            \"Scores reflect explicit human annotations, not automatic model grading.\","` | — |
| [SRC-70795F4B61-L000251](../../scripts/compare_answer_quality_runs.py#L251) | 251 | `"            \"Retrieval precision/recall require comparable candidate pools and relevance judgments.\","` | — |
| [SRC-70795F4B61-L000252](../../scripts/compare_answer_quality_runs.py#L252) | 252 | `"            \"Citation support measures reviewer-labelled citations that support the associated claims; URL presence alone is not evidence of support.\","` | — |
| [SRC-70795F4B61-L000253](../../scripts/compare_answer_quality_runs.py#L253) | 253 | `"        ],"` | — |
| [SRC-70795F4B61-L000254](../../scripts/compare_answer_quality_runs.py#L254) | 254 | `"    }"` | — |
| [SRC-70795F4B61-L000255](../../scripts/compare_answer_quality_runs.py#L255) | 255 | `""` | — |
| [SRC-70795F4B61-L000256](../../scripts/compare_answer_quality_runs.py#L256) | 256 | `""` | — |
| [SRC-70795F4B61-L000257](../../scripts/compare_answer_quality_runs.py#L257) | 257 | `"def compare_runs("` | — |
| [SRC-70795F4B61-L000258](../../scripts/compare_answer_quality_runs.py#L258) | 258 | `"    baseline: dict[str, Any],"` | — |
| [SRC-70795F4B61-L000259](../../scripts/compare_answer_quality_runs.py#L259) | 259 | `"    candidate: dict[str, Any],"` | — |
| [SRC-70795F4B61-L000260](../../scripts/compare_answer_quality_runs.py#L260) | 260 | `"    *,"` | — |
| [SRC-70795F4B61-L000261](../../scripts/compare_answer_quality_runs.py#L261) | 261 | `"    corpus: dict[str, Any] \| None = None,"` | — |
| [SRC-70795F4B61-L000262](../../scripts/compare_answer_quality_runs.py#L262) | 262 | `"    baseline_reviews: dict[str, Any] \| None = None,"` | — |
| [SRC-70795F4B61-L000263](../../scripts/compare_answer_quality_runs.py#L263) | 263 | `"    candidate_reviews: dict[str, Any] \| None = None,"` | — |
| [SRC-70795F4B61-L000264](../../scripts/compare_answer_quality_runs.py#L264) | 264 | `") -> dict[str, Any]:"` | — |
| [SRC-70795F4B61-L000265](../../scripts/compare_answer_quality_runs.py#L265) | 265 | `"    problems = validate_run(baseline, \"baseline\") + validate_run(candidate, \"candidate\")"` | — |
| [SRC-70795F4B61-L000266](../../scripts/compare_answer_quality_runs.py#L266) | 266 | `"    if problems:"` | — |
| [SRC-70795F4B61-L000267](../../scripts/compare_answer_quality_runs.py#L267) | 267 | `"        raise ValueError(\"; \".join(problems))"` | — |
| [SRC-70795F4B61-L000268](../../scripts/compare_answer_quality_runs.py#L268) | 268 | `"    if baseline.get(\"benchmark_id\") != candidate.get(\"benchmark_id\"):"` | — |
| [SRC-70795F4B61-L000269](../../scripts/compare_answer_quality_runs.py#L269) | 269 | `"        raise ValueError(\"baseline/candidate benchmark_id differs\")"` | — |
| [SRC-70795F4B61-L000270](../../scripts/compare_answer_quality_runs.py#L270) | 270 | `"    if baseline.get(\"benchmark_version\") != candidate.get(\"benchmark_version\"):"` | — |
| [SRC-70795F4B61-L000271](../../scripts/compare_answer_quality_runs.py#L271) | 271 | `"        raise ValueError(\"baseline/candidate benchmark_version differs\")"` | — |
| [SRC-70795F4B61-L000272](../../scripts/compare_answer_quality_runs.py#L272) | 272 | `"    if corpus is not None:"` | — |
| [SRC-70795F4B61-L000273](../../scripts/compare_answer_quality_runs.py#L273) | 273 | `"        if corpus.get(\"benchmark_id\") != baseline.get(\"benchmark_id\"):"` | — |
| [SRC-70795F4B61-L000274](../../scripts/compare_answer_quality_runs.py#L274) | 274 | `"            raise ValueError(\"runs do not match the supplied corpus benchmark_id\")"` | — |
| [SRC-70795F4B61-L000275](../../scripts/compare_answer_quality_runs.py#L275) | 275 | `"        if corpus.get(\"version\") != baseline.get(\"benchmark_version\"):"` | — |
| [SRC-70795F4B61-L000276](../../scripts/compare_answer_quality_runs.py#L276) | 276 | `"            raise ValueError(\"runs do not match the supplied corpus benchmark_version\")"` | — |
| [SRC-70795F4B61-L000277](../../scripts/compare_answer_quality_runs.py#L277) | 277 | `"    baseline_by_id = {row[\"case_id\"]: row for row in baseline[\"results\"]}"` | — |
| [SRC-70795F4B61-L000278](../../scripts/compare_answer_quality_runs.py#L278) | 278 | `"    candidate_by_id = {row[\"case_id\"]: row for row in candidate[\"results\"]}"` | — |
| [SRC-70795F4B61-L000279](../../scripts/compare_answer_quality_runs.py#L279) | 279 | `"    if set(baseline_by_id) != set(candidate_by_id):"` | — |
| [SRC-70795F4B61-L000280](../../scripts/compare_answer_quality_runs.py#L280) | 280 | `"        missing_candidate = sorted(set(baseline_by_id) - set(candidate_by_id))"` | — |
| [SRC-70795F4B61-L000281](../../scripts/compare_answer_quality_runs.py#L281) | 281 | `"        missing_baseline = sorted(set(candidate_by_id) - set(baseline_by_id))"` | — |
| [SRC-70795F4B61-L000282](../../scripts/compare_answer_quality_runs.py#L282) | 282 | `"        raise ValueError("` | — |
| [SRC-70795F4B61-L000283](../../scripts/compare_answer_quality_runs.py#L283) | 283 | `"            f\"incomparable case sets; missing in candidate={missing_candidate}; \""` | — |
| [SRC-70795F4B61-L000284](../../scripts/compare_answer_quality_runs.py#L284) | 284 | `"            f\"missing in baseline={missing_baseline}\""` | — |
| [SRC-70795F4B61-L000285](../../scripts/compare_answer_quality_runs.py#L285) | 285 | `"        )"` | — |
| [SRC-70795F4B61-L000286](../../scripts/compare_answer_quality_runs.py#L286) | 286 | `"    for case_id in baseline_by_id:"` | — |
| [SRC-70795F4B61-L000287](../../scripts/compare_answer_quality_runs.py#L287) | 287 | `"        if baseline_by_id[case_id].get(\"prompt\") != candidate_by_id[case_id].get(\"prompt\"):"` | — |
| [SRC-70795F4B61-L000288](../../scripts/compare_answer_quality_runs.py#L288) | 288 | `"            raise ValueError(f\"incomparable question text for {case_id}\")"` | — |
| [SRC-70795F4B61-L000289](../../scripts/compare_answer_quality_runs.py#L289) | 289 | `""` | — |
| [SRC-70795F4B61-L000290](../../scripts/compare_answer_quality_runs.py#L290) | 290 | `"    before_runtime = run_metrics(baseline)"` | — |
