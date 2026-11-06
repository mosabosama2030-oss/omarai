# Workspace Product Profile & Demand Discovery Implementation Plan

> **For agentic workers:** Use the repository's TDD workflow task-by-task. Steps use checkbox syntax.

**Goal:** Connect the new Arabic RTL workspace to a tenant-scoped product profile, real buyer-intent discovery, persisted discovery evidence, and human-reviewed signal saving.

**Architecture:** Add small tenant-scoped SQLite records and protected endpoints, reuse the existing `sales_domain` and `WebAgent` pipeline, and expose the workflow through the existing workspace. Do not duplicate search logic or enable paid/optional providers by default.

**Tech Stack:** Python 3.12, stdlib HTTP server, SQLite, static HTML/JavaScript, pytest, GitHub Actions.

**Spec:** `docs/superpowers/specs/2026-11-06-workspace-demand-discovery-design.md` and `docs/OMARAI_SALES_INTELLIGENCE_ARCHITECTURE_AR.md`.

## Global Constraints
- Work only on `feat/workspace-demand-discovery-2026-11-06`, based on current main SHA `a297abd271d48f459effad083a9f424a1499cd39`.
- Never trust a client-supplied `tenant_id`; use the authenticated principal.
- Viewer is read-only and cannot run discovery or write product data.
- Paid/optional search providers must stay disabled by default in this workflow.
- Save a source as a demand signal only when the server-side stored run labels it `public_demand_signal`.
- Preserve publication date, event date, and observation time as distinct/unknown where not supplied.
- No secrets, hosting configuration changes, production deployment, or PR merge.
- Do not activate UI modules without real API contracts.

## Review Focus
- Cross-tenant product-profile/run access using guessed IDs.
- Viewer attempts to create profiles, discover, or save a signal.
- Malformed arrays, oversized product text, invalid locale, empty query plan, and duplicate product profiles.
- Optional connectors with configured API keys but no explicit per-run owner approval.
- Discovery results containing related listings, negative intent, or no qualified buyer signal.
- Browser attempting to save an unrelated result or alter a server-side qualification label.

---

### Task 1: Pin storage and API contracts with failing tests

**Files:**
- Modify: `tests/test_api.py`
- Modify: `tests/test_sales_domain.py`
- Create: `tests/test_workspace_discovery.py`

**Interfaces:**
- Product profile data uses `ProductProfile` plus `MarketProfile` serialization.
- API response records are tenant-scoped and never accept a tenant identifier from the browser.
- Save endpoint accepts a stored `run_id` and source index, not a client-supplied source payload.

- [x] Add tests for tenant-scoped create/list/get of product profiles.
- [x] Add tests for discovery run creation/list/get and tenant isolation.
- [x] Add tests proving only a stored source marked `public_demand_signal` can be saved.
- [x] Add tests for viewer denial, unauthenticated denial in public mode, invalid profile values, and duplicate profile behavior.
- [x] Run focused tests to verify expected RED (missing contracts).

### Task 2: Add tenant-scoped storage

**Files:**
- Modify: `agents/omarai.py`
- Modify: `tests/test_workspace_discovery.py`

**Interfaces:**
- `LeadStore.save_product_profile(profile: dict, *, tenant_id: str) -> dict`
- `LeadStore.list_product_profiles(*, tenant_id: str) -> list[dict]`
- `LeadStore.get_product_profile(profile_id: str, *, tenant_id: str) -> dict | None`
- `LeadStore.save_discovery_run(profile_id: str, run: dict, *, tenant_id: str) -> dict`
- `LeadStore.list_discovery_runs(*, tenant_id: str, limit: int = 50) -> list[dict]`
- `LeadStore.get_discovery_run(run_id: str, *, tenant_id: str) -> dict | None`
- `LeadStore.save_discovery_signal(run_id: str, source_index: int, *, tenant_id: str) -> tuple[dict, bool] | None`

- [x] Add `product_profiles` table with tenant-scoped uniqueness and index.
- [x] Add `discovery_runs` table with tenant-scoped profile foreign key and index.
- [x] Store only bounded public response fields; never model prompts or secrets.
- [x] Save leads only by loading the source from the stored run and verifying its server-side qualification label.
- [x] Run storage tests and existing LeadStore tests.

### Task 3: Connect structured buyer discovery to WebAgent

