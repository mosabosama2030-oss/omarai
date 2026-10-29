"""Small deterministic intent routing for Omarai's answer engine.

This module chooses a strategy; it does not search, call a model, or claim that
an answer is factually verified. Keep the rules explicit and unit-testable.
"""
from __future__ import annotations

import re
import unicodedata
from typing import Any

MAX_CONTEXT_TURNS = 8

ROUTES = frozenset({
    "LOCAL", "MODEL_ONLY", "CLARIFY", "WEB_SIMPLE", "WEB_DEEP",
    "LEAD_GENERATION",
})

_ARABIC_DIACRITICS = re.compile(r"[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06ED]")
_PUNCTUATION = re.compile(r"[؟?!.،,؛;:()\[\]{}\"'«»]+")
_SPACE = re.compile(r"\s+")

_SMALLTALK = frozenset({
    "hi", "hello", "hey", "hello there", "hi there",
    "thanks", "thank you", "thanks that helps", "thank you that helps",
    "got it", "okay thanks", "ok thanks", "how are you", "how are you doing",
    "hello how are you", "hi how are you",
    "ازيك", "ازيك عامل ايه", "ازيك عامل ايه النهارده", "عامل ايه", "عامله ايه", "اهلا", "مرحبا",
    "السلام عليكم", "السلام عليكم ورحمه الله وبركاته",
    "صباح الخير", "مساء الخير", "شكرا", "شكرا لك", "متشكر", "متشكره",
    "تمام شكرا", "تمام", "حسنا", "العفو",
})

# Elliptical questions whose subject normally must be recovered from dialogue.
_AMBIGUOUS_ARABIC = frozenset({
    "كام سعرها", "كم سعرها", "بكام سعرها", "سعرها كام", "سعرها بكام",
    "كام تمنها", "كم تمنها", "بكام دي", "بكام ده", "سعره كام", "كام سعره",
    "كم سعره", "قارنهم", "قارنهملي", "قارن بينهم", "قارن بينهما",
    "ما رايك فيها", "ايه رايك فيها", "هل هي كويسه", "هل هو كويس",
    "هل دي كويسه", "هل ده كويس", "هل هو جيد", "هل هي جيده",
    "اشتريها ولا لا", "اشتريه ولا لا",
    "فين", "فين هي", "فين هو", "فين مكانها", "فين مكانه",
    "مكانها فين", "مكانه فين", "موجوده فين", "موجود فين",
    "فين الاقيها", "فين الاقيه",
    "هل فيه ضمان", "فيه ضمان", "هل لها ضمان", "هل له ضمان",
    "هل عليها ضمان", "هل عليه ضمان", "هل يوجد ضمان",
    "ضمانها ايه", "ضمانه ايه",
})
_AMBIGUOUS_ENGLISH = frozenset({
    "how much is it", "how much does it cost", "what is its price",
    "what about it", "what about this", "is it good", "is this good",
    "does it work", "compare them", "compare these", "compare the two",
    "what do you think of it", "should i buy it", "is it worth it",
    "where is it", "where can i find it", "is there a warranty",
    "does it have a warranty", "is it covered by warranty",
})
_DEEP_TERMS = (
    "بحث عميق", "بحث معمق", "بحث مكثف", "بحث شامل", "بالتفصيل",
    "قارن", "مقارنه", "حلل بعمق", "مزايا وعيوب", "الايجابيات والسلبيات",
    "كل الجوانب", "دراسه مقارنه", "compare", "comparison", "deep research",
    "in-depth", "comprehensive", "pros and cons", "trade-offs",
)
_MULTIPART_MARKERS = (
    "بالاضافه الى", "مع مراعاه", "من حيث", "وكذلك", "و ايضا", "والفرق",
    "على ان تشمل", "and also", "as well as", "taking into account",
    "in terms of", "along with",
)


def _normalize(value: str) -> str:
    value = unicodedata.normalize("NFKC", value or "").casefold()
    value = _ARABIC_DIACRITICS.sub("", value)
    value = value.translate(str.maketrans({
        "أ": "ا", "إ": "ا", "آ": "ا", "ٱ": "ا", "ى": "ي", "ة": "ه", "ـ": "",
    }))
    value = _PUNCTUATION.sub(" ", value)
    return _SPACE.sub(" ", value).strip()


