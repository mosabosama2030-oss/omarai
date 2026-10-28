# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **013**
- سجلات الأسطر: **800**
- النطاق: SRC-D57B0BB030-L000053 إلى SRC-E599346ABE-L000679
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## وثائق وفهرسة

### FILE-D57B0BB030 — [docs/DEPLOY_RENDER_AR.md](../DEPLOY_RENDER_AR.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-D57B0BB030-L000053](../DEPLOY_RENDER_AR.md#L53) | 53 | `""` | — |
| [SRC-D57B0BB030-L000054](../DEPLOY_RENDER_AR.md#L54) | 54 | ``"ملف قبول التشغيل `scripts/hosted_smoke_test.py` متاح على الفرع الذي أُعدّت فيه هذه الحزمة. بعد دمجه في `main`، أضف GitHub Actions secrets باسم `OMARAI_ACCESS_TOKEN` (نفس رمز الخدمة) و`OMARAI_BASE_URL` (أصل HTTPS للخدمة فقط)، ثم شغّل workflow اليدوي `Omarai hosted acceptance smoke`. يستخدم الاختبار العنوان المحفوظ في إعدادات المستودع لتجنب إرسال رمز الوصول إلى عنوان حرّ. الاختبار ينفذ اتصالات بحث ونموذج فعلية وقد يستهلك استخدامًا من حساب المزود."`` | — |
| [SRC-D57B0BB030-L000055](../DEPLOY_RENDER_AR.md#L55) | 55 | `""` | — |
| [SRC-D57B0BB030-L000056](../DEPLOY_RENDER_AR.md#L56) | 56 | `"إذا لم تدمج حزمة الاختبار بعد، استخدم زر الاختبار الحي المدمج في واجهة Omarai، ثم أجرِ فحص HTTP 401 دون رمز وصول، وتجربة سؤال عربي ومراجعة المصادر."` | — |
| [SRC-D57B0BB030-L000057](../DEPLOY_RENDER_AR.md#L57) | 57 | `""` | — |
| [SRC-D57B0BB030-L000058](../DEPLOY_RENDER_AR.md#L58) | 58 | `"## إذا فشل النشر"` | — |
| [SRC-D57B0BB030-L000059](../DEPLOY_RENDER_AR.md#L59) | 59 | `""` | — |
| [SRC-D57B0BB030-L000060](../DEPLOY_RENDER_AR.md#L60) | 60 | `"- افتح Logs على Render، ولا تنشر أي قيمة سرية في Issue عام."` | — |
| [SRC-D57B0BB030-L000061](../DEPLOY_RENDER_AR.md#L61) | 61 | ``"- تحقق أن الخادم يستمع على الواجهة العامة والمنفذ الذي توفره بيئة الاستضافة؛ يستخدم Dockerfile الحالي متغير `PORT`."`` | — |
| [SRC-D57B0BB030-L000062](../DEPLOY_RENDER_AR.md#L62) | 62 | ``"- إذا كانت الخدمة تبدأ ثم تفشل فحص الصحة، راجع أن `/api/health` يعيد HTTP 200."`` | — |
| [SRC-D57B0BB030-L000063](../DEPLOY_RENDER_AR.md#L63) | 63 | ``"- تحقق أن `OMARAI_PUBLIC_DEPLOYMENT=1` ورمز الوصول مضبوطين، وأن الرمز 32 حرفًا على الأقل."`` | — |
| [SRC-D57B0BB030-L000064](../DEPLOY_RENDER_AR.md#L64) | 64 | `"- إذا فشل النموذج، تحقق من صحة مفتاح المزود وحدوده. وإذا فشل البحث فقط، قد تكون محركات البحث العامة حظرت الطلب أو لم ترجع نتائج قابلة للتحليل."` | — |
| [SRC-D57B0BB030-L000065](../DEPLOY_RENDER_AR.md#L65) | 65 | `""` | — |
| [SRC-D57B0BB030-L000066](../DEPLOY_RENDER_AR.md#L66) | 66 | `"راجع كذلك [دليل القبول العام](GO_LIVE_CHECKLIST_AR.md) قبل اعتماد النسخة."` | — |
## وثائق وفهرسة

### FILE-51D44BE378 — [docs/DEPLOY_SNAPDEPLOY_AR.md](../DEPLOY_SNAPDEPLOY_AR.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-51D44BE378-L000001](../DEPLOY_SNAPDEPLOY_AR.md#L1) | 1 | `"# نشر Omarai على SnapDeploy Free — دليل عربي"` | — |
| [SRC-51D44BE378-L000002](../DEPLOY_SNAPDEPLOY_AR.md#L2) | 2 | `""` | — |
| [SRC-51D44BE378-L000003](../DEPLOY_SNAPDEPLOY_AR.md#L3) | 3 | ``"هذا دليل بديل للنشر بعد تعذّر Render. الإعداد الموجود في المستودع متوافق مبدئيًا مع تشغيل Docker على SnapDeploy: `Dockerfile` في جذر المشروع، وخادم يستمع على `0.0.0.0` والمنفذ الذي توفره البيئة، وفحص صحة عبر `/api/health`. **هذا الدليل لا يعني أن حسابًا أو خدمة قد أُنشئت بالفعل.**"`` | — |
| [SRC-51D44BE378-L000004](../DEPLOY_SNAPDEPLOY_AR.md#L4) | 4 | `""` | — |
| [SRC-51D44BE378-L000005](../DEPLOY_SNAPDEPLOY_AR.md#L5) | 5 | `"## حدود الخطة المجانية — راجعها قبل النشر"` | — |
| [SRC-51D44BE378-L000006](../DEPLOY_SNAPDEPLOY_AR.md#L6) | 6 | `""` | — |
| [SRC-51D44BE378-L000007](../DEPLOY_SNAPDEPLOY_AR.md#L7) | 7 | `"بحسب وثائق SnapDeploy الحالية وقت كتابة الدليل:"` | — |
| [SRC-51D44BE378-L000008](../DEPLOY_SNAPDEPLOY_AR.md#L8) | 8 | `"- لا يلزم إدخال بطاقة دفع للبدء في الخطة المجانية."` | — |
| [SRC-51D44BE378-L000009](../DEPLOY_SNAPDEPLOY_AR.md#L9) | 9 | `"- الحد المشترك هو 100 ساعة تشغيل للحاويات شهريًا، وحتى 4 حاويات بالحجم الصغير."` | — |
| [SRC-51D44BE378-L000010](../DEPLOY_SNAPDEPLOY_AR.md#L10) | 10 | `"- الحاوية الصغيرة لها 512 MB RAM و0.25 vCPU، وتدخل في السكون بعد نحو 15 دقيقة بلا زيارات؛ قد يستغرق الاستيقاظ قرابة 60 ثانية."` | — |
| [SRC-51D44BE378-L000011](../DEPLOY_SNAPDEPLOY_AR.md#L11) | 11 | `"- لا يوجد قرص دائم في الخطة المجانية؛ يُعاد ضبط نظام الملفات عند الاستيقاظ أو إعادة التشغيل أو النشر."` | — |
| [SRC-51D44BE378-L000012](../DEPLOY_SNAPDEPLOY_AR.md#L12) | 12 | `"- يحصل التطبيق على عنوان HTTPS فرعي وشهادة TLS."` | — |
| [SRC-51D44BE378-L000013](../DEPLOY_SNAPDEPLOY_AR.md#L13) | 13 | `""` | — |
| [SRC-51D44BE378-L000014](../DEPLOY_SNAPDEPLOY_AR.md#L14) | 14 | `"قد تتغير الحدود والشروط؛ راجع [وثائق الخطة المجانية](https://snapdeploy.dev/docs/free-tier) قبل المتابعة. الخطة مناسبة لتجربة شخصية واختبار قبول، وليست تشغيلًا دائمًا أو مكانًا لحفظ بيانات عملاء."` | — |
| [SRC-51D44BE378-L000015](../DEPLOY_SNAPDEPLOY_AR.md#L15) | 15 | `""` | — |
| [SRC-51D44BE378-L000016](../DEPLOY_SNAPDEPLOY_AR.md#L16) | 16 | `"## 1. إنشاء الحساب وربط GitHub"` | — |
| [SRC-51D44BE378-L000017](../DEPLOY_SNAPDEPLOY_AR.md#L17) | 17 | `""` | — |
| [SRC-51D44BE378-L000018](../DEPLOY_SNAPDEPLOY_AR.md#L18) | 18 | `"1. افتح [SnapDeploy](https://snapdeploy.dev/) من متصفح الهاتف وأنشئ حسابًا بالبريد أو عبر GitHub."` | — |
| [SRC-51D44BE378-L000019](../DEPLOY_SNAPDEPLOY_AR.md#L19) | 19 | `"2. أكّد البريد إذا طُلب ذلك، ثم افتح لوحة التحكم."` | — |
| [SRC-51D44BE378-L000020](../DEPLOY_SNAPDEPLOY_AR.md#L20) | 20 | `"3. اختر **Deploy** ثم طريقة النشر من **GitHub repository**."` | — |
| [SRC-51D44BE378-L000021](../DEPLOY_SNAPDEPLOY_AR.md#L21) | 21 | `"4. اربط حساب GitHub. إذا ظهرت إعدادات اختيار المستودعات، امنح الحد الأدنى من الوصول المطلوب بدل توسيع الصلاحيات بلا حاجة."` | — |
| [SRC-51D44BE378-L000022](../DEPLOY_SNAPDEPLOY_AR.md#L22) | 22 | ``"5. اختر المستودع `mosabosama2030-oss/omarai)، والفرع `main)، ومجلد الجذر الذي يحتوي على `Dockerfile`."`` | — |
| [SRC-51D44BE378-L000023](../DEPLOY_SNAPDEPLOY_AR.md#L23) | 23 | ``"6. تأكد أن المنصة اكتشفت `Dockerfile` الموجود في جذر المستودع. لا تحتاج إلى إنشاء ملف إعدادات خاص بالمنصة لهذه النسخة."`` | — |
| [SRC-51D44BE378-L000024](../DEPLOY_SNAPDEPLOY_AR.md#L24) | 24 | `""` | — |
| [SRC-51D44BE378-L000025](../DEPLOY_SNAPDEPLOY_AR.md#L25) | 25 | `"## ربط نسخة النشر بالمصدر"` | — |
| [SRC-51D44BE378-L000026](../DEPLOY_SNAPDEPLOY_AR.md#L26) | 26 | `""` | — |
| [SRC-51D44BE378-L000027](../DEPLOY_SNAPDEPLOY_AR.md#L27) | 27 | ``"لا يكفي أن يعمل `/api/health`؛ يجب أن يمكن ربط الخدمة بالالتزام الذي بُنيت منه الصورة. يمرر SnapDeploy متغيرات البناء ذات البادئات العامة مثل `PUBLIC_*` إلى وسيطات بناء Docker، بينما تكون المتغيرات الأخرى متاحة وقت التشغيل فقط، وفق [توثيقه الرسمي](https://snapdeploy.dev/docs/deployment) و[دليل متغيرات البيئة](https://snapdeploy.dev/docs/environment-variables)."`` | — |
| [SRC-51D44BE378-L000028](../DEPLOY_SNAPDEPLOY_AR.md#L28) | 28 | `""` | — |
| [SRC-51D44BE378-L000029](../DEPLOY_SNAPDEPLOY_AR.md#L29) | 29 | `"### إعداد هوية البناء على SnapDeploy"` | — |
| [SRC-51D44BE378-L000030](../DEPLOY_SNAPDEPLOY_AR.md#L30) | 30 | `""` | — |
| [SRC-51D44BE378-L000031](../DEPLOY_SNAPDEPLOY_AR.md#L31) | 31 | ``"1. بعد تحديد التزام `main` الذي تريد تشغيله، انسخ SHA الكامل المكوّن من 40 حرفًا."`` | — |
| [SRC-51D44BE378-L000032](../DEPLOY_SNAPDEPLOY_AR.md#L32) | 32 | ``"2. أضف أو حدّث متغير البيئة غير السري `PUBLIC_OMARAI_BUILD_SHA` على خدمة SnapDeploy واجعل قيمته هي SHA نفسه. هذا المتغير بيانات إصدار علنية وليست رمز وصول أو مفتاح API؛ لا تستخدم البادئة العامة مطلقًا لأي سر."`` | — |
| [SRC-51D44BE378-L000033](../DEPLOY_SNAPDEPLOY_AR.md#L33) | 33 | ``"3. أعد بناء الخدمة/نشرها بعد تعيين القيمة. يقرأ Dockerfile `PUBLIC_OMARAI_BUILD_SHA` كبديل لوسيط `OMARAI_BUILD_SHA` التقليدي، ويتحقق من شكله قبل كتابة ملف هوية البناء."`` | — |
| [SRC-51D44BE378-L000034](../DEPLOY_SNAPDEPLOY_AR.md#L34) | 34 | ``"4. افتح `/api/health` وتحقق من أن `build.sha` يطابق الالتزام الكامل الذي اخترته بالضبط، وأن `sha_status=available` و`sha_source=image_baked`."`` | — |
| [SRC-51D44BE378-L000035](../DEPLOY_SNAPDEPLOY_AR.md#L35) | 35 | `""` | — |
| [SRC-51D44BE378-L000036](../DEPLOY_SNAPDEPLOY_AR.md#L36) | 36 | `"في بيئات Docker التي تسمح بتمرير وسيطات البناء مباشرة، يظل هذا الأمر مدعومًا:"` | — |
| [SRC-51D44BE378-L000037](../DEPLOY_SNAPDEPLOY_AR.md#L37) | 37 | `""` | — |
| [SRC-51D44BE378-L000038](../DEPLOY_SNAPDEPLOY_AR.md#L38) | 38 | ````"```bash"```` | — |
| [SRC-51D44BE378-L000039](../DEPLOY_SNAPDEPLOY_AR.md#L39) | 39 | `"docker build --build-arg OMARAI_BUILD_SHA=\"$(git rev-parse HEAD)\" ."` | — |
| [SRC-51D44BE378-L000040](../DEPLOY_SNAPDEPLOY_AR.md#L40) | 40 | ````"```"```` | — |
| [SRC-51D44BE378-L000041](../DEPLOY_SNAPDEPLOY_AR.md#L41) | 41 | `""` | — |
| [SRC-51D44BE378-L000042](../DEPLOY_SNAPDEPLOY_AR.md#L42) | 42 | ``"لا تعلن قبول الإصدار إذا ظلت قيمة `build.sha` تساوي `unknown`. تغيير قيمة المتغير وحده أو نجاح صفحة الصحة لا يثبت أن مزودي البحث أو النموذج يعملون؛ أكمل اختبارات القبول الحية بشكل منفصل."`` | — |
| [SRC-51D44BE378-L000043](../DEPLOY_SNAPDEPLOY_AR.md#L43) | 43 | `""` | — |
| [SRC-51D44BE378-L000044](../DEPLOY_SNAPDEPLOY_AR.md#L44) | 44 | `"## 2. ضبط متغيرات البيئة والأسرار"` | — |
| [SRC-51D44BE378-L000045](../DEPLOY_SNAPDEPLOY_AR.md#L45) | 45 | `""` | — |
| [SRC-51D44BE378-L000046](../DEPLOY_SNAPDEPLOY_AR.md#L46) | 46 | ``"قد تعرض المنصة متغيرات مكتشفة من `.env.example`. القيم المكتوبة على شكل أمثلة ليست أسرارًا صالحة؛ استبدلها بقيمك الحقيقية في لوحة SnapDeploy فقط."`` | — |
| [SRC-51D44BE378-L000047](../DEPLOY_SNAPDEPLOY_AR.md#L47) | 47 | `""` | — |
| [SRC-51D44BE378-L000048](../DEPLOY_SNAPDEPLOY_AR.md#L48) | 48 | `"أضف أو اضبط المتغيرات الثلاثة التالية:"` | — |
| [SRC-51D44BE378-L000049](../DEPLOY_SNAPDEPLOY_AR.md#L49) | 49 | `""` | — |
| [SRC-51D44BE378-L000050](../DEPLOY_SNAPDEPLOY_AR.md#L50) | 50 | `"\| المتغير \| القيمة \|"` | — |
| [SRC-51D44BE378-L000051](../DEPLOY_SNAPDEPLOY_AR.md#L51) | 51 | `"\|---\|---\|"` | — |
| [SRC-51D44BE378-L000052](../DEPLOY_SNAPDEPLOY_AR.md#L52) | 52 | ``"\| `OMARAI_PUBLIC_DEPLOYMENT` \| `1` \|"`` | — |
| [SRC-51D44BE378-L000053](../DEPLOY_SNAPDEPLOY_AR.md#L53) | 53 | ``"\| `OMARAI_ACCESS_TOKEN` \| رمز وصول عشوائي خاص بك، طوله 32 حرفًا على الأقل \|"`` | — |
| [SRC-51D44BE378-L000054](../DEPLOY_SNAPDEPLOY_AR.md#L54) | 54 | ``"\| `OPENROUTER_API_KEY` \| مفتاح OpenRouter الخاص بك لتوليد الإجابات والتحليل \|"`` | — |
| [SRC-51D44BE378-L000055](../DEPLOY_SNAPDEPLOY_AR.md#L55) | 55 | `""` | — |
| [SRC-51D44BE378-L000056](../DEPLOY_SNAPDEPLOY_AR.md#L56) | 56 | `"أنشئ رمز الوصول في Termux محليًا باستخدام Python، ثم انسخه مباشرة إلى خانة السر في SnapDeploy:"` | — |
| [SRC-51D44BE378-L000057](../DEPLOY_SNAPDEPLOY_AR.md#L57) | 57 | `""` | — |
| [SRC-51D44BE378-L000058](../DEPLOY_SNAPDEPLOY_AR.md#L58) | 58 | ````"```bash"```` | — |
| [SRC-51D44BE378-L000059](../DEPLOY_SNAPDEPLOY_AR.md#L59) | 59 | `"python -c \"import secrets; print(secrets.token_urlsafe(48))\""` | — |
| [SRC-51D44BE378-L000060](../DEPLOY_SNAPDEPLOY_AR.md#L60) | 60 | ````"```"```` | — |
| [SRC-51D44BE378-L000061](../DEPLOY_SNAPDEPLOY_AR.md#L61) | 61 | `""` | — |
| [SRC-51D44BE378-L000062](../DEPLOY_SNAPDEPLOY_AR.md#L62) | 62 | `"لا ترسل الرمز أو مفتاح OpenRouter إلى ChatGPT أو DeepSeek، ولا تضعهما في GitHub أو ملف README أو لقطات شاشة. لا تستخدم مفتاح OpenRouter نفسه رمزًا لدخول التطبيق."` | — |
| [SRC-51D44BE378-L000063](../DEPLOY_SNAPDEPLOY_AR.md#L63) | 63 | `""` | — |
| [SRC-51D44BE378-L000064](../DEPLOY_SNAPDEPLOY_AR.md#L64) | 64 | ``"اترك `OMARAI_OPENROUTER_WEB_SEARCH` غير مضبوط؛ تفعيله خيار إضافي يمكن أن يستهلك رصيدًا. استخدام النماذج المجانية قد يظل خاضعًا لحصص ومعدلات توفر المزود، وقد تتغير النماذج المتاحة. راجع التسعير وحدود المفتاح لدى OpenRouter ولا توافق على موارد أو استخدام مدفوع."`` | — |
| [SRC-51D44BE378-L000065](../DEPLOY_SNAPDEPLOY_AR.md#L65) | 65 | `""` | — |
| [SRC-51D44BE378-L000066](../DEPLOY_SNAPDEPLOY_AR.md#L66) | 66 | `"## 3. النشر الأول"` | — |
| [SRC-51D44BE378-L000067](../DEPLOY_SNAPDEPLOY_AR.md#L67) | 67 | `""` | — |
| [SRC-51D44BE378-L000068](../DEPLOY_SNAPDEPLOY_AR.md#L68) | 68 | `"1. راجع اختيار المستودع والفرع والمتغيرات مرة أخيرة."` | — |
| [SRC-51D44BE378-L000069](../DEPLOY_SNAPDEPLOY_AR.md#L69) | 69 | `"2. اضغط **Deploy** مرة واحدة وانتظر نتيجة البناء والتشغيل."` | — |
| [SRC-51D44BE378-L000070](../DEPLOY_SNAPDEPLOY_AR.md#L70) | 70 | `"3. إذا فشل البناء، افتح سجل البناء واقرأ أول خطأ حقيقي قبل إعادة المحاولة؛ المحاولات الفاشلة قد تُحتسب ضمن حد النشر اليومي."` | — |
| [SRC-51D44BE378-L000071](../DEPLOY_SNAPDEPLOY_AR.md#L71) | 71 | `"4. افتح عنوان HTTPS الذي أعطته المنصة. قد تكون أول زيارة بعد السكون صفحة استيقاظ أو تحتاج إلى الانتظار قرابة دقيقة."` | — |
| [SRC-51D44BE378-L000072](../DEPLOY_SNAPDEPLOY_AR.md#L72) | 72 | ``"5. افتح `https://عنوان-خدمتك/api/health`. النجاح المبدئي هو استجابة HTTP 200 ومحتوى JSON يحتوي على `\"ok\": true`. نجاح الصحة وحده لا يثبت أن البحث والنموذج يعملان."`` | — |
| [SRC-51D44BE378-L000073](../DEPLOY_SNAPDEPLOY_AR.md#L73) | 73 | `""` | — |
| [SRC-51D44BE378-L000074](../DEPLOY_SNAPDEPLOY_AR.md#L74) | 74 | `"## 4. اختبار Omarai من الهاتف"` | — |
| [SRC-51D44BE378-L000075](../DEPLOY_SNAPDEPLOY_AR.md#L75) | 75 | `""` | — |
| [SRC-51D44BE378-L000076](../DEPLOY_SNAPDEPLOY_AR.md#L76) | 76 | `"1. افتح الصفحة الرئيسية للرابط المستضاف."` | — |
| [SRC-51D44BE378-L000077](../DEPLOY_SNAPDEPLOY_AR.md#L77) | 77 | ``"2. أدخل `OMARAI_ACCESS_TOKEN` في خانة الوصول الآمن داخل الواجهة واحفظه على هذا الجهاز فقط."`` | — |
| [SRC-51D44BE378-L000078](../DEPLOY_SNAPDEPLOY_AR.md#L78) | 78 | `"3. شغّل زر **اختبار حي للإنترنت والنموذج**."` | — |
| [SRC-51D44BE378-L000079](../DEPLOY_SNAPDEPLOY_AR.md#L79) | 79 | `"4. أرسل سؤالًا عامًا بالعربية، مثل: «ما عاصمة مصر؟ اذكر مصادر قابلة للفتح». تأكد من ظهور إجابة ومصادر حقيقية، وافتح مصدرًا واحدًا على الأقل."` | — |
| [SRC-51D44BE378-L000080](../DEPLOY_SNAPDEPLOY_AR.md#L80) | 80 | `"5. جرّب الطلب برمز غير صحيح وتأكد من رفض الوصول. لا تختبر ببيانات شخصية أو بيانات عملاء."` | — |
| [SRC-51D44BE378-L000081](../DEPLOY_SNAPDEPLOY_AR.md#L81) | 81 | `"6. لا تعتبر النشر مقبولًا إذا نجحت الصفحة فقط وفشل تشخيص البحث أو النموذج."` | — |
| [SRC-51D44BE378-L000082](../DEPLOY_SNAPDEPLOY_AR.md#L82) | 82 | `""` | — |
| [SRC-51D44BE378-L000083](../DEPLOY_SNAPDEPLOY_AR.md#L83) | 83 | `"## 5. اختبار القبول الآلي الاختياري"` | — |
| [SRC-51D44BE378-L000084](../DEPLOY_SNAPDEPLOY_AR.md#L84) | 84 | `""` | — |
| [SRC-51D44BE378-L000085](../DEPLOY_SNAPDEPLOY_AR.md#L85) | 85 | `"المستودع يحتوي على workflow يدوي باسم **Omarai hosted acceptance smoke** في GitHub Actions. بعد أن تكون الخدمة قد استيقظت وتعمل:"` | — |
| [SRC-51D44BE378-L000086](../DEPLOY_SNAPDEPLOY_AR.md#L86) | 86 | `""` | — |
| [SRC-51D44BE378-L000087](../DEPLOY_SNAPDEPLOY_AR.md#L87) | 87 | `"1. افتح إعدادات المستودع في GitHub ثم **Settings → Secrets and variables → Actions**."` | — |
| [SRC-51D44BE378-L000088](../DEPLOY_SNAPDEPLOY_AR.md#L88) | 88 | ``"2. أضف Secret باسم `OMARAI_ACCESS_TOKEN`، والقيمة مطابقة تمامًا لرمز التطبيق في SnapDeploy."`` | — |
| [SRC-51D44BE378-L000089](../DEPLOY_SNAPDEPLOY_AR.md#L89) | 89 | ``"3. أضف Secret باسم `OMARAI_BASE_URL`، والقيمة هي أصل HTTPS فقط، مثل `https://your-service.containers.snapdeploy.app`؛ لا تضف `/api` ولا الرمز إلى الرابط."`` | — |
| [SRC-51D44BE378-L000090](../DEPLOY_SNAPDEPLOY_AR.md#L90) | 90 | `"4. افتح **Actions → Omarai hosted acceptance smoke → Run workflow**."` | — |
| [SRC-51D44BE378-L000091](../DEPLOY_SNAPDEPLOY_AR.md#L91) | 91 | `"5. راجع نتيجة الفحص. الاختبار يتصل فعليًا بالبحث والنموذج ويمكن أن يستهلك حصة المزود. لا تشغله حتى تكون موافقًا على هذا الاستخدام. خدمات SnapDeploy النائمة قد لا تستيقظ عبر طلبات CI؛ افتح الرابط يدويًا أولًا وانتظر اكتمال الاستيقاظ."` | — |
| [SRC-51D44BE378-L000092](../DEPLOY_SNAPDEPLOY_AR.md#L92) | 92 | `""` | — |
| [SRC-51D44BE378-L000093](../DEPLOY_SNAPDEPLOY_AR.md#L93) | 93 | `"لا تنشر سجلًا يحتوي على أسرار. احذف أو احجب أي رموز من السجلات قبل مشاركتها."` | — |
| [SRC-51D44BE378-L000094](../DEPLOY_SNAPDEPLOY_AR.md#L94) | 94 | `""` | — |
| [SRC-51D44BE378-L000095](../DEPLOY_SNAPDEPLOY_AR.md#L95) | 95 | `"## القيود الحالية التي لا يحلها النشر"` | — |
| [SRC-51D44BE378-L000096](../DEPLOY_SNAPDEPLOY_AR.md#L96) | 96 | `""` | — |
| [SRC-51D44BE378-L000097](../DEPLOY_SNAPDEPLOY_AR.md#L97) | 97 | `"- Omarai يرسل سؤال المستخدم والسياق المختار ومقتطفات المصادر إلى مزود النموذج الخارجي عند استخدام التوليد؛ لا تُدخل كلمات مرور أو بيانات سرية."` | — |
| [SRC-51D44BE378-L000098](../DEPLOY_SNAPDEPLOY_AR.md#L98) | 98 | `"- البحث العام قد يتعطل أو يتعرض للتحديد والحجب؛ لا يوجد ضمان أن كل سؤال سينجح أو أن كل منصة اجتماعية ستكون قابلة للبحث."` | — |
| [SRC-51D44BE378-L000099](../DEPLOY_SNAPDEPLOY_AR.md#L99) | 99 | ``"- قاعدة العملاء SQLite موجودة محليًا، لكن نظام الملفات المجاني مؤقت. لا تعتمد على `/leads` لحفظ بيانات دائمة؛ قد تضيع البيانات بعد السكون أو إعادة التشغيل أو النشر."`` | — |
| [SRC-51D44BE378-L000100](../DEPLOY_SNAPDEPLOY_AR.md#L100) | 100 | `"- رمز التطبيق مشترك وليس نظام مستخدمين متعددين. لا توزعه على أشخاص لا تثق بهم."` | — |
| [SRC-51D44BE378-L000101](../DEPLOY_SNAPDEPLOY_AR.md#L101) | 101 | `"- لا تعني نتيجة Smoke Test ضمان تشغيل دائم أو تدقيق أمني كامل."` | — |
| [SRC-51D44BE378-L000102](../DEPLOY_SNAPDEPLOY_AR.md#L102) | 102 | `""` | — |
| [SRC-51D44BE378-L000103](../DEPLOY_SNAPDEPLOY_AR.md#L103) | 103 | `"## روابط مرجعية"` | — |
| [SRC-51D44BE378-L000104](../DEPLOY_SNAPDEPLOY_AR.md#L104) | 104 | `""` | — |
| [SRC-51D44BE378-L000105](../DEPLOY_SNAPDEPLOY_AR.md#L105) | 105 | `"- [SnapDeploy — النشر من GitHub](https://snapdeploy.dev/docs/github)"` | — |
| [SRC-51D44BE378-L000106](../DEPLOY_SNAPDEPLOY_AR.md#L106) | 106 | `"- [SnapDeploy — متغيرات البيئة والأسرار](https://snapdeploy.dev/docs/environment-variables)"` | — |
| [SRC-51D44BE378-L000107](../DEPLOY_SNAPDEPLOY_AR.md#L107) | 107 | `"- [SnapDeploy — الخطة المجانية والحدود](https://snapdeploy.dev/docs/free-tier)"` | — |
## وثائق وفهرسة

### FILE-E599346ABE — [docs/generate_index.py](../generate_index.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-E599346ABE-L000001](../generate_index.py#L1) | 1 | `"\"\"\"Generate Omarai's deterministic repository-wide file and source-symbol index.\"\"\""` | — |
| [SRC-E599346ABE-L000002](../generate_index.py#L2) | 2 | `""` | — |
| [SRC-E599346ABE-L000003](../generate_index.py#L3) | 3 | `"from __future__ import annotations"` | — |
| [SRC-E599346ABE-L000004](../generate_index.py#L4) | 4 | `""` | — |
| [SRC-E599346ABE-L000005](../generate_index.py#L5) | 5 | `"import argparse"` | — |
| [SRC-E599346ABE-L000006](../generate_index.py#L6) | 6 | `"import ast"` | — |
| [SRC-E599346ABE-L000007](../generate_index.py#L7) | 7 | `"import hashlib"` | — |
| [SRC-E599346ABE-L000008](../generate_index.py#L8) | 8 | `"import json"` | — |
| [SRC-E599346ABE-L000009](../generate_index.py#L9) | 9 | `"import os"` | — |
| [SRC-E599346ABE-L000010](../generate_index.py#L10) | 10 | `"import posixpath"` | — |
| [SRC-E599346ABE-L000011](../generate_index.py#L11) | 11 | `"import re"` | — |
| [SRC-E599346ABE-L000012](../generate_index.py#L12) | 12 | `"import subprocess"` | — |
| [SRC-E599346ABE-L000013](../generate_index.py#L13) | 13 | `"import sys"` | — |
| [SRC-E599346ABE-L000014](../generate_index.py#L14) | 14 | `"import tempfile"` | — |
| [SRC-E599346ABE-L000015](../generate_index.py#L15) | 15 | `"import tokenize"` | — |
| [SRC-E599346ABE-L000016](../generate_index.py#L16) | 16 | `"from io import StringIO"` | — |
| [SRC-E599346ABE-L000017](../generate_index.py#L17) | 17 | `"from urllib.parse import quote"` | — |
| [SRC-E599346ABE-L000018](../generate_index.py#L18) | 18 | `"from collections.abc import Sequence"` | — |
| [SRC-E599346ABE-L000019](../generate_index.py#L19) | 19 | `"from dataclasses import dataclass"` | — |
| [SRC-E599346ABE-L000020](../generate_index.py#L20) | 20 | `"from pathlib import Path"` | — |
| [SRC-E599346ABE-L000021](../generate_index.py#L21) | 21 | `""` | — |
| [SRC-E599346ABE-L000022](../generate_index.py#L22) | 22 | `"EXCLUDED_DIRECTORIES = frozenset("` | — |
| [SRC-E599346ABE-L000023](../generate_index.py#L23) | 23 | `"    {"` | — |
| [SRC-E599346ABE-L000024](../generate_index.py#L24) | 24 | `"        \".git\","` | — |
| [SRC-E599346ABE-L000025](../generate_index.py#L25) | 25 | `"        \".hg\","` | — |
| [SRC-E599346ABE-L000026](../generate_index.py#L26) | 26 | `"        \".svn\","` | — |
| [SRC-E599346ABE-L000027](../generate_index.py#L27) | 27 | `"        \".venv\","` | — |
| [SRC-E599346ABE-L000028](../generate_index.py#L28) | 28 | `"        \"venv\","` | — |
| [SRC-E599346ABE-L000029](../generate_index.py#L29) | 29 | `"        \"env\","` | — |
| [SRC-E599346ABE-L000030](../generate_index.py#L30) | 30 | `"        \"virtualenv\","` | — |
| [SRC-E599346ABE-L000031](../generate_index.py#L31) | 31 | `"        \"__pycache__\","` | — |
| [SRC-E599346ABE-L000032](../generate_index.py#L32) | 32 | `"        \".pytest_cache\","` | — |
| [SRC-E599346ABE-L000033](../generate_index.py#L33) | 33 | `"        \".ruff_cache\","` | — |
| [SRC-E599346ABE-L000034](../generate_index.py#L34) | 34 | `"        \".mypy_cache\","` | — |
| [SRC-E599346ABE-L000035](../generate_index.py#L35) | 35 | `"        \".tox\","` | — |
| [SRC-E599346ABE-L000036](../generate_index.py#L36) | 36 | `"        \".nox\","` | — |
| [SRC-E599346ABE-L000037](../generate_index.py#L37) | 37 | `"        \"node_modules\","` | — |
| [SRC-E599346ABE-L000038](../generate_index.py#L38) | 38 | `"        \"site-packages\","` | — |
| [SRC-E599346ABE-L000039](../generate_index.py#L39) | 39 | `"        \"build\","` | — |
| [SRC-E599346ABE-L000040](../generate_index.py#L40) | 40 | `"        \"dist\","` | — |
| [SRC-E599346ABE-L000041](../generate_index.py#L41) | 41 | `"    }"` | — |
| [SRC-E599346ABE-L000042](../generate_index.py#L42) | 42 | `")"` | — |
| [SRC-E599346ABE-L000043](../generate_index.py#L43) | 43 | `"SENSITIVE_FILENAMES = frozenset("` | — |
| [SRC-E599346ABE-L000044](../generate_index.py#L44) | 44 | `"    {"` | — |
| [SRC-E599346ABE-L000045](../generate_index.py#L45) | 45 | `"        \".env\","` | — |
| [SRC-E599346ABE-L000046](../generate_index.py#L46) | 46 | `"        \".env.local\","` | — |
| [SRC-E599346ABE-L000047](../generate_index.py#L47) | 47 | `"        \".env.production\","` | — |
| [SRC-E599346ABE-L000048](../generate_index.py#L48) | 48 | `"        \".env.development\","` | — |
| [SRC-E599346ABE-L000049](../generate_index.py#L49) | 49 | `"        \"id_rsa\","` | — |
| [SRC-E599346ABE-L000050](../generate_index.py#L50) | 50 | `"        \"id_ed25519\","` | — |
| [SRC-E599346ABE-L000051](../generate_index.py#L51) | 51 | `"    }"` | — |
| [SRC-E599346ABE-L000052](../generate_index.py#L52) | 52 | `")"` | — |
| [SRC-E599346ABE-L000053](../generate_index.py#L53) | 53 | `"EXCLUDED_SUFFIXES = frozenset("` | — |
| [SRC-E599346ABE-L000054](../generate_index.py#L54) | 54 | `"    {"` | — |
| [SRC-E599346ABE-L000055](../generate_index.py#L55) | 55 | `"        \".pyc\","` | — |
| [SRC-E599346ABE-L000056](../generate_index.py#L56) | 56 | `"        \".pyo\","` | — |
| [SRC-E599346ABE-L000057](../generate_index.py#L57) | 57 | `"        \".sqlite\","` | — |
| [SRC-E599346ABE-L000058](../generate_index.py#L58) | 58 | `"        \".sqlite3\","` | — |
| [SRC-E599346ABE-L000059](../generate_index.py#L59) | 59 | `"        \".db\","` | — |
| [SRC-E599346ABE-L000060](../generate_index.py#L60) | 60 | `"        \".pem\","` | — |
| [SRC-E599346ABE-L000061](../generate_index.py#L61) | 61 | `"        \".key\","` | — |
| [SRC-E599346ABE-L000062](../generate_index.py#L62) | 62 | `"        \".p12\","` | — |
| [SRC-E599346ABE-L000063](../generate_index.py#L63) | 63 | `"        \".pfx\","` | — |
| [SRC-E599346ABE-L000064](../generate_index.py#L64) | 64 | `"    }"` | — |
| [SRC-E599346ABE-L000065](../generate_index.py#L65) | 65 | `")"` | — |
| [SRC-E599346ABE-L000066](../generate_index.py#L66) | 66 | `"MAX_INDEXED_TEXT_BYTES = 2 * 1024 * 1024"` | — |
| [SRC-E599346ABE-L000067](../generate_index.py#L67) | 67 | `"MAX_DESCRIPTION_LENGTH = 240"` | — |
| [SRC-E599346ABE-L000068](../generate_index.py#L68) | 68 | `"INDEX_RELATIVE_PATH = \"docs/MASTER_INDEX.md\""` | — |
| [SRC-E599346ABE-L000069](../generate_index.py#L69) | 69 | `"SOURCE_LINES_INDEX_RELATIVE_PATH = \"docs/SOURCE_LINES_INDEX.md\""` | — |
| [SRC-E599346ABE-L000070](../generate_index.py#L70) | 70 | `"COVERAGE_AUDIT_RELATIVE_PATH = \"docs/INDEX_COVERAGE_AUDIT.md\""` | — |
| [SRC-E599346ABE-L000071](../generate_index.py#L71) | 71 | `"INDEX_OUTPUT_PATHS = frozenset("` | — |
| [SRC-E599346ABE-L000072](../generate_index.py#L72) | 72 | `"    {INDEX_RELATIVE_PATH, SOURCE_LINES_INDEX_RELATIVE_PATH, COVERAGE_AUDIT_RELATIVE_PATH}"` | — |
| [SRC-E599346ABE-L000073](../generate_index.py#L73) | 73 | `")"` | — |
| [SRC-E599346ABE-L000074](../generate_index.py#L74) | 74 | `"SOURCE_LINES_PAGES_DIR = \"docs/source_index\""` | — |
| [SRC-E599346ABE-L000075](../generate_index.py#L75) | 75 | `"SOURCE_LINES_PAGE_SIZE = 800"` | — |
| [SRC-E599346ABE-L000076](../generate_index.py#L76) | 76 | `"SOURCE_LINES_PAGE_RE = re.compile(r\"SOURCE_LINES_\\d{3,}\\.md\")"` | — |
| [SRC-E599346ABE-L000077](../generate_index.py#L77) | 77 | `""` | — |
| [SRC-E599346ABE-L000078](../generate_index.py#L78) | 78 | `"PYTHON_EXTENSIONS = frozenset({\".py\"})"` | — |
| [SRC-E599346ABE-L000079](../generate_index.py#L79) | 79 | `"JAVASCRIPT_EXTENSIONS = frozenset({\".js\", \".mjs\", \".cjs\", \".jsx\", \".ts\", \".tsx\"})"` | — |
| [SRC-E599346ABE-L000080](../generate_index.py#L80) | 80 | `"CSS_EXTENSIONS = frozenset({\".css\", \".scss\"})"` | — |
| [SRC-E599346ABE-L000081](../generate_index.py#L81) | 81 | `"CONFIG_EXTENSIONS = frozenset({\".yml\", \".yaml\", \".toml\", \".json\", \".ini\", \".cfg\"})"` | — |
| [SRC-E599346ABE-L000082](../generate_index.py#L82) | 82 | `"TEXT_SCAN_EXTENSIONS = ("` | — |
| [SRC-E599346ABE-L000083](../generate_index.py#L83) | 83 | `"    PYTHON_EXTENSIONS"` | — |
| [SRC-E599346ABE-L000084](../generate_index.py#L84) | 84 | `"    \| JAVASCRIPT_EXTENSIONS"` | — |
| [SRC-E599346ABE-L000085](../generate_index.py#L85) | 85 | `"    \| CSS_EXTENSIONS"` | — |
| [SRC-E599346ABE-L000086](../generate_index.py#L86) | 86 | `"    \| CONFIG_EXTENSIONS"` | — |
| [SRC-E599346ABE-L000087](../generate_index.py#L87) | 87 | `"    \| frozenset({\".html\", \".htm\", \".sh\", \".md\", \".env.example\", \".example\"})"` | — |
| [SRC-E599346ABE-L000088](../generate_index.py#L88) | 88 | `")"` | — |
| [SRC-E599346ABE-L000089](../generate_index.py#L89) | 89 | `""` | — |
| [SRC-E599346ABE-L000090](../generate_index.py#L90) | 90 | `"JS_IDENTIFIER = r\"[A-Za-z_$][A-Za-z0-9_$]*\""` | — |
| [SRC-E599346ABE-L000091](../generate_index.py#L91) | 91 | `"JS_FUNCTION_RE = re.compile("` | — |
| [SRC-E599346ABE-L000092](../generate_index.py#L92) | 92 | `"    rf\"\\b(?:async\\s+)?function\\s*\\*?\\s+({JS_IDENTIFIER})\\s*\\(\""` | — |
| [SRC-E599346ABE-L000093](../generate_index.py#L93) | 93 | `")"` | — |
| [SRC-E599346ABE-L000094](../generate_index.py#L94) | 94 | `"JS_CLASS_RE = re.compile(rf\"\\bclass\\s+({JS_IDENTIFIER})\\b\")"` | — |
| [SRC-E599346ABE-L000095](../generate_index.py#L95) | 95 | `"JS_ARROW_ASSIGNMENT_RE = re.compile("` | — |
| [SRC-E599346ABE-L000096](../generate_index.py#L96) | 96 | `"    rf\"\\b(?:const\|let\|var)\\s+({JS_IDENTIFIER})\\s*=\\s*\""` | — |
| [SRC-E599346ABE-L000097](../generate_index.py#L97) | 97 | `"    rf\"(?:async\\s*)?(?:\\([^;\\n]*?\\)\|{JS_IDENTIFIER})\\s*=>\""` | — |
| [SRC-E599346ABE-L000098](../generate_index.py#L98) | 98 | `")"` | — |
| [SRC-E599346ABE-L000099](../generate_index.py#L99) | 99 | `"JS_FUNCTION_ASSIGNMENT_RE = re.compile("` | — |
| [SRC-E599346ABE-L000100](../generate_index.py#L100) | 100 | `"    rf\"\\b(?:const\|let\|var)\\s+({JS_IDENTIFIER})\\s*=\\s*(?:async\\s*)?function\\b\""` | — |
| [SRC-E599346ABE-L000101](../generate_index.py#L101) | 101 | `")"` | — |
| [SRC-E599346ABE-L000102](../generate_index.py#L102) | 102 | `"JS_VARIABLE_RE = re.compile(rf\"\\b(?:const\|let\|var)\\s+({JS_IDENTIFIER})\\b\")"` | — |
| [SRC-E599346ABE-L000103](../generate_index.py#L103) | 103 | `"HTML_ATTRIBUTE_RE = re.compile("` | — |
| [SRC-E599346ABE-L000104](../generate_index.py#L104) | 104 | `"    r\"\"\"\\b(id\|name\|data-testid)\\s*=\\s*([\"'])(.*?)\\2\"\"\","` | — |
| [SRC-E599346ABE-L000105](../generate_index.py#L105) | 105 | `"    flags=re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-E599346ABE-L000106](../generate_index.py#L106) | 106 | `")"` | — |
| [SRC-E599346ABE-L000107](../generate_index.py#L107) | 107 | `"HTML_SCRIPT_RE = re.compile(r\"<script\\b[^>]*>(.*?)</script\\s*>\", re.IGNORECASE \| re.DOTALL)"` | — |
| [SRC-E599346ABE-L000108](../generate_index.py#L108) | 108 | `"HTML_STYLE_RE = re.compile(r\"<style\\b[^>]*>(.*?)</style\\s*>\", re.IGNORECASE \| re.DOTALL)"` | — |
| [SRC-E599346ABE-L000109](../generate_index.py#L109) | 109 | `"CSS_COMMENT_RE = re.compile(r\"/\\*.*?\\*/\", re.DOTALL)"` | — |
| [SRC-E599346ABE-L000110](../generate_index.py#L110) | 110 | `"CSS_CUSTOM_PROPERTY_RE = re.compile(r\"--([A-Za-z_][A-Za-z0-9_-]*)\\s*:\")"` | — |
| [SRC-E599346ABE-L000111](../generate_index.py#L111) | 111 | `"CSS_CLASS_RE = re.compile(r\"(?<![\\w.-])\\.([A-Za-z_][A-Za-z0-9_-]*)\")"` | — |
| [SRC-E599346ABE-L000112](../generate_index.py#L112) | 112 | `"CSS_ID_RE = re.compile(r\"(?<![\\w.#])#([A-Za-z_][A-Za-z0-9_-]*)\")"` | — |
| [SRC-E599346ABE-L000113](../generate_index.py#L113) | 113 | `"SHELL_FUNCTION_RE = re.compile("` | — |
| [SRC-E599346ABE-L000114](../generate_index.py#L114) | 114 | `"    r\"^\\s*(?:function\\s+)?([A-Za-z_][A-Za-z0-9_]*)\\s*\\(\\s*\\)\\s*\\{?\","` | — |
| [SRC-E599346ABE-L000115](../generate_index.py#L115) | 115 | `"    re.MULTILINE,"` | — |
| [SRC-E599346ABE-L000116](../generate_index.py#L116) | 116 | `")"` | — |
| [SRC-E599346ABE-L000117](../generate_index.py#L117) | 117 | `"MARKDOWN_HEADING_RE = re.compile(r\"^\\s{0,3}(#{1,6})\\s+(.+?)\\s*#*\\s*$\", re.MULTILINE)"` | — |
| [SRC-E599346ABE-L000118](../generate_index.py#L118) | 118 | `"YAML_KEY_RE = re.compile(r\"^\\s*([A-Za-z_][A-Za-z0-9_.-]*)\\s*:\", re.MULTILINE)"` | — |
| [SRC-E599346ABE-L000119](../generate_index.py#L119) | 119 | `"TOML_KEY_RE = re.compile(r\"^\\s*([A-Za-z0-9_.-]+)\\s*=\", re.MULTILINE)"` | — |
| [SRC-E599346ABE-L000120](../generate_index.py#L120) | 120 | `"TOML_SECTION_RE = re.compile(r\"^\\s*\\[([^\\]]+)\\]\\s*$\", re.MULTILINE)"` | — |
| [SRC-E599346ABE-L000121](../generate_index.py#L121) | 121 | `"JSON_KEY_RE = re.compile(r'\"([^\"]+)\"\\s*:')"` | — |
| [SRC-E599346ABE-L000122](../generate_index.py#L122) | 122 | `"INI_SECTION_RE = re.compile(r\"^\\s*\\[([^\\]]+)\\]\\s*$\", re.MULTILINE)"` | — |
| [SRC-E599346ABE-L000123](../generate_index.py#L123) | 123 | `"INI_KEY_RE = re.compile(r\"^\\s*([A-Za-z0-9_.-]+)\\s*=\", re.MULTILINE)"` | — |
| [SRC-E599346ABE-L000124](../generate_index.py#L124) | 124 | `"UPPER_SNAKE_RE = re.compile(r\"\\b[A-Z][A-Z0-9]*(?:_[A-Z0-9]+)+\\b\")"` | — |
| [SRC-E599346ABE-L000125](../generate_index.py#L125) | 125 | `"API_PATH_RE = re.compile(r\"\"\"[\"'](/(?:api\|leads)(?:/[A-Za-z0-9_{}./-]+)*)[\"']\"\"\")"` | — |
| [SRC-E599346ABE-L000126](../generate_index.py#L126) | 126 | `"FINDING_MARKER_NAMES = ("` | — |
| [SRC-E599346ABE-L000127](../generate_index.py#L127) | 127 | `"    \"TODO\","` | — |
| [SRC-E599346ABE-L000128](../generate_index.py#L128) | 128 | `"    \"FIXME\","` | — |
| [SRC-E599346ABE-L000129](../generate_index.py#L129) | 129 | `"    \"BUG\","` | — |
| [SRC-E599346ABE-L000130](../generate_index.py#L130) | 130 | `"    \"HACK\","` | — |
| [SRC-E599346ABE-L000131](../generate_index.py#L131) | 131 | `"    \"XXX\","` | — |
| [SRC-E599346ABE-L000132](../generate_index.py#L132) | 132 | `"    \"REVIEW\","` | — |
| [SRC-E599346ABE-L000133](../generate_index.py#L133) | 133 | `"    \"SECURITY\","` | — |
| [SRC-E599346ABE-L000134](../generate_index.py#L134) | 134 | `"    \"DEPRECATED\","` | — |
| [SRC-E599346ABE-L000135](../generate_index.py#L135) | 135 | `"    \"ISSUE\","` | — |
| [SRC-E599346ABE-L000136](../generate_index.py#L136) | 136 | `"    \"DEFECT\","` | — |
| [SRC-E599346ABE-L000137](../generate_index.py#L137) | 137 | `"    \"REGRESSION\","` | — |
| [SRC-E599346ABE-L000138](../generate_index.py#L138) | 138 | `"    \"RISK\","` | — |
| [SRC-E599346ABE-L000139](../generate_index.py#L139) | 139 | `"    \"GAP\","` | — |
| [SRC-E599346ABE-L000140](../generate_index.py#L140) | 140 | `"    \"ERROR\","` | — |
| [SRC-E599346ABE-L000141](../generate_index.py#L141) | 141 | `"    \"WARNING\","` | — |
| [SRC-E599346ABE-L000142](../generate_index.py#L142) | 142 | `"    \"PERF\","` | — |
| [SRC-E599346ABE-L000143](../generate_index.py#L143) | 143 | `"    \"PRIVACY\","` | — |
| [SRC-E599346ABE-L000144](../generate_index.py#L144) | 144 | `"    \"DATA_LOSS\","` | — |
| [SRC-E599346ABE-L000145](../generate_index.py#L145) | 145 | `"    \"ACCESSIBILITY\","` | — |
| [SRC-E599346ABE-L000146](../generate_index.py#L146) | 146 | `")"` | — |
| [SRC-E599346ABE-L000147](../generate_index.py#L147) | 147 | `"_FINDING_MARKER_ALTERNATION = \"\|\".join("` | — |
| [SRC-E599346ABE-L000148](../generate_index.py#L148) | 148 | `"    sorted(FINDING_MARKER_NAMES, key=len, reverse=True)"` | — |
| [SRC-E599346ABE-L000149](../generate_index.py#L149) | 149 | `")"` | — |
| [SRC-E599346ABE-L000150](../generate_index.py#L150) | 150 | `"FINDING_MARKER_RE = re.compile("` | — |
| [SRC-E599346ABE-L000151](../generate_index.py#L151) | 151 | `"    rf\"(?:^\|[;\|]\\s*)\\s*({_FINDING_MARKER_ALTERNATION})\\s*:\\s*(.*?)\""` | — |
| [SRC-E599346ABE-L000152](../generate_index.py#L152) | 152 | `"    rf\"(?=(?:[;\|]\\s*)(?:{_FINDING_MARKER_ALTERNATION})\\s*:\|$)\""` | — |
| [SRC-E599346ABE-L000153](../generate_index.py#L153) | 153 | `")"` | — |
| [SRC-E599346ABE-L000154](../generate_index.py#L154) | 154 | `""` | — |
| [SRC-E599346ABE-L000155](../generate_index.py#L155) | 155 | `""` | — |
| [SRC-E599346ABE-L000156](../generate_index.py#L156) | 156 | `"@dataclass(frozen=True, slots=True)"` | — |
| [SRC-E599346ABE-L000157](../generate_index.py#L157) | 157 | `"class IndexedSymbol:"` | — |
| [SRC-E599346ABE-L000158](../generate_index.py#L158) | 158 | `"    \"\"\"Represent a Python definition or module/class assignment.\"\"\""` | — |
| [SRC-E599346ABE-L000159](../generate_index.py#L159) | 159 | `""` | — |
| [SRC-E599346ABE-L000160](../generate_index.py#L160) | 160 | `"    file: str"` | — |
| [SRC-E599346ABE-L000161](../generate_index.py#L161) | 161 | `"    name: str"` | — |
| [SRC-E599346ABE-L000162](../generate_index.py#L162) | 162 | `"    kind: str"` | — |
| [SRC-E599346ABE-L000163](../generate_index.py#L163) | 163 | `"    line: int"` | — |
| [SRC-E599346ABE-L000164](../generate_index.py#L164) | 164 | `"    description: str"` | — |
| [SRC-E599346ABE-L000165](../generate_index.py#L165) | 165 | `"    documented: bool \| None"` | — |
| [SRC-E599346ABE-L000166](../generate_index.py#L166) | 166 | `""` | — |
| [SRC-E599346ABE-L000167](../generate_index.py#L167) | 167 | `""` | — |
| [SRC-E599346ABE-L000168](../generate_index.py#L168) | 168 | `"@dataclass(frozen=True, slots=True)"` | — |
| [SRC-E599346ABE-L000169](../generate_index.py#L169) | 169 | `"class IndexedFile:"` | — |
| [SRC-E599346ABE-L000170](../generate_index.py#L170) | 170 | `"    \"\"\"Represent a repository file with stable identifiers and navigation metadata.\"\"\""` | — |
| [SRC-E599346ABE-L000171](../generate_index.py#L171) | 171 | `""` | — |
| [SRC-E599346ABE-L000172](../generate_index.py#L172) | 172 | `"    file: str"` | — |
| [SRC-E599346ABE-L000173](../generate_index.py#L173) | 173 | `"    file_type: str"` | — |
| [SRC-E599346ABE-L000174](../generate_index.py#L174) | 174 | `"    size_bytes: int"` | — |
| [SRC-E599346ABE-L000175](../generate_index.py#L175) | 175 | `"    line_count: int \| None"` | — |
| [SRC-E599346ABE-L000176](../generate_index.py#L176) | 176 | `"    indexing_scope: str"` | — |
| [SRC-E599346ABE-L000177](../generate_index.py#L177) | 177 | `"    file_id: str"` | — |
| [SRC-E599346ABE-L000178](../generate_index.py#L178) | 178 | `"    category: str"` | — |
| [SRC-E599346ABE-L000179](../generate_index.py#L179) | 179 | `""` | — |
| [SRC-E599346ABE-L000180](../generate_index.py#L180) | 180 | `""` | — |
| [SRC-E599346ABE-L000181](../generate_index.py#L181) | 181 | `"@dataclass(frozen=True, slots=True)"` | — |
| [SRC-E599346ABE-L000182](../generate_index.py#L182) | 182 | `"class IndexedMarker:"` | — |
| [SRC-E599346ABE-L000183](../generate_index.py#L183) | 183 | `"    \"\"\"Represent a statically discovered symbol outside the Python AST index.\"\"\""` | — |
| [SRC-E599346ABE-L000184](../generate_index.py#L184) | 184 | `""` | — |
| [SRC-E599346ABE-L000185](../generate_index.py#L185) | 185 | `"    file: str"` | — |
| [SRC-E599346ABE-L000186](../generate_index.py#L186) | 186 | `"    name: str"` | — |
| [SRC-E599346ABE-L000187](../generate_index.py#L187) | 187 | `"    kind: str"` | — |
| [SRC-E599346ABE-L000188](../generate_index.py#L188) | 188 | `"    line: int"` | — |
| [SRC-E599346ABE-L000189](../generate_index.py#L189) | 189 | `""` | — |
| [SRC-E599346ABE-L000190](../generate_index.py#L190) | 190 | `""` | — |
| [SRC-E599346ABE-L000191](../generate_index.py#L191) | 191 | `"@dataclass(frozen=True, slots=True)"` | — |
| [SRC-E599346ABE-L000192](../generate_index.py#L192) | 192 | `"class IndexedLine:"` | — |
| [SRC-E599346ABE-L000193](../generate_index.py#L193) | 193 | `"    \"\"\"Represent one exact logical line from an eligible readable repository text file.\"\"\""` | — |
| [SRC-E599346ABE-L000194](../generate_index.py#L194) | 194 | `""` | — |
| [SRC-E599346ABE-L000195](../generate_index.py#L195) | 195 | `"    file: str"` | — |
| [SRC-E599346ABE-L000196](../generate_index.py#L196) | 196 | `"    file_id: str"` | — |
| [SRC-E599346ABE-L000197](../generate_index.py#L197) | 197 | `"    line_id: str"` | — |
| [SRC-E599346ABE-L000198](../generate_index.py#L198) | 198 | `"    category: str"` | — |
| [SRC-E599346ABE-L000199](../generate_index.py#L199) | 199 | `"    line: int"` | — |
| [SRC-E599346ABE-L000200](../generate_index.py#L200) | 200 | `"    content: str"` | — |
| [SRC-E599346ABE-L000201](../generate_index.py#L201) | 201 | `""` | — |
| [SRC-E599346ABE-L000202](../generate_index.py#L202) | 202 | `""` | — |
| [SRC-E599346ABE-L000203](../generate_index.py#L203) | 203 | `"@dataclass(frozen=True, slots=True)"` | — |
| [SRC-E599346ABE-L000204](../generate_index.py#L204) | 204 | `"class IndexedFinding:"` | — |
| [SRC-E599346ABE-L000205](../generate_index.py#L205) | 205 | `"    \"\"\"Represent a source annotation that explicitly requests attention.\"\"\""` | — |
| [SRC-E599346ABE-L000206](../generate_index.py#L206) | 206 | `""` | — |
| [SRC-E599346ABE-L000207](../generate_index.py#L207) | 207 | `"    finding_id: str"` | — |
| [SRC-E599346ABE-L000208](../generate_index.py#L208) | 208 | `"    file: str"` | — |
| [SRC-E599346ABE-L000209](../generate_index.py#L209) | 209 | `"    line_id: str"` | — |
| [SRC-E599346ABE-L000210](../generate_index.py#L210) | 210 | `"    marker: str"` | — |
| [SRC-E599346ABE-L000211](../generate_index.py#L211) | 211 | `"    description: str"` | — |
| [SRC-E599346ABE-L000212](../generate_index.py#L212) | 212 | `""` | — |
| [SRC-E599346ABE-L000213](../generate_index.py#L213) | 213 | `""` | — |
| [SRC-E599346ABE-L000214](../generate_index.py#L214) | 214 | `"class IndexGenerationError(RuntimeError):"` | — |
| [SRC-E599346ABE-L000215](../generate_index.py#L215) | 215 | `"    \"\"\"Signal that a complete Python AST index could not be generated.\"\"\""` | — |
| [SRC-E599346ABE-L000216](../generate_index.py#L216) | 216 | `""` | — |
| [SRC-E599346ABE-L000217](../generate_index.py#L217) | 217 | `""` | — |
| [SRC-E599346ABE-L000218](../generate_index.py#L218) | 218 | `"class SymbolVisitor(ast.NodeVisitor):"` | — |
| [SRC-E599346ABE-L000219](../generate_index.py#L219) | 219 | `"    \"\"\"Collect Python classes, functions, methods and module/class assignments.\"\"\""` | — |
| [SRC-E599346ABE-L000220](../generate_index.py#L220) | 220 | `""` | — |
| [SRC-E599346ABE-L000221](../generate_index.py#L221) | 221 | `"    def __init__(self, relative_file: str) -> None:"` | — |
| [SRC-E599346ABE-L000222](../generate_index.py#L222) | 222 | `"        \"\"\"Initialize the visitor for one repository-relative Python file.\"\"\""` | — |
| [SRC-E599346ABE-L000223](../generate_index.py#L223) | 223 | `"        self.relative_file = relative_file"` | — |
| [SRC-E599346ABE-L000224](../generate_index.py#L224) | 224 | `"        self.symbols: list[IndexedSymbol] = []"` | — |
| [SRC-E599346ABE-L000225](../generate_index.py#L225) | 225 | `"        self.scope: list[str] = []"` | — |
| [SRC-E599346ABE-L000226](../generate_index.py#L226) | 226 | `"        self.function_depth = 0"` | — |
| [SRC-E599346ABE-L000227](../generate_index.py#L227) | 227 | `""` | — |
| [SRC-E599346ABE-L000228](../generate_index.py#L228) | 228 | `"    @staticmethod"` | — |
| [SRC-E599346ABE-L000229](../generate_index.py#L229) | 229 | `"    def _description(node: ast.AST) -> tuple[str, bool]:"` | — |
| [SRC-E599346ABE-L000230](../generate_index.py#L230) | 230 | `"        \"\"\"Return a compact first-paragraph summary and its documentation state.\"\"\""` | — |
| [SRC-E599346ABE-L000231](../generate_index.py#L231) | 231 | `"        docstring = ast.get_docstring(node, clean=True)"` | — |
| [SRC-E599346ABE-L000232](../generate_index.py#L232) | 232 | `"        if not docstring or not docstring.strip():"` | — |
| [SRC-E599346ABE-L000233](../generate_index.py#L233) | 233 | `"            return \"لا توجد Docstring.\", False"` | — |
| [SRC-E599346ABE-L000234](../generate_index.py#L234) | 234 | `""` | — |
| [SRC-E599346ABE-L000235](../generate_index.py#L235) | 235 | `"        first_paragraph = docstring.strip().split(\"\\n\\n\", maxsplit=1)[0]"` | — |
| [SRC-E599346ABE-L000236](../generate_index.py#L236) | 236 | `"        summary = \" \".join(first_paragraph.split())"` | — |
| [SRC-E599346ABE-L000237](../generate_index.py#L237) | 237 | `"        if len(summary) > MAX_DESCRIPTION_LENGTH:"` | — |
| [SRC-E599346ABE-L000238](../generate_index.py#L238) | 238 | `"            summary = summary[: MAX_DESCRIPTION_LENGTH - 3].rstrip() + \"...\""` | — |
| [SRC-E599346ABE-L000239](../generate_index.py#L239) | 239 | `"        return summary, True"` | — |
| [SRC-E599346ABE-L000240](../generate_index.py#L240) | 240 | `""` | — |
| [SRC-E599346ABE-L000241](../generate_index.py#L241) | 241 | `"    def _record_definition("` | — |
| [SRC-E599346ABE-L000242](../generate_index.py#L242) | 242 | `"        self,"` | — |
| [SRC-E599346ABE-L000243](../generate_index.py#L243) | 243 | `"        node: ast.ClassDef \| ast.FunctionDef \| ast.AsyncFunctionDef,"` | — |
| [SRC-E599346ABE-L000244](../generate_index.py#L244) | 244 | `"        kind: str,"` | — |
| [SRC-E599346ABE-L000245](../generate_index.py#L245) | 245 | `"    ) -> None:"` | — |
| [SRC-E599346ABE-L000246](../generate_index.py#L246) | 246 | `"        \"\"\"Record one class/function definition while preserving its qualified scope.\"\"\""` | — |
| [SRC-E599346ABE-L000247](../generate_index.py#L247) | 247 | `"        description, documented = self._description(node)"` | — |
| [SRC-E599346ABE-L000248](../generate_index.py#L248) | 248 | `"        qualified_name = \".\".join((*self.scope, node.name))"` | — |
| [SRC-E599346ABE-L000249](../generate_index.py#L249) | 249 | `"        self.symbols.append("` | — |
| [SRC-E599346ABE-L000250](../generate_index.py#L250) | 250 | `"            IndexedSymbol("` | — |
| [SRC-E599346ABE-L000251](../generate_index.py#L251) | 251 | `"                file=self.relative_file,"` | — |
| [SRC-E599346ABE-L000252](../generate_index.py#L252) | 252 | `"                name=qualified_name,"` | — |
| [SRC-E599346ABE-L000253](../generate_index.py#L253) | 253 | `"                kind=kind,"` | — |
| [SRC-E599346ABE-L000254](../generate_index.py#L254) | 254 | `"                line=node.lineno,"` | — |
| [SRC-E599346ABE-L000255](../generate_index.py#L255) | 255 | `"                description=description,"` | — |
| [SRC-E599346ABE-L000256](../generate_index.py#L256) | 256 | `"                documented=documented,"` | — |
| [SRC-E599346ABE-L000257](../generate_index.py#L257) | 257 | `"            )"` | — |
| [SRC-E599346ABE-L000258](../generate_index.py#L258) | 258 | `"        )"` | — |
| [SRC-E599346ABE-L000259](../generate_index.py#L259) | 259 | `""` | — |
| [SRC-E599346ABE-L000260](../generate_index.py#L260) | 260 | `"    def _record_assignment_target(self, node: ast.AST, line: int) -> None:"` | — |
| [SRC-E599346ABE-L000261](../generate_index.py#L261) | 261 | `"        \"\"\"Record declared names from a module-level or class-level assignment.\"\"\""` | — |
| [SRC-E599346ABE-L000262](../generate_index.py#L262) | 262 | `"        if isinstance(node, ast.Name):"` | — |
| [SRC-E599346ABE-L000263](../generate_index.py#L263) | 263 | `"            qualified_name = \".\".join((*self.scope, node.id))"` | — |
| [SRC-E599346ABE-L000264](../generate_index.py#L264) | 264 | `"            self.symbols.append("` | — |
| [SRC-E599346ABE-L000265](../generate_index.py#L265) | 265 | `"                IndexedSymbol("` | — |
| [SRC-E599346ABE-L000266](../generate_index.py#L266) | 266 | `"                    file=self.relative_file,"` | — |
| [SRC-E599346ABE-L000267](../generate_index.py#L267) | 267 | `"                    name=qualified_name,"` | — |
| [SRC-E599346ABE-L000268](../generate_index.py#L268) | 268 | `"                    kind=\"متغير/ثابت Python\","` | — |
| [SRC-E599346ABE-L000269](../generate_index.py#L269) | 269 | `"                    line=line,"` | — |
| [SRC-E599346ABE-L000270](../generate_index.py#L270) | 270 | `"                    description=\"تعريف على مستوى الوحدة أو الكلاس.\","` | — |
| [SRC-E599346ABE-L000271](../generate_index.py#L271) | 271 | `"                    documented=None,"` | — |
| [SRC-E599346ABE-L000272](../generate_index.py#L272) | 272 | `"                )"` | — |
| [SRC-E599346ABE-L000273](../generate_index.py#L273) | 273 | `"            )"` | — |
| [SRC-E599346ABE-L000274](../generate_index.py#L274) | 274 | `"        elif isinstance(node, (ast.Tuple, ast.List)):"` | — |
| [SRC-E599346ABE-L000275](../generate_index.py#L275) | 275 | `"            for element in node.elts:"` | — |
| [SRC-E599346ABE-L000276](../generate_index.py#L276) | 276 | `"                self._record_assignment_target(element, line)"` | — |
| [SRC-E599346ABE-L000277](../generate_index.py#L277) | 277 | `""` | — |
| [SRC-E599346ABE-L000278](../generate_index.py#L278) | 278 | `"    def visit_Assign(self, node: ast.Assign) -> None:"` | — |
| [SRC-E599346ABE-L000279](../generate_index.py#L279) | 279 | `"        \"\"\"Index module/class assignment names but avoid flooding the index with locals.\"\"\""` | — |
| [SRC-E599346ABE-L000280](../generate_index.py#L280) | 280 | `"        if self.function_depth == 0:"` | — |
| [SRC-E599346ABE-L000281](../generate_index.py#L281) | 281 | `"            for target in node.targets:"` | — |
| [SRC-E599346ABE-L000282](../generate_index.py#L282) | 282 | `"                self._record_assignment_target(target, node.lineno)"` | — |
| [SRC-E599346ABE-L000283](../generate_index.py#L283) | 283 | `"        self.generic_visit(node)"` | — |
| [SRC-E599346ABE-L000284](../generate_index.py#L284) | 284 | `""` | — |
| [SRC-E599346ABE-L000285](../generate_index.py#L285) | 285 | `"    def visit_AnnAssign(self, node: ast.AnnAssign) -> None:"` | — |
| [SRC-E599346ABE-L000286](../generate_index.py#L286) | 286 | `"        \"\"\"Index annotated module/class assignments without counting local variables.\"\"\""` | — |
| [SRC-E599346ABE-L000287](../generate_index.py#L287) | 287 | `"        if self.function_depth == 0:"` | — |
| [SRC-E599346ABE-L000288](../generate_index.py#L288) | 288 | `"            self._record_assignment_target(node.target, node.lineno)"` | — |
| [SRC-E599346ABE-L000289](../generate_index.py#L289) | 289 | `"        self.generic_visit(node)"` | — |
| [SRC-E599346ABE-L000290](../generate_index.py#L290) | 290 | `""` | — |
| [SRC-E599346ABE-L000291](../generate_index.py#L291) | 291 | `"    def visit_ClassDef(self, node: ast.ClassDef) -> None:"` | — |
| [SRC-E599346ABE-L000292](../generate_index.py#L292) | 292 | `"        \"\"\"Record a class and recursively inspect its body.\"\"\""` | — |
| [SRC-E599346ABE-L000293](../generate_index.py#L293) | 293 | `"        self._record_definition(node, \"كلاس\")"` | — |
| [SRC-E599346ABE-L000294](../generate_index.py#L294) | 294 | `"        self.scope.append(node.name)"` | — |
| [SRC-E599346ABE-L000295](../generate_index.py#L295) | 295 | `"        try:"` | — |
| [SRC-E599346ABE-L000296](../generate_index.py#L296) | 296 | `"            self.generic_visit(node)"` | — |
| [SRC-E599346ABE-L000297](../generate_index.py#L297) | 297 | `"        finally:"` | — |
| [SRC-E599346ABE-L000298](../generate_index.py#L298) | 298 | `"            self.scope.pop()"` | — |
| [SRC-E599346ABE-L000299](../generate_index.py#L299) | 299 | `""` | — |
| [SRC-E599346ABE-L000300](../generate_index.py#L300) | 300 | `"    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:"` | — |
| [SRC-E599346ABE-L000301](../generate_index.py#L301) | 301 | `"        \"\"\"Record a synchronous function or method and nested definitions.\"\"\""` | — |
| [SRC-E599346ABE-L000302](../generate_index.py#L302) | 302 | `"        self._record_definition(node, \"دالة\")"` | — |
| [SRC-E599346ABE-L000303](../generate_index.py#L303) | 303 | `"        self.scope.append(node.name)"` | — |
| [SRC-E599346ABE-L000304](../generate_index.py#L304) | 304 | `"        self.function_depth += 1"` | — |
| [SRC-E599346ABE-L000305](../generate_index.py#L305) | 305 | `"        try:"` | — |
| [SRC-E599346ABE-L000306](../generate_index.py#L306) | 306 | `"            self.generic_visit(node)"` | — |
| [SRC-E599346ABE-L000307](../generate_index.py#L307) | 307 | `"        finally:"` | — |
| [SRC-E599346ABE-L000308](../generate_index.py#L308) | 308 | `"            self.function_depth -= 1"` | — |
| [SRC-E599346ABE-L000309](../generate_index.py#L309) | 309 | `"            self.scope.pop()"` | — |
| [SRC-E599346ABE-L000310](../generate_index.py#L310) | 310 | `""` | — |
| [SRC-E599346ABE-L000311](../generate_index.py#L311) | 311 | `"    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:"` | — |
| [SRC-E599346ABE-L000312](../generate_index.py#L312) | 312 | `"        \"\"\"Record an asynchronous function or method and nested definitions.\"\"\""` | — |
| [SRC-E599346ABE-L000313](../generate_index.py#L313) | 313 | `"        self._record_definition(node, \"دالة غير متزامنة\")"` | — |
| [SRC-E599346ABE-L000314](../generate_index.py#L314) | 314 | `"        self.scope.append(node.name)"` | — |
| [SRC-E599346ABE-L000315](../generate_index.py#L315) | 315 | `"        self.function_depth += 1"` | — |
| [SRC-E599346ABE-L000316](../generate_index.py#L316) | 316 | `"        try:"` | — |
| [SRC-E599346ABE-L000317](../generate_index.py#L317) | 317 | `"            self.generic_visit(node)"` | — |
| [SRC-E599346ABE-L000318](../generate_index.py#L318) | 318 | `"        finally:"` | — |
| [SRC-E599346ABE-L000319](../generate_index.py#L319) | 319 | `"            self.function_depth -= 1"` | — |
| [SRC-E599346ABE-L000320](../generate_index.py#L320) | 320 | `"            self.scope.pop()"` | — |
| [SRC-E599346ABE-L000321](../generate_index.py#L321) | 321 | `""` | — |
| [SRC-E599346ABE-L000322](../generate_index.py#L322) | 322 | `""` | — |
| [SRC-E599346ABE-L000323](../generate_index.py#L323) | 323 | `"def _is_sensitive_or_runtime_path(path: Path) -> bool:"` | — |
| [SRC-E599346ABE-L000324](../generate_index.py#L324) | 324 | `"    \"\"\"Exclude known local secrets, runtime databases, keys and generated bytecode.\"\"\""` | — |
| [SRC-E599346ABE-L000325](../generate_index.py#L325) | 325 | `"    name = path.name.lower()"` | — |
| [SRC-E599346ABE-L000326](../generate_index.py#L326) | 326 | `"    if name in SENSITIVE_FILENAMES:"` | — |
| [SRC-E599346ABE-L000327](../generate_index.py#L327) | 327 | `"        return True"` | — |
| [SRC-E599346ABE-L000328](../generate_index.py#L328) | 328 | `"    if name.startswith(\".env\") and name != \".env.example\":"` | — |
| [SRC-E599346ABE-L000329](../generate_index.py#L329) | 329 | `"        return True"` | — |
| [SRC-E599346ABE-L000330](../generate_index.py#L330) | 330 | `"    return path.suffix.lower() in EXCLUDED_SUFFIXES"` | — |
| [SRC-E599346ABE-L000331](../generate_index.py#L331) | 331 | `""` | — |
| [SRC-E599346ABE-L000332](../generate_index.py#L332) | 332 | `""` | — |
| [SRC-E599346ABE-L000333](../generate_index.py#L333) | 333 | `"def _stable_file_id(relative_file: str) -> str:"` | — |
| [SRC-E599346ABE-L000334](../generate_index.py#L334) | 334 | `"    \"\"\"Return a deterministic path-derived identifier without hashing file contents.\"\"\""` | — |
| [SRC-E599346ABE-L000335](../generate_index.py#L335) | 335 | `"    digest = hashlib.sha256(relative_file.encode(\"utf-8\")).hexdigest()[:10].upper()"` | — |
| [SRC-E599346ABE-L000336](../generate_index.py#L336) | 336 | `"    return f\"FILE-{digest}\""` | — |
| [SRC-E599346ABE-L000337](../generate_index.py#L337) | 337 | `""` | — |
| [SRC-E599346ABE-L000338](../generate_index.py#L338) | 338 | `""` | — |
| [SRC-E599346ABE-L000339](../generate_index.py#L339) | 339 | `"def _category_for_path(relative_file: str) -> str:"` | — |
| [SRC-E599346ABE-L000340](../generate_index.py#L340) | 340 | `"    \"\"\"Assign an understandable navigation category from the repository-relative path.\"\"\""` | — |
| [SRC-E599346ABE-L000341](../generate_index.py#L341) | 341 | `"    normalized = relative_file.replace(\"\\\\\", \"/\")"` | — |
| [SRC-E599346ABE-L000342](../generate_index.py#L342) | 342 | `"    name = Path(normalized).name.lower()"` | — |
| [SRC-E599346ABE-L000343](../generate_index.py#L343) | 343 | `"    suffix = Path(normalized).suffix.lower()"` | — |
| [SRC-E599346ABE-L000344](../generate_index.py#L344) | 344 | `"    if normalized.startswith(\"tests/\") or \"/tests/\" in normalized:"` | — |
| [SRC-E599346ABE-L000345](../generate_index.py#L345) | 345 | `"        return \"اختبارات\""` | — |
| [SRC-E599346ABE-L000346](../generate_index.py#L346) | 346 | `"    if normalized.startswith(\".github/workflows/\"):"` | — |
| [SRC-E599346ABE-L000347](../generate_index.py#L347) | 347 | `"        return \"CI وأتمتة\""` | — |
| [SRC-E599346ABE-L000348](../generate_index.py#L348) | 348 | `"    if normalized.startswith(\"agents/\"):"` | — |
| [SRC-E599346ABE-L000349](../generate_index.py#L349) | 349 | `"        return \"الوكيل والمنطق\""` | — |
| [SRC-E599346ABE-L000350](../generate_index.py#L350) | 350 | `"    if normalized.startswith(\"api/\"):"` | — |
| [SRC-E599346ABE-L000351](../generate_index.py#L351) | 351 | `"        return \"واجهات API\""` | — |
| [SRC-E599346ABE-L000352](../generate_index.py#L352) | 352 | `"    if normalized.startswith(\"cli/\"):"` | — |
| [SRC-E599346ABE-L000353](../generate_index.py#L353) | 353 | `"        return \"واجهة سطر الأوامر\""` | — |
| [SRC-E599346ABE-L000354](../generate_index.py#L354) | 354 | `"    if normalized.startswith(\"docs/\"):"` | — |
| [SRC-E599346ABE-L000355](../generate_index.py#L355) | 355 | `"        return \"وثائق وفهرسة\""` | — |
| [SRC-E599346ABE-L000356](../generate_index.py#L356) | 356 | `"    if normalized.startswith((\"web/\", \"static/\", \"templates/\")) or suffix in {"` | — |
| [SRC-E599346ABE-L000357](../generate_index.py#L357) | 357 | `"        \".html\", \".htm\", \".css\", \".scss\", \".js\", \".mjs\", \".cjs\", \".jsx\", \".ts\", \".tsx\","` | — |
| [SRC-E599346ABE-L000358](../generate_index.py#L358) | 358 | `"        \".vue\", \".svelte\","` | — |
| [SRC-E599346ABE-L000359](../generate_index.py#L359) | 359 | `"    }:"` | — |
| [SRC-E599346ABE-L000360](../generate_index.py#L360) | 360 | `"        return \"واجهة الويب\""` | — |
| [SRC-E599346ABE-L000361](../generate_index.py#L361) | 361 | `"    if name in {"` | — |
| [SRC-E599346ABE-L000362](../generate_index.py#L362) | 362 | `"        \"dockerfile\", \"makefile\", \"procfile\", \"pyproject.toml\","` | — |
| [SRC-E599346ABE-L000363](../generate_index.py#L363) | 363 | `"        \"requirements.txt\", \"requirements-dev.txt\", \".gitignore\","` | — |
| [SRC-E599346ABE-L000364](../generate_index.py#L364) | 364 | `"        \".dockerignore\", \".editorconfig\","` | — |
| [SRC-E599346ABE-L000365](../generate_index.py#L365) | 365 | `"    } or suffix in {\".yml\", \".yaml\", \".toml\", \".ini\", \".cfg\", \".json\", \".jsonl\", \".xml\"}:"` | — |
| [SRC-E599346ABE-L000366](../generate_index.py#L366) | 366 | `"        return \"إعدادات وتشغيل\""` | — |
| [SRC-E599346ABE-L000367](../generate_index.py#L367) | 367 | `"    if suffix in {\".md\", \".rst\", \".txt\"}:"` | — |
| [SRC-E599346ABE-L000368](../generate_index.py#L368) | 368 | `"        return \"وثائق ونصوص\""` | — |
| [SRC-E599346ABE-L000369](../generate_index.py#L369) | 369 | `"    return \"ملفات أخرى\""` | — |
| [SRC-E599346ABE-L000370](../generate_index.py#L370) | 370 | `""` | — |
| [SRC-E599346ABE-L000371](../generate_index.py#L371) | 371 | `""` | — |
| [SRC-E599346ABE-L000372](../generate_index.py#L372) | 372 | `"def discover_repository_files(root: Path) -> list[Path]:"` | — |
| [SRC-E599346ABE-L000373](../generate_index.py#L373) | 373 | `"    \"\"\"Return the stable file inventory, excluding the generated index and runtime data.\"\"\""` | — |
| [SRC-E599346ABE-L000374](../generate_index.py#L374) | 374 | `"    discovered: list[Path] = []"` | — |
| [SRC-E599346ABE-L000375](../generate_index.py#L375) | 375 | `"    for current_directory, directory_names, file_names in os.walk("` | — |
| [SRC-E599346ABE-L000376](../generate_index.py#L376) | 376 | `"        root,"` | — |
| [SRC-E599346ABE-L000377](../generate_index.py#L377) | 377 | `"        topdown=True,"` | — |
| [SRC-E599346ABE-L000378](../generate_index.py#L378) | 378 | `"        followlinks=False,"` | — |
| [SRC-E599346ABE-L000379](../generate_index.py#L379) | 379 | `"    ):"` | — |
| [SRC-E599346ABE-L000380](../generate_index.py#L380) | 380 | `"        directory_names[:] = sorted("` | — |
| [SRC-E599346ABE-L000381](../generate_index.py#L381) | 381 | `"            name"` | — |
| [SRC-E599346ABE-L000382](../generate_index.py#L382) | 382 | `"            for name in directory_names"` | — |
| [SRC-E599346ABE-L000383](../generate_index.py#L383) | 383 | `"            if name not in EXCLUDED_DIRECTORIES"` | — |
| [SRC-E599346ABE-L000384](../generate_index.py#L384) | 384 | `"            and not name.lower().endswith((\".egg-info\", \".dist-info\"))"` | — |
| [SRC-E599346ABE-L000385](../generate_index.py#L385) | 385 | `"            and not (Path(current_directory) / name).is_symlink()"` | — |
| [SRC-E599346ABE-L000386](../generate_index.py#L386) | 386 | `"        )"` | — |
| [SRC-E599346ABE-L000387](../generate_index.py#L387) | 387 | `"        for file_name in sorted(file_names):"` | — |
| [SRC-E599346ABE-L000388](../generate_index.py#L388) | 388 | `"            candidate = Path(current_directory) / file_name"` | — |
| [SRC-E599346ABE-L000389](../generate_index.py#L389) | 389 | `"            if candidate.is_symlink() or _is_sensitive_or_runtime_path(candidate):"` | — |
| [SRC-E599346ABE-L000390](../generate_index.py#L390) | 390 | `"                continue"` | — |
| [SRC-E599346ABE-L000391](../generate_index.py#L391) | 391 | `"            relative_file = candidate.relative_to(root).as_posix()"` | — |
| [SRC-E599346ABE-L000392](../generate_index.py#L392) | 392 | `"            if ("` | — |
| [SRC-E599346ABE-L000393](../generate_index.py#L393) | 393 | `"                relative_file in INDEX_OUTPUT_PATHS"` | — |
| [SRC-E599346ABE-L000394](../generate_index.py#L394) | 394 | `"                or relative_file.startswith(SOURCE_LINES_PAGES_DIR + \"/\")"` | — |
| [SRC-E599346ABE-L000395](../generate_index.py#L395) | 395 | `"            ):"` | — |
| [SRC-E599346ABE-L000396](../generate_index.py#L396) | 396 | `"                # Exclude generated index outputs to prevent self-indexing loops."` | — |
| [SRC-E599346ABE-L000397](../generate_index.py#L397) | 397 | `"                continue"` | — |
| [SRC-E599346ABE-L000398](../generate_index.py#L398) | 398 | `"            discovered.append(candidate)"` | — |
| [SRC-E599346ABE-L000399](../generate_index.py#L399) | 399 | `""` | — |
| [SRC-E599346ABE-L000400](../generate_index.py#L400) | 400 | `"    return sorted("` | — |
| [SRC-E599346ABE-L000401](../generate_index.py#L401) | 401 | `"        discovered,"` | — |
| [SRC-E599346ABE-L000402](../generate_index.py#L402) | 402 | `"        key=lambda path: path.relative_to(root).as_posix().casefold(),"` | — |
| [SRC-E599346ABE-L000403](../generate_index.py#L403) | 403 | `"    )"` | — |
| [SRC-E599346ABE-L000404](../generate_index.py#L404) | 404 | `""` | — |
| [SRC-E599346ABE-L000405](../generate_index.py#L405) | 405 | `""` | — |
| [SRC-E599346ABE-L000406](../generate_index.py#L406) | 406 | `"def _read_text_bounded(path: Path) -> str \| None:"` | — |
| [SRC-E599346ABE-L000407](../generate_index.py#L407) | 407 | `"    \"\"\"Read supported UTF-8 text files only when they are within the scan-size bound.\"\"\""` | — |
| [SRC-E599346ABE-L000408](../generate_index.py#L408) | 408 | `"    try:"` | — |
| [SRC-E599346ABE-L000409](../generate_index.py#L409) | 409 | `"        if path.stat().st_size > MAX_INDEXED_TEXT_BYTES:"` | — |
| [SRC-E599346ABE-L000410](../generate_index.py#L410) | 410 | `"            return None"` | — |
| [SRC-E599346ABE-L000411](../generate_index.py#L411) | 411 | `"        if path.suffix.lower() == \".py\":"` | — |
| [SRC-E599346ABE-L000412](../generate_index.py#L412) | 412 | `"            with tokenize.open(str(path)) as source_stream:"` | — |
| [SRC-E599346ABE-L000413](../generate_index.py#L413) | 413 | `"                text = source_stream.read()"` | — |
| [SRC-E599346ABE-L000414](../generate_index.py#L414) | 414 | `"        else:"` | — |
| [SRC-E599346ABE-L000415](../generate_index.py#L415) | 415 | `"            text = path.read_text(encoding=\"utf-8\")"` | — |
| [SRC-E599346ABE-L000416](../generate_index.py#L416) | 416 | `"        if \"\\x00\" in text:"` | — |
| [SRC-E599346ABE-L000417](../generate_index.py#L417) | 417 | `"            return None"` | — |
| [SRC-E599346ABE-L000418](../generate_index.py#L418) | 418 | `"        return text"` | — |
| [SRC-E599346ABE-L000419](../generate_index.py#L419) | 419 | `"    except (OSError, UnicodeError, LookupError, tokenize.TokenError):"` | — |
| [SRC-E599346ABE-L000420](../generate_index.py#L420) | 420 | `"        return None"` | — |
| [SRC-E599346ABE-L000421](../generate_index.py#L421) | 421 | `""` | — |
| [SRC-E599346ABE-L000422](../generate_index.py#L422) | 422 | `""` | — |
| [SRC-E599346ABE-L000423](../generate_index.py#L423) | 423 | `"def _count_lines(text: str) -> int:"` | — |
| [SRC-E599346ABE-L000424](../generate_index.py#L424) | 424 | `"    \"\"\"Count source lines without adding an extra line for a trailing newline.\"\"\""` | — |
| [SRC-E599346ABE-L000425](../generate_index.py#L425) | 425 | `"    if not text:"` | — |
| [SRC-E599346ABE-L000426](../generate_index.py#L426) | 426 | `"        return 0"` | — |
| [SRC-E599346ABE-L000427](../generate_index.py#L427) | 427 | `"    return text.count(\"\\n\") + (not text.endswith(\"\\n\"))"` | — |
| [SRC-E599346ABE-L000428](../generate_index.py#L428) | 428 | `""` | — |
| [SRC-E599346ABE-L000429](../generate_index.py#L429) | 429 | `""` | — |
| [SRC-E599346ABE-L000430](../generate_index.py#L430) | 430 | `"def _file_type(path: Path) -> str:"` | — |
| [SRC-E599346ABE-L000431](../generate_index.py#L431) | 431 | `"    \"\"\"Return a readable file type based on a known filename or extension.\"\"\""` | — |
| [SRC-E599346ABE-L000432](../generate_index.py#L432) | 432 | `"    name = path.name.lower()"` | — |
| [SRC-E599346ABE-L000433](../generate_index.py#L433) | 433 | `"    if name in {\"dockerfile\", \"makefile\", \"procfile\"}:"` | — |
| [SRC-E599346ABE-L000434](../generate_index.py#L434) | 434 | `"        return name.capitalize()"` | — |
| [SRC-E599346ABE-L000435](../generate_index.py#L435) | 435 | `"    suffix = path.suffix.lower()"` | — |
| [SRC-E599346ABE-L000436](../generate_index.py#L436) | 436 | `"    labels = {"` | — |
| [SRC-E599346ABE-L000437](../generate_index.py#L437) | 437 | `"        \".py\": \"Python\","` | — |
| [SRC-E599346ABE-L000438](../generate_index.py#L438) | 438 | `"        \".html\": \"HTML\","` | — |
| [SRC-E599346ABE-L000439](../generate_index.py#L439) | 439 | `"        \".htm\": \"HTML\","` | — |
| [SRC-E599346ABE-L000440](../generate_index.py#L440) | 440 | `"        \".js\": \"JavaScript\","` | — |
| [SRC-E599346ABE-L000441](../generate_index.py#L441) | 441 | `"        \".mjs\": \"JavaScript module\","` | — |
| [SRC-E599346ABE-L000442](../generate_index.py#L442) | 442 | `"        \".cjs\": \"CommonJS\","` | — |
| [SRC-E599346ABE-L000443](../generate_index.py#L443) | 443 | `"        \".jsx\": \"React JSX\","` | — |
| [SRC-E599346ABE-L000444](../generate_index.py#L444) | 444 | `"        \".ts\": \"TypeScript\","` | — |
| [SRC-E599346ABE-L000445](../generate_index.py#L445) | 445 | `"        \".tsx\": \"TypeScript JSX\","` | — |
| [SRC-E599346ABE-L000446](../generate_index.py#L446) | 446 | `"        \".css\": \"CSS\","` | — |
| [SRC-E599346ABE-L000447](../generate_index.py#L447) | 447 | `"        \".scss\": \"SCSS\","` | — |
| [SRC-E599346ABE-L000448](../generate_index.py#L448) | 448 | `"        \".md\": \"Markdown\","` | — |
| [SRC-E599346ABE-L000449](../generate_index.py#L449) | 449 | `"        \".yml\": \"YAML\","` | — |
| [SRC-E599346ABE-L000450](../generate_index.py#L450) | 450 | `"        \".yaml\": \"YAML\","` | — |
| [SRC-E599346ABE-L000451](../generate_index.py#L451) | 451 | `"        \".json\": \"JSON\","` | — |
| [SRC-E599346ABE-L000452](../generate_index.py#L452) | 452 | `"        \".toml\": \"TOML\","` | — |
| [SRC-E599346ABE-L000453](../generate_index.py#L453) | 453 | `"        \".sh\": \"Shell\","` | — |
| [SRC-E599346ABE-L000454](../generate_index.py#L454) | 454 | `"        \".sql\": \"SQL\","` | — |
| [SRC-E599346ABE-L000455](../generate_index.py#L455) | 455 | `"        \".txt\": \"Text\","` | — |
| [SRC-E599346ABE-L000456](../generate_index.py#L456) | 456 | `"        \".svg\": \"SVG\","` | — |
| [SRC-E599346ABE-L000457](../generate_index.py#L457) | 457 | `"        \".png\": \"PNG image\","` | — |
| [SRC-E599346ABE-L000458](../generate_index.py#L458) | 458 | `"        \".jpg\": \"JPEG image\","` | — |
| [SRC-E599346ABE-L000459](../generate_index.py#L459) | 459 | `"        \".jpeg\": \"JPEG image\","` | — |
| [SRC-E599346ABE-L000460](../generate_index.py#L460) | 460 | `"        \".webp\": \"WebP image\","` | — |
| [SRC-E599346ABE-L000461](../generate_index.py#L461) | 461 | `"    }"` | — |
| [SRC-E599346ABE-L000462](../generate_index.py#L462) | 462 | `"    return labels.get(suffix, suffix[1:].upper() if suffix else \"بدون امتداد\")"` | — |
| [SRC-E599346ABE-L000463](../generate_index.py#L463) | 463 | `""` | — |
| [SRC-E599346ABE-L000464](../generate_index.py#L464) | 464 | `""` | — |
| [SRC-E599346ABE-L000465](../generate_index.py#L465) | 465 | `"def _indexing_scope(path: Path, text: str \| None) -> str:"` | — |
| [SRC-E599346ABE-L000466](../generate_index.py#L466) | 466 | `"    \"\"\"Describe precisely whether a file receives symbol extraction or path inventory only.\"\"\""` | — |
| [SRC-E599346ABE-L000467](../generate_index.py#L467) | 467 | `"    if text is None:"` | — |
| [SRC-E599346ABE-L000468](../generate_index.py#L468) | 468 | `"        return \"جرد المسار والحجم فقط (ثنائي/غير مقروء/أكبر من حد الفحص)\""` | — |
| [SRC-E599346ABE-L000469](../generate_index.py#L469) | 469 | `"    suffix = path.suffix.lower()"` | — |
| [SRC-E599346ABE-L000470](../generate_index.py#L470) | 470 | `"    if suffix in PYTHON_EXTENSIONS:"` | — |
| [SRC-E599346ABE-L000471](../generate_index.py#L471) | 471 | `"        return \"جرد الملف + AST Python\""` | — |
| [SRC-E599346ABE-L000472](../generate_index.py#L472) | 472 | `"    if suffix in JAVASCRIPT_EXTENSIONS:"` | — |
| [SRC-E599346ABE-L000473](../generate_index.py#L473) | 473 | `"        return \"جرد الملف + رموز JavaScript/TypeScript ساكنة\""` | — |
| [SRC-E599346ABE-L000474](../generate_index.py#L474) | 474 | `"    if suffix in CSS_EXTENSIONS:"` | — |
| [SRC-E599346ABE-L000475](../generate_index.py#L475) | 475 | `"        return \"جرد الملف + محددات CSS والمتغيرات المخصصة\""` | — |
| [SRC-E599346ABE-L000476](../generate_index.py#L476) | 476 | `"    if suffix in {\".html\", \".htm\"}:"` | — |
| [SRC-E599346ABE-L000477](../generate_index.py#L477) | 477 | `"        return \"جرد الملف + معرفات HTML والرموز داخل script/style\""` | — |
| [SRC-E599346ABE-L000478](../generate_index.py#L478) | 478 | `"    if suffix == \".md\":"` | — |
| [SRC-E599346ABE-L000479](../generate_index.py#L479) | 479 | `"        return \"جرد الملف + عناوين Markdown\""` | — |
| [SRC-E599346ABE-L000480](../generate_index.py#L480) | 480 | `"    if suffix in CONFIG_EXTENSIONS:"` | — |
| [SRC-E599346ABE-L000481](../generate_index.py#L481) | 481 | `"        return \"جرد الملف + مفاتيح إعداد ساكنة\""` | — |
| [SRC-E599346ABE-L000482](../generate_index.py#L482) | 482 | `"    if suffix == \".sh\":"` | — |
| [SRC-E599346ABE-L000483](../generate_index.py#L483) | 483 | `"        return \"جرد الملف + دوال Shell\""` | — |
| [SRC-E599346ABE-L000484](../generate_index.py#L484) | 484 | `"    if path.name.lower() in {\"dockerfile\", \"makefile\", \"procfile\"}:"` | — |
| [SRC-E599346ABE-L000485](../generate_index.py#L485) | 485 | `"        return \"جرد الملف + أسماء إعدادات عامة إن وجدت\""` | — |
| [SRC-E599346ABE-L000486](../generate_index.py#L486) | 486 | `"    if path.name.lower() == \".env.example\" or suffix == \".example\":"` | — |
| [SRC-E599346ABE-L000487](../generate_index.py#L487) | 487 | `"        return \"جرد الملف + أسماء إعدادات عامة إن وجدت\""` | — |
| [SRC-E599346ABE-L000488](../generate_index.py#L488) | 488 | `"    return \"جرد ملف نصي فقط\""` | — |
| [SRC-E599346ABE-L000489](../generate_index.py#L489) | 489 | `""` | — |
| [SRC-E599346ABE-L000490](../generate_index.py#L490) | 490 | `""` | — |
| [SRC-E599346ABE-L000491](../generate_index.py#L491) | 491 | `"def build_file_inventory(root: Path) -> list[IndexedFile]:"` | — |
| [SRC-E599346ABE-L000492](../generate_index.py#L492) | 492 | `"    \"\"\"Inventory repository files and record whether static symbol scanning was possible.\"\"\""` | — |
| [SRC-E599346ABE-L000493](../generate_index.py#L493) | 493 | `"    inventory: list[IndexedFile] = []"` | — |
| [SRC-E599346ABE-L000494](../generate_index.py#L494) | 494 | `"    for path in discover_repository_files(root):"` | — |
| [SRC-E599346ABE-L000495](../generate_index.py#L495) | 495 | `"        text = _read_text_bounded(path)"` | — |
| [SRC-E599346ABE-L000496](../generate_index.py#L496) | 496 | `"        inventory.append("` | — |
| [SRC-E599346ABE-L000497](../generate_index.py#L497) | 497 | `"            IndexedFile("` | — |
| [SRC-E599346ABE-L000498](../generate_index.py#L498) | 498 | `"                file=path.relative_to(root).as_posix(),"` | — |
| [SRC-E599346ABE-L000499](../generate_index.py#L499) | 499 | `"                file_type=_file_type(path),"` | — |
| [SRC-E599346ABE-L000500](../generate_index.py#L500) | 500 | `"                size_bytes=path.stat().st_size,"` | — |
| [SRC-E599346ABE-L000501](../generate_index.py#L501) | 501 | `"                line_count=_count_lines(text) if text is not None else None,"` | — |
| [SRC-E599346ABE-L000502](../generate_index.py#L502) | 502 | `"                indexing_scope=_indexing_scope(path, text),"` | — |
| [SRC-E599346ABE-L000503](../generate_index.py#L503) | 503 | `"                file_id=_stable_file_id(path.relative_to(root).as_posix()),"` | — |
| [SRC-E599346ABE-L000504](../generate_index.py#L504) | 504 | `"                category=_category_for_path(path.relative_to(root).as_posix()),"` | — |
| [SRC-E599346ABE-L000505](../generate_index.py#L505) | 505 | `"            )"` | — |
| [SRC-E599346ABE-L000506](../generate_index.py#L506) | 506 | `"        )"` | — |
| [SRC-E599346ABE-L000507](../generate_index.py#L507) | 507 | `"    return inventory"` | — |
| [SRC-E599346ABE-L000508](../generate_index.py#L508) | 508 | `""` | — |
| [SRC-E599346ABE-L000509](../generate_index.py#L509) | 509 | `""` | — |
| [SRC-E599346ABE-L000510](../generate_index.py#L510) | 510 | `"def _tracked_paths_or_none(root: Path) -> set[str] \| None:"` | — |
| [SRC-E599346ABE-L000511](../generate_index.py#L511) | 511 | `"    \"\"\"Return tracked repository paths, or None when the root is not a Git checkout.\"\"\""` | — |
| [SRC-E599346ABE-L000512](../generate_index.py#L512) | 512 | `"    try:"` | — |
| [SRC-E599346ABE-L000513](../generate_index.py#L513) | 513 | `"        result = subprocess.run("` | — |
| [SRC-E599346ABE-L000514](../generate_index.py#L514) | 514 | `"            [\"git\", \"-C\", str(root), \"ls-files\", \"-z\"],"` | — |
| [SRC-E599346ABE-L000515](../generate_index.py#L515) | 515 | `"            check=True,"` | — |
| [SRC-E599346ABE-L000516](../generate_index.py#L516) | 516 | `"            capture_output=True,"` | — |
| [SRC-E599346ABE-L000517](../generate_index.py#L517) | 517 | `"        )"` | — |
| [SRC-E599346ABE-L000518](../generate_index.py#L518) | 518 | `"    except (OSError, subprocess.SubprocessError):"` | — |
| [SRC-E599346ABE-L000519](../generate_index.py#L519) | 519 | `"        return None"` | — |
| [SRC-E599346ABE-L000520](../generate_index.py#L520) | 520 | `"    try:"` | — |
| [SRC-E599346ABE-L000521](../generate_index.py#L521) | 521 | `"        return {"` | — |
| [SRC-E599346ABE-L000522](../generate_index.py#L522) | 522 | `"            path"` | — |
| [SRC-E599346ABE-L000523](../generate_index.py#L523) | 523 | `"            for path in result.stdout.decode(\"utf-8\").split(\"\\x00\")"` | — |
| [SRC-E599346ABE-L000524](../generate_index.py#L524) | 524 | `"            if path"` | — |
| [SRC-E599346ABE-L000525](../generate_index.py#L525) | 525 | `"        }"` | — |
| [SRC-E599346ABE-L000526](../generate_index.py#L526) | 526 | `"    except UnicodeError:"` | — |
| [SRC-E599346ABE-L000527](../generate_index.py#L527) | 527 | `"        return None"` | — |
| [SRC-E599346ABE-L000528](../generate_index.py#L528) | 528 | `""` | — |
| [SRC-E599346ABE-L000529](../generate_index.py#L529) | 529 | `""` | — |
| [SRC-E599346ABE-L000530](../generate_index.py#L530) | 530 | `"def discover_excluded_paths(root: Path) -> list[tuple[str, str]]:"` | — |
| [SRC-E599346ABE-L000531](../generate_index.py#L531) | 531 | `"    \"\"\"List excluded tracked path names and reasons without opening excluded contents.\"\"\""` | — |
| [SRC-E599346ABE-L000532](../generate_index.py#L532) | 532 | `"    tracked_paths = _tracked_paths_or_none(root)"` | — |
| [SRC-E599346ABE-L000533](../generate_index.py#L533) | 533 | `""` | — |
| [SRC-E599346ABE-L000534](../generate_index.py#L534) | 534 | `"    def tracked_scope_contains(relative_path: str, is_directory: bool = False) -> bool:"` | — |
| [SRC-E599346ABE-L000535](../generate_index.py#L535) | 535 | `"        if tracked_paths is None:"` | — |
| [SRC-E599346ABE-L000536](../generate_index.py#L536) | 536 | `"            return True"` | — |
| [SRC-E599346ABE-L000537](../generate_index.py#L537) | 537 | `"        normalized = relative_path.rstrip(\"/\")"` | — |
| [SRC-E599346ABE-L000538](../generate_index.py#L538) | 538 | `"        if is_directory:"` | — |
| [SRC-E599346ABE-L000539](../generate_index.py#L539) | 539 | `"            prefix = normalized + \"/\""` | — |
| [SRC-E599346ABE-L000540](../generate_index.py#L540) | 540 | `"            return any(path.startswith(prefix) for path in tracked_paths)"` | — |
| [SRC-E599346ABE-L000541](../generate_index.py#L541) | 541 | `"        return normalized in tracked_paths"` | — |
| [SRC-E599346ABE-L000542](../generate_index.py#L542) | 542 | `""` | — |
| [SRC-E599346ABE-L000543](../generate_index.py#L543) | 543 | `"    excluded: list[tuple[str, str]] = ["` | — |
| [SRC-E599346ABE-L000544](../generate_index.py#L544) | 544 | `"        (path, \"مخرج فهرسة مولد مستبعد لمنع الحلقة الذاتية\")"` | — |
| [SRC-E599346ABE-L000545](../generate_index.py#L545) | 545 | `"        for path in sorted(INDEX_OUTPUT_PATHS)"` | — |
| [SRC-E599346ABE-L000546](../generate_index.py#L546) | 546 | `"    ]"` | — |
| [SRC-E599346ABE-L000547](../generate_index.py#L547) | 547 | `"    excluded.append("` | — |
| [SRC-E599346ABE-L000548](../generate_index.py#L548) | 548 | `"        ("` | — |
| [SRC-E599346ABE-L000549](../generate_index.py#L549) | 549 | `"            SOURCE_LINES_PAGES_DIR + \"/\","` | — |
| [SRC-E599346ABE-L000550](../generate_index.py#L550) | 550 | `"            \"مجلد صفحات فهرسة مولدة مستبعد لمنع الحلقة الذاتية\","` | — |
| [SRC-E599346ABE-L000551](../generate_index.py#L551) | 551 | `"        )"` | — |
| [SRC-E599346ABE-L000552](../generate_index.py#L552) | 552 | `"    )"` | — |
| [SRC-E599346ABE-L000553](../generate_index.py#L553) | 553 | `"    for current_directory, directory_names, file_names in os.walk("` | — |
| [SRC-E599346ABE-L000554](../generate_index.py#L554) | 554 | `"        root,"` | — |
| [SRC-E599346ABE-L000555](../generate_index.py#L555) | 555 | `"        topdown=True,"` | — |
| [SRC-E599346ABE-L000556](../generate_index.py#L556) | 556 | `"        followlinks=False,"` | — |
| [SRC-E599346ABE-L000557](../generate_index.py#L557) | 557 | `"    ):"` | — |
| [SRC-E599346ABE-L000558](../generate_index.py#L558) | 558 | `"        kept_directories: list[str] = []"` | — |
| [SRC-E599346ABE-L000559](../generate_index.py#L559) | 559 | `"        for name in sorted(directory_names):"` | — |
| [SRC-E599346ABE-L000560](../generate_index.py#L560) | 560 | `"            candidate = Path(current_directory) / name"` | — |
| [SRC-E599346ABE-L000561](../generate_index.py#L561) | 561 | `"            relative = candidate.relative_to(root).as_posix()"` | — |
| [SRC-E599346ABE-L000562](../generate_index.py#L562) | 562 | `"            if candidate.is_symlink():"` | — |
| [SRC-E599346ABE-L000563](../generate_index.py#L563) | 563 | `"                if tracked_scope_contains(relative, is_directory=True):"` | — |
| [SRC-E599346ABE-L000564](../generate_index.py#L564) | 564 | `"                    excluded.append((relative + \"/\", \"رابط رمزي مستبعد لسلامة التتبع\"))"` | — |
| [SRC-E599346ABE-L000565](../generate_index.py#L565) | 565 | `"            elif name in EXCLUDED_DIRECTORIES:"` | — |
| [SRC-E599346ABE-L000566](../generate_index.py#L566) | 566 | `"                if tracked_scope_contains(relative, is_directory=True):"` | — |
| [SRC-E599346ABE-L000567](../generate_index.py#L567) | 567 | `"                    excluded.append((relative + \"/\", \"مجلد بيئة أو اعتماديات أو مخرجات مولدة مستبعد\"))"` | — |
| [SRC-E599346ABE-L000568](../generate_index.py#L568) | 568 | `"            elif name.lower().endswith((\".egg-info\", \".dist-info\")):"` | — |
| [SRC-E599346ABE-L000569](../generate_index.py#L569) | 569 | `"                if tracked_scope_contains(relative, is_directory=True):"` | — |
| [SRC-E599346ABE-L000570](../generate_index.py#L570) | 570 | `"                    excluded.append((relative + \"/\", \"بيانات تغليف مولدة مستبعدة\"))"` | — |
| [SRC-E599346ABE-L000571](../generate_index.py#L571) | 571 | `"            elif relative == SOURCE_LINES_PAGES_DIR:"` | — |
| [SRC-E599346ABE-L000572](../generate_index.py#L572) | 572 | `"                excluded.append("` | — |
| [SRC-E599346ABE-L000573](../generate_index.py#L573) | 573 | `"                    ("` | — |
| [SRC-E599346ABE-L000574](../generate_index.py#L574) | 574 | `"                        relative + \"/\","` | — |
| [SRC-E599346ABE-L000575](../generate_index.py#L575) | 575 | `"                        \"مجلد صفحات فهرسة مولدة مستبعد لمنع الحلقة الذاتية\","` | — |
| [SRC-E599346ABE-L000576](../generate_index.py#L576) | 576 | `"                    )"` | — |
| [SRC-E599346ABE-L000577](../generate_index.py#L577) | 577 | `"                )"` | — |
| [SRC-E599346ABE-L000578](../generate_index.py#L578) | 578 | `"            else:"` | — |
| [SRC-E599346ABE-L000579](../generate_index.py#L579) | 579 | `"                kept_directories.append(name)"` | — |
| [SRC-E599346ABE-L000580](../generate_index.py#L580) | 580 | `"        directory_names[:] = kept_directories"` | — |
| [SRC-E599346ABE-L000581](../generate_index.py#L581) | 581 | `""` | — |
| [SRC-E599346ABE-L000582](../generate_index.py#L582) | 582 | `"        for name in sorted(file_names):"` | — |
| [SRC-E599346ABE-L000583](../generate_index.py#L583) | 583 | `"            candidate = Path(current_directory) / name"` | — |
| [SRC-E599346ABE-L000584](../generate_index.py#L584) | 584 | `"            relative = candidate.relative_to(root).as_posix()"` | — |
| [SRC-E599346ABE-L000585](../generate_index.py#L585) | 585 | `"            if candidate.is_symlink():"` | — |
| [SRC-E599346ABE-L000586](../generate_index.py#L586) | 586 | `"                if tracked_scope_contains(relative):"` | — |
| [SRC-E599346ABE-L000587](../generate_index.py#L587) | 587 | `"                    excluded.append((relative, \"رابط رمزي مستبعد لسلامة التتبع\"))"` | — |
| [SRC-E599346ABE-L000588](../generate_index.py#L588) | 588 | `"            elif _is_sensitive_or_runtime_path(candidate):"` | — |
| [SRC-E599346ABE-L000589](../generate_index.py#L589) | 589 | `"                if tracked_scope_contains(relative):"` | — |
| [SRC-E599346ABE-L000590](../generate_index.py#L590) | 590 | `"                    if name.lower().startswith(\".env\") and name.lower() != \".env.example\":"` | — |
| [SRC-E599346ABE-L000591](../generate_index.py#L591) | 591 | `"                        reason = \"ملف بيئة محلي مستبعد وقائيًا؛ لم تُقرأ محتوياته\""` | — |
| [SRC-E599346ABE-L000592](../generate_index.py#L592) | 592 | `"                    elif candidate.suffix.lower() in EXCLUDED_SUFFIXES:"` | — |
| [SRC-E599346ABE-L000593](../generate_index.py#L593) | 593 | `"                        reason = \"قاعدة بيانات أو ملف مفتاح/شهادة مستبعد\""` | — |
| [SRC-E599346ABE-L000594](../generate_index.py#L594) | 594 | `"                    else:"` | — |
| [SRC-E599346ABE-L000595](../generate_index.py#L595) | 595 | `"                        reason = \"اسم ملف حساس معروف؛ لم تُقرأ محتوياته\""` | — |
| [SRC-E599346ABE-L000596](../generate_index.py#L596) | 596 | `"                    excluded.append((relative, reason))"` | — |
| [SRC-E599346ABE-L000597](../generate_index.py#L597) | 597 | `"            elif relative in INDEX_OUTPUT_PATHS:"` | — |
| [SRC-E599346ABE-L000598](../generate_index.py#L598) | 598 | `"                excluded.append((relative, \"مخرج فهرسة مولد مستبعد لمنع الحلقة الذاتية\"))"` | — |
| [SRC-E599346ABE-L000599](../generate_index.py#L599) | 599 | `"            elif ("` | — |
| [SRC-E599346ABE-L000600](../generate_index.py#L600) | 600 | `"                relative.startswith(SOURCE_LINES_PAGES_DIR + \"/\")"` | — |
| [SRC-E599346ABE-L000601](../generate_index.py#L601) | 601 | `"                and tracked_scope_contains(relative)"` | — |
| [SRC-E599346ABE-L000602](../generate_index.py#L602) | 602 | `"            ):"` | — |
| [SRC-E599346ABE-L000603](../generate_index.py#L603) | 603 | `"                excluded.append((relative, \"صفحة فهرسة مولدة مستبعدة لمنع الحلقة الذاتية\"))"` | — |
| [SRC-E599346ABE-L000604](../generate_index.py#L604) | 604 | `""` | — |
| [SRC-E599346ABE-L000605](../generate_index.py#L605) | 605 | `"    return sorted(set(excluded), key=lambda item: (item[0].casefold(), item[1]))"` | — |
| [SRC-E599346ABE-L000606](../generate_index.py#L606) | 606 | `""` | — |
| [SRC-E599346ABE-L000607](../generate_index.py#L607) | 607 | `""` | — |
| [SRC-E599346ABE-L000608](../generate_index.py#L608) | 608 | `"def _text_index_skip_reason(path: Path) -> str:"` | — |
| [SRC-E599346ABE-L000609](../generate_index.py#L609) | 609 | `"    \"\"\"Return a concrete safe reason when a file could not be line-indexed.\"\"\""` | — |
| [SRC-E599346ABE-L000610](../generate_index.py#L610) | 610 | `"    try:"` | — |
| [SRC-E599346ABE-L000611](../generate_index.py#L611) | 611 | `"        if path.stat().st_size > MAX_INDEXED_TEXT_BYTES:"` | — |
| [SRC-E599346ABE-L000612](../generate_index.py#L612) | 612 | `"            return f\"الحجم يتجاوز حد الفهرسة ({MAX_INDEXED_TEXT_BYTES} بايت)\""` | — |
| [SRC-E599346ABE-L000613](../generate_index.py#L613) | 613 | `"        if path.suffix.lower() == \".py\":"` | — |
| [SRC-E599346ABE-L000614](../generate_index.py#L614) | 614 | `"            with tokenize.open(str(path)) as source_stream:"` | — |
| [SRC-E599346ABE-L000615](../generate_index.py#L615) | 615 | `"                source = source_stream.read()"` | — |
| [SRC-E599346ABE-L000616](../generate_index.py#L616) | 616 | `"        else:"` | — |
| [SRC-E599346ABE-L000617](../generate_index.py#L617) | 617 | `"            source = path.read_text(encoding=\"utf-8\")"` | — |
| [SRC-E599346ABE-L000618](../generate_index.py#L618) | 618 | `"        if \"\\x00\" in source:"` | — |
| [SRC-E599346ABE-L000619](../generate_index.py#L619) | 619 | `"            return \"يحتوي محرف NUL؛ عومل كملف غير نصي\""` | — |
| [SRC-E599346ABE-L000620](../generate_index.py#L620) | 620 | `"    except (OSError, UnicodeError, LookupError, tokenize.TokenError):"` | — |
| [SRC-E599346ABE-L000621](../generate_index.py#L621) | 621 | `"        return \"تعذرت قراءته كنص صالح بترميز مدعوم\""` | — |
| [SRC-E599346ABE-L000622](../generate_index.py#L622) | 622 | `"    return \"سبب غير مصنف؛ يحتاج مراجعة أداة الفهرسة\""` | — |
| [SRC-E599346ABE-L000623](../generate_index.py#L623) | 623 | `""` | — |
| [SRC-E599346ABE-L000624](../generate_index.py#L624) | 624 | `""` | — |
| [SRC-E599346ABE-L000625](../generate_index.py#L625) | 625 | `"def validate_source_line_coverage("` | — |
| [SRC-E599346ABE-L000626](../generate_index.py#L626) | 626 | `"    root: Path,"` | — |
| [SRC-E599346ABE-L000627](../generate_index.py#L627) | 627 | `"    inventory: list[IndexedFile],"` | — |
| [SRC-E599346ABE-L000628](../generate_index.py#L628) | 628 | `"    source_lines: list[IndexedLine],"` | — |
| [SRC-E599346ABE-L000629](../generate_index.py#L629) | 629 | `") -> None:"` | — |
| [SRC-E599346ABE-L000630](../generate_index.py#L630) | 630 | `"    \"\"\"Fail generation if line coverage, IDs, or exact source text do not match.\"\"\""` | — |
| [SRC-E599346ABE-L000631](../generate_index.py#L631) | 631 | `"    eligible_files = {"` | — |
| [SRC-E599346ABE-L000632](../generate_index.py#L632) | 632 | `"        item.file: item"` | — |
| [SRC-E599346ABE-L000633](../generate_index.py#L633) | 633 | `"        for item in inventory"` | — |
| [SRC-E599346ABE-L000634](../generate_index.py#L634) | 634 | `"        if item.line_count is not None"` | — |
| [SRC-E599346ABE-L000635](../generate_index.py#L635) | 635 | `"    }"` | — |
| [SRC-E599346ABE-L000636](../generate_index.py#L636) | 636 | `"    expected_lines_by_file: dict[str, list[str]] = {}"` | — |
| [SRC-E599346ABE-L000637](../generate_index.py#L637) | 637 | `"    failures: list[str] = []"` | — |
| [SRC-E599346ABE-L000638](../generate_index.py#L638) | 638 | `"    seen_ids: set[str] = set()"` | — |
| [SRC-E599346ABE-L000639](../generate_index.py#L639) | 639 | `"    actual_lines: dict[str, list[int]] = {file: [] for file in eligible_files}"` | — |
| [SRC-E599346ABE-L000640](../generate_index.py#L640) | 640 | `""` | — |
| [SRC-E599346ABE-L000641](../generate_index.py#L641) | 641 | `"    # Re-read every eligible source independently to detect races or corrupted line records."` | — |
| [SRC-E599346ABE-L000642](../generate_index.py#L642) | 642 | `"    for file, item in eligible_files.items():"` | — |
| [SRC-E599346ABE-L000643](../generate_index.py#L643) | 643 | `"        source = _read_text_bounded(root / file)"` | — |
| [SRC-E599346ABE-L000644](../generate_index.py#L644) | 644 | `"        if source is None:"` | — |
| [SRC-E599346ABE-L000645](../generate_index.py#L645) | 645 | `"            failures.append(f\"{file}: تعذرت إعادة قراءة ملف مؤهل للتحقق\")"` | — |
| [SRC-E599346ABE-L000646](../generate_index.py#L646) | 646 | `"            expected_lines_by_file[file] = []"` | — |
| [SRC-E599346ABE-L000647](../generate_index.py#L647) | 647 | `"            continue"` | — |
| [SRC-E599346ABE-L000648](../generate_index.py#L648) | 648 | `"        expected_contents = source.splitlines()"` | — |
| [SRC-E599346ABE-L000649](../generate_index.py#L649) | 649 | `"        expected_lines_by_file[file] = expected_contents"` | — |
| [SRC-E599346ABE-L000650](../generate_index.py#L650) | 650 | `"        if len(expected_contents) != item.line_count:"` | — |
| [SRC-E599346ABE-L000651](../generate_index.py#L651) | 651 | `"            failures.append("` | — |
| [SRC-E599346ABE-L000652](../generate_index.py#L652) | 652 | `"                f\"{file}: تغير عدد الأسطر بعد إعداد الجرد \""` | — |
| [SRC-E599346ABE-L000653](../generate_index.py#L653) | 653 | `"                f\"(الجرد {item.line_count}، الحالي {len(expected_contents)})\""` | — |
| [SRC-E599346ABE-L000654](../generate_index.py#L654) | 654 | `"            )"` | — |
| [SRC-E599346ABE-L000655](../generate_index.py#L655) | 655 | `""` | — |
| [SRC-E599346ABE-L000656](../generate_index.py#L656) | 656 | `"    actual_records_by_file: dict[str, dict[int, IndexedLine]] = {"` | — |
| [SRC-E599346ABE-L000657](../generate_index.py#L657) | 657 | `"        file: {} for file in eligible_files"` | — |
| [SRC-E599346ABE-L000658](../generate_index.py#L658) | 658 | `"    }"` | — |
| [SRC-E599346ABE-L000659](../generate_index.py#L659) | 659 | `"    for source_line in source_lines:"` | — |
| [SRC-E599346ABE-L000660](../generate_index.py#L660) | 660 | `"        if source_line.file not in eligible_files:"` | — |
| [SRC-E599346ABE-L000661](../generate_index.py#L661) | 661 | `"            failures.append(f\"{source_line.file}: سجل سطر لملف غير مؤهل\")"` | — |
| [SRC-E599346ABE-L000662](../generate_index.py#L662) | 662 | `"            continue"` | — |
| [SRC-E599346ABE-L000663](../generate_index.py#L663) | 663 | `""` | — |
| [SRC-E599346ABE-L000664](../generate_index.py#L664) | 664 | `"        actual_lines[source_line.file].append(source_line.line)"` | — |
| [SRC-E599346ABE-L000665](../generate_index.py#L665) | 665 | `"        actual_records_by_file[source_line.file][source_line.line] = source_line"` | — |
| [SRC-E599346ABE-L000666](../generate_index.py#L666) | 666 | `"        expected_item = eligible_files[source_line.file]"` | — |
| [SRC-E599346ABE-L000667](../generate_index.py#L667) | 667 | `""` | — |
| [SRC-E599346ABE-L000668](../generate_index.py#L668) | 668 | `"        if source_line.line < 1:"` | — |
| [SRC-E599346ABE-L000669](../generate_index.py#L669) | 669 | `"            failures.append(f\"{source_line.file}: رقم سطر غير صالح {source_line.line}\")"` | — |
| [SRC-E599346ABE-L000670](../generate_index.py#L670) | 670 | `"            continue"` | — |
| [SRC-E599346ABE-L000671](../generate_index.py#L671) | 671 | `""` | — |
| [SRC-E599346ABE-L000672](../generate_index.py#L672) | 672 | `"        expected_contents = expected_lines_by_file.get(source_line.file, [])"` | — |
| [SRC-E599346ABE-L000673](../generate_index.py#L673) | 673 | `"        if ("` | — |
| [SRC-E599346ABE-L000674](../generate_index.py#L674) | 674 | `"            source_line.line <= len(expected_contents)"` | — |
| [SRC-E599346ABE-L000675](../generate_index.py#L675) | 675 | `"            and source_line.content != expected_contents[source_line.line - 1]"` | — |
| [SRC-E599346ABE-L000676](../generate_index.py#L676) | 676 | `"        ):"` | — |
| [SRC-E599346ABE-L000677](../generate_index.py#L677) | 677 | `"            failures.append("` | — |
| [SRC-E599346ABE-L000678](../generate_index.py#L678) | 678 | `"                f\"{source_line.file}:{source_line.line}: نص السطر لا يطابق المصدر\""` | — |
| [SRC-E599346ABE-L000679](../generate_index.py#L679) | 679 | `"            )"` | — |
