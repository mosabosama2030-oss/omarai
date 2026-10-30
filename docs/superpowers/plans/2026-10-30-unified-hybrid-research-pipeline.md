# Unified Hybrid Research Pipeline Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** Route Omarai's context, intent, task interpretation, aspect extraction, query planning, and evidence matching through one bounded, auditable orchestration function.

**Architecture:** Add `agents/research_pipeline.py` as a coordinator over existing modules. Reuse the same coordinator from `research.py` and `web_agent.py`; keep the optional semantic scorer injected and disabled unless explicitly supplied, while retaining current source/claim guardrails.

**Tech Stack:** Python 3.11+, existing stdlib and Omarai modules, pytest, Ruff.

**Spec:** `docs/superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md`

## Global Constraints
- No new runtime dependencies.
- Maximum 8 aspects and 8 planned queries.
- No additional LLM/provider calls or paid services.
- No change to API, database, secrets, hosting, or deployment.
- Lexical and semantic relevance are candidate-ranking signals, never proof of claim truth.
- Preserve existing request budgets, source guardrails, citation validation, and clarification behavior.

## Review Focus
- Ambiguous follow-up without an anchor must remain CLARIFY and produce no search queries.
- A chained follow-up must preserve the latest substantive topic without reviving stale topics.
- Arabic compound questions with multiple criteria must keep each explicit aspect within the query cap.
- Empty/malformed sources and malformed optional semantic scores must fail closed without exceptions.
- Missing semantic scorer must be explicitly marked unassessed, not as a successful semantic match.

---

### Task 1: Add the unified orchestration contract

**Files:**
- Create: `agents/research_pipeline.py`
- Test: `tests/test_research_pipeline.py`

**Interfaces:**
- `build_research_pipeline(question, plan=None, *, history=None, mode="auto", intent_route="", dialogue_context=None, sources=None, compact_fn=None, semantic_matcher=None) -> dict[str, Any]`
- Returns bounded `contextual_question`, `intent`, `task_spec`, `aspects`, `query_strategy_matrix`, `queries`, `evidence_ledger`, and stage-status diagnostics.

- [ ] Write tests for explicit aspect preservation, clarification without a referent, evidence-ledger semantics, and safe optional-scorer fallback.
- [ ] Run targeted tests and observe failure before implementation.
- [ ] Implement the coordinator using existing modules only.
- [ ] Run targeted tests and Ruff.

### Task 2: Integrate plan construction

**Files:**
- Modify: `agents/research.py::_attach_task_understanding`
- Modify: `agents/web_agent.py` planning block around TaskSpec and query strategy construction.
- Test: `tests/test_research.py`, `tests/test_web_agent.py`, `tests/test_research_pipeline.py`

- [ ] Add regression coverage proving both fallback and WebAgent plans use the shared pipeline.
- [ ] Replace duplicated TaskSpec/matrix assembly with the coordinator.
- [ ] Preserve the existing query budget and mode-specific prioritization.
- [ ] Run targeted integration tests.

### Task 3: Integrate post-retrieval matching diagnostics

**Files:**
- Modify: `agents/web_agent.py` after source collection and before answer generation.
- Test: `tests/test_research_pipeline.py`, `tests/test_web_agent.py`

- [ ] Add a test showing each explicit aspect gets a lexical evidence ledger entry and missing aspects remain visible.
- [ ] Attach pipeline evidence diagnostics to the existing research report without changing source acceptance or claim-verification rules.
- [ ] Ensure semantic status remains `not_configured` unless an injected scorer returns validated bounded scores.
- [ ] Run the full relevant test set.

### Task 4: Verify and document

**Files:**
- Update: `docs/OMARAI_REMEDIATION_REGISTER_AR.md` only if its current structure supports a non-duplicative entry.
- Update: this design/plan with actual evidence.

- [ ] Run CI on the final PR head.
- [ ] Inspect the complete PR diff and workflow results.
- [ ] Record untested hosted behavior as NOT_RUN.
- [ ] Leave PR open and unmerged for Human Director review.


## تنفيذ موثق — 2026-10-30

