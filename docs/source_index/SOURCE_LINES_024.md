# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **024**
- سجلات الأسطر: **800**
- النطاق: SRC-A8360B1B03-L000190 إلى SRC-547CAF1FE3-L000110
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## ملفات أخرى

### FILE-A8360B1B03 — [scripts/hosted_smoke_test.py](../../scripts/hosted_smoke_test.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
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
| [SRC-4FFD5AFC54-L000028](../../scripts/run_answer_quality_benchmark.py#L28) | 28 | `"import os"` | — |
| [SRC-4FFD5AFC54-L000029](../../scripts/run_answer_quality_benchmark.py#L29) | 29 | `"import sys"` | — |
| [SRC-4FFD5AFC54-L000030](../../scripts/run_answer_quality_benchmark.py#L30) | 30 | `"import time"` | — |
| [SRC-4FFD5AFC54-L000031](../../scripts/run_answer_quality_benchmark.py#L31) | 31 | `"import urllib.error"` | — |
| [SRC-4FFD5AFC54-L000032](../../scripts/run_answer_quality_benchmark.py#L32) | 32 | `"import urllib.parse"` | — |
| [SRC-4FFD5AFC54-L000033](../../scripts/run_answer_quality_benchmark.py#L33) | 33 | `"import urllib.request"` | — |
| [SRC-4FFD5AFC54-L000034](../../scripts/run_answer_quality_benchmark.py#L34) | 34 | `"from datetime import UTC, datetime"` | — |
| [SRC-4FFD5AFC54-L000035](../../scripts/run_answer_quality_benchmark.py#L35) | 35 | `"from pathlib import Path"` | — |
| [SRC-4FFD5AFC54-L000036](../../scripts/run_answer_quality_benchmark.py#L36) | 36 | `""` | — |
| [SRC-4FFD5AFC54-L000037](../../scripts/run_answer_quality_benchmark.py#L37) | 37 | `"ROOT = Path(__file__).resolve().parents[1]"` | — |
| [SRC-4FFD5AFC54-L000038](../../scripts/run_answer_quality_benchmark.py#L38) | 38 | `"DEFAULT_CORPUS = ROOT / \"tests\" / \"fixtures\" / \"answer_quality_cases.json\""` | — |
| [SRC-4FFD5AFC54-L000039](../../scripts/run_answer_quality_benchmark.py#L39) | 39 | `"MAX_RESPONSE_BYTES = 2_000_000"` | — |
| [SRC-4FFD5AFC54-L000040](../../scripts/run_answer_quality_benchmark.py#L40) | 40 | `""` | — |
| [SRC-4FFD5AFC54-L000041](../../scripts/run_answer_quality_benchmark.py#L41) | 41 | `""` | — |
| [SRC-4FFD5AFC54-L000042](../../scripts/run_answer_quality_benchmark.py#L42) | 42 | `"def validate_base_url(base_url: str, *, token_present: bool = False) -> str:"` | — |
| [SRC-4FFD5AFC54-L000043](../../scripts/run_answer_quality_benchmark.py#L43) | 43 | `"    \"\"\"Validate and normalize an API origin before any request can carry a token.\"\"\""` | — |
| [SRC-4FFD5AFC54-L000044](../../scripts/run_answer_quality_benchmark.py#L44) | 44 | `"    if not isinstance(base_url, str) or not base_url.strip():"` | — |
| [SRC-4FFD5AFC54-L000045](../../scripts/run_answer_quality_benchmark.py#L45) | 45 | `"        raise ValueError(\"Base URL must be a non-empty HTTP(S) origin.\")"` | — |
| [SRC-4FFD5AFC54-L000046](../../scripts/run_answer_quality_benchmark.py#L46) | 46 | `"    try:"` | — |
| [SRC-4FFD5AFC54-L000047](../../scripts/run_answer_quality_benchmark.py#L47) | 47 | `"        parsed = urllib.parse.urlsplit(base_url.strip())"` | — |
| [SRC-4FFD5AFC54-L000048](../../scripts/run_answer_quality_benchmark.py#L48) | 48 | `"        scheme = parsed.scheme.lower()"` | — |
| [SRC-4FFD5AFC54-L000049](../../scripts/run_answer_quality_benchmark.py#L49) | 49 | `"        host = (parsed.hostname or \"\").lower().rstrip(\".\")"` | — |
| [SRC-4FFD5AFC54-L000050](../../scripts/run_answer_quality_benchmark.py#L50) | 50 | `"        port = parsed.port"` | — |
| [SRC-4FFD5AFC54-L000051](../../scripts/run_answer_quality_benchmark.py#L51) | 51 | `"    except ValueError as exc:"` | — |
| [SRC-4FFD5AFC54-L000052](../../scripts/run_answer_quality_benchmark.py#L52) | 52 | `"        raise ValueError(\"Base URL is malformed.\") from exc"` | — |
| [SRC-4FFD5AFC54-L000053](../../scripts/run_answer_quality_benchmark.py#L53) | 53 | `""` | — |
| [SRC-4FFD5AFC54-L000054](../../scripts/run_answer_quality_benchmark.py#L54) | 54 | `"    if scheme not in {\"http\", \"https\"} or not host:"` | — |
| [SRC-4FFD5AFC54-L000055](../../scripts/run_answer_quality_benchmark.py#L55) | 55 | `"        raise ValueError(\"Base URL must use HTTP or HTTPS and include a hostname.\")"` | — |
| [SRC-4FFD5AFC54-L000056](../../scripts/run_answer_quality_benchmark.py#L56) | 56 | `"    if parsed.username is not None or parsed.password is not None:"` | — |
| [SRC-4FFD5AFC54-L000057](../../scripts/run_answer_quality_benchmark.py#L57) | 57 | `"        raise ValueError(\"Base URL must not include a username or password.\")"` | — |
| [SRC-4FFD5AFC54-L000058](../../scripts/run_answer_quality_benchmark.py#L58) | 58 | `"    if parsed.path not in {\"\", \"/\"} or parsed.query or parsed.fragment:"` | — |
| [SRC-4FFD5AFC54-L000059](../../scripts/run_answer_quality_benchmark.py#L59) | 59 | `"        raise ValueError(\"Base URL must contain only the origin, without path, query, or fragment.\")"` | — |
| [SRC-4FFD5AFC54-L000060](../../scripts/run_answer_quality_benchmark.py#L60) | 60 | `""` | — |
| [SRC-4FFD5AFC54-L000061](../../scripts/run_answer_quality_benchmark.py#L61) | 61 | `"    loopback = host == \"localhost\""` | — |
| [SRC-4FFD5AFC54-L000062](../../scripts/run_answer_quality_benchmark.py#L62) | 62 | `"    try:"` | — |
| [SRC-4FFD5AFC54-L000063](../../scripts/run_answer_quality_benchmark.py#L63) | 63 | `"        loopback = ipaddress.ip_address(host).is_loopback"` | — |
| [SRC-4FFD5AFC54-L000064](../../scripts/run_answer_quality_benchmark.py#L64) | 64 | `"    except ValueError:"` | — |
| [SRC-4FFD5AFC54-L000065](../../scripts/run_answer_quality_benchmark.py#L65) | 65 | `"        pass"` | — |
| [SRC-4FFD5AFC54-L000066](../../scripts/run_answer_quality_benchmark.py#L66) | 66 | `""` | — |
| [SRC-4FFD5AFC54-L000067](../../scripts/run_answer_quality_benchmark.py#L67) | 67 | `"    if scheme == \"http\" and not loopback:"` | — |
| [SRC-4FFD5AFC54-L000068](../../scripts/run_answer_quality_benchmark.py#L68) | 68 | `"        raise ValueError(\"Plain HTTP is allowed only for localhost or a loopback IP.\")"` | — |
| [SRC-4FFD5AFC54-L000069](../../scripts/run_answer_quality_benchmark.py#L69) | 69 | `""` | — |
| [SRC-4FFD5AFC54-L000070](../../scripts/run_answer_quality_benchmark.py#L70) | 70 | `"    if (scheme == \"https\" and port == 443) or (scheme == \"http\" and port == 80):"` | — |
| [SRC-4FFD5AFC54-L000071](../../scripts/run_answer_quality_benchmark.py#L71) | 71 | `"        port = None"` | — |
| [SRC-4FFD5AFC54-L000072](../../scripts/run_answer_quality_benchmark.py#L72) | 72 | `"    host_for_origin = f\"[{host}]\" if \":\" in host else host"` | — |
| [SRC-4FFD5AFC54-L000073](../../scripts/run_answer_quality_benchmark.py#L73) | 73 | `"    origin = f\"{scheme}://{host_for_origin}\" + (f\":{port}\" if port is not None else \"\")"` | — |
| [SRC-4FFD5AFC54-L000074](../../scripts/run_answer_quality_benchmark.py#L74) | 74 | `""` | — |
| [SRC-4FFD5AFC54-L000075](../../scripts/run_answer_quality_benchmark.py#L75) | 75 | `"    if token_present and not loopback:"` | — |
| [SRC-4FFD5AFC54-L000076](../../scripts/run_answer_quality_benchmark.py#L76) | 76 | `"        allowed = os.getenv(\"OMARAI_BENCHMARK_ALLOWED_ORIGIN\", \"\").strip()"` | — |
| [SRC-4FFD5AFC54-L000077](../../scripts/run_answer_quality_benchmark.py#L77) | 77 | `"        if not allowed:"` | — |
| [SRC-4FFD5AFC54-L000078](../../scripts/run_answer_quality_benchmark.py#L78) | 78 | `"            raise ValueError("` | — |
| [SRC-4FFD5AFC54-L000079](../../scripts/run_answer_quality_benchmark.py#L79) | 79 | `"                \"A bearer token requires OMARAI_BENCHMARK_ALLOWED_ORIGIN to match \""` | — |
| [SRC-4FFD5AFC54-L000080](../../scripts/run_answer_quality_benchmark.py#L80) | 80 | `"                \"the exact HTTPS deployment origin.\""` | — |
| [SRC-4FFD5AFC54-L000081](../../scripts/run_answer_quality_benchmark.py#L81) | 81 | `"            )"` | — |
| [SRC-4FFD5AFC54-L000082](../../scripts/run_answer_quality_benchmark.py#L82) | 82 | `"        allowed_origin = validate_base_url(allowed, token_present=False)"` | — |
| [SRC-4FFD5AFC54-L000083](../../scripts/run_answer_quality_benchmark.py#L83) | 83 | `"        if allowed_origin != origin:"` | — |
| [SRC-4FFD5AFC54-L000084](../../scripts/run_answer_quality_benchmark.py#L84) | 84 | `"            raise ValueError("` | — |
| [SRC-4FFD5AFC54-L000085](../../scripts/run_answer_quality_benchmark.py#L85) | 85 | `"                \"Refusing to send the bearer token: base URL does not match \""` | — |
| [SRC-4FFD5AFC54-L000086](../../scripts/run_answer_quality_benchmark.py#L86) | 86 | `"                \"OMARAI_BENCHMARK_ALLOWED_ORIGIN.\""` | — |
| [SRC-4FFD5AFC54-L000087](../../scripts/run_answer_quality_benchmark.py#L87) | 87 | `"            )"` | — |
| [SRC-4FFD5AFC54-L000088](../../scripts/run_answer_quality_benchmark.py#L88) | 88 | `"    return origin"` | — |
| [SRC-4FFD5AFC54-L000089](../../scripts/run_answer_quality_benchmark.py#L89) | 89 | `""` | — |
| [SRC-4FFD5AFC54-L000090](../../scripts/run_answer_quality_benchmark.py#L90) | 90 | `""` | — |
| [SRC-4FFD5AFC54-L000091](../../scripts/run_answer_quality_benchmark.py#L91) | 91 | `"class _NoRedirectHandler(urllib.request.HTTPRedirectHandler):"` | — |
| [SRC-4FFD5AFC54-L000092](../../scripts/run_answer_quality_benchmark.py#L92) | 92 | `"    \"\"\"Do not follow redirects; the bearer token must never move to another origin.\"\"\""` | — |
| [SRC-4FFD5AFC54-L000093](../../scripts/run_answer_quality_benchmark.py#L93) | 93 | `""` | — |
| [SRC-4FFD5AFC54-L000094](../../scripts/run_answer_quality_benchmark.py#L94) | 94 | `"    def redirect_request(self, req, fp, code, msg, headers, newurl):"` | — |
| [SRC-4FFD5AFC54-L000095](../../scripts/run_answer_quality_benchmark.py#L95) | 95 | `"        return None"` | — |
| [SRC-4FFD5AFC54-L000096](../../scripts/run_answer_quality_benchmark.py#L96) | 96 | `""` | — |
| [SRC-4FFD5AFC54-L000097](../../scripts/run_answer_quality_benchmark.py#L97) | 97 | `""` | — |
| [SRC-4FFD5AFC54-L000098](../../scripts/run_answer_quality_benchmark.py#L98) | 98 | `"_NO_REDIRECT_OPENER = urllib.request.build_opener(_NoRedirectHandler())"` | — |
| [SRC-4FFD5AFC54-L000099](../../scripts/run_answer_quality_benchmark.py#L99) | 99 | `""` | — |
| [SRC-4FFD5AFC54-L000100](../../scripts/run_answer_quality_benchmark.py#L100) | 100 | `"REQUIRED_FIELDS = {"` | — |
| [SRC-4FFD5AFC54-L000101](../../scripts/run_answer_quality_benchmark.py#L101) | 101 | `"    \"case_id\","` | — |
| [SRC-4FFD5AFC54-L000102](../../scripts/run_answer_quality_benchmark.py#L102) | 102 | `"    \"category\","` | — |
| [SRC-4FFD5AFC54-L000103](../../scripts/run_answer_quality_benchmark.py#L103) | 103 | `"    \"language\","` | — |
| [SRC-4FFD5AFC54-L000104](../../scripts/run_answer_quality_benchmark.py#L104) | 104 | `"    \"question\","` | — |
| [SRC-4FFD5AFC54-L000105](../../scripts/run_answer_quality_benchmark.py#L105) | 105 | `"    \"expected_strategy\","` | — |
| [SRC-4FFD5AFC54-L000106](../../scripts/run_answer_quality_benchmark.py#L106) | 106 | `"    \"required_behaviors\","` | — |
| [SRC-4FFD5AFC54-L000107](../../scripts/run_answer_quality_benchmark.py#L107) | 107 | `"    \"forbidden_behaviors\","` | — |
| [SRC-4FFD5AFC54-L000108](../../scripts/run_answer_quality_benchmark.py#L108) | 108 | `"    \"evidence_fixture\","` | — |
| [SRC-4FFD5AFC54-L000109](../../scripts/run_answer_quality_benchmark.py#L109) | 109 | `"    \"failure_conditions\","` | — |
| [SRC-4FFD5AFC54-L000110](../../scripts/run_answer_quality_benchmark.py#L110) | 110 | `"    \"evaluation_mode\","` | — |
| [SRC-4FFD5AFC54-L000111](../../scripts/run_answer_quality_benchmark.py#L111) | 111 | `"}"` | — |
| [SRC-4FFD5AFC54-L000112](../../scripts/run_answer_quality_benchmark.py#L112) | 112 | `"ALLOWED_STRATEGIES = {\"local\", \"model_no_search\", \"web_search\", \"clarify\"}"` | — |
| [SRC-4FFD5AFC54-L000113](../../scripts/run_answer_quality_benchmark.py#L113) | 113 | `"ALLOWED_EVAL_MODES = {\"deterministic_structure\", \"fixture_assisted\", \"human_judgment\"}"` | — |
| [SRC-4FFD5AFC54-L000114](../../scripts/run_answer_quality_benchmark.py#L114) | 114 | `""` | — |
| [SRC-4FFD5AFC54-L000115](../../scripts/run_answer_quality_benchmark.py#L115) | 115 | `""` | — |
| [SRC-4FFD5AFC54-L000116](../../scripts/run_answer_quality_benchmark.py#L116) | 116 | `"def _utc_now() -> str:"` | — |
| [SRC-4FFD5AFC54-L000117](../../scripts/run_answer_quality_benchmark.py#L117) | 117 | `"    return datetime.now(UTC).isoformat(timespec=\"seconds\")"` | — |
| [SRC-4FFD5AFC54-L000118](../../scripts/run_answer_quality_benchmark.py#L118) | 118 | `""` | — |
| [SRC-4FFD5AFC54-L000119](../../scripts/run_answer_quality_benchmark.py#L119) | 119 | `""` | — |
| [SRC-4FFD5AFC54-L000120](../../scripts/run_answer_quality_benchmark.py#L120) | 120 | `"def load_corpus(path: Path) -> dict:"` | — |
| [SRC-4FFD5AFC54-L000121](../../scripts/run_answer_quality_benchmark.py#L121) | 121 | `"    if not path.is_file():"` | — |
| [SRC-4FFD5AFC54-L000122](../../scripts/run_answer_quality_benchmark.py#L122) | 122 | `"        raise FileNotFoundError(f\"Corpus not found: {path}\")"` | — |
| [SRC-4FFD5AFC54-L000123](../../scripts/run_answer_quality_benchmark.py#L123) | 123 | `"    data = json.loads(path.read_text(encoding=\"utf-8\"))"` | — |
| [SRC-4FFD5AFC54-L000124](../../scripts/run_answer_quality_benchmark.py#L124) | 124 | `"    if not isinstance(data, dict) or not isinstance(data.get(\"cases\"), list):"` | — |
| [SRC-4FFD5AFC54-L000125](../../scripts/run_answer_quality_benchmark.py#L125) | 125 | `"        raise TypeError(\"Corpus root must be an object with a cases array\")"` | — |
| [SRC-4FFD5AFC54-L000126](../../scripts/run_answer_quality_benchmark.py#L126) | 126 | `"    if data.get(\"parts\"):"` | — |
| [SRC-4FFD5AFC54-L000127](../../scripts/run_answer_quality_benchmark.py#L127) | 127 | `"        raise ValueError(\"Incomplete shard index is not accepted; use merged cases[] corpus\")"` | — |
| [SRC-4FFD5AFC54-L000128](../../scripts/run_answer_quality_benchmark.py#L128) | 128 | `"    return data"` | — |
| [SRC-4FFD5AFC54-L000129](../../scripts/run_answer_quality_benchmark.py#L129) | 129 | `""` | — |
| [SRC-4FFD5AFC54-L000130](../../scripts/run_answer_quality_benchmark.py#L130) | 130 | `""` | — |
| [SRC-4FFD5AFC54-L000131](../../scripts/run_answer_quality_benchmark.py#L131) | 131 | `"def validate_corpus(data: dict) -> list[str]:"` | — |
| [SRC-4FFD5AFC54-L000132](../../scripts/run_answer_quality_benchmark.py#L132) | 132 | `"    \"\"\"Return a list of human-readable problems (empty => OK).\"\"\""` | — |
| [SRC-4FFD5AFC54-L000133](../../scripts/run_answer_quality_benchmark.py#L133) | 133 | `"    problems: list[str] = []"` | — |
| [SRC-4FFD5AFC54-L000134](../../scripts/run_answer_quality_benchmark.py#L134) | 134 | `"    cases = data.get(\"cases\") or []"` | — |
| [SRC-4FFD5AFC54-L000135](../../scripts/run_answer_quality_benchmark.py#L135) | 135 | `"    if data.get(\"case_count\") != len(cases):"` | — |
| [SRC-4FFD5AFC54-L000136](../../scripts/run_answer_quality_benchmark.py#L136) | 136 | `"        problems.append("` | — |
| [SRC-4FFD5AFC54-L000137](../../scripts/run_answer_quality_benchmark.py#L137) | 137 | `"            f\"case_count metadata {data.get('case_count')!r} != len(cases) {len(cases)}\""` | — |
| [SRC-4FFD5AFC54-L000138](../../scripts/run_answer_quality_benchmark.py#L138) | 138 | `"        )"` | — |
| [SRC-4FFD5AFC54-L000139](../../scripts/run_answer_quality_benchmark.py#L139) | 139 | `"    if len(cases) < 40:"` | — |
| [SRC-4FFD5AFC54-L000140](../../scripts/run_answer_quality_benchmark.py#L140) | 140 | `"        problems.append(f\"expected at least 40 cases, found {len(cases)}\")"` | — |
| [SRC-4FFD5AFC54-L000141](../../scripts/run_answer_quality_benchmark.py#L141) | 141 | `"    ids: list[str] = []"` | — |
| [SRC-4FFD5AFC54-L000142](../../scripts/run_answer_quality_benchmark.py#L142) | 142 | `"    for i, case in enumerate(cases):"` | — |
| [SRC-4FFD5AFC54-L000143](../../scripts/run_answer_quality_benchmark.py#L143) | 143 | `"        if not isinstance(case, dict):"` | — |
| [SRC-4FFD5AFC54-L000144](../../scripts/run_answer_quality_benchmark.py#L144) | 144 | `"            problems.append(f\"cases[{i}] is not an object\")"` | — |
| [SRC-4FFD5AFC54-L000145](../../scripts/run_answer_quality_benchmark.py#L145) | 145 | `"            continue"` | — |
| [SRC-4FFD5AFC54-L000146](../../scripts/run_answer_quality_benchmark.py#L146) | 146 | `"        missing = REQUIRED_FIELDS - set(case)"` | — |
| [SRC-4FFD5AFC54-L000147](../../scripts/run_answer_quality_benchmark.py#L147) | 147 | `"        if missing:"` | — |
| [SRC-4FFD5AFC54-L000148](../../scripts/run_answer_quality_benchmark.py#L148) | 148 | `"            problems.append(f\"{case.get('case_id', i)}: missing {sorted(missing)}\")"` | — |
| [SRC-4FFD5AFC54-L000149](../../scripts/run_answer_quality_benchmark.py#L149) | 149 | `"        cid = case.get(\"case_id\")"` | — |
| [SRC-4FFD5AFC54-L000150](../../scripts/run_answer_quality_benchmark.py#L150) | 150 | `"        if isinstance(cid, str):"` | — |
| [SRC-4FFD5AFC54-L000151](../../scripts/run_answer_quality_benchmark.py#L151) | 151 | `"            ids.append(cid)"` | — |
| [SRC-4FFD5AFC54-L000152](../../scripts/run_answer_quality_benchmark.py#L152) | 152 | `"        if case.get(\"expected_strategy\") not in ALLOWED_STRATEGIES:"` | — |
| [SRC-4FFD5AFC54-L000153](../../scripts/run_answer_quality_benchmark.py#L153) | 153 | `"            problems.append(f\"{cid}: bad strategy {case.get('expected_strategy')!r}\")"` | — |
| [SRC-4FFD5AFC54-L000154](../../scripts/run_answer_quality_benchmark.py#L154) | 154 | `"        if case.get(\"evaluation_mode\") not in ALLOWED_EVAL_MODES:"` | — |
| [SRC-4FFD5AFC54-L000155](../../scripts/run_answer_quality_benchmark.py#L155) | 155 | `"            problems.append(f\"{cid}: bad evaluation_mode {case.get('evaluation_mode')!r}\")"` | — |
| [SRC-4FFD5AFC54-L000156](../../scripts/run_answer_quality_benchmark.py#L156) | 156 | `"        q = case.get(\"question\")"` | — |
| [SRC-4FFD5AFC54-L000157](../../scripts/run_answer_quality_benchmark.py#L157) | 157 | `"        if not isinstance(q, str) or len(q.strip()) < 2:"` | — |
| [SRC-4FFD5AFC54-L000158](../../scripts/run_answer_quality_benchmark.py#L158) | 158 | `"            problems.append(f\"{cid}: empty question\")"` | — |
| [SRC-4FFD5AFC54-L000159](../../scripts/run_answer_quality_benchmark.py#L159) | 159 | `"    if len(ids) != len(set(ids)):"` | — |
| [SRC-4FFD5AFC54-L000160](../../scripts/run_answer_quality_benchmark.py#L160) | 160 | `"        problems.append(\"duplicate case_id values\")"` | — |
| [SRC-4FFD5AFC54-L000161](../../scripts/run_answer_quality_benchmark.py#L161) | 161 | `"    return problems"` | — |
| [SRC-4FFD5AFC54-L000162](../../scripts/run_answer_quality_benchmark.py#L162) | 162 | `""` | — |
| [SRC-4FFD5AFC54-L000163](../../scripts/run_answer_quality_benchmark.py#L163) | 163 | `""` | — |
| [SRC-4FFD5AFC54-L000164](../../scripts/run_answer_quality_benchmark.py#L164) | 164 | `"def redact_secrets(text: str) -> str:"` | — |
| [SRC-4FFD5AFC54-L000165](../../scripts/run_answer_quality_benchmark.py#L165) | 165 | `"    \"\"\"Best-effort redaction of common secret patterns from stored outputs.\"\"\""` | — |
| [SRC-4FFD5AFC54-L000166](../../scripts/run_answer_quality_benchmark.py#L166) | 166 | `"    if not text:"` | — |
| [SRC-4FFD5AFC54-L000167](../../scripts/run_answer_quality_benchmark.py#L167) | 167 | `"        return text"` | — |
| [SRC-4FFD5AFC54-L000168](../../scripts/run_answer_quality_benchmark.py#L168) | 168 | `"    out = text"` | — |
| [SRC-4FFD5AFC54-L000169](../../scripts/run_answer_quality_benchmark.py#L169) | 169 | `"    for key in ("` | — |
| [SRC-4FFD5AFC54-L000170](../../scripts/run_answer_quality_benchmark.py#L170) | 170 | `"        \"OPENROUTER_API_KEY\","` | — |
| [SRC-4FFD5AFC54-L000171](../../scripts/run_answer_quality_benchmark.py#L171) | 171 | `"        \"OMARAI_ACCESS_TOKEN\","` | — |
| [SRC-4FFD5AFC54-L000172](../../scripts/run_answer_quality_benchmark.py#L172) | 172 | `"        \"OMARAI_LLM_API_KEY\","` | — |
| [SRC-4FFD5AFC54-L000173](../../scripts/run_answer_quality_benchmark.py#L173) | 173 | `"        \"Authorization\","` | — |
| [SRC-4FFD5AFC54-L000174](../../scripts/run_answer_quality_benchmark.py#L174) | 174 | `"        \"Bearer \","` | — |
| [SRC-4FFD5AFC54-L000175](../../scripts/run_answer_quality_benchmark.py#L175) | 175 | `"    ):"` | — |
| [SRC-4FFD5AFC54-L000176](../../scripts/run_answer_quality_benchmark.py#L176) | 176 | `"        out = out.replace(key, f\"[REDACTED:{key.strip()}]\")"` | — |
| [SRC-4FFD5AFC54-L000177](../../scripts/run_answer_quality_benchmark.py#L177) | 177 | `"    token = os.getenv(\"OMARAI_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-4FFD5AFC54-L000178](../../scripts/run_answer_quality_benchmark.py#L178) | 178 | `"    if token and token in out:"` | — |
| [SRC-4FFD5AFC54-L000179](../../scripts/run_answer_quality_benchmark.py#L179) | 179 | `"        out = out.replace(token, \"[REDACTED:OMARAI_ACCESS_TOKEN]\")"` | — |
| [SRC-4FFD5AFC54-L000180](../../scripts/run_answer_quality_benchmark.py#L180) | 180 | `"    for env_name in (\"OPENROUTER_API_KEY\", \"OMARAI_LLM_API_KEY\"):"` | — |
| [SRC-4FFD5AFC54-L000181](../../scripts/run_answer_quality_benchmark.py#L181) | 181 | `"        val = os.getenv(env_name, \"\").strip()"` | — |
| [SRC-4FFD5AFC54-L000182](../../scripts/run_answer_quality_benchmark.py#L182) | 182 | `"        if val and val in out:"` | — |
| [SRC-4FFD5AFC54-L000183](../../scripts/run_answer_quality_benchmark.py#L183) | 183 | `"            out = out.replace(val, f\"[REDACTED:{env_name}]\")"` | — |
| [SRC-4FFD5AFC54-L000184](../../scripts/run_answer_quality_benchmark.py#L184) | 184 | `"    return out"` | — |
| [SRC-4FFD5AFC54-L000185](../../scripts/run_answer_quality_benchmark.py#L185) | 185 | `""` | — |
| [SRC-4FFD5AFC54-L000186](../../scripts/run_answer_quality_benchmark.py#L186) | 186 | `""` | — |
| [SRC-4FFD5AFC54-L000187](../../scripts/run_answer_quality_benchmark.py#L187) | 187 | `"def post_agent("` | — |
| [SRC-4FFD5AFC54-L000188](../../scripts/run_answer_quality_benchmark.py#L188) | 188 | `"    base_url: str,"` | — |
| [SRC-4FFD5AFC54-L000189](../../scripts/run_answer_quality_benchmark.py#L189) | 189 | `"    question: str,"` | — |
| [SRC-4FFD5AFC54-L000190](../../scripts/run_answer_quality_benchmark.py#L190) | 190 | `"    timeout: float,"` | — |
| [SRC-4FFD5AFC54-L000191](../../scripts/run_answer_quality_benchmark.py#L191) | 191 | `"    token: str \| None,"` | — |
| [SRC-4FFD5AFC54-L000192](../../scripts/run_answer_quality_benchmark.py#L192) | 192 | `") -> tuple[int, dict \| str]:"` | — |
| [SRC-4FFD5AFC54-L000193](../../scripts/run_answer_quality_benchmark.py#L193) | 193 | `"    origin = validate_base_url(base_url, token_present=bool(token))"` | — |
| [SRC-4FFD5AFC54-L000194](../../scripts/run_answer_quality_benchmark.py#L194) | 194 | `"    url = origin + \"/api/agent\""` | — |
| [SRC-4FFD5AFC54-L000195](../../scripts/run_answer_quality_benchmark.py#L195) | 195 | `"    body = json.dumps({\"question\": question, \"history\": []}, ensure_ascii=False).encode(\"utf-8\")"` | — |
| [SRC-4FFD5AFC54-L000196](../../scripts/run_answer_quality_benchmark.py#L196) | 196 | `"    headers = {\"Content-Type\": \"application/json\", \"Content-Length\": str(len(body))}"` | — |
| [SRC-4FFD5AFC54-L000197](../../scripts/run_answer_quality_benchmark.py#L197) | 197 | `"    if token:"` | — |
| [SRC-4FFD5AFC54-L000198](../../scripts/run_answer_quality_benchmark.py#L198) | 198 | `"        headers[\"Authorization\"] = \"Bearer \" + token"` | — |
| [SRC-4FFD5AFC54-L000199](../../scripts/run_answer_quality_benchmark.py#L199) | 199 | `"    req = urllib.request.Request(url, data=body, headers=headers, method=\"POST\")"` | — |
| [SRC-4FFD5AFC54-L000200](../../scripts/run_answer_quality_benchmark.py#L200) | 200 | `"    try:"` | — |
| [SRC-4FFD5AFC54-L000201](../../scripts/run_answer_quality_benchmark.py#L201) | 201 | `"        with _NO_REDIRECT_OPENER.open(req, timeout=timeout) as resp:"` | — |
| [SRC-4FFD5AFC54-L000202](../../scripts/run_answer_quality_benchmark.py#L202) | 202 | `"            raw_bytes = resp.read(MAX_RESPONSE_BYTES + 1)"` | — |
| [SRC-4FFD5AFC54-L000203](../../scripts/run_answer_quality_benchmark.py#L203) | 203 | `"            if len(raw_bytes) > MAX_RESPONSE_BYTES:"` | — |
| [SRC-4FFD5AFC54-L000204](../../scripts/run_answer_quality_benchmark.py#L204) | 204 | `"                return 0, {\"error\": \"ResponseTooLarge\", \"detail\": \"Response exceeded the 2 MB limit.\"}"` | — |
| [SRC-4FFD5AFC54-L000205](../../scripts/run_answer_quality_benchmark.py#L205) | 205 | `"            raw = raw_bytes.decode(\"utf-8\", errors=\"replace\")"` | — |
| [SRC-4FFD5AFC54-L000206](../../scripts/run_answer_quality_benchmark.py#L206) | 206 | `"            status = getattr(resp, \"status\", 200)"` | — |
| [SRC-4FFD5AFC54-L000207](../../scripts/run_answer_quality_benchmark.py#L207) | 207 | `"            try:"` | — |
| [SRC-4FFD5AFC54-L000208](../../scripts/run_answer_quality_benchmark.py#L208) | 208 | `"                return status, json.loads(raw)"` | — |
| [SRC-4FFD5AFC54-L000209](../../scripts/run_answer_quality_benchmark.py#L209) | 209 | `"            except json.JSONDecodeError:"` | — |
| [SRC-4FFD5AFC54-L000210](../../scripts/run_answer_quality_benchmark.py#L210) | 210 | `"                return status, raw"` | — |
| [SRC-4FFD5AFC54-L000211](../../scripts/run_answer_quality_benchmark.py#L211) | 211 | `"    except urllib.error.HTTPError as exc:"` | — |
| [SRC-4FFD5AFC54-L000212](../../scripts/run_answer_quality_benchmark.py#L212) | 212 | `"        raw_bytes = exc.read(MAX_RESPONSE_BYTES + 1)"` | — |
| [SRC-4FFD5AFC54-L000213](../../scripts/run_answer_quality_benchmark.py#L213) | 213 | `"        if len(raw_bytes) > MAX_RESPONSE_BYTES:"` | — |
| [SRC-4FFD5AFC54-L000214](../../scripts/run_answer_quality_benchmark.py#L214) | 214 | `"            return exc.code, {\"error\": \"ResponseTooLarge\", \"detail\": \"Response exceeded the 2 MB limit.\"}"` | — |
| [SRC-4FFD5AFC54-L000215](../../scripts/run_answer_quality_benchmark.py#L215) | 215 | `"        raw = raw_bytes.decode(\"utf-8\", errors=\"replace\")"` | — |
| [SRC-4FFD5AFC54-L000216](../../scripts/run_answer_quality_benchmark.py#L216) | 216 | `"        try:"` | — |
| [SRC-4FFD5AFC54-L000217](../../scripts/run_answer_quality_benchmark.py#L217) | 217 | `"            return exc.code, json.loads(raw)"` | — |
| [SRC-4FFD5AFC54-L000218](../../scripts/run_answer_quality_benchmark.py#L218) | 218 | `"        except json.JSONDecodeError:"` | — |
| [SRC-4FFD5AFC54-L000219](../../scripts/run_answer_quality_benchmark.py#L219) | 219 | `"            return exc.code, raw"` | — |
| [SRC-4FFD5AFC54-L000220](../../scripts/run_answer_quality_benchmark.py#L220) | 220 | `"    except ValueError as exc:"` | — |
| [SRC-4FFD5AFC54-L000221](../../scripts/run_answer_quality_benchmark.py#L221) | 221 | `"        return 0, {\"error\": \"UnsafeBaseURL\", \"detail\": str(exc)}"` | — |
| [SRC-4FFD5AFC54-L000222](../../scripts/run_answer_quality_benchmark.py#L222) | 222 | `"    except (urllib.error.URLError, TimeoutError, OSError) as exc:"` | — |
| [SRC-4FFD5AFC54-L000223](../../scripts/run_answer_quality_benchmark.py#L223) | 223 | `"        return 0, {\"error\": type(exc).__name__, \"detail\": str(exc)}"` | — |
| [SRC-4FFD5AFC54-L000224](../../scripts/run_answer_quality_benchmark.py#L224) | 224 | `""` | — |
| [SRC-4FFD5AFC54-L000225](../../scripts/run_answer_quality_benchmark.py#L225) | 225 | `""` | — |
| [SRC-4FFD5AFC54-L000226](../../scripts/run_answer_quality_benchmark.py#L226) | 226 | `"def run_validate(corpus_path: Path, summary: bool) -> int:"` | — |
| [SRC-4FFD5AFC54-L000227](../../scripts/run_answer_quality_benchmark.py#L227) | 227 | `"    data = load_corpus(corpus_path)"` | — |
| [SRC-4FFD5AFC54-L000228](../../scripts/run_answer_quality_benchmark.py#L228) | 228 | `"    problems = validate_corpus(data)"` | — |
| [SRC-4FFD5AFC54-L000229](../../scripts/run_answer_quality_benchmark.py#L229) | 229 | `"    if problems:"` | — |
| [SRC-4FFD5AFC54-L000230](../../scripts/run_answer_quality_benchmark.py#L230) | 230 | `"        print(\"VALIDATE FAIL\")"` | — |
| [SRC-4FFD5AFC54-L000231](../../scripts/run_answer_quality_benchmark.py#L231) | 231 | `"        for p in problems:"` | — |
| [SRC-4FFD5AFC54-L000232](../../scripts/run_answer_quality_benchmark.py#L232) | 232 | `"            print(\" -\", p)"` | — |
| [SRC-4FFD5AFC54-L000233](../../scripts/run_answer_quality_benchmark.py#L233) | 233 | `"        return 1"` | — |
| [SRC-4FFD5AFC54-L000234](../../scripts/run_answer_quality_benchmark.py#L234) | 234 | `"    cases = data[\"cases\"]"` | — |
| [SRC-4FFD5AFC54-L000235](../../scripts/run_answer_quality_benchmark.py#L235) | 235 | `"    cats = sorted({c[\"category\"] for c in cases})"` | — |
| [SRC-4FFD5AFC54-L000236](../../scripts/run_answer_quality_benchmark.py#L236) | 236 | `"    langs = sorted({c[\"language\"] for c in cases})"` | — |
| [SRC-4FFD5AFC54-L000237](../../scripts/run_answer_quality_benchmark.py#L237) | 237 | `"    print(\"VALIDATE OK\")"` | — |
| [SRC-4FFD5AFC54-L000238](../../scripts/run_answer_quality_benchmark.py#L238) | 238 | `"    print(f\"benchmark_id={data.get('benchmark_id')} version={data.get('version')}\")"` | — |
| [SRC-4FFD5AFC54-L000239](../../scripts/run_answer_quality_benchmark.py#L239) | 239 | `"    print(f\"cases={len(cases)} categories={len(cats)} languages={langs}\")"` | — |
| [SRC-4FFD5AFC54-L000240](../../scripts/run_answer_quality_benchmark.py#L240) | 240 | `"    if summary:"` | — |
| [SRC-4FFD5AFC54-L000241](../../scripts/run_answer_quality_benchmark.py#L241) | 241 | `"        from collections import Counter"` | — |
| [SRC-4FFD5AFC54-L000242](../../scripts/run_answer_quality_benchmark.py#L242) | 242 | `""` | — |
| [SRC-4FFD5AFC54-L000243](../../scripts/run_answer_quality_benchmark.py#L243) | 243 | `"        print(\"strategies:\", dict(Counter(c[\"expected_strategy\"] for c in cases)))"` | — |
| [SRC-4FFD5AFC54-L000244](../../scripts/run_answer_quality_benchmark.py#L244) | 244 | `"        print(\"eval_modes:\", dict(Counter(c[\"evaluation_mode\"] for c in cases)))"` | — |
| [SRC-4FFD5AFC54-L000245](../../scripts/run_answer_quality_benchmark.py#L245) | 245 | `"        print(\"categories:\", \", \".join(cats))"` | — |
| [SRC-4FFD5AFC54-L000246](../../scripts/run_answer_quality_benchmark.py#L246) | 246 | `"    print("` | — |
| [SRC-4FFD5AFC54-L000247](../../scripts/run_answer_quality_benchmark.py#L247) | 247 | `"        \"NOTE: Structural validation is not answer-quality evaluation. \""` | — |
| [SRC-4FFD5AFC54-L000248](../../scripts/run_answer_quality_benchmark.py#L248) | 248 | `"        \"All reasoning cases remain NOT_TESTED until reviewed.\""` | — |
| [SRC-4FFD5AFC54-L000249](../../scripts/run_answer_quality_benchmark.py#L249) | 249 | `"    )"` | — |
| [SRC-4FFD5AFC54-L000250](../../scripts/run_answer_quality_benchmark.py#L250) | 250 | `"    return 0"` | — |
| [SRC-4FFD5AFC54-L000251](../../scripts/run_answer_quality_benchmark.py#L251) | 251 | `""` | — |
| [SRC-4FFD5AFC54-L000252](../../scripts/run_answer_quality_benchmark.py#L252) | 252 | `""` | — |
| [SRC-4FFD5AFC54-L000253](../../scripts/run_answer_quality_benchmark.py#L253) | 253 | `"def run_live("` | — |
| [SRC-4FFD5AFC54-L000254](../../scripts/run_answer_quality_benchmark.py#L254) | 254 | `"    corpus_path: Path,"` | — |
| [SRC-4FFD5AFC54-L000255](../../scripts/run_answer_quality_benchmark.py#L255) | 255 | `"    base_url: str,"` | — |
| [SRC-4FFD5AFC54-L000256](../../scripts/run_answer_quality_benchmark.py#L256) | 256 | `"    case_id: str \| None,"` | — |
| [SRC-4FFD5AFC54-L000257](../../scripts/run_answer_quality_benchmark.py#L257) | 257 | `"    limit: int,"` | — |
| [SRC-4FFD5AFC54-L000258](../../scripts/run_answer_quality_benchmark.py#L258) | 258 | `"    timeout: float,"` | — |
| [SRC-4FFD5AFC54-L000259](../../scripts/run_answer_quality_benchmark.py#L259) | 259 | `"    delay: float,"` | — |
| [SRC-4FFD5AFC54-L000260](../../scripts/run_answer_quality_benchmark.py#L260) | 260 | `"    out_path: Path \| None,"` | — |
| [SRC-4FFD5AFC54-L000261](../../scripts/run_answer_quality_benchmark.py#L261) | 261 | `") -> int:"` | — |
| [SRC-4FFD5AFC54-L000262](../../scripts/run_answer_quality_benchmark.py#L262) | 262 | `"    data = load_corpus(corpus_path)"` | — |
| [SRC-4FFD5AFC54-L000263](../../scripts/run_answer_quality_benchmark.py#L263) | 263 | `"    problems = validate_corpus(data)"` | — |
| [SRC-4FFD5AFC54-L000264](../../scripts/run_answer_quality_benchmark.py#L264) | 264 | `"    if problems:"` | — |
| [SRC-4FFD5AFC54-L000265](../../scripts/run_answer_quality_benchmark.py#L265) | 265 | `"        print(\"Corpus invalid; refusing live run:\")"` | — |
| [SRC-4FFD5AFC54-L000266](../../scripts/run_answer_quality_benchmark.py#L266) | 266 | `"        for p in problems:"` | — |
| [SRC-4FFD5AFC54-L000267](../../scripts/run_answer_quality_benchmark.py#L267) | 267 | `"            print(\" -\", p)"` | — |
| [SRC-4FFD5AFC54-L000268](../../scripts/run_answer_quality_benchmark.py#L268) | 268 | `"        return 2"` | — |
| [SRC-4FFD5AFC54-L000269](../../scripts/run_answer_quality_benchmark.py#L269) | 269 | `""` | — |
| [SRC-4FFD5AFC54-L000270](../../scripts/run_answer_quality_benchmark.py#L270) | 270 | `"    token = os.getenv(\"OMARAI_ACCESS_TOKEN\", \"\").strip() or None"` | — |
| [SRC-4FFD5AFC54-L000271](../../scripts/run_answer_quality_benchmark.py#L271) | 271 | `"    try:"` | — |
| [SRC-4FFD5AFC54-L000272](../../scripts/run_answer_quality_benchmark.py#L272) | 272 | `"        safe_base_url = validate_base_url(base_url, token_present=bool(token))"` | — |
| [SRC-4FFD5AFC54-L000273](../../scripts/run_answer_quality_benchmark.py#L273) | 273 | `"    except ValueError as exc:"` | — |
| [SRC-4FFD5AFC54-L000274](../../scripts/run_answer_quality_benchmark.py#L274) | 274 | `"        print(f\"Unsafe base URL; refusing live run: {exc}\", file=sys.stderr)"` | — |
| [SRC-4FFD5AFC54-L000275](../../scripts/run_answer_quality_benchmark.py#L275) | 275 | `"        return 2"` | — |
| [SRC-4FFD5AFC54-L000276](../../scripts/run_answer_quality_benchmark.py#L276) | 276 | `"    cases = data[\"cases\"]"` | — |
| [SRC-4FFD5AFC54-L000277](../../scripts/run_answer_quality_benchmark.py#L277) | 277 | `"    if case_id:"` | — |
| [SRC-4FFD5AFC54-L000278](../../scripts/run_answer_quality_benchmark.py#L278) | 278 | `"        cases = [c for c in cases if c[\"case_id\"] == case_id]"` | — |
| [SRC-4FFD5AFC54-L000279](../../scripts/run_answer_quality_benchmark.py#L279) | 279 | `"        if not cases:"` | — |
| [SRC-4FFD5AFC54-L000280](../../scripts/run_answer_quality_benchmark.py#L280) | 280 | `"            print(f\"Unknown case_id: {case_id}\", file=sys.stderr)"` | — |
| [SRC-4FFD5AFC54-L000281](../../scripts/run_answer_quality_benchmark.py#L281) | 281 | `"            return 2"` | — |
| [SRC-4FFD5AFC54-L000282](../../scripts/run_answer_quality_benchmark.py#L282) | 282 | `"    if limit > 0:"` | — |
| [SRC-4FFD5AFC54-L000283](../../scripts/run_answer_quality_benchmark.py#L283) | 283 | `"        cases = cases[:limit]"` | — |
| [SRC-4FFD5AFC54-L000284](../../scripts/run_answer_quality_benchmark.py#L284) | 284 | `""` | — |
| [SRC-4FFD5AFC54-L000285](../../scripts/run_answer_quality_benchmark.py#L285) | 285 | `"    results = []"` | — |
| [SRC-4FFD5AFC54-L000286](../../scripts/run_answer_quality_benchmark.py#L286) | 286 | `"    print("` | — |
| [SRC-4FFD5AFC54-L000287](../../scripts/run_answer_quality_benchmark.py#L287) | 287 | `"        \"LIVE mode: fixtures are NOT injected into the server. \""` | — |
| [SRC-4FFD5AFC54-L000288](../../scripts/run_answer_quality_benchmark.py#L288) | 288 | `"        \"Answers are recorded as NOT_TESTED (quality) unless transport fails.\""` | — |
| [SRC-4FFD5AFC54-L000289](../../scripts/run_answer_quality_benchmark.py#L289) | 289 | `"    )"` | — |
| [SRC-4FFD5AFC54-L000290](../../scripts/run_answer_quality_benchmark.py#L290) | 290 | `"    for case in cases:"` | — |
| [SRC-4FFD5AFC54-L000291](../../scripts/run_answer_quality_benchmark.py#L291) | 291 | `"        cid = case[\"case_id\"]"` | — |
| [SRC-4FFD5AFC54-L000292](../../scripts/run_answer_quality_benchmark.py#L292) | 292 | `"        prompt = case[\"question\"]"` | — |
| [SRC-4FFD5AFC54-L000293](../../scripts/run_answer_quality_benchmark.py#L293) | 293 | `"        status_code, payload = post_agent(safe_base_url, prompt, timeout, token)"` | — |
| [SRC-4FFD5AFC54-L000294](../../scripts/run_answer_quality_benchmark.py#L294) | 294 | `"        if isinstance(payload, dict):"` | — |
| [SRC-4FFD5AFC54-L000295](../../scripts/run_answer_quality_benchmark.py#L295) | 295 | `"            safe_payload = json.loads(redact_secrets(json.dumps(payload, ensure_ascii=False)))"` | — |
| [SRC-4FFD5AFC54-L000296](../../scripts/run_answer_quality_benchmark.py#L296) | 296 | `"        else:"` | — |
| [SRC-4FFD5AFC54-L000297](../../scripts/run_answer_quality_benchmark.py#L297) | 297 | `"            safe_payload = redact_secrets(str(payload))"` | — |
| [SRC-4FFD5AFC54-L000298](../../scripts/run_answer_quality_benchmark.py#L298) | 298 | `""` | — |
| [SRC-4FFD5AFC54-L000299](../../scripts/run_answer_quality_benchmark.py#L299) | 299 | `"        transport_ok = 200 <= status_code < 300"` | — |
| [SRC-4FFD5AFC54-L000300](../../scripts/run_answer_quality_benchmark.py#L300) | 300 | `"        record = {"` | — |
| [SRC-4FFD5AFC54-L000301](../../scripts/run_answer_quality_benchmark.py#L301) | 301 | `"            \"case_id\": cid,"` | — |
| [SRC-4FFD5AFC54-L000302](../../scripts/run_answer_quality_benchmark.py#L302) | 302 | `"            \"benchmark_version\": data.get(\"version\"),"` | — |
| [SRC-4FFD5AFC54-L000303](../../scripts/run_answer_quality_benchmark.py#L303) | 303 | `"            \"benchmark_id\": data.get(\"benchmark_id\"),"` | — |
| [SRC-4FFD5AFC54-L000304](../../scripts/run_answer_quality_benchmark.py#L304) | 304 | `"            \"executed_at_utc\": _utc_now(),"` | — |
| [SRC-4FFD5AFC54-L000305](../../scripts/run_answer_quality_benchmark.py#L305) | 305 | `"            \"mode\": \"live_api\","` | — |
| [SRC-4FFD5AFC54-L000306](../../scripts/run_answer_quality_benchmark.py#L306) | 306 | `"            \"base_url\": safe_base_url,"` | — |
| [SRC-4FFD5AFC54-L000307](../../scripts/run_answer_quality_benchmark.py#L307) | 307 | `"            \"http_status\": status_code,"` | — |
| [SRC-4FFD5AFC54-L000308](../../scripts/run_answer_quality_benchmark.py#L308) | 308 | `"            \"prompt\": prompt,"` | — |
| [SRC-4FFD5AFC54-L000309](../../scripts/run_answer_quality_benchmark.py#L309) | 309 | `"            \"expected_strategy\": case[\"expected_strategy\"],"` | — |
| [SRC-4FFD5AFC54-L000310](../../scripts/run_answer_quality_benchmark.py#L310) | 310 | `"            \"category\": case[\"category\"],"` | — |
| [SRC-4FFD5AFC54-L000311](../../scripts/run_answer_quality_benchmark.py#L311) | 311 | `"            \"response\": safe_payload,"` | — |
| [SRC-4FFD5AFC54-L000312](../../scripts/run_answer_quality_benchmark.py#L312) | 312 | `"            \"used_web_search\": ("` | — |
| [SRC-4FFD5AFC54-L000313](../../scripts/run_answer_quality_benchmark.py#L313) | 313 | `"                safe_payload.get(\"used_web_search\") if isinstance(safe_payload, dict) else None"` | — |
| [SRC-4FFD5AFC54-L000314](../../scripts/run_answer_quality_benchmark.py#L314) | 314 | `"            ),"` | — |
| [SRC-4FFD5AFC54-L000315](../../scripts/run_answer_quality_benchmark.py#L315) | 315 | `"            \"used_language_model\": ("` | — |
| [SRC-4FFD5AFC54-L000316](../../scripts/run_answer_quality_benchmark.py#L316) | 316 | `"                safe_payload.get(\"used_language_model\")"` | — |
| [SRC-4FFD5AFC54-L000317](../../scripts/run_answer_quality_benchmark.py#L317) | 317 | `"                if isinstance(safe_payload, dict)"` | — |
| [SRC-4FFD5AFC54-L000318](../../scripts/run_answer_quality_benchmark.py#L318) | 318 | `"                else None"` | — |
| [SRC-4FFD5AFC54-L000319](../../scripts/run_answer_quality_benchmark.py#L319) | 319 | `"            ),"` | — |
| [SRC-4FFD5AFC54-L000320](../../scripts/run_answer_quality_benchmark.py#L320) | 320 | `"            \"sources\": ("` | — |
| [SRC-4FFD5AFC54-L000321](../../scripts/run_answer_quality_benchmark.py#L321) | 321 | `"                safe_payload.get(\"sources\") if isinstance(safe_payload, dict) else None"` | — |
| [SRC-4FFD5AFC54-L000322](../../scripts/run_answer_quality_benchmark.py#L322) | 322 | `"            ),"` | — |
| [SRC-4FFD5AFC54-L000323](../../scripts/run_answer_quality_benchmark.py#L323) | 323 | `"            \"status\": \"NOT_TESTED\","` | — |
| [SRC-4FFD5AFC54-L000324](../../scripts/run_answer_quality_benchmark.py#L324) | 324 | `"            \"transport_ok\": transport_ok,"` | — |
| [SRC-4FFD5AFC54-L000325](../../scripts/run_answer_quality_benchmark.py#L325) | 325 | `"            \"reviewer_notes\": ("` | — |
| [SRC-4FFD5AFC54-L000326](../../scripts/run_answer_quality_benchmark.py#L326) | 326 | `"                \"Response collected; human/fixture review required for PASS/FAIL.\""` | — |
| [SRC-4FFD5AFC54-L000327](../../scripts/run_answer_quality_benchmark.py#L327) | 327 | `"                if transport_ok"` | — |
| [SRC-4FFD5AFC54-L000328](../../scripts/run_answer_quality_benchmark.py#L328) | 328 | `"                else \"Transport or HTTP error; quality not graded.\""` | — |
| [SRC-4FFD5AFC54-L000329](../../scripts/run_answer_quality_benchmark.py#L329) | 329 | `"            ),"` | — |
| [SRC-4FFD5AFC54-L000330](../../scripts/run_answer_quality_benchmark.py#L330) | 330 | `"            \"evidence_fixture_injected\": False,"` | — |
| [SRC-4FFD5AFC54-L000331](../../scripts/run_answer_quality_benchmark.py#L331) | 331 | `"        }"` | — |
| [SRC-4FFD5AFC54-L000332](../../scripts/run_answer_quality_benchmark.py#L332) | 332 | `"        results.append(record)"` | — |
| [SRC-4FFD5AFC54-L000333](../../scripts/run_answer_quality_benchmark.py#L333) | 333 | `"        flag = \"OK\" if transport_ok else \"ERR\""` | — |
| [SRC-4FFD5AFC54-L000334](../../scripts/run_answer_quality_benchmark.py#L334) | 334 | `"        print(f\"[{flag}] {cid} http={status_code}\")"` | — |
| [SRC-4FFD5AFC54-L000335](../../scripts/run_answer_quality_benchmark.py#L335) | 335 | `"        if delay > 0:"` | — |
| [SRC-4FFD5AFC54-L000336](../../scripts/run_answer_quality_benchmark.py#L336) | 336 | `"            time.sleep(delay)"` | — |
| [SRC-4FFD5AFC54-L000337](../../scripts/run_answer_quality_benchmark.py#L337) | 337 | `""` | — |
| [SRC-4FFD5AFC54-L000338](../../scripts/run_answer_quality_benchmark.py#L338) | 338 | `"    envelope = {"` | — |
| [SRC-4FFD5AFC54-L000339](../../scripts/run_answer_quality_benchmark.py#L339) | 339 | `"        \"benchmark_id\": data.get(\"benchmark_id\"),"` | — |
| [SRC-4FFD5AFC54-L000340](../../scripts/run_answer_quality_benchmark.py#L340) | 340 | `"        \"benchmark_version\": data.get(\"version\"),"` | — |
| [SRC-4FFD5AFC54-L000341](../../scripts/run_answer_quality_benchmark.py#L341) | 341 | `"        \"mode\": \"live_api\","` | — |
| [SRC-4FFD5AFC54-L000342](../../scripts/run_answer_quality_benchmark.py#L342) | 342 | `"        \"executed_at_utc\": _utc_now(),"` | — |
| [SRC-4FFD5AFC54-L000343](../../scripts/run_answer_quality_benchmark.py#L343) | 343 | `"        \"case_count\": len(results),"` | — |
| [SRC-4FFD5AFC54-L000344](../../scripts/run_answer_quality_benchmark.py#L344) | 344 | `"        \"results\": results,"` | — |
| [SRC-4FFD5AFC54-L000345](../../scripts/run_answer_quality_benchmark.py#L345) | 345 | `"        \"disclaimer\": ("` | — |
| [SRC-4FFD5AFC54-L000346](../../scripts/run_answer_quality_benchmark.py#L346) | 346 | `"            \"status=NOT_TESTED means answer quality was not auto-graded. \""` | — |
| [SRC-4FFD5AFC54-L000347](../../scripts/run_answer_quality_benchmark.py#L347) | 347 | `"            \"Fixtures in JSON were not applied to the live server.\""` | — |
| [SRC-4FFD5AFC54-L000348](../../scripts/run_answer_quality_benchmark.py#L348) | 348 | `"        ),"` | — |
| [SRC-4FFD5AFC54-L000349](../../scripts/run_answer_quality_benchmark.py#L349) | 349 | `"    }"` | — |
| [SRC-4FFD5AFC54-L000350](../../scripts/run_answer_quality_benchmark.py#L350) | 350 | `"    text = json.dumps(envelope, ensure_ascii=False, indent=2)"` | — |
| [SRC-4FFD5AFC54-L000351](../../scripts/run_answer_quality_benchmark.py#L351) | 351 | `"    if out_path:"` | — |
| [SRC-4FFD5AFC54-L000352](../../scripts/run_answer_quality_benchmark.py#L352) | 352 | `"        out_path.write_text(text + \"\\n\", encoding=\"utf-8\")"` | — |
| [SRC-4FFD5AFC54-L000353](../../scripts/run_answer_quality_benchmark.py#L353) | 353 | `"        print(f\"Wrote {out_path}\")"` | — |
| [SRC-4FFD5AFC54-L000354](../../scripts/run_answer_quality_benchmark.py#L354) | 354 | `"    else:"` | — |
| [SRC-4FFD5AFC54-L000355](../../scripts/run_answer_quality_benchmark.py#L355) | 355 | `"        print(text)"` | — |
| [SRC-4FFD5AFC54-L000356](../../scripts/run_answer_quality_benchmark.py#L356) | 356 | `"    return 0"` | — |
| [SRC-4FFD5AFC54-L000357](../../scripts/run_answer_quality_benchmark.py#L357) | 357 | `""` | — |
| [SRC-4FFD5AFC54-L000358](../../scripts/run_answer_quality_benchmark.py#L358) | 358 | `""` | — |
| [SRC-4FFD5AFC54-L000359](../../scripts/run_answer_quality_benchmark.py#L359) | 359 | `"def main(argv: list[str] \| None = None) -> int:"` | — |
| [SRC-4FFD5AFC54-L000360](../../scripts/run_answer_quality_benchmark.py#L360) | 360 | `"    parser = argparse.ArgumentParser(description=\"Omarai answer-quality benchmark runner\")"` | — |
| [SRC-4FFD5AFC54-L000361](../../scripts/run_answer_quality_benchmark.py#L361) | 361 | `"    parser.add_argument("` | — |
| [SRC-4FFD5AFC54-L000362](../../scripts/run_answer_quality_benchmark.py#L362) | 362 | `"        \"--mode\","` | — |
| [SRC-4FFD5AFC54-L000363](../../scripts/run_answer_quality_benchmark.py#L363) | 363 | `"        choices=(\"validate\", \"live\"),"` | — |
| [SRC-4FFD5AFC54-L000364](../../scripts/run_answer_quality_benchmark.py#L364) | 364 | `"        default=\"validate\","` | — |
| [SRC-4FFD5AFC54-L000365](../../scripts/run_answer_quality_benchmark.py#L365) | 365 | `"        help=\"validate=offline corpus check (default); live=opt-in API calls\","` | — |
| [SRC-4FFD5AFC54-L000366](../../scripts/run_answer_quality_benchmark.py#L366) | 366 | `"    )"` | — |
| [SRC-4FFD5AFC54-L000367](../../scripts/run_answer_quality_benchmark.py#L367) | 367 | `"    parser.add_argument("` | — |
| [SRC-4FFD5AFC54-L000368](../../scripts/run_answer_quality_benchmark.py#L368) | 368 | `"        \"--corpus\","` | — |
| [SRC-4FFD5AFC54-L000369](../../scripts/run_answer_quality_benchmark.py#L369) | 369 | `"        type=Path,"` | — |
| [SRC-4FFD5AFC54-L000370](../../scripts/run_answer_quality_benchmark.py#L370) | 370 | `"        default=DEFAULT_CORPUS,"` | — |
| [SRC-4FFD5AFC54-L000371](../../scripts/run_answer_quality_benchmark.py#L371) | 371 | `"        help=\"Path to answer_quality_cases.json\","` | — |
| [SRC-4FFD5AFC54-L000372](../../scripts/run_answer_quality_benchmark.py#L372) | 372 | `"    )"` | — |
| [SRC-4FFD5AFC54-L000373](../../scripts/run_answer_quality_benchmark.py#L373) | 373 | `"    parser.add_argument(\"--summary\", action=\"store_true\", help=\"Extra validate summary\")"` | — |
| [SRC-4FFD5AFC54-L000374](../../scripts/run_answer_quality_benchmark.py#L374) | 374 | `"    parser.add_argument(\"--base-url\", default=\"http://127.0.0.1:8765\")"` | — |
| [SRC-4FFD5AFC54-L000375](../../scripts/run_answer_quality_benchmark.py#L375) | 375 | `"    parser.add_argument(\"--case-id\", default=None, help=\"Run a single case (live)\")"` | — |
| [SRC-4FFD5AFC54-L000376](../../scripts/run_answer_quality_benchmark.py#L376) | 376 | `"    parser.add_argument(\"--limit\", type=int, default=0, help=\"Max cases in live mode (0=all selected)\")"` | — |
| [SRC-4FFD5AFC54-L000377](../../scripts/run_answer_quality_benchmark.py#L377) | 377 | `"    parser.add_argument(\"--timeout\", type=float, default=60.0)"` | — |
| [SRC-4FFD5AFC54-L000378](../../scripts/run_answer_quality_benchmark.py#L378) | 378 | `"    parser.add_argument(\"--delay\", type=float, default=0.0, help=\"Seconds between live requests\")"` | — |
| [SRC-4FFD5AFC54-L000379](../../scripts/run_answer_quality_benchmark.py#L379) | 379 | `"    parser.add_argument(\"--out\", type=Path, default=None, help=\"Write live results JSON\")"` | — |
| [SRC-4FFD5AFC54-L000380](../../scripts/run_answer_quality_benchmark.py#L380) | 380 | `"    args = parser.parse_args(argv)"` | — |
| [SRC-4FFD5AFC54-L000381](../../scripts/run_answer_quality_benchmark.py#L381) | 381 | `""` | — |
| [SRC-4FFD5AFC54-L000382](../../scripts/run_answer_quality_benchmark.py#L382) | 382 | `"    if args.mode == \"validate\":"` | — |
| [SRC-4FFD5AFC54-L000383](../../scripts/run_answer_quality_benchmark.py#L383) | 383 | `"        return run_validate(args.corpus, args.summary)"` | — |
| [SRC-4FFD5AFC54-L000384](../../scripts/run_answer_quality_benchmark.py#L384) | 384 | `"    if args.mode == \"live\":"` | — |
| [SRC-4FFD5AFC54-L000385](../../scripts/run_answer_quality_benchmark.py#L385) | 385 | `"        if not args.case_id and args.limit <= 0:"` | — |
| [SRC-4FFD5AFC54-L000386](../../scripts/run_answer_quality_benchmark.py#L386) | 386 | `"            print("` | — |
| [SRC-4FFD5AFC54-L000387](../../scripts/run_answer_quality_benchmark.py#L387) | 387 | `"                \"Refusing unbounded live run. Pass --case-id and/or --limit > 0.\","` | — |
| [SRC-4FFD5AFC54-L000388](../../scripts/run_answer_quality_benchmark.py#L388) | 388 | `"                file=sys.stderr,"` | — |
| [SRC-4FFD5AFC54-L000389](../../scripts/run_answer_quality_benchmark.py#L389) | 389 | `"            )"` | — |
| [SRC-4FFD5AFC54-L000390](../../scripts/run_answer_quality_benchmark.py#L390) | 390 | `"            return 2"` | — |
| [SRC-4FFD5AFC54-L000391](../../scripts/run_answer_quality_benchmark.py#L391) | 391 | `"        return run_live("` | — |
| [SRC-4FFD5AFC54-L000392](../../scripts/run_answer_quality_benchmark.py#L392) | 392 | `"            args.corpus,"` | — |
| [SRC-4FFD5AFC54-L000393](../../scripts/run_answer_quality_benchmark.py#L393) | 393 | `"            args.base_url,"` | — |
| [SRC-4FFD5AFC54-L000394](../../scripts/run_answer_quality_benchmark.py#L394) | 394 | `"            args.case_id,"` | — |
| [SRC-4FFD5AFC54-L000395](../../scripts/run_answer_quality_benchmark.py#L395) | 395 | `"            args.limit,"` | — |
| [SRC-4FFD5AFC54-L000396](../../scripts/run_answer_quality_benchmark.py#L396) | 396 | `"            args.timeout,"` | — |
| [SRC-4FFD5AFC54-L000397](../../scripts/run_answer_quality_benchmark.py#L397) | 397 | `"            args.delay,"` | — |
| [SRC-4FFD5AFC54-L000398](../../scripts/run_answer_quality_benchmark.py#L398) | 398 | `"            args.out,"` | — |
| [SRC-4FFD5AFC54-L000399](../../scripts/run_answer_quality_benchmark.py#L399) | 399 | `"        )"` | — |
| [SRC-4FFD5AFC54-L000400](../../scripts/run_answer_quality_benchmark.py#L400) | 400 | `"    return 2"` | — |
| [SRC-4FFD5AFC54-L000401](../../scripts/run_answer_quality_benchmark.py#L401) | 401 | `""` | — |
| [SRC-4FFD5AFC54-L000402](../../scripts/run_answer_quality_benchmark.py#L402) | 402 | `""` | — |
| [SRC-4FFD5AFC54-L000403](../../scripts/run_answer_quality_benchmark.py#L403) | 403 | `"if __name__ == \"__main__\":"` | — |
| [SRC-4FFD5AFC54-L000404](../../scripts/run_answer_quality_benchmark.py#L404) | 404 | `"    raise SystemExit(main())"` | — |
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
| [SRC-03FF422A16-L000064](../../scripts/score_answer_quality_reviews.py#L64) | 64 | `"        if not isinstance(case_id, str) or not case_id.strip():"` | — |
| [SRC-03FF422A16-L000065](../../scripts/score_answer_quality_reviews.py#L65) | 65 | `"            problems.append(label + \": case_id must be a non-empty string\")"` | — |
| [SRC-03FF422A16-L000066](../../scripts/score_answer_quality_reviews.py#L66) | 66 | `"            continue"` | — |
| [SRC-03FF422A16-L000067](../../scripts/score_answer_quality_reviews.py#L67) | 67 | `"        if case_id in seen:"` | — |
| [SRC-03FF422A16-L000068](../../scripts/score_answer_quality_reviews.py#L68) | 68 | `"            problems.append(case_id + \": duplicate review\")"` | — |
| [SRC-03FF422A16-L000069](../../scripts/score_answer_quality_reviews.py#L69) | 69 | `"        seen.add(case_id)"` | — |
| [SRC-03FF422A16-L000070](../../scripts/score_answer_quality_reviews.py#L70) | 70 | `"        if case_id not in valid_case_ids:"` | — |
| [SRC-03FF422A16-L000071](../../scripts/score_answer_quality_reviews.py#L71) | 71 | `"            problems.append(case_id + \": unknown case_id (not in the supplied corpus)\")"` | — |
| [SRC-03FF422A16-L000072](../../scripts/score_answer_quality_reviews.py#L72) | 72 | `"        status = item.get(\"status\")"` | — |
| [SRC-03FF422A16-L000073](../../scripts/score_answer_quality_reviews.py#L73) | 73 | `"        if status not in ALLOWED_STATUSES:"` | — |
| [SRC-03FF422A16-L000074](../../scripts/score_answer_quality_reviews.py#L74) | 74 | `"            problems.append(case_id + \": status must be one of \" + \", \".join(sorted(ALLOWED_STATUSES)))"` | — |
| [SRC-03FF422A16-L000075](../../scripts/score_answer_quality_reviews.py#L75) | 75 | `"            continue"` | — |
| [SRC-03FF422A16-L000076](../../scripts/score_answer_quality_reviews.py#L76) | 76 | `""` | — |
| [SRC-03FF422A16-L000077](../../scripts/score_answer_quality_reviews.py#L77) | 77 | `"        has_score = False"` | — |
| [SRC-03FF422A16-L000078](../../scripts/score_answer_quality_reviews.py#L78) | 78 | `"        for group_name, fields in COUNT_GROUPS.items():"` | — |
| [SRC-03FF422A16-L000079](../../scripts/score_answer_quality_reviews.py#L79) | 79 | `"            group = item.get(group_name)"` | — |
| [SRC-03FF422A16-L000080](../../scripts/score_answer_quality_reviews.py#L80) | 80 | `"            if group is None:"` | — |
| [SRC-03FF422A16-L000081](../../scripts/score_answer_quality_reviews.py#L81) | 81 | `"                continue"` | — |
| [SRC-03FF422A16-L000082](../../scripts/score_answer_quality_reviews.py#L82) | 82 | `"            if not isinstance(group, dict):"` | — |
| [SRC-03FF422A16-L000083](../../scripts/score_answer_quality_reviews.py#L83) | 83 | `"                problems.append(case_id + \": \" + group_name + \" must be an object\")"` | — |
| [SRC-03FF422A16-L000084](../../scripts/score_answer_quality_reviews.py#L84) | 84 | `"                continue"` | — |
| [SRC-03FF422A16-L000085](../../scripts/score_answer_quality_reviews.py#L85) | 85 | `"            has_score = True"` | — |
| [SRC-03FF422A16-L000086](../../scripts/score_answer_quality_reviews.py#L86) | 86 | `"            missing = [field for field in fields if field not in group]"` | — |
| [SRC-03FF422A16-L000087](../../scripts/score_answer_quality_reviews.py#L87) | 87 | `"            if missing:"` | — |
| [SRC-03FF422A16-L000088](../../scripts/score_answer_quality_reviews.py#L88) | 88 | `"                problems.append(case_id + \": \" + group_name + \" missing \" + \", \".join(missing))"` | — |
| [SRC-03FF422A16-L000089](../../scripts/score_answer_quality_reviews.py#L89) | 89 | `"                continue"` | — |
| [SRC-03FF422A16-L000090](../../scripts/score_answer_quality_reviews.py#L90) | 90 | `"            values: dict[str, int] = {}"` | — |
| [SRC-03FF422A16-L000091](../../scripts/score_answer_quality_reviews.py#L91) | 91 | `"            for field in fields:"` | — |
| [SRC-03FF422A16-L000092](../../scripts/score_answer_quality_reviews.py#L92) | 92 | `"                value = group[field]"` | — |
| [SRC-03FF422A16-L000093](../../scripts/score_answer_quality_reviews.py#L93) | 93 | `"                if not _is_nonnegative_int(value):"` | — |
| [SRC-03FF422A16-L000094](../../scripts/score_answer_quality_reviews.py#L94) | 94 | `"                    problems.append(case_id + \": \" + group_name + \".\" + field + \" must be a non-negative integer\")"` | — |
| [SRC-03FF422A16-L000095](../../scripts/score_answer_quality_reviews.py#L95) | 95 | `"                else:"` | — |
| [SRC-03FF422A16-L000096](../../scripts/score_answer_quality_reviews.py#L96) | 96 | `"                    values[field] = value"` | — |
| [SRC-03FF422A16-L000097](../../scripts/score_answer_quality_reviews.py#L97) | 97 | `"            if len(values) != len(fields):"` | — |
| [SRC-03FF422A16-L000098](../../scripts/score_answer_quality_reviews.py#L98) | 98 | `"                continue"` | — |
| [SRC-03FF422A16-L000099](../../scripts/score_answer_quality_reviews.py#L99) | 99 | `"            if group_name == \"retrieval\":"` | — |
| [SRC-03FF422A16-L000100](../../scripts/score_answer_quality_reviews.py#L100) | 100 | `"                if values[\"relevant_retrieved\"] > values[\"retrieved_count\"]:"` | — |
| [SRC-03FF422A16-L000101](../../scripts/score_answer_quality_reviews.py#L101) | 101 | `"                    problems.append(case_id + \": relevant_retrieved cannot exceed retrieved_count\")"` | — |
| [SRC-03FF422A16-L000102](../../scripts/score_answer_quality_reviews.py#L102) | 102 | `"                if values[\"relevant_retrieved\"] > values[\"relevant_available\"]:"` | — |
| [SRC-03FF422A16-L000103](../../scripts/score_answer_quality_reviews.py#L103) | 103 | `"                    problems.append(case_id + \": relevant_retrieved cannot exceed relevant_available\")"` | — |
| [SRC-03FF422A16-L000104](../../scripts/score_answer_quality_reviews.py#L104) | 104 | `"            else:"` | — |
| [SRC-03FF422A16-L000105](../../scripts/score_answer_quality_reviews.py#L105) | 105 | `"                numerator, denominator = fields"` | — |
| [SRC-03FF422A16-L000106](../../scripts/score_answer_quality_reviews.py#L106) | 106 | `"                if values[numerator] > values[denominator]:"` | — |
| [SRC-03FF422A16-L000107](../../scripts/score_answer_quality_reviews.py#L107) | 107 | `"                    problems.append(case_id + \": \" + numerator + \" cannot exceed \" + denominator)"` | — |
| [SRC-03FF422A16-L000108](../../scripts/score_answer_quality_reviews.py#L108) | 108 | `""` | — |
| [SRC-03FF422A16-L000109](../../scripts/score_answer_quality_reviews.py#L109) | 109 | `"        writing = item.get(\"writing_quality\")"` | — |
| [SRC-03FF422A16-L000110](../../scripts/score_answer_quality_reviews.py#L110) | 110 | `"        if writing is not None:"` | — |
| [SRC-03FF422A16-L000111](../../scripts/score_answer_quality_reviews.py#L111) | 111 | `"            has_score = True"` | — |
| [SRC-03FF422A16-L000112](../../scripts/score_answer_quality_reviews.py#L112) | 112 | `"            if ("` | — |
| [SRC-03FF422A16-L000113](../../scripts/score_answer_quality_reviews.py#L113) | 113 | `"                isinstance(writing, bool)"` | — |
| [SRC-03FF422A16-L000114](../../scripts/score_answer_quality_reviews.py#L114) | 114 | `"                or not isinstance(writing, (int, float))"` | — |
| [SRC-03FF422A16-L000115](../../scripts/score_answer_quality_reviews.py#L115) | 115 | `"                or not math.isfinite(float(writing))"` | — |
| [SRC-03FF422A16-L000116](../../scripts/score_answer_quality_reviews.py#L116) | 116 | `"                or float(writing) < 1"` | — |
| [SRC-03FF422A16-L000117](../../scripts/score_answer_quality_reviews.py#L117) | 117 | `"                or float(writing) > 5"` | — |
| [SRC-03FF422A16-L000118](../../scripts/score_answer_quality_reviews.py#L118) | 118 | `"            ):"` | — |
| [SRC-03FF422A16-L000119](../../scripts/score_answer_quality_reviews.py#L119) | 119 | `"                problems.append(case_id + \": writing_quality must be a finite score from 1 to 5\")"` | — |
| [SRC-03FF422A16-L000120](../../scripts/score_answer_quality_reviews.py#L120) | 120 | `""` | — |
| [SRC-03FF422A16-L000121](../../scripts/score_answer_quality_reviews.py#L121) | 121 | `"        if status != \"REVIEWED\" and has_score:"` | — |
| [SRC-03FF422A16-L000122](../../scripts/score_answer_quality_reviews.py#L122) | 122 | `"            problems.append(case_id + \": unreviewed case must not contain metric scores\")"` | — |
| [SRC-03FF422A16-L000123](../../scripts/score_answer_quality_reviews.py#L123) | 123 | `"        if status == \"REVIEWED\" and not has_score:"` | — |
| [SRC-03FF422A16-L000124](../../scripts/score_answer_quality_reviews.py#L124) | 124 | `"            problems.append(case_id + \": REVIEWED case must include at least one scored dimension\")"` | — |
| [SRC-03FF422A16-L000125](../../scripts/score_answer_quality_reviews.py#L125) | 125 | `"    return problems"` | — |
| [SRC-03FF422A16-L000126](../../scripts/score_answer_quality_reviews.py#L126) | 126 | `""` | — |
| [SRC-03FF422A16-L000127](../../scripts/score_answer_quality_reviews.py#L127) | 127 | `""` | — |
| [SRC-03FF422A16-L000128](../../scripts/score_answer_quality_reviews.py#L128) | 128 | `"def _ratio(numerator: int, denominator: int, case_count: int) -> dict[str, Any]:"` | — |
| [SRC-03FF422A16-L000129](../../scripts/score_answer_quality_reviews.py#L129) | 129 | `"    return {"` | — |
| [SRC-03FF422A16-L000130](../../scripts/score_answer_quality_reviews.py#L130) | 130 | `"        \"score\": round(numerator / denominator, 4) if denominator else None,"` | — |
| [SRC-03FF422A16-L000131](../../scripts/score_answer_quality_reviews.py#L131) | 131 | `"        \"numerator\": numerator,"` | — |
| [SRC-03FF422A16-L000132](../../scripts/score_answer_quality_reviews.py#L132) | 132 | `"        \"denominator\": denominator,"` | — |
| [SRC-03FF422A16-L000133](../../scripts/score_answer_quality_reviews.py#L133) | 133 | `"        \"reviewed_case_count\": case_count,"` | — |
| [SRC-03FF422A16-L000134](../../scripts/score_answer_quality_reviews.py#L134) | 134 | `"        \"status\": \"SCORED_FROM_HUMAN_REVIEW\" if denominator else \"NOT_SCORABLE_NO_ANNOTATED_DENOMINATOR\","` | — |
| [SRC-03FF422A16-L000135](../../scripts/score_answer_quality_reviews.py#L135) | 135 | `"    }"` | — |
| [SRC-03FF422A16-L000136](../../scripts/score_answer_quality_reviews.py#L136) | 136 | `""` | — |
| [SRC-03FF422A16-L000137](../../scripts/score_answer_quality_reviews.py#L137) | 137 | `""` | — |
| [SRC-03FF422A16-L000138](../../scripts/score_answer_quality_reviews.py#L138) | 138 | `"def summarize_reviews("` | — |
| [SRC-03FF422A16-L000139](../../scripts/score_answer_quality_reviews.py#L139) | 139 | `"    review_data: dict[str, Any], corpus_data: dict[str, Any]"` | — |
| [SRC-03FF422A16-L000140](../../scripts/score_answer_quality_reviews.py#L140) | 140 | `") -> dict[str, Any]:"` | — |
| [SRC-03FF422A16-L000141](../../scripts/score_answer_quality_reviews.py#L141) | 141 | `"    problems = validate_reviews(review_data, corpus_data)"` | — |
| [SRC-03FF422A16-L000142](../../scripts/score_answer_quality_reviews.py#L142) | 142 | `"    if problems:"` | — |
| [SRC-03FF422A16-L000143](../../scripts/score_answer_quality_reviews.py#L143) | 143 | `"        raise ValueError(\"; \".join(problems))"` | — |
| [SRC-03FF422A16-L000144](../../scripts/score_answer_quality_reviews.py#L144) | 144 | `"    reviews = review_data[\"reviews\"]"` | — |
| [SRC-03FF422A16-L000145](../../scripts/score_answer_quality_reviews.py#L145) | 145 | `"    reviewed = [item for item in reviews if item[\"status\"] == \"REVIEWED\"]"` | — |
| [SRC-03FF422A16-L000146](../../scripts/score_answer_quality_reviews.py#L146) | 146 | `"    status_counts = Counter(item[\"status\"] for item in reviews)"` | — |
| [SRC-03FF422A16-L000147](../../scripts/score_answer_quality_reviews.py#L147) | 147 | `"    corpus_count = len(corpus_data[\"cases\"])"` | — |
| [SRC-03FF422A16-L000148](../../scripts/score_answer_quality_reviews.py#L148) | 148 | `"    reviewed_ids = {item[\"case_id\"] for item in reviewed}"` | — |
| [SRC-03FF422A16-L000149](../../scripts/score_answer_quality_reviews.py#L149) | 149 | `""` | — |
| [SRC-03FF422A16-L000150](../../scripts/score_answer_quality_reviews.py#L150) | 150 | `"    retrieval_rel = retrieval_total = retrieval_available = 0"` | — |
| [SRC-03FF422A16-L000151](../../scripts/score_answer_quality_reviews.py#L151) | 151 | `"    retrieval_cases = set()"` | — |
| [SRC-03FF422A16-L000152](../../scripts/score_answer_quality_reviews.py#L152) | 152 | `"    faithfulness_supported = faithfulness_total = 0"` | — |
| [SRC-03FF422A16-L000153](../../scripts/score_answer_quality_reviews.py#L153) | 153 | `"    faithfulness_cases = set()"` | — |
| [SRC-03FF422A16-L000154](../../scripts/score_answer_quality_reviews.py#L154) | 154 | `"    correctness_correct = correctness_total = 0"` | — |
| [SRC-03FF422A16-L000155](../../scripts/score_answer_quality_reviews.py#L155) | 155 | `"    correctness_cases = set()"` | — |
| [SRC-03FF422A16-L000156](../../scripts/score_answer_quality_reviews.py#L156) | 156 | `"    citation_supported = citation_total = 0"` | — |
| [SRC-03FF422A16-L000157](../../scripts/score_answer_quality_reviews.py#L157) | 157 | `"    citation_cases = set()"` | — |
| [SRC-03FF422A16-L000158](../../scripts/score_answer_quality_reviews.py#L158) | 158 | `"    writing_scores: list[float] = []"` | — |
| [SRC-03FF422A16-L000159](../../scripts/score_answer_quality_reviews.py#L159) | 159 | `""` | — |
| [SRC-03FF422A16-L000160](../../scripts/score_answer_quality_reviews.py#L160) | 160 | `"    for item in reviewed:"` | — |
| [SRC-03FF422A16-L000161](../../scripts/score_answer_quality_reviews.py#L161) | 161 | `"        case_id = item[\"case_id\"]"` | — |
| [SRC-03FF422A16-L000162](../../scripts/score_answer_quality_reviews.py#L162) | 162 | `"        retrieval = item.get(\"retrieval\")"` | — |
| [SRC-03FF422A16-L000163](../../scripts/score_answer_quality_reviews.py#L163) | 163 | `"        if isinstance(retrieval, dict):"` | — |
| [SRC-03FF422A16-L000164](../../scripts/score_answer_quality_reviews.py#L164) | 164 | `"            retrieval_rel += retrieval[\"relevant_retrieved\"]"` | — |
| [SRC-03FF422A16-L000165](../../scripts/score_answer_quality_reviews.py#L165) | 165 | `"            retrieval_total += retrieval[\"retrieved_count\"]"` | — |
| [SRC-03FF422A16-L000166](../../scripts/score_answer_quality_reviews.py#L166) | 166 | `"            retrieval_available += retrieval[\"relevant_available\"]"` | — |
| [SRC-03FF422A16-L000167](../../scripts/score_answer_quality_reviews.py#L167) | 167 | `"            retrieval_cases.add(case_id)"` | — |
| [SRC-03FF422A16-L000168](../../scripts/score_answer_quality_reviews.py#L168) | 168 | `"        faithfulness = item.get(\"faithfulness\")"` | — |
| [SRC-03FF422A16-L000169](../../scripts/score_answer_quality_reviews.py#L169) | 169 | `"        if isinstance(faithfulness, dict):"` | — |
| [SRC-03FF422A16-L000170](../../scripts/score_answer_quality_reviews.py#L170) | 170 | `"            faithfulness_supported += faithfulness[\"supported_claims\"]"` | — |
| [SRC-03FF422A16-L000171](../../scripts/score_answer_quality_reviews.py#L171) | 171 | `"            faithfulness_total += faithfulness[\"reviewed_claims\"]"` | — |
| [SRC-03FF422A16-L000172](../../scripts/score_answer_quality_reviews.py#L172) | 172 | `"            faithfulness_cases.add(case_id)"` | — |
| [SRC-03FF422A16-L000173](../../scripts/score_answer_quality_reviews.py#L173) | 173 | `"        correctness = item.get(\"correctness\")"` | — |
| [SRC-03FF422A16-L000174](../../scripts/score_answer_quality_reviews.py#L174) | 174 | `"        if isinstance(correctness, dict):"` | — |
| [SRC-03FF422A16-L000175](../../scripts/score_answer_quality_reviews.py#L175) | 175 | `"            correctness_correct += correctness[\"correct_facts\"]"` | — |
| [SRC-03FF422A16-L000176](../../scripts/score_answer_quality_reviews.py#L176) | 176 | `"            correctness_total += correctness[\"reviewed_facts\"]"` | — |
| [SRC-03FF422A16-L000177](../../scripts/score_answer_quality_reviews.py#L177) | 177 | `"            correctness_cases.add(case_id)"` | — |
| [SRC-03FF422A16-L000178](../../scripts/score_answer_quality_reviews.py#L178) | 178 | `"        citations = item.get(\"citations\")"` | — |
| [SRC-03FF422A16-L000179](../../scripts/score_answer_quality_reviews.py#L179) | 179 | `"        if isinstance(citations, dict):"` | — |
| [SRC-03FF422A16-L000180](../../scripts/score_answer_quality_reviews.py#L180) | 180 | `"            citation_supported += citations[\"supported_citations\"]"` | — |
| [SRC-03FF422A16-L000181](../../scripts/score_answer_quality_reviews.py#L181) | 181 | `"            citation_total += citations[\"reviewed_citations\"]"` | — |
| [SRC-03FF422A16-L000182](../../scripts/score_answer_quality_reviews.py#L182) | 182 | `"            citation_cases.add(case_id)"` | — |
| [SRC-03FF422A16-L000183](../../scripts/score_answer_quality_reviews.py#L183) | 183 | `"        score = item.get(\"writing_quality\")"` | — |
| [SRC-03FF422A16-L000184](../../scripts/score_answer_quality_reviews.py#L184) | 184 | `"        if score is not None:"` | — |
| [SRC-03FF422A16-L000185](../../scripts/score_answer_quality_reviews.py#L185) | 185 | `"            writing_scores.append(float(score))"` | — |
| [SRC-03FF422A16-L000186](../../scripts/score_answer_quality_reviews.py#L186) | 186 | `""` | — |
| [SRC-03FF422A16-L000187](../../scripts/score_answer_quality_reviews.py#L187) | 187 | `"    return {"` | — |
| [SRC-03FF422A16-L000188](../../scripts/score_answer_quality_reviews.py#L188) | 188 | `"        \"benchmark_id\": corpus_data.get(\"benchmark_id\", \"unknown\"),"` | — |
| [SRC-03FF422A16-L000189](../../scripts/score_answer_quality_reviews.py#L189) | 189 | `"        \"review_schema_version\": review_data.get(\"schema_version\", \"unknown\"),"` | — |
| [SRC-03FF422A16-L000190](../../scripts/score_answer_quality_reviews.py#L190) | 190 | `"        \"scoring_method\": \"aggregate_from_explicit_human_annotations\","` | — |
| [SRC-03FF422A16-L000191](../../scripts/score_answer_quality_reviews.py#L191) | 191 | `"        \"automatic_answer_grading\": False,"` | — |
| [SRC-03FF422A16-L000192](../../scripts/score_answer_quality_reviews.py#L192) | 192 | `"        \"ragas_executed\": False,"` | — |
| [SRC-03FF422A16-L000193](../../scripts/score_answer_quality_reviews.py#L193) | 193 | `"        \"corpus_case_count\": corpus_count,"` | — |
| [SRC-03FF422A16-L000194](../../scripts/score_answer_quality_reviews.py#L194) | 194 | `"        \"submitted_review_count\": len(reviews),"` | — |
| [SRC-03FF422A16-L000195](../../scripts/score_answer_quality_reviews.py#L195) | 195 | `"        \"unique_reviewed_case_count\": len(reviewed_ids),"` | — |
| [SRC-03FF422A16-L000196](../../scripts/score_answer_quality_reviews.py#L196) | 196 | `"        \"case_status_counts\": {status: status_counts.get(status, 0) for status in sorted(ALLOWED_STATUSES)},"` | — |
| [SRC-03FF422A16-L000197](../../scripts/score_answer_quality_reviews.py#L197) | 197 | `"        \"reviewed_case_coverage\": round(len(reviewed_ids) / corpus_count, 4) if corpus_count else 0.0,"` | — |
| [SRC-03FF422A16-L000198](../../scripts/score_answer_quality_reviews.py#L198) | 198 | `"        \"metrics\": {"` | — |
| [SRC-03FF422A16-L000199](../../scripts/score_answer_quality_reviews.py#L199) | 199 | `"            \"retrieval_precision\": _ratio(retrieval_rel, retrieval_total, len(retrieval_cases)),"` | — |
| [SRC-03FF422A16-L000200](../../scripts/score_answer_quality_reviews.py#L200) | 200 | `"            \"retrieval_recall\": _ratio(retrieval_rel, retrieval_available, len(retrieval_cases)),"` | — |
| [SRC-03FF422A16-L000201](../../scripts/score_answer_quality_reviews.py#L201) | 201 | `"            \"faithfulness\": _ratio(faithfulness_supported, faithfulness_total, len(faithfulness_cases)),"` | — |
| [SRC-03FF422A16-L000202](../../scripts/score_answer_quality_reviews.py#L202) | 202 | `"            \"correctness\": _ratio(correctness_correct, correctness_total, len(correctness_cases)),"` | — |
| [SRC-03FF422A16-L000203](../../scripts/score_answer_quality_reviews.py#L203) | 203 | `"            \"citation_support\": _ratio(citation_supported, citation_total, len(citation_cases)),"` | — |
| [SRC-03FF422A16-L000204](../../scripts/score_answer_quality_reviews.py#L204) | 204 | `"            \"writing_quality_1_to_5\": {"` | — |
| [SRC-03FF422A16-L000205](../../scripts/score_answer_quality_reviews.py#L205) | 205 | `"                \"score\": round(sum(writing_scores) / len(writing_scores), 3) if writing_scores else None,"` | — |
| [SRC-03FF422A16-L000206](../../scripts/score_answer_quality_reviews.py#L206) | 206 | `"                \"scale_min\": 1,"` | — |
| [SRC-03FF422A16-L000207](../../scripts/score_answer_quality_reviews.py#L207) | 207 | `"                \"scale_max\": 5,"` | — |
| [SRC-03FF422A16-L000208](../../scripts/score_answer_quality_reviews.py#L208) | 208 | `"                \"reviewed_case_count\": len(writing_scores),"` | — |
| [SRC-03FF422A16-L000209](../../scripts/score_answer_quality_reviews.py#L209) | 209 | `"                \"status\": \"SCORED_FROM_HUMAN_REVIEW\" if writing_scores else \"NOT_SCORABLE_NO_HUMAN_SCORES\","` | — |
| [SRC-03FF422A16-L000210](../../scripts/score_answer_quality_reviews.py#L210) | 210 | `"            },"` | — |
| [SRC-03FF422A16-L000211](../../scripts/score_answer_quality_reviews.py#L211) | 211 | `"        },"` | — |
| [SRC-03FF422A16-L000212](../../scripts/score_answer_quality_reviews.py#L212) | 212 | `"        \"limitations\": ["` | — |
| [SRC-03FF422A16-L000213](../../scripts/score_answer_quality_reviews.py#L213) | 213 | `"            \"Metrics include only explicitly reviewed cases and human-entered labels.\","` | — |
| [SRC-03FF422A16-L000214](../../scripts/score_answer_quality_reviews.py#L214) | 214 | `"            \"Retrieval scores depend on consistent, deduplicated relevance counts and a defined candidate pool.\","` | — |
| [SRC-03FF422A16-L000215](../../scripts/score_answer_quality_reviews.py#L215) | 215 | `"            \"Faithfulness and correctness reflect reviewer judgments, not automatic proof of truth.\","` | — |
| [SRC-03FF422A16-L000216](../../scripts/score_answer_quality_reviews.py#L216) | 216 | `"            \"Writing quality is a 1-to-5 human rating; it is not a fluency model score.\","` | — |
| [SRC-03FF422A16-L000217](../../scripts/score_answer_quality_reviews.py#L217) | 217 | `"            \"RAGAS was not executed and no unobserved case is assigned a PASS.\","` | — |
| [SRC-03FF422A16-L000218](../../scripts/score_answer_quality_reviews.py#L218) | 218 | `"        ],"` | — |
| [SRC-03FF422A16-L000219](../../scripts/score_answer_quality_reviews.py#L219) | 219 | `"    }"` | — |
| [SRC-03FF422A16-L000220](../../scripts/score_answer_quality_reviews.py#L220) | 220 | `""` | — |
| [SRC-03FF422A16-L000221](../../scripts/score_answer_quality_reviews.py#L221) | 221 | `""` | — |
| [SRC-03FF422A16-L000222](../../scripts/score_answer_quality_reviews.py#L222) | 222 | `"def main(argv: list[str] \| None = None) -> int:"` | — |
| [SRC-03FF422A16-L000223](../../scripts/score_answer_quality_reviews.py#L223) | 223 | `"    parser = argparse.ArgumentParser(description=__doc__)"` | — |
| [SRC-03FF422A16-L000224](../../scripts/score_answer_quality_reviews.py#L224) | 224 | `"    parser.add_argument(\"--reviews\", required=True, type=Path, help=\"JSON file containing explicit human review annotations\")"` | — |
| [SRC-03FF422A16-L000225](../../scripts/score_answer_quality_reviews.py#L225) | 225 | `"    parser.add_argument(\"--corpus\", default=DEFAULT_CORPUS, type=Path, help=\"Answer-quality corpus used to validate case IDs\")"` | — |
| [SRC-03FF422A16-L000226](../../scripts/score_answer_quality_reviews.py#L226) | 226 | `"    parser.add_argument(\"--out\", type=Path, help=\"Optional path to write the summary JSON\")"` | — |
| [SRC-03FF422A16-L000227](../../scripts/score_answer_quality_reviews.py#L227) | 227 | `"    args = parser.parse_args(argv)"` | — |
| [SRC-03FF422A16-L000228](../../scripts/score_answer_quality_reviews.py#L228) | 228 | `""` | — |
| [SRC-03FF422A16-L000229](../../scripts/score_answer_quality_reviews.py#L229) | 229 | `"    try:"` | — |
| [SRC-03FF422A16-L000230](../../scripts/score_answer_quality_reviews.py#L230) | 230 | `"        reviews = load_json_object(args.reviews)"` | — |
| [SRC-03FF422A16-L000231](../../scripts/score_answer_quality_reviews.py#L231) | 231 | `"        corpus = load_json_object(args.corpus)"` | — |
| [SRC-03FF422A16-L000232](../../scripts/score_answer_quality_reviews.py#L232) | 232 | `"        summary = summarize_reviews(reviews, corpus)"` | — |
| [SRC-03FF422A16-L000233](../../scripts/score_answer_quality_reviews.py#L233) | 233 | `"    except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:"` | — |
| [SRC-03FF422A16-L000234](../../scripts/score_answer_quality_reviews.py#L234) | 234 | `"        print(\"REVIEW SCORECARD INVALID: \" + str(exc), file=sys.stderr)"` | — |
| [SRC-03FF422A16-L000235](../../scripts/score_answer_quality_reviews.py#L235) | 235 | `"        return 2"` | — |
| [SRC-03FF422A16-L000236](../../scripts/score_answer_quality_reviews.py#L236) | 236 | `""` | — |
| [SRC-03FF422A16-L000237](../../scripts/score_answer_quality_reviews.py#L237) | 237 | `"    output = json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True)"` | — |
| [SRC-03FF422A16-L000238](../../scripts/score_answer_quality_reviews.py#L238) | 238 | `"    if args.out:"` | — |
| [SRC-03FF422A16-L000239](../../scripts/score_answer_quality_reviews.py#L239) | 239 | `"        args.out.write_text(output + \"\\n\", encoding=\"utf-8\")"` | — |
| [SRC-03FF422A16-L000240](../../scripts/score_answer_quality_reviews.py#L240) | 240 | `"    print(output)"` | — |
| [SRC-03FF422A16-L000241](../../scripts/score_answer_quality_reviews.py#L241) | 241 | `"    return 0"` | — |
| [SRC-03FF422A16-L000242](../../scripts/score_answer_quality_reviews.py#L242) | 242 | `""` | — |
| [SRC-03FF422A16-L000243](../../scripts/score_answer_quality_reviews.py#L243) | 243 | `""` | — |
| [SRC-03FF422A16-L000244](../../scripts/score_answer_quality_reviews.py#L244) | 244 | `"if __name__ == \"__main__\":"` | — |
| [SRC-03FF422A16-L000245](../../scripts/score_answer_quality_reviews.py#L245) | 245 | `"    raise SystemExit(main())"` | — |
## ملفات أخرى

### FILE-547CAF1FE3 — [scripts/sqlite_backup_restore.py](../../scripts/sqlite_backup_restore.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-547CAF1FE3-L000001](../../scripts/sqlite_backup_restore.py#L1) | 1 | `"#!/usr/bin/env python3"` | — |
| [SRC-547CAF1FE3-L000002](../../scripts/sqlite_backup_restore.py#L2) | 2 | `"\"\"\"Create and restore verified, non-overwriting snapshots of Omarai's SQLite lead DB.\"\"\""` | — |
| [SRC-547CAF1FE3-L000003](../../scripts/sqlite_backup_restore.py#L3) | 3 | `"from __future__ import annotations"` | — |
| [SRC-547CAF1FE3-L000004](../../scripts/sqlite_backup_restore.py#L4) | 4 | `""` | — |
| [SRC-547CAF1FE3-L000005](../../scripts/sqlite_backup_restore.py#L5) | 5 | `"import argparse"` | — |
| [SRC-547CAF1FE3-L000006](../../scripts/sqlite_backup_restore.py#L6) | 6 | `"from contextlib import closing"` | — |
| [SRC-547CAF1FE3-L000007](../../scripts/sqlite_backup_restore.py#L7) | 7 | `"import json"` | — |
| [SRC-547CAF1FE3-L000008](../../scripts/sqlite_backup_restore.py#L8) | 8 | `"import os"` | — |
| [SRC-547CAF1FE3-L000009](../../scripts/sqlite_backup_restore.py#L9) | 9 | `"import sqlite3"` | — |
| [SRC-547CAF1FE3-L000010](../../scripts/sqlite_backup_restore.py#L10) | 10 | `"import sys"` | — |
| [SRC-547CAF1FE3-L000011](../../scripts/sqlite_backup_restore.py#L11) | 11 | `"from pathlib import Path"` | — |
| [SRC-547CAF1FE3-L000012](../../scripts/sqlite_backup_restore.py#L12) | 12 | `"from typing import Any"` | — |
| [SRC-547CAF1FE3-L000013](../../scripts/sqlite_backup_restore.py#L13) | 13 | `""` | — |
| [SRC-547CAF1FE3-L000014](../../scripts/sqlite_backup_restore.py#L14) | 14 | `""` | — |
| [SRC-547CAF1FE3-L000015](../../scripts/sqlite_backup_restore.py#L15) | 15 | `"class BackupError(RuntimeError):"` | — |
| [SRC-547CAF1FE3-L000016](../../scripts/sqlite_backup_restore.py#L16) | 16 | `"    \"\"\"Raised when a backup/restore operation cannot be proven safe.\"\"\""` | — |
| [SRC-547CAF1FE3-L000017](../../scripts/sqlite_backup_restore.py#L17) | 17 | `""` | — |
| [SRC-547CAF1FE3-L000018](../../scripts/sqlite_backup_restore.py#L18) | 18 | `""` | — |
| [SRC-547CAF1FE3-L000019](../../scripts/sqlite_backup_restore.py#L19) | 19 | `"def _open_read_only(path: Path) -> sqlite3.Connection:"` | — |
| [SRC-547CAF1FE3-L000020](../../scripts/sqlite_backup_restore.py#L20) | 20 | `"    \"\"\"Open an existing SQLite database without accidentally creating a missing source.\"\"\""` | — |
| [SRC-547CAF1FE3-L000021](../../scripts/sqlite_backup_restore.py#L21) | 21 | `"    try:"` | — |
| [SRC-547CAF1FE3-L000022](../../scripts/sqlite_backup_restore.py#L22) | 22 | `"        return sqlite3.connect(f\"{path.as_uri()}?mode=ro\", uri=True, timeout=10)"` | — |
| [SRC-547CAF1FE3-L000023](../../scripts/sqlite_backup_restore.py#L23) | 23 | `"    except (OSError, sqlite3.Error) as exc:"` | — |
| [SRC-547CAF1FE3-L000024](../../scripts/sqlite_backup_restore.py#L24) | 24 | `"        raise BackupError(f\"cannot open SQLite source: {type(exc).__name__}\") from exc"` | — |
| [SRC-547CAF1FE3-L000025](../../scripts/sqlite_backup_restore.py#L25) | 25 | `""` | — |
| [SRC-547CAF1FE3-L000026](../../scripts/sqlite_backup_restore.py#L26) | 26 | `""` | — |
| [SRC-547CAF1FE3-L000027](../../scripts/sqlite_backup_restore.py#L27) | 27 | `"def _validate_omarai_database(db: sqlite3.Connection) -> int:"` | — |
| [SRC-547CAF1FE3-L000028](../../scripts/sqlite_backup_restore.py#L28) | 28 | `"    \"\"\"Require a healthy SQLite file containing the Omarai leads table.\"\"\""` | — |
| [SRC-547CAF1FE3-L000029](../../scripts/sqlite_backup_restore.py#L29) | 29 | `"    try:"` | — |
| [SRC-547CAF1FE3-L000030](../../scripts/sqlite_backup_restore.py#L30) | 30 | `"        integrity_row = db.execute(\"PRAGMA integrity_check\").fetchone()"` | — |
| [SRC-547CAF1FE3-L000031](../../scripts/sqlite_backup_restore.py#L31) | 31 | `"        if not integrity_row or integrity_row[0] != \"ok\":"` | — |
| [SRC-547CAF1FE3-L000032](../../scripts/sqlite_backup_restore.py#L32) | 32 | `"            raise BackupError(\"SQLite integrity_check did not return ok\")"` | — |
| [SRC-547CAF1FE3-L000033](../../scripts/sqlite_backup_restore.py#L33) | 33 | `"        table_row = db.execute("` | — |
| [SRC-547CAF1FE3-L000034](../../scripts/sqlite_backup_restore.py#L34) | 34 | `"            \"SELECT 1 FROM sqlite_master WHERE type='table' AND name='leads'\""` | — |
| [SRC-547CAF1FE3-L000035](../../scripts/sqlite_backup_restore.py#L35) | 35 | `"        ).fetchone()"` | — |
| [SRC-547CAF1FE3-L000036](../../scripts/sqlite_backup_restore.py#L36) | 36 | `"        if not table_row:"` | — |
| [SRC-547CAF1FE3-L000037](../../scripts/sqlite_backup_restore.py#L37) | 37 | `"            raise BackupError(\"source is not an Omarai leads database\")"` | — |
| [SRC-547CAF1FE3-L000038](../../scripts/sqlite_backup_restore.py#L38) | 38 | `"        count_row = db.execute(\"SELECT COUNT(*) FROM leads\").fetchone()"` | — |
| [SRC-547CAF1FE3-L000039](../../scripts/sqlite_backup_restore.py#L39) | 39 | `"        if not count_row:"` | — |
| [SRC-547CAF1FE3-L000040](../../scripts/sqlite_backup_restore.py#L40) | 40 | `"            raise BackupError(\"could not count leads in database\")"` | — |
| [SRC-547CAF1FE3-L000041](../../scripts/sqlite_backup_restore.py#L41) | 41 | `"        return int(count_row[0])"` | — |
| [SRC-547CAF1FE3-L000042](../../scripts/sqlite_backup_restore.py#L42) | 42 | `"    except sqlite3.Error as exc:"` | — |
| [SRC-547CAF1FE3-L000043](../../scripts/sqlite_backup_restore.py#L43) | 43 | `"        raise BackupError(f\"SQLite validation failed: {type(exc).__name__}\") from exc"` | — |
| [SRC-547CAF1FE3-L000044](../../scripts/sqlite_backup_restore.py#L44) | 44 | `""` | — |
| [SRC-547CAF1FE3-L000045](../../scripts/sqlite_backup_restore.py#L45) | 45 | `""` | — |
| [SRC-547CAF1FE3-L000046](../../scripts/sqlite_backup_restore.py#L46) | 46 | `"def _create_destination_exclusively(path: Path) -> None:"` | — |
| [SRC-547CAF1FE3-L000047](../../scripts/sqlite_backup_restore.py#L47) | 47 | `"    \"\"\"Create a new destination without overwriting an existing file or following its symlink.\"\"\""` | — |
| [SRC-547CAF1FE3-L000048](../../scripts/sqlite_backup_restore.py#L48) | 48 | `"    path.parent.mkdir(parents=True, exist_ok=True)"` | — |
| [SRC-547CAF1FE3-L000049](../../scripts/sqlite_backup_restore.py#L49) | 49 | `"    descriptor = os.open(path, os.O_CREAT \| os.O_EXCL \| os.O_WRONLY, 0o600)"` | — |
| [SRC-547CAF1FE3-L000050](../../scripts/sqlite_backup_restore.py#L50) | 50 | `"    os.close(descriptor)"` | — |
| [SRC-547CAF1FE3-L000051](../../scripts/sqlite_backup_restore.py#L51) | 51 | `"    try:"` | — |
| [SRC-547CAF1FE3-L000052](../../scripts/sqlite_backup_restore.py#L52) | 52 | `"        path.chmod(0o600)"` | — |
| [SRC-547CAF1FE3-L000053](../../scripts/sqlite_backup_restore.py#L53) | 53 | `"    except OSError:"` | — |
| [SRC-547CAF1FE3-L000054](../../scripts/sqlite_backup_restore.py#L54) | 54 | `"        # The exclusive-create mode remains the primary permission setting; do not"` | — |
| [SRC-547CAF1FE3-L000055](../../scripts/sqlite_backup_restore.py#L55) | 55 | `"        # discard a completed backup solely because chmod is unavailable on a host."` | — |
| [SRC-547CAF1FE3-L000056](../../scripts/sqlite_backup_restore.py#L56) | 56 | `"        pass"` | — |
| [SRC-547CAF1FE3-L000057](../../scripts/sqlite_backup_restore.py#L57) | 57 | `""` | — |
| [SRC-547CAF1FE3-L000058](../../scripts/sqlite_backup_restore.py#L58) | 58 | `""` | — |
| [SRC-547CAF1FE3-L000059](../../scripts/sqlite_backup_restore.py#L59) | 59 | `"def _copy_verified_database(source: str \| Path, destination: str \| Path) -> dict[str, Any]:"` | — |
| [SRC-547CAF1FE3-L000060](../../scripts/sqlite_backup_restore.py#L60) | 60 | `"    source_path = Path(source).expanduser().resolve(strict=True)"` | — |
| [SRC-547CAF1FE3-L000061](../../scripts/sqlite_backup_restore.py#L61) | 61 | `"    requested_destination = Path(destination).expanduser()"` | — |
| [SRC-547CAF1FE3-L000062](../../scripts/sqlite_backup_restore.py#L62) | 62 | `"    destination_path = requested_destination.resolve(strict=False)"` | — |
| [SRC-547CAF1FE3-L000063](../../scripts/sqlite_backup_restore.py#L63) | 63 | `""` | — |
| [SRC-547CAF1FE3-L000064](../../scripts/sqlite_backup_restore.py#L64) | 64 | `"    if not source_path.is_file():"` | — |
| [SRC-547CAF1FE3-L000065](../../scripts/sqlite_backup_restore.py#L65) | 65 | `"        raise BackupError(\"source must be an existing regular file\")"` | — |
| [SRC-547CAF1FE3-L000066](../../scripts/sqlite_backup_restore.py#L66) | 66 | `"    if source_path == destination_path:"` | — |
| [SRC-547CAF1FE3-L000067](../../scripts/sqlite_backup_restore.py#L67) | 67 | `"        raise BackupError(\"source and destination must be different paths\")"` | — |
| [SRC-547CAF1FE3-L000068](../../scripts/sqlite_backup_restore.py#L68) | 68 | `"    # Check the user-supplied path before resolving it so a dangling symlink is"` | — |
| [SRC-547CAF1FE3-L000069](../../scripts/sqlite_backup_restore.py#L69) | 69 | `"    # never mistaken for an absent destination and followed to a new target."` | — |
| [SRC-547CAF1FE3-L000070](../../scripts/sqlite_backup_restore.py#L70) | 70 | `"    if requested_destination.exists() or requested_destination.is_symlink() or destination_path.exists():"` | — |
| [SRC-547CAF1FE3-L000071](../../scripts/sqlite_backup_restore.py#L71) | 71 | `"        raise FileExistsError(f\"destination already exists: {requested_destination}\")"` | — |
| [SRC-547CAF1FE3-L000072](../../scripts/sqlite_backup_restore.py#L72) | 72 | `""` | — |
| [SRC-547CAF1FE3-L000073](../../scripts/sqlite_backup_restore.py#L73) | 73 | `"    # Validate the source before creating anything at the destination."` | — |
| [SRC-547CAF1FE3-L000074](../../scripts/sqlite_backup_restore.py#L74) | 74 | `"    with closing(_open_read_only(source_path)) as source_db:"` | — |
| [SRC-547CAF1FE3-L000075](../../scripts/sqlite_backup_restore.py#L75) | 75 | `"        source_count = _validate_omarai_database(source_db)"` | — |
| [SRC-547CAF1FE3-L000076](../../scripts/sqlite_backup_restore.py#L76) | 76 | `"        _create_destination_exclusively(destination_path)"` | — |
| [SRC-547CAF1FE3-L000077](../../scripts/sqlite_backup_restore.py#L77) | 77 | `"        try:"` | — |
| [SRC-547CAF1FE3-L000078](../../scripts/sqlite_backup_restore.py#L78) | 78 | `"            with closing(sqlite3.connect(destination_path, timeout=10)) as destination_db:"` | — |
| [SRC-547CAF1FE3-L000079](../../scripts/sqlite_backup_restore.py#L79) | 79 | `"                source_db.backup(destination_db)"` | — |
| [SRC-547CAF1FE3-L000080](../../scripts/sqlite_backup_restore.py#L80) | 80 | `"                destination_db.commit()"` | — |
| [SRC-547CAF1FE3-L000081](../../scripts/sqlite_backup_restore.py#L81) | 81 | `"                restored_count = _validate_omarai_database(destination_db)"` | — |
| [SRC-547CAF1FE3-L000082](../../scripts/sqlite_backup_restore.py#L82) | 82 | `"                if restored_count != source_count:"` | — |
| [SRC-547CAF1FE3-L000083](../../scripts/sqlite_backup_restore.py#L83) | 83 | `"                    raise BackupError("` | — |
| [SRC-547CAF1FE3-L000084](../../scripts/sqlite_backup_restore.py#L84) | 84 | `"                        \"lead count changed during snapshot: \""` | — |
| [SRC-547CAF1FE3-L000085](../../scripts/sqlite_backup_restore.py#L85) | 85 | `"                        f\"source={source_count}, destination={restored_count}\""` | — |
| [SRC-547CAF1FE3-L000086](../../scripts/sqlite_backup_restore.py#L86) | 86 | `"                    )"` | — |
| [SRC-547CAF1FE3-L000087](../../scripts/sqlite_backup_restore.py#L87) | 87 | `"        except Exception:"` | — |
| [SRC-547CAF1FE3-L000088](../../scripts/sqlite_backup_restore.py#L88) | 88 | `"            # Remove only the destination created by this operation; never touch source."` | — |
| [SRC-547CAF1FE3-L000089](../../scripts/sqlite_backup_restore.py#L89) | 89 | `"            try:"` | — |
| [SRC-547CAF1FE3-L000090](../../scripts/sqlite_backup_restore.py#L90) | 90 | `"                destination_path.unlink(missing_ok=True)"` | — |
| [SRC-547CAF1FE3-L000091](../../scripts/sqlite_backup_restore.py#L91) | 91 | `"            except OSError:"` | — |
| [SRC-547CAF1FE3-L000092](../../scripts/sqlite_backup_restore.py#L92) | 92 | `"                pass"` | — |
| [SRC-547CAF1FE3-L000093](../../scripts/sqlite_backup_restore.py#L93) | 93 | `"            raise"` | — |
| [SRC-547CAF1FE3-L000094](../../scripts/sqlite_backup_restore.py#L94) | 94 | `""` | — |
| [SRC-547CAF1FE3-L000095](../../scripts/sqlite_backup_restore.py#L95) | 95 | `"    return {"` | — |
| [SRC-547CAF1FE3-L000096](../../scripts/sqlite_backup_restore.py#L96) | 96 | `"        \"result\": \"passed\","` | — |
| [SRC-547CAF1FE3-L000097](../../scripts/sqlite_backup_restore.py#L97) | 97 | `"        \"source\": str(source_path),"` | — |
| [SRC-547CAF1FE3-L000098](../../scripts/sqlite_backup_restore.py#L98) | 98 | `"        \"destination\": str(destination_path),"` | — |
| [SRC-547CAF1FE3-L000099](../../scripts/sqlite_backup_restore.py#L99) | 99 | `"        \"integrity_check\": \"ok\","` | — |
| [SRC-547CAF1FE3-L000100](../../scripts/sqlite_backup_restore.py#L100) | 100 | `"        \"lead_count\": source_count,"` | — |
| [SRC-547CAF1FE3-L000101](../../scripts/sqlite_backup_restore.py#L101) | 101 | `"        \"overwrite\": False,"` | — |
| [SRC-547CAF1FE3-L000102](../../scripts/sqlite_backup_restore.py#L102) | 102 | `"    }"` | — |
| [SRC-547CAF1FE3-L000103](../../scripts/sqlite_backup_restore.py#L103) | 103 | `""` | — |
| [SRC-547CAF1FE3-L000104](../../scripts/sqlite_backup_restore.py#L104) | 104 | `""` | — |
| [SRC-547CAF1FE3-L000105](../../scripts/sqlite_backup_restore.py#L105) | 105 | `"def backup_database(source: str \| Path, destination: str \| Path) -> dict[str, Any]:"` | — |
| [SRC-547CAF1FE3-L000106](../../scripts/sqlite_backup_restore.py#L106) | 106 | `"    \"\"\"Create a consistent SQLite snapshot of a healthy Omarai leads database.\"\"\""` | — |
| [SRC-547CAF1FE3-L000107](../../scripts/sqlite_backup_restore.py#L107) | 107 | `"    return _copy_verified_database(source, destination)"` | — |
| [SRC-547CAF1FE3-L000108](../../scripts/sqlite_backup_restore.py#L108) | 108 | `""` | — |
| [SRC-547CAF1FE3-L000109](../../scripts/sqlite_backup_restore.py#L109) | 109 | `""` | — |
| [SRC-547CAF1FE3-L000110](../../scripts/sqlite_backup_restore.py#L110) | 110 | `"def restore_database(backup: str \| Path, destination: str \| Path) -> dict[str, Any]:"` | — |
