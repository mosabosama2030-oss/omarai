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
import ipaddress
import json
import math
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CORPUS = ROOT / "tests" / "fixtures" / "answer_quality_cases.json"
MAX_RESPONSE_BYTES = 2_000_000


def _load_request_cost_ledger(path: Path | None, valid_case_ids: set[str]) -> tuple[dict[str, float], str | None]:
    """Load reconciled, externally sourced whole-request USD costs; never estimate them."""
    if path is None:
        return {}, None
    ledger = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(ledger, dict):
        raise ValueError("request-cost ledger root must be an object")
    if ledger.get("currency") != "USD" or ledger.get("scope") != "complete_request":
        raise ValueError("request-cost ledger must declare currency=USD and scope=complete_request")
    source = ledger.get("source")
    if not isinstance(source, str) or not source.strip():
        raise ValueError("request-cost ledger needs a non-empty source describing the reconciliation")
    entries = ledger.get("costs")
    if not isinstance(entries, list):
        raise ValueError("request-cost ledger must contain a costs array")
    costs: dict[str, float] = {}
    for index, entry in enumerate(entries):
        if not isinstance(entry, dict):
            raise ValueError(f"request-cost ledger costs[{index}] must be an object")
        case_id = entry.get("case_id")
        if not isinstance(case_id, str) or case_id not in valid_case_ids:
            raise ValueError(f"request-cost ledger costs[{index}] has an unknown case_id")
        if case_id in costs:
            raise ValueError(f"request-cost ledger has duplicate case_id {case_id}")
        value = _finite_nonnegative_number(entry.get("cost_usd"))
        if value is None:
            raise ValueError(f"request-cost ledger {case_id} cost_usd must be finite and non-negative")
        costs[case_id] = value
    return costs, source.strip()


def _model_calls_from_payload(payload: dict) -> list[dict]:
    """Read only structured per-request model-call metadata from an API response."""
    report = payload.get("search_report")
    understanding = payload.get("task_understanding")
    candidates = [
        payload.get("model_calls"),
        report.get("model_calls") if isinstance(report, dict) else None,
        understanding.get("model_calls") if isinstance(understanding, dict) else None,
    ]
    for candidate in candidates:
        if isinstance(candidate, list) and candidate:
            return [item for item in candidate if isinstance(item, dict)]
    return []


def _finite_nonnegative_number(value) -> float | None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    number = float(value)
    if not math.isfinite(number) or number < 0:
        return None
    return number


def _response_metrics(payload: dict | str, expected_strategy: str, transport_ok: bool) -> dict:
    """Derive conservative telemetry; never infer semantic correctness from HTTP 200."""
    if not isinstance(payload, dict):
        payload = {}
    report = payload.get("search_report")
    report = report if isinstance(report, dict) else {}
    outcome = report.get("search_outcome")
    pipeline = report.get("pipeline_completion_status")
    if expected_strategy != "web_search":
        tool_status = "NOT_APPLICABLE"
    elif not transport_ok:
        tool_status = "TRANSPORT_FAILED"
    elif outcome == "attempted_with_usable_sources":
        tool_status = "SUCCESS_WITH_USABLE_RESULTS"
    elif outcome == "attempted_no_usable_sources":
        tool_status = "ATTEMPTED_NO_USABLE_RESULTS"
    elif outcome == "attempted_research_error":
        tool_status = "TOOL_FAILED"
    elif outcome == "unknown_after_budget_exhaustion":
        tool_status = "BUDGET_EXHAUSTED"
    elif outcome == "not_attempted":
        tool_status = "NOT_ATTEMPTED"
    else:
        tool_status = "UNKNOWN"

    calls = _model_calls_from_payload(payload)
    reported_costs = []
    for call in calls:
        usage = call.get("provider_usage")
        if not isinstance(usage, dict):
            continue
        cost = _finite_nonnegative_number(usage.get("cost_usd"))
        if cost is not None:
            reported_costs.append(cost)

    if not calls:
        cost_status = "NO_MODEL_CALL_METADATA"
    elif len(reported_costs) == len(calls):
        cost_status = "COMPLETE_FOR_RETURNED_MODEL_CALLS"
    elif reported_costs:
        cost_status = "PARTIAL_PROVIDER_REPORTED_MODEL_COST"
    else:
        cost_status = "PROVIDER_COST_NOT_REPORTED"

    return {
        "search_outcome": outcome if isinstance(outcome, str) else "unknown",
        "pipeline_completion_status": pipeline if isinstance(pipeline, str) else "unknown",
        "tool_status": tool_status,
        "source_count": len(payload.get("sources", [])) if isinstance(payload.get("sources"), list) else None,
        "model_call_count": len(calls),
        "provider_reported_model_cost_usd": round(sum(reported_costs), 10) if reported_costs else None,
        "provider_reported_model_cost_call_count": len(reported_costs),
        "provider_reported_model_cost_status": cost_status,
        "request_cost_usd": None,
        "request_cost_status": "NOT_MEASURED_TOTAL_CONNECTOR_COSTS_NOT_EXPOSED",
    }


