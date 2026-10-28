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
    "output_concise": (
        "باختصار", "بإيجاز", "مختصر", "من غير إطالة", "بدون إطالة",
        "briefly", "in brief", "concise", "short answer", "keep it short",
    ),
    "output_detailed": (
        "بالتفصيل", "شرح وافي", "اشرح بالتفصيل", "خطوة بخطوة",
        "in detail", "step by step", "comprehensive explanation", "walkthrough",
    ),
    "output_examples": (
        "مع مثال", "امثلة", "مثال عملي", "بأمثلة", "for example",
        "give examples", "practical example", "worked example",
    ),
    "output_table": (
        "في جدول", "اعمل جدول", "جدول مقارنة", "as a table", "in a table",
        "comparison table", "tabulate",
    ),
    "output_bullets": (
        "نقاط", "على شكل نقاط", "قائمة", "bullet points", "as a list",
        "in bullets", "checklist",
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
    r"(?:ميزاني(?:ة|تي)(?:\s+(?:(?:أقل|اقل)\s+من|بحد\s+اقصى|في\s+حدود))?"
    r"|بحد\s+اقصى|(?:أقل|اقل)\s+من|في\s+حدود|budget(?:\s+of)?|under|below|up\s+to)"
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
                for candidate in forms.copy():
                    for suffix in suffixes:
                        if candidate.endswith(suffix) and len(candidate) - len(suffix) >= 3:
                            forms.add(candidate[:-len(suffix)])
                if target in forms:
                    found = True
                    break
                if (
                    target.isascii()
                    and len(target) >= 4
                    and original_token.isascii()
                    and any(
                        token.endswith(suffix) and token[:-len(suffix)] == target
                        for suffix in english_suffixes
                    )
                ):
                    found = True
                    break
        if found and normalized not in matched:
            matched.append(normalized)
    return matched


def _has_inline_summary_text(question: str) -> bool:
    """Detect explicitly supplied summary text without treating a URL as pasted content."""
    if not isinstance(question, str) or _URL_RE.search(question):
        return False
    normalized = normalize_text(question)
    markers = (
        "النص التالي", "النص الاتي", "النص ده", "النص اللي جاي",
        "المحتوى التالي", "هذا النص", "following text", "the following text",
        "text below", "content below", "this text",
    )
    for marker in markers:
        candidate = normalize_text(marker)
        if candidate and candidate in normalized:
            remainder = normalized.split(candidate, 1)[1].strip()
            if len(remainder) >= 8:
                return True
    return bool(
        re.search(
            r"^\s*(?:لخص(?:\s+لي)?|تلخيص|summari[sz]e|summary)\s*[:：]\s*\S.{12,}$",
            question,
            flags=re.IGNORECASE,
        )
    )


def _has_official_site_target(question: str) -> bool:
    """Conservatively check whether an official-site request names a target."""
    normalized = normalize_text(question)
    for phrase in _PATTERNS["official_site_lookup"]:
        normalized = normalized.replace(normalize_text(phrase), " ")
    action_phrases = (
        "من فضلك", "لو سمحت", "اريد", "عايز", "عاوزه", "ابحث لي عن",
        "ابحث عن", "هات لي", "هاتلي", "هات", "اعثر على", "دور على", "دورلي على",
        "find", "search for", "look up", "please", "can you", "could you", "get me",
        "the", "of", "for", "government",
    )
    for phrase in action_phrases:
        normalized = re.sub(
            rf"(?<!\w){re.escape(normalize_text(phrase))}(?!\w)", " ", normalized
        )
    generic_target_words = {
        "الموقع", "موقع", "الرابط", "رابط", "لينك", "الصفحه", "صفحه",
        "رسمي", "الرسمي", "الرسمى", "حكومي", "الحكومي",
        "وزاره", "هيئه", "جهة", "جهه", "حكوميه",
        "شركه", "الشركه", "مؤسسه", "المؤسسه", "بنك", "البنك",
        "منظمه", "المنظمه", "مصلحه", "المصلحه", "اداره", "الاداره",
        "وزارة", "شركة", "الشركة", "مؤسسة", "الهيئة", "الحكومية",
        "website", "site", "homepage", "official", "ministry", "agency",
        "department", "organization", "organisation", "company", "bank",
        "authority", "portal", "url", "link", "gov", "the",
    }
    ignored = {normalize_text(word) for word in generic_target_words}
    for raw_token in _TOKEN_RE.findall(normalized):
        token = normalize_text(raw_token)
        changed = True
        while changed:
            changed = False
            for prefix in ("وال", "بال", "فال", "كال", "لل", "ال", "و", "ف", "ب", "ل", "ك"):
                if token.startswith(prefix) and len(token) - len(prefix) >= 3:
                    token = token[len(prefix):]
                    changed = True
                    break
        if token and token not in ignored and len(token) >= 2:
            return True
    return False


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
        if any(_contains(normalized, (cue,)) for cue in cues):
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
    matches = {
        family: _contains(normalized, phrases)
        for family, phrases in _PATTERNS.items()
        if not family.startswith("output_")
    }
    output_matches = {
        family: _contains(normalized, phrases)
        for family, phrases in _PATTERNS.items()
        if family.startswith("output_")
    }
    aspect_values: list[str] = []
    try:
        from agents.aspect_planning import extract_aspects
        aspect_values = extract_aspects(raw)[:MAX_TASK_ASPECTS]
    except (ImportError, TypeError, ValueError):
        aspect_values = []

    official_destination = bool(matches["official_site_lookup"])
    government_official_site = bool(
        official_destination
        and bool(_contains(normalized, _OFFICIAL_WORDS))
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
    inline_summary_text = _has_inline_summary_text(raw)
    unresolved_followup = any(normalize_text(cue) in normalized for cue in _FOLLOWUP_CUES)
    missing_required_inputs: list[str] = []
    if intent_route == "CLARIFY":
        missing_required_inputs.append("unresolved_referent_or_incomplete_request")
    if official_destination and not _has_official_site_target(raw):
        missing_required_inputs.append("official_destination_target_entity")
    if family == "summarize" and not urls and not inline_summary_text:
        missing_required_inputs.append("summary_source_url_or_pasted_text")
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
    unresolved = bool(missing_required_inputs) or bool(context.get("needs_clarification")) or (
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

    # Tool requirements are advisory planning metadata, not executable permission.
    # A clarification route is a hard stop even when the UI has a research mode selected.
    route_is_clarification = intent_route == "CLARIFY"
    route_is_local = intent_route == "LOCAL"
    search_requested = (
        intent_route in {"WEB_SIMPLE", "WEB_DEEP", "LEAD_GENERATION"}
        or (
            intent_route == "deterministic_fallback"
            and isinstance(plan, dict)
            and bool(plan.get("queries"))
        )
        or (
            intent_route not in {"LOCAL", "CLARIFY", "BUDGET_EXHAUSTED"}
            and (
                social_required
                or official_destination
                or current_required
                or family in {"find_or_discover", "lead_generation", "general_research"}
                or (
                    family == "compare"
                    and not inline_summary_text
                )
            )
        )
        or (
            clean_mode != "auto"
            and not route_is_clarification
            and not route_is_local
        )
    )
    page_fetch_requested = bool(urls) or (
        family == "summarize"
        and not inline_summary_text
        and not route_is_clarification
    )
    tools: list[str] = []
    if search_requested and not route_is_clarification:
        tools.append("web_search")
    if page_fetch_requested and not route_is_clarification:
        tools.append("page_fetch")
    if social_required and not route_is_clarification:
        tools.append("public_social_search_if_configured")
    if (
        intent_route in {"MODEL_ONLY", "WEB_SIMPLE", "WEB_DEEP", "LEAD_GENERATION", "deterministic_fallback"}
        or (clean_mode != "auto" and not route_is_clarification and not route_is_local)
    ):
        tools.append("language_model_generation_if_configured")
    if tools and ("web_search" in tools or social_required) and not route_is_clarification:
        tools.append("claim_review_if_configured")
    constraints = {
        "explicit_locations": location,
        "explicit_years": years,
        "explicit_dates": dates,
        "explicit_budgets": budgets,
        "explicit_urls": urls,
        "explicit_aspects": explicit_aspects,
        "inline_text_supplied_for_summary": inline_summary_text,
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
        "source_policies": list(dict.fromkeys(
            (["government_official_destination"] if government_official_site else [])
            + (["official_destination"] if official_destination else [])
            + (["current_read_page"] if current_required else [])
            + (["public_social_content"] if social_required else [])
            + (["task_relevant_sources"] if not (government_official_site or official_destination or current_required or social_required) else [])
        )),
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
        "missing_required_inputs": list(dict.fromkeys(missing_required_inputs)),
        "requires_clarification": ambiguity_status == "needs_clarification",
        "clarification_reason": (
            "missing_required_input"
            if missing_required_inputs
            else "no_strong_lexical_conflict_detected"
        ),
        "hypothesis_interpretations": hypothesis_rows,
        "constraints": constraints,
        "output_preferences": {
            "concise": bool(output_matches["output_concise"]),
            "detailed": bool(output_matches["output_detailed"]),
            "examples_requested": bool(output_matches["output_examples"]),
            "table_requested": bool(output_matches["output_table"]),
            "bullets_or_checklist_requested": bool(output_matches["output_bullets"]),
        },
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
    if (
        family in {"general_research", "web_research", "find_or_discover"}
        and (
            spec.get("mode") in {"deep", "latest", "social"}
            or constraints.get("time_sensitive_request")
            or spec.get("planner_depth") == "deep"
            or spec.get("intent_route") in {"WEB_DEEP", "LEAD_GENERATION"}
        )
    ):
        candidates.extend([
            (f"{topic} مصدر رسمي", "primary_source_ar", "prefer an original or primary source when appropriate"),
            (f"{topic} official source report", "primary_source_en", "alternate source-oriented search wording"),
            (f"{topic} limitations risks independent analysis", "independent_analysis", "seek counterevidence and limitations"),
        ])
    if (
        not candidates
        and family not in {"general_question", "ambiguous_or_incomplete"}
        and (
            spec.get("mode") in {"deep", "latest", "social"}
            or spec.get("intent_route") in {"WEB_DEEP", "LEAD_GENERATION"}
        )
    ):
        candidates.append(
            (f"{topic} مصدر موثوق", "source_oriented_alternative", "search wording is a hypothesis, not evidence")
        )
    return candidates


def _label_existing_query(query: str, index: int, spec: dict[str, Any]) -> tuple[str, str]:
    """Classify query wording for diagnostics; this is not a retrieval-success claim."""
    normalized = normalize_text(query)
    constraints = spec.get("constraints") if isinstance(spec.get("constraints"), dict) else {}
    if re.search(r"\bsite\s*:", query, flags=re.IGNORECASE):
        return "platform_scoped", "query explicitly scopes a public site or platform"
    if constraints.get("official_destination_required") and any(
        marker in normalized for marker in ("الموقع الرسمي", "official website", "official site")
    ):
        return "official_destination", "query wording seeks an official destination"
    if constraints.get("time_sensitive_request") and any(
        marker in normalized for marker in ("latest", "recent", "today", "تحديث", "حديث", "احدث", "اخر")
    ):
        return "recent_information", "query wording seeks current information; dates and page readability still require validation"
    if any(marker in normalized for marker in ("تجارب", "اراء", "تجربه", "experience", "owner review", "user review")):
        return "personal_experience", "query wording targets user experience; the author's identity and truth remain unverified"
    if any(marker in normalized for marker in ("اعطال", "الاسباب", "الحلول", "troubleshooting", "common failures")):
        return "troubleshooting", "query wording targets symptoms, causes, or remedies"
    if any(marker in normalized for marker in ("المقارنة", "مقارنة", "قارن", "comparison", "versus", "pros cons", "trade offs")):
        return "comparison", "query wording targets a comparison or trade-off analysis"
    if any(marker in normalized for marker in ("مصدر رسمي", "official source", "manual", "specifications", "مواصفات")):
        return "primary_source", "query wording seeks a primary or technical source"
    if index == 0:
        return "planner_seed", "initial planner query; relevance and source quality are validated later"
    return "planner_alternative", "alternate planner query; label is inferred from wording/position"


def build_query_strategy_matrix(
    question: str,
    task_spec: dict[str, Any],
    existing_queries: Any,
    *,
    limit: int = MAX_STRATEGY_QUERIES,
    compact_fn: Any = None,
) -> list[dict[str, str]]:
    """Return bounded query candidates, prioritizing task-specific evidence strategies.

    The first existing planner query anchors the topic. Task-aware queries are then
    considered before secondary planner queries, so generic alternatives cannot consume
    the whole budget and crowd out explicit user criteria.
    """
    maximum = max(1, min(int(limit), MAX_STRATEGY_QUERIES))
    spec = task_spec if isinstance(task_spec, dict) else {}
    queries = existing_queries if isinstance(existing_queries, list) else []
    rows: list[dict[str, str]] = []
    seen: set[str] = set()

    def add(query: Any, strategy: str, rationale: str, *, enforce_topic: bool = True) -> None:
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
        # Search modifications must preserve a subject anchor. Existing planner
        # queries are retained because they may already contain resolved context.
        anchor_query = str(queries[0]).strip() if queries and isinstance(queries[0], str) else str(question or "")
        topic_tokens = _TOKEN_RE.findall(_query_key(anchor_query))
        query_tokens = _TOKEN_RE.findall(key)
        if enforce_topic and len(topic_tokens) >= 2 and not any(
            token in query_tokens for token in topic_tokens[:3]
        ):
            return
        seen.add(key)
        rows.append({"query": candidate, "strategy": strategy, "rationale": rationale})

    constraints = spec.get("constraints") if isinstance(spec.get("constraints"), dict) else {}
    explicit_aspects = (
        constraints.get("explicit_aspects")
        if isinstance(constraints.get("explicit_aspects"), list)
        else []
    )
    # Use the dedicated aspect extractor as a second deterministic pass. This
    # guards against a classifier losing the final criterion in a long list.
    try:
        from agents.aspect_planning import extract_aspects
        independently_extracted = extract_aspects(question)
    except (ImportError, TypeError, ValueError):
        independently_extracted = []
    merged_aspects: list[str] = []
    aspect_keys: set[str] = set()
    for aspect in [*explicit_aspects, *independently_extracted]:
        if not isinstance(aspect, str) or not aspect.strip():
            continue
        key = _query_key(aspect)
        if key and key not in aspect_keys:
            aspect_keys.add(key)
            merged_aspects.append(aspect.strip())
        if len(merged_aspects) >= MAX_TASK_ASPECTS:
            break
    explicit_aspects = merged_aspects
    spec_for_candidates = dict(spec)
    candidate_constraints = dict(constraints)
    candidate_constraints["explicit_aspects"] = explicit_aspects
    spec_for_candidates["constraints"] = candidate_constraints
    # If every query slot is needed to represent explicit comparison criteria,
    # spend the budget on those criteria rather than a generic planner seed.
    reserve_all_slots_for_criteria = (
        spec.get("task_family") == "compare"
        and len(explicit_aspects) >= maximum
    )
    if queries and not reserve_all_slots_for_criteria:
        seed = queries[0]
        strategy, rationale = (
            _label_existing_query(seed, 0, spec)
            if isinstance(seed, str)
            else ("malformed", "planner seed is not a string")
        )
        add(seed, strategy, rationale, enforce_topic=False)

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

    candidates = _generated_strategy_candidates(base, spec_for_candidates)
    preserve_planner_alternatives_early = (
        spec.get("task_family") == "find_or_discover"
        and bool(constraints.get("explicit_budgets"))
        and not constraints.get("social_evidence_requested")
        and not constraints.get("time_sensitive_request")
        and not constraints.get("official_destination_required")
    )
    if preserve_planner_alternatives_early:
        for index, query in enumerate(queries[1:], start=1):
            if len(rows) >= maximum:
                break
            if isinstance(query, str):
                strategy, rationale = _label_existing_query(query, index, spec)
                add(query, strategy, rationale, enforce_topic=False)

    for query, strategy, rationale in candidates:
        add(query, strategy, rationale)
        if len(rows) >= maximum:
            break

    # Preserve other planner alternatives only after task-targeted candidates.
    for index, query in enumerate(queries[1:], start=1):
        if len(rows) >= maximum:
            break
        if isinstance(query, str):
            strategy, rationale = _label_existing_query(query, index, spec)
        else:
            strategy, rationale = "malformed", "planner alternative is not a string"
        add(query, strategy, rationale, enforce_topic=False)
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
        "missing_required_inputs": value.get("missing_required_inputs") if isinstance(value.get("missing_required_inputs"), list) else [],
        "requires_clarification": value.get("requires_clarification") is True,
        "clarification_reason": str(value.get("clarification_reason") or "unassessed")[:80],
        "constraints": value.get("constraints") if isinstance(value.get("constraints"), dict) else {},
        "output_preferences": value.get("output_preferences") if isinstance(value.get("output_preferences"), dict) else {},
        "evidence_requirements": value.get("evidence_requirements") if isinstance(value.get("evidence_requirements"), list) else [],
        "query_strategies": value.get("query_strategies") if isinstance(value.get("query_strategies"), list) else [],
        "tool_requirements": value.get("tool_requirements") if isinstance(value.get("tool_requirements"), list) else [],
        "decision_checks": value.get("decision_checks") if isinstance(value.get("decision_checks"), list) else [],
        "hypothesis_interpretations": value.get("hypothesis_interpretations") if isinstance(value.get("hypothesis_interpretations"), list) else [],
        "claim": "task planning metadata only; not semantic certainty or factual verification",
    }
    return spec
