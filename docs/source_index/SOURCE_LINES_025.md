# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **025**
- سجلات الأسطر: **800**
- النطاق: SRC-D17CE3D12F-L000391 إلى SRC-9A0DFA994E-L000081
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## وثائق وفهرسة

### FILE-D17CE3D12F — [docs/OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-D17CE3D12F-L000391](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L391) | 391 | `"9. MUST عدم استخدام الثقة التي يعلنها النموذج عن نفسه بديلًا عن تحقق مستقل من الأدلة."` | — |
| [SRC-D17CE3D12F-L000392](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L392) | 392 | `"10. MUST ألا تتجاوز اللغة درجة ما تسمح به الأدلة، ولا يحوّل الاستنتاج الاحتمالي إلى خبر مؤكد."` | — |
| [SRC-D17CE3D12F-L000393](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L393) | 393 | `""` | — |
| [SRC-D17CE3D12F-L000394](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L394) | 394 | `"---"` | — |
| [SRC-D17CE3D12F-L000395](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L395) | 395 | `""` | — |
| [SRC-D17CE3D12F-L000396](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L396) | 396 | `"# القسم التاسع — هندسة الذكاء الاصطناعي والوكلاء (LLMOps/AgentOps)"` | — |
| [SRC-D17CE3D12F-L000397](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L397) | 397 | `""` | — |
| [SRC-D17CE3D12F-L000398](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L398) | 398 | `"## 27. فصل التخطيط والتفويض والتنفيذ والتحقق"` | — |
| [SRC-D17CE3D12F-L000399](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L399) | 399 | `""` | — |
| [SRC-D17CE3D12F-L000400](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L400) | 400 | `"1. MUST أن تظل قواعد الأمان والتفويض والحدود في كود/سياسة موثوقة لا في prompt النموذج وحده."` | — |
| [SRC-D17CE3D12F-L000401](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L401) | 401 | `"2. MUST ألا تمنح مخرجات النموذج صلاحيات أو تنفذ أمرًا خطيرًا دون تحقق مستقل من المخول والمدخلات والسياسة."` | — |
| [SRC-D17CE3D12F-L000402](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L402) | 402 | `"3. SHOULD تقسيم المهمة إلى مراحل معلومة: فهم، وخطة محدودة، وتنفيذ أدوات، وتجميع أدلة، وتحقق، وصياغة، مع السماح بتجاوز المراحل غير اللازمة."` | — |
| [SRC-D17CE3D12F-L000403](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L403) | 403 | `"4. MUST تحديد حد أقصى للخطوات والدورات والمراجعات وتوازي الأدوات والوقت والتكلفة، مع سبب توقف نهائي واضح."` | — |
| [SRC-D17CE3D12F-L000404](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L404) | 404 | `"5. MUST التحقق من مخطط البيانات القادمة من النموذج قبل استخدامها في قرار تنفيذي."` | — |
| [SRC-D17CE3D12F-L000405](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L405) | 405 | `"6. MUST اعتبار prompt ونتيجة النموذج والصفحات المستخرجة ونتيجة الأداة بيانات غير موثوقة، حتى لو جاءت من موفر مشهور."` | — |
| [SRC-D17CE3D12F-L000406](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L406) | 406 | `"7. MUST وجود سياج مستقل يمنع النموذج من تغيير إعدادات الأمان أو تعطيل سجلات التدقيق أو رفع ميزانية التشغيل."` | — |
| [SRC-D17CE3D12F-L000407](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L407) | 407 | `"8. SHOULD حفظ أثر تدقيق مختصر قابل للتتبع لمسار الوكيل وقرارات الأدوات، دون الاحتفاظ غير الضروري بالمحتوى الخاص."` | — |
| [SRC-D17CE3D12F-L000408](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L408) | 408 | `"9. MUST أن تكون أدوات الكتابة/الحذف/النشر/الدفع أو أي أثر خارجي حساس ذات صلاحيات صريحة، مع موافقة بشرية حين يتناسب ذلك مع درجة الخطر."` | — |
| [SRC-D17CE3D12F-L000409](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L409) | 409 | `"10. SHOULD إعطاء الأدوات صلاحيات ضيقة لكل مهمة بدل مشاركة حساب إداري شامل بين الوكلاء."` | — |
| [SRC-D17CE3D12F-L000410](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L410) | 410 | `""` | — |
| [SRC-D17CE3D12F-L000411](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L411) | 411 | `"## 28. حقن التعليمات والبيانات غير الموثوقة"` | — |
| [SRC-D17CE3D12F-L000412](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L412) | 412 | `""` | — |
| [SRC-D17CE3D12F-L000413](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L413) | 413 | `"1. MUST التمييز بين تعليمات النظام/السياسة وبين محتوى الويب ورسائل المستخدم والمرفقات ومخرجات الأدوات."` | — |
| [SRC-D17CE3D12F-L000414](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L414) | 414 | `"2. MUST ألا يتحول النص الذي تطلب صفحة خارجية من Omarai تنفيذه إلى تعليمات عليا؛ تُعامل هذه النصوص كبيانات قابلة للتحليل."` | — |
| [SRC-D17CE3D12F-L000415](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L415) | 415 | `"3. MUST اختبار prompt injection المباشر وغير المباشر، بما فيه محاولة تسريب الأسرار، وتجاوز السياسة، وتبديل الهدف، واستدعاء أداة غير مصرح بها."` | — |
| [SRC-D17CE3D12F-L000416](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L416) | 416 | `"4. MUST ألا تُدرج الأسرار في سياق النموذج لمجرد أن مهمة قد تستفيد منها."` | — |
| [SRC-D17CE3D12F-L000417](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L417) | 417 | `"5. SHOULD تقليل ما يدخل سياق النموذج إلى المعلومات اللازمة للمهمة فقط."` | — |
| [SRC-D17CE3D12F-L000418](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L418) | 418 | `"6. MUST فحص مخرجات النموذج قبل عرض HTML أو تنفيذ كود أو تفسيرها كاستعلام/أمر ذي أثر."` | — |
| [SRC-D17CE3D12F-L000419](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L419) | 419 | `"7. MUST استخدام قائمة أدوات مسموحة مع مخططات ومدخلات وصلاحيات محددة، لا تنفيذ أسماء أدوات ديناميكية غير موثقة."` | — |
| [SRC-D17CE3D12F-L000420](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L420) | 420 | `"8. SHOULD توفير اختبارات red-team دورية لمخاطر LLM والوكيل مع حالات هجوم محفوظة كـ regression tests."` | — |
| [SRC-D17CE3D12F-L000421](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L421) | 421 | `"9. MUST عدم اعتبار «طلب رفضه النموذج» ضابطًا أمنيًا كافيًا إذا كان بإمكانه الوصول إلى مورد أو أداة حساسة."` | — |
| [SRC-D17CE3D12F-L000422](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L422) | 422 | `"10. MUST عزل الأدوات التي تنفذ أوامر أو تشغل كودًا عن أسرار العملية ومخزن البيانات بحسب الحاجة؛ والأفضل عدم توفير تنفيذ عام للأوامر إن لم يكن ضرورة مثبتة."` | — |
| [SRC-D17CE3D12F-L000423](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L423) | 423 | `""` | — |
| [SRC-D17CE3D12F-L000424](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L424) | 424 | `"## 29. تقييم النماذج والموجهات وتغييراتها (AI Evaluation)"` | — |
| [SRC-D17CE3D12F-L000425](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L425) | 425 | `""` | — |
| [SRC-D17CE3D12F-L000426](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L426) | 426 | `"1. MUST اعتبار تغيير النموذج أو إصدار SDK أو system prompt أو قالب الاسترجاع أو إعدادات sampling تغييرًا قد يؤثر في السلوك، وأن يمر باختبارات تناسب أثره."` | — |
| [SRC-D17CE3D12F-L000427](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L427) | 427 | `"2. SHOULD حفظ prompts المهمة والإصدارات والتغييرات بطريقة قابلة للمراجعة، مع عدم تخزين أسرار داخلها."` | — |
| [SRC-D17CE3D12F-L000428](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L428) | 428 | `"3. MUST امتلاك مجموعة تقييم عربية ثابتة تشمل الأسئلة البسيطة، والبحث الحديث، والتعارض، والغموض، والرفض المناسب، وحقن التعليمات، والمصادر المفقودة، والمدخلات الطويلة."` | — |
| [SRC-D17CE3D12F-L000429](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L429) | 429 | `"4. SHOULD تقييم الإجابة عبر محاور منفصلة مثل صحة الادعاء، والاستشهاد، والاكتمال، واللغة، والرفض، والتكلفة، وزمن الإنجاز."` | — |
| [SRC-D17CE3D12F-L000430](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L430) | 430 | `"5. MUST مقارنة الإصدارات الجديدة بمجموعة الأساس؛ لا يكفي مثال واحد أعجب المراجع."` | — |
| [SRC-D17CE3D12F-L000431](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L431) | 431 | `"6. SHOULD استخدام مراجعة بشرية للعينات ذات الأثر العالي أو الحالات التي لا توجد لها مقاييس آلية موثوقة."` | — |
| [SRC-D17CE3D12F-L000432](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L432) | 432 | `"7. MUST تسجيل نسخة النموذج وإعداداته الأساسية عند قياس الجودة، مع إدراك أن الاستجابات قد تختلف رغم نفس الإصدار."` | — |
| [SRC-D17CE3D12F-L000433](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L433) | 433 | `"8. MUST عدم السماح لمقيّم يستخدم النموذج نفسه أن يكون الدليل الوحيد على صحة ذلك النموذج."` | — |
| [SRC-D17CE3D12F-L000434](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L434) | 434 | `"9. SHOULD اختبار الموجهات على هجمات الخصم والتكرار وتغيير ترتيب النصوص وتضارب التعليمات."` | — |
| [SRC-D17CE3D12F-L000435](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L435) | 435 | `"10. MUST توثيق حدود التقييم: حجم العينة، وتغطيتها، وأوجه التحيز، وما لم يتم اختباره."` | — |
| [SRC-D17CE3D12F-L000436](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L436) | 436 | `""` | — |
| [SRC-D17CE3D12F-L000437](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L437) | 437 | `"## 30. توجيه النماذج والموفرين والكلفة"` | — |
| [SRC-D17CE3D12F-L000438](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L438) | 438 | `""` | — |
| [SRC-D17CE3D12F-L000439](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L439) | 439 | `"1. MUST عزل كل موفر عبر adapter وعقد موحد، مع مهلة واستجابة خطأ موحدة واختبارات توافق."` | — |
| [SRC-D17CE3D12F-L000440](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L440) | 440 | `"2. SHOULD قياس زمن البدء، وزمن الاستجابة، وحدود السياق، ومعدل الأخطاء، واستهلاك الرموز، والكلفة/الحصة بحسب المتاح."` | — |
| [SRC-D17CE3D12F-L000441](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L441) | 441 | `"3. MUST تحديد fallback واضح عند فشل نموذج أو موفر، مع منع تدهور الجودة بصمت."` | — |
| [SRC-D17CE3D12F-L000442](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L442) | 442 | `"4. MUST عدم تبديل إلى موفر أقل جودة ثم تقديم النتيجة على أنها مكافئة دون سياسة واضحة أو اختبار."` | — |
| [SRC-D17CE3D12F-L000443](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L443) | 443 | `"5. SHOULD استخدام توجيه حسب المهمة: نموذج صغير/أرخص للأعمال البسيطة، وقدرة أقوى حين تبررها الحاجة، بشرط تحقق الجودة والأمان."` | — |
| [SRC-D17CE3D12F-L000444](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L444) | 444 | `"6. MUST وضع حدود لتكلفة المهمة بما فيها التخطيط والبحث والتركيب والمراجعة؛ لا تترك الاستدعاءات مفتوحة."` | — |
| [SRC-D17CE3D12F-L000445](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L445) | 445 | `"7. SHOULD caching لمخرجات آمنة قابلة لإعادة الاستخدام مع مراعاة الحداثة والخصوصية ونطاق المستخدم."` | — |
| [SRC-D17CE3D12F-L000446](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L446) | 446 | `"8. MUST تجنب تخزين إجابات شخصية أو سرية في cache مشترك أو إعادة عرضها لمستخدم آخر."` | — |
| [SRC-D17CE3D12F-L000447](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L447) | 447 | `"9. SHOULD اختبار انتهاء الحصة، ورفض الخدمة، والـ timeout، والردود المشوهة، وتغير شكل استجابة الموفر."` | — |
| [SRC-D17CE3D12F-L000448](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L448) | 448 | `"10. MUST فصل «المفتاح موجود» و«الموصل مهيأ» عن «الموفر reachable» و«الطلب نجح»؛ لكل حالة دليل مختلف."` | — |
| [SRC-D17CE3D12F-L000449](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L449) | 449 | `""` | — |
| [SRC-D17CE3D12F-L000450](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L450) | 450 | `"## 31. الأدوات والقدرات ذات الأثر"` | — |
| [SRC-D17CE3D12F-L000451](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L451) | 451 | `""` | — |
| [SRC-D17CE3D12F-L000452](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L452) | 452 | `"1. MUST تصنيف الأدوات إلى قراءة عامة، وقراءة بيانات خاصة، وكتابة داخلية، وأثر خارجي حساس."` | — |
| [SRC-D17CE3D12F-L000453](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L453) | 453 | `"2. MUST إجراء تحقق صلاحيات من جهة الخادم قبل كل عملية حساسة."` | — |
| [SRC-D17CE3D12F-L000454](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L454) | 454 | `"3. MUST تحديد idempotency أو تأكيد بشري أو إجراء تعويضي للعمليات التي قد تتكرر أو لا يمكن عكسها."` | — |
| [SRC-D17CE3D12F-L000455](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L455) | 455 | `"4. SHOULD عرض معاينة واضحة لما سيُرسل أو يُغيّر قبل تنفيذ إجراء خارجي مؤثر."` | — |
| [SRC-D17CE3D12F-L000456](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L456) | 456 | `"5. MUST توفير kill switch لتعطيل أداة متضررة أو إساءة استخدامها دون تعطيل غير مرتبط بها متى أمكن."` | — |
| [SRC-D17CE3D12F-L000457](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L457) | 457 | `"6. MUST الاحتفاظ بسجل تدقيق يكفي لمعرفة من طلب العملية، وما السياسة التي سمحت بها، وما المخرج، دون تسريب زائد."` | — |
| [SRC-D17CE3D12F-L000458](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L458) | 458 | `"7. MUST عدم اعتبار نتيجة أداة untrusted executable code؛ تُفحص وتُتحقق وفق نوعها."` | — |
| [SRC-D17CE3D12F-L000459](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L459) | 459 | `"8. SHOULD استخدام sandbox محدود عند تشغيل محتوى أو كود، مع حدود شبكة وملفات وذاكرة ووقت."` | — |
| [SRC-D17CE3D12F-L000460](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L460) | 460 | `"9. MUST ألا تعود أخطاء الأداة بمعلومات سرية إلى النموذج أو المستخدم بلا تنقيح."` | — |
| [SRC-D17CE3D12F-L000461](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L461) | 461 | `"10. MUST اختبار فشل الأداة وبطئها وردها المضلل ومدخلاتها الحدودية، لا النجاح الطبيعي فقط."` | — |
| [SRC-D17CE3D12F-L000462](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L462) | 462 | `""` | — |
| [SRC-D17CE3D12F-L000463](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L463) | 463 | `"---"` | — |
| [SRC-D17CE3D12F-L000464](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L464) | 464 | `""` | — |
| [SRC-D17CE3D12F-L000465](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L465) | 465 | `"# القسم العاشر — الاختبارات والجودة والتحسين"` | — |
| [SRC-D17CE3D12F-L000466](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L466) | 466 | `""` | — |
| [SRC-D17CE3D12F-L000467](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L467) | 467 | `"## 32. مصفوفة الاختبارات"` | — |
| [SRC-D17CE3D12F-L000468](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L468) | 468 | `""` | — |
| [SRC-D17CE3D12F-L000469](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L469) | 469 | `"تُختار الاختبارات بحسب المخاطر، وتشمل عند انطباقها:"` | — |
| [SRC-D17CE3D12F-L000470](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L470) | 470 | `"- Unit tests لمنطق الوحدة."` | — |
| [SRC-D17CE3D12F-L000471](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L471) | 471 | `"- Integration tests للتفاعل مع التخزين والموفرين."` | — |
| [SRC-D17CE3D12F-L000472](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L472) | 472 | `"- Contract tests لواجهات API والأدوات."` | — |
| [SRC-D17CE3D12F-L000473](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L473) | 473 | `"- End-to-end tests لرحلات المستخدم الرئيسية."` | — |
| [SRC-D17CE3D12F-L000474](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L474) | 474 | `"- Regression tests لكل عيب مثبت تم إصلاحه."` | — |
| [SRC-D17CE3D12F-L000475](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L475) | 475 | `"- Property-based/fuzz tests لمدخلات معقدة أو غير موثوقة."` | — |
| [SRC-D17CE3D12F-L000476](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L476) | 476 | `"- Concurrency/race tests لبيانات المستخدمين والحالة المشتركة."` | — |
| [SRC-D17CE3D12F-L000477](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L477) | 477 | `"- Load/stress/soak tests للسعة والأداء."` | — |
| [SRC-D17CE3D12F-L000478](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L478) | 478 | `"- Fault-injection/chaos tests للانقطاع الجزئي والتأخير."` | — |
| [SRC-D17CE3D12F-L000479](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L479) | 479 | `"- Security tests للهوية والصلاحيات وSSRF وXSS والأسرار."` | — |
| [SRC-D17CE3D12F-L000480](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L480) | 480 | `"- Accessibility tests للواجهة."` | — |
| [SRC-D17CE3D12F-L000481](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L481) | 481 | `"- AI evaluation/red-team tests لجودة الإجابات وأمان الأدوات."` | — |
| [SRC-D17CE3D12F-L000482](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L482) | 482 | `"- Migration/restore tests لتغيير البيانات واستعادتها."` | — |
| [SRC-D17CE3D12F-L000483](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L483) | 483 | `""` | — |
| [SRC-D17CE3D12F-L000484](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L484) | 484 | `"MUST أن يكون لكل اختبار اسم وأمر تشغيل وشرط نجاح وبيانات اختبار واضحة بقدر الإمكان. MUST التمييز بين «لم يفشل الاختبار» و«لم يتم تشغيل الاختبار». SHOULD أن تكون الاختبارات الحتمية مستقرة؛ الاختبارات المتذبذبة تُعالج ولا تُعتاد على تجاهلها."` | — |
| [SRC-D17CE3D12F-L000485](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L485) | 485 | `""` | — |
| [SRC-D17CE3D12F-L000486](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L486) | 486 | `"## 33. جودة القياس والاختبار"` | — |
| [SRC-D17CE3D12F-L000487](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L487) | 487 | `""` | — |
| [SRC-D17CE3D12F-L000488](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L488) | 488 | `"1. MUST الإبلاغ عن عدد الاختبارات المنفذة والناجحة والفاشلة والمتخطاة، مع ذكر سبب التخطي."` | — |
| [SRC-D17CE3D12F-L000489](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L489) | 489 | `"2. MUST عدم إخفاء تحذير أو فشل أو flaky test إذا كان يؤثر في الاستنتاج."` | — |
| [SRC-D17CE3D12F-L000490](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L490) | 490 | `"3. SHOULD قياس تغطية الاختبارات للمسارات الحرجة لا chasing رقم تغطية مجرد."` | — |
| [SRC-D17CE3D12F-L000491](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L491) | 491 | `"4. MUST حفظ بيانات/عينات صناعية لا تكشف بيانات المستخدم الحقيقية."` | — |
| [SRC-D17CE3D12F-L000492](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L492) | 492 | `"5. SHOULD استخدام حراس جودة في CI للملفات ذات المخاطر، مع تبرير الاستثناءات."` | — |
| [SRC-D17CE3D12F-L000493](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L493) | 493 | `"6. MUST إعادة اختبار إصلاح العيب نفسه واختبار عدم رجوعه."` | — |
| [SRC-D17CE3D12F-L000494](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L494) | 494 | `"7. MUST ألا تتحول نتيجة mock إلى ادعاء بأن الاتصال الخارجي يعمل حقيقة."` | — |
| [SRC-D17CE3D12F-L000495](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L495) | 495 | `"8. SHOULD فصل الاختبارات التي تستخدم خدمات حقيقية أو أسرارًا عن الاختبارات المحلية حتى يمكن معرفة ما يثبته كل تشغيل."` | — |
| [SRC-D17CE3D12F-L000496](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L496) | 496 | `"9. MUST توثيق قيود بيئة الاختبار وأثرها على الحكم النهائي."` | — |
| [SRC-D17CE3D12F-L000497](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L497) | 497 | `"10. SHOULD مراجعة فشل الاختبارات وتحويل الأسباب المتكررة إلى تحسينات في التصميم أو الأدوات."` | — |
| [SRC-D17CE3D12F-L000498](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L498) | 498 | `""` | — |
| [SRC-D17CE3D12F-L000499](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L499) | 499 | `"## 34. مراجعة الكود والتعاون مع الوكلاء"` | — |
| [SRC-D17CE3D12F-L000500](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L500) | 500 | `""` | — |
| [SRC-D17CE3D12F-L000501](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L501) | 501 | `"1. MUST أن يتضمن كل تغيير غرضًا محدودًا ومعروفًا وأثرًا متوقعًا."` | — |
| [SRC-D17CE3D12F-L000502](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L502) | 502 | `"2. SHOULD أن تراجع التغييرات من زاوية التصميم والتعقيد والصحة والأمن والأداء والاختبارات والقابلية للصيانة، وفق مخاطرها."` | — |
| [SRC-D17CE3D12F-L000503](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L503) | 503 | `"3. MUST مراجعة كامل diff بعد تحرير الملفات آليًا، والتحقق من عدم ضياع أجزاء سابقة أو تغيير تنسيق/سلوك غير مقصود."` | — |
| [SRC-D17CE3D12F-L000504](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L504) | 504 | `"4. MUST ألا يحرر أكثر من منفذ/وكيل الملف نفسه بالتوازي دون تنسيق وتحديث على النسخة الأحدث."` | — |
| [SRC-D17CE3D12F-L000505](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L505) | 505 | `"5. MUST ألا يُقبل تقرير «تم الإصلاح» بدون تحديد الملفات والاختبارات والنتيجة."` | — |
| [SRC-D17CE3D12F-L000506](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L506) | 506 | `"6. SHOULD استخدام قوالب موحدة لطلبات التغيير وإصلاح العيوب ومراجعة الأمن."` | — |
| [SRC-D17CE3D12F-L000507](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L507) | 507 | `"7. MUST الحفاظ على حق مدير المشروع في قرارات الدمج والنشر والمخاطر المقبولة؛ الأدوات والوكلاء يقترحون وينفذون ضمن الصلاحيات ولا ينتزعون سلطة الاعتماد."` | — |
| [SRC-D17CE3D12F-L000508](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L508) | 508 | `"8. MUST ألا ينشئ الوكيل اختبارات تافهة تمر دائمًا لتغطية بند شكلي؛ يجب أن تفشل عند كسر السلوك المقصود."` | — |
| [SRC-D17CE3D12F-L000509](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L509) | 509 | `"9. SHOULD توثيق الافتراضات غير المثبتة بدل بناء طبقات فوقها."` | — |
| [SRC-D17CE3D12F-L000510](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L510) | 510 | `"10. MUST عدم اعتبار موافقة نموذج آخر أو تقرير ذاتي مراجعة مستقلة كافية للقرارات الحساسة."` | — |
| [SRC-D17CE3D12F-L000511](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L511) | 511 | `""` | — |
| [SRC-D17CE3D12F-L000512](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L512) | 512 | `"---"` | — |
| [SRC-D17CE3D12F-L000513](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L513) | 513 | `""` | — |
| [SRC-D17CE3D12F-L000514](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L514) | 514 | `"# القسم الحادي عشر — التكلفة والاستدامة والاعتماد على الأطراف"` | — |
| [SRC-D17CE3D12F-L000515](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L515) | 515 | `""` | — |
| [SRC-D17CE3D12F-L000516](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L516) | 516 | `"## 35. هندسة التكلفة (FinOps)"` | — |
| [SRC-D17CE3D12F-L000517](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L517) | 517 | `""` | — |
| [SRC-D17CE3D12F-L000518](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L518) | 518 | `"1. MUST أن تظل التكلفة المرصودة أو المقدرة لكل طلب ومهمة ضمن حدود محددة عندما تستخدم موارد مدفوعة أو حصصًا محدودة."` | — |
| [SRC-D17CE3D12F-L000519](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L519) | 519 | `"2. MUST تحديد حدود الاستخدام المجاني لكل موفر إن توفرت معلومات موثوقة، مع عدم اعتبار «مجاني الآن» ضمانًا للاستمرار."` | — |
| [SRC-D17CE3D12F-L000520](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L520) | 520 | `"3. SHOULD تتبع عدد نداءات النموذج والبحث والصفحات المستخرجة وطول السياق وزمن التنفيذ والكلفة النقدية أو البديلة."` | — |
| [SRC-D17CE3D12F-L000521](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L521) | 521 | `"4. MUST توفير حد إيقاف أو تخفيف عند استهلاك الحصة أو بلوغ الميزانية، حتى لا تؤدي حلقة وكيل إلى نفاد الرصيد."` | — |
| [SRC-D17CE3D12F-L000522](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L522) | 522 | `"5. SHOULD استخدام تكلفة الوحدة (cost per successful task) بدل النظر إلى التكلفة الإجمالية فقط."` | — |
| [SRC-D17CE3D12F-L000523](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L523) | 523 | `"6. MUST توثيق الاعتماد على مزود واحد وخطة الحد الأدنى لاستعادة الخدمة إذا أغلق الحساب أو غيّر الحصص."` | — |
| [SRC-D17CE3D12F-L000524](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L524) | 524 | `"7. SHOULD مقارنة كلفة التشغيل والكلفة الذهنية للصيانة قبل اعتماد تقنية جديدة."` | — |
| [SRC-D17CE3D12F-L000525](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L525) | 525 | `"8. MUST ألا نستخدم بنية أعلى كلفة أو تعقيدًا دون قيمة مقاسة أو خطر تستوجبه."` | — |
| [SRC-D17CE3D12F-L000526](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L526) | 526 | `"9. SHOULD مراقبة الموارد الخاملة والتخزين المتضخم والـ logs والـ caches التي لا تنتهي صلاحيتها."` | — |
| [SRC-D17CE3D12F-L000527](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L527) | 527 | `"10. MUST التمييز بين التكلفة النقدية وتكلفة وقت المطور والمخاطر التشغيلية."` | — |
| [SRC-D17CE3D12F-L000528](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L528) | 528 | `""` | — |
| [SRC-D17CE3D12F-L000529](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L529) | 529 | `"## 36. الاستدامة وكفاءة الموارد"` | — |
| [SRC-D17CE3D12F-L000530](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L530) | 530 | `""` | — |
| [SRC-D17CE3D12F-L000531](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L531) | 531 | `"1. SHOULD تقليل العمل المكرر والتحميل غير الضروري والطلبات التي لا تضيف قيمة، بما يخفض الكلفة واستهلاك الموارد."` | — |
| [SRC-D17CE3D12F-L000532](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L532) | 532 | `"2. SHOULD اختيار أحجام موارد مناسبة بدل الإفراط في تخصيصها أو جعلها قريبة من حد الانهيار."` | — |
| [SRC-D17CE3D12F-L000533](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L533) | 533 | `"3. MUST عدم التضحية بالأمان أو سلامة النتيجة من أجل تخفيض تكلفة صغير."` | — |
| [SRC-D17CE3D12F-L000534](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L534) | 534 | `"4. SHOULD قياس الأثر عندما يصبح استهلاك الموارد مهمًا، بدل إطلاق ادعاءات بيئية غير مقاسة."` | — |
| [SRC-D17CE3D12F-L000535](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L535) | 535 | `"5. MUST تصميم حدود الموارد كجزء من الأمان والموثوقية، لا باعتبارها تحسينًا ماليًا فقط."` | — |
| [SRC-D17CE3D12F-L000536](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L536) | 536 | `""` | — |
| [SRC-D17CE3D12F-L000537](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L537) | 537 | `"## 37. الاعتمادية على الموردين وقابلية النقل"` | — |
| [SRC-D17CE3D12F-L000538](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L538) | 538 | `""` | — |
| [SRC-D17CE3D12F-L000539](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L539) | 539 | `"1. MUST تسجيل كل خدمة خارجية حرجة، وما البيانات التي ترسل إليها، وحدود حصتها، وشروطها المؤثرة، وطريقة كشف تعطلها."` | — |
| [SRC-D17CE3D12F-L000540](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L540) | 540 | `"2. SHOULD عزل تفاصيل الموفر في adapter لتسهيل التبديل، مع الاعتراف بأن التكافؤ بين النماذج/المصادر غير مضمون."` | — |
| [SRC-D17CE3D12F-L000541](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L541) | 541 | `"3. MUST تحديد ما الذي يستمر في العمل عند فقد كل موفر: الواجهة، والأسئلة غير المعتمدة على البحث، ونتائج cache المناسبة، ورسالة الفشل."` | — |
| [SRC-D17CE3D12F-L000542](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L542) | 542 | `"4. SHOULD الاحتفاظ بخطة تصدير للبيانات الأساسية ونقلها من الاستضافة/المخزن، وفق الإمكانات الفعلية."` | — |
| [SRC-D17CE3D12F-L000543](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L543) | 543 | `"5. MUST عدم الاعتماد على ميزة مجانية حساسة دون خطة بديلة أو التصريح بأن الخدمة قد تتوقف عند انتهاء الحصة."` | — |
| [SRC-D17CE3D12F-L000544](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L544) | 544 | `"6. MUST عدم نقل أسرار أو بيانات خاصة إلى موفر احتياطي دون السماح بذلك بنفس سياسة الخصوصية والأمن."` | — |
| [SRC-D17CE3D12F-L000545](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L545) | 545 | `"7. SHOULD اختبار fallbacks فعليًا بصورة دورية، لا افتراض أنها تعمل لأنها مذكورة في الإعداد."` | — |
| [SRC-D17CE3D12F-L000546](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L546) | 546 | `""` | — |
| [SRC-D17CE3D12F-L000547](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L547) | 547 | `"---"` | — |
| [SRC-D17CE3D12F-L000548](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L548) | 548 | `""` | — |
| [SRC-D17CE3D12F-L000549](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L549) | 549 | `"# القسم الثاني عشر — تجربة المنتج والنمو القابل للقياس"` | — |
| [SRC-D17CE3D12F-L000550](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L550) | 550 | `""` | — |
| [SRC-D17CE3D12F-L000551](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L551) | 551 | `"## 38. ملاحظات المستخدم والتحليلات والتجارب"` | — |
| [SRC-D17CE3D12F-L000552](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L552) | 552 | `""` | — |
| [SRC-D17CE3D12F-L000553](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L553) | 553 | `"1. SHOULD جمع أقل قدر من telemetry المنتج اللازم لفهم نجاح المسارات والأخطاء، مع احترام الخصوصية."` | — |
| [SRC-D17CE3D12F-L000554](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L554) | 554 | `"2. MUST تعريف معنى كل مقياس (مثل «إجابة ناجحة» أو «بحث مكتمل») ومنع تغيير معناه بصمت."` | — |
| [SRC-D17CE3D12F-L000555](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L555) | 555 | `"3. SHOULD الفصل بين البيانات التشغيلية المطلوبة لتصحيح الأعطال والتحليلات المطلوبة لتحسين المنتج."` | — |
| [SRC-D17CE3D12F-L000556](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L556) | 556 | `"4. MUST تجنب إدخال نص السؤال أو الإجابة كاملة في التحليلات الافتراضية ما لم توجد ضرورة وسياسة واضحة."` | — |
| [SRC-D17CE3D12F-L000557](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L557) | 557 | `"5. SHOULD دعم feedback بسيط ومحدد، مع ربطه بإصدار وسياق تقني مناسب عندما لا يكشف بيانات خاصة."` | — |
| [SRC-D17CE3D12F-L000558](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L558) | 558 | `"6. MUST عدم اعتبار تفاعل المستخدم أو طول الإجابة أو إعجابًا واحدًا دليلًا منفردًا على صحة الإجابة."` | — |
| [SRC-D17CE3D12F-L000559](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L559) | 559 | `"7. SHOULD اختبار التغييرات الخطرة عبر إطلاق محدود أو feature flag عند توفر المنصة."` | — |
| [SRC-D17CE3D12F-L000560](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L560) | 560 | `"8. MUST وضع معايير إيقاف للتجربة إذا تدهورت الجودة أو الأمن أو معدل الأخطاء أو الكلفة."` | — |
| [SRC-D17CE3D12F-L000561](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L561) | 561 | `"9. SHOULD التمييز بين المقاييس الكمية والتعليقات النوعية، والتحقق من تحيز العينة."` | — |
| [SRC-D17CE3D12F-L000562](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L562) | 562 | `"10. MUST ألا تجمع تجارب المنتج بيانات حساسة بلا أساس أو تُفعّل تتبعًا خفيًا للمستخدم."` | — |
| [SRC-D17CE3D12F-L000563](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L563) | 563 | `""` | — |
| [SRC-D17CE3D12F-L000564](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L564) | 564 | `"## 39. توثيق المنتج والتشغيل والتغيير"` | — |
| [SRC-D17CE3D12F-L000565](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L565) | 565 | `""` | — |
| [SRC-D17CE3D12F-L000566](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L566) | 566 | `"1. MUST إبقاء README ومخططات المعمارية وملفات الإعداد متوافقة مع السلوك المثبت."` | — |
| [SRC-D17CE3D12F-L000567](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L567) | 567 | `"2. SHOULD وجود runbook مختصر لكل عطل معروف أو مهمة تشغيل مهمة."` | — |
| [SRC-D17CE3D12F-L000568](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L568) | 568 | `"3. MUST توثيق المتطلبات البيئية والأوامر الدقيقة لتثبيت واختبار وتشغيل التطبيق."` | — |
| [SRC-D17CE3D12F-L000569](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L569) | 569 | `"4. SHOULD الاحتفاظ بقاموس للمصطلحات والمقاييس وعقود البيانات المهمة."` | — |
| [SRC-D17CE3D12F-L000570](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L570) | 570 | `"5. MUST توثيق خطوات التراجع وعواقب ترحيل البيانات التي لا يمكن عكسها تلقائيًا."` | — |
| [SRC-D17CE3D12F-L000571](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L571) | 571 | `"6. SHOULD توثيق مسارات تصعيد المشكلة وحدود ما يستطيع النظام إثباته بنفسه."` | — |
| [SRC-D17CE3D12F-L000572](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L572) | 572 | `"7. MUST التعامل مع المستندات ككود قابل للمراجعة؛ تُراجع الروابط والأسماء والإصدارات بعد التغيير."` | — |
| [SRC-D17CE3D12F-L000573](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L573) | 573 | `"8. MUST إزالة الإرشادات القديمة المتعارضة أو وسمها بأنها تاريخية وغير صالحة للتنفيذ."` | — |
| [SRC-D17CE3D12F-L000574](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L574) | 574 | `"9. SHOULD وجود سجل معروف للقيود والديون التقنية والمخاطر، مع مالك أو أولوية أو موعد مراجعة."` | — |
| [SRC-D17CE3D12F-L000575](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L575) | 575 | `"10. MUST عدم استعمال التوثيق لإعلان قدرات لم تثبتها الاختبارات."` | — |
| [SRC-D17CE3D12F-L000576](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L576) | 576 | `""` | — |
| [SRC-D17CE3D12F-L000577](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L577) | 577 | `"---"` | — |
| [SRC-D17CE3D12F-L000578](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L578) | 578 | `""` | — |
| [SRC-D17CE3D12F-L000579](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L579) | 579 | `"# القسم الثالث عشر — النضج والأولويات ومعايير القبول"` | — |
| [SRC-D17CE3D12F-L000580](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L580) | 580 | `""` | — |
| [SRC-D17CE3D12F-L000581](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L581) | 581 | `"## 40. مستويات النضج"` | — |
| [SRC-D17CE3D12F-L000582](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L582) | 582 | `""` | — |
| [SRC-D17CE3D12F-L000583](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L583) | 583 | `"لا ينبغي تطبيق مستوى واحد على كل نظام. يُحدد المستوى لكل مجال حسب المخاطر والحاجة:"` | — |
| [SRC-D17CE3D12F-L000584](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L584) | 584 | `""` | — |
| [SRC-D17CE3D12F-L000585](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L585) | 585 | `"- **المستوى 0 — غير موصوف:** لا يوجد تعريف أو دليل كافٍ؛ الحالة UNKNOWN."` | — |
| [SRC-D17CE3D12F-L000586](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L586) | 586 | `"- **المستوى 1 — أساس مضبوط:** تعريف المتطلب، وسلوك آمن، واختبارات أساسية، ووثائق أولية."` | — |
| [SRC-D17CE3D12F-L000587](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L587) | 587 | `"- **المستوى 2 — متكرر ومقاس:** اختبارات تلقائية ملائمة، ومقاييس، وحدود، ومراجعة دورية."` | — |
| [SRC-D17CE3D12F-L000588](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L588) | 588 | `"- **المستوى 3 — إنتاجي مرن:** التعامل المختبر مع الفشل الجزئي، والاستعادة، والتغيير المتدرج، وعقود واضحة."` | — |
| [SRC-D17CE3D12F-L000589](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L589) | 589 | `"- **المستوى 4 — متكيف ومثبت:** قياس مستمر، واختبارات مخاطر آلية، ومراجعات نضج، وتحسينات مبنية على الحوادث والبيانات."` | — |
| [SRC-D17CE3D12F-L000590](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L590) | 590 | `""` | — |
| [SRC-D17CE3D12F-L000591](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L591) | 591 | `"لا يعني الوصول إلى المستوى الأعلى إضافة تقنيات أكثر. قد يكون النظام البسيط ذو الحدود والاختبارات الواضحة أنضج من نظام موزع غني بالأدوات ولا يمكن تشغيله بثقة."` | — |
| [SRC-D17CE3D12F-L000592](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L592) | 592 | `""` | — |
| [SRC-D17CE3D12F-L000593](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L593) | 593 | `"## 41. بوابة قبول تغيير مؤثر"` | — |
| [SRC-D17CE3D12F-L000594](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L594) | 594 | `""` | — |
| [SRC-D17CE3D12F-L000595](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L595) | 595 | `"قبل دمج تغيير مؤثر معماريًا أو أمنيًا أو تشغيليًا أو متعلقًا بالنموذج، يجب على المنفذ الإجابة على الأسئلة المنطبقة:"` | — |
| [SRC-D17CE3D12F-L000596](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L596) | 596 | `""` | — |
| [SRC-D17CE3D12F-L000597](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L597) | 597 | `"1. ما المشكلة أو الحاجة التي يعالجها التغيير؟"` | — |
| [SRC-D17CE3D12F-L000598](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L598) | 598 | `"2. ما المتطلب/الخطر/المقياس المرتبط به؟"` | — |
| [SRC-D17CE3D12F-L000599](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L599) | 599 | `"3. هل توجد طريقة أبسط؟"` | — |
| [SRC-D17CE3D12F-L000600](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L600) | 600 | `"4. ما الملفات والواجهات والبيانات التي تتأثر؟"` | — |
| [SRC-D17CE3D12F-L000601](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L601) | 601 | `"5. ما حدود الوقت والحجم والتوازي والتكلفة؟"` | — |
| [SRC-D17CE3D12F-L000602](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L602) | 602 | `"6. ماذا يحدث عند المدخل الخاطئ، وفشل المورد، وانقطاع الشبكة، ونفاد الحصة؟"` | — |
| [SRC-D17CE3D12F-L000603](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L603) | 603 | `"7. ما البيانات التي تُجمع أو تُرسل أو تُحذف؟"` | — |
| [SRC-D17CE3D12F-L000604](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L604) | 604 | `"8. ما الصلاحيات الجديدة التي يحتاجها التغيير؟"` | — |
| [SRC-D17CE3D12F-L000605](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L605) | 605 | `"9. كيف يُختبر النجاح والفشل والتداخل مع المستخدمين الآخرين؟"` | — |
| [SRC-D17CE3D12F-L000606](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L606) | 606 | `"10. كيف تتم المراقبة والتعطيل والتراجع؟"` | — |
| [SRC-D17CE3D12F-L000607](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L607) | 607 | `"11. ما الدليل الذي سيسمح بتغيير الحالة من PROPOSED إلى VERIFIED؟"` | — |
| [SRC-D17CE3D12F-L000608](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L608) | 608 | `"12. ما المعروف وما غير المعروف وما المخاطر المتبقية؟"` | — |
| [SRC-D17CE3D12F-L000609](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L609) | 609 | `"13. هل حدّثت الاختبارات والوثائق والمقاييس ذات الصلة؟"` | — |
| [SRC-D17CE3D12F-L000610](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L610) | 610 | `"14. هل يحافظ التغيير على صلاحية مدير المشروع في الدمج والنشر وقبول المخاطر؟"` | — |
| [SRC-D17CE3D12F-L000611](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L611) | 611 | `""` | — |
| [SRC-D17CE3D12F-L000612](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L612) | 612 | `"غياب إجابة مهمة لا يعني بالضرورة إلغاء التغيير؛ لكنه يعني أن الخطر يجب أن يصرح به ويُقبل بوضوح قبل توسيع نطاقه."` | — |
| [SRC-D17CE3D12F-L000613](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L613) | 613 | `""` | — |
| [SRC-D17CE3D12F-L000614](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L614) | 614 | `"## 42. قائمة مراجعة الإصدار"` | — |
| [SRC-D17CE3D12F-L000615](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L615) | 615 | `""` | — |
| [SRC-D17CE3D12F-L000616](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L616) | 616 | `"الإصدار المؤهل للإطلاق يجب أن يجتاز البوابات التي تنطبق عليه:"` | — |
| [SRC-D17CE3D12F-L000617](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L617) | 617 | `""` | — |
| [SRC-D17CE3D12F-L000618](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L618) | 618 | `"- **الصحة:** السلوك الأساسي واختبارات الانحدار والعقود."` | — |
| [SRC-D17CE3D12F-L000619](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L619) | 619 | `"- **الأمن:** الصلاحيات والأسرار والمدخلات غير الموثوقة ومراجعة المخاطر."` | — |
| [SRC-D17CE3D12F-L000620](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L620) | 620 | `"- **الذكاء الاصطناعي:** تقييم عربي مناسب، وحدود خطوات وأدوات، وعدم اختلاق المصادر."` | — |
| [SRC-D17CE3D12F-L000621](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L621) | 621 | `"- **البيانات:** سلامة المخططات والترحيلات والنسخ والاستعادة عند اللزوم."` | — |
| [SRC-D17CE3D12F-L000622](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L622) | 622 | `"- **الأداء:** قياسات للمسارات الحرجة وعدم وجود عيب معروف خطير."` | — |
| [SRC-D17CE3D12F-L000623](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L623) | 623 | `"- **التشغيل:** logs/metrics المناسبة، والتنبيه، وإجراءات التعطل."` | — |
| [SRC-D17CE3D12F-L000624](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L624) | 624 | `"- **التكلفة:** ميزانيات وحدود تمنع الاستهلاك غير المنضبط."` | — |
| [SRC-D17CE3D12F-L000625](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L625) | 625 | `"- **تجربة المستخدم:** واجهة واضحة وأخطاء مفهومة ووصولية/RTL مناسبة."` | — |
| [SRC-D17CE3D12F-L000626](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L626) | 626 | `"- **النشر:** إصدار معروف، وخطة إيقاف أو تراجع."` | — |
| [SRC-D17CE3D12F-L000627](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L627) | 627 | `"- **الحوكمة:** مراجعة diff، وسجل قرار، وموافقة بشرية على الدمج/النشر."` | — |
| [SRC-D17CE3D12F-L000628](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L628) | 628 | `""` | — |
| [SRC-D17CE3D12F-L000629](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L629) | 629 | `"لا يُطلب من كل تغيير صغير تكرار كل فحص شامل؛ يُستخدم تحليل أثر ومخاطر لتحديد ما يلزم. ولا يُسمح لتخفيف البوابات بأن يخفي خطرًا معروفًا."` | — |
| [SRC-D17CE3D12F-L000630](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L630) | 630 | `""` | — |
| [SRC-D17CE3D12F-L000631](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L631) | 631 | `"---"` | — |
| [SRC-D17CE3D12F-L000632](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L632) | 632 | `""` | — |
| [SRC-D17CE3D12F-L000633](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L633) | 633 | `""` | — |
| [SRC-D17CE3D12F-L000634](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L634) | 634 | `"---"` | — |
| [SRC-D17CE3D12F-L000635](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L635) | 635 | `""` | — |
| [SRC-D17CE3D12F-L000636](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L636) | 636 | `"# القسم الرابع عشر — طبقات المنصة والبنية التحتية وحدود الاستخدام"` | — |
| [SRC-D17CE3D12F-L000637](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L637) | 637 | `""` | — |
| [SRC-D17CE3D12F-L000638](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L638) | 638 | `"## 43. إدارة البنية التحتية والإعدادات ككود (IaC & Configuration Management)"` | — |
| [SRC-D17CE3D12F-L000639](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L639) | 639 | `""` | — |
| [SRC-D17CE3D12F-L000640](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L640) | 640 | `"عندما تتيح منصة التشغيل ذلك ويكون الأثر مناسبًا، يجب أن تكون البنية والإعدادات المهمة قابلة لإعادة الإنشاء والمراجعة بدل الاعتماد على تغييرات يدوية غير موثقة."` | — |
| [SRC-D17CE3D12F-L000641](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L641) | 641 | `""` | — |
| [SRC-D17CE3D12F-L000642](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L642) | 642 | `"1. SHOULD حفظ تعريف البنية القابل لإعادة الإنشاء ضمن نظام إصدارات، مع مراجعة التغييرات وبيان أثرها."` | — |
| [SRC-D17CE3D12F-L000643](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L643) | 643 | `"2. MUST فصل التكوين عن الشيفرة والأسرار، والتحقق من القيم المطلوبة عند بدء التشغيل."` | — |
| [SRC-D17CE3D12F-L000644](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L644) | 644 | `"3. MUST توفير إعدادات آمنة افتراضيًا، ورفض البدء أو تعطيل القدرة بوضوح عند فقد إعداد أمني ضروري؛ لا يُنشأ fallback ضعيف بصمت."` | — |
| [SRC-D17CE3D12F-L000645](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L645) | 645 | `"4. SHOULD استخدام بيئات منفصلة للاختبار والتجريب والإنتاج، أو توثيق الفروق عندما تفرض الاستضافة الصغيرة بيئة واحدة."` | — |
| [SRC-D17CE3D12F-L000646](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L646) | 646 | `"5. MUST ألا تستخدم الاختبارات مفاتيح إنتاج أو بيانات شخصية حقيقية دون حاجة وتفويض وضوابط."` | — |
| [SRC-D17CE3D12F-L000647](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L647) | 647 | `"6. SHOULD قياس واكتشاف انحراف الإعدادات بين المصدر والحالة الفعلية (configuration drift) متى أمكن."` | — |
| [SRC-D17CE3D12F-L000648](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L648) | 648 | `"7. MUST أن تكون تغييرات المنافذ والدومينات وCORS والجلسات وشهادات TLS والوصول الإداري مراجعة صريحة، لا تعديلات عرضية."` | — |
| [SRC-D17CE3D12F-L000649](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L649) | 649 | `"8. SHOULD أن يكون تشغيل التطبيق من بيئة جديدة موثقًا وقابلًا للتكرار قدر الإمكان."` | — |
| [SRC-D17CE3D12F-L000650](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L650) | 650 | `"9. MUST عدم تخزين state حساسة للبنية أو قيم runtime المتغيرة داخل المستودع إذا كان مكانها الصحيح خدمة تشغيل أو تخزين محميًا."` | — |
| [SRC-D17CE3D12F-L000651](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L651) | 651 | `"10. MUST تتضمن عملية إعادة الإنشاء أو النشر تحققًا من صحة البيئة والإعدادات قبل استقبال حركة المستخدمين."` | — |
| [SRC-D17CE3D12F-L000652](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L652) | 652 | `""` | — |
| [SRC-D17CE3D12F-L000653](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L653) | 653 | `"## 44. هندسة التخزين والاستعلامات والـ Cache"` | — |
| [SRC-D17CE3D12F-L000654](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L654) | 654 | `""` | — |
| [SRC-D17CE3D12F-L000655](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L655) | 655 | `"1. MUST تحديد متطلبات الاتساق والمعاملات والتنافس قبل اختيار مخزن البيانات أو تغيير نوعه."` | — |
| [SRC-D17CE3D12F-L000656](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L656) | 656 | `"2. SHOULD قياس الاستعلامات الحرجة وفحص الفهارس ونمط القراءة والكتابة وحدود اتصال المخزن قبل زيادة موارده أو تغييره."` | — |
| [SRC-D17CE3D12F-L000657](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L657) | 657 | `"3. MUST تحديد حدود connection pool والمهل وحجم النتائج والصفحات، ومعالجة فشل المخزن بوضوح."` | — |
| [SRC-D17CE3D12F-L000658](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L658) | 658 | `"4. MUST استخدام معاملات وقيود سلامة مناسبة لمنع البيانات الجزئية أو المتعارضة عند تعدد الكتابات."` | — |
| [SRC-D17CE3D12F-L000659](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L659) | 659 | `"5. SHOULD توثيق سياسة الـ cache: ما الذي يجوز تخزينه، ومدة صلاحيته، وكيف يبطل، وما الذي يحدث عند تعذر تحديثه."` | — |
| [SRC-D17CE3D12F-L000660](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L660) | 660 | `"6. MUST ألا تتجاوز الكاش سياسة الحداثة المطلوبة للسؤال؛ إذا قدّم النظام بيانات مخبأة بسبب عطل، يجب أن يراعي نوع المسألة وأن يصرّح بالقدم عندما يكون مهمًا."` | — |
| [SRC-D17CE3D12F-L000661](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L661) | 661 | `"7. MUST عزل الكاش بحسب المستخدم/المستأجر والصلاحيات والإصدار عند تخزين محتوى مخصص أو خاص."` | — |
| [SRC-D17CE3D12F-L000662](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L662) | 662 | `"8. MUST ألا يحتوي مفتاح cache على أسرار مكشوفة، ولا يسجل محتوى خاصًا ضمن metrics عالية الكاردينالية."` | — |
| [SRC-D17CE3D12F-L000663](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L663) | 663 | `"9. SHOULD ضبط حد أعلى للحجم والمدة وعدد العناصر، مع إخلاء (eviction) مفهوم وعدم اعتبار cache مخزنًا دائمًا."` | — |
| [SRC-D17CE3D12F-L000664](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L664) | 664 | `"10. MUST اختبار إبطال الكاش وتزامن التحديث والتكرار وفشل المخزن، لا الاكتفاء بحالة cache hit."` | — |
| [SRC-D17CE3D12F-L000665](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L665) | 665 | `"11. MUST ألا يؤدي تعطل cache قابل لإعادة البناء إلى فقد مصدر الحقيقة."` | — |
| [SRC-D17CE3D12F-L000666](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L666) | 666 | `"12. SHOULD توثيق خطط الانتقال من تخزين بسيط إلى مخزن أكثر قدرة وفق قياسات النمو ومتطلبات الاستعادة."` | — |
| [SRC-D17CE3D12F-L000667](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L667) | 667 | `""` | — |
| [SRC-D17CE3D12F-L000668](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L668) | 668 | `"## 45. الرسائل والأحداث والمهام غير المتزامنة"` | — |
| [SRC-D17CE3D12F-L000669](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L669) | 669 | `""` | — |
| [SRC-D17CE3D12F-L000670](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L670) | 670 | `"ينطبق هذا الجزء عندما تُدخل طوابير أو workers أو webhooks أو أحداثًا داخلية. ليس مطلوبًا إدخال وسيط رسائل الآن بلا حاجة."` | — |
| [SRC-D17CE3D12F-L000671](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L671) | 671 | `""` | — |
| [SRC-D17CE3D12F-L000672](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L672) | 672 | `"1. MUST تحديد مالك كل نوع حدث، ومخططه وإصداره ومتى يعد الحدث قد تم بنجاح."` | — |
| [SRC-D17CE3D12F-L000673](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L673) | 673 | `"2. MUST تصميم معالجة التكرار والتأخير والخروج عن الترتيب وفق خصائص الوسيط الفعلية."` | — |
| [SRC-D17CE3D12F-L000674](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L674) | 674 | `"3. SHOULD استخدام dead-letter queue أو سجل فشل قابل للفحص عند تكرار إخفاق معالجة مهمة، مع سياسة إعادة تشغيل آمنة."` | — |
| [SRC-D17CE3D12F-L000675](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L675) | 675 | `"4. MUST وضع حد لعدد مرات المحاولة وزمن بقاء المهمة وحجم الرسالة ومعدل استهلاك العمال."` | — |
| [SRC-D17CE3D12F-L000676](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L676) | 676 | `"5. MUST ألا تحتوي الرسائل على أسرار أو بيانات شخصية غير ضرورية، وأن تكون صلاحيات الوصول إلى الطابور محدودة."` | — |
| [SRC-D17CE3D12F-L000677](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L677) | 677 | `"6. SHOULD استخدام نمط outbox أو آلية اتساق مماثلة عندما يلزم توحيد كتابة البيانات وإصدار حدث مرتبط بها."` | — |
| [SRC-D17CE3D12F-L000678](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L678) | 678 | `"7. MUST ألا تعتبر الرسالة منجزة قبل ضمان حفظ حالة المعالجة وفق مستوى الديمومة المطلوب."` | — |
| [SRC-D17CE3D12F-L000679](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L679) | 679 | `"8. MUST وضع سياسة لإعادة معالجة الرسائل والمهام القديمة بعد تغيير الكود أو المخطط."` | — |
| [SRC-D17CE3D12F-L000680](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L680) | 680 | `"9. SHOULD جعل worker قابلاً للإيقاف المنضبط، وتحديد سلوك المهمة الجارية أثناء الإغلاق."` | — |
| [SRC-D17CE3D12F-L000681](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L681) | 681 | `"10. MUST مراقبة عمق الطابور، وعمر أقدم مهمة، ومعدل النجاح والفشل، ووقت الانتظار، واستهلاك العمال؛ ارتفاع عمق الطابور قد يكون فشلًا للمستخدم حتى إذا ظل الخادم حيًا."` | — |
| [SRC-D17CE3D12F-L000682](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L682) | 682 | `"11. MUST تطبيق حد تزامن وتغذية راجعة تمنع الطابور من إغراق قاعدة البيانات أو موفر النماذج."` | — |
| [SRC-D17CE3D12F-L000683](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L683) | 683 | `"12. SHOULD اختبار duplicate delivery والتأخير والتوقف وإعادة التشغيل وتلف الرسائل في بيئة آمنة."` | — |
| [SRC-D17CE3D12F-L000684](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L684) | 684 | `""` | — |
| [SRC-D17CE3D12F-L000685](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L685) | 685 | `"## 46. حدود الشبكة وتقديم المحتوى والواجهات الطرفية"` | — |
| [SRC-D17CE3D12F-L000686](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L686) | 686 | `""` | — |
| [SRC-D17CE3D12F-L000687](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L687) | 687 | `"1. MUST أن تظل حدود الثقة واضحة بين المتصفح والـ API والموفرين والروابط الخارجية؛ كل انتقال بيانات عبر الشبكة معرض لفشل أو تلاعب."` | — |
| [SRC-D17CE3D12F-L000688](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L688) | 688 | `"2. MUST استخدام إعدادات TLS موثوقة للواجهات العامة، وعدم تجاوز تحقق الشهادة في الإنتاج."` | — |
| [SRC-D17CE3D12F-L000689](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L689) | 689 | `"3. SHOULD الاستفادة من CDN أو التخزين المؤقت على الحافة للملفات العامة والثابتة فقط عندما تحقق قيمة؛ لا تُخزن ردود خاصة في cache عام."` | — |
| [SRC-D17CE3D12F-L000690](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L690) | 690 | `"4. MUST تمييز المحتوى العام القابل للتخزين عن ردود المستخدم والجلسات والبيانات الحساسة، مع رؤوس cache ملائمة."` | — |
| [SRC-D17CE3D12F-L000691](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L691) | 691 | `"5. SHOULD إضافة سياسة Content Security Policy وسياسات متصفح دفاعية مناسبة لطبيعة الواجهة، بعد اختبار عدم كسر الوظائف."` | — |
| [SRC-D17CE3D12F-L000692](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L692) | 692 | `"6. MUST حماية الطلبات التي تغير الحالة من CSRF عندما تعتمد المصادقة على cookies، مع إعدادات cookie مناسبة مثل Secure وHttpOnly وSameSite وفق الحالة."` | — |
| [SRC-D17CE3D12F-L000693](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L693) | 693 | `"7. MUST ألا يُعرض HTML أو SVG أو روابط قابلة للتنفيذ من مصدر خارجي دون تعقيم وسياسة آمنة؛ والأفضل إبقاء المحتوى نصًا غير نشط."` | — |
| [SRC-D17CE3D12F-L000694](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L694) | 694 | `"8. MUST التحقق من نوع المحتوى وطول الرد قبل التحليل، ومعالجة ملفات مضغوطة أو ردود ضخمة بطريقة تمنع استنزاف الموارد."` | — |
| [SRC-D17CE3D12F-L000695](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L695) | 695 | `"9. SHOULD فرض حدود على اتصالات الشبكة المفتوحة والانتظار وحجم الردود والتحويلات."` | — |
| [SRC-D17CE3D12F-L000696](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L696) | 696 | `"10. MUST حماية الروابط التي يراها المستخدم من الالتباس بين النص الظاهر والنطاق الحقيقي، خاصة مع أسماء نطاقات متشابهة أو أحرف Unicode المضللة."` | — |
| [SRC-D17CE3D12F-L000697](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L697) | 697 | `"11. SHOULD اختبار الواجهة على شبكة بطيئة وانقطاع مفاجئ وانتهاء الجلسة ووجود مزود غير متاح."` | — |
| [SRC-D17CE3D12F-L000698](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L698) | 698 | `"12. MUST ألا يُفسر نجاح TLS أو وصول HTTP على أنه دليل لصحة محتوى المصدر."` | — |
| [SRC-D17CE3D12F-L000699](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L699) | 699 | `""` | — |
| [SRC-D17CE3D12F-L000700](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L700) | 700 | `"## 47. مكافحة الإساءة والطلبات المؤتمتة واستنزاف الموارد"` | — |
| [SRC-D17CE3D12F-L000701](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L701) | 701 | `""` | — |
| [SRC-D17CE3D12F-L000702](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L702) | 702 | `"1. MUST تحليل طرق إساءة الاستخدام التي قد تستهلك حصص البحث أو النماذج أو التخزين، بما فيها loops الآلية وإعادة الطلب وتعدد الحسابات غير الطبيعي."` | — |
| [SRC-D17CE3D12F-L000703](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L703) | 703 | `"2. MUST وضع حدود متدرجة للطلبات مرتفعة الكلفة، ورفض أو تخفيض الخدمة بوضوح عند تجاوز الحد."` | — |
| [SRC-D17CE3D12F-L000704](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L704) | 704 | `"3. SHOULD تمييز الزيارات الطبيعية من الأنماط غير الطبيعية عبر إشارات محدودة ومحترمة للخصوصية، مع تجنب جمع بيانات زائدة."` | — |
| [SRC-D17CE3D12F-L000705](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L705) | 705 | `"4. MUST ألا يُعتمد على عنوان IP وحده كهوية أو آلية عدالة؛ قد يشترك مستخدمون كثيرون في عنوان واحد أو تتغير العناوين."` | — |
| [SRC-D17CE3D12F-L000706](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L706) | 706 | `"5. SHOULD توفير حد يومي/فترّي أو ميزانية لكل مستخدم أو جلسة عند انطباقها، مع حماية من إعادة ضبط العدادات بسهولة."` | — |
| [SRC-D17CE3D12F-L000707](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L707) | 707 | `"6. MUST وجود ضوابط متناسبة لمنع denial of service على المسارات المكلفة: سقف حجم، مهلة، حد تزامن، قائمة انتظار محدودة، وحدود للعمليات الخارجية."` | — |
| [SRC-D17CE3D12F-L000708](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L708) | 708 | `"7. SHOULD إيقاف القدرة المتضررة أو الموفر المستنزف عبر circuit breaker أو إعداد kill switch."` | — |
| [SRC-D17CE3D12F-L000709](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L709) | 709 | `"8. MUST ألا تُستخدم CAPTCHA أو المراقبة الشديدة تلقائيًا دون موازنة الوصولية والخصوصية والمخاطر."` | — |
| [SRC-D17CE3D12F-L000710](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L710) | 710 | `"9. MUST توثيق حدود الحماية التي توفرها منصة الاستضافة نفسها؛ لا يُفترض أن Omarai قادر على امتصاص هجوم حجمي كبير إذا كانت الاستضافة لا توفر ذلك."` | — |
| [SRC-D17CE3D12F-L000711](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L711) | 711 | `"10. MUST عدم الادعاء بحماية DDoS على مستوى الشبكة دون خدمة وشواهد فعلية؛ الضوابط داخل التطبيق لا تعوض سعة الحافة ومزود الشبكة."` | — |
| [SRC-D17CE3D12F-L000712](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L712) | 712 | `"11. SHOULD تضمين إساءة استخدام الوكلاء والموفرات ضمن مراقبة الكلفة والحوادث."` | — |
| [SRC-D17CE3D12F-L000713](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L713) | 713 | `"12. MUST عدم السماح لمستخدم غير موثق بتشغيل أعمال ضخمة أو تكرارية بلا حصص واضحة."` | — |
| [SRC-D17CE3D12F-L000714](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L714) | 714 | `""` | — |
| [SRC-D17CE3D12F-L000715](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L715) | 715 | `"## 48. تجربة المطوّر والمسارات القياسية الآمنة (Developer Experience / Paved Roads)"` | — |
| [SRC-D17CE3D12F-L000716](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L716) | 716 | `""` | — |
| [SRC-D17CE3D12F-L000717](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L717) | 717 | `"المنصة الناضجة تجعل المسار الصحيح أسهل من المسار الخاطئ، دون إجبار المشروع الصغير على بناء منصة داخلية مستقلة."` | — |
| [SRC-D17CE3D12F-L000718](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L718) | 718 | `""` | — |
| [SRC-D17CE3D12F-L000719](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L719) | 719 | `"1. SHOULD توفير مسار موثق من تعديل الكود إلى الاختبار إلى المراجعة إلى النشر، بأوامر ثابتة قدر الإمكان."` | — |
| [SRC-D17CE3D12F-L000720](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L720) | 720 | `"2. SHOULD وجود ملفات إعداد نموذجية خالية من الأسرار، ورسائل خطأ واضحة عند غياب المتطلبات."` | — |
| [SRC-D17CE3D12F-L000721](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L721) | 721 | `"3. MUST أن تكون تعليمات إنشاء بيئة التطوير والاختبار قابلة للتكرار، مع تثبيت إصدارات أو حدود متوافقة للاعتماديات الأساسية."` | — |
| [SRC-D17CE3D12F-L000722](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L722) | 722 | `"4. SHOULD تقديم قوالب للمكونات الجديدة تتضمن الحد الأدنى من العقود والاختبارات والسجلات والصلاحيات."` | — |
| [SRC-D17CE3D12F-L000723](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L723) | 723 | `"5. MUST أن يكون قالب الأداة/الموصل آمنًا افتراضيًا، ولا يمنح صلاحيات واسعة أو يرسل بيانات خاصة تلقائيًا."` | — |
| [SRC-D17CE3D12F-L000724](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L724) | 724 | `"6. SHOULD تسهيل التشغيل المحلي دون فرض اتصال بموفر مدفوع أو إنترنت عندما يمكن اختبار المنطق بمعزل عنه."` | — |
| [SRC-D17CE3D12F-L000725](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L725) | 725 | `"7. MUST فصل الاختبارات الحتمية المحلية عن اختبارات الخدمات الحقيقية، وشرح متطلبات الأخيرة."` | — |
| [SRC-D17CE3D12F-L000726](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L726) | 726 | `"8. SHOULD تقليل زمن feedback عبر تشغيل lint والاختبارات الصغيرة على كل تغيير، وترك الاختبارات الثقيلة لمسار مناسب."` | — |
| [SRC-D17CE3D12F-L000727](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L727) | 727 | `"9. MUST ألا يتطلب تشغيل المشروع معرفة خطوات غير موثقة أو تعديل أسرار داخل المصدر."` | — |
| [SRC-D17CE3D12F-L000728](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L728) | 728 | `"10. SHOULD استخدام توثيق ذاتي للخدمات والواجهات والمقاييس، مع تجنب إنشاء بوابة مطور كاملة قبل أن يكون حجم المكونات يبررها."` | — |
| [SRC-D17CE3D12F-L000729](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L729) | 729 | `"11. MUST الحفاظ على القدرة على تطوير Omarai من أدوات بسيطة، مع إمكانية ترقية المسار إلى CI/CD أكثر أتمتة دون إعادة كتابة بنية المشروع."` | — |
| [SRC-D17CE3D12F-L000730](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L730) | 730 | `"12. SHOULD قياس الاحتكاك المتكرر للمطورين وتحويل الخطوات اليدوية المعرضة للخطأ إلى فحوص آلية تدريجيًا."` | — |
| [SRC-D17CE3D12F-L000731](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L731) | 731 | `""` | — |
| [SRC-D17CE3D12F-L000732](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L732) | 732 | `"## 49. الحوكمة القانونية والتراخيص وسياسة المصادر المفتوحة"` | — |
| [SRC-D17CE3D12F-L000733](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L733) | 733 | `""` | — |
| [SRC-D17CE3D12F-L000734](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L734) | 734 | `"1. MUST مراجعة تراخيص الاعتماديات والمكونات والبيانات التي يُعاد توزيعها أو تضمينها، وفق شروط الاستخدام الفعلية."` | — |
| [SRC-D17CE3D12F-L000735](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L735) | 735 | `"2. MUST عدم إدراج نصوص أو بيانات أو نماذج أو ملفات ليست حقوق استخدامها واضحة في artifact منشور."` | — |
| [SRC-D17CE3D12F-L000736](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L736) | 736 | `"3. SHOULD الاحتفاظ بقائمة للاعتماديات المهمة ومصادرها وتراخيصها والتنبيهات المتعلقة بها."` | — |
| [SRC-D17CE3D12F-L000737](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L737) | 737 | `"4. MUST مراجعة شروط استخدام موفري النماذج والبحث بشأن الاحتفاظ بالبيانات والاستخدام التجاري وحدود الحصص والتوزيع، عند اختيار الموفر وتشغيله."` | — |
| [SRC-D17CE3D12F-L000738](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L738) | 738 | `"5. MUST عدم افتراض أن المحتوى المتاح عبر الويب خالٍ من حقوق النشر أو أن الوصول إليه يعني السماح بكل إعادة استخدام."` | — |
| [SRC-D17CE3D12F-L000739](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L739) | 739 | `"6. SHOULD توضيح نطاق مسؤولية Omarai ومحدودية الإجابات وإمكانية الخطأ للمستخدمين بما يناسب المخاطر وطبيعة المنتج."` | — |
| [SRC-D17CE3D12F-L000740](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L740) | 740 | `"7. MUST عدم تقديم المشورة على أنها بديل مهني مؤهل في المجالات عالية الأثر دون القيود والتحقق المناسبين."` | — |
| [SRC-D17CE3D12F-L000741](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L741) | 741 | `"8. SHOULD وضع سياسة إفصاح أمني للمشروع إذا أصبح مستعملًا من جمهور خارجي أو توجد بيانات مهمة معرضة."` | — |
| [SRC-D17CE3D12F-L000742](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L742) | 742 | `"9. MUST تحديد طريقة الإبلاغ عن الثغرات والجهة المسؤولة عن استلامها، ولو كانت قناة واحدة بسيطة في المرحلة الأولى."` | — |
| [SRC-D17CE3D12F-L000743](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L743) | 743 | `"10. MUST تقييم شروط نقل البيانات عبر الحدود والالتزامات القانونية التي تنطبق فعليًا على السوق والبيانات؛ لا يتم تبني استنتاجات قانونية عامة دون فحص."` | — |
| [SRC-D17CE3D12F-L000744](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L744) | 744 | `"11. SHOULD حفظ NOTICE/attribution عند الحاجة، وحذف المكونات التي لا تتوافق تراخيصها مع طريقة الاستخدام المقصودة."` | — |
| [SRC-D17CE3D12F-L000745](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L745) | 745 | `"12. MUST عدم الادعاء بالشهادة أو المطابقة القانونية بناءً على وجود هذه القائمة."` | — |
| [SRC-D17CE3D12F-L000746](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L746) | 746 | `""` | — |
| [SRC-D17CE3D12F-L000747](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L747) | 747 | `"## 50. حالة الخدمة والتواصل والثقة مع المستخدم"` | — |
| [SRC-D17CE3D12F-L000748](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L748) | 748 | `""` | — |
| [SRC-D17CE3D12F-L000749](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L749) | 749 | `"1. SHOULD أن يكون هناك وصف واضح لما يعمل وما لا يعمل في النسخة الحالية، دون خلط القدرات المخططة بالمثبتة."` | — |
| [SRC-D17CE3D12F-L000750](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L750) | 750 | `"2. SHOULD توفير رسالة حالة للمشكلات المعروفة أو حالة الطلب في الواجهة، حسب حجم المنتج وطبيعة الاعتمادية."` | — |
| [SRC-D17CE3D12F-L000751](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L751) | 751 | `"3. MUST أن تخبر رسائل الفشل المستخدم بما يمكنه فعله لاحقًا دون كشف التفاصيل الداخلية أو الأسرار."` | — |
| [SRC-D17CE3D12F-L000752](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L752) | 752 | `"4. MUST إظهار الفشل الجزئي عندما يؤثر على موثوقية الإجابة؛ لا تعرض إجابة ناقصة وكأن البحث اكتمل."` | — |
| [SRC-D17CE3D12F-L000753](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L753) | 753 | `"5. SHOULD وجود قناة ملاحظات أو إبلاغ عن الخطأ مع معلومات كافية لتشخيصه، وبأقل قدر من البيانات الخاصة."` | — |
| [SRC-D17CE3D12F-L000754](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L754) | 754 | `"6. MUST بيان ما إذا كانت المعلومة آنية أم مبنية على مصادر جرى جلبها، متى كان الفرق مهمًا للقرار."` | — |
| [SRC-D17CE3D12F-L000755](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L755) | 755 | `"7. SHOULD الاحتفاظ بسجل معروف للمشكلات والقيود التي تؤثر في المستخدمين وتحديثه عند إصلاحها."` | — |
| [SRC-D17CE3D12F-L000756](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L756) | 756 | `"8. MUST عدم وعود الدعم أو التوافر أو حفظ البيانات أو حذفها بأكثر مما توفره البنية فعلًا."` | — |
| [SRC-D17CE3D12F-L000757](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L757) | 757 | `"9. SHOULD عند وقوع حادث مؤثر، توضيح الأثر المعروف وما تم إصلاحه وما لا يزال مجهولًا."` | — |
| [SRC-D17CE3D12F-L000758](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L758) | 758 | `"10. MUST عدم إخفاء القيود التشغيلية من خلال لغة تسويقية مبالغ فيها."` | — |
| [SRC-D17CE3D12F-L000759](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L759) | 759 | `""` | — |
| [SRC-D17CE3D12F-L000760](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L760) | 760 | `""` | — |
| [SRC-D17CE3D12F-L000761](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L761) | 761 | `""` | — |
| [SRC-D17CE3D12F-L000762](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L762) | 762 | `"# القسم الخامس عشر — متطلبات هندسية عليا مكملة"` | — |
| [SRC-D17CE3D12F-L000763](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L763) | 763 | `""` | — |
| [SRC-D17CE3D12F-L000764](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L764) | 764 | `"## 51. التفكير المنظومي وتحليل حدود الخدمة"` | — |
| [SRC-D17CE3D12F-L000765](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L765) | 765 | `""` | — |
| [SRC-D17CE3D12F-L000766](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L766) | 766 | `"1. MUST تحليل النظام كتدفق عمل كامل لا كمجموعة ملفات منفصلة؛ فقد يكون السبب الجذري للفشل بين المكونات لا داخل وظيفة واحدة."` | — |
| [SRC-D17CE3D12F-L000767](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L767) | 767 | `"2. SHOULD رسم خريطة تدفق الطلب والبيانات والاعتماديات الخارجية لكل رحلة حرجة، وتحديد أين تُنشأ البيانات وأين تُتحقق وأين تُخزن وأين تُعرض."` | — |
| [SRC-D17CE3D12F-L000768](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L768) | 768 | `"3. MUST تحديد ما إذا كان كل مكوّن حرجًا أو اختياريًا، وتأثير فشله، وخيار التدهور عند تعذره."` | — |
| [SRC-D17CE3D12F-L000769](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L769) | 769 | `"4. SHOULD استخدام خريطة الاعتماديات لكشف النقاط المشتركة التي قد تسبب فشلًا متسلسلًا، مثل موفر واحد أو مخزن واحد أو إعداد واحد."` | — |
| [SRC-D17CE3D12F-L000770](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L770) | 770 | `"5. MUST تحديد مصدر الحقيقة والمسؤولية عن كل قرار حساس؛ لا تتوزع الصلاحية بين الواجهة والنموذج والأداة بصورة مبهمة."` | — |
| [SRC-D17CE3D12F-L000771](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L771) | 771 | `"6. MUST التحقق من حدود الثقة عبر كل انتقال بيانات، لا عند نقطة الدخول فقط."` | — |
| [SRC-D17CE3D12F-L000772](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L772) | 772 | `"7. SHOULD تحليل أثر التغيير خارج الملف الذي عُدل: العقود، والذاكرة، والتخزين، والسجلات، والتكلفة، والسلوك الظاهر للمستخدم."` | — |
| [SRC-D17CE3D12F-L000773](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L773) | 773 | `"8. MUST أن يكون لكل مسار حرج تعريف صريح للنجاح الجزئي والفشل الجزئي والنجاح الكامل."` | — |
| [SRC-D17CE3D12F-L000774](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L774) | 774 | `"9. SHOULD استخدام نموذج سياقي ومخطط حاويات/مكونات (مثل C4 أو بديل مبسط) عند وجود تعقيد يستدعي ذلك؛ لا يُطلب إنشاء رسومات ضخمة لبرنامج صغير."` | — |
| [SRC-D17CE3D12F-L000775](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L775) | 775 | `"10. MUST تحديث الخريطة أو وصف المعمارية عندما يصبح الرسم الحالي مضللًا بسبب تغيير مؤثر."` | — |
| [SRC-D17CE3D12F-L000776](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L776) | 776 | `""` | — |
| [SRC-D17CE3D12F-L000777](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L777) | 777 | `"## 52. تحليل المخاطر والتهديدات وسيناريوهات الإساءة"` | — |
| [SRC-D17CE3D12F-L000778](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L778) | 778 | `""` | — |
| [SRC-D17CE3D12F-L000779](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L779) | 779 | `"1. MUST إجراء Threat Modeling للتغييرات التي تضيف سطح وصول أو بيانات حساسة أو صلاحيات أو اتصالًا خارجيًا أو قدرة تنفيذ."` | — |
| [SRC-D17CE3D12F-L000780](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L780) | 780 | `"2. SHOULD تحديد الأصول والخصوم وحدود الثقة ومسارات الدخول والأثر المتوقع، باستخدام STRIDE أو أسلوب مكافئ عند فائدته."` | — |
| [SRC-D17CE3D12F-L000781](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L781) | 781 | `"3. MUST إضافة Abuse Cases بجانب Use Cases: كيف يمكن استخدام القدرة بطريقة صحيحة ظاهريًا لكنها تستنزف الموارد أو تسرّب بيانات أو تتجاوز السياسة؟"` | — |
| [SRC-D17CE3D12F-L000782](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L782) | 782 | `"4. MUST تقييم المخاطر عبر الشدة، واحتمال الحدوث، والتعرض، وصعوبة الكشف، وعدم اليقين في الأدلة؛ وتوثيق ما يظل مقبولًا ومن وافق عليه."` | — |
| [SRC-D17CE3D12F-L000783](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L783) | 783 | `"5. MUST إعطاء الأولوية للسيناريوهات التي تمس أسرارًا أو خصوصية أو تنفيذ فعل خارجي أو بيانات عدة مستخدمين أو تكلفة غير محدودة."` | — |
| [SRC-D17CE3D12F-L000784](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L784) | 784 | `"6. SHOULD مراجعة أثر التغيرات على الخصم الداخلي أو الحساب المخترق، لا المهاجم الخارجي فقط."` | — |
| [SRC-D17CE3D12F-L000785](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L785) | 785 | `"7. MUST تحويل حوادث وعيوب الإنتاج والحالات الهجومية المثبتة إلى اختبارات انحدار أو ضوابط منع تكرار."` | — |
| [SRC-D17CE3D12F-L000786](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L786) | 786 | `"8. MUST عدم اعتبار وجود فحص آلي أو قائمة عامة إلغاءً للضرورة من التفكير في التهديدات الخاصة بالنظام."` | — |
| [SRC-D17CE3D12F-L000787](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L787) | 787 | `"9. SHOULD مراجعة التهديدات دوريًا وعند تغيير مزود أو منصة استضافة أو نموذج أو صلاحيات أو نموذج بيانات."` | — |
| [SRC-D17CE3D12F-L000788](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L788) | 788 | `"10. MUST توثيق الافتراضات التي لو كانت خاطئة ستبطل الحماية، وتحديد طريقة للتحقق منها."` | — |
| [SRC-D17CE3D12F-L000789](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L789) | 789 | `""` | — |
| [SRC-D17CE3D12F-L000790](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L790) | 790 | `"## 53. Zero Trust وهوية المكونات والاتصالات الداخلية"` | — |
| [SRC-D17CE3D12F-L000791](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L791) | 791 | `""` | — |
| [SRC-D17CE3D12F-L000792](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L792) | 792 | `"ينطبق هذا القسم بدرجة تتناسب مع حقيقة أن النظام قد يبدأ بعملية واحدة ثم ينمو."` | — |
| [SRC-D17CE3D12F-L000793](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L793) | 793 | `""` | — |
| [SRC-D17CE3D12F-L000794](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L794) | 794 | `"1. MUST ألا تعتبر الشبكة الداخلية أو اتصالًا سابقًا أو اسم خدمة ضمانًا كافيًا للثقة."` | — |
| [SRC-D17CE3D12F-L000795](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L795) | 795 | `"2. MUST التحقق من هوية الطرف وصلاحيات العملية عند حدود الموارد الحساسة."` | — |
| [SRC-D17CE3D12F-L000796](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L796) | 796 | `"3. SHOULD استخدام هويات منفصلة للخدمات والعمال بدل مشاركة مفتاح إداري شامل."` | — |
| [SRC-D17CE3D12F-L000797](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L797) | 797 | `"4. MUST تحديد صلاحيات egress: ما النطاقات والبروتوكولات التي تستطيع كل أداة الوصول إليها؟ الاتصال الخارجي ليس حقًا مفتوحًا لكل مكوّن."` | — |
| [SRC-D17CE3D12F-L000798](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L798) | 798 | `"5. MUST منع انتقال صلاحيات المستخدم تلقائيًا إلى الأداة أو النموذج دون تفويض صريح وسياق قابل للتحقق."` | — |
| [SRC-D17CE3D12F-L000799](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L799) | 799 | `"6. SHOULD استخدام رموز قصيرة العمر أو هوية workload حيث تدعم المنصة ذلك."` | — |
| [SRC-D17CE3D12F-L000800](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L800) | 800 | `"7. MUST تسجيل محاولات الوصول المرفوضة بشكل مفيد دون تسجيل الأسرار أو المحتوى الحساس."` | — |
| [SRC-D17CE3D12F-L000801](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L801) | 801 | `"8. MUST أن يكون فشل التحقق من الهوية أو السياسة سببًا للرفض، لا سببًا لتخفيض الحماية."` | — |
| [SRC-D17CE3D12F-L000802](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L802) | 802 | `"9. SHOULD مراجعة الصلاحيات دوريًا وإزالة الوصول الذي لم تعد تحتاج إليه المكونات."` | — |
| [SRC-D17CE3D12F-L000803](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L803) | 803 | `"10. MUST ألا تدّعي المنظومة تطبيق Zero Trust لمجرد ذكر المصطلح؛ يُوثق النطاق والضوابط المختبرة."` | — |
| [SRC-D17CE3D12F-L000804](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L804) | 804 | `""` | — |
| [SRC-D17CE3D12F-L000805](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L805) | 805 | `"## 54. التوافر الجغرافي وتعدد المناطق وتوطين البيانات"` | — |
| [SRC-D17CE3D12F-L000806](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L806) | 806 | `""` | — |
| [SRC-D17CE3D12F-L000807](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L807) | 807 | `"هذا مستوى تطبيقي مشروط بالحاجة. لا يُطلب من نسخة أولية على استضافة مجانية بناء multi-region قبل وجود متطلبات تستدعي ذلك."` | — |
| [SRC-D17CE3D12F-L000808](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L808) | 808 | `""` | — |
| [SRC-D17CE3D12F-L000809](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L809) | 809 | `"1. MUST تحديد نقطة الفشل الواحدة المعروفة في كل قدرة حرجة، بما في ذلك التطبيق والمخزن وDNS والاستضافة والموفر الخارجي وحساب المالك."` | — |
| [SRC-D17CE3D12F-L000810](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L810) | 810 | `"2. SHOULD اختيار نمط الاستعادة وفق RTO/RPO والتكلفة وقيود مزودي الخدمة ومكان البيانات."` | — |
| [SRC-D17CE3D12F-L000811](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L811) | 811 | `"3. MUST تقييم أثر النسخ المتعدد على اتساق البيانات والتكرار والكمون والصلاحيات والفوترة."` | — |
| [SRC-D17CE3D12F-L000812](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L812) | 812 | `"4. SHOULD التمييز بين active-active وactive-passive والنسخ الاحتياطي والاستعادة؛ فهذه حلول مختلفة لا تُجمع في وصف واحد."` | — |
| [SRC-D17CE3D12F-L000813](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L813) | 813 | `"5. MUST ألا تُفعّل كتابة متعددة المناطق لبيانات مشتركة دون سياسة تعارض واتساق مُختبرة."` | — |
| [SRC-D17CE3D12F-L000814](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L814) | 814 | `"6. MUST تحديد متطلبات إقامة البيانات أو نقلها عبر الحدود عند انطباقها، وربط اختيار منطقة التشغيل بها."` | — |
| [SRC-D17CE3D12F-L000815](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L815) | 815 | `"7. SHOULD اختبار مسار التعافي عند انقطاع مكوّن أو منطقة متى كانت البنية تدعم ذلك وبما لا يعرض بيانات حقيقية للخطر."` | — |
| [SRC-D17CE3D12F-L000816](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L816) | 816 | `"8. MUST عدم إعلان التوافر العالي من مجرد تشغيل نسختين إذا كانت النسختان تشتركان في نقطة فشل حاسمة."` | — |
| [SRC-D17CE3D12F-L000817](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L817) | 817 | `"9. SHOULD تقييم الاعتماد الجغرافي على موفر بحث أو نموذج وخطة التدهور عند تعطل المنطقة أو الخدمة."` | — |
| [SRC-D17CE3D12F-L000818](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L818) | 818 | `"10. MUST أن تكون تكلفة التكرار الجغرافي مبررة بأهداف خدمة ومخاطر واضحة وموافقة صاحب المشروع."` | — |
| [SRC-D17CE3D12F-L000819](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L819) | 819 | `""` | — |
| [SRC-D17CE3D12F-L000820](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L820) | 820 | `"## 55. هندسة الفشل وتحليل الأوضاع والآثار (FMEA / Fault Tree)"` | — |
| [SRC-D17CE3D12F-L000821](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L821) | 821 | `""` | — |
| [SRC-D17CE3D12F-L000822](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L822) | 822 | `"1. SHOULD تطبيق تحليل أوضاع الفشل وآثارها على المسارات عالية الأثر: ما الذي قد يفشل؟ كيف يُكتشف؟ ما أثره؟ ما الضابط؟"` | — |
| [SRC-D17CE3D12F-L000823](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L823) | 823 | `"2. MUST تحديد سيناريوهات الفشل المتسلسل التي يُسببها بطء موفر أو امتلاء طابور أو استنزاف اتصالات أو إعادة محاولة غير مضبوطة."` | — |
| [SRC-D17CE3D12F-L000824](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L824) | 824 | `"3. SHOULD استخدام fault injection أو chaos experiments تدريجيًا في بيئة آمنة عندما تصبح الاعتمادية هدفًا مهمًا."` | — |
| [SRC-D17CE3D12F-L000825](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L825) | 825 | `"4. MUST عدم إجراء تجارب تخريبية على إنتاج حقيقي دون نطاق وموافقة وخطة إيقاف وتعافٍ."` | — |
| [SRC-D17CE3D12F-L000826](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L826) | 826 | `"5. MUST وضع شروط توقف للتجربة، مثل ارتفاع الأخطاء أو تجاوز زمن الاستعادة أو التأثير في البيانات."` | — |
| [SRC-D17CE3D12F-L000827](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L827) | 827 | `"6. SHOULD البدء باختبارات حتمية أصغر: قطع موفر وهمي، أو تأخير، أو رد مشوه، أو فقد اتصال مخزن."` | — |
| [SRC-D17CE3D12F-L000828](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L828) | 828 | `"7. MUST قياس زمن الاكتشاف والاحتواء والاستعادة في التمارين ذات الصلة بدل الاكتفاء بقول إن النظام «يتعافى»."` | — |
| [SRC-D17CE3D12F-L000829](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L829) | 829 | `"8. SHOULD تحويل الدروس المستخلصة إلى إجراء آلي أو اختبار يمنع تكرار السبب."` | — |
| [SRC-D17CE3D12F-L000830](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L830) | 830 | `"9. MUST فصل أعطال التطبيق عن أعطال المورد الخارجي في التشخيص والرسائل."` | — |
| [SRC-D17CE3D12F-L000831](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L831) | 831 | `"10. MUST توثيق ما لم يتم اختباره بعد وعدم تفسير غياب الحوادث على أنه إثبات للمرونة."` | — |
| [SRC-D17CE3D12F-L000832](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L832) | 832 | `""` | — |
| [SRC-D17CE3D12F-L000833](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L833) | 833 | `"## 56. دورة حياة API والحوكمة التعاقدية"` | — |
| [SRC-D17CE3D12F-L000834](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L834) | 834 | `""` | — |
| [SRC-D17CE3D12F-L000835](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L835) | 835 | `"1. MUST الاحتفاظ بعقد موثق لكل API عامة أو بينية مهمة، مع مالك وإصدار ومتطلبات المصادقة وحدود الموارد."` | — |
| [SRC-D17CE3D12F-L000836](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L836) | 836 | `"2. SHOULD استعمال مواصفة قابلة للقراءة الآلية مثل OpenAPI حيث يكون ذلك عمليًا."` | — |
| [SRC-D17CE3D12F-L000837](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L837) | 837 | `"3. MUST تعريف الدلالة، لا شكل JSON فقط: ماذا تعني حالات النجاح الجزئي؟ وما أخطاء الاستخدام؟ وما ضمانات الترتيب والتكرار؟"` | — |
| [SRC-D17CE3D12F-L000838](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L838) | 838 | `"4. MUST تصميم pagination وfiltering وsorting وحدود النتائج بطريقة تمنع ردودًا ضخمة أو تكاليف غير متوقعة."` | — |
| [SRC-D17CE3D12F-L000839](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L839) | 839 | `"5. MUST تعريف idempotency للعمليات التي قد تتكرر، ومعنى request ID وcorrelation ID بصورة واضحة."` | — |
| [SRC-D17CE3D12F-L000840](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L840) | 840 | `"6. SHOULD استخدام deprecation policy معلنة لتغيير العقود القديمة، مع إشعار واختبارات وتاريخ إزالة حين يكون ذلك مناسبًا."` | — |
| [SRC-D17CE3D12F-L000841](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L841) | 841 | `"7. MUST اختبار المصادقة والتفويض وحدود المستخدم على مستوى الكائن والعملية والحقول."` | — |
| [SRC-D17CE3D12F-L000842](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L842) | 842 | `"8. MUST ألا يعتمد النظام على إعدادات الواجهة لإخفاء قدرة غير مصرح بها في API."` | — |
| [SRC-D17CE3D12F-L000843](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L843) | 843 | `"9. SHOULD توفير أمثلة طلبات وردود وأخطاء واختبارات عقد قابلة للتشغيل."` | — |
| [SRC-D17CE3D12F-L000844](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L844) | 844 | `"10. MUST التحقق من الإصدارات القديمة التي ما زالت ضمن سياسة الدعم قبل الدمج."` | — |
| [SRC-D17CE3D12F-L000845](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L845) | 845 | `""` | — |
| [SRC-D17CE3D12F-L000846](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L846) | 846 | `"## 57. دورة حياة فهرس البحث والاسترجاع والمحتوى"` | — |
| [SRC-D17CE3D12F-L000847](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L847) | 847 | `""` | — |
| [SRC-D17CE3D12F-L000848](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L848) | 848 | `"1. MUST تعريف كيفية بناء فهارس البحث أو embeddings إن وجدت، وإصدار مخططها، ومصدر بياناتها، ووقت آخر تحديث، وطريقة إعادة البناء."` | — |
| [SRC-D17CE3D12F-L000849](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L849) | 849 | `"2. MUST فصل المصدر الأصلي عن النسخة المخزنة أو المقطعة أو المفهرسة؛ الفهرس قابل لإعادة البناء ولا يصبح مرجع الحقيقة تلقائيًا."` | — |
| [SRC-D17CE3D12F-L000850](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L850) | 850 | `"3. MUST ربط المقاطع المسترجعة بالمصدر الأصلي والمعرفات والإصدار، للحفاظ على provenance ومنع خلط الإصدارات."` | — |
| [SRC-D17CE3D12F-L000851](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L851) | 851 | `"4. SHOULD قياس freshness lag بين تحديث المصدر وانعكاسه في نتائج Omarai."` | — |
| [SRC-D17CE3D12F-L000852](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L852) | 852 | `"5. MUST تحديث أو إبطال نتائج cache والفهرس عند حذف مصدر أو سحب صلاحية الوصول إليه عندما يكون ذلك منطبقًا."` | — |
| [SRC-D17CE3D12F-L000853](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L853) | 853 | `"6. MUST أن تمنع حدود المستخدم/المستأجر الوصول إلى مستندات مفهرسة لا يملك إذنًا بها."` | — |
| [SRC-D17CE3D12F-L000854](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L854) | 854 | `"7. SHOULD اختبار retrieval quality على مجموعة أسئلة معروفة ومصادر داعمة، بما في ذلك حالات لا توجد فيها إجابة."` | — |
| [SRC-D17CE3D12F-L000855](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L855) | 855 | `"8. MUST التعامل مع محتوى قديم أو مقتطف ناقص أو صفحة خطأ باعتباره دليلًا ضعيفًا، لا نصًا موثوقًا."` | — |
| [SRC-D17CE3D12F-L000856](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L856) | 856 | `"9. MUST عدم نسخ أو تخزين المحتوى بما يخالف ضوابط الاستخدام وحقوق المصدر والسياسات المعلنة."` | — |
| [SRC-D17CE3D12F-L000857](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L857) | 857 | `"10. SHOULD حفظ metadata كافية لفهم سبب اختيار مصدر أو مقطع دون تجميع بيانات زائدة."` | — |
| [SRC-D17CE3D12F-L000858](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L858) | 858 | `""` | — |
| [SRC-D17CE3D12F-L000859](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L859) | 859 | `"## 58. حوكمة دورة حياة النموذج والبيانات والـ prompts"` | — |
| [SRC-D17CE3D12F-L000860](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L860) | 860 | `""` | — |
| [SRC-D17CE3D12F-L000861](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L861) | 861 | `"1. MUST تعريف هوية وإصدار النموذج والمزود وإعدادات الطلب الأساسية عند إجراء تقييم موثق."` | — |
| [SRC-D17CE3D12F-L000862](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L862) | 862 | `"2. SHOULD إدارة prompts الحرجة والـ tool schemas وسياسات الاسترجاع كأصول ذات إصدارات ومراجعة، لا نصوص مبعثرة بلا تاريخ."` | — |
| [SRC-D17CE3D12F-L000863](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L863) | 863 | `"3. MUST إجراء مراجعة للمخاطر قبل استخدام نموذج أو مزود أو مجموعة بيانات أو embedding جديد."` | — |
| [SRC-D17CE3D12F-L000864](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L864) | 864 | `"4. MUST تقييم اعتماديات سلسلة توريد الذكاء الاصطناعي، بما فيها SDKs والنماذج والأوزان والبيانات والموجهات وأدوات التقييم."` | — |
| [SRC-D17CE3D12F-L000865](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L865) | 865 | `"5. MUST عدم اعتبار ملف نموذج أو dataset موثوقًا لمجرد أنه نُشر في مستودع مشهور؛ تُراجع المصدر والترخيص والنزاهة والملاءمة."` | — |
| [SRC-D17CE3D12F-L000866](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L866) | 866 | `"6. SHOULD تسجيل تغييرات النموذج أو prompt مع النتيجة على مجموعة التقييم المرجعية."` | — |
| [SRC-D17CE3D12F-L000867](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L867) | 867 | `"7. MUST وضع خطة عند سحب نموذج أو تغير اسمه أو حدود سياقه أو سياسته أو سعره أو استجابته."` | — |
| [SRC-D17CE3D12F-L000868](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L868) | 868 | `"8. MUST حماية prompts الداخلية والبيانات السرية من أن تصبح مخرجات أو مدخلات لمزود بديل دون السماح."` | — |
| [SRC-D17CE3D12F-L000869](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L869) | 869 | `"9. SHOULD تقييم مخاطر poisoning وbackdoor والتلوث أو التسريب في بيانات الاسترجاع عندما يكون مصدرها قابلًا للتعديل الخارجي."` | — |
| [SRC-D17CE3D12F-L000870](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L870) | 870 | `"10. MUST أن تشمل مراجعة الذكاء الاصطناعي السلامة والأمن والخصوصية والجودة والتكلفة وسهولة تفسير أسباب القرار بقدر الحاجة."` | — |
| [SRC-D17CE3D12F-L000871](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L871) | 871 | `""` | — |
| [SRC-D17CE3D12F-L000872](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L872) | 872 | `"## 59. انحراف الجودة بعد النشر والمراقبة المستمرة للذكاء الاصطناعي"` | — |
| [SRC-D17CE3D12F-L000873](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L873) | 873 | `""` | — |
| [SRC-D17CE3D12F-L000874](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L874) | 874 | `"1. SHOULD تتبع مؤشرات الجودة على عينات مناسبة وبطريقة تحترم الخصوصية، مثل صحة الإسناد وكفاية الأدلة والرفض السليم ومعدل الإجابات غير المدعومة."` | — |
| [SRC-D17CE3D12F-L000875](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L875) | 875 | `"2. MUST عدم استنتاج تحسن الجودة من تغير نموذج أو prompt دون مقارنة منهجية."` | — |
| [SRC-D17CE3D12F-L000876](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L876) | 876 | `"3. SHOULD مراقبة تغيّر توزيع الأسئلة والمصادر وأنماط الفشل، مع الانتباه إلى أن تغير التوزيع ليس وحده إثبات تدهور."` | — |
| [SRC-D17CE3D12F-L000877](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L877) | 877 | `"4. MUST التمييز بين drift في البيانات، وتغير سلوك الموفر، وانتهاء حصص الخدمة، وتغير سياسة موفر خارجي."` | — |
| [SRC-D17CE3D12F-L000878](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L878) | 878 | `"5. SHOULD استخدام مراجعة بشرية لعينة من الإجابات والحالات ذات الأثر العالي عند عدم كفاية المقاييس الآلية."` | — |
| [SRC-D17CE3D12F-L000879](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L879) | 879 | `"6. MUST تعريف حد يوقف الإطلاق أو يرجع التغيير إذا ساءت مؤشرات حرجة."` | — |
| [SRC-D17CE3D12F-L000880](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L880) | 880 | `"7. MUST ألا تستخدم سجلات المستخدمين في التقييم أو التدريب الثانوي دون سياسة أساسها معروف ومناسب."` | — |
| [SRC-D17CE3D12F-L000881](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L881) | 881 | `"8. SHOULD اختبار الجودة عبر حالات عربية متنوعة ولهجات واختلافات كتابة، مع تجنب الادعاء بتمثيل كل المستخدمين بعينة صغيرة."` | — |
| [SRC-D17CE3D12F-L000882](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L882) | 882 | `"9. MUST تسجيل حجم العينة وفترة القياس ودرجة عدم اليقين؛ التقييم الآلي لا يعطي ضمانًا مطلقًا."` | — |
| [SRC-D17CE3D12F-L000883](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L883) | 883 | `"10. SHOULD إعادة اختبار التغيرات الخارجية الجوهرية مثل تغيير نموذج المورد أو محرك البحث أو tokenizer."` | — |
| [SRC-D17CE3D12F-L000884](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L884) | 884 | `""` | — |
| [SRC-D17CE3D12F-L000885](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L885) | 885 | `"## 60. البيانات الاصطناعية ومجموعات الاختبار وحماية بيانات الإنتاج"` | — |
| [SRC-D17CE3D12F-L000886](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L886) | 886 | `""` | — |
| [SRC-D17CE3D12F-L000887](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L887) | 887 | `"1. SHOULD تفضيل بيانات اختبار اصطناعية أو منقحة عند تطوير واختبار الميزات."` | — |
| [SRC-D17CE3D12F-L000888](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L888) | 888 | `"2. MUST عدم نسخ قاعدة الإنتاج إلى جهاز مطور أو منصة اختبار دون ضوابط وتصريح وحاجة واضحة."` | — |
| [SRC-D17CE3D12F-L000889](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L889) | 889 | `"3. MUST إزالة الأسرار والمعرفات والبيانات الشخصية من fixtures ولقطات الأخطاء وملفات التسجيل."` | — |
| [SRC-D17CE3D12F-L000890](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L890) | 890 | `"4. SHOULD امتلاك مجموعة اختبار ثابتة للإجابة العربية تشمل حقائق زمنية وأسئلة مبهمة ومصادر متعارضة ورفضًا صحيحًا وحقن تعليمات."` | — |
| [SRC-D17CE3D12F-L000891](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L891) | 891 | `"5. MUST فصل بيانات التقييم عن بيانات التطوير التي استعملت لصياغة نفس التوقعات، متى كانت الاستقلالية مهمة لتجنب التضخيم الوهمي للأداء."` | — |
| [SRC-D17CE3D12F-L000892](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L892) | 892 | `"6. SHOULD كشف التكرارات والتلوث بين مجموعات الاختبار لتقليل خطر النجاح المصطنع."` | — |
| [SRC-D17CE3D12F-L000893](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L893) | 893 | `"7. MUST أن تكون معايير نجاح التقييم محددة قبل تشغيله قدر الإمكان، لا متغيرة بعد رؤية النتيجة."` | — |
| [SRC-D17CE3D12F-L000894](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L894) | 894 | `"8. MUST حفظ النتائج والنسخة والإعدادات وبيئة التنفيذ التي أنتجتها."` | — |
| [SRC-D17CE3D12F-L000895](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L895) | 895 | `"9. SHOULD توفير طريقة لإزالة حالة اختبار أو إصلاح توقعها عند اكتشاف أن المرجع الأصلي قد تغير، مع توثيق التعديل."` | — |
| [SRC-D17CE3D12F-L000896](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L896) | 896 | `"10. MUST عدم إدخال مفاتيح حقيقية أو بيانات شخصية إلى prompt اختبار أو مستودع أمثلة."` | — |
| [SRC-D17CE3D12F-L000897](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L897) | 897 | `""` | — |
| [SRC-D17CE3D12F-L000898](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L898) | 898 | `"## 61. إدارة التغيير والطرح التدريجي والتجارب"` | — |
| [SRC-D17CE3D12F-L000899](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L899) | 899 | `""` | — |
| [SRC-D17CE3D12F-L000900](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L900) | 900 | `"1. MUST تعريف نطاق التغيير ومخاطره قبل الإطلاق، وتحديد كيفية معرفة أن التغيير نجح أو تسبب في تدهور."` | — |
| [SRC-D17CE3D12F-L000901](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L901) | 901 | `"2. SHOULD استخدام feature flags أو canary أو طرح تدريجي عندما تدعم البيئة ذلك وتبرره المخاطر."` | — |
| [SRC-D17CE3D12F-L000902](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L902) | 902 | `"3. MUST تعريف kill switch للميزات المكلفة أو المعرضة للإساءة أو التي تعتمد على موفر خارجي متغير، عندما يكون ذلك عمليًا."` | — |
| [SRC-D17CE3D12F-L000903](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L903) | 903 | `"4. MUST أن يكون إيقاف الميزة سريعًا وواضحًا دون تعديل ملفات عشوائية في الإنتاج."` | — |
| [SRC-D17CE3D12F-L000904](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L904) | 904 | `"5. SHOULD تحديد مدة مراجعة وإزالة feature flag المؤقتة؛ لا تُترك مفاتيح تجريبية دائمة بلا مالك."` | — |
| [SRC-D17CE3D12F-L000905](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L905) | 905 | `"6. MUST فصل تجربة المنتج عن تغيير صلاحيات الأمان أو شروط الخصوصية التي تحتاج موافقة مستقلة."` | — |
| [SRC-D17CE3D12F-L000906](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L906) | 906 | `"7. SHOULD تغيير عامل رئيسي واحد في التجربة عندما تكون ضرورة السببية مهمة، مع توثيق العوامل الأخرى."` | — |
| [SRC-D17CE3D12F-L000907](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L907) | 907 | `"8. MUST إيقاف التجربة عندما تتجاوز حدود الخطأ أو التكلفة أو الضرر المتفق عليها."` | — |
| [SRC-D17CE3D12F-L000908](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L908) | 908 | `"9. MUST عدم استخدام بيانات أو تجارب مضللة لإيهام المستخدم بأن الميزة موثوقة أو مكتملة."` | — |
| [SRC-D17CE3D12F-L000909](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L909) | 909 | `"10. SHOULD توثيق القرار بعد التجربة: اعتماد، أو تعديل، أو rollback، أو إلغاء، مع الأدلة."` | — |
| [SRC-D17CE3D12F-L000910](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L910) | 910 | `""` | — |
| [SRC-D17CE3D12F-L000911](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L911) | 911 | `"## 62. إدارة الثغرات والإفصاح الأمني ودورة الإصلاح"` | — |
| [SRC-D17CE3D12F-L000912](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L912) | 912 | `""` | — |
| [SRC-D17CE3D12F-L000913](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L913) | 913 | `"1. MUST توفير قناة واضحة للإبلاغ عن ثغرة عندما يصبح المشروع معرضًا لاستخدام خارجي أو بيانات مهمة."` | — |
| [SRC-D17CE3D12F-L000914](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L914) | 914 | `"2. MUST أن تصنف الثغرات بحسب الأثر وسهولة الاستغلال والتعرض، لا رقم أداة واحدة فقط."` | — |
| [SRC-D17CE3D12F-L000915](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L915) | 915 | `"3. SHOULD تعريف أزمنة استجابة مستهدفة حسب الشدة والموارد المتاحة، والإفصاح إن لم يكن الإصلاح فوريًا."` | — |
| [SRC-D17CE3D12F-L000916](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L916) | 916 | `"4. MUST حماية التفاصيل الحساسة للثغرة حتى يتوفر إصلاح أو خطة تخفيف مناسبة."` | — |
| [SRC-D17CE3D12F-L000917](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L917) | 917 | `"5. MUST تتضمن عملية الإصلاح اختبارًا يثبت الاستغلال قبل الإصلاح أو يعيد إنتاجه، واختبارًا يثبت المنع بعده متى أمكن."` | — |
| [SRC-D17CE3D12F-L000918](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L918) | 918 | `"6. SHOULD استخدام سياسة disclosure منسقة عند التعامل مع باحثين خارجيين ومزودي اعتماديات."` | — |
| [SRC-D17CE3D12F-L000919](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L919) | 919 | `"7. MUST تدوير الأسرار المتسربة وإزالة النسخ النشطة من الخدمات، لا حذفها من الملف الحالي فقط."` | — |
| [SRC-D17CE3D12F-L000920](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L920) | 920 | `"8. MUST تقييم الأثر التاريخي للتسريب؛ إزالة السر من آخر commit لا تمحو وجوده من تاريخ Git أو النسخ."` | — |
| [SRC-D17CE3D12F-L000921](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L921) | 921 | `"9. SHOULD إضافة فحوص آلية تمنع تكرار فئة الثغرات عندما يكون ذلك ممكنًا."` | — |
| [SRC-D17CE3D12F-L000922](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L922) | 922 | `"10. MUST عدم الادعاء «خالي من الثغرات»؛ يذكر نطاق الفحص وتاريخه وقيوده والثغرات المعروفة المتبقية."` | — |
| [SRC-D17CE3D12F-L000923](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L923) | 923 | `""` | — |
| [SRC-D17CE3D12F-L000924](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L924) | 924 | `"## 63. إدارة الاستمرارية المعرفية والفريق البشري"` | — |
| [SRC-D17CE3D12F-L000925](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L925) | 925 | `""` | — |
| [SRC-D17CE3D12F-L000926](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L926) | 926 | `"1. MUST حفظ القرارات الهندسية وقيود التشغيل وطريقة الاختبار واستعادة النظام داخل المستودع أو سجل موثوق، لا في ذاكرة محادثة فقط."` | — |
| [SRC-D17CE3D12F-L000927](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L927) | 927 | `"2. SHOULD أن يستطيع مساهم جديد فهم كيفية الاختبار والتشغيل وحدود النظام دون الاعتماد على شرح شفهي وحيد."` | — |
| [SRC-D17CE3D12F-L000928](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L928) | 928 | `"3. MUST أن تكون تعليمات الوكلاء والوثائق متوافقة مع الواقع؛ تحديث الدستور لا يغني عن تحديث runbooks وREADME عند تغيير التنفيذ."` | — |
| [SRC-D17CE3D12F-L000929](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L929) | 929 | `"4. SHOULD توثيق المهام الدورية: فحص الاعتماديات، ومراجعة الحصص، والتحقق من الروابط، واختبار الاستعادة، ومراجعة النتائج."` | — |
| [SRC-D17CE3D12F-L000930](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L930) | 930 | `"5. MUST توثيق أي إجراء يدوي عالي المخاطر بطريقة تقلل احتمال الخطأ عند تنفيذه."` | — |
| [SRC-D17CE3D12F-L000931](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L931) | 931 | `"6. SHOULD توفير مبدأ فصل الواجبات منطقيًا حتى عندما يكون المنفذ شخصًا واحدًا، عبر مراجعة لاحقة مستقلة أو فحوص تلقائية في التغييرات الحساسة."` | — |
| [SRC-D17CE3D12F-L000932](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L932) | 932 | `"7. MUST عدم إعطاء وكيل صلاحية اعتماد عمله بنفسه في الدمج أو النشر أو قبول المخاطر العالية."` | — |
| [SRC-D17CE3D12F-L000933](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L933) | 933 | `"8. SHOULD الاحتفاظ بمؤشرات تشغيل واضحة تُقلل العبء المعرفي وتساعد التشخيص."` | — |
| [SRC-D17CE3D12F-L000934](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L934) | 934 | `"9. MUST أن يكون هناك بديل تشغيلي مفهوم عند نفاد حصة موفر أو تعطل حساب أو غياب مطور لفترة."` | — |
| [SRC-D17CE3D12F-L000935](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L935) | 935 | `"10. SHOULD استخدام قوائم تحقق للمهام المتكررة، لا كبديل للفهم بل لتقليل النسيان."` | — |
| [SRC-D17CE3D12F-L000936](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L936) | 936 | `""` | — |
| [SRC-D17CE3D12F-L000937](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L937) | 937 | `"## 64. قابلية النقل وتجنب الارتباط القاتل بمزود (Portability / Exit Strategy)"` | — |
| [SRC-D17CE3D12F-L000938](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L938) | 938 | `""` | — |
| [SRC-D17CE3D12F-L000939](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L939) | 939 | `"1. MUST تحديد العناصر التي يصعب استبدالها: تنسيق البيانات، والنموذج، ومحرك البحث، والتخزين، والاستضافة، وإدارة الأسرار."` | — |
| [SRC-D17CE3D12F-L000940](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L940) | 940 | `"2. SHOULD تقليل استخدام APIs الخاصة بمزود داخل منطق الأعمال، مع عدم إخفاء الفروق الحقيقية بين الخدمات."` | — |
| [SRC-D17CE3D12F-L000941](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L941) | 941 | `"3. MUST توثيق ما يمكن نقله ووقت النقل المتوقع والبيانات التي لا يمكن استخراجها من الموفر إذا كان ذلك معروفًا."` | — |
| [SRC-D17CE3D12F-L000942](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L942) | 942 | `"4. SHOULD توفير تنسيق تصدير قابل للفهم للبيانات التي يملك المستخدم حق تصديرها."` | — |
| [SRC-D17CE3D12F-L000943](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L943) | 943 | `"5. MUST اختبار النسخ أو التصدير والاستعادة عند وجود بيانات لا تعوّض."` | — |
| [SRC-D17CE3D12F-L000944](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L944) | 944 | `"6. MUST ألا تكون المفاتيح أو سجلات القرار أو بيانات المصدر الوحيد قابلة للوصول عبر حساب موفر واحد فقط دون خطة استعادة."` | — |
| [SRC-D17CE3D12F-L000945](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L945) | 945 | `"7. SHOULD تحديد البديل عند توقف خدمة مجانية، أو تغير حصتها، أو إنهاء نموذج أو API."` | — |
| [SRC-D17CE3D12F-L000946](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L946) | 946 | `"8. MUST ألا يشترك fallback في نفس سبب الفشل الذي يعطل المسار الأساسي دون الإفصاح عن ذلك."` | — |
| [SRC-D17CE3D12F-L000947](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L947) | 947 | `"9. SHOULD تقييم تكاليف الخروج والاعتماد على تنسيقات احتكارية قبل الالتزام طويل المدى."` | — |
| [SRC-D17CE3D12F-L000948](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L948) | 948 | `"10. MUST توثيق القيود التي تفرضها الاستضافة الحالية وعدم وصف قابلية النقل بأنها كاملة دون تجربة فعلية."` | — |
| [SRC-D17CE3D12F-L000949](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L949) | 949 | `""` | — |
| [SRC-D17CE3D12F-L000950](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L950) | 950 | `"## 65. حوكمة المعايير والامتثال دون ادعاء الشهادة"` | — |
| [SRC-D17CE3D12F-L000951](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L951) | 951 | `""` | — |
| [SRC-D17CE3D12F-L000952](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L952) | 952 | `"1. MUST تسجيل اسم المعيار أو الدليل وإصداره وتاريخ آخر مراجعة عند استخدامه كأساس لتقييم."` | — |
| [SRC-D17CE3D12F-L000953](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L953) | 953 | `"2. MUST التفريق بين «مستوحى من معيار»، و«ضوابط مختارة من معيار»، و«تم تقييم نطاق محدد»، و«حاصل على شهادة رسمية»؛ هذه عبارات غير متكافئة."` | — |
| [SRC-D17CE3D12F-L000954](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L954) | 954 | `"3. SHOULD الاحتفاظ بخريطة ربط بين المتطلبات الداخلية والمرجعيات ذات الصلة لتقليل ازدواجية الفحوص."` | — |
| [SRC-D17CE3D12F-L000955](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L955) | 955 | `"4. MUST مراجعة الإصدارات المسودة والمنشورة والتغييرات الجوهرية قبل تحديث المتطلبات؛ لا يُعامل draft كمتطلب نهائي."` | — |
| [SRC-D17CE3D12F-L000956](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L956) | 956 | `"5. MUST تحديد نطاق التقييم والاستثناءات والأدلة والمخاطر المفتوحة."` | — |
| [SRC-D17CE3D12F-L000957](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L957) | 957 | `"6. SHOULD إجراء gap assessment قبل التزامات تعاقدية أو تنظيمية أو نشر واسع."` | — |
| [SRC-D17CE3D12F-L000958](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L958) | 958 | `"7. MUST ألا تُستخدم عبارة «متوافق مع NIST/OWASP/ISO» دون تحديد النطاق والأدلة ومتطلبات الطرف الذي يجيز ذلك الادعاء."` | — |
| [SRC-D17CE3D12F-L000959](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L959) | 959 | `"8. SHOULD إعادة التقييم عندما تتغير طبيعة البيانات أو السوق أو النموذج أو الاستضافة أو اعتماديات النظام الحرجة."` | — |
| [SRC-D17CE3D12F-L000960](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L960) | 960 | `"9. MUST أن تتناسب تكلفة الامتثال مع خطر المنتج والتزاماته الفعلية، دون إسقاط المتطلبات القانونية الواجبة."` | — |
| [SRC-D17CE3D12F-L000961](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L961) | 961 | `"10. MUST تحديث المستندات عند تغيير وضع أي مرجع رسمي بدل ترك رابط أو إصدار قديم كأنه لا يتغير."` | — |
| [SRC-D17CE3D12F-L000962](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L962) | 962 | `""` | — |
| [SRC-D17CE3D12F-L000963](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L963) | 963 | `"## 66. نمط التشغيل منخفض الموارد والعمل المحدود عند الانقطاع"` | — |
| [SRC-D17CE3D12F-L000964](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L964) | 964 | `""` | — |
| [SRC-D17CE3D12F-L000965](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L965) | 965 | `"يُصمم Omarai ليبدأ بموارد محدودة من دون جعل محدودية الموارد عذرًا لغياب الحدود أو الصدق."` | — |
| [SRC-D17CE3D12F-L000966](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L966) | 966 | `""` | — |
| [SRC-D17CE3D12F-L000967](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L967) | 967 | `"1. MUST أن يعمل المسار الأساسي بحدود صريحة للوقت والبحث والسياق والأدوات حتى لو كانت الاستضافة صغيرة أو مجانية."` | — |
| [SRC-D17CE3D12F-L000968](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L968) | 968 | `"2. SHOULD فصل القدرات التي تحتاج إنترنت أو مفاتيح أو موفرًا مدفوعًا عن منطق الاستقبال والتحقق وصياغة رسالة الخطأ."` | — |
| [SRC-D17CE3D12F-L000969](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L969) | 969 | `"3. MUST عندما يتعذر البحث، أن يبين النظام أن البحث الحي لم ينجح أو لم يحدث، ولا يقدم ادعاء «تحقق الآن» بلا مصدر حي."` | — |
| [SRC-D17CE3D12F-L000970](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L970) | 970 | `"4. SHOULD توفير سلوك محدود مفيد عندما يفشل موفر خارجي، مثل إجابة عامة واضحة الحدود أو عرض خطأ قابل للفهم، حسب نوع السؤال."` | — |
| [SRC-D17CE3D12F-L000971](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L971) | 971 | `"5. MUST عدم إعادة استخدام نتيجة مخبأة على أنها حديثة إذا كان السؤال يعتمد على الحداثة."` | — |
| [SRC-D17CE3D12F-L000972](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L972) | 972 | `"6. SHOULD إبقاء الاختبارات الحتمية قابلة للتشغيل دون استدعاء APIs مدفوعة كل مرة، مع فصل اختبارات الاتصال الحقيقي."` | — |
| [SRC-D17CE3D12F-L000973](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L973) | 973 | `"7. MUST أن يستطيع المشغل معرفة أي وظائف تعتمد على الإنترنت، وأي وظائف تعمل محليًا، وأي وظائف لم يثبت عملها."` | — |
| [SRC-D17CE3D12F-L000974](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L974) | 974 | `"8. SHOULD توفير طريقة لاختبار صحة الأداة end-to-end بأمر واضح ونتيجة فعلية، وعدم مساواة وجود الموصل بنجاح الاتصال."` | — |
| [SRC-D17CE3D12F-L000975](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L975) | 975 | `"9. MUST ألا تتحول قيود الموارد إلى حلقة تخطيط أو بحث أو retry بلا نهاية."` | — |
| [SRC-D17CE3D12F-L000976](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L976) | 976 | `"10. MUST أن تكون الترقية إلى موارد أكبر أو استضافة أخرى ممكنة دون تغيير معنى العقود أو إزالة ضوابط الأمان."` | — |
| [SRC-D17CE3D12F-L000977](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L977) | 977 | `""` | — |
| [SRC-D17CE3D12F-L000978](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L978) | 978 | `"---"` | — |
| [SRC-D17CE3D12F-L000979](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L979) | 979 | `""` | — |
| [SRC-D17CE3D12F-L000980](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L980) | 980 | `"# القسم السادس عشر — خريطة المرجعيات الخارجية"` | — |
| [SRC-D17CE3D12F-L000981](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L981) | 981 | `""` | — |
| [SRC-D17CE3D12F-L000982](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L982) | 982 | `"تُستخدم المرجعيات التالية لتوجيه المراجعة وتحويل المبادئ إلى فحوص مناسبة. يجب مراجعة الإصدار الرسمي الحالي عند استخدامها، وعدم نسخ ضوابطها آليًا دون فهم السياق."` | — |
| [SRC-D17CE3D12F-L000983](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L983) | 983 | `""` | — |
| [SRC-D17CE3D12F-L000984](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L984) | 984 | `"## أطر المعمارية والتشغيل"` | — |
| [SRC-D17CE3D12F-L000985](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L985) | 985 | `"- [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) — التميز التشغيلي والأمان والموثوقية وكفاءة الأداء والتكلفة والاستدامة."` | — |
| [SRC-D17CE3D12F-L000986](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L986) | 986 | `"- [Microsoft Azure Well-Architected Framework](https://learn.microsoft.com/en-us/azure/architecture/framework/) — موثوقية وأمان وتكلفة وتشغيل وأداء."` | — |
| [SRC-D17CE3D12F-L000987](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L987) | 987 | `"- [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework) — معمارية قابلة للتشغيل والقياس والتحسين والقدرة على التعافي."` | — |
| [SRC-D17CE3D12F-L000988](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L988) | 988 | `"- [Google SRE Books](https://sre.google/books/) — SLI/SLO وميزانيات الأخطاء والاستجابة للحوادث وتشغيل الخدمات."` | — |
| [SRC-D17CE3D12F-L000989](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L989) | 989 | `"- [DORA — Continuous Delivery](https://dora.dev/capabilities/continuous-delivery/) — إطلاق تغييرات بأمان وبسرعة وبصورة مستدامة."` | — |
| [SRC-D17CE3D12F-L000990](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L990) | 990 | `"- [CNCF Cloud Native Definition](https://github.com/cncf/toc/blob/main/DEFINITION.md) — مبادئ تشغيل قابل للتكرار على بيئات متنوعة؛ مرجع للفهم لا شرط لاستخدام تقنيات cloud-native."` | — |
| [SRC-D17CE3D12F-L000991](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L991) | 991 | `""` | — |
| [SRC-D17CE3D12F-L000992](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L992) | 992 | `"## الأمن والخصوصية وسلسلة التوريد"` | — |
| [SRC-D17CE3D12F-L000993](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L993) | 993 | `"- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)."` | — |
| [SRC-D17CE3D12F-L000994](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L994) | 994 | `"- [NIST Secure Software Development Framework (SSDF)](https://csrc.nist.gov/projects/ssdf)."` | — |
| [SRC-D17CE3D12F-L000995](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L995) | 995 | `"- [NIST Privacy Framework](https://www.nist.gov/privacy-framework)."` | — |
| [SRC-D17CE3D12F-L000996](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L996) | 996 | `"- [NIST SP 800-61 Rev. 3 — Incident Response](https://csrc.nist.gov/pubs/sp/800/61/r3/final)."` | — |
| [SRC-D17CE3D12F-L000997](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L997) | 997 | `"- [OWASP Application Security Verification Standard (ASVS)](https://owasp.org/www-project-application-security-verification-standard/)."` | — |
| [SRC-D17CE3D12F-L000998](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L998) | 998 | `"- [OWASP API Security Top 10](https://owasp.org/www-project-api-security/)."` | — |
| [SRC-D17CE3D12F-L000999](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L999) | 999 | `"- [OWASP GenAI Security Project](https://genai.owasp.org/)."` | — |
| [SRC-D17CE3D12F-L001000](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L1000) | 1000 | `"- [OWASP Artificial Intelligence Security Verification Standard (AISVS)](https://owasp.org/projects/artificial-intelligence-security-verification-standard-aisvs-docs)."` | — |
| [SRC-D17CE3D12F-L001001](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L1001) | 1001 | `"- [SLSA — Supply-chain Levels for Software Artifacts](https://slsa.dev/)."` | — |
| [SRC-D17CE3D12F-L001002](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L1002) | 1002 | `"- [GitHub — Secure use of Actions](https://docs.github.com/en/actions/reference/security/secure-use)."` | — |
| [SRC-D17CE3D12F-L001003](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L1003) | 1003 | `""` | — |
| [SRC-D17CE3D12F-L001004](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L1004) | 1004 | `"## الرصد والوصولية والتكلفة"` | — |
| [SRC-D17CE3D12F-L001005](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L1005) | 1005 | `"- [OpenTelemetry Documentation](https://opentelemetry.io/docs/) — توحيد traces وmetrics وlogs ومعانيها."` | — |
| [SRC-D17CE3D12F-L001006](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L1006) | 1006 | `"- [W3C Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/)."` | — |
| [SRC-D17CE3D12F-L001007](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L1007) | 1007 | `"- [FinOps Framework](https://www.finops.org/framework/) — مسؤولية استخدام الموارد وشفافية التكلفة وتحسينها."` | — |
| [SRC-D17CE3D12F-L001008](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L1008) | 1008 | `""` | — |
| [SRC-D17CE3D12F-L001009](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L1009) | 1009 | `"## الذكاء الاصطناعي وتقييم المخاطر"` | — |
| [SRC-D17CE3D12F-L001010](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L1010) | 1010 | `"- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — تحقق من الإصدار/المراجعة الرسمية الحالية قبل أي تقييم؛ تعرض الصفحة الرسمية حالة المراجعة والمستجدات."` | — |
| [SRC-D17CE3D12F-L001011](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L1011) | 1011 | `"- [NIST Generative AI Profile (NIST AI 600-1)](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) — مخاطر الذكاء الاصطناعي التوليدي ودورة حياته."` | — |
| [SRC-D17CE3D12F-L001012](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L1012) | 1012 | `"- [NIST Zero Trust Architecture (SP 800-207)](https://www.nist.gov/publications/zero-trust-architecture) — هوية المورد/العملية والتفويض عند الوصول إلى الموارد."` | — |
| [SRC-D17CE3D12F-L001013](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L1013) | 1013 | `"- [CISA Secure by Design](https://www.cisa.gov/securebydesign) — جعل الحماية والخيارات الآمنة جزءًا من تصميم المنتج."` | — |
| [SRC-D17CE3D12F-L001014](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L1014) | 1014 | `"- [NIST SSDF Publications](https://csrc.nist.gov/Projects/ssdf/publications) — يجب مراجعة حالة النسخة المنشورة أو المسودة قبل استخدامها كمتطلب رسمي؛ صفحة NIST تعرض حالة تحديثات SSDF."` | — |
| [SRC-D17CE3D12F-L001015](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L1015) | 1015 | `"- [Omarai Requirements Traceability and Maturity Model](OMARAI_REQUIREMENTS_TRACEABILITY_AND_MATURITY_MODEL_AR.md) — سجل المتطلبات، ومعايير الدليل، ومراجعات التخصصات، وبوابات القبول."` | — |
| [SRC-D17CE3D12F-L001016](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L1016) | 1016 | `"- [OWASP Top 10 for Large Language Model Applications](https://genai.owasp.org/llm-top-10/)."` | — |
| [SRC-D17CE3D12F-L001017](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L1017) | 1017 | `"- [OWASP AISVS](https://owasp.org/projects/artificial-intelligence-security-verification-standard-aisvs-docs)."` | — |
| [SRC-D17CE3D12F-L001018](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L1018) | 1018 | `""` | — |
| [SRC-D17CE3D12F-L001019](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L1019) | 1019 | `"### قاعدة استخدام المراجع"` | — |
| [SRC-D17CE3D12F-L001020](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L1020) | 1020 | `""` | — |
| [SRC-D17CE3D12F-L001021](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L1021) | 1021 | `"1. المرجع معيار/دليل لتصميم التقييم؛ ليس شهادة اعتماد."` | — |
| [SRC-D17CE3D12F-L001022](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L1022) | 1022 | `"2. عند اختيار بند منه، سجل اسم المرجع وإصداره وتاريخ المراجعة والنطاق الذي ينطبق."` | — |
| [SRC-D17CE3D12F-L001023](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L1023) | 1023 | `"3. لا تُعلن «متوافق مع معيار» إلا بعد تحديد المتطلبات المنطبقة وإجراء تقييم موثق وأدلة تحقق."` | — |
| [SRC-D17CE3D12F-L001024](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L1024) | 1024 | `"4. لا تتبع إصدارًا متغيرًا دون مراجعة أثر التحديث على الضوابط الحالية."` | — |
| [SRC-D17CE3D12F-L001025](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L1025) | 1025 | `"5. إذا تعارضت توصية عامة مع قيد موثق في Omarai، سجّل التعارض والقرار والسبب ولا تتجاهل التوصية بصمت."` | — |
| [SRC-D17CE3D12F-L001026](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L1026) | 1026 | `""` | — |
| [SRC-D17CE3D12F-L001027](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L1027) | 1027 | `"---"` | — |
| [SRC-D17CE3D12F-L001028](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L1028) | 1028 | `""` | — |
| [SRC-D17CE3D12F-L001029](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L1029) | 1029 | `"# الخلاصة الحاكمة"` | — |
| [SRC-D17CE3D12F-L001030](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L1030) | 1030 | `""` | — |
| [SRC-D17CE3D12F-L001031](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L1031) | 1031 | `"هذه الوثيقة توسع متطلبات Omarai إلى ما وراء كتابة الوظائف: فهي تشمل تصميم المنتج، والموثوقية، والسعة، والأمن، والخصوصية، والبيانات، والذكاء الاصطناعي، وتجربة المستخدم، وسلسلة توريد البرمجيات، والتسليم، والتعافي، والتكلفة، والحوكمة."` | — |
| [SRC-D17CE3D12F-L001032](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L1032) | 1032 | `""` | — |
| [SRC-D17CE3D12F-L001033](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L1033) | 1033 | `"لكن **لا توجد قائمة نهائية واحدة تشمل كل ممارسة ممكنة لدى كل منصة ضخمة**. الهدف الصحيح هو تغطية المجالات المعروفة ذات الصلة، وتحديد ما ينطبق منها على Omarai، ثم الانتقال من المتطلبات إلى التنفيذ والاختبارات والقياس. لا تساوي كثرة البنود النضج؛ النضج أن يكون لكل خطر مهم ضابط مناسب ودليل فعلي وخطة عند الفشل."` | — |
| [SRC-D17CE3D12F-L001034](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L1034) | 1034 | `""` | — |
| [SRC-D17CE3D12F-L001035](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L1035) | 1035 | `"كل بند جديد أو تعديل يجب أن يحافظ على القواعد التالية: **الأدلة قبل الادعاءات، الأمان قبل الصلاحيات الواسعة، الحدود قبل التوسع، القياس قبل التحسين، وخطة التراجع قبل الإطلاق عالي المخاطر.**"` | — |
## وثائق وفهرسة

