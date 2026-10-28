# عمارة RAG الوكيلي في Omarai

## المبادئ الخمسة

1. **الاسترجاع كأداة (Retrieval-as-a-Tool)**
   ليس خط أنابيب ثابتًا. الحلقة: خطط → نفّذ استرجاعًا → لاحظ → قرر → تحقق → ألّف.
   التنفيذ: `RetrievalTool` + `AgenticRagOrchestrator`.

2. **ذاكرة منظمة Claim↔Evidence**
   كل ادعاء يُربَط بمعرّفات أدلة مستقرة. الطلاقة مسموحة فقط مع روابط دعم.
   التنفيذ: `MemoryBank` (مع توافق مفاهيمي مع `claim_evidence.py` على main).

3. **وكلاء متخصصون**
   - `QueryReformulator` — تفكيك محاور واستعلامات
   - `IterativeRetriever` — بحث متعدد القفزات
   - `HallucinationGuard` — كشف ادعاءات بلا دعم
   - `FinalComposer` — إجابة مع استشهادات أو امتناع

4. **الاستشهاد جزء من التوليد**
   `format_claim_with_citations` يضيف `[المصدر N]` عند وجود دعم.

5. **تقييم مستمر**
   `eval_rag_metrics`: retrieval_relevance، faithfulness، aspect_coverage، writing_quality_proxy.

## حدود الأمانة

- الدعم **لفظي/معجمي** وليس entailment دلاليًا.
- الاسترجاع يمر عبر `retrieve_fn` الذي يفرض SSRF/URL/الصلة في WebAgent.
- الضبط الدقيق (SFT/RL) **لاحقًا** — ليس بديلًا عن هذه الطبقة.

## مسار الدمج في WebAgent

بعد جمع `sources` وقبل إرجاع الرد:

```python
from agents.agentic_rag_integration import web_agent_post_answer_hook
extra = web_agent_post_answer_hook(question, answer, sources, aspects=aspects)
result.update(extra)
```
