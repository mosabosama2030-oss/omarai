# MASTER INDEX — Omarai

<!-- هذا الملف مُولَّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

> حالة التوثيق هنا تعني وجود Docstring غير فارغة فقط؛ ولا تُقيّم دقتها أو كفايتها.
> يعرض عمود الوصف أول فقرة من الـDocstring للمحافظة على سهولة قراءة الفهرس.

## ملخص الفهرسة

- ملفات Python المفحوصة: **36**
- الدوال والكلاسات المفهرسة: **612**
- موثق بوجود Docstring: **115**
- ناقص Docstring: **497**

## سجل الدوال والكلاسات

| الملف | النوع | اسم الدالة / الكلاس | الوصف | حالة التوثيق | السطر |
|---|---|---|---|---|---:|
| agents/intent_router.py | دالة | _normalize | لا توجد Docstring. | ناقص | 62 |
| agents/intent_router.py | دالة | _is_smalltalk | لا توجد Docstring. | ناقص | 72 |
| agents/intent_router.py | دالة | _has_context | Check whether the latest user turn can plausibly anchor a short follow-up. | موثق | 84 |
| agents/intent_router.py | دالة | _has_live_signal | Recognize common time-sensitive or explicit-search requests without a model. | موثق | 106 |
| agents/intent_router.py | دالة | _is_lead_generation_request | Recognize an explicit request to discover prospective buyers/customers. | موثق | 124 |
| agents/intent_router.py | دالة | _needs_clarification | لا توجد Docstring. | ناقص | 151 |
| agents/intent_router.py | دالة | _is_deep | لا توجد Docstring. | ناقص | 165 |
| agents/intent_router.py | دالة | _is_page_summarization_request | Recognize a request to summarize a specific web page or link. | موثق | 182 |
| agents/intent_router.py | دالة | _has_inline_summary_text | Detect text explicitly pasted after a summary instruction, not a web page URL. | موثق | 199 |
| agents/intent_router.py | دالة | route_intent | Return a deterministic route and auditable reason for a user question. | موثق | 225 |
| agents/omarai.py | دالة | normalize | لا توجد Docstring. | ناقص | 24 |
| agents/omarai.py | دالة | now_utc | لا توجد Docstring. | ناقص | 29 |
| agents/omarai.py | دالة | _csv_safe_cell | Prefix spreadsheet formulas even when hidden whitespace/control chars precede them. | موثق | 32 |
| agents/omarai.py | دالة | analyze | لا توجد Docstring. | ناقص | 51 |
| agents/omarai.py | دالة | validate_url | لا توجد Docstring. | ناقص | 73 |
| agents/omarai.py | كلاس | LeadStore | لا توجد Docstring. | ناقص | 81 |
| agents/omarai.py | دالة | LeadStore.__init__ | لا توجد Docstring. | ناقص | 82 |
| agents/omarai.py | دالة | LeadStore.connect | لا توجد Docstring. | ناقص | 92 |
| agents/omarai.py | دالة | LeadStore.add | لا توجد Docstring. | ناقص | 96 |
| agents/omarai.py | دالة | LeadStore.to_dict | لا توجد Docstring. | ناقص | 115 |
| agents/omarai.py | دالة | LeadStore.list | لا توجد Docstring. | ناقص | 119 |
| agents/omarai.py | دالة | LeadStore.update_status | لا توجد Docstring. | ناقص | 124 |
| agents/omarai.py | دالة | LeadStore.import_csv | لا توجد Docstring. | ناقص | 132 |
| agents/omarai.py | دالة | LeadStore.export_csv | لا توجد Docstring. | ناقص | 146 |
| agents/request_budget.py | كلاس | RequestBudgetExceeded | Raised when a request cannot start more work within its resource budget. | موثق | 17 |
| agents/request_budget.py | دالة | _bounded_env_int | لا توجد Docstring. | ناقص | 32 |
| agents/request_budget.py | كلاس | RequestBudget | Thread-safe counters and a cooperative monotonic deadline for one answer. | موثق | 41 |
| agents/request_budget.py | دالة | RequestBudget.__init__ | لا توجد Docstring. | ناقص | 44 |
| agents/request_budget.py | دالة | RequestBudget.from_environment | لا توجد Docstring. | ناقص | 64 |
| agents/request_budget.py | دالة | RequestBudget.remaining_seconds | لا توجد Docstring. | ناقص | 82 |
| agents/request_budget.py | دالة | RequestBudget.timeout_for | Cap one outbound timeout to time remaining; raise instead of starting at zero. | موثق | 85 |
| agents/request_budget.py | دالة | RequestBudget.remaining_units | Return unused units for a resource; zero means disabled, exhausted, or expired. | موثق | 94 |
| agents/request_budget.py | دالة | RequestBudget.reserve | Atomically reserve resource units before initiating external work. | موثق | 103 |
| agents/request_budget.py | دالة | RequestBudget.snapshot | لا توجد Docstring. | ناقص | 121 |
| agents/research.py | دالة | registrable_domain | Return a normalized registrable domain (or normalized IP/unknown hostname). | موثق | 31 |
| agents/research.py | دالة | extract_urls | Extract explicit HTTP(S) URLs without trying to interpret their content as instructions. | موثق | 99 |
| agents/research.py | دالة | _compact | لا توجد Docstring. | ناقص | 112 |
| agents/research.py | دالة | _normalize_arabic | لا توجد Docstring. | ناقص | 121 |
| agents/research.py | دالة | _contains_any | لا توجد Docstring. | ناقص | 131 |
| agents/research.py | دالة | detect_social_focus | لا توجد Docstring. | ناقص | 149 |
| agents/research.py | دالة | detect_freshness | لا توجد Docstring. | ناقص | 156 |
| agents/research.py | دالة | detect_depth | لا توجد Docstring. | ناقص | 160 |
| agents/research.py | دالة | mentioned_social_platforms | لا توجد Docstring. | ناقص | 164 |
| agents/research.py | دالة | _followup_query | لا توجد Docstring. | ناقص | 180 |
| agents/research.py | دالة | fallback_plan | Build a small but varied plan when no model planner is configured or parsing fails. | موثق | 199 |
| agents/research.py | دالة | validate_plan | لا توجد Docstring. | ناقص | 254 |
| agents/research.py | دالة | _canonical_result_url | لا توجد Docstring. | ناقص | 294 |
| agents/research.py | دالة | classify_source | لا توجد Docstring. | ناقص | 313 |
| agents/research.py | دالة | fuse_ranked_results | Reciprocal-rank-fuse result sets across queries/providers and dedupe URLs. | موثق | 346 |
| agents/research.py | دالة | _parse_publication_date | Parse common search/RSS publication dates without guessing missing dates. | موثق | 415 |
| agents/research.py | دالة | evidence_signal_report | Summarize research coverage; signals describe evidence coverage, not factual truth. | موثق | 457 |
| agents/research.py | دالة | _tokenize | لا توجد Docstring. | ناقص | 563 |
| agents/research.py | دالة | source_relevance_score | لا توجد Docstring. | ناقص | 571 |
| agents/research.py | دالة | filter_relevant_sources | لا توجد Docstring. | ناقص | 605 |
| agents/research.py | دالة | decide_evidence_status | لا توجد Docstring. | ناقص | 642 |
| agents/web_agent.py | دالة | _normalize_search_query | Normalize Arabic letters/diacritics while preserving search operators and dates. | موثق | 102 |
| agents/web_agent.py | دالة | _search_tokens | Tokenize Arabic/English text and expand a small bilingual vocabulary. | موثق | 119 |
| agents/web_agent.py | دالة | _relevance_ratio | Fraction of meaningful query concepts present in a candidate's title/snippet. | موثق | 142 |
| agents/web_agent.py | دالة | _blocked_source_url | لا توجد Docstring. | ناقص | 166 |
| agents/web_agent.py | كلاس | AgentDependencyError | A required optional runtime dependency is unavailable. | موثق | 174 |
| agents/web_agent.py | دالة | _clean_text | لا توجد Docstring. | ناقص | 178 |
| agents/web_agent.py | دالة | _public_http_url | Lexically validate an HTTP URL before using it as a search source. | موثق | 184 |
| agents/web_agent.py | دالة | _public_ip_literals | Resolve host and return its public addresses. | موثق | 211 |
| agents/web_agent.py | دالة | _host_resolves_publicly | Reject local/private destinations before fetching a third-party page. | موثق | 241 |
| agents/web_agent.py | دالة | _pinned_connect_url | Rewrite a validated public URL so the connection target is a checked IP. | موثق | 246 |
| agents/web_agent.py | دالة | _fallback_answer | لا توجد Docstring. | ناقص | 256 |
| agents/web_agent.py | كلاس | WebAgent | Search, inspect, and synthesize web evidence for open-ended questions. | موثق | 269 |
| agents/web_agent.py | دالة | WebAgent.__init__ | لا توجد Docstring. | ناقص | 272 |
| agents/web_agent.py | دالة | WebAgent._effective_timeout | Limit one outbound operation to the remaining per-answer time budget. | موثق | 315 |
| agents/web_agent.py | دالة | WebAgent.status | لا توجد Docstring. | ناقص | 323 |
| agents/web_agent.py | دالة | WebAgent._unwrap_search_url | لا توجد Docstring. | ناقص | 422 |
| agents/web_agent.py | دالة | WebAgent._record_provider_diagnostic | لا توجد Docstring. | ناقص | 435 |
| agents/web_agent.py | دالة | WebAgent._source_matches_query | لا توجد Docstring. | ناقص | 454 |
| agents/web_agent.py | دالة | WebAgent._normalized_source_url_key | Normalize a public HTTP(S) URL for duplicate detection across search rounds. | موثق | 464 |
| agents/web_agent.py | دالة | WebAgent._question_coverage_targets | Extract explicit multi-part answer requirements conservatively; this is not semantic grading. | موثق | 492 |
| agents/web_agent.py | دالة | WebAgent._is_current_search_status_question | Recognize a question about whether this answer already used web search. | موثق | 549 |
| agents/web_agent.py | دالة | WebAgent._is_self_question | Recognize questions about Omarai itself so they do not need web search. | موثق | 569 |
| agents/web_agent.py | دالة | WebAgent._is_navigation_request | A link-finding task can be useful with one clearly labelled candidate result. | موثق | 603 |
| agents/web_agent.py | دالة | WebAgent._is_lead_search | Keep lead discovery distinct from listing searches and generic explanations. | موثق | 613 |
| agents/web_agent.py | دالة | WebAgent._lead_intent_evidence | Return a narrow, inspectable public buyer-intent phrase signal, if present. | موثق | 618 |
| agents/web_agent.py | دالة | WebAgent._lead_generation_queries | Create high-intent buyer-search variants without changing the product/location. | موثق | 652 |
| agents/web_agent.py | دالة | WebAgent._is_listing_discovery | Recognize property/job/product discovery where candidates are useful with caveats. | موثق | 694 |
| agents/web_agent.py | دالة | WebAgent._requires_web_research | Use the web only when the user requests it or the answer depends on live data. | موثق | 714 |
| agents/web_agent.py | دالة | WebAgent._local_answer_result | Build a consistently shaped answer for non-research conversational requests. | موثق | 737 |
| agents/web_agent.py | دالة | WebAgent._local_conversation_reply | Return a short greeting/acknowledgment without a model or web request. | موثق | 760 |
| agents/web_agent.py | دالة | WebAgent._annotate_intent_route | Attach route diagnostics to both response and research-plan metadata. | موثق | 774 |
| agents/web_agent.py | دالة | WebAgent._clarification_result | Ask for a missing referent without calling the model or search providers. | موثق | 789 |
| agents/web_agent.py | دالة | WebAgent._capability_status_snapshot | Describe configured capabilities without claiming a live health check. | موثق | 808 |
| agents/web_agent.py | دالة | WebAgent._self_description_answer | Answer self/capability questions without inventing a live health result. | موثق | 889 |
| agents/web_agent.py | دالة | WebAgent._answer_without_search | Answer stable informational questions with the configured LLM, without fake citations. | موثق | 952 |
| agents/web_agent.py | دالة | WebAgent._search_duckduckgo_html | لا توجد Docstring. | ناقص | 1009 |
| agents/web_agent.py | دالة | WebAgent._search_bing_rss | لا توجد Docstring. | ناقص | 1057 |
| agents/web_agent.py | دالة | WebAgent._search_deepseek_api | Use DeepSeek's optional Search API as a comparison provider, never by default. | موثق | 1102 |
| agents/web_agent.py | دالة | WebAgent._reset_deepseek_search_budget | Reset the bounded optional Search API request budget for one operation. | موثق | 1158 |
| agents/web_agent.py | دالة | WebAgent._reserve_deepseek_search_request | Reserve one paid search request before concurrent queries invoke the provider. | موثق | 1163 |
| agents/web_agent.py | دالة | WebAgent._search_web | Run configured search connectors concurrently with isolated failures and relevance checks. | موثق | 1180 |
| agents/web_agent.py | دالة غير متزامنة | WebAgent._search_web.run_one | لا توجد Docstring. | ناقص | 1223 |
| agents/web_agent.py | دالة غير متزامنة | WebAgent._search_web.run_all | لا توجد Docstring. | ناقص | 1278 |
| agents/web_agent.py | دالة | WebAgent._reserve_search_call | Reserve one outbound search/social-provider request before network I/O. | موثق | 1296 |
| agents/web_agent.py | دالة | WebAgent._search_brave | Use Brave's official web-search API when the operator provides an API key. | موثق | 1302 |
| agents/web_agent.py | دالة | WebAgent._search_tavily | Use Tavily's official search API for structured, extractable live web results. | موثق | 1354 |
| agents/web_agent.py | دالة | WebAgent._search_news | Read the public Google News RSS search feed for freshness-sensitive queries. | موثق | 1407 |
| agents/web_agent.py | دالة | WebAgent._search_social | Search public social content through exposed public endpoints only. | موثق | 1475 |
| agents/web_agent.py | دالة | WebAgent._fetch_page | Fetch a public page with bounded, individually validated redirects and size limits. | موثق | 1955 |
| agents/web_agent.py | دالة | WebAgent._collect_sources | لا توجد Docstring. | ناقص | 2063 |
| agents/web_agent.py | دالة | WebAgent._collect_research | Run independent query searches concurrently, fuse evidence, then fetch top pages. | موثق | 2082 |
| agents/web_agent.py | دالة | WebAgent._sanitize_history | لا توجد Docstring. | ناقص | 2306 |
| agents/web_agent.py | دالة | WebAgent._history_search_query | لا توجد Docstring. | ناقص | 2319 |
| agents/web_agent.py | دالة | WebAgent._record_generation_diagnostic | Store bounded completion metadata without prompts, output text, or secrets. | موثق | 2339 |
| agents/web_agent.py | دالة | WebAgent._request_completion | Call an OpenAI-compatible API with bounded fallback and optional live server search. | موثق | 2360 |
| agents/web_agent.py | دالة | WebAgent._plan_search | Ask the language model how to search, then validate its proposal deterministically. | موثق | 2542 |
| agents/web_agent.py | دالة | WebAgent._generate | لا توجد Docstring. | ناقص | 2658 |
| agents/web_agent.py | دالة | WebAgent._review_answer | Run a bounded evidence audit on deep-research answers; not an independent verifier. | موثق | 2798 |
| agents/web_agent.py | دالة | WebAgent._remove_invalid_citations | Remove citation labels that point outside the exact source list sent to the model. | موثق | 2895 |
| agents/web_agent.py | دالة | WebAgent._remove_invalid_citations.replace | لا توجد Docstring. | ناقص | 2899 |
| agents/web_agent.py | دالة | WebAgent._citation_validation_metadata | Report the scope of citation checks without claiming semantic fact verification. | موثق | 2910 |
| agents/web_agent.py | دالة | WebAgent.diagnostics | Run explicit live checks without exposing credentials or retaining returned content. | موثق | 2940 |
| agents/web_agent.py | دالة | WebAgent.answer | Run one answer with an isolated, observable resource budget. | موثق | 3161 |
| agents/web_agent.py | دالة | WebAgent._answer_with_budget | لا توجد Docstring. | ناقص | 3245 |
| api/omarai.py | كلاس | _DeadlineRequestReader | Read HTTP header lines with one absolute deadline across all fragments. | موثق | 35 |
| api/omarai.py | دالة | _DeadlineRequestReader.__init__ | لا توجد Docstring. | ناقص | 44 |
| api/omarai.py | دالة | _DeadlineRequestReader.readline | لا توجد Docstring. | ناقص | 49 |
| api/omarai.py | دالة | _DeadlineRequestReader.read1 | Read one chunk; body code applies its own idle and absolute deadlines. | موثق | 100 |
| api/omarai.py | دالة | _DeadlineRequestReader.close | لا توجد Docstring. | ناقص | 113 |
| api/omarai.py | دالة | _configured_agent_concurrency_limit | Return a process-local cap for expensive research and diagnostics operations. | موثق | 118 |
| api/omarai.py | كلاس | Handler | لا توجد Docstring. | ناقص | 127 |
| api/omarai.py | دالة | Handler.setup | Install a reader with a strict deadline for the request line and headers. | موثق | 128 |
| api/omarai.py | دالة | Handler.handle_one_request | لا توجد Docstring. | ناقص | 137 |
| api/omarai.py | دالة | Handler._run_bounded_agent_operation | Run an expensive operation only when a process-local slot is available. | موثق | 165 |
| api/omarai.py | دالة | Handler._authorized | لا توجد Docstring. | ناقص | 182 |
| api/omarai.py | دالة | Handler._allowed_origins | Return configured browser origins plus this service’s own origin. | موثق | 191 |
| api/omarai.py | دالة | Handler._origin_allowed | لا توجد Docstring. | ناقص | 221 |
| api/omarai.py | دالة | Handler._rate_limit_client_key | Choose a rate-limit identity without trusting spoofable proxy headers by default. | موثق | 224 |
| api/omarai.py | دالة | Handler._rate_limit_ok | لا توجد Docstring. | ناقص | 240 |
| api/omarai.py | دالة | Handler._read_request_body | Read a bounded body with both idle and absolute wall-clock deadlines. | موثق | 265 |
| api/omarai.py | دالة | Handler.respond | لا توجد Docstring. | ناقص | 336 |
| api/omarai.py | دالة | Handler.do_GET | لا توجد Docstring. | ناقص | 350 |
| api/omarai.py | دالة | Handler.do_POST | لا توجد Docstring. | ناقص | 384 |
| api/omarai.py | دالة | Handler.do_OPTIONS | لا توجد Docstring. | ناقص | 473 |
| api/omarai.py | دالة | Handler.log_message | لا توجد Docstring. | ناقص | 486 |
| api/omarai.py | دالة | answer_question | Answer common operational questions from local records using explicit rules. | موثق | 490 |
| api/omarai.py | دالة | serve | لا توجد Docstring. | ناقص | 526 |
| cli/omarai.py | دالة | main | لا توجد Docstring. | ناقص | 9 |
| docs/generate_index.py | كلاس | IndexedSymbol | Represent a class or function discovered in a Python source file. | موثق | 41 |
| docs/generate_index.py | كلاس | IndexGenerationError | Signal that a complete and trustworthy index could not be generated. | موثق | 52 |
| docs/generate_index.py | كلاس | SymbolVisitor | Collect classes, functions, methods, and their docstring summaries. | موثق | 56 |
| docs/generate_index.py | دالة | SymbolVisitor.__init__ | Initialize the visitor for one repository-relative Python file. | موثق | 59 |
| docs/generate_index.py | دالة | SymbolVisitor._description | Return a compact first-paragraph summary and its documentation state. | موثق | 66 |
| docs/generate_index.py | دالة | SymbolVisitor._record | Record one definition while preserving its qualified scope. | موثق | 78 |
| docs/generate_index.py | دالة | SymbolVisitor.visit_ClassDef | Record a class and recursively inspect its body. | موثق | 97 |
| docs/generate_index.py | دالة | SymbolVisitor.visit_FunctionDef | Record a synchronous function or method and nested definitions. | موثق | 106 |
| docs/generate_index.py | دالة | SymbolVisitor.visit_AsyncFunctionDef | Record an asynchronous function or method and nested definitions. | موثق | 115 |
| docs/generate_index.py | دالة | discover_python_files | Return sorted repository-local Python files, excluding generated environments. | موثق | 125 |
| docs/generate_index.py | دالة | scan_repository | Parse every eligible Python file or fail without producing a partial index. | موثق | 153 |
| docs/generate_index.py | دالة | _markdown_cell | Normalize text and escape Markdown table delimiters. | موثق | 196 |
| docs/generate_index.py | دالة | render_markdown | Render a stable Markdown index; documentation means a non-empty docstring exists. | موثق | 203 |
| docs/generate_index.py | دالة | write_if_changed | Write atomically only when the generated index differs from the existing file. | موثق | 263 |
| docs/generate_index.py | دالة | main | Run indexing from the selected repository root and report changes clearly. | موثق | 292 |
| scripts/hosted_smoke_test.py | كلاس | SmokeError | A live acceptance check failed. | موثق | 15 |
| scripts/hosted_smoke_test.py | كلاس | _SameOriginRedirectHandler | Never forward a bearer token to a different origin during an HTTP redirect. | موثق | 19 |
| scripts/hosted_smoke_test.py | دالة | _SameOriginRedirectHandler._origin | لا توجد Docstring. | ناقص | 23 |
| scripts/hosted_smoke_test.py | دالة | _SameOriginRedirectHandler.redirect_request | لا توجد Docstring. | ناقص | 33 |
| scripts/hosted_smoke_test.py | دالة | normalize_origin | لا توجد Docstring. | ناقص | 48 |
| scripts/hosted_smoke_test.py | دالة | request_json | لا توجد Docstring. | ناقص | 72 |
| scripts/hosted_smoke_test.py | دالة | run_smoke | لا توجد Docstring. | ناقص | 99 |
| scripts/hosted_smoke_test.py | دالة | main | لا توجد Docstring. | ناقص | 172 |
| scripts/run_answer_quality_benchmark.py | دالة | validate_base_url | Validate and normalize an API origin before any request can carry a token. | موثق | 42 |
| scripts/run_answer_quality_benchmark.py | كلاس | _NoRedirectHandler | Do not follow redirects; the bearer token must never move to another origin. | موثق | 91 |
| scripts/run_answer_quality_benchmark.py | دالة | _NoRedirectHandler.redirect_request | لا توجد Docstring. | ناقص | 94 |
| scripts/run_answer_quality_benchmark.py | دالة | _utc_now | لا توجد Docstring. | ناقص | 116 |
| scripts/run_answer_quality_benchmark.py | دالة | load_corpus | لا توجد Docstring. | ناقص | 120 |
| scripts/run_answer_quality_benchmark.py | دالة | validate_corpus | Return a list of human-readable problems (empty => OK). | موثق | 131 |
| scripts/run_answer_quality_benchmark.py | دالة | redact_secrets | Best-effort redaction of common secret patterns from stored outputs. | موثق | 164 |
| scripts/run_answer_quality_benchmark.py | دالة | post_agent | لا توجد Docstring. | ناقص | 187 |
| scripts/run_answer_quality_benchmark.py | دالة | run_validate | لا توجد Docstring. | ناقص | 226 |
| scripts/run_answer_quality_benchmark.py | دالة | run_live | لا توجد Docstring. | ناقص | 253 |
| scripts/run_answer_quality_benchmark.py | دالة | main | لا توجد Docstring. | ناقص | 359 |
| scripts/sqlite_backup_restore.py | كلاس | BackupError | Raised when a backup/restore operation cannot be proven safe. | موثق | 15 |
| scripts/sqlite_backup_restore.py | دالة | _open_read_only | Open an existing SQLite database without accidentally creating a missing source. | موثق | 19 |
| scripts/sqlite_backup_restore.py | دالة | _validate_omarai_database | Require a healthy SQLite file containing the Omarai leads table. | موثق | 27 |
| scripts/sqlite_backup_restore.py | دالة | _create_destination_exclusively | Create a new destination without overwriting an existing file or following its symlink. | موثق | 46 |
| scripts/sqlite_backup_restore.py | دالة | _copy_verified_database | لا توجد Docstring. | ناقص | 59 |
| scripts/sqlite_backup_restore.py | دالة | backup_database | Create a consistent SQLite snapshot of a healthy Omarai leads database. | موثق | 105 |
| scripts/sqlite_backup_restore.py | دالة | restore_database | Restore a snapshot into a new destination; existing files are never overwritten. | موثق | 110 |
| scripts/sqlite_backup_restore.py | دالة | main | لا توجد Docstring. | ناقص | 115 |
| tests/test_agent_modes.py | دالة | test_deep_mode_expands_search_angles_and_returns_coverage_signals | لا توجد Docstring. | ناقص | 7 |
| tests/test_agent_modes.py | دالة | test_deep_mode_expands_search_angles_and_returns_coverage_signals.plan | لا توجد Docstring. | ناقص | 12 |
| tests/test_agent_modes.py | دالة | test_deep_mode_expands_search_angles_and_returns_coverage_signals.collect | لا توجد Docstring. | ناقص | 39 |
| tests/test_answer_quality_corpus.py | دالة | _load_corpus | لا توجد Docstring. | ناقص | 78 |
| tests/test_answer_quality_corpus.py | دالة | test_corpus_file_loads_as_utf8_json | لا توجد Docstring. | ناقص | 88 |
| tests/test_answer_quality_corpus.py | دالة | test_minimum_case_count | لا توجد Docstring. | ناقص | 95 |
| tests/test_answer_quality_corpus.py | دالة | test_case_ids_unique_and_shaped | لا توجد Docstring. | ناقص | 101 |
| tests/test_answer_quality_corpus.py | دالة | test_required_fields_and_types | لا توجد Docstring. | ناقص | 110 |
| tests/test_answer_quality_corpus.py | دالة | test_required_theme_categories_represented | لا توجد Docstring. | ناقص | 135 |
| tests/test_answer_quality_corpus.py | دالة | test_no_empty_or_exact_duplicate_questions | لا توجد Docstring. | ناقص | 142 |
| tests/test_answer_quality_corpus.py | دالة | test_research_cases_declare_fixture_or_controlled_env | لا توجد Docstring. | ناقص | 154 |
| tests/test_answer_quality_corpus.py | دالة | test_safety_categories_include_injection_and_secrets | لا توجد Docstring. | ناقص | 172 |
| tests/test_answer_quality_corpus.py | دالة | test_corpus_does_not_claim_live_execution_results | لا توجد Docstring. | ناقص | 188 |
| tests/test_answer_quality_corpus.py | دالة | test_languages_include_arabic_english_and_mixed | لا توجد Docstring. | ناقص | 196 |
| tests/test_answer_quality_corpus.py | دالة | test_documented_high_risk_examples_match_json_categories | لا توجد Docstring. | ناقص | 206 |
| tests/test_answer_quality_corpus.py | دالة | test_docs_mention_corrected_high_risk_ids | لا توجد Docstring. | ناقص | 218 |
| tests/test_answer_quality_corpus.py | دالة | test_no_placeholder_corpus_content | لا توجد Docstring. | ناقص | 225 |
| tests/test_answer_quality_runner.py | دالة | _load_runner | لا توجد Docstring. | ناقص | 16 |
| tests/test_answer_quality_runner.py | دالة | test_runner_script_exists | لا توجد Docstring. | ناقص | 25 |
| tests/test_answer_quality_runner.py | دالة | test_validate_mode_succeeds_on_real_corpus | لا توجد Docstring. | ناقص | 29 |
| tests/test_answer_quality_runner.py | دالة | test_validate_rejects_missing_file | لا توجد Docstring. | ناقص | 38 |
| tests/test_answer_quality_runner.py | دالة | test_validate_detects_bad_case_count | لا توجد Docstring. | ناقص | 45 |
| tests/test_answer_quality_runner.py | دالة | test_validate_detects_missing_required_field | لا توجد Docstring. | ناقص | 55 |
| tests/test_answer_quality_runner.py | دالة | test_live_refuses_unbounded_without_limit_or_case_id | لا توجد Docstring. | ناقص | 67 |
| tests/test_answer_quality_runner.py | دالة | test_live_unknown_case_id | لا توجد Docstring. | ناقص | 75 |
| tests/test_answer_quality_runner.py | دالة | test_redact_secrets_strips_token_value | لا توجد Docstring. | ناقص | 92 |
| tests/test_answer_quality_runner.py | دالة | test_live_records_not_tested_not_pass | Even on HTTP 200, quality status stays NOT_TESTED (no keyword auto-PASS). | موثق | 101 |
| tests/test_answer_quality_runner.py | دالة | test_live_records_not_tested_not_pass.fake_post | لا توجد Docstring. | ناقص | 105 |
| tests/test_answer_quality_runner.py | دالة | test_validate_base_url_rejects_non_loopback_http | لا توجد Docstring. | ناقص | 136 |
| tests/test_answer_quality_runner.py | دالة | test_validate_base_url_rejects_ambiguous_or_credential_bearing_urls | لا توجد Docstring. | ناقص | 151 |
| tests/test_answer_quality_runner.py | دالة | test_remote_bearer_token_requires_exact_allowlisted_https_origin | لا توجد Docstring. | ناقص | 157 |
| tests/test_answer_quality_runner.py | دالة | test_remote_token_origin_comparison_normalizes_default_https_port | لا توجد Docstring. | ناقص | 169 |
| tests/test_answer_quality_runner.py | دالة | test_redirect_handler_refuses_following_redirects | لا توجد Docstring. | ناقص | 178 |
| tests/test_answer_quality_runner.py | دالة | test_live_rejects_unapproved_remote_url_before_network | لا توجد Docstring. | ناقص | 191 |
| tests/test_answer_quality_runner.py | دالة | test_live_transport_error_still_not_pass | لا توجد Docstring. | ناقص | 208 |
| tests/test_answer_quality_runner.py | دالة | test_live_transport_error_still_not_pass.fake_post | لا توجد Docstring. | ناقص | 211 |
| tests/test_api.py | دالة | local_api | Run the real handler on an ephemeral loopback port with an isolated database. | موثق | 20 |
| tests/test_api.py | دالة | request_json | لا توجد Docstring. | ناقص | 36 |
| tests/test_api.py | دالة | test_api_health_analyze_save_duplicate_list_and_status | لا توجد Docstring. | ناقص | 49 |
| tests/test_api.py | دالة | test_api_rejects_invalid_filters_and_request_shapes | لا توجد Docstring. | ناقص | 120 |
| tests/test_api.py | دالة | test_api_blocks_non_json_and_cross_origin_posts | لا توجد Docstring. | ناقص | 146 |
| tests/test_api.py | دالة | test_configured_frontend_origin_supports_preflight_and_post | لا توجد Docstring. | ناقص | 169 |
| tests/test_api.py | دالة | test_preflight_rejects_unconfigured_origin | لا توجد Docstring. | ناقص | 202 |
| tests/test_api.py | دالة | test_ask_is_honest_when_database_is_empty | لا توجد Docstring. | ناقص | 217 |
| tests/test_api.py | دالة | test_web_agent_endpoint_uses_agent_result | لا توجد Docstring. | ناقص | 227 |
| tests/test_api.py | دالة | test_web_agent_endpoint_uses_agent_result.fake_answer | لا توجد Docstring. | ناقص | 230 |
| tests/test_api.py | دالة | test_live_diagnostics_endpoint_returns_report_without_secrets | لا توجد Docstring. | ناقص | 255 |
| tests/test_api.py | دالة | test_live_diagnostics_endpoint_returns_report_without_secrets.fake_diagnostics | لا توجد Docstring. | ناقص | 258 |
| tests/test_api.py | دالة | test_diagnostics_endpoint_requires_boolean_options | لا توجد Docstring. | ناقص | 287 |
| tests/test_api.py | دالة | test_rate_limit_ignores_spoofed_forwarded_for_by_default | لا توجد Docstring. | ناقص | 299 |
| tests/test_api.py | دالة | test_rate_limit_uses_rightmost_valid_proxy_ip_only_when_enabled | لا توجد Docstring. | ناقص | 308 |
| tests/test_api.py | دالة | test_rate_limit_proxy_header_invalid_value_falls_back_to_peer_ip | لا توجد Docstring. | ناقص | 317 |
| tests/test_api.py | دالة | test_public_api_authentication_and_rate_limit_precede_json_parsing | Reject untrusted API calls before parsing bodies and throttle repeated failures. | موثق | 326 |
| tests/test_api.py | دالة | test_hosted_api_requires_private_token_for_search_and_lead_data | لا توجد Docstring. | ناقص | 354 |
| tests/test_api.py | دالة | test_hosted_api_rate_limits_authenticated_requests | لا توجد Docstring. | ناقص | 379 |
| tests/test_api.py | دالة | test_public_binding_requires_explicit_deployment_flag_and_strong_token | لا توجد Docstring. | ناقص | 400 |
| tests/test_api.py | دالة | test_rate_limiter_prunes_expired_client_buckets | Client IPs do not accumulate forever after their 60-second window expires. | موثق | 413 |
| tests/test_api.py | كلاس | test_rate_limiter_prunes_expired_client_buckets.FakeHandler | لا توجد Docstring. | ناقص | 421 |
| tests/test_api.py | دالة | test_rate_limiter_prunes_expired_client_buckets.FakeHandler.__init__ | لا توجد Docstring. | ناقص | 422 |
| tests/test_api.py | دالة | test_agent_concurrency_cap_rejects_work_when_all_slots_are_busy | لا توجد Docstring. | ناقص | 438 |
| tests/test_api.py | دالة | test_agent_concurrency_cap_rejects_work_when_all_slots_are_busy.slow_answer | لا توجد Docstring. | ناقص | 451 |
| tests/test_api.py | دالة | test_agent_concurrency_cap_rejects_work_when_all_slots_are_busy.first_request | لا توجد Docstring. | ناقص | 471 |
| tests/test_api.py | دالة | test_agent_concurrency_limit_has_hard_bounds | لا توجد Docstring. | ناقص | 494 |
| tests/test_api.py | دالة | test_api_rejects_oversized_request_body | لا توجد Docstring. | ناقص | 503 |
| tests/test_api.py | دالة | test_api_rejects_malformed_content_length | لا توجد Docstring. | ناقص | 515 |
| tests/test_api.py | دالة | test_api_returns_408_when_request_body_read_times_out | لا توجد Docstring. | ناقص | 538 |
| tests/test_api.py | دالة | test_api_absolute_body_deadline_stops_slow_trickle | A client must not evade the total deadline by sending before each idle timeout. | موثق | 564 |
| tests/test_api.py | دالة | test_api_absolute_header_deadline_stops_slow_trickle | Header bytes arriving before idle timeout must not extend the total deadline. | موثق | 611 |
| tests/test_dashboard_security.py | دالة | test_hosted_lead_dashboard_can_send_the_private_access_token | لا توجد Docstring. | ناقص | 7 |
| tests/test_dashboard_security.py | دالة | test_saved_lead_source_links_reject_non_http_schemes | لا توجد Docstring. | ناقص | 14 |
| tests/test_evidence_provenance.py | دالة | _addrinfo | لا توجد Docstring. | ناقص | 11 |
| tests/test_evidence_provenance.py | دالة | test_failed_page_read_is_not_reported_as_fetched | An empty extraction must not set page_fetched through the real collector. | موثق | 16 |
| tests/test_evidence_provenance.py | دالة | test_failed_page_read_is_not_reported_as_fetched.search | لا توجد Docstring. | ناقص | 20 |
| tests/test_evidence_provenance.py | دالة | test_openrouter_citations_stay_unread_in_public_answer | Server-side citations must not be misreported as direct source-page reads. | موثق | 55 |
| tests/test_evidence_provenance.py | دالة | test_openrouter_citations_stay_unread_in_public_answer.collect | لا توجد Docstring. | ناقص | 61 |
| tests/test_evidence_provenance.py | دالة | test_openrouter_citations_stay_unread_in_public_answer.generate | لا توجد Docstring. | ناقص | 110 |
| tests/test_evidence_provenance.py | دالة | test_private_resolution_blocks_page_fetch | لا توجد Docstring. | ناقص | 148 |
| tests/test_evidence_provenance.py | دالة | test_private_resolution_blocks_page_fetch.fake_getaddrinfo | لا توجد Docstring. | ناقص | 151 |
| tests/test_evidence_provenance.py | كلاس | test_private_resolution_blocks_page_fetch.FakeClient | لا توجد Docstring. | ناقص | 154 |
| tests/test_evidence_provenance.py | دالة | test_private_resolution_blocks_page_fetch.FakeClient.__init__ | لا توجد Docstring. | ناقص | 155 |
| tests/test_evidence_provenance.py | دالة | test_private_resolution_blocks_page_fetch.FakeClient.__enter__ | لا توجد Docstring. | ناقص | 158 |
| tests/test_evidence_provenance.py | دالة | test_private_resolution_blocks_page_fetch.FakeClient.__exit__ | لا توجد Docstring. | ناقص | 161 |
| tests/test_evidence_provenance.py | دالة | test_private_resolution_blocks_page_fetch.FakeClient.stream | لا توجد Docstring. | ناقص | 164 |
| tests/test_evidence_provenance.py | دالة | test_page_fetch_connects_to_the_validated_public_ip | لا توجد Docstring. | ناقص | 175 |
| tests/test_evidence_provenance.py | دالة | test_page_fetch_connects_to_the_validated_public_ip.fake_getaddrinfo | لا توجد Docstring. | ناقص | 178 |
| tests/test_evidence_provenance.py | كلاس | test_page_fetch_connects_to_the_validated_public_ip.FakeResponse | لا توجد Docstring. | ناقص | 182 |
| tests/test_evidence_provenance.py | دالة | test_page_fetch_connects_to_the_validated_public_ip.FakeResponse.__init__ | لا توجد Docstring. | ناقص | 186 |
| tests/test_evidence_provenance.py | دالة | test_page_fetch_connects_to_the_validated_public_ip.FakeResponse.iter_bytes | لا توجد Docstring. | ناقص | 189 |
| tests/test_evidence_provenance.py | دالة | test_page_fetch_connects_to_the_validated_public_ip.FakeResponse.__enter__ | لا توجد Docstring. | ناقص | 192 |
| tests/test_evidence_provenance.py | دالة | test_page_fetch_connects_to_the_validated_public_ip.FakeResponse.__exit__ | لا توجد Docstring. | ناقص | 195 |
| tests/test_evidence_provenance.py | كلاس | test_page_fetch_connects_to_the_validated_public_ip.FakeClient | لا توجد Docstring. | ناقص | 198 |
| tests/test_evidence_provenance.py | دالة | test_page_fetch_connects_to_the_validated_public_ip.FakeClient.__init__ | لا توجد Docstring. | ناقص | 199 |
| tests/test_evidence_provenance.py | دالة | test_page_fetch_connects_to_the_validated_public_ip.FakeClient.__enter__ | لا توجد Docstring. | ناقص | 205 |
| tests/test_evidence_provenance.py | دالة | test_page_fetch_connects_to_the_validated_public_ip.FakeClient.__exit__ | لا توجد Docstring. | ناقص | 208 |
| tests/test_evidence_provenance.py | دالة | test_page_fetch_connects_to_the_validated_public_ip.FakeClient.stream | لا توجد Docstring. | ناقص | 211 |
| tests/test_evidence_provenance.py | دالة | test_mixed_public_and_private_dns_answers_block_page_fetch | A hostname is rejected when even one DNS answer is non-global. | موثق | 227 |
| tests/test_evidence_provenance.py | دالة | test_mixed_public_and_private_dns_answers_block_page_fetch.fake_getaddrinfo | لا توجد Docstring. | ناقص | 229 |
| tests/test_evidence_provenance.py | دالة | test_private_redirect_target_is_rejected_before_a_second_connection | Every redirect is validated independently, even after a pinned public request. | موثق | 236 |
| tests/test_evidence_provenance.py | دالة | test_private_redirect_target_is_rejected_before_a_second_connection.fake_getaddrinfo | لا توجد Docstring. | ناقص | 241 |
| tests/test_evidence_provenance.py | كلاس | test_private_redirect_target_is_rejected_before_a_second_connection.FakeResponse | لا توجد Docstring. | ناقص | 246 |
| tests/test_evidence_provenance.py | دالة | test_private_redirect_target_is_rejected_before_a_second_connection.FakeResponse.__init__ | لا توجد Docstring. | ناقص | 249 |
| tests/test_evidence_provenance.py | دالة | test_private_redirect_target_is_rejected_before_a_second_connection.FakeResponse.__enter__ | لا توجد Docstring. | ناقص | 252 |
| tests/test_evidence_provenance.py | دالة | test_private_redirect_target_is_rejected_before_a_second_connection.FakeResponse.__exit__ | لا توجد Docstring. | ناقص | 255 |
| tests/test_evidence_provenance.py | كلاس | test_private_redirect_target_is_rejected_before_a_second_connection.FakeClient | لا توجد Docstring. | ناقص | 258 |
| tests/test_evidence_provenance.py | دالة | test_private_redirect_target_is_rejected_before_a_second_connection.FakeClient.__init__ | لا توجد Docstring. | ناقص | 259 |
| tests/test_evidence_provenance.py | دالة | test_private_redirect_target_is_rejected_before_a_second_connection.FakeClient.__enter__ | لا توجد Docstring. | ناقص | 263 |
| tests/test_evidence_provenance.py | دالة | test_private_redirect_target_is_rejected_before_a_second_connection.FakeClient.__exit__ | لا توجد Docstring. | ناقص | 266 |
| tests/test_evidence_provenance.py | دالة | test_private_redirect_target_is_rejected_before_a_second_connection.FakeClient.stream | لا توجد Docstring. | ناقص | 269 |
| tests/test_evidence_provenance.py | دالة | test_non_global_ipv4_and_ipv6_dns_answers_are_rejected | No DNS answer from a non-global range may pass the page-fetch gate. | موثق | 298 |
| tests/test_evidence_signals.py | دالة | test_evidence_signal_report_uses_domain_provider_page_and_date_coverage | لا توجد Docstring. | ناقص | 8 |
| tests/test_evidence_signals.py | دالة | test_evidence_signal_report_warns_when_no_sources_are_available | لا توجد Docstring. | ناقص | 42 |
| tests/test_evidence_signals.py | دالة | test_publication_date_parser_handles_iso_rfc822_and_relative_dates | لا توجد Docstring. | ناقص | 50 |
| tests/test_generate_index.py | دالة | test_indexes_functions_classes_methods_and_docstring_status | The index includes qualified names and distinguishes documented from missing. | موثق | 20 |
| tests/test_generate_index.py | دالة | test_skips_virtual_environments_and_generated_dependency_directories | The scan avoids vendored dependencies, build outputs, and virtual environments. | موثق | 59 |
| tests/test_generate_index.py | دالة | test_syntax_error_does_not_overwrite_the_previous_index | A failed parse leaves the prior index intact rather than publishing partial data. | موثق | 82 |
| tests/test_generate_index.py | دالة | test_repeated_generation_is_deterministic_and_does_not_rewrite_unchanged_index | An unchanged scan produces identical Markdown and avoids an unnecessary write. | موثق | 103 |
| tests/test_generation_acceptance_matrix.py | كلاس | FakeCompletionResponse | لا توجد Docstring. | ناقص | 11 |
| tests/test_generation_acceptance_matrix.py | دالة | FakeCompletionResponse.__init__ | لا توجد Docstring. | ناقص | 12 |
| tests/test_generation_acceptance_matrix.py | دالة | FakeCompletionResponse.__enter__ | لا توجد Docstring. | ناقص | 24 |
| tests/test_generation_acceptance_matrix.py | دالة | FakeCompletionResponse.__exit__ | لا توجد Docstring. | ناقص | 27 |
| tests/test_generation_acceptance_matrix.py | دالة | FakeCompletionResponse.read | لا توجد Docstring. | ناقص | 30 |
| tests/test_generation_acceptance_matrix.py | دالة | source | لا توجد Docstring. | ناقص | 34 |
| tests/test_generation_acceptance_matrix.py | دالة | test_only_normal_stop_is_accepted_as_a_complete_text_answer | لا توجد Docstring. | ناقص | 63 |
| tests/test_generation_acceptance_matrix.py | دالة | test_both_models_truncated_fail_without_returning_either_partial_answer | لا توجد Docstring. | ناقص | 92 |
| tests/test_generation_acceptance_matrix.py | دالة | test_both_models_truncated_fail_without_returning_either_partial_answer.fake_urlopen | لا توجد Docstring. | ناقص | 98 |
| tests/test_generation_acceptance_matrix.py | دالة | test_model_fallback_cannot_exceed_request_model_call_budget | لا توجد Docstring. | ناقص | 120 |
| tests/test_generation_acceptance_matrix.py | دالة | test_model_fallback_cannot_exceed_request_model_call_budget.fake_urlopen | لا توجد Docstring. | ناقص | 128 |
| tests/test_generation_acceptance_matrix.py | دالة | test_capability_snapshot_separates_configuration_from_live_health | لا توجد Docstring. | ناقص | 147 |
| tests/test_generation_acceptance_matrix.py | دالة | test_capability_answer_discloses_optional_deepseek_search_status | لا توجد Docstring. | ناقص | 180 |
| tests/test_generation_acceptance_matrix.py | دالة | test_operational_truth_overrides_a_model_claim_about_this_request | لا توجد Docstring. | ناقص | 209 |
| tests/test_generation_acceptance_matrix.py | دالة | test_operational_truth_overrides_a_model_claim_about_this_request.dishonest_model | لا توجد Docstring. | ناقص | 213 |
| tests/test_generation_acceptance_matrix.py | دالة | test_generation_budget_exhaustion_preserves_partial_sources | لا توجد Docstring. | ناقص | 234 |
| tests/test_generation_acceptance_matrix.py | دالة | test_generation_budget_exhaustion_preserves_partial_sources.fake_urlopen | لا توجد Docstring. | ناقص | 293 |
| tests/test_generation_acceptance_matrix.py | دالة | test_review_budget_exhaustion_discards_draft_and_preserves_sources | لا توجد Docstring. | ناقص | 314 |
| tests/test_generation_acceptance_matrix.py | دالة | test_review_budget_exhaustion_discards_draft_and_preserves_sources.fake_urlopen | لا توجد Docstring. | ناقص | 373 |
| tests/test_generation_acceptance_matrix.py | دالة | test_search_failure_is_not_reported_as_no_attempt_or_completed_answer | لا توجد Docstring. | ناقص | 394 |
| tests/test_generation_acceptance_matrix.py | دالة | test_research_exception_does_not_claim_no_results_or_no_search | لا توجد Docstring. | ناقص | 449 |
| tests/test_generation_acceptance_matrix.py | دالة | test_research_exception_does_not_claim_no_results_or_no_search.collect_fails_before_diagnostics | لا توجد Docstring. | ناقص | 467 |
| tests/test_generation_acceptance_matrix.py | دالة | test_search_extraction_generation_and_task_review_remain_distinct | لا توجد Docstring. | ناقص | 488 |
| tests/test_generation_acceptance_matrix.py | دالة | test_reviewer_rejects_missing_or_unbounded_final_answer_delimiters | لا توجد Docstring. | ناقص | 569 |
| tests/test_generation_capabilities.py | كلاس | FakeResponse | لا توجد Docstring. | ناقص | 10 |
| tests/test_generation_capabilities.py | دالة | FakeResponse.__init__ | لا توجد Docstring. | ناقص | 11 |
| tests/test_generation_capabilities.py | دالة | FakeResponse.__enter__ | لا توجد Docstring. | ناقص | 17 |
| tests/test_generation_capabilities.py | دالة | FakeResponse.__exit__ | لا توجد Docstring. | ناقص | 20 |
| tests/test_generation_capabilities.py | دالة | FakeResponse.read | لا توجد Docstring. | ناقص | 23 |
| tests/test_generation_capabilities.py | دالة | test_missing_finish_reason_is_rejected_and_bounded_fallback_is_used | لا توجد Docstring. | ناقص | 27 |
| tests/test_generation_capabilities.py | دالة | test_missing_finish_reason_is_rejected_and_bounded_fallback_is_used.fake_urlopen | لا توجد Docstring. | ناقص | 33 |
| tests/test_generation_capabilities.py | دالة | test_unknown_finish_reason_is_rejected_and_fallback_is_used | لا توجد Docstring. | ناقص | 57 |
| tests/test_generation_capabilities.py | دالة | test_unknown_finish_reason_is_rejected_and_fallback_is_used.fake_urlopen | لا توجد Docstring. | ناقص | 63 |
| tests/test_generation_capabilities.py | دالة | test_missing_finish_reason_from_all_models_fails_closed | لا توجد Docstring. | ناقص | 83 |
| tests/test_generation_capabilities.py | دالة | test_missing_finish_reason_from_all_models_fails_closed.fake_urlopen | لا توجد Docstring. | ناقص | 89 |
| tests/test_generation_capabilities.py | دالة | test_capability_question_distinguishes_configuration_from_live_health | لا توجد Docstring. | ناقص | 110 |
| tests/test_generation_capabilities.py | دالة | test_current_request_search_status_is_not_confused_with_capability | لا توجد Docstring. | ناقص | 134 |
| tests/test_generation_capabilities.py | دالة | test_generation_failure_returns_partial_sources_and_diagnostics | لا توجد Docstring. | ناقص | 157 |
| tests/test_generation_capabilities.py | دالة | test_generation_failure_returns_partial_sources_and_diagnostics.failed_generate | لا توجد Docstring. | ناقص | 227 |
| tests/test_hosted_smoke.py | كلاس | Handler | لا توجد Docstring. | ناقص | 16 |
| tests/test_hosted_smoke.py | دالة | Handler.log_message | لا توجد Docstring. | ناقص | 17 |
| tests/test_hosted_smoke.py | دالة | Handler.respond | لا توجد Docstring. | ناقص | 20 |
| tests/test_hosted_smoke.py | دالة | Handler.do_GET | لا توجد Docstring. | ناقص | 28 |
| tests/test_hosted_smoke.py | دالة | Handler.do_POST | لا توجد Docstring. | ناقص | 34 |
| tests/test_hosted_smoke.py | دالة | hosted_server | لا توجد Docstring. | ناقص | 65 |
| tests/test_hosted_smoke.py | دالة | test_normalize_origin_requires_https_and_rejects_credentials_or_paths | لا توجد Docstring. | ناقص | 77 |
| tests/test_hosted_smoke.py | دالة | test_normalize_origin_allows_plain_http_only_for_local_test | لا توجد Docstring. | ناقص | 89 |
| tests/test_hosted_smoke.py | دالة | test_smoke_checks_health_auth_live_diagnostics_and_agent | لا توجد Docstring. | ناقص | 97 |
| tests/test_hosted_smoke.py | دالة | test_smoke_never_forwards_bearer_to_cross_origin_redirect | لا توجد Docstring. | ناقص | 106 |
| tests/test_hosted_smoke.py | كلاس | test_smoke_never_forwards_bearer_to_cross_origin_redirect.RedirectHandler | لا توجد Docstring. | ناقص | 109 |
| tests/test_hosted_smoke.py | دالة | test_smoke_never_forwards_bearer_to_cross_origin_redirect.RedirectHandler.log_message | لا توجد Docstring. | ناقص | 110 |
| tests/test_hosted_smoke.py | دالة | test_smoke_never_forwards_bearer_to_cross_origin_redirect.RedirectHandler.do_GET | لا توجد Docstring. | ناقص | 113 |
| tests/test_hosted_smoke.py | كلاس | test_smoke_never_forwards_bearer_to_cross_origin_redirect.DestinationHandler | لا توجد Docstring. | ناقص | 119 |
| tests/test_hosted_smoke.py | دالة | test_smoke_never_forwards_bearer_to_cross_origin_redirect.DestinationHandler.log_message | لا توجد Docstring. | ناقص | 120 |
| tests/test_hosted_smoke.py | دالة | test_smoke_never_forwards_bearer_to_cross_origin_redirect.DestinationHandler.do_GET | لا توجد Docstring. | ناقص | 123 |
| tests/test_hosted_smoke.py | دالة | test_smoke_refuses_missing_or_short_access_token | لا توجد Docstring. | ناقص | 156 |
| tests/test_hosted_smoke.py | دالة | test_smoke_fails_when_agent_returns_no_live_source | لا توجد Docstring. | ناقص | 161 |
| tests/test_hosted_smoke.py | دالة | test_smoke_fails_when_agent_returns_no_live_source.without_sources | لا توجد Docstring. | ناقص | 164 |
| tests/test_intent_router.py | دالة | test_deterministic_intent_routes | لا توجد Docstring. | ناقص | 23 |
| tests/test_intent_router.py | دالة | test_lead_generation_and_summarization_routes | لا توجد Docstring. | ناقص | 40 |
| tests/test_intent_router.py | دالة | test_generic_explanation_of_lead_generation_is_not_a_lead_search | لا توجد Docstring. | ناقص | 46 |
| tests/test_intent_router.py | دالة | test_capability_question_is_local | لا توجد Docstring. | ناقص | 52 |
| tests/test_intent_router.py | دالة | test_ambiguous_followup_uses_existing_conversation_context | لا توجد Docstring. | ناقص | 62 |
| tests/test_intent_router.py | دالة | test_comparison_followup_requires_context_before_deep_search | لا توجد Docstring. | ناقص | 73 |
| tests/test_intent_router.py | دالة | test_ambiguous_followup_does_not_reuse_stale_topic_after_acknowledgment | لا توجد Docstring. | ناقص | 81 |
| tests/test_intent_router.py | دالة | test_explicit_mode_overrides_conversational_shortcuts | لا توجد Docstring. | ناقص | 93 |
| tests/test_intent_router.py | دالة | test_summarization_routing_respects_page_text_and_missing_input | لا توجد Docstring. | ناقص | 119 |
| tests/test_intent_router_integration.py | دالة | _evidence | لا توجد Docstring. | ناقص | 9 |
| tests/test_intent_router_integration.py | دالة | _report | لا توجد Docstring. | ناقص | 26 |
| tests/test_intent_router_integration.py | دالة | test_greeting_is_local_without_model_or_search | لا توجد Docstring. | ناقص | 43 |
| tests/test_intent_router_integration.py | دالة | test_greeting_is_local_without_model_or_search.unexpected | لا توجد Docstring. | ناقص | 46 |
| tests/test_intent_router_integration.py | دالة | test_ambiguous_question_clarifies_without_model_or_search | لا توجد Docstring. | ناقص | 62 |
| tests/test_intent_router_integration.py | دالة | test_ambiguous_question_clarifies_without_model_or_search.unexpected | لا توجد Docstring. | ناقص | 65 |
| tests/test_intent_router_integration.py | دالة | test_contextual_price_followup_searches_with_previous_subject | لا توجد Docstring. | ناقص | 83 |
| tests/test_intent_router_integration.py | دالة | test_contextual_price_followup_searches_with_previous_subject.collect | لا توجد Docstring. | ناقص | 92 |
| tests/test_intent_router_integration.py | دالة | test_multi_part_comparison_forces_deep_plan_and_multiple_angles | لا توجد Docstring. | ناقص | 115 |
| tests/test_intent_router_integration.py | دالة | test_multi_part_comparison_forces_deep_plan_and_multiple_angles.plan | لا توجد Docstring. | ناقص | 121 |
| tests/test_intent_router_integration.py | دالة | test_multi_part_comparison_forces_deep_plan_and_multiple_angles.collect | لا توجد Docstring. | ناقص | 132 |
| tests/test_live_search_connectors.py | كلاس | FakeResponse | لا توجد Docstring. | ناقص | 8 |
| tests/test_live_search_connectors.py | دالة | FakeResponse.__init__ | لا توجد Docstring. | ناقص | 9 |
| tests/test_live_search_connectors.py | دالة | FakeResponse.raise_for_status | لا توجد Docstring. | ناقص | 13 |
| tests/test_live_search_connectors.py | دالة | FakeResponse.json | لا توجد Docstring. | ناقص | 16 |
| tests/test_live_search_connectors.py | دالة | test_brave_search_adapter_normalizes_real_api_response | لا توجد Docstring. | ناقص | 20 |
| tests/test_live_search_connectors.py | دالة | test_brave_search_adapter_normalizes_real_api_response.fake_get | لا توجد Docstring. | ناقص | 24 |
| tests/test_live_search_connectors.py | دالة | test_tavily_search_adapter_normalizes_live_search_results | لا توجد Docstring. | ناقص | 48 |
| tests/test_live_search_connectors.py | دالة | test_tavily_search_adapter_normalizes_live_search_results.fake_post | لا توجد Docstring. | ناقص | 52 |
| tests/test_live_search_connectors.py | دالة | test_search_api_setup_status_reports_only_presence_not_secret_values | لا توجد Docstring. | ناقص | 74 |
| tests/test_omarai.py | دالة | test_arabic_normalization | لا توجد Docstring. | ناقص | 8 |
| tests/test_omarai.py | دالة | test_high_intent_with_next_step | لا توجد Docstring. | ناقص | 11 |
| tests/test_omarai.py | دالة | test_non_buyer_override | لا توجد Docstring. | ناقص | 16 |
| tests/test_omarai.py | دالة | test_empty_text_rejected | لا توجد Docstring. | ناقص | 21 |
| tests/test_omarai.py | دالة | test_url_required_and_validated | لا توجد Docstring. | ناقص | 25 |
| tests/test_omarai.py | دالة | test_duplicate_is_idempotent | لا توجد Docstring. | ناقص | 32 |
| tests/test_omarai.py | دالة | test_status_updates_are_explicit | لا توجد Docstring. | ناقص | 40 |
| tests/test_omarai.py | دالة | test_csv_requires_columns | لا توجد Docstring. | ناقص | 48 |
| tests/test_omarai.py | دالة | test_csv_export_neutralizes_spreadsheet_formula_injection | لا توجد Docstring. | ناقص | 55 |
| tests/test_proxy_origin.py | دالة | port | لا توجد Docstring. | ناقص | 14 |
| tests/test_proxy_origin.py | دالة | call | لا توجد Docstring. | ناقص | 30 |
| tests/test_proxy_origin.py | دالة | test_own_origin_is_accepted_behind_a_proxy | لا توجد Docstring. | ناقص | 55 |
| tests/test_proxy_origin.py | دالة | test_a_foreign_site_is_still_refused | لا توجد Docstring. | ناقص | 61 |
| tests/test_proxy_origin.py | دالة | test_configured_origin_still_works_without_any_proxy_headers | لا توجد Docstring. | ناقص | 66 |
| tests/test_request_budget.py | كلاس | FakeClock | لا توجد Docstring. | ناقص | 9 |
| tests/test_request_budget.py | دالة | FakeClock.__init__ | لا توجد Docstring. | ناقص | 10 |
| tests/test_request_budget.py | دالة | FakeClock.__call__ | لا توجد Docstring. | ناقص | 13 |
| tests/test_request_budget.py | دالة | test_resource_reservations_are_bounded_and_thread_safe_in_snapshot | لا توجد Docstring. | ناقص | 17 |
| tests/test_request_budget.py | دالة | test_deadline_blocks_new_work_and_caps_outbound_timeout | لا توجد Docstring. | ناقص | 35 |
| tests/test_request_budget.py | دالة | test_environment_overrides_are_clamped | لا توجد Docstring. | ناقص | 51 |
| tests/test_request_budget.py | دالة | test_web_agent_reserves_search_model_and_page_work_before_io | لا توجد Docstring. | ناقص | 65 |
| tests/test_request_budget.py | دالة | test_social_provider_reserves_budget_before_network_io | لا توجد Docstring. | ناقص | 88 |
| tests/test_research.py | دالة | test_social_question_gets_platform_targeted_queries | لا توجد Docstring. | ناقص | 12 |
| tests/test_research.py | دالة | test_follow_up_query_keeps_prior_topic | لا توجد Docstring. | ناقص | 20 |
| tests/test_research.py | دالة | test_plan_validation_caps_queries_and_rejects_non_string_values | لا توجد Docstring. | ناقص | 27 |
| tests/test_research.py | دالة | test_rank_fusion_promotes_cross_provider_consensus_and_deduplicates | لا توجد Docstring. | ناقص | 42 |
| tests/test_research.py | دالة | test_source_classification_distinguishes_social_and_government | لا توجد Docstring. | ناقص | 72 |
| tests/test_research.py | دالة | test_explicit_page_urls_are_extracted_and_not_left_in_search_terms | لا توجد Docstring. | ناقص | 79 |
| tests/test_research.py | دالة | test_registrable_domain_groups_subdomains_and_respects_public_suffixes | لا توجد Docstring. | ناقص | 88 |
| tests/test_research.py | دالة | test_evidence_coverage_does_not_count_sibling_subdomains_as_independent | لا توجد Docstring. | ناقص | 97 |
| tests/test_research_guardrails.py | دالة | test_depth_deep_english_phrases | لا توجد Docstring. | ناقص | 15 |
| tests/test_research_guardrails.py | دالة | test_depth_deep_arabic_phrases | لا توجد Docstring. | ناقص | 21 |
| tests/test_research_guardrails.py | دالة | test_depth_standard_ordinary_questions | لا توجد Docstring. | ناقص | 27 |
| tests/test_research_guardrails.py | دالة | test_depth_does_not_trigger_on_partial_words | لا توجد Docstring. | ناقص | 35 |
| tests/test_research_guardrails.py | دالة | test_freshness_positive_english | لا توجد Docstring. | ناقص | 43 |
| tests/test_research_guardrails.py | دالة | test_freshness_positive_arabic | لا توجد Docstring. | ناقص | 50 |
| tests/test_research_guardrails.py | دالة | test_freshness_negative_know_and_snowden | لا توجد Docstring. | ناقص | 56 |
| tests/test_research_guardrails.py | دالة | test_relevance_keeps_matching_source | لا توجد Docstring. | ناقص | 65 |
| tests/test_research_guardrails.py | دالة | test_relevance_rejects_unrelated | لا توجد Docstring. | ناقص | 91 |
| tests/test_research_guardrails.py | دالة | test_relevance_keeps_official_despite_wording | لا توجد Docstring. | ناقص | 104 |
| tests/test_research_guardrails.py | دالة | test_filter_deduplicates | لا توجد Docstring. | ناقص | 118 |
| tests/test_research_guardrails.py | دالة | test_filter_empty_and_failed_extract | لا توجد Docstring. | ناقص | 144 |
| tests/test_research_guardrails.py | دالة | test_evidence_adequate | لا توجد Docstring. | ناقص | 164 |
| tests/test_research_guardrails.py | دالة | test_evidence_insufficient_empty | لا توجد Docstring. | ناقص | 176 |
| tests/test_research_guardrails.py | دالة | test_evidence_failed_provider | لا توجد Docstring. | ناقص | 182 |
| tests/test_research_guardrails.py | دالة | test_evidence_partial_single_source | لا توجد Docstring. | ناقص | 188 |
| tests/test_sqlite_backup_restore.py | دالة | test_backup_and_restore_preserve_omarai_leads | لا توجد Docstring. | ناقص | 11 |
| tests/test_sqlite_backup_restore.py | دالة | test_backup_never_overwrites_an_existing_destination | لا توجد Docstring. | ناقص | 50 |
| tests/test_sqlite_backup_restore.py | دالة | test_backup_rejects_non_omarai_sqlite_database_without_leaving_destination | لا توجد Docstring. | ناقص | 62 |
| tests/test_sqlite_backup_restore.py | دالة | test_backup_rejects_same_source_and_destination | لا توجد Docstring. | ناقص | 74 |
| tests/test_sqlite_backup_restore.py | دالة | test_restore_rejects_corrupt_backup_without_overwriting_source | لا توجد Docstring. | ناقص | 82 |
| tests/test_sqlite_backup_restore.py | دالة | test_backup_rejects_dangling_symlink_destination | لا توجد Docstring. | ناقص | 93 |
| tests/test_web_agent.py | دالة | sample_source | لا توجد Docstring. | ناقص | 15 |
| tests/test_web_agent.py | دالة | test_agent_synthesizes_with_sources_without_live_network | لا توجد Docstring. | ناقص | 31 |
| tests/test_web_agent.py | دالة | test_agent_synthesizes_with_sources_without_live_network.plan | لا توجد Docstring. | ناقص | 36 |
| tests/test_web_agent.py | دالة | test_agent_synthesizes_with_sources_without_live_network.collect | لا توجد Docstring. | ناقص | 46 |
| tests/test_web_agent.py | دالة | test_agent_synthesizes_with_sources_without_live_network.generate | لا توجد Docstring. | ناقص | 61 |
| tests/test_web_agent.py | دالة | test_agent_returns_search_snippets_if_model_not_configured | لا توجد Docstring. | ناقص | 101 |
| tests/test_web_agent.py | دالة | test_agent_rejects_empty_or_oversized_question | لا توجد Docstring. | ناقص | 133 |
| tests/test_web_agent.py | دالة | test_history_search_query_expands_short_follow_up | لا توجد Docstring. | ناقص | 141 |
| tests/test_web_agent.py | دالة | test_public_url_filter_rejects_local_and_credential_urls | لا توجد Docstring. | ناقص | 148 |
| tests/test_web_agent.py | دالة | test_public_url_filter_accepts_basic_https_url | لا توجد Docstring. | ناقص | 155 |
| tests/test_web_agent.py | دالة | test_search_web_parses_duckduckgo_and_bing_without_ddgs | لا توجد Docstring. | ناقص | 159 |
| tests/test_web_agent.py | كلاس | test_search_web_parses_duckduckgo_and_bing_without_ddgs.FakeResponse | لا توجد Docstring. | ناقص | 178 |
| tests/test_web_agent.py | دالة | test_search_web_parses_duckduckgo_and_bing_without_ddgs.FakeResponse.__init__ | لا توجد Docstring. | ناقص | 181 |
| tests/test_web_agent.py | دالة | test_search_web_parses_duckduckgo_and_bing_without_ddgs.fake_get | لا توجد Docstring. | ناقص | 187 |
| tests/test_web_agent.py | دالة | test_model_planner_preserves_social_intent_and_adds_targeted_query | لا توجد Docstring. | ناقص | 203 |
| tests/test_web_agent.py | دالة | test_direct_social_search_reads_public_reddit_and_bluesky_results | لا توجد Docstring. | ناقص | 224 |
| tests/test_web_agent.py | كلاس | test_direct_social_search_reads_public_reddit_and_bluesky_results.FakeResponse | لا توجد Docstring. | ناقص | 234 |
| tests/test_web_agent.py | دالة | test_direct_social_search_reads_public_reddit_and_bluesky_results.FakeResponse.__init__ | لا توجد Docstring. | ناقص | 237 |
| tests/test_web_agent.py | دالة | test_direct_social_search_reads_public_reddit_and_bluesky_results.FakeResponse.json | لا توجد Docstring. | ناقص | 242 |
| tests/test_web_agent.py | دالة | test_direct_social_search_reads_public_reddit_and_bluesky_results.fake_get | لا توجد Docstring. | ناقص | 245 |
| tests/test_web_agent.py | دالة | test_research_collection_fuses_multiple_queries_and_reports_provenance | لا توجد Docstring. | ناقص | 272 |
| tests/test_web_agent.py | دالة | test_research_collection_fuses_multiple_queries_and_reports_provenance.search | لا توجد Docstring. | ناقص | 275 |
| tests/test_web_agent.py | دالة | test_invalid_citations_are_removed_and_valid_ones_preserved | لا توجد Docstring. | ناقص | 310 |
| tests/test_web_agent.py | دالة | test_citation_metadata_limits_claim_to_index_range_validation | لا توجد Docstring. | ناقص | 319 |
| tests/test_web_agent.py | دالة | test_citation_metadata_reports_invalid_reference_repair | لا توجد Docstring. | ناقص | 336 |
| tests/test_web_agent.py | دالة | test_citation_metadata_reports_absent_markers_and_empty_source_range | لا توجد Docstring. | ناقص | 349 |
| tests/test_web_agent.py | دالة | test_user_supplied_url_is_prioritized_and_page_content_is_extracted | لا توجد Docstring. | ناقص | 358 |
| tests/test_web_agent.py | دالة | test_official_x_search_is_used_only_with_explicit_bearer_token | لا توجد Docstring. | ناقص | 383 |
| tests/test_web_agent.py | كلاس | test_official_x_search_is_used_only_with_explicit_bearer_token.FakeResponse | لا توجد Docstring. | ناقص | 388 |
| tests/test_web_agent.py | دالة | test_official_x_search_is_used_only_with_explicit_bearer_token.FakeResponse.json | لا توجد Docstring. | ناقص | 391 |
| tests/test_web_agent.py | دالة | test_official_x_search_is_used_only_with_explicit_bearer_token.fake_get | لا توجد Docstring. | ناقص | 406 |
| tests/test_web_agent.py | دالة | test_instagram_graph_api_returns_only_public_hashtag_media | لا توجد Docstring. | ناقص | 422 |
| tests/test_web_agent.py | كلاس | test_instagram_graph_api_returns_only_public_hashtag_media.FakeResponse | لا توجد Docstring. | ناقص | 429 |
| tests/test_web_agent.py | دالة | test_instagram_graph_api_returns_only_public_hashtag_media.FakeResponse.__init__ | لا توجد Docstring. | ناقص | 432 |
| tests/test_web_agent.py | دالة | test_instagram_graph_api_returns_only_public_hashtag_media.FakeResponse.json | لا توجد Docstring. | ناقص | 435 |
| tests/test_web_agent.py | دالة | test_instagram_graph_api_returns_only_public_hashtag_media.fake_get | لا توجد Docstring. | ناقص | 440 |
| tests/test_web_agent.py | دالة | test_instagram_api_not_configured_uses_honest_fallback_warning | لا توجد Docstring. | ناقص | 469 |
| tests/test_web_agent.py | دالة | test_facebook_pages_api_reads_only_operator_configured_pages | لا توجد Docstring. | ناقص | 479 |
| tests/test_web_agent.py | كلاس | test_facebook_pages_api_reads_only_operator_configured_pages.FakeResponse | لا توجد Docstring. | ناقص | 485 |
| tests/test_web_agent.py | دالة | test_facebook_pages_api_reads_only_operator_configured_pages.FakeResponse.json | لا توجد Docstring. | ناقص | 488 |
| tests/test_web_agent.py | دالة | test_facebook_pages_api_reads_only_operator_configured_pages.fake_get | لا توجد Docstring. | ناقص | 500 |
| tests/test_web_agent.py | دالة | test_reddit_oauth_api_is_preferred_when_credentials_are_configured | لا توجد Docstring. | ناقص | 516 |
| tests/test_web_agent.py | كلاس | test_reddit_oauth_api_is_preferred_when_credentials_are_configured.FakeResponse | لا توجد Docstring. | ناقص | 523 |
| tests/test_web_agent.py | دالة | test_reddit_oauth_api_is_preferred_when_credentials_are_configured.FakeResponse.__init__ | لا توجد Docstring. | ناقص | 526 |
| tests/test_web_agent.py | دالة | test_reddit_oauth_api_is_preferred_when_credentials_are_configured.FakeResponse.json | لا توجد Docstring. | ناقص | 529 |
| tests/test_web_agent.py | دالة | test_reddit_oauth_api_is_preferred_when_credentials_are_configured.FakeResponse.content | لا توجد Docstring. | ناقص | 533 |
| tests/test_web_agent.py | دالة | test_reddit_oauth_api_is_preferred_when_credentials_are_configured.fake_post | لا توجد Docstring. | ناقص | 539 |
| tests/test_web_agent.py | دالة | test_reddit_oauth_api_is_preferred_when_credentials_are_configured.fake_get | لا توجد Docstring. | ناقص | 543 |
| tests/test_web_agent.py | دالة | test_role_models_are_explicit_and_have_a_fallback | لا توجد Docstring. | ناقص | 572 |
| tests/test_web_agent.py | دالة | test_global_model_override_is_preserved_for_existing_users | لا توجد Docstring. | ناقص | 589 |
| tests/test_web_agent.py | دالة | test_completion_uses_fallback_model_after_primary_http_error | لا توجد Docstring. | ناقص | 601 |
| tests/test_web_agent.py | كلاس | test_completion_uses_fallback_model_after_primary_http_error.FakeResponse | لا توجد Docstring. | ناقص | 611 |
| tests/test_web_agent.py | دالة | test_completion_uses_fallback_model_after_primary_http_error.FakeResponse.__enter__ | لا توجد Docstring. | ناقص | 612 |
| tests/test_web_agent.py | دالة | test_completion_uses_fallback_model_after_primary_http_error.FakeResponse.__exit__ | لا توجد Docstring. | ناقص | 615 |
| tests/test_web_agent.py | دالة | test_completion_uses_fallback_model_after_primary_http_error.FakeResponse.read | لا توجد Docstring. | ناقص | 618 |
| tests/test_web_agent.py | دالة | test_completion_uses_fallback_model_after_primary_http_error.fake_urlopen | لا توجد Docstring. | ناقص | 626 |
| tests/test_web_agent.py | دالة | test_generator_rejects_silent_character_limit_truncation | لا توجد Docstring. | ناقص | 656 |
| tests/test_web_agent.py | دالة | test_completion_discards_truncated_primary_and_uses_complete_fallback | لا توجد Docstring. | ناقص | 671 |
| tests/test_web_agent.py | كلاس | test_completion_discards_truncated_primary_and_uses_complete_fallback.FakeResponse | لا توجد Docstring. | ناقص | 679 |
| tests/test_web_agent.py | دالة | test_completion_discards_truncated_primary_and_uses_complete_fallback.FakeResponse.__init__ | لا توجد Docstring. | ناقص | 680 |
| tests/test_web_agent.py | دالة | test_completion_discards_truncated_primary_and_uses_complete_fallback.FakeResponse.__enter__ | لا توجد Docstring. | ناقص | 688 |
| tests/test_web_agent.py | دالة | test_completion_discards_truncated_primary_and_uses_complete_fallback.FakeResponse.__exit__ | لا توجد Docstring. | ناقص | 691 |
| tests/test_web_agent.py | دالة | test_completion_discards_truncated_primary_and_uses_complete_fallback.FakeResponse.read | لا توجد Docstring. | ناقص | 694 |
| tests/test_web_agent.py | دالة | test_completion_discards_truncated_primary_and_uses_complete_fallback.fake_urlopen | لا توجد Docstring. | ناقص | 697 |
| tests/test_web_agent.py | دالة | test_completion_rejects_response_when_all_models_are_truncated | لا توجد Docstring. | ناقص | 720 |
| tests/test_web_agent.py | كلاس | test_completion_rejects_response_when_all_models_are_truncated.FakeResponse | لا توجد Docstring. | ناقص | 728 |
| tests/test_web_agent.py | دالة | test_completion_rejects_response_when_all_models_are_truncated.FakeResponse.__enter__ | لا توجد Docstring. | ناقص | 729 |
| tests/test_web_agent.py | دالة | test_completion_rejects_response_when_all_models_are_truncated.FakeResponse.__exit__ | لا توجد Docstring. | ناقص | 732 |
| tests/test_web_agent.py | دالة | test_completion_rejects_response_when_all_models_are_truncated.FakeResponse.read | لا توجد Docstring. | ناقص | 735 |
| tests/test_web_agent.py | دالة | test_completion_rejects_response_when_all_models_are_truncated.fake_urlopen | لا توجد Docstring. | ناقص | 743 |
| tests/test_web_agent.py | دالة | test_completion_falls_back_for_malformed_choice | لا توجد Docstring. | ناقص | 758 |
| tests/test_web_agent.py | كلاس | test_completion_falls_back_for_malformed_choice.FakeResponse | لا توجد Docstring. | ناقص | 766 |
| tests/test_web_agent.py | دالة | test_completion_falls_back_for_malformed_choice.FakeResponse.__init__ | لا توجد Docstring. | ناقص | 767 |
| tests/test_web_agent.py | دالة | test_completion_falls_back_for_malformed_choice.FakeResponse.__enter__ | لا توجد Docstring. | ناقص | 770 |
| tests/test_web_agent.py | دالة | test_completion_falls_back_for_malformed_choice.FakeResponse.__exit__ | لا توجد Docstring. | ناقص | 773 |
| tests/test_web_agent.py | دالة | test_completion_falls_back_for_malformed_choice.FakeResponse.read | لا توجد Docstring. | ناقص | 776 |
| tests/test_web_agent.py | دالة | test_completion_falls_back_for_malformed_choice.fake_urlopen | لا توجد Docstring. | ناقص | 779 |
| tests/test_web_agent.py | دالة | test_health_status_reports_models_without_credentials | لا توجد Docstring. | ناقص | 799 |
| tests/test_web_agent.py | دالة | test_health_status_exposes_external_model_privacy_notice_without_secrets | لا توجد Docstring. | ناقص | 817 |
| tests/test_web_agent.py | دالة | test_diagnostics_runs_real_search_and_can_skip_paid_or_rate_limited_model_calls | لا توجد Docstring. | ناقص | 829 |
| tests/test_web_agent.py | دالة | test_diagnostics_calls_a_model_only_when_explicitly_requested | لا توجد Docstring. | ناقص | 851 |
| tests/test_web_agent.py | دالة | test_diagnostics_calls_a_model_only_when_explicitly_requested.completion | لا توجد Docstring. | ناقص | 859 |
| tests/test_web_agent.py | دالة | test_diagnostics_reports_degraded_when_search_has_no_results_and_model_is_unconfigured | لا توجد Docstring. | ناقص | 877 |
| tests/test_web_agent.py | دالة | test_diagnostics_does_not_report_full_success_when_model_probe_fails | لا توجد Docstring. | ناقص | 890 |
| tests/test_web_agent.py | دالة | test_openrouter_live_web_search_tool_is_opt_in_and_returns_citations | لا توجد Docstring. | ناقص | 910 |
| tests/test_web_agent.py | كلاس | test_openrouter_live_web_search_tool_is_opt_in_and_returns_citations.FakeResponse | لا توجد Docstring. | ناقص | 919 |
| tests/test_web_agent.py | دالة | test_openrouter_live_web_search_tool_is_opt_in_and_returns_citations.FakeResponse.__enter__ | لا توجد Docstring. | ناقص | 920 |
| tests/test_web_agent.py | دالة | test_openrouter_live_web_search_tool_is_opt_in_and_returns_citations.FakeResponse.__exit__ | لا توجد Docstring. | ناقص | 923 |
| tests/test_web_agent.py | دالة | test_openrouter_live_web_search_tool_is_opt_in_and_returns_citations.FakeResponse.read | لا توجد Docstring. | ناقص | 926 |
| tests/test_web_agent.py | دالة | test_openrouter_live_web_search_tool_is_opt_in_and_returns_citations.fake_urlopen | لا توجد Docstring. | ناقص | 944 |
| tests/test_web_agent.py | دالة | test_openrouter_live_web_search_remains_disabled_without_explicit_opt_in | لا توجد Docstring. | ناقص | 964 |
| tests/test_web_agent.py | دالة | test_arabic_query_normalization_removes_diacritics_and_unifies_hamza | لا توجد Docstring. | ناقص | 971 |
| tests/test_web_agent.py | دالة | test_relevance_filter_rejects_translation_and_sports_noise | لا توجد Docstring. | ناقص | 979 |
| tests/test_web_agent.py | دالة | test_search_provider_failure_isolated_and_logged | لا توجد Docstring. | ناقص | 991 |
| tests/test_web_agent.py | دالة | test_search_provider_failure_isolated_and_logged.broken | لا توجد Docstring. | ناقص | 994 |
| tests/test_web_agent.py | دالة | test_search_provider_failure_isolated_and_logged.working | لا توجد Docstring. | ناقص | 997 |
| tests/test_web_agent.py | دالة | test_single_user_supplied_page_can_be_summarized_without_claiming_corroboration | لا توجد Docstring. | ناقص | 1023 |
| tests/test_web_agent.py | دالة | test_answer_hides_unwrapped_internal_review_report | لا توجد Docstring. | ناقص | 1071 |
| tests/test_web_agent.py | دالة | test_answer_hides_unwrapped_internal_review_report.collect | لا توجد Docstring. | ناقص | 1085 |
| tests/test_web_agent.py | دالة | test_sibling_subdomains_do_not_satisfy_independent_evidence_gate | لا توجد Docstring. | ناقص | 1124 |
| tests/test_web_agent.py | دالة | test_bounded_evidence_repair_recovers_with_one_relevant_independent_source | لا توجد Docstring. | ناقص | 1167 |
| tests/test_web_agent.py | دالة | test_bounded_evidence_repair_recovers_with_one_relevant_independent_source.collect | لا توجد Docstring. | ناقص | 1181 |
| tests/test_web_agent.py | دالة | test_insufficient_evidence_returns_explicit_refusal_without_calling_llm | لا توجد Docstring. | ناقص | 1225 |
| tests/test_web_agent.py | دالة | test_insufficient_evidence_returns_explicit_refusal_without_calling_llm.collect_only_one_source | لا توجد Docstring. | ناقص | 1239 |
| tests/test_web_agent.py | دالة | test_generate_keeps_web_evidence_in_separate_untrusted_user_message | لا توجد Docstring. | ناقص | 1274 |
| tests/test_web_agent.py | دالة | test_generate_keeps_web_evidence_in_separate_untrusted_user_message.fake_completion | لا توجد Docstring. | ناقص | 1281 |
| tests/test_web_agent.py | دالة | test_review_keeps_untrusted_evidence_out_of_system_message | لا توجد Docstring. | ناقص | 1310 |
| tests/test_web_agent.py | دالة | test_review_keeps_untrusted_evidence_out_of_system_message.fake_completion | لا توجد Docstring. | ناقص | 1317 |
| tests/test_web_agent.py | دالة | test_general_question_uses_model_without_needlessly_searching | لا توجد Docstring. | ناقص | 1343 |
| tests/test_web_agent.py | دالة | test_general_question_uses_model_without_needlessly_searching.fake_completion | لا توجد Docstring. | ناقص | 1348 |
| tests/test_web_agent.py | دالة | test_omarai_capability_question_is_answered_without_network | لا توجد Docstring. | ناقص | 1369 |
| tests/test_web_agent.py | دالة | test_link_lookup_can_return_one_clearly_labelled_candidate | لا توجد Docstring. | ناقص | 1386 |
| tests/test_web_agent.py | دالة | test_google_news_preserves_publisher_identity | لا توجد Docstring. | ناقص | 1432 |
| tests/test_web_agent.py | كلاس | test_google_news_preserves_publisher_identity.FakeResponse | لا توجد Docstring. | ناقص | 1443 |
| tests/test_web_agent.py | دالة | test_relevance_matching_handles_arabic_names_with_english_results | لا توجد Docstring. | ناقص | 1458 |
| tests/test_web_agent.py | دالة | test_routine_lookup_ignores_planner_overclassification | لا توجد Docstring. | ناقص | 1465 |
| tests/test_web_agent.py | دالة | test_routine_lookup_ignores_planner_overclassification.collect | لا توجد Docstring. | ناقص | 1493 |
| tests/test_web_agent.py | دالة | test_listing_discovery_detects_arabic_property_requests | لا توجد Docstring. | ناقص | 1514 |
| tests/test_web_agent.py | دالة | test_single_property_listing_is_returned_with_safety_caveat | لا توجد Docstring. | ناقص | 1520 |
| tests/test_web_agent.py | دالة | test_normalized_source_url_key_ignores_tracking_parameters_and_fragment | لا توجد Docstring. | ناقص | 1566 |
| tests/test_web_agent.py | دالة | test_bounded_repair_deduplicates_same_page_even_with_tracking_url | لا توجد Docstring. | ناقص | 1577 |
| tests/test_web_agent.py | دالة | test_bounded_repair_deduplicates_same_page_even_with_tracking_url.collect | لا توجد Docstring. | ناقص | 1590 |
| tests/test_web_agent.py | دالة | test_social_focused_partial_evidence_does_not_trigger_general_repair | لا توجد Docstring. | ناقص | 1630 |
| tests/test_web_agent.py | دالة | test_social_focused_partial_evidence_does_not_trigger_general_repair.collect | لا توجد Docstring. | ناقص | 1643 |
| tests/test_web_agent.py | دالة | test_question_coverage_targets_extract_arabic_and_english_explicit_criteria | لا توجد Docstring. | ناقص | 1675 |
| tests/test_web_agent.py | دالة | test_question_coverage_targets_do_not_invent_parts_for_simple_question | لا توجد Docstring. | ناقص | 1693 |
| tests/test_web_agent.py | دالة | test_generator_includes_extracted_targets_as_a_non_authoritative_checklist | لا توجد Docstring. | ناقص | 1697 |
| tests/test_web_agent.py | دالة | test_generator_includes_extracted_targets_as_a_non_authoritative_checklist.fake_completion | لا توجد Docstring. | ناقص | 1701 |
| tests/test_web_agent.py | دالة | test_reviewer_checks_coverage_targets_without_claiming_independent_verification | لا توجد Docstring. | ناقص | 1722 |
| tests/test_web_agent.py | دالة | test_reviewer_checks_coverage_targets_without_claiming_independent_verification.fake_completion | لا توجد Docstring. | ناقص | 1726 |
| tests/test_web_agent.py | دالة | test_search_attempt_is_reported_when_no_sources_survive | لا توجد Docstring. | ناقص | 1744 |
| tests/test_web_agent.py | دالة | test_search_attempt_is_reported_when_no_sources_survive.collect | لا توجد Docstring. | ناقص | 1758 |
| tests/test_web_agent.py | دالة | test_success_report_counts_registrable_domains_not_sibling_subdomains | لا توجد Docstring. | ناقص | 1795 |
| tests/test_web_agent.py | دالة | test_completion_rejects_content_filtered_primary_and_uses_fallback | لا توجد Docstring. | ناقص | 1852 |
| tests/test_web_agent.py | كلاس | test_completion_rejects_content_filtered_primary_and_uses_fallback.FakeResponse | لا توجد Docstring. | ناقص | 1860 |
| tests/test_web_agent.py | دالة | test_completion_rejects_content_filtered_primary_and_uses_fallback.FakeResponse.__init__ | لا توجد Docstring. | ناقص | 1861 |
| tests/test_web_agent.py | دالة | test_completion_rejects_content_filtered_primary_and_uses_fallback.FakeResponse.__enter__ | لا توجد Docstring. | ناقص | 1869 |
| tests/test_web_agent.py | دالة | test_completion_rejects_content_filtered_primary_and_uses_fallback.FakeResponse.__exit__ | لا توجد Docstring. | ناقص | 1872 |
| tests/test_web_agent.py | دالة | test_completion_rejects_content_filtered_primary_and_uses_fallback.FakeResponse.read | لا توجد Docstring. | ناقص | 1875 |
| tests/test_web_agent.py | دالة | test_completion_rejects_content_filtered_primary_and_uses_fallback.fake_urlopen | لا توجد Docstring. | ناقص | 1878 |
| tests/test_web_agent.py | دالة | test_reviewer_rejects_duplicate_final_answer_delimiters | لا توجد Docstring. | ناقص | 1896 |
| tests/test_web_agent.py | دالة | test_frontend_review_status_matches_api_contract | لا توجد Docstring. | ناقص | 1914 |
| tests/test_web_agent.py | دالة | test_research_error_preserves_confirmed_search_attempt_without_fabricating_counts | لا توجد Docstring. | ناقص | 1923 |
| tests/test_web_agent.py | دالة | test_research_error_preserves_confirmed_search_attempt_without_fabricating_counts.failed_after_provider_result | لا توجد Docstring. | ناقص | 1935 |
| tests/test_web_agent.py | دالة | test_research_error_without_provider_diagnostics_is_reported_as_unknown | لا توجد Docstring. | ناقص | 1962 |
| tests/test_web_agent.py | دالة | test_research_error_without_provider_diagnostics_is_reported_as_unknown.fail_before_attempt | لا توجد Docstring. | ناقص | 1974 |
| tests/test_web_agent.py | دالة | test_general_answer_does_not_silently_slice_overlong_model_output | لا توجد Docstring. | ناقص | 1991 |
| tests/test_web_agent.py | دالة | test_frontend_discloses_unknown_counts_after_research_error | لا توجد Docstring. | ناقص | 2005 |
| tests/test_web_agent.py | دالة | test_generic_provider_failure_does_not_claim_search_attempt_as_confirmed | لا توجد Docstring. | ناقص | 2014 |
| tests/test_web_agent.py | دالة | test_generic_provider_failure_does_not_claim_search_attempt_as_confirmed.fail_after_generic_provider_error | لا توجد Docstring. | ناقص | 2026 |
| tests/test_web_agent.py | دالة | test_diagnostics_tries_fallback_probe_when_first_probe_has_no_results | لا توجد Docstring. | ناقص | 2051 |
| tests/test_web_agent.py | دالة | test_diagnostics_tries_fallback_probe_when_first_probe_has_no_results.search | لا توجد Docstring. | ناقص | 2055 |
| tests/test_web_agent.py | دالة | test_lead_discovery_is_distinct_from_listing_search | لا توجد Docstring. | ناقص | 2080 |
| tests/test_web_agent.py | دالة | test_buyer_intent_evidence_requires_explicit_purchase_signal | لا توجد Docstring. | ناقص | 2087 |
| tests/test_web_agent.py | دالة | test_lead_generation_does_not_present_sale_listings_as_buyers | لا توجد Docstring. | ناقص | 2104 |
| tests/test_web_agent.py | دالة | test_lead_generation_search_plan_includes_high_intent_queries | لا توجد Docstring. | ناقص | 2156 |
| tests/test_web_agent.py | دالة | test_lead_generation_search_plan_includes_high_intent_queries.collect | لا توجد Docstring. | ناقص | 2169 |
| tests/test_web_agent.py | دالة | test_deepseek_search_adapter_normalizes_results_without_exposing_api_key | لا توجد Docstring. | ناقص | 2207 |
| tests/test_web_agent.py | كلاس | test_deepseek_search_adapter_normalizes_results_without_exposing_api_key.FakeResponse | لا توجد Docstring. | ناقص | 2214 |
| tests/test_web_agent.py | دالة | test_deepseek_search_adapter_normalizes_results_without_exposing_api_key.FakeResponse.raise_for_status | لا توجد Docstring. | ناقص | 2215 |
| tests/test_web_agent.py | دالة | test_deepseek_search_adapter_normalizes_results_without_exposing_api_key.FakeResponse.json | لا توجد Docstring. | ناقص | 2218 |
| tests/test_web_agent.py | دالة | test_deepseek_search_adapter_normalizes_results_without_exposing_api_key.fake_post | لا توجد Docstring. | ناقص | 2232 |
| tests/test_web_agent.py | دالة | test_diagnostics_distinguishes_connector_response_without_matches_from_offline | لا توجد Docstring. | ناقص | 2250 |
| tests/test_web_agent.py | دالة | test_diagnostics_distinguishes_connector_response_without_matches_from_offline.completed_empty_search | لا توجد Docstring. | ناقص | 2254 |
| tests/test_web_agent.py | دالة | test_deepseek_search_request_budget_defaults_to_one_and_is_bounded | لا توجد Docstring. | ناقص | 2270 |
| tests/test_web_agent.py | دالة | test_diagnostics_distinguishes_completed_search_without_matches_from_connection_failure | لا توجد Docstring. | ناقص | 2285 |
| tests/test_web_agent.py | دالة | test_diagnostics_distinguishes_completed_search_without_matches_from_connection_failure.no_results | لا توجد Docstring. | ناقص | 2290 |
| tests/test_web_agent.py | دالة | test_buyer_intent_phrase_inside_negated_text_is_not_a_lead_signal | لا توجد Docstring. | ناقص | 2305 |
| tests/test_web_agent.py | دالة | test_lead_generation_preserves_unknown_state_when_research_throws | لا توجد Docstring. | ناقص | 2315 |
| tests/test_web_agent.py | دالة | test_lead_generation_preserves_unknown_state_when_research_throws.fail_research | لا توجد Docstring. | ناقص | 2329 |
| tests/test_web_agent.py | دالة | test_local_answer_exposes_request_budget_without_claiming_live_search | لا توجد Docstring. | ناقص | 2353 |
| tests/test_web_agent.py | دالة | test_reviewed_answer_without_valid_citations_cannot_be_rated_good | لا توجد Docstring. | ناقص | 2370 |

---

أُنشئ هذا الفهرس بتحليل AST القياسي في Python. تُستثنى مجلدات البيئات الافتراضية والاعتماديات والملفات المولدة لتجنب فهرسة نواتج البناء أو نسخ المكتبات.
