"""Score manually reviewed Omarai answer-quality cases without auto-grading.

This offline tool calculates aggregate retrieval, faithfulness, correctness, citation,
and writing-quality metrics only from explicit review annotations. Missing judgments
remain NOT_TESTED; this script never calls an LLM or treats transport success as PASS.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CORPUS = ROOT / "tests" / "fixtures" / "answer_quality_cases.json"
ALLOWED_STATUSES = {"REVIEWED", "NOT_TESTED", "BLOCKED"}
COUNT_GROUPS = {
    "retrieval": ("relevant_retrieved", "retrieved_count", "relevant_available"),
    "faithfulness": ("supported_claims", "reviewed_claims"),
    "correctness": ("correct_facts", "reviewed_facts"),
    "citations": ("supported_citations", "reviewed_citations"),
}


def load_json_object(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise FileNotFoundError("Input file not found: " + str(path))
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise TypeError("JSON root must be an object")
    return data


def _is_nonnegative_int(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value >= 0


def validate_reviews(
    review_data: dict[str, Any], corpus_data: dict[str, Any]
) -> list[str]:
    problems: list[str] = []
    reviews = review_data.get("reviews")
    corpus_cases = corpus_data.get("cases")
    if not isinstance(reviews, list):
        return ["reviews must be an array"]
    if not isinstance(corpus_cases, list):
        return ["corpus must contain a cases array"]

    valid_case_ids = {
        item.get("case_id")
        for item in corpus_cases
        if isinstance(item, dict) and isinstance(item.get("case_id"), str)
    }
    seen: set[str] = set()
    for index, item in enumerate(reviews):
        label = "reviews[" + str(index) + "]"
        if not isinstance(item, dict):
            problems.append(label + " must be an object")
            continue
        case_id = item.get("case_id")
        if not isinstance(case_id, str) or not case_id.strip():
            problems.append(label + ": case_id must be a non-empty string")
            continue
        if case_id in seen:
            problems.append(case_id + ": duplicate review")
        seen.add(case_id)
        if case_id not in valid_case_ids:
            problems.append(case_id + ": unknown case_id (not in the supplied corpus)")
        status = item.get("status")
        if status not in ALLOWED_STATUSES:
            problems.append(case_id + ": status must be one of " + ", ".join(sorted(ALLOWED_STATUSES)))
            continue

        has_score = False
        for group_name, fields in COUNT_GROUPS.items():
            group = item.get(group_name)
            if group is None:
                continue
            if not isinstance(group, dict):
                problems.append(case_id + ": " + group_name + " must be an object")
                continue
            has_score = True
            missing = [field for field in fields if field not in group]
            if missing:
                problems.append(case_id + ": " + group_name + " missing " + ", ".join(missing))
                continue
            values: dict[str, int] = {}
            for field in fields:
                value = group[field]
                if not _is_nonnegative_int(value):
                    problems.append(case_id + ": " + group_name + "." + field + " must be a non-negative integer")
                else:
                    values[field] = value
            if len(values) != len(fields):
                continue
            if group_name == "retrieval":
                if values["relevant_retrieved"] > values["retrieved_count"]:
                    problems.append(case_id + ": relevant_retrieved cannot exceed retrieved_count")
                if values["relevant_retrieved"] > values["relevant_available"]:
                    problems.append(case_id + ": relevant_retrieved cannot exceed relevant_available")
            else:
                numerator, denominator = fields
                if values[numerator] > values[denominator]:
                    problems.append(case_id + ": " + numerator + " cannot exceed " + denominator)

        writing = item.get("writing_quality")
        if writing is not None:
            has_score = True
            if (
                isinstance(writing, bool)
                or not isinstance(writing, (int, float))
                or not math.isfinite(float(writing))
                or float(writing) < 1
                or float(writing) > 5
            ):
                problems.append(case_id + ": writing_quality must be a finite score from 1 to 5")

        if status != "REVIEWED" and has_score:
            problems.append(case_id + ": unreviewed case must not contain metric scores")
        if status == "REVIEWED" and not has_score:
            problems.append(case_id + ": REVIEWED case must include at least one scored dimension")
    return problems


def _ratio(numerator: int, denominator: int, case_count: int) -> dict[str, Any]:
    return {
        "score": round(numerator / denominator, 4) if denominator else None,
        "numerator": numerator,
        "denominator": denominator,
        "reviewed_case_count": case_count,
        "status": "SCORED_FROM_HUMAN_REVIEW" if denominator else "NOT_SCORABLE_NO_ANNOTATED_DENOMINATOR",
    }


def summarize_reviews(
    review_data: dict[str, Any], corpus_data: dict[str, Any]
) -> dict[str, Any]:
    problems = validate_reviews(review_data, corpus_data)
    if problems:
        raise ValueError("; ".join(problems))
    reviews = review_data["reviews"]
    reviewed = [item for item in reviews if item["status"] == "REVIEWED"]
    status_counts = Counter(item["status"] for item in reviews)
    corpus_count = len(corpus_data["cases"])
    reviewed_ids = {item["case_id"] for item in reviewed}

    retrieval_rel = retrieval_total = retrieval_available = 0
    retrieval_cases = set()
    faithfulness_supported = faithfulness_total = 0
    faithfulness_cases = set()
    correctness_correct = correctness_total = 0
    correctness_cases = set()
    citation_supported = citation_total = 0
    citation_cases = set()
    writing_scores: list[float] = []

    for item in reviewed:
        case_id = item["case_id"]
        retrieval = item.get("retrieval")
        if isinstance(retrieval, dict):
            retrieval_rel += retrieval["relevant_retrieved"]
            retrieval_total += retrieval["retrieved_count"]
            retrieval_available += retrieval["relevant_available"]
            retrieval_cases.add(case_id)
        faithfulness = item.get("faithfulness")
        if isinstance(faithfulness, dict):
            faithfulness_supported += faithfulness["supported_claims"]
            faithfulness_total += faithfulness["reviewed_claims"]
            faithfulness_cases.add(case_id)
        correctness = item.get("correctness")
        if isinstance(correctness, dict):
            correctness_correct += correctness["correct_facts"]
            correctness_total += correctness["reviewed_facts"]
            correctness_cases.add(case_id)
        citations = item.get("citations")
        if isinstance(citations, dict):
            citation_supported += citations["supported_citations"]
            citation_total += citations["reviewed_citations"]
            citation_cases.add(case_id)
        score = item.get("writing_quality")
        if score is not None:
            writing_scores.append(float(score))

    return {
        "benchmark_id": corpus_data.get("benchmark_id", "unknown"),
        "review_schema_version": review_data.get("schema_version", "unknown"),
        "scoring_method": "aggregate_from_explicit_human_annotations",
        "automatic_answer_grading": False,
        "ragas_executed": False,
        "corpus_case_count": corpus_count,
        "submitted_review_count": len(reviews),
        "unique_reviewed_case_count": len(reviewed_ids),
        "case_status_counts": {status: status_counts.get(status, 0) for status in sorted(ALLOWED_STATUSES)},
        "reviewed_case_coverage": round(len(reviewed_ids) / corpus_count, 4) if corpus_count else 0.0,
        "metrics": {
            "retrieval_precision": _ratio(retrieval_rel, retrieval_total, len(retrieval_cases)),
            "retrieval_recall": _ratio(retrieval_rel, retrieval_available, len(retrieval_cases)),
            "faithfulness": _ratio(faithfulness_supported, faithfulness_total, len(faithfulness_cases)),
            "correctness": _ratio(correctness_correct, correctness_total, len(correctness_cases)),
            "citation_support": _ratio(citation_supported, citation_total, len(citation_cases)),
            "writing_quality_1_to_5": {
                "score": round(sum(writing_scores) / len(writing_scores), 3) if writing_scores else None,
                "scale_min": 1,
                "scale_max": 5,
                "reviewed_case_count": len(writing_scores),
                "status": "SCORED_FROM_HUMAN_REVIEW" if writing_scores else "NOT_SCORABLE_NO_HUMAN_SCORES",
            },
        },
        "limitations": [
            "Metrics include only explicitly reviewed cases and human-entered labels.",
            "Retrieval scores depend on consistent, deduplicated relevance counts and a defined candidate pool.",
            "Faithfulness and correctness reflect reviewer judgments, not automatic proof of truth.",
            "Writing quality is a 1-to-5 human rating; it is not a fluency model score.",
            "RAGAS was not executed and no unobserved case is assigned a PASS.",
        ],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reviews", required=True, type=Path, help="JSON file containing explicit human review annotations")
    parser.add_argument("--corpus", default=DEFAULT_CORPUS, type=Path, help="Answer-quality corpus used to validate case IDs")
    parser.add_argument("--out", type=Path, help="Optional path to write the summary JSON")
    args = parser.parse_args(argv)

    try:
        reviews = load_json_object(args.reviews)
        corpus = load_json_object(args.corpus)
        summary = summarize_reviews(reviews, corpus)
    except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
        print("REVIEW SCORECARD INVALID: " + str(exc), file=sys.stderr)
        return 2

    output = json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True)
    if args.out:
        args.out.write_text(output + "\n", encoding="utf-8")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
