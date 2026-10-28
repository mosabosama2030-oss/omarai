# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **034**
- سجلات الأسطر: **800**
- النطاق: SRC-F725E90B2A-L000115 إلى SRC-F725E90B2A-L000914
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-F725E90B2A — [tests/test_web_agent.py](../../tests/test_web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-F725E90B2A-L000115](../../tests/test_web_agent.py#L115) | 115 | `"                \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L000116](../../tests/test_web_agent.py#L116) | 116 | `"                \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L000117](../../tests/test_web_agent.py#L117) | 117 | `"                \"unique_sources\": 2,"` | — |
| [SRC-F725E90B2A-L000118](../../tests/test_web_agent.py#L118) | 118 | `"                \"pages_fetched\": 2,"` | — |
| [SRC-F725E90B2A-L000119](../../tests/test_web_agent.py#L119) | 119 | `"                \"providers_used\": [\"test\"],"` | — |
| [SRC-F725E90B2A-L000120](../../tests/test_web_agent.py#L120) | 120 | `"                \"platform_counts\": {\"web\": 1},"` | — |
| [SRC-F725E90B2A-L000121](../../tests/test_web_agent.py#L121) | 121 | `"                \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L000122](../../tests/test_web_agent.py#L122) | 122 | `"                \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L000123](../../tests/test_web_agent.py#L123) | 123 | `"                \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L000124](../../tests/test_web_agent.py#L124) | 124 | `"            },"` | — |
| [SRC-F725E90B2A-L000125](../../tests/test_web_agent.py#L125) | 125 | `"        ),"` | — |
| [SRC-F725E90B2A-L000126](../../tests/test_web_agent.py#L126) | 126 | `"    )"` | — |
| [SRC-F725E90B2A-L000127](../../tests/test_web_agent.py#L127) | 127 | `""` | — |
| [SRC-F725E90B2A-L000128](../../tests/test_web_agent.py#L128) | 128 | `"    result = agent.answer(\"ما الذي يقوله المصدر؟\")"` | — |
| [SRC-F725E90B2A-L000129](../../tests/test_web_agent.py#L129) | 129 | `""` | — |
| [SRC-F725E90B2A-L000130](../../tests/test_web_agent.py#L130) | 130 | `"    assert result[\"used_web_search\"] is True"` | — |
| [SRC-F725E90B2A-L000131](../../tests/test_web_agent.py#L131) | 131 | `"    assert result[\"used_language_model\"] is False"` | — |
| [SRC-F725E90B2A-L000132](../../tests/test_web_agent.py#L132) | 132 | `"    assert \"OPENROUTER_API_KEY\" in result[\"answer\"]"` | — |
| [SRC-F725E90B2A-L000133](../../tests/test_web_agent.py#L133) | 133 | `"    assert result[\"sources\"][0][\"page_fetched\"] is True"` | — |
| [SRC-F725E90B2A-L000134](../../tests/test_web_agent.py#L134) | 134 | `""` | — |
| [SRC-F725E90B2A-L000135](../../tests/test_web_agent.py#L135) | 135 | `""` | — |
| [SRC-F725E90B2A-L000136](../../tests/test_web_agent.py#L136) | 136 | `"def test_agent_rejects_empty_or_oversized_question():"` | — |
| [SRC-F725E90B2A-L000137](../../tests/test_web_agent.py#L137) | 137 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000138](../../tests/test_web_agent.py#L138) | 138 | `"    with pytest.raises(ValueError):"` | — |
| [SRC-F725E90B2A-L000139](../../tests/test_web_agent.py#L139) | 139 | `"        agent.answer(\"   \")"` | — |
| [SRC-F725E90B2A-L000140](../../tests/test_web_agent.py#L140) | 140 | `"    with pytest.raises(ValueError):"` | — |
| [SRC-F725E90B2A-L000141](../../tests/test_web_agent.py#L141) | 141 | `"        agent.answer(\"س\" * 4001)"` | — |
| [SRC-F725E90B2A-L000142](../../tests/test_web_agent.py#L142) | 142 | `""` | — |
| [SRC-F725E90B2A-L000143](../../tests/test_web_agent.py#L143) | 143 | `""` | — |
| [SRC-F725E90B2A-L000144](../../tests/test_web_agent.py#L144) | 144 | `"def test_history_search_query_expands_short_follow_up():"` | — |
| [SRC-F725E90B2A-L000145](../../tests/test_web_agent.py#L145) | 145 | `"    history = [{\"role\": \"user\", \"content\": \"قارن أسعار السيارات الكهربائية في مصر\"}]"` | — |
| [SRC-F725E90B2A-L000146](../../tests/test_web_agent.py#L146) | 146 | `"    query = WebAgent._history_search_query(\"والسعر؟\", history)"` | — |
| [SRC-F725E90B2A-L000147](../../tests/test_web_agent.py#L147) | 147 | `"    assert \"السيارات الكهربائية\" in query"` | — |
| [SRC-F725E90B2A-L000148](../../tests/test_web_agent.py#L148) | 148 | `"    assert \"والسعر؟\" in query"` | — |
| [SRC-F725E90B2A-L000149](../../tests/test_web_agent.py#L149) | 149 | `""` | — |
| [SRC-F725E90B2A-L000150](../../tests/test_web_agent.py#L150) | 150 | `""` | — |
| [SRC-F725E90B2A-L000151](../../tests/test_web_agent.py#L151) | 151 | `"def test_public_url_filter_rejects_local_and_credential_urls():"` | — |
| [SRC-F725E90B2A-L000152](../../tests/test_web_agent.py#L152) | 152 | `"    assert _public_http_url(\"http://127.0.0.1/admin\") is None"` | — |
| [SRC-F725E90B2A-L000153](../../tests/test_web_agent.py#L153) | 153 | `"    assert _public_http_url(\"http://localhost:8000/\") is None"` | — |
| [SRC-F725E90B2A-L000154](../../tests/test_web_agent.py#L154) | 154 | `"    assert _public_http_url(\"https://user:pass@example.com/private\") is None"` | — |
| [SRC-F725E90B2A-L000155](../../tests/test_web_agent.py#L155) | 155 | `"    assert _public_http_url(\"file:///etc/passwd\") is None"` | — |
| [SRC-F725E90B2A-L000156](../../tests/test_web_agent.py#L156) | 156 | `""` | — |
| [SRC-F725E90B2A-L000157](../../tests/test_web_agent.py#L157) | 157 | `""` | — |
| [SRC-F725E90B2A-L000158](../../tests/test_web_agent.py#L158) | 158 | `"def test_public_url_filter_accepts_basic_https_url():"` | — |
| [SRC-F725E90B2A-L000159](../../tests/test_web_agent.py#L159) | 159 | `"    assert _public_http_url(\"https://example.com/path#section\") == \"https://example.com/path\""` | — |
| [SRC-F725E90B2A-L000160](../../tests/test_web_agent.py#L160) | 160 | `""` | — |
| [SRC-F725E90B2A-L000161](../../tests/test_web_agent.py#L161) | 161 | `""` | — |
| [SRC-F725E90B2A-L000162](../../tests/test_web_agent.py#L162) | 162 | `"def test_search_web_parses_duckduckgo_and_bing_without_ddgs(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000163](../../tests/test_web_agent.py#L163) | 163 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L000164](../../tests/test_web_agent.py#L164) | 164 | `""` | — |
| [SRC-F725E90B2A-L000165](../../tests/test_web_agent.py#L165) | 165 | `"    html = \"\"\""` | — |
| [SRC-F725E90B2A-L000166](../../tests/test_web_agent.py#L166) | 166 | `"    <html><body>"` | — |
| [SRC-F725E90B2A-L000167](../../tests/test_web_agent.py#L167) | 167 | `"      <div class=\"result\">"` | — |
| [SRC-F725E90B2A-L000168](../../tests/test_web_agent.py#L168) | 168 | `"        <a class=\"result__a\" href=\"https://example.com/first\">صفحة أولى</a>"` | — |
| [SRC-F725E90B2A-L000169](../../tests/test_web_agent.py#L169) | 169 | `"        <a class=\"result__snippet\">سؤال بحث تجريبي مقتطف أول</a>"` | — |
| [SRC-F725E90B2A-L000170](../../tests/test_web_agent.py#L170) | 170 | `"      </div>"` | — |
| [SRC-F725E90B2A-L000171](../../tests/test_web_agent.py#L171) | 171 | `"    </body></html>"` | — |
| [SRC-F725E90B2A-L000172](../../tests/test_web_agent.py#L172) | 172 | `"    \"\"\""` | — |
| [SRC-F725E90B2A-L000173](../../tests/test_web_agent.py#L173) | 173 | `"    rss = \"\"\""` | — |
| [SRC-F725E90B2A-L000174](../../tests/test_web_agent.py#L174) | 174 | `"    <rss><channel><item>"` | — |
| [SRC-F725E90B2A-L000175](../../tests/test_web_agent.py#L175) | 175 | `"      <title>صفحة ثانية</title>"` | — |
| [SRC-F725E90B2A-L000176](../../tests/test_web_agent.py#L176) | 176 | `"      <link>https://example.net/second</link>"` | — |
| [SRC-F725E90B2A-L000177](../../tests/test_web_agent.py#L177) | 177 | `"      <description>سؤال بحث تجريبي مقتطف ثاني</description>"` | — |
| [SRC-F725E90B2A-L000178](../../tests/test_web_agent.py#L178) | 178 | `"    </item></channel></rss>"` | — |
| [SRC-F725E90B2A-L000179](../../tests/test_web_agent.py#L179) | 179 | `"    \"\"\""` | — |
| [SRC-F725E90B2A-L000180](../../tests/test_web_agent.py#L180) | 180 | `""` | — |
| [SRC-F725E90B2A-L000181](../../tests/test_web_agent.py#L181) | 181 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L000182](../../tests/test_web_agent.py#L182) | 182 | `"        status_code = 200"` | — |
| [SRC-F725E90B2A-L000183](../../tests/test_web_agent.py#L183) | 183 | `""` | — |
| [SRC-F725E90B2A-L000184](../../tests/test_web_agent.py#L184) | 184 | `"        def __init__(self, text):"` | — |
| [SRC-F725E90B2A-L000185](../../tests/test_web_agent.py#L185) | 185 | `"            self.text = text"` | — |
| [SRC-F725E90B2A-L000186](../../tests/test_web_agent.py#L186) | 186 | `"            self.content = text.encode(\"utf-8\")"` | — |
| [SRC-F725E90B2A-L000187](../../tests/test_web_agent.py#L187) | 187 | `""` | — |
| [SRC-F725E90B2A-L000188](../../tests/test_web_agent.py#L188) | 188 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L000189](../../tests/test_web_agent.py#L189) | 189 | `""` | — |
| [SRC-F725E90B2A-L000190](../../tests/test_web_agent.py#L190) | 190 | `"    def fake_get(url, **kwargs):"` | — |
| [SRC-F725E90B2A-L000191](../../tests/test_web_agent.py#L191) | 191 | `"        calls.append(url)"` | — |
| [SRC-F725E90B2A-L000192](../../tests/test_web_agent.py#L192) | 192 | `"        return FakeResponse(html if \"duckduckgo.com\" in url else rss)"` | — |
| [SRC-F725E90B2A-L000193](../../tests/test_web_agent.py#L193) | 193 | `""` | — |
| [SRC-F725E90B2A-L000194](../../tests/test_web_agent.py#L194) | 194 | `"    monkeypatch.setattr(httpx, \"get\", fake_get)"` | — |
| [SRC-F725E90B2A-L000195](../../tests/test_web_agent.py#L195) | 195 | `"    results = WebAgent()._search_web(\"سؤال بحث تجريبي\")"` | — |
| [SRC-F725E90B2A-L000196](../../tests/test_web_agent.py#L196) | 196 | `""` | — |
| [SRC-F725E90B2A-L000197](../../tests/test_web_agent.py#L197) | 197 | `"    assert len(results) == 2"` | — |
| [SRC-F725E90B2A-L000198](../../tests/test_web_agent.py#L198) | 198 | `"    assert results[0][\"title\"] == \"صفحة أولى\""` | — |
| [SRC-F725E90B2A-L000199](../../tests/test_web_agent.py#L199) | 199 | `"    assert results[0][\"url\"] == \"https://example.com/first\""` | — |
| [SRC-F725E90B2A-L000200](../../tests/test_web_agent.py#L200) | 200 | `"    assert results[1][\"title\"] == \"صفحة ثانية\""` | — |
| [SRC-F725E90B2A-L000201](../../tests/test_web_agent.py#L201) | 201 | `"    assert results[1][\"url\"] == \"https://example.net/second\""` | — |
| [SRC-F725E90B2A-L000202](../../tests/test_web_agent.py#L202) | 202 | `"    assert len(calls) == 2"` | — |
| [SRC-F725E90B2A-L000203](../../tests/test_web_agent.py#L203) | 203 | `""` | — |
| [SRC-F725E90B2A-L000204](../../tests/test_web_agent.py#L204) | 204 | `""` | — |
| [SRC-F725E90B2A-L000205](../../tests/test_web_agent.py#L205) | 205 | `""` | — |
| [SRC-F725E90B2A-L000206](../../tests/test_web_agent.py#L206) | 206 | `"def test_model_planner_preserves_social_intent_and_adds_targeted_query(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000207](../../tests/test_web_agent.py#L207) | 207 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000208](../../tests/test_web_agent.py#L208) | 208 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L000209](../../tests/test_web_agent.py#L209) | 209 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L000210](../../tests/test_web_agent.py#L210) | 210 | `"        agent,"` | — |
| [SRC-F725E90B2A-L000211](../../tests/test_web_agent.py#L211) | 211 | `"        \"_request_completion\","` | — |
| [SRC-F725E90B2A-L000212](../../tests/test_web_agent.py#L212) | 212 | `"        lambda *args, **kwargs: ("` | — |
| [SRC-F725E90B2A-L000213](../../tests/test_web_agent.py#L213) | 213 | `"            '{\"queries\":[\"مراجعات السيارات الكهربائية\"],\"social_focus\":true,'"` | — |
| [SRC-F725E90B2A-L000214](../../tests/test_web_agent.py#L214) | 214 | `"            '\"freshness\":\"any\",\"depth\":\"deep\",\"platforms\":[\"reddit\"]}'"` | — |
| [SRC-F725E90B2A-L000215](../../tests/test_web_agent.py#L215) | 215 | `"        ),"` | — |
| [SRC-F725E90B2A-L000216](../../tests/test_web_agent.py#L216) | 216 | `"    )"` | — |
| [SRC-F725E90B2A-L000217](../../tests/test_web_agent.py#L217) | 217 | `"    plan = agent._plan_search("` | — |
| [SRC-F725E90B2A-L000218](../../tests/test_web_agent.py#L218) | 218 | `"        \"ابحث في Reddit عن تجارب العملاء مع السيارات الكهربائية\","` | — |
| [SRC-F725E90B2A-L000219](../../tests/test_web_agent.py#L219) | 219 | `"        [],"` | — |
| [SRC-F725E90B2A-L000220](../../tests/test_web_agent.py#L220) | 220 | `"    )"` | — |
| [SRC-F725E90B2A-L000221](../../tests/test_web_agent.py#L221) | 221 | `"    assert plan[\"planning_method\"] == \"language_model\""` | — |
| [SRC-F725E90B2A-L000222](../../tests/test_web_agent.py#L222) | 222 | `"    assert plan[\"social_focus\"] is True"` | — |
| [SRC-F725E90B2A-L000223](../../tests/test_web_agent.py#L223) | 223 | `"    assert \"reddit\" in plan[\"platforms\"]"` | — |
| [SRC-F725E90B2A-L000224](../../tests/test_web_agent.py#L224) | 224 | `"    assert any(\"site:reddit.com\" in query for query in plan[\"queries\"])"` | — |
| [SRC-F725E90B2A-L000225](../../tests/test_web_agent.py#L225) | 225 | `""` | — |
| [SRC-F725E90B2A-L000226](../../tests/test_web_agent.py#L226) | 226 | `""` | — |
| [SRC-F725E90B2A-L000227](../../tests/test_web_agent.py#L227) | 227 | `"def test_direct_social_search_reads_public_reddit_and_bluesky_results(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000228](../../tests/test_web_agent.py#L228) | 228 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L000229](../../tests/test_web_agent.py#L229) | 229 | `""` | — |
| [SRC-F725E90B2A-L000230](../../tests/test_web_agent.py#L230) | 230 | `"    reddit_xml = \"\"\"<rss><channel><item>"` | — |
| [SRC-F725E90B2A-L000231](../../tests/test_web_agent.py#L231) | 231 | `"      <title>تجربة سيارة كهربائية</title>"` | — |
| [SRC-F725E90B2A-L000232](../../tests/test_web_agent.py#L232) | 232 | `"      <link>https://www.reddit.com/r/cars/comments/abc123/test/</link>"` | — |
| [SRC-F725E90B2A-L000233](../../tests/test_web_agent.py#L233) | 233 | `"      <description>استهلاك البطارية في الحر</description>"` | — |
| [SRC-F725E90B2A-L000234](../../tests/test_web_agent.py#L234) | 234 | `"      <pubDate>Mon, 12 Oct 2026 10:00:00 GMT</pubDate>"` | — |
| [SRC-F725E90B2A-L000235](../../tests/test_web_agent.py#L235) | 235 | `"    </item></channel></rss>\"\"\""` | — |
| [SRC-F725E90B2A-L000236](../../tests/test_web_agent.py#L236) | 236 | `""` | — |
| [SRC-F725E90B2A-L000237](../../tests/test_web_agent.py#L237) | 237 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L000238](../../tests/test_web_agent.py#L238) | 238 | `"        status_code = 200"` | — |
| [SRC-F725E90B2A-L000239](../../tests/test_web_agent.py#L239) | 239 | `""` | — |
| [SRC-F725E90B2A-L000240](../../tests/test_web_agent.py#L240) | 240 | `"        def __init__(self, text=\"\", data=None):"` | — |
| [SRC-F725E90B2A-L000241](../../tests/test_web_agent.py#L241) | 241 | `"            self.text = text"` | — |
| [SRC-F725E90B2A-L000242](../../tests/test_web_agent.py#L242) | 242 | `"            self.content = text.encode(\"utf-8\")"` | — |
| [SRC-F725E90B2A-L000243](../../tests/test_web_agent.py#L243) | 243 | `"            self._data = data or {}"` | — |
| [SRC-F725E90B2A-L000244](../../tests/test_web_agent.py#L244) | 244 | `""` | — |
| [SRC-F725E90B2A-L000245](../../tests/test_web_agent.py#L245) | 245 | `"        def json(self):"` | — |
| [SRC-F725E90B2A-L000246](../../tests/test_web_agent.py#L246) | 246 | `"            return self._data"` | — |
| [SRC-F725E90B2A-L000247](../../tests/test_web_agent.py#L247) | 247 | `""` | — |
| [SRC-F725E90B2A-L000248](../../tests/test_web_agent.py#L248) | 248 | `"    def fake_get(url, **kwargs):"` | — |
| [SRC-F725E90B2A-L000249](../../tests/test_web_agent.py#L249) | 249 | `"        if \"reddit.com\" in url:"` | — |
| [SRC-F725E90B2A-L000250](../../tests/test_web_agent.py#L250) | 250 | `"            return FakeResponse(reddit_xml)"` | — |
| [SRC-F725E90B2A-L000251](../../tests/test_web_agent.py#L251) | 251 | `"        if \"bsky.app\" in url or \"public.api.bsky.app\" in url:"` | — |
| [SRC-F725E90B2A-L000252](../../tests/test_web_agent.py#L252) | 252 | `"            return FakeResponse(data={"` | — |
| [SRC-F725E90B2A-L000253](../../tests/test_web_agent.py#L253) | 253 | `"                \"posts\": [{"` | — |
| [SRC-F725E90B2A-L000254](../../tests/test_web_agent.py#L254) | 254 | `"                    \"post\": {"` | — |
| [SRC-F725E90B2A-L000255](../../tests/test_web_agent.py#L255) | 255 | `"                        \"uri\": \"at://did:plc:example/app.bsky.feed.post/rkey123\","` | — |
| [SRC-F725E90B2A-L000256](../../tests/test_web_agent.py#L256) | 256 | `"                        \"indexedAt\": \"2026-10-12T10:00:00Z\","` | — |
| [SRC-F725E90B2A-L000257](../../tests/test_web_agent.py#L257) | 257 | `"                        \"record\": {\"text\": \"استخدمت السيارة شهرًا\"},"` | — |
| [SRC-F725E90B2A-L000258](../../tests/test_web_agent.py#L258) | 258 | `"                        \"author\": {\"handle\": \"driver.bsky.social\", \"displayName\": \"Driver\"},"` | — |
| [SRC-F725E90B2A-L000259](../../tests/test_web_agent.py#L259) | 259 | `"                    }"` | — |
| [SRC-F725E90B2A-L000260](../../tests/test_web_agent.py#L260) | 260 | `"                }]"` | — |
| [SRC-F725E90B2A-L000261](../../tests/test_web_agent.py#L261) | 261 | `"            })"` | — |
| [SRC-F725E90B2A-L000262](../../tests/test_web_agent.py#L262) | 262 | `"        raise AssertionError(f\"Unexpected URL: {url}\")"` | — |
| [SRC-F725E90B2A-L000263](../../tests/test_web_agent.py#L263) | 263 | `""` | — |
| [SRC-F725E90B2A-L000264](../../tests/test_web_agent.py#L264) | 264 | `"    monkeypatch.setattr(httpx, \"get\", fake_get)"` | — |
| [SRC-F725E90B2A-L000265](../../tests/test_web_agent.py#L265) | 265 | `"    results, warnings = WebAgent()._search_social("` | — |
| [SRC-F725E90B2A-L000266](../../tests/test_web_agent.py#L266) | 266 | `"        \"سيارة كهربائية\", [\"reddit\", \"bluesky\"]"` | — |
| [SRC-F725E90B2A-L000267](../../tests/test_web_agent.py#L267) | 267 | `"    )"` | — |
| [SRC-F725E90B2A-L000268](../../tests/test_web_agent.py#L268) | 268 | `"    assert warnings == []"` | — |
| [SRC-F725E90B2A-L000269](../../tests/test_web_agent.py#L269) | 269 | `"    assert any(item[\"provider\"] == \"reddit_public_rss\" for item in results)"` | — |
| [SRC-F725E90B2A-L000270](../../tests/test_web_agent.py#L270) | 270 | `"    bsky = next(item for item in results if item[\"provider\"] == \"bluesky_public_search\")"` | — |
| [SRC-F725E90B2A-L000271](../../tests/test_web_agent.py#L271) | 271 | `"    assert bsky[\"url\"] == \"https://bsky.app/profile/driver.bsky.social/post/rkey123\""` | — |
| [SRC-F725E90B2A-L000272](../../tests/test_web_agent.py#L272) | 272 | `"    assert bsky[\"snippet\"] == \"استخدمت السيارة شهرًا\""` | — |
| [SRC-F725E90B2A-L000273](../../tests/test_web_agent.py#L273) | 273 | `""` | — |
| [SRC-F725E90B2A-L000274](../../tests/test_web_agent.py#L274) | 274 | `""` | — |
| [SRC-F725E90B2A-L000275](../../tests/test_web_agent.py#L275) | 275 | `"def test_research_collection_fuses_multiple_queries_and_reports_provenance(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000276](../../tests/test_web_agent.py#L276) | 276 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000277](../../tests/test_web_agent.py#L277) | 277 | `""` | — |
| [SRC-F725E90B2A-L000278](../../tests/test_web_agent.py#L278) | 278 | `"    def search(query):"` | — |
| [SRC-F725E90B2A-L000279](../../tests/test_web_agent.py#L279) | 279 | `"        if query == \"query one\":"` | — |
| [SRC-F725E90B2A-L000280](../../tests/test_web_agent.py#L280) | 280 | `"            return ["` | — |
| [SRC-F725E90B2A-L000281](../../tests/test_web_agent.py#L281) | 281 | `"                {\"title\": \"Shared\", \"url\": \"https://example.com/shared\", \"snippet\": \"Some evidence\", \"provider\": \"ddg\", \"provider_rank\": 1},"` | — |
| [SRC-F725E90B2A-L000282](../../tests/test_web_agent.py#L282) | 282 | `"                {\"title\": \"Unique A\", \"url\": \"https://example.com/a\", \"snippet\": \"Evidence A\", \"provider\": \"ddg\", \"provider_rank\": 2},"` | — |
| [SRC-F725E90B2A-L000283](../../tests/test_web_agent.py#L283) | 283 | `"            ]"` | — |
| [SRC-F725E90B2A-L000284](../../tests/test_web_agent.py#L284) | 284 | `"        return ["` | — |
| [SRC-F725E90B2A-L000285](../../tests/test_web_agent.py#L285) | 285 | `"            {\"title\": \"Shared item\", \"url\": \"https://example.com/shared\", \"snippet\": \"More evidence about this result\", \"provider\": \"bing\", \"provider_rank\": 1},"` | — |
| [SRC-F725E90B2A-L000286](../../tests/test_web_agent.py#L286) | 286 | `"            {\"title\": \"Unique B\", \"url\": \"https://example.com/b\", \"snippet\": \"Evidence B\", \"provider\": \"bing\", \"provider_rank\": 2},"` | — |
| [SRC-F725E90B2A-L000287](../../tests/test_web_agent.py#L287) | 287 | `"        ]"` | — |
| [SRC-F725E90B2A-L000288](../../tests/test_web_agent.py#L288) | 288 | `""` | — |
| [SRC-F725E90B2A-L000289](../../tests/test_web_agent.py#L289) | 289 | `"    monkeypatch.setattr(agent, \"_search_web\", search)"` | — |
| [SRC-F725E90B2A-L000290](../../tests/test_web_agent.py#L290) | 290 | `"    monkeypatch.setattr(agent, \"_fetch_page\", lambda url: (\"Read title\", \"Extracted public page text\"))"` | — |
| [SRC-F725E90B2A-L000291](../../tests/test_web_agent.py#L291) | 291 | `"    sources, warnings, report = agent._collect_research({"` | — |
| [SRC-F725E90B2A-L000292](../../tests/test_web_agent.py#L292) | 292 | `"        \"queries\": [\"query one\", \"query two\"],"` | — |
| [SRC-F725E90B2A-L000293](../../tests/test_web_agent.py#L293) | 293 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L000294](../../tests/test_web_agent.py#L294) | 294 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L000295](../../tests/test_web_agent.py#L295) | 295 | `"        \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L000296](../../tests/test_web_agent.py#L296) | 296 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L000297](../../tests/test_web_agent.py#L297) | 297 | `"    })"` | — |
| [SRC-F725E90B2A-L000298](../../tests/test_web_agent.py#L298) | 298 | `"    shared = next(item for item in sources if \"shared\" in item[\"url\"])"` | — |
| [SRC-F725E90B2A-L000299](../../tests/test_web_agent.py#L299) | 299 | `"    assert warnings == []"` | — |
| [SRC-F725E90B2A-L000300](../../tests/test_web_agent.py#L300) | 300 | `"    assert len(sources) == 3"` | — |
| [SRC-F725E90B2A-L000301](../../tests/test_web_agent.py#L301) | 301 | `"    assert set(shared[\"providers\"]) == {\"ddg\", \"bing\"}"` | — |
| [SRC-F725E90B2A-L000302](../../tests/test_web_agent.py#L302) | 302 | `"    assert {\"query one\", \"query two\"}.issubset(set(shared[\"queries\"]))"` | — |
| [SRC-F725E90B2A-L000303](../../tests/test_web_agent.py#L303) | 303 | `"    assert len(shared[\"queries\"]) >= 2"` | — |
| [SRC-F725E90B2A-L000304](../../tests/test_web_agent.py#L304) | 304 | `"    assert report[\"queries_planned\"] >= 2"` | — |
| [SRC-F725E90B2A-L000305](../../tests/test_web_agent.py#L305) | 305 | `"    assert report[\"queries_attempted\"] >= 2"` | — |
| [SRC-F725E90B2A-L000306](../../tests/test_web_agent.py#L306) | 306 | `"    assert report[\"expansion_queries\"]"` | — |
| [SRC-F725E90B2A-L000307](../../tests/test_web_agent.py#L307) | 307 | `"    assert report[\"pages_fetched\"] == 3"` | — |
| [SRC-F725E90B2A-L000308](../../tests/test_web_agent.py#L308) | 308 | `"    assert \"ddg\" in report[\"providers_used\"]"` | — |
| [SRC-F725E90B2A-L000309](../../tests/test_web_agent.py#L309) | 309 | `"    assert \"bing\" in report[\"providers_used\"]"` | — |
| [SRC-F725E90B2A-L000310](../../tests/test_web_agent.py#L310) | 310 | `""` | — |
| [SRC-F725E90B2A-L000311](../../tests/test_web_agent.py#L311) | 311 | `""` | — |
| [SRC-F725E90B2A-L000312](../../tests/test_web_agent.py#L312) | 312 | `"def test_research_collection_preserves_results_when_query_budget_is_exhausted(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000313](../../tests/test_web_agent.py#L313) | 313 | `"    \"\"\"A budget-limited query must not erase evidence returned by other queries.\"\"\""` | — |
| [SRC-F725E90B2A-L000314](../../tests/test_web_agent.py#L314) | 314 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000315](../../tests/test_web_agent.py#L315) | 315 | `""` | — |
| [SRC-F725E90B2A-L000316](../../tests/test_web_agent.py#L316) | 316 | `"    def search(query):"` | — |
| [SRC-F725E90B2A-L000317](../../tests/test_web_agent.py#L317) | 317 | `"        if query == \"query over budget\":"` | — |
| [SRC-F725E90B2A-L000318](../../tests/test_web_agent.py#L318) | 318 | `"            raise RequestBudgetExceeded(\"تم بلوغ حد موارد الطلب: search_queries.\")"` | — |
| [SRC-F725E90B2A-L000319](../../tests/test_web_agent.py#L319) | 319 | `"        return ["` | — |
| [SRC-F725E90B2A-L000320](../../tests/test_web_agent.py#L320) | 320 | `"            {"` | — |
| [SRC-F725E90B2A-L000321](../../tests/test_web_agent.py#L321) | 321 | `"                **sample_source(0),"` | — |
| [SRC-F725E90B2A-L000322](../../tests/test_web_agent.py#L322) | 322 | `"                \"provider\": \"test_provider\","` | — |
| [SRC-F725E90B2A-L000323](../../tests/test_web_agent.py#L323) | 323 | `"                \"provider_rank\": 1,"` | — |
| [SRC-F725E90B2A-L000324](../../tests/test_web_agent.py#L324) | 324 | `"                \"search_query\": query,"` | — |
| [SRC-F725E90B2A-L000325](../../tests/test_web_agent.py#L325) | 325 | `"                \"queries\": [query],"` | — |
| [SRC-F725E90B2A-L000326](../../tests/test_web_agent.py#L326) | 326 | `"            },"` | — |
| [SRC-F725E90B2A-L000327](../../tests/test_web_agent.py#L327) | 327 | `"            {"` | — |
| [SRC-F725E90B2A-L000328](../../tests/test_web_agent.py#L328) | 328 | `"                **sample_source(1),"` | — |
| [SRC-F725E90B2A-L000329](../../tests/test_web_agent.py#L329) | 329 | `"                \"provider\": \"test_provider\","` | — |
| [SRC-F725E90B2A-L000330](../../tests/test_web_agent.py#L330) | 330 | `"                \"provider_rank\": 2,"` | — |
| [SRC-F725E90B2A-L000331](../../tests/test_web_agent.py#L331) | 331 | `"                \"search_query\": query,"` | — |
| [SRC-F725E90B2A-L000332](../../tests/test_web_agent.py#L332) | 332 | `"                \"queries\": [query],"` | — |
| [SRC-F725E90B2A-L000333](../../tests/test_web_agent.py#L333) | 333 | `"            },"` | — |
| [SRC-F725E90B2A-L000334](../../tests/test_web_agent.py#L334) | 334 | `"        ]"` | — |
| [SRC-F725E90B2A-L000335](../../tests/test_web_agent.py#L335) | 335 | `""` | — |
| [SRC-F725E90B2A-L000336](../../tests/test_web_agent.py#L336) | 336 | `"    monkeypatch.setattr(agent, \"_search_web\", search)"` | — |
| [SRC-F725E90B2A-L000337](../../tests/test_web_agent.py#L337) | 337 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L000338](../../tests/test_web_agent.py#L338) | 338 | `"        agent, \"_fetch_page\", lambda url: (\"Read title\", \"Extracted public page text\")"` | — |
| [SRC-F725E90B2A-L000339](../../tests/test_web_agent.py#L339) | 339 | `"    )"` | — |
| [SRC-F725E90B2A-L000340](../../tests/test_web_agent.py#L340) | 340 | `"    sources, warnings, report = agent._collect_research({"` | — |
| [SRC-F725E90B2A-L000341](../../tests/test_web_agent.py#L341) | 341 | `"        \"queries\": [\"query over budget\", \"query success\"],"` | — |
| [SRC-F725E90B2A-L000342](../../tests/test_web_agent.py#L342) | 342 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L000343](../../tests/test_web_agent.py#L343) | 343 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L000344](../../tests/test_web_agent.py#L344) | 344 | `"        \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L000345](../../tests/test_web_agent.py#L345) | 345 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L000346](../../tests/test_web_agent.py#L346) | 346 | `"    })"` | — |
| [SRC-F725E90B2A-L000347](../../tests/test_web_agent.py#L347) | 347 | `""` | — |
| [SRC-F725E90B2A-L000348](../../tests/test_web_agent.py#L348) | 348 | `"    assert len(sources) == 2"` | — |
| [SRC-F725E90B2A-L000349](../../tests/test_web_agent.py#L349) | 349 | `"    assert report[\"pages_fetched\"] == 2"` | — |
| [SRC-F725E90B2A-L000350](../../tests/test_web_agent.py#L350) | 350 | `"    assert report[\"queries_planned\"] == 2"` | — |
| [SRC-F725E90B2A-L000351](../../tests/test_web_agent.py#L351) | 351 | `"    assert any(\"search_queries\" in warning for warning in warnings)"` | — |
| [SRC-F725E90B2A-L000352](../../tests/test_web_agent.py#L352) | 352 | `""` | — |
| [SRC-F725E90B2A-L000353](../../tests/test_web_agent.py#L353) | 353 | `""` | — |
| [SRC-F725E90B2A-L000354](../../tests/test_web_agent.py#L354) | 354 | `"def test_deep_expansion_budget_error_keeps_initial_evidence(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000355](../../tests/test_web_agent.py#L355) | 355 | `"    \"\"\"A failed deep-search expansion must leave its already collected source usable.\"\"\""` | — |
| [SRC-F725E90B2A-L000356](../../tests/test_web_agent.py#L356) | 356 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000357](../../tests/test_web_agent.py#L357) | 357 | `""` | — |
| [SRC-F725E90B2A-L000358](../../tests/test_web_agent.py#L358) | 358 | `"    def search(query):"` | — |
| [SRC-F725E90B2A-L000359](../../tests/test_web_agent.py#L359) | 359 | `"        if query == \"deep topic\":"` | — |
| [SRC-F725E90B2A-L000360](../../tests/test_web_agent.py#L360) | 360 | `"            return [{"` | — |
| [SRC-F725E90B2A-L000361](../../tests/test_web_agent.py#L361) | 361 | `"                **sample_source(0),"` | — |
| [SRC-F725E90B2A-L000362](../../tests/test_web_agent.py#L362) | 362 | `"                \"provider\": \"test_provider\","` | — |
| [SRC-F725E90B2A-L000363](../../tests/test_web_agent.py#L363) | 363 | `"                \"provider_rank\": 1,"` | — |
| [SRC-F725E90B2A-L000364](../../tests/test_web_agent.py#L364) | 364 | `"                \"search_query\": query,"` | — |
| [SRC-F725E90B2A-L000365](../../tests/test_web_agent.py#L365) | 365 | `"                \"queries\": [query],"` | — |
| [SRC-F725E90B2A-L000366](../../tests/test_web_agent.py#L366) | 366 | `"            }]"` | — |
| [SRC-F725E90B2A-L000367](../../tests/test_web_agent.py#L367) | 367 | `"        raise RequestBudgetExceeded(\"تم بلوغ حد موارد الطلب: search_queries.\")"` | — |
| [SRC-F725E90B2A-L000368](../../tests/test_web_agent.py#L368) | 368 | `""` | — |
| [SRC-F725E90B2A-L000369](../../tests/test_web_agent.py#L369) | 369 | `"    monkeypatch.setattr(agent, \"_search_web\", search)"` | — |
| [SRC-F725E90B2A-L000370](../../tests/test_web_agent.py#L370) | 370 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L000371](../../tests/test_web_agent.py#L371) | 371 | `"        agent, \"_fetch_page\", lambda url: (\"Read title\", \"Extracted public page text\")"` | — |
| [SRC-F725E90B2A-L000372](../../tests/test_web_agent.py#L372) | 372 | `"    )"` | — |
| [SRC-F725E90B2A-L000373](../../tests/test_web_agent.py#L373) | 373 | `"    sources, warnings, report = agent._collect_research({"` | — |
| [SRC-F725E90B2A-L000374](../../tests/test_web_agent.py#L374) | 374 | `"        \"queries\": [\"deep topic\"],"` | — |
| [SRC-F725E90B2A-L000375](../../tests/test_web_agent.py#L375) | 375 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L000376](../../tests/test_web_agent.py#L376) | 376 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L000377](../../tests/test_web_agent.py#L377) | 377 | `"        \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L000378](../../tests/test_web_agent.py#L378) | 378 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L000379](../../tests/test_web_agent.py#L379) | 379 | `"    })"` | — |
| [SRC-F725E90B2A-L000380](../../tests/test_web_agent.py#L380) | 380 | `""` | — |
| [SRC-F725E90B2A-L000381](../../tests/test_web_agent.py#L381) | 381 | `"    assert len(sources) == 1"` | — |
| [SRC-F725E90B2A-L000382](../../tests/test_web_agent.py#L382) | 382 | `"    assert sources[0][\"page_fetched\"] is True"` | — |
| [SRC-F725E90B2A-L000383](../../tests/test_web_agent.py#L383) | 383 | `"    assert report[\"pages_fetched\"] == 1"` | — |
| [SRC-F725E90B2A-L000384](../../tests/test_web_agent.py#L384) | 384 | `"    assert report[\"expansion_queries\"]"` | — |
| [SRC-F725E90B2A-L000385](../../tests/test_web_agent.py#L385) | 385 | `"    assert any(\"search_queries\" in warning for warning in warnings)"` | — |
| [SRC-F725E90B2A-L000386](../../tests/test_web_agent.py#L386) | 386 | `""` | — |
| [SRC-F725E90B2A-L000387](../../tests/test_web_agent.py#L387) | 387 | `""` | — |
| [SRC-F725E90B2A-L000388](../../tests/test_web_agent.py#L388) | 388 | `""` | — |
| [SRC-F725E90B2A-L000389](../../tests/test_web_agent.py#L389) | 389 | `"def test_invalid_citations_are_removed_and_valid_ones_preserved():"` | — |
| [SRC-F725E90B2A-L000390](../../tests/test_web_agent.py#L390) | 390 | `"    answer, warnings = WebAgent._remove_invalid_citations("` | — |
| [SRC-F725E90B2A-L000391](../../tests/test_web_agent.py#L391) | 391 | `"        \"النتيجة [المصدر 1] وادعاء آخر [المصدر 11].\", 1"` | — |
| [SRC-F725E90B2A-L000392](../../tests/test_web_agent.py#L392) | 392 | `"    )"` | — |
| [SRC-F725E90B2A-L000393](../../tests/test_web_agent.py#L393) | 393 | `"    assert \"[المصدر 1]\" in answer"` | — |
| [SRC-F725E90B2A-L000394](../../tests/test_web_agent.py#L394) | 394 | `"    assert \"[المصدر 11]\" not in answer"` | — |
| [SRC-F725E90B2A-L000395](../../tests/test_web_agent.py#L395) | 395 | `"    assert len(warnings) == 1"` | — |
| [SRC-F725E90B2A-L000396](../../tests/test_web_agent.py#L396) | 396 | `""` | — |
| [SRC-F725E90B2A-L000397](../../tests/test_web_agent.py#L397) | 397 | `""` | — |
| [SRC-F725E90B2A-L000398](../../tests/test_web_agent.py#L398) | 398 | `"def test_citation_metadata_limits_claim_to_index_range_validation():"` | — |
| [SRC-F725E90B2A-L000399](../../tests/test_web_agent.py#L399) | 399 | `"    metadata = WebAgent._citation_validation_metadata("` | — |
| [SRC-F725E90B2A-L000400](../../tests/test_web_agent.py#L400) | 400 | `"        \"النتيجة المدعومة مبدئيًا [المصدر 1].\","` | — |
| [SRC-F725E90B2A-L000401](../../tests/test_web_agent.py#L401) | 401 | `"        1,"` | — |
| [SRC-F725E90B2A-L000402](../../tests/test_web_agent.py#L402) | 402 | `"        [],"` | — |
| [SRC-F725E90B2A-L000403](../../tests/test_web_agent.py#L403) | 403 | `"        \"model_claim_audit_completed\","` | — |
| [SRC-F725E90B2A-L000404](../../tests/test_web_agent.py#L404) | 404 | `"    )"` | — |
| [SRC-F725E90B2A-L000405](../../tests/test_web_agent.py#L405) | 405 | `"    assert metadata == {"` | — |
| [SRC-F725E90B2A-L000406](../../tests/test_web_agent.py#L406) | 406 | `"        \"method\": \"numeric_source_index_range_only\","` | — |
| [SRC-F725E90B2A-L000407](../../tests/test_web_agent.py#L407) | 407 | `"        \"status\": \"index_range_check_passed\","` | — |
| [SRC-F725E90B2A-L000408](../../tests/test_web_agent.py#L408) | 408 | `"        \"valid_citation_count\": 1,"` | — |
| [SRC-F725E90B2A-L000409](../../tests/test_web_agent.py#L409) | 409 | `"        \"invalid_references_removed\": 0,"` | — |
| [SRC-F725E90B2A-L000410](../../tests/test_web_agent.py#L410) | 410 | `"        \"max_citable_source_index\": 1,"` | — |
| [SRC-F725E90B2A-L000411](../../tests/test_web_agent.py#L411) | 411 | `"        \"claim_support\": \"model_review_not_independent_fact_check\","` | — |
| [SRC-F725E90B2A-L000412](../../tests/test_web_agent.py#L412) | 412 | `"    }"` | — |
| [SRC-F725E90B2A-L000413](../../tests/test_web_agent.py#L413) | 413 | `""` | — |
| [SRC-F725E90B2A-L000414](../../tests/test_web_agent.py#L414) | 414 | `""` | — |
| [SRC-F725E90B2A-L000415](../../tests/test_web_agent.py#L415) | 415 | `"def test_citation_metadata_reports_invalid_reference_repair():"` | — |
| [SRC-F725E90B2A-L000416](../../tests/test_web_agent.py#L416) | 416 | `"    cleaned, warnings = WebAgent._remove_invalid_citations("` | — |
| [SRC-F725E90B2A-L000417](../../tests/test_web_agent.py#L417) | 417 | `"        \"صحيح [المصدر 1] وخاطئ [المصدر 9].\", 1"` | — |
| [SRC-F725E90B2A-L000418](../../tests/test_web_agent.py#L418) | 418 | `"    )"` | — |
| [SRC-F725E90B2A-L000419](../../tests/test_web_agent.py#L419) | 419 | `"    metadata = WebAgent._citation_validation_metadata("` | — |
| [SRC-F725E90B2A-L000420](../../tests/test_web_agent.py#L420) | 420 | `"        cleaned, 1, warnings, \"not_run\""` | — |
| [SRC-F725E90B2A-L000421](../../tests/test_web_agent.py#L421) | 421 | `"    )"` | — |
| [SRC-F725E90B2A-L000422](../../tests/test_web_agent.py#L422) | 422 | `"    assert metadata[\"status\"] == \"invalid_index_references_removed\""` | — |
| [SRC-F725E90B2A-L000423](../../tests/test_web_agent.py#L423) | 423 | `"    assert metadata[\"valid_citation_count\"] == 1"` | — |
| [SRC-F725E90B2A-L000424](../../tests/test_web_agent.py#L424) | 424 | `"    assert metadata[\"invalid_references_removed\"] == 1"` | — |
| [SRC-F725E90B2A-L000425](../../tests/test_web_agent.py#L425) | 425 | `"    assert metadata[\"claim_support\"] == \"not_verified\""` | — |
| [SRC-F725E90B2A-L000426](../../tests/test_web_agent.py#L426) | 426 | `""` | — |
| [SRC-F725E90B2A-L000427](../../tests/test_web_agent.py#L427) | 427 | `""` | — |
| [SRC-F725E90B2A-L000428](../../tests/test_web_agent.py#L428) | 428 | `"def test_citation_metadata_reports_absent_markers_and_empty_source_range():"` | — |
| [SRC-F725E90B2A-L000429](../../tests/test_web_agent.py#L429) | 429 | `"    metadata = WebAgent._citation_validation_metadata("` | — |
| [SRC-F725E90B2A-L000430](../../tests/test_web_agent.py#L430) | 430 | `"        \"لا توجد إحالات للمصادر.\", 0, [], \"not_run\""` | — |
| [SRC-F725E90B2A-L000431](../../tests/test_web_agent.py#L431) | 431 | `"    )"` | — |
| [SRC-F725E90B2A-L000432](../../tests/test_web_agent.py#L432) | 432 | `"    assert metadata[\"status\"] == \"no_citation_markers_present\""` | — |
| [SRC-F725E90B2A-L000433](../../tests/test_web_agent.py#L433) | 433 | `"    assert metadata[\"valid_citation_count\"] == 0"` | — |
| [SRC-F725E90B2A-L000434](../../tests/test_web_agent.py#L434) | 434 | `"    assert metadata[\"max_citable_source_index\"] == 0"` | — |
| [SRC-F725E90B2A-L000435](../../tests/test_web_agent.py#L435) | 435 | `""` | — |
| [SRC-F725E90B2A-L000436](../../tests/test_web_agent.py#L436) | 436 | `""` | — |
| [SRC-F725E90B2A-L000437](../../tests/test_web_agent.py#L437) | 437 | `"def test_user_supplied_url_is_prioritized_and_page_content_is_extracted(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000438](../../tests/test_web_agent.py#L438) | 438 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000439](../../tests/test_web_agent.py#L439) | 439 | `"    monkeypatch.setattr(agent, \"_search_web\", lambda query: [])"` | — |
| [SRC-F725E90B2A-L000440](../../tests/test_web_agent.py#L440) | 440 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L000441](../../tests/test_web_agent.py#L441) | 441 | `"        agent,"` | — |
| [SRC-F725E90B2A-L000442](../../tests/test_web_agent.py#L442) | 442 | `"        \"_fetch_page\","` | — |
| [SRC-F725E90B2A-L000443](../../tests/test_web_agent.py#L443) | 443 | `"        lambda url: (\"User page title\", \"Full public page text supplied for analysis\"),"` | — |
| [SRC-F725E90B2A-L000444](../../tests/test_web_agent.py#L444) | 444 | `"    )"` | — |
| [SRC-F725E90B2A-L000445](../../tests/test_web_agent.py#L445) | 445 | `"    sources, warnings, report = agent._collect_research({"` | — |
| [SRC-F725E90B2A-L000446](../../tests/test_web_agent.py#L446) | 446 | `"        \"queries\": [\"لخص هذه الصفحة\"],"` | — |
| [SRC-F725E90B2A-L000447](../../tests/test_web_agent.py#L447) | 447 | `"        \"direct_urls\": [\"https://example.com/article\"],"` | — |
| [SRC-F725E90B2A-L000448](../../tests/test_web_agent.py#L448) | 448 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L000449](../../tests/test_web_agent.py#L449) | 449 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L000450](../../tests/test_web_agent.py#L450) | 450 | `"        \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L000451](../../tests/test_web_agent.py#L451) | 451 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L000452](../../tests/test_web_agent.py#L452) | 452 | `"    })"` | — |
| [SRC-F725E90B2A-L000453](../../tests/test_web_agent.py#L453) | 453 | `"    assert warnings == []"` | — |
| [SRC-F725E90B2A-L000454](../../tests/test_web_agent.py#L454) | 454 | `"    assert len(sources) == 1"` | — |
| [SRC-F725E90B2A-L000455](../../tests/test_web_agent.py#L455) | 455 | `"    assert sources[0][\"url\"] == \"https://example.com/article\""` | — |
| [SRC-F725E90B2A-L000456](../../tests/test_web_agent.py#L456) | 456 | `"    assert sources[0][\"title\"] == \"User page title\""` | — |
| [SRC-F725E90B2A-L000457](../../tests/test_web_agent.py#L457) | 457 | `"    assert sources[0][\"page_fetched\"] is True"` | — |
| [SRC-F725E90B2A-L000458](../../tests/test_web_agent.py#L458) | 458 | `"    assert \"user_supplied_url\" in report[\"providers_used\"]"` | — |
| [SRC-F725E90B2A-L000459](../../tests/test_web_agent.py#L459) | 459 | `""` | — |
| [SRC-F725E90B2A-L000460](../../tests/test_web_agent.py#L460) | 460 | `""` | — |
| [SRC-F725E90B2A-L000461](../../tests/test_web_agent.py#L461) | 461 | `""` | — |
| [SRC-F725E90B2A-L000462](../../tests/test_web_agent.py#L462) | 462 | `"def test_official_x_search_is_used_only_with_explicit_bearer_token(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000463](../../tests/test_web_agent.py#L463) | 463 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L000464](../../tests/test_web_agent.py#L464) | 464 | `""` | — |
| [SRC-F725E90B2A-L000465](../../tests/test_web_agent.py#L465) | 465 | `"    monkeypatch.setenv(\"X_BEARER_TOKEN\", \"test-token\")"` | — |
| [SRC-F725E90B2A-L000466](../../tests/test_web_agent.py#L466) | 466 | `""` | — |
| [SRC-F725E90B2A-L000467](../../tests/test_web_agent.py#L467) | 467 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L000468](../../tests/test_web_agent.py#L468) | 468 | `"        status_code = 200"` | — |
| [SRC-F725E90B2A-L000469](../../tests/test_web_agent.py#L469) | 469 | `""` | — |
| [SRC-F725E90B2A-L000470](../../tests/test_web_agent.py#L470) | 470 | `"        def json(self):"` | — |
| [SRC-F725E90B2A-L000471](../../tests/test_web_agent.py#L471) | 471 | `"            return {"` | — |
| [SRC-F725E90B2A-L000472](../../tests/test_web_agent.py#L472) | 472 | `"                \"data\": [{"` | — |
| [SRC-F725E90B2A-L000473](../../tests/test_web_agent.py#L473) | 473 | `"                    \"id\": \"1840000000000000000\","` | — |
| [SRC-F725E90B2A-L000474](../../tests/test_web_agent.py#L474) | 474 | `"                    \"text\": \"تجربة علنية لاستهلاك سيارة كهربائية\","` | — |
| [SRC-F725E90B2A-L000475](../../tests/test_web_agent.py#L475) | 475 | `"                    \"created_at\": \"2026-10-12T10:00:00Z\","` | — |
| [SRC-F725E90B2A-L000476](../../tests/test_web_agent.py#L476) | 476 | `"                    \"author_id\": \"u1\","` | — |
| [SRC-F725E90B2A-L000477](../../tests/test_web_agent.py#L477) | 477 | `"                }],"` | — |
| [SRC-F725E90B2A-L000478](../../tests/test_web_agent.py#L478) | 478 | `"                \"includes\": {"` | — |
| [SRC-F725E90B2A-L000479](../../tests/test_web_agent.py#L479) | 479 | `"                    \"users\": [{\"id\": \"u1\", \"username\": \"driver\", \"name\": \"Driver\"}]"` | — |
| [SRC-F725E90B2A-L000480](../../tests/test_web_agent.py#L480) | 480 | `"                },"` | — |
| [SRC-F725E90B2A-L000481](../../tests/test_web_agent.py#L481) | 481 | `"            }"` | — |
| [SRC-F725E90B2A-L000482](../../tests/test_web_agent.py#L482) | 482 | `""` | — |
| [SRC-F725E90B2A-L000483](../../tests/test_web_agent.py#L483) | 483 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L000484](../../tests/test_web_agent.py#L484) | 484 | `""` | — |
| [SRC-F725E90B2A-L000485](../../tests/test_web_agent.py#L485) | 485 | `"    def fake_get(url, **kwargs):"` | — |
| [SRC-F725E90B2A-L000486](../../tests/test_web_agent.py#L486) | 486 | `"        calls.append((url, kwargs))"` | — |
| [SRC-F725E90B2A-L000487](../../tests/test_web_agent.py#L487) | 487 | `"        return FakeResponse()"` | — |
| [SRC-F725E90B2A-L000488](../../tests/test_web_agent.py#L488) | 488 | `""` | — |
| [SRC-F725E90B2A-L000489](../../tests/test_web_agent.py#L489) | 489 | `"    monkeypatch.setattr(httpx, \"get\", fake_get)"` | — |
| [SRC-F725E90B2A-L000490](../../tests/test_web_agent.py#L490) | 490 | `"    results, warnings = WebAgent()._search_social("` | — |
| [SRC-F725E90B2A-L000491](../../tests/test_web_agent.py#L491) | 491 | `"        \"سيارة كهربائية\", [\"x\"]"` | — |
| [SRC-F725E90B2A-L000492](../../tests/test_web_agent.py#L492) | 492 | `"    )"` | — |
| [SRC-F725E90B2A-L000493](../../tests/test_web_agent.py#L493) | 493 | `"    assert warnings == []"` | — |
| [SRC-F725E90B2A-L000494](../../tests/test_web_agent.py#L494) | 494 | `"    assert len(results) == 1"` | — |
| [SRC-F725E90B2A-L000495](../../tests/test_web_agent.py#L495) | 495 | `"    assert results[0][\"provider\"] == \"x_official_api\""` | — |
| [SRC-F725E90B2A-L000496](../../tests/test_web_agent.py#L496) | 496 | `"    assert results[0][\"url\"] == \"https://x.com/driver/status/1840000000000000000\""` | — |
| [SRC-F725E90B2A-L000497](../../tests/test_web_agent.py#L497) | 497 | `"    assert calls[0][1][\"headers\"][\"Authorization\"] == \"Bearer test-token\""` | — |
| [SRC-F725E90B2A-L000498](../../tests/test_web_agent.py#L498) | 498 | `""` | — |
| [SRC-F725E90B2A-L000499](../../tests/test_web_agent.py#L499) | 499 | `""` | — |
| [SRC-F725E90B2A-L000500](../../tests/test_web_agent.py#L500) | 500 | `""` | — |
| [SRC-F725E90B2A-L000501](../../tests/test_web_agent.py#L501) | 501 | `"def test_instagram_graph_api_returns_only_public_hashtag_media(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000502](../../tests/test_web_agent.py#L502) | 502 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L000503](../../tests/test_web_agent.py#L503) | 503 | `""` | — |
| [SRC-F725E90B2A-L000504](../../tests/test_web_agent.py#L504) | 504 | `"    monkeypatch.setenv(\"INSTAGRAM_USER_ID\", \"ig-user-123\")"` | — |
| [SRC-F725E90B2A-L000505](../../tests/test_web_agent.py#L505) | 505 | `"    monkeypatch.setenv(\"INSTAGRAM_ACCESS_TOKEN\", \"test-ig-token\")"` | — |
| [SRC-F725E90B2A-L000506](../../tests/test_web_agent.py#L506) | 506 | `"    monkeypatch.setenv(\"META_GRAPH_VERSION\", \"v25.0\")"` | — |
| [SRC-F725E90B2A-L000507](../../tests/test_web_agent.py#L507) | 507 | `""` | — |
| [SRC-F725E90B2A-L000508](../../tests/test_web_agent.py#L508) | 508 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L000509](../../tests/test_web_agent.py#L509) | 509 | `"        status_code = 200"` | — |
| [SRC-F725E90B2A-L000510](../../tests/test_web_agent.py#L510) | 510 | `""` | — |
| [SRC-F725E90B2A-L000511](../../tests/test_web_agent.py#L511) | 511 | `"        def __init__(self, payload):"` | — |
| [SRC-F725E90B2A-L000512](../../tests/test_web_agent.py#L512) | 512 | `"            self.payload = payload"` | — |
| [SRC-F725E90B2A-L000513](../../tests/test_web_agent.py#L513) | 513 | `""` | — |
| [SRC-F725E90B2A-L000514](../../tests/test_web_agent.py#L514) | 514 | `"        def json(self):"` | — |
| [SRC-F725E90B2A-L000515](../../tests/test_web_agent.py#L515) | 515 | `"            return self.payload"` | — |
| [SRC-F725E90B2A-L000516](../../tests/test_web_agent.py#L516) | 516 | `""` | — |
| [SRC-F725E90B2A-L000517](../../tests/test_web_agent.py#L517) | 517 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L000518](../../tests/test_web_agent.py#L518) | 518 | `""` | — |
| [SRC-F725E90B2A-L000519](../../tests/test_web_agent.py#L519) | 519 | `"    def fake_get(url, **kwargs):"` | — |
| [SRC-F725E90B2A-L000520](../../tests/test_web_agent.py#L520) | 520 | `"        calls.append((url, kwargs))"` | — |
| [SRC-F725E90B2A-L000521](../../tests/test_web_agent.py#L521) | 521 | `"        if url.endswith(\"/ig_hashtag_search\"):"` | — |
| [SRC-F725E90B2A-L000522](../../tests/test_web_agent.py#L522) | 522 | `"            return FakeResponse({\"data\": [{\"id\": \"tag-7\", \"name\": \"cars\"}]})"` | — |
| [SRC-F725E90B2A-L000523](../../tests/test_web_agent.py#L523) | 523 | `"        if url.endswith(\"/tag-7/recent_media\"):"` | — |
| [SRC-F725E90B2A-L000524](../../tests/test_web_agent.py#L524) | 524 | `"            return FakeResponse({\"data\": [{"` | — |
| [SRC-F725E90B2A-L000525](../../tests/test_web_agent.py#L525) | 525 | `"                \"permalink\": \"https://www.instagram.com/p/ABC123/\","` | — |
| [SRC-F725E90B2A-L000526](../../tests/test_web_agent.py#L526) | 526 | `"                \"caption\": \"Owner shared an electric car review\","` | — |
| [SRC-F725E90B2A-L000527](../../tests/test_web_agent.py#L527) | 527 | `"                \"media_type\": \"IMAGE\","` | — |
| [SRC-F725E90B2A-L000528](../../tests/test_web_agent.py#L528) | 528 | `"                \"timestamp\": \"2026-10-12T10:00:00+0000\","` | — |
| [SRC-F725E90B2A-L000529](../../tests/test_web_agent.py#L529) | 529 | `"                \"like_count\": 17,"` | — |
| [SRC-F725E90B2A-L000530](../../tests/test_web_agent.py#L530) | 530 | `"                \"comments_count\": 4,"` | — |
| [SRC-F725E90B2A-L000531](../../tests/test_web_agent.py#L531) | 531 | `"            }]})"` | — |
| [SRC-F725E90B2A-L000532](../../tests/test_web_agent.py#L532) | 532 | `"        raise AssertionError(f\"Unexpected URL {url}\")"` | — |
| [SRC-F725E90B2A-L000533](../../tests/test_web_agent.py#L533) | 533 | `""` | — |
| [SRC-F725E90B2A-L000534](../../tests/test_web_agent.py#L534) | 534 | `"    monkeypatch.setattr(httpx, \"get\", fake_get)"` | — |
| [SRC-F725E90B2A-L000535](../../tests/test_web_agent.py#L535) | 535 | `"    results, warnings = WebAgent()._search_social("` | — |
| [SRC-F725E90B2A-L000536](../../tests/test_web_agent.py#L536) | 536 | `"        \"Instagram #cars\", [\"instagram\"]"` | — |
| [SRC-F725E90B2A-L000537](../../tests/test_web_agent.py#L537) | 537 | `"    )"` | — |
| [SRC-F725E90B2A-L000538](../../tests/test_web_agent.py#L538) | 538 | `"    assert warnings == []"` | — |
| [SRC-F725E90B2A-L000539](../../tests/test_web_agent.py#L539) | 539 | `"    assert len(results) == 1"` | — |
| [SRC-F725E90B2A-L000540](../../tests/test_web_agent.py#L540) | 540 | `"    assert results[0][\"provider\"] == \"instagram_graph_api\""` | — |
| [SRC-F725E90B2A-L000541](../../tests/test_web_agent.py#L541) | 541 | `"    assert results[0][\"url\"] == \"https://www.instagram.com/p/ABC123/\""` | — |
| [SRC-F725E90B2A-L000542](../../tests/test_web_agent.py#L542) | 542 | `"    assert \"likes=17\" in results[0][\"snippet\"]"` | — |
| [SRC-F725E90B2A-L000543](../../tests/test_web_agent.py#L543) | 543 | `"    assert calls[0][1][\"params\"][\"q\"] == \"cars\""` | — |
| [SRC-F725E90B2A-L000544](../../tests/test_web_agent.py#L544) | 544 | `"    assert calls[0][1][\"params\"][\"access_token\"] == \"test-ig-token\""` | — |
| [SRC-F725E90B2A-L000545](../../tests/test_web_agent.py#L545) | 545 | `"    assert \"test-ig-token\" not in str(results)"` | — |
| [SRC-F725E90B2A-L000546](../../tests/test_web_agent.py#L546) | 546 | `""` | — |
| [SRC-F725E90B2A-L000547](../../tests/test_web_agent.py#L547) | 547 | `""` | — |
| [SRC-F725E90B2A-L000548](../../tests/test_web_agent.py#L548) | 548 | `"def test_instagram_api_not_configured_uses_honest_fallback_warning(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000549](../../tests/test_web_agent.py#L549) | 549 | `"    monkeypatch.delenv(\"INSTAGRAM_USER_ID\", raising=False)"` | — |
| [SRC-F725E90B2A-L000550](../../tests/test_web_agent.py#L550) | 550 | `"    monkeypatch.delenv(\"INSTAGRAM_ACCESS_TOKEN\", raising=False)"` | — |
| [SRC-F725E90B2A-L000551](../../tests/test_web_agent.py#L551) | 551 | `"    results, warnings = WebAgent()._search_social("` | — |
| [SRC-F725E90B2A-L000552](../../tests/test_web_agent.py#L552) | 552 | `"        \"تجارب عامة على Instagram\", [\"instagram\"]"` | — |
| [SRC-F725E90B2A-L000553](../../tests/test_web_agent.py#L553) | 553 | `"    )"` | — |
| [SRC-F725E90B2A-L000554](../../tests/test_web_agent.py#L554) | 554 | `"    assert results == []"` | — |
| [SRC-F725E90B2A-L000555](../../tests/test_web_agent.py#L555) | 555 | `"    assert any(\"indexed public Instagram\" in warning for warning in warnings)"` | — |
| [SRC-F725E90B2A-L000556](../../tests/test_web_agent.py#L556) | 556 | `""` | — |
| [SRC-F725E90B2A-L000557](../../tests/test_web_agent.py#L557) | 557 | `""` | — |
| [SRC-F725E90B2A-L000558](../../tests/test_web_agent.py#L558) | 558 | `"def test_facebook_pages_api_reads_only_operator_configured_pages(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000559](../../tests/test_web_agent.py#L559) | 559 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L000560](../../tests/test_web_agent.py#L560) | 560 | `""` | — |
| [SRC-F725E90B2A-L000561](../../tests/test_web_agent.py#L561) | 561 | `"    monkeypatch.setenv(\"FACEBOOK_PAGE_ACCESS_TOKEN\", \"test-page-token\")"` | — |
| [SRC-F725E90B2A-L000562](../../tests/test_web_agent.py#L562) | 562 | `"    monkeypatch.setenv(\"FACEBOOK_PAGE_IDS\", \"page-1,page-2\")"` | — |
| [SRC-F725E90B2A-L000563](../../tests/test_web_agent.py#L563) | 563 | `""` | — |
| [SRC-F725E90B2A-L000564](../../tests/test_web_agent.py#L564) | 564 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L000565](../../tests/test_web_agent.py#L565) | 565 | `"        status_code = 200"` | — |
| [SRC-F725E90B2A-L000566](../../tests/test_web_agent.py#L566) | 566 | `""` | — |
| [SRC-F725E90B2A-L000567](../../tests/test_web_agent.py#L567) | 567 | `"        def json(self):"` | — |
| [SRC-F725E90B2A-L000568](../../tests/test_web_agent.py#L568) | 568 | `"            return {\"data\": [{"` | — |
| [SRC-F725E90B2A-L000569](../../tests/test_web_agent.py#L569) | 569 | `"                \"message\": \"Electric car owners looking for charging advice\","` | — |
| [SRC-F725E90B2A-L000570](../../tests/test_web_agent.py#L570) | 570 | `"                \"permalink_url\": \"https://www.facebook.com/example/posts/123\","` | — |
| [SRC-F725E90B2A-L000571](../../tests/test_web_agent.py#L571) | 571 | `"                \"created_time\": \"2026-10-12T12:00:00+0000\","` | — |
| [SRC-F725E90B2A-L000572](../../tests/test_web_agent.py#L572) | 572 | `"                \"comments\": {\"data\": ["` | — |
| [SRC-F725E90B2A-L000573](../../tests/test_web_agent.py#L573) | 573 | `"                    {\"message\": \"What is the current price?\", \"like_count\": 3}"` | — |
| [SRC-F725E90B2A-L000574](../../tests/test_web_agent.py#L574) | 574 | `"                ]},"` | — |
| [SRC-F725E90B2A-L000575](../../tests/test_web_agent.py#L575) | 575 | `"            }]}"` | — |
| [SRC-F725E90B2A-L000576](../../tests/test_web_agent.py#L576) | 576 | `""` | — |
| [SRC-F725E90B2A-L000577](../../tests/test_web_agent.py#L577) | 577 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L000578](../../tests/test_web_agent.py#L578) | 578 | `""` | — |
| [SRC-F725E90B2A-L000579](../../tests/test_web_agent.py#L579) | 579 | `"    def fake_get(url, **kwargs):"` | — |
| [SRC-F725E90B2A-L000580](../../tests/test_web_agent.py#L580) | 580 | `"        calls.append((url, kwargs))"` | — |
| [SRC-F725E90B2A-L000581](../../tests/test_web_agent.py#L581) | 581 | `"        return FakeResponse()"` | — |
| [SRC-F725E90B2A-L000582](../../tests/test_web_agent.py#L582) | 582 | `""` | — |
| [SRC-F725E90B2A-L000583](../../tests/test_web_agent.py#L583) | 583 | `"    monkeypatch.setattr(httpx, \"get\", fake_get)"` | — |
| [SRC-F725E90B2A-L000584](../../tests/test_web_agent.py#L584) | 584 | `"    results, warnings = WebAgent()._search_social("` | — |
| [SRC-F725E90B2A-L000585](../../tests/test_web_agent.py#L585) | 585 | `"        \"electric car\", [\"facebook\"]"` | — |
| [SRC-F725E90B2A-L000586](../../tests/test_web_agent.py#L586) | 586 | `"    )"` | — |
| [SRC-F725E90B2A-L000587](../../tests/test_web_agent.py#L587) | 587 | `"    assert len(results) == 2  # one matching post for each explicitly configured page"` | — |
| [SRC-F725E90B2A-L000588](../../tests/test_web_agent.py#L588) | 588 | `"    assert warnings == []"` | — |
| [SRC-F725E90B2A-L000589](../../tests/test_web_agent.py#L589) | 589 | `"    assert all(item[\"provider\"] == \"facebook_pages_api\" for item in results)"` | — |
| [SRC-F725E90B2A-L000590](../../tests/test_web_agent.py#L590) | 590 | `"    assert all(\"Electric car owners\" in item[\"snippet\"] for item in results)"` | — |
| [SRC-F725E90B2A-L000591](../../tests/test_web_agent.py#L591) | 591 | `"    assert len(calls) == 2"` | — |
| [SRC-F725E90B2A-L000592](../../tests/test_web_agent.py#L592) | 592 | `"    assert all(\"Bearer test-page-token\" == call[1][\"headers\"][\"Authorization\"] for call in calls)"` | — |
| [SRC-F725E90B2A-L000593](../../tests/test_web_agent.py#L593) | 593 | `""` | — |
| [SRC-F725E90B2A-L000594](../../tests/test_web_agent.py#L594) | 594 | `""` | — |
| [SRC-F725E90B2A-L000595](../../tests/test_web_agent.py#L595) | 595 | `"def test_reddit_oauth_api_is_preferred_when_credentials_are_configured(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000596](../../tests/test_web_agent.py#L596) | 596 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L000597](../../tests/test_web_agent.py#L597) | 597 | `""` | — |
| [SRC-F725E90B2A-L000598](../../tests/test_web_agent.py#L598) | 598 | `"    monkeypatch.setenv(\"REDDIT_CLIENT_ID\", \"client-test\")"` | — |
| [SRC-F725E90B2A-L000599](../../tests/test_web_agent.py#L599) | 599 | `"    monkeypatch.setenv(\"REDDIT_CLIENT_SECRET\", \"secret-test\")"` | — |
| [SRC-F725E90B2A-L000600](../../tests/test_web_agent.py#L600) | 600 | `"    monkeypatch.setenv(\"REDDIT_USER_AGENT\", \"test:omarai:0.1\")"` | — |
| [SRC-F725E90B2A-L000601](../../tests/test_web_agent.py#L601) | 601 | `""` | — |
| [SRC-F725E90B2A-L000602](../../tests/test_web_agent.py#L602) | 602 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L000603](../../tests/test_web_agent.py#L603) | 603 | `"        status_code = 200"` | — |
| [SRC-F725E90B2A-L000604](../../tests/test_web_agent.py#L604) | 604 | `""` | — |
| [SRC-F725E90B2A-L000605](../../tests/test_web_agent.py#L605) | 605 | `"        def __init__(self, payload):"` | — |
| [SRC-F725E90B2A-L000606](../../tests/test_web_agent.py#L606) | 606 | `"            self.payload = payload"` | — |
| [SRC-F725E90B2A-L000607](../../tests/test_web_agent.py#L607) | 607 | `""` | — |
| [SRC-F725E90B2A-L000608](../../tests/test_web_agent.py#L608) | 608 | `"        def json(self):"` | — |
| [SRC-F725E90B2A-L000609](../../tests/test_web_agent.py#L609) | 609 | `"            return self.payload"` | — |
| [SRC-F725E90B2A-L000610](../../tests/test_web_agent.py#L610) | 610 | `""` | — |
| [SRC-F725E90B2A-L000611](../../tests/test_web_agent.py#L611) | 611 | `"        @property"` | — |
| [SRC-F725E90B2A-L000612](../../tests/test_web_agent.py#L612) | 612 | `"        def content(self):"` | — |
| [SRC-F725E90B2A-L000613](../../tests/test_web_agent.py#L613) | 613 | `"            import json"` | — |
| [SRC-F725E90B2A-L000614](../../tests/test_web_agent.py#L614) | 614 | `"            return json.dumps(self.payload).encode()"` | — |
| [SRC-F725E90B2A-L000615](../../tests/test_web_agent.py#L615) | 615 | `""` | — |
| [SRC-F725E90B2A-L000616](../../tests/test_web_agent.py#L616) | 616 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L000617](../../tests/test_web_agent.py#L617) | 617 | `""` | — |
| [SRC-F725E90B2A-L000618](../../tests/test_web_agent.py#L618) | 618 | `"    def fake_post(url, **kwargs):"` | — |
| [SRC-F725E90B2A-L000619](../../tests/test_web_agent.py#L619) | 619 | `"        calls.append((\"POST\", url, kwargs))"` | — |
| [SRC-F725E90B2A-L000620](../../tests/test_web_agent.py#L620) | 620 | `"        return FakeResponse({\"access_token\": \"test-reddit-access-token\"})"` | — |
| [SRC-F725E90B2A-L000621](../../tests/test_web_agent.py#L621) | 621 | `""` | — |
| [SRC-F725E90B2A-L000622](../../tests/test_web_agent.py#L622) | 622 | `"    def fake_get(url, **kwargs):"` | — |
| [SRC-F725E90B2A-L000623](../../tests/test_web_agent.py#L623) | 623 | `"        calls.append((\"GET\", url, kwargs))"` | — |
| [SRC-F725E90B2A-L000624](../../tests/test_web_agent.py#L624) | 624 | `"        return FakeResponse({\"data\": {\"children\": [{"` | — |
| [SRC-F725E90B2A-L000625](../../tests/test_web_agent.py#L625) | 625 | `"            \"data\": {"` | — |
| [SRC-F725E90B2A-L000626](../../tests/test_web_agent.py#L626) | 626 | `"                \"title\": \"Electric vehicle owner discussion\","` | — |
| [SRC-F725E90B2A-L000627](../../tests/test_web_agent.py#L627) | 627 | `"                \"permalink\": \"/r/cars/comments/example/post/\","` | — |
| [SRC-F725E90B2A-L000628](../../tests/test_web_agent.py#L628) | 628 | `"                \"selftext\": \"Owners discuss battery range.\","` | — |
| [SRC-F725E90B2A-L000629](../../tests/test_web_agent.py#L629) | 629 | `"                \"created_utc\": 1791800000,"` | — |
| [SRC-F725E90B2A-L000630](../../tests/test_web_agent.py#L630) | 630 | `"                \"score\": 25,"` | — |
| [SRC-F725E90B2A-L000631](../../tests/test_web_agent.py#L631) | 631 | `"                \"num_comments\": 8,"` | — |
| [SRC-F725E90B2A-L000632](../../tests/test_web_agent.py#L632) | 632 | `"            }"` | — |
| [SRC-F725E90B2A-L000633](../../tests/test_web_agent.py#L633) | 633 | `"        }]}})"` | — |
| [SRC-F725E90B2A-L000634](../../tests/test_web_agent.py#L634) | 634 | `""` | — |
| [SRC-F725E90B2A-L000635](../../tests/test_web_agent.py#L635) | 635 | `"    monkeypatch.setattr(httpx, \"post\", fake_post)"` | — |
| [SRC-F725E90B2A-L000636](../../tests/test_web_agent.py#L636) | 636 | `"    monkeypatch.setattr(httpx, \"get\", fake_get)"` | — |
| [SRC-F725E90B2A-L000637](../../tests/test_web_agent.py#L637) | 637 | `"    results, warnings = WebAgent()._search_social("` | — |
| [SRC-F725E90B2A-L000638](../../tests/test_web_agent.py#L638) | 638 | `"        \"electric vehicles\", [\"reddit\"]"` | — |
| [SRC-F725E90B2A-L000639](../../tests/test_web_agent.py#L639) | 639 | `"    )"` | — |
| [SRC-F725E90B2A-L000640](../../tests/test_web_agent.py#L640) | 640 | `"    assert len(results) == 1"` | — |
| [SRC-F725E90B2A-L000641](../../tests/test_web_agent.py#L641) | 641 | `"    assert warnings == []"` | — |
| [SRC-F725E90B2A-L000642](../../tests/test_web_agent.py#L642) | 642 | `"    assert results[0][\"provider\"] == \"reddit_oauth_api\""` | — |
| [SRC-F725E90B2A-L000643](../../tests/test_web_agent.py#L643) | 643 | `"    assert results[0][\"url\"] == \"https://www.reddit.com/r/cars/comments/example/post/\""` | — |
| [SRC-F725E90B2A-L000644](../../tests/test_web_agent.py#L644) | 644 | `"    assert \"score=25\" in results[0][\"snippet\"]"` | — |
| [SRC-F725E90B2A-L000645](../../tests/test_web_agent.py#L645) | 645 | `"    assert len([call for call in calls if call[0] == \"POST\"]) == 1"` | — |
| [SRC-F725E90B2A-L000646](../../tests/test_web_agent.py#L646) | 646 | `"    assert any(\"oauth.reddit.com/search\" in call[1] for call in calls if call[0] == \"GET\")"` | — |
| [SRC-F725E90B2A-L000647](../../tests/test_web_agent.py#L647) | 647 | `"    assert \"test-reddit-access-token\" not in str(results)"` | — |
| [SRC-F725E90B2A-L000648](../../tests/test_web_agent.py#L648) | 648 | `""` | — |
| [SRC-F725E90B2A-L000649](../../tests/test_web_agent.py#L649) | 649 | `""` | — |
| [SRC-F725E90B2A-L000650](../../tests/test_web_agent.py#L650) | 650 | `""` | — |
| [SRC-F725E90B2A-L000651](../../tests/test_web_agent.py#L651) | 651 | `"def test_role_models_are_explicit_and_have_a_fallback(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000652](../../tests/test_web_agent.py#L652) | 652 | `"    for name in ("` | — |
| [SRC-F725E90B2A-L000653](../../tests/test_web_agent.py#L653) | 653 | `"        \"OMARAI_LLM_MODEL\","` | — |
| [SRC-F725E90B2A-L000654](../../tests/test_web_agent.py#L654) | 654 | `"        \"OMARAI_PLANNER_MODEL\","` | — |
| [SRC-F725E90B2A-L000655](../../tests/test_web_agent.py#L655) | 655 | `"        \"OMARAI_ANSWER_MODEL\","` | — |
| [SRC-F725E90B2A-L000656](../../tests/test_web_agent.py#L656) | 656 | `"        \"OMARAI_REVIEW_MODEL\","` | — |
| [SRC-F725E90B2A-L000657](../../tests/test_web_agent.py#L657) | 657 | `"        \"OMARAI_LLM_FALLBACK_MODEL\","` | — |
| [SRC-F725E90B2A-L000658](../../tests/test_web_agent.py#L658) | 658 | `"    ):"` | — |
| [SRC-F725E90B2A-L000659](../../tests/test_web_agent.py#L659) | 659 | `"        monkeypatch.delenv(name, raising=False)"` | — |
| [SRC-F725E90B2A-L000660](../../tests/test_web_agent.py#L660) | 660 | `""` | — |
| [SRC-F725E90B2A-L000661](../../tests/test_web_agent.py#L661) | 661 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000662](../../tests/test_web_agent.py#L662) | 662 | `"    assert agent.planner_model == \"nvidia/nemotron-3-ultra-550b-a55b:free\""` | — |
| [SRC-F725E90B2A-L000663](../../tests/test_web_agent.py#L663) | 663 | `"    assert agent.answer_model == \"google/gemma-4-31b-it:free\""` | — |
| [SRC-F725E90B2A-L000664](../../tests/test_web_agent.py#L664) | 664 | `"    assert agent.review_model == agent.answer_model"` | — |
| [SRC-F725E90B2A-L000665](../../tests/test_web_agent.py#L665) | 665 | `"    assert agent.fallback_model == \"openrouter/free\""` | — |
| [SRC-F725E90B2A-L000666](../../tests/test_web_agent.py#L666) | 666 | `""` | — |
| [SRC-F725E90B2A-L000667](../../tests/test_web_agent.py#L667) | 667 | `""` | — |
| [SRC-F725E90B2A-L000668](../../tests/test_web_agent.py#L668) | 668 | `"def test_global_model_override_is_preserved_for_existing_users(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000669](../../tests/test_web_agent.py#L669) | 669 | `"    monkeypatch.setenv(\"OMARAI_LLM_MODEL\", \"example/custom-model\")"` | — |
| [SRC-F725E90B2A-L000670](../../tests/test_web_agent.py#L670) | 670 | `"    monkeypatch.delenv(\"OMARAI_PLANNER_MODEL\", raising=False)"` | — |
| [SRC-F725E90B2A-L000671](../../tests/test_web_agent.py#L671) | 671 | `"    monkeypatch.delenv(\"OMARAI_ANSWER_MODEL\", raising=False)"` | — |
| [SRC-F725E90B2A-L000672](../../tests/test_web_agent.py#L672) | 672 | `"    monkeypatch.delenv(\"OMARAI_REVIEW_MODEL\", raising=False)"` | — |
| [SRC-F725E90B2A-L000673](../../tests/test_web_agent.py#L673) | 673 | `""` | — |
| [SRC-F725E90B2A-L000674](../../tests/test_web_agent.py#L674) | 674 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000675](../../tests/test_web_agent.py#L675) | 675 | `"    assert agent.planner_model == \"example/custom-model\""` | — |
| [SRC-F725E90B2A-L000676](../../tests/test_web_agent.py#L676) | 676 | `"    assert agent.answer_model == \"example/custom-model\""` | — |
| [SRC-F725E90B2A-L000677](../../tests/test_web_agent.py#L677) | 677 | `"    assert agent.review_model == \"example/custom-model\""` | — |
| [SRC-F725E90B2A-L000678](../../tests/test_web_agent.py#L678) | 678 | `""` | — |
| [SRC-F725E90B2A-L000679](../../tests/test_web_agent.py#L679) | 679 | `""` | — |
| [SRC-F725E90B2A-L000680](../../tests/test_web_agent.py#L680) | 680 | `"def test_completion_uses_fallback_model_after_primary_http_error(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000681](../../tests/test_web_agent.py#L681) | 681 | `"    import io"` | — |
| [SRC-F725E90B2A-L000682](../../tests/test_web_agent.py#L682) | 682 | `"    import json"` | — |
| [SRC-F725E90B2A-L000683](../../tests/test_web_agent.py#L683) | 683 | `"    import urllib.error"` | — |
| [SRC-F725E90B2A-L000684](../../tests/test_web_agent.py#L684) | 684 | `""` | — |
| [SRC-F725E90B2A-L000685](../../tests/test_web_agent.py#L685) | 685 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000686](../../tests/test_web_agent.py#L686) | 686 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L000687](../../tests/test_web_agent.py#L687) | 687 | `"    agent.fallback_model = \"openrouter/free\""` | — |
| [SRC-F725E90B2A-L000688](../../tests/test_web_agent.py#L688) | 688 | `"    called = []"` | — |
| [SRC-F725E90B2A-L000689](../../tests/test_web_agent.py#L689) | 689 | `""` | — |
| [SRC-F725E90B2A-L000690](../../tests/test_web_agent.py#L690) | 690 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L000691](../../tests/test_web_agent.py#L691) | 691 | `"        def __enter__(self):"` | — |
| [SRC-F725E90B2A-L000692](../../tests/test_web_agent.py#L692) | 692 | `"            return self"` | — |
| [SRC-F725E90B2A-L000693](../../tests/test_web_agent.py#L693) | 693 | `""` | — |
| [SRC-F725E90B2A-L000694](../../tests/test_web_agent.py#L694) | 694 | `"        def __exit__(self, exc_type, exc, traceback):"` | — |
| [SRC-F725E90B2A-L000695](../../tests/test_web_agent.py#L695) | 695 | `"            return False"` | — |
| [SRC-F725E90B2A-L000696](../../tests/test_web_agent.py#L696) | 696 | `""` | — |
| [SRC-F725E90B2A-L000697](../../tests/test_web_agent.py#L697) | 697 | `"        def read(self, limit):"` | — |
| [SRC-F725E90B2A-L000698](../../tests/test_web_agent.py#L698) | 698 | `"            return json.dumps({"` | — |
| [SRC-F725E90B2A-L000699](../../tests/test_web_agent.py#L699) | 699 | `"                \"choices\": [{"` | — |
| [SRC-F725E90B2A-L000700](../../tests/test_web_agent.py#L700) | 700 | `"                    \"message\": {\"content\": \"إجابة من النموذج الاحتياطي\"},"` | — |
| [SRC-F725E90B2A-L000701](../../tests/test_web_agent.py#L701) | 701 | `"                    \"finish_reason\": \"stop\","` | — |
| [SRC-F725E90B2A-L000702](../../tests/test_web_agent.py#L702) | 702 | `"                }]"` | — |
| [SRC-F725E90B2A-L000703](../../tests/test_web_agent.py#L703) | 703 | `"            }).encode(\"utf-8\")"` | — |
| [SRC-F725E90B2A-L000704](../../tests/test_web_agent.py#L704) | 704 | `""` | — |
| [SRC-F725E90B2A-L000705](../../tests/test_web_agent.py#L705) | 705 | `"    def fake_urlopen(request, timeout):"` | — |
| [SRC-F725E90B2A-L000706](../../tests/test_web_agent.py#L706) | 706 | `"        payload = json.loads(request.data.decode(\"utf-8\"))"` | — |
| [SRC-F725E90B2A-L000707](../../tests/test_web_agent.py#L707) | 707 | `"        called.append(payload[\"model\"])"` | — |
| [SRC-F725E90B2A-L000708](../../tests/test_web_agent.py#L708) | 708 | `"        if payload[\"model\"] == \"broken/primary\":"` | — |
| [SRC-F725E90B2A-L000709](../../tests/test_web_agent.py#L709) | 709 | `"            raise urllib.error.HTTPError("` | — |
| [SRC-F725E90B2A-L000710](../../tests/test_web_agent.py#L710) | 710 | `"                request.full_url,"` | — |
| [SRC-F725E90B2A-L000711](../../tests/test_web_agent.py#L711) | 711 | `"                503,"` | — |
| [SRC-F725E90B2A-L000712](../../tests/test_web_agent.py#L712) | 712 | `"                \"service unavailable\","` | — |
| [SRC-F725E90B2A-L000713](../../tests/test_web_agent.py#L713) | 713 | `"                hdrs=None,"` | — |
| [SRC-F725E90B2A-L000714](../../tests/test_web_agent.py#L714) | 714 | `"                fp=io.BytesIO(b\"private provider diagnostics\"),"` | — |
| [SRC-F725E90B2A-L000715](../../tests/test_web_agent.py#L715) | 715 | `"            )"` | — |
| [SRC-F725E90B2A-L000716](../../tests/test_web_agent.py#L716) | 716 | `"        return FakeResponse()"` | — |
| [SRC-F725E90B2A-L000717](../../tests/test_web_agent.py#L717) | 717 | `""` | — |
| [SRC-F725E90B2A-L000718](../../tests/test_web_agent.py#L718) | 718 | `"    monkeypatch.setattr(\"agents.web_agent.urllib.request.urlopen\", fake_urlopen)"` | — |
| [SRC-F725E90B2A-L000719](../../tests/test_web_agent.py#L719) | 719 | `"    result = agent._request_completion("` | — |
| [SRC-F725E90B2A-L000720](../../tests/test_web_agent.py#L720) | 720 | `"        [{\"role\": \"user\", \"content\": \"اختبار\"}],"` | — |
| [SRC-F725E90B2A-L000721](../../tests/test_web_agent.py#L721) | 721 | `"        model=\"broken/primary\","` | — |
| [SRC-F725E90B2A-L000722](../../tests/test_web_agent.py#L722) | 722 | `"    )"` | — |
| [SRC-F725E90B2A-L000723](../../tests/test_web_agent.py#L723) | 723 | `""` | — |
| [SRC-F725E90B2A-L000724](../../tests/test_web_agent.py#L724) | 724 | `"    assert result == \"إجابة من النموذج الاحتياطي\""` | — |
| [SRC-F725E90B2A-L000725](../../tests/test_web_agent.py#L725) | 725 | `"    assert called == [\"broken/primary\", \"openrouter/free\"]"` | — |
| [SRC-F725E90B2A-L000726](../../tests/test_web_agent.py#L726) | 726 | `"    assert agent.model_usage == [{"` | — |
| [SRC-F725E90B2A-L000727](../../tests/test_web_agent.py#L727) | 727 | `"        \"requested_model\": \"broken/primary\","` | — |
| [SRC-F725E90B2A-L000728](../../tests/test_web_agent.py#L728) | 728 | `"        \"used_model\": \"openrouter/free\","` | — |
| [SRC-F725E90B2A-L000729](../../tests/test_web_agent.py#L729) | 729 | `"        \"fallback_used\": \"true\","` | — |
| [SRC-F725E90B2A-L000730](../../tests/test_web_agent.py#L730) | 730 | `"    }]"` | — |
| [SRC-F725E90B2A-L000731](../../tests/test_web_agent.py#L731) | 731 | `""` | — |
| [SRC-F725E90B2A-L000732](../../tests/test_web_agent.py#L732) | 732 | `""` | — |
| [SRC-F725E90B2A-L000733](../../tests/test_web_agent.py#L733) | 733 | `""` | — |
| [SRC-F725E90B2A-L000734](../../tests/test_web_agent.py#L734) | 734 | `""` | — |
| [SRC-F725E90B2A-L000735](../../tests/test_web_agent.py#L735) | 735 | `"def test_generator_rejects_silent_character_limit_truncation(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000736](../../tests/test_web_agent.py#L736) | 736 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000737](../../tests/test_web_agent.py#L737) | 737 | `"    monkeypatch.setattr(agent, \"_request_completion\", lambda *args, **kwargs: \"ن\" * 24_001)"` | — |
| [SRC-F725E90B2A-L000738](../../tests/test_web_agent.py#L738) | 738 | `""` | — |
| [SRC-F725E90B2A-L000739](../../tests/test_web_agent.py#L739) | 739 | `"    with pytest.raises(RuntimeError, match=\"تجاوزت حد طول النص\"):"` | — |
| [SRC-F725E90B2A-L000740](../../tests/test_web_agent.py#L740) | 740 | `"        agent._generate("` | — |
| [SRC-F725E90B2A-L000741](../../tests/test_web_agent.py#L741) | 741 | `"            question=\"لخص هذا المصدر\","` | — |
| [SRC-F725E90B2A-L000742](../../tests/test_web_agent.py#L742) | 742 | `"            history=[],"` | — |
| [SRC-F725E90B2A-L000743](../../tests/test_web_agent.py#L743) | 743 | `"            sources=[sample_source(0), sample_source(1)],"` | — |
| [SRC-F725E90B2A-L000744](../../tests/test_web_agent.py#L744) | 744 | `"            search_warning=None,"` | — |
| [SRC-F725E90B2A-L000745](../../tests/test_web_agent.py#L745) | 745 | `"            research_plan={\"depth\": \"standard\", \"queries\": [\"لخص هذا المصدر\"]},"` | — |
| [SRC-F725E90B2A-L000746](../../tests/test_web_agent.py#L746) | 746 | `"            search_report={},"` | — |
| [SRC-F725E90B2A-L000747](../../tests/test_web_agent.py#L747) | 747 | `"        )"` | — |
| [SRC-F725E90B2A-L000748](../../tests/test_web_agent.py#L748) | 748 | `""` | — |
| [SRC-F725E90B2A-L000749](../../tests/test_web_agent.py#L749) | 749 | `""` | — |
| [SRC-F725E90B2A-L000750](../../tests/test_web_agent.py#L750) | 750 | `"def test_completion_discards_truncated_primary_and_uses_complete_fallback(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000751](../../tests/test_web_agent.py#L751) | 751 | `"    import json"` | — |
| [SRC-F725E90B2A-L000752](../../tests/test_web_agent.py#L752) | 752 | `""` | — |
| [SRC-F725E90B2A-L000753](../../tests/test_web_agent.py#L753) | 753 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000754](../../tests/test_web_agent.py#L754) | 754 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L000755](../../tests/test_web_agent.py#L755) | 755 | `"    agent.fallback_model = \"openrouter/free\""` | — |
| [SRC-F725E90B2A-L000756](../../tests/test_web_agent.py#L756) | 756 | `"    called = []"` | — |
| [SRC-F725E90B2A-L000757](../../tests/test_web_agent.py#L757) | 757 | `""` | — |
| [SRC-F725E90B2A-L000758](../../tests/test_web_agent.py#L758) | 758 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L000759](../../tests/test_web_agent.py#L759) | 759 | `"        def __init__(self, content, finish_reason):"` | — |
| [SRC-F725E90B2A-L000760](../../tests/test_web_agent.py#L760) | 760 | `"            self.body = json.dumps({"` | — |
| [SRC-F725E90B2A-L000761](../../tests/test_web_agent.py#L761) | 761 | `"                \"choices\": [{"` | — |
| [SRC-F725E90B2A-L000762](../../tests/test_web_agent.py#L762) | 762 | `"                    \"message\": {\"content\": content},"` | — |
| [SRC-F725E90B2A-L000763](../../tests/test_web_agent.py#L763) | 763 | `"                    \"finish_reason\": finish_reason,"` | — |
| [SRC-F725E90B2A-L000764](../../tests/test_web_agent.py#L764) | 764 | `"                }]"` | — |
| [SRC-F725E90B2A-L000765](../../tests/test_web_agent.py#L765) | 765 | `"            }).encode(\"utf-8\")"` | — |
| [SRC-F725E90B2A-L000766](../../tests/test_web_agent.py#L766) | 766 | `""` | — |
| [SRC-F725E90B2A-L000767](../../tests/test_web_agent.py#L767) | 767 | `"        def __enter__(self):"` | — |
| [SRC-F725E90B2A-L000768](../../tests/test_web_agent.py#L768) | 768 | `"            return self"` | — |
| [SRC-F725E90B2A-L000769](../../tests/test_web_agent.py#L769) | 769 | `""` | — |
| [SRC-F725E90B2A-L000770](../../tests/test_web_agent.py#L770) | 770 | `"        def __exit__(self, exc_type, exc, traceback):"` | — |
| [SRC-F725E90B2A-L000771](../../tests/test_web_agent.py#L771) | 771 | `"            return False"` | — |
| [SRC-F725E90B2A-L000772](../../tests/test_web_agent.py#L772) | 772 | `""` | — |
| [SRC-F725E90B2A-L000773](../../tests/test_web_agent.py#L773) | 773 | `"        def read(self, limit):"` | — |
| [SRC-F725E90B2A-L000774](../../tests/test_web_agent.py#L774) | 774 | `"            return self.body"` | — |
| [SRC-F725E90B2A-L000775](../../tests/test_web_agent.py#L775) | 775 | `""` | — |
| [SRC-F725E90B2A-L000776](../../tests/test_web_agent.py#L776) | 776 | `"    def fake_urlopen(request, timeout):"` | — |
| [SRC-F725E90B2A-L000777](../../tests/test_web_agent.py#L777) | 777 | `"        model = json.loads(request.data.decode(\"utf-8\"))[\"model\"]"` | — |
| [SRC-F725E90B2A-L000778](../../tests/test_web_agent.py#L778) | 778 | `"        called.append(model)"` | — |
| [SRC-F725E90B2A-L000779](../../tests/test_web_agent.py#L779) | 779 | `"        if model == \"broken/primary\":"` | — |
| [SRC-F725E90B2A-L000780](../../tests/test_web_agent.py#L780) | 780 | `"            return FakeResponse(\"جزء مبتور لا يجوز عرضه\", \"length\")"` | — |
| [SRC-F725E90B2A-L000781](../../tests/test_web_agent.py#L781) | 781 | `"        return FakeResponse(\"إجابة مكتملة\", \"stop\")"` | — |
| [SRC-F725E90B2A-L000782](../../tests/test_web_agent.py#L782) | 782 | `""` | — |
| [SRC-F725E90B2A-L000783](../../tests/test_web_agent.py#L783) | 783 | `"    monkeypatch.setattr(\"agents.web_agent.urllib.request.urlopen\", fake_urlopen)"` | — |
| [SRC-F725E90B2A-L000784](../../tests/test_web_agent.py#L784) | 784 | `"    result = agent._request_completion("` | — |
| [SRC-F725E90B2A-L000785](../../tests/test_web_agent.py#L785) | 785 | `"        [{\"role\": \"user\", \"content\": \"اختبار\"}],"` | — |
| [SRC-F725E90B2A-L000786](../../tests/test_web_agent.py#L786) | 786 | `"        model=\"broken/primary\","` | — |
| [SRC-F725E90B2A-L000787](../../tests/test_web_agent.py#L787) | 787 | `"    )"` | — |
| [SRC-F725E90B2A-L000788](../../tests/test_web_agent.py#L788) | 788 | `""` | — |
| [SRC-F725E90B2A-L000789](../../tests/test_web_agent.py#L789) | 789 | `"    assert result == \"إجابة مكتملة\""` | — |
| [SRC-F725E90B2A-L000790](../../tests/test_web_agent.py#L790) | 790 | `"    assert called == [\"broken/primary\", \"openrouter/free\"]"` | — |
| [SRC-F725E90B2A-L000791](../../tests/test_web_agent.py#L791) | 791 | `"    assert \"جزء مبتور لا يجوز عرضه\" not in result"` | — |
| [SRC-F725E90B2A-L000792](../../tests/test_web_agent.py#L792) | 792 | `"    assert agent.model_usage == [{"` | — |
| [SRC-F725E90B2A-L000793](../../tests/test_web_agent.py#L793) | 793 | `"        \"requested_model\": \"broken/primary\","` | — |
| [SRC-F725E90B2A-L000794](../../tests/test_web_agent.py#L794) | 794 | `"        \"used_model\": \"openrouter/free\","` | — |
| [SRC-F725E90B2A-L000795](../../tests/test_web_agent.py#L795) | 795 | `"        \"fallback_used\": \"true\","` | — |
| [SRC-F725E90B2A-L000796](../../tests/test_web_agent.py#L796) | 796 | `"    }]"` | — |
| [SRC-F725E90B2A-L000797](../../tests/test_web_agent.py#L797) | 797 | `""` | — |
| [SRC-F725E90B2A-L000798](../../tests/test_web_agent.py#L798) | 798 | `""` | — |
| [SRC-F725E90B2A-L000799](../../tests/test_web_agent.py#L799) | 799 | `"def test_completion_rejects_response_when_all_models_are_truncated(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000800](../../tests/test_web_agent.py#L800) | 800 | `"    import json"` | — |
| [SRC-F725E90B2A-L000801](../../tests/test_web_agent.py#L801) | 801 | `""` | — |
| [SRC-F725E90B2A-L000802](../../tests/test_web_agent.py#L802) | 802 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000803](../../tests/test_web_agent.py#L803) | 803 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L000804](../../tests/test_web_agent.py#L804) | 804 | `"    agent.fallback_model = \"fallback/model\""` | — |
| [SRC-F725E90B2A-L000805](../../tests/test_web_agent.py#L805) | 805 | `"    called = []"` | — |
| [SRC-F725E90B2A-L000806](../../tests/test_web_agent.py#L806) | 806 | `""` | — |
| [SRC-F725E90B2A-L000807](../../tests/test_web_agent.py#L807) | 807 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L000808](../../tests/test_web_agent.py#L808) | 808 | `"        def __enter__(self):"` | — |
| [SRC-F725E90B2A-L000809](../../tests/test_web_agent.py#L809) | 809 | `"            return self"` | — |
| [SRC-F725E90B2A-L000810](../../tests/test_web_agent.py#L810) | 810 | `""` | — |
| [SRC-F725E90B2A-L000811](../../tests/test_web_agent.py#L811) | 811 | `"        def __exit__(self, exc_type, exc, traceback):"` | — |
| [SRC-F725E90B2A-L000812](../../tests/test_web_agent.py#L812) | 812 | `"            return False"` | — |
| [SRC-F725E90B2A-L000813](../../tests/test_web_agent.py#L813) | 813 | `""` | — |
| [SRC-F725E90B2A-L000814](../../tests/test_web_agent.py#L814) | 814 | `"        def read(self, limit):"` | — |
| [SRC-F725E90B2A-L000815](../../tests/test_web_agent.py#L815) | 815 | `"            return json.dumps({"` | — |
| [SRC-F725E90B2A-L000816](../../tests/test_web_agent.py#L816) | 816 | `"                \"choices\": [{"` | — |
| [SRC-F725E90B2A-L000817](../../tests/test_web_agent.py#L817) | 817 | `"                    \"message\": {\"content\": \"نص مبتور\"},"` | — |
| [SRC-F725E90B2A-L000818](../../tests/test_web_agent.py#L818) | 818 | `"                    \"finish_reason\": \"length\","` | — |
| [SRC-F725E90B2A-L000819](../../tests/test_web_agent.py#L819) | 819 | `"                }]"` | — |
| [SRC-F725E90B2A-L000820](../../tests/test_web_agent.py#L820) | 820 | `"            }).encode(\"utf-8\")"` | — |
| [SRC-F725E90B2A-L000821](../../tests/test_web_agent.py#L821) | 821 | `""` | — |
| [SRC-F725E90B2A-L000822](../../tests/test_web_agent.py#L822) | 822 | `"    def fake_urlopen(request, timeout):"` | — |
| [SRC-F725E90B2A-L000823](../../tests/test_web_agent.py#L823) | 823 | `"        called.append(json.loads(request.data.decode(\"utf-8\"))[\"model\"])"` | — |
| [SRC-F725E90B2A-L000824](../../tests/test_web_agent.py#L824) | 824 | `"        return FakeResponse()"` | — |
| [SRC-F725E90B2A-L000825](../../tests/test_web_agent.py#L825) | 825 | `""` | — |
| [SRC-F725E90B2A-L000826](../../tests/test_web_agent.py#L826) | 826 | `"    monkeypatch.setattr(\"agents.web_agent.urllib.request.urlopen\", fake_urlopen)"` | — |
| [SRC-F725E90B2A-L000827](../../tests/test_web_agent.py#L827) | 827 | `"    with pytest.raises(RuntimeError, match=\"مبتورة\"):"` | — |
| [SRC-F725E90B2A-L000828](../../tests/test_web_agent.py#L828) | 828 | `"        agent._request_completion("` | — |
| [SRC-F725E90B2A-L000829](../../tests/test_web_agent.py#L829) | 829 | `"            [{\"role\": \"user\", \"content\": \"اختبار\"}],"` | — |
| [SRC-F725E90B2A-L000830](../../tests/test_web_agent.py#L830) | 830 | `"            model=\"broken/primary\","` | — |
| [SRC-F725E90B2A-L000831](../../tests/test_web_agent.py#L831) | 831 | `"        )"` | — |
| [SRC-F725E90B2A-L000832](../../tests/test_web_agent.py#L832) | 832 | `""` | — |
| [SRC-F725E90B2A-L000833](../../tests/test_web_agent.py#L833) | 833 | `"    assert called == [\"broken/primary\", \"fallback/model\"]"` | — |
| [SRC-F725E90B2A-L000834](../../tests/test_web_agent.py#L834) | 834 | `"    assert agent.model_usage == []"` | — |
| [SRC-F725E90B2A-L000835](../../tests/test_web_agent.py#L835) | 835 | `""` | — |
| [SRC-F725E90B2A-L000836](../../tests/test_web_agent.py#L836) | 836 | `""` | — |
| [SRC-F725E90B2A-L000837](../../tests/test_web_agent.py#L837) | 837 | `"def test_completion_falls_back_for_malformed_choice(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000838](../../tests/test_web_agent.py#L838) | 838 | `"    import json"` | — |
| [SRC-F725E90B2A-L000839](../../tests/test_web_agent.py#L839) | 839 | `""` | — |
| [SRC-F725E90B2A-L000840](../../tests/test_web_agent.py#L840) | 840 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000841](../../tests/test_web_agent.py#L841) | 841 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L000842](../../tests/test_web_agent.py#L842) | 842 | `"    agent.fallback_model = \"fallback/model\""` | — |
| [SRC-F725E90B2A-L000843](../../tests/test_web_agent.py#L843) | 843 | `"    called = []"` | — |
| [SRC-F725E90B2A-L000844](../../tests/test_web_agent.py#L844) | 844 | `""` | — |
| [SRC-F725E90B2A-L000845](../../tests/test_web_agent.py#L845) | 845 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L000846](../../tests/test_web_agent.py#L846) | 846 | `"        def __init__(self, body):"` | — |
| [SRC-F725E90B2A-L000847](../../tests/test_web_agent.py#L847) | 847 | `"            self.body = body"` | — |
| [SRC-F725E90B2A-L000848](../../tests/test_web_agent.py#L848) | 848 | `""` | — |
| [SRC-F725E90B2A-L000849](../../tests/test_web_agent.py#L849) | 849 | `"        def __enter__(self):"` | — |
| [SRC-F725E90B2A-L000850](../../tests/test_web_agent.py#L850) | 850 | `"            return self"` | — |
| [SRC-F725E90B2A-L000851](../../tests/test_web_agent.py#L851) | 851 | `""` | — |
| [SRC-F725E90B2A-L000852](../../tests/test_web_agent.py#L852) | 852 | `"        def __exit__(self, exc_type, exc, traceback):"` | — |
| [SRC-F725E90B2A-L000853](../../tests/test_web_agent.py#L853) | 853 | `"            return False"` | — |
| [SRC-F725E90B2A-L000854](../../tests/test_web_agent.py#L854) | 854 | `""` | — |
| [SRC-F725E90B2A-L000855](../../tests/test_web_agent.py#L855) | 855 | `"        def read(self, limit):"` | — |
| [SRC-F725E90B2A-L000856](../../tests/test_web_agent.py#L856) | 856 | `"            return self.body"` | — |
| [SRC-F725E90B2A-L000857](../../tests/test_web_agent.py#L857) | 857 | `""` | — |
| [SRC-F725E90B2A-L000858](../../tests/test_web_agent.py#L858) | 858 | `"    def fake_urlopen(request, timeout):"` | — |
| [SRC-F725E90B2A-L000859](../../tests/test_web_agent.py#L859) | 859 | `"        model = json.loads(request.data.decode(\"utf-8\"))[\"model\"]"` | — |
| [SRC-F725E90B2A-L000860](../../tests/test_web_agent.py#L860) | 860 | `"        called.append(model)"` | — |
| [SRC-F725E90B2A-L000861](../../tests/test_web_agent.py#L861) | 861 | `"        choices = ("` | — |
| [SRC-F725E90B2A-L000862](../../tests/test_web_agent.py#L862) | 862 | `"            [\"malformed choice\"]"` | — |
| [SRC-F725E90B2A-L000863](../../tests/test_web_agent.py#L863) | 863 | `"            if model == \"broken/primary\""` | — |
| [SRC-F725E90B2A-L000864](../../tests/test_web_agent.py#L864) | 864 | `"            else [{\"message\": {\"content\": \"fallback answer\"}, \"finish_reason\": \"stop\"}]"` | — |
| [SRC-F725E90B2A-L000865](../../tests/test_web_agent.py#L865) | 865 | `"        )"` | — |
| [SRC-F725E90B2A-L000866](../../tests/test_web_agent.py#L866) | 866 | `"        return FakeResponse(json.dumps({\"choices\": choices}).encode(\"utf-8\"))"` | — |
| [SRC-F725E90B2A-L000867](../../tests/test_web_agent.py#L867) | 867 | `""` | — |
| [SRC-F725E90B2A-L000868](../../tests/test_web_agent.py#L868) | 868 | `"    monkeypatch.setattr(\"agents.web_agent.urllib.request.urlopen\", fake_urlopen)"` | — |
| [SRC-F725E90B2A-L000869](../../tests/test_web_agent.py#L869) | 869 | `"    result = agent._request_completion("` | — |
| [SRC-F725E90B2A-L000870](../../tests/test_web_agent.py#L870) | 870 | `"        [{\"role\": \"user\", \"content\": \"test\"}],"` | — |
| [SRC-F725E90B2A-L000871](../../tests/test_web_agent.py#L871) | 871 | `"        model=\"broken/primary\","` | — |
| [SRC-F725E90B2A-L000872](../../tests/test_web_agent.py#L872) | 872 | `"    )"` | — |
| [SRC-F725E90B2A-L000873](../../tests/test_web_agent.py#L873) | 873 | `""` | — |
| [SRC-F725E90B2A-L000874](../../tests/test_web_agent.py#L874) | 874 | `"    assert result == \"fallback answer\""` | — |
| [SRC-F725E90B2A-L000875](../../tests/test_web_agent.py#L875) | 875 | `"    assert called == [\"broken/primary\", \"fallback/model\"]"` | — |
| [SRC-F725E90B2A-L000876](../../tests/test_web_agent.py#L876) | 876 | `""` | — |
| [SRC-F725E90B2A-L000877](../../tests/test_web_agent.py#L877) | 877 | `""` | — |
| [SRC-F725E90B2A-L000878](../../tests/test_web_agent.py#L878) | 878 | `"def test_health_status_reports_models_without_credentials(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000879](../../tests/test_web_agent.py#L879) | 879 | `"    monkeypatch.delenv(\"OPENROUTER_API_KEY\", raising=False)"` | — |
| [SRC-F725E90B2A-L000880](../../tests/test_web_agent.py#L880) | 880 | `"    monkeypatch.delenv(\"OMARAI_LLM_API_KEY\", raising=False)"` | — |
| [SRC-F725E90B2A-L000881](../../tests/test_web_agent.py#L881) | 881 | `"    status = WebAgent.status()"` | — |
| [SRC-F725E90B2A-L000882](../../tests/test_web_agent.py#L882) | 882 | `"    assert status[\"planner_model\"] == \"nvidia/nemotron-3-ultra-550b-a55b:free\""` | — |
| [SRC-F725E90B2A-L000883](../../tests/test_web_agent.py#L883) | 883 | `"    assert status[\"answer_model\"] == \"google/gemma-4-31b-it:free\""` | — |
| [SRC-F725E90B2A-L000884](../../tests/test_web_agent.py#L884) | 884 | `"    assert status[\"fallback_model\"] == \"openrouter/free\""` | — |
| [SRC-F725E90B2A-L000885](../../tests/test_web_agent.py#L885) | 885 | `"    assert status[\"language_model_configured\"] is False"` | — |
| [SRC-F725E90B2A-L000886](../../tests/test_web_agent.py#L886) | 886 | `"    assert status[\"verification_scope\"][\"kind\"] == \"configuration_snapshot\""` | — |
| [SRC-F725E90B2A-L000887](../../tests/test_web_agent.py#L887) | 887 | `"    assert status[\"verification_scope\"][\"live_network_checks_performed\"] is False"` | — |
| [SRC-F725E90B2A-L000888](../../tests/test_web_agent.py#L888) | 888 | `"    assert status[\"verification_scope\"][\"language_model_configured_means\"] == ("` | — |
| [SRC-F725E90B2A-L000889](../../tests/test_web_agent.py#L889) | 889 | `"        \"credential_present_not_successful_completion\""` | — |
| [SRC-F725E90B2A-L000890](../../tests/test_web_agent.py#L890) | 890 | `"    )"` | — |
| [SRC-F725E90B2A-L000891](../../tests/test_web_agent.py#L891) | 891 | `"    assert status[\"verification_scope\"][\"live_diagnostics_endpoint\"] == \"POST /api/diagnostics\""` | — |
| [SRC-F725E90B2A-L000892](../../tests/test_web_agent.py#L892) | 892 | `"    assert \"api_key\" not in status"` | — |
| [SRC-F725E90B2A-L000893](../../tests/test_web_agent.py#L893) | 893 | `""` | — |
| [SRC-F725E90B2A-L000894](../../tests/test_web_agent.py#L894) | 894 | `""` | — |
| [SRC-F725E90B2A-L000895](../../tests/test_web_agent.py#L895) | 895 | `""` | — |
| [SRC-F725E90B2A-L000896](../../tests/test_web_agent.py#L896) | 896 | `"def test_health_status_exposes_external_model_privacy_notice_without_secrets(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000897](../../tests/test_web_agent.py#L897) | 897 | `"    monkeypatch.delenv(\"OPENROUTER_API_KEY\", raising=False)"` | — |
| [SRC-F725E90B2A-L000898](../../tests/test_web_agent.py#L898) | 898 | `"    monkeypatch.delenv(\"OMARAI_LLM_API_KEY\", raising=False)"` | — |
| [SRC-F725E90B2A-L000899](../../tests/test_web_agent.py#L899) | 899 | `"    status = WebAgent.status()"` | — |
| [SRC-F725E90B2A-L000900](../../tests/test_web_agent.py#L900) | 900 | `"    notice = status[\"external_model_privacy_notice\"]"` | — |
| [SRC-F725E90B2A-L000901](../../tests/test_web_agent.py#L901) | 901 | `"    assert \"external model provider\" in notice"` | — |
| [SRC-F725E90B2A-L000902](../../tests/test_web_agent.py#L902) | 902 | `"    assert \"personal/confidential customer data\" in notice"` | — |
| [SRC-F725E90B2A-L000903](../../tests/test_web_agent.py#L903) | 903 | `"    assert \"api_key\" not in status"` | — |
| [SRC-F725E90B2A-L000904](../../tests/test_web_agent.py#L904) | 904 | `"    assert \"OPENROUTER_API_KEY\" not in str(status)"` | — |
| [SRC-F725E90B2A-L000905](../../tests/test_web_agent.py#L905) | 905 | `""` | — |
| [SRC-F725E90B2A-L000906](../../tests/test_web_agent.py#L906) | 906 | `""` | — |
| [SRC-F725E90B2A-L000907](../../tests/test_web_agent.py#L907) | 907 | `""` | — |
| [SRC-F725E90B2A-L000908](../../tests/test_web_agent.py#L908) | 908 | `"def test_diagnostics_runs_real_search_and_can_skip_paid_or_rate_limited_model_calls(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000909](../../tests/test_web_agent.py#L909) | 909 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000910](../../tests/test_web_agent.py#L910) | 910 | `"    monkeypatch.setattr(agent, \"_search_web\", lambda query: ["` | — |
| [SRC-F725E90B2A-L000911](../../tests/test_web_agent.py#L911) | 911 | `"        {\"provider\": \"duckduckgo_html\", \"url\": \"https://example.com/a\"},"` | — |
| [SRC-F725E90B2A-L000912](../../tests/test_web_agent.py#L912) | 912 | `"        {\"provider\": \"bing_rss\", \"url\": \"https://example.com/b\"},"` | — |
| [SRC-F725E90B2A-L000913](../../tests/test_web_agent.py#L913) | 913 | `"    ])"` | — |
| [SRC-F725E90B2A-L000914](../../tests/test_web_agent.py#L914) | 914 | `"    monkeypatch.setattr("` | — |
