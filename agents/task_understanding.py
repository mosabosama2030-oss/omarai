"""Deterministic, auditable natural-language task interpretation for Omarai.

This module produces a bounded TaskSpec and a query-strategy matrix. It does not
claim semantic certainty, generate facts, or execute tools. Signals and hypotheses
are diagnostics, never probabilities. Search plans remain subject to budgets,
source guardrails, and the final evidence checks.
"""
from __future__ import annotations

import re
import unicodedata
from typing import Any

MAX_TASK_CHARS = 4000
MAX_TASK_ASPECTS = 8
MAX_STRATEGY_QUERIES = 8
SUPPORTED_MODES = frozenset({"auto", "deep", "latest", "social"})

_ARABIC_DIACRITICS = re.compile(r"[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06ED]")
_PUNCTUATION = re.compile(r"[؟?!.،,؛;:(){}\[\]\"'«»]+")
_SPACE = re.compile(r"\s+")
_TOKEN_RE = re.compile(r"[a-z0-9]+|[\u0600-\u06FF]+", re.IGNORECASE)

_PATTERNS: dict[str, tuple[str, ...]] = {
    "official_site_lookup": (
        "الموقع الرسمي", "موقع رسمي", "رابط الموقع الرسمي", "الصفحه الرسميه",
        "الموقع الحكومي", "official website", "official site", "official homepage",
    ),
    "social_opinions": (
        "اراء الناس", "اراء المستخدمين", "تجارب الناس", "تجارب المستخدمين",
        "تجارب الملاك", "تجارب ملاك", "تجربة مالك", "مراجعات المستخدمين", "الناس بتقول ايه",
        "real user reviews", "owner experience", "customer opinions", "people's opinions",
        "user experiences", "what do owners say",
    ),
    "summarize": (
        "لخص", "تلخيص", "ملخص", "summarize", "summarise", "summary of",
    ),
    "troubleshoot": (
        "حل مشكلة", "عطل", "اعطال", "مش بيشتغل", "لا يعمل", "خطأ", "رساله خطأ",
        "اصلح", "استكشاف الاعطال", "troubleshoot", "debug", "does not work",
        "not working", "error message", "fix the problem", "common failures",
    ),
    "how_to": (
        "ازاي", "كيف", "طريقة", "خطوات", "اشرح لي كيف", "علمني", "كيفية",
        "how to", "steps to", "walk me through", "teach me",
    ),
    "compare": (
        "قارن", "مقارنه", "الفرق بين", "ايهما افضل", "مميزات وعيوب",
        "الايجابيات والسلبيات", "مفاضله", "compare", "comparison", "versus",
        "trade-offs", "pros and cons", "which is better",
    ),
    "current_information": (
        "اليوم", "النهارده", "النهاردة", "دلوقتي", "الان", "حاليا", "احدث",
        "اخر الاخبار", "الاسعار الحاليه", "المواعيد الحاليه", "في الوقت الحالي",
        "today", "right now", "currently", "latest", "breaking news", "current price",
        "current hours", "this week", "this month",
    ),
    "lead_generation": (
        "عميل محتمل", "عملاء محتملين", "ابحث عن مشترين", "ابحث عن عميل",
        "دور على عملاء", "buyers looking to buy", "find prospects", "lead generation",
        "prospective customers",
    ),
    "recommendation": (
        "رشح", "ترشيح", "تنصحني", "هل اشتري", "اختار ايه", "افضل خيار",
        "recommend", "recommendation", "should i buy", "best option", "what should i choose",
    ),
    "find_or_discover": (
        "ابحث عن", "دور على", "دورلي على", "اعثر على", "هات رابط", "هاتلي",
        "فين الاقي", "اماكن بيع", "ابحث لي عن", "find", "search for", "look up",
        "where can i find", "list of",
    ),
    "explain_or_define": (
        "ما معنى", "يعني ايه", "ما هو", "ما هي", "اشرح", "وضح مفهوم",
        "what is", "what does", "explain", "define",
    ),
    "general_research": (
        "بحث عميق", "بحث شامل", "بحث معمق", "تحقق من", "مصادر موثوقه",
        "اذكر المصادر", "مع مصادر", "بالمصادر", "deep research", "research",
        "verify", "fact check", "with sources", "cite sources",
    ),
}

