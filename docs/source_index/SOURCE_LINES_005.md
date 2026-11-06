# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **005**
- سجلات الأسطر: **800**
- النطاق: SRC-C9CF9B54F8-L000786 إلى SRC-59CF4B7DE8-L000181
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-C9CF9B54F8 — [agents/omarai.py](../../agents/omarai.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-C9CF9B54F8-L000786](../../agents/omarai.py#L786) | 786 | `"                   (id, tenant_id, normalized_name, name, profile_json, created_at, updated_at)"` | — |
| [SRC-C9CF9B54F8-L000787](../../agents/omarai.py#L787) | 787 | `"                   VALUES (?, ?, ?, ?, ?, ?, ?)"` | — |
| [SRC-C9CF9B54F8-L000788](../../agents/omarai.py#L788) | 788 | `"                   ON CONFLICT(tenant_id, normalized_name)"` | — |
| [SRC-C9CF9B54F8-L000789](../../agents/omarai.py#L789) | 789 | `"                   DO UPDATE SET name=excluded.name,"` | — |
| [SRC-C9CF9B54F8-L000790](../../agents/omarai.py#L790) | 790 | `"                                 profile_json=excluded.profile_json,"` | — |
| [SRC-C9CF9B54F8-L000791](../../agents/omarai.py#L791) | 791 | `"                                 updated_at=excluded.updated_at\"\"\","` | — |
| [SRC-C9CF9B54F8-L000792](../../agents/omarai.py#L792) | 792 | `"                (profile_id, tenant, normalized_name, name, encoded, now, now),"` | — |
| [SRC-C9CF9B54F8-L000793](../../agents/omarai.py#L793) | 793 | `"            )"` | — |
| [SRC-C9CF9B54F8-L000794](../../agents/omarai.py#L794) | 794 | `"            row = db.execute("` | — |
| [SRC-C9CF9B54F8-L000795](../../agents/omarai.py#L795) | 795 | `"                \"\"\"SELECT id, name, profile_json, created_at, updated_at"` | — |
| [SRC-C9CF9B54F8-L000796](../../agents/omarai.py#L796) | 796 | `"                   FROM product_profiles"` | — |
| [SRC-C9CF9B54F8-L000797](../../agents/omarai.py#L797) | 797 | `"                   WHERE tenant_id=? AND normalized_name=?\"\"\","` | — |
| [SRC-C9CF9B54F8-L000798](../../agents/omarai.py#L798) | 798 | `"                (tenant, normalized_name),"` | — |
| [SRC-C9CF9B54F8-L000799](../../agents/omarai.py#L799) | 799 | `"            ).fetchone()"` | — |
| [SRC-C9CF9B54F8-L000800](../../agents/omarai.py#L800) | 800 | `"        return self._product_profile_row(row)"` | — |
| [SRC-C9CF9B54F8-L000801](../../agents/omarai.py#L801) | 801 | `""` | — |
| [SRC-C9CF9B54F8-L000802](../../agents/omarai.py#L802) | 802 | `"    def list_product_profiles(self, *, tenant_id: str):"` | — |
| [SRC-C9CF9B54F8-L000803](../../agents/omarai.py#L803) | 803 | `"        tenant = self._tenant(tenant_id)"` | — |
| [SRC-C9CF9B54F8-L000804](../../agents/omarai.py#L804) | 804 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000805](../../agents/omarai.py#L805) | 805 | `"            rows = db.execute("` | — |
| [SRC-C9CF9B54F8-L000806](../../agents/omarai.py#L806) | 806 | `"                \"\"\"SELECT id, name, profile_json, created_at, updated_at"` | — |
| [SRC-C9CF9B54F8-L000807](../../agents/omarai.py#L807) | 807 | `"                   FROM product_profiles WHERE tenant_id=?"` | — |
| [SRC-C9CF9B54F8-L000808](../../agents/omarai.py#L808) | 808 | `"                   ORDER BY updated_at DESC, id LIMIT 100\"\"\","` | — |
| [SRC-C9CF9B54F8-L000809](../../agents/omarai.py#L809) | 809 | `"                (tenant,),"` | — |
| [SRC-C9CF9B54F8-L000810](../../agents/omarai.py#L810) | 810 | `"            ).fetchall()"` | — |
| [SRC-C9CF9B54F8-L000811](../../agents/omarai.py#L811) | 811 | `"        return [self._product_profile_row(row) for row in rows]"` | — |
| [SRC-C9CF9B54F8-L000812](../../agents/omarai.py#L812) | 812 | `""` | — |
| [SRC-C9CF9B54F8-L000813](../../agents/omarai.py#L813) | 813 | `"    def get_product_profile(self, profile_id: str, *, tenant_id: str):"` | — |
| [SRC-C9CF9B54F8-L000814](../../agents/omarai.py#L814) | 814 | `"        if not isinstance(profile_id, str) or not profile_id.strip():"` | — |
| [SRC-C9CF9B54F8-L000815](../../agents/omarai.py#L815) | 815 | `"            return None"` | — |
| [SRC-C9CF9B54F8-L000816](../../agents/omarai.py#L816) | 816 | `"        tenant = self._tenant(tenant_id)"` | — |
| [SRC-C9CF9B54F8-L000817](../../agents/omarai.py#L817) | 817 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000818](../../agents/omarai.py#L818) | 818 | `"            row = db.execute("` | — |
| [SRC-C9CF9B54F8-L000819](../../agents/omarai.py#L819) | 819 | `"                \"\"\"SELECT id, name, profile_json, created_at, updated_at"` | — |
| [SRC-C9CF9B54F8-L000820](../../agents/omarai.py#L820) | 820 | `"                   FROM product_profiles WHERE id=? AND tenant_id=?\"\"\","` | — |
| [SRC-C9CF9B54F8-L000821](../../agents/omarai.py#L821) | 821 | `"                (profile_id.strip(), tenant),"` | — |
| [SRC-C9CF9B54F8-L000822](../../agents/omarai.py#L822) | 822 | `"            ).fetchone()"` | — |
| [SRC-C9CF9B54F8-L000823](../../agents/omarai.py#L823) | 823 | `"        return self._product_profile_row(row)"` | — |
| [SRC-C9CF9B54F8-L000824](../../agents/omarai.py#L824) | 824 | `""` | — |
| [SRC-C9CF9B54F8-L000825](../../agents/omarai.py#L825) | 825 | `"    @staticmethod"` | — |
| [SRC-C9CF9B54F8-L000826](../../agents/omarai.py#L826) | 826 | `"    def _safe_discovery_source(source: dict):"` | — |
| [SRC-C9CF9B54F8-L000827](../../agents/omarai.py#L827) | 827 | `"        from urllib.parse import urlparse"` | — |
| [SRC-C9CF9B54F8-L000828](../../agents/omarai.py#L828) | 828 | `""` | — |
| [SRC-C9CF9B54F8-L000829](../../agents/omarai.py#L829) | 829 | `"        title = str(source.get(\"title\") or \"\")[:300].strip()"` | — |
| [SRC-C9CF9B54F8-L000830](../../agents/omarai.py#L830) | 830 | `"        snippet = str(source.get(\"snippet\") or \"\")[:1600].strip()"` | — |
| [SRC-C9CF9B54F8-L000831](../../agents/omarai.py#L831) | 831 | `"        source_url = validate_url(source.get(\"url\", \"\"))"` | — |
| [SRC-C9CF9B54F8-L000832](../../agents/omarai.py#L832) | 832 | `"        parsed = urlparse(source_url)"` | — |
| [SRC-C9CF9B54F8-L000833](../../agents/omarai.py#L833) | 833 | `"        hostname = (parsed.hostname or \"\").lower().rstrip(\".\")"` | — |
| [SRC-C9CF9B54F8-L000834](../../agents/omarai.py#L834) | 834 | `"        if hostname == \"localhost\" or hostname.endswith((\".localhost\", \".local\")):"` | — |
| [SRC-C9CF9B54F8-L000835](../../agents/omarai.py#L835) | 835 | `"            raise ValueError(\"discovery source URL is not public\")"` | — |
| [SRC-C9CF9B54F8-L000836](../../agents/omarai.py#L836) | 836 | `"        try:"` | — |
| [SRC-C9CF9B54F8-L000837](../../agents/omarai.py#L837) | 837 | `"            address = ipaddress.ip_address(hostname)"` | — |
| [SRC-C9CF9B54F8-L000838](../../agents/omarai.py#L838) | 838 | `"        except ValueError:"` | — |
| [SRC-C9CF9B54F8-L000839](../../agents/omarai.py#L839) | 839 | `"            address = None"` | — |
| [SRC-C9CF9B54F8-L000840](../../agents/omarai.py#L840) | 840 | `"        if address is not None and not address.is_global:"` | — |
| [SRC-C9CF9B54F8-L000841](../../agents/omarai.py#L841) | 841 | `"            raise ValueError(\"discovery source URL is not public\")"` | — |
| [SRC-C9CF9B54F8-L000842](../../agents/omarai.py#L842) | 842 | `"        evidence = source.get(\"lead_intent_evidence\")"` | — |
| [SRC-C9CF9B54F8-L000843](../../agents/omarai.py#L843) | 843 | `"        safe_evidence = None"` | — |
| [SRC-C9CF9B54F8-L000844](../../agents/omarai.py#L844) | 844 | `"        if isinstance(evidence, dict):"` | — |
| [SRC-C9CF9B54F8-L000845](../../agents/omarai.py#L845) | 845 | `"            safe_evidence = {"` | — |
| [SRC-C9CF9B54F8-L000846](../../agents/omarai.py#L846) | 846 | `"                \"phrase\": str(evidence.get(\"phrase\") or \"\")[:500],"` | — |
| [SRC-C9CF9B54F8-L000847](../../agents/omarai.py#L847) | 847 | `"                \"basis\": str(evidence.get(\"basis\") or \"\")[:40],"` | — |
| [SRC-C9CF9B54F8-L000848](../../agents/omarai.py#L848) | 848 | `"                \"signal_type\": str(evidence.get(\"signal_type\") or \"\")[:80],"` | — |
| [SRC-C9CF9B54F8-L000849](../../agents/omarai.py#L849) | 849 | `"                \"product_fit\": str(evidence.get(\"product_fit\") or \"unassessed\")[:40],"` | — |
| [SRC-C9CF9B54F8-L000850](../../agents/omarai.py#L850) | 850 | `"            }"` | — |
| [SRC-C9CF9B54F8-L000851](../../agents/omarai.py#L851) | 851 | `"        providers = source.get(\"providers\")"` | — |
| [SRC-C9CF9B54F8-L000852](../../agents/omarai.py#L852) | 852 | `"        queries = source.get(\"queries\")"` | — |
| [SRC-C9CF9B54F8-L000853](../../agents/omarai.py#L853) | 853 | `"        return {"` | — |
| [SRC-C9CF9B54F8-L000854](../../agents/omarai.py#L854) | 854 | `"            \"title\": title,"` | — |
| [SRC-C9CF9B54F8-L000855](../../agents/omarai.py#L855) | 855 | `"            \"url\": source_url,"` | — |
| [SRC-C9CF9B54F8-L000856](../../agents/omarai.py#L856) | 856 | `"            \"snippet\": snippet,"` | — |
| [SRC-C9CF9B54F8-L000857](../../agents/omarai.py#L857) | 857 | `"            \"platform\": str(source.get(\"platform\") or \"web\")[:80],"` | — |
| [SRC-C9CF9B54F8-L000858](../../agents/omarai.py#L858) | 858 | `"            \"domain\": str(source.get(\"domain\") or \"\")[:253],"` | — |
| [SRC-C9CF9B54F8-L000859](../../agents/omarai.py#L859) | 859 | `"            \"published_at\": ("` | — |
| [SRC-C9CF9B54F8-L000860](../../agents/omarai.py#L860) | 860 | `"                str(source.get(\"published_at\"))[:120]"` | — |
| [SRC-C9CF9B54F8-L000861](../../agents/omarai.py#L861) | 861 | `"                if source.get(\"published_at\") is not None else None"` | — |
| [SRC-C9CF9B54F8-L000862](../../agents/omarai.py#L862) | 862 | `"            ),"` | — |
| [SRC-C9CF9B54F8-L000863](../../agents/omarai.py#L863) | 863 | `"            \"page_fetched\": source.get(\"page_fetched\") is True,"` | — |
| [SRC-C9CF9B54F8-L000864](../../agents/omarai.py#L864) | 864 | `"            \"readable_page_text_available\": source.get(\"readable_page_text_available\") is True,"` | — |
| [SRC-C9CF9B54F8-L000865](../../agents/omarai.py#L865) | 865 | `"            \"providers\": ["` | — |
| [SRC-C9CF9B54F8-L000866](../../agents/omarai.py#L866) | 866 | `"                str(value)[:80] for value in providers[:8] if isinstance(value, str)"` | — |
| [SRC-C9CF9B54F8-L000867](../../agents/omarai.py#L867) | 867 | `"            ] if isinstance(providers, list) else [],"` | — |
| [SRC-C9CF9B54F8-L000868](../../agents/omarai.py#L868) | 868 | `"            \"queries\": ["` | — |
| [SRC-C9CF9B54F8-L000869](../../agents/omarai.py#L869) | 869 | `"                str(value)[:500] for value in queries[:8] if isinstance(value, str)"` | — |
| [SRC-C9CF9B54F8-L000870](../../agents/omarai.py#L870) | 870 | `"            ] if isinstance(queries, list) else [],"` | — |
| [SRC-C9CF9B54F8-L000871](../../agents/omarai.py#L871) | 871 | `"            \"lead_qualification\": ("` | — |
| [SRC-C9CF9B54F8-L000872](../../agents/omarai.py#L872) | 872 | `"                \"public_demand_signal\""` | — |
| [SRC-C9CF9B54F8-L000873](../../agents/omarai.py#L873) | 873 | `"                if source.get(\"lead_qualification\") == \"public_demand_signal\""` | — |
| [SRC-C9CF9B54F8-L000874](../../agents/omarai.py#L874) | 874 | `"                else \"related_result_not_lead\""` | — |
| [SRC-C9CF9B54F8-L000875](../../agents/omarai.py#L875) | 875 | `"            ),"` | — |
| [SRC-C9CF9B54F8-L000876](../../agents/omarai.py#L876) | 876 | `"            \"lead_intent_evidence\": safe_evidence,"` | — |
| [SRC-C9CF9B54F8-L000877](../../agents/omarai.py#L877) | 877 | `"        }"` | — |
| [SRC-C9CF9B54F8-L000878](../../agents/omarai.py#L878) | 878 | `""` | — |
| [SRC-C9CF9B54F8-L000879](../../agents/omarai.py#L879) | 879 | `"    def save_discovery_run(self, profile_id: str, run: dict, *, tenant_id: str):"` | — |
| [SRC-C9CF9B54F8-L000880](../../agents/omarai.py#L880) | 880 | `"        if not isinstance(run, dict):"` | — |
| [SRC-C9CF9B54F8-L000881](../../agents/omarai.py#L881) | 881 | `"            raise TypeError(\"discovery run must be an object\")"` | — |
| [SRC-C9CF9B54F8-L000882](../../agents/omarai.py#L882) | 882 | `"        tenant = self._tenant(tenant_id)"` | — |
| [SRC-C9CF9B54F8-L000883](../../agents/omarai.py#L883) | 883 | `"        profile = self.get_product_profile(profile_id, tenant_id=tenant)"` | — |
| [SRC-C9CF9B54F8-L000884](../../agents/omarai.py#L884) | 884 | `"        if profile is None:"` | — |
| [SRC-C9CF9B54F8-L000885](../../agents/omarai.py#L885) | 885 | `"            return None"` | — |
| [SRC-C9CF9B54F8-L000886](../../agents/omarai.py#L886) | 886 | `"        raw_sources = run.get(\"sources\")"` | — |
| [SRC-C9CF9B54F8-L000887](../../agents/omarai.py#L887) | 887 | `"        raw_sources = raw_sources if isinstance(raw_sources, list) else []"` | — |
| [SRC-C9CF9B54F8-L000888](../../agents/omarai.py#L888) | 888 | `"        sources = ["` | — |
| [SRC-C9CF9B54F8-L000889](../../agents/omarai.py#L889) | 889 | `"            self._safe_discovery_source(item)"` | — |
| [SRC-C9CF9B54F8-L000890](../../agents/omarai.py#L890) | 890 | `"            for item in raw_sources[:30] if isinstance(item, dict)"` | — |
| [SRC-C9CF9B54F8-L000891](../../agents/omarai.py#L891) | 891 | `"        ]"` | — |
| [SRC-C9CF9B54F8-L000892](../../agents/omarai.py#L892) | 892 | `"        raw_queries = run.get(\"search_queries\")"` | — |
| [SRC-C9CF9B54F8-L000893](../../agents/omarai.py#L893) | 893 | `"        if not isinstance(raw_queries, list):"` | — |
| [SRC-C9CF9B54F8-L000894](../../agents/omarai.py#L894) | 894 | `"            raw_queries = []"` | — |
| [SRC-C9CF9B54F8-L000895](../../agents/omarai.py#L895) | 895 | `"        queries = [str(item)[:500] for item in raw_queries[:8] if isinstance(item, str)]"` | — |
| [SRC-C9CF9B54F8-L000896](../../agents/omarai.py#L896) | 896 | `"        raw_report = run.get(\"search_report\")"` | — |
| [SRC-C9CF9B54F8-L000897](../../agents/omarai.py#L897) | 897 | `"        raw_report = raw_report if isinstance(raw_report, dict) else {}"` | — |
| [SRC-C9CF9B54F8-L000898](../../agents/omarai.py#L898) | 898 | `"        lead_report = raw_report.get(\"lead_generation\")"` | — |
| [SRC-C9CF9B54F8-L000899](../../agents/omarai.py#L899) | 899 | `"        report = {"` | — |
| [SRC-C9CF9B54F8-L000900](../../agents/omarai.py#L900) | 900 | `"            \"lead_generation\": lead_report if isinstance(lead_report, dict) else {},"` | — |
| [SRC-C9CF9B54F8-L000901](../../agents/omarai.py#L901) | 901 | `"            \"pipeline_completion_status\": str("` | — |
| [SRC-C9CF9B54F8-L000902](../../agents/omarai.py#L902) | 902 | `"                raw_report.get(\"pipeline_completion_status\")"` | — |
| [SRC-C9CF9B54F8-L000903](../../agents/omarai.py#L903) | 903 | `"                or run.get(\"pipeline_completion_status\")"` | — |
| [SRC-C9CF9B54F8-L000904](../../agents/omarai.py#L904) | 904 | `"                or \"unknown\""` | — |
| [SRC-C9CF9B54F8-L000905](../../agents/omarai.py#L905) | 905 | `"            )[:80],"` | — |
| [SRC-C9CF9B54F8-L000906](../../agents/omarai.py#L906) | 906 | `"            \"search_outcome\": str(raw_report.get(\"search_outcome\") or \"unknown\")[:80],"` | — |
| [SRC-C9CF9B54F8-L000907](../../agents/omarai.py#L907) | 907 | `"            \"search_attempted\": raw_report.get(\"search_attempted\"),"` | — |
| [SRC-C9CF9B54F8-L000908](../../agents/omarai.py#L908) | 908 | `"            \"used_web_search\": run.get(\"used_web_search\") is True,"` | — |
| [SRC-C9CF9B54F8-L000909](../../agents/omarai.py#L909) | 909 | `"            \"used_social_search\": run.get(\"used_social_search\") is True,"` | — |
| [SRC-C9CF9B54F8-L000910](../../agents/omarai.py#L910) | 910 | `"        }"` | — |
| [SRC-C9CF9B54F8-L000911](../../agents/omarai.py#L911) | 911 | `"        report_json = json.dumps(report, ensure_ascii=False, separators=(\",\", \":\"))"` | — |
| [SRC-C9CF9B54F8-L000912](../../agents/omarai.py#L912) | 912 | `"        queries_json = json.dumps(queries, ensure_ascii=False, separators=(\",\", \":\"))"` | — |
| [SRC-C9CF9B54F8-L000913](../../agents/omarai.py#L913) | 913 | `"        sources_json = json.dumps(sources, ensure_ascii=False, separators=(\",\", \":\"))"` | — |
| [SRC-C9CF9B54F8-L000914](../../agents/omarai.py#L914) | 914 | `"        if sum(map(len, (report_json, queries_json, sources_json))) > 120000:"` | — |
| [SRC-C9CF9B54F8-L000915](../../agents/omarai.py#L915) | 915 | `"            raise ValueError(\"discovery result exceeds the storage limit\")"` | — |
| [SRC-C9CF9B54F8-L000916](../../agents/omarai.py#L916) | 916 | `"        run_id = \"discovery_\" + uuid.uuid4().hex"` | — |
| [SRC-C9CF9B54F8-L000917](../../agents/omarai.py#L917) | 917 | `"        now = now_utc()"` | — |
| [SRC-C9CF9B54F8-L000918](../../agents/omarai.py#L918) | 918 | `"        answer = str(run.get(\"answer\") or \"\")[:5000]"` | — |
| [SRC-C9CF9B54F8-L000919](../../agents/omarai.py#L919) | 919 | `"        kind = str(run.get(\"kind\") or \"lead_discovery\")[:100]"` | — |
| [SRC-C9CF9B54F8-L000920](../../agents/omarai.py#L920) | 920 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000921](../../agents/omarai.py#L921) | 921 | `"            db.execute("` | — |
| [SRC-C9CF9B54F8-L000922](../../agents/omarai.py#L922) | 922 | `"                \"\"\"INSERT INTO discovery_runs"` | — |
| [SRC-C9CF9B54F8-L000923](../../agents/omarai.py#L923) | 923 | `"                   (id, tenant_id, profile_id, answer, kind, search_queries_json,"` | — |
| [SRC-C9CF9B54F8-L000924](../../agents/omarai.py#L924) | 924 | `"                    search_report_json, sources_json, created_at)"` | — |
| [SRC-C9CF9B54F8-L000925](../../agents/omarai.py#L925) | 925 | `"                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)\"\"\","` | — |
| [SRC-C9CF9B54F8-L000926](../../agents/omarai.py#L926) | 926 | `"                ("` | — |
| [SRC-C9CF9B54F8-L000927](../../agents/omarai.py#L927) | 927 | `"                    run_id, tenant, profile_id, answer, kind, queries_json,"` | — |
| [SRC-C9CF9B54F8-L000928](../../agents/omarai.py#L928) | 928 | `"                    report_json, sources_json, now,"` | — |
| [SRC-C9CF9B54F8-L000929](../../agents/omarai.py#L929) | 929 | `"                ),"` | — |
| [SRC-C9CF9B54F8-L000930](../../agents/omarai.py#L930) | 930 | `"            )"` | — |
| [SRC-C9CF9B54F8-L000931](../../agents/omarai.py#L931) | 931 | `"            row = db.execute("` | — |
| [SRC-C9CF9B54F8-L000932](../../agents/omarai.py#L932) | 932 | `"                \"\"\"SELECT r.id, r.tenant_id, r.profile_id, p.name AS profile_name,"` | — |
| [SRC-C9CF9B54F8-L000933](../../agents/omarai.py#L933) | 933 | `"                          r.answer, r.kind, r.search_queries_json, r.search_report_json,"` | — |
| [SRC-C9CF9B54F8-L000934](../../agents/omarai.py#L934) | 934 | `"                          r.sources_json, r.created_at"` | — |
| [SRC-C9CF9B54F8-L000935](../../agents/omarai.py#L935) | 935 | `"                   FROM discovery_runs r"` | — |
| [SRC-C9CF9B54F8-L000936](../../agents/omarai.py#L936) | 936 | `"                   JOIN product_profiles p"` | — |
| [SRC-C9CF9B54F8-L000937](../../agents/omarai.py#L937) | 937 | `"                     ON p.id=r.profile_id AND p.tenant_id=r.tenant_id"` | — |
| [SRC-C9CF9B54F8-L000938](../../agents/omarai.py#L938) | 938 | `"                   WHERE r.id=? AND r.tenant_id=?\"\"\","` | — |
| [SRC-C9CF9B54F8-L000939](../../agents/omarai.py#L939) | 939 | `"                (run_id, tenant),"` | — |
| [SRC-C9CF9B54F8-L000940](../../agents/omarai.py#L940) | 940 | `"            ).fetchone()"` | — |
| [SRC-C9CF9B54F8-L000941](../../agents/omarai.py#L941) | 941 | `"        return self._discovery_run_row(row)"` | — |
| [SRC-C9CF9B54F8-L000942](../../agents/omarai.py#L942) | 942 | `""` | — |
| [SRC-C9CF9B54F8-L000943](../../agents/omarai.py#L943) | 943 | `"    @staticmethod"` | — |
| [SRC-C9CF9B54F8-L000944](../../agents/omarai.py#L944) | 944 | `"    def _discovery_run_row(row):"` | — |
| [SRC-C9CF9B54F8-L000945](../../agents/omarai.py#L945) | 945 | `"        if row is None:"` | — |
| [SRC-C9CF9B54F8-L000946](../../agents/omarai.py#L946) | 946 | `"            return None"` | — |
| [SRC-C9CF9B54F8-L000947](../../agents/omarai.py#L947) | 947 | `"        item = dict(row)"` | — |
| [SRC-C9CF9B54F8-L000948](../../agents/omarai.py#L948) | 948 | `"        item[\"search_queries\"] = json.loads(item.pop(\"search_queries_json\"))"` | — |
| [SRC-C9CF9B54F8-L000949](../../agents/omarai.py#L949) | 949 | `"        item[\"search_report\"] = json.loads(item.pop(\"search_report_json\"))"` | — |
| [SRC-C9CF9B54F8-L000950](../../agents/omarai.py#L950) | 950 | `"        item[\"sources\"] = json.loads(item.pop(\"sources_json\"))"` | — |
| [SRC-C9CF9B54F8-L000951](../../agents/omarai.py#L951) | 951 | `"        return item"` | — |
| [SRC-C9CF9B54F8-L000952](../../agents/omarai.py#L952) | 952 | `""` | — |
| [SRC-C9CF9B54F8-L000953](../../agents/omarai.py#L953) | 953 | `"    def list_discovery_runs(self, *, tenant_id: str, limit: int = 50):"` | — |
| [SRC-C9CF9B54F8-L000954](../../agents/omarai.py#L954) | 954 | `"        tenant = self._tenant(tenant_id)"` | — |
| [SRC-C9CF9B54F8-L000955](../../agents/omarai.py#L955) | 955 | `"        limit = max(1, min(int(limit), 100))"` | — |
| [SRC-C9CF9B54F8-L000956](../../agents/omarai.py#L956) | 956 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000957](../../agents/omarai.py#L957) | 957 | `"            rows = db.execute("` | — |
| [SRC-C9CF9B54F8-L000958](../../agents/omarai.py#L958) | 958 | `"                \"\"\"SELECT r.id, r.tenant_id, r.profile_id, p.name AS profile_name,"` | — |
| [SRC-C9CF9B54F8-L000959](../../agents/omarai.py#L959) | 959 | `"                          r.answer, r.kind, r.search_queries_json, r.search_report_json,"` | — |
| [SRC-C9CF9B54F8-L000960](../../agents/omarai.py#L960) | 960 | `"                          r.sources_json, r.created_at"` | — |
| [SRC-C9CF9B54F8-L000961](../../agents/omarai.py#L961) | 961 | `"                   FROM discovery_runs r"` | — |
| [SRC-C9CF9B54F8-L000962](../../agents/omarai.py#L962) | 962 | `"                   JOIN product_profiles p"` | — |
| [SRC-C9CF9B54F8-L000963](../../agents/omarai.py#L963) | 963 | `"                     ON p.id=r.profile_id AND p.tenant_id=r.tenant_id"` | — |
| [SRC-C9CF9B54F8-L000964](../../agents/omarai.py#L964) | 964 | `"                   WHERE r.tenant_id=?"` | — |
| [SRC-C9CF9B54F8-L000965](../../agents/omarai.py#L965) | 965 | `"                   ORDER BY r.created_at DESC, r.id LIMIT ?\"\"\","` | — |
| [SRC-C9CF9B54F8-L000966](../../agents/omarai.py#L966) | 966 | `"                (tenant, limit),"` | — |
| [SRC-C9CF9B54F8-L000967](../../agents/omarai.py#L967) | 967 | `"            ).fetchall()"` | — |
| [SRC-C9CF9B54F8-L000968](../../agents/omarai.py#L968) | 968 | `"        results = []"` | — |
| [SRC-C9CF9B54F8-L000969](../../agents/omarai.py#L969) | 969 | `"        for row in rows:"` | — |
| [SRC-C9CF9B54F8-L000970](../../agents/omarai.py#L970) | 970 | `"            item = self._discovery_run_row(row)"` | — |
| [SRC-C9CF9B54F8-L000971](../../agents/omarai.py#L971) | 971 | `"            results.append({"` | — |
| [SRC-C9CF9B54F8-L000972](../../agents/omarai.py#L972) | 972 | `"                \"id\": item[\"id\"],"` | — |
| [SRC-C9CF9B54F8-L000973](../../agents/omarai.py#L973) | 973 | `"                \"profile_id\": item[\"profile_id\"],"` | — |
| [SRC-C9CF9B54F8-L000974](../../agents/omarai.py#L974) | 974 | `"                \"profile_name\": item[\"profile_name\"],"` | — |
| [SRC-C9CF9B54F8-L000975](../../agents/omarai.py#L975) | 975 | `"                \"answer\": item[\"answer\"],"` | — |
| [SRC-C9CF9B54F8-L000976](../../agents/omarai.py#L976) | 976 | `"                \"kind\": item[\"kind\"],"` | — |
| [SRC-C9CF9B54F8-L000977](../../agents/omarai.py#L977) | 977 | `"                \"created_at\": item[\"created_at\"],"` | — |
| [SRC-C9CF9B54F8-L000978](../../agents/omarai.py#L978) | 978 | `"                \"source_count\": len(item[\"sources\"]),"` | — |
| [SRC-C9CF9B54F8-L000979](../../agents/omarai.py#L979) | 979 | `"                \"qualified_signal_count\": sum("` | — |
| [SRC-C9CF9B54F8-L000980](../../agents/omarai.py#L980) | 980 | `"                    source.get(\"lead_qualification\") == \"public_demand_signal\""` | — |
| [SRC-C9CF9B54F8-L000981](../../agents/omarai.py#L981) | 981 | `"                    for source in item[\"sources\"]"` | — |
| [SRC-C9CF9B54F8-L000982](../../agents/omarai.py#L982) | 982 | `"                ),"` | — |
| [SRC-C9CF9B54F8-L000983](../../agents/omarai.py#L983) | 983 | `"                \"pipeline_completion_status\": item[\"search_report\"].get("` | — |
| [SRC-C9CF9B54F8-L000984](../../agents/omarai.py#L984) | 984 | `"                    \"pipeline_completion_status\", \"unknown\""` | — |
| [SRC-C9CF9B54F8-L000985](../../agents/omarai.py#L985) | 985 | `"                ),"` | — |
| [SRC-C9CF9B54F8-L000986](../../agents/omarai.py#L986) | 986 | `"            })"` | — |
| [SRC-C9CF9B54F8-L000987](../../agents/omarai.py#L987) | 987 | `"        return results"` | — |
| [SRC-C9CF9B54F8-L000988](../../agents/omarai.py#L988) | 988 | `""` | — |
| [SRC-C9CF9B54F8-L000989](../../agents/omarai.py#L989) | 989 | `"    def get_discovery_run(self, run_id: str, *, tenant_id: str):"` | — |
| [SRC-C9CF9B54F8-L000990](../../agents/omarai.py#L990) | 990 | `"        if not isinstance(run_id, str) or not run_id.strip():"` | — |
| [SRC-C9CF9B54F8-L000991](../../agents/omarai.py#L991) | 991 | `"            return None"` | — |
| [SRC-C9CF9B54F8-L000992](../../agents/omarai.py#L992) | 992 | `"        tenant = self._tenant(tenant_id)"` | — |
| [SRC-C9CF9B54F8-L000993](../../agents/omarai.py#L993) | 993 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000994](../../agents/omarai.py#L994) | 994 | `"            row = db.execute("` | — |
| [SRC-C9CF9B54F8-L000995](../../agents/omarai.py#L995) | 995 | `"                \"\"\"SELECT r.id, r.tenant_id, r.profile_id, p.name AS profile_name,"` | — |
| [SRC-C9CF9B54F8-L000996](../../agents/omarai.py#L996) | 996 | `"                          r.answer, r.kind, r.search_queries_json, r.search_report_json,"` | — |
| [SRC-C9CF9B54F8-L000997](../../agents/omarai.py#L997) | 997 | `"                          r.sources_json, r.created_at"` | — |
| [SRC-C9CF9B54F8-L000998](../../agents/omarai.py#L998) | 998 | `"                   FROM discovery_runs r"` | — |
| [SRC-C9CF9B54F8-L000999](../../agents/omarai.py#L999) | 999 | `"                   JOIN product_profiles p"` | — |
| [SRC-C9CF9B54F8-L001000](../../agents/omarai.py#L1000) | 1000 | `"                     ON p.id=r.profile_id AND p.tenant_id=r.tenant_id"` | — |
| [SRC-C9CF9B54F8-L001001](../../agents/omarai.py#L1001) | 1001 | `"                   WHERE r.id=? AND r.tenant_id=?\"\"\","` | — |
| [SRC-C9CF9B54F8-L001002](../../agents/omarai.py#L1002) | 1002 | `"                (run_id.strip(), tenant),"` | — |
| [SRC-C9CF9B54F8-L001003](../../agents/omarai.py#L1003) | 1003 | `"            ).fetchone()"` | — |
| [SRC-C9CF9B54F8-L001004](../../agents/omarai.py#L1004) | 1004 | `"        return self._discovery_run_row(row)"` | — |
| [SRC-C9CF9B54F8-L001005](../../agents/omarai.py#L1005) | 1005 | `""` | — |
| [SRC-C9CF9B54F8-L001006](../../agents/omarai.py#L1006) | 1006 | `"    def save_discovery_signal("` | — |
| [SRC-C9CF9B54F8-L001007](../../agents/omarai.py#L1007) | 1007 | `"        self, run_id: str, source_index: int, *, tenant_id: str"` | — |
| [SRC-C9CF9B54F8-L001008](../../agents/omarai.py#L1008) | 1008 | `"    ):"` | — |
| [SRC-C9CF9B54F8-L001009](../../agents/omarai.py#L1009) | 1009 | `"        if not isinstance(source_index, int) or isinstance(source_index, bool):"` | — |
| [SRC-C9CF9B54F8-L001010](../../agents/omarai.py#L1010) | 1010 | `"            return None"` | — |
| [SRC-C9CF9B54F8-L001011](../../agents/omarai.py#L1011) | 1011 | `"        run = self.get_discovery_run(run_id, tenant_id=tenant_id)"` | — |
| [SRC-C9CF9B54F8-L001012](../../agents/omarai.py#L1012) | 1012 | `"        if run is None or not 0 <= source_index < len(run[\"sources\"]):"` | — |
| [SRC-C9CF9B54F8-L001013](../../agents/omarai.py#L1013) | 1013 | `"            return None"` | — |
| [SRC-C9CF9B54F8-L001014](../../agents/omarai.py#L1014) | 1014 | `"        source = run[\"sources\"][source_index]"` | — |
| [SRC-C9CF9B54F8-L001015](../../agents/omarai.py#L1015) | 1015 | `"        if source.get(\"lead_qualification\") != \"public_demand_signal\":"` | — |
| [SRC-C9CF9B54F8-L001016](../../agents/omarai.py#L1016) | 1016 | `"            return None"` | — |
| [SRC-C9CF9B54F8-L001017](../../agents/omarai.py#L1017) | 1017 | `"        evidence = source.get(\"lead_intent_evidence\")"` | — |
| [SRC-C9CF9B54F8-L001018](../../agents/omarai.py#L1018) | 1018 | `"        if not isinstance(evidence, dict) or not str(evidence.get(\"phrase\") or \"\").strip():"` | — |
| [SRC-C9CF9B54F8-L001019](../../agents/omarai.py#L1019) | 1019 | `"            return None"` | — |
| [SRC-C9CF9B54F8-L001020](../../agents/omarai.py#L1020) | 1020 | `"        profile = self.get_product_profile(run[\"profile_id\"], tenant_id=tenant_id)"` | — |
| [SRC-C9CF9B54F8-L001021](../../agents/omarai.py#L1021) | 1021 | `"        if profile is None:"` | — |
| [SRC-C9CF9B54F8-L001022](../../agents/omarai.py#L1022) | 1022 | `"            return None"` | — |
| [SRC-C9CF9B54F8-L001023](../../agents/omarai.py#L1023) | 1023 | `"        product = profile[\"profile\"].get(\"product\", {})"` | — |
| [SRC-C9CF9B54F8-L001024](../../agents/omarai.py#L1024) | 1024 | `"        market = profile[\"profile\"].get(\"market\", {})"` | — |
| [SRC-C9CF9B54F8-L001025](../../agents/omarai.py#L1025) | 1025 | `"        product_terms = ["` | — |
| [SRC-C9CF9B54F8-L001026](../../agents/omarai.py#L1026) | 1026 | `"            str(item) for item in [product.get(\"name\"), *(product.get(\"aliases\") or [])]"` | — |
| [SRC-C9CF9B54F8-L001027](../../agents/omarai.py#L1027) | 1027 | `"            if isinstance(item, str) and item.strip()"` | — |
| [SRC-C9CF9B54F8-L001028](../../agents/omarai.py#L1028) | 1028 | `"        ]"` | — |
| [SRC-C9CF9B54F8-L001029](../../agents/omarai.py#L1029) | 1029 | `"        location_terms = ["` | — |
| [SRC-C9CF9B54F8-L001030](../../agents/omarai.py#L1030) | 1030 | `"            str(item) for item in (market.get(\"locations\") or [])"` | — |
| [SRC-C9CF9B54F8-L001031](../../agents/omarai.py#L1031) | 1031 | `"            if isinstance(item, str) and item.strip()"` | — |
| [SRC-C9CF9B54F8-L001032](../../agents/omarai.py#L1032) | 1032 | `"        ]"` | — |
| [SRC-C9CF9B54F8-L001033](../../agents/omarai.py#L1033) | 1033 | `"        source_text = str(source.get(\"snippet\") or source.get(\"title\") or \"\").strip()"` | — |
| [SRC-C9CF9B54F8-L001034](../../agents/omarai.py#L1034) | 1034 | `"        if not source_text:"` | — |
| [SRC-C9CF9B54F8-L001035](../../agents/omarai.py#L1035) | 1035 | `"            return None"` | — |
| [SRC-C9CF9B54F8-L001036](../../agents/omarai.py#L1036) | 1036 | `"        note = ("` | — |
| [SRC-C9CF9B54F8-L001037](../../agents/omarai.py#L1037) | 1037 | `"            \"Omarai public demand evidence \| \""` | — |
| [SRC-C9CF9B54F8-L001038](../../agents/omarai.py#L1038) | 1038 | `"            + \"phrase=\" + str(evidence.get(\"phrase\") or \"\")[:240]"` | — |
| [SRC-C9CF9B54F8-L001039](../../agents/omarai.py#L1039) | 1039 | `"            + \" \| basis=\" + str(evidence.get(\"basis\") or \"unknown\")[:40]"` | — |
| [SRC-C9CF9B54F8-L001040](../../agents/omarai.py#L1040) | 1040 | `"            + \" \| signal_type=\" + str(evidence.get(\"signal_type\") or \"unknown\")[:80]"` | — |
| [SRC-C9CF9B54F8-L001041](../../agents/omarai.py#L1041) | 1041 | `"            + \" \| profile=\" + str(profile.get(\"name\") or \"\")[:160]"` | — |
| [SRC-C9CF9B54F8-L001042](../../agents/omarai.py#L1042) | 1042 | `"            + \" \| run=\" + run[\"id\"]"` | — |
| [SRC-C9CF9B54F8-L001043](../../agents/omarai.py#L1043) | 1043 | `"        )"` | — |
| [SRC-C9CF9B54F8-L001044](../../agents/omarai.py#L1044) | 1044 | `"        return self.add("` | — |
| [SRC-C9CF9B54F8-L001045](../../agents/omarai.py#L1045) | 1045 | `"            source_text[:MAX_TEXT],"` | — |
| [SRC-C9CF9B54F8-L001046](../../agents/omarai.py#L1046) | 1046 | `"            source[\"url\"],"` | — |
| [SRC-C9CF9B54F8-L001047](../../agents/omarai.py#L1047) | 1047 | `"            str(source.get(\"platform\") or \"web\")[:80],"` | — |
| [SRC-C9CF9B54F8-L001048](../../agents/omarai.py#L1048) | 1048 | `"            observed_at=now_utc(),"` | — |
| [SRC-C9CF9B54F8-L001049](../../agents/omarai.py#L1049) | 1049 | `"            note=note[:1000],"` | — |
| [SRC-C9CF9B54F8-L001050](../../agents/omarai.py#L1050) | 1050 | `"            product_terms=product_terms,"` | — |
| [SRC-C9CF9B54F8-L001051](../../agents/omarai.py#L1051) | 1051 | `"            location_terms=location_terms,"` | — |
| [SRC-C9CF9B54F8-L001052](../../agents/omarai.py#L1052) | 1052 | `"            tenant_id=tenant_id,"` | — |
| [SRC-C9CF9B54F8-L001053](../../agents/omarai.py#L1053) | 1053 | `"        )"` | — |
| [SRC-C9CF9B54F8-L001054](../../agents/omarai.py#L1054) | 1054 | `""` | — |
| [SRC-C9CF9B54F8-L001055](../../agents/omarai.py#L1055) | 1055 | `"    def import_csv(self, filename: str, *, tenant_id: str \| None = None):"` | — |
| [SRC-C9CF9B54F8-L001056](../../agents/omarai.py#L1056) | 1056 | `"        tenant = self._tenant(tenant_id)"` | — |
| [SRC-C9CF9B54F8-L001057](../../agents/omarai.py#L1057) | 1057 | `"        results = {\"created\": 0, \"duplicates\": 0, \"errors\": []}"` | — |
| [SRC-C9CF9B54F8-L001058](../../agents/omarai.py#L1058) | 1058 | `"        with open(filename, newline=\"\", encoding=\"utf-8-sig\") as stream:"` | — |
| [SRC-C9CF9B54F8-L001059](../../agents/omarai.py#L1059) | 1059 | `"            reader = csv.DictReader(stream)"` | — |
| [SRC-C9CF9B54F8-L001060](../../agents/omarai.py#L1060) | 1060 | `"            required = {\"text\", \"source_url\", \"platform\"}"` | — |
| [SRC-C9CF9B54F8-L001061](../../agents/omarai.py#L1061) | 1061 | `"            if not reader.fieldnames or not required.issubset(reader.fieldnames):"` | — |
| [SRC-C9CF9B54F8-L001062](../../agents/omarai.py#L1062) | 1062 | `"                raise ValueError(\"CSV must contain text,source_url,platform columns\")"` | — |
| [SRC-C9CF9B54F8-L001063](../../agents/omarai.py#L1063) | 1063 | `"            for line, row in enumerate(reader, 2):"` | — |
| [SRC-C9CF9B54F8-L001064](../../agents/omarai.py#L1064) | 1064 | `"                try:"` | — |
| [SRC-C9CF9B54F8-L001065](../../agents/omarai.py#L1065) | 1065 | `"                    _, created = self.add("` | — |
| [SRC-C9CF9B54F8-L001066](../../agents/omarai.py#L1066) | 1066 | `"                        row[\"text\"], row[\"source_url\"], row[\"platform\"],"` | — |
| [SRC-C9CF9B54F8-L001067](../../agents/omarai.py#L1067) | 1067 | `"                        row.get(\"observed_at\") or None, row.get(\"note\") or \"\","` | — |
| [SRC-C9CF9B54F8-L001068](../../agents/omarai.py#L1068) | 1068 | `"                        tenant_id=tenant,"` | — |
| [SRC-C9CF9B54F8-L001069](../../agents/omarai.py#L1069) | 1069 | `"                    )"` | — |
| [SRC-C9CF9B54F8-L001070](../../agents/omarai.py#L1070) | 1070 | `"                    results[\"created\" if created else \"duplicates\"] += 1"` | — |
| [SRC-C9CF9B54F8-L001071](../../agents/omarai.py#L1071) | 1071 | `"                except (ValueError, TypeError) as exc:"` | — |
| [SRC-C9CF9B54F8-L001072](../../agents/omarai.py#L1072) | 1072 | `"                    results[\"errors\"].append({\"line\": line, \"error\": str(exc)})"` | — |
| [SRC-C9CF9B54F8-L001073](../../agents/omarai.py#L1073) | 1073 | `"        return results"` | — |
| [SRC-C9CF9B54F8-L001074](../../agents/omarai.py#L1074) | 1074 | `""` | — |
| [SRC-C9CF9B54F8-L001075](../../agents/omarai.py#L1075) | 1075 | `"    def export_csv(self, filename: str, *, tenant_id: str \| None = None):"` | — |
| [SRC-C9CF9B54F8-L001076](../../agents/omarai.py#L1076) | 1076 | `"        rows = self.list(limit=500, tenant_id=tenant_id)"` | — |
| [SRC-C9CF9B54F8-L001077](../../agents/omarai.py#L1077) | 1077 | `"        with open(filename, \"w\", newline=\"\", encoding=\"utf-8-sig\") as stream:"` | — |
| [SRC-C9CF9B54F8-L001078](../../agents/omarai.py#L1078) | 1078 | `"            fields = ["` | — |
| [SRC-C9CF9B54F8-L001079](../../agents/omarai.py#L1079) | 1079 | `"                \"id\", \"tenant_id\", \"text\", \"source_url\", \"platform\", \"observed_at\","` | — |
| [SRC-C9CF9B54F8-L001080](../../agents/omarai.py#L1080) | 1080 | `"                \"assessment\", \"status\", \"note\", \"created_at\","` | — |
| [SRC-C9CF9B54F8-L001081](../../agents/omarai.py#L1081) | 1081 | `"            ]"` | — |
| [SRC-C9CF9B54F8-L001082](../../agents/omarai.py#L1082) | 1082 | `"            writer = csv.DictWriter(stream, fieldnames=fields, quoting=csv.QUOTE_ALL)"` | — |
| [SRC-C9CF9B54F8-L001083](../../agents/omarai.py#L1083) | 1083 | `"            writer.writeheader()"` | — |
| [SRC-C9CF9B54F8-L001084](../../agents/omarai.py#L1084) | 1084 | `"            for row in rows:"` | — |
| [SRC-C9CF9B54F8-L001085](../../agents/omarai.py#L1085) | 1085 | `"                values = {"` | — |
| [SRC-C9CF9B54F8-L001086](../../agents/omarai.py#L1086) | 1086 | `"                    key: json.dumps(row[key], ensure_ascii=False)"` | — |
| [SRC-C9CF9B54F8-L001087](../../agents/omarai.py#L1087) | 1087 | `"                    if key == \"assessment\""` | — |
| [SRC-C9CF9B54F8-L001088](../../agents/omarai.py#L1088) | 1088 | `"                    else row.get(key, \"\")"` | — |
| [SRC-C9CF9B54F8-L001089](../../agents/omarai.py#L1089) | 1089 | `"                    for key in fields"` | — |
| [SRC-C9CF9B54F8-L001090](../../agents/omarai.py#L1090) | 1090 | `"                }"` | — |
| [SRC-C9CF9B54F8-L001091](../../agents/omarai.py#L1091) | 1091 | `"                writer.writerow({key: _csv_safe_cell(value) for key, value in values.items()})"` | — |
| [SRC-C9CF9B54F8-L001092](../../agents/omarai.py#L1092) | 1092 | `"        return len(rows)"` | — |
## الوكيل والمنطق

### FILE-FDEEAFDFCA — [agents/request_budget.py](../../agents/request_budget.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-FDEEAFDFCA-L000001](../../agents/request_budget.py#L1) | 1 | `"\"\"\"Cooperative per-request resource budgets for Omarai's web-research pipeline."` | — |
| [SRC-FDEEAFDFCA-L000002](../../agents/request_budget.py#L2) | 2 | `""` | — |
| [SRC-FDEEAFDFCA-L000003](../../agents/request_budget.py#L3) | 3 | `"The budget limits work that has not started yet and caps the timeout supplied to"` | — |
| [SRC-FDEEAFDFCA-L000004](../../agents/request_budget.py#L4) | 4 | `"each outbound operation by the remaining request window. Socket libraries may"` | — |
| [SRC-FDEEAFDFCA-L000005](../../agents/request_budget.py#L5) | 5 | `"still overrun a cooperative deadline slightly while unwinding an in-flight call;"` | — |
| [SRC-FDEEAFDFCA-L000006](../../agents/request_budget.py#L6) | 6 | `"this is not a hard real-time cancellation primitive."` | — |
| [SRC-FDEEAFDFCA-L000007](../../agents/request_budget.py#L7) | 7 | `"\"\"\""` | — |
| [SRC-FDEEAFDFCA-L000008](../../agents/request_budget.py#L8) | 8 | `"from __future__ import annotations"` | — |
| [SRC-FDEEAFDFCA-L000009](../../agents/request_budget.py#L9) | 9 | `""` | — |
| [SRC-FDEEAFDFCA-L000010](../../agents/request_budget.py#L10) | 10 | `"import os"` | — |
| [SRC-FDEEAFDFCA-L000011](../../agents/request_budget.py#L11) | 11 | `"import threading"` | — |
| [SRC-FDEEAFDFCA-L000012](../../agents/request_budget.py#L12) | 12 | `"import time"` | — |
| [SRC-FDEEAFDFCA-L000013](../../agents/request_budget.py#L13) | 13 | `"from collections.abc import Callable, Mapping"` | — |
| [SRC-FDEEAFDFCA-L000014](../../agents/request_budget.py#L14) | 14 | `"from typing import Any"` | — |
| [SRC-FDEEAFDFCA-L000015](../../agents/request_budget.py#L15) | 15 | `""` | — |
| [SRC-FDEEAFDFCA-L000016](../../agents/request_budget.py#L16) | 16 | `""` | — |
| [SRC-FDEEAFDFCA-L000017](../../agents/request_budget.py#L17) | 17 | `"class RequestBudgetExceeded(Exception):"` | — |
| [SRC-FDEEAFDFCA-L000018](../../agents/request_budget.py#L18) | 18 | `"    \"\"\"Raised when a request cannot start more work within its resource budget.\"\"\""` | — |
| [SRC-FDEEAFDFCA-L000019](../../agents/request_budget.py#L19) | 19 | `""` | — |
| [SRC-FDEEAFDFCA-L000020](../../agents/request_budget.py#L20) | 20 | `""` | — |
| [SRC-FDEEAFDFCA-L000021](../../agents/request_budget.py#L21) | 21 | `"DEFAULT_TIMEOUT_SECONDS = 90"` | — |
| [SRC-FDEEAFDFCA-L000022](../../agents/request_budget.py#L22) | 22 | `"MAX_TIMEOUT_SECONDS = 120"` | — |
| [SRC-FDEEAFDFCA-L000023](../../agents/request_budget.py#L23) | 23 | `"RESOURCE_LIMITS = {"` | — |
| [SRC-FDEEAFDFCA-L000024](../../agents/request_budget.py#L24) | 24 | `"    \"search_queries\": (8, 8),"` | — |
| [SRC-FDEEAFDFCA-L000025](../../agents/request_budget.py#L25) | 25 | `"    \"search_calls\": (32, 40),"` | — |
| [SRC-FDEEAFDFCA-L000026](../../agents/request_budget.py#L26) | 26 | `"    \"model_calls\": (8, 12),"` | — |
| [SRC-FDEEAFDFCA-L000027](../../agents/request_budget.py#L27) | 27 | `"    \"page_fetches\": (8, 8),"` | — |
| [SRC-FDEEAFDFCA-L000028](../../agents/request_budget.py#L28) | 28 | `"    \"tool_calls\": (3, 3),"` | — |
| [SRC-FDEEAFDFCA-L000029](../../agents/request_budget.py#L29) | 29 | `"}"` | — |
| [SRC-FDEEAFDFCA-L000030](../../agents/request_budget.py#L30) | 30 | `""` | — |
| [SRC-FDEEAFDFCA-L000031](../../agents/request_budget.py#L31) | 31 | `"# Hard ceilings for the public hosted-acceptance profile. Operator environment"` | — |
| [SRC-FDEEAFDFCA-L000032](../../agents/request_budget.py#L32) | 32 | `"# limits may lower these values, but can never be raised by a client request."` | — |
| [SRC-FDEEAFDFCA-L000033](../../agents/request_budget.py#L33) | 33 | `"HOSTED_SMOKE_BUDGET_LIMITS = {"` | — |
| [SRC-FDEEAFDFCA-L000034](../../agents/request_budget.py#L34) | 34 | `"    \"search_queries\": 3,"` | — |
| [SRC-FDEEAFDFCA-L000035](../../agents/request_budget.py#L35) | 35 | `"    \"search_calls\": 12,"` | — |
| [SRC-FDEEAFDFCA-L000036](../../agents/request_budget.py#L36) | 36 | `"    \"model_calls\": 6,"` | — |
| [SRC-FDEEAFDFCA-L000037](../../agents/request_budget.py#L37) | 37 | `"    \"page_fetches\": 4,"` | — |
| [SRC-FDEEAFDFCA-L000038](../../agents/request_budget.py#L38) | 38 | `"    \"tool_calls\": 0,"` | — |
| [SRC-FDEEAFDFCA-L000039](../../agents/request_budget.py#L39) | 39 | `"}"` | — |
| [SRC-FDEEAFDFCA-L000040](../../agents/request_budget.py#L40) | 40 | `"HOSTED_SMOKE_BUDGET_TIMEOUT_SECONDS = 75"` | — |
| [SRC-FDEEAFDFCA-L000041](../../agents/request_budget.py#L41) | 41 | `""` | — |
| [SRC-FDEEAFDFCA-L000042](../../agents/request_budget.py#L42) | 42 | `""` | — |
| [SRC-FDEEAFDFCA-L000043](../../agents/request_budget.py#L43) | 43 | `"def _bounded_env_int(name: str, default: int, minimum: int, maximum: int) -> int:"` | — |
| [SRC-FDEEAFDFCA-L000044](../../agents/request_budget.py#L44) | 44 | `"    raw = os.getenv(name, \"\").strip()"` | — |
| [SRC-FDEEAFDFCA-L000045](../../agents/request_budget.py#L45) | 45 | `"    try:"` | — |
| [SRC-FDEEAFDFCA-L000046](../../agents/request_budget.py#L46) | 46 | `"        value = int(raw) if raw else default"` | — |
| [SRC-FDEEAFDFCA-L000047](../../agents/request_budget.py#L47) | 47 | `"    except (TypeError, ValueError):"` | — |
| [SRC-FDEEAFDFCA-L000048](../../agents/request_budget.py#L48) | 48 | `"        value = default"` | — |
| [SRC-FDEEAFDFCA-L000049](../../agents/request_budget.py#L49) | 49 | `"    return max(minimum, min(value, maximum))"` | — |
| [SRC-FDEEAFDFCA-L000050](../../agents/request_budget.py#L50) | 50 | `""` | — |
| [SRC-FDEEAFDFCA-L000051](../../agents/request_budget.py#L51) | 51 | `""` | — |
| [SRC-FDEEAFDFCA-L000052](../../agents/request_budget.py#L52) | 52 | `"class RequestBudget:"` | — |
| [SRC-FDEEAFDFCA-L000053](../../agents/request_budget.py#L53) | 53 | `"    \"\"\"Thread-safe counters and a cooperative monotonic deadline for one answer.\"\"\""` | — |
| [SRC-FDEEAFDFCA-L000054](../../agents/request_budget.py#L54) | 54 | `""` | — |
| [SRC-FDEEAFDFCA-L000055](../../agents/request_budget.py#L55) | 55 | `"    def __init__("` | — |
| [SRC-FDEEAFDFCA-L000056](../../agents/request_budget.py#L56) | 56 | `"        self,"` | — |
| [SRC-FDEEAFDFCA-L000057](../../agents/request_budget.py#L57) | 57 | `"        timeout_seconds: int = DEFAULT_TIMEOUT_SECONDS,"` | — |
| [SRC-FDEEAFDFCA-L000058](../../agents/request_budget.py#L58) | 58 | `"        limits: Mapping[str, int] \| None = None,"` | — |
| [SRC-FDEEAFDFCA-L000059](../../agents/request_budget.py#L59) | 59 | `"        clock: Callable[[], float] = time.monotonic,"` | — |
| [SRC-FDEEAFDFCA-L000060](../../agents/request_budget.py#L60) | 60 | `"        profile: str = \"default\","` | — |
| [SRC-FDEEAFDFCA-L000061](../../agents/request_budget.py#L61) | 61 | `"    ) -> None:"` | — |
| [SRC-FDEEAFDFCA-L000062](../../agents/request_budget.py#L62) | 62 | `"        self._clock = clock"` | — |
| [SRC-FDEEAFDFCA-L000063](../../agents/request_budget.py#L63) | 63 | `"        self.profile = profile"` | — |
| [SRC-FDEEAFDFCA-L000064](../../agents/request_budget.py#L64) | 64 | `"        bounded_timeout = max(10, min(int(timeout_seconds), MAX_TIMEOUT_SECONDS))"` | — |
| [SRC-FDEEAFDFCA-L000065](../../agents/request_budget.py#L65) | 65 | `"        self.started_at = clock()"` | — |
| [SRC-FDEEAFDFCA-L000066](../../agents/request_budget.py#L66) | 66 | `"        self.deadline = self.started_at + bounded_timeout"` | — |
| [SRC-FDEEAFDFCA-L000067](../../agents/request_budget.py#L67) | 67 | `"        self._limits = {"` | — |
| [SRC-FDEEAFDFCA-L000068](../../agents/request_budget.py#L68) | 68 | `"            key: max(0, min(int(value), RESOURCE_LIMITS[key][1]))"` | — |
| [SRC-FDEEAFDFCA-L000069](../../agents/request_budget.py#L69) | 69 | `"            for key, (default, _maximum) in RESOURCE_LIMITS.items()"` | — |
| [SRC-FDEEAFDFCA-L000070](../../agents/request_budget.py#L70) | 70 | `"            for value in [limits[key] if limits and key in limits else default]"` | — |
| [SRC-FDEEAFDFCA-L000071](../../agents/request_budget.py#L71) | 71 | `"        }"` | — |
| [SRC-FDEEAFDFCA-L000072](../../agents/request_budget.py#L72) | 72 | `"        self._counts = {key: 0 for key in self._limits}"` | — |
| [SRC-FDEEAFDFCA-L000073](../../agents/request_budget.py#L73) | 73 | `"        self._exhausted_reasons: set[str] = set()"` | — |
| [SRC-FDEEAFDFCA-L000074](../../agents/request_budget.py#L74) | 74 | `"        self._lock = threading.Lock()"` | — |
| [SRC-FDEEAFDFCA-L000075](../../agents/request_budget.py#L75) | 75 | `""` | — |
| [SRC-FDEEAFDFCA-L000076](../../agents/request_budget.py#L76) | 76 | `"    @classmethod"` | — |
| [SRC-FDEEAFDFCA-L000077](../../agents/request_budget.py#L77) | 77 | `"    def from_environment(cls, profile: str = \"default\") -> RequestBudget:"` | — |
| [SRC-FDEEAFDFCA-L000078](../../agents/request_budget.py#L78) | 78 | `"        if profile not in {\"default\", \"hosted_smoke\"}:"` | — |
| [SRC-FDEEAFDFCA-L000079](../../agents/request_budget.py#L79) | 79 | `"            raise ValueError(f\"unknown request-budget profile: {profile}\")"` | — |
| [SRC-FDEEAFDFCA-L000080](../../agents/request_budget.py#L80) | 80 | `"        timeout = _bounded_env_int("` | — |
| [SRC-FDEEAFDFCA-L000081](../../agents/request_budget.py#L81) | 81 | `"            \"OMARAI_REQUEST_BUDGET_SECONDS\","` | — |
| [SRC-FDEEAFDFCA-L000082](../../agents/request_budget.py#L82) | 82 | `"            DEFAULT_TIMEOUT_SECONDS,"` | — |
| [SRC-FDEEAFDFCA-L000083](../../agents/request_budget.py#L83) | 83 | `"            10,"` | — |
| [SRC-FDEEAFDFCA-L000084](../../agents/request_budget.py#L84) | 84 | `"            MAX_TIMEOUT_SECONDS,"` | — |
| [SRC-FDEEAFDFCA-L000085](../../agents/request_budget.py#L85) | 85 | `"        )"` | — |
| [SRC-FDEEAFDFCA-L000086](../../agents/request_budget.py#L86) | 86 | `"        limits = {"` | — |
| [SRC-FDEEAFDFCA-L000087](../../agents/request_budget.py#L87) | 87 | `"            key: _bounded_env_int("` | — |
| [SRC-FDEEAFDFCA-L000088](../../agents/request_budget.py#L88) | 88 | `"                f\"OMARAI_REQUEST_MAX_{key.upper()}\","` | — |
| [SRC-FDEEAFDFCA-L000089](../../agents/request_budget.py#L89) | 89 | `"                defaults[0],"` | — |
| [SRC-FDEEAFDFCA-L000090](../../agents/request_budget.py#L90) | 90 | `"                0 if key == \"tool_calls\" else 1,"` | — |
| [SRC-FDEEAFDFCA-L000091](../../agents/request_budget.py#L91) | 91 | `"                defaults[1],"` | — |
| [SRC-FDEEAFDFCA-L000092](../../agents/request_budget.py#L92) | 92 | `"            )"` | — |
| [SRC-FDEEAFDFCA-L000093](../../agents/request_budget.py#L93) | 93 | `"            for key, defaults in RESOURCE_LIMITS.items()"` | — |
| [SRC-FDEEAFDFCA-L000094](../../agents/request_budget.py#L94) | 94 | `"        }"` | — |
| [SRC-FDEEAFDFCA-L000095](../../agents/request_budget.py#L95) | 95 | `"        if profile == \"hosted_smoke\":"` | — |
| [SRC-FDEEAFDFCA-L000096](../../agents/request_budget.py#L96) | 96 | `"            timeout = min(timeout, HOSTED_SMOKE_BUDGET_TIMEOUT_SECONDS)"` | — |
| [SRC-FDEEAFDFCA-L000097](../../agents/request_budget.py#L97) | 97 | `"            limits = {"` | — |
| [SRC-FDEEAFDFCA-L000098](../../agents/request_budget.py#L98) | 98 | `"                key: min(limits[key], HOSTED_SMOKE_BUDGET_LIMITS[key])"` | — |
| [SRC-FDEEAFDFCA-L000099](../../agents/request_budget.py#L99) | 99 | `"                for key in RESOURCE_LIMITS"` | — |
| [SRC-FDEEAFDFCA-L000100](../../agents/request_budget.py#L100) | 100 | `"            }"` | — |
| [SRC-FDEEAFDFCA-L000101](../../agents/request_budget.py#L101) | 101 | `"        return cls(timeout_seconds=timeout, limits=limits, profile=profile)"` | — |
| [SRC-FDEEAFDFCA-L000102](../../agents/request_budget.py#L102) | 102 | `""` | — |
| [SRC-FDEEAFDFCA-L000103](../../agents/request_budget.py#L103) | 103 | `"    def remaining_seconds(self) -> float:"` | — |
| [SRC-FDEEAFDFCA-L000104](../../agents/request_budget.py#L104) | 104 | `"        return max(0.0, self.deadline - self._clock())"` | — |
| [SRC-FDEEAFDFCA-L000105](../../agents/request_budget.py#L105) | 105 | `""` | — |
| [SRC-FDEEAFDFCA-L000106](../../agents/request_budget.py#L106) | 106 | `"    def timeout_for(self, configured_seconds: float) -> float:"` | — |
| [SRC-FDEEAFDFCA-L000107](../../agents/request_budget.py#L107) | 107 | `"        \"\"\"Cap one outbound timeout to time remaining; raise instead of starting at zero.\"\"\""` | — |
| [SRC-FDEEAFDFCA-L000108](../../agents/request_budget.py#L108) | 108 | `"        remaining = self.remaining_seconds()"` | — |
| [SRC-FDEEAFDFCA-L000109](../../agents/request_budget.py#L109) | 109 | `"        if remaining <= 0:"` | — |
| [SRC-FDEEAFDFCA-L000110](../../agents/request_budget.py#L110) | 110 | `"            with self._lock:"` | — |
| [SRC-FDEEAFDFCA-L000111](../../agents/request_budget.py#L111) | 111 | `"                self._exhausted_reasons.add(\"deadline\")"` | — |
| [SRC-FDEEAFDFCA-L000112](../../agents/request_budget.py#L112) | 112 | `"            raise RequestBudgetExceeded(\"انتهت ميزانية وقت الطلب.\")"` | — |
| [SRC-FDEEAFDFCA-L000113](../../agents/request_budget.py#L113) | 113 | `"        return min(float(configured_seconds), remaining)"` | — |
| [SRC-FDEEAFDFCA-L000114](../../agents/request_budget.py#L114) | 114 | `""` | — |
| [SRC-FDEEAFDFCA-L000115](../../agents/request_budget.py#L115) | 115 | `"    def remaining_units(self, resource: str) -> int:"` | — |
| [SRC-FDEEAFDFCA-L000116](../../agents/request_budget.py#L116) | 116 | `"        \"\"\"Return unused units for a resource; zero means disabled, exhausted, or expired.\"\"\""` | — |
| [SRC-FDEEAFDFCA-L000117](../../agents/request_budget.py#L117) | 117 | `"        if resource not in self._limits:"` | — |
| [SRC-FDEEAFDFCA-L000118](../../agents/request_budget.py#L118) | 118 | `"            raise ValueError(f\"unknown request-budget resource: {resource}\")"` | — |
| [SRC-FDEEAFDFCA-L000119](../../agents/request_budget.py#L119) | 119 | `"        if self.remaining_seconds() <= 0:"` | — |
| [SRC-FDEEAFDFCA-L000120](../../agents/request_budget.py#L120) | 120 | `"            return 0"` | — |
| [SRC-FDEEAFDFCA-L000121](../../agents/request_budget.py#L121) | 121 | `"        with self._lock:"` | — |
| [SRC-FDEEAFDFCA-L000122](../../agents/request_budget.py#L122) | 122 | `"            return max(0, self._limits[resource] - self._counts[resource])"` | — |
| [SRC-FDEEAFDFCA-L000123](../../agents/request_budget.py#L123) | 123 | `""` | — |
| [SRC-FDEEAFDFCA-L000124](../../agents/request_budget.py#L124) | 124 | `"    def reserve(self, resource: str, amount: int = 1) -> None:"` | — |
| [SRC-FDEEAFDFCA-L000125](../../agents/request_budget.py#L125) | 125 | `"        \"\"\"Atomically reserve resource units before initiating external work.\"\"\""` | — |
| [SRC-FDEEAFDFCA-L000126](../../agents/request_budget.py#L126) | 126 | `"        if resource not in self._limits:"` | — |
| [SRC-FDEEAFDFCA-L000127](../../agents/request_budget.py#L127) | 127 | `"            raise ValueError(f\"unknown request-budget resource: {resource}\")"` | — |
| [SRC-FDEEAFDFCA-L000128](../../agents/request_budget.py#L128) | 128 | `"        if amount < 1:"` | — |
| [SRC-FDEEAFDFCA-L000129](../../agents/request_budget.py#L129) | 129 | `"            raise ValueError(\"reservation amount must be positive\")"` | — |
| [SRC-FDEEAFDFCA-L000130](../../agents/request_budget.py#L130) | 130 | `"        with self._lock:"` | — |
| [SRC-FDEEAFDFCA-L000131](../../agents/request_budget.py#L131) | 131 | `"            if self.remaining_seconds() <= 0:"` | — |
| [SRC-FDEEAFDFCA-L000132](../../agents/request_budget.py#L132) | 132 | `"                self._exhausted_reasons.add(\"deadline\")"` | — |
| [SRC-FDEEAFDFCA-L000133](../../agents/request_budget.py#L133) | 133 | `"                raise RequestBudgetExceeded(\"انتهت ميزانية وقت الطلب.\")"` | — |
| [SRC-FDEEAFDFCA-L000134](../../agents/request_budget.py#L134) | 134 | `"            limit = self._limits[resource]"` | — |
| [SRC-FDEEAFDFCA-L000135](../../agents/request_budget.py#L135) | 135 | `"            if self._counts[resource] + amount > limit:"` | — |
| [SRC-FDEEAFDFCA-L000136](../../agents/request_budget.py#L136) | 136 | `"                self._exhausted_reasons.add(resource)"` | — |
| [SRC-FDEEAFDFCA-L000137](../../agents/request_budget.py#L137) | 137 | `"                raise RequestBudgetExceeded("` | — |
| [SRC-FDEEAFDFCA-L000138](../../agents/request_budget.py#L138) | 138 | `"                    f\"تم بلوغ حد موارد الطلب: {resource}.\""` | — |
| [SRC-FDEEAFDFCA-L000139](../../agents/request_budget.py#L139) | 139 | `"                )"` | — |
| [SRC-FDEEAFDFCA-L000140](../../agents/request_budget.py#L140) | 140 | `"            self._counts[resource] += amount"` | — |
| [SRC-FDEEAFDFCA-L000141](../../agents/request_budget.py#L141) | 141 | `""` | — |
| [SRC-FDEEAFDFCA-L000142](../../agents/request_budget.py#L142) | 142 | `"    def snapshot(self) -> dict[str, Any]:"` | — |
| [SRC-FDEEAFDFCA-L000143](../../agents/request_budget.py#L143) | 143 | `"        with self._lock:"` | — |
| [SRC-FDEEAFDFCA-L000144](../../agents/request_budget.py#L144) | 144 | `"            counts = dict(self._counts)"` | — |
| [SRC-FDEEAFDFCA-L000145](../../agents/request_budget.py#L145) | 145 | `"            limits = dict(self._limits)"` | — |
| [SRC-FDEEAFDFCA-L000146](../../agents/request_budget.py#L146) | 146 | `"            exhausted_reasons = sorted(self._exhausted_reasons)"` | — |
| [SRC-FDEEAFDFCA-L000147](../../agents/request_budget.py#L147) | 147 | `"        remaining = self.remaining_seconds()"` | — |
| [SRC-FDEEAFDFCA-L000148](../../agents/request_budget.py#L148) | 148 | `"        return {"` | — |
| [SRC-FDEEAFDFCA-L000149](../../agents/request_budget.py#L149) | 149 | `"            \"policy\": \"cooperative_per_request_budget\","` | — |
| [SRC-FDEEAFDFCA-L000150](../../agents/request_budget.py#L150) | 150 | `"            \"profile\": self.profile,"` | — |
| [SRC-FDEEAFDFCA-L000151](../../agents/request_budget.py#L151) | 151 | `"            \"timeout_seconds\": round(self.deadline - self.started_at, 3),"` | — |
| [SRC-FDEEAFDFCA-L000152](../../agents/request_budget.py#L152) | 152 | `"            \"elapsed_seconds\": round(max(0.0, self._clock() - self.started_at), 3),"` | — |
| [SRC-FDEEAFDFCA-L000153](../../agents/request_budget.py#L153) | 153 | `"            \"remaining_seconds\": round(remaining, 3),"` | — |
| [SRC-FDEEAFDFCA-L000154](../../agents/request_budget.py#L154) | 154 | `"            \"deadline_exceeded\": remaining <= 0,"` | — |
| [SRC-FDEEAFDFCA-L000155](../../agents/request_budget.py#L155) | 155 | `"            \"budget_exhausted\": bool(exhausted_reasons) or remaining <= 0,"` | — |
| [SRC-FDEEAFDFCA-L000156](../../agents/request_budget.py#L156) | 156 | `"            \"exhausted_reasons\": exhausted_reasons,"` | — |
| [SRC-FDEEAFDFCA-L000157](../../agents/request_budget.py#L157) | 157 | `"            \"counts\": counts,"` | — |
| [SRC-FDEEAFDFCA-L000158](../../agents/request_budget.py#L158) | 158 | `"            \"limits\": limits,"` | — |
| [SRC-FDEEAFDFCA-L000159](../../agents/request_budget.py#L159) | 159 | `"            \"resources_at_limit\": ["` | — |
| [SRC-FDEEAFDFCA-L000160](../../agents/request_budget.py#L160) | 160 | `"                key for key, limit in limits.items() if limit > 0 and counts[key] >= limit"` | — |
| [SRC-FDEEAFDFCA-L000161](../../agents/request_budget.py#L161) | 161 | `"            ],"` | — |
| [SRC-FDEEAFDFCA-L000162](../../agents/request_budget.py#L162) | 162 | `"            \"disabled_resources\": [key for key, limit in limits.items() if limit == 0],"` | — |
| [SRC-FDEEAFDFCA-L000163](../../agents/request_budget.py#L163) | 163 | `"            \"hard_cancellation_guaranteed\": False,"` | — |
| [SRC-FDEEAFDFCA-L000164](../../agents/request_budget.py#L164) | 164 | `"        }"` | — |
## الوكيل والمنطق

### FILE-3D565C3B85 — [agents/requirement_evidence.py](../../agents/requirement_evidence.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-3D565C3B85-L000001](../../agents/requirement_evidence.py#L1) | 1 | `"\"\"\"Build bounded evidence-candidate traces for planned research requirements."` | — |
| [SRC-3D565C3B85-L000002](../../agents/requirement_evidence.py#L2) | 2 | `""` | — |
| [SRC-3D565C3B85-L000003](../../agents/requirement_evidence.py#L3) | 3 | `"Responsibility: connect up to eight requested coverage targets to up to twelve returned"` | — |
| [SRC-3D565C3B85-L000004](../../agents/requirement_evidence.py#L4) | 4 | `"sources and their query provenance. This is lexical candidate mapping only; it never"` | — |
| [SRC-3D565C3B85-L000005](../../agents/requirement_evidence.py#L5) | 5 | `"claims source entailment, semantic support, or factual correctness."` | — |
| [SRC-3D565C3B85-L000006](../../agents/requirement_evidence.py#L6) | 6 | `""` | — |
| [SRC-3D565C3B85-L000007](../../agents/requirement_evidence.py#L7) | 7 | `"Public contract: build_requirement_evidence_ledger(targets, sources, requirement_queries)"` | — |
| [SRC-3D565C3B85-L000008](../../agents/requirement_evidence.py#L8) | 8 | `"returns one bounded record per target, with source indexes, evidence basis, and a status."` | — |
| [SRC-3D565C3B85-L000009](../../agents/requirement_evidence.py#L9) | 9 | `"Dependencies point only to shared text normalization; no network or model calls occur."` | — |
| [SRC-3D565C3B85-L000010](../../agents/requirement_evidence.py#L10) | 10 | `"\"\"\""` | — |
| [SRC-3D565C3B85-L000011](../../agents/requirement_evidence.py#L11) | 11 | `"from __future__ import annotations"` | — |
| [SRC-3D565C3B85-L000012](../../agents/requirement_evidence.py#L12) | 12 | `""` | — |
| [SRC-3D565C3B85-L000013](../../agents/requirement_evidence.py#L13) | 13 | `"import re"` | — |
| [SRC-3D565C3B85-L000014](../../agents/requirement_evidence.py#L14) | 14 | `"from typing import Any"` | — |
| [SRC-3D565C3B85-L000015](../../agents/requirement_evidence.py#L15) | 15 | `""` | — |
| [SRC-3D565C3B85-L000016](../../agents/requirement_evidence.py#L16) | 16 | `"from agents.text_normalization import normalize_text, tokenize_text"` | — |
| [SRC-3D565C3B85-L000017](../../agents/requirement_evidence.py#L17) | 17 | `""` | — |
| [SRC-3D565C3B85-L000018](../../agents/requirement_evidence.py#L18) | 18 | `"_REQUIREMENT_ALIAS_GROUPS = ("` | — |
| [SRC-3D565C3B85-L000019](../../agents/requirement_evidence.py#L19) | 19 | `"    frozenset({\"السعر\", \"سعر\", \"تكلفه\", \"التكلفه\", \"التكاليف\", \"الثمن\", \"price\", \"cost\", \"pricing\", \"fee\"}),"` | — |
| [SRC-3D565C3B85-L000020](../../agents/requirement_evidence.py#L20) | 20 | `"    frozenset({\"البطاريه\", \"بطاريه\", \"battery\", \"batteries\"}),"` | — |
| [SRC-3D565C3B85-L000021](../../agents/requirement_evidence.py#L21) | 21 | `"    frozenset({\"الكاميرا\", \"كاميرا\", \"camera\", \"cameras\", \"تصوير\"}),"` | — |
| [SRC-3D565C3B85-L000022](../../agents/requirement_evidence.py#L22) | 22 | `"    frozenset({\"ضمان\", \"الضمان\", \"warranty\", \"guarantee\"}),"` | — |
| [SRC-3D565C3B85-L000023](../../agents/requirement_evidence.py#L23) | 23 | `"    frozenset({\"الخصوصيه\", \"خصوصيه\", \"privacy\", \"الامان\", \"امان\", \"security\", \"safety\"}),"` | — |
| [SRC-3D565C3B85-L000024](../../agents/requirement_evidence.py#L24) | 24 | `"    frozenset({\"الاعتماديه\", \"اعتماديه\", \"reliability\", \"reliable\", \"الموثوقيه\"}),"` | — |
| [SRC-3D565C3B85-L000025](../../agents/requirement_evidence.py#L25) | 25 | `"    frozenset({\"الدعم\", \"الدعم الفني\", \"support\", \"customer service\", \"خدمه\"}),"` | — |
| [SRC-3D565C3B85-L000026](../../agents/requirement_evidence.py#L26) | 26 | `")"` | — |
| [SRC-3D565C3B85-L000027](../../agents/requirement_evidence.py#L27) | 27 | `""` | — |
| [SRC-3D565C3B85-L000028](../../agents/requirement_evidence.py#L28) | 28 | `""` | — |
| [SRC-3D565C3B85-L000029](../../agents/requirement_evidence.py#L29) | 29 | `"def _alias_token_groups() -> list[set[str]]:"` | — |
| [SRC-3D565C3B85-L000030](../../agents/requirement_evidence.py#L30) | 30 | `"    groups: list[set[str]] = []"` | — |
| [SRC-3D565C3B85-L000031](../../agents/requirement_evidence.py#L31) | 31 | `"    for aliases in _REQUIREMENT_ALIAS_GROUPS:"` | — |
| [SRC-3D565C3B85-L000032](../../agents/requirement_evidence.py#L32) | 32 | `"        tokens: set[str] = set()"` | — |
| [SRC-3D565C3B85-L000033](../../agents/requirement_evidence.py#L33) | 33 | `"        for alias in aliases:"` | — |
| [SRC-3D565C3B85-L000034](../../agents/requirement_evidence.py#L34) | 34 | `"            tokens.update(tokenize_text(alias, drop_stopwords=True))"` | — |
| [SRC-3D565C3B85-L000035](../../agents/requirement_evidence.py#L35) | 35 | `"        groups.append(tokens)"` | — |
| [SRC-3D565C3B85-L000036](../../agents/requirement_evidence.py#L36) | 36 | `"    return groups"` | — |
| [SRC-3D565C3B85-L000037](../../agents/requirement_evidence.py#L37) | 37 | `""` | — |
| [SRC-3D565C3B85-L000038](../../agents/requirement_evidence.py#L38) | 38 | `""` | — |
| [SRC-3D565C3B85-L000039](../../agents/requirement_evidence.py#L39) | 39 | `"def _matched_target_terms(target_tokens: list[str], available_tokens: set[str]) -> list[str]:"` | — |
| [SRC-3D565C3B85-L000040](../../agents/requirement_evidence.py#L40) | 40 | `"    \"\"\"Match target terms conservatively, with a small explicit Arabic/English alias list.\"\"\""` | — |
| [SRC-3D565C3B85-L000041](../../agents/requirement_evidence.py#L41) | 41 | `"    groups = _alias_token_groups()"` | — |
| [SRC-3D565C3B85-L000042](../../agents/requirement_evidence.py#L42) | 42 | `"    matched: list[str] = []"` | — |
| [SRC-3D565C3B85-L000043](../../agents/requirement_evidence.py#L43) | 43 | `"    for token in target_tokens:"` | — |
| [SRC-3D565C3B85-L000044](../../agents/requirement_evidence.py#L44) | 44 | `"        aliases = next((group for group in groups if token in group), {token})"` | — |
| [SRC-3D565C3B85-L000045](../../agents/requirement_evidence.py#L45) | 45 | `"        if aliases.intersection(available_tokens):"` | — |
| [SRC-3D565C3B85-L000046](../../agents/requirement_evidence.py#L46) | 46 | `"            matched.append(token)"` | — |
| [SRC-3D565C3B85-L000047](../../agents/requirement_evidence.py#L47) | 47 | `"    return matched"` | — |
| [SRC-3D565C3B85-L000048](../../agents/requirement_evidence.py#L48) | 48 | `""` | — |
| [SRC-3D565C3B85-L000049](../../agents/requirement_evidence.py#L49) | 49 | `""` | — |
| [SRC-3D565C3B85-L000050](../../agents/requirement_evidence.py#L50) | 50 | `"def build_requirement_evidence_ledger("` | — |
| [SRC-3D565C3B85-L000051](../../agents/requirement_evidence.py#L51) | 51 | `"    coverage_targets: list[str] \| None,"` | — |
| [SRC-3D565C3B85-L000052](../../agents/requirement_evidence.py#L52) | 52 | `"    sources: list[dict[str, Any]] \| None,"` | — |
| [SRC-3D565C3B85-L000053](../../agents/requirement_evidence.py#L53) | 53 | `"    requirement_queries: list[dict[str, Any]] \| None = None,"` | — |
| [SRC-3D565C3B85-L000054](../../agents/requirement_evidence.py#L54) | 54 | `") -> list[dict[str, Any]]:"` | — |
| [SRC-3D565C3B85-L000055](../../agents/requirement_evidence.py#L55) | 55 | `"    \"\"\"Link requirements to query provenance and lexical source candidates, never to truth.\"\"\""` | — |
| [SRC-3D565C3B85-L000056](../../agents/requirement_evidence.py#L56) | 56 | `"    safe_sources = ["` | — |
| [SRC-3D565C3B85-L000057](../../agents/requirement_evidence.py#L57) | 57 | `"        item for item in (sources or [])[:12]"` | — |
| [SRC-3D565C3B85-L000058](../../agents/requirement_evidence.py#L58) | 58 | `"        if isinstance(item, dict)"` | — |
| [SRC-3D565C3B85-L000059](../../agents/requirement_evidence.py#L59) | 59 | `"    ]"` | — |
| [SRC-3D565C3B85-L000060](../../agents/requirement_evidence.py#L60) | 60 | `"    query_rows = ["` | — |
| [SRC-3D565C3B85-L000061](../../agents/requirement_evidence.py#L61) | 61 | `"        item for item in (requirement_queries or [])"` | — |
| [SRC-3D565C3B85-L000062](../../agents/requirement_evidence.py#L62) | 62 | `"        if isinstance(item, dict) and isinstance(item.get(\"target\"), str)"` | — |
| [SRC-3D565C3B85-L000063](../../agents/requirement_evidence.py#L63) | 63 | `"    ]"` | — |
| [SRC-3D565C3B85-L000064](../../agents/requirement_evidence.py#L64) | 64 | `"    query_by_target = {"` | — |
| [SRC-3D565C3B85-L000065](../../agents/requirement_evidence.py#L65) | 65 | `"        normalize_text(item[\"target\"]).strip().casefold(): str(item.get(\"query\") or \"\").strip()"` | — |
| [SRC-3D565C3B85-L000066](../../agents/requirement_evidence.py#L66) | 66 | `"        for item in query_rows"` | — |
| [SRC-3D565C3B85-L000067](../../agents/requirement_evidence.py#L67) | 67 | `"    }"` | — |
| [SRC-3D565C3B85-L000068](../../agents/requirement_evidence.py#L68) | 68 | `"    any_query_metadata = any(isinstance(item.get(\"queries\"), list) for item in safe_sources)"` | — |
| [SRC-3D565C3B85-L000069](../../agents/requirement_evidence.py#L69) | 69 | `"    ledger: list[dict[str, Any]] = []"` | — |
| [SRC-3D565C3B85-L000070](../../agents/requirement_evidence.py#L70) | 70 | `""` | — |
| [SRC-3D565C3B85-L000071](../../agents/requirement_evidence.py#L71) | 71 | `"    for target in (coverage_targets or [])[:8]:"` | — |
| [SRC-3D565C3B85-L000072](../../agents/requirement_evidence.py#L72) | 72 | `"        target_text = str(target or \"\")[:120]"` | — |
| [SRC-3D565C3B85-L000073](../../agents/requirement_evidence.py#L73) | 73 | `"        target_tokens = list(dict.fromkeys(tokenize_text(target_text, drop_stopwords=True)))"` | — |
| [SRC-3D565C3B85-L000074](../../agents/requirement_evidence.py#L74) | 74 | `"        if not target_tokens:"` | — |
| [SRC-3D565C3B85-L000075](../../agents/requirement_evidence.py#L75) | 75 | `"            target_tokens = list(dict.fromkeys(tokenize_text(target_text)))"` | — |
| [SRC-3D565C3B85-L000076](../../agents/requirement_evidence.py#L76) | 76 | `"        key = normalize_text(target_text).strip().casefold()"` | — |
| [SRC-3D565C3B85-L000077](../../agents/requirement_evidence.py#L77) | 77 | `"        targeted_query = query_by_target.get(key, \"\")"` | — |
| [SRC-3D565C3B85-L000078](../../agents/requirement_evidence.py#L78) | 78 | `"        normalized_query = re.sub(r\"\\s+\", \" \", targeted_query).strip().casefold()"` | — |
| [SRC-3D565C3B85-L000079](../../agents/requirement_evidence.py#L79) | 79 | `"        query_result_indexes: list[int] = []"` | — |
| [SRC-3D565C3B85-L000080](../../agents/requirement_evidence.py#L80) | 80 | `"        candidate_sources: list[dict[str, Any]] = []"` | — |
| [SRC-3D565C3B85-L000081](../../agents/requirement_evidence.py#L81) | 81 | `""` | — |
| [SRC-3D565C3B85-L000082](../../agents/requirement_evidence.py#L82) | 82 | `"        for source_index, source in enumerate(safe_sources, 1):"` | — |
| [SRC-3D565C3B85-L000083](../../agents/requirement_evidence.py#L83) | 83 | `"            raw_queries = source.get(\"queries\", [])"` | — |
| [SRC-3D565C3B85-L000084](../../agents/requirement_evidence.py#L84) | 84 | `"            source_queries = ["` | — |
| [SRC-3D565C3B85-L000085](../../agents/requirement_evidence.py#L85) | 85 | `"                re.sub(r\"\\s+\", \" \", str(value)).strip().casefold()"` | — |
| [SRC-3D565C3B85-L000086](../../agents/requirement_evidence.py#L86) | 86 | `"                for value in raw_queries"` | — |
| [SRC-3D565C3B85-L000087](../../agents/requirement_evidence.py#L87) | 87 | `"            ] if isinstance(raw_queries, list) else []"` | — |
| [SRC-3D565C3B85-L000088](../../agents/requirement_evidence.py#L88) | 88 | `"            if normalized_query and normalized_query in source_queries:"` | — |
| [SRC-3D565C3B85-L000089](../../agents/requirement_evidence.py#L89) | 89 | `"                query_result_indexes.append(source_index)"` | — |
| [SRC-3D565C3B85-L000090](../../agents/requirement_evidence.py#L90) | 90 | `""` | — |
| [SRC-3D565C3B85-L000091](../../agents/requirement_evidence.py#L91) | 91 | `"            page_text = str(source.get(\"page_text\") or \"\")"` | — |
| [SRC-3D565C3B85-L000092](../../agents/requirement_evidence.py#L92) | 92 | `"            snippet = str(source.get(\"snippet\") or \"\")"` | — |
| [SRC-3D565C3B85-L000093](../../agents/requirement_evidence.py#L93) | 93 | `"            title = str(source.get(\"title\") or \"\")"` | — |
| [SRC-3D565C3B85-L000094](../../agents/requirement_evidence.py#L94) | 94 | `"            if bool(source.get(\"page_fetched\")) and page_text.strip():"` | — |
| [SRC-3D565C3B85-L000095](../../agents/requirement_evidence.py#L95) | 95 | `"                candidate_text = page_text"` | — |
| [SRC-3D565C3B85-L000096](../../agents/requirement_evidence.py#L96) | 96 | `"                evidence_basis = \"extracted_page_text\""` | — |
| [SRC-3D565C3B85-L000097](../../agents/requirement_evidence.py#L97) | 97 | `"            elif snippet.strip():"` | — |
| [SRC-3D565C3B85-L000098](../../agents/requirement_evidence.py#L98) | 98 | `"                candidate_text = snippet"` | — |
| [SRC-3D565C3B85-L000099](../../agents/requirement_evidence.py#L99) | 99 | `"                evidence_basis = \"search_snippet\""` | — |
| [SRC-3D565C3B85-L000100](../../agents/requirement_evidence.py#L100) | 100 | `"            elif title.strip():"` | — |
| [SRC-3D565C3B85-L000101](../../agents/requirement_evidence.py#L101) | 101 | `"                candidate_text = title"` | — |
| [SRC-3D565C3B85-L000102](../../agents/requirement_evidence.py#L102) | 102 | `"                evidence_basis = \"title_only\""` | — |
| [SRC-3D565C3B85-L000103](../../agents/requirement_evidence.py#L103) | 103 | `"            else:"` | — |
| [SRC-3D565C3B85-L000104](../../agents/requirement_evidence.py#L104) | 104 | `"                candidate_text = \"\""` | — |
| [SRC-3D565C3B85-L000105](../../agents/requirement_evidence.py#L105) | 105 | `"                evidence_basis = \"no_readable_text\""` | — |
| [SRC-3D565C3B85-L000106](../../agents/requirement_evidence.py#L106) | 106 | `"            available_tokens = set(tokenize_text(candidate_text, drop_stopwords=True))"` | — |
| [SRC-3D565C3B85-L000107](../../agents/requirement_evidence.py#L107) | 107 | `"            matched_terms = _matched_target_terms(target_tokens, available_tokens)"` | — |
| [SRC-3D565C3B85-L000108](../../agents/requirement_evidence.py#L108) | 108 | `"            ratio = len(matched_terms) / len(target_tokens) if target_tokens else 0.0"` | — |
| [SRC-3D565C3B85-L000109](../../agents/requirement_evidence.py#L109) | 109 | `"            likely_candidate = bool(matched_terms) and ("` | — |
| [SRC-3D565C3B85-L000110](../../agents/requirement_evidence.py#L110) | 110 | `"                ratio >= 0.5 if len(target_tokens) > 1 else True"` | — |
| [SRC-3D565C3B85-L000111](../../agents/requirement_evidence.py#L111) | 111 | `"            )"` | — |
| [SRC-3D565C3B85-L000112](../../agents/requirement_evidence.py#L112) | 112 | `"            if likely_candidate:"` | — |
| [SRC-3D565C3B85-L000113](../../agents/requirement_evidence.py#L113) | 113 | `"                candidate_sources.append({"` | — |
| [SRC-3D565C3B85-L000114](../../agents/requirement_evidence.py#L114) | 114 | `"                    \"source_index\": source_index,"` | — |
| [SRC-3D565C3B85-L000115](../../agents/requirement_evidence.py#L115) | 115 | `"                    \"matched_target_terms\": matched_terms[:8],"` | — |
| [SRC-3D565C3B85-L000116](../../agents/requirement_evidence.py#L116) | 116 | `"                    \"token_overlap_ratio\": round(ratio, 3),"` | — |
| [SRC-3D565C3B85-L000117](../../agents/requirement_evidence.py#L117) | 117 | `"                    \"evidence_basis\": evidence_basis,"` | — |
| [SRC-3D565C3B85-L000118](../../agents/requirement_evidence.py#L118) | 118 | `"                })"` | — |
| [SRC-3D565C3B85-L000119](../../agents/requirement_evidence.py#L119) | 119 | `""` | — |
| [SRC-3D565C3B85-L000120](../../agents/requirement_evidence.py#L120) | 120 | `"        if candidate_sources:"` | — |
| [SRC-3D565C3B85-L000121](../../agents/requirement_evidence.py#L121) | 121 | `"            status = \"candidate_evidence_found_not_verified\""` | — |
| [SRC-3D565C3B85-L000122](../../agents/requirement_evidence.py#L122) | 122 | `"        elif query_result_indexes:"` | — |
| [SRC-3D565C3B85-L000123](../../agents/requirement_evidence.py#L123) | 123 | `"            status = \"query_returned_candidates_no_lexical_signal\""` | — |
| [SRC-3D565C3B85-L000124](../../agents/requirement_evidence.py#L124) | 124 | `"        elif targeted_query and not any_query_metadata:"` | — |
| [SRC-3D565C3B85-L000125](../../agents/requirement_evidence.py#L125) | 125 | `"            status = \"query_result_linkage_unavailable\""` | — |
| [SRC-3D565C3B85-L000126](../../agents/requirement_evidence.py#L126) | 126 | `"        elif targeted_query:"` | — |
| [SRC-3D565C3B85-L000127](../../agents/requirement_evidence.py#L127) | 127 | `"            status = \"no_candidate_evidence_found\""` | — |
| [SRC-3D565C3B85-L000128](../../agents/requirement_evidence.py#L128) | 128 | `"        else:"` | — |
| [SRC-3D565C3B85-L000129](../../agents/requirement_evidence.py#L129) | 129 | `"            status = \"query_not_available\""` | — |
| [SRC-3D565C3B85-L000130](../../agents/requirement_evidence.py#L130) | 130 | `""` | — |
| [SRC-3D565C3B85-L000131](../../agents/requirement_evidence.py#L131) | 131 | `"        ledger.append({"` | — |
| [SRC-3D565C3B85-L000132](../../agents/requirement_evidence.py#L132) | 132 | `"            \"target\": target_text,"` | — |
| [SRC-3D565C3B85-L000133](../../agents/requirement_evidence.py#L133) | 133 | `"            \"targeted_query\": targeted_query or None,"` | — |
| [SRC-3D565C3B85-L000134](../../agents/requirement_evidence.py#L134) | 134 | `"            \"targeted_query_status\": ("` | — |
| [SRC-3D565C3B85-L000135](../../agents/requirement_evidence.py#L135) | 135 | `"                \"linked_to_returned_sources\" if query_result_indexes"` | — |
| [SRC-3D565C3B85-L000136](../../agents/requirement_evidence.py#L136) | 136 | `"                else \"no_linked_source_record\""` | — |
| [SRC-3D565C3B85-L000137](../../agents/requirement_evidence.py#L137) | 137 | `"            ),"` | — |
| [SRC-3D565C3B85-L000138](../../agents/requirement_evidence.py#L138) | 138 | `"            \"query_result_source_indexes\": query_result_indexes[:12],"` | — |
| [SRC-3D565C3B85-L000139](../../agents/requirement_evidence.py#L139) | 139 | `"            \"candidate_source_indexes\": ["` | — |
| [SRC-3D565C3B85-L000140](../../agents/requirement_evidence.py#L140) | 140 | `"                item[\"source_index\"] for item in candidate_sources"` | — |
| [SRC-3D565C3B85-L000141](../../agents/requirement_evidence.py#L141) | 141 | `"            ],"` | — |
| [SRC-3D565C3B85-L000142](../../agents/requirement_evidence.py#L142) | 142 | `"            \"candidate_sources\": candidate_sources[:8],"` | — |
| [SRC-3D565C3B85-L000143](../../agents/requirement_evidence.py#L143) | 143 | `"            \"status\": status,"` | — |
| [SRC-3D565C3B85-L000144](../../agents/requirement_evidence.py#L144) | 144 | `"            \"method\": \"targeted_query_provenance_plus_lexical_source_screen\","` | — |
| [SRC-3D565C3B85-L000145](../../agents/requirement_evidence.py#L145) | 145 | `"            \"semantic_verification\": False,"` | — |
| [SRC-3D565C3B85-L000146](../../agents/requirement_evidence.py#L146) | 146 | `"            \"source_entailment_verified\": False,"` | — |
| [SRC-3D565C3B85-L000147](../../agents/requirement_evidence.py#L147) | 147 | `"        })"` | — |
| [SRC-3D565C3B85-L000148](../../agents/requirement_evidence.py#L148) | 148 | `"    return ledger"` | — |
## الوكيل والمنطق

### FILE-59CF4B7DE8 — [agents/research.py](../../agents/research.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-59CF4B7DE8-L000001](../../agents/research.py#L1) | 1 | `"\"\"\"Research planning, domain targeting, and multi-query source ranking."` | — |
| [SRC-59CF4B7DE8-L000002](../../agents/research.py#L2) | 2 | `""` | — |
| [SRC-59CF4B7DE8-L000003](../../agents/research.py#L3) | 3 | `"This module is deterministic by design: the language model may propose a plan,"` | — |
| [SRC-59CF4B7DE8-L000004](../../agents/research.py#L4) | 4 | `"but all queries, result counts and source records are validated before use."` | — |
| [SRC-59CF4B7DE8-L000005](../../agents/research.py#L5) | 5 | `"\"\"\""` | — |
| [SRC-59CF4B7DE8-L000006](../../agents/research.py#L6) | 6 | `"from __future__ import annotations"` | — |
| [SRC-59CF4B7DE8-L000007](../../agents/research.py#L7) | 7 | `""` | — |
| [SRC-59CF4B7DE8-L000008](../../agents/research.py#L8) | 8 | `"import ipaddress"` | — |
| [SRC-59CF4B7DE8-L000009](../../agents/research.py#L9) | 9 | `"import re"` | — |
| [SRC-59CF4B7DE8-L000010](../../agents/research.py#L10) | 10 | `"from datetime import UTC, datetime, timedelta"` | — |
| [SRC-59CF4B7DE8-L000011](../../agents/research.py#L11) | 11 | `"from email.utils import parsedate_to_datetime"` | — |
| [SRC-59CF4B7DE8-L000012](../../agents/research.py#L12) | 12 | `"from typing import Any"` | — |
| [SRC-59CF4B7DE8-L000013](../../agents/research.py#L13) | 13 | `"from urllib.parse import urlparse"` | — |
| [SRC-59CF4B7DE8-L000014](../../agents/research.py#L14) | 14 | `""` | — |
| [SRC-59CF4B7DE8-L000015](../../agents/research.py#L15) | 15 | `"import tldextract"` | — |
| [SRC-59CF4B7DE8-L000016](../../agents/research.py#L16) | 16 | `""` | — |
| [SRC-59CF4B7DE8-L000017](../../agents/research.py#L17) | 17 | `"from agents.aspect_planning import extract_aspects"` | — |
| [SRC-59CF4B7DE8-L000018](../../agents/research.py#L18) | 18 | `"from agents.intent_router import resolve_followup_query"` | — |
| [SRC-59CF4B7DE8-L000019](../../agents/research.py#L19) | 19 | `""` | — |
| [SRC-59CF4B7DE8-L000020](../../agents/research.py#L20) | 20 | `"MAX_PLAN_QUERIES = 8"` | — |
| [SRC-59CF4B7DE8-L000021](../../agents/research.py#L21) | 21 | `"MAX_QUERY_CHARS = 240"` | — |
| [SRC-59CF4B7DE8-L000022](../../agents/research.py#L22) | 22 | `"MAX_FUSED_RESULTS = 18"` | — |
| [SRC-59CF4B7DE8-L000023](../../agents/research.py#L23) | 23 | `""` | — |
| [SRC-59CF4B7DE8-L000024](../../agents/research.py#L24) | 24 | `""` | — |
| [SRC-59CF4B7DE8-L000025](../../agents/research.py#L25) | 25 | `"# Use the Public Suffix List snapshot bundled with tldextract; never fetch it at"` | — |
| [SRC-59CF4B7DE8-L000026](../../agents/research.py#L26) | 26 | `"# runtime. Including private suffixes keeps tenant-hosted sites (e.g. github.io)"` | — |
| [SRC-59CF4B7DE8-L000027](../../agents/research.py#L27) | 27 | `"# separate, while subdomains belonging to one registrable site share one identity."` | — |
| [SRC-59CF4B7DE8-L000028](../../agents/research.py#L28) | 28 | `"_DOMAIN_EXTRACTOR = tldextract.TLDExtract("` | — |
| [SRC-59CF4B7DE8-L000029](../../agents/research.py#L29) | 29 | `"    suffix_list_urls=(),"` | — |
| [SRC-59CF4B7DE8-L000030](../../agents/research.py#L30) | 30 | `"    include_psl_private_domains=True,"` | — |
| [SRC-59CF4B7DE8-L000031](../../agents/research.py#L31) | 31 | `")"` | — |
| [SRC-59CF4B7DE8-L000032](../../agents/research.py#L32) | 32 | `""` | — |
| [SRC-59CF4B7DE8-L000033](../../agents/research.py#L33) | 33 | `""` | — |
| [SRC-59CF4B7DE8-L000034](../../agents/research.py#L34) | 34 | `"def registrable_domain(value: Any) -> str:"` | — |
| [SRC-59CF4B7DE8-L000035](../../agents/research.py#L35) | 35 | `"    \"\"\"Return a normalized registrable domain (or normalized IP/unknown hostname)."` | — |
| [SRC-59CF4B7DE8-L000036](../../agents/research.py#L36) | 36 | `""` | — |
| [SRC-59CF4B7DE8-L000037](../../agents/research.py#L37) | 37 | `"    This is a conservative source-diversity key, not proof that two publishers"` | — |
| [SRC-59CF4B7DE8-L000038](../../agents/research.py#L38) | 38 | `"    are editorially independent. It prevents sibling subdomains from being"` | — |
| [SRC-59CF4B7DE8-L000039](../../agents/research.py#L39) | 39 | `"    counted as separate domains in the evidence coverage threshold."` | — |
| [SRC-59CF4B7DE8-L000040](../../agents/research.py#L40) | 40 | `"    \"\"\""` | — |
| [SRC-59CF4B7DE8-L000041](../../agents/research.py#L41) | 41 | `"    candidate = str(value or \"\").strip()"` | — |
| [SRC-59CF4B7DE8-L000042](../../agents/research.py#L42) | 42 | `"    if not candidate:"` | — |
| [SRC-59CF4B7DE8-L000043](../../agents/research.py#L43) | 43 | `"        return \"\""` | — |
| [SRC-59CF4B7DE8-L000044](../../agents/research.py#L44) | 44 | `"    parsed = urlparse(candidate if \"://\" in candidate else \"//\" + candidate)"` | — |
| [SRC-59CF4B7DE8-L000045](../../agents/research.py#L45) | 45 | `"    host = (parsed.hostname or \"\").rstrip(\".\").lower()"` | — |
| [SRC-59CF4B7DE8-L000046](../../agents/research.py#L46) | 46 | `"    if not host:"` | — |
| [SRC-59CF4B7DE8-L000047](../../agents/research.py#L47) | 47 | `"        return \"\""` | — |
| [SRC-59CF4B7DE8-L000048](../../agents/research.py#L48) | 48 | `"    try:"` | — |
| [SRC-59CF4B7DE8-L000049](../../agents/research.py#L49) | 49 | `"        return str(ipaddress.ip_address(host))"` | — |
| [SRC-59CF4B7DE8-L000050](../../agents/research.py#L50) | 50 | `"    except ValueError:"` | — |
| [SRC-59CF4B7DE8-L000051](../../agents/research.py#L51) | 51 | `"        pass"` | — |
| [SRC-59CF4B7DE8-L000052](../../agents/research.py#L52) | 52 | `"    try:"` | — |
| [SRC-59CF4B7DE8-L000053](../../agents/research.py#L53) | 53 | `"        host = host.encode(\"idna\").decode(\"ascii\").lower()"` | — |
| [SRC-59CF4B7DE8-L000054](../../agents/research.py#L54) | 54 | `"    except UnicodeError:"` | — |
| [SRC-59CF4B7DE8-L000055](../../agents/research.py#L55) | 55 | `"        return host"` | — |
| [SRC-59CF4B7DE8-L000056](../../agents/research.py#L56) | 56 | `"    extracted = _DOMAIN_EXTRACTOR(host)"` | — |
| [SRC-59CF4B7DE8-L000057](../../agents/research.py#L57) | 57 | `"    return (extracted.top_domain_under_public_suffix or host).lower()"` | — |
| [SRC-59CF4B7DE8-L000058](../../agents/research.py#L58) | 58 | `""` | — |
| [SRC-59CF4B7DE8-L000059](../../agents/research.py#L59) | 59 | `"SOCIAL_DOMAINS = {"` | — |
| [SRC-59CF4B7DE8-L000060](../../agents/research.py#L60) | 60 | `"    \"reddit\": \"reddit.com\","` | — |
| [SRC-59CF4B7DE8-L000061](../../agents/research.py#L61) | 61 | `"    \"youtube\": \"youtube.com\","` | — |
| [SRC-59CF4B7DE8-L000062](../../agents/research.py#L62) | 62 | `"    \"facebook\": \"facebook.com\","` | — |
| [SRC-59CF4B7DE8-L000063](../../agents/research.py#L63) | 63 | `"    \"instagram\": \"instagram.com\","` | — |
| [SRC-59CF4B7DE8-L000064](../../agents/research.py#L64) | 64 | `"    \"x\": \"x.com\","` | — |
| [SRC-59CF4B7DE8-L000065](../../agents/research.py#L65) | 65 | `"    \"twitter\": \"twitter.com\","` | — |
| [SRC-59CF4B7DE8-L000066](../../agents/research.py#L66) | 66 | `"    \"tiktok\": \"tiktok.com\","` | — |
| [SRC-59CF4B7DE8-L000067](../../agents/research.py#L67) | 67 | `"    \"linkedin\": \"linkedin.com\","` | — |
| [SRC-59CF4B7DE8-L000068](../../agents/research.py#L68) | 68 | `"    \"threads\": \"threads.net\","` | — |
| [SRC-59CF4B7DE8-L000069](../../agents/research.py#L69) | 69 | `"    \"bluesky\": \"bsky.app\","` | — |
| [SRC-59CF4B7DE8-L000070](../../agents/research.py#L70) | 70 | `"}"` | — |
| [SRC-59CF4B7DE8-L000071](../../agents/research.py#L71) | 71 | `""` | — |
| [SRC-59CF4B7DE8-L000072](../../agents/research.py#L72) | 72 | `"_SOCIAL_TERMS = ("` | — |
| [SRC-59CF4B7DE8-L000073](../../agents/research.py#L73) | 73 | `"    \"social media\", \"social network\", \"social posts\", \"social pages\", \"public social\", \"public posts\","` | — |
| [SRC-59CF4B7DE8-L000074](../../agents/research.py#L74) | 74 | `"    \"facebook\", \"instagram\", \"reddit\", \"youtube\", \"twitter\", \"x.com\","` | — |
| [SRC-59CF4B7DE8-L000075](../../agents/research.py#L75) | 75 | `"    \"tiktok\", \"linkedin\", \"threads\", \"bluesky\","` | — |
| [SRC-59CF4B7DE8-L000076](../../agents/research.py#L76) | 76 | `"    \"سوشيال\", \"التواصل الاجتماعي\", \"مواقع التواصل\", \"صفحات التواصل\","` | — |
| [SRC-59CF4B7DE8-L000077](../../agents/research.py#L77) | 77 | `"    \"منشورات\", \"تعليقات الناس\", \"آراء الناس\", \"تجارب المستخدمين\","` | — |
| [SRC-59CF4B7DE8-L000078](../../agents/research.py#L78) | 78 | `"    \"تجارب العملاء\", \"اراء العملاء\", \"آراء العملاء\", \"رأي الناس\","` | — |
| [SRC-59CF4B7DE8-L000079](../../agents/research.py#L79) | 79 | `"    \"كلام الناس\", \"الناس بتقول\", \"مراجعات العملاء\", \"تعليقات العملاء\","` | — |
| [SRC-59CF4B7DE8-L000080](../../agents/research.py#L80) | 80 | `"    \"بوستات\", \"فيدوهات\", \"فيديوهات\", \"ريلز\", \"تويتر\", \"فيسبوك\","` | — |
| [SRC-59CF4B7DE8-L000081](../../agents/research.py#L81) | 81 | `"    \"انستجرام\", \"إنستجرام\", \"تيك توك\", \"لينكدان\", \"لينكدإن\","` | — |
| [SRC-59CF4B7DE8-L000082](../../agents/research.py#L82) | 82 | `"    \"مصادر العملاء\", \"عملاء محتملين\", \"العملاء المحتملين\","` | — |
| [SRC-59CF4B7DE8-L000083](../../agents/research.py#L83) | 83 | `")"` | — |
| [SRC-59CF4B7DE8-L000084](../../agents/research.py#L84) | 84 | `""` | — |
| [SRC-59CF4B7DE8-L000085](../../agents/research.py#L85) | 85 | `"_FRESH_TERMS = ("` | — |
| [SRC-59CF4B7DE8-L000086](../../agents/research.py#L86) | 86 | `"    \"latest\", \"current\", \"today\", \"this week\", \"recent\", \"breaking\", \"news\","` | — |
| [SRC-59CF4B7DE8-L000087](../../agents/research.py#L87) | 87 | `"    \"now\", \"2026\", \"latest price\", \"market price\", \"updated\","` | — |
| [SRC-59CF4B7DE8-L000088](../../agents/research.py#L88) | 88 | `"    \"آخر\", \"اخر\", \"احدث\", \"أحدث\", \"حاليا\", \"حالياً\", \"الآن\", \"دلوقتي\", \"النهارده\", \"مؤخرًا\", \"مؤخرا\", \"اليوم\", \"هذا الاسبوع\","` | — |
| [SRC-59CF4B7DE8-L000089](../../agents/research.py#L89) | 89 | `"    \"هذا الأسبوع\", \"آخر الأخبار\", \"اخر الاخبار\", \"مستجدات\", \"حديث\","` | — |
| [SRC-59CF4B7DE8-L000090](../../agents/research.py#L90) | 90 | `"    \"سعر اليوم\", \"الاسعار الحالية\", \"الأسعار الحالية\", \"جديد\","` | — |
| [SRC-59CF4B7DE8-L000091](../../agents/research.py#L91) | 91 | `")"` | — |
| [SRC-59CF4B7DE8-L000092](../../agents/research.py#L92) | 92 | `""` | — |
| [SRC-59CF4B7DE8-L000093](../../agents/research.py#L93) | 93 | `"_DEEP_TERMS = ("` | — |
| [SRC-59CF4B7DE8-L000094](../../agents/research.py#L94) | 94 | `"    \"deep research\", \"in-depth\", \"comprehensive\", \"exhaustive\", \"compare\","` | — |
| [SRC-59CF4B7DE8-L000095](../../agents/research.py#L95) | 95 | `"    \"comparison\", \"pros and cons\", \"investigate\", \"evidence\", \"sources\","` | — |
| [SRC-59CF4B7DE8-L000096](../../agents/research.py#L96) | 96 | `"    \"بحث عميق\", \"بحث معمق\", \"بحث مكثف\", \"بحث شامل\", \"بالتفصيل\", \"قارن\","` | — |
| [SRC-59CF4B7DE8-L000097](../../agents/research.py#L97) | 97 | `"    \"مقارنة\", \"استقصاء\", \"تحقق\", \"تأكد\", \"مصادر\", \"أدلة\", \"ادلة\","` | — |
| [SRC-59CF4B7DE8-L000098](../../agents/research.py#L98) | 98 | `"    \"كل الجوانب\", \"بحث واسع\", \"متكامل\","` | — |
| [SRC-59CF4B7DE8-L000099](../../agents/research.py#L99) | 99 | `")"` | — |
| [SRC-59CF4B7DE8-L000100](../../agents/research.py#L100) | 100 | `""` | — |
| [SRC-59CF4B7DE8-L000101](../../agents/research.py#L101) | 101 | `""` | — |
| [SRC-59CF4B7DE8-L000102](../../agents/research.py#L102) | 102 | `"def extract_urls(text: str) -> list[str]:"` | — |
| [SRC-59CF4B7DE8-L000103](../../agents/research.py#L103) | 103 | `"    \"\"\"Extract explicit HTTP(S) URLs without trying to interpret their content as instructions.\"\"\""` | — |
| [SRC-59CF4B7DE8-L000104](../../agents/research.py#L104) | 104 | `"    candidates = re.findall(r\"https?://[^\\s<>()]+\", text or \"\", flags=re.IGNORECASE)"` | — |
| [SRC-59CF4B7DE8-L000105](../../agents/research.py#L105) | 105 | `"    cleaned: list[str] = []"` | — |
| [SRC-59CF4B7DE8-L000106](../../agents/research.py#L106) | 106 | `"    for value in candidates:"` | — |
| [SRC-59CF4B7DE8-L000107](../../agents/research.py#L107) | 107 | `"        url = value.rstrip(\".,;!?،؛:)\\\"'»\")"` | — |
| [SRC-59CF4B7DE8-L000108](../../agents/research.py#L108) | 108 | `"        if url and url not in cleaned:"` | — |
| [SRC-59CF4B7DE8-L000109](../../agents/research.py#L109) | 109 | `"            cleaned.append(url[:2048])"` | — |
| [SRC-59CF4B7DE8-L000110](../../agents/research.py#L110) | 110 | `"        if len(cleaned) >= 5:"` | — |
| [SRC-59CF4B7DE8-L000111](../../agents/research.py#L111) | 111 | `"            break"` | — |
| [SRC-59CF4B7DE8-L000112](../../agents/research.py#L112) | 112 | `"    return cleaned"` | — |
| [SRC-59CF4B7DE8-L000113](../../agents/research.py#L113) | 113 | `""` | — |
| [SRC-59CF4B7DE8-L000114](../../agents/research.py#L114) | 114 | `""` | — |
| [SRC-59CF4B7DE8-L000115](../../agents/research.py#L115) | 115 | `"def _compact(value: Any, limit: int = MAX_QUERY_CHARS) -> str:"` | — |
| [SRC-59CF4B7DE8-L000116](../../agents/research.py#L116) | 116 | `"    if not isinstance(value, str):"` | — |
| [SRC-59CF4B7DE8-L000117](../../agents/research.py#L117) | 117 | `"        return \"\""` | — |
| [SRC-59CF4B7DE8-L000118](../../agents/research.py#L118) | 118 | `"    return re.sub(r\"\\s+\", \" \", value).strip()[:limit]"` | — |
| [SRC-59CF4B7DE8-L000119](../../agents/research.py#L119) | 119 | `""` | — |
| [SRC-59CF4B7DE8-L000120](../../agents/research.py#L120) | 120 | `""` | — |
| [SRC-59CF4B7DE8-L000121](../../agents/research.py#L121) | 121 | `"_SEARCH_TOPIC_PRESERVING_META_PREFIX_RE = re.compile("` | — |
| [SRC-59CF4B7DE8-L000122](../../agents/research.py#L122) | 122 | `"    r\"^(?:(?:و?استخدم\|و?استعمل)\\s+مصادر?\\s+متعددة\\s+\""` | — |
| [SRC-59CF4B7DE8-L000123](../../agents/research.py#L123) | 123 | `"    r\"(?:للبحث\\s+عن\|للعثور\\s+على\|لإيجاد\|عن\|حول\|بشأن)\|\""` | — |
| [SRC-59CF4B7DE8-L000124](../../agents/research.py#L124) | 124 | `"    r\"use\\s+multiple\\s+sources\\s+to\\s+(?:research\|find\|investigate))\\s+\","` | — |
| [SRC-59CF4B7DE8-L000125](../../agents/research.py#L125) | 125 | `"    re.IGNORECASE,"` | — |
| [SRC-59CF4B7DE8-L000126](../../agents/research.py#L126) | 126 | `")"` | — |
| [SRC-59CF4B7DE8-L000127](../../agents/research.py#L127) | 127 | `""` | — |
| [SRC-59CF4B7DE8-L000128](../../agents/research.py#L128) | 128 | `"_SEARCH_META_START_RE = re.compile("` | — |
| [SRC-59CF4B7DE8-L000129](../../agents/research.py#L129) | 129 | `"    r\"^(?:و?استخدم\|و?استعمل\|و?اجب\|و?أجب\|و?لا تعرض\|و?لا تقدم\|\""` | — |
| [SRC-59CF4B7DE8-L000130](../../agents/research.py#L130) | 130 | `"    r\"please cite\|cite\|provide links\|mention sources\|use multiple sources\|\""` | — |
| [SRC-59CF4B7DE8-L000131](../../agents/research.py#L131) | 131 | `"    r\"don't present\|do not present)\\b\","` | — |
| [SRC-59CF4B7DE8-L000132](../../agents/research.py#L132) | 132 | `"    re.IGNORECASE,"` | — |
| [SRC-59CF4B7DE8-L000133](../../agents/research.py#L133) | 133 | `")"` | — |
| [SRC-59CF4B7DE8-L000134](../../agents/research.py#L134) | 134 | `"# Treat \"اذكر\" as an action unless its object is clearly citation/format metadata."` | — |
| [SRC-59CF4B7DE8-L000135](../../agents/research.py#L135) | 135 | `"# This preserves topic-bearing prompts such as \"اذكر أبرز السيارات الكهربائية...\"."` | — |
| [SRC-59CF4B7DE8-L000136](../../agents/research.py#L136) | 136 | `"_SEARCH_CITATION_META_START_RE = re.compile("` | — |
| [SRC-59CF4B7DE8-L000137](../../agents/research.py#L137) | 137 | `"    r\"^(?:و?اذكر(?:ي\|وا)?\|mention\|cite\|provide)\\s+\""` | — |
| [SRC-59CF4B7DE8-L000138](../../agents/research.py#L138) | 138 | `"    r\"(?:المصادر\|مصادر\|المصدر\|مصدر(?:[ًٌٍ]ا?\|ا[ًٌٍ]?)?\|\""` | — |
| [SRC-59CF4B7DE8-L000139](../../agents/research.py#L139) | 139 | `"    r\"روابط?\|رابط\|تواريخ?\|تاريخ\|الاخبار\|الأخبار\|\""` | — |
| [SRC-59CF4B7DE8-L000140](../../agents/research.py#L140) | 140 | `"    r\"the original posts\|links\|sources\|dates)(?=\\s\|$\|[،,])\","` | — |
| [SRC-59CF4B7DE8-L000141](../../agents/research.py#L141) | 141 | `"    re.IGNORECASE,"` | — |
| [SRC-59CF4B7DE8-L000142](../../agents/research.py#L142) | 142 | `")"` | — |
| [SRC-59CF4B7DE8-L000143](../../agents/research.py#L143) | 143 | `"# This is a response-quality instruction, not a topic query."` | — |
| [SRC-59CF4B7DE8-L000144](../../agents/research.py#L144) | 144 | `"_SEARCH_UNCERTAINTY_META_START_RE = re.compile("` | — |
| [SRC-59CF4B7DE8-L000145](../../agents/research.py#L145) | 145 | `"    r\"^و?وضّ?ح\\s+اذا\\s+كانت\\s+النتائج\\s+غير\\s+كافيه\\b\""` | — |
| [SRC-59CF4B7DE8-L000146](../../agents/research.py#L146) | 146 | `"    r\".*(?:لتمثيل\|تمثيل).*(?:اراء\\s+المستخدمين\|المستخدمين)\\b\","` | — |
| [SRC-59CF4B7DE8-L000147](../../agents/research.py#L147) | 147 | `"    re.IGNORECASE,"` | — |
| [SRC-59CF4B7DE8-L000148](../../agents/research.py#L148) | 148 | `")"` | — |
| [SRC-59CF4B7DE8-L000149](../../agents/research.py#L149) | 149 | `""` | — |
| [SRC-59CF4B7DE8-L000150](../../agents/research.py#L150) | 150 | `"_SEARCH_FACTS_INFERENCE_META_ONLY_RE = re.compile("` | — |
| [SRC-59CF4B7DE8-L000151](../../agents/research.py#L151) | 151 | `"    r\"^و?(?:ميّز\|ميز)\\s+بين\\s+الحقائق\\s+والاستنتاجات\\s*[.!؟؛،,]*$\","` | — |
| [SRC-59CF4B7DE8-L000152](../../agents/research.py#L152) | 152 | `"    re.IGNORECASE,"` | — |
| [SRC-59CF4B7DE8-L000153](../../agents/research.py#L153) | 153 | `")"` | — |
| [SRC-59CF4B7DE8-L000154](../../agents/research.py#L154) | 154 | `"_SEARCH_META_TAIL_RE = re.compile("` | — |
| [SRC-59CF4B7DE8-L000155](../../agents/research.py#L155) | 155 | `"    r\"\\s*[,،؛;]\\s*(?:و\\s*)?(?:استخدم\|استعمل\|ميّز\|ميز\|اجب\|أجب\|لا تعرض\|لا تقدم\|\""` | — |
| [SRC-59CF4B7DE8-L000156](../../agents/research.py#L156) | 156 | `"    r\"please cite\|cite\|provide links\|mention sources\|use multiple sources\|\""` | — |
| [SRC-59CF4B7DE8-L000157](../../agents/research.py#L157) | 157 | `"    r\"don't present\|do not present\|\""` | — |
| [SRC-59CF4B7DE8-L000158](../../agents/research.py#L158) | 158 | `"    r\"اذكر(?:ي\|وا)?\\s+(?:مصادر?\|المصادر\|مصدر\|روابط?\|رابط\|تواريخ?\|تاريخ\|الاخبار\|الأخبار))\\b.*$\","` | — |
| [SRC-59CF4B7DE8-L000159](../../agents/research.py#L159) | 159 | `"    re.IGNORECASE,"` | — |
| [SRC-59CF4B7DE8-L000160](../../agents/research.py#L160) | 160 | `")"` | — |
| [SRC-59CF4B7DE8-L000161](../../agents/research.py#L161) | 161 | `"_SEARCH_LEADING_ACTION_RE = re.compile("` | — |
| [SRC-59CF4B7DE8-L000162](../../agents/research.py#L162) | 162 | `"    r\"^(?:حلّل\|حلل\|اجمع\|قارن\|ناقش\|استكشف\|استقصِ\|و?ميّز\|و?ميز\|اعرض\|و?وضح\|و?وضّح\|و?اذكر(?:ي\|وا)?\|\""` | — |
| [SRC-59CF4B7DE8-L000163](../../agents/research.py#L163) | 163 | `"    r\"analyze\|analyse\|compare\|investigate\|collect\|gather\|review\|summarize\|\""` | — |
| [SRC-59CF4B7DE8-L000164](../../agents/research.py#L164) | 164 | `"    r\"(?:ابحث\|بحث\|دورلي\|دور\|اعثر)(?:\\s+(?:عن\|على))?)\\s+\","` | — |
| [SRC-59CF4B7DE8-L000165](../../agents/research.py#L165) | 165 | `"    re.IGNORECASE,"` | — |
| [SRC-59CF4B7DE8-L000166](../../agents/research.py#L166) | 166 | `")"` | — |
| [SRC-59CF4B7DE8-L000167](../../agents/research.py#L167) | 167 | `""` | — |
| [SRC-59CF4B7DE8-L000168](../../agents/research.py#L168) | 168 | `""` | — |
| [SRC-59CF4B7DE8-L000169](../../agents/research.py#L169) | 169 | `"def compact_search_query(value: Any, limit: int = MAX_QUERY_CHARS) -> str:"` | — |
| [SRC-59CF4B7DE8-L000170](../../agents/research.py#L170) | 170 | `"    \"\"\"Reduce a full request to the topic-bearing query; preserve safety checks elsewhere.\"\"\""` | — |
| [SRC-59CF4B7DE8-L000171](../../agents/research.py#L171) | 171 | `"    if not isinstance(value, str):"` | — |
| [SRC-59CF4B7DE8-L000172](../../agents/research.py#L172) | 172 | `"        return \"\""` | — |
| [SRC-59CF4B7DE8-L000173](../../agents/research.py#L173) | 173 | `"    cleaned = re.sub(r\"https?://[^\\s<>()]+\", \" \", value, flags=re.IGNORECASE)"` | — |
| [SRC-59CF4B7DE8-L000174](../../agents/research.py#L174) | 174 | `"    # Split question/sentence boundaries without splitting operators such as site:reddit.com."` | — |
| [SRC-59CF4B7DE8-L000175](../../agents/research.py#L175) | 175 | `"    segments = re.split("` | — |
| [SRC-59CF4B7DE8-L000176](../../agents/research.py#L176) | 176 | `"        r\"(?<=[!?؟؛;])\\s+\|(?<=\\.)\\s+(?=[A-Z\\u0600-\\u06FF])\","` | — |
| [SRC-59CF4B7DE8-L000177](../../agents/research.py#L177) | 177 | `"        cleaned,"` | — |
| [SRC-59CF4B7DE8-L000178](../../agents/research.py#L178) | 178 | `"    )"` | — |
| [SRC-59CF4B7DE8-L000179](../../agents/research.py#L179) | 179 | `"    useful: list[str] = []"` | — |
| [SRC-59CF4B7DE8-L000180](../../agents/research.py#L180) | 180 | `"    for segment in segments:"` | — |
| [SRC-59CF4B7DE8-L000181](../../agents/research.py#L181) | 181 | `"        segment = segment.strip()"` | — |
