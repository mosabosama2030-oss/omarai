# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **007**
- سجلات الأسطر: **800**
- النطاق: SRC-1AE03B9EC3-L002073 إلى SRC-1AE03B9EC3-L002872
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-1AE03B9EC3 — [agents/web_agent.py](../../agents/web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1AE03B9EC3-L002073](../../agents/web_agent.py#L2073) | 2073 | `"                    authors = {"` | — |
| [SRC-1AE03B9EC3-L002074](../../agents/web_agent.py#L2074) | 2074 | `"                        user.get(\"id\"): user"` | — |
| [SRC-1AE03B9EC3-L002075](../../agents/web_agent.py#L2075) | 2075 | `"                        for user in data.get(\"includes\", {}).get(\"users\", [])"` | — |
| [SRC-1AE03B9EC3-L002076](../../agents/web_agent.py#L2076) | 2076 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L002077](../../agents/web_agent.py#L2077) | 2077 | `"                    for item in data.get(\"data\", []):"` | — |
| [SRC-1AE03B9EC3-L002078](../../agents/web_agent.py#L2078) | 2078 | `"                        author = authors.get(item.get(\"author_id\"), {})"` | — |
| [SRC-1AE03B9EC3-L002079](../../agents/web_agent.py#L2079) | 2079 | `"                        username = author.get(\"username\", \"\")"` | — |
| [SRC-1AE03B9EC3-L002080](../../agents/web_agent.py#L2080) | 2080 | `"                        post_id = item.get(\"id\", \"\")"` | — |
| [SRC-1AE03B9EC3-L002081](../../agents/web_agent.py#L2081) | 2081 | `"                        if not username or not post_id:"` | — |
| [SRC-1AE03B9EC3-L002082](../../agents/web_agent.py#L2082) | 2082 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002083](../../agents/web_agent.py#L2083) | 2083 | `"                        results.append({"` | — |
| [SRC-1AE03B9EC3-L002084](../../agents/web_agent.py#L2084) | 2084 | `"                            \"title\": _clean_text(author.get(\"name\") or username, 300),"` | — |
| [SRC-1AE03B9EC3-L002085](../../agents/web_agent.py#L2085) | 2085 | `"                            \"url\": f\"https://x.com/{username}/status/{post_id}\","` | — |
| [SRC-1AE03B9EC3-L002086](../../agents/web_agent.py#L2086) | 2086 | `"                            \"snippet\": _clean_text(item.get(\"text\") or \"\", 1200),"` | — |
| [SRC-1AE03B9EC3-L002087](../../agents/web_agent.py#L2087) | 2087 | `"                            \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L002088](../../agents/web_agent.py#L2088) | 2088 | `"                            \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L002089](../../agents/web_agent.py#L2089) | 2089 | `"                            \"provider\": \"x_official_api\","` | — |
| [SRC-1AE03B9EC3-L002090](../../agents/web_agent.py#L2090) | 2090 | `"                            \"provider_rank\": len(["` | — |
| [SRC-1AE03B9EC3-L002091](../../agents/web_agent.py#L2091) | 2091 | `"                                row for row in results"` | — |
| [SRC-1AE03B9EC3-L002092](../../agents/web_agent.py#L2092) | 2092 | `"                                if row.get(\"provider\") == \"x_official_api\""` | — |
| [SRC-1AE03B9EC3-L002093](../../agents/web_agent.py#L2093) | 2093 | `"                            ]) + 1,"` | — |
| [SRC-1AE03B9EC3-L002094](../../agents/web_agent.py#L2094) | 2094 | `"                            \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L002095](../../agents/web_agent.py#L2095) | 2095 | `"                            \"published_at\": _clean_text(item.get(\"created_at\") or \"\", 100),"` | — |
| [SRC-1AE03B9EC3-L002096](../../agents/web_agent.py#L2096) | 2096 | `"                        })"` | — |
| [SRC-1AE03B9EC3-L002097](../../agents/web_agent.py#L2097) | 2097 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L002098](../../agents/web_agent.py#L2098) | 2098 | `"                    warnings.append(f\"X API unavailable (HTTP {response.status_code})\")"` | — |
| [SRC-1AE03B9EC3-L002099](../../agents/web_agent.py#L2099) | 2099 | `"            except (httpx.HTTPError, OSError, ValueError, KeyError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L002100](../../agents/web_agent.py#L2100) | 2100 | `"                warnings.append(\"X API unavailable for this request\")"` | — |
| [SRC-1AE03B9EC3-L002101](../../agents/web_agent.py#L2101) | 2101 | `"        elif \"x\" in platforms:"` | — |
| [SRC-1AE03B9EC3-L002102](../../agents/web_agent.py#L2102) | 2102 | `"            warnings.append(\"X direct API is not configured; indexed public X pages are still searched.\")"` | — |
| [SRC-1AE03B9EC3-L002103](../../agents/web_agent.py#L2103) | 2103 | `""` | — |
| [SRC-1AE03B9EC3-L002104](../../agents/web_agent.py#L2104) | 2104 | `"        if \"youtube\" in platforms and os.getenv(\"YOUTUBE_API_KEY\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L002105](../../agents/web_agent.py#L2105) | 2105 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L002106](../../agents/web_agent.py#L2106) | 2106 | `"                self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L002107](../../agents/web_agent.py#L2107) | 2107 | `"                response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L002108](../../agents/web_agent.py#L2108) | 2108 | `"                    \"https://www.googleapis.com/youtube/v3/search\","` | — |
| [SRC-1AE03B9EC3-L002109](../../agents/web_agent.py#L2109) | 2109 | `"                    params={"` | — |
| [SRC-1AE03B9EC3-L002110](../../agents/web_agent.py#L2110) | 2110 | `"                        \"part\": \"snippet\","` | — |
| [SRC-1AE03B9EC3-L002111](../../agents/web_agent.py#L2111) | 2111 | `"                        \"q\": query,"` | — |
| [SRC-1AE03B9EC3-L002112](../../agents/web_agent.py#L2112) | 2112 | `"                        \"type\": \"video\","` | — |
| [SRC-1AE03B9EC3-L002113](../../agents/web_agent.py#L2113) | 2113 | `"                        \"maxResults\": 8,"` | — |
| [SRC-1AE03B9EC3-L002114](../../agents/web_agent.py#L2114) | 2114 | `"                        \"key\": os.getenv(\"YOUTUBE_API_KEY\", \"\").strip(),"` | — |
| [SRC-1AE03B9EC3-L002115](../../agents/web_agent.py#L2115) | 2115 | `"                    },"` | — |
| [SRC-1AE03B9EC3-L002116](../../agents/web_agent.py#L2116) | 2116 | `"                    headers=headers,"` | — |
| [SRC-1AE03B9EC3-L002117](../../agents/web_agent.py#L2117) | 2117 | `"                    timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L002118](../../agents/web_agent.py#L2118) | 2118 | `"                    follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L002119](../../agents/web_agent.py#L2119) | 2119 | `"                )"` | — |
| [SRC-1AE03B9EC3-L002120](../../agents/web_agent.py#L2120) | 2120 | `"                if response.status_code == 200:"` | — |
| [SRC-1AE03B9EC3-L002121](../../agents/web_agent.py#L2121) | 2121 | `"                    data = response.json()"` | — |
| [SRC-1AE03B9EC3-L002122](../../agents/web_agent.py#L2122) | 2122 | `"                    for item in data.get(\"items\", []):"` | — |
| [SRC-1AE03B9EC3-L002123](../../agents/web_agent.py#L2123) | 2123 | `"                        video_id = item.get(\"id\", {}).get(\"videoId\")"` | — |
| [SRC-1AE03B9EC3-L002124](../../agents/web_agent.py#L2124) | 2124 | `"                        snippet = item.get(\"snippet\", {})"` | — |
| [SRC-1AE03B9EC3-L002125](../../agents/web_agent.py#L2125) | 2125 | `"                        if not video_id:"` | — |
| [SRC-1AE03B9EC3-L002126](../../agents/web_agent.py#L2126) | 2126 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002127](../../agents/web_agent.py#L2127) | 2127 | `"                        results.append({"` | — |
| [SRC-1AE03B9EC3-L002128](../../agents/web_agent.py#L2128) | 2128 | `"                            \"title\": _clean_text(snippet.get(\"title\") or \"\", 300),"` | — |
| [SRC-1AE03B9EC3-L002129](../../agents/web_agent.py#L2129) | 2129 | `"                            \"url\": f\"https://www.youtube.com/watch?v={video_id}\","` | — |
| [SRC-1AE03B9EC3-L002130](../../agents/web_agent.py#L2130) | 2130 | `"                            \"snippet\": _clean_text(snippet.get(\"description\") or \"\", 1200),"` | — |
| [SRC-1AE03B9EC3-L002131](../../agents/web_agent.py#L2131) | 2131 | `"                            \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L002132](../../agents/web_agent.py#L2132) | 2132 | `"                            \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L002133](../../agents/web_agent.py#L2133) | 2133 | `"                            \"provider\": \"youtube_data_api\","` | — |
| [SRC-1AE03B9EC3-L002134](../../agents/web_agent.py#L2134) | 2134 | `"                            \"provider_rank\": len(["` | — |
| [SRC-1AE03B9EC3-L002135](../../agents/web_agent.py#L2135) | 2135 | `"                                row for row in results"` | — |
| [SRC-1AE03B9EC3-L002136](../../agents/web_agent.py#L2136) | 2136 | `"                                if row.get(\"provider\") == \"youtube_data_api\""` | — |
| [SRC-1AE03B9EC3-L002137](../../agents/web_agent.py#L2137) | 2137 | `"                            ]) + 1,"` | — |
| [SRC-1AE03B9EC3-L002138](../../agents/web_agent.py#L2138) | 2138 | `"                            \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L002139](../../agents/web_agent.py#L2139) | 2139 | `"                            \"published_at\": _clean_text(snippet.get(\"publishedAt\") or \"\", 100),"` | — |
| [SRC-1AE03B9EC3-L002140](../../agents/web_agent.py#L2140) | 2140 | `"                        })"` | — |
| [SRC-1AE03B9EC3-L002141](../../agents/web_agent.py#L2141) | 2141 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L002142](../../agents/web_agent.py#L2142) | 2142 | `"                    warnings.append(f\"YouTube Data API unavailable (HTTP {response.status_code})\")"` | — |
| [SRC-1AE03B9EC3-L002143](../../agents/web_agent.py#L2143) | 2143 | `"            except (httpx.HTTPError, OSError, ValueError, KeyError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L002144](../../agents/web_agent.py#L2144) | 2144 | `"                warnings.append(\"YouTube Data API unavailable for this request\")"` | — |
| [SRC-1AE03B9EC3-L002145](../../agents/web_agent.py#L2145) | 2145 | `"        elif \"youtube\" in platforms:"` | — |
| [SRC-1AE03B9EC3-L002146](../../agents/web_agent.py#L2146) | 2146 | `"            warnings.append(\"YouTube direct API is not configured; indexed public YouTube pages are still searched.\")"` | — |
| [SRC-1AE03B9EC3-L002147](../../agents/web_agent.py#L2147) | 2147 | `""` | — |
| [SRC-1AE03B9EC3-L002148](../../agents/web_agent.py#L2148) | 2148 | `"        return results, warnings"` | — |
| [SRC-1AE03B9EC3-L002149](../../agents/web_agent.py#L2149) | 2149 | `""` | — |
| [SRC-1AE03B9EC3-L002150](../../agents/web_agent.py#L2150) | 2150 | `"    def _fetch_page(self, url: str) -> tuple[str, str]:"` | — |
| [SRC-1AE03B9EC3-L002151](../../agents/web_agent.py#L2151) | 2151 | `"        \"\"\"Fetch a public page with bounded redirects and an inspectable extraction outcome.\"\"\""` | — |
| [SRC-1AE03B9EC3-L002152](../../agents/web_agent.py#L2152) | 2152 | `"        def result("` | — |
| [SRC-1AE03B9EC3-L002153](../../agents/web_agent.py#L2153) | 2153 | `"            title: str = \"\","` | — |
| [SRC-1AE03B9EC3-L002154](../../agents/web_agent.py#L2154) | 2154 | `"            page_text: str = \"\","` | — |
| [SRC-1AE03B9EC3-L002155](../../agents/web_agent.py#L2155) | 2155 | `"            status: str = \"unknown\","` | — |
| [SRC-1AE03B9EC3-L002156](../../agents/web_agent.py#L2156) | 2156 | `"            error_class: str \| None = None,"` | — |
| [SRC-1AE03B9EC3-L002157](../../agents/web_agent.py#L2157) | 2157 | `"        ) -> PageFetchResult:"` | — |
| [SRC-1AE03B9EC3-L002158](../../agents/web_agent.py#L2158) | 2158 | `"            return PageFetchResult(title, page_text, status, error_class)"` | — |
| [SRC-1AE03B9EC3-L002159](../../agents/web_agent.py#L2159) | 2159 | `""` | — |
| [SRC-1AE03B9EC3-L002160](../../agents/web_agent.py#L2160) | 2160 | `"        current_url = _public_http_url(url)"` | — |
| [SRC-1AE03B9EC3-L002161](../../agents/web_agent.py#L2161) | 2161 | `"        if not current_url:"` | — |
| [SRC-1AE03B9EC3-L002162](../../agents/web_agent.py#L2162) | 2162 | `"            return result(status=\"rejected_url\", error_class=\"PublicUrlRejected\")"` | — |
| [SRC-1AE03B9EC3-L002163](../../agents/web_agent.py#L2163) | 2163 | `"        budget = getattr(self, \"_request_budget\", None)"` | — |
| [SRC-1AE03B9EC3-L002164](../../agents/web_agent.py#L2164) | 2164 | `"        if budget is not None:"` | — |
| [SRC-1AE03B9EC3-L002165](../../agents/web_agent.py#L2165) | 2165 | `"            budget.reserve(\"page_fetches\")"` | — |
| [SRC-1AE03B9EC3-L002166](../../agents/web_agent.py#L2166) | 2166 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L002167](../../agents/web_agent.py#L2167) | 2167 | `"            import httpx"` | — |
| [SRC-1AE03B9EC3-L002168](../../agents/web_agent.py#L2168) | 2168 | `"            from bs4 import BeautifulSoup"` | — |
| [SRC-1AE03B9EC3-L002169](../../agents/web_agent.py#L2169) | 2169 | `"        except ImportError as exc:"` | — |
| [SRC-1AE03B9EC3-L002170](../../agents/web_agent.py#L2170) | 2170 | `"            raise AgentDependencyError("` | — |
| [SRC-1AE03B9EC3-L002171](../../agents/web_agent.py#L2171) | 2171 | `"                \"حزم استخراج الصفحات غير مثبتة. نفّذ: python -m pip install -e .\""` | — |
| [SRC-1AE03B9EC3-L002172](../../agents/web_agent.py#L2172) | 2172 | `"            ) from exc"` | — |
| [SRC-1AE03B9EC3-L002173](../../agents/web_agent.py#L2173) | 2173 | `""` | — |
| [SRC-1AE03B9EC3-L002174](../../agents/web_agent.py#L2174) | 2174 | `"        headers = {"` | — |
| [SRC-1AE03B9EC3-L002175](../../agents/web_agent.py#L2175) | 2175 | `"            \"User-Agent\": \"OmaraiResearchBot/1.1 (public page research; no login)\","` | — |
| [SRC-1AE03B9EC3-L002176](../../agents/web_agent.py#L2176) | 2176 | `"            \"Accept\": \"text/html,application/xhtml+xml,text/plain;q=0.8\","` | — |
| [SRC-1AE03B9EC3-L002177](../../agents/web_agent.py#L2177) | 2177 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002178](../../agents/web_agent.py#L2178) | 2178 | `"        media_type = \"\""` | — |
| [SRC-1AE03B9EC3-L002179](../../agents/web_agent.py#L2179) | 2179 | `"        html = \"\""` | — |
| [SRC-1AE03B9EC3-L002180](../../agents/web_agent.py#L2180) | 2180 | `"        bytes_truncated = False"` | — |
| [SRC-1AE03B9EC3-L002181](../../agents/web_agent.py#L2181) | 2181 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L002182](../../agents/web_agent.py#L2182) | 2182 | `"            with httpx.Client("` | — |
| [SRC-1AE03B9EC3-L002183](../../agents/web_agent.py#L2183) | 2183 | `"                timeout=self._effective_timeout(8.0),"` | — |
| [SRC-1AE03B9EC3-L002184](../../agents/web_agent.py#L2184) | 2184 | `"                follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L002185](../../agents/web_agent.py#L2185) | 2185 | `"                headers=headers,"` | — |
| [SRC-1AE03B9EC3-L002186](../../agents/web_agent.py#L2186) | 2186 | `"                verify=True,"` | — |
| [SRC-1AE03B9EC3-L002187](../../agents/web_agent.py#L2187) | 2187 | `"                trust_env=False,"` | — |
| [SRC-1AE03B9EC3-L002188](../../agents/web_agent.py#L2188) | 2188 | `"            ) as client:"` | — |
| [SRC-1AE03B9EC3-L002189](../../agents/web_agent.py#L2189) | 2189 | `"                for redirect_number in range(4):"` | — |
| [SRC-1AE03B9EC3-L002190](../../agents/web_agent.py#L2190) | 2190 | `"                    parsed = urllib.parse.urlparse(current_url)"` | — |
| [SRC-1AE03B9EC3-L002191](../../agents/web_agent.py#L2191) | 2191 | `"                    host = parsed.hostname or \"\""` | — |
| [SRC-1AE03B9EC3-L002192](../../agents/web_agent.py#L2192) | 2192 | `"                    # Resolve and pin a public IP. Do not let the HTTP client resolve"` | — |
| [SRC-1AE03B9EC3-L002193](../../agents/web_agent.py#L2193) | 2193 | `"                    # the original hostname a second time."` | — |
| [SRC-1AE03B9EC3-L002194](../../agents/web_agent.py#L2194) | 2194 | `"                    public_ips = _public_ip_literals(host)"` | — |
| [SRC-1AE03B9EC3-L002195](../../agents/web_agent.py#L2195) | 2195 | `"                    if not public_ips:"` | — |
| [SRC-1AE03B9EC3-L002196](../../agents/web_agent.py#L2196) | 2196 | `"                        return result(status=\"blocked_or_unresolved_host\", error_class=\"HostResolutionOrSSRFCheck\")"` | — |
| [SRC-1AE03B9EC3-L002197](../../agents/web_agent.py#L2197) | 2197 | `"                    connect_url = _pinned_connect_url(current_url, public_ips[0])"` | — |
| [SRC-1AE03B9EC3-L002198](../../agents/web_agent.py#L2198) | 2198 | `"                    if not connect_url:"` | — |
| [SRC-1AE03B9EC3-L002199](../../agents/web_agent.py#L2199) | 2199 | `"                        return result(status=\"blocked_connection_target\", error_class=\"PinnedTargetRejected\")"` | — |
| [SRC-1AE03B9EC3-L002200](../../agents/web_agent.py#L2200) | 2200 | `"                    request_headers = {\"Host\": host}"` | — |
| [SRC-1AE03B9EC3-L002201](../../agents/web_agent.py#L2201) | 2201 | `"                    extensions = {\"sni_hostname\": host} if parsed.scheme == \"https\" else {}"` | — |
| [SRC-1AE03B9EC3-L002202](../../agents/web_agent.py#L2202) | 2202 | `"                    with client.stream("` | — |
| [SRC-1AE03B9EC3-L002203](../../agents/web_agent.py#L2203) | 2203 | `"                        \"GET\","` | — |
| [SRC-1AE03B9EC3-L002204](../../agents/web_agent.py#L2204) | 2204 | `"                        connect_url,"` | — |
| [SRC-1AE03B9EC3-L002205](../../agents/web_agent.py#L2205) | 2205 | `"                        headers=request_headers,"` | — |
| [SRC-1AE03B9EC3-L002206](../../agents/web_agent.py#L2206) | 2206 | `"                        extensions=extensions,"` | — |
| [SRC-1AE03B9EC3-L002207](../../agents/web_agent.py#L2207) | 2207 | `"                    ) as response:"` | — |
| [SRC-1AE03B9EC3-L002208](../../agents/web_agent.py#L2208) | 2208 | `"                        if response.status_code in {301, 302, 303, 307, 308}:"` | — |
| [SRC-1AE03B9EC3-L002209](../../agents/web_agent.py#L2209) | 2209 | `"                            location = response.headers.get(\"location\", \"\")"` | — |
| [SRC-1AE03B9EC3-L002210](../../agents/web_agent.py#L2210) | 2210 | `"                            if not location or redirect_number >= 3:"` | — |
| [SRC-1AE03B9EC3-L002211](../../agents/web_agent.py#L2211) | 2211 | `"                                return result(status=\"redirect_failed\", error_class=\"RedirectLimitOrMissingLocation\")"` | — |
| [SRC-1AE03B9EC3-L002212](../../agents/web_agent.py#L2212) | 2212 | `"                            target = _public_http_url("` | — |
| [SRC-1AE03B9EC3-L002213](../../agents/web_agent.py#L2213) | 2213 | `"                                urllib.parse.urljoin(current_url, location)"` | — |
| [SRC-1AE03B9EC3-L002214](../../agents/web_agent.py#L2214) | 2214 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L002215](../../agents/web_agent.py#L2215) | 2215 | `"                            if not target:"` | — |
| [SRC-1AE03B9EC3-L002216](../../agents/web_agent.py#L2216) | 2216 | `"                                return result(status=\"redirect_rejected\", error_class=\"RedirectTargetRejected\")"` | — |
| [SRC-1AE03B9EC3-L002217](../../agents/web_agent.py#L2217) | 2217 | `"                            current_url = target"` | — |
| [SRC-1AE03B9EC3-L002218](../../agents/web_agent.py#L2218) | 2218 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002219](../../agents/web_agent.py#L2219) | 2219 | `"                        if response.status_code < 200 or response.status_code >= 300:"` | — |
| [SRC-1AE03B9EC3-L002220](../../agents/web_agent.py#L2220) | 2220 | `"                            return result(status=\"http_error\", error_class=\"HTTPStatus\")"` | — |
| [SRC-1AE03B9EC3-L002221](../../agents/web_agent.py#L2221) | 2221 | `"                        media_type = response.headers.get("` | — |
| [SRC-1AE03B9EC3-L002222](../../agents/web_agent.py#L2222) | 2222 | `"                            \"content-type\", \"\""` | — |
| [SRC-1AE03B9EC3-L002223](../../agents/web_agent.py#L2223) | 2223 | `"                        ).split(\";\")[0].lower()"` | — |
| [SRC-1AE03B9EC3-L002224](../../agents/web_agent.py#L2224) | 2224 | `"                        if media_type not in {"` | — |
| [SRC-1AE03B9EC3-L002225](../../agents/web_agent.py#L2225) | 2225 | `"                            \"text/html\", \"application/xhtml+xml\", \"text/plain\""` | — |
| [SRC-1AE03B9EC3-L002226](../../agents/web_agent.py#L2226) | 2226 | `"                        }:"` | — |
| [SRC-1AE03B9EC3-L002227](../../agents/web_agent.py#L2227) | 2227 | `"                            return result(status=\"unsupported_content_type\", error_class=\"UnsupportedContentType\")"` | — |
| [SRC-1AE03B9EC3-L002228](../../agents/web_agent.py#L2228) | 2228 | `"                        content_length = response.headers.get(\"content-length\")"` | — |
| [SRC-1AE03B9EC3-L002229](../../agents/web_agent.py#L2229) | 2229 | `"                        if content_length:"` | — |
| [SRC-1AE03B9EC3-L002230](../../agents/web_agent.py#L2230) | 2230 | `"                            try:"` | — |
| [SRC-1AE03B9EC3-L002231](../../agents/web_agent.py#L2231) | 2231 | `"                                if int(content_length) > MAX_PAGE_BYTES:"` | — |
| [SRC-1AE03B9EC3-L002232](../../agents/web_agent.py#L2232) | 2232 | `"                                    return result(status=\"page_too_large\", error_class=\"ContentLengthLimit\")"` | — |
| [SRC-1AE03B9EC3-L002233](../../agents/web_agent.py#L2233) | 2233 | `"                            except ValueError:"` | — |
| [SRC-1AE03B9EC3-L002234](../../agents/web_agent.py#L2234) | 2234 | `"                                pass"` | — |
| [SRC-1AE03B9EC3-L002235](../../agents/web_agent.py#L2235) | 2235 | `"                        chunks: list[bytes] = []"` | — |
| [SRC-1AE03B9EC3-L002236](../../agents/web_agent.py#L2236) | 2236 | `"                        count = 0"` | — |
| [SRC-1AE03B9EC3-L002237](../../agents/web_agent.py#L2237) | 2237 | `"                        for chunk in response.iter_bytes():"` | — |
| [SRC-1AE03B9EC3-L002238](../../agents/web_agent.py#L2238) | 2238 | `"                            count += len(chunk)"` | — |
| [SRC-1AE03B9EC3-L002239](../../agents/web_agent.py#L2239) | 2239 | `"                            if count > MAX_PAGE_BYTES:"` | — |
| [SRC-1AE03B9EC3-L002240](../../agents/web_agent.py#L2240) | 2240 | `"                                remaining = max(0, MAX_PAGE_BYTES - (count - len(chunk)))"` | — |
| [SRC-1AE03B9EC3-L002241](../../agents/web_agent.py#L2241) | 2241 | `"                                if remaining:"` | — |
| [SRC-1AE03B9EC3-L002242](../../agents/web_agent.py#L2242) | 2242 | `"                                    chunks.append(chunk[:remaining])"` | — |
| [SRC-1AE03B9EC3-L002243](../../agents/web_agent.py#L2243) | 2243 | `"                                bytes_truncated = True"` | — |
| [SRC-1AE03B9EC3-L002244](../../agents/web_agent.py#L2244) | 2244 | `"                                break"` | — |
| [SRC-1AE03B9EC3-L002245](../../agents/web_agent.py#L2245) | 2245 | `"                            chunks.append(chunk)"` | — |
| [SRC-1AE03B9EC3-L002246](../../agents/web_agent.py#L2246) | 2246 | `"                        raw = b\"\".join(chunks)"` | — |
| [SRC-1AE03B9EC3-L002247](../../agents/web_agent.py#L2247) | 2247 | `"                        encoding = response.encoding or \"utf-8\""` | — |
| [SRC-1AE03B9EC3-L002248](../../agents/web_agent.py#L2248) | 2248 | `"                        html = raw.decode(encoding, errors=\"replace\")"` | — |
| [SRC-1AE03B9EC3-L002249](../../agents/web_agent.py#L2249) | 2249 | `"                        break"` | — |
| [SRC-1AE03B9EC3-L002250](../../agents/web_agent.py#L2250) | 2250 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L002251](../../agents/web_agent.py#L2251) | 2251 | `"                    return result(status=\"redirect_limit\", error_class=\"RedirectLimit\")"` | — |
| [SRC-1AE03B9EC3-L002252](../../agents/web_agent.py#L2252) | 2252 | `"        except (OSError, ValueError, httpx.HTTPError) as exc:"` | — |
| [SRC-1AE03B9EC3-L002253](../../agents/web_agent.py#L2253) | 2253 | `"            return result(status=\"network_error\", error_class=type(exc).__name__)"` | — |
| [SRC-1AE03B9EC3-L002254](../../agents/web_agent.py#L2254) | 2254 | `""` | — |
| [SRC-1AE03B9EC3-L002255](../../agents/web_agent.py#L2255) | 2255 | `"        if media_type == \"text/plain\":"` | — |
| [SRC-1AE03B9EC3-L002256](../../agents/web_agent.py#L2256) | 2256 | `"            bounded_text = _clean_text(html, MAX_PAGE_TEXT_CHARS + 1)"` | — |
| [SRC-1AE03B9EC3-L002257](../../agents/web_agent.py#L2257) | 2257 | `"            text_truncated = len(bounded_text) > MAX_PAGE_TEXT_CHARS"` | — |
| [SRC-1AE03B9EC3-L002258](../../agents/web_agent.py#L2258) | 2258 | `"            page_text = _clean_text(bounded_text, MAX_PAGE_TEXT_CHARS)"` | — |
| [SRC-1AE03B9EC3-L002259](../../agents/web_agent.py#L2259) | 2259 | `"            status = ("` | — |
| [SRC-1AE03B9EC3-L002260](../../agents/web_agent.py#L2260) | 2260 | `"                \"empty_content\" if not page_text"` | — |
| [SRC-1AE03B9EC3-L002261](../../agents/web_agent.py#L2261) | 2261 | `"                else \"partial_extraction\" if bytes_truncated or text_truncated"` | — |
| [SRC-1AE03B9EC3-L002262](../../agents/web_agent.py#L2262) | 2262 | `"                else \"content_extracted\""` | — |
| [SRC-1AE03B9EC3-L002263](../../agents/web_agent.py#L2263) | 2263 | `"            )"` | — |
| [SRC-1AE03B9EC3-L002264](../../agents/web_agent.py#L2264) | 2264 | `"            return result(\"\", page_text, status)"` | — |
| [SRC-1AE03B9EC3-L002265](../../agents/web_agent.py#L2265) | 2265 | `""` | — |
| [SRC-1AE03B9EC3-L002266](../../agents/web_agent.py#L2266) | 2266 | `"        soup = BeautifulSoup(html, \"html.parser\")"` | — |
| [SRC-1AE03B9EC3-L002267](../../agents/web_agent.py#L2267) | 2267 | `"        title = _clean_text(soup.title.get_text(\" \", strip=True), 300) if soup.title else \"\""` | — |
| [SRC-1AE03B9EC3-L002268](../../agents/web_agent.py#L2268) | 2268 | `"        for element in soup(["` | — |
| [SRC-1AE03B9EC3-L002269](../../agents/web_agent.py#L2269) | 2269 | `"            \"script\", \"style\", \"nav\", \"footer\", \"header\", \"noscript\","` | — |
| [SRC-1AE03B9EC3-L002270](../../agents/web_agent.py#L2270) | 2270 | `"            \"svg\", \"form\", \"iframe\", \"template\""` | — |
| [SRC-1AE03B9EC3-L002271](../../agents/web_agent.py#L2271) | 2271 | `"        ]):"` | — |
| [SRC-1AE03B9EC3-L002272](../../agents/web_agent.py#L2272) | 2272 | `"            element.decompose()"` | — |
| [SRC-1AE03B9EC3-L002273](../../agents/web_agent.py#L2273) | 2273 | `"        main = soup.find(\"main\") or soup.find(\"article\") or soup.body or soup"` | — |
| [SRC-1AE03B9EC3-L002274](../../agents/web_agent.py#L2274) | 2274 | `"        bounded_text = _clean_text(main.get_text(\" \", strip=True), MAX_PAGE_TEXT_CHARS + 1)"` | — |
| [SRC-1AE03B9EC3-L002275](../../agents/web_agent.py#L2275) | 2275 | `"        text_truncated = len(bounded_text) > MAX_PAGE_TEXT_CHARS"` | — |
| [SRC-1AE03B9EC3-L002276](../../agents/web_agent.py#L2276) | 2276 | `"        page_text = _clean_text(bounded_text, MAX_PAGE_TEXT_CHARS)"` | — |
| [SRC-1AE03B9EC3-L002277](../../agents/web_agent.py#L2277) | 2277 | `"        status = ("` | — |
| [SRC-1AE03B9EC3-L002278](../../agents/web_agent.py#L2278) | 2278 | `"            \"no_text_extracted\" if not page_text"` | — |
| [SRC-1AE03B9EC3-L002279](../../agents/web_agent.py#L2279) | 2279 | `"            else \"partial_extraction\" if bytes_truncated or text_truncated"` | — |
| [SRC-1AE03B9EC3-L002280](../../agents/web_agent.py#L2280) | 2280 | `"            else \"content_extracted\""` | — |
| [SRC-1AE03B9EC3-L002281](../../agents/web_agent.py#L2281) | 2281 | `"        )"` | — |
| [SRC-1AE03B9EC3-L002282](../../agents/web_agent.py#L2282) | 2282 | `"        return result(title, page_text, status)"` | — |
| [SRC-1AE03B9EC3-L002283](../../agents/web_agent.py#L2283) | 2283 | `""` | — |
| [SRC-1AE03B9EC3-L002284](../../agents/web_agent.py#L2284) | 2284 | `"    def _collect_sources(self, query: str) -> tuple[list[dict[str, Any]], str \| None]:"` | — |
| [SRC-1AE03B9EC3-L002285](../../agents/web_agent.py#L2285) | 2285 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L002286](../../agents/web_agent.py#L2286) | 2286 | `"            sources = self._search_web(query)"` | — |
| [SRC-1AE03B9EC3-L002287](../../agents/web_agent.py#L2287) | 2287 | `"        except (RuntimeError, AgentDependencyError) as exc:"` | — |
| [SRC-1AE03B9EC3-L002288](../../agents/web_agent.py#L2288) | 2288 | `"            return [], str(exc)"` | — |
| [SRC-1AE03B9EC3-L002289](../../agents/web_agent.py#L2289) | 2289 | `"        for source in sources[:MAX_FETCHED_PAGES]:"` | — |
| [SRC-1AE03B9EC3-L002290](../../agents/web_agent.py#L2290) | 2290 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L002291](../../agents/web_agent.py#L2291) | 2291 | `"                title, page_text = self._fetch_page(source[\"url\"])"` | — |
| [SRC-1AE03B9EC3-L002292](../../agents/web_agent.py#L2292) | 2292 | `"            except (AgentDependencyError, RuntimeError):"` | — |
| [SRC-1AE03B9EC3-L002293](../../agents/web_agent.py#L2293) | 2293 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L002294](../../agents/web_agent.py#L2294) | 2294 | `"            if title:"` | — |
| [SRC-1AE03B9EC3-L002295](../../agents/web_agent.py#L2295) | 2295 | `"                source[\"title\"] = title"` | — |
| [SRC-1AE03B9EC3-L002296](../../agents/web_agent.py#L2296) | 2296 | `"            if page_text:"` | — |
| [SRC-1AE03B9EC3-L002297](../../agents/web_agent.py#L2297) | 2297 | `"                source[\"page_text\"] = page_text"` | — |
| [SRC-1AE03B9EC3-L002298](../../agents/web_agent.py#L2298) | 2298 | `"                source[\"page_fetched\"] = True"` | — |
| [SRC-1AE03B9EC3-L002299](../../agents/web_agent.py#L2299) | 2299 | `"                # Prefer extracted text over a thin search snippet."` | — |
| [SRC-1AE03B9EC3-L002300](../../agents/web_agent.py#L2300) | 2300 | `"                source[\"snippet\"] = page_text[:1800]"` | — |
| [SRC-1AE03B9EC3-L002301](../../agents/web_agent.py#L2301) | 2301 | `"        return sources, None"` | — |
| [SRC-1AE03B9EC3-L002302](../../agents/web_agent.py#L2302) | 2302 | `""` | — |
| [SRC-1AE03B9EC3-L002303](../../agents/web_agent.py#L2303) | 2303 | `"    def _collect_research("` | — |
| [SRC-1AE03B9EC3-L002304](../../agents/web_agent.py#L2304) | 2304 | `"        self, plan: dict[str, Any]"` | — |
| [SRC-1AE03B9EC3-L002305](../../agents/web_agent.py#L2305) | 2305 | `"    ) -> tuple[list[dict[str, Any]], list[str], dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L002306](../../agents/web_agent.py#L2306) | 2306 | `"        \"\"\"Run independent query searches concurrently, fuse evidence, then fetch top pages.\"\"\""` | — |
| [SRC-1AE03B9EC3-L002307](../../agents/web_agent.py#L2307) | 2307 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L002308](../../agents/web_agent.py#L2308) | 2308 | `"            query_limit = int(plan.get(\"query_limit\", MAX_PLAN_QUERIES))"` | — |
| [SRC-1AE03B9EC3-L002309](../../agents/web_agent.py#L2309) | 2309 | `"        except (TypeError, ValueError, OverflowError):"` | — |
| [SRC-1AE03B9EC3-L002310](../../agents/web_agent.py#L2310) | 2310 | `"            query_limit = MAX_PLAN_QUERIES"` | — |
| [SRC-1AE03B9EC3-L002311](../../agents/web_agent.py#L2311) | 2311 | `"        query_limit = max(1, min(query_limit, MAX_PLAN_QUERIES))"` | — |
| [SRC-1AE03B9EC3-L002312](../../agents/web_agent.py#L2312) | 2312 | `"        queries = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L002313](../../agents/web_agent.py#L2313) | 2313 | `"            compact_search_query(query)"` | — |
| [SRC-1AE03B9EC3-L002314](../../agents/web_agent.py#L2314) | 2314 | `"            for query in plan.get(\"queries\", [])[:query_limit]"` | — |
| [SRC-1AE03B9EC3-L002315](../../agents/web_agent.py#L2315) | 2315 | `"            if isinstance(query, str) and query.strip()"` | — |
| [SRC-1AE03B9EC3-L002316](../../agents/web_agent.py#L2316) | 2316 | `"        ))"` | — |
| [SRC-1AE03B9EC3-L002317](../../agents/web_agent.py#L2317) | 2317 | `"        queries = [query for query in queries if query]"` | — |
| [SRC-1AE03B9EC3-L002318](../../agents/web_agent.py#L2318) | 2318 | `"        warnings: list[str] = []"` | — |
| [SRC-1AE03B9EC3-L002319](../../agents/web_agent.py#L2319) | 2319 | `"        if not queries and not plan.get(\"direct_urls\"):"` | — |
| [SRC-1AE03B9EC3-L002320](../../agents/web_agent.py#L2320) | 2320 | `"            warnings.append(\"لم يُنشأ استعلام موضوعي قابل للبحث؛ لم تُستدعَ محركات البحث.\")"` | — |
| [SRC-1AE03B9EC3-L002321](../../agents/web_agent.py#L2321) | 2321 | `"        batches: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L002322](../../agents/web_agent.py#L2322) | 2322 | `"        query_counts: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L002323](../../agents/web_agent.py#L2323) | 2323 | `"        search_started_queries = 0"` | — |
| [SRC-1AE03B9EC3-L002324](../../agents/web_agent.py#L2324) | 2324 | `""` | — |
| [SRC-1AE03B9EC3-L002325](../../agents/web_agent.py#L2325) | 2325 | `"        if queries:"` | — |
| [SRC-1AE03B9EC3-L002326](../../agents/web_agent.py#L2326) | 2326 | `"            with ThreadPoolExecutor(max_workers=min(MAX_RESEARCH_WORKERS, len(queries))) as pool:"` | — |
| [SRC-1AE03B9EC3-L002327](../../agents/web_agent.py#L2327) | 2327 | `"                futures = {pool.submit(self._search_web, query): query for query in queries}"` | — |
| [SRC-1AE03B9EC3-L002328](../../agents/web_agent.py#L2328) | 2328 | `"                for future in as_completed(futures):"` | — |
| [SRC-1AE03B9EC3-L002329](../../agents/web_agent.py#L2329) | 2329 | `"                    query = futures[future]"` | — |
| [SRC-1AE03B9EC3-L002330](../../agents/web_agent.py#L2330) | 2330 | `"                    search_started_queries += 1"` | — |
| [SRC-1AE03B9EC3-L002331](../../agents/web_agent.py#L2331) | 2331 | `"                    try:"` | — |
| [SRC-1AE03B9EC3-L002332](../../agents/web_agent.py#L2332) | 2332 | `"                        results = future.result()"` | — |
| [SRC-1AE03B9EC3-L002333](../../agents/web_agent.py#L2333) | 2333 | `"                    except (RequestBudgetExceeded, RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L002334](../../agents/web_agent.py#L2334) | 2334 | `"                        warnings.append(f\"تعذر بحث الاستعلام «{query[:70]}»: {exc}\")"` | — |
| [SRC-1AE03B9EC3-L002335](../../agents/web_agent.py#L2335) | 2335 | `"                        query_counts.append({\"query\": query, \"results\": 0})"` | — |
| [SRC-1AE03B9EC3-L002336](../../agents/web_agent.py#L2336) | 2336 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L002337](../../agents/web_agent.py#L2337) | 2337 | `"                    query_counts.append({\"query\": query, \"results\": len(results)})"` | — |
| [SRC-1AE03B9EC3-L002338](../../agents/web_agent.py#L2338) | 2338 | `"                    grouped: dict[str, list[dict[str, Any]]] = {}"` | — |
| [SRC-1AE03B9EC3-L002339](../../agents/web_agent.py#L2339) | 2339 | `"                    for source in results:"` | — |
| [SRC-1AE03B9EC3-L002340](../../agents/web_agent.py#L2340) | 2340 | `"                        provider = str(source.get(\"provider\") or \"web_search\")"` | — |
| [SRC-1AE03B9EC3-L002341](../../agents/web_agent.py#L2341) | 2341 | `"                        grouped.setdefault(provider, []).append(source)"` | — |
| [SRC-1AE03B9EC3-L002342](../../agents/web_agent.py#L2342) | 2342 | `"                    for provider, items in grouped.items():"` | — |
| [SRC-1AE03B9EC3-L002343](../../agents/web_agent.py#L2343) | 2343 | `"                        items.sort(key=lambda item: int(item.get(\"provider_rank\", 999)))"` | — |
| [SRC-1AE03B9EC3-L002344](../../agents/web_agent.py#L2344) | 2344 | `"                        batches.append({\"query\": query, \"provider\": provider, \"results\": items})"` | — |
| [SRC-1AE03B9EC3-L002345](../../agents/web_agent.py#L2345) | 2345 | `""` | — |
| [SRC-1AE03B9EC3-L002346](../../agents/web_agent.py#L2346) | 2346 | `"        # Evidence-gap iteration: deep tasks get up to three targeted follow-up searches"` | — |
| [SRC-1AE03B9EC3-L002347](../../agents/web_agent.py#L2347) | 2347 | `"        # when initial coverage is thin. This uses observed source/domain/provider coverage,"` | — |
| [SRC-1AE03B9EC3-L002348](../../agents/web_agent.py#L2348) | 2348 | `"        # not the language model's subjective claim that it has enough evidence."` | — |
| [SRC-1AE03B9EC3-L002349](../../agents/web_agent.py#L2349) | 2349 | `"        preliminary = fuse_ranked_results(batches, limit=MAX_SEARCH_RESULTS)"` | — |
| [SRC-1AE03B9EC3-L002350](../../agents/web_agent.py#L2350) | 2350 | `"        preliminary_domains = {"` | — |
| [SRC-1AE03B9EC3-L002351](../../agents/web_agent.py#L2351) | 2351 | `"            registrable_domain(item.get(\"domain\") or urllib.parse.urlparse(item.get(\"url\", \"\")).hostname)"` | — |
| [SRC-1AE03B9EC3-L002352](../../agents/web_agent.py#L2352) | 2352 | `"            for item in preliminary"` | — |
| [SRC-1AE03B9EC3-L002353](../../agents/web_agent.py#L2353) | 2353 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002354](../../agents/web_agent.py#L2354) | 2354 | `"        preliminary_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L002355](../../agents/web_agent.py#L2355) | 2355 | `"        preliminary_providers = {"` | — |
| [SRC-1AE03B9EC3-L002356](../../agents/web_agent.py#L2356) | 2356 | `"            provider for item in preliminary for provider in item.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L002357](../../agents/web_agent.py#L2357) | 2357 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002358](../../agents/web_agent.py#L2358) | 2358 | `"        needs_expansion = ("` | — |
| [SRC-1AE03B9EC3-L002359](../../agents/web_agent.py#L2359) | 2359 | `"            plan.get(\"depth\") == \"deep\""` | — |
| [SRC-1AE03B9EC3-L002360](../../agents/web_agent.py#L2360) | 2360 | `"            and (len(preliminary) < 8 or len(preliminary_domains) < 5 or len(preliminary_providers) < 2)"` | — |
| [SRC-1AE03B9EC3-L002361](../../agents/web_agent.py#L2361) | 2361 | `"        )"` | — |
| [SRC-1AE03B9EC3-L002362](../../agents/web_agent.py#L2362) | 2362 | `"        expansion_queries: list[str] = []"` | — |
| [SRC-1AE03B9EC3-L002363](../../agents/web_agent.py#L2363) | 2363 | `"        if needs_expansion and len(queries) < query_limit and queries:"` | — |
| [SRC-1AE03B9EC3-L002364](../../agents/web_agent.py#L2364) | 2364 | `"            base_query = (queries[0] if queries else \"\")"` | — |
| [SRC-1AE03B9EC3-L002365](../../agents/web_agent.py#L2365) | 2365 | `"            candidates = ["` | — |
| [SRC-1AE03B9EC3-L002366](../../agents/web_agent.py#L2366) | 2366 | `"                f\"{base_query} official sources data reports\","` | — |
| [SRC-1AE03B9EC3-L002367](../../agents/web_agent.py#L2367) | 2367 | `"                f\"{base_query} limitations risks criticism alternatives\","` | — |
| [SRC-1AE03B9EC3-L002368](../../agents/web_agent.py#L2368) | 2368 | `"                f\"{base_query} recent developments case studies analysis\","` | — |
| [SRC-1AE03B9EC3-L002369](../../agents/web_agent.py#L2369) | 2369 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L002370](../../agents/web_agent.py#L2370) | 2370 | `"            existing = {item.casefold() for item in queries}"` | — |
| [SRC-1AE03B9EC3-L002371](../../agents/web_agent.py#L2371) | 2371 | `"            expansion_queries = []"` | — |
| [SRC-1AE03B9EC3-L002372](../../agents/web_agent.py#L2372) | 2372 | `"            seen_expansions = set(existing)"` | — |
| [SRC-1AE03B9EC3-L002373](../../agents/web_agent.py#L2373) | 2373 | `"            for candidate in candidates:"` | — |
| [SRC-1AE03B9EC3-L002374](../../agents/web_agent.py#L2374) | 2374 | `"                compacted = compact_search_query(candidate)"` | — |
| [SRC-1AE03B9EC3-L002375](../../agents/web_agent.py#L2375) | 2375 | `"                key = compacted.casefold()"` | — |
| [SRC-1AE03B9EC3-L002376](../../agents/web_agent.py#L2376) | 2376 | `"                if compacted and key not in seen_expansions:"` | — |
| [SRC-1AE03B9EC3-L002377](../../agents/web_agent.py#L2377) | 2377 | `"                    expansion_queries.append(compacted)"` | — |
| [SRC-1AE03B9EC3-L002378](../../agents/web_agent.py#L2378) | 2378 | `"                    seen_expansions.add(key)"` | — |
| [SRC-1AE03B9EC3-L002379](../../agents/web_agent.py#L2379) | 2379 | `"                if len(expansion_queries) >= max(0, query_limit - len(queries)):"` | — |
| [SRC-1AE03B9EC3-L002380](../../agents/web_agent.py#L2380) | 2380 | `"                    break"` | — |
| [SRC-1AE03B9EC3-L002381](../../agents/web_agent.py#L2381) | 2381 | `"            if expansion_queries:"` | — |
| [SRC-1AE03B9EC3-L002382](../../agents/web_agent.py#L2382) | 2382 | `"                with ThreadPoolExecutor("` | — |
| [SRC-1AE03B9EC3-L002383](../../agents/web_agent.py#L2383) | 2383 | `"                    max_workers=min(MAX_RESEARCH_WORKERS, len(expansion_queries))"` | — |
| [SRC-1AE03B9EC3-L002384](../../agents/web_agent.py#L2384) | 2384 | `"                ) as pool:"` | — |
| [SRC-1AE03B9EC3-L002385](../../agents/web_agent.py#L2385) | 2385 | `"                    futures = {"` | — |
| [SRC-1AE03B9EC3-L002386](../../agents/web_agent.py#L2386) | 2386 | `"                        pool.submit(self._search_web, query): query"` | — |
| [SRC-1AE03B9EC3-L002387](../../agents/web_agent.py#L2387) | 2387 | `"                        for query in expansion_queries"` | — |
| [SRC-1AE03B9EC3-L002388](../../agents/web_agent.py#L2388) | 2388 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L002389](../../agents/web_agent.py#L2389) | 2389 | `"                    for future in as_completed(futures):"` | — |
| [SRC-1AE03B9EC3-L002390](../../agents/web_agent.py#L2390) | 2390 | `"                        query = futures[future]"` | — |
| [SRC-1AE03B9EC3-L002391](../../agents/web_agent.py#L2391) | 2391 | `"                        search_started_queries += 1"` | — |
| [SRC-1AE03B9EC3-L002392](../../agents/web_agent.py#L2392) | 2392 | `"                        try:"` | — |
| [SRC-1AE03B9EC3-L002393](../../agents/web_agent.py#L2393) | 2393 | `"                            results = future.result()"` | — |
| [SRC-1AE03B9EC3-L002394](../../agents/web_agent.py#L2394) | 2394 | `"                        except (RequestBudgetExceeded, RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L002395](../../agents/web_agent.py#L2395) | 2395 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L002396](../../agents/web_agent.py#L2396) | 2396 | `"                                f\"تعذر بحث زاوية إضافية «{query[:70]}»: {exc}\""` | — |
| [SRC-1AE03B9EC3-L002397](../../agents/web_agent.py#L2397) | 2397 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L002398](../../agents/web_agent.py#L2398) | 2398 | `"                            query_counts.append({\"query\": query, \"results\": 0})"` | — |
| [SRC-1AE03B9EC3-L002399](../../agents/web_agent.py#L2399) | 2399 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002400](../../agents/web_agent.py#L2400) | 2400 | `"                        query_counts.append({\"query\": query, \"results\": len(results)})"` | — |
| [SRC-1AE03B9EC3-L002401](../../agents/web_agent.py#L2401) | 2401 | `"                        grouped: dict[str, list[dict[str, Any]]] = {}"` | — |
| [SRC-1AE03B9EC3-L002402](../../agents/web_agent.py#L2402) | 2402 | `"                        for source in results:"` | — |
| [SRC-1AE03B9EC3-L002403](../../agents/web_agent.py#L2403) | 2403 | `"                            grouped.setdefault("` | — |
| [SRC-1AE03B9EC3-L002404](../../agents/web_agent.py#L2404) | 2404 | `"                                str(source.get(\"provider\") or \"web_search\"), []"` | — |
| [SRC-1AE03B9EC3-L002405](../../agents/web_agent.py#L2405) | 2405 | `"                            ).append(source)"` | — |
| [SRC-1AE03B9EC3-L002406](../../agents/web_agent.py#L2406) | 2406 | `"                        for provider, items in grouped.items():"` | — |
| [SRC-1AE03B9EC3-L002407](../../agents/web_agent.py#L2407) | 2407 | `"                            items.sort(key=lambda item: int(item.get(\"provider_rank\", 999)))"` | — |
| [SRC-1AE03B9EC3-L002408](../../agents/web_agent.py#L2408) | 2408 | `"                            batches.append({"` | — |
| [SRC-1AE03B9EC3-L002409](../../agents/web_agent.py#L2409) | 2409 | `"                                \"query\": query, \"provider\": provider, \"results\": items"` | — |
| [SRC-1AE03B9EC3-L002410](../../agents/web_agent.py#L2410) | 2410 | `"                            })"` | — |
| [SRC-1AE03B9EC3-L002411](../../agents/web_agent.py#L2411) | 2411 | `"                queries.extend(expansion_queries)"` | — |
| [SRC-1AE03B9EC3-L002412](../../agents/web_agent.py#L2412) | 2412 | `"                plan[\"queries\"] = list(queries)"` | — |
| [SRC-1AE03B9EC3-L002413](../../agents/web_agent.py#L2413) | 2413 | `""` | — |
| [SRC-1AE03B9EC3-L002414](../../agents/web_agent.py#L2414) | 2414 | `"        # Google News RSS is included concurrently by _search_web for freshness-bearing queries."` | — |
| [SRC-1AE03B9EC3-L002415](../../agents/web_agent.py#L2415) | 2415 | `""` | — |
| [SRC-1AE03B9EC3-L002416](../../agents/web_agent.py#L2416) | 2416 | `"        # A social-focused task uses public social endpoints in parallel with indexed"` | — |
| [SRC-1AE03B9EC3-L002417](../../agents/web_agent.py#L2417) | 2417 | `"        # public pages. No login, private profile, session cookie or anti-bot bypass."` | — |
| [SRC-1AE03B9EC3-L002418](../../agents/web_agent.py#L2418) | 2418 | `"        social_results: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L002419](../../agents/web_agent.py#L2419) | 2419 | `"        if plan.get(\"social_focus\") and queries:"` | — |
| [SRC-1AE03B9EC3-L002420](../../agents/web_agent.py#L2420) | 2420 | `"            requested_platforms = plan.get(\"platforms\") or []"` | — |
| [SRC-1AE03B9EC3-L002421](../../agents/web_agent.py#L2421) | 2421 | `"            if requested_platforms:"` | — |
| [SRC-1AE03B9EC3-L002422](../../agents/web_agent.py#L2422) | 2422 | `"                platforms = list(dict.fromkeys(requested_platforms))"` | — |
| [SRC-1AE03B9EC3-L002423](../../agents/web_agent.py#L2423) | 2423 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L002424](../../agents/web_agent.py#L2424) | 2424 | `"                # Broad social research: always try no-key public sources, and add"` | — |
| [SRC-1AE03B9EC3-L002425](../../agents/web_agent.py#L2425) | 2425 | `"                # official platform connectors only when they are configured."` | — |
| [SRC-1AE03B9EC3-L002426](../../agents/web_agent.py#L2426) | 2426 | `"                platforms = [\"reddit\", \"bluesky\"]"` | — |
| [SRC-1AE03B9EC3-L002427](../../agents/web_agent.py#L2427) | 2427 | `"                optional_connectors = {"` | — |
| [SRC-1AE03B9EC3-L002428](../../agents/web_agent.py#L2428) | 2428 | `"                    \"facebook\": bool("` | — |
| [SRC-1AE03B9EC3-L002429](../../agents/web_agent.py#L2429) | 2429 | `"                        os.getenv(\"FACEBOOK_PAGE_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L002430](../../agents/web_agent.py#L2430) | 2430 | `"                        and os.getenv(\"FACEBOOK_PAGE_IDS\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L002431](../../agents/web_agent.py#L2431) | 2431 | `"                    ),"` | — |
| [SRC-1AE03B9EC3-L002432](../../agents/web_agent.py#L2432) | 2432 | `"                    \"instagram\": bool("` | — |
| [SRC-1AE03B9EC3-L002433](../../agents/web_agent.py#L2433) | 2433 | `"                        os.getenv(\"INSTAGRAM_USER_ID\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L002434](../../agents/web_agent.py#L2434) | 2434 | `"                        and os.getenv(\"INSTAGRAM_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L002435](../../agents/web_agent.py#L2435) | 2435 | `"                    ),"` | — |
| [SRC-1AE03B9EC3-L002436](../../agents/web_agent.py#L2436) | 2436 | `"                    \"x\": bool(os.getenv(\"X_BEARER_TOKEN\", \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L002437](../../agents/web_agent.py#L2437) | 2437 | `"                    \"youtube\": bool(os.getenv(\"YOUTUBE_API_KEY\", \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L002438](../../agents/web_agent.py#L2438) | 2438 | `"                }"` | — |
| [SRC-1AE03B9EC3-L002439](../../agents/web_agent.py#L2439) | 2439 | `"                platforms.extend("` | — |
| [SRC-1AE03B9EC3-L002440](../../agents/web_agent.py#L2440) | 2440 | `"                    name for name, ready in optional_connectors.items()"` | — |
| [SRC-1AE03B9EC3-L002441](../../agents/web_agent.py#L2441) | 2441 | `"                    if ready and name not in platforms"` | — |
| [SRC-1AE03B9EC3-L002442](../../agents/web_agent.py#L2442) | 2442 | `"                )"` | — |
| [SRC-1AE03B9EC3-L002443](../../agents/web_agent.py#L2443) | 2443 | `"            social_results, social_warnings = self._search_social((queries[0] if queries else \"\"), platforms)"` | — |
| [SRC-1AE03B9EC3-L002444](../../agents/web_agent.py#L2444) | 2444 | `"            warnings.extend(social_warnings)"` | — |
| [SRC-1AE03B9EC3-L002445](../../agents/web_agent.py#L2445) | 2445 | `"            social_groups: dict[str, list[dict[str, Any]]] = {}"` | — |
| [SRC-1AE03B9EC3-L002446](../../agents/web_agent.py#L2446) | 2446 | `"            for source in social_results:"` | — |
| [SRC-1AE03B9EC3-L002447](../../agents/web_agent.py#L2447) | 2447 | `"                social_groups.setdefault(str(source.get(\"provider\") or \"social\"), []).append(source)"` | — |
| [SRC-1AE03B9EC3-L002448](../../agents/web_agent.py#L2448) | 2448 | `"            for provider, items in social_groups.items():"` | — |
| [SRC-1AE03B9EC3-L002449](../../agents/web_agent.py#L2449) | 2449 | `"                items.sort(key=lambda item: int(item.get(\"provider_rank\", 999)))"` | — |
| [SRC-1AE03B9EC3-L002450](../../agents/web_agent.py#L2450) | 2450 | `"                batches.append({\"query\": (queries[0] if queries else \"\"), \"provider\": provider, \"results\": items})"` | — |
| [SRC-1AE03B9EC3-L002451](../../agents/web_agent.py#L2451) | 2451 | `""` | — |
| [SRC-1AE03B9EC3-L002452](../../agents/web_agent.py#L2452) | 2452 | `"        # Explicit URLs are first-class inputs: fetch the page the user actually asked about"` | — |
| [SRC-1AE03B9EC3-L002453](../../agents/web_agent.py#L2453) | 2453 | `"        # instead of relying on a search engine to rediscover it. URL and DNS checks still apply."` | — |
| [SRC-1AE03B9EC3-L002454](../../agents/web_agent.py#L2454) | 2454 | `"        direct_urls: list[str] = []"` | — |
| [SRC-1AE03B9EC3-L002455](../../agents/web_agent.py#L2455) | 2455 | `"        for value in plan.get(\"direct_urls\", [])[:5]:"` | — |
| [SRC-1AE03B9EC3-L002456](../../agents/web_agent.py#L2456) | 2456 | `"            safe_url = _public_http_url(value)"` | — |
| [SRC-1AE03B9EC3-L002457](../../agents/web_agent.py#L2457) | 2457 | `"            if safe_url and not _blocked_source_url(safe_url) and safe_url not in direct_urls:"` | — |
| [SRC-1AE03B9EC3-L002458](../../agents/web_agent.py#L2458) | 2458 | `"                direct_urls.append(safe_url)"` | — |
| [SRC-1AE03B9EC3-L002459](../../agents/web_agent.py#L2459) | 2459 | `"        for direct_url in direct_urls:"` | — |
| [SRC-1AE03B9EC3-L002460](../../agents/web_agent.py#L2460) | 2460 | `"            batches.append({"` | — |
| [SRC-1AE03B9EC3-L002461](../../agents/web_agent.py#L2461) | 2461 | `"                \"query\": (queries[0] if queries else \"\"),"` | — |
| [SRC-1AE03B9EC3-L002462](../../agents/web_agent.py#L2462) | 2462 | `"                \"provider\": \"user_supplied_url\","` | — |
| [SRC-1AE03B9EC3-L002463](../../agents/web_agent.py#L2463) | 2463 | `"                \"results\": [{"` | — |
| [SRC-1AE03B9EC3-L002464](../../agents/web_agent.py#L2464) | 2464 | `"                    \"title\": \"رابط قدمه المستخدم للتحليل\","` | — |
| [SRC-1AE03B9EC3-L002465](../../agents/web_agent.py#L2465) | 2465 | `"                    \"url\": direct_url,"` | — |
| [SRC-1AE03B9EC3-L002466](../../agents/web_agent.py#L2466) | 2466 | `"                    \"snippet\": \"\","` | — |
| [SRC-1AE03B9EC3-L002467](../../agents/web_agent.py#L2467) | 2467 | `"                    \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L002468](../../agents/web_agent.py#L2468) | 2468 | `"                    \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L002469](../../agents/web_agent.py#L2469) | 2469 | `"                    \"provider\": \"user_supplied_url\","` | — |
| [SRC-1AE03B9EC3-L002470](../../agents/web_agent.py#L2470) | 2470 | `"                    \"provider_rank\": 1,"` | — |
| [SRC-1AE03B9EC3-L002471](../../agents/web_agent.py#L2471) | 2471 | `"                    \"search_query\": (queries[0] if queries else \"\"),"` | — |
| [SRC-1AE03B9EC3-L002472](../../agents/web_agent.py#L2472) | 2472 | `"                    \"published_at\": \"\","` | — |
| [SRC-1AE03B9EC3-L002473](../../agents/web_agent.py#L2473) | 2473 | `"                }],"` | — |
| [SRC-1AE03B9EC3-L002474](../../agents/web_agent.py#L2474) | 2474 | `"            })"` | — |
| [SRC-1AE03B9EC3-L002475](../../agents/web_agent.py#L2475) | 2475 | `""` | — |
| [SRC-1AE03B9EC3-L002476](../../agents/web_agent.py#L2476) | 2476 | `"        raw_results_count = sum(len(batch.get(\"results\", [])) for batch in batches if isinstance(batch, dict) and isinstance(batch.get(\"results\", []), list))"` | — |
| [SRC-1AE03B9EC3-L002477](../../agents/web_agent.py#L2477) | 2477 | `"        sources = fuse_ranked_results(batches, limit=MAX_SEARCH_RESULTS)"` | — |
| [SRC-1AE03B9EC3-L002478](../../agents/web_agent.py#L2478) | 2478 | `"        for source in sources:"` | — |
| [SRC-1AE03B9EC3-L002479](../../agents/web_agent.py#L2479) | 2479 | `"            source.setdefault(\"page_fetch_status\", \"not_attempted\")"` | — |
| [SRC-1AE03B9EC3-L002480](../../agents/web_agent.py#L2480) | 2480 | `"        # Fetch page text only for the best few public URLs; do it concurrently with strict bounds."` | — |
| [SRC-1AE03B9EC3-L002481](../../agents/web_agent.py#L2481) | 2481 | `"        fetch_targets = sources[:MAX_FETCHED_PAGES]"` | — |
| [SRC-1AE03B9EC3-L002482](../../agents/web_agent.py#L2482) | 2482 | `"        for source in fetch_targets:"` | — |
| [SRC-1AE03B9EC3-L002483](../../agents/web_agent.py#L2483) | 2483 | `"            source[\"page_fetch_status\"] = \"attempted\""` | — |
| [SRC-1AE03B9EC3-L002484](../../agents/web_agent.py#L2484) | 2484 | `"        fetched_count = 0"` | — |
| [SRC-1AE03B9EC3-L002485](../../agents/web_agent.py#L2485) | 2485 | `"        if fetch_targets:"` | — |
| [SRC-1AE03B9EC3-L002486](../../agents/web_agent.py#L2486) | 2486 | `"            with ThreadPoolExecutor(max_workers=min(4, len(fetch_targets))) as pool:"` | — |
| [SRC-1AE03B9EC3-L002487](../../agents/web_agent.py#L2487) | 2487 | `"                futures = {"` | — |
| [SRC-1AE03B9EC3-L002488](../../agents/web_agent.py#L2488) | 2488 | `"                    pool.submit(self._fetch_page, source[\"url\"]): source"` | — |
| [SRC-1AE03B9EC3-L002489](../../agents/web_agent.py#L2489) | 2489 | `"                    for source in fetch_targets"` | — |
| [SRC-1AE03B9EC3-L002490](../../agents/web_agent.py#L2490) | 2490 | `"                }"` | — |
| [SRC-1AE03B9EC3-L002491](../../agents/web_agent.py#L2491) | 2491 | `"                for future in as_completed(futures):"` | — |
| [SRC-1AE03B9EC3-L002492](../../agents/web_agent.py#L2492) | 2492 | `"                    source = futures[future]"` | — |
| [SRC-1AE03B9EC3-L002493](../../agents/web_agent.py#L2493) | 2493 | `"                    try:"` | — |
| [SRC-1AE03B9EC3-L002494](../../agents/web_agent.py#L2494) | 2494 | `"                        fetch_result = future.result()"` | — |
| [SRC-1AE03B9EC3-L002495](../../agents/web_agent.py#L2495) | 2495 | `"                    except RequestBudgetExceeded as exc:"` | — |
| [SRC-1AE03B9EC3-L002496](../../agents/web_agent.py#L2496) | 2496 | `"                        source[\"page_fetch_status\"] = \"budget_exhausted\""` | — |
| [SRC-1AE03B9EC3-L002497](../../agents/web_agent.py#L2497) | 2497 | `"                        source[\"page_fetch_error_class\"] = type(exc).__name__"` | — |
| [SRC-1AE03B9EC3-L002498](../../agents/web_agent.py#L2498) | 2498 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L002499](../../agents/web_agent.py#L2499) | 2499 | `"                    except (RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L002500](../../agents/web_agent.py#L2500) | 2500 | `"                        source[\"page_fetch_status\"] = \"fetch_failed\""` | — |
| [SRC-1AE03B9EC3-L002501](../../agents/web_agent.py#L2501) | 2501 | `"                        source[\"page_fetch_error_class\"] = type(exc).__name__"` | — |
| [SRC-1AE03B9EC3-L002502](../../agents/web_agent.py#L2502) | 2502 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L002503](../../agents/web_agent.py#L2503) | 2503 | `"                    title, page_text = fetch_result"` | — |
| [SRC-1AE03B9EC3-L002504](../../agents/web_agent.py#L2504) | 2504 | `"                    observed_status = getattr(fetch_result, \"status\", None)"` | — |
| [SRC-1AE03B9EC3-L002505](../../agents/web_agent.py#L2505) | 2505 | `"                    error_class = getattr(fetch_result, \"error_class\", None)"` | — |
| [SRC-1AE03B9EC3-L002506](../../agents/web_agent.py#L2506) | 2506 | `"                    if title:"` | — |
| [SRC-1AE03B9EC3-L002507](../../agents/web_agent.py#L2507) | 2507 | `"                        source[\"title\"] = title"` | — |
| [SRC-1AE03B9EC3-L002508](../../agents/web_agent.py#L2508) | 2508 | `"                    if page_text and page_text.strip():"` | — |
| [SRC-1AE03B9EC3-L002509](../../agents/web_agent.py#L2509) | 2509 | `"                        source[\"page_text\"] = page_text"` | — |
| [SRC-1AE03B9EC3-L002510](../../agents/web_agent.py#L2510) | 2510 | `"                        source[\"snippet\"] = page_text[:1800]"` | — |
| [SRC-1AE03B9EC3-L002511](../../agents/web_agent.py#L2511) | 2511 | `"                        source[\"page_fetched\"] = True"` | — |
| [SRC-1AE03B9EC3-L002512](../../agents/web_agent.py#L2512) | 2512 | `"                        source[\"page_fetch_status\"] = ("` | — |
| [SRC-1AE03B9EC3-L002513](../../agents/web_agent.py#L2513) | 2513 | `"                            observed_status"` | — |
| [SRC-1AE03B9EC3-L002514](../../agents/web_agent.py#L2514) | 2514 | `"                            if observed_status in {\"content_extracted\", \"partial_extraction\"}"` | — |
| [SRC-1AE03B9EC3-L002515](../../agents/web_agent.py#L2515) | 2515 | `"                            else \"partial_extraction\""` | — |
| [SRC-1AE03B9EC3-L002516](../../agents/web_agent.py#L2516) | 2516 | `"                            if len(page_text) >= MAX_PAGE_TEXT_CHARS"` | — |
| [SRC-1AE03B9EC3-L002517](../../agents/web_agent.py#L2517) | 2517 | `"                            else \"content_extracted\""` | — |
| [SRC-1AE03B9EC3-L002518](../../agents/web_agent.py#L2518) | 2518 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L002519](../../agents/web_agent.py#L2519) | 2519 | `"                        if error_class:"` | — |
| [SRC-1AE03B9EC3-L002520](../../agents/web_agent.py#L2520) | 2520 | `"                            source[\"page_fetch_error_class\"] = str(error_class)[:80]"` | — |
| [SRC-1AE03B9EC3-L002521](../../agents/web_agent.py#L2521) | 2521 | `"                        else:"` | — |
| [SRC-1AE03B9EC3-L002522](../../agents/web_agent.py#L2522) | 2522 | `"                            source.pop(\"page_fetch_error_class\", None)"` | — |
| [SRC-1AE03B9EC3-L002523](../../agents/web_agent.py#L2523) | 2523 | `"                        fetched_count += 1"` | — |
| [SRC-1AE03B9EC3-L002524](../../agents/web_agent.py#L2524) | 2524 | `"                        if source[\"page_fetch_status\"] == \"partial_extraction\":"` | — |
| [SRC-1AE03B9EC3-L002525](../../agents/web_agent.py#L2525) | 2525 | `"                            host = urllib.parse.urlparse(source.get(\"url\", \"\")).hostname or \"المصدر\""` | — |
| [SRC-1AE03B9EC3-L002526](../../agents/web_agent.py#L2526) | 2526 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L002527](../../agents/web_agent.py#L2527) | 2527 | `"                                f\"استُخرج جزء من نص {host} فقط؛ قد تكون الصفحة أطول من الحد الآمن.\""` | — |
| [SRC-1AE03B9EC3-L002528](../../agents/web_agent.py#L2528) | 2528 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L002529](../../agents/web_agent.py#L2529) | 2529 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L002530](../../agents/web_agent.py#L2530) | 2530 | `"                        source[\"page_fetched\"] = False"` | — |
| [SRC-1AE03B9EC3-L002531](../../agents/web_agent.py#L2531) | 2531 | `"                        if observed_status in {"` | — |
| [SRC-1AE03B9EC3-L002532](../../agents/web_agent.py#L2532) | 2532 | `"                            \"rejected_url\", \"blocked_or_unresolved_host\", \"blocked_connection_target\","` | — |
| [SRC-1AE03B9EC3-L002533](../../agents/web_agent.py#L2533) | 2533 | `"                            \"redirect_failed\", \"redirect_rejected\", \"redirect_limit\", \"http_error\","` | — |
| [SRC-1AE03B9EC3-L002534](../../agents/web_agent.py#L2534) | 2534 | `"                            \"unsupported_content_type\", \"page_too_large\", \"network_error\","` | — |
| [SRC-1AE03B9EC3-L002535](../../agents/web_agent.py#L2535) | 2535 | `"                            \"empty_content\", \"no_text_extracted\", \"budget_exhausted\","` | — |
| [SRC-1AE03B9EC3-L002536](../../agents/web_agent.py#L2536) | 2536 | `"                        }:"` | — |
| [SRC-1AE03B9EC3-L002537](../../agents/web_agent.py#L2537) | 2537 | `"                            source[\"page_fetch_status\"] = observed_status"` | — |
| [SRC-1AE03B9EC3-L002538](../../agents/web_agent.py#L2538) | 2538 | `"                        else:"` | — |
| [SRC-1AE03B9EC3-L002539](../../agents/web_agent.py#L2539) | 2539 | `"                            source[\"page_fetch_status\"] = \"no_text_extracted\""` | — |
| [SRC-1AE03B9EC3-L002540](../../agents/web_agent.py#L2540) | 2540 | `"                        if error_class:"` | — |
| [SRC-1AE03B9EC3-L002541](../../agents/web_agent.py#L2541) | 2541 | `"                            source[\"page_fetch_error_class\"] = str(error_class)[:80]"` | — |
| [SRC-1AE03B9EC3-L002542](../../agents/web_agent.py#L2542) | 2542 | `"                        host = urllib.parse.urlparse(source.get(\"url\", \"\")).hostname or \"المصدر\""` | — |
| [SRC-1AE03B9EC3-L002543](../../agents/web_agent.py#L2543) | 2543 | `"                        if source[\"page_fetch_status\"] in {\"no_text_extracted\", \"empty_content\"}:"` | — |
| [SRC-1AE03B9EC3-L002544](../../agents/web_agent.py#L2544) | 2544 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L002545](../../agents/web_agent.py#L2545) | 2545 | `"                                f\"لم يمكن استخراج نص من {host}؛ جُلبت الصفحة أو جرت محاولة قراءتها لكن قد تكون ديناميكية أو محجوبة.\""` | — |
| [SRC-1AE03B9EC3-L002546](../../agents/web_agent.py#L2546) | 2546 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L002547](../../agents/web_agent.py#L2547) | 2547 | `"                        else:"` | — |
| [SRC-1AE03B9EC3-L002548](../../agents/web_agent.py#L2548) | 2548 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L002549](../../agents/web_agent.py#L2549) | 2549 | `"                                f\"تعذرت قراءة نص {host} بسبب حالة الجلب: {source['page_fetch_status']}.\""` | — |
| [SRC-1AE03B9EC3-L002550](../../agents/web_agent.py#L2550) | 2550 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L002551](../../agents/web_agent.py#L2551) | 2551 | `""` | — |
| [SRC-1AE03B9EC3-L002552](../../agents/web_agent.py#L2552) | 2552 | `"        # Reorder on consensus first, and keep clear machine-readable provenance."` | — |
| [SRC-1AE03B9EC3-L002553](../../agents/web_agent.py#L2553) | 2553 | `"        sources.sort(key=lambda source: source.get(\"rank_score\", 0), reverse=True)"` | — |
| [SRC-1AE03B9EC3-L002554](../../agents/web_agent.py#L2554) | 2554 | `"        providers = sorted({"` | — |
| [SRC-1AE03B9EC3-L002555](../../agents/web_agent.py#L2555) | 2555 | `"            provider"` | — |
| [SRC-1AE03B9EC3-L002556](../../agents/web_agent.py#L2556) | 2556 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L002557](../../agents/web_agent.py#L2557) | 2557 | `"            for provider in source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L002558](../../agents/web_agent.py#L2558) | 2558 | `"        })"` | — |
| [SRC-1AE03B9EC3-L002559](../../agents/web_agent.py#L2559) | 2559 | `"        platform_counts: dict[str, int] = {}"` | — |
| [SRC-1AE03B9EC3-L002560](../../agents/web_agent.py#L2560) | 2560 | `"        for source in sources:"` | — |
| [SRC-1AE03B9EC3-L002561](../../agents/web_agent.py#L2561) | 2561 | `"            label = source.get(\"platform\", \"web\")"` | — |
| [SRC-1AE03B9EC3-L002562](../../agents/web_agent.py#L2562) | 2562 | `"            platform_counts[label] = platform_counts.get(label, 0) + 1"` | — |
| [SRC-1AE03B9EC3-L002563](../../agents/web_agent.py#L2563) | 2563 | `"        page_failure_statuses = {"` | — |
| [SRC-1AE03B9EC3-L002564](../../agents/web_agent.py#L2564) | 2564 | `"            \"fetch_failed\", \"no_text_extracted\", \"rejected_url\","` | — |
| [SRC-1AE03B9EC3-L002565](../../agents/web_agent.py#L2565) | 2565 | `"            \"blocked_or_unresolved_host\", \"blocked_connection_target\","` | — |
| [SRC-1AE03B9EC3-L002566](../../agents/web_agent.py#L2566) | 2566 | `"            \"redirect_failed\", \"redirect_rejected\", \"redirect_limit\","` | — |
| [SRC-1AE03B9EC3-L002567](../../agents/web_agent.py#L2567) | 2567 | `"            \"http_error\", \"unsupported_content_type\", \"page_too_large\","` | — |
| [SRC-1AE03B9EC3-L002568](../../agents/web_agent.py#L2568) | 2568 | `"            \"network_error\", \"empty_content\", \"budget_exhausted\","` | — |
| [SRC-1AE03B9EC3-L002569](../../agents/web_agent.py#L2569) | 2569 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002570](../../agents/web_agent.py#L2570) | 2570 | `"        page_status_values = ("` | — |
| [SRC-1AE03B9EC3-L002571](../../agents/web_agent.py#L2571) | 2571 | `"            \"not_attempted\", \"attempted\", \"content_extracted\", \"partial_extraction\","` | — |
| [SRC-1AE03B9EC3-L002572](../../agents/web_agent.py#L2572) | 2572 | `"            \"no_text_extracted\", \"fetch_failed\", \"rejected_url\","` | — |
| [SRC-1AE03B9EC3-L002573](../../agents/web_agent.py#L2573) | 2573 | `"            \"blocked_or_unresolved_host\", \"blocked_connection_target\","` | — |
| [SRC-1AE03B9EC3-L002574](../../agents/web_agent.py#L2574) | 2574 | `"            \"redirect_failed\", \"redirect_rejected\", \"redirect_limit\","` | — |
| [SRC-1AE03B9EC3-L002575](../../agents/web_agent.py#L2575) | 2575 | `"            \"http_error\", \"unsupported_content_type\", \"page_too_large\","` | — |
| [SRC-1AE03B9EC3-L002576](../../agents/web_agent.py#L2576) | 2576 | `"            \"network_error\", \"empty_content\", \"budget_exhausted\","` | — |
| [SRC-1AE03B9EC3-L002577](../../agents/web_agent.py#L2577) | 2577 | `"        )"` | — |
| [SRC-1AE03B9EC3-L002578](../../agents/web_agent.py#L2578) | 2578 | `"        page_fetch_status_counts = {"` | — |
| [SRC-1AE03B9EC3-L002579](../../agents/web_agent.py#L2579) | 2579 | `"            status: sum(source.get(\"page_fetch_status\") == status for source in fetch_targets)"` | — |
| [SRC-1AE03B9EC3-L002580](../../agents/web_agent.py#L2580) | 2580 | `"            for status in page_status_values"` | — |
| [SRC-1AE03B9EC3-L002581](../../agents/web_agent.py#L2581) | 2581 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002582](../../agents/web_agent.py#L2582) | 2582 | `"        provider_diagnostics = list(self._provider_diagnostics)"` | — |
| [SRC-1AE03B9EC3-L002583](../../agents/web_agent.py#L2583) | 2583 | `"        provider_candidates_received = sum("` | — |
| [SRC-1AE03B9EC3-L002584](../../agents/web_agent.py#L2584) | 2584 | `"            max(0, int(row.get(\"result_count\", 0) or 0))"` | — |
| [SRC-1AE03B9EC3-L002585](../../agents/web_agent.py#L2585) | 2585 | `"            for row in provider_diagnostics if isinstance(row, dict)"` | — |
| [SRC-1AE03B9EC3-L002586](../../agents/web_agent.py#L2586) | 2586 | `"        )"` | — |
| [SRC-1AE03B9EC3-L002587](../../agents/web_agent.py#L2587) | 2587 | `"        provider_candidates_accepted = sum("` | — |
| [SRC-1AE03B9EC3-L002588](../../agents/web_agent.py#L2588) | 2588 | `"            max(0, int(row.get(\"accepted_count\", 0) or 0))"` | — |
| [SRC-1AE03B9EC3-L002589](../../agents/web_agent.py#L2589) | 2589 | `"            for row in provider_diagnostics if isinstance(row, dict)"` | — |
| [SRC-1AE03B9EC3-L002590](../../agents/web_agent.py#L2590) | 2590 | `"        )"` | — |
| [SRC-1AE03B9EC3-L002591](../../agents/web_agent.py#L2591) | 2591 | `"        provider_candidates_rejected = sum("` | — |
| [SRC-1AE03B9EC3-L002592](../../agents/web_agent.py#L2592) | 2592 | `"            max(0, int(row.get(\"rejected_count\", 0) or 0))"` | — |
| [SRC-1AE03B9EC3-L002593](../../agents/web_agent.py#L2593) | 2593 | `"            for row in provider_diagnostics if isinstance(row, dict)"` | — |
| [SRC-1AE03B9EC3-L002594](../../agents/web_agent.py#L2594) | 2594 | `"        )"` | — |
| [SRC-1AE03B9EC3-L002595](../../agents/web_agent.py#L2595) | 2595 | `"        report = {"` | — |
| [SRC-1AE03B9EC3-L002596](../../agents/web_agent.py#L2596) | 2596 | `"            \"raw_results\": raw_results_count,"` | — |
| [SRC-1AE03B9EC3-L002597](../../agents/web_agent.py#L2597) | 2597 | `"            \"provider_candidates_received\": provider_candidates_received,"` | — |
| [SRC-1AE03B9EC3-L002598](../../agents/web_agent.py#L2598) | 2598 | `"            \"provider_candidates_accepted\": provider_candidates_accepted,"` | — |
| [SRC-1AE03B9EC3-L002599](../../agents/web_agent.py#L2599) | 2599 | `"            \"provider_candidates_rejected\": provider_candidates_rejected,"` | — |
| [SRC-1AE03B9EC3-L002600](../../agents/web_agent.py#L2600) | 2600 | `"            \"unique_urls\": len({"` | — |
| [SRC-1AE03B9EC3-L002601](../../agents/web_agent.py#L2601) | 2601 | `"                self._normalized_source_url_key(source.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L002602](../../agents/web_agent.py#L2602) | 2602 | `"                for source in sources"` | — |
| [SRC-1AE03B9EC3-L002603](../../agents/web_agent.py#L2603) | 2603 | `"                if self._normalized_source_url_key(source.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L002604](../../agents/web_agent.py#L2604) | 2604 | `"            }),"` | — |
| [SRC-1AE03B9EC3-L002605](../../agents/web_agent.py#L2605) | 2605 | `"            \"pages_content_extracted\": fetched_count,"` | — |
| [SRC-1AE03B9EC3-L002606](../../agents/web_agent.py#L2606) | 2606 | `"            \"pages_partial_extracted\": sum("` | — |
| [SRC-1AE03B9EC3-L002607](../../agents/web_agent.py#L2607) | 2607 | `"                source.get(\"page_fetch_status\") == \"partial_extraction\""` | — |
| [SRC-1AE03B9EC3-L002608](../../agents/web_agent.py#L2608) | 2608 | `"                for source in fetch_targets"` | — |
| [SRC-1AE03B9EC3-L002609](../../agents/web_agent.py#L2609) | 2609 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L002610](../../agents/web_agent.py#L2610) | 2610 | `"            \"pages_extract_failed\": sum("` | — |
| [SRC-1AE03B9EC3-L002611](../../agents/web_agent.py#L2611) | 2611 | `"                source.get(\"page_fetch_status\") in page_failure_statuses"` | — |
| [SRC-1AE03B9EC3-L002612](../../agents/web_agent.py#L2612) | 2612 | `"                for source in fetch_targets"` | — |
| [SRC-1AE03B9EC3-L002613](../../agents/web_agent.py#L2613) | 2613 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L002614](../../agents/web_agent.py#L2614) | 2614 | `"            \"page_fetch_status_counts\": page_fetch_status_counts,"` | — |
| [SRC-1AE03B9EC3-L002615](../../agents/web_agent.py#L2615) | 2615 | `"            \"queries_planned\": len(queries),"` | — |
| [SRC-1AE03B9EC3-L002616](../../agents/web_agent.py#L2616) | 2616 | `"            \"queries_attempted\": search_started_queries,"` | — |
| [SRC-1AE03B9EC3-L002617](../../agents/web_agent.py#L2617) | 2617 | `"            \"query_results\": query_counts,"` | — |
| [SRC-1AE03B9EC3-L002618](../../agents/web_agent.py#L2618) | 2618 | `"            \"unique_sources\": len(sources),"` | — |
| [SRC-1AE03B9EC3-L002619](../../agents/web_agent.py#L2619) | 2619 | `"            \"pages_fetched\": fetched_count,"` | — |
| [SRC-1AE03B9EC3-L002620](../../agents/web_agent.py#L2620) | 2620 | `"            \"providers_used\": providers,"` | — |
| [SRC-1AE03B9EC3-L002621](../../agents/web_agent.py#L2621) | 2621 | `"            \"provider_counts\": {"` | — |
| [SRC-1AE03B9EC3-L002622](../../agents/web_agent.py#L2622) | 2622 | `"                provider: sum(provider in source.get(\"providers\", []) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L002623](../../agents/web_agent.py#L2623) | 2623 | `"                for provider in providers"` | — |
| [SRC-1AE03B9EC3-L002624](../../agents/web_agent.py#L2624) | 2624 | `"            },"` | — |
| [SRC-1AE03B9EC3-L002625](../../agents/web_agent.py#L2625) | 2625 | `"            \"platform_counts\": platform_counts,"` | — |
| [SRC-1AE03B9EC3-L002626](../../agents/web_agent.py#L2626) | 2626 | `"            \"social_direct_results\": len(social_results),"` | — |
| [SRC-1AE03B9EC3-L002627](../../agents/web_agent.py#L2627) | 2627 | `"            \"expansion_queries\": expansion_queries,"` | — |
| [SRC-1AE03B9EC3-L002628](../../agents/web_agent.py#L2628) | 2628 | `"            \"evidence_signals\": evidence_signal_report(sources, plan.get(\"freshness\", \"any\")),"` | — |
| [SRC-1AE03B9EC3-L002629](../../agents/web_agent.py#L2629) | 2629 | `"            \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L002630](../../agents/web_agent.py#L2630) | 2630 | `"            \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L002631](../../agents/web_agent.py#L2631) | 2631 | `"            \"dialogue_context\": plan.get(\"dialogue_context\", {}),"` | — |
| [SRC-1AE03B9EC3-L002632](../../agents/web_agent.py#L2632) | 2632 | `"            \"provider_diagnostics\": provider_diagnostics,"` | — |
| [SRC-1AE03B9EC3-L002633](../../agents/web_agent.py#L2633) | 2633 | `"            \"connector_summary\": self._connector_status_summary("` | — |
| [SRC-1AE03B9EC3-L002634](../../agents/web_agent.py#L2634) | 2634 | `"                provider_diagnostics, sources"` | — |
| [SRC-1AE03B9EC3-L002635](../../agents/web_agent.py#L2635) | 2635 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L002636](../../agents/web_agent.py#L2636) | 2636 | `"            \"pages_fetch_attempted\": len(fetch_targets),"` | — |
| [SRC-1AE03B9EC3-L002637](../../agents/web_agent.py#L2637) | 2637 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002638](../../agents/web_agent.py#L2638) | 2638 | `"        return sources, list(dict.fromkeys(warnings)), report"` | — |
| [SRC-1AE03B9EC3-L002639](../../agents/web_agent.py#L2639) | 2639 | `""` | — |
| [SRC-1AE03B9EC3-L002640](../../agents/web_agent.py#L2640) | 2640 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L002641](../../agents/web_agent.py#L2641) | 2641 | `"    def _history_search_query(question: str, history: list[dict[str, str]]) -> str:"` | — |
| [SRC-1AE03B9EC3-L002642](../../agents/web_agent.py#L2642) | 2642 | `"        \"\"\"Backward-compatible wrapper for the shared follow-up resolver.\"\"\""` | — |
| [SRC-1AE03B9EC3-L002643](../../agents/web_agent.py#L2643) | 2643 | `"        return resolve_followup_query(question, history)"` | — |
| [SRC-1AE03B9EC3-L002644](../../agents/web_agent.py#L2644) | 2644 | `""` | — |
| [SRC-1AE03B9EC3-L002645](../../agents/web_agent.py#L2645) | 2645 | `"    def _connector_status_summary(self, diagnostics: list[dict[str, Any]] \| None,"` | — |
| [SRC-1AE03B9EC3-L002646](../../agents/web_agent.py#L2646) | 2646 | `"                                  sources: list[dict[str, Any]] \| None = None) -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L002647](../../agents/web_agent.py#L2647) | 2647 | `"        \"\"\"Summarize this request's connector states without exposing credentials.\"\"\""` | — |
| [SRC-1AE03B9EC3-L002648](../../agents/web_agent.py#L2648) | 2648 | `"        optional = {"` | — |
| [SRC-1AE03B9EC3-L002649](../../agents/web_agent.py#L2649) | 2649 | `"            \"deepseek_search_api\": (\"DEEPSEEK_SEARCH_API_KEY\",), \"brave_search_api\": (\"BRAVE_SEARCH_API_KEY\",),"` | — |
| [SRC-1AE03B9EC3-L002650](../../agents/web_agent.py#L2650) | 2650 | `"            \"tavily_search_api\": (\"TAVILY_API_KEY\",), \"reddit_oauth_api\": (\"REDDIT_CLIENT_ID\", \"REDDIT_CLIENT_SECRET\"),"` | — |
| [SRC-1AE03B9EC3-L002651](../../agents/web_agent.py#L2651) | 2651 | `"            \"facebook_pages_api\": (\"FACEBOOK_PAGE_ACCESS_TOKEN\", \"FACEBOOK_PAGE_IDS\"),"` | — |
| [SRC-1AE03B9EC3-L002652](../../agents/web_agent.py#L2652) | 2652 | `"            \"instagram_graph_api\": (\"INSTAGRAM_USER_ID\", \"INSTAGRAM_ACCESS_TOKEN\"),"` | — |
| [SRC-1AE03B9EC3-L002653](../../agents/web_agent.py#L2653) | 2653 | `"            \"x_official_api\": (\"X_BEARER_TOKEN\",), \"youtube_data_api\": (\"YOUTUBE_API_KEY\",),"` | — |
| [SRC-1AE03B9EC3-L002654](../../agents/web_agent.py#L2654) | 2654 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002655](../../agents/web_agent.py#L2655) | 2655 | `"        config: dict[str, tuple[bool, str]] = {"` | — |
| [SRC-1AE03B9EC3-L002656](../../agents/web_agent.py#L2656) | 2656 | `"            \"duckduckgo_html\": (True, \"built_in_no_api_key\"), \"bing_rss\": (True, \"built_in_no_api_key\"),"` | — |
| [SRC-1AE03B9EC3-L002657](../../agents/web_agent.py#L2657) | 2657 | `"            \"google_news_rss\": (True, \"built_in_conditional_no_api_key\"),"` | — |
| [SRC-1AE03B9EC3-L002658](../../agents/web_agent.py#L2658) | 2658 | `"            \"reddit_public_rss\": (True, \"built_in_no_api_key\"), \"bluesky_public_search\": (True, \"built_in_no_api_key\"),"` | — |
| [SRC-1AE03B9EC3-L002659](../../agents/web_agent.py#L2659) | 2659 | `"            \"openrouter_web_search\": (bool(self.openrouter_web_search_enabled),"` | — |
| [SRC-1AE03B9EC3-L002660](../../agents/web_agent.py#L2660) | 2660 | `"                \"enabled\" if self.openrouter_web_search_enabled else \"disabled\"),"` | — |
| [SRC-1AE03B9EC3-L002661](../../agents/web_agent.py#L2661) | 2661 | `"            \"user_supplied_url\": (True, \"request_driven\"),"` | — |
| [SRC-1AE03B9EC3-L002662](../../agents/web_agent.py#L2662) | 2662 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002663](../../agents/web_agent.py#L2663) | 2663 | `"        for name, keys in optional.items():"` | — |
| [SRC-1AE03B9EC3-L002664](../../agents/web_agent.py#L2664) | 2664 | `"            ready = all(bool(os.getenv(key, \"\").strip()) for key in keys)"` | — |
| [SRC-1AE03B9EC3-L002665](../../agents/web_agent.py#L2665) | 2665 | `"            config[name] = (ready, \"configured\" if ready else \"not_configured\")"` | — |
| [SRC-1AE03B9EC3-L002666](../../agents/web_agent.py#L2666) | 2666 | `"        grouped: dict[str, list[dict[str, Any]]] = {}"` | — |
| [SRC-1AE03B9EC3-L002667](../../agents/web_agent.py#L2667) | 2667 | `"        for item in diagnostics or []:"` | — |
| [SRC-1AE03B9EC3-L002668](../../agents/web_agent.py#L2668) | 2668 | `"            if isinstance(item, dict):"` | — |
| [SRC-1AE03B9EC3-L002669](../../agents/web_agent.py#L2669) | 2669 | `"                name = _clean_text(item.get(\"provider\", \"unknown\"), 80) or \"unknown\""` | — |
| [SRC-1AE03B9EC3-L002670](../../agents/web_agent.py#L2670) | 2670 | `"                grouped.setdefault(name, []).append(item)"` | — |
| [SRC-1AE03B9EC3-L002671](../../agents/web_agent.py#L2671) | 2671 | `"        useful: dict[str, int] = {}"` | — |
| [SRC-1AE03B9EC3-L002672](../../agents/web_agent.py#L2672) | 2672 | `"        for source in sources or []:"` | — |
| [SRC-1AE03B9EC3-L002673](../../agents/web_agent.py#L2673) | 2673 | `"            if not isinstance(source, dict):"` | — |
| [SRC-1AE03B9EC3-L002674](../../agents/web_agent.py#L2674) | 2674 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L002675](../../agents/web_agent.py#L2675) | 2675 | `"            providers = source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L002676](../../agents/web_agent.py#L2676) | 2676 | `"            if isinstance(providers, str):"` | — |
| [SRC-1AE03B9EC3-L002677](../../agents/web_agent.py#L2677) | 2677 | `"                providers = [providers]"` | — |
| [SRC-1AE03B9EC3-L002678](../../agents/web_agent.py#L2678) | 2678 | `"            if not isinstance(providers, list):"` | — |
| [SRC-1AE03B9EC3-L002679](../../agents/web_agent.py#L2679) | 2679 | `"                providers = []"` | — |
| [SRC-1AE03B9EC3-L002680](../../agents/web_agent.py#L2680) | 2680 | `"            if isinstance(source.get(\"provider\"), str):"` | — |
| [SRC-1AE03B9EC3-L002681](../../agents/web_agent.py#L2681) | 2681 | `"                providers = providers + [source[\"provider\"]]"` | — |
| [SRC-1AE03B9EC3-L002682](../../agents/web_agent.py#L2682) | 2682 | `"            for name in {str(value) for value in providers if value}:"` | — |
| [SRC-1AE03B9EC3-L002683](../../agents/web_agent.py#L2683) | 2683 | `"                useful[name] = useful.get(name, 0) + 1"` | — |
| [SRC-1AE03B9EC3-L002684](../../agents/web_agent.py#L2684) | 2684 | `"        priority = {\"ok\": 0, \"no_results\": 1, \"filtered_all\": 2, \"not_attempted\": 3,"` | — |
| [SRC-1AE03B9EC3-L002685](../../agents/web_agent.py#L2685) | 2685 | `"                    \"disabled\": 4, \"not_configured\": 5, \"budget_exhausted\": 6,"` | — |
| [SRC-1AE03B9EC3-L002686](../../agents/web_agent.py#L2686) | 2686 | `"                    \"unknown\": 6, \"rate_limited\": 7, \"unauthorized\": 8, \"http_error\": 9,"` | — |
| [SRC-1AE03B9EC3-L002687](../../agents/web_agent.py#L2687) | 2687 | `"                    \"timeout\": 10, \"failed\": 11, \"error\": 11}"` | — |
| [SRC-1AE03B9EC3-L002688](../../agents/web_agent.py#L2688) | 2688 | `"        confirmed_attempt_statuses = _SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES \| {"` | — |
| [SRC-1AE03B9EC3-L002689](../../agents/web_agent.py#L2689) | 2689 | `"            \"http_error\", \"unauthorized\", \"rate_limited\", \"invalid_response\""` | — |
| [SRC-1AE03B9EC3-L002690](../../agents/web_agent.py#L2690) | 2690 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002691](../../agents/web_agent.py#L2691) | 2691 | `"        uncertain_attempt_statuses = {\"timeout\", \"failed\", \"error\", \"unknown\", \"inconclusive\"}"` | — |
| [SRC-1AE03B9EC3-L002692](../../agents/web_agent.py#L2692) | 2692 | `""` | — |
| [SRC-1AE03B9EC3-L002693](../../agents/web_agent.py#L2693) | 2693 | `"        def redact(value: Any) -> str:"` | — |
| [SRC-1AE03B9EC3-L002694](../../agents/web_agent.py#L2694) | 2694 | `"            safe = _clean_text(str(value or \"\"), 180)"` | — |
| [SRC-1AE03B9EC3-L002695](../../agents/web_agent.py#L2695) | 2695 | `"            safe = re.sub(r\"(?i)(bearer\\s+)[A-Za-z0-9._~+/-]+=*\", r\"\\1[REDACTED]\", safe)"` | — |
| [SRC-1AE03B9EC3-L002696](../../agents/web_agent.py#L2696) | 2696 | `"            safe = re.sub(r\"(?i)\\b(api[_-]?key\|access[_-]?token\|refresh[_-]?token\|token\|secret\|password)\\s*[:=]\\s*[^\\s,;]+\", r\"\\1=[REDACTED]\", safe)"` | — |
| [SRC-1AE03B9EC3-L002697](../../agents/web_agent.py#L2697) | 2697 | `"            safe = re.sub(r\"(?i)([?&](?:api[_-]?key\|access[_-]?token\|token\|key)=)[^&\\s]+\", r\"\\1[REDACTED]\", safe)"` | — |
| [SRC-1AE03B9EC3-L002698](../../agents/web_agent.py#L2698) | 2698 | `"            return safe[:180]"` | — |
| [SRC-1AE03B9EC3-L002699](../../agents/web_agent.py#L2699) | 2699 | `""` | — |
| [SRC-1AE03B9EC3-L002700](../../agents/web_agent.py#L2700) | 2700 | `"        names = set(config) \| set(grouped) \| set(useful)"` | — |
| [SRC-1AE03B9EC3-L002701](../../agents/web_agent.py#L2701) | 2701 | `"        connectors = []"` | — |
| [SRC-1AE03B9EC3-L002702](../../agents/web_agent.py#L2702) | 2702 | `"        for name in sorted(names):"` | — |
| [SRC-1AE03B9EC3-L002703](../../agents/web_agent.py#L2703) | 2703 | `"            ready, config_status = config.get(name, (bool(grouped.get(name) or useful.get(name)), \"observed_in_code_path\"))"` | — |
| [SRC-1AE03B9EC3-L002704](../../agents/web_agent.py#L2704) | 2704 | `"            attempts = grouped.get(name, [])"` | — |
| [SRC-1AE03B9EC3-L002705](../../agents/web_agent.py#L2705) | 2705 | `"            statuses = [_clean_text(row.get(\"status\", \"unknown\"), 40).lower() or \"unknown\" for row in attempts]"` | — |
| [SRC-1AE03B9EC3-L002706](../../agents/web_agent.py#L2706) | 2706 | `"            status = max(statuses, key=lambda value: priority.get(value, 6)) if statuses else ("` | — |
| [SRC-1AE03B9EC3-L002707](../../agents/web_agent.py#L2707) | 2707 | `"                \"ok\" if useful.get(name, 0) else \"not_configured\" if not ready else \"not_attempted\")"` | — |
| [SRC-1AE03B9EC3-L002708](../../agents/web_agent.py#L2708) | 2708 | `"            if any(value in confirmed_attempt_statuses for value in statuses) or useful.get(name, 0):"` | — |
| [SRC-1AE03B9EC3-L002709](../../agents/web_agent.py#L2709) | 2709 | `"                attempted: bool \| None = True"` | — |
| [SRC-1AE03B9EC3-L002710](../../agents/web_agent.py#L2710) | 2710 | `"            elif any(value in uncertain_attempt_statuses for value in statuses):"` | — |
| [SRC-1AE03B9EC3-L002711](../../agents/web_agent.py#L2711) | 2711 | `"                attempted = None"` | — |
| [SRC-1AE03B9EC3-L002712](../../agents/web_agent.py#L2712) | 2712 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L002713](../../agents/web_agent.py#L2713) | 2713 | `"                attempted = False"` | — |
| [SRC-1AE03B9EC3-L002714](../../agents/web_agent.py#L2714) | 2714 | `"            successful_statuses = set(statuses) & _SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES"` | — |
| [SRC-1AE03B9EC3-L002715](../../agents/web_agent.py#L2715) | 2715 | `"            error_response_statuses = set(statuses) & {\"http_error\", \"unauthorized\", \"rate_limited\"}"` | — |
| [SRC-1AE03B9EC3-L002716](../../agents/web_agent.py#L2716) | 2716 | `"            uncertain_failure_statuses = set(statuses) & {\"timeout\", \"failed\", \"error\", \"unknown\", \"inconclusive\"}"` | — |
| [SRC-1AE03B9EC3-L002717](../../agents/web_agent.py#L2717) | 2717 | `"            failure_observed = bool(error_response_statuses or uncertain_failure_statuses or \"budget_exhausted\" in statuses)"` | — |
| [SRC-1AE03B9EC3-L002718](../../agents/web_agent.py#L2718) | 2718 | `"            available: bool \| None = ("` | — |
| [SRC-1AE03B9EC3-L002719](../../agents/web_agent.py#L2719) | 2719 | `"                True if successful_statuses or useful.get(name, 0)"` | — |
| [SRC-1AE03B9EC3-L002720](../../agents/web_agent.py#L2720) | 2720 | `"                else False if error_response_statuses or not ready or \"disabled\" in statuses or \"budget_exhausted\" in statuses"` | — |
| [SRC-1AE03B9EC3-L002721](../../agents/web_agent.py#L2721) | 2721 | `"                else None"` | — |
| [SRC-1AE03B9EC3-L002722](../../agents/web_agent.py#L2722) | 2722 | `"            )"` | — |
| [SRC-1AE03B9EC3-L002723](../../agents/web_agent.py#L2723) | 2723 | `"            verified: bool \| None = ("` | — |
| [SRC-1AE03B9EC3-L002724](../../agents/web_agent.py#L2724) | 2724 | `"                True if successful_statuses or useful.get(name, 0)"` | — |
| [SRC-1AE03B9EC3-L002725](../../agents/web_agent.py#L2725) | 2725 | `"                else False if error_response_statuses"` | — |
| [SRC-1AE03B9EC3-L002726](../../agents/web_agent.py#L2726) | 2726 | `"                else None"` | — |
| [SRC-1AE03B9EC3-L002727](../../agents/web_agent.py#L2727) | 2727 | `"            )"` | — |
| [SRC-1AE03B9EC3-L002728](../../agents/web_agent.py#L2728) | 2728 | `"            implementation_status = ("` | — |
| [SRC-1AE03B9EC3-L002729](../../agents/web_agent.py#L2729) | 2729 | `"                \"implemented_in_code\" if name in config"` | — |
| [SRC-1AE03B9EC3-L002730](../../agents/web_agent.py#L2730) | 2730 | `"                else \"observed_runtime_path\" if attempts or useful.get(name, 0)"` | — |
| [SRC-1AE03B9EC3-L002731](../../agents/web_agent.py#L2731) | 2731 | `"                else \"unknown\""` | — |
| [SRC-1AE03B9EC3-L002732](../../agents/web_agent.py#L2732) | 2732 | `"            )"` | — |
| [SRC-1AE03B9EC3-L002733](../../agents/web_agent.py#L2733) | 2733 | `"            queries = list(dict.fromkeys(_clean_text(row.get(\"query\", \"\"), 180) for row in attempts if row.get(\"query\")))[:3]"` | — |
| [SRC-1AE03B9EC3-L002734](../../agents/web_agent.py#L2734) | 2734 | `"            errors = list(dict.fromkeys(redact(row.get(\"error\")) for row in attempts if row.get(\"error\")))[:3]"` | — |
| [SRC-1AE03B9EC3-L002735](../../agents/web_agent.py#L2735) | 2735 | `"            result_count = sum(max(0, int(row.get(\"result_count\", 0) or 0)) for row in attempts)"` | — |
| [SRC-1AE03B9EC3-L002736](../../agents/web_agent.py#L2736) | 2736 | `"            accepted_count = sum("` | — |
| [SRC-1AE03B9EC3-L002737](../../agents/web_agent.py#L2737) | 2737 | `"                max(0, int(row.get(\"accepted_count\", row.get(\"result_count\", 0)) or 0))"` | — |
| [SRC-1AE03B9EC3-L002738](../../agents/web_agent.py#L2738) | 2738 | `"                for row in attempts"` | — |
| [SRC-1AE03B9EC3-L002739](../../agents/web_agent.py#L2739) | 2739 | `"            )"` | — |
| [SRC-1AE03B9EC3-L002740](../../agents/web_agent.py#L2740) | 2740 | `"            rejected_count = sum(max(0, int(row.get(\"rejected_count\", 0) or 0)) for row in attempts)"` | — |
| [SRC-1AE03B9EC3-L002741](../../agents/web_agent.py#L2741) | 2741 | `"            rejection_count_totals = {reason: 0 for reason in _PROVIDER_REJECTION_REASONS}"` | — |
| [SRC-1AE03B9EC3-L002742](../../agents/web_agent.py#L2742) | 2742 | `"            rejection_counts_seen = False"` | — |
| [SRC-1AE03B9EC3-L002743](../../agents/web_agent.py#L2743) | 2743 | `"            rejection_counts_complete = True"` | — |
| [SRC-1AE03B9EC3-L002744](../../agents/web_agent.py#L2744) | 2744 | `"            for row in attempts:"` | — |
| [SRC-1AE03B9EC3-L002745](../../agents/web_agent.py#L2745) | 2745 | `"                row_counts = row.get(\"rejection_counts\")"` | — |
| [SRC-1AE03B9EC3-L002746](../../agents/web_agent.py#L2746) | 2746 | `"                if not isinstance(row_counts, dict):"` | — |
| [SRC-1AE03B9EC3-L002747](../../agents/web_agent.py#L2747) | 2747 | `"                    # Legacy/incomplete records with actual rejections prevent claiming"` | — |
| [SRC-1AE03B9EC3-L002748](../../agents/web_agent.py#L2748) | 2748 | `"                    # that an aggregate breakdown covers every rejected candidate."` | — |
| [SRC-1AE03B9EC3-L002749](../../agents/web_agent.py#L2749) | 2749 | `"                    if max(0, int(row.get(\"rejected_count\", 0) or 0)) > 0:"` | — |
| [SRC-1AE03B9EC3-L002750](../../agents/web_agent.py#L2750) | 2750 | `"                        rejection_counts_complete = False"` | — |
| [SRC-1AE03B9EC3-L002751](../../agents/web_agent.py#L2751) | 2751 | `"                    continue"` | — |
| [SRC-1AE03B9EC3-L002752](../../agents/web_agent.py#L2752) | 2752 | `"                rejection_counts_seen = True"` | — |
| [SRC-1AE03B9EC3-L002753](../../agents/web_agent.py#L2753) | 2753 | `"                for reason in _PROVIDER_REJECTION_REASONS:"` | — |
| [SRC-1AE03B9EC3-L002754](../../agents/web_agent.py#L2754) | 2754 | `"                    try:"` | — |
| [SRC-1AE03B9EC3-L002755](../../agents/web_agent.py#L2755) | 2755 | `"                        rejection_count_totals[reason] += max(0, int(row_counts.get(reason, 0) or 0))"` | — |
| [SRC-1AE03B9EC3-L002756](../../agents/web_agent.py#L2756) | 2756 | `"                    except (TypeError, ValueError, OverflowError):"` | — |
| [SRC-1AE03B9EC3-L002757](../../agents/web_agent.py#L2757) | 2757 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L002758](../../agents/web_agent.py#L2758) | 2758 | `"            rejection_counts_observed = ("` | — |
| [SRC-1AE03B9EC3-L002759](../../agents/web_agent.py#L2759) | 2759 | `"                rejection_counts_seen"` | — |
| [SRC-1AE03B9EC3-L002760](../../agents/web_agent.py#L2760) | 2760 | `"                and rejection_counts_complete"` | — |
| [SRC-1AE03B9EC3-L002761](../../agents/web_agent.py#L2761) | 2761 | `"                and sum(rejection_count_totals.values()) == rejected_count"` | — |
| [SRC-1AE03B9EC3-L002762](../../agents/web_agent.py#L2762) | 2762 | `"            )"` | — |
| [SRC-1AE03B9EC3-L002763](../../agents/web_agent.py#L2763) | 2763 | `"            candidate_rejection_observed = \"filtered_all\" in statuses or rejected_count > 0"` | — |
| [SRC-1AE03B9EC3-L002764](../../agents/web_agent.py#L2764) | 2764 | `"            connectors.append({"` | — |
| [SRC-1AE03B9EC3-L002765](../../agents/web_agent.py#L2765) | 2765 | `"                \"name\": name, \"in_codebase\": name in config or bool(attempts),"` | — |
| [SRC-1AE03B9EC3-L002766](../../agents/web_agent.py#L2766) | 2766 | `"                \"implementation_status\": implementation_status,"` | — |
| [SRC-1AE03B9EC3-L002767](../../agents/web_agent.py#L2767) | 2767 | `"                \"configured\": bool(ready), \"configuration_status\": config_status,"` | — |
| [SRC-1AE03B9EC3-L002768](../../agents/web_agent.py#L2768) | 2768 | `"                \"attempted\": attempted, \"available_for_this_request\": available,"` | — |
| [SRC-1AE03B9EC3-L002769](../../agents/web_agent.py#L2769) | 2769 | `"                \"verified_for_this_request\": verified, \"failure_observed\": failure_observed,"` | — |
| [SRC-1AE03B9EC3-L002770](../../agents/web_agent.py#L2770) | 2770 | `"                \"candidate_rejection_observed\": candidate_rejection_observed,"` | — |
| [SRC-1AE03B9EC3-L002771](../../agents/web_agent.py#L2771) | 2771 | `"                \"status\": status, \"observed_statuses\": list(dict.fromkeys(statuses))[:6],"` | — |
| [SRC-1AE03B9EC3-L002772](../../agents/web_agent.py#L2772) | 2772 | `"                \"result_count\": result_count, \"accepted_count\": accepted_count,"` | — |
| [SRC-1AE03B9EC3-L002773](../../agents/web_agent.py#L2773) | 2773 | `"                \"useful_result_count\": useful.get(name, 0),"` | — |
| [SRC-1AE03B9EC3-L002774](../../agents/web_agent.py#L2774) | 2774 | `"                \"rejected_count\": rejected_count,"` | — |
| [SRC-1AE03B9EC3-L002775](../../agents/web_agent.py#L2775) | 2775 | `"                \"rejection_counts_observed\": rejection_counts_observed,"` | — |
| [SRC-1AE03B9EC3-L002776](../../agents/web_agent.py#L2776) | 2776 | `"                \"rejection_counts\": rejection_count_totals if rejection_counts_observed else None,"` | — |
| [SRC-1AE03B9EC3-L002777](../../agents/web_agent.py#L2777) | 2777 | `"                \"queries\": queries, \"errors\": errors,"` | — |
| [SRC-1AE03B9EC3-L002778](../../agents/web_agent.py#L2778) | 2778 | `"            })"` | — |
| [SRC-1AE03B9EC3-L002779](../../agents/web_agent.py#L2779) | 2779 | `"        return {"` | — |
| [SRC-1AE03B9EC3-L002780](../../agents/web_agent.py#L2780) | 2780 | `"            \"scope\": \"this_request_only\","` | — |
| [SRC-1AE03B9EC3-L002781](../../agents/web_agent.py#L2781) | 2781 | `"            \"semantics\": \"result_count is connector-reported rows; useful_result_count counts final fused source records attributed to a connector; neither proves factual accuracy or editorial independence.\","` | — |
| [SRC-1AE03B9EC3-L002782](../../agents/web_agent.py#L2782) | 2782 | `"            \"attempted_count\": sum(bool(item[\"attempted\"]) for item in connectors),"` | — |
| [SRC-1AE03B9EC3-L002783](../../agents/web_agent.py#L2783) | 2783 | `"            \"failed_count\": sum(item[\"status\"] in {\"failed\", \"error\", \"timeout\", \"http_error\", \"unauthorized\", \"rate_limited\"} for item in connectors),"` | — |
| [SRC-1AE03B9EC3-L002784](../../agents/web_agent.py#L2784) | 2784 | `"            \"connectors\": connectors[:24],"` | — |
| [SRC-1AE03B9EC3-L002785](../../agents/web_agent.py#L2785) | 2785 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002786](../../agents/web_agent.py#L2786) | 2786 | `""` | — |
| [SRC-1AE03B9EC3-L002787](../../agents/web_agent.py#L2787) | 2787 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L002788](../../agents/web_agent.py#L2788) | 2788 | `"    def _sanitize_history(history: Any) -> list[dict[str, str]]:"` | — |
| [SRC-1AE03B9EC3-L002789](../../agents/web_agent.py#L2789) | 2789 | `"        if not isinstance(history, list):"` | — |
| [SRC-1AE03B9EC3-L002790](../../agents/web_agent.py#L2790) | 2790 | `"            return []"` | — |
| [SRC-1AE03B9EC3-L002791](../../agents/web_agent.py#L2791) | 2791 | `"        result: list[dict[str, str]] = []"` | — |
| [SRC-1AE03B9EC3-L002792](../../agents/web_agent.py#L2792) | 2792 | `"        for item in history[-MAX_HISTORY_ITEMS:]:"` | — |
| [SRC-1AE03B9EC3-L002793](../../agents/web_agent.py#L2793) | 2793 | `"            if not isinstance(item, dict) or item.get(\"role\") not in {\"user\", \"assistant\"}:"` | — |
| [SRC-1AE03B9EC3-L002794](../../agents/web_agent.py#L2794) | 2794 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L002795](../../agents/web_agent.py#L2795) | 2795 | `"            text = _clean_text(item.get(\"content\"), MAX_HISTORY_CHARS)"` | — |
| [SRC-1AE03B9EC3-L002796](../../agents/web_agent.py#L2796) | 2796 | `"            if text:"` | — |
| [SRC-1AE03B9EC3-L002797](../../agents/web_agent.py#L2797) | 2797 | `"                result.append({\"role\": item[\"role\"], \"content\": text})"` | — |
| [SRC-1AE03B9EC3-L002798](../../agents/web_agent.py#L2798) | 2798 | `"        return result"` | — |
| [SRC-1AE03B9EC3-L002799](../../agents/web_agent.py#L2799) | 2799 | `""` | — |
| [SRC-1AE03B9EC3-L002800](../../agents/web_agent.py#L2800) | 2800 | `"    def _record_generation_diagnostic("` | — |
| [SRC-1AE03B9EC3-L002801](../../agents/web_agent.py#L2801) | 2801 | `"        self,"` | — |
| [SRC-1AE03B9EC3-L002802](../../agents/web_agent.py#L2802) | 2802 | `"        requested_model: str,"` | — |
| [SRC-1AE03B9EC3-L002803](../../agents/web_agent.py#L2803) | 2803 | `"        attempted_model: str,"` | — |
| [SRC-1AE03B9EC3-L002804](../../agents/web_agent.py#L2804) | 2804 | `"        status: str,"` | — |
| [SRC-1AE03B9EC3-L002805](../../agents/web_agent.py#L2805) | 2805 | `"        finish_reason: str \| None = None,"` | — |
| [SRC-1AE03B9EC3-L002806](../../agents/web_agent.py#L2806) | 2806 | `"        error_class: str \| None = None,"` | — |
| [SRC-1AE03B9EC3-L002807](../../agents/web_agent.py#L2807) | 2807 | `"        request_started: bool = True,"` | — |
| [SRC-1AE03B9EC3-L002808](../../agents/web_agent.py#L2808) | 2808 | `"        remote_response_received: bool \| None = None,"` | — |
| [SRC-1AE03B9EC3-L002809](../../agents/web_agent.py#L2809) | 2809 | `"    ) -> None:"` | — |
| [SRC-1AE03B9EC3-L002810](../../agents/web_agent.py#L2810) | 2810 | `"        \"\"\"Store bounded metadata for each model attempt; never retain prompts or output.\"\"\""` | — |
| [SRC-1AE03B9EC3-L002811](../../agents/web_agent.py#L2811) | 2811 | `"        self._generation_attempt_sequence = getattr(self, \"_generation_attempt_sequence\", 0) + 1"` | — |
| [SRC-1AE03B9EC3-L002812](../../agents/web_agent.py#L2812) | 2812 | `"        record: dict[str, Any] = {"` | — |
| [SRC-1AE03B9EC3-L002813](../../agents/web_agent.py#L2813) | 2813 | `"            \"attempt_number\": self._generation_attempt_sequence,"` | — |
| [SRC-1AE03B9EC3-L002814](../../agents/web_agent.py#L2814) | 2814 | `"            \"requested_model\": str(requested_model)[:160],"` | — |
| [SRC-1AE03B9EC3-L002815](../../agents/web_agent.py#L2815) | 2815 | `"            \"attempted_model\": str(attempted_model)[:160],"` | — |
| [SRC-1AE03B9EC3-L002816](../../agents/web_agent.py#L2816) | 2816 | `"            \"fallback_used\": str(attempted_model) != str(requested_model),"` | — |
| [SRC-1AE03B9EC3-L002817](../../agents/web_agent.py#L2817) | 2817 | `"            \"request_started\": bool(request_started),"` | — |
| [SRC-1AE03B9EC3-L002818](../../agents/web_agent.py#L2818) | 2818 | `"            \"status\": str(status)[:48],"` | — |
| [SRC-1AE03B9EC3-L002819](../../agents/web_agent.py#L2819) | 2819 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002820](../../agents/web_agent.py#L2820) | 2820 | `"        if remote_response_received is None and isinstance(finish_reason, str) and finish_reason.strip():"` | — |
| [SRC-1AE03B9EC3-L002821](../../agents/web_agent.py#L2821) | 2821 | `"            # A concrete finish_reason can only be observed after a provider response was received."` | — |
| [SRC-1AE03B9EC3-L002822](../../agents/web_agent.py#L2822) | 2822 | `"            remote_response_received = True"` | — |
| [SRC-1AE03B9EC3-L002823](../../agents/web_agent.py#L2823) | 2823 | `"        if remote_response_received is not None:"` | — |
| [SRC-1AE03B9EC3-L002824](../../agents/web_agent.py#L2824) | 2824 | `"            record[\"remote_response_received\"] = bool(remote_response_received)"` | — |
| [SRC-1AE03B9EC3-L002825](../../agents/web_agent.py#L2825) | 2825 | `"        if isinstance(finish_reason, str) and finish_reason.strip():"` | — |
| [SRC-1AE03B9EC3-L002826](../../agents/web_agent.py#L2826) | 2826 | `"            record[\"finish_reason\"] = finish_reason.strip()[:48]"` | — |
| [SRC-1AE03B9EC3-L002827](../../agents/web_agent.py#L2827) | 2827 | `"        if isinstance(error_class, str) and error_class:"` | — |
| [SRC-1AE03B9EC3-L002828](../../agents/web_agent.py#L2828) | 2828 | `"            record[\"error_class\"] = error_class[:80]"` | — |
| [SRC-1AE03B9EC3-L002829](../../agents/web_agent.py#L2829) | 2829 | `"        self.generation_diagnostics.append(record)"` | — |
| [SRC-1AE03B9EC3-L002830](../../agents/web_agent.py#L2830) | 2830 | `"        self.generation_diagnostics = self.generation_diagnostics[-12:]"` | — |
| [SRC-1AE03B9EC3-L002831](../../agents/web_agent.py#L2831) | 2831 | `""` | — |
| [SRC-1AE03B9EC3-L002832](../../agents/web_agent.py#L2832) | 2832 | `"    def _request_completion("` | — |
| [SRC-1AE03B9EC3-L002833](../../agents/web_agent.py#L2833) | 2833 | `"        self,"` | — |
| [SRC-1AE03B9EC3-L002834](../../agents/web_agent.py#L2834) | 2834 | `"        messages: list[dict[str, str]],"` | — |
| [SRC-1AE03B9EC3-L002835](../../agents/web_agent.py#L2835) | 2835 | `"        max_tokens: int = 1400,"` | — |
| [SRC-1AE03B9EC3-L002836](../../agents/web_agent.py#L2836) | 2836 | `"        temperature: float = 0.2,"` | — |
| [SRC-1AE03B9EC3-L002837](../../agents/web_agent.py#L2837) | 2837 | `"        timeout: int \| None = None,"` | — |
| [SRC-1AE03B9EC3-L002838](../../agents/web_agent.py#L2838) | 2838 | `"        model: str \| None = None,"` | — |
| [SRC-1AE03B9EC3-L002839](../../agents/web_agent.py#L2839) | 2839 | `"        enable_web_search: bool = False,"` | — |
| [SRC-1AE03B9EC3-L002840](../../agents/web_agent.py#L2840) | 2840 | `"    ) -> str:"` | — |
| [SRC-1AE03B9EC3-L002841](../../agents/web_agent.py#L2841) | 2841 | `"        \"\"\"Call an OpenAI-compatible API with bounded fallback and optional live server search.\"\"\""` | — |
| [SRC-1AE03B9EC3-L002842](../../agents/web_agent.py#L2842) | 2842 | `"        requested_model = (model or self.answer_model).strip()"` | — |
| [SRC-1AE03B9EC3-L002843](../../agents/web_agent.py#L2843) | 2843 | `"        if not self.api_key:"` | — |
| [SRC-1AE03B9EC3-L002844](../../agents/web_agent.py#L2844) | 2844 | `"            self._record_generation_diagnostic("` | — |
| [SRC-1AE03B9EC3-L002845](../../agents/web_agent.py#L2845) | 2845 | `"                requested_model=requested_model,"` | — |
| [SRC-1AE03B9EC3-L002846](../../agents/web_agent.py#L2846) | 2846 | `"                attempted_model=requested_model,"` | — |
| [SRC-1AE03B9EC3-L002847](../../agents/web_agent.py#L2847) | 2847 | `"                status=\"not_configured\","` | — |
| [SRC-1AE03B9EC3-L002848](../../agents/web_agent.py#L2848) | 2848 | `"                error_class=\"MissingAPIKey\","` | — |
| [SRC-1AE03B9EC3-L002849](../../agents/web_agent.py#L2849) | 2849 | `"                request_started=False,"` | — |
| [SRC-1AE03B9EC3-L002850](../../agents/web_agent.py#L2850) | 2850 | `"                remote_response_received=False,"` | — |
| [SRC-1AE03B9EC3-L002851](../../agents/web_agent.py#L2851) | 2851 | `"            )"` | — |
| [SRC-1AE03B9EC3-L002852](../../agents/web_agent.py#L2852) | 2852 | `"            raise RuntimeError(\"لم يتم ضبط مفتاح نموذج اللغة.\")"` | — |
| [SRC-1AE03B9EC3-L002853](../../agents/web_agent.py#L2853) | 2853 | `""` | — |
| [SRC-1AE03B9EC3-L002854](../../agents/web_agent.py#L2854) | 2854 | `"        model_candidates = [requested_model]"` | — |
| [SRC-1AE03B9EC3-L002855](../../agents/web_agent.py#L2855) | 2855 | `"        if self.fallback_model and self.fallback_model not in model_candidates:"` | — |
| [SRC-1AE03B9EC3-L002856](../../agents/web_agent.py#L2856) | 2856 | `"            model_candidates.append(self.fallback_model)"` | — |
| [SRC-1AE03B9EC3-L002857](../../agents/web_agent.py#L2857) | 2857 | `""` | — |
| [SRC-1AE03B9EC3-L002858](../../agents/web_agent.py#L2858) | 2858 | `"        last_error: RuntimeError \| None = None"` | — |
| [SRC-1AE03B9EC3-L002859](../../agents/web_agent.py#L2859) | 2859 | `"        for candidate_model in model_candidates:"` | — |
| [SRC-1AE03B9EC3-L002860](../../agents/web_agent.py#L2860) | 2860 | `"            budget = getattr(self, \"_request_budget\", None)"` | — |
| [SRC-1AE03B9EC3-L002861](../../agents/web_agent.py#L2861) | 2861 | `"            use_web_search = enable_web_search and self.openrouter_web_search_enabled"` | — |
| [SRC-1AE03B9EC3-L002862](../../agents/web_agent.py#L2862) | 2862 | `"            if budget is not None:"` | — |
| [SRC-1AE03B9EC3-L002863](../../agents/web_agent.py#L2863) | 2863 | `"                try:"` | — |
| [SRC-1AE03B9EC3-L002864](../../agents/web_agent.py#L2864) | 2864 | `"                    budget.reserve(\"model_calls\")"` | — |
| [SRC-1AE03B9EC3-L002865](../../agents/web_agent.py#L2865) | 2865 | `"                    request_timeout = budget.timeout_for(timeout or self.timeout)"` | — |
| [SRC-1AE03B9EC3-L002866](../../agents/web_agent.py#L2866) | 2866 | `"                    if use_web_search and budget.remaining_units(\"tool_calls\") < 3:"` | — |
| [SRC-1AE03B9EC3-L002867](../../agents/web_agent.py#L2867) | 2867 | `"                        # The model may still answer, but the optional server-side search"` | — |
| [SRC-1AE03B9EC3-L002868](../../agents/web_agent.py#L2868) | 2868 | `"                        # tool is disabled when its separate budget is unavailable."` | — |
| [SRC-1AE03B9EC3-L002869](../../agents/web_agent.py#L2869) | 2869 | `"                        use_web_search = False"` | — |
| [SRC-1AE03B9EC3-L002870](../../agents/web_agent.py#L2870) | 2870 | `"                    elif use_web_search:"` | — |
| [SRC-1AE03B9EC3-L002871](../../agents/web_agent.py#L2871) | 2871 | `"                        # Reserve the maximum server-side tool calls offered by this request."` | — |
| [SRC-1AE03B9EC3-L002872](../../agents/web_agent.py#L2872) | 2872 | `"                        budget.reserve(\"tool_calls\", amount=3)"` | — |
