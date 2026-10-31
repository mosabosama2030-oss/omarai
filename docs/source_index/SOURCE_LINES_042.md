# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **042**
- سجلات الأسطر: **800**
- النطاق: SRC-4397BC2CD2-L000082 إلى SRC-3D0DE98F65-L000084
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-4397BC2CD2 — [tests/test_intent_router_integration.py](../../tests/test_intent_router_integration.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-4397BC2CD2-L000082](../../tests/test_intent_router_integration.py#L82) | 82 | `""` | — |
| [SRC-4397BC2CD2-L000083](../../tests/test_intent_router_integration.py#L83) | 83 | `"def test_contextual_price_followup_searches_with_previous_subject(monkeypatch) -> None:"` | — |
| [SRC-4397BC2CD2-L000084](../../tests/test_intent_router_integration.py#L84) | 84 | `"    agent = WebAgent()"` | — |
| [SRC-4397BC2CD2-L000085](../../tests/test_intent_router_integration.py#L85) | 85 | `"    agent.api_key = \"\"  # Keep this acceptance test deterministic and offline."` | — |
| [SRC-4397BC2CD2-L000086](../../tests/test_intent_router_integration.py#L86) | 86 | `"    seen: dict = {}"` | — |
| [SRC-4397BC2CD2-L000087](../../tests/test_intent_router_integration.py#L87) | 87 | `"    history = ["` | — |
| [SRC-4397BC2CD2-L000088](../../tests/test_intent_router_integration.py#L88) | 88 | `"        {\"role\": \"user\", \"content\": \"عايز أعرف سعر iPhone 17 في مصر\"},"` | — |
| [SRC-4397BC2CD2-L000089](../../tests/test_intent_router_integration.py#L89) | 89 | `"        {\"role\": \"assistant\", \"content\": \"نتحدث عن هاتف iPhone 17 في السوق المصري.\"},"` | — |
| [SRC-4397BC2CD2-L000090](../../tests/test_intent_router_integration.py#L90) | 90 | `"    ]"` | — |
| [SRC-4397BC2CD2-L000091](../../tests/test_intent_router_integration.py#L91) | 91 | `""` | — |
| [SRC-4397BC2CD2-L000092](../../tests/test_intent_router_integration.py#L92) | 92 | `"    def collect(plan):"` | — |
| [SRC-4397BC2CD2-L000093](../../tests/test_intent_router_integration.py#L93) | 93 | `"        seen[\"plan\"] = dict(plan)"` | — |
| [SRC-4397BC2CD2-L000094](../../tests/test_intent_router_integration.py#L94) | 94 | `"        sources = ["` | — |
| [SRC-4397BC2CD2-L000095](../../tests/test_intent_router_integration.py#L95) | 95 | `"            _evidence(\"example.com\", plan[\"queries\"]),"` | — |
| [SRC-4397BC2CD2-L000096](../../tests/test_intent_router_integration.py#L96) | 96 | `"            _evidence(\"example.net\", plan[\"queries\"]),"` | — |
| [SRC-4397BC2CD2-L000097](../../tests/test_intent_router_integration.py#L97) | 97 | `"        ]"` | — |
| [SRC-4397BC2CD2-L000098](../../tests/test_intent_router_integration.py#L98) | 98 | `"        return sources, [], _report(plan, sources)"` | — |
| [SRC-4397BC2CD2-L000099](../../tests/test_intent_router_integration.py#L99) | 99 | `""` | — |
| [SRC-4397BC2CD2-L000100](../../tests/test_intent_router_integration.py#L100) | 100 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-4397BC2CD2-L000101](../../tests/test_intent_router_integration.py#L101) | 101 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, source: True)"` | — |
| [SRC-4397BC2CD2-L000102](../../tests/test_intent_router_integration.py#L102) | 102 | `"    def generate(resolved_question, *args, **kwargs):"` | — |
| [SRC-4397BC2CD2-L000103](../../tests/test_intent_router_integration.py#L103) | 103 | `"        seen[\"generation_question\"] = resolved_question"` | — |
| [SRC-4397BC2CD2-L000104](../../tests/test_intent_router_integration.py#L104) | 104 | `"        return \"توجد أسعار مختلفة حسب النسخة [المصدر 1].\""` | — |
| [SRC-4397BC2CD2-L000105](../../tests/test_intent_router_integration.py#L105) | 105 | `""` | — |
| [SRC-4397BC2CD2-L000106](../../tests/test_intent_router_integration.py#L106) | 106 | `"    def review(resolved_question, answer, sources):"` | — |
| [SRC-4397BC2CD2-L000107](../../tests/test_intent_router_integration.py#L107) | 107 | `"        seen[\"review_question\"] = resolved_question"` | — |
| [SRC-4397BC2CD2-L000108](../../tests/test_intent_router_integration.py#L108) | 108 | `"        return answer"` | — |
| [SRC-4397BC2CD2-L000109](../../tests/test_intent_router_integration.py#L109) | 109 | `""` | — |
| [SRC-4397BC2CD2-L000110](../../tests/test_intent_router_integration.py#L110) | 110 | `"    monkeypatch.setattr(agent, \"_generate\", generate)"` | — |
| [SRC-4397BC2CD2-L000111](../../tests/test_intent_router_integration.py#L111) | 111 | `"    monkeypatch.setattr(agent, \"_review_answer\", review)"` | — |
| [SRC-4397BC2CD2-L000112](../../tests/test_intent_router_integration.py#L112) | 112 | `""` | — |
| [SRC-4397BC2CD2-L000113](../../tests/test_intent_router_integration.py#L113) | 113 | `"    result = agent.answer(\"كام سعرها؟\", history=history)"` | — |
| [SRC-4397BC2CD2-L000114](../../tests/test_intent_router_integration.py#L114) | 114 | `""` | — |
| [SRC-4397BC2CD2-L000115](../../tests/test_intent_router_integration.py#L115) | 115 | `"    assert result[\"intent_route\"] == \"WEB_SIMPLE\""` | — |
| [SRC-4397BC2CD2-L000116](../../tests/test_intent_router_integration.py#L116) | 116 | `"    assert result[\"research_plan\"][\"intent_route\"] == \"WEB_SIMPLE\""` | — |
| [SRC-4397BC2CD2-L000117](../../tests/test_intent_router_integration.py#L117) | 117 | `"    assert result[\"used_web_search\"] is True"` | — |
| [SRC-4397BC2CD2-L000118](../../tests/test_intent_router_integration.py#L118) | 118 | `"    assert result[\"citation_validation\"][\"method\"] == \"numeric_source_index_range_only\""` | — |
| [SRC-4397BC2CD2-L000119](../../tests/test_intent_router_integration.py#L119) | 119 | `"    assert result[\"search_report\"][\"citation_validation\"] == result[\"citation_validation\"]"` | — |
| [SRC-4397BC2CD2-L000120](../../tests/test_intent_router_integration.py#L120) | 120 | `"    assert any(\"iPhone 17\" in query for query in seen[\"plan\"][\"queries\"])"` | — |
| [SRC-4397BC2CD2-L000121](../../tests/test_intent_router_integration.py#L121) | 121 | `"    # The plan already resolved the follow-up for search, but historically generation"` | — |
| [SRC-4397BC2CD2-L000122](../../tests/test_intent_router_integration.py#L122) | 122 | `"    # still received only \"كام سعرها؟\". All answer stages must receive the same context."` | — |
| [SRC-4397BC2CD2-L000123](../../tests/test_intent_router_integration.py#L123) | 123 | `"    assert \"iPhone 17\" in seen[\"generation_question\"]"` | — |
| [SRC-4397BC2CD2-L000124](../../tests/test_intent_router_integration.py#L124) | 124 | `"    assert \"كام سعرها\" in seen[\"generation_question\"]"` | — |
| [SRC-4397BC2CD2-L000125](../../tests/test_intent_router_integration.py#L125) | 125 | `"    assert seen[\"review_question\"] == seen[\"generation_question\"]"` | — |
| [SRC-4397BC2CD2-L000126](../../tests/test_intent_router_integration.py#L126) | 126 | `""` | — |
| [SRC-4397BC2CD2-L000127](../../tests/test_intent_router_integration.py#L127) | 127 | `""` | — |
| [SRC-4397BC2CD2-L000128](../../tests/test_intent_router_integration.py#L128) | 128 | `"def test_multi_part_comparison_forces_deep_plan_and_multiple_angles(monkeypatch) -> None:"` | — |
| [SRC-4397BC2CD2-L000129](../../tests/test_intent_router_integration.py#L129) | 129 | `"    agent = WebAgent()"` | — |
| [SRC-4397BC2CD2-L000130](../../tests/test_intent_router_integration.py#L130) | 130 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-4397BC2CD2-L000131](../../tests/test_intent_router_integration.py#L131) | 131 | `"    seen: dict = {\"plans\": []}"` | — |
| [SRC-4397BC2CD2-L000132](../../tests/test_intent_router_integration.py#L132) | 132 | `"    history = []"` | — |
| [SRC-4397BC2CD2-L000133](../../tests/test_intent_router_integration.py#L133) | 133 | `""` | — |
| [SRC-4397BC2CD2-L000134](../../tests/test_intent_router_integration.py#L134) | 134 | `"    def plan(question, prior_history):"` | — |
| [SRC-4397BC2CD2-L000135](../../tests/test_intent_router_integration.py#L135) | 135 | `"        return {"` | — |
| [SRC-4397BC2CD2-L000136](../../tests/test_intent_router_integration.py#L136) | 136 | `"            \"queries\": [\"iPhone 17 versus Samsung S26\"],"` | — |
| [SRC-4397BC2CD2-L000137](../../tests/test_intent_router_integration.py#L137) | 137 | `"            \"direct_urls\": [],"` | — |
| [SRC-4397BC2CD2-L000138](../../tests/test_intent_router_integration.py#L138) | 138 | `"            \"social_focus\": False,"` | — |
| [SRC-4397BC2CD2-L000139](../../tests/test_intent_router_integration.py#L139) | 139 | `"            \"freshness\": \"any\","` | — |
| [SRC-4397BC2CD2-L000140](../../tests/test_intent_router_integration.py#L140) | 140 | `"            \"depth\": \"standard\","` | — |
| [SRC-4397BC2CD2-L000141](../../tests/test_intent_router_integration.py#L141) | 141 | `"            \"platforms\": [],"` | — |
| [SRC-4397BC2CD2-L000142](../../tests/test_intent_router_integration.py#L142) | 142 | `"            \"planning_method\": \"test_single_query\","` | — |
| [SRC-4397BC2CD2-L000143](../../tests/test_intent_router_integration.py#L143) | 143 | `"        }"` | — |
| [SRC-4397BC2CD2-L000144](../../tests/test_intent_router_integration.py#L144) | 144 | `""` | — |
| [SRC-4397BC2CD2-L000145](../../tests/test_intent_router_integration.py#L145) | 145 | `"    def collect(research_plan):"` | — |
| [SRC-4397BC2CD2-L000146](../../tests/test_intent_router_integration.py#L146) | 146 | `"        seen[\"plans\"].append(dict(research_plan))"` | — |
| [SRC-4397BC2CD2-L000147](../../tests/test_intent_router_integration.py#L147) | 147 | `"        sources = ["` | — |
| [SRC-4397BC2CD2-L000148](../../tests/test_intent_router_integration.py#L148) | 148 | `"            _evidence(\"example.com\", research_plan[\"queries\"]),"` | — |
| [SRC-4397BC2CD2-L000149](../../tests/test_intent_router_integration.py#L149) | 149 | `"            _evidence(\"example.net\", research_plan[\"queries\"]),"` | — |
| [SRC-4397BC2CD2-L000150](../../tests/test_intent_router_integration.py#L150) | 150 | `"        ]"` | — |
| [SRC-4397BC2CD2-L000151](../../tests/test_intent_router_integration.py#L151) | 151 | `"        return sources, [], _report(research_plan, sources)"` | — |
| [SRC-4397BC2CD2-L000152](../../tests/test_intent_router_integration.py#L152) | 152 | `""` | — |
| [SRC-4397BC2CD2-L000153](../../tests/test_intent_router_integration.py#L153) | 153 | `"    monkeypatch.setattr(agent, \"_plan_search\", plan)"` | — |
| [SRC-4397BC2CD2-L000154](../../tests/test_intent_router_integration.py#L154) | 154 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-4397BC2CD2-L000155](../../tests/test_intent_router_integration.py#L155) | 155 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, source: True)"` | — |
| [SRC-4397BC2CD2-L000156](../../tests/test_intent_router_integration.py#L156) | 156 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: \"مقارنة أولية [المصدر 1].\")"` | — |
| [SRC-4397BC2CD2-L000157](../../tests/test_intent_router_integration.py#L157) | 157 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-4397BC2CD2-L000158](../../tests/test_intent_router_integration.py#L158) | 158 | `"    monkeypatch.setattr(agent, \"_repair_answer_coverage\", lambda _q, answer, _s, _m: answer)"` | — |
| [SRC-4397BC2CD2-L000159](../../tests/test_intent_router_integration.py#L159) | 159 | `""` | — |
| [SRC-4397BC2CD2-L000160](../../tests/test_intent_router_integration.py#L160) | 160 | `"    result = agent.answer("` | — |
| [SRC-4397BC2CD2-L000161](../../tests/test_intent_router_integration.py#L161) | 161 | `"        \"قارن بين iPhone 17 وSamsung S26 من حيث السعر والبطارية والكاميرا\","` | — |
| [SRC-4397BC2CD2-L000162](../../tests/test_intent_router_integration.py#L162) | 162 | `"        history=history,"` | — |
| [SRC-4397BC2CD2-L000163](../../tests/test_intent_router_integration.py#L163) | 163 | `"    )"` | — |
| [SRC-4397BC2CD2-L000164](../../tests/test_intent_router_integration.py#L164) | 164 | `""` | — |
| [SRC-4397BC2CD2-L000165](../../tests/test_intent_router_integration.py#L165) | 165 | `"    assert result[\"intent_route\"] == \"WEB_DEEP\""` | — |
| [SRC-4397BC2CD2-L000166](../../tests/test_intent_router_integration.py#L166) | 166 | `"    assert result[\"research_plan\"][\"intent_route\"] == \"WEB_DEEP\""` | — |
| [SRC-4397BC2CD2-L000167](../../tests/test_intent_router_integration.py#L167) | 167 | `"    assert result[\"research_plan\"][\"depth\"] == \"deep\""` | — |
| [SRC-4397BC2CD2-L000168](../../tests/test_intent_router_integration.py#L168) | 168 | `"    initial_plan = seen[\"plans\"][0]"` | — |
| [SRC-4397BC2CD2-L000169](../../tests/test_intent_router_integration.py#L169) | 169 | `"    assert len(initial_plan[\"queries\"]) > 1"` | — |
| [SRC-4397BC2CD2-L000170](../../tests/test_intent_router_integration.py#L170) | 170 | `"    assert initial_plan[\"coverage_gap_repair_slot_reserved\"] is True"` | — |
| [SRC-4397BC2CD2-L000171](../../tests/test_intent_router_integration.py#L171) | 171 | `"    assert initial_plan[\"query_limit\"] == 7"` | — |
| [SRC-4397BC2CD2-L000172](../../tests/test_intent_router_integration.py#L172) | 172 | `"    # Each requested criterion gets a distinct search angle before generic deep"` | — |
| [SRC-4397BC2CD2-L000173](../../tests/test_intent_router_integration.py#L173) | 173 | `"    # modifiers consume the bounded query budget."` | — |
| [SRC-4397BC2CD2-L000174](../../tests/test_intent_router_integration.py#L174) | 174 | `"    planned_queries = \" \".join(initial_plan[\"queries\"]).casefold()"` | — |
| [SRC-4397BC2CD2-L000175](../../tests/test_intent_router_integration.py#L175) | 175 | `"    assert \"السعر\" in planned_queries"` | — |
| [SRC-4397BC2CD2-L000176](../../tests/test_intent_router_integration.py#L176) | 176 | `"    assert \"البطارية\" in planned_queries"` | — |
| [SRC-4397BC2CD2-L000177](../../tests/test_intent_router_integration.py#L177) | 177 | `"    assert \"الكاميرا\" in planned_queries"` | — |
| [SRC-4397BC2CD2-L000178](../../tests/test_intent_router_integration.py#L178) | 178 | `"    assert len(initial_plan[\"queries\"]) <= 7"` | — |
| [SRC-4397BC2CD2-L000179](../../tests/test_intent_router_integration.py#L179) | 179 | `"    assert result[\"used_web_search\"] is True"` | — |
| [SRC-4397BC2CD2-L000180](../../tests/test_intent_router_integration.py#L180) | 180 | `"    coverage = result[\"answer_coverage\"]"` | — |
| [SRC-4397BC2CD2-L000181](../../tests/test_intent_router_integration.py#L181) | 181 | `"    assert coverage[\"method\"] == \"explicit_criteria_heuristic\""` | — |
| [SRC-4397BC2CD2-L000182](../../tests/test_intent_router_integration.py#L182) | 182 | `"    assert coverage[\"targets\"] == [\"السعر\", \"البطارية\", \"الكاميرا\"]"` | — |
| [SRC-4397BC2CD2-L000183](../../tests/test_intent_router_integration.py#L183) | 183 | `"    assert coverage[\"status\"] == \"model_review_requested_not_machine_verified\""` | — |
| [SRC-4397BC2CD2-L000184](../../tests/test_intent_router_integration.py#L184) | 184 | `"    assert coverage[\"automatically_graded\"] is False"` | — |
| [SRC-4397BC2CD2-L000185](../../tests/test_intent_router_integration.py#L185) | 185 | `"    # The mocked sources do not contain battery/camera evidence. The task must"` | — |
| [SRC-4397BC2CD2-L000186](../../tests/test_intent_router_integration.py#L186) | 186 | `"    # remain visibly incomplete even if the planner generated multiple queries."` | — |
| [SRC-4397BC2CD2-L000187](../../tests/test_intent_router_integration.py#L187) | 187 | `"    assert coverage[\"source_evidence_gap_count\"] == 2"` | — |
| [SRC-4397BC2CD2-L000188](../../tests/test_intent_router_integration.py#L188) | 188 | `"    assert result[\"task_fulfillment_status\"] == \"possible_gap_detected\""` | — |
| [SRC-4397BC2CD2-L000189](../../tests/test_intent_router_integration.py#L189) | 189 | `"    assert len(seen[\"plans\"]) == 2"` | — |
| [SRC-4397BC2CD2-L000190](../../tests/test_intent_router_integration.py#L190) | 190 | `"    assert \"البطارية\" in \" \".join(seen[\"plans\"][1][\"queries\"])"` | — |
| [SRC-4397BC2CD2-L000191](../../tests/test_intent_router_integration.py#L191) | 191 | `"    assert result[\"search_report\"][\"criterion_gap_research\"][\"attempted\"] is True"` | — |
| [SRC-4397BC2CD2-L000192](../../tests/test_intent_router_integration.py#L192) | 192 | `"    assert result[\"search_report\"][\"criterion_gap_research\"][\"status\"] == \"search_completed_no_new_criterion_evidence\""` | — |
| [SRC-4397BC2CD2-L000193](../../tests/test_intent_router_integration.py#L193) | 193 | `""` | — |
| [SRC-4397BC2CD2-L000194](../../tests/test_intent_router_integration.py#L194) | 194 | `"def test_deep_plan_preserves_all_eight_explicit_criteria_within_query_budget(monkeypatch) -> None:"` | — |
| [SRC-4397BC2CD2-L000195](../../tests/test_intent_router_integration.py#L195) | 195 | `"    agent = WebAgent()"` | — |
| [SRC-4397BC2CD2-L000196](../../tests/test_intent_router_integration.py#L196) | 196 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-4397BC2CD2-L000197](../../tests/test_intent_router_integration.py#L197) | 197 | `"    seen: dict = {\"plans\": []}"` | — |
| [SRC-4397BC2CD2-L000198](../../tests/test_intent_router_integration.py#L198) | 198 | `"    question = ("` | — |
| [SRC-4397BC2CD2-L000199](../../tests/test_intent_router_integration.py#L199) | 199 | `"        \"قارن بين خدمات من حيث السعر، الخصوصية، الاعتمادية، الدعم، \""` | — |
| [SRC-4397BC2CD2-L000200](../../tests/test_intent_router_integration.py#L200) | 200 | `"        \"الأمان، السرعة، الجودة، والتوفر\""` | — |
| [SRC-4397BC2CD2-L000201](../../tests/test_intent_router_integration.py#L201) | 201 | `"    )"` | — |
| [SRC-4397BC2CD2-L000202](../../tests/test_intent_router_integration.py#L202) | 202 | `""` | — |
| [SRC-4397BC2CD2-L000203](../../tests/test_intent_router_integration.py#L203) | 203 | `"    def plan(_question, _history):"` | — |
| [SRC-4397BC2CD2-L000204](../../tests/test_intent_router_integration.py#L204) | 204 | `"        return {"` | — |
| [SRC-4397BC2CD2-L000205](../../tests/test_intent_router_integration.py#L205) | 205 | `"            \"queries\": [\"مقارنة الخدمات\"],"` | — |
| [SRC-4397BC2CD2-L000206](../../tests/test_intent_router_integration.py#L206) | 206 | `"            \"direct_urls\": [],"` | — |
| [SRC-4397BC2CD2-L000207](../../tests/test_intent_router_integration.py#L207) | 207 | `"            \"social_focus\": False,"` | — |
| [SRC-4397BC2CD2-L000208](../../tests/test_intent_router_integration.py#L208) | 208 | `"            \"freshness\": \"any\","` | — |
| [SRC-4397BC2CD2-L000209](../../tests/test_intent_router_integration.py#L209) | 209 | `"            \"depth\": \"standard\","` | — |
| [SRC-4397BC2CD2-L000210](../../tests/test_intent_router_integration.py#L210) | 210 | `"            \"platforms\": [],"` | — |
| [SRC-4397BC2CD2-L000211](../../tests/test_intent_router_integration.py#L211) | 211 | `"            \"planning_method\": \"test_single_query\","` | — |
| [SRC-4397BC2CD2-L000212](../../tests/test_intent_router_integration.py#L212) | 212 | `"        }"` | — |
| [SRC-4397BC2CD2-L000213](../../tests/test_intent_router_integration.py#L213) | 213 | `""` | — |
| [SRC-4397BC2CD2-L000214](../../tests/test_intent_router_integration.py#L214) | 214 | `"    def collect(research_plan):"` | — |
| [SRC-4397BC2CD2-L000215](../../tests/test_intent_router_integration.py#L215) | 215 | `"        seen[\"plans\"].append(dict(research_plan))"` | — |
| [SRC-4397BC2CD2-L000216](../../tests/test_intent_router_integration.py#L216) | 216 | `"        sources = ["` | — |
| [SRC-4397BC2CD2-L000217](../../tests/test_intent_router_integration.py#L217) | 217 | `"            _evidence(\"example.com\", research_plan[\"queries\"]),"` | — |
| [SRC-4397BC2CD2-L000218](../../tests/test_intent_router_integration.py#L218) | 218 | `"            _evidence(\"example.net\", research_plan[\"queries\"]),"` | — |
| [SRC-4397BC2CD2-L000219](../../tests/test_intent_router_integration.py#L219) | 219 | `"        ]"` | — |
| [SRC-4397BC2CD2-L000220](../../tests/test_intent_router_integration.py#L220) | 220 | `"        return sources, [], _report(research_plan, sources)"` | — |
| [SRC-4397BC2CD2-L000221](../../tests/test_intent_router_integration.py#L221) | 221 | `""` | — |
| [SRC-4397BC2CD2-L000222](../../tests/test_intent_router_integration.py#L222) | 222 | `"    monkeypatch.setattr(agent, \"_plan_search\", plan)"` | — |
| [SRC-4397BC2CD2-L000223](../../tests/test_intent_router_integration.py#L223) | 223 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-4397BC2CD2-L000224](../../tests/test_intent_router_integration.py#L224) | 224 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda _query, _source: True)"` | — |
| [SRC-4397BC2CD2-L000225](../../tests/test_intent_router_integration.py#L225) | 225 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: \"مقارنة أولية [المصدر 1].\")"` | — |
| [SRC-4397BC2CD2-L000226](../../tests/test_intent_router_integration.py#L226) | 226 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda _question, answer, _sources: answer)"` | — |
| [SRC-4397BC2CD2-L000227](../../tests/test_intent_router_integration.py#L227) | 227 | `"    monkeypatch.setattr(agent, \"_repair_answer_coverage\", lambda _q, answer, _s, _m: answer)"` | — |
| [SRC-4397BC2CD2-L000228](../../tests/test_intent_router_integration.py#L228) | 228 | `""` | — |
| [SRC-4397BC2CD2-L000229](../../tests/test_intent_router_integration.py#L229) | 229 | `"    agent.answer(question, history=[])"` | — |
| [SRC-4397BC2CD2-L000230](../../tests/test_intent_router_integration.py#L230) | 230 | `""` | — |
| [SRC-4397BC2CD2-L000231](../../tests/test_intent_router_integration.py#L231) | 231 | `"    # All eight explicit criteria consume the bounded initial query allowance;"` | — |
| [SRC-4397BC2CD2-L000232](../../tests/test_intent_router_integration.py#L232) | 232 | `"    # the system must not launch an unbudgeted ninth query for coverage repair."` | — |
| [SRC-4397BC2CD2-L000233](../../tests/test_intent_router_integration.py#L233) | 233 | `"    assert len(seen[\"plans\"]) == 1"` | — |
| [SRC-4397BC2CD2-L000234](../../tests/test_intent_router_integration.py#L234) | 234 | `"    targets = WebAgent._question_coverage_targets(question)"` | — |
| [SRC-4397BC2CD2-L000235](../../tests/test_intent_router_integration.py#L235) | 235 | `"    assert len(targets) == 8"` | — |
| [SRC-4397BC2CD2-L000236](../../tests/test_intent_router_integration.py#L236) | 236 | `"    initial_plan = seen[\"plans\"][0]"` | — |
| [SRC-4397BC2CD2-L000237](../../tests/test_intent_router_integration.py#L237) | 237 | `"    queries = initial_plan[\"queries\"]"` | — |
| [SRC-4397BC2CD2-L000238](../../tests/test_intent_router_integration.py#L238) | 238 | `"    assert initial_plan[\"coverage_gap_repair_slot_reserved\"] is False"` | — |
| [SRC-4397BC2CD2-L000239](../../tests/test_intent_router_integration.py#L239) | 239 | `"    assert initial_plan[\"query_limit\"] == 8"` | — |
| [SRC-4397BC2CD2-L000240](../../tests/test_intent_router_integration.py#L240) | 240 | `"    assert len(queries) == 8"` | — |
| [SRC-4397BC2CD2-L000241](../../tests/test_intent_router_integration.py#L241) | 241 | `"    for target in targets:"` | — |
| [SRC-4397BC2CD2-L000242](../../tests/test_intent_router_integration.py#L242) | 242 | `"        assert any(target in query for query in queries), f\"Missing criterion query for {target!r}\""` | — |
| [SRC-4397BC2CD2-L000243](../../tests/test_intent_router_integration.py#L243) | 243 | `""` | — |
## اختبارات

### FILE-62DC597310 — [tests/test_live_search_connectors.py](../../tests/test_live_search_connectors.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-62DC597310-L000001](../../tests/test_live_search_connectors.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-62DC597310-L000002](../../tests/test_live_search_connectors.py#L2) | 2 | `""` | — |
| [SRC-62DC597310-L000003](../../tests/test_live_search_connectors.py#L3) | 3 | `"import httpx"` | — |
| [SRC-62DC597310-L000004](../../tests/test_live_search_connectors.py#L4) | 4 | `""` | — |
| [SRC-62DC597310-L000005](../../tests/test_live_search_connectors.py#L5) | 5 | `"from agents.web_agent import WebAgent"` | — |
| [SRC-62DC597310-L000006](../../tests/test_live_search_connectors.py#L6) | 6 | `""` | — |
| [SRC-62DC597310-L000007](../../tests/test_live_search_connectors.py#L7) | 7 | `""` | — |
| [SRC-62DC597310-L000008](../../tests/test_live_search_connectors.py#L8) | 8 | `"class FakeResponse:"` | — |
| [SRC-62DC597310-L000009](../../tests/test_live_search_connectors.py#L9) | 9 | `"    def __init__(self, payload):"` | — |
| [SRC-62DC597310-L000010](../../tests/test_live_search_connectors.py#L10) | 10 | `"        self.payload = payload"` | — |
| [SRC-62DC597310-L000011](../../tests/test_live_search_connectors.py#L11) | 11 | `"        self.status_code = 200"` | — |
| [SRC-62DC597310-L000012](../../tests/test_live_search_connectors.py#L12) | 12 | `""` | — |
| [SRC-62DC597310-L000013](../../tests/test_live_search_connectors.py#L13) | 13 | `"    def raise_for_status(self):"` | — |
| [SRC-62DC597310-L000014](../../tests/test_live_search_connectors.py#L14) | 14 | `"        return None"` | — |
| [SRC-62DC597310-L000015](../../tests/test_live_search_connectors.py#L15) | 15 | `""` | — |
| [SRC-62DC597310-L000016](../../tests/test_live_search_connectors.py#L16) | 16 | `"    def json(self):"` | — |
| [SRC-62DC597310-L000017](../../tests/test_live_search_connectors.py#L17) | 17 | `"        return self.payload"` | — |
| [SRC-62DC597310-L000018](../../tests/test_live_search_connectors.py#L18) | 18 | `""` | — |
| [SRC-62DC597310-L000019](../../tests/test_live_search_connectors.py#L19) | 19 | `""` | — |
| [SRC-62DC597310-L000020](../../tests/test_live_search_connectors.py#L20) | 20 | `"def test_brave_search_adapter_normalizes_real_api_response(monkeypatch):"` | — |
| [SRC-62DC597310-L000021](../../tests/test_live_search_connectors.py#L21) | 21 | `"    monkeypatch.setenv(\"BRAVE_SEARCH_API_KEY\", \"unit-test-secret\")"` | — |
| [SRC-62DC597310-L000022](../../tests/test_live_search_connectors.py#L22) | 22 | `"    requested = {}"` | — |
| [SRC-62DC597310-L000023](../../tests/test_live_search_connectors.py#L23) | 23 | `""` | — |
| [SRC-62DC597310-L000024](../../tests/test_live_search_connectors.py#L24) | 24 | `"    def fake_get(url, **kwargs):"` | — |
| [SRC-62DC597310-L000025](../../tests/test_live_search_connectors.py#L25) | 25 | `"        requested[\"url\"] = url"` | — |
| [SRC-62DC597310-L000026](../../tests/test_live_search_connectors.py#L26) | 26 | `"        requested.update(kwargs)"` | — |
| [SRC-62DC597310-L000027](../../tests/test_live_search_connectors.py#L27) | 27 | `"        return FakeResponse({"` | — |
| [SRC-62DC597310-L000028](../../tests/test_live_search_connectors.py#L28) | 28 | `"            \"web\": {"` | — |
| [SRC-62DC597310-L000029](../../tests/test_live_search_connectors.py#L29) | 29 | `"                \"results\": [{"` | — |
| [SRC-62DC597310-L000030](../../tests/test_live_search_connectors.py#L30) | 30 | `"                    \"title\": \"Current research\","` | — |
| [SRC-62DC597310-L000031](../../tests/test_live_search_connectors.py#L31) | 31 | `"                    \"url\": \"https://example.org/research\","` | — |
| [SRC-62DC597310-L000032](../../tests/test_live_search_connectors.py#L32) | 32 | `"                    \"description\": \"A substantive search result.\","` | — |
| [SRC-62DC597310-L000033](../../tests/test_live_search_connectors.py#L33) | 33 | `"                    \"page_age\": \"October 10, 2026\","` | — |
| [SRC-62DC597310-L000034](../../tests/test_live_search_connectors.py#L34) | 34 | `"                }]"` | — |
| [SRC-62DC597310-L000035](../../tests/test_live_search_connectors.py#L35) | 35 | `"            }"` | — |
| [SRC-62DC597310-L000036](../../tests/test_live_search_connectors.py#L36) | 36 | `"        })"` | — |
| [SRC-62DC597310-L000037](../../tests/test_live_search_connectors.py#L37) | 37 | `""` | — |
| [SRC-62DC597310-L000038](../../tests/test_live_search_connectors.py#L38) | 38 | `"    monkeypatch.setattr(httpx, \"get\", fake_get)"` | — |
| [SRC-62DC597310-L000039](../../tests/test_live_search_connectors.py#L39) | 39 | `"    rows = WebAgent()._search_brave(\"بحث حديث\")"` | — |
| [SRC-62DC597310-L000040](../../tests/test_live_search_connectors.py#L40) | 40 | `"    assert requested[\"url\"] == \"https://api.search.brave.com/res/v1/web/search\""` | — |
| [SRC-62DC597310-L000041](../../tests/test_live_search_connectors.py#L41) | 41 | `"    assert requested[\"headers\"][\"X-Subscription-Token\"] == \"unit-test-secret\""` | — |
| [SRC-62DC597310-L000042](../../tests/test_live_search_connectors.py#L42) | 42 | `"    assert requested[\"params\"][\"country\"] == \"EG\""` | — |
| [SRC-62DC597310-L000043](../../tests/test_live_search_connectors.py#L43) | 43 | `"    assert rows[0][\"provider\"] == \"brave_search_api\""` | — |
| [SRC-62DC597310-L000044](../../tests/test_live_search_connectors.py#L44) | 44 | `"    assert rows[0][\"published_at\"] == \"October 10, 2026\""` | — |
| [SRC-62DC597310-L000045](../../tests/test_live_search_connectors.py#L45) | 45 | `"    assert \"unit-test-secret\" not in str(rows)"` | — |
| [SRC-62DC597310-L000046](../../tests/test_live_search_connectors.py#L46) | 46 | `""` | — |
| [SRC-62DC597310-L000047](../../tests/test_live_search_connectors.py#L47) | 47 | `""` | — |
| [SRC-62DC597310-L000048](../../tests/test_live_search_connectors.py#L48) | 48 | `"def test_tavily_search_adapter_normalizes_live_search_results(monkeypatch):"` | — |
| [SRC-62DC597310-L000049](../../tests/test_live_search_connectors.py#L49) | 49 | `"    monkeypatch.setenv(\"TAVILY_API_KEY\", \"unit-test-tavily-secret\")"` | — |
| [SRC-62DC597310-L000050](../../tests/test_live_search_connectors.py#L50) | 50 | `"    requested = {}"` | — |
| [SRC-62DC597310-L000051](../../tests/test_live_search_connectors.py#L51) | 51 | `""` | — |
| [SRC-62DC597310-L000052](../../tests/test_live_search_connectors.py#L52) | 52 | `"    def fake_post(url, **kwargs):"` | — |
| [SRC-62DC597310-L000053](../../tests/test_live_search_connectors.py#L53) | 53 | `"        requested[\"url\"] = url"` | — |
| [SRC-62DC597310-L000054](../../tests/test_live_search_connectors.py#L54) | 54 | `"        requested.update(kwargs)"` | — |
| [SRC-62DC597310-L000055](../../tests/test_live_search_connectors.py#L55) | 55 | `"        return FakeResponse({"` | — |
| [SRC-62DC597310-L000056](../../tests/test_live_search_connectors.py#L56) | 56 | `"            \"results\": [{"` | — |
| [SRC-62DC597310-L000057](../../tests/test_live_search_connectors.py#L57) | 57 | `"                \"title\": \"Official report\","` | — |
| [SRC-62DC597310-L000058](../../tests/test_live_search_connectors.py#L58) | 58 | `"                \"url\": \"https://example.org/report\","` | — |
| [SRC-62DC597310-L000059](../../tests/test_live_search_connectors.py#L59) | 59 | `"                \"content\": \"A source excerpt from the search response.\","` | — |
| [SRC-62DC597310-L000060](../../tests/test_live_search_connectors.py#L60) | 60 | `"                \"published_date\": \"2026-10-11\","` | — |
| [SRC-62DC597310-L000061](../../tests/test_live_search_connectors.py#L61) | 61 | `"            }]"` | — |
| [SRC-62DC597310-L000062](../../tests/test_live_search_connectors.py#L62) | 62 | `"        })"` | — |
| [SRC-62DC597310-L000063](../../tests/test_live_search_connectors.py#L63) | 63 | `""` | — |
| [SRC-62DC597310-L000064](../../tests/test_live_search_connectors.py#L64) | 64 | `"    monkeypatch.setattr(httpx, \"post\", fake_post)"` | — |
| [SRC-62DC597310-L000065](../../tests/test_live_search_connectors.py#L65) | 65 | `"    rows = WebAgent()._search_tavily(\"official sources report\")"` | — |
| [SRC-62DC597310-L000066](../../tests/test_live_search_connectors.py#L66) | 66 | `"    assert requested[\"url\"] == \"https://api.tavily.com/search\""` | — |
| [SRC-62DC597310-L000067](../../tests/test_live_search_connectors.py#L67) | 67 | `"    assert requested[\"json\"][\"api_key\"] == \"unit-test-tavily-secret\""` | — |
| [SRC-62DC597310-L000068](../../tests/test_live_search_connectors.py#L68) | 68 | `"    assert requested[\"json\"][\"include_answer\"] is False"` | — |
| [SRC-62DC597310-L000069](../../tests/test_live_search_connectors.py#L69) | 69 | `"    assert rows[0][\"provider\"] == \"tavily_search_api\""` | — |
| [SRC-62DC597310-L000070](../../tests/test_live_search_connectors.py#L70) | 70 | `"    assert rows[0][\"snippet\"].startswith(\"A source excerpt\")"` | — |
| [SRC-62DC597310-L000071](../../tests/test_live_search_connectors.py#L71) | 71 | `"    assert \"unit-test-tavily-secret\" not in str(rows)"` | — |
| [SRC-62DC597310-L000072](../../tests/test_live_search_connectors.py#L72) | 72 | `""` | — |
| [SRC-62DC597310-L000073](../../tests/test_live_search_connectors.py#L73) | 73 | `""` | — |
| [SRC-62DC597310-L000074](../../tests/test_live_search_connectors.py#L74) | 74 | `"def test_search_api_setup_status_reports_only_presence_not_secret_values(monkeypatch):"` | — |
| [SRC-62DC597310-L000075](../../tests/test_live_search_connectors.py#L75) | 75 | `"    monkeypatch.setenv(\"BRAVE_SEARCH_API_KEY\", \"brave-secret\")"` | — |
| [SRC-62DC597310-L000076](../../tests/test_live_search_connectors.py#L76) | 76 | `"    monkeypatch.setenv(\"TAVILY_API_KEY\", \"tavily-secret\")"` | — |
| [SRC-62DC597310-L000077](../../tests/test_live_search_connectors.py#L77) | 77 | `"    status = WebAgent.status()"` | — |
| [SRC-62DC597310-L000078](../../tests/test_live_search_connectors.py#L78) | 78 | `"    assert status[\"brave_search_api_configured\"] is True"` | — |
| [SRC-62DC597310-L000079](../../tests/test_live_search_connectors.py#L79) | 79 | `"    assert status[\"tavily_search_api_configured\"] is True"` | — |
| [SRC-62DC597310-L000080](../../tests/test_live_search_connectors.py#L80) | 80 | `"    assert \"brave-secret\" not in str(status)"` | — |
| [SRC-62DC597310-L000081](../../tests/test_live_search_connectors.py#L81) | 81 | `"    assert \"tavily-secret\" not in str(status)"` | — |
## اختبارات

### FILE-1521F490CA — [tests/test_multitenant.py](../../tests/test_multitenant.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1521F490CA-L000001](../../tests/test_multitenant.py#L1) | 1 | `"\"\"\"Tenant isolation, migration, and scoped export regression tests.\"\"\""` | — |
| [SRC-1521F490CA-L000002](../../tests/test_multitenant.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-1521F490CA-L000003](../../tests/test_multitenant.py#L3) | 3 | `""` | — |
| [SRC-1521F490CA-L000004](../../tests/test_multitenant.py#L4) | 4 | `"import csv"` | — |
| [SRC-1521F490CA-L000005](../../tests/test_multitenant.py#L5) | 5 | `"import hashlib"` | — |
| [SRC-1521F490CA-L000006](../../tests/test_multitenant.py#L6) | 6 | `"import sqlite3"` | — |
| [SRC-1521F490CA-L000007](../../tests/test_multitenant.py#L7) | 7 | `""` | — |
| [SRC-1521F490CA-L000008](../../tests/test_multitenant.py#L8) | 8 | `"from agents.omarai import DEFAULT_TENANT_ID, LeadStore, normalize"` | — |
| [SRC-1521F490CA-L000009](../../tests/test_multitenant.py#L9) | 9 | `""` | — |
| [SRC-1521F490CA-L000010](../../tests/test_multitenant.py#L10) | 10 | `""` | — |
| [SRC-1521F490CA-L000011](../../tests/test_multitenant.py#L11) | 11 | `"def _tenant_member(store: LeadStore, name: str, email: str, token: str):"` | — |
| [SRC-1521F490CA-L000012](../../tests/test_multitenant.py#L12) | 12 | `"    tenant_id = store.create_tenant(name, name.casefold())"` | — |
| [SRC-1521F490CA-L000013](../../tests/test_multitenant.py#L13) | 13 | `"    user_id = store.create_user(email, name + \" User\")"` | — |
| [SRC-1521F490CA-L000014](../../tests/test_multitenant.py#L14) | 14 | `"    store.add_membership(tenant_id, user_id, \"sales_agent\")"` | — |
| [SRC-1521F490CA-L000015](../../tests/test_multitenant.py#L15) | 15 | `"    store.create_api_token(token, tenant_id, user_id, label=name)"` | — |
| [SRC-1521F490CA-L000016](../../tests/test_multitenant.py#L16) | 16 | `"    return tenant_id, user_id"` | — |
| [SRC-1521F490CA-L000017](../../tests/test_multitenant.py#L17) | 17 | `""` | — |
| [SRC-1521F490CA-L000018](../../tests/test_multitenant.py#L18) | 18 | `""` | — |
| [SRC-1521F490CA-L000019](../../tests/test_multitenant.py#L19) | 19 | `"def test_tenant_scoped_fingerprints_reads_updates_and_exports(tmp_path):"` | — |
| [SRC-1521F490CA-L000020](../../tests/test_multitenant.py#L20) | 20 | `"    store = LeadStore(tmp_path / \"multi.sqlite3\")"` | — |
| [SRC-1521F490CA-L000021](../../tests/test_multitenant.py#L21) | 21 | `"    tenant_a, _, = _tenant_member("` | — |
| [SRC-1521F490CA-L000022](../../tests/test_multitenant.py#L22) | 22 | `"        store, \"Company A\", \"a@example.test\", \"A\" * 40"` | — |
| [SRC-1521F490CA-L000023](../../tests/test_multitenant.py#L23) | 23 | `"    )"` | — |
| [SRC-1521F490CA-L000024](../../tests/test_multitenant.py#L24) | 24 | `"    tenant_b, _, = _tenant_member("` | — |
| [SRC-1521F490CA-L000025](../../tests/test_multitenant.py#L25) | 25 | `"        store, \"Company B\", \"b@example.test\", \"B\" * 40"` | — |
| [SRC-1521F490CA-L000026](../../tests/test_multitenant.py#L26) | 26 | `"    )"` | — |
| [SRC-1521F490CA-L000027](../../tests/test_multitenant.py#L27) | 27 | `""` | — |
| [SRC-1521F490CA-L000028](../../tests/test_multitenant.py#L28) | 28 | `"    payload = (\"Buyer asks to purchase a product\", \"https://example.test/post/1\")"` | — |
| [SRC-1521F490CA-L000029](../../tests/test_multitenant.py#L29) | 29 | `"    lead_a, created_a = store.add("` | — |
| [SRC-1521F490CA-L000030](../../tests/test_multitenant.py#L30) | 30 | `"        *payload, tenant_id=tenant_a"` | — |
| [SRC-1521F490CA-L000031](../../tests/test_multitenant.py#L31) | 31 | `"    )"` | — |
| [SRC-1521F490CA-L000032](../../tests/test_multitenant.py#L32) | 32 | `"    lead_b, created_b = store.add("` | — |
| [SRC-1521F490CA-L000033](../../tests/test_multitenant.py#L33) | 33 | `"        *payload, tenant_id=tenant_b"` | — |
| [SRC-1521F490CA-L000034](../../tests/test_multitenant.py#L34) | 34 | `"    )"` | — |
| [SRC-1521F490CA-L000035](../../tests/test_multitenant.py#L35) | 35 | `""` | — |
| [SRC-1521F490CA-L000036](../../tests/test_multitenant.py#L36) | 36 | `"    assert created_a is True"` | — |
| [SRC-1521F490CA-L000037](../../tests/test_multitenant.py#L37) | 37 | `"    assert created_b is True"` | — |
| [SRC-1521F490CA-L000038](../../tests/test_multitenant.py#L38) | 38 | `"    assert lead_a[\"id\"] != lead_b[\"id\"]"` | — |
| [SRC-1521F490CA-L000039](../../tests/test_multitenant.py#L39) | 39 | `"    assert lead_a[\"tenant_id\"] == tenant_a"` | — |
| [SRC-1521F490CA-L000040](../../tests/test_multitenant.py#L40) | 40 | `"    assert lead_b[\"tenant_id\"] == tenant_b"` | — |
| [SRC-1521F490CA-L000041](../../tests/test_multitenant.py#L41) | 41 | `"    assert [row[\"id\"] for row in store.list(tenant_id=tenant_a)] == [lead_a[\"id\"]]"` | — |
| [SRC-1521F490CA-L000042](../../tests/test_multitenant.py#L42) | 42 | `"    assert [row[\"id\"] for row in store.list(tenant_id=tenant_b)] == [lead_b[\"id\"]]"` | — |
| [SRC-1521F490CA-L000043](../../tests/test_multitenant.py#L43) | 43 | `""` | — |
| [SRC-1521F490CA-L000044](../../tests/test_multitenant.py#L44) | 44 | `"    assert store.update_status("` | — |
| [SRC-1521F490CA-L000045](../../tests/test_multitenant.py#L45) | 45 | `"        lead_b[\"id\"], \"qualified\", tenant_id=tenant_a"` | — |
| [SRC-1521F490CA-L000046](../../tests/test_multitenant.py#L46) | 46 | `"    ) is None"` | — |
| [SRC-1521F490CA-L000047](../../tests/test_multitenant.py#L47) | 47 | `"    updated_b = store.update_status("` | — |
| [SRC-1521F490CA-L000048](../../tests/test_multitenant.py#L48) | 48 | `"        lead_b[\"id\"], \"qualified\", tenant_id=tenant_b"` | — |
| [SRC-1521F490CA-L000049](../../tests/test_multitenant.py#L49) | 49 | `"    )"` | — |
| [SRC-1521F490CA-L000050](../../tests/test_multitenant.py#L50) | 50 | `"    assert updated_b is not None"` | — |
| [SRC-1521F490CA-L000051](../../tests/test_multitenant.py#L51) | 51 | `"    assert updated_b[\"status\"] == \"qualified\""` | — |
| [SRC-1521F490CA-L000052](../../tests/test_multitenant.py#L52) | 52 | `""` | — |
| [SRC-1521F490CA-L000053](../../tests/test_multitenant.py#L53) | 53 | `"    export_path = tmp_path / \"company-a.csv\""` | — |
| [SRC-1521F490CA-L000054](../../tests/test_multitenant.py#L54) | 54 | `"    assert store.export_csv(export_path, tenant_id=tenant_a) == 1"` | — |
| [SRC-1521F490CA-L000055](../../tests/test_multitenant.py#L55) | 55 | `"    with export_path.open(newline=\"\", encoding=\"utf-8-sig\") as stream:"` | — |
| [SRC-1521F490CA-L000056](../../tests/test_multitenant.py#L56) | 56 | `"        rows = list(csv.DictReader(stream))"` | — |
| [SRC-1521F490CA-L000057](../../tests/test_multitenant.py#L57) | 57 | `"    assert len(rows) == 1"` | — |
| [SRC-1521F490CA-L000058](../../tests/test_multitenant.py#L58) | 58 | `"    assert rows[0][\"tenant_id\"] == tenant_a"` | — |
| [SRC-1521F490CA-L000059](../../tests/test_multitenant.py#L59) | 59 | `"    assert rows[0][\"id\"] == lead_a[\"id\"]"` | — |
| [SRC-1521F490CA-L000060](../../tests/test_multitenant.py#L60) | 60 | `""` | — |
| [SRC-1521F490CA-L000061](../../tests/test_multitenant.py#L61) | 61 | `""` | — |
| [SRC-1521F490CA-L000062](../../tests/test_multitenant.py#L62) | 62 | `"def test_api_tokens_resolve_only_active_tenant_memberships(tmp_path):"` | — |
| [SRC-1521F490CA-L000063](../../tests/test_multitenant.py#L63) | 63 | `"    store = LeadStore(tmp_path / \"tokens.sqlite3\")"` | — |
| [SRC-1521F490CA-L000064](../../tests/test_multitenant.py#L64) | 64 | `"    tenant_id, user_id = _tenant_member("` | — |
| [SRC-1521F490CA-L000065](../../tests/test_multitenant.py#L65) | 65 | `"        store, \"Company\", \"owner@example.test\", \"C\" * 40"` | — |
| [SRC-1521F490CA-L000066](../../tests/test_multitenant.py#L66) | 66 | `"    )"` | — |
| [SRC-1521F490CA-L000067](../../tests/test_multitenant.py#L67) | 67 | `""` | — |
| [SRC-1521F490CA-L000068](../../tests/test_multitenant.py#L68) | 68 | `"    principal = store.resolve_api_token(\"C\" * 40)"` | — |
| [SRC-1521F490CA-L000069](../../tests/test_multitenant.py#L69) | 69 | `"    assert principal == {"` | — |
| [SRC-1521F490CA-L000070](../../tests/test_multitenant.py#L70) | 70 | `"        \"tenant_id\": tenant_id,"` | — |
| [SRC-1521F490CA-L000071](../../tests/test_multitenant.py#L71) | 71 | `"        \"user_id\": user_id,"` | — |
| [SRC-1521F490CA-L000072](../../tests/test_multitenant.py#L72) | 72 | `"        \"role\": \"sales_agent\","` | — |
| [SRC-1521F490CA-L000073](../../tests/test_multitenant.py#L73) | 73 | `"    }"` | — |
| [SRC-1521F490CA-L000074](../../tests/test_multitenant.py#L74) | 74 | `"    assert store.resolve_api_token(\"X\" * 40) is None"` | — |
| [SRC-1521F490CA-L000075](../../tests/test_multitenant.py#L75) | 75 | `""` | — |
| [SRC-1521F490CA-L000076](../../tests/test_multitenant.py#L76) | 76 | `"    with store.connect() as db:"` | — |
| [SRC-1521F490CA-L000077](../../tests/test_multitenant.py#L77) | 77 | `"        db.execute("` | — |
| [SRC-1521F490CA-L000078](../../tests/test_multitenant.py#L78) | 78 | `"            \"UPDATE tenant_memberships SET active=0 WHERE tenant_id=? AND user_id=?\","` | — |
| [SRC-1521F490CA-L000079](../../tests/test_multitenant.py#L79) | 79 | `"            (tenant_id, user_id),"` | — |
| [SRC-1521F490CA-L000080](../../tests/test_multitenant.py#L80) | 80 | `"        )"` | — |
| [SRC-1521F490CA-L000081](../../tests/test_multitenant.py#L81) | 81 | `"    assert store.resolve_api_token(\"C\" * 40) is None"` | — |
| [SRC-1521F490CA-L000082](../../tests/test_multitenant.py#L82) | 82 | `""` | — |
| [SRC-1521F490CA-L000083](../../tests/test_multitenant.py#L83) | 83 | `""` | — |
| [SRC-1521F490CA-L000084](../../tests/test_multitenant.py#L84) | 84 | `"def test_legacy_single_company_database_migrates_without_losing_leads(tmp_path):"` | — |
| [SRC-1521F490CA-L000085](../../tests/test_multitenant.py#L85) | 85 | `"    path = tmp_path / \"legacy.sqlite3\""` | — |
| [SRC-1521F490CA-L000086](../../tests/test_multitenant.py#L86) | 86 | `"    legacy_text = \"Old lead\""` | — |
| [SRC-1521F490CA-L000087](../../tests/test_multitenant.py#L87) | 87 | `"    legacy_url = \"https://example.test/legacy\""` | — |
| [SRC-1521F490CA-L000088](../../tests/test_multitenant.py#L88) | 88 | `"    legacy_fingerprint = hashlib.sha256("` | — |
| [SRC-1521F490CA-L000089](../../tests/test_multitenant.py#L89) | 89 | `"        (legacy_url.rstrip(\"/\") + \"\\n\" + normalize(legacy_text)).encode()"` | — |
| [SRC-1521F490CA-L000090](../../tests/test_multitenant.py#L90) | 90 | `"    ).hexdigest()"` | — |
| [SRC-1521F490CA-L000091](../../tests/test_multitenant.py#L91) | 91 | `"    with sqlite3.connect(path) as db:"` | — |
| [SRC-1521F490CA-L000092](../../tests/test_multitenant.py#L92) | 92 | `"        db.execute("` | — |
| [SRC-1521F490CA-L000093](../../tests/test_multitenant.py#L93) | 93 | `"            \"\"\"CREATE TABLE leads ("` | — |
| [SRC-1521F490CA-L000094](../../tests/test_multitenant.py#L94) | 94 | `"                id TEXT PRIMARY KEY,"` | — |
| [SRC-1521F490CA-L000095](../../tests/test_multitenant.py#L95) | 95 | `"                fingerprint TEXT UNIQUE NOT NULL,"` | — |
| [SRC-1521F490CA-L000096](../../tests/test_multitenant.py#L96) | 96 | `"                text TEXT NOT NULL,"` | — |
| [SRC-1521F490CA-L000097](../../tests/test_multitenant.py#L97) | 97 | `"                source_url TEXT NOT NULL,"` | — |
| [SRC-1521F490CA-L000098](../../tests/test_multitenant.py#L98) | 98 | `"                platform TEXT NOT NULL,"` | — |
| [SRC-1521F490CA-L000099](../../tests/test_multitenant.py#L99) | 99 | `"                observed_at TEXT NOT NULL,"` | — |
| [SRC-1521F490CA-L000100](../../tests/test_multitenant.py#L100) | 100 | `"                assessment TEXT NOT NULL,"` | — |
| [SRC-1521F490CA-L000101](../../tests/test_multitenant.py#L101) | 101 | `"                status TEXT NOT NULL,"` | — |
| [SRC-1521F490CA-L000102](../../tests/test_multitenant.py#L102) | 102 | `"                note TEXT NOT NULL,"` | — |
| [SRC-1521F490CA-L000103](../../tests/test_multitenant.py#L103) | 103 | `"                created_at TEXT NOT NULL,"` | — |
| [SRC-1521F490CA-L000104](../../tests/test_multitenant.py#L104) | 104 | `"                updated_at TEXT NOT NULL"` | — |
| [SRC-1521F490CA-L000105](../../tests/test_multitenant.py#L105) | 105 | `"            )\"\"\""` | — |
| [SRC-1521F490CA-L000106](../../tests/test_multitenant.py#L106) | 106 | `"        )"` | — |
| [SRC-1521F490CA-L000107](../../tests/test_multitenant.py#L107) | 107 | `"        db.execute("` | — |
| [SRC-1521F490CA-L000108](../../tests/test_multitenant.py#L108) | 108 | `"            \"\"\"INSERT INTO leads VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)\"\"\","` | — |
| [SRC-1521F490CA-L000109](../../tests/test_multitenant.py#L109) | 109 | `"            ("` | — |
| [SRC-1521F490CA-L000110](../../tests/test_multitenant.py#L110) | 110 | `"                \"legacy-lead\", legacy_fingerprint, legacy_text,"` | — |
| [SRC-1521F490CA-L000111](../../tests/test_multitenant.py#L111) | 111 | `"                legacy_url, \"manual\", \"2026-10-30T00:00:00Z\","` | — |
| [SRC-1521F490CA-L000112](../../tests/test_multitenant.py#L112) | 112 | `"                '{\"score\": 0}', \"new\", \"\", \"2026-10-30T00:00:00Z\","` | — |
| [SRC-1521F490CA-L000113](../../tests/test_multitenant.py#L113) | 113 | `"                \"2026-10-30T00:00:00Z\","` | — |
| [SRC-1521F490CA-L000114](../../tests/test_multitenant.py#L114) | 114 | `"            ),"` | — |
| [SRC-1521F490CA-L000115](../../tests/test_multitenant.py#L115) | 115 | `"        )"` | — |
| [SRC-1521F490CA-L000116](../../tests/test_multitenant.py#L116) | 116 | `""` | — |
| [SRC-1521F490CA-L000117](../../tests/test_multitenant.py#L117) | 117 | `"    store = LeadStore(path)"` | — |
| [SRC-1521F490CA-L000118](../../tests/test_multitenant.py#L118) | 118 | `"    leads = store.list(tenant_id=DEFAULT_TENANT_ID)"` | — |
| [SRC-1521F490CA-L000119](../../tests/test_multitenant.py#L119) | 119 | `"    assert len(leads) == 1"` | — |
| [SRC-1521F490CA-L000120](../../tests/test_multitenant.py#L120) | 120 | `"    assert leads[0][\"id\"] == \"legacy-lead\""` | — |
| [SRC-1521F490CA-L000121](../../tests/test_multitenant.py#L121) | 121 | `"    assert leads[0][\"tenant_id\"] == DEFAULT_TENANT_ID"` | — |
| [SRC-1521F490CA-L000122](../../tests/test_multitenant.py#L122) | 122 | `""` | — |
| [SRC-1521F490CA-L000123](../../tests/test_multitenant.py#L123) | 123 | `"    duplicate, created = store.add("` | — |
| [SRC-1521F490CA-L000124](../../tests/test_multitenant.py#L124) | 124 | `"        \"Old lead\", \"https://example.test/legacy\", tenant_id=DEFAULT_TENANT_ID"` | — |
| [SRC-1521F490CA-L000125](../../tests/test_multitenant.py#L125) | 125 | `"    )"` | — |
| [SRC-1521F490CA-L000126](../../tests/test_multitenant.py#L126) | 126 | `"    assert created is False"` | — |
| [SRC-1521F490CA-L000127](../../tests/test_multitenant.py#L127) | 127 | `"    assert duplicate[\"id\"] == \"legacy-lead\""` | — |
| [SRC-1521F490CA-L000128](../../tests/test_multitenant.py#L128) | 128 | `""` | — |
| [SRC-1521F490CA-L000129](../../tests/test_multitenant.py#L129) | 129 | `"    with store.connect() as db:"` | — |
| [SRC-1521F490CA-L000130](../../tests/test_multitenant.py#L130) | 130 | `"        columns = {row[\"name\"] for row in db.execute(\"PRAGMA table_info(leads)\")}"` | — |
| [SRC-1521F490CA-L000131](../../tests/test_multitenant.py#L131) | 131 | `"        unique_indexes = ["` | — |
| [SRC-1521F490CA-L000132](../../tests/test_multitenant.py#L132) | 132 | `"            row[\"name\"] for row in db.execute(\"PRAGMA index_list(leads)\")"` | — |
| [SRC-1521F490CA-L000133](../../tests/test_multitenant.py#L133) | 133 | `"            if row[\"unique\"]"` | — |
| [SRC-1521F490CA-L000134](../../tests/test_multitenant.py#L134) | 134 | `"        ]"` | — |
| [SRC-1521F490CA-L000135](../../tests/test_multitenant.py#L135) | 135 | `"        unique_columns = ["` | — |
| [SRC-1521F490CA-L000136](../../tests/test_multitenant.py#L136) | 136 | `"            ["` | — |
| [SRC-1521F490CA-L000137](../../tests/test_multitenant.py#L137) | 137 | `"                item[\"name\"]"` | — |
| [SRC-1521F490CA-L000138](../../tests/test_multitenant.py#L138) | 138 | `"                for item in db.execute(f\"PRAGMA index_info('{index_name}')\")"` | — |
| [SRC-1521F490CA-L000139](../../tests/test_multitenant.py#L139) | 139 | `"            ]"` | — |
| [SRC-1521F490CA-L000140](../../tests/test_multitenant.py#L140) | 140 | `"            for index_name in unique_indexes"` | — |
| [SRC-1521F490CA-L000141](../../tests/test_multitenant.py#L141) | 141 | `"        ]"` | — |
| [SRC-1521F490CA-L000142](../../tests/test_multitenant.py#L142) | 142 | `"    assert \"tenant_id\" in columns"` | — |
| [SRC-1521F490CA-L000143](../../tests/test_multitenant.py#L143) | 143 | `"    assert [\"fingerprint\"] not in unique_columns"` | — |
| [SRC-1521F490CA-L000144](../../tests/test_multitenant.py#L144) | 144 | `"    assert [\"tenant_id\", \"fingerprint\"] in unique_columns"` | — |
## اختبارات

### FILE-4405E7912C — [tests/test_multitenant_api.py](../../tests/test_multitenant_api.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-4405E7912C-L000001](../../tests/test_multitenant_api.py#L1) | 1 | `"\"\"\"HTTP-level tenant authorization regression tests.\"\"\""` | — |
| [SRC-4405E7912C-L000002](../../tests/test_multitenant_api.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-4405E7912C-L000003](../../tests/test_multitenant_api.py#L3) | 3 | `""` | — |
| [SRC-4405E7912C-L000004](../../tests/test_multitenant_api.py#L4) | 4 | `"import json"` | — |
| [SRC-4405E7912C-L000005](../../tests/test_multitenant_api.py#L5) | 5 | `"import threading"` | — |
| [SRC-4405E7912C-L000006](../../tests/test_multitenant_api.py#L6) | 6 | `"from http.server import ThreadingHTTPServer"` | — |
| [SRC-4405E7912C-L000007](../../tests/test_multitenant_api.py#L7) | 7 | `"from urllib.error import HTTPError"` | — |
| [SRC-4405E7912C-L000008](../../tests/test_multitenant_api.py#L8) | 8 | `"from urllib.request import Request, urlopen"` | — |
| [SRC-4405E7912C-L000009](../../tests/test_multitenant_api.py#L9) | 9 | `""` | — |
| [SRC-4405E7912C-L000010](../../tests/test_multitenant_api.py#L10) | 10 | `"import pytest"` | — |
| [SRC-4405E7912C-L000011](../../tests/test_multitenant_api.py#L11) | 11 | `""` | — |
| [SRC-4405E7912C-L000012](../../tests/test_multitenant_api.py#L12) | 12 | `"from agents.omarai import LeadStore"` | — |
| [SRC-4405E7912C-L000013](../../tests/test_multitenant_api.py#L13) | 13 | `"from api.omarai import Handler"` | — |
| [SRC-4405E7912C-L000014](../../tests/test_multitenant_api.py#L14) | 14 | `""` | — |
| [SRC-4405E7912C-L000015](../../tests/test_multitenant_api.py#L15) | 15 | `""` | — |
| [SRC-4405E7912C-L000016](../../tests/test_multitenant_api.py#L16) | 16 | `"@pytest.fixture"` | — |
| [SRC-4405E7912C-L000017](../../tests/test_multitenant_api.py#L17) | 17 | `"def tenant_api(tmp_path, monkeypatch):"` | — |
| [SRC-4405E7912C-L000018](../../tests/test_multitenant_api.py#L18) | 18 | `"    monkeypatch.setenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"1\")"` | — |
| [SRC-4405E7912C-L000019](../../tests/test_multitenant_api.py#L19) | 19 | `"    monkeypatch.delenv(\"OMARAI_ACCESS_TOKEN\", raising=False)"` | — |
| [SRC-4405E7912C-L000020](../../tests/test_multitenant_api.py#L20) | 20 | `"    previous_store = Handler.store"` | — |
| [SRC-4405E7912C-L000021](../../tests/test_multitenant_api.py#L21) | 21 | `"    Handler.store = LeadStore(tmp_path / \"tenant-api.sqlite3\")"` | — |
| [SRC-4405E7912C-L000022](../../tests/test_multitenant_api.py#L22) | 22 | `"    server = ThreadingHTTPServer((\"127.0.0.1\", 0), Handler)"` | — |
| [SRC-4405E7912C-L000023](../../tests/test_multitenant_api.py#L23) | 23 | `"    thread = threading.Thread(target=server.serve_forever, daemon=True)"` | — |
| [SRC-4405E7912C-L000024](../../tests/test_multitenant_api.py#L24) | 24 | `"    thread.start()"` | — |
| [SRC-4405E7912C-L000025](../../tests/test_multitenant_api.py#L25) | 25 | `"    try:"` | — |
| [SRC-4405E7912C-L000026](../../tests/test_multitenant_api.py#L26) | 26 | `"        yield f\"http://127.0.0.1:{server.server_port}\", Handler.store"` | — |
| [SRC-4405E7912C-L000027](../../tests/test_multitenant_api.py#L27) | 27 | `"    finally:"` | — |
| [SRC-4405E7912C-L000028](../../tests/test_multitenant_api.py#L28) | 28 | `"        server.shutdown()"` | — |
| [SRC-4405E7912C-L000029](../../tests/test_multitenant_api.py#L29) | 29 | `"        server.server_close()"` | — |
| [SRC-4405E7912C-L000030](../../tests/test_multitenant_api.py#L30) | 30 | `"        thread.join(timeout=3)"` | — |
| [SRC-4405E7912C-L000031](../../tests/test_multitenant_api.py#L31) | 31 | `"        Handler.store = previous_store"` | — |
| [SRC-4405E7912C-L000032](../../tests/test_multitenant_api.py#L32) | 32 | `""` | — |
| [SRC-4405E7912C-L000033](../../tests/test_multitenant_api.py#L33) | 33 | `""` | — |
| [SRC-4405E7912C-L000034](../../tests/test_multitenant_api.py#L34) | 34 | `"def request_json(base, path, *, method=\"GET\", payload=None, token=\"\"):"` | — |
| [SRC-4405E7912C-L000035](../../tests/test_multitenant_api.py#L35) | 35 | `"    body = None if payload is None else json.dumps(payload).encode(\"utf-8\")"` | — |
| [SRC-4405E7912C-L000036](../../tests/test_multitenant_api.py#L36) | 36 | `"    headers = {}"` | — |
| [SRC-4405E7912C-L000037](../../tests/test_multitenant_api.py#L37) | 37 | `"    if body is not None:"` | — |
| [SRC-4405E7912C-L000038](../../tests/test_multitenant_api.py#L38) | 38 | `"        headers[\"Content-Type\"] = \"application/json\""` | — |
| [SRC-4405E7912C-L000039](../../tests/test_multitenant_api.py#L39) | 39 | `"    if token:"` | — |
| [SRC-4405E7912C-L000040](../../tests/test_multitenant_api.py#L40) | 40 | `"        headers[\"Authorization\"] = \"Bearer \" + token"` | — |
| [SRC-4405E7912C-L000041](../../tests/test_multitenant_api.py#L41) | 41 | `"    request = Request(base + path, data=body, method=method, headers=headers)"` | — |
| [SRC-4405E7912C-L000042](../../tests/test_multitenant_api.py#L42) | 42 | `"    try:"` | — |
| [SRC-4405E7912C-L000043](../../tests/test_multitenant_api.py#L43) | 43 | `"        with urlopen(request, timeout=3) as response:"` | — |
| [SRC-4405E7912C-L000044](../../tests/test_multitenant_api.py#L44) | 44 | `"            return response.status, json.loads(response.read().decode(\"utf-8\"))"` | — |
| [SRC-4405E7912C-L000045](../../tests/test_multitenant_api.py#L45) | 45 | `"    except HTTPError as error:"` | — |
| [SRC-4405E7912C-L000046](../../tests/test_multitenant_api.py#L46) | 46 | `"        return error.code, json.loads(error.read().decode(\"utf-8\"))"` | — |
| [SRC-4405E7912C-L000047](../../tests/test_multitenant_api.py#L47) | 47 | `""` | — |
| [SRC-4405E7912C-L000048](../../tests/test_multitenant_api.py#L48) | 48 | `""` | — |
| [SRC-4405E7912C-L000049](../../tests/test_multitenant_api.py#L49) | 49 | `"def _tenant(store, name, email, token):"` | — |
| [SRC-4405E7912C-L000050](../../tests/test_multitenant_api.py#L50) | 50 | `"    tenant_id = store.create_tenant(name, name.casefold())"` | — |
| [SRC-4405E7912C-L000051](../../tests/test_multitenant_api.py#L51) | 51 | `"    user_id = store.create_user(email, name + \" User\")"` | — |
| [SRC-4405E7912C-L000052](../../tests/test_multitenant_api.py#L52) | 52 | `"    store.add_membership(tenant_id, user_id, \"sales_agent\")"` | — |
| [SRC-4405E7912C-L000053](../../tests/test_multitenant_api.py#L53) | 53 | `"    store.create_api_token(token, tenant_id, user_id, label=name)"` | — |
| [SRC-4405E7912C-L000054](../../tests/test_multitenant_api.py#L54) | 54 | `"    return tenant_id"` | — |
| [SRC-4405E7912C-L000055](../../tests/test_multitenant_api.py#L55) | 55 | `""` | — |
| [SRC-4405E7912C-L000056](../../tests/test_multitenant_api.py#L56) | 56 | `""` | — |
| [SRC-4405E7912C-L000057](../../tests/test_multitenant_api.py#L57) | 57 | `"def test_api_ignores_client_tenant_id_and_blocks_cross_tenant_reads_and_updates(tenant_api):"` | — |
| [SRC-4405E7912C-L000058](../../tests/test_multitenant_api.py#L58) | 58 | `"    base, store = tenant_api"` | — |
| [SRC-4405E7912C-L000059](../../tests/test_multitenant_api.py#L59) | 59 | `"    token_a = \"tenant-a-token-\" + \"A\" * 32"` | — |
| [SRC-4405E7912C-L000060](../../tests/test_multitenant_api.py#L60) | 60 | `"    token_b = \"tenant-b-token-\" + \"B\" * 32"` | — |
| [SRC-4405E7912C-L000061](../../tests/test_multitenant_api.py#L61) | 61 | `"    tenant_a = _tenant(store, \"Company A\", \"api-a@example.test\", token_a)"` | — |
| [SRC-4405E7912C-L000062](../../tests/test_multitenant_api.py#L62) | 62 | `"    tenant_b = _tenant(store, \"Company B\", \"api-b@example.test\", token_b)"` | — |
| [SRC-4405E7912C-L000063](../../tests/test_multitenant_api.py#L63) | 63 | `""` | — |
| [SRC-4405E7912C-L000064](../../tests/test_multitenant_api.py#L64) | 64 | `"    status, created_a = request_json("` | — |
| [SRC-4405E7912C-L000065](../../tests/test_multitenant_api.py#L65) | 65 | `"        base,"` | — |
| [SRC-4405E7912C-L000066](../../tests/test_multitenant_api.py#L66) | 66 | `"        \"/api/leads\","` | — |
| [SRC-4405E7912C-L000067](../../tests/test_multitenant_api.py#L67) | 67 | `"        method=\"POST\","` | — |
| [SRC-4405E7912C-L000068](../../tests/test_multitenant_api.py#L68) | 68 | `"        token=token_a,"` | — |
| [SRC-4405E7912C-L000069](../../tests/test_multitenant_api.py#L69) | 69 | `"        payload={"` | — |
| [SRC-4405E7912C-L000070](../../tests/test_multitenant_api.py#L70) | 70 | `"            \"tenant_id\": tenant_b,"` | — |
| [SRC-4405E7912C-L000071](../../tests/test_multitenant_api.py#L71) | 71 | `"            \"text\": \"Buyer A wants to purchase\","` | — |
| [SRC-4405E7912C-L000072](../../tests/test_multitenant_api.py#L72) | 72 | `"            \"source_url\": \"https://example.test/a\","` | — |
| [SRC-4405E7912C-L000073](../../tests/test_multitenant_api.py#L73) | 73 | `"            \"platform\": \"public\","` | — |
| [SRC-4405E7912C-L000074](../../tests/test_multitenant_api.py#L74) | 74 | `"        },"` | — |
| [SRC-4405E7912C-L000075](../../tests/test_multitenant_api.py#L75) | 75 | `"    )"` | — |
| [SRC-4405E7912C-L000076](../../tests/test_multitenant_api.py#L76) | 76 | `"    assert status == 201"` | — |
| [SRC-4405E7912C-L000077](../../tests/test_multitenant_api.py#L77) | 77 | `"    assert created_a[\"lead\"][\"tenant_id\"] == tenant_a"` | — |
| [SRC-4405E7912C-L000078](../../tests/test_multitenant_api.py#L78) | 78 | `""` | — |
| [SRC-4405E7912C-L000079](../../tests/test_multitenant_api.py#L79) | 79 | `"    status, created_b = request_json("` | — |
| [SRC-4405E7912C-L000080](../../tests/test_multitenant_api.py#L80) | 80 | `"        base,"` | — |
| [SRC-4405E7912C-L000081](../../tests/test_multitenant_api.py#L81) | 81 | `"        \"/api/leads\","` | — |
| [SRC-4405E7912C-L000082](../../tests/test_multitenant_api.py#L82) | 82 | `"        method=\"POST\","` | — |
| [SRC-4405E7912C-L000083](../../tests/test_multitenant_api.py#L83) | 83 | `"        token=token_b,"` | — |
| [SRC-4405E7912C-L000084](../../tests/test_multitenant_api.py#L84) | 84 | `"        payload={"` | — |
| [SRC-4405E7912C-L000085](../../tests/test_multitenant_api.py#L85) | 85 | `"            \"tenant_id\": tenant_a,"` | — |
| [SRC-4405E7912C-L000086](../../tests/test_multitenant_api.py#L86) | 86 | `"            \"text\": \"Buyer B wants to purchase\","` | — |
| [SRC-4405E7912C-L000087](../../tests/test_multitenant_api.py#L87) | 87 | `"            \"source_url\": \"https://example.test/b\","` | — |
| [SRC-4405E7912C-L000088](../../tests/test_multitenant_api.py#L88) | 88 | `"            \"platform\": \"public\","` | — |
| [SRC-4405E7912C-L000089](../../tests/test_multitenant_api.py#L89) | 89 | `"        },"` | — |
| [SRC-4405E7912C-L000090](../../tests/test_multitenant_api.py#L90) | 90 | `"    )"` | — |
| [SRC-4405E7912C-L000091](../../tests/test_multitenant_api.py#L91) | 91 | `"    assert status == 201"` | — |
| [SRC-4405E7912C-L000092](../../tests/test_multitenant_api.py#L92) | 92 | `"    assert created_b[\"lead\"][\"tenant_id\"] == tenant_b"` | — |
| [SRC-4405E7912C-L000093](../../tests/test_multitenant_api.py#L93) | 93 | `""` | — |
| [SRC-4405E7912C-L000094](../../tests/test_multitenant_api.py#L94) | 94 | `"    status, listing_a = request_json("` | — |
| [SRC-4405E7912C-L000095](../../tests/test_multitenant_api.py#L95) | 95 | `"        base, f\"/api/leads?tenant_id={tenant_b}\", token=token_a"` | — |
| [SRC-4405E7912C-L000096](../../tests/test_multitenant_api.py#L96) | 96 | `"    )"` | — |
| [SRC-4405E7912C-L000097](../../tests/test_multitenant_api.py#L97) | 97 | `"    assert status == 200"` | — |
| [SRC-4405E7912C-L000098](../../tests/test_multitenant_api.py#L98) | 98 | `"    assert [lead[\"id\"] for lead in listing_a[\"leads\"]] == [created_a[\"lead\"][\"id\"]]"` | — |
| [SRC-4405E7912C-L000099](../../tests/test_multitenant_api.py#L99) | 99 | `""` | — |
| [SRC-4405E7912C-L000100](../../tests/test_multitenant_api.py#L100) | 100 | `"    status, listing_b = request_json(base, \"/api/leads\", token=token_b)"` | — |
| [SRC-4405E7912C-L000101](../../tests/test_multitenant_api.py#L101) | 101 | `"    assert status == 200"` | — |
| [SRC-4405E7912C-L000102](../../tests/test_multitenant_api.py#L102) | 102 | `"    assert [lead[\"id\"] for lead in listing_b[\"leads\"]] == [created_b[\"lead\"][\"id\"]]"` | — |
| [SRC-4405E7912C-L000103](../../tests/test_multitenant_api.py#L103) | 103 | `""` | — |
| [SRC-4405E7912C-L000104](../../tests/test_multitenant_api.py#L104) | 104 | `"    status, denied = request_json("` | — |
| [SRC-4405E7912C-L000105](../../tests/test_multitenant_api.py#L105) | 105 | `"        base,"` | — |
| [SRC-4405E7912C-L000106](../../tests/test_multitenant_api.py#L106) | 106 | `"        f\"/api/leads/{created_b['lead']['id']}/status\","` | — |
| [SRC-4405E7912C-L000107](../../tests/test_multitenant_api.py#L107) | 107 | `"        method=\"POST\","` | — |
| [SRC-4405E7912C-L000108](../../tests/test_multitenant_api.py#L108) | 108 | `"        token=token_a,"` | — |
| [SRC-4405E7912C-L000109](../../tests/test_multitenant_api.py#L109) | 109 | `"        payload={\"status\": \"qualified\"},"` | — |
| [SRC-4405E7912C-L000110](../../tests/test_multitenant_api.py#L110) | 110 | `"    )"` | — |
| [SRC-4405E7912C-L000111](../../tests/test_multitenant_api.py#L111) | 111 | `"    assert status == 404"` | — |
| [SRC-4405E7912C-L000112](../../tests/test_multitenant_api.py#L112) | 112 | `"    assert denied[\"error\"] == \"lead not found\""` | — |
| [SRC-4405E7912C-L000113](../../tests/test_multitenant_api.py#L113) | 113 | `""` | — |
| [SRC-4405E7912C-L000114](../../tests/test_multitenant_api.py#L114) | 114 | `"    status, changed = request_json("` | — |
| [SRC-4405E7912C-L000115](../../tests/test_multitenant_api.py#L115) | 115 | `"        base,"` | — |
| [SRC-4405E7912C-L000116](../../tests/test_multitenant_api.py#L116) | 116 | `"        f\"/api/leads/{created_b['lead']['id']}/status\","` | — |
| [SRC-4405E7912C-L000117](../../tests/test_multitenant_api.py#L117) | 117 | `"        method=\"POST\","` | — |
| [SRC-4405E7912C-L000118](../../tests/test_multitenant_api.py#L118) | 118 | `"        token=token_b,"` | — |
| [SRC-4405E7912C-L000119](../../tests/test_multitenant_api.py#L119) | 119 | `"        payload={\"status\": \"qualified\"},"` | — |
| [SRC-4405E7912C-L000120](../../tests/test_multitenant_api.py#L120) | 120 | `"    )"` | — |
| [SRC-4405E7912C-L000121](../../tests/test_multitenant_api.py#L121) | 121 | `"    assert status == 200"` | — |
| [SRC-4405E7912C-L000122](../../tests/test_multitenant_api.py#L122) | 122 | `"    assert changed[\"lead\"][\"status\"] == \"qualified\""` | — |
| [SRC-4405E7912C-L000123](../../tests/test_multitenant_api.py#L123) | 123 | `""` | — |
| [SRC-4405E7912C-L000124](../../tests/test_multitenant_api.py#L124) | 124 | `""` | — |
| [SRC-4405E7912C-L000125](../../tests/test_multitenant_api.py#L125) | 125 | `"def test_public_api_rejects_unknown_token(tenant_api):"` | — |
| [SRC-4405E7912C-L000126](../../tests/test_multitenant_api.py#L126) | 126 | `"    base, _ = tenant_api"` | — |
| [SRC-4405E7912C-L000127](../../tests/test_multitenant_api.py#L127) | 127 | `"    status, error = request_json("` | — |
| [SRC-4405E7912C-L000128](../../tests/test_multitenant_api.py#L128) | 128 | `"        base,"` | — |
| [SRC-4405E7912C-L000129](../../tests/test_multitenant_api.py#L129) | 129 | `"        \"/api/leads\","` | — |
| [SRC-4405E7912C-L000130](../../tests/test_multitenant_api.py#L130) | 130 | `"        token=\"unknown-token-\" + \"X\" * 32,"` | — |
| [SRC-4405E7912C-L000131](../../tests/test_multitenant_api.py#L131) | 131 | `"    )"` | — |
| [SRC-4405E7912C-L000132](../../tests/test_multitenant_api.py#L132) | 132 | `"    assert status == 401"` | — |
| [SRC-4405E7912C-L000133](../../tests/test_multitenant_api.py#L133) | 133 | `"    assert \"رمز الوصول\" in error[\"error\"]"` | — |
| [SRC-4405E7912C-L000134](../../tests/test_multitenant_api.py#L134) | 134 | `""` | — |
| [SRC-4405E7912C-L000135](../../tests/test_multitenant_api.py#L135) | 135 | `""` | — |
| [SRC-4405E7912C-L000136](../../tests/test_multitenant_api.py#L136) | 136 | `"def test_viewer_membership_is_read_only(tenant_api):"` | — |
| [SRC-4405E7912C-L000137](../../tests/test_multitenant_api.py#L137) | 137 | `"    base, store = tenant_api"` | — |
| [SRC-4405E7912C-L000138](../../tests/test_multitenant_api.py#L138) | 138 | `"    tenant_id = store.create_tenant(\"Read Only Company\", \"read-only-company\")"` | — |
| [SRC-4405E7912C-L000139](../../tests/test_multitenant_api.py#L139) | 139 | `"    user_id = store.create_user(\"viewer@example.test\", \"Viewer\")"` | — |
| [SRC-4405E7912C-L000140](../../tests/test_multitenant_api.py#L140) | 140 | `"    store.add_membership(tenant_id, user_id, \"viewer\")"` | — |
| [SRC-4405E7912C-L000141](../../tests/test_multitenant_api.py#L141) | 141 | `"    token = \"viewer-token-\" + \"V\" * 32"` | — |
| [SRC-4405E7912C-L000142](../../tests/test_multitenant_api.py#L142) | 142 | `"    store.create_api_token(token, tenant_id, user_id, label=\"viewer\")"` | — |
| [SRC-4405E7912C-L000143](../../tests/test_multitenant_api.py#L143) | 143 | `""` | — |
| [SRC-4405E7912C-L000144](../../tests/test_multitenant_api.py#L144) | 144 | `"    status, listing = request_json(base, \"/api/leads\", token=token)"` | — |
| [SRC-4405E7912C-L000145](../../tests/test_multitenant_api.py#L145) | 145 | `"    assert status == 200"` | — |
| [SRC-4405E7912C-L000146](../../tests/test_multitenant_api.py#L146) | 146 | `"    assert listing[\"count\"] == 0"` | — |
| [SRC-4405E7912C-L000147](../../tests/test_multitenant_api.py#L147) | 147 | `""` | — |
| [SRC-4405E7912C-L000148](../../tests/test_multitenant_api.py#L148) | 148 | `"    status, error = request_json("` | — |
| [SRC-4405E7912C-L000149](../../tests/test_multitenant_api.py#L149) | 149 | `"        base,"` | — |
| [SRC-4405E7912C-L000150](../../tests/test_multitenant_api.py#L150) | 150 | `"        \"/api/leads\","` | — |
| [SRC-4405E7912C-L000151](../../tests/test_multitenant_api.py#L151) | 151 | `"        method=\"POST\","` | — |
| [SRC-4405E7912C-L000152](../../tests/test_multitenant_api.py#L152) | 152 | `"        token=token,"` | — |
| [SRC-4405E7912C-L000153](../../tests/test_multitenant_api.py#L153) | 153 | `"        payload={"` | — |
| [SRC-4405E7912C-L000154](../../tests/test_multitenant_api.py#L154) | 154 | `"            \"text\": \"Viewer must not write\","` | — |
| [SRC-4405E7912C-L000155](../../tests/test_multitenant_api.py#L155) | 155 | `"            \"source_url\": \"https://example.test/viewer\","` | — |
| [SRC-4405E7912C-L000156](../../tests/test_multitenant_api.py#L156) | 156 | `"        },"` | — |
| [SRC-4405E7912C-L000157](../../tests/test_multitenant_api.py#L157) | 157 | `"    )"` | — |
| [SRC-4405E7912C-L000158](../../tests/test_multitenant_api.py#L158) | 158 | `"    assert status == 403"` | — |
| [SRC-4405E7912C-L000159](../../tests/test_multitenant_api.py#L159) | 159 | `"    assert \"للقراءة فقط\" in error[\"error\"]"` | — |
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
