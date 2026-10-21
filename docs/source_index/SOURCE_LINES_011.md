# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **011**
- سجلات الأسطر: **800**
- النطاق: SRC-E599346ABE-L000183 إلى SRC-E599346ABE-L000982
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## وثائق وفهرسة

### FILE-E599346ABE — [docs/generate_index.py](../generate_index.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-E599346ABE-L000183](../generate_index.py#L183) | 183 | `"    \"\"\"Represent a statically discovered symbol outside the Python AST index.\"\"\""` | — |
| [SRC-E599346ABE-L000184](../generate_index.py#L184) | 184 | `""` | — |
| [SRC-E599346ABE-L000185](../generate_index.py#L185) | 185 | `"    file: str"` | — |
| [SRC-E599346ABE-L000186](../generate_index.py#L186) | 186 | `"    name: str"` | — |
| [SRC-E599346ABE-L000187](../generate_index.py#L187) | 187 | `"    kind: str"` | — |
| [SRC-E599346ABE-L000188](../generate_index.py#L188) | 188 | `"    line: int"` | — |
| [SRC-E599346ABE-L000189](../generate_index.py#L189) | 189 | `""` | — |
| [SRC-E599346ABE-L000190](../generate_index.py#L190) | 190 | `""` | — |
| [SRC-E599346ABE-L000191](../generate_index.py#L191) | 191 | `"@dataclass(frozen=True, slots=True)"` | — |
| [SRC-E599346ABE-L000192](../generate_index.py#L192) | 192 | `"class IndexedLine:"` | — |
| [SRC-E599346ABE-L000193](../generate_index.py#L193) | 193 | `"    \"\"\"Represent one exact logical line from an eligible readable repository text file.\"\"\""` | — |
| [SRC-E599346ABE-L000194](../generate_index.py#L194) | 194 | `""` | — |
| [SRC-E599346ABE-L000195](../generate_index.py#L195) | 195 | `"    file: str"` | — |
| [SRC-E599346ABE-L000196](../generate_index.py#L196) | 196 | `"    file_id: str"` | — |
| [SRC-E599346ABE-L000197](../generate_index.py#L197) | 197 | `"    line_id: str"` | — |
| [SRC-E599346ABE-L000198](../generate_index.py#L198) | 198 | `"    category: str"` | — |
| [SRC-E599346ABE-L000199](../generate_index.py#L199) | 199 | `"    line: int"` | — |
| [SRC-E599346ABE-L000200](../generate_index.py#L200) | 200 | `"    content: str"` | — |
| [SRC-E599346ABE-L000201](../generate_index.py#L201) | 201 | `""` | — |
| [SRC-E599346ABE-L000202](../generate_index.py#L202) | 202 | `""` | — |
| [SRC-E599346ABE-L000203](../generate_index.py#L203) | 203 | `"@dataclass(frozen=True, slots=True)"` | — |
| [SRC-E599346ABE-L000204](../generate_index.py#L204) | 204 | `"class IndexedFinding:"` | — |
| [SRC-E599346ABE-L000205](../generate_index.py#L205) | 205 | `"    \"\"\"Represent a source annotation that explicitly requests attention.\"\"\""` | — |
| [SRC-E599346ABE-L000206](../generate_index.py#L206) | 206 | `""` | — |
| [SRC-E599346ABE-L000207](../generate_index.py#L207) | 207 | `"    finding_id: str"` | — |
| [SRC-E599346ABE-L000208](../generate_index.py#L208) | 208 | `"    file: str"` | — |
| [SRC-E599346ABE-L000209](../generate_index.py#L209) | 209 | `"    line_id: str"` | — |
| [SRC-E599346ABE-L000210](../generate_index.py#L210) | 210 | `"    marker: str"` | — |
| [SRC-E599346ABE-L000211](../generate_index.py#L211) | 211 | `"    description: str"` | — |
| [SRC-E599346ABE-L000212](../generate_index.py#L212) | 212 | `""` | — |
| [SRC-E599346ABE-L000213](../generate_index.py#L213) | 213 | `""` | — |
| [SRC-E599346ABE-L000214](../generate_index.py#L214) | 214 | `"class IndexGenerationError(RuntimeError):"` | — |
| [SRC-E599346ABE-L000215](../generate_index.py#L215) | 215 | `"    \"\"\"Signal that a complete Python AST index could not be generated.\"\"\""` | — |
| [SRC-E599346ABE-L000216](../generate_index.py#L216) | 216 | `""` | — |
| [SRC-E599346ABE-L000217](../generate_index.py#L217) | 217 | `""` | — |
| [SRC-E599346ABE-L000218](../generate_index.py#L218) | 218 | `"class SymbolVisitor(ast.NodeVisitor):"` | — |
| [SRC-E599346ABE-L000219](../generate_index.py#L219) | 219 | `"    \"\"\"Collect Python classes, functions, methods and module/class assignments.\"\"\""` | — |
| [SRC-E599346ABE-L000220](../generate_index.py#L220) | 220 | `""` | — |
| [SRC-E599346ABE-L000221](../generate_index.py#L221) | 221 | `"    def __init__(self, relative_file: str) -> None:"` | — |
| [SRC-E599346ABE-L000222](../generate_index.py#L222) | 222 | `"        \"\"\"Initialize the visitor for one repository-relative Python file.\"\"\""` | — |
| [SRC-E599346ABE-L000223](../generate_index.py#L223) | 223 | `"        self.relative_file = relative_file"` | — |
| [SRC-E599346ABE-L000224](../generate_index.py#L224) | 224 | `"        self.symbols: list[IndexedSymbol] = []"` | — |
| [SRC-E599346ABE-L000225](../generate_index.py#L225) | 225 | `"        self.scope: list[str] = []"` | — |
| [SRC-E599346ABE-L000226](../generate_index.py#L226) | 226 | `"        self.function_depth = 0"` | — |
| [SRC-E599346ABE-L000227](../generate_index.py#L227) | 227 | `""` | — |
| [SRC-E599346ABE-L000228](../generate_index.py#L228) | 228 | `"    @staticmethod"` | — |
| [SRC-E599346ABE-L000229](../generate_index.py#L229) | 229 | `"    def _description(node: ast.AST) -> tuple[str, bool]:"` | — |
| [SRC-E599346ABE-L000230](../generate_index.py#L230) | 230 | `"        \"\"\"Return a compact first-paragraph summary and its documentation state.\"\"\""` | — |
| [SRC-E599346ABE-L000231](../generate_index.py#L231) | 231 | `"        docstring = ast.get_docstring(node, clean=True)"` | — |
| [SRC-E599346ABE-L000232](../generate_index.py#L232) | 232 | `"        if not docstring or not docstring.strip():"` | — |
| [SRC-E599346ABE-L000233](../generate_index.py#L233) | 233 | `"            return \"لا توجد Docstring.\", False"` | — |
| [SRC-E599346ABE-L000234](../generate_index.py#L234) | 234 | `""` | — |
| [SRC-E599346ABE-L000235](../generate_index.py#L235) | 235 | `"        first_paragraph = docstring.strip().split(\"\\n\\n\", maxsplit=1)[0]"` | — |
| [SRC-E599346ABE-L000236](../generate_index.py#L236) | 236 | `"        summary = \" \".join(first_paragraph.split())"` | — |
| [SRC-E599346ABE-L000237](../generate_index.py#L237) | 237 | `"        if len(summary) > MAX_DESCRIPTION_LENGTH:"` | — |
| [SRC-E599346ABE-L000238](../generate_index.py#L238) | 238 | `"            summary = summary[: MAX_DESCRIPTION_LENGTH - 3].rstrip() + \"...\""` | — |
| [SRC-E599346ABE-L000239](../generate_index.py#L239) | 239 | `"        return summary, True"` | — |
| [SRC-E599346ABE-L000240](../generate_index.py#L240) | 240 | `""` | — |
| [SRC-E599346ABE-L000241](../generate_index.py#L241) | 241 | `"    def _record_definition("` | — |
| [SRC-E599346ABE-L000242](../generate_index.py#L242) | 242 | `"        self,"` | — |
| [SRC-E599346ABE-L000243](../generate_index.py#L243) | 243 | `"        node: ast.ClassDef \| ast.FunctionDef \| ast.AsyncFunctionDef,"` | — |
| [SRC-E599346ABE-L000244](../generate_index.py#L244) | 244 | `"        kind: str,"` | — |
| [SRC-E599346ABE-L000245](../generate_index.py#L245) | 245 | `"    ) -> None:"` | — |
| [SRC-E599346ABE-L000246](../generate_index.py#L246) | 246 | `"        \"\"\"Record one class/function definition while preserving its qualified scope.\"\"\""` | — |
| [SRC-E599346ABE-L000247](../generate_index.py#L247) | 247 | `"        description, documented = self._description(node)"` | — |
| [SRC-E599346ABE-L000248](../generate_index.py#L248) | 248 | `"        qualified_name = \".\".join((*self.scope, node.name))"` | — |
| [SRC-E599346ABE-L000249](../generate_index.py#L249) | 249 | `"        self.symbols.append("` | — |
| [SRC-E599346ABE-L000250](../generate_index.py#L250) | 250 | `"            IndexedSymbol("` | — |
| [SRC-E599346ABE-L000251](../generate_index.py#L251) | 251 | `"                file=self.relative_file,"` | — |
| [SRC-E599346ABE-L000252](../generate_index.py#L252) | 252 | `"                name=qualified_name,"` | — |
| [SRC-E599346ABE-L000253](../generate_index.py#L253) | 253 | `"                kind=kind,"` | — |
| [SRC-E599346ABE-L000254](../generate_index.py#L254) | 254 | `"                line=node.lineno,"` | — |
| [SRC-E599346ABE-L000255](../generate_index.py#L255) | 255 | `"                description=description,"` | — |
| [SRC-E599346ABE-L000256](../generate_index.py#L256) | 256 | `"                documented=documented,"` | — |
| [SRC-E599346ABE-L000257](../generate_index.py#L257) | 257 | `"            )"` | — |
| [SRC-E599346ABE-L000258](../generate_index.py#L258) | 258 | `"        )"` | — |
| [SRC-E599346ABE-L000259](../generate_index.py#L259) | 259 | `""` | — |
| [SRC-E599346ABE-L000260](../generate_index.py#L260) | 260 | `"    def _record_assignment_target(self, node: ast.AST, line: int) -> None:"` | — |
| [SRC-E599346ABE-L000261](../generate_index.py#L261) | 261 | `"        \"\"\"Record declared names from a module-level or class-level assignment.\"\"\""` | — |
| [SRC-E599346ABE-L000262](../generate_index.py#L262) | 262 | `"        if isinstance(node, ast.Name):"` | — |
| [SRC-E599346ABE-L000263](../generate_index.py#L263) | 263 | `"            qualified_name = \".\".join((*self.scope, node.id))"` | — |
| [SRC-E599346ABE-L000264](../generate_index.py#L264) | 264 | `"            self.symbols.append("` | — |
| [SRC-E599346ABE-L000265](../generate_index.py#L265) | 265 | `"                IndexedSymbol("` | — |
| [SRC-E599346ABE-L000266](../generate_index.py#L266) | 266 | `"                    file=self.relative_file,"` | — |
| [SRC-E599346ABE-L000267](../generate_index.py#L267) | 267 | `"                    name=qualified_name,"` | — |
| [SRC-E599346ABE-L000268](../generate_index.py#L268) | 268 | `"                    kind=\"متغير/ثابت Python\","` | — |
| [SRC-E599346ABE-L000269](../generate_index.py#L269) | 269 | `"                    line=line,"` | — |
| [SRC-E599346ABE-L000270](../generate_index.py#L270) | 270 | `"                    description=\"تعريف على مستوى الوحدة أو الكلاس.\","` | — |
| [SRC-E599346ABE-L000271](../generate_index.py#L271) | 271 | `"                    documented=None,"` | — |
| [SRC-E599346ABE-L000272](../generate_index.py#L272) | 272 | `"                )"` | — |
| [SRC-E599346ABE-L000273](../generate_index.py#L273) | 273 | `"            )"` | — |
| [SRC-E599346ABE-L000274](../generate_index.py#L274) | 274 | `"        elif isinstance(node, (ast.Tuple, ast.List)):"` | — |
| [SRC-E599346ABE-L000275](../generate_index.py#L275) | 275 | `"            for element in node.elts:"` | — |
| [SRC-E599346ABE-L000276](../generate_index.py#L276) | 276 | `"                self._record_assignment_target(element, line)"` | — |
| [SRC-E599346ABE-L000277](../generate_index.py#L277) | 277 | `""` | — |
| [SRC-E599346ABE-L000278](../generate_index.py#L278) | 278 | `"    def visit_Assign(self, node: ast.Assign) -> None:"` | — |
| [SRC-E599346ABE-L000279](../generate_index.py#L279) | 279 | `"        \"\"\"Index module/class assignment names but avoid flooding the index with locals.\"\"\""` | — |
| [SRC-E599346ABE-L000280](../generate_index.py#L280) | 280 | `"        if self.function_depth == 0:"` | — |
| [SRC-E599346ABE-L000281](../generate_index.py#L281) | 281 | `"            for target in node.targets:"` | — |
| [SRC-E599346ABE-L000282](../generate_index.py#L282) | 282 | `"                self._record_assignment_target(target, node.lineno)"` | — |
| [SRC-E599346ABE-L000283](../generate_index.py#L283) | 283 | `"        self.generic_visit(node)"` | — |
| [SRC-E599346ABE-L000284](../generate_index.py#L284) | 284 | `""` | — |
| [SRC-E599346ABE-L000285](../generate_index.py#L285) | 285 | `"    def visit_AnnAssign(self, node: ast.AnnAssign) -> None:"` | — |
| [SRC-E599346ABE-L000286](../generate_index.py#L286) | 286 | `"        \"\"\"Index annotated module/class assignments without counting local variables.\"\"\""` | — |
| [SRC-E599346ABE-L000287](../generate_index.py#L287) | 287 | `"        if self.function_depth == 0:"` | — |
| [SRC-E599346ABE-L000288](../generate_index.py#L288) | 288 | `"            self._record_assignment_target(node.target, node.lineno)"` | — |
| [SRC-E599346ABE-L000289](../generate_index.py#L289) | 289 | `"        self.generic_visit(node)"` | — |
| [SRC-E599346ABE-L000290](../generate_index.py#L290) | 290 | `""` | — |
| [SRC-E599346ABE-L000291](../generate_index.py#L291) | 291 | `"    def visit_ClassDef(self, node: ast.ClassDef) -> None:"` | — |
| [SRC-E599346ABE-L000292](../generate_index.py#L292) | 292 | `"        \"\"\"Record a class and recursively inspect its body.\"\"\""` | — |
| [SRC-E599346ABE-L000293](../generate_index.py#L293) | 293 | `"        self._record_definition(node, \"كلاس\")"` | — |
| [SRC-E599346ABE-L000294](../generate_index.py#L294) | 294 | `"        self.scope.append(node.name)"` | — |
| [SRC-E599346ABE-L000295](../generate_index.py#L295) | 295 | `"        try:"` | — |
| [SRC-E599346ABE-L000296](../generate_index.py#L296) | 296 | `"            self.generic_visit(node)"` | — |
| [SRC-E599346ABE-L000297](../generate_index.py#L297) | 297 | `"        finally:"` | — |
| [SRC-E599346ABE-L000298](../generate_index.py#L298) | 298 | `"            self.scope.pop()"` | — |
| [SRC-E599346ABE-L000299](../generate_index.py#L299) | 299 | `""` | — |
| [SRC-E599346ABE-L000300](../generate_index.py#L300) | 300 | `"    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:"` | — |
| [SRC-E599346ABE-L000301](../generate_index.py#L301) | 301 | `"        \"\"\"Record a synchronous function or method and nested definitions.\"\"\""` | — |
| [SRC-E599346ABE-L000302](../generate_index.py#L302) | 302 | `"        self._record_definition(node, \"دالة\")"` | — |
| [SRC-E599346ABE-L000303](../generate_index.py#L303) | 303 | `"        self.scope.append(node.name)"` | — |
| [SRC-E599346ABE-L000304](../generate_index.py#L304) | 304 | `"        self.function_depth += 1"` | — |
| [SRC-E599346ABE-L000305](../generate_index.py#L305) | 305 | `"        try:"` | — |
| [SRC-E599346ABE-L000306](../generate_index.py#L306) | 306 | `"            self.generic_visit(node)"` | — |
| [SRC-E599346ABE-L000307](../generate_index.py#L307) | 307 | `"        finally:"` | — |
| [SRC-E599346ABE-L000308](../generate_index.py#L308) | 308 | `"            self.function_depth -= 1"` | — |
| [SRC-E599346ABE-L000309](../generate_index.py#L309) | 309 | `"            self.scope.pop()"` | — |
| [SRC-E599346ABE-L000310](../generate_index.py#L310) | 310 | `""` | — |
| [SRC-E599346ABE-L000311](../generate_index.py#L311) | 311 | `"    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:"` | — |
| [SRC-E599346ABE-L000312](../generate_index.py#L312) | 312 | `"        \"\"\"Record an asynchronous function or method and nested definitions.\"\"\""` | — |
| [SRC-E599346ABE-L000313](../generate_index.py#L313) | 313 | `"        self._record_definition(node, \"دالة غير متزامنة\")"` | — |
| [SRC-E599346ABE-L000314](../generate_index.py#L314) | 314 | `"        self.scope.append(node.name)"` | — |
| [SRC-E599346ABE-L000315](../generate_index.py#L315) | 315 | `"        self.function_depth += 1"` | — |
| [SRC-E599346ABE-L000316](../generate_index.py#L316) | 316 | `"        try:"` | — |
| [SRC-E599346ABE-L000317](../generate_index.py#L317) | 317 | `"            self.generic_visit(node)"` | — |
| [SRC-E599346ABE-L000318](../generate_index.py#L318) | 318 | `"        finally:"` | — |
| [SRC-E599346ABE-L000319](../generate_index.py#L319) | 319 | `"            self.function_depth -= 1"` | — |
| [SRC-E599346ABE-L000320](../generate_index.py#L320) | 320 | `"            self.scope.pop()"` | — |
| [SRC-E599346ABE-L000321](../generate_index.py#L321) | 321 | `""` | — |
| [SRC-E599346ABE-L000322](../generate_index.py#L322) | 322 | `""` | — |
| [SRC-E599346ABE-L000323](../generate_index.py#L323) | 323 | `"def _is_sensitive_or_runtime_path(path: Path) -> bool:"` | — |
| [SRC-E599346ABE-L000324](../generate_index.py#L324) | 324 | `"    \"\"\"Exclude known local secrets, runtime databases, keys and generated bytecode.\"\"\""` | — |
| [SRC-E599346ABE-L000325](../generate_index.py#L325) | 325 | `"    name = path.name.lower()"` | — |
| [SRC-E599346ABE-L000326](../generate_index.py#L326) | 326 | `"    if name in SENSITIVE_FILENAMES:"` | — |
| [SRC-E599346ABE-L000327](../generate_index.py#L327) | 327 | `"        return True"` | — |
| [SRC-E599346ABE-L000328](../generate_index.py#L328) | 328 | `"    if name.startswith(\".env\") and name != \".env.example\":"` | — |
| [SRC-E599346ABE-L000329](../generate_index.py#L329) | 329 | `"        return True"` | — |
| [SRC-E599346ABE-L000330](../generate_index.py#L330) | 330 | `"    return path.suffix.lower() in EXCLUDED_SUFFIXES"` | — |
| [SRC-E599346ABE-L000331](../generate_index.py#L331) | 331 | `""` | — |
| [SRC-E599346ABE-L000332](../generate_index.py#L332) | 332 | `""` | — |
| [SRC-E599346ABE-L000333](../generate_index.py#L333) | 333 | `"def _stable_file_id(relative_file: str) -> str:"` | — |
| [SRC-E599346ABE-L000334](../generate_index.py#L334) | 334 | `"    \"\"\"Return a deterministic path-derived identifier without hashing file contents.\"\"\""` | — |
| [SRC-E599346ABE-L000335](../generate_index.py#L335) | 335 | `"    digest = hashlib.sha256(relative_file.encode(\"utf-8\")).hexdigest()[:10].upper()"` | — |
| [SRC-E599346ABE-L000336](../generate_index.py#L336) | 336 | `"    return f\"FILE-{digest}\""` | — |
| [SRC-E599346ABE-L000337](../generate_index.py#L337) | 337 | `""` | — |
| [SRC-E599346ABE-L000338](../generate_index.py#L338) | 338 | `""` | — |
| [SRC-E599346ABE-L000339](../generate_index.py#L339) | 339 | `"def _category_for_path(relative_file: str) -> str:"` | — |
| [SRC-E599346ABE-L000340](../generate_index.py#L340) | 340 | `"    \"\"\"Assign an understandable navigation category from the repository-relative path.\"\"\""` | — |
| [SRC-E599346ABE-L000341](../generate_index.py#L341) | 341 | `"    normalized = relative_file.replace(\"\\\\\", \"/\")"` | — |
| [SRC-E599346ABE-L000342](../generate_index.py#L342) | 342 | `"    name = Path(normalized).name.lower()"` | — |
| [SRC-E599346ABE-L000343](../generate_index.py#L343) | 343 | `"    suffix = Path(normalized).suffix.lower()"` | — |
| [SRC-E599346ABE-L000344](../generate_index.py#L344) | 344 | `"    if normalized.startswith(\"tests/\") or \"/tests/\" in normalized:"` | — |
| [SRC-E599346ABE-L000345](../generate_index.py#L345) | 345 | `"        return \"اختبارات\""` | — |
| [SRC-E599346ABE-L000346](../generate_index.py#L346) | 346 | `"    if normalized.startswith(\".github/workflows/\"):"` | — |
| [SRC-E599346ABE-L000347](../generate_index.py#L347) | 347 | `"        return \"CI وأتمتة\""` | — |
| [SRC-E599346ABE-L000348](../generate_index.py#L348) | 348 | `"    if normalized.startswith(\"agents/\"):"` | — |
| [SRC-E599346ABE-L000349](../generate_index.py#L349) | 349 | `"        return \"الوكيل والمنطق\""` | — |
| [SRC-E599346ABE-L000350](../generate_index.py#L350) | 350 | `"    if normalized.startswith(\"api/\"):"` | — |
| [SRC-E599346ABE-L000351](../generate_index.py#L351) | 351 | `"        return \"واجهات API\""` | — |
| [SRC-E599346ABE-L000352](../generate_index.py#L352) | 352 | `"    if normalized.startswith(\"cli/\"):"` | — |
| [SRC-E599346ABE-L000353](../generate_index.py#L353) | 353 | `"        return \"واجهة سطر الأوامر\""` | — |
| [SRC-E599346ABE-L000354](../generate_index.py#L354) | 354 | `"    if normalized.startswith(\"docs/\"):"` | — |
| [SRC-E599346ABE-L000355](../generate_index.py#L355) | 355 | `"        return \"وثائق وفهرسة\""` | — |
| [SRC-E599346ABE-L000356](../generate_index.py#L356) | 356 | `"    if normalized.startswith((\"web/\", \"static/\", \"templates/\")) or suffix in {"` | — |
| [SRC-E599346ABE-L000357](../generate_index.py#L357) | 357 | `"        \".html\", \".htm\", \".css\", \".scss\", \".js\", \".mjs\", \".cjs\", \".jsx\", \".ts\", \".tsx\","` | — |
| [SRC-E599346ABE-L000358](../generate_index.py#L358) | 358 | `"        \".vue\", \".svelte\","` | — |
| [SRC-E599346ABE-L000359](../generate_index.py#L359) | 359 | `"    }:"` | — |
| [SRC-E599346ABE-L000360](../generate_index.py#L360) | 360 | `"        return \"واجهة الويب\""` | — |
| [SRC-E599346ABE-L000361](../generate_index.py#L361) | 361 | `"    if name in {"` | — |
| [SRC-E599346ABE-L000362](../generate_index.py#L362) | 362 | `"        \"dockerfile\", \"makefile\", \"procfile\", \"pyproject.toml\","` | — |
| [SRC-E599346ABE-L000363](../generate_index.py#L363) | 363 | `"        \"requirements.txt\", \"requirements-dev.txt\", \".gitignore\","` | — |
| [SRC-E599346ABE-L000364](../generate_index.py#L364) | 364 | `"        \".dockerignore\", \".editorconfig\","` | — |
| [SRC-E599346ABE-L000365](../generate_index.py#L365) | 365 | `"    } or suffix in {\".yml\", \".yaml\", \".toml\", \".ini\", \".cfg\", \".json\", \".jsonl\", \".xml\"}:"` | — |
| [SRC-E599346ABE-L000366](../generate_index.py#L366) | 366 | `"        return \"إعدادات وتشغيل\""` | — |
| [SRC-E599346ABE-L000367](../generate_index.py#L367) | 367 | `"    if suffix in {\".md\", \".rst\", \".txt\"}:"` | — |
| [SRC-E599346ABE-L000368](../generate_index.py#L368) | 368 | `"        return \"وثائق ونصوص\""` | — |
| [SRC-E599346ABE-L000369](../generate_index.py#L369) | 369 | `"    return \"ملفات أخرى\""` | — |
| [SRC-E599346ABE-L000370](../generate_index.py#L370) | 370 | `""` | — |
| [SRC-E599346ABE-L000371](../generate_index.py#L371) | 371 | `""` | — |
| [SRC-E599346ABE-L000372](../generate_index.py#L372) | 372 | `"def discover_repository_files(root: Path) -> list[Path]:"` | — |
| [SRC-E599346ABE-L000373](../generate_index.py#L373) | 373 | `"    \"\"\"Return the stable file inventory, excluding the generated index and runtime data.\"\"\""` | — |
| [SRC-E599346ABE-L000374](../generate_index.py#L374) | 374 | `"    discovered: list[Path] = []"` | — |
| [SRC-E599346ABE-L000375](../generate_index.py#L375) | 375 | `"    for current_directory, directory_names, file_names in os.walk("` | — |
| [SRC-E599346ABE-L000376](../generate_index.py#L376) | 376 | `"        root,"` | — |
| [SRC-E599346ABE-L000377](../generate_index.py#L377) | 377 | `"        topdown=True,"` | — |
| [SRC-E599346ABE-L000378](../generate_index.py#L378) | 378 | `"        followlinks=False,"` | — |
| [SRC-E599346ABE-L000379](../generate_index.py#L379) | 379 | `"    ):"` | — |
| [SRC-E599346ABE-L000380](../generate_index.py#L380) | 380 | `"        directory_names[:] = sorted("` | — |
| [SRC-E599346ABE-L000381](../generate_index.py#L381) | 381 | `"            name"` | — |
| [SRC-E599346ABE-L000382](../generate_index.py#L382) | 382 | `"            for name in directory_names"` | — |
| [SRC-E599346ABE-L000383](../generate_index.py#L383) | 383 | `"            if name not in EXCLUDED_DIRECTORIES"` | — |
| [SRC-E599346ABE-L000384](../generate_index.py#L384) | 384 | `"            and not name.lower().endswith((\".egg-info\", \".dist-info\"))"` | — |
| [SRC-E599346ABE-L000385](../generate_index.py#L385) | 385 | `"            and not (Path(current_directory) / name).is_symlink()"` | — |
| [SRC-E599346ABE-L000386](../generate_index.py#L386) | 386 | `"        )"` | — |
| [SRC-E599346ABE-L000387](../generate_index.py#L387) | 387 | `"        for file_name in sorted(file_names):"` | — |
| [SRC-E599346ABE-L000388](../generate_index.py#L388) | 388 | `"            candidate = Path(current_directory) / file_name"` | — |
| [SRC-E599346ABE-L000389](../generate_index.py#L389) | 389 | `"            if candidate.is_symlink() or _is_sensitive_or_runtime_path(candidate):"` | — |
| [SRC-E599346ABE-L000390](../generate_index.py#L390) | 390 | `"                continue"` | — |
| [SRC-E599346ABE-L000391](../generate_index.py#L391) | 391 | `"            relative_file = candidate.relative_to(root).as_posix()"` | — |
| [SRC-E599346ABE-L000392](../generate_index.py#L392) | 392 | `"            if ("` | — |
| [SRC-E599346ABE-L000393](../generate_index.py#L393) | 393 | `"                relative_file in INDEX_OUTPUT_PATHS"` | — |
| [SRC-E599346ABE-L000394](../generate_index.py#L394) | 394 | `"                or relative_file.startswith(SOURCE_LINES_PAGES_DIR + \"/\")"` | — |
| [SRC-E599346ABE-L000395](../generate_index.py#L395) | 395 | `"            ):"` | — |
| [SRC-E599346ABE-L000396](../generate_index.py#L396) | 396 | `"                # Exclude generated index outputs to prevent self-indexing loops."` | — |
| [SRC-E599346ABE-L000397](../generate_index.py#L397) | 397 | `"                continue"` | — |
| [SRC-E599346ABE-L000398](../generate_index.py#L398) | 398 | `"            discovered.append(candidate)"` | — |
| [SRC-E599346ABE-L000399](../generate_index.py#L399) | 399 | `""` | — |
| [SRC-E599346ABE-L000400](../generate_index.py#L400) | 400 | `"    return sorted("` | — |
| [SRC-E599346ABE-L000401](../generate_index.py#L401) | 401 | `"        discovered,"` | — |
| [SRC-E599346ABE-L000402](../generate_index.py#L402) | 402 | `"        key=lambda path: path.relative_to(root).as_posix().casefold(),"` | — |
| [SRC-E599346ABE-L000403](../generate_index.py#L403) | 403 | `"    )"` | — |
| [SRC-E599346ABE-L000404](../generate_index.py#L404) | 404 | `""` | — |
| [SRC-E599346ABE-L000405](../generate_index.py#L405) | 405 | `""` | — |
| [SRC-E599346ABE-L000406](../generate_index.py#L406) | 406 | `"def _read_text_bounded(path: Path) -> str \| None:"` | — |
| [SRC-E599346ABE-L000407](../generate_index.py#L407) | 407 | `"    \"\"\"Read supported UTF-8 text files only when they are within the scan-size bound.\"\"\""` | — |
| [SRC-E599346ABE-L000408](../generate_index.py#L408) | 408 | `"    try:"` | — |
| [SRC-E599346ABE-L000409](../generate_index.py#L409) | 409 | `"        if path.stat().st_size > MAX_INDEXED_TEXT_BYTES:"` | — |
| [SRC-E599346ABE-L000410](../generate_index.py#L410) | 410 | `"            return None"` | — |
| [SRC-E599346ABE-L000411](../generate_index.py#L411) | 411 | `"        if path.suffix.lower() == \".py\":"` | — |
| [SRC-E599346ABE-L000412](../generate_index.py#L412) | 412 | `"            with tokenize.open(str(path)) as source_stream:"` | — |
| [SRC-E599346ABE-L000413](../generate_index.py#L413) | 413 | `"                text = source_stream.read()"` | — |
| [SRC-E599346ABE-L000414](../generate_index.py#L414) | 414 | `"        else:"` | — |
| [SRC-E599346ABE-L000415](../generate_index.py#L415) | 415 | `"            text = path.read_text(encoding=\"utf-8\")"` | — |
| [SRC-E599346ABE-L000416](../generate_index.py#L416) | 416 | `"        if \"\\x00\" in text:"` | — |
| [SRC-E599346ABE-L000417](../generate_index.py#L417) | 417 | `"            return None"` | — |
| [SRC-E599346ABE-L000418](../generate_index.py#L418) | 418 | `"        return text"` | — |
| [SRC-E599346ABE-L000419](../generate_index.py#L419) | 419 | `"    except (OSError, UnicodeError, LookupError, tokenize.TokenError):"` | — |
| [SRC-E599346ABE-L000420](../generate_index.py#L420) | 420 | `"        return None"` | — |
| [SRC-E599346ABE-L000421](../generate_index.py#L421) | 421 | `""` | — |
| [SRC-E599346ABE-L000422](../generate_index.py#L422) | 422 | `""` | — |
| [SRC-E599346ABE-L000423](../generate_index.py#L423) | 423 | `"def _count_lines(text: str) -> int:"` | — |
| [SRC-E599346ABE-L000424](../generate_index.py#L424) | 424 | `"    \"\"\"Count source lines without adding an extra line for a trailing newline.\"\"\""` | — |
| [SRC-E599346ABE-L000425](../generate_index.py#L425) | 425 | `"    if not text:"` | — |
| [SRC-E599346ABE-L000426](../generate_index.py#L426) | 426 | `"        return 0"` | — |
| [SRC-E599346ABE-L000427](../generate_index.py#L427) | 427 | `"    return text.count(\"\\n\") + (not text.endswith(\"\\n\"))"` | — |
| [SRC-E599346ABE-L000428](../generate_index.py#L428) | 428 | `""` | — |
| [SRC-E599346ABE-L000429](../generate_index.py#L429) | 429 | `""` | — |
| [SRC-E599346ABE-L000430](../generate_index.py#L430) | 430 | `"def _file_type(path: Path) -> str:"` | — |
| [SRC-E599346ABE-L000431](../generate_index.py#L431) | 431 | `"    \"\"\"Return a readable file type based on a known filename or extension.\"\"\""` | — |
| [SRC-E599346ABE-L000432](../generate_index.py#L432) | 432 | `"    name = path.name.lower()"` | — |
| [SRC-E599346ABE-L000433](../generate_index.py#L433) | 433 | `"    if name in {\"dockerfile\", \"makefile\", \"procfile\"}:"` | — |
| [SRC-E599346ABE-L000434](../generate_index.py#L434) | 434 | `"        return name.capitalize()"` | — |
| [SRC-E599346ABE-L000435](../generate_index.py#L435) | 435 | `"    suffix = path.suffix.lower()"` | — |
| [SRC-E599346ABE-L000436](../generate_index.py#L436) | 436 | `"    labels = {"` | — |
| [SRC-E599346ABE-L000437](../generate_index.py#L437) | 437 | `"        \".py\": \"Python\","` | — |
| [SRC-E599346ABE-L000438](../generate_index.py#L438) | 438 | `"        \".html\": \"HTML\","` | — |
| [SRC-E599346ABE-L000439](../generate_index.py#L439) | 439 | `"        \".htm\": \"HTML\","` | — |
| [SRC-E599346ABE-L000440](../generate_index.py#L440) | 440 | `"        \".js\": \"JavaScript\","` | — |
| [SRC-E599346ABE-L000441](../generate_index.py#L441) | 441 | `"        \".mjs\": \"JavaScript module\","` | — |
| [SRC-E599346ABE-L000442](../generate_index.py#L442) | 442 | `"        \".cjs\": \"CommonJS\","` | — |
| [SRC-E599346ABE-L000443](../generate_index.py#L443) | 443 | `"        \".jsx\": \"React JSX\","` | — |
| [SRC-E599346ABE-L000444](../generate_index.py#L444) | 444 | `"        \".ts\": \"TypeScript\","` | — |
| [SRC-E599346ABE-L000445](../generate_index.py#L445) | 445 | `"        \".tsx\": \"TypeScript JSX\","` | — |
| [SRC-E599346ABE-L000446](../generate_index.py#L446) | 446 | `"        \".css\": \"CSS\","` | — |
| [SRC-E599346ABE-L000447](../generate_index.py#L447) | 447 | `"        \".scss\": \"SCSS\","` | — |
| [SRC-E599346ABE-L000448](../generate_index.py#L448) | 448 | `"        \".md\": \"Markdown\","` | — |
| [SRC-E599346ABE-L000449](../generate_index.py#L449) | 449 | `"        \".yml\": \"YAML\","` | — |
| [SRC-E599346ABE-L000450](../generate_index.py#L450) | 450 | `"        \".yaml\": \"YAML\","` | — |
| [SRC-E599346ABE-L000451](../generate_index.py#L451) | 451 | `"        \".json\": \"JSON\","` | — |
| [SRC-E599346ABE-L000452](../generate_index.py#L452) | 452 | `"        \".toml\": \"TOML\","` | — |
| [SRC-E599346ABE-L000453](../generate_index.py#L453) | 453 | `"        \".sh\": \"Shell\","` | — |
| [SRC-E599346ABE-L000454](../generate_index.py#L454) | 454 | `"        \".sql\": \"SQL\","` | — |
| [SRC-E599346ABE-L000455](../generate_index.py#L455) | 455 | `"        \".txt\": \"Text\","` | — |
| [SRC-E599346ABE-L000456](../generate_index.py#L456) | 456 | `"        \".svg\": \"SVG\","` | — |
| [SRC-E599346ABE-L000457](../generate_index.py#L457) | 457 | `"        \".png\": \"PNG image\","` | — |
| [SRC-E599346ABE-L000458](../generate_index.py#L458) | 458 | `"        \".jpg\": \"JPEG image\","` | — |
| [SRC-E599346ABE-L000459](../generate_index.py#L459) | 459 | `"        \".jpeg\": \"JPEG image\","` | — |
| [SRC-E599346ABE-L000460](../generate_index.py#L460) | 460 | `"        \".webp\": \"WebP image\","` | — |
| [SRC-E599346ABE-L000461](../generate_index.py#L461) | 461 | `"    }"` | — |
| [SRC-E599346ABE-L000462](../generate_index.py#L462) | 462 | `"    return labels.get(suffix, suffix[1:].upper() if suffix else \"بدون امتداد\")"` | — |
| [SRC-E599346ABE-L000463](../generate_index.py#L463) | 463 | `""` | — |
| [SRC-E599346ABE-L000464](../generate_index.py#L464) | 464 | `""` | — |
| [SRC-E599346ABE-L000465](../generate_index.py#L465) | 465 | `"def _indexing_scope(path: Path, text: str \| None) -> str:"` | — |
| [SRC-E599346ABE-L000466](../generate_index.py#L466) | 466 | `"    \"\"\"Describe precisely whether a file receives symbol extraction or path inventory only.\"\"\""` | — |
| [SRC-E599346ABE-L000467](../generate_index.py#L467) | 467 | `"    if text is None:"` | — |
| [SRC-E599346ABE-L000468](../generate_index.py#L468) | 468 | `"        return \"جرد المسار والحجم فقط (ثنائي/غير مقروء/أكبر من حد الفحص)\""` | — |
| [SRC-E599346ABE-L000469](../generate_index.py#L469) | 469 | `"    suffix = path.suffix.lower()"` | — |
| [SRC-E599346ABE-L000470](../generate_index.py#L470) | 470 | `"    if suffix in PYTHON_EXTENSIONS:"` | — |
| [SRC-E599346ABE-L000471](../generate_index.py#L471) | 471 | `"        return \"جرد الملف + AST Python\""` | — |
| [SRC-E599346ABE-L000472](../generate_index.py#L472) | 472 | `"    if suffix in JAVASCRIPT_EXTENSIONS:"` | — |
| [SRC-E599346ABE-L000473](../generate_index.py#L473) | 473 | `"        return \"جرد الملف + رموز JavaScript/TypeScript ساكنة\""` | — |
| [SRC-E599346ABE-L000474](../generate_index.py#L474) | 474 | `"    if suffix in CSS_EXTENSIONS:"` | — |
| [SRC-E599346ABE-L000475](../generate_index.py#L475) | 475 | `"        return \"جرد الملف + محددات CSS والمتغيرات المخصصة\""` | — |
| [SRC-E599346ABE-L000476](../generate_index.py#L476) | 476 | `"    if suffix in {\".html\", \".htm\"}:"` | — |
| [SRC-E599346ABE-L000477](../generate_index.py#L477) | 477 | `"        return \"جرد الملف + معرفات HTML والرموز داخل script/style\""` | — |
| [SRC-E599346ABE-L000478](../generate_index.py#L478) | 478 | `"    if suffix == \".md\":"` | — |
| [SRC-E599346ABE-L000479](../generate_index.py#L479) | 479 | `"        return \"جرد الملف + عناوين Markdown\""` | — |
| [SRC-E599346ABE-L000480](../generate_index.py#L480) | 480 | `"    if suffix in CONFIG_EXTENSIONS:"` | — |
| [SRC-E599346ABE-L000481](../generate_index.py#L481) | 481 | `"        return \"جرد الملف + مفاتيح إعداد ساكنة\""` | — |
| [SRC-E599346ABE-L000482](../generate_index.py#L482) | 482 | `"    if suffix == \".sh\":"` | — |
| [SRC-E599346ABE-L000483](../generate_index.py#L483) | 483 | `"        return \"جرد الملف + دوال Shell\""` | — |
| [SRC-E599346ABE-L000484](../generate_index.py#L484) | 484 | `"    if path.name.lower() in {\"dockerfile\", \"makefile\", \"procfile\"}:"` | — |
| [SRC-E599346ABE-L000485](../generate_index.py#L485) | 485 | `"        return \"جرد الملف + أسماء إعدادات عامة إن وجدت\""` | — |
| [SRC-E599346ABE-L000486](../generate_index.py#L486) | 486 | `"    if path.name.lower() == \".env.example\" or suffix == \".example\":"` | — |
| [SRC-E599346ABE-L000487](../generate_index.py#L487) | 487 | `"        return \"جرد الملف + أسماء إعدادات عامة إن وجدت\""` | — |
| [SRC-E599346ABE-L000488](../generate_index.py#L488) | 488 | `"    return \"جرد ملف نصي فقط\""` | — |
| [SRC-E599346ABE-L000489](../generate_index.py#L489) | 489 | `""` | — |
| [SRC-E599346ABE-L000490](../generate_index.py#L490) | 490 | `""` | — |
| [SRC-E599346ABE-L000491](../generate_index.py#L491) | 491 | `"def build_file_inventory(root: Path) -> list[IndexedFile]:"` | — |
| [SRC-E599346ABE-L000492](../generate_index.py#L492) | 492 | `"    \"\"\"Inventory repository files and record whether static symbol scanning was possible.\"\"\""` | — |
| [SRC-E599346ABE-L000493](../generate_index.py#L493) | 493 | `"    inventory: list[IndexedFile] = []"` | — |
| [SRC-E599346ABE-L000494](../generate_index.py#L494) | 494 | `"    for path in discover_repository_files(root):"` | — |
| [SRC-E599346ABE-L000495](../generate_index.py#L495) | 495 | `"        text = _read_text_bounded(path)"` | — |
| [SRC-E599346ABE-L000496](../generate_index.py#L496) | 496 | `"        inventory.append("` | — |
| [SRC-E599346ABE-L000497](../generate_index.py#L497) | 497 | `"            IndexedFile("` | — |
| [SRC-E599346ABE-L000498](../generate_index.py#L498) | 498 | `"                file=path.relative_to(root).as_posix(),"` | — |
| [SRC-E599346ABE-L000499](../generate_index.py#L499) | 499 | `"                file_type=_file_type(path),"` | — |
| [SRC-E599346ABE-L000500](../generate_index.py#L500) | 500 | `"                size_bytes=path.stat().st_size,"` | — |
| [SRC-E599346ABE-L000501](../generate_index.py#L501) | 501 | `"                line_count=_count_lines(text) if text is not None else None,"` | — |
| [SRC-E599346ABE-L000502](../generate_index.py#L502) | 502 | `"                indexing_scope=_indexing_scope(path, text),"` | — |
| [SRC-E599346ABE-L000503](../generate_index.py#L503) | 503 | `"                file_id=_stable_file_id(path.relative_to(root).as_posix()),"` | — |
| [SRC-E599346ABE-L000504](../generate_index.py#L504) | 504 | `"                category=_category_for_path(path.relative_to(root).as_posix()),"` | — |
| [SRC-E599346ABE-L000505](../generate_index.py#L505) | 505 | `"            )"` | — |
| [SRC-E599346ABE-L000506](../generate_index.py#L506) | 506 | `"        )"` | — |
| [SRC-E599346ABE-L000507](../generate_index.py#L507) | 507 | `"    return inventory"` | — |
| [SRC-E599346ABE-L000508](../generate_index.py#L508) | 508 | `""` | — |
| [SRC-E599346ABE-L000509](../generate_index.py#L509) | 509 | `""` | — |
| [SRC-E599346ABE-L000510](../generate_index.py#L510) | 510 | `"def _tracked_paths_or_none(root: Path) -> set[str] \| None:"` | — |
| [SRC-E599346ABE-L000511](../generate_index.py#L511) | 511 | `"    \"\"\"Return tracked repository paths, or None when the root is not a Git checkout.\"\"\""` | — |
| [SRC-E599346ABE-L000512](../generate_index.py#L512) | 512 | `"    try:"` | — |
| [SRC-E599346ABE-L000513](../generate_index.py#L513) | 513 | `"        result = subprocess.run("` | — |
| [SRC-E599346ABE-L000514](../generate_index.py#L514) | 514 | `"            [\"git\", \"-C\", str(root), \"ls-files\", \"-z\"],"` | — |
| [SRC-E599346ABE-L000515](../generate_index.py#L515) | 515 | `"            check=True,"` | — |
| [SRC-E599346ABE-L000516](../generate_index.py#L516) | 516 | `"            capture_output=True,"` | — |
| [SRC-E599346ABE-L000517](../generate_index.py#L517) | 517 | `"        )"` | — |
| [SRC-E599346ABE-L000518](../generate_index.py#L518) | 518 | `"    except (OSError, subprocess.SubprocessError):"` | — |
| [SRC-E599346ABE-L000519](../generate_index.py#L519) | 519 | `"        return None"` | — |
| [SRC-E599346ABE-L000520](../generate_index.py#L520) | 520 | `"    try:"` | — |
| [SRC-E599346ABE-L000521](../generate_index.py#L521) | 521 | `"        return {"` | — |
| [SRC-E599346ABE-L000522](../generate_index.py#L522) | 522 | `"            path"` | — |
| [SRC-E599346ABE-L000523](../generate_index.py#L523) | 523 | `"            for path in result.stdout.decode(\"utf-8\").split(\"\\x00\")"` | — |
| [SRC-E599346ABE-L000524](../generate_index.py#L524) | 524 | `"            if path"` | — |
| [SRC-E599346ABE-L000525](../generate_index.py#L525) | 525 | `"        }"` | — |
| [SRC-E599346ABE-L000526](../generate_index.py#L526) | 526 | `"    except UnicodeError:"` | — |
| [SRC-E599346ABE-L000527](../generate_index.py#L527) | 527 | `"        return None"` | — |
| [SRC-E599346ABE-L000528](../generate_index.py#L528) | 528 | `""` | — |
| [SRC-E599346ABE-L000529](../generate_index.py#L529) | 529 | `""` | — |
| [SRC-E599346ABE-L000530](../generate_index.py#L530) | 530 | `"def discover_excluded_paths(root: Path) -> list[tuple[str, str]]:"` | — |
| [SRC-E599346ABE-L000531](../generate_index.py#L531) | 531 | `"    \"\"\"List excluded tracked path names and reasons without opening excluded contents.\"\"\""` | — |
| [SRC-E599346ABE-L000532](../generate_index.py#L532) | 532 | `"    tracked_paths = _tracked_paths_or_none(root)"` | — |
| [SRC-E599346ABE-L000533](../generate_index.py#L533) | 533 | `""` | — |
| [SRC-E599346ABE-L000534](../generate_index.py#L534) | 534 | `"    def tracked_scope_contains(relative_path: str, is_directory: bool = False) -> bool:"` | — |
| [SRC-E599346ABE-L000535](../generate_index.py#L535) | 535 | `"        if tracked_paths is None:"` | — |
| [SRC-E599346ABE-L000536](../generate_index.py#L536) | 536 | `"            return True"` | — |
| [SRC-E599346ABE-L000537](../generate_index.py#L537) | 537 | `"        normalized = relative_path.rstrip(\"/\")"` | — |
| [SRC-E599346ABE-L000538](../generate_index.py#L538) | 538 | `"        if is_directory:"` | — |
| [SRC-E599346ABE-L000539](../generate_index.py#L539) | 539 | `"            prefix = normalized + \"/\""` | — |
| [SRC-E599346ABE-L000540](../generate_index.py#L540) | 540 | `"            return any(path.startswith(prefix) for path in tracked_paths)"` | — |
| [SRC-E599346ABE-L000541](../generate_index.py#L541) | 541 | `"        return normalized in tracked_paths"` | — |
| [SRC-E599346ABE-L000542](../generate_index.py#L542) | 542 | `""` | — |
| [SRC-E599346ABE-L000543](../generate_index.py#L543) | 543 | `"    excluded: list[tuple[str, str]] = ["` | — |
| [SRC-E599346ABE-L000544](../generate_index.py#L544) | 544 | `"        (path, \"مخرج فهرسة مولد مستبعد لمنع الحلقة الذاتية\")"` | — |
| [SRC-E599346ABE-L000545](../generate_index.py#L545) | 545 | `"        for path in sorted(INDEX_OUTPUT_PATHS)"` | — |
| [SRC-E599346ABE-L000546](../generate_index.py#L546) | 546 | `"    ]"` | — |
| [SRC-E599346ABE-L000547](../generate_index.py#L547) | 547 | `"    excluded.append("` | — |
| [SRC-E599346ABE-L000548](../generate_index.py#L548) | 548 | `"        ("` | — |
| [SRC-E599346ABE-L000549](../generate_index.py#L549) | 549 | `"            SOURCE_LINES_PAGES_DIR + \"/\","` | — |
| [SRC-E599346ABE-L000550](../generate_index.py#L550) | 550 | `"            \"مجلد صفحات فهرسة مولدة مستبعد لمنع الحلقة الذاتية\","` | — |
| [SRC-E599346ABE-L000551](../generate_index.py#L551) | 551 | `"        )"` | — |
| [SRC-E599346ABE-L000552](../generate_index.py#L552) | 552 | `"    )"` | — |
| [SRC-E599346ABE-L000553](../generate_index.py#L553) | 553 | `"    for current_directory, directory_names, file_names in os.walk("` | — |
| [SRC-E599346ABE-L000554](../generate_index.py#L554) | 554 | `"        root,"` | — |
| [SRC-E599346ABE-L000555](../generate_index.py#L555) | 555 | `"        topdown=True,"` | — |
| [SRC-E599346ABE-L000556](../generate_index.py#L556) | 556 | `"        followlinks=False,"` | — |
| [SRC-E599346ABE-L000557](../generate_index.py#L557) | 557 | `"    ):"` | — |
| [SRC-E599346ABE-L000558](../generate_index.py#L558) | 558 | `"        kept_directories: list[str] = []"` | — |
| [SRC-E599346ABE-L000559](../generate_index.py#L559) | 559 | `"        for name in sorted(directory_names):"` | — |
| [SRC-E599346ABE-L000560](../generate_index.py#L560) | 560 | `"            candidate = Path(current_directory) / name"` | — |
| [SRC-E599346ABE-L000561](../generate_index.py#L561) | 561 | `"            relative = candidate.relative_to(root).as_posix()"` | — |
| [SRC-E599346ABE-L000562](../generate_index.py#L562) | 562 | `"            if candidate.is_symlink():"` | — |
| [SRC-E599346ABE-L000563](../generate_index.py#L563) | 563 | `"                if tracked_scope_contains(relative, is_directory=True):"` | — |
| [SRC-E599346ABE-L000564](../generate_index.py#L564) | 564 | `"                    excluded.append((relative + \"/\", \"رابط رمزي مستبعد لسلامة التتبع\"))"` | — |
| [SRC-E599346ABE-L000565](../generate_index.py#L565) | 565 | `"            elif name in EXCLUDED_DIRECTORIES:"` | — |
| [SRC-E599346ABE-L000566](../generate_index.py#L566) | 566 | `"                if tracked_scope_contains(relative, is_directory=True):"` | — |
| [SRC-E599346ABE-L000567](../generate_index.py#L567) | 567 | `"                    excluded.append((relative + \"/\", \"مجلد بيئة أو اعتماديات أو مخرجات مولدة مستبعد\"))"` | — |
| [SRC-E599346ABE-L000568](../generate_index.py#L568) | 568 | `"            elif name.lower().endswith((\".egg-info\", \".dist-info\")):"` | — |
| [SRC-E599346ABE-L000569](../generate_index.py#L569) | 569 | `"                if tracked_scope_contains(relative, is_directory=True):"` | — |
| [SRC-E599346ABE-L000570](../generate_index.py#L570) | 570 | `"                    excluded.append((relative + \"/\", \"بيانات تغليف مولدة مستبعدة\"))"` | — |
| [SRC-E599346ABE-L000571](../generate_index.py#L571) | 571 | `"            elif relative == SOURCE_LINES_PAGES_DIR:"` | — |
| [SRC-E599346ABE-L000572](../generate_index.py#L572) | 572 | `"                excluded.append("` | — |
| [SRC-E599346ABE-L000573](../generate_index.py#L573) | 573 | `"                    ("` | — |
| [SRC-E599346ABE-L000574](../generate_index.py#L574) | 574 | `"                        relative + \"/\","` | — |
| [SRC-E599346ABE-L000575](../generate_index.py#L575) | 575 | `"                        \"مجلد صفحات فهرسة مولدة مستبعد لمنع الحلقة الذاتية\","` | — |
| [SRC-E599346ABE-L000576](../generate_index.py#L576) | 576 | `"                    )"` | — |
| [SRC-E599346ABE-L000577](../generate_index.py#L577) | 577 | `"                )"` | — |
| [SRC-E599346ABE-L000578](../generate_index.py#L578) | 578 | `"            else:"` | — |
| [SRC-E599346ABE-L000579](../generate_index.py#L579) | 579 | `"                kept_directories.append(name)"` | — |
| [SRC-E599346ABE-L000580](../generate_index.py#L580) | 580 | `"        directory_names[:] = kept_directories"` | — |
| [SRC-E599346ABE-L000581](../generate_index.py#L581) | 581 | `""` | — |
| [SRC-E599346ABE-L000582](../generate_index.py#L582) | 582 | `"        for name in sorted(file_names):"` | — |
| [SRC-E599346ABE-L000583](../generate_index.py#L583) | 583 | `"            candidate = Path(current_directory) / name"` | — |
| [SRC-E599346ABE-L000584](../generate_index.py#L584) | 584 | `"            relative = candidate.relative_to(root).as_posix()"` | — |
| [SRC-E599346ABE-L000585](../generate_index.py#L585) | 585 | `"            if candidate.is_symlink():"` | — |
| [SRC-E599346ABE-L000586](../generate_index.py#L586) | 586 | `"                if tracked_scope_contains(relative):"` | — |
| [SRC-E599346ABE-L000587](../generate_index.py#L587) | 587 | `"                    excluded.append((relative, \"رابط رمزي مستبعد لسلامة التتبع\"))"` | — |
| [SRC-E599346ABE-L000588](../generate_index.py#L588) | 588 | `"            elif _is_sensitive_or_runtime_path(candidate):"` | — |
| [SRC-E599346ABE-L000589](../generate_index.py#L589) | 589 | `"                if tracked_scope_contains(relative):"` | — |
| [SRC-E599346ABE-L000590](../generate_index.py#L590) | 590 | `"                    if name.lower().startswith(\".env\") and name.lower() != \".env.example\":"` | — |
| [SRC-E599346ABE-L000591](../generate_index.py#L591) | 591 | `"                        reason = \"ملف بيئة محلي مستبعد وقائيًا؛ لم تُقرأ محتوياته\""` | — |
| [SRC-E599346ABE-L000592](../generate_index.py#L592) | 592 | `"                    elif candidate.suffix.lower() in EXCLUDED_SUFFIXES:"` | — |
| [SRC-E599346ABE-L000593](../generate_index.py#L593) | 593 | `"                        reason = \"قاعدة بيانات أو ملف مفتاح/شهادة مستبعد\""` | — |
| [SRC-E599346ABE-L000594](../generate_index.py#L594) | 594 | `"                    else:"` | — |
| [SRC-E599346ABE-L000595](../generate_index.py#L595) | 595 | `"                        reason = \"اسم ملف حساس معروف؛ لم تُقرأ محتوياته\""` | — |
| [SRC-E599346ABE-L000596](../generate_index.py#L596) | 596 | `"                    excluded.append((relative, reason))"` | — |
| [SRC-E599346ABE-L000597](../generate_index.py#L597) | 597 | `"            elif relative in INDEX_OUTPUT_PATHS:"` | — |
| [SRC-E599346ABE-L000598](../generate_index.py#L598) | 598 | `"                excluded.append((relative, \"مخرج فهرسة مولد مستبعد لمنع الحلقة الذاتية\"))"` | — |
| [SRC-E599346ABE-L000599](../generate_index.py#L599) | 599 | `"            elif ("` | — |
| [SRC-E599346ABE-L000600](../generate_index.py#L600) | 600 | `"                relative.startswith(SOURCE_LINES_PAGES_DIR + \"/\")"` | — |
| [SRC-E599346ABE-L000601](../generate_index.py#L601) | 601 | `"                and tracked_scope_contains(relative)"` | — |
| [SRC-E599346ABE-L000602](../generate_index.py#L602) | 602 | `"            ):"` | — |
| [SRC-E599346ABE-L000603](../generate_index.py#L603) | 603 | `"                excluded.append((relative, \"صفحة فهرسة مولدة مستبعدة لمنع الحلقة الذاتية\"))"` | — |
| [SRC-E599346ABE-L000604](../generate_index.py#L604) | 604 | `""` | — |
| [SRC-E599346ABE-L000605](../generate_index.py#L605) | 605 | `"    return sorted(set(excluded), key=lambda item: (item[0].casefold(), item[1]))"` | — |
| [SRC-E599346ABE-L000606](../generate_index.py#L606) | 606 | `""` | — |
| [SRC-E599346ABE-L000607](../generate_index.py#L607) | 607 | `""` | — |
| [SRC-E599346ABE-L000608](../generate_index.py#L608) | 608 | `"def _text_index_skip_reason(path: Path) -> str:"` | — |
| [SRC-E599346ABE-L000609](../generate_index.py#L609) | 609 | `"    \"\"\"Return a concrete safe reason when a file could not be line-indexed.\"\"\""` | — |
| [SRC-E599346ABE-L000610](../generate_index.py#L610) | 610 | `"    try:"` | — |
| [SRC-E599346ABE-L000611](../generate_index.py#L611) | 611 | `"        if path.stat().st_size > MAX_INDEXED_TEXT_BYTES:"` | — |
| [SRC-E599346ABE-L000612](../generate_index.py#L612) | 612 | `"            return f\"الحجم يتجاوز حد الفهرسة ({MAX_INDEXED_TEXT_BYTES} بايت)\""` | — |
| [SRC-E599346ABE-L000613](../generate_index.py#L613) | 613 | `"        if path.suffix.lower() == \".py\":"` | — |
| [SRC-E599346ABE-L000614](../generate_index.py#L614) | 614 | `"            with tokenize.open(str(path)) as source_stream:"` | — |
| [SRC-E599346ABE-L000615](../generate_index.py#L615) | 615 | `"                source = source_stream.read()"` | — |
| [SRC-E599346ABE-L000616](../generate_index.py#L616) | 616 | `"        else:"` | — |
| [SRC-E599346ABE-L000617](../generate_index.py#L617) | 617 | `"            source = path.read_text(encoding=\"utf-8\")"` | — |
| [SRC-E599346ABE-L000618](../generate_index.py#L618) | 618 | `"        if \"\\x00\" in source:"` | — |
| [SRC-E599346ABE-L000619](../generate_index.py#L619) | 619 | `"            return \"يحتوي محرف NUL؛ عومل كملف غير نصي\""` | — |
| [SRC-E599346ABE-L000620](../generate_index.py#L620) | 620 | `"    except (OSError, UnicodeError, LookupError, tokenize.TokenError):"` | — |
| [SRC-E599346ABE-L000621](../generate_index.py#L621) | 621 | `"        return \"تعذرت قراءته كنص صالح بترميز مدعوم\""` | — |
| [SRC-E599346ABE-L000622](../generate_index.py#L622) | 622 | `"    return \"سبب غير مصنف؛ يحتاج مراجعة أداة الفهرسة\""` | — |
| [SRC-E599346ABE-L000623](../generate_index.py#L623) | 623 | `""` | — |
| [SRC-E599346ABE-L000624](../generate_index.py#L624) | 624 | `""` | — |
| [SRC-E599346ABE-L000625](../generate_index.py#L625) | 625 | `"def validate_source_line_coverage("` | — |
| [SRC-E599346ABE-L000626](../generate_index.py#L626) | 626 | `"    root: Path,"` | — |
| [SRC-E599346ABE-L000627](../generate_index.py#L627) | 627 | `"    inventory: list[IndexedFile],"` | — |
| [SRC-E599346ABE-L000628](../generate_index.py#L628) | 628 | `"    source_lines: list[IndexedLine],"` | — |
| [SRC-E599346ABE-L000629](../generate_index.py#L629) | 629 | `") -> None:"` | — |
| [SRC-E599346ABE-L000630](../generate_index.py#L630) | 630 | `"    \"\"\"Fail generation if line coverage, IDs, or exact source text do not match.\"\"\""` | — |
| [SRC-E599346ABE-L000631](../generate_index.py#L631) | 631 | `"    eligible_files = {"` | — |
| [SRC-E599346ABE-L000632](../generate_index.py#L632) | 632 | `"        item.file: item"` | — |
| [SRC-E599346ABE-L000633](../generate_index.py#L633) | 633 | `"        for item in inventory"` | — |
| [SRC-E599346ABE-L000634](../generate_index.py#L634) | 634 | `"        if item.line_count is not None"` | — |
| [SRC-E599346ABE-L000635](../generate_index.py#L635) | 635 | `"    }"` | — |
| [SRC-E599346ABE-L000636](../generate_index.py#L636) | 636 | `"    expected_lines_by_file: dict[str, list[str]] = {}"` | — |
| [SRC-E599346ABE-L000637](../generate_index.py#L637) | 637 | `"    failures: list[str] = []"` | — |
| [SRC-E599346ABE-L000638](../generate_index.py#L638) | 638 | `"    seen_ids: set[str] = set()"` | — |
| [SRC-E599346ABE-L000639](../generate_index.py#L639) | 639 | `"    actual_lines: dict[str, list[int]] = {file: [] for file in eligible_files}"` | — |
| [SRC-E599346ABE-L000640](../generate_index.py#L640) | 640 | `""` | — |
| [SRC-E599346ABE-L000641](../generate_index.py#L641) | 641 | `"    # Re-read every eligible source independently to detect races or corrupted line records."` | — |
| [SRC-E599346ABE-L000642](../generate_index.py#L642) | 642 | `"    for file, item in eligible_files.items():"` | — |
| [SRC-E599346ABE-L000643](../generate_index.py#L643) | 643 | `"        source = _read_text_bounded(root / file)"` | — |
| [SRC-E599346ABE-L000644](../generate_index.py#L644) | 644 | `"        if source is None:"` | — |
| [SRC-E599346ABE-L000645](../generate_index.py#L645) | 645 | `"            failures.append(f\"{file}: تعذرت إعادة قراءة ملف مؤهل للتحقق\")"` | — |
| [SRC-E599346ABE-L000646](../generate_index.py#L646) | 646 | `"            expected_lines_by_file[file] = []"` | — |
| [SRC-E599346ABE-L000647](../generate_index.py#L647) | 647 | `"            continue"` | — |
| [SRC-E599346ABE-L000648](../generate_index.py#L648) | 648 | `"        expected_contents = source.splitlines()"` | — |
| [SRC-E599346ABE-L000649](../generate_index.py#L649) | 649 | `"        expected_lines_by_file[file] = expected_contents"` | — |
| [SRC-E599346ABE-L000650](../generate_index.py#L650) | 650 | `"        if len(expected_contents) != item.line_count:"` | — |
| [SRC-E599346ABE-L000651](../generate_index.py#L651) | 651 | `"            failures.append("` | — |
| [SRC-E599346ABE-L000652](../generate_index.py#L652) | 652 | `"                f\"{file}: تغير عدد الأسطر بعد إعداد الجرد \""` | — |
| [SRC-E599346ABE-L000653](../generate_index.py#L653) | 653 | `"                f\"(الجرد {item.line_count}، الحالي {len(expected_contents)})\""` | — |
| [SRC-E599346ABE-L000654](../generate_index.py#L654) | 654 | `"            )"` | — |
| [SRC-E599346ABE-L000655](../generate_index.py#L655) | 655 | `""` | — |
| [SRC-E599346ABE-L000656](../generate_index.py#L656) | 656 | `"    actual_records_by_file: dict[str, dict[int, IndexedLine]] = {"` | — |
| [SRC-E599346ABE-L000657](../generate_index.py#L657) | 657 | `"        file: {} for file in eligible_files"` | — |
| [SRC-E599346ABE-L000658](../generate_index.py#L658) | 658 | `"    }"` | — |
| [SRC-E599346ABE-L000659](../generate_index.py#L659) | 659 | `"    for source_line in source_lines:"` | — |
| [SRC-E599346ABE-L000660](../generate_index.py#L660) | 660 | `"        if source_line.file not in eligible_files:"` | — |
| [SRC-E599346ABE-L000661](../generate_index.py#L661) | 661 | `"            failures.append(f\"{source_line.file}: سجل سطر لملف غير مؤهل\")"` | — |
| [SRC-E599346ABE-L000662](../generate_index.py#L662) | 662 | `"            continue"` | — |
| [SRC-E599346ABE-L000663](../generate_index.py#L663) | 663 | `""` | — |
| [SRC-E599346ABE-L000664](../generate_index.py#L664) | 664 | `"        actual_lines[source_line.file].append(source_line.line)"` | — |
| [SRC-E599346ABE-L000665](../generate_index.py#L665) | 665 | `"        actual_records_by_file[source_line.file][source_line.line] = source_line"` | — |
| [SRC-E599346ABE-L000666](../generate_index.py#L666) | 666 | `"        expected_item = eligible_files[source_line.file]"` | — |
| [SRC-E599346ABE-L000667](../generate_index.py#L667) | 667 | `""` | — |
| [SRC-E599346ABE-L000668](../generate_index.py#L668) | 668 | `"        if source_line.line < 1:"` | — |
| [SRC-E599346ABE-L000669](../generate_index.py#L669) | 669 | `"            failures.append(f\"{source_line.file}: رقم سطر غير صالح {source_line.line}\")"` | — |
| [SRC-E599346ABE-L000670](../generate_index.py#L670) | 670 | `"            continue"` | — |
| [SRC-E599346ABE-L000671](../generate_index.py#L671) | 671 | `""` | — |
| [SRC-E599346ABE-L000672](../generate_index.py#L672) | 672 | `"        expected_contents = expected_lines_by_file.get(source_line.file, [])"` | — |
| [SRC-E599346ABE-L000673](../generate_index.py#L673) | 673 | `"        if ("` | — |
| [SRC-E599346ABE-L000674](../generate_index.py#L674) | 674 | `"            source_line.line <= len(expected_contents)"` | — |
| [SRC-E599346ABE-L000675](../generate_index.py#L675) | 675 | `"            and source_line.content != expected_contents[source_line.line - 1]"` | — |
| [SRC-E599346ABE-L000676](../generate_index.py#L676) | 676 | `"        ):"` | — |
| [SRC-E599346ABE-L000677](../generate_index.py#L677) | 677 | `"            failures.append("` | — |
| [SRC-E599346ABE-L000678](../generate_index.py#L678) | 678 | `"                f\"{source_line.file}:{source_line.line}: نص السطر لا يطابق المصدر\""` | — |
| [SRC-E599346ABE-L000679](../generate_index.py#L679) | 679 | `"            )"` | — |
| [SRC-E599346ABE-L000680](../generate_index.py#L680) | 680 | `""` | — |
| [SRC-E599346ABE-L000681](../generate_index.py#L681) | 681 | `"        expected_line_id = _source_line_id(source_line.file, source_line.line)"` | — |
| [SRC-E599346ABE-L000682](../generate_index.py#L682) | 682 | `"        if source_line.line_id != expected_line_id:"` | — |
| [SRC-E599346ABE-L000683](../generate_index.py#L683) | 683 | `"            failures.append("` | — |
| [SRC-E599346ABE-L000684](../generate_index.py#L684) | 684 | `"                f\"{source_line.file}:{source_line.line}: كود SRC لا يطابق المسار ورقم السطر\""` | — |
| [SRC-E599346ABE-L000685](../generate_index.py#L685) | 685 | `"            )"` | — |
| [SRC-E599346ABE-L000686](../generate_index.py#L686) | 686 | `"        if source_line.file_id != _stable_file_id(source_line.file):"` | — |
| [SRC-E599346ABE-L000687](../generate_index.py#L687) | 687 | `"            failures.append("` | — |
| [SRC-E599346ABE-L000688](../generate_index.py#L688) | 688 | `"                f\"{source_line.file}:{source_line.line}: كود FILE لا يطابق مسار الملف\""` | — |
| [SRC-E599346ABE-L000689](../generate_index.py#L689) | 689 | `"            )"` | — |
| [SRC-E599346ABE-L000690](../generate_index.py#L690) | 690 | `"        if source_line.file_id != expected_item.file_id:"` | — |
| [SRC-E599346ABE-L000691](../generate_index.py#L691) | 691 | `"            failures.append("` | — |
| [SRC-E599346ABE-L000692](../generate_index.py#L692) | 692 | `"                f\"{source_line.file}:{source_line.line}: معرّف الملف لا يطابق الجرد\""` | — |
| [SRC-E599346ABE-L000693](../generate_index.py#L693) | 693 | `"            )"` | — |
| [SRC-E599346ABE-L000694](../generate_index.py#L694) | 694 | `"        if source_line.category != expected_item.category:"` | — |
| [SRC-E599346ABE-L000695](../generate_index.py#L695) | 695 | `"            failures.append("` | — |
| [SRC-E599346ABE-L000696](../generate_index.py#L696) | 696 | `"                f\"{source_line.file}:{source_line.line}: تصنيف السطر لا يطابق الجرد\""` | — |
| [SRC-E599346ABE-L000697](../generate_index.py#L697) | 697 | `"            )"` | — |
| [SRC-E599346ABE-L000698](../generate_index.py#L698) | 698 | `"        if source_line.line_id in seen_ids:"` | — |
| [SRC-E599346ABE-L000699](../generate_index.py#L699) | 699 | `"            failures.append(f\"{source_line.file}:{source_line.line}: معرّف SRC مكرر\")"` | — |
| [SRC-E599346ABE-L000700](../generate_index.py#L700) | 700 | `"        seen_ids.add(source_line.line_id)"` | — |
| [SRC-E599346ABE-L000701](../generate_index.py#L701) | 701 | `""` | — |
| [SRC-E599346ABE-L000702](../generate_index.py#L702) | 702 | `"    for file, item in eligible_files.items():"` | — |
| [SRC-E599346ABE-L000703](../generate_index.py#L703) | 703 | `"        actual = sorted(actual_lines[file])"` | — |
| [SRC-E599346ABE-L000704](../generate_index.py#L704) | 704 | `"        expected = list(range(1, (item.line_count or 0) + 1))"` | — |
| [SRC-E599346ABE-L000705](../generate_index.py#L705) | 705 | `"        if actual != expected:"` | — |
| [SRC-E599346ABE-L000706](../generate_index.py#L706) | 706 | `"            failures.append("` | — |
| [SRC-E599346ABE-L000707](../generate_index.py#L707) | 707 | `"                f\"{file}: المتوقع {len(expected)} سجل سطر مرقم بالتتابع، \""` | — |
| [SRC-E599346ABE-L000708](../generate_index.py#L708) | 708 | `"                f\"الموجود {len(actual)}\""` | — |
| [SRC-E599346ABE-L000709](../generate_index.py#L709) | 709 | `"            )"` | — |
| [SRC-E599346ABE-L000710](../generate_index.py#L710) | 710 | `""` | — |
| [SRC-E599346ABE-L000711](../generate_index.py#L711) | 711 | `"    if failures:"` | — |
| [SRC-E599346ABE-L000712](../generate_index.py#L712) | 712 | `"        raise IndexGenerationError("` | — |
| [SRC-E599346ABE-L000713](../generate_index.py#L713) | 713 | `"            \"فشل تحقق اكتمال فهرسة السطور؛ لن يُنشر فهرس جزئي:\\n- \""` | — |
| [SRC-E599346ABE-L000714](../generate_index.py#L714) | 714 | `"            + \"\\n- \".join(sorted(set(failures)))"` | — |
| [SRC-E599346ABE-L000715](../generate_index.py#L715) | 715 | `"        )"` | — |
| [SRC-E599346ABE-L000716](../generate_index.py#L716) | 716 | `""` | — |
| [SRC-E599346ABE-L000717](../generate_index.py#L717) | 717 | `""` | — |
| [SRC-E599346ABE-L000718](../generate_index.py#L718) | 718 | `"def discover_python_files(root: Path) -> list[Path]:"` | — |
| [SRC-E599346ABE-L000719](../generate_index.py#L719) | 719 | `"    \"\"\"Return sorted Python files from the eligible repository inventory.\"\"\""` | — |
| [SRC-E599346ABE-L000720](../generate_index.py#L720) | 720 | `""` | — |
| [SRC-E599346ABE-L000721](../generate_index.py#L721) | 721 | `"    return ["` | — |
| [SRC-E599346ABE-L000722](../generate_index.py#L722) | 722 | `"        path"` | — |
| [SRC-E599346ABE-L000723](../generate_index.py#L723) | 723 | `"        for path in discover_repository_files(root)"` | — |
| [SRC-E599346ABE-L000724](../generate_index.py#L724) | 724 | `"        if path.suffix.lower() == \".py\""` | — |
| [SRC-E599346ABE-L000725](../generate_index.py#L725) | 725 | `"    ]"` | — |
| [SRC-E599346ABE-L000726](../generate_index.py#L726) | 726 | `""` | — |
| [SRC-E599346ABE-L000727](../generate_index.py#L727) | 727 | `""` | — |
| [SRC-E599346ABE-L000728](../generate_index.py#L728) | 728 | `"def scan_repository(root: Path) -> tuple[list[IndexedSymbol], int]:"` | — |
| [SRC-E599346ABE-L000729](../generate_index.py#L729) | 729 | `"    \"\"\"Parse every eligible Python file or fail without producing a partial index.\"\"\""` | — |
| [SRC-E599346ABE-L000730](../generate_index.py#L730) | 730 | `"    python_files = discover_python_files(root)"` | — |
| [SRC-E599346ABE-L000731](../generate_index.py#L731) | 731 | `"    all_symbols: list[IndexedSymbol] = []"` | — |
| [SRC-E599346ABE-L000732](../generate_index.py#L732) | 732 | `"    failures: list[str] = []"` | — |
| [SRC-E599346ABE-L000733](../generate_index.py#L733) | 733 | `""` | — |
| [SRC-E599346ABE-L000734](../generate_index.py#L734) | 734 | `"    for source_path in python_files:"` | — |
| [SRC-E599346ABE-L000735](../generate_index.py#L735) | 735 | `"        relative_file = source_path.relative_to(root).as_posix()"` | — |
| [SRC-E599346ABE-L000736](../generate_index.py#L736) | 736 | `"        try:"` | — |
| [SRC-E599346ABE-L000737](../generate_index.py#L737) | 737 | `"            with tokenize.open(str(source_path)) as source_stream:"` | — |
| [SRC-E599346ABE-L000738](../generate_index.py#L738) | 738 | `"                source = source_stream.read()"` | — |
| [SRC-E599346ABE-L000739](../generate_index.py#L739) | 739 | `"            syntax_tree = ast.parse(source, filename=relative_file)"` | — |
| [SRC-E599346ABE-L000740](../generate_index.py#L740) | 740 | `"        except SyntaxError as exc:"` | — |
| [SRC-E599346ABE-L000741](../generate_index.py#L741) | 741 | `"            location = f\"السطر {exc.lineno}: {exc.msg}\" if exc.lineno else exc.msg"` | — |
| [SRC-E599346ABE-L000742](../generate_index.py#L742) | 742 | `"            failures.append(f\"{relative_file}: {location}\")"` | — |
| [SRC-E599346ABE-L000743](../generate_index.py#L743) | 743 | `"            continue"` | — |
| [SRC-E599346ABE-L000744](../generate_index.py#L744) | 744 | `"        except (OSError, UnicodeError, LookupError, tokenize.TokenError) as exc:"` | — |
| [SRC-E599346ABE-L000745](../generate_index.py#L745) | 745 | `"            failures.append(f\"{relative_file}: {type(exc).__name__}: {exc}\")"` | — |
| [SRC-E599346ABE-L000746](../generate_index.py#L746) | 746 | `"            continue"` | — |
| [SRC-E599346ABE-L000747](../generate_index.py#L747) | 747 | `""` | — |
| [SRC-E599346ABE-L000748](../generate_index.py#L748) | 748 | `"        visitor = SymbolVisitor(relative_file)"` | — |
| [SRC-E599346ABE-L000749](../generate_index.py#L749) | 749 | `"        visitor.visit(syntax_tree)"` | — |
| [SRC-E599346ABE-L000750](../generate_index.py#L750) | 750 | `"        all_symbols.extend(visitor.symbols)"` | — |
| [SRC-E599346ABE-L000751](../generate_index.py#L751) | 751 | `""` | — |
| [SRC-E599346ABE-L000752](../generate_index.py#L752) | 752 | `"    if failures:"` | — |
| [SRC-E599346ABE-L000753](../generate_index.py#L753) | 753 | `"        detail = \"\\n\".join(f\"- {failure}\" for failure in failures)"` | — |
| [SRC-E599346ABE-L000754](../generate_index.py#L754) | 754 | `"        raise IndexGenerationError("` | — |
| [SRC-E599346ABE-L000755](../generate_index.py#L755) | 755 | `"            \"تعذر إنشاء فهرس Python كامل؛ لم يُكتب MASTER_INDEX.md. \""` | — |
| [SRC-E599346ABE-L000756](../generate_index.py#L756) | 756 | `"            \"أصلح الملفات التالية ثم أعد التشغيل:\\n\" + detail"` | — |
| [SRC-E599346ABE-L000757](../generate_index.py#L757) | 757 | `"        )"` | — |
| [SRC-E599346ABE-L000758](../generate_index.py#L758) | 758 | `""` | — |
| [SRC-E599346ABE-L000759](../generate_index.py#L759) | 759 | `"    all_symbols.sort("` | — |
| [SRC-E599346ABE-L000760](../generate_index.py#L760) | 760 | `"        key=lambda symbol: ("` | — |
| [SRC-E599346ABE-L000761](../generate_index.py#L761) | 761 | `"            symbol.file.casefold(),"` | — |
| [SRC-E599346ABE-L000762](../generate_index.py#L762) | 762 | `"            symbol.line,"` | — |
| [SRC-E599346ABE-L000763](../generate_index.py#L763) | 763 | `"            symbol.name.casefold(),"` | — |
| [SRC-E599346ABE-L000764](../generate_index.py#L764) | 764 | `"            symbol.kind,"` | — |
| [SRC-E599346ABE-L000765](../generate_index.py#L765) | 765 | `"        )"` | — |
| [SRC-E599346ABE-L000766](../generate_index.py#L766) | 766 | `"    )"` | — |
| [SRC-E599346ABE-L000767](../generate_index.py#L767) | 767 | `"    return all_symbols, len(python_files)"` | — |
| [SRC-E599346ABE-L000768](../generate_index.py#L768) | 768 | `""` | — |
| [SRC-E599346ABE-L000769](../generate_index.py#L769) | 769 | `""` | — |
| [SRC-E599346ABE-L000770](../generate_index.py#L770) | 770 | `"def _line_at(source: str, offset: int, base_line: int = 1) -> int:"` | — |
| [SRC-E599346ABE-L000771](../generate_index.py#L771) | 771 | `"    \"\"\"Return a 1-based line number for a match in the supplied source fragment.\"\"\""` | — |
| [SRC-E599346ABE-L000772](../generate_index.py#L772) | 772 | `"    return base_line + source.count(\"\\n\", 0, offset)"` | — |
| [SRC-E599346ABE-L000773](../generate_index.py#L773) | 773 | `""` | — |
| [SRC-E599346ABE-L000774](../generate_index.py#L774) | 774 | `""` | — |
| [SRC-E599346ABE-L000775](../generate_index.py#L775) | 775 | `"def _add_marker("` | — |
| [SRC-E599346ABE-L000776](../generate_index.py#L776) | 776 | `"    markers: list[IndexedMarker],"` | — |
| [SRC-E599346ABE-L000777](../generate_index.py#L777) | 777 | `"    seen: set[tuple[str, str, str]],"` | — |
| [SRC-E599346ABE-L000778](../generate_index.py#L778) | 778 | `"    relative_file: str,"` | — |
| [SRC-E599346ABE-L000779](../generate_index.py#L779) | 779 | `"    name: str,"` | — |
| [SRC-E599346ABE-L000780](../generate_index.py#L780) | 780 | `"    kind: str,"` | — |
| [SRC-E599346ABE-L000781](../generate_index.py#L781) | 781 | `"    line: int,"` | — |
| [SRC-E599346ABE-L000782](../generate_index.py#L782) | 782 | `") -> None:"` | — |
| [SRC-E599346ABE-L000783](../generate_index.py#L783) | 783 | `"    \"\"\"Add the first occurrence of a symbol category within one file.\"\"\""` | — |
| [SRC-E599346ABE-L000784](../generate_index.py#L784) | 784 | `"    clean_name = \" \".join(name.strip().split())"` | — |
| [SRC-E599346ABE-L000785](../generate_index.py#L785) | 785 | `"    if not clean_name:"` | — |
| [SRC-E599346ABE-L000786](../generate_index.py#L786) | 786 | `"        return"` | — |
| [SRC-E599346ABE-L000787](../generate_index.py#L787) | 787 | `"    key = (relative_file, clean_name, kind)"` | — |
| [SRC-E599346ABE-L000788](../generate_index.py#L788) | 788 | `"    if key in seen:"` | — |
| [SRC-E599346ABE-L000789](../generate_index.py#L789) | 789 | `"        return"` | — |
| [SRC-E599346ABE-L000790](../generate_index.py#L790) | 790 | `"    seen.add(key)"` | — |
| [SRC-E599346ABE-L000791](../generate_index.py#L791) | 791 | `"    markers.append("` | — |
| [SRC-E599346ABE-L000792](../generate_index.py#L792) | 792 | `"        IndexedMarker("` | — |
| [SRC-E599346ABE-L000793](../generate_index.py#L793) | 793 | `"            file=relative_file,"` | — |
| [SRC-E599346ABE-L000794](../generate_index.py#L794) | 794 | `"            name=clean_name,"` | — |
| [SRC-E599346ABE-L000795](../generate_index.py#L795) | 795 | `"            kind=kind,"` | — |
| [SRC-E599346ABE-L000796](../generate_index.py#L796) | 796 | `"            line=max(line, 1),"` | — |
| [SRC-E599346ABE-L000797](../generate_index.py#L797) | 797 | `"        )"` | — |
| [SRC-E599346ABE-L000798](../generate_index.py#L798) | 798 | `"    )"` | — |
| [SRC-E599346ABE-L000799](../generate_index.py#L799) | 799 | `""` | — |
| [SRC-E599346ABE-L000800](../generate_index.py#L800) | 800 | `""` | — |
| [SRC-E599346ABE-L000801](../generate_index.py#L801) | 801 | `"def _scan_javascript("` | — |
| [SRC-E599346ABE-L000802](../generate_index.py#L802) | 802 | `"    source: str,"` | — |
| [SRC-E599346ABE-L000803](../generate_index.py#L803) | 803 | `"    relative_file: str,"` | — |
| [SRC-E599346ABE-L000804](../generate_index.py#L804) | 804 | `"    markers: list[IndexedMarker],"` | — |
| [SRC-E599346ABE-L000805](../generate_index.py#L805) | 805 | `"    seen: set[tuple[str, str, str]],"` | — |
| [SRC-E599346ABE-L000806](../generate_index.py#L806) | 806 | `"    base_line: int = 1,"` | — |
| [SRC-E599346ABE-L000807](../generate_index.py#L807) | 807 | `") -> None:"` | — |
| [SRC-E599346ABE-L000808](../generate_index.py#L808) | 808 | `"    \"\"\"Extract navigational JS/TS declarations using bounded regular-expression heuristics.\"\"\""` | — |
| [SRC-E599346ABE-L000809](../generate_index.py#L809) | 809 | `"    for pattern, kind in ("` | — |
| [SRC-E599346ABE-L000810](../generate_index.py#L810) | 810 | `"        (JS_FUNCTION_RE, \"دالة JavaScript/TypeScript\"),"` | — |
| [SRC-E599346ABE-L000811](../generate_index.py#L811) | 811 | `"        (JS_CLASS_RE, \"كلاس JavaScript/TypeScript\"),"` | — |
| [SRC-E599346ABE-L000812](../generate_index.py#L812) | 812 | `"    ):"` | — |
| [SRC-E599346ABE-L000813](../generate_index.py#L813) | 813 | `"        for match in pattern.finditer(source):"` | — |
| [SRC-E599346ABE-L000814](../generate_index.py#L814) | 814 | `"            _add_marker("` | — |
| [SRC-E599346ABE-L000815](../generate_index.py#L815) | 815 | `"                markers,"` | — |
| [SRC-E599346ABE-L000816](../generate_index.py#L816) | 816 | `"                seen,"` | — |
| [SRC-E599346ABE-L000817](../generate_index.py#L817) | 817 | `"                relative_file,"` | — |
| [SRC-E599346ABE-L000818](../generate_index.py#L818) | 818 | `"                match.group(1),"` | — |
| [SRC-E599346ABE-L000819](../generate_index.py#L819) | 819 | `"                kind,"` | — |
| [SRC-E599346ABE-L000820](../generate_index.py#L820) | 820 | `"                _line_at(source, match.start(), base_line),"` | — |
| [SRC-E599346ABE-L000821](../generate_index.py#L821) | 821 | `"            )"` | — |
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