### FILE-E1EAC11EFE — [docs/OMARAI_HANDOFF_CHECKLIST_AR.md](../OMARAI_HANDOFF_CHECKLIST_AR.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-E1EAC11EFE-L000001](../OMARAI_HANDOFF_CHECKLIST_AR.md#L1) | 1 | `"# Omarai — قائمة تسليم القبول والإغلاق"` | — |
| [SRC-E1EAC11EFE-L000002](../OMARAI_HANDOFF_CHECKLIST_AR.md#L2) | 2 | `""` | — |
| [SRC-E1EAC11EFE-L000003](../OMARAI_HANDOFF_CHECKLIST_AR.md#L3) | 3 | `"**تاريخ اللقطة:** 27 أكتوبر 2026 (بعد دمج PR #98 وفحوص CI اللاحقة)  "` | — |
| [SRC-E1EAC11EFE-L000004](../OMARAI_HANDOFF_CHECKLIST_AR.md#L4) | 4 | `"**الغرض:** قائمة موحدة لتسريع الإغلاق مع عدم تحويل الاختبارات الجزئية إلى ادعاء جاهزية.  "` | — |
| [SRC-E1EAC11EFE-L000005](../OMARAI_HANDOFF_CHECKLIST_AR.md#L5) | 5 | `"**سجل العيوب التفصيلي:** [OMARAI_REMEDIATION_REGISTER_AR.md](OMARAI_REMEDIATION_REGISTER_AR.md)  "` | — |
| [SRC-E1EAC11EFE-L000006](../OMARAI_HANDOFF_CHECKLIST_AR.md#L6) | 6 | ``"**الفهرسة المولدة:** لا تُعدّل ملفات `MASTER_INDEX.md` أو `SOURCE_LINES_INDEX.md` يدويًا؛ مصدرها `docs/generate_index.py`."`` | — |
| [SRC-E1EAC11EFE-L000007](../OMARAI_HANDOFF_CHECKLIST_AR.md#L7) | 7 | `""` | — |
| [SRC-E1EAC11EFE-L000008](../OMARAI_HANDOFF_CHECKLIST_AR.md#L8) | 8 | `"## مستجد التسليم — PR #98 وإصلاح هوية البناء"` | — |
| [SRC-E1EAC11EFE-L000009](../OMARAI_HANDOFF_CHECKLIST_AR.md#L9) | 9 | `""` | — |
| [SRC-E1EAC11EFE-L000010](../OMARAI_HANDOFF_CHECKLIST_AR.md#L10) | 10 | ``"- **PR #98 — MERGED:** [الرابط](https://github.com/mosabosama2030-oss/omarai/pull/98)، التزام الدمج `d9a8f83796547591d651c41ff657475bcec9b0ab`. أصبح Dockerfile يقبل `PUBLIC_OMARAI_BUILD_SHA` غير السري الذي تمرره SnapDeploy إلى البناء، ويختبر CI تطابق SHA في `/api/health`."`` | — |
| [SRC-E1EAC11EFE-L000011](../OMARAI_HANDOFF_CHECKLIST_AR.md#L11) | 11 | `"- **CI بعد الدمج — FIXED_AND_TESTED:** [#40471732289](https://github.com/mosabosama2030-oss/omarai/actions/runs/40471732289) و[تحديث الفهرس #40471732508](https://github.com/mosabosama2030-oss/omarai/actions/runs/40471732508) نجحا على SHA الدمج. ونجح PR CI على رأس التغيير في [#40471611641](https://github.com/mosabosama2030-oss/omarai/actions/runs/40471611641)."` | — |
| [SRC-E1EAC11EFE-L000012](../OMARAI_HANDOFF_CHECKLIST_AR.md#L12) | 12 | ``"- **هوية نسخة الاستضافة — NOT_CONFIRMED:** لا يزال `GET /api/health` يعرض `build.sha=unknown`. بعد اكتمال آخر تغييرات `main`، يلزم ضبط `PUBLIC_OMARAI_BUILD_SHA` في SnapDeploy على SHA النهائي ثم إعادة البناء والتحقق من مطابقة القيمة."`` | — |
| [SRC-E1EAC11EFE-L000013](../OMARAI_HANDOFF_CHECKLIST_AR.md#L13) | 13 | `"- **البحث الحي — NOT_RUN / BLOCKED:** لم تجتز جلسة المتصفح الاختبارية المصادقة؛ الرمز المحفوظ على جهاز المستخدم لا ينتقل تلقائيًا إلى ملف المتصفح الاختباري. أدخل الرمز بنفسك في واجهة Omarai من صفحة إعداد الملف الاختباري واحفظ الجلسة؛ لا ترسله في المحادثة. بعد نجاح المصادقة يجب تشغيل السؤال الأساسي، والبحث عن الموقع الرسمي في وضع «الأحدث الآن»، والبحث المعمق، وتوثيق المصادر المفتوحة."` | — |
| [SRC-E1EAC11EFE-L000014](../OMARAI_HANDOFF_CHECKLIST_AR.md#L14) | 14 | `"- لم يُنفّذ نشر يدوي من هذه الجلسة أو تعديل إعدادات SnapDeploy حتى الآن. نجاح CI لا يعني القبول الحي أو التشغيل بنسبة 100%."` | — |
| [SRC-E1EAC11EFE-L000015](../OMARAI_HANDOFF_CHECKLIST_AR.md#L15) | 15 | `""` | — |
| [SRC-E1EAC11EFE-L000016](../OMARAI_HANDOFF_CHECKLIST_AR.md#L16) | 16 | `"## خط الأساس الذي جرى التحقق منه"` | — |
| [SRC-E1EAC11EFE-L000017](../OMARAI_HANDOFF_CHECKLIST_AR.md#L17) | 17 | `""` | — |
| [SRC-E1EAC11EFE-L000018](../OMARAI_HANDOFF_CHECKLIST_AR.md#L18) | 18 | ``"- **`main` بعد دمج PR #95:** `3760418b5f32294faec7e49ef2cccb006419ee27`. أكمل تشغيل CI بعد الدمج [#40469019954](https://github.com/mosabosama2030-oss/omarai/actions/runs/40469019954) بنجاح على SHA نفسه؛ اكتملت اختبارات Python 3.11 و3.12 وبناء الحاوية واختبار API المحمي. اكتمل توليد الفهرس في [#40469019921](https://github.com/mosabosama2030-oss/omarai/actions/runs/40469019921)."`` | — |
| [SRC-E1EAC11EFE-L000019](../OMARAI_HANDOFF_CHECKLIST_AR.md#L19) | 19 | `"- **PR #94:** مدمج في 27 أكتوبر 2026؛ يحافظ وضع «الأحدث الآن» على نية العثور على موقع رسمي بدل توسيعها تلقائيًا إلى أخبار عامة. هذا إصلاح لمنطق خطة البحث، وليس إثباتًا لنجاح استرجاع الموقع حيًا."` | — |
| [SRC-E1EAC11EFE-L000020](../OMARAI_HANDOFF_CHECKLIST_AR.md#L20) | 20 | ``"- **PR #93:** أُغلق في 27 أكتوبر 2026 دون دمج، بعد التحقق من وصول تصحيحه إلى `main` ضمن PR #95. المرجع الصحيح في سجل المعالجة هو [CI #40395465598](https://github.com/mosabosama2030-oss/omarai/actions/runs/40395465598)، وليس تشغيل تحديث الفهرس #40395465626. لا حاجة لدمج الفرع القديم."`` | — |
| [SRC-E1EAC11EFE-L000021](../OMARAI_HANDOFF_CHECKLIST_AR.md#L21) | 21 | ``"- **PR #95:** **MERGED** في 27 أكتوبر 2026؛ التزام الدمج [#3760418b5f32294faec7e49ef2cccb006419ee27](https://github.com/mosabosama2030-oss/omarai/commit/3760418b5f32294faec7e49ef2cccb006419ee27). اجتاز رأس PR `07a4099da00ca2d506d3782615622361389f5171` تشغيل CI [#40467019476](https://github.com/mosabosama2030-oss/omarai/actions/runs/40467019476)؛ ثم اجتاز SHA الدمج CI في [#40469019954](https://github.com/mosabosama2030-oss/omarai/actions/runs/40469019954). هذا يثبت الفحوص الآلية فقط ولا يثبت سلامة البحث الحي."`` | — |
| [SRC-E1EAC11EFE-L000022](../OMARAI_HANDOFF_CHECKLIST_AR.md#L22) | 22 | ``"- **هوية نسخة الاستضافة:** لا تُعتبر مؤكدة حتى يُرجع `GET /api/health` قيمة `build.sha` تطابق SHA المعتمد بالضبط. ظهور `unknown` لا يثبت أن الاستضافة تشغل `main`."`` | — |
| [SRC-E1EAC11EFE-L000023](../OMARAI_HANDOFF_CHECKLIST_AR.md#L23) | 23 | ``"- **إعادة فحص الاستضافة (27 أكتوبر 2026):** الصفحة الرئيسية وواجهة Omarai وحقل السؤال ظهرت في المتصفح. في وضع «بحث معمّق»، انتهى السؤال «ما عاصمة مصر؟» برسالة: «رمز الوصول غير صحيح أو غير محفوظ. راجع رمز التطبيق المستضاف». وقراءة `GET /api/health` أعادت `ok=true` لكن `build.sha=unknown` و`sha_status=unknown`؛ كما تنص الاستجابة على أن فحص الشبكة الحي لم يُنفّذ وأن أعلام الجاهزية لا تثبت اتصال الموفرين أو اكتمال إجابة النموذج. لا يحسم الخطأ المرئي هل رمز التطبيق مفقود أم غير مطابق. لم تُدخل أو تُكشف أسرار، ولم تتغير إعدادات الاستضافة أو يحدث نشر."`` | — |
| [SRC-E1EAC11EFE-L000024](../OMARAI_HANDOFF_CHECKLIST_AR.md#L24) | 24 | ``"- **الاختبارات الحية المدفوعة/ذات الاستهلاك:** لا تُشغّل تلقائيًا. يتطلب فحص `POST /api/diagnostics` أو hosted smoke موافقة المشغّل، لأنهما قد يرسلان طلبات فعلية إلى موفر النموذج والبحث."`` | — |
| [SRC-E1EAC11EFE-L000025](../OMARAI_HANDOFF_CHECKLIST_AR.md#L25) | 25 | `""` | — |
| [SRC-E1EAC11EFE-L000026](../OMARAI_HANDOFF_CHECKLIST_AR.md#L26) | 26 | `"## إصلاح البحث المعمّق — اجتاز CI؛ القبول الحي ما زال متعطلًا"` | — |
| [SRC-E1EAC11EFE-L000027](../OMARAI_HANDOFF_CHECKLIST_AR.md#L27) | 27 | `""` | — |
| [SRC-E1EAC11EFE-L000028](../OMARAI_HANDOFF_CHECKLIST_AR.md#L28) | 28 | `"### الملاحظة البرمجية"` | — |
| [SRC-E1EAC11EFE-L000029](../OMARAI_HANDOFF_CHECKLIST_AR.md#L29) | 29 | `""` | — |
| [SRC-E1EAC11EFE-L000030](../OMARAI_HANDOFF_CHECKLIST_AR.md#L30) | 30 | ``"في `agents/web_agent.py`، يجمع `_collect_research` نتائج الاستعلامات المتوازية ويعالج استثناءات الموصلات المعتادة. لكن `RequestBudgetExceeded` الذي قد يصدر قبل بدء استعلام جديد لم يكن ضمن الاستثناءات المعالجة في حلقتَي البحث الأولي والتوسعة العميقة. قد يسمح ذلك لاستعلام واحد مستنفد للميزانية بإفشال تجميع البحث كله، وبالتالي إهدار نتائج اكتمل جمعها من استعلامات أخرى."`` | — |
| [SRC-E1EAC11EFE-L000031](../OMARAI_HANDOFF_CHECKLIST_AR.md#L31) | 31 | `""` | — |
| [SRC-E1EAC11EFE-L000032](../OMARAI_HANDOFF_CHECKLIST_AR.md#L32) | 32 | `"### التصحيح واختبارات الانحدار"` | — |
| [SRC-E1EAC11EFE-L000033](../OMARAI_HANDOFF_CHECKLIST_AR.md#L33) | 33 | `""` | — |
| [SRC-E1EAC11EFE-L000034](../OMARAI_HANDOFF_CHECKLIST_AR.md#L34) | 34 | `"- معالجة استثناء الميزانية على مستوى كل استعلام؛ تسجيل تحذير مع الاحتفاظ بنتائج الاستعلامات المكتملة."` | — |
| [SRC-E1EAC11EFE-L000035](../OMARAI_HANDOFF_CHECKLIST_AR.md#L35) | 35 | `"- إضافة اختبار دون اتصال لحالة فشل أحد الاستعلامات مع نجاح آخر."` | — |
| [SRC-E1EAC11EFE-L000036](../OMARAI_HANDOFF_CHECKLIST_AR.md#L36) | 36 | ``"- إضافة اختبار آخر يثبت بقاء الأدلة الأولية عندما تتعطل استعلامات التوسعة في وضع `deep`."`` | — |
| [SRC-E1EAC11EFE-L000037](../OMARAI_HANDOFF_CHECKLIST_AR.md#L37) | 37 | `"- التحقق الآلي مطلوب على Python 3.11 و3.12، وRuff، ومزامنة الفهرس، وبناء الحاوية واختبار API المحمي."` | — |
| [SRC-E1EAC11EFE-L000038](../OMARAI_HANDOFF_CHECKLIST_AR.md#L38) | 38 | `""` | — |
| [SRC-E1EAC11EFE-L000039](../OMARAI_HANDOFF_CHECKLIST_AR.md#L39) | 39 | ``"**الحالة بعد الدمج:** إصلاح الاحتفاظ بالأدلة الجزئية `FIXED_AND_TESTED` على CI قبل الدمج وبعده. يظل قبول البحث الحي `PARTIAL / BLOCKED` بسبب رسالة رمز الوصول من الاستضافة؛ كما لا تثبت هذه الاختبارات زوال كل احتمال لتعطل DNS/الشبكة أو صلاحية جميع الموفرين."`` | — |
| [SRC-E1EAC11EFE-L000040](../OMARAI_HANDOFF_CHECKLIST_AR.md#L40) | 40 | `""` | — |
| [SRC-E1EAC11EFE-L000041](../OMARAI_HANDOFF_CHECKLIST_AR.md#L41) | 41 | `"## بوابات التسليم النهائية"` | — |
| [SRC-E1EAC11EFE-L000042](../OMARAI_HANDOFF_CHECKLIST_AR.md#L42) | 42 | `""` | — |
| [SRC-E1EAC11EFE-L000043](../OMARAI_HANDOFF_CHECKLIST_AR.md#L43) | 43 | `"\| البوابة \| معيار القبول \| الحالة قبل تنفيذها \|"` | — |
| [SRC-E1EAC11EFE-L000044](../OMARAI_HANDOFF_CHECKLIST_AR.md#L44) | 44 | `"\|---\|---\|---\|"` | — |
| [SRC-E1EAC11EFE-L000045](../OMARAI_HANDOFF_CHECKLIST_AR.md#L45) | 45 | `"\| B1 — منطق البحث والميزانية \| اختبارات الانحدار الجديدة وكل مجموعة CI خضراء على SHA واحد؛ الاحتفاظ بالنتائج الجزئية عند نفاد الميزانية \| **FIXED_AND_TESTED آليًا**: CI ناجح على رأس PR #95 [#40467019476](https://github.com/mosabosama2030-oss/omarai/actions/runs/40467019476) وعلى SHA الدمج [#40469019954](https://github.com/mosabosama2030-oss/omarai/actions/runs/40469019954). قبول البحث الحي ما زال فاشلًا بسبب خطأ رمز الوصول المستضاف \|"` | — |
| [SRC-E1EAC11EFE-L000046](../OMARAI_HANDOFF_CHECKLIST_AR.md#L46) | 46 | `"\| B2 — أمان البحث \| استمرار التحقق من URL وDNS وSSRF، منع التحويلات غير المفحوصة، وعدم تجاوز تحديات anti-bot \| يجب ألا يتراجع بسبب الإصلاح \|"` | — |
| [SRC-E1EAC11EFE-L000047](../OMARAI_HANDOFF_CHECKLIST_AR.md#L47) | 47 | ``"\| B3 — هوية البناء \| `/api/health` يعيد SHA مطابقًا تمامًا لالتزام الإصدار الذي اختاره المدير \| **NOT_CONFIRMED**: `/api/health` يرد `ok=true` لكن `build.sha=unknown` و`sha_status=unknown`؛ يلزم إصدار يتضمن SHA قابلًا للتحقق \|"`` | — |
| [SRC-E1EAC11EFE-L000048](../OMARAI_HANDOFF_CHECKLIST_AR.md#L48) | 48 | `"\| B4 — قبول البحث الحي \| حفظ استجابة منفصلة لسؤال بسيط، وموقع رسمي في latest، وبحث معمّق، وسؤال حديث؛ وتسجيل الاستعلامات والموفرين والصفحات المقروءة والأخطاء \| **FAILED / PARTIAL**: اختبار واحد فقط «ما عاصمة مصر؟» في وضع deep أظهر رسالة خطأ رمز الوصول؛ لم تكتمل الإجابة، ولم تُنفذ بقية السيناريوهات \|"` | — |
| [SRC-E1EAC11EFE-L000049](../OMARAI_HANDOFF_CHECKLIST_AR.md#L49) | 49 | `"\| B5 — قبول الإجابات \| الروابط تفتح، النص الكامل يُقرأ عند الإمكان، الإجابة ترتبط بالأدلة؛ يصرّح النظام بعدم كفاية الأدلة بدل اختلاقها \| يتطلب فحصًا يدويًا لعينة حية \|"` | — |
| [SRC-E1EAC11EFE-L000050](../OMARAI_HANDOFF_CHECKLIST_AR.md#L50) | 50 | `"\| B6 — واجهة الهاتف \| RTL، التحميل، الفشل وإعادة المحاولة، عدم إظهار نجاح الاتصال كأنه نجاح بحث، وروابط المصادر على Android \| **PARTIAL**: ظهرت الواجهة وحقل السؤال في جلسة المتصفح؛ لم يكتمل الطلب بسبب خطأ رمز الوصول، ولم يُنجز قبول بصري كامل على Android \|"` | — |
| [SRC-E1EAC11EFE-L000051](../OMARAI_HANDOFF_CHECKLIST_AR.md#L51) | 51 | `"\| B7 — الأمان والتشغيل \| إعادة مراجعة مستقلة، حماية رمز الوصول، حدود التزامن والطلبات، وعدم كشف المفاتيح أو بيانات المستخدم \| اختبارات CI لا تغلق الاختبارات الحمراء الحية \|"` | — |
| [SRC-E1EAC11EFE-L000052](../OMARAI_HANDOFF_CHECKLIST_AR.md#L52) | 52 | ``"\| B8 — البيانات الدائمة \| إذا استُخدم مخزن العملاء: إثبات دوام `OMARAI_DB_PATH` والنسخ والاستعادة على المضيف الفعلي؛ وإلا يُترك الجزء غير مستخدم \| `NOT_RUN` على مضيف فعلي \|"`` | — |
| [SRC-E1EAC11EFE-L000053](../OMARAI_HANDOFF_CHECKLIST_AR.md#L53) | 53 | `"\| B9 — التوثيق والفهرس \| مصدر واحد لسجل العيوب، مخرجات الفهرس مولدة من البرنامج النصي، وعدم تكرار سجلات إصلاح متعارضة \| يُفحص في CI \|"` | — |
| [SRC-E1EAC11EFE-L000054](../OMARAI_HANDOFF_CHECKLIST_AR.md#L54) | 54 | `""` | — |
| [SRC-E1EAC11EFE-L000055](../OMARAI_HANDOFF_CHECKLIST_AR.md#L55) | 55 | `"## الاختبارات العملية بعد الموافقة على النشر"` | — |
| [SRC-E1EAC11EFE-L000056](../OMARAI_HANDOFF_CHECKLIST_AR.md#L56) | 56 | `""` | — |
| [SRC-E1EAC11EFE-L000057](../OMARAI_HANDOFF_CHECKLIST_AR.md#L57) | 57 | `"نفّذ على المضيف المعتمد فقط وبعد اختيار SHA المراد تسليمه:"` | — |
| [SRC-E1EAC11EFE-L000058](../OMARAI_HANDOFF_CHECKLIST_AR.md#L58) | 58 | `""` | — |
| [SRC-E1EAC11EFE-L000059](../OMARAI_HANDOFF_CHECKLIST_AR.md#L59) | 59 | ``"1. **سؤال بسيط:** `ما عاصمة مصر؟` — يسجل ما إذا كانت إجابة المعرفة العامة أو إجابة البحث، ولا يخلط بينهما."`` | — |
| [SRC-E1EAC11EFE-L000060](../OMARAI_HANDOFF_CHECKLIST_AR.md#L60) | 60 | ``"2. **بحث ملاحي حديث:** `ابحث عن الموقع الرسمي لوزارة الاتصالات وتكنولوجيا المعلومات المصرية` مع اختيار «الأحدث الآن» — يجب أن يكون الرابط من الموقع الرسمي نفسه، لا مجرد خبر صحفي عن الوزارة."`` | — |
| [SRC-E1EAC11EFE-L000061](../OMARAI_HANDOFF_CHECKLIST_AR.md#L61) | 61 | `"3. **بحث معمّق:** سؤال محدد يتطلب عدة مصادر مختلفة — سجل عدد الاستعلامات التي جرى تشغيلها، عدد النتائج المقبولة والمرفوضة، الصفحات التي قُرئ نصها، وسبب أي استنفاد للميزانية."` | — |
| [SRC-E1EAC11EFE-L000062](../OMARAI_HANDOFF_CHECKLIST_AR.md#L62) | 62 | `"4. **طلب حديث مستقل:** خبر رسمي أو قرار حديث ذو تاريخ معلوم — لا يُقبل المقتطف وحده كقراءة صفحة، ويجب عرض تاريخ النشر عندما يكون متاحًا."` | — |
| [SRC-E1EAC11EFE-L000063](../OMARAI_HANDOFF_CHECKLIST_AR.md#L63) | 63 | `""` | — |
| [SRC-E1EAC11EFE-L000064](../OMARAI_HANDOFF_CHECKLIST_AR.md#L64) | 64 | ``"احفظ نسخة من الاستجابة المهيكلة لكل تجربة، بما فيها `search_report` و`request_budget` و`warnings` و`sources`. احذف أو احجب أي سؤال خاص أو رمز أو بيانات لا يحتاجها سجل القبول."`` | — |
| [SRC-E1EAC11EFE-L000065](../OMARAI_HANDOFF_CHECKLIST_AR.md#L65) | 65 | `""` | — |
| [SRC-E1EAC11EFE-L000066](../OMARAI_HANDOFF_CHECKLIST_AR.md#L66) | 66 | `"## المطلوب لاستكمال القبول"` | — |
| [SRC-E1EAC11EFE-L000067](../OMARAI_HANDOFF_CHECKLIST_AR.md#L67) | 67 | `""` | — |
| [SRC-E1EAC11EFE-L000068](../OMARAI_HANDOFF_CHECKLIST_AR.md#L68) | 68 | ``"- تم دمج PR #95 بعد نجاح CI على رأسه، ثم نجاح CI على SHA الدمج `3760418...`؛ رابط التشغيل النهائي [#40469019954](https://github.com/mosabosama2030-oss/omarai/actions/runs/40469019954)."`` | — |
| [SRC-E1EAC11EFE-L000069](../OMARAI_HANDOFF_CHECKLIST_AR.md#L69) | 69 | ``"- تم إغلاق PR #93 دون دمج بعد التحقق من تضمين تصحيحه في `main`."`` | — |
| [SRC-E1EAC11EFE-L000070](../OMARAI_HANDOFF_CHECKLIST_AR.md#L70) | 70 | `"- الخطوة المعلقة الآن: راجع لوحة SnapDeploy وسجلات الخدمة للتحقق من إعداد رمز وصول التطبيق. لا ترسل قيمة الرمز في المحادثة، ولا تغيّر الإعدادات أو تنشر نسخة دون موافقة منفصلة."` | — |
| [SRC-E1EAC11EFE-L000071](../OMARAI_HANDOFF_CHECKLIST_AR.md#L71) | 71 | `"- بعد إصلاح سبب الخطأ بموافقة مدير الاستضافة، يلزم إذن منفصل لأي إعادة اختبار قد تستهلك أرصدة؛ لا يُعلن نجاح القبول حتى تستجيب الأسئلة فعليًا وتثبت هوية البناء."` | — |
| [SRC-E1EAC11EFE-L000072](../OMARAI_HANDOFF_CHECKLIST_AR.md#L72) | 72 | `"- لا تعتبر Omarai جاهزًا للتسليم حتى تُغلق البوابات التي تنطبق على نطاق الاستخدام وتُوثّق البوابات غير المنفذة كقيود معروفة."` | — |
| [SRC-E1EAC11EFE-L000073](../OMARAI_HANDOFF_CHECKLIST_AR.md#L73) | 73 | `""` | — |
| [SRC-E1EAC11EFE-L000074](../OMARAI_HANDOFF_CHECKLIST_AR.md#L74) | 74 | ``"**قاعدة الإغلاق:** `FIXED_AND_TESTED` تعني إصلاحًا واختبارًا على SHA معروف؛ `PARTIAL` يعني دليلًا جزئيًا؛ `NOT_RUN` يعني أن الاختبار لم يُنفذ؛ `UNKNOWN` يعني أن الأدلة لا تسمح بالحكم. لا تعني أي منها ضمنًا أن الخدمة المستضافة قد نُشرت أو قبلت."`` | — |
## وثائق وفهرسة

### FILE-9A0DFA994E — [docs/OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-9A0DFA994E-L000001](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L1) | 1 | `"# فهم اللغة الطبيعية وتخطيط المهمة في Omarai"` | — |
| [SRC-9A0DFA994E-L000002](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L2) | 2 | `""` | — |
| [SRC-9A0DFA994E-L000003](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L3) | 3 | `"## الغرض"` | — |
| [SRC-9A0DFA994E-L000004](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L4) | 4 | `""` | — |
| [SRC-9A0DFA994E-L000005](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L5) | 5 | `"تضيف هذه الطبقة تمثيلًا منظمًا لمقصد السؤال وقيوده واحتياجات الأدلة واستراتيجيات البحث. وهي تكمل التوجيه الحتمي، وسياق الحوار، ومخطط البحث؛ ولا تستبدلها بمحرك واحد يدّعي فهم كل شيء."` | — |
| [SRC-9A0DFA994E-L000006](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L6) | 6 | `""` | — |
| [SRC-9A0DFA994E-L000007](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L7) | 7 | `"الملفات الرئيسية:"` | — |
| [SRC-9A0DFA994E-L000008](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L8) | 8 | `""` | — |
| [SRC-9A0DFA994E-L000009](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L9) | 9 | ``"- `agents/task_understanding.py`: تطبيع النص، عائلات المهام، القيود الصريحة، فرضيات التفسير، احتياجات الأدلة، ومصفوفة استراتيجيات البحث."`` | — |
| [SRC-9A0DFA994E-L000010](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L10) | 10 | ``"- `agents/intent_router.py`: يحدد المسار الأولي مثل LOCAL وCLARIFY وMODEL_ONLY وWEB_SIMPLE وWEB_DEEP وLEAD_GENERATION."`` | — |
| [SRC-9A0DFA994E-L000011](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L11) | 11 | ``"- `agents/dialogue_state.py`: يحد من توريث سياق الرسائل السابقة ويتحقق من تفسير المتابعة."`` | — |
| [SRC-9A0DFA994E-L000012](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L12) | 12 | ``"- `agents/aspect_planning.py`: يستخرج محاور الأسئلة المركبة وينشئ سجلًا لفظيًا لمحاور الأدلة."`` | — |
| [SRC-9A0DFA994E-L000013](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L13) | 13 | ``"- `agents/research.py`: ينشئ الخطة الاحتياطية ويتحقق من خطة النموذج ويربطها بمواصفة المهمة."`` | — |
| [SRC-9A0DFA994E-L000014](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L14) | 14 | ``"- `agents/web_agent.py`: يطبق سقف الاستعلامات النهائي، وينفذ البحث، ويعيد حواجز قبول المصدر بعد إصلاح الأدلة، ويصدر تشخيصات مراحل التنفيذ."`` | — |
| [SRC-9A0DFA994E-L000015](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L15) | 15 | `""` | — |
| [SRC-9A0DFA994E-L000016](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L16) | 16 | `"## مواصفة المهمة TaskSpec"` | — |
| [SRC-9A0DFA994E-L000017](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L17) | 17 | `""` | — |
| [SRC-9A0DFA994E-L000018](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L18) | 18 | ``"تنتج `build_task_spec` سجلًا محدودًا تحت المخطط `omarai.task_spec.v1`. يشمل:"`` | — |
| [SRC-9A0DFA994E-L000019](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L19) | 19 | `""` | — |
| [SRC-9A0DFA994E-L000020](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L20) | 20 | `"1. **عائلة المهمة الرئيسية** مثل المقارنة، والمعلومات الحالية، والموقع الرسمي، وآراء الناس، والشرح، وحل المشكلات، والتوصية، والتلخيص، والعملاء المحتملين، والصحة والقانون، والبرمجة، وتحليل البيانات، والحساب، والترجمة، والكتابة والتحرير، والتخطيط، والإبداع."` | — |
| [SRC-9A0DFA994E-L000021](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L21) | 21 | `"2. **القيود الصريحة** مثل البلد والسنة والتاريخ والميزانية والروابط ومحاور المقارنة واللغة الظاهرة في النص."` | — |
| [SRC-9A0DFA994E-L000022](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L22) | 22 | `"3. **متطلبات الدليل** مثل قراءة الصفحة فعلًا، والحصول على تاريخ حديث، وتفضيل المصدر الأولي، وفصل تجربة المستخدم عن الإعلان، ومراعاة الاختصاص القانوني أو المرجع الصحي عند انطباقهما."` | — |
| [SRC-9A0DFA994E-L000023](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L23) | 23 | `"4. **متطلبات الأدوات** بوصفها احتياجات تخطيطية محدودة؛ لا تمنح تصريحًا لتشغيل أداة غير مُعدة أو غير مسموح بها."` | — |
| [SRC-9A0DFA994E-L000024](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L24) | 24 | `"5. **فرضيات التفسير الثانوية** والإشارات النصية التي تدعمها. أعداد الإشارات تشخيصية، وليست احتمالات معايرة أو درجات صحة."` | — |
| [SRC-9A0DFA994E-L000025](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L25) | 25 | `"6. **سياق الحوار المطبّع**: هل الرسالة متابعة؟ ما الموضوع والكيانات والخانات التي جرى توريثها؟ هل حدث تغيير موضوع؟ وما أساس الحل؟ تحفظ الحقول بحجم محدود."` | — |
| [SRC-9A0DFA994E-L000026](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L26) | 26 | `"7. **تفضيلات شكل الإجابة** مثل الإيجاز أو التفصيل أو الأمثلة أو الجدول أو النقاط أو الصيغة JSON أو طلب المصادر والروابط أو الشرح المبسط للمبتدئ."` | — |
| [SRC-9A0DFA994E-L000027](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L27) | 27 | `"8. **مدخلات إلزامية ناقصة** مثل اسم الجهة لطلب موقع رسمي، أو النص/الرابط المطلوب تلخيصه. يمكن لمسار التشغيل أن يطلب توضيحًا قبل استدعاء الموصلات بدل البحث عن موضوع مخمّن."` | — |
| [SRC-9A0DFA994E-L000028](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L28) | 28 | `"9. **فحوص القرار** التي تفرض التحقق من صلاحية الأداة، وحدود الاستعلامات والوقت، وصلتها بالموضوع، وسياسة المصدر، والتفريق بين الاستعلام المخطط والمنفذ، وبين نجاح الموصل وصلاحية الدليل، وعدم اتباع تعليمات مزروعة في صفحات مسترجعة."` | — |
| [SRC-9A0DFA994E-L000029](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L29) | 29 | `""` | — |
| [SRC-9A0DFA994E-L000030](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L30) | 30 | `"لا تضيف المواصفة موقعًا جغرافيًا أو ميزانية أو تاريخًا لم يذكره المستخدم. مفردات المواقع والكيانات المدعومة حاليًا محدودة وقابلة للتوسعة، وليست محلل كيانات عالميًا. قائمة متطلبات الأدوات وصفية وليست إذن تنفيذ؛ تُفلتر النسخة التي تُعرض للتشخيص بقائمة سماح للحقول والأدوات المعروفة."` | — |
| [SRC-9A0DFA994E-L000031](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L31) | 31 | `""` | — |
| [SRC-9A0DFA994E-L000032](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L32) | 32 | `"## عائلات الاستفسارات والقيود المتراكبة"` | — |
| [SRC-9A0DFA994E-L000033](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L33) | 33 | `""` | — |
| [SRC-9A0DFA994E-L000034](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L34) | 34 | `"العائلة الرئيسية لا تلغي القيود الأخرى. مثلًا، سؤال «قارن تجارب الملاك في مصر اليوم» قد يتطلب في الوقت نفسه:"` | — |
| [SRC-9A0DFA994E-L000035](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L35) | 35 | `""` | — |
| [SRC-9A0DFA994E-L000036](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L36) | 36 | `"- جمع أدلة مقارنة لكل محور صريح؛"` | — |
| [SRC-9A0DFA994E-L000037](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L37) | 37 | `"- بحثًا اجتماعيًا عن منشورات عامة؛"` | — |
| [SRC-9A0DFA994E-L000038](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L38) | 38 | `"- تاريخ نشر أو تحديث مناسبًا لأن السؤال مرتبط باليوم؛"` | — |
| [SRC-9A0DFA994E-L000039](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L39) | 39 | `"- الحفاظ على السوق المحلي المذكور؛"` | — |
| [SRC-9A0DFA994E-L000040](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L40) | 40 | `"- تمييز منشور تجربة شخصية محتملة عن ترويج تجاري؛"` | — |
| [SRC-9A0DFA994E-L000041](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L41) | 41 | `"- الامتناع عن تحويل عينة صغيرة إلى حكم عام على كل الملاك."` | — |
| [SRC-9A0DFA994E-L000042](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L42) | 42 | `""` | — |
| [SRC-9A0DFA994E-L000043](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L43) | 43 | `"هذه القيود مستقلة في المواصفة، وتُضاف متطلبات البحث الحديثة والاجتماعية والمقارنة معًا عند انطباقها. وينطبق النمط نفسه على المجالات الأخرى: المقارنة قد تحتاج بحثًا متعدد المعايير، والصحة تميّز المعلومات العامة من التشخيص الشخصي، والقانون يحتفظ بالاختصاص وتاريخ النفاذ، والبرمجة تفصل الخطأ المرصود عن فرضيات السبب، وتحليل البيانات يحافظ على تعريف المقياس ودرجة جودة البيانات. أما طلب «الموقع الرسمي» فهو بحث عن وجهة وليس بحثًا عن خبر حديث، حتى عند اختيار واجهة Latest؛ لا يثبت امتداد النطاق وحده ملكية الجهة."` | — |
| [SRC-9A0DFA994E-L000044](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L44) | 44 | `""` | — |
| [SRC-9A0DFA994E-L000045](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L45) | 45 | `"## مصفوفة استراتيجية البحث"` | — |
| [SRC-9A0DFA994E-L000046](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L46) | 46 | `""` | — |
| [SRC-9A0DFA994E-L000047](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L47) | 47 | ``"تسجل `build_query_strategy_matrix` الاستعلامات المخططة مع وسم الاستراتيجية والسبب. ويمكن أن تتضمن:"`` | — |
| [SRC-9A0DFA994E-L000048](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L48) | 48 | `""` | — |
| [SRC-9A0DFA994E-L000049](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L49) | 49 | `"- استعلام الموضوع الأساسي؛"` | — |
| [SRC-9A0DFA994E-L000050](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L50) | 50 | `"- استعلامًا لكل معيار مقارنة صريح؛"` | — |
| [SRC-9A0DFA994E-L000051](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L51) | 51 | `"- بحثًا عن مصدر أولي أو دليل فني؛"` | — |
| [SRC-9A0DFA994E-L000052](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L52) | 52 | `"- صياغة عربية وإنجليزية عند فائدتها؛"` | — |
| [SRC-9A0DFA994E-L000053](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L53) | 53 | `"- استعلامات تجارب شخصية ومناقشات متباينة في البحث الاجتماعي؛"` | — |
| [SRC-9A0DFA994E-L000054](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L54) | 54 | `"- استعلامات عن إعلان رسمي حديث وتاريخ النشر عند طلب المعلومات الحالية؛"` | — |
| [SRC-9A0DFA994E-L000055](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L55) | 55 | `"- بحثًا عن الأعراض والأسباب المحتملة ودليل الشركة في الاستكشاف الفني للأعطال."` | — |
| [SRC-9A0DFA994E-L000056](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L56) | 56 | `""` | — |
| [SRC-9A0DFA994E-L000057](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L57) | 57 | `"الحد الحالي هو ثمانية استعلامات كحد أقصى للخطة الموسعة، مع ميزانية أصغر للاستعلامات الاعتيادية. تتبع الاستعلامات إزالة التكرار وتطبيعًا محدودًا. تُحفظ بذرة الخطة أولًا، ثم تُعطى الأولوية لاستراتيجيات الدليل الخاصة بالمهمة قبل بدائل المخطط الثانوية، حتى لا تستهلك الاستعلامات العامة كل الميزانية. لا يغيّر سجل الاستراتيجيات بنفسه قائمة الاستعلامات التنفيذية؛ يختار مسار التشغيل النهائي ما ينفذ ضمن الوضع والميزانية الفعليين. يُحفظ استعلام المتابعة الذي حلّ السياق حتى لو اختلف لفظه عن السؤال القصير."` | — |
| [SRC-9A0DFA994E-L000058](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L58) | 58 | `""` | — |
| [SRC-9A0DFA994E-L000059](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L59) | 59 | ``"وجود استراتيجية في المصفوفة لا يعني أن الاستعلام أُرسل إلى محرك بحث. الحقول `actual_queries` و`actual_query_count` تصف الخطة التي وصلت إلى مسار التنفيذ، بينما توضح حالة البحث وتشخيصات الموصلات ما يمكن إثبات أنه نُفذ فعليًا."`` | — |
| [SRC-9A0DFA994E-L000060](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L60) | 60 | `""` | — |
| [SRC-9A0DFA994E-L000061](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L61) | 61 | `"## التعامل مع السياق والالتباس"` | — |
| [SRC-9A0DFA994E-L000062](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L62) | 62 | `""` | — |
| [SRC-9A0DFA994E-L000063](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L63) | 63 | `"- السؤال المستقل يظل مستقلًا ولا يرث موضوعًا قديمًا لمجرد وجود تاريخ محادثة."` | — |
| [SRC-9A0DFA994E-L000064](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L64) | 64 | `"- سؤال المتابعة المختصر يمكن ربطه بالموضوع السابق إذا كان له مرجع واضح."` | — |
| [SRC-9A0DFA994E-L000065](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L65) | 65 | `"- إذا كان المرجع غير محلول، فالنتيجة المطلوبة هي الاستيضاح بدل اختراع موضوع والبحث عنه."` | — |
| [SRC-9A0DFA994E-L000066](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L66) | 66 | `"- قبل التخطيط والبحث، يكتشف فحص أولي محدود حالتين ملزمتين: غياب الجهة المطلوبة للموقع الرسمي، وغياب كل من الرابط والنص عند طلب تلخيص. لا يفرض هذا الفحص توضيحًا لكل تفضيل اختياري."` | — |
| [SRC-9A0DFA994E-L000067](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L67) | 67 | `"- يمكن للتفسير الدلالي القائم على النموذج اقتراح متابعة، لكن التحقق الحتمي يحد من حجم النص والقيم المنقولة، ولا يمنحه سلطة تنفيذ أداة."` | — |
| [SRC-9A0DFA994E-L000068](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L68) | 68 | `"- تُطبع العربية بإزالة التشكيل والتطويل وتوحيد بعض الحروف، مع مطابقة على حدود الكلمات وصيغ لواصق شائعة. هذا ليس محللًا صرفيًا كاملًا؛ غرضه تقليل التصادمات، مثل عدم تفسير «الإنذار» على أنه «الآن»، والتقاط «وروابط» كطلب روابط."` | — |
| [SRC-9A0DFA994E-L000069](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L69) | 69 | `""` | — |
| [SRC-9A0DFA994E-L000070](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L70) | 70 | `"## دورة التنفيذ ومصدر الحقيقة"` | — |
| [SRC-9A0DFA994E-L000071](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L71) | 71 | `""` | — |
| [SRC-9A0DFA994E-L000072](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L72) | 72 | ``"تقرير الاستجابة يعرض كتلة `task_understanding` التي تجمع المواصفة والمصفوفة والاستعلامات الفعلية وحالة الأدوات. عند وجود معلومات تشخيصية، يحتفظ بعينات محدودة من حالات الموصلات، مثل حالة الاتصال أو فئة الخطأ أو عدد النتائج. المقصود فصل:"`` | — |
| [SRC-9A0DFA994E-L000073](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L73) | 73 | `""` | — |
| [SRC-9A0DFA994E-L000074](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L74) | 74 | `"- الأداة المطلوبة؛"` | — |
| [SRC-9A0DFA994E-L000075](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L75) | 75 | `"- محاولة تشغيلها؛"` | — |
| [SRC-9A0DFA994E-L000076](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L76) | 76 | `"- نتيجة الموصل؛"` | — |
| [SRC-9A0DFA994E-L000077](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L77) | 77 | `"- المرشح المكتشف؛"` | — |
| [SRC-9A0DFA994E-L000078](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L78) | 78 | `"- المصدر المقبول بعد الفلترة؛"` | — |
| [SRC-9A0DFA994E-L000079](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L79) | 79 | `"- الصفحة التي قُرئت؛"` | — |
| [SRC-9A0DFA994E-L000080](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L80) | 80 | `"- استخدام المصدر في الإجابة؛"` | — |
| [SRC-9A0DFA994E-L000081](../OMARAI_NATURAL_LANGUAGE_UNDERSTANDING_AR.md#L81) | 81 | `"- توليد الإجابة ومراجعتها؛"` | — |
