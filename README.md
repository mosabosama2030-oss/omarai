# Omarai — Arabic Lead-Intent Agent

Omarai is a standalone, local-first assistant for organizing customer-interest signals that an operator is authorized to process. It is independent from MosaabAI.

## MVP features
- Arabic-aware, explainable, rule-based intent analysis.
- Local SQLite storage with source URL, platform, timestamp, evidence and manual status.
- Duplicate prevention for the same normalized text and source.
- Local HTTP API, mobile-friendly Arabic RTL dashboard, and rule-based Q&A over saved records.
- CSV import/export and CLI.
- Tests and GitHub Actions.

## Honest limitations
Omarai does **not** crawl Facebook, Instagram, WhatsApp or property portals automatically. You must enter text manually or import data from a permitted source. A score is a transparent rule score, not a probability or proof of purchase. The app does not send messages or automatically contact leads.

## Run on Android / Termux
```bash
pkg install python
python -m cli.omarai serve
```
Open `http://127.0.0.1:8765` on the same phone. It binds to loopback by default; do not expose it to the public internet without authentication.

Ask the local assistant about saved records, scoring rules, or the next signal to review. Answers use the local SQLite database and explicit rules; no message is sent.

Analyze text:
```bash
python -m cli.omarai analyze --text "بدور على شقة في التجمع الخامس وممكن معاينة" --product "شقة,عقار" --location "التجمع الخامس"
```

CSV import requires `text,source_url,platform` columns:
```bash
python -m cli.omarai import-csv --file leads.csv
python -m cli.omarai list --limit 50
python -m cli.omarai export-csv --file leads-export.csv
```

Run checks:
```bash
python -m pip install pytest ruff
python -m pytest -q
ruff check agents api cli tests
```

Data is stored locally in `~/.omarai/omarai.sqlite3` by default. Only process public/authorized sources, minimize personal data, and review leads manually.