def _is_smalltalk(question: str) -> bool:
    normalized = _normalize(question)
    if normalized in {_normalize(item) for item in _SMALLTALK}:
        return True
    # Keep these patterns narrow: an opening greeting followed by a real question
    # is not itself a greeting-only request.
    return bool(
        normalized.startswith("السلام عليكم ")
        and normalized[14:].strip() in _SMALLTALK
    )


def _has_context(history: Any) -> bool:
    """Return true only when history has a usable topic anchor, not a bare follow-up."""
    return bool(_latest_context_anchor(history))


def _has_live_signal(question: str) -> bool:
    """Recognize common time-sensitive or explicit-search requests without a model."""
    normalized = _normalize(question)
    live_terms = (
        "ابحث", "بحث عن", "دور على", "دورلي", "هات رابط", "هاتلي", "جيبلي",
        "اعثر على", "موقع", "رابط", "لينك", "اخبار", "اخر", "احدث", "اليوم",
        "دلوقتي", "حاليا", "سعر", "اسعار", "للبيع", "للايجار", "ايجار",
        "معاينه", "عميل محتمل", "عملاء محتملين", "وظائف", "وظيفه", "حجز",
        "موعد", "الطقس", "سهم", "سعر الصرف", "search", "find", "look up",
        "latest", "today", "current", "news", "price", "for sale", "for rent",
        "real estate", "job opening", "appointment", "reservation", "weather",
        "stock price", "exchange rate",
    )
    return any(_normalize(term) in normalized for term in live_terms) or bool(
        re.search(r"https?://", question, flags=re.IGNORECASE)
    )


def _is_lead_generation_request(question: str) -> bool:
    """Recognize an explicit request to discover prospective buyers/customers.

    A product or property listing request alone is not lead generation. This
    route requires a prospect/customer target plus an action to find one.
    """
    normalized = _normalize(question)
    arabic_actions = ("ابحث عن", "دور على", "دورلي على", "اعثر على", "هاتلي", "هات")
    arabic_targets = ("عميل", "عملاء", "مشتري", "مشتر", "مشترين", "عملاء محتملين")
    english_patterns = (
        r"\b(?:find|search for|look for|identify|generate|build|create)\b.{0,45}\b(?:buyers?|customers?|prospects?|leads?)\b|\b(?:find|build|create|generate)\s+(?:a\s+)?(?:lead generation|prospect list)\b",
    )
    if any(action in normalized for action in arabic_actions) and any(
        target in normalized for target in arabic_targets
    ):
        return True
    if any(re.search(pattern, normalized) for pattern in english_patterns):
        return True
    return bool(
        re.search(
            r"\b(?:buyers?|customers?|prospects?|leads?)\b.{0,45}\b"
            r"(?:looking to buy|want to buy|wants to buy|seeking to purchase)\b",
            normalized,
        )
    )


_FOLLOWUP_LEAD_IN_RE = re.compile(
    r"^(?:(?:و?طيب|و?طب|و?تمام|well|okay|ok|so)\s+)+",
    re.IGNORECASE,
)

_FOLLOWUP_ASPECT_FRAGMENTS = frozenset({
    "السعر", "سعرها كام", "سعره كام", "سعرها", "سعره", "والسعر", "وسعرها",
    "الاسعار", "والاسعار", "الاسعار الحاليه", "اسعار الحاليه", "السعر الحالي",
    "سعر اليوم", "اسعار اليوم", "التكلفه", "والتكلفه", "الضمان", "والضمان",
    "ضمانها", "ضمانه", "البطاريه", "والبطاريه", "الكاميرا", "والكاميرا",
    "المميزات", "والمميزات", "العيوب", "والعيوب", "المكان", "والمكان",
    "المصدر", "والمصدر", "الرابط", "والرابط", "التاريخ", "والتاريخ",
    "المراجعات", "والمراجعات", "الاراء", "والاراء", "and the price",
    "and the warranty", "what about the warranty", "what about the price",
    "its price", "the warranty", "the location", "the pros", "the cons",
})


