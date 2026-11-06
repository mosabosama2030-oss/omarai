# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **035**
- سجلات الأسطر: **800**
- النطاق: SRC-676B69CB6C-L000066 إلى SRC-70795F4B61-L000249
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## وثائق وفهرسة

### FILE-676B69CB6C — [docs/superpowers/plans/2026-11-06-workspace-demand-discovery.md](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-676B69CB6C-L000066](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L66) | 66 | ``"- [x] Add `product_profiles` table with tenant-scoped uniqueness and index."`` | — |
| [SRC-676B69CB6C-L000067](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L67) | 67 | ``"- [x] Add `discovery_runs` table with tenant-scoped profile foreign key and index."`` | — |
| [SRC-676B69CB6C-L000068](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L68) | 68 | `"- [x] Store only bounded public response fields; never model prompts or secrets."` | — |
| [SRC-676B69CB6C-L000069](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L69) | 69 | `"- [x] Save leads only by loading the source from the stored run and verifying its server-side qualification label."` | — |
| [SRC-676B69CB6C-L000070](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L70) | 70 | `"- [x] Run storage tests and existing LeadStore tests."` | — |
| [SRC-676B69CB6C-L000071](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L71) | 71 | `""` | — |
| [SRC-676B69CB6C-L000072](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L72) | 72 | `"### Task 3: Connect structured buyer discovery to WebAgent"` | — |
| [SRC-676B69CB6C-L000073](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L73) | 73 | `""` | — |
| [SRC-676B69CB6C-L000074](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L74) | 74 | `"**Files:**"` | — |
| [SRC-676B69CB6C-L000075](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L75) | 75 | ``"- Modify: `agents/web_agent.py`"`` | — |
| [SRC-676B69CB6C-L000076](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L76) | 76 | ``"- Create/modify: `tests/test_workspace_discovery.py`"`` | — |
| [SRC-676B69CB6C-L000077](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L77) | 77 | `""` | — |
| [SRC-676B69CB6C-L000078](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L78) | 78 | `"**Interfaces:**"` | — |
| [SRC-676B69CB6C-L000079](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L79) | 79 | ``"- Extend `WebAgent.answer(..., buyer_queries: list[str] \| None = None)`."`` | — |
| [SRC-676B69CB6C-L000080](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L80) | 80 | ``"- Extend internal `_answer_with_budget(..., buyer_queries: list[str] \| None = None)`."`` | — |
| [SRC-676B69CB6C-L000081](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L81) | 81 | ``"- Preserve existing callers when `buyer_queries` is omitted."`` | — |
| [SRC-676B69CB6C-L000082](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L82) | 82 | ``"- Add per-instance `allow_optional_providers` control, defaulting to existing behavior for legacy routes."`` | — |
| [SRC-676B69CB6C-L000083](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L83) | 83 | `""` | — |
| [SRC-676B69CB6C-L000084](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L84) | 84 | `"- [x] Force the lead-generation route only when structured buyer queries are supplied by the new discovery endpoint."` | — |
| [SRC-676B69CB6C-L000085](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L85) | 85 | `"- [x] Validate and cap buyer query count/length (1–8 queries, max 500 characters each)."` | — |
| [SRC-676B69CB6C-L000086](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L86) | 86 | ``"- [x] Prefer structured queries over prose-derived `_lead_generation_queries`."`` | — |
| [SRC-676B69CB6C-L000087](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L87) | 87 | `"- [x] Gate DeepSeek, Brave, Tavily, and optional social APIs when the per-instance control is false."` | — |
| [SRC-676B69CB6C-L000088](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L88) | 88 | `"- [x] Keep DDG/Bing/Google News and public no-key social retrieval under existing bounded controls."` | — |
| [SRC-676B69CB6C-L000089](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L89) | 89 | `"- [x] Add tests that structured product/location queries reach the lead-generation path and optional providers are not invoked by default."` | — |
| [SRC-676B69CB6C-L000090](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L90) | 90 | `""` | — |
| [SRC-676B69CB6C-L000091](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L91) | 91 | `"### Task 4: Implement protected API contracts"` | — |
| [SRC-676B69CB6C-L000092](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L92) | 92 | `""` | — |
| [SRC-676B69CB6C-L000093](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L93) | 93 | `"**Files:**"` | — |
| [SRC-676B69CB6C-L000094](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L94) | 94 | ``"- Modify: `api/omarai.py`"`` | — |
| [SRC-676B69CB6C-L000095](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L95) | 95 | ``"- Modify: `tests/test_api.py`"`` | — |
| [SRC-676B69CB6C-L000096](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L96) | 96 | `""` | — |
| [SRC-676B69CB6C-L000097](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L97) | 97 | `"**Interfaces:**"` | — |
| [SRC-676B69CB6C-L000098](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L98) | 98 | ``"- `GET /api/product-profiles`"`` | — |
| [SRC-676B69CB6C-L000099](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L99) | 99 | ``"- `POST /api/product-profiles`"`` | — |
| [SRC-676B69CB6C-L000100](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L100) | 100 | ``"- `GET /api/discoveries`"`` | — |
| [SRC-676B69CB6C-L000101](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L101) | 101 | ``"- `GET /api/discoveries/{run_id}`"`` | — |
| [SRC-676B69CB6C-L000102](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L102) | 102 | ``"- `POST /api/discoveries`"`` | — |
| [SRC-676B69CB6C-L000103](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L103) | 103 | ``"- `POST /api/discoveries/{run_id}/signals/{source_index}/save`"`` | — |
| [SRC-676B69CB6C-L000104](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L104) | 104 | `""` | — |
| [SRC-676B69CB6C-L000105](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L105) | 105 | ``"- [x] Validate request JSON arrays and bounded field sizes through `ProductProfile` and `MarketProfile`."`` | — |
| [SRC-676B69CB6C-L000106](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L106) | 106 | ``"- [x] Derive all tenant scope from `self._authenticated_principal`."`` | — |
| [SRC-676B69CB6C-L000107](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L107) | 107 | `"- [x] Require a non-viewer role to create profiles or run discovery."` | — |
| [SRC-676B69CB6C-L000108](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L108) | 108 | ``"- [x] Require owner role plus explicit `allow_optional_providers=true` to enable optional providers."`` | — |
| [SRC-676B69CB6C-L000109](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L109) | 109 | ``"- [x] Build a product-anchored prompt and queries through `build_buyer_queries`."`` | — |
| [SRC-676B69CB6C-L000110](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L110) | 110 | `"- [x] Persist the bounded discovery response and return its run ID."` | — |
| [SRC-676B69CB6C-L000111](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L111) | 111 | `"- [x] Return 404 for run/profile IDs outside the current tenant."` | — |
| [SRC-676B69CB6C-L000112](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L112) | 112 | ``"- [x] Route save requests through `LeadStore.save_discovery_signal`; never trust browser-provided source qualification."`` | — |
| [SRC-676B69CB6C-L000113](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L113) | 113 | `"- [x] Run API integration/security tests."` | — |
| [SRC-676B69CB6C-L000114](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L114) | 114 | `""` | — |
| [SRC-676B69CB6C-L000115](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L115) | 115 | `"### Task 5: Connect the RTL workspace"` | — |
| [SRC-676B69CB6C-L000116](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L116) | 116 | `""` | — |
| [SRC-676B69CB6C-L000117](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L117) | 117 | `"**Files:**"` | — |
| [SRC-676B69CB6C-L000118](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L118) | 118 | ``"- Modify: `web/workspace.html`"`` | — |
| [SRC-676B69CB6C-L000119](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L119) | 119 | ``"- Modify: `tests/test_dashboard_security.py`"`` | — |
| [SRC-676B69CB6C-L000120](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L120) | 120 | ``"- Modify: `tests/test_api.py` (if static-route contract coverage is located here)"`` | — |
| [SRC-676B69CB6C-L000121](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L121) | 121 | `""` | — |
| [SRC-676B69CB6C-L000122](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L122) | 122 | `"**Interfaces:**"` | — |
| [SRC-676B69CB6C-L000123](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L123) | 123 | ``"- Activate `offer` (Product Profile) and `campaign` (Demand Discovery) only."`` | — |
| [SRC-676B69CB6C-L000124](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L124) | 124 | `"- Read product profiles and discovery runs from their authenticated APIs."` | — |
| [SRC-676B69CB6C-L000125](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L125) | 125 | `"- Save selected qualified signals using the stored discovery run ID and source index."` | — |
| [SRC-676B69CB6C-L000126](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L126) | 126 | `""` | — |
| [SRC-676B69CB6C-L000127](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L127) | 127 | `"- [x] Add product profile editor with aliases, use cases, problems solved, locations, industries, customer types, decision roles, and exclusions."` | — |
| [SRC-676B69CB6C-L000128](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L128) | 128 | `"- [x] Add discovery screen to choose a saved profile, run search, show prior run history, and inspect evidence."` | — |
| [SRC-676B69CB6C-L000129](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L129) | 129 | `"- [x] Display qualified buyer signals separately from related-but-unqualified results."` | — |
| [SRC-676B69CB6C-L000130](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L130) | 130 | `"- [x] Show evidence phrase, evidence basis (snippet/page text/title), source link, and publication-date unknown states."` | — |
| [SRC-676B69CB6C-L000131](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L131) | 131 | `"- [x] Add explicit unchecked opt-in for optional providers; owner-only on the server with cost/quota disclosure."` | — |
| [SRC-676B69CB6C-L000132](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L132) | 132 | `"- [x] Add save action only for server-qualified public demand signals; then refresh leads and pipeline."` | — |
| [SRC-676B69CB6C-L000133](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L133) | 133 | ``"- [x] Fix the placeholder's general research navigation to `/agent`."`` | — |
| [SRC-676B69CB6C-L000134](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L134) | 134 | `"- [x] Keep all other unimplemented modules visibly unavailable."` | — |
| [SRC-676B69CB6C-L000135](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L135) | 135 | `"- [x] Run workspace static/security tests."` | — |
| [SRC-676B69CB6C-L000136](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L136) | 136 | `""` | — |
| [SRC-676B69CB6C-L000137](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L137) | 137 | `"### Task 6: Documentation, CI, review, and handoff"` | — |
| [SRC-676B69CB6C-L000138](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L138) | 138 | `""` | — |
| [SRC-676B69CB6C-L000139](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L139) | 139 | `"**Files:**"` | — |
| [SRC-676B69CB6C-L000140](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L140) | 140 | ``"- Modify: `docs/IMPLEMENTATION_SCOPE.md`"`` | — |
| [SRC-676B69CB6C-L000141](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L141) | 141 | ``"- Modify: `README.md` only if current product capabilities description needs updating."`` | — |
| [SRC-676B69CB6C-L000142](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L142) | 142 | ``"- Modify: `docs/OMARAI_REQUIREMENTS_REGISTER.md` for material requirement status/evidence, if exact owners can be identified without rewriting the historical baseline."`` | — |
| [SRC-676B69CB6C-L000143](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L143) | 143 | `""` | — |
| [SRC-676B69CB6C-L000144](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L144) | 144 | `"- [x] Verify full pytest, Ruff on Python 3.11/3.12, Docker build, public-startup credential gate, and protected API smoke through GitHub Actions."` | — |
| [SRC-676B69CB6C-L000145](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L145) | 145 | `"- [x] Inspect the 11-file PR diff and scan it for common secret/token patterns; no matches or generated-index changes were found."` | — |
| [SRC-676B69CB6C-L000146](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L146) | 146 | `"- [x] Record live provider tests, post-deploy hosted acceptance, browser E2E, and persistence on SnapDeploy as NOT_RUN/UNKNOWN."` | — |
| [SRC-676B69CB6C-L000147](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L147) | 147 | ``"- [x] Open PR #155 against `main`; leave merge and SnapDeploy deployment to the Human Director."`` | — |
| [SRC-676B69CB6C-L000148](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L148) | 148 | `""` | — |
| [SRC-676B69CB6C-L000149](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L149) | 149 | `"## Expected delivery boundary"` | — |
| [SRC-676B69CB6C-L000150](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L150) | 150 | `""` | — |
| [SRC-676B69CB6C-L000151](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L151) | 151 | `"This plan enables a first real vertical slice: saved product/market profile → buyer-intent search → persisted evidence results → human-reviewed qualified signal → existing leads pipeline. It does **not** claim that company profiles, market analytics, scheduled monitoring, outbound messaging, audit center, or the remaining disabled modules are complete."` | — |
| [SRC-676B69CB6C-L000152](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L152) | 152 | `""` | — |
| [SRC-676B69CB6C-L000153](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L153) | 153 | `""` | — |
| [SRC-676B69CB6C-L000154](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L154) | 154 | `"## Final execution and verification note"` | — |
| [SRC-676B69CB6C-L000155](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L155) | 155 | `""` | — |
| [SRC-676B69CB6C-L000156](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L156) | 156 | ``"- Final code head (before the documentation-only evidence refresh): `1f30370a0808d9ac52b75f630544c1041d5d5fca`."`` | — |
| [SRC-676B69CB6C-L000157](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L157) | 157 | ``"- TDD regression was observed: run [42190588227](https://github.com/mosabosama2030-oss/omarai/actions/runs/42190588227) reported **866 passed, 1 failed**; the only failure was the new assertion that bootstrap must use `Promise.allSettled`."`` | — |
| [SRC-676B69CB6C-L000158](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L158) | 158 | ``"- Implemented the fix in `web/workspace.html`: verify the session separately, load three data resources with `Promise.allSettled`, reset failed resource state to avoid stale data, preserve the authenticated workspace on non-auth data failures, and surface a partial-data warning. A 401 still reopens the login gate."`` | — |
| [SRC-676B69CB6C-L000159](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L159) | 159 | ``"- Successful CI [42190782142](https://github.com/mosabosama2030-oss/omarai/actions/runs/42190782142) on `1f30370a0808d9ac52b75f630544c1041d5d5fca`: **867 passed on Python 3.11 (45.17s)**, **867 passed on Python 3.12 (43.61s)**, Ruff passed on both, generated-index checks passed, Docker build passed, public-container credential gate passed, and protected API smoke passed."`` | — |
| [SRC-676B69CB6C-L000160](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L160) | 160 | `"- No local pytest command, live search/model call, paid provider usage, SnapDeploy deployment, browser E2E, or hosted acceptance was run."` | — |
| [SRC-676B69CB6C-L000161](../superpowers/plans/2026-11-06-workspace-demand-discovery.md#L161) | 161 | `"- PR: [#155 — feat(workspace): connect product profiles and buyer-intent discovery](https://github.com/mosabosama2030-oss/omarai/pull/155). Open for Human Director review; not merged."` | — |
## وثائق وفهرسة

### FILE-8524B08F5D — [docs/superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-8524B08F5D-L000001](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L1) | 1 | `"# تصميم خط المعالجة الهجين الموحد للبحث والفهم"` | — |
| [SRC-8524B08F5D-L000002](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L2) | 2 | `""` | — |
| [SRC-8524B08F5D-L000003](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L3) | 3 | `"**التاريخ:** 2026-10-30  "` | — |
| [SRC-8524B08F5D-L000004](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L4) | 4 | `"**الحالة:** تصميم تنفيذ ضمن فرع مراجعة؛ لا دمج ولا نشر."` | — |
| [SRC-8524B08F5D-L000005](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L5) | 5 | `""` | — |
| [SRC-8524B08F5D-L000006](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L6) | 6 | `"## الهدف"` | — |
| [SRC-8524B08F5D-L000007](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L7) | 7 | `"ربط فهم السؤال والنية والسياق وتفكيك المحاور وتخطيط الاستعلامات ومطابقة المصادر وتغطية الأدلة في مسار واحد قابل للتفسير والاختبار، مع إبقاء القرار النهائي حول صحة الادعاءات في طبقة التحقق الحالية."` | — |
| [SRC-8524B08F5D-L000008](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L8) | 8 | `""` | — |
| [SRC-8524B08F5D-L000009](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L9) | 9 | `"## الحالة الحالية المثبتة"` | — |
| [SRC-8524B08F5D-L000010](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L10) | 10 | ``"- `intent_router.py` يحل توجيه النية والمتابعات."`` | — |
| [SRC-8524B08F5D-L000011](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L11) | 11 | ``"- `task_understanding.py` ينتج TaskSpec ومصفوفة استراتيجيات البحث."`` | — |
| [SRC-8524B08F5D-L000012](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L12) | 12 | ``"- `aspect_planning.py` يستخرج المحاور ويبني سجل مرشحات لفظية للأدلة."`` | — |
| [SRC-8524B08F5D-L000013](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L13) | 13 | ``"- `research.py` يبني الخطط الاحتياطية ويصنف/يرتب نتائج البحث."`` | — |
| [SRC-8524B08F5D-L000014](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L14) | 14 | ``"- `web_agent.py` يستدعي هذه الوحدات بصورة متفرقة ثم يجري فحوص صلة وتغطية أخرى. المطابقة اللفظية ليست تحققًا دلاليًا ولا إثباتًا لصحة الادعاء."`` | — |
| [SRC-8524B08F5D-L000015](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L15) | 15 | `""` | — |
| [SRC-8524B08F5D-L000016](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L16) | 16 | `"## القرار المعماري"` | — |
| [SRC-8524B08F5D-L000017](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L17) | 17 | ``"إضافة وحدة تنسيق صغيرة `agents/research_pipeline.py` تستدعي الوحدات الحالية ولا تستبدلها:"`` | — |
| [SRC-8524B08F5D-L000018](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L18) | 18 | `"1. **Context:** حل المتابعة إلى موضوع حديث واضح، دون إحياء موضوع قديم بعد انتهاء السياق."` | — |
| [SRC-8524B08F5D-L000019](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L19) | 19 | `"2. **Intent:** استخدام قرار المسار القادم من WebAgent؛ وعند غيابه فقط، استخدام الموجّه الحتمي."` | — |
| [SRC-8524B08F5D-L000020](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L20) | 20 | `"3. **Task understanding:** بناء TaskSpec للهدف والقيود والمخرجات وسياسات الأدلة."` | — |
| [SRC-8524B08F5D-L000021](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L21) | 21 | `"4. **Aspect decomposition:** دمج المحاور الصريحة من TaskSpec مع استخراج مستقل ثانٍ، وإزالة التكرار ضمن سقف 8 محاور."` | — |
| [SRC-8524B08F5D-L000022](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L22) | 22 | `"5. **Query planning:** بناء مصفوفة استعلامات محدودة بحد 8، مع الحفاظ على موضوع السؤال وأولوية المحاور."` | — |
| [SRC-8524B08F5D-L000023](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L23) | 23 | `"6. **Evidence matching:** إنشاء سجل مرشحات لكل محور من المصادر المسترجعة، مع توضيح أن التطابق اللفظي مرشح فقط."` | — |
| [SRC-8524B08F5D-L000024](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L24) | 24 | ``"7. **Semantic stage:** واجهة اختيارية محدودة لمقيّم دلالي يحقنه المستدعي عند توافر مقيّم آمن؛ لا ينشئ هذا التغيير استدعاء نموذج إضافيًا ولا يستخدم خدمة مدفوعة. عند غيابه يسجل `not_configured` ولا يرفع المرشحات اللفظية إلى تحقق دلالي."`` | — |
| [SRC-8524B08F5D-L000025](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L25) | 25 | `"8. **Verification:** إبقاء حواجز المصادر والتحقق من الادعاءات والاستشهادات الموجودة كما هي؛ لا تغطية ولا تشابه كلمات يثبتان صحة المعلومة."` | — |
| [SRC-8524B08F5D-L000026](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L26) | 26 | `""` | — |
| [SRC-8524B08F5D-L000027](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L27) | 27 | `"## التكامل"` | — |
| [SRC-8524B08F5D-L000028](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L28) | 28 | ``"- `research.py::_attach_task_understanding` يستخدم المنسق الموحد بدل بناء TaskSpec والمصفوفة كلًا على حدة."`` | — |
| [SRC-8524B08F5D-L000029](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L29) | 29 | ``"- `web_agent.py` يستخدم المنسق نفسه قبل تنفيذ الاستعلامات، ثم يضيف سجل الأدلة بعد جمع المصادر إلى تقرير البحث."`` | — |
| [SRC-8524B08F5D-L000030](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L30) | 30 | `"- لا تغيير في عقود API أو قاعدة البيانات أو الموصلات أو إعدادات الاستضافة."` | — |
| [SRC-8524B08F5D-L000031](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L31) | 31 | `""` | — |
| [SRC-8524B08F5D-L000032](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L32) | 32 | `"## الحدود"` | — |
| [SRC-8524B08F5D-L000033](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L33) | 33 | `"- لا ذاكرة دلالية دائمة، ولا embeddings أو مكتبات جديدة."` | — |
| [SRC-8524B08F5D-L000034](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L34) | 34 | `"- لا استدعاء LLM إضافي ولا استهلاك مدفوع."` | — |
| [SRC-8524B08F5D-L000035](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L35) | 35 | `"- المقيّم الدلالي الاختياري لا يثبت صحة الادعاءات؛ لا يمكنه إلا ترتيب مرشحات الصلة."` | — |
| [SRC-8524B08F5D-L000036](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L36) | 36 | `"- لا تخفيف من SSRF أو صلة البحث أو حدود الوقت والميزانية أو حواجز المصادر."` | — |
| [SRC-8524B08F5D-L000037](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L37) | 37 | `"- لا دمج PR أو نشر."` | — |
| [SRC-8524B08F5D-L000038](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L38) | 38 | `""` | — |
| [SRC-8524B08F5D-L000039](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L39) | 39 | `"## النجاح"` | — |
| [SRC-8524B08F5D-L000040](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L40) | 40 | `"اختبارات وحدات وانحدار تثبت: الحفاظ على سياق المتابعة الصحيح، طلب التوضيح عند غياب المرجع، استخراج المحاور، حد الاستعلامات، ربط كل محور بسجل مرشحاته، التمييز بين المرشح اللفظي والتحقق الدلالي، وسلامة الرجوع عند فشل المقيّم الاختياري."` | — |
| [SRC-8524B08F5D-L000041](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L41) | 41 | `""` | — |
| [SRC-8524B08F5D-L000042](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L42) | 42 | `""` | — |
| [SRC-8524B08F5D-L000043](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L43) | 43 | `"## نتيجة التنفيذ وحدود المرحلة الحالية"` | — |
| [SRC-8524B08F5D-L000044](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L44) | 44 | `"- تحقق ربط المراحل الحتمية وتكاملها مع مخرجات مخطط البحث اللغوي الموجود."` | — |
| [SRC-8524B08F5D-L000045](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L45) | 45 | `"- المطابقة اللفظية تنتج مرشحات لكل محور، وتبقى منفصلة عن تحقق الادعاء."` | — |
| [SRC-8524B08F5D-L000046](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L46) | 46 | ``"- مقيّم الصلة الدلالية الاختياري له واجهة bounded واختبارات رفض الدرجات غير الصالحة والتدهور عند الاستثناء؛ لكنه غير موصول افتراضيًا بمسار WebAgent، لذلك الحالة التشغيلية المعلنة هي `not_configured`."`` | — |
| [SRC-8524B08F5D-L000047](../superpowers/specs/2026-10-30-unified-hybrid-research-pipeline-design.md#L47) | 47 | ``"- لا يُسمح بتحويل حالة `not_configured` إلى `evaluated` إلا بعد توفير مقيّم دلالي فعلي مضبوط بميزانية/مهلة واختبارات قبول مستقلة."`` | — |
## وثائق وفهرسة

### FILE-BFCEEA0374 — [docs/superpowers/specs/2026-11-06-workspace-demand-discovery-design.md](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-BFCEEA0374-L000001](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L1) | 1 | `"# تصميم ربط ملف المنتج واكتشاف الطلب بمساحة عمل Omarai"` | — |
| [SRC-BFCEEA0374-L000002](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L2) | 2 | `""` | — |
| [SRC-BFCEEA0374-L000003](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L3) | 3 | `"**التاريخ:** 6 نوفمبر 2026  "` | — |
| [SRC-BFCEEA0374-L000004](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L4) | 4 | ``"**المرجع:** `main` عند `a297abd271d48f459effad083a9f424a1499cd39`  "`` | — |
| [SRC-BFCEEA0374-L000005](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L5) | 5 | `"**الحالة:** تصميم تنفيذ ضمن فرع مستقل؛ لا يغيّر الإنتاج ولا يدمج تلقائيًا."` | — |
| [SRC-BFCEEA0374-L000006](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L6) | 6 | `""` | — |
| [SRC-BFCEEA0374-L000007](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L7) | 7 | `"## المشكلة"` | — |
| [SRC-BFCEEA0374-L000008](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L8) | 8 | `""` | — |
| [SRC-BFCEEA0374-L000009](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L9) | 9 | ``"مساحة العمل تعرض أربعة أقسام فقط متصلة بواجهات فعلية. نموذج الإشارة الحالي يدعم الإدخال اليدوي والتحليل القواعدي، لكنه لا يشغل بحث المشترين. محرك البحث الحالي يملك بالفعل مسار `LEAD_GENERATION`، ونماذج `ProductProfile` و`MarketProfile` وبناء استعلامات مشتري مرتبطة بالمنتج، لكن الواجهة لا تمرر هذه البيانات إليه ولا تحفظ نتائج التشغيل كسجل مستقل."`` | — |
| [SRC-BFCEEA0374-L000010](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L10) | 10 | `""` | — |
| [SRC-BFCEEA0374-L000011](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L11) | 11 | `"## الهدف"` | — |
| [SRC-BFCEEA0374-L000012](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L12) | 12 | `""` | — |
| [SRC-BFCEEA0374-L000013](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L13) | 13 | `"إنشاء مسار عربي RTL قابل للاستخدام من داخل الواجهة:"` | — |
| [SRC-BFCEEA0374-L000014](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L14) | 14 | `"1. حفظ ملف منتج/خدمة وسوق مستهدف تحت المستأجر الحالي."` | — |
| [SRC-BFCEEA0374-L000015](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L15) | 15 | `"2. تشغيل بحث اكتشاف مرتبط بالملف باستخدام محرك البحث وإشارات نية الشراء الموجودة."` | — |
| [SRC-BFCEEA0374-L000016](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L16) | 16 | `"3. حفظ سجل تشغيل ونتائجه العامة القابلة للمراجعة تحت المستأجر نفسه."` | — |
| [SRC-BFCEEA0374-L000017](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L17) | 17 | ``"4. فصل الإشارات المصنفة `public_demand_signal` عن النتائج المرتبطة بالموضوع فقط."`` | — |
| [SRC-BFCEEA0374-L000018](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L18) | 18 | `"5. السماح بحفظ الإشارة المؤهلة إلى صندوق الإشارات بعد مراجعة المستخدم، مع الاحتفاظ بمصدرها وعبارة الدليل ونوعه في الملاحظة."` | — |
| [SRC-BFCEEA0374-L000019](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L19) | 19 | `"6. إظهار الاستعلامات، حالة التنفيذ، ومحدودية الدليل بصدق."` | — |
| [SRC-BFCEEA0374-L000020](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L20) | 20 | `""` | — |
| [SRC-BFCEEA0374-L000021](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L21) | 21 | `"## البدائل"` | — |
| [SRC-BFCEEA0374-L000022](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L22) | 22 | `""` | — |
| [SRC-BFCEEA0374-L000023](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L23) | 23 | ``"- **A — ربط الواجهة مباشرة بـ`/api/agent`:** أسرع، لكنه يرسل سؤالًا حرًا ولا يفرض عقد ProductProfile/MarketProfile أو سياسة حفظ نتائج مبيعات واضحة."`` | — |
| [SRC-BFCEEA0374-L000024](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L24) | 24 | `"- **B — تكرار محرك بحث للمبيعات:** يمنح تخصيصًا ظاهريًا لكنه يكرر البحث والتصفية والميزانيات وحواجز URL، ويخلق اختلافًا في السلوك."` | — |
| [SRC-BFCEEA0374-L000025](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L25) | 25 | `"- **C — endpoint تجاري منظم يعيد استخدام WebAgent وsales_domain:** يفرض ملفًا منظمًا، ويعيد استخدام محرك البحث وتصنيف نية الشراء، مع تخزين tenant-scoped للملفات وعمليات الاكتشاف. **هذا هو الاختيار** لأنه يحقق مسارًا متصلًا دون محرك ثانٍ."` | — |
| [SRC-BFCEEA0374-L000026](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L26) | 26 | `""` | — |
| [SRC-BFCEEA0374-L000027](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L27) | 27 | `"## النطاق"` | — |
| [SRC-BFCEEA0374-L000028](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L28) | 28 | `""` | — |
| [SRC-BFCEEA0374-L000029](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L29) | 29 | `"- إضافة تخزين tenant-scoped لملفات المنتج/السوق وسجلات عمليات الاكتشاف."` | — |
| [SRC-BFCEEA0374-L000030](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L30) | 30 | `"- إضافة عقود API محمية لقراءة/حفظ الملفات، تشغيل الاكتشاف، قراءة سجل التشغيل، وحفظ إشارة من تشغيل محفوظ."` | — |
| [SRC-BFCEEA0374-L000031](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L31) | 31 | ``"- تمرير استعلامات `build_buyer_queries` مباشرة إلى WebAgent بدل إعادة استخراج المنتج من نص حر."`` | — |
| [SRC-BFCEEA0374-L000032](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L32) | 32 | `"- إبقاء الموصلات الاختيارية التي قد تستهلك حصصًا/تكلفة معطلة افتراضيًا في مسار الاكتشاف؛ لا يسمح بتفعيلها إلا بطلب صريح من المالك في نفس التشغيل."` | — |
| [SRC-BFCEEA0374-L000033](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L33) | 33 | `"- تفعيل شاشتي ملف المنتج والاكتشاف فقط بعد ربطهما بعقود حقيقية."` | — |
| [SRC-BFCEEA0374-L000034](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L34) | 34 | `"- إبقاء الوحدات الأخرى غير المنفذة معطلة."` | — |
| [SRC-BFCEEA0374-L000035](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L35) | 35 | `"- حفظ الإشارة المؤهلة بعد فعل صريح من المستخدم فقط؛ لا تواصل آلي."` | — |
| [SRC-BFCEEA0374-L000036](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L36) | 36 | `""` | — |
| [SRC-BFCEEA0374-L000037](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L37) | 37 | `"## خارج النطاق"` | — |
| [SRC-BFCEEA0374-L000038](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L38) | 38 | `""` | — |
| [SRC-BFCEEA0374-L000039](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L39) | 39 | `"- إنشاء CRM كامل أو ملفات شركات أو حملات مجدولة أو تنبيهات أو مهام خلفية."` | — |
| [SRC-BFCEEA0374-L000040](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L40) | 40 | `"- الادعاء بأن كل المصادر والمنصات متاحة أو أن نتائج البحث تمثل كل السوق."` | — |
| [SRC-BFCEEA0374-L000041](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L41) | 41 | `"- بناء محرك بحث جديد أو تفعيل Firecrawl؛ PR #153 منفصل ومفتوح على خط الأساس الحالي."` | — |
| [SRC-BFCEEA0374-L000042](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L42) | 42 | `"- إرسال رسائل أو جمع بيانات اتصال خاصة."` | — |
| [SRC-BFCEEA0374-L000043](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L43) | 43 | `"- تغيير أسرار SnapDeploy أو مفاتيح المزودين أو النشر أو الدمج."` | — |
| [SRC-BFCEEA0374-L000044](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L44) | 44 | `""` | — |
| [SRC-BFCEEA0374-L000045](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L45) | 45 | `"## البيانات والأمان"` | — |
| [SRC-BFCEEA0374-L000046](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L46) | 46 | `""` | — |
| [SRC-BFCEEA0374-L000047](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L47) | 47 | ``"- كل ملف منتج وكل تشغيل وكل مصدر محفوظ يقيّد بـ`tenant_id` المستمد من principal موثوق على الخادم، وليس من body أو query."`` | — |
| [SRC-BFCEEA0374-L000048](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L48) | 48 | `"- يجب أن تشمل المفاتيح والقيود الفريدة نطاق المستأجر."` | — |
| [SRC-BFCEEA0374-L000049](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L49) | 49 | ``"- استرجاع الإشارة للحفظ يكون بواسطة `run_id + source_index + tenant_id` من سجل محفوظ في الخادم؛ لا يثق الخادم في تصنيف يرسله المتصفح."`` | — |
| [SRC-BFCEEA0374-L000050](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L50) | 50 | ``"- لا تُحفظ نتيجة غير مصنفة `public_demand_signal` كإشارة شراء من إجراء الحفظ الخاص بالتشغيل."`` | — |
| [SRC-BFCEEA0374-L000051](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L51) | 51 | `"- لا يعرض النظام هوية الكاتب أو قناة اتصال إلا إذا كانت موجودة ومتحققًا منها في المصدر. لا تستنتجها."` | — |
| [SRC-BFCEEA0374-L000052](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L52) | 52 | `"- النص والمقتطفات والصفحات بيانات غير موثوقة."` | — |
| [SRC-BFCEEA0374-L000053](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L53) | 53 | `"- لا تُشغّل DeepSeek/Brave/Tavily أو موصلات اختيارية ذات حصص/تكلفة تلقائيًا في مسار الاكتشاف. التفعيل صريح ومن المالك فقط."` | — |
| [SRC-BFCEEA0374-L000054](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L54) | 54 | `"- لا تُعرض درجة التحليل القواعدي الحالية كاحتمال شراء."` | — |
| [SRC-BFCEEA0374-L000055](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L55) | 55 | `""` | — |
| [SRC-BFCEEA0374-L000056](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L56) | 56 | `"## معيار القبول"` | — |
| [SRC-BFCEEA0374-L000057](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L57) | 57 | `""` | — |
| [SRC-BFCEEA0374-L000058](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L58) | 58 | `"- يمكن حفظ ملفين بمنتجين مختلفين لنفس المستأجر، واسترجاعهما؛ ولا يستطيع مستأجر آخر قراءتهما."` | — |
| [SRC-BFCEEA0374-L000059](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L59) | 59 | `"- يرفض الخادم viewer من الكتابة أو تشغيل الاكتشاف."` | — |
| [SRC-BFCEEA0374-L000060](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L60) | 60 | `"- يولد البحث استعلامات من أسماء/مرادفات المنتج والموقع، دون تسرب عبارات عقارية إلى المنتجات غير العقارية."` | — |
| [SRC-BFCEEA0374-L000061](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L61) | 61 | `"- يستدعي endpoint محرك WebAgent الحالي بعقد buyer queries منظمة، لا بمحرك ثانٍ."` | — |
| [SRC-BFCEEA0374-L000062](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L62) | 62 | `"- لا تُستدعى الموصلات الاختيارية عند ترك خيار الاستخدام الاختياري مغلقًا."` | — |
| [SRC-BFCEEA0374-L000063](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L63) | 63 | `"- يحفظ سجل تشغيل مع مصادره وحالاتها تحت المستأجر."` | — |
| [SRC-BFCEEA0374-L000064](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L64) | 64 | ``"- لا يقبل endpoint الحفظ مصدرًا غير مصنف `public_demand_signal`، ولا يقبل معرف تشغيل تابعًا لمستأجر آخر."`` | — |
| [SRC-BFCEEA0374-L000065](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L65) | 65 | `"- الواجهة تعرض الدليل والمصدر ونوع النص/أساسه والحدود، وتسمح بحفظ الإشارة المؤهلة يدويًا فقط."` | — |
| [SRC-BFCEEA0374-L000066](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L66) | 66 | `"- جميع الاختبارات الآلية وCI ذات الصلة ناجحة؛ قبول الاستضافة بعد النشر يبقى منفصلًا ويتطلب إجراء Human Director."` | — |
| [SRC-BFCEEA0374-L000067](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L67) | 67 | `""` | — |
| [SRC-BFCEEA0374-L000068](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L68) | 68 | `"## القرارات التنفيذية"` | — |
| [SRC-BFCEEA0374-L000069](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L69) | 69 | `""` | — |
| [SRC-BFCEEA0374-L000070](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L70) | 70 | ``"- إعادة استخدام `agents.sales_domain` و`WebAgent` و`LeadStore` بدل إنشاء محرك مستقل."`` | — |
| [SRC-BFCEEA0374-L000071](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L71) | 71 | ``"- تخزين ملفات المنتج وتشغيلات الاكتشاف في SQLite مع migration آمن عبر `CREATE TABLE IF NOT EXISTS` وفهارس tenant-scoped."`` | — |
| [SRC-BFCEEA0374-L000072](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L72) | 72 | `"- عدم تغيير أي مفتاح أو إعداد استضافة."` | — |
| [SRC-BFCEEA0374-L000073](../superpowers/specs/2026-11-06-workspace-demand-discovery-design.md#L73) | 73 | `"- لا دمج ولا نشر ضمن هذا العمل."` | — |
## وثائق وفهرسة

### FILE-6B9B9ABE27 — [docs/ui-directions/README.md](../ui-directions/README.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-6B9B9ABE27-L000001](../ui-directions/README.md#L1) | 1 | `"# Omarai — Three Glass UI Directions"` | — |
| [SRC-6B9B9ABE27-L000002](../ui-directions/README.md#L2) | 2 | `""` | — |
| [SRC-6B9B9ABE27-L000003](../ui-directions/README.md#L3) | 3 | `"**Status:** Visual proposals for Human Director selection only. No direction is implemented or connected to production APIs."` | — |
| [SRC-6B9B9ABE27-L000004](../ui-directions/README.md#L4) | 4 | `""` | — |
| [SRC-6B9B9ABE27-L000005](../ui-directions/README.md#L5) | 5 | `"Design project: https://design.agent-native.com/design/sGSw7-l6baKesddSGTdvl?editorView=overview"` | — |
| [SRC-6B9B9ABE27-L000006](../ui-directions/README.md#L6) | 6 | `""` | — |
| [SRC-6B9B9ABE27-L000007](../ui-directions/README.md#L7) | 7 | `"## Option 01 — Aurora Glass"` | — |
| [SRC-6B9B9ABE27-L000008](../ui-directions/README.md#L8) | 8 | `"- Expressive frosted surfaces with teal/cyan/violet ambient glow."` | — |
| [SRC-6B9B9ABE27-L000009](../ui-directions/README.md#L9) | 9 | `"- Futuristic, colorful Android-inspired atmosphere with restrained layering."` | — |
| [SRC-6B9B9ABE27-L000010](../ui-directions/README.md#L10) | 10 | `"- Best when the product should feel distinctly modern and visually memorable."` | — |
| [SRC-6B9B9ABE27-L000011](../ui-directions/README.md#L11) | 11 | `"- Preview: [variant-01-aurora-glass.html](variant-01-aurora-glass.html)"` | — |
| [SRC-6B9B9ABE27-L000012](../ui-directions/README.md#L12) | 12 | `""` | — |
| [SRC-6B9B9ABE27-L000013](../ui-directions/README.md#L13) | 13 | `"## Option 02 — Precision Glass"` | — |
| [SRC-6B9B9ABE27-L000014](../ui-directions/README.md#L14) | 14 | `"- Restrained graphite glass, generous spacing, soft blue accent, evidence-first hierarchy."` | — |
| [SRC-6B9B9ABE27-L000015](../ui-directions/README.md#L15) | 15 | `"- Apple-inspired calm spatial depth without copying platform UI."` | — |
| [SRC-6B9B9ABE27-L000016](../ui-directions/README.md#L16) | 16 | `"- Best for sustained daily use, readability, and professional trust."` | — |
| [SRC-6B9B9ABE27-L000017](../ui-directions/README.md#L17) | 17 | `"- Preview: [variant-02-precision-glass.html](variant-02-precision-glass.html)"` | — |
| [SRC-6B9B9ABE27-L000018](../ui-directions/README.md#L18) | 18 | `""` | — |
| [SRC-6B9B9ABE27-L000019](../ui-directions/README.md#L19) | 19 | `"## Option 03 — Neon Command"` | — |
| [SRC-6B9B9ABE27-L000020](../ui-directions/README.md#L20) | 20 | `"- Compact command-center layout with navy surfaces and cyan/indigo luminous edges."` | — |
| [SRC-6B9B9ABE27-L000021](../ui-directions/README.md#L21) | 21 | `"- Strong operational hierarchy and denser information display."` | — |
| [SRC-6B9B9ABE27-L000022](../ui-directions/README.md#L22) | 22 | `"- Best for power users monitoring multiple market signals and qualification stages."` | — |
| [SRC-6B9B9ABE27-L000023](../ui-directions/README.md#L23) | 23 | `"- Preview: [variant-03-neon-command.html](variant-03-neon-command.html)"` | — |
| [SRC-6B9B9ABE27-L000024](../ui-directions/README.md#L24) | 24 | `""` | — |
| [SRC-6B9B9ABE27-L000025](../ui-directions/README.md#L25) | 25 | `"## Shared design requirements"` | — |
| [SRC-6B9B9ABE27-L000026](../ui-directions/README.md#L26) | 26 | `"- Arabic-first RTL; Noto Sans Arabic / IBM Plex Arabic system fallback."` | — |
| [SRC-6B9B9ABE27-L000027](../ui-directions/README.md#L27) | 27 | `"- Responsive desktop and mobile layouts with CSS breakpoints."` | — |
| [SRC-6B9B9ABE27-L000028](../ui-directions/README.md#L28) | 28 | `"- Evidence source/date and human-review status remain visible."` | — |
| [SRC-6B9B9ABE27-L000029](../ui-directions/README.md#L29) | 29 | `"- Demo records are illustrative and explicitly labeled."` | — |
| [SRC-6B9B9ABE27-L000030](../ui-directions/README.md#L30) | 30 | `"- No fabricated purchase probability, contact details, or real-world claims."` | — |
| [SRC-6B9B9ABE27-L000031](../ui-directions/README.md#L31) | 31 | `"- Static prototypes only: no production APIs, authentication, or backend behavior."` | — |
| [SRC-6B9B9ABE27-L000032](../ui-directions/README.md#L32) | 32 | `""` | — |
| [SRC-6B9B9ABE27-L000033](../ui-directions/README.md#L33) | 33 | `"## Approval gate"` | — |
| [SRC-6B9B9ABE27-L000034](../ui-directions/README.md#L34) | 34 | `"Human Director selects one direction. Only after selection should the chosen visual direction be refined and implemented against Omarai's existing session/lead API contracts. The other two remain archived proposals. No merge or deployment is authorized by this PR."` | — |
| [SRC-6B9B9ABE27-L000035](../ui-directions/README.md#L35) | 35 | `""` | — |
| [SRC-6B9B9ABE27-L000036](../ui-directions/README.md#L36) | 36 | `"## Human Director decision — 4 November 2026"` | — |
| [SRC-6B9B9ABE27-L000037](../ui-directions/README.md#L37) | 37 | `""` | — |
| [SRC-6B9B9ABE27-L000038](../ui-directions/README.md#L38) | 38 | `"**Selected:** Option 03 — Neon Command. This is the approved visual direction for implementation."` | — |
| [SRC-6B9B9ABE27-L000039](../ui-directions/README.md#L39) | 39 | `""` | — |
| [SRC-6B9B9ABE27-L000040](../ui-directions/README.md#L40) | 40 | `"- Implementation and backend connection are tracked in [PR #151](https://github.com/mosabosama2030-oss/omarai/pull/151)."` | — |
| [SRC-6B9B9ABE27-L000041](../ui-directions/README.md#L41) | 41 | `"- Options 01 and 02 remain reference proposals only."` | — |
| [SRC-6B9B9ABE27-L000042](../ui-directions/README.md#L42) | 42 | `"- This PR contains design previews; it does not implement or deploy the selected interface."` | — |
## وثائق وفهرسة

### FILE-7EB8FCD215 — [docs/ui-directions/variant-01-aurora-glass.html](../ui-directions/variant-01-aurora-glass.html#L1)

- النوع: **HTML**
- نطاق الفهرسة: جرد الملف + معرفات HTML والرموز داخل script/style

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-7EB8FCD215-L000001](../ui-directions/variant-01-aurora-glass.html#L1) | 1 | `"<!doctype html><html lang='ar' dir='rtl' data-agent-native-node-id=\"an-19qch1x\"><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><style>*{box-sizing:border-box}body{margin:0;background:radial-gradient(ellipse at 15% 5%,#173d58 0,transparent 38%),radial-gradient(ellipse at 85% 25%,#30234f 0,transparent 35%),#080e19;color:#e9f3ff;font:15px system-ui,'Noto Sans Arabic',sans-serif}.app{display:grid;grid-template-columns:245px 1fr;min-height:100vh;gap:18px;padding:20px}.side,.panel,.stat{background:linear-gradient(145deg,#ffffff12,#ffffff05);border:1px solid #b9d8ff20;backdrop-filter:blur(22px);border-radius:22px;box-shadow:0 20px 60px #0003}.side{padding:22px}.brand{font-size:25px;font-weight:800;color:#78eadb}.nav{margin-top:34px;display:grid;gap:10px}.nav div{padding:13px;border-radius:12px;color:#a9bdd2}.nav .active{background:#7debd51a;color:#8ff6e2;border:1px solid #8ff6e222}.main{min-width:0}.top{display:flex;justify-content:space-between;align-items:center;gap:12px}.pill{border:1px solid #ffffff20;background:#ffffff0b;padding:10px 15px;border-radius:30px;color:#bcd0e7}.hero{margin:25px 0}.hero h1{font-size:30px;margin:0 0 8px}.muted{color:#94a9c1}.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}.stat{padding:20px}.num{font-size:28px;color:#82efdc;font-weight:750;margin:12px 0}.layout{display:grid;grid-template-columns:1.5fr 1fr;gap:16px;margin-top:16px}.panel{padding:20px}.row{display:flex;justify-content:space-between;gap:12px;padding:15px 0;border-bottom:1px solid #ffffff12}.tag{color:#9af0d9;background:#4bd4b018;padding:6px 10px;border-radius:20px;font-size:12px}.stage{height:8px;background:#ffffff12;border-radius:20px;margin:12px 0}.stage i{display:block;width:62%;height:100%;background:linear-gradient(90deg,#67e7d1,#8c8cff);border-radius:20px}@media(max-width:850px){.app{grid-template-columns:1fr;padding:12px}.side{display:none}.stats{grid-template-columns:repeat(2,1fr)}.layout{grid-template-columns:1fr}.top{flex-wrap:wrap}.hero h1{font-size:24px}}@media(max-width:480px){.stats{gap:8px}.stat,.panel{padding:14px}.num{font-size:23px}.bottom{display:flex;position:sticky;bottom:8px;background:#101c2ce8;border:1px solid #ffffff20;border-radius:18px;padding:12px;justify-content:space-around;margin-top:14px}}</style></head><body data-agent-native-node-id=\"an-jqo3wt\"><div class='app' data-agent-native-node-id=\"an-id3wsl\"><aside class='side' data-agent-native-node-id=\"an-1mtuhlh\"><div class='brand' data-agent-native-node-id=\"an-1kt8xq9\">◈ عُمراي</div><p class='muted' data-agent-native-node-id=\"an-v1xw0d\">ذكاء المبيعات</p><div class='nav' data-agent-native-node-id=\"an-2kobx4\"><div class='active' data-agent-native-node-id=\"an-1463rp0\">◫ نظرة عامة</div><div data-agent-native-node-id=\"an-1d77149\">⌕ إشارات الطلب</div><div data-agent-native-node-id=\"an-1bo0gxl\">◎ مسار التأهيل</div><div data-agent-native-node-id=\"an-17ekjf2\">⌘ استخبارات السوق</div><div data-agent-native-node-id=\"an-1cwuece\">◉ المصادر</div></div></aside><main class='main' data-agent-native-node-id=\"an-s92bpi\"><div class='top' data-agent-native-node-id=\"an-cc9n77\"><span class='pill' data-agent-native-node-id=\"an-1jbfl7j\">⌕ ابحث في الإشارات والشركات</span><span class='pill' data-agent-native-node-id=\"an-1pixy7p\">مساحة العمل · القاهرة</span></div><section class='hero' data-agent-native-node-id=\"an-167w5oj\"><p class='muted' data-agent-native-node-id=\"an-weq0yq\">مساحة الاكتشاف / اليوم</p><h1 data-agent-native-node-id=\"an-yuv4wp\">أهلاً بك في مركز استخبارات المبيعات</h1><p class='muted' data-agent-native-node-id=\"an-1sofdf4\">راجع إشارات الاحتياج، افحص الأدلة، ثم قرر الخطوة التالية.</p></section><div class='stats' data-agent-native-node-id=\"an-5oj080\"><div class='stat' data-agent-native-node-id=\"an-v7letp\">الإشارات المحمّلة<div class='num' data-agent-native-node-id=\"an-14ar0bz\">128</div><span class='muted' data-agent-native-node-id=\"an-g0ywlg\">بيانات توضيحية</span></div><div class='stat' data-agent-native-node-id=\"an-1xnrcua\">تحتاج مراجعة<div class='num' data-agent-native-node-id=\"an-1la7h4l\">24</div><span class='muted' data-agent-native-node-id=\"an-5xvonf\">دليل ينتظر التحقق</span></div><div class='stat' data-agent-native-node-id=\"an-fi81m7\">مؤهلة<div class='num' data-agent-native-node-id=\"an-1vyro0u\">16</div><span class='muted' data-agent-native-node-id=\"an-691w91\">بعد مراجعة بشرية</span></div><div class='stat' data-agent-native-node-id=\"an-dcasvc\">متابعة<div class='num' data-agent-native-node-id=\"an-gx0je3\">9</div><span class='muted' data-agent-native-node-id=\"an-18eyy4r\">إجراء معتمد</span></div></div><div class='layout' data-agent-native-node-id=\"an-o3zzps\"><section class='panel' data-agent-native-node-id=\"an-hrlmec\"><h2 data-agent-native-node-id=\"an-a0ruc7\">إشارات نية الشراء</h2><div class='row' data-agent-native-node-id=\"an-ppfwfb\"><div data-agent-native-node-id=\"an-lfbdow\"><b data-agent-native-node-id=\"an-miv3l8\">طلب توريد تجهيزات مكتبية</b><p class='muted' data-agent-native-node-id=\"an-13dfohj\">مصدر عام · منذ ساعتين</p></div><span class='tag' data-agent-native-node-id=\"an-9o8iae\">يحتاج مراجعة</span></div><div class='row' data-agent-native-node-id=\"an-vbx8l6\"><div data-agent-native-node-id=\"an-vluil2\"><b data-agent-native-node-id=\"an-8gvvpq\">بحث عن مقاول صيانة تكييف</b><p class='muted' data-agent-native-node-id=\"an-17hc0lw\">طلب خدمة منشور · أمس</p></div><span class='tag' data-agent-native-node-id=\"an-1hauho4\">دليل مرفق</span></div><div class='row' data-agent-native-node-id=\"an-1b2uxnn\"><div data-agent-native-node-id=\"an-ux9f9v\"><b data-agent-native-node-id=\"an-1v8ly8q\">احتياج معدات لمشروع جديد</b><p class='muted' data-agent-native-node-id=\"an-1h1ku9q\">إعلان طلب · منذ 3 أيام</p></div><span class='tag' data-agent-native-node-id=\"an-174ll6b\">مراجعة بشرية</span></div></section><section class='panel' data-agent-native-node-id=\"an-o9dfs0\"><h2 data-agent-native-node-id=\"an-1i8fydy\">مسار التأهيل</h2><p class='muted' data-agent-native-node-id=\"an-1ww1ij3\">من الإشارة إلى فرصة قابلة للمتابعة</p><div class='row' data-agent-native-node-id=\"an-1pf4hxb\">جديد <b data-agent-native-node-id=\"an-11rtvkb\">24</b></div><div class='stage' data-agent-native-node-id=\"an-8fp3e2\"><i data-agent-native-node-id=\"an-utv0o8\"></i></div><div class='row' data-agent-native-node-id=\"an-1l2qrh2\">مؤهل <b data-agent-native-node-id=\"an-el3suf\">16</b></div><div class='row' data-agent-native-node-id=\"an-1s3h6yb\">موافقة متابعة <b data-agent-native-node-id=\"an-1ij68k7\">9</b></div><p class='muted' data-agent-native-node-id=\"an-mtq2mz\">لا تمثل الأرقام احتمال شراء.</p></section></div><div class='bottom' style='display:none' data-agent-native-node-id=\"an-tgu348\">نظرة عامة　 إشارات　 متابعة　 المزيد</div></main></div></body></html>"` | — |
## وثائق وفهرسة

### FILE-2A9FC16EBA — [docs/ui-directions/variant-02-precision-glass.html](../ui-directions/variant-02-precision-glass.html#L1)

- النوع: **HTML**
- نطاق الفهرسة: جرد الملف + معرفات HTML والرموز داخل script/style

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-2A9FC16EBA-L000001](../ui-directions/variant-02-precision-glass.html#L1) | 1 | `"<!doctype html><html lang='ar' dir='rtl' data-agent-native-node-id=\"an-19qch1x\"><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><style>*{box-sizing:border-box}body{margin:0;background:linear-gradient(135deg,#11151d,#202630 55%,#10141b);color:#f4f6fa;font:15px system-ui,'Noto Sans Arabic',sans-serif}.app{display:grid;grid-template-columns:230px 1fr;gap:24px;padding:28px;min-height:100vh}.side,.panel,.stat{background:#ffffff09;border:1px solid #ffffff12;border-radius:18px;backdrop-filter:blur(18px)}.side{padding:24px}.brand{font-size:24px;font-weight:800}.nav{margin-top:38px;display:grid;gap:8px}.nav div{padding:12px;color:#aab2c0;border-radius:10px}.nav .active{background:#ffffff13;color:white}.main{min-width:0}.top{display:flex;justify-content:space-between;align-items:center}.pill{background:#ffffff0a;border:1px solid #ffffff15;border-radius:25px;padding:10px 15px;color:#c7ced9}.hero{margin:32px 0 24px}.hero h1{font-size:30px;margin:8px 0}.muted{color:#9ca6b5}.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}.stat{padding:22px}.num{font-size:28px;font-weight:750;margin-top:12px;color:#b6caff}.layout{display:grid;grid-template-columns:1.65fr 1fr;gap:16px;margin-top:18px}.panel{padding:22px}.head{display:flex;justify-content:space-between;align-items:center}.row{display:grid;grid-template-columns:1fr auto;gap:16px;padding:17px 0;border-bottom:1px solid #ffffff10}.tag{font-size:12px;border:1px solid #9dbbff35;color:#c2d2ff;padding:6px 10px;border-radius:20px}.small{font-size:13px;color:#9ca6b5;margin-top:6px}.stage{padding:12px;border-radius:12px;background:#ffffff07;margin:8px 0;display:flex;justify-content:space-between}@media(max-width:900px){.app{grid-template-columns:1fr;padding:14px}.side{display:none}.stats{grid-template-columns:repeat(2,1fr)}.layout{grid-template-columns:1fr}}@media(max-width:520px){.hero h1{font-size:23px}.stat,.panel{padding:15px}.top{flex-wrap:wrap;gap:10px}.row{grid-template-columns:1fr}.tag{width:max-content}.stats{gap:9px}}</style></head><body data-agent-native-node-id=\"an-1j4akuv\"><div class='app' data-agent-native-node-id=\"an-1hfh13r\"><aside class='side' data-agent-native-node-id=\"an-112duoj\"><div class='brand' data-agent-native-node-id=\"an-1pcl5xi\">عُمرَاي <span style='color:#a9bfff' data-agent-native-node-id=\"an-18n69jp\">◈</span></div><p class='muted' data-agent-native-node-id=\"an-kez2g3\">Sales Intelligence</p><div class='nav' data-agent-native-node-id=\"an-1p4ub9j\"><div class='active' data-agent-native-node-id=\"an-sg1enl\">نظرة عامة</div><div data-agent-native-node-id=\"an-1k86e90\">إشارات الطلب</div><div data-agent-native-node-id=\"an-qpqymk\">الفرص المؤهلة</div><div data-agent-native-node-id=\"an-1med0am\">الشركات</div><div data-agent-native-node-id=\"an-1hu57w9\">المصادر</div></div></aside><main class='main' data-agent-native-node-id=\"an-1mzncze\"><div class='top' data-agent-native-node-id=\"an-1e00uky\"><span class='pill' data-agent-native-node-id=\"an-7potb\">⌕ بحث في مساحة العمل</span><span class='pill' data-agent-native-node-id=\"an-11th5gr\">القاهرة · السوق الحالي</span></div><div class='hero' data-agent-native-node-id=\"an-1lzto1f\"><p class='muted' data-agent-native-node-id=\"an-1gpsw30\">لوحة التحكم</p><h1 data-agent-native-node-id=\"an-4buxe3\">صورة واضحة للطلب الحقيقي</h1><p class='muted' data-agent-native-node-id=\"an-1h4ptkn\">كل إشارة مرتبطة بمصدر وتاريخ رصد وحالة مراجعة.</p></div><div class='stats' data-agent-native-node-id=\"an-u5n57n\"><div class='stat' data-agent-native-node-id=\"an-17c38zi\">الإشارات<div class='num' data-agent-native-node-id=\"an-2av4q2\">128</div><span class='muted' data-agent-native-node-id=\"an-137q4v3\">عينة توضيحية</span></div><div class='stat' data-agent-native-node-id=\"an-1hwxyth\">تحتاج تحقق<div class='num' data-agent-native-node-id=\"an-1meevms\">24</div><span class='muted' data-agent-native-node-id=\"an-16bhkaz\">غير محسومة</span></div><div class='stat' data-agent-native-node-id=\"an-38nlrf\">مؤهلة<div class='num' data-agent-native-node-id=\"an-vjexqh\">16</div><span class='muted' data-agent-native-node-id=\"an-1ukwo4b\">بعد المراجعة</span></div><div class='stat' data-agent-native-node-id=\"an-168nhnz\">متابعة معتمدة<div class='num' data-agent-native-node-id=\"an-j5dhyj\">9</div><span class='muted' data-agent-native-node-id=\"an-q7lg7k\">بقرار بشري</span></div></div><div class='layout' data-agent-native-node-id=\"an-1qlm3ef\"><section class='panel' data-agent-native-node-id=\"an-c6kpy3\"><div class='head' data-agent-native-node-id=\"an-1j2luvv\"><h2 data-agent-native-node-id=\"an-7i25e\">سجل الإشارات</h2><span class='pill' data-agent-native-node-id=\"an-q5k2sk\">تصفية</span></div><div class='row' data-agent-native-node-id=\"an-u2h5rr\"><div data-agent-native-node-id=\"an-1ehg159\"><b data-agent-native-node-id=\"an-dut9mw\">طلب توريد تجهيزات مكتبية</b><div class='small' data-agent-native-node-id=\"an-10dplvb\">طلب منشور · مصدر عام · رُصد اليوم</div></div><span class='tag' data-agent-native-node-id=\"an-wfjfwj\">قيد المراجعة</span></div><div class='row' data-agent-native-node-id=\"an-1bg1cwv\"><div data-agent-native-node-id=\"an-1wbu9nc\"><b data-agent-native-node-id=\"an-1c8pq2g\">بحث عن خدمة صيانة</b><div class='small' data-agent-native-node-id=\"an-p98jb0\">طلب خدمة · مصدر عام · أمس</div></div><span class='tag' data-agent-native-node-id=\"an-vta5sd\">يحتاج تحقق</span></div><div class='row' data-agent-native-node-id=\"an-soyt1f\"><div data-agent-native-node-id=\"an-1kadc9f\"><b data-agent-native-node-id=\"an-1y8nzvb\">احتياج معدات مشروع</b><div class='small' data-agent-native-node-id=\"an-1ak348p\">إعلان طلب · منذ 3 أيام</div></div><span class='tag' data-agent-native-node-id=\"an-1n9ezek\">مؤهل</span></div></section><section class='panel' data-agent-native-node-id=\"an-1eav9eb\"><h2 data-agent-native-node-id=\"an-1bmvh9u\">التقدم</h2><div class='stage' data-agent-native-node-id=\"an-ar13bc\">جديد <b data-agent-native-node-id=\"an-1s814ma\">24</b></div><div class='stage' data-agent-native-node-id=\"an-1mq3eg4\">قيد التحقق <b data-agent-native-node-id=\"an-h4z0g5\">16</b></div><div class='stage' data-agent-native-node-id=\"an-4nspk5\">موافقة متابعة <b data-agent-native-node-id=\"an-fm2q8d\">9</b></div><p class='muted' data-agent-native-node-id=\"an-1fqgeo8\">الترتيب يعكس حالة المراجعة، وليس احتمالية الشراء.</p></section></div></main></div></body></html>"` | — |
## وثائق وفهرسة

### FILE-D7D5153A8A — [docs/ui-directions/variant-03-neon-command.html](../ui-directions/variant-03-neon-command.html#L1)

- النوع: **HTML**
- نطاق الفهرسة: جرد الملف + معرفات HTML والرموز داخل script/style

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-D7D5153A8A-L000001](../ui-directions/variant-03-neon-command.html#L1) | 1 | `"<!doctype html><html lang='ar' dir='rtl' data-agent-native-node-id=\"an-19qch1x\"><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><style>*{box-sizing:border-box}body{margin:0;background:radial-gradient(ellipse at 50% -20%,#15364d,transparent 55%),#070d16;color:#e7f7ff;font:14px system-ui,'Noto Sans Arabic',sans-serif}.app{display:grid;grid-template-columns:220px 1fr;gap:14px;padding:16px;min-height:100vh}.side,.panel,.stat{background:linear-gradient(145deg,#102334d9,#0b1724d9);border:1px solid #4ad8ff24;border-radius:16px;box-shadow:inset 0 1px #ffffff08,0 14px 40px #0004}.side{padding:18px}.brand{font-size:23px;font-weight:800;color:#6cecff}.nav{display:grid;gap:7px;margin-top:30px}.nav div{padding:12px;border-radius:9px;color:#89a9bc}.nav .active{background:#43dfff14;border:1px solid #43dfff2b;color:#7beaff}.main{min-width:0}.top{display:flex;justify-content:space-between;gap:10px}.pill{padding:9px 13px;border:1px solid #39cfff25;border-radius:9px;background:#0d1d2a;color:#9bc5d8}.hero{margin:22px 0}.hero h1{margin:5px 0;font-size:27px}.muted{color:#7799ad}.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}.stat{padding:17px}.num{font-size:26px;color:#71eaff;font-weight:800;margin:8px 0}.layout{display:grid;grid-template-columns:1.7fr 1fr;gap:12px;margin-top:12px}.panel{padding:17px}.panel h2{font-size:16px}.row{display:flex;justify-content:space-between;gap:10px;padding:13px 0;border-bottom:1px solid #2b4b5c}.tag{font-size:11px;color:#7ceaff;border:1px solid #2e9dbb55;padding:5px 9px;border-radius:7px}.meta{font-size:12px;color:#7593a5;margin-top:5px}.stage{display:flex;justify-content:space-between;padding:10px;margin:7px 0;background:#07131f;border:1px solid #1c3c50;border-radius:9px}.bar{height:5px;background:#152e3d;margin:10px 0;border-radius:9px}.bar i{display:block;width:57%;height:100%;background:#52dfff}@media(max-width:900px){.app{grid-template-columns:1fr;padding:10px}.side{display:none}.stats{grid-template-columns:repeat(2,1fr)}.layout{grid-template-columns:1fr}}@media(max-width:520px){.top{flex-direction:column}.hero h1{font-size:22px}.stat,.panel{padding:13px}.row{flex-direction:column}.tag{width:max-content}.stats{gap:7px}}</style></head><body data-agent-native-node-id=\"an-1mq2fgv\"><div class='app' data-agent-native-node-id=\"an-1snvlzn\"><aside class='side' data-agent-native-node-id=\"an-1u3uwz9\"><div class='brand' data-agent-native-node-id=\"an-1kzndb8\">◈ OMARAI</div><p class='muted' data-agent-native-node-id=\"an-ze5rg3\">INTELLIGENCE OS</p><div class='nav' data-agent-native-node-id=\"an-1r5k24x\"><div class='active' data-agent-native-node-id=\"an-z3nr0e\">⌘ مركز القيادة</div><div data-agent-native-node-id=\"an-1p079np\">⌕ إشارات الطلب</div><div data-agent-native-node-id=\"an-1291c89\">▤ التأهيل</div><div data-agent-native-node-id=\"an-phglyz\">◉ المصادر</div><div data-agent-native-node-id=\"an-8t0lis\">◌ حالة النظام</div></div></aside><main class='main' data-agent-native-node-id=\"an-1i54o1l\"><div class='top' data-agent-native-node-id=\"an-1jzcjba\"><span class='pill' data-agent-native-node-id=\"an-14wb78m\">⌕ بحث سريع / أمر</span><span class='pill' data-agent-native-node-id=\"an-1ku3fel\">MARKET: CAIRO · DEMO</span></div><section class='hero' data-agent-native-node-id=\"an-1amx86t\"><p class='muted' data-agent-native-node-id=\"an-15vdw4u\">SALES INTELLIGENCE / OVERVIEW</p><h1 data-agent-native-node-id=\"an-1y9mhoi\">مركز قيادة فرص السوق</h1><p class='muted' data-agent-native-node-id=\"an-4tzg1a\">رصد الاحتياج ← تحقق من الدليل ← تأهيل ← موافقة بشرية</p></section><div class='stats' data-agent-native-node-id=\"an-13ci5nn\"><div class='stat' data-agent-native-node-id=\"an-1a41epk\">إشارات واردة<div class='num' data-agent-native-node-id=\"an-wbhqbf\">128</div><span class='muted' data-agent-native-node-id=\"an-1df3phi\">بيانات تجريبية</span></div><div class='stat' data-agent-native-node-id=\"an-1s37bcg\">تحتاج تحقق<div class='num' data-agent-native-node-id=\"an-a4np0m\">24</div><span class='muted' data-agent-native-node-id=\"an-1584zmq\">Evidence review</span></div><div class='stat' data-agent-native-node-id=\"an-10uv4u1\">فرص مؤهلة<div class='num' data-agent-native-node-id=\"an-gjrv4f\">16</div><span class='muted' data-agent-native-node-id=\"an-1pirizs\">Reviewed</span></div><div class='stat' data-agent-native-node-id=\"an-1lrxcs7\">متابعة معتمدة<div class='num' data-agent-native-node-id=\"an-13wf6iv\">9</div><span class='muted' data-agent-native-node-id=\"an-s3k1hp\">Human-approved</span></div></div><div class='layout' data-agent-native-node-id=\"an-1f9sws\"><section class='panel' data-agent-native-node-id=\"an-uxvkmt\"><h2 data-agent-native-node-id=\"an-1xmc0cq\">LIVE SIGNAL QUEUE <span class='tag' data-agent-native-node-id=\"an-2h120v\">DEMO</span></h2><div class='row' data-agent-native-node-id=\"an-p2w54e\"><div data-agent-native-node-id=\"an-s1tel5\"><b data-agent-native-node-id=\"an-1yimqje\">طلب توريد تجهيزات مكتبية</b><div class='meta' data-agent-native-node-id=\"an-grpnev\">Public request · observed today</div></div><span class='tag' data-agent-native-node-id=\"an-nyd3xz\">REVIEW</span></div><div class='row' data-agent-native-node-id=\"an-ifohvr\"><div data-agent-native-node-id=\"an-3yxllp\"><b data-agent-native-node-id=\"an-ew8vf2\">طلب خدمة صيانة تكييف</b><div class='meta' data-agent-native-node-id=\"an-1vqr3zn\">Service request · yesterday</div></div><span class='tag' data-agent-native-node-id=\"an-s6kpwr\">VERIFY</span></div><div class='row' data-agent-native-node-id=\"an-1a7e2g0\"><div data-agent-native-node-id=\"an-202ik7\"><b data-agent-native-node-id=\"an-q0ez4n\">احتياج معدات مشروع</b><div class='meta' data-agent-native-node-id=\"an-xv1lu2\">Public listing · 3 days</div></div><span class='tag' data-agent-native-node-id=\"an-12nnh34\">QUALIFY</span></div></section><section class='panel' data-agent-native-node-id=\"an-ud0485\"><h2 data-agent-native-node-id=\"an-1xxdkmf\">QUALIFICATION PIPELINE</h2><div class='stage' data-agent-native-node-id=\"an-148mwmh\">New <b data-agent-native-node-id=\"an-1pi8wxr\">24</b></div><div class='bar' data-agent-native-node-id=\"an-1dyg74u\"><i data-agent-native-node-id=\"an-1mp2h7o\"></i></div><div class='stage' data-agent-native-node-id=\"an-pe36jr\">Verified <b data-agent-native-node-id=\"an-9927oo\">16</b></div><div class='stage' data-agent-native-node-id=\"an-1uli6yk\">Approved <b data-agent-native-node-id=\"an-1hwy8tc\">9</b></div><p class='muted' data-agent-native-node-id=\"an-5lffxl\">Operational states only — no purchase-probability score.</p></section></div></main></div></body></html>"` | — |
## ملفات أخرى

### FILE-C693279643 — [LICENSE](../../LICENSE#L1)

- النوع: **بدون امتداد**
- نطاق الفهرسة: جرد ملف نصي فقط

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-C693279643-L000001](../../LICENSE#L1) | 1 | `"MIT License"` | — |
| [SRC-C693279643-L000002](../../LICENSE#L2) | 2 | `""` | — |
| [SRC-C693279643-L000003](../../LICENSE#L3) | 3 | `"Copyright (c) 2026 Omarai contributors"` | — |
| [SRC-C693279643-L000004](../../LICENSE#L4) | 4 | `""` | — |
| [SRC-C693279643-L000005](../../LICENSE#L5) | 5 | `"Permission is hereby granted, free of charge, to any person obtaining a copy"` | — |
| [SRC-C693279643-L000006](../../LICENSE#L6) | 6 | `"of this software and associated documentation files (the \"Software\"), to deal"` | — |
| [SRC-C693279643-L000007](../../LICENSE#L7) | 7 | `"in the Software without restriction, including without limitation the rights"` | — |
| [SRC-C693279643-L000008](../../LICENSE#L8) | 8 | `"to use, copy, modify, merge, publish, distribute, sublicense, and/or sell"` | — |
| [SRC-C693279643-L000009](../../LICENSE#L9) | 9 | `"copies of the Software, and to permit persons to whom the Software is"` | — |
| [SRC-C693279643-L000010](../../LICENSE#L10) | 10 | `"furnished to do so, subject to the following conditions:"` | — |
| [SRC-C693279643-L000011](../../LICENSE#L11) | 11 | `""` | — |
| [SRC-C693279643-L000012](../../LICENSE#L12) | 12 | `"The above copyright notice and this permission notice shall be included in all"` | — |
| [SRC-C693279643-L000013](../../LICENSE#L13) | 13 | `"copies or substantial portions of the Software."` | — |
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
| [SRC-B335630551-L000001](../../README.md#L1) | 1 | `"# Omarai — Arabic-First AI Sales Intelligence & Customer Acquisition Agent"` | — |
| [SRC-B335630551-L000002](../../README.md#L2) | 2 | `""` | — |
| [SRC-B335630551-L000003](../../README.md#L3) | 3 | `"> **Foundational engineering requirements:** mandatory contributor/agent rules are in [AGENTS.md](AGENTS.md). The core architecture and security charter is [OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md](docs/OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md); the expanded platform practices across reliability, security, privacy, data, SRE, AI, accessibility, supply chain, and cost are in [OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md](docs/OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md); and the requirement IDs, expert-review lenses, evidence model, risk priorities, maturity stages, and release gates are in [OMARAI_REQUIREMENTS_TRACEABILITY_AND_MATURITY_MODEL_AR.md](docs/OMARAI_REQUIREMENTS_TRACEABILITY_AND_MATURITY_MODEL_AR.md). The initial foundational requirements checklist is [OMARAI_REQUIREMENTS_REGISTER.md](docs/OMARAI_REQUIREMENTS_REGISTER.md). These documents define required direction; they do not prove every control is implemented or tested. Use the [documentation index](docs/README.md) to find the current source of truth for each topic."` | — |
| [SRC-B335630551-L000004](../../README.md#L4) | 4 | `""` | — |
| [SRC-B335630551-L000005](../../README.md#L5) | 5 | `""` | — |
| [SRC-B335630551-L000006](../../README.md#L6) | 6 | `"Omarai's product mission is to be an Arabic-first AI Sales Intelligence and Customer Acquisition Agent: understand a product or service and its market, discover public and permitted buying-demand signals, verify their evidence, qualify opportunities, and recommend useful sales follow-ups."` | — |
| [SRC-B335630551-L000007](../../README.md#L7) | 7 | `""` | — |
| [SRC-B335630551-L000008](../../README.md#L8) | 8 | ``"The current repository provides a bounded web-research and evidence pipeline, a `LEAD_GENERATION` intent route, an initial buyer-signal detector, and a local lead workspace. These are foundational capabilities, **not proof of a complete end-to-end sales intelligence product**. Product understanding, ICP-aware demand discovery, multi-type signal classification, evidence-backed qualification, and the full sales workflow remain subject to the implementation and acceptance gates in the [Sales Intelligence Architecture](docs/OMARAI_SALES_INTELLIGENCE_ARCHITECTURE_AR.md)."`` | — |
| [SRC-B335630551-L000009](../../README.md#L9) | 9 | `""` | — |
| [SRC-B335630551-L000010](../../README.md#L10) | 10 | `"The existing responsive RTL research interface and general web-research capabilities remain shared platform capabilities. The sales domain should reuse them rather than create a second search engine."` | — |
| [SRC-B335630551-L000011](../../README.md#L11) | 11 | `""` | — |
| [SRC-B335630551-L000012](../../README.md#L12) | 12 | ``"The Arabic RTL sales workspace is the product's primary experience at `/` and `/workspace`. The general-purpose web-research agent remains available at `/agent`, while the legacy lead dashboard remains at `/leads`. Public-web research, page reading, evidence handling, and language models are shared platform capabilities that support the sales-intelligence mission; they are not the product's end goal."`` | — |
| [SRC-B335630551-L000013](../../README.md#L13) | 13 | `""` | — |
| [SRC-B335630551-L000014](../../README.md#L14) | 14 | `"## Product direction and current delivery snapshot — 6 November 2026"` | — |
| [SRC-B335630551-L000015](../../README.md#L15) | 15 | `""` | — |
| [SRC-B335630551-L000016](../../README.md#L16) | 16 | `"Omarai's approved product direction is evidence-backed discovery and qualification of public buying-demand signals for a user-described product/service and market. A company matching the target profile is not, by itself, a buyer-intent signal. The product does not perform automated outreach."` | — |
| [SRC-B335630551-L000017](../../README.md#L17) | 17 | `""` | — |
| [SRC-B335630551-L000018](../../README.md#L18) | 18 | ``"- Current `main`: `a297abd271d48f459effad083a9f424a1499cd39`."`` | — |
| [SRC-B335630551-L000019](../../README.md#L19) | 19 | ``"- The default route `/` and `/workspace` serve the Arabic sales workspace; `/agent` serves the general research agent; `/leads` preserves the legacy lead view."`` | — |
| [SRC-B335630551-L000020](../../README.md#L20) | 20 | `"- The currently connected workspace views are overview, existing demand-signal inbox, qualification pipeline, and a non-probing system snapshot. Other menu modules remain unavailable unless a server-side contract is implemented and verified."` | — |
| [SRC-B335630551-L000021](../../README.md#L21) | 21 | ``"- Product profiles and buyer-intent discovery are proposed in [PR #155](https://github.com/mosabosama2030-oss/omarai/pull/155), which is **open and not merged** in this snapshot. Do not treat those capabilities as part of `main`."`` | — |
| [SRC-B335630551-L000022](../../README.md#L22) | 22 | `"- See [current project status and governing decisions](docs/OMARAI_PROJECT_STATUS_AND_DECISIONS_AR.md) for merge state, CI evidence, open risks, and release gates."` | — |
| [SRC-B335630551-L000023](../../README.md#L23) | 23 | `""` | — |
| [SRC-B335630551-L000024](../../README.md#L24) | 24 | `"## What this version does"` | — |
| [SRC-B335630551-L000025](../../README.md#L25) | 25 | `""` | — |
| [SRC-B335630551-L000026](../../README.md#L26) | 26 | `"- Plans up to eight search queries from a natural-language question with a dedicated reasoning/planning model, and uses a deterministic multi-query fallback when the model is unavailable."` | — |
| [SRC-B335630551-L000027](../../README.md#L27) | 27 | `"- Uses separate model roles by default: NVIDIA Nemotron 3 Ultra (free) for query planning and Google Gemma 4 31B Instruct (free) for answer synthesis and the second-pass consistency review; retries with OpenRouter's free-model router if a chosen model fails."` | — |
| [SRC-B335630551-L000028](../../README.md#L28) | 28 | `"- Runs DuckDuckGo HTML and Bing RSS independently for every planned query; can add official Brave Search API and Tavily Search API result indexes when their environment keys are configured; uses Google News RSS for queries judged time-sensitive."` | — |
| [SRC-B335630551-L000029](../../README.md#L29) | 29 | `"- Fuses duplicate results across queries and engines using reciprocal-rank fusion, preserving provider, query, domain, platform, publication-date and page-extraction provenance."` | — |
| [SRC-B335630551-L000030](../../README.md#L30) | 30 | `"- Extracts text from up to eight accessible public pages per question with request-size and timeout bounds, following at most three individually validated public redirects."` | — |
| [SRC-B335630551-L000031](../../README.md#L31) | 31 | ``"- Searches public Reddit RSS and the Bluesky public search endpoint when social discussion is relevant; can use Reddit's OAuth API when `REDDIT_CLIENT_ID` and `REDDIT_CLIENT_SECRET` are provided."`` | — |
| [SRC-B335630551-L000032](../../README.md#L32) | 32 | `"- Searches indexed public pages on Facebook, Instagram, X, TikTok, LinkedIn, Threads and YouTube through the general web engines."` | — |
| [SRC-B335630551-L000033](../../README.md#L33) | 33 | `"- Can use the official Meta Graph API to read posts and a small sample of public comments from explicitly configured Facebook Pages when the token has suitable permissions."` | — |
| [SRC-B335630551-L000034](../../README.md#L34) | 34 | ``"- Can use Instagram Graph API hashtag search to read public hashtag media when `INSTAGRAM_USER_ID` and `INSTAGRAM_ACCESS_TOKEN` have the required permissions. It is not a global Instagram search and has platform quotas."`` | — |
| [SRC-B335630551-L000035](../../README.md#L35) | 35 | ``"- Can use the official X recent-post endpoint when `X_BEARER_TOKEN` is configured and the account/API tier permits the request; can use the official YouTube Data API when `YOUTUBE_API_KEY` is configured."`` | — |
| [SRC-B335630551-L000036](../../README.md#L36) | 36 | `"- Generates an evidence-grounded answer in the user's language, showing source links, query plan, provider coverage, direct page reads, platform mix, source/domain diversity, date coverage, and evidence-coverage warnings. Coverage indicators describe breadth and inspectability; they are not probabilities that the answer is true."` | — |
| [SRC-B335630551-L000037](../../README.md#L37) | 37 | `"- Carries up to eight recent chat messages from the current browser session into follow-up questions."` | — |
| [SRC-B335630551-L000038](../../README.md#L38) | 38 | ``"- Keeps the existing local SQLite lead workspace at `/leads`. The approved Arabic RTL Neon Command sales workspace is the default home at `/` and remains available at `/workspace`; it includes overview, tenant-scoped product/market profiles, buyer-intent discovery runs using the existing lead-generation search pipeline, human-reviewed saving of server-qualified public-demand signals, signal review, and qualification-status updates. The general web-research agent remains available at `/agent`. The system-state view reads the non-probing `/api/health` configuration snapshot. Company profiles, market analytics, scheduled monitoring, evidence/audit centers, tasks, settings and other modules without completed server contracts remain explicitly unavailable."`` | — |
| [SRC-B335630551-L000039](../../README.md#L39) | 39 | `"- Binds to loopback by default; it is not a public production deployment."` | — |
| [SRC-B335630551-L000040](../../README.md#L40) | 40 | `""` | — |
| [SRC-B335630551-L000041](../../README.md#L41) | 41 | ``"**Verification semantics:** `GET /api/health` is a configuration/dependency snapshot, not proof that search providers or the model are reachable. Check the `agent.verification_scope` field to see what is and is not verified. Use the protected `POST /api/diagnostics` endpoint for explicit live search/model probes; a passed diagnostic only verifies the specific probes run at that time, not every optional connector or answer quality."`` | — |
| [SRC-B335630551-L000042](../../README.md#L42) | 42 | `""` | — |
| [SRC-B335630551-L000043](../../README.md#L43) | 43 | `"This is a tool-using research agent built around existing language models, not a foundation model trained from scratch. The role-specific defaults aim for more consistent behaviour than using a router that selects a different free model at random on each call. Exact availability and response quality still depend on OpenRouter/provider conditions. **Privacy warning:** the user's question, conversation context and selected web excerpts are sent to the configured external language-model provider for planning/synthesis/review. OpenRouter's NVIDIA Nemotron free endpoint states that session data may be logged for security and product improvement; do not send passwords, API keys, private information or personal/confidential customer data through the free endpoint. See the [NVIDIA Nemotron free-endpoint privacy notice](https://openrouter.ai/nvidia/nemotron-3-ultra-550b-a55b:free). Its language-model planner decides how to search, but query count, URLs and result shapes are validated by deterministic code. Cross-engine agreement improves discovery and ranking but is not independent fact verification. Public social pages that require login, blocked pages and private profiles are not fetched; social search cannot promise complete coverage of any platform. Direct official-platform access varies: Reddit API access requires approved app credentials and is subject to Reddit's terms; Facebook Pages reads require a valid token, page identifiers and correct permissions; Instagram hashtag search requires a professional Instagram account token and the specific supported permissions; X API access requires an authorized bearer token and suitable access; YouTube direct API search requires a Google API key. These APIs do not grant universal access to all content, accounts or comments. Review each platform's terms, quotas and permitted use before using the agent commercially. The agent never bypasses login, paywall or access controls and does not send messages or make automated contact with people."` | — |
| [SRC-B335630551-L000044](../../README.md#L44) | 44 | `""` | — |
| [SRC-B335630551-L000045](../../README.md#L45) | 45 | `""` | — |
| [SRC-B335630551-L000046](../../README.md#L46) | 46 | `"## Living repository index"` | — |
| [SRC-B335630551-L000047](../../README.md#L47) | 47 | `""` | — |
| [SRC-B335630551-L000048](../../README.md#L48) | 48 | `"**Current delivery gate (Arabic):** [OMARAI HANDOFF CHECKLIST](docs/OMARAI_HANDOFF_CHECKLIST_AR.md) — current release blockers, required evidence, and operator actions. The central [remediation register](docs/OMARAI_REMEDIATION_REGISTER_AR.md) remains the detailed issue history."` | — |
| [SRC-B335630551-L000049](../../README.md#L49) | 49 | `""` | — |
| [SRC-B335630551-L000050](../../README.md#L50) | 50 | `"Omarai maintains a categorized master index and a paginated, line-by-line source index:"` | — |
| [SRC-B335630551-L000051](../../README.md#L51) | 51 | `""` | — |
| [SRC-B335630551-L000052](../../README.md#L52) | 52 | ``"- [MASTER INDEX](docs/MASTER_INDEX.md): file inventory with stable file IDs, Python AST definitions, static frontend/configuration symbols, and explicitly marked TODO/FIXME/BUG/HACK/XXX/REVIEW/SECURITY/DEPRECATED/ISSUE/DEFECT/REGRESSION/RISK/GAP/ERROR/WARNING/PERF/PRIVACY/DATA_LOSS/ACCESSIBILITY entries. Each review marker has an `FND-...` code and a link to the exact source line."`` | — |
| [SRC-B335630551-L000053](../../README.md#L53) | 53 | `"- [SOURCE LINES INDEX](docs/SOURCE_LINES_INDEX.md): search-friendly directory of files, page links, per-file line counts, and links to each source line."` | — |
| [SRC-B335630551-L000054](../../README.md#L54) | 54 | `"- [INDEX COVERAGE AUDIT](docs/INDEX_COVERAGE_AUDIT.md): generated evidence of line-count consistency, metadata-only files, excluded path names and their reasons, and the exact scope of any “100%” coverage statement."` | — |
| [SRC-B335630551-L000055](../../README.md#L55) | 55 | ``"- [Source line pages](docs/source_index/): small generated pages containing every logical line from eligible readable text files. Each line has a `SRC-<FILEHASH>-L000001` code, exact JSON-escaped text, and a link back to the source file at the matching line. Pages are capped at 800 line records to remain navigable on mobile and in GitHub's web view."`` | — |
| [SRC-B335630551-L000056](../../README.md#L56) | 56 | `"- [Local source search](docs/search_code.py): offline text/regex search with file, line, nearby context, and GitHub line links. It excludes common secret/configuration files, databases, key files, symlinks, and runtime directories; it does not detect every secret or replace a security audit."` | — |
| [SRC-B335630551-L000057](../../README.md#L57) | 57 | `""` | — |
| [SRC-B335630551-L000058](../../README.md#L58) | 58 | ``"Example: `python docs/search_code.py \"resolve_followup_query\" --ext py --context 2`."`` | — |
| [SRC-B335630551-L000059](../../README.md#L59) | 59 | `""` | — |
| [SRC-B335630551-L000060](../../README.md#L60) | 60 | ``"The generator now refuses to publish indexes if any eligible file has missing, duplicated, or misnumbered source-line records. It still cannot infer every unmarked logical/programming defect; known issues should be recorded explicitly with a supported marker (for example, `# BUG: explain the defect`) so the generated `FND-...` register can point to the corresponding `SRC-...` line."`` | — |
| [SRC-B335630551-L000061](../../README.md#L61) | 61 | `""` | — |
| [SRC-B335630551-L000062](../../README.md#L62) | 62 | `"Regenerate and verify the indexes locally:"` | — |
| [SRC-B335630551-L000063](../../README.md#L63) | 63 | `""` | — |
| [SRC-B335630551-L000064](../../README.md#L64) | 64 | ````"```bash"```` | — |
| [SRC-B335630551-L000065](../../README.md#L65) | 65 | `"python docs/generate_index.py"` | — |
| [SRC-B335630551-L000066](../../README.md#L66) | 66 | `"python docs/generate_index.py --check"` | — |
| [SRC-B335630551-L000067](../../README.md#L67) | 67 | ````"```"```` | — |
| [SRC-B335630551-L000068](../../README.md#L68) | 68 | `""` | — |
| [SRC-B335630551-L000069](../../README.md#L69) | 69 | ``"GitHub Actions validates the generator on Python 3.11 and 3.12. The publishing workflow runs on pushes to `main` and the `feat/**`, `fix/**`, and `feature/**` branches. It regenerates and commits all indexes and generated pages only when output changes; obsolete generated pages are removed, while generated-index-only commits are ignored to avoid loops. Documentation-only and repository-hygiene branches are still tested with indexes regenerated in the isolated test workspace, but do not carry a large generated-page diff solely because documentation lines moved; after merge, the publisher refreshes the committed indexes on `main`. If direct publication to `main` is rejected, it opens a pull request instead of force-updating a branch or auto-merging."`` | — |
| [SRC-B335630551-L000070](../../README.md#L70) | 70 | `""` | — |
| [SRC-B335630551-L000071](../../README.md#L71) | 71 | ``"When a known code issue is found, add a source comment using one supported marker name (TODO, FIXME, BUG, HACK, XXX, REVIEW, SECURITY, DEPRECATED, ISSUE, DEFECT, REGRESSION, RISK, GAP, ERROR, WARNING, PERF, PRIVACY, DATA_LOSS, or ACCESSIBILITY), followed by a colon and a concise description. The index assigns an `FND-...` code and links it to the exact `SRC-...` source-line record; removing or editing that source annotation updates the generated register on the next index run. Coverage includes every logical line in eligible readable text files up to 2 MiB. Known local secrets, runtime databases, dependency/build directories, binary/unreadable files and oversized files are excluded from line-level indexing by design but listed by metadata where eligible. Static review markers help track explicit findings; no source index can prove that every arbitrary logic bug has been detected or that all code is correct."`` | — |
| [SRC-B335630551-L000072](../../README.md#L72) | 72 | `""` | — |
| [SRC-B335630551-L000073](../../README.md#L73) | 73 | `"## Per-request resource budget"` | — |
| [SRC-B335630551-L000074](../../README.md#L74) | 74 | `""` | — |
| [SRC-B335630551-L000075](../../README.md#L75) | 75 | ``"Each `POST /api/agent` answer includes a `request_budget` object with elapsed and remaining time, reserved resource counts, and configured limits. The current defaults are a 90-second cooperative deadline, at most 8 search queries, 32 provider search calls, 8 model HTTP attempts, 8 page fetches, and up to 3 optional server-side search-tool calls per request. Operator limits may be lowered or raised only within hard caps: `OMARAI_REQUEST_BUDGET_SECONDS` (10–120), `OMARAI_REQUEST_MAX_SEARCH_QUERIES` (1–8), `OMARAI_REQUEST_MAX_SEARCH_CALLS` (1–40), `OMARAI_REQUEST_MAX_MODEL_CALLS` (1–12), `OMARAI_REQUEST_MAX_PAGE_FETCHES` (1–8), and `OMARAI_REQUEST_MAX_TOOL_CALLS` (0–3). Invalid numeric values fall back to the defaults; out-of-range values are clamped."`` | — |
| [SRC-B335630551-L000076](../../README.md#L76) | 76 | `""` | — |
| [SRC-B335630551-L000077](../../README.md#L77) | 77 | `"The deadline caps the timeout passed to outbound operations and prevents new work from being reserved after the deadline or a resource cap is exhausted. It is **cooperative, not hard cancellation**: a network call already in progress may overrun slightly while its client unwinds. Do not interpret this metadata as a load test, a throughput guarantee, or proof that any live provider is reachable. CI tests for budget logic are separate from live-provider validation."` | — |
| [SRC-B335630551-L000078](../../README.md#L78) | 78 | `""` | — |
| [SRC-B335630551-L000079](../../README.md#L79) | 79 | ``"The HTTP ingress caps active handler connections at 32 per process by default through `OMARAI_MAX_CONCURRENT_HTTP_CONNECTIONS` (bounded to 1–128). When all slots are occupied, excess sockets receive HTTP 503 with `Retry-After: 5` before a handler thread is created. The in-memory rate limiter also caps client buckets at 4,096 per process; new identities beyond that ceiling share a conservative overflow quota. Separately, expensive `/api/agent` and `/api/diagnostics` operations remain limited to at most 4 concurrent operations per process by default; configure `OMARAI_MAX_CONCURRENT_AGENT_REQUESTS` from 1 to 8. These are **process-local** controls, not distributed limits across workers or replicas, and they are not throughput/load-test claims."`` | — |
| [SRC-B335630551-L000080](../../README.md#L80) | 80 | `""` | — |
| [SRC-B335630551-L000081](../../README.md#L81) | 81 | `"## Experimental DeepSeek Search provider"` | — |
| [SRC-B335630551-L000082](../../README.md#L82) | 82 | `""` | — |
| [SRC-B335630551-L000083](../../README.md#L83) | 83 | `"Omarai can optionally compare results from DeepSeek's Search API when"` | — |
| [SRC-B335630551-L000084](../../README.md#L84) | 84 | ``"`DEEPSEEK_SEARCH_API_KEY` is configured in the host's secret settings. It is"`` | — |
| [SRC-B335630551-L000085](../../README.md#L85) | 85 | `"**disabled by default**; DuckDuckGo and Bing remain configured as before."` | — |
| [SRC-B335630551-L000086](../../README.md#L86) | 86 | `"To limit possible spend when opted in, the request budget defaults to **one"` | — |
| [SRC-B335630551-L000087](../../README.md#L87) | 87 | `"DeepSeek Search call per answer/diagnostic operation**. It can be set from 0 to 3"` | — |
| [SRC-B335630551-L000088](../../README.md#L88) | 88 | ``"using `OMARAI_DEEPSEEK_SEARCH_REQUEST_BUDGET`; invalid values fall back to 1."`` | — |
| [SRC-B335630551-L000089](../../README.md#L89) | 89 | `"DeepSeek Search is billed per successful request (currently documented at"` | — |
| [SRC-B335630551-L000090](../../README.md#L90) | 90 | `"US$0.75 per 1,000 successful searches); review the"` | — |
| [SRC-B335630551-L000091](../../README.md#L91) | 91 | `"[official Search & Fetch guide](https://api-docs.deepseek.com/guides/search/)"` | — |
| [SRC-B335630551-L000092](../../README.md#L92) | 92 | `"before enabling it. Unit tests use a mocked response; this repository change"` | — |
| [SRC-B335630551-L000093](../../README.md#L93) | 93 | `"does not claim live DeepSeek connectivity or answer-quality improvement."` | — |
| [SRC-B335630551-L000094](../../README.md#L94) | 94 | `""` | — |
| [SRC-B335630551-L000095](../../README.md#L95) | 95 | `"## Hosting and live acceptance"` | — |
| [SRC-B335630551-L000096](../../README.md#L96) | 96 | `""` | — |
| [SRC-B335630551-L000097](../../README.md#L97) | 97 | `"Omarai includes several **alternative** hosting paths. Choose one provider; the presence of a config file is not proof that a service exists or has passed acceptance."` | — |
| [SRC-B335630551-L000098](../../README.md#L98) | 98 | `""` | — |
| [SRC-B335630551-L000099](../../README.md#L99) | 99 | ``"- **Railway:** [Arabic deployment guide](docs/DEPLOY_RAILWAY_AR.md), using `railway.json`."`` | — |
| [SRC-B335630551-L000100](../../README.md#L100) | 100 | `"- **SnapDeploy:** [free-demo guide](docs/DEPLOY_SNAPDEPLOY_AR.md). Confirm current quotas and terms before use; ephemeral storage means it is not a durable lead database."` | — |
| [SRC-B335630551-L000101](../../README.md#L101) | 101 | ``"- **Render:** [optional alternative guide](docs/DEPLOY_RENDER_AR.md), using `render.yaml`. Use it only if the provider/account is available to you."`` | — |
| [SRC-B335630551-L000102](../../README.md#L102) | 102 | `""` | — |
| [SRC-B335630551-L000103](../../README.md#L103) | 103 | ``"All providers share the same acceptance rules. The API reports a validated source revision at `/api/health`: it prefers image-baked `BUILD_SHA`, then documented platform Git metadata where supported. For another Docker host, pass `--build-arg OMARAI_BUILD_SHA=\"$(git rev-parse HEAD)\"`. A local/container build is not evidence of a live deployment; compare the reported SHA with the exact intended commit."`` | — |
| [SRC-B335630551-L000104](../../README.md#L104) | 104 | `""` | — |
| [SRC-B335630551-L000105](../../README.md#L105) | 105 | `"**Initial operating model:** one company/workspace. The tenant/user/membership/token/session foundation and tenant-scoped lead CRUD/list/import/export are included in the base [PR #145](https://github.com/mosabosama2030-oss/omarai/pull/145) and pass automated CI on that branch; this does not make Omarai a production-ready multi-customer SaaS. Self-service user/membership provisioning, a complete role matrix, hosted acceptance, durable-volume verification, backup/restore, and multi-process load tests remain open. Until those gates are completed, keep the hosted instance restricted to one company/operator and do not store confidential records for multiple customers. Concurrency and rate-limit state remain process-local, not distributed; the current ceilings do not establish production load capacity."` | — |
| [SRC-B335630551-L000106](../../README.md#L106) | 106 | `""` | — |
| [SRC-B335630551-L000107](../../README.md#L107) | 107 | ``"For a public-bound instance, set `OMARAI_PUBLIC_DEPLOYMENT=1` and a separate random `OMARAI_ACCESS_TOKEN` of at least 32 characters. The app refuses public binding without both. Configure `OPENROUTER_API_KEY` or `OMARAI_LLM_API_KEY` only in the provider's secret store. If the UI is on another origin, set `OMARAI_ALLOWED_ORIGINS` to the exact trusted origins (scheme, host, optional port; no path or wildcard). The built-in UI served from the same host usually needs no extra origin entry. Public API routes require the bearer token and apply a default in-memory per-client IP limit of 20 requests per minute. The browser stores only the app access token in local storage, not the provider API key."`` | — |
| [SRC-B335630551-L000108](../../README.md#L108) | 108 | `""` | — |
| [SRC-B335630551-L000109](../../README.md#L109) | 109 | ``"Before accepting any host, follow the [go-live checklist](docs/GO_LIVE_CHECKLIST_AR.md) and run the manually triggered [hosted acceptance smoke workflow](.github/workflows/hosted-smoke.yml) only after setting GitHub Actions secrets `OMARAI_ACCESS_TOKEN` and `OMARAI_BASE_URL` to the authorized service. The workflow makes real model/search calls and may incur usage charges; do not run it without human approval. On hosts with a genuinely persistent mounted volume, set `OMARAI_DB_PATH` to a file inside the mount (for example, `/data/omarai.sqlite3`). This setting selects a path; it does not create storage or replace backups and a tested restore. Keep the lead workspace disabled for important records until persistence across restart/redeploy and restore are verified on the actual host."`` | — |
| [SRC-B335630551-L000110](../../README.md#L110) | 110 | `""` | — |
| [SRC-B335630551-L000111](../../README.md#L111) | 111 | `"## Run on Android / Termux"` | — |
| [SRC-B335630551-L000112](../../README.md#L112) | 112 | `""` | — |
| [SRC-B335630551-L000113](../../README.md#L113) | 113 | `"From the repository directory:"` | — |
| [SRC-B335630551-L000114](../../README.md#L114) | 114 | `""` | — |
| [SRC-B335630551-L000115](../../README.md#L115) | 115 | ````"```bash"```` | — |
| [SRC-B335630551-L000116](../../README.md#L116) | 116 | `"python -m pip install -e ."` | — |
| [SRC-B335630551-L000117](../../README.md#L117) | 117 | ````"```"```` | — |
| [SRC-B335630551-L000118](../../README.md#L118) | 118 | `""` | — |
| [SRC-B335630551-L000119](../../README.md#L119) | 119 | ``"The default language-model configuration uses OpenRouter: Nemotron 3 Ultra (free) plans queries, Gemma 4 31B Instruct (free) writes the answer and performs the optional second-pass review, and `openrouter/free` is the fallback if a selected model fails. Create an OpenRouter API key, then enter it without putting the secret into a command-history entry. The model key enables both search planning and generative synthesis; general web search can still run without it, but results will not be turned into a full language-model analysis:"`` | — |
| [SRC-B335630551-L000120](../../README.md#L120) | 120 | `""` | — |
| [SRC-B335630551-L000121](../../README.md#L121) | 121 | ````"```bash"```` | — |
| [SRC-B335630551-L000122](../../README.md#L122) | 122 | `"read -r -s -p \"OpenRouter API key: \" OPENROUTER_API_KEY"` | — |
| [SRC-B335630551-L000123](../../README.md#L123) | 123 | `"printf '\\n'"` | — |
| [SRC-B335630551-L000124](../../README.md#L124) | 124 | `"export OPENROUTER_API_KEY"` | — |
| [SRC-B335630551-L000125](../../README.md#L125) | 125 | `"python -m cli.omarai serve"` | — |
| [SRC-B335630551-L000126](../../README.md#L126) | 126 | ````"```"```` | — |
| [SRC-B335630551-L000127](../../README.md#L127) | 127 | `""` | — |
| [SRC-B335630551-L000128](../../README.md#L128) | 128 | `"Keep this Termux session running and open **http://127.0.0.1:8765** in the phone's browser. The agent chat is the home screen. The existing lead workspace remains available at **http://127.0.0.1:8765/leads**."` | — |
| [SRC-B335630551-L000129](../../README.md#L129) | 129 | `""` | — |
| [SRC-B335630551-L000130](../../README.md#L130) | 130 | `"The key is held in the current shell environment and is not written into the repository. Enter it again in a new Termux session. Never commit API keys or paste them into public issues or chat."` | — |
| [SRC-B335630551-L000131](../../README.md#L131) | 131 | `""` | — |
| [SRC-B335630551-L000132](../../README.md#L132) | 132 | `"### Optional configuration"` | — |
| [SRC-B335630551-L000133](../../README.md#L133) | 133 | `""` | — |
| [SRC-B335630551-L000134](../../README.md#L134) | 134 | `"For additional live web-search indexes, configure either official search API. These keys are optional: the built-in public engines are still attempted, and each API may have its own account, quota, rate limit or cost. Do not assume an API is free or that a configured key is valid until you run the live diagnostics."` | — |
| [SRC-B335630551-L000135](../../README.md#L135) | 135 | `""` | — |
| [SRC-B335630551-L000136](../../README.md#L136) | 136 | ````"```bash"```` | — |
| [SRC-B335630551-L000137](../../README.md#L137) | 137 | `"read -r -s -p \"Brave Search API key: \" BRAVE_SEARCH_API_KEY; printf '\\\\n'; export BRAVE_SEARCH_API_KEY"` | — |
| [SRC-B335630551-L000138](../../README.md#L138) | 138 | `"read -r -s -p \"Tavily API key: \" TAVILY_API_KEY; printf '\\\\n'; export TAVILY_API_KEY"` | — |
| [SRC-B335630551-L000139](../../README.md#L139) | 139 | ````"```"```` | — |
| [SRC-B335630551-L000140](../../README.md#L140) | 140 | `""` | — |
| [SRC-B335630551-L000141](../../README.md#L141) | 141 | `""` | — |
| [SRC-B335630551-L000142](../../README.md#L142) | 142 | `"For a different OpenAI-compatible endpoint or model, set these environment variables before starting the server:"` | — |
| [SRC-B335630551-L000143](../../README.md#L143) | 143 | `""` | — |
| [SRC-B335630551-L000144](../../README.md#L144) | 144 | ````"```bash"```` | — |
| [SRC-B335630551-L000145](../../README.md#L145) | 145 | `"export OMARAI_LLM_BASE_URL=\"https://openrouter.ai/api/v1\""` | — |
| [SRC-B335630551-L000146](../../README.md#L146) | 146 | `"export OMARAI_LLM_MODEL=\"openrouter/free\""` | — |
| [SRC-B335630551-L000147](../../README.md#L147) | 147 | ````"```"```` | — |
| [SRC-B335630551-L000148](../../README.md#L148) | 148 | `""` | — |
| [SRC-B335630551-L000149](../../README.md#L149) | 149 | ``"Use `OMARAI_LLM_API_KEY` instead of `OPENROUTER_API_KEY` when you want a separate environment variable. `OMARAI_LLM_TIMEOUT` accepts a timeout in seconds from 5 to 60. To customize model roles, set `OMARAI_PLANNER_MODEL`, `OMARAI_ANSWER_MODEL`, and/or `OMARAI_REVIEW_MODEL`; `OMARAI_LLM_MODEL` remains a global override for all roles that have no role-specific override. `OMARAI_LLM_FALLBACK_MODEL` changes the default `openrouter/free` fallback. Provider pricing, model availability and rate limits can change; check the chosen provider before using a paid model. Optional social credentials may be configured in the same Termux session before starting the server: `REDDIT_CLIENT_ID` + `REDDIT_CLIENT_SECRET` (official OAuth access), `X_BEARER_TOKEN`, `YOUTUBE_API_KEY`, `INSTAGRAM_USER_ID` + `INSTAGRAM_ACCESS_TOKEN` + optional `META_GRAPH_VERSION`, and `FACEBOOK_PAGE_ACCESS_TOKEN` + `FACEBOOK_PAGE_IDS` (comma-separated Page IDs that the authorized token can access). Use `read -r -s` to enter secrets privately rather than saving them in shell history. Do not store keys in source files, HTML, commits or chat messages."`` | — |
| [SRC-B335630551-L000150](../../README.md#L150) | 150 | `""` | — |
| [SRC-B335630551-L000151](../../README.md#L151) | 151 | `"If no language-model key is configured, Omarai can still attempt web search and show source snippets, but it cannot provide the full generative understanding/synthesis layer. If search providers are temporarily unavailable, the agent reports the limitation rather than pretending that a search succeeded."` | — |
| [SRC-B335630551-L000152](../../README.md#L152) | 152 | `""` | — |
| [SRC-B335630551-L000153](../../README.md#L153) | 153 | `"For the platform boundaries, optional credentials and safe Termux setup for social connectors, see the [Arabic research connectors guide](docs/RESEARCH_CONNECTORS_AR.md)."` | — |
| [SRC-B335630551-L000154](../../README.md#L154) | 154 | `""` | — |
| [SRC-B335630551-L000155](../../README.md#L155) | 155 | `"## API"` | — |
| [SRC-B335630551-L000156](../../README.md#L156) | 156 | `""` | — |
| [SRC-B335630551-L000157](../../README.md#L157) | 157 | ``"- `GET /` — web-research chat"`` | — |
| [SRC-B335630551-L000158](../../README.md#L158) | 158 | ``"- `GET /leads` — existing lead workspace"`` | — |
| [SRC-B335630551-L000159](../../README.md#L159) | 159 | ``"- `GET /api/health` — setup and dependency status (never returns the API key)"`` | — |
| [SRC-B335630551-L000160](../../README.md#L160) | 160 | ``"- `POST /api/diagnostics` — opt-in live checks for web search and the language model; set `test_social: true` to also probe public/authorized social connectors"`` | — |
| [SRC-B335630551-L000161](../../README.md#L161) | 161 | ``"- `POST /api/agent` — open-ended question plus optional recent `history`"`` | — |
| [SRC-B335630551-L000162](../../README.md#L162) | 162 | ``"- `POST /api/analyze` — existing rule-based lead-text assessment"`` | — |
| [SRC-B335630551-L000163](../../README.md#L163) | 163 | ``"- `GET/POST /api/leads` — existing local lead records"`` | — |
| [SRC-B335630551-L000164](../../README.md#L164) | 164 | `""` | — |
| [SRC-B335630551-L000165](../../README.md#L165) | 165 | `"Example request:"` | — |
| [SRC-B335630551-L000166](../../README.md#L166) | 166 | `""` | — |
| [SRC-B335630551-L000167](../../README.md#L167) | 167 | ````"```json"```` | — |
| [SRC-B335630551-L000168](../../README.md#L168) | 168 | `"{"` | — |
| [SRC-B335630551-L000169](../../README.md#L169) | 169 | `"  \"question\": \"Compare the latest public information about two technologies\","` | — |
| [SRC-B335630551-L000170](../../README.md#L170) | 170 | `"  \"history\": []"` | — |
| [SRC-B335630551-L000171](../../README.md#L171) | 171 | `"}"` | — |
| [SRC-B335630551-L000172](../../README.md#L172) | 172 | ````"```"```` | — |
| [SRC-B335630551-L000173](../../README.md#L173) | 173 | `""` | — |
| [SRC-B335630551-L000174](../../README.md#L174) | 174 | ``"The `/api/diagnostics` response reports pass/fail/degraded states, returned result counts, provider counts, elapsed time, and the model that actually answered (including fallback use). The Arabic web UI offers automatic, deep, latest-information, and public-social research modes, plus a live-test button. The model check sends one small completion request; optional social checks perform real public/API requests and can take longer. The response from `/api/agent` includes `answer`, `sources`, `search_queries`, `research_plan`, `search_report`, `used_web_search`, `used_social_search`, `used_language_model`, and any warnings. The request can pass `mode` as `auto`, `deep`, `latest`, or `social`. The report records planned and attempted queries, unique result count, pages read, providers, platform breakdown, citation-range checks and whether an optional second-pass consistency review completed. That second pass uses the same configured model/provider and is not independent fact verification. URL syntax and resolved private/local addresses are checked before page fetches; public redirects are followed only through a small bounded loop with each destination revalidated. Search engines may still return inaccessible, stale or noisy results, which the agent must disclose."`` | — |
| [SRC-B335630551-L000175](../../README.md#L175) | 175 | `""` | — |
| [SRC-B335630551-L000176](../../README.md#L176) | 176 | `"## Existing lead workspace"` | — |
| [SRC-B335630551-L000177](../../README.md#L177) | 177 | `""` | — |
| [SRC-B335630551-L000178](../../README.md#L178) | 178 | ``"The previous local lead-intent tool is preserved at `/leads`. It stores data locally in `~/.omarai/omarai.sqlite3`. Its transparent rule score is not a statistical probability of a purchase. Process only public/authorized data, minimize personal information, and manually review business decisions."`` | — |
| [SRC-B335630551-L000179](../../README.md#L179) | 179 | `""` | — |
| [SRC-B335630551-L000180](../../README.md#L180) | 180 | `"Analyze text from the CLI:"` | — |
| [SRC-B335630551-L000181](../../README.md#L181) | 181 | `""` | — |
| [SRC-B335630551-L000182](../../README.md#L182) | 182 | ````"```bash"```` | — |
| [SRC-B335630551-L000183](../../README.md#L183) | 183 | `"python -m cli.omarai analyze --text \"بدور على شقة في التجمع الخامس وممكن معاينة\" --product \"شقة,عقار\" --location \"التجمع الخامس\""` | — |
| [SRC-B335630551-L000184](../../README.md#L184) | 184 | ````"```"```` | — |
| [SRC-B335630551-L000185](../../README.md#L185) | 185 | `""` | — |
| [SRC-B335630551-L000186](../../README.md#L186) | 186 | ``"CSV import requires `text,source_url,platform` columns:"`` | — |
| [SRC-B335630551-L000187](../../README.md#L187) | 187 | `""` | — |
| [SRC-B335630551-L000188](../../README.md#L188) | 188 | ````"```bash"```` | — |
| [SRC-B335630551-L000189](../../README.md#L189) | 189 | `"python -m cli.omarai import-csv --file leads.csv"` | — |
| [SRC-B335630551-L000190](../../README.md#L190) | 190 | `"python -m cli.omarai list --limit 50"` | — |
| [SRC-B335630551-L000191](../../README.md#L191) | 191 | `"python -m cli.omarai export-csv --file leads-export.csv"` | — |
| [SRC-B335630551-L000192](../../README.md#L192) | 192 | ````"```"```` | — |
| [SRC-B335630551-L000193](../../README.md#L193) | 193 | `""` | — |
| [SRC-B335630551-L000194](../../README.md#L194) | 194 | `"## Checks"` | — |
| [SRC-B335630551-L000195](../../README.md#L195) | 195 | `""` | — |
| [SRC-B335630551-L000196](../../README.md#L196) | 196 | ````"```bash"```` | — |
| [SRC-B335630551-L000197](../../README.md#L197) | 197 | `"python -m pip install -e \".[dev]\""` | — |
| [SRC-B335630551-L000198](../../README.md#L198) | 198 | `"ruff check agents api cli tests"` | — |
| [SRC-B335630551-L000199](../../README.md#L199) | 199 | `"python -m pytest -q"` | — |
| [SRC-B335630551-L000200](../../README.md#L200) | 200 | ````"```"```` | — |
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
