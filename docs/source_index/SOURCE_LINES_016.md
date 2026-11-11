# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **016**
- سجلات الأسطر: **800**
- النطاق: SRC-1AE03B9EC3-L002811 إلى SRC-1AE03B9EC3-L003610
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-1AE03B9EC3 — [agents/web_agent.py](../../agents/web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1AE03B9EC3-L002811](../../agents/web_agent.py#L2811) | 2811 | `"                    follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L002812](../../agents/web_agent.py#L2812) | 2812 | `"                )"` | — |
| [SRC-1AE03B9EC3-L002813](../../agents/web_agent.py#L2813) | 2813 | `"                if response.status_code == 200:"` | — |
| [SRC-1AE03B9EC3-L002814](../../agents/web_agent.py#L2814) | 2814 | `"                    data = response.json()"` | — |
| [SRC-1AE03B9EC3-L002815](../../agents/web_agent.py#L2815) | 2815 | `"                    authors = {"` | — |
| [SRC-1AE03B9EC3-L002816](../../agents/web_agent.py#L2816) | 2816 | `"                        user.get(\"id\"): user"` | — |
| [SRC-1AE03B9EC3-L002817](../../agents/web_agent.py#L2817) | 2817 | `"                        for user in data.get(\"includes\", {}).get(\"users\", [])"` | — |
| [SRC-1AE03B9EC3-L002818](../../agents/web_agent.py#L2818) | 2818 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L002819](../../agents/web_agent.py#L2819) | 2819 | `"                    for item in data.get(\"data\", []):"` | — |
| [SRC-1AE03B9EC3-L002820](../../agents/web_agent.py#L2820) | 2820 | `"                        author = authors.get(item.get(\"author_id\"), {})"` | — |
| [SRC-1AE03B9EC3-L002821](../../agents/web_agent.py#L2821) | 2821 | `"                        username = author.get(\"username\", \"\")"` | — |
| [SRC-1AE03B9EC3-L002822](../../agents/web_agent.py#L2822) | 2822 | `"                        post_id = item.get(\"id\", \"\")"` | — |
| [SRC-1AE03B9EC3-L002823](../../agents/web_agent.py#L2823) | 2823 | `"                        if not username or not post_id:"` | — |
| [SRC-1AE03B9EC3-L002824](../../agents/web_agent.py#L2824) | 2824 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002825](../../agents/web_agent.py#L2825) | 2825 | `"                        results.append({"` | — |
| [SRC-1AE03B9EC3-L002826](../../agents/web_agent.py#L2826) | 2826 | `"                            \"title\": _clean_text(author.get(\"name\") or username, 300),"` | — |
| [SRC-1AE03B9EC3-L002827](../../agents/web_agent.py#L2827) | 2827 | `"                            \"url\": f\"https://x.com/{username}/status/{post_id}\","` | — |
| [SRC-1AE03B9EC3-L002828](../../agents/web_agent.py#L2828) | 2828 | `"                            \"snippet\": _clean_text(item.get(\"text\") or \"\", 1200),"` | — |
| [SRC-1AE03B9EC3-L002829](../../agents/web_agent.py#L2829) | 2829 | `"                            \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L002830](../../agents/web_agent.py#L2830) | 2830 | `"                            \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L002831](../../agents/web_agent.py#L2831) | 2831 | `"                            \"provider\": \"x_official_api\","` | — |
| [SRC-1AE03B9EC3-L002832](../../agents/web_agent.py#L2832) | 2832 | `"                            \"provider_rank\": len(["` | — |
| [SRC-1AE03B9EC3-L002833](../../agents/web_agent.py#L2833) | 2833 | `"                                row for row in results"` | — |
| [SRC-1AE03B9EC3-L002834](../../agents/web_agent.py#L2834) | 2834 | `"                                if row.get(\"provider\") == \"x_official_api\""` | — |
| [SRC-1AE03B9EC3-L002835](../../agents/web_agent.py#L2835) | 2835 | `"                            ]) + 1,"` | — |
| [SRC-1AE03B9EC3-L002836](../../agents/web_agent.py#L2836) | 2836 | `"                            \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L002837](../../agents/web_agent.py#L2837) | 2837 | `"                            \"published_at\": _clean_text(item.get(\"created_at\") or \"\", 100),"` | — |
| [SRC-1AE03B9EC3-L002838](../../agents/web_agent.py#L2838) | 2838 | `"                        })"` | — |
| [SRC-1AE03B9EC3-L002839](../../agents/web_agent.py#L2839) | 2839 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L002840](../../agents/web_agent.py#L2840) | 2840 | `"                    warnings.append(f\"X API unavailable (HTTP {response.status_code})\")"` | — |
| [SRC-1AE03B9EC3-L002841](../../agents/web_agent.py#L2841) | 2841 | `"            except (httpx.HTTPError, OSError, ValueError, KeyError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L002842](../../agents/web_agent.py#L2842) | 2842 | `"                warnings.append(\"X API unavailable for this request\")"` | — |
| [SRC-1AE03B9EC3-L002843](../../agents/web_agent.py#L2843) | 2843 | `"        elif \"x\" in platforms:"` | — |
| [SRC-1AE03B9EC3-L002844](../../agents/web_agent.py#L2844) | 2844 | `"            warnings.append(\"X direct API is not configured; indexed public X pages are still searched.\")"` | — |
| [SRC-1AE03B9EC3-L002845](../../agents/web_agent.py#L2845) | 2845 | `""` | — |
| [SRC-1AE03B9EC3-L002846](../../agents/web_agent.py#L2846) | 2846 | `"        if \"youtube\" in platforms and os.getenv(\"YOUTUBE_API_KEY\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L002847](../../agents/web_agent.py#L2847) | 2847 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L002848](../../agents/web_agent.py#L2848) | 2848 | `"                self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L002849](../../agents/web_agent.py#L2849) | 2849 | `"                response = _bounded_http_request(\"GET\", "` | — |
| [SRC-1AE03B9EC3-L002850](../../agents/web_agent.py#L2850) | 2850 | `"                    \"https://www.googleapis.com/youtube/v3/search\","` | — |
| [SRC-1AE03B9EC3-L002851](../../agents/web_agent.py#L2851) | 2851 | `"                    params={"` | — |
| [SRC-1AE03B9EC3-L002852](../../agents/web_agent.py#L2852) | 2852 | `"                        \"part\": \"snippet\","` | — |
| [SRC-1AE03B9EC3-L002853](../../agents/web_agent.py#L2853) | 2853 | `"                        \"q\": query,"` | — |
| [SRC-1AE03B9EC3-L002854](../../agents/web_agent.py#L2854) | 2854 | `"                        \"type\": \"video\","` | — |
| [SRC-1AE03B9EC3-L002855](../../agents/web_agent.py#L2855) | 2855 | `"                        \"maxResults\": 8,"` | — |
| [SRC-1AE03B9EC3-L002856](../../agents/web_agent.py#L2856) | 2856 | `"                        \"key\": os.getenv(\"YOUTUBE_API_KEY\", \"\").strip(),"` | — |
| [SRC-1AE03B9EC3-L002857](../../agents/web_agent.py#L2857) | 2857 | `"                    },"` | — |
| [SRC-1AE03B9EC3-L002858](../../agents/web_agent.py#L2858) | 2858 | `"                    headers=headers,"` | — |
| [SRC-1AE03B9EC3-L002859](../../agents/web_agent.py#L2859) | 2859 | `"                    timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L002860](../../agents/web_agent.py#L2860) | 2860 | `"                    follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L002861](../../agents/web_agent.py#L2861) | 2861 | `"                )"` | — |
| [SRC-1AE03B9EC3-L002862](../../agents/web_agent.py#L2862) | 2862 | `"                if response.status_code == 200:"` | — |
| [SRC-1AE03B9EC3-L002863](../../agents/web_agent.py#L2863) | 2863 | `"                    data = response.json()"` | — |
| [SRC-1AE03B9EC3-L002864](../../agents/web_agent.py#L2864) | 2864 | `"                    for item in data.get(\"items\", []):"` | — |
| [SRC-1AE03B9EC3-L002865](../../agents/web_agent.py#L2865) | 2865 | `"                        video_id = item.get(\"id\", {}).get(\"videoId\")"` | — |
| [SRC-1AE03B9EC3-L002866](../../agents/web_agent.py#L2866) | 2866 | `"                        snippet = item.get(\"snippet\", {})"` | — |
| [SRC-1AE03B9EC3-L002867](../../agents/web_agent.py#L2867) | 2867 | `"                        if not video_id:"` | — |
| [SRC-1AE03B9EC3-L002868](../../agents/web_agent.py#L2868) | 2868 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002869](../../agents/web_agent.py#L2869) | 2869 | `"                        results.append({"` | — |
| [SRC-1AE03B9EC3-L002870](../../agents/web_agent.py#L2870) | 2870 | `"                            \"title\": _clean_text(snippet.get(\"title\") or \"\", 300),"` | — |
| [SRC-1AE03B9EC3-L002871](../../agents/web_agent.py#L2871) | 2871 | `"                            \"url\": f\"https://www.youtube.com/watch?v={video_id}\","` | — |
| [SRC-1AE03B9EC3-L002872](../../agents/web_agent.py#L2872) | 2872 | `"                            \"snippet\": _clean_text(snippet.get(\"description\") or \"\", 1200),"` | — |
| [SRC-1AE03B9EC3-L002873](../../agents/web_agent.py#L2873) | 2873 | `"                            \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L002874](../../agents/web_agent.py#L2874) | 2874 | `"                            \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L002875](../../agents/web_agent.py#L2875) | 2875 | `"                            \"provider\": \"youtube_data_api\","` | — |
| [SRC-1AE03B9EC3-L002876](../../agents/web_agent.py#L2876) | 2876 | `"                            \"provider_rank\": len(["` | — |
| [SRC-1AE03B9EC3-L002877](../../agents/web_agent.py#L2877) | 2877 | `"                                row for row in results"` | — |
| [SRC-1AE03B9EC3-L002878](../../agents/web_agent.py#L2878) | 2878 | `"                                if row.get(\"provider\") == \"youtube_data_api\""` | — |
| [SRC-1AE03B9EC3-L002879](../../agents/web_agent.py#L2879) | 2879 | `"                            ]) + 1,"` | — |
| [SRC-1AE03B9EC3-L002880](../../agents/web_agent.py#L2880) | 2880 | `"                            \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L002881](../../agents/web_agent.py#L2881) | 2881 | `"                            \"published_at\": _clean_text(snippet.get(\"publishedAt\") or \"\", 100),"` | — |
| [SRC-1AE03B9EC3-L002882](../../agents/web_agent.py#L2882) | 2882 | `"                        })"` | — |
| [SRC-1AE03B9EC3-L002883](../../agents/web_agent.py#L2883) | 2883 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L002884](../../agents/web_agent.py#L2884) | 2884 | `"                    warnings.append(f\"YouTube Data API unavailable (HTTP {response.status_code})\")"` | — |
| [SRC-1AE03B9EC3-L002885](../../agents/web_agent.py#L2885) | 2885 | `"            except (httpx.HTTPError, OSError, ValueError, KeyError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L002886](../../agents/web_agent.py#L2886) | 2886 | `"                warnings.append(\"YouTube Data API unavailable for this request\")"` | — |
| [SRC-1AE03B9EC3-L002887](../../agents/web_agent.py#L2887) | 2887 | `"        elif \"youtube\" in platforms:"` | — |
| [SRC-1AE03B9EC3-L002888](../../agents/web_agent.py#L2888) | 2888 | `"            warnings.append(\"YouTube direct API is not configured; indexed public YouTube pages are still searched.\")"` | — |
| [SRC-1AE03B9EC3-L002889](../../agents/web_agent.py#L2889) | 2889 | `""` | — |
| [SRC-1AE03B9EC3-L002890](../../agents/web_agent.py#L2890) | 2890 | `"        return results, warnings"` | — |
| [SRC-1AE03B9EC3-L002891](../../agents/web_agent.py#L2891) | 2891 | `""` | — |
| [SRC-1AE03B9EC3-L002892](../../agents/web_agent.py#L2892) | 2892 | `"    def _fetch_page(self, url: str) -> tuple[str, str]:"` | — |
| [SRC-1AE03B9EC3-L002893](../../agents/web_agent.py#L2893) | 2893 | `"        \"\"\"Fetch a public page with bounded redirects and an inspectable extraction outcome.\"\"\""` | — |
| [SRC-1AE03B9EC3-L002894](../../agents/web_agent.py#L2894) | 2894 | `"        def result("` | — |
| [SRC-1AE03B9EC3-L002895](../../agents/web_agent.py#L2895) | 2895 | `"            title: str = \"\","` | — |
| [SRC-1AE03B9EC3-L002896](../../agents/web_agent.py#L2896) | 2896 | `"            page_text: str = \"\","` | — |
| [SRC-1AE03B9EC3-L002897](../../agents/web_agent.py#L2897) | 2897 | `"            status: str = \"unknown\","` | — |
| [SRC-1AE03B9EC3-L002898](../../agents/web_agent.py#L2898) | 2898 | `"            error_class: str \| None = None,"` | — |
| [SRC-1AE03B9EC3-L002899](../../agents/web_agent.py#L2899) | 2899 | `"        ) -> PageFetchResult:"` | — |
| [SRC-1AE03B9EC3-L002900](../../agents/web_agent.py#L2900) | 2900 | `"            return PageFetchResult(title, page_text, status, error_class)"` | — |
| [SRC-1AE03B9EC3-L002901](../../agents/web_agent.py#L2901) | 2901 | `""` | — |
| [SRC-1AE03B9EC3-L002902](../../agents/web_agent.py#L2902) | 2902 | `"        current_url = _public_http_url(url)"` | — |
| [SRC-1AE03B9EC3-L002903](../../agents/web_agent.py#L2903) | 2903 | `"        if not current_url:"` | — |
| [SRC-1AE03B9EC3-L002904](../../agents/web_agent.py#L2904) | 2904 | `"            return result(status=\"rejected_url\", error_class=\"PublicUrlRejected\")"` | — |
| [SRC-1AE03B9EC3-L002905](../../agents/web_agent.py#L2905) | 2905 | `"        budget = getattr(self, \"_request_budget\", None)"` | — |
| [SRC-1AE03B9EC3-L002906](../../agents/web_agent.py#L2906) | 2906 | `"        if budget is not None:"` | — |
| [SRC-1AE03B9EC3-L002907](../../agents/web_agent.py#L2907) | 2907 | `"            budget.reserve(\"page_fetches\")"` | — |
| [SRC-1AE03B9EC3-L002908](../../agents/web_agent.py#L2908) | 2908 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L002909](../../agents/web_agent.py#L2909) | 2909 | `"            import httpx"` | — |
| [SRC-1AE03B9EC3-L002910](../../agents/web_agent.py#L2910) | 2910 | `"            from bs4 import BeautifulSoup"` | — |
| [SRC-1AE03B9EC3-L002911](../../agents/web_agent.py#L2911) | 2911 | `"        except ImportError as exc:"` | — |
| [SRC-1AE03B9EC3-L002912](../../agents/web_agent.py#L2912) | 2912 | `"            raise AgentDependencyError("` | — |
| [SRC-1AE03B9EC3-L002913](../../agents/web_agent.py#L2913) | 2913 | `"                \"حزم استخراج الصفحات غير مثبتة. نفّذ: python -m pip install -e .\""` | — |
| [SRC-1AE03B9EC3-L002914](../../agents/web_agent.py#L2914) | 2914 | `"            ) from exc"` | — |
| [SRC-1AE03B9EC3-L002915](../../agents/web_agent.py#L2915) | 2915 | `""` | — |
| [SRC-1AE03B9EC3-L002916](../../agents/web_agent.py#L2916) | 2916 | `"        headers = {"` | — |
| [SRC-1AE03B9EC3-L002917](../../agents/web_agent.py#L2917) | 2917 | `"            \"User-Agent\": \"OmaraiResearchBot/1.1 (public page research; no login)\","` | — |
| [SRC-1AE03B9EC3-L002918](../../agents/web_agent.py#L2918) | 2918 | `"            \"Accept\": \"text/html,application/xhtml+xml,text/plain;q=0.8\","` | — |
| [SRC-1AE03B9EC3-L002919](../../agents/web_agent.py#L2919) | 2919 | `"            \"Accept-Encoding\": \"identity\","` | — |
| [SRC-1AE03B9EC3-L002920](../../agents/web_agent.py#L2920) | 2920 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002921](../../agents/web_agent.py#L2921) | 2921 | `"        media_type = \"\""` | — |
| [SRC-1AE03B9EC3-L002922](../../agents/web_agent.py#L2922) | 2922 | `"        html = \"\""` | — |
| [SRC-1AE03B9EC3-L002923](../../agents/web_agent.py#L2923) | 2923 | `"        bytes_truncated = False"` | — |
| [SRC-1AE03B9EC3-L002924](../../agents/web_agent.py#L2924) | 2924 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L002925](../../agents/web_agent.py#L2925) | 2925 | `"            with httpx.Client("` | — |
| [SRC-1AE03B9EC3-L002926](../../agents/web_agent.py#L2926) | 2926 | `"                timeout=self._effective_timeout(8.0),"` | — |
| [SRC-1AE03B9EC3-L002927](../../agents/web_agent.py#L2927) | 2927 | `"                follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L002928](../../agents/web_agent.py#L2928) | 2928 | `"                headers=headers,"` | — |
| [SRC-1AE03B9EC3-L002929](../../agents/web_agent.py#L2929) | 2929 | `"                verify=True,"` | — |
| [SRC-1AE03B9EC3-L002930](../../agents/web_agent.py#L2930) | 2930 | `"                trust_env=False,"` | — |
| [SRC-1AE03B9EC3-L002931](../../agents/web_agent.py#L2931) | 2931 | `"            ) as client:"` | — |
| [SRC-1AE03B9EC3-L002932](../../agents/web_agent.py#L2932) | 2932 | `"                for redirect_number in range(4):"` | — |
| [SRC-1AE03B9EC3-L002933](../../agents/web_agent.py#L2933) | 2933 | `"                    parsed = urllib.parse.urlparse(current_url)"` | — |
| [SRC-1AE03B9EC3-L002934](../../agents/web_agent.py#L2934) | 2934 | `"                    host = parsed.hostname or \"\""` | — |
| [SRC-1AE03B9EC3-L002935](../../agents/web_agent.py#L2935) | 2935 | `"                    # Resolve and pin a public IP. Do not let the HTTP client resolve"` | — |
| [SRC-1AE03B9EC3-L002936](../../agents/web_agent.py#L2936) | 2936 | `"                    # the original hostname a second time."` | — |
| [SRC-1AE03B9EC3-L002937](../../agents/web_agent.py#L2937) | 2937 | `"                    public_ips = _public_ip_literals(host)"` | — |
| [SRC-1AE03B9EC3-L002938](../../agents/web_agent.py#L2938) | 2938 | `"                    if not public_ips:"` | — |
| [SRC-1AE03B9EC3-L002939](../../agents/web_agent.py#L2939) | 2939 | `"                        return result(status=\"blocked_or_unresolved_host\", error_class=\"HostResolutionOrSSRFCheck\")"` | — |
| [SRC-1AE03B9EC3-L002940](../../agents/web_agent.py#L2940) | 2940 | `"                    connect_url = _pinned_connect_url(current_url, public_ips[0])"` | — |
| [SRC-1AE03B9EC3-L002941](../../agents/web_agent.py#L2941) | 2941 | `"                    if not connect_url:"` | — |
| [SRC-1AE03B9EC3-L002942](../../agents/web_agent.py#L2942) | 2942 | `"                        return result(status=\"blocked_connection_target\", error_class=\"PinnedTargetRejected\")"` | — |
| [SRC-1AE03B9EC3-L002943](../../agents/web_agent.py#L2943) | 2943 | `"                    request_headers = {\"Host\": host}"` | — |
| [SRC-1AE03B9EC3-L002944](../../agents/web_agent.py#L2944) | 2944 | `"                    extensions = {\"sni_hostname\": host} if parsed.scheme == \"https\" else {}"` | — |
| [SRC-1AE03B9EC3-L002945](../../agents/web_agent.py#L2945) | 2945 | `"                    with client.stream("` | — |
| [SRC-1AE03B9EC3-L002946](../../agents/web_agent.py#L2946) | 2946 | `"                        \"GET\","` | — |
| [SRC-1AE03B9EC3-L002947](../../agents/web_agent.py#L2947) | 2947 | `"                        connect_url,"` | — |
| [SRC-1AE03B9EC3-L002948](../../agents/web_agent.py#L2948) | 2948 | `"                        headers=request_headers,"` | — |
| [SRC-1AE03B9EC3-L002949](../../agents/web_agent.py#L2949) | 2949 | `"                        extensions=extensions,"` | — |
| [SRC-1AE03B9EC3-L002950](../../agents/web_agent.py#L2950) | 2950 | `"                    ) as response:"` | — |
| [SRC-1AE03B9EC3-L002951](../../agents/web_agent.py#L2951) | 2951 | `"                        if response.status_code in {301, 302, 303, 307, 308}:"` | — |
| [SRC-1AE03B9EC3-L002952](../../agents/web_agent.py#L2952) | 2952 | `"                            location = response.headers.get(\"location\", \"\")"` | — |
| [SRC-1AE03B9EC3-L002953](../../agents/web_agent.py#L2953) | 2953 | `"                            if not location or redirect_number >= 3:"` | — |
| [SRC-1AE03B9EC3-L002954](../../agents/web_agent.py#L2954) | 2954 | `"                                return result(status=\"redirect_failed\", error_class=\"RedirectLimitOrMissingLocation\")"` | — |
| [SRC-1AE03B9EC3-L002955](../../agents/web_agent.py#L2955) | 2955 | `"                            target = _public_http_url("` | — |
| [SRC-1AE03B9EC3-L002956](../../agents/web_agent.py#L2956) | 2956 | `"                                urllib.parse.urljoin(current_url, location)"` | — |
| [SRC-1AE03B9EC3-L002957](../../agents/web_agent.py#L2957) | 2957 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L002958](../../agents/web_agent.py#L2958) | 2958 | `"                            if not target:"` | — |
| [SRC-1AE03B9EC3-L002959](../../agents/web_agent.py#L2959) | 2959 | `"                                return result(status=\"redirect_rejected\", error_class=\"RedirectTargetRejected\")"` | — |
| [SRC-1AE03B9EC3-L002960](../../agents/web_agent.py#L2960) | 2960 | `"                            current_url = target"` | — |
| [SRC-1AE03B9EC3-L002961](../../agents/web_agent.py#L2961) | 2961 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002962](../../agents/web_agent.py#L2962) | 2962 | `"                        if response.status_code < 200 or response.status_code >= 300:"` | — |
| [SRC-1AE03B9EC3-L002963](../../agents/web_agent.py#L2963) | 2963 | `"                            return result(status=\"http_error\", error_class=\"HTTPStatus\")"` | — |
| [SRC-1AE03B9EC3-L002964](../../agents/web_agent.py#L2964) | 2964 | `"                        media_type = response.headers.get("` | — |
| [SRC-1AE03B9EC3-L002965](../../agents/web_agent.py#L2965) | 2965 | `"                            \"content-type\", \"\""` | — |
| [SRC-1AE03B9EC3-L002966](../../agents/web_agent.py#L2966) | 2966 | `"                        ).split(\";\")[0].lower()"` | — |
| [SRC-1AE03B9EC3-L002967](../../agents/web_agent.py#L2967) | 2967 | `"                        if media_type not in {"` | — |
| [SRC-1AE03B9EC3-L002968](../../agents/web_agent.py#L2968) | 2968 | `"                            \"text/html\", \"application/xhtml+xml\", \"text/plain\""` | — |
| [SRC-1AE03B9EC3-L002969](../../agents/web_agent.py#L2969) | 2969 | `"                        }:"` | — |
| [SRC-1AE03B9EC3-L002970](../../agents/web_agent.py#L2970) | 2970 | `"                            return result(status=\"unsupported_content_type\", error_class=\"UnsupportedContentType\")"` | — |
| [SRC-1AE03B9EC3-L002971](../../agents/web_agent.py#L2971) | 2971 | `"                        content_length = response.headers.get(\"content-length\")"` | — |
| [SRC-1AE03B9EC3-L002972](../../agents/web_agent.py#L2972) | 2972 | `"                        if content_length:"` | — |
| [SRC-1AE03B9EC3-L002973](../../agents/web_agent.py#L2973) | 2973 | `"                            try:"` | — |
| [SRC-1AE03B9EC3-L002974](../../agents/web_agent.py#L2974) | 2974 | `"                                if int(content_length) > MAX_PAGE_BYTES:"` | — |
| [SRC-1AE03B9EC3-L002975](../../agents/web_agent.py#L2975) | 2975 | `"                                    return result(status=\"page_too_large\", error_class=\"ContentLengthLimit\")"` | — |
| [SRC-1AE03B9EC3-L002976](../../agents/web_agent.py#L2976) | 2976 | `"                            except ValueError:"` | — |
| [SRC-1AE03B9EC3-L002977](../../agents/web_agent.py#L2977) | 2977 | `"                                pass"` | — |
| [SRC-1AE03B9EC3-L002978](../../agents/web_agent.py#L2978) | 2978 | `"                        chunks: list[bytes] = []"` | — |
| [SRC-1AE03B9EC3-L002979](../../agents/web_agent.py#L2979) | 2979 | `"                        count = 0"` | — |
| [SRC-1AE03B9EC3-L002980](../../agents/web_agent.py#L2980) | 2980 | `"                        for chunk in response.iter_bytes():"` | — |
| [SRC-1AE03B9EC3-L002981](../../agents/web_agent.py#L2981) | 2981 | `"                            count += len(chunk)"` | — |
| [SRC-1AE03B9EC3-L002982](../../agents/web_agent.py#L2982) | 2982 | `"                            if count > MAX_PAGE_BYTES:"` | — |
| [SRC-1AE03B9EC3-L002983](../../agents/web_agent.py#L2983) | 2983 | `"                                remaining = max(0, MAX_PAGE_BYTES - (count - len(chunk)))"` | — |
| [SRC-1AE03B9EC3-L002984](../../agents/web_agent.py#L2984) | 2984 | `"                                if remaining:"` | — |
| [SRC-1AE03B9EC3-L002985](../../agents/web_agent.py#L2985) | 2985 | `"                                    chunks.append(chunk[:remaining])"` | — |
| [SRC-1AE03B9EC3-L002986](../../agents/web_agent.py#L2986) | 2986 | `"                                bytes_truncated = True"` | — |
| [SRC-1AE03B9EC3-L002987](../../agents/web_agent.py#L2987) | 2987 | `"                                break"` | — |
| [SRC-1AE03B9EC3-L002988](../../agents/web_agent.py#L2988) | 2988 | `"                            chunks.append(chunk)"` | — |
| [SRC-1AE03B9EC3-L002989](../../agents/web_agent.py#L2989) | 2989 | `"                        raw = b\"\".join(chunks)"` | — |
| [SRC-1AE03B9EC3-L002990](../../agents/web_agent.py#L2990) | 2990 | `"                        encoding = response.encoding or \"utf-8\""` | — |
| [SRC-1AE03B9EC3-L002991](../../agents/web_agent.py#L2991) | 2991 | `"                        html = raw.decode(encoding, errors=\"replace\")"` | — |
| [SRC-1AE03B9EC3-L002992](../../agents/web_agent.py#L2992) | 2992 | `"                        break"` | — |
| [SRC-1AE03B9EC3-L002993](../../agents/web_agent.py#L2993) | 2993 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L002994](../../agents/web_agent.py#L2994) | 2994 | `"                    return result(status=\"redirect_limit\", error_class=\"RedirectLimit\")"` | — |
| [SRC-1AE03B9EC3-L002995](../../agents/web_agent.py#L2995) | 2995 | `"        except httpx.DecodingError:"` | — |
| [SRC-1AE03B9EC3-L002996](../../agents/web_agent.py#L2996) | 2996 | `"            return result(status=\"decoding_error\", error_class=\"ContentDecodingError\")"` | — |
| [SRC-1AE03B9EC3-L002997](../../agents/web_agent.py#L2997) | 2997 | `"        except (OSError, ValueError, httpx.HTTPError) as exc:"` | — |
| [SRC-1AE03B9EC3-L002998](../../agents/web_agent.py#L2998) | 2998 | `"            return result(status=\"network_error\", error_class=type(exc).__name__)"` | — |
| [SRC-1AE03B9EC3-L002999](../../agents/web_agent.py#L2999) | 2999 | `""` | — |
| [SRC-1AE03B9EC3-L003000](../../agents/web_agent.py#L3000) | 3000 | `"        if media_type == \"text/plain\":"` | — |
| [SRC-1AE03B9EC3-L003001](../../agents/web_agent.py#L3001) | 3001 | `"            bounded_text = _clean_text(html, MAX_PAGE_TEXT_CHARS + 1)"` | — |
| [SRC-1AE03B9EC3-L003002](../../agents/web_agent.py#L3002) | 3002 | `"            text_truncated = len(bounded_text) > MAX_PAGE_TEXT_CHARS"` | — |
| [SRC-1AE03B9EC3-L003003](../../agents/web_agent.py#L3003) | 3003 | `"            page_text = _clean_text(bounded_text, MAX_PAGE_TEXT_CHARS)"` | — |
| [SRC-1AE03B9EC3-L003004](../../agents/web_agent.py#L3004) | 3004 | `"            status = ("` | — |
| [SRC-1AE03B9EC3-L003005](../../agents/web_agent.py#L3005) | 3005 | `"                \"empty_content\" if not page_text"` | — |
| [SRC-1AE03B9EC3-L003006](../../agents/web_agent.py#L3006) | 3006 | `"                else \"partial_extraction\" if bytes_truncated or text_truncated"` | — |
| [SRC-1AE03B9EC3-L003007](../../agents/web_agent.py#L3007) | 3007 | `"                else \"content_extracted\""` | — |
| [SRC-1AE03B9EC3-L003008](../../agents/web_agent.py#L3008) | 3008 | `"            )"` | — |
| [SRC-1AE03B9EC3-L003009](../../agents/web_agent.py#L3009) | 3009 | `"            return result(\"\", page_text, status)"` | — |
| [SRC-1AE03B9EC3-L003010](../../agents/web_agent.py#L3010) | 3010 | `""` | — |
| [SRC-1AE03B9EC3-L003011](../../agents/web_agent.py#L3011) | 3011 | `"        soup = BeautifulSoup(html, \"html.parser\")"` | — |
| [SRC-1AE03B9EC3-L003012](../../agents/web_agent.py#L3012) | 3012 | `"        title = _clean_text(soup.title.get_text(\" \", strip=True), 300) if soup.title else \"\""` | — |
| [SRC-1AE03B9EC3-L003013](../../agents/web_agent.py#L3013) | 3013 | `"        for element in soup(["` | — |
| [SRC-1AE03B9EC3-L003014](../../agents/web_agent.py#L3014) | 3014 | `"            \"script\", \"style\", \"nav\", \"footer\", \"header\", \"noscript\","` | — |
| [SRC-1AE03B9EC3-L003015](../../agents/web_agent.py#L3015) | 3015 | `"            \"svg\", \"form\", \"iframe\", \"template\""` | — |
| [SRC-1AE03B9EC3-L003016](../../agents/web_agent.py#L3016) | 3016 | `"        ]):"` | — |
| [SRC-1AE03B9EC3-L003017](../../agents/web_agent.py#L3017) | 3017 | `"            element.decompose()"` | — |
| [SRC-1AE03B9EC3-L003018](../../agents/web_agent.py#L3018) | 3018 | `"        main = soup.find(\"main\") or soup.find(\"article\") or soup.body or soup"` | — |
| [SRC-1AE03B9EC3-L003019](../../agents/web_agent.py#L3019) | 3019 | `"        bounded_text = _clean_text(main.get_text(\" \", strip=True), MAX_PAGE_TEXT_CHARS + 1)"` | — |
| [SRC-1AE03B9EC3-L003020](../../agents/web_agent.py#L3020) | 3020 | `"        text_truncated = len(bounded_text) > MAX_PAGE_TEXT_CHARS"` | — |
| [SRC-1AE03B9EC3-L003021](../../agents/web_agent.py#L3021) | 3021 | `"        page_text = _clean_text(bounded_text, MAX_PAGE_TEXT_CHARS)"` | — |
| [SRC-1AE03B9EC3-L003022](../../agents/web_agent.py#L3022) | 3022 | `"        status = ("` | — |
| [SRC-1AE03B9EC3-L003023](../../agents/web_agent.py#L3023) | 3023 | `"            \"no_text_extracted\" if not page_text"` | — |
| [SRC-1AE03B9EC3-L003024](../../agents/web_agent.py#L3024) | 3024 | `"            else \"partial_extraction\" if bytes_truncated or text_truncated"` | — |
| [SRC-1AE03B9EC3-L003025](../../agents/web_agent.py#L3025) | 3025 | `"            else \"content_extracted\""` | — |
| [SRC-1AE03B9EC3-L003026](../../agents/web_agent.py#L3026) | 3026 | `"        )"` | — |
| [SRC-1AE03B9EC3-L003027](../../agents/web_agent.py#L3027) | 3027 | `"        return result(title, page_text, status)"` | — |
| [SRC-1AE03B9EC3-L003028](../../agents/web_agent.py#L3028) | 3028 | `""` | — |
| [SRC-1AE03B9EC3-L003029](../../agents/web_agent.py#L3029) | 3029 | `"    def _collect_sources(self, query: str) -> tuple[list[dict[str, Any]], str \| None]:"` | — |
| [SRC-1AE03B9EC3-L003030](../../agents/web_agent.py#L3030) | 3030 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L003031](../../agents/web_agent.py#L3031) | 3031 | `"            sources = self._search_web(query)"` | — |
| [SRC-1AE03B9EC3-L003032](../../agents/web_agent.py#L3032) | 3032 | `"        except (RuntimeError, AgentDependencyError) as exc:"` | — |
| [SRC-1AE03B9EC3-L003033](../../agents/web_agent.py#L3033) | 3033 | `"            return [], str(exc)"` | — |
| [SRC-1AE03B9EC3-L003034](../../agents/web_agent.py#L3034) | 3034 | `"        for source in sources[:MAX_FETCHED_PAGES]:"` | — |
| [SRC-1AE03B9EC3-L003035](../../agents/web_agent.py#L3035) | 3035 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L003036](../../agents/web_agent.py#L3036) | 3036 | `"                title, page_text = self._fetch_page(source[\"url\"])"` | — |
| [SRC-1AE03B9EC3-L003037](../../agents/web_agent.py#L3037) | 3037 | `"            except (AgentDependencyError, RuntimeError):"` | — |
| [SRC-1AE03B9EC3-L003038](../../agents/web_agent.py#L3038) | 3038 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L003039](../../agents/web_agent.py#L3039) | 3039 | `"            if title:"` | — |
| [SRC-1AE03B9EC3-L003040](../../agents/web_agent.py#L3040) | 3040 | `"                source[\"title\"] = title"` | — |
| [SRC-1AE03B9EC3-L003041](../../agents/web_agent.py#L3041) | 3041 | `"            if page_text:"` | — |
| [SRC-1AE03B9EC3-L003042](../../agents/web_agent.py#L3042) | 3042 | `"                source[\"page_text\"] = page_text"` | — |
| [SRC-1AE03B9EC3-L003043](../../agents/web_agent.py#L3043) | 3043 | `"                source[\"page_fetched\"] = True"` | — |
| [SRC-1AE03B9EC3-L003044](../../agents/web_agent.py#L3044) | 3044 | `"                # Prefer extracted text over a thin search snippet."` | — |
| [SRC-1AE03B9EC3-L003045](../../agents/web_agent.py#L3045) | 3045 | `"                source[\"snippet\"] = page_text[:1800]"` | — |
| [SRC-1AE03B9EC3-L003046](../../agents/web_agent.py#L3046) | 3046 | `"        return sources, None"` | — |
| [SRC-1AE03B9EC3-L003047](../../agents/web_agent.py#L3047) | 3047 | `""` | — |
| [SRC-1AE03B9EC3-L003048](../../agents/web_agent.py#L3048) | 3048 | `"    def _collect_research("` | — |
| [SRC-1AE03B9EC3-L003049](../../agents/web_agent.py#L3049) | 3049 | `"        self, plan: dict[str, Any]"` | — |
| [SRC-1AE03B9EC3-L003050](../../agents/web_agent.py#L3050) | 3050 | `"    ) -> tuple[list[dict[str, Any]], list[str], dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L003051](../../agents/web_agent.py#L3051) | 3051 | `"        \"\"\"Run independent query searches concurrently, fuse evidence, then fetch top pages.\"\"\""` | — |
| [SRC-1AE03B9EC3-L003052](../../agents/web_agent.py#L3052) | 3052 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L003053](../../agents/web_agent.py#L3053) | 3053 | `"            query_limit = int(plan.get(\"query_limit\", MAX_PLAN_QUERIES))"` | — |
| [SRC-1AE03B9EC3-L003054](../../agents/web_agent.py#L3054) | 3054 | `"        except (TypeError, ValueError, OverflowError):"` | — |
| [SRC-1AE03B9EC3-L003055](../../agents/web_agent.py#L3055) | 3055 | `"            query_limit = MAX_PLAN_QUERIES"` | — |
| [SRC-1AE03B9EC3-L003056](../../agents/web_agent.py#L3056) | 3056 | `"        query_limit = max(1, min(query_limit, MAX_PLAN_QUERIES))"` | — |
| [SRC-1AE03B9EC3-L003057](../../agents/web_agent.py#L3057) | 3057 | `"        raw_queries = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L003058](../../agents/web_agent.py#L3058) | 3058 | `"            compact_search_query(query)"` | — |
| [SRC-1AE03B9EC3-L003059](../../agents/web_agent.py#L3059) | 3059 | `"            for query in plan.get(\"queries\", [])[:query_limit]"` | — |
| [SRC-1AE03B9EC3-L003060](../../agents/web_agent.py#L3060) | 3060 | `"            if isinstance(query, str) and query.strip()"` | — |
| [SRC-1AE03B9EC3-L003061](../../agents/web_agent.py#L3061) | 3061 | `"        ))"` | — |
| [SRC-1AE03B9EC3-L003062](../../agents/web_agent.py#L3062) | 3062 | `"        raw_queries = [query for query in raw_queries if query]"` | — |
| [SRC-1AE03B9EC3-L003063](../../agents/web_agent.py#L3063) | 3063 | `"        target_aspects = ["` | — |
| [SRC-1AE03B9EC3-L003064](../../agents/web_agent.py#L3064) | 3064 | `"            str(target).strip()[:120]"` | — |
| [SRC-1AE03B9EC3-L003065](../../agents/web_agent.py#L3065) | 3065 | `"            for target in (plan.get(\"coverage_targets\") or [])[:8]"` | — |
| [SRC-1AE03B9EC3-L003066](../../agents/web_agent.py#L3066) | 3066 | `"            if isinstance(target, str) and target.strip()"` | — |
| [SRC-1AE03B9EC3-L003067](../../agents/web_agent.py#L3067) | 3067 | `"        ]"` | — |
| [SRC-1AE03B9EC3-L003068](../../agents/web_agent.py#L3068) | 3068 | `"        # Reserve part of the existing query ceiling for evidence-gap repair."` | — |
| [SRC-1AE03B9EC3-L003069](../../agents/web_agent.py#L3069) | 3069 | `"        # This is a bounded retrieval loop, not an unbounded agent loop."` | — |
| [SRC-1AE03B9EC3-L003070](../../agents/web_agent.py#L3070) | 3070 | `"        repair_slot_limit = ("` | — |
| [SRC-1AE03B9EC3-L003071](../../agents/web_agent.py#L3071) | 3071 | `"            min(3, len(target_aspects), max(0, query_limit - 1))"` | — |
| [SRC-1AE03B9EC3-L003072](../../agents/web_agent.py#L3072) | 3072 | `"            if target_aspects else 0"` | — |
| [SRC-1AE03B9EC3-L003073](../../agents/web_agent.py#L3073) | 3073 | `"        )"` | — |
| [SRC-1AE03B9EC3-L003074](../../agents/web_agent.py#L3074) | 3074 | `"        initial_query_limit = max(1, query_limit - repair_slot_limit)"` | — |
| [SRC-1AE03B9EC3-L003075](../../agents/web_agent.py#L3075) | 3075 | `"        queries = raw_queries[:initial_query_limit]"` | — |
| [SRC-1AE03B9EC3-L003076](../../agents/web_agent.py#L3076) | 3076 | `"        warnings: list[str] = []"` | — |
| [SRC-1AE03B9EC3-L003077](../../agents/web_agent.py#L3077) | 3077 | `"        if not queries and not plan.get(\"direct_urls\"):"` | — |
| [SRC-1AE03B9EC3-L003078](../../agents/web_agent.py#L3078) | 3078 | `"            warnings.append(\"لم يُنشأ استعلام موضوعي قابل للبحث؛ لم تُستدعَ محركات البحث.\")"` | — |
| [SRC-1AE03B9EC3-L003079](../../agents/web_agent.py#L3079) | 3079 | `"        batches: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L003080](../../agents/web_agent.py#L3080) | 3080 | `"        query_counts: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L003081](../../agents/web_agent.py#L3081) | 3081 | `"        search_started_queries = 0"` | — |
| [SRC-1AE03B9EC3-L003082](../../agents/web_agent.py#L3082) | 3082 | `""` | — |
| [SRC-1AE03B9EC3-L003083](../../agents/web_agent.py#L3083) | 3083 | `"        if queries:"` | — |
| [SRC-1AE03B9EC3-L003084](../../agents/web_agent.py#L3084) | 3084 | `"            with ThreadPoolExecutor(max_workers=min(MAX_RESEARCH_WORKERS, len(queries))) as pool:"` | — |
| [SRC-1AE03B9EC3-L003085](../../agents/web_agent.py#L3085) | 3085 | `"                futures = {pool.submit(self._search_web, query): query for query in queries}"` | — |
| [SRC-1AE03B9EC3-L003086](../../agents/web_agent.py#L3086) | 3086 | `"                for future in as_completed(futures):"` | — |
| [SRC-1AE03B9EC3-L003087](../../agents/web_agent.py#L3087) | 3087 | `"                    query = futures[future]"` | — |
| [SRC-1AE03B9EC3-L003088](../../agents/web_agent.py#L3088) | 3088 | `"                    search_started_queries += 1"` | — |
| [SRC-1AE03B9EC3-L003089](../../agents/web_agent.py#L3089) | 3089 | `"                    try:"` | — |
| [SRC-1AE03B9EC3-L003090](../../agents/web_agent.py#L3090) | 3090 | `"                        results = future.result()"` | — |
| [SRC-1AE03B9EC3-L003091](../../agents/web_agent.py#L3091) | 3091 | `"                    except (RequestBudgetExceeded, RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L003092](../../agents/web_agent.py#L3092) | 3092 | `"                        warnings.append(f\"تعذر بحث الاستعلام «{query[:70]}»: {exc}\")"` | — |
| [SRC-1AE03B9EC3-L003093](../../agents/web_agent.py#L3093) | 3093 | `"                        query_counts.append({\"query\": query, \"results\": 0})"` | — |
| [SRC-1AE03B9EC3-L003094](../../agents/web_agent.py#L3094) | 3094 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L003095](../../agents/web_agent.py#L3095) | 3095 | `"                    query_counts.append({\"query\": query, \"results\": len(results)})"` | — |
| [SRC-1AE03B9EC3-L003096](../../agents/web_agent.py#L3096) | 3096 | `"                    grouped: dict[str, list[dict[str, Any]]] = {}"` | — |
| [SRC-1AE03B9EC3-L003097](../../agents/web_agent.py#L3097) | 3097 | `"                    for source in results:"` | — |
| [SRC-1AE03B9EC3-L003098](../../agents/web_agent.py#L3098) | 3098 | `"                        provider = str(source.get(\"provider\") or \"web_search\")"` | — |
| [SRC-1AE03B9EC3-L003099](../../agents/web_agent.py#L3099) | 3099 | `"                        grouped.setdefault(provider, []).append(source)"` | — |
| [SRC-1AE03B9EC3-L003100](../../agents/web_agent.py#L3100) | 3100 | `"                    for provider, items in grouped.items():"` | — |
| [SRC-1AE03B9EC3-L003101](../../agents/web_agent.py#L3101) | 3101 | `"                        items.sort(key=lambda item: int(item.get(\"provider_rank\", 999)))"` | — |
| [SRC-1AE03B9EC3-L003102](../../agents/web_agent.py#L3102) | 3102 | `"                        batches.append({\"query\": query, \"provider\": provider, \"results\": items})"` | — |
| [SRC-1AE03B9EC3-L003103](../../agents/web_agent.py#L3103) | 3103 | `""` | — |
| [SRC-1AE03B9EC3-L003104](../../agents/web_agent.py#L3104) | 3104 | `"        # Evidence-gap iteration: deep tasks get up to three targeted follow-up searches"` | — |
| [SRC-1AE03B9EC3-L003105](../../agents/web_agent.py#L3105) | 3105 | `"        # when initial coverage is thin. This uses observed source/domain/provider coverage,"` | — |
| [SRC-1AE03B9EC3-L003106](../../agents/web_agent.py#L3106) | 3106 | `"        # not the language model's subjective claim that it has enough evidence."` | — |
| [SRC-1AE03B9EC3-L003107](../../agents/web_agent.py#L3107) | 3107 | `"        preliminary = fuse_ranked_results(batches, limit=MAX_SEARCH_RESULTS)"` | — |
| [SRC-1AE03B9EC3-L003108](../../agents/web_agent.py#L3108) | 3108 | `"        preliminary_domains = {"` | — |
| [SRC-1AE03B9EC3-L003109](../../agents/web_agent.py#L3109) | 3109 | `"            registrable_domain(item.get(\"domain\") or urllib.parse.urlparse(item.get(\"url\", \"\")).hostname)"` | — |
| [SRC-1AE03B9EC3-L003110](../../agents/web_agent.py#L3110) | 3110 | `"            for item in preliminary"` | — |
| [SRC-1AE03B9EC3-L003111](../../agents/web_agent.py#L3111) | 3111 | `"        }"` | — |
| [SRC-1AE03B9EC3-L003112](../../agents/web_agent.py#L3112) | 3112 | `"        preliminary_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L003113](../../agents/web_agent.py#L3113) | 3113 | `"        preliminary_providers = {"` | — |
| [SRC-1AE03B9EC3-L003114](../../agents/web_agent.py#L3114) | 3114 | `"            provider for item in preliminary for provider in item.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L003115](../../agents/web_agent.py#L3115) | 3115 | `"        }"` | — |
| [SRC-1AE03B9EC3-L003116](../../agents/web_agent.py#L3116) | 3116 | `"        needs_expansion = ("` | — |
| [SRC-1AE03B9EC3-L003117](../../agents/web_agent.py#L3117) | 3117 | `"            plan.get(\"intent_route\") != \"LEAD_GENERATION\""` | — |
| [SRC-1AE03B9EC3-L003118](../../agents/web_agent.py#L3118) | 3118 | `"            and plan.get(\"depth\") == \"deep\""` | — |
| [SRC-1AE03B9EC3-L003119](../../agents/web_agent.py#L3119) | 3119 | `"            and (len(preliminary) < 8 or len(preliminary_domains) < 5 or len(preliminary_providers) < 2)"` | — |
| [SRC-1AE03B9EC3-L003120](../../agents/web_agent.py#L3120) | 3120 | `"        )"` | — |
| [SRC-1AE03B9EC3-L003121](../../agents/web_agent.py#L3121) | 3121 | `"        preliminary_ledger = build_evidence_ledger(target_aspects, preliminary)"` | — |
| [SRC-1AE03B9EC3-L003122](../../agents/web_agent.py#L3122) | 3122 | `"        missing_aspects = list(preliminary_ledger.get(\"missing\") or [])"` | — |
| [SRC-1AE03B9EC3-L003123](../../agents/web_agent.py#L3123) | 3123 | `"        expansion_queries: list[str] = []"` | — |
| [SRC-1AE03B9EC3-L003124](../../agents/web_agent.py#L3124) | 3124 | `"        # Do not issue generic repairs when a standard task already has per-requirement queries."` | — |
| [SRC-1AE03B9EC3-L003125](../../agents/web_agent.py#L3125) | 3125 | `"        # Legacy plans without those query records still need the bounded missing-aspect fallback;"` | — |
| [SRC-1AE03B9EC3-L003126](../../agents/web_agent.py#L3126) | 3126 | `"        # deep research may expand further even after targeted queries."` | — |
| [SRC-1AE03B9EC3-L003127](../../agents/web_agent.py#L3127) | 3127 | `"        if ("` | — |
| [SRC-1AE03B9EC3-L003128](../../agents/web_agent.py#L3128) | 3128 | `"            plan.get(\"intent_route\") != \"LEAD_GENERATION\""` | — |
| [SRC-1AE03B9EC3-L003129](../../agents/web_agent.py#L3129) | 3129 | `"            and (missing_aspects or needs_expansion)"` | — |
| [SRC-1AE03B9EC3-L003130](../../agents/web_agent.py#L3130) | 3130 | `"            and len(queries) < query_limit"` | — |
| [SRC-1AE03B9EC3-L003131](../../agents/web_agent.py#L3131) | 3131 | `"            and queries"` | — |
| [SRC-1AE03B9EC3-L003132](../../agents/web_agent.py#L3132) | 3132 | `"            and ("` | — |
| [SRC-1AE03B9EC3-L003133](../../agents/web_agent.py#L3133) | 3133 | `"                not plan.get(\"requirement_queries\")"` | — |
| [SRC-1AE03B9EC3-L003134](../../agents/web_agent.py#L3134) | 3134 | `"                or plan.get(\"depth\") == \"deep\""` | — |
| [SRC-1AE03B9EC3-L003135](../../agents/web_agent.py#L3135) | 3135 | `"            )"` | — |
| [SRC-1AE03B9EC3-L003136](../../agents/web_agent.py#L3136) | 3136 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L003137](../../agents/web_agent.py#L3137) | 3137 | `"            base_query = (queries[0] if queries else \"\")"` | — |
| [SRC-1AE03B9EC3-L003138](../../agents/web_agent.py#L3138) | 3138 | `"            remaining_slots = max(0, query_limit - len(queries))"` | — |
| [SRC-1AE03B9EC3-L003139](../../agents/web_agent.py#L3139) | 3139 | `"            aspect_queries = repair_queries_for_missing_aspects("` | — |
| [SRC-1AE03B9EC3-L003140](../../agents/web_agent.py#L3140) | 3140 | `"                base_query,"` | — |
| [SRC-1AE03B9EC3-L003141](../../agents/web_agent.py#L3141) | 3141 | `"                missing_aspects,"` | — |
| [SRC-1AE03B9EC3-L003142](../../agents/web_agent.py#L3142) | 3142 | `"                limit=min(repair_slot_limit, remaining_slots),"` | — |
| [SRC-1AE03B9EC3-L003143](../../agents/web_agent.py#L3143) | 3143 | `"                compact_fn=compact_search_query,"` | — |
| [SRC-1AE03B9EC3-L003144](../../agents/web_agent.py#L3144) | 3144 | `"            )"` | — |
| [SRC-1AE03B9EC3-L003145](../../agents/web_agent.py#L3145) | 3145 | `"            candidates = list(aspect_queries)"` | — |
| [SRC-1AE03B9EC3-L003146](../../agents/web_agent.py#L3146) | 3146 | `"            if needs_expansion:"` | — |
| [SRC-1AE03B9EC3-L003147](../../agents/web_agent.py#L3147) | 3147 | `"                candidates.extend(["` | — |
| [SRC-1AE03B9EC3-L003148](../../agents/web_agent.py#L3148) | 3148 | `"                    f\"{base_query} official sources data reports\","` | — |
| [SRC-1AE03B9EC3-L003149](../../agents/web_agent.py#L3149) | 3149 | `"                    f\"{base_query} limitations risks criticism alternatives\","` | — |
| [SRC-1AE03B9EC3-L003150](../../agents/web_agent.py#L3150) | 3150 | `"                    f\"{base_query} recent developments case studies analysis\","` | — |
| [SRC-1AE03B9EC3-L003151](../../agents/web_agent.py#L3151) | 3151 | `"                ])"` | — |
| [SRC-1AE03B9EC3-L003152](../../agents/web_agent.py#L3152) | 3152 | `"            existing = {item.casefold() for item in queries}"` | — |
| [SRC-1AE03B9EC3-L003153](../../agents/web_agent.py#L3153) | 3153 | `"            expansion_queries = []"` | — |
| [SRC-1AE03B9EC3-L003154](../../agents/web_agent.py#L3154) | 3154 | `"            seen_expansions = set(existing)"` | — |
| [SRC-1AE03B9EC3-L003155](../../agents/web_agent.py#L3155) | 3155 | `"            for candidate in candidates:"` | — |
| [SRC-1AE03B9EC3-L003156](../../agents/web_agent.py#L3156) | 3156 | `"                compacted = compact_search_query(candidate)"` | — |
| [SRC-1AE03B9EC3-L003157](../../agents/web_agent.py#L3157) | 3157 | `"                key = compacted.casefold()"` | — |
| [SRC-1AE03B9EC3-L003158](../../agents/web_agent.py#L3158) | 3158 | `"                if compacted and key not in seen_expansions:"` | — |
| [SRC-1AE03B9EC3-L003159](../../agents/web_agent.py#L3159) | 3159 | `"                    expansion_queries.append(compacted)"` | — |
| [SRC-1AE03B9EC3-L003160](../../agents/web_agent.py#L3160) | 3160 | `"                    seen_expansions.add(key)"` | — |
| [SRC-1AE03B9EC3-L003161](../../agents/web_agent.py#L3161) | 3161 | `"                if len(expansion_queries) >= remaining_slots:"` | — |
| [SRC-1AE03B9EC3-L003162](../../agents/web_agent.py#L3162) | 3162 | `"                    break"` | — |
| [SRC-1AE03B9EC3-L003163](../../agents/web_agent.py#L3163) | 3163 | `"            if expansion_queries:"` | — |
| [SRC-1AE03B9EC3-L003164](../../agents/web_agent.py#L3164) | 3164 | `"                with ThreadPoolExecutor("` | — |
| [SRC-1AE03B9EC3-L003165](../../agents/web_agent.py#L3165) | 3165 | `"                    max_workers=min(MAX_RESEARCH_WORKERS, len(expansion_queries))"` | — |
| [SRC-1AE03B9EC3-L003166](../../agents/web_agent.py#L3166) | 3166 | `"                ) as pool:"` | — |
| [SRC-1AE03B9EC3-L003167](../../agents/web_agent.py#L3167) | 3167 | `"                    futures = {"` | — |
| [SRC-1AE03B9EC3-L003168](../../agents/web_agent.py#L3168) | 3168 | `"                        pool.submit(self._search_web, query): query"` | — |
| [SRC-1AE03B9EC3-L003169](../../agents/web_agent.py#L3169) | 3169 | `"                        for query in expansion_queries"` | — |
| [SRC-1AE03B9EC3-L003170](../../agents/web_agent.py#L3170) | 3170 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L003171](../../agents/web_agent.py#L3171) | 3171 | `"                    for future in as_completed(futures):"` | — |
| [SRC-1AE03B9EC3-L003172](../../agents/web_agent.py#L3172) | 3172 | `"                        query = futures[future]"` | — |
| [SRC-1AE03B9EC3-L003173](../../agents/web_agent.py#L3173) | 3173 | `"                        search_started_queries += 1"` | — |
| [SRC-1AE03B9EC3-L003174](../../agents/web_agent.py#L3174) | 3174 | `"                        try:"` | — |
| [SRC-1AE03B9EC3-L003175](../../agents/web_agent.py#L3175) | 3175 | `"                            results = future.result()"` | — |
| [SRC-1AE03B9EC3-L003176](../../agents/web_agent.py#L3176) | 3176 | `"                        except (RequestBudgetExceeded, RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L003177](../../agents/web_agent.py#L3177) | 3177 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L003178](../../agents/web_agent.py#L3178) | 3178 | `"                                f\"تعذر بحث زاوية إضافية «{query[:70]}»: {exc}\""` | — |
| [SRC-1AE03B9EC3-L003179](../../agents/web_agent.py#L3179) | 3179 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L003180](../../agents/web_agent.py#L3180) | 3180 | `"                            query_counts.append({\"query\": query, \"results\": 0})"` | — |
| [SRC-1AE03B9EC3-L003181](../../agents/web_agent.py#L3181) | 3181 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L003182](../../agents/web_agent.py#L3182) | 3182 | `"                        query_counts.append({\"query\": query, \"results\": len(results)})"` | — |
| [SRC-1AE03B9EC3-L003183](../../agents/web_agent.py#L3183) | 3183 | `"                        grouped: dict[str, list[dict[str, Any]]] = {}"` | — |
| [SRC-1AE03B9EC3-L003184](../../agents/web_agent.py#L3184) | 3184 | `"                        for source in results:"` | — |
| [SRC-1AE03B9EC3-L003185](../../agents/web_agent.py#L3185) | 3185 | `"                            grouped.setdefault("` | — |
| [SRC-1AE03B9EC3-L003186](../../agents/web_agent.py#L3186) | 3186 | `"                                str(source.get(\"provider\") or \"web_search\"), []"` | — |
| [SRC-1AE03B9EC3-L003187](../../agents/web_agent.py#L3187) | 3187 | `"                            ).append(source)"` | — |
| [SRC-1AE03B9EC3-L003188](../../agents/web_agent.py#L3188) | 3188 | `"                        for provider, items in grouped.items():"` | — |
| [SRC-1AE03B9EC3-L003189](../../agents/web_agent.py#L3189) | 3189 | `"                            items.sort(key=lambda item: int(item.get(\"provider_rank\", 999)))"` | — |
| [SRC-1AE03B9EC3-L003190](../../agents/web_agent.py#L3190) | 3190 | `"                            batches.append({"` | — |
| [SRC-1AE03B9EC3-L003191](../../agents/web_agent.py#L3191) | 3191 | `"                                \"query\": query, \"provider\": provider, \"results\": items"` | — |
| [SRC-1AE03B9EC3-L003192](../../agents/web_agent.py#L3192) | 3192 | `"                            })"` | — |
| [SRC-1AE03B9EC3-L003193](../../agents/web_agent.py#L3193) | 3193 | `"                queries.extend(expansion_queries)"` | — |
| [SRC-1AE03B9EC3-L003194](../../agents/web_agent.py#L3194) | 3194 | `"        # Report queries actually selected, not planned queries skipped to reserve repair capacity."` | — |
| [SRC-1AE03B9EC3-L003195](../../agents/web_agent.py#L3195) | 3195 | `"        plan[\"queries\"] = list(dict.fromkeys(queries))"` | — |
| [SRC-1AE03B9EC3-L003196](../../agents/web_agent.py#L3196) | 3196 | `""` | — |
| [SRC-1AE03B9EC3-L003197](../../agents/web_agent.py#L3197) | 3197 | `"        # Google News RSS is included concurrently by _search_web for freshness-bearing queries."` | — |
| [SRC-1AE03B9EC3-L003198](../../agents/web_agent.py#L3198) | 3198 | `""` | — |
| [SRC-1AE03B9EC3-L003199](../../agents/web_agent.py#L3199) | 3199 | `"        # A social-focused task uses public social endpoints in parallel with indexed"` | — |
| [SRC-1AE03B9EC3-L003200](../../agents/web_agent.py#L3200) | 3200 | `"        # public pages. No login, private profile, session cookie or anti-bot bypass."` | — |
| [SRC-1AE03B9EC3-L003201](../../agents/web_agent.py#L3201) | 3201 | `"        social_results: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L003202](../../agents/web_agent.py#L3202) | 3202 | `"        if plan.get(\"social_focus\") and queries:"` | — |
| [SRC-1AE03B9EC3-L003203](../../agents/web_agent.py#L3203) | 3203 | `"            requested_platforms = plan.get(\"platforms\") or []"` | — |
| [SRC-1AE03B9EC3-L003204](../../agents/web_agent.py#L3204) | 3204 | `"            if requested_platforms:"` | — |
| [SRC-1AE03B9EC3-L003205](../../agents/web_agent.py#L3205) | 3205 | `"                platforms = list(dict.fromkeys(requested_platforms))"` | — |
| [SRC-1AE03B9EC3-L003206](../../agents/web_agent.py#L3206) | 3206 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L003207](../../agents/web_agent.py#L3207) | 3207 | `"                # Broad social research: always try no-key public sources, and add"` | — |
| [SRC-1AE03B9EC3-L003208](../../agents/web_agent.py#L3208) | 3208 | `"                # official platform connectors only when they are configured."` | — |
| [SRC-1AE03B9EC3-L003209](../../agents/web_agent.py#L3209) | 3209 | `"                platforms = [\"reddit\", \"bluesky\"]"` | — |
| [SRC-1AE03B9EC3-L003210](../../agents/web_agent.py#L3210) | 3210 | `"                optional_connectors = {"` | — |
| [SRC-1AE03B9EC3-L003211](../../agents/web_agent.py#L3211) | 3211 | `"                    \"facebook\": bool("` | — |
| [SRC-1AE03B9EC3-L003212](../../agents/web_agent.py#L3212) | 3212 | `"                        os.getenv(\"FACEBOOK_PAGE_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L003213](../../agents/web_agent.py#L3213) | 3213 | `"                        and os.getenv(\"FACEBOOK_PAGE_IDS\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L003214](../../agents/web_agent.py#L3214) | 3214 | `"                    ),"` | — |
| [SRC-1AE03B9EC3-L003215](../../agents/web_agent.py#L3215) | 3215 | `"                    \"instagram\": bool("` | — |
| [SRC-1AE03B9EC3-L003216](../../agents/web_agent.py#L3216) | 3216 | `"                        os.getenv(\"INSTAGRAM_USER_ID\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L003217](../../agents/web_agent.py#L3217) | 3217 | `"                        and os.getenv(\"INSTAGRAM_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L003218](../../agents/web_agent.py#L3218) | 3218 | `"                    ),"` | — |
| [SRC-1AE03B9EC3-L003219](../../agents/web_agent.py#L3219) | 3219 | `"                    \"x\": bool(os.getenv(\"X_BEARER_TOKEN\", \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L003220](../../agents/web_agent.py#L3220) | 3220 | `"                    \"youtube\": bool(os.getenv(\"YOUTUBE_API_KEY\", \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L003221](../../agents/web_agent.py#L3221) | 3221 | `"                }"` | — |
| [SRC-1AE03B9EC3-L003222](../../agents/web_agent.py#L3222) | 3222 | `"                platforms.extend("` | — |
| [SRC-1AE03B9EC3-L003223](../../agents/web_agent.py#L3223) | 3223 | `"                    name for name, ready in optional_connectors.items()"` | — |
| [SRC-1AE03B9EC3-L003224](../../agents/web_agent.py#L3224) | 3224 | `"                    if ready and name not in platforms"` | — |
| [SRC-1AE03B9EC3-L003225](../../agents/web_agent.py#L3225) | 3225 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003226](../../agents/web_agent.py#L3226) | 3226 | `"            social_results, social_warnings = self._search_social((queries[0] if queries else \"\"), platforms)"` | — |
| [SRC-1AE03B9EC3-L003227](../../agents/web_agent.py#L3227) | 3227 | `"            warnings.extend(social_warnings)"` | — |
| [SRC-1AE03B9EC3-L003228](../../agents/web_agent.py#L3228) | 3228 | `"            social_groups: dict[str, list[dict[str, Any]]] = {}"` | — |
| [SRC-1AE03B9EC3-L003229](../../agents/web_agent.py#L3229) | 3229 | `"            for source in social_results:"` | — |
| [SRC-1AE03B9EC3-L003230](../../agents/web_agent.py#L3230) | 3230 | `"                social_groups.setdefault(str(source.get(\"provider\") or \"social\"), []).append(source)"` | — |
| [SRC-1AE03B9EC3-L003231](../../agents/web_agent.py#L3231) | 3231 | `"            for provider, items in social_groups.items():"` | — |
| [SRC-1AE03B9EC3-L003232](../../agents/web_agent.py#L3232) | 3232 | `"                items.sort(key=lambda item: int(item.get(\"provider_rank\", 999)))"` | — |
| [SRC-1AE03B9EC3-L003233](../../agents/web_agent.py#L3233) | 3233 | `"                batches.append({\"query\": (queries[0] if queries else \"\"), \"provider\": provider, \"results\": items})"` | — |
| [SRC-1AE03B9EC3-L003234](../../agents/web_agent.py#L3234) | 3234 | `""` | — |
| [SRC-1AE03B9EC3-L003235](../../agents/web_agent.py#L3235) | 3235 | `"        # Explicit URLs are first-class inputs: fetch the page the user actually asked about"` | — |
| [SRC-1AE03B9EC3-L003236](../../agents/web_agent.py#L3236) | 3236 | `"        # instead of relying on a search engine to rediscover it. URL and DNS checks still apply."` | — |
| [SRC-1AE03B9EC3-L003237](../../agents/web_agent.py#L3237) | 3237 | `"        direct_urls: list[str] = []"` | — |
| [SRC-1AE03B9EC3-L003238](../../agents/web_agent.py#L3238) | 3238 | `"        for value in plan.get(\"direct_urls\", [])[:5]:"` | — |
| [SRC-1AE03B9EC3-L003239](../../agents/web_agent.py#L3239) | 3239 | `"            safe_url = _public_http_url(value)"` | — |
| [SRC-1AE03B9EC3-L003240](../../agents/web_agent.py#L3240) | 3240 | `"            if safe_url and not _blocked_source_url(safe_url) and safe_url not in direct_urls:"` | — |
| [SRC-1AE03B9EC3-L003241](../../agents/web_agent.py#L3241) | 3241 | `"                direct_urls.append(safe_url)"` | — |
| [SRC-1AE03B9EC3-L003242](../../agents/web_agent.py#L3242) | 3242 | `"        for direct_url in direct_urls:"` | — |
| [SRC-1AE03B9EC3-L003243](../../agents/web_agent.py#L3243) | 3243 | `"            batches.append({"` | — |
| [SRC-1AE03B9EC3-L003244](../../agents/web_agent.py#L3244) | 3244 | `"                \"query\": (queries[0] if queries else \"\"),"` | — |
| [SRC-1AE03B9EC3-L003245](../../agents/web_agent.py#L3245) | 3245 | `"                \"provider\": \"user_supplied_url\","` | — |
| [SRC-1AE03B9EC3-L003246](../../agents/web_agent.py#L3246) | 3246 | `"                \"results\": [{"` | — |
| [SRC-1AE03B9EC3-L003247](../../agents/web_agent.py#L3247) | 3247 | `"                    \"title\": \"رابط قدمه المستخدم للتحليل\","` | — |
| [SRC-1AE03B9EC3-L003248](../../agents/web_agent.py#L3248) | 3248 | `"                    \"url\": direct_url,"` | — |
| [SRC-1AE03B9EC3-L003249](../../agents/web_agent.py#L3249) | 3249 | `"                    \"snippet\": \"\","` | — |
| [SRC-1AE03B9EC3-L003250](../../agents/web_agent.py#L3250) | 3250 | `"                    \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L003251](../../agents/web_agent.py#L3251) | 3251 | `"                    \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L003252](../../agents/web_agent.py#L3252) | 3252 | `"                    \"provider\": \"user_supplied_url\","` | — |
| [SRC-1AE03B9EC3-L003253](../../agents/web_agent.py#L3253) | 3253 | `"                    \"provider_rank\": 1,"` | — |
| [SRC-1AE03B9EC3-L003254](../../agents/web_agent.py#L3254) | 3254 | `"                    \"search_query\": (queries[0] if queries else \"\"),"` | — |
| [SRC-1AE03B9EC3-L003255](../../agents/web_agent.py#L3255) | 3255 | `"                    \"published_at\": \"\","` | — |
| [SRC-1AE03B9EC3-L003256](../../agents/web_agent.py#L3256) | 3256 | `"                }],"` | — |
| [SRC-1AE03B9EC3-L003257](../../agents/web_agent.py#L3257) | 3257 | `"            })"` | — |
| [SRC-1AE03B9EC3-L003258](../../agents/web_agent.py#L3258) | 3258 | `""` | — |
| [SRC-1AE03B9EC3-L003259](../../agents/web_agent.py#L3259) | 3259 | `"        raw_results_count = sum(len(batch.get(\"results\", [])) for batch in batches if isinstance(batch, dict) and isinstance(batch.get(\"results\", []), list))"` | — |
| [SRC-1AE03B9EC3-L003260](../../agents/web_agent.py#L3260) | 3260 | `"        sources = fuse_ranked_results(batches, limit=MAX_SEARCH_RESULTS)"` | — |
| [SRC-1AE03B9EC3-L003261](../../agents/web_agent.py#L3261) | 3261 | `""` | — |
| [SRC-1AE03B9EC3-L003262](../../agents/web_agent.py#L3262) | 3262 | `"        # Keep at least one returned source per explicit criterion query in the"` | — |
| [SRC-1AE03B9EC3-L003263](../../agents/web_agent.py#L3263) | 3263 | `"        # bounded source set sent to synthesis. Global fusion can otherwise crowd"` | — |
| [SRC-1AE03B9EC3-L003264](../../agents/web_agent.py#L3264) | 3264 | `"        # lower-ranked criterion results out before the model can inspect them."` | — |
| [SRC-1AE03B9EC3-L003265](../../agents/web_agent.py#L3265) | 3265 | `"        requirement_queries = plan.get(\"requirement_queries\", [])"` | — |
| [SRC-1AE03B9EC3-L003266](../../agents/web_agent.py#L3266) | 3266 | `"        if isinstance(requirement_queries, list) and requirement_queries:"` | — |
| [SRC-1AE03B9EC3-L003267](../../agents/web_agent.py#L3267) | 3267 | `"            globally_fused = sources"` | — |
| [SRC-1AE03B9EC3-L003268](../../agents/web_agent.py#L3268) | 3268 | `"            globally_fused_by_url = {"` | — |
| [SRC-1AE03B9EC3-L003269](../../agents/web_agent.py#L3269) | 3269 | `"                self._normalized_source_url_key(item.get(\"url\", \"\")): item"` | — |
| [SRC-1AE03B9EC3-L003270](../../agents/web_agent.py#L3270) | 3270 | `"                for item in globally_fused"` | — |
| [SRC-1AE03B9EC3-L003271](../../agents/web_agent.py#L3271) | 3271 | `"                if self._normalized_source_url_key(item.get(\"url\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L003272](../../agents/web_agent.py#L3272) | 3272 | `"            }"` | — |
| [SRC-1AE03B9EC3-L003273](../../agents/web_agent.py#L3273) | 3273 | `"            pinned_by_url: dict[str, dict[str, Any]] = {}"` | — |
| [SRC-1AE03B9EC3-L003274](../../agents/web_agent.py#L3274) | 3274 | `"            pinned_sources: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L003275](../../agents/web_agent.py#L3275) | 3275 | `"            for requirement in requirement_queries[:MAX_PLAN_QUERIES]:"` | — |
| [SRC-1AE03B9EC3-L003276](../../agents/web_agent.py#L3276) | 3276 | `"                if not isinstance(requirement, dict):"` | — |
| [SRC-1AE03B9EC3-L003277](../../agents/web_agent.py#L3277) | 3277 | `"                    continue"` | — |
| [SRC-1AE03B9EC3-L003278](../../agents/web_agent.py#L3278) | 3278 | `"                target_query = compact_search_query(str(requirement.get(\"query\") or \"\"))"` | — |
| [SRC-1AE03B9EC3-L003279](../../agents/web_agent.py#L3279) | 3279 | `"                if not target_query:"` | — |
| [SRC-1AE03B9EC3-L003280](../../agents/web_agent.py#L3280) | 3280 | `"                    continue"` | — |
| [SRC-1AE03B9EC3-L003281](../../agents/web_agent.py#L3281) | 3281 | `"                query_key = re.sub(r\"\\s+\", \" \", target_query).strip().casefold()"` | — |
| [SRC-1AE03B9EC3-L003282](../../agents/web_agent.py#L3282) | 3282 | `"                criterion_batches = ["` | — |
| [SRC-1AE03B9EC3-L003283](../../agents/web_agent.py#L3283) | 3283 | `"                    batch for batch in batches"` | — |
| [SRC-1AE03B9EC3-L003284](../../agents/web_agent.py#L3284) | 3284 | `"                    if re.sub("` | — |
| [SRC-1AE03B9EC3-L003285](../../agents/web_agent.py#L3285) | 3285 | `"                        r\"\\s+\", \" \", str(batch.get(\"query\") or \"\")"` | — |
| [SRC-1AE03B9EC3-L003286](../../agents/web_agent.py#L3286) | 3286 | `"                    ).strip().casefold() == query_key"` | — |
| [SRC-1AE03B9EC3-L003287](../../agents/web_agent.py#L3287) | 3287 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L003288](../../agents/web_agent.py#L3288) | 3288 | `"                criterion_candidates = fuse_ranked_results("` | — |
| [SRC-1AE03B9EC3-L003289](../../agents/web_agent.py#L3289) | 3289 | `"                    criterion_batches, limit=MAX_SEARCH_RESULTS"` | — |
| [SRC-1AE03B9EC3-L003290](../../agents/web_agent.py#L3290) | 3290 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003291](../../agents/web_agent.py#L3291) | 3291 | `"                candidate = None"` | — |
| [SRC-1AE03B9EC3-L003292](../../agents/web_agent.py#L3292) | 3292 | `"                if criterion_candidates:"` | — |
| [SRC-1AE03B9EC3-L003293](../../agents/web_agent.py#L3293) | 3293 | `"                    criterion_ledger = build_requirement_evidence_ledger("` | — |
| [SRC-1AE03B9EC3-L003294](../../agents/web_agent.py#L3294) | 3294 | `"                        [str(requirement.get(\"target\") or \"\")],"` | — |
| [SRC-1AE03B9EC3-L003295](../../agents/web_agent.py#L3295) | 3295 | `"                        criterion_candidates,"` | — |
| [SRC-1AE03B9EC3-L003296](../../agents/web_agent.py#L3296) | 3296 | `"                        [requirement],"` | — |
| [SRC-1AE03B9EC3-L003297](../../agents/web_agent.py#L3297) | 3297 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L003298](../../agents/web_agent.py#L3298) | 3298 | `"                    candidate_indexes = ("` | — |
| [SRC-1AE03B9EC3-L003299](../../agents/web_agent.py#L3299) | 3299 | `"                        criterion_ledger[0].get(\"candidate_source_indexes\", [])"` | — |
| [SRC-1AE03B9EC3-L003300](../../agents/web_agent.py#L3300) | 3300 | `"                        if criterion_ledger else []"` | — |
| [SRC-1AE03B9EC3-L003301](../../agents/web_agent.py#L3301) | 3301 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L003302](../../agents/web_agent.py#L3302) | 3302 | `"                    if candidate_indexes:"` | — |
| [SRC-1AE03B9EC3-L003303](../../agents/web_agent.py#L3303) | 3303 | `"                        candidate = criterion_candidates[int(candidate_indexes[0]) - 1]"` | — |
| [SRC-1AE03B9EC3-L003304](../../agents/web_agent.py#L3304) | 3304 | `"                if candidate is None:"` | — |
| [SRC-1AE03B9EC3-L003305](../../agents/web_agent.py#L3305) | 3305 | `"                    candidate = next("` | — |
| [SRC-1AE03B9EC3-L003306](../../agents/web_agent.py#L3306) | 3306 | `"                        ("` | — |
| [SRC-1AE03B9EC3-L003307](../../agents/web_agent.py#L3307) | 3307 | `"                            item for item in globally_fused"` | — |
| [SRC-1AE03B9EC3-L003308](../../agents/web_agent.py#L3308) | 3308 | `"                            if query_key in {"` | — |
| [SRC-1AE03B9EC3-L003309](../../agents/web_agent.py#L3309) | 3309 | `"                                re.sub(r\"\\s+\", \" \", str(value)).strip().casefold()"` | — |
| [SRC-1AE03B9EC3-L003310](../../agents/web_agent.py#L3310) | 3310 | `"                                for value in item.get(\"queries\", [])"` | — |
| [SRC-1AE03B9EC3-L003311](../../agents/web_agent.py#L3311) | 3311 | `"                            }"` | — |
| [SRC-1AE03B9EC3-L003312](../../agents/web_agent.py#L3312) | 3312 | `"                        ),"` | — |
| [SRC-1AE03B9EC3-L003313](../../agents/web_agent.py#L3313) | 3313 | `"                        criterion_candidates[0] if criterion_candidates else None,"` | — |
| [SRC-1AE03B9EC3-L003314](../../agents/web_agent.py#L3314) | 3314 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L003315](../../agents/web_agent.py#L3315) | 3315 | `"                if not candidate:"` | — |
| [SRC-1AE03B9EC3-L003316](../../agents/web_agent.py#L3316) | 3316 | `"                    continue"` | — |
| [SRC-1AE03B9EC3-L003317](../../agents/web_agent.py#L3317) | 3317 | `"                source_key = self._normalized_source_url_key(candidate.get(\"url\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L003318](../../agents/web_agent.py#L3318) | 3318 | `"                if not source_key:"` | — |
| [SRC-1AE03B9EC3-L003319](../../agents/web_agent.py#L3319) | 3319 | `"                    continue"` | — |
| [SRC-1AE03B9EC3-L003320](../../agents/web_agent.py#L3320) | 3320 | `"                selected = ("` | — |
| [SRC-1AE03B9EC3-L003321](../../agents/web_agent.py#L3321) | 3321 | `"                    pinned_by_url.get(source_key)"` | — |
| [SRC-1AE03B9EC3-L003322](../../agents/web_agent.py#L3322) | 3322 | `"                    or globally_fused_by_url.get(source_key)"` | — |
| [SRC-1AE03B9EC3-L003323](../../agents/web_agent.py#L3323) | 3323 | `"                    or candidate"` | — |
| [SRC-1AE03B9EC3-L003324](../../agents/web_agent.py#L3324) | 3324 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003325](../../agents/web_agent.py#L3325) | 3325 | `"                if source_key not in pinned_by_url:"` | — |
| [SRC-1AE03B9EC3-L003326](../../agents/web_agent.py#L3326) | 3326 | `"                    pinned_by_url[source_key] = selected"` | — |
| [SRC-1AE03B9EC3-L003327](../../agents/web_agent.py#L3327) | 3327 | `"                    pinned_sources.append(selected)"` | — |
| [SRC-1AE03B9EC3-L003328](../../agents/web_agent.py#L3328) | 3328 | `"                selected_queries = selected.setdefault(\"queries\", [])"` | — |
| [SRC-1AE03B9EC3-L003329](../../agents/web_agent.py#L3329) | 3329 | `"                if target_query not in selected_queries:"` | — |
| [SRC-1AE03B9EC3-L003330](../../agents/web_agent.py#L3330) | 3330 | `"                    selected_queries.append(target_query)"` | — |
| [SRC-1AE03B9EC3-L003331](../../agents/web_agent.py#L3331) | 3331 | `"            pinned_keys = set(pinned_by_url)"` | — |
| [SRC-1AE03B9EC3-L003332](../../agents/web_agent.py#L3332) | 3332 | `"            sources = ("` | — |
| [SRC-1AE03B9EC3-L003333](../../agents/web_agent.py#L3333) | 3333 | `"                pinned_sources"` | — |
| [SRC-1AE03B9EC3-L003334](../../agents/web_agent.py#L3334) | 3334 | `"                + ["` | — |
| [SRC-1AE03B9EC3-L003335](../../agents/web_agent.py#L3335) | 3335 | `"                    item for item in globally_fused"` | — |
| [SRC-1AE03B9EC3-L003336](../../agents/web_agent.py#L3336) | 3336 | `"                    if self._normalized_source_url_key(item.get(\"url\", \"\")) not in pinned_keys"` | — |
| [SRC-1AE03B9EC3-L003337](../../agents/web_agent.py#L3337) | 3337 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L003338](../../agents/web_agent.py#L3338) | 3338 | `"            )[:MAX_SEARCH_RESULTS]"` | — |
| [SRC-1AE03B9EC3-L003339](../../agents/web_agent.py#L3339) | 3339 | `""` | — |
| [SRC-1AE03B9EC3-L003340](../../agents/web_agent.py#L3340) | 3340 | `"        for source in sources:"` | — |
| [SRC-1AE03B9EC3-L003341](../../agents/web_agent.py#L3341) | 3341 | `"            source.setdefault(\"page_fetch_status\", \"not_attempted\")"` | — |
| [SRC-1AE03B9EC3-L003342](../../agents/web_agent.py#L3342) | 3342 | `"        # Fetch page text only for the best few public URLs; do it concurrently with strict bounds."` | — |
| [SRC-1AE03B9EC3-L003343](../../agents/web_agent.py#L3343) | 3343 | `"        fetch_targets = sources[:MAX_FETCHED_PAGES]"` | — |
| [SRC-1AE03B9EC3-L003344](../../agents/web_agent.py#L3344) | 3344 | `"        for source in fetch_targets:"` | — |
| [SRC-1AE03B9EC3-L003345](../../agents/web_agent.py#L3345) | 3345 | `"            source[\"page_fetch_status\"] = \"attempted\""` | — |
| [SRC-1AE03B9EC3-L003346](../../agents/web_agent.py#L3346) | 3346 | `"        fetched_count = 0"` | — |
| [SRC-1AE03B9EC3-L003347](../../agents/web_agent.py#L3347) | 3347 | `"        if fetch_targets:"` | — |
| [SRC-1AE03B9EC3-L003348](../../agents/web_agent.py#L3348) | 3348 | `"            with ThreadPoolExecutor(max_workers=min(4, len(fetch_targets))) as pool:"` | — |
| [SRC-1AE03B9EC3-L003349](../../agents/web_agent.py#L3349) | 3349 | `"                futures = {"` | — |
| [SRC-1AE03B9EC3-L003350](../../agents/web_agent.py#L3350) | 3350 | `"                    pool.submit(self._fetch_page, source[\"url\"]): source"` | — |
| [SRC-1AE03B9EC3-L003351](../../agents/web_agent.py#L3351) | 3351 | `"                    for source in fetch_targets"` | — |
| [SRC-1AE03B9EC3-L003352](../../agents/web_agent.py#L3352) | 3352 | `"                }"` | — |
| [SRC-1AE03B9EC3-L003353](../../agents/web_agent.py#L3353) | 3353 | `"                for future in as_completed(futures):"` | — |
| [SRC-1AE03B9EC3-L003354](../../agents/web_agent.py#L3354) | 3354 | `"                    source = futures[future]"` | — |
| [SRC-1AE03B9EC3-L003355](../../agents/web_agent.py#L3355) | 3355 | `"                    try:"` | — |
| [SRC-1AE03B9EC3-L003356](../../agents/web_agent.py#L3356) | 3356 | `"                        fetch_result = future.result()"` | — |
| [SRC-1AE03B9EC3-L003357](../../agents/web_agent.py#L3357) | 3357 | `"                    except RequestBudgetExceeded as exc:"` | — |
| [SRC-1AE03B9EC3-L003358](../../agents/web_agent.py#L3358) | 3358 | `"                        source[\"page_fetch_status\"] = \"budget_exhausted\""` | — |
| [SRC-1AE03B9EC3-L003359](../../agents/web_agent.py#L3359) | 3359 | `"                        source[\"page_fetch_error_class\"] = type(exc).__name__"` | — |
| [SRC-1AE03B9EC3-L003360](../../agents/web_agent.py#L3360) | 3360 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L003361](../../agents/web_agent.py#L3361) | 3361 | `"                    except (RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L003362](../../agents/web_agent.py#L3362) | 3362 | `"                        source[\"page_fetch_status\"] = \"fetch_failed\""` | — |
| [SRC-1AE03B9EC3-L003363](../../agents/web_agent.py#L3363) | 3363 | `"                        source[\"page_fetch_error_class\"] = type(exc).__name__"` | — |
| [SRC-1AE03B9EC3-L003364](../../agents/web_agent.py#L3364) | 3364 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L003365](../../agents/web_agent.py#L3365) | 3365 | `"                    title, page_text = fetch_result"` | — |
| [SRC-1AE03B9EC3-L003366](../../agents/web_agent.py#L3366) | 3366 | `"                    observed_status = getattr(fetch_result, \"status\", None)"` | — |
| [SRC-1AE03B9EC3-L003367](../../agents/web_agent.py#L3367) | 3367 | `"                    error_class = getattr(fetch_result, \"error_class\", None)"` | — |
| [SRC-1AE03B9EC3-L003368](../../agents/web_agent.py#L3368) | 3368 | `"                    if title:"` | — |
| [SRC-1AE03B9EC3-L003369](../../agents/web_agent.py#L3369) | 3369 | `"                        source[\"title\"] = title"` | — |
| [SRC-1AE03B9EC3-L003370](../../agents/web_agent.py#L3370) | 3370 | `"                    if page_text and page_text.strip():"` | — |
| [SRC-1AE03B9EC3-L003371](../../agents/web_agent.py#L3371) | 3371 | `"                        source[\"page_text\"] = page_text"` | — |
| [SRC-1AE03B9EC3-L003372](../../agents/web_agent.py#L3372) | 3372 | `"                        source[\"snippet\"] = page_text[:1800]"` | — |
| [SRC-1AE03B9EC3-L003373](../../agents/web_agent.py#L3373) | 3373 | `"                        source[\"page_fetched\"] = True"` | — |
| [SRC-1AE03B9EC3-L003374](../../agents/web_agent.py#L3374) | 3374 | `"                        source[\"page_fetch_status\"] = ("` | — |
| [SRC-1AE03B9EC3-L003375](../../agents/web_agent.py#L3375) | 3375 | `"                            observed_status"` | — |
| [SRC-1AE03B9EC3-L003376](../../agents/web_agent.py#L3376) | 3376 | `"                            if observed_status in {\"content_extracted\", \"partial_extraction\"}"` | — |
| [SRC-1AE03B9EC3-L003377](../../agents/web_agent.py#L3377) | 3377 | `"                            else \"partial_extraction\""` | — |
| [SRC-1AE03B9EC3-L003378](../../agents/web_agent.py#L3378) | 3378 | `"                            if len(page_text) >= MAX_PAGE_TEXT_CHARS"` | — |
| [SRC-1AE03B9EC3-L003379](../../agents/web_agent.py#L3379) | 3379 | `"                            else \"content_extracted\""` | — |
| [SRC-1AE03B9EC3-L003380](../../agents/web_agent.py#L3380) | 3380 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L003381](../../agents/web_agent.py#L3381) | 3381 | `"                        if error_class:"` | — |
| [SRC-1AE03B9EC3-L003382](../../agents/web_agent.py#L3382) | 3382 | `"                            source[\"page_fetch_error_class\"] = str(error_class)[:80]"` | — |
| [SRC-1AE03B9EC3-L003383](../../agents/web_agent.py#L3383) | 3383 | `"                        else:"` | — |
| [SRC-1AE03B9EC3-L003384](../../agents/web_agent.py#L3384) | 3384 | `"                            source.pop(\"page_fetch_error_class\", None)"` | — |
| [SRC-1AE03B9EC3-L003385](../../agents/web_agent.py#L3385) | 3385 | `"                        fetched_count += 1"` | — |
| [SRC-1AE03B9EC3-L003386](../../agents/web_agent.py#L3386) | 3386 | `"                        if source[\"page_fetch_status\"] == \"partial_extraction\":"` | — |
| [SRC-1AE03B9EC3-L003387](../../agents/web_agent.py#L3387) | 3387 | `"                            host = urllib.parse.urlparse(source.get(\"url\", \"\")).hostname or \"المصدر\""` | — |
| [SRC-1AE03B9EC3-L003388](../../agents/web_agent.py#L3388) | 3388 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L003389](../../agents/web_agent.py#L3389) | 3389 | `"                                f\"استُخرج جزء من نص {host} فقط؛ قد تكون الصفحة أطول من الحد الآمن.\""` | — |
| [SRC-1AE03B9EC3-L003390](../../agents/web_agent.py#L3390) | 3390 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L003391](../../agents/web_agent.py#L3391) | 3391 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L003392](../../agents/web_agent.py#L3392) | 3392 | `"                        source[\"page_fetched\"] = False"` | — |
| [SRC-1AE03B9EC3-L003393](../../agents/web_agent.py#L3393) | 3393 | `"                        if observed_status in {"` | — |
| [SRC-1AE03B9EC3-L003394](../../agents/web_agent.py#L3394) | 3394 | `"                            \"rejected_url\", \"blocked_or_unresolved_host\", \"blocked_connection_target\","` | — |
| [SRC-1AE03B9EC3-L003395](../../agents/web_agent.py#L3395) | 3395 | `"                            \"redirect_failed\", \"redirect_rejected\", \"redirect_limit\", \"http_error\","` | — |
| [SRC-1AE03B9EC3-L003396](../../agents/web_agent.py#L3396) | 3396 | `"                            \"unsupported_content_type\", \"page_too_large\", \"network_error\","` | — |
| [SRC-1AE03B9EC3-L003397](../../agents/web_agent.py#L3397) | 3397 | `"                            \"empty_content\", \"no_text_extracted\", \"budget_exhausted\","` | — |
| [SRC-1AE03B9EC3-L003398](../../agents/web_agent.py#L3398) | 3398 | `"                        }:"` | — |
| [SRC-1AE03B9EC3-L003399](../../agents/web_agent.py#L3399) | 3399 | `"                            source[\"page_fetch_status\"] = observed_status"` | — |
| [SRC-1AE03B9EC3-L003400](../../agents/web_agent.py#L3400) | 3400 | `"                        else:"` | — |
| [SRC-1AE03B9EC3-L003401](../../agents/web_agent.py#L3401) | 3401 | `"                            source[\"page_fetch_status\"] = \"no_text_extracted\""` | — |
| [SRC-1AE03B9EC3-L003402](../../agents/web_agent.py#L3402) | 3402 | `"                        if error_class:"` | — |
| [SRC-1AE03B9EC3-L003403](../../agents/web_agent.py#L3403) | 3403 | `"                            source[\"page_fetch_error_class\"] = str(error_class)[:80]"` | — |
| [SRC-1AE03B9EC3-L003404](../../agents/web_agent.py#L3404) | 3404 | `"                        host = urllib.parse.urlparse(source.get(\"url\", \"\")).hostname or \"المصدر\""` | — |
| [SRC-1AE03B9EC3-L003405](../../agents/web_agent.py#L3405) | 3405 | `"                        if source[\"page_fetch_status\"] in {\"no_text_extracted\", \"empty_content\"}:"` | — |
| [SRC-1AE03B9EC3-L003406](../../agents/web_agent.py#L3406) | 3406 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L003407](../../agents/web_agent.py#L3407) | 3407 | `"                                f\"لم يمكن استخراج نص من {host}؛ جُلبت الصفحة أو جرت محاولة قراءتها لكن قد تكون ديناميكية أو محجوبة.\""` | — |
| [SRC-1AE03B9EC3-L003408](../../agents/web_agent.py#L3408) | 3408 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L003409](../../agents/web_agent.py#L3409) | 3409 | `"                        else:"` | — |
| [SRC-1AE03B9EC3-L003410](../../agents/web_agent.py#L3410) | 3410 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L003411](../../agents/web_agent.py#L3411) | 3411 | `"                                f\"تعذرت قراءة نص {host} بسبب حالة الجلب: {source['page_fetch_status']}.\""` | — |
| [SRC-1AE03B9EC3-L003412](../../agents/web_agent.py#L3412) | 3412 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L003413](../../agents/web_agent.py#L3413) | 3413 | `""` | — |
| [SRC-1AE03B9EC3-L003414](../../agents/web_agent.py#L3414) | 3414 | `"        # Reorder on consensus first, and keep clear machine-readable provenance."` | — |
| [SRC-1AE03B9EC3-L003415](../../agents/web_agent.py#L3415) | 3415 | `"        sources.sort(key=lambda source: source.get(\"rank_score\", 0), reverse=True)"` | — |
| [SRC-1AE03B9EC3-L003416](../../agents/web_agent.py#L3416) | 3416 | `"        providers = sorted({"` | — |
| [SRC-1AE03B9EC3-L003417](../../agents/web_agent.py#L3417) | 3417 | `"            provider"` | — |
| [SRC-1AE03B9EC3-L003418](../../agents/web_agent.py#L3418) | 3418 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L003419](../../agents/web_agent.py#L3419) | 3419 | `"            for provider in source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L003420](../../agents/web_agent.py#L3420) | 3420 | `"        })"` | — |
| [SRC-1AE03B9EC3-L003421](../../agents/web_agent.py#L3421) | 3421 | `"        platform_counts: dict[str, int] = {}"` | — |
| [SRC-1AE03B9EC3-L003422](../../agents/web_agent.py#L3422) | 3422 | `"        for source in sources:"` | — |
| [SRC-1AE03B9EC3-L003423](../../agents/web_agent.py#L3423) | 3423 | `"            label = source.get(\"platform\", \"web\")"` | — |
| [SRC-1AE03B9EC3-L003424](../../agents/web_agent.py#L3424) | 3424 | `"            platform_counts[label] = platform_counts.get(label, 0) + 1"` | — |
| [SRC-1AE03B9EC3-L003425](../../agents/web_agent.py#L3425) | 3425 | `"        page_failure_statuses = {"` | — |
| [SRC-1AE03B9EC3-L003426](../../agents/web_agent.py#L3426) | 3426 | `"            \"fetch_failed\", \"no_text_extracted\", \"rejected_url\","` | — |
| [SRC-1AE03B9EC3-L003427](../../agents/web_agent.py#L3427) | 3427 | `"            \"blocked_or_unresolved_host\", \"blocked_connection_target\","` | — |
| [SRC-1AE03B9EC3-L003428](../../agents/web_agent.py#L3428) | 3428 | `"            \"redirect_failed\", \"redirect_rejected\", \"redirect_limit\","` | — |
| [SRC-1AE03B9EC3-L003429](../../agents/web_agent.py#L3429) | 3429 | `"            \"http_error\", \"unsupported_content_type\", \"page_too_large\","` | — |
| [SRC-1AE03B9EC3-L003430](../../agents/web_agent.py#L3430) | 3430 | `"            \"network_error\", \"empty_content\", \"budget_exhausted\","` | — |
| [SRC-1AE03B9EC3-L003431](../../agents/web_agent.py#L3431) | 3431 | `"        }"` | — |
| [SRC-1AE03B9EC3-L003432](../../agents/web_agent.py#L3432) | 3432 | `"        page_status_values = ("` | — |
| [SRC-1AE03B9EC3-L003433](../../agents/web_agent.py#L3433) | 3433 | `"            \"not_attempted\", \"attempted\", \"content_extracted\", \"partial_extraction\","` | — |
| [SRC-1AE03B9EC3-L003434](../../agents/web_agent.py#L3434) | 3434 | `"            \"no_text_extracted\", \"fetch_failed\", \"rejected_url\","` | — |
| [SRC-1AE03B9EC3-L003435](../../agents/web_agent.py#L3435) | 3435 | `"            \"blocked_or_unresolved_host\", \"blocked_connection_target\","` | — |
| [SRC-1AE03B9EC3-L003436](../../agents/web_agent.py#L3436) | 3436 | `"            \"redirect_failed\", \"redirect_rejected\", \"redirect_limit\","` | — |
| [SRC-1AE03B9EC3-L003437](../../agents/web_agent.py#L3437) | 3437 | `"            \"http_error\", \"unsupported_content_type\", \"page_too_large\","` | — |
| [SRC-1AE03B9EC3-L003438](../../agents/web_agent.py#L3438) | 3438 | `"            \"network_error\", \"empty_content\", \"budget_exhausted\","` | — |
| [SRC-1AE03B9EC3-L003439](../../agents/web_agent.py#L3439) | 3439 | `"        )"` | — |
| [SRC-1AE03B9EC3-L003440](../../agents/web_agent.py#L3440) | 3440 | `"        page_fetch_status_counts = {"` | — |
| [SRC-1AE03B9EC3-L003441](../../agents/web_agent.py#L3441) | 3441 | `"            status: sum(source.get(\"page_fetch_status\") == status for source in fetch_targets)"` | — |
| [SRC-1AE03B9EC3-L003442](../../agents/web_agent.py#L3442) | 3442 | `"            for status in page_status_values"` | — |
| [SRC-1AE03B9EC3-L003443](../../agents/web_agent.py#L3443) | 3443 | `"        }"` | — |
| [SRC-1AE03B9EC3-L003444](../../agents/web_agent.py#L3444) | 3444 | `"        provider_diagnostics = list(self._provider_diagnostics)"` | — |
| [SRC-1AE03B9EC3-L003445](../../agents/web_agent.py#L3445) | 3445 | `"        provider_candidates_received = sum("` | — |
| [SRC-1AE03B9EC3-L003446](../../agents/web_agent.py#L3446) | 3446 | `"            max(0, int(row.get(\"result_count\", 0) or 0))"` | — |
| [SRC-1AE03B9EC3-L003447](../../agents/web_agent.py#L3447) | 3447 | `"            for row in provider_diagnostics if isinstance(row, dict)"` | — |
| [SRC-1AE03B9EC3-L003448](../../agents/web_agent.py#L3448) | 3448 | `"        )"` | — |
| [SRC-1AE03B9EC3-L003449](../../agents/web_agent.py#L3449) | 3449 | `"        provider_candidates_accepted = sum("` | — |
| [SRC-1AE03B9EC3-L003450](../../agents/web_agent.py#L3450) | 3450 | `"            max(0, int(row.get(\"accepted_count\", 0) or 0))"` | — |
| [SRC-1AE03B9EC3-L003451](../../agents/web_agent.py#L3451) | 3451 | `"            for row in provider_diagnostics if isinstance(row, dict)"` | — |
| [SRC-1AE03B9EC3-L003452](../../agents/web_agent.py#L3452) | 3452 | `"        )"` | — |
| [SRC-1AE03B9EC3-L003453](../../agents/web_agent.py#L3453) | 3453 | `"        provider_candidates_rejected = sum("` | — |
| [SRC-1AE03B9EC3-L003454](../../agents/web_agent.py#L3454) | 3454 | `"            max(0, int(row.get(\"rejected_count\", 0) or 0))"` | — |
| [SRC-1AE03B9EC3-L003455](../../agents/web_agent.py#L3455) | 3455 | `"            for row in provider_diagnostics if isinstance(row, dict)"` | — |
| [SRC-1AE03B9EC3-L003456](../../agents/web_agent.py#L3456) | 3456 | `"        )"` | — |
| [SRC-1AE03B9EC3-L003457](../../agents/web_agent.py#L3457) | 3457 | `"        report = {"` | — |
| [SRC-1AE03B9EC3-L003458](../../agents/web_agent.py#L3458) | 3458 | `"            \"raw_results\": raw_results_count,"` | — |
| [SRC-1AE03B9EC3-L003459](../../agents/web_agent.py#L3459) | 3459 | `"            \"provider_candidates_received\": provider_candidates_received,"` | — |
| [SRC-1AE03B9EC3-L003460](../../agents/web_agent.py#L3460) | 3460 | `"            \"provider_candidates_accepted\": provider_candidates_accepted,"` | — |
| [SRC-1AE03B9EC3-L003461](../../agents/web_agent.py#L3461) | 3461 | `"            \"provider_candidates_rejected\": provider_candidates_rejected,"` | — |
| [SRC-1AE03B9EC3-L003462](../../agents/web_agent.py#L3462) | 3462 | `"            \"unique_urls\": len({"` | — |
| [SRC-1AE03B9EC3-L003463](../../agents/web_agent.py#L3463) | 3463 | `"                self._normalized_source_url_key(source.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L003464](../../agents/web_agent.py#L3464) | 3464 | `"                for source in sources"` | — |
| [SRC-1AE03B9EC3-L003465](../../agents/web_agent.py#L3465) | 3465 | `"                if self._normalized_source_url_key(source.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L003466](../../agents/web_agent.py#L3466) | 3466 | `"            }),"` | — |
| [SRC-1AE03B9EC3-L003467](../../agents/web_agent.py#L3467) | 3467 | `"            \"pages_content_extracted\": fetched_count,"` | — |
| [SRC-1AE03B9EC3-L003468](../../agents/web_agent.py#L3468) | 3468 | `"            \"pages_partial_extracted\": sum("` | — |
| [SRC-1AE03B9EC3-L003469](../../agents/web_agent.py#L3469) | 3469 | `"                source.get(\"page_fetch_status\") == \"partial_extraction\""` | — |
| [SRC-1AE03B9EC3-L003470](../../agents/web_agent.py#L3470) | 3470 | `"                for source in fetch_targets"` | — |
| [SRC-1AE03B9EC3-L003471](../../agents/web_agent.py#L3471) | 3471 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L003472](../../agents/web_agent.py#L3472) | 3472 | `"            \"pages_extract_failed\": sum("` | — |
| [SRC-1AE03B9EC3-L003473](../../agents/web_agent.py#L3473) | 3473 | `"                source.get(\"page_fetch_status\") in page_failure_statuses"` | — |
| [SRC-1AE03B9EC3-L003474](../../agents/web_agent.py#L3474) | 3474 | `"                for source in fetch_targets"` | — |
| [SRC-1AE03B9EC3-L003475](../../agents/web_agent.py#L3475) | 3475 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L003476](../../agents/web_agent.py#L3476) | 3476 | `"            \"page_fetch_status_counts\": page_fetch_status_counts,"` | — |
| [SRC-1AE03B9EC3-L003477](../../agents/web_agent.py#L3477) | 3477 | `"            \"queries_planned\": len(queries),"` | — |
| [SRC-1AE03B9EC3-L003478](../../agents/web_agent.py#L3478) | 3478 | `"            \"queries_attempted\": search_started_queries,"` | — |
| [SRC-1AE03B9EC3-L003479](../../agents/web_agent.py#L3479) | 3479 | `"            \"query_results\": query_counts,"` | — |
| [SRC-1AE03B9EC3-L003480](../../agents/web_agent.py#L3480) | 3480 | `"            \"unique_sources\": len(sources),"` | — |
| [SRC-1AE03B9EC3-L003481](../../agents/web_agent.py#L3481) | 3481 | `"            \"pages_fetched\": fetched_count,"` | — |
| [SRC-1AE03B9EC3-L003482](../../agents/web_agent.py#L3482) | 3482 | `"            \"providers_used\": providers,"` | — |
| [SRC-1AE03B9EC3-L003483](../../agents/web_agent.py#L3483) | 3483 | `"            \"provider_counts\": {"` | — |
| [SRC-1AE03B9EC3-L003484](../../agents/web_agent.py#L3484) | 3484 | `"                provider: sum(provider in source.get(\"providers\", []) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L003485](../../agents/web_agent.py#L3485) | 3485 | `"                for provider in providers"` | — |
| [SRC-1AE03B9EC3-L003486](../../agents/web_agent.py#L3486) | 3486 | `"            },"` | — |
| [SRC-1AE03B9EC3-L003487](../../agents/web_agent.py#L3487) | 3487 | `"            \"platform_counts\": platform_counts,"` | — |
| [SRC-1AE03B9EC3-L003488](../../agents/web_agent.py#L3488) | 3488 | `"            \"social_direct_results\": len(social_results),"` | — |
| [SRC-1AE03B9EC3-L003489](../../agents/web_agent.py#L3489) | 3489 | `"            \"expansion_queries\": expansion_queries,"` | — |
| [SRC-1AE03B9EC3-L003490](../../agents/web_agent.py#L3490) | 3490 | `"            \"evidence_signals\": evidence_signal_report(sources, plan.get(\"freshness\", \"any\")),"` | — |
| [SRC-1AE03B9EC3-L003491](../../agents/web_agent.py#L3491) | 3491 | `"            \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L003492](../../agents/web_agent.py#L3492) | 3492 | `"            \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L003493](../../agents/web_agent.py#L3493) | 3493 | `"            \"dialogue_context\": plan.get(\"dialogue_context\", {}),"` | — |
| [SRC-1AE03B9EC3-L003494](../../agents/web_agent.py#L3494) | 3494 | `"            \"provider_diagnostics\": provider_diagnostics,"` | — |
| [SRC-1AE03B9EC3-L003495](../../agents/web_agent.py#L3495) | 3495 | `"            \"connector_summary\": self._connector_status_summary("` | — |
| [SRC-1AE03B9EC3-L003496](../../agents/web_agent.py#L3496) | 3496 | `"                provider_diagnostics, sources"` | — |
| [SRC-1AE03B9EC3-L003497](../../agents/web_agent.py#L3497) | 3497 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L003498](../../agents/web_agent.py#L3498) | 3498 | `"            \"pages_fetch_attempted\": len(fetch_targets),"` | — |
| [SRC-1AE03B9EC3-L003499](../../agents/web_agent.py#L3499) | 3499 | `"        }"` | — |
| [SRC-1AE03B9EC3-L003500](../../agents/web_agent.py#L3500) | 3500 | `"        coverage_targets = plan.get(\"coverage_targets\") or []"` | — |
| [SRC-1AE03B9EC3-L003501](../../agents/web_agent.py#L3501) | 3501 | `"        if isinstance(coverage_targets, list) and coverage_targets:"` | — |
| [SRC-1AE03B9EC3-L003502](../../agents/web_agent.py#L3502) | 3502 | `"            safe_targets = ["` | — |
| [SRC-1AE03B9EC3-L003503](../../agents/web_agent.py#L3503) | 3503 | `"                target[:120]"` | — |
| [SRC-1AE03B9EC3-L003504](../../agents/web_agent.py#L3504) | 3504 | `"                for target in coverage_targets"` | — |
| [SRC-1AE03B9EC3-L003505](../../agents/web_agent.py#L3505) | 3505 | `"                if isinstance(target, str) and target.strip()"` | — |
| [SRC-1AE03B9EC3-L003506](../../agents/web_agent.py#L3506) | 3506 | `"            ][:8]"` | — |
| [SRC-1AE03B9EC3-L003507](../../agents/web_agent.py#L3507) | 3507 | `"            ledger = build_evidence_ledger(safe_targets, sources)"` | — |
| [SRC-1AE03B9EC3-L003508](../../agents/web_agent.py#L3508) | 3508 | `"            report[\"aspects\"] = safe_targets"` | — |
| [SRC-1AE03B9EC3-L003509](../../agents/web_agent.py#L3509) | 3509 | `"            report[\"evidence_ledger\"] = ledger"` | — |
| [SRC-1AE03B9EC3-L003510](../../agents/web_agent.py#L3510) | 3510 | `"            report[\"aspect_diagnostics_ar\"] = arabic_aspect_diagnostics(ledger)"` | — |
| [SRC-1AE03B9EC3-L003511](../../agents/web_agent.py#L3511) | 3511 | `"            report[\"aspect_evidence_gaps\"] = list(ledger.get(\"missing\") or [])"` | — |
| [SRC-1AE03B9EC3-L003512](../../agents/web_agent.py#L3512) | 3512 | `"            report[\"aspect_coverage_lexical_ratio\"] = ledger.get(\"coverage_ratio\")"` | — |
| [SRC-1AE03B9EC3-L003513](../../agents/web_agent.py#L3513) | 3513 | `"            report[\"aspect_coverage_is_not_truth_score\"] = True"` | — |
| [SRC-1AE03B9EC3-L003514](../../agents/web_agent.py#L3514) | 3514 | `""` | — |
| [SRC-1AE03B9EC3-L003515](../../agents/web_agent.py#L3515) | 3515 | `"        return sources, list(dict.fromkeys(warnings)), report"` | — |
| [SRC-1AE03B9EC3-L003516](../../agents/web_agent.py#L3516) | 3516 | `""` | — |
| [SRC-1AE03B9EC3-L003517](../../agents/web_agent.py#L3517) | 3517 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L003518](../../agents/web_agent.py#L3518) | 3518 | `"    def _history_search_query(question: str, history: list[dict[str, str]]) -> str:"` | — |
| [SRC-1AE03B9EC3-L003519](../../agents/web_agent.py#L3519) | 3519 | `"        \"\"\"Backward-compatible wrapper for the shared follow-up resolver.\"\"\""` | — |
| [SRC-1AE03B9EC3-L003520](../../agents/web_agent.py#L3520) | 3520 | `"        return resolve_followup_query(question, history)"` | — |
| [SRC-1AE03B9EC3-L003521](../../agents/web_agent.py#L3521) | 3521 | `""` | — |
| [SRC-1AE03B9EC3-L003522](../../agents/web_agent.py#L3522) | 3522 | `"    def _connector_status_summary(self, diagnostics: list[dict[str, Any]] \| None,"` | — |
| [SRC-1AE03B9EC3-L003523](../../agents/web_agent.py#L3523) | 3523 | `"                                  sources: list[dict[str, Any]] \| None = None) -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L003524](../../agents/web_agent.py#L3524) | 3524 | `"        \"\"\"Summarize this request's connector states without exposing credentials.\"\"\""` | — |
| [SRC-1AE03B9EC3-L003525](../../agents/web_agent.py#L3525) | 3525 | `"        optional = {"` | — |
| [SRC-1AE03B9EC3-L003526](../../agents/web_agent.py#L3526) | 3526 | `"            \"deepseek_search_api\": (\"DEEPSEEK_SEARCH_API_KEY\",), \"brave_search_api\": (\"BRAVE_SEARCH_API_KEY\",),"` | — |
| [SRC-1AE03B9EC3-L003527](../../agents/web_agent.py#L3527) | 3527 | `"            \"tavily_search_api\": (\"TAVILY_API_KEY\",), \"reddit_oauth_api\": (\"REDDIT_CLIENT_ID\", \"REDDIT_CLIENT_SECRET\"),"` | — |
| [SRC-1AE03B9EC3-L003528](../../agents/web_agent.py#L3528) | 3528 | `"            \"facebook_pages_api\": (\"FACEBOOK_PAGE_ACCESS_TOKEN\", \"FACEBOOK_PAGE_IDS\"),"` | — |
| [SRC-1AE03B9EC3-L003529](../../agents/web_agent.py#L3529) | 3529 | `"            \"instagram_graph_api\": (\"INSTAGRAM_USER_ID\", \"INSTAGRAM_ACCESS_TOKEN\"),"` | — |
| [SRC-1AE03B9EC3-L003530](../../agents/web_agent.py#L3530) | 3530 | `"            \"x_official_api\": (\"X_BEARER_TOKEN\",), \"youtube_data_api\": (\"YOUTUBE_API_KEY\",),"` | — |
| [SRC-1AE03B9EC3-L003531](../../agents/web_agent.py#L3531) | 3531 | `"        }"` | — |
| [SRC-1AE03B9EC3-L003532](../../agents/web_agent.py#L3532) | 3532 | `"        config: dict[str, tuple[bool, str]] = {"` | — |
| [SRC-1AE03B9EC3-L003533](../../agents/web_agent.py#L3533) | 3533 | `"            \"duckduckgo_html\": (True, \"built_in_no_api_key\"), \"bing_rss\": (True, \"built_in_no_api_key\"),"` | — |
| [SRC-1AE03B9EC3-L003534](../../agents/web_agent.py#L3534) | 3534 | `"            \"google_news_rss\": (True, \"built_in_conditional_no_api_key\"),"` | — |
| [SRC-1AE03B9EC3-L003535](../../agents/web_agent.py#L3535) | 3535 | `"            \"openalex\": (True, \"built_in_free_academic\"),"` | — |
| [SRC-1AE03B9EC3-L003536](../../agents/web_agent.py#L3536) | 3536 | `"            \"arxiv\": (True, \"built_in_free_academic\"),"` | — |
| [SRC-1AE03B9EC3-L003537](../../agents/web_agent.py#L3537) | 3537 | `"            \"crossref\": (True, \"built_in_free_academic\"),"` | — |
| [SRC-1AE03B9EC3-L003538](../../agents/web_agent.py#L3538) | 3538 | `"            \"reddit_public_rss\": (True, \"built_in_no_api_key\"), \"bluesky_public_search\": (True, \"built_in_no_api_key\"),"` | — |
| [SRC-1AE03B9EC3-L003539](../../agents/web_agent.py#L3539) | 3539 | `"            \"openrouter_web_search\": (bool(self.openrouter_web_search_enabled),"` | — |
| [SRC-1AE03B9EC3-L003540](../../agents/web_agent.py#L3540) | 3540 | `"                \"enabled\" if self.openrouter_web_search_enabled else \"disabled\"),"` | — |
| [SRC-1AE03B9EC3-L003541](../../agents/web_agent.py#L3541) | 3541 | `"            \"user_supplied_url\": (True, \"request_driven\"),"` | — |
| [SRC-1AE03B9EC3-L003542](../../agents/web_agent.py#L3542) | 3542 | `"        }"` | — |
| [SRC-1AE03B9EC3-L003543](../../agents/web_agent.py#L3543) | 3543 | `"        for name, keys in optional.items():"` | — |
| [SRC-1AE03B9EC3-L003544](../../agents/web_agent.py#L3544) | 3544 | `"            ready = all(bool(os.getenv(key, \"\").strip()) for key in keys)"` | — |
| [SRC-1AE03B9EC3-L003545](../../agents/web_agent.py#L3545) | 3545 | `"            config[name] = (ready, \"configured\" if ready else \"not_configured\")"` | — |
| [SRC-1AE03B9EC3-L003546](../../agents/web_agent.py#L3546) | 3546 | `"        grouped: dict[str, list[dict[str, Any]]] = {}"` | — |
| [SRC-1AE03B9EC3-L003547](../../agents/web_agent.py#L3547) | 3547 | `"        for item in diagnostics or []:"` | — |
| [SRC-1AE03B9EC3-L003548](../../agents/web_agent.py#L3548) | 3548 | `"            if isinstance(item, dict):"` | — |
| [SRC-1AE03B9EC3-L003549](../../agents/web_agent.py#L3549) | 3549 | `"                name = _clean_text(item.get(\"provider\", \"unknown\"), 80) or \"unknown\""` | — |
| [SRC-1AE03B9EC3-L003550](../../agents/web_agent.py#L3550) | 3550 | `"                grouped.setdefault(name, []).append(item)"` | — |
| [SRC-1AE03B9EC3-L003551](../../agents/web_agent.py#L3551) | 3551 | `"        useful: dict[str, int] = {}"` | — |
| [SRC-1AE03B9EC3-L003552](../../agents/web_agent.py#L3552) | 3552 | `"        for source in sources or []:"` | — |
| [SRC-1AE03B9EC3-L003553](../../agents/web_agent.py#L3553) | 3553 | `"            if not isinstance(source, dict):"` | — |
| [SRC-1AE03B9EC3-L003554](../../agents/web_agent.py#L3554) | 3554 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L003555](../../agents/web_agent.py#L3555) | 3555 | `"            providers = source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L003556](../../agents/web_agent.py#L3556) | 3556 | `"            if isinstance(providers, str):"` | — |
| [SRC-1AE03B9EC3-L003557](../../agents/web_agent.py#L3557) | 3557 | `"                providers = [providers]"` | — |
| [SRC-1AE03B9EC3-L003558](../../agents/web_agent.py#L3558) | 3558 | `"            if not isinstance(providers, list):"` | — |
| [SRC-1AE03B9EC3-L003559](../../agents/web_agent.py#L3559) | 3559 | `"                providers = []"` | — |
| [SRC-1AE03B9EC3-L003560](../../agents/web_agent.py#L3560) | 3560 | `"            if isinstance(source.get(\"provider\"), str):"` | — |
| [SRC-1AE03B9EC3-L003561](../../agents/web_agent.py#L3561) | 3561 | `"                providers = providers + [source[\"provider\"]]"` | — |
| [SRC-1AE03B9EC3-L003562](../../agents/web_agent.py#L3562) | 3562 | `"            for name in {str(value) for value in providers if value}:"` | — |
| [SRC-1AE03B9EC3-L003563](../../agents/web_agent.py#L3563) | 3563 | `"                useful[name] = useful.get(name, 0) + 1"` | — |
| [SRC-1AE03B9EC3-L003564](../../agents/web_agent.py#L3564) | 3564 | `"        priority = {\"ok\": 0, \"no_results\": 1, \"filtered_all\": 2, \"not_attempted\": 3,"` | — |
| [SRC-1AE03B9EC3-L003565](../../agents/web_agent.py#L3565) | 3565 | `"                    \"disabled\": 4, \"not_configured\": 5, \"budget_exhausted\": 6,"` | — |
| [SRC-1AE03B9EC3-L003566](../../agents/web_agent.py#L3566) | 3566 | `"                    \"unknown\": 6, \"rate_limited\": 7, \"unauthorized\": 8, \"blocked\": 9,"` | — |
| [SRC-1AE03B9EC3-L003567](../../agents/web_agent.py#L3567) | 3567 | `"                    \"http_error\": 9, \"invalid_response\": 10,"` | — |
| [SRC-1AE03B9EC3-L003568](../../agents/web_agent.py#L3568) | 3568 | `"                    \"timeout\": 10, \"failed\": 11, \"error\": 11}"` | — |
| [SRC-1AE03B9EC3-L003569](../../agents/web_agent.py#L3569) | 3569 | `"        confirmed_attempt_statuses = _SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES \| {"` | — |
| [SRC-1AE03B9EC3-L003570](../../agents/web_agent.py#L3570) | 3570 | `"            \"blocked\", \"http_error\", \"unauthorized\", \"rate_limited\", \"invalid_response\""` | — |
| [SRC-1AE03B9EC3-L003571](../../agents/web_agent.py#L3571) | 3571 | `"        }"` | — |
| [SRC-1AE03B9EC3-L003572](../../agents/web_agent.py#L3572) | 3572 | `"        uncertain_attempt_statuses = {\"timeout\", \"failed\", \"error\", \"unknown\", \"inconclusive\"}"` | — |
| [SRC-1AE03B9EC3-L003573](../../agents/web_agent.py#L3573) | 3573 | `""` | — |
| [SRC-1AE03B9EC3-L003574](../../agents/web_agent.py#L3574) | 3574 | `"        def redact(value: Any) -> str:"` | — |
| [SRC-1AE03B9EC3-L003575](../../agents/web_agent.py#L3575) | 3575 | `"            safe = _clean_text(str(value or \"\"), 180)"` | — |
| [SRC-1AE03B9EC3-L003576](../../agents/web_agent.py#L3576) | 3576 | `"            safe = re.sub(r\"(?i)(bearer\\s+)[A-Za-z0-9._~+/-]+=*\", r\"\\1[REDACTED]\", safe)"` | — |
| [SRC-1AE03B9EC3-L003577](../../agents/web_agent.py#L3577) | 3577 | `"            safe = re.sub(r\"(?i)\\b(api[_-]?key\|access[_-]?token\|refresh[_-]?token\|token\|secret\|password)\\s*[:=]\\s*[^\\s,;]+\", r\"\\1=[REDACTED]\", safe)"` | — |
| [SRC-1AE03B9EC3-L003578](../../agents/web_agent.py#L3578) | 3578 | `"            safe = re.sub(r\"(?i)([?&](?:api[_-]?key\|access[_-]?token\|token\|key)=)[^&\\s]+\", r\"\\1[REDACTED]\", safe)"` | — |
| [SRC-1AE03B9EC3-L003579](../../agents/web_agent.py#L3579) | 3579 | `"            return safe[:180]"` | — |
| [SRC-1AE03B9EC3-L003580](../../agents/web_agent.py#L3580) | 3580 | `""` | — |
| [SRC-1AE03B9EC3-L003581](../../agents/web_agent.py#L3581) | 3581 | `"        names = set(config) \| set(grouped) \| set(useful)"` | — |
| [SRC-1AE03B9EC3-L003582](../../agents/web_agent.py#L3582) | 3582 | `"        connectors = []"` | — |
| [SRC-1AE03B9EC3-L003583](../../agents/web_agent.py#L3583) | 3583 | `"        for name in sorted(names):"` | — |
| [SRC-1AE03B9EC3-L003584](../../agents/web_agent.py#L3584) | 3584 | `"            ready, config_status = config.get(name, (bool(grouped.get(name) or useful.get(name)), \"observed_in_code_path\"))"` | — |
| [SRC-1AE03B9EC3-L003585](../../agents/web_agent.py#L3585) | 3585 | `"            attempts = grouped.get(name, [])"` | — |
| [SRC-1AE03B9EC3-L003586](../../agents/web_agent.py#L3586) | 3586 | `"            statuses = [_clean_text(row.get(\"status\", \"unknown\"), 40).lower() or \"unknown\" for row in attempts]"` | — |
| [SRC-1AE03B9EC3-L003587](../../agents/web_agent.py#L3587) | 3587 | `"            status = max(statuses, key=lambda value: priority.get(value, 6)) if statuses else ("` | — |
| [SRC-1AE03B9EC3-L003588](../../agents/web_agent.py#L3588) | 3588 | `"                \"ok\" if useful.get(name, 0) else \"not_configured\" if not ready else \"not_attempted\")"` | — |
| [SRC-1AE03B9EC3-L003589](../../agents/web_agent.py#L3589) | 3589 | `"            if any(value in confirmed_attempt_statuses for value in statuses) or useful.get(name, 0):"` | — |
| [SRC-1AE03B9EC3-L003590](../../agents/web_agent.py#L3590) | 3590 | `"                attempted: bool \| None = True"` | — |
| [SRC-1AE03B9EC3-L003591](../../agents/web_agent.py#L3591) | 3591 | `"            elif any(value in uncertain_attempt_statuses for value in statuses):"` | — |
| [SRC-1AE03B9EC3-L003592](../../agents/web_agent.py#L3592) | 3592 | `"                attempted = None"` | — |
| [SRC-1AE03B9EC3-L003593](../../agents/web_agent.py#L3593) | 3593 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L003594](../../agents/web_agent.py#L3594) | 3594 | `"                attempted = False"` | — |
| [SRC-1AE03B9EC3-L003595](../../agents/web_agent.py#L3595) | 3595 | `"            successful_statuses = set(statuses) & _SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES"` | — |
| [SRC-1AE03B9EC3-L003596](../../agents/web_agent.py#L3596) | 3596 | `"            error_response_statuses = set(statuses) & {"` | — |
| [SRC-1AE03B9EC3-L003597](../../agents/web_agent.py#L3597) | 3597 | `"                \"blocked\", \"http_error\", \"unauthorized\", \"rate_limited\", \"invalid_response\""` | — |
| [SRC-1AE03B9EC3-L003598](../../agents/web_agent.py#L3598) | 3598 | `"            }"` | — |
| [SRC-1AE03B9EC3-L003599](../../agents/web_agent.py#L3599) | 3599 | `"            uncertain_failure_statuses = set(statuses) & {\"timeout\", \"failed\", \"error\", \"unknown\", \"inconclusive\"}"` | — |
| [SRC-1AE03B9EC3-L003600](../../agents/web_agent.py#L3600) | 3600 | `"            failure_observed = bool(error_response_statuses or uncertain_failure_statuses or \"budget_exhausted\" in statuses)"` | — |
| [SRC-1AE03B9EC3-L003601](../../agents/web_agent.py#L3601) | 3601 | `"            available: bool \| None = ("` | — |
| [SRC-1AE03B9EC3-L003602](../../agents/web_agent.py#L3602) | 3602 | `"                True if successful_statuses or useful.get(name, 0)"` | — |
| [SRC-1AE03B9EC3-L003603](../../agents/web_agent.py#L3603) | 3603 | `"                else False if error_response_statuses or not ready or \"disabled\" in statuses or \"budget_exhausted\" in statuses"` | — |
| [SRC-1AE03B9EC3-L003604](../../agents/web_agent.py#L3604) | 3604 | `"                else None"` | — |
| [SRC-1AE03B9EC3-L003605](../../agents/web_agent.py#L3605) | 3605 | `"            )"` | — |
| [SRC-1AE03B9EC3-L003606](../../agents/web_agent.py#L3606) | 3606 | `"            verified: bool \| None = ("` | — |
| [SRC-1AE03B9EC3-L003607](../../agents/web_agent.py#L3607) | 3607 | `"                True if successful_statuses or useful.get(name, 0)"` | — |
| [SRC-1AE03B9EC3-L003608](../../agents/web_agent.py#L3608) | 3608 | `"                else False if error_response_statuses"` | — |
| [SRC-1AE03B9EC3-L003609](../../agents/web_agent.py#L3609) | 3609 | `"                else None"` | — |
| [SRC-1AE03B9EC3-L003610](../../agents/web_agent.py#L3610) | 3610 | `"            )"` | — |
