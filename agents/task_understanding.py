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

# Closed, code-owned playbooks. The model receives concise task guidance derived
# from these IDs; arbitrary planner/source text cannot add executable instructions.
_REASONING_GUIDANCE = {
    "preserve_goal_and_constraints": "حافظ على مقصد المستخدم والكيانات والبلد والسنة والميزانية والتواريخ والصيغة التي ذكرها صراحة؛ لا تخترع قيودًا مفقودة.",
    "separate_facts_inferences_hypotheses": "افصل ما يقوله المصدر مباشرة عن الاستنتاج والفرضية والمعلومة المجهولة؛ لا ترفع الفرضية إلى حقيقة دون دليل.",
    "ground_material_claims": "اربط كل ادعاء واقعي جوهري بدليل مناسب من المصدر؛ الاستشهاد أو تشابه الكلمات وحده لا يثبت صحة الادعاء.",
    "bounded_stop_rule": "استخدم المحاولات والوقت المسموحين فقط؛ عند نقص الدليل، أجب جزئيًا أو امتنع بوضوح بدل التخمين.",
    "clarify_required_input": "إذا غاب مدخل إلزامي يغيّر معنى المهمة، اطلبه قبل تشغيل أداة أو اختراع هدف.",
    "resolve_followup_slots": "في المتابعة، احتفظ فقط بالسياق الذي له مرجع واضح، وطبّق التغييرات التي ذكرها المستخدم، ولا ترث موضوعًا قديمًا بعد تغيير الموضوع.",
    "verify_official_destination": "طابق اسم الجهة والبلد أولًا؛ فضّل نطاق الجهة أو رابطًا صادرًا عن بوابة رسمية موثوقة، ولا تعتبر امتداد النطاق وحده إثباتًا للملكية.",
    "separate_event_and_publication_dates": "ميّز تاريخ وقوع الحدث عن تاريخ النشر وآخر تحديث وتاريخ الوصول؛ لا تستخدم خبرًا قديمًا لإثبات حالة متغيرة الآن.",
    "reject_stale_current_claims": "للمعلومة الحالية، افحص حداثة المصدر وقابلية قراءة الصفحة وارتباطها بالحالة الحالية؛ اعرض عدم التأكد إذا غاب دليل حديث مؤهل.",
    "decompose_explicit_criteria": "قسّم المقارنة إلى كل معيار صريح، وابحث عن دليل لكل معيار، وسجّل المحاور التي لا تزال بلا دليل بدل إسقاطها.",
    "normalize_comparison_conditions": "قبل المقارنة، وحّد العملة والوحدات والفترة وظروف الاستخدام؛ لا تقارن قيمًا غير قابلة للمقارنة دون شرح الفرق.",
    "separate_specs_and_experiences": "افصل المواصفات الرسمية عن الاختبارات الصحفية وتجارب الأفراد والإعلانات؛ لكل نوع منها ما يستطيع إثباته وحدوده.",
    "balance_social_evidence": "ميّز التجربة الشخصية المحتملة عن السؤال والترويج والمحتوى الصحفي؛ اعرض عينة المنشورات وتواريخها والاختلافات ولا تعمم على الجميع.",
    "record_observed_symptoms": "احفظ رسالة الخطأ والبيئة والإصدار والخطوات التي يمكن تكرارها؛ ميّز الملاحظة المرصودة عن تفسير السبب.",
    "rank_testable_hypotheses": "أنشئ عدة فرضيات للسبب، ورتّبها وفق الأدلة المتاحة وقابلية الاختبار، ولا تدّعِ إثبات السبب قبل تجربة تفصل بين الفرضيات.",
    "verify_primary_technical_docs": "تحقق من دليل المنتج أو مرجع الواجهة أو سجل التغيير الأصلي، واستخدم اختبارًا يعيد إنتاج المشكلة للتحقق من الإصلاح.",
    "prefer_low_risk_steps": "ابدأ بخطوات تشخيص قابلة للعكس ومنخفضة المخاطر، واذكر شروط التوقف؛ لا تقترح إجراءً خطيرًا لمجرد أنه احتمال.",
    "ordered_safe_procedure": "اذكر المتطلبات المسبقة والتحذيرات ثم الخطوات بالترتيب، وأضف طريقة للتحقق من النتيجة ولا تساوِ بين إكمال الخطوات ونجاحها.",
    "check_health_scope_and_urgency": "افصل التثقيف الصحي العام عن التشخيص الشخصي، وقدّم مصادر صحية موثوقة وحدود المعلومات، ووجّه الحالات الطارئة إلى الرعاية المناسبة.",
    "check_legal_jurisdiction_and_effective_date": "حدّد الدولة أو الاختصاص القانوني وتاريخ النفاذ، وقدّم النص الأصلي الرسمي عند توفره، ولا تعرض المعلومات العامة بوصفها استشارة قانونية خاصة.",
    "validate_data_before_interpreting": "تحقق من تعريف المقياس ووحدة التحليل والفترة والبيانات الناقصة والتكرارات والقيم الشاذة قبل تفسير النتائج؛ الارتباط لا يثبت السببية.",
    "validate_units_and_arithmetic": "تحقق من الوحدات والمدخلات والافتراضات، واعرض المعادلة أو خطوات الحساب القابلة للفحص، وأجرِ تحققًا حسابيًا مستقلًا عندما يلزم.",
    "preserve_translation_meaning": "حافظ على المعنى والنبرة والأسماء والمصطلحات وصيغة الهدف؛ أظهر الالتباس الحقيقي بدل اختراع معنى للنص.",
    "preserve_user_facts_in_writing": "التزم بالجمهور والنبرة والشكل المطلوب، ولا تضف حقائق غير مقدمة أو موثقة، وافصل إعادة الصياغة عن التحقق الواقعي.",
    "plan_dependencies_and_fallbacks": "رتّب العمل حسب التبعيات والموارد والموعد والمخاطر، وبيّن الافتراضات والبدائل، ولا تصف خطوة مقترحة بأنها نُفذت.",
    "compare_recommendation_tradeoffs": "وازن البدائل وفق احتياج المستخدم وقيوده، وبيّن المفاضلات والمعلومات الناقصة، ولا تعلن فائزًا عامًا دون أساس مقارنة واضح.",
    "summarize_only_available_content": "لخّص النص المقدم أو الصفحة التي قُرئت فعلًا فقط؛ لا تستنتج محتوى غير مقروء من عنوان أو رابط.",
    "qualify_buyer_intent": "ميّز إشارة نية شراء صريحة عن إعلان بيع أو صفحة تجارية؛ لا تعتبر الإعلان عميلًا ولا تزعم التحقق من الهوية.",
    "prefer_lowest_sufficient_tool": "اختر أقل مسار أدوات كافٍ للمهمة؛ لا تبحث في الويب عندما تكفي المادة المقدمة أو الحساب المحلي، ولا تشغّل أداة غير مهيأة أو غير مسموح بها.",
}
_REASONING_FAMILY_IDS = {
    "official_site_lookup": ("verify_official_destination",),
    "social_opinions": ("balance_social_evidence", "separate_specs_and_experiences"),
    "summarize": ("summarize_only_available_content",),
    "troubleshoot": ("record_observed_symptoms", "rank_testable_hypotheses", "verify_primary_technical_docs", "prefer_low_risk_steps"),
    "compare": ("decompose_explicit_criteria", "normalize_comparison_conditions", "separate_specs_and_experiences"),
    "how_to": ("ordered_safe_procedure",),
    "lead_generation": ("qualify_buyer_intent",),
    "recommendation": ("compare_recommendation_tradeoffs",),
    "medical_information": ("check_health_scope_and_urgency",),
    "legal_information": ("check_legal_jurisdiction_and_effective_date",),
    "coding_or_technical_design": ("record_observed_symptoms", "rank_testable_hypotheses", "verify_primary_technical_docs"),
    "data_analysis": ("validate_data_before_interpreting",),
    "calculation": ("validate_units_and_arithmetic",),
    "translation": ("preserve_translation_meaning",),
    "writing_or_editing": ("preserve_user_facts_in_writing",),
    "planning": ("plan_dependencies_and_fallbacks",),
    "creative_generation": ("preserve_user_facts_in_writing",),
}
_DECISION_MATRIX = (
    {"stage": "interpret", "check": "goal_context_required_inputs", "pass_action": "preserve_explicit_constraints", "fail_action": "clarify_missing_required_input"},
    {"stage": "route", "check": "tool_permission_and_readiness", "pass_action": "use_only_allowed_configured_tools", "fail_action": "report_not_configured_or_blocked"},
    {"stage": "plan", "check": "distinct_relevant_queries_and_budget", "pass_action": "execute_bounded_deduplicated_plan", "fail_action": "stop_and_report_limit"},
    {"stage": "evidence", "check": "relevance_identity_freshness_readability", "pass_action": "retain_task_eligible_evidence", "fail_action": "exclude_and_record_reason"},
    {"stage": "synthesize", "check": "claim_support_and_scope", "pass_action": "cite_supported_claims_and_qualify_inference", "fail_action": "answer_partially_or_abstain"},
    {"stage": "terminate", "check": "actual_stage_outcomes", "pass_action": "report_observed_completion_state", "fail_action": "mark_partial_failed_or_not_run"},
)
_DECISION_STAGES = {row["stage"] for row in _DECISION_MATRIX}
_DECISION_IDS = {
    field: {row[field] for row in _DECISION_MATRIX}
    for field in ("check", "pass_action", "fail_action")
}


