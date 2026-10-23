# Omarai — نطاق التنفيذ الفعلي وحدوده

**Purpose:** Keep this scope note aligned with the source code and operator-visible claims. This document is a scope description, not a certification of compliance or live-provider availability.

**Latest post-merge baseline checked:** `main` at merge commit `528a2552c0cda809d6c444713466e0e075c13ed9` after PR #76 merged on 2026-10-21. The earlier `d46a546...` baseline below is a historical audit snapshot. Current verification and gaps are recorded in [the post-merge verification report](OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md).  
**Evidence labels:** `VERIFIED` means directly confirmed in source or a named automated check; `INFERRED` means a bounded conclusion from source structure; `UNKNOWN` means live or environmental evidence is not available. A source-level capability must not be described as a live integration test.

## Baseline history and post-merge correction — 2026-10-21

The original baseline section below records `main` at `d46a546aba97a9ca32a32c92f1cd6d8a9db2cc81`, after PR #75, when the audit-closure changes had not yet merged. PR #76 has now merged into `main` via `528a2552c0cda809d6c444713466e0e075c13ed9`. The latest PR-head CI inspected after that merge is [run #39654908040](https://github.com/mosabosama2030-oss/omarai/actions/runs/39654908040), with 384 passing tests on both Python 3.11 and 3.12, successful Ruff/index checks, and a successful production-container/API smoke job. GitHub comparison of the tested PR head `3fb0288...` to merge commit `528a255...` reports zero changed files, so the file trees match.

**CI on the merge SHA itself remains `NOT_CONFIRMED` in this review.** This update does not establish live provider availability, a hosted service, factual correctness of all answers, durable storage on a target host, load capacity, or multi-tenant isolation. Full evidence and remaining acceptance gates are in [the post-merge verification report](OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md).

## Implemented in the repository

