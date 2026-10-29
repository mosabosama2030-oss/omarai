"""Offline tests for the paired benchmark metrics and baseline comparison."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "evaluate_benchmark_metrics.py"


def _load_module():
    spec = importlib.util.spec_from_file_location("benchmark_metrics", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _run(run_id: str, sha: str, rows: list[dict]) -> dict:
    return {
        "benchmark_id": "OMARAI-REDTEAM-001",
        "benchmark_version": "1.0.0",
        "run_id": run_id,
        "commit_sha": sha,
        "cases": rows,
    }


def _row(case_id: str, **overrides) -> dict:
    row = {
        "case_id": case_id,
        "language": "ar-EG",
        "correct": True,
        "gold_claims": 4,
        "retrieved_gold_claims": 3,
        "citations_required": True,
        "citations_total": 2,
        "citations_supported": 1,
        "tool_required": True,
        "tool_attempted": 2,
        "tool_succeeded": 1,
        "latency_ms": 1000,
        "cost_usd": 0.002,
        "input_tokens": 100,
        "output_tokens": 50,
    }
    row.update(overrides)
    return row


def test_summary_computes_all_requested_metrics():
    mod = _load_module()
    data = _run("run-a", "a" * 40, [_row("AQ-001"), _row("AQ-002", correct=False)])
    summary = mod.summarize(data)
    assert summary["accuracy"] == 0.5
    assert summary["claim_recall"] == 0.75
    assert summary["citation_precision"] == 0.5
    assert summary["citation_coverage"] == 1.0
    assert summary["tool_success_rate"] == 0.5
    assert summary["latency_ms_median"] == 1000
    assert summary["latency_ms_p95"] == 1000
    assert summary["cost_usd_mean"] == pytest.approx(0.002)
    assert summary["cost_usd_total"] == pytest.approx(0.004)


def test_unknown_metrics_are_not_silently_counted_as_zero():
    mod = _load_module()
    data = _run("run-a", "a" * 40, [_row(
        "AQ-001", correct=None, gold_claims=None, retrieved_gold_claims=None,
        citations_total=None, citations_supported=None, tool_attempted=None,
        tool_succeeded=None, latency_ms=None, cost_usd=None,
    )])
    summary = mod.summarize(data)
    assert summary["accuracy"] is None
    assert summary["claim_recall"] is None
    assert summary["citation_precision"] is None
    assert summary["tool_success_rate"] is None
    assert summary["latency_ms_median"] is None
    assert summary["cost_usd_mean"] is None


def test_required_tool_explicitly_not_attempted_counts_as_failure():
    mod = _load_module()
    data = _run("run-a", "a" * 40, [_row("AQ-001", tool_attempted=0, tool_succeeded=0)])
    summary = mod.summarize(data)
    assert summary["tool_success_rate"] == 0.0
    assert summary["tool_attempt_denominator"] == 1


def test_comparison_uses_only_paired_case_ids_and_reports_deltas():
    mod = _load_module()
    baseline = _run("baseline", "a" * 40, [_row("AQ-001"), _row("AQ-002")])
    candidate = _run(
        "candidate", "b" * 40,
        [_row("AQ-001", correct=False, latency_ms=2000, cost_usd=0.004), _row("AQ-003")],
    )
    report = mod.compare_runs(baseline, candidate)
    assert report["paired_case_ids"] == ["AQ-001"]
    assert report["paired_case_count"] == 1
    assert report["baseline_summary"]["accuracy"] == 1.0
    assert report["candidate_summary"]["accuracy"] == 0.0
    assert report["candidate_summary"]["latency_ms_median"] == 2000
    assert "Gold-claim recall" in mod.render_markdown(report)


def test_comparison_rejects_different_benchmark_versions():
    mod = _load_module()
    baseline = _run("baseline", "a" * 40, [_row("AQ-001")])
    candidate = _run("candidate", "b" * 40, [_row("AQ-001")])
    candidate["benchmark_version"] = "2.0"
    with pytest.raises(ValueError, match="benchmark_version"):
        mod.compare_runs(baseline, candidate)


def test_validation_rejects_invalid_metric_counts():
    mod = _load_module()
    data = _run("run-a", "a" * 40, [_row("AQ-001", citations_supported=3, citations_total=2)])
    assert any("cannot exceed citations_total" in issue for issue in mod.validate_run(data))


def test_validation_rejects_duplicate_case_ids():
    mod = _load_module()
    data = _run("run-a", "a" * 40, [_row("AQ-001"), _row("AQ-001")])
    assert any("unique" in issue for issue in mod.validate_run(data))


def test_not_measured_baseline_cannot_contain_fabricated_results():
    mod = _load_module()
    data = _run("baseline", "a" * 40, [_row("AQ-001")])
    data["baseline_status"] = "NOT_MEASURED"
    assert any("must not contain fabricated" in issue for issue in mod.validate_run(data))


def test_percentile_interpolates_deterministically():
    mod = _load_module()
    assert mod.percentile([10, 20, 30, 40], 0.95) == pytest.approx(38.5)
    assert mod.percentile([], 0.95) is None
