"""Offline / optional live runner for OMARAI-REDTEAM-001 answer-quality cases.

Modes
-----
validate (default)
    Load and structurally validate the corpus. No network.

live (explicit opt-in)
    POST selected cases to an existing Omarai HTTP API (/api/agent).
    Does NOT inject JSON evidence fixtures into the server.
    Does NOT auto-grade PASS/FAIL for answer quality; records NOT_TESTED
    unless a transport/auth error makes the run unusable.

Standard library only. Secrets only via environment (never CLI flags for tokens).

Examples
--------
  python scripts/run_answer_quality_benchmark.py
  python scripts/run_answer_quality_benchmark.py --mode validate --summary
  python scripts/run_answer_quality_benchmark.py --mode live --base-url http://127.0.0.1:8765 \\
      --case-id AQ-001 --limit 1 --out /tmp/aq_results.json
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CORPUS = ROOT / "tests" / "fixtures" / "answer_quality_cases.json"

REQUIRED_FIELDS = {
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


def _utc_now() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds")


def load_corpus(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(f"Corpus not found: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("cases"), list):
        raise TypeError("Corpus root must be an object with a cases array")
    if data.get("parts"):
        raise ValueError("Incomplete shard index is not accepted; use merged cases[] corpus")
    return data


def validate_corpus(data: dict) -> list[str]:
    """Return a list of human-readable problems (empty => OK)."""
    problems: list[str] = []
    cases = data.get("cases") or []
    if data.get("case_count") != len(cases):
        problems.append(
            f"case_count metadata {data.get('case_count')!r} != len(cases) {len(cases)}"
        )
    if len(cases) < 40:
        problems.append(f"expected at least 40 cases, found {len(cases)}")
    ids: list[str] = []
    for i, case in enumerate(cases):
        if not isinstance(case, dict):
            problems.append(f"cases[{i}] is not an object")
            continue
        missing = REQUIRED_FIELDS - set(case)
        if missing:
            problems.append(f"{case.get('case_id', i)}: missing {sorted(missing)}")
        cid = case.get("case_id")
        if isinstance(cid, str):
            ids.append(cid)
        if case.get("expected_strategy") not in ALLOWED_STRATEGIES:
            problems.append(f"{cid}: bad strategy {case.get('expected_strategy')!r}")
        if case.get("evaluation_mode") not in ALLOWED_EVAL_MODES:
            problems.append(f"{cid}: bad evaluation_mode {case.get('evaluation_mode')!r}")
        q = case.get("question")
        if not isinstance(q, str) or len(q.strip()) < 2:
            problems.append(f"{cid}: empty question")
    if len(ids) != len(set(ids)):
        problems.append("duplicate case_id values")
    return problems


def redact_secrets(text: str) -> str:
    """Best-effort redaction of common secret patterns from stored outputs."""
    if not text:
        return text
    out = text
    for key in (
        "OPENROUTER_API_KEY",
        "OMARAI_ACCESS_TOKEN",
        "OMARAI_LLM_API_KEY",
        "Authorization",
        "Bearer ",
    ):
        out = out.replace(key, f"[REDACTED:{key.strip()}]")
    token = os.getenv("OMARAI_ACCESS_TOKEN", "").strip()
    if token and token in out:
        out = out.replace(token, "[REDACTED:OMARAI_ACCESS_TOKEN]")
    for env_name in ("OPENROUTER_API_KEY", "OMARAI_LLM_API_KEY"):
        val = os.getenv(env_name, "").strip()
        if val and val in out:
            out = out.replace(val, f"[REDACTED:{env_name}]")
    return out


def post_agent(
    base_url: str,
    question: str,
    timeout: float,
    token: str | None,
) -> tuple[int, dict | str]:
    url = base_url.rstrip("/") + "/api/agent"
    body = json.dumps({"question": question, "history": []}, ensure_ascii=False).encode("utf-8")
    headers = {"Content-Type": "application/json", "Content-Length": str(len(body))}
    if token:
        headers["Authorization"] = "Bearer " + token
    req = urllib.request.Request(url, data=body, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode("utf-8", errors="replace")
            status = getattr(resp, "status", 200)
            try:
                return status, json.loads(raw)
            except json.JSONDecodeError:
                return status, raw
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", errors="replace")
        try:
            return exc.code, json.loads(raw)
        except json.JSONDecodeError:
            return exc.code, raw
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return 0, {"error": type(exc).__name__, "detail": str(exc)}


def run_validate(corpus_path: Path, summary: bool) -> int:
    data = load_corpus(corpus_path)
    problems = validate_corpus(data)
    if problems:
        print("VALIDATE FAIL")
        for p in problems:
            print(" -", p)
        return 1
    cases = data["cases"]
    cats = sorted({c["category"] for c in cases})
    langs = sorted({c["language"] for c in cases})
    print("VALIDATE OK")
    print(f"benchmark_id={data.get('benchmark_id')} version={data.get('version')}")
    print(f"cases={len(cases)} categories={len(cats)} languages={langs}")
    if summary:
        from collections import Counter

        print("strategies:", dict(Counter(c["expected_strategy"] for c in cases)))
        print("eval_modes:", dict(Counter(c["evaluation_mode"] for c in cases)))
        print("categories:", ", ".join(cats))
    print(
        "NOTE: Structural validation is not answer-quality evaluation. "
        "All reasoning cases remain NOT_TESTED until reviewed."
    )
    return 0


def run_live(
    corpus_path: Path,
    base_url: str,
    case_id: str | None,
    limit: int,
    timeout: float,
    delay: float,
    out_path: Path | None,
) -> int:
    data = load_corpus(corpus_path)
    problems = validate_corpus(data)
    if problems:
        print("Corpus invalid; refusing live run:")
        for p in problems:
            print(" -", p)
        return 2

    token = os.getenv("OMARAI_ACCESS_TOKEN", "").strip() or None
    cases = data["cases"]
    if case_id:
        cases = [c for c in cases if c["case_id"] == case_id]
        if not cases:
            print(f"Unknown case_id: {case_id}", file=sys.stderr)
            return 2
    if limit > 0:
        cases = cases[:limit]

    results = []
    print(
        "LIVE mode: fixtures are NOT injected into the server. "
        "Answers are recorded as NOT_TESTED (quality) unless transport fails."
    )
    for case in cases:
        cid = case["case_id"]
        prompt = case["question"]
        status_code, payload = post_agent(base_url, prompt, timeout, token)
        if isinstance(payload, dict):
            safe_payload = json.loads(redact_secrets(json.dumps(payload, ensure_ascii=False)))
        else:
            safe_payload = redact_secrets(str(payload))

        transport_ok = 200 <= status_code < 300
        record = {
            "case_id": cid,
            "benchmark_version": data.get("version"),
            "benchmark_id": data.get("benchmark_id"),
            "executed_at_utc": _utc_now(),
            "mode": "live_api",
            "base_url": base_url,
            "http_status": status_code,
            "prompt": prompt,
            "expected_strategy": case["expected_strategy"],
            "category": case["category"],
            "response": safe_payload,
            "used_web_search": (
                safe_payload.get("used_web_search") if isinstance(safe_payload, dict) else None
            ),
            "used_language_model": (
                safe_payload.get("used_language_model")
                if isinstance(safe_payload, dict)
                else None
            ),
            "sources": (
                safe_payload.get("sources") if isinstance(safe_payload, dict) else None
            ),
            "status": "NOT_TESTED",
            "transport_ok": transport_ok,
            "reviewer_notes": (
                "Response collected; human/fixture review required for PASS/FAIL."
                if transport_ok
                else "Transport or HTTP error; quality not graded."
            ),
            "evidence_fixture_injected": False,
        }
        results.append(record)
        flag = "OK" if transport_ok else "ERR"
        print(f"[{flag}] {cid} http={status_code}")
        if delay > 0:
            time.sleep(delay)

    envelope = {
        "benchmark_id": data.get("benchmark_id"),
        "benchmark_version": data.get("version"),
        "mode": "live_api",
        "executed_at_utc": _utc_now(),
        "case_count": len(results),
        "results": results,
        "disclaimer": (
            "status=NOT_TESTED means answer quality was not auto-graded. "
            "Fixtures in JSON were not applied to the live server."
        ),
    }
    text = json.dumps(envelope, ensure_ascii=False, indent=2)
    if out_path:
        out_path.write_text(text + "\n", encoding="utf-8")
        print(f"Wrote {out_path}")
    else:
        print(text)
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Omarai answer-quality benchmark runner")
    parser.add_argument(
        "--mode",
        choices=("validate", "live"),
        default="validate",
        help="validate=offline corpus check (default); live=opt-in API calls",
    )
    parser.add_argument(
        "--corpus",
        type=Path,
        default=DEFAULT_CORPUS,
        help="Path to answer_quality_cases.json",
    )
    parser.add_argument("--summary", action="store_true", help="Extra validate summary")
    parser.add_argument("--base-url", default="http://127.0.0.1:8765")
    parser.add_argument("--case-id", default=None, help="Run a single case (live)")
    parser.add_argument("--limit", type=int, default=0, help="Max cases in live mode (0=all selected)")
    parser.add_argument("--timeout", type=float, default=60.0)
    parser.add_argument("--delay", type=float, default=0.0, help="Seconds between live requests")
    parser.add_argument("--out", type=Path, default=None, help="Write live results JSON")
    args = parser.parse_args(argv)

    if args.mode == "validate":
        return run_validate(args.corpus, args.summary)
    if args.mode == "live":
        if not args.case_id and args.limit <= 0:
            print(
                "Refusing unbounded live run. Pass --case-id and/or --limit > 0.",
                file=sys.stderr,
            )
            return 2
        return run_live(
            args.corpus,
            args.base_url,
            args.case_id,
            args.limit,
            args.timeout,
            args.delay,
            args.out,
        )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
