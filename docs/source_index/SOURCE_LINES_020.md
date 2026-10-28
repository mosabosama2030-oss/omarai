# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **020**
- سجلات الأسطر: **800**
- النطاق: SRC-E73001D9AC-L000356 إلى SRC-D17CE3D12F-L000252
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## وثائق وفهرسة

### FILE-E73001D9AC — [docs/OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-E73001D9AC-L000356](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L356) | 356 | `"- **Zero Trust وأقل صلاحية:** لا تُمنح الثقة بسبب موقع المكوّن أو ملكيته. تُفحص هوية الطلب وصلاحية المستخدم والعملية والمورد عند كل حد مناسب، وتطبق سياسة المنع الافتراضي. لا يملك LLM أو Skill أو Workflow أو Agent Profile صلاحية منح نفسه إذنًا."` | — |
| [SRC-E73001D9AC-L000357](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L357) | 357 | `"- **Tool Broker قابل للاختبار:** كل استدعاء أداة يمر عبر وسيط يفرض المصادقة والتفويض والتحقق من المخطط والميزانية والمهلة ونطاق البيانات، ويسجل نتيجة التنفيذ المنقحة. لا ينفذ النموذج أوامر shell حرة أو كودًا حرًا."` | — |
| [SRC-E73001D9AC-L000358](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L358) | 358 | `"- **حقن التعليمات:** كل محتوى مستخدم أو ويب أو ملف أو ذاكرة أو مخرجات نموذج بيانات غير موثوقة حتى التحقق. تُفصل البيانات عن سياسة النظام، وتخضع الخطط والاستدعاءات لمخططات وallowlists وحدود، ولا تكفي البرومبتات أو فلاتر الكلمات كحاجز وحيد."` | — |
| [SRC-E73001D9AC-L000359](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L359) | 359 | `"- **الشبكة وSSRF:** يجب فحص عناوين الوجهة وDNS وعناوين IPv4/IPv6 والتحويلات وإعادة التوجيه وحدود الحجم والوقت؛ تمنع الاتصالات إلى loopback والشبكات الخاصة وlink-local وmetadata والمحجوزات، مع اختبار فعلي وفق بيئة التشغيل. لا يُفترض أن الحماية موجودة أو مكتملة دون اختبار."` | — |
| [SRC-E73001D9AC-L000360](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L360) | 360 | `"- **API والواجهة:** تُفرض المصادقة وصلاحيات الكائنات على الخادم، مع ضوابط input validation وrate limiting وCORS وCSRF عندما ينطبق وoutput encoding/XSS والحماية من path traversal وأخطاء لا تكشف أسرارًا. لا تُعرض نقاط الإدارة والتشخيص علنًا بلا حماية."` | — |
| [SRC-E73001D9AC-L000361](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L361) | 361 | `"- **الأسرار والخصوصية:** لا أسرار في Git أو المتصفح أو سجلات الطلب. يُقيَّم تدفق البيانات لكل مزود نموذج وfallback، ولا تُرسل بيانات حساسة إلى مزود غير معتمد. تُنقح السجلات، وتُحدد صلاحياتها وفترات الاحتفاظ والحذف، وتُراجع النسخ الاحتياطية واستعادتها."` | — |
| [SRC-E73001D9AC-L000362](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L362) | 362 | `"- **العزل وحالة المهمة:** سياق مستقل لكل طلب؛ لا ذاكرة أو متغيرات mutable مشتركة بلا عزل مثبت. لا تُفترض حماية تعدد المستخدمين دون اختبارات تداخل وعزل. كل إجراء خارجي حساس يتطلب تفويضًا وتأكيدًا مناسبين، وidempotency عند احتمالية التكرار."` | — |
| [SRC-E73001D9AC-L000363](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L363) | 363 | `"- **سلسلة التوريد وCI/CD:** أقل صلاحيات للرموز والأكشنات، وفحص الاعتماديات والأسرار، وتثبيت إصدارات عند ملاءمة ذلك، ومنع PR غير الموثوق من الوصول إلى أسرار الإنتاج، وربط artifact بالـ commit والاختبارات التي أنتجته."` | — |
| [SRC-E73001D9AC-L000364](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L364) | 364 | `"- **توليد الكود:** لا يُشغّل كود مولد من النموذج في مسار الإنتاج. أي تجربة مستقبلية تحتاج إلى قرار مستقل، وبيئة عزل مختبرة، وشبكة مغلقة افتراضيًا، وملفات وأسرار غير متاحة للعملية، وحدود موارد، واختبارات هروب وتصعيد صلاحيات، ومراجعة بشرية."` | — |
| [SRC-E73001D9AC-L000365](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L365) | 365 | `"- **الكشف والاستجابة:** سجلات منقحة، وحدود إنذار، ووسيلة إيقاف للمسار المتأثر، وإجراء تدوير للأسرار واحتواء الحادث وتحليل السبب الجذري واختبار منع التكرار. حدود الخدمة والتكلفة جزء من الأمن ضد الإساءة والاستنزاف."` | — |
| [SRC-E73001D9AC-L000366](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L366) | 366 | `"- **بوابة القبول الأمني:** لا تُفعّل قدرة جديدة ذات خطر قبل اجتياز الاختبارات الأمنية المرتبطة بها. وجود سياسة أو sandbox أو فحص ثابت لا يثبت وحده فعالية الحماية؛ يلزم دليل على الضبط في بيئة ونطاق معروفين. تُسجّل الحالات غير المختبرة NOT_RUN/UNKNOWN ولا تُعامل كنجاح."` | — |
| [SRC-E73001D9AC-L000367](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L367) | 367 | `""` | — |
| [SRC-E73001D9AC-L000368](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L368) | 368 | `"التفاصيل التفصيلية للأصول وحدود الثقة ونموذج التهديد واختبارات الرفض والعزل وسلسلة التوريد والاستجابة للحوادث موجودة في القسم 17 من وثيقة المعمارية المرتبطة."` | — |
| [SRC-E73001D9AC-L000369](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L369) | 369 | `""` | — |
| [SRC-E73001D9AC-L000370](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L370) | 370 | `"---"` | — |
| [SRC-E73001D9AC-L000371](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L371) | 371 | `""` | — |
| [SRC-E73001D9AC-L000372](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L372) | 372 | `"# الجزء الخامس — الأداء، التزامن، السعة والتوسع"` | — |
| [SRC-E73001D9AC-L000373](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L373) | 373 | `""` | — |
| [SRC-E73001D9AC-L000374](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L374) | 374 | `"## 7. استراتيجية التحمل والسرعة"` | — |
| [SRC-E73001D9AC-L000375](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L375) | 375 | `""` | — |
| [SRC-E73001D9AC-L000376](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L376) | 376 | `"### 7.1 ميزانية لكل طلب"` | — |
| [SRC-E73001D9AC-L000377](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L377) | 377 | `"يتضمن سياق الطلب، بحسب المسار:"` | — |
| [SRC-E73001D9AC-L000378](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L378) | 378 | `"- مهلة إجمالية absolute deadline."` | — |
| [SRC-E73001D9AC-L000379](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L379) | 379 | `"- حدًا لعدد مراحل التخطيط وإعادة التخطيط."` | — |
| [SRC-E73001D9AC-L000380](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L380) | 380 | `"- حدًا لعدد استدعاءات أدوات البحث."` | — |
| [SRC-E73001D9AC-L000381](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L381) | 381 | `"- حدًا لحجم النتائج والصفحات والنص المستخرج."` | — |
| [SRC-E73001D9AC-L000382](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L382) | 382 | `"- حدًا لعدد استدعاءات النموذج وحجم المدخلات والمخرجات."` | — |
| [SRC-E73001D9AC-L000383](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L383) | 383 | `"- حدًا للتزامن لكل موفر خارجي."` | — |
| [SRC-E73001D9AC-L000384](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L384) | 384 | `"- حدًا لاستخدام الذاكرة والمهام الفرعية حيث يمكن فرضه."` | — |
| [SRC-E73001D9AC-L000385](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L385) | 385 | `"- سياسة واضحة للتوقف والإجابة الجزئية عند نفاد الميزانية."` | — |
| [SRC-E73001D9AC-L000386](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L386) | 386 | `""` | — |
| [SRC-E73001D9AC-L000387](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L387) | 387 | `"تُحدد القيم من واقع الاختبارات وإمكانات الاستضافة؛ لا توجد أرقام سحرية تصلح لجميع البيئات."` | — |
| [SRC-E73001D9AC-L000388](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L388) | 388 | `""` | — |
| [SRC-E73001D9AC-L000389](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L389) | 389 | `"### 7.2 تحسين المسارات"` | — |
| [SRC-E73001D9AC-L000390](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L390) | 390 | `"- تصنيف مبكر للسؤال: مباشر، يحتاج بحثًا، متعدد الخطوات، غير مسموح أو غير واضح."` | — |
| [SRC-E73001D9AC-L000391](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L391) | 391 | `"- عدم استدعاء النموذج للتصنيف إن أمكن حسم السؤال بقواعد بسيطة موثوقة."` | — |
| [SRC-E73001D9AC-L000392](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L392) | 392 | `"- عدم البحث في الحالات التي لا تضيف فيها المصادر قيمة."` | — |
| [SRC-E73001D9AC-L000393](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L393) | 393 | `"- البحث المتوازي فقط للمهام المستقلة وبحد تزامن معلوم."` | — |
| [SRC-E73001D9AC-L000394](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L394) | 394 | `"- إيقاف البحث عندما تتحقق تغطية كافية بحسب معايير محددة، لا بعد عدد اعتباطي من الاستدعاءات فقط."` | — |
| [SRC-E73001D9AC-L000395](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L395) | 395 | `"- منع التكرار عبر fingerprint أو مفاتيح cache مناسبة."` | — |
| [SRC-E73001D9AC-L000396](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L396) | 396 | `"- ضغط السياق المرسل إلى النموذج إلى المعلومات اللازمة، مع الحفاظ على المصادر والتحذيرات المهمة."` | — |
| [SRC-E73001D9AC-L000397](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L397) | 397 | `"- قياس فائدة كل تمريرة: التحسن في جودة الإجابة مقابل الوقت والتكلفة؛ وإزالة أي تمريرة لا تقدم فائدة مثبتة."` | — |
| [SRC-E73001D9AC-L000398](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L398) | 398 | `"- فصل زمن الخادم عن زمن المزود الخارجي حتى يُعرف مصدر البطء."` | — |
| [SRC-E73001D9AC-L000399](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L399) | 399 | `""` | — |
| [SRC-E73001D9AC-L000400](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L400) | 400 | `"### 7.3 حماية التنفيذ المتزامن"` | — |
| [SRC-E73001D9AC-L000401](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L401) | 401 | `"- عدم مشاركة كائنات الطلبات mutable بين جلسات المستخدمين."` | — |
| [SRC-E73001D9AC-L000402](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L402) | 402 | `"- تجنب متغيرات global التي تحمل تاريخ مستخدم أو ميزانية طلب."` | — |
| [SRC-E73001D9AC-L000403](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L403) | 403 | `"- فرض حدود concurrency لكل نوع مورد ومزود."` | — |
| [SRC-E73001D9AC-L000404](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L404) | 404 | `"- استخدام أقفال أو معاملات للبيانات التي قد تُعدل بالتوازي."` | — |
| [SRC-E73001D9AC-L000405](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L405) | 405 | `"- كشف تداخل الطلبات في الاختبارات باستخدام معرّفات مستخدمين وبيانات مميزة ومخرجات قابلة للتحقق."` | — |
| [SRC-E73001D9AC-L000406](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L406) | 406 | `"- التحقق من سلوك الإلغاء وانتهاء المهلة وعدم تسرب موارد التنفيذ."` | — |
| [SRC-E73001D9AC-L000407](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L407) | 407 | `""` | — |
| [SRC-E73001D9AC-L000408](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L408) | 408 | `"### 7.4 المرونة عند تعطل الموفرات"` | — |
| [SRC-E73001D9AC-L000409](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L409) | 409 | `"- timeout لكل اتصال."` | — |
| [SRC-E73001D9AC-L000410](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L410) | 410 | `"- circuit breaker مع حالة half-open لاختبار عودة الخدمة."` | — |
| [SRC-E73001D9AC-L000411](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L411) | 411 | `"- retry محدود مع backoff وjitter إذا كانت العملية آمنة للإعادة."` | — |
| [SRC-E73001D9AC-L000412](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L412) | 412 | `"- fallback محدد ومختبر، لا سلسلة مفتوحة من بدائل مجهولة."` | — |
| [SRC-E73001D9AC-L000413](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L413) | 413 | `"- تمييز الفشل الكامل من الانخفاض في مستوى الخدمة."` | — |
| [SRC-E73001D9AC-L000414](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L414) | 414 | `"- المحافظة على إجابة مفيدة مع التحذير عندما يمكن ذلك، وإبلاغ المستخدم عندما لا يتوفر دليل كافٍ."` | — |
| [SRC-E73001D9AC-L000415](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L415) | 415 | `"- عدم وصف fallback بأنه مكافئ في الجودة دون مقارنة."` | — |
| [SRC-E73001D9AC-L000416](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L416) | 416 | `"- لا يجوز أن يؤدي فشل المراجعة الاختيارية إلى محو إجابة صحيحة مكتملة تلقائيًا؛ تعتمد السياسة على المخاطر."` | — |
| [SRC-E73001D9AC-L000417](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L417) | 417 | `""` | — |
| [SRC-E73001D9AC-L000418](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L418) | 418 | `"### 7.5 التوسع"` | — |
| [SRC-E73001D9AC-L000419](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L419) | 419 | `"التدرج الموصى به:"` | — |
| [SRC-E73001D9AC-L000420](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L420) | 420 | `"1. كود منظم وحدود واضحة واختبارات تزامن."` | — |
| [SRC-E73001D9AC-L000421](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L421) | 421 | `"2. ضبط موارد العملية الواحدة والمراقبة."` | — |
| [SRC-E73001D9AC-L000422](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L422) | 422 | `"3. عزل موصلات البطء عن المسارات السريعة."` | — |
| [SRC-E73001D9AC-L000423](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L423) | 423 | `"4. إضافة طوابير وعمال للمهام الطويلة عند الحاجة."` | — |
| [SRC-E73001D9AC-L000424](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L424) | 424 | `"5. نقل البيانات إلى تخزين مناسب عند إثبات حدود المخزن الحالي."` | — |
| [SRC-E73001D9AC-L000425](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L425) | 425 | `"6. إضافة نسخ متعددة للخدمة وتخزين مشترك وموازن تحميل عندما تسمح المنصة والقياسات."` | — |
| [SRC-E73001D9AC-L000426](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L426) | 426 | `"7. اختبارات مناطق فشل ونسخ احتياطي وتعافٍ عندما تصبح متطلبات الخدمة تبررها."` | — |
| [SRC-E73001D9AC-L000427](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L427) | 427 | `""` | — |
| [SRC-E73001D9AC-L000428](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L428) | 428 | `"لا يُفترض أن الاستضافة المجانية تضمن توافرًا عاليًا أو موارد مضمونة أو توسعًا أفقيًا. يجب توثيق حدود الخطة الفعلية والقياسات بدل ادعاء مستوى مؤسسي لا تدعمه الاستضافة."` | — |
| [SRC-E73001D9AC-L000429](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L429) | 429 | `""` | — |
| [SRC-E73001D9AC-L000430](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L430) | 430 | `"## 8. مؤشرات الأداء والاعتمادية"` | — |
| [SRC-E73001D9AC-L000431](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L431) | 431 | `""` | — |
| [SRC-E73001D9AC-L000432](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L432) | 432 | `"يجب جمع هذه المقاييس بحسب المسار والموفر والإصدار، مع تجنب البيانات الحساسة:"` | — |
| [SRC-E73001D9AC-L000433](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L433) | 433 | `""` | — |
| [SRC-E73001D9AC-L000434](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L434) | 434 | `"- زمن الاستجابة p50 وp95 وp99."` | — |
| [SRC-E73001D9AC-L000435](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L435) | 435 | `"- معدل الطلبات الناجحة ومعدل 4xx و5xx والمهلات."` | — |
| [SRC-E73001D9AC-L000436](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L436) | 436 | `"- throughput بوحدة requests/second."` | — |
| [SRC-E73001D9AC-L000437](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L437) | 437 | `"- الطلبات النشطة، والانتظار، وعمق الطابور."` | — |
| [SRC-E73001D9AC-L000438](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L438) | 438 | `"- زمن البحث، وزمن جلب الصفحات، وزمن النموذج، وزمن التحقق."` | — |
| [SRC-E73001D9AC-L000439](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L439) | 439 | `"- عدد استدعاءات المزودات والصفحات والرموز عند إتاحتها."` | — |
| [SRC-E73001D9AC-L000440](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L440) | 440 | `"- معدل استخدام cache ومعدل النتائج المكررة."` | — |
| [SRC-E73001D9AC-L000441](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L441) | 441 | `"- الذاكرة والمعالج وعدد الاتصالات المفتوحة."` | — |
| [SRC-E73001D9AC-L000442](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L442) | 442 | `"- نسبة الطلبات المنفذة ضمن الميزانية."` | — |
| [SRC-E73001D9AC-L000443](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L443) | 443 | `"- نسبة نجاح الأدوات لكل موصل وتوزيع أسباب الفشل."` | — |
| [SRC-E73001D9AC-L000444](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L444) | 444 | `"- تكلفة الخدمة المقدرة لكل طلب عندما تكون هناك تكلفة قابلة للحساب."` | — |
| [SRC-E73001D9AC-L000445](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L445) | 445 | `"- مؤشرات الجودة: الدعم بالمصادر، وتغطية الاستشهادات، وأخطاء الوقائع، والتصريحات غير المدعومة."` | — |
| [SRC-E73001D9AC-L000446](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L446) | 446 | `""` | — |
| [SRC-E73001D9AC-L000447](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L447) | 447 | `"### 8.1 أهداف الخدمة (SLOs)"` | — |
| [SRC-E73001D9AC-L000448](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L448) | 448 | `"- يبدأ العمل بقياس خط الأساس على بيئة موثقة، ثم يعتمد مالك المشروع أهدافًا رقمية واقعية لكل فئة طلب."` | — |
| [SRC-E73001D9AC-L000449](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L449) | 449 | `"- يجب فصل SLO داخل سيطرة التطبيق عن زمن مزود خارجي لا يتحكم فيه التطبيق."` | — |
| [SRC-E73001D9AC-L000450](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L450) | 450 | `"- كل SLO له نافذة قياس وتعريف للنجاح ومصدر بيانات واستثناءات موثقة."` | — |
| [SRC-E73001D9AC-L000451](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L451) | 451 | `"- لا تعلن قدرة استيعاب معينة من المستخدمين إلا بعد اختبارها تحت حمل موثق مع تحديد البيئة وحجم الطلبات ونسبة الأخطاء."` | — |
| [SRC-E73001D9AC-L000452](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L452) | 452 | `"- أي هدف رقمي قبل القياس موسوم PROPOSED، وليس وعدًا للمستخدم."` | — |
| [SRC-E73001D9AC-L000453](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L453) | 453 | `""` | — |
| [SRC-E73001D9AC-L000454](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L454) | 454 | `"---"` | — |
| [SRC-E73001D9AC-L000455](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L455) | 455 | `""` | — |
| [SRC-E73001D9AC-L000456](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L456) | 456 | `"# الجزء السادس — جودة الإجابات والذكاء العملي"` | — |
| [SRC-E73001D9AC-L000457](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L457) | 457 | `""` | — |
| [SRC-E73001D9AC-L000458](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L458) | 458 | `"## 9. عقد الإجابة"` | — |
| [SRC-E73001D9AC-L000459](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L459) | 459 | `""` | — |
| [SRC-E73001D9AC-L000460](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L460) | 460 | `"يجب أن يسعى Omarai إلى:"` | — |
| [SRC-E73001D9AC-L000461](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L461) | 461 | `"1. فهم السؤال وسياقه، مع طلب توضيح فقط عند الضرورة الحقيقية."` | — |
| [SRC-E73001D9AC-L000462](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L462) | 462 | `"2. الإجابة بالعربية الواضحة افتراضيًا وباللغة المطلوبة عند طلبها."` | — |
| [SRC-E73001D9AC-L000463](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L463) | 463 | `"3. استخدام بحث حديث للمعلومات المتغيرة أو الأسئلة التي تحتاج إلى مصادر."` | — |
| [SRC-E73001D9AC-L000464](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L464) | 464 | `"4. تمييز الحقائق من الاستنتاجات والتوصيات والافتراضات."` | — |
| [SRC-E73001D9AC-L000465](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L465) | 465 | `"5. عرض روابط المصدر وسياق زمني مناسب حيثما أمكن."` | — |
| [SRC-E73001D9AC-L000466](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L466) | 466 | `"6. الإفصاح عن قصور التغطية أو تعذر الوصول أو تضارب المصادر."` | — |
| [SRC-E73001D9AC-L000467](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L467) | 467 | `"7. عدم اختلاق مصادر أو نتائج أدوات أو ملفات أو تنفيذات."` | — |
| [SRC-E73001D9AC-L000468](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L468) | 468 | `"8. عدم ادعاء استعمال أداة أو نموذج أو مصدر لم يُستخدم فعليًا."` | — |
| [SRC-E73001D9AC-L000469](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L469) | 469 | `"9. التصريح بعدم المعرفة عندما تكون الأدلة غير كافية."` | — |
| [SRC-E73001D9AC-L000470](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L470) | 470 | `"10. توضيح ما أنجز وما فشل في المهام متعددة الخطوات."` | — |
| [SRC-E73001D9AC-L000471](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L471) | 471 | `"11. صياغة إجابات عملية ومباشرة مع توسع متدرج حسب تعقيد السؤال."` | — |
| [SRC-E73001D9AC-L000472](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L472) | 472 | `"12. احترام حدود الصلاحيات والسياسات حتى لو طلبت التعليمات المسترجعة خلاف ذلك."` | — |
| [SRC-E73001D9AC-L000473](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L473) | 473 | `""` | — |
| [SRC-E73001D9AC-L000474](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L474) | 474 | `"## 10. تحقق الادعاءات وجودة المصادر"` | — |
| [SRC-E73001D9AC-L000475](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L475) | 475 | `"- المصدر الأولي الموثوق يفضّل عندما يناسب السؤال."` | — |
| [SRC-E73001D9AC-L000476](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L476) | 476 | `"- يراعى تاريخ النشر وتاريخ الحدث، خصوصًا في الأخبار والمعلومات المتغيرة."` | — |
| [SRC-E73001D9AC-L000477](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L477) | 477 | `"- أكثر من مصدر لا يعني تحققًا مستقلًا إذا كانت المصادر تنقل عن بعضها."` | — |
| [SRC-E73001D9AC-L000478](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L478) | 478 | `"- يراعى تعارض المصالح والمحتوى الآلي أو المكرر والنتائج المفبركة."` | — |
| [SRC-E73001D9AC-L000479](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L479) | 479 | `"- عند تعذر قراءة صفحة، لا يُنسب إليها محتوى لم يُفحص."` | — |
| [SRC-E73001D9AC-L000480](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L480) | 480 | `"- ينبغي أن يمكن تتبع كل ادعاء مهم إلى دليل أو وضعه كاستنتاج أو عدم يقين."` | — |
| [SRC-E73001D9AC-L000481](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L481) | 481 | `"- لا تُعرض درجة ثقة رقمية إلا بعد وجود منهج معاير وقياسات تدعمها؛ خلاف ذلك، يستخدم وصف نوعي واضح."` | — |
| [SRC-E73001D9AC-L000482](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L482) | 482 | `""` | — |
| [SRC-E73001D9AC-L000483](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L483) | 483 | `"## 11. التقييم والتحسين"` | — |
| [SRC-E73001D9AC-L000484](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L484) | 484 | `"- مجموعة اختبارات ثابتة للأسئلة العربية والفصحى والعامية والأخطاء الإملائية."` | — |
| [SRC-E73001D9AC-L000485](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L485) | 485 | `"- مجموعة أسئلة تتطلب بحثًا حديثًا وأخرى لا تحتاج إلى بحث."` | — |
| [SRC-E73001D9AC-L000486](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L486) | 486 | `"- حالات تعارض مصادر ومصادر قديمة وروابط ميتة ومعلومات ناقصة."` | — |
| [SRC-E73001D9AC-L000487](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L487) | 487 | `"- حالات prompt injection ومخرجات أدوات مشوهة وحالات timeout."` | — |
| [SRC-E73001D9AC-L000488](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L488) | 488 | `"- قياس صحة المصادر ودعم الادعاءات وتكامل الإجابة وسلامة الامتناع."` | — |
| [SRC-E73001D9AC-L000489](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L489) | 489 | `"- استخدام مراجعين بشريين للعينات المهمة عندما تسمح الموارد."` | — |
| [SRC-E73001D9AC-L000490](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L490) | 490 | `"- تتبع regression بين الإصدارات؛ التحسن في معيار واحد لا يبرر إهمال التدهور في الأمان أو السرعة."` | — |
| [SRC-E73001D9AC-L000491](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L491) | 491 | `"- عدم اعتبار تقييم نموذج لغوي واحد للحالة تقييمًا نهائيًا مستقلًا."` | — |
| [SRC-E73001D9AC-L000492](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L492) | 492 | `""` | — |
| [SRC-E73001D9AC-L000493](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L493) | 493 | `"---"` | — |
| [SRC-E73001D9AC-L000494](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L494) | 494 | `""` | — |
| [SRC-E73001D9AC-L000495](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L495) | 495 | `"# الجزء السابع — دورة التطوير والإصدارات"` | — |
| [SRC-E73001D9AC-L000496](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L496) | 496 | `""` | — |
| [SRC-E73001D9AC-L000497](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L497) | 497 | `"## 12. قواعد التطوير الآمن"` | — |
| [SRC-E73001D9AC-L000498](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L498) | 498 | `""` | — |
| [SRC-E73001D9AC-L000499](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L499) | 499 | `"- فحص حالة المستودع والفرع وHEAD قبل إجراء تعديل."` | — |
| [SRC-E73001D9AC-L000500](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L500) | 500 | `"- إنشاء فرع مستقل للتغيير، وتجنب الكتابة غير الضرورية إلى main."` | — |
| [SRC-E73001D9AC-L000501](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L501) | 501 | `"- جعل التعديل صغيرًا ومحدود الأثر متى أمكن."` | — |
| [SRC-E73001D9AC-L000502](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L502) | 502 | `"- إضافة اختبار يكشف العيب قبل أو مع إصلاحه."` | — |
| [SRC-E73001D9AC-L000503](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L503) | 503 | `"- تشغيل الفحوص ذات الصلة وتسجيل مخرجاتها الفعلية."` | — |
| [SRC-E73001D9AC-L000504](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L504) | 504 | `"- عدم الادعاء بأن الاختبارات نجحت إذا لم تُنفّذ أو لم تظهر نتيجتها."` | — |
| [SRC-E73001D9AC-L000505](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L505) | 505 | `"- مراجعة diff للتأكد من عدم وجود تغييرات جانبية."` | — |
| [SRC-E73001D9AC-L000506](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L506) | 506 | `"- تحديث التوثيق والأمثلة عندما تتغير الواجهات أو السلوك."` | — |
| [SRC-E73001D9AC-L000507](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L507) | 507 | `"- عدم دمج PR أو النشر النهائي دون تصريح صاحب المشروع."` | — |
| [SRC-E73001D9AC-L000508](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L508) | 508 | `"- حفظ النتائج برقم الالتزام والبيئة وأمر التشغيل."` | — |
| [SRC-E73001D9AC-L000509](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L509) | 509 | `""` | — |
| [SRC-E73001D9AC-L000510](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L510) | 510 | `"## 13. طبقات الاختبار المطلوبة"` | — |
| [SRC-E73001D9AC-L000511](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L511) | 511 | `""` | — |
| [SRC-E73001D9AC-L000512](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L512) | 512 | `"### T0 — فحوص محلية أساسية"` | — |
| [SRC-E73001D9AC-L000513](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L513) | 513 | `"تنسيق، lint، استيراد الوحدات، وفحوص النوع حيث تستخدم."` | — |
| [SRC-E73001D9AC-L000514](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L514) | 514 | `""` | — |
| [SRC-E73001D9AC-L000515](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L515) | 515 | `"### T1 — اختبارات الوحدة"` | — |
| [SRC-E73001D9AC-L000516](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L516) | 516 | `"التحقق من المنطق المحدد وحدود الإدخال والمخرجات والحالات الاستثنائية."` | — |
| [SRC-E73001D9AC-L000517](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L517) | 517 | `""` | — |
| [SRC-E73001D9AC-L000518](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L518) | 518 | `"### T2 — اختبارات العقود والتكامل"` | — |
| [SRC-E73001D9AC-L000519](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L519) | 519 | `"اختبار واجهات API ومخططات الأدوات وعقود موصلات البحث والنماذج."` | — |
| [SRC-E73001D9AC-L000520](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L520) | 520 | `""` | — |
| [SRC-E73001D9AC-L000521](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L521) | 521 | `"### T3 — اختبارات النظام من طرف إلى طرف"` | — |
| [SRC-E73001D9AC-L000522](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L522) | 522 | `"اختبار المسار الكامل للسؤال والبحث وتوليد الإجابة وعرض المصادر؛ باستخدام خدمات وهمية أو موفر اختباري حيث يناسب."` | — |
| [SRC-E73001D9AC-L000523](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L523) | 523 | `""` | — |
| [SRC-E73001D9AC-L000524](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L524) | 524 | `"### T4 — اختبارات التزامن والعزل"` | — |
| [SRC-E73001D9AC-L000525](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L525) | 525 | `"طلبات متزامنة ببيانات مختلفة، وإلغاء وtimeouts وأخطاء متداخلة، مع التأكد من عدم تسرب السياق."` | — |
| [SRC-E73001D9AC-L000526](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L526) | 526 | `""` | — |
| [SRC-E73001D9AC-L000527](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L527) | 527 | `"### T5 — اختبارات الأداء والحمل"` | — |
| [SRC-E73001D9AC-L000528](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L528) | 528 | `"حمل تدريجي، ذروة، زيادة مفاجئة، وتحمل مستمر. توثيق عدد العملاء ومعدل الوصول وزمن الاختبار وبيئة التنفيذ."` | — |
| [SRC-E73001D9AC-L000529](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L529) | 529 | `""` | — |
| [SRC-E73001D9AC-L000530](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L530) | 530 | `"### T6 — اختبارات الفشل والتعافي"` | — |
| [SRC-E73001D9AC-L000531](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L531) | 531 | `"تعطل موفر، تأخره، رد غير صالح، انقطاع شبكة، إعادة تشغيل عامل، نفاد حصة؛ والتحقق من التعافي وسلامة الحالة."` | — |
| [SRC-E73001D9AC-L000532](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L532) | 532 | `""` | — |
| [SRC-E73001D9AC-L000533](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L533) | 533 | `"### T7 — اختبارات الأمن والخصوصية"` | — |
| [SRC-E73001D9AC-L000534](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L534) | 534 | `"صلاحيات، جلسات، SSRF، حقن تعليمات، تسريب الأسرار، إساءة استخدام API، والتحقق من عدم اختلاط بيانات المستخدمين."` | — |
| [SRC-E73001D9AC-L000535](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L535) | 535 | `""` | — |
| [SRC-E73001D9AC-L000536](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L536) | 536 | `"### T8 — تقييم جودة الإجابة"` | — |
| [SRC-E73001D9AC-L000537](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L537) | 537 | `"صحة المصادر والاستشهادات، التغطية، وضوح عدم اليقين، والامتناع عند نقص الأدلة."` | — |
| [SRC-E73001D9AC-L000538](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L538) | 538 | `""` | — |
| [SRC-E73001D9AC-L000539](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L539) | 539 | `"لا يلزم تشغيل كل اختبار مكلف على كل تعديل صغير؛ لكن يجب أن تكون التغييرات ذات المخاطر العالية مرتبطة بمجموعة اختبار إلزامية، مع تشغيل اختبارات شاملة قبل إصدار إنتاجي."` | — |
| [SRC-E73001D9AC-L000540](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L540) | 540 | `""` | — |
| [SRC-E73001D9AC-L000541](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L541) | 541 | `"## 14. بوابات إصدار مقترحة"` | — |
| [SRC-E73001D9AC-L000542](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L542) | 542 | `"قبل وسم إصدار بأنه جاهز للإنتاج:"` | — |
| [SRC-E73001D9AC-L000543](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L543) | 543 | `"- نجاح الاختبارات الإلزامية المسجلة لهذا الإصدار."` | — |
| [SRC-E73001D9AC-L000544](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L544) | 544 | `"- عدم وجود ثغرات حرجة أو عالية غير معالجة دون استثناء مخاطر مكتوب ومقبول من المالك."` | — |
| [SRC-E73001D9AC-L000545](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L545) | 545 | `"- مراجعة الأسرار والاعتماديات وإعدادات النشر."` | — |
| [SRC-E73001D9AC-L000546](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L546) | 546 | `"- اختبارات دخان بعد النشر مع تمييز صحتها الفعلية عن فحص الإعدادات."` | — |
| [SRC-E73001D9AC-L000547](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L547) | 547 | `"- وجود خطة rollback واختبارها عندما يكون أثر النشر كبيرًا."` | — |
| [SRC-E73001D9AC-L000548](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L548) | 548 | `"- توثيق القيود المعروفة وحدود السعة والتحذيرات."` | — |
| [SRC-E73001D9AC-L000549](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L549) | 549 | `"- تفعيل المقاييس والتنبيهات الأساسية قبل استقبال حمل حقيقي."` | — |
| [SRC-E73001D9AC-L000550](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L550) | 550 | `""` | — |
| [SRC-E73001D9AC-L000551](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L551) | 551 | `"---"` | — |
| [SRC-E73001D9AC-L000552](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L552) | 552 | `""` | — |
| [SRC-E73001D9AC-L000553](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L553) | 553 | `"# الجزء الثامن — تشغيل الخدمة والتعافي"` | — |
| [SRC-E73001D9AC-L000554](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L554) | 554 | `""` | — |
| [SRC-E73001D9AC-L000555](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L555) | 555 | `"## 15. الجاهزية والتشخيص"` | — |
| [SRC-E73001D9AC-L000556](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L556) | 556 | ``"- `liveness`: هل العملية نفسها حية ويمكنها مواصلة العمل؟"`` | — |
| [SRC-E73001D9AC-L000557](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L557) | 557 | ``"- `readiness`: هل العملية جاهزة لقبول هذا النوع من الطلبات؟"`` | — |
| [SRC-E73001D9AC-L000558](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L558) | 558 | `"- حالة الموصل: إعداد موجود، اتصال فعلي ناجح، أو غير متاح."` | — |
| [SRC-E73001D9AC-L000559](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L559) | 559 | `"- حالة النموذج: إعداد، نجاح طلب تشخيص حي، أو فشل/عدم فحص."` | — |
| [SRC-E73001D9AC-L000560](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L560) | 560 | `"- يجب ألا تخلط نقطة health بين “المفتاح موجود” و“الخدمة تعمل الآن”."` | — |
| [SRC-E73001D9AC-L000561](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L561) | 561 | `"- يُذكر نطاق التحقق ووقت إجرائه والموصلات التي شملها."` | — |
| [SRC-E73001D9AC-L000562](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L562) | 562 | `"- endpoint التشخيص الذي ينفذ اتصالات خارجية يُحمى ويُحد معدل استدعائه."` | — |
| [SRC-E73001D9AC-L000563](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L563) | 563 | `""` | — |
| [SRC-E73001D9AC-L000564](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L564) | 564 | `"## 16. النسخ الاحتياطي والاستعادة"` | — |
| [SRC-E73001D9AC-L000565](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L565) | 565 | `"- تحديد البيانات التي تحتاج نسخًا احتياطيًا والبيانات التي لا ينبغي الاحتفاظ بها."` | — |
| [SRC-E73001D9AC-L000566](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L566) | 566 | `"- تحديد تواتر النسخ ومكانها وصلاحية الوصول إليها."` | — |
| [SRC-E73001D9AC-L000567](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L567) | 567 | `"- تشفير النسخ الحساسة إذا كانت خارج بيئة موثوقة."` | — |
| [SRC-E73001D9AC-L000568](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L568) | 568 | `"- منع نسخ الأسرار غير الضرورية في ملفات النسخ."` | — |
| [SRC-E73001D9AC-L000569](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L569) | 569 | `"- اختبار الاستعادة الفعلية دوريًا في بيئة معزولة."` | — |
| [SRC-E73001D9AC-L000570](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L570) | 570 | `"- تحديد هدف مقبول لفقدان البيانات (RPO) وزمن التعافي (RTO) عندما تتطلب الخدمة ذلك."` | — |
| [SRC-E73001D9AC-L000571](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L571) | 571 | `"- توثيق الخطوات اليدوية التي لا تزال ضرورية في مرحلة الاستضافة الحالية."` | — |
| [SRC-E73001D9AC-L000572](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L572) | 572 | `""` | — |
| [SRC-E73001D9AC-L000573](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L573) | 573 | `"## 17. خطة التدهور الآمن"` | — |
| [SRC-E73001D9AC-L000574](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L574) | 574 | `"عند الضغط أو تعطل خدمة خارجية، يجوز تقليل ميزات اختيارية بترتيب محدد، مثل:"` | — |
| [SRC-E73001D9AC-L000575](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L575) | 575 | `"1. إلغاء المراجعة الإضافية غير الضرورية."` | — |
| [SRC-E73001D9AC-L000576](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L576) | 576 | `"2. تقليل عدد استعلامات البحث ضمن حد يحافظ على الحد الأدنى للجودة."` | — |
| [SRC-E73001D9AC-L000577](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L577) | 577 | `"3. إيقاف موصل متدهور مؤقتًا بدائرة قاطع."` | — |
| [SRC-E73001D9AC-L000578](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L578) | 578 | `"4. إعادة إجابة جزئية موثقة بالحدود عند ملاءمتها."` | — |
| [SRC-E73001D9AC-L000579](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L579) | 579 | `"5. رفض الطلبات الجديدة المكلفة مؤقتًا مع رسالة صريحة."` | — |
| [SRC-E73001D9AC-L000580](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L580) | 580 | `""` | — |
| [SRC-E73001D9AC-L000581](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L581) | 581 | `"ولا يجوز بسبب الضغط تعطيل المصادقة أو حدود الصلاحيات أو التحقق من SSRF أو عزل بيانات المستخدمين."` | — |
| [SRC-E73001D9AC-L000582](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L582) | 582 | `""` | — |
| [SRC-E73001D9AC-L000583](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L583) | 583 | `"---"` | — |
| [SRC-E73001D9AC-L000584](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L584) | 584 | `""` | — |
| [SRC-E73001D9AC-L000585](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L585) | 585 | `"# الجزء التاسع — خارطة التنفيذ والاعتماد"` | — |
| [SRC-E73001D9AC-L000586](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L586) | 586 | `""` | — |
| [SRC-E73001D9AC-L000587](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L587) | 587 | `"## 18. ترتيب التنفيذ بحسب المخاطر والاعتماديات"` | — |
| [SRC-E73001D9AC-L000588](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L588) | 588 | `""` | — |
| [SRC-E73001D9AC-L000589](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L589) | 589 | `"**المرحلة A — جرد مثبت للحالة الحالية**"` | — |
| [SRC-E73001D9AC-L000590](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L590) | 590 | `"- تسجيل HEAD والفرع وبيئة التشغيل واعتماديات المشروع."` | — |
| [SRC-E73001D9AC-L000591](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L591) | 591 | `"- رسم دورة الطلب الحقيقية من API حتى البحث والنموذج والإجابة."` | — |
| [SRC-E73001D9AC-L000592](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L592) | 592 | `"- فهرسة نقاط الاتصال الخارجية والأدوات والبيانات الحساسة."` | — |
| [SRC-E73001D9AC-L000593](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L593) | 593 | `"- قراءة الاختبارات وتشغيلها وتسجيل النتائج؛ لا افتراض نجاحها."` | — |
| [SRC-E73001D9AC-L000594](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L594) | 594 | `"- تقرير فجوات يوسم كل نتيجة VERIFIED أو INFERRED أو PROPOSED أو UNKNOWN."` | — |
| [SRC-E73001D9AC-L000595](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L595) | 595 | `""` | — |
| [SRC-E73001D9AC-L000596](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L596) | 596 | `"**المرحلة B — حماية الأساس**"` | — |
| [SRC-E73001D9AC-L000597](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L597) | 597 | `"- عزل سياق الطلبات والذاكرة."` | — |
| [SRC-E73001D9AC-L000598](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L598) | 598 | `"- حدود الإدخال والوقت والعدد والحجم والتزامن."` | — |
| [SRC-E73001D9AC-L000599](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L599) | 599 | `"- تحقق من صلاحيات الواجهات والعمليات الحساسة."` | — |
| [SRC-E73001D9AC-L000600](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L600) | 600 | `"- مراجعة SSRF والتحويلات وDNS وأحجام الاستجابات."` | — |
| [SRC-E73001D9AC-L000601](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L601) | 601 | `"- حماية الأسرار والسجلات وواجهات التشخيص."` | — |
| [SRC-E73001D9AC-L000602](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L602) | 602 | `"- اختبارات regression لكل عيب يُصلح."` | — |
| [SRC-E73001D9AC-L000603](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L603) | 603 | `""` | — |
| [SRC-E73001D9AC-L000604](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L604) | 604 | `"**المرحلة C — مقاومة التعطل**"` | — |
| [SRC-E73001D9AC-L000605](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L605) | 605 | `"- timeouts وcancellation وretry محدود وcircuit breaker."` | — |
| [SRC-E73001D9AC-L000606](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L606) | 606 | `"- حدود التزامن والضغط والطوابير عند الحاجة."` | — |
| [SRC-E73001D9AC-L000607](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L607) | 607 | `"- سلوك واضح للموفر المتعطل."` | — |
| [SRC-E73001D9AC-L000608](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L608) | 608 | `"- اختبارات failure injection وإعادة التشغيل."` | — |
| [SRC-E73001D9AC-L000609](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L609) | 609 | `""` | — |
| [SRC-E73001D9AC-L000610](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L610) | 610 | `"**المرحلة D — القياس والأداء**"` | — |
| [SRC-E73001D9AC-L000611](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L611) | 611 | `"- إنشاء خط أساس لزمن الاستجابة والموارد وجودة النتائج."` | — |
| [SRC-E73001D9AC-L000612](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L612) | 612 | `"- إزالة التكرار وتحسين الاستعلامات والمسارات."` | — |
| [SRC-E73001D9AC-L000613](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L613) | 613 | `"- اختبارات التزامن والحمل تحت البيئة المتاحة."` | — |
| [SRC-E73001D9AC-L000614](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L614) | 614 | `"- اعتماد حدود سعة واقعية موثقة."` | — |
| [SRC-E73001D9AC-L000615](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L615) | 615 | `""` | — |
| [SRC-E73001D9AC-L000616](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L616) | 616 | `"**المرحلة E — صلابة المعرفة**"` | — |
| [SRC-E73001D9AC-L000617](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L617) | 617 | `"- قياس إسناد الادعاءات للمصادر."` | — |
| [SRC-E73001D9AC-L000618](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L618) | 618 | `"- اختبارات التواريخ والتعارض والروابط الميتة وحقن التعليمات."` | — |
| [SRC-E73001D9AC-L000619](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L619) | 619 | `"- سياسة واضحة لعدم اليقين والإجابات الجزئية."` | — |
| [SRC-E73001D9AC-L000620](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L620) | 620 | `"- مجموعة regression عربية ثابتة."` | — |
| [SRC-E73001D9AC-L000621](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L621) | 621 | `""` | — |
| [SRC-E73001D9AC-L000622](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L622) | 622 | `"**المرحلة F — الاستعداد التشغيلي**"` | — |
| [SRC-E73001D9AC-L000623](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L623) | 623 | `"- مراقبة وتنبيهات وسجلات منقحة."` | — |
| [SRC-E73001D9AC-L000624](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L624) | 624 | `"- نسخ احتياطي واستعادة عند الحاجة."` | — |
| [SRC-E73001D9AC-L000625](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L625) | 625 | `"- خطة rollback وحوادث."` | — |
| [SRC-E73001D9AC-L000626](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L626) | 626 | `"- مستند نشر يوضح الأسرار والبيئة والفحوص والقيود."` | — |
| [SRC-E73001D9AC-L000627](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L627) | 627 | `""` | — |
| [SRC-E73001D9AC-L000628](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L628) | 628 | `"**المرحلة G — التوسع**"` | — |
| [SRC-E73001D9AC-L000629](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L629) | 629 | `"- الانتقال من عملية واحدة إلى عمال أو طوابير أو نسخ أفقية فقط عندما تثبت القياسات الحاجة والجدوى."` | — |
| [SRC-E73001D9AC-L000630](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L630) | 630 | `"- ترحيل التخزين عند بلوغ حدود الأداء أو التوافر الموثقة."` | — |
| [SRC-E73001D9AC-L000631](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L631) | 631 | `"- إعادة اختبارات السعة والأمن بعد كل تغير معماري مؤثر."` | — |
| [SRC-E73001D9AC-L000632](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L632) | 632 | `""` | — |
| [SRC-E73001D9AC-L000633](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L633) | 633 | `"كل مرحلة لها معايير دخول وخروج وأدلة، ولا تُعد منجزة بمجرد كتابة خطة لها."` | — |
| [SRC-E73001D9AC-L000634](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L634) | 634 | `""` | — |
| [SRC-E73001D9AC-L000635](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L635) | 635 | `"---"` | — |
| [SRC-E73001D9AC-L000636](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L636) | 636 | `""` | — |
| [SRC-E73001D9AC-L000637](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L637) | 637 | `""` | — |
| [SRC-E73001D9AC-L000638](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L638) | 638 | `"### ترتيب توسيع القدرات والمهارات والوكلاء"` | — |
| [SRC-E73001D9AC-L000639](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L639) | 639 | `""` | — |
| [SRC-E73001D9AC-L000640](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L640) | 640 | `"المراحل A–G أعلاه تغطي الجرد والحماية والاعتمادية والقياس والمعرفة والاستعداد التشغيلي والتوسع. وداخل هذه المراحل، يكون ترتيب بناء قدرات الذكاء الاصطناعي هو: (1) إثبات الحالة والاختبارات، (2) عقود الأدوات وفرض الصلاحيات، (3) المهارات وسير العمل، (4) مواصفات المهام والتركيب المحدود من العناصر المعتمدة، (5) تقييم الحاجة إلى Meta-Agent يولد مسودات فقط، (6) دراسة توليد الكود كقرار مستقبلي اختياري. هذا ترتيب متخصص يكمّل المراحل ولا يلغيها أو يستبدل متطلبات الأمن والتشغيل."` | — |
| [SRC-E73001D9AC-L000641](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L641) | 641 | `""` | — |
| [SRC-E73001D9AC-L000642](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L642) | 642 | `"**بوابة التوسع:** لا ننتقل إلى إنشاء الوكلاء لمجرد انتهاء المرحلة السابقة؛ يلزم دليل على حاجة لا تغطيها المهارات وسير العمل بصورة مناسبة، ومقارنة مفيدة في الجودة والكلفة والصيانة والمخاطر. لا يثبت نجاح الاختبارات التي كتبها النموذج لنفسه أمان التنفيذ، ولا تُفعل قدرة جديدة دون مراجعة مستقلة مناسبة وموافقة بشرية عند اللزوم."` | — |
| [SRC-E73001D9AC-L000643](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L643) | 643 | `""` | — |
| [SRC-E73001D9AC-L000644](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L644) | 644 | `"التفصيل المرجعي وبوابات قبول كل مرحلة وارد في [المعمارية الحاكمة للقدرات والمهارات وسير العمل والوكلاء](OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md)."` | — |
| [SRC-E73001D9AC-L000645](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L645) | 645 | `""` | — |
| [SRC-E73001D9AC-L000646](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L646) | 646 | `"---"` | — |
| [SRC-E73001D9AC-L000647](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L647) | 647 | `""` | — |
| [SRC-E73001D9AC-L000648](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L648) | 648 | `"# الجزء العاشر — معمارية التوسع والتطوير المستمر"` | — |
| [SRC-E73001D9AC-L000649](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L649) | 649 | `""` | — |
| [SRC-E73001D9AC-L000650](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L650) | 650 | `"هذا الجزء متطلب تأسيسي مستقل. الغرض ليس توقع كل ميزة مستقبلية، بل بناء نظام يمكنه استيعاب التغيير بأقل كلفة ومخاطر ممكنة، مع الحفاظ على التوافق والأمان والموثوقية."` | — |
| [SRC-E73001D9AC-L000651](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L651) | 651 | `""` | — |
| [SRC-E73001D9AC-L000652](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L652) | 652 | `"## 19. النتيجة المعمارية المستهدفة"` | — |
| [SRC-E73001D9AC-L000653](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L653) | 653 | `""` | — |
| [SRC-E73001D9AC-L000654](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L654) | 654 | `"يجب أن تسمح معمارية Omarai، وفق الأدلة والموارد المتاحة، بما يلي:"` | — |
| [SRC-E73001D9AC-L000655](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L655) | 655 | `""` | — |
| [SRC-E73001D9AC-L000656](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L656) | 656 | `"- إضافة قدرات وخدمات ووكلاء وأدوات ومصادر بيانات دون إعادة كتابة النواة بالكامل."` | — |
| [SRC-E73001D9AC-L000657](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L657) | 657 | `"- رفع السعة تدريجيًا عبر تحسين المكونات، ثم زيادة الموارد، ثم إضافة عمليات أو نسخ خدمة، ثم فصل مكونات محددة عند ثبوت الحاجة."` | — |
| [SRC-E73001D9AC-L000658](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L658) | 658 | `"- تبديل موفر بحث أو نموذج أو تخزين من خلال واجهات وعقود معرفة، دون انتشار تفاصيل المورد في منطق الأعمال."` | — |
| [SRC-E73001D9AC-L000659](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L659) | 659 | `"- إصدار تغييرات للنواة والواجهة وواجهات API ومخططات البيانات بطريقة قابلة للاختبار والتراجع."` | — |
| [SRC-E73001D9AC-L000660](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L660) | 660 | `"- اختبار كل مكوّن في عزلة نسبية، واختبار الرحلات الكاملة للتأكد من التوافق."` | — |
| [SRC-E73001D9AC-L000661](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L661) | 661 | `"- ترحيل البيانات القديمة والحفاظ على سلامتها، وعدم افتراض إمكانية مسح التخزين وإعادة إنشائه في بيئة الإنتاج."` | — |
| [SRC-E73001D9AC-L000662](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L662) | 662 | `"- الحفاظ على صلاحيات واضحة وحدود ثقة عند إضافة الأدوات أو الوكلاء أو العمال."` | — |
| [SRC-E73001D9AC-L000663](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L663) | 663 | `"- اكتشاف التعقيد المعماري والاعتماديات الدائرية وتراكم الديون التقنية قبل أن تعيق التطوير."` | — |
| [SRC-E73001D9AC-L000664](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L664) | 664 | `""` | — |
| [SRC-E73001D9AC-L000665](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L665) | 665 | `"**مبدأ التصميم:** نخطط لقابلية التوسع والتغيير، ونؤجل التعقيد غير الضروري. قابلية التوسع ليست مرادفًا للخدمات المصغّرة، ولا يتطلب التطوير طويل الأمد تحويل كل وحدة برمجية إلى خدمة مستقلة."` | — |
| [SRC-E73001D9AC-L000666](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L666) | 666 | `""` | — |
| [SRC-E73001D9AC-L000667](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L667) | 667 | `"يُفهم التوسع في القدرات وفق التسلسل الحاكم: أدوات ذات عقود وصلاحيات ← مهارات قابلة لإعادة الاستخدام ← سير عمل قابل للاختبار ← تركيب مهام محدود ← وكلاء عند ثبوت الحاجة. لا يلزم إنشاء وكيل أو خدمة مستقلة لكل اختصاص. انظر [المعمارية الحاكمة للقدرات والمهارات وسير العمل والوكلاء](OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md) للتعاريف وبوابات الانتقال."` | — |
| [SRC-E73001D9AC-L000668](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L668) | 668 | `""` | — |
| [SRC-E73001D9AC-L000669](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L669) | 669 | `"## 20. نمط البداية: Modular Monolith بحدود واضحة"` | — |
| [SRC-E73001D9AC-L000670](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L670) | 670 | `""` | — |
| [SRC-E73001D9AC-L000671](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L671) | 671 | `"**الاختيار الافتراضي المقترح:** تطبيق منظم من نوع Modular Monolith عندما يناسب حجم المشروع وبيئة الاستضافة. يعني ذلك إمكان تشغيل التطبيق كوحدة نشر واحدة، مع فصل الوحدات منطقيًا ومنع تشابك مسؤولياتها."` | — |
| [SRC-E73001D9AC-L000672](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L672) | 672 | `""` | — |
| [SRC-E73001D9AC-L000673](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L673) | 673 | `"يجب أن تكون لكل وحدة:"` | — |
| [SRC-E73001D9AC-L000674](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L674) | 674 | `"- مسؤولية محددة ومحدودات ملكية واضحة."` | — |
| [SRC-E73001D9AC-L000675](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L675) | 675 | `"- واجهة عامة صغيرة ومعلومة؛ وتظل تفاصيل التنفيذ داخل الوحدة."` | — |
| [SRC-E73001D9AC-L000676](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L676) | 676 | `"- مدخلات ومخرجات قابلة للتحقق بعقود محددة."` | — |
| [SRC-E73001D9AC-L000677](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L677) | 677 | `"- اختبارات وحدة وعقود تغطي واجهاتها."` | — |
| [SRC-E73001D9AC-L000678](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L678) | 678 | `"- ملكية واضحة للبيانات التي تنشئها أو تعدلها."` | — |
| [SRC-E73001D9AC-L000679](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L679) | 679 | `"- حدود صلاحيات وموارد مناسبة لطبيعة عملها."` | — |
| [SRC-E73001D9AC-L000680](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L680) | 680 | `"- سجل اعتماديات يمنع إنشاء دورات اعتماد غير مقصودة."` | — |
| [SRC-E73001D9AC-L000681](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L681) | 681 | `""` | — |
| [SRC-E73001D9AC-L000682](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L682) | 682 | `"لا يجوز لوحدة أن تستورد التفاصيل الداخلية لوحدة أخرى أو تعدل مخازنها مباشرة بصورة تتجاوز العقد المتفق عليه. يمكن السماح باستثناءات محددة ومبررة، لكن يجب تسجيلها ومراجعتها."` | — |
| [SRC-E73001D9AC-L000683](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L683) | 683 | `""` | — |
| [SRC-E73001D9AC-L000684](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L684) | 684 | `"### متى نفصل الوحدة إلى خدمة مستقلة؟"` | — |
| [SRC-E73001D9AC-L000685](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L685) | 685 | `""` | — |
| [SRC-E73001D9AC-L000686](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L686) | 686 | `"لا يتم التفكيك لمجرد اتباع موضة معمارية. يُدرس فصل الوحدة عندما يتوفر واحد أو أكثر من الأدلة التالية:"` | — |
| [SRC-E73001D9AC-L000687](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L687) | 687 | `"- احتياج توسع مستقل واضح لا يمكن خدمته بكفاءة داخل التطبيق الحالي."` | — |
| [SRC-E73001D9AC-L000688](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L688) | 688 | `"- متطلبات عزل أمني أو صلاحيات أو موارد تختلف جذريًا عن بقية النظام."` | — |
| [SRC-E73001D9AC-L000689](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L689) | 689 | `"- اختلاف موثق في دورة النشر أو التوافر أو قيود التشغيل."` | — |
| [SRC-E73001D9AC-L000690](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L690) | 690 | `"- اختناق مقاس في الأداء أو حدود عملية تمنع التوسع المطلوب."` | — |
| [SRC-E73001D9AC-L000691](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L691) | 691 | `"- حاجة إلى فريق أو نطاق ملكية مستقل مع عقود تشغيلية واضحة."` | — |
| [SRC-E73001D9AC-L000692](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L692) | 692 | `""` | — |
| [SRC-E73001D9AC-L000693](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L693) | 693 | `"قبل الفصل، تُوثق كلفة الشبكات والكمون، وفشل الاتصال، والمصادقة بين الخدمات، والمراقبة، والنشر والتراجع، والتناسق والاتساق، والاختبارات الإضافية. إذا لم تفوق الفائدة هذه التكاليف، تبقى الوحدة داخل التطبيق معزولة منطقيًا."` | — |
| [SRC-E73001D9AC-L000694](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L694) | 694 | `""` | — |
| [SRC-E73001D9AC-L000695](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L695) | 695 | `"## 21. حدود المجال والواجهات (Domain Boundaries, Ports & Adapters)"` | — |
| [SRC-E73001D9AC-L000696](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L696) | 696 | `""` | — |
| [SRC-E73001D9AC-L000697](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L697) | 697 | `"تُحدد المجالات المنطقية بما يلائم الكود الحقيقي، وقد تشمل: واجهات الطلبات، والهوية والصلاحيات، وتنسيق المهام، والتخطيط، والبحث، وجلب الصفحات، وتنفيذ الأدوات، وتجميع الأدلة، والتحقق من الإجابات، والذاكرة والتخزين، والمراقبة."` | — |
| [SRC-E73001D9AC-L000698](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L698) | 698 | `""` | — |
| [SRC-E73001D9AC-L000699](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L699) | 699 | `"هذه قائمة مجالات محتملة وليست إلزامًا بإنشاء وحدة منفصلة لكل اسم. يتم تحديد الحدود بعد فحص تدفق البيانات والاعتماديات الفعلية."` | — |
| [SRC-E73001D9AC-L000700](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L700) | 700 | `""` | — |
| [SRC-E73001D9AC-L000701](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L701) | 701 | `"- تعتمد قواعد الأعمال على واجهات داخلية مستقرة، لا على مكتبة مورد خارجي بشكل مباشر."` | — |
| [SRC-E73001D9AC-L000702](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L702) | 702 | `"- توضع تفاصيل HTTP وSDK الخاص بالمورد وعمليات التحويل داخل Adapter مناسب."` | — |
| [SRC-E73001D9AC-L000703](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L703) | 703 | `"- تعرف العقود سلوك النجاح والفشل والمهلة والإلغاء وحدود الحجم وإعادة المحاولة."` | — |
| [SRC-E73001D9AC-L000704](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L704) | 704 | `"- تعزل صيغة رد موفر معين عن بقية النواة عبر تحويل صريح واختبارات للعقد."` | — |
| [SRC-E73001D9AC-L000705](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L705) | 705 | `"- لا تتسلل بيانات الاعتماد أو أسرار المورد إلى النماذج أو الواجهة أو سجلات المجال."` | — |
| [SRC-E73001D9AC-L000706](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L706) | 706 | `"- تُمنع الدورات بين الوحدات باستخدام اتجاه اعتماد واضح أو واجهات مشتركة صغيرة ومملوكة بوضوح."` | — |
| [SRC-E73001D9AC-L000707](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L707) | 707 | `"- لا تنشأ طبقة تجريد عامة إلا عندما توجد حاجة واقعية أو أكثر من تنفيذ حقيقي أو فائدة واضحة في الاختبار؛ لا نبني إطارات عمل داخلية ضخمة للتوقع فقط."` | — |
| [SRC-E73001D9AC-L000708](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L708) | 708 | `""` | — |
| [SRC-E73001D9AC-L000709](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L709) | 709 | `"## 22. عقود الأدوات والقدرات والمهارات وسير العمل والوكلاء والإضافات"` | — |
| [SRC-E73001D9AC-L000710](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L710) | 710 | `""` | — |
| [SRC-E73001D9AC-L000711](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L711) | 711 | `"أي مكوّن جديد يجب أن يلتزم بعقد تسجيل واضح، لكن لا يُعامل كل نوع مكوّن باعتباره شيئًا واحدًا. يُستخدم التفريق التالي مع [المعمارية الحاكمة للقدرات والمهارات وسير العمل والوكلاء](OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md):"` | — |
| [SRC-E73001D9AC-L000712](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L712) | 712 | `""` | — |
| [SRC-E73001D9AC-L000713](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L713) | 713 | `"- **Tool / الأداة:** عملية أو موصل بمدخلات ومخرجات وأخطاء وحدود معروفة."` | — |
| [SRC-E73001D9AC-L000714](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L714) | 714 | `"- **Capability / القدرة:** إذن محدد النطاق لتنفيذ نوع من الأفعال؛ لا تمنحها رسالة النموذج أو ملف التعريف لنفسه."` | — |
| [SRC-E73001D9AC-L000715](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L715) | 715 | `"- **Skill / المهارة:** وحدة قابلة لإعادة الاستخدام تجمع غرضًا ومدخلات ومخرجات وقدرات معتمدة ومعايير نجاح واختبارات."` | — |
| [SRC-E73001D9AC-L000716](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L716) | 716 | `"- **Workflow / سير العمل:** خطوات وانتقالات وحدود توقف وميزانيات محددة؛ يمكنه استدعاء مهارات وأدوات، لكنه لا يوسع الصلاحيات."` | — |
| [SRC-E73001D9AC-L000717](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L717) | 717 | `"- **Agent Profile / ملف تعريف الوكيل:** وصفة معلنة تحدد الهدف والمهارات والإصدارات والقيود وسياسة الذاكرة؛ ليست كودًا تنفيذيًا حرًا."` | — |
| [SRC-E73001D9AC-L000718](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L718) | 718 | `"- **Agent / الوكيل:** سياق تنفيذ يركب هدفًا ومهارات وأدوات ضمن السياسة؛ لا يُفترض أنه دائم أو مستقل عن ضوابط المنصة."` | — |
| [SRC-E73001D9AC-L000719](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L719) | 719 | `"- **Plugin / الإضافة:** مكون خارجي أو حزمة طرف ثالث، تؤجل إلى حين تبرير الحاجة ومراجعة المصدر وسلسلة التوريد والعزل."` | — |
| [SRC-E73001D9AC-L000720](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L720) | 720 | `""` | — |
| [SRC-E73001D9AC-L000721](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L721) | 721 | `"يتضمن عقد الأداة، بحسب الحاجة:"` | — |
| [SRC-E73001D9AC-L000722](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L722) | 722 | `"- معرفًا ثابتًا واسمًا ووصفًا وإصدارًا ومالكًا."` | — |
| [SRC-E73001D9AC-L000723](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L723) | 723 | `"- مخطط input/output صارمًا وحدودًا للأحجام والأنواع."` | — |
| [SRC-E73001D9AC-L000724](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L724) | 724 | `"- متطلبات الصلاحيات والهوية ونطاق البيانات."` | — |
| [SRC-E73001D9AC-L000725](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L725) | 725 | `"- تصنيف المخاطر: قراءة عامة، قراءة خاصة، كتابة داخلية، أو أثر خارجي حساس."` | — |
| [SRC-E73001D9AC-L000726](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L726) | 726 | `"- timeout وbudget وconcurrency limit وسياسة إلغاء."` | — |
| [SRC-E73001D9AC-L000727](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L727) | 727 | `"- سياسة retries وidempotency إن كان لها أثر متكرر."` | — |
| [SRC-E73001D9AC-L000728](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L728) | 728 | `"- تصنيفًا للأخطاء: خطأ مدخلات، رفض صلاحية، حد موارد، timeout، تعطل موفر، أو فشل داخلي."` | — |
| [SRC-E73001D9AC-L000729](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L729) | 729 | `"- شروط فحص الصحة ومعنى نتيجة الفحص وحدودها الزمنية."` | — |
| [SRC-E73001D9AC-L000730](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L730) | 730 | `"- اختبارات إيجابية وسلبية واختبارات انقطاع/بطء/ردود غير صالحة."` | — |
| [SRC-E73001D9AC-L000731](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L731) | 731 | `"- طريقة تعطيل أو إيقاف الأداة دون إيقاف غيرها متى أمكن."` | — |
| [SRC-E73001D9AC-L000732](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L732) | 732 | `"- سياسة سجلات لا تكشف الأسرار أو بيانات المستخدم غير الضرورية."` | — |
| [SRC-E73001D9AC-L000733](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L733) | 733 | `""` | — |
| [SRC-E73001D9AC-L000734](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L734) | 734 | `"ويجب أن تتضمن عقود المهارات وسير العمل، بالقدر المناسب:"` | — |
| [SRC-E73001D9AC-L000735](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L735) | 735 | `"- المدخلات والمخرجات ومعايير النجاح والفشل."` | — |
| [SRC-E73001D9AC-L000736](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L736) | 736 | `"- الأدوات والمهارات التابعة مع إصداراتها المسموح بها."` | — |
| [SRC-E73001D9AC-L000737](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L737) | 737 | `"- صلاحيات وميزانية وحدود خطوات واضحة."` | — |
| [SRC-E73001D9AC-L000738](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L738) | 738 | `"- اختبارات عربية، واختبارات فشل، واختبارات عدم تجاوز الصلاحيات."` | — |
| [SRC-E73001D9AC-L000739](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L739) | 739 | `"- حالة الاعتماد وسجل تغييرات يمكن تتبعه."` | — |
| [SRC-E73001D9AC-L000740](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L740) | 740 | `""` | — |
| [SRC-E73001D9AC-L000741](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L741) | 741 | `"تُفرض الصلاحيات عند التنفيذ، ولا يثبت التحقق من المخطط أن السلوك آمن أو صحيح. وتظل الإضافات معطلة افتراضيًا حتى اكتمال إعداداتها وفحوصها. لا يملك أي Plugin أو Agent أو Skill حق منح نفسه صلاحيات جديدة، أو تجاوز ميزانية الطلب، أو تعديل سياسات الأمان. لا يسمح بالتنفيذ الديناميكي لكود قادم من المستخدم أو النموذج دون قرار مستقل ومراجعة وعزل واختبارات أمنية ملائمة."` | — |
| [SRC-E73001D9AC-L000742](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L742) | 742 | `""` | — |
| [SRC-E73001D9AC-L000743](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L743) | 743 | `"**الترتيب الافتراضي للتوسع:** أصلح واثبت النواة الحالية أولًا، ثم وحّد عقود الأدوات والصلاحيات، ثم نظّم القدرات المتكررة كمهارات، ثم المسارات متعددة الخطوات كسير عمل. لا يُنشأ مصنع وكلاء أو Meta-Agent إلا عندما تثبت الحاجة والفائدة بالقياس. وعند إنشائه، يقتصر دوره الأولي على مسودات التعريفات؛ ولا يكتب كودًا تنفيذيًا أو يعتمد نفسه أو يفعل تعريفًا دون المرور ببوابات التحقق والموافقة."` | — |
| [SRC-E73001D9AC-L000744](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L744) | 744 | `""` | — |
| [SRC-E73001D9AC-L000745](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L745) | 745 | `"يُحافظ على سلوك الوظائف الحالية أثناء استخراج المهارات أو سير العمل، ويجب توفير اختبارات regression قبل اعتماد التغيير. لا نعيد كتابة المكونات القائمة لمجرد نقلها إلى أسماء معمارية جديدة."` | — |
| [SRC-E73001D9AC-L000746](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L746) | 746 | `" "` | — |
| [SRC-E73001D9AC-L000747](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L747) | 747 | `"## 23. إصدار واجهات API وعقود الرسائل"` | — |
| [SRC-E73001D9AC-L000748](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L748) | 748 | `""` | — |
| [SRC-E73001D9AC-L000749](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L749) | 749 | `"- تُوثق الواجهات العامة بعقود ومخططات قابلة للمراجعة، ويفضل توليد أو اختبار المخططات من مصدر واحد للحقيقة عندما يكون ذلك عمليًا."` | — |
| [SRC-E73001D9AC-L000750](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L750) | 750 | `"- الإضافات المتوافقة، مثل حقول اختيارية جديدة لا تغير المعنى، تُفضّل على تغييرات تكسر العملاء."` | — |
| [SRC-E73001D9AC-L000751](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L751) | 751 | `"- أي تغيير غير متوافق يتطلب إصدارًا أو مسار ترحيل واضحًا وفترة انتقال مناسبة."` | — |
| [SRC-E73001D9AC-L000752](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L752) | 752 | `"- لا يُحذف حقل أو يغير معناه بصمت، ولا تتحول قيمة اختيارية إلى إلزامية دون خطة."` | — |
| [SRC-E73001D9AC-L000753](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L753) | 753 | `"- يستخدم التحقق في جهة الخادم حتى عندما يتحقق العميل من نفس المخطط."` | — |
| [SRC-E73001D9AC-L000754](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L754) | 754 | `"- تُختبر العقود بأمثلة صحيحة وخاطئة وحدود وأحجام قصوى وحالات إصدار قديم."` | — |
| [SRC-E73001D9AC-L000755](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L755) | 755 | `"- عند استخدام أحداث أو رسائل طوابير، تتضمن الرسالة نوع الحدث وإصداره ومعرف تتبع وبيانات لازمة فقط، ولا تتضمن أسرارًا."` | — |
| [SRC-E73001D9AC-L000756](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L756) | 756 | `"- يجب تحمل الرسائل المكررة أو الخارجة عن الترتيب إذا كان وسيط الرسائل أو طبيعة النظام يسمحان بذلك؛ لا يُفترض تنفيذ الرسالة مرة واحدة فقط دون ضمان."` | — |
| [SRC-E73001D9AC-L000757](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L757) | 757 | `"- لا يوعد بالتوافق العكسي إلا ضمن نطاق إصدار وخطة دعم معلومة."` | — |
| [SRC-E73001D9AC-L000758](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L758) | 758 | `""` | — |
| [SRC-E73001D9AC-L000759](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L759) | 759 | `"## 24. تطور مخططات البيانات والترحيلات"` | — |
| [SRC-E73001D9AC-L000760](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L760) | 760 | `""` | — |
| [SRC-E73001D9AC-L000761](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L761) | 761 | `"يجب أن يتعامل التطوير مع البيانات على أنها أصل مستمر، لا مخزن يمكن إعادة بنائه بلا عواقب."` | — |
| [SRC-E73001D9AC-L000762](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L762) | 762 | `""` | — |
| [SRC-E73001D9AC-L000763](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L763) | 763 | `"- كل تغيير بنيوي في البيانات له ترحيل (migration) محدد وقابل للاختبار."` | — |
| [SRC-E73001D9AC-L000764](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L764) | 764 | `"- فحص أثر الترحيل على البيانات القديمة والفهارس والتنافس والقفل وزمن التوقف."` | — |
| [SRC-E73001D9AC-L000765](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L765) | 765 | `"- تفضيل نمط expand–migrate–contract عند الحاجة إلى تغيير متوافق تدريجيًا: إضافة ما يلزم أولًا، ثم نقل البيانات وقراءة/كتابة متوافقة خلال فترة الانتقال، ثم إزالة البنية القديمة بعد إثبات الاستخدام وعدم الحاجة."` | — |
| [SRC-E73001D9AC-L000766](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L766) | 766 | `"- حفظ نسخة احتياطية صالحة قبل التغييرات الخطرة عندما تنطبق الحاجة، مع اختبار استعادة لا مجرد وجود الملف."` | — |
| [SRC-E73001D9AC-L000767](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L767) | 767 | `"- منع ترحيل هدّام لا رجعة فيه دون تحذير صريح وموافقة وخطة استعادة مناسبة."` | — |
| [SRC-E73001D9AC-L000768](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L768) | 768 | `"- تضمين اختبارات للبيانات القديمة والناقصة وغير المتوقعة والتكرارات وفشل المعاملة."` | — |
| [SRC-E73001D9AC-L000769](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L769) | 769 | `"- تعريف ملكية كل جدول أو مساحة بيانات، وسياسات الحذف والاحتفاظ والخصوصية."` | — |
| [SRC-E73001D9AC-L000770](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L770) | 770 | `"- قياس حجم البيانات ومعدل الكتابة ومشكلات القفل قبل اختيار التوسع أو نقل التخزين."` | — |
| [SRC-E73001D9AC-L000771](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L771) | 771 | `"- لا تتحول قاعدة محلية إلى قاعدة موزعة لمجرد توقع نمو غير مقاس؛ يُوثق معيار الانتقال بناءً على الاستخدام الفعلي."` | — |
| [SRC-E73001D9AC-L000772](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L772) | 772 | `""` | — |
| [SRC-E73001D9AC-L000773](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L773) | 773 | `"## 25. حالة الطلب والتوزيع والتوسع الأفقي"` | — |
| [SRC-E73001D9AC-L000774](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L774) | 774 | `""` | — |
| [SRC-E73001D9AC-L000775](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L775) | 775 | `"لتشغيل عدة نسخ من Omarai، ينبغي تجنب افتراض أن ذاكرة عملية واحدة هي مصدر الحالة الوحيد."` | — |
| [SRC-E73001D9AC-L000776](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L776) | 776 | `""` | — |
| [SRC-E73001D9AC-L000777](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L777) | 777 | `"- تصنف الحالة إلى: حالة قصيرة العمر داخل الطلب، وحالة دائمة للمستخدم، وحالة مهام طويلة، وcache قابل لإعادة البناء."` | — |
| [SRC-E73001D9AC-L000778](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L778) | 778 | `"- الحالة داخل الطلب تظل محلية ما دام الطلب داخل العملية؛ أما ما يجب أن يعيش بعد إعادة التشغيل أو ينتقل بين النسخ فيحتاج تخزينًا أو وسيطًا مناسبًا."` | — |
| [SRC-E73001D9AC-L000779](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L779) | 779 | `"- لا تحفظ المحادثة أو صلاحيات المستخدم في متغير عالمي قابل للتغيير مشترك بين الطلبات."` | — |
| [SRC-E73001D9AC-L000780](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L780) | 780 | `"- مفاتيح الحالة وcache تراعي نطاق المستخدم أو المستأجر، ونوع البيانات، وإصدار المخطط، ومدة الصلاحية."` | — |
| [SRC-E73001D9AC-L000781](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L781) | 781 | `"- لا يعتمد توجيه الطلبات على sticky sessions إلا بقرار مبرر مع خطة للتعطل؛ يُفضّل وضوح مكان الحالة وإمكانية استعادتها."` | — |
| [SRC-E73001D9AC-L000782](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L782) | 782 | `"- استخدام idempotency وسجل حالات واضح عند وجود مهام قد يعاد تسليمها."` | — |
| [SRC-E73001D9AC-L000783](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L783) | 783 | `"- يجب أن تتحمل المهام الطويلة إعادة تشغيل العامل وفق سياسة واضحة، وتمنع تكرار الأثر الخارجي أو تكشفه قبل تنفيذه."` | — |
| [SRC-E73001D9AC-L000784](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L784) | 784 | `"- التوسع الأفقي يتطلب فحص اتصالات قاعدة البيانات وحدود الموفرات ومشاركة الملفات ومفاتيح cache والتوقيت وساعات النظام."` | — |
| [SRC-E73001D9AC-L000785](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L785) | 785 | `"- تحديد حدود اتصال لكل نسخة، وحدود إجمالية عند الحاجة حتى لا يؤدي عدد النسخ إلى إغراق قاعدة البيانات أو الموفر الخارجي."` | — |
| [SRC-E73001D9AC-L000786](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L786) | 786 | `"- فصل الصحة المحلية للعملية عن الجاهزية لقبول طلبات جديدة، مع سلوك سليم أثناء الإغلاق واستنزاف الطلبات (graceful shutdown)."` | — |
| [SRC-E73001D9AC-L000787](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L787) | 787 | `""` | — |
| [SRC-E73001D9AC-L000788](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L788) | 788 | `"## 26. اختبارات اللياقة المعمارية (Architecture Fitness Functions)"` | — |
| [SRC-E73001D9AC-L000789](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L789) | 789 | `""` | — |
| [SRC-E73001D9AC-L000790](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L790) | 790 | `"يجب أن تتحول القواعد المعمارية المهمة إلى فحوص تكرارية حيثما أمكن، بدل الاعتماد الكامل على ذاكرة المطور أو المراجعة اليدوية."` | — |
| [SRC-E73001D9AC-L000791](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L791) | 791 | `""` | — |
| [SRC-E73001D9AC-L000792](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L792) | 792 | `"من أمثلة الفحوص الممكنة بعد مراجعة بنية الكود:"` | — |
| [SRC-E73001D9AC-L000793](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L793) | 793 | `"- منع الاعتماديات الدائرية بين المجالات."` | — |
| [SRC-E73001D9AC-L000794](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L794) | 794 | `"- منع استيراد ملفات خاصة من وحدة أخرى خارج واجهتها المعلنة."` | — |
| [SRC-E73001D9AC-L000795](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L795) | 795 | `"- كشف الأسرار في الفروق والملفات المضافة."` | — |
| [SRC-E73001D9AC-L000796](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L796) | 796 | `"- التحقق من أن كل أداة مسجلة لها schema وحدود زمنية وصلاحيات واختبارات ذات صلة."` | — |
| [SRC-E73001D9AC-L000797](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L797) | 797 | `"- التحقق من أن كل Skill وWorkflow لها مدخلات ومخرجات وحدود ونسخة واختبارات، ولا تستدعي قدرات غير معتمدة."` | — |
| [SRC-E73001D9AC-L000798](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L798) | 798 | `"- التحقق من أن الخطط الصادرة عن النماذج تُفحص قبل التنفيذ، ولا تستطيع تغيير الميزانيات أو الصلاحيات."` | — |
| [SRC-E73001D9AC-L000799](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L799) | 799 | `"- منع تنفيذ كود عام من مخرجات النموذج في مسارات التشغيل، ما لم يعتمد قرار مستقل وآلية عزل واختبارات مناسبة."` | — |
| [SRC-E73001D9AC-L000800](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L800) | 800 | `"- التحقق من أن مسودات التعريف لا تدخل الكتالوج النشط دون اعتماد، وأن Meta-Agent لا يملك اعتماد نفسه."` | — |
| [SRC-E73001D9AC-L000801](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L801) | 801 | `"- اختبارات regression تثبت الحفاظ على السلوك القائم عند استخراج وظيفة إلى Skill أو Workflow."` | — |
| [SRC-E73001D9AC-L000802](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L802) | 802 | `"- التأكد من أن نقاط API الحساسة تخضع للمصادقة والصلاحيات المطلوبة."` | — |
| [SRC-E73001D9AC-L000803](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L803) | 803 | `"- اختبارات تزامن تمنع اختلاط سياق المستخدمين."` | — |
| [SRC-E73001D9AC-L000804](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L804) | 804 | `"- اختبارات عقود تمنع انكسار العملاء أو موصلات البحث عند تغيّر الردود."` | — |
| [SRC-E73001D9AC-L000805](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L805) | 805 | `"- اختبارات ترحيل للبيانات من إصدار سابق إلى الإصدار الجديد."` | — |
| [SRC-E73001D9AC-L000806](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L806) | 806 | `"- اختبارات أداء مرجعية للمسارات المهمة مع حدود تنبيه معقولة."` | — |
| [SRC-E73001D9AC-L000807](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L807) | 807 | `"- فحص أن التكوين الافتراضي لا يفتح الإدارة أو التشخيص للعامة بلا حماية."` | — |
| [SRC-E73001D9AC-L000808](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L808) | 808 | `""` | — |
| [SRC-E73001D9AC-L000809](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L809) | 809 | `"لا تُضاف فحوص شكلية لا تحمي خطرًا حقيقيًا، ولا تفشل خطوط البناء لأسباب غير مستقرة أو غير موثقة. لكل فحص مالك وسبب وطريقة تفسير ووسيلة استثناء مؤقت محدودة."` | — |
| [SRC-E73001D9AC-L000810](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L810) | 810 | `""` | — |
| [SRC-E73001D9AC-L000811](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L811) | 811 | `"## 27. إدارة الديون التقنية والتغيير المستمر"` | — |
| [SRC-E73001D9AC-L000812](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L812) | 812 | `""` | — |
| [SRC-E73001D9AC-L000813](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L813) | 813 | `"- الحفاظ على خريطة اعتماديات بسيطة ومحدثة للمكونات الحرجة ومزوديها ومخازنها."` | — |
| [SRC-E73001D9AC-L000814](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L814) | 814 | `"- تسجيل القرارات التي يصعب الرجوع عنها في ADR، مع البدائل والتكلفة والمخاطر وأدلة الاختيار."` | — |
| [SRC-E73001D9AC-L000815](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L815) | 815 | `"- فصل الديون التقنية المعروفة عن العيوب المثبتة والميزات المؤجلة."` | — |
| [SRC-E73001D9AC-L000816](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L816) | 816 | `"- تقييم الدين التقني وفق احتمال فشل، ونطاق أثر، وكلفة لاحقة، وتكرار لمس الوحدة، بدل التعامل معه كقائمة شكلية."` | — |
| [SRC-E73001D9AC-L000817](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L817) | 817 | `"- عدم إجراء refactor واسع أثناء إصلاح عيب أمني عاجل إلا لضرورة موثقة؛ يفصل التغيير ليسهل مراجعته واختباره."` | — |
| [SRC-E73001D9AC-L000818](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L818) | 818 | `"- تحديد سياسة lifecycle للاعتماديات: تحديثات أمنية عاجلة، وتحديثات اعتيادية، واختبارات توافق، والتخلص من المكتبات المهجورة."` | — |
| [SRC-E73001D9AC-L000819](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L819) | 819 | `"- توفير feature flags أو إعدادات إيقاف عندما تخدم تقليل مخاطر الإطلاق، مع خطة لحذف الأعلام المؤقتة بعد انتهاء الحاجة."` | — |
| [SRC-E73001D9AC-L000820](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L820) | 820 | `"- نشر التغييرات الكبيرة تدريجيًا حيث تسمح المنصة، ومراقبة النتائج، ووقف النشر أو التراجع إذا تجاوزت حدود الفشل المعتمدة."` | — |
| [SRC-E73001D9AC-L000821](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L821) | 821 | `"- الحفاظ على changelog مناسب للتغييرات التي تمس المستخدم أو API أو التشغيل."` | — |
| [SRC-E73001D9AC-L000822](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L822) | 822 | `"- عدم السماح بأن يصبح عدد التجريدات أو الخدمات أكبر من قدرة المشروع على اختبارها ومراقبتها وصيانتها."` | — |
| [SRC-E73001D9AC-L000823](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L823) | 823 | `""` | — |
| [SRC-E73001D9AC-L000824](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L824) | 824 | `"## 28. بوابة قبول التوسع والتطوير"` | — |
| [SRC-E73001D9AC-L000825](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L825) | 825 | `""` | — |
| [SRC-E73001D9AC-L000826](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L826) | 826 | `"قبل اعتماد تغيير يضيف مجالًا أو أداة أو وكيلًا أو مخزنًا أو خدمة، يجب الإجابة وتوثيق ما ينطبق:"` | — |
| [SRC-E73001D9AC-L000827](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L827) | 827 | `"1. ما المشكلة الفعلية أو الحاجة المتوقعة التي يعالجها التغيير؟"` | — |
| [SRC-E73001D9AC-L000828](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L828) | 828 | `"2. هل يوجد حل أبسط داخل البنية الحالية؟"` | — |
| [SRC-E73001D9AC-L000829](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L829) | 829 | `"3. ما الواجهة أو العقد الذي يفصل المكون عن بقية النظام؟"` | — |
| [SRC-E73001D9AC-L000830](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L830) | 830 | `"4. كيف سيُختبر النجاح والفشل وانقطاع الاتصال والمدخلات غير الصالحة؟"` | — |
| [SRC-E73001D9AC-L000831](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L831) | 831 | `"5. ما أثر التغيير على صلاحيات المستخدمين وحدود الثقة والخصوصية؟"` | — |
| [SRC-E73001D9AC-L000832](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L832) | 832 | `"6. هل يحتاج إلى بيانات أو أسرار أو موارد جديدة؟"` | — |
| [SRC-E73001D9AC-L000833](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L833) | 833 | `"7. كيف ستُدار الإصدارات والتوافق والترحيلات؟"` | — |
| [SRC-E73001D9AC-L000834](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L834) | 834 | `"8. ما الحد الأقصى للوقت والحجم والتزامن والتكلفة؟"` | — |
| [SRC-E73001D9AC-L000835](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L835) | 835 | `"9. كيف تتم المراقبة والتعطيل والتراجع؟"` | — |
| [SRC-E73001D9AC-L000836](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L836) | 836 | `"10. ما الدليل الذي يسمح بالقول إن التغيير حسّن قابلية التوسع أو التطوير؟"` | — |
| [SRC-E73001D9AC-L000837](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L837) | 837 | `"11. ما الاختبارات الحالية التي تثبت عدم كسر السلوك السابق؟"` | — |
| [SRC-E73001D9AC-L000838](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L838) | 838 | `"12. من يوافق على المخاطر المتبقية؟"` | — |
| [SRC-E73001D9AC-L000839](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L839) | 839 | `""` | — |
| [SRC-E73001D9AC-L000840](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L840) | 840 | `"**معيار القبول:** لا يلزم أن يكون كل تفصيل مثاليًا أو موزعًا على خدمات مستقلة. يلزم أن تكون الحدود مفهومة، والمخاطر المتوقعة معالجة، والتغيير قابلًا للاختبار والصيانة والتراجع بقدر يتناسب مع خطورته."` | — |
| [SRC-E73001D9AC-L000841](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L841) | 841 | `""` | — |
| [SRC-E73001D9AC-L000842](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L842) | 842 | `"---"` | — |
| [SRC-E73001D9AC-L000843](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L843) | 843 | `""` | — |
| [SRC-E73001D9AC-L000844](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L844) | 844 | `"# الجزء الحادي عشر — تعريف “مكتمل” وقرار تغيير المتطلبات"` | — |
| [SRC-E73001D9AC-L000845](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L845) | 845 | `""` | — |
| [SRC-E73001D9AC-L000846](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L846) | 846 | `"## 29. تعريف الإنجاز"` | — |
| [SRC-E73001D9AC-L000847](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L847) | 847 | `"تُعتبر القدرة منجزة فقط عندما تتوافر كل العناصر المنطبقة:"` | — |
| [SRC-E73001D9AC-L000848](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L848) | 848 | `"1. متطلب محدد يمكن فهمه واختباره."` | — |
| [SRC-E73001D9AC-L000849](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L849) | 849 | `"2. تنفيذ واضح ضمن ملفات وإصدار محددين."` | — |
| [SRC-E73001D9AC-L000850](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L850) | 850 | `"3. اختبار نجاح واختبارات فشل وحدود ذات صلة."` | — |
| [SRC-E73001D9AC-L000851](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L851) | 851 | `"4. نتيجة فعلية محفوظة."` | — |
| [SRC-E73001D9AC-L000852](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L852) | 852 | `"5. قياس أداء إذا كان الادعاء متعلقًا بالسرعة أو السعة."` | — |
| [SRC-E73001D9AC-L000853](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L853) | 853 | `"6. دليل أمني إذا كان الادعاء متعلقًا بالأمان أو العزل."` | — |
| [SRC-E73001D9AC-L000854](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L854) | 854 | `"7. توثيق للقيود والبيئة ونطاق التحقق."` | — |
| [SRC-E73001D9AC-L000855](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L855) | 855 | `"8. مراجعة أن القدرة لم تُضعف خصائص قائمة."` | — |
| [SRC-E73001D9AC-L000856](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L856) | 856 | `"9. حالة VERIFIED مرتبطة بالالتزام المحدد، لا بالمشروع كله."` | — |
| [SRC-E73001D9AC-L000857](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L857) | 857 | `""` | — |
| [SRC-E73001D9AC-L000858](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L858) | 858 | `"## 30. سجل القرارات والاستثناءات"` | — |
| [SRC-E73001D9AC-L000859](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L859) | 859 | `""` | — |
| [SRC-E73001D9AC-L000860](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L860) | 860 | `"يُسجل قرار الاتجاه Skill/Workflow-First وAgent-Later وتفصيلاته في [المعمارية الحاكمة للقدرات والمهارات وسير العمل والوكلاء](OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md)، ويظل مقترحًا حتى موافقة المدير البشري. أي تغيير لاحق يوسع الاستقلالية أو يسمح بتوليد الكود أو يغير سقف الصلاحيات يحتاج إلى ADR مستقل يوضح الحاجة والأدلة والبدائل والمخاطر والاختبارات والموافقة المطلوبة."` | — |
| [SRC-E73001D9AC-L000861](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L861) | 861 | `""` | — |
| [SRC-E73001D9AC-L000862](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L862) | 862 | `"يجب تسجيل القرارات المعمارية الكبيرة في ADR موجز يتضمن:"` | — |
| [SRC-E73001D9AC-L000863](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L863) | 863 | `"- المشكلة والسياق."` | — |
| [SRC-E73001D9AC-L000864](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L864) | 864 | `"- البدائل التي دُرست."` | — |
| [SRC-E73001D9AC-L000865](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L865) | 865 | `"- القرار وأسبابه."` | — |
| [SRC-E73001D9AC-L000866](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L866) | 866 | `"- آثار القرار على الأمان والأداء والتكلفة والاستضافة."` | — |
| [SRC-E73001D9AC-L000867](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L867) | 867 | `"- كيفية الاختبار والتراجع."` | — |
| [SRC-E73001D9AC-L000868](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L868) | 868 | `"- المخاطر المفتوحة وصاحب قبولها."` | — |
| [SRC-E73001D9AC-L000869](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L869) | 869 | `"- تاريخ القرار والمراجع/الالتزام المرتبط."` | — |
| [SRC-E73001D9AC-L000870](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L870) | 870 | `""` | — |
| [SRC-E73001D9AC-L000871](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L871) | 871 | `"أي استثناء من MUST يجب أن يكون صريحًا، محدد النطاق والمدة، مع بديل تعويضي وخطة إغلاق وموافقة صاحب المشروع؛ لا يُحوّل إلى استثناء شامل دائم."` | — |
| [SRC-E73001D9AC-L000872](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L872) | 872 | `""` | — |
| [SRC-E73001D9AC-L000873](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L873) | 873 | `"## 31. القاعدة النهائية"` | — |
| [SRC-E73001D9AC-L000874](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L874) | 874 | `""` | — |
| [SRC-E73001D9AC-L000875](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L875) | 875 | `"هذا الدستور يحكم اتجاه التطوير، لكنه لا يجيز تضخيم المعمارية بلا دليل، ولا يسمح بتسويق مزايا غير مختبرة. الأولوية هي بناء نظام **سريع بقدر ما تسمح به الأدلة والموارد، قوي أمام الأعطال، مقيد الصلاحيات، قابل للمراقبة، وصادق في حدود معرفته**."` | — |
| [SRC-E73001D9AC-L000876](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L876) | 876 | `""` | — |
| [SRC-E73001D9AC-L000877](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L877) | 877 | `"---"` | — |
| [SRC-E73001D9AC-L000878](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L878) | 878 | `""` | — |
| [SRC-E73001D9AC-L000879](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L879) | 879 | `"# مراجع معيارية خارجية للمراجعة الدورية"` | — |
| [SRC-E73001D9AC-L000880](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L880) | 880 | `""` | — |
| [SRC-E73001D9AC-L000881](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L881) | 881 | `"هذه المراجع مصادر إرشادية تُستخدم لاختيار الضوابط والاختبارات المناسبة، ولا تعني أن Omarai متوافق معها بمجرد إدراجها في الوثيقة. يجب تثبيت الإصدار المستخدم في كل تقييم أمني:"` | — |
| [SRC-E73001D9AC-L000882](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L882) | 882 | `""` | — |
| [SRC-E73001D9AC-L000883](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L883) | 883 | `"- [NIST Cybersecurity Framework (CSF) 2.0](https://www.nist.gov/cyberframework) — الحوكمة وتحديد المخاطر والحماية والكشف والاستجابة والتعافي."` | — |
| [SRC-E73001D9AC-L000884](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L884) | 884 | `"- [NIST Secure Software Development Framework (SSDF)](https://csrc.nist.gov/projects/ssdf) — ممارسات تطوير البرامج الآمنة وإدارة الثغرات."` | — |
| [SRC-E73001D9AC-L000885](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L885) | 885 | `"- [NIST AI Risk Management Framework (AI RMF)](https://www.nist.gov/itl/ai-risk-management-framework) — مخاطر الذكاء الاصطناعي وخصائص الثقة."` | — |
| [SRC-E73001D9AC-L000886](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L886) | 886 | `"- [OWASP Application Security Verification Standard (ASVS)](https://owasp.org/projects/asvs) — متطلبات قابلة للتحقق لأمن تطبيقات الويب."` | — |
| [SRC-E73001D9AC-L000887](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L887) | 887 | `"- [OWASP GenAI Security Project — LLM Top 10](https://genai.owasp.org/llm-top-10/) — مخاطر تطبيقات النماذج والوكلاء، بما فيها حقن التعليمات وإساءة استخدام الأدوات وتسريب المعلومات."` | — |
| [SRC-E73001D9AC-L000888](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L888) | 888 | `"- [OWASP Artificial Intelligence Security Verification Standard (AISVS)](https://owasp.org/projects/artificial-intelligence-security-verification-standard-aisvs-docs) — متطلبات تحقق أمنية مخصصة لأنظمة الذكاء الاصطناعي."` | — |
| [SRC-E73001D9AC-L000889](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L889) | 889 | `"- [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) — مبادئ المعمارية التشغيلية والأمان والموثوقية والأداء والتكلفة والاستدامة."` | — |
| [SRC-E73001D9AC-L000890](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L890) | 890 | `"- [Microsoft Azure Well-Architected Framework](https://learn.microsoft.com/en-us/azure/architecture/framework/) — مرجع مراجعة موثوقية وأمن وأداء وتكلفة الأنظمة."` | — |
| [SRC-E73001D9AC-L000891](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L891) | 891 | `"- [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework) — تصميم الأنظمة وتشغيلها وقياسها وتحسينها."` | — |
| [SRC-E73001D9AC-L000892](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L892) | 892 | `"- [Google SRE Books](https://sre.google/books/) — أهداف مستوى الخدمة وميزانيات الأخطاء والاستجابة للحوادث."` | — |
| [SRC-E73001D9AC-L000893](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L893) | 893 | `"- [DORA — Continuous Delivery](https://dora.dev/capabilities/continuous-delivery/) — تسليم تغييرات آمنة وقابلة للتكرار."` | — |
| [SRC-E73001D9AC-L000894](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L894) | 894 | `"- [OpenTelemetry](https://opentelemetry.io/docs/) — توحيد المقاييس والسجلات والتتبعات."` | — |
| [SRC-E73001D9AC-L000895](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L895) | 895 | `"- [OWASP API Security Top 10](https://owasp.org/www-project-api-security/) — مخاطر شائعة في واجهات API."` | — |
| [SRC-E73001D9AC-L000896](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L896) | 896 | `"- [SLSA](https://slsa.dev/) — سلامة سلسلة توريد البرمجيات وإثبات منشأ artifacts."` | — |
| [SRC-E73001D9AC-L000897](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L897) | 897 | `"- [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) — إمكانية الوصول إلى محتوى الويب."` | — |
| [SRC-E73001D9AC-L000898](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L898) | 898 | `"- [NIST Privacy Framework](https://www.nist.gov/privacy-framework) — إدارة مخاطر الخصوصية."` | — |
| [SRC-E73001D9AC-L000899](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L899) | 899 | `"- [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) — الاستعداد والاستجابة لحوادث الأمن السيبراني."` | — |
| [SRC-E73001D9AC-L000900](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L900) | 900 | `"- [FinOps Framework](https://www.finops.org/framework/) — الشفافية والمسؤولية وتحسين تكلفة استخدام التقنية."` | — |
| [SRC-E73001D9AC-L000901](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L901) | 901 | `"- [Omarai Global Platform Engineering Baseline](OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md) — المتطلبات الموسعة وعناصر المراجعة العملية."` | — |
| [SRC-E73001D9AC-L000902](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L902) | 902 | `""` | — |
| [SRC-E73001D9AC-L000903](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L903) | 903 | `"تُراجع الإصدارات الرسمية دوريًا، وتُسجل النسخة والتاريخ عند تحويل أي مرجع إلى قائمة اختبار. لا تُستخدم عبارة “متوافق مع NIST/OWASP” إلا بعد وجود تقييم نطاقي وأدلة تغطي المتطلبات المنطبقة."` | — |
## وثائق وفهرسة

