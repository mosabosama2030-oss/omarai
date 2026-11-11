# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **006**
- سجلات الأسطر: **800**
- النطاق: SRC-FDEEAFDFCA-L000028 إلى SRC-59CF4B7DE8-L000515
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-FDEEAFDFCA — [agents/request_budget.py](../../agents/request_budget.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
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
| [SRC-59CF4B7DE8-L000182](../../agents/research.py#L182) | 182 | `"        if not segment:"` | — |
| [SRC-59CF4B7DE8-L000183](../../agents/research.py#L183) | 183 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000184](../../agents/research.py#L184) | 184 | `"        normalized_segment = re.sub(r\"[\\u064B-\\u065F\\u0670]\", \"\", segment)"` | — |
| [SRC-59CF4B7DE8-L000185](../../agents/research.py#L185) | 185 | `"        normalized_segment = _normalize_arabic(normalized_segment).casefold()"` | — |
| [SRC-59CF4B7DE8-L000186](../../agents/research.py#L186) | 186 | `"        if ("` | — |
| [SRC-59CF4B7DE8-L000187](../../agents/research.py#L187) | 187 | `"            _SEARCH_CITATION_META_START_RE.search(normalized_segment)"` | — |
| [SRC-59CF4B7DE8-L000188](../../agents/research.py#L188) | 188 | `"            or _SEARCH_UNCERTAINTY_META_START_RE.search(normalized_segment)"` | — |
| [SRC-59CF4B7DE8-L000189](../../agents/research.py#L189) | 189 | `"            or _SEARCH_FACTS_INFERENCE_META_ONLY_RE.search(normalized_segment)"` | — |
| [SRC-59CF4B7DE8-L000190](../../agents/research.py#L190) | 190 | `"        ):"` | — |
| [SRC-59CF4B7DE8-L000191](../../agents/research.py#L191) | 191 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000192](../../agents/research.py#L192) | 192 | `"        if _SEARCH_META_START_RE.search(normalized_segment):"` | — |
| [SRC-59CF4B7DE8-L000193](../../agents/research.py#L193) | 193 | `"            # Keep a concrete topic when a \"use multiple sources\" directive"` | — |
| [SRC-59CF4B7DE8-L000194](../../agents/research.py#L194) | 194 | `"            # introduces the subject, but discard standalone formatting clauses."` | — |
| [SRC-59CF4B7DE8-L000195](../../agents/research.py#L195) | 195 | `"            preserved = _SEARCH_TOPIC_PRESERVING_META_PREFIX_RE.sub(\"\", segment, count=1).strip()"` | — |
| [SRC-59CF4B7DE8-L000196](../../agents/research.py#L196) | 196 | `"            if not preserved:"` | — |
| [SRC-59CF4B7DE8-L000197](../../agents/research.py#L197) | 197 | `"                continue"` | — |
| [SRC-59CF4B7DE8-L000198](../../agents/research.py#L198) | 198 | `"            if preserved == segment:"` | — |
| [SRC-59CF4B7DE8-L000199](../../agents/research.py#L199) | 199 | `"                continue"` | — |
| [SRC-59CF4B7DE8-L000200](../../agents/research.py#L200) | 200 | `"            segment = preserved"` | — |
| [SRC-59CF4B7DE8-L000201](../../agents/research.py#L201) | 201 | `"        segment = _SEARCH_META_TAIL_RE.sub(\"\", segment).strip()"` | — |
| [SRC-59CF4B7DE8-L000202](../../agents/research.py#L202) | 202 | `"        segment = _SEARCH_LEADING_ACTION_RE.sub(\"\", segment).strip()"` | — |
| [SRC-59CF4B7DE8-L000203](../../agents/research.py#L203) | 203 | `"        if segment:"` | — |
| [SRC-59CF4B7DE8-L000204](../../agents/research.py#L204) | 204 | `"            useful.append(segment)"` | — |
| [SRC-59CF4B7DE8-L000205](../../agents/research.py#L205) | 205 | `"    result = re.sub(r\"\\s+\", \" \", \" \".join(useful)).strip(\" \\t\\r\\n,،;؛\")"` | — |
| [SRC-59CF4B7DE8-L000206](../../agents/research.py#L206) | 206 | `"    if not result:"` | — |
| [SRC-59CF4B7DE8-L000207](../../agents/research.py#L207) | 207 | `"        return \"\""` | — |
| [SRC-59CF4B7DE8-L000208](../../agents/research.py#L208) | 208 | `"    try:"` | — |
| [SRC-59CF4B7DE8-L000209](../../agents/research.py#L209) | 209 | `"        max_chars = max(2, min(int(limit), MAX_QUERY_CHARS))"` | — |
| [SRC-59CF4B7DE8-L000210](../../agents/research.py#L210) | 210 | `"    except (TypeError, ValueError, OverflowError):"` | — |
| [SRC-59CF4B7DE8-L000211](../../agents/research.py#L211) | 211 | `"        max_chars = MAX_QUERY_CHARS"` | — |
| [SRC-59CF4B7DE8-L000212](../../agents/research.py#L212) | 212 | `"    if len(result) > max_chars:"` | — |
| [SRC-59CF4B7DE8-L000213](../../agents/research.py#L213) | 213 | `"        shortened = result[:max_chars]"` | — |
| [SRC-59CF4B7DE8-L000214](../../agents/research.py#L214) | 214 | `"        result = shortened.rsplit(\" \", 1)[0] if \" \" in shortened else shortened"` | — |
| [SRC-59CF4B7DE8-L000215](../../agents/research.py#L215) | 215 | `"    return result"` | — |
| [SRC-59CF4B7DE8-L000216](../../agents/research.py#L216) | 216 | `""` | — |
| [SRC-59CF4B7DE8-L000217](../../agents/research.py#L217) | 217 | `""` | — |
| [SRC-59CF4B7DE8-L000218](../../agents/research.py#L218) | 218 | `"_ARABIC_RE = re.compile(r\"[؀-ۿ]\")"` | — |
| [SRC-59CF4B7DE8-L000219](../../agents/research.py#L219) | 219 | `""` | — |
| [SRC-59CF4B7DE8-L000220](../../agents/research.py#L220) | 220 | `""` | — |
| [SRC-59CF4B7DE8-L000221](../../agents/research.py#L221) | 221 | `"def _normalize_arabic(text: str) -> str:"` | — |
| [SRC-59CF4B7DE8-L000222](../../agents/research.py#L222) | 222 | `"    if not text:"` | — |
| [SRC-59CF4B7DE8-L000223](../../agents/research.py#L223) | 223 | `"        return \"\""` | — |
| [SRC-59CF4B7DE8-L000224](../../agents/research.py#L224) | 224 | `"    return (text.replace(\"\\u0623\", \"\\u0627\")"` | — |
| [SRC-59CF4B7DE8-L000225](../../agents/research.py#L225) | 225 | `"                .replace(\"\\u0625\", \"\\u0627\")"` | — |
| [SRC-59CF4B7DE8-L000226](../../agents/research.py#L226) | 226 | `"                .replace(\"\\u0622\", \"\\u0627\")"` | — |
| [SRC-59CF4B7DE8-L000227](../../agents/research.py#L227) | 227 | `"                .replace(\"\\u0629\", \"\\u0647\")"` | — |
| [SRC-59CF4B7DE8-L000228](../../agents/research.py#L228) | 228 | `"                .replace(\"\\u0649\", \"\\u064a\"))"` | — |
| [SRC-59CF4B7DE8-L000229](../../agents/research.py#L229) | 229 | `""` | — |
| [SRC-59CF4B7DE8-L000230](../../agents/research.py#L230) | 230 | `""` | — |
| [SRC-59CF4B7DE8-L000231](../../agents/research.py#L231) | 231 | `"def _contains_any(text: str, terms: tuple) -> bool:"` | — |
| [SRC-59CF4B7DE8-L000232](../../agents/research.py#L232) | 232 | `"    if not text:"` | — |
| [SRC-59CF4B7DE8-L000233](../../agents/research.py#L233) | 233 | `"        return False"` | — |
| [SRC-59CF4B7DE8-L000234](../../agents/research.py#L234) | 234 | `"    haystack = _normalize_arabic(text.casefold())"` | — |
| [SRC-59CF4B7DE8-L000235](../../agents/research.py#L235) | 235 | `"    for term in terms:"` | — |
| [SRC-59CF4B7DE8-L000236](../../agents/research.py#L236) | 236 | `"        if not term:"` | — |
| [SRC-59CF4B7DE8-L000237](../../agents/research.py#L237) | 237 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000238](../../agents/research.py#L238) | 238 | `"        t = _normalize_arabic(term.casefold())"` | — |
| [SRC-59CF4B7DE8-L000239](../../agents/research.py#L239) | 239 | `"        if _ARABIC_RE.search(t):"` | — |
| [SRC-59CF4B7DE8-L000240](../../agents/research.py#L240) | 240 | `"            if t in haystack:"` | — |
| [SRC-59CF4B7DE8-L000241](../../agents/research.py#L241) | 241 | `"                return True"` | — |
| [SRC-59CF4B7DE8-L000242](../../agents/research.py#L242) | 242 | `"        else:"` | — |
| [SRC-59CF4B7DE8-L000243](../../agents/research.py#L243) | 243 | `"            pat = r\"(?<![a-zA-Z0-9])\" + re.escape(t) + r\"(?![a-zA-Z0-9])\""` | — |
| [SRC-59CF4B7DE8-L000244](../../agents/research.py#L244) | 244 | `"            if re.search(pat, haystack):"` | — |
| [SRC-59CF4B7DE8-L000245](../../agents/research.py#L245) | 245 | `"                return True"` | — |
| [SRC-59CF4B7DE8-L000246](../../agents/research.py#L246) | 246 | `"    return False"` | — |
| [SRC-59CF4B7DE8-L000247](../../agents/research.py#L247) | 247 | `""` | — |
| [SRC-59CF4B7DE8-L000248](../../agents/research.py#L248) | 248 | `""` | — |
| [SRC-59CF4B7DE8-L000249](../../agents/research.py#L249) | 249 | `"def detect_social_focus(question: str, history: list[dict[str, str]] \| None = None) -> bool:"` | — |
| [SRC-59CF4B7DE8-L000250](../../agents/research.py#L250) | 250 | `"    context = question + \" \" + \" \".join("` | — |
| [SRC-59CF4B7DE8-L000251](../../agents/research.py#L251) | 251 | `"        item.get(\"content\", \"\") for item in (history or [])[-4:]"` | — |
| [SRC-59CF4B7DE8-L000252](../../agents/research.py#L252) | 252 | `"    )"` | — |
| [SRC-59CF4B7DE8-L000253](../../agents/research.py#L253) | 253 | `"    return _contains_any(context, _SOCIAL_TERMS)"` | — |
| [SRC-59CF4B7DE8-L000254](../../agents/research.py#L254) | 254 | `""` | — |
| [SRC-59CF4B7DE8-L000255](../../agents/research.py#L255) | 255 | `""` | — |
| [SRC-59CF4B7DE8-L000256](../../agents/research.py#L256) | 256 | `"def detect_freshness(question: str) -> bool:"` | — |
| [SRC-59CF4B7DE8-L000257](../../agents/research.py#L257) | 257 | `"    return _contains_any(question, _FRESH_TERMS)"` | — |
| [SRC-59CF4B7DE8-L000258](../../agents/research.py#L258) | 258 | `""` | — |
| [SRC-59CF4B7DE8-L000259](../../agents/research.py#L259) | 259 | `""` | — |
| [SRC-59CF4B7DE8-L000260](../../agents/research.py#L260) | 260 | `"def detect_depth(question: str) -> str:"` | — |
| [SRC-59CF4B7DE8-L000261](../../agents/research.py#L261) | 261 | `"    return \"deep\" if _contains_any(question, _DEEP_TERMS) else \"standard\""` | — |
| [SRC-59CF4B7DE8-L000262](../../agents/research.py#L262) | 262 | `""` | — |
| [SRC-59CF4B7DE8-L000263](../../agents/research.py#L263) | 263 | `""` | — |
| [SRC-59CF4B7DE8-L000264](../../agents/research.py#L264) | 264 | `"def extract_question_coverage_targets(question: str) -> list[str]:"` | — |
| [SRC-59CF4B7DE8-L000265](../../agents/research.py#L265) | 265 | `"    \"\"\"Extract explicit multi-part requirements; this is a heuristic, not semantic parsing.\"\"\""` | — |
| [SRC-59CF4B7DE8-L000266](../../agents/research.py#L266) | 266 | `"    if not isinstance(question, str) or not question.strip():"` | — |
| [SRC-59CF4B7DE8-L000267](../../agents/research.py#L267) | 267 | `"        return []"` | — |
| [SRC-59CF4B7DE8-L000268](../../agents/research.py#L268) | 268 | `"    text = question.strip()[:4000]"` | — |
| [SRC-59CF4B7DE8-L000269](../../agents/research.py#L269) | 269 | `"    marker = re.compile("` | — |
| [SRC-59CF4B7DE8-L000270](../../agents/research.py#L270) | 270 | `"        r\"(?:من\\s+حيث\|من\\s+ناحية\|من\\s+الناحية\|فيما\\s+يتعلق\\s+ب\|فيما\\s+يخص\|\""` | — |
| [SRC-59CF4B7DE8-L000271](../../agents/research.py#L271) | 271 | `"        r\"من\\s+منظور\|in\\s+terms\\s+of\|with\\s+respect\\s+to\|\""` | — |
| [SRC-59CF4B7DE8-L000272](../../agents/research.py#L272) | 272 | `"        r\"from\\s+the\\s+perspective\\s+of\|based\\s+on\\s+the\\s+following\\s+criteria)\""` | — |
| [SRC-59CF4B7DE8-L000273](../../agents/research.py#L273) | 273 | `"        r\"\\s*(.+?)(?=[؟?!.؛;\\n]\|$)\","` | — |
| [SRC-59CF4B7DE8-L000274](../../agents/research.py#L274) | 274 | `"        flags=re.IGNORECASE,"` | — |
| [SRC-59CF4B7DE8-L000275](../../agents/research.py#L275) | 275 | `"    )"` | — |
| [SRC-59CF4B7DE8-L000276](../../agents/research.py#L276) | 276 | `"    match = marker.search(text)"` | — |
| [SRC-59CF4B7DE8-L000277](../../agents/research.py#L277) | 277 | `"    if match:"` | — |
| [SRC-59CF4B7DE8-L000278](../../agents/research.py#L278) | 278 | `"        raw = match.group(1)"` | — |
| [SRC-59CF4B7DE8-L000279](../../agents/research.py#L279) | 279 | `"        raw = re.split("` | — |
| [SRC-59CF4B7DE8-L000280](../../agents/research.py#L280) | 280 | `"            r\"(?:،\|,\|؛\|;)\\s*(?:و?اذكر\|و?وضح\|بيّن\|اشرح\|and\\s+(?:explain\|note\|discuss))\\b\","` | — |
| [SRC-59CF4B7DE8-L000281](../../agents/research.py#L281) | 281 | `"            raw,"` | — |
| [SRC-59CF4B7DE8-L000282](../../agents/research.py#L282) | 282 | `"            maxsplit=1,"` | — |
| [SRC-59CF4B7DE8-L000283](../../agents/research.py#L283) | 283 | `"            flags=re.IGNORECASE,"` | — |
| [SRC-59CF4B7DE8-L000284](../../agents/research.py#L284) | 284 | `"        )[0]"` | — |
| [SRC-59CF4B7DE8-L000285](../../agents/research.py#L285) | 285 | `"        pieces = re.split("` | — |
| [SRC-59CF4B7DE8-L000286](../../agents/research.py#L286) | 286 | `"            r\"\\s*(?:،\|,\|؛\|;\|/)\\s*\|\""` | — |
| [SRC-59CF4B7DE8-L000287](../../agents/research.py#L287) | 287 | `"            r\"\\s+\\band\\b\\s+\|\\s+\\bas well as\\b\\s+\|\""` | — |
| [SRC-59CF4B7DE8-L000288](../../agents/research.py#L288) | 288 | `"            r\"\\s+و(?=ال\|[ء-ي])\","` | — |
| [SRC-59CF4B7DE8-L000289](../../agents/research.py#L289) | 289 | `"            raw,"` | — |
| [SRC-59CF4B7DE8-L000290](../../agents/research.py#L290) | 290 | `"            flags=re.IGNORECASE,"` | — |
| [SRC-59CF4B7DE8-L000291](../../agents/research.py#L291) | 291 | `"        )"` | — |
| [SRC-59CF4B7DE8-L000292](../../agents/research.py#L292) | 292 | `"    else:"` | — |
| [SRC-59CF4B7DE8-L000293](../../agents/research.py#L293) | 293 | `"        question_parts = ["` | — |
| [SRC-59CF4B7DE8-L000294](../../agents/research.py#L294) | 294 | `"            part.strip(\" \\t\\r\\n-•\")"` | — |
| [SRC-59CF4B7DE8-L000295](../../agents/research.py#L295) | 295 | `"            for part in re.split(r\"[؟?]+\", text)"` | — |
| [SRC-59CF4B7DE8-L000296](../../agents/research.py#L296) | 296 | `"            if len(part.strip(\" \\t\\r\\n-•\")) >= 4"` | — |
| [SRC-59CF4B7DE8-L000297](../../agents/research.py#L297) | 297 | `"        ]"` | — |
| [SRC-59CF4B7DE8-L000298](../../agents/research.py#L298) | 298 | `"        pieces = question_parts if len(question_parts) > 1 else []"` | — |
| [SRC-59CF4B7DE8-L000299](../../agents/research.py#L299) | 299 | `"        # Reuse the shared aspect vocabulary for compound factual questions that do"` | — |
| [SRC-59CF4B7DE8-L000300](../../agents/research.py#L300) | 300 | `"        # not use a formal comparison marker (e.g. capital + population). This is"` | — |
| [SRC-59CF4B7DE8-L000301](../../agents/research.py#L301) | 301 | `"        # deterministic decomposition only; it does not claim semantic verification."` | — |
| [SRC-59CF4B7DE8-L000302](../../agents/research.py#L302) | 302 | `"        if not pieces:"` | — |
| [SRC-59CF4B7DE8-L000303](../../agents/research.py#L303) | 303 | `"            pieces = extract_aspects(text)"` | — |
| [SRC-59CF4B7DE8-L000304](../../agents/research.py#L304) | 304 | `""` | — |
| [SRC-59CF4B7DE8-L000305](../../agents/research.py#L305) | 305 | `"    targets: list[str] = []"` | — |
| [SRC-59CF4B7DE8-L000306](../../agents/research.py#L306) | 306 | `"    seen: set[str] = set()"` | — |
| [SRC-59CF4B7DE8-L000307](../../agents/research.py#L307) | 307 | `"    for piece in pieces:"` | — |
| [SRC-59CF4B7DE8-L000308](../../agents/research.py#L308) | 308 | `"        target = re.sub(r\"^[\\s:،,؛;/.!?\\-–—]+\|[\\s:،,؛;/.!?\\-–—]+$\", \"\", piece).strip()"` | — |
| [SRC-59CF4B7DE8-L000309](../../agents/research.py#L309) | 309 | `"        target = re.sub(r\"^(?:و\\s*)\", \"\", target).strip()"` | — |
| [SRC-59CF4B7DE8-L000310](../../agents/research.py#L310) | 310 | `"        if len(target) < 2:"` | — |
| [SRC-59CF4B7DE8-L000311](../../agents/research.py#L311) | 311 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000312](../../agents/research.py#L312) | 312 | `"        if len(target) > 120:"` | — |
| [SRC-59CF4B7DE8-L000313](../../agents/research.py#L313) | 313 | `"            target = target[:120].rsplit(\" \", 1)[0].strip()"` | — |
| [SRC-59CF4B7DE8-L000314](../../agents/research.py#L314) | 314 | `"        key = _normalize_arabic(compact_search_query(target)).casefold()"` | — |
| [SRC-59CF4B7DE8-L000315](../../agents/research.py#L315) | 315 | `"        if key and key not in seen:"` | — |
| [SRC-59CF4B7DE8-L000316](../../agents/research.py#L316) | 316 | `"            seen.add(key)"` | — |
| [SRC-59CF4B7DE8-L000317](../../agents/research.py#L317) | 317 | `"            targets.append(target)"` | — |
| [SRC-59CF4B7DE8-L000318](../../agents/research.py#L318) | 318 | `"        if len(targets) >= MAX_PLAN_QUERIES:"` | — |
| [SRC-59CF4B7DE8-L000319](../../agents/research.py#L319) | 319 | `"            break"` | — |
| [SRC-59CF4B7DE8-L000320](../../agents/research.py#L320) | 320 | `"    return targets"` | — |
| [SRC-59CF4B7DE8-L000321](../../agents/research.py#L321) | 321 | `""` | — |
| [SRC-59CF4B7DE8-L000322](../../agents/research.py#L322) | 322 | `""` | — |
| [SRC-59CF4B7DE8-L000323](../../agents/research.py#L323) | 323 | `"def build_requirement_queries("` | — |
| [SRC-59CF4B7DE8-L000324](../../agents/research.py#L324) | 324 | `"    base_query: str, targets: list[str] \| None = None"` | — |
| [SRC-59CF4B7DE8-L000325](../../agents/research.py#L325) | 325 | `") -> list[dict[str, str]]:"` | — |
| [SRC-59CF4B7DE8-L000326](../../agents/research.py#L326) | 326 | `"    \"\"\"Create one bounded search query per explicit requirement.\"\"\""` | — |
| [SRC-59CF4B7DE8-L000327](../../agents/research.py#L327) | 327 | `"    if not base_query or not targets:"` | — |
| [SRC-59CF4B7DE8-L000328](../../agents/research.py#L328) | 328 | `"        return []"` | — |
| [SRC-59CF4B7DE8-L000329](../../agents/research.py#L329) | 329 | `"    output: list[dict[str, str]] = []"` | — |
| [SRC-59CF4B7DE8-L000330](../../agents/research.py#L330) | 330 | `"    for target in targets[:MAX_PLAN_QUERIES]:"` | — |
| [SRC-59CF4B7DE8-L000331](../../agents/research.py#L331) | 331 | `"        if not isinstance(target, str) or not target.strip():"` | — |
| [SRC-59CF4B7DE8-L000332](../../agents/research.py#L332) | 332 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000333](../../agents/research.py#L333) | 333 | `"        clean_target = target.strip()[:120]"` | — |
| [SRC-59CF4B7DE8-L000334](../../agents/research.py#L334) | 334 | `"        prefix_limit = max("` | — |
| [SRC-59CF4B7DE8-L000335](../../agents/research.py#L335) | 335 | `"            80,"` | — |
| [SRC-59CF4B7DE8-L000336](../../agents/research.py#L336) | 336 | `"            MAX_QUERY_CHARS - min(len(clean_target), MAX_QUERY_CHARS - 80) - 1,"` | — |
| [SRC-59CF4B7DE8-L000337](../../agents/research.py#L337) | 337 | `"        )"` | — |
| [SRC-59CF4B7DE8-L000338](../../agents/research.py#L338) | 338 | `"        prefix = compact_search_query(base_query, limit=prefix_limit)"` | — |
| [SRC-59CF4B7DE8-L000339](../../agents/research.py#L339) | 339 | `"        query = compact_search_query("` | — |
| [SRC-59CF4B7DE8-L000340](../../agents/research.py#L340) | 340 | `"            f\"{prefix} {clean_target}\", limit=MAX_QUERY_CHARS"` | — |
| [SRC-59CF4B7DE8-L000341](../../agents/research.py#L341) | 341 | `"        )"` | — |
| [SRC-59CF4B7DE8-L000342](../../agents/research.py#L342) | 342 | `"        if query:"` | — |
| [SRC-59CF4B7DE8-L000343](../../agents/research.py#L343) | 343 | `"            output.append({\"target\": clean_target, \"query\": query})"` | — |
| [SRC-59CF4B7DE8-L000344](../../agents/research.py#L344) | 344 | `"    return output"` | — |
| [SRC-59CF4B7DE8-L000345](../../agents/research.py#L345) | 345 | `""` | — |
| [SRC-59CF4B7DE8-L000346](../../agents/research.py#L346) | 346 | `""` | — |
| [SRC-59CF4B7DE8-L000347](../../agents/research.py#L347) | 347 | `""` | — |
| [SRC-59CF4B7DE8-L000348](../../agents/research.py#L348) | 348 | `"def mentioned_social_platforms(text: str) -> list[str]:"` | — |
| [SRC-59CF4B7DE8-L000349](../../agents/research.py#L349) | 349 | `"    rules = ("` | — |
| [SRC-59CF4B7DE8-L000350](../../agents/research.py#L350) | 350 | `"        (\"reddit\", (\"reddit\", \"ريديت\")),"` | — |
| [SRC-59CF4B7DE8-L000351](../../agents/research.py#L351) | 351 | `"        (\"youtube\", (\"youtube\", \"يوتيوب\")),"` | — |
| [SRC-59CF4B7DE8-L000352](../../agents/research.py#L352) | 352 | `"        (\"facebook\", (\"facebook\", \"فيسبوك\", \"فيس بوك\")),"` | — |
| [SRC-59CF4B7DE8-L000353](../../agents/research.py#L353) | 353 | `"        (\"instagram\", (\"instagram\", \"انستجرام\", \"إنستجرام\")),"` | — |
| [SRC-59CF4B7DE8-L000354](../../agents/research.py#L354) | 354 | `"        (\"x\", (\"x.com\", \"twitter\", \"تويتر\", \"اكس\", \"إكس\")),"` | — |
| [SRC-59CF4B7DE8-L000355](../../agents/research.py#L355) | 355 | `"        (\"tiktok\", (\"tiktok\", \"تيك توك\")),"` | — |
| [SRC-59CF4B7DE8-L000356](../../agents/research.py#L356) | 356 | `"        (\"linkedin\", (\"linkedin\", \"لينكدان\", \"لينكدإن\")),"` | — |
| [SRC-59CF4B7DE8-L000357](../../agents/research.py#L357) | 357 | `"        (\"threads\", (\"threads\", \"ثريدز\")),"` | — |
| [SRC-59CF4B7DE8-L000358](../../agents/research.py#L358) | 358 | `"        (\"bluesky\", (\"bluesky\", \"بلو سكاي\")),"` | — |
| [SRC-59CF4B7DE8-L000359](../../agents/research.py#L359) | 359 | `"    )"` | — |
| [SRC-59CF4B7DE8-L000360](../../agents/research.py#L360) | 360 | `"    low = text.casefold()"` | — |
| [SRC-59CF4B7DE8-L000361](../../agents/research.py#L361) | 361 | `"    return [name for name, aliases in rules if any(alias.casefold() in low for alias in aliases)]"` | — |
| [SRC-59CF4B7DE8-L000362](../../agents/research.py#L362) | 362 | `""` | — |
| [SRC-59CF4B7DE8-L000363](../../agents/research.py#L363) | 363 | `""` | — |
| [SRC-59CF4B7DE8-L000364](../../agents/research.py#L364) | 364 | `"def _attach_task_understanding("` | — |
| [SRC-59CF4B7DE8-L000365](../../agents/research.py#L365) | 365 | `"    plan: dict[str, Any],"` | — |
| [SRC-59CF4B7DE8-L000366](../../agents/research.py#L366) | 366 | `"    question: str,"` | — |
| [SRC-59CF4B7DE8-L000367](../../agents/research.py#L367) | 367 | `"    *,"` | — |
| [SRC-59CF4B7DE8-L000368](../../agents/research.py#L368) | 368 | `"    intent_route: str = \"deterministic_fallback\","` | — |
| [SRC-59CF4B7DE8-L000369](../../agents/research.py#L369) | 369 | `"    mode: str = \"auto\","` | — |
| [SRC-59CF4B7DE8-L000370](../../agents/research.py#L370) | 370 | `") -> dict[str, Any]:"` | — |
| [SRC-59CF4B7DE8-L000371](../../agents/research.py#L371) | 371 | `"    \"\"\"Attach deterministic task interpretation and a bounded strategy matrix.\"\"\""` | — |
| [SRC-59CF4B7DE8-L000372](../../agents/research.py#L372) | 372 | `"    result = dict(plan)"` | — |
| [SRC-59CF4B7DE8-L000373](../../agents/research.py#L373) | 373 | `"    from agents.research_pipeline import build_research_pipeline"` | — |
| [SRC-59CF4B7DE8-L000374](../../agents/research.py#L374) | 374 | `""` | — |
| [SRC-59CF4B7DE8-L000375](../../agents/research.py#L375) | 375 | `"    pipeline = build_research_pipeline("` | — |
| [SRC-59CF4B7DE8-L000376](../../agents/research.py#L376) | 376 | `"        question,"` | — |
| [SRC-59CF4B7DE8-L000377](../../agents/research.py#L377) | 377 | `"        result,"` | — |
| [SRC-59CF4B7DE8-L000378](../../agents/research.py#L378) | 378 | `"        mode=mode,"` | — |
| [SRC-59CF4B7DE8-L000379](../../agents/research.py#L379) | 379 | `"        intent_route=intent_route,"` | — |
| [SRC-59CF4B7DE8-L000380](../../agents/research.py#L380) | 380 | `"        compact_fn=compact_search_query,"` | — |
| [SRC-59CF4B7DE8-L000381](../../agents/research.py#L381) | 381 | `"    )"` | — |
| [SRC-59CF4B7DE8-L000382](../../agents/research.py#L382) | 382 | `"    # Planning remains declarative here; the request runner enforces its own"` | — |
| [SRC-59CF4B7DE8-L000383](../../agents/research.py#L383) | 383 | `"    # selected-mode and budget limits before executing the bounded query matrix."` | — |
| [SRC-59CF4B7DE8-L000384](../../agents/research.py#L384) | 384 | `"    result[\"task_spec\"] = pipeline[\"task_spec\"]"` | — |
| [SRC-59CF4B7DE8-L000385](../../agents/research.py#L385) | 385 | `"    result[\"query_strategy_matrix\"] = pipeline[\"query_strategy_matrix\"]"` | — |
| [SRC-59CF4B7DE8-L000386](../../agents/research.py#L386) | 386 | `"    result[\"research_pipeline\"] = {"` | — |
| [SRC-59CF4B7DE8-L000387](../../agents/research.py#L387) | 387 | `"        \"aspects\": pipeline[\"aspects\"],"` | — |
| [SRC-59CF4B7DE8-L000388](../../agents/research.py#L388) | 388 | `"        \"stages\": pipeline[\"stages\"],"` | — |
| [SRC-59CF4B7DE8-L000389](../../agents/research.py#L389) | 389 | `"    }"` | — |
| [SRC-59CF4B7DE8-L000390](../../agents/research.py#L390) | 390 | `"    return result"` | — |
| [SRC-59CF4B7DE8-L000391](../../agents/research.py#L391) | 391 | `""` | — |
| [SRC-59CF4B7DE8-L000392](../../agents/research.py#L392) | 392 | `""` | — |
| [SRC-59CF4B7DE8-L000393](../../agents/research.py#L393) | 393 | `"def fallback_plan("` | — |
| [SRC-59CF4B7DE8-L000394](../../agents/research.py#L394) | 394 | `"    question: str, history: list[dict[str, str]] \| None = None"` | — |
| [SRC-59CF4B7DE8-L000395](../../agents/research.py#L395) | 395 | `") -> dict[str, Any]:"` | — |
| [SRC-59CF4B7DE8-L000396](../../agents/research.py#L396) | 396 | `"    \"\"\"Build a small but varied plan when no model planner is configured or parsing fails.\"\"\""` | — |
| [SRC-59CF4B7DE8-L000397](../../agents/research.py#L397) | 397 | `"    contextual_question = resolve_followup_query(question, history)"` | — |
| [SRC-59CF4B7DE8-L000398](../../agents/research.py#L398) | 398 | `"    direct_urls = extract_urls(question)"` | — |
| [SRC-59CF4B7DE8-L000399](../../agents/research.py#L399) | 399 | `"    base = compact_search_query(contextual_question)"` | — |
| [SRC-59CF4B7DE8-L000400](../../agents/research.py#L400) | 400 | `"    coverage_targets = extract_question_coverage_targets(question)"` | — |
| [SRC-59CF4B7DE8-L000401](../../agents/research.py#L401) | 401 | `"    requirement_queries = build_requirement_queries(base, coverage_targets)"` | — |
| [SRC-59CF4B7DE8-L000402](../../agents/research.py#L402) | 402 | `"    social_focus = detect_social_focus(contextual_question)"` | — |
| [SRC-59CF4B7DE8-L000403](../../agents/research.py#L403) | 403 | `"    fresh = detect_freshness(contextual_question)"` | — |
| [SRC-59CF4B7DE8-L000404](../../agents/research.py#L404) | 404 | `"    detected_depth = detect_depth(contextual_question)"` | — |
| [SRC-59CF4B7DE8-L000405](../../agents/research.py#L405) | 405 | `"    deep = detected_depth == \"deep\""` | — |
| [SRC-59CF4B7DE8-L000406](../../agents/research.py#L406) | 406 | `"    platforms = mentioned_social_platforms(contextual_question)"` | — |
| [SRC-59CF4B7DE8-L000407](../../agents/research.py#L407) | 407 | `"    queries: list[str] = [base] if base else []"` | — |
| [SRC-59CF4B7DE8-L000408](../../agents/research.py#L408) | 408 | `""` | — |
| [SRC-59CF4B7DE8-L000409](../../agents/research.py#L409) | 409 | `"    if fresh and base:"` | — |
| [SRC-59CF4B7DE8-L000410](../../agents/research.py#L410) | 410 | `"        queries.append(compact_search_query(base + \" أحدث مستجدات آخر الأخبار\"))"` | — |
| [SRC-59CF4B7DE8-L000411](../../agents/research.py#L411) | 411 | `"    if base and _contains_any(contextual_question, (\"قارن\", \"مقارنة\", \"compare\", \"versus\", \"vs\", \"الفرق بين\")):"` | — |
| [SRC-59CF4B7DE8-L000412](../../agents/research.py#L412) | 412 | `"        queries.append(compact_search_query(base + \" مقارنة مراجعات مميزات عيوب\"))"` | — |
| [SRC-59CF4B7DE8-L000413](../../agents/research.py#L413) | 413 | `""` | — |
| [SRC-59CF4B7DE8-L000414](../../agents/research.py#L414) | 414 | `"    if social_focus and base:"` | — |
| [SRC-59CF4B7DE8-L000415](../../agents/research.py#L415) | 415 | `"        selected = platforms or [\"facebook\", \"instagram\", \"reddit\"]"` | — |
| [SRC-59CF4B7DE8-L000416](../../agents/research.py#L416) | 416 | `"        for platform in selected[:3]:"` | — |
| [SRC-59CF4B7DE8-L000417](../../agents/research.py#L417) | 417 | `"            domain = SOCIAL_DOMAINS[platform]"` | — |
| [SRC-59CF4B7DE8-L000418](../../agents/research.py#L418) | 418 | `"            site_query = compact_search_query(f\"site:{domain} {base}\")"` | — |
| [SRC-59CF4B7DE8-L000419](../../agents/research.py#L419) | 419 | `"            if site_query not in queries:"` | — |
| [SRC-59CF4B7DE8-L000420](../../agents/research.py#L420) | 420 | `"                queries.append(site_query)"` | — |
| [SRC-59CF4B7DE8-L000421](../../agents/research.py#L421) | 421 | `""` | — |
| [SRC-59CF4B7DE8-L000422](../../agents/research.py#L422) | 422 | `"    if deep and base and not social_focus and len(queries) < MAX_PLAN_QUERIES:"` | — |
| [SRC-59CF4B7DE8-L000423](../../agents/research.py#L423) | 423 | `"        queries.append(compact_search_query(base + \" مصادر موثوقة تقارير إحصاءات\"))"` | — |
| [SRC-59CF4B7DE8-L000424](../../agents/research.py#L424) | 424 | `""` | — |
| [SRC-59CF4B7DE8-L000425](../../agents/research.py#L425) | 425 | `"    if requirement_queries:"` | — |
| [SRC-59CF4B7DE8-L000426](../../agents/research.py#L426) | 426 | `"        optional_queries = list(queries)"` | — |
| [SRC-59CF4B7DE8-L000427](../../agents/research.py#L427) | 427 | `"        if len(requirement_queries) >= MAX_PLAN_QUERIES:"` | — |
| [SRC-59CF4B7DE8-L000428](../../agents/research.py#L428) | 428 | `"            priority_queries = [item[\"query\"] for item in requirement_queries]"` | — |
| [SRC-59CF4B7DE8-L000429](../../agents/research.py#L429) | 429 | `"        else:"` | — |
| [SRC-59CF4B7DE8-L000430](../../agents/research.py#L430) | 430 | `"            priority_queries = ([base] if base else []) + ["` | — |
| [SRC-59CF4B7DE8-L000431](../../agents/research.py#L431) | 431 | `"                item[\"query\"] for item in requirement_queries"` | — |
| [SRC-59CF4B7DE8-L000432](../../agents/research.py#L432) | 432 | `"            ]"` | — |
| [SRC-59CF4B7DE8-L000433](../../agents/research.py#L433) | 433 | `"        priority_seen = {item.casefold() for item in priority_queries}"` | — |
| [SRC-59CF4B7DE8-L000434](../../agents/research.py#L434) | 434 | `"        queries = priority_queries + ["` | — |
| [SRC-59CF4B7DE8-L000435](../../agents/research.py#L435) | 435 | `"            item for item in optional_queries if item.casefold() not in priority_seen"` | — |
| [SRC-59CF4B7DE8-L000436](../../agents/research.py#L436) | 436 | `"        ]"` | — |
| [SRC-59CF4B7DE8-L000437](../../agents/research.py#L437) | 437 | `""` | — |
| [SRC-59CF4B7DE8-L000438](../../agents/research.py#L438) | 438 | `"    unique: list[str] = []"` | — |
| [SRC-59CF4B7DE8-L000439](../../agents/research.py#L439) | 439 | `"    seen: set[str] = set()"` | — |
| [SRC-59CF4B7DE8-L000440](../../agents/research.py#L440) | 440 | `"    for query in queries:"` | — |
| [SRC-59CF4B7DE8-L000441](../../agents/research.py#L441) | 441 | `"        value = compact_search_query(query)"` | — |
| [SRC-59CF4B7DE8-L000442](../../agents/research.py#L442) | 442 | `"        key = value.casefold()"` | — |
| [SRC-59CF4B7DE8-L000443](../../agents/research.py#L443) | 443 | `"        if value and key not in seen:"` | — |
| [SRC-59CF4B7DE8-L000444](../../agents/research.py#L444) | 444 | `"            unique.append(value)"` | — |
| [SRC-59CF4B7DE8-L000445](../../agents/research.py#L445) | 445 | `"            seen.add(key)"` | — |
| [SRC-59CF4B7DE8-L000446](../../agents/research.py#L446) | 446 | `"        if len(unique) >= MAX_PLAN_QUERIES:"` | — |
| [SRC-59CF4B7DE8-L000447](../../agents/research.py#L447) | 447 | `"            break"` | — |
| [SRC-59CF4B7DE8-L000448](../../agents/research.py#L448) | 448 | `""` | — |
| [SRC-59CF4B7DE8-L000449](../../agents/research.py#L449) | 449 | `"    base_plan = {"` | — |
| [SRC-59CF4B7DE8-L000450](../../agents/research.py#L450) | 450 | `"        \"queries\": unique or ([base] if base else []),"` | — |
| [SRC-59CF4B7DE8-L000451](../../agents/research.py#L451) | 451 | `"        \"coverage_targets\": coverage_targets,"` | — |
| [SRC-59CF4B7DE8-L000452](../../agents/research.py#L452) | 452 | `"        \"requirement_queries\": requirement_queries,"` | — |
| [SRC-59CF4B7DE8-L000453](../../agents/research.py#L453) | 453 | `"        \"direct_urls\": direct_urls,"` | — |
| [SRC-59CF4B7DE8-L000454](../../agents/research.py#L454) | 454 | `"        \"social_focus\": social_focus,"` | — |
| [SRC-59CF4B7DE8-L000455](../../agents/research.py#L455) | 455 | `"        \"freshness\": \"current\" if fresh else \"any\","` | — |
| [SRC-59CF4B7DE8-L000456](../../agents/research.py#L456) | 456 | `"        \"depth\": detected_depth,"` | — |
| [SRC-59CF4B7DE8-L000457](../../agents/research.py#L457) | 457 | `"        \"platforms\": platforms,"` | — |
| [SRC-59CF4B7DE8-L000458](../../agents/research.py#L458) | 458 | `"        \"planning_method\": \"deterministic_fallback\","` | — |
| [SRC-59CF4B7DE8-L000459](../../agents/research.py#L459) | 459 | `"    }"` | — |
| [SRC-59CF4B7DE8-L000460](../../agents/research.py#L460) | 460 | `"    return _attach_task_understanding("` | — |
| [SRC-59CF4B7DE8-L000461](../../agents/research.py#L461) | 461 | `"        base_plan, contextual_question, intent_route=\"deterministic_fallback\""` | — |
| [SRC-59CF4B7DE8-L000462](../../agents/research.py#L462) | 462 | `"    )"` | — |
| [SRC-59CF4B7DE8-L000463](../../agents/research.py#L463) | 463 | `""` | — |
| [SRC-59CF4B7DE8-L000464](../../agents/research.py#L464) | 464 | `""` | — |
| [SRC-59CF4B7DE8-L000465](../../agents/research.py#L465) | 465 | `"def validate_plan("` | — |
| [SRC-59CF4B7DE8-L000466](../../agents/research.py#L466) | 466 | `"    candidate: Any, question: str, history: list[dict[str, str]] \| None = None"` | — |
| [SRC-59CF4B7DE8-L000467](../../agents/research.py#L467) | 467 | `") -> dict[str, Any]:"` | — |
| [SRC-59CF4B7DE8-L000468](../../agents/research.py#L468) | 468 | `"    fallback = fallback_plan(question, history)"` | — |
| [SRC-59CF4B7DE8-L000469](../../agents/research.py#L469) | 469 | `"    if not isinstance(candidate, dict):"` | — |
| [SRC-59CF4B7DE8-L000470](../../agents/research.py#L470) | 470 | `"        return fallback"` | — |
| [SRC-59CF4B7DE8-L000471](../../agents/research.py#L471) | 471 | `"    raw_queries = candidate.get(\"queries\", [])"` | — |
| [SRC-59CF4B7DE8-L000472](../../agents/research.py#L472) | 472 | `"    if not isinstance(raw_queries, list):"` | — |
| [SRC-59CF4B7DE8-L000473](../../agents/research.py#L473) | 473 | `"        return fallback"` | — |
| [SRC-59CF4B7DE8-L000474](../../agents/research.py#L474) | 474 | `"    queries: list[str] = []"` | — |
| [SRC-59CF4B7DE8-L000475](../../agents/research.py#L475) | 475 | `"    seen: set[str] = set()"` | — |
| [SRC-59CF4B7DE8-L000476](../../agents/research.py#L476) | 476 | `"    for item in raw_queries:"` | — |
| [SRC-59CF4B7DE8-L000477](../../agents/research.py#L477) | 477 | `"        query = compact_search_query(item)"` | — |
| [SRC-59CF4B7DE8-L000478](../../agents/research.py#L478) | 478 | `"        # Never accept prompt-like multi-line payloads as search-query instructions."` | — |
| [SRC-59CF4B7DE8-L000479](../../agents/research.py#L479) | 479 | `"        query = query.replace(\"\\n\", \" \").replace(\"\\r\", \" \")"` | — |
| [SRC-59CF4B7DE8-L000480](../../agents/research.py#L480) | 480 | `"        if len(query) < 2:"` | — |
| [SRC-59CF4B7DE8-L000481](../../agents/research.py#L481) | 481 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000482](../../agents/research.py#L482) | 482 | `"        if query.casefold() not in seen:"` | — |
| [SRC-59CF4B7DE8-L000483](../../agents/research.py#L483) | 483 | `"            seen.add(query.casefold())"` | — |
| [SRC-59CF4B7DE8-L000484](../../agents/research.py#L484) | 484 | `"            queries.append(query)"` | — |
| [SRC-59CF4B7DE8-L000485](../../agents/research.py#L485) | 485 | `"        if len(queries) >= MAX_PLAN_QUERIES:"` | — |
| [SRC-59CF4B7DE8-L000486](../../agents/research.py#L486) | 486 | `"            break"` | — |
| [SRC-59CF4B7DE8-L000487](../../agents/research.py#L487) | 487 | `"    if not queries:"` | — |
| [SRC-59CF4B7DE8-L000488](../../agents/research.py#L488) | 488 | `"        return fallback"` | — |
| [SRC-59CF4B7DE8-L000489](../../agents/research.py#L489) | 489 | `"    base = fallback_plan(question, history)"` | — |
| [SRC-59CF4B7DE8-L000490](../../agents/research.py#L490) | 490 | `"    coverage_targets = list(base.get(\"coverage_targets\") or [])"` | — |
| [SRC-59CF4B7DE8-L000491](../../agents/research.py#L491) | 491 | `"    requirement_queries = list(base.get(\"requirement_queries\") or [])"` | — |
| [SRC-59CF4B7DE8-L000492](../../agents/research.py#L492) | 492 | `"    if requirement_queries:"` | — |
| [SRC-59CF4B7DE8-L000493](../../agents/research.py#L493) | 493 | `"        required_prefix: list[str] = []"` | — |
| [SRC-59CF4B7DE8-L000494](../../agents/research.py#L494) | 494 | `"        if len(requirement_queries) < MAX_PLAN_QUERIES and base.get(\"queries\"):"` | — |
| [SRC-59CF4B7DE8-L000495](../../agents/research.py#L495) | 495 | `"            required_prefix.append(base[\"queries\"][0])"` | — |
| [SRC-59CF4B7DE8-L000496](../../agents/research.py#L496) | 496 | `"        required_prefix.extend("` | — |
| [SRC-59CF4B7DE8-L000497](../../agents/research.py#L497) | 497 | `"            item[\"query\"] for item in requirement_queries if item.get(\"query\")"` | — |
| [SRC-59CF4B7DE8-L000498](../../agents/research.py#L498) | 498 | `"        )"` | — |
| [SRC-59CF4B7DE8-L000499](../../agents/research.py#L499) | 499 | `"        queries = list(dict.fromkeys(required_prefix + queries))[:MAX_PLAN_QUERIES]"` | — |
| [SRC-59CF4B7DE8-L000500](../../agents/research.py#L500) | 500 | `"    platforms = candidate.get(\"platforms\")"` | — |
| [SRC-59CF4B7DE8-L000501](../../agents/research.py#L501) | 501 | `"    if not isinstance(platforms, list):"` | — |
| [SRC-59CF4B7DE8-L000502](../../agents/research.py#L502) | 502 | `"        platforms = base[\"platforms\"]"` | — |
| [SRC-59CF4B7DE8-L000503](../../agents/research.py#L503) | 503 | `"    safe_platforms = [p for p in platforms if isinstance(p, str) and p in SOCIAL_DOMAINS]"` | — |
| [SRC-59CF4B7DE8-L000504](../../agents/research.py#L504) | 504 | `"    validated_plan = {"` | — |
| [SRC-59CF4B7DE8-L000505](../../agents/research.py#L505) | 505 | `"        \"queries\": queries,"` | — |
| [SRC-59CF4B7DE8-L000506](../../agents/research.py#L506) | 506 | `"        \"coverage_targets\": coverage_targets,"` | — |
| [SRC-59CF4B7DE8-L000507](../../agents/research.py#L507) | 507 | `"        \"requirement_queries\": requirement_queries,"` | — |
| [SRC-59CF4B7DE8-L000508](../../agents/research.py#L508) | 508 | `"        \"direct_urls\": fallback[\"direct_urls\"],"` | — |
| [SRC-59CF4B7DE8-L000509](../../agents/research.py#L509) | 509 | `"        \"social_focus\": bool(candidate.get(\"social_focus\", base[\"social_focus\"])),"` | — |
| [SRC-59CF4B7DE8-L000510](../../agents/research.py#L510) | 510 | `"        \"freshness\": \"current\" if candidate.get(\"freshness\") == \"current\" else base[\"freshness\"],"` | — |
| [SRC-59CF4B7DE8-L000511](../../agents/research.py#L511) | 511 | `"        \"depth\": \"deep\" if candidate.get(\"depth\") == \"deep\" else base[\"depth\"],"` | — |
| [SRC-59CF4B7DE8-L000512](../../agents/research.py#L512) | 512 | `"        \"platforms\": list(dict.fromkeys(safe_platforms))[:5],"` | — |
| [SRC-59CF4B7DE8-L000513](../../agents/research.py#L513) | 513 | `"        \"planning_method\": \"language_model\","` | — |
| [SRC-59CF4B7DE8-L000514](../../agents/research.py#L514) | 514 | `"    }"` | — |
| [SRC-59CF4B7DE8-L000515](../../agents/research.py#L515) | 515 | `"    return _attach_task_understanding("` | — |
