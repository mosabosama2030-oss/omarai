# Workspace Product Profiles — Design

**Status:** implementation scope selected for the first sales-workspace vertical slice.
**Owner:** Human Director.

## Intent
Connect the existing "ملف المنتج والعرض" navigation item to a real product-and-market profile workflow. The user must be able to create, list, and update multiple product profiles within the authenticated workspace. This is the prerequisite data foundation for demand-discovery runs; it is not itself a search or customer-discovery feature.

## Why this slice first
The repository already contains validated domain contracts in `agents/sales_domain.py` (`ProductProfile`, `ProductFact`, and `MarketProfile`), but the current SQLite store and HTTP API have no product-profile persistence or endpoints. The current UI marks this module disabled. Connecting this one bounded capability creates a real, reusable foundation without pretending discovery or CRM capabilities already exist.

## Goals
- Persist multiple product and market profiles in SQLite.
- Enforce tenant ownership from the authenticated server principal for every read and write.
- Reuse existing domain validation and JSON serialization.
- Expose authenticated list/create/update API contracts.
- Connect the existing RTL UI to these APIs with loading, empty, validation, and error states.
- Keep unimplemented modules disabled and accurately labeled.
- Fix the workspace placeholder's research-agent link to open `/agent`.

## Non-goals
- No web search, source scraping, discovery run, lead creation, evidence extraction, or prospect resolution in this slice.
- No provider or model changes, no new secrets, no paid API usage.
- No tenant provisioning, memberships administration, or authentication changes.
- No redesign of the approved Neon Command UI.
- No production deployment or merge.

## Approaches considered
1. **Store JSON in a tenant-scoped table — selected.** Add one `product_profiles` table with profile/market JSON and timestamps, indexed by tenant and update time. This preserves the existing validated domain objects and avoids premature normalization while keeping ownership and uniqueness in SQL.
2. **Create separate relational tables for every product field.** Rejected for this first slice: the domain is still evolving, and aliases/use cases/facts are bounded collections already represented by validated models. Additional joins would not yet enable an end-user capability.
3. **Keep product profiles in browser storage.** Rejected: browser state is not authoritative, cannot securely enforce tenant isolation, and would not be available to subsequent discovery tasks.

## API contract
- `GET /api/products` — list profiles for authenticated tenant only; read access includes viewer.
- `POST /api/products` — create a profile; viewer is denied.
- `POST /api/products/{id}` — update a profile belonging to authenticated tenant; cross-tenant identifiers return 404; viewer is denied.
- Request body: `profile` object using the exact `ProductProfile` fields and `market` object using the exact `MarketProfile` fields. Ignore no unknown fields silently: reject malformed structures and unsupported fields.
- The server derives `tenant_id` only from the verified principal; any client-supplied tenant ID is ignored/rejected and never used for authorization.

## Data model and compatibility
Create `product_profiles(id, tenant_id, profile_json, market_json, created_at, updated_at)`, with a foreign key to `tenants(id)` and index `(tenant_id, updated_at DESC)`. Use `CREATE TABLE IF NOT EXISTS`; no destructive migration and no changes to existing lead/session tables. Existing databases gain the table on normal store initialization. Product facts preserve their explicit origin and evidence pointer.

## UI behavior
Enable only "ملف المنتج والعرض" when its API is implemented and tested. Support create/list/edit. Keep discovery, campaigns, evidence, companies, and other unsupported modules disabled until their own server contracts and tests exist. Do not expose fields or data that have not been saved by the API.

## Security and failure cases
- Unauthenticated API requests are rejected by existing API authorization middleware.
- Viewer may list but cannot create or update.
- A user's tenant comes only from the server-authenticated principal.
- Product ID from another tenant behaves as not found.
- Invalid arrays, facts, enums, lengths, or unknown fields return 400 without persistence.
- Database failure returns the existing generic 500 response; no secret or raw SQL details leak.

## Acceptance
- Storage CRUD persists across new store instances using the same SQLite file.
- Multiple products can coexist for one tenant.
- A second tenant cannot list, read, or update another tenant's profiles.
- API enforces authentication and viewer write denial.
- UI reads/writes only through the API and shows stored records.
- Targeted tests, full pytest, Ruff, container build and CI pass before PR review.
