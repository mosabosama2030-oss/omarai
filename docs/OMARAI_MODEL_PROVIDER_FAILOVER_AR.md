# إعداد موفري النماذج والاحتياط — Gemini وMistral

**الحالة:** دعم برمجي واختبارات Mock؛ لا يعني وجود مفتاح أن الاتصال الحي تحقق.

## 1. الإعداد

لا تضع مفاتيح API في Git أو ملفات الواجهة أو سجلات التشغيل. أضفها كمتغيرات بيئة في بيئة التشغيل بعد مراجعة التكلفة وسياسة البيانات:

```bash
export GEMINI_API_KEY="..."
export MISTRAL_API_KEY="..."
```

الافتراضات الحالية (يمكن تغييرها فقط إلى معرفات مثبتة في كتالوج المورد):

- Gemini: `gemini-3.1-flash-lite`
- Mistral: `mistral-small-latest` (API alias لنموذج Mistral Small 4)

يمكن تجاوز المعرفين عبر `OMARAI_GEMINI_MODEL` و`OMARAI_MISTRAL_MODEL`.

## 2. ترتيب اختيار المزود

1. `OMARAI_LLM_API_KEY` أو `OPENROUTER_API_KEY` مع `OMARAI_LLM_BASE_URL` هو المزود الأساسي إن وُجد.
2. إذا لم يوجد مفتاح عام، يصبح Gemini أساسيًا عند توفر `GEMINI_API_KEY`.
3. إذا لم يوجد ما سبق، يصبح Mistral أساسيًا عند توفر `MISTRAL_API_KEY`.
4. بعد فشل المحاولات الأساسية، يُجرب النموذج الاحتياطي للمزود الأساسي إن كان مضبوطًا، ثم المزودون البدلاء المتاحون.
5. أداة OpenRouter web search لا تُرسل إلى Gemini أو Mistral.
6. semantic claim verifier يستخدم `allow_fallback=False`؛ لا تنتقل مطالبة التحقق إلى مزود آخر بصمت.

يُسجل 429 كـ`rate_limited` و401/403 كـ`unauthorized` دون تخزين جسم استجابة المزود أو بيانات الاعتماد.

## 3. الخصوصية والتكلفة

قد تُرسل المطالبات ومقتطفات الصفحات إلى المزود الأساسي، ثم إلى مزود بديل عند الفشل. لا ترسل أسرارًا أو بيانات شخصية/تجارية سرية في المطالبات. تحقق من شروط الاحتفاظ بالبيانات والأسعار والحصص لكل حساب قبل التفعيل.

لا تنفذ اختبارات حية أو مدفوعة تلقائيًا. `GET /api/health` يعرض لقطة إعدادات لا اتصالًا مثبتًا. تشخيص المزود الحي عبر `POST /api/diagnostics` يتطلب موافقة صريحة `allow_provider_usage=true` وعضوية owner، وقد يستهلك حصة أو تكلفة.

## 4. الاختبارات

تغطي اختبارات `tests/test_model_provider_failover.py` اختيار المزود، معرفات النماذج الافتراضية، الانتقال عند الفشل، عدم تسريب مفاتيح في status، منع انتقال semantic verifier، وحصر أداة OpenRouter في OpenRouter. هذه اختبارات Mock وليست اختبار اتصال فعلي.

## 5. المراجع الرسمية

- [Google Gemini OpenAI compatibility](https://ai.google.dev/gemini-api/docs/openai)
- [Google Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite)
- [Mistral Small 4 model card](https://docs.mistral.ai/models/mistral-small-4-0-26-03)
- [Mistral API playground and model aliases](https://docs.mistral.ai/getting-started/quickstarts/studio/test-model-playground)