def validate_base_url(base_url: str, *, token_present: bool = False) -> str:
    """Validate and normalize an API origin before any request can carry a token."""
    if not isinstance(base_url, str) or not base_url.strip():
        raise ValueError("Base URL must be a non-empty HTTP(S) origin.")
    try:
        parsed = urllib.parse.urlsplit(base_url.strip())
        scheme = parsed.scheme.lower()
        host = (parsed.hostname or "").lower().rstrip(".")
        port = parsed.port
    except ValueError as exc:
        raise ValueError("Base URL is malformed.") from exc

    if scheme not in {"http", "https"} or not host:
        raise ValueError("Base URL must use HTTP or HTTPS and include a hostname.")
    if parsed.username is not None or parsed.password is not None:
        raise ValueError("Base URL must not include a username or password.")
    if parsed.path not in {"", "/"} or parsed.query or parsed.fragment:
        raise ValueError("Base URL must contain only the origin, without path, query, or fragment.")

    loopback = host == "localhost"
    try:
        loopback = ipaddress.ip_address(host).is_loopback
    except ValueError:
        pass

    if scheme == "http" and not loopback:
        raise ValueError("Plain HTTP is allowed only for localhost or a loopback IP.")

    if (scheme == "https" and port == 443) or (scheme == "http" and port == 80):
        port = None
    host_for_origin = f"[{host}]" if ":" in host else host
    origin = f"{scheme}://{host_for_origin}" + (f":{port}" if port is not None else "")

    if token_present and not loopback:
        allowed = os.getenv("OMARAI_BENCHMARK_ALLOWED_ORIGIN", "").strip()
        if not allowed:
            raise ValueError(
                "A bearer token requires OMARAI_BENCHMARK_ALLOWED_ORIGIN to match "
                "the exact HTTPS deployment origin."
            )
        allowed_origin = validate_base_url(allowed, token_present=False)
        if allowed_origin != origin:
            raise ValueError(
                "Refusing to send the bearer token: base URL does not match "
                "OMARAI_BENCHMARK_ALLOWED_ORIGIN."
            )
    return origin


