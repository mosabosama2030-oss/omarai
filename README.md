# Omarai — Web Research & Generative Q&A Agent

Omarai is an Arabic-first web research agent with a responsive RTL chat UI. You can ask open-ended questions in natural language, search the public web, extract text from accessible pages, compare and summarize findings, ask follow-up questions, and inspect the source links.

## What this version does

- Plans up to five search queries from a natural-language question with the configured language model, and uses a deterministic multi-query fallback when the model is unavailable.
- Runs DuckDuckGo HTML and Bing RSS independently for every planned query; uses Google News RSS for queries judged time-sensitive.
- Fuses duplicate results across queries and engines using reciprocal-rank fusion, preserving provider, query, domain, platform, publication-date and page-extraction provenance.
- Extracts text from up to five accessible public pages per question with request-size and timeout bounds.
- Searches public Reddit RSS and the Bluesky public search endpoint when social discussion is relevant. Searches indexed public pages on Facebook, Instagram, X, TikTok, LinkedIn, Threads and YouTube through the general web engines.
- Can use the official X recent-post endpoint when `X_BEARER_TOKEN` is configured and the account/API tier permits the request; can use the official YouTube Data API when `YOUTUBE_API_KEY` is configured.
- Generates an evidence-grounded answer in the user's language, showing source links, search query plan, provider coverage, direct page reads, platform mix and warnings.
- Carries up to eight recent chat messages from the current browser session into follow-up questions.
- Keeps the existing local SQLite lead workspace at `/leads`.
- Binds to loopback by default; it is not a public production deployment.

This is a tool-using research agent built around an existing language model, not a foundation model trained from scratch. Its language-model planner decides how to search, but query count, URLs and result shapes are validated by deterministic code. Cross-engine agreement improves discovery and ranking but is not independent fact verification. Public social pages that require login, blocked pages and private profiles are not fetched; social search cannot promise complete coverage of any platform. Direct official-platform access varies: X API access requires an authorized bearer token and suitable API access; Meta/Instagram generally require authorized API access and permissions; YouTube direct API search requires a Google API key. Review each platform's terms, quotas and permitted use before using the agent commercially. The agent never bypasses login, paywall or access controls and does not send messages or make automated contact with people.

## Run on Android / Termux

From the repository directory:

```bash
python -m pip install -e .
```

The default language-model route is OpenRouter's free-model router. Create an API key in your OpenRouter account, then enter it without putting the secret into a command-history entry. The model key enables both search planning and generative synthesis; general web search can still run without it, but results will not be turned into a full language-model analysis:

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

Use `OMARAI_LLM_API_KEY` instead of `OPENROUTER_API_KEY` when you want a separate environment variable. `OMARAI_LLM_TIMEOUT` accepts a timeout in seconds from 5 to 60. Provider pricing, model availability and rate limits can change; check the chosen provider before using a paid model. For optional direct X search, configure `X_BEARER_TOKEN`. For direct YouTube Data API search, configure `YOUTUBE_API_KEY` in the Termux session before starting the server. Do not store keys in source files, HTML, commits or chat messages.

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

The response includes `answer`, `sources`, `search_queries`, `research_plan`, `search_report`, `used_web_search`, `used_social_search`, `used_language_model`, and any warnings. The report records planned and attempted queries, unique result count, pages read, providers, platform breakdown, citation-range checks and whether an optional second-pass consistency review completed. That second pass uses the same configured model/provider and is not independent fact verification. URL syntax is validated and resolved private/local addresses are rejected before page fetches; the fetcher does not follow redirects. Search engines may still return inaccessible, stale or noisy results, which the agent must disclose.

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