### FILE-D17CE3D12F — [docs/OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-D17CE3D12F-L000001](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L1) | 1 | `"# Omarai — خط الأساس الهندسي للمنصات العالمية واسعة النطاق"` | — |
| [SRC-D17CE3D12F-L000002](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L2) | 2 | `""` | — |
| [SRC-D17CE3D12F-L000003](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L3) | 3 | `"**المعرّف:** OMARAI-GLOBAL-PLATFORM-BASELINE-001  "` | — |
| [SRC-D17CE3D12F-L000004](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L4) | 4 | `"**الإصدار:** 1.0.0  "` | — |
| [SRC-D17CE3D12F-L000005](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L5) | 5 | `"**الحالة:** معيار تأسيسي مقترح للمراجعة والاعتماد من مدير المشروع  "` | — |
| [SRC-D17CE3D12F-L000006](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L6) | 6 | `"**النطاق:** المنتج، والمعمارية، والبيانات، والأمن، والذكاء الاصطناعي، والواجهة، والتشغيل، وسلسلة توريد البرمجيات، والتكلفة، والحوكمة  "` | — |
| [SRC-D17CE3D12F-L000007](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L7) | 7 | `"**علاقته بالدستور:** وثيقة مكمّلة للدستور التأسيسي للهندسة والموثوقية والأمان والذكاء، ولـ [سجل المتطلبات والتتبع والنضج وبوابات الاعتماد](OMARAI_REQUIREMENTS_TRACEABILITY_AND_MATURITY_MODEL_AR.md) الذي يحول المتطلبات إلى حالات وأدلة وبوابات قرار؛ وتُقرأ الوثائق معًا لا بدلًا من بعضها. ويُستخدم [سجل المتطلبات الأساسية الأولي](OMARAI_REQUIREMENTS_REGISTER.md) لتحويل البنود الأساسية إلى معرفات وأولويات ومعايير قبول قابلة للتتبع.  "` | — |
| [SRC-D17CE3D12F-L000008](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L8) | 8 | `"**قاعدة الدليل:** هذه المتطلبات لا تثبت وحدها أن Omarai يطبقها. الحالة تظل PROPOSED إلى أن يوجد تنفيذ واختبار/قياس مناسب."` | — |
| [SRC-D17CE3D12F-L000009](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L9) | 9 | `""` | — |
| [SRC-D17CE3D12F-L000010](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L10) | 10 | `"---"` | — |
| [SRC-D17CE3D12F-L000011](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L11) | 11 | `""` | — |
| [SRC-D17CE3D12F-L000012](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L12) | 12 | `"## 0. حدود الوثيقة وكيفية استخدامها"` | — |
| [SRC-D17CE3D12F-L000013](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L13) | 13 | `""` | — |
| [SRC-D17CE3D12F-L000014](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L14) | 14 | `"لا توجد قائمة عامة واحدة تحتوي حرفيًا على كل سياسة داخلية تستخدمها كل منصة عالمية كبيرة؛ كثير من السياسات التجارية والداخلية غير منشور، وتختلف الاحتياجات باختلاف المخاطر والمنتج والبنية والميزانية. لذلك لا تدّعي هذه الوثيقة معرفة الأسرار الداخلية للشركات. إنها تجمع متطلبات وممارسات عامة منشورة ومبادئ هندسية ناضجة، ثم تكيّفها مع Omarai."` | — |
| [SRC-D17CE3D12F-L000015](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L15) | 15 | `""` | — |
| [SRC-D17CE3D12F-L000016](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L16) | 16 | `"نموذج المرجع يشمل، بحسب الصلة: أطر Well-Architected لدى AWS وMicrosoft Azure وGoogle Cloud؛ ممارسات SRE؛ مبادئ التسليم البرمجي المستمر؛ OWASP لتطبيقات الويب وواجهات API والذكاء الاصطناعي؛ أطر NIST للأمن والخصوصية وتطوير البرمجيات والاستجابة للحوادث؛ OpenTelemetry؛ SLSA؛ WCAG؛ وFinOps. وجود اسم معيار هنا لا يعني التوافق معه."` | — |
| [SRC-D17CE3D12F-L000017](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L17) | 17 | `""` | — |
| [SRC-D17CE3D12F-L000018](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L18) | 18 | `"### 0.1 الكلمات الملزمة"` | — |
| [SRC-D17CE3D12F-L000019](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L19) | 19 | `""` | — |
| [SRC-D17CE3D12F-L000020](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L20) | 20 | `"- **MUST / إلزامي:** شرط قبول في النطاق الذي ينطبق عليه."` | — |
| [SRC-D17CE3D12F-L000021](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L21) | 21 | `"- **SHOULD / افتراضيًا:** يطبّق ما لم يوثق سبب استثناء معقول وموافقة مناسبة."` | — |
| [SRC-D17CE3D12F-L000022](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L22) | 22 | `"- **MAY / عند الحاجة:** خيار مشروط بالقيمة والدليل."` | — |
| [SRC-D17CE3D12F-L000023](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L23) | 23 | `"- **VERIFIED / متحقق:** دليل قابل للفحص، مع أمر/اختبار/قياس وبيئة ونطاق."` | — |
| [SRC-D17CE3D12F-L000024](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L24) | 24 | `"- **INFERRED / مستنتج:** تفسير تدعمه قرائن لكنه غير مثبت باختبار مباشر."` | — |
| [SRC-D17CE3D12F-L000025](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L25) | 25 | `"- **PROPOSED / مقترح:** مطلب أو حل مستقبلي غير منفّذ/غير متحقق منه."` | — |
| [SRC-D17CE3D12F-L000026](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L26) | 26 | `"- **UNKNOWN / غير معلوم:** الأدلة المتاحة لا تكفي للحكم."` | — |
| [SRC-D17CE3D12F-L000027](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L27) | 27 | `""` | — |
| [SRC-D17CE3D12F-L000028](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L28) | 28 | `"### 0.2 مبدأ الملاءمة ومنع التضخم المعماري"` | — |
| [SRC-D17CE3D12F-L000029](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L29) | 29 | `""` | — |
| [SRC-D17CE3D12F-L000030](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L30) | 30 | `"1. كل متطلب يُربط بخطر أو احتياج أو وعد للمستخدم، وباختبار أو مقياس عند الإمكان."` | — |
| [SRC-D17CE3D12F-L000031](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L31) | 31 | `"2. لا يعني «مستوى عالمي» شراء خدمات مدفوعة أو بناء بنية موزعة منذ البداية. يجب أن يعمل الأساس ضمن قيود الاستضافة الحالية، وأن تبقى الضوابط اللاحقة قابلة للتفعيل تدريجيًا."` | — |
| [SRC-D17CE3D12F-L000032](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L32) | 32 | `"3. لا نضيف Kubernetes أو service mesh أو Kafka أو قواعد بيانات موزعة أو أكثر من قاعدة بيانات أو عشرات الخدمات لمجرد أنها شائعة لدى الشركات الكبيرة. كل تقنية تحتاج سببًا، وكلفة تشغيل وصيانة، وخطة مراقبة وتراجع، واختبارًا يثبت فائدتها."` | — |
| [SRC-D17CE3D12F-L000033](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L33) | 33 | `"4. يحدد نطاق كل ضابط بوضوح: كل الإصدارات، أم الإنتاج فقط، أم عند وجود حسابات مستخدمين/بيانات خاصة/مهام ذات أثر خارجي، أم عند تجاوز عتبة سعة محددة."` | — |
| [SRC-D17CE3D12F-L000034](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L34) | 34 | `"5. عندما لا تتوفر بيئة أو ميزانية لتطبيق ضابط، يجب تسجيل الخطر والبديل المؤقت والحدود بدل إخفاء الفجوة."` | — |
| [SRC-D17CE3D12F-L000035](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L35) | 35 | `"6. لا يُستخدم «جاهز للإنتاج» أو «آمن» أو «يتحمل ملايين المستخدمين» دون نطاق تشغيلي وأدلة ذات صلة."` | — |
| [SRC-D17CE3D12F-L000036](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L36) | 36 | `""` | — |
| [SRC-D17CE3D12F-L000037](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L37) | 37 | `"---"` | — |
| [SRC-D17CE3D12F-L000038](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L38) | 38 | `""` | — |
| [SRC-D17CE3D12F-L000039](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L39) | 39 | `"# القسم الأول — المتطلبات المؤسسية والتصميمية"` | — |
| [SRC-D17CE3D12F-L000040](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L40) | 40 | `""` | — |
| [SRC-D17CE3D12F-L000041](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L41) | 41 | `"## 1. تعريف المنتج وعقود السلوك"` | — |
| [SRC-D17CE3D12F-L000042](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L42) | 42 | `""` | — |
| [SRC-D17CE3D12F-L000043](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L43) | 43 | `"1. MUST أن يكون لكل مسار مستخدم رئيسي تعريف واضح للمدخلات، والمخرجات، وحالات الفشل، وما يراه المستخدم عند عدم توفر البحث أو النموذج أو أداة."` | — |
| [SRC-D17CE3D12F-L000044](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L44) | 44 | `"2. MUST فصل السلوك الموعود عن القدرة التجريبية أو المستقبلية في README والواجهة والوثائق."` | — |
| [SRC-D17CE3D12F-L000045](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L45) | 45 | `"3. SHOULD صياغة رحلة السؤال الرئيسية كمسار قابل للتتبع: استقبال → تحقق → تحديد الحاجة إلى البحث → جمع الأدلة → تقييم المصادر → تركيب الإجابة → مراجعة القيود → عرض المصادر/عدم اليقين."` | — |
| [SRC-D17CE3D12F-L000046](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L46) | 46 | `"4. MUST ألا يؤدي فشل مكوّن اختياري إلى إظهار نجاح زائف أو إجابة تبدو مؤكدة رغم غياب دليل ضروري."` | — |
| [SRC-D17CE3D12F-L000047](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L47) | 47 | `"5. SHOULD تحديد فئات الأسئلة التي يستطيع المنتج الإجابة عنها بكفاءة، والفئات التي تتطلب مصادر حديثة، والفئات التي ينبغي فيها الامتناع أو طلب توضيح."` | — |
| [SRC-D17CE3D12F-L000048](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L48) | 48 | `"6. MUST توثيق التغييرات التي تكسر سلوكًا متوقعًا للمستخدم، وإتاحتها عبر سجل تغييرات عند التأثير الملحوظ."` | — |
| [SRC-D17CE3D12F-L000049](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L49) | 49 | `"7. SHOULD الاحتفاظ بمجموعة حالات استخدام واقعية بالعربية لاختبار المسارات المهمة بعد كل تغيير."` | — |
| [SRC-D17CE3D12F-L000050](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L50) | 50 | `""` | — |
| [SRC-D17CE3D12F-L000051](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L51) | 51 | `"## 2. نموذج الخدمة والملكية والمسؤولية"` | — |
| [SRC-D17CE3D12F-L000052](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L52) | 52 | `""` | — |
| [SRC-D17CE3D12F-L000053](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L53) | 53 | `"1. لكل مكوّن حرج مالك منطقي مسؤول عن صحة سلوكه واختباراته ومراقبته ووثائقه؛ في مشروع يقوده شخص واحد، يمكن أن تكون هذه أدوارًا يجمعها شخص واحد، ولا نفترض وجود فريق غير موجود."` | — |
| [SRC-D17CE3D12F-L000054](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L54) | 54 | `"2. SHOULD وجود سجل خدمات ومكونات يتضمن: الغرض، الاعتماديات، حساسية البيانات، متطلبات الأسرار، طريقة الاختبار، طريقة التشغيل، حدود الموارد، وآلية الإيقاف."` | — |
| [SRC-D17CE3D12F-L000055](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L55) | 55 | `"3. MUST تحديد حدود الثقة بين الواجهة وAPI والوكيل ومزوّدي النماذج وأدوات البحث والتخزين."` | — |
| [SRC-D17CE3D12F-L000056](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L56) | 56 | `"4. MUST أن تكون إعدادات الإنتاج منفصلة عن الاختبارات والتطوير، مع قيم آمنة افتراضيًا وعدم تضمين مفاتيح حقيقية في الأمثلة."` | — |
| [SRC-D17CE3D12F-L000057](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L57) | 57 | `"5. SHOULD تعريف مستويات حرجة للخدمات والبيانات حتى تتناسب الضوابط مع الأثر الفعلي للفشل."` | — |
| [SRC-D17CE3D12F-L000058](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L58) | 58 | `"6. MUST ألا تكون تعليمات التشغيل أو الاستعادة معتمدة على معرفة شفوية غير موثقة وحدها."` | — |
| [SRC-D17CE3D12F-L000059](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L59) | 59 | `""` | — |
| [SRC-D17CE3D12F-L000060](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L60) | 60 | `"## 3. مبادئ القرار المعماري"` | — |
| [SRC-D17CE3D12F-L000061](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L61) | 61 | `""` | — |
| [SRC-D17CE3D12F-L000062](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L62) | 62 | `"1. MUST تقييم البساطة، والتكلفة، والأمن، والموثوقية، والأداء، وقابلية الصيانة معًا؛ لا يحل أي منها تلقائيًا محل الأخرى."` | — |
| [SRC-D17CE3D12F-L000063](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L63) | 63 | `"2. MUST توثيق القرار المؤثر في ADR أو سجل مكافئ، مع المشكلة والبدائل والاختيار والأسباب والمخاطر والاختبارات والتراجع."` | — |
| [SRC-D17CE3D12F-L000064](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L64) | 64 | `"3. SHOULD فصل التغييرات الكبيرة إلى تغييرات صغيرة قابلة للمراجعة، ما لم يوجد سبب تشغيل موثق لغير ذلك."` | — |
| [SRC-D17CE3D12F-L000065](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L65) | 65 | `"4. MUST تجنّب الاعتماديات الدائرية والواجهات الداخلية غير المستقرة بين الوحدات."` | — |
| [SRC-D17CE3D12F-L000066](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L66) | 66 | `"5. MUST وضع خطة لإزالة التجريدات المؤقتة والأعلام والواجهات القديمة بعد انتهاء الحاجة إليها."` | — |
| [SRC-D17CE3D12F-L000067](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L67) | 67 | `"6. MUST عدم تحويل «المستقبل قد يحتاج ذلك» وحده إلى سبب كافٍ لإضافة نظام موزع معقد."` | — |
| [SRC-D17CE3D12F-L000068](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L68) | 68 | `""` | — |
| [SRC-D17CE3D12F-L000069](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L69) | 69 | `"---"` | — |
| [SRC-D17CE3D12F-L000070](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L70) | 70 | `""` | — |
| [SRC-D17CE3D12F-L000071](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L71) | 71 | `"# القسم الثاني — هندسة الخدمة الموثوقة (SRE) والاستعداد التشغيلي"` | — |
| [SRC-D17CE3D12F-L000072](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L72) | 72 | `""` | — |
| [SRC-D17CE3D12F-L000073](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L73) | 73 | `"## 4. مؤشرات مستوى الخدمة SLI والأهداف SLO واتفاقيات SLA"` | — |
| [SRC-D17CE3D12F-L000074](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L74) | 74 | `""` | — |
| [SRC-D17CE3D12F-L000075](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L75) | 75 | `"1. SHOULD تعريف SLI لكل مسار مهم، مثل نجاح الطلب، وزمن الاستجابة، ونسبة إتمام البحث، وصحة عرض المصادر، ومعدل الأخطاء."` | — |
| [SRC-D17CE3D12F-L000076](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L76) | 76 | `"2. SHOULD وضع أهداف SLO مبدئية قابلة للقياس بناءً على البيئة المتاحة ثم تعديلها بالقياس؛ لا تُخترع نسبة توافر أو زمن استجابة بلا خط أساس."` | — |
| [SRC-D17CE3D12F-L000077](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L77) | 77 | `"3. إذا تعهّد Omarai لاحقًا بمستوى خدمة لعملاء، MUST التمييز بين SLO داخلي وSLA تعاقدي، وتعريف نافذة القياس والاستثناءات وطريقة الحساب."` | — |
| [SRC-D17CE3D12F-L000078](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L78) | 78 | `"4. SHOULD استخدام ميزانية أخطاء (Error Budget) عندما يصبح الاعتماد التشغيلي عليها مفيدًا: إذا استهلكت الأعطال الميزانية، تُعطى الأولوية للإصلاح والموثوقية بدل تسريع إطلاق الميزات."` | — |
| [SRC-D17CE3D12F-L000079](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L79) | 79 | `"5. MUST قياس الفشل من منظور المستخدم لا من صحة العملية وحدها؛ قد تكون العملية «حية» لكن الخدمة عاجزة عن إكمال الطلب."` | — |
| [SRC-D17CE3D12F-L000080](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L80) | 80 | `"6. MUST عدم إعلان هدف توافر عالٍ لا تسمح به استضافة مجانية أو موفر خارجي أو تصميم أحادي النقطة."` | — |
| [SRC-D17CE3D12F-L000081](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L81) | 81 | `"7. SHOULD تحديد حدود تدهور مقبولة لكل رحلة حرجة، بما فيها وضع محدود عند تعطل البحث أو مزود النموذج."` | — |
| [SRC-D17CE3D12F-L000082](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L82) | 82 | `""` | — |
| [SRC-D17CE3D12F-L000083](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L83) | 83 | `"## 5. مراجعة الاستعداد للإنتاج (Production Readiness Review)"` | — |
| [SRC-D17CE3D12F-L000084](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L84) | 84 | `""` | — |
| [SRC-D17CE3D12F-L000085](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L85) | 85 | `"قبل إطلاق قدرة ذات أثر ملحوظ أو تعريض بيانات حقيقية لها، تتم مراجعة تناسبية تشمل:"` | — |
| [SRC-D17CE3D12F-L000086](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L86) | 86 | `"- قائمة اعتماديات خارجية وحدود حصصها وطرق تعطلها."` | — |
| [SRC-D17CE3D12F-L000087](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L87) | 87 | `"- إعدادات البيئة والأسرار والمنافذ ونقاط الإدارة."` | — |
| [SRC-D17CE3D12F-L000088](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L88) | 88 | `"- الصحة والجاهزية والإغلاق الآمن."` | — |
| [SRC-D17CE3D12F-L000089](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L89) | 89 | `"- سجلات ومقاييس وتنبيهات ذات معنى."` | — |
| [SRC-D17CE3D12F-L000090](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L90) | 90 | `"- سياسة الوقت والموارد وإعادة المحاولة والإلغاء."` | — |
| [SRC-D17CE3D12F-L000091](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L91) | 91 | `"- معالجة البيانات الخاصة وفترة الاحتفاظ بها."` | — |
| [SRC-D17CE3D12F-L000092](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L92) | 92 | `"- النسخ الاحتياطي والاستعادة عند وجود بيانات لا تعوّض."` | — |
| [SRC-D17CE3D12F-L000093](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L93) | 93 | `"- خطة التراجع أو التعطيل."` | — |
| [SRC-D17CE3D12F-L000094](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L94) | 94 | `"- اختبارات النجاح والفشل والضغط الأساسية."` | — |
| [SRC-D17CE3D12F-L000095](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L95) | 95 | `"- دليل تشغيل مختصر واستجابة للحوادث."` | — |
| [SRC-D17CE3D12F-L000096](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L96) | 96 | `"- كلفة تقريبية لكل طلب/مهمة وحدود تمنع الاستهلاك غير المقصود."` | — |
| [SRC-D17CE3D12F-L000097](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L97) | 97 | `""` | — |
| [SRC-D17CE3D12F-L000098](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L98) | 98 | `"لا تعني القائمة أن كل بند يحتاج منصة مدفوعة؛ يمكن تنفيذ الضوابط الأساسية بأدوات بسيطة، على أن تكون الأدلة مناسبة للمخاطر."` | — |
| [SRC-D17CE3D12F-L000099](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L99) | 99 | `""` | — |
| [SRC-D17CE3D12F-L000100](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L100) | 100 | `"## 6. إدارة الحوادث والمشكلات"` | — |
| [SRC-D17CE3D12F-L000101](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L101) | 101 | `""` | — |
| [SRC-D17CE3D12F-L000102](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L102) | 102 | `"1. MUST وجود تصنيف أولي للحوادث بحسب أثرها على المستخدم والبيانات والأمن والتكلفة."` | — |
| [SRC-D17CE3D12F-L000103](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L103) | 103 | `"2. SHOULD وجود خطة استجابة مكتوبة: اكتشاف → احتواء → استعادة → تواصل → تحليل السبب → منع التكرار."` | — |
| [SRC-D17CE3D12F-L000104](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L104) | 104 | `"3. MUST حفظ سجل زمني للقرارات والتغييرات المؤثرة أثناء الحادث، مع حجب الأسرار والبيانات الشخصية."` | — |
| [SRC-D17CE3D12F-L000105](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L105) | 105 | `"4. SHOULD تكون مراجعة ما بعد الحادث قائمة على تحسين النظام والضوابط، لا على لوم الأفراد؛ وتحدد أسبابًا مباشرة ومساهمة، لا مجرد «خطأ بشري»."` | — |
| [SRC-D17CE3D12F-L000106](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L106) | 106 | `"5. MUST أن تتضمن الاستجابة الأمنية حفظ الأدلة، وعزل الاعتماديات أو الأسرار المتأثرة، وتدوير بيانات الاعتماد، وتقييم أثر البيانات، وتحديد إجراءات إشعار مناسبة وفق الالتزامات القانونية والعقود المنطبقة."` | — |
| [SRC-D17CE3D12F-L000107](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L107) | 107 | `"6. SHOULD وجود وضع صيانة أو رسالة حالة صادقة عند تعذر الخدمة، بدل تعليق الواجهة دون تفسير."` | — |
| [SRC-D17CE3D12F-L000108](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L108) | 108 | `"7. MUST اختبار خطوات الاستعادة للحوادث الحرجة دوريًا بقدر يتناسب مع أهمية الخدمة."` | — |
| [SRC-D17CE3D12F-L000109](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L109) | 109 | `""` | — |
| [SRC-D17CE3D12F-L000110](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L110) | 110 | `"## 7. المرونة والتدهور الآمن"` | — |
| [SRC-D17CE3D12F-L000111](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L111) | 111 | `""` | — |
| [SRC-D17CE3D12F-L000112](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L112) | 112 | `"1. MUST لكل اتصال خارجي مهلة صريحة (timeout) قابلة للضبط ضمن حدود معقولة."` | — |
| [SRC-D17CE3D12F-L000113](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L113) | 113 | `"2. MUST وضع ميزانيات وقت وعدد محاولات إجمالية للطلب؛ لا يجوز أن يستهلك كل مكون ميزانية مستقلة بلا حد إجمالي."` | — |
| [SRC-D17CE3D12F-L000114](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L114) | 114 | `"3. SHOULD استخدام إعادة المحاولة مع exponential backoff وjitter للأخطاء العابرة فقط، لا لكل أنواع الأخطاء."` | — |
| [SRC-D17CE3D12F-L000115](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L115) | 115 | `"4. MUST عدم إعادة محاولة عملية ذات أثر خارجي غير idempotent بلا آلية تمنع تكرار الأثر أو تتحمله بوضوح."` | — |
| [SRC-D17CE3D12F-L000116](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L116) | 116 | `"5. SHOULD استخدام circuit breaker أو bulkhead أو حد تزامن عندما تثبت مخاطر انهيار متسلسل أو احتجاز الموارد."` | — |
| [SRC-D17CE3D12F-L000117](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L117) | 117 | `"6. MUST تطبيق backpressure ورفض منضبط للطلبات الزائدة عند بلوغ الحدود، بدل قبول عمل لا يمكن إنجازه."` | — |
| [SRC-D17CE3D12F-L000118](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L118) | 118 | `"7. SHOULD أن يستخدم النظام نتيجة مخبأة قديمة فقط عندما تكون صلاحيتها ونوع السؤال والسياسة واضحة للمستخدم؛ لا تُستخدم نتائج قديمة بصمت في سؤال يتطلب معلومة آنية."` | — |
| [SRC-D17CE3D12F-L000119](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L119) | 119 | `"8. MUST تحديد فشل مغلق (fail closed) للأمن والصلاحيات، وفشل متدهور (graceful degradation) للقدرات الاختيارية؛ لا تُضعف الصلاحيات بسبب تعطل خدمة الهوية أو السياسة."` | — |
| [SRC-D17CE3D12F-L000120](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L120) | 120 | `"9. MUST منع retry storms وتكرار الاستدعاءات المكلفة عبر ميزانية إعادة محاولات على مستوى الطلب والموفر، لا عبر حد محلي فقط."` | — |
| [SRC-D17CE3D12F-L000121](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L121) | 121 | `""` | — |
| [SRC-D17CE3D12F-L000122](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L122) | 122 | `"---"` | — |
| [SRC-D17CE3D12F-L000123](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L123) | 123 | `""` | — |
| [SRC-D17CE3D12F-L000124](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L124) | 124 | `"# القسم الثالث — السعة والأداء والأنظمة الموزعة"` | — |
| [SRC-D17CE3D12F-L000125](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L125) | 125 | `""` | — |
| [SRC-D17CE3D12F-L000126](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L126) | 126 | `"## 8. هندسة الأداء والسعة"` | — |
| [SRC-D17CE3D12F-L000127](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L127) | 127 | `""` | — |
| [SRC-D17CE3D12F-L000128](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L128) | 128 | `"1. MUST تحديد المسارات التي تستحق القياس قبل تحسينها؛ لا تعتمد قرارات الأداء على الانطباع فقط."` | — |
| [SRC-D17CE3D12F-L000129](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L129) | 129 | `"2. SHOULD قياس latency عند p50 وp95 وp99 حيث يكون حجم العينات مناسبًا، إضافة إلى معدل الطلبات والأخطاء والموارد، مع فصل زمن الانتظار عن زمن التنفيذ."` | — |
| [SRC-D17CE3D12F-L000130](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L130) | 130 | `"3. MUST وضع حدود لأحجام الطلبات والردود والصفحات المستخرجة ونتائج البحث والسياق النصي وعدد الأدوات والخطوات والتوازي."` | — |
| [SRC-D17CE3D12F-L000131](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L131) | 131 | `"4. SHOULD استخدام workload models تمثل أنماط الاستخدام الواقعية، بما فيها التفاوت في حجم الأسئلة، والمصادر البطيئة، ومعدلات الطلب المتغيرة."` | — |
| [SRC-D17CE3D12F-L000132](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L132) | 132 | `"5. MUST عدم الادعاء بسعة مستخدمين متزامنين محددة دون اختبار حمل موثق يتضمن نسخة الكود والبيئة والإعدادات ونمط الحمل ومدة الاختبار ونتائجه."` | — |
| [SRC-D17CE3D12F-L000133](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L133) | 133 | `"6. SHOULD قياس كلفة الطلب من حيث زمن CPU والذاكرة وحركة الشبكة واستدعاءات البحث والنموذج والتخزين."` | — |
| [SRC-D17CE3D12F-L000134](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L134) | 134 | `"7. MUST تحديد نقطة الفشل الأولى المعروفة أو المجهولة: حد الموفر، أو ذاكرة العملية، أو اتصالات قاعدة البيانات، أو زمن المهام، أو حصة الاستضافة."` | — |
| [SRC-D17CE3D12F-L000135](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L135) | 135 | `"8. SHOULD إجراء اختبارات load وstress وsoak بصورة تدريجية عندما تسمح البيئة؛ لا يساوي اختبار قصير ناجح إثبات تحمل يوم كامل أو ذروة كبيرة."` | — |
| [SRC-D17CE3D12F-L000136](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L136) | 136 | `"9. MUST فحص أثر المنافسة (contention) والـ N+1 queries والتكرار غير الضروري وفتح الاتصالات على زمن الاستجابة."` | — |
| [SRC-D17CE3D12F-L000137](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L137) | 137 | `"10. MUST تحسين بناءً على قياسات، ثم إعادة القياس مع اختبار الانحدار."` | — |
| [SRC-D17CE3D12F-L000138](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L138) | 138 | `""` | — |
| [SRC-D17CE3D12F-L000139](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L139) | 139 | `"## 9. حدود الموارد والتوازن بين الإنصاف والتكلفة"` | — |
| [SRC-D17CE3D12F-L000140](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L140) | 140 | `""` | — |
| [SRC-D17CE3D12F-L000141](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L141) | 141 | `"1. MUST تحديد حد لكل طلب ولكل مستخدم/مفتاح عند وجود هوية، يشمل الوقت والحجم والتوازي وعدد الخطوات والاستدعاءات والتكلفة المقدرة."` | — |
| [SRC-D17CE3D12F-L000142](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L142) | 142 | `"2. SHOULD استخدام حصص مستقلة للمصادر الخارجية بحسب قيودها وتكلفتها."` | — |
| [SRC-D17CE3D12F-L000143](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L143) | 143 | `"3. MUST حماية مسارات العمل من مستخدم واحد أو مهمة واحدة تستهلك معظم الموارد؛ استخدم fair-use أو concurrency limits عندما ينطبق ذلك."` | — |
| [SRC-D17CE3D12F-L000144](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L144) | 144 | `"4. MUST وضع سقف واضح لعمق التخطيط وعمليات البحث وجلب الصفحات واستدعاءات النموذج والمراجعة وإعادة المحاولة."` | — |
| [SRC-D17CE3D12F-L000145](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L145) | 145 | `"5. SHOULD إعطاء الأولوية للطلبات القصيرة والحاسمة أو المهمة حسب سياسة معلنة عندما تتجاوز الطوابير قدرتها."` | — |
| [SRC-D17CE3D12F-L000146](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L146) | 146 | `"6. MUST توفير إلغاء ينتشر إلى الاتصالات والمهام التي لم تعد مطلوبة، حيث تدعم الأدوات ذلك."` | — |
| [SRC-D17CE3D12F-L000147](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L147) | 147 | `"7. SHOULD قياس نسبة الوقت المستهلك في انتظار موفر خارجي حتى يمكن تمييز بطء Omarai عن بطء المورد."` | — |
| [SRC-D17CE3D12F-L000148](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L148) | 148 | `"8. MUST منع حلقة لا نهائية بين وكيل وآخر أو بين التخطيط والتنفيذ والمراجعة؛ كل دورة لها شرط توقف وحد أقصى ومخرج فشل صريح."` | — |
| [SRC-D17CE3D12F-L000149](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L149) | 149 | `""` | — |
| [SRC-D17CE3D12F-L000150](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L150) | 150 | `"## 10. قرارات الأنظمة الموزعة"` | — |
| [SRC-D17CE3D12F-L000151](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L151) | 151 | `""` | — |
| [SRC-D17CE3D12F-L000152](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L152) | 152 | `"قبل توزيع أجزاء التطبيق، MUST تحليل ما يلي: تأخر الشبكة، والانقطاع الجزئي، وتكرار الرسائل، وعدم ترتيبها، واختلاف الساعات، وازدواج تنفيذ المهام، وتناسق الحالة، وفشل مخزن الحالة أو الاكتشاف أو المصادقة بين الخدمات."` | — |
| [SRC-D17CE3D12F-L000153](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L153) | 153 | `""` | — |
| [SRC-D17CE3D12F-L000154](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L154) | 154 | `"1. SHOULD اعتبار التسليم «مرة واحدة على الأقل» احتمالًا واقعيًا في الطوابير؛ صمّم التكرار بسلام بدل افتراض exactly-once دون ضمان من التقنية."` | — |
| [SRC-D17CE3D12F-L000155](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L155) | 155 | `"2. MUST تعريف idempotency keys أو سجل معالجة أو آلية مماثلة للعمليات التي يجب عدم تكرار أثرها."` | — |
| [SRC-D17CE3D12F-L000156](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L156) | 156 | `"3. MUST تحديد مصدر الحقيقة لكل نوع من الحالة، وعدم ترك نسخ متعددة قابلة للكتابة بلا سياسة حل تعارض."` | — |
| [SRC-D17CE3D12F-L000157](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L157) | 157 | `"4. SHOULD استخدام deadlines تنتقل عبر المكونات بدل إعادة بدء مهلة جديدة عند كل انتقال."` | — |
| [SRC-D17CE3D12F-L000158](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L158) | 158 | `"5. MUST تصميم graceful shutdown لتوقف استقبال العمل الجديد وإنهاء أو حفظ الجاري ضمن مهلة محددة."` | — |
| [SRC-D17CE3D12F-L000159](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L159) | 159 | `"6. MUST عدم جعل توفر أداة ثانوية شرطًا لعمل النواة كلها، إلا إذا كانت ضرورية لصحة النتيجة."` | — |
| [SRC-D17CE3D12F-L000160](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L160) | 160 | `"7. SHOULD اختبار التعطل الجزئي والتأخير وامتلاء الطابور وانقطاع قاعدة البيانات في بيئة آمنة قبل اعتماد تصميم موزع حرج."` | — |
| [SRC-D17CE3D12F-L000161](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L161) | 161 | `""` | — |
| [SRC-D17CE3D12F-L000162](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L162) | 162 | `"---"` | — |
| [SRC-D17CE3D12F-L000163](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L163) | 163 | `""` | — |
| [SRC-D17CE3D12F-L000164](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L164) | 164 | `"# القسم الرابع — هندسة البيانات والخصوصية والهوية"` | — |
| [SRC-D17CE3D12F-L000165](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L165) | 165 | `""` | — |
| [SRC-D17CE3D12F-L000166](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L166) | 166 | `"## 11. حوكمة البيانات وجودتها ودورة حياتها"` | — |
| [SRC-D17CE3D12F-L000167](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L167) | 167 | `""` | — |
| [SRC-D17CE3D12F-L000168](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L168) | 168 | `"1. MUST إعداد تصنيف عملي للبيانات، مثل عامة، تشغيلية داخلية، شخصية، حساسة، أسرار، مع تحديد من يمكنه رؤيتها."` | — |
| [SRC-D17CE3D12F-L000169](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L169) | 169 | `"2. MUST تحديد مصدر الحقيقة ومالك البيانات وشكلها ومخططها وجودتها وفترة الاحتفاظ بها لكل مخزن مهم."` | — |
| [SRC-D17CE3D12F-L000170](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L170) | 170 | `"3. SHOULD قياس الاكتمال والتكرار والصلاحية والحداثة والاتساق والمراجع المكسورة ومشكلات الترميز وفق طبيعة البيانات."` | — |
| [SRC-D17CE3D12F-L000171](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L171) | 171 | `"4. MUST التحقق من البيانات عند حدود النظام، وعدم الاعتماد على صحة متصفح المستخدم أو مخرجات النموذج أو موفر خارجي."` | — |
| [SRC-D17CE3D12F-L000172](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L172) | 172 | `"5. MUST تحديد قواعد الاحتفاظ والحذف والتصدير والاستعادة، بما فيها الكاش والسجلات والنسخ الاحتياطية والبيانات المنسوخة إلى موفرين خارجيين."` | — |
| [SRC-D17CE3D12F-L000173](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L173) | 173 | `"6. SHOULD تسجيل lineage كافٍ لمعرفة مصدر البيانات والتحويلات التي مرت بها متى كان ذلك مهمًا للقرار أو التحقيق."` | — |
| [SRC-D17CE3D12F-L000174](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L174) | 174 | `"7. MUST حماية أسرار المستخدمين ومحتوى محادثاتهم من الاستخدام غير الضروري في التسجيل والتحليلات."` | — |
| [SRC-D17CE3D12F-L000175](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L175) | 175 | `"8. MUST اختبار ترحيلات البيانات من الإصدارات القديمة، والتعامل مع السجلات الناقصة أو القديمة أو غير الصالحة."` | — |
| [SRC-D17CE3D12F-L000176](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L176) | 176 | `"9. MUST أن تكون سياسة حذف البيانات صريحة في شأن زمن الحذف من الأنظمة النشطة والنسخ الاحتياطية والموفرين؛ لا يعد الحذف فوريًا أو شاملًا إلا إذا ثبت."` | — |
| [SRC-D17CE3D12F-L000177](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L177) | 177 | `"10. SHOULD استخدام معرفات داخلية بدل نسخ بيانات شخصية إلى سجلات التشغيل حين تكفي المعرفات."` | — |
| [SRC-D17CE3D12F-L000178](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L178) | 178 | `""` | — |
| [SRC-D17CE3D12F-L000179](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L179) | 179 | `"## 12. الهوية والمصادقة والتفويض"` | — |
| [SRC-D17CE3D12F-L000180](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L180) | 180 | `""` | — |
| [SRC-D17CE3D12F-L000181](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L181) | 181 | `"عندما يُتاح المنتج لأكثر من مستخدم أو عميل، MUST:"` | — |
| [SRC-D17CE3D12F-L000182](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L182) | 182 | `"1. فصل المصادقة (من أنت؟) عن التفويض (ما الذي يسمح لك بفعله؟)."` | — |
| [SRC-D17CE3D12F-L000183](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L183) | 183 | `"2. التحقق من الصلاحية على مستوى المورد/السجل/العملية، لا على مستوى صفحة الواجهة فقط."` | — |
| [SRC-D17CE3D12F-L000184](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L184) | 184 | `"3. تطبيق أقل صلاحية ورفض افتراضي عند غياب السياسة أو تعطل التحقق."` | — |
| [SRC-D17CE3D12F-L000185](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L185) | 185 | `"4. اختبار IDOR/BOLA وتبديل المعرفات والوصول العرضي إلى محادثات مستخدم آخر."` | — |
| [SRC-D17CE3D12F-L000186](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L186) | 186 | `"5. حماية الجلسات والرموز والكوكيز من السرقة والتثبيت والتسريب؛ وتحديد انتهاء صلاحيتها وإبطالها."` | — |
| [SRC-D17CE3D12F-L000187](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L187) | 187 | `"6. منع أسرار الاعتماد من الظهور في URL أو سجلات الوصول أو رسائل الخطأ."` | — |
| [SRC-D17CE3D12F-L000188](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L188) | 188 | `"7. تحديد مسارات استعادة الحساب وتغيير بيانات الاعتماد ومراجعة الصلاحيات."` | — |
| [SRC-D17CE3D12F-L000189](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L189) | 189 | `"8. توثيق فصل حساب المالك/الإدارة عن المستخدم العادي وعدم نشر لوحات الإدارة بلا حماية."` | — |
| [SRC-D17CE3D12F-L000190](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L190) | 190 | `"9. عند الحاجة، دعم SSO/OIDC أو إدارة المؤسسات وفق حاجة مثبتة؛ لا يُضاف هذا التعقيد إلى نسخة فردية بلا متطلب."` | — |
| [SRC-D17CE3D12F-L000191](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L191) | 191 | `"10. اختبار سلوك الصلاحيات في API مباشرة، لا الاكتفاء باختبار الواجهة."` | — |
| [SRC-D17CE3D12F-L000192](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L192) | 192 | `""` | — |
| [SRC-D17CE3D12F-L000193](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L193) | 193 | `"## 13. العزل متعدد المستأجرين (Multi-tenancy)"` | — |
| [SRC-D17CE3D12F-L000194](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L194) | 194 | `""` | — |
| [SRC-D17CE3D12F-L000195](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L195) | 195 | `"هذا القسم يصبح إلزاميًا قبل تقديم مساحة عمل مشتركة لعدة جهات مستقلة، وليس مطلوبًا إنشاء نظام مؤسسات كامل قبل وجود مستخدمين متعددين."` | — |
| [SRC-D17CE3D12F-L000196](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L196) | 196 | `""` | — |
| [SRC-D17CE3D12F-L000197](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L197) | 197 | `"1. MUST تعريف حد واضح للمستأجر Tenant، وكيفية تحديده من سياق موثوق لا من قيمة غير موثقة يرسلها العميل."` | — |
| [SRC-D17CE3D12F-L000198](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L198) | 198 | `"2. MUST تمرير سياق المستأجر والتحقق منه في كل مسار يصل إلى بياناته، بما في ذلك البحث والتخزين والكاش والمهام والطوابير والسجلات والتصدير."` | — |
| [SRC-D17CE3D12F-L000199](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L199) | 199 | `"3. MUST تضمين tenant/user scope في مفاتيح cache والجلسات وعناصر التخزين عند انطباقه."` | — |
| [SRC-D17CE3D12F-L000200](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L200) | 200 | `"4. MUST اختبار حالات اختلاط المستأجرين وIDOR/BOLA وطلبات متزامنة بهويات مختلفة."` | — |
| [SRC-D17CE3D12F-L000201](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L201) | 201 | `"5. SHOULD توفير حصص وتحديد معدل لكل مستأجر، مع منع أن يستنزف عميل الموارد المشتركة كلها."` | — |
| [SRC-D17CE3D12F-L000202](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L202) | 202 | `"6. MUST تحديد تصدير البيانات والحذف ومشاركة البيانات داخل المؤسسة وصلاحيات الأدوار."` | — |
| [SRC-D17CE3D12F-L000203](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L203) | 203 | `"7. MUST تحديد ما إذا كانت البيانات مشتركة منطقيًا أو معزولة ماديًا، وشرح المخاطر ومقايضات التكلفة."` | — |
| [SRC-D17CE3D12F-L000204](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L204) | 204 | `"8. MUST منع إدخال بيانات مستأجر في ذاكرة مشتركة أو prompt أو retrieval index دون سياسة عزل واختبارات."` | — |
| [SRC-D17CE3D12F-L000205](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L205) | 205 | `"9. SHOULD دعم إجراءات إيقاف أو تعليق عميل مع الحفاظ على سلامة البيانات وسجل التدقيق."` | — |
| [SRC-D17CE3D12F-L000206](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L206) | 206 | `""` | — |
| [SRC-D17CE3D12F-L000207](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L207) | 207 | `"## 14. الخصوصية والموافقة والمتطلبات القانونية"` | — |
| [SRC-D17CE3D12F-L000208](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L208) | 208 | `""` | — |
| [SRC-D17CE3D12F-L000209](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L209) | 209 | `"1. MUST تطبيق تقليل البيانات: لا تُجمع البيانات لمجرد أن جمعها ممكن."` | — |
| [SRC-D17CE3D12F-L000210](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L210) | 210 | `"2. MUST بيان ما يرسل إلى موفري النماذج والبحث وأسباب الإرسال وفئات البيانات، بحسب سياق المنتج."` | — |
| [SRC-D17CE3D12F-L000211](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L211) | 211 | `"3. MUST عدم إرسال بيانات شخصية أو أسرار إلى مزود خارجي إلا وفق إعداد/سياسة مصرح بها ومبرر واضح."` | — |
| [SRC-D17CE3D12F-L000212](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L212) | 212 | `"4. SHOULD إتاحة أقل قدر مناسب من التحكم للمستخدم في سجل المحادثة والحذف والاحتفاظ عندما تكون هذه الميزات موجودة."` | — |
| [SRC-D17CE3D12F-L000213](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L213) | 213 | `"5. MUST عدم استخدام المحادثات للتدريب أو التحليلات أو أي غرض ثانوي إلا وفق سياسة وإذن/أساس مناسبين."` | — |
| [SRC-D17CE3D12F-L000214](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L214) | 214 | `"6. MUST مراعاة المتطلبات القانونية والتنظيمية والتعاقدية المنطبقة حسب الدول والأسواق والبيانات؛ لا تُفترض مطابقة GDPR أو غيره بمجرد إضافة رابط."` | — |
| [SRC-D17CE3D12F-L000215](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L215) | 215 | `"7. SHOULD إجراء تقييم أثر خصوصية قبل إضافة ملفات أو بيانات حساسة أو ميزات ذاكرة دائمة واسعة."` | — |
| [SRC-D17CE3D12F-L000216](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L216) | 216 | `"8. MUST مراجعة مخاطر إعادة التعرف من البيانات المجمّعة، والاحتفاظ في logs/traces، وإرسال telemetry إلى جهة ثالثة."` | — |
| [SRC-D17CE3D12F-L000217](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L217) | 217 | `"9. MUST توثيق حدود الحذف من مزود خارجي والنسخ الاحتياطي؛ لا تُقدم وعودًا تتجاوز قدرة Omarai ومزودي الخدمة."` | — |
| [SRC-D17CE3D12F-L000218](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L218) | 218 | `"10. SHOULD تحديد إجراءات استجابة لطلب الوصول أو التصحيح أو الحذف عندما تكون حقوق مماثلة واجبة التطبيق."` | — |
| [SRC-D17CE3D12F-L000219](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L219) | 219 | `""` | — |
| [SRC-D17CE3D12F-L000220](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L220) | 220 | `"---"` | — |
| [SRC-D17CE3D12F-L000221](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L221) | 221 | `""` | — |
| [SRC-D17CE3D12F-L000222](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L222) | 222 | `"# القسم الخامس — أمن التطبيق وواجهات API وسلسلة التوريد"` | — |
| [SRC-D17CE3D12F-L000223](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L223) | 223 | `""` | — |
| [SRC-D17CE3D12F-L000224](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L224) | 224 | `"## 15. دورة حياة التطوير الآمن (Secure SDLC)"` | — |
| [SRC-D17CE3D12F-L000225](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L225) | 225 | `""` | — |
| [SRC-D17CE3D12F-L000226](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L226) | 226 | `"1. MUST دمج الأمن في التخطيط والتصميم والبرمجة والاختبار والنشر والصيانة، لا في فحص أخير فقط."` | — |
| [SRC-D17CE3D12F-L000227](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L227) | 227 | `"2. MUST إجراء threat modeling عند تغير تدفق حساس للبيانات أو الأدوات أو الهوية أو الاتصالات الخارجية."` | — |
| [SRC-D17CE3D12F-L000228](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L228) | 228 | `"3. SHOULD استخدام نمذجة تهديدات عملية مثل STRIDE أو أسلوب مكافئ عندما يساعد في كشف الأصول والحدود والخصوم ومسارات الهجوم."` | — |
| [SRC-D17CE3D12F-L000229](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L229) | 229 | `"4. MUST وجود سياسة للتعامل مع الثغرات: تسجيلها، وتقييم شدتها، وإصلاحها، وإعادة اختبارها، وتوثيق المخاطر المتبقية."` | — |
| [SRC-D17CE3D12F-L000230](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L230) | 230 | `"5. MUST اعتماد إعدادات آمنة افتراضيًا، وعدم فتح وضع تشخيصي أو CORS واسع أو endpoint إداري للعامة بلا حاجة."` | — |
| [SRC-D17CE3D12F-L000231](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L231) | 231 | `"6. SHOULD تشغيل فحوص static analysis وdependency scanning وsecret scanning وweb/API security tests حين تسمح بيئة الأدوات."` | — |
| [SRC-D17CE3D12F-L000232](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L232) | 232 | `"7. MUST مراجعة التغييرات عالية الخطورة قبل الدمج، مع التركيز على الأثر الأمني والبيانات والصلاحيات والفشل."` | — |
| [SRC-D17CE3D12F-L000233](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L233) | 233 | `"8. MUST عدم اعتبار الفحص الآلي بديلًا لنموذج التهديد أو مراجعة السياق."` | — |
| [SRC-D17CE3D12F-L000234](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L234) | 234 | `"9. SHOULD تعريف سياسة زمنية للتعامل مع ثغرات Critical/High وفق القدرة الفعلية والمخاطر، وعدم تركها بلا مالك أو موعد."` | — |
| [SRC-D17CE3D12F-L000235](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L235) | 235 | `"10. MUST تجنب تسريب stack traces أو تفاصيل بيئة التشغيل للمستخدم."` | — |
| [SRC-D17CE3D12F-L000236](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L236) | 236 | `""` | — |
| [SRC-D17CE3D12F-L000237](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L237) | 237 | `"## 16. أمن واجهات API وحدود الشبكة"` | — |
| [SRC-D17CE3D12F-L000238](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L238) | 238 | `""` | — |
| [SRC-D17CE3D12F-L000239](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L239) | 239 | `"1. MUST فرض تحقق مخطط المدخلات في الخادم، وتحديد أحجام الجسم والرؤوس والطلبات والوقت."` | — |
| [SRC-D17CE3D12F-L000240](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L240) | 240 | `"2. MUST تطبيق مصادقة وتفويض لكل مسار يحتاجهما، مع حماية مستوى الكائن والوظيفة والخصائص."` | — |
| [SRC-D17CE3D12F-L000241](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L241) | 241 | `"3. MUST وضع rate limits وquotas على المسارات المعرضة للإساءة أو التكلفة العالية، مع تحديد معدل منصف عندما يكون التمييز بين المستخدمين ممكنًا."` | — |
| [SRC-D17CE3D12F-L000242](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L242) | 242 | `"4. MUST ضبط CORS للواجهات المطلوبة فقط، وعدم استخدام wildcard مع credentials."` | — |
| [SRC-D17CE3D12F-L000243](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L243) | 243 | `"5. MUST حماية من SSRF: قائمة سماح للأهداف عند إمكانها، حظر عناوين loopback/private/link-local والميتا داتا، فحص IPv4/IPv6، معالجة DNS وإعادة الحل، والتحكم في redirects، والبروتوكولات والمنافذ، وإعادة التحقق بعد كل تحويل."` | — |
| [SRC-D17CE3D12F-L000244](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L244) | 244 | `"6. MUST منع الوصول إلى ملفات محلية أو أنظمة داخلية عبر URL يقدمه المستخدم، بما في ذلك التحايل بترميزات أو أسماء مضللة."` | — |
| [SRC-D17CE3D12F-L000245](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L245) | 245 | `"7. MUST التحقق من توقيعات webhooks إن وجدت، مع timestamp وreplay protection وحدود حجم وزمن."` | — |
| [SRC-D17CE3D12F-L000246](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L246) | 246 | `"8. SHOULD اعتماد request/correlation ID آمن وعدم قبول قيمة غير موثوقة لتحديد هوية المستخدم."` | — |
| [SRC-D17CE3D12F-L000247](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L247) | 247 | `"9. MUST ألا تكشف رسائل الخطأ وجود حسابات أو أسرار أو مسارات محلية إلا ما يلزم."` | — |
| [SRC-D17CE3D12F-L000248](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L248) | 248 | `"10. SHOULD اختبار API وفق مخاطر OWASP API Security Top 10، خصوصًا BOLA، والقصور في المصادقة، والاستهلاك غير المحدود للموارد، وسوء إعدادات الأمان، والاعتماد غير الآمن على APIs أخرى."` | — |
| [SRC-D17CE3D12F-L000249](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L249) | 249 | `""` | — |
| [SRC-D17CE3D12F-L000250](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L250) | 250 | `"## 17. إدارة الأسرار والتشفير والثقة"` | — |
| [SRC-D17CE3D12F-L000251](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L251) | 251 | `""` | — |
| [SRC-D17CE3D12F-L000252](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L252) | 252 | `"1. MUST حفظ مفاتيح API والرموز وكلمات المرور خارج الشيفرة والتاريخ والوثائق والأمثلة والـ frontend."` | — |