def _strip_followup_leadin(value: str) -> str:
    return _FOLLOWUP_LEAD_IN_RE.sub("", value).strip()


_FOLLOWUP_LEAD_IN_RE = re.compile(
    r"^(?:(?:و?طيب|و?طب|و?تمام|well|okay|ok|so)\s+)+",
    re.IGNORECASE,
)

_FOLLOWUP_ASPECT_FRAGMENTS = frozenset({
    "السعر", "سعرها كام", "سعره كام", "سعرها", "سعره", "والسعر", "وسعرها",
    "الاسعار", "والاسعار", "الاسعار الحاليه", "اسعار الحاليه", "السعر الحالي",
    "سعر اليوم", "اسعار اليوم", "التكلفه", "والتكلفه", "الضمان", "والضمان",
    "ضمانها", "ضمانه", "البطاريه", "والبطاريه", "الكاميرا", "والكاميرا",
    "المميزات", "والمميزات", "العيوب", "والعيوب", "المكان", "والمكان",
    "المصدر", "والمصدر", "الرابط", "والرابط", "التاريخ", "والتاريخ",
    "المراجعات", "والمراجعات", "الاراء", "والاراء", "and the price",
    "and the warranty", "what about the warranty", "what about the price",
    "its price", "the warranty", "the location", "the pros", "the cons",
})


_CONTEXTUAL_ASPECT_RE = re.compile(
    r"^(?:ال)?(?:سعر|ثمن|اسعار|تكلفه|ضمان|بطاريه|كاميرا|مميزات|عيوب|"
    r"مكان|مصدر|رابط|تاريخ|مراجعات|اراء|توفر|سرعه|اداء|جوده|صيانه)"
)
_CONTEXTUAL_ENGLISH_ASPECT_RE = re.compile(
    r"^(?:what about(?: its)?|how about(?: its)?|and (?:the|its|their)|its) +"
    r"(?:price|warranty|battery|camera|location|source|link|date|pros|cons)"
)


def _strip_followup_leadin(value: str) -> str:
    return _FOLLOWUP_LEAD_IN_RE.sub("", value).strip()


def _starts_with_contextual_aspect(question: str) -> bool:
    """Recognize aspect-led follow-ups without merging standalone new topics."""
    normalized = _normalize(question)
    if _CONTEXTUAL_ENGLISH_ASPECT_RE.match(normalized):
        return True
    stripped = _strip_followup_leadin(normalized)
    if stripped != normalized:
        return bool(_CONTEXTUAL_ASPECT_RE.match(stripped))
    if normalized.startswith("و"):
        return bool(_CONTEXTUAL_ASPECT_RE.match(normalized[1:]))
    return False


def _needs_clarification(question: str) -> bool:
    normalized = _strip_followup_leadin(_normalize(question))
    ambiguous = {_normalize(item) for item in _AMBIGUOUS_ARABIC}
    ambiguous.update(_normalize(item) for item in _AMBIGUOUS_ENGLISH)
    if (
        normalized in ambiguous
        or normalized in _FOLLOWUP_ASPECT_FRAGMENTS
        or _starts_with_contextual_aspect(question)
    ):
        return True
    # Common inflected forms and short property-only follow-ups.
    return bool(
        re.fullmatch(r"(?:كام|كم|بكام)\s+(?:سعر|ثمن)\s*(?:ها|ه|هم)", normalized)
        or re.fullmatch(r"(?:قارن|قارنلي)\s+(?:بينهم|بينهما|دول|دي|دولتين)", normalized)
        or re.fullmatch(r"(?:و)?(?:السعر|الاسعار|التكلفه|الضمان|المميزات|العيوب|البطاريه|الكاميرا|المكان|المصدر|الرابط|التاريخ)", normalized)
    )