_FRESHNESS_CUES = _PATTERNS["current_information"]
_SOCIAL_CUES = _PATTERNS["social_opinions"]
_LOCATION_CUES = (
    "في مصر", "داخل مصر", "بالقاهرة", "في القاهره", "بالاسكندريه", "في السعودية",
    "في الامارات", "in egypt", "within egypt", "in cairo", "in saudi arabia",
    "in the uae", "in the united states", "in the uk",
)
_OFFICIAL_WORDS = ("وزارة", "هيئة حكومية", "جهة حكومية", "مصلحة حكومية", "ministry", "government agency")
_YEAR_RE = re.compile(r"(?<!\d)(?:19\d{2}|20\d{2})(?!\d)")
_DATE_RE = re.compile(r"(?<!\d)(?:\d{4}-\d{2}-\d{2}|\d{1,2}[/-]\d{1,2}[/-]\d{2,4})(?!\d)")
_URL_RE = re.compile(r"https?://[^\s<>]+", re.IGNORECASE)
_BUDGET_RE = re.compile(
    r"(?:ميزاني(?:ة|تي)(?:\s+(?:اقل\s+من|بحد\s+اقصى|في\s+حدود))?"
    r"|بحد\s+اقصى|اقل\s+من|في\s+حدود|budget(?:\s+of)?|under|below|up\s+to)"
    r"\s*[:：]?\s*(?:egp|usd|eur|جنيه|دولار|ريال)?\s*[\d,.\u0660-\u0669]+"
    r"(?:\s*(?:الف|ألف|مليون|thousand|million|k))?",
    re.IGNORECASE,
)
_FOLLOWUP_CUES = (
    "سعرها", "سعره", "قارنهم", "بينهم", "ما رايك فيها", "هل هي كويسه",
    "what about it", "compare them", "is it good", "should i buy it",
    "its price", "the warranty",
)
_QUERY_STOP = re.compile(
    r"\b(?:من حيث|in terms of|taking into account|with respect to)\b.*$",
    re.IGNORECASE,
)


def normalize_text(value: Any) -> str:
    """Normalize orthographic variation for matching; preserve the original elsewhere."""
    if not isinstance(value, str):
        return ""
    text = unicodedata.normalize("NFKC", value).casefold()
    text = _ARABIC_DIACRITICS.sub("", text)
    text = text.replace("ـ", "").translate(str.maketrans({
        "أ": "ا", "إ": "ا", "آ": "ا", "ٱ": "ا", "ى": "ي", "ة": "ه",
    }))
    return _SPACE.sub(" ", _PUNCTUATION.sub(" ", text)).strip()


def _contains(text: str, phrases: tuple[str, ...]) -> list[str]:
    """Match phrases on token boundaries and only strip known Arabic clitics/suffixes.

    This deliberately avoids substring collisions such as "الان" (now) inside
    "الانذار" (alarm), while retaining common forms such as "سعرها" and "قارنهم".
    """
    tokens = _TOKEN_RE.findall(text)
    matched: list[str] = []
    prefixes = ("وال", "بال", "فال", "كال", "لل", "ال", "و", "ف", "ب", "ل", "ك")
    suffixes = ("هما", "هم", "هن", "ها", "ه", "كم", "كن", "ك", "نا", "ني")
    english_suffixes = ("ing", "ed", "es", "s")
    for phrase in phrases:
        normalized = normalize_text(phrase)
        phrase_tokens = _TOKEN_RE.findall(normalized)
        if not phrase_tokens:
            continue
        found = False
        width = len(phrase_tokens)
        for index in range(max(0, len(tokens) - width + 1)):
            segment = tokens[index:index + width]
            if [token.casefold() for token in segment] == [token.casefold() for token in phrase_tokens]:
                found = True
                break
        if not found and width == 1:
            target = phrase_tokens[0].casefold()
            for original_token in tokens:
                token = original_token.casefold()
                forms = {token}
                changed = True
                while changed:
                    changed = False
                    for prefix in prefixes:
                        if token.startswith(prefix) and len(token) - len(prefix) >= 3:
                            token = token[len(prefix):]
                            forms.add(token)
                            changed = True
                            break
                for candidate in list(forms):
                    for suffix in suffixes:
                        if candidate.endswith(suffix) and len(candidate) - len(suffix) >= 3:
                            forms.add(candidate[:-len(suffix)])
                if target in forms:
                    found = True
                    break
                if target.isascii() and len(target) >= 4 and original_token.isascii():
                    if any(token.endswith(suffix) and token[:-len(suffix)] == target for suffix in english_suffixes):
                        found = True
                        break
        if found and normalized not in matched:
            matched.append(normalized)
    return matched


