# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **029**
- سجلات الأسطر: **800**
- النطاق: SRC-70795F4B61-L000360 إلى SRC-03FF422A16-L000063
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## ملفات أخرى

### FILE-70795F4B61 — [scripts/compare_answer_quality_runs.py](../../scripts/compare_answer_quality_runs.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-70795F4B61-L000360](../../scripts/compare_answer_quality_runs.py#L360) | 360 | `"    output = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True)"` | — |
| [SRC-70795F4B61-L000361](../../scripts/compare_answer_quality_runs.py#L361) | 361 | `"    if args.out:"` | — |
| [SRC-70795F4B61-L000362](../../scripts/compare_answer_quality_runs.py#L362) | 362 | `"        args.out.write_text(output + \"\\n\", encoding=\"utf-8\")"` | — |
| [SRC-70795F4B61-L000363](../../scripts/compare_answer_quality_runs.py#L363) | 363 | `"        print(\"Wrote \" + str(args.out))"` | — |
| [SRC-70795F4B61-L000364](../../scripts/compare_answer_quality_runs.py#L364) | 364 | `"    print(output)"` | — |
| [SRC-70795F4B61-L000365](../../scripts/compare_answer_quality_runs.py#L365) | 365 | `"    return 0 if result[\"acceptance_status\"] == \"COMPARABLE_WITH_REVIEWED_QUALITY_AND_BUILD_IDENTITIES\" else 2"` | — |
| [SRC-70795F4B61-L000366](../../scripts/compare_answer_quality_runs.py#L366) | 366 | `""` | — |
| [SRC-70795F4B61-L000367](../../scripts/compare_answer_quality_runs.py#L367) | 367 | `""` | — |
| [SRC-70795F4B61-L000368](../../scripts/compare_answer_quality_runs.py#L368) | 368 | `"if __name__ == \"__main__\":"` | — |
| [SRC-70795F4B61-L000369](../../scripts/compare_answer_quality_runs.py#L369) | 369 | `"    raise SystemExit(main())"` | — |
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
| [SRC-A8360B1B03-L000006](../../scripts/hosted_smoke_test.py#L6) | 6 | `"import json"` | — |
| [SRC-A8360B1B03-L000007](../../scripts/hosted_smoke_test.py#L7) | 7 | `"import os"` | — |
| [SRC-A8360B1B03-L000008](../../scripts/hosted_smoke_test.py#L8) | 8 | `"import re"` | — |
| [SRC-A8360B1B03-L000009](../../scripts/hosted_smoke_test.py#L9) | 9 | `"import sys"` | — |
| [SRC-A8360B1B03-L000010](../../scripts/hosted_smoke_test.py#L10) | 10 | `"import urllib.error"` | — |
| [SRC-A8360B1B03-L000011](../../scripts/hosted_smoke_test.py#L11) | 11 | `"import urllib.parse"` | — |
| [SRC-A8360B1B03-L000012](../../scripts/hosted_smoke_test.py#L12) | 12 | `"import urllib.request"` | — |
| [SRC-A8360B1B03-L000013](../../scripts/hosted_smoke_test.py#L13) | 13 | `"from typing import Any"` | — |
| [SRC-A8360B1B03-L000014](../../scripts/hosted_smoke_test.py#L14) | 14 | `""` | — |
| [SRC-A8360B1B03-L000015](../../scripts/hosted_smoke_test.py#L15) | 15 | `""` | — |
| [SRC-A8360B1B03-L000016](../../scripts/hosted_smoke_test.py#L16) | 16 | `"class SmokeError(RuntimeError):"` | — |
| [SRC-A8360B1B03-L000017](../../scripts/hosted_smoke_test.py#L17) | 17 | `"    \"\"\"A live acceptance check failed.\"\"\""` | — |
| [SRC-A8360B1B03-L000018](../../scripts/hosted_smoke_test.py#L18) | 18 | `""` | — |
| [SRC-A8360B1B03-L000019](../../scripts/hosted_smoke_test.py#L19) | 19 | `""` | — |
| [SRC-A8360B1B03-L000020](../../scripts/hosted_smoke_test.py#L20) | 20 | `"class _SameOriginRedirectHandler(urllib.request.HTTPRedirectHandler):"` | — |
| [SRC-A8360B1B03-L000021](../../scripts/hosted_smoke_test.py#L21) | 21 | `"    \"\"\"Never forward a bearer token to a different origin during an HTTP redirect.\"\"\""` | — |
| [SRC-A8360B1B03-L000022](../../scripts/hosted_smoke_test.py#L22) | 22 | `""` | — |
| [SRC-A8360B1B03-L000023](../../scripts/hosted_smoke_test.py#L23) | 23 | `"    @staticmethod"` | — |
| [SRC-A8360B1B03-L000024](../../scripts/hosted_smoke_test.py#L24) | 24 | `"    def _origin(url: str) -> tuple[str, str, int \| None]:"` | — |
| [SRC-A8360B1B03-L000025](../../scripts/hosted_smoke_test.py#L25) | 25 | `"        parsed = urllib.parse.urlsplit(url)"` | — |
| [SRC-A8360B1B03-L000026](../../scripts/hosted_smoke_test.py#L26) | 26 | `"        try:"` | — |
| [SRC-A8360B1B03-L000027](../../scripts/hosted_smoke_test.py#L27) | 27 | `"            port = parsed.port"` | — |
| [SRC-A8360B1B03-L000028](../../scripts/hosted_smoke_test.py#L28) | 28 | `"        except ValueError:"` | — |
| [SRC-A8360B1B03-L000029](../../scripts/hosted_smoke_test.py#L29) | 29 | `"            return \"\", \"\", None"` | — |
| [SRC-A8360B1B03-L000030](../../scripts/hosted_smoke_test.py#L30) | 30 | `"        if port is None:"` | — |
| [SRC-A8360B1B03-L000031](../../scripts/hosted_smoke_test.py#L31) | 31 | `"            port = 443 if parsed.scheme.lower() == \"https\" else 80 if parsed.scheme.lower() == \"http\" else None"` | — |
| [SRC-A8360B1B03-L000032](../../scripts/hosted_smoke_test.py#L32) | 32 | `"        return parsed.scheme.lower(), (parsed.hostname or \"\").lower(), port"` | — |
| [SRC-A8360B1B03-L000033](../../scripts/hosted_smoke_test.py#L33) | 33 | `""` | — |
| [SRC-A8360B1B03-L000034](../../scripts/hosted_smoke_test.py#L34) | 34 | `"    def redirect_request(self, req, fp, code, msg, headers, newurl):"` | — |
| [SRC-A8360B1B03-L000035](../../scripts/hosted_smoke_test.py#L35) | 35 | `"        target_url = urllib.parse.urljoin(req.full_url, newurl)"` | — |
| [SRC-A8360B1B03-L000036](../../scripts/hosted_smoke_test.py#L36) | 36 | `"        target = urllib.parse.urlsplit(target_url)"` | — |
| [SRC-A8360B1B03-L000037](../../scripts/hosted_smoke_test.py#L37) | 37 | `"        if ("` | — |
| [SRC-A8360B1B03-L000038](../../scripts/hosted_smoke_test.py#L38) | 38 | `"            self._origin(req.full_url) != self._origin(target_url)"` | — |
| [SRC-A8360B1B03-L000039](../../scripts/hosted_smoke_test.py#L39) | 39 | `"            or target.scheme.lower() not in {\"http\", \"https\"}"` | — |
| [SRC-A8360B1B03-L000040](../../scripts/hosted_smoke_test.py#L40) | 40 | `"            or target.username"` | — |
| [SRC-A8360B1B03-L000041](../../scripts/hosted_smoke_test.py#L41) | 41 | `"            or target.password"` | — |
| [SRC-A8360B1B03-L000042](../../scripts/hosted_smoke_test.py#L42) | 42 | `"        ):"` | — |
| [SRC-A8360B1B03-L000043](../../scripts/hosted_smoke_test.py#L43) | 43 | `"            raise urllib.error.HTTPError("` | — |
| [SRC-A8360B1B03-L000044](../../scripts/hosted_smoke_test.py#L44) | 44 | `"                req.full_url, code, \"Cross-origin redirect blocked\", headers, fp"` | — |
| [SRC-A8360B1B03-L000045](../../scripts/hosted_smoke_test.py#L45) | 45 | `"            )"` | — |
| [SRC-A8360B1B03-L000046](../../scripts/hosted_smoke_test.py#L46) | 46 | `"        return super().redirect_request(req, fp, code, msg, headers, target_url)"` | — |
| [SRC-A8360B1B03-L000047](../../scripts/hosted_smoke_test.py#L47) | 47 | `""` | — |
| [SRC-A8360B1B03-L000048](../../scripts/hosted_smoke_test.py#L48) | 48 | `""` | — |
| [SRC-A8360B1B03-L000049](../../scripts/hosted_smoke_test.py#L49) | 49 | `"def normalize_origin(value: str, allow_http: bool = False) -> str:"` | — |
| [SRC-A8360B1B03-L000050](../../scripts/hosted_smoke_test.py#L50) | 50 | `"    parsed = urllib.parse.urlsplit((value or \"\").strip())"` | — |
| [SRC-A8360B1B03-L000051](../../scripts/hosted_smoke_test.py#L51) | 51 | `"    if parsed.scheme not in {\"https\", \"http\"} or not parsed.hostname:"` | — |
| [SRC-A8360B1B03-L000052](../../scripts/hosted_smoke_test.py#L52) | 52 | `"        raise SmokeError(\"Provide an absolute HTTPS origin, for example https://your-app.example.com.\")"` | — |
| [SRC-A8360B1B03-L000053](../../scripts/hosted_smoke_test.py#L53) | 53 | `"    if parsed.username or parsed.password or parsed.query or parsed.fragment:"` | — |
| [SRC-A8360B1B03-L000054](../../scripts/hosted_smoke_test.py#L54) | 54 | `"        raise SmokeError(\"The base URL must not contain credentials, a query, or a fragment.\")"` | — |
| [SRC-A8360B1B03-L000055](../../scripts/hosted_smoke_test.py#L55) | 55 | `"    if parsed.path not in {\"\", \"/\"}:"` | — |
| [SRC-A8360B1B03-L000056](../../scripts/hosted_smoke_test.py#L56) | 56 | `"        raise SmokeError(\"The base URL must be an origin only; do not add /api or another path.\")"` | — |
| [SRC-A8360B1B03-L000057](../../scripts/hosted_smoke_test.py#L57) | 57 | `"    if parsed.scheme != \"https\" and not ("` | — |
| [SRC-A8360B1B03-L000058](../../scripts/hosted_smoke_test.py#L58) | 58 | `"        allow_http and parsed.hostname.lower() in {\"localhost\", \"127.0.0.1\", \"::1\"}"` | — |
| [SRC-A8360B1B03-L000059](../../scripts/hosted_smoke_test.py#L59) | 59 | `"    ):"` | — |
| [SRC-A8360B1B03-L000060](../../scripts/hosted_smoke_test.py#L60) | 60 | `"        raise SmokeError(\"Hosted tests require HTTPS; plain HTTP is allowed only for local tests.\")"` | — |
| [SRC-A8360B1B03-L000061](../../scripts/hosted_smoke_test.py#L61) | 61 | `"    try:"` | — |
| [SRC-A8360B1B03-L000062](../../scripts/hosted_smoke_test.py#L62) | 62 | `"        port = parsed.port"` | — |
| [SRC-A8360B1B03-L000063](../../scripts/hosted_smoke_test.py#L63) | 63 | `"    except ValueError as exc:"` | — |
| [SRC-A8360B1B03-L000064](../../scripts/hosted_smoke_test.py#L64) | 64 | `"        raise SmokeError(\"Invalid port in base URL.\") from exc"` | — |
| [SRC-A8360B1B03-L000065](../../scripts/hosted_smoke_test.py#L65) | 65 | `"    host = parsed.hostname"` | — |
| [SRC-A8360B1B03-L000066](../../scripts/hosted_smoke_test.py#L66) | 66 | `"    if \":\" in host and not host.startswith(\"[\"):"` | — |
| [SRC-A8360B1B03-L000067](../../scripts/hosted_smoke_test.py#L67) | 67 | `"        host = f\"[{host}]\""` | — |
| [SRC-A8360B1B03-L000068](../../scripts/hosted_smoke_test.py#L68) | 68 | `"    if port:"` | — |
| [SRC-A8360B1B03-L000069](../../scripts/hosted_smoke_test.py#L69) | 69 | `"        host += f\":{port}\""` | — |
| [SRC-A8360B1B03-L000070](../../scripts/hosted_smoke_test.py#L70) | 70 | `"    return f\"{parsed.scheme}://{host}\""` | — |
| [SRC-A8360B1B03-L000071](../../scripts/hosted_smoke_test.py#L71) | 71 | `""` | — |
| [SRC-A8360B1B03-L000072](../../scripts/hosted_smoke_test.py#L72) | 72 | `""` | — |
| [SRC-A8360B1B03-L000073](../../scripts/hosted_smoke_test.py#L73) | 73 | `"def request_json(url: str, *, token: str = \"\", payload: dict[str, Any] \| None = None,"` | — |
| [SRC-A8360B1B03-L000074](../../scripts/hosted_smoke_test.py#L74) | 74 | `"                 timeout: float = 90) -> tuple[int, dict[str, Any] \| None]:"` | — |
| [SRC-A8360B1B03-L000075](../../scripts/hosted_smoke_test.py#L75) | 75 | `"    headers = {\"Accept\": \"application/json\"}"` | — |
| [SRC-A8360B1B03-L000076](../../scripts/hosted_smoke_test.py#L76) | 76 | `"    data = None"` | — |
| [SRC-A8360B1B03-L000077](../../scripts/hosted_smoke_test.py#L77) | 77 | `"    if payload is not None:"` | — |
| [SRC-A8360B1B03-L000078](../../scripts/hosted_smoke_test.py#L78) | 78 | `"        headers[\"Content-Type\"] = \"application/json\""` | — |
| [SRC-A8360B1B03-L000079](../../scripts/hosted_smoke_test.py#L79) | 79 | `"        data = json.dumps(payload, ensure_ascii=False).encode()"` | — |
| [SRC-A8360B1B03-L000080](../../scripts/hosted_smoke_test.py#L80) | 80 | `"    if token:"` | — |
| [SRC-A8360B1B03-L000081](../../scripts/hosted_smoke_test.py#L81) | 81 | `"        headers[\"Authorization\"] = \"Bearer \" + token"` | — |
| [SRC-A8360B1B03-L000082](../../scripts/hosted_smoke_test.py#L82) | 82 | `"    request = urllib.request.Request(url, data=data, headers=headers)"` | — |
| [SRC-A8360B1B03-L000083](../../scripts/hosted_smoke_test.py#L83) | 83 | `"    try:"` | — |
| [SRC-A8360B1B03-L000084](../../scripts/hosted_smoke_test.py#L84) | 84 | `"        opener = urllib.request.build_opener(_SameOriginRedirectHandler())"` | — |
| [SRC-A8360B1B03-L000085](../../scripts/hosted_smoke_test.py#L85) | 85 | `"        with opener.open(request, timeout=timeout) as response:"` | — |
| [SRC-A8360B1B03-L000086](../../scripts/hosted_smoke_test.py#L86) | 86 | `"            status, body = response.status, response.read(1_000_000)"` | — |
| [SRC-A8360B1B03-L000087](../../scripts/hosted_smoke_test.py#L87) | 87 | `"    except urllib.error.HTTPError as exc:"` | — |
| [SRC-A8360B1B03-L000088](../../scripts/hosted_smoke_test.py#L88) | 88 | `"        status = exc.code"` | — |
| [SRC-A8360B1B03-L000089](../../scripts/hosted_smoke_test.py#L89) | 89 | `"        body = exc.read(100_000)"` | — |
| [SRC-A8360B1B03-L000090](../../scripts/hosted_smoke_test.py#L90) | 90 | `"    except (urllib.error.URLError, TimeoutError, OSError) as exc:"` | — |
| [SRC-A8360B1B03-L000091](../../scripts/hosted_smoke_test.py#L91) | 91 | `"        path = urllib.parse.urlsplit(url).path"` | — |
| [SRC-A8360B1B03-L000092](../../scripts/hosted_smoke_test.py#L92) | 92 | `"        raise SmokeError(f\"Network request failed at {path}; check the service and network.\") from exc"` | — |
| [SRC-A8360B1B03-L000093](../../scripts/hosted_smoke_test.py#L93) | 93 | `"    try:"` | — |
| [SRC-A8360B1B03-L000094](../../scripts/hosted_smoke_test.py#L94) | 94 | `"        result = json.loads(body.decode(\"utf-8\"))"` | — |
| [SRC-A8360B1B03-L000095](../../scripts/hosted_smoke_test.py#L95) | 95 | `"    except (UnicodeDecodeError, json.JSONDecodeError):"` | — |
| [SRC-A8360B1B03-L000096](../../scripts/hosted_smoke_test.py#L96) | 96 | `"        result = None"` | — |
| [SRC-A8360B1B03-L000097](../../scripts/hosted_smoke_test.py#L97) | 97 | `"    return status, result if isinstance(result, dict) else None"` | — |
| [SRC-A8360B1B03-L000098](../../scripts/hosted_smoke_test.py#L98) | 98 | `""` | — |
| [SRC-A8360B1B03-L000099](../../scripts/hosted_smoke_test.py#L99) | 99 | `""` | — |
| [SRC-A8360B1B03-L000100](../../scripts/hosted_smoke_test.py#L100) | 100 | `"def run_smoke("` | — |
| [SRC-A8360B1B03-L000101](../../scripts/hosted_smoke_test.py#L101) | 101 | `"    origin: str,"` | — |
| [SRC-A8360B1B03-L000102](../../scripts/hosted_smoke_test.py#L102) | 102 | `"    token: str,"` | — |
| [SRC-A8360B1B03-L000103](../../scripts/hosted_smoke_test.py#L103) | 103 | `"    *,"` | — |
| [SRC-A8360B1B03-L000104](../../scripts/hosted_smoke_test.py#L104) | 104 | `"    timeout: float = 90,"` | — |
| [SRC-A8360B1B03-L000105](../../scripts/hosted_smoke_test.py#L105) | 105 | `"    allow_http: bool = False,"` | — |
| [SRC-A8360B1B03-L000106](../../scripts/hosted_smoke_test.py#L106) | 106 | `"    expected_sha: str \| None = None,"` | — |
| [SRC-A8360B1B03-L000107](../../scripts/hosted_smoke_test.py#L107) | 107 | `") -> dict[str, Any]:"` | — |
| [SRC-A8360B1B03-L000108](../../scripts/hosted_smoke_test.py#L108) | 108 | `"    origin = normalize_origin(origin, allow_http)"` | — |
| [SRC-A8360B1B03-L000109](../../scripts/hosted_smoke_test.py#L109) | 109 | `"    if expected_sha is not None and not re.fullmatch(r\"[0-9a-fA-F]{40}\", expected_sha.strip()):"` | — |
| [SRC-A8360B1B03-L000110](../../scripts/hosted_smoke_test.py#L110) | 110 | `"        raise SmokeError(\"The expected source revision must be a full 40-character Git SHA.\")"` | — |
| [SRC-A8360B1B03-L000111](../../scripts/hosted_smoke_test.py#L111) | 111 | `"    if len(token.strip()) < 32:"` | — |
| [SRC-A8360B1B03-L000112](../../scripts/hosted_smoke_test.py#L112) | 112 | `"        raise SmokeError(\"OMARAI_ACCESS_TOKEN is missing or shorter than 32 characters.\")"` | — |
| [SRC-A8360B1B03-L000113](../../scripts/hosted_smoke_test.py#L113) | 113 | `""` | — |
| [SRC-A8360B1B03-L000114](../../scripts/hosted_smoke_test.py#L114) | 114 | `"    status, health = request_json(f\"{origin}/api/health\", timeout=min(timeout, 20))"` | — |
| [SRC-A8360B1B03-L000115](../../scripts/hosted_smoke_test.py#L115) | 115 | `"    if status != 200 or not health or health.get(\"ok\") is not True:"` | — |
| [SRC-A8360B1B03-L000116](../../scripts/hosted_smoke_test.py#L116) | 116 | `"        raise SmokeError(f\"Health check failed (HTTP {status}).\")"` | — |
| [SRC-A8360B1B03-L000117](../../scripts/hosted_smoke_test.py#L117) | 117 | `"    checks: dict[str, Any] = {\"health\": \"passed\"}"` | — |
| [SRC-A8360B1B03-L000118](../../scripts/hosted_smoke_test.py#L118) | 118 | `""` | — |
| [SRC-A8360B1B03-L000119](../../scripts/hosted_smoke_test.py#L119) | 119 | `"    build = health.get(\"build\")"` | — |
| [SRC-A8360B1B03-L000120](../../scripts/hosted_smoke_test.py#L120) | 120 | `"    reported_sha = build.get(\"sha\") if isinstance(build, dict) else None"` | — |
| [SRC-A8360B1B03-L000121](../../scripts/hosted_smoke_test.py#L121) | 121 | `"    if expected_sha is not None:"` | — |
| [SRC-A8360B1B03-L000122](../../scripts/hosted_smoke_test.py#L122) | 122 | `"        expected = expected_sha.strip().lower()"` | — |
| [SRC-A8360B1B03-L000123](../../scripts/hosted_smoke_test.py#L123) | 123 | `"        if not isinstance(reported_sha, str) or reported_sha.lower() != expected:"` | — |
| [SRC-A8360B1B03-L000124](../../scripts/hosted_smoke_test.py#L124) | 124 | `"            raise SmokeError("` | — |
| [SRC-A8360B1B03-L000125](../../scripts/hosted_smoke_test.py#L125) | 125 | `"                \"The deployed service SHA does not match the expected Git commit. \""` | — |
| [SRC-A8360B1B03-L000126](../../scripts/hosted_smoke_test.py#L126) | 126 | `"                \"Pass OMARAI_BUILD_SHA as a Docker build argument for the deployed revision, \""` | — |
| [SRC-A8360B1B03-L000127](../../scripts/hosted_smoke_test.py#L127) | 127 | `"                \"then rebuild and redeploy.\""` | — |
| [SRC-A8360B1B03-L000128](../../scripts/hosted_smoke_test.py#L128) | 128 | `"            )"` | — |
| [SRC-A8360B1B03-L000129](../../scripts/hosted_smoke_test.py#L129) | 129 | `"        checks[\"build_identity\"] = {"` | — |
| [SRC-A8360B1B03-L000130](../../scripts/hosted_smoke_test.py#L130) | 130 | `"            \"status\": \"passed\","` | — |
| [SRC-A8360B1B03-L000131](../../scripts/hosted_smoke_test.py#L131) | 131 | `"            \"expected_sha\": expected,"` | — |
| [SRC-A8360B1B03-L000132](../../scripts/hosted_smoke_test.py#L132) | 132 | `"            \"reported_sha\": reported_sha.lower(),"` | — |
| [SRC-A8360B1B03-L000133](../../scripts/hosted_smoke_test.py#L133) | 133 | `"        }"` | — |
| [SRC-A8360B1B03-L000134](../../scripts/hosted_smoke_test.py#L134) | 134 | `"    else:"` | — |
| [SRC-A8360B1B03-L000135](../../scripts/hosted_smoke_test.py#L135) | 135 | `"        checks[\"build_identity\"] = {"` | — |
| [SRC-A8360B1B03-L000136](../../scripts/hosted_smoke_test.py#L136) | 136 | `"            \"status\": \"not_checked\","` | — |
| [SRC-A8360B1B03-L000137](../../scripts/hosted_smoke_test.py#L137) | 137 | `"            \"reported_sha\": reported_sha if isinstance(reported_sha, str) else \"unknown\","` | — |
| [SRC-A8360B1B03-L000138](../../scripts/hosted_smoke_test.py#L138) | 138 | `"        }"` | — |
| [SRC-A8360B1B03-L000139](../../scripts/hosted_smoke_test.py#L139) | 139 | `""` | — |
| [SRC-A8360B1B03-L000140](../../scripts/hosted_smoke_test.py#L140) | 140 | `"    status, _ = request_json("` | — |
| [SRC-A8360B1B03-L000141](../../scripts/hosted_smoke_test.py#L141) | 141 | `"        f\"{origin}/api/agent\", payload={\"question\": \"اختبار رفض الوصول غير المصرح به\"},"` | — |
| [SRC-A8360B1B03-L000142](../../scripts/hosted_smoke_test.py#L142) | 142 | `"        timeout=min(timeout, 20),"` | — |
| [SRC-A8360B1B03-L000143](../../scripts/hosted_smoke_test.py#L143) | 143 | `"    )"` | — |
| [SRC-A8360B1B03-L000144](../../scripts/hosted_smoke_test.py#L144) | 144 | `"    if status != 401:"` | — |
| [SRC-A8360B1B03-L000145](../../scripts/hosted_smoke_test.py#L145) | 145 | `"        raise SmokeError(f\"Unauthenticated POST /api/agent should return 401, received {status}.\")"` | — |
| [SRC-A8360B1B03-L000146](../../scripts/hosted_smoke_test.py#L146) | 146 | `"    checks[\"authentication\"] = \"passed\""` | — |
| [SRC-A8360B1B03-L000147](../../scripts/hosted_smoke_test.py#L147) | 147 | `""` | — |
| [SRC-A8360B1B03-L000148](../../scripts/hosted_smoke_test.py#L148) | 148 | `"    # These are real network/provider calls and may incur model/search usage."` | — |
| [SRC-A8360B1B03-L000149](../../scripts/hosted_smoke_test.py#L149) | 149 | `"    status, diagnostics = request_json("` | — |
| [SRC-A8360B1B03-L000150](../../scripts/hosted_smoke_test.py#L150) | 150 | `"        f\"{origin}/api/diagnostics\", token=token,"` | — |
| [SRC-A8360B1B03-L000151](../../scripts/hosted_smoke_test.py#L151) | 151 | `"        payload={\"test_model\": True, \"test_social\": False}, timeout=timeout,"` | — |
| [SRC-A8360B1B03-L000152](../../scripts/hosted_smoke_test.py#L152) | 152 | `"    )"` | — |
| [SRC-A8360B1B03-L000153](../../scripts/hosted_smoke_test.py#L153) | 153 | `"    if status != 200 or not diagnostics:"` | — |
| [SRC-A8360B1B03-L000154](../../scripts/hosted_smoke_test.py#L154) | 154 | `"        raise SmokeError(f\"Authenticated diagnostics failed (HTTP {status}).\")"` | — |
| [SRC-A8360B1B03-L000155](../../scripts/hosted_smoke_test.py#L155) | 155 | `"    parts = diagnostics.get(\"checks\", {})"` | — |
| [SRC-A8360B1B03-L000156](../../scripts/hosted_smoke_test.py#L156) | 156 | `"    web = parts.get(\"web_search\", {}) if isinstance(parts, dict) else {}"` | — |
| [SRC-A8360B1B03-L000157](../../scripts/hosted_smoke_test.py#L157) | 157 | `"    model = parts.get(\"language_model\", {}) if isinstance(parts, dict) else {}"` | — |
| [SRC-A8360B1B03-L000158](../../scripts/hosted_smoke_test.py#L158) | 158 | `"    if not isinstance(web, dict) or web.get(\"status\") != \"passed\":"` | — |
| [SRC-A8360B1B03-L000159](../../scripts/hosted_smoke_test.py#L159) | 159 | `"        raise SmokeError(\"The real web-search connectivity test did not pass.\")"` | — |
| [SRC-A8360B1B03-L000160](../../scripts/hosted_smoke_test.py#L160) | 160 | `"    if not isinstance(model, dict) or model.get(\"status\") != \"passed\":"` | — |
| [SRC-A8360B1B03-L000161](../../scripts/hosted_smoke_test.py#L161) | 161 | `"        raise SmokeError(\"The configured language model did not pass a real completion test.\")"` | — |
| [SRC-A8360B1B03-L000162](../../scripts/hosted_smoke_test.py#L162) | 162 | `"    checks[\"live_search\"] = {"` | — |
| [SRC-A8360B1B03-L000163](../../scripts/hosted_smoke_test.py#L163) | 163 | `"        \"status\": \"passed\", \"result_count\": web.get(\"result_count\", 0),"` | — |
| [SRC-A8360B1B03-L000164](../../scripts/hosted_smoke_test.py#L164) | 164 | `"        \"provider_counts\": web.get(\"provider_counts\", {}),"` | — |
| [SRC-A8360B1B03-L000165](../../scripts/hosted_smoke_test.py#L165) | 165 | `"    }"` | — |
| [SRC-A8360B1B03-L000166](../../scripts/hosted_smoke_test.py#L166) | 166 | `"    checks[\"language_model\"] = {\"status\": \"passed\", \"response_received\": True}"` | — |
| [SRC-A8360B1B03-L000167](../../scripts/hosted_smoke_test.py#L167) | 167 | `""` | — |
| [SRC-A8360B1B03-L000168](../../scripts/hosted_smoke_test.py#L168) | 168 | `"    status, answer = request_json("` | — |
| [SRC-A8360B1B03-L000169](../../scripts/hosted_smoke_test.py#L169) | 169 | `"        f\"{origin}/api/agent\", token=token, timeout=timeout,"` | — |
| [SRC-A8360B1B03-L000170](../../scripts/hosted_smoke_test.py#L170) | 170 | `"        payload={"` | — |
| [SRC-A8360B1B03-L000171](../../scripts/hosted_smoke_test.py#L171) | 171 | `"            \"question\": \"اختبار تشغيل: ما عاصمة مصر؟ أجب بالعربية بإيجاز واستند إلى المصادر.\","` | — |
| [SRC-A8360B1B03-L000172](../../scripts/hosted_smoke_test.py#L172) | 172 | `"            \"history\": [], \"mode\": \"auto\","` | — |
| [SRC-A8360B1B03-L000173](../../scripts/hosted_smoke_test.py#L173) | 173 | `"        },"` | — |
| [SRC-A8360B1B03-L000174](../../scripts/hosted_smoke_test.py#L174) | 174 | `"    )"` | — |
| [SRC-A8360B1B03-L000175](../../scripts/hosted_smoke_test.py#L175) | 175 | `"    if status != 200 or not answer:"` | — |
| [SRC-A8360B1B03-L000176](../../scripts/hosted_smoke_test.py#L176) | 176 | `"        raise SmokeError(f\"Authenticated agent request failed (HTTP {status}).\")"` | — |
| [SRC-A8360B1B03-L000177](../../scripts/hosted_smoke_test.py#L177) | 177 | `"    sources = answer.get(\"sources\")"` | — |
| [SRC-A8360B1B03-L000178](../../scripts/hosted_smoke_test.py#L178) | 178 | `"    usable = ["` | — |
| [SRC-A8360B1B03-L000179](../../scripts/hosted_smoke_test.py#L179) | 179 | `"        item for item in sources if isinstance(item, dict)"` | — |
| [SRC-A8360B1B03-L000180](../../scripts/hosted_smoke_test.py#L180) | 180 | `"        and isinstance(item.get(\"url\"), str)"` | — |
| [SRC-A8360B1B03-L000181](../../scripts/hosted_smoke_test.py#L181) | 181 | `"        and urllib.parse.urlsplit(item[\"url\"]).scheme in {\"http\", \"https\"}"` | — |
| [SRC-A8360B1B03-L000182](../../scripts/hosted_smoke_test.py#L182) | 182 | `"        and urllib.parse.urlsplit(item[\"url\"]).hostname"` | — |
| [SRC-A8360B1B03-L000183](../../scripts/hosted_smoke_test.py#L183) | 183 | `"    ] if isinstance(sources, list) else []"` | — |
| [SRC-A8360B1B03-L000184](../../scripts/hosted_smoke_test.py#L184) | 184 | `"    if answer.get(\"used_web_search\") is not True or not usable:"` | — |
| [SRC-A8360B1B03-L000185](../../scripts/hosted_smoke_test.py#L185) | 185 | `"        raise SmokeError(\"Agent request did not return a live web search with usable source URLs.\")"` | — |
| [SRC-A8360B1B03-L000186](../../scripts/hosted_smoke_test.py#L186) | 186 | `"    if answer.get(\"used_language_model\") is not True:"` | — |
| [SRC-A8360B1B03-L000187](../../scripts/hosted_smoke_test.py#L187) | 187 | `"        raise SmokeError(\"Agent request did not confirm that a language model was used.\")"` | — |
| [SRC-A8360B1B03-L000188](../../scripts/hosted_smoke_test.py#L188) | 188 | `"    report = answer.get(\"search_report\")"` | — |
| [SRC-A8360B1B03-L000189](../../scripts/hosted_smoke_test.py#L189) | 189 | `"    checks[\"agent_request\"] = {"` | — |
| [SRC-A8360B1B03-L000190](../../scripts/hosted_smoke_test.py#L190) | 190 | `"        \"status\": \"passed\", \"source_count\": len(usable),"` | — |
| [SRC-A8360B1B03-L000191](../../scripts/hosted_smoke_test.py#L191) | 191 | `"        \"direct_pages_read\": report.get(\"pages_fetched\") if isinstance(report, dict) else None,"` | — |
| [SRC-A8360B1B03-L000192](../../scripts/hosted_smoke_test.py#L192) | 192 | `"        \"providers_reported\": report.get(\"providers_used\", []) if isinstance(report, dict) else [],"` | — |
| [SRC-A8360B1B03-L000193](../../scripts/hosted_smoke_test.py#L193) | 193 | `"        \"answer_received\": bool(str(answer.get(\"answer\", \"\")).strip()),"` | — |
| [SRC-A8360B1B03-L000194](../../scripts/hosted_smoke_test.py#L194) | 194 | `"    }"` | — |
| [SRC-A8360B1B03-L000195](../../scripts/hosted_smoke_test.py#L195) | 195 | `"    return {"` | — |
| [SRC-A8360B1B03-L000196](../../scripts/hosted_smoke_test.py#L196) | 196 | `"        \"result\": \"passed\", \"target_host\": urllib.parse.urlsplit(origin).hostname,"` | — |
| [SRC-A8360B1B03-L000197](../../scripts/hosted_smoke_test.py#L197) | 197 | `"        \"checks\": checks,"` | — |
| [SRC-A8360B1B03-L000198](../../scripts/hosted_smoke_test.py#L198) | 198 | `"        \"note\": \"This proves the request path worked at test time, not continuous uptime. Provider usage may incur charges.\","` | — |
| [SRC-A8360B1B03-L000199](../../scripts/hosted_smoke_test.py#L199) | 199 | `"    }"` | — |
| [SRC-A8360B1B03-L000200](../../scripts/hosted_smoke_test.py#L200) | 200 | `""` | — |
| [SRC-A8360B1B03-L000201](../../scripts/hosted_smoke_test.py#L201) | 201 | `""` | — |
| [SRC-A8360B1B03-L000202](../../scripts/hosted_smoke_test.py#L202) | 202 | `"def main() -> int:"` | — |
| [SRC-A8360B1B03-L000203](../../scripts/hosted_smoke_test.py#L203) | 203 | `"    parser = argparse.ArgumentParser(description=\"Run live acceptance checks against hosted Omarai.\")"` | — |
| [SRC-A8360B1B03-L000204](../../scripts/hosted_smoke_test.py#L204) | 204 | `"    parser.add_argument(\"--base-url\", default=os.getenv(\"OMARAI_BASE_URL\", \"\"))"` | — |
| [SRC-A8360B1B03-L000205](../../scripts/hosted_smoke_test.py#L205) | 205 | `"    parser.add_argument(\"--timeout\", type=float, default=90)"` | — |
| [SRC-A8360B1B03-L000206](../../scripts/hosted_smoke_test.py#L206) | 206 | `"    parser.add_argument("` | — |
| [SRC-A8360B1B03-L000207](../../scripts/hosted_smoke_test.py#L207) | 207 | `"        \"--expected-sha\","` | — |
| [SRC-A8360B1B03-L000208](../../scripts/hosted_smoke_test.py#L208) | 208 | `"        default=os.getenv(\"OMARAI_EXPECTED_BUILD_SHA\", \"\"),"` | — |
| [SRC-A8360B1B03-L000209](../../scripts/hosted_smoke_test.py#L209) | 209 | `"        help=\"Require the deployed image to report this full 40-character source Git SHA.\","` | — |
| [SRC-A8360B1B03-L000210](../../scripts/hosted_smoke_test.py#L210) | 210 | `"    )"` | — |
| [SRC-A8360B1B03-L000211](../../scripts/hosted_smoke_test.py#L211) | 211 | `"    parser.add_argument(\"--allow-http\", action=\"store_true\","` | — |
| [SRC-A8360B1B03-L000212](../../scripts/hosted_smoke_test.py#L212) | 212 | `"                        help=\"Allow HTTP only for localhost/127.0.0.1/::1 testing.\")"` | — |
| [SRC-A8360B1B03-L000213](../../scripts/hosted_smoke_test.py#L213) | 213 | `"    args = parser.parse_args()"` | — |
| [SRC-A8360B1B03-L000214](../../scripts/hosted_smoke_test.py#L214) | 214 | `"    try:"` | — |
| [SRC-A8360B1B03-L000215](../../scripts/hosted_smoke_test.py#L215) | 215 | `"        result = run_smoke("` | — |
| [SRC-A8360B1B03-L000216](../../scripts/hosted_smoke_test.py#L216) | 216 | `"            args.base_url,"` | — |
| [SRC-A8360B1B03-L000217](../../scripts/hosted_smoke_test.py#L217) | 217 | `"            os.getenv(\"OMARAI_ACCESS_TOKEN\", \"\").strip(),"` | — |
| [SRC-A8360B1B03-L000218](../../scripts/hosted_smoke_test.py#L218) | 218 | `"            timeout=max(5, min(args.timeout, 240)),"` | — |
| [SRC-A8360B1B03-L000219](../../scripts/hosted_smoke_test.py#L219) | 219 | `"            allow_http=args.allow_http,"` | — |
| [SRC-A8360B1B03-L000220](../../scripts/hosted_smoke_test.py#L220) | 220 | `"            expected_sha=args.expected_sha or None,"` | — |
| [SRC-A8360B1B03-L000221](../../scripts/hosted_smoke_test.py#L221) | 221 | `"        )"` | — |
| [SRC-A8360B1B03-L000222](../../scripts/hosted_smoke_test.py#L222) | 222 | `"    except SmokeError as exc:"` | — |
| [SRC-A8360B1B03-L000223](../../scripts/hosted_smoke_test.py#L223) | 223 | `"        print(json.dumps({\"result\": \"failed\", \"error\": str(exc)}, ensure_ascii=False, indent=2))"` | — |
| [SRC-A8360B1B03-L000224](../../scripts/hosted_smoke_test.py#L224) | 224 | `"        return 1"` | — |
| [SRC-A8360B1B03-L000225](../../scripts/hosted_smoke_test.py#L225) | 225 | `"    print(json.dumps(result, ensure_ascii=False, indent=2))"` | — |
| [SRC-A8360B1B03-L000226](../../scripts/hosted_smoke_test.py#L226) | 226 | `"    return 0"` | — |
| [SRC-A8360B1B03-L000227](../../scripts/hosted_smoke_test.py#L227) | 227 | `""` | — |
| [SRC-A8360B1B03-L000228](../../scripts/hosted_smoke_test.py#L228) | 228 | `""` | — |
| [SRC-A8360B1B03-L000229](../../scripts/hosted_smoke_test.py#L229) | 229 | `"if __name__ == \"__main__\":"` | — |
| [SRC-A8360B1B03-L000230](../../scripts/hosted_smoke_test.py#L230) | 230 | `"    sys.exit(main())"` | — |
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
| [SRC-4FFD5AFC54-L000030](../../scripts/run_answer_quality_benchmark.py#L30) | 30 | `"import sys"` | — |
| [SRC-4FFD5AFC54-L000031](../../scripts/run_answer_quality_benchmark.py#L31) | 31 | `"import time"` | — |
| [SRC-4FFD5AFC54-L000032](../../scripts/run_answer_quality_benchmark.py#L32) | 32 | `"import urllib.error"` | — |
| [SRC-4FFD5AFC54-L000033](../../scripts/run_answer_quality_benchmark.py#L33) | 33 | `"import urllib.parse"` | — |
| [SRC-4FFD5AFC54-L000034](../../scripts/run_answer_quality_benchmark.py#L34) | 34 | `"import urllib.request"` | — |
| [SRC-4FFD5AFC54-L000035](../../scripts/run_answer_quality_benchmark.py#L35) | 35 | `"from datetime import UTC, datetime"` | — |
| [SRC-4FFD5AFC54-L000036](../../scripts/run_answer_quality_benchmark.py#L36) | 36 | `"from pathlib import Path"` | — |
| [SRC-4FFD5AFC54-L000037](../../scripts/run_answer_quality_benchmark.py#L37) | 37 | `""` | — |
| [SRC-4FFD5AFC54-L000038](../../scripts/run_answer_quality_benchmark.py#L38) | 38 | `"ROOT = Path(__file__).resolve().parents[1]"` | — |
| [SRC-4FFD5AFC54-L000039](../../scripts/run_answer_quality_benchmark.py#L39) | 39 | `"DEFAULT_CORPUS = ROOT / \"tests\" / \"fixtures\" / \"answer_quality_cases.json\""` | — |
| [SRC-4FFD5AFC54-L000040](../../scripts/run_answer_quality_benchmark.py#L40) | 40 | `"MAX_RESPONSE_BYTES = 2_000_000"` | — |
| [SRC-4FFD5AFC54-L000041](../../scripts/run_answer_quality_benchmark.py#L41) | 41 | `""` | — |
| [SRC-4FFD5AFC54-L000042](../../scripts/run_answer_quality_benchmark.py#L42) | 42 | `""` | — |
| [SRC-4FFD5AFC54-L000043](../../scripts/run_answer_quality_benchmark.py#L43) | 43 | `"def _model_calls_from_payload(payload: dict) -> list[dict]:"` | — |
| [SRC-4FFD5AFC54-L000044](../../scripts/run_answer_quality_benchmark.py#L44) | 44 | `"    \"\"\"Read only structured per-request model-call metadata from an API response.\"\"\""` | — |
| [SRC-4FFD5AFC54-L000045](../../scripts/run_answer_quality_benchmark.py#L45) | 45 | `"    report = payload.get(\"search_report\")"` | — |
| [SRC-4FFD5AFC54-L000046](../../scripts/run_answer_quality_benchmark.py#L46) | 46 | `"    understanding = payload.get(\"task_understanding\")"` | — |
| [SRC-4FFD5AFC54-L000047](../../scripts/run_answer_quality_benchmark.py#L47) | 47 | `"    candidates = ["` | — |
| [SRC-4FFD5AFC54-L000048](../../scripts/run_answer_quality_benchmark.py#L48) | 48 | `"        payload.get(\"model_calls\"),"` | — |
| [SRC-4FFD5AFC54-L000049](../../scripts/run_answer_quality_benchmark.py#L49) | 49 | `"        report.get(\"model_calls\") if isinstance(report, dict) else None,"` | — |
| [SRC-4FFD5AFC54-L000050](../../scripts/run_answer_quality_benchmark.py#L50) | 50 | `"        understanding.get(\"model_calls\") if isinstance(understanding, dict) else None,"` | — |
| [SRC-4FFD5AFC54-L000051](../../scripts/run_answer_quality_benchmark.py#L51) | 51 | `"    ]"` | — |
| [SRC-4FFD5AFC54-L000052](../../scripts/run_answer_quality_benchmark.py#L52) | 52 | `"    for candidate in candidates:"` | — |
| [SRC-4FFD5AFC54-L000053](../../scripts/run_answer_quality_benchmark.py#L53) | 53 | `"        if isinstance(candidate, list):"` | — |
| [SRC-4FFD5AFC54-L000054](../../scripts/run_answer_quality_benchmark.py#L54) | 54 | `"            return [item for item in candidate if isinstance(item, dict)]"` | — |
| [SRC-4FFD5AFC54-L000055](../../scripts/run_answer_quality_benchmark.py#L55) | 55 | `"    return []"` | — |
| [SRC-4FFD5AFC54-L000056](../../scripts/run_answer_quality_benchmark.py#L56) | 56 | `""` | — |
| [SRC-4FFD5AFC54-L000057](../../scripts/run_answer_quality_benchmark.py#L57) | 57 | `""` | — |
| [SRC-4FFD5AFC54-L000058](../../scripts/run_answer_quality_benchmark.py#L58) | 58 | `"def _finite_nonnegative_number(value) -> float \| None:"` | — |
| [SRC-4FFD5AFC54-L000059](../../scripts/run_answer_quality_benchmark.py#L59) | 59 | `"    if isinstance(value, bool) or not isinstance(value, (int, float)):"` | — |
| [SRC-4FFD5AFC54-L000060](../../scripts/run_answer_quality_benchmark.py#L60) | 60 | `"        return None"` | — |
| [SRC-4FFD5AFC54-L000061](../../scripts/run_answer_quality_benchmark.py#L61) | 61 | `"    number = float(value)"` | — |
| [SRC-4FFD5AFC54-L000062](../../scripts/run_answer_quality_benchmark.py#L62) | 62 | `"    if not math.isfinite(number) or number < 0:"` | — |
| [SRC-4FFD5AFC54-L000063](../../scripts/run_answer_quality_benchmark.py#L63) | 63 | `"        return None"` | — |
| [SRC-4FFD5AFC54-L000064](../../scripts/run_answer_quality_benchmark.py#L64) | 64 | `"    return number"` | — |
| [SRC-4FFD5AFC54-L000065](../../scripts/run_answer_quality_benchmark.py#L65) | 65 | `""` | — |
| [SRC-4FFD5AFC54-L000066](../../scripts/run_answer_quality_benchmark.py#L66) | 66 | `""` | — |
| [SRC-4FFD5AFC54-L000067](../../scripts/run_answer_quality_benchmark.py#L67) | 67 | `"def _response_metrics(payload: dict \| str, expected_strategy: str, transport_ok: bool) -> dict:"` | — |
| [SRC-4FFD5AFC54-L000068](../../scripts/run_answer_quality_benchmark.py#L68) | 68 | `"    \"\"\"Derive conservative telemetry; never infer semantic correctness from HTTP 200.\"\"\""` | — |
| [SRC-4FFD5AFC54-L000069](../../scripts/run_answer_quality_benchmark.py#L69) | 69 | `"    if not isinstance(payload, dict):"` | — |
| [SRC-4FFD5AFC54-L000070](../../scripts/run_answer_quality_benchmark.py#L70) | 70 | `"        payload = {}"` | — |
| [SRC-4FFD5AFC54-L000071](../../scripts/run_answer_quality_benchmark.py#L71) | 71 | `"    report = payload.get(\"search_report\")"` | — |
| [SRC-4FFD5AFC54-L000072](../../scripts/run_answer_quality_benchmark.py#L72) | 72 | `"    report = report if isinstance(report, dict) else {}"` | — |
| [SRC-4FFD5AFC54-L000073](../../scripts/run_answer_quality_benchmark.py#L73) | 73 | `"    outcome = report.get(\"search_outcome\")"` | — |
| [SRC-4FFD5AFC54-L000074](../../scripts/run_answer_quality_benchmark.py#L74) | 74 | `"    pipeline = report.get(\"pipeline_completion_status\")"` | — |
| [SRC-4FFD5AFC54-L000075](../../scripts/run_answer_quality_benchmark.py#L75) | 75 | `"    if expected_strategy != \"web_search\":"` | — |
| [SRC-4FFD5AFC54-L000076](../../scripts/run_answer_quality_benchmark.py#L76) | 76 | `"        tool_status = \"NOT_APPLICABLE\""` | — |
| [SRC-4FFD5AFC54-L000077](../../scripts/run_answer_quality_benchmark.py#L77) | 77 | `"    elif not transport_ok:"` | — |
| [SRC-4FFD5AFC54-L000078](../../scripts/run_answer_quality_benchmark.py#L78) | 78 | `"        tool_status = \"TRANSPORT_FAILED\""` | — |
| [SRC-4FFD5AFC54-L000079](../../scripts/run_answer_quality_benchmark.py#L79) | 79 | `"    elif outcome == \"attempted_with_usable_sources\":"` | — |
| [SRC-4FFD5AFC54-L000080](../../scripts/run_answer_quality_benchmark.py#L80) | 80 | `"        tool_status = \"SUCCESS_WITH_USABLE_RESULTS\""` | — |
| [SRC-4FFD5AFC54-L000081](../../scripts/run_answer_quality_benchmark.py#L81) | 81 | `"    elif outcome == \"attempted_no_usable_sources\":"` | — |
| [SRC-4FFD5AFC54-L000082](../../scripts/run_answer_quality_benchmark.py#L82) | 82 | `"        tool_status = \"ATTEMPTED_NO_USABLE_RESULTS\""` | — |
| [SRC-4FFD5AFC54-L000083](../../scripts/run_answer_quality_benchmark.py#L83) | 83 | `"    elif outcome == \"attempted_research_error\":"` | — |
| [SRC-4FFD5AFC54-L000084](../../scripts/run_answer_quality_benchmark.py#L84) | 84 | `"        tool_status = \"TOOL_FAILED\""` | — |
| [SRC-4FFD5AFC54-L000085](../../scripts/run_answer_quality_benchmark.py#L85) | 85 | `"    elif outcome == \"unknown_after_budget_exhaustion\":"` | — |
| [SRC-4FFD5AFC54-L000086](../../scripts/run_answer_quality_benchmark.py#L86) | 86 | `"        tool_status = \"BUDGET_EXHAUSTED\""` | — |
| [SRC-4FFD5AFC54-L000087](../../scripts/run_answer_quality_benchmark.py#L87) | 87 | `"    elif outcome == \"not_attempted\":"` | — |
| [SRC-4FFD5AFC54-L000088](../../scripts/run_answer_quality_benchmark.py#L88) | 88 | `"        tool_status = \"NOT_ATTEMPTED\""` | — |
| [SRC-4FFD5AFC54-L000089](../../scripts/run_answer_quality_benchmark.py#L89) | 89 | `"    else:"` | — |
| [SRC-4FFD5AFC54-L000090](../../scripts/run_answer_quality_benchmark.py#L90) | 90 | `"        tool_status = \"UNKNOWN\""` | — |
| [SRC-4FFD5AFC54-L000091](../../scripts/run_answer_quality_benchmark.py#L91) | 91 | `""` | — |
| [SRC-4FFD5AFC54-L000092](../../scripts/run_answer_quality_benchmark.py#L92) | 92 | `"    calls = _model_calls_from_payload(payload)"` | — |
| [SRC-4FFD5AFC54-L000093](../../scripts/run_answer_quality_benchmark.py#L93) | 93 | `"    reported_costs = []"` | — |
| [SRC-4FFD5AFC54-L000094](../../scripts/run_answer_quality_benchmark.py#L94) | 94 | `"    for call in calls:"` | — |
| [SRC-4FFD5AFC54-L000095](../../scripts/run_answer_quality_benchmark.py#L95) | 95 | `"        usage = call.get(\"provider_usage\")"` | — |
| [SRC-4FFD5AFC54-L000096](../../scripts/run_answer_quality_benchmark.py#L96) | 96 | `"        if not isinstance(usage, dict):"` | — |
| [SRC-4FFD5AFC54-L000097](../../scripts/run_answer_quality_benchmark.py#L97) | 97 | `"            continue"` | — |
| [SRC-4FFD5AFC54-L000098](../../scripts/run_answer_quality_benchmark.py#L98) | 98 | `"        cost = _finite_nonnegative_number(usage.get(\"cost_usd\"))"` | — |
| [SRC-4FFD5AFC54-L000099](../../scripts/run_answer_quality_benchmark.py#L99) | 99 | `"        if cost is not None:"` | — |
| [SRC-4FFD5AFC54-L000100](../../scripts/run_answer_quality_benchmark.py#L100) | 100 | `"            reported_costs.append(cost)"` | — |
| [SRC-4FFD5AFC54-L000101](../../scripts/run_answer_quality_benchmark.py#L101) | 101 | `""` | — |
| [SRC-4FFD5AFC54-L000102](../../scripts/run_answer_quality_benchmark.py#L102) | 102 | `"    if not calls:"` | — |
| [SRC-4FFD5AFC54-L000103](../../scripts/run_answer_quality_benchmark.py#L103) | 103 | `"        cost_status = \"NO_MODEL_CALL_METADATA\""` | — |
| [SRC-4FFD5AFC54-L000104](../../scripts/run_answer_quality_benchmark.py#L104) | 104 | `"    elif len(reported_costs) == len(calls):"` | — |
| [SRC-4FFD5AFC54-L000105](../../scripts/run_answer_quality_benchmark.py#L105) | 105 | `"        cost_status = \"COMPLETE_FOR_RETURNED_MODEL_CALLS\""` | — |
| [SRC-4FFD5AFC54-L000106](../../scripts/run_answer_quality_benchmark.py#L106) | 106 | `"    elif reported_costs:"` | — |
| [SRC-4FFD5AFC54-L000107](../../scripts/run_answer_quality_benchmark.py#L107) | 107 | `"        cost_status = \"PARTIAL_PROVIDER_REPORTED_MODEL_COST\""` | — |
| [SRC-4FFD5AFC54-L000108](../../scripts/run_answer_quality_benchmark.py#L108) | 108 | `"    else:"` | — |
| [SRC-4FFD5AFC54-L000109](../../scripts/run_answer_quality_benchmark.py#L109) | 109 | `"        cost_status = \"PROVIDER_COST_NOT_REPORTED\""` | — |
| [SRC-4FFD5AFC54-L000110](../../scripts/run_answer_quality_benchmark.py#L110) | 110 | `""` | — |
| [SRC-4FFD5AFC54-L000111](../../scripts/run_answer_quality_benchmark.py#L111) | 111 | `"    return {"` | — |
| [SRC-4FFD5AFC54-L000112](../../scripts/run_answer_quality_benchmark.py#L112) | 112 | `"        \"search_outcome\": outcome if isinstance(outcome, str) else \"unknown\","` | — |
| [SRC-4FFD5AFC54-L000113](../../scripts/run_answer_quality_benchmark.py#L113) | 113 | `"        \"pipeline_completion_status\": pipeline if isinstance(pipeline, str) else \"unknown\","` | — |
| [SRC-4FFD5AFC54-L000114](../../scripts/run_answer_quality_benchmark.py#L114) | 114 | `"        \"tool_status\": tool_status,"` | — |
| [SRC-4FFD5AFC54-L000115](../../scripts/run_answer_quality_benchmark.py#L115) | 115 | `"        \"source_count\": len(payload.get(\"sources\", [])) if isinstance(payload.get(\"sources\"), list) else None,"` | — |
| [SRC-4FFD5AFC54-L000116](../../scripts/run_answer_quality_benchmark.py#L116) | 116 | `"        \"model_call_count\": len(calls),"` | — |
| [SRC-4FFD5AFC54-L000117](../../scripts/run_answer_quality_benchmark.py#L117) | 117 | `"        \"provider_reported_model_cost_usd\": round(sum(reported_costs), 10) if reported_costs else None,"` | — |
| [SRC-4FFD5AFC54-L000118](../../scripts/run_answer_quality_benchmark.py#L118) | 118 | `"        \"provider_reported_model_cost_call_count\": len(reported_costs),"` | — |
| [SRC-4FFD5AFC54-L000119](../../scripts/run_answer_quality_benchmark.py#L119) | 119 | `"        \"provider_reported_model_cost_status\": cost_status,"` | — |
| [SRC-4FFD5AFC54-L000120](../../scripts/run_answer_quality_benchmark.py#L120) | 120 | `"        \"request_cost_usd\": None,"` | — |
| [SRC-4FFD5AFC54-L000121](../../scripts/run_answer_quality_benchmark.py#L121) | 121 | `"        \"request_cost_status\": \"NOT_MEASURED_TOTAL_CONNECTOR_COSTS_NOT_EXPOSED\","` | — |
| [SRC-4FFD5AFC54-L000122](../../scripts/run_answer_quality_benchmark.py#L122) | 122 | `"    }"` | — |
| [SRC-4FFD5AFC54-L000123](../../scripts/run_answer_quality_benchmark.py#L123) | 123 | `""` | — |
| [SRC-4FFD5AFC54-L000124](../../scripts/run_answer_quality_benchmark.py#L124) | 124 | `""` | — |
| [SRC-4FFD5AFC54-L000125](../../scripts/run_answer_quality_benchmark.py#L125) | 125 | `"def validate_base_url(base_url: str, *, token_present: bool = False) -> str:"` | — |
| [SRC-4FFD5AFC54-L000126](../../scripts/run_answer_quality_benchmark.py#L126) | 126 | `"    \"\"\"Validate and normalize an API origin before any request can carry a token.\"\"\""` | — |
| [SRC-4FFD5AFC54-L000127](../../scripts/run_answer_quality_benchmark.py#L127) | 127 | `"    if not isinstance(base_url, str) or not base_url.strip():"` | — |
| [SRC-4FFD5AFC54-L000128](../../scripts/run_answer_quality_benchmark.py#L128) | 128 | `"        raise ValueError(\"Base URL must be a non-empty HTTP(S) origin.\")"` | — |
| [SRC-4FFD5AFC54-L000129](../../scripts/run_answer_quality_benchmark.py#L129) | 129 | `"    try:"` | — |
| [SRC-4FFD5AFC54-L000130](../../scripts/run_answer_quality_benchmark.py#L130) | 130 | `"        parsed = urllib.parse.urlsplit(base_url.strip())"` | — |
| [SRC-4FFD5AFC54-L000131](../../scripts/run_answer_quality_benchmark.py#L131) | 131 | `"        scheme = parsed.scheme.lower()"` | — |
| [SRC-4FFD5AFC54-L000132](../../scripts/run_answer_quality_benchmark.py#L132) | 132 | `"        host = (parsed.hostname or \"\").lower().rstrip(\".\")"` | — |
| [SRC-4FFD5AFC54-L000133](../../scripts/run_answer_quality_benchmark.py#L133) | 133 | `"        port = parsed.port"` | — |
| [SRC-4FFD5AFC54-L000134](../../scripts/run_answer_quality_benchmark.py#L134) | 134 | `"    except ValueError as exc:"` | — |
| [SRC-4FFD5AFC54-L000135](../../scripts/run_answer_quality_benchmark.py#L135) | 135 | `"        raise ValueError(\"Base URL is malformed.\") from exc"` | — |
| [SRC-4FFD5AFC54-L000136](../../scripts/run_answer_quality_benchmark.py#L136) | 136 | `""` | — |
| [SRC-4FFD5AFC54-L000137](../../scripts/run_answer_quality_benchmark.py#L137) | 137 | `"    if scheme not in {\"http\", \"https\"} or not host:"` | — |
| [SRC-4FFD5AFC54-L000138](../../scripts/run_answer_quality_benchmark.py#L138) | 138 | `"        raise ValueError(\"Base URL must use HTTP or HTTPS and include a hostname.\")"` | — |
| [SRC-4FFD5AFC54-L000139](../../scripts/run_answer_quality_benchmark.py#L139) | 139 | `"    if parsed.username is not None or parsed.password is not None:"` | — |
| [SRC-4FFD5AFC54-L000140](../../scripts/run_answer_quality_benchmark.py#L140) | 140 | `"        raise ValueError(\"Base URL must not include a username or password.\")"` | — |
| [SRC-4FFD5AFC54-L000141](../../scripts/run_answer_quality_benchmark.py#L141) | 141 | `"    if parsed.path not in {\"\", \"/\"} or parsed.query or parsed.fragment:"` | — |
| [SRC-4FFD5AFC54-L000142](../../scripts/run_answer_quality_benchmark.py#L142) | 142 | `"        raise ValueError(\"Base URL must contain only the origin, without path, query, or fragment.\")"` | — |
| [SRC-4FFD5AFC54-L000143](../../scripts/run_answer_quality_benchmark.py#L143) | 143 | `""` | — |
| [SRC-4FFD5AFC54-L000144](../../scripts/run_answer_quality_benchmark.py#L144) | 144 | `"    loopback = host == \"localhost\""` | — |
| [SRC-4FFD5AFC54-L000145](../../scripts/run_answer_quality_benchmark.py#L145) | 145 | `"    try:"` | — |
| [SRC-4FFD5AFC54-L000146](../../scripts/run_answer_quality_benchmark.py#L146) | 146 | `"        loopback = ipaddress.ip_address(host).is_loopback"` | — |
| [SRC-4FFD5AFC54-L000147](../../scripts/run_answer_quality_benchmark.py#L147) | 147 | `"    except ValueError:"` | — |
| [SRC-4FFD5AFC54-L000148](../../scripts/run_answer_quality_benchmark.py#L148) | 148 | `"        pass"` | — |
| [SRC-4FFD5AFC54-L000149](../../scripts/run_answer_quality_benchmark.py#L149) | 149 | `""` | — |
| [SRC-4FFD5AFC54-L000150](../../scripts/run_answer_quality_benchmark.py#L150) | 150 | `"    if scheme == \"http\" and not loopback:"` | — |
| [SRC-4FFD5AFC54-L000151](../../scripts/run_answer_quality_benchmark.py#L151) | 151 | `"        raise ValueError(\"Plain HTTP is allowed only for localhost or a loopback IP.\")"` | — |
| [SRC-4FFD5AFC54-L000152](../../scripts/run_answer_quality_benchmark.py#L152) | 152 | `""` | — |
| [SRC-4FFD5AFC54-L000153](../../scripts/run_answer_quality_benchmark.py#L153) | 153 | `"    if (scheme == \"https\" and port == 443) or (scheme == \"http\" and port == 80):"` | — |
| [SRC-4FFD5AFC54-L000154](../../scripts/run_answer_quality_benchmark.py#L154) | 154 | `"        port = None"` | — |
| [SRC-4FFD5AFC54-L000155](../../scripts/run_answer_quality_benchmark.py#L155) | 155 | `"    host_for_origin = f\"[{host}]\" if \":\" in host else host"` | — |
| [SRC-4FFD5AFC54-L000156](../../scripts/run_answer_quality_benchmark.py#L156) | 156 | `"    origin = f\"{scheme}://{host_for_origin}\" + (f\":{port}\" if port is not None else \"\")"` | — |
| [SRC-4FFD5AFC54-L000157](../../scripts/run_answer_quality_benchmark.py#L157) | 157 | `""` | — |
| [SRC-4FFD5AFC54-L000158](../../scripts/run_answer_quality_benchmark.py#L158) | 158 | `"    if token_present and not loopback:"` | — |
| [SRC-4FFD5AFC54-L000159](../../scripts/run_answer_quality_benchmark.py#L159) | 159 | `"        allowed = os.getenv(\"OMARAI_BENCHMARK_ALLOWED_ORIGIN\", \"\").strip()"` | — |
| [SRC-4FFD5AFC54-L000160](../../scripts/run_answer_quality_benchmark.py#L160) | 160 | `"        if not allowed:"` | — |
| [SRC-4FFD5AFC54-L000161](../../scripts/run_answer_quality_benchmark.py#L161) | 161 | `"            raise ValueError("` | — |
| [SRC-4FFD5AFC54-L000162](../../scripts/run_answer_quality_benchmark.py#L162) | 162 | `"                \"A bearer token requires OMARAI_BENCHMARK_ALLOWED_ORIGIN to match \""` | — |
| [SRC-4FFD5AFC54-L000163](../../scripts/run_answer_quality_benchmark.py#L163) | 163 | `"                \"the exact HTTPS deployment origin.\""` | — |
| [SRC-4FFD5AFC54-L000164](../../scripts/run_answer_quality_benchmark.py#L164) | 164 | `"            )"` | — |
| [SRC-4FFD5AFC54-L000165](../../scripts/run_answer_quality_benchmark.py#L165) | 165 | `"        allowed_origin = validate_base_url(allowed, token_present=False)"` | — |
| [SRC-4FFD5AFC54-L000166](../../scripts/run_answer_quality_benchmark.py#L166) | 166 | `"        if allowed_origin != origin:"` | — |
| [SRC-4FFD5AFC54-L000167](../../scripts/run_answer_quality_benchmark.py#L167) | 167 | `"            raise ValueError("` | — |
| [SRC-4FFD5AFC54-L000168](../../scripts/run_answer_quality_benchmark.py#L168) | 168 | `"                \"Refusing to send the bearer token: base URL does not match \""` | — |
| [SRC-4FFD5AFC54-L000169](../../scripts/run_answer_quality_benchmark.py#L169) | 169 | `"                \"OMARAI_BENCHMARK_ALLOWED_ORIGIN.\""` | — |
| [SRC-4FFD5AFC54-L000170](../../scripts/run_answer_quality_benchmark.py#L170) | 170 | `"            )"` | — |
| [SRC-4FFD5AFC54-L000171](../../scripts/run_answer_quality_benchmark.py#L171) | 171 | `"    return origin"` | — |
| [SRC-4FFD5AFC54-L000172](../../scripts/run_answer_quality_benchmark.py#L172) | 172 | `""` | — |
| [SRC-4FFD5AFC54-L000173](../../scripts/run_answer_quality_benchmark.py#L173) | 173 | `""` | — |
| [SRC-4FFD5AFC54-L000174](../../scripts/run_answer_quality_benchmark.py#L174) | 174 | `"class _NoRedirectHandler(urllib.request.HTTPRedirectHandler):"` | — |
| [SRC-4FFD5AFC54-L000175](../../scripts/run_answer_quality_benchmark.py#L175) | 175 | `"    \"\"\"Do not follow redirects; the bearer token must never move to another origin.\"\"\""` | — |
| [SRC-4FFD5AFC54-L000176](../../scripts/run_answer_quality_benchmark.py#L176) | 176 | `""` | — |
| [SRC-4FFD5AFC54-L000177](../../scripts/run_answer_quality_benchmark.py#L177) | 177 | `"    def redirect_request(self, req, fp, code, msg, headers, newurl):"` | — |
| [SRC-4FFD5AFC54-L000178](../../scripts/run_answer_quality_benchmark.py#L178) | 178 | `"        return None"` | — |
| [SRC-4FFD5AFC54-L000179](../../scripts/run_answer_quality_benchmark.py#L179) | 179 | `""` | — |
| [SRC-4FFD5AFC54-L000180](../../scripts/run_answer_quality_benchmark.py#L180) | 180 | `""` | — |
| [SRC-4FFD5AFC54-L000181](../../scripts/run_answer_quality_benchmark.py#L181) | 181 | `"_NO_REDIRECT_OPENER = urllib.request.build_opener(_NoRedirectHandler())"` | — |
| [SRC-4FFD5AFC54-L000182](../../scripts/run_answer_quality_benchmark.py#L182) | 182 | `""` | — |
| [SRC-4FFD5AFC54-L000183](../../scripts/run_answer_quality_benchmark.py#L183) | 183 | `"REQUIRED_FIELDS = {"` | — |
| [SRC-4FFD5AFC54-L000184](../../scripts/run_answer_quality_benchmark.py#L184) | 184 | `"    \"case_id\","` | — |
| [SRC-4FFD5AFC54-L000185](../../scripts/run_answer_quality_benchmark.py#L185) | 185 | `"    \"category\","` | — |
| [SRC-4FFD5AFC54-L000186](../../scripts/run_answer_quality_benchmark.py#L186) | 186 | `"    \"language\","` | — |
| [SRC-4FFD5AFC54-L000187](../../scripts/run_answer_quality_benchmark.py#L187) | 187 | `"    \"question\","` | — |
| [SRC-4FFD5AFC54-L000188](../../scripts/run_answer_quality_benchmark.py#L188) | 188 | `"    \"expected_strategy\","` | — |
| [SRC-4FFD5AFC54-L000189](../../scripts/run_answer_quality_benchmark.py#L189) | 189 | `"    \"required_behaviors\","` | — |
| [SRC-4FFD5AFC54-L000190](../../scripts/run_answer_quality_benchmark.py#L190) | 190 | `"    \"forbidden_behaviors\","` | — |
| [SRC-4FFD5AFC54-L000191](../../scripts/run_answer_quality_benchmark.py#L191) | 191 | `"    \"evidence_fixture\","` | — |
| [SRC-4FFD5AFC54-L000192](../../scripts/run_answer_quality_benchmark.py#L192) | 192 | `"    \"failure_conditions\","` | — |
| [SRC-4FFD5AFC54-L000193](../../scripts/run_answer_quality_benchmark.py#L193) | 193 | `"    \"evaluation_mode\","` | — |
| [SRC-4FFD5AFC54-L000194](../../scripts/run_answer_quality_benchmark.py#L194) | 194 | `"}"` | — |
| [SRC-4FFD5AFC54-L000195](../../scripts/run_answer_quality_benchmark.py#L195) | 195 | `"ALLOWED_STRATEGIES = {\"local\", \"model_no_search\", \"web_search\", \"clarify\"}"` | — |
| [SRC-4FFD5AFC54-L000196](../../scripts/run_answer_quality_benchmark.py#L196) | 196 | `"ALLOWED_EVAL_MODES = {\"deterministic_structure\", \"fixture_assisted\", \"human_judgment\"}"` | — |
| [SRC-4FFD5AFC54-L000197](../../scripts/run_answer_quality_benchmark.py#L197) | 197 | `""` | — |
| [SRC-4FFD5AFC54-L000198](../../scripts/run_answer_quality_benchmark.py#L198) | 198 | `""` | — |
| [SRC-4FFD5AFC54-L000199](../../scripts/run_answer_quality_benchmark.py#L199) | 199 | `"def _utc_now() -> str:"` | — |
| [SRC-4FFD5AFC54-L000200](../../scripts/run_answer_quality_benchmark.py#L200) | 200 | `"    return datetime.now(UTC).isoformat(timespec=\"seconds\")"` | — |
| [SRC-4FFD5AFC54-L000201](../../scripts/run_answer_quality_benchmark.py#L201) | 201 | `""` | — |
| [SRC-4FFD5AFC54-L000202](../../scripts/run_answer_quality_benchmark.py#L202) | 202 | `""` | — |
| [SRC-4FFD5AFC54-L000203](../../scripts/run_answer_quality_benchmark.py#L203) | 203 | `"def load_corpus(path: Path) -> dict:"` | — |
| [SRC-4FFD5AFC54-L000204](../../scripts/run_answer_quality_benchmark.py#L204) | 204 | `"    if not path.is_file():"` | — |
| [SRC-4FFD5AFC54-L000205](../../scripts/run_answer_quality_benchmark.py#L205) | 205 | `"        raise FileNotFoundError(f\"Corpus not found: {path}\")"` | — |
| [SRC-4FFD5AFC54-L000206](../../scripts/run_answer_quality_benchmark.py#L206) | 206 | `"    data = json.loads(path.read_text(encoding=\"utf-8\"))"` | — |
| [SRC-4FFD5AFC54-L000207](../../scripts/run_answer_quality_benchmark.py#L207) | 207 | `"    if not isinstance(data, dict) or not isinstance(data.get(\"cases\"), list):"` | — |
| [SRC-4FFD5AFC54-L000208](../../scripts/run_answer_quality_benchmark.py#L208) | 208 | `"        raise TypeError(\"Corpus root must be an object with a cases array\")"` | — |
| [SRC-4FFD5AFC54-L000209](../../scripts/run_answer_quality_benchmark.py#L209) | 209 | `"    if data.get(\"parts\"):"` | — |
| [SRC-4FFD5AFC54-L000210](../../scripts/run_answer_quality_benchmark.py#L210) | 210 | `"        raise ValueError(\"Incomplete shard index is not accepted; use merged cases[] corpus\")"` | — |
| [SRC-4FFD5AFC54-L000211](../../scripts/run_answer_quality_benchmark.py#L211) | 211 | `"    return data"` | — |
| [SRC-4FFD5AFC54-L000212](../../scripts/run_answer_quality_benchmark.py#L212) | 212 | `""` | — |
| [SRC-4FFD5AFC54-L000213](../../scripts/run_answer_quality_benchmark.py#L213) | 213 | `""` | — |
| [SRC-4FFD5AFC54-L000214](../../scripts/run_answer_quality_benchmark.py#L214) | 214 | `"def validate_corpus(data: dict) -> list[str]:"` | — |
| [SRC-4FFD5AFC54-L000215](../../scripts/run_answer_quality_benchmark.py#L215) | 215 | `"    \"\"\"Return a list of human-readable problems (empty => OK).\"\"\""` | — |
| [SRC-4FFD5AFC54-L000216](../../scripts/run_answer_quality_benchmark.py#L216) | 216 | `"    problems: list[str] = []"` | — |
| [SRC-4FFD5AFC54-L000217](../../scripts/run_answer_quality_benchmark.py#L217) | 217 | `"    cases = data.get(\"cases\") or []"` | — |
| [SRC-4FFD5AFC54-L000218](../../scripts/run_answer_quality_benchmark.py#L218) | 218 | `"    if data.get(\"case_count\") != len(cases):"` | — |
| [SRC-4FFD5AFC54-L000219](../../scripts/run_answer_quality_benchmark.py#L219) | 219 | `"        problems.append("` | — |
| [SRC-4FFD5AFC54-L000220](../../scripts/run_answer_quality_benchmark.py#L220) | 220 | `"            f\"case_count metadata {data.get('case_count')!r} != len(cases) {len(cases)}\""` | — |
| [SRC-4FFD5AFC54-L000221](../../scripts/run_answer_quality_benchmark.py#L221) | 221 | `"        )"` | — |
| [SRC-4FFD5AFC54-L000222](../../scripts/run_answer_quality_benchmark.py#L222) | 222 | `"    if len(cases) < 40:"` | — |
| [SRC-4FFD5AFC54-L000223](../../scripts/run_answer_quality_benchmark.py#L223) | 223 | `"        problems.append(f\"expected at least 40 cases, found {len(cases)}\")"` | — |
| [SRC-4FFD5AFC54-L000224](../../scripts/run_answer_quality_benchmark.py#L224) | 224 | `"    ids: list[str] = []"` | — |
| [SRC-4FFD5AFC54-L000225](../../scripts/run_answer_quality_benchmark.py#L225) | 225 | `"    for i, case in enumerate(cases):"` | — |
| [SRC-4FFD5AFC54-L000226](../../scripts/run_answer_quality_benchmark.py#L226) | 226 | `"        if not isinstance(case, dict):"` | — |
| [SRC-4FFD5AFC54-L000227](../../scripts/run_answer_quality_benchmark.py#L227) | 227 | `"            problems.append(f\"cases[{i}] is not an object\")"` | — |
| [SRC-4FFD5AFC54-L000228](../../scripts/run_answer_quality_benchmark.py#L228) | 228 | `"            continue"` | — |
| [SRC-4FFD5AFC54-L000229](../../scripts/run_answer_quality_benchmark.py#L229) | 229 | `"        missing = REQUIRED_FIELDS - set(case)"` | — |
| [SRC-4FFD5AFC54-L000230](../../scripts/run_answer_quality_benchmark.py#L230) | 230 | `"        if missing:"` | — |
| [SRC-4FFD5AFC54-L000231](../../scripts/run_answer_quality_benchmark.py#L231) | 231 | `"            problems.append(f\"{case.get('case_id', i)}: missing {sorted(missing)}\")"` | — |
| [SRC-4FFD5AFC54-L000232](../../scripts/run_answer_quality_benchmark.py#L232) | 232 | `"        cid = case.get(\"case_id\")"` | — |
| [SRC-4FFD5AFC54-L000233](../../scripts/run_answer_quality_benchmark.py#L233) | 233 | `"        if isinstance(cid, str):"` | — |
| [SRC-4FFD5AFC54-L000234](../../scripts/run_answer_quality_benchmark.py#L234) | 234 | `"            ids.append(cid)"` | — |
| [SRC-4FFD5AFC54-L000235](../../scripts/run_answer_quality_benchmark.py#L235) | 235 | `"        if case.get(\"expected_strategy\") not in ALLOWED_STRATEGIES:"` | — |
| [SRC-4FFD5AFC54-L000236](../../scripts/run_answer_quality_benchmark.py#L236) | 236 | `"            problems.append(f\"{cid}: bad strategy {case.get('expected_strategy')!r}\")"` | — |
| [SRC-4FFD5AFC54-L000237](../../scripts/run_answer_quality_benchmark.py#L237) | 237 | `"        if case.get(\"evaluation_mode\") not in ALLOWED_EVAL_MODES:"` | — |
| [SRC-4FFD5AFC54-L000238](../../scripts/run_answer_quality_benchmark.py#L238) | 238 | `"            problems.append(f\"{cid}: bad evaluation_mode {case.get('evaluation_mode')!r}\")"` | — |
| [SRC-4FFD5AFC54-L000239](../../scripts/run_answer_quality_benchmark.py#L239) | 239 | `"        q = case.get(\"question\")"` | — |
| [SRC-4FFD5AFC54-L000240](../../scripts/run_answer_quality_benchmark.py#L240) | 240 | `"        if not isinstance(q, str) or len(q.strip()) < 2:"` | — |
| [SRC-4FFD5AFC54-L000241](../../scripts/run_answer_quality_benchmark.py#L241) | 241 | `"            problems.append(f\"{cid}: empty question\")"` | — |
| [SRC-4FFD5AFC54-L000242](../../scripts/run_answer_quality_benchmark.py#L242) | 242 | `"    if len(ids) != len(set(ids)):"` | — |
| [SRC-4FFD5AFC54-L000243](../../scripts/run_answer_quality_benchmark.py#L243) | 243 | `"        problems.append(\"duplicate case_id values\")"` | — |
| [SRC-4FFD5AFC54-L000244](../../scripts/run_answer_quality_benchmark.py#L244) | 244 | `"    return problems"` | — |
| [SRC-4FFD5AFC54-L000245](../../scripts/run_answer_quality_benchmark.py#L245) | 245 | `""` | — |
| [SRC-4FFD5AFC54-L000246](../../scripts/run_answer_quality_benchmark.py#L246) | 246 | `""` | — |
| [SRC-4FFD5AFC54-L000247](../../scripts/run_answer_quality_benchmark.py#L247) | 247 | `"def redact_secrets(text: str) -> str:"` | — |
| [SRC-4FFD5AFC54-L000248](../../scripts/run_answer_quality_benchmark.py#L248) | 248 | `"    \"\"\"Best-effort redaction of common secret patterns from stored outputs.\"\"\""` | — |
| [SRC-4FFD5AFC54-L000249](../../scripts/run_answer_quality_benchmark.py#L249) | 249 | `"    if not text:"` | — |
| [SRC-4FFD5AFC54-L000250](../../scripts/run_answer_quality_benchmark.py#L250) | 250 | `"        return text"` | — |
| [SRC-4FFD5AFC54-L000251](../../scripts/run_answer_quality_benchmark.py#L251) | 251 | `"    out = text"` | — |
| [SRC-4FFD5AFC54-L000252](../../scripts/run_answer_quality_benchmark.py#L252) | 252 | `"    for key in ("` | — |
| [SRC-4FFD5AFC54-L000253](../../scripts/run_answer_quality_benchmark.py#L253) | 253 | `"        \"OPENROUTER_API_KEY\","` | — |
| [SRC-4FFD5AFC54-L000254](../../scripts/run_answer_quality_benchmark.py#L254) | 254 | `"        \"OMARAI_ACCESS_TOKEN\","` | — |
| [SRC-4FFD5AFC54-L000255](../../scripts/run_answer_quality_benchmark.py#L255) | 255 | `"        \"OMARAI_LLM_API_KEY\","` | — |
| [SRC-4FFD5AFC54-L000256](../../scripts/run_answer_quality_benchmark.py#L256) | 256 | `"        \"Authorization\","` | — |
| [SRC-4FFD5AFC54-L000257](../../scripts/run_answer_quality_benchmark.py#L257) | 257 | `"        \"Bearer \","` | — |
| [SRC-4FFD5AFC54-L000258](../../scripts/run_answer_quality_benchmark.py#L258) | 258 | `"    ):"` | — |
| [SRC-4FFD5AFC54-L000259](../../scripts/run_answer_quality_benchmark.py#L259) | 259 | `"        out = out.replace(key, f\"[REDACTED:{key.strip()}]\")"` | — |
| [SRC-4FFD5AFC54-L000260](../../scripts/run_answer_quality_benchmark.py#L260) | 260 | `"    token = os.getenv(\"OMARAI_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-4FFD5AFC54-L000261](../../scripts/run_answer_quality_benchmark.py#L261) | 261 | `"    if token and token in out:"` | — |
| [SRC-4FFD5AFC54-L000262](../../scripts/run_answer_quality_benchmark.py#L262) | 262 | `"        out = out.replace(token, \"[REDACTED:OMARAI_ACCESS_TOKEN]\")"` | — |
| [SRC-4FFD5AFC54-L000263](../../scripts/run_answer_quality_benchmark.py#L263) | 263 | `"    for env_name in (\"OPENROUTER_API_KEY\", \"OMARAI_LLM_API_KEY\"):"` | — |
| [SRC-4FFD5AFC54-L000264](../../scripts/run_answer_quality_benchmark.py#L264) | 264 | `"        val = os.getenv(env_name, \"\").strip()"` | — |
| [SRC-4FFD5AFC54-L000265](../../scripts/run_answer_quality_benchmark.py#L265) | 265 | `"        if val and val in out:"` | — |
| [SRC-4FFD5AFC54-L000266](../../scripts/run_answer_quality_benchmark.py#L266) | 266 | `"            out = out.replace(val, f\"[REDACTED:{env_name}]\")"` | — |
| [SRC-4FFD5AFC54-L000267](../../scripts/run_answer_quality_benchmark.py#L267) | 267 | `"    return out"` | — |
| [SRC-4FFD5AFC54-L000268](../../scripts/run_answer_quality_benchmark.py#L268) | 268 | `""` | — |
| [SRC-4FFD5AFC54-L000269](../../scripts/run_answer_quality_benchmark.py#L269) | 269 | `""` | — |
| [SRC-4FFD5AFC54-L000270](../../scripts/run_answer_quality_benchmark.py#L270) | 270 | `"def post_agent("` | — |
| [SRC-4FFD5AFC54-L000271](../../scripts/run_answer_quality_benchmark.py#L271) | 271 | `"    base_url: str,"` | — |
| [SRC-4FFD5AFC54-L000272](../../scripts/run_answer_quality_benchmark.py#L272) | 272 | `"    question: str,"` | — |
| [SRC-4FFD5AFC54-L000273](../../scripts/run_answer_quality_benchmark.py#L273) | 273 | `"    timeout: float,"` | — |
| [SRC-4FFD5AFC54-L000274](../../scripts/run_answer_quality_benchmark.py#L274) | 274 | `"    token: str \| None,"` | — |
| [SRC-4FFD5AFC54-L000275](../../scripts/run_answer_quality_benchmark.py#L275) | 275 | `") -> tuple[int, dict \| str]:"` | — |
| [SRC-4FFD5AFC54-L000276](../../scripts/run_answer_quality_benchmark.py#L276) | 276 | `"    origin = validate_base_url(base_url, token_present=bool(token))"` | — |
| [SRC-4FFD5AFC54-L000277](../../scripts/run_answer_quality_benchmark.py#L277) | 277 | `"    url = origin + \"/api/agent\""` | — |
| [SRC-4FFD5AFC54-L000278](../../scripts/run_answer_quality_benchmark.py#L278) | 278 | `"    body = json.dumps({\"question\": question, \"history\": []}, ensure_ascii=False).encode(\"utf-8\")"` | — |
| [SRC-4FFD5AFC54-L000279](../../scripts/run_answer_quality_benchmark.py#L279) | 279 | `"    headers = {\"Content-Type\": \"application/json\", \"Content-Length\": str(len(body))}"` | — |
| [SRC-4FFD5AFC54-L000280](../../scripts/run_answer_quality_benchmark.py#L280) | 280 | `"    if token:"` | — |
| [SRC-4FFD5AFC54-L000281](../../scripts/run_answer_quality_benchmark.py#L281) | 281 | `"        headers[\"Authorization\"] = \"Bearer \" + token"` | — |
| [SRC-4FFD5AFC54-L000282](../../scripts/run_answer_quality_benchmark.py#L282) | 282 | `"    req = urllib.request.Request(url, data=body, headers=headers, method=\"POST\")"` | — |
| [SRC-4FFD5AFC54-L000283](../../scripts/run_answer_quality_benchmark.py#L283) | 283 | `"    try:"` | — |
| [SRC-4FFD5AFC54-L000284](../../scripts/run_answer_quality_benchmark.py#L284) | 284 | `"        with _NO_REDIRECT_OPENER.open(req, timeout=timeout) as resp:"` | — |
| [SRC-4FFD5AFC54-L000285](../../scripts/run_answer_quality_benchmark.py#L285) | 285 | `"            raw_bytes = resp.read(MAX_RESPONSE_BYTES + 1)"` | — |
| [SRC-4FFD5AFC54-L000286](../../scripts/run_answer_quality_benchmark.py#L286) | 286 | `"            if len(raw_bytes) > MAX_RESPONSE_BYTES:"` | — |
| [SRC-4FFD5AFC54-L000287](../../scripts/run_answer_quality_benchmark.py#L287) | 287 | `"                return 0, {\"error\": \"ResponseTooLarge\", \"detail\": \"Response exceeded the 2 MB limit.\"}"` | — |
| [SRC-4FFD5AFC54-L000288](../../scripts/run_answer_quality_benchmark.py#L288) | 288 | `"            raw = raw_bytes.decode(\"utf-8\", errors=\"replace\")"` | — |
| [SRC-4FFD5AFC54-L000289](../../scripts/run_answer_quality_benchmark.py#L289) | 289 | `"            status = getattr(resp, \"status\", 200)"` | — |
| [SRC-4FFD5AFC54-L000290](../../scripts/run_answer_quality_benchmark.py#L290) | 290 | `"            try:"` | — |
| [SRC-4FFD5AFC54-L000291](../../scripts/run_answer_quality_benchmark.py#L291) | 291 | `"                return status, json.loads(raw)"` | — |
| [SRC-4FFD5AFC54-L000292](../../scripts/run_answer_quality_benchmark.py#L292) | 292 | `"            except json.JSONDecodeError:"` | — |
| [SRC-4FFD5AFC54-L000293](../../scripts/run_answer_quality_benchmark.py#L293) | 293 | `"                return status, raw"` | — |
| [SRC-4FFD5AFC54-L000294](../../scripts/run_answer_quality_benchmark.py#L294) | 294 | `"    except urllib.error.HTTPError as exc:"` | — |
| [SRC-4FFD5AFC54-L000295](../../scripts/run_answer_quality_benchmark.py#L295) | 295 | `"        raw_bytes = exc.read(MAX_RESPONSE_BYTES + 1)"` | — |
| [SRC-4FFD5AFC54-L000296](../../scripts/run_answer_quality_benchmark.py#L296) | 296 | `"        if len(raw_bytes) > MAX_RESPONSE_BYTES:"` | — |
| [SRC-4FFD5AFC54-L000297](../../scripts/run_answer_quality_benchmark.py#L297) | 297 | `"            return exc.code, {\"error\": \"ResponseTooLarge\", \"detail\": \"Response exceeded the 2 MB limit.\"}"` | — |
| [SRC-4FFD5AFC54-L000298](../../scripts/run_answer_quality_benchmark.py#L298) | 298 | `"        raw = raw_bytes.decode(\"utf-8\", errors=\"replace\")"` | — |
| [SRC-4FFD5AFC54-L000299](../../scripts/run_answer_quality_benchmark.py#L299) | 299 | `"        try:"` | — |
| [SRC-4FFD5AFC54-L000300](../../scripts/run_answer_quality_benchmark.py#L300) | 300 | `"            return exc.code, json.loads(raw)"` | — |
| [SRC-4FFD5AFC54-L000301](../../scripts/run_answer_quality_benchmark.py#L301) | 301 | `"        except json.JSONDecodeError:"` | — |
| [SRC-4FFD5AFC54-L000302](../../scripts/run_answer_quality_benchmark.py#L302) | 302 | `"            return exc.code, raw"` | — |
| [SRC-4FFD5AFC54-L000303](../../scripts/run_answer_quality_benchmark.py#L303) | 303 | `"    except ValueError as exc:"` | — |
| [SRC-4FFD5AFC54-L000304](../../scripts/run_answer_quality_benchmark.py#L304) | 304 | `"        return 0, {\"error\": \"UnsafeBaseURL\", \"detail\": str(exc)}"` | — |
| [SRC-4FFD5AFC54-L000305](../../scripts/run_answer_quality_benchmark.py#L305) | 305 | `"    except (urllib.error.URLError, TimeoutError, OSError) as exc:"` | — |
| [SRC-4FFD5AFC54-L000306](../../scripts/run_answer_quality_benchmark.py#L306) | 306 | `"        return 0, {\"error\": type(exc).__name__, \"detail\": str(exc)}"` | — |
| [SRC-4FFD5AFC54-L000307](../../scripts/run_answer_quality_benchmark.py#L307) | 307 | `""` | — |
| [SRC-4FFD5AFC54-L000308](../../scripts/run_answer_quality_benchmark.py#L308) | 308 | `""` | — |
| [SRC-4FFD5AFC54-L000309](../../scripts/run_answer_quality_benchmark.py#L309) | 309 | `"def run_validate(corpus_path: Path, summary: bool) -> int:"` | — |
| [SRC-4FFD5AFC54-L000310](../../scripts/run_answer_quality_benchmark.py#L310) | 310 | `"    data = load_corpus(corpus_path)"` | — |
| [SRC-4FFD5AFC54-L000311](../../scripts/run_answer_quality_benchmark.py#L311) | 311 | `"    problems = validate_corpus(data)"` | — |
| [SRC-4FFD5AFC54-L000312](../../scripts/run_answer_quality_benchmark.py#L312) | 312 | `"    if problems:"` | — |
| [SRC-4FFD5AFC54-L000313](../../scripts/run_answer_quality_benchmark.py#L313) | 313 | `"        print(\"VALIDATE FAIL\")"` | — |
| [SRC-4FFD5AFC54-L000314](../../scripts/run_answer_quality_benchmark.py#L314) | 314 | `"        for p in problems:"` | — |
| [SRC-4FFD5AFC54-L000315](../../scripts/run_answer_quality_benchmark.py#L315) | 315 | `"            print(\" -\", p)"` | — |
| [SRC-4FFD5AFC54-L000316](../../scripts/run_answer_quality_benchmark.py#L316) | 316 | `"        return 1"` | — |
| [SRC-4FFD5AFC54-L000317](../../scripts/run_answer_quality_benchmark.py#L317) | 317 | `"    cases = data[\"cases\"]"` | — |
| [SRC-4FFD5AFC54-L000318](../../scripts/run_answer_quality_benchmark.py#L318) | 318 | `"    cats = sorted({c[\"category\"] for c in cases})"` | — |
| [SRC-4FFD5AFC54-L000319](../../scripts/run_answer_quality_benchmark.py#L319) | 319 | `"    langs = sorted({c[\"language\"] for c in cases})"` | — |
| [SRC-4FFD5AFC54-L000320](../../scripts/run_answer_quality_benchmark.py#L320) | 320 | `"    print(\"VALIDATE OK\")"` | — |
| [SRC-4FFD5AFC54-L000321](../../scripts/run_answer_quality_benchmark.py#L321) | 321 | `"    print(f\"benchmark_id={data.get('benchmark_id')} version={data.get('version')}\")"` | — |
| [SRC-4FFD5AFC54-L000322](../../scripts/run_answer_quality_benchmark.py#L322) | 322 | `"    print(f\"cases={len(cases)} categories={len(cats)} languages={langs}\")"` | — |
| [SRC-4FFD5AFC54-L000323](../../scripts/run_answer_quality_benchmark.py#L323) | 323 | `"    if summary:"` | — |
| [SRC-4FFD5AFC54-L000324](../../scripts/run_answer_quality_benchmark.py#L324) | 324 | `"        from collections import Counter"` | — |
| [SRC-4FFD5AFC54-L000325](../../scripts/run_answer_quality_benchmark.py#L325) | 325 | `""` | — |
| [SRC-4FFD5AFC54-L000326](../../scripts/run_answer_quality_benchmark.py#L326) | 326 | `"        print(\"strategies:\", dict(Counter(c[\"expected_strategy\"] for c in cases)))"` | — |
| [SRC-4FFD5AFC54-L000327](../../scripts/run_answer_quality_benchmark.py#L327) | 327 | `"        print(\"eval_modes:\", dict(Counter(c[\"evaluation_mode\"] for c in cases)))"` | — |
| [SRC-4FFD5AFC54-L000328](../../scripts/run_answer_quality_benchmark.py#L328) | 328 | `"        print(\"categories:\", \", \".join(cats))"` | — |
| [SRC-4FFD5AFC54-L000329](../../scripts/run_answer_quality_benchmark.py#L329) | 329 | `"    print("` | — |
| [SRC-4FFD5AFC54-L000330](../../scripts/run_answer_quality_benchmark.py#L330) | 330 | `"        \"NOTE: Structural validation is not answer-quality evaluation. \""` | — |
| [SRC-4FFD5AFC54-L000331](../../scripts/run_answer_quality_benchmark.py#L331) | 331 | `"        \"All reasoning cases remain NOT_TESTED until reviewed.\""` | — |
| [SRC-4FFD5AFC54-L000332](../../scripts/run_answer_quality_benchmark.py#L332) | 332 | `"    )"` | — |
| [SRC-4FFD5AFC54-L000333](../../scripts/run_answer_quality_benchmark.py#L333) | 333 | `"    return 0"` | — |
| [SRC-4FFD5AFC54-L000334](../../scripts/run_answer_quality_benchmark.py#L334) | 334 | `""` | — |
| [SRC-4FFD5AFC54-L000335](../../scripts/run_answer_quality_benchmark.py#L335) | 335 | `""` | — |
| [SRC-4FFD5AFC54-L000336](../../scripts/run_answer_quality_benchmark.py#L336) | 336 | `"def run_live("` | — |
| [SRC-4FFD5AFC54-L000337](../../scripts/run_answer_quality_benchmark.py#L337) | 337 | `"    corpus_path: Path,"` | — |
| [SRC-4FFD5AFC54-L000338](../../scripts/run_answer_quality_benchmark.py#L338) | 338 | `"    base_url: str,"` | — |
| [SRC-4FFD5AFC54-L000339](../../scripts/run_answer_quality_benchmark.py#L339) | 339 | `"    case_id: str \| None,"` | — |
| [SRC-4FFD5AFC54-L000340](../../scripts/run_answer_quality_benchmark.py#L340) | 340 | `"    limit: int,"` | — |
| [SRC-4FFD5AFC54-L000341](../../scripts/run_answer_quality_benchmark.py#L341) | 341 | `"    timeout: float,"` | — |
| [SRC-4FFD5AFC54-L000342](../../scripts/run_answer_quality_benchmark.py#L342) | 342 | `"    delay: float,"` | — |
| [SRC-4FFD5AFC54-L000343](../../scripts/run_answer_quality_benchmark.py#L343) | 343 | `"    out_path: Path \| None,"` | — |
| [SRC-4FFD5AFC54-L000344](../../scripts/run_answer_quality_benchmark.py#L344) | 344 | `"    build_sha: str \| None = None,"` | — |
| [SRC-4FFD5AFC54-L000345](../../scripts/run_answer_quality_benchmark.py#L345) | 345 | `") -> int:"` | — |
| [SRC-4FFD5AFC54-L000346](../../scripts/run_answer_quality_benchmark.py#L346) | 346 | `"    data = load_corpus(corpus_path)"` | — |
| [SRC-4FFD5AFC54-L000347](../../scripts/run_answer_quality_benchmark.py#L347) | 347 | `"    problems = validate_corpus(data)"` | — |
| [SRC-4FFD5AFC54-L000348](../../scripts/run_answer_quality_benchmark.py#L348) | 348 | `"    if problems:"` | — |
| [SRC-4FFD5AFC54-L000349](../../scripts/run_answer_quality_benchmark.py#L349) | 349 | `"        print(\"Corpus invalid; refusing live run:\")"` | — |
| [SRC-4FFD5AFC54-L000350](../../scripts/run_answer_quality_benchmark.py#L350) | 350 | `"        for p in problems:"` | — |
| [SRC-4FFD5AFC54-L000351](../../scripts/run_answer_quality_benchmark.py#L351) | 351 | `"            print(\" -\", p)"` | — |
| [SRC-4FFD5AFC54-L000352](../../scripts/run_answer_quality_benchmark.py#L352) | 352 | `"        return 2"` | — |
| [SRC-4FFD5AFC54-L000353](../../scripts/run_answer_quality_benchmark.py#L353) | 353 | `""` | — |
| [SRC-4FFD5AFC54-L000354](../../scripts/run_answer_quality_benchmark.py#L354) | 354 | `"    token = os.getenv(\"OMARAI_ACCESS_TOKEN\", \"\").strip() or None"` | — |
| [SRC-4FFD5AFC54-L000355](../../scripts/run_answer_quality_benchmark.py#L355) | 355 | `"    try:"` | — |
| [SRC-4FFD5AFC54-L000356](../../scripts/run_answer_quality_benchmark.py#L356) | 356 | `"        safe_base_url = validate_base_url(base_url, token_present=bool(token))"` | — |
| [SRC-4FFD5AFC54-L000357](../../scripts/run_answer_quality_benchmark.py#L357) | 357 | `"    except ValueError as exc:"` | — |
| [SRC-4FFD5AFC54-L000358](../../scripts/run_answer_quality_benchmark.py#L358) | 358 | `"        print(f\"Unsafe base URL; refusing live run: {exc}\", file=sys.stderr)"` | — |
| [SRC-4FFD5AFC54-L000359](../../scripts/run_answer_quality_benchmark.py#L359) | 359 | `"        return 2"` | — |
| [SRC-4FFD5AFC54-L000360](../../scripts/run_answer_quality_benchmark.py#L360) | 360 | `"    cases = data[\"cases\"]"` | — |
| [SRC-4FFD5AFC54-L000361](../../scripts/run_answer_quality_benchmark.py#L361) | 361 | `"    if case_id:"` | — |
| [SRC-4FFD5AFC54-L000362](../../scripts/run_answer_quality_benchmark.py#L362) | 362 | `"        cases = [c for c in cases if c[\"case_id\"] == case_id]"` | — |
| [SRC-4FFD5AFC54-L000363](../../scripts/run_answer_quality_benchmark.py#L363) | 363 | `"        if not cases:"` | — |
| [SRC-4FFD5AFC54-L000364](../../scripts/run_answer_quality_benchmark.py#L364) | 364 | `"            print(f\"Unknown case_id: {case_id}\", file=sys.stderr)"` | — |
| [SRC-4FFD5AFC54-L000365](../../scripts/run_answer_quality_benchmark.py#L365) | 365 | `"            return 2"` | — |
| [SRC-4FFD5AFC54-L000366](../../scripts/run_answer_quality_benchmark.py#L366) | 366 | `"    if limit > 0:"` | — |
| [SRC-4FFD5AFC54-L000367](../../scripts/run_answer_quality_benchmark.py#L367) | 367 | `"        cases = cases[:limit]"` | — |
| [SRC-4FFD5AFC54-L000368](../../scripts/run_answer_quality_benchmark.py#L368) | 368 | `""` | — |
| [SRC-4FFD5AFC54-L000369](../../scripts/run_answer_quality_benchmark.py#L369) | 369 | `"    results = []"` | — |
| [SRC-4FFD5AFC54-L000370](../../scripts/run_answer_quality_benchmark.py#L370) | 370 | `"    print("` | — |
| [SRC-4FFD5AFC54-L000371](../../scripts/run_answer_quality_benchmark.py#L371) | 371 | `"        \"LIVE mode: fixtures are NOT injected into the server. \""` | — |
| [SRC-4FFD5AFC54-L000372](../../scripts/run_answer_quality_benchmark.py#L372) | 372 | `"        \"Answers are recorded as NOT_TESTED (quality) unless transport fails.\""` | — |
| [SRC-4FFD5AFC54-L000373](../../scripts/run_answer_quality_benchmark.py#L373) | 373 | `"    )"` | — |
| [SRC-4FFD5AFC54-L000374](../../scripts/run_answer_quality_benchmark.py#L374) | 374 | `"    for case in cases:"` | — |
| [SRC-4FFD5AFC54-L000375](../../scripts/run_answer_quality_benchmark.py#L375) | 375 | `"        cid = case[\"case_id\"]"` | — |
| [SRC-4FFD5AFC54-L000376](../../scripts/run_answer_quality_benchmark.py#L376) | 376 | `"        prompt = case[\"question\"]"` | — |
| [SRC-4FFD5AFC54-L000377](../../scripts/run_answer_quality_benchmark.py#L377) | 377 | `"        request_started = time.perf_counter()"` | — |
| [SRC-4FFD5AFC54-L000378](../../scripts/run_answer_quality_benchmark.py#L378) | 378 | `"        status_code, payload = post_agent(safe_base_url, prompt, timeout, token)"` | — |
| [SRC-4FFD5AFC54-L000379](../../scripts/run_answer_quality_benchmark.py#L379) | 379 | `"        elapsed_ms = round((time.perf_counter() - request_started) * 1000, 2)"` | — |
| [SRC-4FFD5AFC54-L000380](../../scripts/run_answer_quality_benchmark.py#L380) | 380 | `"        if isinstance(payload, dict):"` | — |
| [SRC-4FFD5AFC54-L000381](../../scripts/run_answer_quality_benchmark.py#L381) | 381 | `"            safe_payload = json.loads(redact_secrets(json.dumps(payload, ensure_ascii=False)))"` | — |
| [SRC-4FFD5AFC54-L000382](../../scripts/run_answer_quality_benchmark.py#L382) | 382 | `"        else:"` | — |
| [SRC-4FFD5AFC54-L000383](../../scripts/run_answer_quality_benchmark.py#L383) | 383 | `"            safe_payload = redact_secrets(str(payload))"` | — |
| [SRC-4FFD5AFC54-L000384](../../scripts/run_answer_quality_benchmark.py#L384) | 384 | `""` | — |
| [SRC-4FFD5AFC54-L000385](../../scripts/run_answer_quality_benchmark.py#L385) | 385 | `"        transport_ok = 200 <= status_code < 300"` | — |
| [SRC-4FFD5AFC54-L000386](../../scripts/run_answer_quality_benchmark.py#L386) | 386 | `"        response_metrics = _response_metrics(safe_payload, case[\"expected_strategy\"], transport_ok)"` | — |
| [SRC-4FFD5AFC54-L000387](../../scripts/run_answer_quality_benchmark.py#L387) | 387 | `"        record = {"` | — |
| [SRC-4FFD5AFC54-L000388](../../scripts/run_answer_quality_benchmark.py#L388) | 388 | `"            \"case_id\": cid,"` | — |
| [SRC-4FFD5AFC54-L000389](../../scripts/run_answer_quality_benchmark.py#L389) | 389 | `"            \"benchmark_version\": data.get(\"version\"),"` | — |
| [SRC-4FFD5AFC54-L000390](../../scripts/run_answer_quality_benchmark.py#L390) | 390 | `"            \"benchmark_id\": data.get(\"benchmark_id\"),"` | — |
| [SRC-4FFD5AFC54-L000391](../../scripts/run_answer_quality_benchmark.py#L391) | 391 | `"            \"executed_at_utc\": _utc_now(),"` | — |
| [SRC-4FFD5AFC54-L000392](../../scripts/run_answer_quality_benchmark.py#L392) | 392 | `"            \"mode\": \"live_api\","` | — |
| [SRC-4FFD5AFC54-L000393](../../scripts/run_answer_quality_benchmark.py#L393) | 393 | `"            \"base_url\": safe_base_url,"` | — |
| [SRC-4FFD5AFC54-L000394](../../scripts/run_answer_quality_benchmark.py#L394) | 394 | `"            \"http_status\": status_code,"` | — |
| [SRC-4FFD5AFC54-L000395](../../scripts/run_answer_quality_benchmark.py#L395) | 395 | `"            \"elapsed_ms\": elapsed_ms,"` | — |
| [SRC-4FFD5AFC54-L000396](../../scripts/run_answer_quality_benchmark.py#L396) | 396 | `"            \"build_sha\": build_sha or \"unknown\","` | — |
| [SRC-4FFD5AFC54-L000397](../../scripts/run_answer_quality_benchmark.py#L397) | 397 | `"            **response_metrics,"` | — |
| [SRC-4FFD5AFC54-L000398](../../scripts/run_answer_quality_benchmark.py#L398) | 398 | `"            \"prompt\": prompt,"` | — |
| [SRC-4FFD5AFC54-L000399](../../scripts/run_answer_quality_benchmark.py#L399) | 399 | `"            \"expected_strategy\": case[\"expected_strategy\"],"` | — |
| [SRC-4FFD5AFC54-L000400](../../scripts/run_answer_quality_benchmark.py#L400) | 400 | `"            \"category\": case[\"category\"],"` | — |
| [SRC-4FFD5AFC54-L000401](../../scripts/run_answer_quality_benchmark.py#L401) | 401 | `"            \"response\": safe_payload,"` | — |
| [SRC-4FFD5AFC54-L000402](../../scripts/run_answer_quality_benchmark.py#L402) | 402 | `"            \"used_web_search\": ("` | — |
| [SRC-4FFD5AFC54-L000403](../../scripts/run_answer_quality_benchmark.py#L403) | 403 | `"                safe_payload.get(\"used_web_search\") if isinstance(safe_payload, dict) else None"` | — |
| [SRC-4FFD5AFC54-L000404](../../scripts/run_answer_quality_benchmark.py#L404) | 404 | `"            ),"` | — |
| [SRC-4FFD5AFC54-L000405](../../scripts/run_answer_quality_benchmark.py#L405) | 405 | `"            \"used_language_model\": ("` | — |
| [SRC-4FFD5AFC54-L000406](../../scripts/run_answer_quality_benchmark.py#L406) | 406 | `"                safe_payload.get(\"used_language_model\")"` | — |
| [SRC-4FFD5AFC54-L000407](../../scripts/run_answer_quality_benchmark.py#L407) | 407 | `"                if isinstance(safe_payload, dict)"` | — |
| [SRC-4FFD5AFC54-L000408](../../scripts/run_answer_quality_benchmark.py#L408) | 408 | `"                else None"` | — |
| [SRC-4FFD5AFC54-L000409](../../scripts/run_answer_quality_benchmark.py#L409) | 409 | `"            ),"` | — |
| [SRC-4FFD5AFC54-L000410](../../scripts/run_answer_quality_benchmark.py#L410) | 410 | `"            \"sources\": ("` | — |
| [SRC-4FFD5AFC54-L000411](../../scripts/run_answer_quality_benchmark.py#L411) | 411 | `"                safe_payload.get(\"sources\") if isinstance(safe_payload, dict) else None"` | — |
| [SRC-4FFD5AFC54-L000412](../../scripts/run_answer_quality_benchmark.py#L412) | 412 | `"            ),"` | — |
| [SRC-4FFD5AFC54-L000413](../../scripts/run_answer_quality_benchmark.py#L413) | 413 | `"            \"status\": \"NOT_TESTED\","` | — |
| [SRC-4FFD5AFC54-L000414](../../scripts/run_answer_quality_benchmark.py#L414) | 414 | `"            \"transport_ok\": transport_ok,"` | — |
| [SRC-4FFD5AFC54-L000415](../../scripts/run_answer_quality_benchmark.py#L415) | 415 | `"            \"reviewer_notes\": ("` | — |
| [SRC-4FFD5AFC54-L000416](../../scripts/run_answer_quality_benchmark.py#L416) | 416 | `"                \"Response collected; human/fixture review required for PASS/FAIL.\""` | — |
| [SRC-4FFD5AFC54-L000417](../../scripts/run_answer_quality_benchmark.py#L417) | 417 | `"                if transport_ok"` | — |
| [SRC-4FFD5AFC54-L000418](../../scripts/run_answer_quality_benchmark.py#L418) | 418 | `"                else \"Transport or HTTP error; quality not graded.\""` | — |
| [SRC-4FFD5AFC54-L000419](../../scripts/run_answer_quality_benchmark.py#L419) | 419 | `"            ),"` | — |
| [SRC-4FFD5AFC54-L000420](../../scripts/run_answer_quality_benchmark.py#L420) | 420 | `"            \"evidence_fixture_injected\": False,"` | — |
| [SRC-4FFD5AFC54-L000421](../../scripts/run_answer_quality_benchmark.py#L421) | 421 | `"        }"` | — |
| [SRC-4FFD5AFC54-L000422](../../scripts/run_answer_quality_benchmark.py#L422) | 422 | `"        results.append(record)"` | — |
| [SRC-4FFD5AFC54-L000423](../../scripts/run_answer_quality_benchmark.py#L423) | 423 | `"        flag = \"OK\" if transport_ok else \"ERR\""` | — |
| [SRC-4FFD5AFC54-L000424](../../scripts/run_answer_quality_benchmark.py#L424) | 424 | `"        print(f\"[{flag}] {cid} http={status_code}\")"` | — |
| [SRC-4FFD5AFC54-L000425](../../scripts/run_answer_quality_benchmark.py#L425) | 425 | `"        if delay > 0:"` | — |
| [SRC-4FFD5AFC54-L000426](../../scripts/run_answer_quality_benchmark.py#L426) | 426 | `"            time.sleep(delay)"` | — |
| [SRC-4FFD5AFC54-L000427](../../scripts/run_answer_quality_benchmark.py#L427) | 427 | `""` | — |
| [SRC-4FFD5AFC54-L000428](../../scripts/run_answer_quality_benchmark.py#L428) | 428 | `"    envelope = {"` | — |
| [SRC-4FFD5AFC54-L000429](../../scripts/run_answer_quality_benchmark.py#L429) | 429 | `"        \"benchmark_id\": data.get(\"benchmark_id\"),"` | — |
| [SRC-4FFD5AFC54-L000430](../../scripts/run_answer_quality_benchmark.py#L430) | 430 | `"        \"benchmark_version\": data.get(\"version\"),"` | — |
| [SRC-4FFD5AFC54-L000431](../../scripts/run_answer_quality_benchmark.py#L431) | 431 | `"        \"mode\": \"live_api\","` | — |
| [SRC-4FFD5AFC54-L000432](../../scripts/run_answer_quality_benchmark.py#L432) | 432 | `"        \"build_sha\": build_sha or \"unknown\","` | — |
| [SRC-4FFD5AFC54-L000433](../../scripts/run_answer_quality_benchmark.py#L433) | 433 | `"        \"executed_at_utc\": _utc_now(),"` | — |
| [SRC-4FFD5AFC54-L000434](../../scripts/run_answer_quality_benchmark.py#L434) | 434 | `"        \"case_count\": len(results),"` | — |
| [SRC-4FFD5AFC54-L000435](../../scripts/run_answer_quality_benchmark.py#L435) | 435 | `"        \"results\": results,"` | — |
| [SRC-4FFD5AFC54-L000436](../../scripts/run_answer_quality_benchmark.py#L436) | 436 | `"        \"disclaimer\": ("` | — |
| [SRC-4FFD5AFC54-L000437](../../scripts/run_answer_quality_benchmark.py#L437) | 437 | `"            \"status=NOT_TESTED means answer quality was not auto-graded. \""` | — |
| [SRC-4FFD5AFC54-L000438](../../scripts/run_answer_quality_benchmark.py#L438) | 438 | `"            \"Fixtures in JSON were not applied to the live server.\""` | — |
| [SRC-4FFD5AFC54-L000439](../../scripts/run_answer_quality_benchmark.py#L439) | 439 | `"        ),"` | — |
| [SRC-4FFD5AFC54-L000440](../../scripts/run_answer_quality_benchmark.py#L440) | 440 | `"    }"` | — |
| [SRC-4FFD5AFC54-L000441](../../scripts/run_answer_quality_benchmark.py#L441) | 441 | `"    text = json.dumps(envelope, ensure_ascii=False, indent=2)"` | — |
| [SRC-4FFD5AFC54-L000442](../../scripts/run_answer_quality_benchmark.py#L442) | 442 | `"    if out_path:"` | — |
| [SRC-4FFD5AFC54-L000443](../../scripts/run_answer_quality_benchmark.py#L443) | 443 | `"        out_path.write_text(text + \"\\n\", encoding=\"utf-8\")"` | — |
| [SRC-4FFD5AFC54-L000444](../../scripts/run_answer_quality_benchmark.py#L444) | 444 | `"        print(f\"Wrote {out_path}\")"` | — |
| [SRC-4FFD5AFC54-L000445](../../scripts/run_answer_quality_benchmark.py#L445) | 445 | `"    else:"` | — |
| [SRC-4FFD5AFC54-L000446](../../scripts/run_answer_quality_benchmark.py#L446) | 446 | `"        print(text)"` | — |
| [SRC-4FFD5AFC54-L000447](../../scripts/run_answer_quality_benchmark.py#L447) | 447 | `"    return 0"` | — |
| [SRC-4FFD5AFC54-L000448](../../scripts/run_answer_quality_benchmark.py#L448) | 448 | `""` | — |
| [SRC-4FFD5AFC54-L000449](../../scripts/run_answer_quality_benchmark.py#L449) | 449 | `""` | — |
| [SRC-4FFD5AFC54-L000450](../../scripts/run_answer_quality_benchmark.py#L450) | 450 | `"def main(argv: list[str] \| None = None) -> int:"` | — |
| [SRC-4FFD5AFC54-L000451](../../scripts/run_answer_quality_benchmark.py#L451) | 451 | `"    parser = argparse.ArgumentParser(description=\"Omarai answer-quality benchmark runner\")"` | — |
| [SRC-4FFD5AFC54-L000452](../../scripts/run_answer_quality_benchmark.py#L452) | 452 | `"    parser.add_argument("` | — |
| [SRC-4FFD5AFC54-L000453](../../scripts/run_answer_quality_benchmark.py#L453) | 453 | `"        \"--mode\","` | — |
| [SRC-4FFD5AFC54-L000454](../../scripts/run_answer_quality_benchmark.py#L454) | 454 | `"        choices=(\"validate\", \"live\"),"` | — |
| [SRC-4FFD5AFC54-L000455](../../scripts/run_answer_quality_benchmark.py#L455) | 455 | `"        default=\"validate\","` | — |
| [SRC-4FFD5AFC54-L000456](../../scripts/run_answer_quality_benchmark.py#L456) | 456 | `"        help=\"validate=offline corpus check (default); live=opt-in API calls\","` | — |
| [SRC-4FFD5AFC54-L000457](../../scripts/run_answer_quality_benchmark.py#L457) | 457 | `"    )"` | — |
| [SRC-4FFD5AFC54-L000458](../../scripts/run_answer_quality_benchmark.py#L458) | 458 | `"    parser.add_argument("` | — |
| [SRC-4FFD5AFC54-L000459](../../scripts/run_answer_quality_benchmark.py#L459) | 459 | `"        \"--corpus\","` | — |
| [SRC-4FFD5AFC54-L000460](../../scripts/run_answer_quality_benchmark.py#L460) | 460 | `"        type=Path,"` | — |
| [SRC-4FFD5AFC54-L000461](../../scripts/run_answer_quality_benchmark.py#L461) | 461 | `"        default=DEFAULT_CORPUS,"` | — |
| [SRC-4FFD5AFC54-L000462](../../scripts/run_answer_quality_benchmark.py#L462) | 462 | `"        help=\"Path to answer_quality_cases.json\","` | — |
| [SRC-4FFD5AFC54-L000463](../../scripts/run_answer_quality_benchmark.py#L463) | 463 | `"    )"` | — |
| [SRC-4FFD5AFC54-L000464](../../scripts/run_answer_quality_benchmark.py#L464) | 464 | `"    parser.add_argument(\"--summary\", action=\"store_true\", help=\"Extra validate summary\")"` | — |
| [SRC-4FFD5AFC54-L000465](../../scripts/run_answer_quality_benchmark.py#L465) | 465 | `"    parser.add_argument(\"--base-url\", default=\"http://127.0.0.1:8765\")"` | — |
| [SRC-4FFD5AFC54-L000466](../../scripts/run_answer_quality_benchmark.py#L466) | 466 | `"    parser.add_argument(\"--case-id\", default=None, help=\"Run a single case (live)\")"` | — |
| [SRC-4FFD5AFC54-L000467](../../scripts/run_answer_quality_benchmark.py#L467) | 467 | `"    parser.add_argument(\"--limit\", type=int, default=0, help=\"Max cases in live mode (0=all selected)\")"` | — |
| [SRC-4FFD5AFC54-L000468](../../scripts/run_answer_quality_benchmark.py#L468) | 468 | `"    parser.add_argument(\"--timeout\", type=float, default=60.0)"` | — |
| [SRC-4FFD5AFC54-L000469](../../scripts/run_answer_quality_benchmark.py#L469) | 469 | `"    parser.add_argument(\"--build-sha\", default=None, help=\"Exact deployed source SHA (required for a defensible baseline comparison)\")"` | — |
| [SRC-4FFD5AFC54-L000470](../../scripts/run_answer_quality_benchmark.py#L470) | 470 | `"    parser.add_argument(\"--delay\", type=float, default=0.0, help=\"Seconds between live requests\")"` | — |
| [SRC-4FFD5AFC54-L000471](../../scripts/run_answer_quality_benchmark.py#L471) | 471 | `"    parser.add_argument(\"--out\", type=Path, default=None, help=\"Write live results JSON\")"` | — |
| [SRC-4FFD5AFC54-L000472](../../scripts/run_answer_quality_benchmark.py#L472) | 472 | `"    args = parser.parse_args(argv)"` | — |
| [SRC-4FFD5AFC54-L000473](../../scripts/run_answer_quality_benchmark.py#L473) | 473 | `""` | — |
| [SRC-4FFD5AFC54-L000474](../../scripts/run_answer_quality_benchmark.py#L474) | 474 | `"    if args.mode == \"validate\":"` | — |
| [SRC-4FFD5AFC54-L000475](../../scripts/run_answer_quality_benchmark.py#L475) | 475 | `"        return run_validate(args.corpus, args.summary)"` | — |
| [SRC-4FFD5AFC54-L000476](../../scripts/run_answer_quality_benchmark.py#L476) | 476 | `"    if args.mode == \"live\":"` | — |
| [SRC-4FFD5AFC54-L000477](../../scripts/run_answer_quality_benchmark.py#L477) | 477 | `"        if not args.case_id and args.limit <= 0:"` | — |
| [SRC-4FFD5AFC54-L000478](../../scripts/run_answer_quality_benchmark.py#L478) | 478 | `"            print("` | — |
| [SRC-4FFD5AFC54-L000479](../../scripts/run_answer_quality_benchmark.py#L479) | 479 | `"                \"Refusing unbounded live run. Pass --case-id and/or --limit > 0.\","` | — |
| [SRC-4FFD5AFC54-L000480](../../scripts/run_answer_quality_benchmark.py#L480) | 480 | `"                file=sys.stderr,"` | — |
| [SRC-4FFD5AFC54-L000481](../../scripts/run_answer_quality_benchmark.py#L481) | 481 | `"            )"` | — |
| [SRC-4FFD5AFC54-L000482](../../scripts/run_answer_quality_benchmark.py#L482) | 482 | `"            return 2"` | — |
| [SRC-4FFD5AFC54-L000483](../../scripts/run_answer_quality_benchmark.py#L483) | 483 | `"        return run_live("` | — |
| [SRC-4FFD5AFC54-L000484](../../scripts/run_answer_quality_benchmark.py#L484) | 484 | `"            args.corpus,"` | — |
| [SRC-4FFD5AFC54-L000485](../../scripts/run_answer_quality_benchmark.py#L485) | 485 | `"            args.base_url,"` | — |
| [SRC-4FFD5AFC54-L000486](../../scripts/run_answer_quality_benchmark.py#L486) | 486 | `"            args.case_id,"` | — |
| [SRC-4FFD5AFC54-L000487](../../scripts/run_answer_quality_benchmark.py#L487) | 487 | `"            args.limit,"` | — |
| [SRC-4FFD5AFC54-L000488](../../scripts/run_answer_quality_benchmark.py#L488) | 488 | `"            args.timeout,"` | — |
| [SRC-4FFD5AFC54-L000489](../../scripts/run_answer_quality_benchmark.py#L489) | 489 | `"            args.delay,"` | — |
| [SRC-4FFD5AFC54-L000490](../../scripts/run_answer_quality_benchmark.py#L490) | 490 | `"            args.out,"` | — |
| [SRC-4FFD5AFC54-L000491](../../scripts/run_answer_quality_benchmark.py#L491) | 491 | `"            args.build_sha,"` | — |
| [SRC-4FFD5AFC54-L000492](../../scripts/run_answer_quality_benchmark.py#L492) | 492 | `"        )"` | — |
| [SRC-4FFD5AFC54-L000493](../../scripts/run_answer_quality_benchmark.py#L493) | 493 | `"    return 2"` | — |
| [SRC-4FFD5AFC54-L000494](../../scripts/run_answer_quality_benchmark.py#L494) | 494 | `""` | — |
| [SRC-4FFD5AFC54-L000495](../../scripts/run_answer_quality_benchmark.py#L495) | 495 | `""` | — |
| [SRC-4FFD5AFC54-L000496](../../scripts/run_answer_quality_benchmark.py#L496) | 496 | `"if __name__ == \"__main__\":"` | — |
| [SRC-4FFD5AFC54-L000497](../../scripts/run_answer_quality_benchmark.py#L497) | 497 | `"    raise SystemExit(main())"` | — |
## ملفات أخرى

### FILE-03FF422A16 — [scripts/score_answer_quality_reviews.py](../../scripts/score_answer_quality_reviews.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-03FF422A16-L000001](../../scripts/score_answer_quality_reviews.py#L1) | 1 | `"\"\"\"Score manually reviewed Omarai answer-quality cases without auto-grading."` | — |
| [SRC-03FF422A16-L000002](../../scripts/score_answer_quality_reviews.py#L2) | 2 | `""` | — |
| [SRC-03FF422A16-L000003](../../scripts/score_answer_quality_reviews.py#L3) | 3 | `"This offline tool calculates aggregate retrieval, faithfulness, correctness, citation,"` | — |
| [SRC-03FF422A16-L000004](../../scripts/score_answer_quality_reviews.py#L4) | 4 | `"and writing-quality metrics only from explicit review annotations. Missing judgments"` | — |
| [SRC-03FF422A16-L000005](../../scripts/score_answer_quality_reviews.py#L5) | 5 | `"remain NOT_TESTED; this script never calls an LLM or treats transport success as PASS."` | — |
| [SRC-03FF422A16-L000006](../../scripts/score_answer_quality_reviews.py#L6) | 6 | `"\"\"\""` | — |
| [SRC-03FF422A16-L000007](../../scripts/score_answer_quality_reviews.py#L7) | 7 | `"from __future__ import annotations"` | — |
| [SRC-03FF422A16-L000008](../../scripts/score_answer_quality_reviews.py#L8) | 8 | `""` | — |
| [SRC-03FF422A16-L000009](../../scripts/score_answer_quality_reviews.py#L9) | 9 | `"import argparse"` | — |
| [SRC-03FF422A16-L000010](../../scripts/score_answer_quality_reviews.py#L10) | 10 | `"import json"` | — |
| [SRC-03FF422A16-L000011](../../scripts/score_answer_quality_reviews.py#L11) | 11 | `"import math"` | — |
| [SRC-03FF422A16-L000012](../../scripts/score_answer_quality_reviews.py#L12) | 12 | `"import sys"` | — |
| [SRC-03FF422A16-L000013](../../scripts/score_answer_quality_reviews.py#L13) | 13 | `"from collections import Counter"` | — |
| [SRC-03FF422A16-L000014](../../scripts/score_answer_quality_reviews.py#L14) | 14 | `"from pathlib import Path"` | — |
| [SRC-03FF422A16-L000015](../../scripts/score_answer_quality_reviews.py#L15) | 15 | `"from typing import Any"` | — |
| [SRC-03FF422A16-L000016](../../scripts/score_answer_quality_reviews.py#L16) | 16 | `""` | — |
| [SRC-03FF422A16-L000017](../../scripts/score_answer_quality_reviews.py#L17) | 17 | `"ROOT = Path(__file__).resolve().parents[1]"` | — |
| [SRC-03FF422A16-L000018](../../scripts/score_answer_quality_reviews.py#L18) | 18 | `"DEFAULT_CORPUS = ROOT / \"tests\" / \"fixtures\" / \"answer_quality_cases.json\""` | — |
| [SRC-03FF422A16-L000019](../../scripts/score_answer_quality_reviews.py#L19) | 19 | `"ALLOWED_STATUSES = {\"REVIEWED\", \"NOT_TESTED\", \"BLOCKED\"}"` | — |
| [SRC-03FF422A16-L000020](../../scripts/score_answer_quality_reviews.py#L20) | 20 | `"COUNT_GROUPS = {"` | — |
| [SRC-03FF422A16-L000021](../../scripts/score_answer_quality_reviews.py#L21) | 21 | `"    \"retrieval\": (\"relevant_retrieved\", \"retrieved_count\", \"relevant_available\"),"` | — |
| [SRC-03FF422A16-L000022](../../scripts/score_answer_quality_reviews.py#L22) | 22 | `"    \"faithfulness\": (\"supported_claims\", \"reviewed_claims\"),"` | — |
| [SRC-03FF422A16-L000023](../../scripts/score_answer_quality_reviews.py#L23) | 23 | `"    \"correctness\": (\"correct_facts\", \"reviewed_facts\"),"` | — |
| [SRC-03FF422A16-L000024](../../scripts/score_answer_quality_reviews.py#L24) | 24 | `"    \"citations\": (\"supported_citations\", \"reviewed_citations\"),"` | — |
| [SRC-03FF422A16-L000025](../../scripts/score_answer_quality_reviews.py#L25) | 25 | `"}"` | — |
| [SRC-03FF422A16-L000026](../../scripts/score_answer_quality_reviews.py#L26) | 26 | `""` | — |
| [SRC-03FF422A16-L000027](../../scripts/score_answer_quality_reviews.py#L27) | 27 | `""` | — |
| [SRC-03FF422A16-L000028](../../scripts/score_answer_quality_reviews.py#L28) | 28 | `"def load_json_object(path: Path) -> dict[str, Any]:"` | — |
| [SRC-03FF422A16-L000029](../../scripts/score_answer_quality_reviews.py#L29) | 29 | `"    if not path.is_file():"` | — |
| [SRC-03FF422A16-L000030](../../scripts/score_answer_quality_reviews.py#L30) | 30 | `"        raise FileNotFoundError(\"Input file not found: \" + str(path))"` | — |
| [SRC-03FF422A16-L000031](../../scripts/score_answer_quality_reviews.py#L31) | 31 | `"    data = json.loads(path.read_text(encoding=\"utf-8\"))"` | — |
| [SRC-03FF422A16-L000032](../../scripts/score_answer_quality_reviews.py#L32) | 32 | `"    if not isinstance(data, dict):"` | — |
| [SRC-03FF422A16-L000033](../../scripts/score_answer_quality_reviews.py#L33) | 33 | `"        raise TypeError(\"JSON root must be an object\")"` | — |
| [SRC-03FF422A16-L000034](../../scripts/score_answer_quality_reviews.py#L34) | 34 | `"    return data"` | — |
| [SRC-03FF422A16-L000035](../../scripts/score_answer_quality_reviews.py#L35) | 35 | `""` | — |
| [SRC-03FF422A16-L000036](../../scripts/score_answer_quality_reviews.py#L36) | 36 | `""` | — |
| [SRC-03FF422A16-L000037](../../scripts/score_answer_quality_reviews.py#L37) | 37 | `"def _is_nonnegative_int(value: Any) -> bool:"` | — |
| [SRC-03FF422A16-L000038](../../scripts/score_answer_quality_reviews.py#L38) | 38 | `"    return isinstance(value, int) and not isinstance(value, bool) and value >= 0"` | — |
| [SRC-03FF422A16-L000039](../../scripts/score_answer_quality_reviews.py#L39) | 39 | `""` | — |
| [SRC-03FF422A16-L000040](../../scripts/score_answer_quality_reviews.py#L40) | 40 | `""` | — |
| [SRC-03FF422A16-L000041](../../scripts/score_answer_quality_reviews.py#L41) | 41 | `"def validate_reviews("` | — |
| [SRC-03FF422A16-L000042](../../scripts/score_answer_quality_reviews.py#L42) | 42 | `"    review_data: dict[str, Any], corpus_data: dict[str, Any]"` | — |
| [SRC-03FF422A16-L000043](../../scripts/score_answer_quality_reviews.py#L43) | 43 | `") -> list[str]:"` | — |
| [SRC-03FF422A16-L000044](../../scripts/score_answer_quality_reviews.py#L44) | 44 | `"    problems: list[str] = []"` | — |
| [SRC-03FF422A16-L000045](../../scripts/score_answer_quality_reviews.py#L45) | 45 | `"    reviews = review_data.get(\"reviews\")"` | — |
| [SRC-03FF422A16-L000046](../../scripts/score_answer_quality_reviews.py#L46) | 46 | `"    corpus_cases = corpus_data.get(\"cases\")"` | — |
| [SRC-03FF422A16-L000047](../../scripts/score_answer_quality_reviews.py#L47) | 47 | `"    if not isinstance(reviews, list):"` | — |
| [SRC-03FF422A16-L000048](../../scripts/score_answer_quality_reviews.py#L48) | 48 | `"        return [\"reviews must be an array\"]"` | — |
| [SRC-03FF422A16-L000049](../../scripts/score_answer_quality_reviews.py#L49) | 49 | `"    if not isinstance(corpus_cases, list):"` | — |
| [SRC-03FF422A16-L000050](../../scripts/score_answer_quality_reviews.py#L50) | 50 | `"        return [\"corpus must contain a cases array\"]"` | — |
| [SRC-03FF422A16-L000051](../../scripts/score_answer_quality_reviews.py#L51) | 51 | `""` | — |
| [SRC-03FF422A16-L000052](../../scripts/score_answer_quality_reviews.py#L52) | 52 | `"    valid_case_ids = {"` | — |
| [SRC-03FF422A16-L000053](../../scripts/score_answer_quality_reviews.py#L53) | 53 | `"        item.get(\"case_id\")"` | — |
| [SRC-03FF422A16-L000054](../../scripts/score_answer_quality_reviews.py#L54) | 54 | `"        for item in corpus_cases"` | — |
| [SRC-03FF422A16-L000055](../../scripts/score_answer_quality_reviews.py#L55) | 55 | `"        if isinstance(item, dict) and isinstance(item.get(\"case_id\"), str)"` | — |
| [SRC-03FF422A16-L000056](../../scripts/score_answer_quality_reviews.py#L56) | 56 | `"    }"` | — |
| [SRC-03FF422A16-L000057](../../scripts/score_answer_quality_reviews.py#L57) | 57 | `"    seen: set[str] = set()"` | — |
| [SRC-03FF422A16-L000058](../../scripts/score_answer_quality_reviews.py#L58) | 58 | `"    for index, item in enumerate(reviews):"` | — |
| [SRC-03FF422A16-L000059](../../scripts/score_answer_quality_reviews.py#L59) | 59 | `"        label = \"reviews[\" + str(index) + \"]\""` | — |
| [SRC-03FF422A16-L000060](../../scripts/score_answer_quality_reviews.py#L60) | 60 | `"        if not isinstance(item, dict):"` | — |
| [SRC-03FF422A16-L000061](../../scripts/score_answer_quality_reviews.py#L61) | 61 | `"            problems.append(label + \" must be an object\")"` | — |
| [SRC-03FF422A16-L000062](../../scripts/score_answer_quality_reviews.py#L62) | 62 | `"            continue"` | — |
| [SRC-03FF422A16-L000063](../../scripts/score_answer_quality_reviews.py#L63) | 63 | `"        case_id = item.get(\"case_id\")"` | — |