def _is_clarification_message(content: Any) -> bool:
    if not isinstance(content, str):
        return False
    normalized = _normalize(content)
    return any(marker in normalized for marker in (
        "تقصد ايه تحديدا", "اكتب اسم الشيء", "ابعت الرابط",
        "what are you referring to", "please name the item",
        "share its link", "clarify what you mean",
    ))


def _latest_context_anchor(history: Any) -> str:
    """Find the latest substantive user topic, skipping ellipsis follow-ups only.

    A recent acknowledgment is a hard boundary: never search past it for stale topics.
    Short entity replies can anchor context when the assistant explicitly asked for one.
    """
    if not isinstance(history, list):
        return ""
    bounded = history[-MAX_CONTEXT_TURNS:]
    for index in range(len(bounded) - 1, -1, -1):
        item = bounded[index]
        if not isinstance(item, dict) or item.get("role") != "user":
            continue
        content = item.get("content")
        if not isinstance(content, str):
            continue
        normalized = _normalize(content)
        if not normalized or _is_smalltalk(normalized):
            return ""
        if _needs_clarification(content):
            continue
        meaningful = re.findall(r"[a-z0-9]+|[\u0600-\u06FF]+", normalized)
        if len(meaningful) >= 2 and len(normalized) >= 8:
            return re.sub(r"\s+", " ", content).strip()[:300]
        if index > 0:
            previous = bounded[index - 1]
            if isinstance(previous, dict) and previous.get("role") == "assistant" and _is_clarification_message(previous.get("content")):
                return re.sub(r"\s+", " ", content).strip()[:120]
        return ""
    return ""


def _pending_clarification_query(history: Any) -> str:
    """Return the unresolved elliptical question immediately awaiting a user slot-fill."""
    if not isinstance(history, list) or not history:
        return ""
    last_index = len(history) - 1
    while last_index >= 0 and not (
        isinstance(history[last_index], dict)
        and isinstance(history[last_index].get("content"), str)
        and history[last_index].get("content", "").strip()
    ):
        last_index -= 1
    if last_index < 0 or history[last_index].get("role") != "assistant":
        return ""
    if not _is_clarification_message(history[last_index].get("content")):
        return ""
    for index in range(last_index - 1, -1, -1):
        item = history[index]
        if isinstance(item, dict) and item.get("role") == "user":
            content = item.get("content")
            if not isinstance(content, str) or not _needs_clarification(content):
                return ""
            if _latest_context_anchor(history[:index]):
                return ""
            return content.strip()[:180]
    return ""


def _is_clarification_answer(question: str, history: Any) -> bool:
    """Recognize a concise answer to Omarai's immediately preceding clarification."""
    if not _pending_clarification_query(history) or not isinstance(question, str):
        return False
    query = question.strip()
    if not query or len(query) >= 100 or _needs_clarification(query) or _is_smalltalk(query):
        return False
    # A self-contained live request should not be mistaken for a slot-fill.
    return not (_has_live_signal(query) or re.search(r"https?://", query, re.IGNORECASE))


def _is_contextual_followup(question: str) -> bool:
    """Detect short referent-dependent follow-ups without treating every 'okay' as one."""
    if not isinstance(question, str) or len(question.strip()) >= 100:
        return False
    if re.search(r"https?://", question, re.IGNORECASE):
        return False
    normalized = _strip_followup_leadin(_normalize(question))
    if _needs_clarification(question) or _starts_with_contextual_aspect(question):
        return True
    # Pronouns and deictic references are strong signals only in a short turn.
    detached_reference = re.fullmatch(
        r"(?:و)?(?:هي|هو|دي|ده|دول|هما|ذلك|تلك|عليها|عليه|فيها|فيه|لها|له|"
        r"سعرها|سعره|مكانها|مكانه|ضمانها|ضمانه|بطاريتها|كاميرتها|مميزاتها|عيوبها)",
        normalized,
    )
    # Arabic often attaches object pronouns to verbs (e.g. "أشتريه", "أستخدمها").
    # These are easy to miss with whitespace-token pronoun lists.
    attached_reference = re.search(
        r"\b(?:استخدم|اشتري|اجيب|اشغل|افتح|اصلح|احط|اجرب|اربط|اوصل|اخد|اخلي|"
        r"اركب|انقل|ادفع|اطلب|احجز)[\u0600-\u06FF]{0,18}(?:ه|ها|هم|هما|هن|ك|كم|كن)\b",
        normalized,
    )
    return bool(detached_reference or attached_reference)


