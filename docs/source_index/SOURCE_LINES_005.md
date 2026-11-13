# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **005**
- سجلات الأسطر: **800**
- النطاق: SRC-C9CF9B54F8-L000600 إلى SRC-FDEEAFDFCA-L000023
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-C9CF9B54F8 — [agents/omarai.py](../../agents/omarai.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-C9CF9B54F8-L000600](../../agents/omarai.py#L600) | 600 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000601](../../agents/omarai.py#L601) | 601 | `"            row = db.execute("` | — |
| [SRC-C9CF9B54F8-L000602](../../agents/omarai.py#L602) | 602 | `"                \"\"\"SELECT m.tenant_id, m.user_id, m.role"` | — |
| [SRC-C9CF9B54F8-L000603](../../agents/omarai.py#L603) | 603 | `"                   FROM tenant_memberships m"` | — |
| [SRC-C9CF9B54F8-L000604](../../agents/omarai.py#L604) | 604 | `"                   JOIN tenants t ON t.id=m.tenant_id AND t.active=1"` | — |
| [SRC-C9CF9B54F8-L000605](../../agents/omarai.py#L605) | 605 | `"                   JOIN users u ON u.id=m.user_id AND u.active=1"` | — |
| [SRC-C9CF9B54F8-L000606](../../agents/omarai.py#L606) | 606 | `"                   WHERE m.tenant_id=? AND m.user_id=? AND m.active=1\"\"\","` | — |
| [SRC-C9CF9B54F8-L000607](../../agents/omarai.py#L607) | 607 | `"                (DEFAULT_TENANT_ID, DEFAULT_USER_ID),"` | — |
| [SRC-C9CF9B54F8-L000608](../../agents/omarai.py#L608) | 608 | `"            ).fetchone()"` | — |
| [SRC-C9CF9B54F8-L000609](../../agents/omarai.py#L609) | 609 | `"        return dict(row) if row else {}"` | — |
| [SRC-C9CF9B54F8-L000610](../../agents/omarai.py#L610) | 610 | `""` | — |
| [SRC-C9CF9B54F8-L000611](../../agents/omarai.py#L611) | 611 | `"    def create_tenant(self, name: str, slug: str \| None = None) -> str:"` | — |
| [SRC-C9CF9B54F8-L000612](../../agents/omarai.py#L612) | 612 | `"        clean_name = str(name or \"\").strip()[:160]"` | — |
| [SRC-C9CF9B54F8-L000613](../../agents/omarai.py#L613) | 613 | `"        if not clean_name:"` | — |
| [SRC-C9CF9B54F8-L000614](../../agents/omarai.py#L614) | 614 | `"            raise ValueError(\"tenant name is required\")"` | — |
| [SRC-C9CF9B54F8-L000615](../../agents/omarai.py#L615) | 615 | `"        clean_slug = re.sub("` | — |
| [SRC-C9CF9B54F8-L000616](../../agents/omarai.py#L616) | 616 | `"            r\"[^a-z0-9-]+\", \"-\", str(slug or clean_name.casefold())"` | — |
| [SRC-C9CF9B54F8-L000617](../../agents/omarai.py#L617) | 617 | `"        ).strip(\"-\")[:80]"` | — |
| [SRC-C9CF9B54F8-L000618](../../agents/omarai.py#L618) | 618 | `"        if not clean_slug:"` | — |
| [SRC-C9CF9B54F8-L000619](../../agents/omarai.py#L619) | 619 | `"            raise ValueError(\"tenant slug is invalid\")"` | — |
| [SRC-C9CF9B54F8-L000620](../../agents/omarai.py#L620) | 620 | `"        tenant_id = \"tenant_\" + uuid.uuid4().hex"` | — |
| [SRC-C9CF9B54F8-L000621](../../agents/omarai.py#L621) | 621 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000622](../../agents/omarai.py#L622) | 622 | `"            db.execute("` | — |
| [SRC-C9CF9B54F8-L000623](../../agents/omarai.py#L623) | 623 | `"                \"INSERT INTO tenants (id, name, slug, active, created_at) VALUES (?, ?, ?, 1, ?)\","` | — |
| [SRC-C9CF9B54F8-L000624](../../agents/omarai.py#L624) | 624 | `"                (tenant_id, clean_name, clean_slug, now_utc()),"` | — |
| [SRC-C9CF9B54F8-L000625](../../agents/omarai.py#L625) | 625 | `"            )"` | — |
| [SRC-C9CF9B54F8-L000626](../../agents/omarai.py#L626) | 626 | `"        return tenant_id"` | — |
| [SRC-C9CF9B54F8-L000627](../../agents/omarai.py#L627) | 627 | `""` | — |
| [SRC-C9CF9B54F8-L000628](../../agents/omarai.py#L628) | 628 | `"    def create_user(self, email: str, display_name: str, user_id: str \| None = None) -> str:"` | — |
| [SRC-C9CF9B54F8-L000629](../../agents/omarai.py#L629) | 629 | `"        clean_email = str(email or \"\").strip().lower()[:254]"` | — |
| [SRC-C9CF9B54F8-L000630](../../agents/omarai.py#L630) | 630 | `"        clean_name = str(display_name or \"\").strip()[:160]"` | — |
| [SRC-C9CF9B54F8-L000631](../../agents/omarai.py#L631) | 631 | `"        if not clean_email or \"@\" not in clean_email or not clean_name:"` | — |
| [SRC-C9CF9B54F8-L000632](../../agents/omarai.py#L632) | 632 | `"            raise ValueError(\"valid email and display name are required\")"` | — |
| [SRC-C9CF9B54F8-L000633](../../agents/omarai.py#L633) | 633 | `"        identity = str(user_id or (\"user_\" + uuid.uuid4().hex))"` | — |
| [SRC-C9CF9B54F8-L000634](../../agents/omarai.py#L634) | 634 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000635](../../agents/omarai.py#L635) | 635 | `"            db.execute("` | — |
| [SRC-C9CF9B54F8-L000636](../../agents/omarai.py#L636) | 636 | `"                \"\"\"INSERT INTO users (id, email, display_name, active, created_at)"` | — |
| [SRC-C9CF9B54F8-L000637](../../agents/omarai.py#L637) | 637 | `"                   VALUES (?, ?, ?, 1, ?)\"\"\","` | — |
| [SRC-C9CF9B54F8-L000638](../../agents/omarai.py#L638) | 638 | `"                (identity, clean_email, clean_name, now_utc()),"` | — |
| [SRC-C9CF9B54F8-L000639](../../agents/omarai.py#L639) | 639 | `"            )"` | — |
| [SRC-C9CF9B54F8-L000640](../../agents/omarai.py#L640) | 640 | `"        return identity"` | — |
| [SRC-C9CF9B54F8-L000641](../../agents/omarai.py#L641) | 641 | `""` | — |
| [SRC-C9CF9B54F8-L000642](../../agents/omarai.py#L642) | 642 | `"    def add_membership(self, tenant_id: str, user_id: str, role: str = \"sales_agent\"):"` | — |
| [SRC-C9CF9B54F8-L000643](../../agents/omarai.py#L643) | 643 | `"        tenant = self._tenant(tenant_id)"` | — |
| [SRC-C9CF9B54F8-L000644](../../agents/omarai.py#L644) | 644 | `"        if role not in self.ALLOWED_ROLES:"` | — |
| [SRC-C9CF9B54F8-L000645](../../agents/omarai.py#L645) | 645 | `"            raise ValueError(\"unsupported membership role\")"` | — |
| [SRC-C9CF9B54F8-L000646](../../agents/omarai.py#L646) | 646 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000647](../../agents/omarai.py#L647) | 647 | `"            exists = db.execute("` | — |
| [SRC-C9CF9B54F8-L000648](../../agents/omarai.py#L648) | 648 | `"                \"\"\"SELECT 1 FROM tenants t"` | — |
| [SRC-C9CF9B54F8-L000649](../../agents/omarai.py#L649) | 649 | `"                   JOIN users u ON u.id=?"` | — |
| [SRC-C9CF9B54F8-L000650](../../agents/omarai.py#L650) | 650 | `"                   WHERE t.id=? AND t.active=1 AND u.active=1\"\"\","` | — |
| [SRC-C9CF9B54F8-L000651](../../agents/omarai.py#L651) | 651 | `"                (user_id, tenant),"` | — |
| [SRC-C9CF9B54F8-L000652](../../agents/omarai.py#L652) | 652 | `"            ).fetchone()"` | — |
| [SRC-C9CF9B54F8-L000653](../../agents/omarai.py#L653) | 653 | `"            if not exists:"` | — |
| [SRC-C9CF9B54F8-L000654](../../agents/omarai.py#L654) | 654 | `"                raise ValueError(\"active tenant and user are required\")"` | — |
| [SRC-C9CF9B54F8-L000655](../../agents/omarai.py#L655) | 655 | `"            db.execute("` | — |
| [SRC-C9CF9B54F8-L000656](../../agents/omarai.py#L656) | 656 | `"                \"\"\"INSERT INTO tenant_memberships"` | — |
| [SRC-C9CF9B54F8-L000657](../../agents/omarai.py#L657) | 657 | `"                   (tenant_id, user_id, role, active, created_at)"` | — |
| [SRC-C9CF9B54F8-L000658](../../agents/omarai.py#L658) | 658 | `"                   VALUES (?, ?, ?, 1, ?)"` | — |
| [SRC-C9CF9B54F8-L000659](../../agents/omarai.py#L659) | 659 | `"                   ON CONFLICT(tenant_id, user_id)"` | — |
| [SRC-C9CF9B54F8-L000660](../../agents/omarai.py#L660) | 660 | `"                   DO UPDATE SET role=excluded.role, active=1\"\"\","` | — |
| [SRC-C9CF9B54F8-L000661](../../agents/omarai.py#L661) | 661 | `"                (tenant, user_id, role, now_utc()),"` | — |
| [SRC-C9CF9B54F8-L000662](../../agents/omarai.py#L662) | 662 | `"            )"` | — |
| [SRC-C9CF9B54F8-L000663](../../agents/omarai.py#L663) | 663 | `""` | — |
| [SRC-C9CF9B54F8-L000664](../../agents/omarai.py#L664) | 664 | `"    @staticmethod"` | — |
| [SRC-C9CF9B54F8-L000665](../../agents/omarai.py#L665) | 665 | `"    def _token_hash(token: str) -> str:"` | — |
| [SRC-C9CF9B54F8-L000666](../../agents/omarai.py#L666) | 666 | `"        return hashlib.sha256(token.encode(\"utf-8\")).hexdigest()"` | — |
| [SRC-C9CF9B54F8-L000667](../../agents/omarai.py#L667) | 667 | `""` | — |
| [SRC-C9CF9B54F8-L000668](../../agents/omarai.py#L668) | 668 | `"    @staticmethod"` | — |
| [SRC-C9CF9B54F8-L000669](../../agents/omarai.py#L669) | 669 | `"    def _normalize_token_expiry(expires_at: str \| None) -> str \| None:"` | — |
| [SRC-C9CF9B54F8-L000670](../../agents/omarai.py#L670) | 670 | `"        \"\"\"Store token expiries as validated UTC timestamps for safe comparisons.\"\"\""` | — |
| [SRC-C9CF9B54F8-L000671](../../agents/omarai.py#L671) | 671 | `"        if expires_at is None:"` | — |
| [SRC-C9CF9B54F8-L000672](../../agents/omarai.py#L672) | 672 | `"            return None"` | — |
| [SRC-C9CF9B54F8-L000673](../../agents/omarai.py#L673) | 673 | `"        if not isinstance(expires_at, str) or not expires_at.strip():"` | — |
| [SRC-C9CF9B54F8-L000674](../../agents/omarai.py#L674) | 674 | `"            raise ValueError(\"expires_at must be an ISO-8601 timestamp with a timezone\")"` | — |
| [SRC-C9CF9B54F8-L000675](../../agents/omarai.py#L675) | 675 | `"        value = expires_at.strip()"` | — |
| [SRC-C9CF9B54F8-L000676](../../agents/omarai.py#L676) | 676 | `"        if value.endswith(\"Z\"):"` | — |
| [SRC-C9CF9B54F8-L000677](../../agents/omarai.py#L677) | 677 | `"            value = value[:-1] + \"+00:00\""` | — |
| [SRC-C9CF9B54F8-L000678](../../agents/omarai.py#L678) | 678 | `"        try:"` | — |
| [SRC-C9CF9B54F8-L000679](../../agents/omarai.py#L679) | 679 | `"            parsed = datetime.fromisoformat(value)"` | — |
| [SRC-C9CF9B54F8-L000680](../../agents/omarai.py#L680) | 680 | `"        except ValueError as exc:"` | — |
| [SRC-C9CF9B54F8-L000681](../../agents/omarai.py#L681) | 681 | `"            raise ValueError("` | — |
| [SRC-C9CF9B54F8-L000682](../../agents/omarai.py#L682) | 682 | `"                \"expires_at must be an ISO-8601 timestamp with a timezone\""` | — |
| [SRC-C9CF9B54F8-L000683](../../agents/omarai.py#L683) | 683 | `"            ) from exc"` | — |
| [SRC-C9CF9B54F8-L000684](../../agents/omarai.py#L684) | 684 | `"        if parsed.tzinfo is None or parsed.utcoffset() is None:"` | — |
| [SRC-C9CF9B54F8-L000685](../../agents/omarai.py#L685) | 685 | `"            raise ValueError(\"expires_at must include an explicit timezone\")"` | — |
| [SRC-C9CF9B54F8-L000686](../../agents/omarai.py#L686) | 686 | `"        normalized = parsed.astimezone(UTC)"` | — |
| [SRC-C9CF9B54F8-L000687](../../agents/omarai.py#L687) | 687 | `"        if normalized <= datetime.now(UTC):"` | — |
| [SRC-C9CF9B54F8-L000688](../../agents/omarai.py#L688) | 688 | `"            raise ValueError(\"expires_at must be in the future\")"` | — |
| [SRC-C9CF9B54F8-L000689](../../agents/omarai.py#L689) | 689 | `"        return normalized.isoformat(timespec=\"seconds\").replace(\"+00:00\", \"Z\")"` | — |
| [SRC-C9CF9B54F8-L000690](../../agents/omarai.py#L690) | 690 | `""` | — |
| [SRC-C9CF9B54F8-L000691](../../agents/omarai.py#L691) | 691 | `"    def create_api_token("` | — |
| [SRC-C9CF9B54F8-L000692](../../agents/omarai.py#L692) | 692 | `"        self,"` | — |
| [SRC-C9CF9B54F8-L000693](../../agents/omarai.py#L693) | 693 | `"        token: str,"` | — |
| [SRC-C9CF9B54F8-L000694](../../agents/omarai.py#L694) | 694 | `"        tenant_id: str,"` | — |
| [SRC-C9CF9B54F8-L000695](../../agents/omarai.py#L695) | 695 | `"        user_id: str,"` | — |
| [SRC-C9CF9B54F8-L000696](../../agents/omarai.py#L696) | 696 | `"        label: str = \"api\","` | — |
| [SRC-C9CF9B54F8-L000697](../../agents/omarai.py#L697) | 697 | `"        expires_at: str \| None = None,"` | — |
| [SRC-C9CF9B54F8-L000698](../../agents/omarai.py#L698) | 698 | `"    ):"` | — |
| [SRC-C9CF9B54F8-L000699](../../agents/omarai.py#L699) | 699 | `"        if not isinstance(token, str) or len(token.strip()) < 32:"` | — |
| [SRC-C9CF9B54F8-L000700](../../agents/omarai.py#L700) | 700 | `"            raise ValueError(\"API token must contain at least 32 characters\")"` | — |
| [SRC-C9CF9B54F8-L000701](../../agents/omarai.py#L701) | 701 | `"        tenant = self._tenant(tenant_id)"` | — |
| [SRC-C9CF9B54F8-L000702](../../agents/omarai.py#L702) | 702 | `"        expires_at = self._normalize_token_expiry(expires_at)"` | — |
| [SRC-C9CF9B54F8-L000703](../../agents/omarai.py#L703) | 703 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000704](../../agents/omarai.py#L704) | 704 | `"            membership = db.execute("` | — |
| [SRC-C9CF9B54F8-L000705](../../agents/omarai.py#L705) | 705 | `"                \"\"\"SELECT 1 FROM tenant_memberships m"` | — |
| [SRC-C9CF9B54F8-L000706](../../agents/omarai.py#L706) | 706 | `"                   JOIN tenants t ON t.id=m.tenant_id AND t.active=1"` | — |
| [SRC-C9CF9B54F8-L000707](../../agents/omarai.py#L707) | 707 | `"                   JOIN users u ON u.id=m.user_id AND u.active=1"` | — |
| [SRC-C9CF9B54F8-L000708](../../agents/omarai.py#L708) | 708 | `"                   WHERE m.tenant_id=? AND m.user_id=? AND m.active=1\"\"\","` | — |
| [SRC-C9CF9B54F8-L000709](../../agents/omarai.py#L709) | 709 | `"                (tenant, user_id),"` | — |
| [SRC-C9CF9B54F8-L000710](../../agents/omarai.py#L710) | 710 | `"            ).fetchone()"` | — |
| [SRC-C9CF9B54F8-L000711](../../agents/omarai.py#L711) | 711 | `"            if not membership:"` | — |
| [SRC-C9CF9B54F8-L000712](../../agents/omarai.py#L712) | 712 | `"                raise ValueError(\"active tenant membership is required\")"` | — |
| [SRC-C9CF9B54F8-L000713](../../agents/omarai.py#L713) | 713 | `"            db.execute("` | — |
| [SRC-C9CF9B54F8-L000714](../../agents/omarai.py#L714) | 714 | `"                \"\"\"INSERT INTO api_tokens"` | — |
| [SRC-C9CF9B54F8-L000715](../../agents/omarai.py#L715) | 715 | `"                   (token_hash, tenant_id, user_id, label, active, created_at, expires_at)"` | — |
| [SRC-C9CF9B54F8-L000716](../../agents/omarai.py#L716) | 716 | `"                   VALUES (?, ?, ?, ?, 1, ?, ?)\"\"\","` | — |
| [SRC-C9CF9B54F8-L000717](../../agents/omarai.py#L717) | 717 | `"                ("` | — |
| [SRC-C9CF9B54F8-L000718](../../agents/omarai.py#L718) | 718 | `"                    self._token_hash(token.strip()),"` | — |
| [SRC-C9CF9B54F8-L000719](../../agents/omarai.py#L719) | 719 | `"                    tenant,"` | — |
| [SRC-C9CF9B54F8-L000720](../../agents/omarai.py#L720) | 720 | `"                    user_id,"` | — |
| [SRC-C9CF9B54F8-L000721](../../agents/omarai.py#L721) | 721 | `"                    str(label or \"api\")[:80],"` | — |
| [SRC-C9CF9B54F8-L000722](../../agents/omarai.py#L722) | 722 | `"                    now_utc(),"` | — |
| [SRC-C9CF9B54F8-L000723](../../agents/omarai.py#L723) | 723 | `"                    expires_at,"` | — |
| [SRC-C9CF9B54F8-L000724](../../agents/omarai.py#L724) | 724 | `"                ),"` | — |
| [SRC-C9CF9B54F8-L000725](../../agents/omarai.py#L725) | 725 | `"            )"` | — |
| [SRC-C9CF9B54F8-L000726](../../agents/omarai.py#L726) | 726 | `""` | — |
| [SRC-C9CF9B54F8-L000727](../../agents/omarai.py#L727) | 727 | `"    def resolve_api_token(self, token: str) -> dict \| None:"` | — |
| [SRC-C9CF9B54F8-L000728](../../agents/omarai.py#L728) | 728 | `"        if not isinstance(token, str) or len(token.strip()) < 32:"` | — |
| [SRC-C9CF9B54F8-L000729](../../agents/omarai.py#L729) | 729 | `"            return None"` | — |
| [SRC-C9CF9B54F8-L000730](../../agents/omarai.py#L730) | 730 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000731](../../agents/omarai.py#L731) | 731 | `"            row = db.execute("` | — |
| [SRC-C9CF9B54F8-L000732](../../agents/omarai.py#L732) | 732 | `"                \"\"\"SELECT m.tenant_id, m.user_id, m.role"` | — |
| [SRC-C9CF9B54F8-L000733](../../agents/omarai.py#L733) | 733 | `"                   FROM api_tokens a"` | — |
| [SRC-C9CF9B54F8-L000734](../../agents/omarai.py#L734) | 734 | `"                   JOIN tenant_memberships m"` | — |
| [SRC-C9CF9B54F8-L000735](../../agents/omarai.py#L735) | 735 | `"                     ON m.tenant_id=a.tenant_id AND m.user_id=a.user_id"` | — |
| [SRC-C9CF9B54F8-L000736](../../agents/omarai.py#L736) | 736 | `"                   JOIN tenants t ON t.id=m.tenant_id AND t.active=1"` | — |
| [SRC-C9CF9B54F8-L000737](../../agents/omarai.py#L737) | 737 | `"                   JOIN users u ON u.id=m.user_id AND u.active=1"` | — |
| [SRC-C9CF9B54F8-L000738](../../agents/omarai.py#L738) | 738 | `"                   WHERE a.token_hash=? AND a.active=1 AND m.active=1"` | — |
| [SRC-C9CF9B54F8-L000739](../../agents/omarai.py#L739) | 739 | `"                     AND (a.expires_at IS NULL OR a.expires_at > ?)\"\"\","` | — |
| [SRC-C9CF9B54F8-L000740](../../agents/omarai.py#L740) | 740 | `"                (self._token_hash(token.strip()), now_utc()),"` | — |
| [SRC-C9CF9B54F8-L000741](../../agents/omarai.py#L741) | 741 | `"            ).fetchone()"` | — |
| [SRC-C9CF9B54F8-L000742](../../agents/omarai.py#L742) | 742 | `"        return dict(row) if row else None"` | — |
| [SRC-C9CF9B54F8-L000743](../../agents/omarai.py#L743) | 743 | `""` | — |
| [SRC-C9CF9B54F8-L000744](../../agents/omarai.py#L744) | 744 | `"    def create_web_session("` | — |
| [SRC-C9CF9B54F8-L000745](../../agents/omarai.py#L745) | 745 | `"        self,"` | — |
| [SRC-C9CF9B54F8-L000746](../../agents/omarai.py#L746) | 746 | `"        access_token: str,"` | — |
| [SRC-C9CF9B54F8-L000747](../../agents/omarai.py#L747) | 747 | `"        *,"` | — |
| [SRC-C9CF9B54F8-L000748](../../agents/omarai.py#L748) | 748 | `"        shared_token: str = \"\","` | — |
| [SRC-C9CF9B54F8-L000749](../../agents/omarai.py#L749) | 749 | `"        max_age_seconds: int = 8 * 60 * 60,"` | — |
| [SRC-C9CF9B54F8-L000750](../../agents/omarai.py#L750) | 750 | `"    ) -> tuple[str, dict] \| None:"` | — |
| [SRC-C9CF9B54F8-L000751](../../agents/omarai.py#L751) | 751 | `"        \"\"\"Exchange a valid API credential for a short-lived opaque browser session.\"\"\""` | — |
| [SRC-C9CF9B54F8-L000752](../../agents/omarai.py#L752) | 752 | `"        if not isinstance(access_token, str) or len(access_token.strip()) < 32:"` | — |
| [SRC-C9CF9B54F8-L000753](../../agents/omarai.py#L753) | 753 | `"            return None"` | — |
| [SRC-C9CF9B54F8-L000754](../../agents/omarai.py#L754) | 754 | `"        token = access_token.strip()"` | — |
| [SRC-C9CF9B54F8-L000755](../../agents/omarai.py#L755) | 755 | `"        is_shared = bool(shared_token and hmac.compare_digest(token, shared_token))"` | — |
| [SRC-C9CF9B54F8-L000756](../../agents/omarai.py#L756) | 756 | `"        principal = self.default_principal() if is_shared else self.resolve_api_token(token)"` | — |
| [SRC-C9CF9B54F8-L000757](../../agents/omarai.py#L757) | 757 | `"        if not principal:"` | — |
| [SRC-C9CF9B54F8-L000758](../../agents/omarai.py#L758) | 758 | `"            return None"` | — |
| [SRC-C9CF9B54F8-L000759](../../agents/omarai.py#L759) | 759 | `"        if ("` | — |
| [SRC-C9CF9B54F8-L000760](../../agents/omarai.py#L760) | 760 | `"            not isinstance(max_age_seconds, int)"` | — |
| [SRC-C9CF9B54F8-L000761](../../agents/omarai.py#L761) | 761 | `"            or isinstance(max_age_seconds, bool)"` | — |
| [SRC-C9CF9B54F8-L000762](../../agents/omarai.py#L762) | 762 | `"            or not 60 <= max_age_seconds <= 24 * 60 * 60"` | — |
| [SRC-C9CF9B54F8-L000763](../../agents/omarai.py#L763) | 763 | `"        ):"` | — |
| [SRC-C9CF9B54F8-L000764](../../agents/omarai.py#L764) | 764 | `"            raise ValueError(\"browser session lifetime must be between 60 seconds and 24 hours\")"` | — |
| [SRC-C9CF9B54F8-L000765](../../agents/omarai.py#L765) | 765 | `""` | — |
| [SRC-C9CF9B54F8-L000766](../../agents/omarai.py#L766) | 766 | `"        session_id = secrets.token_urlsafe(32)"` | — |
| [SRC-C9CF9B54F8-L000767](../../agents/omarai.py#L767) | 767 | `"        created_at = now_utc()"` | — |
| [SRC-C9CF9B54F8-L000768](../../agents/omarai.py#L768) | 768 | `"        expires_at = ("` | — |
| [SRC-C9CF9B54F8-L000769](../../agents/omarai.py#L769) | 769 | `"            datetime.now(UTC) + timedelta(seconds=max_age_seconds)"` | — |
| [SRC-C9CF9B54F8-L000770](../../agents/omarai.py#L770) | 770 | `"        ).isoformat(timespec=\"seconds\").replace(\"+00:00\", \"Z\")"` | — |
| [SRC-C9CF9B54F8-L000771](../../agents/omarai.py#L771) | 771 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000772](../../agents/omarai.py#L772) | 772 | `"            # Browser sessions are short-lived credentials, not an audit log."` | — |
| [SRC-C9CF9B54F8-L000773](../../agents/omarai.py#L773) | 773 | `"            # Prune expired and revoked rows opportunistically before inserting"` | — |
| [SRC-C9CF9B54F8-L000774](../../agents/omarai.py#L774) | 774 | `"            # a new session so abandoned rows cannot grow without bound."` | — |
| [SRC-C9CF9B54F8-L000775](../../agents/omarai.py#L775) | 775 | `"            db.execute("` | — |
| [SRC-C9CF9B54F8-L000776](../../agents/omarai.py#L776) | 776 | `"                \"\"\"DELETE FROM web_sessions"` | — |
| [SRC-C9CF9B54F8-L000777](../../agents/omarai.py#L777) | 777 | `"                   WHERE revoked_at IS NOT NULL OR expires_at <= ?\"\"\","` | — |
| [SRC-C9CF9B54F8-L000778](../../agents/omarai.py#L778) | 778 | `"                (created_at,),"` | — |
| [SRC-C9CF9B54F8-L000779](../../agents/omarai.py#L779) | 779 | `"            )"` | — |
| [SRC-C9CF9B54F8-L000780](../../agents/omarai.py#L780) | 780 | `"            db.execute("` | — |
| [SRC-C9CF9B54F8-L000781](../../agents/omarai.py#L781) | 781 | `"                \"\"\"INSERT INTO web_sessions"` | — |
| [SRC-C9CF9B54F8-L000782](../../agents/omarai.py#L782) | 782 | `"                   (session_hash, credential_hash, is_shared_token, tenant_id,"` | — |
| [SRC-C9CF9B54F8-L000783](../../agents/omarai.py#L783) | 783 | `"                    user_id, created_at, expires_at, revoked_at)"` | — |
| [SRC-C9CF9B54F8-L000784](../../agents/omarai.py#L784) | 784 | `"                   VALUES (?, ?, ?, ?, ?, ?, ?, NULL)\"\"\","` | — |
| [SRC-C9CF9B54F8-L000785](../../agents/omarai.py#L785) | 785 | `"                ("` | — |
| [SRC-C9CF9B54F8-L000786](../../agents/omarai.py#L786) | 786 | `"                    self._token_hash(session_id),"` | — |
| [SRC-C9CF9B54F8-L000787](../../agents/omarai.py#L787) | 787 | `"                    self._token_hash(token),"` | — |
| [SRC-C9CF9B54F8-L000788](../../agents/omarai.py#L788) | 788 | `"                    1 if is_shared else 0,"` | — |
| [SRC-C9CF9B54F8-L000789](../../agents/omarai.py#L789) | 789 | `"                    principal[\"tenant_id\"],"` | — |
| [SRC-C9CF9B54F8-L000790](../../agents/omarai.py#L790) | 790 | `"                    principal[\"user_id\"],"` | — |
| [SRC-C9CF9B54F8-L000791](../../agents/omarai.py#L791) | 791 | `"                    created_at,"` | — |
| [SRC-C9CF9B54F8-L000792](../../agents/omarai.py#L792) | 792 | `"                    expires_at,"` | — |
| [SRC-C9CF9B54F8-L000793](../../agents/omarai.py#L793) | 793 | `"                ),"` | — |
| [SRC-C9CF9B54F8-L000794](../../agents/omarai.py#L794) | 794 | `"            )"` | — |
| [SRC-C9CF9B54F8-L000795](../../agents/omarai.py#L795) | 795 | `"        return session_id, principal"` | — |
| [SRC-C9CF9B54F8-L000796](../../agents/omarai.py#L796) | 796 | `""` | — |
| [SRC-C9CF9B54F8-L000797](../../agents/omarai.py#L797) | 797 | `"    def resolve_web_session("` | — |
| [SRC-C9CF9B54F8-L000798](../../agents/omarai.py#L798) | 798 | `"        self,"` | — |
| [SRC-C9CF9B54F8-L000799](../../agents/omarai.py#L799) | 799 | `"        session_id: str,"` | — |
| [SRC-C9CF9B54F8-L000800](../../agents/omarai.py#L800) | 800 | `"        *,"` | — |
| [SRC-C9CF9B54F8-L000801](../../agents/omarai.py#L801) | 801 | `"        shared_token: str = \"\","` | — |
| [SRC-C9CF9B54F8-L000802](../../agents/omarai.py#L802) | 802 | `"    ) -> dict \| None:"` | — |
| [SRC-C9CF9B54F8-L000803](../../agents/omarai.py#L803) | 803 | `"        \"\"\"Resolve an opaque browser session and re-check its backing credential.\"\"\""` | — |
| [SRC-C9CF9B54F8-L000804](../../agents/omarai.py#L804) | 804 | `"        if not isinstance(session_id, str) or not re.fullmatch("` | — |
| [SRC-C9CF9B54F8-L000805](../../agents/omarai.py#L805) | 805 | `"            r\"[A-Za-z0-9_-]{32,128}\", session_id"` | — |
| [SRC-C9CF9B54F8-L000806](../../agents/omarai.py#L806) | 806 | `"        ):"` | — |
| [SRC-C9CF9B54F8-L000807](../../agents/omarai.py#L807) | 807 | `"            return None"` | — |
| [SRC-C9CF9B54F8-L000808](../../agents/omarai.py#L808) | 808 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000809](../../agents/omarai.py#L809) | 809 | `"            session = db.execute("` | — |
| [SRC-C9CF9B54F8-L000810](../../agents/omarai.py#L810) | 810 | `"                \"\"\"SELECT credential_hash, is_shared_token, tenant_id, user_id"` | — |
| [SRC-C9CF9B54F8-L000811](../../agents/omarai.py#L811) | 811 | `"                   FROM web_sessions"` | — |
| [SRC-C9CF9B54F8-L000812](../../agents/omarai.py#L812) | 812 | `"                   WHERE session_hash=? AND revoked_at IS NULL AND expires_at > ?\"\"\","` | — |
| [SRC-C9CF9B54F8-L000813](../../agents/omarai.py#L813) | 813 | `"                (self._token_hash(session_id), now_utc()),"` | — |
| [SRC-C9CF9B54F8-L000814](../../agents/omarai.py#L814) | 814 | `"            ).fetchone()"` | — |
| [SRC-C9CF9B54F8-L000815](../../agents/omarai.py#L815) | 815 | `"            if not session:"` | — |
| [SRC-C9CF9B54F8-L000816](../../agents/omarai.py#L816) | 816 | `"                return None"` | — |
| [SRC-C9CF9B54F8-L000817](../../agents/omarai.py#L817) | 817 | `"            if session[\"is_shared_token\"]:"` | — |
| [SRC-C9CF9B54F8-L000818](../../agents/omarai.py#L818) | 818 | `"                if ("` | — |
| [SRC-C9CF9B54F8-L000819](../../agents/omarai.py#L819) | 819 | `"                    not shared_token"` | — |
| [SRC-C9CF9B54F8-L000820](../../agents/omarai.py#L820) | 820 | `"                    or not hmac.compare_digest("` | — |
| [SRC-C9CF9B54F8-L000821](../../agents/omarai.py#L821) | 821 | `"                        session[\"credential_hash\"], self._token_hash(shared_token)"` | — |
| [SRC-C9CF9B54F8-L000822](../../agents/omarai.py#L822) | 822 | `"                    )"` | — |
| [SRC-C9CF9B54F8-L000823](../../agents/omarai.py#L823) | 823 | `"                ):"` | — |
| [SRC-C9CF9B54F8-L000824](../../agents/omarai.py#L824) | 824 | `"                    return None"` | — |
| [SRC-C9CF9B54F8-L000825](../../agents/omarai.py#L825) | 825 | `"                principal = db.execute("` | — |
| [SRC-C9CF9B54F8-L000826](../../agents/omarai.py#L826) | 826 | `"                    \"\"\"SELECT m.tenant_id, m.user_id, m.role"` | — |
| [SRC-C9CF9B54F8-L000827](../../agents/omarai.py#L827) | 827 | `"                       FROM tenant_memberships m"` | — |
| [SRC-C9CF9B54F8-L000828](../../agents/omarai.py#L828) | 828 | `"                       JOIN tenants t ON t.id=m.tenant_id AND t.active=1"` | — |
| [SRC-C9CF9B54F8-L000829](../../agents/omarai.py#L829) | 829 | `"                       JOIN users u ON u.id=m.user_id AND u.active=1"` | — |
| [SRC-C9CF9B54F8-L000830](../../agents/omarai.py#L830) | 830 | `"                       WHERE m.tenant_id=? AND m.user_id=? AND m.active=1\"\"\","` | — |
| [SRC-C9CF9B54F8-L000831](../../agents/omarai.py#L831) | 831 | `"                    (session[\"tenant_id\"], session[\"user_id\"]),"` | — |
| [SRC-C9CF9B54F8-L000832](../../agents/omarai.py#L832) | 832 | `"                ).fetchone()"` | — |
| [SRC-C9CF9B54F8-L000833](../../agents/omarai.py#L833) | 833 | `"                return dict(principal) if principal else None"` | — |
| [SRC-C9CF9B54F8-L000834](../../agents/omarai.py#L834) | 834 | `""` | — |
| [SRC-C9CF9B54F8-L000835](../../agents/omarai.py#L835) | 835 | `"            principal = db.execute("` | — |
| [SRC-C9CF9B54F8-L000836](../../agents/omarai.py#L836) | 836 | `"                \"\"\"SELECT m.tenant_id, m.user_id, m.role"` | — |
| [SRC-C9CF9B54F8-L000837](../../agents/omarai.py#L837) | 837 | `"                   FROM api_tokens a"` | — |
| [SRC-C9CF9B54F8-L000838](../../agents/omarai.py#L838) | 838 | `"                   JOIN tenant_memberships m"` | — |
| [SRC-C9CF9B54F8-L000839](../../agents/omarai.py#L839) | 839 | `"                     ON m.tenant_id=a.tenant_id AND m.user_id=a.user_id"` | — |
| [SRC-C9CF9B54F8-L000840](../../agents/omarai.py#L840) | 840 | `"                   JOIN tenants t ON t.id=m.tenant_id AND t.active=1"` | — |
| [SRC-C9CF9B54F8-L000841](../../agents/omarai.py#L841) | 841 | `"                   JOIN users u ON u.id=m.user_id AND u.active=1"` | — |
| [SRC-C9CF9B54F8-L000842](../../agents/omarai.py#L842) | 842 | `"                   WHERE a.token_hash=? AND a.tenant_id=? AND a.user_id=?"` | — |
| [SRC-C9CF9B54F8-L000843](../../agents/omarai.py#L843) | 843 | `"                     AND a.active=1 AND m.active=1"` | — |
| [SRC-C9CF9B54F8-L000844](../../agents/omarai.py#L844) | 844 | `"                     AND (a.expires_at IS NULL OR a.expires_at > ?)\"\"\","` | — |
| [SRC-C9CF9B54F8-L000845](../../agents/omarai.py#L845) | 845 | `"                ("` | — |
| [SRC-C9CF9B54F8-L000846](../../agents/omarai.py#L846) | 846 | `"                    session[\"credential_hash\"],"` | — |
| [SRC-C9CF9B54F8-L000847](../../agents/omarai.py#L847) | 847 | `"                    session[\"tenant_id\"],"` | — |
| [SRC-C9CF9B54F8-L000848](../../agents/omarai.py#L848) | 848 | `"                    session[\"user_id\"],"` | — |
| [SRC-C9CF9B54F8-L000849](../../agents/omarai.py#L849) | 849 | `"                    now_utc(),"` | — |
| [SRC-C9CF9B54F8-L000850](../../agents/omarai.py#L850) | 850 | `"                ),"` | — |
| [SRC-C9CF9B54F8-L000851](../../agents/omarai.py#L851) | 851 | `"            ).fetchone()"` | — |
| [SRC-C9CF9B54F8-L000852](../../agents/omarai.py#L852) | 852 | `"        return dict(principal) if principal else None"` | — |
| [SRC-C9CF9B54F8-L000853](../../agents/omarai.py#L853) | 853 | `""` | — |
| [SRC-C9CF9B54F8-L000854](../../agents/omarai.py#L854) | 854 | `"    def revoke_web_session(self, session_id: str) -> bool:"` | — |
| [SRC-C9CF9B54F8-L000855](../../agents/omarai.py#L855) | 855 | `"        \"\"\"Revoke one opaque browser session without revoking its backing API token.\"\"\""` | — |
| [SRC-C9CF9B54F8-L000856](../../agents/omarai.py#L856) | 856 | `"        if not isinstance(session_id, str) or not re.fullmatch("` | — |
| [SRC-C9CF9B54F8-L000857](../../agents/omarai.py#L857) | 857 | `"            r\"[A-Za-z0-9_-]{32,128}\", session_id"` | — |
| [SRC-C9CF9B54F8-L000858](../../agents/omarai.py#L858) | 858 | `"        ):"` | — |
| [SRC-C9CF9B54F8-L000859](../../agents/omarai.py#L859) | 859 | `"            return False"` | — |
| [SRC-C9CF9B54F8-L000860](../../agents/omarai.py#L860) | 860 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000861](../../agents/omarai.py#L861) | 861 | `"            cursor = db.execute("` | — |
| [SRC-C9CF9B54F8-L000862](../../agents/omarai.py#L862) | 862 | `"                \"\"\"UPDATE web_sessions SET revoked_at=?"` | — |
| [SRC-C9CF9B54F8-L000863](../../agents/omarai.py#L863) | 863 | `"                   WHERE session_hash=? AND revoked_at IS NULL\"\"\","` | — |
| [SRC-C9CF9B54F8-L000864](../../agents/omarai.py#L864) | 864 | `"                (now_utc(), self._token_hash(session_id)),"` | — |
| [SRC-C9CF9B54F8-L000865](../../agents/omarai.py#L865) | 865 | `"            )"` | — |
| [SRC-C9CF9B54F8-L000866](../../agents/omarai.py#L866) | 866 | `"        return cursor.rowcount == 1"` | — |
| [SRC-C9CF9B54F8-L000867](../../agents/omarai.py#L867) | 867 | `""` | — |
| [SRC-C9CF9B54F8-L000868](../../agents/omarai.py#L868) | 868 | `"    def revoke_api_token("` | — |
| [SRC-C9CF9B54F8-L000869](../../agents/omarai.py#L869) | 869 | `"        self,"` | — |
| [SRC-C9CF9B54F8-L000870](../../agents/omarai.py#L870) | 870 | `"        token: str,"` | — |
| [SRC-C9CF9B54F8-L000871](../../agents/omarai.py#L871) | 871 | `"        *,"` | — |
| [SRC-C9CF9B54F8-L000872](../../agents/omarai.py#L872) | 872 | `"        tenant_id: str,"` | — |
| [SRC-C9CF9B54F8-L000873](../../agents/omarai.py#L873) | 873 | `"        user_id: str,"` | — |
| [SRC-C9CF9B54F8-L000874](../../agents/omarai.py#L874) | 874 | `"    ) -> bool:"` | — |
| [SRC-C9CF9B54F8-L000875](../../agents/omarai.py#L875) | 875 | `"        \"\"\"Revoke only a token owned by the authenticated user in the active tenant.\"\"\""` | — |
| [SRC-C9CF9B54F8-L000876](../../agents/omarai.py#L876) | 876 | `"        if not isinstance(token, str) or len(token.strip()) < 32:"` | — |
| [SRC-C9CF9B54F8-L000877](../../agents/omarai.py#L877) | 877 | `"            return False"` | — |
| [SRC-C9CF9B54F8-L000878](../../agents/omarai.py#L878) | 878 | `"        tenant = self._tenant(tenant_id)"` | — |
| [SRC-C9CF9B54F8-L000879](../../agents/omarai.py#L879) | 879 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000880](../../agents/omarai.py#L880) | 880 | `"            membership = db.execute("` | — |
| [SRC-C9CF9B54F8-L000881](../../agents/omarai.py#L881) | 881 | `"                \"\"\"SELECT 1 FROM tenant_memberships m"` | — |
| [SRC-C9CF9B54F8-L000882](../../agents/omarai.py#L882) | 882 | `"                   JOIN tenants t ON t.id=m.tenant_id AND t.active=1"` | — |
| [SRC-C9CF9B54F8-L000883](../../agents/omarai.py#L883) | 883 | `"                   JOIN users u ON u.id=m.user_id AND u.active=1"` | — |
| [SRC-C9CF9B54F8-L000884](../../agents/omarai.py#L884) | 884 | `"                   WHERE m.tenant_id=? AND m.user_id=? AND m.active=1\"\"\","` | — |
| [SRC-C9CF9B54F8-L000885](../../agents/omarai.py#L885) | 885 | `"                (tenant, user_id),"` | — |
| [SRC-C9CF9B54F8-L000886](../../agents/omarai.py#L886) | 886 | `"            ).fetchone()"` | — |
| [SRC-C9CF9B54F8-L000887](../../agents/omarai.py#L887) | 887 | `"            if not membership:"` | — |
| [SRC-C9CF9B54F8-L000888](../../agents/omarai.py#L888) | 888 | `"                return False"` | — |
| [SRC-C9CF9B54F8-L000889](../../agents/omarai.py#L889) | 889 | `"            cursor = db.execute("` | — |
| [SRC-C9CF9B54F8-L000890](../../agents/omarai.py#L890) | 890 | `"                \"\"\"UPDATE api_tokens SET active=0"` | — |
| [SRC-C9CF9B54F8-L000891](../../agents/omarai.py#L891) | 891 | `"                   WHERE token_hash=? AND tenant_id=? AND user_id=? AND active=1\"\"\","` | — |
| [SRC-C9CF9B54F8-L000892](../../agents/omarai.py#L892) | 892 | `"                (self._token_hash(token.strip()), tenant, user_id),"` | — |
| [SRC-C9CF9B54F8-L000893](../../agents/omarai.py#L893) | 893 | `"            )"` | — |
| [SRC-C9CF9B54F8-L000894](../../agents/omarai.py#L894) | 894 | `"        return cursor.rowcount == 1"` | — |
| [SRC-C9CF9B54F8-L000895](../../agents/omarai.py#L895) | 895 | `""` | — |
| [SRC-C9CF9B54F8-L000896](../../agents/omarai.py#L896) | 896 | `"    def add("` | — |
| [SRC-C9CF9B54F8-L000897](../../agents/omarai.py#L897) | 897 | `"        self,"` | — |
| [SRC-C9CF9B54F8-L000898](../../agents/omarai.py#L898) | 898 | `"        text: str,"` | — |
| [SRC-C9CF9B54F8-L000899](../../agents/omarai.py#L899) | 899 | `"        source_url: str,"` | — |
| [SRC-C9CF9B54F8-L000900](../../agents/omarai.py#L900) | 900 | `"        platform: str = \"manual\","` | — |
| [SRC-C9CF9B54F8-L000901](../../agents/omarai.py#L901) | 901 | `"        observed_at: str \| None = None,"` | — |
| [SRC-C9CF9B54F8-L000902](../../agents/omarai.py#L902) | 902 | `"        note: str = \"\","` | — |
| [SRC-C9CF9B54F8-L000903](../../agents/omarai.py#L903) | 903 | `"        product_terms=(),"` | — |
| [SRC-C9CF9B54F8-L000904](../../agents/omarai.py#L904) | 904 | `"        location_terms=(),"` | — |
| [SRC-C9CF9B54F8-L000905](../../agents/omarai.py#L905) | 905 | `"        *,"` | — |
| [SRC-C9CF9B54F8-L000906](../../agents/omarai.py#L906) | 906 | `"        tenant_id: str \| None = None,"` | — |
| [SRC-C9CF9B54F8-L000907](../../agents/omarai.py#L907) | 907 | `"    ):"` | — |
| [SRC-C9CF9B54F8-L000908](../../agents/omarai.py#L908) | 908 | `"        if not isinstance(text, str) or not text.strip():"` | — |
| [SRC-C9CF9B54F8-L000909](../../agents/omarai.py#L909) | 909 | `"            raise ValueError(\"text is required\")"` | — |
| [SRC-C9CF9B54F8-L000910](../../agents/omarai.py#L910) | 910 | `"        if len(text) > MAX_TEXT:"` | — |
| [SRC-C9CF9B54F8-L000911](../../agents/omarai.py#L911) | 911 | `"            raise ValueError(\"text is too long\")"` | — |
| [SRC-C9CF9B54F8-L000912](../../agents/omarai.py#L912) | 912 | `"        tenant = self._tenant(tenant_id)"` | — |
| [SRC-C9CF9B54F8-L000913](../../agents/omarai.py#L913) | 913 | `"        url = validate_url(source_url)"` | — |
| [SRC-C9CF9B54F8-L000914](../../agents/omarai.py#L914) | 914 | `"        normalized = normalize(text)"` | — |
| [SRC-C9CF9B54F8-L000915](../../agents/omarai.py#L915) | 915 | `"        fingerprint = hashlib.sha256("` | — |
| [SRC-C9CF9B54F8-L000916](../../agents/omarai.py#L916) | 916 | `"            (url.rstrip(\"/\") + \"\\n\" + normalized).encode()"` | — |
| [SRC-C9CF9B54F8-L000917](../../agents/omarai.py#L917) | 917 | `"        ).hexdigest()"` | — |
| [SRC-C9CF9B54F8-L000918](../../agents/omarai.py#L918) | 918 | `"        lead_id = hashlib.sha256("` | — |
| [SRC-C9CF9B54F8-L000919](../../agents/omarai.py#L919) | 919 | `"            (tenant + \"\\n\" + fingerprint).encode()"` | — |
| [SRC-C9CF9B54F8-L000920](../../agents/omarai.py#L920) | 920 | `"        ).hexdigest()[:24]"` | — |
| [SRC-C9CF9B54F8-L000921](../../agents/omarai.py#L921) | 921 | `"        timestamp = observed_at or now_utc()"` | — |
| [SRC-C9CF9B54F8-L000922](../../agents/omarai.py#L922) | 922 | `"        assessment = analyze(text, product_terms=product_terms, location_terms=location_terms)"` | — |
| [SRC-C9CF9B54F8-L000923](../../agents/omarai.py#L923) | 923 | `"        domain_observed_at = timestamp"` | — |
| [SRC-C9CF9B54F8-L000924](../../agents/omarai.py#L924) | 924 | `"        try:"` | — |
| [SRC-C9CF9B54F8-L000925](../../agents/omarai.py#L925) | 925 | `"            parsed_observed_at = datetime.fromisoformat(str(timestamp))"` | — |
| [SRC-C9CF9B54F8-L000926](../../agents/omarai.py#L926) | 926 | `"            if parsed_observed_at.tzinfo is None:"` | — |
| [SRC-C9CF9B54F8-L000927](../../agents/omarai.py#L927) | 927 | `"                domain_observed_at = None"` | — |
| [SRC-C9CF9B54F8-L000928](../../agents/omarai.py#L928) | 928 | `"        except (TypeError, ValueError):"` | — |
| [SRC-C9CF9B54F8-L000929](../../agents/omarai.py#L929) | 929 | `"            domain_observed_at = None"` | — |
| [SRC-C9CF9B54F8-L000930](../../agents/omarai.py#L930) | 930 | `"        evidence = DemandEvidence("` | — |
| [SRC-C9CF9B54F8-L000931](../../agents/omarai.py#L931) | 931 | `"            source_id=lead_id,"` | — |
| [SRC-C9CF9B54F8-L000932](../../agents/omarai.py#L932) | 932 | `"            source_url=url,"` | — |
| [SRC-C9CF9B54F8-L000933](../../agents/omarai.py#L933) | 933 | `"            excerpt=text.strip()[:2_000],"` | — |
| [SRC-C9CF9B54F8-L000934](../../agents/omarai.py#L934) | 934 | `"            content_basis=EvidenceBasis.USER_PROVIDED,"` | — |
| [SRC-C9CF9B54F8-L000935](../../agents/omarai.py#L935) | 935 | `"            observed_at=domain_observed_at,"` | — |
| [SRC-C9CF9B54F8-L000936](../../agents/omarai.py#L936) | 936 | `"            page_read=False,"` | — |
| [SRC-C9CF9B54F8-L000937](../../agents/omarai.py#L937) | 937 | `"        )"` | — |
| [SRC-C9CF9B54F8-L000938](../../agents/omarai.py#L938) | 938 | `"        domain_signal = DemandSignal("` | — |
| [SRC-C9CF9B54F8-L000939](../../agents/omarai.py#L939) | 939 | `"            signal_id=lead_id,"` | — |
| [SRC-C9CF9B54F8-L000940](../../agents/omarai.py#L940) | 940 | `"            signal_type=DemandSignalType(assessment[\"signal_type\"]),"` | — |
| [SRC-C9CF9B54F8-L000941](../../agents/omarai.py#L941) | 941 | `"            evidence=evidence,"` | — |
| [SRC-C9CF9B54F8-L000942](../../agents/omarai.py#L942) | 942 | `"            product_fit=ProductFit.UNASSESSED,"` | — |
| [SRC-C9CF9B54F8-L000943](../../agents/omarai.py#L943) | 943 | `"            identity_status=IdentityStatus.UNKNOWN,"` | — |
| [SRC-C9CF9B54F8-L000944](../../agents/omarai.py#L944) | 944 | `"            classification_reason=assessment[\"summary\"],"` | — |
| [SRC-C9CF9B54F8-L000945](../../agents/omarai.py#L945) | 945 | `"        )"` | — |
| [SRC-C9CF9B54F8-L000946](../../agents/omarai.py#L946) | 946 | `"        qualification = LeadQualification("` | — |
| [SRC-C9CF9B54F8-L000947](../../agents/omarai.py#L947) | 947 | `"            signal_id=lead_id,"` | — |
| [SRC-C9CF9B54F8-L000948](../../agents/omarai.py#L948) | 948 | `"            product_fit=ProductFit.UNASSESSED,"` | — |
| [SRC-C9CF9B54F8-L000949](../../agents/omarai.py#L949) | 949 | `"            source_quality=SourceQuality.UNKNOWN,"` | — |
| [SRC-C9CF9B54F8-L000950](../../agents/omarai.py#L950) | 950 | `"            freshness=FreshnessStatus.UNKNOWN,"` | — |
| [SRC-C9CF9B54F8-L000951](../../agents/omarai.py#L951) | 951 | `"            identity_status=IdentityStatus.UNKNOWN,"` | — |
| [SRC-C9CF9B54F8-L000952](../../agents/omarai.py#L952) | 952 | `"            contactability=ContactabilityStatus.NOT_ASSESSED,"` | — |
| [SRC-C9CF9B54F8-L000953](../../agents/omarai.py#L953) | 953 | `"            missing_information=("` | — |
| [SRC-C9CF9B54F8-L000954](../../agents/omarai.py#L954) | 954 | `"                \"product_fit\", \"source_quality\", \"freshness\","` | — |
| [SRC-C9CF9B54F8-L000955](../../agents/omarai.py#L955) | 955 | `"                \"identity\", \"contactability\","` | — |
| [SRC-C9CF9B54F8-L000956](../../agents/omarai.py#L956) | 956 | `"            ),"` | — |
| [SRC-C9CF9B54F8-L000957](../../agents/omarai.py#L957) | 957 | `"        )"` | — |
| [SRC-C9CF9B54F8-L000958](../../agents/omarai.py#L958) | 958 | `"        assessment[\"domain_signal\"] = domain_signal.to_dict()"` | — |
| [SRC-C9CF9B54F8-L000959](../../agents/omarai.py#L959) | 959 | `"        assessment[\"qualification\"] = qualification.to_dict()"` | — |
| [SRC-C9CF9B54F8-L000960](../../agents/omarai.py#L960) | 960 | `"        now = now_utc()"` | — |
| [SRC-C9CF9B54F8-L000961](../../agents/omarai.py#L961) | 961 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000962](../../agents/omarai.py#L962) | 962 | `"            active_tenant = db.execute("` | — |
| [SRC-C9CF9B54F8-L000963](../../agents/omarai.py#L963) | 963 | `"                \"SELECT 1 FROM tenants WHERE id=? AND active=1\", (tenant,)"` | — |
| [SRC-C9CF9B54F8-L000964](../../agents/omarai.py#L964) | 964 | `"            ).fetchone()"` | — |
| [SRC-C9CF9B54F8-L000965](../../agents/omarai.py#L965) | 965 | `"            if not active_tenant:"` | — |
| [SRC-C9CF9B54F8-L000966](../../agents/omarai.py#L966) | 966 | `"                raise ValueError(\"active tenant is required\")"` | — |
| [SRC-C9CF9B54F8-L000967](../../agents/omarai.py#L967) | 967 | `"            cursor = db.execute("` | — |
| [SRC-C9CF9B54F8-L000968](../../agents/omarai.py#L968) | 968 | `"                \"\"\"INSERT OR IGNORE INTO leads"` | — |
| [SRC-C9CF9B54F8-L000969](../../agents/omarai.py#L969) | 969 | `"                   (id, tenant_id, fingerprint, text, source_url, platform, observed_at,"` | — |
| [SRC-C9CF9B54F8-L000970](../../agents/omarai.py#L970) | 970 | `"                    assessment, status, note, created_at, updated_at)"` | — |
| [SRC-C9CF9B54F8-L000971](../../agents/omarai.py#L971) | 971 | `"                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)\"\"\","` | — |
| [SRC-C9CF9B54F8-L000972](../../agents/omarai.py#L972) | 972 | `"                ("` | — |
| [SRC-C9CF9B54F8-L000973](../../agents/omarai.py#L973) | 973 | `"                    lead_id, tenant, fingerprint, text.strip(), url,"` | — |
| [SRC-C9CF9B54F8-L000974](../../agents/omarai.py#L974) | 974 | `"                    str(platform)[:80], timestamp,"` | — |
| [SRC-C9CF9B54F8-L000975](../../agents/omarai.py#L975) | 975 | `"                    json.dumps(assessment, ensure_ascii=False), \"new\","` | — |
| [SRC-C9CF9B54F8-L000976](../../agents/omarai.py#L976) | 976 | `"                    str(note)[:1000], now, now,"` | — |
| [SRC-C9CF9B54F8-L000977](../../agents/omarai.py#L977) | 977 | `"                ),"` | — |
| [SRC-C9CF9B54F8-L000978](../../agents/omarai.py#L978) | 978 | `"            )"` | — |
| [SRC-C9CF9B54F8-L000979](../../agents/omarai.py#L979) | 979 | `"            row = db.execute("` | — |
| [SRC-C9CF9B54F8-L000980](../../agents/omarai.py#L980) | 980 | `"                \"SELECT * FROM leads WHERE tenant_id=? AND fingerprint=?\","` | — |
| [SRC-C9CF9B54F8-L000981](../../agents/omarai.py#L981) | 981 | `"                (tenant, fingerprint),"` | — |
| [SRC-C9CF9B54F8-L000982](../../agents/omarai.py#L982) | 982 | `"            ).fetchone()"` | — |
| [SRC-C9CF9B54F8-L000983](../../agents/omarai.py#L983) | 983 | `"        return self.to_dict(row), cursor.rowcount == 1"` | — |
| [SRC-C9CF9B54F8-L000984](../../agents/omarai.py#L984) | 984 | `""` | — |
| [SRC-C9CF9B54F8-L000985](../../agents/omarai.py#L985) | 985 | `"    @staticmethod"` | — |
| [SRC-C9CF9B54F8-L000986](../../agents/omarai.py#L986) | 986 | `"    def to_dict(row):"` | — |
| [SRC-C9CF9B54F8-L000987](../../agents/omarai.py#L987) | 987 | `"        item = dict(row)"` | — |
| [SRC-C9CF9B54F8-L000988](../../agents/omarai.py#L988) | 988 | `"        item[\"assessment\"] = json.loads(item[\"assessment\"])"` | — |
| [SRC-C9CF9B54F8-L000989](../../agents/omarai.py#L989) | 989 | `"        return item"` | — |
| [SRC-C9CF9B54F8-L000990](../../agents/omarai.py#L990) | 990 | `""` | — |
| [SRC-C9CF9B54F8-L000991](../../agents/omarai.py#L991) | 991 | `"    def list("` | — |
| [SRC-C9CF9B54F8-L000992](../../agents/omarai.py#L992) | 992 | `"        self,"` | — |
| [SRC-C9CF9B54F8-L000993](../../agents/omarai.py#L993) | 993 | `"        status: str \| None = None,"` | — |
| [SRC-C9CF9B54F8-L000994](../../agents/omarai.py#L994) | 994 | `"        limit: int = 100,"` | — |
| [SRC-C9CF9B54F8-L000995](../../agents/omarai.py#L995) | 995 | `"        *,"` | — |
| [SRC-C9CF9B54F8-L000996](../../agents/omarai.py#L996) | 996 | `"        tenant_id: str \| None = None,"` | — |
| [SRC-C9CF9B54F8-L000997](../../agents/omarai.py#L997) | 997 | `"    ):"` | — |
| [SRC-C9CF9B54F8-L000998](../../agents/omarai.py#L998) | 998 | `"        tenant = self._tenant(tenant_id)"` | — |
| [SRC-C9CF9B54F8-L000999](../../agents/omarai.py#L999) | 999 | `"        limit = max(1, min(int(limit), 500))"` | — |
| [SRC-C9CF9B54F8-L001000](../../agents/omarai.py#L1000) | 1000 | `"        query = \"SELECT * FROM leads WHERE tenant_id=?\""` | — |
| [SRC-C9CF9B54F8-L001001](../../agents/omarai.py#L1001) | 1001 | `"        params: list[object] = [tenant]"` | — |
| [SRC-C9CF9B54F8-L001002](../../agents/omarai.py#L1002) | 1002 | `"        if status is not None:"` | — |
| [SRC-C9CF9B54F8-L001003](../../agents/omarai.py#L1003) | 1003 | `"            query += \" AND status=?\""` | — |
| [SRC-C9CF9B54F8-L001004](../../agents/omarai.py#L1004) | 1004 | `"            params.append(status)"` | — |
| [SRC-C9CF9B54F8-L001005](../../agents/omarai.py#L1005) | 1005 | `"        query += \" ORDER BY created_at DESC LIMIT ?\""` | — |
| [SRC-C9CF9B54F8-L001006](../../agents/omarai.py#L1006) | 1006 | `"        params.append(limit)"` | — |
| [SRC-C9CF9B54F8-L001007](../../agents/omarai.py#L1007) | 1007 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L001008](../../agents/omarai.py#L1008) | 1008 | `"            rows = db.execute(query, tuple(params)).fetchall()"` | — |
| [SRC-C9CF9B54F8-L001009](../../agents/omarai.py#L1009) | 1009 | `"        return [self.to_dict(row) for row in rows]"` | — |
| [SRC-C9CF9B54F8-L001010](../../agents/omarai.py#L1010) | 1010 | `""` | — |
| [SRC-C9CF9B54F8-L001011](../../agents/omarai.py#L1011) | 1011 | `"    def update_status("` | — |
| [SRC-C9CF9B54F8-L001012](../../agents/omarai.py#L1012) | 1012 | `"        self,"` | — |
| [SRC-C9CF9B54F8-L001013](../../agents/omarai.py#L1013) | 1013 | `"        lead_id: str,"` | — |
| [SRC-C9CF9B54F8-L001014](../../agents/omarai.py#L1014) | 1014 | `"        status: str,"` | — |
| [SRC-C9CF9B54F8-L001015](../../agents/omarai.py#L1015) | 1015 | `"        *,"` | — |
| [SRC-C9CF9B54F8-L001016](../../agents/omarai.py#L1016) | 1016 | `"        tenant_id: str \| None = None,"` | — |
| [SRC-C9CF9B54F8-L001017](../../agents/omarai.py#L1017) | 1017 | `"    ):"` | — |
| [SRC-C9CF9B54F8-L001018](../../agents/omarai.py#L1018) | 1018 | `"        if status not in self.ALLOWED_STATUSES:"` | — |
| [SRC-C9CF9B54F8-L001019](../../agents/omarai.py#L1019) | 1019 | `"            raise ValueError(\"unsupported status\")"` | — |
| [SRC-C9CF9B54F8-L001020](../../agents/omarai.py#L1020) | 1020 | `"        tenant = self._tenant(tenant_id)"` | — |
| [SRC-C9CF9B54F8-L001021](../../agents/omarai.py#L1021) | 1021 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L001022](../../agents/omarai.py#L1022) | 1022 | `"            db.execute("` | — |
| [SRC-C9CF9B54F8-L001023](../../agents/omarai.py#L1023) | 1023 | `"                \"UPDATE leads SET status=?, updated_at=? WHERE id=? AND tenant_id=?\","` | — |
| [SRC-C9CF9B54F8-L001024](../../agents/omarai.py#L1024) | 1024 | `"                (status, now_utc(), lead_id, tenant),"` | — |
| [SRC-C9CF9B54F8-L001025](../../agents/omarai.py#L1025) | 1025 | `"            )"` | — |
| [SRC-C9CF9B54F8-L001026](../../agents/omarai.py#L1026) | 1026 | `"            row = db.execute("` | — |
| [SRC-C9CF9B54F8-L001027](../../agents/omarai.py#L1027) | 1027 | `"                \"SELECT * FROM leads WHERE id=? AND tenant_id=?\","` | — |
| [SRC-C9CF9B54F8-L001028](../../agents/omarai.py#L1028) | 1028 | `"                (lead_id, tenant),"` | — |
| [SRC-C9CF9B54F8-L001029](../../agents/omarai.py#L1029) | 1029 | `"            ).fetchone()"` | — |
| [SRC-C9CF9B54F8-L001030](../../agents/omarai.py#L1030) | 1030 | `"        return self.to_dict(row) if row else None"` | — |
| [SRC-C9CF9B54F8-L001031](../../agents/omarai.py#L1031) | 1031 | `""` | — |
| [SRC-C9CF9B54F8-L001032](../../agents/omarai.py#L1032) | 1032 | `"    @staticmethod"` | — |
| [SRC-C9CF9B54F8-L001033](../../agents/omarai.py#L1033) | 1033 | `"    def _product_profile_row(row):"` | — |
| [SRC-C9CF9B54F8-L001034](../../agents/omarai.py#L1034) | 1034 | `"        if row is None:"` | — |
| [SRC-C9CF9B54F8-L001035](../../agents/omarai.py#L1035) | 1035 | `"            return None"` | — |
| [SRC-C9CF9B54F8-L001036](../../agents/omarai.py#L1036) | 1036 | `"        return {"` | — |
| [SRC-C9CF9B54F8-L001037](../../agents/omarai.py#L1037) | 1037 | `"            \"id\": row[\"id\"],"` | — |
| [SRC-C9CF9B54F8-L001038](../../agents/omarai.py#L1038) | 1038 | `"            \"name\": row[\"name\"],"` | — |
| [SRC-C9CF9B54F8-L001039](../../agents/omarai.py#L1039) | 1039 | `"            \"profile\": json.loads(row[\"profile_json\"]),"` | — |
| [SRC-C9CF9B54F8-L001040](../../agents/omarai.py#L1040) | 1040 | `"            \"created_at\": row[\"created_at\"],"` | — |
| [SRC-C9CF9B54F8-L001041](../../agents/omarai.py#L1041) | 1041 | `"            \"updated_at\": row[\"updated_at\"],"` | — |
| [SRC-C9CF9B54F8-L001042](../../agents/omarai.py#L1042) | 1042 | `"        }"` | — |
| [SRC-C9CF9B54F8-L001043](../../agents/omarai.py#L1043) | 1043 | `""` | — |
| [SRC-C9CF9B54F8-L001044](../../agents/omarai.py#L1044) | 1044 | `"    def save_product_profile(self, profile: dict, *, tenant_id: str):"` | — |
| [SRC-C9CF9B54F8-L001045](../../agents/omarai.py#L1045) | 1045 | `"        if not isinstance(profile, dict):"` | — |
| [SRC-C9CF9B54F8-L001046](../../agents/omarai.py#L1046) | 1046 | `"            raise TypeError(\"profile must be an object\")"` | — |
| [SRC-C9CF9B54F8-L001047](../../agents/omarai.py#L1047) | 1047 | `"        product = profile.get(\"product\")"` | — |
| [SRC-C9CF9B54F8-L001048](../../agents/omarai.py#L1048) | 1048 | `"        if not isinstance(product, dict):"` | — |
| [SRC-C9CF9B54F8-L001049](../../agents/omarai.py#L1049) | 1049 | `"            raise TypeError(\"product profile is required\")"` | — |
| [SRC-C9CF9B54F8-L001050](../../agents/omarai.py#L1050) | 1050 | `"        name = str(product.get(\"name\") or \"\").strip()"` | — |
| [SRC-C9CF9B54F8-L001051](../../agents/omarai.py#L1051) | 1051 | `"        if not name or len(name) > 240:"` | — |
| [SRC-C9CF9B54F8-L001052](../../agents/omarai.py#L1052) | 1052 | `"            raise ValueError(\"product name is required and must be at most 240 characters\")"` | — |
| [SRC-C9CF9B54F8-L001053](../../agents/omarai.py#L1053) | 1053 | `"        normalized_name = normalize(name)"` | — |
| [SRC-C9CF9B54F8-L001054](../../agents/omarai.py#L1054) | 1054 | `"        if not normalized_name:"` | — |
| [SRC-C9CF9B54F8-L001055](../../agents/omarai.py#L1055) | 1055 | `"            raise ValueError(\"product name is invalid\")"` | — |
| [SRC-C9CF9B54F8-L001056](../../agents/omarai.py#L1056) | 1056 | `"        encoded = json.dumps(profile, ensure_ascii=False, separators=(\",\", \":\"))"` | — |
| [SRC-C9CF9B54F8-L001057](../../agents/omarai.py#L1057) | 1057 | `"        if len(encoded) > 30000:"` | — |
| [SRC-C9CF9B54F8-L001058](../../agents/omarai.py#L1058) | 1058 | `"            raise ValueError(\"product profile is too large\")"` | — |
| [SRC-C9CF9B54F8-L001059](../../agents/omarai.py#L1059) | 1059 | `"        tenant = self._tenant(tenant_id)"` | — |
| [SRC-C9CF9B54F8-L001060](../../agents/omarai.py#L1060) | 1060 | `"        now = now_utc()"` | — |
| [SRC-C9CF9B54F8-L001061](../../agents/omarai.py#L1061) | 1061 | `"        profile_id = \"profile_\" + uuid.uuid4().hex"` | — |
| [SRC-C9CF9B54F8-L001062](../../agents/omarai.py#L1062) | 1062 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L001063](../../agents/omarai.py#L1063) | 1063 | `"            active_tenant = db.execute("` | — |
| [SRC-C9CF9B54F8-L001064](../../agents/omarai.py#L1064) | 1064 | `"                \"SELECT 1 FROM tenants WHERE id=? AND active=1\", (tenant,)"` | — |
| [SRC-C9CF9B54F8-L001065](../../agents/omarai.py#L1065) | 1065 | `"            ).fetchone()"` | — |
| [SRC-C9CF9B54F8-L001066](../../agents/omarai.py#L1066) | 1066 | `"            if not active_tenant:"` | — |
| [SRC-C9CF9B54F8-L001067](../../agents/omarai.py#L1067) | 1067 | `"                raise ValueError(\"active tenant is required\")"` | — |
| [SRC-C9CF9B54F8-L001068](../../agents/omarai.py#L1068) | 1068 | `"            db.execute("` | — |
| [SRC-C9CF9B54F8-L001069](../../agents/omarai.py#L1069) | 1069 | `"                \"\"\"INSERT INTO product_profiles"` | — |
| [SRC-C9CF9B54F8-L001070](../../agents/omarai.py#L1070) | 1070 | `"                   (id, tenant_id, normalized_name, name, profile_json, created_at, updated_at)"` | — |
| [SRC-C9CF9B54F8-L001071](../../agents/omarai.py#L1071) | 1071 | `"                   VALUES (?, ?, ?, ?, ?, ?, ?)"` | — |
| [SRC-C9CF9B54F8-L001072](../../agents/omarai.py#L1072) | 1072 | `"                   ON CONFLICT(tenant_id, normalized_name)"` | — |
| [SRC-C9CF9B54F8-L001073](../../agents/omarai.py#L1073) | 1073 | `"                   DO UPDATE SET name=excluded.name,"` | — |
| [SRC-C9CF9B54F8-L001074](../../agents/omarai.py#L1074) | 1074 | `"                                 profile_json=excluded.profile_json,"` | — |
| [SRC-C9CF9B54F8-L001075](../../agents/omarai.py#L1075) | 1075 | `"                                 updated_at=excluded.updated_at\"\"\","` | — |
| [SRC-C9CF9B54F8-L001076](../../agents/omarai.py#L1076) | 1076 | `"                (profile_id, tenant, normalized_name, name, encoded, now, now),"` | — |
| [SRC-C9CF9B54F8-L001077](../../agents/omarai.py#L1077) | 1077 | `"            )"` | — |
| [SRC-C9CF9B54F8-L001078](../../agents/omarai.py#L1078) | 1078 | `"            row = db.execute("` | — |
| [SRC-C9CF9B54F8-L001079](../../agents/omarai.py#L1079) | 1079 | `"                \"\"\"SELECT id, name, profile_json, created_at, updated_at"` | — |
| [SRC-C9CF9B54F8-L001080](../../agents/omarai.py#L1080) | 1080 | `"                   FROM product_profiles"` | — |
| [SRC-C9CF9B54F8-L001081](../../agents/omarai.py#L1081) | 1081 | `"                   WHERE tenant_id=? AND normalized_name=?\"\"\","` | — |
| [SRC-C9CF9B54F8-L001082](../../agents/omarai.py#L1082) | 1082 | `"                (tenant, normalized_name),"` | — |
| [SRC-C9CF9B54F8-L001083](../../agents/omarai.py#L1083) | 1083 | `"            ).fetchone()"` | — |
| [SRC-C9CF9B54F8-L001084](../../agents/omarai.py#L1084) | 1084 | `"        return self._product_profile_row(row)"` | — |
| [SRC-C9CF9B54F8-L001085](../../agents/omarai.py#L1085) | 1085 | `""` | — |
| [SRC-C9CF9B54F8-L001086](../../agents/omarai.py#L1086) | 1086 | `"    def list_product_profiles(self, *, tenant_id: str):"` | — |
| [SRC-C9CF9B54F8-L001087](../../agents/omarai.py#L1087) | 1087 | `"        tenant = self._tenant(tenant_id)"` | — |
| [SRC-C9CF9B54F8-L001088](../../agents/omarai.py#L1088) | 1088 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L001089](../../agents/omarai.py#L1089) | 1089 | `"            rows = db.execute("` | — |
| [SRC-C9CF9B54F8-L001090](../../agents/omarai.py#L1090) | 1090 | `"                \"\"\"SELECT id, name, profile_json, created_at, updated_at"` | — |
| [SRC-C9CF9B54F8-L001091](../../agents/omarai.py#L1091) | 1091 | `"                   FROM product_profiles WHERE tenant_id=?"` | — |
| [SRC-C9CF9B54F8-L001092](../../agents/omarai.py#L1092) | 1092 | `"                   ORDER BY updated_at DESC, id LIMIT 100\"\"\","` | — |
| [SRC-C9CF9B54F8-L001093](../../agents/omarai.py#L1093) | 1093 | `"                (tenant,),"` | — |
| [SRC-C9CF9B54F8-L001094](../../agents/omarai.py#L1094) | 1094 | `"            ).fetchall()"` | — |
| [SRC-C9CF9B54F8-L001095](../../agents/omarai.py#L1095) | 1095 | `"        return [self._product_profile_row(row) for row in rows]"` | — |
| [SRC-C9CF9B54F8-L001096](../../agents/omarai.py#L1096) | 1096 | `""` | — |
| [SRC-C9CF9B54F8-L001097](../../agents/omarai.py#L1097) | 1097 | `"    def get_product_profile(self, profile_id: str, *, tenant_id: str):"` | — |
| [SRC-C9CF9B54F8-L001098](../../agents/omarai.py#L1098) | 1098 | `"        if not isinstance(profile_id, str) or not profile_id.strip():"` | — |
| [SRC-C9CF9B54F8-L001099](../../agents/omarai.py#L1099) | 1099 | `"            return None"` | — |
| [SRC-C9CF9B54F8-L001100](../../agents/omarai.py#L1100) | 1100 | `"        tenant = self._tenant(tenant_id)"` | — |
| [SRC-C9CF9B54F8-L001101](../../agents/omarai.py#L1101) | 1101 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L001102](../../agents/omarai.py#L1102) | 1102 | `"            row = db.execute("` | — |
| [SRC-C9CF9B54F8-L001103](../../agents/omarai.py#L1103) | 1103 | `"                \"\"\"SELECT id, name, profile_json, created_at, updated_at"` | — |
| [SRC-C9CF9B54F8-L001104](../../agents/omarai.py#L1104) | 1104 | `"                   FROM product_profiles WHERE id=? AND tenant_id=?\"\"\","` | — |
| [SRC-C9CF9B54F8-L001105](../../agents/omarai.py#L1105) | 1105 | `"                (profile_id.strip(), tenant),"` | — |
| [SRC-C9CF9B54F8-L001106](../../agents/omarai.py#L1106) | 1106 | `"            ).fetchone()"` | — |
| [SRC-C9CF9B54F8-L001107](../../agents/omarai.py#L1107) | 1107 | `"        return self._product_profile_row(row)"` | — |
| [SRC-C9CF9B54F8-L001108](../../agents/omarai.py#L1108) | 1108 | `""` | — |
| [SRC-C9CF9B54F8-L001109](../../agents/omarai.py#L1109) | 1109 | `"    @staticmethod"` | — |
| [SRC-C9CF9B54F8-L001110](../../agents/omarai.py#L1110) | 1110 | `"    def _safe_discovery_source(source: dict):"` | — |
| [SRC-C9CF9B54F8-L001111](../../agents/omarai.py#L1111) | 1111 | `"        from urllib.parse import urlparse"` | — |
| [SRC-C9CF9B54F8-L001112](../../agents/omarai.py#L1112) | 1112 | `""` | — |
| [SRC-C9CF9B54F8-L001113](../../agents/omarai.py#L1113) | 1113 | `"        title = str(source.get(\"title\") or \"\")[:300].strip()"` | — |
| [SRC-C9CF9B54F8-L001114](../../agents/omarai.py#L1114) | 1114 | `"        snippet = str(source.get(\"snippet\") or \"\")[:1600].strip()"` | — |
| [SRC-C9CF9B54F8-L001115](../../agents/omarai.py#L1115) | 1115 | `"        source_url = validate_url(source.get(\"url\", \"\"))"` | — |
| [SRC-C9CF9B54F8-L001116](../../agents/omarai.py#L1116) | 1116 | `"        parsed = urlparse(source_url)"` | — |
| [SRC-C9CF9B54F8-L001117](../../agents/omarai.py#L1117) | 1117 | `"        hostname = (parsed.hostname or \"\").lower().rstrip(\".\")"` | — |
| [SRC-C9CF9B54F8-L001118](../../agents/omarai.py#L1118) | 1118 | `"        if hostname == \"localhost\" or hostname.endswith((\".localhost\", \".local\")):"` | — |
| [SRC-C9CF9B54F8-L001119](../../agents/omarai.py#L1119) | 1119 | `"            raise ValueError(\"discovery source URL is not public\")"` | — |
| [SRC-C9CF9B54F8-L001120](../../agents/omarai.py#L1120) | 1120 | `"        try:"` | — |
| [SRC-C9CF9B54F8-L001121](../../agents/omarai.py#L1121) | 1121 | `"            address = ipaddress.ip_address(hostname)"` | — |
| [SRC-C9CF9B54F8-L001122](../../agents/omarai.py#L1122) | 1122 | `"        except ValueError:"` | — |
| [SRC-C9CF9B54F8-L001123](../../agents/omarai.py#L1123) | 1123 | `"            address = None"` | — |
| [SRC-C9CF9B54F8-L001124](../../agents/omarai.py#L1124) | 1124 | `"        if address is not None and not address.is_global:"` | — |
| [SRC-C9CF9B54F8-L001125](../../agents/omarai.py#L1125) | 1125 | `"            raise ValueError(\"discovery source URL is not public\")"` | — |
| [SRC-C9CF9B54F8-L001126](../../agents/omarai.py#L1126) | 1126 | `"        evidence = source.get(\"lead_intent_evidence\")"` | — |
| [SRC-C9CF9B54F8-L001127](../../agents/omarai.py#L1127) | 1127 | `"        safe_evidence = None"` | — |
| [SRC-C9CF9B54F8-L001128](../../agents/omarai.py#L1128) | 1128 | `"        if isinstance(evidence, dict):"` | — |
| [SRC-C9CF9B54F8-L001129](../../agents/omarai.py#L1129) | 1129 | `"            safe_evidence = {"` | — |
| [SRC-C9CF9B54F8-L001130](../../agents/omarai.py#L1130) | 1130 | `"                \"phrase\": str(evidence.get(\"phrase\") or \"\")[:500],"` | — |
| [SRC-C9CF9B54F8-L001131](../../agents/omarai.py#L1131) | 1131 | `"                \"basis\": str(evidence.get(\"basis\") or \"\")[:40],"` | — |
| [SRC-C9CF9B54F8-L001132](../../agents/omarai.py#L1132) | 1132 | `"                \"signal_type\": str(evidence.get(\"signal_type\") or \"\")[:80],"` | — |
| [SRC-C9CF9B54F8-L001133](../../agents/omarai.py#L1133) | 1133 | `"                \"product_fit\": str(evidence.get(\"product_fit\") or \"unassessed\")[:40],"` | — |
| [SRC-C9CF9B54F8-L001134](../../agents/omarai.py#L1134) | 1134 | `"            }"` | — |
| [SRC-C9CF9B54F8-L001135](../../agents/omarai.py#L1135) | 1135 | `"        providers = source.get(\"providers\")"` | — |
| [SRC-C9CF9B54F8-L001136](../../agents/omarai.py#L1136) | 1136 | `"        queries = source.get(\"queries\")"` | — |
| [SRC-C9CF9B54F8-L001137](../../agents/omarai.py#L1137) | 1137 | `"        return {"` | — |
| [SRC-C9CF9B54F8-L001138](../../agents/omarai.py#L1138) | 1138 | `"            \"title\": title,"` | — |
| [SRC-C9CF9B54F8-L001139](../../agents/omarai.py#L1139) | 1139 | `"            \"url\": source_url,"` | — |
| [SRC-C9CF9B54F8-L001140](../../agents/omarai.py#L1140) | 1140 | `"            \"snippet\": snippet,"` | — |
| [SRC-C9CF9B54F8-L001141](../../agents/omarai.py#L1141) | 1141 | `"            \"platform\": str(source.get(\"platform\") or \"web\")[:80],"` | — |
| [SRC-C9CF9B54F8-L001142](../../agents/omarai.py#L1142) | 1142 | `"            \"domain\": str(source.get(\"domain\") or \"\")[:253],"` | — |
| [SRC-C9CF9B54F8-L001143](../../agents/omarai.py#L1143) | 1143 | `"            \"published_at\": ("` | — |
| [SRC-C9CF9B54F8-L001144](../../agents/omarai.py#L1144) | 1144 | `"                str(source.get(\"published_at\"))[:120]"` | — |
| [SRC-C9CF9B54F8-L001145](../../agents/omarai.py#L1145) | 1145 | `"                if source.get(\"published_at\") is not None else None"` | — |
| [SRC-C9CF9B54F8-L001146](../../agents/omarai.py#L1146) | 1146 | `"            ),"` | — |
| [SRC-C9CF9B54F8-L001147](../../agents/omarai.py#L1147) | 1147 | `"            \"page_fetched\": source.get(\"page_fetched\") is True,"` | — |
| [SRC-C9CF9B54F8-L001148](../../agents/omarai.py#L1148) | 1148 | `"            \"readable_page_text_available\": source.get(\"readable_page_text_available\") is True,"` | — |
| [SRC-C9CF9B54F8-L001149](../../agents/omarai.py#L1149) | 1149 | `"            \"providers\": ["` | — |
| [SRC-C9CF9B54F8-L001150](../../agents/omarai.py#L1150) | 1150 | `"                str(value)[:80] for value in providers[:8] if isinstance(value, str)"` | — |
| [SRC-C9CF9B54F8-L001151](../../agents/omarai.py#L1151) | 1151 | `"            ] if isinstance(providers, list) else [],"` | — |
| [SRC-C9CF9B54F8-L001152](../../agents/omarai.py#L1152) | 1152 | `"            \"queries\": ["` | — |
| [SRC-C9CF9B54F8-L001153](../../agents/omarai.py#L1153) | 1153 | `"                str(value)[:500] for value in queries[:8] if isinstance(value, str)"` | — |
| [SRC-C9CF9B54F8-L001154](../../agents/omarai.py#L1154) | 1154 | `"            ] if isinstance(queries, list) else [],"` | — |
| [SRC-C9CF9B54F8-L001155](../../agents/omarai.py#L1155) | 1155 | `"            \"lead_qualification\": ("` | — |
| [SRC-C9CF9B54F8-L001156](../../agents/omarai.py#L1156) | 1156 | `"                \"public_demand_signal\""` | — |
| [SRC-C9CF9B54F8-L001157](../../agents/omarai.py#L1157) | 1157 | `"                if source.get(\"lead_qualification\") == \"public_demand_signal\""` | — |
| [SRC-C9CF9B54F8-L001158](../../agents/omarai.py#L1158) | 1158 | `"                else \"related_result_not_lead\""` | — |
| [SRC-C9CF9B54F8-L001159](../../agents/omarai.py#L1159) | 1159 | `"            ),"` | — |
| [SRC-C9CF9B54F8-L001160](../../agents/omarai.py#L1160) | 1160 | `"            \"lead_intent_evidence\": safe_evidence,"` | — |
| [SRC-C9CF9B54F8-L001161](../../agents/omarai.py#L1161) | 1161 | `"        }"` | — |
| [SRC-C9CF9B54F8-L001162](../../agents/omarai.py#L1162) | 1162 | `""` | — |
| [SRC-C9CF9B54F8-L001163](../../agents/omarai.py#L1163) | 1163 | `"    def save_discovery_run(self, profile_id: str, run: dict, *, tenant_id: str):"` | — |
| [SRC-C9CF9B54F8-L001164](../../agents/omarai.py#L1164) | 1164 | `"        if not isinstance(run, dict):"` | — |
| [SRC-C9CF9B54F8-L001165](../../agents/omarai.py#L1165) | 1165 | `"            raise TypeError(\"discovery run must be an object\")"` | — |
| [SRC-C9CF9B54F8-L001166](../../agents/omarai.py#L1166) | 1166 | `"        tenant = self._tenant(tenant_id)"` | — |
| [SRC-C9CF9B54F8-L001167](../../agents/omarai.py#L1167) | 1167 | `"        profile = self.get_product_profile(profile_id, tenant_id=tenant)"` | — |
| [SRC-C9CF9B54F8-L001168](../../agents/omarai.py#L1168) | 1168 | `"        if profile is None:"` | — |
| [SRC-C9CF9B54F8-L001169](../../agents/omarai.py#L1169) | 1169 | `"            return None"` | — |
| [SRC-C9CF9B54F8-L001170](../../agents/omarai.py#L1170) | 1170 | `"        raw_sources = run.get(\"sources\")"` | — |
| [SRC-C9CF9B54F8-L001171](../../agents/omarai.py#L1171) | 1171 | `"        raw_sources = raw_sources if isinstance(raw_sources, list) else []"` | — |
| [SRC-C9CF9B54F8-L001172](../../agents/omarai.py#L1172) | 1172 | `"        sources = ["` | — |
| [SRC-C9CF9B54F8-L001173](../../agents/omarai.py#L1173) | 1173 | `"            self._safe_discovery_source(item)"` | — |
| [SRC-C9CF9B54F8-L001174](../../agents/omarai.py#L1174) | 1174 | `"            for item in raw_sources[:30] if isinstance(item, dict)"` | — |
| [SRC-C9CF9B54F8-L001175](../../agents/omarai.py#L1175) | 1175 | `"        ]"` | — |
| [SRC-C9CF9B54F8-L001176](../../agents/omarai.py#L1176) | 1176 | `"        raw_queries = run.get(\"search_queries\")"` | — |
| [SRC-C9CF9B54F8-L001177](../../agents/omarai.py#L1177) | 1177 | `"        if not isinstance(raw_queries, list):"` | — |
| [SRC-C9CF9B54F8-L001178](../../agents/omarai.py#L1178) | 1178 | `"            raw_queries = []"` | — |
| [SRC-C9CF9B54F8-L001179](../../agents/omarai.py#L1179) | 1179 | `"        queries = [str(item)[:500] for item in raw_queries[:8] if isinstance(item, str)]"` | — |
| [SRC-C9CF9B54F8-L001180](../../agents/omarai.py#L1180) | 1180 | `"        raw_report = run.get(\"search_report\")"` | — |
| [SRC-C9CF9B54F8-L001181](../../agents/omarai.py#L1181) | 1181 | `"        raw_report = raw_report if isinstance(raw_report, dict) else {}"` | — |
| [SRC-C9CF9B54F8-L001182](../../agents/omarai.py#L1182) | 1182 | `"        lead_report = raw_report.get(\"lead_generation\")"` | — |
| [SRC-C9CF9B54F8-L001183](../../agents/omarai.py#L1183) | 1183 | `"        report = {"` | — |
| [SRC-C9CF9B54F8-L001184](../../agents/omarai.py#L1184) | 1184 | `"            \"lead_generation\": lead_report if isinstance(lead_report, dict) else {},"` | — |
| [SRC-C9CF9B54F8-L001185](../../agents/omarai.py#L1185) | 1185 | `"            \"pipeline_completion_status\": str("` | — |
| [SRC-C9CF9B54F8-L001186](../../agents/omarai.py#L1186) | 1186 | `"                raw_report.get(\"pipeline_completion_status\")"` | — |
| [SRC-C9CF9B54F8-L001187](../../agents/omarai.py#L1187) | 1187 | `"                or run.get(\"pipeline_completion_status\")"` | — |
| [SRC-C9CF9B54F8-L001188](../../agents/omarai.py#L1188) | 1188 | `"                or \"unknown\""` | — |
| [SRC-C9CF9B54F8-L001189](../../agents/omarai.py#L1189) | 1189 | `"            )[:80],"` | — |
| [SRC-C9CF9B54F8-L001190](../../agents/omarai.py#L1190) | 1190 | `"            \"search_outcome\": str(raw_report.get(\"search_outcome\") or \"unknown\")[:80],"` | — |
| [SRC-C9CF9B54F8-L001191](../../agents/omarai.py#L1191) | 1191 | `"            \"search_attempted\": raw_report.get(\"search_attempted\"),"` | — |
| [SRC-C9CF9B54F8-L001192](../../agents/omarai.py#L1192) | 1192 | `"            \"used_web_search\": run.get(\"used_web_search\") is True,"` | — |
| [SRC-C9CF9B54F8-L001193](../../agents/omarai.py#L1193) | 1193 | `"            \"used_social_search\": run.get(\"used_social_search\") is True,"` | — |
| [SRC-C9CF9B54F8-L001194](../../agents/omarai.py#L1194) | 1194 | `"        }"` | — |
| [SRC-C9CF9B54F8-L001195](../../agents/omarai.py#L1195) | 1195 | `"        report_json = json.dumps(report, ensure_ascii=False, separators=(\",\", \":\"))"` | — |
| [SRC-C9CF9B54F8-L001196](../../agents/omarai.py#L1196) | 1196 | `"        queries_json = json.dumps(queries, ensure_ascii=False, separators=(\",\", \":\"))"` | — |
| [SRC-C9CF9B54F8-L001197](../../agents/omarai.py#L1197) | 1197 | `"        sources_json = json.dumps(sources, ensure_ascii=False, separators=(\",\", \":\"))"` | — |
| [SRC-C9CF9B54F8-L001198](../../agents/omarai.py#L1198) | 1198 | `"        if sum(map(len, (report_json, queries_json, sources_json))) > 120000:"` | — |
| [SRC-C9CF9B54F8-L001199](../../agents/omarai.py#L1199) | 1199 | `"            raise ValueError(\"discovery result exceeds the storage limit\")"` | — |
| [SRC-C9CF9B54F8-L001200](../../agents/omarai.py#L1200) | 1200 | `"        run_id = \"discovery_\" + uuid.uuid4().hex"` | — |
| [SRC-C9CF9B54F8-L001201](../../agents/omarai.py#L1201) | 1201 | `"        now = now_utc()"` | — |
| [SRC-C9CF9B54F8-L001202](../../agents/omarai.py#L1202) | 1202 | `"        answer = str(run.get(\"answer\") or \"\")[:5000]"` | — |
| [SRC-C9CF9B54F8-L001203](../../agents/omarai.py#L1203) | 1203 | `"        kind = str(run.get(\"kind\") or \"lead_discovery\")[:100]"` | — |
| [SRC-C9CF9B54F8-L001204](../../agents/omarai.py#L1204) | 1204 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L001205](../../agents/omarai.py#L1205) | 1205 | `"            db.execute("` | — |
| [SRC-C9CF9B54F8-L001206](../../agents/omarai.py#L1206) | 1206 | `"                \"\"\"INSERT INTO discovery_runs"` | — |
| [SRC-C9CF9B54F8-L001207](../../agents/omarai.py#L1207) | 1207 | `"                   (id, tenant_id, profile_id, answer, kind, search_queries_json,"` | — |
| [SRC-C9CF9B54F8-L001208](../../agents/omarai.py#L1208) | 1208 | `"                    search_report_json, sources_json, created_at)"` | — |
| [SRC-C9CF9B54F8-L001209](../../agents/omarai.py#L1209) | 1209 | `"                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)\"\"\","` | — |
| [SRC-C9CF9B54F8-L001210](../../agents/omarai.py#L1210) | 1210 | `"                ("` | — |
| [SRC-C9CF9B54F8-L001211](../../agents/omarai.py#L1211) | 1211 | `"                    run_id, tenant, profile_id, answer, kind, queries_json,"` | — |
| [SRC-C9CF9B54F8-L001212](../../agents/omarai.py#L1212) | 1212 | `"                    report_json, sources_json, now,"` | — |
| [SRC-C9CF9B54F8-L001213](../../agents/omarai.py#L1213) | 1213 | `"                ),"` | — |
| [SRC-C9CF9B54F8-L001214](../../agents/omarai.py#L1214) | 1214 | `"            )"` | — |
| [SRC-C9CF9B54F8-L001215](../../agents/omarai.py#L1215) | 1215 | `"            row = db.execute("` | — |
| [SRC-C9CF9B54F8-L001216](../../agents/omarai.py#L1216) | 1216 | `"                \"\"\"SELECT r.id, r.tenant_id, r.profile_id, p.name AS profile_name,"` | — |
| [SRC-C9CF9B54F8-L001217](../../agents/omarai.py#L1217) | 1217 | `"                          r.answer, r.kind, r.search_queries_json, r.search_report_json,"` | — |
| [SRC-C9CF9B54F8-L001218](../../agents/omarai.py#L1218) | 1218 | `"                          r.sources_json, r.created_at"` | — |
| [SRC-C9CF9B54F8-L001219](../../agents/omarai.py#L1219) | 1219 | `"                   FROM discovery_runs r"` | — |
| [SRC-C9CF9B54F8-L001220](../../agents/omarai.py#L1220) | 1220 | `"                   JOIN product_profiles p"` | — |
| [SRC-C9CF9B54F8-L001221](../../agents/omarai.py#L1221) | 1221 | `"                     ON p.id=r.profile_id AND p.tenant_id=r.tenant_id"` | — |
| [SRC-C9CF9B54F8-L001222](../../agents/omarai.py#L1222) | 1222 | `"                   WHERE r.id=? AND r.tenant_id=?\"\"\","` | — |
| [SRC-C9CF9B54F8-L001223](../../agents/omarai.py#L1223) | 1223 | `"                (run_id, tenant),"` | — |
| [SRC-C9CF9B54F8-L001224](../../agents/omarai.py#L1224) | 1224 | `"            ).fetchone()"` | — |
| [SRC-C9CF9B54F8-L001225](../../agents/omarai.py#L1225) | 1225 | `"        return self._discovery_run_row(row)"` | — |
| [SRC-C9CF9B54F8-L001226](../../agents/omarai.py#L1226) | 1226 | `""` | — |
| [SRC-C9CF9B54F8-L001227](../../agents/omarai.py#L1227) | 1227 | `"    @staticmethod"` | — |
| [SRC-C9CF9B54F8-L001228](../../agents/omarai.py#L1228) | 1228 | `"    def _discovery_run_row(row):"` | — |
| [SRC-C9CF9B54F8-L001229](../../agents/omarai.py#L1229) | 1229 | `"        if row is None:"` | — |
| [SRC-C9CF9B54F8-L001230](../../agents/omarai.py#L1230) | 1230 | `"            return None"` | — |
| [SRC-C9CF9B54F8-L001231](../../agents/omarai.py#L1231) | 1231 | `"        item = dict(row)"` | — |
| [SRC-C9CF9B54F8-L001232](../../agents/omarai.py#L1232) | 1232 | `"        item[\"search_queries\"] = json.loads(item.pop(\"search_queries_json\"))"` | — |
| [SRC-C9CF9B54F8-L001233](../../agents/omarai.py#L1233) | 1233 | `"        item[\"search_report\"] = json.loads(item.pop(\"search_report_json\"))"` | — |
| [SRC-C9CF9B54F8-L001234](../../agents/omarai.py#L1234) | 1234 | `"        item[\"sources\"] = json.loads(item.pop(\"sources_json\"))"` | — |
| [SRC-C9CF9B54F8-L001235](../../agents/omarai.py#L1235) | 1235 | `"        return item"` | — |
| [SRC-C9CF9B54F8-L001236](../../agents/omarai.py#L1236) | 1236 | `""` | — |
| [SRC-C9CF9B54F8-L001237](../../agents/omarai.py#L1237) | 1237 | `"    def list_discovery_runs(self, *, tenant_id: str, limit: int = 50):"` | — |
| [SRC-C9CF9B54F8-L001238](../../agents/omarai.py#L1238) | 1238 | `"        tenant = self._tenant(tenant_id)"` | — |
| [SRC-C9CF9B54F8-L001239](../../agents/omarai.py#L1239) | 1239 | `"        limit = max(1, min(int(limit), 100))"` | — |
| [SRC-C9CF9B54F8-L001240](../../agents/omarai.py#L1240) | 1240 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L001241](../../agents/omarai.py#L1241) | 1241 | `"            rows = db.execute("` | — |
| [SRC-C9CF9B54F8-L001242](../../agents/omarai.py#L1242) | 1242 | `"                \"\"\"SELECT r.id, r.tenant_id, r.profile_id, p.name AS profile_name,"` | — |
| [SRC-C9CF9B54F8-L001243](../../agents/omarai.py#L1243) | 1243 | `"                          r.answer, r.kind, r.search_queries_json, r.search_report_json,"` | — |
| [SRC-C9CF9B54F8-L001244](../../agents/omarai.py#L1244) | 1244 | `"                          r.sources_json, r.created_at"` | — |
| [SRC-C9CF9B54F8-L001245](../../agents/omarai.py#L1245) | 1245 | `"                   FROM discovery_runs r"` | — |
| [SRC-C9CF9B54F8-L001246](../../agents/omarai.py#L1246) | 1246 | `"                   JOIN product_profiles p"` | — |
| [SRC-C9CF9B54F8-L001247](../../agents/omarai.py#L1247) | 1247 | `"                     ON p.id=r.profile_id AND p.tenant_id=r.tenant_id"` | — |
| [SRC-C9CF9B54F8-L001248](../../agents/omarai.py#L1248) | 1248 | `"                   WHERE r.tenant_id=?"` | — |
| [SRC-C9CF9B54F8-L001249](../../agents/omarai.py#L1249) | 1249 | `"                   ORDER BY r.created_at DESC, r.id LIMIT ?\"\"\","` | — |
| [SRC-C9CF9B54F8-L001250](../../agents/omarai.py#L1250) | 1250 | `"                (tenant, limit),"` | — |
| [SRC-C9CF9B54F8-L001251](../../agents/omarai.py#L1251) | 1251 | `"            ).fetchall()"` | — |
| [SRC-C9CF9B54F8-L001252](../../agents/omarai.py#L1252) | 1252 | `"        results = []"` | — |
| [SRC-C9CF9B54F8-L001253](../../agents/omarai.py#L1253) | 1253 | `"        for row in rows:"` | — |
| [SRC-C9CF9B54F8-L001254](../../agents/omarai.py#L1254) | 1254 | `"            item = self._discovery_run_row(row)"` | — |
| [SRC-C9CF9B54F8-L001255](../../agents/omarai.py#L1255) | 1255 | `"            results.append({"` | — |
| [SRC-C9CF9B54F8-L001256](../../agents/omarai.py#L1256) | 1256 | `"                \"id\": item[\"id\"],"` | — |
| [SRC-C9CF9B54F8-L001257](../../agents/omarai.py#L1257) | 1257 | `"                \"profile_id\": item[\"profile_id\"],"` | — |
| [SRC-C9CF9B54F8-L001258](../../agents/omarai.py#L1258) | 1258 | `"                \"profile_name\": item[\"profile_name\"],"` | — |
| [SRC-C9CF9B54F8-L001259](../../agents/omarai.py#L1259) | 1259 | `"                \"answer\": item[\"answer\"],"` | — |
| [SRC-C9CF9B54F8-L001260](../../agents/omarai.py#L1260) | 1260 | `"                \"kind\": item[\"kind\"],"` | — |
| [SRC-C9CF9B54F8-L001261](../../agents/omarai.py#L1261) | 1261 | `"                \"created_at\": item[\"created_at\"],"` | — |
| [SRC-C9CF9B54F8-L001262](../../agents/omarai.py#L1262) | 1262 | `"                \"source_count\": len(item[\"sources\"]),"` | — |
| [SRC-C9CF9B54F8-L001263](../../agents/omarai.py#L1263) | 1263 | `"                \"qualified_signal_count\": sum("` | — |
| [SRC-C9CF9B54F8-L001264](../../agents/omarai.py#L1264) | 1264 | `"                    source.get(\"lead_qualification\") == \"public_demand_signal\""` | — |
| [SRC-C9CF9B54F8-L001265](../../agents/omarai.py#L1265) | 1265 | `"                    for source in item[\"sources\"]"` | — |
| [SRC-C9CF9B54F8-L001266](../../agents/omarai.py#L1266) | 1266 | `"                ),"` | — |
| [SRC-C9CF9B54F8-L001267](../../agents/omarai.py#L1267) | 1267 | `"                \"pipeline_completion_status\": item[\"search_report\"].get("` | — |
| [SRC-C9CF9B54F8-L001268](../../agents/omarai.py#L1268) | 1268 | `"                    \"pipeline_completion_status\", \"unknown\""` | — |
| [SRC-C9CF9B54F8-L001269](../../agents/omarai.py#L1269) | 1269 | `"                ),"` | — |
| [SRC-C9CF9B54F8-L001270](../../agents/omarai.py#L1270) | 1270 | `"            })"` | — |
| [SRC-C9CF9B54F8-L001271](../../agents/omarai.py#L1271) | 1271 | `"        return results"` | — |
| [SRC-C9CF9B54F8-L001272](../../agents/omarai.py#L1272) | 1272 | `""` | — |
| [SRC-C9CF9B54F8-L001273](../../agents/omarai.py#L1273) | 1273 | `"    def get_discovery_run(self, run_id: str, *, tenant_id: str):"` | — |
| [SRC-C9CF9B54F8-L001274](../../agents/omarai.py#L1274) | 1274 | `"        if not isinstance(run_id, str) or not run_id.strip():"` | — |
| [SRC-C9CF9B54F8-L001275](../../agents/omarai.py#L1275) | 1275 | `"            return None"` | — |
| [SRC-C9CF9B54F8-L001276](../../agents/omarai.py#L1276) | 1276 | `"        tenant = self._tenant(tenant_id)"` | — |
| [SRC-C9CF9B54F8-L001277](../../agents/omarai.py#L1277) | 1277 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L001278](../../agents/omarai.py#L1278) | 1278 | `"            row = db.execute("` | — |
| [SRC-C9CF9B54F8-L001279](../../agents/omarai.py#L1279) | 1279 | `"                \"\"\"SELECT r.id, r.tenant_id, r.profile_id, p.name AS profile_name,"` | — |
| [SRC-C9CF9B54F8-L001280](../../agents/omarai.py#L1280) | 1280 | `"                          r.answer, r.kind, r.search_queries_json, r.search_report_json,"` | — |
| [SRC-C9CF9B54F8-L001281](../../agents/omarai.py#L1281) | 1281 | `"                          r.sources_json, r.created_at"` | — |
| [SRC-C9CF9B54F8-L001282](../../agents/omarai.py#L1282) | 1282 | `"                   FROM discovery_runs r"` | — |
| [SRC-C9CF9B54F8-L001283](../../agents/omarai.py#L1283) | 1283 | `"                   JOIN product_profiles p"` | — |
| [SRC-C9CF9B54F8-L001284](../../agents/omarai.py#L1284) | 1284 | `"                     ON p.id=r.profile_id AND p.tenant_id=r.tenant_id"` | — |
| [SRC-C9CF9B54F8-L001285](../../agents/omarai.py#L1285) | 1285 | `"                   WHERE r.id=? AND r.tenant_id=?\"\"\","` | — |
| [SRC-C9CF9B54F8-L001286](../../agents/omarai.py#L1286) | 1286 | `"                (run_id.strip(), tenant),"` | — |
| [SRC-C9CF9B54F8-L001287](../../agents/omarai.py#L1287) | 1287 | `"            ).fetchone()"` | — |
| [SRC-C9CF9B54F8-L001288](../../agents/omarai.py#L1288) | 1288 | `"        return self._discovery_run_row(row)"` | — |
| [SRC-C9CF9B54F8-L001289](../../agents/omarai.py#L1289) | 1289 | `""` | — |
| [SRC-C9CF9B54F8-L001290](../../agents/omarai.py#L1290) | 1290 | `"    def save_discovery_signal("` | — |
| [SRC-C9CF9B54F8-L001291](../../agents/omarai.py#L1291) | 1291 | `"        self, run_id: str, source_index: int, *, tenant_id: str"` | — |
| [SRC-C9CF9B54F8-L001292](../../agents/omarai.py#L1292) | 1292 | `"    ):"` | — |
| [SRC-C9CF9B54F8-L001293](../../agents/omarai.py#L1293) | 1293 | `"        if not isinstance(source_index, int) or isinstance(source_index, bool):"` | — |
| [SRC-C9CF9B54F8-L001294](../../agents/omarai.py#L1294) | 1294 | `"            return None"` | — |
| [SRC-C9CF9B54F8-L001295](../../agents/omarai.py#L1295) | 1295 | `"        run = self.get_discovery_run(run_id, tenant_id=tenant_id)"` | — |
| [SRC-C9CF9B54F8-L001296](../../agents/omarai.py#L1296) | 1296 | `"        if run is None or not 0 <= source_index < len(run[\"sources\"]):"` | — |
| [SRC-C9CF9B54F8-L001297](../../agents/omarai.py#L1297) | 1297 | `"            return None"` | — |
| [SRC-C9CF9B54F8-L001298](../../agents/omarai.py#L1298) | 1298 | `"        source = run[\"sources\"][source_index]"` | — |
| [SRC-C9CF9B54F8-L001299](../../agents/omarai.py#L1299) | 1299 | `"        if source.get(\"lead_qualification\") != \"public_demand_signal\":"` | — |
| [SRC-C9CF9B54F8-L001300](../../agents/omarai.py#L1300) | 1300 | `"            return None"` | — |
| [SRC-C9CF9B54F8-L001301](../../agents/omarai.py#L1301) | 1301 | `"        evidence = source.get(\"lead_intent_evidence\")"` | — |
| [SRC-C9CF9B54F8-L001302](../../agents/omarai.py#L1302) | 1302 | `"        if not isinstance(evidence, dict) or not str(evidence.get(\"phrase\") or \"\").strip():"` | — |
| [SRC-C9CF9B54F8-L001303](../../agents/omarai.py#L1303) | 1303 | `"            return None"` | — |
| [SRC-C9CF9B54F8-L001304](../../agents/omarai.py#L1304) | 1304 | `"        profile = self.get_product_profile(run[\"profile_id\"], tenant_id=tenant_id)"` | — |
| [SRC-C9CF9B54F8-L001305](../../agents/omarai.py#L1305) | 1305 | `"        if profile is None:"` | — |
| [SRC-C9CF9B54F8-L001306](../../agents/omarai.py#L1306) | 1306 | `"            return None"` | — |
| [SRC-C9CF9B54F8-L001307](../../agents/omarai.py#L1307) | 1307 | `"        product = profile[\"profile\"].get(\"product\", {})"` | — |
| [SRC-C9CF9B54F8-L001308](../../agents/omarai.py#L1308) | 1308 | `"        market = profile[\"profile\"].get(\"market\", {})"` | — |
| [SRC-C9CF9B54F8-L001309](../../agents/omarai.py#L1309) | 1309 | `"        product_terms = ["` | — |
| [SRC-C9CF9B54F8-L001310](../../agents/omarai.py#L1310) | 1310 | `"            str(item) for item in [product.get(\"name\"), *(product.get(\"aliases\") or [])]"` | — |
| [SRC-C9CF9B54F8-L001311](../../agents/omarai.py#L1311) | 1311 | `"            if isinstance(item, str) and item.strip()"` | — |
| [SRC-C9CF9B54F8-L001312](../../agents/omarai.py#L1312) | 1312 | `"        ]"` | — |
| [SRC-C9CF9B54F8-L001313](../../agents/omarai.py#L1313) | 1313 | `"        location_terms = ["` | — |
| [SRC-C9CF9B54F8-L001314](../../agents/omarai.py#L1314) | 1314 | `"            str(item) for item in (market.get(\"locations\") or [])"` | — |
| [SRC-C9CF9B54F8-L001315](../../agents/omarai.py#L1315) | 1315 | `"            if isinstance(item, str) and item.strip()"` | — |
| [SRC-C9CF9B54F8-L001316](../../agents/omarai.py#L1316) | 1316 | `"        ]"` | — |
| [SRC-C9CF9B54F8-L001317](../../agents/omarai.py#L1317) | 1317 | `"        source_text = str(source.get(\"snippet\") or source.get(\"title\") or \"\").strip()"` | — |
| [SRC-C9CF9B54F8-L001318](../../agents/omarai.py#L1318) | 1318 | `"        if not source_text:"` | — |
| [SRC-C9CF9B54F8-L001319](../../agents/omarai.py#L1319) | 1319 | `"            return None"` | — |
| [SRC-C9CF9B54F8-L001320](../../agents/omarai.py#L1320) | 1320 | `"        note = ("` | — |
| [SRC-C9CF9B54F8-L001321](../../agents/omarai.py#L1321) | 1321 | `"            \"Omarai public demand evidence \| \""` | — |
| [SRC-C9CF9B54F8-L001322](../../agents/omarai.py#L1322) | 1322 | `"            + \"phrase=\" + str(evidence.get(\"phrase\") or \"\")[:240]"` | — |
| [SRC-C9CF9B54F8-L001323](../../agents/omarai.py#L1323) | 1323 | `"            + \" \| basis=\" + str(evidence.get(\"basis\") or \"unknown\")[:40]"` | — |
| [SRC-C9CF9B54F8-L001324](../../agents/omarai.py#L1324) | 1324 | `"            + \" \| signal_type=\" + str(evidence.get(\"signal_type\") or \"unknown\")[:80]"` | — |
| [SRC-C9CF9B54F8-L001325](../../agents/omarai.py#L1325) | 1325 | `"            + \" \| profile=\" + str(profile.get(\"name\") or \"\")[:160]"` | — |
| [SRC-C9CF9B54F8-L001326](../../agents/omarai.py#L1326) | 1326 | `"            + \" \| run=\" + run[\"id\"]"` | — |
| [SRC-C9CF9B54F8-L001327](../../agents/omarai.py#L1327) | 1327 | `"        )"` | — |
| [SRC-C9CF9B54F8-L001328](../../agents/omarai.py#L1328) | 1328 | `"        return self.add("` | — |
| [SRC-C9CF9B54F8-L001329](../../agents/omarai.py#L1329) | 1329 | `"            source_text[:MAX_TEXT],"` | — |
| [SRC-C9CF9B54F8-L001330](../../agents/omarai.py#L1330) | 1330 | `"            source[\"url\"],"` | — |
| [SRC-C9CF9B54F8-L001331](../../agents/omarai.py#L1331) | 1331 | `"            str(source.get(\"platform\") or \"web\")[:80],"` | — |
| [SRC-C9CF9B54F8-L001332](../../agents/omarai.py#L1332) | 1332 | `"            observed_at=now_utc(),"` | — |
| [SRC-C9CF9B54F8-L001333](../../agents/omarai.py#L1333) | 1333 | `"            note=note[:1000],"` | — |
| [SRC-C9CF9B54F8-L001334](../../agents/omarai.py#L1334) | 1334 | `"            product_terms=product_terms,"` | — |
| [SRC-C9CF9B54F8-L001335](../../agents/omarai.py#L1335) | 1335 | `"            location_terms=location_terms,"` | — |
| [SRC-C9CF9B54F8-L001336](../../agents/omarai.py#L1336) | 1336 | `"            tenant_id=tenant_id,"` | — |
| [SRC-C9CF9B54F8-L001337](../../agents/omarai.py#L1337) | 1337 | `"        )"` | — |
| [SRC-C9CF9B54F8-L001338](../../agents/omarai.py#L1338) | 1338 | `""` | — |
| [SRC-C9CF9B54F8-L001339](../../agents/omarai.py#L1339) | 1339 | `"    def import_csv(self, filename: str, *, tenant_id: str \| None = None):"` | — |
| [SRC-C9CF9B54F8-L001340](../../agents/omarai.py#L1340) | 1340 | `"        tenant = self._tenant(tenant_id)"` | — |
| [SRC-C9CF9B54F8-L001341](../../agents/omarai.py#L1341) | 1341 | `"        results = {\"created\": 0, \"duplicates\": 0, \"errors\": []}"` | — |
| [SRC-C9CF9B54F8-L001342](../../agents/omarai.py#L1342) | 1342 | `"        with open(filename, newline=\"\", encoding=\"utf-8-sig\") as stream:"` | — |
| [SRC-C9CF9B54F8-L001343](../../agents/omarai.py#L1343) | 1343 | `"            reader = csv.DictReader(stream)"` | — |
| [SRC-C9CF9B54F8-L001344](../../agents/omarai.py#L1344) | 1344 | `"            required = {\"text\", \"source_url\", \"platform\"}"` | — |
| [SRC-C9CF9B54F8-L001345](../../agents/omarai.py#L1345) | 1345 | `"            if not reader.fieldnames or not required.issubset(reader.fieldnames):"` | — |
| [SRC-C9CF9B54F8-L001346](../../agents/omarai.py#L1346) | 1346 | `"                raise ValueError(\"CSV must contain text,source_url,platform columns\")"` | — |
| [SRC-C9CF9B54F8-L001347](../../agents/omarai.py#L1347) | 1347 | `"            for line, row in enumerate(reader, 2):"` | — |
| [SRC-C9CF9B54F8-L001348](../../agents/omarai.py#L1348) | 1348 | `"                try:"` | — |
| [SRC-C9CF9B54F8-L001349](../../agents/omarai.py#L1349) | 1349 | `"                    _, created = self.add("` | — |
| [SRC-C9CF9B54F8-L001350](../../agents/omarai.py#L1350) | 1350 | `"                        row[\"text\"], row[\"source_url\"], row[\"platform\"],"` | — |
| [SRC-C9CF9B54F8-L001351](../../agents/omarai.py#L1351) | 1351 | `"                        row.get(\"observed_at\") or None, row.get(\"note\") or \"\","` | — |
| [SRC-C9CF9B54F8-L001352](../../agents/omarai.py#L1352) | 1352 | `"                        tenant_id=tenant,"` | — |
| [SRC-C9CF9B54F8-L001353](../../agents/omarai.py#L1353) | 1353 | `"                    )"` | — |
| [SRC-C9CF9B54F8-L001354](../../agents/omarai.py#L1354) | 1354 | `"                    results[\"created\" if created else \"duplicates\"] += 1"` | — |
| [SRC-C9CF9B54F8-L001355](../../agents/omarai.py#L1355) | 1355 | `"                except (ValueError, TypeError) as exc:"` | — |
| [SRC-C9CF9B54F8-L001356](../../agents/omarai.py#L1356) | 1356 | `"                    results[\"errors\"].append({\"line\": line, \"error\": str(exc)})"` | — |
| [SRC-C9CF9B54F8-L001357](../../agents/omarai.py#L1357) | 1357 | `"        return results"` | — |
| [SRC-C9CF9B54F8-L001358](../../agents/omarai.py#L1358) | 1358 | `""` | — |
| [SRC-C9CF9B54F8-L001359](../../agents/omarai.py#L1359) | 1359 | `"    def export_csv(self, filename: str, *, tenant_id: str \| None = None):"` | — |
| [SRC-C9CF9B54F8-L001360](../../agents/omarai.py#L1360) | 1360 | `"        rows = self.list(limit=500, tenant_id=tenant_id)"` | — |
| [SRC-C9CF9B54F8-L001361](../../agents/omarai.py#L1361) | 1361 | `"        with open(filename, \"w\", newline=\"\", encoding=\"utf-8-sig\") as stream:"` | — |
| [SRC-C9CF9B54F8-L001362](../../agents/omarai.py#L1362) | 1362 | `"            fields = ["` | — |
| [SRC-C9CF9B54F8-L001363](../../agents/omarai.py#L1363) | 1363 | `"                \"id\", \"tenant_id\", \"text\", \"source_url\", \"platform\", \"observed_at\","` | — |
| [SRC-C9CF9B54F8-L001364](../../agents/omarai.py#L1364) | 1364 | `"                \"assessment\", \"status\", \"note\", \"created_at\","` | — |
| [SRC-C9CF9B54F8-L001365](../../agents/omarai.py#L1365) | 1365 | `"            ]"` | — |
| [SRC-C9CF9B54F8-L001366](../../agents/omarai.py#L1366) | 1366 | `"            writer = csv.DictWriter(stream, fieldnames=fields, quoting=csv.QUOTE_ALL)"` | — |
| [SRC-C9CF9B54F8-L001367](../../agents/omarai.py#L1367) | 1367 | `"            writer.writeheader()"` | — |
| [SRC-C9CF9B54F8-L001368](../../agents/omarai.py#L1368) | 1368 | `"            for row in rows:"` | — |
| [SRC-C9CF9B54F8-L001369](../../agents/omarai.py#L1369) | 1369 | `"                values = {"` | — |
| [SRC-C9CF9B54F8-L001370](../../agents/omarai.py#L1370) | 1370 | `"                    key: json.dumps(row[key], ensure_ascii=False)"` | — |
| [SRC-C9CF9B54F8-L001371](../../agents/omarai.py#L1371) | 1371 | `"                    if key == \"assessment\""` | — |
| [SRC-C9CF9B54F8-L001372](../../agents/omarai.py#L1372) | 1372 | `"                    else row.get(key, \"\")"` | — |
| [SRC-C9CF9B54F8-L001373](../../agents/omarai.py#L1373) | 1373 | `"                    for key in fields"` | — |
| [SRC-C9CF9B54F8-L001374](../../agents/omarai.py#L1374) | 1374 | `"                }"` | — |
| [SRC-C9CF9B54F8-L001375](../../agents/omarai.py#L1375) | 1375 | `"                writer.writerow({key: _csv_safe_cell(value) for key, value in values.items()})"` | — |
| [SRC-C9CF9B54F8-L001376](../../agents/omarai.py#L1376) | 1376 | `"        return len(rows)"` | — |
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
