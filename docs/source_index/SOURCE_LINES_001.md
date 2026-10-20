# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **001**
- سجلات الأسطر: **800**
- النطاق: SRC-2F754321D6-L000001 إلى SRC-C9CF9B54F8-L000101
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
| [SRC-9F6E30987B-L000025](../../.github/workflows/hosted-smoke.yml#L25) | 25 | `"            echo \"::error::GitHub Actions secret OMARAI_ACCESS_TOKEN is missing or too short.\""` | FND-ERROR-9F6E30987B-L000025 |
| [SRC-9F6E30987B-L000026](../../.github/workflows/hosted-smoke.yml#L26) | 26 | `"            exit 1"` | — |
| [SRC-9F6E30987B-L000027](../../.github/workflows/hosted-smoke.yml#L27) | 27 | `"          fi"` | — |
| [SRC-9F6E30987B-L000028](../../.github/workflows/hosted-smoke.yml#L28) | 28 | `"          if [[ -z \"${OMARAI_BASE_URL}\" ]]; then"` | — |
| [SRC-9F6E30987B-L000029](../../.github/workflows/hosted-smoke.yml#L29) | 29 | `"            echo \"::error::GitHub Actions secret OMARAI_BASE_URL is missing.\""` | FND-ERROR-9F6E30987B-L000029 |
| [SRC-9F6E30987B-L000030](../../.github/workflows/hosted-smoke.yml#L30) | 30 | `"            exit 1"` | — |
| [SRC-9F6E30987B-L000031](../../.github/workflows/hosted-smoke.yml#L31) | 31 | `"          fi"` | — |
| [SRC-9F6E30987B-L000032](../../.github/workflows/hosted-smoke.yml#L32) | 32 | `"          if [[ \"${OMARAI_BASE_URL}\" != https://* \|\| \"${OMARAI_BASE_URL}\" == *\\?* \|\| \"${OMARAI_BASE_URL}\" == *\\#* ]]; then"` | — |
| [SRC-9F6E30987B-L000033](../../.github/workflows/hosted-smoke.yml#L33) | 33 | `"            echo \"::error::OMARAI_BASE_URL must be an HTTPS origin without a path, query, or fragment.\""` | FND-ERROR-9F6E30987B-L000033 |
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
| [SRC-9F6E30987B-L000047](../../.github/workflows/hosted-smoke.yml#L47) | 47 | `"        run: python scripts/hosted_smoke_test.py --base-url \"$OMARAI_BASE_URL\" --timeout 180"` | — |
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
| [SRC-1DB27D9318-L000024](../../.github/workflows/tests.yml#L24) | 24 | `"      - name: Verify living index generation against the full repository"` | — |
| [SRC-1DB27D9318-L000025](../../.github/workflows/tests.yml#L25) | 25 | `"        run: \|"` | — |
| [SRC-1DB27D9318-L000026](../../.github/workflows/tests.yml#L26) | 26 | `"          python docs/generate_index.py"` | — |
| [SRC-1DB27D9318-L000027](../../.github/workflows/tests.yml#L27) | 27 | `"          python docs/generate_index.py --check"` | — |
| [SRC-1DB27D9318-L000028](../../.github/workflows/tests.yml#L28) | 28 | `"      - run: python -m pytest -q"` | — |
| [SRC-1DB27D9318-L000029](../../.github/workflows/tests.yml#L29) | 29 | `""` | — |
| [SRC-1DB27D9318-L000030](../../.github/workflows/tests.yml#L30) | 30 | `"  container-build:"` | — |
| [SRC-1DB27D9318-L000031](../../.github/workflows/tests.yml#L31) | 31 | `"    runs-on: ubuntu-latest"` | — |
| [SRC-1DB27D9318-L000032](../../.github/workflows/tests.yml#L32) | 32 | `"    steps:"` | — |
| [SRC-1DB27D9318-L000033](../../.github/workflows/tests.yml#L33) | 33 | `"      - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7.0.1"` | — |
| [SRC-1DB27D9318-L000034](../../.github/workflows/tests.yml#L34) | 34 | `"      - name: Build production container"` | — |
| [SRC-1DB27D9318-L000035](../../.github/workflows/tests.yml#L35) | 35 | `"        run: docker build --tag omarai:ci ."` | — |
| [SRC-1DB27D9318-L000036](../../.github/workflows/tests.yml#L36) | 36 | `"      - name: Start container and smoke-test protected API"` | — |
| [SRC-1DB27D9318-L000037](../../.github/workflows/tests.yml#L37) | 37 | `"        shell: bash"` | — |
| [SRC-1DB27D9318-L000038](../../.github/workflows/tests.yml#L38) | 38 | `"        run: \|"` | — |
| [SRC-1DB27D9318-L000039](../../.github/workflows/tests.yml#L39) | 39 | `"          set -euo pipefail"` | — |
| [SRC-1DB27D9318-L000040](../../.github/workflows/tests.yml#L40) | 40 | `"          docker run --detach --rm --name omarai-ci \\"` | — |
| [SRC-1DB27D9318-L000041](../../.github/workflows/tests.yml#L41) | 41 | `"            --publish 127.0.0.1:18765:8000 \\"` | — |
| [SRC-1DB27D9318-L000042](../../.github/workflows/tests.yml#L42) | 42 | `"            --env OMARAI_PUBLIC_DEPLOYMENT=1 \\"` | — |
| [SRC-1DB27D9318-L000043](../../.github/workflows/tests.yml#L43) | 43 | `"            --env OMARAI_ACCESS_TOKEN=ci-only-test-token-not-for-production-123456 \\"` | — |
| [SRC-1DB27D9318-L000044](../../.github/workflows/tests.yml#L44) | 44 | `"            omarai:ci"` | — |
| [SRC-1DB27D9318-L000045](../../.github/workflows/tests.yml#L45) | 45 | `"          cleanup() { docker stop omarai-ci >/dev/null 2>&1 \|\| true; }"` | — |
| [SRC-1DB27D9318-L000046](../../.github/workflows/tests.yml#L46) | 46 | `"          trap cleanup EXIT"` | — |
| [SRC-1DB27D9318-L000047](../../.github/workflows/tests.yml#L47) | 47 | `""` | — |
| [SRC-1DB27D9318-L000048](../../.github/workflows/tests.yml#L48) | 48 | `"          healthy=false"` | — |
| [SRC-1DB27D9318-L000049](../../.github/workflows/tests.yml#L49) | 49 | `"          for _ in $(seq 1 30); do"` | — |
| [SRC-1DB27D9318-L000050](../../.github/workflows/tests.yml#L50) | 50 | `"            if curl --silent --fail http://127.0.0.1:18765/api/health \\"` | — |
| [SRC-1DB27D9318-L000051](../../.github/workflows/tests.yml#L51) | 51 | `"              --output /tmp/omarai-health.json; then"` | — |
| [SRC-1DB27D9318-L000052](../../.github/workflows/tests.yml#L52) | 52 | `"              healthy=true"` | — |
| [SRC-1DB27D9318-L000053](../../.github/workflows/tests.yml#L53) | 53 | `"              break"` | — |
| [SRC-1DB27D9318-L000054](../../.github/workflows/tests.yml#L54) | 54 | `"            fi"` | — |
| [SRC-1DB27D9318-L000055](../../.github/workflows/tests.yml#L55) | 55 | `"            sleep 1"` | — |
| [SRC-1DB27D9318-L000056](../../.github/workflows/tests.yml#L56) | 56 | `"          done"` | — |
| [SRC-1DB27D9318-L000057](../../.github/workflows/tests.yml#L57) | 57 | `"          if [[ \"$healthy\" != \"true\" ]]; then"` | — |
| [SRC-1DB27D9318-L000058](../../.github/workflows/tests.yml#L58) | 58 | `"            docker logs omarai-ci"` | — |
| [SRC-1DB27D9318-L000059](../../.github/workflows/tests.yml#L59) | 59 | `"            exit 1"` | — |
| [SRC-1DB27D9318-L000060](../../.github/workflows/tests.yml#L60) | 60 | `"          fi"` | — |
| [SRC-1DB27D9318-L000061](../../.github/workflows/tests.yml#L61) | 61 | `"          python -c 'import json; assert json.load(open(\"/tmp/omarai-health.json\", encoding=\"utf-8\"))[\"ok\"] is True'"` | — |
| [SRC-1DB27D9318-L000062](../../.github/workflows/tests.yml#L62) | 62 | `""` | — |
| [SRC-1DB27D9318-L000063](../../.github/workflows/tests.yml#L63) | 63 | `"          status=\"$(curl --silent --output /tmp/omarai-unauth.json --write-out \"%{http_code}\" \\"` | — |
| [SRC-1DB27D9318-L000064](../../.github/workflows/tests.yml#L64) | 64 | `"            --header \"Content-Type: application/json\" \\"` | — |
| [SRC-1DB27D9318-L000065](../../.github/workflows/tests.yml#L65) | 65 | `"            --data '{\"question\":\"smoke\"}' http://127.0.0.1:18765/api/agent)\""` | — |
| [SRC-1DB27D9318-L000066](../../.github/workflows/tests.yml#L66) | 66 | `"          if [[ \"$status\" != \"401\" ]]; then"` | — |
| [SRC-1DB27D9318-L000067](../../.github/workflows/tests.yml#L67) | 67 | `"            cat /tmp/omarai-unauth.json"` | — |
| [SRC-1DB27D9318-L000068](../../.github/workflows/tests.yml#L68) | 68 | `"            echo \"Unauthenticated /api/agent should return HTTP 401, got $status.\""` | — |
| [SRC-1DB27D9318-L000069](../../.github/workflows/tests.yml#L69) | 69 | `"            exit 1"` | — |
| [SRC-1DB27D9318-L000070](../../.github/workflows/tests.yml#L70) | 70 | `"          fi"` | — |
| [SRC-1DB27D9318-L000071](../../.github/workflows/tests.yml#L71) | 71 | `""` | — |
| [SRC-1DB27D9318-L000072](../../.github/workflows/tests.yml#L72) | 72 | `"          status=\"$(curl --silent --output /tmp/omarai-leads.json --write-out \"%{http_code}\" \\"` | — |
| [SRC-1DB27D9318-L000073](../../.github/workflows/tests.yml#L73) | 73 | `"            http://127.0.0.1:18765/api/leads)\""` | — |
| [SRC-1DB27D9318-L000074](../../.github/workflows/tests.yml#L74) | 74 | `"          if [[ \"$status\" != \"401\" ]]; then"` | — |
| [SRC-1DB27D9318-L000075](../../.github/workflows/tests.yml#L75) | 75 | `"            cat /tmp/omarai-leads.json"` | — |
| [SRC-1DB27D9318-L000076](../../.github/workflows/tests.yml#L76) | 76 | `"            echo \"Unauthenticated /api/leads should return HTTP 401, got $status.\""` | — |
| [SRC-1DB27D9318-L000077](../../.github/workflows/tests.yml#L77) | 77 | `"            exit 1"` | — |
| [SRC-1DB27D9318-L000078](../../.github/workflows/tests.yml#L78) | 78 | `"          fi"` | — |
| [SRC-1DB27D9318-L000079](../../.github/workflows/tests.yml#L79) | 79 | `""` | — |
| [SRC-1DB27D9318-L000080](../../.github/workflows/tests.yml#L80) | 80 | `"          status=\"$(curl --silent --output /tmp/omarai-leads-auth.json --write-out \"%{http_code}\" \\"` | — |
| [SRC-1DB27D9318-L000081](../../.github/workflows/tests.yml#L81) | 81 | `"            --header \"Authorization: Bearer ci-only-test-token-not-for-production-123456\" \\"` | — |
| [SRC-1DB27D9318-L000082](../../.github/workflows/tests.yml#L82) | 82 | `"            http://127.0.0.1:18765/api/leads)\""` | — |
| [SRC-1DB27D9318-L000083](../../.github/workflows/tests.yml#L83) | 83 | `"          if [[ \"$status\" != \"200\" ]]; then"` | — |
| [SRC-1DB27D9318-L000084](../../.github/workflows/tests.yml#L84) | 84 | `"            cat /tmp/omarai-leads-auth.json"` | — |
| [SRC-1DB27D9318-L000085](../../.github/workflows/tests.yml#L85) | 85 | `"            echo \"Authenticated /api/leads should return HTTP 200, got $status.\""` | — |
| [SRC-1DB27D9318-L000086](../../.github/workflows/tests.yml#L86) | 86 | `"            exit 1"` | — |
| [SRC-1DB27D9318-L000087](../../.github/workflows/tests.yml#L87) | 87 | `"          fi"` | — |
| [SRC-1DB27D9318-L000088](../../.github/workflows/tests.yml#L88) | 88 | `""` | — |
| [SRC-1DB27D9318-L000089](../../.github/workflows/tests.yml#L89) | 89 | `"          status=\"$(curl --silent --output /tmp/omarai-analysis.json --write-out \"%{http_code}\" \\"` | — |
| [SRC-1DB27D9318-L000090](../../.github/workflows/tests.yml#L90) | 90 | `"            --header \"Authorization: Bearer ci-only-test-token-not-for-production-123456\" \\"` | — |
| [SRC-1DB27D9318-L000091](../../.github/workflows/tests.yml#L91) | 91 | `"            --header \"Content-Type: application/json\" \\"` | — |
| [SRC-1DB27D9318-L000092](../../.github/workflows/tests.yml#L92) | 92 | `"            --data '{\"text\":\"بدور على شقة\",\"product_terms\":[\"شقة\"]}' \\"` | — |
| [SRC-1DB27D9318-L000093](../../.github/workflows/tests.yml#L93) | 93 | `"            http://127.0.0.1:18765/api/analyze)\""` | — |
| [SRC-1DB27D9318-L000094](../../.github/workflows/tests.yml#L94) | 94 | `"          if [[ \"$status\" != \"200\" ]]; then"` | — |
| [SRC-1DB27D9318-L000095](../../.github/workflows/tests.yml#L95) | 95 | `"            cat /tmp/omarai-analysis.json"` | — |
| [SRC-1DB27D9318-L000096](../../.github/workflows/tests.yml#L96) | 96 | `"            echo \"Authenticated /api/analyze should return HTTP 200, got $status.\""` | — |
| [SRC-1DB27D9318-L000097](../../.github/workflows/tests.yml#L97) | 97 | `"            exit 1"` | — |
| [SRC-1DB27D9318-L000098](../../.github/workflows/tests.yml#L98) | 98 | `"          fi"` | — |
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
| [SRC-84F7DE82AF-L000044](../../.github/workflows/update_index.yml#L44) | 44 | `"      - name: Generate the master, review-marker, and paginated source-line indexes"` | FND-REVIEW-84F7DE82AF-L000044 |
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
| [SRC-84F7DE82AF-L000090](../../.github/workflows/update_index.yml#L90) | 90 | `"              --body \"Automated refresh of docs/MASTER_INDEX.md, docs/SOURCE_LINES_INDEX.md, and paginated files under docs/source_index/. Includes the repository inventory, named symbol index, explicit review-marker register, and all eligible readable source lines. Opened because direct publication to main was rejected. No force update or auto-merge was performed.\""` | FND-REVIEW-84F7DE82AF-L000090 |
| [SRC-84F7DE82AF-L000091](../../.github/workflows/update_index.yml#L91) | 91 | `"            exit 0"` | — |
| [SRC-84F7DE82AF-L000092](../../.github/workflows/update_index.yml#L92) | 92 | `"          fi"` | — |
| [SRC-84F7DE82AF-L000093](../../.github/workflows/update_index.yml#L93) | 93 | `""` | — |
| [SRC-84F7DE82AF-L000094](../../.github/workflows/update_index.yml#L94) | 94 | `"          pr_number=\"$(gh pr list --state open --base main --head \"${automation_branch}\" --json number --jq '.[0].number // empty')\""` | — |
| [SRC-84F7DE82AF-L000095](../../.github/workflows/update_index.yml#L95) | 95 | `"          if [ -z \"${pr_number}\" ]; then"` | — |
| [SRC-84F7DE82AF-L000096](../../.github/workflows/update_index.yml#L96) | 96 | `"            gh pr create \\"` | — |
| [SRC-84F7DE82AF-L000097](../../.github/workflows/update_index.yml#L97) | 97 | `"              --base main \\"` | — |
| [SRC-84F7DE82AF-L000098](../../.github/workflows/update_index.yml#L98) | 98 | `"              --head \"${automation_branch}\" \\"` | — |
| [SRC-84F7DE82AF-L000099](../../.github/workflows/update_index.yml#L99) | 99 | `"              --title \"docs(index): refresh repository source-line inventory\" \\"` | — |
| [SRC-84F7DE82AF-L000100](../../.github/workflows/update_index.yml#L100) | 100 | `"              --body \"Automated refresh of docs/MASTER_INDEX.md, docs/SOURCE_LINES_INDEX.md, and paginated files under docs/source_index/. Includes the repository inventory, named symbol index, explicit review-marker register, and all eligible readable source lines. Opened because direct publication to main was rejected. No force update or auto-merge was performed.\""` | FND-REVIEW-84F7DE82AF-L000100 |
| [SRC-84F7DE82AF-L000101](../../.github/workflows/update_index.yml#L101) | 101 | `"          else"` | — |
| [SRC-84F7DE82AF-L000102](../../.github/workflows/update_index.yml#L102) | 102 | `"            gh pr edit \"${pr_number}\" \\"` | — |
| [SRC-84F7DE82AF-L000103](../../.github/workflows/update_index.yml#L103) | 103 | `"              --title \"docs(index): refresh repository source-line inventory\" \\"` | — |
| [SRC-84F7DE82AF-L000104](../../.github/workflows/update_index.yml#L104) | 104 | `"              --body \"Automated refresh of docs/MASTER_INDEX.md, docs/SOURCE_LINES_INDEX.md, and paginated files under docs/source_index/. Includes the repository inventory, named symbol index, explicit review-marker register, and all eligible readable source lines. Updated because direct publication to main was rejected. No auto-merge was performed.\""` | FND-REVIEW-84F7DE82AF-L000104 |
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
| [SRC-A54FF182C7-L000007](../../AGENTS.md#L7) | 7 | ``"- Read `docs/OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md` for broad platform requirements and release reviews involving reliability/SRE, capacity, API/security, privacy/data governance, CI/CD/supply chain, recovery, accessibility, search quality, AI/agent evaluation, cost, and operational governance. Apply only the controls relevant to the change, but explicitly record material gaps and risks."`` | — |
| [SRC-A54FF182C7-L000008](../../AGENTS.md#L8) | 8 | ``"- Use `docs/OMARAI_REQUIREMENTS_TRACEABILITY_AND_MATURITY_MODEL_AR.md` to classify important requirements, identify relevant expert-review lenses, record evidence and limitations, prioritize risks, and apply the change/release gates. Do not mark a requirement VERIFIED without implementation and reproducible evidence."`` | — |
| [SRC-A54FF182C7-L000009](../../AGENTS.md#L9) | 9 | ``"- Keep `docs/OMARAI_REQUIREMENTS_REGISTER.md` synchronized with material changes: record new findings and update the related requirement status only when supporting evidence exists. Until the code and relevant tests have been examined, use UNKNOWN; state unrun checks as NOT_RUN."`` | — |
| [SRC-A54FF182C7-L000010](../../AGENTS.md#L10) | 10 | `"- The charter is a design requirement, not evidence that controls already exist. Inspect the actual code and tests before describing implementation status."` | — |
| [SRC-A54FF182C7-L000011](../../AGENTS.md#L11) | 11 | ``"- Treat `README.md` as a description of the current documented behavior, but verify claims against code and runtime evidence when the task requires it."`` | — |
| [SRC-A54FF182C7-L000012](../../AGENTS.md#L12) | 12 | `""` | — |
| [SRC-A54FF182C7-L000013](../../AGENTS.md#L13) | 13 | `"## Evidence discipline"` | — |
| [SRC-A54FF182C7-L000014](../../AGENTS.md#L14) | 14 | `"- Label consequential findings **VERIFIED**, **INFERRED**, **PROPOSED**, or **UNKNOWN**."` | — |
| [SRC-A54FF182C7-L000015](../../AGENTS.md#L15) | 15 | `"- Never invent files, functions, branches, commits, workflows, test results, tool capabilities, deployment status, capacity numbers, or security guarantees."` | — |
| [SRC-A54FF182C7-L000016](../../AGENTS.md#L16) | 16 | `"- A configured API key is not proof that a connector works. A health/configuration response is not proof that a provider is reachable. A model's self-review is not independent verification."` | — |
| [SRC-A54FF182C7-L000017](../../AGENTS.md#L17) | 17 | `"- When reporting a test, include the exact command, actual result, relevant commit or code state, and any environment limitation. Never say a test was run when it was not."` | — |
| [SRC-A54FF182C7-L000018](../../AGENTS.md#L18) | 18 | `"- Prefer regression tests for fixed defects and measurable evidence for performance, capacity, quality, and security claims."` | — |
| [SRC-A54FF182C7-L000019](../../AGENTS.md#L19) | 19 | `""` | — |
| [SRC-A54FF182C7-L000020](../../AGENTS.md#L20) | 20 | `"## Architecture evolution and scalability"` | — |
| [SRC-A54FF182C7-L000021](../../AGENTS.md#L21) | 21 | `"- Treat scalability, maintainability, and controlled evolution as foundational requirements; read the relevant charter sections before introducing modules, agents, tools, providers, persistence, queues, or services."` | — |
| [SRC-A54FF182C7-L000022](../../AGENTS.md#L22) | 22 | `"- Prefer a well-bounded modular monolith until measured scaling, fault-isolation, security, or release-independence needs justify a separate service. Do not add microservices or abstraction layers for appearance."` | — |
| [SRC-A54FF182C7-L000023](../../AGENTS.md#L23) | 23 | `"- New modules must have explicit responsibilities, public contracts, ownership, dependency direction, and appropriate tests. Avoid circular imports and cross-module access to private implementation details."` | — |
| [SRC-A54FF182C7-L000024](../../AGENTS.md#L24) | 24 | `"- Wrap external providers behind adapters and validate their input/output contracts. Keep provider-specific SDKs and response shapes out of domain logic."` | — |
| [SRC-A54FF182C7-L000025](../../AGENTS.md#L25) | 25 | `"- New tools/agents/plugins must declare schema, permissions, data classification, timeout, resource budget, concurrency limit, retry/idempotency behavior where applicable, health-check semantics, failure modes, and disable/rollback path."` | — |
| [SRC-A54FF182C7-L000026](../../AGENTS.md#L26) | 26 | `"- Treat API and event schema changes as versioned contracts. Prefer backward-compatible evolution; document deprecations and provide migration paths for breaking changes."` | — |
| [SRC-A54FF182C7-L000027](../../AGENTS.md#L27) | 27 | `"- All persistent data-shape changes need a tested migration and data-preservation/rollback strategy proportionate to risk. Never assume production data can be recreated from scratch."` | — |
| [SRC-A54FF182C7-L000028](../../AGENTS.md#L28) | 28 | `"- Do not rely on in-process global mutable state for cross-request user, tenant, or long-running task state. Assess what must survive process restarts before adding multi-process or horizontal scaling."` | — |
| [SRC-A54FF182C7-L000029](../../AGENTS.md#L29) | 29 | `"- Before extracting services, adding queues, changing storage, or introducing a distributed system, state the evidence-based need, operational costs, failure modes, security boundary, and acceptance tests."` | — |
| [SRC-A54FF182C7-L000030](../../AGENTS.md#L30) | 30 | `"- Add architecture fitness checks where practical for dependency boundaries, contracts, migrations, secrets, concurrency isolation, and critical performance limits."` | — |
| [SRC-A54FF182C7-L000031](../../AGENTS.md#L31) | 31 | `"- Record material architectural choices and exceptions in an ADR or equivalent, including rejected alternatives, tests, risks, compatibility, and rollback."` | — |
| [SRC-A54FF182C7-L000032](../../AGENTS.md#L32) | 32 | `"- Keep expansion incremental and reversible; do not represent future architecture goals as current capabilities."` | — |
| [SRC-A54FF182C7-L000033](../../AGENTS.md#L33) | 33 | `""` | — |
| [SRC-A54FF182C7-L000034](../../AGENTS.md#L34) | 34 | `"## Required engineering behavior"` | — |
| [SRC-A54FF182C7-L000035](../../AGENTS.md#L35) | 35 | `"- Prefer the smallest safe change that solves the verified problem. Do not rewrite the architecture without a documented reason and migration path."` | — |
| [SRC-A54FF182C7-L000036](../../AGENTS.md#L36) | 36 | `"- Preserve existing behavior unless the task explicitly authorizes a change; identify compatibility risks."` | — |
| [SRC-A54FF182C7-L000037](../../AGENTS.md#L37) | 37 | `"- Bound external calls, retries, payload sizes, number of search results/pages, planning steps, model calls, elapsed time, and concurrency where applicable."` | — |
| [SRC-A54FF182C7-L000038](../../AGENTS.md#L38) | 38 | `"- Treat model output, search results, fetched pages, user files, and external tool outputs as untrusted data. Validate schemas and permissions at deterministic execution boundaries."` | — |
| [SRC-A54FF182C7-L000039](../../AGENTS.md#L39) | 39 | `"- Do not expose secrets, private user data, internal traces, or sensitive prompts in logs, HTTP errors, front-end assets, commits, or reports."` | — |
| [SRC-A54FF182C7-L000040](../../AGENTS.md#L40) | 40 | `"- Do not weaken authentication, authorization, SSRF protections, tenant/session isolation, resource limits, or test coverage to improve speed."` | — |
| [SRC-A54FF182C7-L000041](../../AGENTS.md#L41) | 41 | `"- Do not give a model unrestricted shell, filesystem, network, or database access. Tools must be explicitly registered, scoped, bounded, and verified."` | — |
| [SRC-A54FF182C7-L000042](../../AGENTS.md#L42) | 42 | `"- For any change affecting security, external networking, persistence, concurrency, or tool execution, add or identify appropriate negative/failure tests, not only happy-path checks."` | — |
| [SRC-A54FF182C7-L000043](../../AGENTS.md#L43) | 43 | `"- For performance or scalability work, establish a baseline and test in a named environment. Never claim support for an arbitrary user count without a reproducible load-test result."` | — |
| [SRC-A54FF182C7-L000044](../../AGENTS.md#L44) | 44 | `"- If evidence is insufficient, state the unknown and the smallest safe method to verify it."` | — |
| [SRC-A54FF182C7-L000045](../../AGENTS.md#L45) | 45 | `""` | — |
| [SRC-A54FF182C7-L000046](../../AGENTS.md#L46) | 46 | `"## Change and release control"` | — |
| [SRC-A54FF182C7-L000047](../../AGENTS.md#L47) | 47 | `"- Inspect the current branch, HEAD, working diff, and relevant files before editing."` | — |
| [SRC-A54FF182C7-L000048](../../AGENTS.md#L48) | 48 | `"- Work on a dedicated branch; keep changes scoped and reviewable."` | — |
| [SRC-A54FF182C7-L000049](../../AGENTS.md#L49) | 49 | `"- Run applicable checks when tools and environment permit, and report any checks that could not be run."` | — |
| [SRC-A54FF182C7-L000050](../../AGENTS.md#L50) | 50 | `"- Review the final diff and verify documentation links and new-file paths."` | — |
| [SRC-A54FF182C7-L000051](../../AGENTS.md#L51) | 51 | `"- Never merge a pull request, force-update a protected branch, or deploy to production without explicit authorization from the Human Director."` | — |
| [SRC-A54FF182C7-L000052](../../AGENTS.md#L52) | 52 | ``"- Do not present a proposed or unmerged change as already effective on `main`."`` | — |
| [SRC-A54FF182C7-L000053](../../AGENTS.md#L53) | 53 | `"- Update the charter or related documentation when a material design decision changes; document major architectural choices and exceptions with rationale, risks, tests, and rollback considerations."` | — |
| [SRC-A54FF182C7-L000054](../../AGENTS.md#L54) | 54 | `""` | — |
| [SRC-A54FF182C7-L000055](../../AGENTS.md#L55) | 55 | `"## Platform-grade readiness"` | — |
| [SRC-A54FF182C7-L000056](../../AGENTS.md#L56) | 56 | `"- For material production-facing changes, assess the applicable release gates in both the charter and the Global Platform Engineering Baseline; do not treat a checklist as proof of compliance."` | — |
| [SRC-A54FF182C7-L000057](../../AGENTS.md#L57) | 57 | `"- Define measurable SLI/SLO or a baseline where useful. Never invent uptime, latency, capacity, security maturity, cost, or recovery guarantees."` | — |
| [SRC-A54FF182C7-L000058](../../AGENTS.md#L58) | 58 | `"- Review blast radius, dependency failure, graceful degradation, quotas, per-request budgets, data lifecycle, tenant isolation when multi-user, supply-chain exposure, observability/privacy, and recovery proportional to risk."` | — |
| [SRC-A54FF182C7-L000059](../../AGENTS.md#L59) | 59 | `"- For AI/agent changes, test Arabic task quality, citation support, prompt injection, untrusted tool/page content, unauthorized actions, loops, provider failures, cost bounds, and safe fallback as applicable."` | — |
| [SRC-A54FF182C7-L000060](../../AGENTS.md#L60) | 60 | `"- Require an explicit reason before adding distributed infrastructure; document simpler alternatives and lifecycle costs. Do not apply every enterprise control blindly to a small deployment, but do not conceal a risk merely because a control is expensive or not yet supported."` | — |
| [SRC-A54FF182C7-L000061](../../AGENTS.md#L61) | 61 | `""` | — |
| [SRC-A54FF182C7-L000062](../../AGENTS.md#L62) | 62 | `"## Requirement traceability and expert review"` | — |
| [SRC-A54FF182C7-L000063](../../AGENTS.md#L63) | 63 | `"- For material changes, create or update stable requirement IDs and record applicability, status, evidence, test command/results, environment, limitations, residual risk, and owner in the requirements register or an equivalent reviewed record."` | — |
| [SRC-A54FF182C7-L000064](../../AGENTS.md#L64) | 64 | `"- Use all relevant discipline lenses (architecture, security, privacy, data, SRE, performance, AI evaluation, search/evidence, accessibility, supply chain, cost, and operations); do not claim that a human specialist independently reviewed work unless that actually happened."` | — |
| [SRC-A54FF182C7-L000065](../../AGENTS.md#L65) | 65 | `"- Keep non-applicable and waived requirements distinct from unknown ones. Exceptions to MUST controls need scope, compensating controls, an approver, a revisit/expiry condition, and recorded residual risk."` | — |
| [SRC-A54FF182C7-L000066](../../AGENTS.md#L66) | 66 | `"- Do not build advanced infrastructure to satisfy a checklist by appearance. Use trigger conditions and evidence in the baseline to decide when advanced requirements apply."` | — |
| [SRC-A54FF182C7-L000067](../../AGENTS.md#L67) | 67 | `""` | — |
| [SRC-A54FF182C7-L000068](../../AGENTS.md#L68) | 68 | `"## Acceptance principle"` | — |
| [SRC-A54FF182C7-L000069](../../AGENTS.md#L69) | 69 | `"A capability is not complete because it appears in a plan, comment, prompt, or documentation. It is complete only to the extent supported by the implementation, relevant tests, observed output, and explicitly stated limitations."` | — |
## الوكيل والمنطق

### FILE-E120A62E2E — [agents/__init__.py](../../agents/__init__.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-E120A62E2E-L000001](../../agents/__init__.py#L1) | 1 | `"\"\"\"Omarai lead-intent agent package.\"\"\""` | — |
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
| [SRC-5587371288-L000042](../../agents/intent_router.py#L42) | 42 | `"})"` | — |
| [SRC-5587371288-L000043](../../agents/intent_router.py#L43) | 43 | `"_AMBIGUOUS_ENGLISH = frozenset({"` | — |
| [SRC-5587371288-L000044](../../agents/intent_router.py#L44) | 44 | `"    \"how much is it\", \"how much does it cost\", \"what is its price\","` | — |
| [SRC-5587371288-L000045](../../agents/intent_router.py#L45) | 45 | `"    \"what about it\", \"what about this\", \"is it good\", \"is this good\","` | — |
| [SRC-5587371288-L000046](../../agents/intent_router.py#L46) | 46 | `"    \"does it work\", \"compare them\", \"compare these\", \"compare the two\","` | — |
| [SRC-5587371288-L000047](../../agents/intent_router.py#L47) | 47 | `"    \"what do you think of it\", \"should i buy it\", \"is it worth it\","` | — |
| [SRC-5587371288-L000048](../../agents/intent_router.py#L48) | 48 | `"})"` | — |
| [SRC-5587371288-L000049](../../agents/intent_router.py#L49) | 49 | `"_DEEP_TERMS = ("` | — |
| [SRC-5587371288-L000050](../../agents/intent_router.py#L50) | 50 | `"    \"بحث عميق\", \"بحث معمق\", \"بحث مكثف\", \"بحث شامل\", \"بالتفصيل\","` | — |
| [SRC-5587371288-L000051](../../agents/intent_router.py#L51) | 51 | `"    \"قارن\", \"مقارنه\", \"حلل بعمق\", \"مزايا وعيوب\", \"الايجابيات والسلبيات\","` | — |
| [SRC-5587371288-L000052](../../agents/intent_router.py#L52) | 52 | `"    \"كل الجوانب\", \"دراسه مقارنه\", \"compare\", \"comparison\", \"deep research\","` | — |
| [SRC-5587371288-L000053](../../agents/intent_router.py#L53) | 53 | `"    \"in-depth\", \"comprehensive\", \"pros and cons\", \"trade-offs\","` | — |
| [SRC-5587371288-L000054](../../agents/intent_router.py#L54) | 54 | `")"` | — |
| [SRC-5587371288-L000055](../../agents/intent_router.py#L55) | 55 | `"_MULTIPART_MARKERS = ("` | — |
| [SRC-5587371288-L000056](../../agents/intent_router.py#L56) | 56 | `"    \"بالاضافه الى\", \"مع مراعاه\", \"من حيث\", \"وكذلك\", \"و ايضا\", \"والفرق\","` | — |
| [SRC-5587371288-L000057](../../agents/intent_router.py#L57) | 57 | `"    \"على ان تشمل\", \"and also\", \"as well as\", \"taking into account\","` | — |
| [SRC-5587371288-L000058](../../agents/intent_router.py#L58) | 58 | `"    \"in terms of\", \"along with\","` | — |
| [SRC-5587371288-L000059](../../agents/intent_router.py#L59) | 59 | `")"` | — |
| [SRC-5587371288-L000060](../../agents/intent_router.py#L60) | 60 | `""` | — |
| [SRC-5587371288-L000061](../../agents/intent_router.py#L61) | 61 | `""` | — |
| [SRC-5587371288-L000062](../../agents/intent_router.py#L62) | 62 | `"def _normalize(value: str) -> str:"` | — |
| [SRC-5587371288-L000063](../../agents/intent_router.py#L63) | 63 | `"    value = unicodedata.normalize(\"NFKC\", value or \"\").casefold()"` | — |
| [SRC-5587371288-L000064](../../agents/intent_router.py#L64) | 64 | `"    value = _ARABIC_DIACRITICS.sub(\"\", value)"` | — |
| [SRC-5587371288-L000065](../../agents/intent_router.py#L65) | 65 | `"    value = value.translate(str.maketrans({"` | — |
| [SRC-5587371288-L000066](../../agents/intent_router.py#L66) | 66 | `"        \"أ\": \"ا\", \"إ\": \"ا\", \"آ\": \"ا\", \"ٱ\": \"ا\", \"ى\": \"ي\", \"ة\": \"ه\", \"ـ\": \"\","` | — |
| [SRC-5587371288-L000067](../../agents/intent_router.py#L67) | 67 | `"    }))"` | — |
| [SRC-5587371288-L000068](../../agents/intent_router.py#L68) | 68 | `"    value = _PUNCTUATION.sub(\" \", value)"` | — |
| [SRC-5587371288-L000069](../../agents/intent_router.py#L69) | 69 | `"    return _SPACE.sub(\" \", value).strip()"` | — |
| [SRC-5587371288-L000070](../../agents/intent_router.py#L70) | 70 | `""` | — |
| [SRC-5587371288-L000071](../../agents/intent_router.py#L71) | 71 | `""` | — |
| [SRC-5587371288-L000072](../../agents/intent_router.py#L72) | 72 | `"def _is_smalltalk(question: str) -> bool:"` | — |
| [SRC-5587371288-L000073](../../agents/intent_router.py#L73) | 73 | `"    normalized = _normalize(question)"` | — |
| [SRC-5587371288-L000074](../../agents/intent_router.py#L74) | 74 | `"    if normalized in {_normalize(item) for item in _SMALLTALK}:"` | — |
| [SRC-5587371288-L000075](../../agents/intent_router.py#L75) | 75 | `"        return True"` | — |
| [SRC-5587371288-L000076](../../agents/intent_router.py#L76) | 76 | `"    # Keep these patterns narrow: an opening greeting followed by a real question"` | — |
| [SRC-5587371288-L000077](../../agents/intent_router.py#L77) | 77 | `"    # is not itself a greeting-only request."` | — |
| [SRC-5587371288-L000078](../../agents/intent_router.py#L78) | 78 | `"    return bool("` | — |
| [SRC-5587371288-L000079](../../agents/intent_router.py#L79) | 79 | `"        normalized.startswith(\"السلام عليكم \")"` | — |
| [SRC-5587371288-L000080](../../agents/intent_router.py#L80) | 80 | `"        and normalized[14:].strip() in _SMALLTALK"` | — |
| [SRC-5587371288-L000081](../../agents/intent_router.py#L81) | 81 | `"    )"` | — |
| [SRC-5587371288-L000082](../../agents/intent_router.py#L82) | 82 | `""` | — |
| [SRC-5587371288-L000083](../../agents/intent_router.py#L83) | 83 | `""` | — |
| [SRC-5587371288-L000084](../../agents/intent_router.py#L84) | 84 | `"def _has_context(history: Any) -> bool:"` | — |
| [SRC-5587371288-L000085](../../agents/intent_router.py#L85) | 85 | `"    \"\"\"Check whether the latest user turn can plausibly anchor a short follow-up."` | — |
| [SRC-5587371288-L000086](../../agents/intent_router.py#L86) | 86 | `""` | — |
| [SRC-5587371288-L000087](../../agents/intent_router.py#L87) | 87 | `"    Do not resurrect an older topic after the user's most recent turn was only"` | — |
| [SRC-5587371288-L000088](../../agents/intent_router.py#L88) | 88 | `"    an acknowledgment; stale context is a common source of wrong referents."` | — |
| [SRC-5587371288-L000089](../../agents/intent_router.py#L89) | 89 | `"    \"\"\""` | — |
| [SRC-5587371288-L000090](../../agents/intent_router.py#L90) | 90 | `"    if not isinstance(history, list):"` | — |
| [SRC-5587371288-L000091](../../agents/intent_router.py#L91) | 91 | `"        return False"` | — |
| [SRC-5587371288-L000092](../../agents/intent_router.py#L92) | 92 | `"    for item in reversed(history[-MAX_CONTEXT_TURNS:]):"` | — |
| [SRC-5587371288-L000093](../../agents/intent_router.py#L93) | 93 | `"        if not isinstance(item, dict) or item.get(\"role\") != \"user\":"` | — |
| [SRC-5587371288-L000094](../../agents/intent_router.py#L94) | 94 | `"            continue"` | — |
| [SRC-5587371288-L000095](../../agents/intent_router.py#L95) | 95 | `"        content = item.get(\"content\")"` | — |
| [SRC-5587371288-L000096](../../agents/intent_router.py#L96) | 96 | `"        if not isinstance(content, str):"` | — |
| [SRC-5587371288-L000097](../../agents/intent_router.py#L97) | 97 | `"            continue"` | — |
| [SRC-5587371288-L000098](../../agents/intent_router.py#L98) | 98 | `"        normalized = _normalize(content)"` | — |
| [SRC-5587371288-L000099](../../agents/intent_router.py#L99) | 99 | `"        if not normalized or _is_smalltalk(normalized):"` | — |
| [SRC-5587371288-L000100](../../agents/intent_router.py#L100) | 100 | `"            return False"` | — |
| [SRC-5587371288-L000101](../../agents/intent_router.py#L101) | 101 | `"        meaningful = re.findall(r\"[a-z0-9]+\|[\\u0600-\\u06FF]+\", normalized)"` | — |
| [SRC-5587371288-L000102](../../agents/intent_router.py#L102) | 102 | `"        return len(meaningful) >= 2 and len(normalized) >= 8"` | — |
| [SRC-5587371288-L000103](../../agents/intent_router.py#L103) | 103 | `"    return False"` | — |
| [SRC-5587371288-L000104](../../agents/intent_router.py#L104) | 104 | `""` | — |
| [SRC-5587371288-L000105](../../agents/intent_router.py#L105) | 105 | `""` | — |
| [SRC-5587371288-L000106](../../agents/intent_router.py#L106) | 106 | `"def _has_live_signal(question: str) -> bool:"` | — |
| [SRC-5587371288-L000107](../../agents/intent_router.py#L107) | 107 | `"    \"\"\"Recognize common time-sensitive or explicit-search requests without a model.\"\"\""` | — |
| [SRC-5587371288-L000108](../../agents/intent_router.py#L108) | 108 | `"    normalized = _normalize(question)"` | — |
| [SRC-5587371288-L000109](../../agents/intent_router.py#L109) | 109 | `"    live_terms = ("` | — |
| [SRC-5587371288-L000110](../../agents/intent_router.py#L110) | 110 | `"        \"ابحث\", \"بحث عن\", \"دور على\", \"دورلي\", \"هات رابط\", \"هاتلي\", \"جيبلي\","` | — |
| [SRC-5587371288-L000111](../../agents/intent_router.py#L111) | 111 | `"        \"اعثر على\", \"موقع\", \"رابط\", \"لينك\", \"اخبار\", \"اخر\", \"احدث\", \"اليوم\","` | — |
| [SRC-5587371288-L000112](../../agents/intent_router.py#L112) | 112 | `"        \"دلوقتي\", \"حاليا\", \"سعر\", \"اسعار\", \"للبيع\", \"للايجار\", \"ايجار\","` | — |
| [SRC-5587371288-L000113](../../agents/intent_router.py#L113) | 113 | `"        \"معاينه\", \"عميل محتمل\", \"عملاء محتملين\", \"وظائف\", \"وظيفه\", \"حجز\","` | — |
| [SRC-5587371288-L000114](../../agents/intent_router.py#L114) | 114 | `"        \"موعد\", \"الطقس\", \"سهم\", \"سعر الصرف\", \"search\", \"find\", \"look up\","` | — |
| [SRC-5587371288-L000115](../../agents/intent_router.py#L115) | 115 | `"        \"latest\", \"today\", \"current\", \"news\", \"price\", \"for sale\", \"for rent\","` | — |
| [SRC-5587371288-L000116](../../agents/intent_router.py#L116) | 116 | `"        \"real estate\", \"job opening\", \"appointment\", \"reservation\", \"weather\","` | — |
| [SRC-5587371288-L000117](../../agents/intent_router.py#L117) | 117 | `"        \"stock price\", \"exchange rate\","` | — |
| [SRC-5587371288-L000118](../../agents/intent_router.py#L118) | 118 | `"    )"` | — |
| [SRC-5587371288-L000119](../../agents/intent_router.py#L119) | 119 | `"    return any(_normalize(term) in normalized for term in live_terms) or bool("` | — |
| [SRC-5587371288-L000120](../../agents/intent_router.py#L120) | 120 | `"        re.search(r\"https?://\", question, flags=re.IGNORECASE)"` | — |
| [SRC-5587371288-L000121](../../agents/intent_router.py#L121) | 121 | `"    )"` | — |
| [SRC-5587371288-L000122](../../agents/intent_router.py#L122) | 122 | `""` | — |
| [SRC-5587371288-L000123](../../agents/intent_router.py#L123) | 123 | `""` | — |
| [SRC-5587371288-L000124](../../agents/intent_router.py#L124) | 124 | `"def _is_lead_generation_request(question: str) -> bool:"` | — |
| [SRC-5587371288-L000125](../../agents/intent_router.py#L125) | 125 | `"    \"\"\"Recognize an explicit request to discover prospective buyers/customers."` | — |
| [SRC-5587371288-L000126](../../agents/intent_router.py#L126) | 126 | `""` | — |
| [SRC-5587371288-L000127](../../agents/intent_router.py#L127) | 127 | `"    A product or property listing request alone is not lead generation. This"` | — |
| [SRC-5587371288-L000128](../../agents/intent_router.py#L128) | 128 | `"    route requires a prospect/customer target plus an action to find one."` | — |
| [SRC-5587371288-L000129](../../agents/intent_router.py#L129) | 129 | `"    \"\"\""` | — |
| [SRC-5587371288-L000130](../../agents/intent_router.py#L130) | 130 | `"    normalized = _normalize(question)"` | — |
| [SRC-5587371288-L000131](../../agents/intent_router.py#L131) | 131 | `"    arabic_actions = (\"ابحث عن\", \"دور على\", \"دورلي على\", \"اعثر على\", \"هاتلي\", \"هات\")"` | — |
| [SRC-5587371288-L000132](../../agents/intent_router.py#L132) | 132 | `"    arabic_targets = (\"عميل\", \"عملاء\", \"مشتري\", \"مشتر\", \"مشترين\", \"عملاء محتملين\")"` | — |
| [SRC-5587371288-L000133](../../agents/intent_router.py#L133) | 133 | `"    english_patterns = ("` | — |
| [SRC-5587371288-L000134](../../agents/intent_router.py#L134) | 134 | `"        r\"\\b(?:find\|search for\|look for\|identify\|generate\|build\|create)\\b.{0,45}\\b(?:buyers?\|customers?\|prospects?\|leads?)\\b\|\\b(?:find\|build\|create\|generate)\\s+(?:a\\s+)?(?:lead generation\|prospect list)\\b\","` | — |
| [SRC-5587371288-L000135](../../agents/intent_router.py#L135) | 135 | `"    )"` | — |
| [SRC-5587371288-L000136](../../agents/intent_router.py#L136) | 136 | `"    if any(action in normalized for action in arabic_actions) and any("` | — |
| [SRC-5587371288-L000137](../../agents/intent_router.py#L137) | 137 | `"        target in normalized for target in arabic_targets"` | — |
| [SRC-5587371288-L000138](../../agents/intent_router.py#L138) | 138 | `"    ):"` | — |
| [SRC-5587371288-L000139](../../agents/intent_router.py#L139) | 139 | `"        return True"` | — |
| [SRC-5587371288-L000140](../../agents/intent_router.py#L140) | 140 | `"    if any(re.search(pattern, normalized) for pattern in english_patterns):"` | — |
| [SRC-5587371288-L000141](../../agents/intent_router.py#L141) | 141 | `"        return True"` | — |
| [SRC-5587371288-L000142](../../agents/intent_router.py#L142) | 142 | `"    return bool("` | — |
| [SRC-5587371288-L000143](../../agents/intent_router.py#L143) | 143 | `"        re.search("` | — |
| [SRC-5587371288-L000144](../../agents/intent_router.py#L144) | 144 | `"            r\"\\b(?:buyers?\|customers?\|prospects?\|leads?)\\b.{0,45}\\b\""` | — |
| [SRC-5587371288-L000145](../../agents/intent_router.py#L145) | 145 | `"            r\"(?:looking to buy\|want to buy\|wants to buy\|seeking to purchase)\\b\","` | — |
| [SRC-5587371288-L000146](../../agents/intent_router.py#L146) | 146 | `"            normalized,"` | — |
| [SRC-5587371288-L000147](../../agents/intent_router.py#L147) | 147 | `"        )"` | — |
| [SRC-5587371288-L000148](../../agents/intent_router.py#L148) | 148 | `"    )"` | — |
| [SRC-5587371288-L000149](../../agents/intent_router.py#L149) | 149 | `""` | — |
| [SRC-5587371288-L000150](../../agents/intent_router.py#L150) | 150 | `""` | — |
| [SRC-5587371288-L000151](../../agents/intent_router.py#L151) | 151 | `"def _needs_clarification(question: str) -> bool:"` | — |
| [SRC-5587371288-L000152](../../agents/intent_router.py#L152) | 152 | `"    normalized = _normalize(question)"` | — |
| [SRC-5587371288-L000153](../../agents/intent_router.py#L153) | 153 | `"    if ("` | — |
| [SRC-5587371288-L000154](../../agents/intent_router.py#L154) | 154 | `"        normalized in {_normalize(item) for item in _AMBIGUOUS_ARABIC}"` | — |
| [SRC-5587371288-L000155](../../agents/intent_router.py#L155) | 155 | `"        or normalized in {_normalize(item) for item in _AMBIGUOUS_ENGLISH}"` | — |
| [SRC-5587371288-L000156](../../agents/intent_router.py#L156) | 156 | `"    ):"` | — |
| [SRC-5587371288-L000157](../../agents/intent_router.py#L157) | 157 | `"        return True"` | — |
| [SRC-5587371288-L000158](../../agents/intent_router.py#L158) | 158 | `"    # Common inflected forms missed by exact phrase matching."` | — |
| [SRC-5587371288-L000159](../../agents/intent_router.py#L159) | 159 | `"    return bool("` | — |
| [SRC-5587371288-L000160](../../agents/intent_router.py#L160) | 160 | `"        re.fullmatch(r\"(?:كام\|كم\|بكام)\\s+(?:سعر\|ثمن)\\s*(?:ها\|ه\|هم)\", normalized)"` | — |
| [SRC-5587371288-L000161](../../agents/intent_router.py#L161) | 161 | `"        or re.fullmatch(r\"(?:قارن\|قارنلي)\\s+(?:بينهم\|بينهما\|دول\|دي\|دولتين)\", normalized)"` | — |
| [SRC-5587371288-L000162](../../agents/intent_router.py#L162) | 162 | `"    )"` | — |
| [SRC-5587371288-L000163](../../agents/intent_router.py#L163) | 163 | `""` | — |
| [SRC-5587371288-L000164](../../agents/intent_router.py#L164) | 164 | `""` | — |
| [SRC-5587371288-L000165](../../agents/intent_router.py#L165) | 165 | `"def _is_deep(question: str) -> bool:"` | — |
| [SRC-5587371288-L000166](../../agents/intent_router.py#L166) | 166 | `"    normalized = _normalize(question)"` | — |
| [SRC-5587371288-L000167](../../agents/intent_router.py#L167) | 167 | `"    if any(_normalize(term) in normalized for term in _DEEP_TERMS):"` | — |
| [SRC-5587371288-L000168](../../agents/intent_router.py#L168) | 168 | `"        return True"` | — |
| [SRC-5587371288-L000169](../../agents/intent_router.py#L169) | 169 | `"    # Explicit multi-dimension comparisons need evidence from more than one angle."` | — |
| [SRC-5587371288-L000170](../../agents/intent_router.py#L170) | 170 | `"    dimensions = ("` | — |
| [SRC-5587371288-L000171](../../agents/intent_router.py#L171) | 171 | `"        \"السعر\", \"سعر\", \"بطاريه\", \"كاميرا\", \"اداء\", \"امان\", \"تكلفه\","` | — |
| [SRC-5587371288-L000172](../../agents/intent_router.py#L172) | 172 | `"        \"الصيانه\", \"الجوده\", \"المميزات\", \"العيوب\", \"الاراء\", \"المراجعات\","` | — |
| [SRC-5587371288-L000173](../../agents/intent_router.py#L173) | 173 | `"        \"price\", \"battery\", \"camera\", \"performance\", \"safety\", \"cost\","` | — |
| [SRC-5587371288-L000174](../../agents/intent_router.py#L174) | 174 | `"        \"maintenance\", \"quality\", \"features\", \"drawbacks\", \"reviews\","` | — |
| [SRC-5587371288-L000175](../../agents/intent_router.py#L175) | 175 | `"    )"` | — |
| [SRC-5587371288-L000176](../../agents/intent_router.py#L176) | 176 | `"    matched_dimensions = sum(1 for item in dimensions if _normalize(item) in normalized)"` | — |
| [SRC-5587371288-L000177](../../agents/intent_router.py#L177) | 177 | `"    return matched_dimensions >= 2 and any("` | — |
| [SRC-5587371288-L000178](../../agents/intent_router.py#L178) | 178 | `"        marker in normalized for marker in _MULTIPART_MARKERS"` | — |
| [SRC-5587371288-L000179](../../agents/intent_router.py#L179) | 179 | `"    )"` | — |
| [SRC-5587371288-L000180](../../agents/intent_router.py#L180) | 180 | `""` | — |
| [SRC-5587371288-L000181](../../agents/intent_router.py#L181) | 181 | `""` | — |
| [SRC-5587371288-L000182](../../agents/intent_router.py#L182) | 182 | `"def _is_page_summarization_request(question: str) -> bool:"` | — |
| [SRC-5587371288-L000183](../../agents/intent_router.py#L183) | 183 | `"    \"\"\"Recognize a request to summarize a specific web page or link.\"\"\""` | — |
| [SRC-5587371288-L000184](../../agents/intent_router.py#L184) | 184 | `"    normalized = _normalize(question)"` | — |
| [SRC-5587371288-L000185](../../agents/intent_router.py#L185) | 185 | `"    terms = (\"لخص\", \"تلخيص\", \"ملخص\", \"summarize\", \"summarise\", \"summary\")"` | — |
| [SRC-5587371288-L000186](../../agents/intent_router.py#L186) | 186 | `"    page_references = ("` | — |
| [SRC-5587371288-L000187](../../agents/intent_router.py#L187) | 187 | `"        \"صفحه\", \"الصفحه\", \"مقال\", \"المقال\", \"رابط\", \"لينك\", \"url\","` | — |
| [SRC-5587371288-L000188](../../agents/intent_router.py#L188) | 188 | `"        \"link\", \"article\", \"page\", \"webpage\", \"web page\", \"website\","` | — |
| [SRC-5587371288-L000189](../../agents/intent_router.py#L189) | 189 | `"    )"` | — |
| [SRC-5587371288-L000190](../../agents/intent_router.py#L190) | 190 | `"    return ("` | — |
| [SRC-5587371288-L000191](../../agents/intent_router.py#L191) | 191 | `"        any(_normalize(term) in normalized for term in terms)"` | — |
| [SRC-5587371288-L000192](../../agents/intent_router.py#L192) | 192 | `"        and ("` | — |
| [SRC-5587371288-L000193](../../agents/intent_router.py#L193) | 193 | `"            bool(re.search(r\"https?://\", question, flags=re.IGNORECASE))"` | — |
| [SRC-5587371288-L000194](../../agents/intent_router.py#L194) | 194 | `"            or any(_normalize(term) in normalized for term in page_references)"` | — |
| [SRC-5587371288-L000195](../../agents/intent_router.py#L195) | 195 | `"        )"` | — |
| [SRC-5587371288-L000196](../../agents/intent_router.py#L196) | 196 | `"    )"` | — |
| [SRC-5587371288-L000197](../../agents/intent_router.py#L197) | 197 | `""` | — |
| [SRC-5587371288-L000198](../../agents/intent_router.py#L198) | 198 | `""` | — |
| [SRC-5587371288-L000199](../../agents/intent_router.py#L199) | 199 | `"def _has_inline_summary_text(question: str) -> bool:"` | — |
| [SRC-5587371288-L000200](../../agents/intent_router.py#L200) | 200 | `"    \"\"\"Detect text explicitly pasted after a summary instruction, not a web page URL.\"\"\""` | — |
| [SRC-5587371288-L000201](../../agents/intent_router.py#L201) | 201 | `"    if re.search(r\"https?://\", question, flags=re.IGNORECASE):"` | — |
| [SRC-5587371288-L000202](../../agents/intent_router.py#L202) | 202 | `"        return False"` | — |
| [SRC-5587371288-L000203](../../agents/intent_router.py#L203) | 203 | `"    normalized = _normalize(question)"` | — |
| [SRC-5587371288-L000204](../../agents/intent_router.py#L204) | 204 | `"    markers = ("` | — |
| [SRC-5587371288-L000205](../../agents/intent_router.py#L205) | 205 | `"        \"النص التالي\", \"النص الاتي\", \"النص ده\", \"النص اللي جاي\","` | — |
| [SRC-5587371288-L000206](../../agents/intent_router.py#L206) | 206 | `"        \"this text\", \"following text\", \"the following text\", \"text below\","` | — |
| [SRC-5587371288-L000207](../../agents/intent_router.py#L207) | 207 | `"        \"text to summarize\", \"content below\","` | — |
| [SRC-5587371288-L000208](../../agents/intent_router.py#L208) | 208 | `"    )"` | — |
| [SRC-5587371288-L000209](../../agents/intent_router.py#L209) | 209 | `"    for marker in markers:"` | — |
| [SRC-5587371288-L000210](../../agents/intent_router.py#L210) | 210 | `"        normalized_marker = _normalize(marker)"` | — |
| [SRC-5587371288-L000211](../../agents/intent_router.py#L211) | 211 | `"        if normalized_marker in normalized:"` | — |
| [SRC-5587371288-L000212](../../agents/intent_router.py#L212) | 212 | `"            remainder = normalized.split(normalized_marker, 1)[1].strip()"` | — |
| [SRC-5587371288-L000213](../../agents/intent_router.py#L213) | 213 | `"            if len(remainder) >= 8:"` | — |
| [SRC-5587371288-L000214](../../agents/intent_router.py#L214) | 214 | `"                return True"` | — |
| [SRC-5587371288-L000215](../../agents/intent_router.py#L215) | 215 | `"    # Also allow a concise direct form such as \"لخص: [pasted paragraph]\"."` | — |
| [SRC-5587371288-L000216](../../agents/intent_router.py#L216) | 216 | `"    return bool("` | — |
| [SRC-5587371288-L000217](../../agents/intent_router.py#L217) | 217 | `"        re.search("` | — |
| [SRC-5587371288-L000218](../../agents/intent_router.py#L218) | 218 | `"            r\"^\\s*(?:لخص(?:\\s+لي)?\|تلخيص\|summari[sz]e\|summary)\\s*[:：]\\s*\\S.{12,}$\","` | — |
| [SRC-5587371288-L000219](../../agents/intent_router.py#L219) | 219 | `"            question,"` | — |
| [SRC-5587371288-L000220](../../agents/intent_router.py#L220) | 220 | `"            flags=re.IGNORECASE,"` | — |
| [SRC-5587371288-L000221](../../agents/intent_router.py#L221) | 221 | `"        )"` | — |
| [SRC-5587371288-L000222](../../agents/intent_router.py#L222) | 222 | `"    )"` | — |
| [SRC-5587371288-L000223](../../agents/intent_router.py#L223) | 223 | `""` | — |
| [SRC-5587371288-L000224](../../agents/intent_router.py#L224) | 224 | `""` | — |
| [SRC-5587371288-L000225](../../agents/intent_router.py#L225) | 225 | `"def route_intent("` | — |
| [SRC-5587371288-L000226](../../agents/intent_router.py#L226) | 226 | `"    question: str,"` | — |
| [SRC-5587371288-L000227](../../agents/intent_router.py#L227) | 227 | `"    history: Any = None,"` | — |
| [SRC-5587371288-L000228](../../agents/intent_router.py#L228) | 228 | `"    mode: str = \"auto\","` | — |
| [SRC-5587371288-L000229](../../agents/intent_router.py#L229) | 229 | `"    *,"` | — |
| [SRC-5587371288-L000230](../../agents/intent_router.py#L230) | 230 | `"    capability_question: bool = False,"` | — |
| [SRC-5587371288-L000231](../../agents/intent_router.py#L231) | 231 | `"    requires_web: bool = False,"` | — |
| [SRC-5587371288-L000232](../../agents/intent_router.py#L232) | 232 | `") -> dict[str, Any]:"` | — |
| [SRC-5587371288-L000233](../../agents/intent_router.py#L233) | 233 | `"    \"\"\"Return a deterministic route and auditable reason for a user question.\"\"\""` | — |
| [SRC-5587371288-L000234](../../agents/intent_router.py#L234) | 234 | `"    clean_mode = mode.strip().lower() if isinstance(mode, str) else \"auto\""` | — |
| [SRC-5587371288-L000235](../../agents/intent_router.py#L235) | 235 | `"    context_available = _has_context(history)"` | — |
| [SRC-5587371288-L000236](../../agents/intent_router.py#L236) | 236 | `""` | — |
| [SRC-5587371288-L000237](../../agents/intent_router.py#L237) | 237 | `"    # An explicitly selected mode is a user control and takes precedence over"` | — |
| [SRC-5587371288-L000238](../../agents/intent_router.py#L238) | 238 | `"    # conversational heuristics; it must not silently convert a requested search."` | — |
| [SRC-5587371288-L000239](../../agents/intent_router.py#L239) | 239 | `"    if clean_mode != \"auto\":"` | — |
| [SRC-5587371288-L000240](../../agents/intent_router.py#L240) | 240 | `"        route = \"WEB_DEEP\" if clean_mode == \"deep\" else \"WEB_SIMPLE\""` | — |
| [SRC-5587371288-L000241](../../agents/intent_router.py#L241) | 241 | `"        return {"` | — |
| [SRC-5587371288-L000242](../../agents/intent_router.py#L242) | 242 | `"            \"route\": route,"` | — |
| [SRC-5587371288-L000243](../../agents/intent_router.py#L243) | 243 | `"            \"reason\": \"explicit_mode\","` | — |
| [SRC-5587371288-L000244](../../agents/intent_router.py#L244) | 244 | `"            \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000245](../../agents/intent_router.py#L245) | 245 | `"            \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000246](../../agents/intent_router.py#L246) | 246 | `"        }"` | — |
| [SRC-5587371288-L000247](../../agents/intent_router.py#L247) | 247 | `""` | — |
| [SRC-5587371288-L000248](../../agents/intent_router.py#L248) | 248 | `"    if capability_question:"` | — |
| [SRC-5587371288-L000249](../../agents/intent_router.py#L249) | 249 | `"        return {"` | — |
| [SRC-5587371288-L000250](../../agents/intent_router.py#L250) | 250 | `"            \"route\": \"LOCAL\","` | — |
| [SRC-5587371288-L000251](../../agents/intent_router.py#L251) | 251 | `"            \"reason\": \"capability_question\","` | — |
| [SRC-5587371288-L000252](../../agents/intent_router.py#L252) | 252 | `"            \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000253](../../agents/intent_router.py#L253) | 253 | `"            \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000254](../../agents/intent_router.py#L254) | 254 | `"        }"` | — |
| [SRC-5587371288-L000255](../../agents/intent_router.py#L255) | 255 | `""` | — |
| [SRC-5587371288-L000256](../../agents/intent_router.py#L256) | 256 | `"    if _is_smalltalk(question):"` | — |
| [SRC-5587371288-L000257](../../agents/intent_router.py#L257) | 257 | `"        return {"` | — |
| [SRC-5587371288-L000258](../../agents/intent_router.py#L258) | 258 | `"            \"route\": \"LOCAL\","` | — |
| [SRC-5587371288-L000259](../../agents/intent_router.py#L259) | 259 | `"            \"reason\": \"short_conversational_turn\","` | — |
| [SRC-5587371288-L000260](../../agents/intent_router.py#L260) | 260 | `"            \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000261](../../agents/intent_router.py#L261) | 261 | `"            \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000262](../../agents/intent_router.py#L262) | 262 | `"        }"` | — |
| [SRC-5587371288-L000263](../../agents/intent_router.py#L263) | 263 | `""` | — |
| [SRC-5587371288-L000264](../../agents/intent_router.py#L264) | 264 | `"    # A page/link summary needs a concrete source. Pasted text is handled locally;"` | — |
| [SRC-5587371288-L000265](../../agents/intent_router.py#L265) | 265 | `"    # an absent source must trigger clarification rather than a search for \"the page\"."` | — |
| [SRC-5587371288-L000266](../../agents/intent_router.py#L266) | 266 | `"    if _is_page_summarization_request(question):"` | — |
| [SRC-5587371288-L000267](../../agents/intent_router.py#L267) | 267 | `"        if _has_inline_summary_text(question):"` | — |
| [SRC-5587371288-L000268](../../agents/intent_router.py#L268) | 268 | `"            return {"` | — |
| [SRC-5587371288-L000269](../../agents/intent_router.py#L269) | 269 | `"                \"route\": \"MODEL_ONLY\","` | — |
| [SRC-5587371288-L000270](../../agents/intent_router.py#L270) | 270 | `"                \"reason\": \"summarization_text_provided\","` | — |
| [SRC-5587371288-L000271](../../agents/intent_router.py#L271) | 271 | `"                \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000272](../../agents/intent_router.py#L272) | 272 | `"                \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000273](../../agents/intent_router.py#L273) | 273 | `"            }"` | — |
| [SRC-5587371288-L000274](../../agents/intent_router.py#L274) | 274 | `"        if re.search(r\"https?://\", question, flags=re.IGNORECASE):"` | — |
| [SRC-5587371288-L000275](../../agents/intent_router.py#L275) | 275 | `"            return {"` | — |
| [SRC-5587371288-L000276](../../agents/intent_router.py#L276) | 276 | `"                \"route\": \"WEB_SIMPLE\","` | — |
| [SRC-5587371288-L000277](../../agents/intent_router.py#L277) | 277 | `"                \"reason\": \"summarization_request\","` | — |
| [SRC-5587371288-L000278](../../agents/intent_router.py#L278) | 278 | `"                \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000279](../../agents/intent_router.py#L279) | 279 | `"                \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000280](../../agents/intent_router.py#L280) | 280 | `"            }"` | — |
| [SRC-5587371288-L000281](../../agents/intent_router.py#L281) | 281 | `"        return {"` | — |
| [SRC-5587371288-L000282](../../agents/intent_router.py#L282) | 282 | `"            \"route\": \"CLARIFY\","` | — |
| [SRC-5587371288-L000283](../../agents/intent_router.py#L283) | 283 | `"            \"reason\": \"missing_summarization_input\","` | — |
| [SRC-5587371288-L000284](../../agents/intent_router.py#L284) | 284 | `"            \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000285](../../agents/intent_router.py#L285) | 285 | `"            \"needs_clarification\": True,"` | — |
| [SRC-5587371288-L000286](../../agents/intent_router.py#L286) | 286 | `"        }"` | — |
| [SRC-5587371288-L000287](../../agents/intent_router.py#L287) | 287 | `""` | — |
| [SRC-5587371288-L000288](../../agents/intent_router.py#L288) | 288 | `"    ambiguous = _needs_clarification(question)"` | — |
| [SRC-5587371288-L000289](../../agents/intent_router.py#L289) | 289 | `"    if ambiguous and not context_available:"` | — |
| [SRC-5587371288-L000290](../../agents/intent_router.py#L290) | 290 | `"        return {"` | — |
| [SRC-5587371288-L000291](../../agents/intent_router.py#L291) | 291 | `"            \"route\": \"CLARIFY\","` | — |
| [SRC-5587371288-L000292](../../agents/intent_router.py#L292) | 292 | `"            \"reason\": \"missing_referent_and_no_conversation_context\","` | — |
| [SRC-5587371288-L000293](../../agents/intent_router.py#L293) | 293 | `"            \"context_available\": False,"` | — |
| [SRC-5587371288-L000294](../../agents/intent_router.py#L294) | 294 | `"            \"needs_clarification\": True,"` | — |
| [SRC-5587371288-L000295](../../agents/intent_router.py#L295) | 295 | `"        }"` | — |
| [SRC-5587371288-L000296](../../agents/intent_router.py#L296) | 296 | `""` | — |
| [SRC-5587371288-L000297](../../agents/intent_router.py#L297) | 297 | `"    if _is_lead_generation_request(question):"` | — |
| [SRC-5587371288-L000298](../../agents/intent_router.py#L298) | 298 | `"        return {"` | — |
| [SRC-5587371288-L000299](../../agents/intent_router.py#L299) | 299 | `"            \"route\": \"LEAD_GENERATION\","` | — |
| [SRC-5587371288-L000300](../../agents/intent_router.py#L300) | 300 | `"            \"reason\": \"explicit_prospect_or_buyer_discovery_request\","` | — |
| [SRC-5587371288-L000301](../../agents/intent_router.py#L301) | 301 | `"            \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000302](../../agents/intent_router.py#L302) | 302 | `"            \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000303](../../agents/intent_router.py#L303) | 303 | `"        }"` | — |
| [SRC-5587371288-L000304](../../agents/intent_router.py#L304) | 304 | `""` | — |
| [SRC-5587371288-L000305](../../agents/intent_router.py#L305) | 305 | `"    if _is_deep(question):"` | — |
| [SRC-5587371288-L000306](../../agents/intent_router.py#L306) | 306 | `"        return {"` | — |
| [SRC-5587371288-L000307](../../agents/intent_router.py#L307) | 307 | `"            \"route\": \"WEB_DEEP\","` | — |
| [SRC-5587371288-L000308](../../agents/intent_router.py#L308) | 308 | `"            \"reason\": \"comparison_or_multi_part_research\","` | — |
| [SRC-5587371288-L000309](../../agents/intent_router.py#L309) | 309 | `"            \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000310](../../agents/intent_router.py#L310) | 310 | `"            \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000311](../../agents/intent_router.py#L311) | 311 | `"        }"` | — |
| [SRC-5587371288-L000312](../../agents/intent_router.py#L312) | 312 | `""` | — |
| [SRC-5587371288-L000313](../../agents/intent_router.py#L313) | 313 | `"    if requires_web or _has_live_signal(question):"` | — |
| [SRC-5587371288-L000314](../../agents/intent_router.py#L314) | 314 | `"        return {"` | — |
| [SRC-5587371288-L000315](../../agents/intent_router.py#L315) | 315 | `"            \"route\": \"WEB_SIMPLE\","` | — |
| [SRC-5587371288-L000316](../../agents/intent_router.py#L316) | 316 | `"            \"reason\": \"freshness_or_explicit_research_signal\","` | — |
| [SRC-5587371288-L000317](../../agents/intent_router.py#L317) | 317 | `"            \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000318](../../agents/intent_router.py#L318) | 318 | `"            \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000319](../../agents/intent_router.py#L319) | 319 | `"        }"` | — |
| [SRC-5587371288-L000320](../../agents/intent_router.py#L320) | 320 | `""` | — |
| [SRC-5587371288-L000321](../../agents/intent_router.py#L321) | 321 | `"    return {"` | — |
| [SRC-5587371288-L000322](../../agents/intent_router.py#L322) | 322 | `"        \"route\": \"MODEL_ONLY\","` | — |
| [SRC-5587371288-L000323](../../agents/intent_router.py#L323) | 323 | `"        \"reason\": \"stable_knowledge_or_conversation\","` | — |
| [SRC-5587371288-L000324](../../agents/intent_router.py#L324) | 324 | `"        \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000325](../../agents/intent_router.py#L325) | 325 | `"        \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000326](../../agents/intent_router.py#L326) | 326 | `"    }"` | — |
## الوكيل والمنطق

### FILE-C9CF9B54F8 — [agents/omarai.py](../../agents/omarai.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-C9CF9B54F8-L000001](../../agents/omarai.py#L1) | 1 | `"\"\"\"Explainable Arabic lead-intent analysis and local SQLite storage.\"\"\""` | — |
| [SRC-C9CF9B54F8-L000002](../../agents/omarai.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-C9CF9B54F8-L000003](../../agents/omarai.py#L3) | 3 | `""` | — |
| [SRC-C9CF9B54F8-L000004](../../agents/omarai.py#L4) | 4 | `"import csv"` | — |
| [SRC-C9CF9B54F8-L000005](../../agents/omarai.py#L5) | 5 | `"import hashlib"` | — |
| [SRC-C9CF9B54F8-L000006](../../agents/omarai.py#L6) | 6 | `"import json"` | — |
| [SRC-C9CF9B54F8-L000007](../../agents/omarai.py#L7) | 7 | `"import re"` | — |
| [SRC-C9CF9B54F8-L000008](../../agents/omarai.py#L8) | 8 | `"import sqlite3"` | — |
| [SRC-C9CF9B54F8-L000009](../../agents/omarai.py#L9) | 9 | `"import unicodedata"` | — |
| [SRC-C9CF9B54F8-L000010](../../agents/omarai.py#L10) | 10 | `"from datetime import UTC, datetime"` | — |
| [SRC-C9CF9B54F8-L000011](../../agents/omarai.py#L11) | 11 | `"from pathlib import Path"` | — |
| [SRC-C9CF9B54F8-L000012](../../agents/omarai.py#L12) | 12 | `"from urllib.parse import urlparse"` | — |
| [SRC-C9CF9B54F8-L000013](../../agents/omarai.py#L13) | 13 | `""` | — |
| [SRC-C9CF9B54F8-L000014](../../agents/omarai.py#L14) | 14 | `"MAX_TEXT = 12000"` | — |
| [SRC-C9CF9B54F8-L000015](../../agents/omarai.py#L15) | 15 | `"_TRANSLATION = str.maketrans({\"أ\":\"ا\",\"إ\":\"ا\",\"آ\":\"ا\",\"ٱ\":\"ا\",\"ى\":\"ي\",\"ئ\":\"ي\",\"ؤ\":\"و\",\"ـ\":\"\"})"` | — |
| [SRC-C9CF9B54F8-L000016](../../agents/omarai.py#L16) | 16 | `"SIGNALS = {"` | — |
| [SRC-C9CF9B54F8-L000017](../../agents/omarai.py#L17) | 17 | `"    \"high\": (35, (\"عايز اشتري\", \"عاوز اشتري\", \"بدور على شقة\", \"بدور على عقار\", \"مطلوب شقة\", \"عايز وحدة\", \"محتاج اشتري\")),"` | — |
| [SRC-C9CF9B54F8-L000018](../../agents/omarai.py#L18) | 18 | `"    \"next_step\": (20, (\"ممكن معاينة\", \"عايز اعاين\", \"عاوز اعاين\", \"ابعت التفاصيل\", \"ابعت اللوكيشن\", \"ميعاد للمعاينة\")),"` | — |
| [SRC-C9CF9B54F8-L000019](../../agents/omarai.py#L19) | 19 | `"    \"budget\": (15, (\"السعر كام\", \"مقدم كام\", \"ميزانيتي\", \"معايا مقدم\", \"تقسيط\", \"على اقساط\", \"في حدود\")),"` | — |
| [SRC-C9CF9B54F8-L000020](../../agents/omarai.py#L20) | 20 | `"    \"explore\": (10, (\"بدور على\", \"فيه شقق\", \"ايه المتاح\", \"عايز اعرف الاسعار\")),"` | — |
| [SRC-C9CF9B54F8-L000021](../../agents/omarai.py#L21) | 21 | `"}"` | — |
| [SRC-C9CF9B54F8-L000022](../../agents/omarai.py#L22) | 22 | `"NOT_BUYER = (\"مش عايز اشتري\", \"مش عاوز اشتري\", \"عايز ابيع\", \"عاوز ابيع\", \"عندي شقة للبيع\", \"انا وسيط\", \"انا سمسار\", \"عايز ايجار\", \"للايجار\")"` | — |
| [SRC-C9CF9B54F8-L000023](../../agents/omarai.py#L23) | 23 | `""` | — |
| [SRC-C9CF9B54F8-L000024](../../agents/omarai.py#L24) | 24 | `"def normalize(text: str) -> str:"` | — |
| [SRC-C9CF9B54F8-L000025](../../agents/omarai.py#L25) | 25 | `"    value = unicodedata.normalize(\"NFKC\", str(text)).translate(_TRANSLATION)"` | — |
| [SRC-C9CF9B54F8-L000026](../../agents/omarai.py#L26) | 26 | `"    value = \"\".join(c for c in value if not unicodedata.category(c).startswith(\"M\"))"` | — |
| [SRC-C9CF9B54F8-L000027](../../agents/omarai.py#L27) | 27 | `"    return re.sub(r\"\\s+\", \" \", re.sub(r\"[^\\w\\s]\", \" \", value.casefold())).strip()"` | — |
| [SRC-C9CF9B54F8-L000028](../../agents/omarai.py#L28) | 28 | `""` | — |
| [SRC-C9CF9B54F8-L000029](../../agents/omarai.py#L29) | 29 | `"def now_utc() -> str:"` | — |
| [SRC-C9CF9B54F8-L000030](../../agents/omarai.py#L30) | 30 | `"    return datetime.now(UTC).isoformat(timespec=\"seconds\").replace(\"+00:00\", \"Z\")"` | — |
| [SRC-C9CF9B54F8-L000031](../../agents/omarai.py#L31) | 31 | `""` | — |
| [SRC-C9CF9B54F8-L000032](../../agents/omarai.py#L32) | 32 | `"def _csv_safe_cell(value: object) -> str:"` | — |
| [SRC-C9CF9B54F8-L000033](../../agents/omarai.py#L33) | 33 | `"    \"\"\"Prefix spreadsheet formulas even when hidden whitespace/control chars precede them.\"\"\""` | — |
| [SRC-C9CF9B54F8-L000034](../../agents/omarai.py#L34) | 34 | `"    text = \"\" if value is None else str(value)"` | — |
| [SRC-C9CF9B54F8-L000035](../../agents/omarai.py#L35) | 35 | `"    if not text:"` | — |
| [SRC-C9CF9B54F8-L000036](../../agents/omarai.py#L36) | 36 | `"        return text"` | — |
| [SRC-C9CF9B54F8-L000037](../../agents/omarai.py#L37) | 37 | `"    index = 0"` | — |
| [SRC-C9CF9B54F8-L000038](../../agents/omarai.py#L38) | 38 | `"    while index < len(text) and ("` | — |
| [SRC-C9CF9B54F8-L000039](../../agents/omarai.py#L39) | 39 | `"        text[index].isspace()"` | — |
| [SRC-C9CF9B54F8-L000040](../../agents/omarai.py#L40) | 40 | `"        or unicodedata.category(text[index]) in {\"Cc\", \"Cf\"}"` | — |
| [SRC-C9CF9B54F8-L000041](../../agents/omarai.py#L41) | 41 | `"    ):"` | — |
| [SRC-C9CF9B54F8-L000042](../../agents/omarai.py#L42) | 42 | `"        index += 1"` | — |
| [SRC-C9CF9B54F8-L000043](../../agents/omarai.py#L43) | 43 | `"    first_non_format = text[index:index + 1]"` | — |
| [SRC-C9CF9B54F8-L000044](../../agents/omarai.py#L44) | 44 | `"    formula_prefixes = {\"=\", \"+\", \"-\", \"@\", \"＝\", \"＋\", \"－\", \"＠\"}"` | — |
| [SRC-C9CF9B54F8-L000045](../../agents/omarai.py#L45) | 45 | `"    if text[0] in \"\\t\\r\\n\" or first_non_format in formula_prefixes:"` | — |
| [SRC-C9CF9B54F8-L000046](../../agents/omarai.py#L46) | 46 | `"        # OWASP notes that a tab inside the quoted CSV field is more resilient"` | — |
| [SRC-C9CF9B54F8-L000047](../../agents/omarai.py#L47) | 47 | `"        # in Excel than an apostrophe, although no CSV mitigation is universal."` | — |
| [SRC-C9CF9B54F8-L000048](../../agents/omarai.py#L48) | 48 | `"        return \"\\t\" + text"` | — |
| [SRC-C9CF9B54F8-L000049](../../agents/omarai.py#L49) | 49 | `"    return text"` | — |
| [SRC-C9CF9B54F8-L000050](../../agents/omarai.py#L50) | 50 | `""` | — |
| [SRC-C9CF9B54F8-L000051](../../agents/omarai.py#L51) | 51 | `"def analyze(text: str, product_terms=(), location_terms=()) -> dict:"` | — |
| [SRC-C9CF9B54F8-L000052](../../agents/omarai.py#L52) | 52 | `"    if not isinstance(text, str) or not text.strip():"` | — |
| [SRC-C9CF9B54F8-L000053](../../agents/omarai.py#L53) | 53 | `"        raise ValueError(\"text must not be empty\")"` | — |
| [SRC-C9CF9B54F8-L000054](../../agents/omarai.py#L54) | 54 | `"    if len(text) > MAX_TEXT:"` | — |
| [SRC-C9CF9B54F8-L000055](../../agents/omarai.py#L55) | 55 | `"        raise ValueError(f\"text must be at most {MAX_TEXT} characters\")"` | — |
| [SRC-C9CF9B54F8-L000056](../../agents/omarai.py#L56) | 56 | `"    body = normalize(text)"` | — |
| [SRC-C9CF9B54F8-L000057](../../agents/omarai.py#L57) | 57 | `"    excluded = [p for p in NOT_BUYER if normalize(p) in body]"` | — |
| [SRC-C9CF9B54F8-L000058](../../agents/omarai.py#L58) | 58 | `"    if excluded:"` | — |
| [SRC-C9CF9B54F8-L000059](../../agents/omarai.py#L59) | 59 | `"        return {\"score\": 0, \"label\": \"not_buyer_signal\", \"summary\": \"قد لا تكون إشارة شراء مباشرة؛ راجع النص يدويًا.\", \"matched_signals\": [{\"phrase\": p, \"category\": \"exclusion\", \"points\": 0} for p in excluded], \"warnings\": [\"تصنيف أولي وليس حكمًا نهائيًا.\"]}"` | — |
| [SRC-C9CF9B54F8-L000060](../../agents/omarai.py#L60) | 60 | `"    matches = []"` | — |
| [SRC-C9CF9B54F8-L000061](../../agents/omarai.py#L61) | 61 | `"    for category, (points, phrases) in SIGNALS.items():"` | — |
| [SRC-C9CF9B54F8-L000062](../../agents/omarai.py#L62) | 62 | `"        found = next((p for p in phrases if normalize(p) in body), None)"` | — |
| [SRC-C9CF9B54F8-L000063](../../agents/omarai.py#L63) | 63 | `"        if found:"` | — |
| [SRC-C9CF9B54F8-L000064](../../agents/omarai.py#L64) | 64 | `"            matches.append({\"phrase\": found, \"category\": category, \"points\": points})"` | — |
| [SRC-C9CF9B54F8-L000065](../../agents/omarai.py#L65) | 65 | `"    for category, terms in ((\"product_context\", product_terms), (\"location_context\", location_terms)):"` | — |
| [SRC-C9CF9B54F8-L000066](../../agents/omarai.py#L66) | 66 | `"        found = next((normalize(t) for t in terms if isinstance(t, str) and normalize(t) and normalize(t) in body), None)"` | — |
| [SRC-C9CF9B54F8-L000067](../../agents/omarai.py#L67) | 67 | `"        if found:"` | — |
| [SRC-C9CF9B54F8-L000068](../../agents/omarai.py#L68) | 68 | `"            matches.append({\"phrase\": found, \"category\": category, \"points\": 10})"` | — |
| [SRC-C9CF9B54F8-L000069](../../agents/omarai.py#L69) | 69 | `"    score = min(100, sum(x[\"points\"] for x in matches))"` | — |
| [SRC-C9CF9B54F8-L000070](../../agents/omarai.py#L70) | 70 | `"    label = \"high_intent\" if score >= 55 and any(x[\"category\"] == \"high\" for x in matches) else \"medium_intent\" if score >= 40 else \"early_research\" if score >= 20 else \"unclear\""` | — |
| [SRC-C9CF9B54F8-L000071](../../agents/omarai.py#L71) | 71 | `"    return {\"score\": score, \"label\": label, \"summary\": {\"high_intent\":\"إشارة قوية نسبيًا وفق قواعد بسيطة وتحتاج مراجعة بشرية.\",\"medium_intent\":\"مؤشرات اهتمام تستحق التأهيل والتحقق.\",\"early_research\":\"اهتمام مبكر؛ ليس عميلًا مؤهلًا بعد.\",\"unclear\":\"لا توجد مؤشرات كافية.\"}[label], \"matched_signals\": matches, \"warnings\": [\"الدرجة ليست احتمالًا إحصائيًا للشراء.\", \"لا تثبت هوية الكاتب أو قدرته على الدفع أو نيته.\", \"استخدم مصادر عامة ومسموحًا بمعالجتها فقط.\"]}"` | — |
| [SRC-C9CF9B54F8-L000072](../../agents/omarai.py#L72) | 72 | `""` | — |
| [SRC-C9CF9B54F8-L000073](../../agents/omarai.py#L73) | 73 | `"def validate_url(url: str) -> str:"` | — |
| [SRC-C9CF9B54F8-L000074](../../agents/omarai.py#L74) | 74 | `"    parsed = urlparse(str(url or \"\").strip())"` | — |
| [SRC-C9CF9B54F8-L000075](../../agents/omarai.py#L75) | 75 | `"    if parsed.scheme not in (\"http\", \"https\") or not parsed.netloc or parsed.username or parsed.password:"` | — |
| [SRC-C9CF9B54F8-L000076](../../agents/omarai.py#L76) | 76 | `"        raise ValueError(\"source_url must be an absolute http(s) URL without embedded credentials\")"` | — |
| [SRC-C9CF9B54F8-L000077](../../agents/omarai.py#L77) | 77 | `"    if len(url) > 2048:"` | — |
| [SRC-C9CF9B54F8-L000078](../../agents/omarai.py#L78) | 78 | `"        raise ValueError(\"source_url is too long\")"` | — |
| [SRC-C9CF9B54F8-L000079](../../agents/omarai.py#L79) | 79 | `"    return url.strip()"` | — |
| [SRC-C9CF9B54F8-L000080](../../agents/omarai.py#L80) | 80 | `""` | — |
| [SRC-C9CF9B54F8-L000081](../../agents/omarai.py#L81) | 81 | `"class LeadStore:"` | — |
| [SRC-C9CF9B54F8-L000082](../../agents/omarai.py#L82) | 82 | `"    def __init__(self, path: str \| Path \| None = None):"` | — |
| [SRC-C9CF9B54F8-L000083](../../agents/omarai.py#L83) | 83 | `"        self.path = Path(path or Path.home()/\".omarai\"/\"omarai.sqlite3\").expanduser()"` | — |
| [SRC-C9CF9B54F8-L000084](../../agents/omarai.py#L84) | 84 | `"        self.path.parent.mkdir(parents=True, exist_ok=True)"` | — |
| [SRC-C9CF9B54F8-L000085](../../agents/omarai.py#L85) | 85 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000086](../../agents/omarai.py#L86) | 86 | `"            db.execute(\"\"\"CREATE TABLE IF NOT EXISTS leads ("` | — |
| [SRC-C9CF9B54F8-L000087](../../agents/omarai.py#L87) | 87 | `"            id TEXT PRIMARY KEY, fingerprint TEXT UNIQUE NOT NULL, text TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000088](../../agents/omarai.py#L88) | 88 | `"            source_url TEXT NOT NULL, platform TEXT NOT NULL, observed_at TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000089](../../agents/omarai.py#L89) | 89 | `"            assessment TEXT NOT NULL, status TEXT NOT NULL, note TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000090](../../agents/omarai.py#L90) | 90 | `"            created_at TEXT NOT NULL, updated_at TEXT NOT NULL)\"\"\")"` | — |
| [SRC-C9CF9B54F8-L000091](../../agents/omarai.py#L91) | 91 | `"            db.execute(\"CREATE INDEX IF NOT EXISTS leads_status_idx ON leads(status, created_at DESC)\")"` | — |
| [SRC-C9CF9B54F8-L000092](../../agents/omarai.py#L92) | 92 | `"    def connect(self):"` | — |
| [SRC-C9CF9B54F8-L000093](../../agents/omarai.py#L93) | 93 | `"        db = sqlite3.connect(self.path, timeout=10)"` | — |
| [SRC-C9CF9B54F8-L000094](../../agents/omarai.py#L94) | 94 | `"        db.row_factory = sqlite3.Row"` | — |
| [SRC-C9CF9B54F8-L000095](../../agents/omarai.py#L95) | 95 | `"        return db"` | — |
| [SRC-C9CF9B54F8-L000096](../../agents/omarai.py#L96) | 96 | `"    def add(self, text: str, source_url: str, platform: str=\"manual\", observed_at: str \| None=None, note: str=\"\", product_terms=(), location_terms=()):"` | — |
| [SRC-C9CF9B54F8-L000097](../../agents/omarai.py#L97) | 97 | `"        if not isinstance(text, str) or not text.strip():"` | — |
| [SRC-C9CF9B54F8-L000098](../../agents/omarai.py#L98) | 98 | `"            raise ValueError(\"text is required\")"` | — |
| [SRC-C9CF9B54F8-L000099](../../agents/omarai.py#L99) | 99 | `"        if len(text) > MAX_TEXT:"` | — |
| [SRC-C9CF9B54F8-L000100](../../agents/omarai.py#L100) | 100 | `"            raise ValueError(\"text is too long\")"` | — |
| [SRC-C9CF9B54F8-L000101](../../agents/omarai.py#L101) | 101 | `"        url = validate_url(source_url)"` | — |
