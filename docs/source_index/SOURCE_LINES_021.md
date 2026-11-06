# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **021**
- سجلات الأسطر: **800**
- النطاق: SRC-1AE03B9EC3-L007181 إلى SRC-EEF2E6447C-L000682
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-1AE03B9EC3 — [agents/web_agent.py](../../agents/web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1AE03B9EC3-L007181](../../agents/web_agent.py#L7181) | 7181 | `"        if semantic_answer_withheld:"` | — |
| [SRC-1AE03B9EC3-L007182](../../agents/web_agent.py#L7182) | 7182 | `"            pipeline_completion_status = \"partial\""` | — |
| [SRC-1AE03B9EC3-L007183](../../agents/web_agent.py#L7183) | 7183 | `"        report[\"pipeline_completion_status\"] = pipeline_completion_status"` | — |
| [SRC-1AE03B9EC3-L007184](../../agents/web_agent.py#L7184) | 7184 | `"        report[\"completion_stages\"] = completion_stages"` | — |
| [SRC-1AE03B9EC3-L007185](../../agents/web_agent.py#L7185) | 7185 | `"        report[\"pipeline_completion_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L007186](../../agents/web_agent.py#L7186) | 7186 | `"            \"pipeline stage completion only; not a guarantee of factual correctness\""` | — |
| [SRC-1AE03B9EC3-L007187](../../agents/web_agent.py#L7187) | 7187 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007188](../../agents/web_agent.py#L7188) | 7188 | `""` | — |
| [SRC-1AE03B9EC3-L007189](../../agents/web_agent.py#L7189) | 7189 | `"        public_sources = []"` | — |
| [SRC-1AE03B9EC3-L007190](../../agents/web_agent.py#L7190) | 7190 | `"        for source in sources:"` | — |
| [SRC-1AE03B9EC3-L007191](../../agents/web_agent.py#L7191) | 7191 | `"            public_sources.append({"` | — |
| [SRC-1AE03B9EC3-L007192](../../agents/web_agent.py#L7192) | 7192 | `"                \"title\": source.get(\"title\") or \"نتيجة ويب\","` | — |
| [SRC-1AE03B9EC3-L007193](../../agents/web_agent.py#L7193) | 7193 | `"                \"url\": source[\"url\"],"` | — |
| [SRC-1AE03B9EC3-L007194](../../agents/web_agent.py#L7194) | 7194 | `"                \"snippet\": source.get(\"snippet\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L007195](../../agents/web_agent.py#L7195) | 7195 | `"                \"page_fetched\": bool(source.get(\"page_fetched\")),"` | — |
| [SRC-1AE03B9EC3-L007196](../../agents/web_agent.py#L7196) | 7196 | `"                \"readable_page_text_available\": bool(source.get(\"page_fetched\")) and bool(str(source.get(\"page_text\") or \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L007197](../../agents/web_agent.py#L7197) | 7197 | `"                \"page_text_present_without_fetch_flag\": bool(str(source.get(\"page_text\") or \"\").strip()) and not bool(source.get(\"page_fetched\")),"` | — |
| [SRC-1AE03B9EC3-L007198](../../agents/web_agent.py#L7198) | 7198 | `"                \"providers\": source.get(\"providers\", []),"` | — |
| [SRC-1AE03B9EC3-L007199](../../agents/web_agent.py#L7199) | 7199 | `"                \"queries\": source.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L007200](../../agents/web_agent.py#L7200) | 7200 | `"                \"platform\": source.get(\"platform\", \"web\"),"` | — |
| [SRC-1AE03B9EC3-L007201](../../agents/web_agent.py#L7201) | 7201 | `"                \"domain\": source.get(\"domain\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L007202](../../agents/web_agent.py#L7202) | 7202 | `"                \"source_class\": source.get(\"source_class\", \"general\"),"` | — |
| [SRC-1AE03B9EC3-L007203](../../agents/web_agent.py#L7203) | 7203 | `"                \"published_at\": source.get(\"published_at\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L007204](../../agents/web_agent.py#L7204) | 7204 | `"                \"publisher_name\": source.get(\"publisher_name\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L007205](../../agents/web_agent.py#L7205) | 7205 | `"                \"publisher_url\": source.get(\"publisher_url\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L007206](../../agents/web_agent.py#L7206) | 7206 | `"                \"rank_score\": round(float(source.get(\"rank_score\", 0)), 6),"` | — |
| [SRC-1AE03B9EC3-L007207](../../agents/web_agent.py#L7207) | 7207 | `"                \"lead_qualification\": source.get(\"lead_qualification\"),"` | — |
| [SRC-1AE03B9EC3-L007208](../../agents/web_agent.py#L7208) | 7208 | `"                \"lead_intent_evidence\": source.get(\"lead_intent_evidence\"),"` | — |
| [SRC-1AE03B9EC3-L007209](../../agents/web_agent.py#L7209) | 7209 | `"            })"` | — |
| [SRC-1AE03B9EC3-L007210](../../agents/web_agent.py#L7210) | 7210 | `"        return {"` | — |
| [SRC-1AE03B9EC3-L007211](../../agents/web_agent.py#L7211) | 7211 | `"            \"answer\": answer,"` | — |
| [SRC-1AE03B9EC3-L007212](../../agents/web_agent.py#L7212) | 7212 | `"            \"question\": question,"` | — |
| [SRC-1AE03B9EC3-L007213](../../agents/web_agent.py#L7213) | 7213 | `"            \"search_query\": (plan.get(\"queries\") or [\"\"])[0],"` | — |
| [SRC-1AE03B9EC3-L007214](../../agents/web_agent.py#L7214) | 7214 | `"            \"search_queries\": plan.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L007215](../../agents/web_agent.py#L7215) | 7215 | `"            \"research_plan\": {"` | — |
| [SRC-1AE03B9EC3-L007216](../../agents/web_agent.py#L7216) | 7216 | `"                \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L007217](../../agents/web_agent.py#L7217) | 7217 | `"                \"freshness\": plan.get(\"freshness\", \"any\"),"` | — |
| [SRC-1AE03B9EC3-L007218](../../agents/web_agent.py#L7218) | 7218 | `"                \"social_focus\": bool(plan.get(\"social_focus\")),"` | — |
| [SRC-1AE03B9EC3-L007219](../../agents/web_agent.py#L7219) | 7219 | `"                \"platforms\": plan.get(\"platforms\", []),"` | — |
| [SRC-1AE03B9EC3-L007220](../../agents/web_agent.py#L7220) | 7220 | `"                \"mode\": clean_mode,"` | — |
| [SRC-1AE03B9EC3-L007221](../../agents/web_agent.py#L7221) | 7221 | `"                \"direct_urls_provided\": len(plan.get(\"direct_urls\", [])),"` | — |
| [SRC-1AE03B9EC3-L007222](../../agents/web_agent.py#L7222) | 7222 | `"                \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L007223](../../agents/web_agent.py#L7223) | 7223 | `"                \"dialogue_context\": plan.get(\"dialogue_context\", {}),"` | — |
| [SRC-1AE03B9EC3-L007224](../../agents/web_agent.py#L7224) | 7224 | `"                \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L007225](../../agents/web_agent.py#L7225) | 7225 | `"                \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L007226](../../agents/web_agent.py#L7226) | 7226 | `"            },"` | — |
| [SRC-1AE03B9EC3-L007227](../../agents/web_agent.py#L7227) | 7227 | `"            \"search_report\": report,"` | — |
| [SRC-1AE03B9EC3-L007228](../../agents/web_agent.py#L7228) | 7228 | `"            \"sources\": public_sources,"` | — |
| [SRC-1AE03B9EC3-L007229](../../agents/web_agent.py#L7229) | 7229 | `"            \"research_quality\": research_quality,"` | — |
| [SRC-1AE03B9EC3-L007230](../../agents/web_agent.py#L7230) | 7230 | `"            \"citation_validation\": citation_validation,"` | — |
| [SRC-1AE03B9EC3-L007231](../../agents/web_agent.py#L7231) | 7231 | `"            \"answer_evidence_status\": answer_evidence_status,"` | — |
| [SRC-1AE03B9EC3-L007232](../../agents/web_agent.py#L7232) | 7232 | `"            \"answer_coverage\": answer_coverage,"` | — |
| [SRC-1AE03B9EC3-L007233](../../agents/web_agent.py#L7233) | 7233 | `"            \"answer_integrity\": answer_integrity,"` | — |
| [SRC-1AE03B9EC3-L007234](../../agents/web_agent.py#L7234) | 7234 | `"            \"task_fulfillment_status\": task_fulfillment_status,"` | — |
| [SRC-1AE03B9EC3-L007235](../../agents/web_agent.py#L7235) | 7235 | `"            \"coverage_repair_status\": coverage_repair_status,"` | — |
| [SRC-1AE03B9EC3-L007236](../../agents/web_agent.py#L7236) | 7236 | `"            \"used_language_model\": used_llm,"` | — |
| [SRC-1AE03B9EC3-L007237](../../agents/web_agent.py#L7237) | 7237 | `"            \"used_web_search\": bool(sources),"` | — |
| [SRC-1AE03B9EC3-L007238](../../agents/web_agent.py#L7238) | 7238 | `"            \"search_attempted\": search_attempted,"` | — |
| [SRC-1AE03B9EC3-L007239](../../agents/web_agent.py#L7239) | 7239 | `"            \"used_social_search\": bool(report.get(\"social_direct_results\", 0)),"` | — |
| [SRC-1AE03B9EC3-L007240](../../agents/web_agent.py#L7240) | 7240 | `"            \"warnings\": warnings,"` | — |
| [SRC-1AE03B9EC3-L007241](../../agents/web_agent.py#L7241) | 7241 | `"            \"kind\": \"web_research\" if used_llm else \"web_fallback\","` | — |
| [SRC-1AE03B9EC3-L007242](../../agents/web_agent.py#L7242) | 7242 | `"            \"final_answer_status\": final_answer_status,"` | — |
| [SRC-1AE03B9EC3-L007243](../../agents/web_agent.py#L7243) | 7243 | `"            \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L007244](../../agents/web_agent.py#L7244) | 7244 | `"            \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L007245](../../agents/web_agent.py#L7245) | 7245 | `"        }"` | — |
| [SRC-1AE03B9EC3-L007246](../../agents/web_agent.py#L7246) | 7246 | `""` | — |
| [SRC-1AE03B9EC3-L007247](../../agents/web_agent.py#L7247) | 7247 | `"def _normalized_provider_usage("` | — |
| [SRC-1AE03B9EC3-L007248](../../agents/web_agent.py#L7248) | 7248 | `"    usage: Any, *, provider_base_url: str = \"\""` | — |
| [SRC-1AE03B9EC3-L007249](../../agents/web_agent.py#L7249) | 7249 | `") -> dict[str, int \| float] \| None:"` | — |
| [SRC-1AE03B9EC3-L007250](../../agents/web_agent.py#L7250) | 7250 | `"    \"\"\"Allowlist safe counters; interpret generic 'cost' as USD only for OpenRouter.\"\"\""` | — |
| [SRC-1AE03B9EC3-L007251](../../agents/web_agent.py#L7251) | 7251 | `"    if not isinstance(usage, dict):"` | — |
| [SRC-1AE03B9EC3-L007252](../../agents/web_agent.py#L7252) | 7252 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L007253](../../agents/web_agent.py#L7253) | 7253 | `"    normalized: dict[str, int \| float] = {}"` | — |
| [SRC-1AE03B9EC3-L007254](../../agents/web_agent.py#L7254) | 7254 | `"    for source_key in (\"prompt_tokens\", \"completion_tokens\", \"total_tokens\"):"` | — |
| [SRC-1AE03B9EC3-L007255](../../agents/web_agent.py#L7255) | 7255 | `"        value = usage.get(source_key)"` | — |
| [SRC-1AE03B9EC3-L007256](../../agents/web_agent.py#L7256) | 7256 | `"        if isinstance(value, int) and not isinstance(value, bool) and value >= 0:"` | — |
| [SRC-1AE03B9EC3-L007257](../../agents/web_agent.py#L7257) | 7257 | `"            normalized[source_key] = value"` | — |
| [SRC-1AE03B9EC3-L007258](../../agents/web_agent.py#L7258) | 7258 | `"    cost_keys = [\"cost_usd\"]"` | — |
| [SRC-1AE03B9EC3-L007259](../../agents/web_agent.py#L7259) | 7259 | `"    provider_host = \"\""` | — |
| [SRC-1AE03B9EC3-L007260](../../agents/web_agent.py#L7260) | 7260 | `"    if isinstance(provider_base_url, str):"` | — |
| [SRC-1AE03B9EC3-L007261](../../agents/web_agent.py#L7261) | 7261 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L007262](../../agents/web_agent.py#L7262) | 7262 | `"            provider_host = (urllib.parse.urlsplit(provider_base_url.strip()).hostname or \"\").lower().rstrip(\".\")"` | — |
| [SRC-1AE03B9EC3-L007263](../../agents/web_agent.py#L7263) | 7263 | `"        except ValueError:"` | — |
| [SRC-1AE03B9EC3-L007264](../../agents/web_agent.py#L7264) | 7264 | `"            provider_host = \"\""` | — |
| [SRC-1AE03B9EC3-L007265](../../agents/web_agent.py#L7265) | 7265 | `"    is_openrouter = ("` | — |
| [SRC-1AE03B9EC3-L007266](../../agents/web_agent.py#L7266) | 7266 | `"        provider_host == \"openrouter.ai\""` | — |
| [SRC-1AE03B9EC3-L007267](../../agents/web_agent.py#L7267) | 7267 | `"        or provider_host.endswith(\".openrouter.ai\")"` | — |
| [SRC-1AE03B9EC3-L007268](../../agents/web_agent.py#L7268) | 7268 | `"    )"` | — |
| [SRC-1AE03B9EC3-L007269](../../agents/web_agent.py#L7269) | 7269 | `"    if is_openrouter:"` | — |
| [SRC-1AE03B9EC3-L007270](../../agents/web_agent.py#L7270) | 7270 | `"        cost_keys.extend([\"cost\", \"total_cost\"])"` | — |
| [SRC-1AE03B9EC3-L007271](../../agents/web_agent.py#L7271) | 7271 | `"    for source_key in cost_keys:"` | — |
| [SRC-1AE03B9EC3-L007272](../../agents/web_agent.py#L7272) | 7272 | `"        value = usage.get(source_key)"` | — |
| [SRC-1AE03B9EC3-L007273](../../agents/web_agent.py#L7273) | 7273 | `"        if isinstance(value, (int, float)) and not isinstance(value, bool):"` | — |
| [SRC-1AE03B9EC3-L007274](../../agents/web_agent.py#L7274) | 7274 | `"            number = float(value)"` | — |
| [SRC-1AE03B9EC3-L007275](../../agents/web_agent.py#L7275) | 7275 | `"            if number >= 0 and math.isfinite(number):"` | — |
| [SRC-1AE03B9EC3-L007276](../../agents/web_agent.py#L7276) | 7276 | `"                normalized[\"cost_usd\"] = number"` | — |
| [SRC-1AE03B9EC3-L007277](../../agents/web_agent.py#L7277) | 7277 | `"                break"` | — |
| [SRC-1AE03B9EC3-L007278](../../agents/web_agent.py#L7278) | 7278 | `"    return normalized or None"` | — |
| [SRC-1AE03B9EC3-L007279](../../agents/web_agent.py#L7279) | 7279 | `""` | — |
| [SRC-1AE03B9EC3-L007280](../../agents/web_agent.py#L7280) | 7280 | `"def _model_usage_record("` | — |
| [SRC-1AE03B9EC3-L007281](../../agents/web_agent.py#L7281) | 7281 | `"    requested_model: str,"` | — |
| [SRC-1AE03B9EC3-L007282](../../agents/web_agent.py#L7282) | 7282 | `"    candidate_model: str,"` | — |
| [SRC-1AE03B9EC3-L007283](../../agents/web_agent.py#L7283) | 7283 | `"    response_data: dict[str, Any],"` | — |
| [SRC-1AE03B9EC3-L007284](../../agents/web_agent.py#L7284) | 7284 | `"    provider_base_url: str,"` | — |
| [SRC-1AE03B9EC3-L007285](../../agents/web_agent.py#L7285) | 7285 | `") -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L007286](../../agents/web_agent.py#L7286) | 7286 | `"    \"\"\"Return only allowlisted provider usage metadata, never raw prompts/responses.\"\"\""` | — |
| [SRC-1AE03B9EC3-L007287](../../agents/web_agent.py#L7287) | 7287 | `"    record: dict[str, Any] = {"` | — |
| [SRC-1AE03B9EC3-L007288](../../agents/web_agent.py#L7288) | 7288 | `"        \"requested_model\": requested_model,"` | — |
| [SRC-1AE03B9EC3-L007289](../../agents/web_agent.py#L7289) | 7289 | `"        \"used_model\": candidate_model,"` | — |
| [SRC-1AE03B9EC3-L007290](../../agents/web_agent.py#L7290) | 7290 | `"        \"fallback_used\": \"true\" if candidate_model != requested_model else \"false\","` | — |
| [SRC-1AE03B9EC3-L007291](../../agents/web_agent.py#L7291) | 7291 | `"    }"` | — |
| [SRC-1AE03B9EC3-L007292](../../agents/web_agent.py#L7292) | 7292 | `"    provider_usage = _normalized_provider_usage("` | — |
| [SRC-1AE03B9EC3-L007293](../../agents/web_agent.py#L7293) | 7293 | `"        response_data.get(\"usage\"), provider_base_url=provider_base_url"` | — |
| [SRC-1AE03B9EC3-L007294](../../agents/web_agent.py#L7294) | 7294 | `"    )"` | — |
| [SRC-1AE03B9EC3-L007295](../../agents/web_agent.py#L7295) | 7295 | `"    if provider_usage is not None:"` | — |
| [SRC-1AE03B9EC3-L007296](../../agents/web_agent.py#L7296) | 7296 | `"        record[\"provider_usage\"] = provider_usage"` | — |
| [SRC-1AE03B9EC3-L007297](../../agents/web_agent.py#L7297) | 7297 | `"    return record"` | — |
## واجهات API

### FILE-D8438CDB65 — [api/__init__.py](../../api/__init__.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-D8438CDB65-L000001](../../api/__init__.py#L1) | 1 | `"\"\"\"Omarai local API package.\"\"\""` | — |
## واجهات API

### FILE-EEF2E6447C — [api/omarai.py](../../api/omarai.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-EEF2E6447C-L000001](../../api/omarai.py#L1) | 1 | `"\"\"\"HTTP API for Omarai's web-research agent and lead workspace.\"\"\""` | — |
| [SRC-EEF2E6447C-L000002](../../api/omarai.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-EEF2E6447C-L000003](../../api/omarai.py#L3) | 3 | `""` | — |
| [SRC-EEF2E6447C-L000004](../../api/omarai.py#L4) | 4 | `"import base64"` | — |
| [SRC-EEF2E6447C-L000005](../../api/omarai.py#L5) | 5 | `"import hashlib"` | — |
| [SRC-EEF2E6447C-L000006](../../api/omarai.py#L6) | 6 | `"import hmac"` | — |
| [SRC-EEF2E6447C-L000007](../../api/omarai.py#L7) | 7 | `"import ipaddress"` | — |
| [SRC-EEF2E6447C-L000008](../../api/omarai.py#L8) | 8 | `"import json"` | — |
| [SRC-EEF2E6447C-L000009](../../api/omarai.py#L9) | 9 | `"import os"` | — |
| [SRC-EEF2E6447C-L000010](../../api/omarai.py#L10) | 10 | `"import re"` | — |
| [SRC-EEF2E6447C-L000011](../../api/omarai.py#L11) | 11 | `"import threading"` | — |
| [SRC-EEF2E6447C-L000012](../../api/omarai.py#L12) | 12 | `"import time"` | — |
| [SRC-EEF2E6447C-L000013](../../api/omarai.py#L13) | 13 | `"from collections import defaultdict, deque"` | — |
| [SRC-EEF2E6447C-L000014](../../api/omarai.py#L14) | 14 | `"from functools import lru_cache"` | — |
| [SRC-EEF2E6447C-L000015](../../api/omarai.py#L15) | 15 | `"from http.cookies import SimpleCookie"` | — |
| [SRC-EEF2E6447C-L000016](../../api/omarai.py#L16) | 16 | `"from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer"` | — |
| [SRC-EEF2E6447C-L000017](../../api/omarai.py#L17) | 17 | `"from pathlib import Path"` | — |
| [SRC-EEF2E6447C-L000018](../../api/omarai.py#L18) | 18 | `"from typing import ClassVar"` | — |
| [SRC-EEF2E6447C-L000019](../../api/omarai.py#L19) | 19 | `"from urllib.parse import parse_qs, urlparse"` | — |
| [SRC-EEF2E6447C-L000020](../../api/omarai.py#L20) | 20 | `""` | — |
| [SRC-EEF2E6447C-L000021](../../api/omarai.py#L21) | 21 | `"from agents.omarai import LeadStore, analyze, normalize"` | — |
| [SRC-EEF2E6447C-L000022](../../api/omarai.py#L22) | 22 | `"from agents.sales_domain import MarketProfile, ProductProfile, build_buyer_queries"` | — |
| [SRC-EEF2E6447C-L000023](../../api/omarai.py#L23) | 23 | `"from agents.web_agent import WebAgent"` | — |
| [SRC-EEF2E6447C-L000024](../../api/omarai.py#L24) | 24 | `""` | — |
| [SRC-EEF2E6447C-L000025](../../api/omarai.py#L25) | 25 | `"ROOT = Path(__file__).resolve().parents[1] / \"web\""` | — |
| [SRC-EEF2E6447C-L000026](../../api/omarai.py#L26) | 26 | `"AGENT_DASHBOARD = ROOT / \"agent.html\""` | — |
| [SRC-EEF2E6447C-L000027](../../api/omarai.py#L27) | 27 | `"LEADS_DASHBOARD = ROOT / \"dashboard.html\""` | — |
| [SRC-EEF2E6447C-L000028](../../api/omarai.py#L28) | 28 | `"WORKSPACE_DASHBOARD = ROOT / \"workspace.html\""` | — |
| [SRC-EEF2E6447C-L000029](../../api/omarai.py#L29) | 29 | `"MAX_REQUEST_BODY_BYTES = 200_000"` | — |
| [SRC-EEF2E6447C-L000030](../../api/omarai.py#L30) | 30 | `"BROWSER_SESSION_COOKIE_MAX_AGE = 8 * 60 * 60"` | — |
| [SRC-EEF2E6447C-L000031](../../api/omarai.py#L31) | 31 | `"BROWSER_SESSION_ID_RE = re.compile(r\"^[A-Za-z0-9_-]{32,128}$\")"` | — |
| [SRC-EEF2E6447C-L000032](../../api/omarai.py#L32) | 32 | `""` | — |
| [SRC-EEF2E6447C-L000033](../../api/omarai.py#L33) | 33 | `""` | — |
| [SRC-EEF2E6447C-L000034](../../api/omarai.py#L34) | 34 | `"def _csp_hash_source(value: str) -> str:"` | — |
| [SRC-EEF2E6447C-L000035](../../api/omarai.py#L35) | 35 | `"    digest = base64.b64encode(hashlib.sha256(value.encode(\"utf-8\")).digest()).decode(\"ascii\")"` | — |
| [SRC-EEF2E6447C-L000036](../../api/omarai.py#L36) | 36 | `"    return f\"'sha256-{digest}'\""` | — |
| [SRC-EEF2E6447C-L000037](../../api/omarai.py#L37) | 37 | `""` | — |
| [SRC-EEF2E6447C-L000038](../../api/omarai.py#L38) | 38 | `""` | — |
| [SRC-EEF2E6447C-L000039](../../api/omarai.py#L39) | 39 | `"@lru_cache(maxsize=1)"` | — |
| [SRC-EEF2E6447C-L000040](../../api/omarai.py#L40) | 40 | `"def _content_security_policy() -> str:"` | — |
| [SRC-EEF2E6447C-L000041](../../api/omarai.py#L41) | 41 | `"    \"\"\"Allow only known inline blocks/attributes from the static first-party HTML."` | — |
| [SRC-EEF2E6447C-L000042](../../api/omarai.py#L42) | 42 | `""` | — |
| [SRC-EEF2E6447C-L000043](../../api/omarai.py#L43) | 43 | `"    Hashes deliberately replace unsafe-inline. Updating an inline script/style means its"` | — |
| [SRC-EEF2E6447C-L000044](../../api/omarai.py#L44) | 44 | `"    hash changes automatically with the served source. This is not a sanitizer for"` | — |
| [SRC-EEF2E6447C-L000045](../../api/omarai.py#L45) | 45 | `"    untrusted HTML; callers must never splice untrusted input into these static files."` | — |
| [SRC-EEF2E6447C-L000046](../../api/omarai.py#L46) | 46 | `"    \"\"\""` | — |
| [SRC-EEF2E6447C-L000047](../../api/omarai.py#L47) | 47 | `"    script_hashes: set[str] = set()"` | — |
| [SRC-EEF2E6447C-L000048](../../api/omarai.py#L48) | 48 | `"    style_hashes: set[str] = set()"` | — |
| [SRC-EEF2E6447C-L000049](../../api/omarai.py#L49) | 49 | `"    event_handler_hashes: set[str] = set()"` | — |
| [SRC-EEF2E6447C-L000050](../../api/omarai.py#L50) | 50 | `"    style_attribute_hashes: set[str] = set()"` | — |
| [SRC-EEF2E6447C-L000051](../../api/omarai.py#L51) | 51 | `""` | — |
| [SRC-EEF2E6447C-L000052](../../api/omarai.py#L52) | 52 | `"    for html_path in sorted(ROOT.glob(\"*.html\")):"` | — |
| [SRC-EEF2E6447C-L000053](../../api/omarai.py#L53) | 53 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000054](../../api/omarai.py#L54) | 54 | `"            document = html_path.read_text(encoding=\"utf-8\")"` | — |
| [SRC-EEF2E6447C-L000055](../../api/omarai.py#L55) | 55 | `"        except (OSError, UnicodeError):"` | — |
| [SRC-EEF2E6447C-L000056](../../api/omarai.py#L56) | 56 | `"            continue"` | — |
| [SRC-EEF2E6447C-L000057](../../api/omarai.py#L57) | 57 | `""` | — |
| [SRC-EEF2E6447C-L000058](../../api/omarai.py#L58) | 58 | `"        for match in re.finditer("` | — |
| [SRC-EEF2E6447C-L000059](../../api/omarai.py#L59) | 59 | `"            r\"<script\\b(?P<attrs>[^>]*)>(?P<body>.*?)</script\\s*>\","` | — |
| [SRC-EEF2E6447C-L000060](../../api/omarai.py#L60) | 60 | `"            document,"` | — |
| [SRC-EEF2E6447C-L000061](../../api/omarai.py#L61) | 61 | `"            re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-EEF2E6447C-L000062](../../api/omarai.py#L62) | 62 | `"        ):"` | — |
| [SRC-EEF2E6447C-L000063](../../api/omarai.py#L63) | 63 | `"            if re.search(r\"\\bsrc\\s*=\", match.group(\"attrs\"), re.IGNORECASE):"` | — |
| [SRC-EEF2E6447C-L000064](../../api/omarai.py#L64) | 64 | `"                continue"` | — |
| [SRC-EEF2E6447C-L000065](../../api/omarai.py#L65) | 65 | `"            script_hashes.add(_csp_hash_source(match.group(\"body\")))"` | — |
| [SRC-EEF2E6447C-L000066](../../api/omarai.py#L66) | 66 | `""` | — |
| [SRC-EEF2E6447C-L000067](../../api/omarai.py#L67) | 67 | `"        for match in re.finditer("` | — |
| [SRC-EEF2E6447C-L000068](../../api/omarai.py#L68) | 68 | `"            r\"<style\\b[^>]*>(?P<body>.*?)</style\\s*>\","` | — |
| [SRC-EEF2E6447C-L000069](../../api/omarai.py#L69) | 69 | `"            document,"` | — |
| [SRC-EEF2E6447C-L000070](../../api/omarai.py#L70) | 70 | `"            re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-EEF2E6447C-L000071](../../api/omarai.py#L71) | 71 | `"        ):"` | — |
| [SRC-EEF2E6447C-L000072](../../api/omarai.py#L72) | 72 | `"            style_hashes.add(_csp_hash_source(match.group(\"body\")))"` | — |
| [SRC-EEF2E6447C-L000073](../../api/omarai.py#L73) | 73 | `""` | — |
| [SRC-EEF2E6447C-L000074](../../api/omarai.py#L74) | 74 | `"        # This scan intentionally includes style/event attributes embedded in"` | — |
| [SRC-EEF2E6447C-L000075](../../api/omarai.py#L75) | 75 | `"        # trusted first-party HTML templates assembled by inline scripts."` | — |
| [SRC-EEF2E6447C-L000076](../../api/omarai.py#L76) | 76 | `"        for match in re.finditer("` | — |
| [SRC-EEF2E6447C-L000077](../../api/omarai.py#L77) | 77 | `"            r\"\"\"\\bstyle\\s*=\\s*([\"'])(.*?)\\1\"\"\","` | — |
| [SRC-EEF2E6447C-L000078](../../api/omarai.py#L78) | 78 | `"            document,"` | — |
| [SRC-EEF2E6447C-L000079](../../api/omarai.py#L79) | 79 | `"            re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-EEF2E6447C-L000080](../../api/omarai.py#L80) | 80 | `"        ):"` | — |
| [SRC-EEF2E6447C-L000081](../../api/omarai.py#L81) | 81 | `"            style_attribute_hashes.add(_csp_hash_source(match.group(2).strip()))"` | — |
| [SRC-EEF2E6447C-L000082](../../api/omarai.py#L82) | 82 | `""` | — |
| [SRC-EEF2E6447C-L000083](../../api/omarai.py#L83) | 83 | `"        for match in re.finditer("` | — |
| [SRC-EEF2E6447C-L000084](../../api/omarai.py#L84) | 84 | `"            r\"\"\"\\bon[a-z]+\\s*=\\s*([\"'])(.*?)\\1\"\"\","` | — |
| [SRC-EEF2E6447C-L000085](../../api/omarai.py#L85) | 85 | `"            document,"` | — |
| [SRC-EEF2E6447C-L000086](../../api/omarai.py#L86) | 86 | `"            re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-EEF2E6447C-L000087](../../api/omarai.py#L87) | 87 | `"        ):"` | — |
| [SRC-EEF2E6447C-L000088](../../api/omarai.py#L88) | 88 | `"            event_handler_hashes.add(_csp_hash_source(match.group(2).strip()))"` | — |
| [SRC-EEF2E6447C-L000089](../../api/omarai.py#L89) | 89 | `""` | — |
| [SRC-EEF2E6447C-L000090](../../api/omarai.py#L90) | 90 | `"    script_sources = [\"'self'\", *sorted(script_hashes)]"` | — |
| [SRC-EEF2E6447C-L000091](../../api/omarai.py#L91) | 91 | `"    style_sources = [\"'self'\", *sorted(style_hashes)]"` | — |
| [SRC-EEF2E6447C-L000092](../../api/omarai.py#L92) | 92 | `"    if event_handler_hashes:"` | — |
| [SRC-EEF2E6447C-L000093](../../api/omarai.py#L93) | 93 | `"        script_sources.extend([\"'unsafe-hashes'\", *sorted(event_handler_hashes)])"` | — |
| [SRC-EEF2E6447C-L000094](../../api/omarai.py#L94) | 94 | `"    if style_attribute_hashes:"` | — |
| [SRC-EEF2E6447C-L000095](../../api/omarai.py#L95) | 95 | `"        style_sources.extend([\"'unsafe-hashes'\", *sorted(style_attribute_hashes)])"` | — |
| [SRC-EEF2E6447C-L000096](../../api/omarai.py#L96) | 96 | `""` | — |
| [SRC-EEF2E6447C-L000097](../../api/omarai.py#L97) | 97 | `"    return ("` | — |
| [SRC-EEF2E6447C-L000098](../../api/omarai.py#L98) | 98 | `"        \"default-src 'self'; base-uri 'self'; object-src 'none'; frame-ancestors 'none'; \""` | — |
| [SRC-EEF2E6447C-L000099](../../api/omarai.py#L99) | 99 | `"        \"form-action 'self'; connect-src 'self'; img-src 'self' data:; \""` | — |
| [SRC-EEF2E6447C-L000100](../../api/omarai.py#L100) | 100 | `"        f\"script-src {' '.join(script_sources)}; \""` | — |
| [SRC-EEF2E6447C-L000101](../../api/omarai.py#L101) | 101 | `"        f\"style-src {' '.join(style_sources)}; font-src 'self' data:\""` | — |
| [SRC-EEF2E6447C-L000102](../../api/omarai.py#L102) | 102 | `"    )"` | — |
| [SRC-EEF2E6447C-L000103](../../api/omarai.py#L103) | 103 | `"# Bound request-line + header parsing before application code or body processing."` | — |
| [SRC-EEF2E6447C-L000104](../../api/omarai.py#L104) | 104 | `"REQUEST_HEADER_READ_TIMEOUT_SECONDS = 8.0"` | — |
| [SRC-EEF2E6447C-L000105](../../api/omarai.py#L105) | 105 | `"REQUEST_HEADER_IDLE_TIMEOUT_SECONDS = 2.0"` | — |
| [SRC-EEF2E6447C-L000106](../../api/omarai.py#L106) | 106 | `"MAX_REQUEST_HEADER_READ_TIMEOUT_SECONDS = 15.0"` | — |
| [SRC-EEF2E6447C-L000107](../../api/omarai.py#L107) | 107 | `"# Absolute deadline for reading the entire body, not merely a per-read idle timeout."` | — |
| [SRC-EEF2E6447C-L000108](../../api/omarai.py#L108) | 108 | `"REQUEST_BODY_READ_TIMEOUT_SECONDS = 10.0"` | — |
| [SRC-EEF2E6447C-L000109](../../api/omarai.py#L109) | 109 | `"REQUEST_BODY_IDLE_TIMEOUT_SECONDS = 2.0"` | — |
| [SRC-EEF2E6447C-L000110](../../api/omarai.py#L110) | 110 | `"MAX_REQUEST_BODY_READ_TIMEOUT_SECONDS = 30.0"` | — |
| [SRC-EEF2E6447C-L000111](../../api/omarai.py#L111) | 111 | `"REQUEST_BODY_READ_CHUNK_BYTES = 8_192"` | — |
| [SRC-EEF2E6447C-L000112](../../api/omarai.py#L112) | 112 | `""` | — |
| [SRC-EEF2E6447C-L000113](../../api/omarai.py#L113) | 113 | `""` | — |
| [SRC-EEF2E6447C-L000114](../../api/omarai.py#L114) | 114 | `""` | — |
| [SRC-EEF2E6447C-L000115](../../api/omarai.py#L115) | 115 | `"def _lead_store_from_environment() -> LeadStore:"` | — |
| [SRC-EEF2E6447C-L000116](../../api/omarai.py#L116) | 116 | `"    \"\"\"Use an operator-configured database path when a persistent volume is available.\"\"\""` | — |
| [SRC-EEF2E6447C-L000117](../../api/omarai.py#L117) | 117 | `"    configured_path = os.getenv(\"OMARAI_DB_PATH\", \"\").strip()"` | — |
| [SRC-EEF2E6447C-L000118](../../api/omarai.py#L118) | 118 | `"    return LeadStore(configured_path or None)"` | — |
| [SRC-EEF2E6447C-L000119](../../api/omarai.py#L119) | 119 | `""` | — |
| [SRC-EEF2E6447C-L000120](../../api/omarai.py#L120) | 120 | `""` | — |
| [SRC-EEF2E6447C-L000121](../../api/omarai.py#L121) | 121 | `"def _profile_terms(value, field_name: str) -> tuple[str, ...]:"` | — |
| [SRC-EEF2E6447C-L000122](../../api/omarai.py#L122) | 122 | `"    \"\"\"Validate bounded ProductProfile/MarketProfile string arrays.\"\"\""` | — |
| [SRC-EEF2E6447C-L000123](../../api/omarai.py#L123) | 123 | `"    if value is None:"` | — |
| [SRC-EEF2E6447C-L000124](../../api/omarai.py#L124) | 124 | `"        return ()"` | — |
| [SRC-EEF2E6447C-L000125](../../api/omarai.py#L125) | 125 | `"    if not isinstance(value, list) or len(value) > 40:"` | — |
| [SRC-EEF2E6447C-L000126](../../api/omarai.py#L126) | 126 | `"        raise ValueError(f\"{field_name} must be a list of at most 40 strings\")"` | — |
| [SRC-EEF2E6447C-L000127](../../api/omarai.py#L127) | 127 | `"    if any(not isinstance(item, str) or len(item) > 240 for item in value):"` | — |
| [SRC-EEF2E6447C-L000128](../../api/omarai.py#L128) | 128 | `"        raise ValueError(f\"{field_name} items must be strings of at most 240 characters\")"` | — |
| [SRC-EEF2E6447C-L000129](../../api/omarai.py#L129) | 129 | `"    return tuple(value)"` | — |
| [SRC-EEF2E6447C-L000130](../../api/omarai.py#L130) | 130 | `""` | — |
| [SRC-EEF2E6447C-L000131](../../api/omarai.py#L131) | 131 | `""` | — |
| [SRC-EEF2E6447C-L000132](../../api/omarai.py#L132) | 132 | `"def _product_market_from_payload(data: dict):"` | — |
| [SRC-EEF2E6447C-L000133](../../api/omarai.py#L133) | 133 | `"    product_data = data.get(\"product\")"` | — |
| [SRC-EEF2E6447C-L000134](../../api/omarai.py#L134) | 134 | `"    market_data = data.get(\"market\")"` | — |
| [SRC-EEF2E6447C-L000135](../../api/omarai.py#L135) | 135 | `"    if not isinstance(product_data, dict) or not isinstance(market_data, dict):"` | — |
| [SRC-EEF2E6447C-L000136](../../api/omarai.py#L136) | 136 | `"        raise TypeError(\"product and market objects are required\")"` | — |
| [SRC-EEF2E6447C-L000137](../../api/omarai.py#L137) | 137 | `"    product = ProductProfile("` | — |
| [SRC-EEF2E6447C-L000138](../../api/omarai.py#L138) | 138 | `"        name=product_data.get(\"name\", \"\"),"` | — |
| [SRC-EEF2E6447C-L000139](../../api/omarai.py#L139) | 139 | `"        aliases=_profile_terms(product_data.get(\"aliases\"), \"aliases\"),"` | — |
| [SRC-EEF2E6447C-L000140](../../api/omarai.py#L140) | 140 | `"        category_path=_profile_terms(product_data.get(\"category_path\"), \"category_path\"),"` | — |
| [SRC-EEF2E6447C-L000141](../../api/omarai.py#L141) | 141 | `"        use_cases=_profile_terms(product_data.get(\"use_cases\"), \"use_cases\"),"` | — |
| [SRC-EEF2E6447C-L000142](../../api/omarai.py#L142) | 142 | `"        problems_solved=_profile_terms(product_data.get(\"problems_solved\"), \"problems_solved\"),"` | — |
| [SRC-EEF2E6447C-L000143](../../api/omarai.py#L143) | 143 | `"    )"` | — |
| [SRC-EEF2E6447C-L000144](../../api/omarai.py#L144) | 144 | `"    market = MarketProfile("` | — |
| [SRC-EEF2E6447C-L000145](../../api/omarai.py#L145) | 145 | `"        locations=_profile_terms(market_data.get(\"locations\"), \"locations\"),"` | — |
| [SRC-EEF2E6447C-L000146](../../api/omarai.py#L146) | 146 | `"        industries=_profile_terms(market_data.get(\"industries\"), \"industries\"),"` | — |
| [SRC-EEF2E6447C-L000147](../../api/omarai.py#L147) | 147 | `"        customer_types=_profile_terms(market_data.get(\"customer_types\"), \"customer_types\"),"` | — |
| [SRC-EEF2E6447C-L000148](../../api/omarai.py#L148) | 148 | `"        decision_roles=_profile_terms(market_data.get(\"decision_roles\"), \"decision_roles\"),"` | — |
| [SRC-EEF2E6447C-L000149](../../api/omarai.py#L149) | 149 | `"        exclusions=_profile_terms(market_data.get(\"exclusions\"), \"exclusions\"),"` | — |
| [SRC-EEF2E6447C-L000150](../../api/omarai.py#L150) | 150 | `"    )"` | — |
| [SRC-EEF2E6447C-L000151](../../api/omarai.py#L151) | 151 | `"    locale = data.get(\"locale\", \"auto\")"` | — |
| [SRC-EEF2E6447C-L000152](../../api/omarai.py#L152) | 152 | `"    if not isinstance(locale, str) or locale not in {\"auto\", \"ar\", \"en\", \"mixed\"}:"` | — |
| [SRC-EEF2E6447C-L000153](../../api/omarai.py#L153) | 153 | `"        raise ValueError(\"locale must be auto, ar, en, or mixed\")"` | — |
| [SRC-EEF2E6447C-L000154](../../api/omarai.py#L154) | 154 | `"    return product, market, locale"` | — |
| [SRC-EEF2E6447C-L000155](../../api/omarai.py#L155) | 155 | `""` | — |
| [SRC-EEF2E6447C-L000156](../../api/omarai.py#L156) | 156 | `""` | — |
| [SRC-EEF2E6447C-L000157](../../api/omarai.py#L157) | 157 | `"class _DeadlineRequestReader:"` | — |
| [SRC-EEF2E6447C-L000158](../../api/omarai.py#L158) | 158 | `"    \"\"\"Read HTTP header lines with one absolute deadline across all fragments."` | — |
| [SRC-EEF2E6447C-L000159](../../api/omarai.py#L159) | 159 | `""` | — |
| [SRC-EEF2E6447C-L000160](../../api/omarai.py#L160) | 160 | `"    The standard buffered readline can wait indefinitely for a newline if a"` | — |
| [SRC-EEF2E6447C-L000161](../../api/omarai.py#L161) | 161 | `"    client keeps trickling bytes. This reader checks the same deadline before"` | — |
| [SRC-EEF2E6447C-L000162](../../api/omarai.py#L162) | 162 | `"    every socket read and buffers only bounded look-ahead so request body bytes"` | — |
| [SRC-EEF2E6447C-L000163](../../api/omarai.py#L163) | 163 | `"    received with the headers are preserved for read1()."` | — |
| [SRC-EEF2E6447C-L000164](../../api/omarai.py#L164) | 164 | `"    \"\"\""` | — |
| [SRC-EEF2E6447C-L000165](../../api/omarai.py#L165) | 165 | `""` | — |
| [SRC-EEF2E6447C-L000166](../../api/omarai.py#L166) | 166 | `"    def __init__(self, connection, handler):"` | — |
| [SRC-EEF2E6447C-L000167](../../api/omarai.py#L167) | 167 | `"        self.connection = connection"` | — |
| [SRC-EEF2E6447C-L000168](../../api/omarai.py#L168) | 168 | `"        self.handler = handler"` | — |
| [SRC-EEF2E6447C-L000169](../../api/omarai.py#L169) | 169 | `"        self._buffer = bytearray()"` | — |
| [SRC-EEF2E6447C-L000170](../../api/omarai.py#L170) | 170 | `""` | — |
| [SRC-EEF2E6447C-L000171](../../api/omarai.py#L171) | 171 | `"    def readline(self, limit=-1):"` | — |
| [SRC-EEF2E6447C-L000172](../../api/omarai.py#L172) | 172 | `"        if limit == 0:"` | — |
| [SRC-EEF2E6447C-L000173](../../api/omarai.py#L173) | 173 | `"            return b\"\""` | — |
| [SRC-EEF2E6447C-L000174](../../api/omarai.py#L174) | 174 | `"        max_bytes = int(limit) if limit is not None and limit > 0 else 65_537"` | — |
| [SRC-EEF2E6447C-L000175](../../api/omarai.py#L175) | 175 | `"        previous_timeout = self.connection.gettimeout()"` | — |
| [SRC-EEF2E6447C-L000176](../../api/omarai.py#L176) | 176 | `"        line = bytearray()"` | — |
| [SRC-EEF2E6447C-L000177](../../api/omarai.py#L177) | 177 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000178](../../api/omarai.py#L178) | 178 | `"            while len(line) < max_bytes:"` | — |
| [SRC-EEF2E6447C-L000179](../../api/omarai.py#L179) | 179 | `"                deadline = getattr(self.handler, \"_request_header_deadline\", None)"` | — |
| [SRC-EEF2E6447C-L000180](../../api/omarai.py#L180) | 180 | `"                if deadline is None:"` | — |
| [SRC-EEF2E6447C-L000181](../../api/omarai.py#L181) | 181 | `"                    raise TimeoutError(\"request-header deadline is not active\")"` | — |
| [SRC-EEF2E6447C-L000182](../../api/omarai.py#L182) | 182 | `"                remaining = deadline - time.monotonic()"` | — |
| [SRC-EEF2E6447C-L000183](../../api/omarai.py#L183) | 183 | `"                if remaining <= 0:"` | — |
| [SRC-EEF2E6447C-L000184](../../api/omarai.py#L184) | 184 | `"                    raise TimeoutError(\"absolute request-header deadline exceeded\")"` | — |
| [SRC-EEF2E6447C-L000185](../../api/omarai.py#L185) | 185 | `""` | — |
| [SRC-EEF2E6447C-L000186](../../api/omarai.py#L186) | 186 | `"                newline_index = self._buffer.find(b\"\\n\")"` | — |
| [SRC-EEF2E6447C-L000187](../../api/omarai.py#L187) | 187 | `"                if newline_index >= 0:"` | — |
| [SRC-EEF2E6447C-L000188](../../api/omarai.py#L188) | 188 | `"                    take = min(newline_index + 1, max_bytes - len(line))"` | — |
| [SRC-EEF2E6447C-L000189](../../api/omarai.py#L189) | 189 | `"                    line.extend(self._buffer[:take])"` | — |
| [SRC-EEF2E6447C-L000190](../../api/omarai.py#L190) | 190 | `"                    del self._buffer[:take]"` | — |
| [SRC-EEF2E6447C-L000191](../../api/omarai.py#L191) | 191 | `"                    break"` | — |
| [SRC-EEF2E6447C-L000192](../../api/omarai.py#L192) | 192 | `""` | — |
| [SRC-EEF2E6447C-L000193](../../api/omarai.py#L193) | 193 | `"                if self._buffer:"` | — |
| [SRC-EEF2E6447C-L000194](../../api/omarai.py#L194) | 194 | `"                    take = min(len(self._buffer), max_bytes - len(line))"` | — |
| [SRC-EEF2E6447C-L000195](../../api/omarai.py#L195) | 195 | `"                    line.extend(self._buffer[:take])"` | — |
| [SRC-EEF2E6447C-L000196](../../api/omarai.py#L196) | 196 | `"                    del self._buffer[:take]"` | — |
| [SRC-EEF2E6447C-L000197](../../api/omarai.py#L197) | 197 | `"                    if len(line) >= max_bytes:"` | — |
| [SRC-EEF2E6447C-L000198](../../api/omarai.py#L198) | 198 | `"                        break"` | — |
| [SRC-EEF2E6447C-L000199](../../api/omarai.py#L199) | 199 | `""` | — |
| [SRC-EEF2E6447C-L000200](../../api/omarai.py#L200) | 200 | `"                remaining = deadline - time.monotonic()"` | — |
| [SRC-EEF2E6447C-L000201](../../api/omarai.py#L201) | 201 | `"                if remaining <= 0:"` | — |
| [SRC-EEF2E6447C-L000202](../../api/omarai.py#L202) | 202 | `"                    raise TimeoutError(\"absolute request-header deadline exceeded\")"` | — |
| [SRC-EEF2E6447C-L000203](../../api/omarai.py#L203) | 203 | `"                idle_timeout = max("` | — |
| [SRC-EEF2E6447C-L000204](../../api/omarai.py#L204) | 204 | `"                    0.1,"` | — |
| [SRC-EEF2E6447C-L000205](../../api/omarai.py#L205) | 205 | `"                    min("` | — |
| [SRC-EEF2E6447C-L000206](../../api/omarai.py#L206) | 206 | `"                        float(REQUEST_HEADER_IDLE_TIMEOUT_SECONDS),"` | — |
| [SRC-EEF2E6447C-L000207](../../api/omarai.py#L207) | 207 | `"                        MAX_REQUEST_HEADER_READ_TIMEOUT_SECONDS,"` | — |
| [SRC-EEF2E6447C-L000208](../../api/omarai.py#L208) | 208 | `"                    ),"` | — |
| [SRC-EEF2E6447C-L000209](../../api/omarai.py#L209) | 209 | `"                )"` | — |
| [SRC-EEF2E6447C-L000210](../../api/omarai.py#L210) | 210 | `"                self.connection.settimeout(min(idle_timeout, remaining))"` | — |
| [SRC-EEF2E6447C-L000211](../../api/omarai.py#L211) | 211 | `"                chunk = self.connection.recv(min(4_096, max_bytes - len(line)))"` | — |
| [SRC-EEF2E6447C-L000212](../../api/omarai.py#L212) | 212 | `"                if not chunk:"` | — |
| [SRC-EEF2E6447C-L000213](../../api/omarai.py#L213) | 213 | `"                    break"` | — |
| [SRC-EEF2E6447C-L000214](../../api/omarai.py#L214) | 214 | `"                self._buffer.extend(chunk)"` | — |
| [SRC-EEF2E6447C-L000215](../../api/omarai.py#L215) | 215 | `"        finally:"` | — |
| [SRC-EEF2E6447C-L000216](../../api/omarai.py#L216) | 216 | `"            try:"` | — |
| [SRC-EEF2E6447C-L000217](../../api/omarai.py#L217) | 217 | `"                self.connection.settimeout(previous_timeout)"` | — |
| [SRC-EEF2E6447C-L000218](../../api/omarai.py#L218) | 218 | `"            except OSError:"` | — |
| [SRC-EEF2E6447C-L000219](../../api/omarai.py#L219) | 219 | `"                pass"` | — |
| [SRC-EEF2E6447C-L000220](../../api/omarai.py#L220) | 220 | `"        return bytes(line)"` | — |
| [SRC-EEF2E6447C-L000221](../../api/omarai.py#L221) | 221 | `""` | — |
| [SRC-EEF2E6447C-L000222](../../api/omarai.py#L222) | 222 | `"    def read1(self, size=-1):"` | — |
| [SRC-EEF2E6447C-L000223](../../api/omarai.py#L223) | 223 | `"        \"\"\"Read one chunk; body code applies its own idle and absolute deadlines.\"\"\""` | — |
| [SRC-EEF2E6447C-L000224](../../api/omarai.py#L224) | 224 | `"        if size == 0:"` | — |
| [SRC-EEF2E6447C-L000225](../../api/omarai.py#L225) | 225 | `"            return b\"\""` | — |
| [SRC-EEF2E6447C-L000226](../../api/omarai.py#L226) | 226 | `"        if size is None or size < 0:"` | — |
| [SRC-EEF2E6447C-L000227](../../api/omarai.py#L227) | 227 | `"            size = 8_192"` | — |
| [SRC-EEF2E6447C-L000228](../../api/omarai.py#L228) | 228 | `"        if self._buffer:"` | — |
| [SRC-EEF2E6447C-L000229](../../api/omarai.py#L229) | 229 | `"            take = min(len(self._buffer), size)"` | — |
| [SRC-EEF2E6447C-L000230](../../api/omarai.py#L230) | 230 | `"            data = bytes(self._buffer[:take])"` | — |
| [SRC-EEF2E6447C-L000231](../../api/omarai.py#L231) | 231 | `"            del self._buffer[:take]"` | — |
| [SRC-EEF2E6447C-L000232](../../api/omarai.py#L232) | 232 | `"            return data"` | — |
| [SRC-EEF2E6447C-L000233](../../api/omarai.py#L233) | 233 | `"        return self.connection.recv(size)"` | — |
| [SRC-EEF2E6447C-L000234](../../api/omarai.py#L234) | 234 | `""` | — |
| [SRC-EEF2E6447C-L000235](../../api/omarai.py#L235) | 235 | `"    def close(self):"` | — |
| [SRC-EEF2E6447C-L000236](../../api/omarai.py#L236) | 236 | `"        # The request handler owns the socket and closes its output stream."` | — |
| [SRC-EEF2E6447C-L000237](../../api/omarai.py#L237) | 237 | `"        return None"` | — |
| [SRC-EEF2E6447C-L000238](../../api/omarai.py#L238) | 238 | `""` | — |
| [SRC-EEF2E6447C-L000239](../../api/omarai.py#L239) | 239 | `""` | — |
| [SRC-EEF2E6447C-L000240](../../api/omarai.py#L240) | 240 | `"def _configured_agent_concurrency_limit() -> int:"` | — |
| [SRC-EEF2E6447C-L000241](../../api/omarai.py#L241) | 241 | `"    \"\"\"Return a process-local cap for expensive research and diagnostics operations.\"\"\""` | — |
| [SRC-EEF2E6447C-L000242](../../api/omarai.py#L242) | 242 | `"    try:"` | — |
| [SRC-EEF2E6447C-L000243](../../api/omarai.py#L243) | 243 | `"        configured = int(os.getenv(\"OMARAI_MAX_CONCURRENT_AGENT_REQUESTS\", \"4\").strip())"` | — |
| [SRC-EEF2E6447C-L000244](../../api/omarai.py#L244) | 244 | `"    except ValueError:"` | — |
| [SRC-EEF2E6447C-L000245](../../api/omarai.py#L245) | 245 | `"        configured = 4"` | — |
| [SRC-EEF2E6447C-L000246](../../api/omarai.py#L246) | 246 | `"    return max(1, min(configured, 8))"` | — |
| [SRC-EEF2E6447C-L000247](../../api/omarai.py#L247) | 247 | `""` | — |
| [SRC-EEF2E6447C-L000248](../../api/omarai.py#L248) | 248 | `""` | — |
| [SRC-EEF2E6447C-L000249](../../api/omarai.py#L249) | 249 | `"DEFAULT_HTTP_CONNECTION_LIMIT = 32"` | — |
| [SRC-EEF2E6447C-L000250](../../api/omarai.py#L250) | 250 | `"MAX_HTTP_CONNECTION_LIMIT = 128"` | — |
| [SRC-EEF2E6447C-L000251](../../api/omarai.py#L251) | 251 | `""` | — |
| [SRC-EEF2E6447C-L000252](../../api/omarai.py#L252) | 252 | `""` | — |
| [SRC-EEF2E6447C-L000253](../../api/omarai.py#L253) | 253 | `"def _configured_http_connection_limit() -> int:"` | — |
| [SRC-EEF2E6447C-L000254](../../api/omarai.py#L254) | 254 | `"    \"\"\"Return the bounded number of live HTTP handler threads for this process.\"\"\""` | — |
| [SRC-EEF2E6447C-L000255](../../api/omarai.py#L255) | 255 | `"    try:"` | — |
| [SRC-EEF2E6447C-L000256](../../api/omarai.py#L256) | 256 | `"        configured = int(os.getenv(\"OMARAI_MAX_CONCURRENT_HTTP_CONNECTIONS\", \"32\").strip())"` | — |
| [SRC-EEF2E6447C-L000257](../../api/omarai.py#L257) | 257 | `"    except ValueError:"` | — |
| [SRC-EEF2E6447C-L000258](../../api/omarai.py#L258) | 258 | `"        configured = DEFAULT_HTTP_CONNECTION_LIMIT"` | — |
| [SRC-EEF2E6447C-L000259](../../api/omarai.py#L259) | 259 | `"    return max(1, min(configured, MAX_HTTP_CONNECTION_LIMIT))"` | — |
| [SRC-EEF2E6447C-L000260](../../api/omarai.py#L260) | 260 | `""` | — |
| [SRC-EEF2E6447C-L000261](../../api/omarai.py#L261) | 261 | `""` | — |
| [SRC-EEF2E6447C-L000262](../../api/omarai.py#L262) | 262 | `"BUILD_SHA_FILE = Path(__file__).resolve().parents[1] / \"BUILD_SHA\""` | — |
| [SRC-EEF2E6447C-L000263](../../api/omarai.py#L263) | 263 | `"_PLATFORM_BUILD_SHA_ENVIRONMENTS = ("` | — |
| [SRC-EEF2E6447C-L000264](../../api/omarai.py#L264) | 264 | `"    (\"RAILWAY_GIT_COMMIT_SHA\", \"platform:railway\"),"` | — |
| [SRC-EEF2E6447C-L000265](../../api/omarai.py#L265) | 265 | `"    (\"RENDER_GIT_COMMIT\", \"platform:render\"),"` | — |
| [SRC-EEF2E6447C-L000266](../../api/omarai.py#L266) | 266 | `")"` | — |
| [SRC-EEF2E6447C-L000267](../../api/omarai.py#L267) | 267 | `""` | — |
| [SRC-EEF2E6447C-L000268](../../api/omarai.py#L268) | 268 | `""` | — |
| [SRC-EEF2E6447C-L000269](../../api/omarai.py#L269) | 269 | `"def _valid_build_sha(value: str) -> bool:"` | — |
| [SRC-EEF2E6447C-L000270](../../api/omarai.py#L270) | 270 | `"    candidate = value.strip().lower()"` | — |
| [SRC-EEF2E6447C-L000271](../../api/omarai.py#L271) | 271 | `"    return len(candidate) == 40 and all(char in \"0123456789abcdef\" for char in candidate)"` | — |
| [SRC-EEF2E6447C-L000272](../../api/omarai.py#L272) | 272 | `""` | — |
| [SRC-EEF2E6447C-L000273](../../api/omarai.py#L273) | 273 | `""` | — |
| [SRC-EEF2E6447C-L000274](../../api/omarai.py#L274) | 274 | `"def _build_identity() -> tuple[str, str]:"` | — |
| [SRC-EEF2E6447C-L000275](../../api/omarai.py#L275) | 275 | `"    \"\"\"Prefer immutable image metadata, then documented hosting-provided Git SHAs.\"\"\""` | — |
| [SRC-EEF2E6447C-L000276](../../api/omarai.py#L276) | 276 | `"    try:"` | — |
| [SRC-EEF2E6447C-L000277](../../api/omarai.py#L277) | 277 | `"        baked = BUILD_SHA_FILE.read_text(encoding=\"ascii\").strip().lower()"` | — |
| [SRC-EEF2E6447C-L000278](../../api/omarai.py#L278) | 278 | `"    except (OSError, UnicodeError):"` | — |
| [SRC-EEF2E6447C-L000279](../../api/omarai.py#L279) | 279 | `"        baked = \"\""` | — |
| [SRC-EEF2E6447C-L000280](../../api/omarai.py#L280) | 280 | `"    if _valid_build_sha(baked):"` | — |
| [SRC-EEF2E6447C-L000281](../../api/omarai.py#L281) | 281 | `"        return baked, \"image_baked\""` | — |
| [SRC-EEF2E6447C-L000282](../../api/omarai.py#L282) | 282 | `""` | — |
| [SRC-EEF2E6447C-L000283](../../api/omarai.py#L283) | 283 | `"    for environment_name, source in _PLATFORM_BUILD_SHA_ENVIRONMENTS:"` | — |
| [SRC-EEF2E6447C-L000284](../../api/omarai.py#L284) | 284 | `"        candidate = os.getenv(environment_name, \"\").strip().lower()"` | — |
| [SRC-EEF2E6447C-L000285](../../api/omarai.py#L285) | 285 | `"        if _valid_build_sha(candidate):"` | — |
| [SRC-EEF2E6447C-L000286](../../api/omarai.py#L286) | 286 | `"            return candidate, source"` | — |
| [SRC-EEF2E6447C-L000287](../../api/omarai.py#L287) | 287 | `"    return \"unknown\", \"unknown\""` | — |
| [SRC-EEF2E6447C-L000288](../../api/omarai.py#L288) | 288 | `""` | — |
| [SRC-EEF2E6447C-L000289](../../api/omarai.py#L289) | 289 | `""` | — |
| [SRC-EEF2E6447C-L000290](../../api/omarai.py#L290) | 290 | `"def _build_sha() -> str:"` | — |
| [SRC-EEF2E6447C-L000291](../../api/omarai.py#L291) | 291 | `"    \"\"\"Return a validated source SHA, or 'unknown' when no trusted build evidence exists.\"\"\""` | — |
| [SRC-EEF2E6447C-L000292](../../api/omarai.py#L292) | 292 | `"    return _build_identity()[0]"` | — |
| [SRC-EEF2E6447C-L000293](../../api/omarai.py#L293) | 293 | `""` | — |
| [SRC-EEF2E6447C-L000294](../../api/omarai.py#L294) | 294 | `""` | — |
| [SRC-EEF2E6447C-L000295](../../api/omarai.py#L295) | 295 | `"class Handler(BaseHTTPRequestHandler):"` | — |
| [SRC-EEF2E6447C-L000296](../../api/omarai.py#L296) | 296 | `"    def setup(self):"` | — |
| [SRC-EEF2E6447C-L000297](../../api/omarai.py#L297) | 297 | `"        \"\"\"Install a reader with a strict deadline for the request line and headers.\"\"\""` | — |
| [SRC-EEF2E6447C-L000298](../../api/omarai.py#L298) | 298 | `"        self.connection = self.request"` | — |
| [SRC-EEF2E6447C-L000299](../../api/omarai.py#L299) | 299 | `"        if self.timeout is not None:"` | — |
| [SRC-EEF2E6447C-L000300](../../api/omarai.py#L300) | 300 | `"            self.connection.settimeout(self.timeout)"` | — |
| [SRC-EEF2E6447C-L000301](../../api/omarai.py#L301) | 301 | `"        self._request_header_deadline = None"` | — |
| [SRC-EEF2E6447C-L000302](../../api/omarai.py#L302) | 302 | `"        self.rfile = _DeadlineRequestReader(self.connection, self)"` | — |
| [SRC-EEF2E6447C-L000303](../../api/omarai.py#L303) | 303 | `"        self.wfile = self.connection.makefile(\"wb\", self.wbufsize)"` | — |
| [SRC-EEF2E6447C-L000304](../../api/omarai.py#L304) | 304 | `""` | — |
| [SRC-EEF2E6447C-L000305](../../api/omarai.py#L305) | 305 | `"    def handle_one_request(self):"` | — |
| [SRC-EEF2E6447C-L000306](../../api/omarai.py#L306) | 306 | `"        timeout = max("` | — |
| [SRC-EEF2E6447C-L000307](../../api/omarai.py#L307) | 307 | `"            0.1,"` | — |
| [SRC-EEF2E6447C-L000308](../../api/omarai.py#L308) | 308 | `"            min("` | — |
| [SRC-EEF2E6447C-L000309](../../api/omarai.py#L309) | 309 | `"                float(REQUEST_HEADER_READ_TIMEOUT_SECONDS),"` | — |
| [SRC-EEF2E6447C-L000310](../../api/omarai.py#L310) | 310 | `"                MAX_REQUEST_HEADER_READ_TIMEOUT_SECONDS,"` | — |
| [SRC-EEF2E6447C-L000311](../../api/omarai.py#L311) | 311 | `"            ),"` | — |
| [SRC-EEF2E6447C-L000312](../../api/omarai.py#L312) | 312 | `"        )"` | — |
| [SRC-EEF2E6447C-L000313](../../api/omarai.py#L313) | 313 | `"        self._request_header_deadline = time.monotonic() + timeout"` | — |
| [SRC-EEF2E6447C-L000314](../../api/omarai.py#L314) | 314 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000315](../../api/omarai.py#L315) | 315 | `"            super().handle_one_request()"` | — |
| [SRC-EEF2E6447C-L000316](../../api/omarai.py#L316) | 316 | `"        except TimeoutError:"` | — |
| [SRC-EEF2E6447C-L000317](../../api/omarai.py#L317) | 317 | `"            # Incomplete request line/headers are untrusted protocol input;"` | — |
| [SRC-EEF2E6447C-L000318](../../api/omarai.py#L318) | 318 | `"            # close the socket without trying to parse or answer a partial request."` | — |
| [SRC-EEF2E6447C-L000319](../../api/omarai.py#L319) | 319 | `"            self.close_connection = True"` | — |
| [SRC-EEF2E6447C-L000320](../../api/omarai.py#L320) | 320 | `"        finally:"` | — |
| [SRC-EEF2E6447C-L000321](../../api/omarai.py#L321) | 321 | `"            self._request_header_deadline = None"` | — |
| [SRC-EEF2E6447C-L000322](../../api/omarai.py#L322) | 322 | `""` | — |
| [SRC-EEF2E6447C-L000323](../../api/omarai.py#L323) | 323 | `"    def parse_request(self):"` | — |
| [SRC-EEF2E6447C-L000324](../../api/omarai.py#L324) | 324 | `"        \"\"\"Reject ambiguous HTTP message framing before dispatching any handler.\"\"\""` | — |
| [SRC-EEF2E6447C-L000325](../../api/omarai.py#L325) | 325 | `"        if not super().parse_request():"` | — |
| [SRC-EEF2E6447C-L000326](../../api/omarai.py#L326) | 326 | `"            return False"` | — |
| [SRC-EEF2E6447C-L000327](../../api/omarai.py#L327) | 327 | `""` | — |
| [SRC-EEF2E6447C-L000328](../../api/omarai.py#L328) | 328 | `"        transfer_encodings = self.headers.get_all(\"Transfer-Encoding\", [])"` | — |
| [SRC-EEF2E6447C-L000329](../../api/omarai.py#L329) | 329 | `"        if transfer_encodings:"` | — |
| [SRC-EEF2E6447C-L000330](../../api/omarai.py#L330) | 330 | `"            # This API does not implement chunked request decoding. Never let a"` | — |
| [SRC-EEF2E6447C-L000331](../../api/omarai.py#L331) | 331 | `"            # proxy/backend disagree about where the request body ends."` | — |
| [SRC-EEF2E6447C-L000332](../../api/omarai.py#L332) | 332 | `"            self.close_connection = True"` | — |
| [SRC-EEF2E6447C-L000333](../../api/omarai.py#L333) | 333 | `"            self.send_error(400, \"Transfer-Encoding is not supported\")"` | — |
| [SRC-EEF2E6447C-L000334](../../api/omarai.py#L334) | 334 | `"            return False"` | — |
| [SRC-EEF2E6447C-L000335](../../api/omarai.py#L335) | 335 | `""` | — |
| [SRC-EEF2E6447C-L000336](../../api/omarai.py#L336) | 336 | `"        content_lengths = self.headers.get_all(\"Content-Length\", [])"` | — |
| [SRC-EEF2E6447C-L000337](../../api/omarai.py#L337) | 337 | `"        if len(content_lengths) > 1:"` | — |
| [SRC-EEF2E6447C-L000338](../../api/omarai.py#L338) | 338 | `"            self.close_connection = True"` | — |
| [SRC-EEF2E6447C-L000339](../../api/omarai.py#L339) | 339 | `"            self.send_error(400, \"Multiple Content-Length headers are not supported\")"` | — |
| [SRC-EEF2E6447C-L000340](../../api/omarai.py#L340) | 340 | `"            return False"` | — |
| [SRC-EEF2E6447C-L000341](../../api/omarai.py#L341) | 341 | `""` | — |
| [SRC-EEF2E6447C-L000342](../../api/omarai.py#L342) | 342 | `"        if content_lengths:"` | — |
| [SRC-EEF2E6447C-L000343](../../api/omarai.py#L343) | 343 | `"            raw_size = content_lengths[0].strip()"` | — |
| [SRC-EEF2E6447C-L000344](../../api/omarai.py#L344) | 344 | `"            if not raw_size or not raw_size.isascii() or not raw_size.isdecimal():"` | — |
| [SRC-EEF2E6447C-L000345](../../api/omarai.py#L345) | 345 | `"                self.close_connection = True"` | — |
| [SRC-EEF2E6447C-L000346](../../api/omarai.py#L346) | 346 | `"                self.send_error(400, \"valid Content-Length is required\")"` | — |
| [SRC-EEF2E6447C-L000347](../../api/omarai.py#L347) | 347 | `"                return False"` | — |
| [SRC-EEF2E6447C-L000348](../../api/omarai.py#L348) | 348 | `"            if self.command != \"POST\" and raw_size.lstrip(\"0\"):"` | — |
| [SRC-EEF2E6447C-L000349](../../api/omarai.py#L349) | 349 | `"                # GET/HEAD/other methods are not allowed to leave unread bytes"` | — |
| [SRC-EEF2E6447C-L000350](../../api/omarai.py#L350) | 350 | `"                # on a persistent connection."` | — |
| [SRC-EEF2E6447C-L000351](../../api/omarai.py#L351) | 351 | `"                self.close_connection = True"` | — |
| [SRC-EEF2E6447C-L000352](../../api/omarai.py#L352) | 352 | `"                self.send_error(400, \"Content-Length body is not supported for this method\")"` | — |
| [SRC-EEF2E6447C-L000353](../../api/omarai.py#L353) | 353 | `"                return False"` | — |
| [SRC-EEF2E6447C-L000354](../../api/omarai.py#L354) | 354 | `""` | — |
| [SRC-EEF2E6447C-L000355](../../api/omarai.py#L355) | 355 | `"        return True"` | — |
| [SRC-EEF2E6447C-L000356](../../api/omarai.py#L356) | 356 | `""` | — |
| [SRC-EEF2E6447C-L000357](../../api/omarai.py#L357) | 357 | `"    store = _lead_store_from_environment()"` | — |
| [SRC-EEF2E6447C-L000358](../../api/omarai.py#L358) | 358 | `"    _rate_lock = threading.Lock()"` | — |
| [SRC-EEF2E6447C-L000359](../../api/omarai.py#L359) | 359 | `"    _request_times: ClassVar[dict[str, deque[float]]] = defaultdict(deque)"` | — |
| [SRC-EEF2E6447C-L000360](../../api/omarai.py#L360) | 360 | `"    _rate_last_cleanup: ClassVar[float] = 0.0"` | — |
| [SRC-EEF2E6447C-L000361](../../api/omarai.py#L361) | 361 | `"    RATE_LIMIT_REQUESTS = 20"` | — |
| [SRC-EEF2E6447C-L000362](../../api/omarai.py#L362) | 362 | `"    RATE_LIMIT_WINDOW_SECONDS = 60"` | — |
| [SRC-EEF2E6447C-L000363](../../api/omarai.py#L363) | 363 | `"    RATE_LIMIT_CLEANUP_INTERVAL_SECONDS = 60"` | — |
| [SRC-EEF2E6447C-L000364](../../api/omarai.py#L364) | 364 | `"    # Reserve the final bucket for clients beyond the per-process tracking ceiling."` | — |
| [SRC-EEF2E6447C-L000365](../../api/omarai.py#L365) | 365 | `"    MAX_RATE_LIMIT_CLIENT_BUCKETS = 4096"` | — |
| [SRC-EEF2E6447C-L000366](../../api/omarai.py#L366) | 366 | `"    RATE_LIMIT_OVERFLOW_KEY = \"__omarai_overflow__\""` | — |
| [SRC-EEF2E6447C-L000367](../../api/omarai.py#L367) | 367 | `"    AGENT_CONCURRENCY_LIMIT = _configured_agent_concurrency_limit()"` | — |
| [SRC-EEF2E6447C-L000368](../../api/omarai.py#L368) | 368 | `"    _agent_semaphore = threading.BoundedSemaphore(AGENT_CONCURRENCY_LIMIT)"` | — |
| [SRC-EEF2E6447C-L000369](../../api/omarai.py#L369) | 369 | `""` | — |
| [SRC-EEF2E6447C-L000370](../../api/omarai.py#L370) | 370 | `"    def _run_bounded_agent_operation(self, operation):"` | — |
| [SRC-EEF2E6447C-L000371](../../api/omarai.py#L371) | 371 | `"        \"\"\"Run an expensive operation only when a process-local slot is available.\"\"\""` | — |
| [SRC-EEF2E6447C-L000372](../../api/omarai.py#L372) | 372 | `"        cls = type(self)"` | — |
| [SRC-EEF2E6447C-L000373](../../api/omarai.py#L373) | 373 | `"        if not cls._agent_semaphore.acquire(blocking=False):"` | — |
| [SRC-EEF2E6447C-L000374](../../api/omarai.py#L374) | 374 | `"            return self.respond("` | — |
| [SRC-EEF2E6447C-L000375](../../api/omarai.py#L375) | 375 | `"                503,"` | — |
| [SRC-EEF2E6447C-L000376](../../api/omarai.py#L376) | 376 | `"                {"` | — |
| [SRC-EEF2E6447C-L000377](../../api/omarai.py#L377) | 377 | `"                    \"error\": \"خدمة البحث مشغولة حاليًا؛ أعد المحاولة بعد قليل.\","` | — |
| [SRC-EEF2E6447C-L000378](../../api/omarai.py#L378) | 378 | `"                    \"retry_after_seconds\": 5,"` | — |
| [SRC-EEF2E6447C-L000379](../../api/omarai.py#L379) | 379 | `"                    \"process_concurrency_limit\": cls.AGENT_CONCURRENCY_LIMIT,"` | — |
| [SRC-EEF2E6447C-L000380](../../api/omarai.py#L380) | 380 | `"                },"` | — |
| [SRC-EEF2E6447C-L000381](../../api/omarai.py#L381) | 381 | `"            )"` | — |
| [SRC-EEF2E6447C-L000382](../../api/omarai.py#L382) | 382 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000383](../../api/omarai.py#L383) | 383 | `"            return self.respond(200, operation())"` | — |
| [SRC-EEF2E6447C-L000384](../../api/omarai.py#L384) | 384 | `"        finally:"` | — |
| [SRC-EEF2E6447C-L000385](../../api/omarai.py#L385) | 385 | `"            cls._agent_semaphore.release()"` | — |
| [SRC-EEF2E6447C-L000386](../../api/omarai.py#L386) | 386 | `""` | — |
| [SRC-EEF2E6447C-L000387](../../api/omarai.py#L387) | 387 | `"    def _session_cookie_name(self):"` | — |
| [SRC-EEF2E6447C-L000388](../../api/omarai.py#L388) | 388 | `"        \"\"\"Use the __Host- prefix on HTTPS public deployments.\"\"\""` | — |
| [SRC-EEF2E6447C-L000389](../../api/omarai.py#L389) | 389 | `"        if os.getenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"\").strip() == \"1\":"` | — |
| [SRC-EEF2E6447C-L000390](../../api/omarai.py#L390) | 390 | `"            return \"__Host-omarai_session\""` | — |
| [SRC-EEF2E6447C-L000391](../../api/omarai.py#L391) | 391 | `"        return \"omarai_session\""` | — |
| [SRC-EEF2E6447C-L000392](../../api/omarai.py#L392) | 392 | `""` | — |
| [SRC-EEF2E6447C-L000393](../../api/omarai.py#L393) | 393 | `"    def _session_cookie_header(self, token: str) -> str:"` | — |
| [SRC-EEF2E6447C-L000394](../../api/omarai.py#L394) | 394 | `"        if not BROWSER_SESSION_ID_RE.fullmatch(token):"` | — |
| [SRC-EEF2E6447C-L000395](../../api/omarai.py#L395) | 395 | `"            raise ValueError(\"browser access token has an unsupported format\")"` | — |
| [SRC-EEF2E6447C-L000396](../../api/omarai.py#L396) | 396 | `"        parts = ["` | — |
| [SRC-EEF2E6447C-L000397](../../api/omarai.py#L397) | 397 | `"            f\"{self._session_cookie_name()}={token}\","` | — |
| [SRC-EEF2E6447C-L000398](../../api/omarai.py#L398) | 398 | `"            \"Path=/\","` | — |
| [SRC-EEF2E6447C-L000399](../../api/omarai.py#L399) | 399 | `"            \"HttpOnly\","` | — |
| [SRC-EEF2E6447C-L000400](../../api/omarai.py#L400) | 400 | `"            \"SameSite=Strict\","` | — |
| [SRC-EEF2E6447C-L000401](../../api/omarai.py#L401) | 401 | `"            f\"Max-Age={BROWSER_SESSION_COOKIE_MAX_AGE}\","` | — |
| [SRC-EEF2E6447C-L000402](../../api/omarai.py#L402) | 402 | `"        ]"` | — |
| [SRC-EEF2E6447C-L000403](../../api/omarai.py#L403) | 403 | `"        if os.getenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"\").strip() == \"1\":"` | — |
| [SRC-EEF2E6447C-L000404](../../api/omarai.py#L404) | 404 | `"            parts.insert(2, \"Secure\")"` | — |
| [SRC-EEF2E6447C-L000405](../../api/omarai.py#L405) | 405 | `"        return \"; \".join(parts)"` | — |
| [SRC-EEF2E6447C-L000406](../../api/omarai.py#L406) | 406 | `""` | — |
| [SRC-EEF2E6447C-L000407](../../api/omarai.py#L407) | 407 | `"    def _clear_session_cookie_header(self) -> str:"` | — |
| [SRC-EEF2E6447C-L000408](../../api/omarai.py#L408) | 408 | `"        parts = ["` | — |
| [SRC-EEF2E6447C-L000409](../../api/omarai.py#L409) | 409 | `"            f\"{self._session_cookie_name()}=\","` | — |
| [SRC-EEF2E6447C-L000410](../../api/omarai.py#L410) | 410 | `"            \"Path=/\","` | — |
| [SRC-EEF2E6447C-L000411](../../api/omarai.py#L411) | 411 | `"            \"HttpOnly\","` | — |
| [SRC-EEF2E6447C-L000412](../../api/omarai.py#L412) | 412 | `"            \"SameSite=Strict\","` | — |
| [SRC-EEF2E6447C-L000413](../../api/omarai.py#L413) | 413 | `"            \"Max-Age=0\","` | — |
| [SRC-EEF2E6447C-L000414](../../api/omarai.py#L414) | 414 | `"        ]"` | — |
| [SRC-EEF2E6447C-L000415](../../api/omarai.py#L415) | 415 | `"        if os.getenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"\").strip() == \"1\":"` | — |
| [SRC-EEF2E6447C-L000416](../../api/omarai.py#L416) | 416 | `"            parts.insert(2, \"Secure\")"` | — |
| [SRC-EEF2E6447C-L000417](../../api/omarai.py#L417) | 417 | `"        return \"; \".join(parts)"` | — |
| [SRC-EEF2E6447C-L000418](../../api/omarai.py#L418) | 418 | `""` | — |
| [SRC-EEF2E6447C-L000419](../../api/omarai.py#L419) | 419 | `"    def _principal_for_access_token(self, token: str):"` | — |
| [SRC-EEF2E6447C-L000420](../../api/omarai.py#L420) | 420 | `"        expected = os.getenv(\"OMARAI_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-EEF2E6447C-L000421](../../api/omarai.py#L421) | 421 | `"        if expected and hmac.compare_digest(token, expected):"` | — |
| [SRC-EEF2E6447C-L000422](../../api/omarai.py#L422) | 422 | `"            return self.store.default_principal()"` | — |
| [SRC-EEF2E6447C-L000423](../../api/omarai.py#L423) | 423 | `"        return self.store.resolve_api_token(token)"` | — |
| [SRC-EEF2E6447C-L000424](../../api/omarai.py#L424) | 424 | `""` | — |
| [SRC-EEF2E6447C-L000425](../../api/omarai.py#L425) | 425 | `"    _FORWARDING_HEADERS = ("` | — |
| [SRC-EEF2E6447C-L000426](../../api/omarai.py#L426) | 426 | `"        \"X-Forwarded-For\", \"X-Forwarded-Host\", \"X-Forwarded-Proto\","` | — |
| [SRC-EEF2E6447C-L000427](../../api/omarai.py#L427) | 427 | `"        \"X-Real-IP\", \"Forwarded\", \"CF-Connecting-IP\", \"True-Client-IP\","` | — |
| [SRC-EEF2E6447C-L000428](../../api/omarai.py#L428) | 428 | `"    )"` | — |
| [SRC-EEF2E6447C-L000429](../../api/omarai.py#L429) | 429 | `""` | — |
| [SRC-EEF2E6447C-L000430](../../api/omarai.py#L430) | 430 | `"    def _has_forwarding_headers(self) -> bool:"` | — |
| [SRC-EEF2E6447C-L000431](../../api/omarai.py#L431) | 431 | `"        return any(self.headers.get(name) for name in self._FORWARDING_HEADERS)"` | — |
| [SRC-EEF2E6447C-L000432](../../api/omarai.py#L432) | 432 | `""` | — |
| [SRC-EEF2E6447C-L000433](../../api/omarai.py#L433) | 433 | `"    def _authorized(self):"` | — |
| [SRC-EEF2E6447C-L000434](../../api/omarai.py#L434) | 434 | `"        \"\"\"Resolve a verified bearer token or HttpOnly browser cookie."` | — |
| [SRC-EEF2E6447C-L000435](../../api/omarai.py#L435) | 435 | `""` | — |
| [SRC-EEF2E6447C-L000436](../../api/omarai.py#L436) | 436 | `"        Browser cookies are accepted only with same-origin POST requests. Request-body"` | — |
| [SRC-EEF2E6447C-L000437](../../api/omarai.py#L437) | 437 | `"        tenant IDs are never used to establish tenant context."` | — |
| [SRC-EEF2E6447C-L000438](../../api/omarai.py#L438) | 438 | `"        \"\"\""` | — |
| [SRC-EEF2E6447C-L000439](../../api/omarai.py#L439) | 439 | `"        self._authenticated_principal = None"` | — |
| [SRC-EEF2E6447C-L000440](../../api/omarai.py#L440) | 440 | `"        self._cookie_authenticated = False"` | — |
| [SRC-EEF2E6447C-L000441](../../api/omarai.py#L441) | 441 | `"        self._browser_session_id = \"\""` | — |
| [SRC-EEF2E6447C-L000442](../../api/omarai.py#L442) | 442 | `"        supplied = self.headers.get(\"Authorization\", \"\")"` | — |
| [SRC-EEF2E6447C-L000443](../../api/omarai.py#L443) | 443 | `"        if supplied.startswith(\"Bearer \"):"` | — |
| [SRC-EEF2E6447C-L000444](../../api/omarai.py#L444) | 444 | `"            token = supplied[7:].strip()"` | — |
| [SRC-EEF2E6447C-L000445](../../api/omarai.py#L445) | 445 | `"            self._authenticated_principal = self._principal_for_access_token(token)"` | — |
| [SRC-EEF2E6447C-L000446](../../api/omarai.py#L446) | 446 | `"            return bool(self._authenticated_principal)"` | — |
| [SRC-EEF2E6447C-L000447](../../api/omarai.py#L447) | 447 | `""` | — |
| [SRC-EEF2E6447C-L000448](../../api/omarai.py#L448) | 448 | `"        cookie = SimpleCookie()"` | — |
| [SRC-EEF2E6447C-L000449](../../api/omarai.py#L449) | 449 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000450](../../api/omarai.py#L450) | 450 | `"            cookie.load(self.headers.get(\"Cookie\", \"\"))"` | — |
| [SRC-EEF2E6447C-L000451](../../api/omarai.py#L451) | 451 | `"        except Exception:"` | — |
| [SRC-EEF2E6447C-L000452](../../api/omarai.py#L452) | 452 | `"            cookie = SimpleCookie()"` | — |
| [SRC-EEF2E6447C-L000453](../../api/omarai.py#L453) | 453 | `"        morsel = cookie.get(self._session_cookie_name())"` | — |
| [SRC-EEF2E6447C-L000454](../../api/omarai.py#L454) | 454 | `"        if morsel is not None:"` | — |
| [SRC-EEF2E6447C-L000455](../../api/omarai.py#L455) | 455 | `"            token = morsel.value"` | — |
| [SRC-EEF2E6447C-L000456](../../api/omarai.py#L456) | 456 | `"            if BROWSER_SESSION_ID_RE.fullmatch(token):"` | — |
| [SRC-EEF2E6447C-L000457](../../api/omarai.py#L457) | 457 | `"                self._authenticated_principal = self.store.resolve_web_session("` | — |
| [SRC-EEF2E6447C-L000458](../../api/omarai.py#L458) | 458 | `"                    token,"` | — |
| [SRC-EEF2E6447C-L000459](../../api/omarai.py#L459) | 459 | `"                    shared_token=os.getenv(\"OMARAI_ACCESS_TOKEN\", \"\").strip(),"` | — |
| [SRC-EEF2E6447C-L000460](../../api/omarai.py#L460) | 460 | `"                )"` | — |
| [SRC-EEF2E6447C-L000461](../../api/omarai.py#L461) | 461 | `"                self._cookie_authenticated = bool(self._authenticated_principal)"` | — |
| [SRC-EEF2E6447C-L000462](../../api/omarai.py#L462) | 462 | `"                if self._cookie_authenticated:"` | — |
| [SRC-EEF2E6447C-L000463](../../api/omarai.py#L463) | 463 | `"                    self._browser_session_id = token"` | — |
| [SRC-EEF2E6447C-L000464](../../api/omarai.py#L464) | 464 | `"                return self._cookie_authenticated"` | — |
| [SRC-EEF2E6447C-L000465](../../api/omarai.py#L465) | 465 | `""` | — |
| [SRC-EEF2E6447C-L000466](../../api/omarai.py#L466) | 466 | `"        # Loopback is not proof of a human identity: reverse proxies and tunnels"` | — |
| [SRC-EEF2E6447C-L000467](../../api/omarai.py#L467) | 467 | `"        # may connect from 127.0.0.1 while forwarding untrusted remote requests."` | — |
| [SRC-EEF2E6447C-L000468](../../api/omarai.py#L468) | 468 | `"        # Local development must opt in explicitly; public deployments never do."` | — |
| [SRC-EEF2E6447C-L000469](../../api/omarai.py#L469) | 469 | `"        if ("` | — |
| [SRC-EEF2E6447C-L000470](../../api/omarai.py#L470) | 470 | `"            os.getenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"\").strip() != \"1\""` | — |
| [SRC-EEF2E6447C-L000471](../../api/omarai.py#L471) | 471 | `"            and os.getenv(\"OMARAI_ALLOW_LOOPBACK_AUTH\", \"\").strip() == \"1\""` | — |
| [SRC-EEF2E6447C-L000472](../../api/omarai.py#L472) | 472 | `"            and not self._has_forwarding_headers()"` | — |
| [SRC-EEF2E6447C-L000473](../../api/omarai.py#L473) | 473 | `"        ):"` | — |
| [SRC-EEF2E6447C-L000474](../../api/omarai.py#L474) | 474 | `"            try:"` | — |
| [SRC-EEF2E6447C-L000475](../../api/omarai.py#L475) | 475 | `"                if ipaddress.ip_address(self.client_address[0]).is_loopback:"` | — |
| [SRC-EEF2E6447C-L000476](../../api/omarai.py#L476) | 476 | `"                    self._authenticated_principal = self.store.default_principal()"` | — |
| [SRC-EEF2E6447C-L000477](../../api/omarai.py#L477) | 477 | `"                    return bool(self._authenticated_principal)"` | — |
| [SRC-EEF2E6447C-L000478](../../api/omarai.py#L478) | 478 | `"            except ValueError:"` | — |
| [SRC-EEF2E6447C-L000479](../../api/omarai.py#L479) | 479 | `"                pass"` | — |
| [SRC-EEF2E6447C-L000480](../../api/omarai.py#L480) | 480 | `"        return False"` | — |
| [SRC-EEF2E6447C-L000481](../../api/omarai.py#L481) | 481 | `""` | — |
| [SRC-EEF2E6447C-L000482](../../api/omarai.py#L482) | 482 | `"    def _allowed_origins(self):"` | — |
| [SRC-EEF2E6447C-L000483](../../api/omarai.py#L483) | 483 | `"        \"\"\"Return configured browser origins plus this service’s own origin."` | — |
| [SRC-EEF2E6447C-L000484](../../api/omarai.py#L484) | 484 | `""` | — |
| [SRC-EEF2E6447C-L000485](../../api/omarai.py#L485) | 485 | `"        OMARAI_ALLOWED_ORIGINS is a comma-separated list of trusted origins"` | — |
| [SRC-EEF2E6447C-L000486](../../api/omarai.py#L486) | 486 | `"        (scheme + host + optional port; no path and no wildcard)."` | — |
| [SRC-EEF2E6447C-L000487](../../api/omarai.py#L487) | 487 | `"        \"\"\""` | — |
| [SRC-EEF2E6447C-L000488](../../api/omarai.py#L488) | 488 | `"        configured = os.getenv(\"OMARAI_ALLOWED_ORIGINS\", \"\")"` | — |
| [SRC-EEF2E6447C-L000489](../../api/omarai.py#L489) | 489 | `"        origins = {"` | — |
| [SRC-EEF2E6447C-L000490](../../api/omarai.py#L490) | 490 | `"            item.strip().rstrip(\"/\")"` | — |
| [SRC-EEF2E6447C-L000491](../../api/omarai.py#L491) | 491 | `"            for item in configured.split(\",\")"` | — |
| [SRC-EEF2E6447C-L000492](../../api/omarai.py#L492) | 492 | `"            if item.strip()"` | — |
| [SRC-EEF2E6447C-L000493](../../api/omarai.py#L493) | 493 | `"        }"` | — |
| [SRC-EEF2E6447C-L000494](../../api/omarai.py#L494) | 494 | `"        if os.getenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"\").strip() == \"1\":"` | — |
| [SRC-EEF2E6447C-L000495](../../api/omarai.py#L495) | 495 | `"            # Host identifies the requested service origin. Do not derive allowed"` | — |
| [SRC-EEF2E6447C-L000496](../../api/omarai.py#L496) | 496 | `"            # origins from X-Forwarded-Host: direct clients can spoof that header"` | — |
| [SRC-EEF2E6447C-L000497](../../api/omarai.py#L497) | 497 | `"            # unless the reverse proxy is separately configured to overwrite it."` | — |
| [SRC-EEF2E6447C-L000498](../../api/omarai.py#L498) | 498 | `"            scheme = self.headers.get(\"X-Forwarded-Proto\", \"https\").split(\",\", 1)[0].strip().lower()"` | — |
| [SRC-EEF2E6447C-L000499](../../api/omarai.py#L499) | 499 | `"            host = self.headers.get(\"Host\", \"\").split(\",\", 1)[0].strip()"` | — |
| [SRC-EEF2E6447C-L000500](../../api/omarai.py#L500) | 500 | `"            if host:"` | — |
| [SRC-EEF2E6447C-L000501](../../api/omarai.py#L501) | 501 | `"                origins.add(f\"https://{host}\".rstrip(\"/\"))"` | — |
| [SRC-EEF2E6447C-L000502](../../api/omarai.py#L502) | 502 | `"                origins.add(f\"{scheme}://{host}\".rstrip(\"/\"))"` | — |
| [SRC-EEF2E6447C-L000503](../../api/omarai.py#L503) | 503 | `"        else:"` | — |
| [SRC-EEF2E6447C-L000504](../../api/omarai.py#L504) | 504 | `"            port = self.server.server_port"` | — |
| [SRC-EEF2E6447C-L000505](../../api/omarai.py#L505) | 505 | `"            origins.update("` | — |
| [SRC-EEF2E6447C-L000506](../../api/omarai.py#L506) | 506 | `"                {"` | — |
| [SRC-EEF2E6447C-L000507](../../api/omarai.py#L507) | 507 | `"                    f\"http://127.0.0.1:{port}\","` | — |
| [SRC-EEF2E6447C-L000508](../../api/omarai.py#L508) | 508 | `"                    f\"http://localhost:{port}\","` | — |
| [SRC-EEF2E6447C-L000509](../../api/omarai.py#L509) | 509 | `"                    f\"http://[::1]:{port}\","` | — |
| [SRC-EEF2E6447C-L000510](../../api/omarai.py#L510) | 510 | `"                }"` | — |
| [SRC-EEF2E6447C-L000511](../../api/omarai.py#L511) | 511 | `"            )"` | — |
| [SRC-EEF2E6447C-L000512](../../api/omarai.py#L512) | 512 | `"        return origins"` | — |
| [SRC-EEF2E6447C-L000513](../../api/omarai.py#L513) | 513 | `""` | — |
| [SRC-EEF2E6447C-L000514](../../api/omarai.py#L514) | 514 | `"    def _origin_allowed(self, origin):"` | — |
| [SRC-EEF2E6447C-L000515](../../api/omarai.py#L515) | 515 | `"        return bool(origin) and origin.rstrip(\"/\") in self._allowed_origins()"` | — |
| [SRC-EEF2E6447C-L000516](../../api/omarai.py#L516) | 516 | `""` | — |
| [SRC-EEF2E6447C-L000517](../../api/omarai.py#L517) | 517 | `"    def _rate_limit_client_key(self):"` | — |
| [SRC-EEF2E6447C-L000518](../../api/omarai.py#L518) | 518 | `"        \"\"\"Choose a rate-limit identity without trusting spoofable proxy headers by default."` | — |
| [SRC-EEF2E6447C-L000519](../../api/omarai.py#L519) | 519 | `""` | — |
| [SRC-EEF2E6447C-L000520](../../api/omarai.py#L520) | 520 | `"        Set OMARAI_TRUST_PROXY_HEADERS=1 only when the deployment's trusted reverse"` | — |
| [SRC-EEF2E6447C-L000521](../../api/omarai.py#L521) | 521 | `"        proxy appends the actual client IP as the rightmost X-Forwarded-For value."` | — |
| [SRC-EEF2E6447C-L000522](../../api/omarai.py#L522) | 522 | `"        \"\"\""` | — |
| [SRC-EEF2E6447C-L000523](../../api/omarai.py#L523) | 523 | `"        direct_ip = self.client_address[0]"` | — |
| [SRC-EEF2E6447C-L000524](../../api/omarai.py#L524) | 524 | `"        if os.getenv(\"OMARAI_TRUST_PROXY_HEADERS\", \"\").strip() != \"1\":"` | — |
| [SRC-EEF2E6447C-L000525](../../api/omarai.py#L525) | 525 | `"            return direct_ip"` | — |
| [SRC-EEF2E6447C-L000526](../../api/omarai.py#L526) | 526 | `"        forwarded = self.headers.get(\"X-Forwarded-For\", \"\")"` | — |
| [SRC-EEF2E6447C-L000527](../../api/omarai.py#L527) | 527 | `"        candidate = forwarded.rsplit(\",\", 1)[-1].strip() if forwarded else \"\""` | — |
| [SRC-EEF2E6447C-L000528](../../api/omarai.py#L528) | 528 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000529](../../api/omarai.py#L529) | 529 | `"            return str(ipaddress.ip_address(candidate))"` | — |
| [SRC-EEF2E6447C-L000530](../../api/omarai.py#L530) | 530 | `"        except ValueError:"` | — |
| [SRC-EEF2E6447C-L000531](../../api/omarai.py#L531) | 531 | `"            return direct_ip"` | — |
| [SRC-EEF2E6447C-L000532](../../api/omarai.py#L532) | 532 | `""` | — |
| [SRC-EEF2E6447C-L000533](../../api/omarai.py#L533) | 533 | `"    def _rate_limit_ok(self):"` | — |
| [SRC-EEF2E6447C-L000534](../../api/omarai.py#L534) | 534 | `"        client_ip = self._rate_limit_client_key()"` | — |
| [SRC-EEF2E6447C-L000535](../../api/omarai.py#L535) | 535 | `"        now = time.monotonic()"` | — |
| [SRC-EEF2E6447C-L000536](../../api/omarai.py#L536) | 536 | `"        cls = type(self)"` | — |
| [SRC-EEF2E6447C-L000537](../../api/omarai.py#L537) | 537 | `"        with self._rate_lock:"` | — |
| [SRC-EEF2E6447C-L000538](../../api/omarai.py#L538) | 538 | `"            # Periodically remove IP buckets whose entire sliding window has expired."` | — |
| [SRC-EEF2E6447C-L000539](../../api/omarai.py#L539) | 539 | `"            # Without this sweep, a public endpoint could retain one empty deque per"` | — |
| [SRC-EEF2E6447C-L000540](../../api/omarai.py#L540) | 540 | `"            # distinct client IP forever, even though the rate-limit window is 60 sec."` | — |
| [SRC-EEF2E6447C-L000541](../../api/omarai.py#L541) | 541 | `"            if now - cls._rate_last_cleanup >= cls.RATE_LIMIT_CLEANUP_INTERVAL_SECONDS:"` | — |
| [SRC-EEF2E6447C-L000542](../../api/omarai.py#L542) | 542 | `"                cutoff = now - cls.RATE_LIMIT_WINDOW_SECONDS"` | — |
| [SRC-EEF2E6447C-L000543](../../api/omarai.py#L543) | 543 | `"                for key, timestamps in list(cls._request_times.items()):"` | — |
| [SRC-EEF2E6447C-L000544](../../api/omarai.py#L544) | 544 | `"                    while timestamps and timestamps[0] <= cutoff:"` | — |
| [SRC-EEF2E6447C-L000545](../../api/omarai.py#L545) | 545 | `"                        timestamps.popleft()"` | — |
| [SRC-EEF2E6447C-L000546](../../api/omarai.py#L546) | 546 | `"                    if not timestamps:"` | — |
| [SRC-EEF2E6447C-L000547](../../api/omarai.py#L547) | 547 | `"                        cls._request_times.pop(key, None)"` | — |
| [SRC-EEF2E6447C-L000548](../../api/omarai.py#L548) | 548 | `"                cls._rate_last_cleanup = now"` | — |
| [SRC-EEF2E6447C-L000549](../../api/omarai.py#L549) | 549 | `""` | — |
| [SRC-EEF2E6447C-L000550](../../api/omarai.py#L550) | 550 | `"            if ("` | — |
| [SRC-EEF2E6447C-L000551](../../api/omarai.py#L551) | 551 | `"                client_ip not in cls._request_times"` | — |
| [SRC-EEF2E6447C-L000552](../../api/omarai.py#L552) | 552 | `"                and len(cls._request_times) >= max(1, cls.MAX_RATE_LIMIT_CLIENT_BUCKETS) - 1"` | — |
| [SRC-EEF2E6447C-L000553](../../api/omarai.py#L553) | 553 | `"            ):"` | — |
| [SRC-EEF2E6447C-L000554](../../api/omarai.py#L554) | 554 | `"                # Bound attacker-controlled cardinality. Excess identities share a"` | — |
| [SRC-EEF2E6447C-L000555](../../api/omarai.py#L555) | 555 | `"                # conservative overflow bucket instead of allocating one deque per IP."` | — |
| [SRC-EEF2E6447C-L000556](../../api/omarai.py#L556) | 556 | `"                client_ip = cls.RATE_LIMIT_OVERFLOW_KEY"` | — |
| [SRC-EEF2E6447C-L000557](../../api/omarai.py#L557) | 557 | `"            events = cls._request_times[client_ip]"` | — |
| [SRC-EEF2E6447C-L000558](../../api/omarai.py#L558) | 558 | `"            while events and now - events[0] >= cls.RATE_LIMIT_WINDOW_SECONDS:"` | — |
| [SRC-EEF2E6447C-L000559](../../api/omarai.py#L559) | 559 | `"                events.popleft()"` | — |
| [SRC-EEF2E6447C-L000560](../../api/omarai.py#L560) | 560 | `"            if len(events) >= cls.RATE_LIMIT_REQUESTS:"` | — |
| [SRC-EEF2E6447C-L000561](../../api/omarai.py#L561) | 561 | `"                return False"` | — |
| [SRC-EEF2E6447C-L000562](../../api/omarai.py#L562) | 562 | `"            events.append(now)"` | — |
| [SRC-EEF2E6447C-L000563](../../api/omarai.py#L563) | 563 | `"            return True"` | — |
| [SRC-EEF2E6447C-L000564](../../api/omarai.py#L564) | 564 | `""` | — |
| [SRC-EEF2E6447C-L000565](../../api/omarai.py#L565) | 565 | `"    def _read_request_body(self) -> bytes \| None:"` | — |
| [SRC-EEF2E6447C-L000566](../../api/omarai.py#L566) | 566 | `"        \"\"\"Read a bounded body with both idle and absolute wall-clock deadlines.\"\"\""` | — |
| [SRC-EEF2E6447C-L000567](../../api/omarai.py#L567) | 567 | `"        raw_size = self.headers.get(\"Content-Length\", \"\").strip()"` | — |
| [SRC-EEF2E6447C-L000568](../../api/omarai.py#L568) | 568 | `"        if not raw_size or not raw_size.isascii() or not raw_size.isdecimal():"` | — |
| [SRC-EEF2E6447C-L000569](../../api/omarai.py#L569) | 569 | `"            self.respond(400, {\"error\": \"valid Content-Length is required\"})"` | — |
| [SRC-EEF2E6447C-L000570](../../api/omarai.py#L570) | 570 | `"            return None"` | — |
| [SRC-EEF2E6447C-L000571](../../api/omarai.py#L571) | 571 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000572](../../api/omarai.py#L572) | 572 | `"            size = int(raw_size)"` | — |
| [SRC-EEF2E6447C-L000573](../../api/omarai.py#L573) | 573 | `"        except ValueError:"` | — |
| [SRC-EEF2E6447C-L000574](../../api/omarai.py#L574) | 574 | `"            self.respond(400, {\"error\": \"valid Content-Length is required\"})"` | — |
| [SRC-EEF2E6447C-L000575](../../api/omarai.py#L575) | 575 | `"            return None"` | — |
| [SRC-EEF2E6447C-L000576](../../api/omarai.py#L576) | 576 | `"        if size <= 0:"` | — |
| [SRC-EEF2E6447C-L000577](../../api/omarai.py#L577) | 577 | `"            self.respond(400, {\"error\": \"request body is required\"})"` | — |
| [SRC-EEF2E6447C-L000578](../../api/omarai.py#L578) | 578 | `"            return None"` | — |
| [SRC-EEF2E6447C-L000579](../../api/omarai.py#L579) | 579 | `"        if size > MAX_REQUEST_BODY_BYTES:"` | — |
| [SRC-EEF2E6447C-L000580](../../api/omarai.py#L580) | 580 | `"            # The declared body remains unread; do not reuse this connection."` | — |
| [SRC-EEF2E6447C-L000581](../../api/omarai.py#L581) | 581 | `"            self.close_connection = True"` | — |
| [SRC-EEF2E6447C-L000582](../../api/omarai.py#L582) | 582 | `"            self.respond(413, {\"error\": \"request too large\"})"` | — |
| [SRC-EEF2E6447C-L000583](../../api/omarai.py#L583) | 583 | `"            return None"` | — |
| [SRC-EEF2E6447C-L000584](../../api/omarai.py#L584) | 584 | `""` | — |
| [SRC-EEF2E6447C-L000585](../../api/omarai.py#L585) | 585 | `"        total_timeout = max("` | — |
| [SRC-EEF2E6447C-L000586](../../api/omarai.py#L586) | 586 | `"            0.1,"` | — |
| [SRC-EEF2E6447C-L000587](../../api/omarai.py#L587) | 587 | `"            min("` | — |
| [SRC-EEF2E6447C-L000588](../../api/omarai.py#L588) | 588 | `"                float(REQUEST_BODY_READ_TIMEOUT_SECONDS),"` | — |
| [SRC-EEF2E6447C-L000589](../../api/omarai.py#L589) | 589 | `"                MAX_REQUEST_BODY_READ_TIMEOUT_SECONDS,"` | — |
| [SRC-EEF2E6447C-L000590](../../api/omarai.py#L590) | 590 | `"            ),"` | — |
| [SRC-EEF2E6447C-L000591](../../api/omarai.py#L591) | 591 | `"        )"` | — |
| [SRC-EEF2E6447C-L000592](../../api/omarai.py#L592) | 592 | `"        idle_timeout = max("` | — |
| [SRC-EEF2E6447C-L000593](../../api/omarai.py#L593) | 593 | `"            0.1,"` | — |
| [SRC-EEF2E6447C-L000594](../../api/omarai.py#L594) | 594 | `"            min("` | — |
| [SRC-EEF2E6447C-L000595](../../api/omarai.py#L595) | 595 | `"                float(REQUEST_BODY_IDLE_TIMEOUT_SECONDS),"` | — |
| [SRC-EEF2E6447C-L000596](../../api/omarai.py#L596) | 596 | `"                MAX_REQUEST_BODY_READ_TIMEOUT_SECONDS,"` | — |
| [SRC-EEF2E6447C-L000597](../../api/omarai.py#L597) | 597 | `"            ),"` | — |
| [SRC-EEF2E6447C-L000598](../../api/omarai.py#L598) | 598 | `"        )"` | — |
| [SRC-EEF2E6447C-L000599](../../api/omarai.py#L599) | 599 | `"        deadline = time.monotonic() + total_timeout"` | — |
| [SRC-EEF2E6447C-L000600](../../api/omarai.py#L600) | 600 | `"        previous_timeout = self.connection.gettimeout()"` | — |
| [SRC-EEF2E6447C-L000601](../../api/omarai.py#L601) | 601 | `"        body = bytearray()"` | — |
| [SRC-EEF2E6447C-L000602](../../api/omarai.py#L602) | 602 | `"        timed_out = False"` | — |
| [SRC-EEF2E6447C-L000603](../../api/omarai.py#L603) | 603 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000604](../../api/omarai.py#L604) | 604 | `"            while len(body) < size:"` | — |
| [SRC-EEF2E6447C-L000605](../../api/omarai.py#L605) | 605 | `"                remaining = deadline - time.monotonic()"` | — |
| [SRC-EEF2E6447C-L000606](../../api/omarai.py#L606) | 606 | `"                if remaining <= 0:"` | — |
| [SRC-EEF2E6447C-L000607](../../api/omarai.py#L607) | 607 | `"                    timed_out = True"` | — |
| [SRC-EEF2E6447C-L000608](../../api/omarai.py#L608) | 608 | `"                    break"` | — |
| [SRC-EEF2E6447C-L000609](../../api/omarai.py#L609) | 609 | `"                self.connection.settimeout(min(idle_timeout, remaining))"` | — |
| [SRC-EEF2E6447C-L000610](../../api/omarai.py#L610) | 610 | `"                try:"` | — |
| [SRC-EEF2E6447C-L000611](../../api/omarai.py#L611) | 611 | `"                    # read1 performs at most one underlying read, letting us re-check"` | — |
| [SRC-EEF2E6447C-L000612](../../api/omarai.py#L612) | 612 | `"                    # the absolute deadline between body fragments."` | — |
| [SRC-EEF2E6447C-L000613](../../api/omarai.py#L613) | 613 | `"                    chunk = self.rfile.read1("` | — |
| [SRC-EEF2E6447C-L000614](../../api/omarai.py#L614) | 614 | `"                        min(size - len(body), REQUEST_BODY_READ_CHUNK_BYTES)"` | — |
| [SRC-EEF2E6447C-L000615](../../api/omarai.py#L615) | 615 | `"                    )"` | — |
| [SRC-EEF2E6447C-L000616](../../api/omarai.py#L616) | 616 | `"                except TimeoutError:"` | — |
| [SRC-EEF2E6447C-L000617](../../api/omarai.py#L617) | 617 | `"                    timed_out = True"` | — |
| [SRC-EEF2E6447C-L000618](../../api/omarai.py#L618) | 618 | `"                    break"` | — |
| [SRC-EEF2E6447C-L000619](../../api/omarai.py#L619) | 619 | `"                if not chunk:"` | — |
| [SRC-EEF2E6447C-L000620](../../api/omarai.py#L620) | 620 | `"                    break"` | — |
| [SRC-EEF2E6447C-L000621](../../api/omarai.py#L621) | 621 | `"                body.extend(chunk)"` | — |
| [SRC-EEF2E6447C-L000622](../../api/omarai.py#L622) | 622 | `"        finally:"` | — |
| [SRC-EEF2E6447C-L000623](../../api/omarai.py#L623) | 623 | `"            try:"` | — |
| [SRC-EEF2E6447C-L000624](../../api/omarai.py#L624) | 624 | `"                self.connection.settimeout(previous_timeout)"` | — |
| [SRC-EEF2E6447C-L000625](../../api/omarai.py#L625) | 625 | `"            except OSError:"` | — |
| [SRC-EEF2E6447C-L000626](../../api/omarai.py#L626) | 626 | `"                pass"` | — |
| [SRC-EEF2E6447C-L000627](../../api/omarai.py#L627) | 627 | `""` | — |
| [SRC-EEF2E6447C-L000628](../../api/omarai.py#L628) | 628 | `"        if timed_out:"` | — |
| [SRC-EEF2E6447C-L000629](../../api/omarai.py#L629) | 629 | `"            self.close_connection = True"` | — |
| [SRC-EEF2E6447C-L000630](../../api/omarai.py#L630) | 630 | `"            self.respond(408, {\"error\": \"request body read timed out\"})"` | — |
| [SRC-EEF2E6447C-L000631](../../api/omarai.py#L631) | 631 | `"            return None"` | — |
| [SRC-EEF2E6447C-L000632](../../api/omarai.py#L632) | 632 | `"        if len(body) != size:"` | — |
| [SRC-EEF2E6447C-L000633](../../api/omarai.py#L633) | 633 | `"            self.close_connection = True"` | — |
| [SRC-EEF2E6447C-L000634](../../api/omarai.py#L634) | 634 | `"            self.respond(400, {\"error\": \"incomplete request body\"})"` | — |
| [SRC-EEF2E6447C-L000635](../../api/omarai.py#L635) | 635 | `"            return None"` | — |
| [SRC-EEF2E6447C-L000636](../../api/omarai.py#L636) | 636 | `"        return bytes(body)"` | — |
| [SRC-EEF2E6447C-L000637](../../api/omarai.py#L637) | 637 | `""` | — |
| [SRC-EEF2E6447C-L000638](../../api/omarai.py#L638) | 638 | `"    def end_headers(self):"` | — |
| [SRC-EEF2E6447C-L000639](../../api/omarai.py#L639) | 639 | `"        \"\"\"Apply defensive browser headers to successful and error responses alike.\"\"\""` | — |
| [SRC-EEF2E6447C-L000640](../../api/omarai.py#L640) | 640 | `"        self.send_header(\"X-Content-Type-Options\", \"nosniff\")"` | — |
| [SRC-EEF2E6447C-L000641](../../api/omarai.py#L641) | 641 | `"        self.send_header(\"X-Frame-Options\", \"DENY\")"` | — |
| [SRC-EEF2E6447C-L000642](../../api/omarai.py#L642) | 642 | `"        self.send_header(\"Referrer-Policy\", \"strict-origin-when-cross-origin\")"` | — |
| [SRC-EEF2E6447C-L000643](../../api/omarai.py#L643) | 643 | `"        self.send_header(\"Permissions-Policy\", \"camera=(), microphone=(), geolocation=()\")"` | — |
| [SRC-EEF2E6447C-L000644](../../api/omarai.py#L644) | 644 | `"        self.send_header(\"Content-Security-Policy\", _content_security_policy())"` | — |
| [SRC-EEF2E6447C-L000645](../../api/omarai.py#L645) | 645 | `"        super().end_headers()"` | — |
| [SRC-EEF2E6447C-L000646](../../api/omarai.py#L646) | 646 | `""` | — |
| [SRC-EEF2E6447C-L000647](../../api/omarai.py#L647) | 647 | `"    def respond("` | — |
| [SRC-EEF2E6447C-L000648](../../api/omarai.py#L648) | 648 | `"        self,"` | — |
| [SRC-EEF2E6447C-L000649](../../api/omarai.py#L649) | 649 | `"        status,"` | — |
| [SRC-EEF2E6447C-L000650](../../api/omarai.py#L650) | 650 | `"        payload,"` | — |
| [SRC-EEF2E6447C-L000651](../../api/omarai.py#L651) | 651 | `"        content_type=\"application/json; charset=utf-8\","` | — |
| [SRC-EEF2E6447C-L000652](../../api/omarai.py#L652) | 652 | `"        extra_headers: list[tuple[str, str]] \| None = None,"` | — |
| [SRC-EEF2E6447C-L000653](../../api/omarai.py#L653) | 653 | `"    ):"` | — |
| [SRC-EEF2E6447C-L000654](../../api/omarai.py#L654) | 654 | `"        body = payload.encode() if isinstance(payload, str) else json.dumps(payload, ensure_ascii=False).encode()"` | — |
| [SRC-EEF2E6447C-L000655](../../api/omarai.py#L655) | 655 | `"        self.send_response(status)"` | — |
| [SRC-EEF2E6447C-L000656](../../api/omarai.py#L656) | 656 | `"        self.send_header(\"Content-Type\", content_type)"` | — |
| [SRC-EEF2E6447C-L000657](../../api/omarai.py#L657) | 657 | `"        self.send_header(\"Content-Length\", str(len(body)))"` | — |
| [SRC-EEF2E6447C-L000658](../../api/omarai.py#L658) | 658 | `"        self.send_header(\"Cache-Control\", \"no-store\")"` | — |
| [SRC-EEF2E6447C-L000659](../../api/omarai.py#L659) | 659 | `"        origin = self.headers.get(\"Origin\")"` | — |
| [SRC-EEF2E6447C-L000660](../../api/omarai.py#L660) | 660 | `"        if origin and self._origin_allowed(origin):"` | — |
| [SRC-EEF2E6447C-L000661](../../api/omarai.py#L661) | 661 | `"            self.send_header(\"Access-Control-Allow-Origin\", origin)"` | — |
| [SRC-EEF2E6447C-L000662](../../api/omarai.py#L662) | 662 | `"            self.send_header(\"Vary\", \"Origin\")"` | — |
| [SRC-EEF2E6447C-L000663](../../api/omarai.py#L663) | 663 | `"        for name, value in extra_headers or []:"` | — |
| [SRC-EEF2E6447C-L000664](../../api/omarai.py#L664) | 664 | `"            self.send_header(name, value)"` | — |
| [SRC-EEF2E6447C-L000665](../../api/omarai.py#L665) | 665 | `"        self.end_headers()"` | — |
| [SRC-EEF2E6447C-L000666](../../api/omarai.py#L666) | 666 | `"        self.wfile.write(body)"` | — |
| [SRC-EEF2E6447C-L000667](../../api/omarai.py#L667) | 667 | `""` | — |
| [SRC-EEF2E6447C-L000668](../../api/omarai.py#L668) | 668 | `"    def do_GET(self):"` | — |
| [SRC-EEF2E6447C-L000669](../../api/omarai.py#L669) | 669 | `"        parsed = urlparse(self.path)"` | — |
| [SRC-EEF2E6447C-L000670](../../api/omarai.py#L670) | 670 | `"        if parsed.path == \"/agent\":"` | — |
| [SRC-EEF2E6447C-L000671](../../api/omarai.py#L671) | 671 | `"            if not AGENT_DASHBOARD.exists():"` | — |
| [SRC-EEF2E6447C-L000672](../../api/omarai.py#L672) | 672 | `"                return self.respond(404, {\"error\": \"agent dashboard missing\"})"` | — |
| [SRC-EEF2E6447C-L000673](../../api/omarai.py#L673) | 673 | `"            return self.respond(200, AGENT_DASHBOARD.read_text(encoding=\"utf-8\"), \"text/html; charset=utf-8\")"` | — |
| [SRC-EEF2E6447C-L000674](../../api/omarai.py#L674) | 674 | `"        if parsed.path in {\"/\", \"/workspace\"}:"` | — |
| [SRC-EEF2E6447C-L000675](../../api/omarai.py#L675) | 675 | `"            if not WORKSPACE_DASHBOARD.exists():"` | — |
| [SRC-EEF2E6447C-L000676](../../api/omarai.py#L676) | 676 | `"                return self.respond(404, {\"error\": \"workspace dashboard missing\"})"` | — |
| [SRC-EEF2E6447C-L000677](../../api/omarai.py#L677) | 677 | `"            return self.respond(200, WORKSPACE_DASHBOARD.read_text(encoding=\"utf-8\"), \"text/html; charset=utf-8\")"` | — |
| [SRC-EEF2E6447C-L000678](../../api/omarai.py#L678) | 678 | `"        if parsed.path == \"/leads\":"` | — |
| [SRC-EEF2E6447C-L000679](../../api/omarai.py#L679) | 679 | `"            if not LEADS_DASHBOARD.exists():"` | — |
| [SRC-EEF2E6447C-L000680](../../api/omarai.py#L680) | 680 | `"                return self.respond(404, {\"error\": \"leads dashboard missing\"})"` | — |
| [SRC-EEF2E6447C-L000681](../../api/omarai.py#L681) | 681 | `"            return self.respond(200, LEADS_DASHBOARD.read_text(encoding=\"utf-8\"), \"text/html; charset=utf-8\")"` | — |
| [SRC-EEF2E6447C-L000682](../../api/omarai.py#L682) | 682 | `"        if parsed.path == \"/api/health\":"` | — |
