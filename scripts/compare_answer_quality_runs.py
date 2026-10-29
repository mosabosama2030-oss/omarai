"""Compare two Omarai benchmark runs without inventing quality or cost measurements.

Runtime measurements come from explicit run telemetry. Factual accuracy, retrieval
precision/recall, faithfulness, citation support, and writing quality require matching
human-review files; missing annotations remain unscored. The comparator is offline.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import math
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CORPUS = ROOT / "tests" / "fixtures" / "answer_quality_cases.json"
REQUIRED_RUN_FIELDS = {"benchmark_id", "benchmark_version", "results"}


def load_json_object(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise FileNotFoundError("Input file not found: " + str(path))
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise TypeError("JSON root must be an object: " + str(path))
    return data


def _finite_nonnegative(value: Any) -> float | None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    number = float(value)
    if not math.isfinite(number) or number < 0:
        return None
    return number


def validate_run(run: dict[str, Any], label: str) -> list[str]:
    problems: list[str] = []
    missing = REQUIRED_RUN_FIELDS - set(run)
    if missing:
        problems.append(f"{label}: missing run fields {sorted(missing)}")
    results = run.get("results")
    if not isinstance(results, list) or not results:
        problems.append(f"{label}: results must be a non-empty array")
        return problems
    seen: set[str] = set()
    for index, record in enumerate(results):
        if not isinstance(record, dict):
            problems.append(f"{label}: results[{index}] must be an object")
            continue
        case_id = record.get("case_id")
        if not isinstance(case_id, str) or not case_id.strip():
            problems.append(f"{label}: results[{index}] has no case_id")
            continue
        prompt = record.get("prompt")
        if not isinstance(prompt, str) or not prompt.strip():
            problems.append(f"{label}/{case_id}: prompt must be a non-empty string")
        if case_id in seen:
            problems.append(f"{label}: duplicate case_id {case_id}")
        seen.add(case_id)
        if "elapsed_ms" in record and _finite_nonnegative(record["elapsed_ms"]) is None:
            problems.append(f"{label}/{case_id}: elapsed_ms must be finite and non-negative")
    return problems


def _percentile_nearest_rank(values: list[float], percentile: float) -> float | None:
    if not values:
        return None
    ordered = sorted(values)
    index = max(0, math.ceil(percentile * len(ordered)) - 1)
    return round(ordered[index], 2)


def _rate(numerator: int, denominator: int) -> dict[str, Any]:
    return {
        "score": round(numerator / denominator, 4) if denominator else None,
        "numerator": numerator,
        "denominator": denominator,
        "status": "SCORED" if denominator else "NOT_SCORABLE_NO_DENOMINATOR",
    }


def run_metrics(run: dict[str, Any]) -> dict[str, Any]:
    results = run["results"]
    transport_ok = [r for r in results if r.get("transport_ok") is True]
    elapsed = [
        float(value)
        for record in results
        if (value := _finite_nonnegative(record.get("elapsed_ms"))) is not None
    ]
    search_cases = [r for r in results if r.get("expected_strategy") == "web_search"]
    search_attempted = [
        r for r in search_cases
        if r.get("search_outcome") not in (None, "", "unknown", "not_attempted")
    ]
    usable = [r for r in search_cases if r.get("tool_status") == "SUCCESS_WITH_USABLE_RESULTS"]
    tool_failed = [r for r in search_cases if r.get("tool_status") == "TOOL_FAILED"]
    no_usable = [r for r in search_cases if r.get("tool_status") == "ATTEMPTED_NO_USABLE_RESULTS"]
    costs = [
        float(value)
        for record in results
        if (value := _finite_nonnegative(record.get("provider_reported_model_cost_usd"))) is not None
    ]
    complete_cost_cases = sum(
        1 for r in results
        if r.get("provider_reported_model_cost_status") == "COMPLETE_FOR_RETURNED_MODEL_CALLS"
    )
    reconciled_request_costs = [
        float(value)
        for record in results
        if record.get("request_cost_status") == "RECONCILED_COMPLETE_REQUEST_COST"
        and (value := _finite_nonnegative(record.get("request_cost_usd"))) is not None
    ]
    complete_request_cost_count = len(reconciled_request_costs)
    request_cost_complete = complete_request_cost_count == len(results)
    return {
        "case_count": len(results),
        "transport_success_rate": _rate(len(transport_ok), len(results)),
        "latency_ms": {
            "sample_count": len(elapsed),
            "mean": round(sum(elapsed) / len(elapsed), 2) if elapsed else None,
            "p50": _percentile_nearest_rank(elapsed, 0.50),
            "p95": _percentile_nearest_rank(elapsed, 0.95),
            "max": round(max(elapsed), 2) if elapsed else None,
            "status": "SCORED" if elapsed else "NOT_MEASURED",
            "semantics": "Sequential end-to-end HTTP request time; not a concurrency/load test.",
        },
        "tool_usage": {
            "web_search_case_count": len(search_cases),
            "search_attempt_rate": _rate(len(search_attempted), len(search_cases)),
            "usable_result_rate": _rate(len(usable), len(search_cases)),
            "tool_error_rate_among_search_cases": _rate(len(tool_failed), len(search_cases)),
            "attempted_without_usable_results": len(no_usable),
            "unknown_tool_outcome_count": sum(
                1 for r in search_cases
                if r.get("tool_status") in (None, "", "UNKNOWN")
            ),
        },
        "provider_reported_model_cost": {
            "reported_sum_usd": round(sum(costs), 10) if costs else None,
            "cases_with_any_reported_cost": len(costs),
            "cases_complete_for_returned_model_calls": complete_cost_cases,
            "status": (
                "PARTIAL_OR_PROVIDER_REPORTED_ONLY"
                if costs
                else "NOT_MEASURED_NO_PROVIDER_COST_REPORTED"
            ),
            "complete_request_cost_usd": (
                round(sum(reconciled_request_costs), 10) if request_cost_complete else None
            ),
            "complete_request_cost_status": (
                "RECONCILED_COMPLETE_REQUEST_COST"
                if request_cost_complete
                else (
                    "PARTIAL_EXTERNAL_COST_RECONCILIATION"
                    if complete_request_cost_count
                    else "NOT_MEASURED_TOTAL_CONNECTOR_COSTS_NOT_EXPOSED"
                )
            ),
            "complete_request_cost_case_count": complete_request_cost_count,
        },
    }


def _load_review_scorer():
    path = ROOT / "scripts" / "score_answer_quality_reviews.py"
    spec = importlib.util.spec_from_file_location("omarai_review_scorecard", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load existing review scorecard: " + str(path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _reviewed_case_ids(review_data: dict[str, Any]) -> set[str]:
    reviews = review_data.get("reviews")
    if not isinstance(reviews, list):
        raise ValueError("review file must contain a reviews array")
    return {
        item["case_id"]
        for item in reviews
        if isinstance(item, dict) and item.get("status") == "REVIEWED"
        and isinstance(item.get("case_id"), str)
    }


def review_comparison(
    baseline_reviews: dict[str, Any],
    candidate_reviews: dict[str, Any],
    corpus: dict[str, Any],
) -> dict[str, Any]:
    baseline_ids = _reviewed_case_ids(baseline_reviews)
    candidate_ids = _reviewed_case_ids(candidate_reviews)
    if not baseline_ids or not candidate_ids:
        raise ValueError("both review files need explicitly REVIEWED cases")
    if baseline_ids != candidate_ids:
        raise ValueError(
            "incomparable review coverage: REVIEWED case IDs differ between baseline and candidate"
        )
    corpus_cases = corpus.get("cases")
    if not isinstance(corpus_cases, list) or not corpus_cases:
        raise ValueError("corpus must contain a non-empty cases array for full-coverage acceptance")
    corpus_ids = {
        item.get("case_id")
        for item in corpus_cases
        if isinstance(item, dict) and isinstance(item.get("case_id"), str)
    }
    if baseline_ids != corpus_ids:
        missing = sorted(corpus_ids - baseline_ids)
        extra = sorted(baseline_ids - corpus_ids)
        raise ValueError(
            f"incomplete human review coverage: missing={missing}; unknown={extra}"
        )
    scorer = _load_review_scorer()
    baseline = scorer.summarize_reviews(baseline_reviews, corpus)
    candidate = scorer.summarize_reviews(candidate_reviews, corpus)
    aliases = {
        "retrieval_precision": "retrieval_precision",
        "retrieval_recall": "retrieval_recall",
        "factual_accuracy": "correctness",
        "faithfulness": "faithfulness",
        "citation_support": "citation_support",
        "writing_quality_1_to_5": "writing_quality_1_to_5",
    }
    metrics: dict[str, Any] = {}
    for output_name, score_name in aliases.items():
        before = baseline["metrics"][score_name]["score"]
        after = candidate["metrics"][score_name]["score"]
        metrics[output_name] = {
            "baseline": before,
            "candidate": after,
            "delta": round(after - before, 4) if before is not None and after is not None else None,
            "status": (
                "COMPARED" if before is not None and after is not None
                else "NOT_SCORABLE_MISSING_ANNOTATED_DENOMINATOR"
            ),
            "source": "explicit_human_review",
        }
    return {
        "reviewed_case_count": len(baseline_ids),
        "baseline_review_coverage": baseline["reviewed_case_coverage"],
        "candidate_review_coverage": candidate["reviewed_case_coverage"],
        "metrics": metrics,
        "automatic_answer_grading": False,
        "limitations": [
            "Scores reflect explicit human annotations, not automatic model grading.",
            "Retrieval precision/recall require comparable candidate pools and relevance judgments.",
            "Citation support measures reviewer-labelled citations that support the associated claims; URL presence alone is not evidence of support.",
        ],
    }


def compare_runs(
    baseline: dict[str, Any],
    candidate: dict[str, Any],
    *,
    corpus: dict[str, Any] | None = None,
    baseline_reviews: dict[str, Any] | None = None,
    candidate_reviews: dict[str, Any] | None = None,
) -> dict[str, Any]:
    problems = validate_run(baseline, "baseline") + validate_run(candidate, "candidate")
    if problems:
        raise ValueError("; ".join(problems))
    if baseline.get("benchmark_id") != candidate.get("benchmark_id"):
        raise ValueError("baseline/candidate benchmark_id differs")
    if baseline.get("benchmark_version") != candidate.get("benchmark_version"):
        raise ValueError("baseline/candidate benchmark_version differs")
    if corpus is not None:
        if corpus.get("benchmark_id") != baseline.get("benchmark_id"):
            raise ValueError("runs do not match the supplied corpus benchmark_id")
        if corpus.get("version") != baseline.get("benchmark_version"):
            raise ValueError("runs do not match the supplied corpus benchmark_version")
    baseline_by_id = {row["case_id"]: row for row in baseline["results"]}
    candidate_by_id = {row["case_id"]: row for row in candidate["results"]}
    if set(baseline_by_id) != set(candidate_by_id):
        missing_candidate = sorted(set(baseline_by_id) - set(candidate_by_id))
        missing_baseline = sorted(set(candidate_by_id) - set(baseline_by_id))
        raise ValueError(
            f"incomparable case sets; missing in candidate={missing_candidate}; "
            f"missing in baseline={missing_baseline}"
        )
    corpus_by_id = {
        case["case_id"]: case
        for case in (corpus.get("cases", []) if corpus is not None else [])
        if isinstance(case, dict) and isinstance(case.get("case_id"), str)
    }
    for case_id in baseline_by_id:
        before_row = baseline_by_id[case_id]
        after_row = candidate_by_id[case_id]
        if before_row.get("prompt") != after_row.get("prompt"):
            raise ValueError(f"incomparable question text for {case_id}")
        if corpus is not None:
            corpus_case = corpus_by_id.get(case_id)
            if not isinstance(corpus_case, dict):
                raise ValueError(f"{case_id}: case_id is not present in the supplied corpus")
            if before_row.get("prompt") != corpus_case.get("question"):
                raise ValueError(f"{case_id}: recorded prompt differs from the canonical corpus question")
            if before_row.get("expected_strategy") != corpus_case.get("expected_strategy"):
                raise ValueError(f"{case_id}: expected_strategy differs from the canonical corpus")

    before_runtime = run_metrics(baseline)
    after_runtime = run_metrics(candidate)
    time_metrics = {}
    for key in ("mean", "p50", "p95", "max"):
        before = before_runtime["latency_ms"][key]
        after = after_runtime["latency_ms"][key]
        time_metrics[key] = {
            "baseline_ms": before,
            "candidate_ms": after,
            "delta_ms": round(after - before, 2) if before is not None and after is not None else None,
            "status": "COMPARED" if before is not None and after is not None else "NOT_MEASURED",
        }

    cost_before = before_runtime["provider_reported_model_cost"]["reported_sum_usd"]
    cost_after = after_runtime["provider_reported_model_cost"]["reported_sum_usd"]
    cost_delta = round(cost_after - cost_before, 10) if cost_before is not None and cost_after is not None else None
    request_cost_before = before_runtime["provider_reported_model_cost"]["complete_request_cost_usd"]
    request_cost_after = after_runtime["provider_reported_model_cost"]["complete_request_cost_usd"]
    request_cost_delta = (
        round(request_cost_after - request_cost_before, 10)
        if request_cost_before is not None and request_cost_after is not None
        else None
    )
    runtime_deltas = {
        "complete_request_cost_usd": {
            "baseline": request_cost_before,
            "candidate": request_cost_after,
            "delta": request_cost_delta,
            "status": (
                "COMPARED"
                if request_cost_before is not None and request_cost_after is not None
                else "NOT_MEASURED_OR_INCOMPLETE_RECONCILIATION"
            ),
        },
        "transport_success_rate": {
            "baseline": before_runtime["transport_success_rate"]["score"],
            "candidate": after_runtime["transport_success_rate"]["score"],
        },
        "usable_result_rate": {
            "baseline": before_runtime["tool_usage"]["usable_result_rate"]["score"],
            "candidate": after_runtime["tool_usage"]["usable_result_rate"]["score"],
        },
        "provider_reported_model_cost_usd": {
            "baseline": cost_before,
            "candidate": cost_after,
            "delta": cost_delta,
            "status": (
                "PARTIAL_OR_PROVIDER_REPORTED_ONLY"
                if cost_before is not None and cost_after is not None
                else "NOT_MEASURED"
            ),
        },
    }
    for key in ("transport_success_rate", "usable_result_rate"):
        before = runtime_deltas[key]["baseline"]
        after = runtime_deltas[key]["candidate"]
        runtime_deltas[key]["delta"] = round(after - before, 4) if before is not None and after is not None else None
    comparison: dict[str, Any] = {
        "schema_version": "1.0",
        "benchmark_id": baseline["benchmark_id"],
        "benchmark_version": baseline["benchmark_version"],
        "case_count": len(baseline_by_id),
        "baseline": {
            "build_sha": baseline.get("build_sha", "unknown"),
            "executed_at_utc": baseline.get("executed_at_utc"),
            "metrics": before_runtime,
        },
        "candidate": {
            "build_sha": candidate.get("build_sha", "unknown"),
            "executed_at_utc": candidate.get("executed_at_utc"),
            "metrics": after_runtime,
        },
        "runtime_deltas": runtime_deltas,
        "latency_comparison": time_metrics,
        "quality_comparison": None,
        "acceptance_status": "PARTIAL",
        "acceptance_blockers": [],
        "interpretation": [
            "The same benchmark version, case IDs, and exact question text were compared.",
            "HTTP transport success is not semantic correctness, and a successful search request is not proof that the answer is correct.",
            "Complete request cost is intentionally null because search connector costs are not consistently exposed; only explicit provider-reported model cost is summarized.",
        ],
    }
    sha_re = re.compile(r"^[0-9a-fA-F]{40}$")
    for label, run in (("baseline", baseline), ("candidate", candidate)):
        if not isinstance(run.get("build_sha"), str) or not sha_re.fullmatch(run["build_sha"]):
            comparison["acceptance_blockers"].append(f"{label}_build_sha_missing_or_invalid")
    for label, metrics in (("baseline", before_runtime), ("candidate", after_runtime)):
        if metrics["provider_reported_model_cost"]["complete_request_cost_status"] != "RECONCILED_COMPLETE_REQUEST_COST":
            comparison["acceptance_blockers"].append(f"{label}_complete_request_cost_missing_or_partial")
    if baseline_reviews is None and candidate_reviews is None:
        comparison["acceptance_blockers"].append("human_review_files_missing")
    elif baseline_reviews is None or candidate_reviews is None or corpus is None:
        comparison["acceptance_blockers"].append("both_review_files_and_corpus_are_required")
    else:
        corpus_ids = {
            case.get("case_id")
            for case in corpus.get("cases", [])
            if isinstance(case, dict) and isinstance(case.get("case_id"), str)
        }
        if set(baseline_by_id) != corpus_ids:
            comparison["acceptance_blockers"].append("benchmark_run_does_not_cover_entire_corpus")
        comparison["quality_comparison"] = review_comparison(
            baseline_reviews, candidate_reviews, corpus
        )
        unscored_quality = [
            name for name, metric in comparison["quality_comparison"]["metrics"].items()
            if metric["status"] != "COMPARED"
        ]
        if unscored_quality:
            comparison["acceptance_blockers"].append(
                "required_quality_metrics_unscored:" + ",".join(unscored_quality)
            )
    if not comparison["acceptance_blockers"]:
        comparison["acceptance_status"] = "COMPARABLE_WITH_REVIEWED_QUALITY_AND_BUILD_IDENTITIES"
    else:
        comparison["acceptance_status"] = "INCOMPLETE"
    return comparison


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline-run", type=Path, required=True)
    parser.add_argument("--candidate-run", type=Path, required=True)
    parser.add_argument("--baseline-reviews", type=Path)
    parser.add_argument("--candidate-reviews", type=Path)
    parser.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args(argv)
    if bool(args.baseline_reviews) != bool(args.candidate_reviews):
        parser.error("provide both --baseline-reviews and --candidate-reviews, or neither")
    try:
        baseline = load_json_object(args.baseline_run)
        candidate = load_json_object(args.candidate_run)
        corpus = load_json_object(args.corpus) if args.baseline_reviews else None
        before_reviews = load_json_object(args.baseline_reviews) if args.baseline_reviews else None
        after_reviews = load_json_object(args.candidate_reviews) if args.candidate_reviews else None
        result = compare_runs(
            baseline, candidate, corpus=corpus,
            baseline_reviews=before_reviews, candidate_reviews=after_reviews,
        )
    except (OSError, ValueError, TypeError, json.JSONDecodeError, KeyError) as exc:
        print("COMPARISON INVALID: " + str(exc), file=sys.stderr)
        return 2
    output = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True)
    if args.out:
        args.out.write_text(output + "\n", encoding="utf-8")
        print("Wrote " + str(args.out))
    print(output)
    return 0 if result["acceptance_status"] == "COMPARABLE_WITH_REVIEWED_QUALITY_AND_BUILD_IDENTITIES" else 2


if __name__ == "__main__":
    raise SystemExit(main())
