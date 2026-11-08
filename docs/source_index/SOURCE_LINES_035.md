# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **035**
- سجلات الأسطر: **800**
- النطاق: SRC-69F3587825-L000210 إلى SRC-B335630551-L000085
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## وثائق وفهرسة

### FILE-69F3587825 — [docs/search_code.py](../search_code.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
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
| [SRC-6B9B9ABE27-L000012](../ui-directions/README.md#L12) | 12 | `""` | — |
| [SRC-6B9B9ABE27-L000013](../ui-directions/README.md#L13) | 13 | `"## Option 02 — Precision Glass"` | — |
| [SRC-6B9B9ABE27-L000014](../ui-directions/README.md#L14) | 14 | `"- Restrained graphite glass, generous spacing, soft blue accent, evidence-first hierarchy."` | — |
| [SRC-6B9B9ABE27-L000015](../ui-directions/README.md#L15) | 15 | `"- Apple-inspired calm spatial depth without copying platform UI."` | — |
| [SRC-6B9B9ABE27-L000016](../ui-directions/README.md#L16) | 16 | `"- Best for sustained daily use, readability, and professional trust."` | — |
| [SRC-6B9B9ABE27-L000017](../ui-directions/README.md#L17) | 17 | `"- Preview: [variant-02-precision-glass.html](variant-02-precision-glass.html)"` | — |
| [SRC-6B9B9ABE27-L000018](../ui-directions/README.md#L18) | 18 | `""` | — |
| [SRC-6B9B9ABE27-L000019](../ui-directions/README.md#L19) | 19 | `"## Option 03 — Neon Command"` | — |
| [SRC-6B9B9ABE27-L000020](../ui-directions/README.md#L20) | 20 | `"- Compact command-center layout with navy surfaces and cyan/indigo luminous edges."` | — |
| [SRC-6B9B9ABE27-L000021](../ui-directions/README.md#L21) | 21 | `"- Strong operational hierarchy and denser information display."` | — |
| [SRC-6B9B9ABE27-L000022](../ui-directions/README.md#L22) | 22 | `"- Best for power users monitoring multiple market signals and qualification stages."` | — |
| [SRC-6B9B9ABE27-L000023](../ui-directions/README.md#L23) | 23 | `"- Preview: [variant-03-neon-command.html](variant-03-neon-command.html)"` | — |
| [SRC-6B9B9ABE27-L000024](../ui-directions/README.md#L24) | 24 | `""` | — |
| [SRC-6B9B9ABE27-L000025](../ui-directions/README.md#L25) | 25 | `"## Shared design requirements"` | — |
| [SRC-6B9B9ABE27-L000026](../ui-directions/README.md#L26) | 26 | `"- Arabic-first RTL; Noto Sans Arabic / IBM Plex Arabic system fallback."` | — |
| [SRC-6B9B9ABE27-L000027](../ui-directions/README.md#L27) | 27 | `"- Responsive desktop and mobile layouts with CSS breakpoints."` | — |
| [SRC-6B9B9ABE27-L000028](../ui-directions/README.md#L28) | 28 | `"- Evidence source/date and human-review status remain visible."` | — |
| [SRC-6B9B9ABE27-L000029](../ui-directions/README.md#L29) | 29 | `"- Demo records are illustrative and explicitly labeled."` | — |
| [SRC-6B9B9ABE27-L000030](../ui-directions/README.md#L30) | 30 | `"- No fabricated purchase probability, contact details, or real-world claims."` | — |
| [SRC-6B9B9ABE27-L000031](../ui-directions/README.md#L31) | 31 | `"- Static prototypes only: no production APIs, authentication, or backend behavior."` | — |
| [SRC-6B9B9ABE27-L000032](../ui-directions/README.md#L32) | 32 | `""` | — |
| [SRC-6B9B9ABE27-L000033](../ui-directions/README.md#L33) | 33 | `"## Approval gate"` | — |
| [SRC-6B9B9ABE27-L000034](../ui-directions/README.md#L34) | 34 | `"Human Director selects one direction. Only after selection should the chosen visual direction be refined and implemented against Omarai's existing session/lead API contracts. The other two remain archived proposals. No merge or deployment is authorized by this PR."` | — |
| [SRC-6B9B9ABE27-L000035](../ui-directions/README.md#L35) | 35 | `""` | — |
| [SRC-6B9B9ABE27-L000036](../ui-directions/README.md#L36) | 36 | `"## Human Director decision — 4 November 2026"` | — |
| [SRC-6B9B9ABE27-L000037](../ui-directions/README.md#L37) | 37 | `""` | — |
| [SRC-6B9B9ABE27-L000038](../ui-directions/README.md#L38) | 38 | `"**Selected:** Option 03 — Neon Command. This is the approved visual direction for implementation."` | — |
| [SRC-6B9B9ABE27-L000039](../ui-directions/README.md#L39) | 39 | `""` | — |
| [SRC-6B9B9ABE27-L000040](../ui-directions/README.md#L40) | 40 | `"- Implementation and backend connection are tracked in [PR #151](https://github.com/mosabosama2030-oss/omarai/pull/151)."` | — |
| [SRC-6B9B9ABE27-L000041](../ui-directions/README.md#L41) | 41 | `"- Options 01 and 02 remain reference proposals only."` | — |
| [SRC-6B9B9ABE27-L000042](../ui-directions/README.md#L42) | 42 | `"- This PR contains design previews; it does not implement or deploy the selected interface."` | — |
## وثائق وفهرسة

### FILE-7EB8FCD215 — [docs/ui-directions/variant-01-aurora-glass.html](../ui-directions/variant-01-aurora-glass.html#L1)

- النوع: **HTML**
- نطاق الفهرسة: جرد الملف + معرفات HTML والرموز داخل script/style

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-7EB8FCD215-L000001](../ui-directions/variant-01-aurora-glass.html#L1) | 1 | `"<!doctype html><html lang='ar' dir='rtl' data-agent-native-node-id=\"an-19qch1x\"><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><style>*{box-sizing:border-box}body{margin:0;background:radial-gradient(ellipse at 15% 5%,#173d58 0,transparent 38%),radial-gradient(ellipse at 85% 25%,#30234f 0,transparent 35%),#080e19;color:#e9f3ff;font:15px system-ui,'Noto Sans Arabic',sans-serif}.app{display:grid;grid-template-columns:245px 1fr;min-height:100vh;gap:18px;padding:20px}.side,.panel,.stat{background:linear-gradient(145deg,#ffffff12,#ffffff05);border:1px solid #b9d8ff20;backdrop-filter:blur(22px);border-radius:22px;box-shadow:0 20px 60px #0003}.side{padding:22px}.brand{font-size:25px;font-weight:800;color:#78eadb}.nav{margin-top:34px;display:grid;gap:10px}.nav div{padding:13px;border-radius:12px;color:#a9bdd2}.nav .active{background:#7debd51a;color:#8ff6e2;border:1px solid #8ff6e222}.main{min-width:0}.top{display:flex;justify-content:space-between;align-items:center;gap:12px}.pill{border:1px solid #ffffff20;background:#ffffff0b;padding:10px 15px;border-radius:30px;color:#bcd0e7}.hero{margin:25px 0}.hero h1{font-size:30px;margin:0 0 8px}.muted{color:#94a9c1}.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}.stat{padding:20px}.num{font-size:28px;color:#82efdc;font-weight:750;margin:12px 0}.layout{display:grid;grid-template-columns:1.5fr 1fr;gap:16px;margin-top:16px}.panel{padding:20px}.row{display:flex;justify-content:space-between;gap:12px;padding:15px 0;border-bottom:1px solid #ffffff12}.tag{color:#9af0d9;background:#4bd4b018;padding:6px 10px;border-radius:20px;font-size:12px}.stage{height:8px;background:#ffffff12;border-radius:20px;margin:12px 0}.stage i{display:block;width:62%;height:100%;background:linear-gradient(90deg,#67e7d1,#8c8cff);border-radius:20px}@media(max-width:850px){.app{grid-template-columns:1fr;padding:12px}.side{display:none}.stats{grid-template-columns:repeat(2,1fr)}.layout{grid-template-columns:1fr}.top{flex-wrap:wrap}.hero h1{font-size:24px}}@media(max-width:480px){.stats{gap:8px}.stat,.panel{padding:14px}.num{font-size:23px}.bottom{display:flex;position:sticky;bottom:8px;background:#101c2ce8;border:1px solid #ffffff20;border-radius:18px;padding:12px;justify-content:space-around;margin-top:14px}}</style></head><body data-agent-native-node-id=\"an-jqo3wt\"><div class='app' data-agent-native-node-id=\"an-id3wsl\"><aside class='side' data-agent-native-node-id=\"an-1mtuhlh\"><div class='brand' data-agent-native-node-id=\"an-1kt8xq9\">◈ عُمراي</div><p class='muted' data-agent-native-node-id=\"an-v1xw0d\">ذكاء المبيعات</p><div class='nav' data-agent-native-node-id=\"an-2kobx4\"><div class='active' data-agent-native-node-id=\"an-1463rp0\">◫ نظرة عامة</div><div data-agent-native-node-id=\"an-1d77149\">⌕ إشارات الطلب</div><div data-agent-native-node-id=\"an-1bo0gxl\">◎ مسار التأهيل</div><div data-agent-native-node-id=\"an-17ekjf2\">⌘ استخبارات السوق</div><div data-agent-native-node-id=\"an-1cwuece\">◉ المصادر</div></div></aside><main class='main' data-agent-native-node-id=\"an-s92bpi\"><div class='top' data-agent-native-node-id=\"an-cc9n77\"><span class='pill' data-agent-native-node-id=\"an-1jbfl7j\">⌕ ابحث في الإشارات والشركات</span><span class='pill' data-agent-native-node-id=\"an-1pixy7p\">مساحة العمل · القاهرة</span></div><section class='hero' data-agent-native-node-id=\"an-167w5oj\"><p class='muted' data-agent-native-node-id=\"an-weq0yq\">مساحة الاكتشاف / اليوم</p><h1 data-agent-native-node-id=\"an-yuv4wp\">أهلاً بك في مركز استخبارات المبيعات</h1><p class='muted' data-agent-native-node-id=\"an-1sofdf4\">راجع إشارات الاحتياج، افحص الأدلة، ثم قرر الخطوة التالية.</p></section><div class='stats' data-agent-native-node-id=\"an-5oj080\"><div class='stat' data-agent-native-node-id=\"an-v7letp\">الإشارات المحمّلة<div class='num' data-agent-native-node-id=\"an-14ar0bz\">128</div><span class='muted' data-agent-native-node-id=\"an-g0ywlg\">بيانات توضيحية</span></div><div class='stat' data-agent-native-node-id=\"an-1xnrcua\">تحتاج مراجعة<div class='num' data-agent-native-node-id=\"an-1la7h4l\">24</div><span class='muted' data-agent-native-node-id=\"an-5xvonf\">دليل ينتظر التحقق</span></div><div class='stat' data-agent-native-node-id=\"an-fi81m7\">مؤهلة<div class='num' data-agent-native-node-id=\"an-1vyro0u\">16</div><span class='muted' data-agent-native-node-id=\"an-691w91\">بعد مراجعة بشرية</span></div><div class='stat' data-agent-native-node-id=\"an-dcasvc\">متابعة<div class='num' data-agent-native-node-id=\"an-gx0je3\">9</div><span class='muted' data-agent-native-node-id=\"an-18eyy4r\">إجراء معتمد</span></div></div><div class='layout' data-agent-native-node-id=\"an-o3zzps\"><section class='panel' data-agent-native-node-id=\"an-hrlmec\"><h2 data-agent-native-node-id=\"an-a0ruc7\">إشارات نية الشراء</h2><div class='row' data-agent-native-node-id=\"an-ppfwfb\"><div data-agent-native-node-id=\"an-lfbdow\"><b data-agent-native-node-id=\"an-miv3l8\">طلب توريد تجهيزات مكتبية</b><p class='muted' data-agent-native-node-id=\"an-13dfohj\">مصدر عام · منذ ساعتين</p></div><span class='tag' data-agent-native-node-id=\"an-9o8iae\">يحتاج مراجعة</span></div><div class='row' data-agent-native-node-id=\"an-vbx8l6\"><div data-agent-native-node-id=\"an-vluil2\"><b data-agent-native-node-id=\"an-8gvvpq\">بحث عن مقاول صيانة تكييف</b><p class='muted' data-agent-native-node-id=\"an-17hc0lw\">طلب خدمة منشور · أمس</p></div><span class='tag' data-agent-native-node-id=\"an-1hauho4\">دليل مرفق</span></div><div class='row' data-agent-native-node-id=\"an-1b2uxnn\"><div data-agent-native-node-id=\"an-ux9f9v\"><b data-agent-native-node-id=\"an-1v8ly8q\">احتياج معدات لمشروع جديد</b><p class='muted' data-agent-native-node-id=\"an-1h1ku9q\">إعلان طلب · منذ 3 أيام</p></div><span class='tag' data-agent-native-node-id=\"an-174ll6b\">مراجعة بشرية</span></div></section><section class='panel' data-agent-native-node-id=\"an-o9dfs0\"><h2 data-agent-native-node-id=\"an-1i8fydy\">مسار التأهيل</h2><p class='muted' data-agent-native-node-id=\"an-1ww1ij3\">من الإشارة إلى فرصة قابلة للمتابعة</p><div class='row' data-agent-native-node-id=\"an-1pf4hxb\">جديد <b data-agent-native-node-id=\"an-11rtvkb\">24</b></div><div class='stage' data-agent-native-node-id=\"an-8fp3e2\"><i data-agent-native-node-id=\"an-utv0o8\"></i></div><div class='row' data-agent-native-node-id=\"an-1l2qrh2\">مؤهل <b data-agent-native-node-id=\"an-el3suf\">16</b></div><div class='row' data-agent-native-node-id=\"an-1s3h6yb\">موافقة متابعة <b data-agent-native-node-id=\"an-1ij68k7\">9</b></div><p class='muted' data-agent-native-node-id=\"an-mtq2mz\">لا تمثل الأرقام احتمال شراء.</p></section></div><div class='bottom' style='display:none' data-agent-native-node-id=\"an-tgu348\">نظرة عامة　 إشارات　 متابعة　 المزيد</div></main></div></body></html>"` | — |
## وثائق وفهرسة

### FILE-2A9FC16EBA — [docs/ui-directions/variant-02-precision-glass.html](../ui-directions/variant-02-precision-glass.html#L1)

- النوع: **HTML**
- نطاق الفهرسة: جرد الملف + معرفات HTML والرموز داخل script/style

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-2A9FC16EBA-L000001](../ui-directions/variant-02-precision-glass.html#L1) | 1 | `"<!doctype html><html lang='ar' dir='rtl' data-agent-native-node-id=\"an-19qch1x\"><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><style>*{box-sizing:border-box}body{margin:0;background:linear-gradient(135deg,#11151d,#202630 55%,#10141b);color:#f4f6fa;font:15px system-ui,'Noto Sans Arabic',sans-serif}.app{display:grid;grid-template-columns:230px 1fr;gap:24px;padding:28px;min-height:100vh}.side,.panel,.stat{background:#ffffff09;border:1px solid #ffffff12;border-radius:18px;backdrop-filter:blur(18px)}.side{padding:24px}.brand{font-size:24px;font-weight:800}.nav{margin-top:38px;display:grid;gap:8px}.nav div{padding:12px;color:#aab2c0;border-radius:10px}.nav .active{background:#ffffff13;color:white}.main{min-width:0}.top{display:flex;justify-content:space-between;align-items:center}.pill{background:#ffffff0a;border:1px solid #ffffff15;border-radius:25px;padding:10px 15px;color:#c7ced9}.hero{margin:32px 0 24px}.hero h1{font-size:30px;margin:8px 0}.muted{color:#9ca6b5}.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}.stat{padding:22px}.num{font-size:28px;font-weight:750;margin-top:12px;color:#b6caff}.layout{display:grid;grid-template-columns:1.65fr 1fr;gap:16px;margin-top:18px}.panel{padding:22px}.head{display:flex;justify-content:space-between;align-items:center}.row{display:grid;grid-template-columns:1fr auto;gap:16px;padding:17px 0;border-bottom:1px solid #ffffff10}.tag{font-size:12px;border:1px solid #9dbbff35;color:#c2d2ff;padding:6px 10px;border-radius:20px}.small{font-size:13px;color:#9ca6b5;margin-top:6px}.stage{padding:12px;border-radius:12px;background:#ffffff07;margin:8px 0;display:flex;justify-content:space-between}@media(max-width:900px){.app{grid-template-columns:1fr;padding:14px}.side{display:none}.stats{grid-template-columns:repeat(2,1fr)}.layout{grid-template-columns:1fr}}@media(max-width:520px){.hero h1{font-size:23px}.stat,.panel{padding:15px}.top{flex-wrap:wrap;gap:10px}.row{grid-template-columns:1fr}.tag{width:max-content}.stats{gap:9px}}</style></head><body data-agent-native-node-id=\"an-1j4akuv\"><div class='app' data-agent-native-node-id=\"an-1hfh13r\"><aside class='side' data-agent-native-node-id=\"an-112duoj\"><div class='brand' data-agent-native-node-id=\"an-1pcl5xi\">عُمرَاي <span style='color:#a9bfff' data-agent-native-node-id=\"an-18n69jp\">◈</span></div><p class='muted' data-agent-native-node-id=\"an-kez2g3\">Sales Intelligence</p><div class='nav' data-agent-native-node-id=\"an-1p4ub9j\"><div class='active' data-agent-native-node-id=\"an-sg1enl\">نظرة عامة</div><div data-agent-native-node-id=\"an-1k86e90\">إشارات الطلب</div><div data-agent-native-node-id=\"an-qpqymk\">الفرص المؤهلة</div><div data-agent-native-node-id=\"an-1med0am\">الشركات</div><div data-agent-native-node-id=\"an-1hu57w9\">المصادر</div></div></aside><main class='main' data-agent-native-node-id=\"an-1mzncze\"><div class='top' data-agent-native-node-id=\"an-1e00uky\"><span class='pill' data-agent-native-node-id=\"an-7potb\">⌕ بحث في مساحة العمل</span><span class='pill' data-agent-native-node-id=\"an-11th5gr\">القاهرة · السوق الحالي</span></div><div class='hero' data-agent-native-node-id=\"an-1lzto1f\"><p class='muted' data-agent-native-node-id=\"an-1gpsw30\">لوحة التحكم</p><h1 data-agent-native-node-id=\"an-4buxe3\">صورة واضحة للطلب الحقيقي</h1><p class='muted' data-agent-native-node-id=\"an-1h4ptkn\">كل إشارة مرتبطة بمصدر وتاريخ رصد وحالة مراجعة.</p></div><div class='stats' data-agent-native-node-id=\"an-u5n57n\"><div class='stat' data-agent-native-node-id=\"an-17c38zi\">الإشارات<div class='num' data-agent-native-node-id=\"an-2av4q2\">128</div><span class='muted' data-agent-native-node-id=\"an-137q4v3\">عينة توضيحية</span></div><div class='stat' data-agent-native-node-id=\"an-1hwxyth\">تحتاج تحقق<div class='num' data-agent-native-node-id=\"an-1meevms\">24</div><span class='muted' data-agent-native-node-id=\"an-16bhkaz\">غير محسومة</span></div><div class='stat' data-agent-native-node-id=\"an-38nlrf\">مؤهلة<div class='num' data-agent-native-node-id=\"an-vjexqh\">16</div><span class='muted' data-agent-native-node-id=\"an-1ukwo4b\">بعد المراجعة</span></div><div class='stat' data-agent-native-node-id=\"an-168nhnz\">متابعة معتمدة<div class='num' data-agent-native-node-id=\"an-j5dhyj\">9</div><span class='muted' data-agent-native-node-id=\"an-q7lg7k\">بقرار بشري</span></div></div><div class='layout' data-agent-native-node-id=\"an-1qlm3ef\"><section class='panel' data-agent-native-node-id=\"an-c6kpy3\"><div class='head' data-agent-native-node-id=\"an-1j2luvv\"><h2 data-agent-native-node-id=\"an-7i25e\">سجل الإشارات</h2><span class='pill' data-agent-native-node-id=\"an-q5k2sk\">تصفية</span></div><div class='row' data-agent-native-node-id=\"an-u2h5rr\"><div data-agent-native-node-id=\"an-1ehg159\"><b data-agent-native-node-id=\"an-dut9mw\">طلب توريد تجهيزات مكتبية</b><div class='small' data-agent-native-node-id=\"an-10dplvb\">طلب منشور · مصدر عام · رُصد اليوم</div></div><span class='tag' data-agent-native-node-id=\"an-wfjfwj\">قيد المراجعة</span></div><div class='row' data-agent-native-node-id=\"an-1bg1cwv\"><div data-agent-native-node-id=\"an-1wbu9nc\"><b data-agent-native-node-id=\"an-1c8pq2g\">بحث عن خدمة صيانة</b><div class='small' data-agent-native-node-id=\"an-p98jb0\">طلب خدمة · مصدر عام · أمس</div></div><span class='tag' data-agent-native-node-id=\"an-vta5sd\">يحتاج تحقق</span></div><div class='row' data-agent-native-node-id=\"an-soyt1f\"><div data-agent-native-node-id=\"an-1kadc9f\"><b data-agent-native-node-id=\"an-1y8nzvb\">احتياج معدات مشروع</b><div class='small' data-agent-native-node-id=\"an-1ak348p\">إعلان طلب · منذ 3 أيام</div></div><span class='tag' data-agent-native-node-id=\"an-1n9ezek\">مؤهل</span></div></section><section class='panel' data-agent-native-node-id=\"an-1eav9eb\"><h2 data-agent-native-node-id=\"an-1bmvh9u\">التقدم</h2><div class='stage' data-agent-native-node-id=\"an-ar13bc\">جديد <b data-agent-native-node-id=\"an-1s814ma\">24</b></div><div class='stage' data-agent-native-node-id=\"an-1mq3eg4\">قيد التحقق <b data-agent-native-node-id=\"an-h4z0g5\">16</b></div><div class='stage' data-agent-native-node-id=\"an-4nspk5\">موافقة متابعة <b data-agent-native-node-id=\"an-fm2q8d\">9</b></div><p class='muted' data-agent-native-node-id=\"an-1fqgeo8\">الترتيب يعكس حالة المراجعة، وليس احتمالية الشراء.</p></section></div></main></div></body></html>"` | — |
## وثائق وفهرسة

### FILE-D7D5153A8A — [docs/ui-directions/variant-03-neon-command.html](../ui-directions/variant-03-neon-command.html#L1)

- النوع: **HTML**
- نطاق الفهرسة: جرد الملف + معرفات HTML والرموز داخل script/style

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-D7D5153A8A-L000001](../ui-directions/variant-03-neon-command.html#L1) | 1 | `"<!doctype html><html lang='ar' dir='rtl' data-agent-native-node-id=\"an-19qch1x\"><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><style>*{box-sizing:border-box}body{margin:0;background:radial-gradient(ellipse at 50% -20%,#15364d,transparent 55%),#070d16;color:#e7f7ff;font:14px system-ui,'Noto Sans Arabic',sans-serif}.app{display:grid;grid-template-columns:220px 1fr;gap:14px;padding:16px;min-height:100vh}.side,.panel,.stat{background:linear-gradient(145deg,#102334d9,#0b1724d9);border:1px solid #4ad8ff24;border-radius:16px;box-shadow:inset 0 1px #ffffff08,0 14px 40px #0004}.side{padding:18px}.brand{font-size:23px;font-weight:800;color:#6cecff}.nav{display:grid;gap:7px;margin-top:30px}.nav div{padding:12px;border-radius:9px;color:#89a9bc}.nav .active{background:#43dfff14;border:1px solid #43dfff2b;color:#7beaff}.main{min-width:0}.top{display:flex;justify-content:space-between;gap:10px}.pill{padding:9px 13px;border:1px solid #39cfff25;border-radius:9px;background:#0d1d2a;color:#9bc5d8}.hero{margin:22px 0}.hero h1{margin:5px 0;font-size:27px}.muted{color:#7799ad}.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}.stat{padding:17px}.num{font-size:26px;color:#71eaff;font-weight:800;margin:8px 0}.layout{display:grid;grid-template-columns:1.7fr 1fr;gap:12px;margin-top:12px}.panel{padding:17px}.panel h2{font-size:16px}.row{display:flex;justify-content:space-between;gap:10px;padding:13px 0;border-bottom:1px solid #2b4b5c}.tag{font-size:11px;color:#7ceaff;border:1px solid #2e9dbb55;padding:5px 9px;border-radius:7px}.meta{font-size:12px;color:#7593a5;margin-top:5px}.stage{display:flex;justify-content:space-between;padding:10px;margin:7px 0;background:#07131f;border:1px solid #1c3c50;border-radius:9px}.bar{height:5px;background:#152e3d;margin:10px 0;border-radius:9px}.bar i{display:block;width:57%;height:100%;background:#52dfff}@media(max-width:900px){.app{grid-template-columns:1fr;padding:10px}.side{display:none}.stats{grid-template-columns:repeat(2,1fr)}.layout{grid-template-columns:1fr}}@media(max-width:520px){.top{flex-direction:column}.hero h1{font-size:22px}.stat,.panel{padding:13px}.row{flex-direction:column}.tag{width:max-content}.stats{gap:7px}}</style></head><body data-agent-native-node-id=\"an-1mq2fgv\"><div class='app' data-agent-native-node-id=\"an-1snvlzn\"><aside class='side' data-agent-native-node-id=\"an-1u3uwz9\"><div class='brand' data-agent-native-node-id=\"an-1kzndb8\">◈ OMARAI</div><p class='muted' data-agent-native-node-id=\"an-ze5rg3\">INTELLIGENCE OS</p><div class='nav' data-agent-native-node-id=\"an-1r5k24x\"><div class='active' data-agent-native-node-id=\"an-z3nr0e\">⌘ مركز القيادة</div><div data-agent-native-node-id=\"an-1p079np\">⌕ إشارات الطلب</div><div data-agent-native-node-id=\"an-1291c89\">▤ التأهيل</div><div data-agent-native-node-id=\"an-phglyz\">◉ المصادر</div><div data-agent-native-node-id=\"an-8t0lis\">◌ حالة النظام</div></div></aside><main class='main' data-agent-native-node-id=\"an-1i54o1l\"><div class='top' data-agent-native-node-id=\"an-1jzcjba\"><span class='pill' data-agent-native-node-id=\"an-14wb78m\">⌕ بحث سريع / أمر</span><span class='pill' data-agent-native-node-id=\"an-1ku3fel\">MARKET: CAIRO · DEMO</span></div><section class='hero' data-agent-native-node-id=\"an-1amx86t\"><p class='muted' data-agent-native-node-id=\"an-15vdw4u\">SALES INTELLIGENCE / OVERVIEW</p><h1 data-agent-native-node-id=\"an-1y9mhoi\">مركز قيادة فرص السوق</h1><p class='muted' data-agent-native-node-id=\"an-4tzg1a\">رصد الاحتياج ← تحقق من الدليل ← تأهيل ← موافقة بشرية</p></section><div class='stats' data-agent-native-node-id=\"an-13ci5nn\"><div class='stat' data-agent-native-node-id=\"an-1a41epk\">إشارات واردة<div class='num' data-agent-native-node-id=\"an-wbhqbf\">128</div><span class='muted' data-agent-native-node-id=\"an-1df3phi\">بيانات تجريبية</span></div><div class='stat' data-agent-native-node-id=\"an-1s37bcg\">تحتاج تحقق<div class='num' data-agent-native-node-id=\"an-a4np0m\">24</div><span class='muted' data-agent-native-node-id=\"an-1584zmq\">Evidence review</span></div><div class='stat' data-agent-native-node-id=\"an-10uv4u1\">فرص مؤهلة<div class='num' data-agent-native-node-id=\"an-gjrv4f\">16</div><span class='muted' data-agent-native-node-id=\"an-1pirizs\">Reviewed</span></div><div class='stat' data-agent-native-node-id=\"an-1lrxcs7\">متابعة معتمدة<div class='num' data-agent-native-node-id=\"an-13wf6iv\">9</div><span class='muted' data-agent-native-node-id=\"an-s3k1hp\">Human-approved</span></div></div><div class='layout' data-agent-native-node-id=\"an-1f9sws\"><section class='panel' data-agent-native-node-id=\"an-uxvkmt\"><h2 data-agent-native-node-id=\"an-1xmc0cq\">LIVE SIGNAL QUEUE <span class='tag' data-agent-native-node-id=\"an-2h120v\">DEMO</span></h2><div class='row' data-agent-native-node-id=\"an-p2w54e\"><div data-agent-native-node-id=\"an-s1tel5\"><b data-agent-native-node-id=\"an-1yimqje\">طلب توريد تجهيزات مكتبية</b><div class='meta' data-agent-native-node-id=\"an-grpnev\">Public request · observed today</div></div><span class='tag' data-agent-native-node-id=\"an-nyd3xz\">REVIEW</span></div><div class='row' data-agent-native-node-id=\"an-ifohvr\"><div data-agent-native-node-id=\"an-3yxllp\"><b data-agent-native-node-id=\"an-ew8vf2\">طلب خدمة صيانة تكييف</b><div class='meta' data-agent-native-node-id=\"an-1vqr3zn\">Service request · yesterday</div></div><span class='tag' data-agent-native-node-id=\"an-s6kpwr\">VERIFY</span></div><div class='row' data-agent-native-node-id=\"an-1a7e2g0\"><div data-agent-native-node-id=\"an-202ik7\"><b data-agent-native-node-id=\"an-q0ez4n\">احتياج معدات مشروع</b><div class='meta' data-agent-native-node-id=\"an-xv1lu2\">Public listing · 3 days</div></div><span class='tag' data-agent-native-node-id=\"an-12nnh34\">QUALIFY</span></div></section><section class='panel' data-agent-native-node-id=\"an-ud0485\"><h2 data-agent-native-node-id=\"an-1xxdkmf\">QUALIFICATION PIPELINE</h2><div class='stage' data-agent-native-node-id=\"an-148mwmh\">New <b data-agent-native-node-id=\"an-1pi8wxr\">24</b></div><div class='bar' data-agent-native-node-id=\"an-1dyg74u\"><i data-agent-native-node-id=\"an-1mp2h7o\"></i></div><div class='stage' data-agent-native-node-id=\"an-pe36jr\">Verified <b data-agent-native-node-id=\"an-9927oo\">16</b></div><div class='stage' data-agent-native-node-id=\"an-1uli6yk\">Approved <b data-agent-native-node-id=\"an-1hwy8tc\">9</b></div><p class='muted' data-agent-native-node-id=\"an-5lffxl\">Operational states only — no purchase-probability score.</p></section></div></main></div></body></html>"` | — |
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
| [SRC-50C86B7ED8-L000016](../../pyproject.toml#L16) | 16 | `"  \"psycopg[binary]>=3.2,<4\","` | — |
| [SRC-50C86B7ED8-L000017](../../pyproject.toml#L17) | 17 | `"]"` | — |
| [SRC-50C86B7ED8-L000018](../../pyproject.toml#L18) | 18 | `""` | — |
| [SRC-50C86B7ED8-L000019](../../pyproject.toml#L19) | 19 | `"[project.optional-dependencies]"` | — |
| [SRC-50C86B7ED8-L000020](../../pyproject.toml#L20) | 20 | `"dev = [\"pytest>=8.0\", \"ruff>=0.5\"]"` | — |
| [SRC-50C86B7ED8-L000021](../../pyproject.toml#L21) | 21 | `""` | — |
| [SRC-50C86B7ED8-L000022](../../pyproject.toml#L22) | 22 | `"[tool.pytest.ini_options]"` | — |
| [SRC-50C86B7ED8-L000023](../../pyproject.toml#L23) | 23 | `"testpaths = [\"tests\"]"` | — |
| [SRC-50C86B7ED8-L000024](../../pyproject.toml#L24) | 24 | `""` | — |
| [SRC-50C86B7ED8-L000025](../../pyproject.toml#L25) | 25 | `"[tool.setuptools.packages.find]"` | — |
| [SRC-50C86B7ED8-L000026](../../pyproject.toml#L26) | 26 | `"include = [\"agents*\", \"api*\", \"cli*\"]"` | — |
| [SRC-50C86B7ED8-L000027](../../pyproject.toml#L27) | 27 | `"exclude = [\"tests*\", \"web*\"]"` | — |
| [SRC-50C86B7ED8-L000028](../../pyproject.toml#L28) | 28 | `""` | — |
| [SRC-50C86B7ED8-L000029](../../pyproject.toml#L29) | 29 | `"[tool.ruff]"` | — |
| [SRC-50C86B7ED8-L000030](../../pyproject.toml#L30) | 30 | `"line-length = 100"` | — |
| [SRC-50C86B7ED8-L000031](../../pyproject.toml#L31) | 31 | `"target-version = \"py311\""` | — |
| [SRC-50C86B7ED8-L000032](../../pyproject.toml#L32) | 32 | `""` | — |
| [SRC-50C86B7ED8-L000033](../../pyproject.toml#L33) | 33 | `"[tool.ruff.lint]"` | — |
| [SRC-50C86B7ED8-L000034](../../pyproject.toml#L34) | 34 | `"# Keep default rules; ignore only patterns intentional in this codebase."` | — |
| [SRC-50C86B7ED8-L000035](../../pyproject.toml#L35) | 35 | `"# BLE001: broad except at API boundary to avoid leaking internals"` | — |
| [SRC-50C86B7ED8-L000036](../../pyproject.toml#L36) | 36 | `"# E501: long Arabic/English diagnostic strings"` | — |
| [SRC-50C86B7ED8-L000037](../../pyproject.toml#L37) | 37 | `"# I001: historical import order; do not block CI on style alone"` | — |
| [SRC-50C86B7ED8-L000038](../../pyproject.toml#L38) | 38 | `"# F841: unused assignment kept for clarity in some tests"` | — |
| [SRC-50C86B7ED8-L000039](../../pyproject.toml#L39) | 39 | `"# RUF100: residual noqa:BLE001 comments after BLE001 is ignored globally"` | — |
| [SRC-50C86B7ED8-L000040](../../pyproject.toml#L40) | 40 | `"ignore = [\"BLE001\", \"E501\", \"I001\", \"F841\", \"RUF100\"]"` | — |
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
| [SRC-B335630551-L000001](../../README.md#L1) | 1 | `"# Omarai — Arabic-First AI Sales Intelligence & Customer Acquisition Agent"` | — |
| [SRC-B335630551-L000002](../../README.md#L2) | 2 | `""` | — |
| [SRC-B335630551-L000003](../../README.md#L3) | 3 | `"> **Foundational engineering requirements:** mandatory contributor/agent rules are in [AGENTS.md](AGENTS.md). The core architecture and security charter is [OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md](docs/OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md); the expanded platform practices across reliability, security, privacy, data, SRE, AI, accessibility, supply chain, and cost are in [OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md](docs/OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md); and the requirement IDs, expert-review lenses, evidence model, risk priorities, maturity stages, and release gates are in [OMARAI_REQUIREMENTS_TRACEABILITY_AND_MATURITY_MODEL_AR.md](docs/OMARAI_REQUIREMENTS_TRACEABILITY_AND_MATURITY_MODEL_AR.md). The initial foundational requirements checklist is [OMARAI_REQUIREMENTS_REGISTER.md](docs/OMARAI_REQUIREMENTS_REGISTER.md). These documents define required direction; they do not prove every control is implemented or tested. Use the [documentation index](docs/README.md) to find the current source of truth for each topic."` | — |
| [SRC-B335630551-L000004](../../README.md#L4) | 4 | `""` | — |
| [SRC-B335630551-L000005](../../README.md#L5) | 5 | `""` | — |
| [SRC-B335630551-L000006](../../README.md#L6) | 6 | `"Omarai's product mission is to be an Arabic-first AI Sales Intelligence and Customer Acquisition Agent: understand a product or service and its market, discover public and permitted buying-demand signals, verify their evidence, qualify opportunities, and recommend useful sales follow-ups."` | — |
| [SRC-B335630551-L000007](../../README.md#L7) | 7 | `""` | — |
| [SRC-B335630551-L000008](../../README.md#L8) | 8 | ``"The current repository provides a bounded web-research and evidence pipeline, a `LEAD_GENERATION` intent route, an initial buyer-signal detector, and a local lead workspace. These are foundational capabilities, **not proof of a complete end-to-end sales intelligence product**. Product understanding, ICP-aware demand discovery, multi-type signal classification, evidence-backed qualification, and the full sales workflow remain subject to the implementation and acceptance gates in the [Sales Intelligence Architecture](docs/OMARAI_SALES_INTELLIGENCE_ARCHITECTURE_AR.md)."`` | — |
| [SRC-B335630551-L000009](../../README.md#L9) | 9 | `""` | — |
| [SRC-B335630551-L000010](../../README.md#L10) | 10 | `"The existing responsive RTL research interface and general web-research capabilities remain shared platform capabilities. The sales domain should reuse them rather than create a second search engine."` | — |
| [SRC-B335630551-L000011](../../README.md#L11) | 11 | `""` | — |
| [SRC-B335630551-L000012](../../README.md#L12) | 12 | ``"The Arabic RTL sales workspace is the product's primary experience at `/` and `/workspace`. The general-purpose web-research agent remains available at `/agent`, while the legacy lead dashboard remains at `/leads`. Public-web research, page reading, evidence handling, and language models are shared platform capabilities that support the sales-intelligence mission; they are not the product's end goal."`` | — |
| [SRC-B335630551-L000013](../../README.md#L13) | 13 | `""` | — |
| [SRC-B335630551-L000014](../../README.md#L14) | 14 | `"## Product direction and current delivery snapshot — 6 November 2026"` | — |
| [SRC-B335630551-L000015](../../README.md#L15) | 15 | `""` | — |
| [SRC-B335630551-L000016](../../README.md#L16) | 16 | `"Omarai's approved product direction is evidence-backed discovery and qualification of public buying-demand signals for a user-described product/service and market. A company matching the target profile is not, by itself, a buyer-intent signal. The product does not perform automated outreach."` | — |
| [SRC-B335630551-L000017](../../README.md#L17) | 17 | `""` | — |
| [SRC-B335630551-L000018](../../README.md#L18) | 18 | ``"- Current `main`: `a297abd271d48f459effad083a9f424a1499cd39`."`` | — |
| [SRC-B335630551-L000019](../../README.md#L19) | 19 | ``"- The default route `/` and `/workspace` serve the Arabic sales workspace; `/agent` serves the general research agent; `/leads` preserves the legacy lead view."`` | — |
| [SRC-B335630551-L000020](../../README.md#L20) | 20 | `"- The currently connected workspace views are overview, existing demand-signal inbox, qualification pipeline, and a non-probing system snapshot. Other menu modules remain unavailable unless a server-side contract is implemented and verified."` | — |
| [SRC-B335630551-L000021](../../README.md#L21) | 21 | ``"- Product profiles and buyer-intent discovery are proposed in [PR #155](https://github.com/mosabosama2030-oss/omarai/pull/155), which is **open and not merged** in this snapshot. Do not treat those capabilities as part of `main`."`` | — |
| [SRC-B335630551-L000022](../../README.md#L22) | 22 | `"- See [current project status and governing decisions](docs/OMARAI_PROJECT_STATUS_AND_DECISIONS_AR.md) for merge state, CI evidence, open risks, and release gates."` | — |
| [SRC-B335630551-L000023](../../README.md#L23) | 23 | `""` | — |
| [SRC-B335630551-L000024](../../README.md#L24) | 24 | `"## What this version does"` | — |
| [SRC-B335630551-L000025](../../README.md#L25) | 25 | `""` | — |
| [SRC-B335630551-L000026](../../README.md#L26) | 26 | `"- Plans up to eight search queries from a natural-language question with a dedicated reasoning/planning model, and uses a deterministic multi-query fallback when the model is unavailable."` | — |
| [SRC-B335630551-L000027](../../README.md#L27) | 27 | `"- Uses separate model roles by default: NVIDIA Nemotron 3 Ultra (free) for query planning and Google Gemma 4 31B Instruct (free) for answer synthesis and the second-pass consistency review; retries with OpenRouter's free-model router if a chosen model fails."` | — |
| [SRC-B335630551-L000028](../../README.md#L28) | 28 | `"- Runs DuckDuckGo HTML and Bing RSS independently for every planned query; can add official Brave Search API and Tavily Search API result indexes when their environment keys are configured; uses Google News RSS for queries judged time-sensitive."` | — |
| [SRC-B335630551-L000029](../../README.md#L29) | 29 | `"- Fuses duplicate results across queries and engines using reciprocal-rank fusion, preserving provider, query, domain, platform, publication-date and page-extraction provenance."` | — |
| [SRC-B335630551-L000030](../../README.md#L30) | 30 | `"- Extracts text from up to eight accessible public pages per question with request-size and timeout bounds, following at most three individually validated public redirects."` | — |
| [SRC-B335630551-L000031](../../README.md#L31) | 31 | ``"- Searches public Reddit RSS and the Bluesky public search endpoint when social discussion is relevant; can use Reddit's OAuth API when `REDDIT_CLIENT_ID` and `REDDIT_CLIENT_SECRET` are provided."`` | — |
| [SRC-B335630551-L000032](../../README.md#L32) | 32 | `"- Searches indexed public pages on Facebook, Instagram, X, TikTok, LinkedIn, Threads and YouTube through the general web engines."` | — |
| [SRC-B335630551-L000033](../../README.md#L33) | 33 | `"- Can use the official Meta Graph API to read posts and a small sample of public comments from explicitly configured Facebook Pages when the token has suitable permissions."` | — |
| [SRC-B335630551-L000034](../../README.md#L34) | 34 | ``"- Can use Instagram Graph API hashtag search to read public hashtag media when `INSTAGRAM_USER_ID` and `INSTAGRAM_ACCESS_TOKEN` have the required permissions. It is not a global Instagram search and has platform quotas."`` | — |
| [SRC-B335630551-L000035](../../README.md#L35) | 35 | ``"- Can use the official X recent-post endpoint when `X_BEARER_TOKEN` is configured and the account/API tier permits the request; can use the official YouTube Data API when `YOUTUBE_API_KEY` is configured."`` | — |
| [SRC-B335630551-L000036](../../README.md#L36) | 36 | `"- Generates an evidence-grounded answer in the user's language, showing source links, query plan, provider coverage, direct page reads, platform mix, source/domain diversity, date coverage, and evidence-coverage warnings. Coverage indicators describe breadth and inspectability; they are not probabilities that the answer is true."` | — |
| [SRC-B335630551-L000037](../../README.md#L37) | 37 | `"- Carries up to eight recent chat messages from the current browser session into follow-up questions."` | — |
| [SRC-B335630551-L000038](../../README.md#L38) | 38 | ``"- Keeps the existing local SQLite lead workspace at `/leads`. The approved Arabic RTL Neon Command sales workspace is the default home at `/` and remains available at `/workspace`; it includes overview, tenant-scoped product/market profiles, buyer-intent discovery runs using the existing lead-generation search pipeline, human-reviewed saving of server-qualified public-demand signals, signal review, and qualification-status updates. The general web-research agent remains available at `/agent`. The system-state view reads the non-probing `/api/health` configuration snapshot. Company profiles, market analytics, scheduled monitoring, evidence/audit centers, tasks, settings and other modules without completed server contracts remain explicitly unavailable."`` | — |
| [SRC-B335630551-L000039](../../README.md#L39) | 39 | `"- Binds to loopback by default; it is not a public production deployment."` | — |
| [SRC-B335630551-L000040](../../README.md#L40) | 40 | `""` | — |
| [SRC-B335630551-L000041](../../README.md#L41) | 41 | ``"**Verification semantics:** `GET /api/health` is a configuration/dependency snapshot, not proof that search providers or the model are reachable. Check the `agent.verification_scope` field to see what is and is not verified. Use the protected `POST /api/diagnostics` endpoint for explicit live search/model probes; a passed diagnostic only verifies the specific probes run at that time, not every optional connector or answer quality."`` | — |
| [SRC-B335630551-L000042](../../README.md#L42) | 42 | `""` | — |
| [SRC-B335630551-L000043](../../README.md#L43) | 43 | `"This is a tool-using research agent built around existing language models, not a foundation model trained from scratch. The role-specific defaults aim for more consistent behaviour than using a router that selects a different free model at random on each call. Exact availability and response quality still depend on OpenRouter/provider conditions. **Privacy warning:** the user's question, conversation context and selected web excerpts are sent to the configured external language-model provider for planning/synthesis/review. OpenRouter's NVIDIA Nemotron free endpoint states that session data may be logged for security and product improvement; do not send passwords, API keys, private information or personal/confidential customer data through the free endpoint. See the [NVIDIA Nemotron free-endpoint privacy notice](https://openrouter.ai/nvidia/nemotron-3-ultra-550b-a55b:free). Its language-model planner decides how to search, but query count, URLs and result shapes are validated by deterministic code. Cross-engine agreement improves discovery and ranking but is not independent fact verification. Public social pages that require login, blocked pages and private profiles are not fetched; social search cannot promise complete coverage of any platform. Direct official-platform access varies: Reddit API access requires approved app credentials and is subject to Reddit's terms; Facebook Pages reads require a valid token, page identifiers and correct permissions; Instagram hashtag search requires a professional Instagram account token and the specific supported permissions; X API access requires an authorized bearer token and suitable access; YouTube direct API search requires a Google API key. These APIs do not grant universal access to all content, accounts or comments. Review each platform's terms, quotas and permitted use before using the agent commercially. The agent never bypasses login, paywall or access controls and does not send messages or make automated contact with people."` | — |
| [SRC-B335630551-L000044](../../README.md#L44) | 44 | `""` | — |
| [SRC-B335630551-L000045](../../README.md#L45) | 45 | `""` | — |
| [SRC-B335630551-L000046](../../README.md#L46) | 46 | `"## Living repository index"` | — |
| [SRC-B335630551-L000047](../../README.md#L47) | 47 | `""` | — |
| [SRC-B335630551-L000048](../../README.md#L48) | 48 | `"**Current delivery gate (Arabic):** [OMARAI HANDOFF CHECKLIST](docs/OMARAI_HANDOFF_CHECKLIST_AR.md) — current release blockers, required evidence, and operator actions. The central [remediation register](docs/OMARAI_REMEDIATION_REGISTER_AR.md) remains the detailed issue history."` | — |
| [SRC-B335630551-L000049](../../README.md#L49) | 49 | `""` | — |
| [SRC-B335630551-L000050](../../README.md#L50) | 50 | `"Omarai maintains a categorized master index and a paginated, line-by-line source index:"` | — |
| [SRC-B335630551-L000051](../../README.md#L51) | 51 | `""` | — |
| [SRC-B335630551-L000052](../../README.md#L52) | 52 | ``"- [MASTER INDEX](docs/MASTER_INDEX.md): file inventory with stable file IDs, Python AST definitions, static frontend/configuration symbols, and explicitly marked TODO/FIXME/BUG/HACK/XXX/REVIEW/SECURITY/DEPRECATED/ISSUE/DEFECT/REGRESSION/RISK/GAP/ERROR/WARNING/PERF/PRIVACY/DATA_LOSS/ACCESSIBILITY entries. Each review marker has an `FND-...` code and a link to the exact source line."`` | — |
| [SRC-B335630551-L000053](../../README.md#L53) | 53 | `"- [SOURCE LINES INDEX](docs/SOURCE_LINES_INDEX.md): search-friendly directory of files, page links, per-file line counts, and links to each source line."` | — |
| [SRC-B335630551-L000054](../../README.md#L54) | 54 | `"- [INDEX COVERAGE AUDIT](docs/INDEX_COVERAGE_AUDIT.md): generated evidence of line-count consistency, metadata-only files, excluded path names and their reasons, and the exact scope of any “100%” coverage statement."` | — |
| [SRC-B335630551-L000055](../../README.md#L55) | 55 | ``"- [Source line pages](docs/source_index/): small generated pages containing every logical line from eligible readable text files. Each line has a `SRC-<FILEHASH>-L000001` code, exact JSON-escaped text, and a link back to the source file at the matching line. Pages are capped at 800 line records to remain navigable on mobile and in GitHub's web view."`` | — |
| [SRC-B335630551-L000056](../../README.md#L56) | 56 | `"- [Local source search](docs/search_code.py): offline text/regex search with file, line, nearby context, and GitHub line links. It excludes common secret/configuration files, databases, key files, symlinks, and runtime directories; it does not detect every secret or replace a security audit."` | — |
| [SRC-B335630551-L000057](../../README.md#L57) | 57 | `""` | — |
| [SRC-B335630551-L000058](../../README.md#L58) | 58 | ``"Example: `python docs/search_code.py \"resolve_followup_query\" --ext py --context 2`."`` | — |
| [SRC-B335630551-L000059](../../README.md#L59) | 59 | `""` | — |
| [SRC-B335630551-L000060](../../README.md#L60) | 60 | ``"The generator now refuses to publish indexes if any eligible file has missing, duplicated, or misnumbered source-line records. It still cannot infer every unmarked logical/programming defect; known issues should be recorded explicitly with a supported marker (for example, `# BUG: explain the defect`) so the generated `FND-...` register can point to the corresponding `SRC-...` line."`` | — |
| [SRC-B335630551-L000061](../../README.md#L61) | 61 | `""` | — |
| [SRC-B335630551-L000062](../../README.md#L62) | 62 | `"Regenerate and verify the indexes locally:"` | — |
| [SRC-B335630551-L000063](../../README.md#L63) | 63 | `""` | — |
| [SRC-B335630551-L000064](../../README.md#L64) | 64 | ````"```bash"```` | — |
| [SRC-B335630551-L000065](../../README.md#L65) | 65 | `"python docs/generate_index.py"` | — |
| [SRC-B335630551-L000066](../../README.md#L66) | 66 | `"python docs/generate_index.py --check"` | — |
| [SRC-B335630551-L000067](../../README.md#L67) | 67 | ````"```"```` | — |
| [SRC-B335630551-L000068](../../README.md#L68) | 68 | `""` | — |
| [SRC-B335630551-L000069](../../README.md#L69) | 69 | ``"GitHub Actions validates the generator on Python 3.11 and 3.12. The publishing workflow runs on pushes to `main` and the `feat/**`, `fix/**`, and `feature/**` branches. It regenerates and commits all indexes and generated pages only when output changes; obsolete generated pages are removed, while generated-index-only commits are ignored to avoid loops. Documentation-only and repository-hygiene branches are still tested with indexes regenerated in the isolated test workspace, but do not carry a large generated-page diff solely because documentation lines moved; after merge, the publisher refreshes the committed indexes on `main`. If direct publication to `main` is rejected, it opens a pull request instead of force-updating a branch or auto-merging."`` | — |
| [SRC-B335630551-L000070](../../README.md#L70) | 70 | `""` | — |
| [SRC-B335630551-L000071](../../README.md#L71) | 71 | ``"When a known code issue is found, add a source comment using one supported marker name (TODO, FIXME, BUG, HACK, XXX, REVIEW, SECURITY, DEPRECATED, ISSUE, DEFECT, REGRESSION, RISK, GAP, ERROR, WARNING, PERF, PRIVACY, DATA_LOSS, or ACCESSIBILITY), followed by a colon and a concise description. The index assigns an `FND-...` code and links it to the exact `SRC-...` source-line record; removing or editing that source annotation updates the generated register on the next index run. Coverage includes every logical line in eligible readable text files up to 2 MiB. Known local secrets, runtime databases, dependency/build directories, binary/unreadable files and oversized files are excluded from line-level indexing by design but listed by metadata where eligible. Static review markers help track explicit findings; no source index can prove that every arbitrary logic bug has been detected or that all code is correct."`` | — |
| [SRC-B335630551-L000072](../../README.md#L72) | 72 | `""` | — |
| [SRC-B335630551-L000073](../../README.md#L73) | 73 | `"## Per-request resource budget"` | — |
| [SRC-B335630551-L000074](../../README.md#L74) | 74 | `""` | — |
| [SRC-B335630551-L000075](../../README.md#L75) | 75 | ``"Each `POST /api/agent` answer includes a `request_budget` object with elapsed and remaining time, reserved resource counts, and configured limits. The current defaults are a 90-second cooperative deadline, at most 8 search queries, 32 provider search calls, 8 model HTTP attempts, 8 page fetches, and up to 3 optional server-side search-tool calls per request. Operator limits may be lowered or raised only within hard caps: `OMARAI_REQUEST_BUDGET_SECONDS` (10–120), `OMARAI_REQUEST_MAX_SEARCH_QUERIES` (1–8), `OMARAI_REQUEST_MAX_SEARCH_CALLS` (1–40), `OMARAI_REQUEST_MAX_MODEL_CALLS` (1–12), `OMARAI_REQUEST_MAX_PAGE_FETCHES` (1–8), and `OMARAI_REQUEST_MAX_TOOL_CALLS` (0–3). Invalid numeric values fall back to the defaults; out-of-range values are clamped."`` | — |
| [SRC-B335630551-L000076](../../README.md#L76) | 76 | `""` | — |
| [SRC-B335630551-L000077](../../README.md#L77) | 77 | `"The deadline caps the timeout passed to outbound operations and prevents new work from being reserved after the deadline or a resource cap is exhausted. It is **cooperative, not hard cancellation**: a network call already in progress may overrun slightly while its client unwinds. Do not interpret this metadata as a load test, a throughput guarantee, or proof that any live provider is reachable. CI tests for budget logic are separate from live-provider validation."` | — |
| [SRC-B335630551-L000078](../../README.md#L78) | 78 | `""` | — |
| [SRC-B335630551-L000079](../../README.md#L79) | 79 | ``"The HTTP ingress caps active handler connections at 32 per process by default through `OMARAI_MAX_CONCURRENT_HTTP_CONNECTIONS` (bounded to 1–128). When all slots are occupied, excess sockets receive HTTP 503 with `Retry-After: 5` before a handler thread is created. The in-memory rate limiter also caps client buckets at 4,096 per process; new identities beyond that ceiling share a conservative overflow quota. Separately, expensive `/api/agent` and `/api/diagnostics` operations remain limited to at most 4 concurrent operations per process by default; configure `OMARAI_MAX_CONCURRENT_AGENT_REQUESTS` from 1 to 8. These are **process-local** controls, not distributed limits across workers or replicas, and they are not throughput/load-test claims."`` | — |
| [SRC-B335630551-L000080](../../README.md#L80) | 80 | `""` | — |
| [SRC-B335630551-L000081](../../README.md#L81) | 81 | `"## Experimental DeepSeek Search provider"` | — |
| [SRC-B335630551-L000082](../../README.md#L82) | 82 | `""` | — |
| [SRC-B335630551-L000083](../../README.md#L83) | 83 | `"Omarai can optionally compare results from DeepSeek's Search API when"` | — |
| [SRC-B335630551-L000084](../../README.md#L84) | 84 | ``"`DEEPSEEK_SEARCH_API_KEY` is configured in the host's secret settings. It is"`` | — |
| [SRC-B335630551-L000085](../../README.md#L85) | 85 | `"**disabled by default**; DuckDuckGo and Bing remain configured as before."` | — |