def _reasoning_strategy_ids(
    family: str,
    constraints: dict[str, Any],
    context_resolution: dict[str, Any],
    missing_required_inputs: list[str],
) -> list[str]:
    selected = [
        "preserve_goal_and_constraints",
        "separate_facts_inferences_hypotheses",
        "ground_material_claims",
        "bounded_stop_rule",
        "prefer_lowest_sufficient_tool",
    ]
    selected.extend(_REASONING_FAMILY_IDS.get(family, ()))
    if missing_required_inputs or context_resolution.get("needs_clarification"):
        selected.append("clarify_required_input")
    if context_resolution.get("is_follow_up"):
        selected.append("resolve_followup_slots")
    if constraints.get("time_sensitive_request"):
        selected.extend(("separate_event_and_publication_dates", "reject_stale_current_claims"))
    if constraints.get("official_destination_required"):
        selected.append("verify_official_destination")
    if constraints.get("social_evidence_requested"):
        selected.append("balance_social_evidence")
    if len(constraints.get("explicit_aspects") or []) > 1:
        selected.append("decompose_explicit_criteria")
    if constraints.get("explicit_budgets"):
        selected.append("preserve_goal_and_constraints")
    return list(dict.fromkeys(item for item in selected if item in _REASONING_GUIDANCE))[:12]


