# Make Omarai Sales Workspace the Default Home — Implementation Plan

**Goal:** Serve the approved Arabic RTL Neon Command sales workspace at `/` while preserving the research agent at `/agent` and the legacy lead page at `/leads`.

**Architecture:** Reuse the existing `web/workspace.html` and its existing authenticated APIs. Change only route selection and navigation/documentation; do not add backend capabilities, storage models, providers, or database migrations.

**Tech Stack:** Python 3.12 stdlib HTTP server, static HTML/CSS/JavaScript, pytest, existing GitHub Actions workflows.

**Spec:** Existing approved workspace in `web/workspace.html`, current sales-intelligence architecture, and repository instructions in `AGENTS.md`.

## Global Constraints
- Keep `/api/session`, `/api/leads`, `/api/analyze`, `/api/health`, and logout contracts unchanged.
- Keep `/workspace` as a backward-compatible alias.
- Preserve `/agent` as the general web-research interface and `/leads` as the legacy lead UI.
- Do not enable menu modules that do not have real server-side contracts.
- Keep same-origin HttpOnly browser sessions; never persist access tokens in localStorage or sessionStorage.
- No production deployment, secret changes, provider calls, database changes, or PR merge.

## Review Focus
- Root page must not silently remove access to the general research agent.
- Workspace's "وكيل البحث" navigation must not link back to the new root page.
- Existing workspace API/session and legacy lead paths must remain reachable.
- UI-only modules without backend contracts must remain explicitly unavailable.
- The root route must return Arabic RTL HTML and not a stale redirect.

---

### Task 1: Pin the intended route behavior

**Files:**
- Modify: `tests/test_api.py`

**Interfaces:**
- `GET /` and `GET /workspace` return the same sales-workspace HTML.
- `GET /agent` returns the existing research-agent HTML.
- `GET /leads` returns the existing legacy lead HTML.

- [ ] Rewrite the existing route integration test to assert the new home contract and preserve all three secondary paths.
- [ ] Commit the test first and inspect GitHub Actions for the expected RED result against the old route behavior.

### Task 2: Route the home page to the approved workspace

**Files:**
- Modify: `api/omarai.py`
- Modify: `web/workspace.html`

- [ ] Serve `/agent` from `agent.html` only.
- [ ] Serve both `/` and `/workspace` from `workspace.html`.
- [ ] Point the workspace's "وكيل البحث" link to `/agent`.
- [ ] Preserve all API and authorization behavior.

### Task 3: Align documentation and handoff

**Files:**
- Modify: `README.md`
- Modify: `docs/IMPLEMENTATION_SCOPE.md`

- [ ] Document the sales workspace as the default home and the research/legacy pages as retained routes.
- [ ] State clearly that modules without server-side contracts remain unavailable.

### Task 4: Verify

- [ ] Run `pytest tests/test_api.py tests/test_dashboard_security.py -q`.
- [ ] Run the full `pytest -q` suite and `ruff check .` where available.
- [ ] Confirm GitHub Actions on the final branch SHA.
- [ ] Review the full diff, create a PR against `main`, and leave merge/deploy to the Human Director.
