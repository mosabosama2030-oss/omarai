#!/usr/bin/env python3
"""Apply MemoryBank / agentic RAG post-answer hook into agents/web_agent.py.

Run from repo root:
  python3 scripts/apply_memory_bank_web_agent_hooks.py
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "agents" / "web_agent.py"

IMPORT_BLOCK = """from agents.agentic_rag_integration import web_agent_post_answer_hook
"""

HOOK_SNIPPET = """
        # Structured claim–evidence memory (agentic RAG) — lexical support only
        try:
            aspects = list((result.get("search_report") or {}).get("aspects") or [])
            enrichment = web_agent_post_answer_hook(
                question if "question" in dir() else str(result.get("question") or ""),
                str(result.get("answer") or ""),
                list(result.get("sources") or []),
                aspects=aspects,
            )
            result.update(enrichment)
            if isinstance(result.get("search_report"), dict):
                result["search_report"]["agentic_rag"] = enrichment.get("agentic_rag")
        except (RuntimeError, ValueError, TypeError, OSError, KeyError):
            result.setdefault("agentic_rag", {"enabled": False, "error": "hook_failed"})
"""


def main() -> None:
    text = TARGET.read_text(encoding="utf-8")
    if "web_agent_post_answer_hook" in text and "agentic_rag" in text:
        print("hooks already present")
        return
    if "from agents.agentic_rag_integration import web_agent_post_answer_hook" not in text:
        if "from agents.claim_evidence import" in text:
            text = text.replace(
                "from agents.claim_evidence import",
                IMPORT_BLOCK + "from agents.claim_evidence import",
                1,
            )
        elif "from agents.research import" in text:
            text = text.replace(
                "from agents.research import",
                IMPORT_BLOCK + "from agents.research import",
                1,
            )
        else:
            text = IMPORT_BLOCK + text

    marker = 'result["claim_evidence_status"] = "sentence_level_trace_only"'
    if marker in text and "web_agent_post_answer_hook(" not in text:
        text = text.replace(marker, marker + "\n" + HOOK_SNIPPET, 1)
    elif "web_agent_post_answer_hook(" not in text:
        text += (
            "\n# NOTE: call web_agent_post_answer_hook(question, answer, sources) "
            "before returning result\n"
        )
        print("warning: marker not found; import added only")
    TARGET.write_text(text, encoding="utf-8")
    print(f"patched {TARGET}")


if __name__ == "__main__":
    main()
