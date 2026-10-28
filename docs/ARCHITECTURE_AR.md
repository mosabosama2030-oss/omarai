# عمارة RAG الوكيلي والذاكرة المنظمة في Omarai

## المبادئ الخمسة

1. **الاسترجاع كأداة (Retrieval-as-a-Tool)**
   حلقة: خطط → استرجع → لاحظ → قرر → تحقق → ألّف.
   التنفيذ: `RetrievalTool` + `AgenticRagOrchestrator`.

2. **ذاكرة منظمة Claim↔Evidence** (`MemoryBank`)
   - `ingest_sources`: تحويل نتائج البحث إلى Evidence بمعرّف ثابت
   - `bind_claim` / `bind_answer`: ربط كل جملة ادعاء بأدلة عبر تداخل توكنات
   - الحالات: `supported` (≥0.45) · `weak` (≥0.25) · `unsupported`
   - `format_claim_with_citations`: إضافة `[المصدر N]`
   - `render_supported_answer`: إسقاط غير المدعوم
   - `graph`: عقد ادعاءات/أدلة + حواف
   - `to_claim_evidence_ledger_shape`: توافق مع `claim_evidence` على main

3. **وكلاء متخصصون**
   QueryReformulator · IterativeRetriever · HallucinationGuard · FinalComposer

4. **الاستشهاد جزء من التوليد** — إلزامي عند وجود دعم

5. **تقييم مستمر** — retrieval_relevance / faithfulness / aspect_coverage / writing_quality_proxy

## حدود الأمانة

- الدعم **لفظي/معجمي** وليس entailment دلاليًا.
- `retrieve_fn` يفرض SSRF/URL/الصلة في WebAgent.
- الضبط الدقيق (SFT/RL) لاحقًا وليس بديلًا.

## الربط مع WebAgent

```python
from agents.agentic_rag_integration import web_agent_post_answer_hook
result.update(web_agent_post_answer_hook(question, answer, sources, aspects=aspects))
```

أو: `python3 scripts/apply_memory_bank_web_agent_hooks.py`