- **RED:** GitHub Actions run [41055101051](https://github.com/mosabosama2030-oss/omarai/actions/runs/41055101051) فشل أثناء جمع الاختبارات بسبب غياب `agents.research_pipeline` قبل تنفيذ الوحدة، كما هو متوقع من اختبار العقد الأولي.
- **تصحيح أثناء التنفيذ:** ظهر Ruff أن `build_task_spec` و`build_query_strategy_matrix` ما زالا مستخدمين في مسارات أخرى داخل `web_agent.py`؛ أُعيد الاحتفاظ بالاستيراد هناك، وحُذفت الاستيرادات غير المستخدمة من `research.py`. فشل آخر في الاختبار كشف أن اختبار مهلة المقيّم لم يستخرج محاور متعددة، ثم صُحح الاختبار ليستخدم سؤالًا مركبًا. وبعدها صحح عدد الاستثناءات المتوقع ليتناسب مع عدد المحاور.
- **GREEN / CI:** run [41056403423](https://github.com/mosabosama2030-oss/omarai/actions/runs/41056403423) على code SHA `c68595cb0f38b3d1d64add600eb0172209980dea` نجح:
  - Python 3.11: **623 passed**.
  - Python 3.12: **623 passed**.
  - Ruff: All checks passed.
  - Generated-index verification: success.
  - Production container build + protected API smoke: success.
- رأس PR الحالي بعد أتمتة الفهرسة: `c10dcf63420b57365d10fdeda0a5be7aaaa4b84c`. المقارنة من code-tested SHA تُظهر تغييرات فهرسة مولدة فقط، دون تغييرات runtime أو tests.
- **الحد المتبقي:** لا يوجد semantic scorer موصول افتراضيًا في WebAgent؛ يسجل المسار `not_configured`. واجهة المقيّم الاختيارية موجودة ومختبرة للفشل، لكن لا ندّعي مطابقة دلالية حية أو تحسينًا مقاسًا. لا hosted acceptance أو بحث حي أو استدعاءات مدفوعة.
- **الحالة:** PR #132 Draft/Open/Not merged؛ لا دمج ولا نشر.


### مراجعة نهائية بعد إعادة بناء TaskSpec — 2026-10-30
- أظهرت مراجعة الكود أن إعادة استخدام TaskSpec المسبق بعد توليد الخطة قد تُسقط `planner_depth` و`planner_freshness`. أُلغي هذا الاختصار، وأُبقي بناء TaskSpec النهائي داخل المنسق بعد توفر بيانات الخطة، مع بقاء preflight يمر عبر المنسق نفسه.
- اختبار انحدار جديد يثبت حفظ بيانات عمق وحداثة خطة البحث.
- **التحقق النهائي للكود:** run [41056744662](https://github.com/mosabosama2030-oss/omarai/actions/runs/41056744662) على SHA `b72168a6fbf360f5fc088fe125a4ad9623fdb958`:
  - Python 3.11: **623 passed**.
  - Python 3.12: **623 passed**.
  - Ruff: All checks passed.
  - Docker build وProtected API Smoke: success.
- PR head بعد تحديث الفهارس والوثائق: `ce7e32f11b0612c3519f89f670eee0a143e94fc8`. التغييرات بعد SHA المختبر هي ملفات الفهرسة المولدة فقط؛ لا تغييرات كود أو اختبارات بعد التشغيل الناجح.


### بوابة التوضيح الإلزامي — 2026-10-30
- أُضيف منع لتخطيط/تنفيذ الاستعلامات عندما يقرر TaskSpec أن مدخلًا إلزاميًا مفقود، حتى إذا وصل مسار بحث upstream مثل `WEB_SIMPLE`.
- اختبار `هات الموقع الرسمي` دون اسم جهة يثبت أن الاستيضاح يوقف الاستعلامات.
- **آخر تحقق للكود:** run [41057068443](https://github.com/mosabosama2030-oss/omarai/actions/runs/41057068443) على SHA `6ebcb720a6ef1166fdd2ef672a00c4e01ba4cfda`:
  - Python 3.11: **624 passed**.
  - Python 3.12: **624 passed**.
  - Ruff: All checks passed.
  - Docker build + Protected API Smoke: success.
- رأس PR بعد أتمتة الفهرسة: `51c459d329239b6386d2f79529a046e2759d5dad`; الفارق عن SHA المختبر يقتصر على ملفات الفهرسة المولدة.
