"""Structural validation for the Omarai answer-quality adversarial corpus.

This module validates the benchmark *schema and coverage only*.
It does NOT execute Omarai against the cases and must never be interpreted
as evidence of successful reasoning or safety outcomes on live answers.
"""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

import pytest

FIXTURE_PATH = Path(__file__).resolve().parent / "fixtures" / "answer_quality_cases.json"

REQUIRED_CASE_FIELDS = {
    "case_id",
    "category",
    "language",
    "question",
    "expected_strategy",
    "required_behaviors",
    "forbidden_behaviors",
    "evidence_fixture",
    "failure_conditions",
    "evaluation_mode",
}

ALLOWED_STRATEGIES = {"local", "model_no_search", "web_search", "clarify"}
ALLOWED_EVAL_MODES = {
    "deterministic",
    "human_judgment",
    "human_judgment_with_fixture",
}

# Mission-required theme coverage (mapped to case categories present in the corpus).
REQUIRED_THEME_CATEGORIES = {
    "simple_conversational_no_search",
    "general_knowledge",
    "omarai_capabilities",
    "current_information",
    "multi_subquestions",
    "ambiguous_requires_clarification",
    "arabic_spelling_variation",
    "irrelevant_search_results",
    "empty_results_provider_failure",
    "conflicting_sources",
    "stale_sources_for_current_question",
    "false_independent_corroboration",
    "evidence_does_not_support_claim",
    "invalid_misleading_links",
    "prompt_injection_in_retrieved_content",
    "retrieved_override_secret_exfil",
    "missing_model_credentials",
    "overconfident_insufficient_evidence",
    "incomplete_ignores_part",
    "lead_not_verified_customer",
}


@pytest.fixture(scope="module")
def corpus() -> dict:
    assert FIXTURE_PATH.is_file(), f"Missing corpus fixture: {FIXTURE_PATH}"
    data = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    assert isinstance(data, dict)
    return data


@pytest.fixture(scope="module")
def cases(corpus: dict) -> list[dict]:
    raw = corpus.get("cases")
    assert isinstance(raw, list) and raw, "corpus.cases must be a non-empty list"
    return raw


def test_corpus_metadata(corpus: dict):
    assert corpus.get("benchmark_id") == "OMARAI-REDTEAM-001"
    assert isinstance(corpus.get("version"), str) and corpus["version"]
    assert set(corpus.get("allowed_strategies", [])) == ALLOWED_STRATEGIES
    modes = set(corpus.get("allowed_evaluation_modes", []))
    assert ALLOWED_EVAL_MODES.issubset(modes)
    assert corpus.get("case_count") == len(corpus["cases"])


def test_minimum_case_count(cases: list[dict]):
    assert len(cases) >= 40, f"Need at least 40 cases, found {len(cases)}"


def test_case_ids_unique_and_shaped(cases: list[dict]):
    ids = [c.get("case_id") for c in cases]
    assert all(isinstance(i, str) and i for i in ids)
    assert len(ids) == len(set(ids)), "Duplicate case_id values"
    for case_id in ids:
        assert re.fullmatch(r"AQ-\d{3,}", case_id), f"Unexpected case_id shape: {case_id}"


def test_required_fields_and_types(cases: list[dict]):
    for case in cases:
        missing = REQUIRED_CASE_FIELDS - set(case)
        assert not missing, f"{case.get('case_id')}: missing {missing}"
        assert isinstance(case["question"], str) and case["question"].strip()
        assert isinstance(case["category"], str) and case["category"].strip()
        assert isinstance(case["language"], str) and case["language"].strip()
        assert case["expected_strategy"] in ALLOWED_STRATEGIES
        assert case["evaluation_mode"] in ALLOWED_EVAL_MODES
        assert isinstance(case["required_behaviors"], list) and case["required_behaviors"]
        assert isinstance(case["forbidden_behaviors"], list) and case["forbidden_behaviors"]
        assert isinstance(case["failure_conditions"], list) and case["failure_conditions"]
        assert isinstance(case["evidence_fixture"], dict)
        for item in case["required_behaviors"] + case["forbidden_behaviors"] + case[
            "failure_conditions"
        ]:
            assert isinstance(item, str) and item.strip(), f"{case['case_id']}: empty criterion"


def test_required_theme_categories_represented(cases: list[dict]):
    present = {c["category"] for c in cases}
    missing = REQUIRED_THEME_CATEGORIES - present
    assert not missing, f"Missing required theme categories: {sorted(missing)}"


def test_strategy_distribution_not_collapsed(cases: list[dict]):
    counts = Counter(c["expected_strategy"] for c in cases)
    # Corpus must exercise more than a single strategy.
    assert len(counts) >= 3, f"Strategy diversity too low: {dict(counts)}"
    assert counts["web_search"] >= 10
    assert counts["local"] >= 3
    assert counts["clarify"] >= 2


def test_no_empty_or_near_duplicate_questions(cases: list[dict]):
    normalized = []
    for case in cases:
        q = re.sub(r"\s+", " ", case["question"].strip().casefold())
        assert len(q) >= 8, f"{case['case_id']}: question too short"
        normalized.append(q)
    assert len(normalized) == len(set(normalized)), "Duplicate or identical questions"


def test_research_cases_declare_fixture_or_env(cases: list[dict]):
    for case in cases:
        if case["expected_strategy"] != "web_search":
            continue
        fixture = case["evidence_fixture"]
        ftype = fixture.get("type")
        assert ftype in {
            "synthetic_search",
            "synthetic_page",
            "synthetic_fetch_failure",
            "ssrf_blocked",
            "env",
            "none",
        }, f"{case['case_id']}: unexpected evidence_fixture.type={ftype}"
        # Prefer explicit fixtures for web cases; allow none only with note.
        if ftype == "none":
            assert fixture.get("note"), f"{case['case_id']}: web_search with type none needs note"


def test_safety_cases_present(cases: list[dict]):
    text = " ".join(
        c["question"] + " " + json.dumps(c["evidence_fixture"], ensure_ascii=False)
        for c in cases
    ).lower()
    assert "openrouter_api_key" in text or "omarai_access_token" in text
    assert "169.254.169.254" in text or "127.0.0.1" in text
    injection_cases = [
        c
        for c in cases
        if c["category"]
        in {"prompt_injection_in_retrieved_content", "retrieved_override_secret_exfil"}
    ]
    assert len(injection_cases) >= 2
