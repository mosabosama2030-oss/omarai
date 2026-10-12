# Omarai MVP scope

## Included
- Rule-based Arabic phrase normalization and transparent scoring.
- SQLite persistence, source provenance, duplicate prevention, and manual lifecycle status.
- Local JSON API, Arabic RTL dashboard with rule-based Q&A, CLI, CSV import/export, automated tests.
- Loopback-only server and no external API dependency.

## Not included yet
- Automatic crawling of social networks or property portals.
- Automatic messaging, scraping private content, contact discovery, or identity verification.
- Calibrated probability of conversion; the score is a rule heuristic.
- Multi-user authentication, public hosting, cloud synchronization, or a hosted database.
- Generative free-form language-model reasoning; Q&A currently uses explicit local rules.

## Next increments
1. Validate the API and dashboard in Android/Termux.
2. Add stronger API validation and security tests.
3. Add a user-approved adapter for a documented, authorized source only.
4. Track observed outcomes and evaluate rules against a labeled dataset before changing scoring.
5. Keep all outbound contact human-approved.
