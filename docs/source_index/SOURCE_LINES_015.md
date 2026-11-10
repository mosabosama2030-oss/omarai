# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **015**
- سجلات الأسطر: **800**
- النطاق: SRC-1AE03B9EC3-L002040 إلى SRC-1AE03B9EC3-L002839
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-1AE03B9EC3 — [agents/web_agent.py](../../agents/web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1AE03B9EC3-L002040](../../agents/web_agent.py#L2040) | 2040 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L002041](../../agents/web_agent.py#L2041) | 2041 | `"                    normalized_item = dict(item)"` | — |
| [SRC-1AE03B9EC3-L002042](../../agents/web_agent.py#L2042) | 2042 | `"                    normalized_item[\"url\"] = safe_url"` | — |
| [SRC-1AE03B9EC3-L002043](../../agents/web_agent.py#L2043) | 2043 | `"                    normalized_item.setdefault(\"provider\", name)"` | — |
| [SRC-1AE03B9EC3-L002044](../../agents/web_agent.py#L2044) | 2044 | `"                    normalized_item.setdefault(\"search_query\", search_query)"` | — |
| [SRC-1AE03B9EC3-L002045](../../agents/web_agent.py#L2045) | 2045 | `"                    evidence = \" \".join(str(normalized_item.get(k) or \"\") for k in (\"title\", \"snippet\"))"` | — |
| [SRC-1AE03B9EC3-L002046](../../agents/web_agent.py#L2046) | 2046 | `"                    if _relevance_ratio(search_query, evidence) < _minimum_relevance_ratio(search_query):"` | — |
| [SRC-1AE03B9EC3-L002047](../../agents/web_agent.py#L2047) | 2047 | `"                        rejected += 1"` | — |
| [SRC-1AE03B9EC3-L002048](../../agents/web_agent.py#L2048) | 2048 | `"                        rejection_counts[\"relevance_below_threshold\"] += 1"` | — |
| [SRC-1AE03B9EC3-L002049](../../agents/web_agent.py#L2049) | 2049 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L002050](../../agents/web_agent.py#L2050) | 2050 | `"                    accepted.append(normalized_item)"` | — |
| [SRC-1AE03B9EC3-L002051](../../agents/web_agent.py#L2051) | 2051 | `"                if accepted:"` | — |
| [SRC-1AE03B9EC3-L002052](../../agents/web_agent.py#L2052) | 2052 | `"                    status = \"ok\""` | — |
| [SRC-1AE03B9EC3-L002053](../../agents/web_agent.py#L2053) | 2053 | `"                    error = None"` | — |
| [SRC-1AE03B9EC3-L002054](../../agents/web_agent.py#L2054) | 2054 | `"                elif raw:"` | — |
| [SRC-1AE03B9EC3-L002055](../../agents/web_agent.py#L2055) | 2055 | `"                    status = \"filtered_all\""` | — |
| [SRC-1AE03B9EC3-L002056](../../agents/web_agent.py#L2056) | 2056 | `"                    details = \", \".join("` | — |
| [SRC-1AE03B9EC3-L002057](../../agents/web_agent.py#L2057) | 2057 | `"                        f\"{reason}={count}\" for reason, count in rejection_counts.items() if count"` | — |
| [SRC-1AE03B9EC3-L002058](../../agents/web_agent.py#L2058) | 2058 | `"                    ) or \"no reason counters recorded\""` | — |
| [SRC-1AE03B9EC3-L002059](../../agents/web_agent.py#L2059) | 2059 | `"                    error = f\"all candidates rejected; {details}\""` | — |
| [SRC-1AE03B9EC3-L002060](../../agents/web_agent.py#L2060) | 2060 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L002061](../../agents/web_agent.py#L2061) | 2061 | `"                    status = \"no_results\""` | — |
| [SRC-1AE03B9EC3-L002062](../../agents/web_agent.py#L2062) | 2062 | `"                    error = \"connector returned no parseable results\""` | — |
| [SRC-1AE03B9EC3-L002063](../../agents/web_agent.py#L2063) | 2063 | `"                self._record_provider_diagnostic("` | — |
| [SRC-1AE03B9EC3-L002064](../../agents/web_agent.py#L2064) | 2064 | `"                    name, search_query, status, len(raw), rejected, error,"` | — |
| [SRC-1AE03B9EC3-L002065](../../agents/web_agent.py#L2065) | 2065 | `"                    accepted_count=len(accepted), rejection_counts=rejection_counts if raw else None,"` | — |
| [SRC-1AE03B9EC3-L002066](../../agents/web_agent.py#L2066) | 2066 | `"                )"` | — |
| [SRC-1AE03B9EC3-L002067](../../agents/web_agent.py#L2067) | 2067 | `"                return accepted"` | — |
| [SRC-1AE03B9EC3-L002068](../../agents/web_agent.py#L2068) | 2068 | `"            except RequestBudgetExceeded as exc:"` | — |
| [SRC-1AE03B9EC3-L002069](../../agents/web_agent.py#L2069) | 2069 | `"                self._record_provider_diagnostic("` | — |
| [SRC-1AE03B9EC3-L002070](../../agents/web_agent.py#L2070) | 2070 | `"                    name, search_query, \"budget_exhausted\", error=str(exc)"` | — |
| [SRC-1AE03B9EC3-L002071](../../agents/web_agent.py#L2071) | 2071 | `"                )"` | — |
| [SRC-1AE03B9EC3-L002072](../../agents/web_agent.py#L2072) | 2072 | `"            except TimeoutError:"` | — |
| [SRC-1AE03B9EC3-L002073](../../agents/web_agent.py#L2073) | 2073 | `"                self._record_provider_diagnostic("` | — |
| [SRC-1AE03B9EC3-L002074](../../agents/web_agent.py#L2074) | 2074 | `"                    name, search_query, \"timeout\", error=\"provider exceeded its bounded request timeout\""` | — |
| [SRC-1AE03B9EC3-L002075](../../agents/web_agent.py#L2075) | 2075 | `"                )"` | — |
| [SRC-1AE03B9EC3-L002076](../../agents/web_agent.py#L2076) | 2076 | `"            except Exception as exc:  # noqa: BLE001 - isolate a connector without leaking provider bodies/secrets"` | — |
| [SRC-1AE03B9EC3-L002077](../../agents/web_agent.py#L2077) | 2077 | `"                if type(exc).__name__ == \"DecodingError\":"` | — |
| [SRC-1AE03B9EC3-L002078](../../agents/web_agent.py#L2078) | 2078 | `"                    detail = \"provider response decoding failed\""` | — |
| [SRC-1AE03B9EC3-L002079](../../agents/web_agent.py#L2079) | 2079 | `"                    status = \"invalid_response\""` | — |
| [SRC-1AE03B9EC3-L002080](../../agents/web_agent.py#L2080) | 2080 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L002081](../../agents/web_agent.py#L2081) | 2081 | `"                    detail = f\"{type(exc).__name__}: {exc}\" if isinstance(exc, RuntimeError) else type(exc).__name__"` | — |
| [SRC-1AE03B9EC3-L002082](../../agents/web_agent.py#L2082) | 2082 | `"                    status = \"failed\""` | — |
| [SRC-1AE03B9EC3-L002083](../../agents/web_agent.py#L2083) | 2083 | `"                    status_match = re.search(r\"(?i)\\bHTTP\\s+(\\d{3})\\b\", str(exc))"` | — |
| [SRC-1AE03B9EC3-L002084](../../agents/web_agent.py#L2084) | 2084 | `"                    if status_match:"` | — |
| [SRC-1AE03B9EC3-L002085](../../agents/web_agent.py#L2085) | 2085 | `"                        status_code = int(status_match.group(1))"` | — |
| [SRC-1AE03B9EC3-L002086](../../agents/web_agent.py#L2086) | 2086 | `"                        if status_code == 202:"` | — |
| [SRC-1AE03B9EC3-L002087](../../agents/web_agent.py#L2087) | 2087 | `"                            status = \"blocked\""` | — |
| [SRC-1AE03B9EC3-L002088](../../agents/web_agent.py#L2088) | 2088 | `"                        elif status_code == 429:"` | — |
| [SRC-1AE03B9EC3-L002089](../../agents/web_agent.py#L2089) | 2089 | `"                            status = \"rate_limited\""` | — |
| [SRC-1AE03B9EC3-L002090](../../agents/web_agent.py#L2090) | 2090 | `"                        elif status_code in {401, 403}:"` | — |
| [SRC-1AE03B9EC3-L002091](../../agents/web_agent.py#L2091) | 2091 | `"                            status = \"unauthorized\""` | — |
| [SRC-1AE03B9EC3-L002092](../../agents/web_agent.py#L2092) | 2092 | `"                        elif 300 <= status_code < 600:"` | — |
| [SRC-1AE03B9EC3-L002093](../../agents/web_agent.py#L2093) | 2093 | `"                            # Do not bypass redirects/challenges or retry a blocked response."` | — |
| [SRC-1AE03B9EC3-L002094](../../agents/web_agent.py#L2094) | 2094 | `"                            status = \"http_error\""` | — |
| [SRC-1AE03B9EC3-L002095](../../agents/web_agent.py#L2095) | 2095 | `"                self._record_provider_diagnostic(name, search_query, status, error=detail)"` | — |
| [SRC-1AE03B9EC3-L002096](../../agents/web_agent.py#L2096) | 2096 | `"            return []"` | — |
| [SRC-1AE03B9EC3-L002097](../../agents/web_agent.py#L2097) | 2097 | `""` | — |
| [SRC-1AE03B9EC3-L002098](../../agents/web_agent.py#L2098) | 2098 | `"        async def run_all() -> list[list[dict[str, Any]]]:"` | — |
| [SRC-1AE03B9EC3-L002099](../../agents/web_agent.py#L2099) | 2099 | `"            return await asyncio.gather(*(run_one(name, method) for name, method in adapters))"` | — |
| [SRC-1AE03B9EC3-L002100](../../agents/web_agent.py#L2100) | 2100 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L002101](../../agents/web_agent.py#L2101) | 2101 | `"            provider_batches = asyncio.run(run_all())"` | — |
| [SRC-1AE03B9EC3-L002102](../../agents/web_agent.py#L2102) | 2102 | `"            combined = [item for batch in provider_batches for item in batch]"` | — |
| [SRC-1AE03B9EC3-L002103](../../agents/web_agent.py#L2103) | 2103 | `"            # Scholarly fallback only for explicit research-shaped queries; reuse"` | — |
| [SRC-1AE03B9EC3-L002104](../../agents/web_agent.py#L2104) | 2104 | `"            # run_one so budget, timeouts, public-URL/SSRF, blocklist and relevance"` | — |
| [SRC-1AE03B9EC3-L002105](../../agents/web_agent.py#L2105) | 2105 | `"            # validation are identical to ordinary search connectors."` | — |
| [SRC-1AE03B9EC3-L002106](../../agents/web_agent.py#L2106) | 2106 | `"            academic_markers = ("` | — |
| [SRC-1AE03B9EC3-L002107](../../agents/web_agent.py#L2107) | 2107 | `"                \"دراسة علمية\", \"دراسات\", \"ابحاث\", \"أبحاث\", \"بحث علمي\","` | — |
| [SRC-1AE03B9EC3-L002108](../../agents/web_agent.py#L2108) | 2108 | `"                \"ورقة علمية\", \"أوراق علمية\", \"academic\", \"research\","` | — |
| [SRC-1AE03B9EC3-L002109](../../agents/web_agent.py#L2109) | 2109 | `"                \"scientific study\", \"research paper\", \"peer reviewed\","` | — |
| [SRC-1AE03B9EC3-L002110](../../agents/web_agent.py#L2110) | 2110 | `"                \"peer-reviewed\", \"scholarly\", \"literature review\","` | — |
| [SRC-1AE03B9EC3-L002111](../../agents/web_agent.py#L2111) | 2111 | `"                \"systematic review\", \"arxiv\", \"openalex\", \"crossref\","` | — |
| [SRC-1AE03B9EC3-L002112](../../agents/web_agent.py#L2112) | 2112 | `"            )"` | — |
| [SRC-1AE03B9EC3-L002113](../../agents/web_agent.py#L2113) | 2113 | `"            if len(combined) < 3 and any(marker in search_query.casefold() for marker in academic_markers):"` | — |
| [SRC-1AE03B9EC3-L002114](../../agents/web_agent.py#L2114) | 2114 | `"                academic_adapters: list[tuple[str, Any]] = ["` | — |
| [SRC-1AE03B9EC3-L002115](../../agents/web_agent.py#L2115) | 2115 | `"                    (\"openalex\", lambda q: search_openalex(q, limit=3)),"` | — |
| [SRC-1AE03B9EC3-L002116](../../agents/web_agent.py#L2116) | 2116 | `"                    (\"arxiv\", lambda q: search_arxiv(q, limit=3)),"` | — |
| [SRC-1AE03B9EC3-L002117](../../agents/web_agent.py#L2117) | 2117 | `"                    (\"crossref\", lambda q: search_crossref(q, limit=3)),"` | — |
| [SRC-1AE03B9EC3-L002118](../../agents/web_agent.py#L2118) | 2118 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L002119](../../agents/web_agent.py#L2119) | 2119 | `""` | — |
| [SRC-1AE03B9EC3-L002120](../../agents/web_agent.py#L2120) | 2120 | `"                async def run_academic_all() -> list[list[dict[str, Any]]]:"` | — |
| [SRC-1AE03B9EC3-L002121](../../agents/web_agent.py#L2121) | 2121 | `"                    return await asyncio.gather("` | — |
| [SRC-1AE03B9EC3-L002122](../../agents/web_agent.py#L2122) | 2122 | `"                        *(run_one(name, method) for name, method in academic_adapters)"` | — |
| [SRC-1AE03B9EC3-L002123](../../agents/web_agent.py#L2123) | 2123 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L002124](../../agents/web_agent.py#L2124) | 2124 | `""` | — |
| [SRC-1AE03B9EC3-L002125](../../agents/web_agent.py#L2125) | 2125 | `"                provider_batches.extend(asyncio.run(run_academic_all()))"` | — |
| [SRC-1AE03B9EC3-L002126](../../agents/web_agent.py#L2126) | 2126 | `"        except RuntimeError as exc:"` | — |
| [SRC-1AE03B9EC3-L002127](../../agents/web_agent.py#L2127) | 2127 | `"            # This method is synchronous by contract; the HTTP server invokes it in worker threads."` | — |
| [SRC-1AE03B9EC3-L002128](../../agents/web_agent.py#L2128) | 2128 | `"            raise RuntimeError(\"تعذر تشغيل مجدول موصلات البحث.\") from exc"` | — |
| [SRC-1AE03B9EC3-L002129](../../agents/web_agent.py#L2129) | 2129 | `"        combined = [item for batch in provider_batches for item in batch]"` | — |
| [SRC-1AE03B9EC3-L002130](../../agents/web_agent.py#L2130) | 2130 | `"        # De-duplicate repeated URLs before ranking/fusion."` | — |
| [SRC-1AE03B9EC3-L002131](../../agents/web_agent.py#L2131) | 2131 | `"        unique: dict[str, dict[str, Any]] = {}"` | — |
| [SRC-1AE03B9EC3-L002132](../../agents/web_agent.py#L2132) | 2132 | `"        for item in combined:"` | — |
| [SRC-1AE03B9EC3-L002133](../../agents/web_agent.py#L2133) | 2133 | `"            key = item[\"url\"].split(\"#\", 1)[0].rstrip(\"/\")"` | — |
| [SRC-1AE03B9EC3-L002134](../../agents/web_agent.py#L2134) | 2134 | `"            if key not in unique or len(str(item.get(\"snippet\") or \"\")) > len(str(unique[key].get(\"snippet\") or \"\")):"` | — |
| [SRC-1AE03B9EC3-L002135](../../agents/web_agent.py#L2135) | 2135 | `"                unique[key] = item"` | — |
| [SRC-1AE03B9EC3-L002136](../../agents/web_agent.py#L2136) | 2136 | `"        if not unique:"` | — |
| [SRC-1AE03B9EC3-L002137](../../agents/web_agent.py#L2137) | 2137 | `"            raise RuntimeError(\"لم تُرجع موصلات البحث نتائج مرتبطة وقابلة للاستخدام.\")"` | — |
| [SRC-1AE03B9EC3-L002138](../../agents/web_agent.py#L2138) | 2138 | `"        return list(unique.values())"` | — |
| [SRC-1AE03B9EC3-L002139](../../agents/web_agent.py#L2139) | 2139 | `""` | — |
| [SRC-1AE03B9EC3-L002140](../../agents/web_agent.py#L2140) | 2140 | `"    def _reserve_search_call(self) -> None:"` | — |
| [SRC-1AE03B9EC3-L002141](../../agents/web_agent.py#L2141) | 2141 | `"        \"\"\"Reserve one outbound search/social-provider request before network I/O.\"\"\""` | — |
| [SRC-1AE03B9EC3-L002142](../../agents/web_agent.py#L2142) | 2142 | `"        budget = getattr(self, \"_request_budget\", None)"` | — |
| [SRC-1AE03B9EC3-L002143](../../agents/web_agent.py#L2143) | 2143 | `"        if budget is not None:"` | — |
| [SRC-1AE03B9EC3-L002144](../../agents/web_agent.py#L2144) | 2144 | `"            budget.reserve(\"search_calls\")"` | — |
| [SRC-1AE03B9EC3-L002145](../../agents/web_agent.py#L2145) | 2145 | `""` | — |
| [SRC-1AE03B9EC3-L002146](../../agents/web_agent.py#L2146) | 2146 | `"    def _search_brave(self, query: str) -> list[dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L002147](../../agents/web_agent.py#L2147) | 2147 | `"        \"\"\"Use Brave's official web-search API when the operator provides an API key.\"\"\""` | — |
| [SRC-1AE03B9EC3-L002148](../../agents/web_agent.py#L2148) | 2148 | `"        api_key = os.getenv(\"BRAVE_SEARCH_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L002149](../../agents/web_agent.py#L2149) | 2149 | `"        if not api_key:"` | — |
| [SRC-1AE03B9EC3-L002150](../../agents/web_agent.py#L2150) | 2150 | `"            return []"` | — |
| [SRC-1AE03B9EC3-L002151](../../agents/web_agent.py#L2151) | 2151 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L002152](../../agents/web_agent.py#L2152) | 2152 | `"            from importlib.util import find_spec"` | — |
| [SRC-1AE03B9EC3-L002153](../../agents/web_agent.py#L2153) | 2153 | `"            if find_spec(\"httpx\") is None:"` | — |
| [SRC-1AE03B9EC3-L002154](../../agents/web_agent.py#L2154) | 2154 | `"                raise AgentDependencyError(\"حزمة httpx غير مثبتة.\")"` | — |
| [SRC-1AE03B9EC3-L002155](../../agents/web_agent.py#L2155) | 2155 | `"        except ImportError as exc:"` | — |
| [SRC-1AE03B9EC3-L002156](../../agents/web_agent.py#L2156) | 2156 | `"            raise AgentDependencyError(\"حزمة httpx غير مثبتة.\") from exc"` | — |
| [SRC-1AE03B9EC3-L002157](../../agents/web_agent.py#L2157) | 2157 | `"        is_arabic = bool(re.search(r\"[\\u0600-\\u06FF]\", query))"` | — |
| [SRC-1AE03B9EC3-L002158](../../agents/web_agent.py#L2158) | 2158 | `"        response = _bounded_http_request(\"GET\", "` | — |
| [SRC-1AE03B9EC3-L002159](../../agents/web_agent.py#L2159) | 2159 | `"            \"https://api.search.brave.com/res/v1/web/search\","` | — |
| [SRC-1AE03B9EC3-L002160](../../agents/web_agent.py#L2160) | 2160 | `"            params={"` | — |
| [SRC-1AE03B9EC3-L002161](../../agents/web_agent.py#L2161) | 2161 | `"                \"q\": query[:600],"` | — |
| [SRC-1AE03B9EC3-L002162](../../agents/web_agent.py#L2162) | 2162 | `"                \"count\": MAX_PROVIDER_RESULTS,"` | — |
| [SRC-1AE03B9EC3-L002163](../../agents/web_agent.py#L2163) | 2163 | `"                \"country\": \"EG\" if is_arabic else \"US\","` | — |
| [SRC-1AE03B9EC3-L002164](../../agents/web_agent.py#L2164) | 2164 | `"                \"search_lang\": \"ar\" if is_arabic else \"en\","` | — |
| [SRC-1AE03B9EC3-L002165](../../agents/web_agent.py#L2165) | 2165 | `"                \"extra_snippets\": \"true\","` | — |
| [SRC-1AE03B9EC3-L002166](../../agents/web_agent.py#L2166) | 2166 | `"            },"` | — |
| [SRC-1AE03B9EC3-L002167](../../agents/web_agent.py#L2167) | 2167 | `"            headers={"` | — |
| [SRC-1AE03B9EC3-L002168](../../agents/web_agent.py#L2168) | 2168 | `"                \"Accept\": \"application/json\","` | — |
| [SRC-1AE03B9EC3-L002169](../../agents/web_agent.py#L2169) | 2169 | `"                \"X-Subscription-Token\": api_key,"` | — |
| [SRC-1AE03B9EC3-L002170](../../agents/web_agent.py#L2170) | 2170 | `"                \"User-Agent\": \"OmaraiResearchAgent/1.0\","` | — |
| [SRC-1AE03B9EC3-L002171](../../agents/web_agent.py#L2171) | 2171 | `"            },"` | — |
| [SRC-1AE03B9EC3-L002172](../../agents/web_agent.py#L2172) | 2172 | `"            timeout=self._effective_timeout(8.5),"` | — |
| [SRC-1AE03B9EC3-L002173](../../agents/web_agent.py#L2173) | 2173 | `"            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L002174](../../agents/web_agent.py#L2174) | 2174 | `"        )"` | — |
| [SRC-1AE03B9EC3-L002175](../../agents/web_agent.py#L2175) | 2175 | `"        response.raise_for_status()"` | — |
| [SRC-1AE03B9EC3-L002176](../../agents/web_agent.py#L2176) | 2176 | `"        payload = response.json()"` | — |
| [SRC-1AE03B9EC3-L002177](../../agents/web_agent.py#L2177) | 2177 | `"        web_results = payload.get(\"web\", {}).get(\"results\", [])"` | — |
| [SRC-1AE03B9EC3-L002178](../../agents/web_agent.py#L2178) | 2178 | `"        rows: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L002179](../../agents/web_agent.py#L2179) | 2179 | `"        for item in web_results if isinstance(web_results, list) else []:"` | — |
| [SRC-1AE03B9EC3-L002180](../../agents/web_agent.py#L2180) | 2180 | `"            if not isinstance(item, dict):"` | — |
| [SRC-1AE03B9EC3-L002181](../../agents/web_agent.py#L2181) | 2181 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L002182](../../agents/web_agent.py#L2182) | 2182 | `"            url = _public_http_url(item.get(\"url\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L002183](../../agents/web_agent.py#L2183) | 2183 | `"            if not url:"` | — |
| [SRC-1AE03B9EC3-L002184](../../agents/web_agent.py#L2184) | 2184 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L002185](../../agents/web_agent.py#L2185) | 2185 | `"            snippets = item.get(\"extra_snippets\", [])"` | — |
| [SRC-1AE03B9EC3-L002186](../../agents/web_agent.py#L2186) | 2186 | `"            extra = \" \".join(x for x in snippets if isinstance(x, str)) if isinstance(snippets, list) else \"\""` | — |
| [SRC-1AE03B9EC3-L002187](../../agents/web_agent.py#L2187) | 2187 | `"            rows.append({"` | — |
| [SRC-1AE03B9EC3-L002188](../../agents/web_agent.py#L2188) | 2188 | `"                \"title\": _clean_text(item.get(\"title\", \"\"), 300),"` | — |
| [SRC-1AE03B9EC3-L002189](../../agents/web_agent.py#L2189) | 2189 | `"                \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L002190](../../agents/web_agent.py#L2190) | 2190 | `"                \"snippet\": _clean_text(item.get(\"description\", \"\") + \" \" + extra, 1600),"` | — |
| [SRC-1AE03B9EC3-L002191](../../agents/web_agent.py#L2191) | 2191 | `"                \"provider\": \"brave_search_api\","` | — |
| [SRC-1AE03B9EC3-L002192](../../agents/web_agent.py#L2192) | 2192 | `"                \"provider_rank\": len(rows) + 1,"` | — |
| [SRC-1AE03B9EC3-L002193](../../agents/web_agent.py#L2193) | 2193 | `"                \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L002194](../../agents/web_agent.py#L2194) | 2194 | `"                \"published_at\": _clean_text(item.get(\"page_age\", \"\") or item.get(\"published_at\", \"\"), 100),"` | — |
| [SRC-1AE03B9EC3-L002195](../../agents/web_agent.py#L2195) | 2195 | `"            })"` | — |
| [SRC-1AE03B9EC3-L002196](../../agents/web_agent.py#L2196) | 2196 | `"            if len(rows) >= MAX_PROVIDER_RESULTS:"` | — |
| [SRC-1AE03B9EC3-L002197](../../agents/web_agent.py#L2197) | 2197 | `"                break"` | — |
| [SRC-1AE03B9EC3-L002198](../../agents/web_agent.py#L2198) | 2198 | `"        return rows"` | — |
| [SRC-1AE03B9EC3-L002199](../../agents/web_agent.py#L2199) | 2199 | `""` | — |
| [SRC-1AE03B9EC3-L002200](../../agents/web_agent.py#L2200) | 2200 | `"    def _search_tavily(self, query: str) -> list[dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L002201](../../agents/web_agent.py#L2201) | 2201 | `"        \"\"\"Use Tavily's official search API for structured, extractable live web results.\"\"\""` | — |
| [SRC-1AE03B9EC3-L002202](../../agents/web_agent.py#L2202) | 2202 | `"        api_key = os.getenv(\"TAVILY_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L002203](../../agents/web_agent.py#L2203) | 2203 | `"        if not api_key:"` | — |
| [SRC-1AE03B9EC3-L002204](../../agents/web_agent.py#L2204) | 2204 | `"            return []"` | — |
| [SRC-1AE03B9EC3-L002205](../../agents/web_agent.py#L2205) | 2205 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L002206](../../agents/web_agent.py#L2206) | 2206 | `"            from importlib.util import find_spec"` | — |
| [SRC-1AE03B9EC3-L002207](../../agents/web_agent.py#L2207) | 2207 | `"            if find_spec(\"httpx\") is None:"` | — |
| [SRC-1AE03B9EC3-L002208](../../agents/web_agent.py#L2208) | 2208 | `"                raise AgentDependencyError(\"حزمة httpx غير مثبتة.\")"` | — |
| [SRC-1AE03B9EC3-L002209](../../agents/web_agent.py#L2209) | 2209 | `"        except ImportError as exc:"` | — |
| [SRC-1AE03B9EC3-L002210](../../agents/web_agent.py#L2210) | 2210 | `"            raise AgentDependencyError(\"حزمة httpx غير مثبتة.\") from exc"` | — |
| [SRC-1AE03B9EC3-L002211](../../agents/web_agent.py#L2211) | 2211 | `"        from agents.research import detect_depth, detect_freshness"` | — |
| [SRC-1AE03B9EC3-L002212](../../agents/web_agent.py#L2212) | 2212 | `""` | — |
| [SRC-1AE03B9EC3-L002213](../../agents/web_agent.py#L2213) | 2213 | `"        response = _bounded_http_request(\"POST\", "` | — |
| [SRC-1AE03B9EC3-L002214](../../agents/web_agent.py#L2214) | 2214 | `"            \"https://api.tavily.com/search\","` | — |
| [SRC-1AE03B9EC3-L002215](../../agents/web_agent.py#L2215) | 2215 | `"            json={"` | — |
| [SRC-1AE03B9EC3-L002216](../../agents/web_agent.py#L2216) | 2216 | `"                \"api_key\": api_key,"` | — |
| [SRC-1AE03B9EC3-L002217](../../agents/web_agent.py#L2217) | 2217 | `"                \"query\": query[:500],"` | — |
| [SRC-1AE03B9EC3-L002218](../../agents/web_agent.py#L2218) | 2218 | `"                \"search_depth\": \"advanced\" if detect_depth(query) == \"deep\" else \"basic\","` | — |
| [SRC-1AE03B9EC3-L002219](../../agents/web_agent.py#L2219) | 2219 | `"                \"topic\": \"news\" if detect_freshness(query) else \"general\","` | — |
| [SRC-1AE03B9EC3-L002220](../../agents/web_agent.py#L2220) | 2220 | `"                \"max_results\": MAX_PROVIDER_RESULTS,"` | — |
| [SRC-1AE03B9EC3-L002221](../../agents/web_agent.py#L2221) | 2221 | `"                \"include_answer\": False,"` | — |
| [SRC-1AE03B9EC3-L002222](../../agents/web_agent.py#L2222) | 2222 | `"                \"include_raw_content\": False,"` | — |
| [SRC-1AE03B9EC3-L002223](../../agents/web_agent.py#L2223) | 2223 | `"            },"` | — |
| [SRC-1AE03B9EC3-L002224](../../agents/web_agent.py#L2224) | 2224 | `"            headers={"` | — |
| [SRC-1AE03B9EC3-L002225](../../agents/web_agent.py#L2225) | 2225 | `"                \"Accept\": \"application/json\","` | — |
| [SRC-1AE03B9EC3-L002226](../../agents/web_agent.py#L2226) | 2226 | `"                \"Content-Type\": \"application/json\","` | — |
| [SRC-1AE03B9EC3-L002227](../../agents/web_agent.py#L2227) | 2227 | `"                \"User-Agent\": \"OmaraiResearchAgent/1.0\","` | — |
| [SRC-1AE03B9EC3-L002228](../../agents/web_agent.py#L2228) | 2228 | `"            },"` | — |
| [SRC-1AE03B9EC3-L002229](../../agents/web_agent.py#L2229) | 2229 | `"            timeout=self._effective_timeout(8.5),"` | — |
| [SRC-1AE03B9EC3-L002230](../../agents/web_agent.py#L2230) | 2230 | `"            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L002231](../../agents/web_agent.py#L2231) | 2231 | `"        )"` | — |
| [SRC-1AE03B9EC3-L002232](../../agents/web_agent.py#L2232) | 2232 | `"        response.raise_for_status()"` | — |
| [SRC-1AE03B9EC3-L002233](../../agents/web_agent.py#L2233) | 2233 | `"        payload = response.json()"` | — |
| [SRC-1AE03B9EC3-L002234](../../agents/web_agent.py#L2234) | 2234 | `"        search_results = payload.get(\"results\", [])"` | — |
| [SRC-1AE03B9EC3-L002235](../../agents/web_agent.py#L2235) | 2235 | `"        rows: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L002236](../../agents/web_agent.py#L2236) | 2236 | `"        for item in search_results if isinstance(search_results, list) else []:"` | — |
| [SRC-1AE03B9EC3-L002237](../../agents/web_agent.py#L2237) | 2237 | `"            if not isinstance(item, dict):"` | — |
| [SRC-1AE03B9EC3-L002238](../../agents/web_agent.py#L2238) | 2238 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L002239](../../agents/web_agent.py#L2239) | 2239 | `"            url = _public_http_url(item.get(\"url\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L002240](../../agents/web_agent.py#L2240) | 2240 | `"            if not url:"` | — |
| [SRC-1AE03B9EC3-L002241](../../agents/web_agent.py#L2241) | 2241 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L002242](../../agents/web_agent.py#L2242) | 2242 | `"            rows.append({"` | — |
| [SRC-1AE03B9EC3-L002243](../../agents/web_agent.py#L2243) | 2243 | `"                \"title\": _clean_text(item.get(\"title\", \"\"), 300),"` | — |
| [SRC-1AE03B9EC3-L002244](../../agents/web_agent.py#L2244) | 2244 | `"                \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L002245](../../agents/web_agent.py#L2245) | 2245 | `"                \"snippet\": _clean_text(item.get(\"content\", \"\"), 1600),"` | — |
| [SRC-1AE03B9EC3-L002246](../../agents/web_agent.py#L2246) | 2246 | `"                \"provider\": \"tavily_search_api\","` | — |
| [SRC-1AE03B9EC3-L002247](../../agents/web_agent.py#L2247) | 2247 | `"                \"provider_rank\": len(rows) + 1,"` | — |
| [SRC-1AE03B9EC3-L002248](../../agents/web_agent.py#L2248) | 2248 | `"                \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L002249](../../agents/web_agent.py#L2249) | 2249 | `"                \"published_at\": _clean_text(item.get(\"published_date\", \"\"), 100),"` | — |
| [SRC-1AE03B9EC3-L002250](../../agents/web_agent.py#L2250) | 2250 | `"            })"` | — |
| [SRC-1AE03B9EC3-L002251](../../agents/web_agent.py#L2251) | 2251 | `"            if len(rows) >= MAX_PROVIDER_RESULTS:"` | — |
| [SRC-1AE03B9EC3-L002252](../../agents/web_agent.py#L2252) | 2252 | `"                break"` | — |
| [SRC-1AE03B9EC3-L002253](../../agents/web_agent.py#L2253) | 2253 | `"        return rows"` | — |
| [SRC-1AE03B9EC3-L002254](../../agents/web_agent.py#L2254) | 2254 | `""` | — |
| [SRC-1AE03B9EC3-L002255](../../agents/web_agent.py#L2255) | 2255 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L002256](../../agents/web_agent.py#L2256) | 2256 | `"    def _firecrawl_search_country(query: str) -> str \| None:"` | — |
| [SRC-1AE03B9EC3-L002257](../../agents/web_agent.py#L2257) | 2257 | `"        \"\"\"Return a country code only when the query explicitly names geography.\"\"\""` | — |
| [SRC-1AE03B9EC3-L002258](../../agents/web_agent.py#L2258) | 2258 | `"        normalized = _normalize_search_query(query).casefold()"` | — |
| [SRC-1AE03B9EC3-L002259](../../agents/web_agent.py#L2259) | 2259 | `"        rules = ("` | — |
| [SRC-1AE03B9EC3-L002260](../../agents/web_agent.py#L2260) | 2260 | `"            (\"SA\", r\"(?<!\\w)(?:saudi arabia\|ksa\|riyadh\|jeddah)(?!\\w)\|السعودي(?:ة\|ه)\"),"` | — |
| [SRC-1AE03B9EC3-L002261](../../agents/web_agent.py#L2261) | 2261 | `"            (\"AE\", r\"(?<!\\w)(?:uae\|united arab emirates\|dubai\|abu dhabi)(?!\\w)\|الامارات\"),"` | — |
| [SRC-1AE03B9EC3-L002262](../../agents/web_agent.py#L2262) | 2262 | `"            (\"UK\", r\"(?<!\\w)(?:united kingdom\|great britain\|uk\|london)(?!\\w)\|المملكه المتحده\|بريطانيا\"),"` | — |
| [SRC-1AE03B9EC3-L002263](../../agents/web_agent.py#L2263) | 2263 | `"            (\"EG\", r\"(?<!\\w)(?:egypt\|egyptian\|cairo\|alexandria\|giza)(?!\\w)\|مصر\|القاهره\|الاسكندريه\|الجيزه\"),"` | — |
| [SRC-1AE03B9EC3-L002264](../../agents/web_agent.py#L2264) | 2264 | `"            (\"US\", r\"(?<!\\w)(?:united states\|usa\|u\\.s\\.a\\.\|america\|new york\|los angeles)(?!\\w)\|الولايات المتحده\|امريكا\"),"` | — |
| [SRC-1AE03B9EC3-L002265](../../agents/web_agent.py#L2265) | 2265 | `"        )"` | — |
| [SRC-1AE03B9EC3-L002266](../../agents/web_agent.py#L2266) | 2266 | `"        for country, pattern in rules:"` | — |
| [SRC-1AE03B9EC3-L002267](../../agents/web_agent.py#L2267) | 2267 | `"            if re.search(pattern, normalized, flags=re.IGNORECASE):"` | — |
| [SRC-1AE03B9EC3-L002268](../../agents/web_agent.py#L2268) | 2268 | `"                return country"` | — |
| [SRC-1AE03B9EC3-L002269](../../agents/web_agent.py#L2269) | 2269 | `"        # Language is not geography. Leave country unset when the user did not name one."` | — |
| [SRC-1AE03B9EC3-L002270](../../agents/web_agent.py#L2270) | 2270 | `""` | — |
| [SRC-1AE03B9EC3-L002271](../../agents/web_agent.py#L2271) | 2271 | `"    def _search_firecrawl(self, query: str) -> list[dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L002272](../../agents/web_agent.py#L2272) | 2272 | `"        \"\"\"Use Firecrawl v2 web search; caller enforces explicit enablement and budget.\"\"\""` | — |
| [SRC-1AE03B9EC3-L002273](../../agents/web_agent.py#L2273) | 2273 | `"        api_key = os.getenv(\"FIRECRAWL_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L002274](../../agents/web_agent.py#L2274) | 2274 | `"        if ("` | — |
| [SRC-1AE03B9EC3-L002275](../../agents/web_agent.py#L2275) | 2275 | `"            os.getenv(\"FIRECRAWL_SEARCH_ENABLED\", \"\").strip() != \"1\""` | — |
| [SRC-1AE03B9EC3-L002276](../../agents/web_agent.py#L2276) | 2276 | `"            or not api_key"` | — |
| [SRC-1AE03B9EC3-L002277](../../agents/web_agent.py#L2277) | 2277 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L002278](../../agents/web_agent.py#L2278) | 2278 | `"            return []"` | — |
| [SRC-1AE03B9EC3-L002279](../../agents/web_agent.py#L2279) | 2279 | `"        request_payload: dict[str, Any] = {"` | — |
| [SRC-1AE03B9EC3-L002280](../../agents/web_agent.py#L2280) | 2280 | `"            \"query\": query[:500],"` | — |
| [SRC-1AE03B9EC3-L002281](../../agents/web_agent.py#L2281) | 2281 | `"            \"sources\": [\"web\"],"` | — |
| [SRC-1AE03B9EC3-L002282](../../agents/web_agent.py#L2282) | 2282 | `"            \"limit\": MAX_PROVIDER_RESULTS,"` | — |
| [SRC-1AE03B9EC3-L002283](../../agents/web_agent.py#L2283) | 2283 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002284](../../agents/web_agent.py#L2284) | 2284 | `"        country = self._firecrawl_search_country(query)"` | — |
| [SRC-1AE03B9EC3-L002285](../../agents/web_agent.py#L2285) | 2285 | `"        # Omission is not neutral: Firecrawl's API defaults the country to US."` | — |
| [SRC-1AE03B9EC3-L002286](../../agents/web_agent.py#L2286) | 2286 | `"        # Guard direct calls as well as the adapter-registration path."` | — |
| [SRC-1AE03B9EC3-L002287](../../agents/web_agent.py#L2287) | 2287 | `"        if country is None:"` | — |
| [SRC-1AE03B9EC3-L002288](../../agents/web_agent.py#L2288) | 2288 | `"            return []"` | — |
| [SRC-1AE03B9EC3-L002289](../../agents/web_agent.py#L2289) | 2289 | `"        request_payload[\"country\"] = country"` | — |
| [SRC-1AE03B9EC3-L002290](../../agents/web_agent.py#L2290) | 2290 | `"        response = _bounded_http_request("` | — |
| [SRC-1AE03B9EC3-L002291](../../agents/web_agent.py#L2291) | 2291 | `"            \"POST\","` | — |
| [SRC-1AE03B9EC3-L002292](../../agents/web_agent.py#L2292) | 2292 | `"            \"https://api.firecrawl.dev/v2/search\","` | — |
| [SRC-1AE03B9EC3-L002293](../../agents/web_agent.py#L2293) | 2293 | `"            json=request_payload,"` | — |
| [SRC-1AE03B9EC3-L002294](../../agents/web_agent.py#L2294) | 2294 | `"            headers={"` | — |
| [SRC-1AE03B9EC3-L002295](../../agents/web_agent.py#L2295) | 2295 | `"                \"Accept\": \"application/json\","` | — |
| [SRC-1AE03B9EC3-L002296](../../agents/web_agent.py#L2296) | 2296 | `"                \"Content-Type\": \"application/json\","` | — |
| [SRC-1AE03B9EC3-L002297](../../agents/web_agent.py#L2297) | 2297 | `"                \"Authorization\": \"Bearer \" + api_key,"` | — |
| [SRC-1AE03B9EC3-L002298](../../agents/web_agent.py#L2298) | 2298 | `"                \"User-Agent\": \"OmaraiResearchAgent/1.0\","` | — |
| [SRC-1AE03B9EC3-L002299](../../agents/web_agent.py#L2299) | 2299 | `"            },"` | — |
| [SRC-1AE03B9EC3-L002300](../../agents/web_agent.py#L2300) | 2300 | `"            timeout=self._effective_timeout(8.5),"` | — |
| [SRC-1AE03B9EC3-L002301](../../agents/web_agent.py#L2301) | 2301 | `"            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L002302](../../agents/web_agent.py#L2302) | 2302 | `"        )"` | — |
| [SRC-1AE03B9EC3-L002303](../../agents/web_agent.py#L2303) | 2303 | `"        response.raise_for_status()"` | — |
| [SRC-1AE03B9EC3-L002304](../../agents/web_agent.py#L2304) | 2304 | `"        payload = response.json()"` | — |
| [SRC-1AE03B9EC3-L002305](../../agents/web_agent.py#L2305) | 2305 | `"        if not isinstance(payload, dict) or payload.get(\"success\") is False:"` | — |
| [SRC-1AE03B9EC3-L002306](../../agents/web_agent.py#L2306) | 2306 | `"            raise RuntimeError(\"Firecrawl search returned an unsuccessful response\")"` | — |
| [SRC-1AE03B9EC3-L002307](../../agents/web_agent.py#L2307) | 2307 | `"        data = payload.get(\"data\", {})"` | — |
| [SRC-1AE03B9EC3-L002308](../../agents/web_agent.py#L2308) | 2308 | `"        web_results = data.get(\"web\", []) if isinstance(data, dict) else data"` | — |
| [SRC-1AE03B9EC3-L002309](../../agents/web_agent.py#L2309) | 2309 | `"        rows: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L002310](../../agents/web_agent.py#L2310) | 2310 | `"        for item in web_results if isinstance(web_results, list) else []:"` | — |
| [SRC-1AE03B9EC3-L002311](../../agents/web_agent.py#L2311) | 2311 | `"            if not isinstance(item, dict):"` | — |
| [SRC-1AE03B9EC3-L002312](../../agents/web_agent.py#L2312) | 2312 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L002313](../../agents/web_agent.py#L2313) | 2313 | `"            url = _public_http_url(item.get(\"url\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L002314](../../agents/web_agent.py#L2314) | 2314 | `"            title = _clean_text(item.get(\"title\", \"\"), 300)"` | — |
| [SRC-1AE03B9EC3-L002315](../../agents/web_agent.py#L2315) | 2315 | `"            description = _clean_text("` | — |
| [SRC-1AE03B9EC3-L002316](../../agents/web_agent.py#L2316) | 2316 | `"                item.get(\"description\", \"\") or item.get(\"snippet\", \"\"), 1600"` | — |
| [SRC-1AE03B9EC3-L002317](../../agents/web_agent.py#L2317) | 2317 | `"            )"` | — |
| [SRC-1AE03B9EC3-L002318](../../agents/web_agent.py#L2318) | 2318 | `"            if not url or not title or not description:"` | — |
| [SRC-1AE03B9EC3-L002319](../../agents/web_agent.py#L2319) | 2319 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L002320](../../agents/web_agent.py#L2320) | 2320 | `"            rows.append({"` | — |
| [SRC-1AE03B9EC3-L002321](../../agents/web_agent.py#L2321) | 2321 | `"                \"title\": title,"` | — |
| [SRC-1AE03B9EC3-L002322](../../agents/web_agent.py#L2322) | 2322 | `"                \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L002323](../../agents/web_agent.py#L2323) | 2323 | `"                \"snippet\": description,"` | — |
| [SRC-1AE03B9EC3-L002324](../../agents/web_agent.py#L2324) | 2324 | `"                \"provider\": \"firecrawl_search_api\","` | — |
| [SRC-1AE03B9EC3-L002325](../../agents/web_agent.py#L2325) | 2325 | `"                \"provider_rank\": len(rows) + 1,"` | — |
| [SRC-1AE03B9EC3-L002326](../../agents/web_agent.py#L2326) | 2326 | `"                \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L002327](../../agents/web_agent.py#L2327) | 2327 | `"                \"published_at\": _clean_text("` | — |
| [SRC-1AE03B9EC3-L002328](../../agents/web_agent.py#L2328) | 2328 | `"                    item.get(\"publishedAt\", \"\") or item.get(\"published_at\", \"\"), 100"` | — |
| [SRC-1AE03B9EC3-L002329](../../agents/web_agent.py#L2329) | 2329 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L002330](../../agents/web_agent.py#L2330) | 2330 | `"            })"` | — |
| [SRC-1AE03B9EC3-L002331](../../agents/web_agent.py#L2331) | 2331 | `"            if len(rows) >= MAX_PROVIDER_RESULTS:"` | — |
| [SRC-1AE03B9EC3-L002332](../../agents/web_agent.py#L2332) | 2332 | `"                break"` | — |
| [SRC-1AE03B9EC3-L002333](../../agents/web_agent.py#L2333) | 2333 | `"        return rows"` | — |
| [SRC-1AE03B9EC3-L002334](../../agents/web_agent.py#L2334) | 2334 | `""` | — |
| [SRC-1AE03B9EC3-L002335](../../agents/web_agent.py#L2335) | 2335 | `"    def _search_news(self, query: str) -> list[dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L002336](../../agents/web_agent.py#L2336) | 2336 | `"        \"\"\"Read the public Google News RSS search feed for freshness-sensitive queries.\"\"\""` | — |
| [SRC-1AE03B9EC3-L002337](../../agents/web_agent.py#L2337) | 2337 | `"        import xml.etree.ElementTree as ET"` | — |
| [SRC-1AE03B9EC3-L002338](../../agents/web_agent.py#L2338) | 2338 | `""` | — |
| [SRC-1AE03B9EC3-L002339](../../agents/web_agent.py#L2339) | 2339 | `"        response = _bounded_http_request(\"GET\", "` | — |
| [SRC-1AE03B9EC3-L002340](../../agents/web_agent.py#L2340) | 2340 | `"            \"https://news.google.com/rss/search\","` | — |
| [SRC-1AE03B9EC3-L002341](../../agents/web_agent.py#L2341) | 2341 | `"            params={\"q\": query, \"hl\": \"ar\", \"gl\": \"EG\", \"ceid\": \"EG:ar\"},"` | — |
| [SRC-1AE03B9EC3-L002342](../../agents/web_agent.py#L2342) | 2342 | `"            headers={"` | — |
| [SRC-1AE03B9EC3-L002343](../../agents/web_agent.py#L2343) | 2343 | `"                \"User-Agent\": \"OmaraiResearchBot/1.2\","` | — |
| [SRC-1AE03B9EC3-L002344](../../agents/web_agent.py#L2344) | 2344 | `"                \"Accept-Language\": \"ar,en;q=0.9\","` | — |
| [SRC-1AE03B9EC3-L002345](../../agents/web_agent.py#L2345) | 2345 | `"            },"` | — |
| [SRC-1AE03B9EC3-L002346](../../agents/web_agent.py#L2346) | 2346 | `"            timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L002347](../../agents/web_agent.py#L2347) | 2347 | `"            # Refuse automatic redirects from public search endpoints; never fetch an"` | — |
| [SRC-1AE03B9EC3-L002348](../../agents/web_agent.py#L2348) | 2348 | `"            # unchecked redirect target as part of a provider search request."` | — |
| [SRC-1AE03B9EC3-L002349](../../agents/web_agent.py#L2349) | 2349 | `"            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L002350](../../agents/web_agent.py#L2350) | 2350 | `"        )"` | — |
| [SRC-1AE03B9EC3-L002351](../../agents/web_agent.py#L2351) | 2351 | `"        if response.status_code != 200:"` | — |
| [SRC-1AE03B9EC3-L002352](../../agents/web_agent.py#L2352) | 2352 | `"            raise RuntimeError(f\"HTTP {response.status_code}\")"` | — |
| [SRC-1AE03B9EC3-L002353](../../agents/web_agent.py#L2353) | 2353 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L002354](../../agents/web_agent.py#L2354) | 2354 | `"            root = ET.fromstring(response.content)"` | — |
| [SRC-1AE03B9EC3-L002355](../../agents/web_agent.py#L2355) | 2355 | `"        except ET.ParseError as exc:"` | — |
| [SRC-1AE03B9EC3-L002356](../../agents/web_agent.py#L2356) | 2356 | `"            raise RuntimeError(\"invalid RSS XML\") from exc"` | — |
| [SRC-1AE03B9EC3-L002357](../../agents/web_agent.py#L2357) | 2357 | `"        results: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L002358](../../agents/web_agent.py#L2358) | 2358 | `"        for item in root.iter():"` | — |
| [SRC-1AE03B9EC3-L002359](../../agents/web_agent.py#L2359) | 2359 | `"            if item.tag.rsplit(\"}\", 1)[-1] != \"item\":"` | — |
| [SRC-1AE03B9EC3-L002360](../../agents/web_agent.py#L2360) | 2360 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L002361](../../agents/web_agent.py#L2361) | 2361 | `"            fields = {"` | — |
| [SRC-1AE03B9EC3-L002362](../../agents/web_agent.py#L2362) | 2362 | `"                child.tag.rsplit(\"}\", 1)[-1]: (child.text or \"\")"` | — |
| [SRC-1AE03B9EC3-L002363](../../agents/web_agent.py#L2363) | 2363 | `"                for child in item"` | — |
| [SRC-1AE03B9EC3-L002364](../../agents/web_agent.py#L2364) | 2364 | `"            }"` | — |
| [SRC-1AE03B9EC3-L002365](../../agents/web_agent.py#L2365) | 2365 | `"            url = _public_http_url(fields.get(\"link\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L002366](../../agents/web_agent.py#L2366) | 2366 | `"            if not url or _blocked_source_url(url):"` | — |
| [SRC-1AE03B9EC3-L002367](../../agents/web_agent.py#L2367) | 2367 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L002368](../../agents/web_agent.py#L2368) | 2368 | `"            # Keep every parseable, safe candidate here. _search_web applies the"` | — |
| [SRC-1AE03B9EC3-L002369](../../agents/web_agent.py#L2369) | 2369 | `"            # shared relevance filter and records accepted/rejected counters."` | — |
| [SRC-1AE03B9EC3-L002370](../../agents/web_agent.py#L2370) | 2370 | `"            # Filtering again in this adapter mislabels a valid feed as no results."` | — |
| [SRC-1AE03B9EC3-L002371](../../agents/web_agent.py#L2371) | 2371 | `"            source_node = next("` | — |
| [SRC-1AE03B9EC3-L002372](../../agents/web_agent.py#L2372) | 2372 | `"                (child for child in item if child.tag.rsplit(\"}\", 1)[-1] == \"source\"),"` | — |
| [SRC-1AE03B9EC3-L002373](../../agents/web_agent.py#L2373) | 2373 | `"                None,"` | — |
| [SRC-1AE03B9EC3-L002374](../../agents/web_agent.py#L2374) | 2374 | `"            )"` | — |
| [SRC-1AE03B9EC3-L002375](../../agents/web_agent.py#L2375) | 2375 | `"            publisher_url = _public_http_url("` | — |
| [SRC-1AE03B9EC3-L002376](../../agents/web_agent.py#L2376) | 2376 | `"                source_node.attrib.get(\"url\", \"\") if source_node is not None else \"\""` | — |
| [SRC-1AE03B9EC3-L002377](../../agents/web_agent.py#L2377) | 2377 | `"            )"` | — |
| [SRC-1AE03B9EC3-L002378](../../agents/web_agent.py#L2378) | 2378 | `"            publisher_name = _clean_text("` | — |
| [SRC-1AE03B9EC3-L002379](../../agents/web_agent.py#L2379) | 2379 | `"                source_node.text if source_node is not None else \"\", 200"` | — |
| [SRC-1AE03B9EC3-L002380](../../agents/web_agent.py#L2380) | 2380 | `"            )"` | — |
| [SRC-1AE03B9EC3-L002381](../../agents/web_agent.py#L2381) | 2381 | `"            publisher_domain = ("` | — |
| [SRC-1AE03B9EC3-L002382](../../agents/web_agent.py#L2382) | 2382 | `"                (urllib.parse.urlparse(publisher_url).hostname or \"\").lower()"` | — |
| [SRC-1AE03B9EC3-L002383](../../agents/web_agent.py#L2383) | 2383 | `"                if publisher_url else \"\""` | — |
| [SRC-1AE03B9EC3-L002384](../../agents/web_agent.py#L2384) | 2384 | `"            )"` | — |
| [SRC-1AE03B9EC3-L002385](../../agents/web_agent.py#L2385) | 2385 | `"            results.append({"` | — |
| [SRC-1AE03B9EC3-L002386](../../agents/web_agent.py#L2386) | 2386 | `"                \"title\": _clean_text(fields.get(\"title\", \"\"), 300),"` | — |
| [SRC-1AE03B9EC3-L002387](../../agents/web_agent.py#L2387) | 2387 | `"                \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L002388](../../agents/web_agent.py#L2388) | 2388 | `"                \"snippet\": _clean_text(fields.get(\"description\", \"\"), 1200),"` | — |
| [SRC-1AE03B9EC3-L002389](../../agents/web_agent.py#L2389) | 2389 | `"                \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L002390](../../agents/web_agent.py#L2390) | 2390 | `"                \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L002391](../../agents/web_agent.py#L2391) | 2391 | `"                \"provider\": \"google_news_rss\","` | — |
| [SRC-1AE03B9EC3-L002392](../../agents/web_agent.py#L2392) | 2392 | `"                \"provider_rank\": len(results) + 1,"` | — |
| [SRC-1AE03B9EC3-L002393](../../agents/web_agent.py#L2393) | 2393 | `"                \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L002394](../../agents/web_agent.py#L2394) | 2394 | `"                \"published_at\": _clean_text(fields.get(\"pubDate\", \"\"), 100),"` | — |
| [SRC-1AE03B9EC3-L002395](../../agents/web_agent.py#L2395) | 2395 | `"                \"publisher_name\": publisher_name,"` | — |
| [SRC-1AE03B9EC3-L002396](../../agents/web_agent.py#L2396) | 2396 | `"                \"publisher_url\": publisher_url or \"\","` | — |
| [SRC-1AE03B9EC3-L002397](../../agents/web_agent.py#L2397) | 2397 | `"                \"publisher_domain\": publisher_domain,"` | — |
| [SRC-1AE03B9EC3-L002398](../../agents/web_agent.py#L2398) | 2398 | `"            })"` | — |
| [SRC-1AE03B9EC3-L002399](../../agents/web_agent.py#L2399) | 2399 | `"            if len(results) >= MAX_PROVIDER_RESULTS:"` | — |
| [SRC-1AE03B9EC3-L002400](../../agents/web_agent.py#L2400) | 2400 | `"                break"` | — |
| [SRC-1AE03B9EC3-L002401](../../agents/web_agent.py#L2401) | 2401 | `"        return results"` | — |
| [SRC-1AE03B9EC3-L002402](../../agents/web_agent.py#L2402) | 2402 | `""` | — |
| [SRC-1AE03B9EC3-L002403](../../agents/web_agent.py#L2403) | 2403 | `"    def _search_social("` | — |
| [SRC-1AE03B9EC3-L002404](../../agents/web_agent.py#L2404) | 2404 | `"        self, query: str, platforms: list[str]"` | — |
| [SRC-1AE03B9EC3-L002405](../../agents/web_agent.py#L2405) | 2405 | `"    ) -> tuple[list[dict[str, Any]], list[str]]:"` | — |
| [SRC-1AE03B9EC3-L002406](../../agents/web_agent.py#L2406) | 2406 | `"        \"\"\"Search public social content through exposed public endpoints only.\"\"\""` | — |
| [SRC-1AE03B9EC3-L002407](../../agents/web_agent.py#L2407) | 2407 | `"        query = compact_search_query(query)"` | — |
| [SRC-1AE03B9EC3-L002408](../../agents/web_agent.py#L2408) | 2408 | `"        if not query:"` | — |
| [SRC-1AE03B9EC3-L002409](../../agents/web_agent.py#L2409) | 2409 | `"            return [], [\"لم يبدأ البحث الاجتماعي لعدم وجود كلمات موضوعية قابلة للبحث.\"]"` | — |
| [SRC-1AE03B9EC3-L002410](../../agents/web_agent.py#L2410) | 2410 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L002411](../../agents/web_agent.py#L2411) | 2411 | `"            import xml.etree.ElementTree as ET"` | — |
| [SRC-1AE03B9EC3-L002412](../../agents/web_agent.py#L2412) | 2412 | `""` | — |
| [SRC-1AE03B9EC3-L002413](../../agents/web_agent.py#L2413) | 2413 | `"            import httpx"` | — |
| [SRC-1AE03B9EC3-L002414](../../agents/web_agent.py#L2414) | 2414 | `"            from bs4 import BeautifulSoup"` | — |
| [SRC-1AE03B9EC3-L002415](../../agents/web_agent.py#L2415) | 2415 | `"        except ImportError as exc:"` | — |
| [SRC-1AE03B9EC3-L002416](../../agents/web_agent.py#L2416) | 2416 | `"            raise AgentDependencyError("` | — |
| [SRC-1AE03B9EC3-L002417](../../agents/web_agent.py#L2417) | 2417 | `"                \"حزم البحث الاجتماعي غير مثبتة. نفّذ: python -m pip install -e .\""` | — |
| [SRC-1AE03B9EC3-L002418](../../agents/web_agent.py#L2418) | 2418 | `"            ) from exc"` | — |
| [SRC-1AE03B9EC3-L002419](../../agents/web_agent.py#L2419) | 2419 | `""` | — |
| [SRC-1AE03B9EC3-L002420](../../agents/web_agent.py#L2420) | 2420 | `"        results: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L002421](../../agents/web_agent.py#L2421) | 2421 | `"        warnings: list[str] = []"` | — |
| [SRC-1AE03B9EC3-L002422](../../agents/web_agent.py#L2422) | 2422 | `"        headers = {"` | — |
| [SRC-1AE03B9EC3-L002423](../../agents/web_agent.py#L2423) | 2423 | `"            \"User-Agent\": \"OmaraiResearchBot/1.0 (public-content search; no login)\","` | — |
| [SRC-1AE03B9EC3-L002424](../../agents/web_agent.py#L2424) | 2424 | `"            \"Accept-Language\": \"ar,en;q=0.9\","` | — |
| [SRC-1AE03B9EC3-L002425](../../agents/web_agent.py#L2425) | 2425 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002426](../../agents/web_agent.py#L2426) | 2426 | `""` | — |
| [SRC-1AE03B9EC3-L002427](../../agents/web_agent.py#L2427) | 2427 | `"        optional_providers_enabled = getattr(self, \"allow_optional_providers\", True)"` | — |
| [SRC-1AE03B9EC3-L002428](../../agents/web_agent.py#L2428) | 2428 | `"        reddit_client_id = ("` | — |
| [SRC-1AE03B9EC3-L002429](../../agents/web_agent.py#L2429) | 2429 | `"            os.getenv(\"REDDIT_CLIENT_ID\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L002430](../../agents/web_agent.py#L2430) | 2430 | `"            if optional_providers_enabled else \"\""` | — |
| [SRC-1AE03B9EC3-L002431](../../agents/web_agent.py#L2431) | 2431 | `"        )"` | — |
| [SRC-1AE03B9EC3-L002432](../../agents/web_agent.py#L2432) | 2432 | `"        reddit_client_secret = ("` | — |
| [SRC-1AE03B9EC3-L002433](../../agents/web_agent.py#L2433) | 2433 | `"            os.getenv(\"REDDIT_CLIENT_SECRET\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L002434](../../agents/web_agent.py#L2434) | 2434 | `"            if optional_providers_enabled else \"\""` | — |
| [SRC-1AE03B9EC3-L002435](../../agents/web_agent.py#L2435) | 2435 | `"        )"` | — |
| [SRC-1AE03B9EC3-L002436](../../agents/web_agent.py#L2436) | 2436 | `"        reddit_user_agent = os.getenv("` | — |
| [SRC-1AE03B9EC3-L002437](../../agents/web_agent.py#L2437) | 2437 | `"            \"REDDIT_USER_AGENT\","` | — |
| [SRC-1AE03B9EC3-L002438](../../agents/web_agent.py#L2438) | 2438 | `"            \"web:omarai-research-agent:v0.3 (public-content research)\","` | — |
| [SRC-1AE03B9EC3-L002439](../../agents/web_agent.py#L2439) | 2439 | `"        ).strip()"` | — |
| [SRC-1AE03B9EC3-L002440](../../agents/web_agent.py#L2440) | 2440 | `"        if \"reddit\" in platforms and reddit_client_id and reddit_client_secret:"` | — |
| [SRC-1AE03B9EC3-L002441](../../agents/web_agent.py#L2441) | 2441 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L002442](../../agents/web_agent.py#L2442) | 2442 | `"                self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L002443](../../agents/web_agent.py#L2443) | 2443 | `"                token_response = _bounded_http_request(\"POST\", "` | — |
| [SRC-1AE03B9EC3-L002444](../../agents/web_agent.py#L2444) | 2444 | `"                    \"https://www.reddit.com/api/v1/access_token\","` | — |
| [SRC-1AE03B9EC3-L002445](../../agents/web_agent.py#L2445) | 2445 | `"                    data={\"grant_type\": \"client_credentials\"},"` | — |
| [SRC-1AE03B9EC3-L002446](../../agents/web_agent.py#L2446) | 2446 | `"                    auth=(reddit_client_id, reddit_client_secret),"` | — |
| [SRC-1AE03B9EC3-L002447](../../agents/web_agent.py#L2447) | 2447 | `"                    headers={\"User-Agent\": reddit_user_agent},"` | — |
| [SRC-1AE03B9EC3-L002448](../../agents/web_agent.py#L2448) | 2448 | `"                    timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L002449](../../agents/web_agent.py#L2449) | 2449 | `"                    follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L002450](../../agents/web_agent.py#L2450) | 2450 | `"                )"` | — |
| [SRC-1AE03B9EC3-L002451](../../agents/web_agent.py#L2451) | 2451 | `"                if token_response.status_code == 200:"` | — |
| [SRC-1AE03B9EC3-L002452](../../agents/web_agent.py#L2452) | 2452 | `"                    access_token = token_response.json().get(\"access_token\", \"\")"` | — |
| [SRC-1AE03B9EC3-L002453](../../agents/web_agent.py#L2453) | 2453 | `"                    if access_token:"` | — |
| [SRC-1AE03B9EC3-L002454](../../agents/web_agent.py#L2454) | 2454 | `"                        self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L002455](../../agents/web_agent.py#L2455) | 2455 | `"                        search_response = _bounded_http_request(\"GET\", "` | — |
| [SRC-1AE03B9EC3-L002456](../../agents/web_agent.py#L2456) | 2456 | `"                            \"https://oauth.reddit.com/search\","` | — |
| [SRC-1AE03B9EC3-L002457](../../agents/web_agent.py#L2457) | 2457 | `"                            params={"` | — |
| [SRC-1AE03B9EC3-L002458](../../agents/web_agent.py#L2458) | 2458 | `"                                \"q\": query,"` | — |
| [SRC-1AE03B9EC3-L002459](../../agents/web_agent.py#L2459) | 2459 | `"                                \"sort\": \"relevance\","` | — |
| [SRC-1AE03B9EC3-L002460](../../agents/web_agent.py#L2460) | 2460 | `"                                \"t\": \"all\","` | — |
| [SRC-1AE03B9EC3-L002461](../../agents/web_agent.py#L2461) | 2461 | `"                                \"limit\": 10,"` | — |
| [SRC-1AE03B9EC3-L002462](../../agents/web_agent.py#L2462) | 2462 | `"                                \"type\": \"link\","` | — |
| [SRC-1AE03B9EC3-L002463](../../agents/web_agent.py#L2463) | 2463 | `"                            },"` | — |
| [SRC-1AE03B9EC3-L002464](../../agents/web_agent.py#L2464) | 2464 | `"                            headers={"` | — |
| [SRC-1AE03B9EC3-L002465](../../agents/web_agent.py#L2465) | 2465 | `"                                **headers,"` | — |
| [SRC-1AE03B9EC3-L002466](../../agents/web_agent.py#L2466) | 2466 | `"                                \"User-Agent\": reddit_user_agent,"` | — |
| [SRC-1AE03B9EC3-L002467](../../agents/web_agent.py#L2467) | 2467 | `"                                \"Authorization\": \"Bearer \" + access_token,"` | — |
| [SRC-1AE03B9EC3-L002468](../../agents/web_agent.py#L2468) | 2468 | `"                            },"` | — |
| [SRC-1AE03B9EC3-L002469](../../agents/web_agent.py#L2469) | 2469 | `"                            timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L002470](../../agents/web_agent.py#L2470) | 2470 | `"                            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L002471](../../agents/web_agent.py#L2471) | 2471 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L002472](../../agents/web_agent.py#L2472) | 2472 | `"                        if search_response.status_code == 200:"` | — |
| [SRC-1AE03B9EC3-L002473](../../agents/web_agent.py#L2473) | 2473 | `"                            children = search_response.json().get(\"data\", {}).get(\"children\", [])"` | — |
| [SRC-1AE03B9EC3-L002474](../../agents/web_agent.py#L2474) | 2474 | `"                            rank = 0"` | — |
| [SRC-1AE03B9EC3-L002475](../../agents/web_agent.py#L2475) | 2475 | `"                            for child in children:"` | — |
| [SRC-1AE03B9EC3-L002476](../../agents/web_agent.py#L2476) | 2476 | `"                                post = child.get(\"data\", {}) if isinstance(child, dict) else {}"` | — |
| [SRC-1AE03B9EC3-L002477](../../agents/web_agent.py#L2477) | 2477 | `"                                permalink = str(post.get(\"permalink\") or \"\")"` | — |
| [SRC-1AE03B9EC3-L002478](../../agents/web_agent.py#L2478) | 2478 | `"                                url = _public_http_url("` | — |
| [SRC-1AE03B9EC3-L002479](../../agents/web_agent.py#L2479) | 2479 | `"                                    permalink if permalink.startswith(\"http\")"` | — |
| [SRC-1AE03B9EC3-L002480](../../agents/web_agent.py#L2480) | 2480 | `"                                    else \"https://www.reddit.com\" + permalink"` | — |
| [SRC-1AE03B9EC3-L002481](../../agents/web_agent.py#L2481) | 2481 | `"                                )"` | — |
| [SRC-1AE03B9EC3-L002482](../../agents/web_agent.py#L2482) | 2482 | `"                                if not url:"` | — |
| [SRC-1AE03B9EC3-L002483](../../agents/web_agent.py#L2483) | 2483 | `"                                    continue"` | — |
| [SRC-1AE03B9EC3-L002484](../../agents/web_agent.py#L2484) | 2484 | `"                                rank += 1"` | — |
| [SRC-1AE03B9EC3-L002485](../../agents/web_agent.py#L2485) | 2485 | `"                                snippet = _clean_text(post.get(\"selftext\") or \"\", 1000)"` | — |
| [SRC-1AE03B9EC3-L002486](../../agents/web_agent.py#L2486) | 2486 | `"                                metrics = []"` | — |
| [SRC-1AE03B9EC3-L002487](../../agents/web_agent.py#L2487) | 2487 | `"                                if post.get(\"score\") is not None:"` | — |
| [SRC-1AE03B9EC3-L002488](../../agents/web_agent.py#L2488) | 2488 | `"                                    metrics.append(\"score=\" + str(post[\"score\"]))"` | — |
| [SRC-1AE03B9EC3-L002489](../../agents/web_agent.py#L2489) | 2489 | `"                                if post.get(\"num_comments\") is not None:"` | — |
| [SRC-1AE03B9EC3-L002490](../../agents/web_agent.py#L2490) | 2490 | `"                                    metrics.append(\"comments=\" + str(post[\"num_comments\"]))"` | — |
| [SRC-1AE03B9EC3-L002491](../../agents/web_agent.py#L2491) | 2491 | `"                                if metrics:"` | — |
| [SRC-1AE03B9EC3-L002492](../../agents/web_agent.py#L2492) | 2492 | `"                                    snippet = (snippet + \" \| \" if snippet else \"\") + \", \".join(metrics)"` | — |
| [SRC-1AE03B9EC3-L002493](../../agents/web_agent.py#L2493) | 2493 | `"                                results.append({"` | — |
| [SRC-1AE03B9EC3-L002494](../../agents/web_agent.py#L2494) | 2494 | `"                                    \"title\": _clean_text(post.get(\"title\") or \"Reddit post\", 300),"` | — |
| [SRC-1AE03B9EC3-L002495](../../agents/web_agent.py#L2495) | 2495 | `"                                    \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L002496](../../agents/web_agent.py#L2496) | 2496 | `"                                    \"snippet\": snippet,"` | — |
| [SRC-1AE03B9EC3-L002497](../../agents/web_agent.py#L2497) | 2497 | `"                                    \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L002498](../../agents/web_agent.py#L2498) | 2498 | `"                                    \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L002499](../../agents/web_agent.py#L2499) | 2499 | `"                                    \"provider\": \"reddit_oauth_api\","` | — |
| [SRC-1AE03B9EC3-L002500](../../agents/web_agent.py#L2500) | 2500 | `"                                    \"provider_rank\": rank,"` | — |
| [SRC-1AE03B9EC3-L002501](../../agents/web_agent.py#L2501) | 2501 | `"                                    \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L002502](../../agents/web_agent.py#L2502) | 2502 | `"                                    \"published_at\": _clean_text(str(post.get(\"created_utc\") or \"\"), 100),"` | — |
| [SRC-1AE03B9EC3-L002503](../../agents/web_agent.py#L2503) | 2503 | `"                                })"` | — |
| [SRC-1AE03B9EC3-L002504](../../agents/web_agent.py#L2504) | 2504 | `"                        else:"` | — |
| [SRC-1AE03B9EC3-L002505](../../agents/web_agent.py#L2505) | 2505 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L002506](../../agents/web_agent.py#L2506) | 2506 | `"                                f\"Reddit OAuth search unavailable (HTTP {search_response.status_code}).\""` | — |
| [SRC-1AE03B9EC3-L002507](../../agents/web_agent.py#L2507) | 2507 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L002508](../../agents/web_agent.py#L2508) | 2508 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L002509](../../agents/web_agent.py#L2509) | 2509 | `"                        warnings.append(\"Reddit OAuth did not return an access token.\")"` | — |
| [SRC-1AE03B9EC3-L002510](../../agents/web_agent.py#L2510) | 2510 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L002511](../../agents/web_agent.py#L2511) | 2511 | `"                    warnings.append("` | — |
| [SRC-1AE03B9EC3-L002512](../../agents/web_agent.py#L2512) | 2512 | `"                        f\"Reddit OAuth authentication unavailable (HTTP {token_response.status_code}).\""` | — |
| [SRC-1AE03B9EC3-L002513](../../agents/web_agent.py#L2513) | 2513 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L002514](../../agents/web_agent.py#L2514) | 2514 | `"            except (httpx.HTTPError, OSError, ValueError, KeyError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L002515](../../agents/web_agent.py#L2515) | 2515 | `"                warnings.append(\"Reddit OAuth search failed for this request.\")"` | — |
| [SRC-1AE03B9EC3-L002516](../../agents/web_agent.py#L2516) | 2516 | `""` | — |
| [SRC-1AE03B9EC3-L002517](../../agents/web_agent.py#L2517) | 2517 | `"        if \"reddit\" in platforms and not any("` | — |
| [SRC-1AE03B9EC3-L002518](../../agents/web_agent.py#L2518) | 2518 | `"            row.get(\"provider\") == \"reddit_oauth_api\" for row in results"` | — |
| [SRC-1AE03B9EC3-L002519](../../agents/web_agent.py#L2519) | 2519 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L002520](../../agents/web_agent.py#L2520) | 2520 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L002521](../../agents/web_agent.py#L2521) | 2521 | `"                self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L002522](../../agents/web_agent.py#L2522) | 2522 | `"                response = _bounded_http_request(\"GET\", "` | — |
| [SRC-1AE03B9EC3-L002523](../../agents/web_agent.py#L2523) | 2523 | `"                    \"https://www.reddit.com/search.rss\","` | — |
| [SRC-1AE03B9EC3-L002524](../../agents/web_agent.py#L2524) | 2524 | `"                    params={\"q\": query, \"sort\": \"relevance\", \"t\": \"all\", \"limit\": \"8\"},"` | — |
| [SRC-1AE03B9EC3-L002525](../../agents/web_agent.py#L2525) | 2525 | `"                    headers=headers,"` | — |
| [SRC-1AE03B9EC3-L002526](../../agents/web_agent.py#L2526) | 2526 | `"                    timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L002527](../../agents/web_agent.py#L2527) | 2527 | `"                    follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L002528](../../agents/web_agent.py#L2528) | 2528 | `"                )"` | — |
| [SRC-1AE03B9EC3-L002529](../../agents/web_agent.py#L2529) | 2529 | `"                if response.status_code == 200:"` | — |
| [SRC-1AE03B9EC3-L002530](../../agents/web_agent.py#L2530) | 2530 | `"                    root = ET.fromstring(response.content)"` | — |
| [SRC-1AE03B9EC3-L002531](../../agents/web_agent.py#L2531) | 2531 | `"                    for item in root.iter():"` | — |
| [SRC-1AE03B9EC3-L002532](../../agents/web_agent.py#L2532) | 2532 | `"                        if item.tag.rsplit(\"}\", 1)[-1] != \"item\":"` | — |
| [SRC-1AE03B9EC3-L002533](../../agents/web_agent.py#L2533) | 2533 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002534](../../agents/web_agent.py#L2534) | 2534 | `"                        fields = {"` | — |
| [SRC-1AE03B9EC3-L002535](../../agents/web_agent.py#L2535) | 2535 | `"                            child.tag.rsplit(\"}\", 1)[-1]: (child.text or \"\")"` | — |
| [SRC-1AE03B9EC3-L002536](../../agents/web_agent.py#L2536) | 2536 | `"                            for child in item"` | — |
| [SRC-1AE03B9EC3-L002537](../../agents/web_agent.py#L2537) | 2537 | `"                        }"` | — |
| [SRC-1AE03B9EC3-L002538](../../agents/web_agent.py#L2538) | 2538 | `"                        url = _public_http_url(fields.get(\"link\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L002539](../../agents/web_agent.py#L2539) | 2539 | `"                        if not url or \"reddit.com/\" not in url:"` | — |
| [SRC-1AE03B9EC3-L002540](../../agents/web_agent.py#L2540) | 2540 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002541](../../agents/web_agent.py#L2541) | 2541 | `"                        description = BeautifulSoup("` | — |
| [SRC-1AE03B9EC3-L002542](../../agents/web_agent.py#L2542) | 2542 | `"                            fields.get(\"description\", \"\"), \"html.parser\""` | — |
| [SRC-1AE03B9EC3-L002543](../../agents/web_agent.py#L2543) | 2543 | `"                        ).get_text(\" \", strip=True)"` | — |
| [SRC-1AE03B9EC3-L002544](../../agents/web_agent.py#L2544) | 2544 | `"                        results.append({"` | — |
| [SRC-1AE03B9EC3-L002545](../../agents/web_agent.py#L2545) | 2545 | `"                            \"title\": _clean_text(fields.get(\"title\", \"\"), 300),"` | — |
| [SRC-1AE03B9EC3-L002546](../../agents/web_agent.py#L2546) | 2546 | `"                            \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L002547](../../agents/web_agent.py#L2547) | 2547 | `"                            \"snippet\": _clean_text(description, 1200),"` | — |
| [SRC-1AE03B9EC3-L002548](../../agents/web_agent.py#L2548) | 2548 | `"                            \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L002549](../../agents/web_agent.py#L2549) | 2549 | `"                            \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L002550](../../agents/web_agent.py#L2550) | 2550 | `"                            \"provider\": \"reddit_public_rss\","` | — |
| [SRC-1AE03B9EC3-L002551](../../agents/web_agent.py#L2551) | 2551 | `"                            \"provider_rank\": len(["` | — |
| [SRC-1AE03B9EC3-L002552](../../agents/web_agent.py#L2552) | 2552 | `"                                row for row in results"` | — |
| [SRC-1AE03B9EC3-L002553](../../agents/web_agent.py#L2553) | 2553 | `"                                if row.get(\"provider\") == \"reddit_public_rss\""` | — |
| [SRC-1AE03B9EC3-L002554](../../agents/web_agent.py#L2554) | 2554 | `"                            ]) + 1,"` | — |
| [SRC-1AE03B9EC3-L002555](../../agents/web_agent.py#L2555) | 2555 | `"                            \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L002556](../../agents/web_agent.py#L2556) | 2556 | `"                            \"published_at\": _clean_text(fields.get(\"pubDate\", \"\"), 100),"` | — |
| [SRC-1AE03B9EC3-L002557](../../agents/web_agent.py#L2557) | 2557 | `"                        })"` | — |
| [SRC-1AE03B9EC3-L002558](../../agents/web_agent.py#L2558) | 2558 | `"                        if sum(row.get(\"provider\") == \"reddit_public_rss\" for row in results) >= 8:"` | — |
| [SRC-1AE03B9EC3-L002559](../../agents/web_agent.py#L2559) | 2559 | `"                            break"` | — |
| [SRC-1AE03B9EC3-L002560](../../agents/web_agent.py#L2560) | 2560 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L002561](../../agents/web_agent.py#L2561) | 2561 | `"                    warnings.append(f\"Reddit public RSS unavailable (HTTP {response.status_code})\")"` | — |
| [SRC-1AE03B9EC3-L002562](../../agents/web_agent.py#L2562) | 2562 | `"            except (httpx.HTTPError, OSError, ValueError, ET.ParseError):"` | — |
| [SRC-1AE03B9EC3-L002563](../../agents/web_agent.py#L2563) | 2563 | `"                warnings.append(\"Reddit public RSS unavailable for this request\")"` | — |
| [SRC-1AE03B9EC3-L002564](../../agents/web_agent.py#L2564) | 2564 | `""` | — |
| [SRC-1AE03B9EC3-L002565](../../agents/web_agent.py#L2565) | 2565 | `"        if \"bluesky\" in platforms:"` | — |
| [SRC-1AE03B9EC3-L002566](../../agents/web_agent.py#L2566) | 2566 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L002567](../../agents/web_agent.py#L2567) | 2567 | `"                self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L002568](../../agents/web_agent.py#L2568) | 2568 | `"                response = _bounded_http_request(\"GET\", "` | — |
| [SRC-1AE03B9EC3-L002569](../../agents/web_agent.py#L2569) | 2569 | `"                    \"https://public.api.bsky.app/xrpc/app.bsky.feed.searchPosts\","` | — |
| [SRC-1AE03B9EC3-L002570](../../agents/web_agent.py#L2570) | 2570 | `"                    params={\"q\": query, \"limit\": 10},"` | — |
| [SRC-1AE03B9EC3-L002571](../../agents/web_agent.py#L2571) | 2571 | `"                    headers=headers,"` | — |
| [SRC-1AE03B9EC3-L002572](../../agents/web_agent.py#L2572) | 2572 | `"                    timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L002573](../../agents/web_agent.py#L2573) | 2573 | `"                    follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L002574](../../agents/web_agent.py#L2574) | 2574 | `"                )"` | — |
| [SRC-1AE03B9EC3-L002575](../../agents/web_agent.py#L2575) | 2575 | `"                if response.status_code == 200:"` | — |
| [SRC-1AE03B9EC3-L002576](../../agents/web_agent.py#L2576) | 2576 | `"                    data = response.json()"` | — |
| [SRC-1AE03B9EC3-L002577](../../agents/web_agent.py#L2577) | 2577 | `"                    for item in data.get(\"posts\", []):"` | — |
| [SRC-1AE03B9EC3-L002578](../../agents/web_agent.py#L2578) | 2578 | `"                        post = item.get(\"post\", {})"` | — |
| [SRC-1AE03B9EC3-L002579](../../agents/web_agent.py#L2579) | 2579 | `"                        record = post.get(\"record\", {})"` | — |
| [SRC-1AE03B9EC3-L002580](../../agents/web_agent.py#L2580) | 2580 | `"                        author = post.get(\"author\", {})"` | — |
| [SRC-1AE03B9EC3-L002581](../../agents/web_agent.py#L2581) | 2581 | `"                        uri = post.get(\"uri\", \"\")"` | — |
| [SRC-1AE03B9EC3-L002582](../../agents/web_agent.py#L2582) | 2582 | `"                        rkey = uri.rsplit(\"/\", 1)[-1]"` | — |
| [SRC-1AE03B9EC3-L002583](../../agents/web_agent.py#L2583) | 2583 | `"                        handle = author.get(\"handle\", \"\")"` | — |
| [SRC-1AE03B9EC3-L002584](../../agents/web_agent.py#L2584) | 2584 | `"                        if not handle or not rkey:"` | — |
| [SRC-1AE03B9EC3-L002585](../../agents/web_agent.py#L2585) | 2585 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002586](../../agents/web_agent.py#L2586) | 2586 | `"                        url = f\"https://bsky.app/profile/{handle}/post/{rkey}\""` | — |
| [SRC-1AE03B9EC3-L002587](../../agents/web_agent.py#L2587) | 2587 | `"                        results.append({"` | — |
| [SRC-1AE03B9EC3-L002588](../../agents/web_agent.py#L2588) | 2588 | `"                            \"title\": _clean_text(author.get(\"displayName\") or handle, 300),"` | — |
| [SRC-1AE03B9EC3-L002589](../../agents/web_agent.py#L2589) | 2589 | `"                            \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L002590](../../agents/web_agent.py#L2590) | 2590 | `"                            \"snippet\": _clean_text(record.get(\"text\") or \"\", 1200),"` | — |
| [SRC-1AE03B9EC3-L002591](../../agents/web_agent.py#L2591) | 2591 | `"                            \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L002592](../../agents/web_agent.py#L2592) | 2592 | `"                            \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L002593](../../agents/web_agent.py#L2593) | 2593 | `"                            \"provider\": \"bluesky_public_search\","` | — |
| [SRC-1AE03B9EC3-L002594](../../agents/web_agent.py#L2594) | 2594 | `"                            \"provider_rank\": len(["` | — |
| [SRC-1AE03B9EC3-L002595](../../agents/web_agent.py#L2595) | 2595 | `"                                row for row in results"` | — |
| [SRC-1AE03B9EC3-L002596](../../agents/web_agent.py#L2596) | 2596 | `"                                if row.get(\"provider\") == \"bluesky_public_search\""` | — |
| [SRC-1AE03B9EC3-L002597](../../agents/web_agent.py#L2597) | 2597 | `"                            ]) + 1,"` | — |
| [SRC-1AE03B9EC3-L002598](../../agents/web_agent.py#L2598) | 2598 | `"                            \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L002599](../../agents/web_agent.py#L2599) | 2599 | `"                            \"published_at\": _clean_text(post.get(\"indexedAt\") or \"\", 100),"` | — |
| [SRC-1AE03B9EC3-L002600](../../agents/web_agent.py#L2600) | 2600 | `"                        })"` | — |
| [SRC-1AE03B9EC3-L002601](../../agents/web_agent.py#L2601) | 2601 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L002602](../../agents/web_agent.py#L2602) | 2602 | `"                    warnings.append(f\"Bluesky public search unavailable (HTTP {response.status_code})\")"` | — |
| [SRC-1AE03B9EC3-L002603](../../agents/web_agent.py#L2603) | 2603 | `"            except (httpx.HTTPError, OSError, ValueError, KeyError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L002604](../../agents/web_agent.py#L2604) | 2604 | `"                warnings.append(\"Bluesky public search unavailable for this request\")"` | — |
| [SRC-1AE03B9EC3-L002605](../../agents/web_agent.py#L2605) | 2605 | `""` | — |
| [SRC-1AE03B9EC3-L002606](../../agents/web_agent.py#L2606) | 2606 | `"        if \"facebook\" in platforms:"` | — |
| [SRC-1AE03B9EC3-L002607](../../agents/web_agent.py#L2607) | 2607 | `"            fb_token = os.getenv(\"FACEBOOK_PAGE_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L002608](../../agents/web_agent.py#L2608) | 2608 | `"            page_ids = ["` | — |
| [SRC-1AE03B9EC3-L002609](../../agents/web_agent.py#L2609) | 2609 | `"                value.strip()"` | — |
| [SRC-1AE03B9EC3-L002610](../../agents/web_agent.py#L2610) | 2610 | `"                for value in os.getenv(\"FACEBOOK_PAGE_IDS\", \"\").split(\",\")"` | — |
| [SRC-1AE03B9EC3-L002611](../../agents/web_agent.py#L2611) | 2611 | `"                if value.strip()"` | — |
| [SRC-1AE03B9EC3-L002612](../../agents/web_agent.py#L2612) | 2612 | `"            ][:5]"` | — |
| [SRC-1AE03B9EC3-L002613](../../agents/web_agent.py#L2613) | 2613 | `"            graph_version = os.getenv(\"META_GRAPH_VERSION\", \"v25.0\").strip()"` | — |
| [SRC-1AE03B9EC3-L002614](../../agents/web_agent.py#L2614) | 2614 | `"            if fb_token and page_ids:"` | — |
| [SRC-1AE03B9EC3-L002615](../../agents/web_agent.py#L2615) | 2615 | `"                # Scope direct reading to page IDs supplied by the operator and the"` | — |
| [SRC-1AE03B9EC3-L002616](../../agents/web_agent.py#L2616) | 2616 | `"                # permissions granted to this token. This is not global Facebook search."` | — |
| [SRC-1AE03B9EC3-L002617](../../agents/web_agent.py#L2617) | 2617 | `"                query_terms = {"` | — |
| [SRC-1AE03B9EC3-L002618](../../agents/web_agent.py#L2618) | 2618 | `"                    word.casefold()"` | — |
| [SRC-1AE03B9EC3-L002619](../../agents/web_agent.py#L2619) | 2619 | `"                    for word in re.findall(r\"[\\w\\u0600-\\u06FF]+\", query, flags=re.UNICODE)"` | — |
| [SRC-1AE03B9EC3-L002620](../../agents/web_agent.py#L2620) | 2620 | `"                    if len(word) >= 3"` | — |
| [SRC-1AE03B9EC3-L002621](../../agents/web_agent.py#L2621) | 2621 | `"                }"` | — |
| [SRC-1AE03B9EC3-L002622](../../agents/web_agent.py#L2622) | 2622 | `"                for page_id in page_ids:"` | — |
| [SRC-1AE03B9EC3-L002623](../../agents/web_agent.py#L2623) | 2623 | `"                    try:"` | — |
| [SRC-1AE03B9EC3-L002624](../../agents/web_agent.py#L2624) | 2624 | `"                        self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L002625](../../agents/web_agent.py#L2625) | 2625 | `"                        response = _bounded_http_request(\"GET\", "` | — |
| [SRC-1AE03B9EC3-L002626](../../agents/web_agent.py#L2626) | 2626 | `"                            f\"https://graph.facebook.com/{graph_version}/{page_id}/posts\","` | — |
| [SRC-1AE03B9EC3-L002627](../../agents/web_agent.py#L2627) | 2627 | `"                            params={"` | — |
| [SRC-1AE03B9EC3-L002628](../../agents/web_agent.py#L2628) | 2628 | `"                                \"fields\": ("` | — |
| [SRC-1AE03B9EC3-L002629](../../agents/web_agent.py#L2629) | 2629 | `"                                    \"message,permalink_url,created_time,\""` | — |
| [SRC-1AE03B9EC3-L002630](../../agents/web_agent.py#L2630) | 2630 | `"                                    \"comments.limit(10){message,created_time,like_count}\""` | — |
| [SRC-1AE03B9EC3-L002631](../../agents/web_agent.py#L2631) | 2631 | `"                                ),"` | — |
| [SRC-1AE03B9EC3-L002632](../../agents/web_agent.py#L2632) | 2632 | `"                                \"limit\": 10,"` | — |
| [SRC-1AE03B9EC3-L002633](../../agents/web_agent.py#L2633) | 2633 | `"                            },"` | — |
| [SRC-1AE03B9EC3-L002634](../../agents/web_agent.py#L2634) | 2634 | `"                            headers={"` | — |
| [SRC-1AE03B9EC3-L002635](../../agents/web_agent.py#L2635) | 2635 | `"                                **headers,"` | — |
| [SRC-1AE03B9EC3-L002636](../../agents/web_agent.py#L2636) | 2636 | `"                                \"Authorization\": \"Bearer \" + fb_token,"` | — |
| [SRC-1AE03B9EC3-L002637](../../agents/web_agent.py#L2637) | 2637 | `"                            },"` | — |
| [SRC-1AE03B9EC3-L002638](../../agents/web_agent.py#L2638) | 2638 | `"                            timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L002639](../../agents/web_agent.py#L2639) | 2639 | `"                            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L002640](../../agents/web_agent.py#L2640) | 2640 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L002641](../../agents/web_agent.py#L2641) | 2641 | `"                        if response.status_code != 200:"` | — |
| [SRC-1AE03B9EC3-L002642](../../agents/web_agent.py#L2642) | 2642 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L002643](../../agents/web_agent.py#L2643) | 2643 | `"                                \"Facebook Pages API unavailable for one configured page \""` | — |
| [SRC-1AE03B9EC3-L002644](../../agents/web_agent.py#L2644) | 2644 | `"                                f\"(HTTP {response.status_code}); verify page ownership, token and permissions.\""` | — |
| [SRC-1AE03B9EC3-L002645](../../agents/web_agent.py#L2645) | 2645 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L002646](../../agents/web_agent.py#L2646) | 2646 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002647](../../agents/web_agent.py#L2647) | 2647 | `"                        posts = response.json().get(\"data\", [])"` | — |
| [SRC-1AE03B9EC3-L002648](../../agents/web_agent.py#L2648) | 2648 | `"                        rank = 0"` | — |
| [SRC-1AE03B9EC3-L002649](../../agents/web_agent.py#L2649) | 2649 | `"                        for post in posts:"` | — |
| [SRC-1AE03B9EC3-L002650](../../agents/web_agent.py#L2650) | 2650 | `"                            message = _clean_text(post.get(\"message\") or \"\", 1400)"` | — |
| [SRC-1AE03B9EC3-L002651](../../agents/web_agent.py#L2651) | 2651 | `"                            comments = post.get(\"comments\", {}).get(\"data\", [])"` | — |
| [SRC-1AE03B9EC3-L002652](../../agents/web_agent.py#L2652) | 2652 | `"                            comment_text = ["` | — |
| [SRC-1AE03B9EC3-L002653](../../agents/web_agent.py#L2653) | 2653 | `"                                _clean_text(item.get(\"message\") or \"\", 500)"` | — |
| [SRC-1AE03B9EC3-L002654](../../agents/web_agent.py#L2654) | 2654 | `"                                for item in comments"` | — |
| [SRC-1AE03B9EC3-L002655](../../agents/web_agent.py#L2655) | 2655 | `"                                if isinstance(item, dict) and item.get(\"message\")"` | — |
| [SRC-1AE03B9EC3-L002656](../../agents/web_agent.py#L2656) | 2656 | `"                            ]"` | — |
| [SRC-1AE03B9EC3-L002657](../../agents/web_agent.py#L2657) | 2657 | `"                            searchable = (message + \" \" + \" \".join(comment_text)).casefold()"` | — |
| [SRC-1AE03B9EC3-L002658](../../agents/web_agent.py#L2658) | 2658 | `"                            matched = sum(term in searchable for term in query_terms)"` | — |
| [SRC-1AE03B9EC3-L002659](../../agents/web_agent.py#L2659) | 2659 | `"                            if query_terms and matched == 0:"` | — |
| [SRC-1AE03B9EC3-L002660](../../agents/web_agent.py#L2660) | 2660 | `"                                continue"` | — |
| [SRC-1AE03B9EC3-L002661](../../agents/web_agent.py#L2661) | 2661 | `"                            permalink = _public_http_url(post.get(\"permalink_url\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L002662](../../agents/web_agent.py#L2662) | 2662 | `"                            if not permalink:"` | — |
| [SRC-1AE03B9EC3-L002663](../../agents/web_agent.py#L2663) | 2663 | `"                                continue"` | — |
| [SRC-1AE03B9EC3-L002664](../../agents/web_agent.py#L2664) | 2664 | `"                            rank += 1"` | — |
| [SRC-1AE03B9EC3-L002665](../../agents/web_agent.py#L2665) | 2665 | `"                            excerpt = message"` | — |
| [SRC-1AE03B9EC3-L002666](../../agents/web_agent.py#L2666) | 2666 | `"                            if comment_text:"` | — |
| [SRC-1AE03B9EC3-L002667](../../agents/web_agent.py#L2667) | 2667 | `"                                excerpt = ("` | — |
| [SRC-1AE03B9EC3-L002668](../../agents/web_agent.py#L2668) | 2668 | `"                                    excerpt + \"\\n\\nتعليقات عامة على المنشور:\\n\""` | — |
| [SRC-1AE03B9EC3-L002669](../../agents/web_agent.py#L2669) | 2669 | `"                                    if excerpt else \"تعليقات عامة على المنشور:\\n\""` | — |
| [SRC-1AE03B9EC3-L002670](../../agents/web_agent.py#L2670) | 2670 | `"                                ) + \"\\n— \".join(comment_text)"` | — |
| [SRC-1AE03B9EC3-L002671](../../agents/web_agent.py#L2671) | 2671 | `"                            results.append({"` | — |
| [SRC-1AE03B9EC3-L002672](../../agents/web_agent.py#L2672) | 2672 | `"                                \"title\": _clean_text(message or \"Facebook public Page post\", 300),"` | — |
| [SRC-1AE03B9EC3-L002673](../../agents/web_agent.py#L2673) | 2673 | `"                                \"url\": permalink,"` | — |
| [SRC-1AE03B9EC3-L002674](../../agents/web_agent.py#L2674) | 2674 | `"                                \"snippet\": _clean_text(excerpt, 1800),"` | — |
| [SRC-1AE03B9EC3-L002675](../../agents/web_agent.py#L2675) | 2675 | `"                                \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L002676](../../agents/web_agent.py#L2676) | 2676 | `"                                \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L002677](../../agents/web_agent.py#L2677) | 2677 | `"                                \"provider\": \"facebook_pages_api\","` | — |
| [SRC-1AE03B9EC3-L002678](../../agents/web_agent.py#L2678) | 2678 | `"                                \"provider_rank\": rank,"` | — |
| [SRC-1AE03B9EC3-L002679](../../agents/web_agent.py#L2679) | 2679 | `"                                \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L002680](../../agents/web_agent.py#L2680) | 2680 | `"                                \"published_at\": _clean_text(post.get(\"created_time\") or \"\", 100),"` | — |
| [SRC-1AE03B9EC3-L002681](../../agents/web_agent.py#L2681) | 2681 | `"                            })"` | — |
| [SRC-1AE03B9EC3-L002682](../../agents/web_agent.py#L2682) | 2682 | `"                            if rank >= 10:"` | — |
| [SRC-1AE03B9EC3-L002683](../../agents/web_agent.py#L2683) | 2683 | `"                                break"` | — |
| [SRC-1AE03B9EC3-L002684](../../agents/web_agent.py#L2684) | 2684 | `"                    except (httpx.HTTPError, OSError, ValueError, KeyError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L002685](../../agents/web_agent.py#L2685) | 2685 | `"                        warnings.append(\"Facebook Pages API failed for one configured page.\")"` | — |
| [SRC-1AE03B9EC3-L002686](../../agents/web_agent.py#L2686) | 2686 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L002687](../../agents/web_agent.py#L2687) | 2687 | `"                warnings.append("` | — |
| [SRC-1AE03B9EC3-L002688](../../agents/web_agent.py#L2688) | 2688 | `"                    \"Facebook direct API is not configured for specific pages; indexed public Facebook pages are still searched.\""` | — |
| [SRC-1AE03B9EC3-L002689](../../agents/web_agent.py#L2689) | 2689 | `"                )"` | — |
| [SRC-1AE03B9EC3-L002690](../../agents/web_agent.py#L2690) | 2690 | `""` | — |
| [SRC-1AE03B9EC3-L002691](../../agents/web_agent.py#L2691) | 2691 | `"        if \"instagram\" in platforms:"` | — |
| [SRC-1AE03B9EC3-L002692](../../agents/web_agent.py#L2692) | 2692 | `"            ig_user_id = os.getenv(\"INSTAGRAM_USER_ID\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L002693](../../agents/web_agent.py#L2693) | 2693 | `"            ig_token = os.getenv(\"INSTAGRAM_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L002694](../../agents/web_agent.py#L2694) | 2694 | `"            graph_version = os.getenv(\"META_GRAPH_VERSION\", \"v25.0\").strip()"` | — |
| [SRC-1AE03B9EC3-L002695](../../agents/web_agent.py#L2695) | 2695 | `"            if ig_user_id and ig_token:"` | — |
| [SRC-1AE03B9EC3-L002696](../../agents/web_agent.py#L2696) | 2696 | `"                # The official Hashtag Search API returns public hashtag media only."` | — |
| [SRC-1AE03B9EC3-L002697](../../agents/web_agent.py#L2697) | 2697 | `"                # It does not search every Instagram post or bypass private accounts."` | — |
| [SRC-1AE03B9EC3-L002698](../../agents/web_agent.py#L2698) | 2698 | `"                hashtags = re.findall(r\"#([\\w\\u0600-\\u06FF]+)\", query, flags=re.UNICODE)"` | — |
| [SRC-1AE03B9EC3-L002699](../../agents/web_agent.py#L2699) | 2699 | `"                if not hashtags:"` | — |
| [SRC-1AE03B9EC3-L002700](../../agents/web_agent.py#L2700) | 2700 | `"                    words = re.findall(r\"[\\w\\u0600-\\u06FF]+\", query, flags=re.UNICODE)"` | — |
| [SRC-1AE03B9EC3-L002701](../../agents/web_agent.py#L2701) | 2701 | `"                    stopwords = {"` | — |
| [SRC-1AE03B9EC3-L002702](../../agents/web_agent.py#L2702) | 2702 | `"                        \"ابحث\", \"بحث\", \"عن\", \"في\", \"على\", \"من\", \"مع\", \"تجارب\","` | — |
| [SRC-1AE03B9EC3-L002703](../../agents/web_agent.py#L2703) | 2703 | `"                        \"الناس\", \"العملاء\", \"منشورات\", \"تعليقات\", \"مواقع\", \"التواصل\","` | — |
| [SRC-1AE03B9EC3-L002704](../../agents/web_agent.py#L2704) | 2704 | `"                        \"الاجتماعي\", \"public\", \"search\", \"social\", \"media\", \"posts\","` | — |
| [SRC-1AE03B9EC3-L002705](../../agents/web_agent.py#L2705) | 2705 | `"                        \"find\", \"about\", \"with\", \"the\", \"and\", \"for\","` | — |
| [SRC-1AE03B9EC3-L002706](../../agents/web_agent.py#L2706) | 2706 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L002707](../../agents/web_agent.py#L2707) | 2707 | `"                    useful = ["` | — |
| [SRC-1AE03B9EC3-L002708](../../agents/web_agent.py#L2708) | 2708 | `"                        word for word in words"` | — |
| [SRC-1AE03B9EC3-L002709](../../agents/web_agent.py#L2709) | 2709 | `"                        if len(word) >= 3 and word.casefold() not in stopwords"` | — |
| [SRC-1AE03B9EC3-L002710](../../agents/web_agent.py#L2710) | 2710 | `"                    ]"` | — |
| [SRC-1AE03B9EC3-L002711](../../agents/web_agent.py#L2711) | 2711 | `"                    if useful:"` | — |
| [SRC-1AE03B9EC3-L002712](../../agents/web_agent.py#L2712) | 2712 | `"                        hashtags = [\"_\".join(useful[:3])]"` | — |
| [SRC-1AE03B9EC3-L002713](../../agents/web_agent.py#L2713) | 2713 | `"                # Meta limits unique hashtag searches over a rolling week; keep this"` | — |
| [SRC-1AE03B9EC3-L002714](../../agents/web_agent.py#L2714) | 2714 | `"                # connector conservative and use no more than two tags per user request."` | — |
| [SRC-1AE03B9EC3-L002715](../../agents/web_agent.py#L2715) | 2715 | `"                for hashtag in list(dict.fromkeys(hashtags))[:1]:"` | — |
| [SRC-1AE03B9EC3-L002716](../../agents/web_agent.py#L2716) | 2716 | `"                    try:"` | — |
| [SRC-1AE03B9EC3-L002717](../../agents/web_agent.py#L2717) | 2717 | `"                        self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L002718](../../agents/web_agent.py#L2718) | 2718 | `"                        search_response = _bounded_http_request(\"GET\", "` | — |
| [SRC-1AE03B9EC3-L002719](../../agents/web_agent.py#L2719) | 2719 | `"                            f\"https://graph.facebook.com/{graph_version}/ig_hashtag_search\","` | — |
| [SRC-1AE03B9EC3-L002720](../../agents/web_agent.py#L2720) | 2720 | `"                            params={"` | — |
| [SRC-1AE03B9EC3-L002721](../../agents/web_agent.py#L2721) | 2721 | `"                                \"user_id\": ig_user_id,"` | — |
| [SRC-1AE03B9EC3-L002722](../../agents/web_agent.py#L2722) | 2722 | `"                                \"q\": hashtag,"` | — |
| [SRC-1AE03B9EC3-L002723](../../agents/web_agent.py#L2723) | 2723 | `"                                \"fields\": \"id,name\","` | — |
| [SRC-1AE03B9EC3-L002724](../../agents/web_agent.py#L2724) | 2724 | `"                                \"access_token\": ig_token,"` | — |
| [SRC-1AE03B9EC3-L002725](../../agents/web_agent.py#L2725) | 2725 | `"                            },"` | — |
| [SRC-1AE03B9EC3-L002726](../../agents/web_agent.py#L2726) | 2726 | `"                            headers=headers,"` | — |
| [SRC-1AE03B9EC3-L002727](../../agents/web_agent.py#L2727) | 2727 | `"                            timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L002728](../../agents/web_agent.py#L2728) | 2728 | `"                            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L002729](../../agents/web_agent.py#L2729) | 2729 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L002730](../../agents/web_agent.py#L2730) | 2730 | `"                        if search_response.status_code != 200:"` | — |
| [SRC-1AE03B9EC3-L002731](../../agents/web_agent.py#L2731) | 2731 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L002732](../../agents/web_agent.py#L2732) | 2732 | `"                                \"Instagram Graph API hashtag search unavailable \""` | — |
| [SRC-1AE03B9EC3-L002733](../../agents/web_agent.py#L2733) | 2733 | `"                                f\"(HTTP {search_response.status_code}); check permissions and access.\""` | — |
| [SRC-1AE03B9EC3-L002734](../../agents/web_agent.py#L2734) | 2734 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L002735](../../agents/web_agent.py#L2735) | 2735 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002736](../../agents/web_agent.py#L2736) | 2736 | `"                        tag_data = search_response.json().get(\"data\", [])"` | — |
| [SRC-1AE03B9EC3-L002737](../../agents/web_agent.py#L2737) | 2737 | `"                        if not tag_data:"` | — |
| [SRC-1AE03B9EC3-L002738](../../agents/web_agent.py#L2738) | 2738 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002739](../../agents/web_agent.py#L2739) | 2739 | `"                        hashtag_id = tag_data[0].get(\"id\")"` | — |
| [SRC-1AE03B9EC3-L002740](../../agents/web_agent.py#L2740) | 2740 | `"                        if not hashtag_id:"` | — |
| [SRC-1AE03B9EC3-L002741](../../agents/web_agent.py#L2741) | 2741 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002742](../../agents/web_agent.py#L2742) | 2742 | `"                        self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L002743](../../agents/web_agent.py#L2743) | 2743 | `"                        media_response = _bounded_http_request(\"GET\", "` | — |
| [SRC-1AE03B9EC3-L002744](../../agents/web_agent.py#L2744) | 2744 | `"                            f\"https://graph.facebook.com/{graph_version}/{hashtag_id}/recent_media\","` | — |
| [SRC-1AE03B9EC3-L002745](../../agents/web_agent.py#L2745) | 2745 | `"                            params={"` | — |
| [SRC-1AE03B9EC3-L002746](../../agents/web_agent.py#L2746) | 2746 | `"                                \"user_id\": ig_user_id,"` | — |
| [SRC-1AE03B9EC3-L002747](../../agents/web_agent.py#L2747) | 2747 | `"                                \"fields\": \"id,caption,media_type,permalink,timestamp,like_count,comments_count\","` | — |
| [SRC-1AE03B9EC3-L002748](../../agents/web_agent.py#L2748) | 2748 | `"                                \"limit\": 20,"` | — |
| [SRC-1AE03B9EC3-L002749](../../agents/web_agent.py#L2749) | 2749 | `"                                \"access_token\": ig_token,"` | — |
| [SRC-1AE03B9EC3-L002750](../../agents/web_agent.py#L2750) | 2750 | `"                            },"` | — |
| [SRC-1AE03B9EC3-L002751](../../agents/web_agent.py#L2751) | 2751 | `"                            headers=headers,"` | — |
| [SRC-1AE03B9EC3-L002752](../../agents/web_agent.py#L2752) | 2752 | `"                            timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L002753](../../agents/web_agent.py#L2753) | 2753 | `"                            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L002754](../../agents/web_agent.py#L2754) | 2754 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L002755](../../agents/web_agent.py#L2755) | 2755 | `"                        if media_response.status_code != 200:"` | — |
| [SRC-1AE03B9EC3-L002756](../../agents/web_agent.py#L2756) | 2756 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L002757](../../agents/web_agent.py#L2757) | 2757 | `"                                \"Instagram public hashtag media unavailable \""` | — |
| [SRC-1AE03B9EC3-L002758](../../agents/web_agent.py#L2758) | 2758 | `"                                f\"(HTTP {media_response.status_code}).\""` | — |
| [SRC-1AE03B9EC3-L002759](../../agents/web_agent.py#L2759) | 2759 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L002760](../../agents/web_agent.py#L2760) | 2760 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002761](../../agents/web_agent.py#L2761) | 2761 | `"                        items = media_response.json().get(\"data\", [])"` | — |
| [SRC-1AE03B9EC3-L002762](../../agents/web_agent.py#L2762) | 2762 | `"                        for item in items:"` | — |
| [SRC-1AE03B9EC3-L002763](../../agents/web_agent.py#L2763) | 2763 | `"                            url = _public_http_url(item.get(\"permalink\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L002764](../../agents/web_agent.py#L2764) | 2764 | `"                            if not url:"` | — |
| [SRC-1AE03B9EC3-L002765](../../agents/web_agent.py#L2765) | 2765 | `"                                continue"` | — |
| [SRC-1AE03B9EC3-L002766](../../agents/web_agent.py#L2766) | 2766 | `"                            metrics = []"` | — |
| [SRC-1AE03B9EC3-L002767](../../agents/web_agent.py#L2767) | 2767 | `"                            if item.get(\"like_count\") is not None:"` | — |
| [SRC-1AE03B9EC3-L002768](../../agents/web_agent.py#L2768) | 2768 | `"                                metrics.append(\"likes=\" + str(item[\"like_count\"]))"` | — |
| [SRC-1AE03B9EC3-L002769](../../agents/web_agent.py#L2769) | 2769 | `"                            if item.get(\"comments_count\") is not None:"` | — |
| [SRC-1AE03B9EC3-L002770](../../agents/web_agent.py#L2770) | 2770 | `"                                metrics.append(\"comments=\" + str(item[\"comments_count\"]))"` | — |
| [SRC-1AE03B9EC3-L002771](../../agents/web_agent.py#L2771) | 2771 | `"                            caption = _clean_text(item.get(\"caption\") or \"\", 1200)"` | — |
| [SRC-1AE03B9EC3-L002772](../../agents/web_agent.py#L2772) | 2772 | `"                            if metrics:"` | — |
| [SRC-1AE03B9EC3-L002773](../../agents/web_agent.py#L2773) | 2773 | `"                                caption = (caption + \" \| \" if caption else \"\") + \", \".join(metrics)"` | — |
| [SRC-1AE03B9EC3-L002774](../../agents/web_agent.py#L2774) | 2774 | `"                            results.append({"` | — |
| [SRC-1AE03B9EC3-L002775](../../agents/web_agent.py#L2775) | 2775 | `"                                \"title\": \"Instagram public hashtag: #\" + hashtag,"` | — |
| [SRC-1AE03B9EC3-L002776](../../agents/web_agent.py#L2776) | 2776 | `"                                \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L002777](../../agents/web_agent.py#L2777) | 2777 | `"                                \"snippet\": caption,"` | — |
| [SRC-1AE03B9EC3-L002778](../../agents/web_agent.py#L2778) | 2778 | `"                                \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L002779](../../agents/web_agent.py#L2779) | 2779 | `"                                \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L002780](../../agents/web_agent.py#L2780) | 2780 | `"                                \"provider\": \"instagram_graph_api\","` | — |
| [SRC-1AE03B9EC3-L002781](../../agents/web_agent.py#L2781) | 2781 | `"                                \"provider_rank\": len(["` | — |
| [SRC-1AE03B9EC3-L002782](../../agents/web_agent.py#L2782) | 2782 | `"                                    row for row in results"` | — |
| [SRC-1AE03B9EC3-L002783](../../agents/web_agent.py#L2783) | 2783 | `"                                    if row.get(\"provider\") == \"instagram_graph_api\""` | — |
| [SRC-1AE03B9EC3-L002784](../../agents/web_agent.py#L2784) | 2784 | `"                                ]) + 1,"` | — |
| [SRC-1AE03B9EC3-L002785](../../agents/web_agent.py#L2785) | 2785 | `"                                \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L002786](../../agents/web_agent.py#L2786) | 2786 | `"                                \"published_at\": _clean_text(item.get(\"timestamp\") or \"\", 100),"` | — |
| [SRC-1AE03B9EC3-L002787](../../agents/web_agent.py#L2787) | 2787 | `"                            })"` | — |
| [SRC-1AE03B9EC3-L002788](../../agents/web_agent.py#L2788) | 2788 | `"                    except (httpx.HTTPError, OSError, ValueError, KeyError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L002789](../../agents/web_agent.py#L2789) | 2789 | `"                        warnings.append(\"Instagram Graph API search failed for a requested hashtag.\")"` | — |
| [SRC-1AE03B9EC3-L002790](../../agents/web_agent.py#L2790) | 2790 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L002791](../../agents/web_agent.py#L2791) | 2791 | `"                warnings.append("` | — |
| [SRC-1AE03B9EC3-L002792](../../agents/web_agent.py#L2792) | 2792 | `"                    \"Instagram direct API is not configured; indexed public Instagram pages are still searched.\""` | — |
| [SRC-1AE03B9EC3-L002793](../../agents/web_agent.py#L2793) | 2793 | `"                )"` | — |
| [SRC-1AE03B9EC3-L002794](../../agents/web_agent.py#L2794) | 2794 | `""` | — |
| [SRC-1AE03B9EC3-L002795](../../agents/web_agent.py#L2795) | 2795 | `"        if \"x\" in platforms and os.getenv(\"X_BEARER_TOKEN\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L002796](../../agents/web_agent.py#L2796) | 2796 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L002797](../../agents/web_agent.py#L2797) | 2797 | `"                self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L002798](../../agents/web_agent.py#L2798) | 2798 | `"                response = _bounded_http_request(\"GET\", "` | — |
| [SRC-1AE03B9EC3-L002799](../../agents/web_agent.py#L2799) | 2799 | `"                    \"https://api.x.com/2/tweets/search/recent\","` | — |
| [SRC-1AE03B9EC3-L002800](../../agents/web_agent.py#L2800) | 2800 | `"                    params={"` | — |
| [SRC-1AE03B9EC3-L002801](../../agents/web_agent.py#L2801) | 2801 | `"                        \"query\": query + \" -is:retweet\","` | — |
| [SRC-1AE03B9EC3-L002802](../../agents/web_agent.py#L2802) | 2802 | `"                        \"max_results\": 10,"` | — |
| [SRC-1AE03B9EC3-L002803](../../agents/web_agent.py#L2803) | 2803 | `"                        \"tweet.fields\": \"created_at,lang,public_metrics,author_id\","` | — |
| [SRC-1AE03B9EC3-L002804](../../agents/web_agent.py#L2804) | 2804 | `"                        \"expansions\": \"author_id\","` | — |
| [SRC-1AE03B9EC3-L002805](../../agents/web_agent.py#L2805) | 2805 | `"                        \"user.fields\": \"name,username\","` | — |
| [SRC-1AE03B9EC3-L002806](../../agents/web_agent.py#L2806) | 2806 | `"                    },"` | — |
| [SRC-1AE03B9EC3-L002807](../../agents/web_agent.py#L2807) | 2807 | `"                    headers={"` | — |
| [SRC-1AE03B9EC3-L002808](../../agents/web_agent.py#L2808) | 2808 | `"                        **headers,"` | — |
| [SRC-1AE03B9EC3-L002809](../../agents/web_agent.py#L2809) | 2809 | `"                        \"Authorization\": \"Bearer \" + os.getenv(\"X_BEARER_TOKEN\", \"\").strip(),"` | — |
| [SRC-1AE03B9EC3-L002810](../../agents/web_agent.py#L2810) | 2810 | `"                    },"` | — |
| [SRC-1AE03B9EC3-L002811](../../agents/web_agent.py#L2811) | 2811 | `"                    timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L002812](../../agents/web_agent.py#L2812) | 2812 | `"                    follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L002813](../../agents/web_agent.py#L2813) | 2813 | `"                )"` | — |
| [SRC-1AE03B9EC3-L002814](../../agents/web_agent.py#L2814) | 2814 | `"                if response.status_code == 200:"` | — |
| [SRC-1AE03B9EC3-L002815](../../agents/web_agent.py#L2815) | 2815 | `"                    data = response.json()"` | — |
| [SRC-1AE03B9EC3-L002816](../../agents/web_agent.py#L2816) | 2816 | `"                    authors = {"` | — |
| [SRC-1AE03B9EC3-L002817](../../agents/web_agent.py#L2817) | 2817 | `"                        user.get(\"id\"): user"` | — |
| [SRC-1AE03B9EC3-L002818](../../agents/web_agent.py#L2818) | 2818 | `"                        for user in data.get(\"includes\", {}).get(\"users\", [])"` | — |
| [SRC-1AE03B9EC3-L002819](../../agents/web_agent.py#L2819) | 2819 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L002820](../../agents/web_agent.py#L2820) | 2820 | `"                    for item in data.get(\"data\", []):"` | — |
| [SRC-1AE03B9EC3-L002821](../../agents/web_agent.py#L2821) | 2821 | `"                        author = authors.get(item.get(\"author_id\"), {})"` | — |
| [SRC-1AE03B9EC3-L002822](../../agents/web_agent.py#L2822) | 2822 | `"                        username = author.get(\"username\", \"\")"` | — |
| [SRC-1AE03B9EC3-L002823](../../agents/web_agent.py#L2823) | 2823 | `"                        post_id = item.get(\"id\", \"\")"` | — |
| [SRC-1AE03B9EC3-L002824](../../agents/web_agent.py#L2824) | 2824 | `"                        if not username or not post_id:"` | — |
| [SRC-1AE03B9EC3-L002825](../../agents/web_agent.py#L2825) | 2825 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002826](../../agents/web_agent.py#L2826) | 2826 | `"                        results.append({"` | — |
| [SRC-1AE03B9EC3-L002827](../../agents/web_agent.py#L2827) | 2827 | `"                            \"title\": _clean_text(author.get(\"name\") or username, 300),"` | — |
| [SRC-1AE03B9EC3-L002828](../../agents/web_agent.py#L2828) | 2828 | `"                            \"url\": f\"https://x.com/{username}/status/{post_id}\","` | — |
| [SRC-1AE03B9EC3-L002829](../../agents/web_agent.py#L2829) | 2829 | `"                            \"snippet\": _clean_text(item.get(\"text\") or \"\", 1200),"` | — |
| [SRC-1AE03B9EC3-L002830](../../agents/web_agent.py#L2830) | 2830 | `"                            \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L002831](../../agents/web_agent.py#L2831) | 2831 | `"                            \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L002832](../../agents/web_agent.py#L2832) | 2832 | `"                            \"provider\": \"x_official_api\","` | — |
| [SRC-1AE03B9EC3-L002833](../../agents/web_agent.py#L2833) | 2833 | `"                            \"provider_rank\": len(["` | — |
| [SRC-1AE03B9EC3-L002834](../../agents/web_agent.py#L2834) | 2834 | `"                                row for row in results"` | — |
| [SRC-1AE03B9EC3-L002835](../../agents/web_agent.py#L2835) | 2835 | `"                                if row.get(\"provider\") == \"x_official_api\""` | — |
| [SRC-1AE03B9EC3-L002836](../../agents/web_agent.py#L2836) | 2836 | `"                            ]) + 1,"` | — |
| [SRC-1AE03B9EC3-L002837](../../agents/web_agent.py#L2837) | 2837 | `"                            \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L002838](../../agents/web_agent.py#L2838) | 2838 | `"                            \"published_at\": _clean_text(item.get(\"created_at\") or \"\", 100),"` | — |
| [SRC-1AE03B9EC3-L002839](../../agents/web_agent.py#L2839) | 2839 | `"                        })"` | — |
