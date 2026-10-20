# Omarai — Web Research & Generative Q&A Agent

> **Foundational engineering requirements:** mandatory contributor/agent rules are in [AGENTS.md](AGENTS.md). The core architecture and security charter is [OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md](docs/OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md); the expanded platform practices across reliability, security, privacy, data, SRE, AI, accessibility, supply chain, and cost are in [OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md](docs/OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md); and the requirement IDs, expert-review lenses, evidence model, risk priorities, maturity stages, and release gates are in [OMARAI_REQUIREMENTS_TRACEABILITY_AND_MATURITY_MODEL_AR.md](docs/OMARAI_REQUIREMENTS_TRACEABILITY_AND_MATURITY_MODEL_AR.md). The initial foundational requirements checklist is [OMARAI_REQUIREMENTS_REGISTER.md](docs/OMARAI_REQUIREMENTS_REGISTER.md). These documents define required direction; they do not prove every control is implemented or tested.

Omarai is an Arabic-first web research agent with a responsive RTL chat UI. You can ask open-ended questions in natural language, search the public web, extract text from accessible pages, compare and summarize findings, ask follow-up questions, and inspect the source links.

## What this version does

- Plans up to eight search queries from a natural-language question with a dedicated reasoning/planning model, and uses a deterministic multi-query fallback when the model is unavailable.
- Uses separate model roles by default: NVIDIA Nemotron 3 Ultra (free) for query planning and Google Gemma 4 31B Instruct (free) for answer synthesis and the second-pass consistency review; retries with OpenRouter's free-model router if a chosen model fails.
- Runs DuckDuckGo HTML and Bing RSS independently for every planned query; can add official Brave Search API and Tavily Search API result indexes when their environment keys are configured; uses Google News RSS for queries judged time-sensitive.
- Fuses duplicate results across queries and engines using reciprocal-rank fusion, preserving provider, query, domain, platform, publication-date and page-extraction provenance.
- Extracts text from up to eight accessible public pages per question with request-size and timeout bounds, following at most three individually validated public redirects.
- Searches public Reddit RSS and the Bluesky public search endpoint when social discussion is relevant; can use Reddit's OAuth API when `REDDIT_CLIENT_ID` and `REDDIT_CLIENT_SECRET` are provided.
- Searches indexed public pages on Facebook, Instagram, X, TikTok, LinkedIn, Threads and YouTube through the general web engines.
- Can use the official Meta Graph API to read posts and a small sample of public comments from explicitly configured Facebook Pages when the token has suitable permissions.
- Can use Instagram Graph API hashtag search to read public hashtag media when `INSTAGRAM_USER_ID` and `INSTAGRAM_ACCESS_TOKEN` have the required permissions. It is not a global Instagram search and has platform quotas.
- Can use the official X recent-post endpoint when `X_BEARER_TOKEN` is configured and the account/API tier permits the request; can use the official YouTube Data API when `YOUTUBE_API_KEY` is configured.
- Generates an evidence-grounded answer in the user's language, showing source links, query plan, provider coverage, direct page reads, platform mix, source/domain diversity, date coverage, and evidence-coverage warnings. Coverage indicators describe breadth and inspectability; they are not probabilities that the answer is true.
- Carries up to eight recent chat messages from the current browser session into follow-up questions.
- Keeps the existing local SQLite lead workspace at `/leads`.
- Binds to loopback by default; it is not a public production deployment.

**Verification semantics:** `GET /api/health` is a configuration/dependency snapshot, not proof that search providers or the model are reachable. Check the `agent.verification_scope` field to see what is and is not verified. Use the protected `POST /api/diagnostics` endpoint for explicit live search/model probes; a passed diagnostic only verifies the specific probes run at that time, not every optional connector or answer quality.

