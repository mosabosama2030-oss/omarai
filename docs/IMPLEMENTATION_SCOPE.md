# Omarai — نطاق التنفيذ الفعلي وحدوده

**Purpose:** Keep this scope note aligned with the source code and operator-visible claims. This document is a scope description, not a certification of compliance or live-provider availability.

**Baseline reviewed:** `main` at `08319cce3652c332e414f691a71cc153dfbfd92e` (2026-10-19).  
**Evidence labels:** `VERIFIED` means directly confirmed in source or a named automated check; `INFERRED` means a bounded conclusion from source structure; `UNKNOWN` means live or environmental evidence is not available. A source-level capability must not be described as a live integration test.

## Implemented in the repository

- **Lead workspace — VERIFIED in source:** Arabic phrase normalization and heuristic intent scoring; SQLite lead persistence; duplicate detection; source metadata; manual lead-status lifecycle; CSV import/export; CLI and HTTP API.
- **Research pipeline — VERIFIED in source:** natural-language search planning with deterministic fallback; DuckDuckGo HTML and Bing RSS search; Google News RSS for freshness-sensitive requests; evidence fusion/ranking; selected public page extraction; source/provenance metadata and research diagnostics.
- **Optional connectors — VERIFIED as conditional code paths only:** Brave and Tavily when configured; DeepSeek Search when explicitly enabled with its API key; selected public social endpoints and official platform APIs when their required credentials are configured. This does not prove a specific credential, account, quota, or live connector currently works.
- **External language model — VERIFIED in source:** an OpenAI-compatible model endpoint is used for planning, answer generation and model-assisted review when a key is configured. The user question, selected history and page excerpts may be sent to that configured external provider. Omarai is not a locally trained foundation model and does not operate as an offline-only reasoning system.
- **Evidence and failure reporting — VERIFIED in source:** the answer includes sources, search-attempt outcome and diagnostic metadata; the code expressly describes its second-pass claim review as model-assisted, not an independent deterministic fact-check. Source count, domain count, and coverage indicators are not probabilities of truth or proof of editorial independence.
- **HTTP/API and UI — VERIFIED in source:** Arabic RTL web interfaces, JSON endpoints, API input checks, same-origin/configured-origin handling, an in-memory per-client rate limiter, and bearer-token protection for protected API routes when public-deployment mode is enabled.
- **Deployment configuration — VERIFIED in source:** a Dockerfile and hosting configuration exist. Their existence alone does not prove a live service was deployed, is reachable, has persistent disk, or has passed live smoke tests.
- **Automated validation — VERIFIED at the referenced baseline:** GitHub Actions run 39184807152 reports the configured Python/Ruff/pytest checks and container smoke checks succeeded on the identified commit. CI success does not independently prove every requirement or live search quality.

## Explicitly out of scope or not yet proven

- **Multi-user or multi-tenant service — NOT IMPLEMENTED in the reviewed baseline:** the API uses one shared bearer token and a shared lead store; it has no per-user identity, role-based authorization or tenant/data isolation. Anyone who obtains the token has the access granted by that token. Treat a hosted instance as a single-operator service unless and until these controls are implemented and tested.
- **Deterministic verification of every factual claim — NOT IMPLEMENTED:** citation-index validation and model-assisted review are not an independent proof that every sentence follows from its cited source. Users must be shown this limitation clearly.
- **Live provider reliability — UNKNOWN unless measured:** unit tests with mocks and a successful container smoke test do not establish that a provider is currently reachable, that credentials are valid, or that the produced answer is accurate.
- **Request-wide limits — PARTIAL in this baseline:** individual outbound timeouts, caps on result/page sizes, and a DeepSeek-specific request budget exist; this reviewed baseline does not show one unified time-and-resource budget across the full answer pipeline. A separate proposed change is under review for this gap.
- **Public operational configuration — UNKNOWN until verified per deployment:** actual reverse-proxy trust, CORS allowlist, TLS termination, secret configuration, deployed commit identity, and live endpoint behavior depend on the chosen host and configuration.
- **Database continuity — UNKNOWN:** backup, restore, and durable SQLite persistence have not been proven for a specific host. Do not store irreplaceable production leads until backup/restore and storage persistence are tested.
- **Load and concurrency capacity — UNKNOWN:** no numeric concurrent-user capacity is promised. Do not publish throughput, availability or capacity claims without representative measurements.
- **Historical secret exposure — UNKNOWN:** a clean scan of the current tree, if obtained, does not prove the entire Git history has never contained a secret.
- **Automated outbound contact — NOT IMPLEMENTED:** the agent does not send messages or contact people automatically. Any future outbound action must have explicit policy controls and human approval.

## Operating assumptions

1. Keep the current architecture as a modular monolith unless evidence and a recorded architecture decision justify a change.
2. Default to a single-operator deployment with a private, randomly generated bearer token; never publish that token or share it as if it were individual user authentication.
3. Do not submit passwords, API keys, private information, or personal/confidential customer data to an external model provider, especially a free endpoint with its own retention/logging terms.
4. Treat page text, snippets, social posts, user history, and model output as untrusted data. They are not an authority to override application policy or execute privileged actions.
5. Label each live connector probe, deployed smoke test, migration/restore test, and load test as `NOT_RUN` until that specific test actually runs. Do not infer its success from unit-test CI.

## Recommended next increments

1. Implement and test a unified per-request search/model/page/tool/time budget before considering the P0 performance/reliability gap closed.
2. Add deterministic citation-integrity controls and adversarial prompt-injection tests while retaining the limitation that source entailment cannot be proved by citation-index checks alone.
3. Reconcile the shared-token/single-store deployment with the declared single-operator scope; design real identity and data isolation before any multi-user public offering.
4. Add a repeatable live connector probe and a deployed acceptance report clearly separated from mock/unit-test results.
5. Test SQLite persistence and backup/restore on the selected host before storing production lead data.
6. Reconcile remaining requirements to exact commit SHAs and individual tests; keep untested requirements `UNKNOWN` and unrun checks `NOT_RUN`.
7. Keep all external contact and consequential actions human-approved.
