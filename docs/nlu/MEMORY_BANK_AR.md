# بنك الذاكرة المنظمة (Memory Bank)

## الهدف
ربط كل ادعاء في الإجابة بدليل مسترجع بمعرّف ثابت، ومنع الطلاقة بلا سند.

## الكيانات
- **Evidence**: url, title, snippet, evidence_id, source_index, readable
- **Claim**: text, claim_id, evidence_ids, support_score, status, aspect

## العمليات
1. `ingest_sources(sources)` — تعبئة الأدلة من نتائج البحث
2. `bind_claim(text)` / `bind_answer(answer)` — ربط جمل الإجابة
3. `format_claim_with_citations` — إضافة `[المصدر N]`
4. `render_supported_answer` — إعادة بناء النص بعد إسقاط unsupported
5. `graph()` — عقد وحواف للتشخيص
6. `to_claim_evidence_ledger_shape()` — شكل متوافق مع `claim_evidence.py` على main

## التصنيف
| score | status |
|------|--------|
| ≥ 0.45 | supported |
| ≥ 0.25 | weak |
| < 0.25 | unsupported |

## الأمانة
التطابق لفظي/معجمي فقط. ليس entailment دلاليًا ولا درجة ثقة احتمالية.

## الربط مع WebAgent
```python
from agents.agentic_rag_integration import web_agent_post_answer_hook
result.update(web_agent_post_answer_hook(question, answer, sources, aspects=aspects))
```
