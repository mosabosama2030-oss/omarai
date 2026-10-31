# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **030**
- سجلات الأسطر: **800**
- النطاق: SRC-70795F4B61-L000430 إلى SRC-4FFD5AFC54-L000468
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## ملفات أخرى

### FILE-70795F4B61 — [scripts/compare_answer_quality_runs.py](../../scripts/compare_answer_quality_runs.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
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
| [SRC-A8360B1B03-L000010](../../scripts/hosted_smoke_test.py#L10) | 10 | `"import urllib.error"` | — |
| [SRC-A8360B1B03-L000011](../../scripts/hosted_smoke_test.py#L11) | 11 | `"import urllib.parse"` | — |
| [SRC-A8360B1B03-L000012](../../scripts/hosted_smoke_test.py#L12) | 12 | `"import urllib.request"` | — |
| [SRC-A8360B1B03-L000013](../../scripts/hosted_smoke_test.py#L13) | 13 | `"from typing import Any"` | — |
| [SRC-A8360B1B03-L000014](../../scripts/hosted_smoke_test.py#L14) | 14 | `""` | — |
| [SRC-A8360B1B03-L000015](../../scripts/hosted_smoke_test.py#L15) | 15 | `""` | — |
| [SRC-A8360B1B03-L000016](../../scripts/hosted_smoke_test.py#L16) | 16 | `"class SmokeError(RuntimeError):"` | — |
| [SRC-A8360B1B03-L000017](../../scripts/hosted_smoke_test.py#L17) | 17 | `"    \"\"\"A live acceptance check failed.\"\"\""` | — |
| [SRC-A8360B1B03-L000018](../../scripts/hosted_smoke_test.py#L18) | 18 | `""` | — |
| [SRC-A8360B1B03-L000019](../../scripts/hosted_smoke_test.py#L19) | 19 | `""` | — |
| [SRC-A8360B1B03-L000020](../../scripts/hosted_smoke_test.py#L20) | 20 | `"class _SameOriginRedirectHandler(urllib.request.HTTPRedirectHandler):"` | — |
| [SRC-A8360B1B03-L000021](../../scripts/hosted_smoke_test.py#L21) | 21 | `"    \"\"\"Never forward a bearer token to a different origin during an HTTP redirect.\"\"\""` | — |
| [SRC-A8360B1B03-L000022](../../scripts/hosted_smoke_test.py#L22) | 22 | `""` | — |
| [SRC-A8360B1B03-L000023](../../scripts/hosted_smoke_test.py#L23) | 23 | `"    @staticmethod"` | — |
| [SRC-A8360B1B03-L000024](../../scripts/hosted_smoke_test.py#L24) | 24 | `"    def _origin(url: str) -> tuple[str, str, int \| None]:"` | — |
| [SRC-A8360B1B03-L000025](../../scripts/hosted_smoke_test.py#L25) | 25 | `"        parsed = urllib.parse.urlsplit(url)"` | — |
| [SRC-A8360B1B03-L000026](../../scripts/hosted_smoke_test.py#L26) | 26 | `"        try:"` | — |
| [SRC-A8360B1B03-L000027](../../scripts/hosted_smoke_test.py#L27) | 27 | `"            port = parsed.port"` | — |
| [SRC-A8360B1B03-L000028](../../scripts/hosted_smoke_test.py#L28) | 28 | `"        except ValueError:"` | — |
| [SRC-A8360B1B03-L000029](../../scripts/hosted_smoke_test.py#L29) | 29 | `"            return \"\", \"\", None"` | — |
| [SRC-A8360B1B03-L000030](../../scripts/hosted_smoke_test.py#L30) | 30 | `"        if port is None:"` | — |
| [SRC-A8360B1B03-L000031](../../scripts/hosted_smoke_test.py#L31) | 31 | `"            port = 443 if parsed.scheme.lower() == \"https\" else 80 if parsed.scheme.lower() == \"http\" else None"` | — |
| [SRC-A8360B1B03-L000032](../../scripts/hosted_smoke_test.py#L32) | 32 | `"        return parsed.scheme.lower(), (parsed.hostname or \"\").lower(), port"` | — |
| [SRC-A8360B1B03-L000033](../../scripts/hosted_smoke_test.py#L33) | 33 | `""` | — |
| [SRC-A8360B1B03-L000034](../../scripts/hosted_smoke_test.py#L34) | 34 | `"    def redirect_request(self, req, fp, code, msg, headers, newurl):"` | — |
| [SRC-A8360B1B03-L000035](../../scripts/hosted_smoke_test.py#L35) | 35 | `"        target_url = urllib.parse.urljoin(req.full_url, newurl)"` | — |
| [SRC-A8360B1B03-L000036](../../scripts/hosted_smoke_test.py#L36) | 36 | `"        target = urllib.parse.urlsplit(target_url)"` | — |
| [SRC-A8360B1B03-L000037](../../scripts/hosted_smoke_test.py#L37) | 37 | `"        if ("` | — |
| [SRC-A8360B1B03-L000038](../../scripts/hosted_smoke_test.py#L38) | 38 | `"            self._origin(req.full_url) != self._origin(target_url)"` | — |
| [SRC-A8360B1B03-L000039](../../scripts/hosted_smoke_test.py#L39) | 39 | `"            or target.scheme.lower() not in {\"http\", \"https\"}"` | — |
| [SRC-A8360B1B03-L000040](../../scripts/hosted_smoke_test.py#L40) | 40 | `"            or target.username"` | — |
| [SRC-A8360B1B03-L000041](../../scripts/hosted_smoke_test.py#L41) | 41 | `"            or target.password"` | — |
| [SRC-A8360B1B03-L000042](../../scripts/hosted_smoke_test.py#L42) | 42 | `"        ):"` | — |
| [SRC-A8360B1B03-L000043](../../scripts/hosted_smoke_test.py#L43) | 43 | `"            raise urllib.error.HTTPError("` | — |
| [SRC-A8360B1B03-L000044](../../scripts/hosted_smoke_test.py#L44) | 44 | `"                req.full_url, code, \"Cross-origin redirect blocked\", headers, fp"` | — |
| [SRC-A8360B1B03-L000045](../../scripts/hosted_smoke_test.py#L45) | 45 | `"            )"` | — |
| [SRC-A8360B1B03-L000046](../../scripts/hosted_smoke_test.py#L46) | 46 | `"        return super().redirect_request(req, fp, code, msg, headers, target_url)"` | — |
| [SRC-A8360B1B03-L000047](../../scripts/hosted_smoke_test.py#L47) | 47 | `""` | — |
| [SRC-A8360B1B03-L000048](../../scripts/hosted_smoke_test.py#L48) | 48 | `""` | — |
| [SRC-A8360B1B03-L000049](../../scripts/hosted_smoke_test.py#L49) | 49 | `"def normalize_origin(value: str, allow_http: bool = False) -> str:"` | — |
| [SRC-A8360B1B03-L000050](../../scripts/hosted_smoke_test.py#L50) | 50 | `"    parsed = urllib.parse.urlsplit((value or \"\").strip())"` | — |
| [SRC-A8360B1B03-L000051](../../scripts/hosted_smoke_test.py#L51) | 51 | `"    if parsed.scheme not in {\"https\", \"http\"} or not parsed.hostname:"` | — |
| [SRC-A8360B1B03-L000052](../../scripts/hosted_smoke_test.py#L52) | 52 | `"        raise SmokeError(\"Provide an absolute HTTPS origin, for example https://your-app.example.com.\")"` | — |
| [SRC-A8360B1B03-L000053](../../scripts/hosted_smoke_test.py#L53) | 53 | `"    if parsed.username or parsed.password or parsed.query or parsed.fragment:"` | — |
| [SRC-A8360B1B03-L000054](../../scripts/hosted_smoke_test.py#L54) | 54 | `"        raise SmokeError(\"The base URL must not contain credentials, a query, or a fragment.\")"` | — |
| [SRC-A8360B1B03-L000055](../../scripts/hosted_smoke_test.py#L55) | 55 | `"    if parsed.path not in {\"\", \"/\"}:"` | — |
| [SRC-A8360B1B03-L000056](../../scripts/hosted_smoke_test.py#L56) | 56 | `"        raise SmokeError(\"The base URL must be an origin only; do not add /api or another path.\")"` | — |
| [SRC-A8360B1B03-L000057](../../scripts/hosted_smoke_test.py#L57) | 57 | `"    if parsed.scheme != \"https\" and not ("` | — |
| [SRC-A8360B1B03-L000058](../../scripts/hosted_smoke_test.py#L58) | 58 | `"        allow_http and parsed.hostname.lower() in {\"localhost\", \"127.0.0.1\", \"::1\"}"` | — |
| [SRC-A8360B1B03-L000059](../../scripts/hosted_smoke_test.py#L59) | 59 | `"    ):"` | — |
| [SRC-A8360B1B03-L000060](../../scripts/hosted_smoke_test.py#L60) | 60 | `"        raise SmokeError(\"Hosted tests require HTTPS; plain HTTP is allowed only for local tests.\")"` | — |
| [SRC-A8360B1B03-L000061](../../scripts/hosted_smoke_test.py#L61) | 61 | `"    try:"` | — |
| [SRC-A8360B1B03-L000062](../../scripts/hosted_smoke_test.py#L62) | 62 | `"        port = parsed.port"` | — |
| [SRC-A8360B1B03-L000063](../../scripts/hosted_smoke_test.py#L63) | 63 | `"    except ValueError as exc:"` | — |
| [SRC-A8360B1B03-L000064](../../scripts/hosted_smoke_test.py#L64) | 64 | `"        raise SmokeError(\"Invalid port in base URL.\") from exc"` | — |
| [SRC-A8360B1B03-L000065](../../scripts/hosted_smoke_test.py#L65) | 65 | `"    host = parsed.hostname"` | — |
| [SRC-A8360B1B03-L000066](../../scripts/hosted_smoke_test.py#L66) | 66 | `"    if \":\" in host and not host.startswith(\"[\"):"` | — |
| [SRC-A8360B1B03-L000067](../../scripts/hosted_smoke_test.py#L67) | 67 | `"        host = f\"[{host}]\""` | — |
| [SRC-A8360B1B03-L000068](../../scripts/hosted_smoke_test.py#L68) | 68 | `"    if port:"` | — |
| [SRC-A8360B1B03-L000069](../../scripts/hosted_smoke_test.py#L69) | 69 | `"        host += f\":{port}\""` | — |
| [SRC-A8360B1B03-L000070](../../scripts/hosted_smoke_test.py#L70) | 70 | `"    return f\"{parsed.scheme}://{host}\""` | — |
| [SRC-A8360B1B03-L000071](../../scripts/hosted_smoke_test.py#L71) | 71 | `""` | — |
| [SRC-A8360B1B03-L000072](../../scripts/hosted_smoke_test.py#L72) | 72 | `""` | — |
| [SRC-A8360B1B03-L000073](../../scripts/hosted_smoke_test.py#L73) | 73 | `"def request_json(url: str, *, token: str = \"\", payload: dict[str, Any] \| None = None,"` | — |
| [SRC-A8360B1B03-L000074](../../scripts/hosted_smoke_test.py#L74) | 74 | `"                 timeout: float = 90) -> tuple[int, dict[str, Any] \| None]:"` | — |
| [SRC-A8360B1B03-L000075](../../scripts/hosted_smoke_test.py#L75) | 75 | `"    headers = {\"Accept\": \"application/json\"}"` | — |
| [SRC-A8360B1B03-L000076](../../scripts/hosted_smoke_test.py#L76) | 76 | `"    data = None"` | — |
| [SRC-A8360B1B03-L000077](../../scripts/hosted_smoke_test.py#L77) | 77 | `"    if payload is not None:"` | — |
| [SRC-A8360B1B03-L000078](../../scripts/hosted_smoke_test.py#L78) | 78 | `"        headers[\"Content-Type\"] = \"application/json\""` | — |
| [SRC-A8360B1B03-L000079](../../scripts/hosted_smoke_test.py#L79) | 79 | `"        data = json.dumps(payload, ensure_ascii=False).encode()"` | — |
| [SRC-A8360B1B03-L000080](../../scripts/hosted_smoke_test.py#L80) | 80 | `"    if token:"` | — |
| [SRC-A8360B1B03-L000081](../../scripts/hosted_smoke_test.py#L81) | 81 | `"        headers[\"Authorization\"] = \"Bearer \" + token"` | — |
| [SRC-A8360B1B03-L000082](../../scripts/hosted_smoke_test.py#L82) | 82 | `"    request = urllib.request.Request(url, data=data, headers=headers)"` | — |
| [SRC-A8360B1B03-L000083](../../scripts/hosted_smoke_test.py#L83) | 83 | `"    try:"` | — |
| [SRC-A8360B1B03-L000084](../../scripts/hosted_smoke_test.py#L84) | 84 | `"        opener = urllib.request.build_opener(_SameOriginRedirectHandler())"` | — |
| [SRC-A8360B1B03-L000085](../../scripts/hosted_smoke_test.py#L85) | 85 | `"        with opener.open(request, timeout=timeout) as response:"` | — |
| [SRC-A8360B1B03-L000086](../../scripts/hosted_smoke_test.py#L86) | 86 | `"            status, body = response.status, response.read(1_000_000)"` | — |
| [SRC-A8360B1B03-L000087](../../scripts/hosted_smoke_test.py#L87) | 87 | `"    except urllib.error.HTTPError as exc:"` | — |
| [SRC-A8360B1B03-L000088](../../scripts/hosted_smoke_test.py#L88) | 88 | `"        status = exc.code"` | — |
| [SRC-A8360B1B03-L000089](../../scripts/hosted_smoke_test.py#L89) | 89 | `"        body = exc.read(100_000)"` | — |
| [SRC-A8360B1B03-L000090](../../scripts/hosted_smoke_test.py#L90) | 90 | `"    except (urllib.error.URLError, TimeoutError, OSError) as exc:"` | — |
| [SRC-A8360B1B03-L000091](../../scripts/hosted_smoke_test.py#L91) | 91 | `"        path = urllib.parse.urlsplit(url).path"` | — |
| [SRC-A8360B1B03-L000092](../../scripts/hosted_smoke_test.py#L92) | 92 | `"        raise SmokeError(f\"Network request failed at {path}; check the service and network.\") from exc"` | — |
| [SRC-A8360B1B03-L000093](../../scripts/hosted_smoke_test.py#L93) | 93 | `"    try:"` | — |
| [SRC-A8360B1B03-L000094](../../scripts/hosted_smoke_test.py#L94) | 94 | `"        result = json.loads(body.decode(\"utf-8\"))"` | — |
| [SRC-A8360B1B03-L000095](../../scripts/hosted_smoke_test.py#L95) | 95 | `"    except (UnicodeDecodeError, json.JSONDecodeError):"` | — |
| [SRC-A8360B1B03-L000096](../../scripts/hosted_smoke_test.py#L96) | 96 | `"        result = None"` | — |
| [SRC-A8360B1B03-L000097](../../scripts/hosted_smoke_test.py#L97) | 97 | `"    return status, result if isinstance(result, dict) else None"` | — |
| [SRC-A8360B1B03-L000098](../../scripts/hosted_smoke_test.py#L98) | 98 | `""` | — |
| [SRC-A8360B1B03-L000099](../../scripts/hosted_smoke_test.py#L99) | 99 | `""` | — |
| [SRC-A8360B1B03-L000100](../../scripts/hosted_smoke_test.py#L100) | 100 | `"def run_smoke("` | — |
| [SRC-A8360B1B03-L000101](../../scripts/hosted_smoke_test.py#L101) | 101 | `"    origin: str,"` | — |
| [SRC-A8360B1B03-L000102](../../scripts/hosted_smoke_test.py#L102) | 102 | `"    token: str,"` | — |
| [SRC-A8360B1B03-L000103](../../scripts/hosted_smoke_test.py#L103) | 103 | `"    *,"` | — |
| [SRC-A8360B1B03-L000104](../../scripts/hosted_smoke_test.py#L104) | 104 | `"    timeout: float = 90,"` | — |
| [SRC-A8360B1B03-L000105](../../scripts/hosted_smoke_test.py#L105) | 105 | `"    allow_http: bool = False,"` | — |
| [SRC-A8360B1B03-L000106](../../scripts/hosted_smoke_test.py#L106) | 106 | `"    expected_sha: str \| None = None,"` | — |
| [SRC-A8360B1B03-L000107](../../scripts/hosted_smoke_test.py#L107) | 107 | `") -> dict[str, Any]:"` | — |
| [SRC-A8360B1B03-L000108](../../scripts/hosted_smoke_test.py#L108) | 108 | `"    origin = normalize_origin(origin, allow_http)"` | — |
| [SRC-A8360B1B03-L000109](../../scripts/hosted_smoke_test.py#L109) | 109 | `"    if expected_sha is not None and not re.fullmatch(r\"[0-9a-fA-F]{40}\", expected_sha.strip()):"` | — |
| [SRC-A8360B1B03-L000110](../../scripts/hosted_smoke_test.py#L110) | 110 | `"        raise SmokeError(\"The expected source revision must be a full 40-character Git SHA.\")"` | — |
| [SRC-A8360B1B03-L000111](../../scripts/hosted_smoke_test.py#L111) | 111 | `"    if len(token.strip()) < 32:"` | — |
| [SRC-A8360B1B03-L000112](../../scripts/hosted_smoke_test.py#L112) | 112 | `"        raise SmokeError(\"OMARAI_ACCESS_TOKEN is missing or shorter than 32 characters.\")"` | — |
| [SRC-A8360B1B03-L000113](../../scripts/hosted_smoke_test.py#L113) | 113 | `""` | — |
| [SRC-A8360B1B03-L000114](../../scripts/hosted_smoke_test.py#L114) | 114 | `"    status, health = request_json(f\"{origin}/api/health\", timeout=min(timeout, 20))"` | — |
| [SRC-A8360B1B03-L000115](../../scripts/hosted_smoke_test.py#L115) | 115 | `"    if status != 200 or not health or health.get(\"ok\") is not True:"` | — |
| [SRC-A8360B1B03-L000116](../../scripts/hosted_smoke_test.py#L116) | 116 | `"        raise SmokeError(f\"Health check failed (HTTP {status}).\")"` | — |
| [SRC-A8360B1B03-L000117](../../scripts/hosted_smoke_test.py#L117) | 117 | `"    checks: dict[str, Any] = {\"health\": \"passed\"}"` | — |
| [SRC-A8360B1B03-L000118](../../scripts/hosted_smoke_test.py#L118) | 118 | `""` | — |
| [SRC-A8360B1B03-L000119](../../scripts/hosted_smoke_test.py#L119) | 119 | `"    build = health.get(\"build\")"` | — |
| [SRC-A8360B1B03-L000120](../../scripts/hosted_smoke_test.py#L120) | 120 | `"    reported_sha = build.get(\"sha\") if isinstance(build, dict) else None"` | — |
| [SRC-A8360B1B03-L000121](../../scripts/hosted_smoke_test.py#L121) | 121 | `"    if expected_sha is not None:"` | — |
| [SRC-A8360B1B03-L000122](../../scripts/hosted_smoke_test.py#L122) | 122 | `"        expected = expected_sha.strip().lower()"` | — |
| [SRC-A8360B1B03-L000123](../../scripts/hosted_smoke_test.py#L123) | 123 | `"        if not isinstance(reported_sha, str) or reported_sha.lower() != expected:"` | — |
| [SRC-A8360B1B03-L000124](../../scripts/hosted_smoke_test.py#L124) | 124 | `"            raise SmokeError("` | — |
| [SRC-A8360B1B03-L000125](../../scripts/hosted_smoke_test.py#L125) | 125 | `"                \"The deployed service SHA does not match the expected Git commit. \""` | — |
| [SRC-A8360B1B03-L000126](../../scripts/hosted_smoke_test.py#L126) | 126 | `"                \"Pass OMARAI_BUILD_SHA as a Docker build argument for the deployed revision, \""` | — |
| [SRC-A8360B1B03-L000127](../../scripts/hosted_smoke_test.py#L127) | 127 | `"                \"then rebuild and redeploy.\""` | — |
| [SRC-A8360B1B03-L000128](../../scripts/hosted_smoke_test.py#L128) | 128 | `"            )"` | — |
| [SRC-A8360B1B03-L000129](../../scripts/hosted_smoke_test.py#L129) | 129 | `"        checks[\"build_identity\"] = {"` | — |
| [SRC-A8360B1B03-L000130](../../scripts/hosted_smoke_test.py#L130) | 130 | `"            \"status\": \"passed\","` | — |
| [SRC-A8360B1B03-L000131](../../scripts/hosted_smoke_test.py#L131) | 131 | `"            \"expected_sha\": expected,"` | — |
| [SRC-A8360B1B03-L000132](../../scripts/hosted_smoke_test.py#L132) | 132 | `"            \"reported_sha\": reported_sha.lower(),"` | — |
| [SRC-A8360B1B03-L000133](../../scripts/hosted_smoke_test.py#L133) | 133 | `"        }"` | — |
| [SRC-A8360B1B03-L000134](../../scripts/hosted_smoke_test.py#L134) | 134 | `"    else:"` | — |
| [SRC-A8360B1B03-L000135](../../scripts/hosted_smoke_test.py#L135) | 135 | `"        checks[\"build_identity\"] = {"` | — |
| [SRC-A8360B1B03-L000136](../../scripts/hosted_smoke_test.py#L136) | 136 | `"            \"status\": \"not_checked\","` | — |
| [SRC-A8360B1B03-L000137](../../scripts/hosted_smoke_test.py#L137) | 137 | `"            \"reported_sha\": reported_sha if isinstance(reported_sha, str) else \"unknown\","` | — |
| [SRC-A8360B1B03-L000138](../../scripts/hosted_smoke_test.py#L138) | 138 | `"        }"` | — |
| [SRC-A8360B1B03-L000139](../../scripts/hosted_smoke_test.py#L139) | 139 | `""` | — |
| [SRC-A8360B1B03-L000140](../../scripts/hosted_smoke_test.py#L140) | 140 | `"    status, _ = request_json("` | — |
| [SRC-A8360B1B03-L000141](../../scripts/hosted_smoke_test.py#L141) | 141 | `"        f\"{origin}/api/agent\", payload={\"question\": \"اختبار رفض الوصول غير المصرح به\"},"` | — |
| [SRC-A8360B1B03-L000142](../../scripts/hosted_smoke_test.py#L142) | 142 | `"        timeout=min(timeout, 20),"` | — |
| [SRC-A8360B1B03-L000143](../../scripts/hosted_smoke_test.py#L143) | 143 | `"    )"` | — |
| [SRC-A8360B1B03-L000144](../../scripts/hosted_smoke_test.py#L144) | 144 | `"    if status != 401:"` | — |
| [SRC-A8360B1B03-L000145](../../scripts/hosted_smoke_test.py#L145) | 145 | `"        raise SmokeError(f\"Unauthenticated POST /api/agent should return 401, received {status}.\")"` | — |
| [SRC-A8360B1B03-L000146](../../scripts/hosted_smoke_test.py#L146) | 146 | `"    checks[\"authentication\"] = \"passed\""` | — |
| [SRC-A8360B1B03-L000147](../../scripts/hosted_smoke_test.py#L147) | 147 | `""` | — |
| [SRC-A8360B1B03-L000148](../../scripts/hosted_smoke_test.py#L148) | 148 | `"    # These are real network/provider calls and may incur model/search usage."` | — |
| [SRC-A8360B1B03-L000149](../../scripts/hosted_smoke_test.py#L149) | 149 | `"    status, diagnostics = request_json("` | — |
| [SRC-A8360B1B03-L000150](../../scripts/hosted_smoke_test.py#L150) | 150 | `"        f\"{origin}/api/diagnostics\", token=token,"` | — |
| [SRC-A8360B1B03-L000151](../../scripts/hosted_smoke_test.py#L151) | 151 | `"        payload={\"test_model\": True, \"test_social\": False}, timeout=timeout,"` | — |
| [SRC-A8360B1B03-L000152](../../scripts/hosted_smoke_test.py#L152) | 152 | `"    )"` | — |
| [SRC-A8360B1B03-L000153](../../scripts/hosted_smoke_test.py#L153) | 153 | `"    if status != 200 or not diagnostics:"` | — |
| [SRC-A8360B1B03-L000154](../../scripts/hosted_smoke_test.py#L154) | 154 | `"        raise SmokeError(f\"Authenticated diagnostics failed (HTTP {status}).\")"` | — |
| [SRC-A8360B1B03-L000155](../../scripts/hosted_smoke_test.py#L155) | 155 | `"    parts = diagnostics.get(\"checks\", {})"` | — |
| [SRC-A8360B1B03-L000156](../../scripts/hosted_smoke_test.py#L156) | 156 | `"    web = parts.get(\"web_search\", {}) if isinstance(parts, dict) else {}"` | — |
| [SRC-A8360B1B03-L000157](../../scripts/hosted_smoke_test.py#L157) | 157 | `"    model = parts.get(\"language_model\", {}) if isinstance(parts, dict) else {}"` | — |
| [SRC-A8360B1B03-L000158](../../scripts/hosted_smoke_test.py#L158) | 158 | `"    if not isinstance(web, dict) or web.get(\"status\") != \"passed\":"` | — |
| [SRC-A8360B1B03-L000159](../../scripts/hosted_smoke_test.py#L159) | 159 | `"        raise SmokeError(\"The real web-search connectivity test did not pass.\")"` | — |
| [SRC-A8360B1B03-L000160](../../scripts/hosted_smoke_test.py#L160) | 160 | `"    if not isinstance(model, dict) or model.get(\"status\") != \"passed\":"` | — |
| [SRC-A8360B1B03-L000161](../../scripts/hosted_smoke_test.py#L161) | 161 | `"        raise SmokeError(\"The configured language model did not pass a real completion test.\")"` | — |
| [SRC-A8360B1B03-L000162](../../scripts/hosted_smoke_test.py#L162) | 162 | `"    checks[\"live_search\"] = {"` | — |
| [SRC-A8360B1B03-L000163](../../scripts/hosted_smoke_test.py#L163) | 163 | `"        \"status\": \"passed\", \"result_count\": web.get(\"result_count\", 0),"` | — |
| [SRC-A8360B1B03-L000164](../../scripts/hosted_smoke_test.py#L164) | 164 | `"        \"provider_counts\": web.get(\"provider_counts\", {}),"` | — |
| [SRC-A8360B1B03-L000165](../../scripts/hosted_smoke_test.py#L165) | 165 | `"    }"` | — |
| [SRC-A8360B1B03-L000166](../../scripts/hosted_smoke_test.py#L166) | 166 | `"    checks[\"language_model\"] = {\"status\": \"passed\", \"response_received\": True}"` | — |
| [SRC-A8360B1B03-L000167](../../scripts/hosted_smoke_test.py#L167) | 167 | `""` | — |
| [SRC-A8360B1B03-L000168](../../scripts/hosted_smoke_test.py#L168) | 168 | `"    status, answer = request_json("` | — |
| [SRC-A8360B1B03-L000169](../../scripts/hosted_smoke_test.py#L169) | 169 | `"        f\"{origin}/api/agent\", token=token, timeout=timeout,"` | — |
| [SRC-A8360B1B03-L000170](../../scripts/hosted_smoke_test.py#L170) | 170 | `"        payload={"` | — |
| [SRC-A8360B1B03-L000171](../../scripts/hosted_smoke_test.py#L171) | 171 | `"            \"question\": \"اختبار تشغيل: ما عاصمة مصر؟ أجب بالعربية بإيجاز واستند إلى المصادر.\","` | — |
| [SRC-A8360B1B03-L000172](../../scripts/hosted_smoke_test.py#L172) | 172 | `"            \"history\": [], \"mode\": \"auto\","` | — |
| [SRC-A8360B1B03-L000173](../../scripts/hosted_smoke_test.py#L173) | 173 | `"        },"` | — |
| [SRC-A8360B1B03-L000174](../../scripts/hosted_smoke_test.py#L174) | 174 | `"    )"` | — |
| [SRC-A8360B1B03-L000175](../../scripts/hosted_smoke_test.py#L175) | 175 | `"    if status != 200 or not answer:"` | — |
| [SRC-A8360B1B03-L000176](../../scripts/hosted_smoke_test.py#L176) | 176 | `"        raise SmokeError(f\"Authenticated agent request failed (HTTP {status}).\")"` | — |
| [SRC-A8360B1B03-L000177](../../scripts/hosted_smoke_test.py#L177) | 177 | `"    sources = answer.get(\"sources\")"` | — |
| [SRC-A8360B1B03-L000178](../../scripts/hosted_smoke_test.py#L178) | 178 | `"    usable = ["` | — |
| [SRC-A8360B1B03-L000179](../../scripts/hosted_smoke_test.py#L179) | 179 | `"        item for item in sources if isinstance(item, dict)"` | — |
| [SRC-A8360B1B03-L000180](../../scripts/hosted_smoke_test.py#L180) | 180 | `"        and isinstance(item.get(\"url\"), str)"` | — |
| [SRC-A8360B1B03-L000181](../../scripts/hosted_smoke_test.py#L181) | 181 | `"        and urllib.parse.urlsplit(item[\"url\"]).scheme in {\"http\", \"https\"}"` | — |
| [SRC-A8360B1B03-L000182](../../scripts/hosted_smoke_test.py#L182) | 182 | `"        and urllib.parse.urlsplit(item[\"url\"]).hostname"` | — |
| [SRC-A8360B1B03-L000183](../../scripts/hosted_smoke_test.py#L183) | 183 | `"    ] if isinstance(sources, list) else []"` | — |
| [SRC-A8360B1B03-L000184](../../scripts/hosted_smoke_test.py#L184) | 184 | `"    if answer.get(\"used_web_search\") is not True or not usable:"` | — |
| [SRC-A8360B1B03-L000185](../../scripts/hosted_smoke_test.py#L185) | 185 | `"        raise SmokeError(\"Agent request did not return a live web search with usable source URLs.\")"` | — |
| [SRC-A8360B1B03-L000186](../../scripts/hosted_smoke_test.py#L186) | 186 | `"    if answer.get(\"used_language_model\") is not True:"` | — |
| [SRC-A8360B1B03-L000187](../../scripts/hosted_smoke_test.py#L187) | 187 | `"        raise SmokeError(\"Agent request did not confirm that a language model was used.\")"` | — |
| [SRC-A8360B1B03-L000188](../../scripts/hosted_smoke_test.py#L188) | 188 | `"    report = answer.get(\"search_report\")"` | — |
| [SRC-A8360B1B03-L000189](../../scripts/hosted_smoke_test.py#L189) | 189 | `"    checks[\"agent_request\"] = {"` | — |
| [SRC-A8360B1B03-L000190](../../scripts/hosted_smoke_test.py#L190) | 190 | `"        \"status\": \"passed\", \"source_count\": len(usable),"` | — |
| [SRC-A8360B1B03-L000191](../../scripts/hosted_smoke_test.py#L191) | 191 | `"        \"direct_pages_read\": report.get(\"pages_fetched\") if isinstance(report, dict) else None,"` | — |
| [SRC-A8360B1B03-L000192](../../scripts/hosted_smoke_test.py#L192) | 192 | `"        \"providers_reported\": report.get(\"providers_used\", []) if isinstance(report, dict) else [],"` | — |
| [SRC-A8360B1B03-L000193](../../scripts/hosted_smoke_test.py#L193) | 193 | `"        \"answer_received\": bool(str(answer.get(\"answer\", \"\")).strip()),"` | — |
| [SRC-A8360B1B03-L000194](../../scripts/hosted_smoke_test.py#L194) | 194 | `"    }"` | — |
| [SRC-A8360B1B03-L000195](../../scripts/hosted_smoke_test.py#L195) | 195 | `"    return {"` | — |
| [SRC-A8360B1B03-L000196](../../scripts/hosted_smoke_test.py#L196) | 196 | `"        \"result\": \"passed\", \"target_host\": urllib.parse.urlsplit(origin).hostname,"` | — |
| [SRC-A8360B1B03-L000197](../../scripts/hosted_smoke_test.py#L197) | 197 | `"        \"checks\": checks,"` | — |
| [SRC-A8360B1B03-L000198](../../scripts/hosted_smoke_test.py#L198) | 198 | `"        \"note\": \"This proves the request path worked at test time, not continuous uptime. Provider usage may incur charges.\","` | — |
| [SRC-A8360B1B03-L000199](../../scripts/hosted_smoke_test.py#L199) | 199 | `"    }"` | — |
| [SRC-A8360B1B03-L000200](../../scripts/hosted_smoke_test.py#L200) | 200 | `""` | — |
| [SRC-A8360B1B03-L000201](../../scripts/hosted_smoke_test.py#L201) | 201 | `""` | — |
| [SRC-A8360B1B03-L000202](../../scripts/hosted_smoke_test.py#L202) | 202 | `"def main() -> int:"` | — |
| [SRC-A8360B1B03-L000203](../../scripts/hosted_smoke_test.py#L203) | 203 | `"    parser = argparse.ArgumentParser(description=\"Run live acceptance checks against hosted Omarai.\")"` | — |
| [SRC-A8360B1B03-L000204](../../scripts/hosted_smoke_test.py#L204) | 204 | `"    parser.add_argument(\"--base-url\", default=os.getenv(\"OMARAI_BASE_URL\", \"\"))"` | — |
| [SRC-A8360B1B03-L000205](../../scripts/hosted_smoke_test.py#L205) | 205 | `"    parser.add_argument(\"--timeout\", type=float, default=90)"` | — |
| [SRC-A8360B1B03-L000206](../../scripts/hosted_smoke_test.py#L206) | 206 | `"    parser.add_argument("` | — |
| [SRC-A8360B1B03-L000207](../../scripts/hosted_smoke_test.py#L207) | 207 | `"        \"--expected-sha\","` | — |
| [SRC-A8360B1B03-L000208](../../scripts/hosted_smoke_test.py#L208) | 208 | `"        default=os.getenv(\"OMARAI_EXPECTED_BUILD_SHA\", \"\"),"` | — |
| [SRC-A8360B1B03-L000209](../../scripts/hosted_smoke_test.py#L209) | 209 | `"        help=\"Require the deployed image to report this full 40-character source Git SHA.\","` | — |
| [SRC-A8360B1B03-L000210](../../scripts/hosted_smoke_test.py#L210) | 210 | `"    )"` | — |
| [SRC-A8360B1B03-L000211](../../scripts/hosted_smoke_test.py#L211) | 211 | `"    parser.add_argument(\"--allow-http\", action=\"store_true\","` | — |
| [SRC-A8360B1B03-L000212](../../scripts/hosted_smoke_test.py#L212) | 212 | `"                        help=\"Allow HTTP only for localhost/127.0.0.1/::1 testing.\")"` | — |
| [SRC-A8360B1B03-L000213](../../scripts/hosted_smoke_test.py#L213) | 213 | `"    args = parser.parse_args()"` | — |
| [SRC-A8360B1B03-L000214](../../scripts/hosted_smoke_test.py#L214) | 214 | `"    try:"` | — |
| [SRC-A8360B1B03-L000215](../../scripts/hosted_smoke_test.py#L215) | 215 | `"        result = run_smoke("` | — |
| [SRC-A8360B1B03-L000216](../../scripts/hosted_smoke_test.py#L216) | 216 | `"            args.base_url,"` | — |
| [SRC-A8360B1B03-L000217](../../scripts/hosted_smoke_test.py#L217) | 217 | `"            os.getenv(\"OMARAI_ACCESS_TOKEN\", \"\").strip(),"` | — |
| [SRC-A8360B1B03-L000218](../../scripts/hosted_smoke_test.py#L218) | 218 | `"            timeout=max(5, min(args.timeout, 240)),"` | — |
| [SRC-A8360B1B03-L000219](../../scripts/hosted_smoke_test.py#L219) | 219 | `"            allow_http=args.allow_http,"` | — |
| [SRC-A8360B1B03-L000220](../../scripts/hosted_smoke_test.py#L220) | 220 | `"            expected_sha=args.expected_sha or None,"` | — |
| [SRC-A8360B1B03-L000221](../../scripts/hosted_smoke_test.py#L221) | 221 | `"        )"` | — |
| [SRC-A8360B1B03-L000222](../../scripts/hosted_smoke_test.py#L222) | 222 | `"    except SmokeError as exc:"` | — |
| [SRC-A8360B1B03-L000223](../../scripts/hosted_smoke_test.py#L223) | 223 | `"        print(json.dumps({\"result\": \"failed\", \"error\": str(exc)}, ensure_ascii=False, indent=2))"` | — |
| [SRC-A8360B1B03-L000224](../../scripts/hosted_smoke_test.py#L224) | 224 | `"        return 1"` | — |
| [SRC-A8360B1B03-L000225](../../scripts/hosted_smoke_test.py#L225) | 225 | `"    print(json.dumps(result, ensure_ascii=False, indent=2))"` | — |
| [SRC-A8360B1B03-L000226](../../scripts/hosted_smoke_test.py#L226) | 226 | `"    return 0"` | — |
| [SRC-A8360B1B03-L000227](../../scripts/hosted_smoke_test.py#L227) | 227 | `""` | — |
| [SRC-A8360B1B03-L000228](../../scripts/hosted_smoke_test.py#L228) | 228 | `""` | — |
| [SRC-A8360B1B03-L000229](../../scripts/hosted_smoke_test.py#L229) | 229 | `"if __name__ == \"__main__\":"` | — |
| [SRC-A8360B1B03-L000230](../../scripts/hosted_smoke_test.py#L230) | 230 | `"    sys.exit(main())"` | — |
## ملفات أخرى

### FILE-4FFD5AFC54 — [scripts/run_answer_quality_benchmark.py](../../scripts/run_answer_quality_benchmark.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-4FFD5AFC54-L000001](../../scripts/run_answer_quality_benchmark.py#L1) | 1 | `"\"\"\"Offline / optional live runner for OMARAI-REDTEAM-001 answer-quality cases."` | — |
| [SRC-4FFD5AFC54-L000002](../../scripts/run_answer_quality_benchmark.py#L2) | 2 | `""` | — |
| [SRC-4FFD5AFC54-L000003](../../scripts/run_answer_quality_benchmark.py#L3) | 3 | `"Modes"` | — |
| [SRC-4FFD5AFC54-L000004](../../scripts/run_answer_quality_benchmark.py#L4) | 4 | `"-----"` | — |
| [SRC-4FFD5AFC54-L000005](../../scripts/run_answer_quality_benchmark.py#L5) | 5 | `"validate (default)"` | — |
| [SRC-4FFD5AFC54-L000006](../../scripts/run_answer_quality_benchmark.py#L6) | 6 | `"    Load and structurally validate the corpus. No network."` | — |
| [SRC-4FFD5AFC54-L000007](../../scripts/run_answer_quality_benchmark.py#L7) | 7 | `""` | — |
| [SRC-4FFD5AFC54-L000008](../../scripts/run_answer_quality_benchmark.py#L8) | 8 | `"live (explicit opt-in)"` | — |
| [SRC-4FFD5AFC54-L000009](../../scripts/run_answer_quality_benchmark.py#L9) | 9 | `"    POST selected cases to an existing Omarai HTTP API (/api/agent)."` | — |
| [SRC-4FFD5AFC54-L000010](../../scripts/run_answer_quality_benchmark.py#L10) | 10 | `"    Does NOT inject JSON evidence fixtures into the server."` | — |
| [SRC-4FFD5AFC54-L000011](../../scripts/run_answer_quality_benchmark.py#L11) | 11 | `"    Does NOT auto-grade PASS/FAIL for answer quality; records NOT_TESTED"` | — |
| [SRC-4FFD5AFC54-L000012](../../scripts/run_answer_quality_benchmark.py#L12) | 12 | `"    unless a transport/auth error makes the run unusable."` | — |
| [SRC-4FFD5AFC54-L000013](../../scripts/run_answer_quality_benchmark.py#L13) | 13 | `""` | — |
| [SRC-4FFD5AFC54-L000014](../../scripts/run_answer_quality_benchmark.py#L14) | 14 | `"Standard library only. Secrets only via environment (never CLI flags for tokens)."` | — |
| [SRC-4FFD5AFC54-L000015](../../scripts/run_answer_quality_benchmark.py#L15) | 15 | `""` | — |
| [SRC-4FFD5AFC54-L000016](../../scripts/run_answer_quality_benchmark.py#L16) | 16 | `"Examples"` | — |
| [SRC-4FFD5AFC54-L000017](../../scripts/run_answer_quality_benchmark.py#L17) | 17 | `"--------"` | — |
| [SRC-4FFD5AFC54-L000018](../../scripts/run_answer_quality_benchmark.py#L18) | 18 | `"  python scripts/run_answer_quality_benchmark.py"` | — |
| [SRC-4FFD5AFC54-L000019](../../scripts/run_answer_quality_benchmark.py#L19) | 19 | `"  python scripts/run_answer_quality_benchmark.py --mode validate --summary"` | — |
| [SRC-4FFD5AFC54-L000020](../../scripts/run_answer_quality_benchmark.py#L20) | 20 | `"  python scripts/run_answer_quality_benchmark.py --mode live --base-url http://127.0.0.1:8765 \\\\"` | — |
| [SRC-4FFD5AFC54-L000021](../../scripts/run_answer_quality_benchmark.py#L21) | 21 | `"      --case-id AQ-001 --limit 1 --out /tmp/aq_results.json"` | — |
| [SRC-4FFD5AFC54-L000022](../../scripts/run_answer_quality_benchmark.py#L22) | 22 | `"\"\"\""` | — |
| [SRC-4FFD5AFC54-L000023](../../scripts/run_answer_quality_benchmark.py#L23) | 23 | `"from __future__ import annotations"` | — |
| [SRC-4FFD5AFC54-L000024](../../scripts/run_answer_quality_benchmark.py#L24) | 24 | `""` | — |
| [SRC-4FFD5AFC54-L000025](../../scripts/run_answer_quality_benchmark.py#L25) | 25 | `"import argparse"` | — |
| [SRC-4FFD5AFC54-L000026](../../scripts/run_answer_quality_benchmark.py#L26) | 26 | `"import ipaddress"` | — |
| [SRC-4FFD5AFC54-L000027](../../scripts/run_answer_quality_benchmark.py#L27) | 27 | `"import json"` | — |
| [SRC-4FFD5AFC54-L000028](../../scripts/run_answer_quality_benchmark.py#L28) | 28 | `"import math"` | — |
| [SRC-4FFD5AFC54-L000029](../../scripts/run_answer_quality_benchmark.py#L29) | 29 | `"import os"` | — |
| [SRC-4FFD5AFC54-L000030](../../scripts/run_answer_quality_benchmark.py#L30) | 30 | `"import re"` | — |
| [SRC-4FFD5AFC54-L000031](../../scripts/run_answer_quality_benchmark.py#L31) | 31 | `"import sys"` | — |
| [SRC-4FFD5AFC54-L000032](../../scripts/run_answer_quality_benchmark.py#L32) | 32 | `"import time"` | — |
| [SRC-4FFD5AFC54-L000033](../../scripts/run_answer_quality_benchmark.py#L33) | 33 | `"import urllib.error"` | — |
| [SRC-4FFD5AFC54-L000034](../../scripts/run_answer_quality_benchmark.py#L34) | 34 | `"import urllib.parse"` | — |
| [SRC-4FFD5AFC54-L000035](../../scripts/run_answer_quality_benchmark.py#L35) | 35 | `"import urllib.request"` | — |
| [SRC-4FFD5AFC54-L000036](../../scripts/run_answer_quality_benchmark.py#L36) | 36 | `"from datetime import UTC, datetime"` | — |
| [SRC-4FFD5AFC54-L000037](../../scripts/run_answer_quality_benchmark.py#L37) | 37 | `"from pathlib import Path"` | — |
| [SRC-4FFD5AFC54-L000038](../../scripts/run_answer_quality_benchmark.py#L38) | 38 | `""` | — |
| [SRC-4FFD5AFC54-L000039](../../scripts/run_answer_quality_benchmark.py#L39) | 39 | `"ROOT = Path(__file__).resolve().parents[1]"` | — |
| [SRC-4FFD5AFC54-L000040](../../scripts/run_answer_quality_benchmark.py#L40) | 40 | `"DEFAULT_CORPUS = ROOT / \"tests\" / \"fixtures\" / \"answer_quality_cases.json\""` | — |
| [SRC-4FFD5AFC54-L000041](../../scripts/run_answer_quality_benchmark.py#L41) | 41 | `"MAX_RESPONSE_BYTES = 2_000_000"` | — |
| [SRC-4FFD5AFC54-L000042](../../scripts/run_answer_quality_benchmark.py#L42) | 42 | `""` | — |
| [SRC-4FFD5AFC54-L000043](../../scripts/run_answer_quality_benchmark.py#L43) | 43 | `""` | — |
| [SRC-4FFD5AFC54-L000044](../../scripts/run_answer_quality_benchmark.py#L44) | 44 | `"def _load_request_cost_ledger(path: Path \| None, valid_case_ids: set[str]) -> tuple[dict[str, float], str \| None]:"` | — |
| [SRC-4FFD5AFC54-L000045](../../scripts/run_answer_quality_benchmark.py#L45) | 45 | `"    \"\"\"Load reconciled, externally sourced whole-request USD costs; never estimate them.\"\"\""` | — |
| [SRC-4FFD5AFC54-L000046](../../scripts/run_answer_quality_benchmark.py#L46) | 46 | `"    if path is None:"` | — |
| [SRC-4FFD5AFC54-L000047](../../scripts/run_answer_quality_benchmark.py#L47) | 47 | `"        return {}, None"` | — |
| [SRC-4FFD5AFC54-L000048](../../scripts/run_answer_quality_benchmark.py#L48) | 48 | `"    ledger = json.loads(path.read_text(encoding=\"utf-8\"))"` | — |
| [SRC-4FFD5AFC54-L000049](../../scripts/run_answer_quality_benchmark.py#L49) | 49 | `"    if not isinstance(ledger, dict):"` | — |
| [SRC-4FFD5AFC54-L000050](../../scripts/run_answer_quality_benchmark.py#L50) | 50 | `"        raise ValueError(\"request-cost ledger root must be an object\")"` | — |
| [SRC-4FFD5AFC54-L000051](../../scripts/run_answer_quality_benchmark.py#L51) | 51 | `"    if ledger.get(\"currency\") != \"USD\" or ledger.get(\"scope\") != \"complete_request\":"` | — |
| [SRC-4FFD5AFC54-L000052](../../scripts/run_answer_quality_benchmark.py#L52) | 52 | `"        raise ValueError(\"request-cost ledger must declare currency=USD and scope=complete_request\")"` | — |
| [SRC-4FFD5AFC54-L000053](../../scripts/run_answer_quality_benchmark.py#L53) | 53 | `"    source = ledger.get(\"source\")"` | — |
| [SRC-4FFD5AFC54-L000054](../../scripts/run_answer_quality_benchmark.py#L54) | 54 | `"    if not isinstance(source, str) or not source.strip():"` | — |
| [SRC-4FFD5AFC54-L000055](../../scripts/run_answer_quality_benchmark.py#L55) | 55 | `"        raise ValueError(\"request-cost ledger needs a non-empty source describing the reconciliation\")"` | — |
| [SRC-4FFD5AFC54-L000056](../../scripts/run_answer_quality_benchmark.py#L56) | 56 | `"    entries = ledger.get(\"costs\")"` | — |
| [SRC-4FFD5AFC54-L000057](../../scripts/run_answer_quality_benchmark.py#L57) | 57 | `"    if not isinstance(entries, list):"` | — |
| [SRC-4FFD5AFC54-L000058](../../scripts/run_answer_quality_benchmark.py#L58) | 58 | `"        raise ValueError(\"request-cost ledger must contain a costs array\")"` | — |
| [SRC-4FFD5AFC54-L000059](../../scripts/run_answer_quality_benchmark.py#L59) | 59 | `"    costs: dict[str, float] = {}"` | — |
| [SRC-4FFD5AFC54-L000060](../../scripts/run_answer_quality_benchmark.py#L60) | 60 | `"    for index, entry in enumerate(entries):"` | — |
| [SRC-4FFD5AFC54-L000061](../../scripts/run_answer_quality_benchmark.py#L61) | 61 | `"        if not isinstance(entry, dict):"` | — |
| [SRC-4FFD5AFC54-L000062](../../scripts/run_answer_quality_benchmark.py#L62) | 62 | `"            raise ValueError(f\"request-cost ledger costs[{index}] must be an object\")"` | — |
| [SRC-4FFD5AFC54-L000063](../../scripts/run_answer_quality_benchmark.py#L63) | 63 | `"        case_id = entry.get(\"case_id\")"` | — |
| [SRC-4FFD5AFC54-L000064](../../scripts/run_answer_quality_benchmark.py#L64) | 64 | `"        if not isinstance(case_id, str) or case_id not in valid_case_ids:"` | — |
| [SRC-4FFD5AFC54-L000065](../../scripts/run_answer_quality_benchmark.py#L65) | 65 | `"            raise ValueError(f\"request-cost ledger costs[{index}] has an unknown case_id\")"` | — |
| [SRC-4FFD5AFC54-L000066](../../scripts/run_answer_quality_benchmark.py#L66) | 66 | `"        if case_id in costs:"` | — |
| [SRC-4FFD5AFC54-L000067](../../scripts/run_answer_quality_benchmark.py#L67) | 67 | `"            raise ValueError(f\"request-cost ledger has duplicate case_id {case_id}\")"` | — |
| [SRC-4FFD5AFC54-L000068](../../scripts/run_answer_quality_benchmark.py#L68) | 68 | `"        value = _finite_nonnegative_number(entry.get(\"cost_usd\"))"` | — |
| [SRC-4FFD5AFC54-L000069](../../scripts/run_answer_quality_benchmark.py#L69) | 69 | `"        if value is None:"` | — |
| [SRC-4FFD5AFC54-L000070](../../scripts/run_answer_quality_benchmark.py#L70) | 70 | `"            raise ValueError(f\"request-cost ledger {case_id} cost_usd must be finite and non-negative\")"` | — |
| [SRC-4FFD5AFC54-L000071](../../scripts/run_answer_quality_benchmark.py#L71) | 71 | `"        costs[case_id] = value"` | — |
| [SRC-4FFD5AFC54-L000072](../../scripts/run_answer_quality_benchmark.py#L72) | 72 | `"    return costs, source.strip()"` | — |
| [SRC-4FFD5AFC54-L000073](../../scripts/run_answer_quality_benchmark.py#L73) | 73 | `""` | — |
| [SRC-4FFD5AFC54-L000074](../../scripts/run_answer_quality_benchmark.py#L74) | 74 | `""` | — |
| [SRC-4FFD5AFC54-L000075](../../scripts/run_answer_quality_benchmark.py#L75) | 75 | `"def _model_calls_from_payload(payload: dict) -> list[dict]:"` | — |
| [SRC-4FFD5AFC54-L000076](../../scripts/run_answer_quality_benchmark.py#L76) | 76 | `"    \"\"\"Read only structured per-request model-call metadata from an API response.\"\"\""` | — |
| [SRC-4FFD5AFC54-L000077](../../scripts/run_answer_quality_benchmark.py#L77) | 77 | `"    report = payload.get(\"search_report\")"` | — |
| [SRC-4FFD5AFC54-L000078](../../scripts/run_answer_quality_benchmark.py#L78) | 78 | `"    understanding = payload.get(\"task_understanding\")"` | — |
| [SRC-4FFD5AFC54-L000079](../../scripts/run_answer_quality_benchmark.py#L79) | 79 | `"    candidates = ["` | — |
| [SRC-4FFD5AFC54-L000080](../../scripts/run_answer_quality_benchmark.py#L80) | 80 | `"        payload.get(\"model_calls\"),"` | — |
| [SRC-4FFD5AFC54-L000081](../../scripts/run_answer_quality_benchmark.py#L81) | 81 | `"        report.get(\"model_calls\") if isinstance(report, dict) else None,"` | — |
| [SRC-4FFD5AFC54-L000082](../../scripts/run_answer_quality_benchmark.py#L82) | 82 | `"        understanding.get(\"model_calls\") if isinstance(understanding, dict) else None,"` | — |
| [SRC-4FFD5AFC54-L000083](../../scripts/run_answer_quality_benchmark.py#L83) | 83 | `"    ]"` | — |
| [SRC-4FFD5AFC54-L000084](../../scripts/run_answer_quality_benchmark.py#L84) | 84 | `"    for candidate in candidates:"` | — |
| [SRC-4FFD5AFC54-L000085](../../scripts/run_answer_quality_benchmark.py#L85) | 85 | `"        if isinstance(candidate, list) and candidate:"` | — |
| [SRC-4FFD5AFC54-L000086](../../scripts/run_answer_quality_benchmark.py#L86) | 86 | `"            return [item for item in candidate if isinstance(item, dict)]"` | — |
| [SRC-4FFD5AFC54-L000087](../../scripts/run_answer_quality_benchmark.py#L87) | 87 | `"    return []"` | — |
| [SRC-4FFD5AFC54-L000088](../../scripts/run_answer_quality_benchmark.py#L88) | 88 | `""` | — |
| [SRC-4FFD5AFC54-L000089](../../scripts/run_answer_quality_benchmark.py#L89) | 89 | `""` | — |
| [SRC-4FFD5AFC54-L000090](../../scripts/run_answer_quality_benchmark.py#L90) | 90 | `"def _finite_nonnegative_number(value) -> float \| None:"` | — |
| [SRC-4FFD5AFC54-L000091](../../scripts/run_answer_quality_benchmark.py#L91) | 91 | `"    if isinstance(value, bool) or not isinstance(value, (int, float)):"` | — |
| [SRC-4FFD5AFC54-L000092](../../scripts/run_answer_quality_benchmark.py#L92) | 92 | `"        return None"` | — |
| [SRC-4FFD5AFC54-L000093](../../scripts/run_answer_quality_benchmark.py#L93) | 93 | `"    number = float(value)"` | — |
| [SRC-4FFD5AFC54-L000094](../../scripts/run_answer_quality_benchmark.py#L94) | 94 | `"    if not math.isfinite(number) or number < 0:"` | — |
| [SRC-4FFD5AFC54-L000095](../../scripts/run_answer_quality_benchmark.py#L95) | 95 | `"        return None"` | — |
| [SRC-4FFD5AFC54-L000096](../../scripts/run_answer_quality_benchmark.py#L96) | 96 | `"    return number"` | — |
| [SRC-4FFD5AFC54-L000097](../../scripts/run_answer_quality_benchmark.py#L97) | 97 | `""` | — |
| [SRC-4FFD5AFC54-L000098](../../scripts/run_answer_quality_benchmark.py#L98) | 98 | `""` | — |
| [SRC-4FFD5AFC54-L000099](../../scripts/run_answer_quality_benchmark.py#L99) | 99 | `"def _response_metrics(payload: dict \| str, expected_strategy: str, transport_ok: bool) -> dict:"` | — |
| [SRC-4FFD5AFC54-L000100](../../scripts/run_answer_quality_benchmark.py#L100) | 100 | `"    \"\"\"Derive conservative telemetry; never infer semantic correctness from HTTP 200.\"\"\""` | — |
| [SRC-4FFD5AFC54-L000101](../../scripts/run_answer_quality_benchmark.py#L101) | 101 | `"    if not isinstance(payload, dict):"` | — |
| [SRC-4FFD5AFC54-L000102](../../scripts/run_answer_quality_benchmark.py#L102) | 102 | `"        payload = {}"` | — |
| [SRC-4FFD5AFC54-L000103](../../scripts/run_answer_quality_benchmark.py#L103) | 103 | `"    report = payload.get(\"search_report\")"` | — |
| [SRC-4FFD5AFC54-L000104](../../scripts/run_answer_quality_benchmark.py#L104) | 104 | `"    report = report if isinstance(report, dict) else {}"` | — |
| [SRC-4FFD5AFC54-L000105](../../scripts/run_answer_quality_benchmark.py#L105) | 105 | `"    outcome = report.get(\"search_outcome\")"` | — |
| [SRC-4FFD5AFC54-L000106](../../scripts/run_answer_quality_benchmark.py#L106) | 106 | `"    pipeline = report.get(\"pipeline_completion_status\")"` | — |
| [SRC-4FFD5AFC54-L000107](../../scripts/run_answer_quality_benchmark.py#L107) | 107 | `"    source_rows = payload.get(\"sources\")"` | — |
| [SRC-4FFD5AFC54-L000108](../../scripts/run_answer_quality_benchmark.py#L108) | 108 | `"    source_rows_known = isinstance(source_rows, list)"` | — |
| [SRC-4FFD5AFC54-L000109](../../scripts/run_answer_quality_benchmark.py#L109) | 109 | `"    source_count = len(source_rows) if source_rows_known else None"` | — |
| [SRC-4FFD5AFC54-L000110](../../scripts/run_answer_quality_benchmark.py#L110) | 110 | `"    if expected_strategy != \"web_search\":"` | — |
| [SRC-4FFD5AFC54-L000111](../../scripts/run_answer_quality_benchmark.py#L111) | 111 | `"        tool_status = \"NOT_APPLICABLE\""` | — |
| [SRC-4FFD5AFC54-L000112](../../scripts/run_answer_quality_benchmark.py#L112) | 112 | `"    elif not transport_ok:"` | — |
| [SRC-4FFD5AFC54-L000113](../../scripts/run_answer_quality_benchmark.py#L113) | 113 | `"        tool_status = \"TRANSPORT_FAILED\""` | — |
| [SRC-4FFD5AFC54-L000114](../../scripts/run_answer_quality_benchmark.py#L114) | 114 | `"    elif outcome == \"attempted_with_usable_sources\":"` | — |
| [SRC-4FFD5AFC54-L000115](../../scripts/run_answer_quality_benchmark.py#L115) | 115 | `"        if source_count is None:"` | — |
| [SRC-4FFD5AFC54-L000116](../../scripts/run_answer_quality_benchmark.py#L116) | 116 | `"            tool_status = \"UNKNOWN_SOURCE_COUNT\""` | — |
| [SRC-4FFD5AFC54-L000117](../../scripts/run_answer_quality_benchmark.py#L117) | 117 | `"        elif source_count == 0:"` | — |
| [SRC-4FFD5AFC54-L000118](../../scripts/run_answer_quality_benchmark.py#L118) | 118 | `"            tool_status = \"INCONSISTENT_SEARCH_OUTCOME_NO_RETURNED_SOURCES\""` | — |
| [SRC-4FFD5AFC54-L000119](../../scripts/run_answer_quality_benchmark.py#L119) | 119 | `"        else:"` | — |
| [SRC-4FFD5AFC54-L000120](../../scripts/run_answer_quality_benchmark.py#L120) | 120 | `"            tool_status = \"SUCCESS_WITH_USABLE_RESULTS\""` | — |
| [SRC-4FFD5AFC54-L000121](../../scripts/run_answer_quality_benchmark.py#L121) | 121 | `"    elif outcome == \"attempted_no_usable_sources\":"` | — |
| [SRC-4FFD5AFC54-L000122](../../scripts/run_answer_quality_benchmark.py#L122) | 122 | `"        if source_count is not None and source_count > 0:"` | — |
| [SRC-4FFD5AFC54-L000123](../../scripts/run_answer_quality_benchmark.py#L123) | 123 | `"            tool_status = \"INCONSISTENT_SEARCH_OUTCOME_WITH_RETURNED_SOURCES\""` | — |
| [SRC-4FFD5AFC54-L000124](../../scripts/run_answer_quality_benchmark.py#L124) | 124 | `"        else:"` | — |
| [SRC-4FFD5AFC54-L000125](../../scripts/run_answer_quality_benchmark.py#L125) | 125 | `"            tool_status = \"ATTEMPTED_NO_USABLE_RESULTS\""` | — |
| [SRC-4FFD5AFC54-L000126](../../scripts/run_answer_quality_benchmark.py#L126) | 126 | `"    elif outcome == \"attempted_research_error\":"` | — |
| [SRC-4FFD5AFC54-L000127](../../scripts/run_answer_quality_benchmark.py#L127) | 127 | `"        tool_status = \"TOOL_FAILED\""` | — |
| [SRC-4FFD5AFC54-L000128](../../scripts/run_answer_quality_benchmark.py#L128) | 128 | `"    elif outcome == \"unknown_after_budget_exhaustion\":"` | — |
| [SRC-4FFD5AFC54-L000129](../../scripts/run_answer_quality_benchmark.py#L129) | 129 | `"        tool_status = \"BUDGET_EXHAUSTED\""` | — |
| [SRC-4FFD5AFC54-L000130](../../scripts/run_answer_quality_benchmark.py#L130) | 130 | `"    elif outcome == \"not_attempted\":"` | — |
| [SRC-4FFD5AFC54-L000131](../../scripts/run_answer_quality_benchmark.py#L131) | 131 | `"        tool_status = \"NOT_ATTEMPTED\""` | — |
| [SRC-4FFD5AFC54-L000132](../../scripts/run_answer_quality_benchmark.py#L132) | 132 | `"    else:"` | — |
| [SRC-4FFD5AFC54-L000133](../../scripts/run_answer_quality_benchmark.py#L133) | 133 | `"        tool_status = \"UNKNOWN\""` | — |
| [SRC-4FFD5AFC54-L000134](../../scripts/run_answer_quality_benchmark.py#L134) | 134 | `""` | — |
| [SRC-4FFD5AFC54-L000135](../../scripts/run_answer_quality_benchmark.py#L135) | 135 | `"    task_understanding = payload.get(\"task_understanding\")"` | — |
| [SRC-4FFD5AFC54-L000136](../../scripts/run_answer_quality_benchmark.py#L136) | 136 | `"    task_understanding = task_understanding if isinstance(task_understanding, dict) else {}"` | — |
| [SRC-4FFD5AFC54-L000137](../../scripts/run_answer_quality_benchmark.py#L137) | 137 | `"    tool_execution = task_understanding.get(\"tool_execution\")"` | — |
| [SRC-4FFD5AFC54-L000138](../../scripts/run_answer_quality_benchmark.py#L138) | 138 | `"    tool_execution = tool_execution if isinstance(tool_execution, dict) else {}"` | — |
| [SRC-4FFD5AFC54-L000139](../../scripts/run_answer_quality_benchmark.py#L139) | 139 | `"    raw_tool_rows = tool_execution.get(\"tool_status_matrix\")"` | — |
| [SRC-4FFD5AFC54-L000140](../../scripts/run_answer_quality_benchmark.py#L140) | 140 | `"    requirements_raw = tool_execution.get(\"required_tools\")"` | — |
| [SRC-4FFD5AFC54-L000141](../../scripts/run_answer_quality_benchmark.py#L141) | 141 | `"    required_tool_matrix_present = ("` | — |
| [SRC-4FFD5AFC54-L000142](../../scripts/run_answer_quality_benchmark.py#L142) | 142 | `"        isinstance(raw_tool_rows, list) and isinstance(requirements_raw, list)"` | — |
| [SRC-4FFD5AFC54-L000143](../../scripts/run_answer_quality_benchmark.py#L143) | 143 | `"    )"` | — |
| [SRC-4FFD5AFC54-L000144](../../scripts/run_answer_quality_benchmark.py#L144) | 144 | `"    matrix_rows = [row for row in raw_tool_rows if isinstance(row, dict)] if isinstance(raw_tool_rows, list) else []"` | — |
| [SRC-4FFD5AFC54-L000145](../../scripts/run_answer_quality_benchmark.py#L145) | 145 | `"    required_tool_names = ["` | — |
| [SRC-4FFD5AFC54-L000146](../../scripts/run_answer_quality_benchmark.py#L146) | 146 | `"        name.strip()"` | — |
| [SRC-4FFD5AFC54-L000147](../../scripts/run_answer_quality_benchmark.py#L147) | 147 | `"        for name in requirements_raw"` | — |
| [SRC-4FFD5AFC54-L000148](../../scripts/run_answer_quality_benchmark.py#L148) | 148 | `"        if isinstance(name, str) and name.strip()"` | — |
| [SRC-4FFD5AFC54-L000149](../../scripts/run_answer_quality_benchmark.py#L149) | 149 | `"    ] if isinstance(requirements_raw, list) else []"` | — |
| [SRC-4FFD5AFC54-L000150](../../scripts/run_answer_quality_benchmark.py#L150) | 150 | `"    allowed_statuses = {"` | — |
| [SRC-4FFD5AFC54-L000151](../../scripts/run_answer_quality_benchmark.py#L151) | 151 | `"        \"web_search\": {"` | — |
| [SRC-4FFD5AFC54-L000152](../../scripts/run_answer_quality_benchmark.py#L152) | 152 | `"            \"failed\", \"unknown\", \"not_attempted\", \"counter_mismatch\","` | — |
| [SRC-4FFD5AFC54-L000153](../../scripts/run_answer_quality_benchmark.py#L153) | 153 | `"            \"completed_with_results\", \"completed_no_usable_results\","` | — |
| [SRC-4FFD5AFC54-L000154](../../scripts/run_answer_quality_benchmark.py#L154) | 154 | `"        },"` | — |
| [SRC-4FFD5AFC54-L000155](../../scripts/run_answer_quality_benchmark.py#L155) | 155 | `"        \"page_fetch\": {"` | — |
| [SRC-4FFD5AFC54-L000156](../../scripts/run_answer_quality_benchmark.py#L156) | 156 | `"            \"counter_mismatch\", \"completed_with_read_pages\","` | — |
| [SRC-4FFD5AFC54-L000157](../../scripts/run_answer_quality_benchmark.py#L157) | 157 | `"            \"attempted_no_readable_pages\", \"unknown\","` | — |
| [SRC-4FFD5AFC54-L000158](../../scripts/run_answer_quality_benchmark.py#L158) | 158 | `"            \"not_attempted_after_search_error\", \"not_attempted_no_fetchable_candidates\","` | — |
| [SRC-4FFD5AFC54-L000159](../../scripts/run_answer_quality_benchmark.py#L159) | 159 | `"            \"not_attempted\","` | — |
| [SRC-4FFD5AFC54-L000160](../../scripts/run_answer_quality_benchmark.py#L160) | 160 | `"        },"` | — |
| [SRC-4FFD5AFC54-L000161](../../scripts/run_answer_quality_benchmark.py#L161) | 161 | `"        \"public_social_search_if_configured\": {"` | — |
| [SRC-4FFD5AFC54-L000162](../../scripts/run_answer_quality_benchmark.py#L162) | 162 | `"            \"completed_with_results\", \"failed\", \"unknown\","` | — |
| [SRC-4FFD5AFC54-L000163](../../scripts/run_answer_quality_benchmark.py#L163) | 163 | `"            \"completed_no_usable_results\", \"not_attempted\", \"not_configured\","` | — |
| [SRC-4FFD5AFC54-L000164](../../scripts/run_answer_quality_benchmark.py#L164) | 164 | `"        },"` | — |
| [SRC-4FFD5AFC54-L000165](../../scripts/run_answer_quality_benchmark.py#L165) | 165 | `"        \"language_model_generation_if_configured\": {"` | — |
| [SRC-4FFD5AFC54-L000166](../../scripts/run_answer_quality_benchmark.py#L166) | 166 | `"            \"completed\", \"not_configured\", \"failed\", \"not_attempted\","` | — |
| [SRC-4FFD5AFC54-L000167](../../scripts/run_answer_quality_benchmark.py#L167) | 167 | `"            \"not_attempted_no_evidence\", \"unknown\","` | — |
| [SRC-4FFD5AFC54-L000168](../../scripts/run_answer_quality_benchmark.py#L168) | 168 | `"        },"` | — |
| [SRC-4FFD5AFC54-L000169](../../scripts/run_answer_quality_benchmark.py#L169) | 169 | `"        \"claim_review_if_configured\": {"` | — |
| [SRC-4FFD5AFC54-L000170](../../scripts/run_answer_quality_benchmark.py#L170) | 170 | `"            \"completed_model_assisted_review\", \"failed\","` | — |
| [SRC-4FFD5AFC54-L000171](../../scripts/run_answer_quality_benchmark.py#L171) | 171 | `"            \"not_attempted_no_evidence\", \"not_attempted\", \"unknown\","` | — |
| [SRC-4FFD5AFC54-L000172](../../scripts/run_answer_quality_benchmark.py#L172) | 172 | `"        },"` | — |
| [SRC-4FFD5AFC54-L000173](../../scripts/run_answer_quality_benchmark.py#L173) | 173 | `"    }"` | — |
| [SRC-4FFD5AFC54-L000174](../../scripts/run_answer_quality_benchmark.py#L174) | 174 | `"    successful_statuses = {"` | — |
| [SRC-4FFD5AFC54-L000175](../../scripts/run_answer_quality_benchmark.py#L175) | 175 | `"        \"web_search\": {\"completed_with_results\"},"` | — |
| [SRC-4FFD5AFC54-L000176](../../scripts/run_answer_quality_benchmark.py#L176) | 176 | `"        \"page_fetch\": {\"completed_with_read_pages\"},"` | — |
| [SRC-4FFD5AFC54-L000177](../../scripts/run_answer_quality_benchmark.py#L177) | 177 | `"        \"public_social_search_if_configured\": {\"completed_with_results\"},"` | — |
| [SRC-4FFD5AFC54-L000178](../../scripts/run_answer_quality_benchmark.py#L178) | 178 | `"        \"language_model_generation_if_configured\": {\"completed\"},"` | — |
| [SRC-4FFD5AFC54-L000179](../../scripts/run_answer_quality_benchmark.py#L179) | 179 | `"        \"claim_review_if_configured\": {\"completed_model_assisted_review\"},"` | — |
| [SRC-4FFD5AFC54-L000180](../../scripts/run_answer_quality_benchmark.py#L180) | 180 | `"    }"` | — |
| [SRC-4FFD5AFC54-L000181](../../scripts/run_answer_quality_benchmark.py#L181) | 181 | `"    required_tool_statuses = []"` | — |
| [SRC-4FFD5AFC54-L000182](../../scripts/run_answer_quality_benchmark.py#L182) | 182 | `"    required_name_set = set(required_tool_names)"` | — |
| [SRC-4FFD5AFC54-L000183](../../scripts/run_answer_quality_benchmark.py#L183) | 183 | `"    reported_required_names = {"` | — |
| [SRC-4FFD5AFC54-L000184](../../scripts/run_answer_quality_benchmark.py#L184) | 184 | `"        row.get(\"tool\")"` | — |
| [SRC-4FFD5AFC54-L000185](../../scripts/run_answer_quality_benchmark.py#L185) | 185 | `"        for row in matrix_rows"` | — |
| [SRC-4FFD5AFC54-L000186](../../scripts/run_answer_quality_benchmark.py#L186) | 186 | `"        if row.get(\"required_by_task_spec\") is True and isinstance(row.get(\"tool\"), str)"` | — |
| [SRC-4FFD5AFC54-L000187](../../scripts/run_answer_quality_benchmark.py#L187) | 187 | `"    }"` | — |
| [SRC-4FFD5AFC54-L000188](../../scripts/run_answer_quality_benchmark.py#L188) | 188 | `"    required_tool_matrix_complete = ("` | — |
| [SRC-4FFD5AFC54-L000189](../../scripts/run_answer_quality_benchmark.py#L189) | 189 | `"        required_tool_matrix_present"` | — |
| [SRC-4FFD5AFC54-L000190](../../scripts/run_answer_quality_benchmark.py#L190) | 190 | `"        and len(required_tool_names) == len(required_name_set)"` | — |
| [SRC-4FFD5AFC54-L000191](../../scripts/run_answer_quality_benchmark.py#L191) | 191 | `"        and reported_required_names == required_name_set"` | — |
| [SRC-4FFD5AFC54-L000192](../../scripts/run_answer_quality_benchmark.py#L192) | 192 | `"    )"` | — |
| [SRC-4FFD5AFC54-L000193](../../scripts/run_answer_quality_benchmark.py#L193) | 193 | `"    for tool in dict.fromkeys(required_tool_names):"` | — |
| [SRC-4FFD5AFC54-L000194](../../scripts/run_answer_quality_benchmark.py#L194) | 194 | `"        matches = ["` | — |
| [SRC-4FFD5AFC54-L000195](../../scripts/run_answer_quality_benchmark.py#L195) | 195 | `"            row for row in matrix_rows"` | — |
| [SRC-4FFD5AFC54-L000196](../../scripts/run_answer_quality_benchmark.py#L196) | 196 | `"            if row.get(\"tool\") == tool and row.get(\"required_by_task_spec\") is True"` | — |
| [SRC-4FFD5AFC54-L000197](../../scripts/run_answer_quality_benchmark.py#L197) | 197 | `"        ]"` | — |
| [SRC-4FFD5AFC54-L000198](../../scripts/run_answer_quality_benchmark.py#L198) | 198 | `"        if len(matches) == 0:"` | — |
| [SRC-4FFD5AFC54-L000199](../../scripts/run_answer_quality_benchmark.py#L199) | 199 | `"            status = \"missing_matrix_row\""` | — |
| [SRC-4FFD5AFC54-L000200](../../scripts/run_answer_quality_benchmark.py#L200) | 200 | `"            status_observed = False"` | — |
| [SRC-4FFD5AFC54-L000201](../../scripts/run_answer_quality_benchmark.py#L201) | 201 | `"            successful = False"` | — |
| [SRC-4FFD5AFC54-L000202](../../scripts/run_answer_quality_benchmark.py#L202) | 202 | `"            required_tool_matrix_complete = False"` | — |
| [SRC-4FFD5AFC54-L000203](../../scripts/run_answer_quality_benchmark.py#L203) | 203 | `"        elif len(matches) > 1:"` | — |
| [SRC-4FFD5AFC54-L000204](../../scripts/run_answer_quality_benchmark.py#L204) | 204 | `"            status = \"duplicate_matrix_rows\""` | — |
| [SRC-4FFD5AFC54-L000205](../../scripts/run_answer_quality_benchmark.py#L205) | 205 | `"            status_observed = False"` | — |
| [SRC-4FFD5AFC54-L000206](../../scripts/run_answer_quality_benchmark.py#L206) | 206 | `"            successful = False"` | — |
| [SRC-4FFD5AFC54-L000207](../../scripts/run_answer_quality_benchmark.py#L207) | 207 | `"            required_tool_matrix_complete = False"` | — |
| [SRC-4FFD5AFC54-L000208](../../scripts/run_answer_quality_benchmark.py#L208) | 208 | `"        else:"` | — |
| [SRC-4FFD5AFC54-L000209](../../scripts/run_answer_quality_benchmark.py#L209) | 209 | `"            raw_status = matches[0].get(\"status\")"` | — |
| [SRC-4FFD5AFC54-L000210](../../scripts/run_answer_quality_benchmark.py#L210) | 210 | `"            status_observed = isinstance(raw_status, str) and bool(raw_status.strip())"` | — |
| [SRC-4FFD5AFC54-L000211](../../scripts/run_answer_quality_benchmark.py#L211) | 211 | `"            status = raw_status if status_observed else \"missing_status\""` | — |
| [SRC-4FFD5AFC54-L000212](../../scripts/run_answer_quality_benchmark.py#L212) | 212 | `"            status_valid = status_observed and status in allowed_statuses.get(tool, set())"` | — |
| [SRC-4FFD5AFC54-L000213](../../scripts/run_answer_quality_benchmark.py#L213) | 213 | `"            successful = status_valid and status in successful_statuses.get(tool, set())"` | — |
| [SRC-4FFD5AFC54-L000214](../../scripts/run_answer_quality_benchmark.py#L214) | 214 | `"            if not status_valid:"` | — |
| [SRC-4FFD5AFC54-L000215](../../scripts/run_answer_quality_benchmark.py#L215) | 215 | `"                required_tool_matrix_complete = False"` | — |
| [SRC-4FFD5AFC54-L000216](../../scripts/run_answer_quality_benchmark.py#L216) | 216 | `"        required_tool_statuses.append({"` | — |
| [SRC-4FFD5AFC54-L000217](../../scripts/run_answer_quality_benchmark.py#L217) | 217 | `"            \"tool\": tool,"` | — |
| [SRC-4FFD5AFC54-L000218](../../scripts/run_answer_quality_benchmark.py#L218) | 218 | `"            \"status\": status,"` | — |
| [SRC-4FFD5AFC54-L000219](../../scripts/run_answer_quality_benchmark.py#L219) | 219 | `"            \"status_observed\": status_observed,"` | — |
| [SRC-4FFD5AFC54-L000220](../../scripts/run_answer_quality_benchmark.py#L220) | 220 | `"            \"status_valid\": status_valid if len(matches) == 1 else False,"` | — |
| [SRC-4FFD5AFC54-L000221](../../scripts/run_answer_quality_benchmark.py#L221) | 221 | `"            \"successful_completion\": successful,"` | — |
| [SRC-4FFD5AFC54-L000222](../../scripts/run_answer_quality_benchmark.py#L222) | 222 | `"        })"` | — |
| [SRC-4FFD5AFC54-L000223](../../scripts/run_answer_quality_benchmark.py#L223) | 223 | `"    if expected_strategy == \"web_search\" and \"web_search\" not in required_name_set:"` | — |
| [SRC-4FFD5AFC54-L000224](../../scripts/run_answer_quality_benchmark.py#L224) | 224 | `"        required_tool_matrix_complete = False"` | — |
| [SRC-4FFD5AFC54-L000225](../../scripts/run_answer_quality_benchmark.py#L225) | 225 | `""` | — |
| [SRC-4FFD5AFC54-L000226](../../scripts/run_answer_quality_benchmark.py#L226) | 226 | `"    calls = _model_calls_from_payload(payload)"` | — |
| [SRC-4FFD5AFC54-L000227](../../scripts/run_answer_quality_benchmark.py#L227) | 227 | `"    reported_costs = []"` | — |
| [SRC-4FFD5AFC54-L000228](../../scripts/run_answer_quality_benchmark.py#L228) | 228 | `"    for call in calls:"` | — |
| [SRC-4FFD5AFC54-L000229](../../scripts/run_answer_quality_benchmark.py#L229) | 229 | `"        usage = call.get(\"provider_usage\")"` | — |
| [SRC-4FFD5AFC54-L000230](../../scripts/run_answer_quality_benchmark.py#L230) | 230 | `"        if not isinstance(usage, dict):"` | — |
| [SRC-4FFD5AFC54-L000231](../../scripts/run_answer_quality_benchmark.py#L231) | 231 | `"            continue"` | — |
| [SRC-4FFD5AFC54-L000232](../../scripts/run_answer_quality_benchmark.py#L232) | 232 | `"        cost = _finite_nonnegative_number(usage.get(\"cost_usd\"))"` | — |
| [SRC-4FFD5AFC54-L000233](../../scripts/run_answer_quality_benchmark.py#L233) | 233 | `"        if cost is not None:"` | — |
| [SRC-4FFD5AFC54-L000234](../../scripts/run_answer_quality_benchmark.py#L234) | 234 | `"            reported_costs.append(cost)"` | — |
| [SRC-4FFD5AFC54-L000235](../../scripts/run_answer_quality_benchmark.py#L235) | 235 | `""` | — |
| [SRC-4FFD5AFC54-L000236](../../scripts/run_answer_quality_benchmark.py#L236) | 236 | `"    if not calls:"` | — |
| [SRC-4FFD5AFC54-L000237](../../scripts/run_answer_quality_benchmark.py#L237) | 237 | `"        cost_status = \"NO_MODEL_CALL_METADATA\""` | — |
| [SRC-4FFD5AFC54-L000238](../../scripts/run_answer_quality_benchmark.py#L238) | 238 | `"    elif len(reported_costs) == len(calls):"` | — |
| [SRC-4FFD5AFC54-L000239](../../scripts/run_answer_quality_benchmark.py#L239) | 239 | `"        cost_status = \"COMPLETE_FOR_RETURNED_MODEL_CALLS\""` | — |
| [SRC-4FFD5AFC54-L000240](../../scripts/run_answer_quality_benchmark.py#L240) | 240 | `"    elif reported_costs:"` | — |
| [SRC-4FFD5AFC54-L000241](../../scripts/run_answer_quality_benchmark.py#L241) | 241 | `"        cost_status = \"PARTIAL_PROVIDER_REPORTED_MODEL_COST\""` | — |
| [SRC-4FFD5AFC54-L000242](../../scripts/run_answer_quality_benchmark.py#L242) | 242 | `"    else:"` | — |
| [SRC-4FFD5AFC54-L000243](../../scripts/run_answer_quality_benchmark.py#L243) | 243 | `"        cost_status = \"PROVIDER_COST_NOT_REPORTED\""` | — |
| [SRC-4FFD5AFC54-L000244](../../scripts/run_answer_quality_benchmark.py#L244) | 244 | `""` | — |
| [SRC-4FFD5AFC54-L000245](../../scripts/run_answer_quality_benchmark.py#L245) | 245 | `"    return {"` | — |
| [SRC-4FFD5AFC54-L000246](../../scripts/run_answer_quality_benchmark.py#L246) | 246 | `"        \"search_outcome\": outcome if isinstance(outcome, str) else \"unknown\","` | — |
| [SRC-4FFD5AFC54-L000247](../../scripts/run_answer_quality_benchmark.py#L247) | 247 | `"        \"pipeline_completion_status\": pipeline if isinstance(pipeline, str) else \"unknown\","` | — |
| [SRC-4FFD5AFC54-L000248](../../scripts/run_answer_quality_benchmark.py#L248) | 248 | `"        \"tool_status\": tool_status,"` | — |
| [SRC-4FFD5AFC54-L000249](../../scripts/run_answer_quality_benchmark.py#L249) | 249 | `"        \"required_tool_statuses\": required_tool_statuses,"` | — |
| [SRC-4FFD5AFC54-L000250](../../scripts/run_answer_quality_benchmark.py#L250) | 250 | `"        \"required_tool_success_count\": sum(1 for row in required_tool_statuses if row[\"successful_completion\"]),"` | — |
| [SRC-4FFD5AFC54-L000251](../../scripts/run_answer_quality_benchmark.py#L251) | 251 | `"        \"required_tool_count\": len(required_tool_statuses),"` | — |
| [SRC-4FFD5AFC54-L000252](../../scripts/run_answer_quality_benchmark.py#L252) | 252 | `"        \"required_tool_success_rate\": ("` | — |
| [SRC-4FFD5AFC54-L000253](../../scripts/run_answer_quality_benchmark.py#L253) | 253 | `"            round("` | — |
| [SRC-4FFD5AFC54-L000254](../../scripts/run_answer_quality_benchmark.py#L254) | 254 | `"                sum(1 for row in required_tool_statuses if row[\"successful_completion\"])"` | — |
| [SRC-4FFD5AFC54-L000255](../../scripts/run_answer_quality_benchmark.py#L255) | 255 | `"                / len(required_tool_statuses),"` | — |
| [SRC-4FFD5AFC54-L000256](../../scripts/run_answer_quality_benchmark.py#L256) | 256 | `"                4,"` | — |
| [SRC-4FFD5AFC54-L000257](../../scripts/run_answer_quality_benchmark.py#L257) | 257 | `"            )"` | — |
| [SRC-4FFD5AFC54-L000258](../../scripts/run_answer_quality_benchmark.py#L258) | 258 | `"            if required_tool_statuses"` | — |
| [SRC-4FFD5AFC54-L000259](../../scripts/run_answer_quality_benchmark.py#L259) | 259 | `"            else None"` | — |
| [SRC-4FFD5AFC54-L000260](../../scripts/run_answer_quality_benchmark.py#L260) | 260 | `"        ),"` | — |
| [SRC-4FFD5AFC54-L000261](../../scripts/run_answer_quality_benchmark.py#L261) | 261 | `"        \"required_tool_status_metrics_status\": ("` | — |
| [SRC-4FFD5AFC54-L000262](../../scripts/run_answer_quality_benchmark.py#L262) | 262 | `"            \"NOT_MEASURED_TOOL_REQUIREMENTS_OR_MATRIX_UNKNOWN\""` | — |
| [SRC-4FFD5AFC54-L000263](../../scripts/run_answer_quality_benchmark.py#L263) | 263 | `"            if not required_tool_matrix_present"` | — |
| [SRC-4FFD5AFC54-L000264](../../scripts/run_answer_quality_benchmark.py#L264) | 264 | `"            else \"SCORED_FROM_TOOL_EXECUTION_MATRIX\""` | — |
| [SRC-4FFD5AFC54-L000265](../../scripts/run_answer_quality_benchmark.py#L265) | 265 | `"            if required_tool_matrix_complete"` | — |
| [SRC-4FFD5AFC54-L000266](../../scripts/run_answer_quality_benchmark.py#L266) | 266 | `"            else \"INCOMPLETE_TOOL_STATUS_MATRIX\""` | — |
| [SRC-4FFD5AFC54-L000267](../../scripts/run_answer_quality_benchmark.py#L267) | 267 | `"        ),"` | — |
| [SRC-4FFD5AFC54-L000268](../../scripts/run_answer_quality_benchmark.py#L268) | 268 | `"        \"required_tool_matrix_present\": required_tool_matrix_present,"` | — |
| [SRC-4FFD5AFC54-L000269](../../scripts/run_answer_quality_benchmark.py#L269) | 269 | `"        \"required_tool_matrix_complete\": required_tool_matrix_complete,"` | — |
| [SRC-4FFD5AFC54-L000270](../../scripts/run_answer_quality_benchmark.py#L270) | 270 | `"        \"source_count\": source_count,"` | — |
| [SRC-4FFD5AFC54-L000271](../../scripts/run_answer_quality_benchmark.py#L271) | 271 | `"        \"model_call_count\": len(calls),"` | — |
| [SRC-4FFD5AFC54-L000272](../../scripts/run_answer_quality_benchmark.py#L272) | 272 | `"        \"provider_reported_model_cost_usd\": round(sum(reported_costs), 10) if reported_costs else None,"` | — |
| [SRC-4FFD5AFC54-L000273](../../scripts/run_answer_quality_benchmark.py#L273) | 273 | `"        \"provider_reported_model_cost_call_count\": len(reported_costs),"` | — |
| [SRC-4FFD5AFC54-L000274](../../scripts/run_answer_quality_benchmark.py#L274) | 274 | `"        \"provider_reported_model_cost_status\": cost_status,"` | — |
| [SRC-4FFD5AFC54-L000275](../../scripts/run_answer_quality_benchmark.py#L275) | 275 | `"        \"request_cost_usd\": None,"` | — |
| [SRC-4FFD5AFC54-L000276](../../scripts/run_answer_quality_benchmark.py#L276) | 276 | `"        \"request_cost_status\": \"NOT_MEASURED_TOTAL_CONNECTOR_COSTS_NOT_EXPOSED\","` | — |
| [SRC-4FFD5AFC54-L000277](../../scripts/run_answer_quality_benchmark.py#L277) | 277 | `"    }"` | — |
| [SRC-4FFD5AFC54-L000278](../../scripts/run_answer_quality_benchmark.py#L278) | 278 | `""` | — |
| [SRC-4FFD5AFC54-L000279](../../scripts/run_answer_quality_benchmark.py#L279) | 279 | `""` | — |
| [SRC-4FFD5AFC54-L000280](../../scripts/run_answer_quality_benchmark.py#L280) | 280 | `"def validate_base_url(base_url: str, *, token_present: bool = False) -> str:"` | — |
| [SRC-4FFD5AFC54-L000281](../../scripts/run_answer_quality_benchmark.py#L281) | 281 | `"    \"\"\"Validate and normalize an API origin before any request can carry a token.\"\"\""` | — |
| [SRC-4FFD5AFC54-L000282](../../scripts/run_answer_quality_benchmark.py#L282) | 282 | `"    if not isinstance(base_url, str) or not base_url.strip():"` | — |
| [SRC-4FFD5AFC54-L000283](../../scripts/run_answer_quality_benchmark.py#L283) | 283 | `"        raise ValueError(\"Base URL must be a non-empty HTTP(S) origin.\")"` | — |
| [SRC-4FFD5AFC54-L000284](../../scripts/run_answer_quality_benchmark.py#L284) | 284 | `"    try:"` | — |
| [SRC-4FFD5AFC54-L000285](../../scripts/run_answer_quality_benchmark.py#L285) | 285 | `"        parsed = urllib.parse.urlsplit(base_url.strip())"` | — |
| [SRC-4FFD5AFC54-L000286](../../scripts/run_answer_quality_benchmark.py#L286) | 286 | `"        scheme = parsed.scheme.lower()"` | — |
| [SRC-4FFD5AFC54-L000287](../../scripts/run_answer_quality_benchmark.py#L287) | 287 | `"        host = (parsed.hostname or \"\").lower().rstrip(\".\")"` | — |
| [SRC-4FFD5AFC54-L000288](../../scripts/run_answer_quality_benchmark.py#L288) | 288 | `"        port = parsed.port"` | — |
| [SRC-4FFD5AFC54-L000289](../../scripts/run_answer_quality_benchmark.py#L289) | 289 | `"    except ValueError as exc:"` | — |
| [SRC-4FFD5AFC54-L000290](../../scripts/run_answer_quality_benchmark.py#L290) | 290 | `"        raise ValueError(\"Base URL is malformed.\") from exc"` | — |
| [SRC-4FFD5AFC54-L000291](../../scripts/run_answer_quality_benchmark.py#L291) | 291 | `""` | — |
| [SRC-4FFD5AFC54-L000292](../../scripts/run_answer_quality_benchmark.py#L292) | 292 | `"    if scheme not in {\"http\", \"https\"} or not host:"` | — |
| [SRC-4FFD5AFC54-L000293](../../scripts/run_answer_quality_benchmark.py#L293) | 293 | `"        raise ValueError(\"Base URL must use HTTP or HTTPS and include a hostname.\")"` | — |
| [SRC-4FFD5AFC54-L000294](../../scripts/run_answer_quality_benchmark.py#L294) | 294 | `"    if parsed.username is not None or parsed.password is not None:"` | — |
| [SRC-4FFD5AFC54-L000295](../../scripts/run_answer_quality_benchmark.py#L295) | 295 | `"        raise ValueError(\"Base URL must not include a username or password.\")"` | — |
| [SRC-4FFD5AFC54-L000296](../../scripts/run_answer_quality_benchmark.py#L296) | 296 | `"    if parsed.path not in {\"\", \"/\"} or parsed.query or parsed.fragment:"` | — |
| [SRC-4FFD5AFC54-L000297](../../scripts/run_answer_quality_benchmark.py#L297) | 297 | `"        raise ValueError(\"Base URL must contain only the origin, without path, query, or fragment.\")"` | — |
| [SRC-4FFD5AFC54-L000298](../../scripts/run_answer_quality_benchmark.py#L298) | 298 | `""` | — |
| [SRC-4FFD5AFC54-L000299](../../scripts/run_answer_quality_benchmark.py#L299) | 299 | `"    loopback = host == \"localhost\""` | — |
| [SRC-4FFD5AFC54-L000300](../../scripts/run_answer_quality_benchmark.py#L300) | 300 | `"    try:"` | — |
| [SRC-4FFD5AFC54-L000301](../../scripts/run_answer_quality_benchmark.py#L301) | 301 | `"        loopback = ipaddress.ip_address(host).is_loopback"` | — |
| [SRC-4FFD5AFC54-L000302](../../scripts/run_answer_quality_benchmark.py#L302) | 302 | `"    except ValueError:"` | — |
| [SRC-4FFD5AFC54-L000303](../../scripts/run_answer_quality_benchmark.py#L303) | 303 | `"        pass"` | — |
| [SRC-4FFD5AFC54-L000304](../../scripts/run_answer_quality_benchmark.py#L304) | 304 | `""` | — |
| [SRC-4FFD5AFC54-L000305](../../scripts/run_answer_quality_benchmark.py#L305) | 305 | `"    if scheme == \"http\" and not loopback:"` | — |
| [SRC-4FFD5AFC54-L000306](../../scripts/run_answer_quality_benchmark.py#L306) | 306 | `"        raise ValueError(\"Plain HTTP is allowed only for localhost or a loopback IP.\")"` | — |
| [SRC-4FFD5AFC54-L000307](../../scripts/run_answer_quality_benchmark.py#L307) | 307 | `""` | — |
| [SRC-4FFD5AFC54-L000308](../../scripts/run_answer_quality_benchmark.py#L308) | 308 | `"    if (scheme == \"https\" and port == 443) or (scheme == \"http\" and port == 80):"` | — |
| [SRC-4FFD5AFC54-L000309](../../scripts/run_answer_quality_benchmark.py#L309) | 309 | `"        port = None"` | — |
| [SRC-4FFD5AFC54-L000310](../../scripts/run_answer_quality_benchmark.py#L310) | 310 | `"    host_for_origin = f\"[{host}]\" if \":\" in host else host"` | — |
| [SRC-4FFD5AFC54-L000311](../../scripts/run_answer_quality_benchmark.py#L311) | 311 | `"    origin = f\"{scheme}://{host_for_origin}\" + (f\":{port}\" if port is not None else \"\")"` | — |
| [SRC-4FFD5AFC54-L000312](../../scripts/run_answer_quality_benchmark.py#L312) | 312 | `""` | — |
| [SRC-4FFD5AFC54-L000313](../../scripts/run_answer_quality_benchmark.py#L313) | 313 | `"    if token_present and not loopback:"` | — |
| [SRC-4FFD5AFC54-L000314](../../scripts/run_answer_quality_benchmark.py#L314) | 314 | `"        allowed = os.getenv(\"OMARAI_BENCHMARK_ALLOWED_ORIGIN\", \"\").strip()"` | — |
| [SRC-4FFD5AFC54-L000315](../../scripts/run_answer_quality_benchmark.py#L315) | 315 | `"        if not allowed:"` | — |
| [SRC-4FFD5AFC54-L000316](../../scripts/run_answer_quality_benchmark.py#L316) | 316 | `"            raise ValueError("` | — |
| [SRC-4FFD5AFC54-L000317](../../scripts/run_answer_quality_benchmark.py#L317) | 317 | `"                \"A bearer token requires OMARAI_BENCHMARK_ALLOWED_ORIGIN to match \""` | — |
| [SRC-4FFD5AFC54-L000318](../../scripts/run_answer_quality_benchmark.py#L318) | 318 | `"                \"the exact HTTPS deployment origin.\""` | — |
| [SRC-4FFD5AFC54-L000319](../../scripts/run_answer_quality_benchmark.py#L319) | 319 | `"            )"` | — |
| [SRC-4FFD5AFC54-L000320](../../scripts/run_answer_quality_benchmark.py#L320) | 320 | `"        allowed_origin = validate_base_url(allowed, token_present=False)"` | — |
| [SRC-4FFD5AFC54-L000321](../../scripts/run_answer_quality_benchmark.py#L321) | 321 | `"        if allowed_origin != origin:"` | — |
| [SRC-4FFD5AFC54-L000322](../../scripts/run_answer_quality_benchmark.py#L322) | 322 | `"            raise ValueError("` | — |
| [SRC-4FFD5AFC54-L000323](../../scripts/run_answer_quality_benchmark.py#L323) | 323 | `"                \"Refusing to send the bearer token: base URL does not match \""` | — |
| [SRC-4FFD5AFC54-L000324](../../scripts/run_answer_quality_benchmark.py#L324) | 324 | `"                \"OMARAI_BENCHMARK_ALLOWED_ORIGIN.\""` | — |
| [SRC-4FFD5AFC54-L000325](../../scripts/run_answer_quality_benchmark.py#L325) | 325 | `"            )"` | — |
| [SRC-4FFD5AFC54-L000326](../../scripts/run_answer_quality_benchmark.py#L326) | 326 | `"    return origin"` | — |
| [SRC-4FFD5AFC54-L000327](../../scripts/run_answer_quality_benchmark.py#L327) | 327 | `""` | — |
| [SRC-4FFD5AFC54-L000328](../../scripts/run_answer_quality_benchmark.py#L328) | 328 | `""` | — |
| [SRC-4FFD5AFC54-L000329](../../scripts/run_answer_quality_benchmark.py#L329) | 329 | `"class _NoRedirectHandler(urllib.request.HTTPRedirectHandler):"` | — |
| [SRC-4FFD5AFC54-L000330](../../scripts/run_answer_quality_benchmark.py#L330) | 330 | `"    \"\"\"Do not follow redirects; the bearer token must never move to another origin.\"\"\""` | — |
| [SRC-4FFD5AFC54-L000331](../../scripts/run_answer_quality_benchmark.py#L331) | 331 | `""` | — |
| [SRC-4FFD5AFC54-L000332](../../scripts/run_answer_quality_benchmark.py#L332) | 332 | `"    def redirect_request(self, req, fp, code, msg, headers, newurl):"` | — |
| [SRC-4FFD5AFC54-L000333](../../scripts/run_answer_quality_benchmark.py#L333) | 333 | `"        return None"` | — |
| [SRC-4FFD5AFC54-L000334](../../scripts/run_answer_quality_benchmark.py#L334) | 334 | `""` | — |
| [SRC-4FFD5AFC54-L000335](../../scripts/run_answer_quality_benchmark.py#L335) | 335 | `""` | — |
| [SRC-4FFD5AFC54-L000336](../../scripts/run_answer_quality_benchmark.py#L336) | 336 | `"_NO_REDIRECT_OPENER = urllib.request.build_opener(_NoRedirectHandler())"` | — |
| [SRC-4FFD5AFC54-L000337](../../scripts/run_answer_quality_benchmark.py#L337) | 337 | `""` | — |
| [SRC-4FFD5AFC54-L000338](../../scripts/run_answer_quality_benchmark.py#L338) | 338 | `"REQUIRED_FIELDS = {"` | — |
| [SRC-4FFD5AFC54-L000339](../../scripts/run_answer_quality_benchmark.py#L339) | 339 | `"    \"case_id\","` | — |
| [SRC-4FFD5AFC54-L000340](../../scripts/run_answer_quality_benchmark.py#L340) | 340 | `"    \"category\","` | — |
| [SRC-4FFD5AFC54-L000341](../../scripts/run_answer_quality_benchmark.py#L341) | 341 | `"    \"language\","` | — |
| [SRC-4FFD5AFC54-L000342](../../scripts/run_answer_quality_benchmark.py#L342) | 342 | `"    \"question\","` | — |
| [SRC-4FFD5AFC54-L000343](../../scripts/run_answer_quality_benchmark.py#L343) | 343 | `"    \"expected_strategy\","` | — |
| [SRC-4FFD5AFC54-L000344](../../scripts/run_answer_quality_benchmark.py#L344) | 344 | `"    \"required_behaviors\","` | — |
| [SRC-4FFD5AFC54-L000345](../../scripts/run_answer_quality_benchmark.py#L345) | 345 | `"    \"forbidden_behaviors\","` | — |
| [SRC-4FFD5AFC54-L000346](../../scripts/run_answer_quality_benchmark.py#L346) | 346 | `"    \"evidence_fixture\","` | — |
| [SRC-4FFD5AFC54-L000347](../../scripts/run_answer_quality_benchmark.py#L347) | 347 | `"    \"failure_conditions\","` | — |
| [SRC-4FFD5AFC54-L000348](../../scripts/run_answer_quality_benchmark.py#L348) | 348 | `"    \"evaluation_mode\","` | — |
| [SRC-4FFD5AFC54-L000349](../../scripts/run_answer_quality_benchmark.py#L349) | 349 | `"}"` | — |
| [SRC-4FFD5AFC54-L000350](../../scripts/run_answer_quality_benchmark.py#L350) | 350 | `"ALLOWED_STRATEGIES = {\"local\", \"model_no_search\", \"web_search\", \"clarify\"}"` | — |
| [SRC-4FFD5AFC54-L000351](../../scripts/run_answer_quality_benchmark.py#L351) | 351 | `"ALLOWED_EVAL_MODES = {\"deterministic_structure\", \"fixture_assisted\", \"human_judgment\"}"` | — |
| [SRC-4FFD5AFC54-L000352](../../scripts/run_answer_quality_benchmark.py#L352) | 352 | `""` | — |
| [SRC-4FFD5AFC54-L000353](../../scripts/run_answer_quality_benchmark.py#L353) | 353 | `""` | — |
| [SRC-4FFD5AFC54-L000354](../../scripts/run_answer_quality_benchmark.py#L354) | 354 | `"def _utc_now() -> str:"` | — |
| [SRC-4FFD5AFC54-L000355](../../scripts/run_answer_quality_benchmark.py#L355) | 355 | `"    return datetime.now(UTC).isoformat(timespec=\"seconds\")"` | — |
| [SRC-4FFD5AFC54-L000356](../../scripts/run_answer_quality_benchmark.py#L356) | 356 | `""` | — |
| [SRC-4FFD5AFC54-L000357](../../scripts/run_answer_quality_benchmark.py#L357) | 357 | `""` | — |
| [SRC-4FFD5AFC54-L000358](../../scripts/run_answer_quality_benchmark.py#L358) | 358 | `"def load_corpus(path: Path) -> dict:"` | — |
| [SRC-4FFD5AFC54-L000359](../../scripts/run_answer_quality_benchmark.py#L359) | 359 | `"    if not path.is_file():"` | — |
| [SRC-4FFD5AFC54-L000360](../../scripts/run_answer_quality_benchmark.py#L360) | 360 | `"        raise FileNotFoundError(f\"Corpus not found: {path}\")"` | — |
| [SRC-4FFD5AFC54-L000361](../../scripts/run_answer_quality_benchmark.py#L361) | 361 | `"    data = json.loads(path.read_text(encoding=\"utf-8\"))"` | — |
| [SRC-4FFD5AFC54-L000362](../../scripts/run_answer_quality_benchmark.py#L362) | 362 | `"    if not isinstance(data, dict) or not isinstance(data.get(\"cases\"), list):"` | — |
| [SRC-4FFD5AFC54-L000363](../../scripts/run_answer_quality_benchmark.py#L363) | 363 | `"        raise TypeError(\"Corpus root must be an object with a cases array\")"` | — |
| [SRC-4FFD5AFC54-L000364](../../scripts/run_answer_quality_benchmark.py#L364) | 364 | `"    if data.get(\"parts\"):"` | — |
| [SRC-4FFD5AFC54-L000365](../../scripts/run_answer_quality_benchmark.py#L365) | 365 | `"        raise ValueError(\"Incomplete shard index is not accepted; use merged cases[] corpus\")"` | — |
| [SRC-4FFD5AFC54-L000366](../../scripts/run_answer_quality_benchmark.py#L366) | 366 | `"    return data"` | — |
| [SRC-4FFD5AFC54-L000367](../../scripts/run_answer_quality_benchmark.py#L367) | 367 | `""` | — |
| [SRC-4FFD5AFC54-L000368](../../scripts/run_answer_quality_benchmark.py#L368) | 368 | `""` | — |
| [SRC-4FFD5AFC54-L000369](../../scripts/run_answer_quality_benchmark.py#L369) | 369 | `"def validate_corpus(data: dict) -> list[str]:"` | — |
| [SRC-4FFD5AFC54-L000370](../../scripts/run_answer_quality_benchmark.py#L370) | 370 | `"    \"\"\"Return a list of human-readable problems (empty => OK).\"\"\""` | — |
| [SRC-4FFD5AFC54-L000371](../../scripts/run_answer_quality_benchmark.py#L371) | 371 | `"    problems: list[str] = []"` | — |
| [SRC-4FFD5AFC54-L000372](../../scripts/run_answer_quality_benchmark.py#L372) | 372 | `"    cases = data.get(\"cases\") or []"` | — |
| [SRC-4FFD5AFC54-L000373](../../scripts/run_answer_quality_benchmark.py#L373) | 373 | `"    if data.get(\"case_count\") != len(cases):"` | — |
| [SRC-4FFD5AFC54-L000374](../../scripts/run_answer_quality_benchmark.py#L374) | 374 | `"        problems.append("` | — |
| [SRC-4FFD5AFC54-L000375](../../scripts/run_answer_quality_benchmark.py#L375) | 375 | `"            f\"case_count metadata {data.get('case_count')!r} != len(cases) {len(cases)}\""` | — |
| [SRC-4FFD5AFC54-L000376](../../scripts/run_answer_quality_benchmark.py#L376) | 376 | `"        )"` | — |
| [SRC-4FFD5AFC54-L000377](../../scripts/run_answer_quality_benchmark.py#L377) | 377 | `"    if len(cases) < 40:"` | — |
| [SRC-4FFD5AFC54-L000378](../../scripts/run_answer_quality_benchmark.py#L378) | 378 | `"        problems.append(f\"expected at least 40 cases, found {len(cases)}\")"` | — |
| [SRC-4FFD5AFC54-L000379](../../scripts/run_answer_quality_benchmark.py#L379) | 379 | `"    ids: list[str] = []"` | — |
| [SRC-4FFD5AFC54-L000380](../../scripts/run_answer_quality_benchmark.py#L380) | 380 | `"    for i, case in enumerate(cases):"` | — |
| [SRC-4FFD5AFC54-L000381](../../scripts/run_answer_quality_benchmark.py#L381) | 381 | `"        if not isinstance(case, dict):"` | — |
| [SRC-4FFD5AFC54-L000382](../../scripts/run_answer_quality_benchmark.py#L382) | 382 | `"            problems.append(f\"cases[{i}] is not an object\")"` | — |
| [SRC-4FFD5AFC54-L000383](../../scripts/run_answer_quality_benchmark.py#L383) | 383 | `"            continue"` | — |
| [SRC-4FFD5AFC54-L000384](../../scripts/run_answer_quality_benchmark.py#L384) | 384 | `"        missing = REQUIRED_FIELDS - set(case)"` | — |
| [SRC-4FFD5AFC54-L000385](../../scripts/run_answer_quality_benchmark.py#L385) | 385 | `"        if missing:"` | — |
| [SRC-4FFD5AFC54-L000386](../../scripts/run_answer_quality_benchmark.py#L386) | 386 | `"            problems.append(f\"{case.get('case_id', i)}: missing {sorted(missing)}\")"` | — |
| [SRC-4FFD5AFC54-L000387](../../scripts/run_answer_quality_benchmark.py#L387) | 387 | `"        cid = case.get(\"case_id\")"` | — |
| [SRC-4FFD5AFC54-L000388](../../scripts/run_answer_quality_benchmark.py#L388) | 388 | `"        if isinstance(cid, str):"` | — |
| [SRC-4FFD5AFC54-L000389](../../scripts/run_answer_quality_benchmark.py#L389) | 389 | `"            ids.append(cid)"` | — |
| [SRC-4FFD5AFC54-L000390](../../scripts/run_answer_quality_benchmark.py#L390) | 390 | `"        if case.get(\"expected_strategy\") not in ALLOWED_STRATEGIES:"` | — |
| [SRC-4FFD5AFC54-L000391](../../scripts/run_answer_quality_benchmark.py#L391) | 391 | `"            problems.append(f\"{cid}: bad strategy {case.get('expected_strategy')!r}\")"` | — |
| [SRC-4FFD5AFC54-L000392](../../scripts/run_answer_quality_benchmark.py#L392) | 392 | `"        if case.get(\"evaluation_mode\") not in ALLOWED_EVAL_MODES:"` | — |
| [SRC-4FFD5AFC54-L000393](../../scripts/run_answer_quality_benchmark.py#L393) | 393 | `"            problems.append(f\"{cid}: bad evaluation_mode {case.get('evaluation_mode')!r}\")"` | — |
| [SRC-4FFD5AFC54-L000394](../../scripts/run_answer_quality_benchmark.py#L394) | 394 | `"        q = case.get(\"question\")"` | — |
| [SRC-4FFD5AFC54-L000395](../../scripts/run_answer_quality_benchmark.py#L395) | 395 | `"        if not isinstance(q, str) or len(q.strip()) < 2:"` | — |
| [SRC-4FFD5AFC54-L000396](../../scripts/run_answer_quality_benchmark.py#L396) | 396 | `"            problems.append(f\"{cid}: empty question\")"` | — |
| [SRC-4FFD5AFC54-L000397](../../scripts/run_answer_quality_benchmark.py#L397) | 397 | `"    if len(ids) != len(set(ids)):"` | — |
| [SRC-4FFD5AFC54-L000398](../../scripts/run_answer_quality_benchmark.py#L398) | 398 | `"        problems.append(\"duplicate case_id values\")"` | — |
| [SRC-4FFD5AFC54-L000399](../../scripts/run_answer_quality_benchmark.py#L399) | 399 | `"    return problems"` | — |
| [SRC-4FFD5AFC54-L000400](../../scripts/run_answer_quality_benchmark.py#L400) | 400 | `""` | — |
| [SRC-4FFD5AFC54-L000401](../../scripts/run_answer_quality_benchmark.py#L401) | 401 | `""` | — |
| [SRC-4FFD5AFC54-L000402](../../scripts/run_answer_quality_benchmark.py#L402) | 402 | `"def redact_secrets(text: str) -> str:"` | — |
| [SRC-4FFD5AFC54-L000403](../../scripts/run_answer_quality_benchmark.py#L403) | 403 | `"    \"\"\"Best-effort redaction of common secret patterns from stored outputs.\"\"\""` | — |
| [SRC-4FFD5AFC54-L000404](../../scripts/run_answer_quality_benchmark.py#L404) | 404 | `"    if not text:"` | — |
| [SRC-4FFD5AFC54-L000405](../../scripts/run_answer_quality_benchmark.py#L405) | 405 | `"        return text"` | — |
| [SRC-4FFD5AFC54-L000406](../../scripts/run_answer_quality_benchmark.py#L406) | 406 | `"    out = text"` | — |
| [SRC-4FFD5AFC54-L000407](../../scripts/run_answer_quality_benchmark.py#L407) | 407 | `"    for key in ("` | — |
| [SRC-4FFD5AFC54-L000408](../../scripts/run_answer_quality_benchmark.py#L408) | 408 | `"        \"OPENROUTER_API_KEY\","` | — |
| [SRC-4FFD5AFC54-L000409](../../scripts/run_answer_quality_benchmark.py#L409) | 409 | `"        \"OMARAI_ACCESS_TOKEN\","` | — |
| [SRC-4FFD5AFC54-L000410](../../scripts/run_answer_quality_benchmark.py#L410) | 410 | `"        \"OMARAI_LLM_API_KEY\","` | — |
| [SRC-4FFD5AFC54-L000411](../../scripts/run_answer_quality_benchmark.py#L411) | 411 | `"        \"Authorization\","` | — |
| [SRC-4FFD5AFC54-L000412](../../scripts/run_answer_quality_benchmark.py#L412) | 412 | `"        \"Bearer \","` | — |
| [SRC-4FFD5AFC54-L000413](../../scripts/run_answer_quality_benchmark.py#L413) | 413 | `"    ):"` | — |
| [SRC-4FFD5AFC54-L000414](../../scripts/run_answer_quality_benchmark.py#L414) | 414 | `"        out = out.replace(key, f\"[REDACTED:{key.strip()}]\")"` | — |
| [SRC-4FFD5AFC54-L000415](../../scripts/run_answer_quality_benchmark.py#L415) | 415 | `"    token = os.getenv(\"OMARAI_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-4FFD5AFC54-L000416](../../scripts/run_answer_quality_benchmark.py#L416) | 416 | `"    if token and token in out:"` | — |
| [SRC-4FFD5AFC54-L000417](../../scripts/run_answer_quality_benchmark.py#L417) | 417 | `"        out = out.replace(token, \"[REDACTED:OMARAI_ACCESS_TOKEN]\")"` | — |
| [SRC-4FFD5AFC54-L000418](../../scripts/run_answer_quality_benchmark.py#L418) | 418 | `"    for env_name in (\"OPENROUTER_API_KEY\", \"OMARAI_LLM_API_KEY\"):"` | — |
| [SRC-4FFD5AFC54-L000419](../../scripts/run_answer_quality_benchmark.py#L419) | 419 | `"        val = os.getenv(env_name, \"\").strip()"` | — |
| [SRC-4FFD5AFC54-L000420](../../scripts/run_answer_quality_benchmark.py#L420) | 420 | `"        if val and val in out:"` | — |
| [SRC-4FFD5AFC54-L000421](../../scripts/run_answer_quality_benchmark.py#L421) | 421 | `"            out = out.replace(val, f\"[REDACTED:{env_name}]\")"` | — |
| [SRC-4FFD5AFC54-L000422](../../scripts/run_answer_quality_benchmark.py#L422) | 422 | `"    return out"` | — |
| [SRC-4FFD5AFC54-L000423](../../scripts/run_answer_quality_benchmark.py#L423) | 423 | `""` | — |
| [SRC-4FFD5AFC54-L000424](../../scripts/run_answer_quality_benchmark.py#L424) | 424 | `""` | — |
| [SRC-4FFD5AFC54-L000425](../../scripts/run_answer_quality_benchmark.py#L425) | 425 | `"def post_agent("` | — |
| [SRC-4FFD5AFC54-L000426](../../scripts/run_answer_quality_benchmark.py#L426) | 426 | `"    base_url: str,"` | — |
| [SRC-4FFD5AFC54-L000427](../../scripts/run_answer_quality_benchmark.py#L427) | 427 | `"    question: str,"` | — |
| [SRC-4FFD5AFC54-L000428](../../scripts/run_answer_quality_benchmark.py#L428) | 428 | `"    timeout: float,"` | — |
| [SRC-4FFD5AFC54-L000429](../../scripts/run_answer_quality_benchmark.py#L429) | 429 | `"    token: str \| None,"` | — |
| [SRC-4FFD5AFC54-L000430](../../scripts/run_answer_quality_benchmark.py#L430) | 430 | `") -> tuple[int, dict \| str]:"` | — |
| [SRC-4FFD5AFC54-L000431](../../scripts/run_answer_quality_benchmark.py#L431) | 431 | `"    origin = validate_base_url(base_url, token_present=bool(token))"` | — |
| [SRC-4FFD5AFC54-L000432](../../scripts/run_answer_quality_benchmark.py#L432) | 432 | `"    url = origin + \"/api/agent\""` | — |
| [SRC-4FFD5AFC54-L000433](../../scripts/run_answer_quality_benchmark.py#L433) | 433 | `"    body = json.dumps({\"question\": question, \"history\": []}, ensure_ascii=False).encode(\"utf-8\")"` | — |
| [SRC-4FFD5AFC54-L000434](../../scripts/run_answer_quality_benchmark.py#L434) | 434 | `"    headers = {\"Content-Type\": \"application/json\", \"Content-Length\": str(len(body))}"` | — |
| [SRC-4FFD5AFC54-L000435](../../scripts/run_answer_quality_benchmark.py#L435) | 435 | `"    if token:"` | — |
| [SRC-4FFD5AFC54-L000436](../../scripts/run_answer_quality_benchmark.py#L436) | 436 | `"        headers[\"Authorization\"] = \"Bearer \" + token"` | — |
| [SRC-4FFD5AFC54-L000437](../../scripts/run_answer_quality_benchmark.py#L437) | 437 | `"    req = urllib.request.Request(url, data=body, headers=headers, method=\"POST\")"` | — |
| [SRC-4FFD5AFC54-L000438](../../scripts/run_answer_quality_benchmark.py#L438) | 438 | `"    try:"` | — |
| [SRC-4FFD5AFC54-L000439](../../scripts/run_answer_quality_benchmark.py#L439) | 439 | `"        with _NO_REDIRECT_OPENER.open(req, timeout=timeout) as resp:"` | — |
| [SRC-4FFD5AFC54-L000440](../../scripts/run_answer_quality_benchmark.py#L440) | 440 | `"            raw_bytes = resp.read(MAX_RESPONSE_BYTES + 1)"` | — |
| [SRC-4FFD5AFC54-L000441](../../scripts/run_answer_quality_benchmark.py#L441) | 441 | `"            if len(raw_bytes) > MAX_RESPONSE_BYTES:"` | — |
| [SRC-4FFD5AFC54-L000442](../../scripts/run_answer_quality_benchmark.py#L442) | 442 | `"                return 0, {\"error\": \"ResponseTooLarge\", \"detail\": \"Response exceeded the 2 MB limit.\"}"` | — |
| [SRC-4FFD5AFC54-L000443](../../scripts/run_answer_quality_benchmark.py#L443) | 443 | `"            raw = raw_bytes.decode(\"utf-8\", errors=\"replace\")"` | — |
| [SRC-4FFD5AFC54-L000444](../../scripts/run_answer_quality_benchmark.py#L444) | 444 | `"            status = getattr(resp, \"status\", 200)"` | — |
| [SRC-4FFD5AFC54-L000445](../../scripts/run_answer_quality_benchmark.py#L445) | 445 | `"            try:"` | — |
| [SRC-4FFD5AFC54-L000446](../../scripts/run_answer_quality_benchmark.py#L446) | 446 | `"                return status, json.loads(raw)"` | — |
| [SRC-4FFD5AFC54-L000447](../../scripts/run_answer_quality_benchmark.py#L447) | 447 | `"            except json.JSONDecodeError:"` | — |
| [SRC-4FFD5AFC54-L000448](../../scripts/run_answer_quality_benchmark.py#L448) | 448 | `"                return status, raw"` | — |
| [SRC-4FFD5AFC54-L000449](../../scripts/run_answer_quality_benchmark.py#L449) | 449 | `"    except urllib.error.HTTPError as exc:"` | — |
| [SRC-4FFD5AFC54-L000450](../../scripts/run_answer_quality_benchmark.py#L450) | 450 | `"        raw_bytes = exc.read(MAX_RESPONSE_BYTES + 1)"` | — |
| [SRC-4FFD5AFC54-L000451](../../scripts/run_answer_quality_benchmark.py#L451) | 451 | `"        if len(raw_bytes) > MAX_RESPONSE_BYTES:"` | — |
| [SRC-4FFD5AFC54-L000452](../../scripts/run_answer_quality_benchmark.py#L452) | 452 | `"            return exc.code, {\"error\": \"ResponseTooLarge\", \"detail\": \"Response exceeded the 2 MB limit.\"}"` | — |
| [SRC-4FFD5AFC54-L000453](../../scripts/run_answer_quality_benchmark.py#L453) | 453 | `"        raw = raw_bytes.decode(\"utf-8\", errors=\"replace\")"` | — |
| [SRC-4FFD5AFC54-L000454](../../scripts/run_answer_quality_benchmark.py#L454) | 454 | `"        try:"` | — |
| [SRC-4FFD5AFC54-L000455](../../scripts/run_answer_quality_benchmark.py#L455) | 455 | `"            return exc.code, json.loads(raw)"` | — |
| [SRC-4FFD5AFC54-L000456](../../scripts/run_answer_quality_benchmark.py#L456) | 456 | `"        except json.JSONDecodeError:"` | — |
| [SRC-4FFD5AFC54-L000457](../../scripts/run_answer_quality_benchmark.py#L457) | 457 | `"            return exc.code, raw"` | — |
| [SRC-4FFD5AFC54-L000458](../../scripts/run_answer_quality_benchmark.py#L458) | 458 | `"    except ValueError as exc:"` | — |
| [SRC-4FFD5AFC54-L000459](../../scripts/run_answer_quality_benchmark.py#L459) | 459 | `"        return 0, {\"error\": \"UnsafeBaseURL\", \"detail\": str(exc)}"` | — |
| [SRC-4FFD5AFC54-L000460](../../scripts/run_answer_quality_benchmark.py#L460) | 460 | `"    except (urllib.error.URLError, TimeoutError, OSError) as exc:"` | — |
| [SRC-4FFD5AFC54-L000461](../../scripts/run_answer_quality_benchmark.py#L461) | 461 | `"        return 0, {\"error\": type(exc).__name__, \"detail\": str(exc)}"` | — |
| [SRC-4FFD5AFC54-L000462](../../scripts/run_answer_quality_benchmark.py#L462) | 462 | `""` | — |
| [SRC-4FFD5AFC54-L000463](../../scripts/run_answer_quality_benchmark.py#L463) | 463 | `""` | — |
| [SRC-4FFD5AFC54-L000464](../../scripts/run_answer_quality_benchmark.py#L464) | 464 | `"def get_verified_build_sha(base_url: str, timeout: float, token: str \| None = None) -> str:"` | — |
| [SRC-4FFD5AFC54-L000465](../../scripts/run_answer_quality_benchmark.py#L465) | 465 | `"    \"\"\"Read the deployed build identity from /api/health; never trust a caller-only SHA.\"\"\""` | — |
| [SRC-4FFD5AFC54-L000466](../../scripts/run_answer_quality_benchmark.py#L466) | 466 | `"    origin = validate_base_url(base_url, token_present=bool(token))"` | — |
| [SRC-4FFD5AFC54-L000467](../../scripts/run_answer_quality_benchmark.py#L467) | 467 | `"    request = urllib.request.Request("` | — |
| [SRC-4FFD5AFC54-L000468](../../scripts/run_answer_quality_benchmark.py#L468) | 468 | `"        origin + \"/api/health\","` | — |
