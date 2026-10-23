# Omarai — Mandatory Agent and Contributor Instructions

These rules apply to every AI agent, human contributor, code change, test report, and deployment task in this repository.

## Source of truth
- Read `docs/OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md` before architecture, security, performance, data-flow, search, model, tool-execution, concurrency, or deployment changes.
- Read `docs/OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md` before adding or changing tools, capabilities, skills, workflows, TaskSpec, agent profiles, agents, Meta-Agent, memory scope, or generated-code execution. Treat it as a supplementary architecture contract; do not replace the charter or assert its proposed controls are implemented without evidence.
- Read `docs/OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md` for broad platform requirements and release reviews involving reliability/SRE, capacity, API/security, privacy/data governance, CI/CD/supply chain, recovery, accessibility, search quality, AI/agent evaluation, cost, and operational governance. Apply only the controls relevant to the change, but explicitly record material gaps and risks.
- Use `docs/OMARAI_REQUIREMENTS_TRACEABILITY_AND_MATURITY_MODEL_AR.md` to classify important requirements, identify relevant expert-review lenses, record evidence and limitations, prioritize risks, and apply the change/release gates. Do not mark a requirement VERIFIED without implementation and reproducible evidence.
- Keep `docs/OMARAI_REQUIREMENTS_REGISTER.md` synchronized with material changes: record new findings and update the related requirement status only when supporting evidence exists. Until the code and relevant tests have been examined, use UNKNOWN; state unrun checks as NOT_RUN.
- The charter is a design requirement, not evidence that controls already exist. Inspect the actual code and tests before describing implementation status.
- Treat `README.md` as a description of the current documented behavior, but verify claims against code and runtime evidence when the task requires it.

## Evidence discipline
- Label consequential findings **VERIFIED**, **INFERRED**, **PROPOSED**, or **UNKNOWN**.
- Never invent files, functions, branches, commits, workflows, test results, tool capabilities, deployment status, capacity numbers, or security guarantees.
- A configured API key is not proof that a connector works. A health/configuration response is not proof that a provider is reachable. A model's self-review is not independent verification.
- When reporting a test, include the exact command, actual result, relevant commit or code state, and any environment limitation. Never say a test was run when it was not.
- Prefer regression tests for fixed defects and measurable evidence for performance, capacity, quality, and security claims.

## Architecture evolution and scalability
- Treat scalability, maintainability, and controlled evolution as foundational requirements; read the relevant charter sections before introducing modules, agents, tools, providers, persistence, queues, or services.
- Prefer a well-bounded modular monolith until measured scaling, fault-isolation, security, or release-independence needs justify a separate service. Do not add microservices or abstraction layers for appearance.
- New modules must have explicit responsibilities, public contracts, ownership, dependency direction, and appropriate tests. Avoid circular imports and cross-module access to private implementation details.
- Wrap external providers behind adapters and validate their input/output contracts. Keep provider-specific SDKs and response shapes out of domain logic.
- New tools/agents/plugins must declare schema, permissions, data classification, timeout, resource budget, concurrency limit, retry/idempotency behavior where applicable, health-check semantics, failure modes, and disable/rollback path.
- Treat API and event schema changes as versioned contracts. Prefer backward-compatible evolution; document deprecations and provide migration paths for breaking changes.
- All persistent data-shape changes need a tested migration and data-preservation/rollback strategy proportionate to risk. Never assume production data can be recreated from scratch.
- Do not rely on in-process global mutable state for cross-request user, tenant, or long-running task state. Assess what must survive process restarts before adding multi-process or horizontal scaling.
- Before extracting services, adding queues, changing storage, or introducing a distributed system, state the evidence-based need, operational costs, failure modes, security boundary, and acceptance tests.
- Add architecture fitness checks where practical for dependency boundaries, contracts, migrations, secrets, concurrency isolation, and critical performance limits.
- Record material architectural choices and exceptions in an ADR or equivalent, including rejected alternatives, tests, risks, compatibility, and rollback.
- Keep expansion incremental and reversible; do not represent future architecture goals as current capabilities.

## Required engineering behavior
- Prefer the smallest safe change that solves the verified problem. Do not rewrite the architecture without a documented reason and migration path.
- Preserve existing behavior unless the task explicitly authorizes a change; identify compatibility risks.
- Bound external calls, retries, payload sizes, number of search results/pages, planning steps, model calls, elapsed time, and concurrency where applicable.
- Treat model output, search results, fetched pages, user files, and external tool outputs as untrusted data. Validate schemas and permissions at deterministic execution boundaries.
- Do not expose secrets, private user data, internal traces, or sensitive prompts in logs, HTTP errors, front-end assets, commits, or reports.
- Do not weaken authentication, authorization, SSRF protections, tenant/session isolation, resource limits, or test coverage to improve speed.
- Do not give a model unrestricted shell, filesystem, network, or database access. Tools must be explicitly registered, scoped, bounded, and verified.
- For any change affecting security, external networking, persistence, concurrency, or tool execution, add or identify appropriate negative/failure tests, not only happy-path checks.
- For changes that cross a trust boundary, update or reference the threat model, validate deny-by-default authorization at execution time, and document negative tests for the relevant attack paths (e.g., prompt injection, SSRF/redirects, cross-user access, XSS, secret leakage, resource exhaustion, or supply-chain exposure). Disable or narrow a capability when required security controls cannot be demonstrated in its target environment.
- For performance or scalability work, establish a baseline and test in a named environment. Never claim support for an arbitrary user count without a reproducible load-test result.
- If evidence is insufficient, state the unknown and the smallest safe method to verify it.

