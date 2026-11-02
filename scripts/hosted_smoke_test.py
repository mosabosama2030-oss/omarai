#!/usr/bin/env python3
"""End-to-end smoke test for a deployed Omarai instance; uses only stdlib."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
from pathlib import Path
import sys
import urllib.error
import urllib.parse
import urllib.request
from typing import Any


HOSTED_SMOKE_BUDGET_MAX = {
    "search_queries": 3,
    "search_calls": 12,
    "model_calls": 6,
    "page_fetches": 4,
    "tool_calls": 0,
}

LIVE_TEST_QUESTION = (
    "اختبار اكتساب عملاء: ابحث عن طلبات شراء أو مناقصات منشورة وحديثة في مصر تخص "
    "أنظمة إنذار الحريق. لا تعتبر شركة عميلاً محتملاً إلا إذا وجدت إشارة شراء صريحة "
    "أو طلب عرض سعر منشورًا. اعرض لكل إشارة المصدر والرابط والتاريخ ومقتطف الدليل، "
    "وصرّح بوضوح إذا لم تجد طلبًا مؤكدًا."
)


class SmokeError(RuntimeError):
    """A live acceptance check failed, optionally carrying a safe partial report."""

    def __init__(self, message: str, report: dict[str, Any] | None = None):
        super().__init__(message)
        self.report = report or {}


class _SameOriginRedirectHandler(urllib.request.HTTPRedirectHandler):
    """Never forward a bearer token to a different origin during an HTTP redirect."""

    @staticmethod
    def _origin(url: str) -> tuple[str, str, int | None]:
        parsed = urllib.parse.urlsplit(url)
        try:
            port = parsed.port
        except ValueError:
            return "", "", None
        if port is None:
            port = 443 if parsed.scheme.lower() == "https" else 80 if parsed.scheme.lower() == "http" else None
        return parsed.scheme.lower(), (parsed.hostname or "").lower(), port

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        target_url = urllib.parse.urljoin(req.full_url, newurl)
        target = urllib.parse.urlsplit(target_url)
        if (
            self._origin(req.full_url) != self._origin(target_url)
            or target.scheme.lower() not in {"http", "https"}
            or target.username
            or target.password
        ):
            raise urllib.error.HTTPError(
                req.full_url, code, "Cross-origin redirect blocked", headers, fp
            )
        return super().redirect_request(req, fp, code, msg, headers, target_url)


def normalize_origin(value: str, allow_http: bool = False) -> str:
    parsed = urllib.parse.urlsplit((value or "").strip())
    if parsed.scheme not in {"https", "http"} or not parsed.hostname:
        raise SmokeError("Provide an absolute HTTPS origin, for example https://your-app.example.com.")
    if parsed.username or parsed.password or parsed.query or parsed.fragment:
        raise SmokeError("The base URL must not contain credentials, a query, or a fragment.")
    if parsed.path not in {"", "/"}:
        raise SmokeError("The base URL must be an origin only; do not add /api or another path.")
    if parsed.scheme != "https" and not (
        allow_http and parsed.hostname.lower() in {"localhost", "127.0.0.1", "::1"}
    ):
        raise SmokeError("Hosted tests require HTTPS; plain HTTP is allowed only for local tests.")
    try:
        port = parsed.port
    except ValueError as exc:
        raise SmokeError("Invalid port in base URL.") from exc
    host = parsed.hostname
    if ":" in host and not host.startswith("["):
        host = f"[{host}]"
    if port:
        host += f":{port}"
    return f"{parsed.scheme}://{host}"


def request_json(url: str, *, token: str = "", payload: dict[str, Any] | None = None,
                 timeout: float = 90) -> tuple[int, dict[str, Any] | None]:
    headers = {"Accept": "application/json"}
    data = None
    if payload is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(payload, ensure_ascii=False).encode()
    if token:
        headers["Authorization"] = "Bearer " + token
    request = urllib.request.Request(url, data=data, headers=headers)
    try:
        opener = urllib.request.build_opener(_SameOriginRedirectHandler())
        with opener.open(request, timeout=timeout) as response:
            status, body = response.status, response.read(1_000_000)
    except urllib.error.HTTPError as exc:
        status = exc.code
        body = exc.read(100_000)
        if status >= 400:
            response_headers = exc.headers or {}
            metadata = {
                "status": status,
                "content_type": response_headers.get("Content-Type", "")[:160],
                "server": response_headers.get("Server", "")[:120],
                "request_id": response_headers.get("X-Request-ID", "")[:160],
                "correlation_id": response_headers.get("X-Correlation-ID", "")[:160],
                "cf_ray": response_headers.get("CF-Ray", "")[:160],
                "via": response_headers.get("Via", "")[:160],
                "body_bytes_sampled": len(body),
                "body_sha256": hashlib.sha256(body).hexdigest(),
            }
            # Never retain the response body: gateways can echo request data or secrets.
            return status, {"_smoke_http": metadata}
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        path = urllib.parse.urlsplit(url).path
        raise SmokeError(f"Network request failed at {path}; check the service and network.") from exc
    try:
        result = json.loads(body.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        result = None
    return status, result if isinstance(result, dict) else None


def run_smoke(
    origin: str,
    token: str,
    *,
    timeout: float = 90,
    allow_http: bool = False,
    expected_sha: str | None = None,
    local_dev_no_token: bool = False,
    allow_provider_usage: bool = False,
    preflight_only: bool = False,
) -> dict[str, Any]:
    origin = normalize_origin(origin, allow_http or local_dev_no_token)
    target_host = urllib.parse.urlsplit(origin).hostname or ""
    loopback_host = target_host.lower() in {"localhost", "127.0.0.1", "::1"}
    if expected_sha is not None and not re.fullmatch(r"[0-9a-fA-F]{40}", expected_sha.strip()):
        raise SmokeError("The expected source revision must be a full 40-character Git SHA.")
    if local_dev_no_token and not loopback_host:
        raise SmokeError("No-token development mode is restricted to localhost/loopback.")
    if token.strip():
        if len(token.strip()) < 32:
            raise SmokeError("OMARAI_ACCESS_TOKEN is shorter than 32 characters.")
    elif not (local_dev_no_token and loopback_host) and not preflight_only:
        raise SmokeError(
            "OMARAI_ACCESS_TOKEN is required for live hosted acceptance; no-cost preflight may run without it."
        )

    if preflight_only and allow_provider_usage:
        raise SmokeError("--preflight-only cannot be combined with --allow-provider-usage.")

    auth_mode = (
        "bearer_token" if token.strip()
        else "local_loopback_dev_bypass" if local_dev_no_token and loopback_host
        else "preflight_no_token"
    )
    checks: dict[str, Any] = {}
    partial_report: dict[str, Any] = {
        "result": "running",
        "target_host": target_host,
        "auth_mode": auth_mode,
        "checks": checks,
        "transcript": [],
    }
    status, health = request_json(f"{origin}/api/health", timeout=min(timeout, 20))
    if status != 200 or not health or health.get("ok") is not True:
        if isinstance(health, dict) and isinstance(health.get("_smoke_http"), dict):
            partial_report["http_response"] = health["_smoke_http"]
        raise SmokeError(f"Health check failed (HTTP {status}).", partial_report)
    checks["health"] = "passed"

    build = health.get("build")
    reported_sha = build.get("sha") if isinstance(build, dict) else None
    if expected_sha is not None:
        expected = expected_sha.strip().lower()
        if not isinstance(reported_sha, str) or reported_sha.lower() != expected:
            raise SmokeError(
                "The deployed service SHA does not match the expected Git commit. "
                "Pass OMARAI_BUILD_SHA as a Docker build argument for the deployed revision, "
                "then rebuild and redeploy.",
                partial_report,
            )
        checks["build_identity"] = {
            "status": "passed",
            "expected_sha": expected,
            "reported_sha": reported_sha.lower(),
        }
    else:
        checks["build_identity"] = {
            "status": "not_checked",
            "reported_sha": reported_sha if isinstance(reported_sha, str) else "unknown",
        }

    if token.strip() or (preflight_only and not local_dev_no_token):
        status, auth_response = request_json(
            f"{origin}/api/agent", payload={"question": ""},
            timeout=min(timeout, 20),
        )
        if status != 401:
            if isinstance(auth_response, dict) and isinstance(auth_response.get("_smoke_http"), dict):
                partial_report["http_response"] = auth_response["_smoke_http"]
            raise SmokeError(
                f"Unauthenticated POST /api/agent should return 401, received {status}.",
                partial_report,
            )
        checks["authentication"] = "passed"
    else:
        checks["authentication"] = "local_loopback_dev_bypass"

    if preflight_only:
        checks["provider_usage"] = {"status": "skipped_not_approved"}
        partial_report.update({
            "result": "preflight_passed",
            "checks": checks,
            "note": (
                "No-cost preflight only: health, build identity (when requested), and authentication "
                "were checked. No search provider or language model was called."
            ),
        })
        return partial_report

    if not allow_provider_usage:
        checks["provider_usage"] = {"status": "blocked_not_approved"}
        raise SmokeError(
            "No-cost preflight passed, but live search/model usage was not approved. "
            "Re-run with --allow-provider-usage only after explicit human approval.",
            partial_report,
        )

    checks["provider_usage"] = {
        "status": "approved",
        "scope": {
            "profile": "hosted_smoke",
            "max_search_queries": HOSTED_SMOKE_BUDGET_MAX["search_queries"],
            "max_provider_requests": HOSTED_SMOKE_BUDGET_MAX["search_calls"],
            "max_model_calls": HOSTED_SMOKE_BUDGET_MAX["model_calls"],
            "max_page_fetches": HOSTED_SMOKE_BUDGET_MAX["page_fetches"],
            "tool_calls": HOSTED_SMOKE_BUDGET_MAX["tool_calls"],
            "note": "Server-enforced per-request ceilings; operator settings may be stricter.",
        },
    }
    status, answer = request_json(
        f"{origin}/api/agent", token=token, timeout=timeout,
        payload={
            "question": LIVE_TEST_QUESTION,
            "history": [], "mode": "auto", "request_profile": "hosted_smoke",
        },
    )
    if status != 200 or not answer:
        if isinstance(answer, dict) and isinstance(answer.get("_smoke_http"), dict):
            partial_report["http_response"] = answer["_smoke_http"]
        raise SmokeError(f"Authenticated agent request failed (HTTP {status}).", partial_report)
    sources = answer.get("sources")
    usable = [
        item for item in sources if isinstance(item, dict)
        and isinstance(item.get("url"), str)
        and urllib.parse.urlsplit(item["url"]).scheme in {"http", "https"}
        and urllib.parse.urlsplit(item["url"]).hostname
    ] if isinstance(sources, list) else []
    search_report = answer.get("search_report")
    raw_answer = answer.get("answer")
    answer_text = raw_answer.strip() if isinstance(raw_answer, str) else ""
    source_records = [
        {
            "title": str(item.get("title") or "")[:300],
            "url": str(item.get("url") or "")[:2048],
            "provider": str(item.get("provider") or "")[:80],
            "snippet": str(item.get("snippet") or "")[:1200],
            "published_at": str(item.get("published_at") or "")[:100],
        }
        for item in usable
    ]
    transcript = {
        "case_id": "sales_intent_fire_alarm_egypt",
        "question": LIVE_TEST_QUESTION,
        "answer": answer_text,
        "used_web_search": answer.get("used_web_search") is True,
        "used_language_model": answer.get("used_language_model") is True,
        "sources": source_records,
        "pipeline_completion_status": (
            search_report.get("pipeline_completion_status")
            if isinstance(search_report, dict) else None
        ),
        "answer_evidence_status": answer.get("answer_evidence_status"),
        "semantic_claim_verification_status": (
            search_report.get("semantic_claim_verification", {}).get("status")
            if isinstance(search_report, dict)
            and isinstance(search_report.get("semantic_claim_verification"), dict)
            else None
        ),
        "request_budget": answer.get("request_budget"),
    }
    partial_report["transcript"] = [transcript]
    if not answer_text:
        raise SmokeError("Agent request returned an empty or whitespace-only answer.", partial_report)
    if answer.get("used_web_search") is not True or not usable:
        raise SmokeError(
            "Agent request did not return a live web search with usable source URLs.",
            partial_report,
        )
    if answer.get("used_language_model") is not True:
        raise SmokeError(
            "Agent request did not confirm that a language model was used.",
            partial_report,
        )
    request_budget = answer.get("request_budget")
    if not isinstance(request_budget, dict) or request_budget.get("profile") != "hosted_smoke":
        raise SmokeError("Agent response did not confirm the hosted_smoke request budget profile.", partial_report)
    budget_limits = request_budget.get("limits")
    budget_counts = request_budget.get("counts")
    if not isinstance(budget_limits, dict) or not isinstance(budget_counts, dict):
        raise SmokeError("Agent response omitted request-budget limits or counters.", partial_report)
    for resource, maximum in HOSTED_SMOKE_BUDGET_MAX.items():
        limit = budget_limits.get(resource)
        count = budget_counts.get(resource)
        if (
            isinstance(limit, bool) or not isinstance(limit, int)
            or isinstance(count, bool) or not isinstance(count, int)
            or limit < 0 or limit > maximum
            or count < 0 or count > limit
        ):
            raise SmokeError(
                f"Agent hosted_smoke request budget is missing, exceeded, or invalid for {resource}.",
                partial_report,
            )
    if (
        budget_counts["search_queries"] < 1
        or budget_counts["search_calls"] < 1
        or budget_counts["model_calls"] < 1
    ):
        raise SmokeError(
            "Agent hosted_smoke request budget counters do not prove search and model work occurred.",
            partial_report,
        )
    budget_timeout = request_budget.get("timeout_seconds")
    if (
        isinstance(budget_timeout, bool)
        or not isinstance(budget_timeout, (int, float))
        or budget_timeout <= 0
        or budget_timeout > 75
        or request_budget.get("budget_exhausted") is not False
        or request_budget.get("deadline_exceeded") is not False
    ):
        raise SmokeError("Agent hosted_smoke request budget was exhausted or exceeded its timeout ceiling.", partial_report)
    checks["request_budget"] = {
        "status": "passed",
        "profile": "hosted_smoke",
        "timeout_seconds": budget_timeout,
        "limits": budget_limits,
        "counts": budget_counts,
        "budget_exhausted": False,
        "deadline_exceeded": False,
    }
    if not isinstance(search_report, dict):
        raise SmokeError("Agent request did not return a structured search report.", partial_report)
    pipeline_status = search_report.get("pipeline_completion_status")
    if pipeline_status != "completed":
        raise SmokeError(
            f"Agent research pipeline did not complete (status: {pipeline_status or 'missing'}).",
            partial_report,
        )
    semantic_verification = search_report.get("semantic_claim_verification")
    semantic_status = (
        semantic_verification.get("status")
        if isinstance(semantic_verification, dict) else None
    )
    if semantic_status not in {
        "completed_all_claims_supported",
        "completed_no_factual_claims",
    }:
        raise SmokeError(
            f"Agent semantic claim-support review did not pass (status: {semantic_status or 'missing'}).",
            partial_report,
        )
    if search_report.get("insufficient_evidence") is not False:
        raise SmokeError("Agent search report flags insufficient evidence or omits that check.", partial_report)
    if search_report.get("claim_audit_semantics") != "distinct_model_assessed_source_support_not_ground_truth":
        raise SmokeError("Agent claim-audit semantics are missing or not the expected source-support assessment.", partial_report)
    evidence_status = answer.get("answer_evidence_status")
    if evidence_status != "citation_indices_validated_only":
        raise SmokeError(
            f"Agent answer evidence status is not acceptable for hosted acceptance (status: {evidence_status or 'missing'}).",
            partial_report,
        )
    checks["search"] = {
        "status": "passed",
        "pages_fetched": search_report.get("pages_fetched", 0),
        "providers_reported": search_report.get("providers_used", []),
        "pipeline_completion_status": pipeline_status,
    }
    checks["semantic_claim_support"] = {
        "status": "passed",
        "verification_status": semantic_status,
        "insufficient_evidence": False,
        "semantics": "model_assessed_source_support_not_ground_truth",
    }
    checks["language_model"] = {
        "status": "passed",
        "response_received": True,
        "verified_by": "agent_request",
    }
    checks["agent_request"] = {
        "status": "passed", "source_count": len(usable),
        "direct_pages_read": search_report.get("pages_fetched"),
        "providers_reported": search_report.get("providers_used", []),
        "answer_received": True,
        "pipeline_completion_status": pipeline_status,
        "answer_evidence_status": evidence_status,
    }
    partial_report.update({
        "result": "passed",
        "checks": checks,
        "note": (
            "Transcript contains the exact fixed test question, answer, and returned source metadata. "
            "This proves the request path worked at test time, not continuous uptime. The approved "
            "live phase makes one authenticated agent request; that request may fan out to multiple "
            "configured search providers. The server enforces at most 3 planned queries, 12 provider requests, "
            "6 model calls, 4 page fetches, and zero external tool calls for this smoke profile; "
            "operator settings may be stricter. Provider usage may incur charges."
        ),
    })
    return partial_report


def main() -> int:
    parser = argparse.ArgumentParser(description="Run live acceptance checks against hosted Omarai.")
    parser.add_argument("--base-url", default=os.getenv("OMARAI_BASE_URL", ""))
    parser.add_argument("--timeout", type=float, default=90)
    parser.add_argument(
        "--expected-sha",
        default=os.getenv("OMARAI_EXPECTED_BUILD_SHA", ""),
        help="Require the deployed image to report this full 40-character source Git SHA.",
    )
    parser.add_argument("--allow-http", action="store_true",
                        help="Allow HTTP only for localhost/127.0.0.1/::1 testing.")
    parser.add_argument(
        "--local-dev-no-token",
        action="store_true",
        help="Use the app's existing no-token development bypass on loopback only; never for hosted URLs.",
    )
    parser.add_argument(
        "--allow-provider-usage",
        action="store_true",
        help=(
            "Explicitly authorize one live agent request under the server-enforced hosted_smoke "
            "budget: up to 3 planned queries, 12 provider requests, 6 model calls, 4 page fetches, "
            "and zero external tool calls. Operator settings may be stricter."
        ),
    )
    parser.add_argument(
        "--preflight-only",
        action="store_true",
        help="Run health/build/authentication checks only; never call search providers or a language model.",
    )
    parser.add_argument(
        "--output",
        default="",
        help="Optional path for a JSON report containing the exact test question, answer, and sources.",
    )
    args = parser.parse_args()
    try:
        result = run_smoke(
            args.base_url,
            os.getenv("OMARAI_ACCESS_TOKEN", "").strip(),
            timeout=max(5, min(args.timeout, 240)),
            allow_http=args.allow_http,
            expected_sha=args.expected_sha or None,
            local_dev_no_token=args.local_dev_no_token,
            allow_provider_usage=args.allow_provider_usage,
            preflight_only=args.preflight_only,
        )
    except SmokeError as exc:
        failed_report = {**exc.report, "result": "failed", "error": str(exc)}
        rendered = json.dumps(failed_report, ensure_ascii=False, indent=2)
        if args.output:
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(rendered + "\n", encoding="utf-8")
        print(rendered)
        return 1
    rendered = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 0


if __name__ == "__main__":
    sys.exit(main())
