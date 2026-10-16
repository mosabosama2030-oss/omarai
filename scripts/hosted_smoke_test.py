#!/usr/bin/env python3
"""End-to-end smoke test for a deployed Omarai instance; uses only stdlib."""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from typing import Any


class SmokeError(RuntimeError):
    """A live acceptance check failed."""


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
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        path = urllib.parse.urlsplit(url).path
        raise SmokeError(f"Network request failed at {path}; check the service and network.") from exc
    try:
        result = json.loads(body.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        result = None
    return status, result if isinstance(result, dict) else None


def run_smoke(origin: str, token: str, *, timeout: float = 90,
              allow_http: bool = False) -> dict[str, Any]:
    origin = normalize_origin(origin, allow_http)
    if len(token.strip()) < 32:
        raise SmokeError("OMARAI_ACCESS_TOKEN is missing or shorter than 32 characters.")

    status, health = request_json(f"{origin}/api/health", timeout=min(timeout, 20))
    if status != 200 or not health or health.get("ok") is not True:
        raise SmokeError(f"Health check failed (HTTP {status}).")
    checks: dict[str, Any] = {"health": "passed"}

    status, _ = request_json(
        f"{origin}/api/agent", payload={"question": "اختبار رفض الوصول غير المصرح به"},
        timeout=min(timeout, 20),
    )
    if status != 401:
        raise SmokeError(f"Unauthenticated POST /api/agent should return 401, received {status}.")
    checks["authentication"] = "passed"

    # These are real network/provider calls and may incur model/search usage.
    status, diagnostics = request_json(
        f"{origin}/api/diagnostics", token=token,
        payload={"test_model": True, "test_social": False}, timeout=timeout,
    )
    if status != 200 or not diagnostics:
        raise SmokeError(f"Authenticated diagnostics failed (HTTP {status}).")
    parts = diagnostics.get("checks", {})
    web = parts.get("web_search", {}) if isinstance(parts, dict) else {}
    model = parts.get("language_model", {}) if isinstance(parts, dict) else {}
    if not isinstance(web, dict) or web.get("status") != "passed":
        raise SmokeError("The real web-search connectivity test did not pass.")
    if not isinstance(model, dict) or model.get("status") != "passed":
        raise SmokeError("The configured language model did not pass a real completion test.")
    checks["live_search"] = {
        "status": "passed", "result_count": web.get("result_count", 0),
        "provider_counts": web.get("provider_counts", {}),
    }
    checks["language_model"] = {"status": "passed", "response_received": True}

    status, answer = request_json(
        f"{origin}/api/agent", token=token, timeout=timeout,
        payload={
            "question": "اختبار تشغيل: ما عاصمة مصر؟ أجب بالعربية بإيجاز واستند إلى المصادر.",
            "history": [], "mode": "auto",
        },
    )
    if status != 200 or not answer:
        raise SmokeError(f"Authenticated agent request failed (HTTP {status}).")
    sources = answer.get("sources")
    usable = [
        item for item in sources if isinstance(item, dict)
        and isinstance(item.get("url"), str)
        and urllib.parse.urlsplit(item["url"]).scheme in {"http", "https"}
        and urllib.parse.urlsplit(item["url"]).hostname
    ] if isinstance(sources, list) else []
    if answer.get("used_web_search") is not True or not usable:
        raise SmokeError("Agent request did not return a live web search with usable source URLs.")
    if answer.get("used_language_model") is not True:
        raise SmokeError("Agent request did not confirm that a language model was used.")
    report = answer.get("search_report")
    checks["agent_request"] = {
        "status": "passed", "source_count": len(usable),
        "direct_pages_read": report.get("pages_fetched") if isinstance(report, dict) else None,
        "providers_reported": report.get("providers_used", []) if isinstance(report, dict) else [],
        "answer_received": bool(str(answer.get("answer", "")).strip()),
    }
    return {
        "result": "passed", "target_host": urllib.parse.urlsplit(origin).hostname,
        "checks": checks,
        "note": "This proves the request path worked at test time, not continuous uptime. Provider usage may incur charges.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Run live acceptance checks against hosted Omarai.")
    parser.add_argument("--base-url", default=os.getenv("OMARAI_BASE_URL", ""))
    parser.add_argument("--timeout", type=float, default=90)
    parser.add_argument("--allow-http", action="store_true",
                        help="Allow HTTP only for localhost/127.0.0.1/::1 testing.")
    args = parser.parse_args()
    try:
        result = run_smoke(args.base_url, os.getenv("OMARAI_ACCESS_TOKEN", "").strip(),
                           timeout=max(5, min(args.timeout, 240)), allow_http=args.allow_http)
    except SmokeError as exc:
        print(json.dumps({"result": "failed", "error": str(exc)}, ensure_ascii=False, indent=2))
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
