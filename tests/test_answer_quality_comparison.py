from __future__ import annotations

import importlib.util
import json
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
    corpus = json.loads(CORPUS_PATH.read_text(encoding="utf-8"))
    return {
        "benchmark_id": corpus["benchmark_id"],
        "benchmark_version": corpus["version"],
        "build_sha": build_sha,
        "executed_at_utc": "2026-10-29T12:00:00+00:00",
        "results": results,
    }


def _row(case_id: str, *, latency: float, tool_status: str, cost: float | None, request_cost: float | None = None, expected_strategy: str = "web_search") -> dict:
    row = {
        "case_id": case_id,
        "prompt": "Test question " + case_id,
        "expected_strategy": expected_strategy,
        "transport_ok": True,
        "elapsed_ms": latency,
        "tool_status": tool_status,
        "search_outcome": "attempted_with_usable_sources" if tool_status == "SUCCESS_WITH_USABLE_RESULTS" else "attempted_no_usable_sources",
        "provider_reported_model_cost_status": "COMPLETE_FOR_RETURNED_MODEL_CALLS" if cost is not None else "PROVIDER_COST_NOT_REPORTED",
        "request_cost_status": "RECONCILED_COMPLETE_REQUEST_COST" if request_cost is not None else "NOT_MEASURED_TOTAL_CONNECTOR_COSTS_NOT_EXPOSED",
        "required_tool_statuses": (
            [{
                "tool": "web_search",
                "status": "completed_with_results" if tool_status == "SUCCESS_WITH_USABLE_RESULTS" else "completed_no_usable_results",
                "successful_completion": tool_status == "SUCCESS_WITH_USABLE_RESULTS",
            }]
            if expected_strategy == "web_search"
            else []
        ),
    }
    if cost is not None:
        row["provider_reported_model_cost_usd"] = cost
    if request_cost is not None:
        row["request_cost_usd"] = request_cost
    return row


def _reviews(*, correct: int, supported_citations: int) -> dict:
    corpus = json.loads(CORPUS_PATH.read_text(encoding="utf-8"))
    return {
        "schema_version": "1.0",
        "reviews": [
            {
                "case_id": case["case_id"],
                "status": "REVIEWED",
                "retrieval": {
                    "relevant_retrieved": 2 if case["case_id"] == "AQ-007" else 1,
                    "retrieved_count": 3,
                    "relevant_available": 3 if case["case_id"] == "AQ-007" else 2,
                },
                "faithfulness": {"supported_claims": correct, "reviewed_claims": 3},
                "correctness": {"correct_facts": correct, "reviewed_facts": 3},
                "citations": {
                    "supported_citations": supported_citations,
                    "reviewed_citations": 2,
                },
                "writing_quality": 4,
            }
            for case in corpus["cases"]
        ],
    }


def _full_run(*, build_sha: str, candidate: bool) -> dict:
    corpus = json.loads(CORPUS_PATH.read_text(encoding="utf-8"))
    rows = []
    for case in corpus["cases"]:
        case_id = case["case_id"]
        is_aq007 = case_id == "AQ-007"
        is_aq008 = case_id == "AQ-008"
        if candidate:
            latency = 80 if is_aq007 else 120 if is_aq008 else 100
            status = "SUCCESS_WITH_USABLE_RESULTS"
            model_cost = 0.005 if is_aq007 else 0.002 if is_aq008 else None
            request_cost = 0.007 if is_aq007 else 0.009 if is_aq008 else 0.001
        else:
            latency = 100 if is_aq007 else 200 if is_aq008 else 150
            status = "SUCCESS_WITH_USABLE_RESULTS" if is_aq007 else "ATTEMPTED_NO_USABLE_RESULTS"
            model_cost = 0.01 if is_aq007 else None
            request_cost = 0.012 if is_aq007 else 0.015 if is_aq008 else 0.001
        rows.append({
            **_row(
                case_id, latency=latency, tool_status=status,
                cost=model_cost, request_cost=request_cost,
                expected_strategy=case["expected_strategy"],
            ),
            "prompt": case["question"],
        })
    return _run(build_sha=build_sha, results=rows)