def _extract_explicit_locations(question: str) -> list[str]:
    """Return only a small, explicit location vocabulary; never infer geolocation."""
    normalized = normalize_text(question)
    known = (
        ("مصر", ("في مصر", "داخل مصر", "المصري", "المصرية", "مصر", "egypt", "egyptian")),
        ("القاهرة", ("القاهرة", "القاهره", "cairo")),
        ("الإسكندرية", ("الاسكندرية", "الاسكندريه", "alexandria")),
        ("السعودية", ("السعودية", "السعوديه", "saudi arabia")),
        ("الإمارات", ("الامارات", "uae", "united arab emirates")),
        ("المملكة المتحدة", ("المملكة المتحدة", "united kingdom", "the uk")),
        ("الولايات المتحدة", ("الولايات المتحدة", "united states", "the us")),
    )
    result: list[str] = []
    for canonical, cues in known:
        if any(normalize_text(cue) in normalized for cue in cues):
            result.append(canonical)
    return result


def _language_profile(question: str) -> str:
    arabic = len(re.findall(r"[\u0600-\u06FF]", question))
    latin = len(re.findall(r"[A-Za-z]", question))
    if arabic and latin:
        return "mixed"
    if arabic:
        return "ar"
    if latin:
        return "en"
    return "und"


def _primary_family(matches: dict[str, list[str]], mode: str, route: str, normalized: str) -> str:
    # An explicit official-destination request is different from a request for an
    # article mentioning the organization; government verification is a separate slot.
    if matches["official_site_lookup"]:
        return "official_site_lookup"
    for family in (
        "social_opinions", "summarize", "troubleshoot", "compare",
        "lead_generation", "how_to", "recommendation", "current_information",
        "find_or_discover", "explain_or_define", "general_research",
    ):
        if matches.get(family):
            return family
    if route == "CLARIFY":
        return "ambiguous_or_incomplete"
    if route in {"WEB_SIMPLE", "WEB_DEEP", "LEAD_GENERATION"} or mode != "auto":
        return "web_research"
    return "general_question"


