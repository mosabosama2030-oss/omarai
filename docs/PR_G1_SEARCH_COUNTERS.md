# PR-G1: connector summary + split counters

Branch: `fix/search-connector-summary-and-counters`
Base: `main` @ `61246000c49deec70b9dc6e3535efe70069ccad1`

## Intent
- Per-request `connector_summary` from `provider_diagnostics`
- Split counters: `raw_results`, `unique_urls`, `pages_fetch_attempted`, `pages_content_extracted`, `pages_extract_failed`
- UI shows extracted pages vs fetch attempts; expandable connector diagnostics

## Files
- `agents/web_agent.py` — `_connector_status_summary`, report fields
- `web/agent.html` — metrics + connector details
- `tests/test_web_agent.py` — unit tests

## Local tests (NOT CI)
- `test_connector_status_summary_*` PASS
- `test_collect_research_report_splits_*` PASS
- Broader suite: 113 passed; 1 failed due to local `tldextract` stub (public suffix), not this change
- Ruff: NOT_RUN (package install blocked)
- Live search: NOT_RUN

## Note
Full file payloads for this branch are maintained locally; apply the unified patch from the implementing agent artifacts if the large file push is incomplete.

Do not merge without verifying `web/agent.html` is complete (must not be the literal string `<placeholder>`).
