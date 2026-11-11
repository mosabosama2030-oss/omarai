# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **058**
- سجلات الأسطر: **800**
- النطاق: SRC-2822F30DAD-L000217 إلى SRC-AC9D8384E8-L000066
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-2822F30DAD — [tests/test_sales_domain.py](../../tests/test_sales_domain.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-2822F30DAD-L000217](../../tests/test_sales_domain.py#L217) | 217 | `"def test_demand_evidence_keeps_publication_event_and_observation_dates_separate():"` | — |
| [SRC-2822F30DAD-L000218](../../tests/test_sales_domain.py#L218) | 218 | `"    evidence = page_evidence("` | — |
| [SRC-2822F30DAD-L000219](../../tests/test_sales_domain.py#L219) | 219 | `"        publication_date=\"2026-10-20\","` | — |
| [SRC-2822F30DAD-L000220](../../tests/test_sales_domain.py#L220) | 220 | `"        event_date=\"2026-10-18\","` | — |
| [SRC-2822F30DAD-L000221](../../tests/test_sales_domain.py#L221) | 221 | `"        observed_at=\"2026-10-31T08:00:00+02:00\","` | — |
| [SRC-2822F30DAD-L000222](../../tests/test_sales_domain.py#L222) | 222 | `"    )"` | — |
| [SRC-2822F30DAD-L000223](../../tests/test_sales_domain.py#L223) | 223 | `""` | — |
| [SRC-2822F30DAD-L000224](../../tests/test_sales_domain.py#L224) | 224 | `"    assert evidence.publication_date == \"2026-10-20\""` | — |
| [SRC-2822F30DAD-L000225](../../tests/test_sales_domain.py#L225) | 225 | `"    assert evidence.event_date == \"2026-10-18\""` | — |
| [SRC-2822F30DAD-L000226](../../tests/test_sales_domain.py#L226) | 226 | `"    assert evidence.observed_at == \"2026-10-31T08:00:00+02:00\""` | — |
| [SRC-2822F30DAD-L000227](../../tests/test_sales_domain.py#L227) | 227 | `""` | — |
| [SRC-2822F30DAD-L000228](../../tests/test_sales_domain.py#L228) | 228 | `""` | — |
| [SRC-2822F30DAD-L000229](../../tests/test_sales_domain.py#L229) | 229 | `"@pytest.mark.parametrize(\"field\", [\"publication_date\", \"event_date\"])"` | — |
| [SRC-2822F30DAD-L000230](../../tests/test_sales_domain.py#L230) | 230 | `"def test_demand_evidence_rejects_invalid_dates(field):"` | — |
| [SRC-2822F30DAD-L000231](../../tests/test_sales_domain.py#L231) | 231 | `"    with pytest.raises(ValueError, match=\"ISO date\"):"` | — |
| [SRC-2822F30DAD-L000232](../../tests/test_sales_domain.py#L232) | 232 | `"        page_evidence(**{field: \"yesterday\"})"` | — |
| [SRC-2822F30DAD-L000233](../../tests/test_sales_domain.py#L233) | 233 | `""` | — |
| [SRC-2822F30DAD-L000234](../../tests/test_sales_domain.py#L234) | 234 | `""` | — |
| [SRC-2822F30DAD-L000235](../../tests/test_sales_domain.py#L235) | 235 | `"def test_demand_evidence_does_not_invent_missing_dates():"` | — |
| [SRC-2822F30DAD-L000236](../../tests/test_sales_domain.py#L236) | 236 | `"    evidence = page_evidence("` | — |
| [SRC-2822F30DAD-L000237](../../tests/test_sales_domain.py#L237) | 237 | `"        publication_date=None,"` | — |
| [SRC-2822F30DAD-L000238](../../tests/test_sales_domain.py#L238) | 238 | `"        event_date=None,"` | — |
| [SRC-2822F30DAD-L000239](../../tests/test_sales_domain.py#L239) | 239 | `"        observed_at=None,"` | — |
| [SRC-2822F30DAD-L000240](../../tests/test_sales_domain.py#L240) | 240 | `"    )"` | — |
| [SRC-2822F30DAD-L000241](../../tests/test_sales_domain.py#L241) | 241 | `""` | — |
| [SRC-2822F30DAD-L000242](../../tests/test_sales_domain.py#L242) | 242 | `"    assert evidence.publication_date is None"` | — |
| [SRC-2822F30DAD-L000243](../../tests/test_sales_domain.py#L243) | 243 | `"    assert evidence.event_date is None"` | — |
| [SRC-2822F30DAD-L000244](../../tests/test_sales_domain.py#L244) | 244 | `"    assert evidence.observed_at is None"` | — |
| [SRC-2822F30DAD-L000245](../../tests/test_sales_domain.py#L245) | 245 | `""` | — |
| [SRC-2822F30DAD-L000246](../../tests/test_sales_domain.py#L246) | 246 | `""` | — |
| [SRC-2822F30DAD-L000247](../../tests/test_sales_domain.py#L247) | 247 | `"def test_observation_timestamp_requires_timezone():"` | — |
| [SRC-2822F30DAD-L000248](../../tests/test_sales_domain.py#L248) | 248 | `"    with pytest.raises(ValueError, match=\"timezone offset\"):"` | — |
| [SRC-2822F30DAD-L000249](../../tests/test_sales_domain.py#L249) | 249 | `"        page_evidence(observed_at=\"2026-10-31T08:00:00\")"` | — |
| [SRC-2822F30DAD-L000250](../../tests/test_sales_domain.py#L250) | 250 | `""` | — |
| [SRC-2822F30DAD-L000251](../../tests/test_sales_domain.py#L251) | 251 | `""` | — |
| [SRC-2822F30DAD-L000252](../../tests/test_sales_domain.py#L252) | 252 | `"def test_search_snippet_cannot_be_labelled_as_a_read_page():"` | — |
| [SRC-2822F30DAD-L000253](../../tests/test_sales_domain.py#L253) | 253 | `"    with pytest.raises(ValueError, match=\"cannot be marked\"):"` | — |
| [SRC-2822F30DAD-L000254](../../tests/test_sales_domain.py#L254) | 254 | `"        page_evidence("` | — |
| [SRC-2822F30DAD-L000255](../../tests/test_sales_domain.py#L255) | 255 | `"            content_basis=EvidenceBasis.SEARCH_SNIPPET,"` | — |
| [SRC-2822F30DAD-L000256](../../tests/test_sales_domain.py#L256) | 256 | `"            page_read=True,"` | — |
| [SRC-2822F30DAD-L000257](../../tests/test_sales_domain.py#L257) | 257 | `"        )"` | — |
| [SRC-2822F30DAD-L000258](../../tests/test_sales_domain.py#L258) | 258 | `""` | — |
| [SRC-2822F30DAD-L000259](../../tests/test_sales_domain.py#L259) | 259 | `""` | — |
| [SRC-2822F30DAD-L000260](../../tests/test_sales_domain.py#L260) | 260 | `"def test_page_text_requires_successful_page_read():"` | — |
| [SRC-2822F30DAD-L000261](../../tests/test_sales_domain.py#L261) | 261 | `"    with pytest.raises(ValueError, match=\"requires page_read\"):"` | — |
| [SRC-2822F30DAD-L000262](../../tests/test_sales_domain.py#L262) | 262 | `"        page_evidence("` | — |
| [SRC-2822F30DAD-L000263](../../tests/test_sales_domain.py#L263) | 263 | `"            content_basis=EvidenceBasis.PAGE_TEXT,"` | — |
| [SRC-2822F30DAD-L000264](../../tests/test_sales_domain.py#L264) | 264 | `"            page_read=False,"` | — |
| [SRC-2822F30DAD-L000265](../../tests/test_sales_domain.py#L265) | 265 | `"        )"` | — |
| [SRC-2822F30DAD-L000266](../../tests/test_sales_domain.py#L266) | 266 | `""` | — |
| [SRC-2822F30DAD-L000267](../../tests/test_sales_domain.py#L267) | 267 | `""` | — |
| [SRC-2822F30DAD-L000268](../../tests/test_sales_domain.py#L268) | 268 | `"def test_title_and_snippet_evidence_can_remain_unread():"` | — |
| [SRC-2822F30DAD-L000269](../../tests/test_sales_domain.py#L269) | 269 | `"    title = page_evidence("` | — |
| [SRC-2822F30DAD-L000270](../../tests/test_sales_domain.py#L270) | 270 | `"        content_basis=EvidenceBasis.TITLE,"` | — |
| [SRC-2822F30DAD-L000271](../../tests/test_sales_domain.py#L271) | 271 | `"        page_read=False,"` | — |
| [SRC-2822F30DAD-L000272](../../tests/test_sales_domain.py#L272) | 272 | `"    )"` | — |
| [SRC-2822F30DAD-L000273](../../tests/test_sales_domain.py#L273) | 273 | `"    snippet = page_evidence("` | — |
| [SRC-2822F30DAD-L000274](../../tests/test_sales_domain.py#L274) | 274 | `"        content_basis=EvidenceBasis.SEARCH_SNIPPET,"` | — |
| [SRC-2822F30DAD-L000275](../../tests/test_sales_domain.py#L275) | 275 | `"        page_read=False,"` | — |
| [SRC-2822F30DAD-L000276](../../tests/test_sales_domain.py#L276) | 276 | `"    )"` | — |
| [SRC-2822F30DAD-L000277](../../tests/test_sales_domain.py#L277) | 277 | `""` | — |
| [SRC-2822F30DAD-L000278](../../tests/test_sales_domain.py#L278) | 278 | `"    assert title.page_read is False"` | — |
| [SRC-2822F30DAD-L000279](../../tests/test_sales_domain.py#L279) | 279 | `"    assert snippet.page_read is False"` | — |
| [SRC-2822F30DAD-L000280](../../tests/test_sales_domain.py#L280) | 280 | `""` | — |
| [SRC-2822F30DAD-L000281](../../tests/test_sales_domain.py#L281) | 281 | `""` | — |
| [SRC-2822F30DAD-L000282](../../tests/test_sales_domain.py#L282) | 282 | `"def test_demand_type_and_product_fit_are_independent():"` | — |
| [SRC-2822F30DAD-L000283](../../tests/test_sales_domain.py#L283) | 283 | `"    signal = DemandSignal("` | — |
| [SRC-2822F30DAD-L000284](../../tests/test_sales_domain.py#L284) | 284 | `"        signal_id=\"signal-direct\","` | — |
| [SRC-2822F30DAD-L000285](../../tests/test_sales_domain.py#L285) | 285 | `"        signal_type=DemandSignalType.DIRECT_PURCHASE_REQUEST,"` | — |
| [SRC-2822F30DAD-L000286](../../tests/test_sales_domain.py#L286) | 286 | `"        evidence=page_evidence(),"` | — |
| [SRC-2822F30DAD-L000287](../../tests/test_sales_domain.py#L287) | 287 | `"        product_fit=ProductFit.UNASSESSED,"` | — |
| [SRC-2822F30DAD-L000288](../../tests/test_sales_domain.py#L288) | 288 | `"        classification_reason=\"The source explicitly asks to buy.\","` | — |
| [SRC-2822F30DAD-L000289](../../tests/test_sales_domain.py#L289) | 289 | `"    )"` | — |
| [SRC-2822F30DAD-L000290](../../tests/test_sales_domain.py#L290) | 290 | `""` | — |
| [SRC-2822F30DAD-L000291](../../tests/test_sales_domain.py#L291) | 291 | `"    assert signal.signal_type == DemandSignalType.DIRECT_PURCHASE_REQUEST"` | — |
| [SRC-2822F30DAD-L000292](../../tests/test_sales_domain.py#L292) | 292 | `"    assert signal.product_fit == ProductFit.UNASSESSED"` | — |
| [SRC-2822F30DAD-L000293](../../tests/test_sales_domain.py#L293) | 293 | `"    assert signal.identity_status == IdentityStatus.UNKNOWN"` | — |
| [SRC-2822F30DAD-L000294](../../tests/test_sales_domain.py#L294) | 294 | `""` | — |
| [SRC-2822F30DAD-L000295](../../tests/test_sales_domain.py#L295) | 295 | `""` | — |
| [SRC-2822F30DAD-L000296](../../tests/test_sales_domain.py#L296) | 296 | `"def test_assessed_product_fit_requires_a_rationale():"` | — |
| [SRC-2822F30DAD-L000297](../../tests/test_sales_domain.py#L297) | 297 | `"    with pytest.raises(ValueError, match=\"requires a rationale\"):"` | — |
| [SRC-2822F30DAD-L000298](../../tests/test_sales_domain.py#L298) | 298 | `"        DemandSignal("` | — |
| [SRC-2822F30DAD-L000299](../../tests/test_sales_domain.py#L299) | 299 | `"            signal_id=\"signal-fit\","` | — |
| [SRC-2822F30DAD-L000300](../../tests/test_sales_domain.py#L300) | 300 | `"            signal_type=DemandSignalType.STATED_NEED,"` | — |
| [SRC-2822F30DAD-L000301](../../tests/test_sales_domain.py#L301) | 301 | `"            evidence=page_evidence(),"` | — |
| [SRC-2822F30DAD-L000302](../../tests/test_sales_domain.py#L302) | 302 | `"            product_fit=ProductFit.FIT,"` | — |
| [SRC-2822F30DAD-L000303](../../tests/test_sales_domain.py#L303) | 303 | `"        )"` | — |
| [SRC-2822F30DAD-L000304](../../tests/test_sales_domain.py#L304) | 304 | `""` | — |
| [SRC-2822F30DAD-L000305](../../tests/test_sales_domain.py#L305) | 305 | `"    signal = DemandSignal("` | — |
| [SRC-2822F30DAD-L000306](../../tests/test_sales_domain.py#L306) | 306 | `"        signal_id=\"signal-fit\","` | — |
| [SRC-2822F30DAD-L000307](../../tests/test_sales_domain.py#L307) | 307 | `"        signal_type=DemandSignalType.STATED_NEED,"` | — |
| [SRC-2822F30DAD-L000308](../../tests/test_sales_domain.py#L308) | 308 | `"        evidence=page_evidence(),"` | — |
| [SRC-2822F30DAD-L000309](../../tests/test_sales_domain.py#L309) | 309 | `"        product_fit=ProductFit.FIT,"` | — |
| [SRC-2822F30DAD-L000310](../../tests/test_sales_domain.py#L310) | 310 | `"        product_fit_reason=\"The requested specification matches the product profile.\","` | — |
| [SRC-2822F30DAD-L000311](../../tests/test_sales_domain.py#L311) | 311 | `"    )"` | — |
| [SRC-2822F30DAD-L000312](../../tests/test_sales_domain.py#L312) | 312 | `"    assert signal.product_fit == ProductFit.FIT"` | — |
| [SRC-2822F30DAD-L000313](../../tests/test_sales_domain.py#L313) | 313 | `""` | — |
| [SRC-2822F30DAD-L000314](../../tests/test_sales_domain.py#L314) | 314 | `""` | — |
| [SRC-2822F30DAD-L000315](../../tests/test_sales_domain.py#L315) | 315 | `"def test_unassessed_product_fit_must_not_have_a_rationale():"` | — |
| [SRC-2822F30DAD-L000316](../../tests/test_sales_domain.py#L316) | 316 | `"    with pytest.raises(ValueError, match=\"must not have a fit rationale\"):"` | — |
| [SRC-2822F30DAD-L000317](../../tests/test_sales_domain.py#L317) | 317 | `"        DemandSignal("` | — |
| [SRC-2822F30DAD-L000318](../../tests/test_sales_domain.py#L318) | 318 | `"            signal_id=\"signal-unassessed\","` | — |
| [SRC-2822F30DAD-L000319](../../tests/test_sales_domain.py#L319) | 319 | `"            signal_type=DemandSignalType.INDIRECT_INDICATOR,"` | — |
| [SRC-2822F30DAD-L000320](../../tests/test_sales_domain.py#L320) | 320 | `"            evidence=page_evidence(),"` | — |
| [SRC-2822F30DAD-L000321](../../tests/test_sales_domain.py#L321) | 321 | `"            product_fit_reason=\"No assessment has been made.\","` | — |
| [SRC-2822F30DAD-L000322](../../tests/test_sales_domain.py#L322) | 322 | `"        )"` | — |
| [SRC-2822F30DAD-L000323](../../tests/test_sales_domain.py#L323) | 323 | `""` | — |
| [SRC-2822F30DAD-L000324](../../tests/test_sales_domain.py#L324) | 324 | `""` | — |
| [SRC-2822F30DAD-L000325](../../tests/test_sales_domain.py#L325) | 325 | `"def test_icp_match_only_remains_distinct_from_direct_purchase():"` | — |
| [SRC-2822F30DAD-L000326](../../tests/test_sales_domain.py#L326) | 326 | `"    signal = DemandSignal("` | — |
| [SRC-2822F30DAD-L000327](../../tests/test_sales_domain.py#L327) | 327 | `"        signal_id=\"signal-icp\","` | — |
| [SRC-2822F30DAD-L000328](../../tests/test_sales_domain.py#L328) | 328 | `"        signal_type=DemandSignalType.ICP_MATCH_ONLY,"` | — |
| [SRC-2822F30DAD-L000329](../../tests/test_sales_domain.py#L329) | 329 | `"        evidence=page_evidence("` | — |
| [SRC-2822F30DAD-L000330](../../tests/test_sales_domain.py#L330) | 330 | `"            excerpt=\"A business in the target industry operates in Cairo.\","` | — |
| [SRC-2822F30DAD-L000331](../../tests/test_sales_domain.py#L331) | 331 | `"            content_basis=EvidenceBasis.TITLE,"` | — |
| [SRC-2822F30DAD-L000332](../../tests/test_sales_domain.py#L332) | 332 | `"            page_read=False,"` | — |
| [SRC-2822F30DAD-L000333](../../tests/test_sales_domain.py#L333) | 333 | `"        ),"` | — |
| [SRC-2822F30DAD-L000334](../../tests/test_sales_domain.py#L334) | 334 | `"    )"` | — |
| [SRC-2822F30DAD-L000335](../../tests/test_sales_domain.py#L335) | 335 | `""` | — |
| [SRC-2822F30DAD-L000336](../../tests/test_sales_domain.py#L336) | 336 | `"    assert signal.signal_type == DemandSignalType.ICP_MATCH_ONLY"` | — |
| [SRC-2822F30DAD-L000337](../../tests/test_sales_domain.py#L337) | 337 | `"    assert signal.signal_type != DemandSignalType.DIRECT_PURCHASE_REQUEST"` | — |
| [SRC-2822F30DAD-L000338](../../tests/test_sales_domain.py#L338) | 338 | `""` | — |
| [SRC-2822F30DAD-L000339](../../tests/test_sales_domain.py#L339) | 339 | `""` | — |
| [SRC-2822F30DAD-L000340](../../tests/test_sales_domain.py#L340) | 340 | `"def test_lead_qualification_exposes_independent_dimensions_without_probability():"` | — |
| [SRC-2822F30DAD-L000341](../../tests/test_sales_domain.py#L341) | 341 | `"    assessment = LeadQualification("` | — |
| [SRC-2822F30DAD-L000342](../../tests/test_sales_domain.py#L342) | 342 | `"        signal_id=\"signal-1\","` | — |
| [SRC-2822F30DAD-L000343](../../tests/test_sales_domain.py#L343) | 343 | `"        product_fit=ProductFit.FIT,"` | — |
| [SRC-2822F30DAD-L000344](../../tests/test_sales_domain.py#L344) | 344 | `"        source_quality=SourceQuality.PRIMARY_SOURCE,"` | — |
| [SRC-2822F30DAD-L000345](../../tests/test_sales_domain.py#L345) | 345 | `"        freshness=FreshnessStatus.CURRENT,"` | — |
| [SRC-2822F30DAD-L000346](../../tests/test_sales_domain.py#L346) | 346 | `"        identity_status=IdentityStatus.UNVERIFIED,"` | — |
| [SRC-2822F30DAD-L000347](../../tests/test_sales_domain.py#L347) | 347 | `"        contactability=ContactabilityStatus.NOT_ASSESSED,"` | — |
| [SRC-2822F30DAD-L000348](../../tests/test_sales_domain.py#L348) | 348 | `"        missing_information=(\"buyer identity\", \"public contact channel\"),"` | — |
| [SRC-2822F30DAD-L000349](../../tests/test_sales_domain.py#L349) | 349 | `"    )"` | — |
| [SRC-2822F30DAD-L000350](../../tests/test_sales_domain.py#L350) | 350 | `""` | — |
| [SRC-2822F30DAD-L000351](../../tests/test_sales_domain.py#L351) | 351 | `"    result = assessment.to_dict()"` | — |
| [SRC-2822F30DAD-L000352](../../tests/test_sales_domain.py#L352) | 352 | `"    assert result[\"product_fit\"] == \"fit\""` | — |
| [SRC-2822F30DAD-L000353](../../tests/test_sales_domain.py#L353) | 353 | `"    assert result[\"source_quality\"] == \"primary_source\""` | — |
| [SRC-2822F30DAD-L000354](../../tests/test_sales_domain.py#L354) | 354 | `"    assert result[\"freshness\"] == \"current\""` | — |
| [SRC-2822F30DAD-L000355](../../tests/test_sales_domain.py#L355) | 355 | `"    assert result[\"identity_status\"] == \"unverified\""` | — |
| [SRC-2822F30DAD-L000356](../../tests/test_sales_domain.py#L356) | 356 | `"    assert result[\"missing_information\"] == [\"buyer identity\", \"public contact channel\"]"` | — |
| [SRC-2822F30DAD-L000357](../../tests/test_sales_domain.py#L357) | 357 | `"    assert \"purchase_probability\" not in result"` | — |
| [SRC-2822F30DAD-L000358](../../tests/test_sales_domain.py#L358) | 358 | `"    assert \"confidence\" not in result"` | — |
| [SRC-2822F30DAD-L000359](../../tests/test_sales_domain.py#L359) | 359 | `""` | — |
| [SRC-2822F30DAD-L000360](../../tests/test_sales_domain.py#L360) | 360 | `""` | — |
| [SRC-2822F30DAD-L000361](../../tests/test_sales_domain.py#L361) | 361 | `"def test_to_json_dict_preserves_all_evidence_provenance_fields():"` | — |
| [SRC-2822F30DAD-L000362](../../tests/test_sales_domain.py#L362) | 362 | `"    evidence = page_evidence(event_date=\"2026-10-18\")"` | — |
| [SRC-2822F30DAD-L000363](../../tests/test_sales_domain.py#L363) | 363 | `"    serialized = to_json_dict(evidence)"` | — |
| [SRC-2822F30DAD-L000364](../../tests/test_sales_domain.py#L364) | 364 | `""` | — |
| [SRC-2822F30DAD-L000365](../../tests/test_sales_domain.py#L365) | 365 | `"    assert serialized[\"source_url\"] == \"https://example.org/public-post/1\""` | — |
| [SRC-2822F30DAD-L000366](../../tests/test_sales_domain.py#L366) | 366 | `"    assert serialized[\"content_basis\"] == \"page_text\""` | — |
| [SRC-2822F30DAD-L000367](../../tests/test_sales_domain.py#L367) | 367 | `"    assert serialized[\"publication_date\"] == \"2026-10-20\""` | — |
| [SRC-2822F30DAD-L000368](../../tests/test_sales_domain.py#L368) | 368 | `"    assert serialized[\"event_date\"] == \"2026-10-18\""` | — |
| [SRC-2822F30DAD-L000369](../../tests/test_sales_domain.py#L369) | 369 | `"    assert serialized[\"observed_at\"] == \"2026-10-31T08:00:00Z\""` | — |
| [SRC-2822F30DAD-L000370](../../tests/test_sales_domain.py#L370) | 370 | `"    assert serialized[\"page_read\"] is True"` | — |
| [SRC-2822F30DAD-L000371](../../tests/test_sales_domain.py#L371) | 371 | `""` | — |
| [SRC-2822F30DAD-L000372](../../tests/test_sales_domain.py#L372) | 372 | `""` | — |
| [SRC-2822F30DAD-L000373](../../tests/test_sales_domain.py#L373) | 373 | `"def test_domain_models_reject_invalid_sequence_types():"` | — |
| [SRC-2822F30DAD-L000374](../../tests/test_sales_domain.py#L374) | 374 | `"    with pytest.raises(TypeError, match=\"iterable of strings\"):"` | — |
| [SRC-2822F30DAD-L000375](../../tests/test_sales_domain.py#L375) | 375 | `"        ProductProfile(name=\"Product\", aliases=\"one alias\")"` | — |
| [SRC-2822F30DAD-L000376](../../tests/test_sales_domain.py#L376) | 376 | `""` | — |
| [SRC-2822F30DAD-L000377](../../tests/test_sales_domain.py#L377) | 377 | `"    with pytest.raises(TypeError, match=\"TaxonomyCategory instances\"):"` | — |
| [SRC-2822F30DAD-L000378](../../tests/test_sales_domain.py#L378) | 378 | `"        ProductTaxonomy(categories=(\"property\",))"` | — |
| [SRC-2822F30DAD-L000379](../../tests/test_sales_domain.py#L379) | 379 | `""` | — |
| [SRC-2822F30DAD-L000380](../../tests/test_sales_domain.py#L380) | 380 | `""` | — |
| [SRC-2822F30DAD-L000381](../../tests/test_sales_domain.py#L381) | 381 | `"def test_contactability_is_not_inferred_from_identity():"` | — |
| [SRC-2822F30DAD-L000382](../../tests/test_sales_domain.py#L382) | 382 | `"    assessment = LeadQualification("` | — |
| [SRC-2822F30DAD-L000383](../../tests/test_sales_domain.py#L383) | 383 | `"        signal_id=\"signal-contact\","` | — |
| [SRC-2822F30DAD-L000384](../../tests/test_sales_domain.py#L384) | 384 | `"        identity_status=IdentityStatus.VERIFIED,"` | — |
| [SRC-2822F30DAD-L000385](../../tests/test_sales_domain.py#L385) | 385 | `"    )"` | — |
| [SRC-2822F30DAD-L000386](../../tests/test_sales_domain.py#L386) | 386 | `""` | — |
| [SRC-2822F30DAD-L000387](../../tests/test_sales_domain.py#L387) | 387 | `"    assert assessment.identity_status == IdentityStatus.VERIFIED"` | — |
| [SRC-2822F30DAD-L000388](../../tests/test_sales_domain.py#L388) | 388 | `"    assert assessment.contactability == ContactabilityStatus.NOT_ASSESSED"` | — |
## اختبارات

### FILE-2614DCB6FB — [tests/test_search_code.py](../../tests/test_search_code.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-2614DCB6FB-L000001](../../tests/test_search_code.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-2614DCB6FB-L000002](../../tests/test_search_code.py#L2) | 2 | `""` | — |
| [SRC-2614DCB6FB-L000003](../../tests/test_search_code.py#L3) | 3 | `"import importlib.util"` | — |
| [SRC-2614DCB6FB-L000004](../../tests/test_search_code.py#L4) | 4 | `"import re"` | — |
| [SRC-2614DCB6FB-L000005](../../tests/test_search_code.py#L5) | 5 | `"import sys"` | — |
| [SRC-2614DCB6FB-L000006](../../tests/test_search_code.py#L6) | 6 | `"from pathlib import Path"` | — |
| [SRC-2614DCB6FB-L000007](../../tests/test_search_code.py#L7) | 7 | `""` | — |
| [SRC-2614DCB6FB-L000008](../../tests/test_search_code.py#L8) | 8 | `"SEARCH_PATH = Path(__file__).resolve().parents[1] / \"docs\" / \"search_code.py\""` | — |
| [SRC-2614DCB6FB-L000009](../../tests/test_search_code.py#L9) | 9 | `"SEARCH_SPEC = importlib.util.spec_from_file_location(\"omarai_search_code_for_tests\", SEARCH_PATH)"` | — |
| [SRC-2614DCB6FB-L000010](../../tests/test_search_code.py#L10) | 10 | `"assert SEARCH_SPEC is not None"` | — |
| [SRC-2614DCB6FB-L000011](../../tests/test_search_code.py#L11) | 11 | `"assert SEARCH_SPEC.loader is not None"` | — |
| [SRC-2614DCB6FB-L000012](../../tests/test_search_code.py#L12) | 12 | `"SEARCH = importlib.util.module_from_spec(SEARCH_SPEC)"` | — |
| [SRC-2614DCB6FB-L000013](../../tests/test_search_code.py#L13) | 13 | `"sys.modules[SEARCH_SPEC.name] = SEARCH"` | — |
| [SRC-2614DCB6FB-L000014](../../tests/test_search_code.py#L14) | 14 | `"SEARCH_SPEC.loader.exec_module(SEARCH)"` | — |
| [SRC-2614DCB6FB-L000015](../../tests/test_search_code.py#L15) | 15 | `""` | — |
| [SRC-2614DCB6FB-L000016](../../tests/test_search_code.py#L16) | 16 | `""` | — |
| [SRC-2614DCB6FB-L000017](../../tests/test_search_code.py#L17) | 17 | `"def test_search_returns_stable_file_line_and_source_link(tmp_path: Path) -> None:"` | — |
| [SRC-2614DCB6FB-L000018](../../tests/test_search_code.py#L18) | 18 | `"    \"\"\"Text search returns the exact file and 1-based line without network access.\"\"\""` | — |
| [SRC-2614DCB6FB-L000019](../../tests/test_search_code.py#L19) | 19 | `"    source = tmp_path / \"app.py\""` | — |
| [SRC-2614DCB6FB-L000020](../../tests/test_search_code.py#L20) | 20 | `"    source.write_text(\"first = 1\\nneedle = 2\\nlast = 3\\n\", encoding=\"utf-8\")"` | — |
| [SRC-2614DCB6FB-L000021](../../tests/test_search_code.py#L21) | 21 | `""` | — |
| [SRC-2614DCB6FB-L000022](../../tests/test_search_code.py#L22) | 22 | `"    hits = SEARCH.search_repository(tmp_path, \"needle\")"` | — |
| [SRC-2614DCB6FB-L000023](../../tests/test_search_code.py#L23) | 23 | `""` | — |
| [SRC-2614DCB6FB-L000024](../../tests/test_search_code.py#L24) | 24 | `"    assert len(hits) == 1"` | — |
| [SRC-2614DCB6FB-L000025](../../tests/test_search_code.py#L25) | 25 | `"    assert hits[0].file == \"app.py\""` | — |
| [SRC-2614DCB6FB-L000026](../../tests/test_search_code.py#L26) | 26 | `"    assert hits[0].line == 2"` | — |
| [SRC-2614DCB6FB-L000027](../../tests/test_search_code.py#L27) | 27 | `"    assert \"needle = 2\" in hits[0].text"` | — |
| [SRC-2614DCB6FB-L000028](../../tests/test_search_code.py#L28) | 28 | `"    assert hits[0].link.endswith(\"/app.py#L2\")"` | — |
| [SRC-2614DCB6FB-L000029](../../tests/test_search_code.py#L29) | 29 | `""` | — |
| [SRC-2614DCB6FB-L000030](../../tests/test_search_code.py#L30) | 30 | `""` | — |
| [SRC-2614DCB6FB-L000031](../../tests/test_search_code.py#L31) | 31 | `"def test_search_supports_multiline_context_and_regex(tmp_path: Path) -> None:"` | — |
| [SRC-2614DCB6FB-L000032](../../tests/test_search_code.py#L32) | 32 | `"    \"\"\"The context argument returns the requested number of adjacent lines.\"\"\""` | — |
| [SRC-2614DCB6FB-L000033](../../tests/test_search_code.py#L33) | 33 | `"    source = tmp_path / \"app.py\""` | — |
| [SRC-2614DCB6FB-L000034](../../tests/test_search_code.py#L34) | 34 | `"    source.write_text(\"before one\\nbefore two\\nVALUE_42 = 7\\nafter one\\nafter two\\n\", encoding=\"utf-8\")"` | — |
| [SRC-2614DCB6FB-L000035](../../tests/test_search_code.py#L35) | 35 | `""` | — |
| [SRC-2614DCB6FB-L000036](../../tests/test_search_code.py#L36) | 36 | `"    hits = SEARCH.search_repository("` | — |
| [SRC-2614DCB6FB-L000037](../../tests/test_search_code.py#L37) | 37 | `"        tmp_path, r\"VALUE_\\d+\", use_regex=True, context=2"` | — |
| [SRC-2614DCB6FB-L000038](../../tests/test_search_code.py#L38) | 38 | `"    )"` | — |
| [SRC-2614DCB6FB-L000039](../../tests/test_search_code.py#L39) | 39 | `""` | — |
| [SRC-2614DCB6FB-L000040](../../tests/test_search_code.py#L40) | 40 | `"    assert len(hits) == 1"` | — |
| [SRC-2614DCB6FB-L000041](../../tests/test_search_code.py#L41) | 41 | `"    assert hits[0].context_before.splitlines() == [\"before one\", \"before two\"]"` | — |
| [SRC-2614DCB6FB-L000042](../../tests/test_search_code.py#L42) | 42 | `"    assert hits[0].context_after.splitlines() == [\"after one\", \"after two\"]"` | — |
| [SRC-2614DCB6FB-L000043](../../tests/test_search_code.py#L43) | 43 | `""` | — |
| [SRC-2614DCB6FB-L000044](../../tests/test_search_code.py#L44) | 44 | `""` | — |
| [SRC-2614DCB6FB-L000045](../../tests/test_search_code.py#L45) | 45 | `"def test_search_excludes_common_secret_files_and_runtime_directories(tmp_path: Path) -> None:"` | — |
| [SRC-2614DCB6FB-L000046](../../tests/test_search_code.py#L46) | 46 | `"    \"\"\"Local searches skip common secret paths and binary/runtime data.\"\"\""` | — |
| [SRC-2614DCB6FB-L000047](../../tests/test_search_code.py#L47) | 47 | `"    (tmp_path / \"app.py\").write_text(\"safe_value = 1\\n\", encoding=\"utf-8\")"` | — |
| [SRC-2614DCB6FB-L000048](../../tests/test_search_code.py#L48) | 48 | `"    (tmp_path / \".env\").write_text(\"TOKEN=private-value\\n\", encoding=\"utf-8\")"` | — |
| [SRC-2614DCB6FB-L000049](../../tests/test_search_code.py#L49) | 49 | `"    (tmp_path / \"credentials.json\").write_text('{\"token\":\"private-value\"}\\n', encoding=\"utf-8\")"` | — |
| [SRC-2614DCB6FB-L000050](../../tests/test_search_code.py#L50) | 50 | `"    aws_dir = tmp_path / \".aws\""` | — |
| [SRC-2614DCB6FB-L000051](../../tests/test_search_code.py#L51) | 51 | `"    aws_dir.mkdir()"` | — |
| [SRC-2614DCB6FB-L000052](../../tests/test_search_code.py#L52) | 52 | `"    (aws_dir / \"credentials\").write_text(\"token=private-value\\n\", encoding=\"utf-8\")"` | — |
| [SRC-2614DCB6FB-L000053](../../tests/test_search_code.py#L53) | 53 | `"    data_dir = tmp_path / \"data\""` | — |
| [SRC-2614DCB6FB-L000054](../../tests/test_search_code.py#L54) | 54 | `"    data_dir.mkdir()"` | — |
| [SRC-2614DCB6FB-L000055](../../tests/test_search_code.py#L55) | 55 | `"    (data_dir / \"records.sqlite3\").write_bytes(b\"database-token\")"` | — |
| [SRC-2614DCB6FB-L000056](../../tests/test_search_code.py#L56) | 56 | `"    (tmp_path / \"credentials.example\").write_text(\"TOKEN=replace-me\\n\", encoding=\"utf-8\")"` | — |
| [SRC-2614DCB6FB-L000057](../../tests/test_search_code.py#L57) | 57 | `""` | — |
| [SRC-2614DCB6FB-L000058](../../tests/test_search_code.py#L58) | 58 | `"    hits = SEARCH.search_repository(tmp_path, \"private-value\")"` | — |
| [SRC-2614DCB6FB-L000059](../../tests/test_search_code.py#L59) | 59 | `"    safe_example = SEARCH.search_repository(tmp_path, \"replace-me\")"` | — |
| [SRC-2614DCB6FB-L000060](../../tests/test_search_code.py#L60) | 60 | `""` | — |
| [SRC-2614DCB6FB-L000061](../../tests/test_search_code.py#L61) | 61 | `"    assert hits == []"` | — |
| [SRC-2614DCB6FB-L000062](../../tests/test_search_code.py#L62) | 62 | `"    assert len(safe_example) == 1"` | — |
| [SRC-2614DCB6FB-L000063](../../tests/test_search_code.py#L63) | 63 | `"    assert safe_example[0].file == \"credentials.example\""` | — |
| [SRC-2614DCB6FB-L000064](../../tests/test_search_code.py#L64) | 64 | `""` | — |
| [SRC-2614DCB6FB-L000065](../../tests/test_search_code.py#L65) | 65 | `""` | — |
| [SRC-2614DCB6FB-L000066](../../tests/test_search_code.py#L66) | 66 | `"def test_search_validates_query_limits_and_reports_invalid_regex(tmp_path: Path) -> None:"` | — |
| [SRC-2614DCB6FB-L000067](../../tests/test_search_code.py#L67) | 67 | `"    \"\"\"Invalid search controls fail clearly instead of silently returning confusing results.\"\"\""` | — |
| [SRC-2614DCB6FB-L000068](../../tests/test_search_code.py#L68) | 68 | `"    try:"` | — |
| [SRC-2614DCB6FB-L000069](../../tests/test_search_code.py#L69) | 69 | `"        SEARCH.search_repository(tmp_path, \"\")"` | — |
| [SRC-2614DCB6FB-L000070](../../tests/test_search_code.py#L70) | 70 | `"    except ValueError as exc:"` | — |
| [SRC-2614DCB6FB-L000071](../../tests/test_search_code.py#L71) | 71 | `"        assert \"فارغ\" in str(exc)"` | — |
| [SRC-2614DCB6FB-L000072](../../tests/test_search_code.py#L72) | 72 | `"    else:"` | — |
| [SRC-2614DCB6FB-L000073](../../tests/test_search_code.py#L73) | 73 | `"        raise AssertionError(\"An empty search query should be rejected.\")"` | — |
| [SRC-2614DCB6FB-L000074](../../tests/test_search_code.py#L74) | 74 | `""` | — |
| [SRC-2614DCB6FB-L000075](../../tests/test_search_code.py#L75) | 75 | `"    for kwargs in ({\"max_results\": 0}, {\"context\": -1}):"` | — |
| [SRC-2614DCB6FB-L000076](../../tests/test_search_code.py#L76) | 76 | `"        try:"` | — |
| [SRC-2614DCB6FB-L000077](../../tests/test_search_code.py#L77) | 77 | `"            SEARCH.search_repository(tmp_path, \"needle\", **kwargs)"` | — |
| [SRC-2614DCB6FB-L000078](../../tests/test_search_code.py#L78) | 78 | `"        except ValueError:"` | — |
| [SRC-2614DCB6FB-L000079](../../tests/test_search_code.py#L79) | 79 | `"            continue"` | — |
| [SRC-2614DCB6FB-L000080](../../tests/test_search_code.py#L80) | 80 | `"        raise AssertionError(f\"Invalid search limits should be rejected: {kwargs}\")"` | — |
| [SRC-2614DCB6FB-L000081](../../tests/test_search_code.py#L81) | 81 | `""` | — |
| [SRC-2614DCB6FB-L000082](../../tests/test_search_code.py#L82) | 82 | `"    try:"` | — |
| [SRC-2614DCB6FB-L000083](../../tests/test_search_code.py#L83) | 83 | `"        SEARCH.search_repository(tmp_path, \"(\", use_regex=True)"` | — |
| [SRC-2614DCB6FB-L000084](../../tests/test_search_code.py#L84) | 84 | `"    except re.error:"` | — |
| [SRC-2614DCB6FB-L000085](../../tests/test_search_code.py#L85) | 85 | `"        pass"` | — |
| [SRC-2614DCB6FB-L000086](../../tests/test_search_code.py#L86) | 86 | `"    else:"` | — |
| [SRC-2614DCB6FB-L000087](../../tests/test_search_code.py#L87) | 87 | `"        raise AssertionError(\"An invalid regular expression should be rejected.\")"` | — |
| [SRC-2614DCB6FB-L000088](../../tests/test_search_code.py#L88) | 88 | `""` | — |
| [SRC-2614DCB6FB-L000089](../../tests/test_search_code.py#L89) | 89 | `"def test_search_links_use_the_requested_revision_not_main(tmp_path: Path) -> None:"` | — |
| [SRC-2614DCB6FB-L000090](../../tests/test_search_code.py#L90) | 90 | `"    source = tmp_path / \"app.py\""` | — |
| [SRC-2614DCB6FB-L000091](../../tests/test_search_code.py#L91) | 91 | `"    source.write_text(\"needle = 1\\n\", encoding=\"utf-8\")"` | — |
| [SRC-2614DCB6FB-L000092](../../tests/test_search_code.py#L92) | 92 | `""` | — |
| [SRC-2614DCB6FB-L000093](../../tests/test_search_code.py#L93) | 93 | `"    hits = SEARCH.search_repository("` | — |
| [SRC-2614DCB6FB-L000094](../../tests/test_search_code.py#L94) | 94 | `"        tmp_path, \"needle\", repository_ref=\"fix/review-branch\""` | — |
| [SRC-2614DCB6FB-L000095](../../tests/test_search_code.py#L95) | 95 | `"    )"` | — |
| [SRC-2614DCB6FB-L000096](../../tests/test_search_code.py#L96) | 96 | `""` | — |
| [SRC-2614DCB6FB-L000097](../../tests/test_search_code.py#L97) | 97 | `"    assert len(hits) == 1"` | — |
| [SRC-2614DCB6FB-L000098](../../tests/test_search_code.py#L98) | 98 | `"    assert hits[0].link == ("` | — |
| [SRC-2614DCB6FB-L000099](../../tests/test_search_code.py#L99) | 99 | `"        \"https://github.com/mosabosama2030-oss/omarai/\""` | — |
| [SRC-2614DCB6FB-L000100](../../tests/test_search_code.py#L100) | 100 | `"        \"blob/fix/review-branch/app.py#L1\""` | — |
| [SRC-2614DCB6FB-L000101](../../tests/test_search_code.py#L101) | 101 | `"    )"` | — |
| [SRC-2614DCB6FB-L000102](../../tests/test_search_code.py#L102) | 102 | `""` | — |
| [SRC-2614DCB6FB-L000103](../../tests/test_search_code.py#L103) | 103 | `""` | — |
| [SRC-2614DCB6FB-L000104](../../tests/test_search_code.py#L104) | 104 | `"def test_default_repository_ref_prefers_explicit_environment_override("` | — |
| [SRC-2614DCB6FB-L000105](../../tests/test_search_code.py#L105) | 105 | `"    monkeypatch, tmp_path: Path"` | — |
| [SRC-2614DCB6FB-L000106](../../tests/test_search_code.py#L106) | 106 | `") -> None:"` | — |
| [SRC-2614DCB6FB-L000107](../../tests/test_search_code.py#L107) | 107 | `"    monkeypatch.setenv(\"OMARAI_GITHUB_REF\", \"feature/current-review\")"` | — |
| [SRC-2614DCB6FB-L000108](../../tests/test_search_code.py#L108) | 108 | `"    monkeypatch.setenv(\"GITHUB_SHA\", \"a\" * 40)"` | — |
| [SRC-2614DCB6FB-L000109](../../tests/test_search_code.py#L109) | 109 | `""` | — |
| [SRC-2614DCB6FB-L000110](../../tests/test_search_code.py#L110) | 110 | `"    assert SEARCH.default_repository_ref(tmp_path) == \"feature/current-review\""` | — |
| [SRC-2614DCB6FB-L000111](../../tests/test_search_code.py#L111) | 111 | `""` | — |
| [SRC-2614DCB6FB-L000112](../../tests/test_search_code.py#L112) | 112 | `""` | — |
| [SRC-2614DCB6FB-L000113](../../tests/test_search_code.py#L113) | 113 | `"def test_default_repository_ref_uses_valid_ci_sha("` | — |
| [SRC-2614DCB6FB-L000114](../../tests/test_search_code.py#L114) | 114 | `"    monkeypatch, tmp_path: Path"` | — |
| [SRC-2614DCB6FB-L000115](../../tests/test_search_code.py#L115) | 115 | `") -> None:"` | — |
| [SRC-2614DCB6FB-L000116](../../tests/test_search_code.py#L116) | 116 | `"    monkeypatch.delenv(\"OMARAI_GITHUB_REF\", raising=False)"` | — |
| [SRC-2614DCB6FB-L000117](../../tests/test_search_code.py#L117) | 117 | `"    monkeypatch.setenv(\"GITHUB_SHA\", \"B\" * 40)"` | — |
| [SRC-2614DCB6FB-L000118](../../tests/test_search_code.py#L118) | 118 | `""` | — |
| [SRC-2614DCB6FB-L000119](../../tests/test_search_code.py#L119) | 119 | `"    assert SEARCH.default_repository_ref(tmp_path) == \"b\" * 40"` | — |
| [SRC-2614DCB6FB-L000120](../../tests/test_search_code.py#L120) | 120 | `""` | — |
| [SRC-2614DCB6FB-L000121](../../tests/test_search_code.py#L121) | 121 | `"def test_cli_uses_explicit_ref_for_source_links(tmp_path: Path, capsys) -> None:"` | — |
| [SRC-2614DCB6FB-L000122](../../tests/test_search_code.py#L122) | 122 | `"    source = tmp_path / \"app.py\""` | — |
| [SRC-2614DCB6FB-L000123](../../tests/test_search_code.py#L123) | 123 | `"    source.write_text(\"needle = 1\\n\", encoding=\"utf-8\")"` | — |
| [SRC-2614DCB6FB-L000124](../../tests/test_search_code.py#L124) | 124 | `""` | — |
| [SRC-2614DCB6FB-L000125](../../tests/test_search_code.py#L125) | 125 | `"    exit_code = SEARCH.main(["` | — |
| [SRC-2614DCB6FB-L000126](../../tests/test_search_code.py#L126) | 126 | `"        \"needle\", \"--root\", str(tmp_path), \"--ref\", \"fix/cli-review\""` | — |
| [SRC-2614DCB6FB-L000127](../../tests/test_search_code.py#L127) | 127 | `"    ])"` | — |
| [SRC-2614DCB6FB-L000128](../../tests/test_search_code.py#L128) | 128 | `""` | — |
| [SRC-2614DCB6FB-L000129](../../tests/test_search_code.py#L129) | 129 | `"    output = capsys.readouterr().out"` | — |
| [SRC-2614DCB6FB-L000130](../../tests/test_search_code.py#L130) | 130 | `"    assert exit_code == 0"` | — |
| [SRC-2614DCB6FB-L000131](../../tests/test_search_code.py#L131) | 131 | `"    assert \"blob/fix/cli-review/app.py#L1\" in output"` | — |
| [SRC-2614DCB6FB-L000132](../../tests/test_search_code.py#L132) | 132 | `"    assert \"blob/main/app.py#L1\" not in output"` | — |
| [SRC-2614DCB6FB-L000133](../../tests/test_search_code.py#L133) | 133 | `""` | — |
## اختبارات

### FILE-888168CDEB — [tests/test_search_connector_boundaries.py](../../tests/test_search_connector_boundaries.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-888168CDEB-L000001](../../tests/test_search_connector_boundaries.py#L1) | 1 | `"\"\"\"Security regression tests for outbound search connector boundaries.\"\"\""` | — |
| [SRC-888168CDEB-L000002](../../tests/test_search_connector_boundaries.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-888168CDEB-L000003](../../tests/test_search_connector_boundaries.py#L3) | 3 | `""` | — |
| [SRC-888168CDEB-L000004](../../tests/test_search_connector_boundaries.py#L4) | 4 | `"import json"` | — |
| [SRC-888168CDEB-L000005](../../tests/test_search_connector_boundaries.py#L5) | 5 | `"import socket"` | — |
| [SRC-888168CDEB-L000006](../../tests/test_search_connector_boundaries.py#L6) | 6 | `"import urllib.request"` | — |
| [SRC-888168CDEB-L000007](../../tests/test_search_connector_boundaries.py#L7) | 7 | `""` | — |
| [SRC-888168CDEB-L000008](../../tests/test_search_connector_boundaries.py#L8) | 8 | `"import pytest"` | — |
| [SRC-888168CDEB-L000009](../../tests/test_search_connector_boundaries.py#L9) | 9 | `""` | — |
| [SRC-888168CDEB-L000010](../../tests/test_search_connector_boundaries.py#L10) | 10 | `"from agents import search_connectors"` | — |
| [SRC-888168CDEB-L000011](../../tests/test_search_connector_boundaries.py#L11) | 11 | `"from agents.web_agent import _public_http_url, _public_ip_literals"` | — |
| [SRC-888168CDEB-L000012](../../tests/test_search_connector_boundaries.py#L12) | 12 | `""` | — |
| [SRC-888168CDEB-L000013](../../tests/test_search_connector_boundaries.py#L13) | 13 | `""` | — |
| [SRC-888168CDEB-L000014](../../tests/test_search_connector_boundaries.py#L14) | 14 | `"class _FakeResponse:"` | — |
| [SRC-888168CDEB-L000015](../../tests/test_search_connector_boundaries.py#L15) | 15 | `"    def __init__(self, body: bytes):"` | — |
| [SRC-888168CDEB-L000016](../../tests/test_search_connector_boundaries.py#L16) | 16 | `"        self.body = body"` | — |
| [SRC-888168CDEB-L000017](../../tests/test_search_connector_boundaries.py#L17) | 17 | `"        self.read_limit = None"` | — |
| [SRC-888168CDEB-L000018](../../tests/test_search_connector_boundaries.py#L18) | 18 | `""` | — |
| [SRC-888168CDEB-L000019](../../tests/test_search_connector_boundaries.py#L19) | 19 | `"    def __enter__(self):"` | — |
| [SRC-888168CDEB-L000020](../../tests/test_search_connector_boundaries.py#L20) | 20 | `"        return self"` | — |
| [SRC-888168CDEB-L000021](../../tests/test_search_connector_boundaries.py#L21) | 21 | `""` | — |
| [SRC-888168CDEB-L000022](../../tests/test_search_connector_boundaries.py#L22) | 22 | `"    def __exit__(self, *_args):"` | — |
| [SRC-888168CDEB-L000023](../../tests/test_search_connector_boundaries.py#L23) | 23 | `"        return False"` | — |
| [SRC-888168CDEB-L000024](../../tests/test_search_connector_boundaries.py#L24) | 24 | `""` | — |
| [SRC-888168CDEB-L000025](../../tests/test_search_connector_boundaries.py#L25) | 25 | `"    def read(self, limit: int):"` | — |
| [SRC-888168CDEB-L000026](../../tests/test_search_connector_boundaries.py#L26) | 26 | `"        self.read_limit = limit"` | — |
| [SRC-888168CDEB-L000027](../../tests/test_search_connector_boundaries.py#L27) | 27 | `"        return self.body[:limit]"` | — |
| [SRC-888168CDEB-L000028](../../tests/test_search_connector_boundaries.py#L28) | 28 | `""` | — |
| [SRC-888168CDEB-L000029](../../tests/test_search_connector_boundaries.py#L29) | 29 | `""` | — |
| [SRC-888168CDEB-L000030](../../tests/test_search_connector_boundaries.py#L30) | 30 | `"class _FakeOpener:"` | — |
| [SRC-888168CDEB-L000031](../../tests/test_search_connector_boundaries.py#L31) | 31 | `"    def __init__(self, response):"` | — |
| [SRC-888168CDEB-L000032](../../tests/test_search_connector_boundaries.py#L32) | 32 | `"        self.response = response"` | — |
| [SRC-888168CDEB-L000033](../../tests/test_search_connector_boundaries.py#L33) | 33 | `"        self.request = None"` | — |
| [SRC-888168CDEB-L000034](../../tests/test_search_connector_boundaries.py#L34) | 34 | `"        self.timeout = None"` | — |
| [SRC-888168CDEB-L000035](../../tests/test_search_connector_boundaries.py#L35) | 35 | `""` | — |
| [SRC-888168CDEB-L000036](../../tests/test_search_connector_boundaries.py#L36) | 36 | `"    def open(self, request, timeout):"` | — |
| [SRC-888168CDEB-L000037](../../tests/test_search_connector_boundaries.py#L37) | 37 | `"        self.request = request"` | — |
| [SRC-888168CDEB-L000038](../../tests/test_search_connector_boundaries.py#L38) | 38 | `"        self.timeout = timeout"` | — |
| [SRC-888168CDEB-L000039](../../tests/test_search_connector_boundaries.py#L39) | 39 | `"        return self.response"` | — |
| [SRC-888168CDEB-L000040](../../tests/test_search_connector_boundaries.py#L40) | 40 | `""` | — |
| [SRC-888168CDEB-L000041](../../tests/test_search_connector_boundaries.py#L41) | 41 | `""` | — |
| [SRC-888168CDEB-L000042](../../tests/test_search_connector_boundaries.py#L42) | 42 | `"def test_academic_connectors_do_not_follow_provider_redirects():"` | — |
| [SRC-888168CDEB-L000043](../../tests/test_search_connector_boundaries.py#L43) | 43 | `"    handler = search_connectors._NoRedirectHandler()"` | — |
| [SRC-888168CDEB-L000044](../../tests/test_search_connector_boundaries.py#L44) | 44 | `"    request = urllib.request.Request(\"https://api.openalex.org/works\")"` | — |
| [SRC-888168CDEB-L000045](../../tests/test_search_connector_boundaries.py#L45) | 45 | `"    assert handler.redirect_request("` | — |
| [SRC-888168CDEB-L000046](../../tests/test_search_connector_boundaries.py#L46) | 46 | `"        request, None, 302, \"Found\", {}, \"http://127.0.0.1/admin\""` | — |
| [SRC-888168CDEB-L000047](../../tests/test_search_connector_boundaries.py#L47) | 47 | `"    ) is None"` | — |
| [SRC-888168CDEB-L000048](../../tests/test_search_connector_boundaries.py#L48) | 48 | `""` | — |
| [SRC-888168CDEB-L000049](../../tests/test_search_connector_boundaries.py#L49) | 49 | `""` | — |
| [SRC-888168CDEB-L000050](../../tests/test_search_connector_boundaries.py#L50) | 50 | `"def test_academic_json_connector_uses_no_redirect_handler_and_bounded_read(monkeypatch):"` | — |
| [SRC-888168CDEB-L000051](../../tests/test_search_connector_boundaries.py#L51) | 51 | `"    body = json.dumps({\"results\": []}).encode()"` | — |
| [SRC-888168CDEB-L000052](../../tests/test_search_connector_boundaries.py#L52) | 52 | `"    response = _FakeResponse(body)"` | — |
| [SRC-888168CDEB-L000053](../../tests/test_search_connector_boundaries.py#L53) | 53 | `"    opener = _FakeOpener(response)"` | — |
| [SRC-888168CDEB-L000054](../../tests/test_search_connector_boundaries.py#L54) | 54 | `"    captured = {}"` | — |
| [SRC-888168CDEB-L000055](../../tests/test_search_connector_boundaries.py#L55) | 55 | `""` | — |
| [SRC-888168CDEB-L000056](../../tests/test_search_connector_boundaries.py#L56) | 56 | `"    def build_opener(handler_class):"` | — |
| [SRC-888168CDEB-L000057](../../tests/test_search_connector_boundaries.py#L57) | 57 | `"        captured[\"handler_class\"] = handler_class"` | — |
| [SRC-888168CDEB-L000058](../../tests/test_search_connector_boundaries.py#L58) | 58 | `"        return opener"` | — |
| [SRC-888168CDEB-L000059](../../tests/test_search_connector_boundaries.py#L59) | 59 | `""` | — |
| [SRC-888168CDEB-L000060](../../tests/test_search_connector_boundaries.py#L60) | 60 | `"    monkeypatch.setattr(search_connectors.urllib.request, \"build_opener\", build_opener)"` | — |
| [SRC-888168CDEB-L000061](../../tests/test_search_connector_boundaries.py#L61) | 61 | `"    assert search_connectors._http_get_json(\"https://api.openalex.org/works\") == {"` | — |
| [SRC-888168CDEB-L000062](../../tests/test_search_connector_boundaries.py#L62) | 62 | `"        \"results\": []"` | — |
| [SRC-888168CDEB-L000063](../../tests/test_search_connector_boundaries.py#L63) | 63 | `"    }"` | — |
| [SRC-888168CDEB-L000064](../../tests/test_search_connector_boundaries.py#L64) | 64 | `"    assert captured[\"handler_class\"] is search_connectors._NoRedirectHandler"` | — |
| [SRC-888168CDEB-L000065](../../tests/test_search_connector_boundaries.py#L65) | 65 | `"    assert response.read_limit == search_connectors.MAX_CONNECTOR_RESPONSE_BYTES + 1"` | — |
| [SRC-888168CDEB-L000066](../../tests/test_search_connector_boundaries.py#L66) | 66 | `"    assert opener.timeout == search_connectors.DEFAULT_TIMEOUT_SECONDS"` | — |
| [SRC-888168CDEB-L000067](../../tests/test_search_connector_boundaries.py#L67) | 67 | `""` | — |
| [SRC-888168CDEB-L000068](../../tests/test_search_connector_boundaries.py#L68) | 68 | `""` | — |
| [SRC-888168CDEB-L000069](../../tests/test_search_connector_boundaries.py#L69) | 69 | `"def test_academic_text_connector_rejects_oversized_response(monkeypatch):"` | — |
| [SRC-888168CDEB-L000070](../../tests/test_search_connector_boundaries.py#L70) | 70 | `"    response = _FakeResponse(b\"x\" * (search_connectors.MAX_CONNECTOR_RESPONSE_BYTES + 1))"` | — |
| [SRC-888168CDEB-L000071](../../tests/test_search_connector_boundaries.py#L71) | 71 | `"    opener = _FakeOpener(response)"` | — |
| [SRC-888168CDEB-L000072](../../tests/test_search_connector_boundaries.py#L72) | 72 | `"    monkeypatch.setattr("` | — |
| [SRC-888168CDEB-L000073](../../tests/test_search_connector_boundaries.py#L73) | 73 | `"        search_connectors.urllib.request,"` | — |
| [SRC-888168CDEB-L000074](../../tests/test_search_connector_boundaries.py#L74) | 74 | `"        \"build_opener\","` | — |
| [SRC-888168CDEB-L000075](../../tests/test_search_connector_boundaries.py#L75) | 75 | `"        lambda handler_class: opener,"` | — |
| [SRC-888168CDEB-L000076](../../tests/test_search_connector_boundaries.py#L76) | 76 | `"    )"` | — |
| [SRC-888168CDEB-L000077](../../tests/test_search_connector_boundaries.py#L77) | 77 | `"    with pytest.raises(ValueError, match=\"size limit\"):"` | — |
| [SRC-888168CDEB-L000078](../../tests/test_search_connector_boundaries.py#L78) | 78 | `"        search_connectors._http_get_text(\"https://export.arxiv.org/api/query\")"` | — |
| [SRC-888168CDEB-L000079](../../tests/test_search_connector_boundaries.py#L79) | 79 | `""` | — |
| [SRC-888168CDEB-L000080](../../tests/test_search_connector_boundaries.py#L80) | 80 | `""` | — |
| [SRC-888168CDEB-L000081](../../tests/test_search_connector_boundaries.py#L81) | 81 | `"@pytest.mark.parametrize("` | — |
| [SRC-888168CDEB-L000082](../../tests/test_search_connector_boundaries.py#L82) | 82 | `"    \"url\","` | — |
| [SRC-888168CDEB-L000083](../../tests/test_search_connector_boundaries.py#L83) | 83 | `"    ["` | — |
| [SRC-888168CDEB-L000084](../../tests/test_search_connector_boundaries.py#L84) | 84 | `"        \"http://127.0.0.1/admin\","` | — |
| [SRC-888168CDEB-L000085](../../tests/test_search_connector_boundaries.py#L85) | 85 | `"        \"http://10.0.0.8/\","` | — |
| [SRC-888168CDEB-L000086](../../tests/test_search_connector_boundaries.py#L86) | 86 | `"        \"http://172.16.0.1/\","` | — |
| [SRC-888168CDEB-L000087](../../tests/test_search_connector_boundaries.py#L87) | 87 | `"        \"http://192.168.1.20/\","` | — |
| [SRC-888168CDEB-L000088](../../tests/test_search_connector_boundaries.py#L88) | 88 | `"        \"http://169.254.169.254/latest/meta-data\","` | — |
| [SRC-888168CDEB-L000089](../../tests/test_search_connector_boundaries.py#L89) | 89 | `"        \"http://0.0.0.0/\","` | — |
| [SRC-888168CDEB-L000090](../../tests/test_search_connector_boundaries.py#L90) | 90 | `"        \"http://[::1]/\","` | — |
| [SRC-888168CDEB-L000091](../../tests/test_search_connector_boundaries.py#L91) | 91 | `"        \"http://[fc00::1]/\","` | — |
| [SRC-888168CDEB-L000092](../../tests/test_search_connector_boundaries.py#L92) | 92 | `"        \"http://[fe80::1]/\","` | — |
| [SRC-888168CDEB-L000093](../../tests/test_search_connector_boundaries.py#L93) | 93 | `"        \"http://[::ffff:127.0.0.1]/\","` | — |
| [SRC-888168CDEB-L000094](../../tests/test_search_connector_boundaries.py#L94) | 94 | `"        \"http://localhost/\","` | — |
| [SRC-888168CDEB-L000095](../../tests/test_search_connector_boundaries.py#L95) | 95 | `"        \"http://router.local/\","` | — |
| [SRC-888168CDEB-L000096](../../tests/test_search_connector_boundaries.py#L96) | 96 | `"        \"http://service.internal/\","` | — |
| [SRC-888168CDEB-L000097](../../tests/test_search_connector_boundaries.py#L97) | 97 | `"    ],"` | — |
| [SRC-888168CDEB-L000098](../../tests/test_search_connector_boundaries.py#L98) | 98 | `")"` | — |
| [SRC-888168CDEB-L000099](../../tests/test_search_connector_boundaries.py#L99) | 99 | `"def test_public_url_filter_rejects_private_local_and_non_global_targets(url):"` | — |
| [SRC-888168CDEB-L000100](../../tests/test_search_connector_boundaries.py#L100) | 100 | `"    assert _public_http_url(url) is None"` | — |
| [SRC-888168CDEB-L000101](../../tests/test_search_connector_boundaries.py#L101) | 101 | `""` | — |
| [SRC-888168CDEB-L000102](../../tests/test_search_connector_boundaries.py#L102) | 102 | `""` | — |
| [SRC-888168CDEB-L000103](../../tests/test_search_connector_boundaries.py#L103) | 103 | `"@pytest.mark.parametrize("` | — |
| [SRC-888168CDEB-L000104](../../tests/test_search_connector_boundaries.py#L104) | 104 | `"    \"address\","` | — |
| [SRC-888168CDEB-L000105](../../tests/test_search_connector_boundaries.py#L105) | 105 | `"    ["` | — |
| [SRC-888168CDEB-L000106](../../tests/test_search_connector_boundaries.py#L106) | 106 | `"        \"127.0.0.1\","` | — |
| [SRC-888168CDEB-L000107](../../tests/test_search_connector_boundaries.py#L107) | 107 | `"        \"10.0.0.8\","` | — |
| [SRC-888168CDEB-L000108](../../tests/test_search_connector_boundaries.py#L108) | 108 | `"        \"169.254.169.254\","` | — |
| [SRC-888168CDEB-L000109](../../tests/test_search_connector_boundaries.py#L109) | 109 | `"        \"::1\","` | — |
| [SRC-888168CDEB-L000110](../../tests/test_search_connector_boundaries.py#L110) | 110 | `"        \"fc00::1\","` | — |
| [SRC-888168CDEB-L000111](../../tests/test_search_connector_boundaries.py#L111) | 111 | `"        \"fe80::1\","` | — |
| [SRC-888168CDEB-L000112](../../tests/test_search_connector_boundaries.py#L112) | 112 | `"        \"::ffff:127.0.0.1\","` | — |
| [SRC-888168CDEB-L000113](../../tests/test_search_connector_boundaries.py#L113) | 113 | `"    ],"` | — |
| [SRC-888168CDEB-L000114](../../tests/test_search_connector_boundaries.py#L114) | 114 | `")"` | — |
| [SRC-888168CDEB-L000115](../../tests/test_search_connector_boundaries.py#L115) | 115 | `"def test_dns_resolution_fails_closed_for_private_or_local_answers(monkeypatch, address):"` | — |
| [SRC-888168CDEB-L000116](../../tests/test_search_connector_boundaries.py#L116) | 116 | `"    family = socket.AF_INET6 if \":\" in address else socket.AF_INET"` | — |
| [SRC-888168CDEB-L000117](../../tests/test_search_connector_boundaries.py#L117) | 117 | `"    answer = (family, socket.SOCK_STREAM, socket.IPPROTO_TCP, \"\", (address, 443, 0, 0))"` | — |
| [SRC-888168CDEB-L000118](../../tests/test_search_connector_boundaries.py#L118) | 118 | `"    monkeypatch.setattr("` | — |
| [SRC-888168CDEB-L000119](../../tests/test_search_connector_boundaries.py#L119) | 119 | `"        socket,"` | — |
| [SRC-888168CDEB-L000120](../../tests/test_search_connector_boundaries.py#L120) | 120 | `"        \"getaddrinfo\","` | — |
| [SRC-888168CDEB-L000121](../../tests/test_search_connector_boundaries.py#L121) | 121 | `"        lambda *_args, **_kwargs: [answer],"` | — |
| [SRC-888168CDEB-L000122](../../tests/test_search_connector_boundaries.py#L122) | 122 | `"    )"` | — |
| [SRC-888168CDEB-L000123](../../tests/test_search_connector_boundaries.py#L123) | 123 | `"    assert _public_ip_literals(\"private-answer.example\") is None"` | — |
| [SRC-888168CDEB-L000124](../../tests/test_search_connector_boundaries.py#L124) | 124 | `""` | — |
| [SRC-888168CDEB-L000125](../../tests/test_search_connector_boundaries.py#L125) | 125 | `""` | — |
| [SRC-888168CDEB-L000126](../../tests/test_search_connector_boundaries.py#L126) | 126 | `"def test_public_url_filter_keeps_public_https_targets():"` | — |
| [SRC-888168CDEB-L000127](../../tests/test_search_connector_boundaries.py#L127) | 127 | `"    assert _public_http_url(\"https://example.com/path\") == \"https://example.com/path\""` | — |
## اختبارات

### FILE-86913A3106 — [tests/test_search_relevance_mixed_results.py](../../tests/test_search_relevance_mixed_results.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-86913A3106-L000001](../../tests/test_search_relevance_mixed_results.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-86913A3106-L000002](../../tests/test_search_relevance_mixed_results.py#L2) | 2 | `""` | — |
| [SRC-86913A3106-L000003](../../tests/test_search_relevance_mixed_results.py#L3) | 3 | `"import httpx"` | — |
| [SRC-86913A3106-L000004](../../tests/test_search_relevance_mixed_results.py#L4) | 4 | `"import pytest"` | — |
| [SRC-86913A3106-L000005](../../tests/test_search_relevance_mixed_results.py#L5) | 5 | `""` | — |
| [SRC-86913A3106-L000006](../../tests/test_search_relevance_mixed_results.py#L6) | 6 | `"from agents.web_agent import WebAgent, _minimum_relevance_ratio, _relevance_ratio, _relevance_query_tokens"` | — |
| [SRC-86913A3106-L000007](../../tests/test_search_relevance_mixed_results.py#L7) | 7 | `""` | — |
| [SRC-86913A3106-L000008](../../tests/test_search_relevance_mixed_results.py#L8) | 8 | `""` | — |
| [SRC-86913A3106-L000009](../../tests/test_search_relevance_mixed_results.py#L9) | 9 | `"def test_search_web_keeps_relevant_official_result_and_drops_maps_help(monkeypatch):"` | — |
| [SRC-86913A3106-L000010](../../tests/test_search_relevance_mixed_results.py#L10) | 10 | `"    agent = WebAgent()"` | — |
| [SRC-86913A3106-L000011](../../tests/test_search_relevance_mixed_results.py#L11) | 11 | `"    query = \"الموقع الرسمي للبنك المركزي المصري\""` | — |
| [SRC-86913A3106-L000012](../../tests/test_search_relevance_mixed_results.py#L12) | 12 | `"    unrelated = {"` | — |
| [SRC-86913A3106-L000013](../../tests/test_search_relevance_mixed_results.py#L13) | 13 | `"        \"title\": \"خرائط Google\","` | — |
| [SRC-86913A3106-L000014](../../tests/test_search_relevance_mixed_results.py#L14) | 14 | `"        \"url\": \"https://support.google.com/maps/answer/2839911?hl=ar-sa\","` | — |
| [SRC-86913A3106-L000015](../../tests/test_search_relevance_mixed_results.py#L15) | 15 | `"        \"snippet\": \"البحث عن موقعك الجغرافي وتحسين دقته في خرائط Google.\","` | — |
| [SRC-86913A3106-L000016](../../tests/test_search_relevance_mixed_results.py#L16) | 16 | `"        \"provider\": \"test_provider\","` | — |
| [SRC-86913A3106-L000017](../../tests/test_search_relevance_mixed_results.py#L17) | 17 | `"        \"provider_rank\": 1,"` | — |
| [SRC-86913A3106-L000018](../../tests/test_search_relevance_mixed_results.py#L18) | 18 | `"    }"` | — |
| [SRC-86913A3106-L000019](../../tests/test_search_relevance_mixed_results.py#L19) | 19 | `"    official = {"` | — |
| [SRC-86913A3106-L000020](../../tests/test_search_relevance_mixed_results.py#L20) | 20 | `"        \"title\": \"Central Bank of Egypt - Official Website\","` | — |
| [SRC-86913A3106-L000021](../../tests/test_search_relevance_mixed_results.py#L21) | 21 | `"        \"url\": \"https://www.cbe.org.eg/en/Pages/default.aspx\","` | — |
| [SRC-86913A3106-L000022](../../tests/test_search_relevance_mixed_results.py#L22) | 22 | `"        \"snippet\": \"Official website of the Central Bank of Egypt and its monetary policy decisions.\","` | — |
| [SRC-86913A3106-L000023](../../tests/test_search_relevance_mixed_results.py#L23) | 23 | `"        \"provider\": \"test_provider\","` | — |
| [SRC-86913A3106-L000024](../../tests/test_search_relevance_mixed_results.py#L24) | 24 | `"        \"provider_rank\": 2,"` | — |
| [SRC-86913A3106-L000025](../../tests/test_search_relevance_mixed_results.py#L25) | 25 | `"    }"` | — |
| [SRC-86913A3106-L000026](../../tests/test_search_relevance_mixed_results.py#L26) | 26 | `""` | — |
| [SRC-86913A3106-L000027](../../tests/test_search_relevance_mixed_results.py#L27) | 27 | `"    for env_name in (\"DEEPSEEK_SEARCH_API_KEY\", \"BRAVE_SEARCH_API_KEY\", \"TAVILY_API_KEY\"):"` | — |
| [SRC-86913A3106-L000028](../../tests/test_search_relevance_mixed_results.py#L28) | 28 | `"        monkeypatch.delenv(env_name, raising=False)"` | — |
| [SRC-86913A3106-L000029](../../tests/test_search_relevance_mixed_results.py#L29) | 29 | `""` | — |
| [SRC-86913A3106-L000030](../../tests/test_search_relevance_mixed_results.py#L30) | 30 | `"    monkeypatch.setattr(agent, \"_search_duckduckgo_html\", lambda _query: [dict(unrelated), dict(official)])"` | — |
| [SRC-86913A3106-L000031](../../tests/test_search_relevance_mixed_results.py#L31) | 31 | `"    monkeypatch.setattr(agent, \"_search_bing_rss\", lambda _query: [dict(unrelated)])"` | — |
| [SRC-86913A3106-L000032](../../tests/test_search_relevance_mixed_results.py#L32) | 32 | `"    monkeypatch.setattr(agent, \"_search_news\", lambda _query: [])"` | — |
| [SRC-86913A3106-L000033](../../tests/test_search_relevance_mixed_results.py#L33) | 33 | `""` | — |
| [SRC-86913A3106-L000034](../../tests/test_search_relevance_mixed_results.py#L34) | 34 | `"    results = agent._search_web(query)"` | — |
| [SRC-86913A3106-L000035](../../tests/test_search_relevance_mixed_results.py#L35) | 35 | `""` | — |
| [SRC-86913A3106-L000036](../../tests/test_search_relevance_mixed_results.py#L36) | 36 | `"    assert [item[\"url\"] for item in results] == [official[\"url\"]]"` | — |
| [SRC-86913A3106-L000037](../../tests/test_search_relevance_mixed_results.py#L37) | 37 | `"    diagnostics = {"` | — |
| [SRC-86913A3106-L000038](../../tests/test_search_relevance_mixed_results.py#L38) | 38 | `"        row[\"provider\"]: row"` | — |
| [SRC-86913A3106-L000039](../../tests/test_search_relevance_mixed_results.py#L39) | 39 | `"        for row in agent._provider_diagnostics"` | — |
| [SRC-86913A3106-L000040](../../tests/test_search_relevance_mixed_results.py#L40) | 40 | `"        if row.get(\"provider\") in {\"duckduckgo_html\", \"bing_rss\"}"` | — |
| [SRC-86913A3106-L000041](../../tests/test_search_relevance_mixed_results.py#L41) | 41 | `"    }"` | — |
| [SRC-86913A3106-L000042](../../tests/test_search_relevance_mixed_results.py#L42) | 42 | `"    assert diagnostics[\"duckduckgo_html\"][\"status\"] == \"ok\""` | — |
| [SRC-86913A3106-L000043](../../tests/test_search_relevance_mixed_results.py#L43) | 43 | `"    assert diagnostics[\"duckduckgo_html\"][\"accepted_count\"] == 1"` | — |
| [SRC-86913A3106-L000044](../../tests/test_search_relevance_mixed_results.py#L44) | 44 | `"    assert diagnostics[\"duckduckgo_html\"][\"rejection_counts\"][\"relevance_below_threshold\"] == 1"` | — |
| [SRC-86913A3106-L000045](../../tests/test_search_relevance_mixed_results.py#L45) | 45 | `"    assert diagnostics[\"bing_rss\"][\"status\"] == \"filtered_all\""` | — |
| [SRC-86913A3106-L000046](../../tests/test_search_relevance_mixed_results.py#L46) | 46 | `"    assert diagnostics[\"bing_rss\"][\"accepted_count\"] == 0"` | — |
| [SRC-86913A3106-L000047](../../tests/test_search_relevance_mixed_results.py#L47) | 47 | `"    assert diagnostics[\"bing_rss\"][\"rejection_counts\"][\"relevance_below_threshold\"] == 1"` | — |
| [SRC-86913A3106-L000048](../../tests/test_search_relevance_mixed_results.py#L48) | 48 | `""` | — |
| [SRC-86913A3106-L000049](../../tests/test_search_relevance_mixed_results.py#L49) | 49 | `""` | — |
| [SRC-86913A3106-L000050](../../tests/test_search_relevance_mixed_results.py#L50) | 50 | `"def test_three_concept_query_rejects_candidate_matching_only_one_topic():"` | — |
| [SRC-86913A3106-L000051](../../tests/test_search_relevance_mixed_results.py#L51) | 51 | `"    query = \"climate policy emissions\""` | — |
| [SRC-86913A3106-L000052](../../tests/test_search_relevance_mixed_results.py#L52) | 52 | `"    assert len(_relevance_query_tokens(query)) == 3"` | — |
| [SRC-86913A3106-L000053](../../tests/test_search_relevance_mixed_results.py#L53) | 53 | `"    assert _relevance_ratio(query, \"Climate report\") == 0.0"` | — |
| [SRC-86913A3106-L000054](../../tests/test_search_relevance_mixed_results.py#L54) | 54 | `""` | — |
| [SRC-86913A3106-L000055](../../tests/test_search_relevance_mixed_results.py#L55) | 55 | `""` | — |
| [SRC-86913A3106-L000056](../../tests/test_search_relevance_mixed_results.py#L56) | 56 | `"def test_three_concept_query_documents_single_high_value_match_tradeoff():"` | — |
| [SRC-86913A3106-L000057](../../tests/test_search_relevance_mixed_results.py#L57) | 57 | `"    query = \"central bank Egypt\""` | — |
| [SRC-86913A3106-L000058](../../tests/test_search_relevance_mixed_results.py#L58) | 58 | `"    assert len(_relevance_query_tokens(query)) == 3"` | — |
| [SRC-86913A3106-L000059](../../tests/test_search_relevance_mixed_results.py#L59) | 59 | `"    assert _relevance_ratio(query, \"Egypt\") == 0.0"` | — |
| [SRC-86913A3106-L000060](../../tests/test_search_relevance_mixed_results.py#L60) | 60 | `""` | — |
| [SRC-86913A3106-L000061](../../tests/test_search_relevance_mixed_results.py#L61) | 61 | `""` | — |
| [SRC-86913A3106-L000062](../../tests/test_search_relevance_mixed_results.py#L62) | 62 | `"def test_short_two_concept_query_keeps_existing_relevance_floor():"` | — |
| [SRC-86913A3106-L000063](../../tests/test_search_relevance_mixed_results.py#L63) | 63 | `"    assert _relevance_ratio(\"climate emissions\", \"Climate report\") >= _minimum_relevance_ratio(\"climate emissions\")"` | — |
| [SRC-86913A3106-L000064](../../tests/test_search_relevance_mixed_results.py#L64) | 64 | `""` | — |
| [SRC-86913A3106-L000065](../../tests/test_search_relevance_mixed_results.py#L65) | 65 | `""` | — |
| [SRC-86913A3106-L000066](../../tests/test_search_relevance_mixed_results.py#L66) | 66 | `"def test_search_web_preserves_same_page_discovered_by_distinct_providers(monkeypatch):"` | — |
| [SRC-86913A3106-L000067](../../tests/test_search_relevance_mixed_results.py#L67) | 67 | `"    agent = WebAgent()"` | — |
| [SRC-86913A3106-L000068](../../tests/test_search_relevance_mixed_results.py#L68) | 68 | `"    query = \"Central Bank of Egypt official website\""` | — |
| [SRC-86913A3106-L000069](../../tests/test_search_relevance_mixed_results.py#L69) | 69 | `"    candidate = {"` | — |
| [SRC-86913A3106-L000070](../../tests/test_search_relevance_mixed_results.py#L70) | 70 | `"        \"title\": \"Central Bank of Egypt official website\","` | — |
| [SRC-86913A3106-L000071](../../tests/test_search_relevance_mixed_results.py#L71) | 71 | `"        \"url\": \"https://example.com/cbe\","` | — |
| [SRC-86913A3106-L000072](../../tests/test_search_relevance_mixed_results.py#L72) | 72 | `"        \"snippet\": \"Official Central Bank of Egypt website and monetary policy.\","` | — |
| [SRC-86913A3106-L000073](../../tests/test_search_relevance_mixed_results.py#L73) | 73 | `"    }"` | — |
| [SRC-86913A3106-L000074](../../tests/test_search_relevance_mixed_results.py#L74) | 74 | `"    for env_name in ("` | — |
| [SRC-86913A3106-L000075](../../tests/test_search_relevance_mixed_results.py#L75) | 75 | `"        \"DEEPSEEK_SEARCH_API_KEY\","` | — |
| [SRC-86913A3106-L000076](../../tests/test_search_relevance_mixed_results.py#L76) | 76 | `"        \"BRAVE_SEARCH_API_KEY\","` | — |
| [SRC-86913A3106-L000077](../../tests/test_search_relevance_mixed_results.py#L77) | 77 | `"        \"TAVILY_API_KEY\","` | — |
| [SRC-86913A3106-L000078](../../tests/test_search_relevance_mixed_results.py#L78) | 78 | `"    ):"` | — |
| [SRC-86913A3106-L000079](../../tests/test_search_relevance_mixed_results.py#L79) | 79 | `"        monkeypatch.delenv(env_name, raising=False)"` | — |
| [SRC-86913A3106-L000080](../../tests/test_search_relevance_mixed_results.py#L80) | 80 | `""` | — |
| [SRC-86913A3106-L000081](../../tests/test_search_relevance_mixed_results.py#L81) | 81 | `"    monkeypatch.setattr("` | — |
| [SRC-86913A3106-L000082](../../tests/test_search_relevance_mixed_results.py#L82) | 82 | `"        agent, \"_search_duckduckgo_html\","` | — |
| [SRC-86913A3106-L000083](../../tests/test_search_relevance_mixed_results.py#L83) | 83 | `"        lambda _query: ["` | — |
| [SRC-86913A3106-L000084](../../tests/test_search_relevance_mixed_results.py#L84) | 84 | `"            {**candidate, \"url\": \"https://example.com/cbe?utm_source=ddg#home\"},"` | — |
| [SRC-86913A3106-L000085](../../tests/test_search_relevance_mixed_results.py#L85) | 85 | `"            dict(candidate),"` | — |
| [SRC-86913A3106-L000086](../../tests/test_search_relevance_mixed_results.py#L86) | 86 | `"        ],"` | — |
| [SRC-86913A3106-L000087](../../tests/test_search_relevance_mixed_results.py#L87) | 87 | `"    )"` | — |
| [SRC-86913A3106-L000088](../../tests/test_search_relevance_mixed_results.py#L88) | 88 | `"    monkeypatch.setattr("` | — |
| [SRC-86913A3106-L000089](../../tests/test_search_relevance_mixed_results.py#L89) | 89 | `"        agent, \"_search_bing_rss\","` | — |
| [SRC-86913A3106-L000090](../../tests/test_search_relevance_mixed_results.py#L90) | 90 | `"        lambda _query: [{**candidate, \"url\": \"https://example.com/cbe?utm_source=bing\"}],"` | — |
| [SRC-86913A3106-L000091](../../tests/test_search_relevance_mixed_results.py#L91) | 91 | `"    )"` | — |
| [SRC-86913A3106-L000092](../../tests/test_search_relevance_mixed_results.py#L92) | 92 | `"    monkeypatch.setattr(agent, \"_search_news\", lambda _query: [])"` | — |
| [SRC-86913A3106-L000093](../../tests/test_search_relevance_mixed_results.py#L93) | 93 | `""` | — |
| [SRC-86913A3106-L000094](../../tests/test_search_relevance_mixed_results.py#L94) | 94 | `"    results = agent._search_web(query)"` | — |
| [SRC-86913A3106-L000095](../../tests/test_search_relevance_mixed_results.py#L95) | 95 | `""` | — |
| [SRC-86913A3106-L000096](../../tests/test_search_relevance_mixed_results.py#L96) | 96 | `"    assert len(results) == 2"` | — |
| [SRC-86913A3106-L000097](../../tests/test_search_relevance_mixed_results.py#L97) | 97 | `"    assert {item[\"provider\"] for item in results} == {"` | — |
| [SRC-86913A3106-L000098](../../tests/test_search_relevance_mixed_results.py#L98) | 98 | `"        \"duckduckgo_html\","` | — |
| [SRC-86913A3106-L000099](../../tests/test_search_relevance_mixed_results.py#L99) | 99 | `"        \"bing_rss\","` | — |
| [SRC-86913A3106-L000100](../../tests/test_search_relevance_mixed_results.py#L100) | 100 | `"    }"` | — |
| [SRC-86913A3106-L000101](../../tests/test_search_relevance_mixed_results.py#L101) | 101 | `"    assert len({"` | — |
| [SRC-86913A3106-L000102](../../tests/test_search_relevance_mixed_results.py#L102) | 102 | `"        agent._normalized_source_url_key(item[\"url\"])"` | — |
| [SRC-86913A3106-L000103](../../tests/test_search_relevance_mixed_results.py#L103) | 103 | `"        for item in results"` | — |
| [SRC-86913A3106-L000104](../../tests/test_search_relevance_mixed_results.py#L104) | 104 | `"    }) == 1"` | — |
| [SRC-86913A3106-L000105](../../tests/test_search_relevance_mixed_results.py#L105) | 105 | `""` | — |
| [SRC-86913A3106-L000106](../../tests/test_search_relevance_mixed_results.py#L106) | 106 | `""` | — |
| [SRC-86913A3106-L000107](../../tests/test_search_relevance_mixed_results.py#L107) | 107 | `"def test_search_web_keeps_best_duplicate_per_provider_without_erasing_other_providers(monkeypatch):"` | — |
| [SRC-86913A3106-L000108](../../tests/test_search_relevance_mixed_results.py#L108) | 108 | `"    agent = WebAgent()"` | — |
| [SRC-86913A3106-L000109](../../tests/test_search_relevance_mixed_results.py#L109) | 109 | `"    query = \"Central Bank of Egypt official website\""` | — |
| [SRC-86913A3106-L000110](../../tests/test_search_relevance_mixed_results.py#L110) | 110 | `"    short = {"` | — |
| [SRC-86913A3106-L000111](../../tests/test_search_relevance_mixed_results.py#L111) | 111 | `"        \"title\": \"Central Bank of Egypt official website\","` | — |
| [SRC-86913A3106-L000112](../../tests/test_search_relevance_mixed_results.py#L112) | 112 | `"        \"url\": \"https://example.com/cbe\","` | — |
| [SRC-86913A3106-L000113](../../tests/test_search_relevance_mixed_results.py#L113) | 113 | `"        \"snippet\": \"Central Bank of Egypt.\","` | — |
| [SRC-86913A3106-L000114](../../tests/test_search_relevance_mixed_results.py#L114) | 114 | `"    }"` | — |
| [SRC-86913A3106-L000115](../../tests/test_search_relevance_mixed_results.py#L115) | 115 | `"    longer = {"` | — |
| [SRC-86913A3106-L000116](../../tests/test_search_relevance_mixed_results.py#L116) | 116 | `"        **short,"` | — |
| [SRC-86913A3106-L000117](../../tests/test_search_relevance_mixed_results.py#L117) | 117 | `"        \"url\": \"https://example.com/cbe?utm_source=ddg\","` | — |
| [SRC-86913A3106-L000118](../../tests/test_search_relevance_mixed_results.py#L118) | 118 | `"        \"snippet\": \"Official Central Bank of Egypt website and monetary policy decisions.\","` | — |
| [SRC-86913A3106-L000119](../../tests/test_search_relevance_mixed_results.py#L119) | 119 | `"    }"` | — |
| [SRC-86913A3106-L000120](../../tests/test_search_relevance_mixed_results.py#L120) | 120 | `"    for env_name in ("` | — |
| [SRC-86913A3106-L000121](../../tests/test_search_relevance_mixed_results.py#L121) | 121 | `"        \"DEEPSEEK_SEARCH_API_KEY\","` | — |
| [SRC-86913A3106-L000122](../../tests/test_search_relevance_mixed_results.py#L122) | 122 | `"        \"BRAVE_SEARCH_API_KEY\","` | — |
| [SRC-86913A3106-L000123](../../tests/test_search_relevance_mixed_results.py#L123) | 123 | `"        \"TAVILY_API_KEY\","` | — |
| [SRC-86913A3106-L000124](../../tests/test_search_relevance_mixed_results.py#L124) | 124 | `"    ):"` | — |
| [SRC-86913A3106-L000125](../../tests/test_search_relevance_mixed_results.py#L125) | 125 | `"        monkeypatch.delenv(env_name, raising=False)"` | — |
| [SRC-86913A3106-L000126](../../tests/test_search_relevance_mixed_results.py#L126) | 126 | `""` | — |
| [SRC-86913A3106-L000127](../../tests/test_search_relevance_mixed_results.py#L127) | 127 | `"    monkeypatch.setattr("` | — |
| [SRC-86913A3106-L000128](../../tests/test_search_relevance_mixed_results.py#L128) | 128 | `"        agent, \"_search_duckduckgo_html\","` | — |
| [SRC-86913A3106-L000129](../../tests/test_search_relevance_mixed_results.py#L129) | 129 | `"        lambda _query: [dict(short), dict(longer)],"` | — |
| [SRC-86913A3106-L000130](../../tests/test_search_relevance_mixed_results.py#L130) | 130 | `"    )"` | — |
| [SRC-86913A3106-L000131](../../tests/test_search_relevance_mixed_results.py#L131) | 131 | `"    monkeypatch.setattr("` | — |
| [SRC-86913A3106-L000132](../../tests/test_search_relevance_mixed_results.py#L132) | 132 | `"        agent, \"_search_bing_rss\","` | — |
| [SRC-86913A3106-L000133](../../tests/test_search_relevance_mixed_results.py#L133) | 133 | `"        lambda _query: [{"` | — |
| [SRC-86913A3106-L000134](../../tests/test_search_relevance_mixed_results.py#L134) | 134 | `"            **short,"` | — |
| [SRC-86913A3106-L000135](../../tests/test_search_relevance_mixed_results.py#L135) | 135 | `"            \"provider\": \"forged_provider\","` | — |
| [SRC-86913A3106-L000136](../../tests/test_search_relevance_mixed_results.py#L136) | 136 | `"            \"search_query\": \"forged search query\","` | — |
| [SRC-86913A3106-L000137](../../tests/test_search_relevance_mixed_results.py#L137) | 137 | `"        }],"` | — |
| [SRC-86913A3106-L000138](../../tests/test_search_relevance_mixed_results.py#L138) | 138 | `"    )"` | — |
| [SRC-86913A3106-L000139](../../tests/test_search_relevance_mixed_results.py#L139) | 139 | `"    monkeypatch.setattr(agent, \"_search_news\", lambda _query: [])"` | — |
| [SRC-86913A3106-L000140](../../tests/test_search_relevance_mixed_results.py#L140) | 140 | `""` | — |
| [SRC-86913A3106-L000141](../../tests/test_search_relevance_mixed_results.py#L141) | 141 | `"    results = agent._search_web(query)"` | — |
| [SRC-86913A3106-L000142](../../tests/test_search_relevance_mixed_results.py#L142) | 142 | `""` | — |
| [SRC-86913A3106-L000143](../../tests/test_search_relevance_mixed_results.py#L143) | 143 | `"    assert len(results) == 2"` | — |
| [SRC-86913A3106-L000144](../../tests/test_search_relevance_mixed_results.py#L144) | 144 | `"    ddg = next(item for item in results if item[\"provider\"] == \"duckduckgo_html\")"` | — |
| [SRC-86913A3106-L000145](../../tests/test_search_relevance_mixed_results.py#L145) | 145 | `"    assert ddg[\"snippet\"] == longer[\"snippet\"]"` | — |
| [SRC-86913A3106-L000146](../../tests/test_search_relevance_mixed_results.py#L146) | 146 | `"    assert {item[\"provider\"] for item in results} == {"` | — |
| [SRC-86913A3106-L000147](../../tests/test_search_relevance_mixed_results.py#L147) | 147 | `"        \"duckduckgo_html\","` | — |
| [SRC-86913A3106-L000148](../../tests/test_search_relevance_mixed_results.py#L148) | 148 | `"        \"bing_rss\","` | — |
| [SRC-86913A3106-L000149](../../tests/test_search_relevance_mixed_results.py#L149) | 149 | `"    }"` | — |
| [SRC-86913A3106-L000150](../../tests/test_search_relevance_mixed_results.py#L150) | 150 | `"    bing = next(item for item in results if item[\"provider\"] == \"bing_rss\")"` | — |
| [SRC-86913A3106-L000151](../../tests/test_search_relevance_mixed_results.py#L151) | 151 | `"    assert bing[\"search_query\"] == query"` | — |
| [SRC-86913A3106-L000152](../../tests/test_search_relevance_mixed_results.py#L152) | 152 | `""` | — |
| [SRC-86913A3106-L000153](../../tests/test_search_relevance_mixed_results.py#L153) | 153 | `""` | — |
| [SRC-86913A3106-L000154](../../tests/test_search_relevance_mixed_results.py#L154) | 154 | `"def test_search_web_stores_normalized_retrieval_relevance_for_fusion(monkeypatch):"` | — |
| [SRC-86913A3106-L000155](../../tests/test_search_relevance_mixed_results.py#L155) | 155 | `"    agent = WebAgent()"` | — |
| [SRC-86913A3106-L000156](../../tests/test_search_relevance_mixed_results.py#L156) | 156 | `"    query = \"Central Bank of Egypt official website\""` | — |
| [SRC-86913A3106-L000157](../../tests/test_search_relevance_mixed_results.py#L157) | 157 | `"    candidate = {"` | — |
| [SRC-86913A3106-L000158](../../tests/test_search_relevance_mixed_results.py#L158) | 158 | `"        \"title\": \"Central Bank of Egypt official website\","` | — |
| [SRC-86913A3106-L000159](../../tests/test_search_relevance_mixed_results.py#L159) | 159 | `"        \"url\": \"https://example.com/cbe\","` | — |
| [SRC-86913A3106-L000160](../../tests/test_search_relevance_mixed_results.py#L160) | 160 | `"        \"snippet\": \"Official Central Bank of Egypt website and monetary policy decisions.\","` | — |
| [SRC-86913A3106-L000161](../../tests/test_search_relevance_mixed_results.py#L161) | 161 | `"    }"` | — |
| [SRC-86913A3106-L000162](../../tests/test_search_relevance_mixed_results.py#L162) | 162 | `"    for env_name in ("` | — |
| [SRC-86913A3106-L000163](../../tests/test_search_relevance_mixed_results.py#L163) | 163 | `"        \"DEEPSEEK_SEARCH_API_KEY\","` | — |
| [SRC-86913A3106-L000164](../../tests/test_search_relevance_mixed_results.py#L164) | 164 | `"        \"BRAVE_SEARCH_API_KEY\","` | — |
| [SRC-86913A3106-L000165](../../tests/test_search_relevance_mixed_results.py#L165) | 165 | `"        \"TAVILY_API_KEY\","` | — |
| [SRC-86913A3106-L000166](../../tests/test_search_relevance_mixed_results.py#L166) | 166 | `"    ):"` | — |
| [SRC-86913A3106-L000167](../../tests/test_search_relevance_mixed_results.py#L167) | 167 | `"        monkeypatch.delenv(env_name, raising=False)"` | — |
| [SRC-86913A3106-L000168](../../tests/test_search_relevance_mixed_results.py#L168) | 168 | `"    monkeypatch.setattr(agent, \"_search_duckduckgo_html\", lambda _query: [dict(candidate)])"` | — |
| [SRC-86913A3106-L000169](../../tests/test_search_relevance_mixed_results.py#L169) | 169 | `"    monkeypatch.setattr(agent, \"_search_bing_rss\", lambda _query: [])"` | — |
| [SRC-86913A3106-L000170](../../tests/test_search_relevance_mixed_results.py#L170) | 170 | `"    monkeypatch.setattr(agent, \"_search_news\", lambda _query: [])"` | — |
| [SRC-86913A3106-L000171](../../tests/test_search_relevance_mixed_results.py#L171) | 171 | `""` | — |
| [SRC-86913A3106-L000172](../../tests/test_search_relevance_mixed_results.py#L172) | 172 | `"    results = agent._search_web(query)"` | — |
| [SRC-86913A3106-L000173](../../tests/test_search_relevance_mixed_results.py#L173) | 173 | `""` | — |
| [SRC-86913A3106-L000174](../../tests/test_search_relevance_mixed_results.py#L174) | 174 | `"    assert len(results) == 1"` | — |
| [SRC-86913A3106-L000175](../../tests/test_search_relevance_mixed_results.py#L175) | 175 | `"    assert 0.0 <= results[0][\"retrieval_relevance_score\"] <= 1.0"` | — |
| [SRC-86913A3106-L000176](../../tests/test_search_relevance_mixed_results.py#L176) | 176 | `""` | — |
| [SRC-86913A3106-L000177](../../tests/test_search_relevance_mixed_results.py#L177) | 177 | `""` | — |
| [SRC-86913A3106-L000178](../../tests/test_search_relevance_mixed_results.py#L178) | 178 | `"def test_rank_fusion_uses_retrieval_relevance_only_for_exact_rrf_ties():"` | — |
| [SRC-86913A3106-L000179](../../tests/test_search_relevance_mixed_results.py#L179) | 179 | `"    from agents.research import fuse_ranked_results"` | — |
| [SRC-86913A3106-L000180](../../tests/test_search_relevance_mixed_results.py#L180) | 180 | `""` | — |
| [SRC-86913A3106-L000181](../../tests/test_search_relevance_mixed_results.py#L181) | 181 | `"    weak = {"` | — |
| [SRC-86913A3106-L000182](../../tests/test_search_relevance_mixed_results.py#L182) | 182 | `"        \"title\": \"Egypt central bank\","` | — |
| [SRC-86913A3106-L000183](../../tests/test_search_relevance_mixed_results.py#L183) | 183 | `"        \"url\": \"https://example.com/weak\","` | — |
| [SRC-86913A3106-L000184](../../tests/test_search_relevance_mixed_results.py#L184) | 184 | `"        \"snippet\": \"Egypt central bank\","` | — |
| [SRC-86913A3106-L000185](../../tests/test_search_relevance_mixed_results.py#L185) | 185 | `"        \"retrieval_relevance_score\": 0.2,"` | — |
| [SRC-86913A3106-L000186](../../tests/test_search_relevance_mixed_results.py#L186) | 186 | `"    }"` | — |
| [SRC-86913A3106-L000187](../../tests/test_search_relevance_mixed_results.py#L187) | 187 | `"    strong = {"` | — |
| [SRC-86913A3106-L000188](../../tests/test_search_relevance_mixed_results.py#L188) | 188 | `"        \"title\": \"Central Bank of Egypt official website\","` | — |
| [SRC-86913A3106-L000189](../../tests/test_search_relevance_mixed_results.py#L189) | 189 | `"        \"url\": \"https://example.com/strong\","` | — |
| [SRC-86913A3106-L000190](../../tests/test_search_relevance_mixed_results.py#L190) | 190 | `"        \"snippet\": \"Central Bank of Egypt official website and monetary policy.\","` | — |
| [SRC-86913A3106-L000191](../../tests/test_search_relevance_mixed_results.py#L191) | 191 | `"        \"retrieval_relevance_score\": 1.0,"` | — |
| [SRC-86913A3106-L000192](../../tests/test_search_relevance_mixed_results.py#L192) | 192 | `"    }"` | — |
| [SRC-86913A3106-L000193](../../tests/test_search_relevance_mixed_results.py#L193) | 193 | `"    batches = ["` | — |
| [SRC-86913A3106-L000194](../../tests/test_search_relevance_mixed_results.py#L194) | 194 | `"        {"` | — |
| [SRC-86913A3106-L000195](../../tests/test_search_relevance_mixed_results.py#L195) | 195 | `"            \"query\": \"Central Bank of Egypt official website\","` | — |
| [SRC-86913A3106-L000196](../../tests/test_search_relevance_mixed_results.py#L196) | 196 | `"            \"provider\": \"ddg\","` | — |
| [SRC-86913A3106-L000197](../../tests/test_search_relevance_mixed_results.py#L197) | 197 | `"            \"results\": [dict(weak), dict(strong)],"` | — |
| [SRC-86913A3106-L000198](../../tests/test_search_relevance_mixed_results.py#L198) | 198 | `"        },"` | — |
| [SRC-86913A3106-L000199](../../tests/test_search_relevance_mixed_results.py#L199) | 199 | `"        {"` | — |
| [SRC-86913A3106-L000200](../../tests/test_search_relevance_mixed_results.py#L200) | 200 | `"            \"query\": \"Central Bank of Egypt official website\","` | — |
| [SRC-86913A3106-L000201](../../tests/test_search_relevance_mixed_results.py#L201) | 201 | `"            \"provider\": \"bing\","` | — |
| [SRC-86913A3106-L000202](../../tests/test_search_relevance_mixed_results.py#L202) | 202 | `"            \"results\": [dict(strong), dict(weak)],"` | — |
| [SRC-86913A3106-L000203](../../tests/test_search_relevance_mixed_results.py#L203) | 203 | `"        },"` | — |
| [SRC-86913A3106-L000204](../../tests/test_search_relevance_mixed_results.py#L204) | 204 | `"    ]"` | — |
| [SRC-86913A3106-L000205](../../tests/test_search_relevance_mixed_results.py#L205) | 205 | `""` | — |
| [SRC-86913A3106-L000206](../../tests/test_search_relevance_mixed_results.py#L206) | 206 | `"    ranked = fuse_ranked_results(batches)"` | — |
| [SRC-86913A3106-L000207](../../tests/test_search_relevance_mixed_results.py#L207) | 207 | `""` | — |
| [SRC-86913A3106-L000208](../../tests/test_search_relevance_mixed_results.py#L208) | 208 | `"    assert ranked[0][\"url\"] == \"https://example.com/strong\""` | — |
| [SRC-86913A3106-L000209](../../tests/test_search_relevance_mixed_results.py#L209) | 209 | `"    assert ranked[0][\"rank_score\"] == ranked[1][\"rank_score\"]"` | — |
| [SRC-86913A3106-L000210](../../tests/test_search_relevance_mixed_results.py#L210) | 210 | `"    assert ranked[0][\"retrieval_relevance_score\"] == 1.0"` | — |
| [SRC-86913A3106-L000211](../../tests/test_search_relevance_mixed_results.py#L211) | 211 | `"    assert set(ranked[0][\"providers\"]) == {\"ddg\", \"bing\"}"` | — |
| [SRC-86913A3106-L000212](../../tests/test_search_relevance_mixed_results.py#L212) | 212 | `""` | — |
| [SRC-86913A3106-L000213](../../tests/test_search_relevance_mixed_results.py#L213) | 213 | `""` | — |
| [SRC-86913A3106-L000214](../../tests/test_search_relevance_mixed_results.py#L214) | 214 | `"def test_rank_fusion_ignores_invalid_retrieval_relevance_scores():"` | — |
| [SRC-86913A3106-L000215](../../tests/test_search_relevance_mixed_results.py#L215) | 215 | `"    from agents.research import fuse_ranked_results"` | — |
| [SRC-86913A3106-L000216](../../tests/test_search_relevance_mixed_results.py#L216) | 216 | `""` | — |
| [SRC-86913A3106-L000217](../../tests/test_search_relevance_mixed_results.py#L217) | 217 | `"    for invalid in (True, -0.1, 1.1, float(\"nan\"), float(\"inf\"), \"not-a-score\"):"` | — |
| [SRC-86913A3106-L000218](../../tests/test_search_relevance_mixed_results.py#L218) | 218 | `"        ranked = fuse_ranked_results([{"` | — |
| [SRC-86913A3106-L000219](../../tests/test_search_relevance_mixed_results.py#L219) | 219 | `"            \"query\": \"Central Bank of Egypt\","` | — |
| [SRC-86913A3106-L000220](../../tests/test_search_relevance_mixed_results.py#L220) | 220 | `"            \"provider\": \"ddg\","` | — |
| [SRC-86913A3106-L000221](../../tests/test_search_relevance_mixed_results.py#L221) | 221 | `"            \"results\": [{"` | — |
| [SRC-86913A3106-L000222](../../tests/test_search_relevance_mixed_results.py#L222) | 222 | `"                \"title\": \"Central Bank of Egypt\","` | — |
| [SRC-86913A3106-L000223](../../tests/test_search_relevance_mixed_results.py#L223) | 223 | `"                \"url\": \"https://example.com/cbe\","` | — |
| [SRC-86913A3106-L000224](../../tests/test_search_relevance_mixed_results.py#L224) | 224 | `"                \"snippet\": \"Central Bank of Egypt official website.\","` | — |
| [SRC-86913A3106-L000225](../../tests/test_search_relevance_mixed_results.py#L225) | 225 | `"                \"retrieval_relevance_score\": invalid,"` | — |
| [SRC-86913A3106-L000226](../../tests/test_search_relevance_mixed_results.py#L226) | 226 | `"            }],"` | — |
| [SRC-86913A3106-L000227](../../tests/test_search_relevance_mixed_results.py#L227) | 227 | `"        }])"` | — |
| [SRC-86913A3106-L000228](../../tests/test_search_relevance_mixed_results.py#L228) | 228 | `"        assert ranked[0][\"retrieval_relevance_score\"] is None"` | — |
| [SRC-86913A3106-L000229](../../tests/test_search_relevance_mixed_results.py#L229) | 229 | `""` | — |
| [SRC-86913A3106-L000230](../../tests/test_search_relevance_mixed_results.py#L230) | 230 | `""` | — |
| [SRC-86913A3106-L000231](../../tests/test_search_relevance_mixed_results.py#L231) | 231 | `"@pytest.mark.parametrize("` | — |
| [SRC-86913A3106-L000232](../../tests/test_search_relevance_mixed_results.py#L232) | 232 | `"    (\"status_code\", \"expected_status\"),"` | — |
| [SRC-86913A3106-L000233](../../tests/test_search_relevance_mixed_results.py#L233) | 233 | `"    ["` | — |
| [SRC-86913A3106-L000234](../../tests/test_search_relevance_mixed_results.py#L234) | 234 | `"        (202, \"blocked\"),"` | — |
| [SRC-86913A3106-L000235](../../tests/test_search_relevance_mixed_results.py#L235) | 235 | `"        (301, \"http_error\"),"` | — |
| [SRC-86913A3106-L000236](../../tests/test_search_relevance_mixed_results.py#L236) | 236 | `"        (403, \"unauthorized\"),"` | — |
| [SRC-86913A3106-L000237](../../tests/test_search_relevance_mixed_results.py#L237) | 237 | `"        (429, \"rate_limited\"),"` | — |
| [SRC-86913A3106-L000238](../../tests/test_search_relevance_mixed_results.py#L238) | 238 | `"        (500, \"http_error\"),"` | — |
| [SRC-86913A3106-L000239](../../tests/test_search_relevance_mixed_results.py#L239) | 239 | `"    ],"` | — |
| [SRC-86913A3106-L000240](../../tests/test_search_relevance_mixed_results.py#L240) | 240 | `")"` | — |
| [SRC-86913A3106-L000241](../../tests/test_search_relevance_mixed_results.py#L241) | 241 | `"def test_httpx_status_errors_are_classified_from_response_status(status_code, expected_status):"` | — |
| [SRC-86913A3106-L000242](../../tests/test_search_relevance_mixed_results.py#L242) | 242 | `"    request = httpx.Request(\"GET\", \"https://provider.example/search\")"` | — |
| [SRC-86913A3106-L000243](../../tests/test_search_relevance_mixed_results.py#L243) | 243 | `"    response = httpx.Response(status_code, request=request)"` | — |
| [SRC-86913A3106-L000244](../../tests/test_search_relevance_mixed_results.py#L244) | 244 | `"    error = httpx.HTTPStatusError("` | — |
| [SRC-86913A3106-L000245](../../tests/test_search_relevance_mixed_results.py#L245) | 245 | `"        \"provider returned a non-success status\","` | — |
| [SRC-86913A3106-L000246](../../tests/test_search_relevance_mixed_results.py#L246) | 246 | `"        request=request,"` | — |
| [SRC-86913A3106-L000247](../../tests/test_search_relevance_mixed_results.py#L247) | 247 | `"        response=response,"` | — |
| [SRC-86913A3106-L000248](../../tests/test_search_relevance_mixed_results.py#L248) | 248 | `"    )"` | — |
| [SRC-86913A3106-L000249](../../tests/test_search_relevance_mixed_results.py#L249) | 249 | `""` | — |
| [SRC-86913A3106-L000250](../../tests/test_search_relevance_mixed_results.py#L250) | 250 | `"    status, detail = WebAgent._classify_provider_exception(error)"` | — |
| [SRC-86913A3106-L000251](../../tests/test_search_relevance_mixed_results.py#L251) | 251 | `""` | — |
| [SRC-86913A3106-L000252](../../tests/test_search_relevance_mixed_results.py#L252) | 252 | `"    assert status == expected_status"` | — |
| [SRC-86913A3106-L000253](../../tests/test_search_relevance_mixed_results.py#L253) | 253 | `"    assert str(status_code) in detail"` | — |
| [SRC-86913A3106-L000254](../../tests/test_search_relevance_mixed_results.py#L254) | 254 | `"    assert \"provider.example\" not in detail"` | — |
| [SRC-86913A3106-L000255](../../tests/test_search_relevance_mixed_results.py#L255) | 255 | `""` | — |
| [SRC-86913A3106-L000256](../../tests/test_search_relevance_mixed_results.py#L256) | 256 | `""` | — |
| [SRC-86913A3106-L000257](../../tests/test_search_relevance_mixed_results.py#L257) | 257 | `"def test_httpx_timeout_and_decoding_errors_are_not_reported_as_generic_failures():"` | — |
| [SRC-86913A3106-L000258](../../tests/test_search_relevance_mixed_results.py#L258) | 258 | `"    request = httpx.Request(\"GET\", \"https://provider.example/search\")"` | — |
| [SRC-86913A3106-L000259](../../tests/test_search_relevance_mixed_results.py#L259) | 259 | `""` | — |
| [SRC-86913A3106-L000260](../../tests/test_search_relevance_mixed_results.py#L260) | 260 | `"    timeout_status, _ = WebAgent._classify_provider_exception("` | — |
| [SRC-86913A3106-L000261](../../tests/test_search_relevance_mixed_results.py#L261) | 261 | `"        httpx.ReadTimeout(\"provider timed out\", request=request)"` | — |
| [SRC-86913A3106-L000262](../../tests/test_search_relevance_mixed_results.py#L262) | 262 | `"    )"` | — |
| [SRC-86913A3106-L000263](../../tests/test_search_relevance_mixed_results.py#L263) | 263 | `"    decoding_status, _ = WebAgent._classify_provider_exception("` | — |
| [SRC-86913A3106-L000264](../../tests/test_search_relevance_mixed_results.py#L264) | 264 | `"        httpx.DecodingError(\"invalid compressed response\")"` | — |
| [SRC-86913A3106-L000265](../../tests/test_search_relevance_mixed_results.py#L265) | 265 | `"    )"` | — |
| [SRC-86913A3106-L000266](../../tests/test_search_relevance_mixed_results.py#L266) | 266 | `""` | — |
| [SRC-86913A3106-L000267](../../tests/test_search_relevance_mixed_results.py#L267) | 267 | `"    assert timeout_status == \"timeout\""` | — |
| [SRC-86913A3106-L000268](../../tests/test_search_relevance_mixed_results.py#L268) | 268 | `"    assert decoding_status == \"invalid_response\""` | — |
| [SRC-86913A3106-L000269](../../tests/test_search_relevance_mixed_results.py#L269) | 269 | `""` | — |
| [SRC-86913A3106-L000270](../../tests/test_search_relevance_mixed_results.py#L270) | 270 | `""` | — |
| [SRC-86913A3106-L000271](../../tests/test_search_relevance_mixed_results.py#L271) | 271 | `"def test_search_web_overwrites_untrusted_provider_and_query_metadata(monkeypatch):"` | — |
| [SRC-86913A3106-L000272](../../tests/test_search_relevance_mixed_results.py#L272) | 272 | `"    agent = WebAgent()"` | — |
| [SRC-86913A3106-L000273](../../tests/test_search_relevance_mixed_results.py#L273) | 273 | `"    dispatched_queries = []"` | — |
| [SRC-86913A3106-L000274](../../tests/test_search_relevance_mixed_results.py#L274) | 274 | `"    candidate = {"` | — |
| [SRC-86913A3106-L000275](../../tests/test_search_relevance_mixed_results.py#L275) | 275 | `"        \"title\": \"Central Bank of Egypt official website\","` | — |
| [SRC-86913A3106-L000276](../../tests/test_search_relevance_mixed_results.py#L276) | 276 | `"        \"url\": \"https://example.com/cbe\","` | — |
| [SRC-86913A3106-L000277](../../tests/test_search_relevance_mixed_results.py#L277) | 277 | `"        \"snippet\": \"Official Central Bank of Egypt website and monetary policy decisions.\","` | — |
| [SRC-86913A3106-L000278](../../tests/test_search_relevance_mixed_results.py#L278) | 278 | `"        \"provider\": \"brave_search_api\","` | — |
| [SRC-86913A3106-L000279](../../tests/test_search_relevance_mixed_results.py#L279) | 279 | `"        \"search_query\": \"tampered query from an untrusted result\","` | — |
| [SRC-86913A3106-L000280](../../tests/test_search_relevance_mixed_results.py#L280) | 280 | `"    }"` | — |
| [SRC-86913A3106-L000281](../../tests/test_search_relevance_mixed_results.py#L281) | 281 | `"    for env_name in ("` | — |
| [SRC-86913A3106-L000282](../../tests/test_search_relevance_mixed_results.py#L282) | 282 | `"        \"DEEPSEEK_SEARCH_API_KEY\","` | — |
| [SRC-86913A3106-L000283](../../tests/test_search_relevance_mixed_results.py#L283) | 283 | `"        \"BRAVE_SEARCH_API_KEY\","` | — |
| [SRC-86913A3106-L000284](../../tests/test_search_relevance_mixed_results.py#L284) | 284 | `"        \"TAVILY_API_KEY\","` | — |
| [SRC-86913A3106-L000285](../../tests/test_search_relevance_mixed_results.py#L285) | 285 | `"    ):"` | — |
| [SRC-86913A3106-L000286](../../tests/test_search_relevance_mixed_results.py#L286) | 286 | `"        monkeypatch.delenv(env_name, raising=False)"` | — |
| [SRC-86913A3106-L000287](../../tests/test_search_relevance_mixed_results.py#L287) | 287 | `""` | — |
| [SRC-86913A3106-L000288](../../tests/test_search_relevance_mixed_results.py#L288) | 288 | `"    def spoofing_provider(query):"` | — |
| [SRC-86913A3106-L000289](../../tests/test_search_relevance_mixed_results.py#L289) | 289 | `"        dispatched_queries.append(query)"` | — |
| [SRC-86913A3106-L000290](../../tests/test_search_relevance_mixed_results.py#L290) | 290 | `"        return [dict(candidate)]"` | — |
| [SRC-86913A3106-L000291](../../tests/test_search_relevance_mixed_results.py#L291) | 291 | `""` | — |
| [SRC-86913A3106-L000292](../../tests/test_search_relevance_mixed_results.py#L292) | 292 | `"    monkeypatch.setattr(agent, \"_search_duckduckgo_html\", spoofing_provider)"` | — |
| [SRC-86913A3106-L000293](../../tests/test_search_relevance_mixed_results.py#L293) | 293 | `"    monkeypatch.setattr(agent, \"_search_bing_rss\", lambda _query: [])"` | — |
| [SRC-86913A3106-L000294](../../tests/test_search_relevance_mixed_results.py#L294) | 294 | `"    monkeypatch.setattr(agent, \"_search_news\", lambda _query: [])"` | — |
| [SRC-86913A3106-L000295](../../tests/test_search_relevance_mixed_results.py#L295) | 295 | `""` | — |
| [SRC-86913A3106-L000296](../../tests/test_search_relevance_mixed_results.py#L296) | 296 | `"    results = agent._search_web(\"Central Bank of Egypt official website\")"` | — |
| [SRC-86913A3106-L000297](../../tests/test_search_relevance_mixed_results.py#L297) | 297 | `""` | — |
| [SRC-86913A3106-L000298](../../tests/test_search_relevance_mixed_results.py#L298) | 298 | `"    assert len(results) == 1"` | — |
| [SRC-86913A3106-L000299](../../tests/test_search_relevance_mixed_results.py#L299) | 299 | `"    assert results[0][\"provider\"] == \"duckduckgo_html\""` | — |
| [SRC-86913A3106-L000300](../../tests/test_search_relevance_mixed_results.py#L300) | 300 | `"    assert results[0][\"provider\"] != candidate[\"provider\"]"` | — |
| [SRC-86913A3106-L000301](../../tests/test_search_relevance_mixed_results.py#L301) | 301 | `"    assert results[0][\"search_query\"] == dispatched_queries[0]"` | — |
| [SRC-86913A3106-L000302](../../tests/test_search_relevance_mixed_results.py#L302) | 302 | `"    assert results[0][\"search_query\"] != candidate[\"search_query\"]"` | — |
## اختبارات

### FILE-AC9D8384E8 — [tests/test_semantic_claim_verifier.py](../../tests/test_semantic_claim_verifier.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-AC9D8384E8-L000001](../../tests/test_semantic_claim_verifier.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-AC9D8384E8-L000002](../../tests/test_semantic_claim_verifier.py#L2) | 2 | `""` | — |
| [SRC-AC9D8384E8-L000003](../../tests/test_semantic_claim_verifier.py#L3) | 3 | `"import json"` | — |
| [SRC-AC9D8384E8-L000004](../../tests/test_semantic_claim_verifier.py#L4) | 4 | `""` | — |
| [SRC-AC9D8384E8-L000005](../../tests/test_semantic_claim_verifier.py#L5) | 5 | `"import pytest"` | — |
| [SRC-AC9D8384E8-L000006](../../tests/test_semantic_claim_verifier.py#L6) | 6 | `""` | — |
| [SRC-AC9D8384E8-L000007](../../tests/test_semantic_claim_verifier.py#L7) | 7 | `"from agents.semantic_claim_verifier import ("` | — |
| [SRC-AC9D8384E8-L000008](../../tests/test_semantic_claim_verifier.py#L8) | 8 | `"    build_semantic_verification_request,"` | — |
| [SRC-AC9D8384E8-L000009](../../tests/test_semantic_claim_verifier.py#L9) | 9 | `"    parse_semantic_verification_response,"` | — |
| [SRC-AC9D8384E8-L000010](../../tests/test_semantic_claim_verifier.py#L10) | 10 | `"    deterministic_claim_screen,"` | — |
| [SRC-AC9D8384E8-L000011](../../tests/test_semantic_claim_verifier.py#L11) | 11 | `")"` | — |
| [SRC-AC9D8384E8-L000012](../../tests/test_semantic_claim_verifier.py#L12) | 12 | `"from agents.web_agent import WebAgent"` | — |
| [SRC-AC9D8384E8-L000013](../../tests/test_semantic_claim_verifier.py#L13) | 13 | `""` | — |
| [SRC-AC9D8384E8-L000014](../../tests/test_semantic_claim_verifier.py#L14) | 14 | `""` | — |
| [SRC-AC9D8384E8-L000015](../../tests/test_semantic_claim_verifier.py#L15) | 15 | `"def source(**overrides):"` | — |
| [SRC-AC9D8384E8-L000016](../../tests/test_semantic_claim_verifier.py#L16) | 16 | `"    value = {"` | — |
| [SRC-AC9D8384E8-L000017](../../tests/test_semantic_claim_verifier.py#L17) | 17 | `"        \"title\": \"Official report\","` | — |
| [SRC-AC9D8384E8-L000018](../../tests/test_semantic_claim_verifier.py#L18) | 18 | `"        \"url\": \"https://example.org/report\","` | — |
| [SRC-AC9D8384E8-L000019](../../tests/test_semantic_claim_verifier.py#L19) | 19 | `"        \"publisher\": \"Example Office\","` | — |
| [SRC-AC9D8384E8-L000020](../../tests/test_semantic_claim_verifier.py#L20) | 20 | `"        \"published_at\": \"2026-10-30\","` | — |
| [SRC-AC9D8384E8-L000021](../../tests/test_semantic_claim_verifier.py#L21) | 21 | `"        \"page_fetched\": True,"` | — |
| [SRC-AC9D8384E8-L000022](../../tests/test_semantic_claim_verifier.py#L22) | 22 | `"        \"page_text\": \"The report states that the system serves 12 facilities.\","` | — |
| [SRC-AC9D8384E8-L000023](../../tests/test_semantic_claim_verifier.py#L23) | 23 | `"        \"snippet\": \"The system serves 12 facilities.\","` | — |
| [SRC-AC9D8384E8-L000024](../../tests/test_semantic_claim_verifier.py#L24) | 24 | `"    }"` | — |
| [SRC-AC9D8384E8-L000025](../../tests/test_semantic_claim_verifier.py#L25) | 25 | `"    value.update(overrides)"` | — |
| [SRC-AC9D8384E8-L000026](../../tests/test_semantic_claim_verifier.py#L26) | 26 | `"    return value"` | — |
| [SRC-AC9D8384E8-L000027](../../tests/test_semantic_claim_verifier.py#L27) | 27 | `""` | — |
| [SRC-AC9D8384E8-L000028](../../tests/test_semantic_claim_verifier.py#L28) | 28 | `""` | — |
| [SRC-AC9D8384E8-L000029](../../tests/test_semantic_claim_verifier.py#L29) | 29 | `"def response(rows):"` | — |
| [SRC-AC9D8384E8-L000030](../../tests/test_semantic_claim_verifier.py#L30) | 30 | `"    return json.dumps({\"claims\": rows}, ensure_ascii=False)"` | — |
| [SRC-AC9D8384E8-L000031](../../tests/test_semantic_claim_verifier.py#L31) | 31 | `""` | — |
| [SRC-AC9D8384E8-L000032](../../tests/test_semantic_claim_verifier.py#L32) | 32 | `""` | — |
| [SRC-AC9D8384E8-L000033](../../tests/test_semantic_claim_verifier.py#L33) | 33 | `"def row(segment_id=\"S001\", assessment=\"supported\", supporting=None, contradicting=None):"` | — |
| [SRC-AC9D8384E8-L000034](../../tests/test_semantic_claim_verifier.py#L34) | 34 | `"    return {"` | — |
| [SRC-AC9D8384E8-L000035](../../tests/test_semantic_claim_verifier.py#L35) | 35 | `"        \"segment_id\": segment_id,"` | — |
| [SRC-AC9D8384E8-L000036](../../tests/test_semantic_claim_verifier.py#L36) | 36 | `"        \"assessment\": assessment,"` | — |
| [SRC-AC9D8384E8-L000037](../../tests/test_semantic_claim_verifier.py#L37) | 37 | `"        \"supporting_source_indexes\": [1] if supporting is None and assessment == \"supported\" else (supporting or []),"` | — |
| [SRC-AC9D8384E8-L000038](../../tests/test_semantic_claim_verifier.py#L38) | 38 | `"        \"contradicting_source_indexes\": contradicting or [],"` | — |
| [SRC-AC9D8384E8-L000039](../../tests/test_semantic_claim_verifier.py#L39) | 39 | `"    }"` | — |
| [SRC-AC9D8384E8-L000040](../../tests/test_semantic_claim_verifier.py#L40) | 40 | `""` | — |
| [SRC-AC9D8384E8-L000041](../../tests/test_semantic_claim_verifier.py#L41) | 41 | `""` | — |
| [SRC-AC9D8384E8-L000042](../../tests/test_semantic_claim_verifier.py#L42) | 42 | `"def prepared(answer=\"The system serves 12 facilities [source 1].\", sources=None):"` | — |
| [SRC-AC9D8384E8-L000043](../../tests/test_semantic_claim_verifier.py#L43) | 43 | `"    return build_semantic_verification_request("` | — |
| [SRC-AC9D8384E8-L000044](../../tests/test_semantic_claim_verifier.py#L44) | 44 | `"        \"How many facilities does the system serve?\","` | — |
| [SRC-AC9D8384E8-L000045](../../tests/test_semantic_claim_verifier.py#L45) | 45 | `"        answer,"` | — |
| [SRC-AC9D8384E8-L000046](../../tests/test_semantic_claim_verifier.py#L46) | 46 | `"        sources if sources is not None else [source()],"` | — |
| [SRC-AC9D8384E8-L000047](../../tests/test_semantic_claim_verifier.py#L47) | 47 | `"    )"` | — |
| [SRC-AC9D8384E8-L000048](../../tests/test_semantic_claim_verifier.py#L48) | 48 | `""` | — |
| [SRC-AC9D8384E8-L000049](../../tests/test_semantic_claim_verifier.py#L49) | 49 | `""` | — |
| [SRC-AC9D8384E8-L000050](../../tests/test_semantic_claim_verifier.py#L50) | 50 | `"def test_semantic_assessment_accepts_direct_support_from_exact_cited_source():"` | — |
| [SRC-AC9D8384E8-L000051](../../tests/test_semantic_claim_verifier.py#L51) | 51 | `"    request = prepared()"` | — |
| [SRC-AC9D8384E8-L000052](../../tests/test_semantic_claim_verifier.py#L52) | 52 | `"    result = parse_semantic_verification_response("` | — |
| [SRC-AC9D8384E8-L000053](../../tests/test_semantic_claim_verifier.py#L53) | 53 | `"        response([row()]), request"` | — |
| [SRC-AC9D8384E8-L000054](../../tests/test_semantic_claim_verifier.py#L54) | 54 | `"    )"` | — |
| [SRC-AC9D8384E8-L000055](../../tests/test_semantic_claim_verifier.py#L55) | 55 | `"    assert result[\"status\"] == \"completed_all_claims_supported\""` | — |
| [SRC-AC9D8384E8-L000056](../../tests/test_semantic_claim_verifier.py#L56) | 56 | `"    assert result[\"withhold_answer\"] is False"` | — |
| [SRC-AC9D8384E8-L000057](../../tests/test_semantic_claim_verifier.py#L57) | 57 | `"    assert result[\"factual_supported_count\"] == 1"` | — |
| [SRC-AC9D8384E8-L000058](../../tests/test_semantic_claim_verifier.py#L58) | 58 | `"    assert result[\"fact_correctness\"] == \"not_verified\""` | — |
| [SRC-AC9D8384E8-L000059](../../tests/test_semantic_claim_verifier.py#L59) | 59 | `""` | — |
| [SRC-AC9D8384E8-L000060](../../tests/test_semantic_claim_verifier.py#L60) | 60 | `""` | — |
| [SRC-AC9D8384E8-L000061](../../tests/test_semantic_claim_verifier.py#L61) | 61 | `"def test_support_from_uncited_source_is_rejected_even_when_source_is_readable():"` | — |
| [SRC-AC9D8384E8-L000062](../../tests/test_semantic_claim_verifier.py#L62) | 62 | `"    request = prepared("` | — |
| [SRC-AC9D8384E8-L000063](../../tests/test_semantic_claim_verifier.py#L63) | 63 | `"        answer=\"The system serves 12 facilities [source 2].\","` | — |
| [SRC-AC9D8384E8-L000064](../../tests/test_semantic_claim_verifier.py#L64) | 64 | `"        sources=[source(), source(url=\"https://example.net/report\")],"` | — |
| [SRC-AC9D8384E8-L000065](../../tests/test_semantic_claim_verifier.py#L65) | 65 | `"    )"` | — |
| [SRC-AC9D8384E8-L000066](../../tests/test_semantic_claim_verifier.py#L66) | 66 | `"    result = parse_semantic_verification_response(response([row()]), request)"` | — |
