# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **048**
- سجلات الأسطر: **800**
- النطاق: SRC-3D0A619359-L000205 إلى SRC-6BCB799CEC-L000015
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-3D0A619359 — [tests/test_dashboard_security.py](../../tests/test_dashboard_security.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-3D0A619359-L000205](../../tests/test_dashboard_security.py#L205) | 205 | `"    workspace = Path(__file__).resolve().parents[1] / \"web\" / \"workspace.html\""` | — |
| [SRC-3D0A619359-L000206](../../tests/test_dashboard_security.py#L206) | 206 | `"    html = workspace.read_text(encoding=\"utf-8\")"` | — |
| [SRC-3D0A619359-L000207](../../tests/test_dashboard_security.py#L207) | 207 | `"    discovery = html.split(\"function renderDiscovery(){\", 1)[1].split("` | — |
| [SRC-3D0A619359-L000208](../../tests/test_dashboard_security.py#L208) | 208 | `"        \"\\nfunction renderCurrent(\", 1"` | — |
| [SRC-3D0A619359-L000209](../../tests/test_dashboard_security.py#L209) | 209 | `"    )[0]"` | — |
| [SRC-3D0A619359-L000210](../../tests/test_dashboard_security.py#L210) | 210 | `""` | — |
| [SRC-3D0A619359-L000211](../../tests/test_dashboard_security.py#L211) | 211 | `"    assert 'const savedRun=await api(\"/api/discoveries\"' in discovery"` | — |
| [SRC-3D0A619359-L000212](../../tests/test_dashboard_security.py#L212) | 212 | `"    assert \"state.activeDiscovery=savedRun\" in discovery"` | — |
| [SRC-3D0A619359-L000213](../../tests/test_dashboard_security.py#L213) | 213 | `"    assert \"try{await loadDiscoveryRuns()}catch(refreshError)\" in discovery"` | — |
| [SRC-3D0A619359-L000214](../../tests/test_dashboard_security.py#L214) | 214 | `"    assert \"حُفظت نتيجة البحث، لكن تعذر تحديث سجل العمليات\" in discovery"` | — |
| [SRC-3D0A619359-L000215](../../tests/test_dashboard_security.py#L215) | 215 | `""` | — |
| [SRC-3D0A619359-L000216](../../tests/test_dashboard_security.py#L216) | 216 | `""` | — |
| [SRC-3D0A619359-L000217](../../tests/test_dashboard_security.py#L217) | 217 | `"def test_workspace_exposes_ai_chat_as_secondary_entry_using_agent_api_safely():"` | — |
| [SRC-3D0A619359-L000218](../../tests/test_dashboard_security.py#L218) | 218 | `"    workspace = Path(__file__).resolve().parents[1] / \"web\" / \"workspace.html\""` | — |
| [SRC-3D0A619359-L000219](../../tests/test_dashboard_security.py#L219) | 219 | `"    html = workspace.read_text(encoding=\"utf-8\")"` | — |
| [SRC-3D0A619359-L000220](../../tests/test_dashboard_security.py#L220) | 220 | `"    chat = html.split(\"function chatMessageNode(\", 1)[1].split(\"function renderCurrent(){\", 1)[0]"` | — |
| [SRC-3D0A619359-L000221](../../tests/test_dashboard_security.py#L221) | 221 | `""` | — |
| [SRC-3D0A619359-L000222](../../tests/test_dashboard_security.py#L222) | 222 | `"    assert 'id=\"chatNav\"' in html"` | — |
| [SRC-3D0A619359-L000223](../../tests/test_dashboard_security.py#L223) | 223 | `"    assert '$(\"chatNav\").addEventListener(\"click\",()=>navigate(\"chat\"))' in html"` | — |
| [SRC-3D0A619359-L000224](../../tests/test_dashboard_security.py#L224) | 224 | `"    assert 'state.activeView===\"chat\"' in html"` | — |
| [SRC-3D0A619359-L000225](../../tests/test_dashboard_security.py#L225) | 225 | `"    assert 'api(\"/api/agent\"' in chat"` | — |
| [SRC-3D0A619359-L000226](../../tests/test_dashboard_security.py#L226) | 226 | `"    assert \"history:chat.history.slice(-8)\" in chat"` | — |
| [SRC-3D0A619359-L000227](../../tests/test_dashboard_security.py#L227) | 227 | `"    # Untrusted model/source text must only be rendered with textContent-based helpers."` | — |
| [SRC-3D0A619359-L000228](../../tests/test_dashboard_security.py#L228) | 228 | `"    assert \"innerHTML\" not in chat"` | — |
| [SRC-3D0A619359-L000229](../../tests/test_dashboard_security.py#L229) | 229 | `"    assert \"safeHttp(src.url)\" in chat"` | — |
| [SRC-3D0A619359-L000230](../../tests/test_dashboard_security.py#L230) | 230 | `"    assert \"a.rel=\\\"noopener noreferrer\\\"\" in chat"` | — |
| [SRC-3D0A619359-L000231](../../tests/test_dashboard_security.py#L231) | 231 | `""` | — |
| [SRC-3D0A619359-L000232](../../tests/test_dashboard_security.py#L232) | 232 | `""` | — |
| [SRC-3D0A619359-L000233](../../tests/test_dashboard_security.py#L233) | 233 | `"def test_workspace_clears_chat_at_auth_boundaries_and_ignores_stale_responses():"` | — |
| [SRC-3D0A619359-L000234](../../tests/test_dashboard_security.py#L234) | 234 | `"    workspace = Path(__file__).resolve().parents[1] / \"web\" / \"workspace.html\""` | — |
| [SRC-3D0A619359-L000235](../../tests/test_dashboard_security.py#L235) | 235 | `"    script = workspace.read_text(encoding=\"utf-8\").split(\"<script>\", 1)[1].split(\"</script>\", 1)[0]"` | — |
| [SRC-3D0A619359-L000236](../../tests/test_dashboard_security.py#L236) | 236 | `"    auth = script.split(\"function showAuth(\", 1)[1].split(\"function hideAuth(\", 1)[0]"` | — |
| [SRC-3D0A619359-L000237](../../tests/test_dashboard_security.py#L237) | 237 | `"    chat = script.split(\"async function sendChat(\", 1)[1].split(\"function renderCurrent(\", 1)[0]"` | — |
| [SRC-3D0A619359-L000238](../../tests/test_dashboard_security.py#L238) | 238 | `""` | — |
| [SRC-3D0A619359-L000239](../../tests/test_dashboard_security.py#L239) | 239 | `"    assert \"function clearWorkspaceSession()\" in script"` | — |
| [SRC-3D0A619359-L000240](../../tests/test_dashboard_security.py#L240) | 240 | `"    assert \"clearWorkspaceSession()\" in auth"` | — |
| [SRC-3D0A619359-L000241](../../tests/test_dashboard_security.py#L241) | 241 | `"    assert \"state.authSessionVersion=(state.authSessionVersion\|\|0)+1\" in script"` | — |
| [SRC-3D0A619359-L000242](../../tests/test_dashboard_security.py#L242) | 242 | `"    for field in ("` | — |
| [SRC-3D0A619359-L000243](../../tests/test_dashboard_security.py#L243) | 243 | `"        \"state.role=null\","` | — |
| [SRC-3D0A619359-L000244](../../tests/test_dashboard_security.py#L244) | 244 | `"        \"state.leads=[]\","` | — |
| [SRC-3D0A619359-L000245](../../tests/test_dashboard_security.py#L245) | 245 | `"        \"state.profiles=[]\","` | — |
| [SRC-3D0A619359-L000246](../../tests/test_dashboard_security.py#L246) | 246 | `"        \"state.discoveryRuns=[]\","` | — |
| [SRC-3D0A619359-L000247](../../tests/test_dashboard_security.py#L247) | 247 | `"        \"state.loadWarnings=[]\","` | — |
| [SRC-3D0A619359-L000248](../../tests/test_dashboard_security.py#L248) | 248 | `"        \"state.activeDiscovery=null\","` | — |
| [SRC-3D0A619359-L000249](../../tests/test_dashboard_security.py#L249) | 249 | `"        \"state.activeProfileId=null\","` | — |
| [SRC-3D0A619359-L000250](../../tests/test_dashboard_security.py#L250) | 250 | `"        \"state.analysis=null\","` | — |
| [SRC-3D0A619359-L000251](../../tests/test_dashboard_security.py#L251) | 251 | `"    ):"` | — |
| [SRC-3D0A619359-L000252](../../tests/test_dashboard_security.py#L252) | 252 | `"        assert field in script"` | — |
| [SRC-3D0A619359-L000253](../../tests/test_dashboard_security.py#L253) | 253 | `"    assert 'replaceChildren(emptyState(\"مساحة العمل مقفلة\"' in script"` | — |
| [SRC-3D0A619359-L000254](../../tests/test_dashboard_security.py#L254) | 254 | `"    assert \"function clearChatSession()\" in script"` | — |
| [SRC-3D0A619359-L000255](../../tests/test_dashboard_security.py#L255) | 255 | `"    assert \"clearChatSession()\" in script"` | — |
| [SRC-3D0A619359-L000256](../../tests/test_dashboard_security.py#L256) | 256 | `"    assert \"chat.messages=[]\" in script"` | — |
| [SRC-3D0A619359-L000257](../../tests/test_dashboard_security.py#L257) | 257 | `"    assert \"chat.history=[]\" in script"` | — |
| [SRC-3D0A619359-L000258](../../tests/test_dashboard_security.py#L258) | 258 | `"    assert 'chat.mode=\"deep\"' in script"` | — |
| [SRC-3D0A619359-L000259](../../tests/test_dashboard_security.py#L259) | 259 | `"    assert \"chat.sessionVersion=(chat.sessionVersion\|\|0)+1\" in script"` | — |
| [SRC-3D0A619359-L000260](../../tests/test_dashboard_security.py#L260) | 260 | `"    assert \"function advanceWorkspaceSessionVersion()\" in script"` | — |
| [SRC-3D0A619359-L000261](../../tests/test_dashboard_security.py#L261) | 261 | `"    login = script.split('$(\"loginForm\").addEventListener(\"submit\"', 1)[1].split('$(\"logoutButton\").addEventListener', 1)[0]"` | — |
| [SRC-3D0A619359-L000262](../../tests/test_dashboard_security.py#L262) | 262 | `"    assert \"advanceWorkspaceSessionVersion()\" in login"` | — |
| [SRC-3D0A619359-L000263](../../tests/test_dashboard_security.py#L263) | 263 | `"    api = script.split(\"async function api(\", 1)[1].split(\"function clearChatSession(\", 1)[0]"` | — |
| [SRC-3D0A619359-L000264](../../tests/test_dashboard_security.py#L264) | 264 | `"    assert \"const requestSessionVersion=state.authSessionVersion\" in api"` | — |
| [SRC-3D0A619359-L000265](../../tests/test_dashboard_security.py#L265) | 265 | `"    assert \"if(state.authSessionVersion!==requestSessionVersion)\" in api"` | — |
| [SRC-3D0A619359-L000266](../../tests/test_dashboard_security.py#L266) | 266 | `"    assert \"const requestSessionVersion=chat.sessionVersion\" in chat"` | — |
| [SRC-3D0A619359-L000267](../../tests/test_dashboard_security.py#L267) | 267 | `"    assert \"if(state.chat.sessionVersion!==requestSessionVersion)return;\" in chat"` | — |
| [SRC-3D0A619359-L000268](../../tests/test_dashboard_security.py#L268) | 268 | `"    assert \"if(state.chat.sessionVersion===requestSessionVersion)\" in chat"` | — |
| [SRC-3D0A619359-L000269](../../tests/test_dashboard_security.py#L269) | 269 | `""` | — |
| [SRC-3D0A619359-L000270](../../tests/test_dashboard_security.py#L270) | 270 | `""` | — |
| [SRC-3D0A619359-L000271](../../tests/test_dashboard_security.py#L271) | 271 | `"def test_ai_chat_frontends_abort_stalled_requests_with_bounded_timeout():"` | — |
| [SRC-3D0A619359-L000272](../../tests/test_dashboard_security.py#L272) | 272 | `"    root = Path(__file__).resolve().parents[1]"` | — |
| [SRC-3D0A619359-L000273](../../tests/test_dashboard_security.py#L273) | 273 | `"    agent = (root / \"web\" / \"agent.html\").read_text(encoding=\"utf-8\")"` | — |
| [SRC-3D0A619359-L000274](../../tests/test_dashboard_security.py#L274) | 274 | `"    agent_script = agent.split(\"<script>\", 1)[1].split(\"</script>\", 1)[0]"` | — |
| [SRC-3D0A619359-L000275](../../tests/test_dashboard_security.py#L275) | 275 | `"    agent_ask = agent_script.split(\"async function ask(value){\", 1)[1].split("` | — |
| [SRC-3D0A619359-L000276](../../tests/test_dashboard_security.py#L276) | 276 | `"        \"async function runDiagnostics()\", 1"` | — |
| [SRC-3D0A619359-L000277](../../tests/test_dashboard_security.py#L277) | 277 | `"    )[0]"` | — |
| [SRC-3D0A619359-L000278](../../tests/test_dashboard_security.py#L278) | 278 | `""` | — |
| [SRC-3D0A619359-L000279](../../tests/test_dashboard_security.py#L279) | 279 | `"    workspace = (root / \"web\" / \"workspace.html\").read_text(encoding=\"utf-8\")"` | — |
| [SRC-3D0A619359-L000280](../../tests/test_dashboard_security.py#L280) | 280 | `"    workspace_script = workspace.split(\"<script>\", 1)[1].split(\"</script>\", 1)[0]"` | — |
| [SRC-3D0A619359-L000281](../../tests/test_dashboard_security.py#L281) | 281 | `"    api = workspace_script.split(\"async function api(\", 1)[1].split("` | — |
| [SRC-3D0A619359-L000282](../../tests/test_dashboard_security.py#L282) | 282 | `"        \"function clearChatSession(\", 1"` | — |
| [SRC-3D0A619359-L000283](../../tests/test_dashboard_security.py#L283) | 283 | `"    )[0]"` | — |
| [SRC-3D0A619359-L000284](../../tests/test_dashboard_security.py#L284) | 284 | `"    chat = workspace_script.split(\"async function sendChat(){\", 1)[1].split("` | — |
| [SRC-3D0A619359-L000285](../../tests/test_dashboard_security.py#L285) | 285 | `"        \"function renderCurrent(){\", 1"` | — |
| [SRC-3D0A619359-L000286](../../tests/test_dashboard_security.py#L286) | 286 | `"    )[0]"` | — |
| [SRC-3D0A619359-L000287](../../tests/test_dashboard_security.py#L287) | 287 | `""` | — |
| [SRC-3D0A619359-L000288](../../tests/test_dashboard_security.py#L288) | 288 | `"    assert \"signal:opts.signal\" in api"` | — |
| [SRC-3D0A619359-L000289](../../tests/test_dashboard_security.py#L289) | 289 | `"    for request in (agent_ask, chat):"` | — |
| [SRC-3D0A619359-L000290](../../tests/test_dashboard_security.py#L290) | 290 | `"        assert \"new AbortController()\" in request"` | — |
| [SRC-3D0A619359-L000291](../../tests/test_dashboard_security.py#L291) | 291 | `"        assert \"window.setTimeout\" in request"` | — |
| [SRC-3D0A619359-L000292](../../tests/test_dashboard_security.py#L292) | 292 | `"        assert \"135000\" in request"` | — |
| [SRC-3D0A619359-L000293](../../tests/test_dashboard_security.py#L293) | 293 | `"        assert \"requestTimedOut\" in request"` | — |
| [SRC-3D0A619359-L000294](../../tests/test_dashboard_security.py#L294) | 294 | `"        assert \"controller.abort()\" in request"` | — |
| [SRC-3D0A619359-L000295](../../tests/test_dashboard_security.py#L295) | 295 | `"        assert \"window.clearTimeout(timeoutId)\" in request"` | — |
| [SRC-3D0A619359-L000296](../../tests/test_dashboard_security.py#L296) | 296 | `"        assert \"انتهى وقت انتظار الواجهة بعد 135 ثانية\" in request"` | — |
| [SRC-3D0A619359-L000297](../../tests/test_dashboard_security.py#L297) | 297 | `""` | — |
| [SRC-3D0A619359-L000298](../../tests/test_dashboard_security.py#L298) | 298 | `""` | — |
| [SRC-3D0A619359-L000299](../../tests/test_dashboard_security.py#L299) | 299 | `"def test_workspace_distinguishes_saved_records_from_refresh_failures():"` | — |
| [SRC-3D0A619359-L000300](../../tests/test_dashboard_security.py#L300) | 300 | `"    workspace = Path(__file__).resolve().parents[1] / \"web\" / \"workspace.html\""` | — |
| [SRC-3D0A619359-L000301](../../tests/test_dashboard_security.py#L301) | 301 | `"    script = workspace.read_text(encoding=\"utf-8\").split(\"<script>\", 1)[1].split("` | — |
| [SRC-3D0A619359-L000302](../../tests/test_dashboard_security.py#L302) | 302 | `"        \"</script>\", 1"` | — |
| [SRC-3D0A619359-L000303](../../tests/test_dashboard_security.py#L303) | 303 | `"    )[0]"` | — |
| [SRC-3D0A619359-L000304](../../tests/test_dashboard_security.py#L304) | 304 | `""` | — |
| [SRC-3D0A619359-L000305](../../tests/test_dashboard_security.py#L305) | 305 | `"    signals = script.split(\"function renderSignals(){\", 1)[1].split("` | — |
| [SRC-3D0A619359-L000306](../../tests/test_dashboard_security.py#L306) | 306 | `"        \"function drawSignalRows(\", 1"` | — |
| [SRC-3D0A619359-L000307](../../tests/test_dashboard_security.py#L307) | 307 | `"    )[0]"` | — |
| [SRC-3D0A619359-L000308](../../tests/test_dashboard_security.py#L308) | 308 | `"    signal_form = script.split(\"function createSignalForm(){\", 1)[1].split("` | — |
| [SRC-3D0A619359-L000309](../../tests/test_dashboard_security.py#L309) | 309 | `"        \"function renderPipeline(){\", 1"` | — |
| [SRC-3D0A619359-L000310](../../tests/test_dashboard_security.py#L310) | 310 | `"    )[0]"` | — |
| [SRC-3D0A619359-L000311](../../tests/test_dashboard_security.py#L311) | 311 | `"    profile = script.split(\"function renderProductProfile(){\", 1)[1].split("` | — |
| [SRC-3D0A619359-L000312](../../tests/test_dashboard_security.py#L312) | 312 | `"        \"function renderDiscoveryRun(\", 1"` | — |
| [SRC-3D0A619359-L000313](../../tests/test_dashboard_security.py#L313) | 313 | `"    )[0]"` | — |
| [SRC-3D0A619359-L000314](../../tests/test_dashboard_security.py#L314) | 314 | `"    discovery_result = script.split(\"function renderDiscoveryRun(run){\", 1)[1].split("` | — |
| [SRC-3D0A619359-L000315](../../tests/test_dashboard_security.py#L315) | 315 | `"        \"function renderDiscovery(){\", 1"` | — |
| [SRC-3D0A619359-L000316](../../tests/test_dashboard_security.py#L316) | 316 | `"    )[0]"` | — |
| [SRC-3D0A619359-L000317](../../tests/test_dashboard_security.py#L317) | 317 | `""` | — |
| [SRC-3D0A619359-L000318](../../tests/test_dashboard_security.py#L318) | 318 | `"    assert \"تعذر تحديث إشارات الطلب. البيانات المعروضة هي آخر نسخة تم تحميلها.\" in signals"` | — |
| [SRC-3D0A619359-L000319](../../tests/test_dashboard_security.py#L319) | 319 | `"    assert \"تم حفظ الإشارة، لكن تعذر تحديث صندوق الإشارات.\" in signal_form"` | — |
| [SRC-3D0A619359-L000320](../../tests/test_dashboard_security.py#L320) | 320 | `"    assert \"تم حفظ ملف المنتج والسوق، لكن تعذر تحديث قائمة الملفات المحفوظة.\" in profile"` | — |
| [SRC-3D0A619359-L000321](../../tests/test_dashboard_security.py#L321) | 321 | `"    assert \"تم حفظ الإشارة، لكن تعذر تحديث صندوق الإشارات.\" in discovery_result"` | — |
| [SRC-3D0A619359-L000322](../../tests/test_dashboard_security.py#L322) | 322 | `"    assert \"let refreshWarning=\\\"\\\"\" in signal_form"` | — |
| [SRC-3D0A619359-L000323](../../tests/test_dashboard_security.py#L323) | 323 | `"    assert \"let refreshWarning=\\\"\\\"\" in profile"` | — |
| [SRC-3D0A619359-L000324](../../tests/test_dashboard_security.py#L324) | 324 | `"    assert \"let refreshWarning=\\\"\\\"\" in discovery_result"` | — |
| [SRC-3D0A619359-L000325](../../tests/test_dashboard_security.py#L325) | 325 | `"    assert 'const response=await api(\"/api/leads\"' in signal_form"` | — |
| [SRC-3D0A619359-L000326](../../tests/test_dashboard_security.py#L326) | 326 | `"    assert 'const result=await api(\"/api/product-profiles\"' in profile"` | — |
| [SRC-3D0A619359-L000327](../../tests/test_dashboard_security.py#L327) | 327 | `"    assert 'api(\"/api/discoveries/\"+encodeURIComponent(run.id)+\"/signals/\"' in discovery_result"` | — |
## اختبارات

### FILE-29A9CD43D1 — [tests/test_dialogue_context_pipeline.py](../../tests/test_dialogue_context_pipeline.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-29A9CD43D1-L000001](../../tests/test_dialogue_context_pipeline.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-29A9CD43D1-L000002](../../tests/test_dialogue_context_pipeline.py#L2) | 2 | `""` | — |
| [SRC-29A9CD43D1-L000003](../../tests/test_dialogue_context_pipeline.py#L3) | 3 | `"import json"` | — |
| [SRC-29A9CD43D1-L000004](../../tests/test_dialogue_context_pipeline.py#L4) | 4 | `"from typing import Any"` | — |
| [SRC-29A9CD43D1-L000005](../../tests/test_dialogue_context_pipeline.py#L5) | 5 | `""` | — |
| [SRC-29A9CD43D1-L000006](../../tests/test_dialogue_context_pipeline.py#L6) | 6 | `"import pytest"` | — |
| [SRC-29A9CD43D1-L000007](../../tests/test_dialogue_context_pipeline.py#L7) | 7 | `""` | — |
| [SRC-29A9CD43D1-L000008](../../tests/test_dialogue_context_pipeline.py#L8) | 8 | `"from agents.research import evidence_signal_report"` | — |
| [SRC-29A9CD43D1-L000009](../../tests/test_dialogue_context_pipeline.py#L9) | 9 | `"from agents.dialogue_state import might_be_context_dependent"` | — |
| [SRC-29A9CD43D1-L000010](../../tests/test_dialogue_context_pipeline.py#L10) | 10 | `"from agents.web_agent import WebAgent"` | — |
| [SRC-29A9CD43D1-L000011](../../tests/test_dialogue_context_pipeline.py#L11) | 11 | `""` | — |
| [SRC-29A9CD43D1-L000012](../../tests/test_dialogue_context_pipeline.py#L12) | 12 | `""` | — |
| [SRC-29A9CD43D1-L000013](../../tests/test_dialogue_context_pipeline.py#L13) | 13 | `"def _source(domain: str, queries: list[str]) -> dict[str, Any]:"` | — |
| [SRC-29A9CD43D1-L000014](../../tests/test_dialogue_context_pipeline.py#L14) | 14 | `"    return {"` | — |
| [SRC-29A9CD43D1-L000015](../../tests/test_dialogue_context_pipeline.py#L15) | 15 | `"        \"title\": \"iPhone 17 256GB international warranty coverage in Egypt\","` | — |
| [SRC-29A9CD43D1-L000016](../../tests/test_dialogue_context_pipeline.py#L16) | 16 | `"        \"url\": f\"https://{domain}/iphone-warranty\","` | — |
| [SRC-29A9CD43D1-L000017](../../tests/test_dialogue_context_pipeline.py#L17) | 17 | `"        \"snippet\": \"Warranty coverage and service policy for iPhone 17 in Egypt.\","` | — |
| [SRC-29A9CD43D1-L000018](../../tests/test_dialogue_context_pipeline.py#L18) | 18 | `"        \"page_text\": \"Warranty coverage and service policy for iPhone 17 in Egypt.\","` | — |
| [SRC-29A9CD43D1-L000019](../../tests/test_dialogue_context_pipeline.py#L19) | 19 | `"        \"page_fetched\": True,"` | — |
| [SRC-29A9CD43D1-L000020](../../tests/test_dialogue_context_pipeline.py#L20) | 20 | `"        \"providers\": [\"test_search\"],"` | — |
| [SRC-29A9CD43D1-L000021](../../tests/test_dialogue_context_pipeline.py#L21) | 21 | `"        \"queries\": list(queries),"` | — |
| [SRC-29A9CD43D1-L000022](../../tests/test_dialogue_context_pipeline.py#L22) | 22 | `"        \"domain\": domain,"` | — |
| [SRC-29A9CD43D1-L000023](../../tests/test_dialogue_context_pipeline.py#L23) | 23 | `"        \"source_class\": \"general\","` | — |
| [SRC-29A9CD43D1-L000024](../../tests/test_dialogue_context_pipeline.py#L24) | 24 | `"        \"platform\": \"web\","` | — |
| [SRC-29A9CD43D1-L000025](../../tests/test_dialogue_context_pipeline.py#L25) | 25 | `"        \"published_at\": \"\","` | — |
| [SRC-29A9CD43D1-L000026](../../tests/test_dialogue_context_pipeline.py#L26) | 26 | `"        \"rank_score\": 1.0,"` | — |
| [SRC-29A9CD43D1-L000027](../../tests/test_dialogue_context_pipeline.py#L27) | 27 | `"    }"` | — |
| [SRC-29A9CD43D1-L000028](../../tests/test_dialogue_context_pipeline.py#L28) | 28 | `""` | — |
| [SRC-29A9CD43D1-L000029](../../tests/test_dialogue_context_pipeline.py#L29) | 29 | `""` | — |
| [SRC-29A9CD43D1-L000030](../../tests/test_dialogue_context_pipeline.py#L30) | 30 | `"def _report(plan: dict[str, Any], sources: list[dict[str, Any]]) -> dict[str, Any]:"` | — |
| [SRC-29A9CD43D1-L000031](../../tests/test_dialogue_context_pipeline.py#L31) | 31 | `"    return {"` | — |
| [SRC-29A9CD43D1-L000032](../../tests/test_dialogue_context_pipeline.py#L32) | 32 | `"        \"queries_planned\": len(plan.get(\"queries\", [])),"` | — |
| [SRC-29A9CD43D1-L000033](../../tests/test_dialogue_context_pipeline.py#L33) | 33 | `"        \"queries_attempted\": len(plan.get(\"queries\", [])),"` | — |
| [SRC-29A9CD43D1-L000034](../../tests/test_dialogue_context_pipeline.py#L34) | 34 | `"        \"queries_attempted_known\": True,"` | — |
| [SRC-29A9CD43D1-L000035](../../tests/test_dialogue_context_pipeline.py#L35) | 35 | `"        \"search_attempted\": True,"` | — |
| [SRC-29A9CD43D1-L000036](../../tests/test_dialogue_context_pipeline.py#L36) | 36 | `"        \"search_outcome\": \"attempted_with_usable_sources\","` | — |
| [SRC-29A9CD43D1-L000037](../../tests/test_dialogue_context_pipeline.py#L37) | 37 | `"        \"query_results\": [],"` | — |
| [SRC-29A9CD43D1-L000038](../../tests/test_dialogue_context_pipeline.py#L38) | 38 | `"        \"unique_sources\": len(sources),"` | — |
| [SRC-29A9CD43D1-L000039](../../tests/test_dialogue_context_pipeline.py#L39) | 39 | `"        \"pages_fetched\": len(sources),"` | — |
| [SRC-29A9CD43D1-L000040](../../tests/test_dialogue_context_pipeline.py#L40) | 40 | `"        \"providers_used\": [\"test_search\"],"` | — |
| [SRC-29A9CD43D1-L000041](../../tests/test_dialogue_context_pipeline.py#L41) | 41 | `"        \"provider_counts\": {\"test_search\": len(sources)},"` | — |
| [SRC-29A9CD43D1-L000042](../../tests/test_dialogue_context_pipeline.py#L42) | 42 | `"        \"platform_counts\": {\"web\": len(sources)},"` | — |
| [SRC-29A9CD43D1-L000043](../../tests/test_dialogue_context_pipeline.py#L43) | 43 | `"        \"social_direct_results\": 0,"` | — |
| [SRC-29A9CD43D1-L000044](../../tests/test_dialogue_context_pipeline.py#L44) | 44 | `"        \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-29A9CD43D1-L000045](../../tests/test_dialogue_context_pipeline.py#L45) | 45 | `"        \"planning_method\": plan.get(\"planning_method\", \"test\"),"` | — |
| [SRC-29A9CD43D1-L000046](../../tests/test_dialogue_context_pipeline.py#L46) | 46 | `"        \"evidence_signals\": evidence_signal_report(sources),"` | — |
| [SRC-29A9CD43D1-L000047](../../tests/test_dialogue_context_pipeline.py#L47) | 47 | `"    }"` | — |
| [SRC-29A9CD43D1-L000048](../../tests/test_dialogue_context_pipeline.py#L48) | 48 | `""` | — |
| [SRC-29A9CD43D1-L000049](../../tests/test_dialogue_context_pipeline.py#L49) | 49 | `""` | — |
| [SRC-29A9CD43D1-L000050](../../tests/test_dialogue_context_pipeline.py#L50) | 50 | `"def _semantic_context(*, needs_clarification: bool = False) -> dict[str, Any]:"` | — |
| [SRC-29A9CD43D1-L000051](../../tests/test_dialogue_context_pipeline.py#L51) | 51 | `"    return {"` | — |
| [SRC-29A9CD43D1-L000052](../../tests/test_dialogue_context_pipeline.py#L52) | 52 | `"        \"resolved_question\": ("` | — |
| [SRC-29A9CD43D1-L000053](../../tests/test_dialogue_context_pipeline.py#L53) | 53 | `"            \"هل الضمان الدولي لهاتف iPhone 17 سعة 256 جيجابايت الذي اشتريته \""` | — |
| [SRC-29A9CD43D1-L000054](../../tests/test_dialogue_context_pipeline.py#L54) | 54 | `"            \"في مصر يغطي الصيانة داخل مصر؟\""` | — |
| [SRC-29A9CD43D1-L000055](../../tests/test_dialogue_context_pipeline.py#L55) | 55 | `"        ),"` | — |
| [SRC-29A9CD43D1-L000056](../../tests/test_dialogue_context_pipeline.py#L56) | 56 | `"        \"intent\": \"current_information\","` | — |
| [SRC-29A9CD43D1-L000057](../../tests/test_dialogue_context_pipeline.py#L57) | 57 | `"        \"topic\": \"تغطية الضمان\","` | — |
| [SRC-29A9CD43D1-L000058](../../tests/test_dialogue_context_pipeline.py#L58) | 58 | `"        \"entities\": [\"iPhone 17\"],"` | — |
| [SRC-29A9CD43D1-L000059](../../tests/test_dialogue_context_pipeline.py#L59) | 59 | `"        \"slots\": {"` | — |
| [SRC-29A9CD43D1-L000060](../../tests/test_dialogue_context_pipeline.py#L60) | 60 | `"            \"product\": \"iPhone 17\","` | — |
| [SRC-29A9CD43D1-L000061](../../tests/test_dialogue_context_pipeline.py#L61) | 61 | `"            \"capacity\": \"256 جيجابايت\","` | — |
| [SRC-29A9CD43D1-L000062](../../tests/test_dialogue_context_pipeline.py#L62) | 62 | `"            \"country\": \"مصر\","` | — |
| [SRC-29A9CD43D1-L000063](../../tests/test_dialogue_context_pipeline.py#L63) | 63 | `"            \"aspect\": \"الضمان الدولي والصيانة داخل مصر\","` | — |
| [SRC-29A9CD43D1-L000064](../../tests/test_dialogue_context_pipeline.py#L64) | 64 | `"        },"` | — |
| [SRC-29A9CD43D1-L000065](../../tests/test_dialogue_context_pipeline.py#L65) | 65 | `"        \"changed_slots\": [\"aspect\"],"` | — |
| [SRC-29A9CD43D1-L000066](../../tests/test_dialogue_context_pipeline.py#L66) | 66 | `"        \"is_follow_up\": True,"` | — |
| [SRC-29A9CD43D1-L000067](../../tests/test_dialogue_context_pipeline.py#L67) | 67 | `"        \"topic_shift\": False,"` | — |
| [SRC-29A9CD43D1-L000068](../../tests/test_dialogue_context_pipeline.py#L68) | 68 | `"        \"needs_web\": True,"` | — |
| [SRC-29A9CD43D1-L000069](../../tests/test_dialogue_context_pipeline.py#L69) | 69 | `"        \"research_depth\": \"standard\","` | — |
| [SRC-29A9CD43D1-L000070](../../tests/test_dialogue_context_pipeline.py#L70) | 70 | `"        \"needs_clarification\": needs_clarification,"` | — |
| [SRC-29A9CD43D1-L000071](../../tests/test_dialogue_context_pipeline.py#L71) | 71 | `"        \"clarification_question\": ("` | — |
| [SRC-29A9CD43D1-L000072](../../tests/test_dialogue_context_pipeline.py#L72) | 72 | `"            \"تقصد ضمان أي هاتف تحديدًا، أم تريد مقارنة ضمان الهاتفين؟\""` | — |
| [SRC-29A9CD43D1-L000073](../../tests/test_dialogue_context_pipeline.py#L73) | 73 | `"            if needs_clarification else \"\""` | — |
| [SRC-29A9CD43D1-L000074](../../tests/test_dialogue_context_pipeline.py#L74) | 74 | `"        ),"` | — |
| [SRC-29A9CD43D1-L000075](../../tests/test_dialogue_context_pipeline.py#L75) | 75 | `"        \"unresolved_references\": [\"الضمان\"] if needs_clarification else [],"` | — |
| [SRC-29A9CD43D1-L000076](../../tests/test_dialogue_context_pipeline.py#L76) | 76 | `"        \"resolution_basis\": \"history_inferred\","` | — |
| [SRC-29A9CD43D1-L000077](../../tests/test_dialogue_context_pipeline.py#L77) | 77 | `"        \"confidence_band\": \"medium\","` | — |
| [SRC-29A9CD43D1-L000078](../../tests/test_dialogue_context_pipeline.py#L78) | 78 | `"    }"` | — |
| [SRC-29A9CD43D1-L000079](../../tests/test_dialogue_context_pipeline.py#L79) | 79 | `""` | — |
| [SRC-29A9CD43D1-L000080](../../tests/test_dialogue_context_pipeline.py#L80) | 80 | `""` | — |
| [SRC-29A9CD43D1-L000081](../../tests/test_dialogue_context_pipeline.py#L81) | 81 | `"def test_semantic_context_probe_routes_natural_followup_to_search_and_answer("` | — |
| [SRC-29A9CD43D1-L000082](../../tests/test_dialogue_context_pipeline.py#L82) | 82 | `"    monkeypatch: pytest.MonkeyPatch,"` | — |
| [SRC-29A9CD43D1-L000083](../../tests/test_dialogue_context_pipeline.py#L83) | 83 | `") -> None:"` | — |
| [SRC-29A9CD43D1-L000084](../../tests/test_dialogue_context_pipeline.py#L84) | 84 | `"    agent = WebAgent()"` | — |
| [SRC-29A9CD43D1-L000085](../../tests/test_dialogue_context_pipeline.py#L85) | 85 | `"    agent.api_key = \"test-key\"  # All model responses are mocked; no provider call is made."` | — |
| [SRC-29A9CD43D1-L000086](../../tests/test_dialogue_context_pipeline.py#L86) | 86 | `"    history = ["` | — |
| [SRC-29A9CD43D1-L000087](../../tests/test_dialogue_context_pipeline.py#L87) | 87 | `"        {\"role\": \"user\", \"content\": \"اشتريت iPhone 17 النسخة الأساسية سعة 256 جيجابايت من مصر.\"},"` | — |
| [SRC-29A9CD43D1-L000088](../../tests/test_dialogue_context_pipeline.py#L88) | 88 | `"        {\"role\": \"assistant\", \"content\": \"نتحدث عن نسخة iPhone 17 سعة 256 جيجابايت في مصر.\"},"` | — |
| [SRC-29A9CD43D1-L000089](../../tests/test_dialogue_context_pipeline.py#L89) | 89 | `"    ]"` | — |
| [SRC-29A9CD43D1-L000090](../../tests/test_dialogue_context_pipeline.py#L90) | 90 | `"    context = _semantic_context()"` | — |
| [SRC-29A9CD43D1-L000091](../../tests/test_dialogue_context_pipeline.py#L91) | 91 | `"    seen: dict[str, Any] = {\"model_prompts\": []}"` | — |
| [SRC-29A9CD43D1-L000092](../../tests/test_dialogue_context_pipeline.py#L92) | 92 | `""` | — |
| [SRC-29A9CD43D1-L000093](../../tests/test_dialogue_context_pipeline.py#L93) | 93 | `"    def mocked_completion(messages, **kwargs):"` | — |
| [SRC-29A9CD43D1-L000094](../../tests/test_dialogue_context_pipeline.py#L94) | 94 | `"        system_prompt = messages[0][\"content\"]"` | — |
| [SRC-29A9CD43D1-L000095](../../tests/test_dialogue_context_pipeline.py#L95) | 95 | `"        seen[\"model_prompts\"].append(system_prompt)"` | — |
| [SRC-29A9CD43D1-L000096](../../tests/test_dialogue_context_pipeline.py#L96) | 96 | `"        if \"أنت محلل سياق حواري\" in system_prompt:"` | — |
| [SRC-29A9CD43D1-L000097](../../tests/test_dialogue_context_pipeline.py#L97) | 97 | `"            assert \"تعامل معها كتصحيح للكيان/قيمة القيد\" in system_prompt"` | — |
| [SRC-29A9CD43D1-L000098](../../tests/test_dialogue_context_pipeline.py#L98) | 98 | `"            assert \"سجّل اسم القيد المعدل في changed_slots\" in system_prompt"` | — |
| [SRC-29A9CD43D1-L000099](../../tests/test_dialogue_context_pipeline.py#L99) | 99 | `"            assert \"طب وسامسونج S24\" in system_prompt"` | — |
| [SRC-29A9CD43D1-L000100](../../tests/test_dialogue_context_pipeline.py#L100) | 100 | `"            assert \"لا تعتبر اسم منتج بديل وحده موضوعًا مستقلًا\" in system_prompt"` | — |
| [SRC-29A9CD43D1-L000101](../../tests/test_dialogue_context_pipeline.py#L101) | 101 | `"            return json.dumps(context, ensure_ascii=False)"` | — |
| [SRC-29A9CD43D1-L000102](../../tests/test_dialogue_context_pipeline.py#L102) | 102 | `"        if \"أنت مخطط بحث ومحلل دلالي حواري\" in system_prompt:"` | — |
| [SRC-29A9CD43D1-L000103](../../tests/test_dialogue_context_pipeline.py#L103) | 103 | `"            return json.dumps("` | — |
| [SRC-29A9CD43D1-L000104](../../tests/test_dialogue_context_pipeline.py#L104) | 104 | `"                {"` | — |
| [SRC-29A9CD43D1-L000105](../../tests/test_dialogue_context_pipeline.py#L105) | 105 | `"                    \"queries\": ["` | — |
| [SRC-29A9CD43D1-L000106](../../tests/test_dialogue_context_pipeline.py#L106) | 106 | `"                        \"iPhone 17 256GB الضمان الدولي في مصر تغطية الصيانة warranty Egypt\""` | — |
| [SRC-29A9CD43D1-L000107](../../tests/test_dialogue_context_pipeline.py#L107) | 107 | `"                    ],"` | — |
| [SRC-29A9CD43D1-L000108](../../tests/test_dialogue_context_pipeline.py#L108) | 108 | `"                    \"direct_urls\": [],"` | — |
| [SRC-29A9CD43D1-L000109](../../tests/test_dialogue_context_pipeline.py#L109) | 109 | `"                    \"social_focus\": False,"` | — |
| [SRC-29A9CD43D1-L000110](../../tests/test_dialogue_context_pipeline.py#L110) | 110 | `"                    \"freshness\": \"current\","` | — |
| [SRC-29A9CD43D1-L000111](../../tests/test_dialogue_context_pipeline.py#L111) | 111 | `"                    \"depth\": \"standard\","` | — |
| [SRC-29A9CD43D1-L000112](../../tests/test_dialogue_context_pipeline.py#L112) | 112 | `"                    \"platforms\": [],"` | — |
| [SRC-29A9CD43D1-L000113](../../tests/test_dialogue_context_pipeline.py#L113) | 113 | `"                    \"dialogue_context\": context,"` | — |
| [SRC-29A9CD43D1-L000114](../../tests/test_dialogue_context_pipeline.py#L114) | 114 | `"                },"` | — |
| [SRC-29A9CD43D1-L000115](../../tests/test_dialogue_context_pipeline.py#L115) | 115 | `"                ensure_ascii=False,"` | — |
| [SRC-29A9CD43D1-L000116](../../tests/test_dialogue_context_pipeline.py#L116) | 116 | `"            )"` | — |
| [SRC-29A9CD43D1-L000117](../../tests/test_dialogue_context_pipeline.py#L117) | 117 | `"        pytest.fail(\"Unexpected model prompt in mocked offline test\")"` | — |
| [SRC-29A9CD43D1-L000118](../../tests/test_dialogue_context_pipeline.py#L118) | 118 | `""` | — |
| [SRC-29A9CD43D1-L000119](../../tests/test_dialogue_context_pipeline.py#L119) | 119 | `"    monkeypatch.setattr(agent, \"_request_completion\", mocked_completion)"` | — |
| [SRC-29A9CD43D1-L000120](../../tests/test_dialogue_context_pipeline.py#L120) | 120 | `"    seen[\"generated_question\"] = None"` | — |
| [SRC-29A9CD43D1-L000121](../../tests/test_dialogue_context_pipeline.py#L121) | 121 | `"    seen[\"reviewed_question\"] = None"` | — |
| [SRC-29A9CD43D1-L000122](../../tests/test_dialogue_context_pipeline.py#L122) | 122 | `""` | — |
| [SRC-29A9CD43D1-L000123](../../tests/test_dialogue_context_pipeline.py#L123) | 123 | `"    def collect(plan):"` | — |
| [SRC-29A9CD43D1-L000124](../../tests/test_dialogue_context_pipeline.py#L124) | 124 | `"        seen[\"plan\"] = dict(plan)"` | — |
| [SRC-29A9CD43D1-L000125](../../tests/test_dialogue_context_pipeline.py#L125) | 125 | `"        sources = [_source(\"example.com\", plan[\"queries\"]), _source(\"example.net\", plan[\"queries\"])]"` | — |
| [SRC-29A9CD43D1-L000126](../../tests/test_dialogue_context_pipeline.py#L126) | 126 | `"        return sources, [], _report(plan, sources)"` | — |
| [SRC-29A9CD43D1-L000127](../../tests/test_dialogue_context_pipeline.py#L127) | 127 | `""` | — |
| [SRC-29A9CD43D1-L000128](../../tests/test_dialogue_context_pipeline.py#L128) | 128 | `"    def generate(resolved_question, *args, **kwargs):"` | — |
| [SRC-29A9CD43D1-L000129](../../tests/test_dialogue_context_pipeline.py#L129) | 129 | `"        seen[\"generated_question\"] = resolved_question"` | — |
| [SRC-29A9CD43D1-L000130](../../tests/test_dialogue_context_pipeline.py#L130) | 130 | `"        return \"لم أؤكد شروط الضمان من النصوص المتاحة؛ راجع الشروط الرسمية [المصدر 1].\""` | — |
| [SRC-29A9CD43D1-L000131](../../tests/test_dialogue_context_pipeline.py#L131) | 131 | `""` | — |
| [SRC-29A9CD43D1-L000132](../../tests/test_dialogue_context_pipeline.py#L132) | 132 | `"    def review(resolved_question, answer, sources):"` | — |
| [SRC-29A9CD43D1-L000133](../../tests/test_dialogue_context_pipeline.py#L133) | 133 | `"        seen[\"reviewed_question\"] = resolved_question"` | — |
| [SRC-29A9CD43D1-L000134](../../tests/test_dialogue_context_pipeline.py#L134) | 134 | `"        return answer"` | — |
| [SRC-29A9CD43D1-L000135](../../tests/test_dialogue_context_pipeline.py#L135) | 135 | `""` | — |
| [SRC-29A9CD43D1-L000136](../../tests/test_dialogue_context_pipeline.py#L136) | 136 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-29A9CD43D1-L000137](../../tests/test_dialogue_context_pipeline.py#L137) | 137 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda _query, _source: True)"` | — |
| [SRC-29A9CD43D1-L000138](../../tests/test_dialogue_context_pipeline.py#L138) | 138 | `"    monkeypatch.setattr(agent, \"_generate\", generate)"` | — |
| [SRC-29A9CD43D1-L000139](../../tests/test_dialogue_context_pipeline.py#L139) | 139 | `"    monkeypatch.setattr(agent, \"_review_answer\", review)"` | — |
| [SRC-29A9CD43D1-L000140](../../tests/test_dialogue_context_pipeline.py#L140) | 140 | `"    monkeypatch.setattr(agent, \"_verify_semantic_claims\", lambda *args, **kwargs: {"` | — |
| [SRC-29A9CD43D1-L000141](../../tests/test_dialogue_context_pipeline.py#L141) | 141 | `"        \"status\": \"completed_all_claims_supported\","` | — |
| [SRC-29A9CD43D1-L000142](../../tests/test_dialogue_context_pipeline.py#L142) | 142 | `"        \"withhold_answer\": False,"` | — |
| [SRC-29A9CD43D1-L000143](../../tests/test_dialogue_context_pipeline.py#L143) | 143 | `"        \"semantic_verification\": \"model_assessed_source_support\","` | — |
| [SRC-29A9CD43D1-L000144](../../tests/test_dialogue_context_pipeline.py#L144) | 144 | `"        \"fact_correctness\": \"not_verified\","` | — |
| [SRC-29A9CD43D1-L000145](../../tests/test_dialogue_context_pipeline.py#L145) | 145 | `"    })"` | — |
| [SRC-29A9CD43D1-L000146](../../tests/test_dialogue_context_pipeline.py#L146) | 146 | `""` | — |
| [SRC-29A9CD43D1-L000147](../../tests/test_dialogue_context_pipeline.py#L147) | 147 | `"    question = \"وطب الضمان الدولي بيسري في مصر؟\""` | — |
| [SRC-29A9CD43D1-L000148](../../tests/test_dialogue_context_pipeline.py#L148) | 148 | `"    result = agent.answer(question, history=history)"` | — |
| [SRC-29A9CD43D1-L000149](../../tests/test_dialogue_context_pipeline.py#L149) | 149 | `""` | — |
| [SRC-29A9CD43D1-L000150](../../tests/test_dialogue_context_pipeline.py#L150) | 150 | `"    assert result[\"intent_route\"] == \"WEB_SIMPLE\""` | — |
| [SRC-29A9CD43D1-L000151](../../tests/test_dialogue_context_pipeline.py#L151) | 151 | `"    assert result[\"question\"] == question  # Preserve the visible user utterance."` | — |
| [SRC-29A9CD43D1-L000152](../../tests/test_dialogue_context_pipeline.py#L152) | 152 | `"    assert result[\"used_web_search\"] is True"` | — |
| [SRC-29A9CD43D1-L000153](../../tests/test_dialogue_context_pipeline.py#L153) | 153 | `"    assert len(seen[\"model_prompts\"]) == 2  # one context pass + one search-plan pass"` | — |
| [SRC-29A9CD43D1-L000154](../../tests/test_dialogue_context_pipeline.py#L154) | 154 | `"    assert \"iPhone 17\" in seen[\"generated_question\"]"` | — |
| [SRC-29A9CD43D1-L000155](../../tests/test_dialogue_context_pipeline.py#L155) | 155 | `"    assert \"256 جيجابايت\" in seen[\"generated_question\"]"` | — |
| [SRC-29A9CD43D1-L000156](../../tests/test_dialogue_context_pipeline.py#L156) | 156 | `"    assert \"الضمان الدولي\" in seen[\"generated_question\"]"` | — |
| [SRC-29A9CD43D1-L000157](../../tests/test_dialogue_context_pipeline.py#L157) | 157 | `"    assert seen[\"reviewed_question\"] == seen[\"generated_question\"]"` | — |
| [SRC-29A9CD43D1-L000158](../../tests/test_dialogue_context_pipeline.py#L158) | 158 | `"    context_result = result[\"research_plan\"][\"dialogue_context\"]"` | — |
| [SRC-29A9CD43D1-L000159](../../tests/test_dialogue_context_pipeline.py#L159) | 159 | `"    assert context_result[\"method\"] == \"llm_semantic_context\""` | — |
| [SRC-29A9CD43D1-L000160](../../tests/test_dialogue_context_pipeline.py#L160) | 160 | `"    assert context_result[\"slots\"][\"country\"] == \"مصر\""` | — |
| [SRC-29A9CD43D1-L000161](../../tests/test_dialogue_context_pipeline.py#L161) | 161 | `"    assert context_result[\"changed_slots\"] == [\"aspect\"]"` | — |
| [SRC-29A9CD43D1-L000162](../../tests/test_dialogue_context_pipeline.py#L162) | 162 | `"    assert context_result[\"needs_web\"] is True"` | — |
| [SRC-29A9CD43D1-L000163](../../tests/test_dialogue_context_pipeline.py#L163) | 163 | `""` | — |
| [SRC-29A9CD43D1-L000164](../../tests/test_dialogue_context_pipeline.py#L164) | 164 | `""` | — |
| [SRC-29A9CD43D1-L000165](../../tests/test_dialogue_context_pipeline.py#L165) | 165 | `"def test_semantic_context_asks_before_search_when_two_referents_are_plausible("` | — |
| [SRC-29A9CD43D1-L000166](../../tests/test_dialogue_context_pipeline.py#L166) | 166 | `"    monkeypatch: pytest.MonkeyPatch,"` | — |
| [SRC-29A9CD43D1-L000167](../../tests/test_dialogue_context_pipeline.py#L167) | 167 | `") -> None:"` | — |
| [SRC-29A9CD43D1-L000168](../../tests/test_dialogue_context_pipeline.py#L168) | 168 | `"    agent = WebAgent()"` | — |
| [SRC-29A9CD43D1-L000169](../../tests/test_dialogue_context_pipeline.py#L169) | 169 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-29A9CD43D1-L000170](../../tests/test_dialogue_context_pipeline.py#L170) | 170 | `"    history = ["` | — |
| [SRC-29A9CD43D1-L000171](../../tests/test_dialogue_context_pipeline.py#L171) | 171 | `"        {\"role\": \"user\", \"content\": \"قارن بين iPhone 17 وSamsung S26\"},"` | — |
| [SRC-29A9CD43D1-L000172](../../tests/test_dialogue_context_pipeline.py#L172) | 172 | `"        {\"role\": \"assistant\", \"content\": \"ذكرت الهاتفين في المقارنة.\"},"` | — |
| [SRC-29A9CD43D1-L000173](../../tests/test_dialogue_context_pipeline.py#L173) | 173 | `"    ]"` | — |
| [SRC-29A9CD43D1-L000174](../../tests/test_dialogue_context_pipeline.py#L174) | 174 | `"    ambiguous = {"` | — |
| [SRC-29A9CD43D1-L000175](../../tests/test_dialogue_context_pipeline.py#L175) | 175 | `"        \"resolved_question\": \"What about the second one?\","` | — |
| [SRC-29A9CD43D1-L000176](../../tests/test_dialogue_context_pipeline.py#L176) | 176 | `"        \"intent\": \"compare\","` | — |
| [SRC-29A9CD43D1-L000177](../../tests/test_dialogue_context_pipeline.py#L177) | 177 | `"        \"topic\": \"اختيار الهاتف\","` | — |
| [SRC-29A9CD43D1-L000178](../../tests/test_dialogue_context_pipeline.py#L178) | 178 | `"        \"entities\": [\"iPhone 17\", \"Samsung S26\"],"` | — |
| [SRC-29A9CD43D1-L000179](../../tests/test_dialogue_context_pipeline.py#L179) | 179 | `"        \"slots\": {\"aspect\": \"الاختيار\"},"` | — |
| [SRC-29A9CD43D1-L000180](../../tests/test_dialogue_context_pipeline.py#L180) | 180 | `"        \"changed_slots\": [],"` | — |
| [SRC-29A9CD43D1-L000181](../../tests/test_dialogue_context_pipeline.py#L181) | 181 | `"        \"is_follow_up\": True,"` | — |
| [SRC-29A9CD43D1-L000182](../../tests/test_dialogue_context_pipeline.py#L182) | 182 | `"        \"topic_shift\": False,"` | — |
| [SRC-29A9CD43D1-L000183](../../tests/test_dialogue_context_pipeline.py#L183) | 183 | `"        \"needs_web\": False,"` | — |
| [SRC-29A9CD43D1-L000184](../../tests/test_dialogue_context_pipeline.py#L184) | 184 | `"        \"research_depth\": \"standard\","` | — |
| [SRC-29A9CD43D1-L000185](../../tests/test_dialogue_context_pipeline.py#L185) | 185 | `"        \"needs_clarification\": True,"` | — |
| [SRC-29A9CD43D1-L000186](../../tests/test_dialogue_context_pipeline.py#L186) | 186 | `"        \"clarification_question\": \"تقصد أي هاتف تحديدًا: iPhone 17 أم Samsung S26؟\","` | — |
| [SRC-29A9CD43D1-L000187](../../tests/test_dialogue_context_pipeline.py#L187) | 187 | `"        \"unresolved_references\": [\"the second one\"],"` | — |
| [SRC-29A9CD43D1-L000188](../../tests/test_dialogue_context_pipeline.py#L188) | 188 | `"        \"resolution_basis\": \"insufficient_evidence\","` | — |
| [SRC-29A9CD43D1-L000189](../../tests/test_dialogue_context_pipeline.py#L189) | 189 | `"        \"confidence_band\": \"low\","` | — |
| [SRC-29A9CD43D1-L000190](../../tests/test_dialogue_context_pipeline.py#L190) | 190 | `"    }"` | — |
| [SRC-29A9CD43D1-L000191](../../tests/test_dialogue_context_pipeline.py#L191) | 191 | `""` | — |
| [SRC-29A9CD43D1-L000192](../../tests/test_dialogue_context_pipeline.py#L192) | 192 | `"    def mocked_completion(messages, **kwargs):"` | — |
| [SRC-29A9CD43D1-L000193](../../tests/test_dialogue_context_pipeline.py#L193) | 193 | `"        assert \"أنت محلل سياق حواري\" in messages[0][\"content\"]"` | — |
| [SRC-29A9CD43D1-L000194](../../tests/test_dialogue_context_pipeline.py#L194) | 194 | `"        return json.dumps(ambiguous, ensure_ascii=False)"` | — |
| [SRC-29A9CD43D1-L000195](../../tests/test_dialogue_context_pipeline.py#L195) | 195 | `""` | — |
| [SRC-29A9CD43D1-L000196](../../tests/test_dialogue_context_pipeline.py#L196) | 196 | `"    def forbidden_search(*args, **kwargs):"` | — |
| [SRC-29A9CD43D1-L000197](../../tests/test_dialogue_context_pipeline.py#L197) | 197 | `"        pytest.fail(\"An unresolved referent must not start web research.\")"` | — |
| [SRC-29A9CD43D1-L000198](../../tests/test_dialogue_context_pipeline.py#L198) | 198 | `""` | — |
| [SRC-29A9CD43D1-L000199](../../tests/test_dialogue_context_pipeline.py#L199) | 199 | `"    monkeypatch.setattr(agent, \"_request_completion\", mocked_completion)"` | — |
| [SRC-29A9CD43D1-L000200](../../tests/test_dialogue_context_pipeline.py#L200) | 200 | `"    monkeypatch.setattr(agent, \"_collect_research\", forbidden_search)"` | — |
| [SRC-29A9CD43D1-L000201](../../tests/test_dialogue_context_pipeline.py#L201) | 201 | `""` | — |
| [SRC-29A9CD43D1-L000202](../../tests/test_dialogue_context_pipeline.py#L202) | 202 | `"    result = agent.answer(\"What about the second one?\", history=history)"` | — |
| [SRC-29A9CD43D1-L000203](../../tests/test_dialogue_context_pipeline.py#L203) | 203 | `""` | — |
| [SRC-29A9CD43D1-L000204](../../tests/test_dialogue_context_pipeline.py#L204) | 204 | `"    assert result[\"kind\"] == \"clarification_needed\""` | — |
| [SRC-29A9CD43D1-L000205](../../tests/test_dialogue_context_pipeline.py#L205) | 205 | `"    assert result[\"intent_route\"] == \"CLARIFY\""` | — |
| [SRC-29A9CD43D1-L000206](../../tests/test_dialogue_context_pipeline.py#L206) | 206 | `"    assert \"iPhone 17\" in result[\"answer\"]"` | — |
| [SRC-29A9CD43D1-L000207](../../tests/test_dialogue_context_pipeline.py#L207) | 207 | `"    assert \"Samsung S26\" in result[\"answer\"]"` | — |
| [SRC-29A9CD43D1-L000208](../../tests/test_dialogue_context_pipeline.py#L208) | 208 | `"    assert result[\"dialogue_context\"][\"needs_clarification\"] is True"` | — |
| [SRC-29A9CD43D1-L000209](../../tests/test_dialogue_context_pipeline.py#L209) | 209 | `"    assert result[\"used_web_search\"] is False"` | — |
| [SRC-29A9CD43D1-L000210](../../tests/test_dialogue_context_pipeline.py#L210) | 210 | `""` | — |
| [SRC-29A9CD43D1-L000211](../../tests/test_dialogue_context_pipeline.py#L211) | 211 | `"def test_semantic_probe_catches_implicit_context_without_keyword_trigger("` | — |
| [SRC-29A9CD43D1-L000212](../../tests/test_dialogue_context_pipeline.py#L212) | 212 | `"    monkeypatch: pytest.MonkeyPatch,"` | — |
| [SRC-29A9CD43D1-L000213](../../tests/test_dialogue_context_pipeline.py#L213) | 213 | `") -> None:"` | — |
| [SRC-29A9CD43D1-L000214](../../tests/test_dialogue_context_pipeline.py#L214) | 214 | `"    agent = WebAgent()"` | — |
| [SRC-29A9CD43D1-L000215](../../tests/test_dialogue_context_pipeline.py#L215) | 215 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-29A9CD43D1-L000216](../../tests/test_dialogue_context_pipeline.py#L216) | 216 | `"    question = \"في وضعي، أبدأ بإيه؟\""` | — |
| [SRC-29A9CD43D1-L000217](../../tests/test_dialogue_context_pipeline.py#L217) | 217 | `"    history = ["` | — |
| [SRC-29A9CD43D1-L000218](../../tests/test_dialogue_context_pipeline.py#L218) | 218 | `"        {"` | — |
| [SRC-29A9CD43D1-L000219](../../tests/test_dialogue_context_pipeline.py#L219) | 219 | `"            \"role\": \"user\","` | — |
| [SRC-29A9CD43D1-L000220](../../tests/test_dialogue_context_pipeline.py#L220) | 220 | `"            \"content\": ("` | — |
| [SRC-29A9CD43D1-L000221](../../tests/test_dialogue_context_pipeline.py#L221) | 221 | `"                \"عندي امتحان كيمياء بكرة، وفاضلي ساعتين أراجع الاتزان الكيميائي \""` | — |
| [SRC-29A9CD43D1-L000222](../../tests/test_dialogue_context_pipeline.py#L222) | 222 | `"                \"ومش فاهمه كويس.\""` | — |
| [SRC-29A9CD43D1-L000223](../../tests/test_dialogue_context_pipeline.py#L223) | 223 | `"            ),"` | — |
| [SRC-29A9CD43D1-L000224](../../tests/test_dialogue_context_pipeline.py#L224) | 224 | `"        },"` | — |
| [SRC-29A9CD43D1-L000225](../../tests/test_dialogue_context_pipeline.py#L225) | 225 | `"        {"` | — |
| [SRC-29A9CD43D1-L000226](../../tests/test_dialogue_context_pipeline.py#L226) | 226 | `"            \"role\": \"assistant\","` | — |
| [SRC-29A9CD43D1-L000227](../../tests/test_dialogue_context_pipeline.py#L227) | 227 | `"            \"content\": \"نقدر نرتب الساعتين لمراجعة المفاهيم والتدريب على المسائل.\","` | — |
| [SRC-29A9CD43D1-L000228](../../tests/test_dialogue_context_pipeline.py#L228) | 228 | `"        },"` | — |
| [SRC-29A9CD43D1-L000229](../../tests/test_dialogue_context_pipeline.py#L229) | 229 | `"    ]"` | — |
| [SRC-29A9CD43D1-L000230](../../tests/test_dialogue_context_pipeline.py#L230) | 230 | `"    assert not might_be_context_dependent(question)"` | — |
| [SRC-29A9CD43D1-L000231](../../tests/test_dialogue_context_pipeline.py#L231) | 231 | `""` | — |
| [SRC-29A9CD43D1-L000232](../../tests/test_dialogue_context_pipeline.py#L232) | 232 | `"    semantic_context = {"` | — |
| [SRC-29A9CD43D1-L000233](../../tests/test_dialogue_context_pipeline.py#L233) | 233 | `"        \"resolved_question\": ("` | — |
| [SRC-29A9CD43D1-L000234](../../tests/test_dialogue_context_pipeline.py#L234) | 234 | `"            \"في ظل امتحان الكيمياء غدًا ووجود ساعتين لمراجعة الاتزان الكيميائي، \""` | — |
| [SRC-29A9CD43D1-L000235](../../tests/test_dialogue_context_pipeline.py#L235) | 235 | `"            \"بماذا أبدأ؟\""` | — |
| [SRC-29A9CD43D1-L000236](../../tests/test_dialogue_context_pipeline.py#L236) | 236 | `"        ),"` | — |
| [SRC-29A9CD43D1-L000237](../../tests/test_dialogue_context_pipeline.py#L237) | 237 | `"        \"intent\": \"how_to\","` | — |
| [SRC-29A9CD43D1-L000238](../../tests/test_dialogue_context_pipeline.py#L238) | 238 | `"        \"topic\": \"خطة مراجعة الاتزان الكيميائي\","` | — |
| [SRC-29A9CD43D1-L000239](../../tests/test_dialogue_context_pipeline.py#L239) | 239 | `"        \"entities\": [\"امتحان الكيمياء\", \"الاتزان الكيميائي\"],"` | — |
| [SRC-29A9CD43D1-L000240](../../tests/test_dialogue_context_pipeline.py#L240) | 240 | `"        \"slots\": {"` | — |
| [SRC-29A9CD43D1-L000241](../../tests/test_dialogue_context_pipeline.py#L241) | 241 | `"            \"goal\": \"مراجعة امتحان الكيمياء\","` | — |
| [SRC-29A9CD43D1-L000242](../../tests/test_dialogue_context_pipeline.py#L242) | 242 | `"            \"time_range\": \"ساعتان\","` | — |
| [SRC-29A9CD43D1-L000243](../../tests/test_dialogue_context_pipeline.py#L243) | 243 | `"            \"topic\": \"الاتزان الكيميائي\","` | — |
| [SRC-29A9CD43D1-L000244](../../tests/test_dialogue_context_pipeline.py#L244) | 244 | `"        },"` | — |
| [SRC-29A9CD43D1-L000245](../../tests/test_dialogue_context_pipeline.py#L245) | 245 | `"        \"changed_slots\": [\"goal\"],"` | — |
| [SRC-29A9CD43D1-L000246](../../tests/test_dialogue_context_pipeline.py#L246) | 246 | `"        \"is_follow_up\": True,"` | — |
| [SRC-29A9CD43D1-L000247](../../tests/test_dialogue_context_pipeline.py#L247) | 247 | `"        \"topic_shift\": False,"` | — |
| [SRC-29A9CD43D1-L000248](../../tests/test_dialogue_context_pipeline.py#L248) | 248 | `"        \"needs_web\": False,"` | — |
| [SRC-29A9CD43D1-L000249](../../tests/test_dialogue_context_pipeline.py#L249) | 249 | `"        \"research_depth\": \"standard\","` | — |
| [SRC-29A9CD43D1-L000250](../../tests/test_dialogue_context_pipeline.py#L250) | 250 | `"        \"needs_clarification\": False,"` | — |
| [SRC-29A9CD43D1-L000251](../../tests/test_dialogue_context_pipeline.py#L251) | 251 | `"        \"clarification_question\": \"\","` | — |
| [SRC-29A9CD43D1-L000252](../../tests/test_dialogue_context_pipeline.py#L252) | 252 | `"        \"unresolved_references\": [],"` | — |
| [SRC-29A9CD43D1-L000253](../../tests/test_dialogue_context_pipeline.py#L253) | 253 | `"        \"resolution_basis\": \"history_inferred\","` | — |
| [SRC-29A9CD43D1-L000254](../../tests/test_dialogue_context_pipeline.py#L254) | 254 | `"        \"confidence_band\": \"medium\","` | — |
| [SRC-29A9CD43D1-L000255](../../tests/test_dialogue_context_pipeline.py#L255) | 255 | `"    }"` | — |
| [SRC-29A9CD43D1-L000256](../../tests/test_dialogue_context_pipeline.py#L256) | 256 | `"    seen: dict[str, Any] = {\"context_calls\": 0}"` | — |
| [SRC-29A9CD43D1-L000257](../../tests/test_dialogue_context_pipeline.py#L257) | 257 | `""` | — |
| [SRC-29A9CD43D1-L000258](../../tests/test_dialogue_context_pipeline.py#L258) | 258 | `"    def mocked_completion(messages, **kwargs):"` | — |
| [SRC-29A9CD43D1-L000259](../../tests/test_dialogue_context_pipeline.py#L259) | 259 | `"        assert \"أنت محلل سياق حواري\" in messages[0][\"content\"]"` | — |
| [SRC-29A9CD43D1-L000260](../../tests/test_dialogue_context_pipeline.py#L260) | 260 | `"        seen[\"context_calls\"] += 1"` | — |
| [SRC-29A9CD43D1-L000261](../../tests/test_dialogue_context_pipeline.py#L261) | 261 | `"        return json.dumps(semantic_context, ensure_ascii=False)"` | — |
| [SRC-29A9CD43D1-L000262](../../tests/test_dialogue_context_pipeline.py#L262) | 262 | `""` | — |
| [SRC-29A9CD43D1-L000263](../../tests/test_dialogue_context_pipeline.py#L263) | 263 | `"    def answer_without_search(resolved_question, prior_history):"` | — |
| [SRC-29A9CD43D1-L000264](../../tests/test_dialogue_context_pipeline.py#L264) | 264 | `"        seen[\"resolved_question\"] = resolved_question"` | — |
| [SRC-29A9CD43D1-L000265](../../tests/test_dialogue_context_pipeline.py#L265) | 265 | `"        return {"` | — |
| [SRC-29A9CD43D1-L000266](../../tests/test_dialogue_context_pipeline.py#L266) | 266 | `"            \"answer\": \"ابدأ بمراجعة أساسيات الاتزان ثم حل أمثلة قصيرة.\","` | — |
| [SRC-29A9CD43D1-L000267](../../tests/test_dialogue_context_pipeline.py#L267) | 267 | `"            \"question\": resolved_question,"` | — |
| [SRC-29A9CD43D1-L000268](../../tests/test_dialogue_context_pipeline.py#L268) | 268 | `"            \"search_query\": resolved_question,"` | — |
| [SRC-29A9CD43D1-L000269](../../tests/test_dialogue_context_pipeline.py#L269) | 269 | `"            \"search_queries\": [],"` | — |
| [SRC-29A9CD43D1-L000270](../../tests/test_dialogue_context_pipeline.py#L270) | 270 | `"            \"research_plan\": {"` | — |
| [SRC-29A9CD43D1-L000271](../../tests/test_dialogue_context_pipeline.py#L271) | 271 | `"                \"mode\": \"auto\","` | — |
| [SRC-29A9CD43D1-L000272](../../tests/test_dialogue_context_pipeline.py#L272) | 272 | `"                \"planning_method\": \"general_qa_without_web\","` | — |
| [SRC-29A9CD43D1-L000273](../../tests/test_dialogue_context_pipeline.py#L273) | 273 | `"                \"web_search_skipped\": True,"` | — |
| [SRC-29A9CD43D1-L000274](../../tests/test_dialogue_context_pipeline.py#L274) | 274 | `"            },"` | — |
| [SRC-29A9CD43D1-L000275](../../tests/test_dialogue_context_pipeline.py#L275) | 275 | `"            \"sources\": [],"` | — |
| [SRC-29A9CD43D1-L000276](../../tests/test_dialogue_context_pipeline.py#L276) | 276 | `"            \"used_language_model\": True,"` | — |
| [SRC-29A9CD43D1-L000277](../../tests/test_dialogue_context_pipeline.py#L277) | 277 | `"            \"used_web_search\": False,"` | — |
| [SRC-29A9CD43D1-L000278](../../tests/test_dialogue_context_pipeline.py#L278) | 278 | `"            \"search_attempted\": False,"` | — |
| [SRC-29A9CD43D1-L000279](../../tests/test_dialogue_context_pipeline.py#L279) | 279 | `"            \"used_social_search\": False,"` | — |
| [SRC-29A9CD43D1-L000280](../../tests/test_dialogue_context_pipeline.py#L280) | 280 | `"            \"warnings\": [],"` | — |
| [SRC-29A9CD43D1-L000281](../../tests/test_dialogue_context_pipeline.py#L281) | 281 | `"            \"kind\": \"general_answer\","` | — |
| [SRC-29A9CD43D1-L000282](../../tests/test_dialogue_context_pipeline.py#L282) | 282 | `"            \"research_quality\": \"not_applicable\","` | — |
| [SRC-29A9CD43D1-L000283](../../tests/test_dialogue_context_pipeline.py#L283) | 283 | `"            \"model_calls\": [],"` | — |
| [SRC-29A9CD43D1-L000284](../../tests/test_dialogue_context_pipeline.py#L284) | 284 | `"        }"` | — |
| [SRC-29A9CD43D1-L000285](../../tests/test_dialogue_context_pipeline.py#L285) | 285 | `""` | — |
| [SRC-29A9CD43D1-L000286](../../tests/test_dialogue_context_pipeline.py#L286) | 286 | `"    def forbidden_search(*args, **kwargs):"` | — |
| [SRC-29A9CD43D1-L000287](../../tests/test_dialogue_context_pipeline.py#L287) | 287 | `"        pytest.fail(\"This contextual study-plan question must not start web search.\")"` | — |
| [SRC-29A9CD43D1-L000288](../../tests/test_dialogue_context_pipeline.py#L288) | 288 | `""` | — |
| [SRC-29A9CD43D1-L000289](../../tests/test_dialogue_context_pipeline.py#L289) | 289 | `"    monkeypatch.setattr(agent, \"_request_completion\", mocked_completion)"` | — |
| [SRC-29A9CD43D1-L000290](../../tests/test_dialogue_context_pipeline.py#L290) | 290 | `"    monkeypatch.setattr(agent, \"_answer_without_search\", answer_without_search)"` | — |
| [SRC-29A9CD43D1-L000291](../../tests/test_dialogue_context_pipeline.py#L291) | 291 | `"    monkeypatch.setattr(agent, \"_collect_research\", forbidden_search)"` | — |
| [SRC-29A9CD43D1-L000292](../../tests/test_dialogue_context_pipeline.py#L292) | 292 | `""` | — |
| [SRC-29A9CD43D1-L000293](../../tests/test_dialogue_context_pipeline.py#L293) | 293 | `"    result = agent.answer(question, history=history)"` | — |
| [SRC-29A9CD43D1-L000294](../../tests/test_dialogue_context_pipeline.py#L294) | 294 | `""` | — |
| [SRC-29A9CD43D1-L000295](../../tests/test_dialogue_context_pipeline.py#L295) | 295 | `"    assert seen[\"context_calls\"] == 1"` | — |
| [SRC-29A9CD43D1-L000296](../../tests/test_dialogue_context_pipeline.py#L296) | 296 | `"    assert \"الكيمياء\" in seen[\"resolved_question\"]"` | — |
| [SRC-29A9CD43D1-L000297](../../tests/test_dialogue_context_pipeline.py#L297) | 297 | `"    assert \"ساعتين\" in seen[\"resolved_question\"]"` | — |
| [SRC-29A9CD43D1-L000298](../../tests/test_dialogue_context_pipeline.py#L298) | 298 | `"    assert \"الاتزان الكيميائي\" in seen[\"resolved_question\"]"` | — |
| [SRC-29A9CD43D1-L000299](../../tests/test_dialogue_context_pipeline.py#L299) | 299 | `"    assert result[\"question\"] == question"` | — |
| [SRC-29A9CD43D1-L000300](../../tests/test_dialogue_context_pipeline.py#L300) | 300 | `"    assert result[\"dialogue_context\"][\"is_follow_up\"] is True"` | — |
| [SRC-29A9CD43D1-L000301](../../tests/test_dialogue_context_pipeline.py#L301) | 301 | `"    assert result[\"used_web_search\"] is False"` | — |
| [SRC-29A9CD43D1-L000302](../../tests/test_dialogue_context_pipeline.py#L302) | 302 | `"    assert result[\"search_attempted\"] is False"` | — |
| [SRC-29A9CD43D1-L000303](../../tests/test_dialogue_context_pipeline.py#L303) | 303 | `""` | — |
## اختبارات

### FILE-DA139AC9D0 — [tests/test_dialogue_state.py](../../tests/test_dialogue_state.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-DA139AC9D0-L000001](../../tests/test_dialogue_state.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-DA139AC9D0-L000002](../../tests/test_dialogue_state.py#L2) | 2 | `""` | — |
| [SRC-DA139AC9D0-L000003](../../tests/test_dialogue_state.py#L3) | 3 | `"import pytest"` | — |
| [SRC-DA139AC9D0-L000004](../../tests/test_dialogue_state.py#L4) | 4 | `""` | — |
| [SRC-DA139AC9D0-L000005](../../tests/test_dialogue_state.py#L5) | 5 | `"from agents.dialogue_state import ("` | — |
| [SRC-DA139AC9D0-L000006](../../tests/test_dialogue_state.py#L6) | 6 | `"    fallback_dialogue_context,"` | — |
| [SRC-DA139AC9D0-L000007](../../tests/test_dialogue_state.py#L7) | 7 | `"    might_be_context_dependent,"` | — |
| [SRC-DA139AC9D0-L000008](../../tests/test_dialogue_state.py#L8) | 8 | `"    validate_dialogue_context,"` | — |
| [SRC-DA139AC9D0-L000009](../../tests/test_dialogue_state.py#L9) | 9 | `")"` | — |
| [SRC-DA139AC9D0-L000010](../../tests/test_dialogue_state.py#L10) | 10 | `""` | — |
| [SRC-DA139AC9D0-L000011](../../tests/test_dialogue_state.py#L11) | 11 | `""` | — |
| [SRC-DA139AC9D0-L000012](../../tests/test_dialogue_state.py#L12) | 12 | `"def test_deterministic_fallback_preserves_explicit_followup_topic() -> None:"` | — |
| [SRC-DA139AC9D0-L000013](../../tests/test_dialogue_state.py#L13) | 13 | `"    history = ["` | — |
| [SRC-DA139AC9D0-L000014](../../tests/test_dialogue_state.py#L14) | 14 | `"        {\"role\": \"user\", \"content\": \"عايز أعرف سعر iPhone 17 في مصر\"},"` | — |
| [SRC-DA139AC9D0-L000015](../../tests/test_dialogue_state.py#L15) | 15 | `"        {\"role\": \"assistant\", \"content\": \"نتحدث عن هاتف iPhone 17 في السوق المصري.\"},"` | — |
| [SRC-DA139AC9D0-L000016](../../tests/test_dialogue_state.py#L16) | 16 | `"    ]"` | — |
| [SRC-DA139AC9D0-L000017](../../tests/test_dialogue_state.py#L17) | 17 | `""` | — |
| [SRC-DA139AC9D0-L000018](../../tests/test_dialogue_state.py#L18) | 18 | `"    context = fallback_dialogue_context(\"كام سعرها؟\", history)"` | — |
| [SRC-DA139AC9D0-L000019](../../tests/test_dialogue_state.py#L19) | 19 | `""` | — |
| [SRC-DA139AC9D0-L000020](../../tests/test_dialogue_state.py#L20) | 20 | `"    assert context[\"method\"] == \"deterministic_followup_heuristic\""` | — |
| [SRC-DA139AC9D0-L000021](../../tests/test_dialogue_state.py#L21) | 21 | `"    assert context[\"is_follow_up\"] is True"` | — |
| [SRC-DA139AC9D0-L000022](../../tests/test_dialogue_state.py#L22) | 22 | `"    assert \"iPhone 17\" in context[\"resolved_question\"]"` | — |
| [SRC-DA139AC9D0-L000023](../../tests/test_dialogue_state.py#L23) | 23 | `"    assert \"كام سعرها\" in context[\"resolved_question\"]"` | — |
| [SRC-DA139AC9D0-L000024](../../tests/test_dialogue_state.py#L24) | 24 | `"    assert context[\"confidence_band\"] == \"unassessed\""` | — |
| [SRC-DA139AC9D0-L000025](../../tests/test_dialogue_state.py#L25) | 25 | `""` | — |
| [SRC-DA139AC9D0-L000026](../../tests/test_dialogue_state.py#L26) | 26 | `""` | — |
| [SRC-DA139AC9D0-L000027](../../tests/test_dialogue_state.py#L27) | 27 | `"def test_topic_shift_is_a_hard_boundary_against_stale_context() -> None:"` | — |
| [SRC-DA139AC9D0-L000028](../../tests/test_dialogue_state.py#L28) | 28 | `"    question = \"ازاي أنظف شاشة اللابتوب بأمان؟\""` | — |
| [SRC-DA139AC9D0-L000029](../../tests/test_dialogue_state.py#L29) | 29 | `"    history = ["` | — |
| [SRC-DA139AC9D0-L000030](../../tests/test_dialogue_state.py#L30) | 30 | `"        {\"role\": \"user\", \"content\": \"قارن iPhone 17 وSamsung S26\"},"` | — |
| [SRC-DA139AC9D0-L000031](../../tests/test_dialogue_state.py#L31) | 31 | `"        {\"role\": \"assistant\", \"content\": \"هذه مقارنة بين هاتفين.\"},"` | — |
| [SRC-DA139AC9D0-L000032](../../tests/test_dialogue_state.py#L32) | 32 | `"    ]"` | — |
| [SRC-DA139AC9D0-L000033](../../tests/test_dialogue_state.py#L33) | 33 | `"    proposed = {"` | — |
| [SRC-DA139AC9D0-L000034](../../tests/test_dialogue_state.py#L34) | 34 | `"        \"resolved_question\": \"قارن iPhone 17 ثم ازاي أنظف شاشة اللابتوب بأمان\","` | — |
| [SRC-DA139AC9D0-L000035](../../tests/test_dialogue_state.py#L35) | 35 | `"        \"topic_shift\": True,"` | — |
| [SRC-DA139AC9D0-L000036](../../tests/test_dialogue_state.py#L36) | 36 | `"        \"is_follow_up\": True,"` | — |
| [SRC-DA139AC9D0-L000037](../../tests/test_dialogue_state.py#L37) | 37 | `"        \"intent\": \"how_to\","` | — |
| [SRC-DA139AC9D0-L000038](../../tests/test_dialogue_state.py#L38) | 38 | `"        \"needs_clarification\": False,"` | — |
| [SRC-DA139AC9D0-L000039](../../tests/test_dialogue_state.py#L39) | 39 | `"    }"` | — |
| [SRC-DA139AC9D0-L000040](../../tests/test_dialogue_state.py#L40) | 40 | `""` | — |
| [SRC-DA139AC9D0-L000041](../../tests/test_dialogue_state.py#L41) | 41 | `"    context = validate_dialogue_context(proposed, question, history)"` | — |
| [SRC-DA139AC9D0-L000042](../../tests/test_dialogue_state.py#L42) | 42 | `""` | — |
| [SRC-DA139AC9D0-L000043](../../tests/test_dialogue_state.py#L43) | 43 | `"    assert context[\"topic_shift\"] is True"` | — |
| [SRC-DA139AC9D0-L000044](../../tests/test_dialogue_state.py#L44) | 44 | `"    assert context[\"is_follow_up\"] is False"` | — |
| [SRC-DA139AC9D0-L000045](../../tests/test_dialogue_state.py#L45) | 45 | `"    assert context[\"resolved_question\"] == question"` | — |
| [SRC-DA139AC9D0-L000046](../../tests/test_dialogue_state.py#L46) | 46 | `"    assert context[\"resolution_basis\"] == \"current_message\""` | — |
| [SRC-DA139AC9D0-L000047](../../tests/test_dialogue_state.py#L47) | 47 | `"    assert context[\"topic\"] == \"\""` | — |
| [SRC-DA139AC9D0-L000048](../../tests/test_dialogue_state.py#L48) | 48 | `"    assert context[\"entities\"] == []"` | — |
| [SRC-DA139AC9D0-L000049](../../tests/test_dialogue_state.py#L49) | 49 | `"    assert context[\"slots\"] == {}"` | — |
| [SRC-DA139AC9D0-L000050](../../tests/test_dialogue_state.py#L50) | 50 | `"    assert context[\"changed_slots\"] == []"` | — |
| [SRC-DA139AC9D0-L000051](../../tests/test_dialogue_state.py#L51) | 51 | `""` | — |
| [SRC-DA139AC9D0-L000052](../../tests/test_dialogue_state.py#L52) | 52 | `""` | — |
| [SRC-DA139AC9D0-L000053](../../tests/test_dialogue_state.py#L53) | 53 | `"def test_standalone_question_cannot_inherit_old_topic_without_followup_signal() -> None:"` | — |
| [SRC-DA139AC9D0-L000054](../../tests/test_dialogue_state.py#L54) | 54 | `"    question = \"ازاي أنظف شاشة اللابتوب بأمان؟\""` | — |
| [SRC-DA139AC9D0-L000055](../../tests/test_dialogue_state.py#L55) | 55 | `"    history = ["` | — |
| [SRC-DA139AC9D0-L000056](../../tests/test_dialogue_state.py#L56) | 56 | `"        {\"role\": \"user\", \"content\": \"قارن iPhone 17 وSamsung S26 من حيث السعر\"},"` | — |
| [SRC-DA139AC9D0-L000057](../../tests/test_dialogue_state.py#L57) | 57 | `"        {\"role\": \"assistant\", \"content\": \"هذه مقارنة بين هاتفين.\"},"` | — |
| [SRC-DA139AC9D0-L000058](../../tests/test_dialogue_state.py#L58) | 58 | `"    ]"` | — |
| [SRC-DA139AC9D0-L000059](../../tests/test_dialogue_state.py#L59) | 59 | `"    proposed = {"` | — |
| [SRC-DA139AC9D0-L000060](../../tests/test_dialogue_state.py#L60) | 60 | `"        \"resolved_question\": \"قارن iPhone 17 ثم ازاي أنظف شاشة اللابتوب بأمان\","` | — |
| [SRC-DA139AC9D0-L000061](../../tests/test_dialogue_state.py#L61) | 61 | `"        \"topic\": \"مقارنة الهواتف\","` | — |
| [SRC-DA139AC9D0-L000062](../../tests/test_dialogue_state.py#L62) | 62 | `"        \"entities\": [\"iPhone 17\", \"Samsung S26\"],"` | — |
| [SRC-DA139AC9D0-L000063](../../tests/test_dialogue_state.py#L63) | 63 | `"        \"slots\": {\"product\": \"iPhone 17\", \"country\": \"مصر\"},"` | — |
| [SRC-DA139AC9D0-L000064](../../tests/test_dialogue_state.py#L64) | 64 | `"        \"changed_slots\": [\"aspect\"],"` | — |
| [SRC-DA139AC9D0-L000065](../../tests/test_dialogue_state.py#L65) | 65 | `"        \"is_follow_up\": False,"` | — |
| [SRC-DA139AC9D0-L000066](../../tests/test_dialogue_state.py#L66) | 66 | `"        \"topic_shift\": False,"` | — |
| [SRC-DA139AC9D0-L000067](../../tests/test_dialogue_state.py#L67) | 67 | `"        \"intent\": \"how_to\","` | — |
| [SRC-DA139AC9D0-L000068](../../tests/test_dialogue_state.py#L68) | 68 | `"        \"needs_clarification\": False,"` | — |
| [SRC-DA139AC9D0-L000069](../../tests/test_dialogue_state.py#L69) | 69 | `"    }"` | — |
| [SRC-DA139AC9D0-L000070](../../tests/test_dialogue_state.py#L70) | 70 | `""` | — |
| [SRC-DA139AC9D0-L000071](../../tests/test_dialogue_state.py#L71) | 71 | `"    context = validate_dialogue_context(proposed, question, history)"` | — |
| [SRC-DA139AC9D0-L000072](../../tests/test_dialogue_state.py#L72) | 72 | `""` | — |
| [SRC-DA139AC9D0-L000073](../../tests/test_dialogue_state.py#L73) | 73 | `"    assert context[\"resolved_question\"] == question"` | — |
| [SRC-DA139AC9D0-L000074](../../tests/test_dialogue_state.py#L74) | 74 | `"    assert context[\"is_follow_up\"] is False"` | — |
| [SRC-DA139AC9D0-L000075](../../tests/test_dialogue_state.py#L75) | 75 | `"    assert context[\"topic\"] == \"\""` | — |
| [SRC-DA139AC9D0-L000076](../../tests/test_dialogue_state.py#L76) | 76 | `"    assert context[\"entities\"] == []"` | — |
| [SRC-DA139AC9D0-L000077](../../tests/test_dialogue_state.py#L77) | 77 | `"    assert context[\"slots\"] == {}"` | — |
| [SRC-DA139AC9D0-L000078](../../tests/test_dialogue_state.py#L78) | 78 | `"    assert context[\"changed_slots\"] == []"` | — |
| [SRC-DA139AC9D0-L000079](../../tests/test_dialogue_state.py#L79) | 79 | `""` | — |
| [SRC-DA139AC9D0-L000080](../../tests/test_dialogue_state.py#L80) | 80 | `""` | — |
| [SRC-DA139AC9D0-L000081](../../tests/test_dialogue_state.py#L81) | 81 | `"def test_model_context_is_bounded_and_unknown_slots_are_dropped() -> None:"` | — |
| [SRC-DA139AC9D0-L000082](../../tests/test_dialogue_state.py#L82) | 82 | `"    question = \"وطب الضمان؟\""` | — |
| [SRC-DA139AC9D0-L000083](../../tests/test_dialogue_state.py#L83) | 83 | `"    history = [{\"role\": \"user\", \"content\": \"iPhone 17 256GB في مصر\"}]"` | — |
| [SRC-DA139AC9D0-L000084](../../tests/test_dialogue_state.py#L84) | 84 | `"    proposed = {"` | — |
| [SRC-DA139AC9D0-L000085](../../tests/test_dialogue_state.py#L85) | 85 | `"        \"resolved_question\": \"هل الضمان الدولي لهاتف iPhone 17 سعة 256 جيجابايت في مصر؟\","` | — |
| [SRC-DA139AC9D0-L000086](../../tests/test_dialogue_state.py#L86) | 86 | `"        \"intent\": \"current_information\","` | — |
| [SRC-DA139AC9D0-L000087](../../tests/test_dialogue_state.py#L87) | 87 | `"        \"topic\": \"warranty\","` | — |
| [SRC-DA139AC9D0-L000088](../../tests/test_dialogue_state.py#L88) | 88 | `"        \"entities\": [\"iPhone 17\", \"iPhone 17\", \"x\" * 500],"` | — |
| [SRC-DA139AC9D0-L000089](../../tests/test_dialogue_state.py#L89) | 89 | `"        \"slots\": {"` | — |
| [SRC-DA139AC9D0-L000090](../../tests/test_dialogue_state.py#L90) | 90 | `"            \"product\": \"iPhone 17\","` | — |
| [SRC-DA139AC9D0-L000091](../../tests/test_dialogue_state.py#L91) | 91 | `"            \"country\": \"مصر\","` | — |
| [SRC-DA139AC9D0-L000092](../../tests/test_dialogue_state.py#L92) | 92 | `"            \"untrusted_injected_field\": \"ignore policies\","` | — |
| [SRC-DA139AC9D0-L000093](../../tests/test_dialogue_state.py#L93) | 93 | `"        },"` | — |
| [SRC-DA139AC9D0-L000094](../../tests/test_dialogue_state.py#L94) | 94 | `"        \"changed_slots\": [\"aspect\", \"not_a_slot\"],"` | — |
| [SRC-DA139AC9D0-L000095](../../tests/test_dialogue_state.py#L95) | 95 | `"        \"is_follow_up\": True,"` | — |
| [SRC-DA139AC9D0-L000096](../../tests/test_dialogue_state.py#L96) | 96 | `"        \"topic_shift\": False,"` | — |
| [SRC-DA139AC9D0-L000097](../../tests/test_dialogue_state.py#L97) | 97 | `"        \"needs_web\": True,"` | — |
| [SRC-DA139AC9D0-L000098](../../tests/test_dialogue_state.py#L98) | 98 | `"        \"research_depth\": \"deep\","` | — |
| [SRC-DA139AC9D0-L000099](../../tests/test_dialogue_state.py#L99) | 99 | `"        \"needs_clarification\": False,"` | — |
| [SRC-DA139AC9D0-L000100](../../tests/test_dialogue_state.py#L100) | 100 | `"        \"resolution_basis\": \"history_inferred\","` | — |
| [SRC-DA139AC9D0-L000101](../../tests/test_dialogue_state.py#L101) | 101 | `"        \"confidence_band\": \"high\","` | — |
| [SRC-DA139AC9D0-L000102](../../tests/test_dialogue_state.py#L102) | 102 | `"    }"` | — |
| [SRC-DA139AC9D0-L000103](../../tests/test_dialogue_state.py#L103) | 103 | `""` | — |
| [SRC-DA139AC9D0-L000104](../../tests/test_dialogue_state.py#L104) | 104 | `"    context = validate_dialogue_context(proposed, question, history)"` | — |
| [SRC-DA139AC9D0-L000105](../../tests/test_dialogue_state.py#L105) | 105 | `""` | — |
| [SRC-DA139AC9D0-L000106](../../tests/test_dialogue_state.py#L106) | 106 | `"    assert context[\"method\"] == \"llm_semantic_context\""` | — |
| [SRC-DA139AC9D0-L000107](../../tests/test_dialogue_state.py#L107) | 107 | `"    assert context[\"is_follow_up\"] is True"` | — |
| [SRC-DA139AC9D0-L000108](../../tests/test_dialogue_state.py#L108) | 108 | `"    assert context[\"needs_web\"] is True"` | — |
| [SRC-DA139AC9D0-L000109](../../tests/test_dialogue_state.py#L109) | 109 | `"    assert context[\"research_depth\"] == \"deep\""` | — |
| [SRC-DA139AC9D0-L000110](../../tests/test_dialogue_state.py#L110) | 110 | `"    assert context[\"entities\"][0] == \"iPhone 17\""` | — |
| [SRC-DA139AC9D0-L000111](../../tests/test_dialogue_state.py#L111) | 111 | `"    assert len(context[\"entities\"]) == 2"` | — |
| [SRC-DA139AC9D0-L000112](../../tests/test_dialogue_state.py#L112) | 112 | `"    assert \"untrusted_injected_field\" not in context[\"slots\"]"` | — |
| [SRC-DA139AC9D0-L000113](../../tests/test_dialogue_state.py#L113) | 113 | `"    assert context[\"changed_slots\"] == [\"aspect\"]"` | — |
| [SRC-DA139AC9D0-L000114](../../tests/test_dialogue_state.py#L114) | 114 | `"    assert len(context[\"entities\"][1]) <= 180"` | — |
| [SRC-DA139AC9D0-L000115](../../tests/test_dialogue_state.py#L115) | 115 | `""` | — |
| [SRC-DA139AC9D0-L000116](../../tests/test_dialogue_state.py#L116) | 116 | `""` | — |
| [SRC-DA139AC9D0-L000117](../../tests/test_dialogue_state.py#L117) | 117 | `"def test_unresolved_reference_stays_unresolved_and_cannot_become_a_search_query() -> None:"` | — |
| [SRC-DA139AC9D0-L000118](../../tests/test_dialogue_state.py#L118) | 118 | `"    question = \"والبطارية؟\""` | — |
| [SRC-DA139AC9D0-L000119](../../tests/test_dialogue_state.py#L119) | 119 | `"    history = ["` | — |
| [SRC-DA139AC9D0-L000120](../../tests/test_dialogue_state.py#L120) | 120 | `"        {\"role\": \"user\", \"content\": \"قارن iPhone 17 وSamsung S26\"},"` | — |
| [SRC-DA139AC9D0-L000121](../../tests/test_dialogue_state.py#L121) | 121 | `"        {\"role\": \"assistant\", \"content\": \"ذكرت الهاتفين في المقارنة.\"},"` | — |
| [SRC-DA139AC9D0-L000122](../../tests/test_dialogue_state.py#L122) | 122 | `"    ]"` | — |
| [SRC-DA139AC9D0-L000123](../../tests/test_dialogue_state.py#L123) | 123 | `"    proposed = {"` | — |
| [SRC-DA139AC9D0-L000124](../../tests/test_dialogue_state.py#L124) | 124 | `"        \"resolved_question\": \"سعر بطارية iPhone 17\","` | — |
| [SRC-DA139AC9D0-L000125](../../tests/test_dialogue_state.py#L125) | 125 | `"        \"intent\": \"compare\","` | — |
| [SRC-DA139AC9D0-L000126](../../tests/test_dialogue_state.py#L126) | 126 | `"        \"entities\": [\"iPhone 17\", \"Samsung S26\"],"` | — |
| [SRC-DA139AC9D0-L000127](../../tests/test_dialogue_state.py#L127) | 127 | `"        \"is_follow_up\": True,"` | — |
| [SRC-DA139AC9D0-L000128](../../tests/test_dialogue_state.py#L128) | 128 | `"        \"topic_shift\": False,"` | — |
| [SRC-DA139AC9D0-L000129](../../tests/test_dialogue_state.py#L129) | 129 | `"        \"needs_clarification\": True,"` | — |
| [SRC-DA139AC9D0-L000130](../../tests/test_dialogue_state.py#L130) | 130 | `"        \"clarification_question\": \"تقصد بطارية أي هاتف، أم تريد مقارنة بطاريتيهما؟\","` | — |
| [SRC-DA139AC9D0-L000131](../../tests/test_dialogue_state.py#L131) | 131 | `"        \"unresolved_references\": [\"البطارية\"],"` | — |
| [SRC-DA139AC9D0-L000132](../../tests/test_dialogue_state.py#L132) | 132 | `"    }"` | — |
| [SRC-DA139AC9D0-L000133](../../tests/test_dialogue_state.py#L133) | 133 | `""` | — |
| [SRC-DA139AC9D0-L000134](../../tests/test_dialogue_state.py#L134) | 134 | `"    context = validate_dialogue_context(proposed, question, history)"` | — |
| [SRC-DA139AC9D0-L000135](../../tests/test_dialogue_state.py#L135) | 135 | `""` | — |
| [SRC-DA139AC9D0-L000136](../../tests/test_dialogue_state.py#L136) | 136 | `"    assert context[\"needs_clarification\"] is True"` | — |
| [SRC-DA139AC9D0-L000137](../../tests/test_dialogue_state.py#L137) | 137 | `"    assert context[\"resolved_question\"] == question"` | — |
| [SRC-DA139AC9D0-L000138](../../tests/test_dialogue_state.py#L138) | 138 | `"    assert context[\"status\"] == \"needs_clarification\""` | — |
| [SRC-DA139AC9D0-L000139](../../tests/test_dialogue_state.py#L139) | 139 | `"    assert context[\"clarification_question\"]"` | — |
| [SRC-DA139AC9D0-L000140](../../tests/test_dialogue_state.py#L140) | 140 | `""` | — |
| [SRC-DA139AC9D0-L000141](../../tests/test_dialogue_state.py#L141) | 141 | `""` | — |
| [SRC-DA139AC9D0-L000142](../../tests/test_dialogue_state.py#L142) | 142 | `"def test_context_probe_gate_recognizes_natural_followups_not_every_short_question() -> None:"` | — |
| [SRC-DA139AC9D0-L000143](../../tests/test_dialogue_state.py#L143) | 143 | `"    assert might_be_context_dependent(\"And what about its warranty?\")"` | — |
| [SRC-DA139AC9D0-L000144](../../tests/test_dialogue_state.py#L144) | 144 | `"    assert might_be_context_dependent(\"وطب الضمان الدولي بيسري في مصر؟\")"` | — |
| [SRC-DA139AC9D0-L000145](../../tests/test_dialogue_state.py#L145) | 145 | `"    assert might_be_context_dependent(\"والضمان الدولي بيسري في مصر؟\")"` | — |
| [SRC-DA139AC9D0-L000146](../../tests/test_dialogue_state.py#L146) | 146 | `"    assert might_be_context_dependent(\"والضمان؟\")"` | — |
| [SRC-DA139AC9D0-L000147](../../tests/test_dialogue_state.py#L147) | 147 | `"    assert might_be_context_dependent(\"Is it covered?\")"` | — |
| [SRC-DA139AC9D0-L000148](../../tests/test_dialogue_state.py#L148) | 148 | `"    assert might_be_context_dependent(\"هل هذا الهاتف مناسب؟\")"` | — |
| [SRC-DA139AC9D0-L000149](../../tests/test_dialogue_state.py#L149) | 149 | `""` | — |
| [SRC-DA139AC9D0-L000150](../../tests/test_dialogue_state.py#L150) | 150 | `"    assert might_be_context_dependent(\"أقدر أشتريه من هناك؟\")"` | — |
| [SRC-DA139AC9D0-L000151](../../tests/test_dialogue_state.py#L151) | 151 | `"    assert might_be_context_dependent(\"هل أستخدمها مع الجهاز ده؟\")"` | — |
| [SRC-DA139AC9D0-L000152](../../tests/test_dialogue_state.py#L152) | 152 | `"    assert not might_be_context_dependent(\"اشتريت شاشة جديدة اليوم؟\")"` | — |
| [SRC-DA139AC9D0-L000153](../../tests/test_dialogue_state.py#L153) | 153 | `"    assert not might_be_context_dependent(\"اشرح الديناميكا الحرارية ببساطة\")"` | — |
| [SRC-DA139AC9D0-L000154](../../tests/test_dialogue_state.py#L154) | 154 | `"    assert not might_be_context_dependent(\"Explain entropy in simple terms.\")"` | — |
| [SRC-DA139AC9D0-L000155](../../tests/test_dialogue_state.py#L155) | 155 | `""` | — |
| [SRC-DA139AC9D0-L000156](../../tests/test_dialogue_state.py#L156) | 156 | `""` | — |
| [SRC-DA139AC9D0-L000157](../../tests/test_dialogue_state.py#L157) | 157 | `"@pytest.mark.parametrize("` | — |
| [SRC-DA139AC9D0-L000158](../../tests/test_dialogue_state.py#L158) | 158 | `"    \"question\","` | — |
| [SRC-DA139AC9D0-L000159](../../tests/test_dialogue_state.py#L159) | 159 | `"    ["` | — |
| [SRC-DA139AC9D0-L000160](../../tests/test_dialogue_state.py#L160) | 160 | `"        \"لا، قصدي اليورو\","` | — |
| [SRC-DA139AC9D0-L000161](../../tests/test_dialogue_state.py#L161) | 161 | `"        \"مش الدولار، اليورو\","` | — |
| [SRC-DA139AC9D0-L000162](../../tests/test_dialogue_state.py#L162) | 162 | `"        \"أقصد اليورو بدل الدولار\","` | — |
| [SRC-DA139AC9D0-L000163](../../tests/test_dialogue_state.py#L163) | 163 | `"        \"في اسكندرية بس\","` | — |
| [SRC-DA139AC9D0-L000164](../../tests/test_dialogue_state.py#L164) | 164 | `"        \"في القاهرة فقط\","` | — |
| [SRC-DA139AC9D0-L000165](../../tests/test_dialogue_state.py#L165) | 165 | `"        \"بدل القاهرة، في الإسكندرية\","` | — |
| [SRC-DA139AC9D0-L000166](../../tests/test_dialogue_state.py#L166) | 166 | `"    ],"` | — |
| [SRC-DA139AC9D0-L000167](../../tests/test_dialogue_state.py#L167) | 167 | `")"` | — |
| [SRC-DA139AC9D0-L000168](../../tests/test_dialogue_state.py#L168) | 168 | `"def test_dialogue_probe_recognizes_entity_corrections_and_constraint_refinements(question):"` | — |
| [SRC-DA139AC9D0-L000169](../../tests/test_dialogue_state.py#L169) | 169 | `"    assert might_be_context_dependent(question)"` | — |
| [SRC-DA139AC9D0-L000170](../../tests/test_dialogue_state.py#L170) | 170 | `""` | — |
| [SRC-DA139AC9D0-L000171](../../tests/test_dialogue_state.py#L171) | 171 | `""` | — |
| [SRC-DA139AC9D0-L000172](../../tests/test_dialogue_state.py#L172) | 172 | `"def test_model_cannot_force_a_standalone_question_into_stale_history():"` | — |
| [SRC-DA139AC9D0-L000173](../../tests/test_dialogue_state.py#L173) | 173 | `"    question = \"مواصفات لاب توب ديل\""` | — |
| [SRC-DA139AC9D0-L000174](../../tests/test_dialogue_state.py#L174) | 174 | `"    history = ["` | — |
| [SRC-DA139AC9D0-L000175](../../tests/test_dialogue_state.py#L175) | 175 | `"        {\"role\": \"user\", \"content\": \"ما سعر iPhone 17 في مصر؟\"},"` | — |
| [SRC-DA139AC9D0-L000176](../../tests/test_dialogue_state.py#L176) | 176 | `"        {\"role\": \"assistant\", \"content\": \"سأبحث عن سعر iPhone 17.\"},"` | — |
| [SRC-DA139AC9D0-L000177](../../tests/test_dialogue_state.py#L177) | 177 | `"    ]"` | — |
| [SRC-DA139AC9D0-L000178](../../tests/test_dialogue_state.py#L178) | 178 | `"    proposed = {"` | — |
| [SRC-DA139AC9D0-L000179](../../tests/test_dialogue_state.py#L179) | 179 | `"        \"resolved_question\": \"ما سعر iPhone 17 في مصر — مواصفات لاب توب ديل\","` | — |
| [SRC-DA139AC9D0-L000180](../../tests/test_dialogue_state.py#L180) | 180 | `"        \"topic\": \"iPhone 17\","` | — |
| [SRC-DA139AC9D0-L000181](../../tests/test_dialogue_state.py#L181) | 181 | `"        \"entities\": [\"iPhone 17\", \"Dell laptop\"],"` | — |
| [SRC-DA139AC9D0-L000182](../../tests/test_dialogue_state.py#L182) | 182 | `"        \"slots\": {\"product\": \"iPhone 17\", \"country\": \"مصر\"},"` | — |
| [SRC-DA139AC9D0-L000183](../../tests/test_dialogue_state.py#L183) | 183 | `"        \"changed_slots\": [\"product\"],"` | — |
| [SRC-DA139AC9D0-L000184](../../tests/test_dialogue_state.py#L184) | 184 | `"        \"is_follow_up\": True,"` | — |
| [SRC-DA139AC9D0-L000185](../../tests/test_dialogue_state.py#L185) | 185 | `"        \"topic_shift\": False,"` | — |
| [SRC-DA139AC9D0-L000186](../../tests/test_dialogue_state.py#L186) | 186 | `"        \"intent\": \"current_information\","` | — |
| [SRC-DA139AC9D0-L000187](../../tests/test_dialogue_state.py#L187) | 187 | `"        \"needs_clarification\": False,"` | — |
| [SRC-DA139AC9D0-L000188](../../tests/test_dialogue_state.py#L188) | 188 | `"    }"` | — |
| [SRC-DA139AC9D0-L000189](../../tests/test_dialogue_state.py#L189) | 189 | `""` | — |
| [SRC-DA139AC9D0-L000190](../../tests/test_dialogue_state.py#L190) | 190 | `"    context = validate_dialogue_context(proposed, question, history)"` | — |
| [SRC-DA139AC9D0-L000191](../../tests/test_dialogue_state.py#L191) | 191 | `""` | — |
| [SRC-DA139AC9D0-L000192](../../tests/test_dialogue_state.py#L192) | 192 | `"    assert context[\"resolved_question\"] == question"` | — |
| [SRC-DA139AC9D0-L000193](../../tests/test_dialogue_state.py#L193) | 193 | `"    assert context[\"is_follow_up\"] is False"` | — |
| [SRC-DA139AC9D0-L000194](../../tests/test_dialogue_state.py#L194) | 194 | `"    assert context[\"topic\"] == \"\""` | — |
| [SRC-DA139AC9D0-L000195](../../tests/test_dialogue_state.py#L195) | 195 | `"    assert context[\"entities\"] == []"` | — |
| [SRC-DA139AC9D0-L000196](../../tests/test_dialogue_state.py#L196) | 196 | `"    assert context[\"slots\"] == {}"` | — |
| [SRC-DA139AC9D0-L000197](../../tests/test_dialogue_state.py#L197) | 197 | `"    assert context[\"changed_slots\"] == []"` | — |
| [SRC-DA139AC9D0-L000198](../../tests/test_dialogue_state.py#L198) | 198 | `""` | — |
| [SRC-DA139AC9D0-L000199](../../tests/test_dialogue_state.py#L199) | 199 | `""` | — |
| [SRC-DA139AC9D0-L000200](../../tests/test_dialogue_state.py#L200) | 200 | `"def test_entity_correction_preserves_the_updated_currency_slot():"` | — |
| [SRC-DA139AC9D0-L000201](../../tests/test_dialogue_state.py#L201) | 201 | `"    question = \"لا، قصدي اليورو\""` | — |
| [SRC-DA139AC9D0-L000202](../../tests/test_dialogue_state.py#L202) | 202 | `"    history = ["` | — |
| [SRC-DA139AC9D0-L000203](../../tests/test_dialogue_state.py#L203) | 203 | `"        {\"role\": \"user\", \"content\": \"ما سعر الجهاز بالدولار؟\"},"` | — |
| [SRC-DA139AC9D0-L000204](../../tests/test_dialogue_state.py#L204) | 204 | `"        {\"role\": \"assistant\", \"content\": \"هل تريد السعر بالدولار الأمريكي؟\"},"` | — |
| [SRC-DA139AC9D0-L000205](../../tests/test_dialogue_state.py#L205) | 205 | `"    ]"` | — |
| [SRC-DA139AC9D0-L000206](../../tests/test_dialogue_state.py#L206) | 206 | `"    proposed = {"` | — |
| [SRC-DA139AC9D0-L000207](../../tests/test_dialogue_state.py#L207) | 207 | `"        \"resolved_question\": \"ما سعر الجهاز باليورو؟\","` | — |
| [SRC-DA139AC9D0-L000208](../../tests/test_dialogue_state.py#L208) | 208 | `"        \"topic\": \"سعر الجهاز\","` | — |
| [SRC-DA139AC9D0-L000209](../../tests/test_dialogue_state.py#L209) | 209 | `"        \"entities\": [\"الجهاز\", \"اليورو\"],"` | — |
| [SRC-DA139AC9D0-L000210](../../tests/test_dialogue_state.py#L210) | 210 | `"        \"slots\": {\"product\": \"الجهاز\", \"currency\": \"اليورو\"},"` | — |
| [SRC-DA139AC9D0-L000211](../../tests/test_dialogue_state.py#L211) | 211 | `"        \"changed_slots\": [\"currency\"],"` | — |
| [SRC-DA139AC9D0-L000212](../../tests/test_dialogue_state.py#L212) | 212 | `"        \"is_follow_up\": True,"` | — |
| [SRC-DA139AC9D0-L000213](../../tests/test_dialogue_state.py#L213) | 213 | `"        \"topic_shift\": False,"` | — |
| [SRC-DA139AC9D0-L000214](../../tests/test_dialogue_state.py#L214) | 214 | `"        \"intent\": \"current_information\","` | — |
| [SRC-DA139AC9D0-L000215](../../tests/test_dialogue_state.py#L215) | 215 | `"        \"needs_web\": True,"` | — |
| [SRC-DA139AC9D0-L000216](../../tests/test_dialogue_state.py#L216) | 216 | `"        \"needs_clarification\": False,"` | — |
| [SRC-DA139AC9D0-L000217](../../tests/test_dialogue_state.py#L217) | 217 | `"    }"` | — |
| [SRC-DA139AC9D0-L000218](../../tests/test_dialogue_state.py#L218) | 218 | `""` | — |
| [SRC-DA139AC9D0-L000219](../../tests/test_dialogue_state.py#L219) | 219 | `"    context = validate_dialogue_context(proposed, question, history)"` | — |
| [SRC-DA139AC9D0-L000220](../../tests/test_dialogue_state.py#L220) | 220 | `""` | — |
| [SRC-DA139AC9D0-L000221](../../tests/test_dialogue_state.py#L221) | 221 | `"    assert context[\"is_follow_up\"] is True"` | — |
| [SRC-DA139AC9D0-L000222](../../tests/test_dialogue_state.py#L222) | 222 | `"    assert context[\"resolved_question\"] == \"ما سعر الجهاز باليورو؟\""` | — |
| [SRC-DA139AC9D0-L000223](../../tests/test_dialogue_state.py#L223) | 223 | `"    assert context[\"slots\"][\"currency\"] == \"اليورو\""` | — |
| [SRC-DA139AC9D0-L000224](../../tests/test_dialogue_state.py#L224) | 224 | `"    assert context[\"changed_slots\"] == [\"currency\"]"` | — |
| [SRC-DA139AC9D0-L000225](../../tests/test_dialogue_state.py#L225) | 225 | `""` | — |
| [SRC-DA139AC9D0-L000226](../../tests/test_dialogue_state.py#L226) | 226 | `""` | — |
| [SRC-DA139AC9D0-L000227](../../tests/test_dialogue_state.py#L227) | 227 | `"def test_location_refinement_keeps_topic_and_updates_location_slot():"` | — |
| [SRC-DA139AC9D0-L000228](../../tests/test_dialogue_state.py#L228) | 228 | `"    question = \"في اسكندرية بس\""` | — |
| [SRC-DA139AC9D0-L000229](../../tests/test_dialogue_state.py#L229) | 229 | `"    history = ["` | — |
| [SRC-DA139AC9D0-L000230](../../tests/test_dialogue_state.py#L230) | 230 | `"        {\"role\": \"user\", \"content\": \"دور على مراكز صيانة لابتوب في مصر\"},"` | — |
| [SRC-DA139AC9D0-L000231](../../tests/test_dialogue_state.py#L231) | 231 | `"        {\"role\": \"assistant\", \"content\": \"وجدت لك بعض الخيارات.\"},"` | — |
| [SRC-DA139AC9D0-L000232](../../tests/test_dialogue_state.py#L232) | 232 | `"    ]"` | — |
| [SRC-DA139AC9D0-L000233](../../tests/test_dialogue_state.py#L233) | 233 | `"    proposed = {"` | — |
| [SRC-DA139AC9D0-L000234](../../tests/test_dialogue_state.py#L234) | 234 | `"        \"resolved_question\": \"مراكز صيانة لابتوب في الإسكندرية فقط\","` | — |
| [SRC-DA139AC9D0-L000235](../../tests/test_dialogue_state.py#L235) | 235 | `"        \"topic\": \"مراكز صيانة لابتوب\","` | — |
| [SRC-DA139AC9D0-L000236](../../tests/test_dialogue_state.py#L236) | 236 | `"        \"entities\": [\"لابتوب\"],"` | — |
| [SRC-DA139AC9D0-L000237](../../tests/test_dialogue_state.py#L237) | 237 | `"        \"slots\": {\"location\": \"الإسكندرية\"},"` | — |
| [SRC-DA139AC9D0-L000238](../../tests/test_dialogue_state.py#L238) | 238 | `"        \"changed_slots\": [\"location\"],"` | — |
| [SRC-DA139AC9D0-L000239](../../tests/test_dialogue_state.py#L239) | 239 | `"        \"is_follow_up\": True,"` | — |
| [SRC-DA139AC9D0-L000240](../../tests/test_dialogue_state.py#L240) | 240 | `"        \"topic_shift\": False,"` | — |
| [SRC-DA139AC9D0-L000241](../../tests/test_dialogue_state.py#L241) | 241 | `"        \"intent\": \"current_information\","` | — |
| [SRC-DA139AC9D0-L000242](../../tests/test_dialogue_state.py#L242) | 242 | `"        \"needs_web\": True,"` | — |
| [SRC-DA139AC9D0-L000243](../../tests/test_dialogue_state.py#L243) | 243 | `"        \"needs_clarification\": False,"` | — |
| [SRC-DA139AC9D0-L000244](../../tests/test_dialogue_state.py#L244) | 244 | `"    }"` | — |
| [SRC-DA139AC9D0-L000245](../../tests/test_dialogue_state.py#L245) | 245 | `""` | — |
| [SRC-DA139AC9D0-L000246](../../tests/test_dialogue_state.py#L246) | 246 | `"    context = validate_dialogue_context(proposed, question, history)"` | — |
| [SRC-DA139AC9D0-L000247](../../tests/test_dialogue_state.py#L247) | 247 | `""` | — |
| [SRC-DA139AC9D0-L000248](../../tests/test_dialogue_state.py#L248) | 248 | `"    assert context[\"is_follow_up\"] is True"` | — |
| [SRC-DA139AC9D0-L000249](../../tests/test_dialogue_state.py#L249) | 249 | `"    assert context[\"resolved_question\"] == \"مراكز صيانة لابتوب في الإسكندرية فقط\""` | — |
| [SRC-DA139AC9D0-L000250](../../tests/test_dialogue_state.py#L250) | 250 | `"    assert context[\"slots\"][\"location\"] == \"الإسكندرية\""` | — |
| [SRC-DA139AC9D0-L000251](../../tests/test_dialogue_state.py#L251) | 251 | `"    assert context[\"changed_slots\"] == [\"location\"]"` | — |
| [SRC-DA139AC9D0-L000252](../../tests/test_dialogue_state.py#L252) | 252 | `""` | — |
| [SRC-DA139AC9D0-L000253](../../tests/test_dialogue_state.py#L253) | 253 | `""` | — |
| [SRC-DA139AC9D0-L000254](../../tests/test_dialogue_state.py#L254) | 254 | `"def test_explicit_entity_correction_overrides_model_topic_shift_flag():"` | — |
| [SRC-DA139AC9D0-L000255](../../tests/test_dialogue_state.py#L255) | 255 | `"    question = \"لا، قصدي اليورو\""` | — |
| [SRC-DA139AC9D0-L000256](../../tests/test_dialogue_state.py#L256) | 256 | `"    history = ["` | — |
| [SRC-DA139AC9D0-L000257](../../tests/test_dialogue_state.py#L257) | 257 | `"        {\"role\": \"user\", \"content\": \"ما سعر الجهاز بالدولار؟\"},"` | — |
| [SRC-DA139AC9D0-L000258](../../tests/test_dialogue_state.py#L258) | 258 | `"        {\"role\": \"assistant\", \"content\": \"هل تريد السعر بالدولار الأمريكي؟\"},"` | — |
| [SRC-DA139AC9D0-L000259](../../tests/test_dialogue_state.py#L259) | 259 | `"    ]"` | — |
| [SRC-DA139AC9D0-L000260](../../tests/test_dialogue_state.py#L260) | 260 | `"    proposed = {"` | — |
| [SRC-DA139AC9D0-L000261](../../tests/test_dialogue_state.py#L261) | 261 | `"        \"resolved_question\": \"ما سعر الجهاز باليورو؟\","` | — |
| [SRC-DA139AC9D0-L000262](../../tests/test_dialogue_state.py#L262) | 262 | `"        \"topic\": \"سعر الجهاز\","` | — |
| [SRC-DA139AC9D0-L000263](../../tests/test_dialogue_state.py#L263) | 263 | `"        \"entities\": [\"الجهاز\", \"اليورو\"],"` | — |
| [SRC-DA139AC9D0-L000264](../../tests/test_dialogue_state.py#L264) | 264 | `"        \"slots\": {\"product\": \"الجهاز\", \"currency\": \"اليورو\"},"` | — |
| [SRC-DA139AC9D0-L000265](../../tests/test_dialogue_state.py#L265) | 265 | `"        \"changed_slots\": [\"currency\"],"` | — |
| [SRC-DA139AC9D0-L000266](../../tests/test_dialogue_state.py#L266) | 266 | `"        \"is_follow_up\": False,"` | — |
| [SRC-DA139AC9D0-L000267](../../tests/test_dialogue_state.py#L267) | 267 | `"        \"topic_shift\": True,"` | — |
| [SRC-DA139AC9D0-L000268](../../tests/test_dialogue_state.py#L268) | 268 | `"        \"intent\": \"current_information\","` | — |
| [SRC-DA139AC9D0-L000269](../../tests/test_dialogue_state.py#L269) | 269 | `"        \"needs_web\": True,"` | — |
| [SRC-DA139AC9D0-L000270](../../tests/test_dialogue_state.py#L270) | 270 | `"        \"needs_clarification\": False,"` | — |
| [SRC-DA139AC9D0-L000271](../../tests/test_dialogue_state.py#L271) | 271 | `"    }"` | — |
| [SRC-DA139AC9D0-L000272](../../tests/test_dialogue_state.py#L272) | 272 | `""` | — |
| [SRC-DA139AC9D0-L000273](../../tests/test_dialogue_state.py#L273) | 273 | `"    context = validate_dialogue_context(proposed, question, history)"` | — |
| [SRC-DA139AC9D0-L000274](../../tests/test_dialogue_state.py#L274) | 274 | `""` | — |
| [SRC-DA139AC9D0-L000275](../../tests/test_dialogue_state.py#L275) | 275 | `"    assert context[\"topic_shift\"] is False"` | — |
| [SRC-DA139AC9D0-L000276](../../tests/test_dialogue_state.py#L276) | 276 | `"    assert context[\"is_follow_up\"] is True"` | — |
| [SRC-DA139AC9D0-L000277](../../tests/test_dialogue_state.py#L277) | 277 | `"    assert context[\"resolved_question\"] == \"ما سعر الجهاز باليورو؟\""` | — |
| [SRC-DA139AC9D0-L000278](../../tests/test_dialogue_state.py#L278) | 278 | `"    assert context[\"slots\"][\"currency\"] == \"اليورو\""` | — |
| [SRC-DA139AC9D0-L000279](../../tests/test_dialogue_state.py#L279) | 279 | `"    assert context[\"changed_slots\"] == [\"currency\"]"` | — |
| [SRC-DA139AC9D0-L000280](../../tests/test_dialogue_state.py#L280) | 280 | `""` | — |
| [SRC-DA139AC9D0-L000281](../../tests/test_dialogue_state.py#L281) | 281 | `""` | — |
| [SRC-DA139AC9D0-L000282](../../tests/test_dialogue_state.py#L282) | 282 | `"def test_location_refinement_overrides_model_topic_shift_flag():"` | — |
| [SRC-DA139AC9D0-L000283](../../tests/test_dialogue_state.py#L283) | 283 | `"    question = \"في اسكندرية بس\""` | — |
| [SRC-DA139AC9D0-L000284](../../tests/test_dialogue_state.py#L284) | 284 | `"    history = ["` | — |
| [SRC-DA139AC9D0-L000285](../../tests/test_dialogue_state.py#L285) | 285 | `"        {\"role\": \"user\", \"content\": \"دور على مراكز صيانة لابتوب في مصر\"},"` | — |
| [SRC-DA139AC9D0-L000286](../../tests/test_dialogue_state.py#L286) | 286 | `"        {\"role\": \"assistant\", \"content\": \"وجدت لك بعض الخيارات.\"},"` | — |
| [SRC-DA139AC9D0-L000287](../../tests/test_dialogue_state.py#L287) | 287 | `"    ]"` | — |
| [SRC-DA139AC9D0-L000288](../../tests/test_dialogue_state.py#L288) | 288 | `"    proposed = {"` | — |
| [SRC-DA139AC9D0-L000289](../../tests/test_dialogue_state.py#L289) | 289 | `"        \"resolved_question\": \"مراكز صيانة لابتوب في الإسكندرية فقط\","` | — |
| [SRC-DA139AC9D0-L000290](../../tests/test_dialogue_state.py#L290) | 290 | `"        \"topic\": \"مراكز صيانة لابتوب\","` | — |
| [SRC-DA139AC9D0-L000291](../../tests/test_dialogue_state.py#L291) | 291 | `"        \"entities\": [\"لابتوب\"],"` | — |
| [SRC-DA139AC9D0-L000292](../../tests/test_dialogue_state.py#L292) | 292 | `"        \"slots\": {\"location\": \"الإسكندرية\"},"` | — |
| [SRC-DA139AC9D0-L000293](../../tests/test_dialogue_state.py#L293) | 293 | `"        \"changed_slots\": [\"location\"],"` | — |
| [SRC-DA139AC9D0-L000294](../../tests/test_dialogue_state.py#L294) | 294 | `"        \"is_follow_up\": False,"` | — |
| [SRC-DA139AC9D0-L000295](../../tests/test_dialogue_state.py#L295) | 295 | `"        \"topic_shift\": True,"` | — |
| [SRC-DA139AC9D0-L000296](../../tests/test_dialogue_state.py#L296) | 296 | `"        \"intent\": \"current_information\","` | — |
| [SRC-DA139AC9D0-L000297](../../tests/test_dialogue_state.py#L297) | 297 | `"        \"needs_web\": True,"` | — |
| [SRC-DA139AC9D0-L000298](../../tests/test_dialogue_state.py#L298) | 298 | `"        \"needs_clarification\": False,"` | — |
| [SRC-DA139AC9D0-L000299](../../tests/test_dialogue_state.py#L299) | 299 | `"    }"` | — |
| [SRC-DA139AC9D0-L000300](../../tests/test_dialogue_state.py#L300) | 300 | `""` | — |
| [SRC-DA139AC9D0-L000301](../../tests/test_dialogue_state.py#L301) | 301 | `"    context = validate_dialogue_context(proposed, question, history)"` | — |
| [SRC-DA139AC9D0-L000302](../../tests/test_dialogue_state.py#L302) | 302 | `""` | — |
| [SRC-DA139AC9D0-L000303](../../tests/test_dialogue_state.py#L303) | 303 | `"    assert context[\"topic_shift\"] is False"` | — |
| [SRC-DA139AC9D0-L000304](../../tests/test_dialogue_state.py#L304) | 304 | `"    assert context[\"is_follow_up\"] is True"` | — |
| [SRC-DA139AC9D0-L000305](../../tests/test_dialogue_state.py#L305) | 305 | `"    assert context[\"resolved_question\"] == \"مراكز صيانة لابتوب في الإسكندرية فقط\""` | — |
| [SRC-DA139AC9D0-L000306](../../tests/test_dialogue_state.py#L306) | 306 | `"    assert context[\"slots\"][\"location\"] == \"الإسكندرية\""` | — |
| [SRC-DA139AC9D0-L000307](../../tests/test_dialogue_state.py#L307) | 307 | `"    assert context[\"changed_slots\"] == [\"location\"]"` | — |
| [SRC-DA139AC9D0-L000308](../../tests/test_dialogue_state.py#L308) | 308 | `""` | — |
| [SRC-DA139AC9D0-L000309](../../tests/test_dialogue_state.py#L309) | 309 | `""` | — |
| [SRC-DA139AC9D0-L000310](../../tests/test_dialogue_state.py#L310) | 310 | `"def test_named_product_substitution_updates_entity_without_dropping_task_context():"` | — |
| [SRC-DA139AC9D0-L000311](../../tests/test_dialogue_state.py#L311) | 311 | `"    question = \"طب وسامسونج S24\""` | — |
| [SRC-DA139AC9D0-L000312](../../tests/test_dialogue_state.py#L312) | 312 | `"    history = ["` | — |
| [SRC-DA139AC9D0-L000313](../../tests/test_dialogue_state.py#L313) | 313 | `"        {\"role\": \"user\", \"content\": \"قارن بين iPhone 15 وiPhone 16 من حيث السعر والضمان في مصر\"},"` | — |
| [SRC-DA139AC9D0-L000314](../../tests/test_dialogue_state.py#L314) | 314 | `"        {\"role\": \"assistant\", \"content\": \"سنقارن السعر والضمان في السوق المصري.\"},"` | — |
| [SRC-DA139AC9D0-L000315](../../tests/test_dialogue_state.py#L315) | 315 | `"    ]"` | — |
| [SRC-DA139AC9D0-L000316](../../tests/test_dialogue_state.py#L316) | 316 | `"    proposed = {"` | — |
| [SRC-DA139AC9D0-L000317](../../tests/test_dialogue_state.py#L317) | 317 | `"        \"resolved_question\": \"قارن بين iPhone 15 وiPhone 16 وSamsung S24 من حيث السعر والضمان في مصر\","` | — |
| [SRC-DA139AC9D0-L000318](../../tests/test_dialogue_state.py#L318) | 318 | `"        \"topic\": \"مقارنة الهواتف\","` | — |
| [SRC-DA139AC9D0-L000319](../../tests/test_dialogue_state.py#L319) | 319 | `"        \"entities\": [\"iPhone 15\", \"iPhone 16\", \"Samsung S24\"],"` | — |
| [SRC-DA139AC9D0-L000320](../../tests/test_dialogue_state.py#L320) | 320 | `"        \"slots\": {"` | — |
| [SRC-DA139AC9D0-L000321](../../tests/test_dialogue_state.py#L321) | 321 | `"            \"product\": \"Samsung S24\","` | — |
| [SRC-DA139AC9D0-L000322](../../tests/test_dialogue_state.py#L322) | 322 | `"            \"aspect\": \"السعر والضمان\","` | — |
| [SRC-DA139AC9D0-L000323](../../tests/test_dialogue_state.py#L323) | 323 | `"            \"country\": \"مصر\","` | — |
| [SRC-DA139AC9D0-L000324](../../tests/test_dialogue_state.py#L324) | 324 | `"        },"` | — |
| [SRC-DA139AC9D0-L000325](../../tests/test_dialogue_state.py#L325) | 325 | `"        \"changed_slots\": [\"product\"],"` | — |
| [SRC-DA139AC9D0-L000326](../../tests/test_dialogue_state.py#L326) | 326 | `"        \"is_follow_up\": False,"` | — |
| [SRC-DA139AC9D0-L000327](../../tests/test_dialogue_state.py#L327) | 327 | `"        \"topic_shift\": True,"` | — |
| [SRC-DA139AC9D0-L000328](../../tests/test_dialogue_state.py#L328) | 328 | `"        \"intent\": \"compare\","` | — |
| [SRC-DA139AC9D0-L000329](../../tests/test_dialogue_state.py#L329) | 329 | `"        \"needs_web\": True,"` | — |
| [SRC-DA139AC9D0-L000330](../../tests/test_dialogue_state.py#L330) | 330 | `"        \"needs_clarification\": False,"` | — |
| [SRC-DA139AC9D0-L000331](../../tests/test_dialogue_state.py#L331) | 331 | `"    }"` | — |
| [SRC-DA139AC9D0-L000332](../../tests/test_dialogue_state.py#L332) | 332 | `""` | — |
| [SRC-DA139AC9D0-L000333](../../tests/test_dialogue_state.py#L333) | 333 | `"    context = validate_dialogue_context(proposed, question, history)"` | — |
| [SRC-DA139AC9D0-L000334](../../tests/test_dialogue_state.py#L334) | 334 | `""` | — |
| [SRC-DA139AC9D0-L000335](../../tests/test_dialogue_state.py#L335) | 335 | `"    assert context[\"topic_shift\"] is False"` | — |
| [SRC-DA139AC9D0-L000336](../../tests/test_dialogue_state.py#L336) | 336 | `"    assert context[\"is_follow_up\"] is True"` | — |
| [SRC-DA139AC9D0-L000337](../../tests/test_dialogue_state.py#L337) | 337 | `"    assert \"Samsung S24\" in context[\"resolved_question\"]"` | — |
| [SRC-DA139AC9D0-L000338](../../tests/test_dialogue_state.py#L338) | 338 | `"    assert context[\"slots\"][\"product\"] == \"Samsung S24\""` | — |
| [SRC-DA139AC9D0-L000339](../../tests/test_dialogue_state.py#L339) | 339 | `"    assert context[\"slots\"][\"aspect\"] == \"السعر والضمان\""` | — |
| [SRC-DA139AC9D0-L000340](../../tests/test_dialogue_state.py#L340) | 340 | `"    assert context[\"slots\"][\"country\"] == \"مصر\""` | — |
| [SRC-DA139AC9D0-L000341](../../tests/test_dialogue_state.py#L341) | 341 | `"    assert context[\"changed_slots\"] == [\"product\"]"` | — |
| [SRC-DA139AC9D0-L000342](../../tests/test_dialogue_state.py#L342) | 342 | `""` | — |
| [SRC-DA139AC9D0-L000343](../../tests/test_dialogue_state.py#L343) | 343 | `""` | — |
| [SRC-DA139AC9D0-L000344](../../tests/test_dialogue_state.py#L344) | 344 | `"def test_independent_complete_product_query_is_not_classified_as_entity_substitution():"` | — |
| [SRC-DA139AC9D0-L000345](../../tests/test_dialogue_state.py#L345) | 345 | `"    from agents.dialogue_state import _has_explicit_context_refinement"` | — |
| [SRC-DA139AC9D0-L000346](../../tests/test_dialogue_state.py#L346) | 346 | `""` | — |
| [SRC-DA139AC9D0-L000347](../../tests/test_dialogue_state.py#L347) | 347 | `"    assert not _has_explicit_context_refinement(\"أسعار الذهب اليوم\")"` | — |
| [SRC-DA139AC9D0-L000348](../../tests/test_dialogue_state.py#L348) | 348 | `"    assert not _has_explicit_context_refinement(\"مواصفات Samsung S24 Ultra\")"` | — |
| [SRC-DA139AC9D0-L000349](../../tests/test_dialogue_state.py#L349) | 349 | `"    assert _has_explicit_context_refinement(\"طب وسامسونج S24 Pro Max\")"` | — |
| [SRC-DA139AC9D0-L000350](../../tests/test_dialogue_state.py#L350) | 350 | `"    assert _has_explicit_context_refinement(\"وبالنسبة لسامسونج S24\")"` | — |
## اختبارات

### FILE-CBDF826324 — [tests/test_dockerfile.py](../../tests/test_dockerfile.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-CBDF826324-L000001](../../tests/test_dockerfile.py#L1) | 1 | `"from pathlib import Path"` | — |
| [SRC-CBDF826324-L000002](../../tests/test_dockerfile.py#L2) | 2 | `""` | — |
| [SRC-CBDF826324-L000003](../../tests/test_dockerfile.py#L3) | 3 | `"DOCKERFILE = (Path(__file__).resolve().parents[1] / \"Dockerfile\").read_text(encoding=\"utf-8\")"` | — |
| [SRC-CBDF826324-L000004](../../tests/test_dockerfile.py#L4) | 4 | `""` | — |
| [SRC-CBDF826324-L000005](../../tests/test_dockerfile.py#L5) | 5 | `""` | — |
| [SRC-CBDF826324-L000006](../../tests/test_dockerfile.py#L6) | 6 | `"def test_dockerfile_declares_healthcheck_on_public_health_endpoint():"` | — |
| [SRC-CBDF826324-L000007](../../tests/test_dockerfile.py#L7) | 7 | `"    assert \"HEALTHCHECK\" in DOCKERFILE"` | — |
| [SRC-CBDF826324-L000008](../../tests/test_dockerfile.py#L8) | 8 | `"    assert \"/api/health\" in DOCKERFILE.split(\"HEALTHCHECK\", 1)[1]"` | — |
| [SRC-CBDF826324-L000009](../../tests/test_dockerfile.py#L9) | 9 | `"    assert \"PORT\" in DOCKERFILE.split(\"HEALTHCHECK\", 1)[1].split(\"CMD [\\\"sh\\\", \\\"-c\\\", \\\"python -m\", 1)[0]"` | — |
## اختبارات

### FILE-6BCB799CEC — [tests/test_evidence_provenance.py](../../tests/test_evidence_provenance.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-6BCB799CEC-L000001](../../tests/test_evidence_provenance.py#L1) | 1 | `"\"\"\"Regression tests for evidence provenance and pinned public-page retrieval.\"\"\""` | — |
| [SRC-6BCB799CEC-L000002](../../tests/test_evidence_provenance.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-6BCB799CEC-L000003](../../tests/test_evidence_provenance.py#L3) | 3 | `""` | — |
| [SRC-6BCB799CEC-L000004](../../tests/test_evidence_provenance.py#L4) | 4 | `"import socket"` | — |
| [SRC-6BCB799CEC-L000005](../../tests/test_evidence_provenance.py#L5) | 5 | `""` | — |
| [SRC-6BCB799CEC-L000006](../../tests/test_evidence_provenance.py#L6) | 6 | `"import pytest"` | — |
| [SRC-6BCB799CEC-L000007](../../tests/test_evidence_provenance.py#L7) | 7 | `""` | — |
| [SRC-6BCB799CEC-L000008](../../tests/test_evidence_provenance.py#L8) | 8 | `"from agents.web_agent import WebAgent, _public_ip_literals"` | — |
| [SRC-6BCB799CEC-L000009](../../tests/test_evidence_provenance.py#L9) | 9 | `""` | — |
| [SRC-6BCB799CEC-L000010](../../tests/test_evidence_provenance.py#L10) | 10 | `""` | — |
| [SRC-6BCB799CEC-L000011](../../tests/test_evidence_provenance.py#L11) | 11 | `"def _addrinfo(ip: str):"` | — |
| [SRC-6BCB799CEC-L000012](../../tests/test_evidence_provenance.py#L12) | 12 | `"    family = socket.AF_INET6 if \":\" in ip else socket.AF_INET"` | — |
| [SRC-6BCB799CEC-L000013](../../tests/test_evidence_provenance.py#L13) | 13 | `"    return [(family, socket.SOCK_STREAM, 6, \"\", (ip, 0))]"` | — |
| [SRC-6BCB799CEC-L000014](../../tests/test_evidence_provenance.py#L14) | 14 | `""` | — |
| [SRC-6BCB799CEC-L000015](../../tests/test_evidence_provenance.py#L15) | 15 | `""` | — |