def test_comparison_measures_latency_tools_cost_and_human_reviewed_quality():
    mod = load_module()
    baseline = _full_run(build_sha="a" * 40, candidate=False)
    candidate = _full_run(build_sha="b" * 40, candidate=True)
    corpus = mod.load_json_object(CORPUS_PATH)
    result = mod.compare_runs(
        baseline,
        candidate,
        corpus=corpus,
        baseline_reviews=_reviews(correct=2, supported_citations=1),
        candidate_reviews=_reviews(correct=3, supported_citations=2),
    )
    assert result["acceptance_status"] == "COMPARABLE_WITH_REVIEWED_QUALITY_AND_BUILD_IDENTITIES"
    assert result["case_count"] == 45
    assert result["baseline"]["metrics"]["latency_ms"]["p50"] == 150
    assert result["candidate"]["metrics"]["latency_ms"]["p95"] == 120
    assert result["runtime_deltas"]["usable_result_rate"]["baseline"] == pytest.approx(1 / 30)
    assert result["runtime_deltas"]["usable_result_rate"]["candidate"] == 1.0
    assert result["runtime_deltas"]["required_tool_success_rate"]["baseline"] == pytest.approx(1 / 30)
    assert result["runtime_deltas"]["required_tool_success_rate"]["candidate"] == 1.0
    assert result["runtime_deltas"]["required_tool_success_rate"]["delta"] == pytest.approx(29 / 30)
    assert result["runtime_deltas"]["provider_reported_model_cost_usd"]["delta"] == -0.003
    assert result["baseline"]["metrics"]["provider_reported_model_cost"]["complete_request_cost_usd"] == pytest.approx(0.070)
    assert result["runtime_deltas"]["complete_request_cost_usd"]["delta"] == pytest.approx(-0.011)
    assert result["runtime_deltas"]["complete_request_cost_usd"]["status"] == "COMPARED"
    assert result["quality_comparison"]["metrics"]["factual_accuracy"]["baseline"] == pytest.approx(2 / 3, abs=0.0001)
    assert result["quality_comparison"]["metrics"]["factual_accuracy"]["candidate"] == 1.0
    assert result["quality_comparison"]["metrics"]["citation_support"]["delta"] == 0.5


def test_missing_build_sha_and_review_data_cannot_claim_complete_acceptance():
    mod = load_module()
    baseline = _run(build_sha="unknown", results=[_row("AQ-001", latency=100, tool_status="SUCCESS_WITH_USABLE_RESULTS", cost=None)])
    candidate = _run(build_sha="", results=[_row("AQ-001", latency=90, tool_status="SUCCESS_WITH_USABLE_RESULTS", cost=None)])
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


def test_quality_comparison_rejects_incomplete_human_review_coverage():
    mod = load_module()
    corpus = mod.load_json_object(CORPUS_PATH)
    partial = {
        "schema_version": "1.0",
        "reviews": [{
            "case_id": "AQ-001",
            "status": "REVIEWED",
            "correctness": {"correct_facts": 1, "reviewed_facts": 1},
        }],
    }
    full = _reviews(correct=1, supported_citations=1)
    with pytest.raises(ValueError, match="incomplete human review coverage"):
        mod.review_comparison(partial, full, corpus)


def test_comparison_requires_nonempty_recorded_question_text():
    mod = load_module()
    baseline = _run(build_sha="a" * 40, results=[{"case_id": "AQ-001", "elapsed_ms": 20}])
    candidate = _run(build_sha="b" * 40, results=[{"case_id": "AQ-001", "elapsed_ms": 10}])
    errors = mod.validate_run(baseline, "baseline")
    assert any("prompt must be a non-empty string" in error for error in errors)
    with pytest.raises(ValueError, match="prompt must be a non-empty string"):
        mod.compare_runs(baseline, candidate)
