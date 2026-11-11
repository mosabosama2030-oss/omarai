# Omarai UI Recovery and Request Timeout Implementation Plan

> **For agentic workers:** Use the approved native execution path in this session. Steps use checkbox syntax for tracking.

**Goal:** Add bounded client-side request waiting and make workspace save/refresh failures independently visible.

**Architecture:** Keep the existing static HTML/JavaScript architecture. Extend the shared workspace API wrapper with an optional AbortSignal, apply the same bounded client deadline to both chat surfaces, and isolate secondary refresh failures from successful writes.

**Tech Stack:** Existing HTML, browser Fetch API, AbortController, Python pytest contract tests.

**Spec:** `docs/superpowers/specs/2026-11-11-omarai-ui-recovery-timeout.md`

## Global Constraints
- Client deadline: 135 seconds.
- Client abort does not claim server cancellation.
- Preserve existing auth-session version guards and duplicate-submit guards.
- No new dependencies, credentials, paid provider calls, database changes, merge, or deploy.

## Review Focus
- Timeout versus ordinary network error must produce distinct, accurate status.
- A late response after logout/session replacement must not mutate the new session.
- A second submit while the first request is active must remain blocked.
- A successful save followed by failed refresh must not be reported as a failed save.
- Failed refresh must preserve the last successful data and restore the refresh control.

---

### Task 1: Add failing UI contract tests

**Files:**
- Create: `tests/test_workspace_ui_regressions.py`
- Test: extracted application functions from `web/workspace.html` and `web/agent.html`

- [ ] Add tests for signal forwarding, workspace-chat timeout, legacy-agent timeout, duplicate-submit guard, signal inbox refresh recovery, and successful-save/failed-refresh distinctions.
- [ ] Run the full CI test workflow and confirm the new assertions fail on the current implementation for the expected missing behaviors.

### Task 2: Implement request deadlines

**Files:**
- Modify: `web/workspace.html`
- Modify: `web/agent.html`

- [ ] Forward `opts.signal` from the workspace API wrapper to Fetch.
- [ ] Add a 135-second AbortController deadline to `sendChat()` and `ask()`.
- [ ] Clear timeout handles in `finally`; restore controls and preserve existing session guards.
- [ ] Distinguish timeout from network failure and state that the server may continue processing.

### Task 3: Make save and refresh outcomes independent

**Files:**
- Modify: `web/workspace.html`

- [ ] Catch signal-inbox refresh errors and restore the refresh button.
- [ ] Preserve successful manual-signal, product-profile, and discovery-signal writes when their subsequent list refresh fails.
- [ ] Keep the existing discovery-run partial-success behavior.

### Task 4: Link inline citations in workspace chat

**Files:**
- Modify: `web/workspace.html`
- Test: `tests/test_workspace_ui_regressions.py`

- [ ] Render `[المصدر N]` and `[source N]` markers as safe links to `sources[N-1]` only when the indexed source has a valid HTTP(S) URL.
- [ ] Keep invalid/out-of-range markers as plain text; never infer or shift source indexes.

### Task 5: Verify

- [ ] Run targeted UI contract tests.
- [ ] Run full pytest and Ruff on Python 3.11 and 3.12 through GitHub Actions.
- [ ] Report hosted runtime, browser-level behavior, server cancellation, and volume durability as unverified unless separately tested.
