# Unified Hybrid Research Pipeline Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

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