def build_task_spec(
    question: str,
    *,
    mode: str = "auto",
    intent_route: str = "",
    plan: dict[str, Any] | None = None,
    dialogue_context: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Build a bounded task specification, interpretation hypotheses, and test matrix."""
    raw = question if isinstance(question, str) else ""
    raw = raw[:MAX_TASK_CHARS]
    normalized = normalize_text(raw)
    clean_mode = mode.strip().lower() if isinstance(mode, str) else "auto"
    if clean_mode not in SUPPORTED_MODES:
        clean_mode = "auto"
    matches = {family: _contains(normalized, phrases) for family, phrases in _PATTERNS.items()}
    aspect_values: list[str] = []
    try:
        from agents.aspect_planning import extract_aspects
        aspect_values = extract_aspects(raw)[:MAX_TASK_ASPECTS]
    except (ImportError, TypeError, ValueError):
        aspect_values = []

    official_destination = bool(matches["official_site_lookup"])
    government_official_site = bool(
        official_destination
        and any(normalize_text(word) in normalized for word in _OFFICIAL_WORDS)
    )
    navigation = official_destination or bool(
        _URL_RE.search(raw)
        or any(normalize_text(term) in normalized for term in ("هات رابط", "website", "homepage"))
    )
    explicit_freshness = bool(_contains(normalized, _FRESHNESS_CUES))
    current_required = (clean_mode == "latest" or explicit_freshness) and not navigation
    social_required = clean_mode == "social" or bool(matches["social_opinions"])
    family = _primary_family(matches, clean_mode, intent_route, normalized)

    if family == "official_site_lookup":
        evidence_requirements = [
            "target_entity_match",
            "official_domain_or_independently_linked_official_destination",
            "never_substitute_an_article_or_unrelated_directory",
        ]
        query_strategies = ["exact_entity", "official_domain", "government_portal_cross_check"]
    elif family == "social_opinions":
        evidence_requirements = [
            "public_social_platform_url",
            "original_post_or_readable_post_content_when_available",
            "heuristic_classification_is_not_identity_or_truth_verification",
        ]
        query_strategies = ["topic_platform", "personal_experience", "discussion", "commercial_exclusion"]
    elif family == "summarize":
        evidence_requirements = [
            "read_the_requested_text_or_page",
            "do_not_summarize_unread_content_from_title_only",
            "preserve_source_scope_and_important_qualifiers",
        ]
        query_strategies = ["exact_url_or_supplied_text", "page_read", "scope_preserving_summary"]
    elif family == "troubleshoot":
        evidence_requirements = [
            "preserve_error_message_and_environment",
            "prefer_manual_or_primary_technical_source",
            "separate_diagnosis_hypotheses_from_confirmed_cause",
        ]
        query_strategies = ["symptom_exact_text", "cause_hypotheses", "official_manual", "safe_remedy"]
    elif family == "compare":
        evidence_requirements = [
            "preserve_each_explicit_comparison_criterion",
            "source_support_for_each_material_comparison",
            "distinguish_primary_specs_from_individual_experience",
        ]
        query_strategies = ["topic_baseline", "one_query_per_criterion", "primary_specification", "independent_comparison"]
    elif family == "how_to":
        evidence_requirements = [
            "ordered_actionable_steps",
            "surface prerequisites and safety constraints",
            "distinguish general guidance from product-specific instructions",
        ]
        query_strategies = ["goal_exact_match", "official_guide", "stepwise_method"]
    elif family == "lead_generation":
        evidence_requirements = [
            "public_buyer_intent_signal",
            "do_not_treat_listing_or_ad_as_a_buyer",
            "identity_not_verified_without_separate_evidence",
        ]
        query_strategies = ["buyer_intent_phrase", "public_discussion", "recent_signal"]
    elif family == "recommendation":
        evidence_requirements = [
            "preserve_budget_location_and_use_case_if_explicit",
            "compare_alternatives",
            "make_tradeoffs_and_missing_information_visible",
        ]
        query_strategies = ["use_case", "budget_and_location", "pros_cons", "alternatives"]
    else:
        evidence_requirements = [
            "match_sources_to_the_question",
            "distinguish_search_snippet_from_read_page",
            "cite_material_web_claims",
        ]
        query_strategies = ["exact_topic", "primary_source", "cross_check_if_needed"]

    # Source freshness, requested officiality, and social evidence are orthogonal
    # constraints. Preserve them even when another intent is the primary family.
    if current_required and not official_destination:
        evidence_requirements.extend([
            "publication_or_update_date",
            "page_text_successfully_read",
            "prefer_primary_current_source",
            "do_not_use_stale_page_as_current_proof",
        ])
        query_strategies.extend(["recent_official_update", "primary_source", "date_check"])
    if social_required and family != "social_opinions":
        evidence_requirements.extend([
            "public_social_platform_url",
            "separate_personal_experience_from_promotion",
            "heuristic_classification_is_not_identity_or_truth_verification",
        ])
        query_strategies.extend(["personal_experience", "discussion", "commercial_exclusion"])
    if official_destination and family != "official_site_lookup":
        evidence_requirements.extend([
            "distinguish_official_destination_from_mentions_or_articles",
            "do_not_claim_domain_ownership_without_independent_evidence",
        ])
        query_strategies.extend(["official_domain", "government_portal_cross_check"])
    if "compare" in matches and family != "compare":
        evidence_requirements.extend([
            "preserve_explicit_comparison_criteria",
            "do_not_collapse_multiple_dimensions_into_one_generic_answer",
        ])
        query_strategies.extend(["one_query_per_criterion", "independent_comparison"])
    if len(explicit_aspects := aspect_values) > 1:
        evidence_requirements.append("track_evidence_coverage_per_explicit_aspect")
        query_strategies.append("one_query_per_criterion")
    query_strategies = list(dict.fromkeys(query_strategies))
    evidence_requirements = list(dict.fromkeys(evidence_requirements))

    location = _extract_explicit_locations(raw)
    years = list(dict.fromkeys(_YEAR_RE.findall(raw)))
    dates = list(dict.fromkeys(_DATE_RE.findall(raw)))
    budgets = [m.group(0).strip()[:100] for m in _BUDGET_RE.finditer(raw)]
    urls = list(dict.fromkeys(_URL_RE.findall(raw)))[:5]
    unresolved_followup = any(normalize_text(cue) in normalized for cue in _FOLLOWUP_CUES)
    context = dialogue_context if isinstance(dialogue_context, dict) else {}
    explicit_aspects = list(dict.fromkeys(aspect_values))[:MAX_TASK_ASPECTS]

    # Hypotheses are alternatives considered by the deterministic classifier. Counts
    # are matched lexical signals, not calibrated confidence or probability.
    hypothesis_rows: list[dict[str, Any]] = []
    for candidate_family, signals in matches.items():
        if signals:
            hypothesis_rows.append({
                "family": candidate_family,
                "matched_signal_count": len(signals),
                "signals": signals[:4],
                "status": "candidate_interpretation",
            })
    hypothesis_rows.sort(
        key=lambda item: (-item["matched_signal_count"], item["family"])
    )
    for item in hypothesis_rows:
        item["selected"] = item["family"] == family
    if len(hypothesis_rows) > 8:
        hypothesis_rows = hypothesis_rows[:8]

    # A conflict is a reason to preserve alternatives in diagnostics, not a reason to
    # invent certainty. High ambiguity is limited to unresolved references or a
    # short fragment explicitly marked as contextual.
    unresolved = bool(context.get("needs_clarification")) or (
        len(raw.strip()) <= 28 and unresolved_followup
        and not context.get("resolved_question")
    )
    if unresolved:
        ambiguity_status = "needs_clarification"
    elif len(hypothesis_rows) >= 3:
        ambiguity_status = "multiple_overlapping_signals"
    elif len(hypothesis_rows) == 2:
        ambiguity_status = "some_intent_overlap"
    else:
        ambiguity_status = "no_strong_lexical_conflict_detected"

    tools: list[str] = []
    if intent_route in {"WEB_SIMPLE", "WEB_DEEP", "LEAD_GENERATION"} or clean_mode != "auto":
        tools.append("web_search")
    if urls or navigation or family == "summarize":
        tools.append("page_fetch")
    if social_required:
        tools.append("public_social_search_if_configured")
    if intent_route != "LOCAL":
        tools.append("language_model_generation_if_configured")
    if tools and ("web_search" in tools or social_required):
        tools.append("claim_review_if_configured")
    constraints = {
        "explicit_locations": location,
        "explicit_years": years,
        "explicit_dates": dates,
        "explicit_budgets": budgets,
        "explicit_urls": urls,
        "explicit_aspects": explicit_aspects,
        "time_sensitive_request": current_required,
        "official_site_required": government_official_site,
        "official_destination_required": official_destination,
        "social_evidence_requested": social_required,
        "language_profile": _language_profile(raw),
        "source_policy": (
            "government_official_destination" if government_official_site
            else "official_destination" if official_destination
            else "current_read_page" if current_required
            else "public_social_content" if social_required
            else "task_relevant_sources"
        ),
    }
    spec = {
        "schema": "omarai.task_spec.v1",
        "task_family": family,
        "mode": clean_mode,
        "intent_route": intent_route or "unassessed",
        "normalization": "unicode_nfkc_arabic_diacritic_and_letter_normalization",
        "classification_method": "deterministic_multi_pattern_hypotheses",
        "classification_is_probability": False,
        "ambiguity_status": ambiguity_status,
        "hypothesis_interpretations": hypothesis_rows,
        "constraints": constraints,
        "evidence_requirements": evidence_requirements,
        "query_strategies": query_strategies,
        "tool_requirements": list(dict.fromkeys(tools)),
        "decision_checks": [
            "resolve_context_without_carrying_stale_topic",
            "preserve_explicit_entities_and_constraints",
            "validate_topic_relevance",
            "apply_mode_specific_source_guardrails",
            "distinguish_search_result_snippet_from_read_page",
            "report_each_failed_stage",
            "cite_claims_or_abstain_when_evidence_is_insufficient",
        ],
        "limits": {
            "max_question_chars": MAX_TASK_CHARS,
            "max_aspects": MAX_TASK_ASPECTS,
            "max_query_strategies": MAX_STRATEGY_QUERIES,
        },
        "claim": "task planning metadata only; not semantic certainty or factual verification",
    }
    if plan and isinstance(plan, dict):
        spec["planner_freshness"] = str(plan.get("freshness") or "unknown")
        spec["planner_depth"] = str(plan.get("depth") or "unknown")
    return spec


def _query_key(value: str) -> str:
    return normalize_text(value)


def _generated_strategy_candidates(topic: str, spec: dict[str, Any]) -> list[tuple[str, str, str]]:
    family = str(spec.get("task_family") or "")
    constraints = spec.get("constraints") if isinstance(spec.get("constraints"), dict) else {}
    aspects = constraints.get("explicit_aspects") if isinstance(constraints.get("explicit_aspects"), list) else []
    candidates: list[tuple[str, str, str]] = []
    if not topic.strip():
        return candidates
    locations = constraints.get("explicit_locations") or []
    location_suffix = " ".join(str(item) for item in locations[:2])
    hypotheses = spec.get("hypothesis_interpretations")
    hypothesis_families = {
        str(item.get("family"))
        for item in hypotheses
        if isinstance(item, dict) and item.get("family")
    } if isinstance(hypotheses, list) else set()
    if family == "official_site_lookup" or constraints.get("official_destination_required"):
        candidates.extend([
            (f"{topic} الموقع الرسمي", "official_destination", "exact official-site discovery"),
            (f"{topic} official website government portal", "official_domain", "cross-language destination discovery"),
        ])
    if constraints.get("time_sensitive_request"):
        candidates.extend([
            (f"{topic} تحديث رسمي حديث {location_suffix}".strip(), "recent_official_update", "current-state fact requires fresh primary evidence"),
            (f"{topic} latest official update {location_suffix}".strip(), "recent_official_update_en", "alternate language and source wording"),
        ])
    if family == "social_opinions" or constraints.get("social_evidence_requested"):
        candidates.extend([
            (f"{topic} تجارب مستخدمين آراء الملاك {location_suffix}".strip(), "personal_experience_ar", "search for first-person experience rather than generic product mentions"),
            (f"{topic} owner experience review {location_suffix}".strip(), "personal_experience_en", "cross-language owner-experience discovery"),
            (f"{topic} common complaints discussion", "discussion_and_complaints", "look for contrasting experiences and discussions"),
        ])
    if family == "compare" or "compare" in hypothesis_families:
        for aspect in aspects[:MAX_TASK_ASPECTS]:
            candidates.append((f"{topic} {aspect}", "explicit_criterion", f"separate evidence retrieval for criterion: {aspect}"))
        candidates.extend([
            (f"{topic} official specifications", "primary_specification", "separate technical specifications from opinion"),
            (f"{topic} independent comparison pros cons", "independent_comparison", "seek comparative analysis and trade-offs"),
        ])
    if family == "troubleshoot" or "troubleshoot" in hypothesis_families:
        candidates.extend([
            (f"{topic} الأعطال الشائعة الأسباب والحلول", "failure_modes_ar", "search causes and remedies without treating hypotheses as confirmed"),
            (f"{topic} troubleshooting common failures official manual", "failure_modes_en", "technical cross-language search and primary manual"),
        ])
    if family == "how_to" or "how_to" in hypothesis_families:
        candidates.extend([
            (f"{topic} خطوات شرح دليل رسمي", "procedural_guide_ar", "seek stepwise procedure and applicable prerequisites"),
            (f"{topic} official guide steps", "procedural_guide_en", "cross-language guide discovery"),
        ])
    if family == "recommendation" or "recommendation" in hypothesis_families:
        candidates.extend([
            (f"{topic} المميزات العيوب البدائل", "tradeoffs_ar", "compare trade-offs and alternatives"),
            (f"{topic} pros cons alternatives review", "tradeoffs_en", "cross-language alternatives discovery"),
        ])
    if family == "lead_generation" or "lead_generation" in hypothesis_families:
        candidates.extend([
            (f"{topic} شخص يبحث عن شراء تجربة سؤال", "buyer_intent_ar", "distinguish explicit buyer intent from product advertisements"),
            (f"{topic} looking to buy seeking recommendations", "buyer_intent_en", "search public discussions for intent signals"),
        ])
    if family in {"general_research", "web_research", "find_or_discover"}:
        candidates.extend([
            (f"{topic} مصدر رسمي", "primary_source_ar", "prefer an original or primary source when appropriate"),
            (f"{topic} official source report", "primary_source_en", "alternate source-oriented search wording"),
            (f"{topic} limitations risks independent analysis", "independent_analysis", "seek counterevidence and limitations"),
        ])
    if not candidates and family not in {"general_question", "ambiguous_or_incomplete"}:
        candidates.append(
            (f"{topic} مصدر موثوق", "source_oriented_alternative", "search wording is a hypothesis, not evidence")
        )
    return candidates


def build_query_strategy_matrix(
    question: str,
    task_spec: dict[str, Any],
    existing_queries: Any,
    *,
    limit: int = MAX_STRATEGY_QUERIES,
    compact_fn: Any = None,
) -> list[dict[str, str]]:
    """Annotate existing plan queries and add bounded, task-specific search strategies."""
    maximum = max(1, min(int(limit), MAX_STRATEGY_QUERIES))
    spec = task_spec if isinstance(task_spec, dict) else {}
    queries = existing_queries if isinstance(existing_queries, list) else []
    rows: list[dict[str, str]] = []
    seen: set[str] = set()

    def add(query: Any, strategy: str, rationale: str) -> None:
        if not isinstance(query, str) or not query.strip() or len(rows) >= maximum:
            return
        candidate = query.strip()
        if compact_fn is not None:
            try:
                candidate = compact_fn(candidate) or ""
            except (TypeError, ValueError):
                candidate = ""
        candidate = _SPACE.sub(" ", candidate).strip()[:240]
        key = _query_key(candidate)
        if not candidate or not key or key in seen:
            return
        # Avoid creating modifier-only queries after a topic was lost upstream.
        topic_tokens = _TOKEN_RE.findall(_query_key(str(queries[0])) if queries else _query_key(question))
        query_tokens = _TOKEN_RE.findall(key)
        if len(topic_tokens) >= 2 and not any(token in query_tokens for token in topic_tokens[:3]):
            return
        seen.add(key)
        rows.append({"query": candidate, "strategy": strategy, "rationale": rationale})

    for index, query in enumerate(queries):
        strategy = "planner_seed" if index == 0 else "planner_alternative"
        rationale = "validated existing planner query; no independent quality claim"
        add(query, strategy, rationale)
    if not rows and (
        spec.get("ambiguity_status") == "needs_clarification"
        or spec.get("task_family") == "ambiguous_or_incomplete"
    ):
        return rows
    base = str(queries[0]).strip() if queries and isinstance(queries[0], str) else ""
    if not base:
        base = re.sub(
            r"^(?:من فضلك|لو سمحت|ابحث لي|ابحث|دورلي|دور|اعثر على|please|search for|find|look up)\s*",
            "", str(question or "").strip(), flags=re.IGNORECASE,
        )
    base = _QUERY_STOP.sub("", base).strip(" \t\r\n-،,؛;")
    if not base:
        return rows
    for query, strategy, rationale in _generated_strategy_candidates(base, spec):
        add(query, strategy, rationale)
        if len(rows) >= maximum:
            break
    return rows


def validate_task_spec(value: Any) -> dict[str, Any]:
    """Return a safe bounded public representation of TaskSpec-like input."""
    if not isinstance(value, dict) or value.get("schema") != "omarai.task_spec.v1":
        return {
            "schema": "omarai.task_spec.v1",
            "status": "not_available",
            "claim": "no validated task specification supplied",
        }
    # Rebuild via the allowlisted JSON-friendly fields rather than passing arbitrary
    # planner/model content through the diagnostics surface.
    spec = {
        "schema": "omarai.task_spec.v1",
        "task_family": str(value.get("task_family") or "general_question")[:80],
        "mode": str(value.get("mode") or "auto")[:20],
        "intent_route": str(value.get("intent_route") or "unassessed")[:40],
        "classification_method": str(value.get("classification_method") or "")[:100],
        "classification_is_probability": False,
        "ambiguity_status": str(value.get("ambiguity_status") or "unassessed")[:80],
        "constraints": value.get("constraints") if isinstance(value.get("constraints"), dict) else {},
        "evidence_requirements": value.get("evidence_requirements") if isinstance(value.get("evidence_requirements"), list) else [],
        "query_strategies": value.get("query_strategies") if isinstance(value.get("query_strategies"), list) else [],
        "tool_requirements": value.get("tool_requirements") if isinstance(value.get("tool_requirements"), list) else [],
        "decision_checks": value.get("decision_checks") if isinstance(value.get("decision_checks"), list) else [],
        "hypothesis_interpretations": value.get("hypothesis_interpretations") if isinstance(value.get("hypothesis_interpretations"), list) else [],
        "claim": "task planning metadata only; not semantic certainty or factual verification",
    }
    return spec
