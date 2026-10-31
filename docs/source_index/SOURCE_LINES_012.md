# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **012**
- سجلات الأسطر: **800**
- النطاق: SRC-1AE03B9EC3-L001883 إلى SRC-1AE03B9EC3-L002682
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-1AE03B9EC3 — [agents/web_agent.py](../../agents/web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1AE03B9EC3-L001883](../../agents/web_agent.py#L1883) | 1883 | `"                                    \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L001884](../../agents/web_agent.py#L1884) | 1884 | `"                                    \"published_at\": _clean_text(str(post.get(\"created_utc\") or \"\"), 100),"` | — |
| [SRC-1AE03B9EC3-L001885](../../agents/web_agent.py#L1885) | 1885 | `"                                })"` | — |
| [SRC-1AE03B9EC3-L001886](../../agents/web_agent.py#L1886) | 1886 | `"                        else:"` | — |
| [SRC-1AE03B9EC3-L001887](../../agents/web_agent.py#L1887) | 1887 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L001888](../../agents/web_agent.py#L1888) | 1888 | `"                                f\"Reddit OAuth search unavailable (HTTP {search_response.status_code}).\""` | — |
| [SRC-1AE03B9EC3-L001889](../../agents/web_agent.py#L1889) | 1889 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L001890](../../agents/web_agent.py#L1890) | 1890 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L001891](../../agents/web_agent.py#L1891) | 1891 | `"                        warnings.append(\"Reddit OAuth did not return an access token.\")"` | — |
| [SRC-1AE03B9EC3-L001892](../../agents/web_agent.py#L1892) | 1892 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L001893](../../agents/web_agent.py#L1893) | 1893 | `"                    warnings.append("` | — |
| [SRC-1AE03B9EC3-L001894](../../agents/web_agent.py#L1894) | 1894 | `"                        f\"Reddit OAuth authentication unavailable (HTTP {token_response.status_code}).\""` | — |
| [SRC-1AE03B9EC3-L001895](../../agents/web_agent.py#L1895) | 1895 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L001896](../../agents/web_agent.py#L1896) | 1896 | `"            except (httpx.HTTPError, OSError, ValueError, KeyError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L001897](../../agents/web_agent.py#L1897) | 1897 | `"                warnings.append(\"Reddit OAuth search failed for this request.\")"` | — |
| [SRC-1AE03B9EC3-L001898](../../agents/web_agent.py#L1898) | 1898 | `""` | — |
| [SRC-1AE03B9EC3-L001899](../../agents/web_agent.py#L1899) | 1899 | `"        if \"reddit\" in platforms and not any("` | — |
| [SRC-1AE03B9EC3-L001900](../../agents/web_agent.py#L1900) | 1900 | `"            row.get(\"provider\") == \"reddit_oauth_api\" for row in results"` | — |
| [SRC-1AE03B9EC3-L001901](../../agents/web_agent.py#L1901) | 1901 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L001902](../../agents/web_agent.py#L1902) | 1902 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L001903](../../agents/web_agent.py#L1903) | 1903 | `"                self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L001904](../../agents/web_agent.py#L1904) | 1904 | `"                response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L001905](../../agents/web_agent.py#L1905) | 1905 | `"                    \"https://www.reddit.com/search.rss\","` | — |
| [SRC-1AE03B9EC3-L001906](../../agents/web_agent.py#L1906) | 1906 | `"                    params={\"q\": query, \"sort\": \"relevance\", \"t\": \"all\", \"limit\": \"8\"},"` | — |
| [SRC-1AE03B9EC3-L001907](../../agents/web_agent.py#L1907) | 1907 | `"                    headers=headers,"` | — |
| [SRC-1AE03B9EC3-L001908](../../agents/web_agent.py#L1908) | 1908 | `"                    timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L001909](../../agents/web_agent.py#L1909) | 1909 | `"                    follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001910](../../agents/web_agent.py#L1910) | 1910 | `"                )"` | — |
| [SRC-1AE03B9EC3-L001911](../../agents/web_agent.py#L1911) | 1911 | `"                if response.status_code == 200:"` | — |
| [SRC-1AE03B9EC3-L001912](../../agents/web_agent.py#L1912) | 1912 | `"                    root = ET.fromstring(response.content)"` | — |
| [SRC-1AE03B9EC3-L001913](../../agents/web_agent.py#L1913) | 1913 | `"                    for item in root.iter():"` | — |
| [SRC-1AE03B9EC3-L001914](../../agents/web_agent.py#L1914) | 1914 | `"                        if item.tag.rsplit(\"}\", 1)[-1] != \"item\":"` | — |
| [SRC-1AE03B9EC3-L001915](../../agents/web_agent.py#L1915) | 1915 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L001916](../../agents/web_agent.py#L1916) | 1916 | `"                        fields = {"` | — |
| [SRC-1AE03B9EC3-L001917](../../agents/web_agent.py#L1917) | 1917 | `"                            child.tag.rsplit(\"}\", 1)[-1]: (child.text or \"\")"` | — |
| [SRC-1AE03B9EC3-L001918](../../agents/web_agent.py#L1918) | 1918 | `"                            for child in item"` | — |
| [SRC-1AE03B9EC3-L001919](../../agents/web_agent.py#L1919) | 1919 | `"                        }"` | — |
| [SRC-1AE03B9EC3-L001920](../../agents/web_agent.py#L1920) | 1920 | `"                        url = _public_http_url(fields.get(\"link\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L001921](../../agents/web_agent.py#L1921) | 1921 | `"                        if not url or \"reddit.com/\" not in url:"` | — |
| [SRC-1AE03B9EC3-L001922](../../agents/web_agent.py#L1922) | 1922 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L001923](../../agents/web_agent.py#L1923) | 1923 | `"                        description = BeautifulSoup("` | — |
| [SRC-1AE03B9EC3-L001924](../../agents/web_agent.py#L1924) | 1924 | `"                            fields.get(\"description\", \"\"), \"html.parser\""` | — |
| [SRC-1AE03B9EC3-L001925](../../agents/web_agent.py#L1925) | 1925 | `"                        ).get_text(\" \", strip=True)"` | — |
| [SRC-1AE03B9EC3-L001926](../../agents/web_agent.py#L1926) | 1926 | `"                        results.append({"` | — |
| [SRC-1AE03B9EC3-L001927](../../agents/web_agent.py#L1927) | 1927 | `"                            \"title\": _clean_text(fields.get(\"title\", \"\"), 300),"` | — |
| [SRC-1AE03B9EC3-L001928](../../agents/web_agent.py#L1928) | 1928 | `"                            \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L001929](../../agents/web_agent.py#L1929) | 1929 | `"                            \"snippet\": _clean_text(description, 1200),"` | — |
| [SRC-1AE03B9EC3-L001930](../../agents/web_agent.py#L1930) | 1930 | `"                            \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L001931](../../agents/web_agent.py#L1931) | 1931 | `"                            \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L001932](../../agents/web_agent.py#L1932) | 1932 | `"                            \"provider\": \"reddit_public_rss\","` | — |
| [SRC-1AE03B9EC3-L001933](../../agents/web_agent.py#L1933) | 1933 | `"                            \"provider_rank\": len(["` | — |
| [SRC-1AE03B9EC3-L001934](../../agents/web_agent.py#L1934) | 1934 | `"                                row for row in results"` | — |
| [SRC-1AE03B9EC3-L001935](../../agents/web_agent.py#L1935) | 1935 | `"                                if row.get(\"provider\") == \"reddit_public_rss\""` | — |
| [SRC-1AE03B9EC3-L001936](../../agents/web_agent.py#L1936) | 1936 | `"                            ]) + 1,"` | — |
| [SRC-1AE03B9EC3-L001937](../../agents/web_agent.py#L1937) | 1937 | `"                            \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L001938](../../agents/web_agent.py#L1938) | 1938 | `"                            \"published_at\": _clean_text(fields.get(\"pubDate\", \"\"), 100),"` | — |
| [SRC-1AE03B9EC3-L001939](../../agents/web_agent.py#L1939) | 1939 | `"                        })"` | — |
| [SRC-1AE03B9EC3-L001940](../../agents/web_agent.py#L1940) | 1940 | `"                        if sum(row.get(\"provider\") == \"reddit_public_rss\" for row in results) >= 8:"` | — |
| [SRC-1AE03B9EC3-L001941](../../agents/web_agent.py#L1941) | 1941 | `"                            break"` | — |
| [SRC-1AE03B9EC3-L001942](../../agents/web_agent.py#L1942) | 1942 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L001943](../../agents/web_agent.py#L1943) | 1943 | `"                    warnings.append(f\"Reddit public RSS unavailable (HTTP {response.status_code})\")"` | — |
| [SRC-1AE03B9EC3-L001944](../../agents/web_agent.py#L1944) | 1944 | `"            except (httpx.HTTPError, OSError, ValueError, ET.ParseError):"` | — |
| [SRC-1AE03B9EC3-L001945](../../agents/web_agent.py#L1945) | 1945 | `"                warnings.append(\"Reddit public RSS unavailable for this request\")"` | — |
| [SRC-1AE03B9EC3-L001946](../../agents/web_agent.py#L1946) | 1946 | `""` | — |
| [SRC-1AE03B9EC3-L001947](../../agents/web_agent.py#L1947) | 1947 | `"        if \"bluesky\" in platforms:"` | — |
| [SRC-1AE03B9EC3-L001948](../../agents/web_agent.py#L1948) | 1948 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L001949](../../agents/web_agent.py#L1949) | 1949 | `"                self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L001950](../../agents/web_agent.py#L1950) | 1950 | `"                response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L001951](../../agents/web_agent.py#L1951) | 1951 | `"                    \"https://public.api.bsky.app/xrpc/app.bsky.feed.searchPosts\","` | — |
| [SRC-1AE03B9EC3-L001952](../../agents/web_agent.py#L1952) | 1952 | `"                    params={\"q\": query, \"limit\": 10},"` | — |
| [SRC-1AE03B9EC3-L001953](../../agents/web_agent.py#L1953) | 1953 | `"                    headers=headers,"` | — |
| [SRC-1AE03B9EC3-L001954](../../agents/web_agent.py#L1954) | 1954 | `"                    timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L001955](../../agents/web_agent.py#L1955) | 1955 | `"                    follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001956](../../agents/web_agent.py#L1956) | 1956 | `"                )"` | — |
| [SRC-1AE03B9EC3-L001957](../../agents/web_agent.py#L1957) | 1957 | `"                if response.status_code == 200:"` | — |
| [SRC-1AE03B9EC3-L001958](../../agents/web_agent.py#L1958) | 1958 | `"                    data = response.json()"` | — |
| [SRC-1AE03B9EC3-L001959](../../agents/web_agent.py#L1959) | 1959 | `"                    for item in data.get(\"posts\", []):"` | — |
| [SRC-1AE03B9EC3-L001960](../../agents/web_agent.py#L1960) | 1960 | `"                        post = item.get(\"post\", {})"` | — |
| [SRC-1AE03B9EC3-L001961](../../agents/web_agent.py#L1961) | 1961 | `"                        record = post.get(\"record\", {})"` | — |
| [SRC-1AE03B9EC3-L001962](../../agents/web_agent.py#L1962) | 1962 | `"                        author = post.get(\"author\", {})"` | — |
| [SRC-1AE03B9EC3-L001963](../../agents/web_agent.py#L1963) | 1963 | `"                        uri = post.get(\"uri\", \"\")"` | — |
| [SRC-1AE03B9EC3-L001964](../../agents/web_agent.py#L1964) | 1964 | `"                        rkey = uri.rsplit(\"/\", 1)[-1]"` | — |
| [SRC-1AE03B9EC3-L001965](../../agents/web_agent.py#L1965) | 1965 | `"                        handle = author.get(\"handle\", \"\")"` | — |
| [SRC-1AE03B9EC3-L001966](../../agents/web_agent.py#L1966) | 1966 | `"                        if not handle or not rkey:"` | — |
| [SRC-1AE03B9EC3-L001967](../../agents/web_agent.py#L1967) | 1967 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L001968](../../agents/web_agent.py#L1968) | 1968 | `"                        url = f\"https://bsky.app/profile/{handle}/post/{rkey}\""` | — |
| [SRC-1AE03B9EC3-L001969](../../agents/web_agent.py#L1969) | 1969 | `"                        results.append({"` | — |
| [SRC-1AE03B9EC3-L001970](../../agents/web_agent.py#L1970) | 1970 | `"                            \"title\": _clean_text(author.get(\"displayName\") or handle, 300),"` | — |
| [SRC-1AE03B9EC3-L001971](../../agents/web_agent.py#L1971) | 1971 | `"                            \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L001972](../../agents/web_agent.py#L1972) | 1972 | `"                            \"snippet\": _clean_text(record.get(\"text\") or \"\", 1200),"` | — |
| [SRC-1AE03B9EC3-L001973](../../agents/web_agent.py#L1973) | 1973 | `"                            \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L001974](../../agents/web_agent.py#L1974) | 1974 | `"                            \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L001975](../../agents/web_agent.py#L1975) | 1975 | `"                            \"provider\": \"bluesky_public_search\","` | — |
| [SRC-1AE03B9EC3-L001976](../../agents/web_agent.py#L1976) | 1976 | `"                            \"provider_rank\": len(["` | — |
| [SRC-1AE03B9EC3-L001977](../../agents/web_agent.py#L1977) | 1977 | `"                                row for row in results"` | — |
| [SRC-1AE03B9EC3-L001978](../../agents/web_agent.py#L1978) | 1978 | `"                                if row.get(\"provider\") == \"bluesky_public_search\""` | — |
| [SRC-1AE03B9EC3-L001979](../../agents/web_agent.py#L1979) | 1979 | `"                            ]) + 1,"` | — |
| [SRC-1AE03B9EC3-L001980](../../agents/web_agent.py#L1980) | 1980 | `"                            \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L001981](../../agents/web_agent.py#L1981) | 1981 | `"                            \"published_at\": _clean_text(post.get(\"indexedAt\") or \"\", 100),"` | — |
| [SRC-1AE03B9EC3-L001982](../../agents/web_agent.py#L1982) | 1982 | `"                        })"` | — |
| [SRC-1AE03B9EC3-L001983](../../agents/web_agent.py#L1983) | 1983 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L001984](../../agents/web_agent.py#L1984) | 1984 | `"                    warnings.append(f\"Bluesky public search unavailable (HTTP {response.status_code})\")"` | — |
| [SRC-1AE03B9EC3-L001985](../../agents/web_agent.py#L1985) | 1985 | `"            except (httpx.HTTPError, OSError, ValueError, KeyError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L001986](../../agents/web_agent.py#L1986) | 1986 | `"                warnings.append(\"Bluesky public search unavailable for this request\")"` | — |
| [SRC-1AE03B9EC3-L001987](../../agents/web_agent.py#L1987) | 1987 | `""` | — |
| [SRC-1AE03B9EC3-L001988](../../agents/web_agent.py#L1988) | 1988 | `"        if \"facebook\" in platforms:"` | — |
| [SRC-1AE03B9EC3-L001989](../../agents/web_agent.py#L1989) | 1989 | `"            fb_token = os.getenv(\"FACEBOOK_PAGE_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L001990](../../agents/web_agent.py#L1990) | 1990 | `"            page_ids = ["` | — |
| [SRC-1AE03B9EC3-L001991](../../agents/web_agent.py#L1991) | 1991 | `"                value.strip()"` | — |
| [SRC-1AE03B9EC3-L001992](../../agents/web_agent.py#L1992) | 1992 | `"                for value in os.getenv(\"FACEBOOK_PAGE_IDS\", \"\").split(\",\")"` | — |
| [SRC-1AE03B9EC3-L001993](../../agents/web_agent.py#L1993) | 1993 | `"                if value.strip()"` | — |
| [SRC-1AE03B9EC3-L001994](../../agents/web_agent.py#L1994) | 1994 | `"            ][:5]"` | — |
| [SRC-1AE03B9EC3-L001995](../../agents/web_agent.py#L1995) | 1995 | `"            graph_version = os.getenv(\"META_GRAPH_VERSION\", \"v25.0\").strip()"` | — |
| [SRC-1AE03B9EC3-L001996](../../agents/web_agent.py#L1996) | 1996 | `"            if fb_token and page_ids:"` | — |
| [SRC-1AE03B9EC3-L001997](../../agents/web_agent.py#L1997) | 1997 | `"                # Scope direct reading to page IDs supplied by the operator and the"` | — |
| [SRC-1AE03B9EC3-L001998](../../agents/web_agent.py#L1998) | 1998 | `"                # permissions granted to this token. This is not global Facebook search."` | — |
| [SRC-1AE03B9EC3-L001999](../../agents/web_agent.py#L1999) | 1999 | `"                query_terms = {"` | — |
| [SRC-1AE03B9EC3-L002000](../../agents/web_agent.py#L2000) | 2000 | `"                    word.casefold()"` | — |
| [SRC-1AE03B9EC3-L002001](../../agents/web_agent.py#L2001) | 2001 | `"                    for word in re.findall(r\"[\\w\\u0600-\\u06FF]+\", query, flags=re.UNICODE)"` | — |
| [SRC-1AE03B9EC3-L002002](../../agents/web_agent.py#L2002) | 2002 | `"                    if len(word) >= 3"` | — |
| [SRC-1AE03B9EC3-L002003](../../agents/web_agent.py#L2003) | 2003 | `"                }"` | — |
| [SRC-1AE03B9EC3-L002004](../../agents/web_agent.py#L2004) | 2004 | `"                for page_id in page_ids:"` | — |
| [SRC-1AE03B9EC3-L002005](../../agents/web_agent.py#L2005) | 2005 | `"                    try:"` | — |
| [SRC-1AE03B9EC3-L002006](../../agents/web_agent.py#L2006) | 2006 | `"                        self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L002007](../../agents/web_agent.py#L2007) | 2007 | `"                        response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L002008](../../agents/web_agent.py#L2008) | 2008 | `"                            f\"https://graph.facebook.com/{graph_version}/{page_id}/posts\","` | — |
| [SRC-1AE03B9EC3-L002009](../../agents/web_agent.py#L2009) | 2009 | `"                            params={"` | — |
| [SRC-1AE03B9EC3-L002010](../../agents/web_agent.py#L2010) | 2010 | `"                                \"fields\": ("` | — |
| [SRC-1AE03B9EC3-L002011](../../agents/web_agent.py#L2011) | 2011 | `"                                    \"message,permalink_url,created_time,\""` | — |
| [SRC-1AE03B9EC3-L002012](../../agents/web_agent.py#L2012) | 2012 | `"                                    \"comments.limit(10){message,created_time,like_count}\""` | — |
| [SRC-1AE03B9EC3-L002013](../../agents/web_agent.py#L2013) | 2013 | `"                                ),"` | — |
| [SRC-1AE03B9EC3-L002014](../../agents/web_agent.py#L2014) | 2014 | `"                                \"limit\": 10,"` | — |
| [SRC-1AE03B9EC3-L002015](../../agents/web_agent.py#L2015) | 2015 | `"                            },"` | — |
| [SRC-1AE03B9EC3-L002016](../../agents/web_agent.py#L2016) | 2016 | `"                            headers={"` | — |
| [SRC-1AE03B9EC3-L002017](../../agents/web_agent.py#L2017) | 2017 | `"                                **headers,"` | — |
| [SRC-1AE03B9EC3-L002018](../../agents/web_agent.py#L2018) | 2018 | `"                                \"Authorization\": \"Bearer \" + fb_token,"` | — |
| [SRC-1AE03B9EC3-L002019](../../agents/web_agent.py#L2019) | 2019 | `"                            },"` | — |
| [SRC-1AE03B9EC3-L002020](../../agents/web_agent.py#L2020) | 2020 | `"                            timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L002021](../../agents/web_agent.py#L2021) | 2021 | `"                            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L002022](../../agents/web_agent.py#L2022) | 2022 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L002023](../../agents/web_agent.py#L2023) | 2023 | `"                        if response.status_code != 200:"` | — |
| [SRC-1AE03B9EC3-L002024](../../agents/web_agent.py#L2024) | 2024 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L002025](../../agents/web_agent.py#L2025) | 2025 | `"                                \"Facebook Pages API unavailable for one configured page \""` | — |
| [SRC-1AE03B9EC3-L002026](../../agents/web_agent.py#L2026) | 2026 | `"                                f\"(HTTP {response.status_code}); verify page ownership, token and permissions.\""` | — |
| [SRC-1AE03B9EC3-L002027](../../agents/web_agent.py#L2027) | 2027 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L002028](../../agents/web_agent.py#L2028) | 2028 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002029](../../agents/web_agent.py#L2029) | 2029 | `"                        posts = response.json().get(\"data\", [])"` | — |
| [SRC-1AE03B9EC3-L002030](../../agents/web_agent.py#L2030) | 2030 | `"                        rank = 0"` | — |
| [SRC-1AE03B9EC3-L002031](../../agents/web_agent.py#L2031) | 2031 | `"                        for post in posts:"` | — |
| [SRC-1AE03B9EC3-L002032](../../agents/web_agent.py#L2032) | 2032 | `"                            message = _clean_text(post.get(\"message\") or \"\", 1400)"` | — |
| [SRC-1AE03B9EC3-L002033](../../agents/web_agent.py#L2033) | 2033 | `"                            comments = post.get(\"comments\", {}).get(\"data\", [])"` | — |
| [SRC-1AE03B9EC3-L002034](../../agents/web_agent.py#L2034) | 2034 | `"                            comment_text = ["` | — |
| [SRC-1AE03B9EC3-L002035](../../agents/web_agent.py#L2035) | 2035 | `"                                _clean_text(item.get(\"message\") or \"\", 500)"` | — |
| [SRC-1AE03B9EC3-L002036](../../agents/web_agent.py#L2036) | 2036 | `"                                for item in comments"` | — |
| [SRC-1AE03B9EC3-L002037](../../agents/web_agent.py#L2037) | 2037 | `"                                if isinstance(item, dict) and item.get(\"message\")"` | — |
| [SRC-1AE03B9EC3-L002038](../../agents/web_agent.py#L2038) | 2038 | `"                            ]"` | — |
| [SRC-1AE03B9EC3-L002039](../../agents/web_agent.py#L2039) | 2039 | `"                            searchable = (message + \" \" + \" \".join(comment_text)).casefold()"` | — |
| [SRC-1AE03B9EC3-L002040](../../agents/web_agent.py#L2040) | 2040 | `"                            matched = sum(term in searchable for term in query_terms)"` | — |
| [SRC-1AE03B9EC3-L002041](../../agents/web_agent.py#L2041) | 2041 | `"                            if query_terms and matched == 0:"` | — |
| [SRC-1AE03B9EC3-L002042](../../agents/web_agent.py#L2042) | 2042 | `"                                continue"` | — |
| [SRC-1AE03B9EC3-L002043](../../agents/web_agent.py#L2043) | 2043 | `"                            permalink = _public_http_url(post.get(\"permalink_url\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L002044](../../agents/web_agent.py#L2044) | 2044 | `"                            if not permalink:"` | — |
| [SRC-1AE03B9EC3-L002045](../../agents/web_agent.py#L2045) | 2045 | `"                                continue"` | — |
| [SRC-1AE03B9EC3-L002046](../../agents/web_agent.py#L2046) | 2046 | `"                            rank += 1"` | — |
| [SRC-1AE03B9EC3-L002047](../../agents/web_agent.py#L2047) | 2047 | `"                            excerpt = message"` | — |
| [SRC-1AE03B9EC3-L002048](../../agents/web_agent.py#L2048) | 2048 | `"                            if comment_text:"` | — |
| [SRC-1AE03B9EC3-L002049](../../agents/web_agent.py#L2049) | 2049 | `"                                excerpt = ("` | — |
| [SRC-1AE03B9EC3-L002050](../../agents/web_agent.py#L2050) | 2050 | `"                                    excerpt + \"\\n\\nتعليقات عامة على المنشور:\\n\""` | — |
| [SRC-1AE03B9EC3-L002051](../../agents/web_agent.py#L2051) | 2051 | `"                                    if excerpt else \"تعليقات عامة على المنشور:\\n\""` | — |
| [SRC-1AE03B9EC3-L002052](../../agents/web_agent.py#L2052) | 2052 | `"                                ) + \"\\n— \".join(comment_text)"` | — |
| [SRC-1AE03B9EC3-L002053](../../agents/web_agent.py#L2053) | 2053 | `"                            results.append({"` | — |
| [SRC-1AE03B9EC3-L002054](../../agents/web_agent.py#L2054) | 2054 | `"                                \"title\": _clean_text(message or \"Facebook public Page post\", 300),"` | — |
| [SRC-1AE03B9EC3-L002055](../../agents/web_agent.py#L2055) | 2055 | `"                                \"url\": permalink,"` | — |
| [SRC-1AE03B9EC3-L002056](../../agents/web_agent.py#L2056) | 2056 | `"                                \"snippet\": _clean_text(excerpt, 1800),"` | — |
| [SRC-1AE03B9EC3-L002057](../../agents/web_agent.py#L2057) | 2057 | `"                                \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L002058](../../agents/web_agent.py#L2058) | 2058 | `"                                \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L002059](../../agents/web_agent.py#L2059) | 2059 | `"                                \"provider\": \"facebook_pages_api\","` | — |
| [SRC-1AE03B9EC3-L002060](../../agents/web_agent.py#L2060) | 2060 | `"                                \"provider_rank\": rank,"` | — |
| [SRC-1AE03B9EC3-L002061](../../agents/web_agent.py#L2061) | 2061 | `"                                \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L002062](../../agents/web_agent.py#L2062) | 2062 | `"                                \"published_at\": _clean_text(post.get(\"created_time\") or \"\", 100),"` | — |
| [SRC-1AE03B9EC3-L002063](../../agents/web_agent.py#L2063) | 2063 | `"                            })"` | — |
| [SRC-1AE03B9EC3-L002064](../../agents/web_agent.py#L2064) | 2064 | `"                            if rank >= 10:"` | — |
| [SRC-1AE03B9EC3-L002065](../../agents/web_agent.py#L2065) | 2065 | `"                                break"` | — |
| [SRC-1AE03B9EC3-L002066](../../agents/web_agent.py#L2066) | 2066 | `"                    except (httpx.HTTPError, OSError, ValueError, KeyError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L002067](../../agents/web_agent.py#L2067) | 2067 | `"                        warnings.append(\"Facebook Pages API failed for one configured page.\")"` | — |
| [SRC-1AE03B9EC3-L002068](../../agents/web_agent.py#L2068) | 2068 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L002069](../../agents/web_agent.py#L2069) | 2069 | `"                warnings.append("` | — |
| [SRC-1AE03B9EC3-L002070](../../agents/web_agent.py#L2070) | 2070 | `"                    \"Facebook direct API is not configured for specific pages; indexed public Facebook pages are still searched.\""` | — |
| [SRC-1AE03B9EC3-L002071](../../agents/web_agent.py#L2071) | 2071 | `"                )"` | — |
| [SRC-1AE03B9EC3-L002072](../../agents/web_agent.py#L2072) | 2072 | `""` | — |
| [SRC-1AE03B9EC3-L002073](../../agents/web_agent.py#L2073) | 2073 | `"        if \"instagram\" in platforms:"` | — |
| [SRC-1AE03B9EC3-L002074](../../agents/web_agent.py#L2074) | 2074 | `"            ig_user_id = os.getenv(\"INSTAGRAM_USER_ID\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L002075](../../agents/web_agent.py#L2075) | 2075 | `"            ig_token = os.getenv(\"INSTAGRAM_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L002076](../../agents/web_agent.py#L2076) | 2076 | `"            graph_version = os.getenv(\"META_GRAPH_VERSION\", \"v25.0\").strip()"` | — |
| [SRC-1AE03B9EC3-L002077](../../agents/web_agent.py#L2077) | 2077 | `"            if ig_user_id and ig_token:"` | — |
| [SRC-1AE03B9EC3-L002078](../../agents/web_agent.py#L2078) | 2078 | `"                # The official Hashtag Search API returns public hashtag media only."` | — |
| [SRC-1AE03B9EC3-L002079](../../agents/web_agent.py#L2079) | 2079 | `"                # It does not search every Instagram post or bypass private accounts."` | — |
| [SRC-1AE03B9EC3-L002080](../../agents/web_agent.py#L2080) | 2080 | `"                hashtags = re.findall(r\"#([\\w\\u0600-\\u06FF]+)\", query, flags=re.UNICODE)"` | — |
| [SRC-1AE03B9EC3-L002081](../../agents/web_agent.py#L2081) | 2081 | `"                if not hashtags:"` | — |
| [SRC-1AE03B9EC3-L002082](../../agents/web_agent.py#L2082) | 2082 | `"                    words = re.findall(r\"[\\w\\u0600-\\u06FF]+\", query, flags=re.UNICODE)"` | — |
| [SRC-1AE03B9EC3-L002083](../../agents/web_agent.py#L2083) | 2083 | `"                    stopwords = {"` | — |
| [SRC-1AE03B9EC3-L002084](../../agents/web_agent.py#L2084) | 2084 | `"                        \"ابحث\", \"بحث\", \"عن\", \"في\", \"على\", \"من\", \"مع\", \"تجارب\","` | — |
| [SRC-1AE03B9EC3-L002085](../../agents/web_agent.py#L2085) | 2085 | `"                        \"الناس\", \"العملاء\", \"منشورات\", \"تعليقات\", \"مواقع\", \"التواصل\","` | — |
| [SRC-1AE03B9EC3-L002086](../../agents/web_agent.py#L2086) | 2086 | `"                        \"الاجتماعي\", \"public\", \"search\", \"social\", \"media\", \"posts\","` | — |
| [SRC-1AE03B9EC3-L002087](../../agents/web_agent.py#L2087) | 2087 | `"                        \"find\", \"about\", \"with\", \"the\", \"and\", \"for\","` | — |
| [SRC-1AE03B9EC3-L002088](../../agents/web_agent.py#L2088) | 2088 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L002089](../../agents/web_agent.py#L2089) | 2089 | `"                    useful = ["` | — |
| [SRC-1AE03B9EC3-L002090](../../agents/web_agent.py#L2090) | 2090 | `"                        word for word in words"` | — |
| [SRC-1AE03B9EC3-L002091](../../agents/web_agent.py#L2091) | 2091 | `"                        if len(word) >= 3 and word.casefold() not in stopwords"` | — |
| [SRC-1AE03B9EC3-L002092](../../agents/web_agent.py#L2092) | 2092 | `"                    ]"` | — |
| [SRC-1AE03B9EC3-L002093](../../agents/web_agent.py#L2093) | 2093 | `"                    if useful:"` | — |
| [SRC-1AE03B9EC3-L002094](../../agents/web_agent.py#L2094) | 2094 | `"                        hashtags = [\"_\".join(useful[:3])]"` | — |
| [SRC-1AE03B9EC3-L002095](../../agents/web_agent.py#L2095) | 2095 | `"                # Meta limits unique hashtag searches over a rolling week; keep this"` | — |
| [SRC-1AE03B9EC3-L002096](../../agents/web_agent.py#L2096) | 2096 | `"                # connector conservative and use no more than two tags per user request."` | — |
| [SRC-1AE03B9EC3-L002097](../../agents/web_agent.py#L2097) | 2097 | `"                for hashtag in list(dict.fromkeys(hashtags))[:1]:"` | — |
| [SRC-1AE03B9EC3-L002098](../../agents/web_agent.py#L2098) | 2098 | `"                    try:"` | — |
| [SRC-1AE03B9EC3-L002099](../../agents/web_agent.py#L2099) | 2099 | `"                        self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L002100](../../agents/web_agent.py#L2100) | 2100 | `"                        search_response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L002101](../../agents/web_agent.py#L2101) | 2101 | `"                            f\"https://graph.facebook.com/{graph_version}/ig_hashtag_search\","` | — |
| [SRC-1AE03B9EC3-L002102](../../agents/web_agent.py#L2102) | 2102 | `"                            params={"` | — |
| [SRC-1AE03B9EC3-L002103](../../agents/web_agent.py#L2103) | 2103 | `"                                \"user_id\": ig_user_id,"` | — |
| [SRC-1AE03B9EC3-L002104](../../agents/web_agent.py#L2104) | 2104 | `"                                \"q\": hashtag,"` | — |
| [SRC-1AE03B9EC3-L002105](../../agents/web_agent.py#L2105) | 2105 | `"                                \"fields\": \"id,name\","` | — |
| [SRC-1AE03B9EC3-L002106](../../agents/web_agent.py#L2106) | 2106 | `"                                \"access_token\": ig_token,"` | — |
| [SRC-1AE03B9EC3-L002107](../../agents/web_agent.py#L2107) | 2107 | `"                            },"` | — |
| [SRC-1AE03B9EC3-L002108](../../agents/web_agent.py#L2108) | 2108 | `"                            headers=headers,"` | — |
| [SRC-1AE03B9EC3-L002109](../../agents/web_agent.py#L2109) | 2109 | `"                            timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L002110](../../agents/web_agent.py#L2110) | 2110 | `"                            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L002111](../../agents/web_agent.py#L2111) | 2111 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L002112](../../agents/web_agent.py#L2112) | 2112 | `"                        if search_response.status_code != 200:"` | — |
| [SRC-1AE03B9EC3-L002113](../../agents/web_agent.py#L2113) | 2113 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L002114](../../agents/web_agent.py#L2114) | 2114 | `"                                \"Instagram Graph API hashtag search unavailable \""` | — |
| [SRC-1AE03B9EC3-L002115](../../agents/web_agent.py#L2115) | 2115 | `"                                f\"(HTTP {search_response.status_code}); check permissions and access.\""` | — |
| [SRC-1AE03B9EC3-L002116](../../agents/web_agent.py#L2116) | 2116 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L002117](../../agents/web_agent.py#L2117) | 2117 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002118](../../agents/web_agent.py#L2118) | 2118 | `"                        tag_data = search_response.json().get(\"data\", [])"` | — |
| [SRC-1AE03B9EC3-L002119](../../agents/web_agent.py#L2119) | 2119 | `"                        if not tag_data:"` | — |
| [SRC-1AE03B9EC3-L002120](../../agents/web_agent.py#L2120) | 2120 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002121](../../agents/web_agent.py#L2121) | 2121 | `"                        hashtag_id = tag_data[0].get(\"id\")"` | — |
| [SRC-1AE03B9EC3-L002122](../../agents/web_agent.py#L2122) | 2122 | `"                        if not hashtag_id:"` | — |
| [SRC-1AE03B9EC3-L002123](../../agents/web_agent.py#L2123) | 2123 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002124](../../agents/web_agent.py#L2124) | 2124 | `"                        self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L002125](../../agents/web_agent.py#L2125) | 2125 | `"                        media_response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L002126](../../agents/web_agent.py#L2126) | 2126 | `"                            f\"https://graph.facebook.com/{graph_version}/{hashtag_id}/recent_media\","` | — |
| [SRC-1AE03B9EC3-L002127](../../agents/web_agent.py#L2127) | 2127 | `"                            params={"` | — |
| [SRC-1AE03B9EC3-L002128](../../agents/web_agent.py#L2128) | 2128 | `"                                \"user_id\": ig_user_id,"` | — |
| [SRC-1AE03B9EC3-L002129](../../agents/web_agent.py#L2129) | 2129 | `"                                \"fields\": \"id,caption,media_type,permalink,timestamp,like_count,comments_count\","` | — |
| [SRC-1AE03B9EC3-L002130](../../agents/web_agent.py#L2130) | 2130 | `"                                \"limit\": 20,"` | — |
| [SRC-1AE03B9EC3-L002131](../../agents/web_agent.py#L2131) | 2131 | `"                                \"access_token\": ig_token,"` | — |
| [SRC-1AE03B9EC3-L002132](../../agents/web_agent.py#L2132) | 2132 | `"                            },"` | — |
| [SRC-1AE03B9EC3-L002133](../../agents/web_agent.py#L2133) | 2133 | `"                            headers=headers,"` | — |
| [SRC-1AE03B9EC3-L002134](../../agents/web_agent.py#L2134) | 2134 | `"                            timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L002135](../../agents/web_agent.py#L2135) | 2135 | `"                            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L002136](../../agents/web_agent.py#L2136) | 2136 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L002137](../../agents/web_agent.py#L2137) | 2137 | `"                        if media_response.status_code != 200:"` | — |
| [SRC-1AE03B9EC3-L002138](../../agents/web_agent.py#L2138) | 2138 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L002139](../../agents/web_agent.py#L2139) | 2139 | `"                                \"Instagram public hashtag media unavailable \""` | — |
| [SRC-1AE03B9EC3-L002140](../../agents/web_agent.py#L2140) | 2140 | `"                                f\"(HTTP {media_response.status_code}).\""` | — |
| [SRC-1AE03B9EC3-L002141](../../agents/web_agent.py#L2141) | 2141 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L002142](../../agents/web_agent.py#L2142) | 2142 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002143](../../agents/web_agent.py#L2143) | 2143 | `"                        items = media_response.json().get(\"data\", [])"` | — |
| [SRC-1AE03B9EC3-L002144](../../agents/web_agent.py#L2144) | 2144 | `"                        for item in items:"` | — |
| [SRC-1AE03B9EC3-L002145](../../agents/web_agent.py#L2145) | 2145 | `"                            url = _public_http_url(item.get(\"permalink\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L002146](../../agents/web_agent.py#L2146) | 2146 | `"                            if not url:"` | — |
| [SRC-1AE03B9EC3-L002147](../../agents/web_agent.py#L2147) | 2147 | `"                                continue"` | — |
| [SRC-1AE03B9EC3-L002148](../../agents/web_agent.py#L2148) | 2148 | `"                            metrics = []"` | — |
| [SRC-1AE03B9EC3-L002149](../../agents/web_agent.py#L2149) | 2149 | `"                            if item.get(\"like_count\") is not None:"` | — |
| [SRC-1AE03B9EC3-L002150](../../agents/web_agent.py#L2150) | 2150 | `"                                metrics.append(\"likes=\" + str(item[\"like_count\"]))"` | — |
| [SRC-1AE03B9EC3-L002151](../../agents/web_agent.py#L2151) | 2151 | `"                            if item.get(\"comments_count\") is not None:"` | — |
| [SRC-1AE03B9EC3-L002152](../../agents/web_agent.py#L2152) | 2152 | `"                                metrics.append(\"comments=\" + str(item[\"comments_count\"]))"` | — |
| [SRC-1AE03B9EC3-L002153](../../agents/web_agent.py#L2153) | 2153 | `"                            caption = _clean_text(item.get(\"caption\") or \"\", 1200)"` | — |
| [SRC-1AE03B9EC3-L002154](../../agents/web_agent.py#L2154) | 2154 | `"                            if metrics:"` | — |
| [SRC-1AE03B9EC3-L002155](../../agents/web_agent.py#L2155) | 2155 | `"                                caption = (caption + \" \| \" if caption else \"\") + \", \".join(metrics)"` | — |
| [SRC-1AE03B9EC3-L002156](../../agents/web_agent.py#L2156) | 2156 | `"                            results.append({"` | — |
| [SRC-1AE03B9EC3-L002157](../../agents/web_agent.py#L2157) | 2157 | `"                                \"title\": \"Instagram public hashtag: #\" + hashtag,"` | — |
| [SRC-1AE03B9EC3-L002158](../../agents/web_agent.py#L2158) | 2158 | `"                                \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L002159](../../agents/web_agent.py#L2159) | 2159 | `"                                \"snippet\": caption,"` | — |
| [SRC-1AE03B9EC3-L002160](../../agents/web_agent.py#L2160) | 2160 | `"                                \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L002161](../../agents/web_agent.py#L2161) | 2161 | `"                                \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L002162](../../agents/web_agent.py#L2162) | 2162 | `"                                \"provider\": \"instagram_graph_api\","` | — |
| [SRC-1AE03B9EC3-L002163](../../agents/web_agent.py#L2163) | 2163 | `"                                \"provider_rank\": len(["` | — |
| [SRC-1AE03B9EC3-L002164](../../agents/web_agent.py#L2164) | 2164 | `"                                    row for row in results"` | — |
| [SRC-1AE03B9EC3-L002165](../../agents/web_agent.py#L2165) | 2165 | `"                                    if row.get(\"provider\") == \"instagram_graph_api\""` | — |
| [SRC-1AE03B9EC3-L002166](../../agents/web_agent.py#L2166) | 2166 | `"                                ]) + 1,"` | — |
| [SRC-1AE03B9EC3-L002167](../../agents/web_agent.py#L2167) | 2167 | `"                                \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L002168](../../agents/web_agent.py#L2168) | 2168 | `"                                \"published_at\": _clean_text(item.get(\"timestamp\") or \"\", 100),"` | — |
| [SRC-1AE03B9EC3-L002169](../../agents/web_agent.py#L2169) | 2169 | `"                            })"` | — |
| [SRC-1AE03B9EC3-L002170](../../agents/web_agent.py#L2170) | 2170 | `"                    except (httpx.HTTPError, OSError, ValueError, KeyError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L002171](../../agents/web_agent.py#L2171) | 2171 | `"                        warnings.append(\"Instagram Graph API search failed for a requested hashtag.\")"` | — |
| [SRC-1AE03B9EC3-L002172](../../agents/web_agent.py#L2172) | 2172 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L002173](../../agents/web_agent.py#L2173) | 2173 | `"                warnings.append("` | — |
| [SRC-1AE03B9EC3-L002174](../../agents/web_agent.py#L2174) | 2174 | `"                    \"Instagram direct API is not configured; indexed public Instagram pages are still searched.\""` | — |
| [SRC-1AE03B9EC3-L002175](../../agents/web_agent.py#L2175) | 2175 | `"                )"` | — |
| [SRC-1AE03B9EC3-L002176](../../agents/web_agent.py#L2176) | 2176 | `""` | — |
| [SRC-1AE03B9EC3-L002177](../../agents/web_agent.py#L2177) | 2177 | `"        if \"x\" in platforms and os.getenv(\"X_BEARER_TOKEN\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L002178](../../agents/web_agent.py#L2178) | 2178 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L002179](../../agents/web_agent.py#L2179) | 2179 | `"                self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L002180](../../agents/web_agent.py#L2180) | 2180 | `"                response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L002181](../../agents/web_agent.py#L2181) | 2181 | `"                    \"https://api.x.com/2/tweets/search/recent\","` | — |
| [SRC-1AE03B9EC3-L002182](../../agents/web_agent.py#L2182) | 2182 | `"                    params={"` | — |
| [SRC-1AE03B9EC3-L002183](../../agents/web_agent.py#L2183) | 2183 | `"                        \"query\": query + \" -is:retweet\","` | — |
| [SRC-1AE03B9EC3-L002184](../../agents/web_agent.py#L2184) | 2184 | `"                        \"max_results\": 10,"` | — |
| [SRC-1AE03B9EC3-L002185](../../agents/web_agent.py#L2185) | 2185 | `"                        \"tweet.fields\": \"created_at,lang,public_metrics,author_id\","` | — |
| [SRC-1AE03B9EC3-L002186](../../agents/web_agent.py#L2186) | 2186 | `"                        \"expansions\": \"author_id\","` | — |
| [SRC-1AE03B9EC3-L002187](../../agents/web_agent.py#L2187) | 2187 | `"                        \"user.fields\": \"name,username\","` | — |
| [SRC-1AE03B9EC3-L002188](../../agents/web_agent.py#L2188) | 2188 | `"                    },"` | — |
| [SRC-1AE03B9EC3-L002189](../../agents/web_agent.py#L2189) | 2189 | `"                    headers={"` | — |
| [SRC-1AE03B9EC3-L002190](../../agents/web_agent.py#L2190) | 2190 | `"                        **headers,"` | — |
| [SRC-1AE03B9EC3-L002191](../../agents/web_agent.py#L2191) | 2191 | `"                        \"Authorization\": \"Bearer \" + os.getenv(\"X_BEARER_TOKEN\", \"\").strip(),"` | — |
| [SRC-1AE03B9EC3-L002192](../../agents/web_agent.py#L2192) | 2192 | `"                    },"` | — |
| [SRC-1AE03B9EC3-L002193](../../agents/web_agent.py#L2193) | 2193 | `"                    timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L002194](../../agents/web_agent.py#L2194) | 2194 | `"                    follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L002195](../../agents/web_agent.py#L2195) | 2195 | `"                )"` | — |
| [SRC-1AE03B9EC3-L002196](../../agents/web_agent.py#L2196) | 2196 | `"                if response.status_code == 200:"` | — |
| [SRC-1AE03B9EC3-L002197](../../agents/web_agent.py#L2197) | 2197 | `"                    data = response.json()"` | — |
| [SRC-1AE03B9EC3-L002198](../../agents/web_agent.py#L2198) | 2198 | `"                    authors = {"` | — |
| [SRC-1AE03B9EC3-L002199](../../agents/web_agent.py#L2199) | 2199 | `"                        user.get(\"id\"): user"` | — |
| [SRC-1AE03B9EC3-L002200](../../agents/web_agent.py#L2200) | 2200 | `"                        for user in data.get(\"includes\", {}).get(\"users\", [])"` | — |
| [SRC-1AE03B9EC3-L002201](../../agents/web_agent.py#L2201) | 2201 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L002202](../../agents/web_agent.py#L2202) | 2202 | `"                    for item in data.get(\"data\", []):"` | — |
| [SRC-1AE03B9EC3-L002203](../../agents/web_agent.py#L2203) | 2203 | `"                        author = authors.get(item.get(\"author_id\"), {})"` | — |
| [SRC-1AE03B9EC3-L002204](../../agents/web_agent.py#L2204) | 2204 | `"                        username = author.get(\"username\", \"\")"` | — |
| [SRC-1AE03B9EC3-L002205](../../agents/web_agent.py#L2205) | 2205 | `"                        post_id = item.get(\"id\", \"\")"` | — |
| [SRC-1AE03B9EC3-L002206](../../agents/web_agent.py#L2206) | 2206 | `"                        if not username or not post_id:"` | — |
| [SRC-1AE03B9EC3-L002207](../../agents/web_agent.py#L2207) | 2207 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002208](../../agents/web_agent.py#L2208) | 2208 | `"                        results.append({"` | — |
| [SRC-1AE03B9EC3-L002209](../../agents/web_agent.py#L2209) | 2209 | `"                            \"title\": _clean_text(author.get(\"name\") or username, 300),"` | — |
| [SRC-1AE03B9EC3-L002210](../../agents/web_agent.py#L2210) | 2210 | `"                            \"url\": f\"https://x.com/{username}/status/{post_id}\","` | — |
| [SRC-1AE03B9EC3-L002211](../../agents/web_agent.py#L2211) | 2211 | `"                            \"snippet\": _clean_text(item.get(\"text\") or \"\", 1200),"` | — |
| [SRC-1AE03B9EC3-L002212](../../agents/web_agent.py#L2212) | 2212 | `"                            \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L002213](../../agents/web_agent.py#L2213) | 2213 | `"                            \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L002214](../../agents/web_agent.py#L2214) | 2214 | `"                            \"provider\": \"x_official_api\","` | — |
| [SRC-1AE03B9EC3-L002215](../../agents/web_agent.py#L2215) | 2215 | `"                            \"provider_rank\": len(["` | — |
| [SRC-1AE03B9EC3-L002216](../../agents/web_agent.py#L2216) | 2216 | `"                                row for row in results"` | — |
| [SRC-1AE03B9EC3-L002217](../../agents/web_agent.py#L2217) | 2217 | `"                                if row.get(\"provider\") == \"x_official_api\""` | — |
| [SRC-1AE03B9EC3-L002218](../../agents/web_agent.py#L2218) | 2218 | `"                            ]) + 1,"` | — |
| [SRC-1AE03B9EC3-L002219](../../agents/web_agent.py#L2219) | 2219 | `"                            \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L002220](../../agents/web_agent.py#L2220) | 2220 | `"                            \"published_at\": _clean_text(item.get(\"created_at\") or \"\", 100),"` | — |
| [SRC-1AE03B9EC3-L002221](../../agents/web_agent.py#L2221) | 2221 | `"                        })"` | — |
| [SRC-1AE03B9EC3-L002222](../../agents/web_agent.py#L2222) | 2222 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L002223](../../agents/web_agent.py#L2223) | 2223 | `"                    warnings.append(f\"X API unavailable (HTTP {response.status_code})\")"` | — |
| [SRC-1AE03B9EC3-L002224](../../agents/web_agent.py#L2224) | 2224 | `"            except (httpx.HTTPError, OSError, ValueError, KeyError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L002225](../../agents/web_agent.py#L2225) | 2225 | `"                warnings.append(\"X API unavailable for this request\")"` | — |
| [SRC-1AE03B9EC3-L002226](../../agents/web_agent.py#L2226) | 2226 | `"        elif \"x\" in platforms:"` | — |
| [SRC-1AE03B9EC3-L002227](../../agents/web_agent.py#L2227) | 2227 | `"            warnings.append(\"X direct API is not configured; indexed public X pages are still searched.\")"` | — |
| [SRC-1AE03B9EC3-L002228](../../agents/web_agent.py#L2228) | 2228 | `""` | — |
| [SRC-1AE03B9EC3-L002229](../../agents/web_agent.py#L2229) | 2229 | `"        if \"youtube\" in platforms and os.getenv(\"YOUTUBE_API_KEY\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L002230](../../agents/web_agent.py#L2230) | 2230 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L002231](../../agents/web_agent.py#L2231) | 2231 | `"                self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L002232](../../agents/web_agent.py#L2232) | 2232 | `"                response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L002233](../../agents/web_agent.py#L2233) | 2233 | `"                    \"https://www.googleapis.com/youtube/v3/search\","` | — |
| [SRC-1AE03B9EC3-L002234](../../agents/web_agent.py#L2234) | 2234 | `"                    params={"` | — |
| [SRC-1AE03B9EC3-L002235](../../agents/web_agent.py#L2235) | 2235 | `"                        \"part\": \"snippet\","` | — |
| [SRC-1AE03B9EC3-L002236](../../agents/web_agent.py#L2236) | 2236 | `"                        \"q\": query,"` | — |
| [SRC-1AE03B9EC3-L002237](../../agents/web_agent.py#L2237) | 2237 | `"                        \"type\": \"video\","` | — |
| [SRC-1AE03B9EC3-L002238](../../agents/web_agent.py#L2238) | 2238 | `"                        \"maxResults\": 8,"` | — |
| [SRC-1AE03B9EC3-L002239](../../agents/web_agent.py#L2239) | 2239 | `"                        \"key\": os.getenv(\"YOUTUBE_API_KEY\", \"\").strip(),"` | — |
| [SRC-1AE03B9EC3-L002240](../../agents/web_agent.py#L2240) | 2240 | `"                    },"` | — |
| [SRC-1AE03B9EC3-L002241](../../agents/web_agent.py#L2241) | 2241 | `"                    headers=headers,"` | — |
| [SRC-1AE03B9EC3-L002242](../../agents/web_agent.py#L2242) | 2242 | `"                    timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L002243](../../agents/web_agent.py#L2243) | 2243 | `"                    follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L002244](../../agents/web_agent.py#L2244) | 2244 | `"                )"` | — |
| [SRC-1AE03B9EC3-L002245](../../agents/web_agent.py#L2245) | 2245 | `"                if response.status_code == 200:"` | — |
| [SRC-1AE03B9EC3-L002246](../../agents/web_agent.py#L2246) | 2246 | `"                    data = response.json()"` | — |
| [SRC-1AE03B9EC3-L002247](../../agents/web_agent.py#L2247) | 2247 | `"                    for item in data.get(\"items\", []):"` | — |
| [SRC-1AE03B9EC3-L002248](../../agents/web_agent.py#L2248) | 2248 | `"                        video_id = item.get(\"id\", {}).get(\"videoId\")"` | — |
| [SRC-1AE03B9EC3-L002249](../../agents/web_agent.py#L2249) | 2249 | `"                        snippet = item.get(\"snippet\", {})"` | — |
| [SRC-1AE03B9EC3-L002250](../../agents/web_agent.py#L2250) | 2250 | `"                        if not video_id:"` | — |
| [SRC-1AE03B9EC3-L002251](../../agents/web_agent.py#L2251) | 2251 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002252](../../agents/web_agent.py#L2252) | 2252 | `"                        results.append({"` | — |
| [SRC-1AE03B9EC3-L002253](../../agents/web_agent.py#L2253) | 2253 | `"                            \"title\": _clean_text(snippet.get(\"title\") or \"\", 300),"` | — |
| [SRC-1AE03B9EC3-L002254](../../agents/web_agent.py#L2254) | 2254 | `"                            \"url\": f\"https://www.youtube.com/watch?v={video_id}\","` | — |
| [SRC-1AE03B9EC3-L002255](../../agents/web_agent.py#L2255) | 2255 | `"                            \"snippet\": _clean_text(snippet.get(\"description\") or \"\", 1200),"` | — |
| [SRC-1AE03B9EC3-L002256](../../agents/web_agent.py#L2256) | 2256 | `"                            \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L002257](../../agents/web_agent.py#L2257) | 2257 | `"                            \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L002258](../../agents/web_agent.py#L2258) | 2258 | `"                            \"provider\": \"youtube_data_api\","` | — |
| [SRC-1AE03B9EC3-L002259](../../agents/web_agent.py#L2259) | 2259 | `"                            \"provider_rank\": len(["` | — |
| [SRC-1AE03B9EC3-L002260](../../agents/web_agent.py#L2260) | 2260 | `"                                row for row in results"` | — |
| [SRC-1AE03B9EC3-L002261](../../agents/web_agent.py#L2261) | 2261 | `"                                if row.get(\"provider\") == \"youtube_data_api\""` | — |
| [SRC-1AE03B9EC3-L002262](../../agents/web_agent.py#L2262) | 2262 | `"                            ]) + 1,"` | — |
| [SRC-1AE03B9EC3-L002263](../../agents/web_agent.py#L2263) | 2263 | `"                            \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L002264](../../agents/web_agent.py#L2264) | 2264 | `"                            \"published_at\": _clean_text(snippet.get(\"publishedAt\") or \"\", 100),"` | — |
| [SRC-1AE03B9EC3-L002265](../../agents/web_agent.py#L2265) | 2265 | `"                        })"` | — |
| [SRC-1AE03B9EC3-L002266](../../agents/web_agent.py#L2266) | 2266 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L002267](../../agents/web_agent.py#L2267) | 2267 | `"                    warnings.append(f\"YouTube Data API unavailable (HTTP {response.status_code})\")"` | — |
| [SRC-1AE03B9EC3-L002268](../../agents/web_agent.py#L2268) | 2268 | `"            except (httpx.HTTPError, OSError, ValueError, KeyError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L002269](../../agents/web_agent.py#L2269) | 2269 | `"                warnings.append(\"YouTube Data API unavailable for this request\")"` | — |
| [SRC-1AE03B9EC3-L002270](../../agents/web_agent.py#L2270) | 2270 | `"        elif \"youtube\" in platforms:"` | — |
| [SRC-1AE03B9EC3-L002271](../../agents/web_agent.py#L2271) | 2271 | `"            warnings.append(\"YouTube direct API is not configured; indexed public YouTube pages are still searched.\")"` | — |
| [SRC-1AE03B9EC3-L002272](../../agents/web_agent.py#L2272) | 2272 | `""` | — |
| [SRC-1AE03B9EC3-L002273](../../agents/web_agent.py#L2273) | 2273 | `"        return results, warnings"` | — |
| [SRC-1AE03B9EC3-L002274](../../agents/web_agent.py#L2274) | 2274 | `""` | — |
| [SRC-1AE03B9EC3-L002275](../../agents/web_agent.py#L2275) | 2275 | `"    def _fetch_page(self, url: str) -> tuple[str, str]:"` | — |
| [SRC-1AE03B9EC3-L002276](../../agents/web_agent.py#L2276) | 2276 | `"        \"\"\"Fetch a public page with bounded redirects and an inspectable extraction outcome.\"\"\""` | — |
| [SRC-1AE03B9EC3-L002277](../../agents/web_agent.py#L2277) | 2277 | `"        def result("` | — |
| [SRC-1AE03B9EC3-L002278](../../agents/web_agent.py#L2278) | 2278 | `"            title: str = \"\","` | — |
| [SRC-1AE03B9EC3-L002279](../../agents/web_agent.py#L2279) | 2279 | `"            page_text: str = \"\","` | — |
| [SRC-1AE03B9EC3-L002280](../../agents/web_agent.py#L2280) | 2280 | `"            status: str = \"unknown\","` | — |
| [SRC-1AE03B9EC3-L002281](../../agents/web_agent.py#L2281) | 2281 | `"            error_class: str \| None = None,"` | — |
| [SRC-1AE03B9EC3-L002282](../../agents/web_agent.py#L2282) | 2282 | `"        ) -> PageFetchResult:"` | — |
| [SRC-1AE03B9EC3-L002283](../../agents/web_agent.py#L2283) | 2283 | `"            return PageFetchResult(title, page_text, status, error_class)"` | — |
| [SRC-1AE03B9EC3-L002284](../../agents/web_agent.py#L2284) | 2284 | `""` | — |
| [SRC-1AE03B9EC3-L002285](../../agents/web_agent.py#L2285) | 2285 | `"        current_url = _public_http_url(url)"` | — |
| [SRC-1AE03B9EC3-L002286](../../agents/web_agent.py#L2286) | 2286 | `"        if not current_url:"` | — |
| [SRC-1AE03B9EC3-L002287](../../agents/web_agent.py#L2287) | 2287 | `"            return result(status=\"rejected_url\", error_class=\"PublicUrlRejected\")"` | — |
| [SRC-1AE03B9EC3-L002288](../../agents/web_agent.py#L2288) | 2288 | `"        budget = getattr(self, \"_request_budget\", None)"` | — |
| [SRC-1AE03B9EC3-L002289](../../agents/web_agent.py#L2289) | 2289 | `"        if budget is not None:"` | — |
| [SRC-1AE03B9EC3-L002290](../../agents/web_agent.py#L2290) | 2290 | `"            budget.reserve(\"page_fetches\")"` | — |
| [SRC-1AE03B9EC3-L002291](../../agents/web_agent.py#L2291) | 2291 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L002292](../../agents/web_agent.py#L2292) | 2292 | `"            import httpx"` | — |
| [SRC-1AE03B9EC3-L002293](../../agents/web_agent.py#L2293) | 2293 | `"            from bs4 import BeautifulSoup"` | — |
| [SRC-1AE03B9EC3-L002294](../../agents/web_agent.py#L2294) | 2294 | `"        except ImportError as exc:"` | — |
| [SRC-1AE03B9EC3-L002295](../../agents/web_agent.py#L2295) | 2295 | `"            raise AgentDependencyError("` | — |
| [SRC-1AE03B9EC3-L002296](../../agents/web_agent.py#L2296) | 2296 | `"                \"حزم استخراج الصفحات غير مثبتة. نفّذ: python -m pip install -e .\""` | — |
| [SRC-1AE03B9EC3-L002297](../../agents/web_agent.py#L2297) | 2297 | `"            ) from exc"` | — |
| [SRC-1AE03B9EC3-L002298](../../agents/web_agent.py#L2298) | 2298 | `""` | — |
| [SRC-1AE03B9EC3-L002299](../../agents/web_agent.py#L2299) | 2299 | `"        headers = {"` | — |
| [SRC-1AE03B9EC3-L002300](../../agents/web_agent.py#L2300) | 2300 | `"            \"User-Agent\": \"OmaraiResearchBot/1.1 (public page research; no login)\","` | — |
| [SRC-1AE03B9EC3-L002301](../../agents/web_agent.py#L2301) | 2301 | `"            \"Accept\": \"text/html,application/xhtml+xml,text/plain;q=0.8\","` | — |
| [SRC-1AE03B9EC3-L002302](../../agents/web_agent.py#L2302) | 2302 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002303](../../agents/web_agent.py#L2303) | 2303 | `"        media_type = \"\""` | — |
| [SRC-1AE03B9EC3-L002304](../../agents/web_agent.py#L2304) | 2304 | `"        html = \"\""` | — |
| [SRC-1AE03B9EC3-L002305](../../agents/web_agent.py#L2305) | 2305 | `"        bytes_truncated = False"` | — |
| [SRC-1AE03B9EC3-L002306](../../agents/web_agent.py#L2306) | 2306 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L002307](../../agents/web_agent.py#L2307) | 2307 | `"            with httpx.Client("` | — |
| [SRC-1AE03B9EC3-L002308](../../agents/web_agent.py#L2308) | 2308 | `"                timeout=self._effective_timeout(8.0),"` | — |
| [SRC-1AE03B9EC3-L002309](../../agents/web_agent.py#L2309) | 2309 | `"                follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L002310](../../agents/web_agent.py#L2310) | 2310 | `"                headers=headers,"` | — |
| [SRC-1AE03B9EC3-L002311](../../agents/web_agent.py#L2311) | 2311 | `"                verify=True,"` | — |
| [SRC-1AE03B9EC3-L002312](../../agents/web_agent.py#L2312) | 2312 | `"                trust_env=False,"` | — |
| [SRC-1AE03B9EC3-L002313](../../agents/web_agent.py#L2313) | 2313 | `"            ) as client:"` | — |
| [SRC-1AE03B9EC3-L002314](../../agents/web_agent.py#L2314) | 2314 | `"                for redirect_number in range(4):"` | — |
| [SRC-1AE03B9EC3-L002315](../../agents/web_agent.py#L2315) | 2315 | `"                    parsed = urllib.parse.urlparse(current_url)"` | — |
| [SRC-1AE03B9EC3-L002316](../../agents/web_agent.py#L2316) | 2316 | `"                    host = parsed.hostname or \"\""` | — |
| [SRC-1AE03B9EC3-L002317](../../agents/web_agent.py#L2317) | 2317 | `"                    # Resolve and pin a public IP. Do not let the HTTP client resolve"` | — |
| [SRC-1AE03B9EC3-L002318](../../agents/web_agent.py#L2318) | 2318 | `"                    # the original hostname a second time."` | — |
| [SRC-1AE03B9EC3-L002319](../../agents/web_agent.py#L2319) | 2319 | `"                    public_ips = _public_ip_literals(host)"` | — |
| [SRC-1AE03B9EC3-L002320](../../agents/web_agent.py#L2320) | 2320 | `"                    if not public_ips:"` | — |
| [SRC-1AE03B9EC3-L002321](../../agents/web_agent.py#L2321) | 2321 | `"                        return result(status=\"blocked_or_unresolved_host\", error_class=\"HostResolutionOrSSRFCheck\")"` | — |
| [SRC-1AE03B9EC3-L002322](../../agents/web_agent.py#L2322) | 2322 | `"                    connect_url = _pinned_connect_url(current_url, public_ips[0])"` | — |
| [SRC-1AE03B9EC3-L002323](../../agents/web_agent.py#L2323) | 2323 | `"                    if not connect_url:"` | — |
| [SRC-1AE03B9EC3-L002324](../../agents/web_agent.py#L2324) | 2324 | `"                        return result(status=\"blocked_connection_target\", error_class=\"PinnedTargetRejected\")"` | — |
| [SRC-1AE03B9EC3-L002325](../../agents/web_agent.py#L2325) | 2325 | `"                    request_headers = {\"Host\": host}"` | — |
| [SRC-1AE03B9EC3-L002326](../../agents/web_agent.py#L2326) | 2326 | `"                    extensions = {\"sni_hostname\": host} if parsed.scheme == \"https\" else {}"` | — |
| [SRC-1AE03B9EC3-L002327](../../agents/web_agent.py#L2327) | 2327 | `"                    with client.stream("` | — |
| [SRC-1AE03B9EC3-L002328](../../agents/web_agent.py#L2328) | 2328 | `"                        \"GET\","` | — |
| [SRC-1AE03B9EC3-L002329](../../agents/web_agent.py#L2329) | 2329 | `"                        connect_url,"` | — |
| [SRC-1AE03B9EC3-L002330](../../agents/web_agent.py#L2330) | 2330 | `"                        headers=request_headers,"` | — |
| [SRC-1AE03B9EC3-L002331](../../agents/web_agent.py#L2331) | 2331 | `"                        extensions=extensions,"` | — |
| [SRC-1AE03B9EC3-L002332](../../agents/web_agent.py#L2332) | 2332 | `"                    ) as response:"` | — |
| [SRC-1AE03B9EC3-L002333](../../agents/web_agent.py#L2333) | 2333 | `"                        if response.status_code in {301, 302, 303, 307, 308}:"` | — |
| [SRC-1AE03B9EC3-L002334](../../agents/web_agent.py#L2334) | 2334 | `"                            location = response.headers.get(\"location\", \"\")"` | — |
| [SRC-1AE03B9EC3-L002335](../../agents/web_agent.py#L2335) | 2335 | `"                            if not location or redirect_number >= 3:"` | — |
| [SRC-1AE03B9EC3-L002336](../../agents/web_agent.py#L2336) | 2336 | `"                                return result(status=\"redirect_failed\", error_class=\"RedirectLimitOrMissingLocation\")"` | — |
| [SRC-1AE03B9EC3-L002337](../../agents/web_agent.py#L2337) | 2337 | `"                            target = _public_http_url("` | — |
| [SRC-1AE03B9EC3-L002338](../../agents/web_agent.py#L2338) | 2338 | `"                                urllib.parse.urljoin(current_url, location)"` | — |
| [SRC-1AE03B9EC3-L002339](../../agents/web_agent.py#L2339) | 2339 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L002340](../../agents/web_agent.py#L2340) | 2340 | `"                            if not target:"` | — |
| [SRC-1AE03B9EC3-L002341](../../agents/web_agent.py#L2341) | 2341 | `"                                return result(status=\"redirect_rejected\", error_class=\"RedirectTargetRejected\")"` | — |
| [SRC-1AE03B9EC3-L002342](../../agents/web_agent.py#L2342) | 2342 | `"                            current_url = target"` | — |
| [SRC-1AE03B9EC3-L002343](../../agents/web_agent.py#L2343) | 2343 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002344](../../agents/web_agent.py#L2344) | 2344 | `"                        if response.status_code < 200 or response.status_code >= 300:"` | — |
| [SRC-1AE03B9EC3-L002345](../../agents/web_agent.py#L2345) | 2345 | `"                            return result(status=\"http_error\", error_class=\"HTTPStatus\")"` | — |
| [SRC-1AE03B9EC3-L002346](../../agents/web_agent.py#L2346) | 2346 | `"                        media_type = response.headers.get("` | — |
| [SRC-1AE03B9EC3-L002347](../../agents/web_agent.py#L2347) | 2347 | `"                            \"content-type\", \"\""` | — |
| [SRC-1AE03B9EC3-L002348](../../agents/web_agent.py#L2348) | 2348 | `"                        ).split(\";\")[0].lower()"` | — |
| [SRC-1AE03B9EC3-L002349](../../agents/web_agent.py#L2349) | 2349 | `"                        if media_type not in {"` | — |
| [SRC-1AE03B9EC3-L002350](../../agents/web_agent.py#L2350) | 2350 | `"                            \"text/html\", \"application/xhtml+xml\", \"text/plain\""` | — |
| [SRC-1AE03B9EC3-L002351](../../agents/web_agent.py#L2351) | 2351 | `"                        }:"` | — |
| [SRC-1AE03B9EC3-L002352](../../agents/web_agent.py#L2352) | 2352 | `"                            return result(status=\"unsupported_content_type\", error_class=\"UnsupportedContentType\")"` | — |
| [SRC-1AE03B9EC3-L002353](../../agents/web_agent.py#L2353) | 2353 | `"                        content_length = response.headers.get(\"content-length\")"` | — |
| [SRC-1AE03B9EC3-L002354](../../agents/web_agent.py#L2354) | 2354 | `"                        if content_length:"` | — |
| [SRC-1AE03B9EC3-L002355](../../agents/web_agent.py#L2355) | 2355 | `"                            try:"` | — |
| [SRC-1AE03B9EC3-L002356](../../agents/web_agent.py#L2356) | 2356 | `"                                if int(content_length) > MAX_PAGE_BYTES:"` | — |
| [SRC-1AE03B9EC3-L002357](../../agents/web_agent.py#L2357) | 2357 | `"                                    return result(status=\"page_too_large\", error_class=\"ContentLengthLimit\")"` | — |
| [SRC-1AE03B9EC3-L002358](../../agents/web_agent.py#L2358) | 2358 | `"                            except ValueError:"` | — |
| [SRC-1AE03B9EC3-L002359](../../agents/web_agent.py#L2359) | 2359 | `"                                pass"` | — |
| [SRC-1AE03B9EC3-L002360](../../agents/web_agent.py#L2360) | 2360 | `"                        chunks: list[bytes] = []"` | — |
| [SRC-1AE03B9EC3-L002361](../../agents/web_agent.py#L2361) | 2361 | `"                        count = 0"` | — |
| [SRC-1AE03B9EC3-L002362](../../agents/web_agent.py#L2362) | 2362 | `"                        for chunk in response.iter_bytes():"` | — |
| [SRC-1AE03B9EC3-L002363](../../agents/web_agent.py#L2363) | 2363 | `"                            count += len(chunk)"` | — |
| [SRC-1AE03B9EC3-L002364](../../agents/web_agent.py#L2364) | 2364 | `"                            if count > MAX_PAGE_BYTES:"` | — |
| [SRC-1AE03B9EC3-L002365](../../agents/web_agent.py#L2365) | 2365 | `"                                remaining = max(0, MAX_PAGE_BYTES - (count - len(chunk)))"` | — |
| [SRC-1AE03B9EC3-L002366](../../agents/web_agent.py#L2366) | 2366 | `"                                if remaining:"` | — |
| [SRC-1AE03B9EC3-L002367](../../agents/web_agent.py#L2367) | 2367 | `"                                    chunks.append(chunk[:remaining])"` | — |
| [SRC-1AE03B9EC3-L002368](../../agents/web_agent.py#L2368) | 2368 | `"                                bytes_truncated = True"` | — |
| [SRC-1AE03B9EC3-L002369](../../agents/web_agent.py#L2369) | 2369 | `"                                break"` | — |
| [SRC-1AE03B9EC3-L002370](../../agents/web_agent.py#L2370) | 2370 | `"                            chunks.append(chunk)"` | — |
| [SRC-1AE03B9EC3-L002371](../../agents/web_agent.py#L2371) | 2371 | `"                        raw = b\"\".join(chunks)"` | — |
| [SRC-1AE03B9EC3-L002372](../../agents/web_agent.py#L2372) | 2372 | `"                        encoding = response.encoding or \"utf-8\""` | — |
| [SRC-1AE03B9EC3-L002373](../../agents/web_agent.py#L2373) | 2373 | `"                        html = raw.decode(encoding, errors=\"replace\")"` | — |
| [SRC-1AE03B9EC3-L002374](../../agents/web_agent.py#L2374) | 2374 | `"                        break"` | — |
| [SRC-1AE03B9EC3-L002375](../../agents/web_agent.py#L2375) | 2375 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L002376](../../agents/web_agent.py#L2376) | 2376 | `"                    return result(status=\"redirect_limit\", error_class=\"RedirectLimit\")"` | — |
| [SRC-1AE03B9EC3-L002377](../../agents/web_agent.py#L2377) | 2377 | `"        except (OSError, ValueError, httpx.HTTPError) as exc:"` | — |
| [SRC-1AE03B9EC3-L002378](../../agents/web_agent.py#L2378) | 2378 | `"            return result(status=\"network_error\", error_class=type(exc).__name__)"` | — |
| [SRC-1AE03B9EC3-L002379](../../agents/web_agent.py#L2379) | 2379 | `""` | — |
| [SRC-1AE03B9EC3-L002380](../../agents/web_agent.py#L2380) | 2380 | `"        if media_type == \"text/plain\":"` | — |
| [SRC-1AE03B9EC3-L002381](../../agents/web_agent.py#L2381) | 2381 | `"            bounded_text = _clean_text(html, MAX_PAGE_TEXT_CHARS + 1)"` | — |
| [SRC-1AE03B9EC3-L002382](../../agents/web_agent.py#L2382) | 2382 | `"            text_truncated = len(bounded_text) > MAX_PAGE_TEXT_CHARS"` | — |
| [SRC-1AE03B9EC3-L002383](../../agents/web_agent.py#L2383) | 2383 | `"            page_text = _clean_text(bounded_text, MAX_PAGE_TEXT_CHARS)"` | — |
| [SRC-1AE03B9EC3-L002384](../../agents/web_agent.py#L2384) | 2384 | `"            status = ("` | — |
| [SRC-1AE03B9EC3-L002385](../../agents/web_agent.py#L2385) | 2385 | `"                \"empty_content\" if not page_text"` | — |
| [SRC-1AE03B9EC3-L002386](../../agents/web_agent.py#L2386) | 2386 | `"                else \"partial_extraction\" if bytes_truncated or text_truncated"` | — |
| [SRC-1AE03B9EC3-L002387](../../agents/web_agent.py#L2387) | 2387 | `"                else \"content_extracted\""` | — |
| [SRC-1AE03B9EC3-L002388](../../agents/web_agent.py#L2388) | 2388 | `"            )"` | — |
| [SRC-1AE03B9EC3-L002389](../../agents/web_agent.py#L2389) | 2389 | `"            return result(\"\", page_text, status)"` | — |
| [SRC-1AE03B9EC3-L002390](../../agents/web_agent.py#L2390) | 2390 | `""` | — |
| [SRC-1AE03B9EC3-L002391](../../agents/web_agent.py#L2391) | 2391 | `"        soup = BeautifulSoup(html, \"html.parser\")"` | — |
| [SRC-1AE03B9EC3-L002392](../../agents/web_agent.py#L2392) | 2392 | `"        title = _clean_text(soup.title.get_text(\" \", strip=True), 300) if soup.title else \"\""` | — |
| [SRC-1AE03B9EC3-L002393](../../agents/web_agent.py#L2393) | 2393 | `"        for element in soup(["` | — |
| [SRC-1AE03B9EC3-L002394](../../agents/web_agent.py#L2394) | 2394 | `"            \"script\", \"style\", \"nav\", \"footer\", \"header\", \"noscript\","` | — |
| [SRC-1AE03B9EC3-L002395](../../agents/web_agent.py#L2395) | 2395 | `"            \"svg\", \"form\", \"iframe\", \"template\""` | — |
| [SRC-1AE03B9EC3-L002396](../../agents/web_agent.py#L2396) | 2396 | `"        ]):"` | — |
| [SRC-1AE03B9EC3-L002397](../../agents/web_agent.py#L2397) | 2397 | `"            element.decompose()"` | — |
| [SRC-1AE03B9EC3-L002398](../../agents/web_agent.py#L2398) | 2398 | `"        main = soup.find(\"main\") or soup.find(\"article\") or soup.body or soup"` | — |
| [SRC-1AE03B9EC3-L002399](../../agents/web_agent.py#L2399) | 2399 | `"        bounded_text = _clean_text(main.get_text(\" \", strip=True), MAX_PAGE_TEXT_CHARS + 1)"` | — |
| [SRC-1AE03B9EC3-L002400](../../agents/web_agent.py#L2400) | 2400 | `"        text_truncated = len(bounded_text) > MAX_PAGE_TEXT_CHARS"` | — |
| [SRC-1AE03B9EC3-L002401](../../agents/web_agent.py#L2401) | 2401 | `"        page_text = _clean_text(bounded_text, MAX_PAGE_TEXT_CHARS)"` | — |
| [SRC-1AE03B9EC3-L002402](../../agents/web_agent.py#L2402) | 2402 | `"        status = ("` | — |
| [SRC-1AE03B9EC3-L002403](../../agents/web_agent.py#L2403) | 2403 | `"            \"no_text_extracted\" if not page_text"` | — |
| [SRC-1AE03B9EC3-L002404](../../agents/web_agent.py#L2404) | 2404 | `"            else \"partial_extraction\" if bytes_truncated or text_truncated"` | — |
| [SRC-1AE03B9EC3-L002405](../../agents/web_agent.py#L2405) | 2405 | `"            else \"content_extracted\""` | — |
| [SRC-1AE03B9EC3-L002406](../../agents/web_agent.py#L2406) | 2406 | `"        )"` | — |
| [SRC-1AE03B9EC3-L002407](../../agents/web_agent.py#L2407) | 2407 | `"        return result(title, page_text, status)"` | — |
| [SRC-1AE03B9EC3-L002408](../../agents/web_agent.py#L2408) | 2408 | `""` | — |
| [SRC-1AE03B9EC3-L002409](../../agents/web_agent.py#L2409) | 2409 | `"    def _collect_sources(self, query: str) -> tuple[list[dict[str, Any]], str \| None]:"` | — |
| [SRC-1AE03B9EC3-L002410](../../agents/web_agent.py#L2410) | 2410 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L002411](../../agents/web_agent.py#L2411) | 2411 | `"            sources = self._search_web(query)"` | — |
| [SRC-1AE03B9EC3-L002412](../../agents/web_agent.py#L2412) | 2412 | `"        except (RuntimeError, AgentDependencyError) as exc:"` | — |
| [SRC-1AE03B9EC3-L002413](../../agents/web_agent.py#L2413) | 2413 | `"            return [], str(exc)"` | — |
| [SRC-1AE03B9EC3-L002414](../../agents/web_agent.py#L2414) | 2414 | `"        for source in sources[:MAX_FETCHED_PAGES]:"` | — |
| [SRC-1AE03B9EC3-L002415](../../agents/web_agent.py#L2415) | 2415 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L002416](../../agents/web_agent.py#L2416) | 2416 | `"                title, page_text = self._fetch_page(source[\"url\"])"` | — |
| [SRC-1AE03B9EC3-L002417](../../agents/web_agent.py#L2417) | 2417 | `"            except (AgentDependencyError, RuntimeError):"` | — |
| [SRC-1AE03B9EC3-L002418](../../agents/web_agent.py#L2418) | 2418 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L002419](../../agents/web_agent.py#L2419) | 2419 | `"            if title:"` | — |
| [SRC-1AE03B9EC3-L002420](../../agents/web_agent.py#L2420) | 2420 | `"                source[\"title\"] = title"` | — |
| [SRC-1AE03B9EC3-L002421](../../agents/web_agent.py#L2421) | 2421 | `"            if page_text:"` | — |
| [SRC-1AE03B9EC3-L002422](../../agents/web_agent.py#L2422) | 2422 | `"                source[\"page_text\"] = page_text"` | — |
| [SRC-1AE03B9EC3-L002423](../../agents/web_agent.py#L2423) | 2423 | `"                source[\"page_fetched\"] = True"` | — |
| [SRC-1AE03B9EC3-L002424](../../agents/web_agent.py#L2424) | 2424 | `"                # Prefer extracted text over a thin search snippet."` | — |
| [SRC-1AE03B9EC3-L002425](../../agents/web_agent.py#L2425) | 2425 | `"                source[\"snippet\"] = page_text[:1800]"` | — |
| [SRC-1AE03B9EC3-L002426](../../agents/web_agent.py#L2426) | 2426 | `"        return sources, None"` | — |
| [SRC-1AE03B9EC3-L002427](../../agents/web_agent.py#L2427) | 2427 | `""` | — |
| [SRC-1AE03B9EC3-L002428](../../agents/web_agent.py#L2428) | 2428 | `"    def _collect_research("` | — |
| [SRC-1AE03B9EC3-L002429](../../agents/web_agent.py#L2429) | 2429 | `"        self, plan: dict[str, Any]"` | — |
| [SRC-1AE03B9EC3-L002430](../../agents/web_agent.py#L2430) | 2430 | `"    ) -> tuple[list[dict[str, Any]], list[str], dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L002431](../../agents/web_agent.py#L2431) | 2431 | `"        \"\"\"Run independent query searches concurrently, fuse evidence, then fetch top pages.\"\"\""` | — |
| [SRC-1AE03B9EC3-L002432](../../agents/web_agent.py#L2432) | 2432 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L002433](../../agents/web_agent.py#L2433) | 2433 | `"            query_limit = int(plan.get(\"query_limit\", MAX_PLAN_QUERIES))"` | — |
| [SRC-1AE03B9EC3-L002434](../../agents/web_agent.py#L2434) | 2434 | `"        except (TypeError, ValueError, OverflowError):"` | — |
| [SRC-1AE03B9EC3-L002435](../../agents/web_agent.py#L2435) | 2435 | `"            query_limit = MAX_PLAN_QUERIES"` | — |
| [SRC-1AE03B9EC3-L002436](../../agents/web_agent.py#L2436) | 2436 | `"        query_limit = max(1, min(query_limit, MAX_PLAN_QUERIES))"` | — |
| [SRC-1AE03B9EC3-L002437](../../agents/web_agent.py#L2437) | 2437 | `"        raw_queries = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L002438](../../agents/web_agent.py#L2438) | 2438 | `"            compact_search_query(query)"` | — |
| [SRC-1AE03B9EC3-L002439](../../agents/web_agent.py#L2439) | 2439 | `"            for query in plan.get(\"queries\", [])[:query_limit]"` | — |
| [SRC-1AE03B9EC3-L002440](../../agents/web_agent.py#L2440) | 2440 | `"            if isinstance(query, str) and query.strip()"` | — |
| [SRC-1AE03B9EC3-L002441](../../agents/web_agent.py#L2441) | 2441 | `"        ))"` | — |
| [SRC-1AE03B9EC3-L002442](../../agents/web_agent.py#L2442) | 2442 | `"        raw_queries = [query for query in raw_queries if query]"` | — |
| [SRC-1AE03B9EC3-L002443](../../agents/web_agent.py#L2443) | 2443 | `"        target_aspects = ["` | — |
| [SRC-1AE03B9EC3-L002444](../../agents/web_agent.py#L2444) | 2444 | `"            str(target).strip()[:120]"` | — |
| [SRC-1AE03B9EC3-L002445](../../agents/web_agent.py#L2445) | 2445 | `"            for target in (plan.get(\"coverage_targets\") or [])[:8]"` | — |
| [SRC-1AE03B9EC3-L002446](../../agents/web_agent.py#L2446) | 2446 | `"            if isinstance(target, str) and target.strip()"` | — |
| [SRC-1AE03B9EC3-L002447](../../agents/web_agent.py#L2447) | 2447 | `"        ]"` | — |
| [SRC-1AE03B9EC3-L002448](../../agents/web_agent.py#L2448) | 2448 | `"        # Reserve part of the existing query ceiling for evidence-gap repair."` | — |
| [SRC-1AE03B9EC3-L002449](../../agents/web_agent.py#L2449) | 2449 | `"        # This is a bounded retrieval loop, not an unbounded agent loop."` | — |
| [SRC-1AE03B9EC3-L002450](../../agents/web_agent.py#L2450) | 2450 | `"        repair_slot_limit = ("` | — |
| [SRC-1AE03B9EC3-L002451](../../agents/web_agent.py#L2451) | 2451 | `"            min(3, len(target_aspects), max(0, query_limit - 1))"` | — |
| [SRC-1AE03B9EC3-L002452](../../agents/web_agent.py#L2452) | 2452 | `"            if target_aspects else 0"` | — |
| [SRC-1AE03B9EC3-L002453](../../agents/web_agent.py#L2453) | 2453 | `"        )"` | — |
| [SRC-1AE03B9EC3-L002454](../../agents/web_agent.py#L2454) | 2454 | `"        initial_query_limit = max(1, query_limit - repair_slot_limit)"` | — |
| [SRC-1AE03B9EC3-L002455](../../agents/web_agent.py#L2455) | 2455 | `"        queries = raw_queries[:initial_query_limit]"` | — |
| [SRC-1AE03B9EC3-L002456](../../agents/web_agent.py#L2456) | 2456 | `"        warnings: list[str] = []"` | — |
| [SRC-1AE03B9EC3-L002457](../../agents/web_agent.py#L2457) | 2457 | `"        if not queries and not plan.get(\"direct_urls\"):"` | — |
| [SRC-1AE03B9EC3-L002458](../../agents/web_agent.py#L2458) | 2458 | `"            warnings.append(\"لم يُنشأ استعلام موضوعي قابل للبحث؛ لم تُستدعَ محركات البحث.\")"` | — |
| [SRC-1AE03B9EC3-L002459](../../agents/web_agent.py#L2459) | 2459 | `"        batches: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L002460](../../agents/web_agent.py#L2460) | 2460 | `"        query_counts: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L002461](../../agents/web_agent.py#L2461) | 2461 | `"        search_started_queries = 0"` | — |
| [SRC-1AE03B9EC3-L002462](../../agents/web_agent.py#L2462) | 2462 | `""` | — |
| [SRC-1AE03B9EC3-L002463](../../agents/web_agent.py#L2463) | 2463 | `"        if queries:"` | — |
| [SRC-1AE03B9EC3-L002464](../../agents/web_agent.py#L2464) | 2464 | `"            with ThreadPoolExecutor(max_workers=min(MAX_RESEARCH_WORKERS, len(queries))) as pool:"` | — |
| [SRC-1AE03B9EC3-L002465](../../agents/web_agent.py#L2465) | 2465 | `"                futures = {pool.submit(self._search_web, query): query for query in queries}"` | — |
| [SRC-1AE03B9EC3-L002466](../../agents/web_agent.py#L2466) | 2466 | `"                for future in as_completed(futures):"` | — |
| [SRC-1AE03B9EC3-L002467](../../agents/web_agent.py#L2467) | 2467 | `"                    query = futures[future]"` | — |
| [SRC-1AE03B9EC3-L002468](../../agents/web_agent.py#L2468) | 2468 | `"                    search_started_queries += 1"` | — |
| [SRC-1AE03B9EC3-L002469](../../agents/web_agent.py#L2469) | 2469 | `"                    try:"` | — |
| [SRC-1AE03B9EC3-L002470](../../agents/web_agent.py#L2470) | 2470 | `"                        results = future.result()"` | — |
| [SRC-1AE03B9EC3-L002471](../../agents/web_agent.py#L2471) | 2471 | `"                    except (RequestBudgetExceeded, RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L002472](../../agents/web_agent.py#L2472) | 2472 | `"                        warnings.append(f\"تعذر بحث الاستعلام «{query[:70]}»: {exc}\")"` | — |
| [SRC-1AE03B9EC3-L002473](../../agents/web_agent.py#L2473) | 2473 | `"                        query_counts.append({\"query\": query, \"results\": 0})"` | — |
| [SRC-1AE03B9EC3-L002474](../../agents/web_agent.py#L2474) | 2474 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L002475](../../agents/web_agent.py#L2475) | 2475 | `"                    query_counts.append({\"query\": query, \"results\": len(results)})"` | — |
| [SRC-1AE03B9EC3-L002476](../../agents/web_agent.py#L2476) | 2476 | `"                    grouped: dict[str, list[dict[str, Any]]] = {}"` | — |
| [SRC-1AE03B9EC3-L002477](../../agents/web_agent.py#L2477) | 2477 | `"                    for source in results:"` | — |
| [SRC-1AE03B9EC3-L002478](../../agents/web_agent.py#L2478) | 2478 | `"                        provider = str(source.get(\"provider\") or \"web_search\")"` | — |
| [SRC-1AE03B9EC3-L002479](../../agents/web_agent.py#L2479) | 2479 | `"                        grouped.setdefault(provider, []).append(source)"` | — |
| [SRC-1AE03B9EC3-L002480](../../agents/web_agent.py#L2480) | 2480 | `"                    for provider, items in grouped.items():"` | — |
| [SRC-1AE03B9EC3-L002481](../../agents/web_agent.py#L2481) | 2481 | `"                        items.sort(key=lambda item: int(item.get(\"provider_rank\", 999)))"` | — |
| [SRC-1AE03B9EC3-L002482](../../agents/web_agent.py#L2482) | 2482 | `"                        batches.append({\"query\": query, \"provider\": provider, \"results\": items})"` | — |
| [SRC-1AE03B9EC3-L002483](../../agents/web_agent.py#L2483) | 2483 | `""` | — |
| [SRC-1AE03B9EC3-L002484](../../agents/web_agent.py#L2484) | 2484 | `"        # Evidence-gap iteration: deep tasks get up to three targeted follow-up searches"` | — |
| [SRC-1AE03B9EC3-L002485](../../agents/web_agent.py#L2485) | 2485 | `"        # when initial coverage is thin. This uses observed source/domain/provider coverage,"` | — |
| [SRC-1AE03B9EC3-L002486](../../agents/web_agent.py#L2486) | 2486 | `"        # not the language model's subjective claim that it has enough evidence."` | — |
| [SRC-1AE03B9EC3-L002487](../../agents/web_agent.py#L2487) | 2487 | `"        preliminary = fuse_ranked_results(batches, limit=MAX_SEARCH_RESULTS)"` | — |
| [SRC-1AE03B9EC3-L002488](../../agents/web_agent.py#L2488) | 2488 | `"        preliminary_domains = {"` | — |
| [SRC-1AE03B9EC3-L002489](../../agents/web_agent.py#L2489) | 2489 | `"            registrable_domain(item.get(\"domain\") or urllib.parse.urlparse(item.get(\"url\", \"\")).hostname)"` | — |
| [SRC-1AE03B9EC3-L002490](../../agents/web_agent.py#L2490) | 2490 | `"            for item in preliminary"` | — |
| [SRC-1AE03B9EC3-L002491](../../agents/web_agent.py#L2491) | 2491 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002492](../../agents/web_agent.py#L2492) | 2492 | `"        preliminary_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L002493](../../agents/web_agent.py#L2493) | 2493 | `"        preliminary_providers = {"` | — |
| [SRC-1AE03B9EC3-L002494](../../agents/web_agent.py#L2494) | 2494 | `"            provider for item in preliminary for provider in item.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L002495](../../agents/web_agent.py#L2495) | 2495 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002496](../../agents/web_agent.py#L2496) | 2496 | `"        needs_expansion = ("` | — |
| [SRC-1AE03B9EC3-L002497](../../agents/web_agent.py#L2497) | 2497 | `"            plan.get(\"depth\") == \"deep\""` | — |
| [SRC-1AE03B9EC3-L002498](../../agents/web_agent.py#L2498) | 2498 | `"            and (len(preliminary) < 8 or len(preliminary_domains) < 5 or len(preliminary_providers) < 2)"` | — |
| [SRC-1AE03B9EC3-L002499](../../agents/web_agent.py#L2499) | 2499 | `"        )"` | — |
| [SRC-1AE03B9EC3-L002500](../../agents/web_agent.py#L2500) | 2500 | `"        preliminary_ledger = build_evidence_ledger(target_aspects, preliminary)"` | — |
| [SRC-1AE03B9EC3-L002501](../../agents/web_agent.py#L2501) | 2501 | `"        missing_aspects = list(preliminary_ledger.get(\"missing\") or [])"` | — |
| [SRC-1AE03B9EC3-L002502](../../agents/web_agent.py#L2502) | 2502 | `"        expansion_queries: list[str] = []"` | — |
| [SRC-1AE03B9EC3-L002503](../../agents/web_agent.py#L2503) | 2503 | `"        # Do not issue generic repairs when a standard task already has per-requirement queries."` | — |
| [SRC-1AE03B9EC3-L002504](../../agents/web_agent.py#L2504) | 2504 | `"        # Legacy plans without those query records still need the bounded missing-aspect fallback;"` | — |
| [SRC-1AE03B9EC3-L002505](../../agents/web_agent.py#L2505) | 2505 | `"        # deep research may expand further even after targeted queries."` | — |
| [SRC-1AE03B9EC3-L002506](../../agents/web_agent.py#L2506) | 2506 | `"        if ("` | — |
| [SRC-1AE03B9EC3-L002507](../../agents/web_agent.py#L2507) | 2507 | `"            (missing_aspects or needs_expansion)"` | — |
| [SRC-1AE03B9EC3-L002508](../../agents/web_agent.py#L2508) | 2508 | `"            and len(queries) < query_limit"` | — |
| [SRC-1AE03B9EC3-L002509](../../agents/web_agent.py#L2509) | 2509 | `"            and queries"` | — |
| [SRC-1AE03B9EC3-L002510](../../agents/web_agent.py#L2510) | 2510 | `"            and ("` | — |
| [SRC-1AE03B9EC3-L002511](../../agents/web_agent.py#L2511) | 2511 | `"                not plan.get(\"requirement_queries\")"` | — |
| [SRC-1AE03B9EC3-L002512](../../agents/web_agent.py#L2512) | 2512 | `"                or plan.get(\"depth\") == \"deep\""` | — |
| [SRC-1AE03B9EC3-L002513](../../agents/web_agent.py#L2513) | 2513 | `"            )"` | — |
| [SRC-1AE03B9EC3-L002514](../../agents/web_agent.py#L2514) | 2514 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L002515](../../agents/web_agent.py#L2515) | 2515 | `"            base_query = (queries[0] if queries else \"\")"` | — |
| [SRC-1AE03B9EC3-L002516](../../agents/web_agent.py#L2516) | 2516 | `"            remaining_slots = max(0, query_limit - len(queries))"` | — |
| [SRC-1AE03B9EC3-L002517](../../agents/web_agent.py#L2517) | 2517 | `"            aspect_queries = repair_queries_for_missing_aspects("` | — |
| [SRC-1AE03B9EC3-L002518](../../agents/web_agent.py#L2518) | 2518 | `"                base_query,"` | — |
| [SRC-1AE03B9EC3-L002519](../../agents/web_agent.py#L2519) | 2519 | `"                missing_aspects,"` | — |
| [SRC-1AE03B9EC3-L002520](../../agents/web_agent.py#L2520) | 2520 | `"                limit=min(repair_slot_limit, remaining_slots),"` | — |
| [SRC-1AE03B9EC3-L002521](../../agents/web_agent.py#L2521) | 2521 | `"                compact_fn=compact_search_query,"` | — |
| [SRC-1AE03B9EC3-L002522](../../agents/web_agent.py#L2522) | 2522 | `"            )"` | — |
| [SRC-1AE03B9EC3-L002523](../../agents/web_agent.py#L2523) | 2523 | `"            candidates = list(aspect_queries)"` | — |
| [SRC-1AE03B9EC3-L002524](../../agents/web_agent.py#L2524) | 2524 | `"            if needs_expansion:"` | — |
| [SRC-1AE03B9EC3-L002525](../../agents/web_agent.py#L2525) | 2525 | `"                candidates.extend(["` | — |
| [SRC-1AE03B9EC3-L002526](../../agents/web_agent.py#L2526) | 2526 | `"                    f\"{base_query} official sources data reports\","` | — |
| [SRC-1AE03B9EC3-L002527](../../agents/web_agent.py#L2527) | 2527 | `"                    f\"{base_query} limitations risks criticism alternatives\","` | — |
| [SRC-1AE03B9EC3-L002528](../../agents/web_agent.py#L2528) | 2528 | `"                    f\"{base_query} recent developments case studies analysis\","` | — |
| [SRC-1AE03B9EC3-L002529](../../agents/web_agent.py#L2529) | 2529 | `"                ])"` | — |
| [SRC-1AE03B9EC3-L002530](../../agents/web_agent.py#L2530) | 2530 | `"            existing = {item.casefold() for item in queries}"` | — |
| [SRC-1AE03B9EC3-L002531](../../agents/web_agent.py#L2531) | 2531 | `"            expansion_queries = []"` | — |
| [SRC-1AE03B9EC3-L002532](../../agents/web_agent.py#L2532) | 2532 | `"            seen_expansions = set(existing)"` | — |
| [SRC-1AE03B9EC3-L002533](../../agents/web_agent.py#L2533) | 2533 | `"            for candidate in candidates:"` | — |
| [SRC-1AE03B9EC3-L002534](../../agents/web_agent.py#L2534) | 2534 | `"                compacted = compact_search_query(candidate)"` | — |
| [SRC-1AE03B9EC3-L002535](../../agents/web_agent.py#L2535) | 2535 | `"                key = compacted.casefold()"` | — |
| [SRC-1AE03B9EC3-L002536](../../agents/web_agent.py#L2536) | 2536 | `"                if compacted and key not in seen_expansions:"` | — |
| [SRC-1AE03B9EC3-L002537](../../agents/web_agent.py#L2537) | 2537 | `"                    expansion_queries.append(compacted)"` | — |
| [SRC-1AE03B9EC3-L002538](../../agents/web_agent.py#L2538) | 2538 | `"                    seen_expansions.add(key)"` | — |
| [SRC-1AE03B9EC3-L002539](../../agents/web_agent.py#L2539) | 2539 | `"                if len(expansion_queries) >= remaining_slots:"` | — |
| [SRC-1AE03B9EC3-L002540](../../agents/web_agent.py#L2540) | 2540 | `"                    break"` | — |
| [SRC-1AE03B9EC3-L002541](../../agents/web_agent.py#L2541) | 2541 | `"            if expansion_queries:"` | — |
| [SRC-1AE03B9EC3-L002542](../../agents/web_agent.py#L2542) | 2542 | `"                with ThreadPoolExecutor("` | — |
| [SRC-1AE03B9EC3-L002543](../../agents/web_agent.py#L2543) | 2543 | `"                    max_workers=min(MAX_RESEARCH_WORKERS, len(expansion_queries))"` | — |
| [SRC-1AE03B9EC3-L002544](../../agents/web_agent.py#L2544) | 2544 | `"                ) as pool:"` | — |
| [SRC-1AE03B9EC3-L002545](../../agents/web_agent.py#L2545) | 2545 | `"                    futures = {"` | — |
| [SRC-1AE03B9EC3-L002546](../../agents/web_agent.py#L2546) | 2546 | `"                        pool.submit(self._search_web, query): query"` | — |
| [SRC-1AE03B9EC3-L002547](../../agents/web_agent.py#L2547) | 2547 | `"                        for query in expansion_queries"` | — |
| [SRC-1AE03B9EC3-L002548](../../agents/web_agent.py#L2548) | 2548 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L002549](../../agents/web_agent.py#L2549) | 2549 | `"                    for future in as_completed(futures):"` | — |
| [SRC-1AE03B9EC3-L002550](../../agents/web_agent.py#L2550) | 2550 | `"                        query = futures[future]"` | — |
| [SRC-1AE03B9EC3-L002551](../../agents/web_agent.py#L2551) | 2551 | `"                        search_started_queries += 1"` | — |
| [SRC-1AE03B9EC3-L002552](../../agents/web_agent.py#L2552) | 2552 | `"                        try:"` | — |
| [SRC-1AE03B9EC3-L002553](../../agents/web_agent.py#L2553) | 2553 | `"                            results = future.result()"` | — |
| [SRC-1AE03B9EC3-L002554](../../agents/web_agent.py#L2554) | 2554 | `"                        except (RequestBudgetExceeded, RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L002555](../../agents/web_agent.py#L2555) | 2555 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L002556](../../agents/web_agent.py#L2556) | 2556 | `"                                f\"تعذر بحث زاوية إضافية «{query[:70]}»: {exc}\""` | — |
| [SRC-1AE03B9EC3-L002557](../../agents/web_agent.py#L2557) | 2557 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L002558](../../agents/web_agent.py#L2558) | 2558 | `"                            query_counts.append({\"query\": query, \"results\": 0})"` | — |
| [SRC-1AE03B9EC3-L002559](../../agents/web_agent.py#L2559) | 2559 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002560](../../agents/web_agent.py#L2560) | 2560 | `"                        query_counts.append({\"query\": query, \"results\": len(results)})"` | — |
| [SRC-1AE03B9EC3-L002561](../../agents/web_agent.py#L2561) | 2561 | `"                        grouped: dict[str, list[dict[str, Any]]] = {}"` | — |
| [SRC-1AE03B9EC3-L002562](../../agents/web_agent.py#L2562) | 2562 | `"                        for source in results:"` | — |
| [SRC-1AE03B9EC3-L002563](../../agents/web_agent.py#L2563) | 2563 | `"                            grouped.setdefault("` | — |
| [SRC-1AE03B9EC3-L002564](../../agents/web_agent.py#L2564) | 2564 | `"                                str(source.get(\"provider\") or \"web_search\"), []"` | — |
| [SRC-1AE03B9EC3-L002565](../../agents/web_agent.py#L2565) | 2565 | `"                            ).append(source)"` | — |
| [SRC-1AE03B9EC3-L002566](../../agents/web_agent.py#L2566) | 2566 | `"                        for provider, items in grouped.items():"` | — |
| [SRC-1AE03B9EC3-L002567](../../agents/web_agent.py#L2567) | 2567 | `"                            items.sort(key=lambda item: int(item.get(\"provider_rank\", 999)))"` | — |
| [SRC-1AE03B9EC3-L002568](../../agents/web_agent.py#L2568) | 2568 | `"                            batches.append({"` | — |
| [SRC-1AE03B9EC3-L002569](../../agents/web_agent.py#L2569) | 2569 | `"                                \"query\": query, \"provider\": provider, \"results\": items"` | — |
| [SRC-1AE03B9EC3-L002570](../../agents/web_agent.py#L2570) | 2570 | `"                            })"` | — |
| [SRC-1AE03B9EC3-L002571](../../agents/web_agent.py#L2571) | 2571 | `"                queries.extend(expansion_queries)"` | — |
| [SRC-1AE03B9EC3-L002572](../../agents/web_agent.py#L2572) | 2572 | `"        # Report queries actually selected, not planned queries skipped to reserve repair capacity."` | — |
| [SRC-1AE03B9EC3-L002573](../../agents/web_agent.py#L2573) | 2573 | `"        plan[\"queries\"] = list(dict.fromkeys(queries))"` | — |
| [SRC-1AE03B9EC3-L002574](../../agents/web_agent.py#L2574) | 2574 | `""` | — |
| [SRC-1AE03B9EC3-L002575](../../agents/web_agent.py#L2575) | 2575 | `"        # Google News RSS is included concurrently by _search_web for freshness-bearing queries."` | — |
| [SRC-1AE03B9EC3-L002576](../../agents/web_agent.py#L2576) | 2576 | `""` | — |
| [SRC-1AE03B9EC3-L002577](../../agents/web_agent.py#L2577) | 2577 | `"        # A social-focused task uses public social endpoints in parallel with indexed"` | — |
| [SRC-1AE03B9EC3-L002578](../../agents/web_agent.py#L2578) | 2578 | `"        # public pages. No login, private profile, session cookie or anti-bot bypass."` | — |
| [SRC-1AE03B9EC3-L002579](../../agents/web_agent.py#L2579) | 2579 | `"        social_results: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L002580](../../agents/web_agent.py#L2580) | 2580 | `"        if plan.get(\"social_focus\") and queries:"` | — |
| [SRC-1AE03B9EC3-L002581](../../agents/web_agent.py#L2581) | 2581 | `"            requested_platforms = plan.get(\"platforms\") or []"` | — |
| [SRC-1AE03B9EC3-L002582](../../agents/web_agent.py#L2582) | 2582 | `"            if requested_platforms:"` | — |
| [SRC-1AE03B9EC3-L002583](../../agents/web_agent.py#L2583) | 2583 | `"                platforms = list(dict.fromkeys(requested_platforms))"` | — |
| [SRC-1AE03B9EC3-L002584](../../agents/web_agent.py#L2584) | 2584 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L002585](../../agents/web_agent.py#L2585) | 2585 | `"                # Broad social research: always try no-key public sources, and add"` | — |
| [SRC-1AE03B9EC3-L002586](../../agents/web_agent.py#L2586) | 2586 | `"                # official platform connectors only when they are configured."` | — |
| [SRC-1AE03B9EC3-L002587](../../agents/web_agent.py#L2587) | 2587 | `"                platforms = [\"reddit\", \"bluesky\"]"` | — |
| [SRC-1AE03B9EC3-L002588](../../agents/web_agent.py#L2588) | 2588 | `"                optional_connectors = {"` | — |
| [SRC-1AE03B9EC3-L002589](../../agents/web_agent.py#L2589) | 2589 | `"                    \"facebook\": bool("` | — |
| [SRC-1AE03B9EC3-L002590](../../agents/web_agent.py#L2590) | 2590 | `"                        os.getenv(\"FACEBOOK_PAGE_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L002591](../../agents/web_agent.py#L2591) | 2591 | `"                        and os.getenv(\"FACEBOOK_PAGE_IDS\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L002592](../../agents/web_agent.py#L2592) | 2592 | `"                    ),"` | — |
| [SRC-1AE03B9EC3-L002593](../../agents/web_agent.py#L2593) | 2593 | `"                    \"instagram\": bool("` | — |
| [SRC-1AE03B9EC3-L002594](../../agents/web_agent.py#L2594) | 2594 | `"                        os.getenv(\"INSTAGRAM_USER_ID\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L002595](../../agents/web_agent.py#L2595) | 2595 | `"                        and os.getenv(\"INSTAGRAM_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L002596](../../agents/web_agent.py#L2596) | 2596 | `"                    ),"` | — |
| [SRC-1AE03B9EC3-L002597](../../agents/web_agent.py#L2597) | 2597 | `"                    \"x\": bool(os.getenv(\"X_BEARER_TOKEN\", \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L002598](../../agents/web_agent.py#L2598) | 2598 | `"                    \"youtube\": bool(os.getenv(\"YOUTUBE_API_KEY\", \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L002599](../../agents/web_agent.py#L2599) | 2599 | `"                }"` | — |
| [SRC-1AE03B9EC3-L002600](../../agents/web_agent.py#L2600) | 2600 | `"                platforms.extend("` | — |
| [SRC-1AE03B9EC3-L002601](../../agents/web_agent.py#L2601) | 2601 | `"                    name for name, ready in optional_connectors.items()"` | — |
| [SRC-1AE03B9EC3-L002602](../../agents/web_agent.py#L2602) | 2602 | `"                    if ready and name not in platforms"` | — |
| [SRC-1AE03B9EC3-L002603](../../agents/web_agent.py#L2603) | 2603 | `"                )"` | — |
| [SRC-1AE03B9EC3-L002604](../../agents/web_agent.py#L2604) | 2604 | `"            social_results, social_warnings = self._search_social((queries[0] if queries else \"\"), platforms)"` | — |
| [SRC-1AE03B9EC3-L002605](../../agents/web_agent.py#L2605) | 2605 | `"            warnings.extend(social_warnings)"` | — |
| [SRC-1AE03B9EC3-L002606](../../agents/web_agent.py#L2606) | 2606 | `"            social_groups: dict[str, list[dict[str, Any]]] = {}"` | — |
| [SRC-1AE03B9EC3-L002607](../../agents/web_agent.py#L2607) | 2607 | `"            for source in social_results:"` | — |
| [SRC-1AE03B9EC3-L002608](../../agents/web_agent.py#L2608) | 2608 | `"                social_groups.setdefault(str(source.get(\"provider\") or \"social\"), []).append(source)"` | — |
| [SRC-1AE03B9EC3-L002609](../../agents/web_agent.py#L2609) | 2609 | `"            for provider, items in social_groups.items():"` | — |
| [SRC-1AE03B9EC3-L002610](../../agents/web_agent.py#L2610) | 2610 | `"                items.sort(key=lambda item: int(item.get(\"provider_rank\", 999)))"` | — |
| [SRC-1AE03B9EC3-L002611](../../agents/web_agent.py#L2611) | 2611 | `"                batches.append({\"query\": (queries[0] if queries else \"\"), \"provider\": provider, \"results\": items})"` | — |
| [SRC-1AE03B9EC3-L002612](../../agents/web_agent.py#L2612) | 2612 | `""` | — |
| [SRC-1AE03B9EC3-L002613](../../agents/web_agent.py#L2613) | 2613 | `"        # Explicit URLs are first-class inputs: fetch the page the user actually asked about"` | — |
| [SRC-1AE03B9EC3-L002614](../../agents/web_agent.py#L2614) | 2614 | `"        # instead of relying on a search engine to rediscover it. URL and DNS checks still apply."` | — |
| [SRC-1AE03B9EC3-L002615](../../agents/web_agent.py#L2615) | 2615 | `"        direct_urls: list[str] = []"` | — |
| [SRC-1AE03B9EC3-L002616](../../agents/web_agent.py#L2616) | 2616 | `"        for value in plan.get(\"direct_urls\", [])[:5]:"` | — |
| [SRC-1AE03B9EC3-L002617](../../agents/web_agent.py#L2617) | 2617 | `"            safe_url = _public_http_url(value)"` | — |
| [SRC-1AE03B9EC3-L002618](../../agents/web_agent.py#L2618) | 2618 | `"            if safe_url and not _blocked_source_url(safe_url) and safe_url not in direct_urls:"` | — |
| [SRC-1AE03B9EC3-L002619](../../agents/web_agent.py#L2619) | 2619 | `"                direct_urls.append(safe_url)"` | — |
| [SRC-1AE03B9EC3-L002620](../../agents/web_agent.py#L2620) | 2620 | `"        for direct_url in direct_urls:"` | — |
| [SRC-1AE03B9EC3-L002621](../../agents/web_agent.py#L2621) | 2621 | `"            batches.append({"` | — |
| [SRC-1AE03B9EC3-L002622](../../agents/web_agent.py#L2622) | 2622 | `"                \"query\": (queries[0] if queries else \"\"),"` | — |
| [SRC-1AE03B9EC3-L002623](../../agents/web_agent.py#L2623) | 2623 | `"                \"provider\": \"user_supplied_url\","` | — |
| [SRC-1AE03B9EC3-L002624](../../agents/web_agent.py#L2624) | 2624 | `"                \"results\": [{"` | — |
| [SRC-1AE03B9EC3-L002625](../../agents/web_agent.py#L2625) | 2625 | `"                    \"title\": \"رابط قدمه المستخدم للتحليل\","` | — |
| [SRC-1AE03B9EC3-L002626](../../agents/web_agent.py#L2626) | 2626 | `"                    \"url\": direct_url,"` | — |
| [SRC-1AE03B9EC3-L002627](../../agents/web_agent.py#L2627) | 2627 | `"                    \"snippet\": \"\","` | — |
| [SRC-1AE03B9EC3-L002628](../../agents/web_agent.py#L2628) | 2628 | `"                    \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L002629](../../agents/web_agent.py#L2629) | 2629 | `"                    \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L002630](../../agents/web_agent.py#L2630) | 2630 | `"                    \"provider\": \"user_supplied_url\","` | — |
| [SRC-1AE03B9EC3-L002631](../../agents/web_agent.py#L2631) | 2631 | `"                    \"provider_rank\": 1,"` | — |
| [SRC-1AE03B9EC3-L002632](../../agents/web_agent.py#L2632) | 2632 | `"                    \"search_query\": (queries[0] if queries else \"\"),"` | — |
| [SRC-1AE03B9EC3-L002633](../../agents/web_agent.py#L2633) | 2633 | `"                    \"published_at\": \"\","` | — |
| [SRC-1AE03B9EC3-L002634](../../agents/web_agent.py#L2634) | 2634 | `"                }],"` | — |
| [SRC-1AE03B9EC3-L002635](../../agents/web_agent.py#L2635) | 2635 | `"            })"` | — |
| [SRC-1AE03B9EC3-L002636](../../agents/web_agent.py#L2636) | 2636 | `""` | — |
| [SRC-1AE03B9EC3-L002637](../../agents/web_agent.py#L2637) | 2637 | `"        raw_results_count = sum(len(batch.get(\"results\", [])) for batch in batches if isinstance(batch, dict) and isinstance(batch.get(\"results\", []), list))"` | — |
| [SRC-1AE03B9EC3-L002638](../../agents/web_agent.py#L2638) | 2638 | `"        sources = fuse_ranked_results(batches, limit=MAX_SEARCH_RESULTS)"` | — |
| [SRC-1AE03B9EC3-L002639](../../agents/web_agent.py#L2639) | 2639 | `""` | — |
| [SRC-1AE03B9EC3-L002640](../../agents/web_agent.py#L2640) | 2640 | `"        # Keep at least one returned source per explicit criterion query in the"` | — |
| [SRC-1AE03B9EC3-L002641](../../agents/web_agent.py#L2641) | 2641 | `"        # bounded source set sent to synthesis. Global fusion can otherwise crowd"` | — |
| [SRC-1AE03B9EC3-L002642](../../agents/web_agent.py#L2642) | 2642 | `"        # lower-ranked criterion results out before the model can inspect them."` | — |
| [SRC-1AE03B9EC3-L002643](../../agents/web_agent.py#L2643) | 2643 | `"        requirement_queries = plan.get(\"requirement_queries\", [])"` | — |
| [SRC-1AE03B9EC3-L002644](../../agents/web_agent.py#L2644) | 2644 | `"        if isinstance(requirement_queries, list) and requirement_queries:"` | — |
| [SRC-1AE03B9EC3-L002645](../../agents/web_agent.py#L2645) | 2645 | `"            globally_fused = sources"` | — |
| [SRC-1AE03B9EC3-L002646](../../agents/web_agent.py#L2646) | 2646 | `"            globally_fused_by_url = {"` | — |
| [SRC-1AE03B9EC3-L002647](../../agents/web_agent.py#L2647) | 2647 | `"                self._normalized_source_url_key(item.get(\"url\", \"\")): item"` | — |
| [SRC-1AE03B9EC3-L002648](../../agents/web_agent.py#L2648) | 2648 | `"                for item in globally_fused"` | — |
| [SRC-1AE03B9EC3-L002649](../../agents/web_agent.py#L2649) | 2649 | `"                if self._normalized_source_url_key(item.get(\"url\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L002650](../../agents/web_agent.py#L2650) | 2650 | `"            }"` | — |
| [SRC-1AE03B9EC3-L002651](../../agents/web_agent.py#L2651) | 2651 | `"            pinned_by_url: dict[str, dict[str, Any]] = {}"` | — |
| [SRC-1AE03B9EC3-L002652](../../agents/web_agent.py#L2652) | 2652 | `"            pinned_sources: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L002653](../../agents/web_agent.py#L2653) | 2653 | `"            for requirement in requirement_queries[:MAX_PLAN_QUERIES]:"` | — |
| [SRC-1AE03B9EC3-L002654](../../agents/web_agent.py#L2654) | 2654 | `"                if not isinstance(requirement, dict):"` | — |
| [SRC-1AE03B9EC3-L002655](../../agents/web_agent.py#L2655) | 2655 | `"                    continue"` | — |
| [SRC-1AE03B9EC3-L002656](../../agents/web_agent.py#L2656) | 2656 | `"                target_query = compact_search_query(str(requirement.get(\"query\") or \"\"))"` | — |
| [SRC-1AE03B9EC3-L002657](../../agents/web_agent.py#L2657) | 2657 | `"                if not target_query:"` | — |
| [SRC-1AE03B9EC3-L002658](../../agents/web_agent.py#L2658) | 2658 | `"                    continue"` | — |
| [SRC-1AE03B9EC3-L002659](../../agents/web_agent.py#L2659) | 2659 | `"                query_key = re.sub(r\"\\s+\", \" \", target_query).strip().casefold()"` | — |
| [SRC-1AE03B9EC3-L002660](../../agents/web_agent.py#L2660) | 2660 | `"                criterion_batches = ["` | — |
| [SRC-1AE03B9EC3-L002661](../../agents/web_agent.py#L2661) | 2661 | `"                    batch for batch in batches"` | — |
| [SRC-1AE03B9EC3-L002662](../../agents/web_agent.py#L2662) | 2662 | `"                    if re.sub("` | — |
| [SRC-1AE03B9EC3-L002663](../../agents/web_agent.py#L2663) | 2663 | `"                        r\"\\s+\", \" \", str(batch.get(\"query\") or \"\")"` | — |
| [SRC-1AE03B9EC3-L002664](../../agents/web_agent.py#L2664) | 2664 | `"                    ).strip().casefold() == query_key"` | — |
| [SRC-1AE03B9EC3-L002665](../../agents/web_agent.py#L2665) | 2665 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L002666](../../agents/web_agent.py#L2666) | 2666 | `"                criterion_candidates = fuse_ranked_results("` | — |
| [SRC-1AE03B9EC3-L002667](../../agents/web_agent.py#L2667) | 2667 | `"                    criterion_batches, limit=MAX_SEARCH_RESULTS"` | — |
| [SRC-1AE03B9EC3-L002668](../../agents/web_agent.py#L2668) | 2668 | `"                )"` | — |
| [SRC-1AE03B9EC3-L002669](../../agents/web_agent.py#L2669) | 2669 | `"                candidate = None"` | — |
| [SRC-1AE03B9EC3-L002670](../../agents/web_agent.py#L2670) | 2670 | `"                if criterion_candidates:"` | — |
| [SRC-1AE03B9EC3-L002671](../../agents/web_agent.py#L2671) | 2671 | `"                    criterion_ledger = build_requirement_evidence_ledger("` | — |
| [SRC-1AE03B9EC3-L002672](../../agents/web_agent.py#L2672) | 2672 | `"                        [str(requirement.get(\"target\") or \"\")],"` | — |
| [SRC-1AE03B9EC3-L002673](../../agents/web_agent.py#L2673) | 2673 | `"                        criterion_candidates,"` | — |
| [SRC-1AE03B9EC3-L002674](../../agents/web_agent.py#L2674) | 2674 | `"                        [requirement],"` | — |
| [SRC-1AE03B9EC3-L002675](../../agents/web_agent.py#L2675) | 2675 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L002676](../../agents/web_agent.py#L2676) | 2676 | `"                    candidate_indexes = ("` | — |
| [SRC-1AE03B9EC3-L002677](../../agents/web_agent.py#L2677) | 2677 | `"                        criterion_ledger[0].get(\"candidate_source_indexes\", [])"` | — |
| [SRC-1AE03B9EC3-L002678](../../agents/web_agent.py#L2678) | 2678 | `"                        if criterion_ledger else []"` | — |
| [SRC-1AE03B9EC3-L002679](../../agents/web_agent.py#L2679) | 2679 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L002680](../../agents/web_agent.py#L2680) | 2680 | `"                    if candidate_indexes:"` | — |
| [SRC-1AE03B9EC3-L002681](../../agents/web_agent.py#L2681) | 2681 | `"                        candidate = criterion_candidates[int(candidate_indexes[0]) - 1]"` | — |
| [SRC-1AE03B9EC3-L002682](../../agents/web_agent.py#L2682) | 2682 | `"                if candidate is None:"` | — |