def resolve_followup_query(question: str, history: Any = None) -> str:
    """Resolve a short contextual follow-up against the nearest substantive topic.

    Repeated follow-ups retain the original topic. An answer to an explicit
    clarification is joined to the pending question. New standalone questions are
    never merged merely because they start with 'طيب' or 'طب'.
    """
    if not isinstance(question, str):
        return ""
    query = re.sub(r"\s+", " ", question).strip()
    if not query:
        return ""
    pending = _pending_clarification_query(history)
    if pending and _is_clarification_answer(query, history):
        return f"{pending[:220]} — {query[:180]}"[:500]
    if len(query) >= 100 or not isinstance(history, list):
        return query[:500]
    if not _is_contextual_followup(query):
        return query[:500]
    previous = _latest_context_anchor(history)
    if not previous:
        return query[:500]
    return f"{previous[:300]} — {query[:180]}"[:500]


def _has_explicit_source_request(question: str) -> bool:
    """Recognize explicit requests for evidence/citations that require web-backed retrieval."""
    normalized = _normalize(question)
    markers = (
        "اذكر مصادر", "اذكر المصدر", "مصادر موثوقة", "مصدر موثوق",
        "مصادر رسمية", "مصادر حديثة", "مع مصادر", "مع المصادر",
        "بالمصادر", "روابط المصادر", "ارفق المصادر", "أرفق المصادر",
        "استشهد بمصادر", "وثق الاجابة", "وثق الإجابة", "المراجع",
        "with sources", "cite sources", "trusted sources", "reliable sources",
        "official sources", "include references", "with citations",
        "source-backed", "cite your sources",
    )
    return any(_normalize(marker) in normalized for marker in markers)


def _is_deep(question: str) -> bool:
    normalized = _normalize(question)
    if any(_normalize(term) in normalized for term in _DEEP_TERMS):
        return True
    # Explicit multi-dimension comparisons need evidence from more than one angle.
    dimensions = (
        "السعر", "سعر", "بطاريه", "كاميرا", "اداء", "امان", "تكلفه",
        "الصيانه", "الجوده", "المميزات", "العيوب", "الاراء", "المراجعات",
        "price", "battery", "camera", "performance", "safety", "cost",
        "maintenance", "quality", "features", "drawbacks", "reviews",
    )
    matched_dimensions = sum(1 for item in dimensions if _normalize(item) in normalized)
    return matched_dimensions >= 2 and any(
        marker in normalized for marker in _MULTIPART_MARKERS
    )


def _is_page_summarization_request(question: str) -> bool:
    """Recognize a request to summarize a specific web page or link."""
    normalized = _normalize(question)
    terms = ("لخص", "تلخيص", "ملخص", "summarize", "summarise", "summary")
    page_references = (
        "صفحه", "الصفحه", "مقال", "المقال", "رابط", "لينك", "url",
        "link", "article", "page", "webpage", "web page", "website",
    )
    return (
        any(_normalize(term) in normalized for term in terms)
        and (
            bool(re.search(r"https?://", question, flags=re.IGNORECASE))
            or any(_normalize(term) in normalized for term in page_references)
        )
    )


def _has_inline_summary_text(question: str) -> bool:
    """Detect text explicitly pasted after a summary instruction, not a web page URL."""
    if re.search(r"https?://", question, flags=re.IGNORECASE):
        return False
    normalized = _normalize(question)
    markers = (
        "النص التالي", "النص الاتي", "النص ده", "النص اللي جاي",
        "this text", "following text", "the following text", "text below",
        "text to summarize", "content below",
    )
    for marker in markers:
        normalized_marker = _normalize(marker)
        if normalized_marker in normalized:
            remainder = normalized.split(normalized_marker, 1)[1].strip()
            if len(remainder) >= 8:
                return True
    # Also allow a concise direct form such as "لخص: [pasted paragraph]".
    return bool(
        re.search(
            r"^\s*(?:لخص(?:\s+لي)?|تلخيص|summari[sz]e|summary)\s*[:：]\s*\S.{12,}$",
            question,
            flags=re.IGNORECASE,
        )
    )


