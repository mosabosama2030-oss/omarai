# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **029**
- سجلات الأسطر: **800**
- النطاق: SRC-C693279643-L000014 إلى SRC-A8360B1B03-L000009
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## ملفات أخرى

### FILE-C693279643 — [LICENSE](../../LICENSE#L1)

- النوع: **بدون امتداد**
- نطاق الفهرسة: جرد ملف نصي فقط

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-C693279643-L000014](../../LICENSE#L14) | 14 | `""` | — |
| [SRC-C693279643-L000015](../../LICENSE#L15) | 15 | `"THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR"` | — |
| [SRC-C693279643-L000016](../../LICENSE#L16) | 16 | `"IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,"` | — |
| [SRC-C693279643-L000017](../../LICENSE#L17) | 17 | `"FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE"` | — |
| [SRC-C693279643-L000018](../../LICENSE#L18) | 18 | `"AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER"` | — |
| [SRC-C693279643-L000019](../../LICENSE#L19) | 19 | `"LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,"` | — |
| [SRC-C693279643-L000020](../../LICENSE#L20) | 20 | `"OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE"` | — |
| [SRC-C693279643-L000021](../../LICENSE#L21) | 21 | `"SOFTWARE."` | — |
## إعدادات وتشغيل

### FILE-50C86B7ED8 — [pyproject.toml](../../pyproject.toml#L1)

- النوع: **TOML**
- نطاق الفهرسة: جرد الملف + مفاتيح إعداد ساكنة

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-50C86B7ED8-L000001](../../pyproject.toml#L1) | 1 | `"[build-system]"` | — |
| [SRC-50C86B7ED8-L000002](../../pyproject.toml#L2) | 2 | `"requires = [\"setuptools>=68\"]"` | — |
| [SRC-50C86B7ED8-L000003](../../pyproject.toml#L3) | 3 | `"build-backend = \"setuptools.build_meta\""` | — |
| [SRC-50C86B7ED8-L000004](../../pyproject.toml#L4) | 4 | `""` | — |
| [SRC-50C86B7ED8-L000005](../../pyproject.toml#L5) | 5 | `"[project]"` | — |
| [SRC-50C86B7ED8-L000006](../../pyproject.toml#L6) | 6 | `"name = \"omarai-agent\""` | — |
| [SRC-50C86B7ED8-L000007](../../pyproject.toml#L7) | 7 | `"version = \"0.2.0\""` | — |
| [SRC-50C86B7ED8-L000008](../../pyproject.toml#L8) | 8 | `"description = \"Arabic-first web research and generative Q&A agent with lead workspace\""` | — |
| [SRC-50C86B7ED8-L000009](../../pyproject.toml#L9) | 9 | `"readme = \"README.md\""` | — |
| [SRC-50C86B7ED8-L000010](../../pyproject.toml#L10) | 10 | `"requires-python = \">=3.11\""` | — |
| [SRC-50C86B7ED8-L000011](../../pyproject.toml#L11) | 11 | `"license = { text = \"MIT\" }"` | — |
| [SRC-50C86B7ED8-L000012](../../pyproject.toml#L12) | 12 | `"dependencies = ["` | — |
| [SRC-50C86B7ED8-L000013](../../pyproject.toml#L13) | 13 | `"  \"beautifulsoup4>=4.12,<5\","` | — |
| [SRC-50C86B7ED8-L000014](../../pyproject.toml#L14) | 14 | `"  \"httpx>=0.27,<1\","` | — |
| [SRC-50C86B7ED8-L000015](../../pyproject.toml#L15) | 15 | `"  \"tldextract>=5.3,<6\","` | — |
| [SRC-50C86B7ED8-L000016](../../pyproject.toml#L16) | 16 | `"]"` | — |
| [SRC-50C86B7ED8-L000017](../../pyproject.toml#L17) | 17 | `""` | — |
| [SRC-50C86B7ED8-L000018](../../pyproject.toml#L18) | 18 | `"[project.optional-dependencies]"` | — |
| [SRC-50C86B7ED8-L000019](../../pyproject.toml#L19) | 19 | `"dev = [\"pytest>=8.0\", \"ruff>=0.5\"]"` | — |
| [SRC-50C86B7ED8-L000020](../../pyproject.toml#L20) | 20 | `""` | — |
| [SRC-50C86B7ED8-L000021](../../pyproject.toml#L21) | 21 | `"[tool.pytest.ini_options]"` | — |
| [SRC-50C86B7ED8-L000022](../../pyproject.toml#L22) | 22 | `"testpaths = [\"tests\"]"` | — |
| [SRC-50C86B7ED8-L000023](../../pyproject.toml#L23) | 23 | `""` | — |
| [SRC-50C86B7ED8-L000024](../../pyproject.toml#L24) | 24 | `"[tool.setuptools.packages.find]"` | — |
| [SRC-50C86B7ED8-L000025](../../pyproject.toml#L25) | 25 | `"include = [\"agents*\", \"api*\", \"cli*\"]"` | — |
| [SRC-50C86B7ED8-L000026](../../pyproject.toml#L26) | 26 | `"exclude = [\"tests*\", \"web*\"]"` | — |
| [SRC-50C86B7ED8-L000027](../../pyproject.toml#L27) | 27 | `""` | — |
| [SRC-50C86B7ED8-L000028](../../pyproject.toml#L28) | 28 | `"[tool.ruff]"` | — |
| [SRC-50C86B7ED8-L000029](../../pyproject.toml#L29) | 29 | `"line-length = 100"` | — |
| [SRC-50C86B7ED8-L000030](../../pyproject.toml#L30) | 30 | `"target-version = \"py311\""` | — |
| [SRC-50C86B7ED8-L000031](../../pyproject.toml#L31) | 31 | `""` | — |
| [SRC-50C86B7ED8-L000032](../../pyproject.toml#L32) | 32 | `"[tool.ruff.lint]"` | — |
| [SRC-50C86B7ED8-L000033](../../pyproject.toml#L33) | 33 | `"# Keep default rules; ignore only patterns intentional in this codebase."` | — |
| [SRC-50C86B7ED8-L000034](../../pyproject.toml#L34) | 34 | `"# BLE001: broad except at API boundary to avoid leaking internals"` | — |
| [SRC-50C86B7ED8-L000035](../../pyproject.toml#L35) | 35 | `"# E501: long Arabic/English diagnostic strings"` | — |
| [SRC-50C86B7ED8-L000036](../../pyproject.toml#L36) | 36 | `"# I001: historical import order; do not block CI on style alone"` | — |
| [SRC-50C86B7ED8-L000037](../../pyproject.toml#L37) | 37 | `"# F841: unused assignment kept for clarity in some tests"` | — |
| [SRC-50C86B7ED8-L000038](../../pyproject.toml#L38) | 38 | `"# RUF100: residual noqa:BLE001 comments after BLE001 is ignored globally"` | — |
| [SRC-50C86B7ED8-L000039](../../pyproject.toml#L39) | 39 | `"ignore = [\"BLE001\", \"E501\", \"I001\", \"F841\", \"RUF100\"]"` | — |
## إعدادات وتشغيل

### FILE-115C2027D9 — [railway.json](../../railway.json#L1)

- النوع: **JSON**
- نطاق الفهرسة: جرد الملف + مفاتيح إعداد ساكنة

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-115C2027D9-L000001](../../railway.json#L1) | 1 | `"{"` | — |
| [SRC-115C2027D9-L000002](../../railway.json#L2) | 2 | `"  \"$schema\": \"https://railway.com/railway.schema.json\","` | — |
| [SRC-115C2027D9-L000003](../../railway.json#L3) | 3 | `"  \"build\": {"` | — |
| [SRC-115C2027D9-L000004](../../railway.json#L4) | 4 | `"    \"builder\": \"DOCKERFILE\","` | — |
| [SRC-115C2027D9-L000005](../../railway.json#L5) | 5 | `"    \"dockerfilePath\": \"Dockerfile\""` | — |
| [SRC-115C2027D9-L000006](../../railway.json#L6) | 6 | `"  },"` | — |
| [SRC-115C2027D9-L000007](../../railway.json#L7) | 7 | `"  \"deploy\": {"` | — |
| [SRC-115C2027D9-L000008](../../railway.json#L8) | 8 | `"    \"startCommand\": \"sh -c 'python -m cli.omarai serve --host 0.0.0.0 --port ${PORT:-8000}'\","` | — |
| [SRC-115C2027D9-L000009](../../railway.json#L9) | 9 | `"    \"healthcheckPath\": \"/api/health\","` | — |
| [SRC-115C2027D9-L000010](../../railway.json#L10) | 10 | `"    \"healthcheckTimeout\": 120,"` | — |
| [SRC-115C2027D9-L000011](../../railway.json#L11) | 11 | `"    \"restartPolicyType\": \"ON_FAILURE\","` | — |
| [SRC-115C2027D9-L000012](../../railway.json#L12) | 12 | `"    \"restartPolicyMaxRetries\": 5"` | — |
| [SRC-115C2027D9-L000013](../../railway.json#L13) | 13 | `"  }"` | — |
| [SRC-115C2027D9-L000014](../../railway.json#L14) | 14 | `"}"` | — |
## وثائق ونصوص

### FILE-B335630551 — [README.md](../../README.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-B335630551-L000001](../../README.md#L1) | 1 | `"# Omarai — Web Research & Generative Q&A Agent"` | — |
| [SRC-B335630551-L000002](../../README.md#L2) | 2 | `""` | — |
| [SRC-B335630551-L000003](../../README.md#L3) | 3 | `"> **Foundational engineering requirements:** mandatory contributor/agent rules are in [AGENTS.md](AGENTS.md). The core architecture and security charter is [OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md](docs/OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md); the expanded platform practices across reliability, security, privacy, data, SRE, AI, accessibility, supply chain, and cost are in [OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md](docs/OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md); and the requirement IDs, expert-review lenses, evidence model, risk priorities, maturity stages, and release gates are in [OMARAI_REQUIREMENTS_TRACEABILITY_AND_MATURITY_MODEL_AR.md](docs/OMARAI_REQUIREMENTS_TRACEABILITY_AND_MATURITY_MODEL_AR.md). The initial foundational requirements checklist is [OMARAI_REQUIREMENTS_REGISTER.md](docs/OMARAI_REQUIREMENTS_REGISTER.md). These documents define required direction; they do not prove every control is implemented or tested. Use the [documentation index](docs/README.md) to find the current source of truth for each topic."` | — |
| [SRC-B335630551-L000004](../../README.md#L4) | 4 | `""` | — |
| [SRC-B335630551-L000005](../../README.md#L5) | 5 | `"Omarai is an Arabic-first web research agent with a responsive RTL chat UI. You can ask open-ended questions in natural language, search the public web, extract text from accessible pages, compare and summarize findings, ask follow-up questions, and inspect the source links."` | — |
| [SRC-B335630551-L000006](../../README.md#L6) | 6 | `""` | — |
| [SRC-B335630551-L000007](../../README.md#L7) | 7 | `"## What this version does"` | — |
| [SRC-B335630551-L000008](../../README.md#L8) | 8 | `""` | — |
| [SRC-B335630551-L000009](../../README.md#L9) | 9 | `"- Plans up to eight search queries from a natural-language question with a dedicated reasoning/planning model, and uses a deterministic multi-query fallback when the model is unavailable."` | — |
| [SRC-B335630551-L000010](../../README.md#L10) | 10 | `"- Uses separate model roles by default: NVIDIA Nemotron 3 Ultra (free) for query planning and Google Gemma 4 31B Instruct (free) for answer synthesis and the second-pass consistency review; retries with OpenRouter's free-model router if a chosen model fails."` | — |
| [SRC-B335630551-L000011](../../README.md#L11) | 11 | `"- Runs DuckDuckGo HTML and Bing RSS independently for every planned query; can add official Brave Search API and Tavily Search API result indexes when their environment keys are configured; uses Google News RSS for queries judged time-sensitive."` | — |
| [SRC-B335630551-L000012](../../README.md#L12) | 12 | `"- Fuses duplicate results across queries and engines using reciprocal-rank fusion, preserving provider, query, domain, platform, publication-date and page-extraction provenance."` | — |
| [SRC-B335630551-L000013](../../README.md#L13) | 13 | `"- Extracts text from up to eight accessible public pages per question with request-size and timeout bounds, following at most three individually validated public redirects."` | — |
| [SRC-B335630551-L000014](../../README.md#L14) | 14 | ``"- Searches public Reddit RSS and the Bluesky public search endpoint when social discussion is relevant; can use Reddit's OAuth API when `REDDIT_CLIENT_ID` and `REDDIT_CLIENT_SECRET` are provided."`` | — |
| [SRC-B335630551-L000015](../../README.md#L15) | 15 | `"- Searches indexed public pages on Facebook, Instagram, X, TikTok, LinkedIn, Threads and YouTube through the general web engines."` | — |
| [SRC-B335630551-L000016](../../README.md#L16) | 16 | `"- Can use the official Meta Graph API to read posts and a small sample of public comments from explicitly configured Facebook Pages when the token has suitable permissions."` | — |
| [SRC-B335630551-L000017](../../README.md#L17) | 17 | ``"- Can use Instagram Graph API hashtag search to read public hashtag media when `INSTAGRAM_USER_ID` and `INSTAGRAM_ACCESS_TOKEN` have the required permissions. It is not a global Instagram search and has platform quotas."`` | — |
| [SRC-B335630551-L000018](../../README.md#L18) | 18 | ``"- Can use the official X recent-post endpoint when `X_BEARER_TOKEN` is configured and the account/API tier permits the request; can use the official YouTube Data API when `YOUTUBE_API_KEY` is configured."`` | — |
| [SRC-B335630551-L000019](../../README.md#L19) | 19 | `"- Generates an evidence-grounded answer in the user's language, showing source links, query plan, provider coverage, direct page reads, platform mix, source/domain diversity, date coverage, and evidence-coverage warnings. Coverage indicators describe breadth and inspectability; they are not probabilities that the answer is true."` | — |
| [SRC-B335630551-L000020](../../README.md#L20) | 20 | `"- Carries up to eight recent chat messages from the current browser session into follow-up questions."` | — |
| [SRC-B335630551-L000021](../../README.md#L21) | 21 | ``"- Keeps the existing local SQLite lead workspace at `/leads`."`` | — |
| [SRC-B335630551-L000022](../../README.md#L22) | 22 | `"- Binds to loopback by default; it is not a public production deployment."` | — |
| [SRC-B335630551-L000023](../../README.md#L23) | 23 | `""` | — |
| [SRC-B335630551-L000024](../../README.md#L24) | 24 | ``"**Verification semantics:** `GET /api/health` is a configuration/dependency snapshot, not proof that search providers or the model are reachable. Check the `agent.verification_scope` field to see what is and is not verified. Use the protected `POST /api/diagnostics` endpoint for explicit live search/model probes; a passed diagnostic only verifies the specific probes run at that time, not every optional connector or answer quality."`` | — |
| [SRC-B335630551-L000025](../../README.md#L25) | 25 | `""` | — |
| [SRC-B335630551-L000026](../../README.md#L26) | 26 | `"This is a tool-using research agent built around existing language models, not a foundation model trained from scratch. The role-specific defaults aim for more consistent behaviour than using a router that selects a different free model at random on each call. Exact availability and response quality still depend on OpenRouter/provider conditions. **Privacy warning:** the user's question, conversation context and selected web excerpts are sent to the configured external language-model provider for planning/synthesis/review. OpenRouter's NVIDIA Nemotron free endpoint states that session data may be logged for security and product improvement; do not send passwords, API keys, private information or personal/confidential customer data through the free endpoint. See the [NVIDIA Nemotron free-endpoint privacy notice](https://openrouter.ai/nvidia/nemotron-3-ultra-550b-a55b:free). Its language-model planner decides how to search, but query count, URLs and result shapes are validated by deterministic code. Cross-engine agreement improves discovery and ranking but is not independent fact verification. Public social pages that require login, blocked pages and private profiles are not fetched; social search cannot promise complete coverage of any platform. Direct official-platform access varies: Reddit API access requires approved app credentials and is subject to Reddit's terms; Facebook Pages reads require a valid token, page identifiers and correct permissions; Instagram hashtag search requires a professional Instagram account token and the specific supported permissions; X API access requires an authorized bearer token and suitable access; YouTube direct API search requires a Google API key. These APIs do not grant universal access to all content, accounts or comments. Review each platform's terms, quotas and permitted use before using the agent commercially. The agent never bypasses login, paywall or access controls and does not send messages or make automated contact with people."` | — |
| [SRC-B335630551-L000027](../../README.md#L27) | 27 | `""` | — |
| [SRC-B335630551-L000028](../../README.md#L28) | 28 | `""` | — |
| [SRC-B335630551-L000029](../../README.md#L29) | 29 | `"## Living repository index"` | — |
| [SRC-B335630551-L000030](../../README.md#L30) | 30 | `""` | — |
| [SRC-B335630551-L000031](../../README.md#L31) | 31 | `"**Current delivery gate (Arabic):** [OMARAI HANDOFF CHECKLIST](docs/OMARAI_HANDOFF_CHECKLIST_AR.md) — current release blockers, required evidence, and operator actions. The central [remediation register](docs/OMARAI_REMEDIATION_REGISTER_AR.md) remains the detailed issue history."` | — |
| [SRC-B335630551-L000032](../../README.md#L32) | 32 | `""` | — |
| [SRC-B335630551-L000033](../../README.md#L33) | 33 | `"Omarai maintains a categorized master index and a paginated, line-by-line source index:"` | — |
| [SRC-B335630551-L000034](../../README.md#L34) | 34 | `""` | — |
| [SRC-B335630551-L000035](../../README.md#L35) | 35 | ``"- [MASTER INDEX](docs/MASTER_INDEX.md): file inventory with stable file IDs, Python AST definitions, static frontend/configuration symbols, and explicitly marked TODO/FIXME/BUG/HACK/XXX/REVIEW/SECURITY/DEPRECATED/ISSUE/DEFECT/REGRESSION/RISK/GAP/ERROR/WARNING/PERF/PRIVACY/DATA_LOSS/ACCESSIBILITY entries. Each review marker has an `FND-...` code and a link to the exact source line."`` | — |
| [SRC-B335630551-L000036](../../README.md#L36) | 36 | `"- [SOURCE LINES INDEX](docs/SOURCE_LINES_INDEX.md): search-friendly directory of files, page links, per-file line counts, and links to each source line."` | — |
| [SRC-B335630551-L000037](../../README.md#L37) | 37 | `"- [INDEX COVERAGE AUDIT](docs/INDEX_COVERAGE_AUDIT.md): generated evidence of line-count consistency, metadata-only files, excluded path names and their reasons, and the exact scope of any “100%” coverage statement."` | — |
| [SRC-B335630551-L000038](../../README.md#L38) | 38 | ``"- [Source line pages](docs/source_index/): small generated pages containing every logical line from eligible readable text files. Each line has a `SRC-<FILEHASH>-L000001` code, exact JSON-escaped text, and a link back to the source file at the matching line. Pages are capped at 800 line records to remain navigable on mobile and in GitHub's web view."`` | — |
| [SRC-B335630551-L000039](../../README.md#L39) | 39 | `"- [Local source search](docs/search_code.py): offline text/regex search with file, line, nearby context, and GitHub line links. It excludes common secret/configuration files, databases, key files, symlinks, and runtime directories; it does not detect every secret or replace a security audit."` | — |
| [SRC-B335630551-L000040](../../README.md#L40) | 40 | `""` | — |
| [SRC-B335630551-L000041](../../README.md#L41) | 41 | ``"Example: `python docs/search_code.py \"resolve_followup_query\" --ext py --context 2`."`` | — |
| [SRC-B335630551-L000042](../../README.md#L42) | 42 | `""` | — |
| [SRC-B335630551-L000043](../../README.md#L43) | 43 | ``"The generator now refuses to publish indexes if any eligible file has missing, duplicated, or misnumbered source-line records. It still cannot infer every unmarked logical/programming defect; known issues should be recorded explicitly with a supported marker (for example, `# BUG: explain the defect`) so the generated `FND-...` register can point to the corresponding `SRC-...` line."`` | — |
| [SRC-B335630551-L000044](../../README.md#L44) | 44 | `""` | — |
| [SRC-B335630551-L000045](../../README.md#L45) | 45 | `"Regenerate and verify the indexes locally:"` | — |
| [SRC-B335630551-L000046](../../README.md#L46) | 46 | `""` | — |
| [SRC-B335630551-L000047](../../README.md#L47) | 47 | ````"```bash"```` | — |
| [SRC-B335630551-L000048](../../README.md#L48) | 48 | `"python docs/generate_index.py"` | — |
| [SRC-B335630551-L000049](../../README.md#L49) | 49 | `"python docs/generate_index.py --check"` | — |
| [SRC-B335630551-L000050](../../README.md#L50) | 50 | ````"```"```` | — |
| [SRC-B335630551-L000051](../../README.md#L51) | 51 | `""` | — |
| [SRC-B335630551-L000052](../../README.md#L52) | 52 | ``"GitHub Actions validates the generator on Python 3.11 and 3.12. The publishing workflow runs on pushes to `main` and the `feat/**`, `fix/**`, and `feature/**` branches. It regenerates and commits all indexes and generated pages only when output changes; obsolete generated pages are removed, while generated-index-only commits are ignored to avoid loops. Documentation-only and repository-hygiene branches are still tested with indexes regenerated in the isolated test workspace, but do not carry a large generated-page diff solely because documentation lines moved; after merge, the publisher refreshes the committed indexes on `main`. If direct publication to `main` is rejected, it opens a pull request instead of force-updating a branch or auto-merging."`` | — |
| [SRC-B335630551-L000053](../../README.md#L53) | 53 | `""` | — |
| [SRC-B335630551-L000054](../../README.md#L54) | 54 | ``"When a known code issue is found, add a source comment using one supported marker name (TODO, FIXME, BUG, HACK, XXX, REVIEW, SECURITY, DEPRECATED, ISSUE, DEFECT, REGRESSION, RISK, GAP, ERROR, WARNING, PERF, PRIVACY, DATA_LOSS, or ACCESSIBILITY), followed by a colon and a concise description. The index assigns an `FND-...` code and links it to the exact `SRC-...` source-line record; removing or editing that source annotation updates the generated register on the next index run. Coverage includes every logical line in eligible readable text files up to 2 MiB. Known local secrets, runtime databases, dependency/build directories, binary/unreadable files and oversized files are excluded from line-level indexing by design but listed by metadata where eligible. Static review markers help track explicit findings; no source index can prove that every arbitrary logic bug has been detected or that all code is correct."`` | — |
| [SRC-B335630551-L000055](../../README.md#L55) | 55 | `""` | — |
| [SRC-B335630551-L000056](../../README.md#L56) | 56 | `"## Per-request resource budget"` | — |
| [SRC-B335630551-L000057](../../README.md#L57) | 57 | `""` | — |
| [SRC-B335630551-L000058](../../README.md#L58) | 58 | ``"Each `POST /api/agent` answer includes a `request_budget` object with elapsed and remaining time, reserved resource counts, and configured limits. The current defaults are a 90-second cooperative deadline, at most 8 search queries, 32 provider search calls, 8 model HTTP attempts, 8 page fetches, and up to 3 optional server-side search-tool calls per request. Operator limits may be lowered or raised only within hard caps: `OMARAI_REQUEST_BUDGET_SECONDS` (10–120), `OMARAI_REQUEST_MAX_SEARCH_QUERIES` (1–8), `OMARAI_REQUEST_MAX_SEARCH_CALLS` (1–40), `OMARAI_REQUEST_MAX_MODEL_CALLS` (1–12), `OMARAI_REQUEST_MAX_PAGE_FETCHES` (1–8), and `OMARAI_REQUEST_MAX_TOOL_CALLS` (0–3). Invalid numeric values fall back to the defaults; out-of-range values are clamped."`` | — |
| [SRC-B335630551-L000059](../../README.md#L59) | 59 | `""` | — |
| [SRC-B335630551-L000060](../../README.md#L60) | 60 | `"The deadline caps the timeout passed to outbound operations and prevents new work from being reserved after the deadline or a resource cap is exhausted. It is **cooperative, not hard cancellation**: a network call already in progress may overrun slightly while its client unwinds. Do not interpret this metadata as a load test, a throughput guarantee, or proof that any live provider is reachable. CI tests for budget logic are separate from live-provider validation."` | — |
| [SRC-B335630551-L000061](../../README.md#L61) | 61 | `""` | — |
| [SRC-B335630551-L000062](../../README.md#L62) | 62 | ``"The HTTP ingress caps active handler connections at 32 per process by default through `OMARAI_MAX_CONCURRENT_HTTP_CONNECTIONS` (bounded to 1–128). When all slots are occupied, excess sockets receive HTTP 503 with `Retry-After: 5` before a handler thread is created. The in-memory rate limiter also caps client buckets at 4,096 per process; new identities beyond that ceiling share a conservative overflow quota. Separately, expensive `/api/agent` and `/api/diagnostics` operations remain limited to at most 4 concurrent operations per process by default; configure `OMARAI_MAX_CONCURRENT_AGENT_REQUESTS` from 1 to 8. These are **process-local** controls, not distributed limits across workers or replicas, and they are not throughput/load-test claims."`` | — |
| [SRC-B335630551-L000063](../../README.md#L63) | 63 | `""` | — |
| [SRC-B335630551-L000064](../../README.md#L64) | 64 | `"## Experimental DeepSeek Search provider"` | — |
| [SRC-B335630551-L000065](../../README.md#L65) | 65 | `""` | — |
| [SRC-B335630551-L000066](../../README.md#L66) | 66 | `"Omarai can optionally compare results from DeepSeek's Search API when"` | — |
| [SRC-B335630551-L000067](../../README.md#L67) | 67 | ``"`DEEPSEEK_SEARCH_API_KEY` is configured in the host's secret settings. It is"`` | — |
| [SRC-B335630551-L000068](../../README.md#L68) | 68 | `"**disabled by default**; DuckDuckGo and Bing remain configured as before."` | — |
| [SRC-B335630551-L000069](../../README.md#L69) | 69 | `"To limit possible spend when opted in, the request budget defaults to **one"` | — |
| [SRC-B335630551-L000070](../../README.md#L70) | 70 | `"DeepSeek Search call per answer/diagnostic operation**. It can be set from 0 to 3"` | — |
| [SRC-B335630551-L000071](../../README.md#L71) | 71 | ``"using `OMARAI_DEEPSEEK_SEARCH_REQUEST_BUDGET`; invalid values fall back to 1."`` | — |
| [SRC-B335630551-L000072](../../README.md#L72) | 72 | `"DeepSeek Search is billed per successful request (currently documented at"` | — |
| [SRC-B335630551-L000073](../../README.md#L73) | 73 | `"US$0.75 per 1,000 successful searches); review the"` | — |
| [SRC-B335630551-L000074](../../README.md#L74) | 74 | `"[official Search & Fetch guide](https://api-docs.deepseek.com/guides/search/)"` | — |
| [SRC-B335630551-L000075](../../README.md#L75) | 75 | `"before enabling it. Unit tests use a mocked response; this repository change"` | — |
| [SRC-B335630551-L000076](../../README.md#L76) | 76 | `"does not claim live DeepSeek connectivity or answer-quality improvement."` | — |
| [SRC-B335630551-L000077](../../README.md#L77) | 77 | `""` | — |
| [SRC-B335630551-L000078](../../README.md#L78) | 78 | `"## Hosting and live acceptance"` | — |
| [SRC-B335630551-L000079](../../README.md#L79) | 79 | `""` | — |
| [SRC-B335630551-L000080](../../README.md#L80) | 80 | `"Omarai includes several **alternative** hosting paths. Choose one provider; the presence of a config file is not proof that a service exists or has passed acceptance."` | — |
| [SRC-B335630551-L000081](../../README.md#L81) | 81 | `""` | — |
| [SRC-B335630551-L000082](../../README.md#L82) | 82 | ``"- **Railway:** [Arabic deployment guide](docs/DEPLOY_RAILWAY_AR.md), using `railway.json`."`` | — |
| [SRC-B335630551-L000083](../../README.md#L83) | 83 | `"- **SnapDeploy:** [free-demo guide](docs/DEPLOY_SNAPDEPLOY_AR.md). Confirm current quotas and terms before use; ephemeral storage means it is not a durable lead database."` | — |
| [SRC-B335630551-L000084](../../README.md#L84) | 84 | ``"- **Render:** [optional alternative guide](docs/DEPLOY_RENDER_AR.md), using `render.yaml`. Use it only if the provider/account is available to you."`` | — |
| [SRC-B335630551-L000085](../../README.md#L85) | 85 | `""` | — |
| [SRC-B335630551-L000086](../../README.md#L86) | 86 | ``"All providers share the same acceptance rules. The API reports a validated source revision at `/api/health`: it prefers image-baked `BUILD_SHA`, then documented platform Git metadata where supported. For another Docker host, pass `--build-arg OMARAI_BUILD_SHA=\"$(git rev-parse HEAD)\"`. A local/container build is not evidence of a live deployment; compare the reported SHA with the exact intended commit."`` | — |
| [SRC-B335630551-L000087](../../README.md#L87) | 87 | `""` | — |
| [SRC-B335630551-L000088](../../README.md#L88) | 88 | `"**Single-operator limit:** the current bearer token is shared application access, not individual identity or a tenant boundary. The lead workspace does not provide confirmed per-customer data isolation. Keep a hosted instance private to one operator; do not store confidential records for multiple customers. Concurrency and rate-limit state are process-local, not distributed. The new HTTP handler and client-bucket ceilings bound per-process growth, but do not establish production load capacity or per-tenant isolation."` | — |
| [SRC-B335630551-L000089](../../README.md#L89) | 89 | `""` | — |
| [SRC-B335630551-L000090](../../README.md#L90) | 90 | ``"For a public-bound instance, set `OMARAI_PUBLIC_DEPLOYMENT=1` and a separate random `OMARAI_ACCESS_TOKEN` of at least 32 characters. The app refuses public binding without both. Configure `OPENROUTER_API_KEY` or `OMARAI_LLM_API_KEY` only in the provider's secret store. If the UI is on another origin, set `OMARAI_ALLOWED_ORIGINS` to the exact trusted origins (scheme, host, optional port; no path or wildcard). The built-in UI served from the same host usually needs no extra origin entry. Public API routes require the bearer token and apply a default in-memory per-client IP limit of 20 requests per minute. The browser stores only the app access token in local storage, not the provider API key."`` | — |
| [SRC-B335630551-L000091](../../README.md#L91) | 91 | `""` | — |
| [SRC-B335630551-L000092](../../README.md#L92) | 92 | ``"Before accepting any host, follow the [go-live checklist](docs/GO_LIVE_CHECKLIST_AR.md) and run the manually triggered [hosted acceptance smoke workflow](.github/workflows/hosted-smoke.yml) only after setting GitHub Actions secrets `OMARAI_ACCESS_TOKEN` and `OMARAI_BASE_URL` to the authorized service. The workflow makes real model/search calls and may incur usage charges; do not run it without human approval. On hosts with a genuinely persistent mounted volume, set `OMARAI_DB_PATH` to a file inside the mount (for example, `/data/omarai.sqlite3`). This setting selects a path; it does not create storage or replace backups and a tested restore. Keep the lead workspace disabled for important records until persistence across restart/redeploy and restore are verified on the actual host."`` | — |
| [SRC-B335630551-L000093](../../README.md#L93) | 93 | `""` | — |
| [SRC-B335630551-L000094](../../README.md#L94) | 94 | `"## Run on Android / Termux"` | — |
| [SRC-B335630551-L000095](../../README.md#L95) | 95 | `""` | — |
| [SRC-B335630551-L000096](../../README.md#L96) | 96 | `"From the repository directory:"` | — |
| [SRC-B335630551-L000097](../../README.md#L97) | 97 | `""` | — |
| [SRC-B335630551-L000098](../../README.md#L98) | 98 | ````"```bash"```` | — |
| [SRC-B335630551-L000099](../../README.md#L99) | 99 | `"python -m pip install -e ."` | — |
| [SRC-B335630551-L000100](../../README.md#L100) | 100 | ````"```"```` | — |
| [SRC-B335630551-L000101](../../README.md#L101) | 101 | `""` | — |
| [SRC-B335630551-L000102](../../README.md#L102) | 102 | ``"The default language-model configuration uses OpenRouter: Nemotron 3 Ultra (free) plans queries, Gemma 4 31B Instruct (free) writes the answer and performs the optional second-pass review, and `openrouter/free` is the fallback if a selected model fails. Create an OpenRouter API key, then enter it without putting the secret into a command-history entry. The model key enables both search planning and generative synthesis; general web search can still run without it, but results will not be turned into a full language-model analysis:"`` | — |
| [SRC-B335630551-L000103](../../README.md#L103) | 103 | `""` | — |
| [SRC-B335630551-L000104](../../README.md#L104) | 104 | ````"```bash"```` | — |
| [SRC-B335630551-L000105](../../README.md#L105) | 105 | `"read -r -s -p \"OpenRouter API key: \" OPENROUTER_API_KEY"` | — |
| [SRC-B335630551-L000106](../../README.md#L106) | 106 | `"printf '\\n'"` | — |
| [SRC-B335630551-L000107](../../README.md#L107) | 107 | `"export OPENROUTER_API_KEY"` | — |
| [SRC-B335630551-L000108](../../README.md#L108) | 108 | `"python -m cli.omarai serve"` | — |
| [SRC-B335630551-L000109](../../README.md#L109) | 109 | ````"```"```` | — |
| [SRC-B335630551-L000110](../../README.md#L110) | 110 | `""` | — |
| [SRC-B335630551-L000111](../../README.md#L111) | 111 | `"Keep this Termux session running and open **http://127.0.0.1:8765** in the phone's browser. The agent chat is the home screen. The existing lead workspace remains available at **http://127.0.0.1:8765/leads**."` | — |
| [SRC-B335630551-L000112](../../README.md#L112) | 112 | `""` | — |
| [SRC-B335630551-L000113](../../README.md#L113) | 113 | `"The key is held in the current shell environment and is not written into the repository. Enter it again in a new Termux session. Never commit API keys or paste them into public issues or chat."` | — |
| [SRC-B335630551-L000114](../../README.md#L114) | 114 | `""` | — |
| [SRC-B335630551-L000115](../../README.md#L115) | 115 | `"### Optional configuration"` | — |
| [SRC-B335630551-L000116](../../README.md#L116) | 116 | `""` | — |
| [SRC-B335630551-L000117](../../README.md#L117) | 117 | `"For additional live web-search indexes, configure either official search API. These keys are optional: the built-in public engines are still attempted, and each API may have its own account, quota, rate limit or cost. Do not assume an API is free or that a configured key is valid until you run the live diagnostics."` | — |
| [SRC-B335630551-L000118](../../README.md#L118) | 118 | `""` | — |
| [SRC-B335630551-L000119](../../README.md#L119) | 119 | ````"```bash"```` | — |
| [SRC-B335630551-L000120](../../README.md#L120) | 120 | `"read -r -s -p \"Brave Search API key: \" BRAVE_SEARCH_API_KEY; printf '\\\\n'; export BRAVE_SEARCH_API_KEY"` | — |
| [SRC-B335630551-L000121](../../README.md#L121) | 121 | `"read -r -s -p \"Tavily API key: \" TAVILY_API_KEY; printf '\\\\n'; export TAVILY_API_KEY"` | — |
| [SRC-B335630551-L000122](../../README.md#L122) | 122 | ````"```"```` | — |
| [SRC-B335630551-L000123](../../README.md#L123) | 123 | `""` | — |
| [SRC-B335630551-L000124](../../README.md#L124) | 124 | `""` | — |
| [SRC-B335630551-L000125](../../README.md#L125) | 125 | `"For a different OpenAI-compatible endpoint or model, set these environment variables before starting the server:"` | — |
| [SRC-B335630551-L000126](../../README.md#L126) | 126 | `""` | — |
| [SRC-B335630551-L000127](../../README.md#L127) | 127 | ````"```bash"```` | — |
| [SRC-B335630551-L000128](../../README.md#L128) | 128 | `"export OMARAI_LLM_BASE_URL=\"https://openrouter.ai/api/v1\""` | — |
| [SRC-B335630551-L000129](../../README.md#L129) | 129 | `"export OMARAI_LLM_MODEL=\"openrouter/free\""` | — |
| [SRC-B335630551-L000130](../../README.md#L130) | 130 | ````"```"```` | — |
| [SRC-B335630551-L000131](../../README.md#L131) | 131 | `""` | — |
| [SRC-B335630551-L000132](../../README.md#L132) | 132 | ``"Use `OMARAI_LLM_API_KEY` instead of `OPENROUTER_API_KEY` when you want a separate environment variable. `OMARAI_LLM_TIMEOUT` accepts a timeout in seconds from 5 to 60. To customize model roles, set `OMARAI_PLANNER_MODEL`, `OMARAI_ANSWER_MODEL`, and/or `OMARAI_REVIEW_MODEL`; `OMARAI_LLM_MODEL` remains a global override for all roles that have no role-specific override. `OMARAI_LLM_FALLBACK_MODEL` changes the default `openrouter/free` fallback. Provider pricing, model availability and rate limits can change; check the chosen provider before using a paid model. Optional social credentials may be configured in the same Termux session before starting the server: `REDDIT_CLIENT_ID` + `REDDIT_CLIENT_SECRET` (official OAuth access), `X_BEARER_TOKEN`, `YOUTUBE_API_KEY`, `INSTAGRAM_USER_ID` + `INSTAGRAM_ACCESS_TOKEN` + optional `META_GRAPH_VERSION`, and `FACEBOOK_PAGE_ACCESS_TOKEN` + `FACEBOOK_PAGE_IDS` (comma-separated Page IDs that the authorized token can access). Use `read -r -s` to enter secrets privately rather than saving them in shell history. Do not store keys in source files, HTML, commits or chat messages."`` | — |
| [SRC-B335630551-L000133](../../README.md#L133) | 133 | `""` | — |
| [SRC-B335630551-L000134](../../README.md#L134) | 134 | `"If no language-model key is configured, Omarai can still attempt web search and show source snippets, but it cannot provide the full generative understanding/synthesis layer. If search providers are temporarily unavailable, the agent reports the limitation rather than pretending that a search succeeded."` | — |
| [SRC-B335630551-L000135](../../README.md#L135) | 135 | `""` | — |
| [SRC-B335630551-L000136](../../README.md#L136) | 136 | `"For the platform boundaries, optional credentials and safe Termux setup for social connectors, see the [Arabic research connectors guide](docs/RESEARCH_CONNECTORS_AR.md)."` | — |
| [SRC-B335630551-L000137](../../README.md#L137) | 137 | `""` | — |
| [SRC-B335630551-L000138](../../README.md#L138) | 138 | `"## API"` | — |
| [SRC-B335630551-L000139](../../README.md#L139) | 139 | `""` | — |
| [SRC-B335630551-L000140](../../README.md#L140) | 140 | ``"- `GET /` — web-research chat"`` | — |
| [SRC-B335630551-L000141](../../README.md#L141) | 141 | ``"- `GET /leads` — existing lead workspace"`` | — |
| [SRC-B335630551-L000142](../../README.md#L142) | 142 | ``"- `GET /api/health` — setup and dependency status (never returns the API key)"`` | — |
| [SRC-B335630551-L000143](../../README.md#L143) | 143 | ``"- `POST /api/diagnostics` — opt-in live checks for web search and the language model; set `test_social: true` to also probe public/authorized social connectors"`` | — |
| [SRC-B335630551-L000144](../../README.md#L144) | 144 | ``"- `POST /api/agent` — open-ended question plus optional recent `history`"`` | — |
| [SRC-B335630551-L000145](../../README.md#L145) | 145 | ``"- `POST /api/analyze` — existing rule-based lead-text assessment"`` | — |
| [SRC-B335630551-L000146](../../README.md#L146) | 146 | ``"- `GET/POST /api/leads` — existing local lead records"`` | — |
| [SRC-B335630551-L000147](../../README.md#L147) | 147 | `""` | — |
| [SRC-B335630551-L000148](../../README.md#L148) | 148 | `"Example request:"` | — |
| [SRC-B335630551-L000149](../../README.md#L149) | 149 | `""` | — |
| [SRC-B335630551-L000150](../../README.md#L150) | 150 | ````"```json"```` | — |
| [SRC-B335630551-L000151](../../README.md#L151) | 151 | `"{"` | — |
| [SRC-B335630551-L000152](../../README.md#L152) | 152 | `"  \"question\": \"Compare the latest public information about two technologies\","` | — |
| [SRC-B335630551-L000153](../../README.md#L153) | 153 | `"  \"history\": []"` | — |
| [SRC-B335630551-L000154](../../README.md#L154) | 154 | `"}"` | — |
| [SRC-B335630551-L000155](../../README.md#L155) | 155 | ````"```"```` | — |
| [SRC-B335630551-L000156](../../README.md#L156) | 156 | `""` | — |
| [SRC-B335630551-L000157](../../README.md#L157) | 157 | ``"The `/api/diagnostics` response reports pass/fail/degraded states, returned result counts, provider counts, elapsed time, and the model that actually answered (including fallback use). The Arabic web UI offers automatic, deep, latest-information, and public-social research modes, plus a live-test button. The model check sends one small completion request; optional social checks perform real public/API requests and can take longer. The response from `/api/agent` includes `answer`, `sources`, `search_queries`, `research_plan`, `search_report`, `used_web_search`, `used_social_search`, `used_language_model`, and any warnings. The request can pass `mode` as `auto`, `deep`, `latest`, or `social`. The report records planned and attempted queries, unique result count, pages read, providers, platform breakdown, citation-range checks and whether an optional second-pass consistency review completed. That second pass uses the same configured model/provider and is not independent fact verification. URL syntax and resolved private/local addresses are checked before page fetches; public redirects are followed only through a small bounded loop with each destination revalidated. Search engines may still return inaccessible, stale or noisy results, which the agent must disclose."`` | — |
| [SRC-B335630551-L000158](../../README.md#L158) | 158 | `""` | — |
| [SRC-B335630551-L000159](../../README.md#L159) | 159 | `"## Existing lead workspace"` | — |
| [SRC-B335630551-L000160](../../README.md#L160) | 160 | `""` | — |
| [SRC-B335630551-L000161](../../README.md#L161) | 161 | ``"The previous local lead-intent tool is preserved at `/leads`. It stores data locally in `~/.omarai/omarai.sqlite3`. Its transparent rule score is not a statistical probability of a purchase. Process only public/authorized data, minimize personal information, and manually review business decisions."`` | — |
| [SRC-B335630551-L000162](../../README.md#L162) | 162 | `""` | — |
| [SRC-B335630551-L000163](../../README.md#L163) | 163 | `"Analyze text from the CLI:"` | — |
| [SRC-B335630551-L000164](../../README.md#L164) | 164 | `""` | — |
| [SRC-B335630551-L000165](../../README.md#L165) | 165 | ````"```bash"```` | — |
| [SRC-B335630551-L000166](../../README.md#L166) | 166 | `"python -m cli.omarai analyze --text \"بدور على شقة في التجمع الخامس وممكن معاينة\" --product \"شقة,عقار\" --location \"التجمع الخامس\""` | — |
| [SRC-B335630551-L000167](../../README.md#L167) | 167 | ````"```"```` | — |
| [SRC-B335630551-L000168](../../README.md#L168) | 168 | `""` | — |
| [SRC-B335630551-L000169](../../README.md#L169) | 169 | ``"CSV import requires `text,source_url,platform` columns:"`` | — |
| [SRC-B335630551-L000170](../../README.md#L170) | 170 | `""` | — |
| [SRC-B335630551-L000171](../../README.md#L171) | 171 | ````"```bash"```` | — |
| [SRC-B335630551-L000172](../../README.md#L172) | 172 | `"python -m cli.omarai import-csv --file leads.csv"` | — |
| [SRC-B335630551-L000173](../../README.md#L173) | 173 | `"python -m cli.omarai list --limit 50"` | — |
| [SRC-B335630551-L000174](../../README.md#L174) | 174 | `"python -m cli.omarai export-csv --file leads-export.csv"` | — |
| [SRC-B335630551-L000175](../../README.md#L175) | 175 | ````"```"```` | — |
| [SRC-B335630551-L000176](../../README.md#L176) | 176 | `""` | — |
| [SRC-B335630551-L000177](../../README.md#L177) | 177 | `"## Checks"` | — |
| [SRC-B335630551-L000178](../../README.md#L178) | 178 | `""` | — |
| [SRC-B335630551-L000179](../../README.md#L179) | 179 | ````"```bash"```` | — |
| [SRC-B335630551-L000180](../../README.md#L180) | 180 | `"python -m pip install -e \".[dev]\""` | — |
| [SRC-B335630551-L000181](../../README.md#L181) | 181 | `"ruff check agents api cli tests"` | — |
| [SRC-B335630551-L000182](../../README.md#L182) | 182 | `"python -m pytest -q"` | — |
| [SRC-B335630551-L000183](../../README.md#L183) | 183 | ````"```"```` | — |
## إعدادات وتشغيل

### FILE-A64CF250B4 — [render.yaml](../../render.yaml#L1)

- النوع: **YAML**
- نطاق الفهرسة: جرد الملف + مفاتيح إعداد ساكنة

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-A64CF250B4-L000001](../../render.yaml#L1) | 1 | `"services:"` | — |
| [SRC-A64CF250B4-L000002](../../render.yaml#L2) | 2 | `"  - type: web"` | — |
| [SRC-A64CF250B4-L000003](../../render.yaml#L3) | 3 | `"    name: omarai"` | — |
| [SRC-A64CF250B4-L000004](../../render.yaml#L4) | 4 | `"    runtime: docker"` | — |
| [SRC-A64CF250B4-L000005](../../render.yaml#L5) | 5 | `"    plan: free"` | — |
| [SRC-A64CF250B4-L000006](../../render.yaml#L6) | 6 | `"    region: frankfurt"` | — |
| [SRC-A64CF250B4-L000007](../../render.yaml#L7) | 7 | `"    dockerfilePath: ./Dockerfile"` | — |
| [SRC-A64CF250B4-L000008](../../render.yaml#L8) | 8 | `"    healthCheckPath: /api/health"` | — |
| [SRC-A64CF250B4-L000009](../../render.yaml#L9) | 9 | `"    envVars:"` | — |
| [SRC-A64CF250B4-L000010](../../render.yaml#L10) | 10 | `"      - key: OMARAI_PUBLIC_DEPLOYMENT"` | — |
| [SRC-A64CF250B4-L000011](../../render.yaml#L11) | 11 | `"        value: \"1\""` | — |
| [SRC-A64CF250B4-L000012](../../render.yaml#L12) | 12 | `"      - key: OMARAI_ACCESS_TOKEN"` | — |
| [SRC-A64CF250B4-L000013](../../render.yaml#L13) | 13 | `"        sync: false"` | — |
| [SRC-A64CF250B4-L000014](../../render.yaml#L14) | 14 | `"      - key: OPENROUTER_API_KEY"` | — |
| [SRC-A64CF250B4-L000015](../../render.yaml#L15) | 15 | `"        sync: false"` | — |
## ملفات أخرى

### FILE-64EDD7FC2B — [scripts/__init__.py](../../scripts/__init__.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-64EDD7FC2B-L000001](../../scripts/__init__.py#L1) | 1 | `"\"\"\"Operational helper scripts for Omarai.\"\"\""` | — |
## ملفات أخرى

### FILE-70795F4B61 — [scripts/compare_answer_quality_runs.py](../../scripts/compare_answer_quality_runs.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-70795F4B61-L000001](../../scripts/compare_answer_quality_runs.py#L1) | 1 | `"\"\"\"Compare two Omarai benchmark runs without inventing quality or cost measurements."` | — |
| [SRC-70795F4B61-L000002](../../scripts/compare_answer_quality_runs.py#L2) | 2 | `""` | — |
| [SRC-70795F4B61-L000003](../../scripts/compare_answer_quality_runs.py#L3) | 3 | `"Runtime measurements come from explicit run telemetry. Factual accuracy, retrieval"` | — |
| [SRC-70795F4B61-L000004](../../scripts/compare_answer_quality_runs.py#L4) | 4 | `"precision/recall, faithfulness, citation support, and writing quality require matching"` | — |
| [SRC-70795F4B61-L000005](../../scripts/compare_answer_quality_runs.py#L5) | 5 | `"human-review files; missing annotations remain unscored. The comparator is offline."` | — |
| [SRC-70795F4B61-L000006](../../scripts/compare_answer_quality_runs.py#L6) | 6 | `"\"\"\""` | — |
| [SRC-70795F4B61-L000007](../../scripts/compare_answer_quality_runs.py#L7) | 7 | `"from __future__ import annotations"` | — |
| [SRC-70795F4B61-L000008](../../scripts/compare_answer_quality_runs.py#L8) | 8 | `""` | — |
| [SRC-70795F4B61-L000009](../../scripts/compare_answer_quality_runs.py#L9) | 9 | `"import argparse"` | — |
| [SRC-70795F4B61-L000010](../../scripts/compare_answer_quality_runs.py#L10) | 10 | `"import importlib.util"` | — |
| [SRC-70795F4B61-L000011](../../scripts/compare_answer_quality_runs.py#L11) | 11 | `"import json"` | — |
| [SRC-70795F4B61-L000012](../../scripts/compare_answer_quality_runs.py#L12) | 12 | `"import math"` | — |
| [SRC-70795F4B61-L000013](../../scripts/compare_answer_quality_runs.py#L13) | 13 | `"import re"` | — |
| [SRC-70795F4B61-L000014](../../scripts/compare_answer_quality_runs.py#L14) | 14 | `"import sys"` | — |
| [SRC-70795F4B61-L000015](../../scripts/compare_answer_quality_runs.py#L15) | 15 | `"from pathlib import Path"` | — |
| [SRC-70795F4B61-L000016](../../scripts/compare_answer_quality_runs.py#L16) | 16 | `"from typing import Any"` | — |
| [SRC-70795F4B61-L000017](../../scripts/compare_answer_quality_runs.py#L17) | 17 | `""` | — |
| [SRC-70795F4B61-L000018](../../scripts/compare_answer_quality_runs.py#L18) | 18 | `"ROOT = Path(__file__).resolve().parents[1]"` | — |
| [SRC-70795F4B61-L000019](../../scripts/compare_answer_quality_runs.py#L19) | 19 | `"DEFAULT_CORPUS = ROOT / \"tests\" / \"fixtures\" / \"answer_quality_cases.json\""` | — |
| [SRC-70795F4B61-L000020](../../scripts/compare_answer_quality_runs.py#L20) | 20 | `"REQUIRED_RUN_FIELDS = {\"benchmark_id\", \"benchmark_version\", \"results\"}"` | — |
| [SRC-70795F4B61-L000021](../../scripts/compare_answer_quality_runs.py#L21) | 21 | `""` | — |
| [SRC-70795F4B61-L000022](../../scripts/compare_answer_quality_runs.py#L22) | 22 | `""` | — |
| [SRC-70795F4B61-L000023](../../scripts/compare_answer_quality_runs.py#L23) | 23 | `"def load_json_object(path: Path) -> dict[str, Any]:"` | — |
| [SRC-70795F4B61-L000024](../../scripts/compare_answer_quality_runs.py#L24) | 24 | `"    if not path.is_file():"` | — |
| [SRC-70795F4B61-L000025](../../scripts/compare_answer_quality_runs.py#L25) | 25 | `"        raise FileNotFoundError(\"Input file not found: \" + str(path))"` | — |
| [SRC-70795F4B61-L000026](../../scripts/compare_answer_quality_runs.py#L26) | 26 | `"    data = json.loads(path.read_text(encoding=\"utf-8\"))"` | — |
| [SRC-70795F4B61-L000027](../../scripts/compare_answer_quality_runs.py#L27) | 27 | `"    if not isinstance(data, dict):"` | — |
| [SRC-70795F4B61-L000028](../../scripts/compare_answer_quality_runs.py#L28) | 28 | `"        raise TypeError(\"JSON root must be an object: \" + str(path))"` | — |
| [SRC-70795F4B61-L000029](../../scripts/compare_answer_quality_runs.py#L29) | 29 | `"    return data"` | — |
| [SRC-70795F4B61-L000030](../../scripts/compare_answer_quality_runs.py#L30) | 30 | `""` | — |
| [SRC-70795F4B61-L000031](../../scripts/compare_answer_quality_runs.py#L31) | 31 | `""` | — |
| [SRC-70795F4B61-L000032](../../scripts/compare_answer_quality_runs.py#L32) | 32 | `"def _finite_nonnegative(value: Any) -> float \| None:"` | — |
| [SRC-70795F4B61-L000033](../../scripts/compare_answer_quality_runs.py#L33) | 33 | `"    if isinstance(value, bool) or not isinstance(value, (int, float)):"` | — |
| [SRC-70795F4B61-L000034](../../scripts/compare_answer_quality_runs.py#L34) | 34 | `"        return None"` | — |
| [SRC-70795F4B61-L000035](../../scripts/compare_answer_quality_runs.py#L35) | 35 | `"    number = float(value)"` | — |
| [SRC-70795F4B61-L000036](../../scripts/compare_answer_quality_runs.py#L36) | 36 | `"    if not math.isfinite(number) or number < 0:"` | — |
| [SRC-70795F4B61-L000037](../../scripts/compare_answer_quality_runs.py#L37) | 37 | `"        return None"` | — |
| [SRC-70795F4B61-L000038](../../scripts/compare_answer_quality_runs.py#L38) | 38 | `"    return number"` | — |
| [SRC-70795F4B61-L000039](../../scripts/compare_answer_quality_runs.py#L39) | 39 | `""` | — |
| [SRC-70795F4B61-L000040](../../scripts/compare_answer_quality_runs.py#L40) | 40 | `""` | — |
| [SRC-70795F4B61-L000041](../../scripts/compare_answer_quality_runs.py#L41) | 41 | `"def validate_run(run: dict[str, Any], label: str) -> list[str]:"` | — |
| [SRC-70795F4B61-L000042](../../scripts/compare_answer_quality_runs.py#L42) | 42 | `"    problems: list[str] = []"` | — |
| [SRC-70795F4B61-L000043](../../scripts/compare_answer_quality_runs.py#L43) | 43 | `"    missing = REQUIRED_RUN_FIELDS - set(run)"` | — |
| [SRC-70795F4B61-L000044](../../scripts/compare_answer_quality_runs.py#L44) | 44 | `"    if missing:"` | — |
| [SRC-70795F4B61-L000045](../../scripts/compare_answer_quality_runs.py#L45) | 45 | `"        problems.append(f\"{label}: missing run fields {sorted(missing)}\")"` | — |
| [SRC-70795F4B61-L000046](../../scripts/compare_answer_quality_runs.py#L46) | 46 | `"    results = run.get(\"results\")"` | — |
| [SRC-70795F4B61-L000047](../../scripts/compare_answer_quality_runs.py#L47) | 47 | `"    if not isinstance(results, list) or not results:"` | — |
| [SRC-70795F4B61-L000048](../../scripts/compare_answer_quality_runs.py#L48) | 48 | `"        problems.append(f\"{label}: results must be a non-empty array\")"` | — |
| [SRC-70795F4B61-L000049](../../scripts/compare_answer_quality_runs.py#L49) | 49 | `"        return problems"` | — |
| [SRC-70795F4B61-L000050](../../scripts/compare_answer_quality_runs.py#L50) | 50 | `"    seen: set[str] = set()"` | — |
| [SRC-70795F4B61-L000051](../../scripts/compare_answer_quality_runs.py#L51) | 51 | `"    for index, record in enumerate(results):"` | — |
| [SRC-70795F4B61-L000052](../../scripts/compare_answer_quality_runs.py#L52) | 52 | `"        if not isinstance(record, dict):"` | — |
| [SRC-70795F4B61-L000053](../../scripts/compare_answer_quality_runs.py#L53) | 53 | `"            problems.append(f\"{label}: results[{index}] must be an object\")"` | — |
| [SRC-70795F4B61-L000054](../../scripts/compare_answer_quality_runs.py#L54) | 54 | `"            continue"` | — |
| [SRC-70795F4B61-L000055](../../scripts/compare_answer_quality_runs.py#L55) | 55 | `"        case_id = record.get(\"case_id\")"` | — |
| [SRC-70795F4B61-L000056](../../scripts/compare_answer_quality_runs.py#L56) | 56 | `"        if not isinstance(case_id, str) or not case_id.strip():"` | — |
| [SRC-70795F4B61-L000057](../../scripts/compare_answer_quality_runs.py#L57) | 57 | `"            problems.append(f\"{label}: results[{index}] has no case_id\")"` | — |
| [SRC-70795F4B61-L000058](../../scripts/compare_answer_quality_runs.py#L58) | 58 | `"            continue"` | — |
| [SRC-70795F4B61-L000059](../../scripts/compare_answer_quality_runs.py#L59) | 59 | `"        prompt = record.get(\"prompt\")"` | — |
| [SRC-70795F4B61-L000060](../../scripts/compare_answer_quality_runs.py#L60) | 60 | `"        if not isinstance(prompt, str) or not prompt.strip():"` | — |
| [SRC-70795F4B61-L000061](../../scripts/compare_answer_quality_runs.py#L61) | 61 | `"            problems.append(f\"{label}/{case_id}: prompt must be a non-empty string\")"` | — |
| [SRC-70795F4B61-L000062](../../scripts/compare_answer_quality_runs.py#L62) | 62 | `"        if case_id in seen:"` | — |
| [SRC-70795F4B61-L000063](../../scripts/compare_answer_quality_runs.py#L63) | 63 | `"            problems.append(f\"{label}: duplicate case_id {case_id}\")"` | — |
| [SRC-70795F4B61-L000064](../../scripts/compare_answer_quality_runs.py#L64) | 64 | `"        seen.add(case_id)"` | — |
| [SRC-70795F4B61-L000065](../../scripts/compare_answer_quality_runs.py#L65) | 65 | `"        if \"elapsed_ms\" in record and _finite_nonnegative(record[\"elapsed_ms\"]) is None:"` | — |
| [SRC-70795F4B61-L000066](../../scripts/compare_answer_quality_runs.py#L66) | 66 | `"            problems.append(f\"{label}/{case_id}: elapsed_ms must be finite and non-negative\")"` | — |
| [SRC-70795F4B61-L000067](../../scripts/compare_answer_quality_runs.py#L67) | 67 | `"    return problems"` | — |
| [SRC-70795F4B61-L000068](../../scripts/compare_answer_quality_runs.py#L68) | 68 | `""` | — |
| [SRC-70795F4B61-L000069](../../scripts/compare_answer_quality_runs.py#L69) | 69 | `""` | — |
| [SRC-70795F4B61-L000070](../../scripts/compare_answer_quality_runs.py#L70) | 70 | `"def _percentile_nearest_rank(values: list[float], percentile: float) -> float \| None:"` | — |
| [SRC-70795F4B61-L000071](../../scripts/compare_answer_quality_runs.py#L71) | 71 | `"    if not values:"` | — |
| [SRC-70795F4B61-L000072](../../scripts/compare_answer_quality_runs.py#L72) | 72 | `"        return None"` | — |
| [SRC-70795F4B61-L000073](../../scripts/compare_answer_quality_runs.py#L73) | 73 | `"    ordered = sorted(values)"` | — |
| [SRC-70795F4B61-L000074](../../scripts/compare_answer_quality_runs.py#L74) | 74 | `"    index = max(0, math.ceil(percentile * len(ordered)) - 1)"` | — |
| [SRC-70795F4B61-L000075](../../scripts/compare_answer_quality_runs.py#L75) | 75 | `"    return round(ordered[index], 2)"` | — |
| [SRC-70795F4B61-L000076](../../scripts/compare_answer_quality_runs.py#L76) | 76 | `""` | — |
| [SRC-70795F4B61-L000077](../../scripts/compare_answer_quality_runs.py#L77) | 77 | `""` | — |
| [SRC-70795F4B61-L000078](../../scripts/compare_answer_quality_runs.py#L78) | 78 | `"def _rate(numerator: int, denominator: int) -> dict[str, Any]:"` | — |
| [SRC-70795F4B61-L000079](../../scripts/compare_answer_quality_runs.py#L79) | 79 | `"    return {"` | — |
| [SRC-70795F4B61-L000080](../../scripts/compare_answer_quality_runs.py#L80) | 80 | `"        \"score\": round(numerator / denominator, 4) if denominator else None,"` | — |
| [SRC-70795F4B61-L000081](../../scripts/compare_answer_quality_runs.py#L81) | 81 | `"        \"numerator\": numerator,"` | — |
| [SRC-70795F4B61-L000082](../../scripts/compare_answer_quality_runs.py#L82) | 82 | `"        \"denominator\": denominator,"` | — |
| [SRC-70795F4B61-L000083](../../scripts/compare_answer_quality_runs.py#L83) | 83 | `"        \"status\": \"SCORED\" if denominator else \"NOT_SCORABLE_NO_DENOMINATOR\","` | — |
| [SRC-70795F4B61-L000084](../../scripts/compare_answer_quality_runs.py#L84) | 84 | `"    }"` | — |
| [SRC-70795F4B61-L000085](../../scripts/compare_answer_quality_runs.py#L85) | 85 | `""` | — |
| [SRC-70795F4B61-L000086](../../scripts/compare_answer_quality_runs.py#L86) | 86 | `""` | — |
| [SRC-70795F4B61-L000087](../../scripts/compare_answer_quality_runs.py#L87) | 87 | `"def run_metrics(run: dict[str, Any]) -> dict[str, Any]:"` | — |
| [SRC-70795F4B61-L000088](../../scripts/compare_answer_quality_runs.py#L88) | 88 | `"    results = run[\"results\"]"` | — |
| [SRC-70795F4B61-L000089](../../scripts/compare_answer_quality_runs.py#L89) | 89 | `"    transport_ok = [r for r in results if r.get(\"transport_ok\") is True]"` | — |
| [SRC-70795F4B61-L000090](../../scripts/compare_answer_quality_runs.py#L90) | 90 | `"    elapsed = ["` | — |
| [SRC-70795F4B61-L000091](../../scripts/compare_answer_quality_runs.py#L91) | 91 | `"        float(value)"` | — |
| [SRC-70795F4B61-L000092](../../scripts/compare_answer_quality_runs.py#L92) | 92 | `"        for record in results"` | — |
| [SRC-70795F4B61-L000093](../../scripts/compare_answer_quality_runs.py#L93) | 93 | `"        if (value := _finite_nonnegative(record.get(\"elapsed_ms\"))) is not None"` | — |
| [SRC-70795F4B61-L000094](../../scripts/compare_answer_quality_runs.py#L94) | 94 | `"    ]"` | — |
| [SRC-70795F4B61-L000095](../../scripts/compare_answer_quality_runs.py#L95) | 95 | `"    search_cases = [r for r in results if r.get(\"expected_strategy\") == \"web_search\"]"` | — |
| [SRC-70795F4B61-L000096](../../scripts/compare_answer_quality_runs.py#L96) | 96 | `"    search_attempted = ["` | — |
| [SRC-70795F4B61-L000097](../../scripts/compare_answer_quality_runs.py#L97) | 97 | `"        r for r in search_cases"` | — |
| [SRC-70795F4B61-L000098](../../scripts/compare_answer_quality_runs.py#L98) | 98 | `"        if r.get(\"search_outcome\") not in (None, \"\", \"unknown\", \"not_attempted\")"` | — |
| [SRC-70795F4B61-L000099](../../scripts/compare_answer_quality_runs.py#L99) | 99 | `"    ]"` | — |
| [SRC-70795F4B61-L000100](../../scripts/compare_answer_quality_runs.py#L100) | 100 | `"    usable = [r for r in search_cases if r.get(\"tool_status\") == \"SUCCESS_WITH_USABLE_RESULTS\"]"` | — |
| [SRC-70795F4B61-L000101](../../scripts/compare_answer_quality_runs.py#L101) | 101 | `"    tool_failed = [r for r in search_cases if r.get(\"tool_status\") == \"TOOL_FAILED\"]"` | — |
| [SRC-70795F4B61-L000102](../../scripts/compare_answer_quality_runs.py#L102) | 102 | `"    no_usable = [r for r in search_cases if r.get(\"tool_status\") == \"ATTEMPTED_NO_USABLE_RESULTS\"]"` | — |
| [SRC-70795F4B61-L000103](../../scripts/compare_answer_quality_runs.py#L103) | 103 | `"    costs = ["` | — |
| [SRC-70795F4B61-L000104](../../scripts/compare_answer_quality_runs.py#L104) | 104 | `"        float(value)"` | — |
| [SRC-70795F4B61-L000105](../../scripts/compare_answer_quality_runs.py#L105) | 105 | `"        for record in results"` | — |
| [SRC-70795F4B61-L000106](../../scripts/compare_answer_quality_runs.py#L106) | 106 | `"        if (value := _finite_nonnegative(record.get(\"provider_reported_model_cost_usd\"))) is not None"` | — |
| [SRC-70795F4B61-L000107](../../scripts/compare_answer_quality_runs.py#L107) | 107 | `"    ]"` | — |
| [SRC-70795F4B61-L000108](../../scripts/compare_answer_quality_runs.py#L108) | 108 | `"    required_tool_rows = ["` | — |
| [SRC-70795F4B61-L000109](../../scripts/compare_answer_quality_runs.py#L109) | 109 | `"        row"` | — |
| [SRC-70795F4B61-L000110](../../scripts/compare_answer_quality_runs.py#L110) | 110 | `"        for record in results"` | — |
| [SRC-70795F4B61-L000111](../../scripts/compare_answer_quality_runs.py#L111) | 111 | `"        for row in record.get(\"required_tool_statuses\", [])"` | — |
| [SRC-70795F4B61-L000112](../../scripts/compare_answer_quality_runs.py#L112) | 112 | `"        if isinstance(row, dict) and isinstance(row.get(\"successful_completion\"), bool)"` | — |
| [SRC-70795F4B61-L000113](../../scripts/compare_answer_quality_runs.py#L113) | 113 | `"    ]"` | — |
| [SRC-70795F4B61-L000114](../../scripts/compare_answer_quality_runs.py#L114) | 114 | `"    required_tool_successes = sum("` | — |
| [SRC-70795F4B61-L000115](../../scripts/compare_answer_quality_runs.py#L115) | 115 | `"        1 for row in required_tool_rows if row[\"successful_completion\"] is True"` | — |
| [SRC-70795F4B61-L000116](../../scripts/compare_answer_quality_runs.py#L116) | 116 | `"    )"` | — |
| [SRC-70795F4B61-L000117](../../scripts/compare_answer_quality_runs.py#L117) | 117 | `"    tool_status_counts: dict[str, int] = {}"` | — |
| [SRC-70795F4B61-L000118](../../scripts/compare_answer_quality_runs.py#L118) | 118 | `"    for row in required_tool_rows:"` | — |
| [SRC-70795F4B61-L000119](../../scripts/compare_answer_quality_runs.py#L119) | 119 | `"        status = row.get(\"status\")"` | — |
| [SRC-70795F4B61-L000120](../../scripts/compare_answer_quality_runs.py#L120) | 120 | `"        if isinstance(status, str):"` | — |
| [SRC-70795F4B61-L000121](../../scripts/compare_answer_quality_runs.py#L121) | 121 | `"            tool_status_counts[status] = tool_status_counts.get(status, 0) + 1"` | — |
| [SRC-70795F4B61-L000122](../../scripts/compare_answer_quality_runs.py#L122) | 122 | `"    required_tool_matrix_telemetry_known = all("` | — |
| [SRC-70795F4B61-L000123](../../scripts/compare_answer_quality_runs.py#L123) | 123 | `"        isinstance(record.get(\"required_tool_matrix_complete\"), bool)"` | — |
| [SRC-70795F4B61-L000124](../../scripts/compare_answer_quality_runs.py#L124) | 124 | `"        for record in results"` | — |
| [SRC-70795F4B61-L000125](../../scripts/compare_answer_quality_runs.py#L125) | 125 | `"    )"` | — |
| [SRC-70795F4B61-L000126](../../scripts/compare_answer_quality_runs.py#L126) | 126 | `"    required_tool_matrix_complete_count = sum("` | — |
| [SRC-70795F4B61-L000127](../../scripts/compare_answer_quality_runs.py#L127) | 127 | `"        1 for record in results if record.get(\"required_tool_matrix_complete\") is True"` | — |
| [SRC-70795F4B61-L000128](../../scripts/compare_answer_quality_runs.py#L128) | 128 | `"    )"` | — |
| [SRC-70795F4B61-L000129](../../scripts/compare_answer_quality_runs.py#L129) | 129 | `"    required_tool_matrix_incomplete_case_ids = ["` | — |
| [SRC-70795F4B61-L000130](../../scripts/compare_answer_quality_runs.py#L130) | 130 | `"        record.get(\"case_id\", \"unknown\")"` | — |
| [SRC-70795F4B61-L000131](../../scripts/compare_answer_quality_runs.py#L131) | 131 | `"        for record in results"` | — |
| [SRC-70795F4B61-L000132](../../scripts/compare_answer_quality_runs.py#L132) | 132 | `"        if record.get(\"required_tool_matrix_complete\") is not True"` | — |
| [SRC-70795F4B61-L000133](../../scripts/compare_answer_quality_runs.py#L133) | 133 | `"    ]"` | — |
| [SRC-70795F4B61-L000134](../../scripts/compare_answer_quality_runs.py#L134) | 134 | `"    complete_cost_cases = sum("` | — |
| [SRC-70795F4B61-L000135](../../scripts/compare_answer_quality_runs.py#L135) | 135 | `"        1 for r in results"` | — |
| [SRC-70795F4B61-L000136](../../scripts/compare_answer_quality_runs.py#L136) | 136 | `"        if r.get(\"provider_reported_model_cost_status\") == \"COMPLETE_FOR_RETURNED_MODEL_CALLS\""` | — |
| [SRC-70795F4B61-L000137](../../scripts/compare_answer_quality_runs.py#L137) | 137 | `"    )"` | — |
| [SRC-70795F4B61-L000138](../../scripts/compare_answer_quality_runs.py#L138) | 138 | `"    reconciled_request_costs = ["` | — |
| [SRC-70795F4B61-L000139](../../scripts/compare_answer_quality_runs.py#L139) | 139 | `"        float(value)"` | — |
| [SRC-70795F4B61-L000140](../../scripts/compare_answer_quality_runs.py#L140) | 140 | `"        for record in results"` | — |
| [SRC-70795F4B61-L000141](../../scripts/compare_answer_quality_runs.py#L141) | 141 | `"        if record.get(\"request_cost_status\") == \"RECONCILED_COMPLETE_REQUEST_COST\""` | — |
| [SRC-70795F4B61-L000142](../../scripts/compare_answer_quality_runs.py#L142) | 142 | `"        and (value := _finite_nonnegative(record.get(\"request_cost_usd\"))) is not None"` | — |
| [SRC-70795F4B61-L000143](../../scripts/compare_answer_quality_runs.py#L143) | 143 | `"    ]"` | — |
| [SRC-70795F4B61-L000144](../../scripts/compare_answer_quality_runs.py#L144) | 144 | `"    complete_request_cost_count = len(reconciled_request_costs)"` | — |
| [SRC-70795F4B61-L000145](../../scripts/compare_answer_quality_runs.py#L145) | 145 | `"    request_cost_complete = complete_request_cost_count == len(results)"` | — |
| [SRC-70795F4B61-L000146](../../scripts/compare_answer_quality_runs.py#L146) | 146 | `"    return {"` | — |
| [SRC-70795F4B61-L000147](../../scripts/compare_answer_quality_runs.py#L147) | 147 | `"        \"case_count\": len(results),"` | — |
| [SRC-70795F4B61-L000148](../../scripts/compare_answer_quality_runs.py#L148) | 148 | `"        \"transport_success_rate\": _rate(len(transport_ok), len(results)),"` | — |
| [SRC-70795F4B61-L000149](../../scripts/compare_answer_quality_runs.py#L149) | 149 | `"        \"latency_ms\": {"` | — |
| [SRC-70795F4B61-L000150](../../scripts/compare_answer_quality_runs.py#L150) | 150 | `"            \"sample_count\": len(elapsed),"` | — |
| [SRC-70795F4B61-L000151](../../scripts/compare_answer_quality_runs.py#L151) | 151 | `"            \"mean\": round(sum(elapsed) / len(elapsed), 2) if elapsed else None,"` | — |
| [SRC-70795F4B61-L000152](../../scripts/compare_answer_quality_runs.py#L152) | 152 | `"            \"p50\": _percentile_nearest_rank(elapsed, 0.50),"` | — |
| [SRC-70795F4B61-L000153](../../scripts/compare_answer_quality_runs.py#L153) | 153 | `"            \"p95\": _percentile_nearest_rank(elapsed, 0.95),"` | — |
| [SRC-70795F4B61-L000154](../../scripts/compare_answer_quality_runs.py#L154) | 154 | `"            \"max\": round(max(elapsed), 2) if elapsed else None,"` | — |
| [SRC-70795F4B61-L000155](../../scripts/compare_answer_quality_runs.py#L155) | 155 | `"            \"status\": \"SCORED\" if elapsed else \"NOT_MEASURED\","` | — |
| [SRC-70795F4B61-L000156](../../scripts/compare_answer_quality_runs.py#L156) | 156 | `"            \"semantics\": \"Sequential end-to-end HTTP request time; not a concurrency/load test.\","` | — |
| [SRC-70795F4B61-L000157](../../scripts/compare_answer_quality_runs.py#L157) | 157 | `"        },"` | — |
| [SRC-70795F4B61-L000158](../../scripts/compare_answer_quality_runs.py#L158) | 158 | `"        \"tool_usage\": {"` | — |
| [SRC-70795F4B61-L000159](../../scripts/compare_answer_quality_runs.py#L159) | 159 | `"            \"web_search_case_count\": len(search_cases),"` | — |
| [SRC-70795F4B61-L000160](../../scripts/compare_answer_quality_runs.py#L160) | 160 | `"            \"search_attempt_rate\": _rate(len(search_attempted), len(search_cases)),"` | — |
| [SRC-70795F4B61-L000161](../../scripts/compare_answer_quality_runs.py#L161) | 161 | `"            \"usable_result_rate\": _rate(len(usable), len(search_cases)),"` | — |
| [SRC-70795F4B61-L000162](../../scripts/compare_answer_quality_runs.py#L162) | 162 | `"            \"tool_error_rate_among_search_cases\": _rate(len(tool_failed), len(search_cases)),"` | — |
| [SRC-70795F4B61-L000163](../../scripts/compare_answer_quality_runs.py#L163) | 163 | `"            \"attempted_without_usable_results\": len(no_usable),"` | — |
| [SRC-70795F4B61-L000164](../../scripts/compare_answer_quality_runs.py#L164) | 164 | `"            \"unknown_tool_outcome_count\": sum("` | — |
| [SRC-70795F4B61-L000165](../../scripts/compare_answer_quality_runs.py#L165) | 165 | `"                1 for r in search_cases"` | — |
| [SRC-70795F4B61-L000166](../../scripts/compare_answer_quality_runs.py#L166) | 166 | `"                if r.get(\"tool_status\") in (None, \"\", \"UNKNOWN\")"` | — |
| [SRC-70795F4B61-L000167](../../scripts/compare_answer_quality_runs.py#L167) | 167 | `"            ),"` | — |
| [SRC-70795F4B61-L000168](../../scripts/compare_answer_quality_runs.py#L168) | 168 | `"            \"required_tool_observation_count\": len(required_tool_rows),"` | — |
| [SRC-70795F4B61-L000169](../../scripts/compare_answer_quality_runs.py#L169) | 169 | `"            \"required_tool_success_count\": required_tool_successes,"` | — |
| [SRC-70795F4B61-L000170](../../scripts/compare_answer_quality_runs.py#L170) | 170 | `"            \"required_tool_success_rate\": _rate(required_tool_successes, len(required_tool_rows)),"` | — |
| [SRC-70795F4B61-L000171](../../scripts/compare_answer_quality_runs.py#L171) | 171 | `"            \"required_tool_status_counts\": tool_status_counts,"` | — |
| [SRC-70795F4B61-L000172](../../scripts/compare_answer_quality_runs.py#L172) | 172 | `"            \"required_tool_status_case_count\": sum("` | — |
| [SRC-70795F4B61-L000173](../../scripts/compare_answer_quality_runs.py#L173) | 173 | `"                1 for r in results"` | — |
| [SRC-70795F4B61-L000174](../../scripts/compare_answer_quality_runs.py#L174) | 174 | `"                if isinstance(r.get(\"required_tool_statuses\"), list)"` | — |
| [SRC-70795F4B61-L000175](../../scripts/compare_answer_quality_runs.py#L175) | 175 | `"                and r.get(\"required_tool_statuses\")"` | — |
| [SRC-70795F4B61-L000176](../../scripts/compare_answer_quality_runs.py#L176) | 176 | `"            ),"` | — |
| [SRC-70795F4B61-L000177](../../scripts/compare_answer_quality_runs.py#L177) | 177 | `"            \"required_tool_matrix_coverage\": {"` | — |
| [SRC-70795F4B61-L000178](../../scripts/compare_answer_quality_runs.py#L178) | 178 | `"                \"score\": ("` | — |
| [SRC-70795F4B61-L000179](../../scripts/compare_answer_quality_runs.py#L179) | 179 | `"                    round(required_tool_matrix_complete_count / len(results), 4)"` | — |
| [SRC-70795F4B61-L000180](../../scripts/compare_answer_quality_runs.py#L180) | 180 | `"                    if results and required_tool_matrix_telemetry_known"` | — |
| [SRC-70795F4B61-L000181](../../scripts/compare_answer_quality_runs.py#L181) | 181 | `"                    else None"` | — |
| [SRC-70795F4B61-L000182](../../scripts/compare_answer_quality_runs.py#L182) | 182 | `"                ),"` | — |
| [SRC-70795F4B61-L000183](../../scripts/compare_answer_quality_runs.py#L183) | 183 | `"                \"complete_case_count\": required_tool_matrix_complete_count,"` | — |
| [SRC-70795F4B61-L000184](../../scripts/compare_answer_quality_runs.py#L184) | 184 | `"                \"case_count\": len(results),"` | — |
| [SRC-70795F4B61-L000185](../../scripts/compare_answer_quality_runs.py#L185) | 185 | `"                \"incomplete_case_ids\": required_tool_matrix_incomplete_case_ids,"` | — |
| [SRC-70795F4B61-L000186](../../scripts/compare_answer_quality_runs.py#L186) | 186 | `"                \"status\": ("` | — |
| [SRC-70795F4B61-L000187](../../scripts/compare_answer_quality_runs.py#L187) | 187 | `"                    \"SCORED_FROM_EXPLICIT_TOOL_MATRIX\""` | — |
| [SRC-70795F4B61-L000188](../../scripts/compare_answer_quality_runs.py#L188) | 188 | `"                    if required_tool_matrix_telemetry_known"` | — |
| [SRC-70795F4B61-L000189](../../scripts/compare_answer_quality_runs.py#L189) | 189 | `"                    else \"NOT_MEASURED_REQUIRED_TOOL_MATRIX_TELEMETRY_MISSING\""` | — |
| [SRC-70795F4B61-L000190](../../scripts/compare_answer_quality_runs.py#L190) | 190 | `"                ),"` | — |
| [SRC-70795F4B61-L000191](../../scripts/compare_answer_quality_runs.py#L191) | 191 | `"            },"` | — |
| [SRC-70795F4B61-L000192](../../scripts/compare_answer_quality_runs.py#L192) | 192 | `"            \"required_tool_success_semantics\": ("` | — |
| [SRC-70795F4B61-L000193](../../scripts/compare_answer_quality_runs.py#L193) | 193 | `"                \"Only tool-specific completed-with-usable-output states count as success; \""` | — |
| [SRC-70795F4B61-L000194](../../scripts/compare_answer_quality_runs.py#L194) | 194 | `"                \"HTTP success and no-result attempts do not.\""` | — |
| [SRC-70795F4B61-L000195](../../scripts/compare_answer_quality_runs.py#L195) | 195 | `"            ),"` | — |
| [SRC-70795F4B61-L000196](../../scripts/compare_answer_quality_runs.py#L196) | 196 | `"        },"` | — |
| [SRC-70795F4B61-L000197](../../scripts/compare_answer_quality_runs.py#L197) | 197 | `"        \"provider_reported_model_cost\": {"` | — |
| [SRC-70795F4B61-L000198](../../scripts/compare_answer_quality_runs.py#L198) | 198 | `"            \"reported_sum_usd\": round(sum(costs), 10) if costs else None,"` | — |
| [SRC-70795F4B61-L000199](../../scripts/compare_answer_quality_runs.py#L199) | 199 | `"            \"cases_with_any_reported_cost\": len(costs),"` | — |
| [SRC-70795F4B61-L000200](../../scripts/compare_answer_quality_runs.py#L200) | 200 | `"            \"cases_complete_for_returned_model_calls\": complete_cost_cases,"` | — |
| [SRC-70795F4B61-L000201](../../scripts/compare_answer_quality_runs.py#L201) | 201 | `"            \"status\": ("` | — |
| [SRC-70795F4B61-L000202](../../scripts/compare_answer_quality_runs.py#L202) | 202 | `"                \"PARTIAL_OR_PROVIDER_REPORTED_ONLY\""` | — |
| [SRC-70795F4B61-L000203](../../scripts/compare_answer_quality_runs.py#L203) | 203 | `"                if costs"` | — |
| [SRC-70795F4B61-L000204](../../scripts/compare_answer_quality_runs.py#L204) | 204 | `"                else \"NOT_MEASURED_NO_PROVIDER_COST_REPORTED\""` | — |
| [SRC-70795F4B61-L000205](../../scripts/compare_answer_quality_runs.py#L205) | 205 | `"            ),"` | — |
| [SRC-70795F4B61-L000206](../../scripts/compare_answer_quality_runs.py#L206) | 206 | `"            \"complete_request_cost_usd\": ("` | — |
| [SRC-70795F4B61-L000207](../../scripts/compare_answer_quality_runs.py#L207) | 207 | `"                round(sum(reconciled_request_costs), 10) if request_cost_complete else None"` | — |
| [SRC-70795F4B61-L000208](../../scripts/compare_answer_quality_runs.py#L208) | 208 | `"            ),"` | — |
| [SRC-70795F4B61-L000209](../../scripts/compare_answer_quality_runs.py#L209) | 209 | `"            \"complete_request_cost_status\": ("` | — |
| [SRC-70795F4B61-L000210](../../scripts/compare_answer_quality_runs.py#L210) | 210 | `"                \"RECONCILED_COMPLETE_REQUEST_COST\""` | — |
| [SRC-70795F4B61-L000211](../../scripts/compare_answer_quality_runs.py#L211) | 211 | `"                if request_cost_complete"` | — |
| [SRC-70795F4B61-L000212](../../scripts/compare_answer_quality_runs.py#L212) | 212 | `"                else ("` | — |
| [SRC-70795F4B61-L000213](../../scripts/compare_answer_quality_runs.py#L213) | 213 | `"                    \"PARTIAL_EXTERNAL_COST_RECONCILIATION\""` | — |
| [SRC-70795F4B61-L000214](../../scripts/compare_answer_quality_runs.py#L214) | 214 | `"                    if complete_request_cost_count"` | — |
| [SRC-70795F4B61-L000215](../../scripts/compare_answer_quality_runs.py#L215) | 215 | `"                    else \"NOT_MEASURED_TOTAL_CONNECTOR_COSTS_NOT_EXPOSED\""` | — |
| [SRC-70795F4B61-L000216](../../scripts/compare_answer_quality_runs.py#L216) | 216 | `"                )"` | — |
| [SRC-70795F4B61-L000217](../../scripts/compare_answer_quality_runs.py#L217) | 217 | `"            ),"` | — |
| [SRC-70795F4B61-L000218](../../scripts/compare_answer_quality_runs.py#L218) | 218 | `"            \"complete_request_cost_case_count\": complete_request_cost_count,"` | — |
| [SRC-70795F4B61-L000219](../../scripts/compare_answer_quality_runs.py#L219) | 219 | `"        },"` | — |
| [SRC-70795F4B61-L000220](../../scripts/compare_answer_quality_runs.py#L220) | 220 | `"    }"` | — |
| [SRC-70795F4B61-L000221](../../scripts/compare_answer_quality_runs.py#L221) | 221 | `""` | — |
| [SRC-70795F4B61-L000222](../../scripts/compare_answer_quality_runs.py#L222) | 222 | `""` | — |
| [SRC-70795F4B61-L000223](../../scripts/compare_answer_quality_runs.py#L223) | 223 | `"def _load_review_scorer():"` | — |
| [SRC-70795F4B61-L000224](../../scripts/compare_answer_quality_runs.py#L224) | 224 | `"    path = ROOT / \"scripts\" / \"score_answer_quality_reviews.py\""` | — |
| [SRC-70795F4B61-L000225](../../scripts/compare_answer_quality_runs.py#L225) | 225 | `"    spec = importlib.util.spec_from_file_location(\"omarai_review_scorecard\", path)"` | — |
| [SRC-70795F4B61-L000226](../../scripts/compare_answer_quality_runs.py#L226) | 226 | `"    if spec is None or spec.loader is None:"` | — |
| [SRC-70795F4B61-L000227](../../scripts/compare_answer_quality_runs.py#L227) | 227 | `"        raise RuntimeError(\"Unable to load existing review scorecard: \" + str(path))"` | — |
| [SRC-70795F4B61-L000228](../../scripts/compare_answer_quality_runs.py#L228) | 228 | `"    module = importlib.util.module_from_spec(spec)"` | — |
| [SRC-70795F4B61-L000229](../../scripts/compare_answer_quality_runs.py#L229) | 229 | `"    spec.loader.exec_module(module)"` | — |
| [SRC-70795F4B61-L000230](../../scripts/compare_answer_quality_runs.py#L230) | 230 | `"    return module"` | — |
| [SRC-70795F4B61-L000231](../../scripts/compare_answer_quality_runs.py#L231) | 231 | `""` | — |
| [SRC-70795F4B61-L000232](../../scripts/compare_answer_quality_runs.py#L232) | 232 | `""` | — |
| [SRC-70795F4B61-L000233](../../scripts/compare_answer_quality_runs.py#L233) | 233 | `"def _reviewed_case_ids(review_data: dict[str, Any]) -> set[str]:"` | — |
| [SRC-70795F4B61-L000234](../../scripts/compare_answer_quality_runs.py#L234) | 234 | `"    reviews = review_data.get(\"reviews\")"` | — |
| [SRC-70795F4B61-L000235](../../scripts/compare_answer_quality_runs.py#L235) | 235 | `"    if not isinstance(reviews, list):"` | — |
| [SRC-70795F4B61-L000236](../../scripts/compare_answer_quality_runs.py#L236) | 236 | `"        raise ValueError(\"review file must contain a reviews array\")"` | — |
| [SRC-70795F4B61-L000237](../../scripts/compare_answer_quality_runs.py#L237) | 237 | `"    return {"` | — |
| [SRC-70795F4B61-L000238](../../scripts/compare_answer_quality_runs.py#L238) | 238 | `"        item[\"case_id\"]"` | — |
| [SRC-70795F4B61-L000239](../../scripts/compare_answer_quality_runs.py#L239) | 239 | `"        for item in reviews"` | — |
| [SRC-70795F4B61-L000240](../../scripts/compare_answer_quality_runs.py#L240) | 240 | `"        if isinstance(item, dict) and item.get(\"status\") == \"REVIEWED\""` | — |
| [SRC-70795F4B61-L000241](../../scripts/compare_answer_quality_runs.py#L241) | 241 | `"        and isinstance(item.get(\"case_id\"), str)"` | — |
| [SRC-70795F4B61-L000242](../../scripts/compare_answer_quality_runs.py#L242) | 242 | `"    }"` | — |
| [SRC-70795F4B61-L000243](../../scripts/compare_answer_quality_runs.py#L243) | 243 | `""` | — |
| [SRC-70795F4B61-L000244](../../scripts/compare_answer_quality_runs.py#L244) | 244 | `""` | — |
| [SRC-70795F4B61-L000245](../../scripts/compare_answer_quality_runs.py#L245) | 245 | `"def review_comparison("` | — |
| [SRC-70795F4B61-L000246](../../scripts/compare_answer_quality_runs.py#L246) | 246 | `"    baseline_reviews: dict[str, Any],"` | — |
| [SRC-70795F4B61-L000247](../../scripts/compare_answer_quality_runs.py#L247) | 247 | `"    candidate_reviews: dict[str, Any],"` | — |
| [SRC-70795F4B61-L000248](../../scripts/compare_answer_quality_runs.py#L248) | 248 | `"    corpus: dict[str, Any],"` | — |
| [SRC-70795F4B61-L000249](../../scripts/compare_answer_quality_runs.py#L249) | 249 | `") -> dict[str, Any]:"` | — |
| [SRC-70795F4B61-L000250](../../scripts/compare_answer_quality_runs.py#L250) | 250 | `"    baseline_ids = _reviewed_case_ids(baseline_reviews)"` | — |
| [SRC-70795F4B61-L000251](../../scripts/compare_answer_quality_runs.py#L251) | 251 | `"    candidate_ids = _reviewed_case_ids(candidate_reviews)"` | — |
| [SRC-70795F4B61-L000252](../../scripts/compare_answer_quality_runs.py#L252) | 252 | `"    if not baseline_ids or not candidate_ids:"` | — |
| [SRC-70795F4B61-L000253](../../scripts/compare_answer_quality_runs.py#L253) | 253 | `"        raise ValueError(\"both review files need explicitly REVIEWED cases\")"` | — |
| [SRC-70795F4B61-L000254](../../scripts/compare_answer_quality_runs.py#L254) | 254 | `"    corpus_cases = corpus.get(\"cases\")"` | — |
| [SRC-70795F4B61-L000255](../../scripts/compare_answer_quality_runs.py#L255) | 255 | `"    if not isinstance(corpus_cases, list) or not corpus_cases:"` | — |
| [SRC-70795F4B61-L000256](../../scripts/compare_answer_quality_runs.py#L256) | 256 | `"        raise ValueError(\"corpus must contain a non-empty cases array for full-coverage acceptance\")"` | — |
| [SRC-70795F4B61-L000257](../../scripts/compare_answer_quality_runs.py#L257) | 257 | `"    corpus_ids = {"` | — |
| [SRC-70795F4B61-L000258](../../scripts/compare_answer_quality_runs.py#L258) | 258 | `"        item.get(\"case_id\")"` | — |
| [SRC-70795F4B61-L000259](../../scripts/compare_answer_quality_runs.py#L259) | 259 | `"        for item in corpus_cases"` | — |
| [SRC-70795F4B61-L000260](../../scripts/compare_answer_quality_runs.py#L260) | 260 | `"        if isinstance(item, dict) and isinstance(item.get(\"case_id\"), str)"` | — |
| [SRC-70795F4B61-L000261](../../scripts/compare_answer_quality_runs.py#L261) | 261 | `"    }"` | — |
| [SRC-70795F4B61-L000262](../../scripts/compare_answer_quality_runs.py#L262) | 262 | `"    for label, reviewed_ids in ("` | — |
| [SRC-70795F4B61-L000263](../../scripts/compare_answer_quality_runs.py#L263) | 263 | `"        (\"baseline\", baseline_ids),"` | — |
| [SRC-70795F4B61-L000264](../../scripts/compare_answer_quality_runs.py#L264) | 264 | `"        (\"candidate\", candidate_ids),"` | — |
| [SRC-70795F4B61-L000265](../../scripts/compare_answer_quality_runs.py#L265) | 265 | `"    ):"` | — |
| [SRC-70795F4B61-L000266](../../scripts/compare_answer_quality_runs.py#L266) | 266 | `"        if reviewed_ids != corpus_ids:"` | — |
| [SRC-70795F4B61-L000267](../../scripts/compare_answer_quality_runs.py#L267) | 267 | `"            missing = sorted(corpus_ids - reviewed_ids)"` | — |
| [SRC-70795F4B61-L000268](../../scripts/compare_answer_quality_runs.py#L268) | 268 | `"            extra = sorted(reviewed_ids - corpus_ids)"` | — |
| [SRC-70795F4B61-L000269](../../scripts/compare_answer_quality_runs.py#L269) | 269 | `"            raise ValueError("` | — |
| [SRC-70795F4B61-L000270](../../scripts/compare_answer_quality_runs.py#L270) | 270 | `"                f\"incomplete human review coverage for {label}: \""` | — |
| [SRC-70795F4B61-L000271](../../scripts/compare_answer_quality_runs.py#L271) | 271 | `"                f\"missing={missing}; unknown={extra}\""` | — |
| [SRC-70795F4B61-L000272](../../scripts/compare_answer_quality_runs.py#L272) | 272 | `"            )"` | — |
| [SRC-70795F4B61-L000273](../../scripts/compare_answer_quality_runs.py#L273) | 273 | `"    if baseline_ids != candidate_ids:"` | — |
| [SRC-70795F4B61-L000274](../../scripts/compare_answer_quality_runs.py#L274) | 274 | `"        raise ValueError("` | — |
| [SRC-70795F4B61-L000275](../../scripts/compare_answer_quality_runs.py#L275) | 275 | `"            \"incomparable review coverage: REVIEWED case IDs differ between baseline and candidate\""` | — |
| [SRC-70795F4B61-L000276](../../scripts/compare_answer_quality_runs.py#L276) | 276 | `"        )"` | — |
| [SRC-70795F4B61-L000277](../../scripts/compare_answer_quality_runs.py#L277) | 277 | `"    scorer = _load_review_scorer()"` | — |
| [SRC-70795F4B61-L000278](../../scripts/compare_answer_quality_runs.py#L278) | 278 | `"    baseline = scorer.summarize_reviews(baseline_reviews, corpus)"` | — |
| [SRC-70795F4B61-L000279](../../scripts/compare_answer_quality_runs.py#L279) | 279 | `"    candidate = scorer.summarize_reviews(candidate_reviews, corpus)"` | — |
| [SRC-70795F4B61-L000280](../../scripts/compare_answer_quality_runs.py#L280) | 280 | `"    aliases = {"` | — |
| [SRC-70795F4B61-L000281](../../scripts/compare_answer_quality_runs.py#L281) | 281 | `"        \"retrieval_precision\": \"retrieval_precision\","` | — |
| [SRC-70795F4B61-L000282](../../scripts/compare_answer_quality_runs.py#L282) | 282 | `"        \"retrieval_recall\": \"retrieval_recall\","` | — |
| [SRC-70795F4B61-L000283](../../scripts/compare_answer_quality_runs.py#L283) | 283 | `"        \"factual_accuracy\": \"correctness\","` | — |
| [SRC-70795F4B61-L000284](../../scripts/compare_answer_quality_runs.py#L284) | 284 | `"        \"faithfulness\": \"faithfulness\","` | — |
| [SRC-70795F4B61-L000285](../../scripts/compare_answer_quality_runs.py#L285) | 285 | `"        \"citation_support\": \"citation_support\","` | — |
| [SRC-70795F4B61-L000286](../../scripts/compare_answer_quality_runs.py#L286) | 286 | `"        \"writing_quality_1_to_5\": \"writing_quality_1_to_5\","` | — |
| [SRC-70795F4B61-L000287](../../scripts/compare_answer_quality_runs.py#L287) | 287 | `"    }"` | — |
| [SRC-70795F4B61-L000288](../../scripts/compare_answer_quality_runs.py#L288) | 288 | `"    metrics: dict[str, Any] = {}"` | — |
| [SRC-70795F4B61-L000289](../../scripts/compare_answer_quality_runs.py#L289) | 289 | `"    for output_name, score_name in aliases.items():"` | — |
| [SRC-70795F4B61-L000290](../../scripts/compare_answer_quality_runs.py#L290) | 290 | `"        before = baseline[\"metrics\"][score_name][\"score\"]"` | — |
| [SRC-70795F4B61-L000291](../../scripts/compare_answer_quality_runs.py#L291) | 291 | `"        after = candidate[\"metrics\"][score_name][\"score\"]"` | — |
| [SRC-70795F4B61-L000292](../../scripts/compare_answer_quality_runs.py#L292) | 292 | `"        metrics[output_name] = {"` | — |
| [SRC-70795F4B61-L000293](../../scripts/compare_answer_quality_runs.py#L293) | 293 | `"            \"baseline\": before,"` | — |
| [SRC-70795F4B61-L000294](../../scripts/compare_answer_quality_runs.py#L294) | 294 | `"            \"candidate\": after,"` | — |
| [SRC-70795F4B61-L000295](../../scripts/compare_answer_quality_runs.py#L295) | 295 | `"            \"delta\": round(after - before, 4) if before is not None and after is not None else None,"` | — |
| [SRC-70795F4B61-L000296](../../scripts/compare_answer_quality_runs.py#L296) | 296 | `"            \"status\": ("` | — |
| [SRC-70795F4B61-L000297](../../scripts/compare_answer_quality_runs.py#L297) | 297 | `"                \"COMPARED\" if before is not None and after is not None"` | — |
| [SRC-70795F4B61-L000298](../../scripts/compare_answer_quality_runs.py#L298) | 298 | `"                else \"NOT_SCORABLE_MISSING_ANNOTATED_DENOMINATOR\""` | — |
| [SRC-70795F4B61-L000299](../../scripts/compare_answer_quality_runs.py#L299) | 299 | `"            ),"` | — |
| [SRC-70795F4B61-L000300](../../scripts/compare_answer_quality_runs.py#L300) | 300 | `"            \"source\": \"explicit_human_review\","` | — |
| [SRC-70795F4B61-L000301](../../scripts/compare_answer_quality_runs.py#L301) | 301 | `"        }"` | — |
| [SRC-70795F4B61-L000302](../../scripts/compare_answer_quality_runs.py#L302) | 302 | `"    return {"` | — |
| [SRC-70795F4B61-L000303](../../scripts/compare_answer_quality_runs.py#L303) | 303 | `"        \"reviewed_case_count\": len(baseline_ids),"` | — |
| [SRC-70795F4B61-L000304](../../scripts/compare_answer_quality_runs.py#L304) | 304 | `"        \"baseline_review_coverage\": baseline[\"reviewed_case_coverage\"],"` | — |
| [SRC-70795F4B61-L000305](../../scripts/compare_answer_quality_runs.py#L305) | 305 | `"        \"candidate_review_coverage\": candidate[\"reviewed_case_coverage\"],"` | — |
| [SRC-70795F4B61-L000306](../../scripts/compare_answer_quality_runs.py#L306) | 306 | `"        \"metrics\": metrics,"` | — |
| [SRC-70795F4B61-L000307](../../scripts/compare_answer_quality_runs.py#L307) | 307 | `"        \"automatic_answer_grading\": False,"` | — |
| [SRC-70795F4B61-L000308](../../scripts/compare_answer_quality_runs.py#L308) | 308 | `"        \"limitations\": ["` | — |
| [SRC-70795F4B61-L000309](../../scripts/compare_answer_quality_runs.py#L309) | 309 | `"            \"Scores reflect explicit human annotations, not automatic model grading.\","` | — |
| [SRC-70795F4B61-L000310](../../scripts/compare_answer_quality_runs.py#L310) | 310 | `"            \"Retrieval precision/recall require comparable candidate pools and relevance judgments.\","` | — |
| [SRC-70795F4B61-L000311](../../scripts/compare_answer_quality_runs.py#L311) | 311 | `"            \"Citation support measures reviewer-labelled citations that support the associated claims; URL presence alone is not evidence of support.\","` | — |
| [SRC-70795F4B61-L000312](../../scripts/compare_answer_quality_runs.py#L312) | 312 | `"        ],"` | — |
| [SRC-70795F4B61-L000313](../../scripts/compare_answer_quality_runs.py#L313) | 313 | `"    }"` | — |
| [SRC-70795F4B61-L000314](../../scripts/compare_answer_quality_runs.py#L314) | 314 | `""` | — |
| [SRC-70795F4B61-L000315](../../scripts/compare_answer_quality_runs.py#L315) | 315 | `""` | — |
| [SRC-70795F4B61-L000316](../../scripts/compare_answer_quality_runs.py#L316) | 316 | `"def compare_runs("` | — |
| [SRC-70795F4B61-L000317](../../scripts/compare_answer_quality_runs.py#L317) | 317 | `"    baseline: dict[str, Any],"` | — |
| [SRC-70795F4B61-L000318](../../scripts/compare_answer_quality_runs.py#L318) | 318 | `"    candidate: dict[str, Any],"` | — |
| [SRC-70795F4B61-L000319](../../scripts/compare_answer_quality_runs.py#L319) | 319 | `"    *,"` | — |
| [SRC-70795F4B61-L000320](../../scripts/compare_answer_quality_runs.py#L320) | 320 | `"    corpus: dict[str, Any] \| None = None,"` | — |
| [SRC-70795F4B61-L000321](../../scripts/compare_answer_quality_runs.py#L321) | 321 | `"    baseline_reviews: dict[str, Any] \| None = None,"` | — |
| [SRC-70795F4B61-L000322](../../scripts/compare_answer_quality_runs.py#L322) | 322 | `"    candidate_reviews: dict[str, Any] \| None = None,"` | — |
| [SRC-70795F4B61-L000323](../../scripts/compare_answer_quality_runs.py#L323) | 323 | `") -> dict[str, Any]:"` | — |
| [SRC-70795F4B61-L000324](../../scripts/compare_answer_quality_runs.py#L324) | 324 | `"    problems = validate_run(baseline, \"baseline\") + validate_run(candidate, \"candidate\")"` | — |
| [SRC-70795F4B61-L000325](../../scripts/compare_answer_quality_runs.py#L325) | 325 | `"    if problems:"` | — |
| [SRC-70795F4B61-L000326](../../scripts/compare_answer_quality_runs.py#L326) | 326 | `"        raise ValueError(\"; \".join(problems))"` | — |
| [SRC-70795F4B61-L000327](../../scripts/compare_answer_quality_runs.py#L327) | 327 | `"    if baseline.get(\"benchmark_id\") != candidate.get(\"benchmark_id\"):"` | — |
| [SRC-70795F4B61-L000328](../../scripts/compare_answer_quality_runs.py#L328) | 328 | `"        raise ValueError(\"baseline/candidate benchmark_id differs\")"` | — |
| [SRC-70795F4B61-L000329](../../scripts/compare_answer_quality_runs.py#L329) | 329 | `"    if baseline.get(\"benchmark_version\") != candidate.get(\"benchmark_version\"):"` | — |
| [SRC-70795F4B61-L000330](../../scripts/compare_answer_quality_runs.py#L330) | 330 | `"        raise ValueError(\"baseline/candidate benchmark_version differs\")"` | — |
| [SRC-70795F4B61-L000331](../../scripts/compare_answer_quality_runs.py#L331) | 331 | `"    if corpus is not None:"` | — |
| [SRC-70795F4B61-L000332](../../scripts/compare_answer_quality_runs.py#L332) | 332 | `"        if corpus.get(\"benchmark_id\") != baseline.get(\"benchmark_id\"):"` | — |
| [SRC-70795F4B61-L000333](../../scripts/compare_answer_quality_runs.py#L333) | 333 | `"            raise ValueError(\"runs do not match the supplied corpus benchmark_id\")"` | — |
| [SRC-70795F4B61-L000334](../../scripts/compare_answer_quality_runs.py#L334) | 334 | `"        if corpus.get(\"version\") != baseline.get(\"benchmark_version\"):"` | — |
| [SRC-70795F4B61-L000335](../../scripts/compare_answer_quality_runs.py#L335) | 335 | `"            raise ValueError(\"runs do not match the supplied corpus benchmark_version\")"` | — |
| [SRC-70795F4B61-L000336](../../scripts/compare_answer_quality_runs.py#L336) | 336 | `"    baseline_by_id = {row[\"case_id\"]: row for row in baseline[\"results\"]}"` | — |
| [SRC-70795F4B61-L000337](../../scripts/compare_answer_quality_runs.py#L337) | 337 | `"    candidate_by_id = {row[\"case_id\"]: row for row in candidate[\"results\"]}"` | — |
| [SRC-70795F4B61-L000338](../../scripts/compare_answer_quality_runs.py#L338) | 338 | `"    if set(baseline_by_id) != set(candidate_by_id):"` | — |
| [SRC-70795F4B61-L000339](../../scripts/compare_answer_quality_runs.py#L339) | 339 | `"        missing_candidate = sorted(set(baseline_by_id) - set(candidate_by_id))"` | — |
| [SRC-70795F4B61-L000340](../../scripts/compare_answer_quality_runs.py#L340) | 340 | `"        missing_baseline = sorted(set(candidate_by_id) - set(baseline_by_id))"` | — |
| [SRC-70795F4B61-L000341](../../scripts/compare_answer_quality_runs.py#L341) | 341 | `"        raise ValueError("` | — |
| [SRC-70795F4B61-L000342](../../scripts/compare_answer_quality_runs.py#L342) | 342 | `"            f\"incomparable case sets; missing in candidate={missing_candidate}; \""` | — |
| [SRC-70795F4B61-L000343](../../scripts/compare_answer_quality_runs.py#L343) | 343 | `"            f\"missing in baseline={missing_baseline}\""` | — |
| [SRC-70795F4B61-L000344](../../scripts/compare_answer_quality_runs.py#L344) | 344 | `"        )"` | — |
| [SRC-70795F4B61-L000345](../../scripts/compare_answer_quality_runs.py#L345) | 345 | `"    corpus_by_id = {"` | — |
| [SRC-70795F4B61-L000346](../../scripts/compare_answer_quality_runs.py#L346) | 346 | `"        case[\"case_id\"]: case"` | — |
| [SRC-70795F4B61-L000347](../../scripts/compare_answer_quality_runs.py#L347) | 347 | `"        for case in (corpus.get(\"cases\", []) if corpus is not None else [])"` | — |
| [SRC-70795F4B61-L000348](../../scripts/compare_answer_quality_runs.py#L348) | 348 | `"        if isinstance(case, dict) and isinstance(case.get(\"case_id\"), str)"` | — |
| [SRC-70795F4B61-L000349](../../scripts/compare_answer_quality_runs.py#L349) | 349 | `"    }"` | — |
| [SRC-70795F4B61-L000350](../../scripts/compare_answer_quality_runs.py#L350) | 350 | `"    for case_id in baseline_by_id:"` | — |
| [SRC-70795F4B61-L000351](../../scripts/compare_answer_quality_runs.py#L351) | 351 | `"        before_row = baseline_by_id[case_id]"` | — |
| [SRC-70795F4B61-L000352](../../scripts/compare_answer_quality_runs.py#L352) | 352 | `"        after_row = candidate_by_id[case_id]"` | — |
| [SRC-70795F4B61-L000353](../../scripts/compare_answer_quality_runs.py#L353) | 353 | `"        if before_row.get(\"prompt\") != after_row.get(\"prompt\"):"` | — |
| [SRC-70795F4B61-L000354](../../scripts/compare_answer_quality_runs.py#L354) | 354 | `"            raise ValueError(f\"incomparable question text for {case_id}\")"` | — |
| [SRC-70795F4B61-L000355](../../scripts/compare_answer_quality_runs.py#L355) | 355 | `"        if corpus is not None:"` | — |
| [SRC-70795F4B61-L000356](../../scripts/compare_answer_quality_runs.py#L356) | 356 | `"            corpus_case = corpus_by_id.get(case_id)"` | — |
| [SRC-70795F4B61-L000357](../../scripts/compare_answer_quality_runs.py#L357) | 357 | `"            if not isinstance(corpus_case, dict):"` | — |
| [SRC-70795F4B61-L000358](../../scripts/compare_answer_quality_runs.py#L358) | 358 | `"                raise ValueError(f\"{case_id}: case_id is not present in the supplied corpus\")"` | — |
| [SRC-70795F4B61-L000359](../../scripts/compare_answer_quality_runs.py#L359) | 359 | `"            if before_row.get(\"prompt\") != corpus_case.get(\"question\"):"` | — |
| [SRC-70795F4B61-L000360](../../scripts/compare_answer_quality_runs.py#L360) | 360 | `"                raise ValueError(f\"{case_id}: recorded prompt differs from the canonical corpus question\")"` | — |
| [SRC-70795F4B61-L000361](../../scripts/compare_answer_quality_runs.py#L361) | 361 | `"            if before_row.get(\"expected_strategy\") != corpus_case.get(\"expected_strategy\"):"` | — |
| [SRC-70795F4B61-L000362](../../scripts/compare_answer_quality_runs.py#L362) | 362 | `"                raise ValueError(f\"{case_id}: expected_strategy differs from the canonical corpus\")"` | — |
| [SRC-70795F4B61-L000363](../../scripts/compare_answer_quality_runs.py#L363) | 363 | `""` | — |
| [SRC-70795F4B61-L000364](../../scripts/compare_answer_quality_runs.py#L364) | 364 | `"    before_runtime = run_metrics(baseline)"` | — |
| [SRC-70795F4B61-L000365](../../scripts/compare_answer_quality_runs.py#L365) | 365 | `"    after_runtime = run_metrics(candidate)"` | — |
| [SRC-70795F4B61-L000366](../../scripts/compare_answer_quality_runs.py#L366) | 366 | `"    time_metrics = {}"` | — |
| [SRC-70795F4B61-L000367](../../scripts/compare_answer_quality_runs.py#L367) | 367 | `"    for key in (\"mean\", \"p50\", \"p95\", \"max\"):"` | — |
| [SRC-70795F4B61-L000368](../../scripts/compare_answer_quality_runs.py#L368) | 368 | `"        before = before_runtime[\"latency_ms\"][key]"` | — |
| [SRC-70795F4B61-L000369](../../scripts/compare_answer_quality_runs.py#L369) | 369 | `"        after = after_runtime[\"latency_ms\"][key]"` | — |
| [SRC-70795F4B61-L000370](../../scripts/compare_answer_quality_runs.py#L370) | 370 | `"        time_metrics[key] = {"` | — |
| [SRC-70795F4B61-L000371](../../scripts/compare_answer_quality_runs.py#L371) | 371 | `"            \"baseline_ms\": before,"` | — |
| [SRC-70795F4B61-L000372](../../scripts/compare_answer_quality_runs.py#L372) | 372 | `"            \"candidate_ms\": after,"` | — |
| [SRC-70795F4B61-L000373](../../scripts/compare_answer_quality_runs.py#L373) | 373 | `"            \"delta_ms\": round(after - before, 2) if before is not None and after is not None else None,"` | — |
| [SRC-70795F4B61-L000374](../../scripts/compare_answer_quality_runs.py#L374) | 374 | `"            \"status\": \"COMPARED\" if before is not None and after is not None else \"NOT_MEASURED\","` | — |
| [SRC-70795F4B61-L000375](../../scripts/compare_answer_quality_runs.py#L375) | 375 | `"        }"` | — |
| [SRC-70795F4B61-L000376](../../scripts/compare_answer_quality_runs.py#L376) | 376 | `""` | — |
| [SRC-70795F4B61-L000377](../../scripts/compare_answer_quality_runs.py#L377) | 377 | `"    cost_before = before_runtime[\"provider_reported_model_cost\"][\"reported_sum_usd\"]"` | — |
| [SRC-70795F4B61-L000378](../../scripts/compare_answer_quality_runs.py#L378) | 378 | `"    cost_after = after_runtime[\"provider_reported_model_cost\"][\"reported_sum_usd\"]"` | — |
| [SRC-70795F4B61-L000379](../../scripts/compare_answer_quality_runs.py#L379) | 379 | `"    cost_delta = round(cost_after - cost_before, 10) if cost_before is not None and cost_after is not None else None"` | — |
| [SRC-70795F4B61-L000380](../../scripts/compare_answer_quality_runs.py#L380) | 380 | `"    request_cost_before = before_runtime[\"provider_reported_model_cost\"][\"complete_request_cost_usd\"]"` | — |
| [SRC-70795F4B61-L000381](../../scripts/compare_answer_quality_runs.py#L381) | 381 | `"    request_cost_after = after_runtime[\"provider_reported_model_cost\"][\"complete_request_cost_usd\"]"` | — |
| [SRC-70795F4B61-L000382](../../scripts/compare_answer_quality_runs.py#L382) | 382 | `"    request_cost_delta = ("` | — |
| [SRC-70795F4B61-L000383](../../scripts/compare_answer_quality_runs.py#L383) | 383 | `"        round(request_cost_after - request_cost_before, 10)"` | — |
| [SRC-70795F4B61-L000384](../../scripts/compare_answer_quality_runs.py#L384) | 384 | `"        if request_cost_before is not None and request_cost_after is not None"` | — |
| [SRC-70795F4B61-L000385](../../scripts/compare_answer_quality_runs.py#L385) | 385 | `"        else None"` | — |
| [SRC-70795F4B61-L000386](../../scripts/compare_answer_quality_runs.py#L386) | 386 | `"    )"` | — |
| [SRC-70795F4B61-L000387](../../scripts/compare_answer_quality_runs.py#L387) | 387 | `"    runtime_deltas = {"` | — |
| [SRC-70795F4B61-L000388](../../scripts/compare_answer_quality_runs.py#L388) | 388 | `"        \"complete_request_cost_usd\": {"` | — |
| [SRC-70795F4B61-L000389](../../scripts/compare_answer_quality_runs.py#L389) | 389 | `"            \"baseline\": request_cost_before,"` | — |
| [SRC-70795F4B61-L000390](../../scripts/compare_answer_quality_runs.py#L390) | 390 | `"            \"candidate\": request_cost_after,"` | — |
| [SRC-70795F4B61-L000391](../../scripts/compare_answer_quality_runs.py#L391) | 391 | `"            \"delta\": request_cost_delta,"` | — |
| [SRC-70795F4B61-L000392](../../scripts/compare_answer_quality_runs.py#L392) | 392 | `"            \"status\": ("` | — |
| [SRC-70795F4B61-L000393](../../scripts/compare_answer_quality_runs.py#L393) | 393 | `"                \"COMPARED\""` | — |
| [SRC-70795F4B61-L000394](../../scripts/compare_answer_quality_runs.py#L394) | 394 | `"                if request_cost_before is not None and request_cost_after is not None"` | — |
| [SRC-70795F4B61-L000395](../../scripts/compare_answer_quality_runs.py#L395) | 395 | `"                else \"NOT_MEASURED_OR_INCOMPLETE_RECONCILIATION\""` | — |
| [SRC-70795F4B61-L000396](../../scripts/compare_answer_quality_runs.py#L396) | 396 | `"            ),"` | — |
| [SRC-70795F4B61-L000397](../../scripts/compare_answer_quality_runs.py#L397) | 397 | `"        },"` | — |
| [SRC-70795F4B61-L000398](../../scripts/compare_answer_quality_runs.py#L398) | 398 | `"        \"transport_success_rate\": {"` | — |
| [SRC-70795F4B61-L000399](../../scripts/compare_answer_quality_runs.py#L399) | 399 | `"            \"baseline\": before_runtime[\"transport_success_rate\"][\"score\"],"` | — |
| [SRC-70795F4B61-L000400](../../scripts/compare_answer_quality_runs.py#L400) | 400 | `"            \"candidate\": after_runtime[\"transport_success_rate\"][\"score\"],"` | — |
| [SRC-70795F4B61-L000401](../../scripts/compare_answer_quality_runs.py#L401) | 401 | `"        },"` | — |
| [SRC-70795F4B61-L000402](../../scripts/compare_answer_quality_runs.py#L402) | 402 | `"        \"usable_result_rate\": {"` | — |
| [SRC-70795F4B61-L000403](../../scripts/compare_answer_quality_runs.py#L403) | 403 | `"            \"baseline\": before_runtime[\"tool_usage\"][\"usable_result_rate\"][\"score\"],"` | — |
| [SRC-70795F4B61-L000404](../../scripts/compare_answer_quality_runs.py#L404) | 404 | `"            \"candidate\": after_runtime[\"tool_usage\"][\"usable_result_rate\"][\"score\"],"` | — |
| [SRC-70795F4B61-L000405](../../scripts/compare_answer_quality_runs.py#L405) | 405 | `"        },"` | — |
| [SRC-70795F4B61-L000406](../../scripts/compare_answer_quality_runs.py#L406) | 406 | `"        \"required_tool_success_rate\": {"` | — |
| [SRC-70795F4B61-L000407](../../scripts/compare_answer_quality_runs.py#L407) | 407 | `"            \"baseline\": before_runtime[\"tool_usage\"][\"required_tool_success_rate\"][\"score\"],"` | — |
| [SRC-70795F4B61-L000408](../../scripts/compare_answer_quality_runs.py#L408) | 408 | `"            \"candidate\": after_runtime[\"tool_usage\"][\"required_tool_success_rate\"][\"score\"],"` | — |
| [SRC-70795F4B61-L000409](../../scripts/compare_answer_quality_runs.py#L409) | 409 | `"        },"` | — |
| [SRC-70795F4B61-L000410](../../scripts/compare_answer_quality_runs.py#L410) | 410 | `"        \"provider_reported_model_cost_usd\": {"` | — |
| [SRC-70795F4B61-L000411](../../scripts/compare_answer_quality_runs.py#L411) | 411 | `"            \"baseline\": cost_before,"` | — |
| [SRC-70795F4B61-L000412](../../scripts/compare_answer_quality_runs.py#L412) | 412 | `"            \"candidate\": cost_after,"` | — |
| [SRC-70795F4B61-L000413](../../scripts/compare_answer_quality_runs.py#L413) | 413 | `"            \"delta\": cost_delta,"` | — |
| [SRC-70795F4B61-L000414](../../scripts/compare_answer_quality_runs.py#L414) | 414 | `"            \"status\": ("` | — |
| [SRC-70795F4B61-L000415](../../scripts/compare_answer_quality_runs.py#L415) | 415 | `"                \"PARTIAL_OR_PROVIDER_REPORTED_ONLY\""` | — |
| [SRC-70795F4B61-L000416](../../scripts/compare_answer_quality_runs.py#L416) | 416 | `"                if cost_before is not None and cost_after is not None"` | — |
| [SRC-70795F4B61-L000417](../../scripts/compare_answer_quality_runs.py#L417) | 417 | `"                else \"NOT_MEASURED\""` | — |
| [SRC-70795F4B61-L000418](../../scripts/compare_answer_quality_runs.py#L418) | 418 | `"            ),"` | — |
| [SRC-70795F4B61-L000419](../../scripts/compare_answer_quality_runs.py#L419) | 419 | `"        },"` | — |
| [SRC-70795F4B61-L000420](../../scripts/compare_answer_quality_runs.py#L420) | 420 | `"    }"` | — |
| [SRC-70795F4B61-L000421](../../scripts/compare_answer_quality_runs.py#L421) | 421 | `"    for key in (\"transport_success_rate\", \"usable_result_rate\", \"required_tool_success_rate\"):"` | — |
| [SRC-70795F4B61-L000422](../../scripts/compare_answer_quality_runs.py#L422) | 422 | `"        before = runtime_deltas[key][\"baseline\"]"` | — |
| [SRC-70795F4B61-L000423](../../scripts/compare_answer_quality_runs.py#L423) | 423 | `"        after = runtime_deltas[key][\"candidate\"]"` | — |
| [SRC-70795F4B61-L000424](../../scripts/compare_answer_quality_runs.py#L424) | 424 | `"        runtime_deltas[key][\"delta\"] = round(after - before, 4) if before is not None and after is not None else None"` | — |
| [SRC-70795F4B61-L000425](../../scripts/compare_answer_quality_runs.py#L425) | 425 | `"    comparison: dict[str, Any] = {"` | — |
| [SRC-70795F4B61-L000426](../../scripts/compare_answer_quality_runs.py#L426) | 426 | `"        \"schema_version\": \"1.0\","` | — |
| [SRC-70795F4B61-L000427](../../scripts/compare_answer_quality_runs.py#L427) | 427 | `"        \"benchmark_id\": baseline[\"benchmark_id\"],"` | — |
| [SRC-70795F4B61-L000428](../../scripts/compare_answer_quality_runs.py#L428) | 428 | `"        \"benchmark_version\": baseline[\"benchmark_version\"],"` | — |
| [SRC-70795F4B61-L000429](../../scripts/compare_answer_quality_runs.py#L429) | 429 | `"        \"case_count\": len(baseline_by_id),"` | — |
| [SRC-70795F4B61-L000430](../../scripts/compare_answer_quality_runs.py#L430) | 430 | `"        \"baseline\": {"` | — |
| [SRC-70795F4B61-L000431](../../scripts/compare_answer_quality_runs.py#L431) | 431 | `"            \"build_sha\": baseline.get(\"build_sha\", \"unknown\"),"` | — |
| [SRC-70795F4B61-L000432](../../scripts/compare_answer_quality_runs.py#L432) | 432 | `"            \"executed_at_utc\": baseline.get(\"executed_at_utc\"),"` | — |
| [SRC-70795F4B61-L000433](../../scripts/compare_answer_quality_runs.py#L433) | 433 | `"            \"metrics\": before_runtime,"` | — |
| [SRC-70795F4B61-L000434](../../scripts/compare_answer_quality_runs.py#L434) | 434 | `"        },"` | — |
| [SRC-70795F4B61-L000435](../../scripts/compare_answer_quality_runs.py#L435) | 435 | `"        \"candidate\": {"` | — |
| [SRC-70795F4B61-L000436](../../scripts/compare_answer_quality_runs.py#L436) | 436 | `"            \"build_sha\": candidate.get(\"build_sha\", \"unknown\"),"` | — |
| [SRC-70795F4B61-L000437](../../scripts/compare_answer_quality_runs.py#L437) | 437 | `"            \"executed_at_utc\": candidate.get(\"executed_at_utc\"),"` | — |
| [SRC-70795F4B61-L000438](../../scripts/compare_answer_quality_runs.py#L438) | 438 | `"            \"metrics\": after_runtime,"` | — |
| [SRC-70795F4B61-L000439](../../scripts/compare_answer_quality_runs.py#L439) | 439 | `"        },"` | — |
| [SRC-70795F4B61-L000440](../../scripts/compare_answer_quality_runs.py#L440) | 440 | `"        \"runtime_deltas\": runtime_deltas,"` | — |
| [SRC-70795F4B61-L000441](../../scripts/compare_answer_quality_runs.py#L441) | 441 | `"        \"latency_comparison\": time_metrics,"` | — |
| [SRC-70795F4B61-L000442](../../scripts/compare_answer_quality_runs.py#L442) | 442 | `"        \"quality_comparison\": None,"` | — |
| [SRC-70795F4B61-L000443](../../scripts/compare_answer_quality_runs.py#L443) | 443 | `"        \"acceptance_status\": \"PARTIAL\","` | — |
| [SRC-70795F4B61-L000444](../../scripts/compare_answer_quality_runs.py#L444) | 444 | `"        \"acceptance_blockers\": [],"` | — |
| [SRC-70795F4B61-L000445](../../scripts/compare_answer_quality_runs.py#L445) | 445 | `"        \"interpretation\": ["` | — |
| [SRC-70795F4B61-L000446](../../scripts/compare_answer_quality_runs.py#L446) | 446 | `"            \"The same benchmark version, case IDs, and exact question text were compared.\","` | — |
| [SRC-70795F4B61-L000447](../../scripts/compare_answer_quality_runs.py#L447) | 447 | `"            \"HTTP transport success is not semantic correctness, and a successful search request is not proof that the answer is correct.\","` | — |
| [SRC-70795F4B61-L000448](../../scripts/compare_answer_quality_runs.py#L448) | 448 | `"            \"Required-tool success is scored only from complete tool-status matrices; missing required rows count as failures and block complete acceptance.\","` | — |
| [SRC-70795F4B61-L000449](../../scripts/compare_answer_quality_runs.py#L449) | 449 | `"            \"Complete request cost is intentionally null because search connector costs are not consistently exposed; only explicit provider-reported model cost is summarized.\","` | — |
| [SRC-70795F4B61-L000450](../../scripts/compare_answer_quality_runs.py#L450) | 450 | `"        ],"` | — |
| [SRC-70795F4B61-L000451](../../scripts/compare_answer_quality_runs.py#L451) | 451 | `"    }"` | — |
| [SRC-70795F4B61-L000452](../../scripts/compare_answer_quality_runs.py#L452) | 452 | `"    for label, metrics in ((\"baseline\", before_runtime), (\"candidate\", after_runtime)):"` | — |
| [SRC-70795F4B61-L000453](../../scripts/compare_answer_quality_runs.py#L453) | 453 | `"        matrix_coverage = metrics[\"tool_usage\"][\"required_tool_matrix_coverage\"]"` | — |
| [SRC-70795F4B61-L000454](../../scripts/compare_answer_quality_runs.py#L454) | 454 | `"        if ("` | — |
| [SRC-70795F4B61-L000455](../../scripts/compare_answer_quality_runs.py#L455) | 455 | `"            matrix_coverage[\"status\"] != \"SCORED_FROM_EXPLICIT_TOOL_MATRIX\""` | — |
| [SRC-70795F4B61-L000456](../../scripts/compare_answer_quality_runs.py#L456) | 456 | `"            or matrix_coverage[\"score\"] != 1.0"` | — |
| [SRC-70795F4B61-L000457](../../scripts/compare_answer_quality_runs.py#L457) | 457 | `"        ):"` | — |
| [SRC-70795F4B61-L000458](../../scripts/compare_answer_quality_runs.py#L458) | 458 | `"            comparison[\"acceptance_blockers\"].append("` | — |
| [SRC-70795F4B61-L000459](../../scripts/compare_answer_quality_runs.py#L459) | 459 | `"                f\"{label}_required_tool_matrix_incomplete\""` | — |
| [SRC-70795F4B61-L000460](../../scripts/compare_answer_quality_runs.py#L460) | 460 | `"            )"` | — |
| [SRC-70795F4B61-L000461](../../scripts/compare_answer_quality_runs.py#L461) | 461 | `"    sha_re = re.compile(r\"^[0-9a-fA-F]{40}$\")"` | — |
| [SRC-70795F4B61-L000462](../../scripts/compare_answer_quality_runs.py#L462) | 462 | `"    for label, run in ((\"baseline\", baseline), (\"candidate\", candidate)):"` | — |
| [SRC-70795F4B61-L000463](../../scripts/compare_answer_quality_runs.py#L463) | 463 | `"        if not isinstance(run.get(\"build_sha\"), str) or not sha_re.fullmatch(run[\"build_sha\"]):"` | — |
| [SRC-70795F4B61-L000464](../../scripts/compare_answer_quality_runs.py#L464) | 464 | `"            comparison[\"acceptance_blockers\"].append(f\"{label}_build_sha_missing_or_invalid\")"` | — |
| [SRC-70795F4B61-L000465](../../scripts/compare_answer_quality_runs.py#L465) | 465 | `"    for label, metrics in ((\"baseline\", before_runtime), (\"candidate\", after_runtime)):"` | — |
| [SRC-70795F4B61-L000466](../../scripts/compare_answer_quality_runs.py#L466) | 466 | `"        if metrics[\"provider_reported_model_cost\"][\"complete_request_cost_status\"] != \"RECONCILED_COMPLETE_REQUEST_COST\":"` | — |
| [SRC-70795F4B61-L000467](../../scripts/compare_answer_quality_runs.py#L467) | 467 | `"            comparison[\"acceptance_blockers\"].append(f\"{label}_complete_request_cost_missing_or_partial\")"` | — |
| [SRC-70795F4B61-L000468](../../scripts/compare_answer_quality_runs.py#L468) | 468 | `"    if baseline_reviews is None and candidate_reviews is None:"` | — |
| [SRC-70795F4B61-L000469](../../scripts/compare_answer_quality_runs.py#L469) | 469 | `"        comparison[\"acceptance_blockers\"].append(\"human_review_files_missing\")"` | — |
| [SRC-70795F4B61-L000470](../../scripts/compare_answer_quality_runs.py#L470) | 470 | `"    elif baseline_reviews is None or candidate_reviews is None or corpus is None:"` | — |
| [SRC-70795F4B61-L000471](../../scripts/compare_answer_quality_runs.py#L471) | 471 | `"        comparison[\"acceptance_blockers\"].append(\"both_review_files_and_corpus_are_required\")"` | — |
| [SRC-70795F4B61-L000472](../../scripts/compare_answer_quality_runs.py#L472) | 472 | `"    else:"` | — |
| [SRC-70795F4B61-L000473](../../scripts/compare_answer_quality_runs.py#L473) | 473 | `"        corpus_ids = {"` | — |
| [SRC-70795F4B61-L000474](../../scripts/compare_answer_quality_runs.py#L474) | 474 | `"            case.get(\"case_id\")"` | — |
| [SRC-70795F4B61-L000475](../../scripts/compare_answer_quality_runs.py#L475) | 475 | `"            for case in corpus.get(\"cases\", [])"` | — |
| [SRC-70795F4B61-L000476](../../scripts/compare_answer_quality_runs.py#L476) | 476 | `"            if isinstance(case, dict) and isinstance(case.get(\"case_id\"), str)"` | — |
| [SRC-70795F4B61-L000477](../../scripts/compare_answer_quality_runs.py#L477) | 477 | `"        }"` | — |
| [SRC-70795F4B61-L000478](../../scripts/compare_answer_quality_runs.py#L478) | 478 | `"        if set(baseline_by_id) != corpus_ids:"` | — |
| [SRC-70795F4B61-L000479](../../scripts/compare_answer_quality_runs.py#L479) | 479 | `"            comparison[\"acceptance_blockers\"].append(\"benchmark_run_does_not_cover_entire_corpus\")"` | — |
| [SRC-70795F4B61-L000480](../../scripts/compare_answer_quality_runs.py#L480) | 480 | `"        comparison[\"quality_comparison\"] = review_comparison("` | — |
| [SRC-70795F4B61-L000481](../../scripts/compare_answer_quality_runs.py#L481) | 481 | `"            baseline_reviews, candidate_reviews, corpus"` | — |
| [SRC-70795F4B61-L000482](../../scripts/compare_answer_quality_runs.py#L482) | 482 | `"        )"` | — |
| [SRC-70795F4B61-L000483](../../scripts/compare_answer_quality_runs.py#L483) | 483 | `"        unscored_quality = ["` | — |
| [SRC-70795F4B61-L000484](../../scripts/compare_answer_quality_runs.py#L484) | 484 | `"            name for name, metric in comparison[\"quality_comparison\"][\"metrics\"].items()"` | — |
| [SRC-70795F4B61-L000485](../../scripts/compare_answer_quality_runs.py#L485) | 485 | `"            if metric[\"status\"] != \"COMPARED\""` | — |
| [SRC-70795F4B61-L000486](../../scripts/compare_answer_quality_runs.py#L486) | 486 | `"        ]"` | — |
| [SRC-70795F4B61-L000487](../../scripts/compare_answer_quality_runs.py#L487) | 487 | `"        if unscored_quality:"` | — |
| [SRC-70795F4B61-L000488](../../scripts/compare_answer_quality_runs.py#L488) | 488 | `"            comparison[\"acceptance_blockers\"].append("` | — |
| [SRC-70795F4B61-L000489](../../scripts/compare_answer_quality_runs.py#L489) | 489 | `"                \"required_quality_metrics_unscored:\" + \",\".join(unscored_quality)"` | — |
| [SRC-70795F4B61-L000490](../../scripts/compare_answer_quality_runs.py#L490) | 490 | `"            )"` | — |
| [SRC-70795F4B61-L000491](../../scripts/compare_answer_quality_runs.py#L491) | 491 | `"    if not comparison[\"acceptance_blockers\"]:"` | — |
| [SRC-70795F4B61-L000492](../../scripts/compare_answer_quality_runs.py#L492) | 492 | `"        comparison[\"acceptance_status\"] = \"COMPARABLE_WITH_REVIEWED_QUALITY_AND_BUILD_IDENTITIES\""` | — |
| [SRC-70795F4B61-L000493](../../scripts/compare_answer_quality_runs.py#L493) | 493 | `"    else:"` | — |
| [SRC-70795F4B61-L000494](../../scripts/compare_answer_quality_runs.py#L494) | 494 | `"        comparison[\"acceptance_status\"] = \"INCOMPLETE\""` | — |
| [SRC-70795F4B61-L000495](../../scripts/compare_answer_quality_runs.py#L495) | 495 | `"    return comparison"` | — |
| [SRC-70795F4B61-L000496](../../scripts/compare_answer_quality_runs.py#L496) | 496 | `""` | — |
| [SRC-70795F4B61-L000497](../../scripts/compare_answer_quality_runs.py#L497) | 497 | `""` | — |
| [SRC-70795F4B61-L000498](../../scripts/compare_answer_quality_runs.py#L498) | 498 | `"def main(argv: list[str] \| None = None) -> int:"` | — |
| [SRC-70795F4B61-L000499](../../scripts/compare_answer_quality_runs.py#L499) | 499 | `"    parser = argparse.ArgumentParser(description=__doc__)"` | — |
| [SRC-70795F4B61-L000500](../../scripts/compare_answer_quality_runs.py#L500) | 500 | `"    parser.add_argument(\"--baseline-run\", type=Path, required=True)"` | — |
| [SRC-70795F4B61-L000501](../../scripts/compare_answer_quality_runs.py#L501) | 501 | `"    parser.add_argument(\"--candidate-run\", type=Path, required=True)"` | — |
| [SRC-70795F4B61-L000502](../../scripts/compare_answer_quality_runs.py#L502) | 502 | `"    parser.add_argument(\"--baseline-reviews\", type=Path)"` | — |
| [SRC-70795F4B61-L000503](../../scripts/compare_answer_quality_runs.py#L503) | 503 | `"    parser.add_argument(\"--candidate-reviews\", type=Path)"` | — |
| [SRC-70795F4B61-L000504](../../scripts/compare_answer_quality_runs.py#L504) | 504 | `"    parser.add_argument(\"--corpus\", type=Path, default=DEFAULT_CORPUS)"` | — |
| [SRC-70795F4B61-L000505](../../scripts/compare_answer_quality_runs.py#L505) | 505 | `"    parser.add_argument(\"--out\", type=Path)"` | — |
| [SRC-70795F4B61-L000506](../../scripts/compare_answer_quality_runs.py#L506) | 506 | `"    args = parser.parse_args(argv)"` | — |
| [SRC-70795F4B61-L000507](../../scripts/compare_answer_quality_runs.py#L507) | 507 | `"    if bool(args.baseline_reviews) != bool(args.candidate_reviews):"` | — |
| [SRC-70795F4B61-L000508](../../scripts/compare_answer_quality_runs.py#L508) | 508 | `"        parser.error(\"provide both --baseline-reviews and --candidate-reviews, or neither\")"` | — |
| [SRC-70795F4B61-L000509](../../scripts/compare_answer_quality_runs.py#L509) | 509 | `"    try:"` | — |
| [SRC-70795F4B61-L000510](../../scripts/compare_answer_quality_runs.py#L510) | 510 | `"        baseline = load_json_object(args.baseline_run)"` | — |
| [SRC-70795F4B61-L000511](../../scripts/compare_answer_quality_runs.py#L511) | 511 | `"        candidate = load_json_object(args.candidate_run)"` | — |
| [SRC-70795F4B61-L000512](../../scripts/compare_answer_quality_runs.py#L512) | 512 | `"        corpus = load_json_object(args.corpus) if args.baseline_reviews else None"` | — |
| [SRC-70795F4B61-L000513](../../scripts/compare_answer_quality_runs.py#L513) | 513 | `"        before_reviews = load_json_object(args.baseline_reviews) if args.baseline_reviews else None"` | — |
| [SRC-70795F4B61-L000514](../../scripts/compare_answer_quality_runs.py#L514) | 514 | `"        after_reviews = load_json_object(args.candidate_reviews) if args.candidate_reviews else None"` | — |
| [SRC-70795F4B61-L000515](../../scripts/compare_answer_quality_runs.py#L515) | 515 | `"        result = compare_runs("` | — |
| [SRC-70795F4B61-L000516](../../scripts/compare_answer_quality_runs.py#L516) | 516 | `"            baseline, candidate, corpus=corpus,"` | — |
| [SRC-70795F4B61-L000517](../../scripts/compare_answer_quality_runs.py#L517) | 517 | `"            baseline_reviews=before_reviews, candidate_reviews=after_reviews,"` | — |
| [SRC-70795F4B61-L000518](../../scripts/compare_answer_quality_runs.py#L518) | 518 | `"        )"` | — |
| [SRC-70795F4B61-L000519](../../scripts/compare_answer_quality_runs.py#L519) | 519 | `"    except (OSError, ValueError, TypeError, json.JSONDecodeError, KeyError) as exc:"` | — |
| [SRC-70795F4B61-L000520](../../scripts/compare_answer_quality_runs.py#L520) | 520 | `"        print(\"COMPARISON INVALID: \" + str(exc), file=sys.stderr)"` | — |
| [SRC-70795F4B61-L000521](../../scripts/compare_answer_quality_runs.py#L521) | 521 | `"        return 2"` | — |
| [SRC-70795F4B61-L000522](../../scripts/compare_answer_quality_runs.py#L522) | 522 | `"    output = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True)"` | — |
| [SRC-70795F4B61-L000523](../../scripts/compare_answer_quality_runs.py#L523) | 523 | `"    if args.out:"` | — |
| [SRC-70795F4B61-L000524](../../scripts/compare_answer_quality_runs.py#L524) | 524 | `"        args.out.write_text(output + \"\\n\", encoding=\"utf-8\")"` | — |
| [SRC-70795F4B61-L000525](../../scripts/compare_answer_quality_runs.py#L525) | 525 | `"        print(\"Wrote \" + str(args.out))"` | — |
| [SRC-70795F4B61-L000526](../../scripts/compare_answer_quality_runs.py#L526) | 526 | `"    print(output)"` | — |
| [SRC-70795F4B61-L000527](../../scripts/compare_answer_quality_runs.py#L527) | 527 | `"    return 0 if result[\"acceptance_status\"] == \"COMPARABLE_WITH_REVIEWED_QUALITY_AND_BUILD_IDENTITIES\" else 2"` | — |
| [SRC-70795F4B61-L000528](../../scripts/compare_answer_quality_runs.py#L528) | 528 | `""` | — |
| [SRC-70795F4B61-L000529](../../scripts/compare_answer_quality_runs.py#L529) | 529 | `""` | — |
| [SRC-70795F4B61-L000530](../../scripts/compare_answer_quality_runs.py#L530) | 530 | `"if __name__ == \"__main__\":"` | — |
| [SRC-70795F4B61-L000531](../../scripts/compare_answer_quality_runs.py#L531) | 531 | `"    raise SystemExit(main())"` | — |
## ملفات أخرى

### FILE-A8360B1B03 — [scripts/hosted_smoke_test.py](../../scripts/hosted_smoke_test.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-A8360B1B03-L000001](../../scripts/hosted_smoke_test.py#L1) | 1 | `"#!/usr/bin/env python3"` | — |
| [SRC-A8360B1B03-L000002](../../scripts/hosted_smoke_test.py#L2) | 2 | `"\"\"\"End-to-end smoke test for a deployed Omarai instance; uses only stdlib.\"\"\""` | — |
| [SRC-A8360B1B03-L000003](../../scripts/hosted_smoke_test.py#L3) | 3 | `"from __future__ import annotations"` | — |
| [SRC-A8360B1B03-L000004](../../scripts/hosted_smoke_test.py#L4) | 4 | `""` | — |
| [SRC-A8360B1B03-L000005](../../scripts/hosted_smoke_test.py#L5) | 5 | `"import argparse"` | — |
| [SRC-A8360B1B03-L000006](../../scripts/hosted_smoke_test.py#L6) | 6 | `"import json"` | — |
| [SRC-A8360B1B03-L000007](../../scripts/hosted_smoke_test.py#L7) | 7 | `"import os"` | — |
| [SRC-A8360B1B03-L000008](../../scripts/hosted_smoke_test.py#L8) | 8 | `"import re"` | — |
| [SRC-A8360B1B03-L000009](../../scripts/hosted_smoke_test.py#L9) | 9 | `"import sys"` | — |
