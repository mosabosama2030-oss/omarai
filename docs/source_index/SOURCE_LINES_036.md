# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **036**
- سجلات الأسطر: **800**
- النطاق: SRC-70795F4B61-L000491 إلى SRC-4FFD5AFC54-L000254
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## ملفات أخرى

### FILE-70795F4B61 — [scripts/compare_answer_quality_runs.py](../../scripts/compare_answer_quality_runs.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-70795F4B61-L000491](../../scripts/compare_answer_quality_runs.py#L491) | 491 | `"    if not comparison[\"acceptance_blockers\"]:"` | — |
| [SRC-70795F4B61-L000492](../../scripts/compare_answer_quality_runs.py#L492) | 492 | `"        comparison[\"acceptance_status\"] = \"COMPARABLE_WITH_REVIEWED_QUALITY_AND_BUILD_IDENTITIES\""` | — |
| [SRC-70795F4B61-L000493](../../scripts/compare_answer_quality_runs.py#L493) | 493 | `"    else:"` | — |
| [SRC-70795F4B61-L000494](../../scripts/compare_answer_quality_runs.py#L494) | 494 | `"        comparison[\"acceptance_status\"] = \"INCOMPLETE\""` | — |
| [SRC-70795F4B61-L000495](../../scripts/compare_answer_quality_runs.py#L495) | 495 | `"    return comparison"` | — |
| [SRC-70795F4B61-L000496](../../scripts/compare_answer_quality_runs.py#L496) | 496 | `""` | — |
| [SRC-70795F4B61-L000497](../../scripts/compare_answer_quality_runs.py#L497) | 497 | `""` | — |
| [SRC-70795F4B61-L000498](../../scripts/compare_answer_quality_runs.py#L498) | 498 | `"def main(argv: list[str] \| None = None) -> int:"` | — |
| [SRC-70795F4B61-L000499](../../scripts/compare_answer_quality_runs.py#L499) | 499 | `"    parser = argparse.ArgumentParser(description=__doc__)"` | — |
| [SRC-70795F4B61-L000500](../../scripts/compare_answer_quality_runs.py#L500) | 500 | `"    parser.add_argument(\"--baseline-run\", type=Path, required=True)"` | — |
| [SRC-70795F4B61-L000501](../../scripts/compare_answer_quality_runs.py#L501) | 501 | `"    parser.add_argument(\"--candidate-run\", type=Path, required=True)"` | — |
| [SRC-70795F4B61-L000502](../../scripts/compare_answer_quality_runs.py#L502) | 502 | `"    parser.add_argument(\"--baseline-reviews\", type=Path)"` | — |
| [SRC-70795F4B61-L000503](../../scripts/compare_answer_quality_runs.py#L503) | 503 | `"    parser.add_argument(\"--candidate-reviews\", type=Path)"` | — |
| [SRC-70795F4B61-L000504](../../scripts/compare_answer_quality_runs.py#L504) | 504 | `"    parser.add_argument(\"--corpus\", type=Path, default=DEFAULT_CORPUS)"` | — |
| [SRC-70795F4B61-L000505](../../scripts/compare_answer_quality_runs.py#L505) | 505 | `"    parser.add_argument(\"--out\", type=Path)"` | — |
| [SRC-70795F4B61-L000506](../../scripts/compare_answer_quality_runs.py#L506) | 506 | `"    args = parser.parse_args(argv)"` | — |
| [SRC-70795F4B61-L000507](../../scripts/compare_answer_quality_runs.py#L507) | 507 | `"    if bool(args.baseline_reviews) != bool(args.candidate_reviews):"` | — |
| [SRC-70795F4B61-L000508](../../scripts/compare_answer_quality_runs.py#L508) | 508 | `"        parser.error(\"provide both --baseline-reviews and --candidate-reviews, or neither\")"` | — |
| [SRC-70795F4B61-L000509](../../scripts/compare_answer_quality_runs.py#L509) | 509 | `"    try:"` | — |
| [SRC-70795F4B61-L000510](../../scripts/compare_answer_quality_runs.py#L510) | 510 | `"        baseline = load_json_object(args.baseline_run)"` | — |
| [SRC-70795F4B61-L000511](../../scripts/compare_answer_quality_runs.py#L511) | 511 | `"        candidate = load_json_object(args.candidate_run)"` | — |
| [SRC-70795F4B61-L000512](../../scripts/compare_answer_quality_runs.py#L512) | 512 | `"        corpus = load_json_object(args.corpus) if args.baseline_reviews else None"` | — |
| [SRC-70795F4B61-L000513](../../scripts/compare_answer_quality_runs.py#L513) | 513 | `"        before_reviews = load_json_object(args.baseline_reviews) if args.baseline_reviews else None"` | — |
| [SRC-70795F4B61-L000514](../../scripts/compare_answer_quality_runs.py#L514) | 514 | `"        after_reviews = load_json_object(args.candidate_reviews) if args.candidate_reviews else None"` | — |
| [SRC-70795F4B61-L000515](../../scripts/compare_answer_quality_runs.py#L515) | 515 | `"        result = compare_runs("` | — |
| [SRC-70795F4B61-L000516](../../scripts/compare_answer_quality_runs.py#L516) | 516 | `"            baseline, candidate, corpus=corpus,"` | — |
| [SRC-70795F4B61-L000517](../../scripts/compare_answer_quality_runs.py#L517) | 517 | `"            baseline_reviews=before_reviews, candidate_reviews=after_reviews,"` | — |
| [SRC-70795F4B61-L000518](../../scripts/compare_answer_quality_runs.py#L518) | 518 | `"        )"` | — |
| [SRC-70795F4B61-L000519](../../scripts/compare_answer_quality_runs.py#L519) | 519 | `"    except (OSError, ValueError, TypeError, json.JSONDecodeError, KeyError) as exc:"` | — |
| [SRC-70795F4B61-L000520](../../scripts/compare_answer_quality_runs.py#L520) | 520 | `"        print(\"COMPARISON INVALID: \" + str(exc), file=sys.stderr)"` | — |
| [SRC-70795F4B61-L000521](../../scripts/compare_answer_quality_runs.py#L521) | 521 | `"        return 2"` | — |
| [SRC-70795F4B61-L000522](../../scripts/compare_answer_quality_runs.py#L522) | 522 | `"    output = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True)"` | — |
| [SRC-70795F4B61-L000523](../../scripts/compare_answer_quality_runs.py#L523) | 523 | `"    if args.out:"` | — |
| [SRC-70795F4B61-L000524](../../scripts/compare_answer_quality_runs.py#L524) | 524 | `"        args.out.write_text(output + \"\\n\", encoding=\"utf-8\")"` | — |
| [SRC-70795F4B61-L000525](../../scripts/compare_answer_quality_runs.py#L525) | 525 | `"        print(\"Wrote \" + str(args.out))"` | — |
| [SRC-70795F4B61-L000526](../../scripts/compare_answer_quality_runs.py#L526) | 526 | `"    print(output)"` | — |
| [SRC-70795F4B61-L000527](../../scripts/compare_answer_quality_runs.py#L527) | 527 | `"    return 0 if result[\"acceptance_status\"] == \"COMPARABLE_WITH_REVIEWED_QUALITY_AND_BUILD_IDENTITIES\" else 2"` | — |
| [SRC-70795F4B61-L000528](../../scripts/compare_answer_quality_runs.py#L528) | 528 | `""` | — |
| [SRC-70795F4B61-L000529](../../scripts/compare_answer_quality_runs.py#L529) | 529 | `""` | — |
| [SRC-70795F4B61-L000530](../../scripts/compare_answer_quality_runs.py#L530) | 530 | `"if __name__ == \"__main__\":"` | — |
| [SRC-70795F4B61-L000531](../../scripts/compare_answer_quality_runs.py#L531) | 531 | `"    raise SystemExit(main())"` | — |
## ملفات أخرى

### FILE-A8360B1B03 — [scripts/hosted_smoke_test.py](../../scripts/hosted_smoke_test.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-A8360B1B03-L000001](../../scripts/hosted_smoke_test.py#L1) | 1 | `"#!/usr/bin/env python3"` | — |
| [SRC-A8360B1B03-L000002](../../scripts/hosted_smoke_test.py#L2) | 2 | `"\"\"\"End-to-end smoke test for a deployed Omarai instance; uses only stdlib.\"\"\""` | — |
| [SRC-A8360B1B03-L000003](../../scripts/hosted_smoke_test.py#L3) | 3 | `"from __future__ import annotations"` | — |
| [SRC-A8360B1B03-L000004](../../scripts/hosted_smoke_test.py#L4) | 4 | `""` | — |
| [SRC-A8360B1B03-L000005](../../scripts/hosted_smoke_test.py#L5) | 5 | `"import argparse"` | — |
| [SRC-A8360B1B03-L000006](../../scripts/hosted_smoke_test.py#L6) | 6 | `"import hashlib"` | — |
| [SRC-A8360B1B03-L000007](../../scripts/hosted_smoke_test.py#L7) | 7 | `"import json"` | — |
| [SRC-A8360B1B03-L000008](../../scripts/hosted_smoke_test.py#L8) | 8 | `"import os"` | — |
| [SRC-A8360B1B03-L000009](../../scripts/hosted_smoke_test.py#L9) | 9 | `"import re"` | — |
| [SRC-A8360B1B03-L000010](../../scripts/hosted_smoke_test.py#L10) | 10 | `"from pathlib import Path"` | — |
| [SRC-A8360B1B03-L000011](../../scripts/hosted_smoke_test.py#L11) | 11 | `"import sys"` | — |
| [SRC-A8360B1B03-L000012](../../scripts/hosted_smoke_test.py#L12) | 12 | `"import urllib.error"` | — |
| [SRC-A8360B1B03-L000013](../../scripts/hosted_smoke_test.py#L13) | 13 | `"import urllib.parse"` | — |
| [SRC-A8360B1B03-L000014](../../scripts/hosted_smoke_test.py#L14) | 14 | `"import urllib.request"` | — |
| [SRC-A8360B1B03-L000015](../../scripts/hosted_smoke_test.py#L15) | 15 | `"from typing import Any"` | — |
| [SRC-A8360B1B03-L000016](../../scripts/hosted_smoke_test.py#L16) | 16 | `""` | — |
| [SRC-A8360B1B03-L000017](../../scripts/hosted_smoke_test.py#L17) | 17 | `""` | — |
| [SRC-A8360B1B03-L000018](../../scripts/hosted_smoke_test.py#L18) | 18 | `"HOSTED_SMOKE_BUDGET_MAX = {"` | — |
| [SRC-A8360B1B03-L000019](../../scripts/hosted_smoke_test.py#L19) | 19 | `"    \"search_queries\": 3,"` | — |
| [SRC-A8360B1B03-L000020](../../scripts/hosted_smoke_test.py#L20) | 20 | `"    \"search_calls\": 12,"` | — |
| [SRC-A8360B1B03-L000021](../../scripts/hosted_smoke_test.py#L21) | 21 | `"    \"model_calls\": 6,"` | — |
| [SRC-A8360B1B03-L000022](../../scripts/hosted_smoke_test.py#L22) | 22 | `"    \"page_fetches\": 4,"` | — |
| [SRC-A8360B1B03-L000023](../../scripts/hosted_smoke_test.py#L23) | 23 | `"    \"tool_calls\": 0,"` | — |
| [SRC-A8360B1B03-L000024](../../scripts/hosted_smoke_test.py#L24) | 24 | `"}"` | — |
| [SRC-A8360B1B03-L000025](../../scripts/hosted_smoke_test.py#L25) | 25 | `""` | — |
| [SRC-A8360B1B03-L000026](../../scripts/hosted_smoke_test.py#L26) | 26 | `"LIVE_TEST_QUESTION = ("` | — |
| [SRC-A8360B1B03-L000027](../../scripts/hosted_smoke_test.py#L27) | 27 | `"    \"اختبار اكتساب عملاء: ابحث عن طلبات شراء أو مناقصات منشورة وحديثة في مصر تخص \""` | — |
| [SRC-A8360B1B03-L000028](../../scripts/hosted_smoke_test.py#L28) | 28 | `"    \"أنظمة إنذار الحريق. لا تعتبر شركة عميلاً محتملاً إلا إذا وجدت إشارة شراء صريحة \""` | — |
| [SRC-A8360B1B03-L000029](../../scripts/hosted_smoke_test.py#L29) | 29 | `"    \"أو طلب عرض سعر منشورًا. اعرض لكل إشارة المصدر والرابط والتاريخ ومقتطف الدليل، \""` | — |
| [SRC-A8360B1B03-L000030](../../scripts/hosted_smoke_test.py#L30) | 30 | `"    \"وصرّح بوضوح إذا لم تجد طلبًا مؤكدًا.\""` | — |
| [SRC-A8360B1B03-L000031](../../scripts/hosted_smoke_test.py#L31) | 31 | `")"` | — |
| [SRC-A8360B1B03-L000032](../../scripts/hosted_smoke_test.py#L32) | 32 | `""` | — |
| [SRC-A8360B1B03-L000033](../../scripts/hosted_smoke_test.py#L33) | 33 | `""` | — |
| [SRC-A8360B1B03-L000034](../../scripts/hosted_smoke_test.py#L34) | 34 | `"class SmokeError(RuntimeError):"` | — |
| [SRC-A8360B1B03-L000035](../../scripts/hosted_smoke_test.py#L35) | 35 | `"    \"\"\"A live acceptance check failed, optionally carrying a safe partial report.\"\"\""` | — |
| [SRC-A8360B1B03-L000036](../../scripts/hosted_smoke_test.py#L36) | 36 | `""` | — |
| [SRC-A8360B1B03-L000037](../../scripts/hosted_smoke_test.py#L37) | 37 | `"    def __init__(self, message: str, report: dict[str, Any] \| None = None):"` | — |
| [SRC-A8360B1B03-L000038](../../scripts/hosted_smoke_test.py#L38) | 38 | `"        super().__init__(message)"` | — |
| [SRC-A8360B1B03-L000039](../../scripts/hosted_smoke_test.py#L39) | 39 | `"        self.report = report or {}"` | — |
| [SRC-A8360B1B03-L000040](../../scripts/hosted_smoke_test.py#L40) | 40 | `""` | — |
| [SRC-A8360B1B03-L000041](../../scripts/hosted_smoke_test.py#L41) | 41 | `""` | — |
| [SRC-A8360B1B03-L000042](../../scripts/hosted_smoke_test.py#L42) | 42 | `"class _SameOriginRedirectHandler(urllib.request.HTTPRedirectHandler):"` | — |
| [SRC-A8360B1B03-L000043](../../scripts/hosted_smoke_test.py#L43) | 43 | `"    \"\"\"Never forward a bearer token to a different origin during an HTTP redirect.\"\"\""` | — |
| [SRC-A8360B1B03-L000044](../../scripts/hosted_smoke_test.py#L44) | 44 | `""` | — |
| [SRC-A8360B1B03-L000045](../../scripts/hosted_smoke_test.py#L45) | 45 | `"    @staticmethod"` | — |
| [SRC-A8360B1B03-L000046](../../scripts/hosted_smoke_test.py#L46) | 46 | `"    def _origin(url: str) -> tuple[str, str, int \| None]:"` | — |
| [SRC-A8360B1B03-L000047](../../scripts/hosted_smoke_test.py#L47) | 47 | `"        parsed = urllib.parse.urlsplit(url)"` | — |
| [SRC-A8360B1B03-L000048](../../scripts/hosted_smoke_test.py#L48) | 48 | `"        try:"` | — |
| [SRC-A8360B1B03-L000049](../../scripts/hosted_smoke_test.py#L49) | 49 | `"            port = parsed.port"` | — |
| [SRC-A8360B1B03-L000050](../../scripts/hosted_smoke_test.py#L50) | 50 | `"        except ValueError:"` | — |
| [SRC-A8360B1B03-L000051](../../scripts/hosted_smoke_test.py#L51) | 51 | `"            return \"\", \"\", None"` | — |
| [SRC-A8360B1B03-L000052](../../scripts/hosted_smoke_test.py#L52) | 52 | `"        if port is None:"` | — |
| [SRC-A8360B1B03-L000053](../../scripts/hosted_smoke_test.py#L53) | 53 | `"            port = 443 if parsed.scheme.lower() == \"https\" else 80 if parsed.scheme.lower() == \"http\" else None"` | — |
| [SRC-A8360B1B03-L000054](../../scripts/hosted_smoke_test.py#L54) | 54 | `"        return parsed.scheme.lower(), (parsed.hostname or \"\").lower(), port"` | — |
| [SRC-A8360B1B03-L000055](../../scripts/hosted_smoke_test.py#L55) | 55 | `""` | — |
| [SRC-A8360B1B03-L000056](../../scripts/hosted_smoke_test.py#L56) | 56 | `"    def redirect_request(self, req, fp, code, msg, headers, newurl):"` | — |
| [SRC-A8360B1B03-L000057](../../scripts/hosted_smoke_test.py#L57) | 57 | `"        target_url = urllib.parse.urljoin(req.full_url, newurl)"` | — |
| [SRC-A8360B1B03-L000058](../../scripts/hosted_smoke_test.py#L58) | 58 | `"        target = urllib.parse.urlsplit(target_url)"` | — |
| [SRC-A8360B1B03-L000059](../../scripts/hosted_smoke_test.py#L59) | 59 | `"        if ("` | — |
| [SRC-A8360B1B03-L000060](../../scripts/hosted_smoke_test.py#L60) | 60 | `"            self._origin(req.full_url) != self._origin(target_url)"` | — |
| [SRC-A8360B1B03-L000061](../../scripts/hosted_smoke_test.py#L61) | 61 | `"            or target.scheme.lower() not in {\"http\", \"https\"}"` | — |
| [SRC-A8360B1B03-L000062](../../scripts/hosted_smoke_test.py#L62) | 62 | `"            or target.username"` | — |
| [SRC-A8360B1B03-L000063](../../scripts/hosted_smoke_test.py#L63) | 63 | `"            or target.password"` | — |
| [SRC-A8360B1B03-L000064](../../scripts/hosted_smoke_test.py#L64) | 64 | `"        ):"` | — |
| [SRC-A8360B1B03-L000065](../../scripts/hosted_smoke_test.py#L65) | 65 | `"            raise urllib.error.HTTPError("` | — |
| [SRC-A8360B1B03-L000066](../../scripts/hosted_smoke_test.py#L66) | 66 | `"                req.full_url, code, \"Cross-origin redirect blocked\", headers, fp"` | — |
| [SRC-A8360B1B03-L000067](../../scripts/hosted_smoke_test.py#L67) | 67 | `"            )"` | — |
| [SRC-A8360B1B03-L000068](../../scripts/hosted_smoke_test.py#L68) | 68 | `"        return super().redirect_request(req, fp, code, msg, headers, target_url)"` | — |
| [SRC-A8360B1B03-L000069](../../scripts/hosted_smoke_test.py#L69) | 69 | `""` | — |
| [SRC-A8360B1B03-L000070](../../scripts/hosted_smoke_test.py#L70) | 70 | `""` | — |
| [SRC-A8360B1B03-L000071](../../scripts/hosted_smoke_test.py#L71) | 71 | `"def normalize_origin(value: str, allow_http: bool = False) -> str:"` | — |
| [SRC-A8360B1B03-L000072](../../scripts/hosted_smoke_test.py#L72) | 72 | `"    parsed = urllib.parse.urlsplit((value or \"\").strip())"` | — |
| [SRC-A8360B1B03-L000073](../../scripts/hosted_smoke_test.py#L73) | 73 | `"    if parsed.scheme not in {\"https\", \"http\"} or not parsed.hostname:"` | — |
| [SRC-A8360B1B03-L000074](../../scripts/hosted_smoke_test.py#L74) | 74 | `"        raise SmokeError(\"Provide an absolute HTTPS origin, for example https://your-app.example.com.\")"` | — |
| [SRC-A8360B1B03-L000075](../../scripts/hosted_smoke_test.py#L75) | 75 | `"    if parsed.username or parsed.password or parsed.query or parsed.fragment:"` | — |
| [SRC-A8360B1B03-L000076](../../scripts/hosted_smoke_test.py#L76) | 76 | `"        raise SmokeError(\"The base URL must not contain credentials, a query, or a fragment.\")"` | — |
| [SRC-A8360B1B03-L000077](../../scripts/hosted_smoke_test.py#L77) | 77 | `"    if parsed.path not in {\"\", \"/\"}:"` | — |
| [SRC-A8360B1B03-L000078](../../scripts/hosted_smoke_test.py#L78) | 78 | `"        raise SmokeError(\"The base URL must be an origin only; do not add /api or another path.\")"` | — |
| [SRC-A8360B1B03-L000079](../../scripts/hosted_smoke_test.py#L79) | 79 | `"    if parsed.scheme != \"https\" and not ("` | — |
| [SRC-A8360B1B03-L000080](../../scripts/hosted_smoke_test.py#L80) | 80 | `"        allow_http and parsed.hostname.lower() in {\"localhost\", \"127.0.0.1\", \"::1\"}"` | — |
| [SRC-A8360B1B03-L000081](../../scripts/hosted_smoke_test.py#L81) | 81 | `"    ):"` | — |
| [SRC-A8360B1B03-L000082](../../scripts/hosted_smoke_test.py#L82) | 82 | `"        raise SmokeError(\"Hosted tests require HTTPS; plain HTTP is allowed only for local tests.\")"` | — |
| [SRC-A8360B1B03-L000083](../../scripts/hosted_smoke_test.py#L83) | 83 | `"    try:"` | — |
| [SRC-A8360B1B03-L000084](../../scripts/hosted_smoke_test.py#L84) | 84 | `"        port = parsed.port"` | — |
| [SRC-A8360B1B03-L000085](../../scripts/hosted_smoke_test.py#L85) | 85 | `"    except ValueError as exc:"` | — |
| [SRC-A8360B1B03-L000086](../../scripts/hosted_smoke_test.py#L86) | 86 | `"        raise SmokeError(\"Invalid port in base URL.\") from exc"` | — |
| [SRC-A8360B1B03-L000087](../../scripts/hosted_smoke_test.py#L87) | 87 | `"    host = parsed.hostname"` | — |
| [SRC-A8360B1B03-L000088](../../scripts/hosted_smoke_test.py#L88) | 88 | `"    if \":\" in host and not host.startswith(\"[\"):"` | — |
| [SRC-A8360B1B03-L000089](../../scripts/hosted_smoke_test.py#L89) | 89 | `"        host = f\"[{host}]\""` | — |
| [SRC-A8360B1B03-L000090](../../scripts/hosted_smoke_test.py#L90) | 90 | `"    if port:"` | — |
| [SRC-A8360B1B03-L000091](../../scripts/hosted_smoke_test.py#L91) | 91 | `"        host += f\":{port}\""` | — |
| [SRC-A8360B1B03-L000092](../../scripts/hosted_smoke_test.py#L92) | 92 | `"    return f\"{parsed.scheme}://{host}\""` | — |
| [SRC-A8360B1B03-L000093](../../scripts/hosted_smoke_test.py#L93) | 93 | `""` | — |
| [SRC-A8360B1B03-L000094](../../scripts/hosted_smoke_test.py#L94) | 94 | `""` | — |
| [SRC-A8360B1B03-L000095](../../scripts/hosted_smoke_test.py#L95) | 95 | `"def request_json(url: str, *, token: str = \"\", payload: dict[str, Any] \| None = None,"` | — |
| [SRC-A8360B1B03-L000096](../../scripts/hosted_smoke_test.py#L96) | 96 | `"                 timeout: float = 90) -> tuple[int, dict[str, Any] \| None]:"` | — |
| [SRC-A8360B1B03-L000097](../../scripts/hosted_smoke_test.py#L97) | 97 | `"    headers = {\"Accept\": \"application/json\"}"` | — |
| [SRC-A8360B1B03-L000098](../../scripts/hosted_smoke_test.py#L98) | 98 | `"    data = None"` | — |
| [SRC-A8360B1B03-L000099](../../scripts/hosted_smoke_test.py#L99) | 99 | `"    if payload is not None:"` | — |
| [SRC-A8360B1B03-L000100](../../scripts/hosted_smoke_test.py#L100) | 100 | `"        headers[\"Content-Type\"] = \"application/json\""` | — |
| [SRC-A8360B1B03-L000101](../../scripts/hosted_smoke_test.py#L101) | 101 | `"        data = json.dumps(payload, ensure_ascii=False).encode()"` | — |
| [SRC-A8360B1B03-L000102](../../scripts/hosted_smoke_test.py#L102) | 102 | `"    if token:"` | — |
| [SRC-A8360B1B03-L000103](../../scripts/hosted_smoke_test.py#L103) | 103 | `"        headers[\"Authorization\"] = \"Bearer \" + token"` | — |
| [SRC-A8360B1B03-L000104](../../scripts/hosted_smoke_test.py#L104) | 104 | `"    request = urllib.request.Request(url, data=data, headers=headers)"` | — |
| [SRC-A8360B1B03-L000105](../../scripts/hosted_smoke_test.py#L105) | 105 | `"    try:"` | — |
| [SRC-A8360B1B03-L000106](../../scripts/hosted_smoke_test.py#L106) | 106 | `"        opener = urllib.request.build_opener(_SameOriginRedirectHandler())"` | — |
| [SRC-A8360B1B03-L000107](../../scripts/hosted_smoke_test.py#L107) | 107 | `"        with opener.open(request, timeout=timeout) as response:"` | — |
| [SRC-A8360B1B03-L000108](../../scripts/hosted_smoke_test.py#L108) | 108 | `"            status, body = response.status, response.read(1_000_000)"` | — |
| [SRC-A8360B1B03-L000109](../../scripts/hosted_smoke_test.py#L109) | 109 | `"    except urllib.error.HTTPError as exc:"` | — |
| [SRC-A8360B1B03-L000110](../../scripts/hosted_smoke_test.py#L110) | 110 | `"        status = exc.code"` | — |
| [SRC-A8360B1B03-L000111](../../scripts/hosted_smoke_test.py#L111) | 111 | `"        body = exc.read(100_000)"` | — |
| [SRC-A8360B1B03-L000112](../../scripts/hosted_smoke_test.py#L112) | 112 | `"        if status >= 400:"` | — |
| [SRC-A8360B1B03-L000113](../../scripts/hosted_smoke_test.py#L113) | 113 | `"            response_headers = exc.headers or {}"` | — |
| [SRC-A8360B1B03-L000114](../../scripts/hosted_smoke_test.py#L114) | 114 | `"            metadata = {"` | — |
| [SRC-A8360B1B03-L000115](../../scripts/hosted_smoke_test.py#L115) | 115 | `"                \"status\": status,"` | — |
| [SRC-A8360B1B03-L000116](../../scripts/hosted_smoke_test.py#L116) | 116 | `"                \"content_type\": response_headers.get(\"Content-Type\", \"\")[:160],"` | — |
| [SRC-A8360B1B03-L000117](../../scripts/hosted_smoke_test.py#L117) | 117 | `"                \"server\": response_headers.get(\"Server\", \"\")[:120],"` | — |
| [SRC-A8360B1B03-L000118](../../scripts/hosted_smoke_test.py#L118) | 118 | `"                \"request_id\": response_headers.get(\"X-Request-ID\", \"\")[:160],"` | — |
| [SRC-A8360B1B03-L000119](../../scripts/hosted_smoke_test.py#L119) | 119 | `"                \"correlation_id\": response_headers.get(\"X-Correlation-ID\", \"\")[:160],"` | — |
| [SRC-A8360B1B03-L000120](../../scripts/hosted_smoke_test.py#L120) | 120 | `"                \"cf_ray\": response_headers.get(\"CF-Ray\", \"\")[:160],"` | — |
| [SRC-A8360B1B03-L000121](../../scripts/hosted_smoke_test.py#L121) | 121 | `"                \"via\": response_headers.get(\"Via\", \"\")[:160],"` | — |
| [SRC-A8360B1B03-L000122](../../scripts/hosted_smoke_test.py#L122) | 122 | `"                \"body_bytes_sampled\": len(body),"` | — |
| [SRC-A8360B1B03-L000123](../../scripts/hosted_smoke_test.py#L123) | 123 | `"                \"body_sha256\": hashlib.sha256(body).hexdigest(),"` | — |
| [SRC-A8360B1B03-L000124](../../scripts/hosted_smoke_test.py#L124) | 124 | `"            }"` | — |
| [SRC-A8360B1B03-L000125](../../scripts/hosted_smoke_test.py#L125) | 125 | `"            # Never retain the response body: gateways can echo request data or secrets."` | — |
| [SRC-A8360B1B03-L000126](../../scripts/hosted_smoke_test.py#L126) | 126 | `"            return status, {\"_smoke_http\": metadata}"` | — |
| [SRC-A8360B1B03-L000127](../../scripts/hosted_smoke_test.py#L127) | 127 | `"    except (urllib.error.URLError, TimeoutError, OSError) as exc:"` | — |
| [SRC-A8360B1B03-L000128](../../scripts/hosted_smoke_test.py#L128) | 128 | `"        path = urllib.parse.urlsplit(url).path"` | — |
| [SRC-A8360B1B03-L000129](../../scripts/hosted_smoke_test.py#L129) | 129 | `"        raise SmokeError(f\"Network request failed at {path}; check the service and network.\") from exc"` | — |
| [SRC-A8360B1B03-L000130](../../scripts/hosted_smoke_test.py#L130) | 130 | `"    try:"` | — |
| [SRC-A8360B1B03-L000131](../../scripts/hosted_smoke_test.py#L131) | 131 | `"        result = json.loads(body.decode(\"utf-8\"))"` | — |
| [SRC-A8360B1B03-L000132](../../scripts/hosted_smoke_test.py#L132) | 132 | `"    except (UnicodeDecodeError, json.JSONDecodeError):"` | — |
| [SRC-A8360B1B03-L000133](../../scripts/hosted_smoke_test.py#L133) | 133 | `"        result = None"` | — |
| [SRC-A8360B1B03-L000134](../../scripts/hosted_smoke_test.py#L134) | 134 | `"    return status, result if isinstance(result, dict) else None"` | — |
| [SRC-A8360B1B03-L000135](../../scripts/hosted_smoke_test.py#L135) | 135 | `""` | — |
| [SRC-A8360B1B03-L000136](../../scripts/hosted_smoke_test.py#L136) | 136 | `""` | — |
| [SRC-A8360B1B03-L000137](../../scripts/hosted_smoke_test.py#L137) | 137 | `"def run_smoke("` | — |
| [SRC-A8360B1B03-L000138](../../scripts/hosted_smoke_test.py#L138) | 138 | `"    origin: str,"` | — |
| [SRC-A8360B1B03-L000139](../../scripts/hosted_smoke_test.py#L139) | 139 | `"    token: str,"` | — |
| [SRC-A8360B1B03-L000140](../../scripts/hosted_smoke_test.py#L140) | 140 | `"    *,"` | — |
| [SRC-A8360B1B03-L000141](../../scripts/hosted_smoke_test.py#L141) | 141 | `"    timeout: float = 90,"` | — |
| [SRC-A8360B1B03-L000142](../../scripts/hosted_smoke_test.py#L142) | 142 | `"    allow_http: bool = False,"` | — |
| [SRC-A8360B1B03-L000143](../../scripts/hosted_smoke_test.py#L143) | 143 | `"    expected_sha: str \| None = None,"` | — |
| [SRC-A8360B1B03-L000144](../../scripts/hosted_smoke_test.py#L144) | 144 | `"    local_dev_no_token: bool = False,"` | — |
| [SRC-A8360B1B03-L000145](../../scripts/hosted_smoke_test.py#L145) | 145 | `"    allow_provider_usage: bool = False,"` | — |
| [SRC-A8360B1B03-L000146](../../scripts/hosted_smoke_test.py#L146) | 146 | `"    preflight_only: bool = False,"` | — |
| [SRC-A8360B1B03-L000147](../../scripts/hosted_smoke_test.py#L147) | 147 | `") -> dict[str, Any]:"` | — |
| [SRC-A8360B1B03-L000148](../../scripts/hosted_smoke_test.py#L148) | 148 | `"    origin = normalize_origin(origin, allow_http or local_dev_no_token)"` | — |
| [SRC-A8360B1B03-L000149](../../scripts/hosted_smoke_test.py#L149) | 149 | `"    target_host = urllib.parse.urlsplit(origin).hostname or \"\""` | — |
| [SRC-A8360B1B03-L000150](../../scripts/hosted_smoke_test.py#L150) | 150 | `"    loopback_host = target_host.lower() in {\"localhost\", \"127.0.0.1\", \"::1\"}"` | — |
| [SRC-A8360B1B03-L000151](../../scripts/hosted_smoke_test.py#L151) | 151 | `"    if expected_sha is not None and not re.fullmatch(r\"[0-9a-fA-F]{40}\", expected_sha.strip()):"` | — |
| [SRC-A8360B1B03-L000152](../../scripts/hosted_smoke_test.py#L152) | 152 | `"        raise SmokeError(\"The expected source revision must be a full 40-character Git SHA.\")"` | — |
| [SRC-A8360B1B03-L000153](../../scripts/hosted_smoke_test.py#L153) | 153 | `"    if local_dev_no_token and not loopback_host:"` | — |
| [SRC-A8360B1B03-L000154](../../scripts/hosted_smoke_test.py#L154) | 154 | `"        raise SmokeError(\"No-token development mode is restricted to localhost/loopback.\")"` | — |
| [SRC-A8360B1B03-L000155](../../scripts/hosted_smoke_test.py#L155) | 155 | `"    if token.strip():"` | — |
| [SRC-A8360B1B03-L000156](../../scripts/hosted_smoke_test.py#L156) | 156 | `"        if len(token.strip()) < 32:"` | — |
| [SRC-A8360B1B03-L000157](../../scripts/hosted_smoke_test.py#L157) | 157 | `"            raise SmokeError(\"OMARAI_ACCESS_TOKEN is shorter than 32 characters.\")"` | — |
| [SRC-A8360B1B03-L000158](../../scripts/hosted_smoke_test.py#L158) | 158 | `"    elif not (local_dev_no_token and loopback_host) and not preflight_only:"` | — |
| [SRC-A8360B1B03-L000159](../../scripts/hosted_smoke_test.py#L159) | 159 | `"        raise SmokeError("` | — |
| [SRC-A8360B1B03-L000160](../../scripts/hosted_smoke_test.py#L160) | 160 | `"            \"OMARAI_ACCESS_TOKEN is required for live hosted acceptance; no-cost preflight may run without it.\""` | — |
| [SRC-A8360B1B03-L000161](../../scripts/hosted_smoke_test.py#L161) | 161 | `"        )"` | — |
| [SRC-A8360B1B03-L000162](../../scripts/hosted_smoke_test.py#L162) | 162 | `""` | — |
| [SRC-A8360B1B03-L000163](../../scripts/hosted_smoke_test.py#L163) | 163 | `"    if preflight_only and allow_provider_usage:"` | — |
| [SRC-A8360B1B03-L000164](../../scripts/hosted_smoke_test.py#L164) | 164 | `"        raise SmokeError(\"--preflight-only cannot be combined with --allow-provider-usage.\")"` | — |
| [SRC-A8360B1B03-L000165](../../scripts/hosted_smoke_test.py#L165) | 165 | `""` | — |
| [SRC-A8360B1B03-L000166](../../scripts/hosted_smoke_test.py#L166) | 166 | `"    auth_mode = ("` | — |
| [SRC-A8360B1B03-L000167](../../scripts/hosted_smoke_test.py#L167) | 167 | `"        \"bearer_token\" if token.strip()"` | — |
| [SRC-A8360B1B03-L000168](../../scripts/hosted_smoke_test.py#L168) | 168 | `"        else \"local_loopback_dev_bypass\" if local_dev_no_token and loopback_host"` | — |
| [SRC-A8360B1B03-L000169](../../scripts/hosted_smoke_test.py#L169) | 169 | `"        else \"preflight_no_token\""` | — |
| [SRC-A8360B1B03-L000170](../../scripts/hosted_smoke_test.py#L170) | 170 | `"    )"` | — |
| [SRC-A8360B1B03-L000171](../../scripts/hosted_smoke_test.py#L171) | 171 | `"    checks: dict[str, Any] = {}"` | — |
| [SRC-A8360B1B03-L000172](../../scripts/hosted_smoke_test.py#L172) | 172 | `"    partial_report: dict[str, Any] = {"` | — |
| [SRC-A8360B1B03-L000173](../../scripts/hosted_smoke_test.py#L173) | 173 | `"        \"result\": \"running\","` | — |
| [SRC-A8360B1B03-L000174](../../scripts/hosted_smoke_test.py#L174) | 174 | `"        \"target_host\": target_host,"` | — |
| [SRC-A8360B1B03-L000175](../../scripts/hosted_smoke_test.py#L175) | 175 | `"        \"auth_mode\": auth_mode,"` | — |
| [SRC-A8360B1B03-L000176](../../scripts/hosted_smoke_test.py#L176) | 176 | `"        \"checks\": checks,"` | — |
| [SRC-A8360B1B03-L000177](../../scripts/hosted_smoke_test.py#L177) | 177 | `"        \"transcript\": [],"` | — |
| [SRC-A8360B1B03-L000178](../../scripts/hosted_smoke_test.py#L178) | 178 | `"    }"` | — |
| [SRC-A8360B1B03-L000179](../../scripts/hosted_smoke_test.py#L179) | 179 | `"    status, health = request_json(f\"{origin}/api/health\", timeout=min(timeout, 20))"` | — |
| [SRC-A8360B1B03-L000180](../../scripts/hosted_smoke_test.py#L180) | 180 | `"    if status != 200 or not health or health.get(\"ok\") is not True:"` | — |
| [SRC-A8360B1B03-L000181](../../scripts/hosted_smoke_test.py#L181) | 181 | `"        if isinstance(health, dict) and isinstance(health.get(\"_smoke_http\"), dict):"` | — |
| [SRC-A8360B1B03-L000182](../../scripts/hosted_smoke_test.py#L182) | 182 | `"            partial_report[\"http_response\"] = health[\"_smoke_http\"]"` | — |
| [SRC-A8360B1B03-L000183](../../scripts/hosted_smoke_test.py#L183) | 183 | `"        raise SmokeError(f\"Health check failed (HTTP {status}).\", partial_report)"` | — |
| [SRC-A8360B1B03-L000184](../../scripts/hosted_smoke_test.py#L184) | 184 | `"    checks[\"health\"] = \"passed\""` | — |
| [SRC-A8360B1B03-L000185](../../scripts/hosted_smoke_test.py#L185) | 185 | `""` | — |
| [SRC-A8360B1B03-L000186](../../scripts/hosted_smoke_test.py#L186) | 186 | `"    build = health.get(\"build\")"` | — |
| [SRC-A8360B1B03-L000187](../../scripts/hosted_smoke_test.py#L187) | 187 | `"    reported_sha = build.get(\"sha\") if isinstance(build, dict) else None"` | — |
| [SRC-A8360B1B03-L000188](../../scripts/hosted_smoke_test.py#L188) | 188 | `"    if expected_sha is not None:"` | — |
| [SRC-A8360B1B03-L000189](../../scripts/hosted_smoke_test.py#L189) | 189 | `"        expected = expected_sha.strip().lower()"` | — |
| [SRC-A8360B1B03-L000190](../../scripts/hosted_smoke_test.py#L190) | 190 | `"        if not isinstance(reported_sha, str) or reported_sha.lower() != expected:"` | — |
| [SRC-A8360B1B03-L000191](../../scripts/hosted_smoke_test.py#L191) | 191 | `"            raise SmokeError("` | — |
| [SRC-A8360B1B03-L000192](../../scripts/hosted_smoke_test.py#L192) | 192 | `"                \"The deployed service SHA does not match the expected Git commit. \""` | — |
| [SRC-A8360B1B03-L000193](../../scripts/hosted_smoke_test.py#L193) | 193 | `"                \"Pass OMARAI_BUILD_SHA as a Docker build argument for the deployed revision, \""` | — |
| [SRC-A8360B1B03-L000194](../../scripts/hosted_smoke_test.py#L194) | 194 | `"                \"then rebuild and redeploy.\","` | — |
| [SRC-A8360B1B03-L000195](../../scripts/hosted_smoke_test.py#L195) | 195 | `"                partial_report,"` | — |
| [SRC-A8360B1B03-L000196](../../scripts/hosted_smoke_test.py#L196) | 196 | `"            )"` | — |
| [SRC-A8360B1B03-L000197](../../scripts/hosted_smoke_test.py#L197) | 197 | `"        checks[\"build_identity\"] = {"` | — |
| [SRC-A8360B1B03-L000198](../../scripts/hosted_smoke_test.py#L198) | 198 | `"            \"status\": \"passed\","` | — |
| [SRC-A8360B1B03-L000199](../../scripts/hosted_smoke_test.py#L199) | 199 | `"            \"expected_sha\": expected,"` | — |
| [SRC-A8360B1B03-L000200](../../scripts/hosted_smoke_test.py#L200) | 200 | `"            \"reported_sha\": reported_sha.lower(),"` | — |
| [SRC-A8360B1B03-L000201](../../scripts/hosted_smoke_test.py#L201) | 201 | `"        }"` | — |
| [SRC-A8360B1B03-L000202](../../scripts/hosted_smoke_test.py#L202) | 202 | `"    else:"` | — |
| [SRC-A8360B1B03-L000203](../../scripts/hosted_smoke_test.py#L203) | 203 | `"        checks[\"build_identity\"] = {"` | — |
| [SRC-A8360B1B03-L000204](../../scripts/hosted_smoke_test.py#L204) | 204 | `"            \"status\": \"not_checked\","` | — |
| [SRC-A8360B1B03-L000205](../../scripts/hosted_smoke_test.py#L205) | 205 | `"            \"reported_sha\": reported_sha if isinstance(reported_sha, str) else \"unknown\","` | — |
| [SRC-A8360B1B03-L000206](../../scripts/hosted_smoke_test.py#L206) | 206 | `"        }"` | — |
| [SRC-A8360B1B03-L000207](../../scripts/hosted_smoke_test.py#L207) | 207 | `""` | — |
| [SRC-A8360B1B03-L000208](../../scripts/hosted_smoke_test.py#L208) | 208 | `"    if token.strip() or (preflight_only and not local_dev_no_token):"` | — |
| [SRC-A8360B1B03-L000209](../../scripts/hosted_smoke_test.py#L209) | 209 | `"        status, auth_response = request_json("` | — |
| [SRC-A8360B1B03-L000210](../../scripts/hosted_smoke_test.py#L210) | 210 | `"            f\"{origin}/api/agent\", payload={\"question\": \"\"},"` | — |
| [SRC-A8360B1B03-L000211](../../scripts/hosted_smoke_test.py#L211) | 211 | `"            timeout=min(timeout, 20),"` | — |
| [SRC-A8360B1B03-L000212](../../scripts/hosted_smoke_test.py#L212) | 212 | `"        )"` | — |
| [SRC-A8360B1B03-L000213](../../scripts/hosted_smoke_test.py#L213) | 213 | `"        if status != 401:"` | — |
| [SRC-A8360B1B03-L000214](../../scripts/hosted_smoke_test.py#L214) | 214 | `"            if isinstance(auth_response, dict) and isinstance(auth_response.get(\"_smoke_http\"), dict):"` | — |
| [SRC-A8360B1B03-L000215](../../scripts/hosted_smoke_test.py#L215) | 215 | `"                partial_report[\"http_response\"] = auth_response[\"_smoke_http\"]"` | — |
| [SRC-A8360B1B03-L000216](../../scripts/hosted_smoke_test.py#L216) | 216 | `"            raise SmokeError("` | — |
| [SRC-A8360B1B03-L000217](../../scripts/hosted_smoke_test.py#L217) | 217 | `"                f\"Unauthenticated POST /api/agent should return 401, received {status}.\","` | — |
| [SRC-A8360B1B03-L000218](../../scripts/hosted_smoke_test.py#L218) | 218 | `"                partial_report,"` | — |
| [SRC-A8360B1B03-L000219](../../scripts/hosted_smoke_test.py#L219) | 219 | `"            )"` | — |
| [SRC-A8360B1B03-L000220](../../scripts/hosted_smoke_test.py#L220) | 220 | `"        checks[\"authentication\"] = \"passed\""` | — |
| [SRC-A8360B1B03-L000221](../../scripts/hosted_smoke_test.py#L221) | 221 | `"    else:"` | — |
| [SRC-A8360B1B03-L000222](../../scripts/hosted_smoke_test.py#L222) | 222 | `"        checks[\"authentication\"] = \"local_loopback_dev_bypass\""` | — |
| [SRC-A8360B1B03-L000223](../../scripts/hosted_smoke_test.py#L223) | 223 | `""` | — |
| [SRC-A8360B1B03-L000224](../../scripts/hosted_smoke_test.py#L224) | 224 | `"    if preflight_only:"` | — |
| [SRC-A8360B1B03-L000225](../../scripts/hosted_smoke_test.py#L225) | 225 | `"        checks[\"provider_usage\"] = {\"status\": \"skipped_not_approved\"}"` | — |
| [SRC-A8360B1B03-L000226](../../scripts/hosted_smoke_test.py#L226) | 226 | `"        partial_report.update({"` | — |
| [SRC-A8360B1B03-L000227](../../scripts/hosted_smoke_test.py#L227) | 227 | `"            \"result\": \"preflight_passed\","` | — |
| [SRC-A8360B1B03-L000228](../../scripts/hosted_smoke_test.py#L228) | 228 | `"            \"checks\": checks,"` | — |
| [SRC-A8360B1B03-L000229](../../scripts/hosted_smoke_test.py#L229) | 229 | `"            \"note\": ("` | — |
| [SRC-A8360B1B03-L000230](../../scripts/hosted_smoke_test.py#L230) | 230 | `"                \"No-cost preflight only: health, build identity (when requested), and authentication \""` | — |
| [SRC-A8360B1B03-L000231](../../scripts/hosted_smoke_test.py#L231) | 231 | `"                \"were checked. No search provider or language model was called.\""` | — |
| [SRC-A8360B1B03-L000232](../../scripts/hosted_smoke_test.py#L232) | 232 | `"            ),"` | — |
| [SRC-A8360B1B03-L000233](../../scripts/hosted_smoke_test.py#L233) | 233 | `"        })"` | — |
| [SRC-A8360B1B03-L000234](../../scripts/hosted_smoke_test.py#L234) | 234 | `"        return partial_report"` | — |
| [SRC-A8360B1B03-L000235](../../scripts/hosted_smoke_test.py#L235) | 235 | `""` | — |
| [SRC-A8360B1B03-L000236](../../scripts/hosted_smoke_test.py#L236) | 236 | `"    if not allow_provider_usage:"` | — |
| [SRC-A8360B1B03-L000237](../../scripts/hosted_smoke_test.py#L237) | 237 | `"        checks[\"provider_usage\"] = {\"status\": \"blocked_not_approved\"}"` | — |
| [SRC-A8360B1B03-L000238](../../scripts/hosted_smoke_test.py#L238) | 238 | `"        raise SmokeError("` | — |
| [SRC-A8360B1B03-L000239](../../scripts/hosted_smoke_test.py#L239) | 239 | `"            \"No-cost preflight passed, but live search/model usage was not approved. \""` | — |
| [SRC-A8360B1B03-L000240](../../scripts/hosted_smoke_test.py#L240) | 240 | `"            \"Re-run with --allow-provider-usage only after explicit human approval.\","` | — |
| [SRC-A8360B1B03-L000241](../../scripts/hosted_smoke_test.py#L241) | 241 | `"            partial_report,"` | — |
| [SRC-A8360B1B03-L000242](../../scripts/hosted_smoke_test.py#L242) | 242 | `"        )"` | — |
| [SRC-A8360B1B03-L000243](../../scripts/hosted_smoke_test.py#L243) | 243 | `""` | — |
| [SRC-A8360B1B03-L000244](../../scripts/hosted_smoke_test.py#L244) | 244 | `"    checks[\"provider_usage\"] = {"` | — |
| [SRC-A8360B1B03-L000245](../../scripts/hosted_smoke_test.py#L245) | 245 | `"        \"status\": \"approved\","` | — |
| [SRC-A8360B1B03-L000246](../../scripts/hosted_smoke_test.py#L246) | 246 | `"        \"scope\": {"` | — |
| [SRC-A8360B1B03-L000247](../../scripts/hosted_smoke_test.py#L247) | 247 | `"            \"profile\": \"hosted_smoke\","` | — |
| [SRC-A8360B1B03-L000248](../../scripts/hosted_smoke_test.py#L248) | 248 | `"            \"max_search_queries\": HOSTED_SMOKE_BUDGET_MAX[\"search_queries\"],"` | — |
| [SRC-A8360B1B03-L000249](../../scripts/hosted_smoke_test.py#L249) | 249 | `"            \"max_provider_requests\": HOSTED_SMOKE_BUDGET_MAX[\"search_calls\"],"` | — |
| [SRC-A8360B1B03-L000250](../../scripts/hosted_smoke_test.py#L250) | 250 | `"            \"max_model_calls\": HOSTED_SMOKE_BUDGET_MAX[\"model_calls\"],"` | — |
| [SRC-A8360B1B03-L000251](../../scripts/hosted_smoke_test.py#L251) | 251 | `"            \"max_page_fetches\": HOSTED_SMOKE_BUDGET_MAX[\"page_fetches\"],"` | — |
| [SRC-A8360B1B03-L000252](../../scripts/hosted_smoke_test.py#L252) | 252 | `"            \"tool_calls\": HOSTED_SMOKE_BUDGET_MAX[\"tool_calls\"],"` | — |
| [SRC-A8360B1B03-L000253](../../scripts/hosted_smoke_test.py#L253) | 253 | `"            \"note\": \"Server-enforced per-request ceilings; operator settings may be stricter.\","` | — |
| [SRC-A8360B1B03-L000254](../../scripts/hosted_smoke_test.py#L254) | 254 | `"        },"` | — |
| [SRC-A8360B1B03-L000255](../../scripts/hosted_smoke_test.py#L255) | 255 | `"    }"` | — |
| [SRC-A8360B1B03-L000256](../../scripts/hosted_smoke_test.py#L256) | 256 | `"    status, answer = request_json("` | — |
| [SRC-A8360B1B03-L000257](../../scripts/hosted_smoke_test.py#L257) | 257 | `"        f\"{origin}/api/agent\", token=token, timeout=timeout,"` | — |
| [SRC-A8360B1B03-L000258](../../scripts/hosted_smoke_test.py#L258) | 258 | `"        payload={"` | — |
| [SRC-A8360B1B03-L000259](../../scripts/hosted_smoke_test.py#L259) | 259 | `"            \"question\": LIVE_TEST_QUESTION,"` | — |
| [SRC-A8360B1B03-L000260](../../scripts/hosted_smoke_test.py#L260) | 260 | `"            \"history\": [], \"mode\": \"auto\", \"request_profile\": \"hosted_smoke\","` | — |
| [SRC-A8360B1B03-L000261](../../scripts/hosted_smoke_test.py#L261) | 261 | `"        },"` | — |
| [SRC-A8360B1B03-L000262](../../scripts/hosted_smoke_test.py#L262) | 262 | `"    )"` | — |
| [SRC-A8360B1B03-L000263](../../scripts/hosted_smoke_test.py#L263) | 263 | `"    if status != 200 or not answer:"` | — |
| [SRC-A8360B1B03-L000264](../../scripts/hosted_smoke_test.py#L264) | 264 | `"        if isinstance(answer, dict) and isinstance(answer.get(\"_smoke_http\"), dict):"` | — |
| [SRC-A8360B1B03-L000265](../../scripts/hosted_smoke_test.py#L265) | 265 | `"            partial_report[\"http_response\"] = answer[\"_smoke_http\"]"` | — |
| [SRC-A8360B1B03-L000266](../../scripts/hosted_smoke_test.py#L266) | 266 | `"        raise SmokeError(f\"Authenticated agent request failed (HTTP {status}).\", partial_report)"` | — |
| [SRC-A8360B1B03-L000267](../../scripts/hosted_smoke_test.py#L267) | 267 | `"    sources = answer.get(\"sources\")"` | — |
| [SRC-A8360B1B03-L000268](../../scripts/hosted_smoke_test.py#L268) | 268 | `"    usable = ["` | — |
| [SRC-A8360B1B03-L000269](../../scripts/hosted_smoke_test.py#L269) | 269 | `"        item for item in sources if isinstance(item, dict)"` | — |
| [SRC-A8360B1B03-L000270](../../scripts/hosted_smoke_test.py#L270) | 270 | `"        and isinstance(item.get(\"url\"), str)"` | — |
| [SRC-A8360B1B03-L000271](../../scripts/hosted_smoke_test.py#L271) | 271 | `"        and urllib.parse.urlsplit(item[\"url\"]).scheme in {\"http\", \"https\"}"` | — |
| [SRC-A8360B1B03-L000272](../../scripts/hosted_smoke_test.py#L272) | 272 | `"        and urllib.parse.urlsplit(item[\"url\"]).hostname"` | — |
| [SRC-A8360B1B03-L000273](../../scripts/hosted_smoke_test.py#L273) | 273 | `"    ] if isinstance(sources, list) else []"` | — |
| [SRC-A8360B1B03-L000274](../../scripts/hosted_smoke_test.py#L274) | 274 | `"    search_report = answer.get(\"search_report\")"` | — |
| [SRC-A8360B1B03-L000275](../../scripts/hosted_smoke_test.py#L275) | 275 | `"    raw_answer = answer.get(\"answer\")"` | — |
| [SRC-A8360B1B03-L000276](../../scripts/hosted_smoke_test.py#L276) | 276 | `"    answer_text = raw_answer.strip() if isinstance(raw_answer, str) else \"\""` | — |
| [SRC-A8360B1B03-L000277](../../scripts/hosted_smoke_test.py#L277) | 277 | `"    source_records = ["` | — |
| [SRC-A8360B1B03-L000278](../../scripts/hosted_smoke_test.py#L278) | 278 | `"        {"` | — |
| [SRC-A8360B1B03-L000279](../../scripts/hosted_smoke_test.py#L279) | 279 | `"            \"title\": str(item.get(\"title\") or \"\")[:300],"` | — |
| [SRC-A8360B1B03-L000280](../../scripts/hosted_smoke_test.py#L280) | 280 | `"            \"url\": str(item.get(\"url\") or \"\")[:2048],"` | — |
| [SRC-A8360B1B03-L000281](../../scripts/hosted_smoke_test.py#L281) | 281 | `"            \"provider\": str(item.get(\"provider\") or \"\")[:80],"` | — |
| [SRC-A8360B1B03-L000282](../../scripts/hosted_smoke_test.py#L282) | 282 | `"            \"snippet\": str(item.get(\"snippet\") or \"\")[:1200],"` | — |
| [SRC-A8360B1B03-L000283](../../scripts/hosted_smoke_test.py#L283) | 283 | `"            \"published_at\": str(item.get(\"published_at\") or \"\")[:100],"` | — |
| [SRC-A8360B1B03-L000284](../../scripts/hosted_smoke_test.py#L284) | 284 | `"        }"` | — |
| [SRC-A8360B1B03-L000285](../../scripts/hosted_smoke_test.py#L285) | 285 | `"        for item in usable"` | — |
| [SRC-A8360B1B03-L000286](../../scripts/hosted_smoke_test.py#L286) | 286 | `"    ]"` | — |
| [SRC-A8360B1B03-L000287](../../scripts/hosted_smoke_test.py#L287) | 287 | `"    transcript = {"` | — |
| [SRC-A8360B1B03-L000288](../../scripts/hosted_smoke_test.py#L288) | 288 | `"        \"case_id\": \"sales_intent_fire_alarm_egypt\","` | — |
| [SRC-A8360B1B03-L000289](../../scripts/hosted_smoke_test.py#L289) | 289 | `"        \"question\": LIVE_TEST_QUESTION,"` | — |
| [SRC-A8360B1B03-L000290](../../scripts/hosted_smoke_test.py#L290) | 290 | `"        \"answer\": answer_text,"` | — |
| [SRC-A8360B1B03-L000291](../../scripts/hosted_smoke_test.py#L291) | 291 | `"        \"used_web_search\": answer.get(\"used_web_search\") is True,"` | — |
| [SRC-A8360B1B03-L000292](../../scripts/hosted_smoke_test.py#L292) | 292 | `"        \"used_language_model\": answer.get(\"used_language_model\") is True,"` | — |
| [SRC-A8360B1B03-L000293](../../scripts/hosted_smoke_test.py#L293) | 293 | `"        \"sources\": source_records,"` | — |
| [SRC-A8360B1B03-L000294](../../scripts/hosted_smoke_test.py#L294) | 294 | `"        \"pipeline_completion_status\": ("` | — |
| [SRC-A8360B1B03-L000295](../../scripts/hosted_smoke_test.py#L295) | 295 | `"            search_report.get(\"pipeline_completion_status\")"` | — |
| [SRC-A8360B1B03-L000296](../../scripts/hosted_smoke_test.py#L296) | 296 | `"            if isinstance(search_report, dict) else None"` | — |
| [SRC-A8360B1B03-L000297](../../scripts/hosted_smoke_test.py#L297) | 297 | `"        ),"` | — |
| [SRC-A8360B1B03-L000298](../../scripts/hosted_smoke_test.py#L298) | 298 | `"        \"answer_evidence_status\": answer.get(\"answer_evidence_status\"),"` | — |
| [SRC-A8360B1B03-L000299](../../scripts/hosted_smoke_test.py#L299) | 299 | `"        \"semantic_claim_verification_status\": ("` | — |
| [SRC-A8360B1B03-L000300](../../scripts/hosted_smoke_test.py#L300) | 300 | `"            search_report.get(\"semantic_claim_verification\", {}).get(\"status\")"` | — |
| [SRC-A8360B1B03-L000301](../../scripts/hosted_smoke_test.py#L301) | 301 | `"            if isinstance(search_report, dict)"` | — |
| [SRC-A8360B1B03-L000302](../../scripts/hosted_smoke_test.py#L302) | 302 | `"            and isinstance(search_report.get(\"semantic_claim_verification\"), dict)"` | — |
| [SRC-A8360B1B03-L000303](../../scripts/hosted_smoke_test.py#L303) | 303 | `"            else None"` | — |
| [SRC-A8360B1B03-L000304](../../scripts/hosted_smoke_test.py#L304) | 304 | `"        ),"` | — |
| [SRC-A8360B1B03-L000305](../../scripts/hosted_smoke_test.py#L305) | 305 | `"        \"request_budget\": answer.get(\"request_budget\"),"` | — |
| [SRC-A8360B1B03-L000306](../../scripts/hosted_smoke_test.py#L306) | 306 | `"    }"` | — |
| [SRC-A8360B1B03-L000307](../../scripts/hosted_smoke_test.py#L307) | 307 | `"    partial_report[\"transcript\"] = [transcript]"` | — |
| [SRC-A8360B1B03-L000308](../../scripts/hosted_smoke_test.py#L308) | 308 | `"    if not answer_text:"` | — |
| [SRC-A8360B1B03-L000309](../../scripts/hosted_smoke_test.py#L309) | 309 | `"        raise SmokeError(\"Agent request returned an empty or whitespace-only answer.\", partial_report)"` | — |
| [SRC-A8360B1B03-L000310](../../scripts/hosted_smoke_test.py#L310) | 310 | `"    if answer.get(\"used_web_search\") is not True or not usable:"` | — |
| [SRC-A8360B1B03-L000311](../../scripts/hosted_smoke_test.py#L311) | 311 | `"        raise SmokeError("` | — |
| [SRC-A8360B1B03-L000312](../../scripts/hosted_smoke_test.py#L312) | 312 | `"            \"Agent request did not return a live web search with usable source URLs.\","` | — |
| [SRC-A8360B1B03-L000313](../../scripts/hosted_smoke_test.py#L313) | 313 | `"            partial_report,"` | — |
| [SRC-A8360B1B03-L000314](../../scripts/hosted_smoke_test.py#L314) | 314 | `"        )"` | — |
| [SRC-A8360B1B03-L000315](../../scripts/hosted_smoke_test.py#L315) | 315 | `"    if answer.get(\"used_language_model\") is not True:"` | — |
| [SRC-A8360B1B03-L000316](../../scripts/hosted_smoke_test.py#L316) | 316 | `"        raise SmokeError("` | — |
| [SRC-A8360B1B03-L000317](../../scripts/hosted_smoke_test.py#L317) | 317 | `"            \"Agent request did not confirm that a language model was used.\","` | — |
| [SRC-A8360B1B03-L000318](../../scripts/hosted_smoke_test.py#L318) | 318 | `"            partial_report,"` | — |
| [SRC-A8360B1B03-L000319](../../scripts/hosted_smoke_test.py#L319) | 319 | `"        )"` | — |
| [SRC-A8360B1B03-L000320](../../scripts/hosted_smoke_test.py#L320) | 320 | `"    request_budget = answer.get(\"request_budget\")"` | — |
| [SRC-A8360B1B03-L000321](../../scripts/hosted_smoke_test.py#L321) | 321 | `"    if not isinstance(request_budget, dict) or request_budget.get(\"profile\") != \"hosted_smoke\":"` | — |
| [SRC-A8360B1B03-L000322](../../scripts/hosted_smoke_test.py#L322) | 322 | `"        raise SmokeError(\"Agent response did not confirm the hosted_smoke request budget profile.\", partial_report)"` | — |
| [SRC-A8360B1B03-L000323](../../scripts/hosted_smoke_test.py#L323) | 323 | `"    budget_limits = request_budget.get(\"limits\")"` | — |
| [SRC-A8360B1B03-L000324](../../scripts/hosted_smoke_test.py#L324) | 324 | `"    budget_counts = request_budget.get(\"counts\")"` | — |
| [SRC-A8360B1B03-L000325](../../scripts/hosted_smoke_test.py#L325) | 325 | `"    if not isinstance(budget_limits, dict) or not isinstance(budget_counts, dict):"` | — |
| [SRC-A8360B1B03-L000326](../../scripts/hosted_smoke_test.py#L326) | 326 | `"        raise SmokeError(\"Agent response omitted request-budget limits or counters.\", partial_report)"` | — |
| [SRC-A8360B1B03-L000327](../../scripts/hosted_smoke_test.py#L327) | 327 | `"    for resource, maximum in HOSTED_SMOKE_BUDGET_MAX.items():"` | — |
| [SRC-A8360B1B03-L000328](../../scripts/hosted_smoke_test.py#L328) | 328 | `"        limit = budget_limits.get(resource)"` | — |
| [SRC-A8360B1B03-L000329](../../scripts/hosted_smoke_test.py#L329) | 329 | `"        count = budget_counts.get(resource)"` | — |
| [SRC-A8360B1B03-L000330](../../scripts/hosted_smoke_test.py#L330) | 330 | `"        if ("` | — |
| [SRC-A8360B1B03-L000331](../../scripts/hosted_smoke_test.py#L331) | 331 | `"            isinstance(limit, bool) or not isinstance(limit, int)"` | — |
| [SRC-A8360B1B03-L000332](../../scripts/hosted_smoke_test.py#L332) | 332 | `"            or isinstance(count, bool) or not isinstance(count, int)"` | — |
| [SRC-A8360B1B03-L000333](../../scripts/hosted_smoke_test.py#L333) | 333 | `"            or limit < 0 or limit > maximum"` | — |
| [SRC-A8360B1B03-L000334](../../scripts/hosted_smoke_test.py#L334) | 334 | `"            or count < 0 or count > limit"` | — |
| [SRC-A8360B1B03-L000335](../../scripts/hosted_smoke_test.py#L335) | 335 | `"        ):"` | — |
| [SRC-A8360B1B03-L000336](../../scripts/hosted_smoke_test.py#L336) | 336 | `"            raise SmokeError("` | — |
| [SRC-A8360B1B03-L000337](../../scripts/hosted_smoke_test.py#L337) | 337 | `"                f\"Agent hosted_smoke request budget is missing, exceeded, or invalid for {resource}.\","` | — |
| [SRC-A8360B1B03-L000338](../../scripts/hosted_smoke_test.py#L338) | 338 | `"                partial_report,"` | — |
| [SRC-A8360B1B03-L000339](../../scripts/hosted_smoke_test.py#L339) | 339 | `"            )"` | — |
| [SRC-A8360B1B03-L000340](../../scripts/hosted_smoke_test.py#L340) | 340 | `"    if ("` | — |
| [SRC-A8360B1B03-L000341](../../scripts/hosted_smoke_test.py#L341) | 341 | `"        budget_counts[\"search_queries\"] < 1"` | — |
| [SRC-A8360B1B03-L000342](../../scripts/hosted_smoke_test.py#L342) | 342 | `"        or budget_counts[\"search_calls\"] < 1"` | — |
| [SRC-A8360B1B03-L000343](../../scripts/hosted_smoke_test.py#L343) | 343 | `"        or budget_counts[\"model_calls\"] < 1"` | — |
| [SRC-A8360B1B03-L000344](../../scripts/hosted_smoke_test.py#L344) | 344 | `"    ):"` | — |
| [SRC-A8360B1B03-L000345](../../scripts/hosted_smoke_test.py#L345) | 345 | `"        raise SmokeError("` | — |
| [SRC-A8360B1B03-L000346](../../scripts/hosted_smoke_test.py#L346) | 346 | `"            \"Agent hosted_smoke request budget counters do not prove search and model work occurred.\","` | — |
| [SRC-A8360B1B03-L000347](../../scripts/hosted_smoke_test.py#L347) | 347 | `"            partial_report,"` | — |
| [SRC-A8360B1B03-L000348](../../scripts/hosted_smoke_test.py#L348) | 348 | `"        )"` | — |
| [SRC-A8360B1B03-L000349](../../scripts/hosted_smoke_test.py#L349) | 349 | `"    budget_timeout = request_budget.get(\"timeout_seconds\")"` | — |
| [SRC-A8360B1B03-L000350](../../scripts/hosted_smoke_test.py#L350) | 350 | `"    if ("` | — |
| [SRC-A8360B1B03-L000351](../../scripts/hosted_smoke_test.py#L351) | 351 | `"        isinstance(budget_timeout, bool)"` | — |
| [SRC-A8360B1B03-L000352](../../scripts/hosted_smoke_test.py#L352) | 352 | `"        or not isinstance(budget_timeout, (int, float))"` | — |
| [SRC-A8360B1B03-L000353](../../scripts/hosted_smoke_test.py#L353) | 353 | `"        or budget_timeout <= 0"` | — |
| [SRC-A8360B1B03-L000354](../../scripts/hosted_smoke_test.py#L354) | 354 | `"        or budget_timeout > 75"` | — |
| [SRC-A8360B1B03-L000355](../../scripts/hosted_smoke_test.py#L355) | 355 | `"        or request_budget.get(\"budget_exhausted\") is not False"` | — |
| [SRC-A8360B1B03-L000356](../../scripts/hosted_smoke_test.py#L356) | 356 | `"        or request_budget.get(\"deadline_exceeded\") is not False"` | — |
| [SRC-A8360B1B03-L000357](../../scripts/hosted_smoke_test.py#L357) | 357 | `"    ):"` | — |
| [SRC-A8360B1B03-L000358](../../scripts/hosted_smoke_test.py#L358) | 358 | `"        raise SmokeError(\"Agent hosted_smoke request budget was exhausted or exceeded its timeout ceiling.\", partial_report)"` | — |
| [SRC-A8360B1B03-L000359](../../scripts/hosted_smoke_test.py#L359) | 359 | `"    checks[\"request_budget\"] = {"` | — |
| [SRC-A8360B1B03-L000360](../../scripts/hosted_smoke_test.py#L360) | 360 | `"        \"status\": \"passed\","` | — |
| [SRC-A8360B1B03-L000361](../../scripts/hosted_smoke_test.py#L361) | 361 | `"        \"profile\": \"hosted_smoke\","` | — |
| [SRC-A8360B1B03-L000362](../../scripts/hosted_smoke_test.py#L362) | 362 | `"        \"timeout_seconds\": budget_timeout,"` | — |
| [SRC-A8360B1B03-L000363](../../scripts/hosted_smoke_test.py#L363) | 363 | `"        \"limits\": budget_limits,"` | — |
| [SRC-A8360B1B03-L000364](../../scripts/hosted_smoke_test.py#L364) | 364 | `"        \"counts\": budget_counts,"` | — |
| [SRC-A8360B1B03-L000365](../../scripts/hosted_smoke_test.py#L365) | 365 | `"        \"budget_exhausted\": False,"` | — |
| [SRC-A8360B1B03-L000366](../../scripts/hosted_smoke_test.py#L366) | 366 | `"        \"deadline_exceeded\": False,"` | — |
| [SRC-A8360B1B03-L000367](../../scripts/hosted_smoke_test.py#L367) | 367 | `"    }"` | — |
| [SRC-A8360B1B03-L000368](../../scripts/hosted_smoke_test.py#L368) | 368 | `"    if not isinstance(search_report, dict):"` | — |
| [SRC-A8360B1B03-L000369](../../scripts/hosted_smoke_test.py#L369) | 369 | `"        raise SmokeError(\"Agent request did not return a structured search report.\", partial_report)"` | — |
| [SRC-A8360B1B03-L000370](../../scripts/hosted_smoke_test.py#L370) | 370 | `"    pipeline_status = search_report.get(\"pipeline_completion_status\")"` | — |
| [SRC-A8360B1B03-L000371](../../scripts/hosted_smoke_test.py#L371) | 371 | `"    if pipeline_status != \"completed\":"` | — |
| [SRC-A8360B1B03-L000372](../../scripts/hosted_smoke_test.py#L372) | 372 | `"        raise SmokeError("` | — |
| [SRC-A8360B1B03-L000373](../../scripts/hosted_smoke_test.py#L373) | 373 | `"            f\"Agent research pipeline did not complete (status: {pipeline_status or 'missing'}).\","` | — |
| [SRC-A8360B1B03-L000374](../../scripts/hosted_smoke_test.py#L374) | 374 | `"            partial_report,"` | — |
| [SRC-A8360B1B03-L000375](../../scripts/hosted_smoke_test.py#L375) | 375 | `"        )"` | — |
| [SRC-A8360B1B03-L000376](../../scripts/hosted_smoke_test.py#L376) | 376 | `"    semantic_verification = search_report.get(\"semantic_claim_verification\")"` | — |
| [SRC-A8360B1B03-L000377](../../scripts/hosted_smoke_test.py#L377) | 377 | `"    semantic_status = ("` | — |
| [SRC-A8360B1B03-L000378](../../scripts/hosted_smoke_test.py#L378) | 378 | `"        semantic_verification.get(\"status\")"` | — |
| [SRC-A8360B1B03-L000379](../../scripts/hosted_smoke_test.py#L379) | 379 | `"        if isinstance(semantic_verification, dict) else None"` | — |
| [SRC-A8360B1B03-L000380](../../scripts/hosted_smoke_test.py#L380) | 380 | `"    )"` | — |
| [SRC-A8360B1B03-L000381](../../scripts/hosted_smoke_test.py#L381) | 381 | `"    if semantic_status not in {"` | — |
| [SRC-A8360B1B03-L000382](../../scripts/hosted_smoke_test.py#L382) | 382 | `"        \"completed_all_claims_supported\","` | — |
| [SRC-A8360B1B03-L000383](../../scripts/hosted_smoke_test.py#L383) | 383 | `"        \"completed_no_factual_claims\","` | — |
| [SRC-A8360B1B03-L000384](../../scripts/hosted_smoke_test.py#L384) | 384 | `"    }:"` | — |
| [SRC-A8360B1B03-L000385](../../scripts/hosted_smoke_test.py#L385) | 385 | `"        raise SmokeError("` | — |
| [SRC-A8360B1B03-L000386](../../scripts/hosted_smoke_test.py#L386) | 386 | `"            f\"Agent semantic claim-support review did not pass (status: {semantic_status or 'missing'}).\","` | — |
| [SRC-A8360B1B03-L000387](../../scripts/hosted_smoke_test.py#L387) | 387 | `"            partial_report,"` | — |
| [SRC-A8360B1B03-L000388](../../scripts/hosted_smoke_test.py#L388) | 388 | `"        )"` | — |
| [SRC-A8360B1B03-L000389](../../scripts/hosted_smoke_test.py#L389) | 389 | `"    if search_report.get(\"insufficient_evidence\") is not False:"` | — |
| [SRC-A8360B1B03-L000390](../../scripts/hosted_smoke_test.py#L390) | 390 | `"        raise SmokeError(\"Agent search report flags insufficient evidence or omits that check.\", partial_report)"` | — |
| [SRC-A8360B1B03-L000391](../../scripts/hosted_smoke_test.py#L391) | 391 | `"    if search_report.get(\"claim_audit_semantics\") != \"distinct_model_assessed_source_support_not_ground_truth\":"` | — |
| [SRC-A8360B1B03-L000392](../../scripts/hosted_smoke_test.py#L392) | 392 | `"        raise SmokeError(\"Agent claim-audit semantics are missing or not the expected source-support assessment.\", partial_report)"` | — |
| [SRC-A8360B1B03-L000393](../../scripts/hosted_smoke_test.py#L393) | 393 | `"    evidence_status = answer.get(\"answer_evidence_status\")"` | — |
| [SRC-A8360B1B03-L000394](../../scripts/hosted_smoke_test.py#L394) | 394 | `"    if evidence_status != \"citation_indices_validated_only\":"` | — |
| [SRC-A8360B1B03-L000395](../../scripts/hosted_smoke_test.py#L395) | 395 | `"        raise SmokeError("` | — |
| [SRC-A8360B1B03-L000396](../../scripts/hosted_smoke_test.py#L396) | 396 | `"            f\"Agent answer evidence status is not acceptable for hosted acceptance (status: {evidence_status or 'missing'}).\","` | — |
| [SRC-A8360B1B03-L000397](../../scripts/hosted_smoke_test.py#L397) | 397 | `"            partial_report,"` | — |
| [SRC-A8360B1B03-L000398](../../scripts/hosted_smoke_test.py#L398) | 398 | `"        )"` | — |
| [SRC-A8360B1B03-L000399](../../scripts/hosted_smoke_test.py#L399) | 399 | `"    checks[\"search\"] = {"` | — |
| [SRC-A8360B1B03-L000400](../../scripts/hosted_smoke_test.py#L400) | 400 | `"        \"status\": \"passed\","` | — |
| [SRC-A8360B1B03-L000401](../../scripts/hosted_smoke_test.py#L401) | 401 | `"        \"pages_fetched\": search_report.get(\"pages_fetched\", 0),"` | — |
| [SRC-A8360B1B03-L000402](../../scripts/hosted_smoke_test.py#L402) | 402 | `"        \"providers_reported\": search_report.get(\"providers_used\", []),"` | — |
| [SRC-A8360B1B03-L000403](../../scripts/hosted_smoke_test.py#L403) | 403 | `"        \"pipeline_completion_status\": pipeline_status,"` | — |
| [SRC-A8360B1B03-L000404](../../scripts/hosted_smoke_test.py#L404) | 404 | `"    }"` | — |
| [SRC-A8360B1B03-L000405](../../scripts/hosted_smoke_test.py#L405) | 405 | `"    checks[\"semantic_claim_support\"] = {"` | — |
| [SRC-A8360B1B03-L000406](../../scripts/hosted_smoke_test.py#L406) | 406 | `"        \"status\": \"passed\","` | — |
| [SRC-A8360B1B03-L000407](../../scripts/hosted_smoke_test.py#L407) | 407 | `"        \"verification_status\": semantic_status,"` | — |
| [SRC-A8360B1B03-L000408](../../scripts/hosted_smoke_test.py#L408) | 408 | `"        \"insufficient_evidence\": False,"` | — |
| [SRC-A8360B1B03-L000409](../../scripts/hosted_smoke_test.py#L409) | 409 | `"        \"semantics\": \"model_assessed_source_support_not_ground_truth\","` | — |
| [SRC-A8360B1B03-L000410](../../scripts/hosted_smoke_test.py#L410) | 410 | `"    }"` | — |
| [SRC-A8360B1B03-L000411](../../scripts/hosted_smoke_test.py#L411) | 411 | `"    checks[\"language_model\"] = {"` | — |
| [SRC-A8360B1B03-L000412](../../scripts/hosted_smoke_test.py#L412) | 412 | `"        \"status\": \"passed\","` | — |
| [SRC-A8360B1B03-L000413](../../scripts/hosted_smoke_test.py#L413) | 413 | `"        \"response_received\": True,"` | — |
| [SRC-A8360B1B03-L000414](../../scripts/hosted_smoke_test.py#L414) | 414 | `"        \"verified_by\": \"agent_request\","` | — |
| [SRC-A8360B1B03-L000415](../../scripts/hosted_smoke_test.py#L415) | 415 | `"    }"` | — |
| [SRC-A8360B1B03-L000416](../../scripts/hosted_smoke_test.py#L416) | 416 | `"    checks[\"agent_request\"] = {"` | — |
| [SRC-A8360B1B03-L000417](../../scripts/hosted_smoke_test.py#L417) | 417 | `"        \"status\": \"passed\", \"source_count\": len(usable),"` | — |
| [SRC-A8360B1B03-L000418](../../scripts/hosted_smoke_test.py#L418) | 418 | `"        \"direct_pages_read\": search_report.get(\"pages_fetched\"),"` | — |
| [SRC-A8360B1B03-L000419](../../scripts/hosted_smoke_test.py#L419) | 419 | `"        \"providers_reported\": search_report.get(\"providers_used\", []),"` | — |
| [SRC-A8360B1B03-L000420](../../scripts/hosted_smoke_test.py#L420) | 420 | `"        \"answer_received\": True,"` | — |
| [SRC-A8360B1B03-L000421](../../scripts/hosted_smoke_test.py#L421) | 421 | `"        \"pipeline_completion_status\": pipeline_status,"` | — |
| [SRC-A8360B1B03-L000422](../../scripts/hosted_smoke_test.py#L422) | 422 | `"        \"answer_evidence_status\": evidence_status,"` | — |
| [SRC-A8360B1B03-L000423](../../scripts/hosted_smoke_test.py#L423) | 423 | `"    }"` | — |
| [SRC-A8360B1B03-L000424](../../scripts/hosted_smoke_test.py#L424) | 424 | `"    partial_report.update({"` | — |
| [SRC-A8360B1B03-L000425](../../scripts/hosted_smoke_test.py#L425) | 425 | `"        \"result\": \"passed\","` | — |
| [SRC-A8360B1B03-L000426](../../scripts/hosted_smoke_test.py#L426) | 426 | `"        \"checks\": checks,"` | — |
| [SRC-A8360B1B03-L000427](../../scripts/hosted_smoke_test.py#L427) | 427 | `"        \"note\": ("` | — |
| [SRC-A8360B1B03-L000428](../../scripts/hosted_smoke_test.py#L428) | 428 | `"            \"Transcript contains the exact fixed test question, answer, and returned source metadata. \""` | — |
| [SRC-A8360B1B03-L000429](../../scripts/hosted_smoke_test.py#L429) | 429 | `"            \"This proves the request path worked at test time, not continuous uptime. The approved \""` | — |
| [SRC-A8360B1B03-L000430](../../scripts/hosted_smoke_test.py#L430) | 430 | `"            \"live phase makes one authenticated agent request; that request may fan out to multiple \""` | — |
| [SRC-A8360B1B03-L000431](../../scripts/hosted_smoke_test.py#L431) | 431 | `"            \"configured search providers. The server enforces at most 3 planned queries, 12 provider requests, \""` | — |
| [SRC-A8360B1B03-L000432](../../scripts/hosted_smoke_test.py#L432) | 432 | `"            \"6 model calls, 4 page fetches, and zero external tool calls for this smoke profile; \""` | — |
| [SRC-A8360B1B03-L000433](../../scripts/hosted_smoke_test.py#L433) | 433 | `"            \"operator settings may be stricter. Provider usage may incur charges.\""` | — |
| [SRC-A8360B1B03-L000434](../../scripts/hosted_smoke_test.py#L434) | 434 | `"        ),"` | — |
| [SRC-A8360B1B03-L000435](../../scripts/hosted_smoke_test.py#L435) | 435 | `"    })"` | — |
| [SRC-A8360B1B03-L000436](../../scripts/hosted_smoke_test.py#L436) | 436 | `"    return partial_report"` | — |
| [SRC-A8360B1B03-L000437](../../scripts/hosted_smoke_test.py#L437) | 437 | `""` | — |
| [SRC-A8360B1B03-L000438](../../scripts/hosted_smoke_test.py#L438) | 438 | `""` | — |
| [SRC-A8360B1B03-L000439](../../scripts/hosted_smoke_test.py#L439) | 439 | `"def main() -> int:"` | — |
| [SRC-A8360B1B03-L000440](../../scripts/hosted_smoke_test.py#L440) | 440 | `"    parser = argparse.ArgumentParser(description=\"Run live acceptance checks against hosted Omarai.\")"` | — |
| [SRC-A8360B1B03-L000441](../../scripts/hosted_smoke_test.py#L441) | 441 | `"    parser.add_argument(\"--base-url\", default=os.getenv(\"OMARAI_BASE_URL\", \"\"))"` | — |
| [SRC-A8360B1B03-L000442](../../scripts/hosted_smoke_test.py#L442) | 442 | `"    parser.add_argument(\"--timeout\", type=float, default=90)"` | — |
| [SRC-A8360B1B03-L000443](../../scripts/hosted_smoke_test.py#L443) | 443 | `"    parser.add_argument("` | — |
| [SRC-A8360B1B03-L000444](../../scripts/hosted_smoke_test.py#L444) | 444 | `"        \"--expected-sha\","` | — |
| [SRC-A8360B1B03-L000445](../../scripts/hosted_smoke_test.py#L445) | 445 | `"        default=os.getenv(\"OMARAI_EXPECTED_BUILD_SHA\", \"\"),"` | — |
| [SRC-A8360B1B03-L000446](../../scripts/hosted_smoke_test.py#L446) | 446 | `"        help=\"Require the deployed image to report this full 40-character source Git SHA.\","` | — |
| [SRC-A8360B1B03-L000447](../../scripts/hosted_smoke_test.py#L447) | 447 | `"    )"` | — |
| [SRC-A8360B1B03-L000448](../../scripts/hosted_smoke_test.py#L448) | 448 | `"    parser.add_argument(\"--allow-http\", action=\"store_true\","` | — |
| [SRC-A8360B1B03-L000449](../../scripts/hosted_smoke_test.py#L449) | 449 | `"                        help=\"Allow HTTP only for localhost/127.0.0.1/::1 testing.\")"` | — |
| [SRC-A8360B1B03-L000450](../../scripts/hosted_smoke_test.py#L450) | 450 | `"    parser.add_argument("` | — |
| [SRC-A8360B1B03-L000451](../../scripts/hosted_smoke_test.py#L451) | 451 | `"        \"--local-dev-no-token\","` | — |
| [SRC-A8360B1B03-L000452](../../scripts/hosted_smoke_test.py#L452) | 452 | `"        action=\"store_true\","` | — |
| [SRC-A8360B1B03-L000453](../../scripts/hosted_smoke_test.py#L453) | 453 | `"        help=\"Use the app's existing no-token development bypass on loopback only; never for hosted URLs.\","` | — |
| [SRC-A8360B1B03-L000454](../../scripts/hosted_smoke_test.py#L454) | 454 | `"    )"` | — |
| [SRC-A8360B1B03-L000455](../../scripts/hosted_smoke_test.py#L455) | 455 | `"    parser.add_argument("` | — |
| [SRC-A8360B1B03-L000456](../../scripts/hosted_smoke_test.py#L456) | 456 | `"        \"--allow-provider-usage\","` | — |
| [SRC-A8360B1B03-L000457](../../scripts/hosted_smoke_test.py#L457) | 457 | `"        action=\"store_true\","` | — |
| [SRC-A8360B1B03-L000458](../../scripts/hosted_smoke_test.py#L458) | 458 | `"        help=("` | — |
| [SRC-A8360B1B03-L000459](../../scripts/hosted_smoke_test.py#L459) | 459 | `"            \"Explicitly authorize one live agent request under the server-enforced hosted_smoke \""` | — |
| [SRC-A8360B1B03-L000460](../../scripts/hosted_smoke_test.py#L460) | 460 | `"            \"budget: up to 3 planned queries, 12 provider requests, 6 model calls, 4 page fetches, \""` | — |
| [SRC-A8360B1B03-L000461](../../scripts/hosted_smoke_test.py#L461) | 461 | `"            \"and zero external tool calls. Operator settings may be stricter.\""` | — |
| [SRC-A8360B1B03-L000462](../../scripts/hosted_smoke_test.py#L462) | 462 | `"        ),"` | — |
| [SRC-A8360B1B03-L000463](../../scripts/hosted_smoke_test.py#L463) | 463 | `"    )"` | — |
| [SRC-A8360B1B03-L000464](../../scripts/hosted_smoke_test.py#L464) | 464 | `"    parser.add_argument("` | — |
| [SRC-A8360B1B03-L000465](../../scripts/hosted_smoke_test.py#L465) | 465 | `"        \"--preflight-only\","` | — |
| [SRC-A8360B1B03-L000466](../../scripts/hosted_smoke_test.py#L466) | 466 | `"        action=\"store_true\","` | — |
| [SRC-A8360B1B03-L000467](../../scripts/hosted_smoke_test.py#L467) | 467 | `"        help=\"Run health/build/authentication checks only; never call search providers or a language model.\","` | — |
| [SRC-A8360B1B03-L000468](../../scripts/hosted_smoke_test.py#L468) | 468 | `"    )"` | — |
| [SRC-A8360B1B03-L000469](../../scripts/hosted_smoke_test.py#L469) | 469 | `"    parser.add_argument("` | — |
| [SRC-A8360B1B03-L000470](../../scripts/hosted_smoke_test.py#L470) | 470 | `"        \"--output\","` | — |
| [SRC-A8360B1B03-L000471](../../scripts/hosted_smoke_test.py#L471) | 471 | `"        default=\"\","` | — |
| [SRC-A8360B1B03-L000472](../../scripts/hosted_smoke_test.py#L472) | 472 | `"        help=\"Optional path for a JSON report containing the exact test question, answer, and sources.\","` | — |
| [SRC-A8360B1B03-L000473](../../scripts/hosted_smoke_test.py#L473) | 473 | `"    )"` | — |
| [SRC-A8360B1B03-L000474](../../scripts/hosted_smoke_test.py#L474) | 474 | `"    args = parser.parse_args()"` | — |
| [SRC-A8360B1B03-L000475](../../scripts/hosted_smoke_test.py#L475) | 475 | `"    try:"` | — |
| [SRC-A8360B1B03-L000476](../../scripts/hosted_smoke_test.py#L476) | 476 | `"        result = run_smoke("` | — |
| [SRC-A8360B1B03-L000477](../../scripts/hosted_smoke_test.py#L477) | 477 | `"            args.base_url,"` | — |
| [SRC-A8360B1B03-L000478](../../scripts/hosted_smoke_test.py#L478) | 478 | `"            os.getenv(\"OMARAI_ACCESS_TOKEN\", \"\").strip(),"` | — |
| [SRC-A8360B1B03-L000479](../../scripts/hosted_smoke_test.py#L479) | 479 | `"            timeout=max(5, min(args.timeout, 240)),"` | — |
| [SRC-A8360B1B03-L000480](../../scripts/hosted_smoke_test.py#L480) | 480 | `"            allow_http=args.allow_http,"` | — |
| [SRC-A8360B1B03-L000481](../../scripts/hosted_smoke_test.py#L481) | 481 | `"            expected_sha=args.expected_sha or None,"` | — |
| [SRC-A8360B1B03-L000482](../../scripts/hosted_smoke_test.py#L482) | 482 | `"            local_dev_no_token=args.local_dev_no_token,"` | — |
| [SRC-A8360B1B03-L000483](../../scripts/hosted_smoke_test.py#L483) | 483 | `"            allow_provider_usage=args.allow_provider_usage,"` | — |
| [SRC-A8360B1B03-L000484](../../scripts/hosted_smoke_test.py#L484) | 484 | `"            preflight_only=args.preflight_only,"` | — |
| [SRC-A8360B1B03-L000485](../../scripts/hosted_smoke_test.py#L485) | 485 | `"        )"` | — |
| [SRC-A8360B1B03-L000486](../../scripts/hosted_smoke_test.py#L486) | 486 | `"    except SmokeError as exc:"` | — |
| [SRC-A8360B1B03-L000487](../../scripts/hosted_smoke_test.py#L487) | 487 | `"        failed_report = {**exc.report, \"result\": \"failed\", \"error\": str(exc)}"` | — |
| [SRC-A8360B1B03-L000488](../../scripts/hosted_smoke_test.py#L488) | 488 | `"        rendered = json.dumps(failed_report, ensure_ascii=False, indent=2)"` | — |
| [SRC-A8360B1B03-L000489](../../scripts/hosted_smoke_test.py#L489) | 489 | `"        if args.output:"` | — |
| [SRC-A8360B1B03-L000490](../../scripts/hosted_smoke_test.py#L490) | 490 | `"            output_path = Path(args.output)"` | — |
| [SRC-A8360B1B03-L000491](../../scripts/hosted_smoke_test.py#L491) | 491 | `"            output_path.parent.mkdir(parents=True, exist_ok=True)"` | — |
| [SRC-A8360B1B03-L000492](../../scripts/hosted_smoke_test.py#L492) | 492 | `"            output_path.write_text(rendered + \"\\n\", encoding=\"utf-8\")"` | — |
| [SRC-A8360B1B03-L000493](../../scripts/hosted_smoke_test.py#L493) | 493 | `"        print(rendered)"` | — |
| [SRC-A8360B1B03-L000494](../../scripts/hosted_smoke_test.py#L494) | 494 | `"        return 1"` | — |
| [SRC-A8360B1B03-L000495](../../scripts/hosted_smoke_test.py#L495) | 495 | `"    rendered = json.dumps(result, ensure_ascii=False, indent=2)"` | — |
| [SRC-A8360B1B03-L000496](../../scripts/hosted_smoke_test.py#L496) | 496 | `"    if args.output:"` | — |
| [SRC-A8360B1B03-L000497](../../scripts/hosted_smoke_test.py#L497) | 497 | `"        output_path = Path(args.output)"` | — |
| [SRC-A8360B1B03-L000498](../../scripts/hosted_smoke_test.py#L498) | 498 | `"        output_path.parent.mkdir(parents=True, exist_ok=True)"` | — |
| [SRC-A8360B1B03-L000499](../../scripts/hosted_smoke_test.py#L499) | 499 | `"        output_path.write_text(rendered + \"\\n\", encoding=\"utf-8\")"` | — |
| [SRC-A8360B1B03-L000500](../../scripts/hosted_smoke_test.py#L500) | 500 | `"    print(rendered)"` | — |
| [SRC-A8360B1B03-L000501](../../scripts/hosted_smoke_test.py#L501) | 501 | `"    return 0"` | — |
| [SRC-A8360B1B03-L000502](../../scripts/hosted_smoke_test.py#L502) | 502 | `""` | — |
| [SRC-A8360B1B03-L000503](../../scripts/hosted_smoke_test.py#L503) | 503 | `""` | — |
| [SRC-A8360B1B03-L000504](../../scripts/hosted_smoke_test.py#L504) | 504 | `"if __name__ == \"__main__\":"` | — |
| [SRC-A8360B1B03-L000505](../../scripts/hosted_smoke_test.py#L505) | 505 | `"    sys.exit(main())"` | — |
## ملفات أخرى

### FILE-4FFD5AFC54 — [scripts/run_answer_quality_benchmark.py](../../scripts/run_answer_quality_benchmark.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-4FFD5AFC54-L000001](../../scripts/run_answer_quality_benchmark.py#L1) | 1 | `"\"\"\"Offline / optional live runner for OMARAI-REDTEAM-001 answer-quality cases."` | — |
| [SRC-4FFD5AFC54-L000002](../../scripts/run_answer_quality_benchmark.py#L2) | 2 | `""` | — |
| [SRC-4FFD5AFC54-L000003](../../scripts/run_answer_quality_benchmark.py#L3) | 3 | `"Modes"` | — |
| [SRC-4FFD5AFC54-L000004](../../scripts/run_answer_quality_benchmark.py#L4) | 4 | `"-----"` | — |
| [SRC-4FFD5AFC54-L000005](../../scripts/run_answer_quality_benchmark.py#L5) | 5 | `"validate (default)"` | — |
| [SRC-4FFD5AFC54-L000006](../../scripts/run_answer_quality_benchmark.py#L6) | 6 | `"    Load and structurally validate the corpus. No network."` | — |
| [SRC-4FFD5AFC54-L000007](../../scripts/run_answer_quality_benchmark.py#L7) | 7 | `""` | — |
| [SRC-4FFD5AFC54-L000008](../../scripts/run_answer_quality_benchmark.py#L8) | 8 | `"live (explicit opt-in)"` | — |
| [SRC-4FFD5AFC54-L000009](../../scripts/run_answer_quality_benchmark.py#L9) | 9 | `"    POST selected cases to an existing Omarai HTTP API (/api/agent)."` | — |
| [SRC-4FFD5AFC54-L000010](../../scripts/run_answer_quality_benchmark.py#L10) | 10 | `"    Does NOT inject JSON evidence fixtures into the server."` | — |
| [SRC-4FFD5AFC54-L000011](../../scripts/run_answer_quality_benchmark.py#L11) | 11 | `"    Does NOT auto-grade PASS/FAIL for answer quality; records NOT_TESTED"` | — |
| [SRC-4FFD5AFC54-L000012](../../scripts/run_answer_quality_benchmark.py#L12) | 12 | `"    unless a transport/auth error makes the run unusable."` | — |
| [SRC-4FFD5AFC54-L000013](../../scripts/run_answer_quality_benchmark.py#L13) | 13 | `""` | — |
| [SRC-4FFD5AFC54-L000014](../../scripts/run_answer_quality_benchmark.py#L14) | 14 | `"Standard library only. Secrets only via environment (never CLI flags for tokens)."` | — |
| [SRC-4FFD5AFC54-L000015](../../scripts/run_answer_quality_benchmark.py#L15) | 15 | `""` | — |
| [SRC-4FFD5AFC54-L000016](../../scripts/run_answer_quality_benchmark.py#L16) | 16 | `"Examples"` | — |
| [SRC-4FFD5AFC54-L000017](../../scripts/run_answer_quality_benchmark.py#L17) | 17 | `"--------"` | — |
| [SRC-4FFD5AFC54-L000018](../../scripts/run_answer_quality_benchmark.py#L18) | 18 | `"  python scripts/run_answer_quality_benchmark.py"` | — |
| [SRC-4FFD5AFC54-L000019](../../scripts/run_answer_quality_benchmark.py#L19) | 19 | `"  python scripts/run_answer_quality_benchmark.py --mode validate --summary"` | — |
| [SRC-4FFD5AFC54-L000020](../../scripts/run_answer_quality_benchmark.py#L20) | 20 | `"  python scripts/run_answer_quality_benchmark.py --mode live --base-url http://127.0.0.1:8765 \\\\"` | — |
| [SRC-4FFD5AFC54-L000021](../../scripts/run_answer_quality_benchmark.py#L21) | 21 | `"      --case-id AQ-001 --limit 1 --out /tmp/aq_results.json"` | — |
| [SRC-4FFD5AFC54-L000022](../../scripts/run_answer_quality_benchmark.py#L22) | 22 | `"\"\"\""` | — |
| [SRC-4FFD5AFC54-L000023](../../scripts/run_answer_quality_benchmark.py#L23) | 23 | `"from __future__ import annotations"` | — |
| [SRC-4FFD5AFC54-L000024](../../scripts/run_answer_quality_benchmark.py#L24) | 24 | `""` | — |
| [SRC-4FFD5AFC54-L000025](../../scripts/run_answer_quality_benchmark.py#L25) | 25 | `"import argparse"` | — |
| [SRC-4FFD5AFC54-L000026](../../scripts/run_answer_quality_benchmark.py#L26) | 26 | `"import ipaddress"` | — |
| [SRC-4FFD5AFC54-L000027](../../scripts/run_answer_quality_benchmark.py#L27) | 27 | `"import json"` | — |
| [SRC-4FFD5AFC54-L000028](../../scripts/run_answer_quality_benchmark.py#L28) | 28 | `"import math"` | — |
| [SRC-4FFD5AFC54-L000029](../../scripts/run_answer_quality_benchmark.py#L29) | 29 | `"import os"` | — |
| [SRC-4FFD5AFC54-L000030](../../scripts/run_answer_quality_benchmark.py#L30) | 30 | `"import re"` | — |
| [SRC-4FFD5AFC54-L000031](../../scripts/run_answer_quality_benchmark.py#L31) | 31 | `"import sys"` | — |
| [SRC-4FFD5AFC54-L000032](../../scripts/run_answer_quality_benchmark.py#L32) | 32 | `"import time"` | — |
| [SRC-4FFD5AFC54-L000033](../../scripts/run_answer_quality_benchmark.py#L33) | 33 | `"import urllib.error"` | — |
| [SRC-4FFD5AFC54-L000034](../../scripts/run_answer_quality_benchmark.py#L34) | 34 | `"import urllib.parse"` | — |
| [SRC-4FFD5AFC54-L000035](../../scripts/run_answer_quality_benchmark.py#L35) | 35 | `"import urllib.request"` | — |
| [SRC-4FFD5AFC54-L000036](../../scripts/run_answer_quality_benchmark.py#L36) | 36 | `"from datetime import UTC, datetime"` | — |
| [SRC-4FFD5AFC54-L000037](../../scripts/run_answer_quality_benchmark.py#L37) | 37 | `"from pathlib import Path"` | — |
| [SRC-4FFD5AFC54-L000038](../../scripts/run_answer_quality_benchmark.py#L38) | 38 | `""` | — |
| [SRC-4FFD5AFC54-L000039](../../scripts/run_answer_quality_benchmark.py#L39) | 39 | `"ROOT = Path(__file__).resolve().parents[1]"` | — |
| [SRC-4FFD5AFC54-L000040](../../scripts/run_answer_quality_benchmark.py#L40) | 40 | `"DEFAULT_CORPUS = ROOT / \"tests\" / \"fixtures\" / \"answer_quality_cases.json\""` | — |
| [SRC-4FFD5AFC54-L000041](../../scripts/run_answer_quality_benchmark.py#L41) | 41 | `"MAX_RESPONSE_BYTES = 2_000_000"` | — |
| [SRC-4FFD5AFC54-L000042](../../scripts/run_answer_quality_benchmark.py#L42) | 42 | `""` | — |
| [SRC-4FFD5AFC54-L000043](../../scripts/run_answer_quality_benchmark.py#L43) | 43 | `""` | — |
| [SRC-4FFD5AFC54-L000044](../../scripts/run_answer_quality_benchmark.py#L44) | 44 | `"def _load_request_cost_ledger(path: Path \| None, valid_case_ids: set[str]) -> tuple[dict[str, float], str \| None]:"` | — |
| [SRC-4FFD5AFC54-L000045](../../scripts/run_answer_quality_benchmark.py#L45) | 45 | `"    \"\"\"Load reconciled, externally sourced whole-request USD costs; never estimate them.\"\"\""` | — |
| [SRC-4FFD5AFC54-L000046](../../scripts/run_answer_quality_benchmark.py#L46) | 46 | `"    if path is None:"` | — |
| [SRC-4FFD5AFC54-L000047](../../scripts/run_answer_quality_benchmark.py#L47) | 47 | `"        return {}, None"` | — |
| [SRC-4FFD5AFC54-L000048](../../scripts/run_answer_quality_benchmark.py#L48) | 48 | `"    ledger = json.loads(path.read_text(encoding=\"utf-8\"))"` | — |
| [SRC-4FFD5AFC54-L000049](../../scripts/run_answer_quality_benchmark.py#L49) | 49 | `"    if not isinstance(ledger, dict):"` | — |
| [SRC-4FFD5AFC54-L000050](../../scripts/run_answer_quality_benchmark.py#L50) | 50 | `"        raise ValueError(\"request-cost ledger root must be an object\")"` | — |
| [SRC-4FFD5AFC54-L000051](../../scripts/run_answer_quality_benchmark.py#L51) | 51 | `"    if ledger.get(\"currency\") != \"USD\" or ledger.get(\"scope\") != \"complete_request\":"` | — |
| [SRC-4FFD5AFC54-L000052](../../scripts/run_answer_quality_benchmark.py#L52) | 52 | `"        raise ValueError(\"request-cost ledger must declare currency=USD and scope=complete_request\")"` | — |
| [SRC-4FFD5AFC54-L000053](../../scripts/run_answer_quality_benchmark.py#L53) | 53 | `"    source = ledger.get(\"source\")"` | — |
| [SRC-4FFD5AFC54-L000054](../../scripts/run_answer_quality_benchmark.py#L54) | 54 | `"    if not isinstance(source, str) or not source.strip():"` | — |
| [SRC-4FFD5AFC54-L000055](../../scripts/run_answer_quality_benchmark.py#L55) | 55 | `"        raise ValueError(\"request-cost ledger needs a non-empty source describing the reconciliation\")"` | — |
| [SRC-4FFD5AFC54-L000056](../../scripts/run_answer_quality_benchmark.py#L56) | 56 | `"    entries = ledger.get(\"costs\")"` | — |
| [SRC-4FFD5AFC54-L000057](../../scripts/run_answer_quality_benchmark.py#L57) | 57 | `"    if not isinstance(entries, list):"` | — |
| [SRC-4FFD5AFC54-L000058](../../scripts/run_answer_quality_benchmark.py#L58) | 58 | `"        raise ValueError(\"request-cost ledger must contain a costs array\")"` | — |
| [SRC-4FFD5AFC54-L000059](../../scripts/run_answer_quality_benchmark.py#L59) | 59 | `"    costs: dict[str, float] = {}"` | — |
| [SRC-4FFD5AFC54-L000060](../../scripts/run_answer_quality_benchmark.py#L60) | 60 | `"    for index, entry in enumerate(entries):"` | — |
| [SRC-4FFD5AFC54-L000061](../../scripts/run_answer_quality_benchmark.py#L61) | 61 | `"        if not isinstance(entry, dict):"` | — |
| [SRC-4FFD5AFC54-L000062](../../scripts/run_answer_quality_benchmark.py#L62) | 62 | `"            raise ValueError(f\"request-cost ledger costs[{index}] must be an object\")"` | — |
| [SRC-4FFD5AFC54-L000063](../../scripts/run_answer_quality_benchmark.py#L63) | 63 | `"        case_id = entry.get(\"case_id\")"` | — |
| [SRC-4FFD5AFC54-L000064](../../scripts/run_answer_quality_benchmark.py#L64) | 64 | `"        if not isinstance(case_id, str) or case_id not in valid_case_ids:"` | — |
| [SRC-4FFD5AFC54-L000065](../../scripts/run_answer_quality_benchmark.py#L65) | 65 | `"            raise ValueError(f\"request-cost ledger costs[{index}] has an unknown case_id\")"` | — |
| [SRC-4FFD5AFC54-L000066](../../scripts/run_answer_quality_benchmark.py#L66) | 66 | `"        if case_id in costs:"` | — |
| [SRC-4FFD5AFC54-L000067](../../scripts/run_answer_quality_benchmark.py#L67) | 67 | `"            raise ValueError(f\"request-cost ledger has duplicate case_id {case_id}\")"` | — |
| [SRC-4FFD5AFC54-L000068](../../scripts/run_answer_quality_benchmark.py#L68) | 68 | `"        value = _finite_nonnegative_number(entry.get(\"cost_usd\"))"` | — |
| [SRC-4FFD5AFC54-L000069](../../scripts/run_answer_quality_benchmark.py#L69) | 69 | `"        if value is None:"` | — |
| [SRC-4FFD5AFC54-L000070](../../scripts/run_answer_quality_benchmark.py#L70) | 70 | `"            raise ValueError(f\"request-cost ledger {case_id} cost_usd must be finite and non-negative\")"` | — |
| [SRC-4FFD5AFC54-L000071](../../scripts/run_answer_quality_benchmark.py#L71) | 71 | `"        costs[case_id] = value"` | — |
| [SRC-4FFD5AFC54-L000072](../../scripts/run_answer_quality_benchmark.py#L72) | 72 | `"    return costs, source.strip()"` | — |
| [SRC-4FFD5AFC54-L000073](../../scripts/run_answer_quality_benchmark.py#L73) | 73 | `""` | — |
| [SRC-4FFD5AFC54-L000074](../../scripts/run_answer_quality_benchmark.py#L74) | 74 | `""` | — |
| [SRC-4FFD5AFC54-L000075](../../scripts/run_answer_quality_benchmark.py#L75) | 75 | `"def _model_calls_from_payload(payload: dict) -> list[dict]:"` | — |
| [SRC-4FFD5AFC54-L000076](../../scripts/run_answer_quality_benchmark.py#L76) | 76 | `"    \"\"\"Read only structured per-request model-call metadata from an API response.\"\"\""` | — |
| [SRC-4FFD5AFC54-L000077](../../scripts/run_answer_quality_benchmark.py#L77) | 77 | `"    report = payload.get(\"search_report\")"` | — |
| [SRC-4FFD5AFC54-L000078](../../scripts/run_answer_quality_benchmark.py#L78) | 78 | `"    understanding = payload.get(\"task_understanding\")"` | — |
| [SRC-4FFD5AFC54-L000079](../../scripts/run_answer_quality_benchmark.py#L79) | 79 | `"    candidates = ["` | — |
| [SRC-4FFD5AFC54-L000080](../../scripts/run_answer_quality_benchmark.py#L80) | 80 | `"        payload.get(\"model_calls\"),"` | — |
| [SRC-4FFD5AFC54-L000081](../../scripts/run_answer_quality_benchmark.py#L81) | 81 | `"        report.get(\"model_calls\") if isinstance(report, dict) else None,"` | — |
| [SRC-4FFD5AFC54-L000082](../../scripts/run_answer_quality_benchmark.py#L82) | 82 | `"        understanding.get(\"model_calls\") if isinstance(understanding, dict) else None,"` | — |
| [SRC-4FFD5AFC54-L000083](../../scripts/run_answer_quality_benchmark.py#L83) | 83 | `"    ]"` | — |
| [SRC-4FFD5AFC54-L000084](../../scripts/run_answer_quality_benchmark.py#L84) | 84 | `"    for candidate in candidates:"` | — |
| [SRC-4FFD5AFC54-L000085](../../scripts/run_answer_quality_benchmark.py#L85) | 85 | `"        if isinstance(candidate, list) and candidate:"` | — |
| [SRC-4FFD5AFC54-L000086](../../scripts/run_answer_quality_benchmark.py#L86) | 86 | `"            return [item for item in candidate if isinstance(item, dict)]"` | — |
| [SRC-4FFD5AFC54-L000087](../../scripts/run_answer_quality_benchmark.py#L87) | 87 | `"    return []"` | — |
| [SRC-4FFD5AFC54-L000088](../../scripts/run_answer_quality_benchmark.py#L88) | 88 | `""` | — |
| [SRC-4FFD5AFC54-L000089](../../scripts/run_answer_quality_benchmark.py#L89) | 89 | `""` | — |
| [SRC-4FFD5AFC54-L000090](../../scripts/run_answer_quality_benchmark.py#L90) | 90 | `"def _finite_nonnegative_number(value) -> float \| None:"` | — |
| [SRC-4FFD5AFC54-L000091](../../scripts/run_answer_quality_benchmark.py#L91) | 91 | `"    if isinstance(value, bool) or not isinstance(value, (int, float)):"` | — |
| [SRC-4FFD5AFC54-L000092](../../scripts/run_answer_quality_benchmark.py#L92) | 92 | `"        return None"` | — |
| [SRC-4FFD5AFC54-L000093](../../scripts/run_answer_quality_benchmark.py#L93) | 93 | `"    number = float(value)"` | — |
| [SRC-4FFD5AFC54-L000094](../../scripts/run_answer_quality_benchmark.py#L94) | 94 | `"    if not math.isfinite(number) or number < 0:"` | — |
| [SRC-4FFD5AFC54-L000095](../../scripts/run_answer_quality_benchmark.py#L95) | 95 | `"        return None"` | — |
| [SRC-4FFD5AFC54-L000096](../../scripts/run_answer_quality_benchmark.py#L96) | 96 | `"    return number"` | — |
| [SRC-4FFD5AFC54-L000097](../../scripts/run_answer_quality_benchmark.py#L97) | 97 | `""` | — |
| [SRC-4FFD5AFC54-L000098](../../scripts/run_answer_quality_benchmark.py#L98) | 98 | `""` | — |
| [SRC-4FFD5AFC54-L000099](../../scripts/run_answer_quality_benchmark.py#L99) | 99 | `"def _response_metrics(payload: dict \| str, expected_strategy: str, transport_ok: bool) -> dict:"` | — |
| [SRC-4FFD5AFC54-L000100](../../scripts/run_answer_quality_benchmark.py#L100) | 100 | `"    \"\"\"Derive conservative telemetry; never infer semantic correctness from HTTP 200.\"\"\""` | — |
| [SRC-4FFD5AFC54-L000101](../../scripts/run_answer_quality_benchmark.py#L101) | 101 | `"    if not isinstance(payload, dict):"` | — |
| [SRC-4FFD5AFC54-L000102](../../scripts/run_answer_quality_benchmark.py#L102) | 102 | `"        payload = {}"` | — |
| [SRC-4FFD5AFC54-L000103](../../scripts/run_answer_quality_benchmark.py#L103) | 103 | `"    report = payload.get(\"search_report\")"` | — |
| [SRC-4FFD5AFC54-L000104](../../scripts/run_answer_quality_benchmark.py#L104) | 104 | `"    report = report if isinstance(report, dict) else {}"` | — |
| [SRC-4FFD5AFC54-L000105](../../scripts/run_answer_quality_benchmark.py#L105) | 105 | `"    outcome = report.get(\"search_outcome\")"` | — |
| [SRC-4FFD5AFC54-L000106](../../scripts/run_answer_quality_benchmark.py#L106) | 106 | `"    pipeline = report.get(\"pipeline_completion_status\")"` | — |
| [SRC-4FFD5AFC54-L000107](../../scripts/run_answer_quality_benchmark.py#L107) | 107 | `"    source_rows = payload.get(\"sources\")"` | — |
| [SRC-4FFD5AFC54-L000108](../../scripts/run_answer_quality_benchmark.py#L108) | 108 | `"    source_rows_known = isinstance(source_rows, list)"` | — |
| [SRC-4FFD5AFC54-L000109](../../scripts/run_answer_quality_benchmark.py#L109) | 109 | `"    source_count = len(source_rows) if source_rows_known else None"` | — |
| [SRC-4FFD5AFC54-L000110](../../scripts/run_answer_quality_benchmark.py#L110) | 110 | `"    if expected_strategy != \"web_search\":"` | — |
| [SRC-4FFD5AFC54-L000111](../../scripts/run_answer_quality_benchmark.py#L111) | 111 | `"        tool_status = \"NOT_APPLICABLE\""` | — |
| [SRC-4FFD5AFC54-L000112](../../scripts/run_answer_quality_benchmark.py#L112) | 112 | `"    elif not transport_ok:"` | — |
| [SRC-4FFD5AFC54-L000113](../../scripts/run_answer_quality_benchmark.py#L113) | 113 | `"        tool_status = \"TRANSPORT_FAILED\""` | — |
| [SRC-4FFD5AFC54-L000114](../../scripts/run_answer_quality_benchmark.py#L114) | 114 | `"    elif outcome == \"attempted_with_usable_sources\":"` | — |
| [SRC-4FFD5AFC54-L000115](../../scripts/run_answer_quality_benchmark.py#L115) | 115 | `"        if source_count is None:"` | — |
| [SRC-4FFD5AFC54-L000116](../../scripts/run_answer_quality_benchmark.py#L116) | 116 | `"            tool_status = \"UNKNOWN_SOURCE_COUNT\""` | — |
| [SRC-4FFD5AFC54-L000117](../../scripts/run_answer_quality_benchmark.py#L117) | 117 | `"        elif source_count == 0:"` | — |
| [SRC-4FFD5AFC54-L000118](../../scripts/run_answer_quality_benchmark.py#L118) | 118 | `"            tool_status = \"INCONSISTENT_SEARCH_OUTCOME_NO_RETURNED_SOURCES\""` | — |
| [SRC-4FFD5AFC54-L000119](../../scripts/run_answer_quality_benchmark.py#L119) | 119 | `"        else:"` | — |
| [SRC-4FFD5AFC54-L000120](../../scripts/run_answer_quality_benchmark.py#L120) | 120 | `"            tool_status = \"SUCCESS_WITH_USABLE_RESULTS\""` | — |
| [SRC-4FFD5AFC54-L000121](../../scripts/run_answer_quality_benchmark.py#L121) | 121 | `"    elif outcome == \"attempted_no_usable_sources\":"` | — |
| [SRC-4FFD5AFC54-L000122](../../scripts/run_answer_quality_benchmark.py#L122) | 122 | `"        if source_count is not None and source_count > 0:"` | — |
| [SRC-4FFD5AFC54-L000123](../../scripts/run_answer_quality_benchmark.py#L123) | 123 | `"            tool_status = \"INCONSISTENT_SEARCH_OUTCOME_WITH_RETURNED_SOURCES\""` | — |
| [SRC-4FFD5AFC54-L000124](../../scripts/run_answer_quality_benchmark.py#L124) | 124 | `"        else:"` | — |
| [SRC-4FFD5AFC54-L000125](../../scripts/run_answer_quality_benchmark.py#L125) | 125 | `"            tool_status = \"ATTEMPTED_NO_USABLE_RESULTS\""` | — |
| [SRC-4FFD5AFC54-L000126](../../scripts/run_answer_quality_benchmark.py#L126) | 126 | `"    elif outcome == \"attempted_research_error\":"` | — |
| [SRC-4FFD5AFC54-L000127](../../scripts/run_answer_quality_benchmark.py#L127) | 127 | `"        tool_status = \"TOOL_FAILED\""` | — |
| [SRC-4FFD5AFC54-L000128](../../scripts/run_answer_quality_benchmark.py#L128) | 128 | `"    elif outcome == \"unknown_after_budget_exhaustion\":"` | — |
| [SRC-4FFD5AFC54-L000129](../../scripts/run_answer_quality_benchmark.py#L129) | 129 | `"        tool_status = \"BUDGET_EXHAUSTED\""` | — |
| [SRC-4FFD5AFC54-L000130](../../scripts/run_answer_quality_benchmark.py#L130) | 130 | `"    elif outcome == \"not_attempted\":"` | — |
| [SRC-4FFD5AFC54-L000131](../../scripts/run_answer_quality_benchmark.py#L131) | 131 | `"        tool_status = \"NOT_ATTEMPTED\""` | — |
| [SRC-4FFD5AFC54-L000132](../../scripts/run_answer_quality_benchmark.py#L132) | 132 | `"    else:"` | — |
| [SRC-4FFD5AFC54-L000133](../../scripts/run_answer_quality_benchmark.py#L133) | 133 | `"        tool_status = \"UNKNOWN\""` | — |
| [SRC-4FFD5AFC54-L000134](../../scripts/run_answer_quality_benchmark.py#L134) | 134 | `""` | — |
| [SRC-4FFD5AFC54-L000135](../../scripts/run_answer_quality_benchmark.py#L135) | 135 | `"    task_understanding = payload.get(\"task_understanding\")"` | — |
| [SRC-4FFD5AFC54-L000136](../../scripts/run_answer_quality_benchmark.py#L136) | 136 | `"    task_understanding = task_understanding if isinstance(task_understanding, dict) else {}"` | — |
| [SRC-4FFD5AFC54-L000137](../../scripts/run_answer_quality_benchmark.py#L137) | 137 | `"    tool_execution = task_understanding.get(\"tool_execution\")"` | — |
| [SRC-4FFD5AFC54-L000138](../../scripts/run_answer_quality_benchmark.py#L138) | 138 | `"    tool_execution = tool_execution if isinstance(tool_execution, dict) else {}"` | — |
| [SRC-4FFD5AFC54-L000139](../../scripts/run_answer_quality_benchmark.py#L139) | 139 | `"    raw_tool_rows = tool_execution.get(\"tool_status_matrix\")"` | — |
| [SRC-4FFD5AFC54-L000140](../../scripts/run_answer_quality_benchmark.py#L140) | 140 | `"    requirements_raw = tool_execution.get(\"required_tools\")"` | — |
| [SRC-4FFD5AFC54-L000141](../../scripts/run_answer_quality_benchmark.py#L141) | 141 | `"    required_tool_matrix_present = ("` | — |
| [SRC-4FFD5AFC54-L000142](../../scripts/run_answer_quality_benchmark.py#L142) | 142 | `"        isinstance(raw_tool_rows, list) and isinstance(requirements_raw, list)"` | — |
| [SRC-4FFD5AFC54-L000143](../../scripts/run_answer_quality_benchmark.py#L143) | 143 | `"    )"` | — |
| [SRC-4FFD5AFC54-L000144](../../scripts/run_answer_quality_benchmark.py#L144) | 144 | `"    matrix_rows = [row for row in raw_tool_rows if isinstance(row, dict)] if isinstance(raw_tool_rows, list) else []"` | — |
| [SRC-4FFD5AFC54-L000145](../../scripts/run_answer_quality_benchmark.py#L145) | 145 | `"    required_tool_names = ["` | — |
| [SRC-4FFD5AFC54-L000146](../../scripts/run_answer_quality_benchmark.py#L146) | 146 | `"        name.strip()"` | — |
| [SRC-4FFD5AFC54-L000147](../../scripts/run_answer_quality_benchmark.py#L147) | 147 | `"        for name in requirements_raw"` | — |
| [SRC-4FFD5AFC54-L000148](../../scripts/run_answer_quality_benchmark.py#L148) | 148 | `"        if isinstance(name, str) and name.strip()"` | — |
| [SRC-4FFD5AFC54-L000149](../../scripts/run_answer_quality_benchmark.py#L149) | 149 | `"    ] if isinstance(requirements_raw, list) else []"` | — |
| [SRC-4FFD5AFC54-L000150](../../scripts/run_answer_quality_benchmark.py#L150) | 150 | `"    allowed_statuses = {"` | — |
| [SRC-4FFD5AFC54-L000151](../../scripts/run_answer_quality_benchmark.py#L151) | 151 | `"        \"web_search\": {"` | — |
| [SRC-4FFD5AFC54-L000152](../../scripts/run_answer_quality_benchmark.py#L152) | 152 | `"            \"failed\", \"unknown\", \"not_attempted\", \"counter_mismatch\","` | — |
| [SRC-4FFD5AFC54-L000153](../../scripts/run_answer_quality_benchmark.py#L153) | 153 | `"            \"completed_with_results\", \"completed_no_usable_results\","` | — |
| [SRC-4FFD5AFC54-L000154](../../scripts/run_answer_quality_benchmark.py#L154) | 154 | `"        },"` | — |
| [SRC-4FFD5AFC54-L000155](../../scripts/run_answer_quality_benchmark.py#L155) | 155 | `"        \"page_fetch\": {"` | — |
| [SRC-4FFD5AFC54-L000156](../../scripts/run_answer_quality_benchmark.py#L156) | 156 | `"            \"counter_mismatch\", \"completed_with_read_pages\","` | — |
| [SRC-4FFD5AFC54-L000157](../../scripts/run_answer_quality_benchmark.py#L157) | 157 | `"            \"attempted_no_readable_pages\", \"unknown\","` | — |
| [SRC-4FFD5AFC54-L000158](../../scripts/run_answer_quality_benchmark.py#L158) | 158 | `"            \"not_attempted_after_search_error\", \"not_attempted_no_fetchable_candidates\","` | — |
| [SRC-4FFD5AFC54-L000159](../../scripts/run_answer_quality_benchmark.py#L159) | 159 | `"            \"not_attempted\","` | — |
| [SRC-4FFD5AFC54-L000160](../../scripts/run_answer_quality_benchmark.py#L160) | 160 | `"        },"` | — |
| [SRC-4FFD5AFC54-L000161](../../scripts/run_answer_quality_benchmark.py#L161) | 161 | `"        \"public_social_search_if_configured\": {"` | — |
| [SRC-4FFD5AFC54-L000162](../../scripts/run_answer_quality_benchmark.py#L162) | 162 | `"            \"completed_with_results\", \"failed\", \"unknown\","` | — |
| [SRC-4FFD5AFC54-L000163](../../scripts/run_answer_quality_benchmark.py#L163) | 163 | `"            \"completed_no_usable_results\", \"not_attempted\", \"not_configured\","` | — |
| [SRC-4FFD5AFC54-L000164](../../scripts/run_answer_quality_benchmark.py#L164) | 164 | `"        },"` | — |
| [SRC-4FFD5AFC54-L000165](../../scripts/run_answer_quality_benchmark.py#L165) | 165 | `"        \"language_model_generation_if_configured\": {"` | — |
| [SRC-4FFD5AFC54-L000166](../../scripts/run_answer_quality_benchmark.py#L166) | 166 | `"            \"completed\", \"not_configured\", \"failed\", \"not_attempted\","` | — |
| [SRC-4FFD5AFC54-L000167](../../scripts/run_answer_quality_benchmark.py#L167) | 167 | `"            \"not_attempted_no_evidence\", \"unknown\","` | — |
| [SRC-4FFD5AFC54-L000168](../../scripts/run_answer_quality_benchmark.py#L168) | 168 | `"        },"` | — |
| [SRC-4FFD5AFC54-L000169](../../scripts/run_answer_quality_benchmark.py#L169) | 169 | `"        \"claim_review_if_configured\": {"` | — |
| [SRC-4FFD5AFC54-L000170](../../scripts/run_answer_quality_benchmark.py#L170) | 170 | `"            \"completed_model_assisted_review\", \"failed\","` | — |
| [SRC-4FFD5AFC54-L000171](../../scripts/run_answer_quality_benchmark.py#L171) | 171 | `"            \"not_attempted_no_evidence\", \"not_attempted\", \"unknown\","` | — |
| [SRC-4FFD5AFC54-L000172](../../scripts/run_answer_quality_benchmark.py#L172) | 172 | `"        },"` | — |
| [SRC-4FFD5AFC54-L000173](../../scripts/run_answer_quality_benchmark.py#L173) | 173 | `"    }"` | — |
| [SRC-4FFD5AFC54-L000174](../../scripts/run_answer_quality_benchmark.py#L174) | 174 | `"    successful_statuses = {"` | — |
| [SRC-4FFD5AFC54-L000175](../../scripts/run_answer_quality_benchmark.py#L175) | 175 | `"        \"web_search\": {\"completed_with_results\"},"` | — |
| [SRC-4FFD5AFC54-L000176](../../scripts/run_answer_quality_benchmark.py#L176) | 176 | `"        \"page_fetch\": {\"completed_with_read_pages\"},"` | — |
| [SRC-4FFD5AFC54-L000177](../../scripts/run_answer_quality_benchmark.py#L177) | 177 | `"        \"public_social_search_if_configured\": {\"completed_with_results\"},"` | — |
| [SRC-4FFD5AFC54-L000178](../../scripts/run_answer_quality_benchmark.py#L178) | 178 | `"        \"language_model_generation_if_configured\": {\"completed\"},"` | — |
| [SRC-4FFD5AFC54-L000179](../../scripts/run_answer_quality_benchmark.py#L179) | 179 | `"        \"claim_review_if_configured\": {\"completed_model_assisted_review\"},"` | — |
| [SRC-4FFD5AFC54-L000180](../../scripts/run_answer_quality_benchmark.py#L180) | 180 | `"    }"` | — |
| [SRC-4FFD5AFC54-L000181](../../scripts/run_answer_quality_benchmark.py#L181) | 181 | `"    required_tool_statuses = []"` | — |
| [SRC-4FFD5AFC54-L000182](../../scripts/run_answer_quality_benchmark.py#L182) | 182 | `"    required_name_set = set(required_tool_names)"` | — |
| [SRC-4FFD5AFC54-L000183](../../scripts/run_answer_quality_benchmark.py#L183) | 183 | `"    reported_required_names = {"` | — |
| [SRC-4FFD5AFC54-L000184](../../scripts/run_answer_quality_benchmark.py#L184) | 184 | `"        row.get(\"tool\")"` | — |
| [SRC-4FFD5AFC54-L000185](../../scripts/run_answer_quality_benchmark.py#L185) | 185 | `"        for row in matrix_rows"` | — |
| [SRC-4FFD5AFC54-L000186](../../scripts/run_answer_quality_benchmark.py#L186) | 186 | `"        if row.get(\"required_by_task_spec\") is True and isinstance(row.get(\"tool\"), str)"` | — |
| [SRC-4FFD5AFC54-L000187](../../scripts/run_answer_quality_benchmark.py#L187) | 187 | `"    }"` | — |
| [SRC-4FFD5AFC54-L000188](../../scripts/run_answer_quality_benchmark.py#L188) | 188 | `"    required_tool_matrix_complete = ("` | — |
| [SRC-4FFD5AFC54-L000189](../../scripts/run_answer_quality_benchmark.py#L189) | 189 | `"        required_tool_matrix_present"` | — |
| [SRC-4FFD5AFC54-L000190](../../scripts/run_answer_quality_benchmark.py#L190) | 190 | `"        and len(required_tool_names) == len(required_name_set)"` | — |
| [SRC-4FFD5AFC54-L000191](../../scripts/run_answer_quality_benchmark.py#L191) | 191 | `"        and reported_required_names == required_name_set"` | — |
| [SRC-4FFD5AFC54-L000192](../../scripts/run_answer_quality_benchmark.py#L192) | 192 | `"    )"` | — |
| [SRC-4FFD5AFC54-L000193](../../scripts/run_answer_quality_benchmark.py#L193) | 193 | `"    for tool in dict.fromkeys(required_tool_names):"` | — |
| [SRC-4FFD5AFC54-L000194](../../scripts/run_answer_quality_benchmark.py#L194) | 194 | `"        matches = ["` | — |
| [SRC-4FFD5AFC54-L000195](../../scripts/run_answer_quality_benchmark.py#L195) | 195 | `"            row for row in matrix_rows"` | — |
| [SRC-4FFD5AFC54-L000196](../../scripts/run_answer_quality_benchmark.py#L196) | 196 | `"            if row.get(\"tool\") == tool and row.get(\"required_by_task_spec\") is True"` | — |
| [SRC-4FFD5AFC54-L000197](../../scripts/run_answer_quality_benchmark.py#L197) | 197 | `"        ]"` | — |
| [SRC-4FFD5AFC54-L000198](../../scripts/run_answer_quality_benchmark.py#L198) | 198 | `"        if len(matches) == 0:"` | — |
| [SRC-4FFD5AFC54-L000199](../../scripts/run_answer_quality_benchmark.py#L199) | 199 | `"            status = \"missing_matrix_row\""` | — |
| [SRC-4FFD5AFC54-L000200](../../scripts/run_answer_quality_benchmark.py#L200) | 200 | `"            status_observed = False"` | — |
| [SRC-4FFD5AFC54-L000201](../../scripts/run_answer_quality_benchmark.py#L201) | 201 | `"            successful = False"` | — |
| [SRC-4FFD5AFC54-L000202](../../scripts/run_answer_quality_benchmark.py#L202) | 202 | `"            required_tool_matrix_complete = False"` | — |
| [SRC-4FFD5AFC54-L000203](../../scripts/run_answer_quality_benchmark.py#L203) | 203 | `"        elif len(matches) > 1:"` | — |
| [SRC-4FFD5AFC54-L000204](../../scripts/run_answer_quality_benchmark.py#L204) | 204 | `"            status = \"duplicate_matrix_rows\""` | — |
| [SRC-4FFD5AFC54-L000205](../../scripts/run_answer_quality_benchmark.py#L205) | 205 | `"            status_observed = False"` | — |
| [SRC-4FFD5AFC54-L000206](../../scripts/run_answer_quality_benchmark.py#L206) | 206 | `"            successful = False"` | — |
| [SRC-4FFD5AFC54-L000207](../../scripts/run_answer_quality_benchmark.py#L207) | 207 | `"            required_tool_matrix_complete = False"` | — |
| [SRC-4FFD5AFC54-L000208](../../scripts/run_answer_quality_benchmark.py#L208) | 208 | `"        else:"` | — |
| [SRC-4FFD5AFC54-L000209](../../scripts/run_answer_quality_benchmark.py#L209) | 209 | `"            raw_status = matches[0].get(\"status\")"` | — |
| [SRC-4FFD5AFC54-L000210](../../scripts/run_answer_quality_benchmark.py#L210) | 210 | `"            status_observed = isinstance(raw_status, str) and bool(raw_status.strip())"` | — |
| [SRC-4FFD5AFC54-L000211](../../scripts/run_answer_quality_benchmark.py#L211) | 211 | `"            status = raw_status if status_observed else \"missing_status\""` | — |
| [SRC-4FFD5AFC54-L000212](../../scripts/run_answer_quality_benchmark.py#L212) | 212 | `"            status_valid = status_observed and status in allowed_statuses.get(tool, set())"` | — |
| [SRC-4FFD5AFC54-L000213](../../scripts/run_answer_quality_benchmark.py#L213) | 213 | `"            successful = status_valid and status in successful_statuses.get(tool, set())"` | — |
| [SRC-4FFD5AFC54-L000214](../../scripts/run_answer_quality_benchmark.py#L214) | 214 | `"            if not status_valid:"` | — |
| [SRC-4FFD5AFC54-L000215](../../scripts/run_answer_quality_benchmark.py#L215) | 215 | `"                required_tool_matrix_complete = False"` | — |
| [SRC-4FFD5AFC54-L000216](../../scripts/run_answer_quality_benchmark.py#L216) | 216 | `"        required_tool_statuses.append({"` | — |
| [SRC-4FFD5AFC54-L000217](../../scripts/run_answer_quality_benchmark.py#L217) | 217 | `"            \"tool\": tool,"` | — |
| [SRC-4FFD5AFC54-L000218](../../scripts/run_answer_quality_benchmark.py#L218) | 218 | `"            \"status\": status,"` | — |
| [SRC-4FFD5AFC54-L000219](../../scripts/run_answer_quality_benchmark.py#L219) | 219 | `"            \"status_observed\": status_observed,"` | — |
| [SRC-4FFD5AFC54-L000220](../../scripts/run_answer_quality_benchmark.py#L220) | 220 | `"            \"status_valid\": status_valid if len(matches) == 1 else False,"` | — |
| [SRC-4FFD5AFC54-L000221](../../scripts/run_answer_quality_benchmark.py#L221) | 221 | `"            \"successful_completion\": successful,"` | — |
| [SRC-4FFD5AFC54-L000222](../../scripts/run_answer_quality_benchmark.py#L222) | 222 | `"        })"` | — |
| [SRC-4FFD5AFC54-L000223](../../scripts/run_answer_quality_benchmark.py#L223) | 223 | `"    if expected_strategy == \"web_search\" and \"web_search\" not in required_name_set:"` | — |
| [SRC-4FFD5AFC54-L000224](../../scripts/run_answer_quality_benchmark.py#L224) | 224 | `"        required_tool_matrix_complete = False"` | — |
| [SRC-4FFD5AFC54-L000225](../../scripts/run_answer_quality_benchmark.py#L225) | 225 | `""` | — |
| [SRC-4FFD5AFC54-L000226](../../scripts/run_answer_quality_benchmark.py#L226) | 226 | `"    calls = _model_calls_from_payload(payload)"` | — |
| [SRC-4FFD5AFC54-L000227](../../scripts/run_answer_quality_benchmark.py#L227) | 227 | `"    reported_costs = []"` | — |
| [SRC-4FFD5AFC54-L000228](../../scripts/run_answer_quality_benchmark.py#L228) | 228 | `"    for call in calls:"` | — |
| [SRC-4FFD5AFC54-L000229](../../scripts/run_answer_quality_benchmark.py#L229) | 229 | `"        usage = call.get(\"provider_usage\")"` | — |
| [SRC-4FFD5AFC54-L000230](../../scripts/run_answer_quality_benchmark.py#L230) | 230 | `"        if not isinstance(usage, dict):"` | — |
| [SRC-4FFD5AFC54-L000231](../../scripts/run_answer_quality_benchmark.py#L231) | 231 | `"            continue"` | — |
| [SRC-4FFD5AFC54-L000232](../../scripts/run_answer_quality_benchmark.py#L232) | 232 | `"        cost = _finite_nonnegative_number(usage.get(\"cost_usd\"))"` | — |
| [SRC-4FFD5AFC54-L000233](../../scripts/run_answer_quality_benchmark.py#L233) | 233 | `"        if cost is not None:"` | — |
| [SRC-4FFD5AFC54-L000234](../../scripts/run_answer_quality_benchmark.py#L234) | 234 | `"            reported_costs.append(cost)"` | — |
| [SRC-4FFD5AFC54-L000235](../../scripts/run_answer_quality_benchmark.py#L235) | 235 | `""` | — |
| [SRC-4FFD5AFC54-L000236](../../scripts/run_answer_quality_benchmark.py#L236) | 236 | `"    if not calls:"` | — |
| [SRC-4FFD5AFC54-L000237](../../scripts/run_answer_quality_benchmark.py#L237) | 237 | `"        cost_status = \"NO_MODEL_CALL_METADATA\""` | — |
| [SRC-4FFD5AFC54-L000238](../../scripts/run_answer_quality_benchmark.py#L238) | 238 | `"    elif len(reported_costs) == len(calls):"` | — |
| [SRC-4FFD5AFC54-L000239](../../scripts/run_answer_quality_benchmark.py#L239) | 239 | `"        cost_status = \"COMPLETE_FOR_RETURNED_MODEL_CALLS\""` | — |
| [SRC-4FFD5AFC54-L000240](../../scripts/run_answer_quality_benchmark.py#L240) | 240 | `"    elif reported_costs:"` | — |
| [SRC-4FFD5AFC54-L000241](../../scripts/run_answer_quality_benchmark.py#L241) | 241 | `"        cost_status = \"PARTIAL_PROVIDER_REPORTED_MODEL_COST\""` | — |
| [SRC-4FFD5AFC54-L000242](../../scripts/run_answer_quality_benchmark.py#L242) | 242 | `"    else:"` | — |
| [SRC-4FFD5AFC54-L000243](../../scripts/run_answer_quality_benchmark.py#L243) | 243 | `"        cost_status = \"PROVIDER_COST_NOT_REPORTED\""` | — |
| [SRC-4FFD5AFC54-L000244](../../scripts/run_answer_quality_benchmark.py#L244) | 244 | `""` | — |
| [SRC-4FFD5AFC54-L000245](../../scripts/run_answer_quality_benchmark.py#L245) | 245 | `"    return {"` | — |
| [SRC-4FFD5AFC54-L000246](../../scripts/run_answer_quality_benchmark.py#L246) | 246 | `"        \"search_outcome\": outcome if isinstance(outcome, str) else \"unknown\","` | — |
| [SRC-4FFD5AFC54-L000247](../../scripts/run_answer_quality_benchmark.py#L247) | 247 | `"        \"pipeline_completion_status\": pipeline if isinstance(pipeline, str) else \"unknown\","` | — |
| [SRC-4FFD5AFC54-L000248](../../scripts/run_answer_quality_benchmark.py#L248) | 248 | `"        \"tool_status\": tool_status,"` | — |
| [SRC-4FFD5AFC54-L000249](../../scripts/run_answer_quality_benchmark.py#L249) | 249 | `"        \"required_tool_statuses\": required_tool_statuses,"` | — |
| [SRC-4FFD5AFC54-L000250](../../scripts/run_answer_quality_benchmark.py#L250) | 250 | `"        \"required_tool_success_count\": sum(1 for row in required_tool_statuses if row[\"successful_completion\"]),"` | — |
| [SRC-4FFD5AFC54-L000251](../../scripts/run_answer_quality_benchmark.py#L251) | 251 | `"        \"required_tool_count\": len(required_tool_statuses),"` | — |
| [SRC-4FFD5AFC54-L000252](../../scripts/run_answer_quality_benchmark.py#L252) | 252 | `"        \"required_tool_success_rate\": ("` | — |
| [SRC-4FFD5AFC54-L000253](../../scripts/run_answer_quality_benchmark.py#L253) | 253 | `"            round("` | — |
| [SRC-4FFD5AFC54-L000254](../../scripts/run_answer_quality_benchmark.py#L254) | 254 | `"                sum(1 for row in required_tool_statuses if row[\"successful_completion\"])"` | — |
