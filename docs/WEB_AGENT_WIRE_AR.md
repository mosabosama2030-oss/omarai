# ربط MemoryBank و Agentic RAG مع WebAgent

## بعد التوليد (موصى به)

```python
from agents.agentic_rag_integration import web_agent_post_answer_hook

aspects = list((search_report or {}).get("aspects") or [])
enrichment = web_agent_post_answer_hook(question, answer, sources, aspects=aspects)
result.update(enrichment)
```

## سكربت آلي

```bash
python3 scripts/apply_memory_bank_web_agent_hooks.py
```

## المسار الوكيلي الكامل

```python
from agents.agentic_rag_integration import run_agentic_rag
payload = run_agentic_rag(question, retrieve_fn=self._search_web, history=history)
```

## لا تفعل

- لا تخفض عتبة الصلة 0.20
- لا تفسّر support_ratio كاحتمال صدق
- لا تتجاوز مسار SSRF