def route_intent(
    question: str,
    history: Any = None,
    mode: str = "auto",
    *,
    capability_question: bool = False,
    requires_web: bool = False,
) -> dict[str, Any]:
    """Return a deterministic route and auditable reason for a user question."""
    clean_mode = mode.strip().lower() if isinstance(mode, str) else "auto"

    # If the assistant just asked for a missing referent, bind the user's concise
    # reply to that pending question instead of answering the entity name in isolation.
    if _is_clarification_answer(question, history):
        return {
            "route": "WEB_DEEP" if clean_mode == "deep" else "WEB_SIMPLE",
            "reason": "answer_to_pending_clarification",
            "context_available": True,
            "needs_clarification": False,
        }

    context_available = _has_context(history)

    # A search mode cannot supply a missing subject. Clarify genuinely elliptical
    # questions before honoring the UI's explicit research mode.
    if _needs_clarification(question) and not context_available:
        return {
            "route": "CLARIFY",
            "reason": "missing_referent_and_no_conversation_context",
            "context_available": False,
            "needs_clarification": True,
        }

    # An explicitly selected mode controls research depth when the request itself
    # is sufficiently specified.
    if clean_mode != "auto":
        route = "WEB_DEEP" if clean_mode == "deep" else "WEB_SIMPLE"
        return {
            "route": route,
            "reason": "explicit_mode",
            "context_available": context_available,
            "needs_clarification": False,
        }

    if capability_question:
        return {
            "route": "LOCAL",
            "reason": "capability_question",
            "context_available": context_available,
            "needs_clarification": False,
        }

    if _is_smalltalk(question):
        return {
            "route": "LOCAL",
            "reason": "short_conversational_turn",
            "context_available": context_available,
            "needs_clarification": False,
        }

    # A page/link summary needs a concrete source. Pasted text is handled locally;
    # an absent source must trigger clarification rather than a search for "the page".
    if _is_page_summarization_request(question):
        if _has_inline_summary_text(question):
            return {
                "route": "MODEL_ONLY",
                "reason": "summarization_text_provided",
                "context_available": context_available,
                "needs_clarification": False,
            }
        if re.search(r"https?://", question, flags=re.IGNORECASE):
            return {
                "route": "WEB_SIMPLE",
                "reason": "summarization_request",
                "context_available": context_available,
                "needs_clarification": False,
            }
        return {
            "route": "CLARIFY",
            "reason": "missing_summarization_input",
            "context_available": context_available,
            "needs_clarification": True,
        }

    ambiguous = _is_contextual_followup(question) or _needs_clarification(question)
    if ambiguous:
        return {
            "route": "WEB_DEEP" if _is_deep(question) else "WEB_SIMPLE",
            "reason": "ambiguous_followup_with_context",
            "context_available": True,
            "needs_clarification": False,
        }

    if _is_lead_generation_request(question):
        return {
            "route": "LEAD_GENERATION",
            "reason": "explicit_prospect_or_buyer_discovery_request",
            "context_available": context_available,
            "needs_clarification": False,
        }

    if _is_deep(question):
        return {
            "route": "WEB_DEEP",
            "reason": "comparison_or_multi_part_research",
            "context_available": context_available,
            "needs_clarification": False,
        }

    if requires_web or _has_live_signal(question) or _has_explicit_source_request(question):
        return {
            "route": "WEB_SIMPLE",
            "reason": (
                "explicit_evidence_request"
                if _has_explicit_source_request(question)
                else "freshness_or_explicit_research_signal"
            ),
            "context_available": context_available,
            "needs_clarification": False,
        }

    return {
        "route": "MODEL_ONLY",
        "reason": "stable_knowledge_or_conversation",
        "context_available": context_available,
        "needs_clarification": False,
    }