- **Lead workspace — VERIFIED in source:** Arabic phrase normalization and heuristic intent scoring; SQLite lead persistence; duplicate detection; source metadata; manual lead-status lifecycle; CSV import/export; CLI and HTTP API.
- **Research pipeline — VERIFIED in source:** natural-language search planning with deterministic fallback; DuckDuckGo HTML and Bing RSS search; Google News RSS for freshness-sensitive requests; evidence fusion/ranking; selected public page extraction; source/provenance metadata and research diagnostics.
- **Optional connectors — VERIFIED as conditional code paths only:** Brave and Tavily when configured; DeepSeek Search when explicitly enabled with its API key; selected public social endpoints and official platform APIs when their required credentials are configured. This does not prove a specific credential, account, quota, or live connector currently works.
- **External language model — VERIFIED in source:** an OpenAI-compatible model endpoint is used for planning, answer generation and model-assisted review when a key is configured. The user question, selected history and page excerpts may be sent to that configured external provider. Omarai is not a locally trained foundation model and does not operate as an offline-only reasoning system.
- **Evidence and failure reporting — VERIFIED in source:** the answer includes sources, search-attempt outcome and diagnostic metadata; the code expressly describes its second-pass claim review as model-assisted, not an independent deterministic fact-check. Source count, domain count, and coverage indicators are not probabilities of truth or proof of editorial independence.
- **HTTP/API and UI — VERIFIED in source:** Arabic RTL web interfaces, JSON endpoints, API input checks, same-origin/configured-origin handling, an in-memory per-client rate limiter, and bearer-token protection for protected API routes when public-deployment mode is enabled.
- **Deployment configuration — VERIFIED in source:** a Dockerfile and hosting configuration exist. Their existence alone does not prove a live service was deployed, is reachable, has persistent disk, or has passed live smoke tests.
- **Automated validation — VERIFIED within the listed test scope:** after the budget/concurrency change, GitHub Actions run [39198411650](https://github.com/mosabosama2030-oss/omarai/actions/runs/39198411650) on PR #44 head `de20d029cb9877c8fdef62148f643eb9022b0956` passed Ruff, 232 pytest tests on Python 3.11, 232 pytest tests on Python 3.12, and container/protected-API smoke checks. PR #45 head `35e85ceae13b15f273997eba043b12126652f05a` passed run [39198109298](https://github.com/mosabosama2030-oss/omarai/actions/runs/39198109298), with 224 pytest tests on each Python version and container smoke checks. Both PRs were subsequently merged into the reviewed `main` lineage. These CI results do not prove live search-provider availability, factual correctness, load capacity, deployment health, or database restore.

## Explicitly out of scope or not yet proven

- **Multi-user or multi-tenant service — NOT IMPLEMENTED in the reviewed baseline:** the API uses one shared bearer token and a shared lead store; it has no per-user identity, role-based authorization or tenant/data isolation. Anyone who obtains the token has the access granted by that token. Treat a hosted instance as a single-operator service unless and until these controls are implemented and tested.
- **Deterministic verification of every factual claim — NOT IMPLEMENTED:** citation-index validation and model-assisted review are not an independent proof that every sentence follows from its cited source. Users must be shown this limitation clearly.
- **Live provider reliability — UNKNOWN unless measured:** unit tests with mocks and a successful container smoke test do not establish that a provider is currently reachable, that credentials are valid, or that the produced answer is accurate.
- **Request-wide limits — VERIFIED within automated unit-test scope:** merged code adds `agents/request_budget.py` and attaches a cooperative per-answer time/resource budget across search queries, provider search calls (including direct social HTTP operations), model attempts, page fetches, and optional server-side search-tool calls. The tested defaults are 90 seconds, 8 search queries, 32 provider/social HTTP operations, 8 model HTTP attempts, 8 page fetches, and up to 3 optional server-side tool calls, with hard-capped environment overrides. The API also applies a process-local semaphore to `/api/agent` and `/api/diagnostics` (default 4, hard maximum 8), returning 503 when all slots are occupied. Regression tests cover budget limits and rejection under an occupied slot. The deadline is cooperative, not hard cancellation; the semaphore is not distributed. Live connectors and production load remain UNKNOWN.
- **Public operational configuration — UNKNOWN until verified per deployment:** actual reverse-proxy trust, CORS allowlist, TLS termination, secret configuration, deployed commit identity, and live endpoint behavior depend on the chosen host and configuration.
- **Database continuity — UNKNOWN:** backup, restore, and durable SQLite persistence have not been proven for a specific host. Do not store irreplaceable production leads until backup/restore and storage persistence are tested.
- **Load and concurrency capacity — UNKNOWN:** a process-local semaphore is present and its rejection path is unit-tested, but that does not establish throughput or a numeric concurrent-user capacity. Do not publish throughput, availability or capacity claims without representative measurements.
- **Historical secret exposure — UNKNOWN:** a clean scan of the current tree, if obtained, does not prove the entire Git history has never contained a secret.
- **Automated outbound contact — NOT IMPLEMENTED:** the agent does not send messages or contact people automatically. Any future outbound action must have explicit policy controls and human approval.

## Operating assumptions

1. Keep the current architecture as a modular monolith unless evidence and a recorded architecture decision justify a change.
2. Default to a single-operator deployment with a private, randomly generated bearer token; never publish that token or share it as if it were individual user authentication.
3. Do not submit passwords, API keys, private information, or personal/confidential customer data to an external model provider, especially a free endpoint with its own retention/logging terms.
4. Treat page text, snippets, social posts, user history, and model output as untrusted data. They are not an authority to override application policy or execute privileged actions.
5. Label each live connector probe, deployed smoke test, migration/restore test, and load test as `NOT_RUN` until that specific test actually runs. Do not infer its success from unit-test CI.

## Explicit operating boundary — 2026-10-21

The current shared bearer token and local lead store do not establish per-user identity, per-tenant ownership, or multi-tenant isolation. Treat the deployed instance as a single-operator private tool only. Process-local concurrency and IP rate-limit state do not coordinate multiple replicas; no production load/soak test has been run. A public multi-customer service remains out of scope until identity/authorization, tenant-scoped data access, distributed limits, durable storage/restore, and adversarial isolation tests are implemented and evidenced.
## Recommended next increments

1. Keep testing the merged cooperative budget against failure paths and resource exhaustion; do not describe it as hard cancellation or load-tested capacity.
2. Add deterministic citation-integrity controls and adversarial prompt-injection tests while retaining the limitation that source entailment cannot be proved by citation-index checks alone.
3. Reconcile the shared-token/single-store deployment with the declared single-operator scope; design real identity and data isolation before any multi-user public offering.
4. Add a repeatable live connector probe and a deployed acceptance report clearly separated from mock/unit-test results.
5. Test SQLite persistence and backup/restore on the selected host before storing production lead data.
6. Reconcile remaining requirements to exact commit SHAs and individual tests; keep untested requirements `UNKNOWN` and unrun checks `NOT_RUN`.
7. Keep all external contact and consequential actions human-approved.


## Latest verification boundary — 2026-10-21

هذا التحديث أحدث من ملحقات CI السابقة في هذه الوثيقة، ويجب قراءته معها دون حذف سجل النتائج التاريخية:

- آخر تشغيل شامل أخضر **قبل** تغيير `docs/search_code.py` و`.github/workflows/tests.yml` هو [run #39651908777](https://github.com/mosabosama2030-oss/omarai/actions/runs/39651908777) على `5a2259ef787d4a4553a503276daf399fa6514f3f`: 380 اختبارًا لكل من Python 3.11 و3.12، وRuff، وفحص الفهرس، وبناء الحاوية واختبار API المحمي ناجحة. لا يغطي هذا التشغيل التغييرات التي أضيفت بعده.
- أُضيف إلى أداة البحث خيار `--ref`، مع `OMARAI_GITHUB_REF` والالتقاط الآمن لمرجع SHA المحلي/CI، حتى تشير الروابط إلى النسخة التي تُراجع بدل تثبيتها على `blob/main`. أضيفت اختبارات لهذه السلوكيات، لكن pytest لم يصل إليها في التشغيل الأخير.
- غُيّر CI إلى فحص الفهرس الملتزم مباشرة باستخدام `python docs/generate_index.py --check`. في [run #39652716421](https://github.com/mosabosama2030-oss/omarai/actions/runs/39652716421) نجح Ruff، لكن فحص الفهرس اكتشف ملفات مولدة قديمة في لقطة PR merge قبل تحديثها آليًا؛ لذلك توقفت pytest ولم تُشغّل.
- **حالة تاريخية وقت كتابة هذا المقطع:** بعد تحديث الفهرس، كان تشغيل [#39653239007](https://github.com/mosabosama2030-oss/omarai/actions/runs/39653239007) على رأس bot بحالة `action_required` بلا jobs. لاحقًا نجح [run #39654908040](https://github.com/mosabosama2030-oss/omarai/actions/runs/39654908040) على رأس PR `3fb028...` قبل الدمج؛ #76 أصبح مدمجًا عبر `528a255...`. تفاصيل الحالة الحالية في تقرير ما بعد الدمج.
- لذلك كانت حالة التغييرات الأخيرة للبحث وفحص الفهرس **PARTIAL / NOT YET FULLY TESTED وقت كتابة هذا المقطع**. استُكملت لاحقًا فحوص CI على رأس PR #76 في run #39654908040. انظر الملحق الحالي أعلى الوثيقة وتقرير ما بعد الدمج.
- لا يغيّر ذلك حالة الاختبارات الحية المستقلة: `NOT_RUN/UNKNOWN` ما زالت تنطبق على hosted smoke، وتوافر كل موفري البحث والنموذج، والتقييم الدلالي لـAQ-001–045، ودوام التخزين/الاستعادة على المضيف، واختبار الحمل، وعزل تعدد المستأجرين، والتقرير المستقل الكامل من Grok.
- **السجل المركزي الوحيد لجميع المعرفات ومعايير الإغلاق:** [`OMARAI_REMEDIATION_REGISTER_AR.md`](OMARAI_REMEDIATION_REGISTER_AR.md). لا تكرر بنودًا جديدة هنا دون إضافتها إلى ذلك السجل.

## تصحيح حالة التحقق بعد تشغيل PR #39653079608 — 21 أكتوبر 2026

تم بعد الملاحظة التاريخية أعلاه إكمال بوابة CI على كود/اختبارات/Workflow مرشح الإغلاق: الالتزام `f2f1bb3c87c709383e0a8c18691f46cd3661e61b`، [تشغيل PR #39653079608](https://github.com/mosabosama2030-oss/omarai/actions/runs/39653079608) — 384 اختبارًا ناجحًا على Python 3.11 و384 على Python 3.12، وRuff وفحص الفهرس وبناء الحاوية واختبار API المحمي ناجحة. بعد ذلك تُظهر المقارنة مع رأس PR الذي شوهد `b848f96...` تغييرات وثائق وفهرسة مولّدة فقط، من دون تغيير التطبيق أو الاختبارات أو Workflow. يظل هذا التصحيح خاصًا بالاختبارات الآلية؛ الاستضافة الحقيقية، ومزودو البحث/النماذج الحيون، وتقييم الجودة الدلالي، ودوام التخزين/الاستعادة، والحمل، والتدقيق المستقل تبقى `NOT_RUN/UNKNOWN`. السجل التفصيلي المعتمد: [سجل الإغلاق المركزي](OMARAI_REMEDIATION_REGISTER_AR.md).


## تحديث نهائي بعد دمج PR #76 — 21 أكتوبر 2026

PR #76 مُدمج في `main` عبر `528a2552c0cda809d6c444713466e0e075c13ed9`. CI على رأس PR قبل الدمج [#39654908040](https://github.com/mosabosama2030-oss/omarai/actions/runs/39654908040) نجح: 384 اختبارًا على Python 3.11 و384 على Python 3.12، وRuff والفهرس وبناء الحاوية وAPI smoke ناجحة. **لم يُثبت في هذه المراجعة تشغيل CI على SHA الدمج نفسه**. الاستضافة الحية، وتوافر المزودين، والصحة الدلالية، ودوام SQLite/الاستعادة، والحمل، والاختبار الأحمر المستقل، وقبول Android/RTL تبقى غير محسومة حسب معيار كل منها. المرجع الأحدث: [تقرير التحقق بعد الدمج](OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md).
