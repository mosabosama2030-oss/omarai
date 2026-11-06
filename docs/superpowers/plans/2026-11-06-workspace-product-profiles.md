# Workspace Product Profiles Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox syntax.

**Goal:** Make the existing "ملف المنتج والعرض" workspace module a real tenant-scoped create/list/update experience.

**Architecture:** Reuse validated domain models in `agents/sales_domain.py`; persist their canonical JSON in a tenant-scoped SQLite table through `LeadStore`; expose authenticated REST-style handlers in the existing HTTP API; connect the current RTL workspace with no new frontend framework.

**Tech Stack:** Python 3.12, stdlib `sqlite3` and `http.server`, existing HTML/CSS/JavaScript, pytest, Ruff.

**Spec:** `docs/superpowers/specs/2026-11-06-workspace-product-profiles-design.md`

## Global Constraints
- Derive tenant ownership from the authenticated principal, never from request data.
- Viewer is read-only; server enforces this for writes.
- No secrets in browser, logs, or repository.
- No external provider calls, paid API use, database reset, or destructive migration.
- Preserve existing API and lead/session behavior.
- Leave merge and deployment to the Human Director.

## Review Focus
- Cross-tenant read/update by guessing a product ID must return no data.
- Empty, non-array, oversized, or unknown profile fields must be rejected.
- Product facts with invalid origin/evidence combinations must be rejected.
- Viewer access must remain read-only even when requests are sent directly.
- Existing workspace research navigation must point to `/agent`, not the root route.

---

### Task 1: Persist product profiles

**Files:**
- Modify: `agents/omarai.py`
- Test: `tests/test_sales_profiles.py`

**Interfaces:**
- `LeadStore.save_product_profile(profile, market, *, tenant_id, profile_id=None) -> dict | None`
- `LeadStore.get_product_profile(profile_id, *, tenant_id) -> dict | None`
- `LeadStore.list_product_profiles(*, tenant_id, limit=100) -> list[dict]`

- [x] Write tests for tenant scoping, update, persistence, and inactive tenant rejection.
- [ ] Correct lint in the API test first and confirm the test branch's expected RED failure.
- [ ] Add non-destructive `product_profiles` table and tenant/update index in `_initialize_schema`.
- [ ] Implement the three storage methods using `ProductProfile.to_dict()` and `MarketProfile.to_dict()`.
- [ ] Run storage tests and verify persistence by reopening the same DB file.

### Task 2: Add the authenticated product API

**Files:**
- Modify: `api/omarai.py`
- Test: `tests/test_multitenant_api.py`

**Interfaces:**
- `GET /api/products`
- `POST /api/products`
- `POST /api/products/{profile_id}`

- [x] Specify API authentication, tenant isolation, viewer, malformed-input tests.
- [ ] Parse only exact domain fields and construct `ProductFact`, `ProductProfile`, and `MarketProfile`.
- [ ] Add list/create/update handlers, using only principal tenant ID.
- [ ] Return 404 for a profile outside the authenticated tenant and 403 for viewer writes.
- [ ] Run API integration tests, including unauthenticated and cross-tenant cases.

### Task 3: Connect the RTL workspace

**Files:**
- Modify: `web/workspace.html`
- Test: `tests/test_dashboard_security.py` and relevant API/UI tests.

- [ ] Enable only the product-profile menu item after its API exists.
- [ ] Add create/list/edit UI backed by `/api/products`.
- [ ] Display load, empty, validation, save, and API-error states.
- [ ] Keep discovery and other unsupported units disabled.
- [ ] Correct placeholder research navigation to `/agent`.
- [ ] Add tests asserting UI routes and API integration hooks without exposing secrets or using browser storage.

### Task 4: Review and verify

- [ ] Update `docs/IMPLEMENTATION_SCOPE.md` and requirements register with evidence-backed state.
- [ ] Review full diff, migrations, tenant boundaries, and CSP implications.
- [ ] Run `pytest -q` and `ruff check agents api cli docs tests`.
- [ ] Verify Docker build and GitHub Actions on final branch SHA.
- [ ] Create a PR for Human Director review; do not merge or deploy.

## Known follow-on work (not in this plan)
Discovery-run orchestration, connecting buyer-query planning to existing search, page reading, demand classification/evidence persistence, connector status, opportunities, company records, and audit history require separate plans and their own acceptance criteria. This feature does not make them active.
