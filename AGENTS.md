# Omarai — Mandatory Agent and Contributor Instructions

These rules apply to every AI agent, human contributor, code change, test report, and deployment task in this repository.

## Source of truth
- Read `docs/OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md` before architecture, security, performance, data-flow, search, model, tool-execution, concurrency, or deployment changes.
- The charter is a design requirement, not evidence that controls already exist. Inspect the actual code and tests before describing implementation status.
- Treat `README.md` as a description of the current documented behavior, but verify claims against code and runtime evidence when the task requires it.

## Evidence discipline
- Label consequential findings **VERIFIED**, **INFERRED**, **PROPOSED**, or **UNKNOWN**.
- Never invent files, functions, branches, commits, workflows, test results, tool capabilities, deployment status, capacity numbers, or security guarantees.
- A configured API key is not proof that a connector works. A health/configuration response is not proof that a provider is reachable. A model's self-review is not independent verification.
- When reporting a test, include the exact command, actual result, relevant commit or code state, and any environment limitation. Never say a test was run when it was not.
- Prefer regression tests for fixed defects and measurable evidence for performance, capacity, quality, and security claims.

## Required engineering behavior
- Prefer the smallest safe change that solves the verified problem. Do not rewrite the architecture without a documented reason and migration path.
- Preserve existing behavior unless the task explicitly authorizes a change; identify compatibility risks.
- Bound external calls, retries, payload sizes, number of search results/pages, planning steps, model calls, elapsed time, and concurrency where applicable.
- Treat model output, search results, fetched pages, user files, and external tool outputs as untrusted data. Validate schemas and permissions at deterministic execution boundaries.
- Do not expose secrets, private user data, internal traces, or sensitive prompts in logs, HTTP errors, front-end assets, commits, or reports.
- Do not weaken authentication, authorization, SSRF protections, tenant/session isolation, resource limits, or test coverage to improve speed.
- Do not give a model unrestricted shell, filesystem, network, or database access. Tools must be explicitly registered, scoped, bounded, and verified.
- For any change affecting security, external networking, persistence, concurrency, or tool execution, add or identify appropriate negative/failure tests, not only happy-path checks.
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

## Acceptance principle
A capability is not complete because it appears in a plan, comment, prompt, or documentation. It is complete only to the extent supported by the implementation, relevant tests, observed output, and explicitly stated limitations.