def reasoning_guidance_for_task_spec(task_spec: dict[str, Any]) -> list[str]:
    """Expand allowlisted reasoning IDs into fixed, non-executable guidance text."""
    ids = task_spec.get("reasoning_strategy_ids") if isinstance(task_spec, dict) else []
    if not isinstance(ids, list):
        return []
    return [_REASONING_GUIDANCE[item] for item in ids if isinstance(item, str) and item in _REASONING_GUIDANCE][:12]

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
    "medical_information": (
        "اعراض", "أعراض", "جرعة", "جرعات", "دواء", "ادوية", "علاج", "تشخيص",
        "medical symptoms", "dosage", "medicine", "medication", "treatment", "diagnosis",
    ),
    "legal_information": (
        "قانون", "قانوني", "نص قانوني", "عقد", "دعوى", "لائحة", "تشريع",
        "legal advice", "law", "contract", "lawsuit", "regulation", "legislation",
    ),
    "coding_or_technical_design": (
        "اكتب كود", "برمج", "كود بايثون", "اشرح الكود", "راجع الكود",
        "الكود التالي", "تصميم api", "اكتب سكربت", "code", "programming",
        "python code", "javascript", "api design", "stack trace", "unit test",
        "refactor", "debug this code",
    ),
    "data_analysis": (
        "حلل البيانات", "تحليل البيانات", "ملف csv", "تحليل جدول", "احسب المتوسط",
        "data analysis", "analyze data", "analyse data", "dataset", "spreadsheet",
        "csv file", "trend analysis", "calculate average", "pivot table",
    ),
    "calculation": (
        "احسب", "كم يساوي", "ما ناتج", "حساب النسبة", "احسب الفرق",
        "calculate", "compute", "what is the result", "percentage calculation",
        "how many", "how much is",
    ),
    "translation": (
        "ترجم", "ترجمة", "ترجم إلى", "ترجم للانجليزية", "ترجم للعربية",
        "translate", "translation", "translate into", "localize this",
    ),
    "writing_or_editing": (
        "اكتب", "اكتب رسالة", "اكتب بريد", "اعد صياغة", "أعد صياغة",
        "صحح لغويا", "راجع النص", "حسن الصياغة", "draft", "write", "rewrite",
        "proofread", "edit this", "polish this", "compose an email",
    ),
    "planning": (
        "ضع خطة", "خطة عمل", "خطة زمنية", "جدول زمني", "خطوات تنفيذ",
        "نظم لي", "رتب لي", "plan", "planning", "roadmap", "itinerary",
        "project schedule", "timeline", "project plan",
    ),
    "creative_generation": (
        "اكتب قصة", "قصة قصيرة", "قصيدة", "سيناريو", "اقترح افكار",
        "اقترح أفكار", "عصف ذهني", "brainstorm", "creative writing",
        "write a story", "poem", "generate ideas",
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
    "output_beginner_friendly": (
        "ببساطة", "بشرح بسيط", "للمبتدئين", "من الصفر", "بلغة سهلة",
        "simple language", "beginner friendly", "beginner-friendly",
        "explain like i'm five", "eli5",
    ),
    "output_citations": (
        "مع مصادر", "اذكر المصادر", "مصادر موثوقة", "روابط مباشرة",
        "with sources", "cite sources", "include references", "with citations",
    ),
    "output_links": (
        "رابط مباشر", "روابط مباشرة", "هات الرابط", "لينك", "url",
        "direct link", "direct links", "include links", "source url",
    ),
    "output_json": (
        "بصيغة json", "تنسيق json", "return json", "output json", "as json",
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
    """Match phrases on token boundaries with conservative Arabic clitic handling.

    The matcher never accepts arbitrary substrings: variants are formed only by
    removing a short, explicit list of common prefixes/suffixes. This avoids
    collisions such as treating "الإنذار" as "الآن".
    """
    tokens = _TOKEN_RE.findall(text)
    matched: list[str] = []
    prefixes = ("وال", "بال", "فال", "كال", "لل", "ال", "و", "ف", "ب", "ل", "ك")
    suffixes = ("هما", "هم", "هن", "ها", "ه", "كم", "كن", "ك", "نا", "ني", "ين", "ات", "ون")
    english_suffixes = ("ing", "ed", "es", "s")
    cache: dict[str, set[str]] = {}

    def token_forms(raw_token: str) -> set[str]:
        original = normalize_text(raw_token)
        if original in cache:
            return cache[original]
        forms = {original} if original else set()
        queue = list(forms)
        while queue:
            current = queue.pop()
            for prefix in prefixes:
                if current.startswith(prefix) and len(current) - len(prefix) >= 3:
                    candidate = current[len(prefix):]
                    if candidate not in forms:
                        forms.add(candidate)
                        queue.append(candidate)
            for suffix in suffixes:
                if current.endswith(suffix) and len(current) - len(suffix) >= 3:
                    candidate = current[:-len(suffix)]
                    if candidate not in forms:
                        forms.add(candidate)
                        queue.append(candidate)
            if current.isascii() and len(current) >= 5:
                for suffix in english_suffixes:
                    if current.endswith(suffix) and len(current) - len(suffix) >= 3:
                        candidate = current[:-len(suffix)]
                        if candidate not in forms:
                            forms.add(candidate)
                            queue.append(candidate)
        cache[original] = forms
        return forms

    token_forms_cache = [token_forms(token) for token in tokens]
    for phrase in phrases:
        normalized = normalize_text(phrase)
        phrase_tokens = _TOKEN_RE.findall(normalized)
        if not phrase_tokens:
            continue
        phrase_forms = [token_forms(token) for token in phrase_tokens]
        width = len(phrase_tokens)
        found = any(
            all(token_forms_cache[index + offset] & phrase_forms[offset] for offset in range(width))
            for index in range(max(0, len(tokens) - width + 1))
        )
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
        "medical_information", "legal_information", "coding_or_technical_design",
        "data_analysis", "translation", "calculation", "planning",
        "creative_generation", "writing_or_editing", "lead_generation",
        "how_to", "recommendation", "current_information", "find_or_discover",
        "explain_or_define", "general_research",
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
    elif family == "medical_information":
        evidence_requirements = [
            "distinguish_general_health_information_from_personal_diagnosis",
            "prefer_current_authoritative_health_sources_when_research_is_requested",
            "preserve_units_dosage_context_and_uncertainty",
            "escalate_urgent_or_emergency_symptoms_to_appropriate_care",
        ]
        query_strategies = ["authoritative_health_source", "symptom_context", "limitations_and_urgency"]
    elif family == "legal_information":
        evidence_requirements = [
            "identify_jurisdiction_and_effective_date_if_relevant",
            "prefer_primary_law_or_official_regulatory_text",
            "distinguish_general_information_from_legal_advice",
        ]
        query_strategies = ["official_law_text", "jurisdiction_and_date", "interpretive_context"]
    elif family == "coding_or_technical_design":
        evidence_requirements = [
            "preserve_language_version_runtime_and_error_text_if_supplied",
            "separate_observed_failure_from_cause_hypotheses",
            "provide_testable_changes_and_regression_tests",
        ]
        query_strategies = ["minimal_reproducer", "documentation_or_api_reference", "test_and_verify"]
    elif family == "data_analysis":
        evidence_requirements = [
            "preserve_dataset_grain_and_metric_definition",
            "inspect_missingness_duplicates_outliers_and_time_coverage",
            "separate_observed_association_from_causal_explanation",
        ]
        query_strategies = ["schema_and_grain", "data_quality", "metric_and_segment_checks"]
    elif family == "calculation":
        evidence_requirements = [
            "show_formula_and_units_when_useful",
            "validate_input_units_and_rounding",
            "distinguish_exact_result_from_assumption_based_estimate",
        ]
        query_strategies = ["formula", "unit_validation", "independent_arithmetic_check"]
    elif family == "translation":
        evidence_requirements = [
            "preserve_meaning_tone_and_named_entities",
            "surface_ambiguous_source_phrasing_instead_of_silently_inventing_meaning",
            "respect_explicit_target_language_and_script",
        ]
        query_strategies = ["source_text", "target_language", "terminology_and_tone"]
    elif family == "writing_or_editing":
        evidence_requirements = [
            "follow_requested_audience_tone_and_format",
            "preserve_user_provided_facts_without_adding_unverified_claims",
            "distinguish_rewrite_from_fact_check",
        ]
        query_strategies = ["audience_and_purpose", "tone_and_format", "fact_preservation"]
    elif family == "planning":
        evidence_requirements = [
            "preserve_goal_constraints_dependencies_and_deadline",
            "make_assumptions_and_unavailable_resources_explicit",
            "separate_proposed_steps_from_completed_actions",
        ]
        query_strategies = ["goal_and_constraints", "dependency_order", "risks_and_fallbacks"]
    elif family == "creative_generation":
        evidence_requirements = [
            "follow_requested_genre_voice_and_constraints",
            "do_not_present_invented_story_details_as_real_facts",
            "preserve_explicit_content_boundaries",
        ]
        query_strategies = ["genre_and_voice", "creative_constraints", "revision_options"]
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
    raw_context_entities = context.get("entities")
    context_entities = [
        str(item).strip()[:120]
        for item in raw_context_entities[:8]
        if isinstance(item, str) and item.strip()
    ] if isinstance(raw_context_entities, list) else []
    raw_context_slots = context.get("slots")
    context_slots: dict[str, str] = {}
    if isinstance(raw_context_slots, dict):
        for raw_key, raw_value in list(raw_context_slots.items())[:16]:
            if isinstance(raw_key, str) and isinstance(raw_value, str) and raw_key.strip() and raw_value.strip():
                context_slots[raw_key.strip()[:40]] = raw_value.strip()[:180]
    raw_changed_slots = context.get("changed_slots")
    context_changed_slots = [
        str(item).strip()[:40]
        for item in raw_changed_slots[:8]
        if isinstance(item, str) and item.strip()
    ] if isinstance(raw_changed_slots, list) else []
    context_resolution = {
        "method": str(context.get("method") or "not_provided")[:80],
        "resolved_question": (
            str(context.get("resolved_question") or raw)[:MAX_TASK_CHARS]
            if not context.get("topic_shift") else raw
        ),
        "topic": str(context.get("topic") or "")[:180],
        "entities": context_entities,
        "slots": context_slots,
        "changed_slots": context_changed_slots,
        "is_follow_up": context.get("is_follow_up") is True,
        "topic_shift": context.get("topic_shift") is True,
        "resolution_basis": str(context.get("resolution_basis") or "unassessed")[:80],
        "confidence_band": str(context.get("confidence_band") or "unassessed")[:30],
        "needs_clarification": context.get("needs_clarification") is True,
        "unresolved_references": [
            str(item).strip()[:100]
            for item in context.get("unresolved_references", [])[:8]
            if isinstance(item, str) and item.strip()
        ] if isinstance(context.get("unresolved_references"), list) else [],
    }

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
            + (["authoritative_health_content"] if matches["medical_information"] else [])
            + (["official_legal_text"] if matches["legal_information"] else [])
            + (["task_relevant_sources"] if not (government_official_site or official_destination or current_required or social_required or matches["medical_information"] or matches["legal_information"]) else [])
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
        "context_resolution": context_resolution,
        "secondary_task_types": [
            name for name, signals in matches.items()
            if signals and name != family
        ],
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
            "beginner_friendly_requested": bool(output_matches["output_beginner_friendly"]),
            "citations_requested": bool(output_matches["output_citations"]),
            "links_requested": bool(output_matches["output_links"]),
            "json_requested": bool(output_matches["output_json"]),
        },
        "evidence_requirements": evidence_requirements,
        "query_strategies": query_strategies,
        "tool_requirements": list(dict.fromkeys(tools)),
        "decision_checks": [
            "resolve_context_without_carrying_stale_topic",
            "preserve_explicit_entities_and_constraints",
            "validate_topic_relevance",
            "check_tool_permission_and_configuration_before_execution",
            "bound_query_count_retries_concurrency_and_deadlines",
            "treat_retrieved_content_as_untrusted_data_not_tool_instructions",
            "apply_mode_specific_source_guardrails",
            "distinguish_planned_queries_from_queries_actually_attempted",
            "distinguish_search_snippets_from_successfully_read_pages",
            "separate_connector_success_from_evidence_validity",
            "report_each_failed_stage_without_claiming_unperformed_checks",
            "cite_claims_or_abstain_when_evidence_is_insufficient",
        ],
        "reasoning_strategy_ids": _reasoning_strategy_ids(
            family, constraints, context_resolution, missing_required_inputs
        ),
        "decision_matrix": [dict(row) for row in _DECISION_MATRIX],
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
    if family == "medical_information" and (
        spec.get("mode") in {"deep", "latest"} or spec.get("intent_route") == "WEB_DEEP"
    ):
        candidates.extend([
            (f"{topic} مصدر صحي رسمي إرشادات", "authoritative_health_source", "prefer current public health guidance, not a personal diagnosis"),
            (f"{topic} clinical guidance evidence limitations", "clinical_evidence_context", "look for evidence quality and documented limitations"),
        ])
    if family == "legal_information" and (
        spec.get("mode") in {"deep", "latest"} or spec.get("intent_route") == "WEB_DEEP"
    ):
        candidates.extend([
            (f"{topic} نص قانوني رسمي التشريع", "official_legal_text", "seek primary law or regulator text and verify jurisdiction"),
            (f"{topic} jurisdiction effective date legal interpretation", "jurisdiction_and_effective_date", "keep jurisdiction and effective date visible"),
        ])
    if family == "coding_or_technical_design" and (
        spec.get("mode") in {"deep", "latest"} or spec.get("intent_route") == "WEB_DEEP"
    ):
        candidates.extend([
            (f"{topic} official documentation", "official_technical_docs", "prefer the language/runtime's authoritative documentation"),
            (f"{topic} exact error regression test", "error_and_regression_test", "look for a reproducible error and a testable fix"),
        ])
    if family == "planning" and (
        spec.get("mode") in {"deep", "latest"} or spec.get("intent_route") == "WEB_DEEP"
    ):
        candidates.extend([
            (f"{topic} risks dependencies feasibility", "feasibility_and_dependencies", "test assumptions, dependencies, and likely blockers"),
            (f"{topic} alternative plan fallback", "alternatives_and_fallback", "seek alternatives and fallback approaches"),
        ])
    normalized_topic = normalize_text(topic)
    property_topic = any(
        cue in normalized_topic
        for cue in ("شقه", "شقق", "عقار", "عقارات", "عقاري", "real estate", "apartment", "property")
    )
    if family == "find_or_discover" and property_topic:
        candidates.extend([
            (f"{topic} إعلانات عقارية", "property_listings", "discover relevant listings without treating ads as independent price evidence"),
            (f"{topic} متوسط أسعار السوق للمتر", "property_market_price_per_meter", "compare asking prices against market-level context"),
            (f"{topic} أسعار البيع الفعلية والتقييم العقاري", "property_transaction_price_check", "distinguish asking prices from completed transaction prices"),
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
        and family in {
            "official_site_lookup", "current_information", "social_opinions",
            "compare", "troubleshoot", "how_to", "recommendation",
            "lead_generation", "general_research", "web_research", "find_or_discover",
            "medical_information", "legal_information", "coding_or_technical_design",
            "planning",
        }
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
    for query, strategy, rationale in candidates:
        add(
            query, strategy, rationale,
            enforce_topic=(strategy != "explicit_criterion"),
        )
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
    """Return an allowlisted, bounded JSON representation of TaskSpec-like input."""
    unavailable = {
        "schema": "omarai.task_spec.v1",
        "status": "not_available",
        "claim": "no validated task specification supplied",
    }
    if not isinstance(value, dict) or value.get("schema") != "omarai.task_spec.v1":
        return unavailable

    def clean_text(item: Any, limit: int = 160) -> str:
        if not isinstance(item, str):
            return ""
        return _SPACE.sub(" ", unicodedata.normalize("NFKC", item).replace("\x00", " ")).strip()[:limit]

    def clean_list(item: Any, *, items: int = 16, chars: int = 160) -> list[str]:
        if not isinstance(item, list):
            return []
        result: list[str] = []
        seen: set[str] = set()
        for raw_item in item[:items * 2]:
            cleaned = clean_text(raw_item, chars)
            key = cleaned.casefold()
            if cleaned and key not in seen:
                result.append(cleaned)
                seen.add(key)
            if len(result) >= items:
                break
        return result

    raw_constraints = value.get("constraints")
    raw_constraints = raw_constraints if isinstance(raw_constraints, dict) else {}
    list_constraint_keys = (
        "explicit_locations", "explicit_years", "explicit_dates",
        "explicit_budgets", "explicit_urls", "explicit_aspects", "source_policies",
    )
    constraints: dict[str, Any] = {
        key: clean_list(raw_constraints.get(key), items=8 if key == "explicit_aspects" else 5, chars=300 if key == "explicit_urls" else 120)
        for key in list_constraint_keys
    }
    for key in (
        "inline_text_supplied_for_summary",
        "time_sensitive_request",
        "official_site_required",
        "official_destination_required",
        "social_evidence_requested",
    ):
        constraints[key] = raw_constraints.get(key) is True
    language_profile = raw_constraints.get("language_profile")
    constraints["language_profile"] = (
        language_profile
        if isinstance(language_profile, str) and language_profile in {"ar", "en", "mixed", "und"}
        else "und"
    )
    allowed_source_policies = {
        "government_official_destination", "official_destination", "current_read_page",
        "public_social_content", "authoritative_health_content", "official_legal_text",
        "task_relevant_sources", "unassessed",
    }
    source_policy = clean_text(raw_constraints.get("source_policy"), 80)
    constraints["source_policy"] = source_policy if source_policy in allowed_source_policies else "unassessed"
    constraints["source_policies"] = [
        item for item in constraints["source_policies"]
        if item in allowed_source_policies
    ]

    raw_preferences = value.get("output_preferences")
    raw_preferences = raw_preferences if isinstance(raw_preferences, dict) else {}
    preference_keys = (
        "concise", "detailed", "examples_requested", "table_requested",
        "bullets_or_checklist_requested", "beginner_friendly_requested",
        "citations_requested", "links_requested", "json_requested",
    )
    output_preferences = {key: raw_preferences.get(key) is True for key in preference_keys}

    raw_context = value.get("context_resolution")
    raw_context = raw_context if isinstance(raw_context, dict) else {}
    raw_slots = raw_context.get("slots")
    slots: dict[str, str] = {}
    if isinstance(raw_slots, dict):
        for raw_key, raw_value in list(raw_slots.items())[:16]:
            key = clean_text(raw_key, 40)
            item = clean_text(raw_value, 180)
            if key and item:
                slots[key] = item
    context_resolution = {
        "method": clean_text(raw_context.get("method"), 80) or "not_provided",
        "resolved_question": clean_text(raw_context.get("resolved_question"), MAX_TASK_CHARS),
        "topic": clean_text(raw_context.get("topic"), 180),
        "entities": clean_list(raw_context.get("entities"), items=8, chars=120),
        "slots": slots,
        "changed_slots": clean_list(raw_context.get("changed_slots"), items=8, chars=40),
        "is_follow_up": raw_context.get("is_follow_up") is True,
        "topic_shift": raw_context.get("topic_shift") is True,
        "resolution_basis": clean_text(raw_context.get("resolution_basis"), 80) or "unassessed",
        "confidence_band": (
            raw_context.get("confidence_band")
            if isinstance(raw_context.get("confidence_band"), str)
            and raw_context.get("confidence_band") in {"low", "medium", "high", "unassessed"}
            else "unassessed"
        ),
        "needs_clarification": raw_context.get("needs_clarification") is True,
        "unresolved_references": clean_list(raw_context.get("unresolved_references"), items=8, chars=100),
    }

    raw_hypotheses = value.get("hypothesis_interpretations")
    hypotheses: list[dict[str, Any]] = []
    if isinstance(raw_hypotheses, list):
        for item in raw_hypotheses[:8]:
            if not isinstance(item, dict):
                continue
            count = item.get("matched_signal_count")
            hypotheses.append({
                "family": clean_text(item.get("family"), 80),
                "matched_signal_count": max(0, min(32, count)) if isinstance(count, int) else 0,
                "signals": clean_list(item.get("signals"), items=4, chars=100),
                "status": clean_text(item.get("status"), 60) or "unassessed",
                "selected": item.get("selected") is True,
            })

    allowed_families = {
        name for name in _PATTERNS if not name.startswith("output_")
    } | {"general_question", "ambiguous_or_incomplete", "web_research"}
    raw_family = clean_text(value.get("task_family"), 80)
    raw_mode = clean_text(value.get("mode"), 20)
    raw_route = clean_text(value.get("intent_route"), 40)
    allowed_routes = {
        "LOCAL", "MODEL_ONLY", "CLARIFY", "WEB_SIMPLE", "WEB_DEEP",
        "LEAD_GENERATION", "BUDGET_EXHAUSTED", "deterministic_fallback",
        "validated_language_model_plan", "unassessed",
    }
    allowed_tools = {
        "web_search", "page_fetch", "public_social_search_if_configured",
        "language_model_generation_if_configured", "claim_review_if_configured",
    }
    allowed_slots = {
        "aspect", "audience", "budget", "capacity", "country", "currency",
        "entity", "goal", "language", "location", "model", "platform",
        "product", "time_range", "variant", "version",
    }
    context_resolution["slots"] = {
        key: item for key, item in context_resolution["slots"].items()
        if key in allowed_slots
    }
    hypotheses = [
        item for item in hypotheses
        if item.get("family") in allowed_families
    ]
    raw_secondary = clean_list(value.get("secondary_task_types"), items=16, chars=80)
    spec = {
        "schema": "omarai.task_spec.v1",
        "task_family": raw_family if raw_family in allowed_families else "general_question",
        "mode": raw_mode if raw_mode in SUPPORTED_MODES else "auto",
        "intent_route": raw_route if raw_route in allowed_routes else "unassessed",
        "classification_method": clean_text(value.get("classification_method"), 100),
        "classification_is_probability": False,
        "ambiguity_status": clean_text(value.get("ambiguity_status"), 80) or "unassessed",
        "missing_required_inputs": [
            item for item in clean_list(value.get("missing_required_inputs"), items=8, chars=100)
            if item in {
                "unresolved_referent_or_incomplete_request",
                "official_destination_target_entity",
                "summary_source_url_or_pasted_text",
            }
        ],
        "requires_clarification": value.get("requires_clarification") is True,
        "clarification_reason": clean_text(value.get("clarification_reason"), 80) or "unassessed",
        "context_resolution": context_resolution,
        "secondary_task_types": [
            item for item in raw_secondary if item in allowed_families
        ],
        "constraints": constraints,
        "output_preferences": output_preferences,
        "evidence_requirements": clean_list(value.get("evidence_requirements"), items=32, chars=180),
        "query_strategies": clean_list(value.get("query_strategies"), items=32, chars=100),
        "tool_requirements": [
            item for item in clean_list(value.get("tool_requirements"), items=12, chars=100)
            if item in allowed_tools
        ],
        "decision_checks": clean_list(value.get("decision_checks"), items=24, chars=120),
        "reasoning_strategy_ids": [
            item for item in clean_list(value.get("reasoning_strategy_ids"), items=12, chars=80)
            if item in _REASONING_GUIDANCE
        ],
        # The matrix is code-owned. Ignore arbitrary incoming rows and return the
        # canonical allowlisted policy so untrusted task/planner data cannot rewrite it.
        "decision_matrix": [dict(row) for row in _DECISION_MATRIX],
        "hypothesis_interpretations": hypotheses,
        "limits": {
            "max_question_chars": MAX_TASK_CHARS,
            "max_aspects": MAX_TASK_ASPECTS,
            "max_query_strategies": MAX_STRATEGY_QUERIES,
        },
        "claim": "task planning metadata only; not semantic certainty or factual verification",
    }
    for key in ("planner_freshness", "planner_depth"):
        if key in value:
            spec[key] = clean_text(value.get(key), 40) or "unknown"
    return spec
