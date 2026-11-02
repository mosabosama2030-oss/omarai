#!/usr/bin/env python3
"""End-to-end smoke test for a deployed Omarai instance; uses only stdlib."""
from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path
import sys
import urllib.error
import urllib.parse
import urllib.request
from typing import Any


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


def _safe_response_metadata(headers: Any, body_size: int) -> dict[str, Any]:
    """Keep only non-secret response metadata useful for diagnosing edge rejections."""
    headers = headers or {}
    request_id = headers.get("X-Request-ID") or headers.get("CF-Ray")
    server = headers.get("Server")
    content_type = headers.get("Content-Type")
    safe_id = (
        request_id.strip()[:128]
        if isinstance(request_id, str)
        and re.fullmatch(r"[A-Za-z0-9._:-]{1,128}", request_id.strip())
        else None
    )
    safe_server = (
        server.strip()[:80]
        if isinstance(server, str)
        and re.fullmatch(r"[A-Za-z0-9._-]{1,80}", server.strip())
        else None
    )
    safe_content_type = (
        content_type.split(";", 1)[0].strip().lower()[:80]
        if isinstance(content_type, str)
        and re.fullmatch(r"[A-Za-z0-9.+-]+/[A-Za-z0-9.+-]+(?:;.*)?", content_type.strip())
        else None
    )
    return {
        "request_id": safe_id,
        "server": safe_server,
        "content_type": safe_content_type,
        "body_bytes": max(0, int(body_size)),
    }


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
    response_metadata: dict[str, Any] | None = None
    try:
        opener = urllib.request.build_opener(_SameOriginRedirectHandler())
        with opener.open(request, timeout=timeout) as response:
            status, body = response.status, response.read(1_000_000)
            response_headers = response.headers
    except urllib.error.HTTPError as exc:
        status = exc.code
        body = exc.read(100_000)
        response_headers = exc.headers
        response_metadata = _safe_response_metadata(response_headers, len(body))
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        path = urllib.parse.urlsplit(url).path
        raise SmokeError(
            f"Network request failed at {path} ({type(exc).__name__}); check the service and network."
        ) from exc
    try:
        result = json.loads(body.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        result = None
    if status >= 400:
        if not isinstance(result, dict):
            result = {}
        result["_http_diagnostics"] = response_metadata or _safe_response_metadata(
            response_headers, len(body)
        )
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
) -> dict[str, Any]:
    origin = normalize_origin(origin, allow_http or local_dev_no_token)
    target_host = urllib.parse.urlsplit(origin).hostname or ""
    loopback_host = target_host.lower() in {"localhost", "127.0.0.1", "::1"}
    if expected_sha is not None and not re.fullmatch(r"[0-9a-fA-F]{40}", expected_sha.strip()):
        raise SmokeError("The expected source revision must be a full 40-character Git SHA.")
    if token.strip():
        if len(token.strip()) < 32:
            raise SmokeError("OMARAI_ACCESS_TOKEN is shorter than 32 characters.")
    elif not (local_dev_no_token and loopback_host):
        raise SmokeError(
            "OMARAI_ACCESS_TOKEN is required for hosted targets. No-token mode is restricted to localhost/loopback."
        )

    if not allow_provider_usage:
        raise SmokeError(
            "This acceptance test performs one owner-only agent request capped at 2 search queries, "
            "8 provider calls, 3 model calls, and 2 page fetches; provider quota or charges may be consumed. "
            "Pass --allow-provider-usage only after explicit human approval."
        )

    auth_mode = "bearer_token" if token.strip() else "local_loopback_dev_bypass"
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
        if isinstance(health, dict) and isinstance(health.get("_http_diagnostics"), dict):
            partial_report["last_http_error"] = {
                "path": "/api/health",
                **health["_http_diagnostics"],
            }
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

    if token.strip():
        status, _ = request_json(
            f"{origin}/api/agent", payload={"question": "اختبار رفض الوصول غير المصرح به"},
            timeout=min(timeout, 20),
        )
        if status != 401:
            raise SmokeError(
                f"Unauthenticated POST /api/agent should return 401, received {status}.",
                partial_report,
            )
        checks["authentication"] = "passed"
    else:
        checks["authentication"] = "local_loopback_dev_bypass"

    # One authenticated agent request performs the bounded live search and model work.
    status, answer = request_json(
        f"{origin}/api/agent", token=token, timeout=timeout,
        payload={
            "question": LIVE_TEST_QUESTION,
            "history": [],
            "mode": "auto",
            "execution_profile": "hosted_smoke",
            "allow_provider_usage": True,
        },
    )
    if status != 200 or not answer:
        if isinstance(answer, dict) and isinstance(answer.get("_http_diagnostics"), dict):
            partial_report["last_http_error"] = {
                "path": "/api/agent",
                **answer["_http_diagnostics"],
            }
        raise SmokeError(f"Authenticated agent request failed (HTTP {status}).", partial_report)
    sources = answer.get("sources")
    usable = [
        item for item in sources if isinstance(item, dict)
        and isinstance(item.get("url"), str)
        and urllib.parse.urlsplit(item["url"]).scheme in {"http", "https"}
        and urllib.parse.urlsplit(item["url"]).hostname
    ] if isinstance(sources, list) else []
    search_report = answer.get("search_report")
    answer_text = str(answer.get("answer", "")).strip()
    request_budget = answer.get("request_budget")
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
        "request_budget": request_budget,
    }
    partial_report["transcript"] = [transcript]
    if not answer_text:
        raise SmokeError("Agent request returned an empty answer.", partial_report)
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
    if not isinstance(search_report, dict):
        raise SmokeError("Agent request omitted its structured search report.", partial_report)
    if search_report.get("search_outcome") != "attempted_with_usable_sources":
        raise SmokeError("Agent search outcome was not completed with usable sources.", partial_report)
    if search_report.get("pipeline_completion_status") != "completed":
        raise SmokeError("Agent research pipeline did not complete successfully.", partial_report)
    if answer.get("answer_evidence_status") != "citation_indices_validated_only":
        raise SmokeError("Agent answer did not pass citation-index validation.", partial_report)
    if not isinstance(request_budget, dict):
        raise SmokeError("Agent request omitted its resource-budget report.", partial_report)
    budget_limits = request_budget.get("limits")
    budget_counts = request_budget.get("counts")
    expected_budget_limits = {
        "search_queries": 2,
        "search_calls": 8,
        "model_calls": 3,
        "page_fetches": 2,
        "tool_calls": 0,
    }
    if not isinstance(budget_limits, dict) or not isinstance(budget_counts, dict):
        raise SmokeError("Agent request budget report is incomplete.", partial_report)
    for resource, maximum in expected_budget_limits.items():
        limit = budget_limits.get(resource)
        count = budget_counts.get(resource)
        if (
            isinstance(limit, bool) or not isinstance(limit, int)
            or limit > maximum or limit < 0
            or isinstance(count, bool) or not isinstance(count, int)
            or count < 0 or count > limit
        ):
            raise SmokeError(f"Agent request exceeded or misreported its {resource} budget.", partial_report)
    checks["live_search"] = {
        "status": "passed",
        "search_outcome": search_report.get("search_outcome"),
        "source_count": len(usable),
        "providers_reported": search_report.get("providers_used", []),
    }
    checks["language_model"] = {
        "status": "passed",
        "response_received": True,
        "verified_by": "agent_request",
    }
    checks["agent_request"] = {
        "status": "passed",
        "source_count": len(usable),
        "direct_pages_read": search_report.get("pages_fetched"),
        "providers_reported": search_report.get("providers_used", []),
        "answer_received": True,
        "pipeline_completion_status": search_report.get("pipeline_completion_status"),
        "answer_evidence_status": answer.get("answer_evidence_status"),
        "request_budget": request_budget,
    }
    partial_report.update({
        "result": "passed",
        "checks": checks,
        "request_budget": request_budget,
        "note": (
            "One owner-authorized agent request was executed under a fixed per-request budget "
            "(2 search queries, 8 provider calls, 3 model calls, 2 page fetches, 0 tool calls). "
            "This confirms the request path at test time, not continuous uptime or factual correctness."
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
        help="Explicitly authorize one hosted-smoke agent request with fixed per-request search/model/page limits; provider quota or charges may be consumed.",
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
