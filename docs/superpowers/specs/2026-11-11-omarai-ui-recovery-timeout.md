# Omarai UI Recovery and Request Timeout Specification

**Status:** Approved for implementation by the Human Director's request to execute the previously defined task list.

## Goal
Make the main workspace chat and legacy agent search recover predictably from long-running browser requests, and prevent successful writes from being reported as failures when a follow-up list refresh fails.

## Required behavior
1. The browser applies a 135-second client-side deadline to `/api/agent` requests in both `web/workspace.html` and `web/agent.html`.
2. Aborting the browser request is not represented as server-side cancellation. The timeout message explicitly says the server may continue within its own request budget.
3. Chat/search controls are restored in `finally`; duplicate submissions remain blocked while a request is active.
4. The workspace API helper forwards an optional AbortSignal without changing callers that do not provide one.
5. Refresh failures preserve the last successfully loaded data and display an actionable error.
6. After a successful save, a later list-refresh failure is reported separately; it must not imply that the save failed or encourage duplicate writes.
7. No connector credentials, provider calls, database schema, deployment settings, or production deployment are changed.

## Non-goals
- No claim of hard server cancellation.
- No automatic retry.
- No production-host restart or hosted-volume durability claim.
- No new JavaScript or Python dependencies.
