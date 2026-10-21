# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **001**
- سجلات الأسطر: **800**
- النطاق: SRC-2F754321D6-L000001 إلى SRC-5587371288-L000044
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## إعدادات وتشغيل

### FILE-2F754321D6 — [.dockerignore](../../.dockerignore#L1)

- النوع: **بدون امتداد**
- نطاق الفهرسة: جرد ملف نصي فقط

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-2F754321D6-L000001](../../.dockerignore#L1) | 1 | `".git"` | — |
| [SRC-2F754321D6-L000002](../../.dockerignore#L2) | 2 | `".github"` | — |
| [SRC-2F754321D6-L000003](../../.dockerignore#L3) | 3 | `".pytest_cache"` | — |
| [SRC-2F754321D6-L000004](../../.dockerignore#L4) | 4 | `".ruff_cache"` | — |
| [SRC-2F754321D6-L000005](../../.dockerignore#L5) | 5 | `"__pycache__"` | — |
| [SRC-2F754321D6-L000006](../../.dockerignore#L6) | 6 | `"*.py[cod]"` | — |
| [SRC-2F754321D6-L000007](../../.dockerignore#L7) | 7 | `"*.sqlite3"` | — |
| [SRC-2F754321D6-L000008](../../.dockerignore#L8) | 8 | `".env"` | — |
| [SRC-2F754321D6-L000009](../../.dockerignore#L9) | 9 | `".env.*"` | — |
| [SRC-2F754321D6-L000010](../../.dockerignore#L10) | 10 | `"!.env.example"` | — |
| [SRC-2F754321D6-L000011](../../.dockerignore#L11) | 11 | `"tests"` | — |
## ملفات أخرى

### FILE-A3046DA0D1 — [.env.example](../../.env.example#L1)

- النوع: **EXAMPLE**
- نطاق الفهرسة: جرد الملف + أسماء إعدادات عامة إن وجدت

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-A3046DA0D1-L000001](../../.env.example#L1) | 1 | `"# Required for a hosted production deployment. Generate a random secret with:"` | — |
| [SRC-A3046DA0D1-L000002](../../.env.example#L2) | 2 | `"# python -c \"import secrets; print(secrets.token_urlsafe(48))\""` | — |
| [SRC-A3046DA0D1-L000003](../../.env.example#L3) | 3 | `"OMARAI_PUBLIC_DEPLOYMENT=1"` | — |
| [SRC-A3046DA0D1-L000004](../../.env.example#L4) | 4 | `"OMARAI_ACCESS_TOKEN=replace-with-a-random-secret-at-least-32-characters"` | — |
| [SRC-A3046DA0D1-L000005](../../.env.example#L5) | 5 | `"OPENROUTER_API_KEY=replace-with-your-own-provider-key"` | — |
| [SRC-A3046DA0D1-L000006](../../.env.example#L6) | 6 | `""` | — |
| [SRC-A3046DA0D1-L000007](../../.env.example#L7) | 7 | `"# Optional: pin stable/paid models after checking current availability and price."` | — |
| [SRC-A3046DA0D1-L000008](../../.env.example#L8) | 8 | `"# OMARAI_PLANNER_MODEL=provider/model-id"` | — |
| [SRC-A3046DA0D1-L000009](../../.env.example#L9) | 9 | `"# OMARAI_ANSWER_MODEL=provider/model-id"` | — |
| [SRC-A3046DA0D1-L000010](../../.env.example#L10) | 10 | `"# OMARAI_REVIEW_MODEL=provider/model-id"` | — |
| [SRC-A3046DA0D1-L000011](../../.env.example#L11) | 11 | `"# OMARAI_LLM_FALLBACK_MODEL=openrouter/free"` | — |
| [SRC-A3046DA0D1-L000012](../../.env.example#L12) | 12 | `""` | — |
| [SRC-A3046DA0D1-L000013](../../.env.example#L13) | 13 | `"# Optional OpenRouter live web-search server tool; uses provider search and may incur charges."` | — |
| [SRC-A3046DA0D1-L000014](../../.env.example#L14) | 14 | `"# OMARAI_OPENROUTER_WEB_SEARCH=1"` | — |
| [SRC-A3046DA0D1-L000015](../../.env.example#L15) | 15 | `""` | — |
| [SRC-A3046DA0D1-L000016](../../.env.example#L16) | 16 | `"# Optional live search APIs; may require separate accounts/credits."` | — |
| [SRC-A3046DA0D1-L000017](../../.env.example#L17) | 17 | `"# BRAVE_SEARCH_API_KEY="` | — |
| [SRC-A3046DA0D1-L000018](../../.env.example#L18) | 18 | `"# TAVILY_API_KEY="` | — |
| [SRC-A3046DA0D1-L000019](../../.env.example#L19) | 19 | `""` | — |
| [SRC-A3046DA0D1-L000020](../../.env.example#L20) | 20 | `""` | — |
| [SRC-A3046DA0D1-L000021](../../.env.example#L21) | 21 | `"# Optional experimental search comparison provider; disabled unless configured."` | — |
| [SRC-A3046DA0D1-L000022](../../.env.example#L22) | 22 | `"# DeepSeek Search/Fetch are paid per successful request (see official pricing/docs)."` | — |
| [SRC-A3046DA0D1-L000023](../../.env.example#L23) | 23 | `"# Do not enable without approval; keep DuckDuckGo/Bing as fallbacks during evaluation."` | — |
| [SRC-A3046DA0D1-L000024](../../.env.example#L24) | 24 | `"# DEEPSEEK_SEARCH_API_KEY="` | — |
| [SRC-A3046DA0D1-L000025](../../.env.example#L25) | 25 | `"# Optional cap per user question/diagnostic operation: integer from 0 to 3 (default 1)."` | — |
| [SRC-A3046DA0D1-L000026](../../.env.example#L26) | 26 | `"# OMARAI_DEEPSEEK_SEARCH_REQUEST_BUDGET=1"` | — |
## CI وأتمتة

### FILE-9F6E30987B — [.github/workflows/hosted-smoke.yml](../../.github/workflows/hosted-smoke.yml#L1)

- النوع: **YAML**
- نطاق الفهرسة: جرد الملف + مفاتيح إعداد ساكنة

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-9F6E30987B-L000001](../../.github/workflows/hosted-smoke.yml#L1) | 1 | `"name: Omarai hosted acceptance smoke"` | — |
| [SRC-9F6E30987B-L000002](../../.github/workflows/hosted-smoke.yml#L2) | 2 | `""` | — |
| [SRC-9F6E30987B-L000003](../../.github/workflows/hosted-smoke.yml#L3) | 3 | `"on:"` | — |
| [SRC-9F6E30987B-L000004](../../.github/workflows/hosted-smoke.yml#L4) | 4 | `"  workflow_dispatch:"` | — |
| [SRC-9F6E30987B-L000005](../../.github/workflows/hosted-smoke.yml#L5) | 5 | `""` | — |
| [SRC-9F6E30987B-L000006](../../.github/workflows/hosted-smoke.yml#L6) | 6 | `"permissions:"` | — |
| [SRC-9F6E30987B-L000007](../../.github/workflows/hosted-smoke.yml#L7) | 7 | `"  contents: read"` | — |
| [SRC-9F6E30987B-L000008](../../.github/workflows/hosted-smoke.yml#L8) | 8 | `""` | — |
| [SRC-9F6E30987B-L000009](../../.github/workflows/hosted-smoke.yml#L9) | 9 | `"concurrency:"` | — |
| [SRC-9F6E30987B-L000010](../../.github/workflows/hosted-smoke.yml#L10) | 10 | `"  group: omarai-hosted-smoke"` | — |
| [SRC-9F6E30987B-L000011](../../.github/workflows/hosted-smoke.yml#L11) | 11 | `"  cancel-in-progress: false"` | — |
| [SRC-9F6E30987B-L000012](../../.github/workflows/hosted-smoke.yml#L12) | 12 | `""` | — |
| [SRC-9F6E30987B-L000013](../../.github/workflows/hosted-smoke.yml#L13) | 13 | `"jobs:"` | — |
| [SRC-9F6E30987B-L000014](../../.github/workflows/hosted-smoke.yml#L14) | 14 | `"  hosted-smoke:"` | — |
| [SRC-9F6E30987B-L000015](../../.github/workflows/hosted-smoke.yml#L15) | 15 | `"    runs-on: ubuntu-latest"` | — |
| [SRC-9F6E30987B-L000016](../../.github/workflows/hosted-smoke.yml#L16) | 16 | `"    timeout-minutes: 8"` | — |
| [SRC-9F6E30987B-L000017](../../.github/workflows/hosted-smoke.yml#L17) | 17 | `"    env:"` | — |
| [SRC-9F6E30987B-L000018](../../.github/workflows/hosted-smoke.yml#L18) | 18 | `"      OMARAI_BASE_URL: ${{ secrets.OMARAI_BASE_URL }}"` | — |
| [SRC-9F6E30987B-L000019](../../.github/workflows/hosted-smoke.yml#L19) | 19 | `"      OMARAI_ACCESS_TOKEN: ${{ secrets.OMARAI_ACCESS_TOKEN }}"` | — |
| [SRC-9F6E30987B-L000020](../../.github/workflows/hosted-smoke.yml#L20) | 20 | `"    steps:"` | — |
| [SRC-9F6E30987B-L000021](../../.github/workflows/hosted-smoke.yml#L21) | 21 | `"      - name: Verify hosted target and access-token secrets are available"` | — |
| [SRC-9F6E30987B-L000022](../../.github/workflows/hosted-smoke.yml#L22) | 22 | `"        shell: bash"` | — |
| [SRC-9F6E30987B-L000023](../../.github/workflows/hosted-smoke.yml#L23) | 23 | `"        run: \|"` | — |
| [SRC-9F6E30987B-L000024](../../.github/workflows/hosted-smoke.yml#L24) | 24 | `"          if [[ -z \"${OMARAI_ACCESS_TOKEN}\" \|\| ${#OMARAI_ACCESS_TOKEN} -lt 32 ]]; then"` | — |
| [SRC-9F6E30987B-L000025](../../.github/workflows/hosted-smoke.yml#L25) | 25 | `"            echo \"::error::GitHub Actions secret OMARAI_ACCESS_TOKEN is missing or too short.\""` | — |
| [SRC-9F6E30987B-L000026](../../.github/workflows/hosted-smoke.yml#L26) | 26 | `"            exit 1"` | — |
| [SRC-9F6E30987B-L000027](../../.github/workflows/hosted-smoke.yml#L27) | 27 | `"          fi"` | — |
| [SRC-9F6E30987B-L000028](../../.github/workflows/hosted-smoke.yml#L28) | 28 | `"          if [[ -z \"${OMARAI_BASE_URL}\" ]]; then"` | — |
| [SRC-9F6E30987B-L000029](../../.github/workflows/hosted-smoke.yml#L29) | 29 | `"            echo \"::error::GitHub Actions secret OMARAI_BASE_URL is missing.\""` | — |
| [SRC-9F6E30987B-L000030](../../.github/workflows/hosted-smoke.yml#L30) | 30 | `"            exit 1"` | — |
| [SRC-9F6E30987B-L000031](../../.github/workflows/hosted-smoke.yml#L31) | 31 | `"          fi"` | — |
| [SRC-9F6E30987B-L000032](../../.github/workflows/hosted-smoke.yml#L32) | 32 | `"          if [[ \"${OMARAI_BASE_URL}\" != https://* \|\| \"${OMARAI_BASE_URL}\" == *\\?* \|\| \"${OMARAI_BASE_URL}\" == *\\#* ]]; then"` | — |
| [SRC-9F6E30987B-L000033](../../.github/workflows/hosted-smoke.yml#L33) | 33 | `"            echo \"::error::OMARAI_BASE_URL must be an HTTPS origin without a path, query, or fragment.\""` | — |
| [SRC-9F6E30987B-L000034](../../.github/workflows/hosted-smoke.yml#L34) | 34 | `"            exit 1"` | — |
| [SRC-9F6E30987B-L000035](../../.github/workflows/hosted-smoke.yml#L35) | 35 | `"          fi"` | — |
| [SRC-9F6E30987B-L000036](../../.github/workflows/hosted-smoke.yml#L36) | 36 | `"          echo \"Hosted target and access-token secrets are present; values not printed.\""` | — |
| [SRC-9F6E30987B-L000037](../../.github/workflows/hosted-smoke.yml#L37) | 37 | `""` | — |
| [SRC-9F6E30987B-L000038](../../.github/workflows/hosted-smoke.yml#L38) | 38 | `"      - name: Check out repository"` | — |
| [SRC-9F6E30987B-L000039](../../.github/workflows/hosted-smoke.yml#L39) | 39 | `"        uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7.0.1"` | — |
| [SRC-9F6E30987B-L000040](../../.github/workflows/hosted-smoke.yml#L40) | 40 | `""` | — |
| [SRC-9F6E30987B-L000041](../../.github/workflows/hosted-smoke.yml#L41) | 41 | `"      - name: Set up Python"` | — |
| [SRC-9F6E30987B-L000042](../../.github/workflows/hosted-smoke.yml#L42) | 42 | `"        uses: actions/setup-python@5fda3b95a4ea91299a34e894583c3862153e4b97 # v7.0.0"` | — |
| [SRC-9F6E30987B-L000043](../../.github/workflows/hosted-smoke.yml#L43) | 43 | `"        with:"` | — |
| [SRC-9F6E30987B-L000044](../../.github/workflows/hosted-smoke.yml#L44) | 44 | `"          python-version: \"3.12\""` | — |
| [SRC-9F6E30987B-L000045](../../.github/workflows/hosted-smoke.yml#L45) | 45 | `""` | — |
| [SRC-9F6E30987B-L000046](../../.github/workflows/hosted-smoke.yml#L46) | 46 | `"      - name: Run live hosted acceptance test"` | — |
| [SRC-9F6E30987B-L000047](../../.github/workflows/hosted-smoke.yml#L47) | 47 | `"        run: python scripts/hosted_smoke_test.py --base-url \"$OMARAI_BASE_URL\" --expected-sha \"$(git rev-parse HEAD)\" --timeout 180"` | — |
## CI وأتمتة

### FILE-1DB27D9318 — [.github/workflows/tests.yml](../../.github/workflows/tests.yml#L1)

- النوع: **YAML**
- نطاق الفهرسة: جرد الملف + مفاتيح إعداد ساكنة

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1DB27D9318-L000001](../../.github/workflows/tests.yml#L1) | 1 | `"name: Omarai tests"` | — |
| [SRC-1DB27D9318-L000002](../../.github/workflows/tests.yml#L2) | 2 | `"on:"` | — |
| [SRC-1DB27D9318-L000003](../../.github/workflows/tests.yml#L3) | 3 | `"  push:"` | — |
| [SRC-1DB27D9318-L000004](../../.github/workflows/tests.yml#L4) | 4 | `"    branches: [\"main\", \"feat/**\", \"fix/**\", \"feature/**\"]"` | — |
| [SRC-1DB27D9318-L000005](../../.github/workflows/tests.yml#L5) | 5 | `"  pull_request:"` | — |
| [SRC-1DB27D9318-L000006](../../.github/workflows/tests.yml#L6) | 6 | `"    branches: [\"main\"]"` | — |
| [SRC-1DB27D9318-L000007](../../.github/workflows/tests.yml#L7) | 7 | `"  workflow_dispatch:"` | — |
| [SRC-1DB27D9318-L000008](../../.github/workflows/tests.yml#L8) | 8 | `"permissions:"` | — |
| [SRC-1DB27D9318-L000009](../../.github/workflows/tests.yml#L9) | 9 | `"  contents: read"` | — |
| [SRC-1DB27D9318-L000010](../../.github/workflows/tests.yml#L10) | 10 | `"jobs:"` | — |
| [SRC-1DB27D9318-L000011](../../.github/workflows/tests.yml#L11) | 11 | `"  test:"` | — |
| [SRC-1DB27D9318-L000012](../../.github/workflows/tests.yml#L12) | 12 | `"    runs-on: ubuntu-latest"` | — |
| [SRC-1DB27D9318-L000013](../../.github/workflows/tests.yml#L13) | 13 | `"    strategy:"` | — |
| [SRC-1DB27D9318-L000014](../../.github/workflows/tests.yml#L14) | 14 | `"      fail-fast: false"` | — |
| [SRC-1DB27D9318-L000015](../../.github/workflows/tests.yml#L15) | 15 | `"      matrix:"` | — |
| [SRC-1DB27D9318-L000016](../../.github/workflows/tests.yml#L16) | 16 | `"        python-version: [\"3.11\", \"3.12\"]"` | — |
| [SRC-1DB27D9318-L000017](../../.github/workflows/tests.yml#L17) | 17 | `"    steps:"` | — |
| [SRC-1DB27D9318-L000018](../../.github/workflows/tests.yml#L18) | 18 | `"      - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7.0.1"` | — |
| [SRC-1DB27D9318-L000019](../../.github/workflows/tests.yml#L19) | 19 | `"      - uses: actions/setup-python@5fda3b95a4ea91299a34e894583c3862153e4b97 # v7.0.0"` | — |
| [SRC-1DB27D9318-L000020](../../.github/workflows/tests.yml#L20) | 20 | `"        with:"` | — |
| [SRC-1DB27D9318-L000021](../../.github/workflows/tests.yml#L21) | 21 | `"          python-version: ${{ matrix.python-version }}"` | — |
| [SRC-1DB27D9318-L000022](../../.github/workflows/tests.yml#L22) | 22 | `"      - run: python -m pip install -e \".[dev]\" ruff"` | — |
| [SRC-1DB27D9318-L000023](../../.github/workflows/tests.yml#L23) | 23 | `"      - run: ruff check agents api cli docs tests"` | — |
| [SRC-1DB27D9318-L000024](../../.github/workflows/tests.yml#L24) | 24 | `"      # PR tests can start before the separate index-publishing workflow finishes"` | — |
| [SRC-1DB27D9318-L000025](../../.github/workflows/tests.yml#L25) | 25 | `"      # pushing its generated files. Regenerate within this isolated checkout first,"` | — |
| [SRC-1DB27D9318-L000026](../../.github/workflows/tests.yml#L26) | 26 | `"      # then verify determinism. The index workflow remains responsible for committing"` | — |
| [SRC-1DB27D9318-L000027](../../.github/workflows/tests.yml#L27) | 27 | `"      # generated artifacts to the branch; main pushes still check the committed index."` | — |
| [SRC-1DB27D9318-L000028](../../.github/workflows/tests.yml#L28) | 28 | `"      - name: Synchronize generated indexes in the PR test workspace"` | — |
| [SRC-1DB27D9318-L000029](../../.github/workflows/tests.yml#L29) | 29 | `"        if: github.event_name == 'pull_request'"` | — |
| [SRC-1DB27D9318-L000030](../../.github/workflows/tests.yml#L30) | 30 | `"        run: python docs/generate_index.py"` | — |
| [SRC-1DB27D9318-L000031](../../.github/workflows/tests.yml#L31) | 31 | `"      - name: Verify generated living indexes against the full repository"` | — |
| [SRC-1DB27D9318-L000032](../../.github/workflows/tests.yml#L32) | 32 | `"        run: python docs/generate_index.py --check"` | — |
| [SRC-1DB27D9318-L000033](../../.github/workflows/tests.yml#L33) | 33 | `"      - run: python -m pytest -q"` | — |
| [SRC-1DB27D9318-L000034](../../.github/workflows/tests.yml#L34) | 34 | `""` | — |
| [SRC-1DB27D9318-L000035](../../.github/workflows/tests.yml#L35) | 35 | `"  container-build:"` | — |
| [SRC-1DB27D9318-L000036](../../.github/workflows/tests.yml#L36) | 36 | `"    runs-on: ubuntu-latest"` | — |
| [SRC-1DB27D9318-L000037](../../.github/workflows/tests.yml#L37) | 37 | `"    steps:"` | — |
| [SRC-1DB27D9318-L000038](../../.github/workflows/tests.yml#L38) | 38 | `"      - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7.0.1"` | — |
| [SRC-1DB27D9318-L000039](../../.github/workflows/tests.yml#L39) | 39 | `"      - name: Build production container"` | — |
| [SRC-1DB27D9318-L000040](../../.github/workflows/tests.yml#L40) | 40 | `"        run: docker build --build-arg OMARAI_BUILD_SHA=\"${GITHUB_SHA}\" --tag omarai:ci ."` | — |
| [SRC-1DB27D9318-L000041](../../.github/workflows/tests.yml#L41) | 41 | `"      - name: Start container and smoke-test protected API"` | — |
| [SRC-1DB27D9318-L000042](../../.github/workflows/tests.yml#L42) | 42 | `"        shell: bash"` | — |
| [SRC-1DB27D9318-L000043](../../.github/workflows/tests.yml#L43) | 43 | `"        run: \|"` | — |
| [SRC-1DB27D9318-L000044](../../.github/workflows/tests.yml#L44) | 44 | `"          set -euo pipefail"` | — |
| [SRC-1DB27D9318-L000045](../../.github/workflows/tests.yml#L45) | 45 | `"          docker run --detach --rm --name omarai-ci \\"` | — |
| [SRC-1DB27D9318-L000046](../../.github/workflows/tests.yml#L46) | 46 | `"            --publish 127.0.0.1:18765:8000 \\"` | — |
| [SRC-1DB27D9318-L000047](../../.github/workflows/tests.yml#L47) | 47 | `"            --env OMARAI_PUBLIC_DEPLOYMENT=1 \\"` | — |
| [SRC-1DB27D9318-L000048](../../.github/workflows/tests.yml#L48) | 48 | `"            --env OMARAI_ACCESS_TOKEN=ci-only-test-token-not-for-production-123456 \\"` | — |
| [SRC-1DB27D9318-L000049](../../.github/workflows/tests.yml#L49) | 49 | `"            omarai:ci"` | — |
| [SRC-1DB27D9318-L000050](../../.github/workflows/tests.yml#L50) | 50 | `"          cleanup() { docker stop omarai-ci >/dev/null 2>&1 \|\| true; }"` | — |
| [SRC-1DB27D9318-L000051](../../.github/workflows/tests.yml#L51) | 51 | `"          trap cleanup EXIT"` | — |
| [SRC-1DB27D9318-L000052](../../.github/workflows/tests.yml#L52) | 52 | `""` | — |
| [SRC-1DB27D9318-L000053](../../.github/workflows/tests.yml#L53) | 53 | `"          healthy=false"` | — |
| [SRC-1DB27D9318-L000054](../../.github/workflows/tests.yml#L54) | 54 | `"          for _ in $(seq 1 30); do"` | — |
| [SRC-1DB27D9318-L000055](../../.github/workflows/tests.yml#L55) | 55 | `"            if curl --silent --fail http://127.0.0.1:18765/api/health \\"` | — |
| [SRC-1DB27D9318-L000056](../../.github/workflows/tests.yml#L56) | 56 | `"              --output /tmp/omarai-health.json; then"` | — |
| [SRC-1DB27D9318-L000057](../../.github/workflows/tests.yml#L57) | 57 | `"              healthy=true"` | — |
| [SRC-1DB27D9318-L000058](../../.github/workflows/tests.yml#L58) | 58 | `"              break"` | — |
| [SRC-1DB27D9318-L000059](../../.github/workflows/tests.yml#L59) | 59 | `"            fi"` | — |
| [SRC-1DB27D9318-L000060](../../.github/workflows/tests.yml#L60) | 60 | `"            sleep 1"` | — |
| [SRC-1DB27D9318-L000061](../../.github/workflows/tests.yml#L61) | 61 | `"          done"` | — |
| [SRC-1DB27D9318-L000062](../../.github/workflows/tests.yml#L62) | 62 | `"          if [[ \"$healthy\" != \"true\" ]]; then"` | — |
| [SRC-1DB27D9318-L000063](../../.github/workflows/tests.yml#L63) | 63 | `"            docker logs omarai-ci"` | — |
| [SRC-1DB27D9318-L000064](../../.github/workflows/tests.yml#L64) | 64 | `"            exit 1"` | — |
| [SRC-1DB27D9318-L000065](../../.github/workflows/tests.yml#L65) | 65 | `"          fi"` | — |
| [SRC-1DB27D9318-L000066](../../.github/workflows/tests.yml#L66) | 66 | `"          python -c 'import json, os; d=json.load(open(\"/tmp/omarai-health.json\", encoding=\"utf-8\")); assert d[\"ok\"] is True; assert d[\"build\"][\"sha\"] == os.environ[\"GITHUB_SHA\"].lower()'"` | — |
| [SRC-1DB27D9318-L000067](../../.github/workflows/tests.yml#L67) | 67 | `""` | — |
| [SRC-1DB27D9318-L000068](../../.github/workflows/tests.yml#L68) | 68 | `"          status=\"$(curl --silent --output /tmp/omarai-unauth.json --write-out \"%{http_code}\" \\"` | — |
| [SRC-1DB27D9318-L000069](../../.github/workflows/tests.yml#L69) | 69 | `"            --header \"Content-Type: application/json\" \\"` | — |
| [SRC-1DB27D9318-L000070](../../.github/workflows/tests.yml#L70) | 70 | `"            --data '{\"question\":\"smoke\"}' http://127.0.0.1:18765/api/agent)\""` | — |
| [SRC-1DB27D9318-L000071](../../.github/workflows/tests.yml#L71) | 71 | `"          if [[ \"$status\" != \"401\" ]]; then"` | — |
| [SRC-1DB27D9318-L000072](../../.github/workflows/tests.yml#L72) | 72 | `"            cat /tmp/omarai-unauth.json"` | — |
| [SRC-1DB27D9318-L000073](../../.github/workflows/tests.yml#L73) | 73 | `"            echo \"Unauthenticated /api/agent should return HTTP 401, got $status.\""` | — |
| [SRC-1DB27D9318-L000074](../../.github/workflows/tests.yml#L74) | 74 | `"            exit 1"` | — |
| [SRC-1DB27D9318-L000075](../../.github/workflows/tests.yml#L75) | 75 | `"          fi"` | — |
| [SRC-1DB27D9318-L000076](../../.github/workflows/tests.yml#L76) | 76 | `""` | — |
| [SRC-1DB27D9318-L000077](../../.github/workflows/tests.yml#L77) | 77 | `"          status=\"$(curl --silent --output /tmp/omarai-leads.json --write-out \"%{http_code}\" \\"` | — |
| [SRC-1DB27D9318-L000078](../../.github/workflows/tests.yml#L78) | 78 | `"            http://127.0.0.1:18765/api/leads)\""` | — |
| [SRC-1DB27D9318-L000079](../../.github/workflows/tests.yml#L79) | 79 | `"          if [[ \"$status\" != \"401\" ]]; then"` | — |
| [SRC-1DB27D9318-L000080](../../.github/workflows/tests.yml#L80) | 80 | `"            cat /tmp/omarai-leads.json"` | — |
| [SRC-1DB27D9318-L000081](../../.github/workflows/tests.yml#L81) | 81 | `"            echo \"Unauthenticated /api/leads should return HTTP 401, got $status.\""` | — |
| [SRC-1DB27D9318-L000082](../../.github/workflows/tests.yml#L82) | 82 | `"            exit 1"` | — |
| [SRC-1DB27D9318-L000083](../../.github/workflows/tests.yml#L83) | 83 | `"          fi"` | — |
| [SRC-1DB27D9318-L000084](../../.github/workflows/tests.yml#L84) | 84 | `""` | — |
| [SRC-1DB27D9318-L000085](../../.github/workflows/tests.yml#L85) | 85 | `"          status=\"$(curl --silent --output /tmp/omarai-leads-auth.json --write-out \"%{http_code}\" \\"` | — |
| [SRC-1DB27D9318-L000086](../../.github/workflows/tests.yml#L86) | 86 | `"            --header \"Authorization: Bearer ci-only-test-token-not-for-production-123456\" \\"` | — |
| [SRC-1DB27D9318-L000087](../../.github/workflows/tests.yml#L87) | 87 | `"            http://127.0.0.1:18765/api/leads)\""` | — |
| [SRC-1DB27D9318-L000088](../../.github/workflows/tests.yml#L88) | 88 | `"          if [[ \"$status\" != \"200\" ]]; then"` | — |
| [SRC-1DB27D9318-L000089](../../.github/workflows/tests.yml#L89) | 89 | `"            cat /tmp/omarai-leads-auth.json"` | — |
| [SRC-1DB27D9318-L000090](../../.github/workflows/tests.yml#L90) | 90 | `"            echo \"Authenticated /api/leads should return HTTP 200, got $status.\""` | — |
| [SRC-1DB27D9318-L000091](../../.github/workflows/tests.yml#L91) | 91 | `"            exit 1"` | — |
| [SRC-1DB27D9318-L000092](../../.github/workflows/tests.yml#L92) | 92 | `"          fi"` | — |
| [SRC-1DB27D9318-L000093](../../.github/workflows/tests.yml#L93) | 93 | `""` | — |
| [SRC-1DB27D9318-L000094](../../.github/workflows/tests.yml#L94) | 94 | `"          status=\"$(curl --silent --output /tmp/omarai-analysis.json --write-out \"%{http_code}\" \\"` | — |
| [SRC-1DB27D9318-L000095](../../.github/workflows/tests.yml#L95) | 95 | `"            --header \"Authorization: Bearer ci-only-test-token-not-for-production-123456\" \\"` | — |
| [SRC-1DB27D9318-L000096](../../.github/workflows/tests.yml#L96) | 96 | `"            --header \"Content-Type: application/json\" \\"` | — |
| [SRC-1DB27D9318-L000097](../../.github/workflows/tests.yml#L97) | 97 | `"            --data '{\"text\":\"بدور على شقة\",\"product_terms\":[\"شقة\"]}' \\"` | — |
| [SRC-1DB27D9318-L000098](../../.github/workflows/tests.yml#L98) | 98 | `"            http://127.0.0.1:18765/api/analyze)\""` | — |
| [SRC-1DB27D9318-L000099](../../.github/workflows/tests.yml#L99) | 99 | `"          if [[ \"$status\" != \"200\" ]]; then"` | — |
| [SRC-1DB27D9318-L000100](../../.github/workflows/tests.yml#L100) | 100 | `"            cat /tmp/omarai-analysis.json"` | — |
| [SRC-1DB27D9318-L000101](../../.github/workflows/tests.yml#L101) | 101 | `"            echo \"Authenticated /api/analyze should return HTTP 200, got $status.\""` | — |
| [SRC-1DB27D9318-L000102](../../.github/workflows/tests.yml#L102) | 102 | `"            exit 1"` | — |
| [SRC-1DB27D9318-L000103](../../.github/workflows/tests.yml#L103) | 103 | `"          fi"` | — |
## CI وأتمتة

### FILE-84F7DE82AF — [.github/workflows/update_index.yml](../../.github/workflows/update_index.yml#L1)

- النوع: **YAML**
- نطاق الفهرسة: جرد الملف + مفاتيح إعداد ساكنة

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-84F7DE82AF-L000001](../../.github/workflows/update_index.yml#L1) | 1 | `"name: Update Omarai complete source and symbol indexes"` | — |
| [SRC-84F7DE82AF-L000002](../../.github/workflows/update_index.yml#L2) | 2 | `""` | — |
| [SRC-84F7DE82AF-L000003](../../.github/workflows/update_index.yml#L3) | 3 | `"on:"` | — |
| [SRC-84F7DE82AF-L000004](../../.github/workflows/update_index.yml#L4) | 4 | `"  push:"` | — |
| [SRC-84F7DE82AF-L000005](../../.github/workflows/update_index.yml#L5) | 5 | `"    branches: [\"main\", \"feat/**\", \"fix/**\", \"feature/**\"]"` | — |
| [SRC-84F7DE82AF-L000006](../../.github/workflows/update_index.yml#L6) | 6 | `"    paths-ignore:"` | — |
| [SRC-84F7DE82AF-L000007](../../.github/workflows/update_index.yml#L7) | 7 | `"      - \"docs/MASTER_INDEX.md\""` | — |
| [SRC-84F7DE82AF-L000008](../../.github/workflows/update_index.yml#L8) | 8 | `"      - \"docs/SOURCE_LINES_INDEX.md\""` | — |
| [SRC-84F7DE82AF-L000009](../../.github/workflows/update_index.yml#L9) | 9 | `"      - \"docs/INDEX_COVERAGE_AUDIT.md\""` | — |
| [SRC-84F7DE82AF-L000010](../../.github/workflows/update_index.yml#L10) | 10 | `"      - \"docs/source_index/**\""` | — |
| [SRC-84F7DE82AF-L000011](../../.github/workflows/update_index.yml#L11) | 11 | `"  workflow_dispatch:"` | — |
| [SRC-84F7DE82AF-L000012](../../.github/workflows/update_index.yml#L12) | 12 | `""` | — |
| [SRC-84F7DE82AF-L000013](../../.github/workflows/update_index.yml#L13) | 13 | `"permissions:"` | — |
| [SRC-84F7DE82AF-L000014](../../.github/workflows/update_index.yml#L14) | 14 | `"  contents: write"` | — |
| [SRC-84F7DE82AF-L000015](../../.github/workflows/update_index.yml#L15) | 15 | `"  pull-requests: write"` | — |
| [SRC-84F7DE82AF-L000016](../../.github/workflows/update_index.yml#L16) | 16 | `""` | — |
| [SRC-84F7DE82AF-L000017](../../.github/workflows/update_index.yml#L17) | 17 | `"# Serialize updates separately per branch. Generated-index-only commits are ignored above."` | — |
| [SRC-84F7DE82AF-L000018](../../.github/workflows/update_index.yml#L18) | 18 | `"concurrency:"` | — |
| [SRC-84F7DE82AF-L000019](../../.github/workflows/update_index.yml#L19) | 19 | `"  group: omarai-living-index-${{ github.ref }}"` | — |
| [SRC-84F7DE82AF-L000020](../../.github/workflows/update_index.yml#L20) | 20 | `"  cancel-in-progress: false"` | — |
| [SRC-84F7DE82AF-L000021](../../.github/workflows/update_index.yml#L21) | 21 | `""` | — |
| [SRC-84F7DE82AF-L000022](../../.github/workflows/update_index.yml#L22) | 22 | `"jobs:"` | — |
| [SRC-84F7DE82AF-L000023](../../.github/workflows/update_index.yml#L23) | 23 | `"  refresh-index:"` | — |
| [SRC-84F7DE82AF-L000024](../../.github/workflows/update_index.yml#L24) | 24 | `"    name: Generate and publish all repository indexes"` | — |
| [SRC-84F7DE82AF-L000025](../../.github/workflows/update_index.yml#L25) | 25 | `"    runs-on: ubuntu-latest"` | — |
| [SRC-84F7DE82AF-L000026](../../.github/workflows/update_index.yml#L26) | 26 | `"    steps:"` | — |
| [SRC-84F7DE82AF-L000027](../../.github/workflows/update_index.yml#L27) | 27 | `"      - name: Check out repository"` | — |
| [SRC-84F7DE82AF-L000028](../../.github/workflows/update_index.yml#L28) | 28 | `"        uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7.0.1"` | — |
| [SRC-84F7DE82AF-L000029](../../.github/workflows/update_index.yml#L29) | 29 | `""` | — |
| [SRC-84F7DE82AF-L000030](../../.github/workflows/update_index.yml#L30) | 30 | `"      - name: Fetch the latest revision of the triggering branch"` | — |
| [SRC-84F7DE82AF-L000031](../../.github/workflows/update_index.yml#L31) | 31 | `"        shell: bash"` | — |
| [SRC-84F7DE82AF-L000032](../../.github/workflows/update_index.yml#L32) | 32 | `"        env:"` | — |
| [SRC-84F7DE82AF-L000033](../../.github/workflows/update_index.yml#L33) | 33 | `"          BRANCH_NAME: ${{ github.ref_name }}"` | — |
| [SRC-84F7DE82AF-L000034](../../.github/workflows/update_index.yml#L34) | 34 | `"        run: \|"` | — |
| [SRC-84F7DE82AF-L000035](../../.github/workflows/update_index.yml#L35) | 35 | `"          set -euo pipefail"` | — |
| [SRC-84F7DE82AF-L000036](../../.github/workflows/update_index.yml#L36) | 36 | `"          git fetch --no-tags origin \"${BRANCH_NAME}\""` | — |
| [SRC-84F7DE82AF-L000037](../../.github/workflows/update_index.yml#L37) | 37 | `"          git checkout --force -B \"${BRANCH_NAME}\" \"origin/${BRANCH_NAME}\""` | — |
| [SRC-84F7DE82AF-L000038](../../.github/workflows/update_index.yml#L38) | 38 | `""` | — |
| [SRC-84F7DE82AF-L000039](../../.github/workflows/update_index.yml#L39) | 39 | `"      - name: Set up Python"` | — |
| [SRC-84F7DE82AF-L000040](../../.github/workflows/update_index.yml#L40) | 40 | `"        uses: actions/setup-python@5fda3b95a4ea91299a34e894583c3862153e4b97 # v7.0.0"` | — |
| [SRC-84F7DE82AF-L000041](../../.github/workflows/update_index.yml#L41) | 41 | `"        with:"` | — |
| [SRC-84F7DE82AF-L000042](../../.github/workflows/update_index.yml#L42) | 42 | `"          python-version: \"3.12\""` | — |
| [SRC-84F7DE82AF-L000043](../../.github/workflows/update_index.yml#L43) | 43 | `""` | — |
| [SRC-84F7DE82AF-L000044](../../.github/workflows/update_index.yml#L44) | 44 | `"      - name: Generate the master, review-marker, and paginated source-line indexes"` | — |
| [SRC-84F7DE82AF-L000045](../../.github/workflows/update_index.yml#L45) | 45 | `"        run: python docs/generate_index.py"` | — |
| [SRC-84F7DE82AF-L000046](../../.github/workflows/update_index.yml#L46) | 46 | `""` | — |
| [SRC-84F7DE82AF-L000047](../../.github/workflows/update_index.yml#L47) | 47 | `"      - name: Verify every generated index and remove stale-page drift"` | — |
| [SRC-84F7DE82AF-L000048](../../.github/workflows/update_index.yml#L48) | 48 | `"        run: python docs/generate_index.py --check"` | — |
| [SRC-84F7DE82AF-L000049](../../.github/workflows/update_index.yml#L49) | 49 | `""` | — |
| [SRC-84F7DE82AF-L000050](../../.github/workflows/update_index.yml#L50) | 50 | `"      - name: Commit and publish the generated indexes only when changed"` | — |
| [SRC-84F7DE82AF-L000051](../../.github/workflows/update_index.yml#L51) | 51 | `"        shell: bash"` | — |
| [SRC-84F7DE82AF-L000052](../../.github/workflows/update_index.yml#L52) | 52 | `"        env:"` | — |
| [SRC-84F7DE82AF-L000053](../../.github/workflows/update_index.yml#L53) | 53 | `"          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}"` | — |
| [SRC-84F7DE82AF-L000054](../../.github/workflows/update_index.yml#L54) | 54 | `"          BRANCH_NAME: ${{ github.ref_name }}"` | — |
| [SRC-84F7DE82AF-L000055](../../.github/workflows/update_index.yml#L55) | 55 | `"        run: \|"` | — |
| [SRC-84F7DE82AF-L000056](../../.github/workflows/update_index.yml#L56) | 56 | `"          set -euo pipefail"` | — |
| [SRC-84F7DE82AF-L000057](../../.github/workflows/update_index.yml#L57) | 57 | `"          git add -- docs/MASTER_INDEX.md docs/SOURCE_LINES_INDEX.md docs/INDEX_COVERAGE_AUDIT.md docs/source_index/"` | — |
| [SRC-84F7DE82AF-L000058](../../.github/workflows/update_index.yml#L58) | 58 | `"          if git diff --cached --quiet; then"` | — |
| [SRC-84F7DE82AF-L000059](../../.github/workflows/update_index.yml#L59) | 59 | `"            echo \"All generated index files are already up to date; no commit is needed.\""` | — |
| [SRC-84F7DE82AF-L000060](../../.github/workflows/update_index.yml#L60) | 60 | `"            exit 0"` | — |
| [SRC-84F7DE82AF-L000061](../../.github/workflows/update_index.yml#L61) | 61 | `"          fi"` | — |
| [SRC-84F7DE82AF-L000062](../../.github/workflows/update_index.yml#L62) | 62 | `""` | — |
| [SRC-84F7DE82AF-L000063](../../.github/workflows/update_index.yml#L63) | 63 | `"          git config user.name \"github-actions[bot]\""` | — |
| [SRC-84F7DE82AF-L000064](../../.github/workflows/update_index.yml#L64) | 64 | `"          git config user.email \"41898282+github-actions[bot]@users.noreply.github.com\""` | — |
| [SRC-84F7DE82AF-L000065](../../.github/workflows/update_index.yml#L65) | 65 | `"          git commit -m \"docs(index): refresh repository source-line inventory\""` | — |
| [SRC-84F7DE82AF-L000066](../../.github/workflows/update_index.yml#L66) | 66 | `""` | — |
| [SRC-84F7DE82AF-L000067](../../.github/workflows/update_index.yml#L67) | 67 | `"          if [[ \"${BRANCH_NAME}\" != \"main\" ]]; then"` | — |
| [SRC-84F7DE82AF-L000068](../../.github/workflows/update_index.yml#L68) | 68 | `"            # Keep feature/fix branches reviewable with their generated index outputs."` | — |
| [SRC-84F7DE82AF-L000069](../../.github/workflows/update_index.yml#L69) | 69 | `"            # This is a normal push; no force update and no merge are performed."` | — |
| [SRC-84F7DE82AF-L000070](../../.github/workflows/update_index.yml#L70) | 70 | `"            git push origin \"HEAD:${BRANCH_NAME}\""` | — |
| [SRC-84F7DE82AF-L000071](../../.github/workflows/update_index.yml#L71) | 71 | `"            echo \"Generated indexes committed to branch ${BRANCH_NAME}.\""` | — |
| [SRC-84F7DE82AF-L000072](../../.github/workflows/update_index.yml#L72) | 72 | `"            exit 0"` | — |
| [SRC-84F7DE82AF-L000073](../../.github/workflows/update_index.yml#L73) | 73 | `"          fi"` | — |
| [SRC-84F7DE82AF-L000074](../../.github/workflows/update_index.yml#L74) | 74 | `""` | — |
| [SRC-84F7DE82AF-L000075](../../.github/workflows/update_index.yml#L75) | 75 | `"          # On main, publish only a fast-forward update. If policy rejects it,"` | — |
| [SRC-84F7DE82AF-L000076](../../.github/workflows/update_index.yml#L76) | 76 | `"          # offer a PR as the fallback; never force-push or auto-merge."` | — |
| [SRC-84F7DE82AF-L000077](../../.github/workflows/update_index.yml#L77) | 77 | `"          if git push origin HEAD:main; then"` | — |
| [SRC-84F7DE82AF-L000078](../../.github/workflows/update_index.yml#L78) | 78 | `"            echo \"Generated indexes were pushed to main.\""` | — |
| [SRC-84F7DE82AF-L000079](../../.github/workflows/update_index.yml#L79) | 79 | `"            exit 0"` | — |
| [SRC-84F7DE82AF-L000080](../../.github/workflows/update_index.yml#L80) | 80 | `"          fi"` | — |
| [SRC-84F7DE82AF-L000081](../../.github/workflows/update_index.yml#L81) | 81 | `""` | — |
| [SRC-84F7DE82AF-L000082](../../.github/workflows/update_index.yml#L82) | 82 | `"          automation_branch=\"automation/living-index\""` | — |
| [SRC-84F7DE82AF-L000083](../../.github/workflows/update_index.yml#L83) | 83 | `"          if ! git push origin \"HEAD:${automation_branch}\"; then"` | — |
| [SRC-84F7DE82AF-L000084](../../.github/workflows/update_index.yml#L84) | 84 | `"            automation_branch=\"automation/living-index-${GITHUB_RUN_ID}\""` | — |
| [SRC-84F7DE82AF-L000085](../../.github/workflows/update_index.yml#L85) | 85 | `"            git push origin \"HEAD:${automation_branch}\""` | — |
| [SRC-84F7DE82AF-L000086](../../.github/workflows/update_index.yml#L86) | 86 | `"            gh pr create \\"` | — |
| [SRC-84F7DE82AF-L000087](../../.github/workflows/update_index.yml#L87) | 87 | `"              --base main \\"` | — |
| [SRC-84F7DE82AF-L000088](../../.github/workflows/update_index.yml#L88) | 88 | `"              --head \"${automation_branch}\" \\"` | — |
| [SRC-84F7DE82AF-L000089](../../.github/workflows/update_index.yml#L89) | 89 | `"              --title \"docs(index): refresh repository source-line inventory\" \\"` | — |
| [SRC-84F7DE82AF-L000090](../../.github/workflows/update_index.yml#L90) | 90 | `"              --body \"Automated refresh of docs/MASTER_INDEX.md, docs/SOURCE_LINES_INDEX.md, and paginated files under docs/source_index/. Includes the repository inventory, named symbol index, explicit review-marker register, and all eligible readable source lines. Opened because direct publication to main was rejected. No force update or auto-merge was performed.\""` | — |
| [SRC-84F7DE82AF-L000091](../../.github/workflows/update_index.yml#L91) | 91 | `"            exit 0"` | — |
| [SRC-84F7DE82AF-L000092](../../.github/workflows/update_index.yml#L92) | 92 | `"          fi"` | — |
| [SRC-84F7DE82AF-L000093](../../.github/workflows/update_index.yml#L93) | 93 | `""` | — |
| [SRC-84F7DE82AF-L000094](../../.github/workflows/update_index.yml#L94) | 94 | `"          pr_number=\"$(gh pr list --state open --base main --head \"${automation_branch}\" --json number --jq '.[0].number // empty')\""` | — |
| [SRC-84F7DE82AF-L000095](../../.github/workflows/update_index.yml#L95) | 95 | `"          if [ -z \"${pr_number}\" ]; then"` | — |
| [SRC-84F7DE82AF-L000096](../../.github/workflows/update_index.yml#L96) | 96 | `"            gh pr create \\"` | — |
| [SRC-84F7DE82AF-L000097](../../.github/workflows/update_index.yml#L97) | 97 | `"              --base main \\"` | — |
| [SRC-84F7DE82AF-L000098](../../.github/workflows/update_index.yml#L98) | 98 | `"              --head \"${automation_branch}\" \\"` | — |
| [SRC-84F7DE82AF-L000099](../../.github/workflows/update_index.yml#L99) | 99 | `"              --title \"docs(index): refresh repository source-line inventory\" \\"` | — |
| [SRC-84F7DE82AF-L000100](../../.github/workflows/update_index.yml#L100) | 100 | `"              --body \"Automated refresh of docs/MASTER_INDEX.md, docs/SOURCE_LINES_INDEX.md, and paginated files under docs/source_index/. Includes the repository inventory, named symbol index, explicit review-marker register, and all eligible readable source lines. Opened because direct publication to main was rejected. No force update or auto-merge was performed.\""` | — |
| [SRC-84F7DE82AF-L000101](../../.github/workflows/update_index.yml#L101) | 101 | `"          else"` | — |
| [SRC-84F7DE82AF-L000102](../../.github/workflows/update_index.yml#L102) | 102 | `"            gh pr edit \"${pr_number}\" \\"` | — |
| [SRC-84F7DE82AF-L000103](../../.github/workflows/update_index.yml#L103) | 103 | `"              --title \"docs(index): refresh repository source-line inventory\" \\"` | — |
| [SRC-84F7DE82AF-L000104](../../.github/workflows/update_index.yml#L104) | 104 | `"              --body \"Automated refresh of docs/MASTER_INDEX.md, docs/SOURCE_LINES_INDEX.md, and paginated files under docs/source_index/. Includes the repository inventory, named symbol index, explicit review-marker register, and all eligible readable source lines. Updated because direct publication to main was rejected. No auto-merge was performed.\""` | — |
| [SRC-84F7DE82AF-L000105](../../.github/workflows/update_index.yml#L105) | 105 | `"          fi"` | — |
## إعدادات وتشغيل

### FILE-BC37D034BA — [.gitignore](../../.gitignore#L1)

- النوع: **بدون امتداد**
- نطاق الفهرسة: جرد ملف نصي فقط

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-BC37D034BA-L000001](../../.gitignore#L1) | 1 | `"__pycache__/"` | — |
| [SRC-BC37D034BA-L000002](../../.gitignore#L2) | 2 | `"*.py[cod]"` | — |
| [SRC-BC37D034BA-L000003](../../.gitignore#L3) | 3 | `".pytest_cache/"` | — |
| [SRC-BC37D034BA-L000004](../../.gitignore#L4) | 4 | `".ruff_cache/"` | — |
| [SRC-BC37D034BA-L000005](../../.gitignore#L5) | 5 | `".venv/"` | — |
| [SRC-BC37D034BA-L000006](../../.gitignore#L6) | 6 | `"venv/"` | — |
| [SRC-BC37D034BA-L000007](../../.gitignore#L7) | 7 | `".env"` | — |
| [SRC-BC37D034BA-L000008](../../.gitignore#L8) | 8 | `"*.sqlite3"` | — |
| [SRC-BC37D034BA-L000009](../../.gitignore#L9) | 9 | `"*.sqlite3-shm"` | — |
| [SRC-BC37D034BA-L000010](../../.gitignore#L10) | 10 | `"*.sqlite3-wal"` | — |
| [SRC-BC37D034BA-L000011](../../.gitignore#L11) | 11 | `".DS_Store"` | — |
| [SRC-BC37D034BA-L000012](../../.gitignore#L12) | 12 | `""` | — |
| [SRC-BC37D034BA-L000013](../../.gitignore#L13) | 13 | `"# Local backups"` | — |
| [SRC-BC37D034BA-L000014](../../.gitignore#L14) | 14 | `"*.bak"` | — |
| [SRC-BC37D034BA-L000015](../../.gitignore#L15) | 15 | `"*.bak2"` | — |
| [SRC-BC37D034BA-L000016](../../.gitignore#L16) | 16 | `"patch_*.py"` | — |
## وثائق ونصوص

### FILE-A54FF182C7 — [AGENTS.md](../../AGENTS.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-A54FF182C7-L000001](../../AGENTS.md#L1) | 1 | `"# Omarai — Mandatory Agent and Contributor Instructions"` | — |
| [SRC-A54FF182C7-L000002](../../AGENTS.md#L2) | 2 | `""` | — |
| [SRC-A54FF182C7-L000003](../../AGENTS.md#L3) | 3 | `"These rules apply to every AI agent, human contributor, code change, test report, and deployment task in this repository."` | — |
| [SRC-A54FF182C7-L000004](../../AGENTS.md#L4) | 4 | `""` | — |
| [SRC-A54FF182C7-L000005](../../AGENTS.md#L5) | 5 | `"## Source of truth"` | — |
| [SRC-A54FF182C7-L000006](../../AGENTS.md#L6) | 6 | ``"- Read `docs/OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md` before architecture, security, performance, data-flow, search, model, tool-execution, concurrency, or deployment changes."`` | — |
| [SRC-A54FF182C7-L000007](../../AGENTS.md#L7) | 7 | ``"- Read `docs/OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md` before adding or changing tools, capabilities, skills, workflows, TaskSpec, agent profiles, agents, Meta-Agent, memory scope, or generated-code execution. Treat it as a supplementary architecture contract; do not replace the charter or assert its proposed controls are implemented without evidence."`` | — |
| [SRC-A54FF182C7-L000008](../../AGENTS.md#L8) | 8 | ``"- Read `docs/OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md` for broad platform requirements and release reviews involving reliability/SRE, capacity, API/security, privacy/data governance, CI/CD/supply chain, recovery, accessibility, search quality, AI/agent evaluation, cost, and operational governance. Apply only the controls relevant to the change, but explicitly record material gaps and risks."`` | — |
| [SRC-A54FF182C7-L000009](../../AGENTS.md#L9) | 9 | ``"- Use `docs/OMARAI_REQUIREMENTS_TRACEABILITY_AND_MATURITY_MODEL_AR.md` to classify important requirements, identify relevant expert-review lenses, record evidence and limitations, prioritize risks, and apply the change/release gates. Do not mark a requirement VERIFIED without implementation and reproducible evidence."`` | — |
| [SRC-A54FF182C7-L000010](../../AGENTS.md#L10) | 10 | ``"- Keep `docs/OMARAI_REQUIREMENTS_REGISTER.md` synchronized with material changes: record new findings and update the related requirement status only when supporting evidence exists. Until the code and relevant tests have been examined, use UNKNOWN; state unrun checks as NOT_RUN."`` | — |
| [SRC-A54FF182C7-L000011](../../AGENTS.md#L11) | 11 | `"- The charter is a design requirement, not evidence that controls already exist. Inspect the actual code and tests before describing implementation status."` | — |
| [SRC-A54FF182C7-L000012](../../AGENTS.md#L12) | 12 | ``"- Treat `README.md` as a description of the current documented behavior, but verify claims against code and runtime evidence when the task requires it."`` | — |
| [SRC-A54FF182C7-L000013](../../AGENTS.md#L13) | 13 | `""` | — |
| [SRC-A54FF182C7-L000014](../../AGENTS.md#L14) | 14 | `"## Evidence discipline"` | — |
| [SRC-A54FF182C7-L000015](../../AGENTS.md#L15) | 15 | `"- Label consequential findings **VERIFIED**, **INFERRED**, **PROPOSED**, or **UNKNOWN**."` | — |
| [SRC-A54FF182C7-L000016](../../AGENTS.md#L16) | 16 | `"- Never invent files, functions, branches, commits, workflows, test results, tool capabilities, deployment status, capacity numbers, or security guarantees."` | — |
| [SRC-A54FF182C7-L000017](../../AGENTS.md#L17) | 17 | `"- A configured API key is not proof that a connector works. A health/configuration response is not proof that a provider is reachable. A model's self-review is not independent verification."` | — |
| [SRC-A54FF182C7-L000018](../../AGENTS.md#L18) | 18 | `"- When reporting a test, include the exact command, actual result, relevant commit or code state, and any environment limitation. Never say a test was run when it was not."` | — |
| [SRC-A54FF182C7-L000019](../../AGENTS.md#L19) | 19 | `"- Prefer regression tests for fixed defects and measurable evidence for performance, capacity, quality, and security claims."` | — |
| [SRC-A54FF182C7-L000020](../../AGENTS.md#L20) | 20 | `""` | — |
| [SRC-A54FF182C7-L000021](../../AGENTS.md#L21) | 21 | `"## Architecture evolution and scalability"` | — |
| [SRC-A54FF182C7-L000022](../../AGENTS.md#L22) | 22 | `"- Treat scalability, maintainability, and controlled evolution as foundational requirements; read the relevant charter sections before introducing modules, agents, tools, providers, persistence, queues, or services."` | — |
| [SRC-A54FF182C7-L000023](../../AGENTS.md#L23) | 23 | `"- Prefer a well-bounded modular monolith until measured scaling, fault-isolation, security, or release-independence needs justify a separate service. Do not add microservices or abstraction layers for appearance."` | — |
| [SRC-A54FF182C7-L000024](../../AGENTS.md#L24) | 24 | `"- New modules must have explicit responsibilities, public contracts, ownership, dependency direction, and appropriate tests. Avoid circular imports and cross-module access to private implementation details."` | — |
| [SRC-A54FF182C7-L000025](../../AGENTS.md#L25) | 25 | `"- Wrap external providers behind adapters and validate their input/output contracts. Keep provider-specific SDKs and response shapes out of domain logic."` | — |
| [SRC-A54FF182C7-L000026](../../AGENTS.md#L26) | 26 | `"- New tools/agents/plugins must declare schema, permissions, data classification, timeout, resource budget, concurrency limit, retry/idempotency behavior where applicable, health-check semantics, failure modes, and disable/rollback path."` | — |
| [SRC-A54FF182C7-L000027](../../AGENTS.md#L27) | 27 | `"- Treat API and event schema changes as versioned contracts. Prefer backward-compatible evolution; document deprecations and provide migration paths for breaking changes."` | — |
| [SRC-A54FF182C7-L000028](../../AGENTS.md#L28) | 28 | `"- All persistent data-shape changes need a tested migration and data-preservation/rollback strategy proportionate to risk. Never assume production data can be recreated from scratch."` | — |
| [SRC-A54FF182C7-L000029](../../AGENTS.md#L29) | 29 | `"- Do not rely on in-process global mutable state for cross-request user, tenant, or long-running task state. Assess what must survive process restarts before adding multi-process or horizontal scaling."` | — |
| [SRC-A54FF182C7-L000030](../../AGENTS.md#L30) | 30 | `"- Before extracting services, adding queues, changing storage, or introducing a distributed system, state the evidence-based need, operational costs, failure modes, security boundary, and acceptance tests."` | — |
| [SRC-A54FF182C7-L000031](../../AGENTS.md#L31) | 31 | `"- Add architecture fitness checks where practical for dependency boundaries, contracts, migrations, secrets, concurrency isolation, and critical performance limits."` | — |
| [SRC-A54FF182C7-L000032](../../AGENTS.md#L32) | 32 | `"- Record material architectural choices and exceptions in an ADR or equivalent, including rejected alternatives, tests, risks, compatibility, and rollback."` | — |
| [SRC-A54FF182C7-L000033](../../AGENTS.md#L33) | 33 | `"- Keep expansion incremental and reversible; do not represent future architecture goals as current capabilities."` | — |
| [SRC-A54FF182C7-L000034](../../AGENTS.md#L34) | 34 | `""` | — |
| [SRC-A54FF182C7-L000035](../../AGENTS.md#L35) | 35 | `"## Required engineering behavior"` | — |
| [SRC-A54FF182C7-L000036](../../AGENTS.md#L36) | 36 | `"- Prefer the smallest safe change that solves the verified problem. Do not rewrite the architecture without a documented reason and migration path."` | — |
| [SRC-A54FF182C7-L000037](../../AGENTS.md#L37) | 37 | `"- Preserve existing behavior unless the task explicitly authorizes a change; identify compatibility risks."` | — |
| [SRC-A54FF182C7-L000038](../../AGENTS.md#L38) | 38 | `"- Bound external calls, retries, payload sizes, number of search results/pages, planning steps, model calls, elapsed time, and concurrency where applicable."` | — |
| [SRC-A54FF182C7-L000039](../../AGENTS.md#L39) | 39 | `"- Treat model output, search results, fetched pages, user files, and external tool outputs as untrusted data. Validate schemas and permissions at deterministic execution boundaries."` | — |
| [SRC-A54FF182C7-L000040](../../AGENTS.md#L40) | 40 | `"- Do not expose secrets, private user data, internal traces, or sensitive prompts in logs, HTTP errors, front-end assets, commits, or reports."` | — |
| [SRC-A54FF182C7-L000041](../../AGENTS.md#L41) | 41 | `"- Do not weaken authentication, authorization, SSRF protections, tenant/session isolation, resource limits, or test coverage to improve speed."` | — |
| [SRC-A54FF182C7-L000042](../../AGENTS.md#L42) | 42 | `"- Do not give a model unrestricted shell, filesystem, network, or database access. Tools must be explicitly registered, scoped, bounded, and verified."` | — |
| [SRC-A54FF182C7-L000043](../../AGENTS.md#L43) | 43 | `"- For any change affecting security, external networking, persistence, concurrency, or tool execution, add or identify appropriate negative/failure tests, not only happy-path checks."` | — |
| [SRC-A54FF182C7-L000044](../../AGENTS.md#L44) | 44 | `"- For changes that cross a trust boundary, update or reference the threat model, validate deny-by-default authorization at execution time, and document negative tests for the relevant attack paths (e.g., prompt injection, SSRF/redirects, cross-user access, XSS, secret leakage, resource exhaustion, or supply-chain exposure). Disable or narrow a capability when required security controls cannot be demonstrated in its target environment."` | — |
| [SRC-A54FF182C7-L000045](../../AGENTS.md#L45) | 45 | `"- For performance or scalability work, establish a baseline and test in a named environment. Never claim support for an arbitrary user count without a reproducible load-test result."` | — |
| [SRC-A54FF182C7-L000046](../../AGENTS.md#L46) | 46 | `"- If evidence is insufficient, state the unknown and the smallest safe method to verify it."` | — |
| [SRC-A54FF182C7-L000047](../../AGENTS.md#L47) | 47 | `""` | — |
| [SRC-A54FF182C7-L000048](../../AGENTS.md#L48) | 48 | `"## Change and release control"` | — |
| [SRC-A54FF182C7-L000049](../../AGENTS.md#L49) | 49 | `"- Inspect the current branch, HEAD, working diff, and relevant files before editing."` | — |
| [SRC-A54FF182C7-L000050](../../AGENTS.md#L50) | 50 | `"- Work on a dedicated branch; keep changes scoped and reviewable."` | — |
| [SRC-A54FF182C7-L000051](../../AGENTS.md#L51) | 51 | `"- Run applicable checks when tools and environment permit, and report any checks that could not be run."` | — |
| [SRC-A54FF182C7-L000052](../../AGENTS.md#L52) | 52 | `"- Review the final diff and verify documentation links and new-file paths."` | — |
| [SRC-A54FF182C7-L000053](../../AGENTS.md#L53) | 53 | `"- Never merge a pull request, force-update a protected branch, or deploy to production without explicit authorization from the Human Director."` | — |
| [SRC-A54FF182C7-L000054](../../AGENTS.md#L54) | 54 | ``"- Do not present a proposed or unmerged change as already effective on `main`."`` | — |
| [SRC-A54FF182C7-L000055](../../AGENTS.md#L55) | 55 | `"- Update the charter or related documentation when a material design decision changes; document major architectural choices and exceptions with rationale, risks, tests, and rollback considerations."` | — |
| [SRC-A54FF182C7-L000056](../../AGENTS.md#L56) | 56 | `""` | — |
| [SRC-A54FF182C7-L000057](../../AGENTS.md#L57) | 57 | `"## Platform-grade readiness"` | — |
| [SRC-A54FF182C7-L000058](../../AGENTS.md#L58) | 58 | `"- For material production-facing changes, assess the applicable release gates in both the charter and the Global Platform Engineering Baseline; do not treat a checklist as proof of compliance."` | — |
| [SRC-A54FF182C7-L000059](../../AGENTS.md#L59) | 59 | `"- Define measurable SLI/SLO or a baseline where useful. Never invent uptime, latency, capacity, security maturity, cost, or recovery guarantees."` | — |
| [SRC-A54FF182C7-L000060](../../AGENTS.md#L60) | 60 | `"- Review blast radius, dependency failure, graceful degradation, quotas, per-request budgets, data lifecycle, tenant isolation when multi-user, supply-chain exposure, observability/privacy, and recovery proportional to risk."` | — |
| [SRC-A54FF182C7-L000061](../../AGENTS.md#L61) | 61 | `"- For AI/agent changes, test Arabic task quality, citation support, prompt injection, untrusted tool/page content, unauthorized actions, loops, provider failures, cost bounds, and safe fallback as applicable."` | — |
| [SRC-A54FF182C7-L000062](../../AGENTS.md#L62) | 62 | `"- Require an explicit reason before adding distributed infrastructure; document simpler alternatives and lifecycle costs. Do not apply every enterprise control blindly to a small deployment, but do not conceal a risk merely because a control is expensive or not yet supported."` | — |
| [SRC-A54FF182C7-L000063](../../AGENTS.md#L63) | 63 | `""` | — |
| [SRC-A54FF182C7-L000064](../../AGENTS.md#L64) | 64 | `"## Requirement traceability and expert review"` | — |
| [SRC-A54FF182C7-L000065](../../AGENTS.md#L65) | 65 | `"- For material changes, create or update stable requirement IDs and record applicability, status, evidence, test command/results, environment, limitations, residual risk, and owner in the requirements register or an equivalent reviewed record."` | — |
| [SRC-A54FF182C7-L000066](../../AGENTS.md#L66) | 66 | `"- Use all relevant discipline lenses (architecture, security, privacy, data, SRE, performance, AI evaluation, search/evidence, accessibility, supply chain, cost, and operations); do not claim that a human specialist independently reviewed work unless that actually happened."` | — |
| [SRC-A54FF182C7-L000067](../../AGENTS.md#L67) | 67 | `"- Keep non-applicable and waived requirements distinct from unknown ones. Exceptions to MUST controls need scope, compensating controls, an approver, a revisit/expiry condition, and recorded residual risk."` | — |
| [SRC-A54FF182C7-L000068](../../AGENTS.md#L68) | 68 | `"- Do not build advanced infrastructure to satisfy a checklist by appearance. Use trigger conditions and evidence in the baseline to decide when advanced requirements apply."` | — |
| [SRC-A54FF182C7-L000069](../../AGENTS.md#L69) | 69 | `""` | — |
| [SRC-A54FF182C7-L000070](../../AGENTS.md#L70) | 70 | `"## Acceptance principle"` | — |
| [SRC-A54FF182C7-L000071](../../AGENTS.md#L71) | 71 | `"A capability is not complete because it appears in a plan, comment, prompt, or documentation. It is complete only to the extent supported by the implementation, relevant tests, observed output, and explicitly stated limitations."` | — |
## الوكيل والمنطق

### FILE-E120A62E2E — [agents/__init__.py](../../agents/__init__.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-E120A62E2E-L000001](../../agents/__init__.py#L1) | 1 | `"\"\"\"Omarai lead-intent agent package.\"\"\""` | — |
## الوكيل والمنطق

### FILE-138992B1FC — [agents/answer_validation.py](../../agents/answer_validation.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-138992B1FC-L000001](../../agents/answer_validation.py#L1) | 1 | `"\"\"\"Conservative, deterministic screening for answer evidence and task coverage."` | — |
| [SRC-138992B1FC-L000002](../../agents/answer_validation.py#L2) | 2 | `""` | — |
| [SRC-138992B1FC-L000003](../../agents/answer_validation.py#L3) | 3 | `"These checks are lexical guardrails. They cannot establish that a statement is true,"` | — |
| [SRC-138992B1FC-L000004](../../agents/answer_validation.py#L4) | 4 | `"that a citation entails a claim, or that a task was semantically completed."` | — |
| [SRC-138992B1FC-L000005](../../agents/answer_validation.py#L5) | 5 | `"\"\"\""` | — |
| [SRC-138992B1FC-L000006](../../agents/answer_validation.py#L6) | 6 | `"from __future__ import annotations"` | — |
| [SRC-138992B1FC-L000007](../../agents/answer_validation.py#L7) | 7 | `""` | — |
| [SRC-138992B1FC-L000008](../../agents/answer_validation.py#L8) | 8 | `"import re"` | — |
| [SRC-138992B1FC-L000009](../../agents/answer_validation.py#L9) | 9 | `"import unicodedata"` | — |
| [SRC-138992B1FC-L000010](../../agents/answer_validation.py#L10) | 10 | `"from typing import Any"` | — |
| [SRC-138992B1FC-L000011](../../agents/answer_validation.py#L11) | 11 | `""` | — |
| [SRC-138992B1FC-L000012](../../agents/answer_validation.py#L12) | 12 | `"_DIGITS = str.maketrans(\"٠١٢٣٤٥٦٧٨٩۰۱۲۳۴۵۶۷۸۹\", \"01234567890123456789\")"` | — |
| [SRC-138992B1FC-L000013](../../agents/answer_validation.py#L13) | 13 | `"_ARABIC_NORMALIZATION = str.maketrans({"` | — |
| [SRC-138992B1FC-L000014](../../agents/answer_validation.py#L14) | 14 | `"    \"أ\": \"ا\", \"إ\": \"ا\", \"آ\": \"ا\", \"ٱ\": \"ا\", \"ى\": \"ي\","` | — |
| [SRC-138992B1FC-L000015](../../agents/answer_validation.py#L15) | 15 | `"    \"ؤ\": \"و\", \"ئ\": \"ي\", \"ة\": \"ه\", \"ـ\": \"\","` | — |
| [SRC-138992B1FC-L000016](../../agents/answer_validation.py#L16) | 16 | `"})"` | — |
| [SRC-138992B1FC-L000017](../../agents/answer_validation.py#L17) | 17 | `"_DIACRITICS = re.compile(r\"[\\u0610-\\u061A\\u064B-\\u065F\\u0670\\u06D6-\\u06ED]\")"` | — |
| [SRC-138992B1FC-L000018](../../agents/answer_validation.py#L18) | 18 | `"_TOKEN = re.compile(r\"[a-z0-9]+\|[\\u0621-\\u064A\\u0660-\\u0669]+\", re.IGNORECASE)"` | — |
| [SRC-138992B1FC-L000019](../../agents/answer_validation.py#L19) | 19 | `"_NUMBER = re.compile(r\"(?<![\\w])\\d+(?:[.,٬٫]\\d+)*(?![\\w])\")"` | — |
| [SRC-138992B1FC-L000020](../../agents/answer_validation.py#L20) | 20 | `"_CITATION = re.compile(r\"\\[(?:المصدر\|source)\\s+(\\d+)\\]\", re.IGNORECASE)"` | — |
| [SRC-138992B1FC-L000021](../../agents/answer_validation.py#L21) | 21 | `"_STOPWORDS = {"` | — |
| [SRC-138992B1FC-L000022](../../agents/answer_validation.py#L22) | 22 | `"    \"من\", \"في\", \"على\", \"عن\", \"الى\", \"و\", \"او\", \"هل\", \"ما\", \"ماذا\", \"كيف\","` | — |
| [SRC-138992B1FC-L000023](../../agents/answer_validation.py#L23) | 23 | `"    \"مع\", \"بين\", \"هذا\", \"هذه\", \"ذلك\", \"تلك\", \"الذي\", \"التي\", \"هو\", \"هي\","` | — |
| [SRC-138992B1FC-L000024](../../agents/answer_validation.py#L24) | 24 | `"    \"the\", \"a\", \"an\", \"and\", \"or\", \"in\", \"on\", \"of\", \"to\", \"for\", \"with\","` | — |
| [SRC-138992B1FC-L000025](../../agents/answer_validation.py#L25) | 25 | `"    \"from\", \"is\", \"are\", \"what\", \"which\", \"who\", \"how\", \"why\", \"when\","` | — |
| [SRC-138992B1FC-L000026](../../agents/answer_validation.py#L26) | 26 | `"    \"where\", \"compare\", \"comparison\", \"based\", \"terms\", \"respect\","` | — |
| [SRC-138992B1FC-L000027](../../agents/answer_validation.py#L27) | 27 | `"}"` | — |
| [SRC-138992B1FC-L000028](../../agents/answer_validation.py#L28) | 28 | `"_UNIT_OR_VALUE_CONTEXT = re.compile("` | — |
| [SRC-138992B1FC-L000029](../../agents/answer_validation.py#L29) | 29 | `"    r\"(?:جنيه\|ج\\.م\|دولار\|ريال\|يورو\|درهم\|egp\|usd\|eur\|\\$\|€\|£\|%\|٪\|\""` | — |
| [SRC-138992B1FC-L000030](../../agents/answer_validation.py#L30) | 30 | `"    r\"متر\|مربع\|كيلومتر\|كلم\|كم\|كيلو\|كجم\|kg\|km\|gb\|mb\|tb\|\""` | — |
| [SRC-138992B1FC-L000031](../../agents/answer_validation.py#L31) | 31 | `"    r\"سنة\|سنوات\|عام\|أعوام\|شهر\|أشهر\|يوم\|أيام\|ساعة\|ساعات\|دقيقة\|دقائق\|\""` | — |
| [SRC-138992B1FC-L000032](../../agents/answer_validation.py#L32) | 32 | `"    r\"مليون\|مليار\|ألف\|الف\|فدان\|درجة\|شخص\|أشخاص)\","` | — |
| [SRC-138992B1FC-L000033](../../agents/answer_validation.py#L33) | 33 | `"    re.IGNORECASE,"` | — |
| [SRC-138992B1FC-L000034](../../agents/answer_validation.py#L34) | 34 | `")"` | — |
| [SRC-138992B1FC-L000035](../../agents/answer_validation.py#L35) | 35 | `""` | — |
| [SRC-138992B1FC-L000036](../../agents/answer_validation.py#L36) | 36 | `""` | — |
| [SRC-138992B1FC-L000037](../../agents/answer_validation.py#L37) | 37 | `"def _normalize(value: Any) -> str:"` | — |
| [SRC-138992B1FC-L000038](../../agents/answer_validation.py#L38) | 38 | `"    text = unicodedata.normalize(\"NFKC\", str(value or \"\")).casefold().translate(_DIGITS)"` | — |
| [SRC-138992B1FC-L000039](../../agents/answer_validation.py#L39) | 39 | `"    text = _DIACRITICS.sub(\"\", text).translate(_ARABIC_NORMALIZATION)"` | — |
| [SRC-138992B1FC-L000040](../../agents/answer_validation.py#L40) | 40 | `"    return text"` | — |
| [SRC-138992B1FC-L000041](../../agents/answer_validation.py#L41) | 41 | `""` | — |
| [SRC-138992B1FC-L000042](../../agents/answer_validation.py#L42) | 42 | `""` | — |
| [SRC-138992B1FC-L000043](../../agents/answer_validation.py#L43) | 43 | `"def _tokens(value: Any, *, drop_stopwords: bool = False) -> list[str]:"` | — |
| [SRC-138992B1FC-L000044](../../agents/answer_validation.py#L44) | 44 | `"    tokens = _TOKEN.findall(_normalize(value))"` | — |
| [SRC-138992B1FC-L000045](../../agents/answer_validation.py#L45) | 45 | `"    if drop_stopwords:"` | — |
| [SRC-138992B1FC-L000046](../../agents/answer_validation.py#L46) | 46 | `"        tokens = [token for token in tokens if token not in _STOPWORDS]"` | — |
| [SRC-138992B1FC-L000047](../../agents/answer_validation.py#L47) | 47 | `"    return tokens"` | — |
| [SRC-138992B1FC-L000048](../../agents/answer_validation.py#L48) | 48 | `""` | — |
| [SRC-138992B1FC-L000049](../../agents/answer_validation.py#L49) | 49 | `""` | — |
| [SRC-138992B1FC-L000050](../../agents/answer_validation.py#L50) | 50 | `"def _numeric_literals(value: Any, *, question: str = \"\") -> set[str]:"` | — |
| [SRC-138992B1FC-L000051](../../agents/answer_validation.py#L51) | 51 | `"    \"\"\"Extract explicit numeric literals, ignoring citation indices and unqualified single digits.\"\"\""` | — |
| [SRC-138992B1FC-L000052](../../agents/answer_validation.py#L52) | 52 | `"    text = _normalize(_CITATION.sub(\" \", str(value or \"\")))"` | — |
| [SRC-138992B1FC-L000053](../../agents/answer_validation.py#L53) | 53 | `"    question_literals = {"` | — |
| [SRC-138992B1FC-L000054](../../agents/answer_validation.py#L54) | 54 | `"        _canonical_number(match.group(0))"` | — |
| [SRC-138992B1FC-L000055](../../agents/answer_validation.py#L55) | 55 | `"        for match in _NUMBER.finditer(_normalize(question))"` | — |
| [SRC-138992B1FC-L000056](../../agents/answer_validation.py#L56) | 56 | `"    }"` | — |
| [SRC-138992B1FC-L000057](../../agents/answer_validation.py#L57) | 57 | `"    result: set[str] = set()"` | — |
| [SRC-138992B1FC-L000058](../../agents/answer_validation.py#L58) | 58 | `"    for match in _NUMBER.finditer(text):"` | — |
| [SRC-138992B1FC-L000059](../../agents/answer_validation.py#L59) | 59 | `"        raw = match.group(0)"` | — |
| [SRC-138992B1FC-L000060](../../agents/answer_validation.py#L60) | 60 | `"        context = text[max(0, match.start() - 24):min(len(text), match.end() + 24)]"` | — |
| [SRC-138992B1FC-L000061](../../agents/answer_validation.py#L61) | 61 | `"        canonical = _canonical_number(raw)"` | — |
| [SRC-138992B1FC-L000062](../../agents/answer_validation.py#L62) | 62 | `"        digit_count = sum(char.isdigit() for char in canonical)"` | — |
| [SRC-138992B1FC-L000063](../../agents/answer_validation.py#L63) | 63 | `"        is_year = len(canonical) == 4 and canonical.startswith((\"19\", \"20\"))"` | — |
| [SRC-138992B1FC-L000064](../../agents/answer_validation.py#L64) | 64 | `"        if digit_count < 2 and not is_year and not _UNIT_OR_VALUE_CONTEXT.search(context):"` | — |
| [SRC-138992B1FC-L000065](../../agents/answer_validation.py#L65) | 65 | `"            continue"` | — |
| [SRC-138992B1FC-L000066](../../agents/answer_validation.py#L66) | 66 | `"        if canonical and canonical not in question_literals:"` | — |
| [SRC-138992B1FC-L000067](../../agents/answer_validation.py#L67) | 67 | `"            result.add(canonical)"` | — |
| [SRC-138992B1FC-L000068](../../agents/answer_validation.py#L68) | 68 | `"    return result"` | — |
| [SRC-138992B1FC-L000069](../../agents/answer_validation.py#L69) | 69 | `""` | — |
| [SRC-138992B1FC-L000070](../../agents/answer_validation.py#L70) | 70 | `""` | — |
| [SRC-138992B1FC-L000071](../../agents/answer_validation.py#L71) | 71 | `"def _canonical_number(value: str) -> str:"` | — |
| [SRC-138992B1FC-L000072](../../agents/answer_validation.py#L72) | 72 | `"    text = _normalize(value).replace(\"٬\", \",\").replace(\"٫\", \".\")"` | — |
| [SRC-138992B1FC-L000073](../../agents/answer_validation.py#L73) | 73 | `"    # Treat conventional comma thousands separators as formatting, not a value change."` | — |
| [SRC-138992B1FC-L000074](../../agents/answer_validation.py#L74) | 74 | `"    text = re.sub(r\"(?<=\\d),(?=\\d{3}(?:\\D\|$))\", \"\", text)"` | — |
| [SRC-138992B1FC-L000075](../../agents/answer_validation.py#L75) | 75 | `"    return text.replace(\",\", \"\")"` | — |
| [SRC-138992B1FC-L000076](../../agents/answer_validation.py#L76) | 76 | `""` | — |
| [SRC-138992B1FC-L000077](../../agents/answer_validation.py#L77) | 77 | `""` | — |
| [SRC-138992B1FC-L000078](../../agents/answer_validation.py#L78) | 78 | `""` | — |
| [SRC-138992B1FC-L000079](../../agents/answer_validation.py#L79) | 79 | `"_VALUE_CUES = {"` | — |
| [SRC-138992B1FC-L000080](../../agents/answer_validation.py#L80) | 80 | `"    \"price_or_cost\": re.compile("` | — |
| [SRC-138992B1FC-L000081](../../agents/answer_validation.py#L81) | 81 | `"        r\"(?:السعر\|سعر\|تكلفه\|تكلفة\|التكاليف\|المبلغ\|الثمن\|price\|cost\|fee\|amount\|\""` | — |
| [SRC-138992B1FC-L000082](../../agents/answer_validation.py#L82) | 82 | `"        r\"جنيه\|دولار\|ريال\|يورو\|egp\|usd\|eur\|\\$\|€\|£)\","` | — |
| [SRC-138992B1FC-L000083](../../agents/answer_validation.py#L83) | 83 | `"        re.IGNORECASE,"` | — |
| [SRC-138992B1FC-L000084](../../agents/answer_validation.py#L84) | 84 | `"    ),"` | — |
| [SRC-138992B1FC-L000085](../../agents/answer_validation.py#L85) | 85 | `"    \"area_or_size\": re.compile("` | — |
| [SRC-138992B1FC-L000086](../../agents/answer_validation.py#L86) | 86 | `"        r\"(?:المساحه\|المساحة\|مساحه\|مساحة\|متر مربع\|متر\|sqm\|square\\s+met(?:er\|re)s?\|area\|size)\","` | — |
| [SRC-138992B1FC-L000087](../../agents/answer_validation.py#L87) | 87 | `"        re.IGNORECASE,"` | — |
| [SRC-138992B1FC-L000088](../../agents/answer_validation.py#L88) | 88 | `"    ),"` | — |
| [SRC-138992B1FC-L000089](../../agents/answer_validation.py#L89) | 89 | `"    \"duration\": re.compile("` | — |
| [SRC-138992B1FC-L000090](../../agents/answer_validation.py#L90) | 90 | `"        r\"(?:المده\|المدة\|الوقت\|مده\|مدة\|فتره\|فترة\|duration\|elapsed\|days?\|weeks?\|months?\|years?\|\""` | — |
| [SRC-138992B1FC-L000091](../../agents/answer_validation.py#L91) | 91 | `"        r\"يوم\|أيام\|اسبوع\|أسبوع\|شهر\|أشهر\|سنه\|سنة\|سنوات\|عام\|أعوام\|ساعة\|ساعات\|دقيقة\|دقائق)\","` | — |
| [SRC-138992B1FC-L000092](../../agents/answer_validation.py#L92) | 92 | `"        re.IGNORECASE,"` | — |
| [SRC-138992B1FC-L000093](../../agents/answer_validation.py#L93) | 93 | `"    ),"` | — |
| [SRC-138992B1FC-L000094](../../agents/answer_validation.py#L94) | 94 | `"    \"percentage_or_rate\": re.compile("` | — |
| [SRC-138992B1FC-L000095](../../agents/answer_validation.py#L95) | 95 | `"        r\"(?:النسبه\|النسبة\|نسبة\|مئويه\|مئوية\|percent(?:age)?\|rate\|٪\|%)\","` | — |
| [SRC-138992B1FC-L000096](../../agents/answer_validation.py#L96) | 96 | `"        re.IGNORECASE,"` | — |
| [SRC-138992B1FC-L000097](../../agents/answer_validation.py#L97) | 97 | `"    ),"` | — |
| [SRC-138992B1FC-L000098](../../agents/answer_validation.py#L98) | 98 | `"    \"date_or_year\": re.compile("` | — |
| [SRC-138992B1FC-L000099](../../agents/answer_validation.py#L99) | 99 | `"        r\"(?:التاريخ\|تاريخ\|الموعد\|موعد\|صدر\|نشر\|بتاريخ\|date\|published\|year\|deadline\|\""` | — |
| [SRC-138992B1FC-L000100](../../agents/answer_validation.py#L100) | 100 | `"        r\"يناير\|فبراير\|مارس\|ابريل\|أبريل\|مايو\|يونيو\|يوليو\|أغسطس\|سبتمبر\|أكتوبر\|نوفمبر\|ديسمبر)\","` | — |
| [SRC-138992B1FC-L000101](../../agents/answer_validation.py#L101) | 101 | `"        re.IGNORECASE,"` | — |
| [SRC-138992B1FC-L000102](../../agents/answer_validation.py#L102) | 102 | `"    ),"` | — |
| [SRC-138992B1FC-L000103](../../agents/answer_validation.py#L103) | 103 | `"}"` | — |
| [SRC-138992B1FC-L000104](../../agents/answer_validation.py#L104) | 104 | `""` | — |
| [SRC-138992B1FC-L000105](../../agents/answer_validation.py#L105) | 105 | `""` | — |
| [SRC-138992B1FC-L000106](../../agents/answer_validation.py#L106) | 106 | `"def _numeric_values_with_cues(value: Any) -> list[tuple[str, str]]:"` | — |
| [SRC-138992B1FC-L000107](../../agents/answer_validation.py#L107) | 107 | `"    \"\"\"Extract number/dimension pairs as review signals, not as semantic claims.\"\"\""` | — |
| [SRC-138992B1FC-L000108](../../agents/answer_validation.py#L108) | 108 | `"    text = _normalize(value)"` | — |
| [SRC-138992B1FC-L000109](../../agents/answer_validation.py#L109) | 109 | `"    found: list[tuple[str, str]] = []"` | — |
| [SRC-138992B1FC-L000110](../../agents/answer_validation.py#L110) | 110 | `"    for match in _NUMBER.finditer(text):"` | — |
| [SRC-138992B1FC-L000111](../../agents/answer_validation.py#L111) | 111 | `"        number = _canonical_number(match.group(0))"` | — |
| [SRC-138992B1FC-L000112](../../agents/answer_validation.py#L112) | 112 | `"        context = text[max(0, match.start() - 55):min(len(text), match.end() + 55)]"` | — |
| [SRC-138992B1FC-L000113](../../agents/answer_validation.py#L113) | 113 | `"        for dimension, pattern in _VALUE_CUES.items():"` | — |
| [SRC-138992B1FC-L000114](../../agents/answer_validation.py#L114) | 114 | `"            if pattern.search(context):"` | — |
| [SRC-138992B1FC-L000115](../../agents/answer_validation.py#L115) | 115 | `"                found.append((dimension, number))"` | — |
| [SRC-138992B1FC-L000116](../../agents/answer_validation.py#L116) | 116 | `"    return found"` | — |
| [SRC-138992B1FC-L000117](../../agents/answer_validation.py#L117) | 117 | `""` | — |
| [SRC-138992B1FC-L000118](../../agents/answer_validation.py#L118) | 118 | `""` | — |
| [SRC-138992B1FC-L000119](../../agents/answer_validation.py#L119) | 119 | `"def audit_answer_integrity("` | — |
| [SRC-138992B1FC-L000120](../../agents/answer_validation.py#L120) | 120 | `"    question: str,"` | — |
| [SRC-138992B1FC-L000121](../../agents/answer_validation.py#L121) | 121 | `"    answer: str,"` | — |
| [SRC-138992B1FC-L000122](../../agents/answer_validation.py#L122) | 122 | `"    sources: list[dict[str, Any]] \| None,"` | — |
| [SRC-138992B1FC-L000123](../../agents/answer_validation.py#L123) | 123 | `"    coverage_targets: list[str] \| None = None,"` | — |
| [SRC-138992B1FC-L000124](../../agents/answer_validation.py#L124) | 124 | `") -> dict[str, Any]:"` | — |
| [SRC-138992B1FC-L000125](../../agents/answer_validation.py#L125) | 125 | `"    \"\"\"Return bounded lexical checks; never label them as semantic fact verification.\"\"\""` | — |
| [SRC-138992B1FC-L000126](../../agents/answer_validation.py#L126) | 126 | `"    safe_sources = [item for item in (sources or []) if isinstance(item, dict)]"` | — |
| [SRC-138992B1FC-L000127](../../agents/answer_validation.py#L127) | 127 | `"    source_texts: list[str] = []"` | — |
| [SRC-138992B1FC-L000128](../../agents/answer_validation.py#L128) | 128 | `"    extracted_page_count = 0"` | — |
| [SRC-138992B1FC-L000129](../../agents/answer_validation.py#L129) | 129 | `"    snippet_count = 0"` | — |
| [SRC-138992B1FC-L000130](../../agents/answer_validation.py#L130) | 130 | `"    source_number_literals: set[str] = set()"` | — |
| [SRC-138992B1FC-L000131](../../agents/answer_validation.py#L131) | 131 | `"    source_text_by_index: dict[int, str] = {}"` | — |
| [SRC-138992B1FC-L000132](../../agents/answer_validation.py#L132) | 132 | `""` | — |
| [SRC-138992B1FC-L000133](../../agents/answer_validation.py#L133) | 133 | `"    for source_index, source in enumerate(safe_sources[:40], 1):"` | — |
| [SRC-138992B1FC-L000134](../../agents/answer_validation.py#L134) | 134 | `"        page_text = str(source.get(\"page_text\") or \"\")"` | — |
| [SRC-138992B1FC-L000135](../../agents/answer_validation.py#L135) | 135 | `"        snippet = str(source.get(\"snippet\") or \"\")"` | — |
| [SRC-138992B1FC-L000136](../../agents/answer_validation.py#L136) | 136 | `"        title = str(source.get(\"title\") or \"\")"` | — |
| [SRC-138992B1FC-L000137](../../agents/answer_validation.py#L137) | 137 | `"        published_at = str(source.get(\"published_at\") or \"\")"` | — |
| [SRC-138992B1FC-L000138](../../agents/answer_validation.py#L138) | 138 | `"        if page_text.strip() and bool(source.get(\"page_fetched\")):"` | — |
| [SRC-138992B1FC-L000139](../../agents/answer_validation.py#L139) | 139 | `"            extracted_page_count += 1"` | — |
| [SRC-138992B1FC-L000140](../../agents/answer_validation.py#L140) | 140 | `"        elif snippet.strip():"` | — |
| [SRC-138992B1FC-L000141](../../agents/answer_validation.py#L141) | 141 | `"            snippet_count += 1"` | — |
| [SRC-138992B1FC-L000142](../../agents/answer_validation.py#L142) | 142 | `"        source_text = \" \".join(part for part in (title, snippet, page_text, published_at) if part)"` | — |
| [SRC-138992B1FC-L000143](../../agents/answer_validation.py#L143) | 143 | `"        if source_text.strip():"` | — |
| [SRC-138992B1FC-L000144](../../agents/answer_validation.py#L144) | 144 | `"            bounded_source_text = source_text[:16000]"` | — |
| [SRC-138992B1FC-L000145](../../agents/answer_validation.py#L145) | 145 | `"            source_texts.append(bounded_source_text)"` | — |
| [SRC-138992B1FC-L000146](../../agents/answer_validation.py#L146) | 146 | `"            source_text_by_index[source_index] = bounded_source_text"` | — |
| [SRC-138992B1FC-L000147](../../agents/answer_validation.py#L147) | 147 | `"            source_number_literals.update(_numeric_literals(bounded_source_text))"` | — |
| [SRC-138992B1FC-L000148](../../agents/answer_validation.py#L148) | 148 | `""` | — |
| [SRC-138992B1FC-L000149](../../agents/answer_validation.py#L149) | 149 | `"    answer_text = str(answer or \"\")[:24000]"` | — |
| [SRC-138992B1FC-L000150](../../agents/answer_validation.py#L150) | 150 | `"    answer_number_literals = _numeric_literals(answer_text, question=question)"` | — |
| [SRC-138992B1FC-L000151](../../agents/answer_validation.py#L151) | 151 | `"    unsupported_numbers = sorted(answer_number_literals - source_number_literals)"` | — |
| [SRC-138992B1FC-L000152](../../agents/answer_validation.py#L152) | 152 | `"    answer_tokens = set(_tokens(_CITATION.sub(\" \", answer_text), drop_stopwords=True))"` | — |
| [SRC-138992B1FC-L000153](../../agents/answer_validation.py#L153) | 153 | `""` | — |
| [SRC-138992B1FC-L000154](../../agents/answer_validation.py#L154) | 154 | `"    # Align citation-bearing sentences only by lexical overlap with the exact cited"` | — |
| [SRC-138992B1FC-L000155](../../agents/answer_validation.py#L155) | 155 | `"    # source index. This is an audit hint, not an entailment or truth check."` | — |
| [SRC-138992B1FC-L000156](../../agents/answer_validation.py#L156) | 156 | `"    citable_sources = safe_sources[:12]"` | — |
| [SRC-138992B1FC-L000157](../../agents/answer_validation.py#L157) | 157 | `"    source_token_sets: list[set[str]] = []"` | — |
| [SRC-138992B1FC-L000158](../../agents/answer_validation.py#L158) | 158 | `"    source_bases: list[str] = []"` | — |
| [SRC-138992B1FC-L000159](../../agents/answer_validation.py#L159) | 159 | `"    for source in citable_sources:"` | — |
| [SRC-138992B1FC-L000160](../../agents/answer_validation.py#L160) | 160 | `"        page_text = str(source.get(\"page_text\") or \"\")"` | — |
| [SRC-138992B1FC-L000161](../../agents/answer_validation.py#L161) | 161 | `"        snippet = str(source.get(\"snippet\") or \"\")"` | — |
| [SRC-138992B1FC-L000162](../../agents/answer_validation.py#L162) | 162 | `"        title = str(source.get(\"title\") or \"\")"` | — |
| [SRC-138992B1FC-L000163](../../agents/answer_validation.py#L163) | 163 | `"        if bool(source.get(\"page_fetched\")) and page_text.strip():"` | — |
| [SRC-138992B1FC-L000164](../../agents/answer_validation.py#L164) | 164 | `"            selected_text = page_text"` | — |
| [SRC-138992B1FC-L000165](../../agents/answer_validation.py#L165) | 165 | `"            basis = \"extracted_page_text\""` | — |
| [SRC-138992B1FC-L000166](../../agents/answer_validation.py#L166) | 166 | `"        elif snippet.strip():"` | — |
| [SRC-138992B1FC-L000167](../../agents/answer_validation.py#L167) | 167 | `"            selected_text = snippet"` | — |
| [SRC-138992B1FC-L000168](../../agents/answer_validation.py#L168) | 168 | `"            basis = \"search_snippet\""` | — |
| [SRC-138992B1FC-L000169](../../agents/answer_validation.py#L169) | 169 | `"        elif title.strip():"` | — |
| [SRC-138992B1FC-L000170](../../agents/answer_validation.py#L170) | 170 | `"            selected_text = title"` | — |
| [SRC-138992B1FC-L000171](../../agents/answer_validation.py#L171) | 171 | `"            basis = \"title_only\""` | — |
| [SRC-138992B1FC-L000172](../../agents/answer_validation.py#L172) | 172 | `"        else:"` | — |
| [SRC-138992B1FC-L000173](../../agents/answer_validation.py#L173) | 173 | `"            selected_text = \"\""` | — |
| [SRC-138992B1FC-L000174](../../agents/answer_validation.py#L174) | 174 | `"            basis = \"no_readable_text\""` | — |
| [SRC-138992B1FC-L000175](../../agents/answer_validation.py#L175) | 175 | `"        source_token_sets.append(set(_tokens(selected_text, drop_stopwords=True)))"` | — |
| [SRC-138992B1FC-L000176](../../agents/answer_validation.py#L176) | 176 | `"        source_bases.append(basis)"` | — |
| [SRC-138992B1FC-L000177](../../agents/answer_validation.py#L177) | 177 | `""` | — |
| [SRC-138992B1FC-L000178](../../agents/answer_validation.py#L178) | 178 | `"    citation_alignment: list[dict[str, Any]] = []"` | — |
| [SRC-138992B1FC-L000179](../../agents/answer_validation.py#L179) | 179 | `"    sentence_parts = ["` | — |
| [SRC-138992B1FC-L000180](../../agents/answer_validation.py#L180) | 180 | `"        part.strip()"` | — |
| [SRC-138992B1FC-L000181](../../agents/answer_validation.py#L181) | 181 | `"        for part in re.split(r\"(?<=[.!?؟])\\s+\|\\n+\", answer_text)"` | — |
| [SRC-138992B1FC-L000182](../../agents/answer_validation.py#L182) | 182 | `"        if part.strip()"` | — |
| [SRC-138992B1FC-L000183](../../agents/answer_validation.py#L183) | 183 | `"    ]"` | — |
| [SRC-138992B1FC-L000184](../../agents/answer_validation.py#L184) | 184 | `"    for sentence_number, sentence in enumerate(sentence_parts[:40], 1):"` | — |
| [SRC-138992B1FC-L000185](../../agents/answer_validation.py#L185) | 185 | `"        cited_indices = ["` | — |
| [SRC-138992B1FC-L000186](../../agents/answer_validation.py#L186) | 186 | `"            int(match.group(1))"` | — |
| [SRC-138992B1FC-L000187](../../agents/answer_validation.py#L187) | 187 | `"            for match in _CITATION.finditer(sentence)"` | — |
| [SRC-138992B1FC-L000188](../../agents/answer_validation.py#L188) | 188 | `"        ]"` | — |
| [SRC-138992B1FC-L000189](../../agents/answer_validation.py#L189) | 189 | `"        if not cited_indices:"` | — |
| [SRC-138992B1FC-L000190](../../agents/answer_validation.py#L190) | 190 | `"            continue"` | — |
| [SRC-138992B1FC-L000191](../../agents/answer_validation.py#L191) | 191 | `"        claim_tokens = list(dict.fromkeys(_tokens(_CITATION.sub(\" \", sentence), drop_stopwords=True)))"` | — |
| [SRC-138992B1FC-L000192](../../agents/answer_validation.py#L192) | 192 | `"        cited_checks: list[dict[str, Any]] = []"` | — |
| [SRC-138992B1FC-L000193](../../agents/answer_validation.py#L193) | 193 | `"        for source_index in list(dict.fromkeys(cited_indices))[:8]:"` | — |
| [SRC-138992B1FC-L000194](../../agents/answer_validation.py#L194) | 194 | `"            if source_index < 1 or source_index > len(source_token_sets):"` | — |
| [SRC-138992B1FC-L000195](../../agents/answer_validation.py#L195) | 195 | `"                cited_checks.append({"` | — |
| [SRC-138992B1FC-L000196](../../agents/answer_validation.py#L196) | 196 | `"                    \"source_index\": source_index,"` | — |
| [SRC-138992B1FC-L000197](../../agents/answer_validation.py#L197) | 197 | `"                    \"status\": \"source_index_out_of_scope\","` | — |
| [SRC-138992B1FC-L000198](../../agents/answer_validation.py#L198) | 198 | `"                    \"evidence_basis\": \"unavailable\","` | — |
| [SRC-138992B1FC-L000199](../../agents/answer_validation.py#L199) | 199 | `"                    \"matched_terms\": [],"` | — |
| [SRC-138992B1FC-L000200](../../agents/answer_validation.py#L200) | 200 | `"                    \"overlap_ratio\": 0.0,"` | — |
| [SRC-138992B1FC-L000201](../../agents/answer_validation.py#L201) | 201 | `"                })"` | — |
| [SRC-138992B1FC-L000202](../../agents/answer_validation.py#L202) | 202 | `"                continue"` | — |
| [SRC-138992B1FC-L000203](../../agents/answer_validation.py#L203) | 203 | `"            available_tokens = source_token_sets[source_index - 1]"` | — |
| [SRC-138992B1FC-L000204](../../agents/answer_validation.py#L204) | 204 | `"            overlap = [token for token in claim_tokens if token in available_tokens]"` | — |
| [SRC-138992B1FC-L000205](../../agents/answer_validation.py#L205) | 205 | `"            ratio = len(overlap) / len(claim_tokens) if claim_tokens else 0.0"` | — |
| [SRC-138992B1FC-L000206](../../agents/answer_validation.py#L206) | 206 | `"            # A lexical match is only a weak proxy for relevance, not entailment."` | — |
| [SRC-138992B1FC-L000207](../../agents/answer_validation.py#L207) | 207 | `"            # Require both relative coverage and at least two content-token matches."` | — |
| [SRC-138992B1FC-L000208](../../agents/answer_validation.py#L208) | 208 | `"            enough_overlap = len(overlap) >= 2 and ratio >= 0.5"` | — |
| [SRC-138992B1FC-L000209](../../agents/answer_validation.py#L209) | 209 | `"            cited_checks.append({"` | — |
| [SRC-138992B1FC-L000210](../../agents/answer_validation.py#L210) | 210 | `"                \"source_index\": source_index,"` | — |
| [SRC-138992B1FC-L000211](../../agents/answer_validation.py#L211) | 211 | `"                \"status\": \"lexical_overlap_signal_found\" if enough_overlap else \"weak_lexical_overlap\","` | — |
| [SRC-138992B1FC-L000212](../../agents/answer_validation.py#L212) | 212 | `"                \"evidence_basis\": source_bases[source_index - 1],"` | — |
| [SRC-138992B1FC-L000213](../../agents/answer_validation.py#L213) | 213 | `"                \"matched_terms\": overlap[:8],"` | — |
| [SRC-138992B1FC-L000214](../../agents/answer_validation.py#L214) | 214 | `"                \"overlap_ratio\": round(ratio, 3),"` | — |
| [SRC-138992B1FC-L000215](../../agents/answer_validation.py#L215) | 215 | `"            })"` | — |
| [SRC-138992B1FC-L000216](../../agents/answer_validation.py#L216) | 216 | `"        sentence_status = ("` | — |
| [SRC-138992B1FC-L000217](../../agents/answer_validation.py#L217) | 217 | `"            \"lexical_overlap_signal_found\""` | — |
| [SRC-138992B1FC-L000218](../../agents/answer_validation.py#L218) | 218 | `"            if any(item[\"status\"] == \"lexical_overlap_signal_found\" for item in cited_checks)"` | — |
| [SRC-138992B1FC-L000219](../../agents/answer_validation.py#L219) | 219 | `"            else \"weak_lexical_overlap\""` | — |
| [SRC-138992B1FC-L000220](../../agents/answer_validation.py#L220) | 220 | `"        )"` | — |
| [SRC-138992B1FC-L000221](../../agents/answer_validation.py#L221) | 221 | `"        citation_alignment.append({"` | — |
| [SRC-138992B1FC-L000222](../../agents/answer_validation.py#L222) | 222 | `"            \"sentence_number\": sentence_number,"` | — |
| [SRC-138992B1FC-L000223](../../agents/answer_validation.py#L223) | 223 | `"            \"status\": sentence_status,"` | — |
| [SRC-138992B1FC-L000224](../../agents/answer_validation.py#L224) | 224 | `"            \"claim_terms_checked\": claim_tokens[:16],"` | — |
| [SRC-138992B1FC-L000225](../../agents/answer_validation.py#L225) | 225 | `"            \"citations\": cited_checks,"` | — |
| [SRC-138992B1FC-L000226](../../agents/answer_validation.py#L226) | 226 | `"        })"` | — |
| [SRC-138992B1FC-L000227](../../agents/answer_validation.py#L227) | 227 | `""` | — |
| [SRC-138992B1FC-L000228](../../agents/answer_validation.py#L228) | 228 | `""` | — |
| [SRC-138992B1FC-L000229](../../agents/answer_validation.py#L229) | 229 | `"    # Check numeric literals against the exact source indices cited in each sentence."` | — |
| [SRC-138992B1FC-L000230](../../agents/answer_validation.py#L230) | 230 | `"    # Values found in some unrelated source do not count as support for this citation."` | — |
| [SRC-138992B1FC-L000231](../../agents/answer_validation.py#L231) | 231 | `"    source_numbers_by_index = {"` | — |
| [SRC-138992B1FC-L000232](../../agents/answer_validation.py#L232) | 232 | `"        index: _numeric_literals(text)"` | — |
| [SRC-138992B1FC-L000233](../../agents/answer_validation.py#L233) | 233 | `"        for index, text in source_text_by_index.items()"` | — |
| [SRC-138992B1FC-L000234](../../agents/answer_validation.py#L234) | 234 | `"    }"` | — |
| [SRC-138992B1FC-L000235](../../agents/answer_validation.py#L235) | 235 | `"    citation_numeric_support: list[dict[str, Any]] = []"` | — |
| [SRC-138992B1FC-L000236](../../agents/answer_validation.py#L236) | 236 | `"    for sentence_number, sentence in enumerate(sentence_parts[:40], 1):"` | — |
| [SRC-138992B1FC-L000237](../../agents/answer_validation.py#L237) | 237 | `"        cited_indices = list(dict.fromkeys("` | — |
| [SRC-138992B1FC-L000238](../../agents/answer_validation.py#L238) | 238 | `"            int(match.group(1)) for match in _CITATION.finditer(sentence)"` | — |
| [SRC-138992B1FC-L000239](../../agents/answer_validation.py#L239) | 239 | `"        ))"` | — |
| [SRC-138992B1FC-L000240](../../agents/answer_validation.py#L240) | 240 | `"        if not cited_indices:"` | — |
| [SRC-138992B1FC-L000241](../../agents/answer_validation.py#L241) | 241 | `"            continue"` | — |
| [SRC-138992B1FC-L000242](../../agents/answer_validation.py#L242) | 242 | `"        claim_numbers = sorted(_numeric_literals(sentence, question=question))"` | — |
| [SRC-138992B1FC-L000243](../../agents/answer_validation.py#L243) | 243 | `"        valid_indices = [index for index in cited_indices if 1 <= index <= len(citable_sources)]"` | — |
| [SRC-138992B1FC-L000244](../../agents/answer_validation.py#L244) | 244 | `"        supported_numbers = {"` | — |
| [SRC-138992B1FC-L000245](../../agents/answer_validation.py#L245) | 245 | `"            number"` | — |
| [SRC-138992B1FC-L000246](../../agents/answer_validation.py#L246) | 246 | `"            for number in claim_numbers"` | — |
| [SRC-138992B1FC-L000247](../../agents/answer_validation.py#L247) | 247 | `"            if any(number in source_numbers_by_index.get(index, set()) for index in valid_indices)"` | — |
| [SRC-138992B1FC-L000248](../../agents/answer_validation.py#L248) | 248 | `"        }"` | — |
| [SRC-138992B1FC-L000249](../../agents/answer_validation.py#L249) | 249 | `"        unsupported_for_citation = ["` | — |
| [SRC-138992B1FC-L000250](../../agents/answer_validation.py#L250) | 250 | `"            number for number in claim_numbers if number not in supported_numbers"` | — |
| [SRC-138992B1FC-L000251](../../agents/answer_validation.py#L251) | 251 | `"        ]"` | — |
| [SRC-138992B1FC-L000252](../../agents/answer_validation.py#L252) | 252 | `"        citation_numeric_support.append({"` | — |
| [SRC-138992B1FC-L000253](../../agents/answer_validation.py#L253) | 253 | `"            \"sentence_number\": sentence_number,"` | — |
| [SRC-138992B1FC-L000254](../../agents/answer_validation.py#L254) | 254 | `"            \"cited_source_indexes\": cited_indices[:8],"` | — |
| [SRC-138992B1FC-L000255](../../agents/answer_validation.py#L255) | 255 | `"            \"claim_numeric_literals\": claim_numbers[:30],"` | — |
| [SRC-138992B1FC-L000256](../../agents/answer_validation.py#L256) | 256 | `"            \"potentially_unsupported_numeric_literals\": unsupported_for_citation[:30],"` | — |
| [SRC-138992B1FC-L000257](../../agents/answer_validation.py#L257) | 257 | `"            \"status\": ("` | — |
| [SRC-138992B1FC-L000258](../../agents/answer_validation.py#L258) | 258 | `"                \"potentially_unsupported_numeric_literals_for_cited_sources\""` | — |
| [SRC-138992B1FC-L000259](../../agents/answer_validation.py#L259) | 259 | `"                if unsupported_for_citation"` | — |
| [SRC-138992B1FC-L000260](../../agents/answer_validation.py#L260) | 260 | `"                else \"numeric_literals_seen_in_cited_source_text\""` | — |
| [SRC-138992B1FC-L000261](../../agents/answer_validation.py#L261) | 261 | `"                if claim_numbers and valid_indices"` | — |
| [SRC-138992B1FC-L000262](../../agents/answer_validation.py#L262) | 262 | `"                else \"no_numeric_literals_to_check\""` | — |
| [SRC-138992B1FC-L000263](../../agents/answer_validation.py#L263) | 263 | `"                if not claim_numbers"` | — |
| [SRC-138992B1FC-L000264](../../agents/answer_validation.py#L264) | 264 | `"                else \"not_assessable_no_readable_cited_source\""` | — |
| [SRC-138992B1FC-L000265](../../agents/answer_validation.py#L265) | 265 | `"            ),"` | — |
| [SRC-138992B1FC-L000266](../../agents/answer_validation.py#L266) | 266 | `"        })"` | — |
| [SRC-138992B1FC-L000267](../../agents/answer_validation.py#L267) | 267 | `""` | — |
| [SRC-138992B1FC-L000268](../../agents/answer_validation.py#L268) | 268 | `"    value_evidence: dict[str, list[dict[str, Any]]] = {}"` | — |
| [SRC-138992B1FC-L000269](../../agents/answer_validation.py#L269) | 269 | `"    for source_index in source_text_by_index:"` | — |
| [SRC-138992B1FC-L000270](../../agents/answer_validation.py#L270) | 270 | `"        source = safe_sources[source_index - 1]"` | — |
| [SRC-138992B1FC-L000271](../../agents/answer_validation.py#L271) | 271 | `"        page_text = str(source.get(\"page_text\") or \"\")"` | — |
| [SRC-138992B1FC-L000272](../../agents/answer_validation.py#L272) | 272 | `"        snippet = str(source.get(\"snippet\") or \"\")"` | — |
| [SRC-138992B1FC-L000273](../../agents/answer_validation.py#L273) | 273 | `"        selected_evidence = page_text if bool(source.get(\"page_fetched\")) and page_text.strip() else snippet"` | — |
| [SRC-138992B1FC-L000274](../../agents/answer_validation.py#L274) | 274 | `"        if not selected_evidence.strip():"` | — |
| [SRC-138992B1FC-L000275](../../agents/answer_validation.py#L275) | 275 | `"            selected_evidence = str(source.get(\"title\") or \"\")"` | — |
| [SRC-138992B1FC-L000276](../../agents/answer_validation.py#L276) | 276 | `"        for dimension, number in _numeric_values_with_cues(selected_evidence):"` | — |
| [SRC-138992B1FC-L000277](../../agents/answer_validation.py#L277) | 277 | `"            value_evidence.setdefault(dimension, []).append({"` | — |
| [SRC-138992B1FC-L000278](../../agents/answer_validation.py#L278) | 278 | `"                \"source_index\": source_index,"` | — |
| [SRC-138992B1FC-L000279](../../agents/answer_validation.py#L279) | 279 | `"                \"value\": number,"` | — |
| [SRC-138992B1FC-L000280](../../agents/answer_validation.py#L280) | 280 | `"            })"` | — |
| [SRC-138992B1FC-L000281](../../agents/answer_validation.py#L281) | 281 | `"    potential_value_discrepancies: list[dict[str, Any]] = []"` | — |
| [SRC-138992B1FC-L000282](../../agents/answer_validation.py#L282) | 282 | `"    for dimension, entries in sorted(value_evidence.items()):"` | — |
| [SRC-138992B1FC-L000283](../../agents/answer_validation.py#L283) | 283 | `"        unique_values = list(dict.fromkeys(entry[\"value\"] for entry in entries))"` | — |
| [SRC-138992B1FC-L000284](../../agents/answer_validation.py#L284) | 284 | `"        source_indexes = sorted({entry[\"source_index\"] for entry in entries})"` | — |
| [SRC-138992B1FC-L000285](../../agents/answer_validation.py#L285) | 285 | `"        if len(unique_values) < 2 or len(source_indexes) < 2:"` | — |
| [SRC-138992B1FC-L000286](../../agents/answer_validation.py#L286) | 286 | `"            continue"` | — |
| [SRC-138992B1FC-L000287](../../agents/answer_validation.py#L287) | 287 | `"        by_value = []"` | — |
| [SRC-138992B1FC-L000288](../../agents/answer_validation.py#L288) | 288 | `"        for value in unique_values[:8]:"` | — |
| [SRC-138992B1FC-L000289](../../agents/answer_validation.py#L289) | 289 | `"            supporting_indexes = sorted({"` | — |
| [SRC-138992B1FC-L000290](../../agents/answer_validation.py#L290) | 290 | `"                entry[\"source_index\"] for entry in entries if entry[\"value\"] == value"` | — |
| [SRC-138992B1FC-L000291](../../agents/answer_validation.py#L291) | 291 | `"            })"` | — |
| [SRC-138992B1FC-L000292](../../agents/answer_validation.py#L292) | 292 | `"            by_value.append({\"value\": value, \"source_indexes\": supporting_indexes[:8]})"` | — |
| [SRC-138992B1FC-L000293](../../agents/answer_validation.py#L293) | 293 | `"        potential_value_discrepancies.append({"` | — |
| [SRC-138992B1FC-L000294](../../agents/answer_validation.py#L294) | 294 | `"            \"dimension\": dimension,"` | — |
| [SRC-138992B1FC-L000295](../../agents/answer_validation.py#L295) | 295 | `"            \"values\": by_value,"` | — |
| [SRC-138992B1FC-L000296](../../agents/answer_validation.py#L296) | 296 | `"            \"source_indexes\": source_indexes[:12],"` | — |
| [SRC-138992B1FC-L000297](../../agents/answer_validation.py#L297) | 297 | `"            \"status\": \"potential_variation_or_conflict_requires_entity_review\","` | — |
| [SRC-138992B1FC-L000298](../../agents/answer_validation.py#L298) | 298 | `"        })"` | — |
| [SRC-138992B1FC-L000299](../../agents/answer_validation.py#L299) | 299 | `""` | — |
| [SRC-138992B1FC-L000300](../../agents/answer_validation.py#L300) | 300 | `"    weak_citation_alignment_count = sum("` | — |
| [SRC-138992B1FC-L000301](../../agents/answer_validation.py#L301) | 301 | `"        item[\"status\"] == \"weak_lexical_overlap\""` | — |
| [SRC-138992B1FC-L000302](../../agents/answer_validation.py#L302) | 302 | `"        for item in citation_alignment"` | — |
| [SRC-138992B1FC-L000303](../../agents/answer_validation.py#L303) | 303 | `"    )"` | — |
| [SRC-138992B1FC-L000304](../../agents/answer_validation.py#L304) | 304 | `"    target_checks: list[dict[str, Any]] = []"` | — |
| [SRC-138992B1FC-L000305](../../agents/answer_validation.py#L305) | 305 | `"    for target in (coverage_targets or [])[:8]:"` | — |
| [SRC-138992B1FC-L000306](../../agents/answer_validation.py#L306) | 306 | `"        target_tokens = list(dict.fromkeys(_tokens(target, drop_stopwords=True)))"` | — |
| [SRC-138992B1FC-L000307](../../agents/answer_validation.py#L307) | 307 | `"        if not target_tokens:"` | — |
| [SRC-138992B1FC-L000308](../../agents/answer_validation.py#L308) | 308 | `"            target_tokens = list(dict.fromkeys(_tokens(target)))"` | — |
| [SRC-138992B1FC-L000309](../../agents/answer_validation.py#L309) | 309 | `"        overlap = [token for token in target_tokens if token in answer_tokens]"` | — |
| [SRC-138992B1FC-L000310](../../agents/answer_validation.py#L310) | 310 | `"        ratio = len(overlap) / len(target_tokens) if target_tokens else 0.0"` | — |
| [SRC-138992B1FC-L000311](../../agents/answer_validation.py#L311) | 311 | `"        likely_covered = bool(overlap) and ("` | — |
| [SRC-138992B1FC-L000312](../../agents/answer_validation.py#L312) | 312 | `"            ratio >= 0.5 if len(target_tokens) > 1 else True"` | — |
| [SRC-138992B1FC-L000313](../../agents/answer_validation.py#L313) | 313 | `"        )"` | — |
| [SRC-138992B1FC-L000314](../../agents/answer_validation.py#L314) | 314 | `"        target_checks.append({"` | — |
| [SRC-138992B1FC-L000315](../../agents/answer_validation.py#L315) | 315 | `"            \"target\": str(target)[:120],"` | — |
| [SRC-138992B1FC-L000316](../../agents/answer_validation.py#L316) | 316 | `"            \"status\": \"lexical_signal_found\" if likely_covered else \"possibly_missing\","` | — |
| [SRC-138992B1FC-L000317](../../agents/answer_validation.py#L317) | 317 | `"            \"matched_terms\": overlap[:12],"` | — |
| [SRC-138992B1FC-L000318](../../agents/answer_validation.py#L318) | 318 | `"            \"missing_terms\": [token for token in target_tokens if token not in answer_tokens][:12],"` | — |
| [SRC-138992B1FC-L000319](../../agents/answer_validation.py#L319) | 319 | `"            \"token_overlap_ratio\": round(ratio, 3),"` | — |
| [SRC-138992B1FC-L000320](../../agents/answer_validation.py#L320) | 320 | `"        })"` | — |
| [SRC-138992B1FC-L000321](../../agents/answer_validation.py#L321) | 321 | `""` | — |
| [SRC-138992B1FC-L000322](../../agents/answer_validation.py#L322) | 322 | `"    citation_count = len(re.findall(r\"\\[(?:المصدر\|source)\\s+\\d+\\]\", answer_text, re.IGNORECASE))"` | — |
| [SRC-138992B1FC-L000323](../../agents/answer_validation.py#L323) | 323 | `"    if extracted_page_count:"` | — |
| [SRC-138992B1FC-L000324](../../agents/answer_validation.py#L324) | 324 | `"        source_scope = \"contains_extracted_page_text_and_or_snippets\""` | — |
| [SRC-138992B1FC-L000325](../../agents/answer_validation.py#L325) | 325 | `"    elif snippet_count:"` | — |
| [SRC-138992B1FC-L000326](../../agents/answer_validation.py#L326) | 326 | `"        source_scope = \"search_snippets_only\""` | — |
| [SRC-138992B1FC-L000327](../../agents/answer_validation.py#L327) | 327 | `"    else:"` | — |
| [SRC-138992B1FC-L000328](../../agents/answer_validation.py#L328) | 328 | `"        source_scope = \"no_readable_source_text\""` | — |
| [SRC-138992B1FC-L000329](../../agents/answer_validation.py#L329) | 329 | `""` | — |
| [SRC-138992B1FC-L000330](../../agents/answer_validation.py#L330) | 330 | `"    if not source_texts:"` | — |
| [SRC-138992B1FC-L000331](../../agents/answer_validation.py#L331) | 331 | `"        numeric_status = \"not_assessable_no_readable_source_text\""` | — |
| [SRC-138992B1FC-L000332](../../agents/answer_validation.py#L332) | 332 | `"    elif unsupported_numbers:"` | — |
| [SRC-138992B1FC-L000333](../../agents/answer_validation.py#L333) | 333 | `"        numeric_status = \"potentially_unsupported_numeric_literals\""` | — |
| [SRC-138992B1FC-L000334](../../agents/answer_validation.py#L334) | 334 | `"    elif answer_number_literals:"` | — |
| [SRC-138992B1FC-L000335](../../agents/answer_validation.py#L335) | 335 | `"        numeric_status = \"all_checked_numeric_literals_appear_in_source_text\""` | — |
| [SRC-138992B1FC-L000336](../../agents/answer_validation.py#L336) | 336 | `"    else:"` | — |
| [SRC-138992B1FC-L000337](../../agents/answer_validation.py#L337) | 337 | `"        numeric_status = \"no_specific_numeric_literals_checked\""` | — |
| [SRC-138992B1FC-L000338](../../agents/answer_validation.py#L338) | 338 | `""` | — |
| [SRC-138992B1FC-L000339](../../agents/answer_validation.py#L339) | 339 | `"    return {"` | — |
| [SRC-138992B1FC-L000340](../../agents/answer_validation.py#L340) | 340 | `"        \"method\": \"deterministic_lexical_screen_only\","` | — |
| [SRC-138992B1FC-L000341](../../agents/answer_validation.py#L341) | 341 | `"        \"semantic_verification\": False,"` | — |
| [SRC-138992B1FC-L000342](../../agents/answer_validation.py#L342) | 342 | `"        \"independent_fact_check\": False,"` | — |
| [SRC-138992B1FC-L000343](../../agents/answer_validation.py#L343) | 343 | `"        \"answer_nonempty\": bool(answer_text.strip()),"` | — |
| [SRC-138992B1FC-L000344](../../agents/answer_validation.py#L344) | 344 | `"        \"source_count\": len(safe_sources),"` | — |
| [SRC-138992B1FC-L000345](../../agents/answer_validation.py#L345) | 345 | `"        \"source_evidence_scope\": source_scope,"` | — |
| [SRC-138992B1FC-L000346](../../agents/answer_validation.py#L346) | 346 | `"        \"pages_with_extracted_text\": extracted_page_count,"` | — |
| [SRC-138992B1FC-L000347](../../agents/answer_validation.py#L347) | 347 | `"        \"sources_with_snippets_only\": snippet_count,"` | — |
| [SRC-138992B1FC-L000348](../../agents/answer_validation.py#L348) | 348 | `"        \"citation_marker_count\": citation_count,"` | — |
| [SRC-138992B1FC-L000349](../../agents/answer_validation.py#L349) | 349 | `"        \"citation_entailment\": \"not_checked\","` | — |
| [SRC-138992B1FC-L000350](../../agents/answer_validation.py#L350) | 350 | `"        \"citation_lexical_alignment_method\": \"content_word_overlap_heuristic_not_entailment\","` | — |
| [SRC-138992B1FC-L000351](../../agents/answer_validation.py#L351) | 351 | `"        \"citation_lexical_alignment\": citation_alignment[:30],"` | — |
| [SRC-138992B1FC-L000352](../../agents/answer_validation.py#L352) | 352 | `"        \"weak_citation_alignment_count\": weak_citation_alignment_count,"` | — |
| [SRC-138992B1FC-L000353](../../agents/answer_validation.py#L353) | 353 | `"        \"citation_numeric_support\": citation_numeric_support[:30],"` | — |
| [SRC-138992B1FC-L000354](../../agents/answer_validation.py#L354) | 354 | `"        \"potentially_unsupported_numeric_by_citation_count\": sum("` | — |
| [SRC-138992B1FC-L000355](../../agents/answer_validation.py#L355) | 355 | `"            len(item[\"potentially_unsupported_numeric_literals\"])"` | — |
| [SRC-138992B1FC-L000356](../../agents/answer_validation.py#L356) | 356 | `"            for item in citation_numeric_support"` | — |
| [SRC-138992B1FC-L000357](../../agents/answer_validation.py#L357) | 357 | `"        ),"` | — |
| [SRC-138992B1FC-L000358](../../agents/answer_validation.py#L358) | 358 | `"        \"potential_value_discrepancies\": potential_value_discrepancies[:8],"` | — |
| [SRC-138992B1FC-L000359](../../agents/answer_validation.py#L359) | 359 | `"        \"potential_value_discrepancy_count\": len(potential_value_discrepancies),"` | — |
| [SRC-138992B1FC-L000360](../../agents/answer_validation.py#L360) | 360 | `"        \"numeric_check_status\": numeric_status,"` | — |
| [SRC-138992B1FC-L000361](../../agents/answer_validation.py#L361) | 361 | `"        \"checked_numeric_literals\": sorted(answer_number_literals)[:40],"` | — |
| [SRC-138992B1FC-L000362](../../agents/answer_validation.py#L362) | 362 | `"        \"potentially_unsupported_numeric_literals\": unsupported_numbers[:40],"` | — |
| [SRC-138992B1FC-L000363](../../agents/answer_validation.py#L363) | 363 | `"        \"potentially_unsupported_numeric_count\": len(unsupported_numbers),"` | — |
| [SRC-138992B1FC-L000364](../../agents/answer_validation.py#L364) | 364 | `"        \"target_coverage\": target_checks,"` | — |
| [SRC-138992B1FC-L000365](../../agents/answer_validation.py#L365) | 365 | `"        \"potentially_missing_target_count\": sum("` | — |
| [SRC-138992B1FC-L000366](../../agents/answer_validation.py#L366) | 366 | `"            item[\"status\"] == \"possibly_missing\" for item in target_checks"` | — |
| [SRC-138992B1FC-L000367](../../agents/answer_validation.py#L367) | 367 | `"        ),"` | — |
| [SRC-138992B1FC-L000368](../../agents/answer_validation.py#L368) | 368 | `"        \"limitations\": ["` | — |
| [SRC-138992B1FC-L000369](../../agents/answer_validation.py#L369) | 369 | `"            \"Token overlap does not prove that an answer fulfills the intended task.\","` | — |
| [SRC-138992B1FC-L000370](../../agents/answer_validation.py#L370) | 370 | `"            \"A number appearing in any source does not prove that the source supports the claim.\","` | — |
| [SRC-138992B1FC-L000371](../../agents/answer_validation.py#L371) | 371 | `"            \"Citation token overlap can be coincidental and does not establish that the source entails the claim.\","` | — |
| [SRC-138992B1FC-L000372](../../agents/answer_validation.py#L372) | 372 | `"            \"Value-discrepancy flags may reflect different products, periods, or units; they are not automatic contradiction findings.\","` | — |
| [SRC-138992B1FC-L000373](../../agents/answer_validation.py#L373) | 373 | `"            \"Contradictory sources and citation-to-claim entailment require claim-level review.\","` | — |
| [SRC-138992B1FC-L000374](../../agents/answer_validation.py#L374) | 374 | `"            \"Search snippets may be partial; extracted page text is still not independent verification.\","` | — |
| [SRC-138992B1FC-L000375](../../agents/answer_validation.py#L375) | 375 | `"        ],"` | — |
| [SRC-138992B1FC-L000376](../../agents/answer_validation.py#L376) | 376 | `"    }"` | — |
## الوكيل والمنطق

### FILE-5587371288 — [agents/intent_router.py](../../agents/intent_router.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-5587371288-L000001](../../agents/intent_router.py#L1) | 1 | `"\"\"\"Small deterministic intent routing for Omarai's answer engine."` | — |
| [SRC-5587371288-L000002](../../agents/intent_router.py#L2) | 2 | `""` | — |
| [SRC-5587371288-L000003](../../agents/intent_router.py#L3) | 3 | `"This module chooses a strategy; it does not search, call a model, or claim that"` | — |
| [SRC-5587371288-L000004](../../agents/intent_router.py#L4) | 4 | `"an answer is factually verified. Keep the rules explicit and unit-testable."` | — |
| [SRC-5587371288-L000005](../../agents/intent_router.py#L5) | 5 | `"\"\"\""` | — |
| [SRC-5587371288-L000006](../../agents/intent_router.py#L6) | 6 | `"from __future__ import annotations"` | — |
| [SRC-5587371288-L000007](../../agents/intent_router.py#L7) | 7 | `""` | — |
| [SRC-5587371288-L000008](../../agents/intent_router.py#L8) | 8 | `"import re"` | — |
| [SRC-5587371288-L000009](../../agents/intent_router.py#L9) | 9 | `"import unicodedata"` | — |
| [SRC-5587371288-L000010](../../agents/intent_router.py#L10) | 10 | `"from typing import Any"` | — |
| [SRC-5587371288-L000011](../../agents/intent_router.py#L11) | 11 | `""` | — |
| [SRC-5587371288-L000012](../../agents/intent_router.py#L12) | 12 | `"MAX_CONTEXT_TURNS = 8"` | — |
| [SRC-5587371288-L000013](../../agents/intent_router.py#L13) | 13 | `""` | — |
| [SRC-5587371288-L000014](../../agents/intent_router.py#L14) | 14 | `"ROUTES = frozenset({"` | — |
| [SRC-5587371288-L000015](../../agents/intent_router.py#L15) | 15 | `"    \"LOCAL\", \"MODEL_ONLY\", \"CLARIFY\", \"WEB_SIMPLE\", \"WEB_DEEP\","` | — |
| [SRC-5587371288-L000016](../../agents/intent_router.py#L16) | 16 | `"    \"LEAD_GENERATION\","` | — |
| [SRC-5587371288-L000017](../../agents/intent_router.py#L17) | 17 | `"})"` | — |
| [SRC-5587371288-L000018](../../agents/intent_router.py#L18) | 18 | `""` | — |
| [SRC-5587371288-L000019](../../agents/intent_router.py#L19) | 19 | `"_ARABIC_DIACRITICS = re.compile(r\"[\\u0610-\\u061A\\u064B-\\u065F\\u0670\\u06D6-\\u06ED]\")"` | — |
| [SRC-5587371288-L000020](../../agents/intent_router.py#L20) | 20 | `"_PUNCTUATION = re.compile(r\"[؟?!.،,؛;:()\\[\\]{}\\\"'«»]+\")"` | — |
| [SRC-5587371288-L000021](../../agents/intent_router.py#L21) | 21 | `"_SPACE = re.compile(r\"\\s+\")"` | — |
| [SRC-5587371288-L000022](../../agents/intent_router.py#L22) | 22 | `""` | — |
| [SRC-5587371288-L000023](../../agents/intent_router.py#L23) | 23 | `"_SMALLTALK = frozenset({"` | — |
| [SRC-5587371288-L000024](../../agents/intent_router.py#L24) | 24 | `"    \"hi\", \"hello\", \"hey\", \"hello there\", \"hi there\","` | — |
| [SRC-5587371288-L000025](../../agents/intent_router.py#L25) | 25 | `"    \"thanks\", \"thank you\", \"thanks that helps\", \"thank you that helps\","` | — |
| [SRC-5587371288-L000026](../../agents/intent_router.py#L26) | 26 | `"    \"got it\", \"okay thanks\", \"ok thanks\", \"how are you\", \"how are you doing\","` | — |
| [SRC-5587371288-L000027](../../agents/intent_router.py#L27) | 27 | `"    \"hello how are you\", \"hi how are you\","` | — |
| [SRC-5587371288-L000028](../../agents/intent_router.py#L28) | 28 | `"    \"ازيك\", \"ازيك عامل ايه\", \"ازيك عامل ايه النهارده\", \"عامل ايه\", \"عامله ايه\", \"اهلا\", \"مرحبا\","` | — |
| [SRC-5587371288-L000029](../../agents/intent_router.py#L29) | 29 | `"    \"السلام عليكم\", \"السلام عليكم ورحمه الله وبركاته\","` | — |
| [SRC-5587371288-L000030](../../agents/intent_router.py#L30) | 30 | `"    \"صباح الخير\", \"مساء الخير\", \"شكرا\", \"شكرا لك\", \"متشكر\", \"متشكره\","` | — |
| [SRC-5587371288-L000031](../../agents/intent_router.py#L31) | 31 | `"    \"تمام شكرا\", \"تمام\", \"حسنا\", \"العفو\","` | — |
| [SRC-5587371288-L000032](../../agents/intent_router.py#L32) | 32 | `"})"` | — |
| [SRC-5587371288-L000033](../../agents/intent_router.py#L33) | 33 | `""` | — |
| [SRC-5587371288-L000034](../../agents/intent_router.py#L34) | 34 | `"# Elliptical questions whose subject normally must be recovered from dialogue."` | — |
| [SRC-5587371288-L000035](../../agents/intent_router.py#L35) | 35 | `"_AMBIGUOUS_ARABIC = frozenset({"` | — |
| [SRC-5587371288-L000036](../../agents/intent_router.py#L36) | 36 | `"    \"كام سعرها\", \"كم سعرها\", \"بكام سعرها\", \"سعرها كام\", \"سعرها بكام\","` | — |
| [SRC-5587371288-L000037](../../agents/intent_router.py#L37) | 37 | `"    \"كام تمنها\", \"كم تمنها\", \"بكام دي\", \"بكام ده\", \"سعره كام\", \"كام سعره\","` | — |
| [SRC-5587371288-L000038](../../agents/intent_router.py#L38) | 38 | `"    \"كم سعره\", \"قارنهم\", \"قارنهملي\", \"قارن بينهم\", \"قارن بينهما\","` | — |
| [SRC-5587371288-L000039](../../agents/intent_router.py#L39) | 39 | `"    \"ما رايك فيها\", \"ايه رايك فيها\", \"هل هي كويسه\", \"هل هو كويس\","` | — |
| [SRC-5587371288-L000040](../../agents/intent_router.py#L40) | 40 | `"    \"هل دي كويسه\", \"هل ده كويس\", \"هل هو جيد\", \"هل هي جيده\","` | — |
| [SRC-5587371288-L000041](../../agents/intent_router.py#L41) | 41 | `"    \"اشتريها ولا لا\", \"اشتريه ولا لا\","` | — |
| [SRC-5587371288-L000042](../../agents/intent_router.py#L42) | 42 | `"    \"فين\", \"فين هي\", \"فين هو\", \"فين مكانها\", \"فين مكانه\","` | — |
| [SRC-5587371288-L000043](../../agents/intent_router.py#L43) | 43 | `"    \"مكانها فين\", \"مكانه فين\", \"موجوده فين\", \"موجود فين\","` | — |
| [SRC-5587371288-L000044](../../agents/intent_router.py#L44) | 44 | `"    \"فين الاقيها\", \"فين الاقيه\","` | — |