This is a tool-using research agent built around existing language models, not a foundation model trained from scratch. The role-specific defaults aim for more consistent behaviour than using a router that selects a different free model at random on each call. Exact availability and response quality still depend on OpenRouter/provider conditions. **Privacy warning:** the user's question, conversation context and selected web excerpts are sent to the configured external language-model provider for planning/synthesis/review. OpenRouter's NVIDIA Nemotron free endpoint states that session data may be logged for security and product improvement; do not send passwords, API keys, private information or personal/confidential customer data through the free endpoint. See the [NVIDIA Nemotron free-endpoint privacy notice](https://openrouter.ai/nvidia/nemotron-3-ultra-550b-a55b:free). Its language-model planner decides how to search, but query count, URLs and result shapes are validated by deterministic code. Cross-engine agreement improves discovery and ranking but is not independent fact verification. Public social pages that require login, blocked pages and private profiles are not fetched; social search cannot promise complete coverage of any platform. Direct official-platform access varies: Reddit API access requires approved app credentials and is subject to Reddit's terms; Facebook Pages reads require a valid token, page identifiers and correct permissions; Instagram hashtag search requires a professional Instagram account token and the specific supported permissions; X API access requires an authorized bearer token and suitable access; YouTube direct API search requires a Google API key. These APIs do not grant universal access to all content, accounts or comments. Review each platform's terms, quotas and permitted use before using the agent commercially. The agent never bypasses login, paywall or access controls and does not send messages or make automated contact with people.


## Living repository index

Omarai maintains two generated navigation indexes:

- [MASTER INDEX](docs/MASTER_INDEX.md): categorized file inventory with stable file IDs, Python AST definitions, static frontend/configuration symbols, and explicit TODO/FIXME/BUG/HACK/XXX/REVIEW/SECURITY/DEPRECATED review-marker entries. Each review marker has its own `FND-...` code and points to an exact source-line ID.
- [SOURCE LINES INDEX](docs/SOURCE_LINES_INDEX.md): line-by-line index of every logical line in each eligible readable text file. Each row carries a deterministic `SRC-<FILEHASH>-L000001` code, original file path, category, line number and JSON-escaped source text. Use browser Find to search a function, variable, phrase, marker or file path, then open the source file at the listed line.

Regenerate both indexes locally:

```bash
python docs/generate_index.py
python docs/generate_index.py --check
```

GitHub Actions validates generation and reproducibility on Python 3.11 and 3.12. The workflow triggered by pushes to `main` regenerates and commits both files only when output changes. If direct publication is rejected, it opens a pull request rather than force-updating a branch or auto-merging. Files excluded for safety or practicality include known local secrets, runtime databases, generated/dependency directories, binary/unreadable files and individual text files larger than 2 MiB. The line index is a source-navigation aid, not a proof that each statement is correct. Explicit review markers are recorded, but arbitrary logic defects cannot be identified with 100% certainty by static indexing alone.

## Per-request resource budget

Each `POST /api/agent` answer includes a `request_budget` object with elapsed and remaining time, reserved resource counts, and configured limits. The current defaults are a 90-second cooperative deadline, at most 8 search queries, 32 provider search calls, 8 model HTTP attempts, 8 page fetches, and up to 3 optional server-side search-tool calls per request. Operator limits may be lowered or raised only within hard caps: `OMARAI_REQUEST_BUDGET_SECONDS` (10–120), `OMARAI_REQUEST_MAX_SEARCH_QUERIES` (1–8), `OMARAI_REQUEST_MAX_SEARCH_CALLS` (1–40), `OMARAI_REQUEST_MAX_MODEL_CALLS` (1–12), `OMARAI_REQUEST_MAX_PAGE_FETCHES` (1–8), and `OMARAI_REQUEST_MAX_TOOL_CALLS` (0–3). Invalid numeric values fall back to the defaults; out-of-range values are clamped.

The deadline caps the timeout passed to outbound operations and prevents new work from being reserved after the deadline or a resource cap is exhausted. It is **cooperative, not hard cancellation**: a network call already in progress may overrun slightly while its client unwinds. Do not interpret this metadata as a load test, a throughput guarantee, or proof that any live provider is reachable. CI tests for budget logic are separate from live-provider validation.

The HTTP API also limits expensive `/api/agent` and `/api/diagnostics` operations to at most 4 concurrent operations per process by default. Configure `OMARAI_MAX_CONCURRENT_AGENT_REQUESTS` from 1 to 8. If all slots are occupied, the API returns HTTP 503 with a short retry hint instead of queueing unlimited expensive work. This is a **process-local** cap, not a distributed semaphore across multiple workers or replicas, and it is not a throughput/load-test claim.

## Experimental DeepSeek Search provider

Omarai can optionally compare results from DeepSeek's Search API when
`DEEPSEEK_SEARCH_API_KEY` is configured in the host's secret settings. It is
**disabled by default**; DuckDuckGo and Bing remain configured as before.
To limit possible spend when opted in, the request budget defaults to **one
DeepSeek Search call per answer/diagnostic operation**. It can be set from 0 to 3
using `OMARAI_DEEPSEEK_SEARCH_REQUEST_BUDGET`; invalid values fall back to 1.
DeepSeek Search is billed per successful request (currently documented at
US$0.75 per 1,000 successful searches); review the
[official Search & Fetch guide](https://api-docs.deepseek.com/guides/search/)
before enabling it. Unit tests use a mocked response; this repository change
does not claim live DeepSeek connectivity or answer-quality improvement.

## Hosted deployment

A Dockerfile and Railway configuration are included for a public hosted instance. This is **deployment-ready configuration, not proof that a hosted service has already been created**: you must connect your Railway account to this GitHub repository, add secrets in the host dashboard, deploy, and run the live diagnostics.

Before public binding, set `OMARAI_PUBLIC_DEPLOYMENT=1` and a separate random `OMARAI_ACCESS_TOKEN` of at least 32 characters. The app refuses public binding without both. Set `OPENROUTER_API_KEY` in the hosting provider's secret variables for natural-language planning and synthesis. If the browser UI is served from a different origin, set `OMARAI_ALLOWED_ORIGINS` to a comma-separated allowlist of trusted origins (scheme + host + optional port, no path and no `*`). The API sends CORS headers only to allowed origins and handles preflight `OPTIONS`; when you open `/` on the same deployed service, the built-in UI uses relative `/api/...` URLs and normally needs no extra origin entry. Public API routes require the bearer token and have a default in-memory limit of 20 requests per minute per client IP. The Arabic UI provides a separate access-token field; it stores only that app token in the browser's local storage, not the provider API key.

See the step-by-step Arabic instructions in `docs/DEPLOY_RAILWAY_AR.md`. Before treating a deployment as accepted, follow the [hosted go-live checklist](docs/GO_LIVE_CHECKLIST_AR.md) and run the manually triggered [hosted acceptance smoke workflow](.github/workflows/hosted-smoke.yml) after configuring the GitHub Actions secrets `OMARAI_ACCESS_TOKEN` and `OMARAI_BASE_URL` (the latter must be only the service's HTTPS origin). The workflow uses that administrator-configured target rather than accepting a free-form URL alongside a secret, preventing accidental or unauthorized token disclosure to arbitrary hosts. It makes real model/search requests and may incur usage charges. SQLite on ephemeral hosting is not durable storage for customer records; do not treat the lead workspace as persistent until a managed database and backups are configured.

## Free hosted deployment (SnapDeploy)

For a free alternative when Render does not work, see the step-by-step Arabic [SnapDeploy guide](docs/DEPLOY_SNAPDEPLOY_AR.md). SnapDeploy's published free tier currently has monthly container-hour limits, sleeps after inactivity, and does not provide persistent disk storage. Treat it as a demo/acceptance-test host, not durable production hosting. Confirm the current limits and charges before deploying.

The guide covers GitHub linking, `main`, the Dockerfile, runtime secrets, HTTPS, live health/model/search tests, and the limitations of the existing SQLite lead workspace. No hosted service is created automatically by this repository.

## Free hosted deployment (Render)

A starter Render Blueprint is included in `render.yaml`, with Arabic setup notes in [docs/DEPLOY_RENDER_AR.md](docs/DEPLOY_RENDER_AR.md). The free service sleeps after inactivity and has an ephemeral filesystem; do not rely on the hosted SQLite lead database for durable storage. This is intended for a personal demo and acceptance testing, not production availability.

Before accepting the deployment, use the [Arabic go-live checklist](docs/GO_LIVE_CHECKLIST_AR.md) when that file is present on the selected branch. Never commit provider keys or the app access token.

## Run on Android / Termux

From the repository directory:

```bash
python -m pip install -e .
```

The default language-model configuration uses OpenRouter: Nemotron 3 Ultra (free) plans queries, Gemma 4 31B Instruct (free) writes the answer and performs the optional second-pass review, and `openrouter/free` is the fallback if a selected model fails. Create an OpenRouter API key, then enter it without putting the secret into a command-history entry. The model key enables both search planning and generative synthesis; general web search can still run without it, but results will not be turned into a full language-model analysis:

```bash
read -r -s -p "OpenRouter API key: " OPENROUTER_API_KEY
printf '\n'
export OPENROUTER_API_KEY
python -m cli.omarai serve
```

Keep this Termux session running and open **http://127.0.0.1:8765** in the phone's browser. The agent chat is the home screen. The existing lead workspace remains available at **http://127.0.0.1:8765/leads**.

The key is held in the current shell environment and is not written into the repository. Enter it again in a new Termux session. Never commit API keys or paste them into public issues or chat.

### Optional configuration

For additional live web-search indexes, configure either official search API. These keys are optional: the built-in public engines are still attempted, and each API may have its own account, quota, rate limit or cost. Do not assume an API is free or that a configured key is valid until you run the live diagnostics.

```bash
read -r -s -p "Brave Search API key: " BRAVE_SEARCH_API_KEY; printf '\\n'; export BRAVE_SEARCH_API_KEY
read -r -s -p "Tavily API key: " TAVILY_API_KEY; printf '\\n'; export TAVILY_API_KEY
```


For a different OpenAI-compatible endpoint or model, set these environment variables before starting the server:

```bash
export OMARAI_LLM_BASE_URL="https://openrouter.ai/api/v1"
export OMARAI_LLM_MODEL="openrouter/free"
```

Use `OMARAI_LLM_API_KEY` instead of `OPENROUTER_API_KEY` when you want a separate environment variable. `OMARAI_LLM_TIMEOUT` accepts a timeout in seconds from 5 to 60. To customize model roles, set `OMARAI_PLANNER_MODEL`, `OMARAI_ANSWER_MODEL`, and/or `OMARAI_REVIEW_MODEL`; `OMARAI_LLM_MODEL` remains a global override for all roles that have no role-specific override. `OMARAI_LLM_FALLBACK_MODEL` changes the default `openrouter/free` fallback. Provider pricing, model availability and rate limits can change; check the chosen provider before using a paid model. Optional social credentials may be configured in the same Termux session before starting the server: `REDDIT_CLIENT_ID` + `REDDIT_CLIENT_SECRET` (official OAuth access), `X_BEARER_TOKEN`, `YOUTUBE_API_KEY`, `INSTAGRAM_USER_ID` + `INSTAGRAM_ACCESS_TOKEN` + optional `META_GRAPH_VERSION`, and `FACEBOOK_PAGE_ACCESS_TOKEN` + `FACEBOOK_PAGE_IDS` (comma-separated Page IDs that the authorized token can access). Use `read -r -s` to enter secrets privately rather than saving them in shell history. Do not store keys in source files, HTML, commits or chat messages.

If no language-model key is configured, Omarai can still attempt web search and show source snippets, but it cannot provide the full generative understanding/synthesis layer. If search providers are temporarily unavailable, the agent reports the limitation rather than pretending that a search succeeded.

For the platform boundaries, optional credentials and safe Termux setup for social connectors, see the [Arabic research connectors guide](docs/RESEARCH_CONNECTORS_AR.md).

## API

- `GET /` — web-research chat
- `GET /leads` — existing lead workspace
- `GET /api/health` — setup and dependency status (never returns the API key)
- `POST /api/diagnostics` — opt-in live checks for web search and the language model; set `test_social: true` to also probe public/authorized social connectors
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

The `/api/diagnostics` response reports pass/fail/degraded states, returned result counts, provider counts, elapsed time, and the model that actually answered (including fallback use). The Arabic web UI offers automatic, deep, latest-information, and public-social research modes, plus a live-test button. The model check sends one small completion request; optional social checks perform real public/API requests and can take longer. The response from `/api/agent` includes `answer`, `sources`, `search_queries`, `research_plan`, `search_report`, `used_web_search`, `used_social_search`, `used_language_model`, and any warnings. The request can pass `mode` as `auto`, `deep`, `latest`, or `social`. The report records planned and attempted queries, unique result count, pages read, providers, platform breakdown, citation-range checks and whether an optional second-pass consistency review completed. That second pass uses the same configured model/provider and is not independent fact verification. URL syntax and resolved private/local addresses are checked before page fetches; public redirects are followed only through a small bounded loop with each destination revalidated. Search engines may still return inaccessible, stale or noisy results, which the agent must disclose.

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
