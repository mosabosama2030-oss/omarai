from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "score_answer_quality_reviews.py"
CORPUS_PATH = ROOT / "tests" / "fixtures" / "answer_quality_cases.json"


def load_module():
    spec = importlib.util.spec_from_file_location("answer_quality_review_scorecard", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def corpus():
    return load_module().load_json_object(CORPUS_PATH)


def test_manual_scorecard_aggregates_only_explicit_reviewed_metrics():
    mod = load_module()
    data = {
        "schema_version": "1.0",
        "reviews": [
            {
                "case_id": "AQ-007",
                "status": "REVIEWED",
                "retrieval": {"relevant_retrieved": 3, "retrieved_count": 5, "relevant_available": 4},
                "faithfulness": {"supported_claims": 4, "reviewed_claims": 5},
                "correctness": {"correct_facts": 3, "reviewed_facts": 4},
                "citations": {"supported_citations": 2, "reviewed_citations": 3},
                "writing_quality": 4,
            },
            {
                "case_id": "AQ-008",
                "status": "REVIEWED",
                "writing_quality": 4,
            },
            {"case_id": "AQ-009", "status": "NOT_TESTED", "notes": "No reviewer judgment yet."},
        ],
    }
    result = mod.summarize_reviews(data, corpus())
    assert result["metrics"]["retrieval_precision"]["score"] == 0.6
    assert result["metrics"]["retrieval_recall"]["score"] == 0.75
    assert result["metrics"]["faithfulness"]["score"] == 0.8
    assert result["metrics"]["correctness"]["score"] == 0.75
    assert result["metrics"]["citation_support"]["score"] == pytest.approx(2 / 3, abs=0.0001)
    assert result["metrics"]["writing_quality_1_to_5"]["score"] == 4.0
    assert result["case_status_counts"]["NOT_TESTED"] == 1
    assert result["unique_reviewed_case_count"] == 2
    assert result["automatic_answer_grading"] is False
    assert result["ragas_executed"] is False


def test_scorecard_keeps_unmeasured_denominators_not_scorable():
    mod = load_module()
    data = {
        "reviews": [{
            "case_id": "AQ-001",
            "status": "REVIEWED",
            "faithfulness": {"supported_claims": 0, "reviewed_claims": 0},
        }],
    }
    result = mod.summarize_reviews(data, corpus())
    assert result["metrics"]["faithfulness"]["score"] is None
    assert result["metrics"]["faithfulness"]["status"] == "NOT_SCORABLE_NO_ANNOTATED_DENOMINATOR"
    assert result["metrics"]["retrieval_precision"]["score"] is None


def test_scorecard_rejects_numerator_larger_than_denominator():
    mod = load_module()
    data = {
        "reviews": [{
            "case_id": "AQ-007",
            "status": "REVIEWED",
            "faithfulness": {"supported_claims": 3, "reviewed_claims": 2},
        }],
    }
    with pytest.raises(ValueError, match="cannot exceed"):
        mod.summarize_reviews(data, corpus())


def test_scorecard_rejects_unknown_case_ids_and_duplicate_reviews():
    mod = load_module()
    data = {"reviews": [
        {"case_id": "AQ-999", "status": "NOT_TESTED"},
        {"case_id": "AQ-001", "status": "NOT_TESTED"},
        {"case_id": "AQ-001", "status": "NOT_TESTED"},
    ]}
    issues = mod.validate_reviews(data, corpus())
    assert any("unknown case_id" in issue for issue in issues)
    assert any("duplicate review" in issue for issue in issues)


def test_not_tested_cases_must_not_carry_metric_scores():
    mod = load_module()
    data = {"reviews": [{
        "case_id": "AQ-001", "status": "NOT_TESTED",
        "writing_quality": 5,
    }]}
    issues = mod.validate_reviews(data, corpus())
    assert any("unreviewed case must not contain metric scores" in issue for issue in issues)


def test_scorecard_cli_writes_a_machine_readable_summary(tmp_path, capsys):
    mod = load_module()
    reviews_path = tmp_path / "reviews.json"
    output_path = tmp_path / "summary.json"
    reviews_path.write_text('{"schema_version":"1.0","reviews":[{"case_id":"AQ-001","status":"REVIEWED","writing_quality":5}]}', encoding="utf-8")
    rc = mod.main(["--reviews", str(reviews_path), "--corpus", str(CORPUS_PATH), "--out", str(output_path)])
    assert rc == 0
    assert '"score": 5.0' in capsys.readouterr().out
    assert output_path.is_file()