## Change and release control
- Inspect the current branch, HEAD, working diff, and relevant files before editing.
- Work on a dedicated branch; keep changes scoped and reviewable.
- Run applicable checks when tools and environment permit, and report any checks that could not be run.
- Review the final diff and verify documentation links and new-file paths.
- Never merge a pull request, force-update a protected branch, or deploy to production without explicit authorization from the Human Director.
- Do not present a proposed or unmerged change as already effective on `main`.
- Update the charter or related documentation when a material design decision changes; document major architectural choices and exceptions with rationale, risks, tests, and rollback considerations.

## Platform-grade readiness
- For material production-facing changes, assess the applicable release gates in both the charter and the Global Platform Engineering Baseline; do not treat a checklist as proof of compliance.
- Define measurable SLI/SLO or a baseline where useful. Never invent uptime, latency, capacity, security maturity, cost, or recovery guarantees.
- Review blast radius, dependency failure, graceful degradation, quotas, per-request budgets, data lifecycle, tenant isolation when multi-user, supply-chain exposure, observability/privacy, and recovery proportional to risk.
- For AI/agent changes, test Arabic task quality, citation support, prompt injection, untrusted tool/page content, unauthorized actions, loops, provider failures, cost bounds, and safe fallback as applicable.
- Require an explicit reason before adding distributed infrastructure; document simpler alternatives and lifecycle costs. Do not apply every enterprise control blindly to a small deployment, but do not conceal a risk merely because a control is expensive or not yet supported.

## Requirement traceability and expert review
- For material changes, create or update stable requirement IDs and record applicability, status, evidence, test command/results, environment, limitations, residual risk, and owner in the requirements register or an equivalent reviewed record.
- Use all relevant discipline lenses (architecture, security, privacy, data, SRE, performance, AI evaluation, search/evidence, accessibility, supply chain, cost, and operations); do not claim that a human specialist independently reviewed work unless that actually happened.
- Keep non-applicable and waived requirements distinct from unknown ones. Exceptions to MUST controls need scope, compensating controls, an approver, a revisit/expiry condition, and recorded residual risk.
- Do not build advanced infrastructure to satisfy a checklist by appearance. Use trigger conditions and evidence in the baseline to decide when advanced requirements apply.

## Acceptance principle
A capability is not complete because it appears in a plan, comment, prompt, or documentation. It is complete only to the extent supported by the implementation, relevant tests, observed output, and explicitly stated limitations.


## Repository hygiene and documentation ownership
- Use [`docs/README.md`](docs/README.md) as the navigation map. Before adding a document, search for an existing owner of the same concern; update the canonical file instead of creating a parallel status or checklist.
- Keep one current source of truth per concern: implementation boundaries in `docs/IMPLEMENTATION_SCOPE.md`; issue/finding IDs in `docs/OMARAI_REMEDIATION_REGISTER_AR.md`; current post-merge evidence in `docs/OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md`; test categories and limitations in `docs/OMARAI_TEST_EVIDENCE_MATRIX_AR.md`.
- Historical audit snapshots belong under `docs/archive/`. Mark their baseline SHA/date and link to current guidance; never silently rewrite old test evidence to look current.
- Do not keep a second live-status document with a different PR state or baseline SHA. Read current PR/branch state from GitHub; avoid hard-coding the state of an open PR in durable docs.
- Never hand-edit generated files under `docs/source_index/`, `docs/MASTER_INDEX.md`, `docs/SOURCE_LINES_INDEX.md`, or `docs/INDEX_COVERAGE_AUDIT.md`. Run `python docs/generate_index.py` and `python docs/generate_index.py --check`; inspect the generated diff. For documentation-only or repository-hygiene PRs, do not add index page churn solely because source lines shifted: the test workflow regenerates and verifies indexes in its isolated checkout, and the publisher refreshes committed indexes on `main` after merge. Keep the strict committed-index check on `main`.
- Each PR should have one purpose, be based on current `main`, link the root cause to exact changes/tests, state checks that were not run, and avoid unrelated generated or historical changes. Do not merge or deploy without human director approval.
