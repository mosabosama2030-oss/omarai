# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **052**
- سجلات الأسطر: **800**
- النطاق: SRC-4405E7912C-L000207 إلى SRC-3D0DE98F65-L000183
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-4405E7912C — [tests/test_multitenant_api.py](../../tests/test_multitenant_api.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-4405E7912C-L000207](../../tests/test_multitenant_api.py#L207) | 207 | `""` | — |
| [SRC-4405E7912C-L000208](../../tests/test_multitenant_api.py#L208) | 208 | `"def test_live_diagnostics_requires_explicit_approval_before_any_provider_call("` | — |
| [SRC-4405E7912C-L000209](../../tests/test_multitenant_api.py#L209) | 209 | `"    tenant_api, monkeypatch"` | — |
| [SRC-4405E7912C-L000210](../../tests/test_multitenant_api.py#L210) | 210 | `"):"` | — |
| [SRC-4405E7912C-L000211](../../tests/test_multitenant_api.py#L211) | 211 | `"    from api.omarai import WebAgent"` | — |
| [SRC-4405E7912C-L000212](../../tests/test_multitenant_api.py#L212) | 212 | `""` | — |
| [SRC-4405E7912C-L000213](../../tests/test_multitenant_api.py#L213) | 213 | `"    base, store = tenant_api"` | — |
| [SRC-4405E7912C-L000214](../../tests/test_multitenant_api.py#L214) | 214 | `"    tenant_id = store.create_tenant(\"Diagnostics Owner\", \"diagnostics-owner\")"` | — |
| [SRC-4405E7912C-L000215](../../tests/test_multitenant_api.py#L215) | 215 | `"    user_id = store.create_user(\"diagnostics-owner@example.test\", \"Owner\")"` | — |
| [SRC-4405E7912C-L000216](../../tests/test_multitenant_api.py#L216) | 216 | `"    store.add_membership(tenant_id, user_id, \"owner\")"` | — |
| [SRC-4405E7912C-L000217](../../tests/test_multitenant_api.py#L217) | 217 | `"    token = \"diagnostics-owner-token-\" + \"O\" * 32"` | — |
| [SRC-4405E7912C-L000218](../../tests/test_multitenant_api.py#L218) | 218 | `""` | — |
| [SRC-4405E7912C-L000219](../../tests/test_multitenant_api.py#L219) | 219 | `"    def unexpected_diagnostics(*_args, **_kwargs):"` | — |
| [SRC-4405E7912C-L000220](../../tests/test_multitenant_api.py#L220) | 220 | `"        pytest.fail(\"diagnostics must not run without explicit provider-use approval\")"` | — |
| [SRC-4405E7912C-L000221](../../tests/test_multitenant_api.py#L221) | 221 | `""` | — |
| [SRC-4405E7912C-L000222](../../tests/test_multitenant_api.py#L222) | 222 | `"    store.create_api_token(token, tenant_id, user_id)"` | — |
| [SRC-4405E7912C-L000223](../../tests/test_multitenant_api.py#L223) | 223 | `"    monkeypatch.setattr(WebAgent, \"diagnostics\", unexpected_diagnostics)"` | — |
| [SRC-4405E7912C-L000224](../../tests/test_multitenant_api.py#L224) | 224 | `""` | — |
| [SRC-4405E7912C-L000225](../../tests/test_multitenant_api.py#L225) | 225 | `"    status, result = request_json("` | — |
| [SRC-4405E7912C-L000226](../../tests/test_multitenant_api.py#L226) | 226 | `"        base,"` | — |
| [SRC-4405E7912C-L000227](../../tests/test_multitenant_api.py#L227) | 227 | `"        \"/api/diagnostics\","` | — |
| [SRC-4405E7912C-L000228](../../tests/test_multitenant_api.py#L228) | 228 | `"        method=\"POST\","` | — |
| [SRC-4405E7912C-L000229](../../tests/test_multitenant_api.py#L229) | 229 | `"        token=token,"` | — |
| [SRC-4405E7912C-L000230](../../tests/test_multitenant_api.py#L230) | 230 | `"        payload={\"test_model\": True, \"test_social\": True},"` | — |
| [SRC-4405E7912C-L000231](../../tests/test_multitenant_api.py#L231) | 231 | `"    )"` | — |
| [SRC-4405E7912C-L000232](../../tests/test_multitenant_api.py#L232) | 232 | `"    assert status == 403"` | — |
| [SRC-4405E7912C-L000233](../../tests/test_multitenant_api.py#L233) | 233 | `"    assert \"explicit owner approval\" in result[\"error\"]"` | — |
| [SRC-4405E7912C-L000234](../../tests/test_multitenant_api.py#L234) | 234 | `""` | — |
| [SRC-4405E7912C-L000235](../../tests/test_multitenant_api.py#L235) | 235 | `""` | — |
| [SRC-4405E7912C-L000236](../../tests/test_multitenant_api.py#L236) | 236 | `"def test_live_diagnostics_is_owner_only_even_with_explicit_approval("` | — |
| [SRC-4405E7912C-L000237](../../tests/test_multitenant_api.py#L237) | 237 | `"    tenant_api, monkeypatch"` | — |
| [SRC-4405E7912C-L000238](../../tests/test_multitenant_api.py#L238) | 238 | `"):"` | — |
| [SRC-4405E7912C-L000239](../../tests/test_multitenant_api.py#L239) | 239 | `"    from api.omarai import WebAgent"` | — |
| [SRC-4405E7912C-L000240](../../tests/test_multitenant_api.py#L240) | 240 | `""` | — |
| [SRC-4405E7912C-L000241](../../tests/test_multitenant_api.py#L241) | 241 | `"    base, store = tenant_api"` | — |
| [SRC-4405E7912C-L000242](../../tests/test_multitenant_api.py#L242) | 242 | `"    tenant_id = store.create_tenant(\"Sales Member Diagnostics\", \"sales-member-diagnostics\")"` | — |
| [SRC-4405E7912C-L000243](../../tests/test_multitenant_api.py#L243) | 243 | `"    user_id = store.create_user(\"sales-member@example.test\", \"Sales Member\")"` | — |
| [SRC-4405E7912C-L000244](../../tests/test_multitenant_api.py#L244) | 244 | `"    store.add_membership(tenant_id, user_id, \"sales_agent\")"` | — |
| [SRC-4405E7912C-L000245](../../tests/test_multitenant_api.py#L245) | 245 | `"    token = \"sales-member-diagnostics-token-\" + \"S\" * 32"` | — |
| [SRC-4405E7912C-L000246](../../tests/test_multitenant_api.py#L246) | 246 | `""` | — |
| [SRC-4405E7912C-L000247](../../tests/test_multitenant_api.py#L247) | 247 | `"    def unexpected_diagnostics(*_args, **_kwargs):"` | — |
| [SRC-4405E7912C-L000248](../../tests/test_multitenant_api.py#L248) | 248 | `"        pytest.fail(\"non-owner diagnostics must be rejected before provider calls\")"` | — |
| [SRC-4405E7912C-L000249](../../tests/test_multitenant_api.py#L249) | 249 | `""` | — |
| [SRC-4405E7912C-L000250](../../tests/test_multitenant_api.py#L250) | 250 | `"    store.create_api_token(token, tenant_id, user_id)"` | — |
| [SRC-4405E7912C-L000251](../../tests/test_multitenant_api.py#L251) | 251 | `"    monkeypatch.setattr(WebAgent, \"diagnostics\", unexpected_diagnostics)"` | — |
| [SRC-4405E7912C-L000252](../../tests/test_multitenant_api.py#L252) | 252 | `""` | — |
| [SRC-4405E7912C-L000253](../../tests/test_multitenant_api.py#L253) | 253 | `"    status, result = request_json("` | — |
| [SRC-4405E7912C-L000254](../../tests/test_multitenant_api.py#L254) | 254 | `"        base,"` | — |
| [SRC-4405E7912C-L000255](../../tests/test_multitenant_api.py#L255) | 255 | `"        \"/api/diagnostics\","` | — |
| [SRC-4405E7912C-L000256](../../tests/test_multitenant_api.py#L256) | 256 | `"        method=\"POST\","` | — |
| [SRC-4405E7912C-L000257](../../tests/test_multitenant_api.py#L257) | 257 | `"        token=token,"` | — |
| [SRC-4405E7912C-L000258](../../tests/test_multitenant_api.py#L258) | 258 | `"        payload={"` | — |
| [SRC-4405E7912C-L000259](../../tests/test_multitenant_api.py#L259) | 259 | `"            \"test_model\": True,"` | — |
| [SRC-4405E7912C-L000260](../../tests/test_multitenant_api.py#L260) | 260 | `"            \"test_social\": True,"` | — |
| [SRC-4405E7912C-L000261](../../tests/test_multitenant_api.py#L261) | 261 | `"            \"allow_provider_usage\": True,"` | — |
| [SRC-4405E7912C-L000262](../../tests/test_multitenant_api.py#L262) | 262 | `"        },"` | — |
| [SRC-4405E7912C-L000263](../../tests/test_multitenant_api.py#L263) | 263 | `"    )"` | — |
| [SRC-4405E7912C-L000264](../../tests/test_multitenant_api.py#L264) | 264 | `"    assert status == 403"` | — |
| [SRC-4405E7912C-L000265](../../tests/test_multitenant_api.py#L265) | 265 | `"    assert \"مالك مساحة العمل\" in result[\"error\"]"` | — |
| [SRC-4405E7912C-L000266](../../tests/test_multitenant_api.py#L266) | 266 | `""` | — |
| [SRC-4405E7912C-L000267](../../tests/test_multitenant_api.py#L267) | 267 | `""` | — |
| [SRC-4405E7912C-L000268](../../tests/test_multitenant_api.py#L268) | 268 | `"def test_owner_can_run_diagnostics_only_after_explicit_approval("` | — |
| [SRC-4405E7912C-L000269](../../tests/test_multitenant_api.py#L269) | 269 | `"    tenant_api, monkeypatch"` | — |
| [SRC-4405E7912C-L000270](../../tests/test_multitenant_api.py#L270) | 270 | `"):"` | — |
| [SRC-4405E7912C-L000271](../../tests/test_multitenant_api.py#L271) | 271 | `"    from api.omarai import WebAgent"` | — |
| [SRC-4405E7912C-L000272](../../tests/test_multitenant_api.py#L272) | 272 | `""` | — |
| [SRC-4405E7912C-L000273](../../tests/test_multitenant_api.py#L273) | 273 | `"    base, store = tenant_api"` | — |
| [SRC-4405E7912C-L000274](../../tests/test_multitenant_api.py#L274) | 274 | `"    tenant_id = store.create_tenant(\"Approved Diagnostics\", \"approved-diagnostics\")"` | — |
| [SRC-4405E7912C-L000275](../../tests/test_multitenant_api.py#L275) | 275 | `"    user_id = store.create_user(\"approved-owner@example.test\", \"Owner\")"` | — |
| [SRC-4405E7912C-L000276](../../tests/test_multitenant_api.py#L276) | 276 | `"    store.add_membership(tenant_id, user_id, \"owner\")"` | — |
| [SRC-4405E7912C-L000277](../../tests/test_multitenant_api.py#L277) | 277 | `"    token = \"approved-diagnostics-token-\" + \"A\" * 32"` | — |
| [SRC-4405E7912C-L000278](../../tests/test_multitenant_api.py#L278) | 278 | `"    store.create_api_token(token, tenant_id, user_id)"` | — |
| [SRC-4405E7912C-L000279](../../tests/test_multitenant_api.py#L279) | 279 | `"    observed = {}"` | — |
| [SRC-4405E7912C-L000280](../../tests/test_multitenant_api.py#L280) | 280 | `""` | — |
| [SRC-4405E7912C-L000281](../../tests/test_multitenant_api.py#L281) | 281 | `"    def fake_diagnostics(self, *, test_model, test_social):"` | — |
| [SRC-4405E7912C-L000282](../../tests/test_multitenant_api.py#L282) | 282 | `"        observed[\"test_model\"] = test_model"` | — |
| [SRC-4405E7912C-L000283](../../tests/test_multitenant_api.py#L283) | 283 | `"        observed[\"test_social\"] = test_social"` | — |
| [SRC-4405E7912C-L000284](../../tests/test_multitenant_api.py#L284) | 284 | `"        return {\"overall_status\": \"passed\", \"model_usage\": []}"` | — |
| [SRC-4405E7912C-L000285](../../tests/test_multitenant_api.py#L285) | 285 | `""` | — |
| [SRC-4405E7912C-L000286](../../tests/test_multitenant_api.py#L286) | 286 | `"    monkeypatch.setattr(WebAgent, \"diagnostics\", fake_diagnostics)"` | — |
| [SRC-4405E7912C-L000287](../../tests/test_multitenant_api.py#L287) | 287 | `"    status, result = request_json("` | — |
| [SRC-4405E7912C-L000288](../../tests/test_multitenant_api.py#L288) | 288 | `"        base,"` | — |
| [SRC-4405E7912C-L000289](../../tests/test_multitenant_api.py#L289) | 289 | `"        \"/api/diagnostics\","` | — |
| [SRC-4405E7912C-L000290](../../tests/test_multitenant_api.py#L290) | 290 | `"        method=\"POST\","` | — |
| [SRC-4405E7912C-L000291](../../tests/test_multitenant_api.py#L291) | 291 | `"        token=token,"` | — |
| [SRC-4405E7912C-L000292](../../tests/test_multitenant_api.py#L292) | 292 | `"        payload={"` | — |
| [SRC-4405E7912C-L000293](../../tests/test_multitenant_api.py#L293) | 293 | `"            \"test_model\": True,"` | — |
| [SRC-4405E7912C-L000294](../../tests/test_multitenant_api.py#L294) | 294 | `"            \"test_social\": False,"` | — |
| [SRC-4405E7912C-L000295](../../tests/test_multitenant_api.py#L295) | 295 | `"            \"allow_provider_usage\": True,"` | — |
| [SRC-4405E7912C-L000296](../../tests/test_multitenant_api.py#L296) | 296 | `"        },"` | — |
| [SRC-4405E7912C-L000297](../../tests/test_multitenant_api.py#L297) | 297 | `"    )"` | — |
| [SRC-4405E7912C-L000298](../../tests/test_multitenant_api.py#L298) | 298 | `"    assert status == 200"` | — |
| [SRC-4405E7912C-L000299](../../tests/test_multitenant_api.py#L299) | 299 | `"    assert result[\"overall_status\"] == \"passed\""` | — |
| [SRC-4405E7912C-L000300](../../tests/test_multitenant_api.py#L300) | 300 | `"    assert observed == {\"test_model\": True, \"test_social\": False}"` | — |
| [SRC-4405E7912C-L000301](../../tests/test_multitenant_api.py#L301) | 301 | `""` | — |
| [SRC-4405E7912C-L000302](../../tests/test_multitenant_api.py#L302) | 302 | `""` | — |
| [SRC-4405E7912C-L000303](../../tests/test_multitenant_api.py#L303) | 303 | `""` | — |
| [SRC-4405E7912C-L000304](../../tests/test_multitenant_api.py#L304) | 304 | `"def test_viewer_cannot_invoke_agent_research_or_model_calls(tenant_api, monkeypatch):"` | — |
| [SRC-4405E7912C-L000305](../../tests/test_multitenant_api.py#L305) | 305 | `"    from api.omarai import WebAgent"` | — |
| [SRC-4405E7912C-L000306](../../tests/test_multitenant_api.py#L306) | 306 | `""` | — |
| [SRC-4405E7912C-L000307](../../tests/test_multitenant_api.py#L307) | 307 | `"    base, store = tenant_api"` | — |
| [SRC-4405E7912C-L000308](../../tests/test_multitenant_api.py#L308) | 308 | `"    monkeypatch.setattr(Handler, \"_rate_limit_ok\", lambda self: True)"` | — |
| [SRC-4405E7912C-L000309](../../tests/test_multitenant_api.py#L309) | 309 | `"    tenant_id = store.create_tenant(\"Viewer Agent Block\", \"viewer-agent-block\")"` | — |
| [SRC-4405E7912C-L000310](../../tests/test_multitenant_api.py#L310) | 310 | `"    user_id = store.create_user(\"viewer-agent@example.test\", \"Viewer\")"` | — |
| [SRC-4405E7912C-L000311](../../tests/test_multitenant_api.py#L311) | 311 | `"    store.add_membership(tenant_id, user_id, \"viewer\")"` | — |
| [SRC-4405E7912C-L000312](../../tests/test_multitenant_api.py#L312) | 312 | `"    token = \"viewer-agent-token-\" + \"W\" * 32"` | — |
| [SRC-4405E7912C-L000313](../../tests/test_multitenant_api.py#L313) | 313 | `"    store.create_api_token(token, tenant_id, user_id)"` | — |
| [SRC-4405E7912C-L000314](../../tests/test_multitenant_api.py#L314) | 314 | `""` | — |
| [SRC-4405E7912C-L000315](../../tests/test_multitenant_api.py#L315) | 315 | `"    def unexpected_answer(*_args, **_kwargs):"` | — |
| [SRC-4405E7912C-L000316](../../tests/test_multitenant_api.py#L316) | 316 | `"        pytest.fail(\"viewer must be denied before agent/model execution\")"` | — |
| [SRC-4405E7912C-L000317](../../tests/test_multitenant_api.py#L317) | 317 | `""` | — |
| [SRC-4405E7912C-L000318](../../tests/test_multitenant_api.py#L318) | 318 | `"    monkeypatch.setattr(WebAgent, \"answer\", unexpected_answer)"` | — |
| [SRC-4405E7912C-L000319](../../tests/test_multitenant_api.py#L319) | 319 | `"    status, result = request_json("` | — |
| [SRC-4405E7912C-L000320](../../tests/test_multitenant_api.py#L320) | 320 | `"        base,"` | — |
| [SRC-4405E7912C-L000321](../../tests/test_multitenant_api.py#L321) | 321 | `"        \"/api/agent\","` | — |
| [SRC-4405E7912C-L000322](../../tests/test_multitenant_api.py#L322) | 322 | `"        method=\"POST\","` | — |
| [SRC-4405E7912C-L000323](../../tests/test_multitenant_api.py#L323) | 323 | `"        token=token,"` | — |
| [SRC-4405E7912C-L000324](../../tests/test_multitenant_api.py#L324) | 324 | `"        payload={\"question\": \"نفّذ بحثًا جديدًا\"},"` | — |
| [SRC-4405E7912C-L000325](../../tests/test_multitenant_api.py#L325) | 325 | `"    )"` | — |
| [SRC-4405E7912C-L000326](../../tests/test_multitenant_api.py#L326) | 326 | `"    assert status == 403"` | — |
| [SRC-4405E7912C-L000327](../../tests/test_multitenant_api.py#L327) | 327 | `"    assert \"viewer\" in result[\"error\"]"` | — |
| [SRC-4405E7912C-L000328](../../tests/test_multitenant_api.py#L328) | 328 | `""` | — |
| [SRC-4405E7912C-L000329](../../tests/test_multitenant_api.py#L329) | 329 | `""` | — |
| [SRC-4405E7912C-L000330](../../tests/test_multitenant_api.py#L330) | 330 | `"def test_agent_api_allowlists_and_forwards_the_hosted_smoke_budget_profile("` | — |
| [SRC-4405E7912C-L000331](../../tests/test_multitenant_api.py#L331) | 331 | `"    tenant_api, monkeypatch"` | — |
| [SRC-4405E7912C-L000332](../../tests/test_multitenant_api.py#L332) | 332 | `"):"` | — |
| [SRC-4405E7912C-L000333](../../tests/test_multitenant_api.py#L333) | 333 | `"    from api.omarai import WebAgent"` | — |
| [SRC-4405E7912C-L000334](../../tests/test_multitenant_api.py#L334) | 334 | `""` | — |
| [SRC-4405E7912C-L000335](../../tests/test_multitenant_api.py#L335) | 335 | `"    base, store = tenant_api"` | — |
| [SRC-4405E7912C-L000336](../../tests/test_multitenant_api.py#L336) | 336 | `"    tenant_id = store.create_tenant(\"Smoke Profile Owner\", \"smoke-profile-owner\")"` | — |
| [SRC-4405E7912C-L000337](../../tests/test_multitenant_api.py#L337) | 337 | `"    user_id = store.create_user(\"smoke-profile@example.test\", \"Smoke Profile Owner\")"` | — |
| [SRC-4405E7912C-L000338](../../tests/test_multitenant_api.py#L338) | 338 | `"    store.add_membership(tenant_id, user_id, \"sales_agent\")"` | — |
| [SRC-4405E7912C-L000339](../../tests/test_multitenant_api.py#L339) | 339 | `"    token = \"smoke-profile-token-\" + \"P\" * 32"` | — |
| [SRC-4405E7912C-L000340](../../tests/test_multitenant_api.py#L340) | 340 | `"    store.create_api_token(token, tenant_id, user_id)"` | — |
| [SRC-4405E7912C-L000341](../../tests/test_multitenant_api.py#L341) | 341 | `"    observed = {}"` | — |
| [SRC-4405E7912C-L000342](../../tests/test_multitenant_api.py#L342) | 342 | `""` | — |
| [SRC-4405E7912C-L000343](../../tests/test_multitenant_api.py#L343) | 343 | `"    def fake_answer(self, question, history=None, mode=\"auto\", *, budget_profile=\"default\"):"` | — |
| [SRC-4405E7912C-L000344](../../tests/test_multitenant_api.py#L344) | 344 | `"        observed.update({"` | — |
| [SRC-4405E7912C-L000345](../../tests/test_multitenant_api.py#L345) | 345 | `"            \"question\": question,"` | — |
| [SRC-4405E7912C-L000346](../../tests/test_multitenant_api.py#L346) | 346 | `"            \"history\": history,"` | — |
| [SRC-4405E7912C-L000347](../../tests/test_multitenant_api.py#L347) | 347 | `"            \"mode\": mode,"` | — |
| [SRC-4405E7912C-L000348](../../tests/test_multitenant_api.py#L348) | 348 | `"            \"budget_profile\": budget_profile,"` | — |
| [SRC-4405E7912C-L000349](../../tests/test_multitenant_api.py#L349) | 349 | `"        })"` | — |
| [SRC-4405E7912C-L000350](../../tests/test_multitenant_api.py#L350) | 350 | `"        return {\"answer\": \"test answer\"}"` | — |
| [SRC-4405E7912C-L000351](../../tests/test_multitenant_api.py#L351) | 351 | `""` | — |
| [SRC-4405E7912C-L000352](../../tests/test_multitenant_api.py#L352) | 352 | `"    monkeypatch.setattr(WebAgent, \"answer\", fake_answer)"` | — |
| [SRC-4405E7912C-L000353](../../tests/test_multitenant_api.py#L353) | 353 | `"    status, result = request_json("` | — |
| [SRC-4405E7912C-L000354](../../tests/test_multitenant_api.py#L354) | 354 | `"        base,"` | — |
| [SRC-4405E7912C-L000355](../../tests/test_multitenant_api.py#L355) | 355 | `"        \"/api/agent\","` | — |
| [SRC-4405E7912C-L000356](../../tests/test_multitenant_api.py#L356) | 356 | `"        method=\"POST\","` | — |
| [SRC-4405E7912C-L000357](../../tests/test_multitenant_api.py#L357) | 357 | `"        token=token,"` | — |
| [SRC-4405E7912C-L000358](../../tests/test_multitenant_api.py#L358) | 358 | `"        payload={"` | — |
| [SRC-4405E7912C-L000359](../../tests/test_multitenant_api.py#L359) | 359 | `"            \"question\": \"اختبار ميزانية القبول\","` | — |
| [SRC-4405E7912C-L000360](../../tests/test_multitenant_api.py#L360) | 360 | `"            \"mode\": \"auto\","` | — |
| [SRC-4405E7912C-L000361](../../tests/test_multitenant_api.py#L361) | 361 | `"            \"request_profile\": \"hosted_smoke\","` | — |
| [SRC-4405E7912C-L000362](../../tests/test_multitenant_api.py#L362) | 362 | `"        },"` | — |
| [SRC-4405E7912C-L000363](../../tests/test_multitenant_api.py#L363) | 363 | `"    )"` | — |
| [SRC-4405E7912C-L000364](../../tests/test_multitenant_api.py#L364) | 364 | `"    assert status == 200"` | — |
| [SRC-4405E7912C-L000365](../../tests/test_multitenant_api.py#L365) | 365 | `"    assert result[\"answer\"] == \"test answer\""` | — |
| [SRC-4405E7912C-L000366](../../tests/test_multitenant_api.py#L366) | 366 | `"    assert observed == {"` | — |
| [SRC-4405E7912C-L000367](../../tests/test_multitenant_api.py#L367) | 367 | `"        \"question\": \"اختبار ميزانية القبول\","` | — |
| [SRC-4405E7912C-L000368](../../tests/test_multitenant_api.py#L368) | 368 | `"        \"history\": [],"` | — |
| [SRC-4405E7912C-L000369](../../tests/test_multitenant_api.py#L369) | 369 | `"        \"mode\": \"auto\","` | — |
| [SRC-4405E7912C-L000370](../../tests/test_multitenant_api.py#L370) | 370 | `"        \"budget_profile\": \"hosted_smoke\","` | — |
| [SRC-4405E7912C-L000371](../../tests/test_multitenant_api.py#L371) | 371 | `"    }"` | — |
| [SRC-4405E7912C-L000372](../../tests/test_multitenant_api.py#L372) | 372 | `""` | — |
| [SRC-4405E7912C-L000373](../../tests/test_multitenant_api.py#L373) | 373 | `"    status, error = request_json("` | — |
| [SRC-4405E7912C-L000374](../../tests/test_multitenant_api.py#L374) | 374 | `"        base,"` | — |
| [SRC-4405E7912C-L000375](../../tests/test_multitenant_api.py#L375) | 375 | `"        \"/api/agent\","` | — |
| [SRC-4405E7912C-L000376](../../tests/test_multitenant_api.py#L376) | 376 | `"        method=\"POST\","` | — |
| [SRC-4405E7912C-L000377](../../tests/test_multitenant_api.py#L377) | 377 | `"        token=token,"` | — |
| [SRC-4405E7912C-L000378](../../tests/test_multitenant_api.py#L378) | 378 | `"        payload={\"question\": \"اختبار ملف غير مسموح\", \"request_profile\": \"unbounded\"},"` | — |
| [SRC-4405E7912C-L000379](../../tests/test_multitenant_api.py#L379) | 379 | `"    )"` | — |
| [SRC-4405E7912C-L000380](../../tests/test_multitenant_api.py#L380) | 380 | `"    assert status == 400"` | — |
| [SRC-4405E7912C-L000381](../../tests/test_multitenant_api.py#L381) | 381 | `"    assert \"request_profile\" in error[\"error\"]"` | — |
| [SRC-4405E7912C-L000382](../../tests/test_multitenant_api.py#L382) | 382 | `"    assert observed[\"budget_profile\"] == \"hosted_smoke\""` | — |
| [SRC-4405E7912C-L000383](../../tests/test_multitenant_api.py#L383) | 383 | `""` | — |
| [SRC-4405E7912C-L000384](../../tests/test_multitenant_api.py#L384) | 384 | `"    status, result = request_json("` | — |
| [SRC-4405E7912C-L000385](../../tests/test_multitenant_api.py#L385) | 385 | `"        base,"` | — |
| [SRC-4405E7912C-L000386](../../tests/test_multitenant_api.py#L386) | 386 | `"        \"/api/agent\","` | — |
| [SRC-4405E7912C-L000387](../../tests/test_multitenant_api.py#L387) | 387 | `"        method=\"POST\","` | — |
| [SRC-4405E7912C-L000388](../../tests/test_multitenant_api.py#L388) | 388 | `"        token=token,"` | — |
| [SRC-4405E7912C-L000389](../../tests/test_multitenant_api.py#L389) | 389 | `"        payload={\"question\": \"اختبار التوافق مع الملف الافتراضي\"},"` | — |
| [SRC-4405E7912C-L000390](../../tests/test_multitenant_api.py#L390) | 390 | `"    )"` | — |
| [SRC-4405E7912C-L000391](../../tests/test_multitenant_api.py#L391) | 391 | `"    assert status == 200"` | — |
| [SRC-4405E7912C-L000392](../../tests/test_multitenant_api.py#L392) | 392 | `"    assert result[\"answer\"] == \"test answer\""` | — |
| [SRC-4405E7912C-L000393](../../tests/test_multitenant_api.py#L393) | 393 | `"    assert observed[\"budget_profile\"] == \"default\""` | — |
## اختبارات

### FILE-44CDA52D01 — [tests/test_omarai.py](../../tests/test_omarai.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-44CDA52D01-L000001](../../tests/test_omarai.py#L1) | 1 | `"import csv"` | — |
| [SRC-44CDA52D01-L000002](../../tests/test_omarai.py#L2) | 2 | `""` | — |
| [SRC-44CDA52D01-L000003](../../tests/test_omarai.py#L3) | 3 | `"import pytest"` | — |
| [SRC-44CDA52D01-L000004](../../tests/test_omarai.py#L4) | 4 | `""` | — |
| [SRC-44CDA52D01-L000005](../../tests/test_omarai.py#L5) | 5 | `"from agents.omarai import LeadStore, analyze, normalize"` | — |
| [SRC-44CDA52D01-L000006](../../tests/test_omarai.py#L6) | 6 | `""` | — |
| [SRC-44CDA52D01-L000007](../../tests/test_omarai.py#L7) | 7 | `""` | — |
| [SRC-44CDA52D01-L000008](../../tests/test_omarai.py#L8) | 8 | `"def test_arabic_normalization():"` | — |
| [SRC-44CDA52D01-L000009](../../tests/test_omarai.py#L9) | 9 | `"    assert normalize(\"إيجارٌ ـ شقة\") == normalize(\"ايجار شقة\")"` | — |
| [SRC-44CDA52D01-L000010](../../tests/test_omarai.py#L10) | 10 | `""` | — |
| [SRC-44CDA52D01-L000011](../../tests/test_omarai.py#L11) | 11 | `"def test_high_intent_with_next_step():"` | — |
| [SRC-44CDA52D01-L000012](../../tests/test_omarai.py#L12) | 12 | `"    result=analyze(\"بدور على شقة وممكن معاينة\")"` | — |
| [SRC-44CDA52D01-L000013](../../tests/test_omarai.py#L13) | 13 | `"    assert result[\"label\"]==\"high_intent\""` | — |
| [SRC-44CDA52D01-L000014](../../tests/test_omarai.py#L14) | 14 | `"    assert result[\"score\"]>=55"` | — |
| [SRC-44CDA52D01-L000015](../../tests/test_omarai.py#L15) | 15 | `""` | — |
| [SRC-44CDA52D01-L000016](../../tests/test_omarai.py#L16) | 16 | `"def test_non_buyer_override():"` | — |
| [SRC-44CDA52D01-L000017](../../tests/test_omarai.py#L17) | 17 | `"    result=analyze(\"مش عايز اشتري، عايز ابيع شقة\")"` | — |
| [SRC-44CDA52D01-L000018](../../tests/test_omarai.py#L18) | 18 | `"    assert result[\"label\"]==\"not_buyer_signal\""` | — |
| [SRC-44CDA52D01-L000019](../../tests/test_omarai.py#L19) | 19 | `"    assert result[\"score\"]==0"` | — |
| [SRC-44CDA52D01-L000020](../../tests/test_omarai.py#L20) | 20 | `""` | — |
| [SRC-44CDA52D01-L000021](../../tests/test_omarai.py#L21) | 21 | `"def test_empty_text_rejected():"` | — |
| [SRC-44CDA52D01-L000022](../../tests/test_omarai.py#L22) | 22 | `"    with pytest.raises(ValueError):"` | — |
| [SRC-44CDA52D01-L000023](../../tests/test_omarai.py#L23) | 23 | `"        analyze(\" \")"` | — |
| [SRC-44CDA52D01-L000024](../../tests/test_omarai.py#L24) | 24 | `""` | — |
| [SRC-44CDA52D01-L000025](../../tests/test_omarai.py#L25) | 25 | `"def test_url_required_and_validated(tmp_path):"` | — |
| [SRC-44CDA52D01-L000026](../../tests/test_omarai.py#L26) | 26 | `"    store=LeadStore(tmp_path/\"db.sqlite3\")"` | — |
| [SRC-44CDA52D01-L000027](../../tests/test_omarai.py#L27) | 27 | `"    with pytest.raises(ValueError):"` | — |
| [SRC-44CDA52D01-L000028](../../tests/test_omarai.py#L28) | 28 | `"        store.add(\"بدور على شقة\",\"\",\"manual\")"` | — |
| [SRC-44CDA52D01-L000029](../../tests/test_omarai.py#L29) | 29 | `"    with pytest.raises(ValueError):"` | — |
| [SRC-44CDA52D01-L000030](../../tests/test_omarai.py#L30) | 30 | `"        store.add(\"بدور على شقة\",\"file:///tmp/private\",\"manual\")"` | — |
| [SRC-44CDA52D01-L000031](../../tests/test_omarai.py#L31) | 31 | `""` | — |
| [SRC-44CDA52D01-L000032](../../tests/test_omarai.py#L32) | 32 | `"def test_duplicate_is_idempotent(tmp_path):"` | — |
| [SRC-44CDA52D01-L000033](../../tests/test_omarai.py#L33) | 33 | `"    store=LeadStore(tmp_path/\"db.sqlite3\")"` | — |
| [SRC-44CDA52D01-L000034](../../tests/test_omarai.py#L34) | 34 | `"    one,created1=store.add(\"بدور على شقة\",\"https://example.com/post/1\",\"facebook\")"` | — |
| [SRC-44CDA52D01-L000035](../../tests/test_omarai.py#L35) | 35 | `"    two,created2=store.add(\"بدور على شقة\",\"https://example.com/post/1\",\"facebook\")"` | — |
| [SRC-44CDA52D01-L000036](../../tests/test_omarai.py#L36) | 36 | `"    assert created1 is True and created2 is False"` | — |
| [SRC-44CDA52D01-L000037](../../tests/test_omarai.py#L37) | 37 | `"    assert one[\"id\"]==two[\"id\"]"` | — |
| [SRC-44CDA52D01-L000038](../../tests/test_omarai.py#L38) | 38 | `"    assert len(store.list())==1"` | — |
| [SRC-44CDA52D01-L000039](../../tests/test_omarai.py#L39) | 39 | `""` | — |
| [SRC-44CDA52D01-L000040](../../tests/test_omarai.py#L40) | 40 | `"def test_status_updates_are_explicit(tmp_path):"` | — |
| [SRC-44CDA52D01-L000041](../../tests/test_omarai.py#L41) | 41 | `"    store=LeadStore(tmp_path/\"db.sqlite3\")"` | — |
| [SRC-44CDA52D01-L000042](../../tests/test_omarai.py#L42) | 42 | `"    lead,_=store.add(\"بدور على شقة\",\"https://example.com/p\",\"manual\")"` | — |
| [SRC-44CDA52D01-L000043](../../tests/test_omarai.py#L43) | 43 | `"    updated=store.update_status(lead[\"id\"],\"qualified\")"` | — |
| [SRC-44CDA52D01-L000044](../../tests/test_omarai.py#L44) | 44 | `"    assert updated[\"status\"]==\"qualified\""` | — |
| [SRC-44CDA52D01-L000045](../../tests/test_omarai.py#L45) | 45 | `"    with pytest.raises(ValueError):"` | — |
| [SRC-44CDA52D01-L000046](../../tests/test_omarai.py#L46) | 46 | `"        store.update_status(lead[\"id\"],\"magic\")"` | — |
| [SRC-44CDA52D01-L000047](../../tests/test_omarai.py#L47) | 47 | `""` | — |
| [SRC-44CDA52D01-L000048](../../tests/test_omarai.py#L48) | 48 | `"def test_csv_requires_columns(tmp_path):"` | — |
| [SRC-44CDA52D01-L000049](../../tests/test_omarai.py#L49) | 49 | `"    bad=tmp_path/\"bad.csv\""` | — |
| [SRC-44CDA52D01-L000050](../../tests/test_omarai.py#L50) | 50 | `"    bad.write_text(\"foo,bar\\na,b\\n\",encoding=\"utf-8\")"` | — |
| [SRC-44CDA52D01-L000051](../../tests/test_omarai.py#L51) | 51 | `"    store=LeadStore(tmp_path/\"db.sqlite3\")"` | — |
| [SRC-44CDA52D01-L000052](../../tests/test_omarai.py#L52) | 52 | `"    with pytest.raises(ValueError):"` | — |
| [SRC-44CDA52D01-L000053](../../tests/test_omarai.py#L53) | 53 | `"        store.import_csv(bad)"` | — |
| [SRC-44CDA52D01-L000054](../../tests/test_omarai.py#L54) | 54 | `""` | — |
| [SRC-44CDA52D01-L000055](../../tests/test_omarai.py#L55) | 55 | `"def test_csv_export_neutralizes_spreadsheet_formula_injection(tmp_path):"` | — |
| [SRC-44CDA52D01-L000056](../../tests/test_omarai.py#L56) | 56 | `"    store = LeadStore(tmp_path / \"db.sqlite3\")"` | — |
| [SRC-44CDA52D01-L000057](../../tests/test_omarai.py#L57) | 57 | `"    store.add("` | — |
| [SRC-44CDA52D01-L000058](../../tests/test_omarai.py#L58) | 58 | `"        '=HYPERLINK(\"https://evil.example\",\"click\")',"` | — |
| [SRC-44CDA52D01-L000059](../../tests/test_omarai.py#L59) | 59 | `"        \"https://example.com/post/1\","` | — |
| [SRC-44CDA52D01-L000060](../../tests/test_omarai.py#L60) | 60 | `"        platform=\"manual\","` | — |
| [SRC-44CDA52D01-L000061](../../tests/test_omarai.py#L61) | 61 | `"        note=\"  +SUM(1,1)\","` | — |
| [SRC-44CDA52D01-L000062](../../tests/test_omarai.py#L62) | 62 | `"    )"` | — |
| [SRC-44CDA52D01-L000063](../../tests/test_omarai.py#L63) | 63 | `"    store.add("` | — |
| [SRC-44CDA52D01-L000064](../../tests/test_omarai.py#L64) | 64 | `"        \"\\u00a0\\ufeff=1+1\","` | — |
| [SRC-44CDA52D01-L000065](../../tests/test_omarai.py#L65) | 65 | `"        \"https://example.com/post/2\","` | — |
| [SRC-44CDA52D01-L000066](../../tests/test_omarai.py#L66) | 66 | `"        platform=\"manual\","` | — |
| [SRC-44CDA52D01-L000067](../../tests/test_omarai.py#L67) | 67 | `"        note=\"\\u00a0\\ufeff=SUM(1,1)\","` | — |
| [SRC-44CDA52D01-L000068](../../tests/test_omarai.py#L68) | 68 | `"    )"` | — |
| [SRC-44CDA52D01-L000069](../../tests/test_omarai.py#L69) | 69 | `"    destination = tmp_path / \"export.csv\""` | — |
| [SRC-44CDA52D01-L000070](../../tests/test_omarai.py#L70) | 70 | `"    assert store.export_csv(destination) == 2"` | — |
| [SRC-44CDA52D01-L000071](../../tests/test_omarai.py#L71) | 71 | `"    raw_csv = destination.read_text(encoding=\"utf-8-sig\")"` | — |
| [SRC-44CDA52D01-L000072](../../tests/test_omarai.py#L72) | 72 | `"    assert '\"\\t=HYPERLINK(' in raw_csv"` | — |
| [SRC-44CDA52D01-L000073](../../tests/test_omarai.py#L73) | 73 | `"    assert '\"\\t  +SUM' in raw_csv"` | — |
| [SRC-44CDA52D01-L000074](../../tests/test_omarai.py#L74) | 74 | `""` | — |
| [SRC-44CDA52D01-L000075](../../tests/test_omarai.py#L75) | 75 | `"    with destination.open(newline=\"\", encoding=\"utf-8-sig\") as stream:"` | — |
| [SRC-44CDA52D01-L000076](../../tests/test_omarai.py#L76) | 76 | `"        rows = list(csv.DictReader(stream))"` | — |
| [SRC-44CDA52D01-L000077](../../tests/test_omarai.py#L77) | 77 | `""` | — |
| [SRC-44CDA52D01-L000078](../../tests/test_omarai.py#L78) | 78 | `"    row1 = next(row for row in rows if row[\"source_url\"] == \"https://example.com/post/1\")"` | — |
| [SRC-44CDA52D01-L000079](../../tests/test_omarai.py#L79) | 79 | `"    row2 = next(row for row in rows if row[\"source_url\"] == \"https://example.com/post/2\")"` | — |
| [SRC-44CDA52D01-L000080](../../tests/test_omarai.py#L80) | 80 | `"    assert row1[\"text\"].startswith(\"\\t=\")"` | — |
| [SRC-44CDA52D01-L000081](../../tests/test_omarai.py#L81) | 81 | `"    assert row1[\"note\"].startswith(\"\\t  +\")"` | — |
| [SRC-44CDA52D01-L000082](../../tests/test_omarai.py#L82) | 82 | `"    assert row2[\"text\"].startswith(\"\\t\\ufeff=\")"` | — |
| [SRC-44CDA52D01-L000083](../../tests/test_omarai.py#L83) | 83 | `"    assert row2[\"note\"].startswith(\"\\t\\u00a0\\ufeff=\")"` | — |
| [SRC-44CDA52D01-L000084](../../tests/test_omarai.py#L84) | 84 | `""` | — |
| [SRC-44CDA52D01-L000085](../../tests/test_omarai.py#L85) | 85 | `""` | — |
| [SRC-44CDA52D01-L000086](../../tests/test_omarai.py#L86) | 86 | `""` | — |
| [SRC-44CDA52D01-L000087](../../tests/test_omarai.py#L87) | 87 | `"def test_generic_fire_alarm_and_supplier_requests_are_sector_neutral():"` | — |
| [SRC-44CDA52D01-L000088](../../tests/test_omarai.py#L88) | 88 | `"    fire_alarm = analyze(\"نحتاج نظام إنذار حريق للمصنع\")"` | — |
| [SRC-44CDA52D01-L000089](../../tests/test_omarai.py#L89) | 89 | `"    supplier = analyze(\"نبحث عن مورد لافتات لمشروع جديد\")"` | — |
| [SRC-44CDA52D01-L000090](../../tests/test_omarai.py#L90) | 90 | `"    assert fire_alarm[\"label\"] == \"high_intent\""` | — |
| [SRC-44CDA52D01-L000091](../../tests/test_omarai.py#L91) | 91 | `"    assert supplier[\"label\"] == \"high_intent\""` | — |
| [SRC-44CDA52D01-L000092](../../tests/test_omarai.py#L92) | 92 | `"    assert fire_alarm[\"score\"] >= 55"` | — |
| [SRC-44CDA52D01-L000093](../../tests/test_omarai.py#L93) | 93 | `"    assert supplier[\"score\"] >= 55"` | — |
| [SRC-44CDA52D01-L000094](../../tests/test_omarai.py#L94) | 94 | `""` | — |
| [SRC-44CDA52D01-L000095](../../tests/test_omarai.py#L95) | 95 | `""` | — |
| [SRC-44CDA52D01-L000096](../../tests/test_omarai.py#L96) | 96 | `"def test_product_mention_alone_does_not_create_a_demand_signal():"` | — |
| [SRC-44CDA52D01-L000097](../../tests/test_omarai.py#L97) | 97 | `"    result = analyze(\"نظام إنذار حريق\")"` | — |
| [SRC-44CDA52D01-L000098](../../tests/test_omarai.py#L98) | 98 | `"    assert result[\"label\"] == \"unclear\""` | — |
| [SRC-44CDA52D01-L000099](../../tests/test_omarai.py#L99) | 99 | `"    assert result[\"score\"] == 0"` | — |
| [SRC-44CDA52D01-L000100](../../tests/test_omarai.py#L100) | 100 | `""` | — |
| [SRC-44CDA52D01-L000101](../../tests/test_omarai.py#L101) | 101 | `""` | — |
| [SRC-44CDA52D01-L000102](../../tests/test_omarai.py#L102) | 102 | `"@pytest.mark.parametrize("` | — |
| [SRC-44CDA52D01-L000103](../../tests/test_omarai.py#L103) | 103 | `"    \"text\","` | — |
| [SRC-44CDA52D01-L000104](../../tests/test_omarai.py#L104) | 104 | `"    ["` | — |
| [SRC-44CDA52D01-L000105](../../tests/test_omarai.py#L105) | 105 | `"        \"مش بدور على شقة\","` | — |
| [SRC-44CDA52D01-L000106](../../tests/test_omarai.py#L106) | 106 | `"        \"مش محتاج نظام إنذار حريق\","` | — |
| [SRC-44CDA52D01-L000107](../../tests/test_omarai.py#L107) | 107 | `"        \"لا نحتاج مورد لافتات\","` | — |
| [SRC-44CDA52D01-L000108](../../tests/test_omarai.py#L108) | 108 | `"        \"not looking for a supplier\","` | — |
| [SRC-44CDA52D01-L000109](../../tests/test_omarai.py#L109) | 109 | `"        \"we do not need a fire alarm system\","` | — |
| [SRC-44CDA52D01-L000110](../../tests/test_omarai.py#L110) | 110 | `"    ],"` | — |
| [SRC-44CDA52D01-L000111](../../tests/test_omarai.py#L111) | 111 | `")"` | — |
| [SRC-44CDA52D01-L000112](../../tests/test_omarai.py#L112) | 112 | `"def test_explicit_negation_never_scores_as_buyer_intent(text):"` | — |
| [SRC-44CDA52D01-L000113](../../tests/test_omarai.py#L113) | 113 | `"    result = analyze(text)"` | — |
| [SRC-44CDA52D01-L000114](../../tests/test_omarai.py#L114) | 114 | `"    assert result[\"label\"] == \"not_buyer_signal\""` | — |
| [SRC-44CDA52D01-L000115](../../tests/test_omarai.py#L115) | 115 | `"    assert result[\"score\"] == 0"` | — |
| [SRC-44CDA52D01-L000116](../../tests/test_omarai.py#L116) | 116 | `""` | — |
| [SRC-44CDA52D01-L000117](../../tests/test_omarai.py#L117) | 117 | `""` | — |
| [SRC-44CDA52D01-L000118](../../tests/test_omarai.py#L118) | 118 | `"@pytest.mark.parametrize("` | — |
| [SRC-44CDA52D01-L000119](../../tests/test_omarai.py#L119) | 119 | `"    \"text\","` | — |
| [SRC-44CDA52D01-L000120](../../tests/test_omarai.py#L120) | 120 | `"    ["` | — |
| [SRC-44CDA52D01-L000121](../../tests/test_omarai.py#L121) | 121 | `"        \"تم الشراء بالفعل\","` | — |
| [SRC-44CDA52D01-L000122](../../tests/test_omarai.py#L122) | 122 | `"        \"وجدنا مورد وتم التعاقد\","` | — |
| [SRC-44CDA52D01-L000123](../../tests/test_omarai.py#L123) | 123 | `"        \"already purchased the equipment\","` | — |
| [SRC-44CDA52D01-L000124](../../tests/test_omarai.py#L124) | 124 | `"        \"supplier selected\","` | — |
| [SRC-44CDA52D01-L000125](../../tests/test_omarai.py#L125) | 125 | `"        \"كنت بدور على شقة\","` | — |
| [SRC-44CDA52D01-L000126](../../tests/test_omarai.py#L126) | 126 | `"    ],"` | — |
| [SRC-44CDA52D01-L000127](../../tests/test_omarai.py#L127) | 127 | `")"` | — |
| [SRC-44CDA52D01-L000128](../../tests/test_omarai.py#L128) | 128 | `"def test_completed_or_past_need_is_not_active_demand(text):"` | — |
| [SRC-44CDA52D01-L000129](../../tests/test_omarai.py#L129) | 129 | `"    result = analyze(text)"` | — |
| [SRC-44CDA52D01-L000130](../../tests/test_omarai.py#L130) | 130 | `"    assert result[\"label\"] == \"closed_or_stale_signal\""` | — |
| [SRC-44CDA52D01-L000131](../../tests/test_omarai.py#L131) | 131 | `"    assert result[\"score\"] == 0"` | — |
| [SRC-44CDA52D01-L000132](../../tests/test_omarai.py#L132) | 132 | `""` | — |
| [SRC-44CDA52D01-L000133](../../tests/test_omarai.py#L133) | 133 | `""` | — |
| [SRC-44CDA52D01-L000134](../../tests/test_omarai.py#L134) | 134 | `"def test_product_and_location_context_do_not_inflate_demand_score():"` | — |
| [SRC-44CDA52D01-L000135](../../tests/test_omarai.py#L135) | 135 | `"    result = analyze("` | — |
| [SRC-44CDA52D01-L000136](../../tests/test_omarai.py#L136) | 136 | `"        \"نظام إنذار حريق في القاهرة\","` | — |
| [SRC-44CDA52D01-L000137](../../tests/test_omarai.py#L137) | 137 | `"        product_terms=[\"نظام إنذار حريق\"],"` | — |
| [SRC-44CDA52D01-L000138](../../tests/test_omarai.py#L138) | 138 | `"        location_terms=[\"القاهرة\"],"` | — |
| [SRC-44CDA52D01-L000139](../../tests/test_omarai.py#L139) | 139 | `"    )"` | — |
| [SRC-44CDA52D01-L000140](../../tests/test_omarai.py#L140) | 140 | `"    assert result[\"score\"] == 0"` | — |
| [SRC-44CDA52D01-L000141](../../tests/test_omarai.py#L141) | 141 | `"    assert result[\"label\"] == \"unclear\""` | — |
| [SRC-44CDA52D01-L000142](../../tests/test_omarai.py#L142) | 142 | `"    assert {item[\"category\"] for item in result[\"matched_signals\"]} == {"` | — |
| [SRC-44CDA52D01-L000143](../../tests/test_omarai.py#L143) | 143 | `"        \"product_context\","` | — |
| [SRC-44CDA52D01-L000144](../../tests/test_omarai.py#L144) | 144 | `"        \"location_context\","` | — |
| [SRC-44CDA52D01-L000145](../../tests/test_omarai.py#L145) | 145 | `"    }"` | — |
| [SRC-44CDA52D01-L000146](../../tests/test_omarai.py#L146) | 146 | `""` | — |
| [SRC-44CDA52D01-L000147](../../tests/test_omarai.py#L147) | 147 | `""` | — |
| [SRC-44CDA52D01-L000148](../../tests/test_omarai.py#L148) | 148 | `""` | — |
| [SRC-44CDA52D01-L000149](../../tests/test_omarai.py#L149) | 149 | `"def test_lead_store_uses_domain_signal_and_qualification_contracts(tmp_path):"` | — |
| [SRC-44CDA52D01-L000150](../../tests/test_omarai.py#L150) | 150 | `"    store = LeadStore(tmp_path / \"domain-contracts.sqlite3\")"` | — |
| [SRC-44CDA52D01-L000151](../../tests/test_omarai.py#L151) | 151 | `"    lead, created = store.add("` | — |
| [SRC-44CDA52D01-L000152](../../tests/test_omarai.py#L152) | 152 | `"        \"نحتاج نظام إنذار حريق للمصنع\","` | — |
| [SRC-44CDA52D01-L000153](../../tests/test_omarai.py#L153) | 153 | `"        \"https://example.com/demand/1\","` | — |
| [SRC-44CDA52D01-L000154](../../tests/test_omarai.py#L154) | 154 | `"        platform=\"manual\","` | — |
| [SRC-44CDA52D01-L000155](../../tests/test_omarai.py#L155) | 155 | `"    )"` | — |
| [SRC-44CDA52D01-L000156](../../tests/test_omarai.py#L156) | 156 | `"    assert created is True"` | — |
| [SRC-44CDA52D01-L000157](../../tests/test_omarai.py#L157) | 157 | `"    assessment = lead[\"assessment\"]"` | — |
| [SRC-44CDA52D01-L000158](../../tests/test_omarai.py#L158) | 158 | `"    assert assessment[\"signal_type\"] == \"direct_purchase_request\""` | — |
| [SRC-44CDA52D01-L000159](../../tests/test_omarai.py#L159) | 159 | `"    assert assessment[\"domain_signal\"][\"signal_type\"] == \"direct_purchase_request\""` | — |
| [SRC-44CDA52D01-L000160](../../tests/test_omarai.py#L160) | 160 | `"    assert assessment[\"domain_signal\"][\"evidence\"][\"content_basis\"] == \"user_provided\""` | — |
| [SRC-44CDA52D01-L000161](../../tests/test_omarai.py#L161) | 161 | `"    assert assessment[\"domain_signal\"][\"product_fit\"] == \"unassessed\""` | — |
| [SRC-44CDA52D01-L000162](../../tests/test_omarai.py#L162) | 162 | `"    assert assessment[\"qualification\"][\"identity_status\"] == \"unknown\""` | — |
| [SRC-44CDA52D01-L000163](../../tests/test_omarai.py#L163) | 163 | `"    assert \"freshness\" in assessment[\"qualification\"][\"missing_information\"]"` | — |
| [SRC-44CDA52D01-L000164](../../tests/test_omarai.py#L164) | 164 | `""` | — |
| [SRC-44CDA52D01-L000165](../../tests/test_omarai.py#L165) | 165 | `""` | — |
| [SRC-44CDA52D01-L000166](../../tests/test_omarai.py#L166) | 166 | `"def test_explicit_demand_types_are_not_product_fit_or_purchase_probability():"` | — |
| [SRC-44CDA52D01-L000167](../../tests/test_omarai.py#L167) | 167 | `"    direct = analyze(\"نبحث عن مورد لافتات للمشروع\")"` | — |
| [SRC-44CDA52D01-L000168](../../tests/test_omarai.py#L168) | 168 | `"    quote = analyze(\"نحتاج عرض سعر لنظام إنذار حريق\")"` | — |
| [SRC-44CDA52D01-L000169](../../tests/test_omarai.py#L169) | 169 | `"    product_only = analyze(\"نظام إنذار حريق\")"` | — |
| [SRC-44CDA52D01-L000170](../../tests/test_omarai.py#L170) | 170 | `"    assert direct[\"signal_type\"] == \"direct_purchase_request\""` | — |
| [SRC-44CDA52D01-L000171](../../tests/test_omarai.py#L171) | 171 | `"    assert quote[\"signal_type\"] == \"request_for_quotation\""` | — |
| [SRC-44CDA52D01-L000172](../../tests/test_omarai.py#L172) | 172 | `"    assert product_only[\"signal_type\"] == \"unknown\""` | — |
## اختبارات

### FILE-851E7A87D6 — [tests/test_postgres_store.py](../../tests/test_postgres_store.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-851E7A87D6-L000001](../../tests/test_postgres_store.py#L1) | 1 | `"\"\"\"PostgreSQL integration tests for the Neon-backed LeadStore."` | — |
| [SRC-851E7A87D6-L000002](../../tests/test_postgres_store.py#L2) | 2 | `""` | — |
| [SRC-851E7A87D6-L000003](../../tests/test_postgres_store.py#L3) | 3 | `"These tests run only when OMARAI_TEST_DATABASE_URL points at an isolated test database."` | — |
| [SRC-851E7A87D6-L000004](../../tests/test_postgres_store.py#L4) | 4 | `"The CI workflow supplies an ephemeral PostgreSQL service; production credentials are never used."` | — |
| [SRC-851E7A87D6-L000005](../../tests/test_postgres_store.py#L5) | 5 | `"\"\"\""` | — |
| [SRC-851E7A87D6-L000006](../../tests/test_postgres_store.py#L6) | 6 | `"from __future__ import annotations"` | — |
| [SRC-851E7A87D6-L000007](../../tests/test_postgres_store.py#L7) | 7 | `""` | — |
| [SRC-851E7A87D6-L000008](../../tests/test_postgres_store.py#L8) | 8 | `"import os"` | — |
| [SRC-851E7A87D6-L000009](../../tests/test_postgres_store.py#L9) | 9 | `"import uuid"` | — |
| [SRC-851E7A87D6-L000010](../../tests/test_postgres_store.py#L10) | 10 | `""` | — |
| [SRC-851E7A87D6-L000011](../../tests/test_postgres_store.py#L11) | 11 | `"import pytest"` | — |
| [SRC-851E7A87D6-L000012](../../tests/test_postgres_store.py#L12) | 12 | `""` | — |
| [SRC-851E7A87D6-L000013](../../tests/test_postgres_store.py#L13) | 13 | `"from agents.omarai import LeadStore, _PostgresConnection, _qmark_to_psycopg"` | — |
| [SRC-851E7A87D6-L000014](../../tests/test_postgres_store.py#L14) | 14 | `""` | — |
| [SRC-851E7A87D6-L000015](../../tests/test_postgres_store.py#L15) | 15 | `""` | — |
| [SRC-851E7A87D6-L000016](../../tests/test_postgres_store.py#L16) | 16 | `"@pytest.fixture"` | — |
| [SRC-851E7A87D6-L000017](../../tests/test_postgres_store.py#L17) | 17 | `"def postgres_store():"` | — |
| [SRC-851E7A87D6-L000018](../../tests/test_postgres_store.py#L18) | 18 | `"    database_url = os.getenv(\"OMARAI_TEST_DATABASE_URL\", \"\").strip()"` | — |
| [SRC-851E7A87D6-L000019](../../tests/test_postgres_store.py#L19) | 19 | `"    if not database_url:"` | — |
| [SRC-851E7A87D6-L000020](../../tests/test_postgres_store.py#L20) | 20 | `"        pytest.skip(\"OMARAI_TEST_DATABASE_URL is not configured\")"` | — |
| [SRC-851E7A87D6-L000021](../../tests/test_postgres_store.py#L21) | 21 | `"    return LeadStore(database_url=database_url)"` | — |
| [SRC-851E7A87D6-L000022](../../tests/test_postgres_store.py#L22) | 22 | `""` | — |
| [SRC-851E7A87D6-L000023](../../tests/test_postgres_store.py#L23) | 23 | `""` | — |
| [SRC-851E7A87D6-L000024](../../tests/test_postgres_store.py#L24) | 24 | `"def _tenant_user(store: LeadStore, marker: str) -> tuple[str, str]:"` | — |
| [SRC-851E7A87D6-L000025](../../tests/test_postgres_store.py#L25) | 25 | `"    tenant_id = store.create_tenant(f\"PostgreSQL test {marker}\", f\"pg-{marker}\")"` | — |
| [SRC-851E7A87D6-L000026](../../tests/test_postgres_store.py#L26) | 26 | `"    user_id = store.create_user(f\"{marker}@example.invalid\", f\"PostgreSQL {marker}\")"` | — |
| [SRC-851E7A87D6-L000027](../../tests/test_postgres_store.py#L27) | 27 | `"    store.add_membership(tenant_id, user_id, \"owner\")"` | — |
| [SRC-851E7A87D6-L000028](../../tests/test_postgres_store.py#L28) | 28 | `"    return tenant_id, user_id"` | — |
| [SRC-851E7A87D6-L000029](../../tests/test_postgres_store.py#L29) | 29 | `""` | — |
| [SRC-851E7A87D6-L000030](../../tests/test_postgres_store.py#L30) | 30 | `""` | — |
| [SRC-851E7A87D6-L000031](../../tests/test_postgres_store.py#L31) | 31 | `"def test_postgres_leads_preserve_tenant_scoping_and_duplicate_semantics(postgres_store):"` | — |
| [SRC-851E7A87D6-L000032](../../tests/test_postgres_store.py#L32) | 32 | `"    marker = uuid.uuid4().hex"` | — |
| [SRC-851E7A87D6-L000033](../../tests/test_postgres_store.py#L33) | 33 | `"    tenant_a, _ = _tenant_user(postgres_store, f\"a-{marker}\")"` | — |
| [SRC-851E7A87D6-L000034](../../tests/test_postgres_store.py#L34) | 34 | `"    tenant_b, _ = _tenant_user(postgres_store, f\"b-{marker}\")"` | — |
| [SRC-851E7A87D6-L000035](../../tests/test_postgres_store.py#L35) | 35 | `"    text = f\"نبحث عن مورد لتجهيزات اختبار PostgreSQL {marker}\""` | — |
| [SRC-851E7A87D6-L000036](../../tests/test_postgres_store.py#L36) | 36 | `"    source_url = f\"https://example.com/postgres/{marker}\""` | — |
| [SRC-851E7A87D6-L000037](../../tests/test_postgres_store.py#L37) | 37 | `""` | — |
| [SRC-851E7A87D6-L000038](../../tests/test_postgres_store.py#L38) | 38 | `"    lead_a, created_a = postgres_store.add(text, source_url, tenant_id=tenant_a)"` | — |
| [SRC-851E7A87D6-L000039](../../tests/test_postgres_store.py#L39) | 39 | `"    lead_b, created_b = postgres_store.add(text, source_url, tenant_id=tenant_b)"` | — |
| [SRC-851E7A87D6-L000040](../../tests/test_postgres_store.py#L40) | 40 | `""` | — |
| [SRC-851E7A87D6-L000041](../../tests/test_postgres_store.py#L41) | 41 | `"    assert created_a is True"` | — |
| [SRC-851E7A87D6-L000042](../../tests/test_postgres_store.py#L42) | 42 | `"    assert created_b is True"` | — |
| [SRC-851E7A87D6-L000043](../../tests/test_postgres_store.py#L43) | 43 | `"    assert lead_a[\"id\"] != lead_b[\"id\"]"` | — |
| [SRC-851E7A87D6-L000044](../../tests/test_postgres_store.py#L44) | 44 | `"    assert [row[\"id\"] for row in postgres_store.list(tenant_id=tenant_a)] == [lead_a[\"id\"]]"` | — |
| [SRC-851E7A87D6-L000045](../../tests/test_postgres_store.py#L45) | 45 | `"    assert [row[\"id\"] for row in postgres_store.list(tenant_id=tenant_b)] == [lead_b[\"id\"]]"` | — |
| [SRC-851E7A87D6-L000046](../../tests/test_postgres_store.py#L46) | 46 | `""` | — |
| [SRC-851E7A87D6-L000047](../../tests/test_postgres_store.py#L47) | 47 | `"    duplicate, created_again = postgres_store.add("` | — |
| [SRC-851E7A87D6-L000048](../../tests/test_postgres_store.py#L48) | 48 | `"        text, source_url, tenant_id=tenant_a"` | — |
| [SRC-851E7A87D6-L000049](../../tests/test_postgres_store.py#L49) | 49 | `"    )"` | — |
| [SRC-851E7A87D6-L000050](../../tests/test_postgres_store.py#L50) | 50 | `"    assert created_again is False"` | — |
| [SRC-851E7A87D6-L000051](../../tests/test_postgres_store.py#L51) | 51 | `"    assert duplicate[\"id\"] == lead_a[\"id\"]"` | — |
| [SRC-851E7A87D6-L000052](../../tests/test_postgres_store.py#L52) | 52 | `""` | — |
| [SRC-851E7A87D6-L000053](../../tests/test_postgres_store.py#L53) | 53 | `"    assert postgres_store.update_status("` | — |
| [SRC-851E7A87D6-L000054](../../tests/test_postgres_store.py#L54) | 54 | `"        lead_a[\"id\"], \"qualified\", tenant_id=tenant_b"` | — |
| [SRC-851E7A87D6-L000055](../../tests/test_postgres_store.py#L55) | 55 | `"    ) is None"` | — |
| [SRC-851E7A87D6-L000056](../../tests/test_postgres_store.py#L56) | 56 | `"    updated = postgres_store.update_status("` | — |
| [SRC-851E7A87D6-L000057](../../tests/test_postgres_store.py#L57) | 57 | `"        lead_a[\"id\"], \"qualified\", tenant_id=tenant_a"` | — |
| [SRC-851E7A87D6-L000058](../../tests/test_postgres_store.py#L58) | 58 | `"    )"` | — |
| [SRC-851E7A87D6-L000059](../../tests/test_postgres_store.py#L59) | 59 | `"    assert updated[\"status\"] == \"qualified\""` | — |
| [SRC-851E7A87D6-L000060](../../tests/test_postgres_store.py#L60) | 60 | `"    assert postgres_store.list(\"qualified\", tenant_id=tenant_a)[0][\"id\"] == lead_a[\"id\"]"` | — |
| [SRC-851E7A87D6-L000061](../../tests/test_postgres_store.py#L61) | 61 | `"    assert postgres_store.list(tenant_id=tenant_b)[0][\"status\"] == \"new\""` | — |
| [SRC-851E7A87D6-L000062](../../tests/test_postgres_store.py#L62) | 62 | `""` | — |
| [SRC-851E7A87D6-L000063](../../tests/test_postgres_store.py#L63) | 63 | `""` | — |
| [SRC-851E7A87D6-L000064](../../tests/test_postgres_store.py#L64) | 64 | `"def test_postgres_tokens_sessions_and_reusable_workspace_records(postgres_store):"` | — |
| [SRC-851E7A87D6-L000065](../../tests/test_postgres_store.py#L65) | 65 | `"    marker = uuid.uuid4().hex"` | — |
| [SRC-851E7A87D6-L000066](../../tests/test_postgres_store.py#L66) | 66 | `"    tenant_id, user_id = _tenant_user(postgres_store, marker)"` | — |
| [SRC-851E7A87D6-L000067](../../tests/test_postgres_store.py#L67) | 67 | `"    token = f\"postgres-test-{marker}-\" + (\"T\" * 40)"` | — |
| [SRC-851E7A87D6-L000068](../../tests/test_postgres_store.py#L68) | 68 | `""` | — |
| [SRC-851E7A87D6-L000069](../../tests/test_postgres_store.py#L69) | 69 | `"    postgres_store.create_api_token(token, tenant_id, user_id, label=\"integration\")"` | — |
| [SRC-851E7A87D6-L000070](../../tests/test_postgres_store.py#L70) | 70 | `"    principal = postgres_store.resolve_api_token(token)"` | — |
| [SRC-851E7A87D6-L000071](../../tests/test_postgres_store.py#L71) | 71 | `"    assert principal == {\"tenant_id\": tenant_id, \"user_id\": user_id, \"role\": \"owner\"}"` | — |
| [SRC-851E7A87D6-L000072](../../tests/test_postgres_store.py#L72) | 72 | `""` | — |
| [SRC-851E7A87D6-L000073](../../tests/test_postgres_store.py#L73) | 73 | `"    created_session = postgres_store.create_web_session(token)"` | — |
| [SRC-851E7A87D6-L000074](../../tests/test_postgres_store.py#L74) | 74 | `"    assert created_session is not None"` | — |
| [SRC-851E7A87D6-L000075](../../tests/test_postgres_store.py#L75) | 75 | `"    session_id, session_principal = created_session"` | — |
| [SRC-851E7A87D6-L000076](../../tests/test_postgres_store.py#L76) | 76 | `"    assert session_principal == principal"` | — |
| [SRC-851E7A87D6-L000077](../../tests/test_postgres_store.py#L77) | 77 | `"    assert postgres_store.resolve_web_session(session_id) == principal"` | — |
| [SRC-851E7A87D6-L000078](../../tests/test_postgres_store.py#L78) | 78 | `"    assert postgres_store.revoke_web_session(session_id) is True"` | — |
| [SRC-851E7A87D6-L000079](../../tests/test_postgres_store.py#L79) | 79 | `"    assert postgres_store.resolve_web_session(session_id) is None"` | — |
| [SRC-851E7A87D6-L000080](../../tests/test_postgres_store.py#L80) | 80 | `""` | — |
| [SRC-851E7A87D6-L000081](../../tests/test_postgres_store.py#L81) | 81 | `"    profile_input = {"` | — |
| [SRC-851E7A87D6-L000082](../../tests/test_postgres_store.py#L82) | 82 | `"        \"product\": {\"name\": f\"PostgreSQL Widget {marker}\", \"aliases\": [\"Widget\"]},"` | — |
| [SRC-851E7A87D6-L000083](../../tests/test_postgres_store.py#L83) | 83 | `"        \"market\": {\"locations\": [\"Cairo\"], \"industries\": [\"Testing\"]},"` | — |
| [SRC-851E7A87D6-L000084](../../tests/test_postgres_store.py#L84) | 84 | `"    }"` | — |
| [SRC-851E7A87D6-L000085](../../tests/test_postgres_store.py#L85) | 85 | `"    profile = postgres_store.save_product_profile(profile_input, tenant_id=tenant_id)"` | — |
| [SRC-851E7A87D6-L000086](../../tests/test_postgres_store.py#L86) | 86 | `"    assert profile[\"name\"] == profile_input[\"product\"][\"name\"]"` | — |
| [SRC-851E7A87D6-L000087](../../tests/test_postgres_store.py#L87) | 87 | `"    assert postgres_store.get_product_profile("` | — |
| [SRC-851E7A87D6-L000088](../../tests/test_postgres_store.py#L88) | 88 | `"        profile[\"id\"], tenant_id=tenant_id"` | — |
| [SRC-851E7A87D6-L000089](../../tests/test_postgres_store.py#L89) | 89 | `"    )[\"profile\"] == profile_input"` | — |
| [SRC-851E7A87D6-L000090](../../tests/test_postgres_store.py#L90) | 90 | `"    assert postgres_store.list_product_profiles(tenant_id=tenant_id)[0][\"id\"] == profile[\"id\"]"` | — |
| [SRC-851E7A87D6-L000091](../../tests/test_postgres_store.py#L91) | 91 | `""` | — |
| [SRC-851E7A87D6-L000092](../../tests/test_postgres_store.py#L92) | 92 | `"    run = postgres_store.save_discovery_run("` | — |
| [SRC-851E7A87D6-L000093](../../tests/test_postgres_store.py#L93) | 93 | `"        profile[\"id\"],"` | — |
| [SRC-851E7A87D6-L000094](../../tests/test_postgres_store.py#L94) | 94 | `"        {"` | — |
| [SRC-851E7A87D6-L000095](../../tests/test_postgres_store.py#L95) | 95 | `"            \"answer\": \"تم العثور على طلب توريد معلن.\","` | — |
| [SRC-851E7A87D6-L000096](../../tests/test_postgres_store.py#L96) | 96 | `"            \"kind\": \"lead_discovery\","` | — |
| [SRC-851E7A87D6-L000097](../../tests/test_postgres_store.py#L97) | 97 | `"            \"search_queries\": [\"نبحث عن مورد\"],"` | — |
| [SRC-851E7A87D6-L000098](../../tests/test_postgres_store.py#L98) | 98 | `"            \"sources\": [{"` | — |
| [SRC-851E7A87D6-L000099](../../tests/test_postgres_store.py#L99) | 99 | `"                \"title\": \"طلب مورد تجريبي\","` | — |
| [SRC-851E7A87D6-L000100](../../tests/test_postgres_store.py#L100) | 100 | `"                \"url\": f\"https://example.com/demand/{marker}\","` | — |
| [SRC-851E7A87D6-L000101](../../tests/test_postgres_store.py#L101) | 101 | `"                \"snippet\": \"نبحث عن مورد لتوريد المنتج\","` | — |
| [SRC-851E7A87D6-L000102](../../tests/test_postgres_store.py#L102) | 102 | `"                \"platform\": \"web\","` | — |
| [SRC-851E7A87D6-L000103](../../tests/test_postgres_store.py#L103) | 103 | `"                \"lead_qualification\": \"public_demand_signal\","` | — |
| [SRC-851E7A87D6-L000104](../../tests/test_postgres_store.py#L104) | 104 | `"                \"lead_intent_evidence\": {"` | — |
| [SRC-851E7A87D6-L000105](../../tests/test_postgres_store.py#L105) | 105 | `"                    \"phrase\": \"نبحث عن مورد\","` | — |
| [SRC-851E7A87D6-L000106](../../tests/test_postgres_store.py#L106) | 106 | `"                    \"basis\": \"source_text\","` | — |
| [SRC-851E7A87D6-L000107](../../tests/test_postgres_store.py#L107) | 107 | `"                    \"signal_type\": \"direct_purchase_request\","` | — |
| [SRC-851E7A87D6-L000108](../../tests/test_postgres_store.py#L108) | 108 | `"                    \"product_fit\": \"unassessed\","` | — |
| [SRC-851E7A87D6-L000109](../../tests/test_postgres_store.py#L109) | 109 | `"                },"` | — |
| [SRC-851E7A87D6-L000110](../../tests/test_postgres_store.py#L110) | 110 | `"            }],"` | — |
| [SRC-851E7A87D6-L000111](../../tests/test_postgres_store.py#L111) | 111 | `"            \"search_report\": {\"search_outcome\": \"results_found\"},"` | — |
| [SRC-851E7A87D6-L000112](../../tests/test_postgres_store.py#L112) | 112 | `"        },"` | — |
| [SRC-851E7A87D6-L000113](../../tests/test_postgres_store.py#L113) | 113 | `"        tenant_id=tenant_id,"` | — |
| [SRC-851E7A87D6-L000114](../../tests/test_postgres_store.py#L114) | 114 | `"    )"` | — |
| [SRC-851E7A87D6-L000115](../../tests/test_postgres_store.py#L115) | 115 | `"    assert run[\"tenant_id\"] == tenant_id"` | — |
| [SRC-851E7A87D6-L000116](../../tests/test_postgres_store.py#L116) | 116 | `"    assert run[\"sources\"][0][\"lead_qualification\"] == \"public_demand_signal\""` | — |
| [SRC-851E7A87D6-L000117](../../tests/test_postgres_store.py#L117) | 117 | `"    assert postgres_store.get_discovery_run("` | — |
| [SRC-851E7A87D6-L000118](../../tests/test_postgres_store.py#L118) | 118 | `"        run[\"id\"], tenant_id=tenant_id"` | — |
| [SRC-851E7A87D6-L000119](../../tests/test_postgres_store.py#L119) | 119 | `"    )[\"id\"] == run[\"id\"]"` | — |
| [SRC-851E7A87D6-L000120](../../tests/test_postgres_store.py#L120) | 120 | `"    assert postgres_store.list_discovery_runs(tenant_id=tenant_id)[0][\"id\"] == run[\"id\"]"` | — |
| [SRC-851E7A87D6-L000121](../../tests/test_postgres_store.py#L121) | 121 | `""` | — |
| [SRC-851E7A87D6-L000122](../../tests/test_postgres_store.py#L122) | 122 | `"    saved_signal, created = postgres_store.save_discovery_signal("` | — |
| [SRC-851E7A87D6-L000123](../../tests/test_postgres_store.py#L123) | 123 | `"        run[\"id\"], 0, tenant_id=tenant_id"` | — |
| [SRC-851E7A87D6-L000124](../../tests/test_postgres_store.py#L124) | 124 | `"    )"` | — |
| [SRC-851E7A87D6-L000125](../../tests/test_postgres_store.py#L125) | 125 | `"    assert created is True"` | — |
| [SRC-851E7A87D6-L000126](../../tests/test_postgres_store.py#L126) | 126 | `"    assert saved_signal[\"tenant_id\"] == tenant_id"` | — |
| [SRC-851E7A87D6-L000127](../../tests/test_postgres_store.py#L127) | 127 | `"    assert postgres_store.revoke_api_token("` | — |
| [SRC-851E7A87D6-L000128](../../tests/test_postgres_store.py#L128) | 128 | `"        token, tenant_id=tenant_id, user_id=user_id"` | — |
| [SRC-851E7A87D6-L000129](../../tests/test_postgres_store.py#L129) | 129 | `"    ) is True"` | — |
| [SRC-851E7A87D6-L000130](../../tests/test_postgres_store.py#L130) | 130 | `"    assert postgres_store.resolve_api_token(token) is None"` | — |
| [SRC-851E7A87D6-L000131](../../tests/test_postgres_store.py#L131) | 131 | `""` | — |
| [SRC-851E7A87D6-L000132](../../tests/test_postgres_store.py#L132) | 132 | `""` | — |
| [SRC-851E7A87D6-L000133](../../tests/test_postgres_store.py#L133) | 133 | `"def test_postgres_placeholder_translation_skips_quoted_question_marks():"` | — |
| [SRC-851E7A87D6-L000134](../../tests/test_postgres_store.py#L134) | 134 | `"    sql = \"SELECT ?, '?' AS literal, \\\"?\\\" AS identifier, ? AS last_value\""` | — |
| [SRC-851E7A87D6-L000135](../../tests/test_postgres_store.py#L135) | 135 | `"    assert _qmark_to_psycopg(sql) == ("` | — |
| [SRC-851E7A87D6-L000136](../../tests/test_postgres_store.py#L136) | 136 | `"        \"SELECT %s, '?' AS literal, \\\"?\\\" AS identifier, %s AS last_value\""` | — |
| [SRC-851E7A87D6-L000137](../../tests/test_postgres_store.py#L137) | 137 | `"    )"` | — |
| [SRC-851E7A87D6-L000138](../../tests/test_postgres_store.py#L138) | 138 | `""` | — |
| [SRC-851E7A87D6-L000139](../../tests/test_postgres_store.py#L139) | 139 | `""` | — |
| [SRC-851E7A87D6-L000140](../../tests/test_postgres_store.py#L140) | 140 | `"def test_postgres_connection_adapter_converts_insert_or_ignore():"` | — |
| [SRC-851E7A87D6-L000141](../../tests/test_postgres_store.py#L141) | 141 | `"    class FakeConnection:"` | — |
| [SRC-851E7A87D6-L000142](../../tests/test_postgres_store.py#L142) | 142 | `"        statement = None"` | — |
| [SRC-851E7A87D6-L000143](../../tests/test_postgres_store.py#L143) | 143 | `"        params = None"` | — |
| [SRC-851E7A87D6-L000144](../../tests/test_postgres_store.py#L144) | 144 | `""` | — |
| [SRC-851E7A87D6-L000145](../../tests/test_postgres_store.py#L145) | 145 | `"        def execute(self, statement, params):"` | — |
| [SRC-851E7A87D6-L000146](../../tests/test_postgres_store.py#L146) | 146 | `"            self.statement = statement"` | — |
| [SRC-851E7A87D6-L000147](../../tests/test_postgres_store.py#L147) | 147 | `"            self.params = params"` | — |
| [SRC-851E7A87D6-L000148](../../tests/test_postgres_store.py#L148) | 148 | `"            return \"cursor\""` | — |
| [SRC-851E7A87D6-L000149](../../tests/test_postgres_store.py#L149) | 149 | `""` | — |
| [SRC-851E7A87D6-L000150](../../tests/test_postgres_store.py#L150) | 150 | `"    connection = FakeConnection()"` | — |
| [SRC-851E7A87D6-L000151](../../tests/test_postgres_store.py#L151) | 151 | `"    adapter = _PostgresConnection(connection)"` | — |
| [SRC-851E7A87D6-L000152](../../tests/test_postgres_store.py#L152) | 152 | `""` | — |
| [SRC-851E7A87D6-L000153](../../tests/test_postgres_store.py#L153) | 153 | `"    result = adapter.execute("` | — |
| [SRC-851E7A87D6-L000154](../../tests/test_postgres_store.py#L154) | 154 | `"        \"INSERT OR IGNORE INTO leads (id, note) VALUES (?, '?')\","` | — |
| [SRC-851E7A87D6-L000155](../../tests/test_postgres_store.py#L155) | 155 | `"        (\"lead-1\",),"` | — |
| [SRC-851E7A87D6-L000156](../../tests/test_postgres_store.py#L156) | 156 | `"    )"` | — |
| [SRC-851E7A87D6-L000157](../../tests/test_postgres_store.py#L157) | 157 | `""` | — |
| [SRC-851E7A87D6-L000158](../../tests/test_postgres_store.py#L158) | 158 | `"    assert result == \"cursor\""` | — |
| [SRC-851E7A87D6-L000159](../../tests/test_postgres_store.py#L159) | 159 | `"    assert connection.statement == ("` | — |
| [SRC-851E7A87D6-L000160](../../tests/test_postgres_store.py#L160) | 160 | `"        \"INSERT INTO leads (id, note) VALUES (%s, '?') ON CONFLICT DO NOTHING\""` | — |
| [SRC-851E7A87D6-L000161](../../tests/test_postgres_store.py#L161) | 161 | `"    )"` | — |
| [SRC-851E7A87D6-L000162](../../tests/test_postgres_store.py#L162) | 162 | `"    assert connection.params == (\"lead-1\",)"` | — |
| [SRC-851E7A87D6-L000163](../../tests/test_postgres_store.py#L163) | 163 | `""` | — |
| [SRC-851E7A87D6-L000164](../../tests/test_postgres_store.py#L164) | 164 | `""` | — |
| [SRC-851E7A87D6-L000165](../../tests/test_postgres_store.py#L165) | 165 | `"def test_postgres_database_url_rejects_unsupported_scheme():"` | — |
| [SRC-851E7A87D6-L000166](../../tests/test_postgres_store.py#L166) | 166 | `"    with pytest.raises(ValueError, match=\"PostgreSQL URL scheme\"):"` | — |
| [SRC-851E7A87D6-L000167](../../tests/test_postgres_store.py#L167) | 167 | `"        LeadStore(database_url=\"mysql://user:pass@example.com/db\")"` | — |
| [SRC-851E7A87D6-L000168](../../tests/test_postgres_store.py#L168) | 168 | `""` | — |
| [SRC-851E7A87D6-L000169](../../tests/test_postgres_store.py#L169) | 169 | `""` | — |
| [SRC-851E7A87D6-L000170](../../tests/test_postgres_store.py#L170) | 170 | `"def test_postgres_database_url_cannot_be_combined_with_sqlite_path(tmp_path):"` | — |
| [SRC-851E7A87D6-L000171](../../tests/test_postgres_store.py#L171) | 171 | `"    with pytest.raises(ValueError, match=\"either database_url or a SQLite path\"):"` | — |
| [SRC-851E7A87D6-L000172](../../tests/test_postgres_store.py#L172) | 172 | `"        LeadStore(tmp_path / \"local.sqlite3\", database_url=\"postgresql://user:pass@example.com/db\")"` | — |
## اختبارات

### FILE-B106ADC5EF — [tests/test_proxy_origin.py](../../tests/test_proxy_origin.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-B106ADC5EF-L000001](../../tests/test_proxy_origin.py#L1) | 1 | `"\"\"\"Regression tests for the proxy-aware Origin check. OMARAI-PROXY-ORIGIN-PATCH\"\"\""` | — |
| [SRC-B106ADC5EF-L000002](../../tests/test_proxy_origin.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-B106ADC5EF-L000003](../../tests/test_proxy_origin.py#L3) | 3 | `"import http.client"` | — |
| [SRC-B106ADC5EF-L000004](../../tests/test_proxy_origin.py#L4) | 4 | `"import threading"` | — |
| [SRC-B106ADC5EF-L000005](../../tests/test_proxy_origin.py#L5) | 5 | `"from http.server import ThreadingHTTPServer"` | — |
| [SRC-B106ADC5EF-L000006](../../tests/test_proxy_origin.py#L6) | 6 | `"import pytest"` | — |
| [SRC-B106ADC5EF-L000007](../../tests/test_proxy_origin.py#L7) | 7 | `"from agents.omarai import LeadStore"` | — |
| [SRC-B106ADC5EF-L000008](../../tests/test_proxy_origin.py#L8) | 8 | `"from api.omarai import Handler"` | — |
| [SRC-B106ADC5EF-L000009](../../tests/test_proxy_origin.py#L9) | 9 | `""` | — |
| [SRC-B106ADC5EF-L000010](../../tests/test_proxy_origin.py#L10) | 10 | `"TOKEN = \"t\" * 40"` | — |
| [SRC-B106ADC5EF-L000011](../../tests/test_proxy_origin.py#L11) | 11 | `"PUBLIC_NAME = \"app-1234.hosting.example\""` | — |
| [SRC-B106ADC5EF-L000012](../../tests/test_proxy_origin.py#L12) | 12 | `""` | — |
| [SRC-B106ADC5EF-L000013](../../tests/test_proxy_origin.py#L13) | 13 | `"@pytest.fixture"` | — |
| [SRC-B106ADC5EF-L000014](../../tests/test_proxy_origin.py#L14) | 14 | `"def port(tmp_path, monkeypatch):"` | — |
| [SRC-B106ADC5EF-L000015](../../tests/test_proxy_origin.py#L15) | 15 | `"    monkeypatch.setenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"1\")"` | — |
| [SRC-B106ADC5EF-L000016](../../tests/test_proxy_origin.py#L16) | 16 | `"    monkeypatch.setenv(\"OMARAI_ACCESS_TOKEN\", TOKEN)"` | — |
| [SRC-B106ADC5EF-L000017](../../tests/test_proxy_origin.py#L17) | 17 | `"    # The public host is explicitly configured; do not infer it from a client header."` | — |
| [SRC-B106ADC5EF-L000018](../../tests/test_proxy_origin.py#L18) | 18 | `"    monkeypatch.setenv(\"OMARAI_ALLOWED_ORIGINS\", \"https://\" + PUBLIC_NAME)"` | — |
| [SRC-B106ADC5EF-L000019](../../tests/test_proxy_origin.py#L19) | 19 | `"    monkeypatch.setattr(Handler, \"store\", LeadStore(tmp_path / \"origin-test.sqlite3\"))"` | — |
| [SRC-B106ADC5EF-L000020](../../tests/test_proxy_origin.py#L20) | 20 | `"    monkeypatch.setattr(Handler, \"RATE_LIMIT_REQUESTS\", 10_000)"` | — |
| [SRC-B106ADC5EF-L000021](../../tests/test_proxy_origin.py#L21) | 21 | `"    server = ThreadingHTTPServer((\"127.0.0.1\", 0), Handler)"` | — |
| [SRC-B106ADC5EF-L000022](../../tests/test_proxy_origin.py#L22) | 22 | `"    thread = threading.Thread(target=server.serve_forever, daemon=True)"` | — |
| [SRC-B106ADC5EF-L000023](../../tests/test_proxy_origin.py#L23) | 23 | `"    thread.start()"` | — |
| [SRC-B106ADC5EF-L000024](../../tests/test_proxy_origin.py#L24) | 24 | `"    try:"` | — |
| [SRC-B106ADC5EF-L000025](../../tests/test_proxy_origin.py#L25) | 25 | `"        yield server.server_port"` | — |
| [SRC-B106ADC5EF-L000026](../../tests/test_proxy_origin.py#L26) | 26 | `"    finally:"` | — |
| [SRC-B106ADC5EF-L000027](../../tests/test_proxy_origin.py#L27) | 27 | `"        server.shutdown()"` | — |
| [SRC-B106ADC5EF-L000028](../../tests/test_proxy_origin.py#L28) | 28 | `"        server.server_close()"` | — |
| [SRC-B106ADC5EF-L000029](../../tests/test_proxy_origin.py#L29) | 29 | `"        thread.join(timeout=3)"` | — |
| [SRC-B106ADC5EF-L000030](../../tests/test_proxy_origin.py#L30) | 30 | `""` | — |
| [SRC-B106ADC5EF-L000031](../../tests/test_proxy_origin.py#L31) | 31 | `"def call(port, method, extra):"` | — |
| [SRC-B106ADC5EF-L000032](../../tests/test_proxy_origin.py#L32) | 32 | `"    body = b'{\"question\": \"x\"}' if method == \"POST\" else b\"\""` | — |
| [SRC-B106ADC5EF-L000033](../../tests/test_proxy_origin.py#L33) | 33 | `"    headers = {\"Content-Type\": \"application/json\", \"Authorization\": \"Bearer \" + TOKEN, **extra}"` | — |
| [SRC-B106ADC5EF-L000034](../../tests/test_proxy_origin.py#L34) | 34 | `"    connection = http.client.HTTPConnection(\"127.0.0.1\", port, timeout=5)"` | — |
| [SRC-B106ADC5EF-L000035](../../tests/test_proxy_origin.py#L35) | 35 | `"    connection.putrequest(method, \"/api/ask\", skip_host=True)"` | — |
| [SRC-B106ADC5EF-L000036](../../tests/test_proxy_origin.py#L36) | 36 | `"    for name, value in headers.items():"` | — |
| [SRC-B106ADC5EF-L000037](../../tests/test_proxy_origin.py#L37) | 37 | `"        connection.putheader(name, value)"` | — |
| [SRC-B106ADC5EF-L000038](../../tests/test_proxy_origin.py#L38) | 38 | `"    connection.putheader(\"Content-Length\", str(len(body)))"` | — |
| [SRC-B106ADC5EF-L000039](../../tests/test_proxy_origin.py#L39) | 39 | `"    connection.endheaders()"` | — |
| [SRC-B106ADC5EF-L000040](../../tests/test_proxy_origin.py#L40) | 40 | `"    if body:"` | — |
| [SRC-B106ADC5EF-L000041](../../tests/test_proxy_origin.py#L41) | 41 | `"        connection.send(body)"` | — |
| [SRC-B106ADC5EF-L000042](../../tests/test_proxy_origin.py#L42) | 42 | `"    response = connection.getresponse()"` | — |
| [SRC-B106ADC5EF-L000043](../../tests/test_proxy_origin.py#L43) | 43 | `"    response.read()"` | — |
| [SRC-B106ADC5EF-L000044](../../tests/test_proxy_origin.py#L44) | 44 | `"    connection.close()"` | — |
| [SRC-B106ADC5EF-L000045](../../tests/test_proxy_origin.py#L45) | 45 | `"    return response.status"` | — |
| [SRC-B106ADC5EF-L000046](../../tests/test_proxy_origin.py#L46) | 46 | `""` | — |
| [SRC-B106ADC5EF-L000047](../../tests/test_proxy_origin.py#L47) | 47 | `"ALLOWED_SHAPES = {"` | — |
| [SRC-B106ADC5EF-L000048](../../tests/test_proxy_origin.py#L48) | 48 | `"    \"proxy keeps Host, forwards https\": {\"Host\": PUBLIC_NAME, \"X-Forwarded-Proto\": \"https\"},"` | — |
| [SRC-B106ADC5EF-L000049](../../tests/test_proxy_origin.py#L49) | 49 | `"    \"proxy keeps Host, sends no proto header\": {\"Host\": PUBLIC_NAME},"` | — |
| [SRC-B106ADC5EF-L000050](../../tests/test_proxy_origin.py#L50) | 50 | `"    \"proxy forwards plain http\": {\"Host\": PUBLIC_NAME, \"X-Forwarded-Proto\": \"http\"},"` | — |
| [SRC-B106ADC5EF-L000051](../../tests/test_proxy_origin.py#L51) | 51 | `"    \"proxy rewrites Host, public name in X-Forwarded-Host\": {"` | — |
| [SRC-B106ADC5EF-L000052](../../tests/test_proxy_origin.py#L52) | 52 | `"        \"Host\": \"127.0.0.1:8000\", \"X-Forwarded-Host\": PUBLIC_NAME, \"X-Forwarded-Proto\": \"http\"},"` | — |
| [SRC-B106ADC5EF-L000053](../../tests/test_proxy_origin.py#L53) | 53 | `"}"` | — |
| [SRC-B106ADC5EF-L000054](../../tests/test_proxy_origin.py#L54) | 54 | `""` | — |
| [SRC-B106ADC5EF-L000055](../../tests/test_proxy_origin.py#L55) | 55 | `"@pytest.mark.parametrize(\"shape\", ALLOWED_SHAPES)"` | — |
| [SRC-B106ADC5EF-L000056](../../tests/test_proxy_origin.py#L56) | 56 | `"def test_own_origin_is_accepted_behind_a_proxy(port, shape):"` | — |
| [SRC-B106ADC5EF-L000057](../../tests/test_proxy_origin.py#L57) | 57 | `"    headers = {**ALLOWED_SHAPES[shape], \"Origin\": \"https://\" + PUBLIC_NAME}"` | — |
| [SRC-B106ADC5EF-L000058](../../tests/test_proxy_origin.py#L58) | 58 | `"    assert call(port, \"POST\", headers) == 200"` | — |
| [SRC-B106ADC5EF-L000059](../../tests/test_proxy_origin.py#L59) | 59 | `"    assert call(port, \"OPTIONS\", {k: v for k, v in headers.items() if k != \"Authorization\"}) == 204"` | — |
| [SRC-B106ADC5EF-L000060](../../tests/test_proxy_origin.py#L60) | 60 | `""` | — |
| [SRC-B106ADC5EF-L000061](../../tests/test_proxy_origin.py#L61) | 61 | `"@pytest.mark.parametrize(\"shape\", ALLOWED_SHAPES)"` | — |
| [SRC-B106ADC5EF-L000062](../../tests/test_proxy_origin.py#L62) | 62 | `"def test_a_foreign_site_is_still_refused(port, shape):"` | — |
| [SRC-B106ADC5EF-L000063](../../tests/test_proxy_origin.py#L63) | 63 | `"    headers = {**ALLOWED_SHAPES[shape], \"Origin\": \"https://evil.example\"}"` | — |
| [SRC-B106ADC5EF-L000064](../../tests/test_proxy_origin.py#L64) | 64 | `"    assert call(port, \"POST\", headers) == 403"` | — |
| [SRC-B106ADC5EF-L000065](../../tests/test_proxy_origin.py#L65) | 65 | `"    assert call(port, \"OPTIONS\", headers) == 403"` | — |
| [SRC-B106ADC5EF-L000066](../../tests/test_proxy_origin.py#L66) | 66 | `""` | — |
| [SRC-B106ADC5EF-L000067](../../tests/test_proxy_origin.py#L67) | 67 | `"def test_configured_origin_still_works_without_any_proxy_headers(port, monkeypatch):"` | — |
| [SRC-B106ADC5EF-L000068](../../tests/test_proxy_origin.py#L68) | 68 | `"    monkeypatch.setenv(\"OMARAI_ALLOWED_ORIGINS\", \"https://frontend.example\")"` | — |
| [SRC-B106ADC5EF-L000069](../../tests/test_proxy_origin.py#L69) | 69 | `"    headers = {\"Host\": \"127.0.0.1:8000\", \"Origin\": \"https://frontend.example\"}"` | — |
| [SRC-B106ADC5EF-L000070](../../tests/test_proxy_origin.py#L70) | 70 | `"    assert call(port, \"POST\", headers) == 200"` | — |
| [SRC-B106ADC5EF-L000071](../../tests/test_proxy_origin.py#L71) | 71 | `""` | — |
| [SRC-B106ADC5EF-L000072](../../tests/test_proxy_origin.py#L72) | 72 | `"def test_spoofed_forwarded_host_cannot_add_an_unapproved_origin(port):"` | — |
| [SRC-B106ADC5EF-L000073](../../tests/test_proxy_origin.py#L73) | 73 | `"    \"\"\"A client-supplied X-Forwarded-Host must not expand the CORS allowlist.\"\"\""` | — |
| [SRC-B106ADC5EF-L000074](../../tests/test_proxy_origin.py#L74) | 74 | `"    headers = {"` | — |
| [SRC-B106ADC5EF-L000075](../../tests/test_proxy_origin.py#L75) | 75 | `"        \"Host\": \"127.0.0.1:8000\","` | — |
| [SRC-B106ADC5EF-L000076](../../tests/test_proxy_origin.py#L76) | 76 | `"        \"X-Forwarded-Host\": \"evil.example\","` | — |
| [SRC-B106ADC5EF-L000077](../../tests/test_proxy_origin.py#L77) | 77 | `"        \"X-Forwarded-Proto\": \"https\","` | — |
| [SRC-B106ADC5EF-L000078](../../tests/test_proxy_origin.py#L78) | 78 | `"        \"Origin\": \"https://evil.example\","` | — |
| [SRC-B106ADC5EF-L000079](../../tests/test_proxy_origin.py#L79) | 79 | `"    }"` | — |
| [SRC-B106ADC5EF-L000080](../../tests/test_proxy_origin.py#L80) | 80 | `"    assert call(port, \"POST\", headers) == 403"` | — |
| [SRC-B106ADC5EF-L000081](../../tests/test_proxy_origin.py#L81) | 81 | `"    assert call("` | — |
| [SRC-B106ADC5EF-L000082](../../tests/test_proxy_origin.py#L82) | 82 | `"        port,"` | — |
| [SRC-B106ADC5EF-L000083](../../tests/test_proxy_origin.py#L83) | 83 | `"        \"OPTIONS\","` | — |
| [SRC-B106ADC5EF-L000084](../../tests/test_proxy_origin.py#L84) | 84 | `"        {key: value for key, value in headers.items() if key != \"Authorization\"},"` | — |
| [SRC-B106ADC5EF-L000085](../../tests/test_proxy_origin.py#L85) | 85 | `"    ) == 403"` | — |
| [SRC-B106ADC5EF-L000086](../../tests/test_proxy_origin.py#L86) | 86 | `""` | — |
## اختبارات

### FILE-3D0DE98F65 — [tests/test_question_requirement_loop.py](../../tests/test_question_requirement_loop.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-3D0DE98F65-L000001](../../tests/test_question_requirement_loop.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-3D0DE98F65-L000002](../../tests/test_question_requirement_loop.py#L2) | 2 | `""` | — |
| [SRC-3D0DE98F65-L000003](../../tests/test_question_requirement_loop.py#L3) | 3 | `"import json"` | — |
| [SRC-3D0DE98F65-L000004](../../tests/test_question_requirement_loop.py#L4) | 4 | `""` | — |
| [SRC-3D0DE98F65-L000005](../../tests/test_question_requirement_loop.py#L5) | 5 | `"from agents.answer_validation import audit_answer_integrity, build_requirement_evidence_ledger"` | — |
| [SRC-3D0DE98F65-L000006](../../tests/test_question_requirement_loop.py#L6) | 6 | `"from agents.research import ("` | — |
| [SRC-3D0DE98F65-L000007](../../tests/test_question_requirement_loop.py#L7) | 7 | `"    MAX_PLAN_QUERIES,"` | — |
| [SRC-3D0DE98F65-L000008](../../tests/test_question_requirement_loop.py#L8) | 8 | `"    extract_question_coverage_targets,"` | — |
| [SRC-3D0DE98F65-L000009](../../tests/test_question_requirement_loop.py#L9) | 9 | `"    fallback_plan,"` | — |
| [SRC-3D0DE98F65-L000010](../../tests/test_question_requirement_loop.py#L10) | 10 | `"    validate_plan,"` | — |
| [SRC-3D0DE98F65-L000011](../../tests/test_question_requirement_loop.py#L11) | 11 | `")"` | — |
| [SRC-3D0DE98F65-L000012](../../tests/test_question_requirement_loop.py#L12) | 12 | `"from agents.web_agent import WebAgent"` | — |
| [SRC-3D0DE98F65-L000013](../../tests/test_question_requirement_loop.py#L13) | 13 | `""` | — |
| [SRC-3D0DE98F65-L000014](../../tests/test_question_requirement_loop.py#L14) | 14 | `""` | — |
| [SRC-3D0DE98F65-L000015](../../tests/test_question_requirement_loop.py#L15) | 15 | `"QUESTION = \"قارن بين iPhone 17 وSamsung S26 من حيث السعر والبطارية والكاميرا\""` | — |
| [SRC-3D0DE98F65-L000016](../../tests/test_question_requirement_loop.py#L16) | 16 | `""` | — |
| [SRC-3D0DE98F65-L000017](../../tests/test_question_requirement_loop.py#L17) | 17 | `""` | — |
| [SRC-3D0DE98F65-L000018](../../tests/test_question_requirement_loop.py#L18) | 18 | `"def test_compound_question_extracts_each_explicit_criterion() -> None:"` | — |
| [SRC-3D0DE98F65-L000019](../../tests/test_question_requirement_loop.py#L19) | 19 | `"    assert extract_question_coverage_targets(QUESTION) == [\"السعر\", \"البطارية\", \"الكاميرا\"]"` | — |
| [SRC-3D0DE98F65-L000020](../../tests/test_question_requirement_loop.py#L20) | 20 | `""` | — |
| [SRC-3D0DE98F65-L000021](../../tests/test_question_requirement_loop.py#L21) | 21 | `""` | — |
| [SRC-3D0DE98F65-L000022](../../tests/test_question_requirement_loop.py#L22) | 22 | `"def test_fallback_plan_assigns_a_bounded_query_to_every_criterion() -> None:"` | — |
| [SRC-3D0DE98F65-L000023](../../tests/test_question_requirement_loop.py#L23) | 23 | `"    plan = fallback_plan(QUESTION)"` | — |
| [SRC-3D0DE98F65-L000024](../../tests/test_question_requirement_loop.py#L24) | 24 | `"    requirement_queries = plan[\"requirement_queries\"]"` | — |
| [SRC-3D0DE98F65-L000025](../../tests/test_question_requirement_loop.py#L25) | 25 | `"    assert [item[\"target\"] for item in requirement_queries] == [\"السعر\", \"البطارية\", \"الكاميرا\"]"` | — |
| [SRC-3D0DE98F65-L000026](../../tests/test_question_requirement_loop.py#L26) | 26 | `"    assert all(item[\"query\"] in plan[\"queries\"] for item in requirement_queries)"` | — |
| [SRC-3D0DE98F65-L000027](../../tests/test_question_requirement_loop.py#L27) | 27 | `"    assert len(plan[\"queries\"]) <= MAX_PLAN_QUERIES"` | — |
| [SRC-3D0DE98F65-L000028](../../tests/test_question_requirement_loop.py#L28) | 28 | `"    assert all(item[\"target\"] in item[\"query\"] for item in requirement_queries)"` | — |
| [SRC-3D0DE98F65-L000029](../../tests/test_question_requirement_loop.py#L29) | 29 | `""` | — |
| [SRC-3D0DE98F65-L000030](../../tests/test_question_requirement_loop.py#L30) | 30 | `""` | — |
| [SRC-3D0DE98F65-L000031](../../tests/test_question_requirement_loop.py#L31) | 31 | `"def test_validated_model_plan_cannot_drop_mandatory_criterion_queries() -> None:"` | — |
| [SRC-3D0DE98F65-L000032](../../tests/test_question_requirement_loop.py#L32) | 32 | `"    fallback = fallback_plan(QUESTION)"` | — |
| [SRC-3D0DE98F65-L000033](../../tests/test_question_requirement_loop.py#L33) | 33 | `"    candidate = {"` | — |
| [SRC-3D0DE98F65-L000034](../../tests/test_question_requirement_loop.py#L34) | 34 | `"        \"queries\": [\"iPhone 17 Samsung S26 reviews\"],"` | — |
| [SRC-3D0DE98F65-L000035](../../tests/test_question_requirement_loop.py#L35) | 35 | `"        \"social_focus\": False,"` | — |
| [SRC-3D0DE98F65-L000036](../../tests/test_question_requirement_loop.py#L36) | 36 | `"        \"freshness\": \"any\","` | — |
| [SRC-3D0DE98F65-L000037](../../tests/test_question_requirement_loop.py#L37) | 37 | `"        \"depth\": \"deep\","` | — |
| [SRC-3D0DE98F65-L000038](../../tests/test_question_requirement_loop.py#L38) | 38 | `"        \"platforms\": [],"` | — |
| [SRC-3D0DE98F65-L000039](../../tests/test_question_requirement_loop.py#L39) | 39 | `"    }"` | — |
| [SRC-3D0DE98F65-L000040](../../tests/test_question_requirement_loop.py#L40) | 40 | `""` | — |
| [SRC-3D0DE98F65-L000041](../../tests/test_question_requirement_loop.py#L41) | 41 | `"    validated = validate_plan(candidate, QUESTION)"` | — |
| [SRC-3D0DE98F65-L000042](../../tests/test_question_requirement_loop.py#L42) | 42 | `""` | — |
| [SRC-3D0DE98F65-L000043](../../tests/test_question_requirement_loop.py#L43) | 43 | `"    assert validated[\"coverage_targets\"] == fallback[\"coverage_targets\"]"` | — |
| [SRC-3D0DE98F65-L000044](../../tests/test_question_requirement_loop.py#L44) | 44 | `"    assert validated[\"requirement_queries\"] == fallback[\"requirement_queries\"]"` | — |
| [SRC-3D0DE98F65-L000045](../../tests/test_question_requirement_loop.py#L45) | 45 | `"    assert all(item[\"query\"] in validated[\"queries\"] for item in fallback[\"requirement_queries\"])"` | — |
| [SRC-3D0DE98F65-L000046](../../tests/test_question_requirement_loop.py#L46) | 46 | `"    assert len(validated[\"queries\"]) <= MAX_PLAN_QUERIES"` | — |
| [SRC-3D0DE98F65-L000047](../../tests/test_question_requirement_loop.py#L47) | 47 | `""` | — |
| [SRC-3D0DE98F65-L000048](../../tests/test_question_requirement_loop.py#L48) | 48 | `""` | — |
| [SRC-3D0DE98F65-L000049](../../tests/test_question_requirement_loop.py#L49) | 49 | `"def test_model_planner_cannot_replace_every_criterion_with_one_generic_query(monkeypatch) -> None:"` | — |
| [SRC-3D0DE98F65-L000050](../../tests/test_question_requirement_loop.py#L50) | 50 | `"    agent = WebAgent()"` | — |
| [SRC-3D0DE98F65-L000051](../../tests/test_question_requirement_loop.py#L51) | 51 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-3D0DE98F65-L000052](../../tests/test_question_requirement_loop.py#L52) | 52 | `"    monkeypatch.setattr("` | — |
| [SRC-3D0DE98F65-L000053](../../tests/test_question_requirement_loop.py#L53) | 53 | `"        agent,"` | — |
| [SRC-3D0DE98F65-L000054](../../tests/test_question_requirement_loop.py#L54) | 54 | `"        \"_request_completion\","` | — |
| [SRC-3D0DE98F65-L000055](../../tests/test_question_requirement_loop.py#L55) | 55 | `"        lambda *args, **kwargs: json.dumps("` | — |
| [SRC-3D0DE98F65-L000056](../../tests/test_question_requirement_loop.py#L56) | 56 | `"            {"` | — |
| [SRC-3D0DE98F65-L000057](../../tests/test_question_requirement_loop.py#L57) | 57 | `"                \"queries\": [\"iPhone Samsung review\"],"` | — |
| [SRC-3D0DE98F65-L000058](../../tests/test_question_requirement_loop.py#L58) | 58 | `"                \"social_focus\": False,"` | — |
| [SRC-3D0DE98F65-L000059](../../tests/test_question_requirement_loop.py#L59) | 59 | `"                \"freshness\": \"any\","` | — |
| [SRC-3D0DE98F65-L000060](../../tests/test_question_requirement_loop.py#L60) | 60 | `"                \"depth\": \"deep\","` | — |
| [SRC-3D0DE98F65-L000061](../../tests/test_question_requirement_loop.py#L61) | 61 | `"                \"platforms\": [],"` | — |
| [SRC-3D0DE98F65-L000062](../../tests/test_question_requirement_loop.py#L62) | 62 | `"            }"` | — |
| [SRC-3D0DE98F65-L000063](../../tests/test_question_requirement_loop.py#L63) | 63 | `"        ),"` | — |
| [SRC-3D0DE98F65-L000064](../../tests/test_question_requirement_loop.py#L64) | 64 | `"    )"` | — |
| [SRC-3D0DE98F65-L000065](../../tests/test_question_requirement_loop.py#L65) | 65 | `""` | — |
| [SRC-3D0DE98F65-L000066](../../tests/test_question_requirement_loop.py#L66) | 66 | `"    plan = agent._plan_search(QUESTION, [])"` | — |
| [SRC-3D0DE98F65-L000067](../../tests/test_question_requirement_loop.py#L67) | 67 | `""` | — |
| [SRC-3D0DE98F65-L000068](../../tests/test_question_requirement_loop.py#L68) | 68 | `"    assert plan[\"coverage_targets\"] == [\"السعر\", \"البطارية\", \"الكاميرا\"]"` | — |
| [SRC-3D0DE98F65-L000069](../../tests/test_question_requirement_loop.py#L69) | 69 | `"    assert all(item[\"query\"] in plan[\"queries\"] for item in plan[\"requirement_queries\"])"` | — |
| [SRC-3D0DE98F65-L000070](../../tests/test_question_requirement_loop.py#L70) | 70 | `"    assert len(plan[\"queries\"]) <= MAX_PLAN_QUERIES"` | — |
| [SRC-3D0DE98F65-L000071](../../tests/test_question_requirement_loop.py#L71) | 71 | `""` | — |
| [SRC-3D0DE98F65-L000072](../../tests/test_question_requirement_loop.py#L72) | 72 | `""` | — |
| [SRC-3D0DE98F65-L000073](../../tests/test_question_requirement_loop.py#L73) | 73 | `"def test_requirement_evidence_ledger_distinguishes_candidate_from_query_only_result() -> None:"` | — |
| [SRC-3D0DE98F65-L000074](../../tests/test_question_requirement_loop.py#L74) | 74 | `"    plan = fallback_plan(QUESTION)"` | — |
| [SRC-3D0DE98F65-L000075](../../tests/test_question_requirement_loop.py#L75) | 75 | `"    queries = plan[\"requirement_queries\"]"` | — |
| [SRC-3D0DE98F65-L000076](../../tests/test_question_requirement_loop.py#L76) | 76 | `"    price_query = next(item[\"query\"] for item in queries if item[\"target\"] == \"السعر\")"` | — |
| [SRC-3D0DE98F65-L000077](../../tests/test_question_requirement_loop.py#L77) | 77 | `"    battery_query = next(item[\"query\"] for item in queries if item[\"target\"] == \"البطارية\")"` | — |
| [SRC-3D0DE98F65-L000078](../../tests/test_question_requirement_loop.py#L78) | 78 | `"    sources = ["` | — |
| [SRC-3D0DE98F65-L000079](../../tests/test_question_requirement_loop.py#L79) | 79 | `"        {"` | — |
| [SRC-3D0DE98F65-L000080](../../tests/test_question_requirement_loop.py#L80) | 80 | `"            \"url\": \"https://example.com/price\","` | — |
| [SRC-3D0DE98F65-L000081](../../tests/test_question_requirement_loop.py#L81) | 81 | `"            \"title\": \"Phone pricing\","` | — |
| [SRC-3D0DE98F65-L000082](../../tests/test_question_requirement_loop.py#L82) | 82 | `"            \"snippet\": \"The current price is listed for both phone models.\","` | — |
| [SRC-3D0DE98F65-L000083](../../tests/test_question_requirement_loop.py#L83) | 83 | `"            \"page_text\": \"The current price is 100 EGP.\","` | — |
| [SRC-3D0DE98F65-L000084](../../tests/test_question_requirement_loop.py#L84) | 84 | `"            \"page_fetched\": True,"` | — |
| [SRC-3D0DE98F65-L000085](../../tests/test_question_requirement_loop.py#L85) | 85 | `"            \"queries\": [price_query],"` | — |
| [SRC-3D0DE98F65-L000086](../../tests/test_question_requirement_loop.py#L86) | 86 | `"        },"` | — |
| [SRC-3D0DE98F65-L000087](../../tests/test_question_requirement_loop.py#L87) | 87 | `"        {"` | — |
| [SRC-3D0DE98F65-L000088](../../tests/test_question_requirement_loop.py#L88) | 88 | `"            \"url\": \"https://example.net/specs\","` | — |
| [SRC-3D0DE98F65-L000089](../../tests/test_question_requirement_loop.py#L89) | 89 | `"            \"title\": \"General technical specifications\","` | — |
| [SRC-3D0DE98F65-L000090](../../tests/test_question_requirement_loop.py#L90) | 90 | `"            \"snippet\": \"Technical specifications for the two products are listed here.\","` | — |
| [SRC-3D0DE98F65-L000091](../../tests/test_question_requirement_loop.py#L91) | 91 | `"            \"page_fetched\": False,"` | — |
| [SRC-3D0DE98F65-L000092](../../tests/test_question_requirement_loop.py#L92) | 92 | `"            \"queries\": [battery_query],"` | — |
| [SRC-3D0DE98F65-L000093](../../tests/test_question_requirement_loop.py#L93) | 93 | `"        },"` | — |
| [SRC-3D0DE98F65-L000094](../../tests/test_question_requirement_loop.py#L94) | 94 | `"    ]"` | — |
| [SRC-3D0DE98F65-L000095](../../tests/test_question_requirement_loop.py#L95) | 95 | `""` | — |
| [SRC-3D0DE98F65-L000096](../../tests/test_question_requirement_loop.py#L96) | 96 | `"    ledger = build_requirement_evidence_ledger(plan[\"coverage_targets\"], sources, queries)"` | — |
| [SRC-3D0DE98F65-L000097](../../tests/test_question_requirement_loop.py#L97) | 97 | `"    by_target = {item[\"target\"]: item for item in ledger}"` | — |
| [SRC-3D0DE98F65-L000098](../../tests/test_question_requirement_loop.py#L98) | 98 | `""` | — |
| [SRC-3D0DE98F65-L000099](../../tests/test_question_requirement_loop.py#L99) | 99 | `"    assert by_target[\"السعر\"][\"status\"] == \"candidate_evidence_found_not_verified\""` | — |
| [SRC-3D0DE98F65-L000100](../../tests/test_question_requirement_loop.py#L100) | 100 | `"    assert by_target[\"السعر\"][\"candidate_source_indexes\"] == [1]"` | — |
| [SRC-3D0DE98F65-L000101](../../tests/test_question_requirement_loop.py#L101) | 101 | `"    assert by_target[\"البطارية\"][\"status\"] == \"query_returned_candidates_no_lexical_signal\""` | — |
| [SRC-3D0DE98F65-L000102](../../tests/test_question_requirement_loop.py#L102) | 102 | `"    assert by_target[\"البطارية\"][\"query_result_source_indexes\"] == [2]"` | — |
| [SRC-3D0DE98F65-L000103](../../tests/test_question_requirement_loop.py#L103) | 103 | `"    assert by_target[\"الكاميرا\"][\"status\"] == \"no_candidate_evidence_found\""` | — |
| [SRC-3D0DE98F65-L000104](../../tests/test_question_requirement_loop.py#L104) | 104 | `"    assert all(item[\"semantic_verification\"] is False for item in ledger)"` | — |
| [SRC-3D0DE98F65-L000105](../../tests/test_question_requirement_loop.py#L105) | 105 | `"    assert all(item[\"source_entailment_verified\"] is False for item in ledger)"` | — |
| [SRC-3D0DE98F65-L000106](../../tests/test_question_requirement_loop.py#L106) | 106 | `""` | — |
| [SRC-3D0DE98F65-L000107](../../tests/test_question_requirement_loop.py#L107) | 107 | `""` | — |
| [SRC-3D0DE98F65-L000108](../../tests/test_question_requirement_loop.py#L108) | 108 | `""` | — |
| [SRC-3D0DE98F65-L000109](../../tests/test_question_requirement_loop.py#L109) | 109 | `"def test_research_keeps_a_relevant_source_for_each_criterion_before_page_fetch(monkeypatch) -> None:"` | — |
| [SRC-3D0DE98F65-L000110](../../tests/test_question_requirement_loop.py#L110) | 110 | `"    agent = WebAgent()"` | — |
| [SRC-3D0DE98F65-L000111](../../tests/test_question_requirement_loop.py#L111) | 111 | `"    targets = [\"price\", \"battery\", \"camera\", \"warranty\"]"` | — |
| [SRC-3D0DE98F65-L000112](../../tests/test_question_requirement_loop.py#L112) | 112 | `"    requirement_queries = ["` | — |
| [SRC-3D0DE98F65-L000113](../../tests/test_question_requirement_loop.py#L113) | 113 | `"        {\"target\": target, \"query\": f\"sample product {target}\"}"` | — |
| [SRC-3D0DE98F65-L000114](../../tests/test_question_requirement_loop.py#L114) | 114 | `"        for target in targets"` | — |
| [SRC-3D0DE98F65-L000115](../../tests/test_question_requirement_loop.py#L115) | 115 | `"    ]"` | — |
| [SRC-3D0DE98F65-L000116](../../tests/test_question_requirement_loop.py#L116) | 116 | `"    plan = {"` | — |
| [SRC-3D0DE98F65-L000117](../../tests/test_question_requirement_loop.py#L117) | 117 | `"        \"queries\": [item[\"query\"] for item in requirement_queries],"` | — |
| [SRC-3D0DE98F65-L000118](../../tests/test_question_requirement_loop.py#L118) | 118 | `"        \"coverage_targets\": targets,"` | — |
| [SRC-3D0DE98F65-L000119](../../tests/test_question_requirement_loop.py#L119) | 119 | `"        \"requirement_queries\": requirement_queries,"` | — |
| [SRC-3D0DE98F65-L000120](../../tests/test_question_requirement_loop.py#L120) | 120 | `"        \"direct_urls\": [],"` | — |
| [SRC-3D0DE98F65-L000121](../../tests/test_question_requirement_loop.py#L121) | 121 | `"        \"social_focus\": False,"` | — |
| [SRC-3D0DE98F65-L000122](../../tests/test_question_requirement_loop.py#L122) | 122 | `"        \"freshness\": \"any\","` | — |
| [SRC-3D0DE98F65-L000123](../../tests/test_question_requirement_loop.py#L123) | 123 | `"        \"depth\": \"standard\","` | — |
| [SRC-3D0DE98F65-L000124](../../tests/test_question_requirement_loop.py#L124) | 124 | `"        \"platforms\": [],"` | — |
| [SRC-3D0DE98F65-L000125](../../tests/test_question_requirement_loop.py#L125) | 125 | `"        \"planning_method\": \"test\","` | — |
| [SRC-3D0DE98F65-L000126](../../tests/test_question_requirement_loop.py#L126) | 126 | `"    }"` | — |
| [SRC-3D0DE98F65-L000127](../../tests/test_question_requirement_loop.py#L127) | 127 | `"    query_index = {"` | — |
| [SRC-3D0DE98F65-L000128](../../tests/test_question_requirement_loop.py#L128) | 128 | `"        item[\"query\"].casefold(): index"` | — |
| [SRC-3D0DE98F65-L000129](../../tests/test_question_requirement_loop.py#L129) | 129 | `"        for index, item in enumerate(requirement_queries)"` | — |
| [SRC-3D0DE98F65-L000130](../../tests/test_question_requirement_loop.py#L130) | 130 | `"    }"` | — |
| [SRC-3D0DE98F65-L000131](../../tests/test_question_requirement_loop.py#L131) | 131 | `""` | — |
| [SRC-3D0DE98F65-L000132](../../tests/test_question_requirement_loop.py#L132) | 132 | `"    def fake_search(query: str):"` | — |
| [SRC-3D0DE98F65-L000133](../../tests/test_question_requirement_loop.py#L133) | 133 | `"        index = query_index[query.casefold()]"` | — |
| [SRC-3D0DE98F65-L000134](../../tests/test_question_requirement_loop.py#L134) | 134 | `"        rows = []"` | — |
| [SRC-3D0DE98F65-L000135](../../tests/test_question_requirement_loop.py#L135) | 135 | `"        for rank in range(1, 7):"` | — |
| [SRC-3D0DE98F65-L000136](../../tests/test_question_requirement_loop.py#L136) | 136 | `"            title = ("` | — |
| [SRC-3D0DE98F65-L000137](../../tests/test_question_requirement_loop.py#L137) | 137 | `"                f\"{targets[index]} detailed evidence\""` | — |
| [SRC-3D0DE98F65-L000138](../../tests/test_question_requirement_loop.py#L138) | 138 | `"                if rank == 6"` | — |
| [SRC-3D0DE98F65-L000139](../../tests/test_question_requirement_loop.py#L139) | 139 | `"                else f\"Generic product listing {index}-{rank}\""` | — |
| [SRC-3D0DE98F65-L000140](../../tests/test_question_requirement_loop.py#L140) | 140 | `"            )"` | — |
| [SRC-3D0DE98F65-L000141](../../tests/test_question_requirement_loop.py#L141) | 141 | `"            rows.append({"` | — |
| [SRC-3D0DE98F65-L000142](../../tests/test_question_requirement_loop.py#L142) | 142 | `"                \"title\": title,"` | — |
| [SRC-3D0DE98F65-L000143](../../tests/test_question_requirement_loop.py#L143) | 143 | `"                \"url\": f\"https://s{index}-r{rank}.example.com/item\","` | — |
| [SRC-3D0DE98F65-L000144](../../tests/test_question_requirement_loop.py#L144) | 144 | `"                \"snippet\": title if rank == 6 else \"General product listing with no criterion detail.\","` | — |
| [SRC-3D0DE98F65-L000145](../../tests/test_question_requirement_loop.py#L145) | 145 | `"                \"provider\": \"test_search\","` | — |
| [SRC-3D0DE98F65-L000146](../../tests/test_question_requirement_loop.py#L146) | 146 | `"                \"provider_rank\": rank,"` | — |
| [SRC-3D0DE98F65-L000147](../../tests/test_question_requirement_loop.py#L147) | 147 | `"                \"domain\": f\"s{index}-r{rank}.example.com\","` | — |
| [SRC-3D0DE98F65-L000148](../../tests/test_question_requirement_loop.py#L148) | 148 | `"            })"` | — |
| [SRC-3D0DE98F65-L000149](../../tests/test_question_requirement_loop.py#L149) | 149 | `"        return rows"` | — |
| [SRC-3D0DE98F65-L000150](../../tests/test_question_requirement_loop.py#L150) | 150 | `""` | — |
| [SRC-3D0DE98F65-L000151](../../tests/test_question_requirement_loop.py#L151) | 151 | `"    def fake_fetch(url: str):"` | — |
| [SRC-3D0DE98F65-L000152](../../tests/test_question_requirement_loop.py#L152) | 152 | `"        hostname = url.split(\"://\", 1)[1].split(\"/\", 1)[0]"` | — |
| [SRC-3D0DE98F65-L000153](../../tests/test_question_requirement_loop.py#L153) | 153 | `"        index = int(hostname.split(\"-r\", 1)[0][1:])"` | — |
| [SRC-3D0DE98F65-L000154](../../tests/test_question_requirement_loop.py#L154) | 154 | `"        target = targets[index]"` | — |
| [SRC-3D0DE98F65-L000155](../../tests/test_question_requirement_loop.py#L155) | 155 | `"        return f\"{target} page\", f\"{target} evidence and detailed specifications.\""` | — |
| [SRC-3D0DE98F65-L000156](../../tests/test_question_requirement_loop.py#L156) | 156 | `""` | — |
| [SRC-3D0DE98F65-L000157](../../tests/test_question_requirement_loop.py#L157) | 157 | `"    monkeypatch.setattr(agent, \"_search_web\", fake_search)"` | — |
| [SRC-3D0DE98F65-L000158](../../tests/test_question_requirement_loop.py#L158) | 158 | `"    monkeypatch.setattr(agent, \"_fetch_page\", fake_fetch)"` | — |
| [SRC-3D0DE98F65-L000159](../../tests/test_question_requirement_loop.py#L159) | 159 | `""` | — |
| [SRC-3D0DE98F65-L000160](../../tests/test_question_requirement_loop.py#L160) | 160 | `"    sources, _warnings, report = agent._collect_research(plan)"` | — |
| [SRC-3D0DE98F65-L000161](../../tests/test_question_requirement_loop.py#L161) | 161 | `""` | — |
| [SRC-3D0DE98F65-L000162](../../tests/test_question_requirement_loop.py#L162) | 162 | `"    assert len(sources) <= 18"` | — |
| [SRC-3D0DE98F65-L000163](../../tests/test_question_requirement_loop.py#L163) | 163 | `"    for item in requirement_queries:"` | — |
| [SRC-3D0DE98F65-L000164](../../tests/test_question_requirement_loop.py#L164) | 164 | `"        matched = ["` | — |
| [SRC-3D0DE98F65-L000165](../../tests/test_question_requirement_loop.py#L165) | 165 | `"            source for source in sources"` | — |
| [SRC-3D0DE98F65-L000166](../../tests/test_question_requirement_loop.py#L166) | 166 | `"            if item[\"query\"] in source.get(\"queries\", [])"` | — |
| [SRC-3D0DE98F65-L000167](../../tests/test_question_requirement_loop.py#L167) | 167 | `"        ]"` | — |
| [SRC-3D0DE98F65-L000168](../../tests/test_question_requirement_loop.py#L168) | 168 | `"        assert matched, f\"criterion query lost from final source pool: {item['target']}\""` | — |
| [SRC-3D0DE98F65-L000169](../../tests/test_question_requirement_loop.py#L169) | 169 | `"        assert any(item[\"target\"] in source[\"title\"] for source in matched[:2])"` | — |
| [SRC-3D0DE98F65-L000170](../../tests/test_question_requirement_loop.py#L170) | 170 | `"    assert report[\"queries_planned\"] == 4"` | — |
| [SRC-3D0DE98F65-L000171](../../tests/test_question_requirement_loop.py#L171) | 171 | `"    assert report[\"queries_attempted\"] == 4"` | — |
| [SRC-3D0DE98F65-L000172](../../tests/test_question_requirement_loop.py#L172) | 172 | `""` | — |
| [SRC-3D0DE98F65-L000173](../../tests/test_question_requirement_loop.py#L173) | 173 | `""` | — |
| [SRC-3D0DE98F65-L000174](../../tests/test_question_requirement_loop.py#L174) | 174 | `"def test_answer_integrity_exposes_requirement_evidence_separately_from_word_overlap() -> None:"` | — |
| [SRC-3D0DE98F65-L000175](../../tests/test_question_requirement_loop.py#L175) | 175 | `"    plan = fallback_plan(QUESTION)"` | — |
| [SRC-3D0DE98F65-L000176](../../tests/test_question_requirement_loop.py#L176) | 176 | `"    price_query = next(item[\"query\"] for item in plan[\"requirement_queries\"] if item[\"target\"] == \"السعر\")"` | — |
| [SRC-3D0DE98F65-L000177](../../tests/test_question_requirement_loop.py#L177) | 177 | `"    sources = ["` | — |
| [SRC-3D0DE98F65-L000178](../../tests/test_question_requirement_loop.py#L178) | 178 | `"        {"` | — |
| [SRC-3D0DE98F65-L000179](../../tests/test_question_requirement_loop.py#L179) | 179 | `"            \"url\": \"https://example.com/price\","` | — |
| [SRC-3D0DE98F65-L000180](../../tests/test_question_requirement_loop.py#L180) | 180 | `"            \"title\": \"Phone pricing\","` | — |
| [SRC-3D0DE98F65-L000181](../../tests/test_question_requirement_loop.py#L181) | 181 | `"            \"snippet\": \"The price is 100 EGP.\","` | — |
| [SRC-3D0DE98F65-L000182](../../tests/test_question_requirement_loop.py#L182) | 182 | `"            \"page_fetched\": False,"` | — |
| [SRC-3D0DE98F65-L000183](../../tests/test_question_requirement_loop.py#L183) | 183 | `"            \"queries\": [price_query],"` | — |
