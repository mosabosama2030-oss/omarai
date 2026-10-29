from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "compare_answer_quality_runs.py"
CORPUS_PATH = ROOT / "tests" / "fixtures" / "answer_quality_cases.json"


def load_module():
    spec = importlib.util.spec_from_file_location("answer_quality_run_comparison", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _run(*, build_sha: str, results: list[dict]) -> dict:
    return {
        "benchmark_id": "OMARAI-REDTEAM-001",
        "benchmark_version": "1.0.0",
        "build_sha": build_sha,
        "executed_at_utc": "2026-10-29T12:00:00+00:00",
        "results": results,
    }


def _row(case_id: str, *, latency: float, tool_status: str, cost: float | None, request_cost: float | None = None) -> dict:
    row = {
        "case_id": case_id,
        "prompt": "Test question " + case_id,
        "expected_strategy": "web_search",
        "transport_ok": True,
        "elapsed_ms": latency,
        "tool_status": tool_status,
        "search_outcome": "attempted_with_usable_sources" if tool_status == "SUCCESS_WITH_USABLE_RESULTS" else "attempted_no_usable_sources",
        "provider_reported_model_cost_status": "COMPLETE_FOR_RETURNED_MODEL_CALLS" if cost is not None else "PROVIDER_COST_NOT_REPORTED",
        "request_cost_status": "RECONCILED_COMPLETE_REQUEST_COST" if request_cost is not None else "NOT_MEASURED_TOTAL_CONNECTOR_COSTS_NOT_EXPOSED",
    }
    if cost is not None:
        row["provider_reported_model_cost_usd"] = cost
    if request_cost is not None:
        row["request_cost_usd"] = request_cost
    return row


def _reviews(*, correct: int, supported_citations: int) -> dict:
    return {
        "schema_version": "1.0",
        "reviews": [
            {
                "case_id": case_id,
                "status": "REVIEWED",
                "retrieval": {
                    "relevant_retrieved": 2 if case_id == "AQ-007" else 1,
                    "retrieved_count": 3,
                    "relevant_available": 3 if case_id == "AQ-007" else 2,
                },
                "faithfulness": {"supported_claims": correct, "reviewed_claims": 3},
                "correctness": {"correct_facts": correct, "reviewed_facts": 3},
                "citations": {
                    "supported_citations": supported_citations,
                    "reviewed_citations": 2,
                },
                "writing_quality": 4,
            }
            for case_id in ("AQ-007", "AQ-008")
        ],
    }


def test_comparison_measures_latency_tools_cost_and_human_reviewed_quality():
    mod = load_module()
    baseline = _run(
        build_sha="a" * 40,
        results=[
            _row("AQ-007", latency=100, tool_status="SUCCESS_WITH_USABLE_RESULTS", cost=0.01, request_cost=0.012),
            _row("AQ-008", latency=200, tool_status="ATTEMPTED_NO_USABLE_RESULTS", cost=None, request_cost=0.015),
        ],
    )
    candidate = _run(
        build_sha="b" * 40,
        results=[
            _row("AQ-007", latency=80, tool_status="SUCCESS_WITH_USABLE_RESULTS", cost=0.005, request_cost=0.007),
            _row("AQ-008", latency=120, tool_status="SUCCESS_WITH_USABLE_RESULTS", cost=0.002, request_cost=0.009),
        ],
    )
    corpus = mod.load_json_object(CORPUS_PATH)
    result = mod.compare_runs(
        baseline,
        candidate,
        corpus=corpus,
        baseline_reviews=_reviews(correct=2, supported_citations=1),
        candidate_reviews=_reviews(correct=3, supported_citations=2),
    )
    assert result["acceptance_status"] == "COMPARABLE_WITH_REVIEWED_QUALITY_AND_BUILD_IDENTITIES"
    assert result["case_count"] == 2
    assert result["baseline"]["metrics"]["latency_ms"]["p50"] == 100
    assert result["candidate"]["metrics"]["latency_ms"]["p95"] == 120
    assert result["runtime_deltas"]["usable_result_rate"]["baseline"] == 0.5
    assert result["runtime_deltas"]["usable_result_rate"]["candidate"] == 1.0
    assert result["runtime_deltas"]["provider_reported_model_cost_usd"]["delta"] == -0.003
    assert result["baseline"]["metrics"]["provider_reported_model_cost"]["complete_request_cost_usd"] == 0.027
    assert result["runtime_deltas"]["complete_request_cost_usd"]["delta"] == -0.011
    assert result["runtime_deltas"]["complete_request_cost_usd"]["status"] == "COMPARED"
    assert result["quality_comparison"]["metrics"]["factual_accuracy"]["baseline"] == pytest.approx(2 / 3, abs=0.0001)
    assert result["quality_comparison"]["metrics"]["factual_accuracy"]["candidate"] == 1.0
    assert result["quality_comparison"]["metrics"]["citation_support"]["delta"] == 0.5


def test_missing_build_sha_and_review_data_cannot_claim_complete_acceptance():
    mod = load_module()
    baseline = _run(build_sha="unknown", results=[_row("AQ-007", latency=100, tool_status="SUCCESS_WITH_USABLE_RESULTS", cost=None)])
    candidate = _run(build_sha="", results=[_row("AQ-007", latency=90, tool_status="SUCCESS_WITH_USABLE_RESULTS", cost=None)])
    result = mod.compare_runs(baseline, candidate)
    assert result["acceptance_status"] == "INCOMPLETE"
    assert "baseline_build_sha_missing_or_invalid" in result["acceptance_blockers"]
    assert "candidate_build_sha_missing_or_invalid" in result["acceptance_blockers"]
    assert "human_review_files_missing" in result["acceptance_blockers"]
    assert result["quality_comparison"] is None
    assert result["baseline"]["metrics"]["provider_reported_model_cost"]["reported_sum_usd"] is None
    assert result["runtime_deltas"]["provider_reported_model_cost_usd"]["status"] == "NOT_MEASURED"


def test_comparison_rejects_different_case_sets_and_questions():
    mod = load_module()
    baseline = _run(build_sha="a" * 40, results=[_row("AQ-007", latency=100, tool_status="SUCCESS_WITH_USABLE_RESULTS", cost=None)])
    missing = _run(build_sha="b" * 40, results=[_row("AQ-008", latency=90, tool_status="SUCCESS_WITH_USABLE_RESULTS", cost=None)])
    with pytest.raises(ValueError, match="incomparable case sets"):
        mod.compare_runs(baseline, missing)
    changed_question = _run(
        build_sha="b" * 40,
        results=[{**_row("AQ-007", latency=90, tool_status="SUCCESS_WITH_USABLE_RESULTS", cost=None), "prompt": "A different prompt"}],
    )
    with pytest.raises(ValueError, match="incomparable question text"):
        mod.compare_runs(baseline, changed_question)


def test_run_validation_rejects_duplicate_ids_and_invalid_latency():
    mod = load_module()
    run = _run(
        build_sha="a" * 40,
        results=[
            _row("AQ-007", latency=-1, tool_status="UNKNOWN", cost=None),
            _row("AQ-007", latency=10, tool_status="UNKNOWN", cost=None),
        ],
    )
    errors = mod.validate_run(run, "run")
    assert any("duplicate case_id" in error for error in errors)
    assert any("elapsed_ms must be finite and non-negative" in error for error in errors)
