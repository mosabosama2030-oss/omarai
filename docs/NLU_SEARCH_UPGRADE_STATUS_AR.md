# حالة دمج حزمة NLU/Search على الفرع

**الفرع:** `feat/nlu-search-upgrade-pack-2026-10-28`
**الأساس:** `main` @ `40a55792e765` (بعد دمج #109 سياق المتابعة)

## ما يُدفع على الفرع
- وحدات: aspect_planning, search_connectors, context_followup, answer_transparency, nlu_search_integration
- ربط `agents/research.py`: `fallback_plan` / `validate_plan` عبر `augment_plan_with_aspects`
- اختبارات الحزمة
- نقاط ربط `web_agent` موثّقة في `docs/WEB_AGENT_WIRE_AR.md` (تطبيق مباشر على الملف الكبير حسب حجم الدفع)

## ما لم يُنفَّذ
- دمج إلى main تلقائيًا
- نشر استضافة
- Hosted smoke

## الأمان
- عتبة الصلة 0.20 دون خفض
- SSRF دون إضعاف
