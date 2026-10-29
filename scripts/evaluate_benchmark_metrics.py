"""Aggregate reviewed Omarai benchmark runs and compare paired baseline/candidate metrics.

This tool never grades natural-language answers automatically. Human/reviewer annotations
are explicit inputs; unknown values remain unknown rather than being treated as zero.
Standard library only.
"""
from __future__ import annotations

import argparse
import json
import math
import statistics
import sys
from pathlib import Path
from typing import Any

REQUIRED_ROOT = {"benchmark_id", "benchmark_version", "run_id", "commit_sha", "cases"}
REQUIRED_CASE = {"case_id", "language"}
NUMERIC_NONNEGATIVE = {
    "gold_claims", "retrieved_gold_claims", "citations_total", "citations_supported",
    "tool_attempted", "tool_succeeded", "latency_ms", "cost_usd",
    "input_tokens", "output_tokens",
}


def load_run(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    problems = validate_run(data)
    if problems:
        raise ValueError("Invalid evaluation run:\n- " + "\n- ".join(problems))
    return data


def validate_run(data: Any) -> list[str]:
    problems: list[str] = []
    if not isinstance(data, dict):
        return ["root must be a JSON object"]
    missing = REQUIRED_ROOT - set(data)
    if missing:
        problems.append(f"missing root fields: {sorted(missing)}")
    if not isinstance(data.get("cases"), list):
        return problems + ["cases must be an array"]
    if not isinstance(data.get("commit_sha"), str) or not data.get("commit_sha", "").strip():
        problems.append("commit_sha must identify the exact tested version")
    ids: list[str] = []
    for index, row in enumerate(data["cases"]):
        where = f"cases[{index}]"
        if not isinstance(row, dict):
            problems.append(f"{where} must be an object")
            continue
        missing_case = REQUIRED_CASE - set(row)
        if missing_case:
            problems.append(f"{where} missing fields: {sorted(missing_case)}")
        case_id = row.get("case_id")
        if isinstance(case_id, str):
            ids.append(case_id)
        else:
            problems.append(f"{where}.case_id must be a string")
        if not isinstance(row.get("language"), str) or not row.get("language", "").strip():
            problems.append(f"{where}.language must be a non-empty string")
        if "correct" in row and row["correct"] is not None and not isinstance(row["correct"], bool):
            problems.append(f"{where}.correct must be true, false, or null")
        for field in NUMERIC_NONNEGATIVE:
            value = row.get(field)
            if value is not None and (
                isinstance(value, bool) or not isinstance(value, (int, float))
                or not math.isfinite(value) or value < 0
            ):
                problems.append(f"{where}.{field} must be a non-negative number or null")
        if row.get("retrieved_gold_claims") is not None and row.get("gold_claims") is not None:
            if row["retrieved_gold_claims"] > row["gold_claims"]:
                problems.append(f"{where}.retrieved_gold_claims cannot exceed gold_claims")
        if row.get("citations_supported") is not None and row.get("citations_total") is not None:
            if row["citations_supported"] > row["citations_total"]:
                problems.append(f"{where}.citations_supported cannot exceed citations_total")
        if row.get("tool_succeeded") is not None and row.get("tool_attempted") is not None:
            if row["tool_succeeded"] > row["tool_attempted"]:
                problems.append(f"{where}.tool_succeeded cannot exceed tool_attempted")
    if len(ids) != len(set(ids)):
        problems.append("case_id values must be unique within a run")
    if data.get("baseline_status") == "NOT_MEASURED" and data["cases"]:
        problems.append("NOT_MEASURED baseline must not contain fabricated case results")
    return problems


def _ratio(numerator: float, denominator: float) -> float | None:
    return numerator / denominator if denominator else None


def _percent(value: float | None) -> str:
    return "N/A" if value is None else f"{value * 100:.2f}%"


def _number(value: float | None, suffix: str = "") -> str:
    return "N/A" if value is None else f"{value:.2f}{suffix}"


def percentile(values: list[float], p: float) -> float | None:
    if not values:
        return None
    ordered = sorted(values)
    if len(ordered) == 1:
        return ordered[0]
    # Linear interpolation; deterministic and documented for small benchmark samples.
    position = (len(ordered) - 1) * p
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return ordered[lower]
    return ordered[lower] + (ordered[upper] - ordered[lower]) * (position - lower)


def summarize(data: dict[str, Any], selected_ids: set[str] | None = None) -> dict[str, Any]:
    rows = [
        row for row in data["cases"]
        if selected_ids is None or row["case_id"] in selected_ids
    ]
    reviewed = [r for r in rows if isinstance(r.get("correct"), bool)]
    gold = [
        r for r in rows
        if isinstance(r.get("gold_claims"), (int, float))
        and isinstance(r.get("retrieved_gold_claims"), (int, float))
    ]
    citation_rows = [
        r for r in rows
        if isinstance(r.get("citations_total"), (int, float))
        and isinstance(r.get("citations_supported"), (int, float))
    ]
    citation_required = [r for r in rows if r.get("citations_required") is True]
    citation_coverage_known = [
        r for r in citation_required if isinstance(r.get("citations_total"), (int, float))
    ]
    tool_rows = [
        r for r in rows
        if r.get("tool_required") is True
        and isinstance(r.get("tool_attempted"), (int, float))
        and isinstance(r.get("tool_succeeded"), (int, float))
    ]
    latencies = [float(r["latency_ms"]) for r in rows if isinstance(r.get("latency_ms"), (int, float))]
    costs = [float(r["cost_usd"]) for r in rows if isinstance(r.get("cost_usd"), (int, float))]
    input_tokens = [r["input_tokens"] for r in rows if isinstance(r.get("input_tokens"), (int, float))]
    output_tokens = [r["output_tokens"] for r in rows if isinstance(r.get("output_tokens"), (int, float))]

    correct_count = sum(r["correct"] is True for r in reviewed)
    gold_total = sum(r["gold_claims"] for r in gold)
    retrieved_total = sum(r["retrieved_gold_claims"] for r in gold)
    citation_total = sum(r["citations_total"] for r in citation_rows)
    citation_supported = sum(r["citations_supported"] for r in citation_rows)
    # Missing tool calls for a known required-tool case count as a failure only when
    # tool_attempted is explicitly 0; unknown attempts remain excluded.
    tool_denominator = sum((r["tool_attempted"] if r["tool_attempted"] > 0 else 1) for r in tool_rows)
    tool_numerator = sum(r["tool_succeeded"] for r in tool_rows)
    citation_coverage = (
        sum(r["citations_total"] > 0 for r in citation_coverage_known) / len(citation_coverage_known)
        if citation_coverage_known else None
    )
    languages: dict[str, int] = {}
    for row in rows:
        languages[row["language"]] = languages.get(row["language"], 0) + 1

    return {
        "run_id": data["run_id"],
        "commit_sha": data["commit_sha"],
        "benchmark_id": data["benchmark_id"],
        "benchmark_version": data["benchmark_version"],
        "case_count": len(rows),
        "language_counts": languages,
        "accuracy": _ratio(correct_count, len(reviewed)),
        "accuracy_reviewed": len(reviewed),
        "accuracy_correct": correct_count,
        "claim_recall": _ratio(retrieved_total, gold_total),
        "gold_claim_count": gold_total,
        "retrieved_gold_claim_count": retrieved_total,
        "citation_precision": _ratio(citation_supported, citation_total),
        "citations_supported": citation_supported,
        "citations_total": citation_total,
        "citation_coverage": citation_coverage,
        "citation_coverage_cases": len(citation_coverage_known),
        "tool_success_rate": _ratio(tool_numerator, tool_denominator),
        "tool_success_count": tool_numerator,
        "tool_attempt_denominator": tool_denominator,
        "tool_required_cases_scored": len(tool_rows),
        "latency_ms_median": statistics.median(latencies) if latencies else None,
        "latency_ms_p95": percentile(latencies, 0.95),
        "latency_observations": len(latencies),
        "cost_usd_total": sum(costs) if costs else None,
        "cost_usd_mean": statistics.mean(costs) if costs else None,
        "cost_observations": len(costs),
        "input_tokens_total": sum(input_tokens) if input_tokens else None,
        "output_tokens_total": sum(output_tokens) if output_tokens else None,
        "input_token_observations": len(input_tokens),
        "output_token_observations": len(output_tokens),
    }


METRICS = [
    ("accuracy", "Accuracy", "percentage"),
    ("claim_recall", "Gold-claim recall", "percentage"),
    ("citation_precision", "Citation support precision", "percentage"),
    ("citation_coverage", "Citation coverage on citation-required cases", "percentage"),
    ("tool_success_rate", "Required-tool success rate", "percentage"),
    ("latency_ms_median", "Median latency (ms)", "lower"),
    ("latency_ms_p95", "P95 latency (ms)", "lower"),
    ("cost_usd_mean", "Mean observed cost/request (USD)", "lower"),
    ("cost_usd_total", "Total observed cost (USD)", "lower"),
]


def compare_runs(baseline: dict[str, Any], candidate: dict[str, Any]) -> dict[str, Any]:
    if baseline["benchmark_id"] != candidate["benchmark_id"]:
        raise ValueError("baseline and candidate benchmark_id must match")
    if baseline["benchmark_version"] != candidate["benchmark_version"]:
        raise ValueError("baseline and candidate benchmark_version must match")
    base_rows = {r["case_id"]: r for r in baseline["cases"]}
    cand_rows = {r["case_id"]: r for r in candidate["cases"]}
    paired = sorted(set(base_rows) & set(cand_rows))
    if not paired:
        raise ValueError("baseline and candidate have no paired case_id values")
    base_summary = summarize(baseline, set(paired))
    cand_summary = summarize(candidate, set(paired))
    deltas = []
    for key, label, kind in METRICS:
        before = base_summary[key]
        after = cand_summary[key]
        delta = None if before is None or after is None else after - before
        if kind == "lower" and before not in (None, 0) and after is not None:
            change_pct = (after - before) / before
        else:
            change_pct = None
        deltas.append({
            "metric": key, "label": label, "kind": kind,
            "baseline": before, "candidate": after, "delta": delta,
            "relative_change": change_pct,
        })
    return {
        "comparison_status": "COMPARABLE",
        "benchmark_id": baseline["benchmark_id"],
        "benchmark_version": baseline["benchmark_version"],
        "baseline_run_id": baseline["run_id"],
        "baseline_commit_sha": baseline["commit_sha"],
        "candidate_run_id": candidate["run_id"],
        "candidate_commit_sha": candidate["commit_sha"],
        "paired_case_count": len(paired),
        "paired_case_ids": paired,
        "baseline_summary": base_summary,
        "candidate_summary": cand_summary,
        "deltas": deltas,
        "limitations": [
            "Answer correctness and citation support require independent reviewer annotations.",
            "Claim recall is valid only when gold_claims and retrieved_gold_claims were annotated consistently.",
            "Costs are observed only when provider/API usage exposes cost or a reviewed estimate is supplied.",
            "A paired comparison is meaningful only when case prompts, grading rubric, and run conditions match.",
        ],
    }


def render_markdown(report: dict[str, Any]) -> str:
    lines = [
        "# Omarai benchmark comparison",
        "",
        f"- Status: **{report['comparison_status']}**",
        f"- Benchmark: `{report['benchmark_id']}` version `{report['benchmark_version']}`",
        f"- Baseline: `{report['baseline_run_id']}` @ `{report['baseline_commit_sha']}`",
        f"- Candidate: `{report['candidate_run_id']}` @ `{report['candidate_commit_sha']}`",
        f"- Paired cases: **{report['paired_case_count']}**",
        "",
        "| Metric | Baseline | Candidate | Delta |",
        "|---|---:|---:|---:|",
    ]
    for row in report["deltas"]:
        key = row["metric"]
        before = row["baseline"]
        after = row["candidate"]
        delta = row["delta"]
        if row["kind"] == "percentage":
            b, a, d = _percent(before), _percent(after), _number(None if delta is None else delta * 100, " pp")
        elif key.startswith("cost_"):
            b, a, d = _number(before, " USD"), _number(after, " USD"), _number(delta, " USD")
        else:
            b, a, d = _number(before), _number(after), _number(delta)
        lines.append(f"| {row['label']} | {b} | {a} | {d} |")
    lines.extend([
        "",
        "## Measurement coverage",
        "",
        f"- Correctness annotations: baseline {report['baseline_summary']['accuracy_reviewed']}; candidate {report['candidate_summary']['accuracy_reviewed']} (paired subset).",
        f"- Gold claims: baseline {report['baseline_summary']['gold_claim_count']}; candidate {report['candidate_summary']['gold_claim_count']}.",
        f"- Citation observations: baseline {report['baseline_summary']['citations_total']}; candidate {report['candidate_summary']['citations_total']}.",
        f"- Latency observations: baseline {report['baseline_summary']['latency_observations']}; candidate {report['candidate_summary']['latency_observations']}.",
        f"- Cost observations: baseline {report['baseline_summary']['cost_observations']}; candidate {report['candidate_summary']['cost_observations']}.",
        "",
        "## Limitations",
        "",
    ])
    lines.extend(f"- {item}" for item in report["limitations"])
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", type=Path, required=True, help="Reviewed baseline run JSON")
    parser.add_argument("--candidate", type=Path, required=True, help="Reviewed candidate run JSON")
    parser.add_argument("--out", type=Path, default=None, help="Markdown report path")
    parser.add_argument("--json-out", type=Path, default=None, help="Machine-readable report path")
    args = parser.parse_args(argv)
    try:
        baseline = load_run(args.baseline)
        candidate = load_run(args.candidate)
        report = compare_runs(baseline, candidate)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"EVALUATION ERROR: {exc}", file=sys.stderr)
        return 2
    markdown = render_markdown(report)
    if args.out:
        args.out.write_text(markdown, encoding="utf-8")
        print(f"Wrote {args.out}")
    else:
        print(markdown)
    if args.json_out:
        args.json_out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Wrote {args.json_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
