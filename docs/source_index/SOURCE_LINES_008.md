# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **008**
- سجلات الأسطر: **800**
- النطاق: SRC-1AE03B9EC3-L001739 إلى SRC-1AE03B9EC3-L002538
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-1AE03B9EC3 — [agents/web_agent.py](../../agents/web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1AE03B9EC3-L001739](../../agents/web_agent.py#L1739) | 1739 | `"            if not url or _blocked_source_url(url):"` | — |
| [SRC-1AE03B9EC3-L001740](../../agents/web_agent.py#L1740) | 1740 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001741](../../agents/web_agent.py#L1741) | 1741 | `"            # Keep every parseable, safe candidate here. _search_web applies the"` | — |
| [SRC-1AE03B9EC3-L001742](../../agents/web_agent.py#L1742) | 1742 | `"            # shared relevance filter and records accepted/rejected counters."` | — |
| [SRC-1AE03B9EC3-L001743](../../agents/web_agent.py#L1743) | 1743 | `"            # Filtering again in this adapter mislabels a valid feed as no results."` | — |
| [SRC-1AE03B9EC3-L001744](../../agents/web_agent.py#L1744) | 1744 | `"            source_node = next("` | — |
| [SRC-1AE03B9EC3-L001745](../../agents/web_agent.py#L1745) | 1745 | `"                (child for child in item if child.tag.rsplit(\"}\", 1)[-1] == \"source\"),"` | — |
| [SRC-1AE03B9EC3-L001746](../../agents/web_agent.py#L1746) | 1746 | `"                None,"` | — |
| [SRC-1AE03B9EC3-L001747](../../agents/web_agent.py#L1747) | 1747 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001748](../../agents/web_agent.py#L1748) | 1748 | `"            publisher_url = _public_http_url("` | — |
| [SRC-1AE03B9EC3-L001749](../../agents/web_agent.py#L1749) | 1749 | `"                source_node.attrib.get(\"url\", \"\") if source_node is not None else \"\""` | — |
| [SRC-1AE03B9EC3-L001750](../../agents/web_agent.py#L1750) | 1750 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001751](../../agents/web_agent.py#L1751) | 1751 | `"            publisher_name = _clean_text("` | — |
| [SRC-1AE03B9EC3-L001752](../../agents/web_agent.py#L1752) | 1752 | `"                source_node.text if source_node is not None else \"\", 200"` | — |
| [SRC-1AE03B9EC3-L001753](../../agents/web_agent.py#L1753) | 1753 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001754](../../agents/web_agent.py#L1754) | 1754 | `"            publisher_domain = ("` | — |
| [SRC-1AE03B9EC3-L001755](../../agents/web_agent.py#L1755) | 1755 | `"                (urllib.parse.urlparse(publisher_url).hostname or \"\").lower()"` | — |
| [SRC-1AE03B9EC3-L001756](../../agents/web_agent.py#L1756) | 1756 | `"                if publisher_url else \"\""` | — |
| [SRC-1AE03B9EC3-L001757](../../agents/web_agent.py#L1757) | 1757 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001758](../../agents/web_agent.py#L1758) | 1758 | `"            results.append({"` | — |
| [SRC-1AE03B9EC3-L001759](../../agents/web_agent.py#L1759) | 1759 | `"                \"title\": _clean_text(fields.get(\"title\", \"\"), 300),"` | — |
| [SRC-1AE03B9EC3-L001760](../../agents/web_agent.py#L1760) | 1760 | `"                \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L001761](../../agents/web_agent.py#L1761) | 1761 | `"                \"snippet\": _clean_text(fields.get(\"description\", \"\"), 1200),"` | — |
| [SRC-1AE03B9EC3-L001762](../../agents/web_agent.py#L1762) | 1762 | `"                \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L001763](../../agents/web_agent.py#L1763) | 1763 | `"                \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L001764](../../agents/web_agent.py#L1764) | 1764 | `"                \"provider\": \"google_news_rss\","` | — |
| [SRC-1AE03B9EC3-L001765](../../agents/web_agent.py#L1765) | 1765 | `"                \"provider_rank\": len(results) + 1,"` | — |
| [SRC-1AE03B9EC3-L001766](../../agents/web_agent.py#L1766) | 1766 | `"                \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L001767](../../agents/web_agent.py#L1767) | 1767 | `"                \"published_at\": _clean_text(fields.get(\"pubDate\", \"\"), 100),"` | — |
| [SRC-1AE03B9EC3-L001768](../../agents/web_agent.py#L1768) | 1768 | `"                \"publisher_name\": publisher_name,"` | — |
| [SRC-1AE03B9EC3-L001769](../../agents/web_agent.py#L1769) | 1769 | `"                \"publisher_url\": publisher_url or \"\","` | — |
| [SRC-1AE03B9EC3-L001770](../../agents/web_agent.py#L1770) | 1770 | `"                \"publisher_domain\": publisher_domain,"` | — |
| [SRC-1AE03B9EC3-L001771](../../agents/web_agent.py#L1771) | 1771 | `"            })"` | — |
| [SRC-1AE03B9EC3-L001772](../../agents/web_agent.py#L1772) | 1772 | `"            if len(results) >= MAX_PROVIDER_RESULTS:"` | — |
| [SRC-1AE03B9EC3-L001773](../../agents/web_agent.py#L1773) | 1773 | `"                break"` | — |
| [SRC-1AE03B9EC3-L001774](../../agents/web_agent.py#L1774) | 1774 | `"        return results"` | — |
| [SRC-1AE03B9EC3-L001775](../../agents/web_agent.py#L1775) | 1775 | `""` | — |
| [SRC-1AE03B9EC3-L001776](../../agents/web_agent.py#L1776) | 1776 | `"    def _search_social("` | — |
| [SRC-1AE03B9EC3-L001777](../../agents/web_agent.py#L1777) | 1777 | `"        self, query: str, platforms: list[str]"` | — |
| [SRC-1AE03B9EC3-L001778](../../agents/web_agent.py#L1778) | 1778 | `"    ) -> tuple[list[dict[str, Any]], list[str]]:"` | — |
| [SRC-1AE03B9EC3-L001779](../../agents/web_agent.py#L1779) | 1779 | `"        \"\"\"Search public social content through exposed public endpoints only.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001780](../../agents/web_agent.py#L1780) | 1780 | `"        query = compact_search_query(query)"` | — |
| [SRC-1AE03B9EC3-L001781](../../agents/web_agent.py#L1781) | 1781 | `"        if not query:"` | — |
| [SRC-1AE03B9EC3-L001782](../../agents/web_agent.py#L1782) | 1782 | `"            return [], [\"لم يبدأ البحث الاجتماعي لعدم وجود كلمات موضوعية قابلة للبحث.\"]"` | — |
| [SRC-1AE03B9EC3-L001783](../../agents/web_agent.py#L1783) | 1783 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L001784](../../agents/web_agent.py#L1784) | 1784 | `"            import xml.etree.ElementTree as ET"` | — |
| [SRC-1AE03B9EC3-L001785](../../agents/web_agent.py#L1785) | 1785 | `""` | — |
| [SRC-1AE03B9EC3-L001786](../../agents/web_agent.py#L1786) | 1786 | `"            import httpx"` | — |
| [SRC-1AE03B9EC3-L001787](../../agents/web_agent.py#L1787) | 1787 | `"            from bs4 import BeautifulSoup"` | — |
| [SRC-1AE03B9EC3-L001788](../../agents/web_agent.py#L1788) | 1788 | `"        except ImportError as exc:"` | — |
| [SRC-1AE03B9EC3-L001789](../../agents/web_agent.py#L1789) | 1789 | `"            raise AgentDependencyError("` | — |
| [SRC-1AE03B9EC3-L001790](../../agents/web_agent.py#L1790) | 1790 | `"                \"حزم البحث الاجتماعي غير مثبتة. نفّذ: python -m pip install -e .\""` | — |
| [SRC-1AE03B9EC3-L001791](../../agents/web_agent.py#L1791) | 1791 | `"            ) from exc"` | — |
| [SRC-1AE03B9EC3-L001792](../../agents/web_agent.py#L1792) | 1792 | `""` | — |
| [SRC-1AE03B9EC3-L001793](../../agents/web_agent.py#L1793) | 1793 | `"        results: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L001794](../../agents/web_agent.py#L1794) | 1794 | `"        warnings: list[str] = []"` | — |
| [SRC-1AE03B9EC3-L001795](../../agents/web_agent.py#L1795) | 1795 | `"        headers = {"` | — |
| [SRC-1AE03B9EC3-L001796](../../agents/web_agent.py#L1796) | 1796 | `"            \"User-Agent\": \"OmaraiResearchBot/1.0 (public-content search; no login)\","` | — |
| [SRC-1AE03B9EC3-L001797](../../agents/web_agent.py#L1797) | 1797 | `"            \"Accept-Language\": \"ar,en;q=0.9\","` | — |
| [SRC-1AE03B9EC3-L001798](../../agents/web_agent.py#L1798) | 1798 | `"        }"` | — |
| [SRC-1AE03B9EC3-L001799](../../agents/web_agent.py#L1799) | 1799 | `""` | — |
| [SRC-1AE03B9EC3-L001800](../../agents/web_agent.py#L1800) | 1800 | `"        reddit_client_id = os.getenv(\"REDDIT_CLIENT_ID\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L001801](../../agents/web_agent.py#L1801) | 1801 | `"        reddit_client_secret = os.getenv(\"REDDIT_CLIENT_SECRET\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L001802](../../agents/web_agent.py#L1802) | 1802 | `"        reddit_user_agent = os.getenv("` | — |
| [SRC-1AE03B9EC3-L001803](../../agents/web_agent.py#L1803) | 1803 | `"            \"REDDIT_USER_AGENT\","` | — |
| [SRC-1AE03B9EC3-L001804](../../agents/web_agent.py#L1804) | 1804 | `"            \"web:omarai-research-agent:v0.3 (public-content research)\","` | — |
| [SRC-1AE03B9EC3-L001805](../../agents/web_agent.py#L1805) | 1805 | `"        ).strip()"` | — |
| [SRC-1AE03B9EC3-L001806](../../agents/web_agent.py#L1806) | 1806 | `"        if \"reddit\" in platforms and reddit_client_id and reddit_client_secret:"` | — |
| [SRC-1AE03B9EC3-L001807](../../agents/web_agent.py#L1807) | 1807 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L001808](../../agents/web_agent.py#L1808) | 1808 | `"                self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L001809](../../agents/web_agent.py#L1809) | 1809 | `"                token_response = httpx.post("` | — |
| [SRC-1AE03B9EC3-L001810](../../agents/web_agent.py#L1810) | 1810 | `"                    \"https://www.reddit.com/api/v1/access_token\","` | — |
| [SRC-1AE03B9EC3-L001811](../../agents/web_agent.py#L1811) | 1811 | `"                    data={\"grant_type\": \"client_credentials\"},"` | — |
| [SRC-1AE03B9EC3-L001812](../../agents/web_agent.py#L1812) | 1812 | `"                    auth=(reddit_client_id, reddit_client_secret),"` | — |
| [SRC-1AE03B9EC3-L001813](../../agents/web_agent.py#L1813) | 1813 | `"                    headers={\"User-Agent\": reddit_user_agent},"` | — |
| [SRC-1AE03B9EC3-L001814](../../agents/web_agent.py#L1814) | 1814 | `"                    timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L001815](../../agents/web_agent.py#L1815) | 1815 | `"                    follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001816](../../agents/web_agent.py#L1816) | 1816 | `"                )"` | — |
| [SRC-1AE03B9EC3-L001817](../../agents/web_agent.py#L1817) | 1817 | `"                if token_response.status_code == 200:"` | — |
| [SRC-1AE03B9EC3-L001818](../../agents/web_agent.py#L1818) | 1818 | `"                    access_token = token_response.json().get(\"access_token\", \"\")"` | — |
| [SRC-1AE03B9EC3-L001819](../../agents/web_agent.py#L1819) | 1819 | `"                    if access_token:"` | — |
| [SRC-1AE03B9EC3-L001820](../../agents/web_agent.py#L1820) | 1820 | `"                        self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L001821](../../agents/web_agent.py#L1821) | 1821 | `"                        search_response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L001822](../../agents/web_agent.py#L1822) | 1822 | `"                            \"https://oauth.reddit.com/search\","` | — |
| [SRC-1AE03B9EC3-L001823](../../agents/web_agent.py#L1823) | 1823 | `"                            params={"` | — |
| [SRC-1AE03B9EC3-L001824](../../agents/web_agent.py#L1824) | 1824 | `"                                \"q\": query,"` | — |
| [SRC-1AE03B9EC3-L001825](../../agents/web_agent.py#L1825) | 1825 | `"                                \"sort\": \"relevance\","` | — |
| [SRC-1AE03B9EC3-L001826](../../agents/web_agent.py#L1826) | 1826 | `"                                \"t\": \"all\","` | — |
| [SRC-1AE03B9EC3-L001827](../../agents/web_agent.py#L1827) | 1827 | `"                                \"limit\": 10,"` | — |
| [SRC-1AE03B9EC3-L001828](../../agents/web_agent.py#L1828) | 1828 | `"                                \"type\": \"link\","` | — |
| [SRC-1AE03B9EC3-L001829](../../agents/web_agent.py#L1829) | 1829 | `"                            },"` | — |
| [SRC-1AE03B9EC3-L001830](../../agents/web_agent.py#L1830) | 1830 | `"                            headers={"` | — |
| [SRC-1AE03B9EC3-L001831](../../agents/web_agent.py#L1831) | 1831 | `"                                **headers,"` | — |
| [SRC-1AE03B9EC3-L001832](../../agents/web_agent.py#L1832) | 1832 | `"                                \"User-Agent\": reddit_user_agent,"` | — |
| [SRC-1AE03B9EC3-L001833](../../agents/web_agent.py#L1833) | 1833 | `"                                \"Authorization\": \"Bearer \" + access_token,"` | — |
| [SRC-1AE03B9EC3-L001834](../../agents/web_agent.py#L1834) | 1834 | `"                            },"` | — |
| [SRC-1AE03B9EC3-L001835](../../agents/web_agent.py#L1835) | 1835 | `"                            timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L001836](../../agents/web_agent.py#L1836) | 1836 | `"                            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001837](../../agents/web_agent.py#L1837) | 1837 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L001838](../../agents/web_agent.py#L1838) | 1838 | `"                        if search_response.status_code == 200:"` | — |
| [SRC-1AE03B9EC3-L001839](../../agents/web_agent.py#L1839) | 1839 | `"                            children = search_response.json().get(\"data\", {}).get(\"children\", [])"` | — |
| [SRC-1AE03B9EC3-L001840](../../agents/web_agent.py#L1840) | 1840 | `"                            rank = 0"` | — |
| [SRC-1AE03B9EC3-L001841](../../agents/web_agent.py#L1841) | 1841 | `"                            for child in children:"` | — |
| [SRC-1AE03B9EC3-L001842](../../agents/web_agent.py#L1842) | 1842 | `"                                post = child.get(\"data\", {}) if isinstance(child, dict) else {}"` | — |
| [SRC-1AE03B9EC3-L001843](../../agents/web_agent.py#L1843) | 1843 | `"                                permalink = str(post.get(\"permalink\") or \"\")"` | — |
| [SRC-1AE03B9EC3-L001844](../../agents/web_agent.py#L1844) | 1844 | `"                                url = _public_http_url("` | — |
| [SRC-1AE03B9EC3-L001845](../../agents/web_agent.py#L1845) | 1845 | `"                                    permalink if permalink.startswith(\"http\")"` | — |
| [SRC-1AE03B9EC3-L001846](../../agents/web_agent.py#L1846) | 1846 | `"                                    else \"https://www.reddit.com\" + permalink"` | — |
| [SRC-1AE03B9EC3-L001847](../../agents/web_agent.py#L1847) | 1847 | `"                                )"` | — |
| [SRC-1AE03B9EC3-L001848](../../agents/web_agent.py#L1848) | 1848 | `"                                if not url:"` | — |
| [SRC-1AE03B9EC3-L001849](../../agents/web_agent.py#L1849) | 1849 | `"                                    continue"` | — |
| [SRC-1AE03B9EC3-L001850](../../agents/web_agent.py#L1850) | 1850 | `"                                rank += 1"` | — |
| [SRC-1AE03B9EC3-L001851](../../agents/web_agent.py#L1851) | 1851 | `"                                snippet = _clean_text(post.get(\"selftext\") or \"\", 1000)"` | — |
| [SRC-1AE03B9EC3-L001852](../../agents/web_agent.py#L1852) | 1852 | `"                                metrics = []"` | — |
| [SRC-1AE03B9EC3-L001853](../../agents/web_agent.py#L1853) | 1853 | `"                                if post.get(\"score\") is not None:"` | — |
| [SRC-1AE03B9EC3-L001854](../../agents/web_agent.py#L1854) | 1854 | `"                                    metrics.append(\"score=\" + str(post[\"score\"]))"` | — |
| [SRC-1AE03B9EC3-L001855](../../agents/web_agent.py#L1855) | 1855 | `"                                if post.get(\"num_comments\") is not None:"` | — |
| [SRC-1AE03B9EC3-L001856](../../agents/web_agent.py#L1856) | 1856 | `"                                    metrics.append(\"comments=\" + str(post[\"num_comments\"]))"` | — |
| [SRC-1AE03B9EC3-L001857](../../agents/web_agent.py#L1857) | 1857 | `"                                if metrics:"` | — |
| [SRC-1AE03B9EC3-L001858](../../agents/web_agent.py#L1858) | 1858 | `"                                    snippet = (snippet + \" \| \" if snippet else \"\") + \", \".join(metrics)"` | — |
| [SRC-1AE03B9EC3-L001859](../../agents/web_agent.py#L1859) | 1859 | `"                                results.append({"` | — |
| [SRC-1AE03B9EC3-L001860](../../agents/web_agent.py#L1860) | 1860 | `"                                    \"title\": _clean_text(post.get(\"title\") or \"Reddit post\", 300),"` | — |
| [SRC-1AE03B9EC3-L001861](../../agents/web_agent.py#L1861) | 1861 | `"                                    \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L001862](../../agents/web_agent.py#L1862) | 1862 | `"                                    \"snippet\": snippet,"` | — |
| [SRC-1AE03B9EC3-L001863](../../agents/web_agent.py#L1863) | 1863 | `"                                    \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L001864](../../agents/web_agent.py#L1864) | 1864 | `"                                    \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L001865](../../agents/web_agent.py#L1865) | 1865 | `"                                    \"provider\": \"reddit_oauth_api\","` | — |
| [SRC-1AE03B9EC3-L001866](../../agents/web_agent.py#L1866) | 1866 | `"                                    \"provider_rank\": rank,"` | — |
| [SRC-1AE03B9EC3-L001867](../../agents/web_agent.py#L1867) | 1867 | `"                                    \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L001868](../../agents/web_agent.py#L1868) | 1868 | `"                                    \"published_at\": _clean_text(str(post.get(\"created_utc\") or \"\"), 100),"` | — |
| [SRC-1AE03B9EC3-L001869](../../agents/web_agent.py#L1869) | 1869 | `"                                })"` | — |
| [SRC-1AE03B9EC3-L001870](../../agents/web_agent.py#L1870) | 1870 | `"                        else:"` | — |
| [SRC-1AE03B9EC3-L001871](../../agents/web_agent.py#L1871) | 1871 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L001872](../../agents/web_agent.py#L1872) | 1872 | `"                                f\"Reddit OAuth search unavailable (HTTP {search_response.status_code}).\""` | — |
| [SRC-1AE03B9EC3-L001873](../../agents/web_agent.py#L1873) | 1873 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L001874](../../agents/web_agent.py#L1874) | 1874 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L001875](../../agents/web_agent.py#L1875) | 1875 | `"                        warnings.append(\"Reddit OAuth did not return an access token.\")"` | — |
| [SRC-1AE03B9EC3-L001876](../../agents/web_agent.py#L1876) | 1876 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L001877](../../agents/web_agent.py#L1877) | 1877 | `"                    warnings.append("` | — |
| [SRC-1AE03B9EC3-L001878](../../agents/web_agent.py#L1878) | 1878 | `"                        f\"Reddit OAuth authentication unavailable (HTTP {token_response.status_code}).\""` | — |
| [SRC-1AE03B9EC3-L001879](../../agents/web_agent.py#L1879) | 1879 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L001880](../../agents/web_agent.py#L1880) | 1880 | `"            except (httpx.HTTPError, OSError, ValueError, KeyError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L001881](../../agents/web_agent.py#L1881) | 1881 | `"                warnings.append(\"Reddit OAuth search failed for this request.\")"` | — |
| [SRC-1AE03B9EC3-L001882](../../agents/web_agent.py#L1882) | 1882 | `""` | — |
| [SRC-1AE03B9EC3-L001883](../../agents/web_agent.py#L1883) | 1883 | `"        if \"reddit\" in platforms and not any("` | — |
| [SRC-1AE03B9EC3-L001884](../../agents/web_agent.py#L1884) | 1884 | `"            row.get(\"provider\") == \"reddit_oauth_api\" for row in results"` | — |
| [SRC-1AE03B9EC3-L001885](../../agents/web_agent.py#L1885) | 1885 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L001886](../../agents/web_agent.py#L1886) | 1886 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L001887](../../agents/web_agent.py#L1887) | 1887 | `"                self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L001888](../../agents/web_agent.py#L1888) | 1888 | `"                response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L001889](../../agents/web_agent.py#L1889) | 1889 | `"                    \"https://www.reddit.com/search.rss\","` | — |
| [SRC-1AE03B9EC3-L001890](../../agents/web_agent.py#L1890) | 1890 | `"                    params={\"q\": query, \"sort\": \"relevance\", \"t\": \"all\", \"limit\": \"8\"},"` | — |
| [SRC-1AE03B9EC3-L001891](../../agents/web_agent.py#L1891) | 1891 | `"                    headers=headers,"` | — |
| [SRC-1AE03B9EC3-L001892](../../agents/web_agent.py#L1892) | 1892 | `"                    timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L001893](../../agents/web_agent.py#L1893) | 1893 | `"                    follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001894](../../agents/web_agent.py#L1894) | 1894 | `"                )"` | — |
| [SRC-1AE03B9EC3-L001895](../../agents/web_agent.py#L1895) | 1895 | `"                if response.status_code == 200:"` | — |
| [SRC-1AE03B9EC3-L001896](../../agents/web_agent.py#L1896) | 1896 | `"                    root = ET.fromstring(response.content)"` | — |
| [SRC-1AE03B9EC3-L001897](../../agents/web_agent.py#L1897) | 1897 | `"                    for item in root.iter():"` | — |
| [SRC-1AE03B9EC3-L001898](../../agents/web_agent.py#L1898) | 1898 | `"                        if item.tag.rsplit(\"}\", 1)[-1] != \"item\":"` | — |
| [SRC-1AE03B9EC3-L001899](../../agents/web_agent.py#L1899) | 1899 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L001900](../../agents/web_agent.py#L1900) | 1900 | `"                        fields = {"` | — |
| [SRC-1AE03B9EC3-L001901](../../agents/web_agent.py#L1901) | 1901 | `"                            child.tag.rsplit(\"}\", 1)[-1]: (child.text or \"\")"` | — |
| [SRC-1AE03B9EC3-L001902](../../agents/web_agent.py#L1902) | 1902 | `"                            for child in item"` | — |
| [SRC-1AE03B9EC3-L001903](../../agents/web_agent.py#L1903) | 1903 | `"                        }"` | — |
| [SRC-1AE03B9EC3-L001904](../../agents/web_agent.py#L1904) | 1904 | `"                        url = _public_http_url(fields.get(\"link\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L001905](../../agents/web_agent.py#L1905) | 1905 | `"                        if not url or \"reddit.com/\" not in url:"` | — |
| [SRC-1AE03B9EC3-L001906](../../agents/web_agent.py#L1906) | 1906 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L001907](../../agents/web_agent.py#L1907) | 1907 | `"                        description = BeautifulSoup("` | — |
| [SRC-1AE03B9EC3-L001908](../../agents/web_agent.py#L1908) | 1908 | `"                            fields.get(\"description\", \"\"), \"html.parser\""` | — |
| [SRC-1AE03B9EC3-L001909](../../agents/web_agent.py#L1909) | 1909 | `"                        ).get_text(\" \", strip=True)"` | — |
| [SRC-1AE03B9EC3-L001910](../../agents/web_agent.py#L1910) | 1910 | `"                        results.append({"` | — |
| [SRC-1AE03B9EC3-L001911](../../agents/web_agent.py#L1911) | 1911 | `"                            \"title\": _clean_text(fields.get(\"title\", \"\"), 300),"` | — |
| [SRC-1AE03B9EC3-L001912](../../agents/web_agent.py#L1912) | 1912 | `"                            \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L001913](../../agents/web_agent.py#L1913) | 1913 | `"                            \"snippet\": _clean_text(description, 1200),"` | — |
| [SRC-1AE03B9EC3-L001914](../../agents/web_agent.py#L1914) | 1914 | `"                            \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L001915](../../agents/web_agent.py#L1915) | 1915 | `"                            \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L001916](../../agents/web_agent.py#L1916) | 1916 | `"                            \"provider\": \"reddit_public_rss\","` | — |
| [SRC-1AE03B9EC3-L001917](../../agents/web_agent.py#L1917) | 1917 | `"                            \"provider_rank\": len(["` | — |
| [SRC-1AE03B9EC3-L001918](../../agents/web_agent.py#L1918) | 1918 | `"                                row for row in results"` | — |
| [SRC-1AE03B9EC3-L001919](../../agents/web_agent.py#L1919) | 1919 | `"                                if row.get(\"provider\") == \"reddit_public_rss\""` | — |
| [SRC-1AE03B9EC3-L001920](../../agents/web_agent.py#L1920) | 1920 | `"                            ]) + 1,"` | — |
| [SRC-1AE03B9EC3-L001921](../../agents/web_agent.py#L1921) | 1921 | `"                            \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L001922](../../agents/web_agent.py#L1922) | 1922 | `"                            \"published_at\": _clean_text(fields.get(\"pubDate\", \"\"), 100),"` | — |
| [SRC-1AE03B9EC3-L001923](../../agents/web_agent.py#L1923) | 1923 | `"                        })"` | — |
| [SRC-1AE03B9EC3-L001924](../../agents/web_agent.py#L1924) | 1924 | `"                        if sum(row.get(\"provider\") == \"reddit_public_rss\" for row in results) >= 8:"` | — |
| [SRC-1AE03B9EC3-L001925](../../agents/web_agent.py#L1925) | 1925 | `"                            break"` | — |
| [SRC-1AE03B9EC3-L001926](../../agents/web_agent.py#L1926) | 1926 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L001927](../../agents/web_agent.py#L1927) | 1927 | `"                    warnings.append(f\"Reddit public RSS unavailable (HTTP {response.status_code})\")"` | — |
| [SRC-1AE03B9EC3-L001928](../../agents/web_agent.py#L1928) | 1928 | `"            except (httpx.HTTPError, OSError, ValueError, ET.ParseError):"` | — |
| [SRC-1AE03B9EC3-L001929](../../agents/web_agent.py#L1929) | 1929 | `"                warnings.append(\"Reddit public RSS unavailable for this request\")"` | — |
| [SRC-1AE03B9EC3-L001930](../../agents/web_agent.py#L1930) | 1930 | `""` | — |
| [SRC-1AE03B9EC3-L001931](../../agents/web_agent.py#L1931) | 1931 | `"        if \"bluesky\" in platforms:"` | — |
| [SRC-1AE03B9EC3-L001932](../../agents/web_agent.py#L1932) | 1932 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L001933](../../agents/web_agent.py#L1933) | 1933 | `"                self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L001934](../../agents/web_agent.py#L1934) | 1934 | `"                response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L001935](../../agents/web_agent.py#L1935) | 1935 | `"                    \"https://public.api.bsky.app/xrpc/app.bsky.feed.searchPosts\","` | — |
| [SRC-1AE03B9EC3-L001936](../../agents/web_agent.py#L1936) | 1936 | `"                    params={\"q\": query, \"limit\": 10},"` | — |
| [SRC-1AE03B9EC3-L001937](../../agents/web_agent.py#L1937) | 1937 | `"                    headers=headers,"` | — |
| [SRC-1AE03B9EC3-L001938](../../agents/web_agent.py#L1938) | 1938 | `"                    timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L001939](../../agents/web_agent.py#L1939) | 1939 | `"                    follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001940](../../agents/web_agent.py#L1940) | 1940 | `"                )"` | — |
| [SRC-1AE03B9EC3-L001941](../../agents/web_agent.py#L1941) | 1941 | `"                if response.status_code == 200:"` | — |
| [SRC-1AE03B9EC3-L001942](../../agents/web_agent.py#L1942) | 1942 | `"                    data = response.json()"` | — |
| [SRC-1AE03B9EC3-L001943](../../agents/web_agent.py#L1943) | 1943 | `"                    for item in data.get(\"posts\", []):"` | — |
| [SRC-1AE03B9EC3-L001944](../../agents/web_agent.py#L1944) | 1944 | `"                        post = item.get(\"post\", {})"` | — |
| [SRC-1AE03B9EC3-L001945](../../agents/web_agent.py#L1945) | 1945 | `"                        record = post.get(\"record\", {})"` | — |
| [SRC-1AE03B9EC3-L001946](../../agents/web_agent.py#L1946) | 1946 | `"                        author = post.get(\"author\", {})"` | — |
| [SRC-1AE03B9EC3-L001947](../../agents/web_agent.py#L1947) | 1947 | `"                        uri = post.get(\"uri\", \"\")"` | — |
| [SRC-1AE03B9EC3-L001948](../../agents/web_agent.py#L1948) | 1948 | `"                        rkey = uri.rsplit(\"/\", 1)[-1]"` | — |
| [SRC-1AE03B9EC3-L001949](../../agents/web_agent.py#L1949) | 1949 | `"                        handle = author.get(\"handle\", \"\")"` | — |
| [SRC-1AE03B9EC3-L001950](../../agents/web_agent.py#L1950) | 1950 | `"                        if not handle or not rkey:"` | — |
| [SRC-1AE03B9EC3-L001951](../../agents/web_agent.py#L1951) | 1951 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L001952](../../agents/web_agent.py#L1952) | 1952 | `"                        url = f\"https://bsky.app/profile/{handle}/post/{rkey}\""` | — |
| [SRC-1AE03B9EC3-L001953](../../agents/web_agent.py#L1953) | 1953 | `"                        results.append({"` | — |
| [SRC-1AE03B9EC3-L001954](../../agents/web_agent.py#L1954) | 1954 | `"                            \"title\": _clean_text(author.get(\"displayName\") or handle, 300),"` | — |
| [SRC-1AE03B9EC3-L001955](../../agents/web_agent.py#L1955) | 1955 | `"                            \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L001956](../../agents/web_agent.py#L1956) | 1956 | `"                            \"snippet\": _clean_text(record.get(\"text\") or \"\", 1200),"` | — |
| [SRC-1AE03B9EC3-L001957](../../agents/web_agent.py#L1957) | 1957 | `"                            \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L001958](../../agents/web_agent.py#L1958) | 1958 | `"                            \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L001959](../../agents/web_agent.py#L1959) | 1959 | `"                            \"provider\": \"bluesky_public_search\","` | — |
| [SRC-1AE03B9EC3-L001960](../../agents/web_agent.py#L1960) | 1960 | `"                            \"provider_rank\": len(["` | — |
| [SRC-1AE03B9EC3-L001961](../../agents/web_agent.py#L1961) | 1961 | `"                                row for row in results"` | — |
| [SRC-1AE03B9EC3-L001962](../../agents/web_agent.py#L1962) | 1962 | `"                                if row.get(\"provider\") == \"bluesky_public_search\""` | — |
| [SRC-1AE03B9EC3-L001963](../../agents/web_agent.py#L1963) | 1963 | `"                            ]) + 1,"` | — |
| [SRC-1AE03B9EC3-L001964](../../agents/web_agent.py#L1964) | 1964 | `"                            \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L001965](../../agents/web_agent.py#L1965) | 1965 | `"                            \"published_at\": _clean_text(post.get(\"indexedAt\") or \"\", 100),"` | — |
| [SRC-1AE03B9EC3-L001966](../../agents/web_agent.py#L1966) | 1966 | `"                        })"` | — |
| [SRC-1AE03B9EC3-L001967](../../agents/web_agent.py#L1967) | 1967 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L001968](../../agents/web_agent.py#L1968) | 1968 | `"                    warnings.append(f\"Bluesky public search unavailable (HTTP {response.status_code})\")"` | — |
| [SRC-1AE03B9EC3-L001969](../../agents/web_agent.py#L1969) | 1969 | `"            except (httpx.HTTPError, OSError, ValueError, KeyError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L001970](../../agents/web_agent.py#L1970) | 1970 | `"                warnings.append(\"Bluesky public search unavailable for this request\")"` | — |
| [SRC-1AE03B9EC3-L001971](../../agents/web_agent.py#L1971) | 1971 | `""` | — |
| [SRC-1AE03B9EC3-L001972](../../agents/web_agent.py#L1972) | 1972 | `"        if \"facebook\" in platforms:"` | — |
| [SRC-1AE03B9EC3-L001973](../../agents/web_agent.py#L1973) | 1973 | `"            fb_token = os.getenv(\"FACEBOOK_PAGE_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L001974](../../agents/web_agent.py#L1974) | 1974 | `"            page_ids = ["` | — |
| [SRC-1AE03B9EC3-L001975](../../agents/web_agent.py#L1975) | 1975 | `"                value.strip()"` | — |
| [SRC-1AE03B9EC3-L001976](../../agents/web_agent.py#L1976) | 1976 | `"                for value in os.getenv(\"FACEBOOK_PAGE_IDS\", \"\").split(\",\")"` | — |
| [SRC-1AE03B9EC3-L001977](../../agents/web_agent.py#L1977) | 1977 | `"                if value.strip()"` | — |
| [SRC-1AE03B9EC3-L001978](../../agents/web_agent.py#L1978) | 1978 | `"            ][:5]"` | — |
| [SRC-1AE03B9EC3-L001979](../../agents/web_agent.py#L1979) | 1979 | `"            graph_version = os.getenv(\"META_GRAPH_VERSION\", \"v25.0\").strip()"` | — |
| [SRC-1AE03B9EC3-L001980](../../agents/web_agent.py#L1980) | 1980 | `"            if fb_token and page_ids:"` | — |
| [SRC-1AE03B9EC3-L001981](../../agents/web_agent.py#L1981) | 1981 | `"                # Scope direct reading to page IDs supplied by the operator and the"` | — |
| [SRC-1AE03B9EC3-L001982](../../agents/web_agent.py#L1982) | 1982 | `"                # permissions granted to this token. This is not global Facebook search."` | — |
| [SRC-1AE03B9EC3-L001983](../../agents/web_agent.py#L1983) | 1983 | `"                query_terms = {"` | — |
| [SRC-1AE03B9EC3-L001984](../../agents/web_agent.py#L1984) | 1984 | `"                    word.casefold()"` | — |
| [SRC-1AE03B9EC3-L001985](../../agents/web_agent.py#L1985) | 1985 | `"                    for word in re.findall(r\"[\\w\\u0600-\\u06FF]+\", query, flags=re.UNICODE)"` | — |
| [SRC-1AE03B9EC3-L001986](../../agents/web_agent.py#L1986) | 1986 | `"                    if len(word) >= 3"` | — |
| [SRC-1AE03B9EC3-L001987](../../agents/web_agent.py#L1987) | 1987 | `"                }"` | — |
| [SRC-1AE03B9EC3-L001988](../../agents/web_agent.py#L1988) | 1988 | `"                for page_id in page_ids:"` | — |
| [SRC-1AE03B9EC3-L001989](../../agents/web_agent.py#L1989) | 1989 | `"                    try:"` | — |
| [SRC-1AE03B9EC3-L001990](../../agents/web_agent.py#L1990) | 1990 | `"                        self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L001991](../../agents/web_agent.py#L1991) | 1991 | `"                        response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L001992](../../agents/web_agent.py#L1992) | 1992 | `"                            f\"https://graph.facebook.com/{graph_version}/{page_id}/posts\","` | — |
| [SRC-1AE03B9EC3-L001993](../../agents/web_agent.py#L1993) | 1993 | `"                            params={"` | — |
| [SRC-1AE03B9EC3-L001994](../../agents/web_agent.py#L1994) | 1994 | `"                                \"fields\": ("` | — |
| [SRC-1AE03B9EC3-L001995](../../agents/web_agent.py#L1995) | 1995 | `"                                    \"message,permalink_url,created_time,\""` | — |
| [SRC-1AE03B9EC3-L001996](../../agents/web_agent.py#L1996) | 1996 | `"                                    \"comments.limit(10){message,created_time,like_count}\""` | — |
| [SRC-1AE03B9EC3-L001997](../../agents/web_agent.py#L1997) | 1997 | `"                                ),"` | — |
| [SRC-1AE03B9EC3-L001998](../../agents/web_agent.py#L1998) | 1998 | `"                                \"limit\": 10,"` | — |
| [SRC-1AE03B9EC3-L001999](../../agents/web_agent.py#L1999) | 1999 | `"                            },"` | — |
| [SRC-1AE03B9EC3-L002000](../../agents/web_agent.py#L2000) | 2000 | `"                            headers={"` | — |
| [SRC-1AE03B9EC3-L002001](../../agents/web_agent.py#L2001) | 2001 | `"                                **headers,"` | — |
| [SRC-1AE03B9EC3-L002002](../../agents/web_agent.py#L2002) | 2002 | `"                                \"Authorization\": \"Bearer \" + fb_token,"` | — |
| [SRC-1AE03B9EC3-L002003](../../agents/web_agent.py#L2003) | 2003 | `"                            },"` | — |
| [SRC-1AE03B9EC3-L002004](../../agents/web_agent.py#L2004) | 2004 | `"                            timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L002005](../../agents/web_agent.py#L2005) | 2005 | `"                            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L002006](../../agents/web_agent.py#L2006) | 2006 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L002007](../../agents/web_agent.py#L2007) | 2007 | `"                        if response.status_code != 200:"` | — |
| [SRC-1AE03B9EC3-L002008](../../agents/web_agent.py#L2008) | 2008 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L002009](../../agents/web_agent.py#L2009) | 2009 | `"                                \"Facebook Pages API unavailable for one configured page \""` | — |
| [SRC-1AE03B9EC3-L002010](../../agents/web_agent.py#L2010) | 2010 | `"                                f\"(HTTP {response.status_code}); verify page ownership, token and permissions.\""` | — |
| [SRC-1AE03B9EC3-L002011](../../agents/web_agent.py#L2011) | 2011 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L002012](../../agents/web_agent.py#L2012) | 2012 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002013](../../agents/web_agent.py#L2013) | 2013 | `"                        posts = response.json().get(\"data\", [])"` | — |
| [SRC-1AE03B9EC3-L002014](../../agents/web_agent.py#L2014) | 2014 | `"                        rank = 0"` | — |
| [SRC-1AE03B9EC3-L002015](../../agents/web_agent.py#L2015) | 2015 | `"                        for post in posts:"` | — |
| [SRC-1AE03B9EC3-L002016](../../agents/web_agent.py#L2016) | 2016 | `"                            message = _clean_text(post.get(\"message\") or \"\", 1400)"` | — |
| [SRC-1AE03B9EC3-L002017](../../agents/web_agent.py#L2017) | 2017 | `"                            comments = post.get(\"comments\", {}).get(\"data\", [])"` | — |
| [SRC-1AE03B9EC3-L002018](../../agents/web_agent.py#L2018) | 2018 | `"                            comment_text = ["` | — |
| [SRC-1AE03B9EC3-L002019](../../agents/web_agent.py#L2019) | 2019 | `"                                _clean_text(item.get(\"message\") or \"\", 500)"` | — |
| [SRC-1AE03B9EC3-L002020](../../agents/web_agent.py#L2020) | 2020 | `"                                for item in comments"` | — |
| [SRC-1AE03B9EC3-L002021](../../agents/web_agent.py#L2021) | 2021 | `"                                if isinstance(item, dict) and item.get(\"message\")"` | — |
| [SRC-1AE03B9EC3-L002022](../../agents/web_agent.py#L2022) | 2022 | `"                            ]"` | — |
| [SRC-1AE03B9EC3-L002023](../../agents/web_agent.py#L2023) | 2023 | `"                            searchable = (message + \" \" + \" \".join(comment_text)).casefold()"` | — |
| [SRC-1AE03B9EC3-L002024](../../agents/web_agent.py#L2024) | 2024 | `"                            matched = sum(term in searchable for term in query_terms)"` | — |
| [SRC-1AE03B9EC3-L002025](../../agents/web_agent.py#L2025) | 2025 | `"                            if query_terms and matched == 0:"` | — |
| [SRC-1AE03B9EC3-L002026](../../agents/web_agent.py#L2026) | 2026 | `"                                continue"` | — |
| [SRC-1AE03B9EC3-L002027](../../agents/web_agent.py#L2027) | 2027 | `"                            permalink = _public_http_url(post.get(\"permalink_url\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L002028](../../agents/web_agent.py#L2028) | 2028 | `"                            if not permalink:"` | — |
| [SRC-1AE03B9EC3-L002029](../../agents/web_agent.py#L2029) | 2029 | `"                                continue"` | — |
| [SRC-1AE03B9EC3-L002030](../../agents/web_agent.py#L2030) | 2030 | `"                            rank += 1"` | — |
| [SRC-1AE03B9EC3-L002031](../../agents/web_agent.py#L2031) | 2031 | `"                            excerpt = message"` | — |
| [SRC-1AE03B9EC3-L002032](../../agents/web_agent.py#L2032) | 2032 | `"                            if comment_text:"` | — |
| [SRC-1AE03B9EC3-L002033](../../agents/web_agent.py#L2033) | 2033 | `"                                excerpt = ("` | — |
| [SRC-1AE03B9EC3-L002034](../../agents/web_agent.py#L2034) | 2034 | `"                                    excerpt + \"\\n\\nتعليقات عامة على المنشور:\\n\""` | — |
| [SRC-1AE03B9EC3-L002035](../../agents/web_agent.py#L2035) | 2035 | `"                                    if excerpt else \"تعليقات عامة على المنشور:\\n\""` | — |
| [SRC-1AE03B9EC3-L002036](../../agents/web_agent.py#L2036) | 2036 | `"                                ) + \"\\n— \".join(comment_text)"` | — |
| [SRC-1AE03B9EC3-L002037](../../agents/web_agent.py#L2037) | 2037 | `"                            results.append({"` | — |
| [SRC-1AE03B9EC3-L002038](../../agents/web_agent.py#L2038) | 2038 | `"                                \"title\": _clean_text(message or \"Facebook public Page post\", 300),"` | — |
| [SRC-1AE03B9EC3-L002039](../../agents/web_agent.py#L2039) | 2039 | `"                                \"url\": permalink,"` | — |
| [SRC-1AE03B9EC3-L002040](../../agents/web_agent.py#L2040) | 2040 | `"                                \"snippet\": _clean_text(excerpt, 1800),"` | — |
| [SRC-1AE03B9EC3-L002041](../../agents/web_agent.py#L2041) | 2041 | `"                                \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L002042](../../agents/web_agent.py#L2042) | 2042 | `"                                \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L002043](../../agents/web_agent.py#L2043) | 2043 | `"                                \"provider\": \"facebook_pages_api\","` | — |
| [SRC-1AE03B9EC3-L002044](../../agents/web_agent.py#L2044) | 2044 | `"                                \"provider_rank\": rank,"` | — |
| [SRC-1AE03B9EC3-L002045](../../agents/web_agent.py#L2045) | 2045 | `"                                \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L002046](../../agents/web_agent.py#L2046) | 2046 | `"                                \"published_at\": _clean_text(post.get(\"created_time\") or \"\", 100),"` | — |
| [SRC-1AE03B9EC3-L002047](../../agents/web_agent.py#L2047) | 2047 | `"                            })"` | — |
| [SRC-1AE03B9EC3-L002048](../../agents/web_agent.py#L2048) | 2048 | `"                            if rank >= 10:"` | — |
| [SRC-1AE03B9EC3-L002049](../../agents/web_agent.py#L2049) | 2049 | `"                                break"` | — |
| [SRC-1AE03B9EC3-L002050](../../agents/web_agent.py#L2050) | 2050 | `"                    except (httpx.HTTPError, OSError, ValueError, KeyError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L002051](../../agents/web_agent.py#L2051) | 2051 | `"                        warnings.append(\"Facebook Pages API failed for one configured page.\")"` | — |
| [SRC-1AE03B9EC3-L002052](../../agents/web_agent.py#L2052) | 2052 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L002053](../../agents/web_agent.py#L2053) | 2053 | `"                warnings.append("` | — |
| [SRC-1AE03B9EC3-L002054](../../agents/web_agent.py#L2054) | 2054 | `"                    \"Facebook direct API is not configured for specific pages; indexed public Facebook pages are still searched.\""` | — |
| [SRC-1AE03B9EC3-L002055](../../agents/web_agent.py#L2055) | 2055 | `"                )"` | — |
| [SRC-1AE03B9EC3-L002056](../../agents/web_agent.py#L2056) | 2056 | `""` | — |
| [SRC-1AE03B9EC3-L002057](../../agents/web_agent.py#L2057) | 2057 | `"        if \"instagram\" in platforms:"` | — |
| [SRC-1AE03B9EC3-L002058](../../agents/web_agent.py#L2058) | 2058 | `"            ig_user_id = os.getenv(\"INSTAGRAM_USER_ID\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L002059](../../agents/web_agent.py#L2059) | 2059 | `"            ig_token = os.getenv(\"INSTAGRAM_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L002060](../../agents/web_agent.py#L2060) | 2060 | `"            graph_version = os.getenv(\"META_GRAPH_VERSION\", \"v25.0\").strip()"` | — |
| [SRC-1AE03B9EC3-L002061](../../agents/web_agent.py#L2061) | 2061 | `"            if ig_user_id and ig_token:"` | — |
| [SRC-1AE03B9EC3-L002062](../../agents/web_agent.py#L2062) | 2062 | `"                # The official Hashtag Search API returns public hashtag media only."` | — |
| [SRC-1AE03B9EC3-L002063](../../agents/web_agent.py#L2063) | 2063 | `"                # It does not search every Instagram post or bypass private accounts."` | — |
| [SRC-1AE03B9EC3-L002064](../../agents/web_agent.py#L2064) | 2064 | `"                hashtags = re.findall(r\"#([\\w\\u0600-\\u06FF]+)\", query, flags=re.UNICODE)"` | — |
| [SRC-1AE03B9EC3-L002065](../../agents/web_agent.py#L2065) | 2065 | `"                if not hashtags:"` | — |
| [SRC-1AE03B9EC3-L002066](../../agents/web_agent.py#L2066) | 2066 | `"                    words = re.findall(r\"[\\w\\u0600-\\u06FF]+\", query, flags=re.UNICODE)"` | — |
| [SRC-1AE03B9EC3-L002067](../../agents/web_agent.py#L2067) | 2067 | `"                    stopwords = {"` | — |
| [SRC-1AE03B9EC3-L002068](../../agents/web_agent.py#L2068) | 2068 | `"                        \"ابحث\", \"بحث\", \"عن\", \"في\", \"على\", \"من\", \"مع\", \"تجارب\","` | — |
| [SRC-1AE03B9EC3-L002069](../../agents/web_agent.py#L2069) | 2069 | `"                        \"الناس\", \"العملاء\", \"منشورات\", \"تعليقات\", \"مواقع\", \"التواصل\","` | — |
| [SRC-1AE03B9EC3-L002070](../../agents/web_agent.py#L2070) | 2070 | `"                        \"الاجتماعي\", \"public\", \"search\", \"social\", \"media\", \"posts\","` | — |
| [SRC-1AE03B9EC3-L002071](../../agents/web_agent.py#L2071) | 2071 | `"                        \"find\", \"about\", \"with\", \"the\", \"and\", \"for\","` | — |
| [SRC-1AE03B9EC3-L002072](../../agents/web_agent.py#L2072) | 2072 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L002073](../../agents/web_agent.py#L2073) | 2073 | `"                    useful = ["` | — |
| [SRC-1AE03B9EC3-L002074](../../agents/web_agent.py#L2074) | 2074 | `"                        word for word in words"` | — |
| [SRC-1AE03B9EC3-L002075](../../agents/web_agent.py#L2075) | 2075 | `"                        if len(word) >= 3 and word.casefold() not in stopwords"` | — |
| [SRC-1AE03B9EC3-L002076](../../agents/web_agent.py#L2076) | 2076 | `"                    ]"` | — |
| [SRC-1AE03B9EC3-L002077](../../agents/web_agent.py#L2077) | 2077 | `"                    if useful:"` | — |
| [SRC-1AE03B9EC3-L002078](../../agents/web_agent.py#L2078) | 2078 | `"                        hashtags = [\"_\".join(useful[:3])]"` | — |
| [SRC-1AE03B9EC3-L002079](../../agents/web_agent.py#L2079) | 2079 | `"                # Meta limits unique hashtag searches over a rolling week; keep this"` | — |
| [SRC-1AE03B9EC3-L002080](../../agents/web_agent.py#L2080) | 2080 | `"                # connector conservative and use no more than two tags per user request."` | — |
| [SRC-1AE03B9EC3-L002081](../../agents/web_agent.py#L2081) | 2081 | `"                for hashtag in list(dict.fromkeys(hashtags))[:1]:"` | — |
| [SRC-1AE03B9EC3-L002082](../../agents/web_agent.py#L2082) | 2082 | `"                    try:"` | — |
| [SRC-1AE03B9EC3-L002083](../../agents/web_agent.py#L2083) | 2083 | `"                        self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L002084](../../agents/web_agent.py#L2084) | 2084 | `"                        search_response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L002085](../../agents/web_agent.py#L2085) | 2085 | `"                            f\"https://graph.facebook.com/{graph_version}/ig_hashtag_search\","` | — |
| [SRC-1AE03B9EC3-L002086](../../agents/web_agent.py#L2086) | 2086 | `"                            params={"` | — |
| [SRC-1AE03B9EC3-L002087](../../agents/web_agent.py#L2087) | 2087 | `"                                \"user_id\": ig_user_id,"` | — |
| [SRC-1AE03B9EC3-L002088](../../agents/web_agent.py#L2088) | 2088 | `"                                \"q\": hashtag,"` | — |
| [SRC-1AE03B9EC3-L002089](../../agents/web_agent.py#L2089) | 2089 | `"                                \"fields\": \"id,name\","` | — |
| [SRC-1AE03B9EC3-L002090](../../agents/web_agent.py#L2090) | 2090 | `"                                \"access_token\": ig_token,"` | — |
| [SRC-1AE03B9EC3-L002091](../../agents/web_agent.py#L2091) | 2091 | `"                            },"` | — |
| [SRC-1AE03B9EC3-L002092](../../agents/web_agent.py#L2092) | 2092 | `"                            headers=headers,"` | — |
| [SRC-1AE03B9EC3-L002093](../../agents/web_agent.py#L2093) | 2093 | `"                            timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L002094](../../agents/web_agent.py#L2094) | 2094 | `"                            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L002095](../../agents/web_agent.py#L2095) | 2095 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L002096](../../agents/web_agent.py#L2096) | 2096 | `"                        if search_response.status_code != 200:"` | — |
| [SRC-1AE03B9EC3-L002097](../../agents/web_agent.py#L2097) | 2097 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L002098](../../agents/web_agent.py#L2098) | 2098 | `"                                \"Instagram Graph API hashtag search unavailable \""` | — |
| [SRC-1AE03B9EC3-L002099](../../agents/web_agent.py#L2099) | 2099 | `"                                f\"(HTTP {search_response.status_code}); check permissions and access.\""` | — |
| [SRC-1AE03B9EC3-L002100](../../agents/web_agent.py#L2100) | 2100 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L002101](../../agents/web_agent.py#L2101) | 2101 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002102](../../agents/web_agent.py#L2102) | 2102 | `"                        tag_data = search_response.json().get(\"data\", [])"` | — |
| [SRC-1AE03B9EC3-L002103](../../agents/web_agent.py#L2103) | 2103 | `"                        if not tag_data:"` | — |
| [SRC-1AE03B9EC3-L002104](../../agents/web_agent.py#L2104) | 2104 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002105](../../agents/web_agent.py#L2105) | 2105 | `"                        hashtag_id = tag_data[0].get(\"id\")"` | — |
| [SRC-1AE03B9EC3-L002106](../../agents/web_agent.py#L2106) | 2106 | `"                        if not hashtag_id:"` | — |
| [SRC-1AE03B9EC3-L002107](../../agents/web_agent.py#L2107) | 2107 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002108](../../agents/web_agent.py#L2108) | 2108 | `"                        self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L002109](../../agents/web_agent.py#L2109) | 2109 | `"                        media_response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L002110](../../agents/web_agent.py#L2110) | 2110 | `"                            f\"https://graph.facebook.com/{graph_version}/{hashtag_id}/recent_media\","` | — |
| [SRC-1AE03B9EC3-L002111](../../agents/web_agent.py#L2111) | 2111 | `"                            params={"` | — |
| [SRC-1AE03B9EC3-L002112](../../agents/web_agent.py#L2112) | 2112 | `"                                \"user_id\": ig_user_id,"` | — |
| [SRC-1AE03B9EC3-L002113](../../agents/web_agent.py#L2113) | 2113 | `"                                \"fields\": \"id,caption,media_type,permalink,timestamp,like_count,comments_count\","` | — |
| [SRC-1AE03B9EC3-L002114](../../agents/web_agent.py#L2114) | 2114 | `"                                \"limit\": 20,"` | — |
| [SRC-1AE03B9EC3-L002115](../../agents/web_agent.py#L2115) | 2115 | `"                                \"access_token\": ig_token,"` | — |
| [SRC-1AE03B9EC3-L002116](../../agents/web_agent.py#L2116) | 2116 | `"                            },"` | — |
| [SRC-1AE03B9EC3-L002117](../../agents/web_agent.py#L2117) | 2117 | `"                            headers=headers,"` | — |
| [SRC-1AE03B9EC3-L002118](../../agents/web_agent.py#L2118) | 2118 | `"                            timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L002119](../../agents/web_agent.py#L2119) | 2119 | `"                            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L002120](../../agents/web_agent.py#L2120) | 2120 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L002121](../../agents/web_agent.py#L2121) | 2121 | `"                        if media_response.status_code != 200:"` | — |
| [SRC-1AE03B9EC3-L002122](../../agents/web_agent.py#L2122) | 2122 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L002123](../../agents/web_agent.py#L2123) | 2123 | `"                                \"Instagram public hashtag media unavailable \""` | — |
| [SRC-1AE03B9EC3-L002124](../../agents/web_agent.py#L2124) | 2124 | `"                                f\"(HTTP {media_response.status_code}).\""` | — |
| [SRC-1AE03B9EC3-L002125](../../agents/web_agent.py#L2125) | 2125 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L002126](../../agents/web_agent.py#L2126) | 2126 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002127](../../agents/web_agent.py#L2127) | 2127 | `"                        items = media_response.json().get(\"data\", [])"` | — |
| [SRC-1AE03B9EC3-L002128](../../agents/web_agent.py#L2128) | 2128 | `"                        for item in items:"` | — |
| [SRC-1AE03B9EC3-L002129](../../agents/web_agent.py#L2129) | 2129 | `"                            url = _public_http_url(item.get(\"permalink\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L002130](../../agents/web_agent.py#L2130) | 2130 | `"                            if not url:"` | — |
| [SRC-1AE03B9EC3-L002131](../../agents/web_agent.py#L2131) | 2131 | `"                                continue"` | — |
| [SRC-1AE03B9EC3-L002132](../../agents/web_agent.py#L2132) | 2132 | `"                            metrics = []"` | — |
| [SRC-1AE03B9EC3-L002133](../../agents/web_agent.py#L2133) | 2133 | `"                            if item.get(\"like_count\") is not None:"` | — |
| [SRC-1AE03B9EC3-L002134](../../agents/web_agent.py#L2134) | 2134 | `"                                metrics.append(\"likes=\" + str(item[\"like_count\"]))"` | — |
| [SRC-1AE03B9EC3-L002135](../../agents/web_agent.py#L2135) | 2135 | `"                            if item.get(\"comments_count\") is not None:"` | — |
| [SRC-1AE03B9EC3-L002136](../../agents/web_agent.py#L2136) | 2136 | `"                                metrics.append(\"comments=\" + str(item[\"comments_count\"]))"` | — |
| [SRC-1AE03B9EC3-L002137](../../agents/web_agent.py#L2137) | 2137 | `"                            caption = _clean_text(item.get(\"caption\") or \"\", 1200)"` | — |
| [SRC-1AE03B9EC3-L002138](../../agents/web_agent.py#L2138) | 2138 | `"                            if metrics:"` | — |
| [SRC-1AE03B9EC3-L002139](../../agents/web_agent.py#L2139) | 2139 | `"                                caption = (caption + \" \| \" if caption else \"\") + \", \".join(metrics)"` | — |
| [SRC-1AE03B9EC3-L002140](../../agents/web_agent.py#L2140) | 2140 | `"                            results.append({"` | — |
| [SRC-1AE03B9EC3-L002141](../../agents/web_agent.py#L2141) | 2141 | `"                                \"title\": \"Instagram public hashtag: #\" + hashtag,"` | — |
| [SRC-1AE03B9EC3-L002142](../../agents/web_agent.py#L2142) | 2142 | `"                                \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L002143](../../agents/web_agent.py#L2143) | 2143 | `"                                \"snippet\": caption,"` | — |
| [SRC-1AE03B9EC3-L002144](../../agents/web_agent.py#L2144) | 2144 | `"                                \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L002145](../../agents/web_agent.py#L2145) | 2145 | `"                                \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L002146](../../agents/web_agent.py#L2146) | 2146 | `"                                \"provider\": \"instagram_graph_api\","` | — |
| [SRC-1AE03B9EC3-L002147](../../agents/web_agent.py#L2147) | 2147 | `"                                \"provider_rank\": len(["` | — |
| [SRC-1AE03B9EC3-L002148](../../agents/web_agent.py#L2148) | 2148 | `"                                    row for row in results"` | — |
| [SRC-1AE03B9EC3-L002149](../../agents/web_agent.py#L2149) | 2149 | `"                                    if row.get(\"provider\") == \"instagram_graph_api\""` | — |
| [SRC-1AE03B9EC3-L002150](../../agents/web_agent.py#L2150) | 2150 | `"                                ]) + 1,"` | — |
| [SRC-1AE03B9EC3-L002151](../../agents/web_agent.py#L2151) | 2151 | `"                                \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L002152](../../agents/web_agent.py#L2152) | 2152 | `"                                \"published_at\": _clean_text(item.get(\"timestamp\") or \"\", 100),"` | — |
| [SRC-1AE03B9EC3-L002153](../../agents/web_agent.py#L2153) | 2153 | `"                            })"` | — |
| [SRC-1AE03B9EC3-L002154](../../agents/web_agent.py#L2154) | 2154 | `"                    except (httpx.HTTPError, OSError, ValueError, KeyError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L002155](../../agents/web_agent.py#L2155) | 2155 | `"                        warnings.append(\"Instagram Graph API search failed for a requested hashtag.\")"` | — |
| [SRC-1AE03B9EC3-L002156](../../agents/web_agent.py#L2156) | 2156 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L002157](../../agents/web_agent.py#L2157) | 2157 | `"                warnings.append("` | — |
| [SRC-1AE03B9EC3-L002158](../../agents/web_agent.py#L2158) | 2158 | `"                    \"Instagram direct API is not configured; indexed public Instagram pages are still searched.\""` | — |
| [SRC-1AE03B9EC3-L002159](../../agents/web_agent.py#L2159) | 2159 | `"                )"` | — |
| [SRC-1AE03B9EC3-L002160](../../agents/web_agent.py#L2160) | 2160 | `""` | — |
| [SRC-1AE03B9EC3-L002161](../../agents/web_agent.py#L2161) | 2161 | `"        if \"x\" in platforms and os.getenv(\"X_BEARER_TOKEN\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L002162](../../agents/web_agent.py#L2162) | 2162 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L002163](../../agents/web_agent.py#L2163) | 2163 | `"                self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L002164](../../agents/web_agent.py#L2164) | 2164 | `"                response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L002165](../../agents/web_agent.py#L2165) | 2165 | `"                    \"https://api.x.com/2/tweets/search/recent\","` | — |
| [SRC-1AE03B9EC3-L002166](../../agents/web_agent.py#L2166) | 2166 | `"                    params={"` | — |
| [SRC-1AE03B9EC3-L002167](../../agents/web_agent.py#L2167) | 2167 | `"                        \"query\": query + \" -is:retweet\","` | — |
| [SRC-1AE03B9EC3-L002168](../../agents/web_agent.py#L2168) | 2168 | `"                        \"max_results\": 10,"` | — |
| [SRC-1AE03B9EC3-L002169](../../agents/web_agent.py#L2169) | 2169 | `"                        \"tweet.fields\": \"created_at,lang,public_metrics,author_id\","` | — |
| [SRC-1AE03B9EC3-L002170](../../agents/web_agent.py#L2170) | 2170 | `"                        \"expansions\": \"author_id\","` | — |
| [SRC-1AE03B9EC3-L002171](../../agents/web_agent.py#L2171) | 2171 | `"                        \"user.fields\": \"name,username\","` | — |
| [SRC-1AE03B9EC3-L002172](../../agents/web_agent.py#L2172) | 2172 | `"                    },"` | — |
| [SRC-1AE03B9EC3-L002173](../../agents/web_agent.py#L2173) | 2173 | `"                    headers={"` | — |
| [SRC-1AE03B9EC3-L002174](../../agents/web_agent.py#L2174) | 2174 | `"                        **headers,"` | — |
| [SRC-1AE03B9EC3-L002175](../../agents/web_agent.py#L2175) | 2175 | `"                        \"Authorization\": \"Bearer \" + os.getenv(\"X_BEARER_TOKEN\", \"\").strip(),"` | — |
| [SRC-1AE03B9EC3-L002176](../../agents/web_agent.py#L2176) | 2176 | `"                    },"` | — |
| [SRC-1AE03B9EC3-L002177](../../agents/web_agent.py#L2177) | 2177 | `"                    timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L002178](../../agents/web_agent.py#L2178) | 2178 | `"                    follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L002179](../../agents/web_agent.py#L2179) | 2179 | `"                )"` | — |
| [SRC-1AE03B9EC3-L002180](../../agents/web_agent.py#L2180) | 2180 | `"                if response.status_code == 200:"` | — |
| [SRC-1AE03B9EC3-L002181](../../agents/web_agent.py#L2181) | 2181 | `"                    data = response.json()"` | — |
| [SRC-1AE03B9EC3-L002182](../../agents/web_agent.py#L2182) | 2182 | `"                    authors = {"` | — |
| [SRC-1AE03B9EC3-L002183](../../agents/web_agent.py#L2183) | 2183 | `"                        user.get(\"id\"): user"` | — |
| [SRC-1AE03B9EC3-L002184](../../agents/web_agent.py#L2184) | 2184 | `"                        for user in data.get(\"includes\", {}).get(\"users\", [])"` | — |
| [SRC-1AE03B9EC3-L002185](../../agents/web_agent.py#L2185) | 2185 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L002186](../../agents/web_agent.py#L2186) | 2186 | `"                    for item in data.get(\"data\", []):"` | — |
| [SRC-1AE03B9EC3-L002187](../../agents/web_agent.py#L2187) | 2187 | `"                        author = authors.get(item.get(\"author_id\"), {})"` | — |
| [SRC-1AE03B9EC3-L002188](../../agents/web_agent.py#L2188) | 2188 | `"                        username = author.get(\"username\", \"\")"` | — |
| [SRC-1AE03B9EC3-L002189](../../agents/web_agent.py#L2189) | 2189 | `"                        post_id = item.get(\"id\", \"\")"` | — |
| [SRC-1AE03B9EC3-L002190](../../agents/web_agent.py#L2190) | 2190 | `"                        if not username or not post_id:"` | — |
| [SRC-1AE03B9EC3-L002191](../../agents/web_agent.py#L2191) | 2191 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002192](../../agents/web_agent.py#L2192) | 2192 | `"                        results.append({"` | — |
| [SRC-1AE03B9EC3-L002193](../../agents/web_agent.py#L2193) | 2193 | `"                            \"title\": _clean_text(author.get(\"name\") or username, 300),"` | — |
| [SRC-1AE03B9EC3-L002194](../../agents/web_agent.py#L2194) | 2194 | `"                            \"url\": f\"https://x.com/{username}/status/{post_id}\","` | — |
| [SRC-1AE03B9EC3-L002195](../../agents/web_agent.py#L2195) | 2195 | `"                            \"snippet\": _clean_text(item.get(\"text\") or \"\", 1200),"` | — |
| [SRC-1AE03B9EC3-L002196](../../agents/web_agent.py#L2196) | 2196 | `"                            \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L002197](../../agents/web_agent.py#L2197) | 2197 | `"                            \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L002198](../../agents/web_agent.py#L2198) | 2198 | `"                            \"provider\": \"x_official_api\","` | — |
| [SRC-1AE03B9EC3-L002199](../../agents/web_agent.py#L2199) | 2199 | `"                            \"provider_rank\": len(["` | — |
| [SRC-1AE03B9EC3-L002200](../../agents/web_agent.py#L2200) | 2200 | `"                                row for row in results"` | — |
| [SRC-1AE03B9EC3-L002201](../../agents/web_agent.py#L2201) | 2201 | `"                                if row.get(\"provider\") == \"x_official_api\""` | — |
| [SRC-1AE03B9EC3-L002202](../../agents/web_agent.py#L2202) | 2202 | `"                            ]) + 1,"` | — |
| [SRC-1AE03B9EC3-L002203](../../agents/web_agent.py#L2203) | 2203 | `"                            \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L002204](../../agents/web_agent.py#L2204) | 2204 | `"                            \"published_at\": _clean_text(item.get(\"created_at\") or \"\", 100),"` | — |
| [SRC-1AE03B9EC3-L002205](../../agents/web_agent.py#L2205) | 2205 | `"                        })"` | — |
| [SRC-1AE03B9EC3-L002206](../../agents/web_agent.py#L2206) | 2206 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L002207](../../agents/web_agent.py#L2207) | 2207 | `"                    warnings.append(f\"X API unavailable (HTTP {response.status_code})\")"` | — |
| [SRC-1AE03B9EC3-L002208](../../agents/web_agent.py#L2208) | 2208 | `"            except (httpx.HTTPError, OSError, ValueError, KeyError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L002209](../../agents/web_agent.py#L2209) | 2209 | `"                warnings.append(\"X API unavailable for this request\")"` | — |
| [SRC-1AE03B9EC3-L002210](../../agents/web_agent.py#L2210) | 2210 | `"        elif \"x\" in platforms:"` | — |
| [SRC-1AE03B9EC3-L002211](../../agents/web_agent.py#L2211) | 2211 | `"            warnings.append(\"X direct API is not configured; indexed public X pages are still searched.\")"` | — |
| [SRC-1AE03B9EC3-L002212](../../agents/web_agent.py#L2212) | 2212 | `""` | — |
| [SRC-1AE03B9EC3-L002213](../../agents/web_agent.py#L2213) | 2213 | `"        if \"youtube\" in platforms and os.getenv(\"YOUTUBE_API_KEY\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L002214](../../agents/web_agent.py#L2214) | 2214 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L002215](../../agents/web_agent.py#L2215) | 2215 | `"                self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L002216](../../agents/web_agent.py#L2216) | 2216 | `"                response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L002217](../../agents/web_agent.py#L2217) | 2217 | `"                    \"https://www.googleapis.com/youtube/v3/search\","` | — |
| [SRC-1AE03B9EC3-L002218](../../agents/web_agent.py#L2218) | 2218 | `"                    params={"` | — |
| [SRC-1AE03B9EC3-L002219](../../agents/web_agent.py#L2219) | 2219 | `"                        \"part\": \"snippet\","` | — |
| [SRC-1AE03B9EC3-L002220](../../agents/web_agent.py#L2220) | 2220 | `"                        \"q\": query,"` | — |
| [SRC-1AE03B9EC3-L002221](../../agents/web_agent.py#L2221) | 2221 | `"                        \"type\": \"video\","` | — |
| [SRC-1AE03B9EC3-L002222](../../agents/web_agent.py#L2222) | 2222 | `"                        \"maxResults\": 8,"` | — |
| [SRC-1AE03B9EC3-L002223](../../agents/web_agent.py#L2223) | 2223 | `"                        \"key\": os.getenv(\"YOUTUBE_API_KEY\", \"\").strip(),"` | — |
| [SRC-1AE03B9EC3-L002224](../../agents/web_agent.py#L2224) | 2224 | `"                    },"` | — |
| [SRC-1AE03B9EC3-L002225](../../agents/web_agent.py#L2225) | 2225 | `"                    headers=headers,"` | — |
| [SRC-1AE03B9EC3-L002226](../../agents/web_agent.py#L2226) | 2226 | `"                    timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L002227](../../agents/web_agent.py#L2227) | 2227 | `"                    follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L002228](../../agents/web_agent.py#L2228) | 2228 | `"                )"` | — |
| [SRC-1AE03B9EC3-L002229](../../agents/web_agent.py#L2229) | 2229 | `"                if response.status_code == 200:"` | — |
| [SRC-1AE03B9EC3-L002230](../../agents/web_agent.py#L2230) | 2230 | `"                    data = response.json()"` | — |
| [SRC-1AE03B9EC3-L002231](../../agents/web_agent.py#L2231) | 2231 | `"                    for item in data.get(\"items\", []):"` | — |
| [SRC-1AE03B9EC3-L002232](../../agents/web_agent.py#L2232) | 2232 | `"                        video_id = item.get(\"id\", {}).get(\"videoId\")"` | — |
| [SRC-1AE03B9EC3-L002233](../../agents/web_agent.py#L2233) | 2233 | `"                        snippet = item.get(\"snippet\", {})"` | — |
| [SRC-1AE03B9EC3-L002234](../../agents/web_agent.py#L2234) | 2234 | `"                        if not video_id:"` | — |
| [SRC-1AE03B9EC3-L002235](../../agents/web_agent.py#L2235) | 2235 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002236](../../agents/web_agent.py#L2236) | 2236 | `"                        results.append({"` | — |
| [SRC-1AE03B9EC3-L002237](../../agents/web_agent.py#L2237) | 2237 | `"                            \"title\": _clean_text(snippet.get(\"title\") or \"\", 300),"` | — |
| [SRC-1AE03B9EC3-L002238](../../agents/web_agent.py#L2238) | 2238 | `"                            \"url\": f\"https://www.youtube.com/watch?v={video_id}\","` | — |
| [SRC-1AE03B9EC3-L002239](../../agents/web_agent.py#L2239) | 2239 | `"                            \"snippet\": _clean_text(snippet.get(\"description\") or \"\", 1200),"` | — |
| [SRC-1AE03B9EC3-L002240](../../agents/web_agent.py#L2240) | 2240 | `"                            \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L002241](../../agents/web_agent.py#L2241) | 2241 | `"                            \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L002242](../../agents/web_agent.py#L2242) | 2242 | `"                            \"provider\": \"youtube_data_api\","` | — |
| [SRC-1AE03B9EC3-L002243](../../agents/web_agent.py#L2243) | 2243 | `"                            \"provider_rank\": len(["` | — |
| [SRC-1AE03B9EC3-L002244](../../agents/web_agent.py#L2244) | 2244 | `"                                row for row in results"` | — |
| [SRC-1AE03B9EC3-L002245](../../agents/web_agent.py#L2245) | 2245 | `"                                if row.get(\"provider\") == \"youtube_data_api\""` | — |
| [SRC-1AE03B9EC3-L002246](../../agents/web_agent.py#L2246) | 2246 | `"                            ]) + 1,"` | — |
| [SRC-1AE03B9EC3-L002247](../../agents/web_agent.py#L2247) | 2247 | `"                            \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L002248](../../agents/web_agent.py#L2248) | 2248 | `"                            \"published_at\": _clean_text(snippet.get(\"publishedAt\") or \"\", 100),"` | — |
| [SRC-1AE03B9EC3-L002249](../../agents/web_agent.py#L2249) | 2249 | `"                        })"` | — |
| [SRC-1AE03B9EC3-L002250](../../agents/web_agent.py#L2250) | 2250 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L002251](../../agents/web_agent.py#L2251) | 2251 | `"                    warnings.append(f\"YouTube Data API unavailable (HTTP {response.status_code})\")"` | — |
| [SRC-1AE03B9EC3-L002252](../../agents/web_agent.py#L2252) | 2252 | `"            except (httpx.HTTPError, OSError, ValueError, KeyError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L002253](../../agents/web_agent.py#L2253) | 2253 | `"                warnings.append(\"YouTube Data API unavailable for this request\")"` | — |
| [SRC-1AE03B9EC3-L002254](../../agents/web_agent.py#L2254) | 2254 | `"        elif \"youtube\" in platforms:"` | — |
| [SRC-1AE03B9EC3-L002255](../../agents/web_agent.py#L2255) | 2255 | `"            warnings.append(\"YouTube direct API is not configured; indexed public YouTube pages are still searched.\")"` | — |
| [SRC-1AE03B9EC3-L002256](../../agents/web_agent.py#L2256) | 2256 | `""` | — |
| [SRC-1AE03B9EC3-L002257](../../agents/web_agent.py#L2257) | 2257 | `"        return results, warnings"` | — |
| [SRC-1AE03B9EC3-L002258](../../agents/web_agent.py#L2258) | 2258 | `""` | — |
| [SRC-1AE03B9EC3-L002259](../../agents/web_agent.py#L2259) | 2259 | `"    def _fetch_page(self, url: str) -> tuple[str, str]:"` | — |
| [SRC-1AE03B9EC3-L002260](../../agents/web_agent.py#L2260) | 2260 | `"        \"\"\"Fetch a public page with bounded redirects and an inspectable extraction outcome.\"\"\""` | — |
| [SRC-1AE03B9EC3-L002261](../../agents/web_agent.py#L2261) | 2261 | `"        def result("` | — |
| [SRC-1AE03B9EC3-L002262](../../agents/web_agent.py#L2262) | 2262 | `"            title: str = \"\","` | — |
| [SRC-1AE03B9EC3-L002263](../../agents/web_agent.py#L2263) | 2263 | `"            page_text: str = \"\","` | — |
| [SRC-1AE03B9EC3-L002264](../../agents/web_agent.py#L2264) | 2264 | `"            status: str = \"unknown\","` | — |
| [SRC-1AE03B9EC3-L002265](../../agents/web_agent.py#L2265) | 2265 | `"            error_class: str \| None = None,"` | — |
| [SRC-1AE03B9EC3-L002266](../../agents/web_agent.py#L2266) | 2266 | `"        ) -> PageFetchResult:"` | — |
| [SRC-1AE03B9EC3-L002267](../../agents/web_agent.py#L2267) | 2267 | `"            return PageFetchResult(title, page_text, status, error_class)"` | — |
| [SRC-1AE03B9EC3-L002268](../../agents/web_agent.py#L2268) | 2268 | `""` | — |
| [SRC-1AE03B9EC3-L002269](../../agents/web_agent.py#L2269) | 2269 | `"        current_url = _public_http_url(url)"` | — |
| [SRC-1AE03B9EC3-L002270](../../agents/web_agent.py#L2270) | 2270 | `"        if not current_url:"` | — |
| [SRC-1AE03B9EC3-L002271](../../agents/web_agent.py#L2271) | 2271 | `"            return result(status=\"rejected_url\", error_class=\"PublicUrlRejected\")"` | — |
| [SRC-1AE03B9EC3-L002272](../../agents/web_agent.py#L2272) | 2272 | `"        budget = getattr(self, \"_request_budget\", None)"` | — |
| [SRC-1AE03B9EC3-L002273](../../agents/web_agent.py#L2273) | 2273 | `"        if budget is not None:"` | — |
| [SRC-1AE03B9EC3-L002274](../../agents/web_agent.py#L2274) | 2274 | `"            budget.reserve(\"page_fetches\")"` | — |
| [SRC-1AE03B9EC3-L002275](../../agents/web_agent.py#L2275) | 2275 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L002276](../../agents/web_agent.py#L2276) | 2276 | `"            import httpx"` | — |
| [SRC-1AE03B9EC3-L002277](../../agents/web_agent.py#L2277) | 2277 | `"            from bs4 import BeautifulSoup"` | — |
| [SRC-1AE03B9EC3-L002278](../../agents/web_agent.py#L2278) | 2278 | `"        except ImportError as exc:"` | — |
| [SRC-1AE03B9EC3-L002279](../../agents/web_agent.py#L2279) | 2279 | `"            raise AgentDependencyError("` | — |
| [SRC-1AE03B9EC3-L002280](../../agents/web_agent.py#L2280) | 2280 | `"                \"حزم استخراج الصفحات غير مثبتة. نفّذ: python -m pip install -e .\""` | — |
| [SRC-1AE03B9EC3-L002281](../../agents/web_agent.py#L2281) | 2281 | `"            ) from exc"` | — |
| [SRC-1AE03B9EC3-L002282](../../agents/web_agent.py#L2282) | 2282 | `""` | — |
| [SRC-1AE03B9EC3-L002283](../../agents/web_agent.py#L2283) | 2283 | `"        headers = {"` | — |
| [SRC-1AE03B9EC3-L002284](../../agents/web_agent.py#L2284) | 2284 | `"            \"User-Agent\": \"OmaraiResearchBot/1.1 (public page research; no login)\","` | — |
| [SRC-1AE03B9EC3-L002285](../../agents/web_agent.py#L2285) | 2285 | `"            \"Accept\": \"text/html,application/xhtml+xml,text/plain;q=0.8\","` | — |
| [SRC-1AE03B9EC3-L002286](../../agents/web_agent.py#L2286) | 2286 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002287](../../agents/web_agent.py#L2287) | 2287 | `"        media_type = \"\""` | — |
| [SRC-1AE03B9EC3-L002288](../../agents/web_agent.py#L2288) | 2288 | `"        html = \"\""` | — |
| [SRC-1AE03B9EC3-L002289](../../agents/web_agent.py#L2289) | 2289 | `"        bytes_truncated = False"` | — |
| [SRC-1AE03B9EC3-L002290](../../agents/web_agent.py#L2290) | 2290 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L002291](../../agents/web_agent.py#L2291) | 2291 | `"            with httpx.Client("` | — |
| [SRC-1AE03B9EC3-L002292](../../agents/web_agent.py#L2292) | 2292 | `"                timeout=self._effective_timeout(8.0),"` | — |
| [SRC-1AE03B9EC3-L002293](../../agents/web_agent.py#L2293) | 2293 | `"                follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L002294](../../agents/web_agent.py#L2294) | 2294 | `"                headers=headers,"` | — |
| [SRC-1AE03B9EC3-L002295](../../agents/web_agent.py#L2295) | 2295 | `"                verify=True,"` | — |
| [SRC-1AE03B9EC3-L002296](../../agents/web_agent.py#L2296) | 2296 | `"                trust_env=False,"` | — |
| [SRC-1AE03B9EC3-L002297](../../agents/web_agent.py#L2297) | 2297 | `"            ) as client:"` | — |
| [SRC-1AE03B9EC3-L002298](../../agents/web_agent.py#L2298) | 2298 | `"                for redirect_number in range(4):"` | — |
| [SRC-1AE03B9EC3-L002299](../../agents/web_agent.py#L2299) | 2299 | `"                    parsed = urllib.parse.urlparse(current_url)"` | — |
| [SRC-1AE03B9EC3-L002300](../../agents/web_agent.py#L2300) | 2300 | `"                    host = parsed.hostname or \"\""` | — |
| [SRC-1AE03B9EC3-L002301](../../agents/web_agent.py#L2301) | 2301 | `"                    # Resolve and pin a public IP. Do not let the HTTP client resolve"` | — |
| [SRC-1AE03B9EC3-L002302](../../agents/web_agent.py#L2302) | 2302 | `"                    # the original hostname a second time."` | — |
| [SRC-1AE03B9EC3-L002303](../../agents/web_agent.py#L2303) | 2303 | `"                    public_ips = _public_ip_literals(host)"` | — |
| [SRC-1AE03B9EC3-L002304](../../agents/web_agent.py#L2304) | 2304 | `"                    if not public_ips:"` | — |
| [SRC-1AE03B9EC3-L002305](../../agents/web_agent.py#L2305) | 2305 | `"                        return result(status=\"blocked_or_unresolved_host\", error_class=\"HostResolutionOrSSRFCheck\")"` | — |
| [SRC-1AE03B9EC3-L002306](../../agents/web_agent.py#L2306) | 2306 | `"                    connect_url = _pinned_connect_url(current_url, public_ips[0])"` | — |
| [SRC-1AE03B9EC3-L002307](../../agents/web_agent.py#L2307) | 2307 | `"                    if not connect_url:"` | — |
| [SRC-1AE03B9EC3-L002308](../../agents/web_agent.py#L2308) | 2308 | `"                        return result(status=\"blocked_connection_target\", error_class=\"PinnedTargetRejected\")"` | — |
| [SRC-1AE03B9EC3-L002309](../../agents/web_agent.py#L2309) | 2309 | `"                    request_headers = {\"Host\": host}"` | — |
| [SRC-1AE03B9EC3-L002310](../../agents/web_agent.py#L2310) | 2310 | `"                    extensions = {\"sni_hostname\": host} if parsed.scheme == \"https\" else {}"` | — |
| [SRC-1AE03B9EC3-L002311](../../agents/web_agent.py#L2311) | 2311 | `"                    with client.stream("` | — |
| [SRC-1AE03B9EC3-L002312](../../agents/web_agent.py#L2312) | 2312 | `"                        \"GET\","` | — |
| [SRC-1AE03B9EC3-L002313](../../agents/web_agent.py#L2313) | 2313 | `"                        connect_url,"` | — |
| [SRC-1AE03B9EC3-L002314](../../agents/web_agent.py#L2314) | 2314 | `"                        headers=request_headers,"` | — |
| [SRC-1AE03B9EC3-L002315](../../agents/web_agent.py#L2315) | 2315 | `"                        extensions=extensions,"` | — |
| [SRC-1AE03B9EC3-L002316](../../agents/web_agent.py#L2316) | 2316 | `"                    ) as response:"` | — |
| [SRC-1AE03B9EC3-L002317](../../agents/web_agent.py#L2317) | 2317 | `"                        if response.status_code in {301, 302, 303, 307, 308}:"` | — |
| [SRC-1AE03B9EC3-L002318](../../agents/web_agent.py#L2318) | 2318 | `"                            location = response.headers.get(\"location\", \"\")"` | — |
| [SRC-1AE03B9EC3-L002319](../../agents/web_agent.py#L2319) | 2319 | `"                            if not location or redirect_number >= 3:"` | — |
| [SRC-1AE03B9EC3-L002320](../../agents/web_agent.py#L2320) | 2320 | `"                                return result(status=\"redirect_failed\", error_class=\"RedirectLimitOrMissingLocation\")"` | — |
| [SRC-1AE03B9EC3-L002321](../../agents/web_agent.py#L2321) | 2321 | `"                            target = _public_http_url("` | — |
| [SRC-1AE03B9EC3-L002322](../../agents/web_agent.py#L2322) | 2322 | `"                                urllib.parse.urljoin(current_url, location)"` | — |
| [SRC-1AE03B9EC3-L002323](../../agents/web_agent.py#L2323) | 2323 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L002324](../../agents/web_agent.py#L2324) | 2324 | `"                            if not target:"` | — |
| [SRC-1AE03B9EC3-L002325](../../agents/web_agent.py#L2325) | 2325 | `"                                return result(status=\"redirect_rejected\", error_class=\"RedirectTargetRejected\")"` | — |
| [SRC-1AE03B9EC3-L002326](../../agents/web_agent.py#L2326) | 2326 | `"                            current_url = target"` | — |
| [SRC-1AE03B9EC3-L002327](../../agents/web_agent.py#L2327) | 2327 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002328](../../agents/web_agent.py#L2328) | 2328 | `"                        if response.status_code < 200 or response.status_code >= 300:"` | — |
| [SRC-1AE03B9EC3-L002329](../../agents/web_agent.py#L2329) | 2329 | `"                            return result(status=\"http_error\", error_class=\"HTTPStatus\")"` | — |
| [SRC-1AE03B9EC3-L002330](../../agents/web_agent.py#L2330) | 2330 | `"                        media_type = response.headers.get("` | — |
| [SRC-1AE03B9EC3-L002331](../../agents/web_agent.py#L2331) | 2331 | `"                            \"content-type\", \"\""` | — |
| [SRC-1AE03B9EC3-L002332](../../agents/web_agent.py#L2332) | 2332 | `"                        ).split(\";\")[0].lower()"` | — |
| [SRC-1AE03B9EC3-L002333](../../agents/web_agent.py#L2333) | 2333 | `"                        if media_type not in {"` | — |
| [SRC-1AE03B9EC3-L002334](../../agents/web_agent.py#L2334) | 2334 | `"                            \"text/html\", \"application/xhtml+xml\", \"text/plain\""` | — |
| [SRC-1AE03B9EC3-L002335](../../agents/web_agent.py#L2335) | 2335 | `"                        }:"` | — |
| [SRC-1AE03B9EC3-L002336](../../agents/web_agent.py#L2336) | 2336 | `"                            return result(status=\"unsupported_content_type\", error_class=\"UnsupportedContentType\")"` | — |
| [SRC-1AE03B9EC3-L002337](../../agents/web_agent.py#L2337) | 2337 | `"                        content_length = response.headers.get(\"content-length\")"` | — |
| [SRC-1AE03B9EC3-L002338](../../agents/web_agent.py#L2338) | 2338 | `"                        if content_length:"` | — |
| [SRC-1AE03B9EC3-L002339](../../agents/web_agent.py#L2339) | 2339 | `"                            try:"` | — |
| [SRC-1AE03B9EC3-L002340](../../agents/web_agent.py#L2340) | 2340 | `"                                if int(content_length) > MAX_PAGE_BYTES:"` | — |
| [SRC-1AE03B9EC3-L002341](../../agents/web_agent.py#L2341) | 2341 | `"                                    return result(status=\"page_too_large\", error_class=\"ContentLengthLimit\")"` | — |
| [SRC-1AE03B9EC3-L002342](../../agents/web_agent.py#L2342) | 2342 | `"                            except ValueError:"` | — |
| [SRC-1AE03B9EC3-L002343](../../agents/web_agent.py#L2343) | 2343 | `"                                pass"` | — |
| [SRC-1AE03B9EC3-L002344](../../agents/web_agent.py#L2344) | 2344 | `"                        chunks: list[bytes] = []"` | — |
| [SRC-1AE03B9EC3-L002345](../../agents/web_agent.py#L2345) | 2345 | `"                        count = 0"` | — |
| [SRC-1AE03B9EC3-L002346](../../agents/web_agent.py#L2346) | 2346 | `"                        for chunk in response.iter_bytes():"` | — |
| [SRC-1AE03B9EC3-L002347](../../agents/web_agent.py#L2347) | 2347 | `"                            count += len(chunk)"` | — |
| [SRC-1AE03B9EC3-L002348](../../agents/web_agent.py#L2348) | 2348 | `"                            if count > MAX_PAGE_BYTES:"` | — |
| [SRC-1AE03B9EC3-L002349](../../agents/web_agent.py#L2349) | 2349 | `"                                remaining = max(0, MAX_PAGE_BYTES - (count - len(chunk)))"` | — |
| [SRC-1AE03B9EC3-L002350](../../agents/web_agent.py#L2350) | 2350 | `"                                if remaining:"` | — |
| [SRC-1AE03B9EC3-L002351](../../agents/web_agent.py#L2351) | 2351 | `"                                    chunks.append(chunk[:remaining])"` | — |
| [SRC-1AE03B9EC3-L002352](../../agents/web_agent.py#L2352) | 2352 | `"                                bytes_truncated = True"` | — |
| [SRC-1AE03B9EC3-L002353](../../agents/web_agent.py#L2353) | 2353 | `"                                break"` | — |
| [SRC-1AE03B9EC3-L002354](../../agents/web_agent.py#L2354) | 2354 | `"                            chunks.append(chunk)"` | — |
| [SRC-1AE03B9EC3-L002355](../../agents/web_agent.py#L2355) | 2355 | `"                        raw = b\"\".join(chunks)"` | — |
| [SRC-1AE03B9EC3-L002356](../../agents/web_agent.py#L2356) | 2356 | `"                        encoding = response.encoding or \"utf-8\""` | — |
| [SRC-1AE03B9EC3-L002357](../../agents/web_agent.py#L2357) | 2357 | `"                        html = raw.decode(encoding, errors=\"replace\")"` | — |
| [SRC-1AE03B9EC3-L002358](../../agents/web_agent.py#L2358) | 2358 | `"                        break"` | — |
| [SRC-1AE03B9EC3-L002359](../../agents/web_agent.py#L2359) | 2359 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L002360](../../agents/web_agent.py#L2360) | 2360 | `"                    return result(status=\"redirect_limit\", error_class=\"RedirectLimit\")"` | — |
| [SRC-1AE03B9EC3-L002361](../../agents/web_agent.py#L2361) | 2361 | `"        except (OSError, ValueError, httpx.HTTPError) as exc:"` | — |
| [SRC-1AE03B9EC3-L002362](../../agents/web_agent.py#L2362) | 2362 | `"            return result(status=\"network_error\", error_class=type(exc).__name__)"` | — |
| [SRC-1AE03B9EC3-L002363](../../agents/web_agent.py#L2363) | 2363 | `""` | — |
| [SRC-1AE03B9EC3-L002364](../../agents/web_agent.py#L2364) | 2364 | `"        if media_type == \"text/plain\":"` | — |
| [SRC-1AE03B9EC3-L002365](../../agents/web_agent.py#L2365) | 2365 | `"            bounded_text = _clean_text(html, MAX_PAGE_TEXT_CHARS + 1)"` | — |
| [SRC-1AE03B9EC3-L002366](../../agents/web_agent.py#L2366) | 2366 | `"            text_truncated = len(bounded_text) > MAX_PAGE_TEXT_CHARS"` | — |
| [SRC-1AE03B9EC3-L002367](../../agents/web_agent.py#L2367) | 2367 | `"            page_text = _clean_text(bounded_text, MAX_PAGE_TEXT_CHARS)"` | — |
| [SRC-1AE03B9EC3-L002368](../../agents/web_agent.py#L2368) | 2368 | `"            status = ("` | — |
| [SRC-1AE03B9EC3-L002369](../../agents/web_agent.py#L2369) | 2369 | `"                \"empty_content\" if not page_text"` | — |
| [SRC-1AE03B9EC3-L002370](../../agents/web_agent.py#L2370) | 2370 | `"                else \"partial_extraction\" if bytes_truncated or text_truncated"` | — |
| [SRC-1AE03B9EC3-L002371](../../agents/web_agent.py#L2371) | 2371 | `"                else \"content_extracted\""` | — |
| [SRC-1AE03B9EC3-L002372](../../agents/web_agent.py#L2372) | 2372 | `"            )"` | — |
| [SRC-1AE03B9EC3-L002373](../../agents/web_agent.py#L2373) | 2373 | `"            return result(\"\", page_text, status)"` | — |
| [SRC-1AE03B9EC3-L002374](../../agents/web_agent.py#L2374) | 2374 | `""` | — |
| [SRC-1AE03B9EC3-L002375](../../agents/web_agent.py#L2375) | 2375 | `"        soup = BeautifulSoup(html, \"html.parser\")"` | — |
| [SRC-1AE03B9EC3-L002376](../../agents/web_agent.py#L2376) | 2376 | `"        title = _clean_text(soup.title.get_text(\" \", strip=True), 300) if soup.title else \"\""` | — |
| [SRC-1AE03B9EC3-L002377](../../agents/web_agent.py#L2377) | 2377 | `"        for element in soup(["` | — |
| [SRC-1AE03B9EC3-L002378](../../agents/web_agent.py#L2378) | 2378 | `"            \"script\", \"style\", \"nav\", \"footer\", \"header\", \"noscript\","` | — |
| [SRC-1AE03B9EC3-L002379](../../agents/web_agent.py#L2379) | 2379 | `"            \"svg\", \"form\", \"iframe\", \"template\""` | — |
| [SRC-1AE03B9EC3-L002380](../../agents/web_agent.py#L2380) | 2380 | `"        ]):"` | — |
| [SRC-1AE03B9EC3-L002381](../../agents/web_agent.py#L2381) | 2381 | `"            element.decompose()"` | — |
| [SRC-1AE03B9EC3-L002382](../../agents/web_agent.py#L2382) | 2382 | `"        main = soup.find(\"main\") or soup.find(\"article\") or soup.body or soup"` | — |
| [SRC-1AE03B9EC3-L002383](../../agents/web_agent.py#L2383) | 2383 | `"        bounded_text = _clean_text(main.get_text(\" \", strip=True), MAX_PAGE_TEXT_CHARS + 1)"` | — |
| [SRC-1AE03B9EC3-L002384](../../agents/web_agent.py#L2384) | 2384 | `"        text_truncated = len(bounded_text) > MAX_PAGE_TEXT_CHARS"` | — |
| [SRC-1AE03B9EC3-L002385](../../agents/web_agent.py#L2385) | 2385 | `"        page_text = _clean_text(bounded_text, MAX_PAGE_TEXT_CHARS)"` | — |
| [SRC-1AE03B9EC3-L002386](../../agents/web_agent.py#L2386) | 2386 | `"        status = ("` | — |
| [SRC-1AE03B9EC3-L002387](../../agents/web_agent.py#L2387) | 2387 | `"            \"no_text_extracted\" if not page_text"` | — |
| [SRC-1AE03B9EC3-L002388](../../agents/web_agent.py#L2388) | 2388 | `"            else \"partial_extraction\" if bytes_truncated or text_truncated"` | — |
| [SRC-1AE03B9EC3-L002389](../../agents/web_agent.py#L2389) | 2389 | `"            else \"content_extracted\""` | — |
| [SRC-1AE03B9EC3-L002390](../../agents/web_agent.py#L2390) | 2390 | `"        )"` | — |
| [SRC-1AE03B9EC3-L002391](../../agents/web_agent.py#L2391) | 2391 | `"        return result(title, page_text, status)"` | — |
| [SRC-1AE03B9EC3-L002392](../../agents/web_agent.py#L2392) | 2392 | `""` | — |
| [SRC-1AE03B9EC3-L002393](../../agents/web_agent.py#L2393) | 2393 | `"    def _collect_sources(self, query: str) -> tuple[list[dict[str, Any]], str \| None]:"` | — |
| [SRC-1AE03B9EC3-L002394](../../agents/web_agent.py#L2394) | 2394 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L002395](../../agents/web_agent.py#L2395) | 2395 | `"            sources = self._search_web(query)"` | — |
| [SRC-1AE03B9EC3-L002396](../../agents/web_agent.py#L2396) | 2396 | `"        except (RuntimeError, AgentDependencyError) as exc:"` | — |
| [SRC-1AE03B9EC3-L002397](../../agents/web_agent.py#L2397) | 2397 | `"            return [], str(exc)"` | — |
| [SRC-1AE03B9EC3-L002398](../../agents/web_agent.py#L2398) | 2398 | `"        for source in sources[:MAX_FETCHED_PAGES]:"` | — |
| [SRC-1AE03B9EC3-L002399](../../agents/web_agent.py#L2399) | 2399 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L002400](../../agents/web_agent.py#L2400) | 2400 | `"                title, page_text = self._fetch_page(source[\"url\"])"` | — |
| [SRC-1AE03B9EC3-L002401](../../agents/web_agent.py#L2401) | 2401 | `"            except (AgentDependencyError, RuntimeError):"` | — |
| [SRC-1AE03B9EC3-L002402](../../agents/web_agent.py#L2402) | 2402 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L002403](../../agents/web_agent.py#L2403) | 2403 | `"            if title:"` | — |
| [SRC-1AE03B9EC3-L002404](../../agents/web_agent.py#L2404) | 2404 | `"                source[\"title\"] = title"` | — |
| [SRC-1AE03B9EC3-L002405](../../agents/web_agent.py#L2405) | 2405 | `"            if page_text:"` | — |
| [SRC-1AE03B9EC3-L002406](../../agents/web_agent.py#L2406) | 2406 | `"                source[\"page_text\"] = page_text"` | — |
| [SRC-1AE03B9EC3-L002407](../../agents/web_agent.py#L2407) | 2407 | `"                source[\"page_fetched\"] = True"` | — |
| [SRC-1AE03B9EC3-L002408](../../agents/web_agent.py#L2408) | 2408 | `"                # Prefer extracted text over a thin search snippet."` | — |
| [SRC-1AE03B9EC3-L002409](../../agents/web_agent.py#L2409) | 2409 | `"                source[\"snippet\"] = page_text[:1800]"` | — |
| [SRC-1AE03B9EC3-L002410](../../agents/web_agent.py#L2410) | 2410 | `"        return sources, None"` | — |
| [SRC-1AE03B9EC3-L002411](../../agents/web_agent.py#L2411) | 2411 | `""` | — |
| [SRC-1AE03B9EC3-L002412](../../agents/web_agent.py#L2412) | 2412 | `"    def _collect_research("` | — |
| [SRC-1AE03B9EC3-L002413](../../agents/web_agent.py#L2413) | 2413 | `"        self, plan: dict[str, Any]"` | — |
| [SRC-1AE03B9EC3-L002414](../../agents/web_agent.py#L2414) | 2414 | `"    ) -> tuple[list[dict[str, Any]], list[str], dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L002415](../../agents/web_agent.py#L2415) | 2415 | `"        \"\"\"Run independent query searches concurrently, fuse evidence, then fetch top pages.\"\"\""` | — |
| [SRC-1AE03B9EC3-L002416](../../agents/web_agent.py#L2416) | 2416 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L002417](../../agents/web_agent.py#L2417) | 2417 | `"            query_limit = int(plan.get(\"query_limit\", MAX_PLAN_QUERIES))"` | — |
| [SRC-1AE03B9EC3-L002418](../../agents/web_agent.py#L2418) | 2418 | `"        except (TypeError, ValueError, OverflowError):"` | — |
| [SRC-1AE03B9EC3-L002419](../../agents/web_agent.py#L2419) | 2419 | `"            query_limit = MAX_PLAN_QUERIES"` | — |
| [SRC-1AE03B9EC3-L002420](../../agents/web_agent.py#L2420) | 2420 | `"        query_limit = max(1, min(query_limit, MAX_PLAN_QUERIES))"` | — |
| [SRC-1AE03B9EC3-L002421](../../agents/web_agent.py#L2421) | 2421 | `"        raw_queries = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L002422](../../agents/web_agent.py#L2422) | 2422 | `"            compact_search_query(query)"` | — |
| [SRC-1AE03B9EC3-L002423](../../agents/web_agent.py#L2423) | 2423 | `"            for query in plan.get(\"queries\", [])[:query_limit]"` | — |
| [SRC-1AE03B9EC3-L002424](../../agents/web_agent.py#L2424) | 2424 | `"            if isinstance(query, str) and query.strip()"` | — |
| [SRC-1AE03B9EC3-L002425](../../agents/web_agent.py#L2425) | 2425 | `"        ))"` | — |
| [SRC-1AE03B9EC3-L002426](../../agents/web_agent.py#L2426) | 2426 | `"        raw_queries = [query for query in raw_queries if query]"` | — |
| [SRC-1AE03B9EC3-L002427](../../agents/web_agent.py#L2427) | 2427 | `"        target_aspects = ["` | — |
| [SRC-1AE03B9EC3-L002428](../../agents/web_agent.py#L2428) | 2428 | `"            str(target).strip()[:120]"` | — |
| [SRC-1AE03B9EC3-L002429](../../agents/web_agent.py#L2429) | 2429 | `"            for target in (plan.get(\"coverage_targets\") or [])[:8]"` | — |
| [SRC-1AE03B9EC3-L002430](../../agents/web_agent.py#L2430) | 2430 | `"            if isinstance(target, str) and target.strip()"` | — |
| [SRC-1AE03B9EC3-L002431](../../agents/web_agent.py#L2431) | 2431 | `"        ]"` | — |
| [SRC-1AE03B9EC3-L002432](../../agents/web_agent.py#L2432) | 2432 | `"        # Reserve part of the existing query ceiling for evidence-gap repair."` | — |
| [SRC-1AE03B9EC3-L002433](../../agents/web_agent.py#L2433) | 2433 | `"        # This is a bounded retrieval loop, not an unbounded agent loop."` | — |
| [SRC-1AE03B9EC3-L002434](../../agents/web_agent.py#L2434) | 2434 | `"        repair_slot_limit = ("` | — |
| [SRC-1AE03B9EC3-L002435](../../agents/web_agent.py#L2435) | 2435 | `"            min(3, len(target_aspects), max(0, query_limit - 1))"` | — |
| [SRC-1AE03B9EC3-L002436](../../agents/web_agent.py#L2436) | 2436 | `"            if target_aspects else 0"` | — |
| [SRC-1AE03B9EC3-L002437](../../agents/web_agent.py#L2437) | 2437 | `"        )"` | — |
| [SRC-1AE03B9EC3-L002438](../../agents/web_agent.py#L2438) | 2438 | `"        initial_query_limit = max(1, query_limit - repair_slot_limit)"` | — |
| [SRC-1AE03B9EC3-L002439](../../agents/web_agent.py#L2439) | 2439 | `"        queries = raw_queries[:initial_query_limit]"` | — |
| [SRC-1AE03B9EC3-L002440](../../agents/web_agent.py#L2440) | 2440 | `"        warnings: list[str] = []"` | — |
| [SRC-1AE03B9EC3-L002441](../../agents/web_agent.py#L2441) | 2441 | `"        if not queries and not plan.get(\"direct_urls\"):"` | — |
| [SRC-1AE03B9EC3-L002442](../../agents/web_agent.py#L2442) | 2442 | `"            warnings.append(\"لم يُنشأ استعلام موضوعي قابل للبحث؛ لم تُستدعَ محركات البحث.\")"` | — |
| [SRC-1AE03B9EC3-L002443](../../agents/web_agent.py#L2443) | 2443 | `"        batches: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L002444](../../agents/web_agent.py#L2444) | 2444 | `"        query_counts: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L002445](../../agents/web_agent.py#L2445) | 2445 | `"        search_started_queries = 0"` | — |
| [SRC-1AE03B9EC3-L002446](../../agents/web_agent.py#L2446) | 2446 | `""` | — |
| [SRC-1AE03B9EC3-L002447](../../agents/web_agent.py#L2447) | 2447 | `"        if queries:"` | — |
| [SRC-1AE03B9EC3-L002448](../../agents/web_agent.py#L2448) | 2448 | `"            with ThreadPoolExecutor(max_workers=min(MAX_RESEARCH_WORKERS, len(queries))) as pool:"` | — |
| [SRC-1AE03B9EC3-L002449](../../agents/web_agent.py#L2449) | 2449 | `"                futures = {pool.submit(self._search_web, query): query for query in queries}"` | — |
| [SRC-1AE03B9EC3-L002450](../../agents/web_agent.py#L2450) | 2450 | `"                for future in as_completed(futures):"` | — |
| [SRC-1AE03B9EC3-L002451](../../agents/web_agent.py#L2451) | 2451 | `"                    query = futures[future]"` | — |
| [SRC-1AE03B9EC3-L002452](../../agents/web_agent.py#L2452) | 2452 | `"                    search_started_queries += 1"` | — |
| [SRC-1AE03B9EC3-L002453](../../agents/web_agent.py#L2453) | 2453 | `"                    try:"` | — |
| [SRC-1AE03B9EC3-L002454](../../agents/web_agent.py#L2454) | 2454 | `"                        results = future.result()"` | — |
| [SRC-1AE03B9EC3-L002455](../../agents/web_agent.py#L2455) | 2455 | `"                    except (RequestBudgetExceeded, RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L002456](../../agents/web_agent.py#L2456) | 2456 | `"                        warnings.append(f\"تعذر بحث الاستعلام «{query[:70]}»: {exc}\")"` | — |
| [SRC-1AE03B9EC3-L002457](../../agents/web_agent.py#L2457) | 2457 | `"                        query_counts.append({\"query\": query, \"results\": 0})"` | — |
| [SRC-1AE03B9EC3-L002458](../../agents/web_agent.py#L2458) | 2458 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L002459](../../agents/web_agent.py#L2459) | 2459 | `"                    query_counts.append({\"query\": query, \"results\": len(results)})"` | — |
| [SRC-1AE03B9EC3-L002460](../../agents/web_agent.py#L2460) | 2460 | `"                    grouped: dict[str, list[dict[str, Any]]] = {}"` | — |
| [SRC-1AE03B9EC3-L002461](../../agents/web_agent.py#L2461) | 2461 | `"                    for source in results:"` | — |
| [SRC-1AE03B9EC3-L002462](../../agents/web_agent.py#L2462) | 2462 | `"                        provider = str(source.get(\"provider\") or \"web_search\")"` | — |
| [SRC-1AE03B9EC3-L002463](../../agents/web_agent.py#L2463) | 2463 | `"                        grouped.setdefault(provider, []).append(source)"` | — |
| [SRC-1AE03B9EC3-L002464](../../agents/web_agent.py#L2464) | 2464 | `"                    for provider, items in grouped.items():"` | — |
| [SRC-1AE03B9EC3-L002465](../../agents/web_agent.py#L2465) | 2465 | `"                        items.sort(key=lambda item: int(item.get(\"provider_rank\", 999)))"` | — |
| [SRC-1AE03B9EC3-L002466](../../agents/web_agent.py#L2466) | 2466 | `"                        batches.append({\"query\": query, \"provider\": provider, \"results\": items})"` | — |
| [SRC-1AE03B9EC3-L002467](../../agents/web_agent.py#L2467) | 2467 | `""` | — |
| [SRC-1AE03B9EC3-L002468](../../agents/web_agent.py#L2468) | 2468 | `"        # Evidence-gap iteration: deep tasks get up to three targeted follow-up searches"` | — |
| [SRC-1AE03B9EC3-L002469](../../agents/web_agent.py#L2469) | 2469 | `"        # when initial coverage is thin. This uses observed source/domain/provider coverage,"` | — |
| [SRC-1AE03B9EC3-L002470](../../agents/web_agent.py#L2470) | 2470 | `"        # not the language model's subjective claim that it has enough evidence."` | — |
| [SRC-1AE03B9EC3-L002471](../../agents/web_agent.py#L2471) | 2471 | `"        preliminary = fuse_ranked_results(batches, limit=MAX_SEARCH_RESULTS)"` | — |
| [SRC-1AE03B9EC3-L002472](../../agents/web_agent.py#L2472) | 2472 | `"        preliminary_domains = {"` | — |
| [SRC-1AE03B9EC3-L002473](../../agents/web_agent.py#L2473) | 2473 | `"            registrable_domain(item.get(\"domain\") or urllib.parse.urlparse(item.get(\"url\", \"\")).hostname)"` | — |
| [SRC-1AE03B9EC3-L002474](../../agents/web_agent.py#L2474) | 2474 | `"            for item in preliminary"` | — |
| [SRC-1AE03B9EC3-L002475](../../agents/web_agent.py#L2475) | 2475 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002476](../../agents/web_agent.py#L2476) | 2476 | `"        preliminary_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L002477](../../agents/web_agent.py#L2477) | 2477 | `"        preliminary_providers = {"` | — |
| [SRC-1AE03B9EC3-L002478](../../agents/web_agent.py#L2478) | 2478 | `"            provider for item in preliminary for provider in item.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L002479](../../agents/web_agent.py#L2479) | 2479 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002480](../../agents/web_agent.py#L2480) | 2480 | `"        needs_expansion = ("` | — |
| [SRC-1AE03B9EC3-L002481](../../agents/web_agent.py#L2481) | 2481 | `"            plan.get(\"depth\") == \"deep\""` | — |
| [SRC-1AE03B9EC3-L002482](../../agents/web_agent.py#L2482) | 2482 | `"            and (len(preliminary) < 8 or len(preliminary_domains) < 5 or len(preliminary_providers) < 2)"` | — |
| [SRC-1AE03B9EC3-L002483](../../agents/web_agent.py#L2483) | 2483 | `"        )"` | — |
| [SRC-1AE03B9EC3-L002484](../../agents/web_agent.py#L2484) | 2484 | `"        preliminary_ledger = build_evidence_ledger(target_aspects, preliminary)"` | — |
| [SRC-1AE03B9EC3-L002485](../../agents/web_agent.py#L2485) | 2485 | `"        missing_aspects = list(preliminary_ledger.get(\"missing\") or [])"` | — |
| [SRC-1AE03B9EC3-L002486](../../agents/web_agent.py#L2486) | 2486 | `"        expansion_queries: list[str] = []"` | — |
| [SRC-1AE03B9EC3-L002487](../../agents/web_agent.py#L2487) | 2487 | `"        if (missing_aspects or needs_expansion) and len(queries) < query_limit and queries:"` | — |
| [SRC-1AE03B9EC3-L002488](../../agents/web_agent.py#L2488) | 2488 | `"            base_query = (queries[0] if queries else \"\")"` | — |
| [SRC-1AE03B9EC3-L002489](../../agents/web_agent.py#L2489) | 2489 | `"            remaining_slots = max(0, query_limit - len(queries))"` | — |
| [SRC-1AE03B9EC3-L002490](../../agents/web_agent.py#L2490) | 2490 | `"            aspect_queries = repair_queries_for_missing_aspects("` | — |
| [SRC-1AE03B9EC3-L002491](../../agents/web_agent.py#L2491) | 2491 | `"                base_query,"` | — |
| [SRC-1AE03B9EC3-L002492](../../agents/web_agent.py#L2492) | 2492 | `"                missing_aspects,"` | — |
| [SRC-1AE03B9EC3-L002493](../../agents/web_agent.py#L2493) | 2493 | `"                limit=min(repair_slot_limit, remaining_slots),"` | — |
| [SRC-1AE03B9EC3-L002494](../../agents/web_agent.py#L2494) | 2494 | `"                compact_fn=compact_search_query,"` | — |
| [SRC-1AE03B9EC3-L002495](../../agents/web_agent.py#L2495) | 2495 | `"            )"` | — |
| [SRC-1AE03B9EC3-L002496](../../agents/web_agent.py#L2496) | 2496 | `"            candidates = list(aspect_queries)"` | — |
| [SRC-1AE03B9EC3-L002497](../../agents/web_agent.py#L2497) | 2497 | `"            if needs_expansion:"` | — |
| [SRC-1AE03B9EC3-L002498](../../agents/web_agent.py#L2498) | 2498 | `"                candidates.extend(["` | — |
| [SRC-1AE03B9EC3-L002499](../../agents/web_agent.py#L2499) | 2499 | `"                    f\"{base_query} official sources data reports\","` | — |
| [SRC-1AE03B9EC3-L002500](../../agents/web_agent.py#L2500) | 2500 | `"                    f\"{base_query} limitations risks criticism alternatives\","` | — |
| [SRC-1AE03B9EC3-L002501](../../agents/web_agent.py#L2501) | 2501 | `"                    f\"{base_query} recent developments case studies analysis\","` | — |
| [SRC-1AE03B9EC3-L002502](../../agents/web_agent.py#L2502) | 2502 | `"                ])"` | — |
| [SRC-1AE03B9EC3-L002503](../../agents/web_agent.py#L2503) | 2503 | `"            existing = {item.casefold() for item in queries}"` | — |
| [SRC-1AE03B9EC3-L002504](../../agents/web_agent.py#L2504) | 2504 | `"            expansion_queries = []"` | — |
| [SRC-1AE03B9EC3-L002505](../../agents/web_agent.py#L2505) | 2505 | `"            seen_expansions = set(existing)"` | — |
| [SRC-1AE03B9EC3-L002506](../../agents/web_agent.py#L2506) | 2506 | `"            for candidate in candidates:"` | — |
| [SRC-1AE03B9EC3-L002507](../../agents/web_agent.py#L2507) | 2507 | `"                compacted = compact_search_query(candidate)"` | — |
| [SRC-1AE03B9EC3-L002508](../../agents/web_agent.py#L2508) | 2508 | `"                key = compacted.casefold()"` | — |
| [SRC-1AE03B9EC3-L002509](../../agents/web_agent.py#L2509) | 2509 | `"                if compacted and key not in seen_expansions:"` | — |
| [SRC-1AE03B9EC3-L002510](../../agents/web_agent.py#L2510) | 2510 | `"                    expansion_queries.append(compacted)"` | — |
| [SRC-1AE03B9EC3-L002511](../../agents/web_agent.py#L2511) | 2511 | `"                    seen_expansions.add(key)"` | — |
| [SRC-1AE03B9EC3-L002512](../../agents/web_agent.py#L2512) | 2512 | `"                if len(expansion_queries) >= remaining_slots:"` | — |
| [SRC-1AE03B9EC3-L002513](../../agents/web_agent.py#L2513) | 2513 | `"                    break"` | — |
| [SRC-1AE03B9EC3-L002514](../../agents/web_agent.py#L2514) | 2514 | `"            if expansion_queries:"` | — |
| [SRC-1AE03B9EC3-L002515](../../agents/web_agent.py#L2515) | 2515 | `"                with ThreadPoolExecutor("` | — |
| [SRC-1AE03B9EC3-L002516](../../agents/web_agent.py#L2516) | 2516 | `"                    max_workers=min(MAX_RESEARCH_WORKERS, len(expansion_queries))"` | — |
| [SRC-1AE03B9EC3-L002517](../../agents/web_agent.py#L2517) | 2517 | `"                ) as pool:"` | — |
| [SRC-1AE03B9EC3-L002518](../../agents/web_agent.py#L2518) | 2518 | `"                    futures = {"` | — |
| [SRC-1AE03B9EC3-L002519](../../agents/web_agent.py#L2519) | 2519 | `"                        pool.submit(self._search_web, query): query"` | — |
| [SRC-1AE03B9EC3-L002520](../../agents/web_agent.py#L2520) | 2520 | `"                        for query in expansion_queries"` | — |
| [SRC-1AE03B9EC3-L002521](../../agents/web_agent.py#L2521) | 2521 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L002522](../../agents/web_agent.py#L2522) | 2522 | `"                    for future in as_completed(futures):"` | — |
| [SRC-1AE03B9EC3-L002523](../../agents/web_agent.py#L2523) | 2523 | `"                        query = futures[future]"` | — |
| [SRC-1AE03B9EC3-L002524](../../agents/web_agent.py#L2524) | 2524 | `"                        search_started_queries += 1"` | — |
| [SRC-1AE03B9EC3-L002525](../../agents/web_agent.py#L2525) | 2525 | `"                        try:"` | — |
| [SRC-1AE03B9EC3-L002526](../../agents/web_agent.py#L2526) | 2526 | `"                            results = future.result()"` | — |
| [SRC-1AE03B9EC3-L002527](../../agents/web_agent.py#L2527) | 2527 | `"                        except (RequestBudgetExceeded, RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L002528](../../agents/web_agent.py#L2528) | 2528 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L002529](../../agents/web_agent.py#L2529) | 2529 | `"                                f\"تعذر بحث زاوية إضافية «{query[:70]}»: {exc}\""` | — |
| [SRC-1AE03B9EC3-L002530](../../agents/web_agent.py#L2530) | 2530 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L002531](../../agents/web_agent.py#L2531) | 2531 | `"                            query_counts.append({\"query\": query, \"results\": 0})"` | — |
| [SRC-1AE03B9EC3-L002532](../../agents/web_agent.py#L2532) | 2532 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002533](../../agents/web_agent.py#L2533) | 2533 | `"                        query_counts.append({\"query\": query, \"results\": len(results)})"` | — |
| [SRC-1AE03B9EC3-L002534](../../agents/web_agent.py#L2534) | 2534 | `"                        grouped: dict[str, list[dict[str, Any]]] = {}"` | — |
| [SRC-1AE03B9EC3-L002535](../../agents/web_agent.py#L2535) | 2535 | `"                        for source in results:"` | — |
| [SRC-1AE03B9EC3-L002536](../../agents/web_agent.py#L2536) | 2536 | `"                            grouped.setdefault("` | — |
| [SRC-1AE03B9EC3-L002537](../../agents/web_agent.py#L2537) | 2537 | `"                                str(source.get(\"provider\") or \"web_search\"), []"` | — |
| [SRC-1AE03B9EC3-L002538](../../agents/web_agent.py#L2538) | 2538 | `"                            ).append(source)"` | — |