class _NoRedirectHandler(urllib.request.HTTPRedirectHandler):
    """Do not follow redirects; the bearer token must never move to another origin."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


_NO_REDIRECT_OPENER = urllib.request.build_opener(_NoRedirectHandler())

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
    origin = validate_base_url(base_url, token_present=bool(token))
    url = origin + "/api/agent"
    body = json.dumps({"question": question, "history": []}, ensure_ascii=False).encode("utf-8")
    headers = {"Content-Type": "application/json", "Content-Length": str(len(body))}
    if token:
        headers["Authorization"] = "Bearer " + token
    req = urllib.request.Request(url, data=body, headers=headers, method="POST")
    try:
        with _NO_REDIRECT_OPENER.open(req, timeout=timeout) as resp:
            raw_bytes = resp.read(MAX_RESPONSE_BYTES + 1)
            if len(raw_bytes) > MAX_RESPONSE_BYTES:
                return 0, {"error": "ResponseTooLarge", "detail": "Response exceeded the 2 MB limit."}
            raw = raw_bytes.decode("utf-8", errors="replace")
            status = getattr(resp, "status", 200)
            try:
                return status, json.loads(raw)
            except json.JSONDecodeError:
                return status, raw
    except urllib.error.HTTPError as exc:
        raw_bytes = exc.read(MAX_RESPONSE_BYTES + 1)
        if len(raw_bytes) > MAX_RESPONSE_BYTES:
            return exc.code, {"error": "ResponseTooLarge", "detail": "Response exceeded the 2 MB limit."}
        raw = raw_bytes.decode("utf-8", errors="replace")
        try:
            return exc.code, json.loads(raw)
        except json.JSONDecodeError:
            return exc.code, raw
    except ValueError as exc:
        return 0, {"error": "UnsafeBaseURL", "detail": str(exc)}
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return 0, {"error": type(exc).__name__, "detail": str(exc)}


def get_verified_build_sha(base_url: str, timeout: float, token: str | None = None) -> str:
    """Read the deployed build identity from /api/health; never trust a caller-only SHA."""
    origin = validate_base_url(base_url, token_present=bool(token))
    request = urllib.request.Request(
        origin + "/api/health",
        headers={"Accept": "application/json"},
        method="GET",
    )
    try:
        with _NO_REDIRECT_OPENER.open(request, timeout=timeout) as response:
            raw = response.read(64_001)
            if len(raw) > 64_000:
                raise ValueError("/api/health response exceeded the 64 KB limit")
            status = getattr(response, "status", 200)
            if not 200 <= status < 300:
                raise ValueError(f"/api/health returned HTTP {status}")
    except urllib.error.HTTPError as exc:
        raise ValueError(f"/api/health returned HTTP {exc.code}") from exc
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        raise ValueError(f"/api/health request failed: {type(exc).__name__}") from exc

    try:
        payload = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError("/api/health did not return valid JSON") from exc
    if not isinstance(payload, dict) or payload.get("ok") is not True:
        raise ValueError("/api/health did not report ok=true")
    build = payload.get("build")
    sha = build.get("sha") if isinstance(build, dict) else None
    if not isinstance(sha, str) or not re.fullmatch(r"[0-9a-fA-F]{40}", sha):
        raise ValueError("/api/health build.sha is missing or not a full 40-character SHA")
    return sha.lower()


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
    build_sha: str | None = None,
    request_costs_path: Path | None = None,
) -> int:
    data = load_corpus(corpus_path)
    problems = validate_corpus(data)
    if problems:
        print("Corpus invalid; refusing live run:")
        for p in problems:
            print(" -", p)
        return 2

    try:
        full_case_ids = {case.get("case_id") for case in data.get("cases", []) if isinstance(case, dict)}
        request_costs, request_cost_source = _load_request_cost_ledger(request_costs_path, full_case_ids)
    except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
        print(f"Invalid request-cost ledger; refusing live run: {exc}", file=sys.stderr)
        return 2

    token = os.getenv("OMARAI_ACCESS_TOKEN", "").strip() or None
    try:
        safe_base_url = validate_base_url(base_url, token_present=bool(token))
    except ValueError as exc:
        print(f"Unsafe base URL; refusing live run: {exc}", file=sys.stderr)
        return 2
    try:
        verified_build_sha = get_verified_build_sha(safe_base_url, timeout, token)
    except ValueError as exc:
        print(f"Unverified deployed build; refusing live run: {exc}", file=sys.stderr)
        return 2
    expected_build_sha = build_sha.strip().lower() if isinstance(build_sha, str) else ""
    if expected_build_sha and expected_build_sha != verified_build_sha:
        print(
            "Build SHA mismatch: --build-sha does not match /api/health build.sha; "
            "refusing live requests.",
            file=sys.stderr,
        )
        return 2
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
        request_started = time.perf_counter()
        status_code, payload = post_agent(safe_base_url, prompt, timeout, token)
        elapsed_ms = round((time.perf_counter() - request_started) * 1000, 2)
        if isinstance(payload, dict):
            safe_payload = json.loads(redact_secrets(json.dumps(payload, ensure_ascii=False)))
        else:
            safe_payload = redact_secrets(str(payload))

        transport_ok = 200 <= status_code < 300
        response_metrics = _response_metrics(safe_payload, case["expected_strategy"], transport_ok)
        if request_cost_source is not None:
            if cid in request_costs:
                response_metrics["request_cost_usd"] = request_costs[cid]
                response_metrics["request_cost_status"] = "RECONCILED_COMPLETE_REQUEST_COST"
                response_metrics["request_cost_source"] = request_cost_source
            else:
                response_metrics["request_cost_status"] = "PARTIAL_EXTERNAL_COST_RECONCILIATION"
                response_metrics["request_cost_source"] = request_cost_source
        record = {
            "case_id": cid,
            "benchmark_version": data.get("version"),
            "benchmark_id": data.get("benchmark_id"),
            "executed_at_utc": _utc_now(),
            "mode": "live_api",
            "base_url": safe_base_url,
            "http_status": status_code,
            "elapsed_ms": elapsed_ms,
            "build_sha": verified_build_sha,
            "build_sha_verification": "confirmed_by_api_health",
            **response_metrics,
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
        "build_sha": verified_build_sha,
        "build_sha_verification": "confirmed_by_api_health",
        "expected_build_sha": expected_build_sha or None,
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
    parser.add_argument("--build-sha", default=None, help="Optional expected deployed SHA; checked against /api/health before any benchmark request")
    parser.add_argument("--request-costs", type=Path, default=None, help="Optional externally reconciled per-case full-request costs in USD")
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
            args.build_sha,
            args.request_costs,
        )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
