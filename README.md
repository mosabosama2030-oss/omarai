# Omarai — Web Research & Generative Q&A Agent

Omarai is an Arabic-first web research agent with a responsive RTL chat UI. You can ask open-ended questions in natural language, search the public web, extract text from accessible pages, compare and summarize findings, ask follow-up questions, and inspect the source links.

## What this version does

- Searches the public web using the `ddgs` metasearch library.
- Attempts to extract text from up to three accessible public pages per question (bounded size and time).
- Uses an OpenAI-compatible generative language API to interpret open-ended questions and synthesize answers in the user's language.
- Returns the search URLs and snippets separately so the user can inspect them.
- Carries up to eight recent chat messages from the current browser session into follow-up questions.
- Keeps the existing local SQLite lead workspace at `/leads`.
- Binds to loopback by default; it is not a public production deployment.

This is a practical agent built around an existing language model, not a foundation model trained from scratch. The quality and breadth of answers depend on the selected model, available search results, network access and provider limits. A search result is not automatically proof. The agent does not bypass logins, paywalls, robots/access controls, and does not automatically scrape private social accounts or send messages.

## Run on Android / Termux

From the repository directory:

```bash
python -m pip install -e .
```

The default language-model route is OpenRouter's free-model router. Create an API key in your OpenRouter account, then enter it without putting the secret into a command-history entry:

```bash
read -r -s -p "OpenRouter API key: " OPENROUTER_API_KEY
printf '\n'
export OPENROUTER_API_KEY
python -m cli.omarai serve
```

Keep this Termux session running and open **http://127.0.0.1:8765** in the phone's browser. The agent chat is the home screen. The existing lead workspace remains available at **http://127.0.0.1:8765/leads**.

The key is held in the current shell environment and is not written into the repository. Enter it again in a new Termux session. Never commit API keys or paste them into public issues or chat.

### Optional configuration

For a different OpenAI-compatible endpoint or model, set these environment variables before starting the server:

```bash
export OMARAI_LLM_BASE_URL="https://openrouter.ai/api/v1"
export OMARAI_LLM_MODEL="openrouter/free"
```

Use `OMARAI_LLM_API_KEY` instead of `OPENROUTER_API_KEY` when you want a separate environment variable. `OMARAI_LLM_TIMEOUT` accepts a timeout in seconds from 5 to 60. Provider pricing, model availability and rate limits can change; check the chosen provider before using a paid model.

If no language-model key is configured, Omarai can still attempt web search and show source snippets, but it cannot provide the full generative understanding/synthesis layer. If search providers are temporarily unavailable, the agent reports the limitation rather than pretending that a search succeeded.

## API

- `GET /` — web-research chat
- `GET /leads` — existing lead workspace
- `GET /api/health` — setup and dependency status (never returns the API key)
- `POST /api/agent` — open-ended question plus optional recent `history`
- `POST /api/analyze` — existing rule-based lead-text assessment
- `GET/POST /api/leads` — existing local lead records

Example request:

```json
{
  "question": "Compare the latest public information about two technologies",
  "history": []
}
```

The response includes `answer`, `sources`, `used_web_search`, `used_language_model`, and any warnings. Source extraction is bounded, and URLs are checked to reject obvious private/local destinations before fetching.

## Existing lead workspace

The previous local lead-intent tool is preserved at `/leads`. It stores data locally in `~/.omarai/omarai.sqlite3`. Its transparent rule score is not a statistical probability of a purchase. Process only public/authorized data, minimize personal information, and manually review business decisions.

Analyze text from the CLI:

```bash
python -m cli.omarai analyze --text "بدور على شقة في التجمع الخامس وممكن معاينة" --product "شقة,عقار" --location "التجمع الخامس"
```

CSV import requires `text,source_url,platform` columns:

```bash
python -m cli.omarai import-csv --file leads.csv
python -m cli.omarai list --limit 50
python -m cli.omarai export-csv --file leads-export.csv
```

## Checks

```bash
python -m pip install -e ".[dev]"
ruff check agents api cli tests
python -m pytest -q
```
