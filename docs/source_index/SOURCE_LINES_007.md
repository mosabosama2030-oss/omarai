# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **007**
- سجلات الأسطر: **800**
- النطاق: SRC-8D00DCEC0D-L000257 إلى SRC-686F71AA50-L000267
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-8D00DCEC0D — [agents/sales_domain.py](../../agents/sales_domain.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-8D00DCEC0D-L000257](../../agents/sales_domain.py#L257) | 257 | `"        object.__setattr__("` | — |
| [SRC-8D00DCEC0D-L000258](../../agents/sales_domain.py#L258) | 258 | `"            self,"` | — |
| [SRC-8D00DCEC0D-L000259](../../agents/sales_domain.py#L259) | 259 | `"            \"problems_solved\","` | — |
| [SRC-8D00DCEC0D-L000260](../../agents/sales_domain.py#L260) | 260 | `"            _clean_terms(self.problems_solved, field_name=\"problems_solved\"),"` | — |
| [SRC-8D00DCEC0D-L000261](../../agents/sales_domain.py#L261) | 261 | `"        )"` | — |
| [SRC-8D00DCEC0D-L000262](../../agents/sales_domain.py#L262) | 262 | `"        if self.category_path:"` | — |
| [SRC-8D00DCEC0D-L000263](../../agents/sales_domain.py#L263) | 263 | `"            object.__setattr__("` | — |
| [SRC-8D00DCEC0D-L000264](../../agents/sales_domain.py#L264) | 264 | `"                self,"` | — |
| [SRC-8D00DCEC0D-L000265](../../agents/sales_domain.py#L265) | 265 | `"                \"category_path\","` | — |
| [SRC-8D00DCEC0D-L000266](../../agents/sales_domain.py#L266) | 266 | `"                _clean_path(self.category_path, field_name=\"category_path\"),"` | — |
| [SRC-8D00DCEC0D-L000267](../../agents/sales_domain.py#L267) | 267 | `"            )"` | — |
| [SRC-8D00DCEC0D-L000268](../../agents/sales_domain.py#L268) | 268 | `"        if not all(isinstance(item, ProductFact) for item in self.facts):"` | — |
| [SRC-8D00DCEC0D-L000269](../../agents/sales_domain.py#L269) | 269 | `"            raise TypeError(\"facts must contain ProductFact instances\")"` | — |
| [SRC-8D00DCEC0D-L000270](../../agents/sales_domain.py#L270) | 270 | `"        if len(self.facts) > MAX_TERM_COUNT:"` | — |
| [SRC-8D00DCEC0D-L000271](../../agents/sales_domain.py#L271) | 271 | `"            raise ValueError(f\"facts exceeds {MAX_TERM_COUNT} items\")"` | — |
| [SRC-8D00DCEC0D-L000272](../../agents/sales_domain.py#L272) | 272 | `""` | — |
| [SRC-8D00DCEC0D-L000273](../../agents/sales_domain.py#L273) | 273 | `"    def matching_terms(self, text: str) -> tuple[str, ...]:"` | — |
| [SRC-8D00DCEC0D-L000274](../../agents/sales_domain.py#L274) | 274 | `"        \"\"\"Return explicitly configured product terms mentioned in text."` | — |
| [SRC-8D00DCEC0D-L000275](../../agents/sales_domain.py#L275) | 275 | `""` | — |
| [SRC-8D00DCEC0D-L000276](../../agents/sales_domain.py#L276) | 276 | `"        A mention is not a demand signal and does not establish a buyer or product fit."` | — |
| [SRC-8D00DCEC0D-L000277](../../agents/sales_domain.py#L277) | 277 | `"        \"\"\""` | — |
| [SRC-8D00DCEC0D-L000278](../../agents/sales_domain.py#L278) | 278 | `"        terms = (self.name, *self.aliases)"` | — |
| [SRC-8D00DCEC0D-L000279](../../agents/sales_domain.py#L279) | 279 | `"        return tuple(term for term in terms if _contains_phrase(text, term))"` | — |
| [SRC-8D00DCEC0D-L000280](../../agents/sales_domain.py#L280) | 280 | `""` | — |
| [SRC-8D00DCEC0D-L000281](../../agents/sales_domain.py#L281) | 281 | `"    def to_dict(self) -> dict[str, object]:"` | — |
| [SRC-8D00DCEC0D-L000282](../../agents/sales_domain.py#L282) | 282 | `"        return {"` | — |
| [SRC-8D00DCEC0D-L000283](../../agents/sales_domain.py#L283) | 283 | `"            \"name\": self.name,"` | — |
| [SRC-8D00DCEC0D-L000284](../../agents/sales_domain.py#L284) | 284 | `"            \"aliases\": list(self.aliases),"` | — |
| [SRC-8D00DCEC0D-L000285](../../agents/sales_domain.py#L285) | 285 | `"            \"category_path\": list(self.category_path),"` | — |
| [SRC-8D00DCEC0D-L000286](../../agents/sales_domain.py#L286) | 286 | `"            \"use_cases\": list(self.use_cases),"` | — |
| [SRC-8D00DCEC0D-L000287](../../agents/sales_domain.py#L287) | 287 | `"            \"problems_solved\": list(self.problems_solved),"` | — |
| [SRC-8D00DCEC0D-L000288](../../agents/sales_domain.py#L288) | 288 | `"            \"facts\": [item.to_dict() for item in self.facts],"` | — |
| [SRC-8D00DCEC0D-L000289](../../agents/sales_domain.py#L289) | 289 | `"        }"` | — |
| [SRC-8D00DCEC0D-L000290](../../agents/sales_domain.py#L290) | 290 | `""` | — |
| [SRC-8D00DCEC0D-L000291](../../agents/sales_domain.py#L291) | 291 | `""` | — |
| [SRC-8D00DCEC0D-L000292](../../agents/sales_domain.py#L292) | 292 | `"@dataclass(frozen=True, slots=True)"` | — |
| [SRC-8D00DCEC0D-L000293](../../agents/sales_domain.py#L293) | 293 | `"class MarketProfile:"` | — |
| [SRC-8D00DCEC0D-L000294](../../agents/sales_domain.py#L294) | 294 | `"    \"\"\"Target-market constraints; matching an ICP is not evidence of purchase intent.\"\"\""` | — |
| [SRC-8D00DCEC0D-L000295](../../agents/sales_domain.py#L295) | 295 | `""` | — |
| [SRC-8D00DCEC0D-L000296](../../agents/sales_domain.py#L296) | 296 | `"    locations: tuple[str, ...] = ()"` | — |
| [SRC-8D00DCEC0D-L000297](../../agents/sales_domain.py#L297) | 297 | `"    industries: tuple[str, ...] = ()"` | — |
| [SRC-8D00DCEC0D-L000298](../../agents/sales_domain.py#L298) | 298 | `"    customer_types: tuple[str, ...] = ()"` | — |
| [SRC-8D00DCEC0D-L000299](../../agents/sales_domain.py#L299) | 299 | `"    decision_roles: tuple[str, ...] = ()"` | — |
| [SRC-8D00DCEC0D-L000300](../../agents/sales_domain.py#L300) | 300 | `"    exclusions: tuple[str, ...] = ()"` | — |
| [SRC-8D00DCEC0D-L000301](../../agents/sales_domain.py#L301) | 301 | `""` | — |
| [SRC-8D00DCEC0D-L000302](../../agents/sales_domain.py#L302) | 302 | `"    def __post_init__(self) -> None:"` | — |
| [SRC-8D00DCEC0D-L000303](../../agents/sales_domain.py#L303) | 303 | `"        for name in (\"locations\", \"industries\", \"customer_types\", \"decision_roles\", \"exclusions\"):"` | — |
| [SRC-8D00DCEC0D-L000304](../../agents/sales_domain.py#L304) | 304 | `"            object.__setattr__("` | — |
| [SRC-8D00DCEC0D-L000305](../../agents/sales_domain.py#L305) | 305 | `"                self,"` | — |
| [SRC-8D00DCEC0D-L000306](../../agents/sales_domain.py#L306) | 306 | `"                name,"` | — |
| [SRC-8D00DCEC0D-L000307](../../agents/sales_domain.py#L307) | 307 | `"                _clean_terms(getattr(self, name), field_name=name),"` | — |
| [SRC-8D00DCEC0D-L000308](../../agents/sales_domain.py#L308) | 308 | `"            )"` | — |
| [SRC-8D00DCEC0D-L000309](../../agents/sales_domain.py#L309) | 309 | `""` | — |
| [SRC-8D00DCEC0D-L000310](../../agents/sales_domain.py#L310) | 310 | `"    def to_dict(self) -> dict[str, list[str]]:"` | — |
| [SRC-8D00DCEC0D-L000311](../../agents/sales_domain.py#L311) | 311 | `"        return {"` | — |
| [SRC-8D00DCEC0D-L000312](../../agents/sales_domain.py#L312) | 312 | `"            name: list(getattr(self, name))"` | — |
| [SRC-8D00DCEC0D-L000313](../../agents/sales_domain.py#L313) | 313 | `"            for name in (\"locations\", \"industries\", \"customer_types\", \"decision_roles\", \"exclusions\")"` | — |
| [SRC-8D00DCEC0D-L000314](../../agents/sales_domain.py#L314) | 314 | `"        }"` | — |
| [SRC-8D00DCEC0D-L000315](../../agents/sales_domain.py#L315) | 315 | `""` | — |
| [SRC-8D00DCEC0D-L000316](../../agents/sales_domain.py#L316) | 316 | `""` | — |
| [SRC-8D00DCEC0D-L000317](../../agents/sales_domain.py#L317) | 317 | `"@dataclass(frozen=True, slots=True)"` | — |
| [SRC-8D00DCEC0D-L000318](../../agents/sales_domain.py#L318) | 318 | `"class TaxonomyCategory:"` | — |
| [SRC-8D00DCEC0D-L000319](../../agents/sales_domain.py#L319) | 319 | `"    \"\"\"A caller-defined taxonomy node; no sector is hard-coded in the matcher.\"\"\""` | — |
| [SRC-8D00DCEC0D-L000320](../../agents/sales_domain.py#L320) | 320 | `""` | — |
| [SRC-8D00DCEC0D-L000321](../../agents/sales_domain.py#L321) | 321 | `"    path: tuple[str, ...]"` | — |
| [SRC-8D00DCEC0D-L000322](../../agents/sales_domain.py#L322) | 322 | `"    aliases: tuple[str, ...]"` | — |
| [SRC-8D00DCEC0D-L000323](../../agents/sales_domain.py#L323) | 323 | `""` | — |
| [SRC-8D00DCEC0D-L000324](../../agents/sales_domain.py#L324) | 324 | `"    def __post_init__(self) -> None:"` | — |
| [SRC-8D00DCEC0D-L000325](../../agents/sales_domain.py#L325) | 325 | `"        object.__setattr__(self, \"path\", _clean_path(self.path, field_name=\"path\"))"` | — |
| [SRC-8D00DCEC0D-L000326](../../agents/sales_domain.py#L326) | 326 | `"        object.__setattr__(self, \"aliases\", _clean_terms(self.aliases, field_name=\"aliases\"))"` | — |
| [SRC-8D00DCEC0D-L000327](../../agents/sales_domain.py#L327) | 327 | `"        if not self.aliases:"` | — |
| [SRC-8D00DCEC0D-L000328](../../agents/sales_domain.py#L328) | 328 | `"            raise ValueError(\"taxonomy category requires at least one alias\")"` | — |
| [SRC-8D00DCEC0D-L000329](../../agents/sales_domain.py#L329) | 329 | `""` | — |
| [SRC-8D00DCEC0D-L000330](../../agents/sales_domain.py#L330) | 330 | `""` | — |
| [SRC-8D00DCEC0D-L000331](../../agents/sales_domain.py#L331) | 331 | `"@dataclass(frozen=True, slots=True)"` | — |
| [SRC-8D00DCEC0D-L000332](../../agents/sales_domain.py#L332) | 332 | `"class ProductTaxonomy:"` | — |
| [SRC-8D00DCEC0D-L000333](../../agents/sales_domain.py#L333) | 333 | `"    \"\"\"Extensible taxonomy supplied by configuration or a verified product catalogue.\"\"\""` | — |
| [SRC-8D00DCEC0D-L000334](../../agents/sales_domain.py#L334) | 334 | `""` | — |
| [SRC-8D00DCEC0D-L000335](../../agents/sales_domain.py#L335) | 335 | `"    categories: tuple[TaxonomyCategory, ...] = ()"` | — |
| [SRC-8D00DCEC0D-L000336](../../agents/sales_domain.py#L336) | 336 | `""` | — |
| [SRC-8D00DCEC0D-L000337](../../agents/sales_domain.py#L337) | 337 | `"    def __post_init__(self) -> None:"` | — |
| [SRC-8D00DCEC0D-L000338](../../agents/sales_domain.py#L338) | 338 | `"        if not all(isinstance(item, TaxonomyCategory) for item in self.categories):"` | — |
| [SRC-8D00DCEC0D-L000339](../../agents/sales_domain.py#L339) | 339 | `"            raise TypeError(\"categories must contain TaxonomyCategory instances\")"` | — |
| [SRC-8D00DCEC0D-L000340](../../agents/sales_domain.py#L340) | 340 | `"        paths = [tuple(normalize_text(part) for part in item.path) for item in self.categories]"` | — |
| [SRC-8D00DCEC0D-L000341](../../agents/sales_domain.py#L341) | 341 | `"        if len(paths) != len(set(paths)):"` | — |
| [SRC-8D00DCEC0D-L000342](../../agents/sales_domain.py#L342) | 342 | `"            raise ValueError(\"taxonomy category paths must be unique\")"` | — |
| [SRC-8D00DCEC0D-L000343](../../agents/sales_domain.py#L343) | 343 | `""` | — |
| [SRC-8D00DCEC0D-L000344](../../agents/sales_domain.py#L344) | 344 | `"    def match_categories(self, text: str) -> tuple[tuple[str, ...], ...]:"` | — |
| [SRC-8D00DCEC0D-L000345](../../agents/sales_domain.py#L345) | 345 | `"        \"\"\"Return all explicit taxonomy matches; never choose a winner by guessing.\"\"\""` | — |
| [SRC-8D00DCEC0D-L000346](../../agents/sales_domain.py#L346) | 346 | `"        matches = ["` | — |
| [SRC-8D00DCEC0D-L000347](../../agents/sales_domain.py#L347) | 347 | `"            category.path"` | — |
| [SRC-8D00DCEC0D-L000348](../../agents/sales_domain.py#L348) | 348 | `"            for category in self.categories"` | — |
| [SRC-8D00DCEC0D-L000349](../../agents/sales_domain.py#L349) | 349 | `"            if any(_contains_phrase(text, alias) for alias in category.aliases)"` | — |
| [SRC-8D00DCEC0D-L000350](../../agents/sales_domain.py#L350) | 350 | `"        ]"` | — |
| [SRC-8D00DCEC0D-L000351](../../agents/sales_domain.py#L351) | 351 | `"        return tuple(matches)"` | — |
| [SRC-8D00DCEC0D-L000352](../../agents/sales_domain.py#L352) | 352 | `""` | — |
| [SRC-8D00DCEC0D-L000353](../../agents/sales_domain.py#L353) | 353 | `"    def to_list(self) -> list[dict[str, list[str]]]:"` | — |
| [SRC-8D00DCEC0D-L000354](../../agents/sales_domain.py#L354) | 354 | `"        return ["` | — |
| [SRC-8D00DCEC0D-L000355](../../agents/sales_domain.py#L355) | 355 | `"            {\"path\": list(item.path), \"aliases\": list(item.aliases)}"` | — |
| [SRC-8D00DCEC0D-L000356](../../agents/sales_domain.py#L356) | 356 | `"            for item in self.categories"` | — |
| [SRC-8D00DCEC0D-L000357](../../agents/sales_domain.py#L357) | 357 | `"        ]"` | — |
| [SRC-8D00DCEC0D-L000358](../../agents/sales_domain.py#L358) | 358 | `""` | — |
| [SRC-8D00DCEC0D-L000359](../../agents/sales_domain.py#L359) | 359 | `""` | — |
| [SRC-8D00DCEC0D-L000360](../../agents/sales_domain.py#L360) | 360 | `"@dataclass(frozen=True, slots=True)"` | — |
| [SRC-8D00DCEC0D-L000361](../../agents/sales_domain.py#L361) | 361 | `"class DemandEvidence:"` | — |
| [SRC-8D00DCEC0D-L000362](../../agents/sales_domain.py#L362) | 362 | `"    \"\"\"Source provenance for a demand signal; dates remain distinct and optional.\"\"\""` | — |
| [SRC-8D00DCEC0D-L000363](../../agents/sales_domain.py#L363) | 363 | `""` | — |
| [SRC-8D00DCEC0D-L000364](../../agents/sales_domain.py#L364) | 364 | `"    source_id: str"` | — |
| [SRC-8D00DCEC0D-L000365](../../agents/sales_domain.py#L365) | 365 | `"    source_url: str"` | — |
| [SRC-8D00DCEC0D-L000366](../../agents/sales_domain.py#L366) | 366 | `"    excerpt: str"` | — |
| [SRC-8D00DCEC0D-L000367](../../agents/sales_domain.py#L367) | 367 | `"    content_basis: EvidenceBasis"` | — |
| [SRC-8D00DCEC0D-L000368](../../agents/sales_domain.py#L368) | 368 | `"    publication_date: str \| None = None"` | — |
| [SRC-8D00DCEC0D-L000369](../../agents/sales_domain.py#L369) | 369 | `"    event_date: str \| None = None"` | — |
| [SRC-8D00DCEC0D-L000370](../../agents/sales_domain.py#L370) | 370 | `"    observed_at: str \| None = None"` | — |
| [SRC-8D00DCEC0D-L000371](../../agents/sales_domain.py#L371) | 371 | `"    page_read: bool = False"` | — |
| [SRC-8D00DCEC0D-L000372](../../agents/sales_domain.py#L372) | 372 | `""` | — |
| [SRC-8D00DCEC0D-L000373](../../agents/sales_domain.py#L373) | 373 | `"    def __post_init__(self) -> None:"` | — |
| [SRC-8D00DCEC0D-L000374](../../agents/sales_domain.py#L374) | 374 | `"        object.__setattr__("` | — |
| [SRC-8D00DCEC0D-L000375](../../agents/sales_domain.py#L375) | 375 | `"            self,"` | — |
| [SRC-8D00DCEC0D-L000376](../../agents/sales_domain.py#L376) | 376 | `"            \"source_id\","` | — |
| [SRC-8D00DCEC0D-L000377](../../agents/sales_domain.py#L377) | 377 | `"            _clean_text(self.source_id, field_name=\"source_id\", maximum=160),"` | — |
| [SRC-8D00DCEC0D-L000378](../../agents/sales_domain.py#L378) | 378 | `"        )"` | — |
| [SRC-8D00DCEC0D-L000379](../../agents/sales_domain.py#L379) | 379 | `"        object.__setattr__(self, \"source_url\", _validate_http_url(self.source_url))"` | — |
| [SRC-8D00DCEC0D-L000380](../../agents/sales_domain.py#L380) | 380 | `"        object.__setattr__("` | — |
| [SRC-8D00DCEC0D-L000381](../../agents/sales_domain.py#L381) | 381 | `"            self,"` | — |
| [SRC-8D00DCEC0D-L000382](../../agents/sales_domain.py#L382) | 382 | `"            \"excerpt\","` | — |
| [SRC-8D00DCEC0D-L000383](../../agents/sales_domain.py#L383) | 383 | `"            _clean_text(self.excerpt, field_name=\"excerpt\", maximum=MAX_TEXT_LENGTH),"` | — |
| [SRC-8D00DCEC0D-L000384](../../agents/sales_domain.py#L384) | 384 | `"        )"` | — |
| [SRC-8D00DCEC0D-L000385](../../agents/sales_domain.py#L385) | 385 | `"        object.__setattr__("` | — |
| [SRC-8D00DCEC0D-L000386](../../agents/sales_domain.py#L386) | 386 | `"            self,"` | — |
| [SRC-8D00DCEC0D-L000387](../../agents/sales_domain.py#L387) | 387 | `"            \"content_basis\","` | — |
| [SRC-8D00DCEC0D-L000388](../../agents/sales_domain.py#L388) | 388 | `"            _enum_value(EvidenceBasis, self.content_basis, field_name=\"content_basis\"),"` | — |
| [SRC-8D00DCEC0D-L000389](../../agents/sales_domain.py#L389) | 389 | `"        )"` | — |
| [SRC-8D00DCEC0D-L000390](../../agents/sales_domain.py#L390) | 390 | `"        object.__setattr__("` | — |
| [SRC-8D00DCEC0D-L000391](../../agents/sales_domain.py#L391) | 391 | `"            self,"` | — |
| [SRC-8D00DCEC0D-L000392](../../agents/sales_domain.py#L392) | 392 | `"            \"publication_date\","` | — |
| [SRC-8D00DCEC0D-L000393](../../agents/sales_domain.py#L393) | 393 | `"            _validate_optional_date(self.publication_date, field_name=\"publication_date\"),"` | — |
| [SRC-8D00DCEC0D-L000394](../../agents/sales_domain.py#L394) | 394 | `"        )"` | — |
| [SRC-8D00DCEC0D-L000395](../../agents/sales_domain.py#L395) | 395 | `"        object.__setattr__("` | — |
| [SRC-8D00DCEC0D-L000396](../../agents/sales_domain.py#L396) | 396 | `"            self,"` | — |
| [SRC-8D00DCEC0D-L000397](../../agents/sales_domain.py#L397) | 397 | `"            \"event_date\","` | — |
| [SRC-8D00DCEC0D-L000398](../../agents/sales_domain.py#L398) | 398 | `"            _validate_optional_date(self.event_date, field_name=\"event_date\"),"` | — |
| [SRC-8D00DCEC0D-L000399](../../agents/sales_domain.py#L399) | 399 | `"        )"` | — |
| [SRC-8D00DCEC0D-L000400](../../agents/sales_domain.py#L400) | 400 | `"        object.__setattr__("` | — |
| [SRC-8D00DCEC0D-L000401](../../agents/sales_domain.py#L401) | 401 | `"            self,"` | — |
| [SRC-8D00DCEC0D-L000402](../../agents/sales_domain.py#L402) | 402 | `"            \"observed_at\","` | — |
| [SRC-8D00DCEC0D-L000403](../../agents/sales_domain.py#L403) | 403 | `"            _validate_optional_datetime(self.observed_at, field_name=\"observed_at\"),"` | — |
| [SRC-8D00DCEC0D-L000404](../../agents/sales_domain.py#L404) | 404 | `"        )"` | — |
| [SRC-8D00DCEC0D-L000405](../../agents/sales_domain.py#L405) | 405 | `"        if not isinstance(self.page_read, bool):"` | — |
| [SRC-8D00DCEC0D-L000406](../../agents/sales_domain.py#L406) | 406 | `"            raise TypeError(\"page_read must be a boolean\")"` | — |
| [SRC-8D00DCEC0D-L000407](../../agents/sales_domain.py#L407) | 407 | `"        if self.content_basis == EvidenceBasis.SEARCH_SNIPPET and self.page_read:"` | — |
| [SRC-8D00DCEC0D-L000408](../../agents/sales_domain.py#L408) | 408 | `"            raise ValueError(\"a search snippet cannot be marked as a successfully read page\")"` | — |
| [SRC-8D00DCEC0D-L000409](../../agents/sales_domain.py#L409) | 409 | `"        if self.content_basis == EvidenceBasis.PAGE_TEXT and not self.page_read:"` | — |
| [SRC-8D00DCEC0D-L000410](../../agents/sales_domain.py#L410) | 410 | `"            raise ValueError(\"page_text evidence requires page_read=True\")"` | — |
| [SRC-8D00DCEC0D-L000411](../../agents/sales_domain.py#L411) | 411 | `""` | — |
| [SRC-8D00DCEC0D-L000412](../../agents/sales_domain.py#L412) | 412 | `"    def to_dict(self) -> dict[str, object]:"` | — |
| [SRC-8D00DCEC0D-L000413](../../agents/sales_domain.py#L413) | 413 | `"        return {"` | — |
| [SRC-8D00DCEC0D-L000414](../../agents/sales_domain.py#L414) | 414 | `"            \"source_id\": self.source_id,"` | — |
| [SRC-8D00DCEC0D-L000415](../../agents/sales_domain.py#L415) | 415 | `"            \"source_url\": self.source_url,"` | — |
| [SRC-8D00DCEC0D-L000416](../../agents/sales_domain.py#L416) | 416 | `"            \"excerpt\": self.excerpt,"` | — |
| [SRC-8D00DCEC0D-L000417](../../agents/sales_domain.py#L417) | 417 | `"            \"content_basis\": self.content_basis.value,"` | — |
| [SRC-8D00DCEC0D-L000418](../../agents/sales_domain.py#L418) | 418 | `"            \"publication_date\": self.publication_date,"` | — |
| [SRC-8D00DCEC0D-L000419](../../agents/sales_domain.py#L419) | 419 | `"            \"event_date\": self.event_date,"` | — |
| [SRC-8D00DCEC0D-L000420](../../agents/sales_domain.py#L420) | 420 | `"            \"observed_at\": self.observed_at,"` | — |
| [SRC-8D00DCEC0D-L000421](../../agents/sales_domain.py#L421) | 421 | `"            \"page_read\": self.page_read,"` | — |
| [SRC-8D00DCEC0D-L000422](../../agents/sales_domain.py#L422) | 422 | `"        }"` | — |
| [SRC-8D00DCEC0D-L000423](../../agents/sales_domain.py#L423) | 423 | `""` | — |
| [SRC-8D00DCEC0D-L000424](../../agents/sales_domain.py#L424) | 424 | `""` | — |
| [SRC-8D00DCEC0D-L000425](../../agents/sales_domain.py#L425) | 425 | `"@dataclass(frozen=True, slots=True)"` | — |
| [SRC-8D00DCEC0D-L000426](../../agents/sales_domain.py#L426) | 426 | `"class DemandSignal:"` | — |
| [SRC-8D00DCEC0D-L000427](../../agents/sales_domain.py#L427) | 427 | `"    \"\"\"A classified demand signal, kept independent from product-fit assessment.\"\"\""` | — |
| [SRC-8D00DCEC0D-L000428](../../agents/sales_domain.py#L428) | 428 | `""` | — |
| [SRC-8D00DCEC0D-L000429](../../agents/sales_domain.py#L429) | 429 | `"    signal_id: str"` | — |
| [SRC-8D00DCEC0D-L000430](../../agents/sales_domain.py#L430) | 430 | `"    signal_type: DemandSignalType"` | — |
| [SRC-8D00DCEC0D-L000431](../../agents/sales_domain.py#L431) | 431 | `"    evidence: DemandEvidence"` | — |
| [SRC-8D00DCEC0D-L000432](../../agents/sales_domain.py#L432) | 432 | `"    product_fit: ProductFit = ProductFit.UNASSESSED"` | — |
| [SRC-8D00DCEC0D-L000433](../../agents/sales_domain.py#L433) | 433 | `"    identity_status: IdentityStatus = IdentityStatus.UNKNOWN"` | — |
| [SRC-8D00DCEC0D-L000434](../../agents/sales_domain.py#L434) | 434 | `"    classification_reason: str = \"\""` | — |
| [SRC-8D00DCEC0D-L000435](../../agents/sales_domain.py#L435) | 435 | `"    product_fit_reason: str = \"\""` | — |
| [SRC-8D00DCEC0D-L000436](../../agents/sales_domain.py#L436) | 436 | `""` | — |
| [SRC-8D00DCEC0D-L000437](../../agents/sales_domain.py#L437) | 437 | `"    def __post_init__(self) -> None:"` | — |
| [SRC-8D00DCEC0D-L000438](../../agents/sales_domain.py#L438) | 438 | `"        object.__setattr__("` | — |
| [SRC-8D00DCEC0D-L000439](../../agents/sales_domain.py#L439) | 439 | `"            self,"` | — |
| [SRC-8D00DCEC0D-L000440](../../agents/sales_domain.py#L440) | 440 | `"            \"signal_id\","` | — |
| [SRC-8D00DCEC0D-L000441](../../agents/sales_domain.py#L441) | 441 | `"            _clean_text(self.signal_id, field_name=\"signal_id\", maximum=160),"` | — |
| [SRC-8D00DCEC0D-L000442](../../agents/sales_domain.py#L442) | 442 | `"        )"` | — |
| [SRC-8D00DCEC0D-L000443](../../agents/sales_domain.py#L443) | 443 | `"        object.__setattr__("` | — |
| [SRC-8D00DCEC0D-L000444](../../agents/sales_domain.py#L444) | 444 | `"            self,"` | — |
| [SRC-8D00DCEC0D-L000445](../../agents/sales_domain.py#L445) | 445 | `"            \"signal_type\","` | — |
| [SRC-8D00DCEC0D-L000446](../../agents/sales_domain.py#L446) | 446 | `"            _enum_value(DemandSignalType, self.signal_type, field_name=\"signal_type\"),"` | — |
| [SRC-8D00DCEC0D-L000447](../../agents/sales_domain.py#L447) | 447 | `"        )"` | — |
| [SRC-8D00DCEC0D-L000448](../../agents/sales_domain.py#L448) | 448 | `"        object.__setattr__("` | — |
| [SRC-8D00DCEC0D-L000449](../../agents/sales_domain.py#L449) | 449 | `"            self,"` | — |
| [SRC-8D00DCEC0D-L000450](../../agents/sales_domain.py#L450) | 450 | `"            \"product_fit\","` | — |
| [SRC-8D00DCEC0D-L000451](../../agents/sales_domain.py#L451) | 451 | `"            _enum_value(ProductFit, self.product_fit, field_name=\"product_fit\"),"` | — |
| [SRC-8D00DCEC0D-L000452](../../agents/sales_domain.py#L452) | 452 | `"        )"` | — |
| [SRC-8D00DCEC0D-L000453](../../agents/sales_domain.py#L453) | 453 | `"        object.__setattr__("` | — |
| [SRC-8D00DCEC0D-L000454](../../agents/sales_domain.py#L454) | 454 | `"            self,"` | — |
| [SRC-8D00DCEC0D-L000455](../../agents/sales_domain.py#L455) | 455 | `"            \"identity_status\","` | — |
| [SRC-8D00DCEC0D-L000456](../../agents/sales_domain.py#L456) | 456 | `"            _enum_value(IdentityStatus, self.identity_status, field_name=\"identity_status\"),"` | — |
| [SRC-8D00DCEC0D-L000457](../../agents/sales_domain.py#L457) | 457 | `"        )"` | — |
| [SRC-8D00DCEC0D-L000458](../../agents/sales_domain.py#L458) | 458 | `"        if not isinstance(self.evidence, DemandEvidence):"` | — |
| [SRC-8D00DCEC0D-L000459](../../agents/sales_domain.py#L459) | 459 | `"            raise TypeError(\"evidence must be a DemandEvidence instance\")"` | — |
| [SRC-8D00DCEC0D-L000460](../../agents/sales_domain.py#L460) | 460 | `"        for name in (\"classification_reason\", \"product_fit_reason\"):"` | — |
| [SRC-8D00DCEC0D-L000461](../../agents/sales_domain.py#L461) | 461 | `"            value = getattr(self, name)"` | — |
| [SRC-8D00DCEC0D-L000462](../../agents/sales_domain.py#L462) | 462 | `"            if not isinstance(value, str):"` | — |
| [SRC-8D00DCEC0D-L000463](../../agents/sales_domain.py#L463) | 463 | `"                raise TypeError(f\"{name} must be a string\")"` | — |
| [SRC-8D00DCEC0D-L000464](../../agents/sales_domain.py#L464) | 464 | `"            if len(value) > 500:"` | — |
| [SRC-8D00DCEC0D-L000465](../../agents/sales_domain.py#L465) | 465 | `"                raise ValueError(f\"{name} exceeds 500 characters\")"` | — |
| [SRC-8D00DCEC0D-L000466](../../agents/sales_domain.py#L466) | 466 | `"        if self.product_fit == ProductFit.UNASSESSED and self.product_fit_reason:"` | — |
| [SRC-8D00DCEC0D-L000467](../../agents/sales_domain.py#L467) | 467 | `"            raise ValueError(\"unassessed product fit must not have a fit rationale\")"` | — |
| [SRC-8D00DCEC0D-L000468](../../agents/sales_domain.py#L468) | 468 | `"        if self.product_fit != ProductFit.UNASSESSED and not self.product_fit_reason.strip():"` | — |
| [SRC-8D00DCEC0D-L000469](../../agents/sales_domain.py#L469) | 469 | `"            raise ValueError(\"assessed product fit requires a rationale\")"` | — |
| [SRC-8D00DCEC0D-L000470](../../agents/sales_domain.py#L470) | 470 | `""` | — |
| [SRC-8D00DCEC0D-L000471](../../agents/sales_domain.py#L471) | 471 | `"    def to_dict(self) -> dict[str, object]:"` | — |
| [SRC-8D00DCEC0D-L000472](../../agents/sales_domain.py#L472) | 472 | `"        return {"` | — |
| [SRC-8D00DCEC0D-L000473](../../agents/sales_domain.py#L473) | 473 | `"            \"signal_id\": self.signal_id,"` | — |
| [SRC-8D00DCEC0D-L000474](../../agents/sales_domain.py#L474) | 474 | `"            \"signal_type\": self.signal_type.value,"` | — |
| [SRC-8D00DCEC0D-L000475](../../agents/sales_domain.py#L475) | 475 | `"            \"evidence\": self.evidence.to_dict(),"` | — |
| [SRC-8D00DCEC0D-L000476](../../agents/sales_domain.py#L476) | 476 | `"            \"product_fit\": self.product_fit.value,"` | — |
| [SRC-8D00DCEC0D-L000477](../../agents/sales_domain.py#L477) | 477 | `"            \"identity_status\": self.identity_status.value,"` | — |
| [SRC-8D00DCEC0D-L000478](../../agents/sales_domain.py#L478) | 478 | `"            \"classification_reason\": self.classification_reason,"` | — |
| [SRC-8D00DCEC0D-L000479](../../agents/sales_domain.py#L479) | 479 | `"            \"product_fit_reason\": self.product_fit_reason,"` | — |
| [SRC-8D00DCEC0D-L000480](../../agents/sales_domain.py#L480) | 480 | `"        }"` | — |
| [SRC-8D00DCEC0D-L000481](../../agents/sales_domain.py#L481) | 481 | `""` | — |
| [SRC-8D00DCEC0D-L000482](../../agents/sales_domain.py#L482) | 482 | `""` | — |
| [SRC-8D00DCEC0D-L000483](../../agents/sales_domain.py#L483) | 483 | `"@dataclass(frozen=True, slots=True)"` | — |
| [SRC-8D00DCEC0D-L000484](../../agents/sales_domain.py#L484) | 484 | `"class LeadQualification:"` | — |
| [SRC-8D00DCEC0D-L000485](../../agents/sales_domain.py#L485) | 485 | `"    \"\"\"Independent qualification dimensions; deliberately contains no purchase score.\"\"\""` | — |
| [SRC-8D00DCEC0D-L000486](../../agents/sales_domain.py#L486) | 486 | `""` | — |
| [SRC-8D00DCEC0D-L000487](../../agents/sales_domain.py#L487) | 487 | `"    signal_id: str"` | — |
| [SRC-8D00DCEC0D-L000488](../../agents/sales_domain.py#L488) | 488 | `"    product_fit: ProductFit = ProductFit.UNASSESSED"` | — |
| [SRC-8D00DCEC0D-L000489](../../agents/sales_domain.py#L489) | 489 | `"    source_quality: SourceQuality = SourceQuality.UNKNOWN"` | — |
| [SRC-8D00DCEC0D-L000490](../../agents/sales_domain.py#L490) | 490 | `"    freshness: FreshnessStatus = FreshnessStatus.UNKNOWN"` | — |
| [SRC-8D00DCEC0D-L000491](../../agents/sales_domain.py#L491) | 491 | `"    identity_status: IdentityStatus = IdentityStatus.UNKNOWN"` | — |
| [SRC-8D00DCEC0D-L000492](../../agents/sales_domain.py#L492) | 492 | `"    contactability: ContactabilityStatus = ContactabilityStatus.NOT_ASSESSED"` | — |
| [SRC-8D00DCEC0D-L000493](../../agents/sales_domain.py#L493) | 493 | `"    missing_information: tuple[str, ...] = ()"` | — |
| [SRC-8D00DCEC0D-L000494](../../agents/sales_domain.py#L494) | 494 | `""` | — |
| [SRC-8D00DCEC0D-L000495](../../agents/sales_domain.py#L495) | 495 | `"    def __post_init__(self) -> None:"` | — |
| [SRC-8D00DCEC0D-L000496](../../agents/sales_domain.py#L496) | 496 | `"        object.__setattr__("` | — |
| [SRC-8D00DCEC0D-L000497](../../agents/sales_domain.py#L497) | 497 | `"            self,"` | — |
| [SRC-8D00DCEC0D-L000498](../../agents/sales_domain.py#L498) | 498 | `"            \"signal_id\","` | — |
| [SRC-8D00DCEC0D-L000499](../../agents/sales_domain.py#L499) | 499 | `"            _clean_text(self.signal_id, field_name=\"signal_id\", maximum=160),"` | — |
| [SRC-8D00DCEC0D-L000500](../../agents/sales_domain.py#L500) | 500 | `"        )"` | — |
| [SRC-8D00DCEC0D-L000501](../../agents/sales_domain.py#L501) | 501 | `"        for name, enum_type in ("` | — |
| [SRC-8D00DCEC0D-L000502](../../agents/sales_domain.py#L502) | 502 | `"            (\"product_fit\", ProductFit),"` | — |
| [SRC-8D00DCEC0D-L000503](../../agents/sales_domain.py#L503) | 503 | `"            (\"source_quality\", SourceQuality),"` | — |
| [SRC-8D00DCEC0D-L000504](../../agents/sales_domain.py#L504) | 504 | `"            (\"freshness\", FreshnessStatus),"` | — |
| [SRC-8D00DCEC0D-L000505](../../agents/sales_domain.py#L505) | 505 | `"            (\"identity_status\", IdentityStatus),"` | — |
| [SRC-8D00DCEC0D-L000506](../../agents/sales_domain.py#L506) | 506 | `"            (\"contactability\", ContactabilityStatus),"` | — |
| [SRC-8D00DCEC0D-L000507](../../agents/sales_domain.py#L507) | 507 | `"        ):"` | — |
| [SRC-8D00DCEC0D-L000508](../../agents/sales_domain.py#L508) | 508 | `"            object.__setattr__("` | — |
| [SRC-8D00DCEC0D-L000509](../../agents/sales_domain.py#L509) | 509 | `"                self,"` | — |
| [SRC-8D00DCEC0D-L000510](../../agents/sales_domain.py#L510) | 510 | `"                name,"` | — |
| [SRC-8D00DCEC0D-L000511](../../agents/sales_domain.py#L511) | 511 | `"                _enum_value(enum_type, getattr(self, name), field_name=name),"` | — |
| [SRC-8D00DCEC0D-L000512](../../agents/sales_domain.py#L512) | 512 | `"            )"` | — |
| [SRC-8D00DCEC0D-L000513](../../agents/sales_domain.py#L513) | 513 | `"        object.__setattr__("` | — |
| [SRC-8D00DCEC0D-L000514](../../agents/sales_domain.py#L514) | 514 | `"            self,"` | — |
| [SRC-8D00DCEC0D-L000515](../../agents/sales_domain.py#L515) | 515 | `"            \"missing_information\","` | — |
| [SRC-8D00DCEC0D-L000516](../../agents/sales_domain.py#L516) | 516 | `"            _clean_terms(self.missing_information, field_name=\"missing_information\"),"` | — |
| [SRC-8D00DCEC0D-L000517](../../agents/sales_domain.py#L517) | 517 | `"        )"` | — |
| [SRC-8D00DCEC0D-L000518](../../agents/sales_domain.py#L518) | 518 | `""` | — |
| [SRC-8D00DCEC0D-L000519](../../agents/sales_domain.py#L519) | 519 | `"    def to_dict(self) -> dict[str, object]:"` | — |
| [SRC-8D00DCEC0D-L000520](../../agents/sales_domain.py#L520) | 520 | `"        return {"` | — |
| [SRC-8D00DCEC0D-L000521](../../agents/sales_domain.py#L521) | 521 | `"            \"signal_id\": self.signal_id,"` | — |
| [SRC-8D00DCEC0D-L000522](../../agents/sales_domain.py#L522) | 522 | `"            \"product_fit\": self.product_fit.value,"` | — |
| [SRC-8D00DCEC0D-L000523](../../agents/sales_domain.py#L523) | 523 | `"            \"source_quality\": self.source_quality.value,"` | — |
| [SRC-8D00DCEC0D-L000524](../../agents/sales_domain.py#L524) | 524 | `"            \"freshness\": self.freshness.value,"` | — |
| [SRC-8D00DCEC0D-L000525](../../agents/sales_domain.py#L525) | 525 | `"            \"identity_status\": self.identity_status.value,"` | — |
| [SRC-8D00DCEC0D-L000526](../../agents/sales_domain.py#L526) | 526 | `"            \"contactability\": self.contactability.value,"` | — |
| [SRC-8D00DCEC0D-L000527](../../agents/sales_domain.py#L527) | 527 | `"            \"missing_information\": list(self.missing_information),"` | — |
| [SRC-8D00DCEC0D-L000528](../../agents/sales_domain.py#L528) | 528 | `"        }"` | — |
| [SRC-8D00DCEC0D-L000529](../../agents/sales_domain.py#L529) | 529 | `""` | — |
| [SRC-8D00DCEC0D-L000530](../../agents/sales_domain.py#L530) | 530 | `""` | — |
| [SRC-8D00DCEC0D-L000531](../../agents/sales_domain.py#L531) | 531 | `""` | — |
| [SRC-8D00DCEC0D-L000532](../../agents/sales_domain.py#L532) | 532 | `"MAX_BUYER_QUERY_COUNT = 8"` | — |
| [SRC-8D00DCEC0D-L000533](../../agents/sales_domain.py#L533) | 533 | `""` | — |
| [SRC-8D00DCEC0D-L000534](../../agents/sales_domain.py#L534) | 534 | `""` | — |
| [SRC-8D00DCEC0D-L000535](../../agents/sales_domain.py#L535) | 535 | `"def build_buyer_queries("` | — |
| [SRC-8D00DCEC0D-L000536](../../agents/sales_domain.py#L536) | 536 | `"    product: ProductProfile,"` | — |
| [SRC-8D00DCEC0D-L000537](../../agents/sales_domain.py#L537) | 537 | `"    market: MarketProfile \| None = None,"` | — |
| [SRC-8D00DCEC0D-L000538](../../agents/sales_domain.py#L538) | 538 | `"    *,"` | — |
| [SRC-8D00DCEC0D-L000539](../../agents/sales_domain.py#L539) | 539 | `"    locale: str = \"auto\","` | — |
| [SRC-8D00DCEC0D-L000540](../../agents/sales_domain.py#L540) | 540 | `"    existing_queries: Iterable[str] = (),"` | — |
| [SRC-8D00DCEC0D-L000541](../../agents/sales_domain.py#L541) | 541 | `"    limit: int = MAX_BUYER_QUERY_COUNT,"` | — |
| [SRC-8D00DCEC0D-L000542](../../agents/sales_domain.py#L542) | 542 | `") -> list[str]:"` | — |
| [SRC-8D00DCEC0D-L000543](../../agents/sales_domain.py#L543) | 543 | `"    \"\"\"Build bounded, product-anchored buyer queries without sector-specific defaults."` | — |
| [SRC-8D00DCEC0D-L000544](../../agents/sales_domain.py#L544) | 544 | `""` | — |
| [SRC-8D00DCEC0D-L000545](../../agents/sales_domain.py#L545) | 545 | `"    Product-specific terms come only from ProductProfile. The default intent"` | — |
| [SRC-8D00DCEC0D-L000546](../../agents/sales_domain.py#L546) | 546 | `"    vocabulary is sector-neutral; category-specific expansions must be supplied"` | — |
| [SRC-8D00DCEC0D-L000547](../../agents/sales_domain.py#L547) | 547 | `"    by an explicit taxonomy/policy rather than silently defaulting to real estate."` | — |
| [SRC-8D00DCEC0D-L000548](../../agents/sales_domain.py#L548) | 548 | `"    \"\"\""` | — |
| [SRC-8D00DCEC0D-L000549](../../agents/sales_domain.py#L549) | 549 | `"    if not isinstance(product, ProductProfile):"` | — |
| [SRC-8D00DCEC0D-L000550](../../agents/sales_domain.py#L550) | 550 | `"        raise TypeError(\"product must be a ProductProfile instance\")"` | — |
| [SRC-8D00DCEC0D-L000551](../../agents/sales_domain.py#L551) | 551 | `"    if market is not None and not isinstance(market, MarketProfile):"` | — |
| [SRC-8D00DCEC0D-L000552](../../agents/sales_domain.py#L552) | 552 | `"        raise TypeError(\"market must be a MarketProfile instance\")"` | — |
| [SRC-8D00DCEC0D-L000553](../../agents/sales_domain.py#L553) | 553 | `"    if locale not in {\"auto\", \"ar\", \"en\", \"mixed\"}:"` | — |
| [SRC-8D00DCEC0D-L000554](../../agents/sales_domain.py#L554) | 554 | `"        raise ValueError(\"locale must be auto, ar, en, or mixed\")"` | — |
| [SRC-8D00DCEC0D-L000555](../../agents/sales_domain.py#L555) | 555 | `"    if not isinstance(limit, int) or isinstance(limit, bool) or not 1 <= limit <= MAX_BUYER_QUERY_COUNT:"` | — |
| [SRC-8D00DCEC0D-L000556](../../agents/sales_domain.py#L556) | 556 | `"        raise ValueError(f\"limit must be between 1 and {MAX_BUYER_QUERY_COUNT}\")"` | — |
| [SRC-8D00DCEC0D-L000557](../../agents/sales_domain.py#L557) | 557 | `""` | — |
| [SRC-8D00DCEC0D-L000558](../../agents/sales_domain.py#L558) | 558 | `"    if locale == \"auto\":"` | — |
| [SRC-8D00DCEC0D-L000559](../../agents/sales_domain.py#L559) | 559 | `"        locale = \"ar\" if re.search(r\"[\\u0600-\\u06FF]\", product.name) else \"en\""` | — |
| [SRC-8D00DCEC0D-L000560](../../agents/sales_domain.py#L560) | 560 | `""` | — |
| [SRC-8D00DCEC0D-L000561](../../agents/sales_domain.py#L561) | 561 | `"    location_suffix = \" \".join(market.locations) if market else \"\""` | — |
| [SRC-8D00DCEC0D-L000562](../../agents/sales_domain.py#L562) | 562 | `"    product_terms = (product.name, *product.aliases)"` | — |
| [SRC-8D00DCEC0D-L000563](../../agents/sales_domain.py#L563) | 563 | `"    candidates: list[str] = []"` | — |
| [SRC-8D00DCEC0D-L000564](../../agents/sales_domain.py#L564) | 564 | `""` | — |
| [SRC-8D00DCEC0D-L000565](../../agents/sales_domain.py#L565) | 565 | `"    for term in product_terms:"` | — |
| [SRC-8D00DCEC0D-L000566](../../agents/sales_domain.py#L566) | 566 | `"        subject = \" \".join(part for part in (term, location_suffix) if part).strip()"` | — |
| [SRC-8D00DCEC0D-L000567](../../agents/sales_domain.py#L567) | 567 | `"        if locale in {\"ar\", \"mixed\"}:"` | — |
| [SRC-8D00DCEC0D-L000568](../../agents/sales_domain.py#L568) | 568 | `"            candidates.extend("` | — |
| [SRC-8D00DCEC0D-L000569](../../agents/sales_domain.py#L569) | 569 | `"                ("` | — |
| [SRC-8D00DCEC0D-L000570](../../agents/sales_domain.py#L570) | 570 | `"                    f'\"مطلوب شراء\" \"{subject}\"',"` | — |
| [SRC-8D00DCEC0D-L000571](../../agents/sales_domain.py#L571) | 571 | `"                    f'\"عايز اشتري\" \"{subject}\"',"` | — |
| [SRC-8D00DCEC0D-L000572](../../agents/sales_domain.py#L572) | 572 | `"                    f'\"أريد شراء\" \"{subject}\"',"` | — |
| [SRC-8D00DCEC0D-L000573](../../agents/sales_domain.py#L573) | 573 | `"                    f'\"بدور على\" \"{subject}\"',"` | — |
| [SRC-8D00DCEC0D-L000574](../../agents/sales_domain.py#L574) | 574 | `"                    f'\"طلب عرض سعر\" \"{subject}\"',"` | — |
| [SRC-8D00DCEC0D-L000575](../../agents/sales_domain.py#L575) | 575 | `"                    f'site:facebook.com/groups \"{subject}\" (\"مطلوب\" OR \"عايز اشتري\" OR \"بدور على\")',"` | — |
| [SRC-8D00DCEC0D-L000576](../../agents/sales_domain.py#L576) | 576 | `"                )"` | — |
| [SRC-8D00DCEC0D-L000577](../../agents/sales_domain.py#L577) | 577 | `"            )"` | — |
| [SRC-8D00DCEC0D-L000578](../../agents/sales_domain.py#L578) | 578 | `"        if locale in {\"en\", \"mixed\"}:"` | — |
| [SRC-8D00DCEC0D-L000579](../../agents/sales_domain.py#L579) | 579 | `"            candidates.extend("` | — |
| [SRC-8D00DCEC0D-L000580](../../agents/sales_domain.py#L580) | 580 | `"                ("` | — |
| [SRC-8D00DCEC0D-L000581](../../agents/sales_domain.py#L581) | 581 | `"                    f'\"looking to buy\" \"{subject}\"',"` | — |
| [SRC-8D00DCEC0D-L000582](../../agents/sales_domain.py#L582) | 582 | `"                    f'\"want to purchase\" \"{subject}\"',"` | — |
| [SRC-8D00DCEC0D-L000583](../../agents/sales_domain.py#L583) | 583 | `"                    f'\"request for quotation\" \"{subject}\"',"` | — |
| [SRC-8D00DCEC0D-L000584](../../agents/sales_domain.py#L584) | 584 | `"                    f'site:linkedin.com/posts \"{subject}\" (\"looking to buy\" OR \"purchase\")',"` | — |
| [SRC-8D00DCEC0D-L000585](../../agents/sales_domain.py#L585) | 585 | `"                )"` | — |
| [SRC-8D00DCEC0D-L000586](../../agents/sales_domain.py#L586) | 586 | `"            )"` | — |
| [SRC-8D00DCEC0D-L000587](../../agents/sales_domain.py#L587) | 587 | `""` | — |
| [SRC-8D00DCEC0D-L000588](../../agents/sales_domain.py#L588) | 588 | `"    # Planner alternatives are supplementary only. Retain one only when it"` | — |
| [SRC-8D00DCEC0D-L000589](../../agents/sales_domain.py#L589) | 589 | `"    # explicitly mentions a configured product name/alias; do not import an"` | — |
| [SRC-8D00DCEC0D-L000590](../../agents/sales_domain.py#L590) | 590 | `"    # unrelated sector or generic listing query into this product's search."` | — |
| [SRC-8D00DCEC0D-L000591](../../agents/sales_domain.py#L591) | 591 | `"    for query in existing_queries:"` | — |
| [SRC-8D00DCEC0D-L000592](../../agents/sales_domain.py#L592) | 592 | `"        if isinstance(query, str) and product.matching_terms(query):"` | — |
| [SRC-8D00DCEC0D-L000593](../../agents/sales_domain.py#L593) | 593 | `"            candidates.append(query)"` | — |
| [SRC-8D00DCEC0D-L000594](../../agents/sales_domain.py#L594) | 594 | `""` | — |
| [SRC-8D00DCEC0D-L000595](../../agents/sales_domain.py#L595) | 595 | `"    result: list[str] = []"` | — |
| [SRC-8D00DCEC0D-L000596](../../agents/sales_domain.py#L596) | 596 | `"    seen: set[str] = set()"` | — |
| [SRC-8D00DCEC0D-L000597](../../agents/sales_domain.py#L597) | 597 | `"    for query in candidates:"` | — |
| [SRC-8D00DCEC0D-L000598](../../agents/sales_domain.py#L598) | 598 | `"        cleaned = _SPACE.sub(\" \", query).strip()[:500]"` | — |
| [SRC-8D00DCEC0D-L000599](../../agents/sales_domain.py#L599) | 599 | `"        key = normalize_text(cleaned)"` | — |
| [SRC-8D00DCEC0D-L000600](../../agents/sales_domain.py#L600) | 600 | `"        if cleaned and key and key not in seen:"` | — |
| [SRC-8D00DCEC0D-L000601](../../agents/sales_domain.py#L601) | 601 | `"            result.append(cleaned)"` | — |
| [SRC-8D00DCEC0D-L000602](../../agents/sales_domain.py#L602) | 602 | `"            seen.add(key)"` | — |
| [SRC-8D00DCEC0D-L000603](../../agents/sales_domain.py#L603) | 603 | `"        if len(result) >= limit:"` | — |
| [SRC-8D00DCEC0D-L000604](../../agents/sales_domain.py#L604) | 604 | `"            break"` | — |
| [SRC-8D00DCEC0D-L000605](../../agents/sales_domain.py#L605) | 605 | `"    return result"` | — |
| [SRC-8D00DCEC0D-L000606](../../agents/sales_domain.py#L606) | 606 | `""` | — |
| [SRC-8D00DCEC0D-L000607](../../agents/sales_domain.py#L607) | 607 | `""` | — |
| [SRC-8D00DCEC0D-L000608](../../agents/sales_domain.py#L608) | 608 | `"def to_json_dict(value: ProductProfile \| MarketProfile \| DemandEvidence \| DemandSignal \| LeadQualification) -> dict[str, object]:"` | — |
| [SRC-8D00DCEC0D-L000609](../../agents/sales_domain.py#L609) | 609 | `"    \"\"\"Serialize a supported domain object without silently dropping evidence fields.\"\"\""` | — |
| [SRC-8D00DCEC0D-L000610](../../agents/sales_domain.py#L610) | 610 | `"    if not hasattr(value, \"to_dict\"):"` | — |
| [SRC-8D00DCEC0D-L000611](../../agents/sales_domain.py#L611) | 611 | `"        raise TypeError(\"unsupported sales domain object\")"` | — |
| [SRC-8D00DCEC0D-L000612](../../agents/sales_domain.py#L612) | 612 | `"    return value.to_dict()"` | — |
## الوكيل والمنطق

### FILE-6E58A660BC — [agents/search_connectors.py](../../agents/search_connectors.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-6E58A660BC-L000001](../../agents/search_connectors.py#L1) | 1 | `"\"\"\"Free academic search connectors for Omarai (M1).\"\"\""` | — |
| [SRC-6E58A660BC-L000002](../../agents/search_connectors.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-6E58A660BC-L000003](../../agents/search_connectors.py#L3) | 3 | `""` | — |
| [SRC-6E58A660BC-L000004](../../agents/search_connectors.py#L4) | 4 | `"import json"` | — |
| [SRC-6E58A660BC-L000005](../../agents/search_connectors.py#L5) | 5 | `"import os"` | — |
| [SRC-6E58A660BC-L000006](../../agents/search_connectors.py#L6) | 6 | `"import re"` | — |
| [SRC-6E58A660BC-L000007](../../agents/search_connectors.py#L7) | 7 | `"import urllib.error"` | — |
| [SRC-6E58A660BC-L000008](../../agents/search_connectors.py#L8) | 8 | `"import urllib.parse"` | — |
| [SRC-6E58A660BC-L000009](../../agents/search_connectors.py#L9) | 9 | `"import urllib.request"` | — |
| [SRC-6E58A660BC-L000010](../../agents/search_connectors.py#L10) | 10 | `"from collections.abc import Callable"` | — |
| [SRC-6E58A660BC-L000011](../../agents/search_connectors.py#L11) | 11 | `"from typing import Any"` | — |
| [SRC-6E58A660BC-L000012](../../agents/search_connectors.py#L12) | 12 | `""` | — |
| [SRC-6E58A660BC-L000013](../../agents/search_connectors.py#L13) | 13 | `"MAX_CONNECTOR_RESULTS = 6"` | — |
| [SRC-6E58A660BC-L000014](../../agents/search_connectors.py#L14) | 14 | `"DEFAULT_TIMEOUT_SECONDS = 5"` | — |
| [SRC-6E58A660BC-L000015](../../agents/search_connectors.py#L15) | 15 | `"USER_AGENT = \"OmaraiResearchBot/1.0 (mailto:ops@example.com)\""` | — |
| [SRC-6E58A660BC-L000016](../../agents/search_connectors.py#L16) | 16 | `"ConnectorFn = Callable[[str, int], list[dict[str, Any]]]"` | — |
| [SRC-6E58A660BC-L000017](../../agents/search_connectors.py#L17) | 17 | `""` | — |
| [SRC-6E58A660BC-L000018](../../agents/search_connectors.py#L18) | 18 | `""` | — |
| [SRC-6E58A660BC-L000019](../../agents/search_connectors.py#L19) | 19 | `"def _clean_text(value: Any, limit: int = 1600) -> str:"` | — |
| [SRC-6E58A660BC-L000020](../../agents/search_connectors.py#L20) | 20 | `"    if not isinstance(value, str):"` | — |
| [SRC-6E58A660BC-L000021](../../agents/search_connectors.py#L21) | 21 | `"        return \"\""` | — |
| [SRC-6E58A660BC-L000022](../../agents/search_connectors.py#L22) | 22 | `"    return re.sub(r\"\\s+\", \" \", value).strip()[:limit]"` | — |
| [SRC-6E58A660BC-L000023](../../agents/search_connectors.py#L23) | 23 | `""` | — |
| [SRC-6E58A660BC-L000024](../../agents/search_connectors.py#L24) | 24 | `""` | — |
| [SRC-6E58A660BC-L000025](../../agents/search_connectors.py#L25) | 25 | `"def _http_get_json(url: str, headers: dict[str, str] \| None = None, timeout: int = DEFAULT_TIMEOUT_SECONDS) -> Any:"` | — |
| [SRC-6E58A660BC-L000026](../../agents/search_connectors.py#L26) | 26 | `"    req_headers = {\"User-Agent\": USER_AGENT, \"Accept\": \"application/json\"}"` | — |
| [SRC-6E58A660BC-L000027](../../agents/search_connectors.py#L27) | 27 | `"    if headers:"` | — |
| [SRC-6E58A660BC-L000028](../../agents/search_connectors.py#L28) | 28 | `"        req_headers.update(headers)"` | — |
| [SRC-6E58A660BC-L000029](../../agents/search_connectors.py#L29) | 29 | `"    request = urllib.request.Request(url, headers=req_headers, method=\"GET\")"` | — |
| [SRC-6E58A660BC-L000030](../../agents/search_connectors.py#L30) | 30 | `"    with urllib.request.urlopen(request, timeout=timeout) as response:"` | — |
| [SRC-6E58A660BC-L000031](../../agents/search_connectors.py#L31) | 31 | `"        return json.loads(response.read().decode(\"utf-8\", errors=\"replace\"))"` | — |
| [SRC-6E58A660BC-L000032](../../agents/search_connectors.py#L32) | 32 | `""` | — |
| [SRC-6E58A660BC-L000033](../../agents/search_connectors.py#L33) | 33 | `""` | — |
| [SRC-6E58A660BC-L000034](../../agents/search_connectors.py#L34) | 34 | `"def _http_get_text(url: str, timeout: int = DEFAULT_TIMEOUT_SECONDS) -> str:"` | — |
| [SRC-6E58A660BC-L000035](../../agents/search_connectors.py#L35) | 35 | `"    request = urllib.request.Request(url, headers={\"User-Agent\": USER_AGENT}, method=\"GET\")"` | — |
| [SRC-6E58A660BC-L000036](../../agents/search_connectors.py#L36) | 36 | `"    with urllib.request.urlopen(request, timeout=timeout) as response:"` | — |
| [SRC-6E58A660BC-L000037](../../agents/search_connectors.py#L37) | 37 | `"        return response.read().decode(\"utf-8\", errors=\"replace\")"` | — |
| [SRC-6E58A660BC-L000038](../../agents/search_connectors.py#L38) | 38 | `""` | — |
| [SRC-6E58A660BC-L000039](../../agents/search_connectors.py#L39) | 39 | `""` | — |
| [SRC-6E58A660BC-L000040](../../agents/search_connectors.py#L40) | 40 | `"def _result(*, title: str, url: str, snippet: str, provider: str, rank: int, query: str, published_at: str = \"\", source_class: str = \"web\") -> dict[str, Any]:"` | — |
| [SRC-6E58A660BC-L000041](../../agents/search_connectors.py#L41) | 41 | `"    return {"` | — |
| [SRC-6E58A660BC-L000042](../../agents/search_connectors.py#L42) | 42 | `"        \"title\": _clean_text(title, 300),"` | — |
| [SRC-6E58A660BC-L000043](../../agents/search_connectors.py#L43) | 43 | `"        \"url\": (url or \"\").strip(),"` | — |
| [SRC-6E58A660BC-L000044](../../agents/search_connectors.py#L44) | 44 | `"        \"snippet\": _clean_text(snippet, 1600),"` | — |
| [SRC-6E58A660BC-L000045](../../agents/search_connectors.py#L45) | 45 | `"        \"page_fetched\": False,"` | — |
| [SRC-6E58A660BC-L000046](../../agents/search_connectors.py#L46) | 46 | `"        \"provider\": provider,"` | — |
| [SRC-6E58A660BC-L000047](../../agents/search_connectors.py#L47) | 47 | `"        \"provider_rank\": rank,"` | — |
| [SRC-6E58A660BC-L000048](../../agents/search_connectors.py#L48) | 48 | `"        \"search_query\": query,"` | — |
| [SRC-6E58A660BC-L000049](../../agents/search_connectors.py#L49) | 49 | `"        \"published_at\": published_at or \"\","` | — |
| [SRC-6E58A660BC-L000050](../../agents/search_connectors.py#L50) | 50 | `"        \"source_class\": source_class,"` | — |
| [SRC-6E58A660BC-L000051](../../agents/search_connectors.py#L51) | 51 | `"    }"` | — |
| [SRC-6E58A660BC-L000052](../../agents/search_connectors.py#L52) | 52 | `""` | — |
| [SRC-6E58A660BC-L000053](../../agents/search_connectors.py#L53) | 53 | `""` | — |
| [SRC-6E58A660BC-L000054](../../agents/search_connectors.py#L54) | 54 | `"def search_openalex(query: str, limit: int = MAX_CONNECTOR_RESULTS) -> list[dict[str, Any]]:"` | — |
| [SRC-6E58A660BC-L000055](../../agents/search_connectors.py#L55) | 55 | `"    if not isinstance(query, str) or not query.strip():"` | — |
| [SRC-6E58A660BC-L000056](../../agents/search_connectors.py#L56) | 56 | `"        return []"` | — |
| [SRC-6E58A660BC-L000057](../../agents/search_connectors.py#L57) | 57 | `"    params = urllib.parse.urlencode({\"search\": query.strip()[:240], \"per_page\": max(1, min(int(limit), MAX_CONNECTOR_RESULTS)), \"mailto\": os.getenv(\"OPENALEX_MAILTO\", \"ops@example.com\")})"` | — |
| [SRC-6E58A660BC-L000058](../../agents/search_connectors.py#L58) | 58 | `"    data = _http_get_json(f\"https://api.openalex.org/works?{params}\")"` | — |
| [SRC-6E58A660BC-L000059](../../agents/search_connectors.py#L59) | 59 | `"    rows: list[dict[str, Any]] = []"` | — |
| [SRC-6E58A660BC-L000060](../../agents/search_connectors.py#L60) | 60 | `"    for item in data.get(\"results\", [])[:limit]:"` | — |
| [SRC-6E58A660BC-L000061](../../agents/search_connectors.py#L61) | 61 | `"        if not isinstance(item, dict):"` | — |
| [SRC-6E58A660BC-L000062](../../agents/search_connectors.py#L62) | 62 | `"            continue"` | — |
| [SRC-6E58A660BC-L000063](../../agents/search_connectors.py#L63) | 63 | `"        title = item.get(\"display_name\") or \"\""` | — |
| [SRC-6E58A660BC-L000064](../../agents/search_connectors.py#L64) | 64 | `"        url = \"\""` | — |
| [SRC-6E58A660BC-L000065](../../agents/search_connectors.py#L65) | 65 | `"        primary = item.get(\"primary_location\") or {}"` | — |
| [SRC-6E58A660BC-L000066](../../agents/search_connectors.py#L66) | 66 | `"        if isinstance(primary, dict) and primary.get(\"landing_page_url\"):"` | — |
| [SRC-6E58A660BC-L000067](../../agents/search_connectors.py#L67) | 67 | `"            url = str(primary.get(\"landing_page_url\"))"` | — |
| [SRC-6E58A660BC-L000068](../../agents/search_connectors.py#L68) | 68 | `"        elif item.get(\"id\"):"` | — |
| [SRC-6E58A660BC-L000069](../../agents/search_connectors.py#L69) | 69 | `"            url = str(item.get(\"id\"))"` | — |
| [SRC-6E58A660BC-L000070](../../agents/search_connectors.py#L70) | 70 | `"        concepts = \", \".join(str(c.get(\"display_name\", \"\")) for c in (item.get(\"concepts\") or [])[:5] if isinstance(c, dict))"` | — |
| [SRC-6E58A660BC-L000071](../../agents/search_connectors.py#L71) | 71 | `"        snippet = f\"{title}. {concepts}\".strip(\". \")"` | — |
| [SRC-6E58A660BC-L000072](../../agents/search_connectors.py#L72) | 72 | `"        if title and url:"` | — |
| [SRC-6E58A660BC-L000073](../../agents/search_connectors.py#L73) | 73 | `"            rows.append(_result(title=title, url=url, snippet=snippet or title, provider=\"openalex\", rank=len(rows) + 1, query=query, published_at=str(item.get(\"publication_date\") or \"\"), source_class=\"academic\"))"` | — |
| [SRC-6E58A660BC-L000074](../../agents/search_connectors.py#L74) | 74 | `"    return rows"` | — |
| [SRC-6E58A660BC-L000075](../../agents/search_connectors.py#L75) | 75 | `""` | — |
| [SRC-6E58A660BC-L000076](../../agents/search_connectors.py#L76) | 76 | `""` | — |
| [SRC-6E58A660BC-L000077](../../agents/search_connectors.py#L77) | 77 | `"def search_arxiv(query: str, limit: int = MAX_CONNECTOR_RESULTS) -> list[dict[str, Any]]:"` | — |
| [SRC-6E58A660BC-L000078](../../agents/search_connectors.py#L78) | 78 | `"    if not isinstance(query, str) or not query.strip():"` | — |
| [SRC-6E58A660BC-L000079](../../agents/search_connectors.py#L79) | 79 | `"        return []"` | — |
| [SRC-6E58A660BC-L000080](../../agents/search_connectors.py#L80) | 80 | `"    params = urllib.parse.urlencode({\"search_query\": f\"all:{query.strip()[:200]}\", \"start\": 0, \"max_results\": max(1, min(int(limit), MAX_CONNECTOR_RESULTS))})"` | — |
| [SRC-6E58A660BC-L000081](../../agents/search_connectors.py#L81) | 81 | `"    xml_text = _http_get_text(f\"https://export.arxiv.org/api/query?{params}\")"` | — |
| [SRC-6E58A660BC-L000082](../../agents/search_connectors.py#L82) | 82 | `"    entries = re.findall(r\"<entry>(.*?)</entry>\", xml_text, flags=re.DOTALL)"` | — |
| [SRC-6E58A660BC-L000083](../../agents/search_connectors.py#L83) | 83 | `"    rows: list[dict[str, Any]] = []"` | — |
| [SRC-6E58A660BC-L000084](../../agents/search_connectors.py#L84) | 84 | `"    for entry in entries[:limit]:"` | — |
| [SRC-6E58A660BC-L000085](../../agents/search_connectors.py#L85) | 85 | `"        title_m = re.search(r\"<title>(.*?)</title>\", entry, re.DOTALL)"` | — |
| [SRC-6E58A660BC-L000086](../../agents/search_connectors.py#L86) | 86 | `"        link_m = re.search(r\"<id>(https?://arxiv\\.org/abs/[^<]+)</id>\", entry)"` | — |
| [SRC-6E58A660BC-L000087](../../agents/search_connectors.py#L87) | 87 | `"        summary_m = re.search(r\"<summary>(.*?)</summary>\", entry, re.DOTALL)"` | — |
| [SRC-6E58A660BC-L000088](../../agents/search_connectors.py#L88) | 88 | `"        published_m = re.search(r\"<published>([^<]+)</published>\", entry)"` | — |
| [SRC-6E58A660BC-L000089](../../agents/search_connectors.py#L89) | 89 | `"        title = _clean_text(title_m.group(1) if title_m else \"\")"` | — |
| [SRC-6E58A660BC-L000090](../../agents/search_connectors.py#L90) | 90 | `"        link = link_m.group(1) if link_m else \"\""` | — |
| [SRC-6E58A660BC-L000091](../../agents/search_connectors.py#L91) | 91 | `"        summary = _clean_text(summary_m.group(1) if summary_m else \"\", 1600)"` | — |
| [SRC-6E58A660BC-L000092](../../agents/search_connectors.py#L92) | 92 | `"        published = published_m.group(1) if published_m else \"\""` | — |
| [SRC-6E58A660BC-L000093](../../agents/search_connectors.py#L93) | 93 | `"        if title and link:"` | — |
| [SRC-6E58A660BC-L000094](../../agents/search_connectors.py#L94) | 94 | `"            rows.append(_result(title=title, url=link, snippet=summary or title, provider=\"arxiv\", rank=len(rows) + 1, query=query, published_at=published, source_class=\"academic\"))"` | — |
| [SRC-6E58A660BC-L000095](../../agents/search_connectors.py#L95) | 95 | `"    return rows"` | — |
| [SRC-6E58A660BC-L000096](../../agents/search_connectors.py#L96) | 96 | `""` | — |
| [SRC-6E58A660BC-L000097](../../agents/search_connectors.py#L97) | 97 | `""` | — |
| [SRC-6E58A660BC-L000098](../../agents/search_connectors.py#L98) | 98 | `"def search_crossref(query: str, limit: int = MAX_CONNECTOR_RESULTS) -> list[dict[str, Any]]:"` | — |
| [SRC-6E58A660BC-L000099](../../agents/search_connectors.py#L99) | 99 | `"    if not isinstance(query, str) or not query.strip():"` | — |
| [SRC-6E58A660BC-L000100](../../agents/search_connectors.py#L100) | 100 | `"        return []"` | — |
| [SRC-6E58A660BC-L000101](../../agents/search_connectors.py#L101) | 101 | `"    params = urllib.parse.urlencode({\"query\": query.strip()[:240], \"rows\": max(1, min(int(limit), MAX_CONNECTOR_RESULTS)), \"mailto\": os.getenv(\"CROSSREF_MAILTO\", \"ops@example.com\")})"` | — |
| [SRC-6E58A660BC-L000102](../../agents/search_connectors.py#L102) | 102 | `"    data = _http_get_json(f\"https://api.crossref.org/works?{params}\", headers={\"User-Agent\": USER_AGENT})"` | — |
| [SRC-6E58A660BC-L000103](../../agents/search_connectors.py#L103) | 103 | `"    items = ((data.get(\"message\") or {}).get(\"items\") or [])[:limit]"` | — |
| [SRC-6E58A660BC-L000104](../../agents/search_connectors.py#L104) | 104 | `"    rows: list[dict[str, Any]] = []"` | — |
| [SRC-6E58A660BC-L000105](../../agents/search_connectors.py#L105) | 105 | `"    for item in items:"` | — |
| [SRC-6E58A660BC-L000106](../../agents/search_connectors.py#L106) | 106 | `"        if not isinstance(item, dict):"` | — |
| [SRC-6E58A660BC-L000107](../../agents/search_connectors.py#L107) | 107 | `"            continue"` | — |
| [SRC-6E58A660BC-L000108](../../agents/search_connectors.py#L108) | 108 | `"        title_list = item.get(\"title\") or []"` | — |
| [SRC-6E58A660BC-L000109](../../agents/search_connectors.py#L109) | 109 | `"        title = title_list[0] if isinstance(title_list, list) and title_list else \"\""` | — |
| [SRC-6E58A660BC-L000110](../../agents/search_connectors.py#L110) | 110 | `"        url = str(item.get(\"URL\") or \"\")"` | — |
| [SRC-6E58A660BC-L000111](../../agents/search_connectors.py#L111) | 111 | `"        container_list = item.get(\"container-title\") or []"` | — |
| [SRC-6E58A660BC-L000112](../../agents/search_connectors.py#L112) | 112 | `"        container = container_list[0] if isinstance(container_list, list) and container_list else \"\""` | — |
| [SRC-6E58A660BC-L000113](../../agents/search_connectors.py#L113) | 113 | `"        year = \"\""` | — |
| [SRC-6E58A660BC-L000114](../../agents/search_connectors.py#L114) | 114 | `"        issued = item.get(\"issued\") or {}"` | — |
| [SRC-6E58A660BC-L000115](../../agents/search_connectors.py#L115) | 115 | `"        if isinstance(issued, dict) and issued.get(\"date-parts\"):"` | — |
| [SRC-6E58A660BC-L000116](../../agents/search_connectors.py#L116) | 116 | `"            try:"` | — |
| [SRC-6E58A660BC-L000117](../../agents/search_connectors.py#L117) | 117 | `"                year = str(issued[\"date-parts\"][0][0])"` | — |
| [SRC-6E58A660BC-L000118](../../agents/search_connectors.py#L118) | 118 | `"            except (IndexError, TypeError, KeyError):"` | — |
| [SRC-6E58A660BC-L000119](../../agents/search_connectors.py#L119) | 119 | `"                year = \"\""` | — |
| [SRC-6E58A660BC-L000120](../../agents/search_connectors.py#L120) | 120 | `"        snippet = _clean_text(f\"{title}. {container} {year}\".strip())"` | — |
| [SRC-6E58A660BC-L000121](../../agents/search_connectors.py#L121) | 121 | `"        if title and url:"` | — |
| [SRC-6E58A660BC-L000122](../../agents/search_connectors.py#L122) | 122 | `"            rows.append(_result(title=title, url=url, snippet=snippet, provider=\"crossref\", rank=len(rows) + 1, query=query, published_at=year, source_class=\"academic\"))"` | — |
| [SRC-6E58A660BC-L000123](../../agents/search_connectors.py#L123) | 123 | `"    return rows"` | — |
| [SRC-6E58A660BC-L000124](../../agents/search_connectors.py#L124) | 124 | `""` | — |
| [SRC-6E58A660BC-L000125](../../agents/search_connectors.py#L125) | 125 | `""` | — |
| [SRC-6E58A660BC-L000126](../../agents/search_connectors.py#L126) | 126 | `"def search_semantic_scholar(query: str, limit: int = MAX_CONNECTOR_RESULTS) -> list[dict[str, Any]]:"` | — |
| [SRC-6E58A660BC-L000127](../../agents/search_connectors.py#L127) | 127 | `"    if not isinstance(query, str) or not query.strip():"` | — |
| [SRC-6E58A660BC-L000128](../../agents/search_connectors.py#L128) | 128 | `"        return []"` | — |
| [SRC-6E58A660BC-L000129](../../agents/search_connectors.py#L129) | 129 | `"    key = os.getenv(\"SEMANTIC_SCHOLAR_API_KEY\", \"\").strip()"` | — |
| [SRC-6E58A660BC-L000130](../../agents/search_connectors.py#L130) | 130 | `"    params = urllib.parse.urlencode({\"query\": query.strip()[:240], \"limit\": max(1, min(int(limit), MAX_CONNECTOR_RESULTS)), \"fields\": \"title,url,abstract,year,externalIds\"})"` | — |
| [SRC-6E58A660BC-L000131](../../agents/search_connectors.py#L131) | 131 | `"    headers = {\"User-Agent\": USER_AGENT}"` | — |
| [SRC-6E58A660BC-L000132](../../agents/search_connectors.py#L132) | 132 | `"    if key:"` | — |
| [SRC-6E58A660BC-L000133](../../agents/search_connectors.py#L133) | 133 | `"        headers[\"x-api-key\"] = key"` | — |
| [SRC-6E58A660BC-L000134](../../agents/search_connectors.py#L134) | 134 | `"    data = _http_get_json(f\"https://api.semanticscholar.org/graph/v1/paper/search?{params}\", headers=headers)"` | — |
| [SRC-6E58A660BC-L000135](../../agents/search_connectors.py#L135) | 135 | `"    rows: list[dict[str, Any]] = []"` | — |
| [SRC-6E58A660BC-L000136](../../agents/search_connectors.py#L136) | 136 | `"    for item in (data.get(\"data\") or [])[:limit]:"` | — |
| [SRC-6E58A660BC-L000137](../../agents/search_connectors.py#L137) | 137 | `"        if not isinstance(item, dict):"` | — |
| [SRC-6E58A660BC-L000138](../../agents/search_connectors.py#L138) | 138 | `"            continue"` | — |
| [SRC-6E58A660BC-L000139](../../agents/search_connectors.py#L139) | 139 | `"        title = item.get(\"title\") or \"\""` | — |
| [SRC-6E58A660BC-L000140](../../agents/search_connectors.py#L140) | 140 | `"        url = item.get(\"url\") or \"\""` | — |
| [SRC-6E58A660BC-L000141](../../agents/search_connectors.py#L141) | 141 | `"        if not url and isinstance(item.get(\"externalIds\"), dict):"` | — |
| [SRC-6E58A660BC-L000142](../../agents/search_connectors.py#L142) | 142 | `"            doi = item[\"externalIds\"].get(\"DOI\")"` | — |
| [SRC-6E58A660BC-L000143](../../agents/search_connectors.py#L143) | 143 | `"            if doi:"` | — |
| [SRC-6E58A660BC-L000144](../../agents/search_connectors.py#L144) | 144 | `"                url = f\"https://doi.org/{doi}\""` | — |
| [SRC-6E58A660BC-L000145](../../agents/search_connectors.py#L145) | 145 | `"        snippet = item.get(\"abstract\") or title"` | — |
| [SRC-6E58A660BC-L000146](../../agents/search_connectors.py#L146) | 146 | `"        year = str(item.get(\"year\") or \"\")"` | — |
| [SRC-6E58A660BC-L000147](../../agents/search_connectors.py#L147) | 147 | `"        if title and url:"` | — |
| [SRC-6E58A660BC-L000148](../../agents/search_connectors.py#L148) | 148 | `"            rows.append(_result(title=title, url=url, snippet=snippet, provider=\"semantic_scholar\", rank=len(rows) + 1, query=query, published_at=year, source_class=\"academic\"))"` | — |
| [SRC-6E58A660BC-L000149](../../agents/search_connectors.py#L149) | 149 | `"    return rows"` | — |
| [SRC-6E58A660BC-L000150](../../agents/search_connectors.py#L150) | 150 | `""` | — |
| [SRC-6E58A660BC-L000151](../../agents/search_connectors.py#L151) | 151 | `""` | — |
| [SRC-6E58A660BC-L000152](../../agents/search_connectors.py#L152) | 152 | `"CONNECTOR_REGISTRY: dict[str, dict[str, Any]] = {"` | — |
| [SRC-6E58A660BC-L000153](../../agents/search_connectors.py#L153) | 153 | `"    \"openalex\": {\"fn\": search_openalex, \"source_class\": \"academic\", \"requires_key\": False},"` | — |
| [SRC-6E58A660BC-L000154](../../agents/search_connectors.py#L154) | 154 | `"    \"arxiv\": {\"fn\": search_arxiv, \"source_class\": \"academic\", \"requires_key\": False},"` | — |
| [SRC-6E58A660BC-L000155](../../agents/search_connectors.py#L155) | 155 | `"    \"crossref\": {\"fn\": search_crossref, \"source_class\": \"academic\", \"requires_key\": False},"` | — |
| [SRC-6E58A660BC-L000156](../../agents/search_connectors.py#L156) | 156 | `"    \"semantic_scholar\": {\"fn\": search_semantic_scholar, \"source_class\": \"academic\", \"requires_key\": False},"` | — |
| [SRC-6E58A660BC-L000157](../../agents/search_connectors.py#L157) | 157 | `"}"` | — |
| [SRC-6E58A660BC-L000158](../../agents/search_connectors.py#L158) | 158 | `""` | — |
| [SRC-6E58A660BC-L000159](../../agents/search_connectors.py#L159) | 159 | `""` | — |
| [SRC-6E58A660BC-L000160](../../agents/search_connectors.py#L160) | 160 | `"def run_connector(name: str, query: str, limit: int = MAX_CONNECTOR_RESULTS) -> list[dict[str, Any]]:"` | — |
| [SRC-6E58A660BC-L000161](../../agents/search_connectors.py#L161) | 161 | `"    meta = CONNECTOR_REGISTRY.get(name)"` | — |
| [SRC-6E58A660BC-L000162](../../agents/search_connectors.py#L162) | 162 | `"    if not meta or meta.get(\"fn\") is None:"` | — |
| [SRC-6E58A660BC-L000163](../../agents/search_connectors.py#L163) | 163 | `"        return []"` | — |
| [SRC-6E58A660BC-L000164](../../agents/search_connectors.py#L164) | 164 | `"    if not isinstance(query, str) or not query.strip():"` | — |
| [SRC-6E58A660BC-L000165](../../agents/search_connectors.py#L165) | 165 | `"        return []"` | — |
| [SRC-6E58A660BC-L000166](../../agents/search_connectors.py#L166) | 166 | `"    try:"` | — |
| [SRC-6E58A660BC-L000167](../../agents/search_connectors.py#L167) | 167 | `"        rows = meta[\"fn\"](query, limit=limit) or []"` | — |
| [SRC-6E58A660BC-L000168](../../agents/search_connectors.py#L168) | 168 | `"        return [row for row in rows if isinstance(row, dict) and row.get(\"url\") and row.get(\"title\")]"` | — |
| [SRC-6E58A660BC-L000169](../../agents/search_connectors.py#L169) | 169 | `"    except (TimeoutError, urllib.error.URLError, urllib.error.HTTPError, ValueError, KeyError, TypeError, json.JSONDecodeError, OSError):"` | — |
| [SRC-6E58A660BC-L000170](../../agents/search_connectors.py#L170) | 170 | `"        return []"` | — |
| [SRC-6E58A660BC-L000171](../../agents/search_connectors.py#L171) | 171 | `""` | — |
| [SRC-6E58A660BC-L000172](../../agents/search_connectors.py#L172) | 172 | `""` | — |
| [SRC-6E58A660BC-L000173](../../agents/search_connectors.py#L173) | 173 | `"def run_free_academic_connectors(query: str, limit_per: int = 4) -> list[dict[str, Any]]:"` | — |
| [SRC-6E58A660BC-L000174](../../agents/search_connectors.py#L174) | 174 | `"    combined: list[dict[str, Any]] = []"` | — |
| [SRC-6E58A660BC-L000175](../../agents/search_connectors.py#L175) | 175 | `"    for name in (\"openalex\", \"arxiv\", \"crossref\"):"` | — |
| [SRC-6E58A660BC-L000176](../../agents/search_connectors.py#L176) | 176 | `"        combined.extend(run_connector(name, query, limit=limit_per))"` | — |
| [SRC-6E58A660BC-L000177](../../agents/search_connectors.py#L177) | 177 | `"    return combined"` | — |
## الوكيل والمنطق

### FILE-686F71AA50 — [agents/task_understanding.py](../../agents/task_understanding.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-686F71AA50-L000001](../../agents/task_understanding.py#L1) | 1 | `"\"\"\"Deterministic, auditable natural-language task interpretation for Omarai."` | — |
| [SRC-686F71AA50-L000002](../../agents/task_understanding.py#L2) | 2 | `""` | — |
| [SRC-686F71AA50-L000003](../../agents/task_understanding.py#L3) | 3 | `"This module produces a bounded TaskSpec and a query-strategy matrix. It does not"` | — |
| [SRC-686F71AA50-L000004](../../agents/task_understanding.py#L4) | 4 | `"claim semantic certainty, generate facts, or execute tools. Signals and hypotheses"` | — |
| [SRC-686F71AA50-L000005](../../agents/task_understanding.py#L5) | 5 | `"are diagnostics, never probabilities. Search plans remain subject to budgets,"` | — |
| [SRC-686F71AA50-L000006](../../agents/task_understanding.py#L6) | 6 | `"source guardrails, and the final evidence checks."` | — |
| [SRC-686F71AA50-L000007](../../agents/task_understanding.py#L7) | 7 | `"\"\"\""` | — |
| [SRC-686F71AA50-L000008](../../agents/task_understanding.py#L8) | 8 | `"from __future__ import annotations"` | — |
| [SRC-686F71AA50-L000009](../../agents/task_understanding.py#L9) | 9 | `""` | — |
| [SRC-686F71AA50-L000010](../../agents/task_understanding.py#L10) | 10 | `"import re"` | — |
| [SRC-686F71AA50-L000011](../../agents/task_understanding.py#L11) | 11 | `"import unicodedata"` | — |
| [SRC-686F71AA50-L000012](../../agents/task_understanding.py#L12) | 12 | `"from typing import Any"` | — |
| [SRC-686F71AA50-L000013](../../agents/task_understanding.py#L13) | 13 | `""` | — |
| [SRC-686F71AA50-L000014](../../agents/task_understanding.py#L14) | 14 | `"MAX_TASK_CHARS = 4000"` | — |
| [SRC-686F71AA50-L000015](../../agents/task_understanding.py#L15) | 15 | `"MAX_TASK_ASPECTS = 8"` | — |
| [SRC-686F71AA50-L000016](../../agents/task_understanding.py#L16) | 16 | `"MAX_STRATEGY_QUERIES = 8"` | — |
| [SRC-686F71AA50-L000017](../../agents/task_understanding.py#L17) | 17 | `"SUPPORTED_MODES = frozenset({\"auto\", \"deep\", \"latest\", \"social\"})"` | — |
| [SRC-686F71AA50-L000018](../../agents/task_understanding.py#L18) | 18 | `""` | — |
| [SRC-686F71AA50-L000019](../../agents/task_understanding.py#L19) | 19 | `"# Closed, code-owned playbooks. The model receives concise task guidance derived"` | — |
| [SRC-686F71AA50-L000020](../../agents/task_understanding.py#L20) | 20 | `"# from these IDs; arbitrary planner/source text cannot add executable instructions."` | — |
| [SRC-686F71AA50-L000021](../../agents/task_understanding.py#L21) | 21 | `"_REASONING_GUIDANCE = {"` | — |
| [SRC-686F71AA50-L000022](../../agents/task_understanding.py#L22) | 22 | `"    \"preserve_goal_and_constraints\": \"حافظ على مقصد المستخدم والكيانات والبلد والسنة والميزانية والتواريخ والصيغة التي ذكرها صراحة؛ لا تخترع قيودًا مفقودة.\","` | — |
| [SRC-686F71AA50-L000023](../../agents/task_understanding.py#L23) | 23 | `"    \"separate_facts_inferences_hypotheses\": \"افصل ما يقوله المصدر مباشرة عن الاستنتاج والفرضية والمعلومة المجهولة؛ لا ترفع الفرضية إلى حقيقة دون دليل.\","` | — |
| [SRC-686F71AA50-L000024](../../agents/task_understanding.py#L24) | 24 | `"    \"ground_material_claims\": \"اربط كل ادعاء واقعي جوهري بدليل مناسب من المصدر؛ الاستشهاد أو تشابه الكلمات وحده لا يثبت صحة الادعاء.\","` | — |
| [SRC-686F71AA50-L000025](../../agents/task_understanding.py#L25) | 25 | `"    \"bounded_stop_rule\": \"استخدم المحاولات والوقت المسموحين فقط؛ عند نقص الدليل، أجب جزئيًا أو امتنع بوضوح بدل التخمين.\","` | — |
| [SRC-686F71AA50-L000026](../../agents/task_understanding.py#L26) | 26 | `"    \"clarify_required_input\": \"إذا غاب مدخل إلزامي يغيّر معنى المهمة، اطلبه قبل تشغيل أداة أو اختراع هدف.\","` | — |
| [SRC-686F71AA50-L000027](../../agents/task_understanding.py#L27) | 27 | `"    \"resolve_followup_slots\": \"في المتابعة، احتفظ فقط بالسياق الذي له مرجع واضح، وطبّق التغييرات التي ذكرها المستخدم، ولا ترث موضوعًا قديمًا بعد تغيير الموضوع.\","` | — |
| [SRC-686F71AA50-L000028](../../agents/task_understanding.py#L28) | 28 | `"    \"verify_official_destination\": \"طابق اسم الجهة والبلد أولًا؛ فضّل نطاق الجهة أو رابطًا صادرًا عن بوابة رسمية موثوقة، ولا تعتبر امتداد النطاق وحده إثباتًا للملكية.\","` | — |
| [SRC-686F71AA50-L000029](../../agents/task_understanding.py#L29) | 29 | `"    \"separate_event_and_publication_dates\": \"ميّز تاريخ وقوع الحدث عن تاريخ النشر وآخر تحديث وتاريخ الوصول؛ لا تستخدم خبرًا قديمًا لإثبات حالة متغيرة الآن.\","` | — |
| [SRC-686F71AA50-L000030](../../agents/task_understanding.py#L30) | 30 | `"    \"reject_stale_current_claims\": \"للمعلومة الحالية، افحص حداثة المصدر وقابلية قراءة الصفحة وارتباطها بالحالة الحالية؛ اعرض عدم التأكد إذا غاب دليل حديث مؤهل.\","` | — |
| [SRC-686F71AA50-L000031](../../agents/task_understanding.py#L31) | 31 | `"    \"decompose_explicit_criteria\": \"قسّم المقارنة إلى كل معيار صريح، وابحث عن دليل لكل معيار، وسجّل المحاور التي لا تزال بلا دليل بدل إسقاطها.\","` | — |
| [SRC-686F71AA50-L000032](../../agents/task_understanding.py#L32) | 32 | `"    \"normalize_comparison_conditions\": \"قبل المقارنة، وحّد العملة والوحدات والفترة وظروف الاستخدام؛ لا تقارن قيمًا غير قابلة للمقارنة دون شرح الفرق.\","` | — |
| [SRC-686F71AA50-L000033](../../agents/task_understanding.py#L33) | 33 | `"    \"separate_specs_and_experiences\": \"افصل المواصفات الرسمية عن الاختبارات الصحفية وتجارب الأفراد والإعلانات؛ لكل نوع منها ما يستطيع إثباته وحدوده.\","` | — |
| [SRC-686F71AA50-L000034](../../agents/task_understanding.py#L34) | 34 | `"    \"balance_social_evidence\": \"ميّز التجربة الشخصية المحتملة عن السؤال والترويج والمحتوى الصحفي؛ اعرض عينة المنشورات وتواريخها والاختلافات ولا تعمم على الجميع.\","` | — |
| [SRC-686F71AA50-L000035](../../agents/task_understanding.py#L35) | 35 | `"    \"record_observed_symptoms\": \"احفظ رسالة الخطأ والبيئة والإصدار والخطوات التي يمكن تكرارها؛ ميّز الملاحظة المرصودة عن تفسير السبب.\","` | — |
| [SRC-686F71AA50-L000036](../../agents/task_understanding.py#L36) | 36 | `"    \"rank_testable_hypotheses\": \"أنشئ عدة فرضيات للسبب، ورتّبها وفق الأدلة المتاحة وقابلية الاختبار، ولا تدّعِ إثبات السبب قبل تجربة تفصل بين الفرضيات.\","` | — |
| [SRC-686F71AA50-L000037](../../agents/task_understanding.py#L37) | 37 | `"    \"verify_primary_technical_docs\": \"تحقق من دليل المنتج أو مرجع الواجهة أو سجل التغيير الأصلي، واستخدم اختبارًا يعيد إنتاج المشكلة للتحقق من الإصلاح.\","` | — |
| [SRC-686F71AA50-L000038](../../agents/task_understanding.py#L38) | 38 | `"    \"prefer_low_risk_steps\": \"ابدأ بخطوات تشخيص قابلة للعكس ومنخفضة المخاطر، واذكر شروط التوقف؛ لا تقترح إجراءً خطيرًا لمجرد أنه احتمال.\","` | — |
| [SRC-686F71AA50-L000039](../../agents/task_understanding.py#L39) | 39 | `"    \"ordered_safe_procedure\": \"اذكر المتطلبات المسبقة والتحذيرات ثم الخطوات بالترتيب، وأضف طريقة للتحقق من النتيجة ولا تساوِ بين إكمال الخطوات ونجاحها.\","` | — |
| [SRC-686F71AA50-L000040](../../agents/task_understanding.py#L40) | 40 | `"    \"check_health_scope_and_urgency\": \"افصل التثقيف الصحي العام عن التشخيص الشخصي، وقدّم مصادر صحية موثوقة وحدود المعلومات، ووجّه الحالات الطارئة إلى الرعاية المناسبة.\","` | — |
| [SRC-686F71AA50-L000041](../../agents/task_understanding.py#L41) | 41 | `"    \"check_legal_jurisdiction_and_effective_date\": \"حدّد الدولة أو الاختصاص القانوني وتاريخ النفاذ، وقدّم النص الأصلي الرسمي عند توفره، ولا تعرض المعلومات العامة بوصفها استشارة قانونية خاصة.\","` | — |
| [SRC-686F71AA50-L000042](../../agents/task_understanding.py#L42) | 42 | `"    \"validate_data_before_interpreting\": \"تحقق من تعريف المقياس ووحدة التحليل والفترة والبيانات الناقصة والتكرارات والقيم الشاذة قبل تفسير النتائج؛ الارتباط لا يثبت السببية.\","` | — |
| [SRC-686F71AA50-L000043](../../agents/task_understanding.py#L43) | 43 | `"    \"validate_units_and_arithmetic\": \"تحقق من الوحدات والمدخلات والافتراضات، واعرض المعادلة أو خطوات الحساب القابلة للفحص، وأجرِ تحققًا حسابيًا مستقلًا عندما يلزم.\","` | — |
| [SRC-686F71AA50-L000044](../../agents/task_understanding.py#L44) | 44 | `"    \"preserve_translation_meaning\": \"حافظ على المعنى والنبرة والأسماء والمصطلحات وصيغة الهدف؛ أظهر الالتباس الحقيقي بدل اختراع معنى للنص.\","` | — |
| [SRC-686F71AA50-L000045](../../agents/task_understanding.py#L45) | 45 | `"    \"preserve_user_facts_in_writing\": \"التزم بالجمهور والنبرة والشكل المطلوب، ولا تضف حقائق غير مقدمة أو موثقة، وافصل إعادة الصياغة عن التحقق الواقعي.\","` | — |
| [SRC-686F71AA50-L000046](../../agents/task_understanding.py#L46) | 46 | `"    \"plan_dependencies_and_fallbacks\": \"رتّب العمل حسب التبعيات والموارد والموعد والمخاطر، وبيّن الافتراضات والبدائل، ولا تصف خطوة مقترحة بأنها نُفذت.\","` | — |
| [SRC-686F71AA50-L000047](../../agents/task_understanding.py#L47) | 47 | `"    \"compare_recommendation_tradeoffs\": \"وازن البدائل وفق احتياج المستخدم وقيوده، وبيّن المفاضلات والمعلومات الناقصة، ولا تعلن فائزًا عامًا دون أساس مقارنة واضح.\","` | — |
| [SRC-686F71AA50-L000048](../../agents/task_understanding.py#L48) | 48 | `"    \"summarize_only_available_content\": \"لخّص النص المقدم أو الصفحة التي قُرئت فعلًا فقط؛ لا تستنتج محتوى غير مقروء من عنوان أو رابط.\","` | — |
| [SRC-686F71AA50-L000049](../../agents/task_understanding.py#L49) | 49 | `"    \"qualify_buyer_intent\": \"ميّز إشارة نية شراء صريحة عن إعلان بيع أو صفحة تجارية؛ لا تعتبر الإعلان عميلًا ولا تزعم التحقق من الهوية.\","` | — |
| [SRC-686F71AA50-L000050](../../agents/task_understanding.py#L50) | 50 | `"    \"prefer_lowest_sufficient_tool\": \"اختر أقل مسار أدوات كافٍ للمهمة؛ لا تبحث في الويب عندما تكفي المادة المقدمة أو الحساب المحلي، ولا تشغّل أداة غير مهيأة أو غير مسموح بها.\","` | — |
| [SRC-686F71AA50-L000051](../../agents/task_understanding.py#L51) | 51 | `"}"` | — |
| [SRC-686F71AA50-L000052](../../agents/task_understanding.py#L52) | 52 | `"_REASONING_FAMILY_IDS = {"` | — |
| [SRC-686F71AA50-L000053](../../agents/task_understanding.py#L53) | 53 | `"    \"official_site_lookup\": (\"verify_official_destination\",),"` | — |
| [SRC-686F71AA50-L000054](../../agents/task_understanding.py#L54) | 54 | `"    \"social_opinions\": (\"balance_social_evidence\", \"separate_specs_and_experiences\"),"` | — |
| [SRC-686F71AA50-L000055](../../agents/task_understanding.py#L55) | 55 | `"    \"summarize\": (\"summarize_only_available_content\",),"` | — |
| [SRC-686F71AA50-L000056](../../agents/task_understanding.py#L56) | 56 | `"    \"troubleshoot\": (\"record_observed_symptoms\", \"rank_testable_hypotheses\", \"verify_primary_technical_docs\", \"prefer_low_risk_steps\"),"` | — |
| [SRC-686F71AA50-L000057](../../agents/task_understanding.py#L57) | 57 | `"    \"compare\": (\"decompose_explicit_criteria\", \"normalize_comparison_conditions\", \"separate_specs_and_experiences\"),"` | — |
| [SRC-686F71AA50-L000058](../../agents/task_understanding.py#L58) | 58 | `"    \"how_to\": (\"ordered_safe_procedure\",),"` | — |
| [SRC-686F71AA50-L000059](../../agents/task_understanding.py#L59) | 59 | `"    \"lead_generation\": (\"qualify_buyer_intent\",),"` | — |
| [SRC-686F71AA50-L000060](../../agents/task_understanding.py#L60) | 60 | `"    \"recommendation\": (\"compare_recommendation_tradeoffs\",),"` | — |
| [SRC-686F71AA50-L000061](../../agents/task_understanding.py#L61) | 61 | `"    \"medical_information\": (\"check_health_scope_and_urgency\",),"` | — |
| [SRC-686F71AA50-L000062](../../agents/task_understanding.py#L62) | 62 | `"    \"legal_information\": (\"check_legal_jurisdiction_and_effective_date\",),"` | — |
| [SRC-686F71AA50-L000063](../../agents/task_understanding.py#L63) | 63 | `"    \"coding_or_technical_design\": (\"record_observed_symptoms\", \"rank_testable_hypotheses\", \"verify_primary_technical_docs\"),"` | — |
| [SRC-686F71AA50-L000064](../../agents/task_understanding.py#L64) | 64 | `"    \"data_analysis\": (\"validate_data_before_interpreting\",),"` | — |
| [SRC-686F71AA50-L000065](../../agents/task_understanding.py#L65) | 65 | `"    \"calculation\": (\"validate_units_and_arithmetic\",),"` | — |
| [SRC-686F71AA50-L000066](../../agents/task_understanding.py#L66) | 66 | `"    \"translation\": (\"preserve_translation_meaning\",),"` | — |
| [SRC-686F71AA50-L000067](../../agents/task_understanding.py#L67) | 67 | `"    \"writing_or_editing\": (\"preserve_user_facts_in_writing\",),"` | — |
| [SRC-686F71AA50-L000068](../../agents/task_understanding.py#L68) | 68 | `"    \"planning\": (\"plan_dependencies_and_fallbacks\",),"` | — |
| [SRC-686F71AA50-L000069](../../agents/task_understanding.py#L69) | 69 | `"    \"creative_generation\": (\"preserve_user_facts_in_writing\",),"` | — |
| [SRC-686F71AA50-L000070](../../agents/task_understanding.py#L70) | 70 | `"}"` | — |
| [SRC-686F71AA50-L000071](../../agents/task_understanding.py#L71) | 71 | `"_DECISION_MATRIX = ("` | — |
| [SRC-686F71AA50-L000072](../../agents/task_understanding.py#L72) | 72 | `"    {\"stage\": \"interpret\", \"check\": \"goal_context_required_inputs\", \"pass_action\": \"preserve_explicit_constraints\", \"fail_action\": \"clarify_missing_required_input\"},"` | — |
| [SRC-686F71AA50-L000073](../../agents/task_understanding.py#L73) | 73 | `"    {\"stage\": \"route\", \"check\": \"tool_permission_and_readiness\", \"pass_action\": \"use_only_allowed_configured_tools\", \"fail_action\": \"report_not_configured_or_blocked\"},"` | — |
| [SRC-686F71AA50-L000074](../../agents/task_understanding.py#L74) | 74 | `"    {\"stage\": \"plan\", \"check\": \"distinct_relevant_queries_and_budget\", \"pass_action\": \"execute_bounded_deduplicated_plan\", \"fail_action\": \"stop_and_report_limit\"},"` | — |
| [SRC-686F71AA50-L000075](../../agents/task_understanding.py#L75) | 75 | `"    {\"stage\": \"evidence\", \"check\": \"relevance_identity_freshness_readability\", \"pass_action\": \"retain_task_eligible_evidence\", \"fail_action\": \"exclude_and_record_reason\"},"` | — |
| [SRC-686F71AA50-L000076](../../agents/task_understanding.py#L76) | 76 | `"    {\"stage\": \"synthesize\", \"check\": \"claim_support_and_scope\", \"pass_action\": \"cite_supported_claims_and_qualify_inference\", \"fail_action\": \"answer_partially_or_abstain\"},"` | — |
| [SRC-686F71AA50-L000077](../../agents/task_understanding.py#L77) | 77 | `"    {\"stage\": \"terminate\", \"check\": \"actual_stage_outcomes\", \"pass_action\": \"report_observed_completion_state\", \"fail_action\": \"mark_partial_failed_or_not_run\"},"` | — |
| [SRC-686F71AA50-L000078](../../agents/task_understanding.py#L78) | 78 | `")"` | — |
| [SRC-686F71AA50-L000079](../../agents/task_understanding.py#L79) | 79 | `"_DECISION_STAGES = {row[\"stage\"] for row in _DECISION_MATRIX}"` | — |
| [SRC-686F71AA50-L000080](../../agents/task_understanding.py#L80) | 80 | `"_DECISION_IDS = {"` | — |
| [SRC-686F71AA50-L000081](../../agents/task_understanding.py#L81) | 81 | `"    field: {row[field] for row in _DECISION_MATRIX}"` | — |
| [SRC-686F71AA50-L000082](../../agents/task_understanding.py#L82) | 82 | `"    for field in (\"check\", \"pass_action\", \"fail_action\")"` | — |
| [SRC-686F71AA50-L000083](../../agents/task_understanding.py#L83) | 83 | `"}"` | — |
| [SRC-686F71AA50-L000084](../../agents/task_understanding.py#L84) | 84 | `""` | — |
| [SRC-686F71AA50-L000085](../../agents/task_understanding.py#L85) | 85 | `""` | — |
| [SRC-686F71AA50-L000086](../../agents/task_understanding.py#L86) | 86 | `"def _reasoning_strategy_ids("` | — |
| [SRC-686F71AA50-L000087](../../agents/task_understanding.py#L87) | 87 | `"    family: str,"` | — |
| [SRC-686F71AA50-L000088](../../agents/task_understanding.py#L88) | 88 | `"    constraints: dict[str, Any],"` | — |
| [SRC-686F71AA50-L000089](../../agents/task_understanding.py#L89) | 89 | `"    context_resolution: dict[str, Any],"` | — |
| [SRC-686F71AA50-L000090](../../agents/task_understanding.py#L90) | 90 | `"    missing_required_inputs: list[str],"` | — |
| [SRC-686F71AA50-L000091](../../agents/task_understanding.py#L91) | 91 | `") -> list[str]:"` | — |
| [SRC-686F71AA50-L000092](../../agents/task_understanding.py#L92) | 92 | `"    selected = ["` | — |
| [SRC-686F71AA50-L000093](../../agents/task_understanding.py#L93) | 93 | `"        \"preserve_goal_and_constraints\","` | — |
| [SRC-686F71AA50-L000094](../../agents/task_understanding.py#L94) | 94 | `"        \"separate_facts_inferences_hypotheses\","` | — |
| [SRC-686F71AA50-L000095](../../agents/task_understanding.py#L95) | 95 | `"        \"ground_material_claims\","` | — |
| [SRC-686F71AA50-L000096](../../agents/task_understanding.py#L96) | 96 | `"        \"bounded_stop_rule\","` | — |
| [SRC-686F71AA50-L000097](../../agents/task_understanding.py#L97) | 97 | `"        \"prefer_lowest_sufficient_tool\","` | — |
| [SRC-686F71AA50-L000098](../../agents/task_understanding.py#L98) | 98 | `"    ]"` | — |
| [SRC-686F71AA50-L000099](../../agents/task_understanding.py#L99) | 99 | `"    selected.extend(_REASONING_FAMILY_IDS.get(family, ()))"` | — |
| [SRC-686F71AA50-L000100](../../agents/task_understanding.py#L100) | 100 | `"    if missing_required_inputs or context_resolution.get(\"needs_clarification\"):"` | — |
| [SRC-686F71AA50-L000101](../../agents/task_understanding.py#L101) | 101 | `"        selected.append(\"clarify_required_input\")"` | — |
| [SRC-686F71AA50-L000102](../../agents/task_understanding.py#L102) | 102 | `"    if context_resolution.get(\"is_follow_up\"):"` | — |
| [SRC-686F71AA50-L000103](../../agents/task_understanding.py#L103) | 103 | `"        selected.append(\"resolve_followup_slots\")"` | — |
| [SRC-686F71AA50-L000104](../../agents/task_understanding.py#L104) | 104 | `"    if constraints.get(\"time_sensitive_request\"):"` | — |
| [SRC-686F71AA50-L000105](../../agents/task_understanding.py#L105) | 105 | `"        selected.extend((\"separate_event_and_publication_dates\", \"reject_stale_current_claims\"))"` | — |
| [SRC-686F71AA50-L000106](../../agents/task_understanding.py#L106) | 106 | `"    if constraints.get(\"official_destination_required\"):"` | — |
| [SRC-686F71AA50-L000107](../../agents/task_understanding.py#L107) | 107 | `"        selected.append(\"verify_official_destination\")"` | — |
| [SRC-686F71AA50-L000108](../../agents/task_understanding.py#L108) | 108 | `"    if constraints.get(\"social_evidence_requested\"):"` | — |
| [SRC-686F71AA50-L000109](../../agents/task_understanding.py#L109) | 109 | `"        selected.append(\"balance_social_evidence\")"` | — |
| [SRC-686F71AA50-L000110](../../agents/task_understanding.py#L110) | 110 | `"    if len(constraints.get(\"explicit_aspects\") or []) > 1:"` | — |
| [SRC-686F71AA50-L000111](../../agents/task_understanding.py#L111) | 111 | `"        selected.append(\"decompose_explicit_criteria\")"` | — |
| [SRC-686F71AA50-L000112](../../agents/task_understanding.py#L112) | 112 | `"    if constraints.get(\"explicit_budgets\"):"` | — |
| [SRC-686F71AA50-L000113](../../agents/task_understanding.py#L113) | 113 | `"        selected.append(\"preserve_goal_and_constraints\")"` | — |
| [SRC-686F71AA50-L000114](../../agents/task_understanding.py#L114) | 114 | `"    return list(dict.fromkeys(item for item in selected if item in _REASONING_GUIDANCE))[:12]"` | — |
| [SRC-686F71AA50-L000115](../../agents/task_understanding.py#L115) | 115 | `""` | — |
| [SRC-686F71AA50-L000116](../../agents/task_understanding.py#L116) | 116 | `""` | — |
| [SRC-686F71AA50-L000117](../../agents/task_understanding.py#L117) | 117 | `"def reasoning_guidance_for_task_spec(task_spec: dict[str, Any]) -> list[str]:"` | — |
| [SRC-686F71AA50-L000118](../../agents/task_understanding.py#L118) | 118 | `"    \"\"\"Expand allowlisted reasoning IDs into fixed, non-executable guidance text.\"\"\""` | — |
| [SRC-686F71AA50-L000119](../../agents/task_understanding.py#L119) | 119 | `"    ids = task_spec.get(\"reasoning_strategy_ids\") if isinstance(task_spec, dict) else []"` | — |
| [SRC-686F71AA50-L000120](../../agents/task_understanding.py#L120) | 120 | `"    if not isinstance(ids, list):"` | — |
| [SRC-686F71AA50-L000121](../../agents/task_understanding.py#L121) | 121 | `"        return []"` | — |
| [SRC-686F71AA50-L000122](../../agents/task_understanding.py#L122) | 122 | `"    return [_REASONING_GUIDANCE[item] for item in ids if isinstance(item, str) and item in _REASONING_GUIDANCE][:12]"` | — |
| [SRC-686F71AA50-L000123](../../agents/task_understanding.py#L123) | 123 | `""` | — |
| [SRC-686F71AA50-L000124](../../agents/task_understanding.py#L124) | 124 | `"_ARABIC_DIACRITICS = re.compile(r\"[\\u0610-\\u061A\\u064B-\\u065F\\u0670\\u06D6-\\u06ED]\")"` | — |
| [SRC-686F71AA50-L000125](../../agents/task_understanding.py#L125) | 125 | `"_PUNCTUATION = re.compile(r\"[؟?!.،,؛;:(){}\\[\\]\\\"'«»]+\")"` | — |
| [SRC-686F71AA50-L000126](../../agents/task_understanding.py#L126) | 126 | `"_SPACE = re.compile(r\"\\s+\")"` | — |
| [SRC-686F71AA50-L000127](../../agents/task_understanding.py#L127) | 127 | `"_TOKEN_RE = re.compile(r\"[a-z0-9]+\|[\\u0600-\\u06FF]+\", re.IGNORECASE)"` | — |
| [SRC-686F71AA50-L000128](../../agents/task_understanding.py#L128) | 128 | `""` | — |
| [SRC-686F71AA50-L000129](../../agents/task_understanding.py#L129) | 129 | `"_PATTERNS: dict[str, tuple[str, ...]] = {"` | — |
| [SRC-686F71AA50-L000130](../../agents/task_understanding.py#L130) | 130 | `"    \"official_site_lookup\": ("` | — |
| [SRC-686F71AA50-L000131](../../agents/task_understanding.py#L131) | 131 | `"        \"الموقع الرسمي\", \"موقع رسمي\", \"رابط الموقع الرسمي\", \"الصفحه الرسميه\","` | — |
| [SRC-686F71AA50-L000132](../../agents/task_understanding.py#L132) | 132 | `"        \"الموقع الحكومي\", \"official website\", \"official site\", \"official homepage\","` | — |
| [SRC-686F71AA50-L000133](../../agents/task_understanding.py#L133) | 133 | `"    ),"` | — |
| [SRC-686F71AA50-L000134](../../agents/task_understanding.py#L134) | 134 | `"    \"social_opinions\": ("` | — |
| [SRC-686F71AA50-L000135](../../agents/task_understanding.py#L135) | 135 | `"        \"اراء الناس\", \"اراء المستخدمين\", \"تجارب الناس\", \"تجارب المستخدمين\","` | — |
| [SRC-686F71AA50-L000136](../../agents/task_understanding.py#L136) | 136 | `"        \"تجارب الملاك\", \"تجارب ملاك\", \"تجربة مالك\", \"مراجعات المستخدمين\", \"الناس بتقول ايه\","` | — |
| [SRC-686F71AA50-L000137](../../agents/task_understanding.py#L137) | 137 | `"        \"real user reviews\", \"owner experience\", \"customer opinions\", \"people's opinions\","` | — |
| [SRC-686F71AA50-L000138](../../agents/task_understanding.py#L138) | 138 | `"        \"user experiences\", \"what do owners say\","` | — |
| [SRC-686F71AA50-L000139](../../agents/task_understanding.py#L139) | 139 | `"    ),"` | — |
| [SRC-686F71AA50-L000140](../../agents/task_understanding.py#L140) | 140 | `"    \"summarize\": ("` | — |
| [SRC-686F71AA50-L000141](../../agents/task_understanding.py#L141) | 141 | `"        \"لخص\", \"تلخيص\", \"ملخص\", \"summarize\", \"summarise\", \"summary of\","` | — |
| [SRC-686F71AA50-L000142](../../agents/task_understanding.py#L142) | 142 | `"    ),"` | — |
| [SRC-686F71AA50-L000143](../../agents/task_understanding.py#L143) | 143 | `"    \"troubleshoot\": ("` | — |
| [SRC-686F71AA50-L000144](../../agents/task_understanding.py#L144) | 144 | `"        \"حل مشكلة\", \"عطل\", \"اعطال\", \"مش بيشتغل\", \"لا يعمل\", \"خطأ\", \"رساله خطأ\","` | — |
| [SRC-686F71AA50-L000145](../../agents/task_understanding.py#L145) | 145 | `"        \"اصلح\", \"استكشاف الاعطال\", \"troubleshoot\", \"debug\", \"does not work\","` | — |
| [SRC-686F71AA50-L000146](../../agents/task_understanding.py#L146) | 146 | `"        \"not working\", \"error message\", \"fix the problem\", \"common failures\","` | — |
| [SRC-686F71AA50-L000147](../../agents/task_understanding.py#L147) | 147 | `"    ),"` | — |
| [SRC-686F71AA50-L000148](../../agents/task_understanding.py#L148) | 148 | `"    \"how_to\": ("` | — |
| [SRC-686F71AA50-L000149](../../agents/task_understanding.py#L149) | 149 | `"        \"ازاي\", \"كيف\", \"طريقة\", \"خطوات\", \"اشرح لي كيف\", \"علمني\", \"كيفية\","` | — |
| [SRC-686F71AA50-L000150](../../agents/task_understanding.py#L150) | 150 | `"        \"how to\", \"steps to\", \"walk me through\", \"teach me\","` | — |
| [SRC-686F71AA50-L000151](../../agents/task_understanding.py#L151) | 151 | `"    ),"` | — |
| [SRC-686F71AA50-L000152](../../agents/task_understanding.py#L152) | 152 | `"    \"compare\": ("` | — |
| [SRC-686F71AA50-L000153](../../agents/task_understanding.py#L153) | 153 | `"        \"قارن\", \"مقارنه\", \"الفرق بين\", \"ايهما افضل\", \"مميزات وعيوب\","` | — |
| [SRC-686F71AA50-L000154](../../agents/task_understanding.py#L154) | 154 | `"        \"الايجابيات والسلبيات\", \"مفاضله\", \"compare\", \"comparison\", \"versus\","` | — |
| [SRC-686F71AA50-L000155](../../agents/task_understanding.py#L155) | 155 | `"        \"trade-offs\", \"pros and cons\", \"which is better\","` | — |
| [SRC-686F71AA50-L000156](../../agents/task_understanding.py#L156) | 156 | `"    ),"` | — |
| [SRC-686F71AA50-L000157](../../agents/task_understanding.py#L157) | 157 | `"    \"current_information\": ("` | — |
| [SRC-686F71AA50-L000158](../../agents/task_understanding.py#L158) | 158 | `"        \"اليوم\", \"النهارده\", \"النهاردة\", \"دلوقتي\", \"الان\", \"حاليا\", \"احدث\","` | — |
| [SRC-686F71AA50-L000159](../../agents/task_understanding.py#L159) | 159 | `"        \"اخر الاخبار\", \"الاسعار الحاليه\", \"المواعيد الحاليه\", \"في الوقت الحالي\","` | — |
| [SRC-686F71AA50-L000160](../../agents/task_understanding.py#L160) | 160 | `"        \"today\", \"right now\", \"currently\", \"latest\", \"breaking news\", \"current price\","` | — |
| [SRC-686F71AA50-L000161](../../agents/task_understanding.py#L161) | 161 | `"        \"current hours\", \"this week\", \"this month\","` | — |
| [SRC-686F71AA50-L000162](../../agents/task_understanding.py#L162) | 162 | `"    ),"` | — |
| [SRC-686F71AA50-L000163](../../agents/task_understanding.py#L163) | 163 | `"    \"lead_generation\": ("` | — |
| [SRC-686F71AA50-L000164](../../agents/task_understanding.py#L164) | 164 | `"        \"عميل محتمل\", \"عملاء محتملين\", \"ابحث عن مشترين\", \"ابحث عن عميل\","` | — |
| [SRC-686F71AA50-L000165](../../agents/task_understanding.py#L165) | 165 | `"        \"دور على عملاء\", \"buyers looking to buy\", \"find prospects\", \"lead generation\","` | — |
| [SRC-686F71AA50-L000166](../../agents/task_understanding.py#L166) | 166 | `"        \"prospective customers\","` | — |
| [SRC-686F71AA50-L000167](../../agents/task_understanding.py#L167) | 167 | `"    ),"` | — |
| [SRC-686F71AA50-L000168](../../agents/task_understanding.py#L168) | 168 | `"    \"recommendation\": ("` | — |
| [SRC-686F71AA50-L000169](../../agents/task_understanding.py#L169) | 169 | `"        \"رشح\", \"ترشيح\", \"تنصحني\", \"هل اشتري\", \"اختار ايه\", \"افضل خيار\","` | — |
| [SRC-686F71AA50-L000170](../../agents/task_understanding.py#L170) | 170 | `"        \"recommend\", \"recommendation\", \"should i buy\", \"best option\", \"what should i choose\","` | — |
| [SRC-686F71AA50-L000171](../../agents/task_understanding.py#L171) | 171 | `"    ),"` | — |
| [SRC-686F71AA50-L000172](../../agents/task_understanding.py#L172) | 172 | `"    \"find_or_discover\": ("` | — |
| [SRC-686F71AA50-L000173](../../agents/task_understanding.py#L173) | 173 | `"        \"ابحث عن\", \"دور على\", \"دورلي على\", \"اعثر على\", \"هات رابط\", \"هاتلي\","` | — |
| [SRC-686F71AA50-L000174](../../agents/task_understanding.py#L174) | 174 | `"        \"فين الاقي\", \"اماكن بيع\", \"ابحث لي عن\", \"find\", \"search for\", \"look up\","` | — |
| [SRC-686F71AA50-L000175](../../agents/task_understanding.py#L175) | 175 | `"        \"where can i find\", \"list of\","` | — |
| [SRC-686F71AA50-L000176](../../agents/task_understanding.py#L176) | 176 | `"    ),"` | — |
| [SRC-686F71AA50-L000177](../../agents/task_understanding.py#L177) | 177 | `"    \"medical_information\": ("` | — |
| [SRC-686F71AA50-L000178](../../agents/task_understanding.py#L178) | 178 | `"        \"اعراض\", \"أعراض\", \"جرعة\", \"جرعات\", \"دواء\", \"ادوية\", \"علاج\", \"تشخيص\","` | — |
| [SRC-686F71AA50-L000179](../../agents/task_understanding.py#L179) | 179 | `"        \"medical symptoms\", \"dosage\", \"medicine\", \"medication\", \"treatment\", \"diagnosis\","` | — |
| [SRC-686F71AA50-L000180](../../agents/task_understanding.py#L180) | 180 | `"    ),"` | — |
| [SRC-686F71AA50-L000181](../../agents/task_understanding.py#L181) | 181 | `"    \"legal_information\": ("` | — |
| [SRC-686F71AA50-L000182](../../agents/task_understanding.py#L182) | 182 | `"        \"قانون\", \"قانوني\", \"نص قانوني\", \"عقد\", \"دعوى\", \"لائحة\", \"تشريع\","` | — |
| [SRC-686F71AA50-L000183](../../agents/task_understanding.py#L183) | 183 | `"        \"legal advice\", \"law\", \"contract\", \"lawsuit\", \"regulation\", \"legislation\","` | — |
| [SRC-686F71AA50-L000184](../../agents/task_understanding.py#L184) | 184 | `"    ),"` | — |
| [SRC-686F71AA50-L000185](../../agents/task_understanding.py#L185) | 185 | `"    \"coding_or_technical_design\": ("` | — |
| [SRC-686F71AA50-L000186](../../agents/task_understanding.py#L186) | 186 | `"        \"اكتب كود\", \"برمج\", \"كود بايثون\", \"اشرح الكود\", \"راجع الكود\","` | — |
| [SRC-686F71AA50-L000187](../../agents/task_understanding.py#L187) | 187 | `"        \"الكود التالي\", \"تصميم api\", \"اكتب سكربت\", \"code\", \"programming\","` | — |
| [SRC-686F71AA50-L000188](../../agents/task_understanding.py#L188) | 188 | `"        \"python code\", \"javascript\", \"api design\", \"stack trace\", \"unit test\","` | — |
| [SRC-686F71AA50-L000189](../../agents/task_understanding.py#L189) | 189 | `"        \"refactor\", \"debug this code\","` | — |
| [SRC-686F71AA50-L000190](../../agents/task_understanding.py#L190) | 190 | `"    ),"` | — |
| [SRC-686F71AA50-L000191](../../agents/task_understanding.py#L191) | 191 | `"    \"data_analysis\": ("` | — |
| [SRC-686F71AA50-L000192](../../agents/task_understanding.py#L192) | 192 | `"        \"حلل البيانات\", \"تحليل البيانات\", \"ملف csv\", \"تحليل جدول\", \"احسب المتوسط\","` | — |
| [SRC-686F71AA50-L000193](../../agents/task_understanding.py#L193) | 193 | `"        \"data analysis\", \"analyze data\", \"analyse data\", \"dataset\", \"spreadsheet\","` | — |
| [SRC-686F71AA50-L000194](../../agents/task_understanding.py#L194) | 194 | `"        \"csv file\", \"trend analysis\", \"calculate average\", \"pivot table\","` | — |
| [SRC-686F71AA50-L000195](../../agents/task_understanding.py#L195) | 195 | `"    ),"` | — |
| [SRC-686F71AA50-L000196](../../agents/task_understanding.py#L196) | 196 | `"    \"calculation\": ("` | — |
| [SRC-686F71AA50-L000197](../../agents/task_understanding.py#L197) | 197 | `"        \"احسب\", \"كم يساوي\", \"ما ناتج\", \"حساب النسبة\", \"احسب الفرق\","` | — |
| [SRC-686F71AA50-L000198](../../agents/task_understanding.py#L198) | 198 | `"        \"calculate\", \"compute\", \"what is the result\", \"percentage calculation\","` | — |
| [SRC-686F71AA50-L000199](../../agents/task_understanding.py#L199) | 199 | `"        \"how many\", \"how much is\","` | — |
| [SRC-686F71AA50-L000200](../../agents/task_understanding.py#L200) | 200 | `"    ),"` | — |
| [SRC-686F71AA50-L000201](../../agents/task_understanding.py#L201) | 201 | `"    \"translation\": ("` | — |
| [SRC-686F71AA50-L000202](../../agents/task_understanding.py#L202) | 202 | `"        \"ترجم\", \"ترجمة\", \"ترجم إلى\", \"ترجم للانجليزية\", \"ترجم للعربية\","` | — |
| [SRC-686F71AA50-L000203](../../agents/task_understanding.py#L203) | 203 | `"        \"translate\", \"translation\", \"translate into\", \"localize this\","` | — |
| [SRC-686F71AA50-L000204](../../agents/task_understanding.py#L204) | 204 | `"    ),"` | — |
| [SRC-686F71AA50-L000205](../../agents/task_understanding.py#L205) | 205 | `"    \"writing_or_editing\": ("` | — |
| [SRC-686F71AA50-L000206](../../agents/task_understanding.py#L206) | 206 | `"        \"اكتب\", \"اكتب رسالة\", \"اكتب بريد\", \"اعد صياغة\", \"أعد صياغة\","` | — |
| [SRC-686F71AA50-L000207](../../agents/task_understanding.py#L207) | 207 | `"        \"صحح لغويا\", \"راجع النص\", \"حسن الصياغة\", \"draft\", \"write\", \"rewrite\","` | — |
| [SRC-686F71AA50-L000208](../../agents/task_understanding.py#L208) | 208 | `"        \"proofread\", \"edit this\", \"polish this\", \"compose an email\","` | — |
| [SRC-686F71AA50-L000209](../../agents/task_understanding.py#L209) | 209 | `"    ),"` | — |
| [SRC-686F71AA50-L000210](../../agents/task_understanding.py#L210) | 210 | `"    \"planning\": ("` | — |
| [SRC-686F71AA50-L000211](../../agents/task_understanding.py#L211) | 211 | `"        \"ضع خطة\", \"خطة عمل\", \"خطة زمنية\", \"جدول زمني\", \"خطوات تنفيذ\","` | — |
| [SRC-686F71AA50-L000212](../../agents/task_understanding.py#L212) | 212 | `"        \"نظم لي\", \"رتب لي\", \"plan\", \"planning\", \"roadmap\", \"itinerary\","` | — |
| [SRC-686F71AA50-L000213](../../agents/task_understanding.py#L213) | 213 | `"        \"project schedule\", \"timeline\", \"project plan\","` | — |
| [SRC-686F71AA50-L000214](../../agents/task_understanding.py#L214) | 214 | `"    ),"` | — |
| [SRC-686F71AA50-L000215](../../agents/task_understanding.py#L215) | 215 | `"    \"creative_generation\": ("` | — |
| [SRC-686F71AA50-L000216](../../agents/task_understanding.py#L216) | 216 | `"        \"اكتب قصة\", \"قصة قصيرة\", \"قصيدة\", \"سيناريو\", \"اقترح افكار\","` | — |
| [SRC-686F71AA50-L000217](../../agents/task_understanding.py#L217) | 217 | `"        \"اقترح أفكار\", \"عصف ذهني\", \"brainstorm\", \"creative writing\","` | — |
| [SRC-686F71AA50-L000218](../../agents/task_understanding.py#L218) | 218 | `"        \"write a story\", \"poem\", \"generate ideas\","` | — |
| [SRC-686F71AA50-L000219](../../agents/task_understanding.py#L219) | 219 | `"    ),"` | — |
| [SRC-686F71AA50-L000220](../../agents/task_understanding.py#L220) | 220 | `"    \"explain_or_define\": ("` | — |
| [SRC-686F71AA50-L000221](../../agents/task_understanding.py#L221) | 221 | `"        \"ما معنى\", \"يعني ايه\", \"ما هو\", \"ما هي\", \"اشرح\", \"وضح مفهوم\","` | — |
| [SRC-686F71AA50-L000222](../../agents/task_understanding.py#L222) | 222 | `"        \"what is\", \"what does\", \"explain\", \"define\","` | — |
| [SRC-686F71AA50-L000223](../../agents/task_understanding.py#L223) | 223 | `"    ),"` | — |
| [SRC-686F71AA50-L000224](../../agents/task_understanding.py#L224) | 224 | `"    \"general_research\": ("` | — |
| [SRC-686F71AA50-L000225](../../agents/task_understanding.py#L225) | 225 | `"        \"بحث عميق\", \"بحث شامل\", \"بحث معمق\", \"تحقق من\", \"مصادر موثوقه\","` | — |
| [SRC-686F71AA50-L000226](../../agents/task_understanding.py#L226) | 226 | `"        \"اذكر المصادر\", \"مع مصادر\", \"بالمصادر\", \"deep research\", \"research\","` | — |
| [SRC-686F71AA50-L000227](../../agents/task_understanding.py#L227) | 227 | `"        \"verify\", \"fact check\", \"with sources\", \"cite sources\","` | — |
| [SRC-686F71AA50-L000228](../../agents/task_understanding.py#L228) | 228 | `"    ),"` | — |
| [SRC-686F71AA50-L000229](../../agents/task_understanding.py#L229) | 229 | `"    \"output_concise\": ("` | — |
| [SRC-686F71AA50-L000230](../../agents/task_understanding.py#L230) | 230 | `"        \"باختصار\", \"بإيجاز\", \"مختصر\", \"من غير إطالة\", \"بدون إطالة\","` | — |
| [SRC-686F71AA50-L000231](../../agents/task_understanding.py#L231) | 231 | `"        \"briefly\", \"in brief\", \"concise\", \"short answer\", \"keep it short\","` | — |
| [SRC-686F71AA50-L000232](../../agents/task_understanding.py#L232) | 232 | `"    ),"` | — |
| [SRC-686F71AA50-L000233](../../agents/task_understanding.py#L233) | 233 | `"    \"output_detailed\": ("` | — |
| [SRC-686F71AA50-L000234](../../agents/task_understanding.py#L234) | 234 | `"        \"بالتفصيل\", \"شرح وافي\", \"اشرح بالتفصيل\", \"خطوة بخطوة\","` | — |
| [SRC-686F71AA50-L000235](../../agents/task_understanding.py#L235) | 235 | `"        \"in detail\", \"step by step\", \"comprehensive explanation\", \"walkthrough\","` | — |
| [SRC-686F71AA50-L000236](../../agents/task_understanding.py#L236) | 236 | `"    ),"` | — |
| [SRC-686F71AA50-L000237](../../agents/task_understanding.py#L237) | 237 | `"    \"output_examples\": ("` | — |
| [SRC-686F71AA50-L000238](../../agents/task_understanding.py#L238) | 238 | `"        \"مع مثال\", \"امثلة\", \"مثال عملي\", \"بأمثلة\", \"for example\","` | — |
| [SRC-686F71AA50-L000239](../../agents/task_understanding.py#L239) | 239 | `"        \"give examples\", \"practical example\", \"worked example\","` | — |
| [SRC-686F71AA50-L000240](../../agents/task_understanding.py#L240) | 240 | `"    ),"` | — |
| [SRC-686F71AA50-L000241](../../agents/task_understanding.py#L241) | 241 | `"    \"output_table\": ("` | — |
| [SRC-686F71AA50-L000242](../../agents/task_understanding.py#L242) | 242 | `"        \"في جدول\", \"اعمل جدول\", \"جدول مقارنة\", \"as a table\", \"in a table\","` | — |
| [SRC-686F71AA50-L000243](../../agents/task_understanding.py#L243) | 243 | `"        \"comparison table\", \"tabulate\","` | — |
| [SRC-686F71AA50-L000244](../../agents/task_understanding.py#L244) | 244 | `"    ),"` | — |
| [SRC-686F71AA50-L000245](../../agents/task_understanding.py#L245) | 245 | `"    \"output_bullets\": ("` | — |
| [SRC-686F71AA50-L000246](../../agents/task_understanding.py#L246) | 246 | `"        \"نقاط\", \"على شكل نقاط\", \"قائمة\", \"bullet points\", \"as a list\","` | — |
| [SRC-686F71AA50-L000247](../../agents/task_understanding.py#L247) | 247 | `"        \"in bullets\", \"checklist\","` | — |
| [SRC-686F71AA50-L000248](../../agents/task_understanding.py#L248) | 248 | `"    ),"` | — |
| [SRC-686F71AA50-L000249](../../agents/task_understanding.py#L249) | 249 | `"    \"output_beginner_friendly\": ("` | — |
| [SRC-686F71AA50-L000250](../../agents/task_understanding.py#L250) | 250 | `"        \"ببساطة\", \"بشرح بسيط\", \"للمبتدئين\", \"من الصفر\", \"بلغة سهلة\","` | — |
| [SRC-686F71AA50-L000251](../../agents/task_understanding.py#L251) | 251 | `"        \"simple language\", \"beginner friendly\", \"beginner-friendly\","` | — |
| [SRC-686F71AA50-L000252](../../agents/task_understanding.py#L252) | 252 | `"        \"explain like i'm five\", \"eli5\","` | — |
| [SRC-686F71AA50-L000253](../../agents/task_understanding.py#L253) | 253 | `"    ),"` | — |
| [SRC-686F71AA50-L000254](../../agents/task_understanding.py#L254) | 254 | `"    \"output_citations\": ("` | — |
| [SRC-686F71AA50-L000255](../../agents/task_understanding.py#L255) | 255 | `"        \"مع مصادر\", \"اذكر المصادر\", \"مصادر موثوقة\", \"روابط مباشرة\","` | — |
| [SRC-686F71AA50-L000256](../../agents/task_understanding.py#L256) | 256 | `"        \"with sources\", \"cite sources\", \"include references\", \"with citations\","` | — |
| [SRC-686F71AA50-L000257](../../agents/task_understanding.py#L257) | 257 | `"    ),"` | — |
| [SRC-686F71AA50-L000258](../../agents/task_understanding.py#L258) | 258 | `"    \"output_links\": ("` | — |
| [SRC-686F71AA50-L000259](../../agents/task_understanding.py#L259) | 259 | `"        \"رابط مباشر\", \"روابط مباشرة\", \"هات الرابط\", \"لينك\", \"url\","` | — |
| [SRC-686F71AA50-L000260](../../agents/task_understanding.py#L260) | 260 | `"        \"direct link\", \"direct links\", \"include links\", \"source url\","` | — |
| [SRC-686F71AA50-L000261](../../agents/task_understanding.py#L261) | 261 | `"    ),"` | — |
| [SRC-686F71AA50-L000262](../../agents/task_understanding.py#L262) | 262 | `"    \"output_json\": ("` | — |
| [SRC-686F71AA50-L000263](../../agents/task_understanding.py#L263) | 263 | `"        \"بصيغة json\", \"تنسيق json\", \"return json\", \"output json\", \"as json\","` | — |
| [SRC-686F71AA50-L000264](../../agents/task_understanding.py#L264) | 264 | `"    ),"` | — |
| [SRC-686F71AA50-L000265](../../agents/task_understanding.py#L265) | 265 | `"}"` | — |
| [SRC-686F71AA50-L000266](../../agents/task_understanding.py#L266) | 266 | `""` | — |
| [SRC-686F71AA50-L000267](../../agents/task_understanding.py#L267) | 267 | `"_FRESHNESS_CUES = _PATTERNS[\"current_information\"]"` | — |