**Files:**
- Modify: `agents/web_agent.py`
- Create/modify: `tests/test_workspace_discovery.py`

**Interfaces:**
- Extend `WebAgent.answer(..., buyer_queries: list[str] | None = None)`.
- Extend internal `_answer_with_budget(..., buyer_queries: list[str] | None = None)`.
- Preserve existing callers when `buyer_queries` is omitted.
- Add per-instance `allow_optional_providers` control, defaulting to existing behavior for legacy routes.

- [x] Force the lead-generation route only when structured buyer queries are supplied by the new discovery endpoint.
- [x] Validate and cap buyer query count/length (1–8 queries, max 500 characters each).
- [x] Prefer structured queries over prose-derived `_lead_generation_queries`.
- [x] Gate DeepSeek, Brave, Tavily, and optional social APIs when the per-instance control is false.
- [x] Keep DDG/Bing/Google News and public no-key social retrieval under existing bounded controls.
- [x] Add tests that structured product/location queries reach the lead-generation path and optional providers are not invoked by default.

### Task 4: Implement protected API contracts

**Files:**
- Modify: `api/omarai.py`
- Modify: `tests/test_api.py`

**Interfaces:**
- `GET /api/product-profiles`
- `POST /api/product-profiles`
- `GET /api/discoveries`
- `GET /api/discoveries/{run_id}`
- `POST /api/discoveries`
- `POST /api/discoveries/{run_id}/signals/{source_index}/save`

- [x] Validate request JSON arrays and bounded field sizes through `ProductProfile` and `MarketProfile`.
- [x] Derive all tenant scope from `self._authenticated_principal`.
- [x] Require a non-viewer role to create profiles or run discovery.
- [x] Require owner role plus explicit `allow_optional_providers=true` to enable optional providers.
- [x] Build a product-anchored prompt and queries through `build_buyer_queries`.
- [x] Persist the bounded discovery response and return its run ID.
- [x] Return 404 for run/profile IDs outside the current tenant.
- [x] Route save requests through `LeadStore.save_discovery_signal`; never trust browser-provided source qualification.
- [x] Run API integration/security tests.

### Task 5: Connect the RTL workspace

**Files:**
- Modify: `web/workspace.html`
- Modify: `tests/test_dashboard_security.py`
- Modify: `tests/test_api.py` (if static-route contract coverage is located here)

**Interfaces:**
- Activate `offer` (Product Profile) and `campaign` (Demand Discovery) only.
- Read product profiles and discovery runs from their authenticated APIs.
- Save selected qualified signals using the stored discovery run ID and source index.

- [x] Add product profile editor with aliases, use cases, problems solved, locations, industries, customer types, decision roles, and exclusions.
- [x] Add discovery screen to choose a saved profile, run search, show prior run history, and inspect evidence.
- [x] Display qualified buyer signals separately from related-but-unqualified results.
- [x] Show evidence phrase, evidence basis (snippet/page text/title), source link, and publication-date unknown states.
- [x] Add explicit unchecked opt-in for optional providers; owner-only on the server with cost/quota disclosure.
- [x] Add save action only for server-qualified public demand signals; then refresh leads and pipeline.
- [x] Fix the placeholder's general research navigation to `/agent`.
- [x] Keep all other unimplemented modules visibly unavailable.
- [x] Run workspace static/security tests.

### Task 6: Documentation, CI, review, and handoff

**Files:**
- Modify: `docs/IMPLEMENTATION_SCOPE.md`
- Modify: `README.md` only if current product capabilities description needs updating.
- Modify: `docs/OMARAI_REQUIREMENTS_REGISTER.md` for material requirement status/evidence, if exact owners can be identified without rewriting the historical baseline.

- [ ] Verify `pytest -q`, `ruff check .`, Docker build, and container/API smoke through GitHub Actions.
- [ ] Inspect the entire branch diff and confirm no secret or unrelated generated-index changes.
- [ ] Record unrun hosted tests as NOT_RUN.
- [ ] Open a PR against `main` and leave merge and SnapDeploy deployment to the Human Director.

## Expected delivery boundary

This plan enables a first real vertical slice: saved product/market profile → buyer-intent search → persisted evidence results → human-reviewed qualified signal → existing leads pipeline. It does **not** claim that company profiles, market analytics, scheduled monitoring, outbound messaging, audit center, or the remaining disabled modules are complete.
