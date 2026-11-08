# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **022**
- سجلات الأسطر: **800**
- النطاق: SRC-EEF2E6447C-L000525 إلى SRC-DD2C0EB6EA-L000005
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## واجهات API

### FILE-EEF2E6447C — [api/omarai.py](../../api/omarai.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-EEF2E6447C-L000525](../../api/omarai.py#L525) | 525 | `"    def _rate_limit_client_key(self):"` | — |
| [SRC-EEF2E6447C-L000526](../../api/omarai.py#L526) | 526 | `"        \"\"\"Choose a rate-limit identity without trusting spoofable proxy headers by default."` | — |
| [SRC-EEF2E6447C-L000527](../../api/omarai.py#L527) | 527 | `""` | — |
| [SRC-EEF2E6447C-L000528](../../api/omarai.py#L528) | 528 | `"        Set OMARAI_TRUST_PROXY_HEADERS=1 only when the deployment's trusted reverse"` | — |
| [SRC-EEF2E6447C-L000529](../../api/omarai.py#L529) | 529 | `"        proxy appends the actual client IP as the rightmost X-Forwarded-For value."` | — |
| [SRC-EEF2E6447C-L000530](../../api/omarai.py#L530) | 530 | `"        \"\"\""` | — |
| [SRC-EEF2E6447C-L000531](../../api/omarai.py#L531) | 531 | `"        direct_ip = self.client_address[0]"` | — |
| [SRC-EEF2E6447C-L000532](../../api/omarai.py#L532) | 532 | `"        if os.getenv(\"OMARAI_TRUST_PROXY_HEADERS\", \"\").strip() != \"1\":"` | — |
| [SRC-EEF2E6447C-L000533](../../api/omarai.py#L533) | 533 | `"            return direct_ip"` | — |
| [SRC-EEF2E6447C-L000534](../../api/omarai.py#L534) | 534 | `"        forwarded = self.headers.get(\"X-Forwarded-For\", \"\")"` | — |
| [SRC-EEF2E6447C-L000535](../../api/omarai.py#L535) | 535 | `"        candidate = forwarded.rsplit(\",\", 1)[-1].strip() if forwarded else \"\""` | — |
| [SRC-EEF2E6447C-L000536](../../api/omarai.py#L536) | 536 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000537](../../api/omarai.py#L537) | 537 | `"            return str(ipaddress.ip_address(candidate))"` | — |
| [SRC-EEF2E6447C-L000538](../../api/omarai.py#L538) | 538 | `"        except ValueError:"` | — |
| [SRC-EEF2E6447C-L000539](../../api/omarai.py#L539) | 539 | `"            return direct_ip"` | — |
| [SRC-EEF2E6447C-L000540](../../api/omarai.py#L540) | 540 | `""` | — |
| [SRC-EEF2E6447C-L000541](../../api/omarai.py#L541) | 541 | `"    def _rate_limit_ok(self):"` | — |
| [SRC-EEF2E6447C-L000542](../../api/omarai.py#L542) | 542 | `"        client_ip = self._rate_limit_client_key()"` | — |
| [SRC-EEF2E6447C-L000543](../../api/omarai.py#L543) | 543 | `"        now = time.monotonic()"` | — |
| [SRC-EEF2E6447C-L000544](../../api/omarai.py#L544) | 544 | `"        cls = type(self)"` | — |
| [SRC-EEF2E6447C-L000545](../../api/omarai.py#L545) | 545 | `"        with self._rate_lock:"` | — |
| [SRC-EEF2E6447C-L000546](../../api/omarai.py#L546) | 546 | `"            # Periodically remove IP buckets whose entire sliding window has expired."` | — |
| [SRC-EEF2E6447C-L000547](../../api/omarai.py#L547) | 547 | `"            # Without this sweep, a public endpoint could retain one empty deque per"` | — |
| [SRC-EEF2E6447C-L000548](../../api/omarai.py#L548) | 548 | `"            # distinct client IP forever, even though the rate-limit window is 60 sec."` | — |
| [SRC-EEF2E6447C-L000549](../../api/omarai.py#L549) | 549 | `"            if now - cls._rate_last_cleanup >= cls.RATE_LIMIT_CLEANUP_INTERVAL_SECONDS:"` | — |
| [SRC-EEF2E6447C-L000550](../../api/omarai.py#L550) | 550 | `"                cutoff = now - cls.RATE_LIMIT_WINDOW_SECONDS"` | — |
| [SRC-EEF2E6447C-L000551](../../api/omarai.py#L551) | 551 | `"                for key, timestamps in list(cls._request_times.items()):"` | — |
| [SRC-EEF2E6447C-L000552](../../api/omarai.py#L552) | 552 | `"                    while timestamps and timestamps[0] <= cutoff:"` | — |
| [SRC-EEF2E6447C-L000553](../../api/omarai.py#L553) | 553 | `"                        timestamps.popleft()"` | — |
| [SRC-EEF2E6447C-L000554](../../api/omarai.py#L554) | 554 | `"                    if not timestamps:"` | — |
| [SRC-EEF2E6447C-L000555](../../api/omarai.py#L555) | 555 | `"                        cls._request_times.pop(key, None)"` | — |
| [SRC-EEF2E6447C-L000556](../../api/omarai.py#L556) | 556 | `"                cls._rate_last_cleanup = now"` | — |
| [SRC-EEF2E6447C-L000557](../../api/omarai.py#L557) | 557 | `""` | — |
| [SRC-EEF2E6447C-L000558](../../api/omarai.py#L558) | 558 | `"            if ("` | — |
| [SRC-EEF2E6447C-L000559](../../api/omarai.py#L559) | 559 | `"                client_ip not in cls._request_times"` | — |
| [SRC-EEF2E6447C-L000560](../../api/omarai.py#L560) | 560 | `"                and len(cls._request_times) >= max(1, cls.MAX_RATE_LIMIT_CLIENT_BUCKETS) - 1"` | — |
| [SRC-EEF2E6447C-L000561](../../api/omarai.py#L561) | 561 | `"            ):"` | — |
| [SRC-EEF2E6447C-L000562](../../api/omarai.py#L562) | 562 | `"                # Bound attacker-controlled cardinality. Excess identities share a"` | — |
| [SRC-EEF2E6447C-L000563](../../api/omarai.py#L563) | 563 | `"                # conservative overflow bucket instead of allocating one deque per IP."` | — |
| [SRC-EEF2E6447C-L000564](../../api/omarai.py#L564) | 564 | `"                client_ip = cls.RATE_LIMIT_OVERFLOW_KEY"` | — |
| [SRC-EEF2E6447C-L000565](../../api/omarai.py#L565) | 565 | `"            events = cls._request_times[client_ip]"` | — |
| [SRC-EEF2E6447C-L000566](../../api/omarai.py#L566) | 566 | `"            while events and now - events[0] >= cls.RATE_LIMIT_WINDOW_SECONDS:"` | — |
| [SRC-EEF2E6447C-L000567](../../api/omarai.py#L567) | 567 | `"                events.popleft()"` | — |
| [SRC-EEF2E6447C-L000568](../../api/omarai.py#L568) | 568 | `"            if len(events) >= cls.RATE_LIMIT_REQUESTS:"` | — |
| [SRC-EEF2E6447C-L000569](../../api/omarai.py#L569) | 569 | `"                return False"` | — |
| [SRC-EEF2E6447C-L000570](../../api/omarai.py#L570) | 570 | `"            events.append(now)"` | — |
| [SRC-EEF2E6447C-L000571](../../api/omarai.py#L571) | 571 | `"            return True"` | — |
| [SRC-EEF2E6447C-L000572](../../api/omarai.py#L572) | 572 | `""` | — |
| [SRC-EEF2E6447C-L000573](../../api/omarai.py#L573) | 573 | `"    def _read_request_body(self) -> bytes \| None:"` | — |
| [SRC-EEF2E6447C-L000574](../../api/omarai.py#L574) | 574 | `"        \"\"\"Read a bounded body with both idle and absolute wall-clock deadlines.\"\"\""` | — |
| [SRC-EEF2E6447C-L000575](../../api/omarai.py#L575) | 575 | `"        raw_size = self.headers.get(\"Content-Length\", \"\").strip()"` | — |
| [SRC-EEF2E6447C-L000576](../../api/omarai.py#L576) | 576 | `"        if not raw_size or not raw_size.isascii() or not raw_size.isdecimal():"` | — |
| [SRC-EEF2E6447C-L000577](../../api/omarai.py#L577) | 577 | `"            self.respond(400, {\"error\": \"valid Content-Length is required\"})"` | — |
| [SRC-EEF2E6447C-L000578](../../api/omarai.py#L578) | 578 | `"            return None"` | — |
| [SRC-EEF2E6447C-L000579](../../api/omarai.py#L579) | 579 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000580](../../api/omarai.py#L580) | 580 | `"            size = int(raw_size)"` | — |
| [SRC-EEF2E6447C-L000581](../../api/omarai.py#L581) | 581 | `"        except ValueError:"` | — |
| [SRC-EEF2E6447C-L000582](../../api/omarai.py#L582) | 582 | `"            self.respond(400, {\"error\": \"valid Content-Length is required\"})"` | — |
| [SRC-EEF2E6447C-L000583](../../api/omarai.py#L583) | 583 | `"            return None"` | — |
| [SRC-EEF2E6447C-L000584](../../api/omarai.py#L584) | 584 | `"        if size <= 0:"` | — |
| [SRC-EEF2E6447C-L000585](../../api/omarai.py#L585) | 585 | `"            self.respond(400, {\"error\": \"request body is required\"})"` | — |
| [SRC-EEF2E6447C-L000586](../../api/omarai.py#L586) | 586 | `"            return None"` | — |
| [SRC-EEF2E6447C-L000587](../../api/omarai.py#L587) | 587 | `"        if size > MAX_REQUEST_BODY_BYTES:"` | — |
| [SRC-EEF2E6447C-L000588](../../api/omarai.py#L588) | 588 | `"            # The declared body remains unread; do not reuse this connection."` | — |
| [SRC-EEF2E6447C-L000589](../../api/omarai.py#L589) | 589 | `"            self.close_connection = True"` | — |
| [SRC-EEF2E6447C-L000590](../../api/omarai.py#L590) | 590 | `"            self.respond(413, {\"error\": \"request too large\"})"` | — |
| [SRC-EEF2E6447C-L000591](../../api/omarai.py#L591) | 591 | `"            return None"` | — |
| [SRC-EEF2E6447C-L000592](../../api/omarai.py#L592) | 592 | `""` | — |
| [SRC-EEF2E6447C-L000593](../../api/omarai.py#L593) | 593 | `"        total_timeout = max("` | — |
| [SRC-EEF2E6447C-L000594](../../api/omarai.py#L594) | 594 | `"            0.1,"` | — |
| [SRC-EEF2E6447C-L000595](../../api/omarai.py#L595) | 595 | `"            min("` | — |
| [SRC-EEF2E6447C-L000596](../../api/omarai.py#L596) | 596 | `"                float(REQUEST_BODY_READ_TIMEOUT_SECONDS),"` | — |
| [SRC-EEF2E6447C-L000597](../../api/omarai.py#L597) | 597 | `"                MAX_REQUEST_BODY_READ_TIMEOUT_SECONDS,"` | — |
| [SRC-EEF2E6447C-L000598](../../api/omarai.py#L598) | 598 | `"            ),"` | — |
| [SRC-EEF2E6447C-L000599](../../api/omarai.py#L599) | 599 | `"        )"` | — |
| [SRC-EEF2E6447C-L000600](../../api/omarai.py#L600) | 600 | `"        idle_timeout = max("` | — |
| [SRC-EEF2E6447C-L000601](../../api/omarai.py#L601) | 601 | `"            0.1,"` | — |
| [SRC-EEF2E6447C-L000602](../../api/omarai.py#L602) | 602 | `"            min("` | — |
| [SRC-EEF2E6447C-L000603](../../api/omarai.py#L603) | 603 | `"                float(REQUEST_BODY_IDLE_TIMEOUT_SECONDS),"` | — |
| [SRC-EEF2E6447C-L000604](../../api/omarai.py#L604) | 604 | `"                MAX_REQUEST_BODY_READ_TIMEOUT_SECONDS,"` | — |
| [SRC-EEF2E6447C-L000605](../../api/omarai.py#L605) | 605 | `"            ),"` | — |
| [SRC-EEF2E6447C-L000606](../../api/omarai.py#L606) | 606 | `"        )"` | — |
| [SRC-EEF2E6447C-L000607](../../api/omarai.py#L607) | 607 | `"        deadline = time.monotonic() + total_timeout"` | — |
| [SRC-EEF2E6447C-L000608](../../api/omarai.py#L608) | 608 | `"        previous_timeout = self.connection.gettimeout()"` | — |
| [SRC-EEF2E6447C-L000609](../../api/omarai.py#L609) | 609 | `"        body = bytearray()"` | — |
| [SRC-EEF2E6447C-L000610](../../api/omarai.py#L610) | 610 | `"        timed_out = False"` | — |
| [SRC-EEF2E6447C-L000611](../../api/omarai.py#L611) | 611 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000612](../../api/omarai.py#L612) | 612 | `"            while len(body) < size:"` | — |
| [SRC-EEF2E6447C-L000613](../../api/omarai.py#L613) | 613 | `"                remaining = deadline - time.monotonic()"` | — |
| [SRC-EEF2E6447C-L000614](../../api/omarai.py#L614) | 614 | `"                if remaining <= 0:"` | — |
| [SRC-EEF2E6447C-L000615](../../api/omarai.py#L615) | 615 | `"                    timed_out = True"` | — |
| [SRC-EEF2E6447C-L000616](../../api/omarai.py#L616) | 616 | `"                    break"` | — |
| [SRC-EEF2E6447C-L000617](../../api/omarai.py#L617) | 617 | `"                self.connection.settimeout(min(idle_timeout, remaining))"` | — |
| [SRC-EEF2E6447C-L000618](../../api/omarai.py#L618) | 618 | `"                try:"` | — |
| [SRC-EEF2E6447C-L000619](../../api/omarai.py#L619) | 619 | `"                    # read1 performs at most one underlying read, letting us re-check"` | — |
| [SRC-EEF2E6447C-L000620](../../api/omarai.py#L620) | 620 | `"                    # the absolute deadline between body fragments."` | — |
| [SRC-EEF2E6447C-L000621](../../api/omarai.py#L621) | 621 | `"                    chunk = self.rfile.read1("` | — |
| [SRC-EEF2E6447C-L000622](../../api/omarai.py#L622) | 622 | `"                        min(size - len(body), REQUEST_BODY_READ_CHUNK_BYTES)"` | — |
| [SRC-EEF2E6447C-L000623](../../api/omarai.py#L623) | 623 | `"                    )"` | — |
| [SRC-EEF2E6447C-L000624](../../api/omarai.py#L624) | 624 | `"                except TimeoutError:"` | — |
| [SRC-EEF2E6447C-L000625](../../api/omarai.py#L625) | 625 | `"                    timed_out = True"` | — |
| [SRC-EEF2E6447C-L000626](../../api/omarai.py#L626) | 626 | `"                    break"` | — |
| [SRC-EEF2E6447C-L000627](../../api/omarai.py#L627) | 627 | `"                if not chunk:"` | — |
| [SRC-EEF2E6447C-L000628](../../api/omarai.py#L628) | 628 | `"                    break"` | — |
| [SRC-EEF2E6447C-L000629](../../api/omarai.py#L629) | 629 | `"                body.extend(chunk)"` | — |
| [SRC-EEF2E6447C-L000630](../../api/omarai.py#L630) | 630 | `"        finally:"` | — |
| [SRC-EEF2E6447C-L000631](../../api/omarai.py#L631) | 631 | `"            try:"` | — |
| [SRC-EEF2E6447C-L000632](../../api/omarai.py#L632) | 632 | `"                self.connection.settimeout(previous_timeout)"` | — |
| [SRC-EEF2E6447C-L000633](../../api/omarai.py#L633) | 633 | `"            except OSError:"` | — |
| [SRC-EEF2E6447C-L000634](../../api/omarai.py#L634) | 634 | `"                pass"` | — |
| [SRC-EEF2E6447C-L000635](../../api/omarai.py#L635) | 635 | `""` | — |
| [SRC-EEF2E6447C-L000636](../../api/omarai.py#L636) | 636 | `"        if timed_out:"` | — |
| [SRC-EEF2E6447C-L000637](../../api/omarai.py#L637) | 637 | `"            self.close_connection = True"` | — |
| [SRC-EEF2E6447C-L000638](../../api/omarai.py#L638) | 638 | `"            self.respond(408, {\"error\": \"request body read timed out\"})"` | — |
| [SRC-EEF2E6447C-L000639](../../api/omarai.py#L639) | 639 | `"            return None"` | — |
| [SRC-EEF2E6447C-L000640](../../api/omarai.py#L640) | 640 | `"        if len(body) != size:"` | — |
| [SRC-EEF2E6447C-L000641](../../api/omarai.py#L641) | 641 | `"            self.close_connection = True"` | — |
| [SRC-EEF2E6447C-L000642](../../api/omarai.py#L642) | 642 | `"            self.respond(400, {\"error\": \"incomplete request body\"})"` | — |
| [SRC-EEF2E6447C-L000643](../../api/omarai.py#L643) | 643 | `"            return None"` | — |
| [SRC-EEF2E6447C-L000644](../../api/omarai.py#L644) | 644 | `"        return bytes(body)"` | — |
| [SRC-EEF2E6447C-L000645](../../api/omarai.py#L645) | 645 | `""` | — |
| [SRC-EEF2E6447C-L000646](../../api/omarai.py#L646) | 646 | `"    def end_headers(self):"` | — |
| [SRC-EEF2E6447C-L000647](../../api/omarai.py#L647) | 647 | `"        \"\"\"Apply defensive browser headers to successful and error responses alike.\"\"\""` | — |
| [SRC-EEF2E6447C-L000648](../../api/omarai.py#L648) | 648 | `"        self.send_header(\"X-Content-Type-Options\", \"nosniff\")"` | — |
| [SRC-EEF2E6447C-L000649](../../api/omarai.py#L649) | 649 | `"        self.send_header(\"X-Frame-Options\", \"DENY\")"` | — |
| [SRC-EEF2E6447C-L000650](../../api/omarai.py#L650) | 650 | `"        self.send_header(\"Referrer-Policy\", \"strict-origin-when-cross-origin\")"` | — |
| [SRC-EEF2E6447C-L000651](../../api/omarai.py#L651) | 651 | `"        self.send_header(\"Permissions-Policy\", \"camera=(), microphone=(), geolocation=()\")"` | — |
| [SRC-EEF2E6447C-L000652](../../api/omarai.py#L652) | 652 | `"        self.send_header(\"Content-Security-Policy\", _content_security_policy())"` | — |
| [SRC-EEF2E6447C-L000653](../../api/omarai.py#L653) | 653 | `"        super().end_headers()"` | — |
| [SRC-EEF2E6447C-L000654](../../api/omarai.py#L654) | 654 | `""` | — |
| [SRC-EEF2E6447C-L000655](../../api/omarai.py#L655) | 655 | `"    def respond("` | — |
| [SRC-EEF2E6447C-L000656](../../api/omarai.py#L656) | 656 | `"        self,"` | — |
| [SRC-EEF2E6447C-L000657](../../api/omarai.py#L657) | 657 | `"        status,"` | — |
| [SRC-EEF2E6447C-L000658](../../api/omarai.py#L658) | 658 | `"        payload,"` | — |
| [SRC-EEF2E6447C-L000659](../../api/omarai.py#L659) | 659 | `"        content_type=\"application/json; charset=utf-8\","` | — |
| [SRC-EEF2E6447C-L000660](../../api/omarai.py#L660) | 660 | `"        extra_headers: list[tuple[str, str]] \| None = None,"` | — |
| [SRC-EEF2E6447C-L000661](../../api/omarai.py#L661) | 661 | `"    ):"` | — |
| [SRC-EEF2E6447C-L000662](../../api/omarai.py#L662) | 662 | `"        body = payload.encode() if isinstance(payload, str) else json.dumps(payload, ensure_ascii=False).encode()"` | — |
| [SRC-EEF2E6447C-L000663](../../api/omarai.py#L663) | 663 | `"        self.send_response(status)"` | — |
| [SRC-EEF2E6447C-L000664](../../api/omarai.py#L664) | 664 | `"        self.send_header(\"Content-Type\", content_type)"` | — |
| [SRC-EEF2E6447C-L000665](../../api/omarai.py#L665) | 665 | `"        self.send_header(\"Content-Length\", str(len(body)))"` | — |
| [SRC-EEF2E6447C-L000666](../../api/omarai.py#L666) | 666 | `"        self.send_header(\"Cache-Control\", \"no-store\")"` | — |
| [SRC-EEF2E6447C-L000667](../../api/omarai.py#L667) | 667 | `"        origin = self.headers.get(\"Origin\")"` | — |
| [SRC-EEF2E6447C-L000668](../../api/omarai.py#L668) | 668 | `"        if origin and self._origin_allowed(origin):"` | — |
| [SRC-EEF2E6447C-L000669](../../api/omarai.py#L669) | 669 | `"            self.send_header(\"Access-Control-Allow-Origin\", origin)"` | — |
| [SRC-EEF2E6447C-L000670](../../api/omarai.py#L670) | 670 | `"            self.send_header(\"Vary\", \"Origin\")"` | — |
| [SRC-EEF2E6447C-L000671](../../api/omarai.py#L671) | 671 | `"        for name, value in extra_headers or []:"` | — |
| [SRC-EEF2E6447C-L000672](../../api/omarai.py#L672) | 672 | `"            self.send_header(name, value)"` | — |
| [SRC-EEF2E6447C-L000673](../../api/omarai.py#L673) | 673 | `"        self.end_headers()"` | — |
| [SRC-EEF2E6447C-L000674](../../api/omarai.py#L674) | 674 | `"        self.wfile.write(body)"` | — |
| [SRC-EEF2E6447C-L000675](../../api/omarai.py#L675) | 675 | `""` | — |
| [SRC-EEF2E6447C-L000676](../../api/omarai.py#L676) | 676 | `"    def do_GET(self):"` | — |
| [SRC-EEF2E6447C-L000677](../../api/omarai.py#L677) | 677 | `"        parsed = urlparse(self.path)"` | — |
| [SRC-EEF2E6447C-L000678](../../api/omarai.py#L678) | 678 | `"        if parsed.path == \"/agent\":"` | — |
| [SRC-EEF2E6447C-L000679](../../api/omarai.py#L679) | 679 | `"            if not AGENT_DASHBOARD.exists():"` | — |
| [SRC-EEF2E6447C-L000680](../../api/omarai.py#L680) | 680 | `"                return self.respond(404, {\"error\": \"agent dashboard missing\"})"` | — |
| [SRC-EEF2E6447C-L000681](../../api/omarai.py#L681) | 681 | `"            return self.respond(200, AGENT_DASHBOARD.read_text(encoding=\"utf-8\"), \"text/html; charset=utf-8\")"` | — |
| [SRC-EEF2E6447C-L000682](../../api/omarai.py#L682) | 682 | `"        if parsed.path in {\"/\", \"/workspace\"}:"` | — |
| [SRC-EEF2E6447C-L000683](../../api/omarai.py#L683) | 683 | `"            if not WORKSPACE_DASHBOARD.exists():"` | — |
| [SRC-EEF2E6447C-L000684](../../api/omarai.py#L684) | 684 | `"                return self.respond(404, {\"error\": \"workspace dashboard missing\"})"` | — |
| [SRC-EEF2E6447C-L000685](../../api/omarai.py#L685) | 685 | `"            return self.respond(200, WORKSPACE_DASHBOARD.read_text(encoding=\"utf-8\"), \"text/html; charset=utf-8\")"` | — |
| [SRC-EEF2E6447C-L000686](../../api/omarai.py#L686) | 686 | `"        if parsed.path == \"/leads\":"` | — |
| [SRC-EEF2E6447C-L000687](../../api/omarai.py#L687) | 687 | `"            if not LEADS_DASHBOARD.exists():"` | — |
| [SRC-EEF2E6447C-L000688](../../api/omarai.py#L688) | 688 | `"                return self.respond(404, {\"error\": \"leads dashboard missing\"})"` | — |
| [SRC-EEF2E6447C-L000689](../../api/omarai.py#L689) | 689 | `"            return self.respond(200, LEADS_DASHBOARD.read_text(encoding=\"utf-8\"), \"text/html; charset=utf-8\")"` | — |
| [SRC-EEF2E6447C-L000690](../../api/omarai.py#L690) | 690 | `"        if parsed.path == \"/api/health\":"` | — |
| [SRC-EEF2E6447C-L000691](../../api/omarai.py#L691) | 691 | `"            return self.respond("` | — |
| [SRC-EEF2E6447C-L000692](../../api/omarai.py#L692) | 692 | `"                200,"` | — |
| [SRC-EEF2E6447C-L000693](../../api/omarai.py#L693) | 693 | `"                {"` | — |
| [SRC-EEF2E6447C-L000694](../../api/omarai.py#L694) | 694 | `"                    \"ok\": True,"` | — |
| [SRC-EEF2E6447C-L000695](../../api/omarai.py#L695) | 695 | `"                    \"app\": \"Omarai\","` | — |
| [SRC-EEF2E6447C-L000696](../../api/omarai.py#L696) | 696 | `"                    \"mode\": \"web-research\","` | — |
| [SRC-EEF2E6447C-L000697](../../api/omarai.py#L697) | 697 | `"                    \"agent\": WebAgent.status(),"` | — |
| [SRC-EEF2E6447C-L000698](../../api/omarai.py#L698) | 698 | `"                    \"storage\": {"` | — |
| [SRC-EEF2E6447C-L000699](../../api/omarai.py#L699) | 699 | `"                        \"backend\": getattr(self.store, \"backend\", \"unknown\"),"` | — |
| [SRC-EEF2E6447C-L000700](../../api/omarai.py#L700) | 700 | `"                        \"database_url_configured\": bool("` | — |
| [SRC-EEF2E6447C-L000701](../../api/omarai.py#L701) | 701 | `"                            os.getenv(\"OMARAI_DATABASE_URL\", \"\").strip()"` | — |
| [SRC-EEF2E6447C-L000702](../../api/omarai.py#L702) | 702 | `"                            or os.getenv(\"DATABASE_URL\", \"\").strip()"` | — |
| [SRC-EEF2E6447C-L000703](../../api/omarai.py#L703) | 703 | `"                        ),"` | — |
| [SRC-EEF2E6447C-L000704](../../api/omarai.py#L704) | 704 | `"                        \"database_path_override_configured\": bool("` | — |
| [SRC-EEF2E6447C-L000705](../../api/omarai.py#L705) | 705 | `"                            os.getenv(\"OMARAI_DB_PATH\", \"\").strip()"` | — |
| [SRC-EEF2E6447C-L000706](../../api/omarai.py#L706) | 706 | `"                        ),"` | — |
| [SRC-EEF2E6447C-L000707](../../api/omarai.py#L707) | 707 | `"                        # This is an operator assertion, not automatic mount detection."` | — |
| [SRC-EEF2E6447C-L000708](../../api/omarai.py#L708) | 708 | `"                        \"persistent_volume_operator_asserted\": ("` | — |
| [SRC-EEF2E6447C-L000709](../../api/omarai.py#L709) | 709 | `"                            os.getenv(\"OMARAI_DB_PERSISTENT\", \"\").strip() == \"1\""` | — |
| [SRC-EEF2E6447C-L000710](../../api/omarai.py#L710) | 710 | `"                        ),"` | — |
| [SRC-EEF2E6447C-L000711](../../api/omarai.py#L711) | 711 | `"                        \"durability_status\": ("` | — |
| [SRC-EEF2E6447C-L000712](../../api/omarai.py#L712) | 712 | `"                            \"external_database_configured\""` | — |
| [SRC-EEF2E6447C-L000713](../../api/omarai.py#L713) | 713 | `"                            if getattr(self.store, \"backend\", \"unknown\") == \"postgresql\""` | — |
| [SRC-EEF2E6447C-L000714](../../api/omarai.py#L714) | 714 | `"                            else \"operator_asserted\""` | — |
| [SRC-EEF2E6447C-L000715](../../api/omarai.py#L715) | 715 | `"                            if os.getenv(\"OMARAI_DB_PERSISTENT\", \"\").strip() == \"1\""` | — |
| [SRC-EEF2E6447C-L000716](../../api/omarai.py#L716) | 716 | `"                            else \"not_guaranteed\""` | — |
| [SRC-EEF2E6447C-L000717](../../api/omarai.py#L717) | 717 | `"                        ),"` | — |
| [SRC-EEF2E6447C-L000718](../../api/omarai.py#L718) | 718 | `"                        \"warning\": ("` | — |
| [SRC-EEF2E6447C-L000719](../../api/omarai.py#L719) | 719 | `"                            \"PostgreSQL is selected; provider durability and backups are outside this health check.\""` | — |
| [SRC-EEF2E6447C-L000720](../../api/omarai.py#L720) | 720 | `"                            if getattr(self.store, \"backend\", \"unknown\") == \"postgresql\""` | — |
| [SRC-EEF2E6447C-L000721](../../api/omarai.py#L721) | 721 | `"                            else None"` | — |
| [SRC-EEF2E6447C-L000722](../../api/omarai.py#L722) | 722 | `"                            if os.getenv(\"OMARAI_DB_PERSISTENT\", \"\").strip() == \"1\""` | — |
| [SRC-EEF2E6447C-L000723](../../api/omarai.py#L723) | 723 | `"                            else \"SQLite records may be lost when the host replaces its ephemeral filesystem.\""` | — |
| [SRC-EEF2E6447C-L000724](../../api/omarai.py#L724) | 724 | `"                        ),"` | — |
| [SRC-EEF2E6447C-L000725](../../api/omarai.py#L725) | 725 | `"                    },"` | — |
| [SRC-EEF2E6447C-L000726](../../api/omarai.py#L726) | 726 | `"                    \"build\": {"` | — |
| [SRC-EEF2E6447C-L000727](../../api/omarai.py#L727) | 727 | `"                        \"sha\": _build_identity()[0],"` | — |
| [SRC-EEF2E6447C-L000728](../../api/omarai.py#L728) | 728 | `"                        \"sha_status\": ("` | — |
| [SRC-EEF2E6447C-L000729](../../api/omarai.py#L729) | 729 | `"                            \"available\" if _build_identity()[0] != \"unknown\" else \"unknown\""` | — |
| [SRC-EEF2E6447C-L000730](../../api/omarai.py#L730) | 730 | `"                        ),"` | — |
| [SRC-EEF2E6447C-L000731](../../api/omarai.py#L731) | 731 | `"                        \"sha_source\": _build_identity()[1],"` | — |
| [SRC-EEF2E6447C-L000732](../../api/omarai.py#L732) | 732 | `"                    },"` | — |
| [SRC-EEF2E6447C-L000733](../../api/omarai.py#L733) | 733 | `"                },"` | — |
| [SRC-EEF2E6447C-L000734](../../api/omarai.py#L734) | 734 | `"            )"` | — |
| [SRC-EEF2E6447C-L000735](../../api/omarai.py#L735) | 735 | `"        if parsed.path == \"/api/product-profiles\":"` | — |
| [SRC-EEF2E6447C-L000736](../../api/omarai.py#L736) | 736 | `"            if not self._rate_limit_ok():"` | — |
| [SRC-EEF2E6447C-L000737](../../api/omarai.py#L737) | 737 | `"                return self.respond(429, {\"error\": \"تجاوزت حد الطلبات المؤقت؛ حاول بعد دقيقة.\"})"` | — |
| [SRC-EEF2E6447C-L000738](../../api/omarai.py#L738) | 738 | `"            if not self._authorized():"` | — |
| [SRC-EEF2E6447C-L000739](../../api/omarai.py#L739) | 739 | `"                return self.respond(401, {\"error\": \"يلزم تسجيل الدخول لقراءة ملفات المنتجات.\"})"` | — |
| [SRC-EEF2E6447C-L000740](../../api/omarai.py#L740) | 740 | `"            profiles = self.store.list_product_profiles("` | — |
| [SRC-EEF2E6447C-L000741](../../api/omarai.py#L741) | 741 | `"                tenant_id=self._authenticated_principal[\"tenant_id\"]"` | — |
| [SRC-EEF2E6447C-L000742](../../api/omarai.py#L742) | 742 | `"            )"` | — |
| [SRC-EEF2E6447C-L000743](../../api/omarai.py#L743) | 743 | `"            return self.respond(200, {\"profiles\": profiles, \"count\": len(profiles)})"` | — |
| [SRC-EEF2E6447C-L000744](../../api/omarai.py#L744) | 744 | `"        if parsed.path == \"/api/discoveries\":"` | — |
| [SRC-EEF2E6447C-L000745](../../api/omarai.py#L745) | 745 | `"            if not self._rate_limit_ok():"` | — |
| [SRC-EEF2E6447C-L000746](../../api/omarai.py#L746) | 746 | `"                return self.respond(429, {\"error\": \"تجاوزت حد الطلبات المؤقت؛ حاول بعد دقيقة.\"})"` | — |
| [SRC-EEF2E6447C-L000747](../../api/omarai.py#L747) | 747 | `"            if not self._authorized():"` | — |
| [SRC-EEF2E6447C-L000748](../../api/omarai.py#L748) | 748 | `"                return self.respond(401, {\"error\": \"يلزم تسجيل الدخول لقراءة سجل الاكتشاف.\"})"` | — |
| [SRC-EEF2E6447C-L000749](../../api/omarai.py#L749) | 749 | `"            runs = self.store.list_discovery_runs("` | — |
| [SRC-EEF2E6447C-L000750](../../api/omarai.py#L750) | 750 | `"                tenant_id=self._authenticated_principal[\"tenant_id\"]"` | — |
| [SRC-EEF2E6447C-L000751](../../api/omarai.py#L751) | 751 | `"            )"` | — |
| [SRC-EEF2E6447C-L000752](../../api/omarai.py#L752) | 752 | `"            return self.respond(200, {\"runs\": runs, \"count\": len(runs)})"` | — |
| [SRC-EEF2E6447C-L000753](../../api/omarai.py#L753) | 753 | `"        discovery_route = parsed.path.split(\"/\")"` | — |
| [SRC-EEF2E6447C-L000754](../../api/omarai.py#L754) | 754 | `"        if ("` | — |
| [SRC-EEF2E6447C-L000755](../../api/omarai.py#L755) | 755 | `"            len(discovery_route) == 4"` | — |
| [SRC-EEF2E6447C-L000756](../../api/omarai.py#L756) | 756 | `"            and discovery_route[1:3] == [\"api\", \"discoveries\"]"` | — |
| [SRC-EEF2E6447C-L000757](../../api/omarai.py#L757) | 757 | `"            and discovery_route[3]"` | — |
| [SRC-EEF2E6447C-L000758](../../api/omarai.py#L758) | 758 | `"        ):"` | — |
| [SRC-EEF2E6447C-L000759](../../api/omarai.py#L759) | 759 | `"            if not self._rate_limit_ok():"` | — |
| [SRC-EEF2E6447C-L000760](../../api/omarai.py#L760) | 760 | `"                return self.respond(429, {\"error\": \"تجاوزت حد الطلبات المؤقت؛ حاول بعد دقيقة.\"})"` | — |
| [SRC-EEF2E6447C-L000761](../../api/omarai.py#L761) | 761 | `"            if not self._authorized():"` | — |
| [SRC-EEF2E6447C-L000762](../../api/omarai.py#L762) | 762 | `"                return self.respond(401, {\"error\": \"يلزم تسجيل الدخول لقراءة عملية الاكتشاف.\"})"` | — |
| [SRC-EEF2E6447C-L000763](../../api/omarai.py#L763) | 763 | `"            run = self.store.get_discovery_run("` | — |
| [SRC-EEF2E6447C-L000764](../../api/omarai.py#L764) | 764 | `"                discovery_route[3],"` | — |
| [SRC-EEF2E6447C-L000765](../../api/omarai.py#L765) | 765 | `"                tenant_id=self._authenticated_principal[\"tenant_id\"],"` | — |
| [SRC-EEF2E6447C-L000766](../../api/omarai.py#L766) | 766 | `"            )"` | — |
| [SRC-EEF2E6447C-L000767](../../api/omarai.py#L767) | 767 | `"            return self.respond(200, run) if run else self.respond(404, {\"error\": \"discovery run not found\"})"` | — |
| [SRC-EEF2E6447C-L000768](../../api/omarai.py#L768) | 768 | `"        if parsed.path == \"/api/session\":"` | — |
| [SRC-EEF2E6447C-L000769](../../api/omarai.py#L769) | 769 | `"            if not self._rate_limit_ok():"` | — |
| [SRC-EEF2E6447C-L000770](../../api/omarai.py#L770) | 770 | `"                return self.respond(429, {\"error\": \"تجاوزت حد الطلبات المؤقت؛ حاول بعد دقيقة.\"})"` | — |
| [SRC-EEF2E6447C-L000771](../../api/omarai.py#L771) | 771 | `"            if not self._authorized():"` | — |
| [SRC-EEF2E6447C-L000772](../../api/omarai.py#L772) | 772 | `"                return self.respond(401, {\"error\": \"لا توجد جلسة صالحة؛ سجّل الدخول مجددًا.\"})"` | — |
| [SRC-EEF2E6447C-L000773](../../api/omarai.py#L773) | 773 | `"            return self.respond("` | — |
| [SRC-EEF2E6447C-L000774](../../api/omarai.py#L774) | 774 | `"                200,"` | — |
| [SRC-EEF2E6447C-L000775](../../api/omarai.py#L775) | 775 | `"                {"` | — |
| [SRC-EEF2E6447C-L000776](../../api/omarai.py#L776) | 776 | `"                    \"authenticated\": True,"` | — |
| [SRC-EEF2E6447C-L000777](../../api/omarai.py#L777) | 777 | `"                    \"role\": self._authenticated_principal[\"role\"],"` | — |
| [SRC-EEF2E6447C-L000778](../../api/omarai.py#L778) | 778 | `"                },"` | — |
| [SRC-EEF2E6447C-L000779](../../api/omarai.py#L779) | 779 | `"            )"` | — |
| [SRC-EEF2E6447C-L000780](../../api/omarai.py#L780) | 780 | `"        if parsed.path == \"/api/leads\":"` | — |
| [SRC-EEF2E6447C-L000781](../../api/omarai.py#L781) | 781 | `"            if not self._rate_limit_ok():"` | — |
| [SRC-EEF2E6447C-L000782](../../api/omarai.py#L782) | 782 | `"                return self.respond(429, {\"error\": \"تجاوزت حد الطلبات المؤقت؛ حاول بعد دقيقة.\"})"` | — |
| [SRC-EEF2E6447C-L000783](../../api/omarai.py#L783) | 783 | `"            if not self._authorized():"` | — |
| [SRC-EEF2E6447C-L000784](../../api/omarai.py#L784) | 784 | `"                return self.respond(401, {\"error\": \"يلزم رمز الوصول الخاص بالتطبيق.\"})"` | — |
| [SRC-EEF2E6447C-L000785](../../api/omarai.py#L785) | 785 | `"            q = parse_qs(parsed.query)"` | — |
| [SRC-EEF2E6447C-L000786](../../api/omarai.py#L786) | 786 | `"            try:"` | — |
| [SRC-EEF2E6447C-L000787](../../api/omarai.py#L787) | 787 | `"                limit = max(1, min(int(q.get(\"limit\", [\"100\"])[0]), 500))"` | — |
| [SRC-EEF2E6447C-L000788](../../api/omarai.py#L788) | 788 | `"                leads = self.store.list(q.get(\"status\", [None])[0], limit, tenant_id=self._authenticated_principal[\"tenant_id\"])"` | — |
| [SRC-EEF2E6447C-L000789](../../api/omarai.py#L789) | 789 | `"            except (ValueError, TypeError):"` | — |
| [SRC-EEF2E6447C-L000790](../../api/omarai.py#L790) | 790 | `"                return self.respond(400, {\"error\": \"invalid status or limit\"})"` | — |
| [SRC-EEF2E6447C-L000791](../../api/omarai.py#L791) | 791 | `"            return self.respond(200, {\"leads\": leads, \"count\": len(leads)})"` | — |
| [SRC-EEF2E6447C-L000792](../../api/omarai.py#L792) | 792 | `"        return self.respond(404, {\"error\": \"not found\"})"` | — |
| [SRC-EEF2E6447C-L000793](../../api/omarai.py#L793) | 793 | `""` | — |
| [SRC-EEF2E6447C-L000794](../../api/omarai.py#L794) | 794 | `"    def do_POST(self):"` | — |
| [SRC-EEF2E6447C-L000795](../../api/omarai.py#L795) | 795 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000796](../../api/omarai.py#L796) | 796 | `"            # Count API attempts before origin/content-type/body validation so invalid"` | — |
| [SRC-EEF2E6447C-L000797](../../api/omarai.py#L797) | 797 | `"            # credentials and malformed requests cannot bypass per-client throttling."` | — |
| [SRC-EEF2E6447C-L000798](../../api/omarai.py#L798) | 798 | `"            path = urlparse(self.path).path"` | — |
| [SRC-EEF2E6447C-L000799](../../api/omarai.py#L799) | 799 | `"            if path.startswith(\"/api/\") and not self._rate_limit_ok():"` | — |
| [SRC-EEF2E6447C-L000800](../../api/omarai.py#L800) | 800 | `"                return self.respond(429, {\"error\": \"تجاوزت حد الطلبات المؤقت؛ حاول بعد دقيقة.\"})"` | — |
| [SRC-EEF2E6447C-L000801](../../api/omarai.py#L801) | 801 | `"            session_login = path == \"/api/session\""` | — |
| [SRC-EEF2E6447C-L000802](../../api/omarai.py#L802) | 802 | `"            session_logout = path == \"/api/session/logout\""` | — |
| [SRC-EEF2E6447C-L000803](../../api/omarai.py#L803) | 803 | `"            if session_logout:"` | — |
| [SRC-EEF2E6447C-L000804](../../api/omarai.py#L804) | 804 | `"                # Logout is idempotent: an expired/revoked session must still be"` | — |
| [SRC-EEF2E6447C-L000805](../../api/omarai.py#L805) | 805 | `"                # able to clear the browser cookie. Resolve it opportunistically"` | — |
| [SRC-EEF2E6447C-L000806](../../api/omarai.py#L806) | 806 | `"                # so a live session is revoked, but do not require it to be valid."` | — |
| [SRC-EEF2E6447C-L000807](../../api/omarai.py#L807) | 807 | `"                self._authorized()"` | — |
| [SRC-EEF2E6447C-L000808](../../api/omarai.py#L808) | 808 | `"            elif path.startswith(\"/api/\") and not session_login and not self._authorized():"` | — |
| [SRC-EEF2E6447C-L000809](../../api/omarai.py#L809) | 809 | `"                return self.respond(401, {\"error\": \"يلزم رمز الوصول الخاص بالتطبيق.\"})"` | — |
| [SRC-EEF2E6447C-L000810](../../api/omarai.py#L810) | 810 | `""` | — |
| [SRC-EEF2E6447C-L000811](../../api/omarai.py#L811) | 811 | `"            content_type = self.headers.get(\"Content-Type\", \"\").split(\";\", 1)[0].strip().lower()"` | — |
| [SRC-EEF2E6447C-L000812](../../api/omarai.py#L812) | 812 | `"            if content_type != \"application/json\":"` | — |
| [SRC-EEF2E6447C-L000813](../../api/omarai.py#L813) | 813 | `"                return self.respond(415, {\"error\": \"Content-Type must be application/json\"})"` | — |
| [SRC-EEF2E6447C-L000814](../../api/omarai.py#L814) | 814 | `"            origin = self.headers.get(\"Origin\")"` | — |
| [SRC-EEF2E6447C-L000815](../../api/omarai.py#L815) | 815 | `"            if session_login and (not origin or not self._origin_allowed(origin)):"` | — |
| [SRC-EEF2E6447C-L000816](../../api/omarai.py#L816) | 816 | `"                return self.respond(403, {\"error\": \"browser session login requires a trusted same-origin request\"})"` | — |
| [SRC-EEF2E6447C-L000817](../../api/omarai.py#L817) | 817 | `"            if ("` | — |
| [SRC-EEF2E6447C-L000818](../../api/omarai.py#L818) | 818 | `"                session_logout"` | — |
| [SRC-EEF2E6447C-L000819](../../api/omarai.py#L819) | 819 | `"                and os.getenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"\").strip() == \"1\""` | — |
| [SRC-EEF2E6447C-L000820](../../api/omarai.py#L820) | 820 | `"                and (not origin or not self._origin_allowed(origin))"` | — |
| [SRC-EEF2E6447C-L000821](../../api/omarai.py#L821) | 821 | `"            ):"` | — |
| [SRC-EEF2E6447C-L000822](../../api/omarai.py#L822) | 822 | `"                return self.respond(403, {\"error\": \"browser session logout requires a trusted same-origin request\"})"` | — |
| [SRC-EEF2E6447C-L000823](../../api/omarai.py#L823) | 823 | `"            if origin and not self._origin_allowed(origin):"` | — |
| [SRC-EEF2E6447C-L000824](../../api/omarai.py#L824) | 824 | `"                return self.respond(403, {\"error\": \"cross-origin requests are not allowed\"})"` | — |
| [SRC-EEF2E6447C-L000825](../../api/omarai.py#L825) | 825 | `"            if getattr(self, \"_cookie_authenticated\", False) and ("` | — |
| [SRC-EEF2E6447C-L000826](../../api/omarai.py#L826) | 826 | `"                not origin or not self._origin_allowed(origin)"` | — |
| [SRC-EEF2E6447C-L000827](../../api/omarai.py#L827) | 827 | `"            ):"` | — |
| [SRC-EEF2E6447C-L000828](../../api/omarai.py#L828) | 828 | `"                return self.respond(403, {\"error\": \"cookie-authenticated requests require a trusted Origin\"})"` | — |
| [SRC-EEF2E6447C-L000829](../../api/omarai.py#L829) | 829 | `""` | — |
| [SRC-EEF2E6447C-L000830](../../api/omarai.py#L830) | 830 | `"            raw_body = self._read_request_body()"` | — |
| [SRC-EEF2E6447C-L000831](../../api/omarai.py#L831) | 831 | `"            if raw_body is None:"` | — |
| [SRC-EEF2E6447C-L000832](../../api/omarai.py#L832) | 832 | `"                return"` | — |
| [SRC-EEF2E6447C-L000833](../../api/omarai.py#L833) | 833 | `"            data = json.loads(raw_body)"` | — |
| [SRC-EEF2E6447C-L000834](../../api/omarai.py#L834) | 834 | `"            if not isinstance(data, dict):"` | — |
| [SRC-EEF2E6447C-L000835](../../api/omarai.py#L835) | 835 | `"                return self.respond(400, {\"error\": \"request body must be a JSON object\"})"` | — |
| [SRC-EEF2E6447C-L000836](../../api/omarai.py#L836) | 836 | `"            if path == \"/api/session\":"` | — |
| [SRC-EEF2E6447C-L000837](../../api/omarai.py#L837) | 837 | `"                token = data.get(\"access_token\", \"\")"` | — |
| [SRC-EEF2E6447C-L000838](../../api/omarai.py#L838) | 838 | `"                if not isinstance(token, str) or len(token.strip()) < 32:"` | — |
| [SRC-EEF2E6447C-L000839](../../api/omarai.py#L839) | 839 | `"                    return self.respond(401, {\"error\": \"رمز الوصول غير صالح.\"})"` | — |
| [SRC-EEF2E6447C-L000840](../../api/omarai.py#L840) | 840 | `"                session = self.store.create_web_session("` | — |
| [SRC-EEF2E6447C-L000841](../../api/omarai.py#L841) | 841 | `"                    token.strip(),"` | — |
| [SRC-EEF2E6447C-L000842](../../api/omarai.py#L842) | 842 | `"                    shared_token=os.getenv(\"OMARAI_ACCESS_TOKEN\", \"\").strip(),"` | — |
| [SRC-EEF2E6447C-L000843](../../api/omarai.py#L843) | 843 | `"                    max_age_seconds=BROWSER_SESSION_COOKIE_MAX_AGE,"` | — |
| [SRC-EEF2E6447C-L000844](../../api/omarai.py#L844) | 844 | `"                )"` | — |
| [SRC-EEF2E6447C-L000845](../../api/omarai.py#L845) | 845 | `"                if not session:"` | — |
| [SRC-EEF2E6447C-L000846](../../api/omarai.py#L846) | 846 | `"                    return self.respond(401, {\"error\": \"رمز الوصول غير صحيح أو منتهي الصلاحية.\"})"` | — |
| [SRC-EEF2E6447C-L000847](../../api/omarai.py#L847) | 847 | `"                session_id, principal = session"` | — |
| [SRC-EEF2E6447C-L000848](../../api/omarai.py#L848) | 848 | `"                self._authenticated_principal = principal"` | — |
| [SRC-EEF2E6447C-L000849](../../api/omarai.py#L849) | 849 | `"                return self.respond("` | — |
| [SRC-EEF2E6447C-L000850](../../api/omarai.py#L850) | 850 | `"                    200,"` | — |
| [SRC-EEF2E6447C-L000851](../../api/omarai.py#L851) | 851 | `"                    {\"authenticated\": True, \"role\": principal[\"role\"]},"` | — |
| [SRC-EEF2E6447C-L000852](../../api/omarai.py#L852) | 852 | `"                    extra_headers=[(\"Set-Cookie\", self._session_cookie_header(session_id))],"` | — |
| [SRC-EEF2E6447C-L000853](../../api/omarai.py#L853) | 853 | `"                )"` | — |
| [SRC-EEF2E6447C-L000854](../../api/omarai.py#L854) | 854 | `""` | — |
| [SRC-EEF2E6447C-L000855](../../api/omarai.py#L855) | 855 | `"            if path == \"/api/session/logout\":"` | — |
| [SRC-EEF2E6447C-L000856](../../api/omarai.py#L856) | 856 | `"                session_id = getattr(self, \"_browser_session_id\", \"\")"` | — |
| [SRC-EEF2E6447C-L000857](../../api/omarai.py#L857) | 857 | `"                if session_id:"` | — |
| [SRC-EEF2E6447C-L000858](../../api/omarai.py#L858) | 858 | `"                    self.store.revoke_web_session(session_id)"` | — |
| [SRC-EEF2E6447C-L000859](../../api/omarai.py#L859) | 859 | `"                return self.respond("` | — |
| [SRC-EEF2E6447C-L000860](../../api/omarai.py#L860) | 860 | `"                    200,"` | — |
| [SRC-EEF2E6447C-L000861](../../api/omarai.py#L861) | 861 | `"                    {\"logged_out\": True},"` | — |
| [SRC-EEF2E6447C-L000862](../../api/omarai.py#L862) | 862 | `"                    extra_headers=[(\"Set-Cookie\", self._clear_session_cookie_header())],"` | — |
| [SRC-EEF2E6447C-L000863](../../api/omarai.py#L863) | 863 | `"                )"` | — |
| [SRC-EEF2E6447C-L000864](../../api/omarai.py#L864) | 864 | `""` | — |
| [SRC-EEF2E6447C-L000865](../../api/omarai.py#L865) | 865 | `"            if path == \"/api/product-profiles\":"` | — |
| [SRC-EEF2E6447C-L000866](../../api/omarai.py#L866) | 866 | `"                principal = self._authenticated_principal"` | — |
| [SRC-EEF2E6447C-L000867](../../api/omarai.py#L867) | 867 | `"                if principal.get(\"role\") == \"viewer\":"` | — |
| [SRC-EEF2E6447C-L000868](../../api/omarai.py#L868) | 868 | `"                    return self.respond(403, {\"error\": \"هذه العضوية للقراءة فقط.\"})"` | — |
| [SRC-EEF2E6447C-L000869](../../api/omarai.py#L869) | 869 | `"                product, market, locale = _product_market_from_payload(data)"` | — |
| [SRC-EEF2E6447C-L000870](../../api/omarai.py#L870) | 870 | `"                saved = self.store.save_product_profile("` | — |
| [SRC-EEF2E6447C-L000871](../../api/omarai.py#L871) | 871 | `"                    {"` | — |
| [SRC-EEF2E6447C-L000872](../../api/omarai.py#L872) | 872 | `"                        \"product\": product.to_dict(),"` | — |
| [SRC-EEF2E6447C-L000873](../../api/omarai.py#L873) | 873 | `"                        \"market\": market.to_dict(),"` | — |
| [SRC-EEF2E6447C-L000874](../../api/omarai.py#L874) | 874 | `"                        \"locale\": locale,"` | — |
| [SRC-EEF2E6447C-L000875](../../api/omarai.py#L875) | 875 | `"                    },"` | — |
| [SRC-EEF2E6447C-L000876](../../api/omarai.py#L876) | 876 | `"                    tenant_id=principal[\"tenant_id\"],"` | — |
| [SRC-EEF2E6447C-L000877](../../api/omarai.py#L877) | 877 | `"                )"` | — |
| [SRC-EEF2E6447C-L000878](../../api/omarai.py#L878) | 878 | `"                return self.respond(201, saved)"` | — |
| [SRC-EEF2E6447C-L000879](../../api/omarai.py#L879) | 879 | `""` | — |
| [SRC-EEF2E6447C-L000880](../../api/omarai.py#L880) | 880 | `"            if path == \"/api/discoveries\":"` | — |
| [SRC-EEF2E6447C-L000881](../../api/omarai.py#L881) | 881 | `"                principal = self._authenticated_principal"` | — |
| [SRC-EEF2E6447C-L000882](../../api/omarai.py#L882) | 882 | `"                if principal.get(\"role\") == \"viewer\":"` | — |
| [SRC-EEF2E6447C-L000883](../../api/omarai.py#L883) | 883 | `"                    return self.respond(403, {\"error\": \"هذه العضوية للقراءة فقط؛ لا يمكنها تشغيل الاكتشاف.\"})"` | — |
| [SRC-EEF2E6447C-L000884](../../api/omarai.py#L884) | 884 | `"                profile_id = data.get(\"profile_id\")"` | — |
| [SRC-EEF2E6447C-L000885](../../api/omarai.py#L885) | 885 | `"                if not isinstance(profile_id, str) or not profile_id.strip():"` | — |
| [SRC-EEF2E6447C-L000886](../../api/omarai.py#L886) | 886 | `"                    return self.respond(400, {\"error\": \"profile_id is required\"})"` | — |
| [SRC-EEF2E6447C-L000887](../../api/omarai.py#L887) | 887 | `"                allow_optional = data.get(\"allow_optional_providers\", False)"` | — |
| [SRC-EEF2E6447C-L000888](../../api/omarai.py#L888) | 888 | `"                if not isinstance(allow_optional, bool):"` | — |
| [SRC-EEF2E6447C-L000889](../../api/omarai.py#L889) | 889 | `"                    return self.respond(400, {\"error\": \"allow_optional_providers must be a boolean\"})"` | — |
| [SRC-EEF2E6447C-L000890](../../api/omarai.py#L890) | 890 | `"                if allow_optional and principal.get(\"role\") != \"owner\":"` | — |
| [SRC-EEF2E6447C-L000891](../../api/omarai.py#L891) | 891 | `"                    return self.respond("` | — |
| [SRC-EEF2E6447C-L000892](../../api/omarai.py#L892) | 892 | `"                        403,"` | — |
| [SRC-EEF2E6447C-L000893](../../api/omarai.py#L893) | 893 | `"                        {\"error\": \"تفعيل موصلات البحث الاختيارية ذات الحصص متاح لمالك مساحة العمل فقط.\"},"` | — |
| [SRC-EEF2E6447C-L000894](../../api/omarai.py#L894) | 894 | `"                    )"` | — |
| [SRC-EEF2E6447C-L000895](../../api/omarai.py#L895) | 895 | `"                profile = self.store.get_product_profile("` | — |
| [SRC-EEF2E6447C-L000896](../../api/omarai.py#L896) | 896 | `"                    profile_id, tenant_id=principal[\"tenant_id\"]"` | — |
| [SRC-EEF2E6447C-L000897](../../api/omarai.py#L897) | 897 | `"                )"` | — |
| [SRC-EEF2E6447C-L000898](../../api/omarai.py#L898) | 898 | `"                if profile is None:"` | — |
| [SRC-EEF2E6447C-L000899](../../api/omarai.py#L899) | 899 | `"                    return self.respond(404, {\"error\": \"product profile not found\"})"` | — |
| [SRC-EEF2E6447C-L000900](../../api/omarai.py#L900) | 900 | `"                product_data = profile[\"profile\"].get(\"product\", {})"` | — |
| [SRC-EEF2E6447C-L000901](../../api/omarai.py#L901) | 901 | `"                market_data = profile[\"profile\"].get(\"market\", {})"` | — |
| [SRC-EEF2E6447C-L000902](../../api/omarai.py#L902) | 902 | `"                product, market, locale = _product_market_from_payload({"` | — |
| [SRC-EEF2E6447C-L000903](../../api/omarai.py#L903) | 903 | `"                    \"product\": product_data,"` | — |
| [SRC-EEF2E6447C-L000904](../../api/omarai.py#L904) | 904 | `"                    \"market\": market_data,"` | — |
| [SRC-EEF2E6447C-L000905](../../api/omarai.py#L905) | 905 | `"                    \"locale\": profile[\"profile\"].get(\"locale\", \"auto\"),"` | — |
| [SRC-EEF2E6447C-L000906](../../api/omarai.py#L906) | 906 | `"                })"` | — |
| [SRC-EEF2E6447C-L000907](../../api/omarai.py#L907) | 907 | `"                buyer_queries = build_buyer_queries(product, market, locale=locale)"` | — |
| [SRC-EEF2E6447C-L000908](../../api/omarai.py#L908) | 908 | `"                if not buyer_queries:"` | — |
| [SRC-EEF2E6447C-L000909](../../api/omarai.py#L909) | 909 | `"                    return self.respond(422, {\"error\": \"تعذر إنشاء استعلامات مرتبطة بملف المنتج والسوق.\"})"` | — |
| [SRC-EEF2E6447C-L000910](../../api/omarai.py#L910) | 910 | `"                locations = \"، \".join(market.locations) if market.locations else \"الموقع غير محدد\""` | — |
| [SRC-EEF2E6447C-L000911](../../api/omarai.py#L911) | 911 | `"                question = ("` | — |
| [SRC-EEF2E6447C-L000912](../../api/omarai.py#L912) | 912 | `"                    \"اكتشف إشارات طلب شراء أو توريد معلنة، وميّز الطلب المباشر عن الاهتمام العام. \""` | — |
| [SRC-EEF2E6447C-L000913](../../api/omarai.py#L913) | 913 | `"                    \"المنتج أو الخدمة: \" + product.name + \". السوق والمناطق: \" + locations + \". \""` | — |
| [SRC-EEF2E6447C-L000914](../../api/omarai.py#L914) | 914 | `"                    \"لا تعتبر ذكر المنتج وحده دليل شراء، ولا تخمّن هوية الكاتب.\""` | — |
| [SRC-EEF2E6447C-L000915](../../api/omarai.py#L915) | 915 | `"                )"` | — |
| [SRC-EEF2E6447C-L000916](../../api/omarai.py#L916) | 916 | `"                agent = WebAgent()"` | — |
| [SRC-EEF2E6447C-L000917](../../api/omarai.py#L917) | 917 | `"                agent.allow_optional_providers = allow_optional"` | — |
| [SRC-EEF2E6447C-L000918](../../api/omarai.py#L918) | 918 | `"                if not allow_optional:"` | — |
| [SRC-EEF2E6447C-L000919](../../api/omarai.py#L919) | 919 | `"                    agent.openrouter_web_search_enabled = False"` | — |
| [SRC-EEF2E6447C-L000920](../../api/omarai.py#L920) | 920 | `"                cls = type(self)"` | — |
| [SRC-EEF2E6447C-L000921](../../api/omarai.py#L921) | 921 | `"                if not cls._agent_semaphore.acquire(blocking=False):"` | — |
| [SRC-EEF2E6447C-L000922](../../api/omarai.py#L922) | 922 | `"                    return self.respond("` | — |
| [SRC-EEF2E6447C-L000923](../../api/omarai.py#L923) | 923 | `"                        503,"` | — |
| [SRC-EEF2E6447C-L000924](../../api/omarai.py#L924) | 924 | `"                        {"` | — |
| [SRC-EEF2E6447C-L000925](../../api/omarai.py#L925) | 925 | `"                            \"error\": \"خدمة البحث مشغولة حاليًا؛ أعد المحاولة بعد قليل.\","` | — |
| [SRC-EEF2E6447C-L000926](../../api/omarai.py#L926) | 926 | `"                            \"retry_after_seconds\": 5,"` | — |
| [SRC-EEF2E6447C-L000927](../../api/omarai.py#L927) | 927 | `"                            \"process_concurrency_limit\": cls.AGENT_CONCURRENCY_LIMIT,"` | — |
| [SRC-EEF2E6447C-L000928](../../api/omarai.py#L928) | 928 | `"                        },"` | — |
| [SRC-EEF2E6447C-L000929](../../api/omarai.py#L929) | 929 | `"                    )"` | — |
| [SRC-EEF2E6447C-L000930](../../api/omarai.py#L930) | 930 | `"                try:"` | — |
| [SRC-EEF2E6447C-L000931](../../api/omarai.py#L931) | 931 | `"                    result = agent.answer(question, buyer_queries=buyer_queries)"` | — |
| [SRC-EEF2E6447C-L000932](../../api/omarai.py#L932) | 932 | `"                    run = self.store.save_discovery_run("` | — |
| [SRC-EEF2E6447C-L000933](../../api/omarai.py#L933) | 933 | `"                        profile_id, result, tenant_id=principal[\"tenant_id\"]"` | — |
| [SRC-EEF2E6447C-L000934](../../api/omarai.py#L934) | 934 | `"                    )"` | — |
| [SRC-EEF2E6447C-L000935](../../api/omarai.py#L935) | 935 | `"                    if run is None:"` | — |
| [SRC-EEF2E6447C-L000936](../../api/omarai.py#L936) | 936 | `"                        return self.respond(404, {\"error\": \"product profile not found\"})"` | — |
| [SRC-EEF2E6447C-L000937](../../api/omarai.py#L937) | 937 | `"                    return self.respond(201, run)"` | — |
| [SRC-EEF2E6447C-L000938](../../api/omarai.py#L938) | 938 | `"                finally:"` | — |
| [SRC-EEF2E6447C-L000939](../../api/omarai.py#L939) | 939 | `"                    cls._agent_semaphore.release()"` | — |
| [SRC-EEF2E6447C-L000940](../../api/omarai.py#L940) | 940 | `""` | — |
| [SRC-EEF2E6447C-L000941](../../api/omarai.py#L941) | 941 | `"            if path.startswith(\"/api/discoveries/\"):"` | — |
| [SRC-EEF2E6447C-L000942](../../api/omarai.py#L942) | 942 | `"                parts = path.split(\"/\")"` | — |
| [SRC-EEF2E6447C-L000943](../../api/omarai.py#L943) | 943 | `"                if ("` | — |
| [SRC-EEF2E6447C-L000944](../../api/omarai.py#L944) | 944 | `"                    len(parts) == 7"` | — |
| [SRC-EEF2E6447C-L000945](../../api/omarai.py#L945) | 945 | `"                    and parts[1:3] == [\"api\", \"discoveries\"]"` | — |
| [SRC-EEF2E6447C-L000946](../../api/omarai.py#L946) | 946 | `"                    and parts[4] == \"signals\""` | — |
| [SRC-EEF2E6447C-L000947](../../api/omarai.py#L947) | 947 | `"                    and parts[6] == \"save\""` | — |
| [SRC-EEF2E6447C-L000948](../../api/omarai.py#L948) | 948 | `"                ):"` | — |
| [SRC-EEF2E6447C-L000949](../../api/omarai.py#L949) | 949 | `"                    principal = self._authenticated_principal"` | — |
| [SRC-EEF2E6447C-L000950](../../api/omarai.py#L950) | 950 | `"                    if principal.get(\"role\") == \"viewer\":"` | — |
| [SRC-EEF2E6447C-L000951](../../api/omarai.py#L951) | 951 | `"                        return self.respond(403, {\"error\": \"هذه العضوية للقراءة فقط.\"})"` | — |
| [SRC-EEF2E6447C-L000952](../../api/omarai.py#L952) | 952 | `"                    try:"` | — |
| [SRC-EEF2E6447C-L000953](../../api/omarai.py#L953) | 953 | `"                        source_index = int(parts[5])"` | — |
| [SRC-EEF2E6447C-L000954](../../api/omarai.py#L954) | 954 | `"                    except ValueError:"` | — |
| [SRC-EEF2E6447C-L000955](../../api/omarai.py#L955) | 955 | `"                        return self.respond(400, {\"error\": \"source index must be an integer\"})"` | — |
| [SRC-EEF2E6447C-L000956](../../api/omarai.py#L956) | 956 | `"                    saved = self.store.save_discovery_signal("` | — |
| [SRC-EEF2E6447C-L000957](../../api/omarai.py#L957) | 957 | `"                        parts[3],"` | — |
| [SRC-EEF2E6447C-L000958](../../api/omarai.py#L958) | 958 | `"                        source_index,"` | — |
| [SRC-EEF2E6447C-L000959](../../api/omarai.py#L959) | 959 | `"                        tenant_id=principal[\"tenant_id\"],"` | — |
| [SRC-EEF2E6447C-L000960](../../api/omarai.py#L960) | 960 | `"                    )"` | — |
| [SRC-EEF2E6447C-L000961](../../api/omarai.py#L961) | 961 | `"                    if saved is None:"` | — |
| [SRC-EEF2E6447C-L000962](../../api/omarai.py#L962) | 962 | `"                        return self.respond("` | — |
| [SRC-EEF2E6447C-L000963](../../api/omarai.py#L963) | 963 | `"                            409,"` | — |
| [SRC-EEF2E6447C-L000964](../../api/omarai.py#L964) | 964 | `"                            {\"error\": \"هذه النتيجة ليست إشارة طلب مؤهلة في سجل الاكتشاف أو لا تنتمي إلى مساحة العمل.\"},"` | — |
| [SRC-EEF2E6447C-L000965](../../api/omarai.py#L965) | 965 | `"                        )"` | — |
| [SRC-EEF2E6447C-L000966](../../api/omarai.py#L966) | 966 | `"                    lead, created = saved"` | — |
| [SRC-EEF2E6447C-L000967](../../api/omarai.py#L967) | 967 | `"                    return self.respond("` | — |
| [SRC-EEF2E6447C-L000968](../../api/omarai.py#L968) | 968 | `"                        201 if created else 200,"` | — |
| [SRC-EEF2E6447C-L000969](../../api/omarai.py#L969) | 969 | `"                        {\"lead\": lead, \"created\": created},"` | — |
| [SRC-EEF2E6447C-L000970](../../api/omarai.py#L970) | 970 | `"                    )"` | — |
| [SRC-EEF2E6447C-L000971](../../api/omarai.py#L971) | 971 | `""` | — |
| [SRC-EEF2E6447C-L000972](../../api/omarai.py#L972) | 972 | `"            if path == \"/api/tokens/revoke\":"` | — |
| [SRC-EEF2E6447C-L000973](../../api/omarai.py#L973) | 973 | `"                supplied = self.headers.get(\"Authorization\", \"\")"` | — |
| [SRC-EEF2E6447C-L000974](../../api/omarai.py#L974) | 974 | `"                token = supplied[7:].strip() if supplied.startswith(\"Bearer \") else \"\""` | — |
| [SRC-EEF2E6447C-L000975](../../api/omarai.py#L975) | 975 | `"                shared_token = os.getenv(\"OMARAI_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-EEF2E6447C-L000976](../../api/omarai.py#L976) | 976 | `"                if shared_token and hmac.compare_digest(token, shared_token):"` | — |
| [SRC-EEF2E6447C-L000977](../../api/omarai.py#L977) | 977 | `"                    return self.respond("` | — |
| [SRC-EEF2E6447C-L000978](../../api/omarai.py#L978) | 978 | `"                        409,"` | — |
| [SRC-EEF2E6447C-L000979](../../api/omarai.py#L979) | 979 | `"                        {"` | — |
| [SRC-EEF2E6447C-L000980](../../api/omarai.py#L980) | 980 | `"                            \"error\": ("` | — |
| [SRC-EEF2E6447C-L000981](../../api/omarai.py#L981) | 981 | `"                                \"shared application token must be rotated by the operator \""` | — |
| [SRC-EEF2E6447C-L000982](../../api/omarai.py#L982) | 982 | `"                                \"through the deployment configuration\""` | — |
| [SRC-EEF2E6447C-L000983](../../api/omarai.py#L983) | 983 | `"                            )"` | — |
| [SRC-EEF2E6447C-L000984](../../api/omarai.py#L984) | 984 | `"                        },"` | — |
| [SRC-EEF2E6447C-L000985](../../api/omarai.py#L985) | 985 | `"                    )"` | — |
| [SRC-EEF2E6447C-L000986](../../api/omarai.py#L986) | 986 | `"                revoked = self.store.revoke_api_token("` | — |
| [SRC-EEF2E6447C-L000987](../../api/omarai.py#L987) | 987 | `"                    token,"` | — |
| [SRC-EEF2E6447C-L000988](../../api/omarai.py#L988) | 988 | `"                    tenant_id=self._authenticated_principal[\"tenant_id\"],"` | — |
| [SRC-EEF2E6447C-L000989](../../api/omarai.py#L989) | 989 | `"                    user_id=self._authenticated_principal[\"user_id\"],"` | — |
| [SRC-EEF2E6447C-L000990](../../api/omarai.py#L990) | 990 | `"                )"` | — |
| [SRC-EEF2E6447C-L000991](../../api/omarai.py#L991) | 991 | `"                if not revoked:"` | — |
| [SRC-EEF2E6447C-L000992](../../api/omarai.py#L992) | 992 | `"                    return self.respond(404, {\"error\": \"token not found\"})"` | — |
| [SRC-EEF2E6447C-L000993](../../api/omarai.py#L993) | 993 | `"                return self.respond(200, {\"revoked\": True})"` | — |
| [SRC-EEF2E6447C-L000994](../../api/omarai.py#L994) | 994 | `""` | — |
| [SRC-EEF2E6447C-L000995](../../api/omarai.py#L995) | 995 | `"            if path == \"/api/diagnostics\":"` | — |
| [SRC-EEF2E6447C-L000996](../../api/omarai.py#L996) | 996 | `"                test_model = data.get(\"test_model\", False)"` | — |
| [SRC-EEF2E6447C-L000997](../../api/omarai.py#L997) | 997 | `"                test_social = data.get(\"test_social\", False)"` | — |
| [SRC-EEF2E6447C-L000998](../../api/omarai.py#L998) | 998 | `"                allow_provider_usage = data.get(\"allow_provider_usage\", False)"` | — |
| [SRC-EEF2E6447C-L000999](../../api/omarai.py#L999) | 999 | `"                if ("` | — |
| [SRC-EEF2E6447C-L001000](../../api/omarai.py#L1000) | 1000 | `"                    not isinstance(test_model, bool)"` | — |
| [SRC-EEF2E6447C-L001001](../../api/omarai.py#L1001) | 1001 | `"                    or not isinstance(test_social, bool)"` | — |
| [SRC-EEF2E6447C-L001002](../../api/omarai.py#L1002) | 1002 | `"                    or not isinstance(allow_provider_usage, bool)"` | — |
| [SRC-EEF2E6447C-L001003](../../api/omarai.py#L1003) | 1003 | `"                ):"` | — |
| [SRC-EEF2E6447C-L001004](../../api/omarai.py#L1004) | 1004 | `"                    return self.respond("` | — |
| [SRC-EEF2E6447C-L001005](../../api/omarai.py#L1005) | 1005 | `"                        400,"` | — |
| [SRC-EEF2E6447C-L001006](../../api/omarai.py#L1006) | 1006 | `"                        {"` | — |
| [SRC-EEF2E6447C-L001007](../../api/omarai.py#L1007) | 1007 | `"                            \"error\": ("` | — |
| [SRC-EEF2E6447C-L001008](../../api/omarai.py#L1008) | 1008 | `"                                \"test_model, test_social, and allow_provider_usage \""` | — |
| [SRC-EEF2E6447C-L001009](../../api/omarai.py#L1009) | 1009 | `"                                \"must be booleans\""` | — |
| [SRC-EEF2E6447C-L001010](../../api/omarai.py#L1010) | 1010 | `"                            )"` | — |
| [SRC-EEF2E6447C-L001011](../../api/omarai.py#L1011) | 1011 | `"                        },"` | — |
| [SRC-EEF2E6447C-L001012](../../api/omarai.py#L1012) | 1012 | `"                    )"` | — |
| [SRC-EEF2E6447C-L001013](../../api/omarai.py#L1013) | 1013 | `"                if not allow_provider_usage:"` | — |
| [SRC-EEF2E6447C-L001014](../../api/omarai.py#L1014) | 1014 | `"                    return self.respond("` | — |
| [SRC-EEF2E6447C-L001015](../../api/omarai.py#L1015) | 1015 | `"                        403,"` | — |
| [SRC-EEF2E6447C-L001016](../../api/omarai.py#L1016) | 1016 | `"                        {"` | — |
| [SRC-EEF2E6447C-L001017](../../api/omarai.py#L1017) | 1017 | `"                            \"error\": ("` | — |
| [SRC-EEF2E6447C-L001018](../../api/omarai.py#L1018) | 1018 | `"                                \"live diagnostics perform outbound search and may consume \""` | — |
| [SRC-EEF2E6447C-L001019](../../api/omarai.py#L1019) | 1019 | `"                                \"provider quota or incur charges; set allow_provider_usage=true \""` | — |
| [SRC-EEF2E6447C-L001020](../../api/omarai.py#L1020) | 1020 | `"                                \"only after explicit owner approval\""` | — |
| [SRC-EEF2E6447C-L001021](../../api/omarai.py#L1021) | 1021 | `"                            )"` | — |
| [SRC-EEF2E6447C-L001022](../../api/omarai.py#L1022) | 1022 | `"                        },"` | — |
| [SRC-EEF2E6447C-L001023](../../api/omarai.py#L1023) | 1023 | `"                    )"` | — |
| [SRC-EEF2E6447C-L001024](../../api/omarai.py#L1024) | 1024 | `"                if self._authenticated_principal.get(\"role\") != \"owner\":"` | — |
| [SRC-EEF2E6447C-L001025](../../api/omarai.py#L1025) | 1025 | `"                    return self.respond("` | — |
| [SRC-EEF2E6447C-L001026](../../api/omarai.py#L1026) | 1026 | `"                        403,"` | — |
| [SRC-EEF2E6447C-L001027](../../api/omarai.py#L1027) | 1027 | `"                        {\"error\": \"فحص الموصلات الحي واستهلاك الحصص متاح لمالك مساحة العمل فقط.\"},"` | — |
| [SRC-EEF2E6447C-L001028](../../api/omarai.py#L1028) | 1028 | `"                    )"` | — |
| [SRC-EEF2E6447C-L001029](../../api/omarai.py#L1029) | 1029 | `"                return self._run_bounded_agent_operation("` | — |
| [SRC-EEF2E6447C-L001030](../../api/omarai.py#L1030) | 1030 | `"                    lambda: WebAgent().diagnostics("` | — |
| [SRC-EEF2E6447C-L001031](../../api/omarai.py#L1031) | 1031 | `"                        test_model=test_model,"` | — |
| [SRC-EEF2E6447C-L001032](../../api/omarai.py#L1032) | 1032 | `"                        test_social=test_social,"` | — |
| [SRC-EEF2E6447C-L001033](../../api/omarai.py#L1033) | 1033 | `"                    )"` | — |
| [SRC-EEF2E6447C-L001034](../../api/omarai.py#L1034) | 1034 | `"                )"` | — |
| [SRC-EEF2E6447C-L001035](../../api/omarai.py#L1035) | 1035 | `""` | — |
| [SRC-EEF2E6447C-L001036](../../api/omarai.py#L1036) | 1036 | `"            if path == \"/api/agent\":"` | — |
| [SRC-EEF2E6447C-L001037](../../api/omarai.py#L1037) | 1037 | `"                if self._authenticated_principal.get(\"role\") == \"viewer\":"` | — |
| [SRC-EEF2E6447C-L001038](../../api/omarai.py#L1038) | 1038 | `"                    return self.respond("` | — |
| [SRC-EEF2E6447C-L001039](../../api/omarai.py#L1039) | 1039 | `"                        403,"` | — |
| [SRC-EEF2E6447C-L001040](../../api/omarai.py#L1040) | 1040 | `"                        {\"error\": \"عضوية viewer لا تملك صلاحية تشغيل البحث أو النموذج.\"},"` | — |
| [SRC-EEF2E6447C-L001041](../../api/omarai.py#L1041) | 1041 | `"                    )"` | — |
| [SRC-EEF2E6447C-L001042](../../api/omarai.py#L1042) | 1042 | `"                question = data.get(\"question\", \"\")"` | — |
| [SRC-EEF2E6447C-L001043](../../api/omarai.py#L1043) | 1043 | `"                if not isinstance(question, str) or not question.strip():"` | — |
| [SRC-EEF2E6447C-L001044](../../api/omarai.py#L1044) | 1044 | `"                    return self.respond(400, {\"error\": \"question must be a non-empty string\"})"` | — |
| [SRC-EEF2E6447C-L001045](../../api/omarai.py#L1045) | 1045 | `"                request_profile = data.get(\"request_profile\", \"default\")"` | — |
| [SRC-EEF2E6447C-L001046](../../api/omarai.py#L1046) | 1046 | `"                if not isinstance(request_profile, str) or request_profile not in {"` | — |
| [SRC-EEF2E6447C-L001047](../../api/omarai.py#L1047) | 1047 | `"                    \"default\", \"hosted_smoke\""` | — |
| [SRC-EEF2E6447C-L001048](../../api/omarai.py#L1048) | 1048 | `"                }:"` | — |
| [SRC-EEF2E6447C-L001049](../../api/omarai.py#L1049) | 1049 | `"                    return self.respond(400, {\"error\": \"request_profile must be default or hosted_smoke\"})"` | — |
| [SRC-EEF2E6447C-L001050](../../api/omarai.py#L1050) | 1050 | `"                agent = WebAgent()"` | — |
| [SRC-EEF2E6447C-L001051](../../api/omarai.py#L1051) | 1051 | `"                history = data.get(\"history\", [])"` | — |
| [SRC-EEF2E6447C-L001052](../../api/omarai.py#L1052) | 1052 | `"                if \"mode\" not in data:"` | — |
| [SRC-EEF2E6447C-L001053](../../api/omarai.py#L1053) | 1053 | `"                    return self._run_bounded_agent_operation("` | — |
| [SRC-EEF2E6447C-L001054](../../api/omarai.py#L1054) | 1054 | `"                        lambda: agent.answer("` | — |
| [SRC-EEF2E6447C-L001055](../../api/omarai.py#L1055) | 1055 | `"                            question, history, budget_profile=request_profile"` | — |
| [SRC-EEF2E6447C-L001056](../../api/omarai.py#L1056) | 1056 | `"                        )"` | — |
| [SRC-EEF2E6447C-L001057](../../api/omarai.py#L1057) | 1057 | `"                    )"` | — |
| [SRC-EEF2E6447C-L001058](../../api/omarai.py#L1058) | 1058 | `"                return self._run_bounded_agent_operation("` | — |
| [SRC-EEF2E6447C-L001059](../../api/omarai.py#L1059) | 1059 | `"                    lambda: agent.answer("` | — |
| [SRC-EEF2E6447C-L001060](../../api/omarai.py#L1060) | 1060 | `"                        question, history, data.get(\"mode\"),"` | — |
| [SRC-EEF2E6447C-L001061](../../api/omarai.py#L1061) | 1061 | `"                        budget_profile=request_profile,"` | — |
| [SRC-EEF2E6447C-L001062](../../api/omarai.py#L1062) | 1062 | `"                    )"` | — |
| [SRC-EEF2E6447C-L001063](../../api/omarai.py#L1063) | 1063 | `"                )"` | — |
| [SRC-EEF2E6447C-L001064](../../api/omarai.py#L1064) | 1064 | `""` | — |
| [SRC-EEF2E6447C-L001065](../../api/omarai.py#L1065) | 1065 | `"            if path == \"/api/ask\":"` | — |
| [SRC-EEF2E6447C-L001066](../../api/omarai.py#L1066) | 1066 | `"                question = data.get(\"question\", \"\")"` | — |
| [SRC-EEF2E6447C-L001067](../../api/omarai.py#L1067) | 1067 | `"                if not isinstance(question, str) or not question.strip():"` | — |
| [SRC-EEF2E6447C-L001068](../../api/omarai.py#L1068) | 1068 | `"                    return self.respond(400, {\"error\": \"question must be a non-empty string\"})"` | — |
| [SRC-EEF2E6447C-L001069](../../api/omarai.py#L1069) | 1069 | `"                if len(question) > 1000:"` | — |
| [SRC-EEF2E6447C-L001070](../../api/omarai.py#L1070) | 1070 | `"                    return self.respond(400, {\"error\": \"question must be at most 1000 characters\"})"` | — |
| [SRC-EEF2E6447C-L001071](../../api/omarai.py#L1071) | 1071 | `"                return self.respond(200, answer_question(question, self.store, tenant_id=self._authenticated_principal[\"tenant_id\"]))"` | — |
| [SRC-EEF2E6447C-L001072](../../api/omarai.py#L1072) | 1072 | `"            if path == \"/api/analyze\":"` | — |
| [SRC-EEF2E6447C-L001073](../../api/omarai.py#L1073) | 1073 | `"                return self.respond("` | — |
| [SRC-EEF2E6447C-L001074](../../api/omarai.py#L1074) | 1074 | `"                    200,"` | — |
| [SRC-EEF2E6447C-L001075](../../api/omarai.py#L1075) | 1075 | `"                    analyze("` | — |
| [SRC-EEF2E6447C-L001076](../../api/omarai.py#L1076) | 1076 | `"                        data.get(\"text\", \"\"),"` | — |
| [SRC-EEF2E6447C-L001077](../../api/omarai.py#L1077) | 1077 | `"                        data.get(\"product_terms\", []),"` | — |
| [SRC-EEF2E6447C-L001078](../../api/omarai.py#L1078) | 1078 | `"                        data.get(\"location_terms\", []),"` | — |
| [SRC-EEF2E6447C-L001079](../../api/omarai.py#L1079) | 1079 | `"                    ),"` | — |
| [SRC-EEF2E6447C-L001080](../../api/omarai.py#L1080) | 1080 | `"                )"` | — |
| [SRC-EEF2E6447C-L001081](../../api/omarai.py#L1081) | 1081 | `"            if path == \"/api/leads\":"` | — |
| [SRC-EEF2E6447C-L001082](../../api/omarai.py#L1082) | 1082 | `"                if self._authenticated_principal[\"role\"] == \"viewer\":"` | — |
| [SRC-EEF2E6447C-L001083](../../api/omarai.py#L1083) | 1083 | `"                    return self.respond(403, {\"error\": \"هذه العضوية للقراءة فقط.\"})"` | — |
| [SRC-EEF2E6447C-L001084](../../api/omarai.py#L1084) | 1084 | `"                lead, created = self.store.add("` | — |
| [SRC-EEF2E6447C-L001085](../../api/omarai.py#L1085) | 1085 | `"                    data.get(\"text\", \"\"),"` | — |
| [SRC-EEF2E6447C-L001086](../../api/omarai.py#L1086) | 1086 | `"                    data.get(\"source_url\", \"\"),"` | — |
| [SRC-EEF2E6447C-L001087](../../api/omarai.py#L1087) | 1087 | `"                    data.get(\"platform\", \"manual\"),"` | — |
| [SRC-EEF2E6447C-L001088](../../api/omarai.py#L1088) | 1088 | `"                    data.get(\"observed_at\"),"` | — |
| [SRC-EEF2E6447C-L001089](../../api/omarai.py#L1089) | 1089 | `"                    data.get(\"note\", \"\"),"` | — |
| [SRC-EEF2E6447C-L001090](../../api/omarai.py#L1090) | 1090 | `"                    data.get(\"product_terms\", []),"` | — |
| [SRC-EEF2E6447C-L001091](../../api/omarai.py#L1091) | 1091 | `"                    data.get(\"location_terms\", []),"` | — |
| [SRC-EEF2E6447C-L001092](../../api/omarai.py#L1092) | 1092 | `"                    tenant_id=self._authenticated_principal[\"tenant_id\"],"` | — |
| [SRC-EEF2E6447C-L001093](../../api/omarai.py#L1093) | 1093 | `"                )"` | — |
| [SRC-EEF2E6447C-L001094](../../api/omarai.py#L1094) | 1094 | `"                return self.respond(201 if created else 200, {\"lead\": lead, \"created\": created})"` | — |
| [SRC-EEF2E6447C-L001095](../../api/omarai.py#L1095) | 1095 | `"            route = path.split(\"/\")"` | — |
| [SRC-EEF2E6447C-L001096](../../api/omarai.py#L1096) | 1096 | `"            if len(route) == 5 and route[1:3] == [\"api\", \"leads\"] and route[4] == \"status\":"` | — |
| [SRC-EEF2E6447C-L001097](../../api/omarai.py#L1097) | 1097 | `"                if self._authenticated_principal[\"role\"] == \"viewer\":"` | — |
| [SRC-EEF2E6447C-L001098](../../api/omarai.py#L1098) | 1098 | `"                    return self.respond(403, {\"error\": \"هذه العضوية للقراءة فقط.\"})"` | — |
| [SRC-EEF2E6447C-L001099](../../api/omarai.py#L1099) | 1099 | `"                lead = self.store.update_status(route[3], data.get(\"status\", \"new\"), tenant_id=self._authenticated_principal[\"tenant_id\"])"` | — |
| [SRC-EEF2E6447C-L001100](../../api/omarai.py#L1100) | 1100 | `"                return self.respond(200, {\"lead\": lead}) if lead else self.respond(404, {\"error\": \"lead not found\"})"` | — |
| [SRC-EEF2E6447C-L001101](../../api/omarai.py#L1101) | 1101 | `"            return self.respond(404, {\"error\": \"not found\"})"` | — |
| [SRC-EEF2E6447C-L001102](../../api/omarai.py#L1102) | 1102 | `"        except (ValueError, TypeError, json.JSONDecodeError) as exc:"` | — |
| [SRC-EEF2E6447C-L001103](../../api/omarai.py#L1103) | 1103 | `"            return self.respond(400, {\"error\": str(exc)})"` | — |
| [SRC-EEF2E6447C-L001104](../../api/omarai.py#L1104) | 1104 | `"        except Exception:  # noqa: BLE001 — keep unexpected details out of API responses"` | — |
| [SRC-EEF2E6447C-L001105](../../api/omarai.py#L1105) | 1105 | `"            return self.respond(500, {\"error\": \"internal server error\"})"` | — |
| [SRC-EEF2E6447C-L001106](../../api/omarai.py#L1106) | 1106 | `""` | — |
| [SRC-EEF2E6447C-L001107](../../api/omarai.py#L1107) | 1107 | `"    def do_OPTIONS(self):"` | — |
| [SRC-EEF2E6447C-L001108](../../api/omarai.py#L1108) | 1108 | `"        origin = self.headers.get(\"Origin\")"` | — |
| [SRC-EEF2E6447C-L001109](../../api/omarai.py#L1109) | 1109 | `"        if not origin or not self._origin_allowed(origin):"` | — |
| [SRC-EEF2E6447C-L001110](../../api/omarai.py#L1110) | 1110 | `"            return self.respond(403, {\"error\": \"cross-origin requests are not allowed\"})"` | — |
| [SRC-EEF2E6447C-L001111](../../api/omarai.py#L1111) | 1111 | `"        self.send_response(204)"` | — |
| [SRC-EEF2E6447C-L001112](../../api/omarai.py#L1112) | 1112 | `"        self.send_header(\"Access-Control-Allow-Origin\", origin)"` | — |
| [SRC-EEF2E6447C-L001113](../../api/omarai.py#L1113) | 1113 | `"        self.send_header(\"Vary\", \"Origin\")"` | — |
| [SRC-EEF2E6447C-L001114](../../api/omarai.py#L1114) | 1114 | `"        self.send_header(\"Access-Control-Allow-Methods\", \"GET, POST, OPTIONS\")"` | — |
| [SRC-EEF2E6447C-L001115](../../api/omarai.py#L1115) | 1115 | `"        self.send_header(\"Access-Control-Allow-Headers\", \"Authorization, Content-Type\")"` | — |
| [SRC-EEF2E6447C-L001116](../../api/omarai.py#L1116) | 1116 | `"        self.send_header(\"Access-Control-Max-Age\", \"600\")"` | — |
| [SRC-EEF2E6447C-L001117](../../api/omarai.py#L1117) | 1117 | `"        self.send_header(\"Content-Length\", \"0\")"` | — |
| [SRC-EEF2E6447C-L001118](../../api/omarai.py#L1118) | 1118 | `"        self.end_headers()"` | — |
| [SRC-EEF2E6447C-L001119](../../api/omarai.py#L1119) | 1119 | `""` | — |
| [SRC-EEF2E6447C-L001120](../../api/omarai.py#L1120) | 1120 | `"    def log_message(self, *args):"` | — |
| [SRC-EEF2E6447C-L001121](../../api/omarai.py#L1121) | 1121 | `"        pass"` | — |
| [SRC-EEF2E6447C-L001122](../../api/omarai.py#L1122) | 1122 | `""` | — |
| [SRC-EEF2E6447C-L001123](../../api/omarai.py#L1123) | 1123 | `""` | — |
| [SRC-EEF2E6447C-L001124](../../api/omarai.py#L1124) | 1124 | `"def answer_question(question, store, *, tenant_id=None):"` | — |
| [SRC-EEF2E6447C-L001125](../../api/omarai.py#L1125) | 1125 | `"    \"\"\"Answer common operational questions from local records using explicit rules.\"\"\""` | — |
| [SRC-EEF2E6447C-L001126](../../api/omarai.py#L1126) | 1126 | `"    normalized = normalize(question)"` | — |
| [SRC-EEF2E6447C-L001127](../../api/omarai.py#L1127) | 1127 | `"    leads = store.list(limit=500, tenant_id=tenant_id)"` | — |
| [SRC-EEF2E6447C-L001128](../../api/omarai.py#L1128) | 1128 | `"    active = [lead for lead in leads if lead[\"status\"] not in {\"rejected\", \"converted\"}]"` | — |
| [SRC-EEF2E6447C-L001129](../../api/omarai.py#L1129) | 1129 | `"    if any(term in normalized for term in (\"افضل عميل\", \"احسن عميل\", \"افضل اشارة\", \"احسن اشارة\", \"اشارة اراجعها\", \"مين افضل\", \"مين اتابع\", \"اتابع مين\", \"اهم عميل\")):"` | — |
| [SRC-EEF2E6447C-L001130](../../api/omarai.py#L1130) | 1130 | `"        if not active:"` | — |
| [SRC-EEF2E6447C-L001131](../../api/omarai.py#L1131) | 1131 | `"            return {\"answer\": \"لا توجد إشارة نشطة محفوظة بعد. حلّل نصًا من مصدر مسموح واحفظه أولًا، ثم اسألني مرة أخرى.\", \"kind\": \"no_data\", \"lead_id\": None}"` | — |
| [SRC-EEF2E6447C-L001132](../../api/omarai.py#L1132) | 1132 | `"        lead = max(active, key=lambda item: (item[\"assessment\"][\"score\"], item[\"updated_at\"]))"` | — |
| [SRC-EEF2E6447C-L001133](../../api/omarai.py#L1133) | 1133 | `"        assessment = lead[\"assessment\"]"` | — |
| [SRC-EEF2E6447C-L001134](../../api/omarai.py#L1134) | 1134 | `"        answer = \"الأولوية المقترحة للمراجعة هي الإشارة \" + lead[\"id\"][:8] + \" بدرجة قواعد \" + str(assessment[\"score\"]) + \"/100. السبب: \" + assessment[\"summary\"] + \" المصدر: \" + lead[\"source_url\"] + \". هذه أولوية مراجعة وليست تأكيدًا أن صاحبه سيشتري.\""` | — |
| [SRC-EEF2E6447C-L001135](../../api/omarai.py#L1135) | 1135 | `"        return {\"answer\": answer, \"kind\": \"lead_recommendation\", \"lead_id\": lead[\"id\"]}"` | — |
| [SRC-EEF2E6447C-L001136](../../api/omarai.py#L1136) | 1136 | `"    if any(term in normalized for term in (\"كام عميل\", \"كم عميل\", \"عدد العملاء\", \"عدد الاشارات\", \"الاحصائيات\", \"احصائيات\")):"` | — |
| [SRC-EEF2E6447C-L001137](../../api/omarai.py#L1137) | 1137 | `"        keys = (\"new\", \"qualified\", \"contacted\", \"converted\", \"needs_review\", \"rejected\")"` | — |
| [SRC-EEF2E6447C-L001138](../../api/omarai.py#L1138) | 1138 | `"        by_status = {key: sum(lead[\"status\"] == key for lead in leads) for key in keys}"` | — |
| [SRC-EEF2E6447C-L001139](../../api/omarai.py#L1139) | 1139 | `"        high = sum(lead[\"assessment\"][\"label\"] == \"high_intent\" for lead in leads)"` | — |
| [SRC-EEF2E6447C-L001140](../../api/omarai.py#L1140) | 1140 | `"        answer = \"في السجل المحلي \" + str(len(leads)) + \" إشارة، منها \" + str(high) + \" بإشارة قوية نسبيًا وفق القواعد. الحالات: جديد \" + str(by_status[\"new\"]) + \"، مؤهل \" + str(by_status[\"qualified\"]) + \"، تم التواصل \" + str(by_status[\"contacted\"]) + \"، تم البيع \" + str(by_status[\"converted\"]) + \"، تحتاج مراجعة \" + str(by_status[\"needs_review\"]) + \"، مرفوض \" + str(by_status[\"rejected\"]) + \".\""` | — |
| [SRC-EEF2E6447C-L001141](../../api/omarai.py#L1141) | 1141 | `"        return {\"answer\": answer, \"kind\": \"local_statistics\", \"lead_id\": None}"` | — |
| [SRC-EEF2E6447C-L001142](../../api/omarai.py#L1142) | 1142 | `"    if any(term in normalized for term in (\"ليه الدرجه\", \"سبب الدرجه\", \"طريقة التقييم\", \"بتقيم ازاي\", \"معيار التقييم\")):"` | — |
| [SRC-EEF2E6447C-L001143](../../api/omarai.py#L1143) | 1143 | `"        latest = max(leads, key=lambda item: item[\"updated_at\"], default=None)"` | — |
| [SRC-EEF2E6447C-L001144](../../api/omarai.py#L1144) | 1144 | `"        if latest:"` | — |
| [SRC-EEF2E6447C-L001145](../../api/omarai.py#L1145) | 1145 | `"            signals = \"، \".join(signal[\"phrase\"] for signal in latest[\"assessment\"][\"matched_signals\"]) or \"لم تُطابق عبارات معروفة\""` | — |
| [SRC-EEF2E6447C-L001146](../../api/omarai.py#L1146) | 1146 | `"            answer = \"الإشارة الأحدث درجتها \" + str(latest[\"assessment\"][\"score\"]) + \"/100 لأن القواعد طابقت: \" + signals + \". الدرجة ليست احتمالًا إحصائيًا ولا تثبت نية الكاتب.\""` | — |
| [SRC-EEF2E6447C-L001147](../../api/omarai.py#L1147) | 1147 | `"        else:"` | — |
| [SRC-EEF2E6447C-L001148](../../api/omarai.py#L1148) | 1148 | `"            answer = \"أحسب الدرجة بقواعد واضحة: تعبير الشراء، خطوة تجارية تالية، السعر أو الميزانية، وسياق المنتج والمكان. كل فئة تحتسب مرة واحدة فقط.\""` | — |
| [SRC-EEF2E6447C-L001149](../../api/omarai.py#L1149) | 1149 | `"        return {\"answer\": answer, \"kind\": \"scoring_explanation\", \"lead_id\": latest[\"id\"] if latest else None}"` | — |
| [SRC-EEF2E6447C-L001150](../../api/omarai.py#L1150) | 1150 | `"    if any(term in normalized for term in (\"اكتب رساله\", \"اكتب رسالة\", \"رساله تواصل\", \"رسالة تواصل\", \"ابعتله\", \"اتواصل ازاي\")):"` | — |
| [SRC-EEF2E6447C-L001151](../../api/omarai.py#L1151) | 1151 | `"        if not active:"` | — |
| [SRC-EEF2E6447C-L001152](../../api/omarai.py#L1152) | 1152 | `"            answer = \"لا توجد إشارة محفوظة أخصص مسودة لها بعد. أدخل نصًا ومصدرًا أولًا.\""` | — |
| [SRC-EEF2E6447C-L001153](../../api/omarai.py#L1153) | 1153 | `"        else:"` | — |
| [SRC-EEF2E6447C-L001154](../../api/omarai.py#L1154) | 1154 | `"            lead = max(active, key=lambda item: (item[\"assessment\"][\"score\"], item[\"updated_at\"]))"` | — |
| [SRC-EEF2E6447C-L001155](../../api/omarai.py#L1155) | 1155 | `"            answer = \"مسودة للمراجعة البشرية فقط: «أهلًا، لاحظت سؤالك المنشور عن العقار/الوحدة. لو ما زلت مهتمًا، هل تحب الاطلاع على التفاصيل المتاحة وخيارات المعاينة؟» مرتبطة بالإشارة \" + lead[\"id\"][:8] + \". لم يتم إرسال أي رسالة.\""` | — |
| [SRC-EEF2E6447C-L001156](../../api/omarai.py#L1156) | 1156 | `"        return {\"answer\": answer, \"kind\": \"message_draft\", \"lead_id\": active[0][\"id\"] if active else None}"` | — |
| [SRC-EEF2E6447C-L001157](../../api/omarai.py#L1157) | 1157 | `"    return {\"answer\": \"أنا المساعد المحلي الخاص بسجل العملاء. استخدم وكيل البحث العام من المسار /agent لطرح أسئلة مفتوحة والبحث في الويب.\", \"kind\": \"help\", \"lead_id\": None}"` | — |
| [SRC-EEF2E6447C-L001158](../../api/omarai.py#L1158) | 1158 | `""` | — |
| [SRC-EEF2E6447C-L001159](../../api/omarai.py#L1159) | 1159 | `""` | — |
| [SRC-EEF2E6447C-L001160](../../api/omarai.py#L1160) | 1160 | `"class BoundedThreadingHTTPServer(ThreadingHTTPServer):"` | — |
| [SRC-EEF2E6447C-L001161](../../api/omarai.py#L1161) | 1161 | `"    \"\"\"Threaded HTTP server with a hard process-local ceiling on handler threads.\"\"\""` | — |
| [SRC-EEF2E6447C-L001162](../../api/omarai.py#L1162) | 1162 | `""` | — |
| [SRC-EEF2E6447C-L001163](../../api/omarai.py#L1163) | 1163 | `"    daemon_threads = True"` | — |
| [SRC-EEF2E6447C-L001164](../../api/omarai.py#L1164) | 1164 | `"    overload_response = ("` | — |
| [SRC-EEF2E6447C-L001165](../../api/omarai.py#L1165) | 1165 | `"        b\"HTTP/1.1 503 Service Unavailable\\r\\n\""` | — |
| [SRC-EEF2E6447C-L001166](../../api/omarai.py#L1166) | 1166 | `"        b\"Connection: close\\r\\n\""` | — |
| [SRC-EEF2E6447C-L001167](../../api/omarai.py#L1167) | 1167 | `"        b\"Retry-After: 5\\r\\n\""` | — |
| [SRC-EEF2E6447C-L001168](../../api/omarai.py#L1168) | 1168 | `"        b\"Content-Length: 0\\r\\n\\r\\n\""` | — |
| [SRC-EEF2E6447C-L001169](../../api/omarai.py#L1169) | 1169 | `"    )"` | — |
| [SRC-EEF2E6447C-L001170](../../api/omarai.py#L1170) | 1170 | `""` | — |
| [SRC-EEF2E6447C-L001171](../../api/omarai.py#L1171) | 1171 | `"    def __init__("` | — |
| [SRC-EEF2E6447C-L001172](../../api/omarai.py#L1172) | 1172 | `"        self,"` | — |
| [SRC-EEF2E6447C-L001173](../../api/omarai.py#L1173) | 1173 | `"        server_address,"` | — |
| [SRC-EEF2E6447C-L001174](../../api/omarai.py#L1174) | 1174 | `"        request_handler_class,"` | — |
| [SRC-EEF2E6447C-L001175](../../api/omarai.py#L1175) | 1175 | `"        bind_and_activate: bool = True,"` | — |
| [SRC-EEF2E6447C-L001176](../../api/omarai.py#L1176) | 1176 | `"        *,"` | — |
| [SRC-EEF2E6447C-L001177](../../api/omarai.py#L1177) | 1177 | `"        max_concurrent_connections: int \| None = None,"` | — |
| [SRC-EEF2E6447C-L001178](../../api/omarai.py#L1178) | 1178 | `"    ):"` | — |
| [SRC-EEF2E6447C-L001179](../../api/omarai.py#L1179) | 1179 | `"        super().__init__(server_address, request_handler_class, bind_and_activate)"` | — |
| [SRC-EEF2E6447C-L001180](../../api/omarai.py#L1180) | 1180 | `"        configured = ("` | — |
| [SRC-EEF2E6447C-L001181](../../api/omarai.py#L1181) | 1181 | `"            _configured_http_connection_limit()"` | — |
| [SRC-EEF2E6447C-L001182](../../api/omarai.py#L1182) | 1182 | `"            if max_concurrent_connections is None"` | — |
| [SRC-EEF2E6447C-L001183](../../api/omarai.py#L1183) | 1183 | `"            else int(max_concurrent_connections)"` | — |
| [SRC-EEF2E6447C-L001184](../../api/omarai.py#L1184) | 1184 | `"        )"` | — |
| [SRC-EEF2E6447C-L001185](../../api/omarai.py#L1185) | 1185 | `"        limit = max(1, min(configured, MAX_HTTP_CONNECTION_LIMIT))"` | — |
| [SRC-EEF2E6447C-L001186](../../api/omarai.py#L1186) | 1186 | `"        self.max_concurrent_connections = limit"` | — |
| [SRC-EEF2E6447C-L001187](../../api/omarai.py#L1187) | 1187 | `"        self._connection_slots = threading.BoundedSemaphore(limit)"` | — |
| [SRC-EEF2E6447C-L001188](../../api/omarai.py#L1188) | 1188 | `""` | — |
| [SRC-EEF2E6447C-L001189](../../api/omarai.py#L1189) | 1189 | `"    def process_request(self, request, client_address):"` | — |
| [SRC-EEF2E6447C-L001190](../../api/omarai.py#L1190) | 1190 | `"        \"\"\"Reject excess accepted sockets before creating another handler thread.\"\"\""` | — |
| [SRC-EEF2E6447C-L001191](../../api/omarai.py#L1191) | 1191 | `"        if not self._connection_slots.acquire(blocking=False):"` | — |
| [SRC-EEF2E6447C-L001192](../../api/omarai.py#L1192) | 1192 | `"            try:"` | — |
| [SRC-EEF2E6447C-L001193](../../api/omarai.py#L1193) | 1193 | `"                request.sendall(self.overload_response)"` | — |
| [SRC-EEF2E6447C-L001194](../../api/omarai.py#L1194) | 1194 | `"            except OSError:"` | — |
| [SRC-EEF2E6447C-L001195](../../api/omarai.py#L1195) | 1195 | `"                pass"` | — |
| [SRC-EEF2E6447C-L001196](../../api/omarai.py#L1196) | 1196 | `"            finally:"` | — |
| [SRC-EEF2E6447C-L001197](../../api/omarai.py#L1197) | 1197 | `"                self.shutdown_request(request)"` | — |
| [SRC-EEF2E6447C-L001198](../../api/omarai.py#L1198) | 1198 | `"            return"` | — |
| [SRC-EEF2E6447C-L001199](../../api/omarai.py#L1199) | 1199 | `"        try:"` | — |
| [SRC-EEF2E6447C-L001200](../../api/omarai.py#L1200) | 1200 | `"            super().process_request(request, client_address)"` | — |
| [SRC-EEF2E6447C-L001201](../../api/omarai.py#L1201) | 1201 | `"        except BaseException:"` | — |
| [SRC-EEF2E6447C-L001202](../../api/omarai.py#L1202) | 1202 | `"            # Thread creation can fail before a worker owns the reserved slot."` | — |
| [SRC-EEF2E6447C-L001203](../../api/omarai.py#L1203) | 1203 | `"            self._connection_slots.release()"` | — |
| [SRC-EEF2E6447C-L001204](../../api/omarai.py#L1204) | 1204 | `"            raise"` | — |
| [SRC-EEF2E6447C-L001205](../../api/omarai.py#L1205) | 1205 | `""` | — |
| [SRC-EEF2E6447C-L001206](../../api/omarai.py#L1206) | 1206 | `"    def process_request_thread(self, request, client_address):"` | — |
| [SRC-EEF2E6447C-L001207](../../api/omarai.py#L1207) | 1207 | `"        \"\"\"Return a slot after the handler has shut down the accepted socket.\"\"\""` | — |
| [SRC-EEF2E6447C-L001208](../../api/omarai.py#L1208) | 1208 | `"        try:"` | — |
| [SRC-EEF2E6447C-L001209](../../api/omarai.py#L1209) | 1209 | `"            super().process_request_thread(request, client_address)"` | — |
| [SRC-EEF2E6447C-L001210](../../api/omarai.py#L1210) | 1210 | `"        finally:"` | — |
| [SRC-EEF2E6447C-L001211](../../api/omarai.py#L1211) | 1211 | `"            self._connection_slots.release()"` | — |
| [SRC-EEF2E6447C-L001212](../../api/omarai.py#L1212) | 1212 | `""` | — |
| [SRC-EEF2E6447C-L001213](../../api/omarai.py#L1213) | 1213 | `""` | — |
| [SRC-EEF2E6447C-L001214](../../api/omarai.py#L1214) | 1214 | `"def serve(host=\"127.0.0.1\", port=8765):"` | — |
| [SRC-EEF2E6447C-L001215](../../api/omarai.py#L1215) | 1215 | `"    public_deployment = os.getenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"\").strip() == \"1\""` | — |
| [SRC-EEF2E6447C-L001216](../../api/omarai.py#L1216) | 1216 | `"    access_token = os.getenv(\"OMARAI_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-EEF2E6447C-L001217](../../api/omarai.py#L1217) | 1217 | `"    if host not in (\"127.0.0.1\", \"localhost\", \"::1\") and ("` | — |
| [SRC-EEF2E6447C-L001218](../../api/omarai.py#L1218) | 1218 | `"        not public_deployment or len(access_token) < 32"` | — |
| [SRC-EEF2E6447C-L001219](../../api/omarai.py#L1219) | 1219 | `"    ):"` | — |
| [SRC-EEF2E6447C-L001220](../../api/omarai.py#L1220) | 1220 | `"        raise ValueError("` | — |
| [SRC-EEF2E6447C-L001221](../../api/omarai.py#L1221) | 1221 | `"                \"Public binding requires OMARAI_PUBLIC_DEPLOYMENT=1 and \""` | — |
| [SRC-EEF2E6447C-L001222](../../api/omarai.py#L1222) | 1222 | `"                \"a private OMARAI_ACCESS_TOKEN of at least 32 characters.\""` | — |
| [SRC-EEF2E6447C-L001223](../../api/omarai.py#L1223) | 1223 | `"            )"` | — |
| [SRC-EEF2E6447C-L001224](../../api/omarai.py#L1224) | 1224 | `"    server = BoundedThreadingHTTPServer((host, port), Handler)"` | — |
| [SRC-EEF2E6447C-L001225](../../api/omarai.py#L1225) | 1225 | `"    print(f\"Omarai running at http://{host}:{port} — Ctrl+C to stop\")"` | — |
| [SRC-EEF2E6447C-L001226](../../api/omarai.py#L1226) | 1226 | `"    print(\"Web research agent: /   \|   Lead workspace: /leads\")"` | — |
| [SRC-EEF2E6447C-L001227](../../api/omarai.py#L1227) | 1227 | `"    try:"` | — |
| [SRC-EEF2E6447C-L001228](../../api/omarai.py#L1228) | 1228 | `"        server.serve_forever()"` | — |
| [SRC-EEF2E6447C-L001229](../../api/omarai.py#L1229) | 1229 | `"    except KeyboardInterrupt:"` | — |
| [SRC-EEF2E6447C-L001230](../../api/omarai.py#L1230) | 1230 | `"        pass"` | — |
| [SRC-EEF2E6447C-L001231](../../api/omarai.py#L1231) | 1231 | `"    finally:"` | — |
| [SRC-EEF2E6447C-L001232](../../api/omarai.py#L1232) | 1232 | `"        server.server_close()"` | — |
| [SRC-EEF2E6447C-L001233](../../api/omarai.py#L1233) | 1233 | `""` | — |
| [SRC-EEF2E6447C-L001234](../../api/omarai.py#L1234) | 1234 | `""` | — |
| [SRC-EEF2E6447C-L001235](../../api/omarai.py#L1235) | 1235 | `"if __name__ == \"__main__\":"` | — |
| [SRC-EEF2E6447C-L001236](../../api/omarai.py#L1236) | 1236 | `"    serve()"` | — |
## وثائق ونصوص

### FILE-65AAF94960 — [artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-65AAF94960-L000001](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L1) | 1 | `"# تقرير قبول الاستضافة — Omarai"` | — |
| [SRC-65AAF94960-L000002](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L2) | 2 | `"**التاريخ:** 27 أكتوبر 2026  "` | — |
| [SRC-65AAF94960-L000003](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L3) | 3 | `"**المضيف:** https://omarai-dec45.containers.snapdeploy.app/  "` | — |
| [SRC-65AAF94960-L000004](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L4) | 4 | `"**جلسة المتصفح:** [TinyFish run af7ebb42-e032-4321-8454-a3628432f53d](https://agent.tinyfish.ai/runs/af7ebb42-e032-4321-8454-a3628432f53d)  "` | — |
| [SRC-65AAF94960-L000005](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L5) | 5 | `"**التصنيف:** PARTIAL / BLOCKED — لا إعلان جاهزية."` | — |
| [SRC-65AAF94960-L000006](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L6) | 6 | `""` | — |
| [SRC-65AAF94960-L000007](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L7) | 7 | `"## الملخص التنفيذي"` | — |
| [SRC-65AAF94960-L000008](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L8) | 8 | `"أُعيد اختبار الواجهة في ملف المتصفح المخصص، دون خزنة أسرار ودون إدخال أو كشف أي رمز. الصفحة حملت، لكن حقل رمز الوصول في **ملف المتصفح الاختباري فارغ**. لذلك فشل سؤال «ما عاصمة مصر؟» قبل تنفيذ البحث. لم تُختبر بعد مصادر البحث الحية ولا البحث الحديث ولا البحث المعمق فعليًا."` | — |
| [SRC-65AAF94960-L000009](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L9) | 9 | `""` | — |
| [SRC-65AAF94960-L000010](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L10) | 10 | `"هذه النتيجة لا تثبت أن الرمز المخزن في متصفح المستخدم غير صحيح؛ إنها تثبت فقط أن رمزًا لم يكن متاحًا في ملف المتصفح الاختباري. التخزين المحلي في المتصفحات/الملفات منفصل."` | — |
| [SRC-65AAF94960-L000011](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L11) | 11 | `""` | — |
| [SRC-65AAF94960-L000012](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L12) | 12 | `"## أدلة القبول"` | — |
| [SRC-65AAF94960-L000013](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L13) | 13 | `"\| الفحص \| النتيجة \| الحالة \|"` | — |
| [SRC-65AAF94960-L000014](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L14) | 14 | `"\|---\|---\|---\|"` | — |
| [SRC-65AAF94960-L000015](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L15) | 15 | `"\| تحميل الصفحة الرئيسية \| ظهرت واجهة Omarai \| VERIFIED \|"` | — |
| [SRC-65AAF94960-L000016](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L16) | 16 | ``"\| وجود رمز وصول في ملف المتصفح الاختباري \| الحقل `accessToken` فارغ ويعرض «أدخل رمز الاستضافة الذي أنشأته» \| VERIFIED \|"`` | — |
| [SRC-65AAF94960-L000017](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L17) | 17 | `"\| سؤال «ما عاصمة مصر؟» في الوضع الافتراضي الظاهر «بحث معمّق» \| فشل قبل استرجاع إجابة أو مصادر \| FAILED / BLOCKED \|"` | — |
| [SRC-65AAF94960-L000018](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L18) | 18 | `"\| نص الخطأ \| «رمز الوصول غير صحيح أو غير محفوظ. راجع رمز التطبيق المستضاف.» \| VERIFIED \|"` | — |
| [SRC-65AAF94960-L000019](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L19) | 19 | `"\| البحث عن الموقع الرسمي لـ OpenAI في «الأحدث الآن» \| لم يُنفذ بسبب حاجز المصادقة \| NOT_RUN \|"` | — |
| [SRC-65AAF94960-L000020](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L20) | 20 | `"\| سؤال بحث معمّق إضافي \| لم يُنفذ بسبب حاجز المصادقة \| NOT_RUN \|"` | — |
| [SRC-65AAF94960-L000021](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L21) | 21 | ``"\| `GET /api/health` \| `ok=true` \| VERIFIED — لكنه لا يثبت صلاحية البحث الحي \|"`` | — |
| [SRC-65AAF94960-L000022](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L22) | 22 | ``"\| هوية البناء \| `build.sha=unknown`, `sha_status=unknown`, `sha_source=unknown` \| BLOCKED / NOT VERIFIED \|"`` | — |
| [SRC-65AAF94960-L000023](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L23) | 23 | ``"\| فحص الشبكة الحي \| `live_network_checks_performed=false` \| NOT_RUN \|"`` | — |
| [SRC-65AAF94960-L000024](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L24) | 24 | `""` | — |
| [SRC-65AAF94960-L000025](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L25) | 25 | `"## تفسير الاستجابة الصحية"` | — |
| [SRC-65AAF94960-L000026](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L26) | 26 | ``"يصرّح رد الصحة بأن `web_search_ready` يعني أن الاعتماديات قابلة للاستيراد، وليس أن مزود البحث متصل؛ وأن `language_model_configured` يعني وجود بيانات اعتماد، وليس نجاح إكمال طلب. ويعرض مصادر منها DuckDuckGo HTML وBing RSS وGoogle News RSS كمدعومة، بينما يعرض DeepSeek/Brave/Tavily على أنها مشروطة الإعداد، ويعرض OpenRouter server-side live web search على أنه معطل. هذه أوصاف إعداد وليست اختبارات اتصال."`` | — |
| [SRC-65AAF94960-L000027](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L27) | 27 | `""` | — |
| [SRC-65AAF94960-L000028](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L28) | 28 | `"## السبب والحالة"` | — |
| [SRC-65AAF94960-L000029](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L29) | 29 | `"- **OMR-LIVE-004 — PARTIAL / BLOCKED:** اختبار الطلبات المحمية يتوقف عند المصادقة. السبب الدقيق وراء عدم وجود الرمز في ملف المتصفح الاختباري هو اختلاف سياق التخزين، لا دليل على فساد الرمز نفسه."` | — |
| [SRC-65AAF94960-L000030](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L30) | 30 | ``"- **OMR-LIVE-005 — CODE/CI FIXED_AND_TESTED; HOST_CONFIGURATION_PENDING:** إصلاح Dockerfile الذي يقرأ `PUBLIC_OMARAI_BUILD_SHA` موجود في #98، لكن المضيف ما زال يعرض SHA مجهولًا. يلزم تعيين متغير الإصدار العام إلى SHA الكامل المعتمد وإعادة البناء/النشر من مالك الاستضافة، ثم التحقق من التطابق. لا تضع أي أسرار في متغير الإصدار."`` | — |
| [SRC-65AAF94960-L000031](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L31) | 31 | ``"- لا يجوز اعتبار نجاح CI أو `ok=true` إثباتًا لصحة البحث أو الإجابات في الإنتاج."`` | — |
| [SRC-65AAF94960-L000032](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L32) | 32 | `""` | — |
| [SRC-65AAF94960-L000033](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L33) | 33 | `"## الخطوات اللازمة للإغلاق"` | — |
| [SRC-65AAF94960-L000034](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L34) | 34 | `"1. افتح جلسة إعداد ملف المتصفح الآمنة من الرابط الذي يوفره ChatGPT، على الموقع المستضاف."` | — |
| [SRC-65AAF94960-L000035](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L35) | 35 | `"2. أدخل رمز الوصول بنفسك في حقل التطبيق، واحفظه داخل ملف المتصفح الاختباري. **لا ترسل الرمز في المحادثة ولا تضعه في سجل GitHub.**"` | — |
| [SRC-65AAF94960-L000036](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L36) | 36 | `"3. أعد اختبار سؤال معرفي بسيط، ثم بحث الموقع الرسمي في وضع «الأحدث الآن»، ثم بحث معمّق؛ سجل حالة الطلب وروابط المصادر الفعلية."` | — |
| [SRC-65AAF94960-L000037](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L37) | 37 | ``"4. راجع إعدادات SnapDeploy لتعيين `PUBLIC_OMARAI_BUILD_SHA` إلى SHA الكامل النهائي المعتمد، ثم أعد البناء/النشر عبر مسار النشر المعتاد، وبعدها تحقق أن `/api/health` يعرض SHA المطابق. هذا التقرير لا يغير إعدادات المضيف ولا ينشر."`` | — |
| [SRC-65AAF94960-L000038](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L38) | 38 | `"5. لا تعلن القبول النهائي حتى تنجح هذه الاختبارات وتوثق مصادر حقيقية قابلة للفتح، أو تسجل كل عائق متبقٍ بوضوح."` | — |
| [SRC-65AAF94960-L000039](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L39) | 39 | `""` | — |
| [SRC-65AAF94960-L000040](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L40) | 40 | `"## حدود العمل"` | — |
| [SRC-65AAF94960-L000041](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L41) | 41 | `"لم تُقرأ أو تُكشف أسرار، ولم تُغير إعدادات الاستضافة، ولم يُنفذ نشر أو إجراء مدفوع. تم استخدام المتصفح للقراءة والاختبار فقط."` | — |
## واجهة سطر الأوامر

### FILE-14C6359E27 — [cli/__init__.py](../../cli/__init__.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-14C6359E27-L000001](../../cli/__init__.py#L1) | 1 | `"\"\"\"Omarai command-line package.\"\"\""` | — |
## واجهة سطر الأوامر

### FILE-9C97DF51AC — [cli/omarai.py](../../cli/omarai.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-9C97DF51AC-L000001](../../cli/omarai.py#L1) | 1 | `"\"\"\"Command-line interface for Omarai.\"\"\""` | — |
| [SRC-9C97DF51AC-L000002](../../cli/omarai.py#L2) | 2 | `"import argparse"` | — |
| [SRC-9C97DF51AC-L000003](../../cli/omarai.py#L3) | 3 | `"import json"` | — |
| [SRC-9C97DF51AC-L000004](../../cli/omarai.py#L4) | 4 | `""` | — |
| [SRC-9C97DF51AC-L000005](../../cli/omarai.py#L5) | 5 | `"from agents.omarai import LeadStore, analyze"` | — |
| [SRC-9C97DF51AC-L000006](../../cli/omarai.py#L6) | 6 | `"from api.omarai import serve"` | — |
| [SRC-9C97DF51AC-L000007](../../cli/omarai.py#L7) | 7 | `""` | — |
| [SRC-9C97DF51AC-L000008](../../cli/omarai.py#L8) | 8 | `""` | — |
| [SRC-9C97DF51AC-L000009](../../cli/omarai.py#L9) | 9 | `"def main():"` | — |
| [SRC-9C97DF51AC-L000010](../../cli/omarai.py#L10) | 10 | `"    parser=argparse.ArgumentParser(prog=\"omarai\",description=\"Arabic lead-intent helper\")"` | — |
| [SRC-9C97DF51AC-L000011](../../cli/omarai.py#L11) | 11 | `"    sub=parser.add_subparsers(dest=\"command\",required=True)"` | — |
| [SRC-9C97DF51AC-L000012](../../cli/omarai.py#L12) | 12 | `"    p=sub.add_parser(\"analyze\")"` | — |
| [SRC-9C97DF51AC-L000013](../../cli/omarai.py#L13) | 13 | `"    p.add_argument(\"--text\",required=True)"` | — |
| [SRC-9C97DF51AC-L000014](../../cli/omarai.py#L14) | 14 | `"    p.add_argument(\"--product\",default=\"\")"` | — |
| [SRC-9C97DF51AC-L000015](../../cli/omarai.py#L15) | 15 | `"    p.add_argument(\"--location\",default=\"\")"` | — |
| [SRC-9C97DF51AC-L000016](../../cli/omarai.py#L16) | 16 | `"    p=sub.add_parser(\"serve\")"` | — |
| [SRC-9C97DF51AC-L000017](../../cli/omarai.py#L17) | 17 | `"    p.add_argument(\"--host\",default=\"127.0.0.1\")"` | — |
| [SRC-9C97DF51AC-L000018](../../cli/omarai.py#L18) | 18 | `"    p.add_argument(\"--port\",type=int,default=8765)"` | — |
| [SRC-9C97DF51AC-L000019](../../cli/omarai.py#L19) | 19 | `"    p=sub.add_parser(\"import-csv\")"` | — |
| [SRC-9C97DF51AC-L000020](../../cli/omarai.py#L20) | 20 | `"    p.add_argument(\"--file\",required=True)"` | — |
| [SRC-9C97DF51AC-L000021](../../cli/omarai.py#L21) | 21 | `"    p=sub.add_parser(\"list\")"` | — |
| [SRC-9C97DF51AC-L000022](../../cli/omarai.py#L22) | 22 | `"    p.add_argument(\"--limit\",type=int,default=100)"` | — |
| [SRC-9C97DF51AC-L000023](../../cli/omarai.py#L23) | 23 | `"    p.add_argument(\"--status\")"` | — |
| [SRC-9C97DF51AC-L000024](../../cli/omarai.py#L24) | 24 | `"    p=sub.add_parser(\"export-csv\")"` | — |
| [SRC-9C97DF51AC-L000025](../../cli/omarai.py#L25) | 25 | `"    p.add_argument(\"--file\",required=True)"` | — |
| [SRC-9C97DF51AC-L000026](../../cli/omarai.py#L26) | 26 | `"    args=parser.parse_args()"` | — |
| [SRC-9C97DF51AC-L000027](../../cli/omarai.py#L27) | 27 | `"    if args.command==\"analyze\":"` | — |
| [SRC-9C97DF51AC-L000028](../../cli/omarai.py#L28) | 28 | `"        result=analyze(args.text,[x.strip() for x in args.product.split(\",\") if x.strip()],[x.strip() for x in args.location.split(\",\") if x.strip()])"` | — |
| [SRC-9C97DF51AC-L000029](../../cli/omarai.py#L29) | 29 | `"        print(json.dumps(result,ensure_ascii=False,indent=2))"` | — |
| [SRC-9C97DF51AC-L000030](../../cli/omarai.py#L30) | 30 | `"        return"` | — |
| [SRC-9C97DF51AC-L000031](../../cli/omarai.py#L31) | 31 | `"    store=LeadStore()"` | — |
| [SRC-9C97DF51AC-L000032](../../cli/omarai.py#L32) | 32 | `"    if args.command==\"serve\":"` | — |
| [SRC-9C97DF51AC-L000033](../../cli/omarai.py#L33) | 33 | `"        serve(args.host,args.port)"` | — |
| [SRC-9C97DF51AC-L000034](../../cli/omarai.py#L34) | 34 | `"    elif args.command==\"import-csv\":"` | — |
| [SRC-9C97DF51AC-L000035](../../cli/omarai.py#L35) | 35 | `"        print(json.dumps(store.import_csv(args.file),ensure_ascii=False,indent=2))"` | — |
| [SRC-9C97DF51AC-L000036](../../cli/omarai.py#L36) | 36 | `"    elif args.command==\"list\":"` | — |
| [SRC-9C97DF51AC-L000037](../../cli/omarai.py#L37) | 37 | `"        print(json.dumps(store.list(args.status,args.limit),ensure_ascii=False,indent=2))"` | — |
| [SRC-9C97DF51AC-L000038](../../cli/omarai.py#L38) | 38 | `"    elif args.command==\"export-csv\":"` | — |
| [SRC-9C97DF51AC-L000039](../../cli/omarai.py#L39) | 39 | `"        print(f\"Exported {store.export_csv(args.file)} leads to {args.file}\")"` | — |
| [SRC-9C97DF51AC-L000040](../../cli/omarai.py#L40) | 40 | `"if __name__==\"__main__\":"` | — |
| [SRC-9C97DF51AC-L000041](../../cli/omarai.py#L41) | 41 | `"    main()"` | — |
## إعدادات وتشغيل

### FILE-DD2C0EB6EA — [Dockerfile](../../Dockerfile#L1)

- النوع: **Dockerfile**
- نطاق الفهرسة: جرد الملف + أسماء إعدادات عامة إن وجدت

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-DD2C0EB6EA-L000001](../../Dockerfile#L1) | 1 | `"FROM python:3.12-slim"` | — |
| [SRC-DD2C0EB6EA-L000002](../../Dockerfile#L2) | 2 | `""` | — |
| [SRC-DD2C0EB6EA-L000003](../../Dockerfile#L3) | 3 | `"ARG OMARAI_BUILD_SHA=unknown"` | — |
| [SRC-DD2C0EB6EA-L000004](../../Dockerfile#L4) | 4 | `"ARG PUBLIC_OMARAI_BUILD_SHA=unknown"` | — |
| [SRC-DD2C0EB6EA-L000005](../../Dockerfile#L5) | 5 | `"ENV PYTHONDONTWRITEBYTECODE=1 \\"` | — |
