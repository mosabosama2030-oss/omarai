# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **005**
- سجلات الأسطر: **800**
- النطاق: SRC-C9CF9B54F8-L000753 إلى SRC-3D565C3B85-L000018
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-C9CF9B54F8 — [agents/omarai.py](../../agents/omarai.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-C9CF9B54F8-L000753](../../agents/omarai.py#L753) | 753 | `"        if ("` | — |
| [SRC-C9CF9B54F8-L000754](../../agents/omarai.py#L754) | 754 | `"            not isinstance(max_age_seconds, int)"` | — |
| [SRC-C9CF9B54F8-L000755](../../agents/omarai.py#L755) | 755 | `"            or isinstance(max_age_seconds, bool)"` | — |
| [SRC-C9CF9B54F8-L000756](../../agents/omarai.py#L756) | 756 | `"            or not 60 <= max_age_seconds <= 24 * 60 * 60"` | — |
| [SRC-C9CF9B54F8-L000757](../../agents/omarai.py#L757) | 757 | `"        ):"` | — |
| [SRC-C9CF9B54F8-L000758](../../agents/omarai.py#L758) | 758 | `"            raise ValueError(\"browser session lifetime must be between 60 seconds and 24 hours\")"` | — |
| [SRC-C9CF9B54F8-L000759](../../agents/omarai.py#L759) | 759 | `""` | — |
| [SRC-C9CF9B54F8-L000760](../../agents/omarai.py#L760) | 760 | `"        session_id = secrets.token_urlsafe(32)"` | — |
| [SRC-C9CF9B54F8-L000761](../../agents/omarai.py#L761) | 761 | `"        created_at = now_utc()"` | — |
| [SRC-C9CF9B54F8-L000762](../../agents/omarai.py#L762) | 762 | `"        expires_at = ("` | — |
| [SRC-C9CF9B54F8-L000763](../../agents/omarai.py#L763) | 763 | `"            datetime.now(UTC) + timedelta(seconds=max_age_seconds)"` | — |
| [SRC-C9CF9B54F8-L000764](../../agents/omarai.py#L764) | 764 | `"        ).isoformat(timespec=\"seconds\").replace(\"+00:00\", \"Z\")"` | — |
| [SRC-C9CF9B54F8-L000765](../../agents/omarai.py#L765) | 765 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000766](../../agents/omarai.py#L766) | 766 | `"            # Browser sessions are short-lived credentials, not an audit log."` | — |
| [SRC-C9CF9B54F8-L000767](../../agents/omarai.py#L767) | 767 | `"            # Prune expired and revoked rows opportunistically before inserting"` | — |
| [SRC-C9CF9B54F8-L000768](../../agents/omarai.py#L768) | 768 | `"            # a new session so abandoned rows cannot grow without bound."` | — |
| [SRC-C9CF9B54F8-L000769](../../agents/omarai.py#L769) | 769 | `"            db.execute("` | — |
| [SRC-C9CF9B54F8-L000770](../../agents/omarai.py#L770) | 770 | `"                \"\"\"DELETE FROM web_sessions"` | — |
| [SRC-C9CF9B54F8-L000771](../../agents/omarai.py#L771) | 771 | `"                   WHERE revoked_at IS NOT NULL OR expires_at <= ?\"\"\","` | — |
| [SRC-C9CF9B54F8-L000772](../../agents/omarai.py#L772) | 772 | `"                (created_at,),"` | — |
| [SRC-C9CF9B54F8-L000773](../../agents/omarai.py#L773) | 773 | `"            )"` | — |
| [SRC-C9CF9B54F8-L000774](../../agents/omarai.py#L774) | 774 | `"            db.execute("` | — |
| [SRC-C9CF9B54F8-L000775](../../agents/omarai.py#L775) | 775 | `"                \"\"\"INSERT INTO web_sessions"` | — |
| [SRC-C9CF9B54F8-L000776](../../agents/omarai.py#L776) | 776 | `"                   (session_hash, credential_hash, is_shared_token, tenant_id,"` | — |
| [SRC-C9CF9B54F8-L000777](../../agents/omarai.py#L777) | 777 | `"                    user_id, created_at, expires_at, revoked_at)"` | — |
| [SRC-C9CF9B54F8-L000778](../../agents/omarai.py#L778) | 778 | `"                   VALUES (?, ?, ?, ?, ?, ?, ?, NULL)\"\"\","` | — |
| [SRC-C9CF9B54F8-L000779](../../agents/omarai.py#L779) | 779 | `"                ("` | — |
| [SRC-C9CF9B54F8-L000780](../../agents/omarai.py#L780) | 780 | `"                    self._token_hash(session_id),"` | — |
| [SRC-C9CF9B54F8-L000781](../../agents/omarai.py#L781) | 781 | `"                    self._token_hash(token),"` | — |
| [SRC-C9CF9B54F8-L000782](../../agents/omarai.py#L782) | 782 | `"                    1 if is_shared else 0,"` | — |
| [SRC-C9CF9B54F8-L000783](../../agents/omarai.py#L783) | 783 | `"                    principal[\"tenant_id\"],"` | — |
| [SRC-C9CF9B54F8-L000784](../../agents/omarai.py#L784) | 784 | `"                    principal[\"user_id\"],"` | — |
| [SRC-C9CF9B54F8-L000785](../../agents/omarai.py#L785) | 785 | `"                    created_at,"` | — |
| [SRC-C9CF9B54F8-L000786](../../agents/omarai.py#L786) | 786 | `"                    expires_at,"` | — |
| [SRC-C9CF9B54F8-L000787](../../agents/omarai.py#L787) | 787 | `"                ),"` | — |
| [SRC-C9CF9B54F8-L000788](../../agents/omarai.py#L788) | 788 | `"            )"` | — |
| [SRC-C9CF9B54F8-L000789](../../agents/omarai.py#L789) | 789 | `"        return session_id, principal"` | — |
| [SRC-C9CF9B54F8-L000790](../../agents/omarai.py#L790) | 790 | `""` | — |
| [SRC-C9CF9B54F8-L000791](../../agents/omarai.py#L791) | 791 | `"    def resolve_web_session("` | — |
| [SRC-C9CF9B54F8-L000792](../../agents/omarai.py#L792) | 792 | `"        self,"` | — |
| [SRC-C9CF9B54F8-L000793](../../agents/omarai.py#L793) | 793 | `"        session_id: str,"` | — |
| [SRC-C9CF9B54F8-L000794](../../agents/omarai.py#L794) | 794 | `"        *,"` | — |
| [SRC-C9CF9B54F8-L000795](../../agents/omarai.py#L795) | 795 | `"        shared_token: str = \"\","` | — |
| [SRC-C9CF9B54F8-L000796](../../agents/omarai.py#L796) | 796 | `"    ) -> dict \| None:"` | — |
| [SRC-C9CF9B54F8-L000797](../../agents/omarai.py#L797) | 797 | `"        \"\"\"Resolve an opaque browser session and re-check its backing credential.\"\"\""` | — |
| [SRC-C9CF9B54F8-L000798](../../agents/omarai.py#L798) | 798 | `"        if not isinstance(session_id, str) or not re.fullmatch("` | — |
| [SRC-C9CF9B54F8-L000799](../../agents/omarai.py#L799) | 799 | `"            r\"[A-Za-z0-9_-]{32,128}\", session_id"` | — |
| [SRC-C9CF9B54F8-L000800](../../agents/omarai.py#L800) | 800 | `"        ):"` | — |
| [SRC-C9CF9B54F8-L000801](../../agents/omarai.py#L801) | 801 | `"            return None"` | — |
| [SRC-C9CF9B54F8-L000802](../../agents/omarai.py#L802) | 802 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000803](../../agents/omarai.py#L803) | 803 | `"            session = db.execute("` | — |
| [SRC-C9CF9B54F8-L000804](../../agents/omarai.py#L804) | 804 | `"                \"\"\"SELECT credential_hash, is_shared_token, tenant_id, user_id"` | — |
| [SRC-C9CF9B54F8-L000805](../../agents/omarai.py#L805) | 805 | `"                   FROM web_sessions"` | — |
| [SRC-C9CF9B54F8-L000806](../../agents/omarai.py#L806) | 806 | `"                   WHERE session_hash=? AND revoked_at IS NULL AND expires_at > ?\"\"\","` | — |
| [SRC-C9CF9B54F8-L000807](../../agents/omarai.py#L807) | 807 | `"                (self._token_hash(session_id), now_utc()),"` | — |
| [SRC-C9CF9B54F8-L000808](../../agents/omarai.py#L808) | 808 | `"            ).fetchone()"` | — |
| [SRC-C9CF9B54F8-L000809](../../agents/omarai.py#L809) | 809 | `"            if not session:"` | — |
| [SRC-C9CF9B54F8-L000810](../../agents/omarai.py#L810) | 810 | `"                return None"` | — |
| [SRC-C9CF9B54F8-L000811](../../agents/omarai.py#L811) | 811 | `"            if session[\"is_shared_token\"]:"` | — |
| [SRC-C9CF9B54F8-L000812](../../agents/omarai.py#L812) | 812 | `"                if ("` | — |
| [SRC-C9CF9B54F8-L000813](../../agents/omarai.py#L813) | 813 | `"                    not shared_token"` | — |
| [SRC-C9CF9B54F8-L000814](../../agents/omarai.py#L814) | 814 | `"                    or not hmac.compare_digest("` | — |
| [SRC-C9CF9B54F8-L000815](../../agents/omarai.py#L815) | 815 | `"                        session[\"credential_hash\"], self._token_hash(shared_token)"` | — |
| [SRC-C9CF9B54F8-L000816](../../agents/omarai.py#L816) | 816 | `"                    )"` | — |
| [SRC-C9CF9B54F8-L000817](../../agents/omarai.py#L817) | 817 | `"                ):"` | — |
| [SRC-C9CF9B54F8-L000818](../../agents/omarai.py#L818) | 818 | `"                    return None"` | — |
| [SRC-C9CF9B54F8-L000819](../../agents/omarai.py#L819) | 819 | `"                principal = db.execute("` | — |
| [SRC-C9CF9B54F8-L000820](../../agents/omarai.py#L820) | 820 | `"                    \"\"\"SELECT m.tenant_id, m.user_id, m.role"` | — |
| [SRC-C9CF9B54F8-L000821](../../agents/omarai.py#L821) | 821 | `"                       FROM tenant_memberships m"` | — |
| [SRC-C9CF9B54F8-L000822](../../agents/omarai.py#L822) | 822 | `"                       JOIN tenants t ON t.id=m.tenant_id AND t.active=1"` | — |
| [SRC-C9CF9B54F8-L000823](../../agents/omarai.py#L823) | 823 | `"                       JOIN users u ON u.id=m.user_id AND u.active=1"` | — |
| [SRC-C9CF9B54F8-L000824](../../agents/omarai.py#L824) | 824 | `"                       WHERE m.tenant_id=? AND m.user_id=? AND m.active=1\"\"\","` | — |
| [SRC-C9CF9B54F8-L000825](../../agents/omarai.py#L825) | 825 | `"                    (session[\"tenant_id\"], session[\"user_id\"]),"` | — |
| [SRC-C9CF9B54F8-L000826](../../agents/omarai.py#L826) | 826 | `"                ).fetchone()"` | — |
| [SRC-C9CF9B54F8-L000827](../../agents/omarai.py#L827) | 827 | `"                return dict(principal) if principal else None"` | — |
| [SRC-C9CF9B54F8-L000828](../../agents/omarai.py#L828) | 828 | `""` | — |
| [SRC-C9CF9B54F8-L000829](../../agents/omarai.py#L829) | 829 | `"            principal = db.execute("` | — |
| [SRC-C9CF9B54F8-L000830](../../agents/omarai.py#L830) | 830 | `"                \"\"\"SELECT m.tenant_id, m.user_id, m.role"` | — |
| [SRC-C9CF9B54F8-L000831](../../agents/omarai.py#L831) | 831 | `"                   FROM api_tokens a"` | — |
| [SRC-C9CF9B54F8-L000832](../../agents/omarai.py#L832) | 832 | `"                   JOIN tenant_memberships m"` | — |
| [SRC-C9CF9B54F8-L000833](../../agents/omarai.py#L833) | 833 | `"                     ON m.tenant_id=a.tenant_id AND m.user_id=a.user_id"` | — |
| [SRC-C9CF9B54F8-L000834](../../agents/omarai.py#L834) | 834 | `"                   JOIN tenants t ON t.id=m.tenant_id AND t.active=1"` | — |
| [SRC-C9CF9B54F8-L000835](../../agents/omarai.py#L835) | 835 | `"                   JOIN users u ON u.id=m.user_id AND u.active=1"` | — |
| [SRC-C9CF9B54F8-L000836](../../agents/omarai.py#L836) | 836 | `"                   WHERE a.token_hash=? AND a.tenant_id=? AND a.user_id=?"` | — |
| [SRC-C9CF9B54F8-L000837](../../agents/omarai.py#L837) | 837 | `"                     AND a.active=1 AND m.active=1"` | — |
| [SRC-C9CF9B54F8-L000838](../../agents/omarai.py#L838) | 838 | `"                     AND (a.expires_at IS NULL OR a.expires_at > ?)\"\"\","` | — |
| [SRC-C9CF9B54F8-L000839](../../agents/omarai.py#L839) | 839 | `"                ("` | — |
| [SRC-C9CF9B54F8-L000840](../../agents/omarai.py#L840) | 840 | `"                    session[\"credential_hash\"],"` | — |
| [SRC-C9CF9B54F8-L000841](../../agents/omarai.py#L841) | 841 | `"                    session[\"tenant_id\"],"` | — |
| [SRC-C9CF9B54F8-L000842](../../agents/omarai.py#L842) | 842 | `"                    session[\"user_id\"],"` | — |
| [SRC-C9CF9B54F8-L000843](../../agents/omarai.py#L843) | 843 | `"                    now_utc(),"` | — |
| [SRC-C9CF9B54F8-L000844](../../agents/omarai.py#L844) | 844 | `"                ),"` | — |
| [SRC-C9CF9B54F8-L000845](../../agents/omarai.py#L845) | 845 | `"            ).fetchone()"` | — |
| [SRC-C9CF9B54F8-L000846](../../agents/omarai.py#L846) | 846 | `"        return dict(principal) if principal else None"` | — |
| [SRC-C9CF9B54F8-L000847](../../agents/omarai.py#L847) | 847 | `""` | — |
| [SRC-C9CF9B54F8-L000848](../../agents/omarai.py#L848) | 848 | `"    def revoke_web_session(self, session_id: str) -> bool:"` | — |
| [SRC-C9CF9B54F8-L000849](../../agents/omarai.py#L849) | 849 | `"        \"\"\"Revoke one opaque browser session without revoking its backing API token.\"\"\""` | — |
| [SRC-C9CF9B54F8-L000850](../../agents/omarai.py#L850) | 850 | `"        if not isinstance(session_id, str) or not re.fullmatch("` | — |
| [SRC-C9CF9B54F8-L000851](../../agents/omarai.py#L851) | 851 | `"            r\"[A-Za-z0-9_-]{32,128}\", session_id"` | — |
| [SRC-C9CF9B54F8-L000852](../../agents/omarai.py#L852) | 852 | `"        ):"` | — |
| [SRC-C9CF9B54F8-L000853](../../agents/omarai.py#L853) | 853 | `"            return False"` | — |
| [SRC-C9CF9B54F8-L000854](../../agents/omarai.py#L854) | 854 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000855](../../agents/omarai.py#L855) | 855 | `"            cursor = db.execute("` | — |
| [SRC-C9CF9B54F8-L000856](../../agents/omarai.py#L856) | 856 | `"                \"\"\"UPDATE web_sessions SET revoked_at=?"` | — |
| [SRC-C9CF9B54F8-L000857](../../agents/omarai.py#L857) | 857 | `"                   WHERE session_hash=? AND revoked_at IS NULL\"\"\","` | — |
| [SRC-C9CF9B54F8-L000858](../../agents/omarai.py#L858) | 858 | `"                (now_utc(), self._token_hash(session_id)),"` | — |
| [SRC-C9CF9B54F8-L000859](../../agents/omarai.py#L859) | 859 | `"            )"` | — |
| [SRC-C9CF9B54F8-L000860](../../agents/omarai.py#L860) | 860 | `"        return cursor.rowcount == 1"` | — |
| [SRC-C9CF9B54F8-L000861](../../agents/omarai.py#L861) | 861 | `""` | — |
| [SRC-C9CF9B54F8-L000862](../../agents/omarai.py#L862) | 862 | `"    def revoke_api_token("` | — |
| [SRC-C9CF9B54F8-L000863](../../agents/omarai.py#L863) | 863 | `"        self,"` | — |
| [SRC-C9CF9B54F8-L000864](../../agents/omarai.py#L864) | 864 | `"        token: str,"` | — |
| [SRC-C9CF9B54F8-L000865](../../agents/omarai.py#L865) | 865 | `"        *,"` | — |
| [SRC-C9CF9B54F8-L000866](../../agents/omarai.py#L866) | 866 | `"        tenant_id: str,"` | — |
| [SRC-C9CF9B54F8-L000867](../../agents/omarai.py#L867) | 867 | `"        user_id: str,"` | — |
| [SRC-C9CF9B54F8-L000868](../../agents/omarai.py#L868) | 868 | `"    ) -> bool:"` | — |
| [SRC-C9CF9B54F8-L000869](../../agents/omarai.py#L869) | 869 | `"        \"\"\"Revoke only a token owned by the authenticated user in the active tenant.\"\"\""` | — |
| [SRC-C9CF9B54F8-L000870](../../agents/omarai.py#L870) | 870 | `"        if not isinstance(token, str) or len(token.strip()) < 32:"` | — |
| [SRC-C9CF9B54F8-L000871](../../agents/omarai.py#L871) | 871 | `"            return False"` | — |
| [SRC-C9CF9B54F8-L000872](../../agents/omarai.py#L872) | 872 | `"        tenant = self._tenant(tenant_id)"` | — |
| [SRC-C9CF9B54F8-L000873](../../agents/omarai.py#L873) | 873 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000874](../../agents/omarai.py#L874) | 874 | `"            membership = db.execute("` | — |
| [SRC-C9CF9B54F8-L000875](../../agents/omarai.py#L875) | 875 | `"                \"\"\"SELECT 1 FROM tenant_memberships m"` | — |
| [SRC-C9CF9B54F8-L000876](../../agents/omarai.py#L876) | 876 | `"                   JOIN tenants t ON t.id=m.tenant_id AND t.active=1"` | — |
| [SRC-C9CF9B54F8-L000877](../../agents/omarai.py#L877) | 877 | `"                   JOIN users u ON u.id=m.user_id AND u.active=1"` | — |
| [SRC-C9CF9B54F8-L000878](../../agents/omarai.py#L878) | 878 | `"                   WHERE m.tenant_id=? AND m.user_id=? AND m.active=1\"\"\","` | — |
| [SRC-C9CF9B54F8-L000879](../../agents/omarai.py#L879) | 879 | `"                (tenant, user_id),"` | — |
| [SRC-C9CF9B54F8-L000880](../../agents/omarai.py#L880) | 880 | `"            ).fetchone()"` | — |
| [SRC-C9CF9B54F8-L000881](../../agents/omarai.py#L881) | 881 | `"            if not membership:"` | — |
| [SRC-C9CF9B54F8-L000882](../../agents/omarai.py#L882) | 882 | `"                return False"` | — |
| [SRC-C9CF9B54F8-L000883](../../agents/omarai.py#L883) | 883 | `"            cursor = db.execute("` | — |
| [SRC-C9CF9B54F8-L000884](../../agents/omarai.py#L884) | 884 | `"                \"\"\"UPDATE api_tokens SET active=0"` | — |
| [SRC-C9CF9B54F8-L000885](../../agents/omarai.py#L885) | 885 | `"                   WHERE token_hash=? AND tenant_id=? AND user_id=? AND active=1\"\"\","` | — |
| [SRC-C9CF9B54F8-L000886](../../agents/omarai.py#L886) | 886 | `"                (self._token_hash(token.strip()), tenant, user_id),"` | — |
| [SRC-C9CF9B54F8-L000887](../../agents/omarai.py#L887) | 887 | `"            )"` | — |
| [SRC-C9CF9B54F8-L000888](../../agents/omarai.py#L888) | 888 | `"        return cursor.rowcount == 1"` | — |
| [SRC-C9CF9B54F8-L000889](../../agents/omarai.py#L889) | 889 | `""` | — |
| [SRC-C9CF9B54F8-L000890](../../agents/omarai.py#L890) | 890 | `"    def add("` | — |
| [SRC-C9CF9B54F8-L000891](../../agents/omarai.py#L891) | 891 | `"        self,"` | — |
| [SRC-C9CF9B54F8-L000892](../../agents/omarai.py#L892) | 892 | `"        text: str,"` | — |
| [SRC-C9CF9B54F8-L000893](../../agents/omarai.py#L893) | 893 | `"        source_url: str,"` | — |
| [SRC-C9CF9B54F8-L000894](../../agents/omarai.py#L894) | 894 | `"        platform: str = \"manual\","` | — |
| [SRC-C9CF9B54F8-L000895](../../agents/omarai.py#L895) | 895 | `"        observed_at: str \| None = None,"` | — |
| [SRC-C9CF9B54F8-L000896](../../agents/omarai.py#L896) | 896 | `"        note: str = \"\","` | — |
| [SRC-C9CF9B54F8-L000897](../../agents/omarai.py#L897) | 897 | `"        product_terms=(),"` | — |
| [SRC-C9CF9B54F8-L000898](../../agents/omarai.py#L898) | 898 | `"        location_terms=(),"` | — |
| [SRC-C9CF9B54F8-L000899](../../agents/omarai.py#L899) | 899 | `"        *,"` | — |
| [SRC-C9CF9B54F8-L000900](../../agents/omarai.py#L900) | 900 | `"        tenant_id: str \| None = None,"` | — |
| [SRC-C9CF9B54F8-L000901](../../agents/omarai.py#L901) | 901 | `"    ):"` | — |
| [SRC-C9CF9B54F8-L000902](../../agents/omarai.py#L902) | 902 | `"        if not isinstance(text, str) or not text.strip():"` | — |
| [SRC-C9CF9B54F8-L000903](../../agents/omarai.py#L903) | 903 | `"            raise ValueError(\"text is required\")"` | — |
| [SRC-C9CF9B54F8-L000904](../../agents/omarai.py#L904) | 904 | `"        if len(text) > MAX_TEXT:"` | — |
| [SRC-C9CF9B54F8-L000905](../../agents/omarai.py#L905) | 905 | `"            raise ValueError(\"text is too long\")"` | — |
| [SRC-C9CF9B54F8-L000906](../../agents/omarai.py#L906) | 906 | `"        tenant = self._tenant(tenant_id)"` | — |
| [SRC-C9CF9B54F8-L000907](../../agents/omarai.py#L907) | 907 | `"        url = validate_url(source_url)"` | — |
| [SRC-C9CF9B54F8-L000908](../../agents/omarai.py#L908) | 908 | `"        normalized = normalize(text)"` | — |
| [SRC-C9CF9B54F8-L000909](../../agents/omarai.py#L909) | 909 | `"        fingerprint = hashlib.sha256("` | — |
| [SRC-C9CF9B54F8-L000910](../../agents/omarai.py#L910) | 910 | `"            (url.rstrip(\"/\") + \"\\n\" + normalized).encode()"` | — |
| [SRC-C9CF9B54F8-L000911](../../agents/omarai.py#L911) | 911 | `"        ).hexdigest()"` | — |
| [SRC-C9CF9B54F8-L000912](../../agents/omarai.py#L912) | 912 | `"        lead_id = hashlib.sha256("` | — |
| [SRC-C9CF9B54F8-L000913](../../agents/omarai.py#L913) | 913 | `"            (tenant + \"\\n\" + fingerprint).encode()"` | — |
| [SRC-C9CF9B54F8-L000914](../../agents/omarai.py#L914) | 914 | `"        ).hexdigest()[:24]"` | — |
| [SRC-C9CF9B54F8-L000915](../../agents/omarai.py#L915) | 915 | `"        timestamp = observed_at or now_utc()"` | — |
| [SRC-C9CF9B54F8-L000916](../../agents/omarai.py#L916) | 916 | `"        assessment = analyze(text, product_terms=product_terms, location_terms=location_terms)"` | — |
| [SRC-C9CF9B54F8-L000917](../../agents/omarai.py#L917) | 917 | `"        domain_observed_at = timestamp"` | — |
| [SRC-C9CF9B54F8-L000918](../../agents/omarai.py#L918) | 918 | `"        try:"` | — |
| [SRC-C9CF9B54F8-L000919](../../agents/omarai.py#L919) | 919 | `"            parsed_observed_at = datetime.fromisoformat(str(timestamp))"` | — |
| [SRC-C9CF9B54F8-L000920](../../agents/omarai.py#L920) | 920 | `"            if parsed_observed_at.tzinfo is None:"` | — |
| [SRC-C9CF9B54F8-L000921](../../agents/omarai.py#L921) | 921 | `"                domain_observed_at = None"` | — |
| [SRC-C9CF9B54F8-L000922](../../agents/omarai.py#L922) | 922 | `"        except (TypeError, ValueError):"` | — |
| [SRC-C9CF9B54F8-L000923](../../agents/omarai.py#L923) | 923 | `"            domain_observed_at = None"` | — |
| [SRC-C9CF9B54F8-L000924](../../agents/omarai.py#L924) | 924 | `"        evidence = DemandEvidence("` | — |
| [SRC-C9CF9B54F8-L000925](../../agents/omarai.py#L925) | 925 | `"            source_id=lead_id,"` | — |
| [SRC-C9CF9B54F8-L000926](../../agents/omarai.py#L926) | 926 | `"            source_url=url,"` | — |
| [SRC-C9CF9B54F8-L000927](../../agents/omarai.py#L927) | 927 | `"            excerpt=text.strip()[:2_000],"` | — |
| [SRC-C9CF9B54F8-L000928](../../agents/omarai.py#L928) | 928 | `"            content_basis=EvidenceBasis.USER_PROVIDED,"` | — |
| [SRC-C9CF9B54F8-L000929](../../agents/omarai.py#L929) | 929 | `"            observed_at=domain_observed_at,"` | — |
| [SRC-C9CF9B54F8-L000930](../../agents/omarai.py#L930) | 930 | `"            page_read=False,"` | — |
| [SRC-C9CF9B54F8-L000931](../../agents/omarai.py#L931) | 931 | `"        )"` | — |
| [SRC-C9CF9B54F8-L000932](../../agents/omarai.py#L932) | 932 | `"        domain_signal = DemandSignal("` | — |
| [SRC-C9CF9B54F8-L000933](../../agents/omarai.py#L933) | 933 | `"            signal_id=lead_id,"` | — |
| [SRC-C9CF9B54F8-L000934](../../agents/omarai.py#L934) | 934 | `"            signal_type=DemandSignalType(assessment[\"signal_type\"]),"` | — |
| [SRC-C9CF9B54F8-L000935](../../agents/omarai.py#L935) | 935 | `"            evidence=evidence,"` | — |
| [SRC-C9CF9B54F8-L000936](../../agents/omarai.py#L936) | 936 | `"            product_fit=ProductFit.UNASSESSED,"` | — |
| [SRC-C9CF9B54F8-L000937](../../agents/omarai.py#L937) | 937 | `"            identity_status=IdentityStatus.UNKNOWN,"` | — |
| [SRC-C9CF9B54F8-L000938](../../agents/omarai.py#L938) | 938 | `"            classification_reason=assessment[\"summary\"],"` | — |
| [SRC-C9CF9B54F8-L000939](../../agents/omarai.py#L939) | 939 | `"        )"` | — |
| [SRC-C9CF9B54F8-L000940](../../agents/omarai.py#L940) | 940 | `"        qualification = LeadQualification("` | — |
| [SRC-C9CF9B54F8-L000941](../../agents/omarai.py#L941) | 941 | `"            signal_id=lead_id,"` | — |
| [SRC-C9CF9B54F8-L000942](../../agents/omarai.py#L942) | 942 | `"            product_fit=ProductFit.UNASSESSED,"` | — |
| [SRC-C9CF9B54F8-L000943](../../agents/omarai.py#L943) | 943 | `"            source_quality=SourceQuality.UNKNOWN,"` | — |
| [SRC-C9CF9B54F8-L000944](../../agents/omarai.py#L944) | 944 | `"            freshness=FreshnessStatus.UNKNOWN,"` | — |
| [SRC-C9CF9B54F8-L000945](../../agents/omarai.py#L945) | 945 | `"            identity_status=IdentityStatus.UNKNOWN,"` | — |
| [SRC-C9CF9B54F8-L000946](../../agents/omarai.py#L946) | 946 | `"            contactability=ContactabilityStatus.NOT_ASSESSED,"` | — |
| [SRC-C9CF9B54F8-L000947](../../agents/omarai.py#L947) | 947 | `"            missing_information=("` | — |
| [SRC-C9CF9B54F8-L000948](../../agents/omarai.py#L948) | 948 | `"                \"product_fit\", \"source_quality\", \"freshness\","` | — |
| [SRC-C9CF9B54F8-L000949](../../agents/omarai.py#L949) | 949 | `"                \"identity\", \"contactability\","` | — |
| [SRC-C9CF9B54F8-L000950](../../agents/omarai.py#L950) | 950 | `"            ),"` | — |
| [SRC-C9CF9B54F8-L000951](../../agents/omarai.py#L951) | 951 | `"        )"` | — |
| [SRC-C9CF9B54F8-L000952](../../agents/omarai.py#L952) | 952 | `"        assessment[\"domain_signal\"] = domain_signal.to_dict()"` | — |
| [SRC-C9CF9B54F8-L000953](../../agents/omarai.py#L953) | 953 | `"        assessment[\"qualification\"] = qualification.to_dict()"` | — |
| [SRC-C9CF9B54F8-L000954](../../agents/omarai.py#L954) | 954 | `"        now = now_utc()"` | — |
| [SRC-C9CF9B54F8-L000955](../../agents/omarai.py#L955) | 955 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000956](../../agents/omarai.py#L956) | 956 | `"            active_tenant = db.execute("` | — |
| [SRC-C9CF9B54F8-L000957](../../agents/omarai.py#L957) | 957 | `"                \"SELECT 1 FROM tenants WHERE id=? AND active=1\", (tenant,)"` | — |
| [SRC-C9CF9B54F8-L000958](../../agents/omarai.py#L958) | 958 | `"            ).fetchone()"` | — |
| [SRC-C9CF9B54F8-L000959](../../agents/omarai.py#L959) | 959 | `"            if not active_tenant:"` | — |
| [SRC-C9CF9B54F8-L000960](../../agents/omarai.py#L960) | 960 | `"                raise ValueError(\"active tenant is required\")"` | — |
| [SRC-C9CF9B54F8-L000961](../../agents/omarai.py#L961) | 961 | `"            cursor = db.execute("` | — |
| [SRC-C9CF9B54F8-L000962](../../agents/omarai.py#L962) | 962 | `"                \"\"\"INSERT OR IGNORE INTO leads"` | — |
| [SRC-C9CF9B54F8-L000963](../../agents/omarai.py#L963) | 963 | `"                   (id, tenant_id, fingerprint, text, source_url, platform, observed_at,"` | — |
| [SRC-C9CF9B54F8-L000964](../../agents/omarai.py#L964) | 964 | `"                    assessment, status, note, created_at, updated_at)"` | — |
| [SRC-C9CF9B54F8-L000965](../../agents/omarai.py#L965) | 965 | `"                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)\"\"\","` | — |
| [SRC-C9CF9B54F8-L000966](../../agents/omarai.py#L966) | 966 | `"                ("` | — |
| [SRC-C9CF9B54F8-L000967](../../agents/omarai.py#L967) | 967 | `"                    lead_id, tenant, fingerprint, text.strip(), url,"` | — |
| [SRC-C9CF9B54F8-L000968](../../agents/omarai.py#L968) | 968 | `"                    str(platform)[:80], timestamp,"` | — |
| [SRC-C9CF9B54F8-L000969](../../agents/omarai.py#L969) | 969 | `"                    json.dumps(assessment, ensure_ascii=False), \"new\","` | — |
| [SRC-C9CF9B54F8-L000970](../../agents/omarai.py#L970) | 970 | `"                    str(note)[:1000], now, now,"` | — |
| [SRC-C9CF9B54F8-L000971](../../agents/omarai.py#L971) | 971 | `"                ),"` | — |
| [SRC-C9CF9B54F8-L000972](../../agents/omarai.py#L972) | 972 | `"            )"` | — |
| [SRC-C9CF9B54F8-L000973](../../agents/omarai.py#L973) | 973 | `"            row = db.execute("` | — |
| [SRC-C9CF9B54F8-L000974](../../agents/omarai.py#L974) | 974 | `"                \"SELECT * FROM leads WHERE tenant_id=? AND fingerprint=?\","` | — |
| [SRC-C9CF9B54F8-L000975](../../agents/omarai.py#L975) | 975 | `"                (tenant, fingerprint),"` | — |
| [SRC-C9CF9B54F8-L000976](../../agents/omarai.py#L976) | 976 | `"            ).fetchone()"` | — |
| [SRC-C9CF9B54F8-L000977](../../agents/omarai.py#L977) | 977 | `"        return self.to_dict(row), cursor.rowcount == 1"` | — |
| [SRC-C9CF9B54F8-L000978](../../agents/omarai.py#L978) | 978 | `""` | — |
| [SRC-C9CF9B54F8-L000979](../../agents/omarai.py#L979) | 979 | `"    @staticmethod"` | — |
| [SRC-C9CF9B54F8-L000980](../../agents/omarai.py#L980) | 980 | `"    def to_dict(row):"` | — |
| [SRC-C9CF9B54F8-L000981](../../agents/omarai.py#L981) | 981 | `"        item = dict(row)"` | — |
| [SRC-C9CF9B54F8-L000982](../../agents/omarai.py#L982) | 982 | `"        item[\"assessment\"] = json.loads(item[\"assessment\"])"` | — |
| [SRC-C9CF9B54F8-L000983](../../agents/omarai.py#L983) | 983 | `"        return item"` | — |
| [SRC-C9CF9B54F8-L000984](../../agents/omarai.py#L984) | 984 | `""` | — |
| [SRC-C9CF9B54F8-L000985](../../agents/omarai.py#L985) | 985 | `"    def list("` | — |
| [SRC-C9CF9B54F8-L000986](../../agents/omarai.py#L986) | 986 | `"        self,"` | — |
| [SRC-C9CF9B54F8-L000987](../../agents/omarai.py#L987) | 987 | `"        status: str \| None = None,"` | — |
| [SRC-C9CF9B54F8-L000988](../../agents/omarai.py#L988) | 988 | `"        limit: int = 100,"` | — |
| [SRC-C9CF9B54F8-L000989](../../agents/omarai.py#L989) | 989 | `"        *,"` | — |
| [SRC-C9CF9B54F8-L000990](../../agents/omarai.py#L990) | 990 | `"        tenant_id: str \| None = None,"` | — |
| [SRC-C9CF9B54F8-L000991](../../agents/omarai.py#L991) | 991 | `"    ):"` | — |
| [SRC-C9CF9B54F8-L000992](../../agents/omarai.py#L992) | 992 | `"        tenant = self._tenant(tenant_id)"` | — |
| [SRC-C9CF9B54F8-L000993](../../agents/omarai.py#L993) | 993 | `"        limit = max(1, min(int(limit), 500))"` | — |
| [SRC-C9CF9B54F8-L000994](../../agents/omarai.py#L994) | 994 | `"        query = \"SELECT * FROM leads WHERE tenant_id=?\""` | — |
| [SRC-C9CF9B54F8-L000995](../../agents/omarai.py#L995) | 995 | `"        params: list[object] = [tenant]"` | — |
| [SRC-C9CF9B54F8-L000996](../../agents/omarai.py#L996) | 996 | `"        if status is not None:"` | — |
| [SRC-C9CF9B54F8-L000997](../../agents/omarai.py#L997) | 997 | `"            query += \" AND status=?\""` | — |
| [SRC-C9CF9B54F8-L000998](../../agents/omarai.py#L998) | 998 | `"            params.append(status)"` | — |
| [SRC-C9CF9B54F8-L000999](../../agents/omarai.py#L999) | 999 | `"        query += \" ORDER BY created_at DESC LIMIT ?\""` | — |
| [SRC-C9CF9B54F8-L001000](../../agents/omarai.py#L1000) | 1000 | `"        params.append(limit)"` | — |
| [SRC-C9CF9B54F8-L001001](../../agents/omarai.py#L1001) | 1001 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L001002](../../agents/omarai.py#L1002) | 1002 | `"            rows = db.execute(query, tuple(params)).fetchall()"` | — |
| [SRC-C9CF9B54F8-L001003](../../agents/omarai.py#L1003) | 1003 | `"        return [self.to_dict(row) for row in rows]"` | — |
| [SRC-C9CF9B54F8-L001004](../../agents/omarai.py#L1004) | 1004 | `""` | — |
| [SRC-C9CF9B54F8-L001005](../../agents/omarai.py#L1005) | 1005 | `"    def update_status("` | — |
| [SRC-C9CF9B54F8-L001006](../../agents/omarai.py#L1006) | 1006 | `"        self,"` | — |
| [SRC-C9CF9B54F8-L001007](../../agents/omarai.py#L1007) | 1007 | `"        lead_id: str,"` | — |
| [SRC-C9CF9B54F8-L001008](../../agents/omarai.py#L1008) | 1008 | `"        status: str,"` | — |
| [SRC-C9CF9B54F8-L001009](../../agents/omarai.py#L1009) | 1009 | `"        *,"` | — |
| [SRC-C9CF9B54F8-L001010](../../agents/omarai.py#L1010) | 1010 | `"        tenant_id: str \| None = None,"` | — |
| [SRC-C9CF9B54F8-L001011](../../agents/omarai.py#L1011) | 1011 | `"    ):"` | — |
| [SRC-C9CF9B54F8-L001012](../../agents/omarai.py#L1012) | 1012 | `"        if status not in self.ALLOWED_STATUSES:"` | — |
| [SRC-C9CF9B54F8-L001013](../../agents/omarai.py#L1013) | 1013 | `"            raise ValueError(\"unsupported status\")"` | — |
| [SRC-C9CF9B54F8-L001014](../../agents/omarai.py#L1014) | 1014 | `"        tenant = self._tenant(tenant_id)"` | — |
| [SRC-C9CF9B54F8-L001015](../../agents/omarai.py#L1015) | 1015 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L001016](../../agents/omarai.py#L1016) | 1016 | `"            db.execute("` | — |
| [SRC-C9CF9B54F8-L001017](../../agents/omarai.py#L1017) | 1017 | `"                \"UPDATE leads SET status=?, updated_at=? WHERE id=? AND tenant_id=?\","` | — |
| [SRC-C9CF9B54F8-L001018](../../agents/omarai.py#L1018) | 1018 | `"                (status, now_utc(), lead_id, tenant),"` | — |
| [SRC-C9CF9B54F8-L001019](../../agents/omarai.py#L1019) | 1019 | `"            )"` | — |
| [SRC-C9CF9B54F8-L001020](../../agents/omarai.py#L1020) | 1020 | `"            row = db.execute("` | — |
| [SRC-C9CF9B54F8-L001021](../../agents/omarai.py#L1021) | 1021 | `"                \"SELECT * FROM leads WHERE id=? AND tenant_id=?\","` | — |
| [SRC-C9CF9B54F8-L001022](../../agents/omarai.py#L1022) | 1022 | `"                (lead_id, tenant),"` | — |
| [SRC-C9CF9B54F8-L001023](../../agents/omarai.py#L1023) | 1023 | `"            ).fetchone()"` | — |
| [SRC-C9CF9B54F8-L001024](../../agents/omarai.py#L1024) | 1024 | `"        return self.to_dict(row) if row else None"` | — |
| [SRC-C9CF9B54F8-L001025](../../agents/omarai.py#L1025) | 1025 | `""` | — |
| [SRC-C9CF9B54F8-L001026](../../agents/omarai.py#L1026) | 1026 | `"    @staticmethod"` | — |
| [SRC-C9CF9B54F8-L001027](../../agents/omarai.py#L1027) | 1027 | `"    def _product_profile_row(row):"` | — |
| [SRC-C9CF9B54F8-L001028](../../agents/omarai.py#L1028) | 1028 | `"        if row is None:"` | — |
| [SRC-C9CF9B54F8-L001029](../../agents/omarai.py#L1029) | 1029 | `"            return None"` | — |
| [SRC-C9CF9B54F8-L001030](../../agents/omarai.py#L1030) | 1030 | `"        return {"` | — |
| [SRC-C9CF9B54F8-L001031](../../agents/omarai.py#L1031) | 1031 | `"            \"id\": row[\"id\"],"` | — |
| [SRC-C9CF9B54F8-L001032](../../agents/omarai.py#L1032) | 1032 | `"            \"name\": row[\"name\"],"` | — |
| [SRC-C9CF9B54F8-L001033](../../agents/omarai.py#L1033) | 1033 | `"            \"profile\": json.loads(row[\"profile_json\"]),"` | — |
| [SRC-C9CF9B54F8-L001034](../../agents/omarai.py#L1034) | 1034 | `"            \"created_at\": row[\"created_at\"],"` | — |
| [SRC-C9CF9B54F8-L001035](../../agents/omarai.py#L1035) | 1035 | `"            \"updated_at\": row[\"updated_at\"],"` | — |
| [SRC-C9CF9B54F8-L001036](../../agents/omarai.py#L1036) | 1036 | `"        }"` | — |
| [SRC-C9CF9B54F8-L001037](../../agents/omarai.py#L1037) | 1037 | `""` | — |
| [SRC-C9CF9B54F8-L001038](../../agents/omarai.py#L1038) | 1038 | `"    def save_product_profile(self, profile: dict, *, tenant_id: str):"` | — |
| [SRC-C9CF9B54F8-L001039](../../agents/omarai.py#L1039) | 1039 | `"        if not isinstance(profile, dict):"` | — |
| [SRC-C9CF9B54F8-L001040](../../agents/omarai.py#L1040) | 1040 | `"            raise TypeError(\"profile must be an object\")"` | — |
| [SRC-C9CF9B54F8-L001041](../../agents/omarai.py#L1041) | 1041 | `"        product = profile.get(\"product\")"` | — |
| [SRC-C9CF9B54F8-L001042](../../agents/omarai.py#L1042) | 1042 | `"        if not isinstance(product, dict):"` | — |
| [SRC-C9CF9B54F8-L001043](../../agents/omarai.py#L1043) | 1043 | `"            raise TypeError(\"product profile is required\")"` | — |
| [SRC-C9CF9B54F8-L001044](../../agents/omarai.py#L1044) | 1044 | `"        name = str(product.get(\"name\") or \"\").strip()"` | — |
| [SRC-C9CF9B54F8-L001045](../../agents/omarai.py#L1045) | 1045 | `"        if not name or len(name) > 240:"` | — |
| [SRC-C9CF9B54F8-L001046](../../agents/omarai.py#L1046) | 1046 | `"            raise ValueError(\"product name is required and must be at most 240 characters\")"` | — |
| [SRC-C9CF9B54F8-L001047](../../agents/omarai.py#L1047) | 1047 | `"        normalized_name = normalize(name)"` | — |
| [SRC-C9CF9B54F8-L001048](../../agents/omarai.py#L1048) | 1048 | `"        if not normalized_name:"` | — |
| [SRC-C9CF9B54F8-L001049](../../agents/omarai.py#L1049) | 1049 | `"            raise ValueError(\"product name is invalid\")"` | — |
| [SRC-C9CF9B54F8-L001050](../../agents/omarai.py#L1050) | 1050 | `"        encoded = json.dumps(profile, ensure_ascii=False, separators=(\",\", \":\"))"` | — |
| [SRC-C9CF9B54F8-L001051](../../agents/omarai.py#L1051) | 1051 | `"        if len(encoded) > 30000:"` | — |
| [SRC-C9CF9B54F8-L001052](../../agents/omarai.py#L1052) | 1052 | `"            raise ValueError(\"product profile is too large\")"` | — |
| [SRC-C9CF9B54F8-L001053](../../agents/omarai.py#L1053) | 1053 | `"        tenant = self._tenant(tenant_id)"` | — |
| [SRC-C9CF9B54F8-L001054](../../agents/omarai.py#L1054) | 1054 | `"        now = now_utc()"` | — |
| [SRC-C9CF9B54F8-L001055](../../agents/omarai.py#L1055) | 1055 | `"        profile_id = \"profile_\" + uuid.uuid4().hex"` | — |
| [SRC-C9CF9B54F8-L001056](../../agents/omarai.py#L1056) | 1056 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L001057](../../agents/omarai.py#L1057) | 1057 | `"            active_tenant = db.execute("` | — |
| [SRC-C9CF9B54F8-L001058](../../agents/omarai.py#L1058) | 1058 | `"                \"SELECT 1 FROM tenants WHERE id=? AND active=1\", (tenant,)"` | — |
| [SRC-C9CF9B54F8-L001059](../../agents/omarai.py#L1059) | 1059 | `"            ).fetchone()"` | — |
| [SRC-C9CF9B54F8-L001060](../../agents/omarai.py#L1060) | 1060 | `"            if not active_tenant:"` | — |
| [SRC-C9CF9B54F8-L001061](../../agents/omarai.py#L1061) | 1061 | `"                raise ValueError(\"active tenant is required\")"` | — |
| [SRC-C9CF9B54F8-L001062](../../agents/omarai.py#L1062) | 1062 | `"            db.execute("` | — |
| [SRC-C9CF9B54F8-L001063](../../agents/omarai.py#L1063) | 1063 | `"                \"\"\"INSERT INTO product_profiles"` | — |
| [SRC-C9CF9B54F8-L001064](../../agents/omarai.py#L1064) | 1064 | `"                   (id, tenant_id, normalized_name, name, profile_json, created_at, updated_at)"` | — |
| [SRC-C9CF9B54F8-L001065](../../agents/omarai.py#L1065) | 1065 | `"                   VALUES (?, ?, ?, ?, ?, ?, ?)"` | — |
| [SRC-C9CF9B54F8-L001066](../../agents/omarai.py#L1066) | 1066 | `"                   ON CONFLICT(tenant_id, normalized_name)"` | — |
| [SRC-C9CF9B54F8-L001067](../../agents/omarai.py#L1067) | 1067 | `"                   DO UPDATE SET name=excluded.name,"` | — |
| [SRC-C9CF9B54F8-L001068](../../agents/omarai.py#L1068) | 1068 | `"                                 profile_json=excluded.profile_json,"` | — |
| [SRC-C9CF9B54F8-L001069](../../agents/omarai.py#L1069) | 1069 | `"                                 updated_at=excluded.updated_at\"\"\","` | — |
| [SRC-C9CF9B54F8-L001070](../../agents/omarai.py#L1070) | 1070 | `"                (profile_id, tenant, normalized_name, name, encoded, now, now),"` | — |
| [SRC-C9CF9B54F8-L001071](../../agents/omarai.py#L1071) | 1071 | `"            )"` | — |
| [SRC-C9CF9B54F8-L001072](../../agents/omarai.py#L1072) | 1072 | `"            row = db.execute("` | — |
| [SRC-C9CF9B54F8-L001073](../../agents/omarai.py#L1073) | 1073 | `"                \"\"\"SELECT id, name, profile_json, created_at, updated_at"` | — |
| [SRC-C9CF9B54F8-L001074](../../agents/omarai.py#L1074) | 1074 | `"                   FROM product_profiles"` | — |
| [SRC-C9CF9B54F8-L001075](../../agents/omarai.py#L1075) | 1075 | `"                   WHERE tenant_id=? AND normalized_name=?\"\"\","` | — |
| [SRC-C9CF9B54F8-L001076](../../agents/omarai.py#L1076) | 1076 | `"                (tenant, normalized_name),"` | — |
| [SRC-C9CF9B54F8-L001077](../../agents/omarai.py#L1077) | 1077 | `"            ).fetchone()"` | — |
| [SRC-C9CF9B54F8-L001078](../../agents/omarai.py#L1078) | 1078 | `"        return self._product_profile_row(row)"` | — |
| [SRC-C9CF9B54F8-L001079](../../agents/omarai.py#L1079) | 1079 | `""` | — |
| [SRC-C9CF9B54F8-L001080](../../agents/omarai.py#L1080) | 1080 | `"    def list_product_profiles(self, *, tenant_id: str):"` | — |
| [SRC-C9CF9B54F8-L001081](../../agents/omarai.py#L1081) | 1081 | `"        tenant = self._tenant(tenant_id)"` | — |
| [SRC-C9CF9B54F8-L001082](../../agents/omarai.py#L1082) | 1082 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L001083](../../agents/omarai.py#L1083) | 1083 | `"            rows = db.execute("` | — |
| [SRC-C9CF9B54F8-L001084](../../agents/omarai.py#L1084) | 1084 | `"                \"\"\"SELECT id, name, profile_json, created_at, updated_at"` | — |
| [SRC-C9CF9B54F8-L001085](../../agents/omarai.py#L1085) | 1085 | `"                   FROM product_profiles WHERE tenant_id=?"` | — |
| [SRC-C9CF9B54F8-L001086](../../agents/omarai.py#L1086) | 1086 | `"                   ORDER BY updated_at DESC, id LIMIT 100\"\"\","` | — |
| [SRC-C9CF9B54F8-L001087](../../agents/omarai.py#L1087) | 1087 | `"                (tenant,),"` | — |
| [SRC-C9CF9B54F8-L001088](../../agents/omarai.py#L1088) | 1088 | `"            ).fetchall()"` | — |
| [SRC-C9CF9B54F8-L001089](../../agents/omarai.py#L1089) | 1089 | `"        return [self._product_profile_row(row) for row in rows]"` | — |
| [SRC-C9CF9B54F8-L001090](../../agents/omarai.py#L1090) | 1090 | `""` | — |
| [SRC-C9CF9B54F8-L001091](../../agents/omarai.py#L1091) | 1091 | `"    def get_product_profile(self, profile_id: str, *, tenant_id: str):"` | — |
| [SRC-C9CF9B54F8-L001092](../../agents/omarai.py#L1092) | 1092 | `"        if not isinstance(profile_id, str) or not profile_id.strip():"` | — |
| [SRC-C9CF9B54F8-L001093](../../agents/omarai.py#L1093) | 1093 | `"            return None"` | — |
| [SRC-C9CF9B54F8-L001094](../../agents/omarai.py#L1094) | 1094 | `"        tenant = self._tenant(tenant_id)"` | — |
| [SRC-C9CF9B54F8-L001095](../../agents/omarai.py#L1095) | 1095 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L001096](../../agents/omarai.py#L1096) | 1096 | `"            row = db.execute("` | — |
| [SRC-C9CF9B54F8-L001097](../../agents/omarai.py#L1097) | 1097 | `"                \"\"\"SELECT id, name, profile_json, created_at, updated_at"` | — |
| [SRC-C9CF9B54F8-L001098](../../agents/omarai.py#L1098) | 1098 | `"                   FROM product_profiles WHERE id=? AND tenant_id=?\"\"\","` | — |
| [SRC-C9CF9B54F8-L001099](../../agents/omarai.py#L1099) | 1099 | `"                (profile_id.strip(), tenant),"` | — |
| [SRC-C9CF9B54F8-L001100](../../agents/omarai.py#L1100) | 1100 | `"            ).fetchone()"` | — |
| [SRC-C9CF9B54F8-L001101](../../agents/omarai.py#L1101) | 1101 | `"        return self._product_profile_row(row)"` | — |
| [SRC-C9CF9B54F8-L001102](../../agents/omarai.py#L1102) | 1102 | `""` | — |
| [SRC-C9CF9B54F8-L001103](../../agents/omarai.py#L1103) | 1103 | `"    @staticmethod"` | — |
| [SRC-C9CF9B54F8-L001104](../../agents/omarai.py#L1104) | 1104 | `"    def _safe_discovery_source(source: dict):"` | — |
| [SRC-C9CF9B54F8-L001105](../../agents/omarai.py#L1105) | 1105 | `"        from urllib.parse import urlparse"` | — |
| [SRC-C9CF9B54F8-L001106](../../agents/omarai.py#L1106) | 1106 | `""` | — |
| [SRC-C9CF9B54F8-L001107](../../agents/omarai.py#L1107) | 1107 | `"        title = str(source.get(\"title\") or \"\")[:300].strip()"` | — |
| [SRC-C9CF9B54F8-L001108](../../agents/omarai.py#L1108) | 1108 | `"        snippet = str(source.get(\"snippet\") or \"\")[:1600].strip()"` | — |
| [SRC-C9CF9B54F8-L001109](../../agents/omarai.py#L1109) | 1109 | `"        source_url = validate_url(source.get(\"url\", \"\"))"` | — |
| [SRC-C9CF9B54F8-L001110](../../agents/omarai.py#L1110) | 1110 | `"        parsed = urlparse(source_url)"` | — |
| [SRC-C9CF9B54F8-L001111](../../agents/omarai.py#L1111) | 1111 | `"        hostname = (parsed.hostname or \"\").lower().rstrip(\".\")"` | — |
| [SRC-C9CF9B54F8-L001112](../../agents/omarai.py#L1112) | 1112 | `"        if hostname == \"localhost\" or hostname.endswith((\".localhost\", \".local\")):"` | — |
| [SRC-C9CF9B54F8-L001113](../../agents/omarai.py#L1113) | 1113 | `"            raise ValueError(\"discovery source URL is not public\")"` | — |
| [SRC-C9CF9B54F8-L001114](../../agents/omarai.py#L1114) | 1114 | `"        try:"` | — |
| [SRC-C9CF9B54F8-L001115](../../agents/omarai.py#L1115) | 1115 | `"            address = ipaddress.ip_address(hostname)"` | — |
| [SRC-C9CF9B54F8-L001116](../../agents/omarai.py#L1116) | 1116 | `"        except ValueError:"` | — |
| [SRC-C9CF9B54F8-L001117](../../agents/omarai.py#L1117) | 1117 | `"            address = None"` | — |
| [SRC-C9CF9B54F8-L001118](../../agents/omarai.py#L1118) | 1118 | `"        if address is not None and not address.is_global:"` | — |
| [SRC-C9CF9B54F8-L001119](../../agents/omarai.py#L1119) | 1119 | `"            raise ValueError(\"discovery source URL is not public\")"` | — |
| [SRC-C9CF9B54F8-L001120](../../agents/omarai.py#L1120) | 1120 | `"        evidence = source.get(\"lead_intent_evidence\")"` | — |
| [SRC-C9CF9B54F8-L001121](../../agents/omarai.py#L1121) | 1121 | `"        safe_evidence = None"` | — |
| [SRC-C9CF9B54F8-L001122](../../agents/omarai.py#L1122) | 1122 | `"        if isinstance(evidence, dict):"` | — |
| [SRC-C9CF9B54F8-L001123](../../agents/omarai.py#L1123) | 1123 | `"            safe_evidence = {"` | — |
| [SRC-C9CF9B54F8-L001124](../../agents/omarai.py#L1124) | 1124 | `"                \"phrase\": str(evidence.get(\"phrase\") or \"\")[:500],"` | — |
| [SRC-C9CF9B54F8-L001125](../../agents/omarai.py#L1125) | 1125 | `"                \"basis\": str(evidence.get(\"basis\") or \"\")[:40],"` | — |
| [SRC-C9CF9B54F8-L001126](../../agents/omarai.py#L1126) | 1126 | `"                \"signal_type\": str(evidence.get(\"signal_type\") or \"\")[:80],"` | — |
| [SRC-C9CF9B54F8-L001127](../../agents/omarai.py#L1127) | 1127 | `"                \"product_fit\": str(evidence.get(\"product_fit\") or \"unassessed\")[:40],"` | — |
| [SRC-C9CF9B54F8-L001128](../../agents/omarai.py#L1128) | 1128 | `"            }"` | — |
| [SRC-C9CF9B54F8-L001129](../../agents/omarai.py#L1129) | 1129 | `"        providers = source.get(\"providers\")"` | — |
| [SRC-C9CF9B54F8-L001130](../../agents/omarai.py#L1130) | 1130 | `"        queries = source.get(\"queries\")"` | — |
| [SRC-C9CF9B54F8-L001131](../../agents/omarai.py#L1131) | 1131 | `"        return {"` | — |
| [SRC-C9CF9B54F8-L001132](../../agents/omarai.py#L1132) | 1132 | `"            \"title\": title,"` | — |
| [SRC-C9CF9B54F8-L001133](../../agents/omarai.py#L1133) | 1133 | `"            \"url\": source_url,"` | — |
| [SRC-C9CF9B54F8-L001134](../../agents/omarai.py#L1134) | 1134 | `"            \"snippet\": snippet,"` | — |
| [SRC-C9CF9B54F8-L001135](../../agents/omarai.py#L1135) | 1135 | `"            \"platform\": str(source.get(\"platform\") or \"web\")[:80],"` | — |
| [SRC-C9CF9B54F8-L001136](../../agents/omarai.py#L1136) | 1136 | `"            \"domain\": str(source.get(\"domain\") or \"\")[:253],"` | — |
| [SRC-C9CF9B54F8-L001137](../../agents/omarai.py#L1137) | 1137 | `"            \"published_at\": ("` | — |
| [SRC-C9CF9B54F8-L001138](../../agents/omarai.py#L1138) | 1138 | `"                str(source.get(\"published_at\"))[:120]"` | — |
| [SRC-C9CF9B54F8-L001139](../../agents/omarai.py#L1139) | 1139 | `"                if source.get(\"published_at\") is not None else None"` | — |
| [SRC-C9CF9B54F8-L001140](../../agents/omarai.py#L1140) | 1140 | `"            ),"` | — |
| [SRC-C9CF9B54F8-L001141](../../agents/omarai.py#L1141) | 1141 | `"            \"page_fetched\": source.get(\"page_fetched\") is True,"` | — |
| [SRC-C9CF9B54F8-L001142](../../agents/omarai.py#L1142) | 1142 | `"            \"readable_page_text_available\": source.get(\"readable_page_text_available\") is True,"` | — |
| [SRC-C9CF9B54F8-L001143](../../agents/omarai.py#L1143) | 1143 | `"            \"providers\": ["` | — |
| [SRC-C9CF9B54F8-L001144](../../agents/omarai.py#L1144) | 1144 | `"                str(value)[:80] for value in providers[:8] if isinstance(value, str)"` | — |
| [SRC-C9CF9B54F8-L001145](../../agents/omarai.py#L1145) | 1145 | `"            ] if isinstance(providers, list) else [],"` | — |
| [SRC-C9CF9B54F8-L001146](../../agents/omarai.py#L1146) | 1146 | `"            \"queries\": ["` | — |
| [SRC-C9CF9B54F8-L001147](../../agents/omarai.py#L1147) | 1147 | `"                str(value)[:500] for value in queries[:8] if isinstance(value, str)"` | — |
| [SRC-C9CF9B54F8-L001148](../../agents/omarai.py#L1148) | 1148 | `"            ] if isinstance(queries, list) else [],"` | — |
| [SRC-C9CF9B54F8-L001149](../../agents/omarai.py#L1149) | 1149 | `"            \"lead_qualification\": ("` | — |
| [SRC-C9CF9B54F8-L001150](../../agents/omarai.py#L1150) | 1150 | `"                \"public_demand_signal\""` | — |
| [SRC-C9CF9B54F8-L001151](../../agents/omarai.py#L1151) | 1151 | `"                if source.get(\"lead_qualification\") == \"public_demand_signal\""` | — |
| [SRC-C9CF9B54F8-L001152](../../agents/omarai.py#L1152) | 1152 | `"                else \"related_result_not_lead\""` | — |
| [SRC-C9CF9B54F8-L001153](../../agents/omarai.py#L1153) | 1153 | `"            ),"` | — |
| [SRC-C9CF9B54F8-L001154](../../agents/omarai.py#L1154) | 1154 | `"            \"lead_intent_evidence\": safe_evidence,"` | — |
| [SRC-C9CF9B54F8-L001155](../../agents/omarai.py#L1155) | 1155 | `"        }"` | — |
| [SRC-C9CF9B54F8-L001156](../../agents/omarai.py#L1156) | 1156 | `""` | — |
| [SRC-C9CF9B54F8-L001157](../../agents/omarai.py#L1157) | 1157 | `"    def save_discovery_run(self, profile_id: str, run: dict, *, tenant_id: str):"` | — |
| [SRC-C9CF9B54F8-L001158](../../agents/omarai.py#L1158) | 1158 | `"        if not isinstance(run, dict):"` | — |
| [SRC-C9CF9B54F8-L001159](../../agents/omarai.py#L1159) | 1159 | `"            raise TypeError(\"discovery run must be an object\")"` | — |
| [SRC-C9CF9B54F8-L001160](../../agents/omarai.py#L1160) | 1160 | `"        tenant = self._tenant(tenant_id)"` | — |
| [SRC-C9CF9B54F8-L001161](../../agents/omarai.py#L1161) | 1161 | `"        profile = self.get_product_profile(profile_id, tenant_id=tenant)"` | — |
| [SRC-C9CF9B54F8-L001162](../../agents/omarai.py#L1162) | 1162 | `"        if profile is None:"` | — |
| [SRC-C9CF9B54F8-L001163](../../agents/omarai.py#L1163) | 1163 | `"            return None"` | — |
| [SRC-C9CF9B54F8-L001164](../../agents/omarai.py#L1164) | 1164 | `"        raw_sources = run.get(\"sources\")"` | — |
| [SRC-C9CF9B54F8-L001165](../../agents/omarai.py#L1165) | 1165 | `"        raw_sources = raw_sources if isinstance(raw_sources, list) else []"` | — |
| [SRC-C9CF9B54F8-L001166](../../agents/omarai.py#L1166) | 1166 | `"        sources = ["` | — |
| [SRC-C9CF9B54F8-L001167](../../agents/omarai.py#L1167) | 1167 | `"            self._safe_discovery_source(item)"` | — |
| [SRC-C9CF9B54F8-L001168](../../agents/omarai.py#L1168) | 1168 | `"            for item in raw_sources[:30] if isinstance(item, dict)"` | — |
| [SRC-C9CF9B54F8-L001169](../../agents/omarai.py#L1169) | 1169 | `"        ]"` | — |
| [SRC-C9CF9B54F8-L001170](../../agents/omarai.py#L1170) | 1170 | `"        raw_queries = run.get(\"search_queries\")"` | — |
| [SRC-C9CF9B54F8-L001171](../../agents/omarai.py#L1171) | 1171 | `"        if not isinstance(raw_queries, list):"` | — |
| [SRC-C9CF9B54F8-L001172](../../agents/omarai.py#L1172) | 1172 | `"            raw_queries = []"` | — |
| [SRC-C9CF9B54F8-L001173](../../agents/omarai.py#L1173) | 1173 | `"        queries = [str(item)[:500] for item in raw_queries[:8] if isinstance(item, str)]"` | — |
| [SRC-C9CF9B54F8-L001174](../../agents/omarai.py#L1174) | 1174 | `"        raw_report = run.get(\"search_report\")"` | — |
| [SRC-C9CF9B54F8-L001175](../../agents/omarai.py#L1175) | 1175 | `"        raw_report = raw_report if isinstance(raw_report, dict) else {}"` | — |
| [SRC-C9CF9B54F8-L001176](../../agents/omarai.py#L1176) | 1176 | `"        lead_report = raw_report.get(\"lead_generation\")"` | — |
| [SRC-C9CF9B54F8-L001177](../../agents/omarai.py#L1177) | 1177 | `"        report = {"` | — |
| [SRC-C9CF9B54F8-L001178](../../agents/omarai.py#L1178) | 1178 | `"            \"lead_generation\": lead_report if isinstance(lead_report, dict) else {},"` | — |
| [SRC-C9CF9B54F8-L001179](../../agents/omarai.py#L1179) | 1179 | `"            \"pipeline_completion_status\": str("` | — |
| [SRC-C9CF9B54F8-L001180](../../agents/omarai.py#L1180) | 1180 | `"                raw_report.get(\"pipeline_completion_status\")"` | — |
| [SRC-C9CF9B54F8-L001181](../../agents/omarai.py#L1181) | 1181 | `"                or run.get(\"pipeline_completion_status\")"` | — |
| [SRC-C9CF9B54F8-L001182](../../agents/omarai.py#L1182) | 1182 | `"                or \"unknown\""` | — |
| [SRC-C9CF9B54F8-L001183](../../agents/omarai.py#L1183) | 1183 | `"            )[:80],"` | — |
| [SRC-C9CF9B54F8-L001184](../../agents/omarai.py#L1184) | 1184 | `"            \"search_outcome\": str(raw_report.get(\"search_outcome\") or \"unknown\")[:80],"` | — |
| [SRC-C9CF9B54F8-L001185](../../agents/omarai.py#L1185) | 1185 | `"            \"search_attempted\": raw_report.get(\"search_attempted\"),"` | — |
| [SRC-C9CF9B54F8-L001186](../../agents/omarai.py#L1186) | 1186 | `"            \"used_web_search\": run.get(\"used_web_search\") is True,"` | — |
| [SRC-C9CF9B54F8-L001187](../../agents/omarai.py#L1187) | 1187 | `"            \"used_social_search\": run.get(\"used_social_search\") is True,"` | — |
| [SRC-C9CF9B54F8-L001188](../../agents/omarai.py#L1188) | 1188 | `"        }"` | — |
| [SRC-C9CF9B54F8-L001189](../../agents/omarai.py#L1189) | 1189 | `"        report_json = json.dumps(report, ensure_ascii=False, separators=(\",\", \":\"))"` | — |
| [SRC-C9CF9B54F8-L001190](../../agents/omarai.py#L1190) | 1190 | `"        queries_json = json.dumps(queries, ensure_ascii=False, separators=(\",\", \":\"))"` | — |
| [SRC-C9CF9B54F8-L001191](../../agents/omarai.py#L1191) | 1191 | `"        sources_json = json.dumps(sources, ensure_ascii=False, separators=(\",\", \":\"))"` | — |
| [SRC-C9CF9B54F8-L001192](../../agents/omarai.py#L1192) | 1192 | `"        if sum(map(len, (report_json, queries_json, sources_json))) > 120000:"` | — |
| [SRC-C9CF9B54F8-L001193](../../agents/omarai.py#L1193) | 1193 | `"            raise ValueError(\"discovery result exceeds the storage limit\")"` | — |
| [SRC-C9CF9B54F8-L001194](../../agents/omarai.py#L1194) | 1194 | `"        run_id = \"discovery_\" + uuid.uuid4().hex"` | — |
| [SRC-C9CF9B54F8-L001195](../../agents/omarai.py#L1195) | 1195 | `"        now = now_utc()"` | — |
| [SRC-C9CF9B54F8-L001196](../../agents/omarai.py#L1196) | 1196 | `"        answer = str(run.get(\"answer\") or \"\")[:5000]"` | — |
| [SRC-C9CF9B54F8-L001197](../../agents/omarai.py#L1197) | 1197 | `"        kind = str(run.get(\"kind\") or \"lead_discovery\")[:100]"` | — |
| [SRC-C9CF9B54F8-L001198](../../agents/omarai.py#L1198) | 1198 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L001199](../../agents/omarai.py#L1199) | 1199 | `"            db.execute("` | — |
| [SRC-C9CF9B54F8-L001200](../../agents/omarai.py#L1200) | 1200 | `"                \"\"\"INSERT INTO discovery_runs"` | — |
| [SRC-C9CF9B54F8-L001201](../../agents/omarai.py#L1201) | 1201 | `"                   (id, tenant_id, profile_id, answer, kind, search_queries_json,"` | — |
| [SRC-C9CF9B54F8-L001202](../../agents/omarai.py#L1202) | 1202 | `"                    search_report_json, sources_json, created_at)"` | — |
| [SRC-C9CF9B54F8-L001203](../../agents/omarai.py#L1203) | 1203 | `"                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)\"\"\","` | — |
| [SRC-C9CF9B54F8-L001204](../../agents/omarai.py#L1204) | 1204 | `"                ("` | — |
| [SRC-C9CF9B54F8-L001205](../../agents/omarai.py#L1205) | 1205 | `"                    run_id, tenant, profile_id, answer, kind, queries_json,"` | — |
| [SRC-C9CF9B54F8-L001206](../../agents/omarai.py#L1206) | 1206 | `"                    report_json, sources_json, now,"` | — |
| [SRC-C9CF9B54F8-L001207](../../agents/omarai.py#L1207) | 1207 | `"                ),"` | — |
| [SRC-C9CF9B54F8-L001208](../../agents/omarai.py#L1208) | 1208 | `"            )"` | — |
| [SRC-C9CF9B54F8-L001209](../../agents/omarai.py#L1209) | 1209 | `"            row = db.execute("` | — |
| [SRC-C9CF9B54F8-L001210](../../agents/omarai.py#L1210) | 1210 | `"                \"\"\"SELECT r.id, r.tenant_id, r.profile_id, p.name AS profile_name,"` | — |
| [SRC-C9CF9B54F8-L001211](../../agents/omarai.py#L1211) | 1211 | `"                          r.answer, r.kind, r.search_queries_json, r.search_report_json,"` | — |
| [SRC-C9CF9B54F8-L001212](../../agents/omarai.py#L1212) | 1212 | `"                          r.sources_json, r.created_at"` | — |
| [SRC-C9CF9B54F8-L001213](../../agents/omarai.py#L1213) | 1213 | `"                   FROM discovery_runs r"` | — |
| [SRC-C9CF9B54F8-L001214](../../agents/omarai.py#L1214) | 1214 | `"                   JOIN product_profiles p"` | — |
| [SRC-C9CF9B54F8-L001215](../../agents/omarai.py#L1215) | 1215 | `"                     ON p.id=r.profile_id AND p.tenant_id=r.tenant_id"` | — |
| [SRC-C9CF9B54F8-L001216](../../agents/omarai.py#L1216) | 1216 | `"                   WHERE r.id=? AND r.tenant_id=?\"\"\","` | — |
| [SRC-C9CF9B54F8-L001217](../../agents/omarai.py#L1217) | 1217 | `"                (run_id, tenant),"` | — |
| [SRC-C9CF9B54F8-L001218](../../agents/omarai.py#L1218) | 1218 | `"            ).fetchone()"` | — |
| [SRC-C9CF9B54F8-L001219](../../agents/omarai.py#L1219) | 1219 | `"        return self._discovery_run_row(row)"` | — |
| [SRC-C9CF9B54F8-L001220](../../agents/omarai.py#L1220) | 1220 | `""` | — |
| [SRC-C9CF9B54F8-L001221](../../agents/omarai.py#L1221) | 1221 | `"    @staticmethod"` | — |
| [SRC-C9CF9B54F8-L001222](../../agents/omarai.py#L1222) | 1222 | `"    def _discovery_run_row(row):"` | — |
| [SRC-C9CF9B54F8-L001223](../../agents/omarai.py#L1223) | 1223 | `"        if row is None:"` | — |
| [SRC-C9CF9B54F8-L001224](../../agents/omarai.py#L1224) | 1224 | `"            return None"` | — |
| [SRC-C9CF9B54F8-L001225](../../agents/omarai.py#L1225) | 1225 | `"        item = dict(row)"` | — |
| [SRC-C9CF9B54F8-L001226](../../agents/omarai.py#L1226) | 1226 | `"        item[\"search_queries\"] = json.loads(item.pop(\"search_queries_json\"))"` | — |
| [SRC-C9CF9B54F8-L001227](../../agents/omarai.py#L1227) | 1227 | `"        item[\"search_report\"] = json.loads(item.pop(\"search_report_json\"))"` | — |
| [SRC-C9CF9B54F8-L001228](../../agents/omarai.py#L1228) | 1228 | `"        item[\"sources\"] = json.loads(item.pop(\"sources_json\"))"` | — |
| [SRC-C9CF9B54F8-L001229](../../agents/omarai.py#L1229) | 1229 | `"        return item"` | — |
| [SRC-C9CF9B54F8-L001230](../../agents/omarai.py#L1230) | 1230 | `""` | — |
| [SRC-C9CF9B54F8-L001231](../../agents/omarai.py#L1231) | 1231 | `"    def list_discovery_runs(self, *, tenant_id: str, limit: int = 50):"` | — |
| [SRC-C9CF9B54F8-L001232](../../agents/omarai.py#L1232) | 1232 | `"        tenant = self._tenant(tenant_id)"` | — |
| [SRC-C9CF9B54F8-L001233](../../agents/omarai.py#L1233) | 1233 | `"        limit = max(1, min(int(limit), 100))"` | — |
| [SRC-C9CF9B54F8-L001234](../../agents/omarai.py#L1234) | 1234 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L001235](../../agents/omarai.py#L1235) | 1235 | `"            rows = db.execute("` | — |
| [SRC-C9CF9B54F8-L001236](../../agents/omarai.py#L1236) | 1236 | `"                \"\"\"SELECT r.id, r.tenant_id, r.profile_id, p.name AS profile_name,"` | — |
| [SRC-C9CF9B54F8-L001237](../../agents/omarai.py#L1237) | 1237 | `"                          r.answer, r.kind, r.search_queries_json, r.search_report_json,"` | — |
| [SRC-C9CF9B54F8-L001238](../../agents/omarai.py#L1238) | 1238 | `"                          r.sources_json, r.created_at"` | — |
| [SRC-C9CF9B54F8-L001239](../../agents/omarai.py#L1239) | 1239 | `"                   FROM discovery_runs r"` | — |
| [SRC-C9CF9B54F8-L001240](../../agents/omarai.py#L1240) | 1240 | `"                   JOIN product_profiles p"` | — |
| [SRC-C9CF9B54F8-L001241](../../agents/omarai.py#L1241) | 1241 | `"                     ON p.id=r.profile_id AND p.tenant_id=r.tenant_id"` | — |
| [SRC-C9CF9B54F8-L001242](../../agents/omarai.py#L1242) | 1242 | `"                   WHERE r.tenant_id=?"` | — |
| [SRC-C9CF9B54F8-L001243](../../agents/omarai.py#L1243) | 1243 | `"                   ORDER BY r.created_at DESC, r.id LIMIT ?\"\"\","` | — |
| [SRC-C9CF9B54F8-L001244](../../agents/omarai.py#L1244) | 1244 | `"                (tenant, limit),"` | — |
| [SRC-C9CF9B54F8-L001245](../../agents/omarai.py#L1245) | 1245 | `"            ).fetchall()"` | — |
| [SRC-C9CF9B54F8-L001246](../../agents/omarai.py#L1246) | 1246 | `"        results = []"` | — |
| [SRC-C9CF9B54F8-L001247](../../agents/omarai.py#L1247) | 1247 | `"        for row in rows:"` | — |
| [SRC-C9CF9B54F8-L001248](../../agents/omarai.py#L1248) | 1248 | `"            item = self._discovery_run_row(row)"` | — |
| [SRC-C9CF9B54F8-L001249](../../agents/omarai.py#L1249) | 1249 | `"            results.append({"` | — |
| [SRC-C9CF9B54F8-L001250](../../agents/omarai.py#L1250) | 1250 | `"                \"id\": item[\"id\"],"` | — |
| [SRC-C9CF9B54F8-L001251](../../agents/omarai.py#L1251) | 1251 | `"                \"profile_id\": item[\"profile_id\"],"` | — |
| [SRC-C9CF9B54F8-L001252](../../agents/omarai.py#L1252) | 1252 | `"                \"profile_name\": item[\"profile_name\"],"` | — |
| [SRC-C9CF9B54F8-L001253](../../agents/omarai.py#L1253) | 1253 | `"                \"answer\": item[\"answer\"],"` | — |
| [SRC-C9CF9B54F8-L001254](../../agents/omarai.py#L1254) | 1254 | `"                \"kind\": item[\"kind\"],"` | — |
| [SRC-C9CF9B54F8-L001255](../../agents/omarai.py#L1255) | 1255 | `"                \"created_at\": item[\"created_at\"],"` | — |
| [SRC-C9CF9B54F8-L001256](../../agents/omarai.py#L1256) | 1256 | `"                \"source_count\": len(item[\"sources\"]),"` | — |
| [SRC-C9CF9B54F8-L001257](../../agents/omarai.py#L1257) | 1257 | `"                \"qualified_signal_count\": sum("` | — |
| [SRC-C9CF9B54F8-L001258](../../agents/omarai.py#L1258) | 1258 | `"                    source.get(\"lead_qualification\") == \"public_demand_signal\""` | — |
| [SRC-C9CF9B54F8-L001259](../../agents/omarai.py#L1259) | 1259 | `"                    for source in item[\"sources\"]"` | — |
| [SRC-C9CF9B54F8-L001260](../../agents/omarai.py#L1260) | 1260 | `"                ),"` | — |
| [SRC-C9CF9B54F8-L001261](../../agents/omarai.py#L1261) | 1261 | `"                \"pipeline_completion_status\": item[\"search_report\"].get("` | — |
| [SRC-C9CF9B54F8-L001262](../../agents/omarai.py#L1262) | 1262 | `"                    \"pipeline_completion_status\", \"unknown\""` | — |
| [SRC-C9CF9B54F8-L001263](../../agents/omarai.py#L1263) | 1263 | `"                ),"` | — |
| [SRC-C9CF9B54F8-L001264](../../agents/omarai.py#L1264) | 1264 | `"            })"` | — |
| [SRC-C9CF9B54F8-L001265](../../agents/omarai.py#L1265) | 1265 | `"        return results"` | — |
| [SRC-C9CF9B54F8-L001266](../../agents/omarai.py#L1266) | 1266 | `""` | — |
| [SRC-C9CF9B54F8-L001267](../../agents/omarai.py#L1267) | 1267 | `"    def get_discovery_run(self, run_id: str, *, tenant_id: str):"` | — |
| [SRC-C9CF9B54F8-L001268](../../agents/omarai.py#L1268) | 1268 | `"        if not isinstance(run_id, str) or not run_id.strip():"` | — |
| [SRC-C9CF9B54F8-L001269](../../agents/omarai.py#L1269) | 1269 | `"            return None"` | — |
| [SRC-C9CF9B54F8-L001270](../../agents/omarai.py#L1270) | 1270 | `"        tenant = self._tenant(tenant_id)"` | — |
| [SRC-C9CF9B54F8-L001271](../../agents/omarai.py#L1271) | 1271 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L001272](../../agents/omarai.py#L1272) | 1272 | `"            row = db.execute("` | — |
| [SRC-C9CF9B54F8-L001273](../../agents/omarai.py#L1273) | 1273 | `"                \"\"\"SELECT r.id, r.tenant_id, r.profile_id, p.name AS profile_name,"` | — |
| [SRC-C9CF9B54F8-L001274](../../agents/omarai.py#L1274) | 1274 | `"                          r.answer, r.kind, r.search_queries_json, r.search_report_json,"` | — |
| [SRC-C9CF9B54F8-L001275](../../agents/omarai.py#L1275) | 1275 | `"                          r.sources_json, r.created_at"` | — |
| [SRC-C9CF9B54F8-L001276](../../agents/omarai.py#L1276) | 1276 | `"                   FROM discovery_runs r"` | — |
| [SRC-C9CF9B54F8-L001277](../../agents/omarai.py#L1277) | 1277 | `"                   JOIN product_profiles p"` | — |
| [SRC-C9CF9B54F8-L001278](../../agents/omarai.py#L1278) | 1278 | `"                     ON p.id=r.profile_id AND p.tenant_id=r.tenant_id"` | — |
| [SRC-C9CF9B54F8-L001279](../../agents/omarai.py#L1279) | 1279 | `"                   WHERE r.id=? AND r.tenant_id=?\"\"\","` | — |
| [SRC-C9CF9B54F8-L001280](../../agents/omarai.py#L1280) | 1280 | `"                (run_id.strip(), tenant),"` | — |
| [SRC-C9CF9B54F8-L001281](../../agents/omarai.py#L1281) | 1281 | `"            ).fetchone()"` | — |
| [SRC-C9CF9B54F8-L001282](../../agents/omarai.py#L1282) | 1282 | `"        return self._discovery_run_row(row)"` | — |
| [SRC-C9CF9B54F8-L001283](../../agents/omarai.py#L1283) | 1283 | `""` | — |
| [SRC-C9CF9B54F8-L001284](../../agents/omarai.py#L1284) | 1284 | `"    def save_discovery_signal("` | — |
| [SRC-C9CF9B54F8-L001285](../../agents/omarai.py#L1285) | 1285 | `"        self, run_id: str, source_index: int, *, tenant_id: str"` | — |
| [SRC-C9CF9B54F8-L001286](../../agents/omarai.py#L1286) | 1286 | `"    ):"` | — |
| [SRC-C9CF9B54F8-L001287](../../agents/omarai.py#L1287) | 1287 | `"        if not isinstance(source_index, int) or isinstance(source_index, bool):"` | — |
| [SRC-C9CF9B54F8-L001288](../../agents/omarai.py#L1288) | 1288 | `"            return None"` | — |
| [SRC-C9CF9B54F8-L001289](../../agents/omarai.py#L1289) | 1289 | `"        run = self.get_discovery_run(run_id, tenant_id=tenant_id)"` | — |
| [SRC-C9CF9B54F8-L001290](../../agents/omarai.py#L1290) | 1290 | `"        if run is None or not 0 <= source_index < len(run[\"sources\"]):"` | — |
| [SRC-C9CF9B54F8-L001291](../../agents/omarai.py#L1291) | 1291 | `"            return None"` | — |
| [SRC-C9CF9B54F8-L001292](../../agents/omarai.py#L1292) | 1292 | `"        source = run[\"sources\"][source_index]"` | — |
| [SRC-C9CF9B54F8-L001293](../../agents/omarai.py#L1293) | 1293 | `"        if source.get(\"lead_qualification\") != \"public_demand_signal\":"` | — |
| [SRC-C9CF9B54F8-L001294](../../agents/omarai.py#L1294) | 1294 | `"            return None"` | — |
| [SRC-C9CF9B54F8-L001295](../../agents/omarai.py#L1295) | 1295 | `"        evidence = source.get(\"lead_intent_evidence\")"` | — |
| [SRC-C9CF9B54F8-L001296](../../agents/omarai.py#L1296) | 1296 | `"        if not isinstance(evidence, dict) or not str(evidence.get(\"phrase\") or \"\").strip():"` | — |
| [SRC-C9CF9B54F8-L001297](../../agents/omarai.py#L1297) | 1297 | `"            return None"` | — |
| [SRC-C9CF9B54F8-L001298](../../agents/omarai.py#L1298) | 1298 | `"        profile = self.get_product_profile(run[\"profile_id\"], tenant_id=tenant_id)"` | — |
| [SRC-C9CF9B54F8-L001299](../../agents/omarai.py#L1299) | 1299 | `"        if profile is None:"` | — |
| [SRC-C9CF9B54F8-L001300](../../agents/omarai.py#L1300) | 1300 | `"            return None"` | — |
| [SRC-C9CF9B54F8-L001301](../../agents/omarai.py#L1301) | 1301 | `"        product = profile[\"profile\"].get(\"product\", {})"` | — |
| [SRC-C9CF9B54F8-L001302](../../agents/omarai.py#L1302) | 1302 | `"        market = profile[\"profile\"].get(\"market\", {})"` | — |
| [SRC-C9CF9B54F8-L001303](../../agents/omarai.py#L1303) | 1303 | `"        product_terms = ["` | — |
| [SRC-C9CF9B54F8-L001304](../../agents/omarai.py#L1304) | 1304 | `"            str(item) for item in [product.get(\"name\"), *(product.get(\"aliases\") or [])]"` | — |
| [SRC-C9CF9B54F8-L001305](../../agents/omarai.py#L1305) | 1305 | `"            if isinstance(item, str) and item.strip()"` | — |
| [SRC-C9CF9B54F8-L001306](../../agents/omarai.py#L1306) | 1306 | `"        ]"` | — |
| [SRC-C9CF9B54F8-L001307](../../agents/omarai.py#L1307) | 1307 | `"        location_terms = ["` | — |
| [SRC-C9CF9B54F8-L001308](../../agents/omarai.py#L1308) | 1308 | `"            str(item) for item in (market.get(\"locations\") or [])"` | — |
| [SRC-C9CF9B54F8-L001309](../../agents/omarai.py#L1309) | 1309 | `"            if isinstance(item, str) and item.strip()"` | — |
| [SRC-C9CF9B54F8-L001310](../../agents/omarai.py#L1310) | 1310 | `"        ]"` | — |
| [SRC-C9CF9B54F8-L001311](../../agents/omarai.py#L1311) | 1311 | `"        source_text = str(source.get(\"snippet\") or source.get(\"title\") or \"\").strip()"` | — |
| [SRC-C9CF9B54F8-L001312](../../agents/omarai.py#L1312) | 1312 | `"        if not source_text:"` | — |
| [SRC-C9CF9B54F8-L001313](../../agents/omarai.py#L1313) | 1313 | `"            return None"` | — |
| [SRC-C9CF9B54F8-L001314](../../agents/omarai.py#L1314) | 1314 | `"        note = ("` | — |
| [SRC-C9CF9B54F8-L001315](../../agents/omarai.py#L1315) | 1315 | `"            \"Omarai public demand evidence \| \""` | — |
| [SRC-C9CF9B54F8-L001316](../../agents/omarai.py#L1316) | 1316 | `"            + \"phrase=\" + str(evidence.get(\"phrase\") or \"\")[:240]"` | — |
| [SRC-C9CF9B54F8-L001317](../../agents/omarai.py#L1317) | 1317 | `"            + \" \| basis=\" + str(evidence.get(\"basis\") or \"unknown\")[:40]"` | — |
| [SRC-C9CF9B54F8-L001318](../../agents/omarai.py#L1318) | 1318 | `"            + \" \| signal_type=\" + str(evidence.get(\"signal_type\") or \"unknown\")[:80]"` | — |
| [SRC-C9CF9B54F8-L001319](../../agents/omarai.py#L1319) | 1319 | `"            + \" \| profile=\" + str(profile.get(\"name\") or \"\")[:160]"` | — |
| [SRC-C9CF9B54F8-L001320](../../agents/omarai.py#L1320) | 1320 | `"            + \" \| run=\" + run[\"id\"]"` | — |
| [SRC-C9CF9B54F8-L001321](../../agents/omarai.py#L1321) | 1321 | `"        )"` | — |
| [SRC-C9CF9B54F8-L001322](../../agents/omarai.py#L1322) | 1322 | `"        return self.add("` | — |
| [SRC-C9CF9B54F8-L001323](../../agents/omarai.py#L1323) | 1323 | `"            source_text[:MAX_TEXT],"` | — |
| [SRC-C9CF9B54F8-L001324](../../agents/omarai.py#L1324) | 1324 | `"            source[\"url\"],"` | — |
| [SRC-C9CF9B54F8-L001325](../../agents/omarai.py#L1325) | 1325 | `"            str(source.get(\"platform\") or \"web\")[:80],"` | — |
| [SRC-C9CF9B54F8-L001326](../../agents/omarai.py#L1326) | 1326 | `"            observed_at=now_utc(),"` | — |
| [SRC-C9CF9B54F8-L001327](../../agents/omarai.py#L1327) | 1327 | `"            note=note[:1000],"` | — |
| [SRC-C9CF9B54F8-L001328](../../agents/omarai.py#L1328) | 1328 | `"            product_terms=product_terms,"` | — |
| [SRC-C9CF9B54F8-L001329](../../agents/omarai.py#L1329) | 1329 | `"            location_terms=location_terms,"` | — |
| [SRC-C9CF9B54F8-L001330](../../agents/omarai.py#L1330) | 1330 | `"            tenant_id=tenant_id,"` | — |
| [SRC-C9CF9B54F8-L001331](../../agents/omarai.py#L1331) | 1331 | `"        )"` | — |
| [SRC-C9CF9B54F8-L001332](../../agents/omarai.py#L1332) | 1332 | `""` | — |
| [SRC-C9CF9B54F8-L001333](../../agents/omarai.py#L1333) | 1333 | `"    def import_csv(self, filename: str, *, tenant_id: str \| None = None):"` | — |
| [SRC-C9CF9B54F8-L001334](../../agents/omarai.py#L1334) | 1334 | `"        tenant = self._tenant(tenant_id)"` | — |
| [SRC-C9CF9B54F8-L001335](../../agents/omarai.py#L1335) | 1335 | `"        results = {\"created\": 0, \"duplicates\": 0, \"errors\": []}"` | — |
| [SRC-C9CF9B54F8-L001336](../../agents/omarai.py#L1336) | 1336 | `"        with open(filename, newline=\"\", encoding=\"utf-8-sig\") as stream:"` | — |
| [SRC-C9CF9B54F8-L001337](../../agents/omarai.py#L1337) | 1337 | `"            reader = csv.DictReader(stream)"` | — |
| [SRC-C9CF9B54F8-L001338](../../agents/omarai.py#L1338) | 1338 | `"            required = {\"text\", \"source_url\", \"platform\"}"` | — |
| [SRC-C9CF9B54F8-L001339](../../agents/omarai.py#L1339) | 1339 | `"            if not reader.fieldnames or not required.issubset(reader.fieldnames):"` | — |
| [SRC-C9CF9B54F8-L001340](../../agents/omarai.py#L1340) | 1340 | `"                raise ValueError(\"CSV must contain text,source_url,platform columns\")"` | — |
| [SRC-C9CF9B54F8-L001341](../../agents/omarai.py#L1341) | 1341 | `"            for line, row in enumerate(reader, 2):"` | — |
| [SRC-C9CF9B54F8-L001342](../../agents/omarai.py#L1342) | 1342 | `"                try:"` | — |
| [SRC-C9CF9B54F8-L001343](../../agents/omarai.py#L1343) | 1343 | `"                    _, created = self.add("` | — |
| [SRC-C9CF9B54F8-L001344](../../agents/omarai.py#L1344) | 1344 | `"                        row[\"text\"], row[\"source_url\"], row[\"platform\"],"` | — |
| [SRC-C9CF9B54F8-L001345](../../agents/omarai.py#L1345) | 1345 | `"                        row.get(\"observed_at\") or None, row.get(\"note\") or \"\","` | — |
| [SRC-C9CF9B54F8-L001346](../../agents/omarai.py#L1346) | 1346 | `"                        tenant_id=tenant,"` | — |
| [SRC-C9CF9B54F8-L001347](../../agents/omarai.py#L1347) | 1347 | `"                    )"` | — |
| [SRC-C9CF9B54F8-L001348](../../agents/omarai.py#L1348) | 1348 | `"                    results[\"created\" if created else \"duplicates\"] += 1"` | — |
| [SRC-C9CF9B54F8-L001349](../../agents/omarai.py#L1349) | 1349 | `"                except (ValueError, TypeError) as exc:"` | — |
| [SRC-C9CF9B54F8-L001350](../../agents/omarai.py#L1350) | 1350 | `"                    results[\"errors\"].append({\"line\": line, \"error\": str(exc)})"` | — |
| [SRC-C9CF9B54F8-L001351](../../agents/omarai.py#L1351) | 1351 | `"        return results"` | — |
| [SRC-C9CF9B54F8-L001352](../../agents/omarai.py#L1352) | 1352 | `""` | — |
| [SRC-C9CF9B54F8-L001353](../../agents/omarai.py#L1353) | 1353 | `"    def export_csv(self, filename: str, *, tenant_id: str \| None = None):"` | — |
| [SRC-C9CF9B54F8-L001354](../../agents/omarai.py#L1354) | 1354 | `"        rows = self.list(limit=500, tenant_id=tenant_id)"` | — |
| [SRC-C9CF9B54F8-L001355](../../agents/omarai.py#L1355) | 1355 | `"        with open(filename, \"w\", newline=\"\", encoding=\"utf-8-sig\") as stream:"` | — |
| [SRC-C9CF9B54F8-L001356](../../agents/omarai.py#L1356) | 1356 | `"            fields = ["` | — |
| [SRC-C9CF9B54F8-L001357](../../agents/omarai.py#L1357) | 1357 | `"                \"id\", \"tenant_id\", \"text\", \"source_url\", \"platform\", \"observed_at\","` | — |
| [SRC-C9CF9B54F8-L001358](../../agents/omarai.py#L1358) | 1358 | `"                \"assessment\", \"status\", \"note\", \"created_at\","` | — |
| [SRC-C9CF9B54F8-L001359](../../agents/omarai.py#L1359) | 1359 | `"            ]"` | — |
| [SRC-C9CF9B54F8-L001360](../../agents/omarai.py#L1360) | 1360 | `"            writer = csv.DictWriter(stream, fieldnames=fields, quoting=csv.QUOTE_ALL)"` | — |
| [SRC-C9CF9B54F8-L001361](../../agents/omarai.py#L1361) | 1361 | `"            writer.writeheader()"` | — |
| [SRC-C9CF9B54F8-L001362](../../agents/omarai.py#L1362) | 1362 | `"            for row in rows:"` | — |
| [SRC-C9CF9B54F8-L001363](../../agents/omarai.py#L1363) | 1363 | `"                values = {"` | — |
| [SRC-C9CF9B54F8-L001364](../../agents/omarai.py#L1364) | 1364 | `"                    key: json.dumps(row[key], ensure_ascii=False)"` | — |
| [SRC-C9CF9B54F8-L001365](../../agents/omarai.py#L1365) | 1365 | `"                    if key == \"assessment\""` | — |
| [SRC-C9CF9B54F8-L001366](../../agents/omarai.py#L1366) | 1366 | `"                    else row.get(key, \"\")"` | — |
| [SRC-C9CF9B54F8-L001367](../../agents/omarai.py#L1367) | 1367 | `"                    for key in fields"` | — |
| [SRC-C9CF9B54F8-L001368](../../agents/omarai.py#L1368) | 1368 | `"                }"` | — |
| [SRC-C9CF9B54F8-L001369](../../agents/omarai.py#L1369) | 1369 | `"                writer.writerow({key: _csv_safe_cell(value) for key, value in values.items()})"` | — |
| [SRC-C9CF9B54F8-L001370](../../agents/omarai.py#L1370) | 1370 | `"        return len(rows)"` | — |
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
