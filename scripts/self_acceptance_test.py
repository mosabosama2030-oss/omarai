#!/usr/bin/env python3
"""Local tokenless self-acceptance runner for Omarai.

The local suite never binds beyond loopback. Live model/search calls are opt-in and
must be explicitly enabled because configured providers may consume quota or money.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
import threading
import time
from datetime import UTC, datetime
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def build_live_questions(product: str = "", custom_questions: list[str] | None = None):
    if custom_questions:
        return [
            {"id": f"custom-{index}", "question": item, "mode": "deep", "history": []}
            for index, item in enumerate(custom_questions, 1)
        ]
    questions = [
        {
            "id": "web-research-smoke",
            "question": "ما عاصمة مصر؟ استخدم البحث العميق وأرفق المصادر التي اعتمدت عليها.",
            "mode": "deep",
            "history": [],
        },
        {
            "id": "context-followup",
            "question": "ما الدليل من المصادر السابقة على إجابتك؟ لا تضف معلومة غير مسندة.",
            "mode": "auto",
            "history_from_previous": True,
        },
    ]
    product = str(product or "").strip()
    if product:
        questions.append({
            "id": "buyer-intent-smoke",
            "question": (
                f"ابحث عن إشارات شراء معلنة علنًا تخص {product} في مصر. "
                "لا تعرض جهة كعميل محتمل إلا إذا وجدت طلب شراء أو احتياجًا مباشرًا موثقًا "
                "برابط ومقتطف وتاريخ؛ استبعد قوائم البيع والتخمين."
            ),
            "mode": "deep",
            "history": [],
        })
    return questions


def summarize_response(status_code: int, payload: dict[str, Any] | None) -> dict[str, Any]:
    payload = payload if isinstance(payload, dict) else {}
    answer = str(payload.get("answer") or "")
    sources = payload.get("sources")
    sources = sources if isinstance(sources, list) else []
    report = payload.get("search_report")
    report = report if isinstance(report, dict) else {}
    completion = payload.get("research_completion")
    completion = completion if isinstance(completion, dict) else {}
    counters = completion.get("counters")
    counters = counters if isinstance(counters, dict) else {}
    return {
        "http_status": status_code,
        "answer_present": bool(answer.strip()),
        "answer_length": len(answer),
        "source_count": len(sources),
        "used_web_search": payload.get("used_web_search") is True,
        "used_language_model": payload.get("used_language_model") is True,
        "research_completion_status": completion.get("status")
            or report.get("pipeline_completion_status")
            or "unknown",
        "invalid_citation_references_removed_count": counters.get(
            "invalid_citation_references_removed_count"
        ),
        "citation_support_warning_count": counters.get("citation_support_warning_count"),
    }


def _request_json(url: str, payload: dict[str, Any] | None = None, timeout: float = 90):
    headers = {"Accept": "application/json"}
    data = None
    method = "GET"
    if payload is not None:
        method = "POST"
        headers["Content-Type"] = "application/json"
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = Request(url, data=data, headers=headers, method=method)
    try:
        with urlopen(request, timeout=timeout) as response:
            body = response.read(2_000_000)
            status = response.status
    except HTTPError as exc:
        body = exc.read(200_000)
        status = exc.code
    except (URLError, TimeoutError, OSError) as exc:
        raise RuntimeError(f"Local acceptance request failed: {type(exc).__name__}") from exc
    try:
        parsed = json.loads(body.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        parsed = None
    return status, parsed if isinstance(parsed, dict) else None


def run_acceptance(
    *,
    output_path: str | Path,
    live: bool = False,
    product: str = "",
    custom_questions: list[str] | None = None,
    timeout: float = 90,
) -> dict[str, Any]:
    if live and os.getenv("OMARAI_SELF_TEST_ALLOW_EXTERNAL_CALLS") != "1":
        raise RuntimeError(
            "Live tests require OMARAI_SELF_TEST_ALLOW_EXTERNAL_CALLS=1; "
            "providers may consume quota or money."
        )

    original_environment = {
        key: os.environ.get(key)
        for key in (
            "OMARAI_TEST_MODE", "OMARAI_PUBLIC_DEPLOYMENT", "OMARAI_ACCESS_TOKEN",
            "OMARAI_ACCESS_USER_ID", "OMARAI_DB_PATH", "OMARAI_DEFAULT_TENANT_ID",
            "OMARAI_DEFAULT_TENANT_NAME",
        )
    }
    with tempfile.TemporaryDirectory(prefix="omarai-self-test-") as temporary:
        os.environ["OMARAI_TEST_MODE"] = "1"
        os.environ.pop("OMARAI_PUBLIC_DEPLOYMENT", None)
        os.environ.pop("OMARAI_ACCESS_TOKEN", None)
        os.environ.pop("OMARAI_ACCESS_USER_ID", None)
        os.environ["OMARAI_DB_PATH"] = str(Path(temporary) / "self-test.sqlite3")
        os.environ["OMARAI_DEFAULT_TENANT_ID"] = "self-test"
        os.environ["OMARAI_DEFAULT_TENANT_NAME"] = "Omarai Self-Test"

        try:
            # Import only after test environment and isolated database are configured.
            from http.server import ThreadingHTTPServer
            from api.omarai import Handler
            from agents.omarai import LeadStore

            previous_store = Handler.store
            Handler.store = LeadStore(
                os.environ["OMARAI_DB_PATH"],
                default_tenant_id="self-test",
                default_tenant_name="Omarai Self-Test",
            )
            server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
            server.daemon_threads = True
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            origin = f"http://127.0.0.1:{server.server_port}"
            started = time.monotonic()
            try:
                health_status, health = _request_json(f"{origin}/api/health", timeout=10)
                if health_status != 200 or not health or health.get("ok") is not True:
                    raise RuntimeError(f"Health check failed with HTTP {health_status}")

                analyze_status, analysis = _request_json(
                    f"{origin}/api/analyze",
                    {"text": "مطلوب شراء منتج تجريبي", "tenant_id": "self-test"},
                    timeout=10,
                )
                if analyze_status != 200 or not analysis:
                    raise RuntimeError(f"Local API analysis failed with HTTP {analyze_status}")

                report: dict[str, Any] = {
                    "schema_version": "1.0",
                    "created_at": datetime.now(UTC).isoformat(),
                    "environment": "local_loopback_isolated_database",
                    "authentication": {
                        "access_token_required": False,
                        "test_mode": True,
                        "bind_host": "127.0.0.1",
                        "tenant_id": "self-test",
                    },
                    "external_calls_enabled": live,
                    "checks": {
                        "health": {"status": "passed", "http_status": health_status},
                        "local_analyze": {
                            "status": "passed",
                            "http_status": analyze_status,
                            "result": analysis,
                        },
                    },
                    "build": health.get("build", {}),
                    "questions": [],
                }

                if live:
                    history: list[dict[str, str]] = []
                    question_specs = build_live_questions(product, custom_questions)
                    previous_answer = ""
                    previous_question = ""
                    for spec in question_specs:
                        question = spec["question"]
                        request_history = list(history) if spec.get("history_from_previous") else spec.get("history", [])
                        request_payload = {
                            "question": question,
                            "history": request_history,
                            "mode": spec.get("mode", "deep"),
                            "tenant_id": "self-test",
                        }
                        request_started = time.monotonic()
                        status, response = _request_json(
                            f"{origin}/api/agent", request_payload, timeout=timeout
                        )
                        response = response if isinstance(response, dict) else {}
                        answer = str(response.get("answer") or "")
                        source_rows = response.get("sources")
                        source_rows = source_rows if isinstance(source_rows, list) else []
                        search_report = response.get("search_report")
                        search_report = search_report if isinstance(search_report, dict) else {}
                        report["questions"].append({
                            "id": spec["id"],
                            "question": question,
                            "mode": spec.get("mode", "deep"),
                            "http_status": status,
                            "answer": answer,
                            "summary": summarize_response(status, response),
                            "sources": [
                                {
                                    "title": item.get("title"),
                                    "url": item.get("url"),
                                    "provider": item.get("provider"),
                                    "snippet": item.get("snippet"),
                                    "published_at": item.get("published_at"),
                                    "page_fetch_status": item.get("page_fetch_status"),
                                }
                                for item in source_rows if isinstance(item, dict)
                            ],
                            "provider_diagnostics": search_report.get(
                                "provider_diagnostics", []
                            ),
                            "warnings": response.get("warnings", []),
                            "elapsed_seconds": round(time.monotonic() - request_started, 2),
                        })
                        if spec.get("history_from_previous"):
                            history = []
                        else:
                            history = [
                                {"role": "user", "content": question},
                                {"role": "assistant", "content": answer},
                            ]
                        previous_question, previous_answer = question, answer

                report["elapsed_seconds"] = round(time.monotonic() - started, 2)
                destination = Path(output_path).expanduser()
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_text(
                    json.dumps(report, ensure_ascii=False, indent=2),
                    encoding="utf-8",
                )
                return report
            finally:
                server.shutdown()
                server.server_close()
                thread.join(timeout=2)
                Handler.store = previous_store
        finally:
            for key, value in original_environment.items():
                if value is None:
                    os.environ.pop(key, None)
                else:
                    os.environ[key] = value


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run Omarai's isolated tokenless self-acceptance checks."
    )
    parser.add_argument("--live", action="store_true",
                        help="Also ask the real agent and record full answers and source evidence.")
    parser.add_argument("--allow-external-calls", action="store_true",
                        help="Explicitly allow live provider calls; they may consume quota or money.")
    parser.add_argument("--product", default="",
                        help="Optional product to test public buyer-intent discovery.")
    parser.add_argument("--question", action="append", default=[],
                        help="Custom live question; repeat to add more questions.")
    parser.add_argument("--output", default="artifacts/self_acceptance/latest.json")
    parser.add_argument("--timeout", type=float, default=90)
    args = parser.parse_args()

    if args.live and not args.allow_external_calls:
        parser.error("--live requires --allow-external-calls")
    if args.allow_external_calls:
        os.environ["OMARAI_SELF_TEST_ALLOW_EXTERNAL_CALLS"] = "1"
    try:
        result = run_acceptance(
            output_path=args.output,
            live=args.live,
            product=args.product,
            custom_questions=args.question or None,
            timeout=max(5, min(args.timeout, 240)),
        )
    except Exception as exc:  # noqa: BLE001 - CLI boundary
        print(json.dumps({
            "result": "failed",
            "error": f"{type(exc).__name__}: {exc}",
        }, ensure_ascii=False, indent=2))
        return 1

    print(json.dumps({
        "result": "passed" if not args.live else "completed_with_live_questions",
        "output": str(Path(args.output).expanduser()),
        "token_required": False,
        "live_question_count": len(result["questions"]),
        "checks": result["checks"],
        "questions": [
            {
                "id": item["id"],
                "question": item["question"],
                "answer": item["answer"],
                "summary": item["summary"],
                "sources": [source.get("url") for source in item["sources"]],
            }
            for item in result["questions"]
        ],
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
