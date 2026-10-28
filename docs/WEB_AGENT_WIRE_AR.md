# ربط Agentic RAG مع WebAgent

## الحد الأدنى (بعد التوليد)

```python
from agents.agentic_rag_integration import web_agent_post_answer_hook

aspects = list((search_report or {}).get("aspects") or [])
enrichment = web_agent_post_answer_hook(
    question, answer, sources, aspects=aspects
)
result.update(enrichment)
```

## المسار الوكيلي الكامل

```python
from agents.agentic_rag_integration import run_agentic_rag

def retrieve_fn(q: str):
    return self._search_web(q)

payload = run_agentic_rag(question, retrieve_fn, history=history, max_hops=3)
```

## لا تفعل

- لا تستدعِ موصلات HTTP خارج مسار URL/SSRF المعتمد.
- لا تخفض عتبة الصلة 0.20.
- لا تعرض support_ratio كاحتمال صدق.
