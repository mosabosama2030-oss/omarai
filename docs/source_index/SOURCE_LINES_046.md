# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **046**
- سجلات الأسطر: **800**
- النطاق: SRC-96F6863E3C-L000070 إلى SRC-AC9D8384E8-L000009
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-96F6863E3C — [tests/test_research_pipeline.py](../../tests/test_research_pipeline.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-96F6863E3C-L000070](../../tests/test_research_pipeline.py#L70) | 70 | `"def test_optional_semantic_matcher_only_ranks_candidates_and_rejects_bad_scores():"` | — |
| [SRC-96F6863E3C-L000071](../../tests/test_research_pipeline.py#L71) | 71 | `"    calls = []"` | — |
| [SRC-96F6863E3C-L000072](../../tests/test_research_pipeline.py#L72) | 72 | `""` | — |
| [SRC-96F6863E3C-L000073](../../tests/test_research_pipeline.py#L73) | 73 | `"    def matcher(aspect, source):"` | — |
| [SRC-96F6863E3C-L000074](../../tests/test_research_pipeline.py#L74) | 74 | `"        calls.append((aspect, source.get(\"url\")))"` | — |
| [SRC-96F6863E3C-L000075](../../tests/test_research_pipeline.py#L75) | 75 | `"        return 0.9 if source.get(\"url\", \"\").endswith(\"/relevant\") else float(\"nan\")"` | — |
| [SRC-96F6863E3C-L000076](../../tests/test_research_pipeline.py#L76) | 76 | `""` | — |
| [SRC-96F6863E3C-L000077](../../tests/test_research_pipeline.py#L77) | 77 | `"    result = build_research_pipeline("` | — |
| [SRC-96F6863E3C-L000078](../../tests/test_research_pipeline.py#L78) | 78 | `"        \"ما سعر الهاتف ومدة الضمان؟\","` | — |
| [SRC-96F6863E3C-L000079](../../tests/test_research_pipeline.py#L79) | 79 | `"        {\"queries\": [\"الهاتف\"]},"` | — |
| [SRC-96F6863E3C-L000080](../../tests/test_research_pipeline.py#L80) | 80 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-96F6863E3C-L000081](../../tests/test_research_pipeline.py#L81) | 81 | `"        sources=["` | — |
| [SRC-96F6863E3C-L000082](../../tests/test_research_pipeline.py#L82) | 82 | `"            {\"title\": \"سعر الهاتف\", \"url\": \"https://example.com/relevant\", \"snippet\": \"السعر\"},"` | — |
| [SRC-96F6863E3C-L000083](../../tests/test_research_pipeline.py#L83) | 83 | `"            {\"title\": \"صفحة أخرى\", \"url\": \"https://example.com/other\", \"snippet\": \"عام\"},"` | — |
| [SRC-96F6863E3C-L000084](../../tests/test_research_pipeline.py#L84) | 84 | `"        ],"` | — |
| [SRC-96F6863E3C-L000085](../../tests/test_research_pipeline.py#L85) | 85 | `"        semantic_matcher=matcher,"` | — |
| [SRC-96F6863E3C-L000086](../../tests/test_research_pipeline.py#L86) | 86 | `"    )"` | — |
| [SRC-96F6863E3C-L000087](../../tests/test_research_pipeline.py#L87) | 87 | `""` | — |
| [SRC-96F6863E3C-L000088](../../tests/test_research_pipeline.py#L88) | 88 | `"    assert result[\"evidence\"][\"semantic_matching\"][\"status\"] == \"evaluated\""` | — |
| [SRC-96F6863E3C-L000089](../../tests/test_research_pipeline.py#L89) | 89 | `"    assert len(calls) == len(result[\"aspects\"]) * 2"` | — |
| [SRC-96F6863E3C-L000090](../../tests/test_research_pipeline.py#L90) | 90 | `"    for candidates in result[\"evidence\"][\"semantic_matching\"][\"candidates\"].values():"` | — |
| [SRC-96F6863E3C-L000091](../../tests/test_research_pipeline.py#L91) | 91 | `"        assert all(0.0 <= item[\"score\"] <= 1.0 for item in candidates)"` | — |
| [SRC-96F6863E3C-L000092](../../tests/test_research_pipeline.py#L92) | 92 | `"    # A semantic relevance score never promotes an aspect into the lexical evidence ledger."` | — |
| [SRC-96F6863E3C-L000093](../../tests/test_research_pipeline.py#L93) | 93 | `"    assert result[\"evidence\"][\"lexical_ledger\"][\"covered\"] != result[\"aspects\"]"` | — |
| [SRC-96F6863E3C-L000094](../../tests/test_research_pipeline.py#L94) | 94 | `""` | — |
| [SRC-96F6863E3C-L000095](../../tests/test_research_pipeline.py#L95) | 95 | `""` | — |
| [SRC-96F6863E3C-L000096](../../tests/test_research_pipeline.py#L96) | 96 | `"def test_fallback_plan_exposes_same_unified_pipeline_contract():"` | — |
| [SRC-96F6863E3C-L000097](../../tests/test_research_pipeline.py#L97) | 97 | `"    from agents.research import fallback_plan"` | — |
| [SRC-96F6863E3C-L000098](../../tests/test_research_pipeline.py#L98) | 98 | `""` | — |
| [SRC-96F6863E3C-L000099](../../tests/test_research_pipeline.py#L99) | 99 | `"    plan = fallback_plan(\"حلل السيارات الكهربائية في مصر من حيث السعر والضمان\")"` | — |
| [SRC-96F6863E3C-L000100](../../tests/test_research_pipeline.py#L100) | 100 | `""` | — |
| [SRC-96F6863E3C-L000101](../../tests/test_research_pipeline.py#L101) | 101 | `"    assert plan[\"research_pipeline\"][\"aspects\"]"` | — |
| [SRC-96F6863E3C-L000102](../../tests/test_research_pipeline.py#L102) | 102 | `"    assert plan[\"research_pipeline\"][\"stages\"][\"query_planning\"] == \"completed\""` | — |
| [SRC-96F6863E3C-L000103](../../tests/test_research_pipeline.py#L103) | 103 | `"    assert plan[\"query_strategy_matrix\"]"` | — |
| [SRC-96F6863E3C-L000104](../../tests/test_research_pipeline.py#L104) | 104 | `""` | — |
| [SRC-96F6863E3C-L000105](../../tests/test_research_pipeline.py#L105) | 105 | `""` | — |
| [SRC-96F6863E3C-L000106](../../tests/test_research_pipeline.py#L106) | 106 | `"def test_semantic_matcher_failure_is_degraded_without_aborting_pipeline():"` | — |
| [SRC-96F6863E3C-L000107](../../tests/test_research_pipeline.py#L107) | 107 | `"    result = build_research_pipeline("` | — |
| [SRC-96F6863E3C-L000108](../../tests/test_research_pipeline.py#L108) | 108 | `"        \"ما سعر الهاتف ومدة الضمان؟\","` | — |
| [SRC-96F6863E3C-L000109](../../tests/test_research_pipeline.py#L109) | 109 | `"        {\"queries\": [\"الهاتف\"]},"` | — |
| [SRC-96F6863E3C-L000110](../../tests/test_research_pipeline.py#L110) | 110 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-96F6863E3C-L000111](../../tests/test_research_pipeline.py#L111) | 111 | `"        sources=[{\"title\": \"سعر الهاتف\", \"url\": \"https://example.com\"}],"` | — |
| [SRC-96F6863E3C-L000112](../../tests/test_research_pipeline.py#L112) | 112 | `"        semantic_matcher=lambda _aspect, _source: (_ for _ in ()).throw(RuntimeError(\"model timeout\")),"` | — |
| [SRC-96F6863E3C-L000113](../../tests/test_research_pipeline.py#L113) | 113 | `"    )"` | — |
| [SRC-96F6863E3C-L000114](../../tests/test_research_pipeline.py#L114) | 114 | `""` | — |
| [SRC-96F6863E3C-L000115](../../tests/test_research_pipeline.py#L115) | 115 | `"    assert result[\"stages\"][\"semantic_matching\"] == \"degraded\""` | — |
| [SRC-96F6863E3C-L000116](../../tests/test_research_pipeline.py#L116) | 116 | `"    assert result[\"evidence\"][\"semantic_matching\"][\"errors\"] == len(result[\"aspects\"])"` | — |
| [SRC-96F6863E3C-L000117](../../tests/test_research_pipeline.py#L117) | 117 | `"    assert result[\"evidence\"][\"lexical_ledger\"][\"aspects\"] == result[\"aspects\"]"` | — |
| [SRC-96F6863E3C-L000118](../../tests/test_research_pipeline.py#L118) | 118 | `""` | — |
| [SRC-96F6863E3C-L000119](../../tests/test_research_pipeline.py#L119) | 119 | `""` | — |
| [SRC-96F6863E3C-L000120](../../tests/test_research_pipeline.py#L120) | 120 | `""` | — |
| [SRC-96F6863E3C-L000121](../../tests/test_research_pipeline.py#L121) | 121 | `"def test_pipeline_preserves_planner_depth_and_freshness_metadata():"` | — |
| [SRC-96F6863E3C-L000122](../../tests/test_research_pipeline.py#L122) | 122 | `"    result = build_research_pipeline("` | — |
| [SRC-96F6863E3C-L000123](../../tests/test_research_pipeline.py#L123) | 123 | `"        \"قارن السيارات الكهربائية في مصر من حيث السعر والبطارية\","` | — |
| [SRC-96F6863E3C-L000124](../../tests/test_research_pipeline.py#L124) | 124 | `"        {"` | — |
| [SRC-96F6863E3C-L000125](../../tests/test_research_pipeline.py#L125) | 125 | `"            \"queries\": [\"السيارات الكهربائية في مصر\"],"` | — |
| [SRC-96F6863E3C-L000126](../../tests/test_research_pipeline.py#L126) | 126 | `"            \"depth\": \"deep\","` | — |
| [SRC-96F6863E3C-L000127](../../tests/test_research_pipeline.py#L127) | 127 | `"            \"freshness\": \"current\","` | — |
| [SRC-96F6863E3C-L000128](../../tests/test_research_pipeline.py#L128) | 128 | `"        },"` | — |
| [SRC-96F6863E3C-L000129](../../tests/test_research_pipeline.py#L129) | 129 | `"        mode=\"deep\","` | — |
| [SRC-96F6863E3C-L000130](../../tests/test_research_pipeline.py#L130) | 130 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-96F6863E3C-L000131](../../tests/test_research_pipeline.py#L131) | 131 | `"    )"` | — |
| [SRC-96F6863E3C-L000132](../../tests/test_research_pipeline.py#L132) | 132 | `""` | — |
| [SRC-96F6863E3C-L000133](../../tests/test_research_pipeline.py#L133) | 133 | `"    assert result[\"task_spec\"][\"planner_depth\"] == \"deep\""` | — |
| [SRC-96F6863E3C-L000134](../../tests/test_research_pipeline.py#L134) | 134 | `"    assert result[\"task_spec\"][\"planner_freshness\"] == \"current\""` | — |
| [SRC-96F6863E3C-L000135](../../tests/test_research_pipeline.py#L135) | 135 | `""` | — |
| [SRC-96F6863E3C-L000136](../../tests/test_research_pipeline.py#L136) | 136 | `""` | — |
| [SRC-96F6863E3C-L000137](../../tests/test_research_pipeline.py#L137) | 137 | `"def test_pipeline_blocks_official_site_search_when_target_entity_is_missing():"` | — |
| [SRC-96F6863E3C-L000138](../../tests/test_research_pipeline.py#L138) | 138 | `"    result = build_research_pipeline("` | — |
| [SRC-96F6863E3C-L000139](../../tests/test_research_pipeline.py#L139) | 139 | `"        \"هات الموقع الرسمي\","` | — |
| [SRC-96F6863E3C-L000140](../../tests/test_research_pipeline.py#L140) | 140 | `"        {\"queries\": [\"الموقع الرسمي\"]},"` | — |
| [SRC-96F6863E3C-L000141](../../tests/test_research_pipeline.py#L141) | 141 | `"        intent_route=\"WEB_SIMPLE\","` | — |
| [SRC-96F6863E3C-L000142](../../tests/test_research_pipeline.py#L142) | 142 | `"    )"` | — |
| [SRC-96F6863E3C-L000143](../../tests/test_research_pipeline.py#L143) | 143 | `""` | — |
| [SRC-96F6863E3C-L000144](../../tests/test_research_pipeline.py#L144) | 144 | `"    assert result[\"task_spec\"][\"requires_clarification\"] is True"` | — |
| [SRC-96F6863E3C-L000145](../../tests/test_research_pipeline.py#L145) | 145 | `"    assert result[\"intent\"][\"needs_clarification\"] is True"` | — |
| [SRC-96F6863E3C-L000146](../../tests/test_research_pipeline.py#L146) | 146 | `"    assert result[\"queries\"] == []"` | — |
| [SRC-96F6863E3C-L000147](../../tests/test_research_pipeline.py#L147) | 147 | `"    assert result[\"stages\"][\"query_planning\"] == \"blocked_pending_clarification\""` | — |
| [SRC-96F6863E3C-L000148](../../tests/test_research_pipeline.py#L148) | 148 | `""` | — |
| [SRC-96F6863E3C-L000149](../../tests/test_research_pipeline.py#L149) | 149 | `"def test_pipeline_marks_upstream_dialogue_context_resolution_as_completed():"` | — |
| [SRC-96F6863E3C-L000150](../../tests/test_research_pipeline.py#L150) | 150 | `"    result = build_research_pipeline("` | — |
| [SRC-96F6863E3C-L000151](../../tests/test_research_pipeline.py#L151) | 151 | `"        \"والضمان؟\","` | — |
| [SRC-96F6863E3C-L000152](../../tests/test_research_pipeline.py#L152) | 152 | `"        {\"queries\": [\"iPhone 17 warranty Egypt\"]},"` | — |
| [SRC-96F6863E3C-L000153](../../tests/test_research_pipeline.py#L153) | 153 | `"        intent_route=\"WEB_SIMPLE\","` | — |
| [SRC-96F6863E3C-L000154](../../tests/test_research_pipeline.py#L154) | 154 | `"        dialogue_context={"` | — |
| [SRC-96F6863E3C-L000155](../../tests/test_research_pipeline.py#L155) | 155 | `"            \"method\": \"llm_semantic_context\","` | — |
| [SRC-96F6863E3C-L000156](../../tests/test_research_pipeline.py#L156) | 156 | `"            \"resolved_question\": \"ما ضمان iPhone 17 في مصر؟\","` | — |
| [SRC-96F6863E3C-L000157](../../tests/test_research_pipeline.py#L157) | 157 | `"            \"topic\": \"iPhone 17\","` | — |
| [SRC-96F6863E3C-L000158](../../tests/test_research_pipeline.py#L158) | 158 | `"            \"is_follow_up\": True,"` | — |
| [SRC-96F6863E3C-L000159](../../tests/test_research_pipeline.py#L159) | 159 | `"            \"topic_shift\": False,"` | — |
| [SRC-96F6863E3C-L000160](../../tests/test_research_pipeline.py#L160) | 160 | `"        },"` | — |
| [SRC-96F6863E3C-L000161](../../tests/test_research_pipeline.py#L161) | 161 | `"    )"` | — |
| [SRC-96F6863E3C-L000162](../../tests/test_research_pipeline.py#L162) | 162 | `""` | — |
| [SRC-96F6863E3C-L000163](../../tests/test_research_pipeline.py#L163) | 163 | `"    assert result[\"contextual_question\"] == \"ما ضمان iPhone 17 في مصر؟\""` | — |
| [SRC-96F6863E3C-L000164](../../tests/test_research_pipeline.py#L164) | 164 | `"    assert result[\"task_spec\"][\"context_resolution\"][\"resolved_question\"] == ("` | — |
| [SRC-96F6863E3C-L000165](../../tests/test_research_pipeline.py#L165) | 165 | `"        \"ما ضمان iPhone 17 في مصر؟\""` | — |
| [SRC-96F6863E3C-L000166](../../tests/test_research_pipeline.py#L166) | 166 | `"    )"` | — |
| [SRC-96F6863E3C-L000167](../../tests/test_research_pipeline.py#L167) | 167 | `"    assert result[\"stages\"][\"context_resolution\"] == \"completed\""` | — |
| [SRC-96F6863E3C-L000168](../../tests/test_research_pipeline.py#L168) | 168 | `"    assert result[\"intent\"][\"context_available\"] is True"` | — |
| [SRC-96F6863E3C-L000169](../../tests/test_research_pipeline.py#L169) | 169 | `"    assert result[\"query_strategy_matrix\"]"` | — |
| [SRC-96F6863E3C-L000170](../../tests/test_research_pipeline.py#L170) | 170 | `"    assert all(\"iPhone 17\" in item[\"query\"] for item in result[\"query_strategy_matrix\"])"` | — |
| [SRC-96F6863E3C-L000171](../../tests/test_research_pipeline.py#L171) | 171 | `""` | — |
| [SRC-96F6863E3C-L000172](../../tests/test_research_pipeline.py#L172) | 172 | `"def test_pipeline_does_not_reuse_resolved_question_after_explicit_topic_shift():"` | — |
| [SRC-96F6863E3C-L000173](../../tests/test_research_pipeline.py#L173) | 173 | `"    result = build_research_pipeline("` | — |
| [SRC-96F6863E3C-L000174](../../tests/test_research_pipeline.py#L174) | 174 | `"        \"ما سعر سامسونج S26؟\","` | — |
| [SRC-96F6863E3C-L000175](../../tests/test_research_pipeline.py#L175) | 175 | `"        {\"queries\": [\"سعر سامسونج S26\"]},"` | — |
| [SRC-96F6863E3C-L000176](../../tests/test_research_pipeline.py#L176) | 176 | `"        intent_route=\"WEB_SIMPLE\","` | — |
| [SRC-96F6863E3C-L000177](../../tests/test_research_pipeline.py#L177) | 177 | `"        dialogue_context={"` | — |
| [SRC-96F6863E3C-L000178](../../tests/test_research_pipeline.py#L178) | 178 | `"            \"resolved_question\": \"ما ضمان iPhone 17 في مصر؟\","` | — |
| [SRC-96F6863E3C-L000179](../../tests/test_research_pipeline.py#L179) | 179 | `"            \"topic_shift\": True,"` | — |
| [SRC-96F6863E3C-L000180](../../tests/test_research_pipeline.py#L180) | 180 | `"        },"` | — |
| [SRC-96F6863E3C-L000181](../../tests/test_research_pipeline.py#L181) | 181 | `"    )"` | — |
| [SRC-96F6863E3C-L000182](../../tests/test_research_pipeline.py#L182) | 182 | `""` | — |
| [SRC-96F6863E3C-L000183](../../tests/test_research_pipeline.py#L183) | 183 | `"    assert result[\"contextual_question\"] == \"ما سعر سامسونج S26؟\""` | — |
| [SRC-96F6863E3C-L000184](../../tests/test_research_pipeline.py#L184) | 184 | `"    assert result[\"task_spec\"][\"context_resolution\"][\"resolved_question\"] == ("` | — |
| [SRC-96F6863E3C-L000185](../../tests/test_research_pipeline.py#L185) | 185 | `"        \"ما سعر سامسونج S26؟\""` | — |
| [SRC-96F6863E3C-L000186](../../tests/test_research_pipeline.py#L186) | 186 | `"    )"` | — |
| [SRC-96F6863E3C-L000187](../../tests/test_research_pipeline.py#L187) | 187 | `""` | — |
| [SRC-96F6863E3C-L000188](../../tests/test_research_pipeline.py#L188) | 188 | `"def test_pipeline_does_not_claim_context_resolution_for_unstructured_metadata():"` | — |
| [SRC-96F6863E3C-L000189](../../tests/test_research_pipeline.py#L189) | 189 | `"    result = build_research_pipeline("` | — |
| [SRC-96F6863E3C-L000190](../../tests/test_research_pipeline.py#L190) | 190 | `"        \"ما سعر الهاتف؟\","` | — |
| [SRC-96F6863E3C-L000191](../../tests/test_research_pipeline.py#L191) | 191 | `"        {\"queries\": [\"سعر الهاتف\"]},"` | — |
| [SRC-96F6863E3C-L000192](../../tests/test_research_pipeline.py#L192) | 192 | `"        intent_route=\"WEB_SIMPLE\","` | — |
| [SRC-96F6863E3C-L000193](../../tests/test_research_pipeline.py#L193) | 193 | `"        dialogue_context={\"trace_label\": \"upstream_metadata_only\"},"` | — |
| [SRC-96F6863E3C-L000194](../../tests/test_research_pipeline.py#L194) | 194 | `"    )"` | — |
| [SRC-96F6863E3C-L000195](../../tests/test_research_pipeline.py#L195) | 195 | `""` | — |
| [SRC-96F6863E3C-L000196](../../tests/test_research_pipeline.py#L196) | 196 | `"    assert result[\"stages\"][\"context_resolution\"] == \"not_needed\""` | — |
| [SRC-96F6863E3C-L000197](../../tests/test_research_pipeline.py#L197) | 197 | `""` | — |
| [SRC-96F6863E3C-L000198](../../tests/test_research_pipeline.py#L198) | 198 | `"def test_pipeline_does_not_claim_lexical_matching_without_readable_source_text():"` | — |
| [SRC-96F6863E3C-L000199](../../tests/test_research_pipeline.py#L199) | 199 | `"    for sources in ("` | — |
| [SRC-96F6863E3C-L000200](../../tests/test_research_pipeline.py#L200) | 200 | `"        [None, \"not-a-source\", {}],"` | — |
| [SRC-96F6863E3C-L000201](../../tests/test_research_pipeline.py#L201) | 201 | `"        [{\"url\": \"https://example.com/no-text\"}],"` | — |
| [SRC-96F6863E3C-L000202](../../tests/test_research_pipeline.py#L202) | 202 | `"        [],"` | — |
| [SRC-96F6863E3C-L000203](../../tests/test_research_pipeline.py#L203) | 203 | `"    ):"` | — |
| [SRC-96F6863E3C-L000204](../../tests/test_research_pipeline.py#L204) | 204 | `"        result = build_research_pipeline("` | — |
| [SRC-96F6863E3C-L000205](../../tests/test_research_pipeline.py#L205) | 205 | `"            \"ما سعر الهاتف والضمان؟\","` | — |
| [SRC-96F6863E3C-L000206](../../tests/test_research_pipeline.py#L206) | 206 | `"            {\"queries\": [\"سعر الهاتف والضمان\"]},"` | — |
| [SRC-96F6863E3C-L000207](../../tests/test_research_pipeline.py#L207) | 207 | `"            intent_route=\"WEB_SIMPLE\","` | — |
| [SRC-96F6863E3C-L000208](../../tests/test_research_pipeline.py#L208) | 208 | `"            sources=sources,"` | — |
| [SRC-96F6863E3C-L000209](../../tests/test_research_pipeline.py#L209) | 209 | `"        )"` | — |
| [SRC-96F6863E3C-L000210](../../tests/test_research_pipeline.py#L210) | 210 | `""` | — |
| [SRC-96F6863E3C-L000211](../../tests/test_research_pipeline.py#L211) | 211 | `"        assert result[\"stages\"][\"lexical_matching\"] == \"not_assessed\""` | — |
| [SRC-96F6863E3C-L000212](../../tests/test_research_pipeline.py#L212) | 212 | `"        assert result[\"evidence_ledger\"][\"covered\"] == []"` | — |
## اختبارات

### FILE-2822F30DAD — [tests/test_sales_domain.py](../../tests/test_sales_domain.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-2822F30DAD-L000001](../../tests/test_sales_domain.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-2822F30DAD-L000002](../../tests/test_sales_domain.py#L2) | 2 | `""` | — |
| [SRC-2822F30DAD-L000003](../../tests/test_sales_domain.py#L3) | 3 | `"import pytest"` | — |
| [SRC-2822F30DAD-L000004](../../tests/test_sales_domain.py#L4) | 4 | `""` | — |
| [SRC-2822F30DAD-L000005](../../tests/test_sales_domain.py#L5) | 5 | `"from agents.sales_domain import ("` | — |
| [SRC-2822F30DAD-L000006](../../tests/test_sales_domain.py#L6) | 6 | `"    ContactabilityStatus,"` | — |
| [SRC-2822F30DAD-L000007](../../tests/test_sales_domain.py#L7) | 7 | `"    DemandEvidence,"` | — |
| [SRC-2822F30DAD-L000008](../../tests/test_sales_domain.py#L8) | 8 | `"    DemandSignal,"` | — |
| [SRC-2822F30DAD-L000009](../../tests/test_sales_domain.py#L9) | 9 | `"    DemandSignalType,"` | — |
| [SRC-2822F30DAD-L000010](../../tests/test_sales_domain.py#L10) | 10 | `"    EvidenceBasis,"` | — |
| [SRC-2822F30DAD-L000011](../../tests/test_sales_domain.py#L11) | 11 | `"    FactOrigin,"` | — |
| [SRC-2822F30DAD-L000012](../../tests/test_sales_domain.py#L12) | 12 | `"    FreshnessStatus,"` | — |
| [SRC-2822F30DAD-L000013](../../tests/test_sales_domain.py#L13) | 13 | `"    IdentityStatus,"` | — |
| [SRC-2822F30DAD-L000014](../../tests/test_sales_domain.py#L14) | 14 | `"    LeadQualification,"` | — |
| [SRC-2822F30DAD-L000015](../../tests/test_sales_domain.py#L15) | 15 | `"    MarketProfile,"` | — |
| [SRC-2822F30DAD-L000016](../../tests/test_sales_domain.py#L16) | 16 | `"    ProductFact,"` | — |
| [SRC-2822F30DAD-L000017](../../tests/test_sales_domain.py#L17) | 17 | `"    ProductFit,"` | — |
| [SRC-2822F30DAD-L000018](../../tests/test_sales_domain.py#L18) | 18 | `"    ProductProfile,"` | — |
| [SRC-2822F30DAD-L000019](../../tests/test_sales_domain.py#L19) | 19 | `"    ProductTaxonomy,"` | — |
| [SRC-2822F30DAD-L000020](../../tests/test_sales_domain.py#L20) | 20 | `"    SourceQuality,"` | — |
| [SRC-2822F30DAD-L000021](../../tests/test_sales_domain.py#L21) | 21 | `"    TaxonomyCategory,"` | — |
| [SRC-2822F30DAD-L000022](../../tests/test_sales_domain.py#L22) | 22 | `"    normalize_text,"` | — |
| [SRC-2822F30DAD-L000023](../../tests/test_sales_domain.py#L23) | 23 | `"    to_json_dict,"` | — |
| [SRC-2822F30DAD-L000024](../../tests/test_sales_domain.py#L24) | 24 | `")"` | — |
| [SRC-2822F30DAD-L000025](../../tests/test_sales_domain.py#L25) | 25 | `""` | — |
| [SRC-2822F30DAD-L000026](../../tests/test_sales_domain.py#L26) | 26 | `""` | — |
| [SRC-2822F30DAD-L000027](../../tests/test_sales_domain.py#L27) | 27 | `"def page_evidence(**overrides):"` | — |
| [SRC-2822F30DAD-L000028](../../tests/test_sales_domain.py#L28) | 28 | `"    values = {"` | — |
| [SRC-2822F30DAD-L000029](../../tests/test_sales_domain.py#L29) | 29 | `"        \"source_id\": \"source-1\","` | — |
| [SRC-2822F30DAD-L000030](../../tests/test_sales_domain.py#L30) | 30 | `"        \"source_url\": \"https://example.org/public-post/1\","` | — |
| [SRC-2822F30DAD-L000031](../../tests/test_sales_domain.py#L31) | 31 | `"        \"excerpt\": \"I am looking to buy a commercial fire alarm system.\","` | — |
| [SRC-2822F30DAD-L000032](../../tests/test_sales_domain.py#L32) | 32 | `"        \"content_basis\": EvidenceBasis.PAGE_TEXT,"` | — |
| [SRC-2822F30DAD-L000033](../../tests/test_sales_domain.py#L33) | 33 | `"        \"publication_date\": \"2026-10-20\","` | — |
| [SRC-2822F30DAD-L000034](../../tests/test_sales_domain.py#L34) | 34 | `"        \"event_date\": None,"` | — |
| [SRC-2822F30DAD-L000035](../../tests/test_sales_domain.py#L35) | 35 | `"        \"observed_at\": \"2026-10-31T08:00:00Z\","` | — |
| [SRC-2822F30DAD-L000036](../../tests/test_sales_domain.py#L36) | 36 | `"        \"page_read\": True,"` | — |
| [SRC-2822F30DAD-L000037](../../tests/test_sales_domain.py#L37) | 37 | `"    }"` | — |
| [SRC-2822F30DAD-L000038](../../tests/test_sales_domain.py#L38) | 38 | `"    values.update(overrides)"` | — |
| [SRC-2822F30DAD-L000039](../../tests/test_sales_domain.py#L39) | 39 | `"    return DemandEvidence(**values)"` | — |
| [SRC-2822F30DAD-L000040](../../tests/test_sales_domain.py#L40) | 40 | `""` | — |
| [SRC-2822F30DAD-L000041](../../tests/test_sales_domain.py#L41) | 41 | `""` | — |
| [SRC-2822F30DAD-L000042](../../tests/test_sales_domain.py#L42) | 42 | `"def test_normalize_text_handles_arabic_and_latin_without_changing_display_value():"` | — |
| [SRC-2822F30DAD-L000043](../../tests/test_sales_domain.py#L43) | 43 | `"    assert normalize_text(\"إِنذار الحَرِيق\") == \"انذار الحريق\""` | — |
| [SRC-2822F30DAD-L000044](../../tests/test_sales_domain.py#L44) | 44 | `"    assert normalize_text(\"Café, FIRE-ALARM\") == \"café fire-alarm\""` | — |
| [SRC-2822F30DAD-L000045](../../tests/test_sales_domain.py#L45) | 45 | `""` | — |
| [SRC-2822F30DAD-L000046](../../tests/test_sales_domain.py#L46) | 46 | `""` | — |
| [SRC-2822F30DAD-L000047](../../tests/test_sales_domain.py#L47) | 47 | `"def test_product_profile_requires_a_name_and_deduplicates_aliases():"` | — |
| [SRC-2822F30DAD-L000048](../../tests/test_sales_domain.py#L48) | 48 | `"    with pytest.raises(ValueError, match=\"name is required\"):"` | — |
| [SRC-2822F30DAD-L000049](../../tests/test_sales_domain.py#L49) | 49 | `"        ProductProfile(name=\" \")"` | — |
| [SRC-2822F30DAD-L000050](../../tests/test_sales_domain.py#L50) | 50 | `""` | — |
| [SRC-2822F30DAD-L000051](../../tests/test_sales_domain.py#L51) | 51 | `"    profile = ProductProfile("` | — |
| [SRC-2822F30DAD-L000052](../../tests/test_sales_domain.py#L52) | 52 | `"        name=\"Fire Alarm Panel\","` | — |
| [SRC-2822F30DAD-L000053](../../tests/test_sales_domain.py#L53) | 53 | `"        aliases=(\"لوحة إنذار\", \"لوحه انذار\", \"FACP\"),"` | — |
| [SRC-2822F30DAD-L000054](../../tests/test_sales_domain.py#L54) | 54 | `"    )"` | — |
| [SRC-2822F30DAD-L000055](../../tests/test_sales_domain.py#L55) | 55 | `""` | — |
| [SRC-2822F30DAD-L000056](../../tests/test_sales_domain.py#L56) | 56 | `"    assert profile.aliases == (\"لوحة إنذار\", \"FACP\")"` | — |
| [SRC-2822F30DAD-L000057](../../tests/test_sales_domain.py#L57) | 57 | `""` | — |
| [SRC-2822F30DAD-L000058](../../tests/test_sales_domain.py#L58) | 58 | `""` | — |
| [SRC-2822F30DAD-L000059](../../tests/test_sales_domain.py#L59) | 59 | `"def test_product_matching_uses_only_explicit_product_terms():"` | — |
| [SRC-2822F30DAD-L000060](../../tests/test_sales_domain.py#L60) | 60 | `"    profile = ProductProfile("` | — |
| [SRC-2822F30DAD-L000061](../../tests/test_sales_domain.py#L61) | 61 | `"        name=\"Fire Alarm Panel\","` | — |
| [SRC-2822F30DAD-L000062](../../tests/test_sales_domain.py#L62) | 62 | `"        aliases=(\"لوحة إنذار الحريق\", \"FACP\"),"` | — |
| [SRC-2822F30DAD-L000063](../../tests/test_sales_domain.py#L63) | 63 | `"    )"` | — |
| [SRC-2822F30DAD-L000064](../../tests/test_sales_domain.py#L64) | 64 | `""` | — |
| [SRC-2822F30DAD-L000065](../../tests/test_sales_domain.py#L65) | 65 | `"    assert profile.matching_terms(\"We need a FACP for a new building.\") == (\"FACP\",)"` | — |
| [SRC-2822F30DAD-L000066](../../tests/test_sales_domain.py#L66) | 66 | `"    assert profile.matching_terms(\"نحتاج لوحة إنذار الحريق للمشروع\") == (\"لوحة إنذار الحريق\",)"` | — |
| [SRC-2822F30DAD-L000067](../../tests/test_sales_domain.py#L67) | 67 | `"    assert profile.matching_terms(\"We need a fire alarm system.\") == ()"` | — |
| [SRC-2822F30DAD-L000068](../../tests/test_sales_domain.py#L68) | 68 | `""` | — |
| [SRC-2822F30DAD-L000069](../../tests/test_sales_domain.py#L69) | 69 | `""` | — |
| [SRC-2822F30DAD-L000070](../../tests/test_sales_domain.py#L70) | 70 | `"def test_product_mention_does_not_create_demand_or_product_fit():"` | — |
| [SRC-2822F30DAD-L000071](../../tests/test_sales_domain.py#L71) | 71 | `"    profile = ProductProfile("` | — |
| [SRC-2822F30DAD-L000072](../../tests/test_sales_domain.py#L72) | 72 | `"        name=\"Fire Alarm Panel\","` | — |
| [SRC-2822F30DAD-L000073](../../tests/test_sales_domain.py#L73) | 73 | `"        aliases=(\"Fire Alarm Panels\",),"` | — |
| [SRC-2822F30DAD-L000074](../../tests/test_sales_domain.py#L74) | 74 | `"    )"` | — |
| [SRC-2822F30DAD-L000075](../../tests/test_sales_domain.py#L75) | 75 | `"    assert profile.matching_terms(\"The company sells Fire Alarm Panels.\") == (\"Fire Alarm Panels\",)"` | — |
| [SRC-2822F30DAD-L000076](../../tests/test_sales_domain.py#L76) | 76 | `""` | — |
| [SRC-2822F30DAD-L000077](../../tests/test_sales_domain.py#L77) | 77 | `"    signal = DemandSignal("` | — |
| [SRC-2822F30DAD-L000078](../../tests/test_sales_domain.py#L78) | 78 | `"        signal_id=\"signal-1\","` | — |
| [SRC-2822F30DAD-L000079](../../tests/test_sales_domain.py#L79) | 79 | `"        signal_type=DemandSignalType.UNKNOWN,"` | — |
| [SRC-2822F30DAD-L000080](../../tests/test_sales_domain.py#L80) | 80 | `"        evidence=page_evidence(),"` | — |
| [SRC-2822F30DAD-L000081](../../tests/test_sales_domain.py#L81) | 81 | `"    )"` | — |
| [SRC-2822F30DAD-L000082](../../tests/test_sales_domain.py#L82) | 82 | `""` | — |
| [SRC-2822F30DAD-L000083](../../tests/test_sales_domain.py#L83) | 83 | `"    assert signal.signal_type == DemandSignalType.UNKNOWN"` | — |
| [SRC-2822F30DAD-L000084](../../tests/test_sales_domain.py#L84) | 84 | `"    assert signal.product_fit == ProductFit.UNASSESSED"` | — |
| [SRC-2822F30DAD-L000085](../../tests/test_sales_domain.py#L85) | 85 | `""` | — |
| [SRC-2822F30DAD-L000086](../../tests/test_sales_domain.py#L86) | 86 | `""` | — |
| [SRC-2822F30DAD-L000087](../../tests/test_sales_domain.py#L87) | 87 | `"def test_product_taxonomy_is_caller_defined_and_supports_multiple_sectors():"` | — |
| [SRC-2822F30DAD-L000088](../../tests/test_sales_domain.py#L88) | 88 | `"    taxonomy = ProductTaxonomy("` | — |
| [SRC-2822F30DAD-L000089](../../tests/test_sales_domain.py#L89) | 89 | `"        categories=("` | — |
| [SRC-2822F30DAD-L000090](../../tests/test_sales_domain.py#L90) | 90 | `"            TaxonomyCategory("` | — |
| [SRC-2822F30DAD-L000091](../../tests/test_sales_domain.py#L91) | 91 | `"                path=(\"safety\", \"fire_detection\"),"` | — |
| [SRC-2822F30DAD-L000092](../../tests/test_sales_domain.py#L92) | 92 | `"                aliases=(\"fire alarm\", \"إنذار حريق\"),"` | — |
| [SRC-2822F30DAD-L000093](../../tests/test_sales_domain.py#L93) | 93 | `"            ),"` | — |
| [SRC-2822F30DAD-L000094](../../tests/test_sales_domain.py#L94) | 94 | `"            TaxonomyCategory("` | — |
| [SRC-2822F30DAD-L000095](../../tests/test_sales_domain.py#L95) | 95 | `"                path=(\"mobility\", \"vehicles\"),"` | — |
| [SRC-2822F30DAD-L000096](../../tests/test_sales_domain.py#L96) | 96 | `"                aliases=(\"vehicle\", \"سيارة\"),"` | — |
| [SRC-2822F30DAD-L000097](../../tests/test_sales_domain.py#L97) | 97 | `"            ),"` | — |
| [SRC-2822F30DAD-L000098](../../tests/test_sales_domain.py#L98) | 98 | `"            TaxonomyCategory("` | — |
| [SRC-2822F30DAD-L000099](../../tests/test_sales_domain.py#L99) | 99 | `"                path=(\"construction\", \"residential_property\"),"` | — |
| [SRC-2822F30DAD-L000100](../../tests/test_sales_domain.py#L100) | 100 | `"                aliases=(\"apartment\", \"شقة\"),"` | — |
| [SRC-2822F30DAD-L000101](../../tests/test_sales_domain.py#L101) | 101 | `"            ),"` | — |
| [SRC-2822F30DAD-L000102](../../tests/test_sales_domain.py#L102) | 102 | `"        )"` | — |
| [SRC-2822F30DAD-L000103](../../tests/test_sales_domain.py#L103) | 103 | `"    )"` | — |
| [SRC-2822F30DAD-L000104](../../tests/test_sales_domain.py#L104) | 104 | `""` | — |
| [SRC-2822F30DAD-L000105](../../tests/test_sales_domain.py#L105) | 105 | `"    assert taxonomy.match_categories(\"نبحث عن إنذار حريق للمصنع\") == ("` | — |
| [SRC-2822F30DAD-L000106](../../tests/test_sales_domain.py#L106) | 106 | `"        (\"safety\", \"fire_detection\"),"` | — |
| [SRC-2822F30DAD-L000107](../../tests/test_sales_domain.py#L107) | 107 | `"    )"` | — |
| [SRC-2822F30DAD-L000108](../../tests/test_sales_domain.py#L108) | 108 | `"    assert taxonomy.match_categories(\"vehicle and apartment\") == ("` | — |
| [SRC-2822F30DAD-L000109](../../tests/test_sales_domain.py#L109) | 109 | `"        (\"mobility\", \"vehicles\"),"` | — |
| [SRC-2822F30DAD-L000110](../../tests/test_sales_domain.py#L110) | 110 | `"        (\"construction\", \"residential_property\"),"` | — |
| [SRC-2822F30DAD-L000111](../../tests/test_sales_domain.py#L111) | 111 | `"    )"` | — |
| [SRC-2822F30DAD-L000112](../../tests/test_sales_domain.py#L112) | 112 | `"    assert taxonomy.match_categories(\"unknown equipment\") == ()"` | — |
| [SRC-2822F30DAD-L000113](../../tests/test_sales_domain.py#L113) | 113 | `""` | — |
| [SRC-2822F30DAD-L000114](../../tests/test_sales_domain.py#L114) | 114 | `""` | — |
| [SRC-2822F30DAD-L000115](../../tests/test_sales_domain.py#L115) | 115 | `"def test_taxonomy_does_not_match_partial_latin_words():"` | — |
| [SRC-2822F30DAD-L000116](../../tests/test_sales_domain.py#L116) | 116 | `"    taxonomy = ProductTaxonomy("` | — |
| [SRC-2822F30DAD-L000117](../../tests/test_sales_domain.py#L117) | 117 | `"        categories=("` | — |
| [SRC-2822F30DAD-L000118](../../tests/test_sales_domain.py#L118) | 118 | `"            TaxonomyCategory(path=(\"mobility\", \"cars\"), aliases=(\"car\",)),"` | — |
| [SRC-2822F30DAD-L000119](../../tests/test_sales_domain.py#L119) | 119 | `"        )"` | — |
| [SRC-2822F30DAD-L000120](../../tests/test_sales_domain.py#L120) | 120 | `"    )"` | — |
| [SRC-2822F30DAD-L000121](../../tests/test_sales_domain.py#L121) | 121 | `""` | — |
| [SRC-2822F30DAD-L000122](../../tests/test_sales_domain.py#L122) | 122 | `"    assert taxonomy.match_categories(\"carton packaging\") == ()"` | — |
| [SRC-2822F30DAD-L000123](../../tests/test_sales_domain.py#L123) | 123 | `"    assert taxonomy.match_categories(\"used car\") == ((\"mobility\", \"cars\"),)"` | — |
| [SRC-2822F30DAD-L000124](../../tests/test_sales_domain.py#L124) | 124 | `""` | — |
| [SRC-2822F30DAD-L000125](../../tests/test_sales_domain.py#L125) | 125 | `""` | — |
| [SRC-2822F30DAD-L000126](../../tests/test_sales_domain.py#L126) | 126 | `"def test_taxonomy_rejects_duplicate_paths():"` | — |
| [SRC-2822F30DAD-L000127](../../tests/test_sales_domain.py#L127) | 127 | `"    first = TaxonomyCategory(path=(\"industry\", \"equipment\"), aliases=(\"machine\",))"` | — |
| [SRC-2822F30DAD-L000128](../../tests/test_sales_domain.py#L128) | 128 | `"    second = TaxonomyCategory(path=(\"industry\", \"equipment\"), aliases=(\"device\",))"` | — |
| [SRC-2822F30DAD-L000129](../../tests/test_sales_domain.py#L129) | 129 | `""` | — |
| [SRC-2822F30DAD-L000130](../../tests/test_sales_domain.py#L130) | 130 | `"    with pytest.raises(ValueError, match=\"paths must be unique\"):"` | — |
| [SRC-2822F30DAD-L000131](../../tests/test_sales_domain.py#L131) | 131 | `"        ProductTaxonomy(categories=(first, second))"` | — |
| [SRC-2822F30DAD-L000132](../../tests/test_sales_domain.py#L132) | 132 | `""` | — |
| [SRC-2822F30DAD-L000133](../../tests/test_sales_domain.py#L133) | 133 | `""` | — |
| [SRC-2822F30DAD-L000134](../../tests/test_sales_domain.py#L134) | 134 | `"def test_source_verified_product_fact_requires_an_evidence_pointer():"` | — |
| [SRC-2822F30DAD-L000135](../../tests/test_sales_domain.py#L135) | 135 | `"    with pytest.raises(ValueError, match=\"require evidence_id\"):"` | — |
| [SRC-2822F30DAD-L000136](../../tests/test_sales_domain.py#L136) | 136 | `"        ProductFact("` | — |
| [SRC-2822F30DAD-L000137](../../tests/test_sales_domain.py#L137) | 137 | `"            field=\"operating_voltage\","` | — |
| [SRC-2822F30DAD-L000138](../../tests/test_sales_domain.py#L138) | 138 | `"            value=\"24V\","` | — |
| [SRC-2822F30DAD-L000139](../../tests/test_sales_domain.py#L139) | 139 | `"            origin=FactOrigin.SOURCE_VERIFIED,"` | — |
| [SRC-2822F30DAD-L000140](../../tests/test_sales_domain.py#L140) | 140 | `"        )"` | — |
| [SRC-2822F30DAD-L000141](../../tests/test_sales_domain.py#L141) | 141 | `""` | — |
| [SRC-2822F30DAD-L000142](../../tests/test_sales_domain.py#L142) | 142 | `"    fact = ProductFact("` | — |
| [SRC-2822F30DAD-L000143](../../tests/test_sales_domain.py#L143) | 143 | `"        field=\"operating_voltage\","` | — |
| [SRC-2822F30DAD-L000144](../../tests/test_sales_domain.py#L144) | 144 | `"        value=\"24V\","` | — |
| [SRC-2822F30DAD-L000145](../../tests/test_sales_domain.py#L145) | 145 | `"        origin=FactOrigin.SOURCE_VERIFIED,"` | — |
| [SRC-2822F30DAD-L000146](../../tests/test_sales_domain.py#L146) | 146 | `"        evidence_id=\"manual-page-12\","` | — |
| [SRC-2822F30DAD-L000147](../../tests/test_sales_domain.py#L147) | 147 | `"    )"` | — |
| [SRC-2822F30DAD-L000148](../../tests/test_sales_domain.py#L148) | 148 | `"    assert fact.to_dict()[\"evidence_id\"] == \"manual-page-12\""` | — |
| [SRC-2822F30DAD-L000149](../../tests/test_sales_domain.py#L149) | 149 | `""` | — |
| [SRC-2822F30DAD-L000150](../../tests/test_sales_domain.py#L150) | 150 | `""` | — |
| [SRC-2822F30DAD-L000151](../../tests/test_sales_domain.py#L151) | 151 | `"def test_market_profile_is_a_constraint_not_a_demand_signal():"` | — |
| [SRC-2822F30DAD-L000152](../../tests/test_sales_domain.py#L152) | 152 | `"    market = MarketProfile("` | — |
| [SRC-2822F30DAD-L000153](../../tests/test_sales_domain.py#L153) | 153 | `"        locations=(\"Egypt\", \"Cairo\"),"` | — |
| [SRC-2822F30DAD-L000154](../../tests/test_sales_domain.py#L154) | 154 | `"        industries=(\"construction\", \"manufacturing\"),"` | — |
| [SRC-2822F30DAD-L000155](../../tests/test_sales_domain.py#L155) | 155 | `"        customer_types=(\"contractor\", \"facility owner\"),"` | — |
| [SRC-2822F30DAD-L000156](../../tests/test_sales_domain.py#L156) | 156 | `"        decision_roles=(\"procurement manager\",),"` | — |
| [SRC-2822F30DAD-L000157](../../tests/test_sales_domain.py#L157) | 157 | `"        exclusions=(\"residential end users\",),"` | — |
| [SRC-2822F30DAD-L000158](../../tests/test_sales_domain.py#L158) | 158 | `"    )"` | — |
| [SRC-2822F30DAD-L000159](../../tests/test_sales_domain.py#L159) | 159 | `""` | — |
| [SRC-2822F30DAD-L000160](../../tests/test_sales_domain.py#L160) | 160 | `"    assert market.to_dict()[\"industries\"] == [\"construction\", \"manufacturing\"]"` | — |
| [SRC-2822F30DAD-L000161](../../tests/test_sales_domain.py#L161) | 161 | `"    assert not hasattr(market, \"purchase_probability\")"` | — |
| [SRC-2822F30DAD-L000162](../../tests/test_sales_domain.py#L162) | 162 | `""` | — |
| [SRC-2822F30DAD-L000163](../../tests/test_sales_domain.py#L163) | 163 | `""` | — |
| [SRC-2822F30DAD-L000164](../../tests/test_sales_domain.py#L164) | 164 | `"def test_buyer_query_generation_is_sector_neutral_and_product_anchored():"` | — |
| [SRC-2822F30DAD-L000165](../../tests/test_sales_domain.py#L165) | 165 | `"    from agents.sales_domain import build_buyer_queries"` | — |
| [SRC-2822F30DAD-L000166](../../tests/test_sales_domain.py#L166) | 166 | `""` | — |
| [SRC-2822F30DAD-L000167](../../tests/test_sales_domain.py#L167) | 167 | `"    vehicle = ProductProfile(name=\"سيارة كهربائية\")"` | — |
| [SRC-2822F30DAD-L000168](../../tests/test_sales_domain.py#L168) | 168 | `"    industrial = ProductProfile(name=\"نظام إنذار حريق صناعي\")"` | — |
| [SRC-2822F30DAD-L000169](../../tests/test_sales_domain.py#L169) | 169 | `"    vehicle_queries = build_buyer_queries(vehicle, locale=\"ar\")"` | — |
| [SRC-2822F30DAD-L000170](../../tests/test_sales_domain.py#L170) | 170 | `"    industrial_queries = build_buyer_queries(industrial, locale=\"ar\")"` | — |
| [SRC-2822F30DAD-L000171](../../tests/test_sales_domain.py#L171) | 171 | `""` | — |
| [SRC-2822F30DAD-L000172](../../tests/test_sales_domain.py#L172) | 172 | `"    assert vehicle_queries"` | — |
| [SRC-2822F30DAD-L000173](../../tests/test_sales_domain.py#L173) | 173 | `"    assert industrial_queries"` | — |
| [SRC-2822F30DAD-L000174](../../tests/test_sales_domain.py#L174) | 174 | `"    assert all(\"شقه\" not in query and \"تمليك\" not in query for query in vehicle_queries)"` | — |
| [SRC-2822F30DAD-L000175](../../tests/test_sales_domain.py#L175) | 175 | `"    assert all(\"شقه\" not in query and \"تمليك\" not in query for query in industrial_queries)"` | — |
| [SRC-2822F30DAD-L000176](../../tests/test_sales_domain.py#L176) | 176 | `"    assert any(\"سيارة كهربائية\" in query for query in vehicle_queries)"` | — |
| [SRC-2822F30DAD-L000177](../../tests/test_sales_domain.py#L177) | 177 | `"    assert any(\"نظام إنذار حريق صناعي\" in query for query in industrial_queries)"` | — |
| [SRC-2822F30DAD-L000178](../../tests/test_sales_domain.py#L178) | 178 | `""` | — |
| [SRC-2822F30DAD-L000179](../../tests/test_sales_domain.py#L179) | 179 | `""` | — |
| [SRC-2822F30DAD-L000180](../../tests/test_sales_domain.py#L180) | 180 | `"def test_buyer_query_generation_uses_only_explicit_market_location():"` | — |
| [SRC-2822F30DAD-L000181](../../tests/test_sales_domain.py#L181) | 181 | `"    from agents.sales_domain import build_buyer_queries"` | — |
| [SRC-2822F30DAD-L000182](../../tests/test_sales_domain.py#L182) | 182 | `""` | — |
| [SRC-2822F30DAD-L000183](../../tests/test_sales_domain.py#L183) | 183 | `"    product = ProductProfile(name=\"FACP\")"` | — |
| [SRC-2822F30DAD-L000184](../../tests/test_sales_domain.py#L184) | 184 | `"    market = MarketProfile(locations=(\"Cairo\", \"Egypt\"))"` | — |
| [SRC-2822F30DAD-L000185](../../tests/test_sales_domain.py#L185) | 185 | `"    queries = build_buyer_queries(product, market, locale=\"en\")"` | — |
| [SRC-2822F30DAD-L000186](../../tests/test_sales_domain.py#L186) | 186 | `""` | — |
| [SRC-2822F30DAD-L000187](../../tests/test_sales_domain.py#L187) | 187 | `"    assert queries"` | — |
| [SRC-2822F30DAD-L000188](../../tests/test_sales_domain.py#L188) | 188 | `"    assert all(\"Cairo Egypt\" in query for query in queries)"` | — |
| [SRC-2822F30DAD-L000189](../../tests/test_sales_domain.py#L189) | 189 | `""` | — |
| [SRC-2822F30DAD-L000190](../../tests/test_sales_domain.py#L190) | 190 | `""` | — |
| [SRC-2822F30DAD-L000191](../../tests/test_sales_domain.py#L191) | 191 | `"def test_buyer_query_generation_drops_unrelated_planner_queries():"` | — |
| [SRC-2822F30DAD-L000192](../../tests/test_sales_domain.py#L192) | 192 | `"    from agents.sales_domain import build_buyer_queries"` | — |
| [SRC-2822F30DAD-L000193](../../tests/test_sales_domain.py#L193) | 193 | `""` | — |
| [SRC-2822F30DAD-L000194](../../tests/test_sales_domain.py#L194) | 194 | `"    product = ProductProfile(name=\"FACP\")"` | — |
| [SRC-2822F30DAD-L000195](../../tests/test_sales_domain.py#L195) | 195 | `"    queries = build_buyer_queries("` | — |
| [SRC-2822F30DAD-L000196](../../tests/test_sales_domain.py#L196) | 196 | `"        product,"` | — |
| [SRC-2822F30DAD-L000197](../../tests/test_sales_domain.py#L197) | 197 | `"        locale=\"en\","` | — |
| [SRC-2822F30DAD-L000198](../../tests/test_sales_domain.py#L198) | 198 | `"        existing_queries=("` | — |
| [SRC-2822F30DAD-L000199](../../tests/test_sales_domain.py#L199) | 199 | `"            \"apartments for sale in Cairo\","` | — |
| [SRC-2822F30DAD-L000200](../../tests/test_sales_domain.py#L200) | 200 | `"            \"FACP procurement request\","` | — |
| [SRC-2822F30DAD-L000201](../../tests/test_sales_domain.py#L201) | 201 | `"            \"generic buying intent\","` | — |
| [SRC-2822F30DAD-L000202](../../tests/test_sales_domain.py#L202) | 202 | `"        ),"` | — |
| [SRC-2822F30DAD-L000203](../../tests/test_sales_domain.py#L203) | 203 | `"    )"` | — |
| [SRC-2822F30DAD-L000204](../../tests/test_sales_domain.py#L204) | 204 | `""` | — |
| [SRC-2822F30DAD-L000205](../../tests/test_sales_domain.py#L205) | 205 | `"    assert any(\"FACP procurement request\" in query for query in queries)"` | — |
| [SRC-2822F30DAD-L000206](../../tests/test_sales_domain.py#L206) | 206 | `"    assert all(\"apartments\" not in query for query in queries)"` | — |
| [SRC-2822F30DAD-L000207](../../tests/test_sales_domain.py#L207) | 207 | `"    assert all(\"generic buying intent\" not in query for query in queries)"` | — |
| [SRC-2822F30DAD-L000208](../../tests/test_sales_domain.py#L208) | 208 | `""` | — |
| [SRC-2822F30DAD-L000209](../../tests/test_sales_domain.py#L209) | 209 | `"def test_demand_evidence_requires_an_absolute_http_url():"` | — |
| [SRC-2822F30DAD-L000210](../../tests/test_sales_domain.py#L210) | 210 | `"    with pytest.raises(ValueError, match=\"absolute HTTP\"):"` | — |
| [SRC-2822F30DAD-L000211](../../tests/test_sales_domain.py#L211) | 211 | `"        page_evidence(source_url=\"/relative/path\")"` | — |
| [SRC-2822F30DAD-L000212](../../tests/test_sales_domain.py#L212) | 212 | `""` | — |
| [SRC-2822F30DAD-L000213](../../tests/test_sales_domain.py#L213) | 213 | `"    with pytest.raises(ValueError, match=\"embedded credentials\"):"` | — |
| [SRC-2822F30DAD-L000214](../../tests/test_sales_domain.py#L214) | 214 | `"        page_evidence(source_url=\"https://user:secret@example.org/post\")"` | — |
| [SRC-2822F30DAD-L000215](../../tests/test_sales_domain.py#L215) | 215 | `""` | — |
| [SRC-2822F30DAD-L000216](../../tests/test_sales_domain.py#L216) | 216 | `""` | — |
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
