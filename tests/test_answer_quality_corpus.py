"""Structural validation for the offline answer-quality adversarial corpus.

This module does NOT execute Omarai against the cases and does NOT claim that
any reasoning case passed. It only verifies that the benchmark file is complete,
internally consistent, and ready for human or fixture-assisted review.
"""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

CORPUS_PATH = Path(__file__).resolve().parent / "fixtures" / "answer_quality_cases.json"

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
ALLOWED_EVAL_MODES = {"deterministic_structure", "fixture_assisted", "human_judgment"}

# Mission-required thematic coverage (mapped to corpus category ids).
REQUIRED_THEME_CATEGORIES = {
    "simple_conversational",
    "general_knowledge",
    "omarai_capabilities",
    "current_information",
    "multi_subquestions",
    "ambiguous_clarify",
    "spelling_variation",
    "irrelevant_results",
    "empty_or_failed_search",
    "conflicting_sources",
    "stale_sources_for_current",
    "false_corroboration",
    "unsupported_claim",
    "invalid_links",
    "prompt_injection_in_content",
    "secret_exfiltration_attempt",
    "missing_model_credentials",
    "overconfidence_insufficient_evidence",
    "incomplete_answer",
    "lead_not_verified",
}

CASE_ID_RE = re.compile(r"^AQ-\d{3}$")


def _load_corpus() -> dict:
    assert CORPUS_PATH.is_file(), f"Missing corpus file: {CORPUS_PATH}"
    data = json.loads(CORPUS_PATH.read_text(encoding="utf-8"))
    assert isinstance(data, dict), "Corpus root must be an object"
    return data


def test_corpus_file_loads_as_utf8_json():
    data = _load_corpus()
    assert data.get("benchmark_id") == "OMARAI-REDTEAM-001"
    assert isinstance(data.get("cases"), list)
    assert data["case_count"] == len(data["cases"])


def test_minimum_case_count():
    data = _load_corpus()
    assert len(data["cases"]) >= 40, f"Need at least 40 cases, found {len(data['cases'])}"


def test_case_ids_unique_and_shaped():
    data = _load_corpus()
    ids = [c["case_id"] for c in data["cases"]]
    assert len(ids) == len(set(ids)), "Duplicate case_id values found"
    for case_id in ids:
        assert CASE_ID_RE.match(case_id), f"Bad case_id shape: {case_id}"


def test_required_fields_and_types():
    data = _load_corpus()
    for case in data["cases"]:
        missing = REQUIRED_CASE_FIELDS - set(case)
        assert not missing, f"{case.get('case_id')}: missing {missing}"
        assert isinstance(case["case_id"], str) and case["case_id"].strip()
        assert isinstance(case["category"], str) and case["category"].strip()
        assert isinstance(case["language"], str) and case["language"].strip()
        assert isinstance(case["question"], str) and len(case["question"].strip()) >= 2
        assert case["expected_strategy"] in ALLOWED_STRATEGIES
        assert case["evaluation_mode"] in ALLOWED_EVAL_MODES
        assert isinstance(case["required_behaviors"], list) and case["required_behaviors"]
        assert isinstance(case["forbidden_behaviors"], list) and case["forbidden_behaviors"]
        assert isinstance(case["failure_conditions"], list) and case["failure_conditions"]
        assert isinstance(case["evidence_fixture"], dict)
        for item in case["required_behaviors"] + case["forbidden_behaviors"] + case["failure_conditions"]:
            assert isinstance(item, str) and item.strip(), f"{case['case_id']}: empty behavior/condition"


def test_required_theme_categories_represented():
    data = _load_corpus()
    present = {c["category"] for c in data["cases"]}
    missing = REQUIRED_THEME_CATEGORIES - present
    assert not missing, f"Missing required categories: {sorted(missing)}"


def test_no_empty_or_near_duplicate_questions():
    data = _load_corpus()
    normalized = []
    for case in data["cases"]:
        q = " ".join(case["question"].casefold().split())
        assert len(q) >= 3, f"{case['case_id']}: question too short"
        normalized.append((case["case_id"], q))
    counts = Counter(q for _, q in normalized)
    dupes = [q for q, n in counts.items() if n > 1]
    assert not dupes, f"Duplicate questions: {dupes}"
    prefixes = Counter(q[:40] for _, q in normalized if len(q) >= 40)
    near = [p for p, n in prefixes.items() if n > 1]
    assert not near, f"Near-duplicate question prefixes: {near}"


def test_research_cases_declare_fixture_or_controlled_env():
    data = _load_corpus()
    for case in data["cases"]:
        if case["expected_strategy"] != "web_search":
            continue
        fixture = case["evidence_fixture"]
        assert fixture.get("type") in {
            "controlled_search",
            "controlled_page",
            "controlled_fetch_failure",
            "ssrf_blocked",
            "env",
            "none",
        } or "notes" in fixture, f"{case['case_id']}: research case needs a clear evidence fixture"


def test_safety_categories_include_injection_and_secrets():
    data = _load_corpus()
    cats = {c["category"] for c in data["cases"]}
    assert "prompt_injection_in_content" in cats
    assert "secret_exfiltration_attempt" in cats
    secret_failures = [
        c
        for c in data["cases"]
        if any("token" in f.casefold() or "secret" in f.casefold() or "key" in f.casefold() for f in c["failure_conditions"])
    ]
    assert secret_failures, "Expected at least one case with secret-related failure conditions"


def test_corpus_does_not_claim_live_execution_results():
    """Guardrail: the fixture file must not embed fabricated PASS/FAIL run outcomes."""
    raw = CORPUS_PATH.read_text(encoding="utf-8")
    data = json.loads(raw)
    for case in data["cases"]:
        assert "observed_result" not in case
        assert "score" not in case
        assert case.get("status") not in {"PASS", "FAIL"}


def test_languages_include_arabic_english_and_mixed():
    data = _load_corpus()
    langs = {c["language"] for c in data["cases"]}
    assert any(x.startswith("ar") for x in langs)
    assert "en" in langs
    assert "mixed" in langs
