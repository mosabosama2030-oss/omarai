# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **016**
- سجلات الأسطر: **800**
- النطاق: SRC-D17CE3D12F-L000809 إلى SRC-B9C3015420-L000013
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## وثائق وفهرسة

### FILE-D17CE3D12F — [docs/OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
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

### FILE-89BEE4CE47 — [docs/OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-89BEE4CE47-L000001](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L1) | 1 | `"# Omarai — تسوية الأدلة بعد دمج الإصلاحات الأولية"` | — |
| [SRC-89BEE4CE47-L000002](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L2) | 2 | `""` | — |
| [SRC-89BEE4CE47-L000003](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L3) | 3 | `"**المعرّف:** OMARAI-OPS-EVIDENCE-RECON-2026-10-19  "` | — |
| [SRC-89BEE4CE47-L000004](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L4) | 4 | `"**تاريخ اللقطة:** 2026-10-19  "` | — |
| [SRC-89BEE4CE47-L000005](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L5) | 5 | ``"**نسخة `main` عند الفحص:** `871d2930405d164d3ae4c53f368937a4f5f01a6f`  "`` | — |
| [SRC-89BEE4CE47-L000006](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L6) | 6 | ``"**الغرض:** تسوية نتائج تدقيق P0 التاريخي مع التغييرات اللاحقة حتى دمج PR #48، مع فصل فحوص الفروع المفتوحة عن أدلة `main`. هذه الوثيقة ليست شهادة امتثال أو ضمانًا بأن الخدمة المنشورة تعمل."`` | — |
| [SRC-89BEE4CE47-L000007](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L7) | 7 | `""` | — |
| [SRC-89BEE4CE47-L000008](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L8) | 8 | `"## ملحق زمني: خط الأساس الحالي بعد #75 — 21 أكتوبر 2026"` | — |
| [SRC-89BEE4CE47-L000009](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L9) | 9 | `""` | — |
| [SRC-89BEE4CE47-L000010](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L10) | 10 | ``"هذا المستند بدأ كسجل تاريخي لنسخة `871d2930405d164d3ae4c53f368937a4f5f01a6f` بتاريخ 19 أكتوبر؛ لا تُحوّل أدلته القديمة إلى دليل على النسخة الحالية."`` | — |
| [SRC-89BEE4CE47-L000011](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L11) | 11 | `""` | — |
| [SRC-89BEE4CE47-L000012](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L12) | 12 | ``"خط الأساس الحالي لـ`main` هو `d46a546aba97a9ca32a32c92f1cd6d8a9db2cc81`. اجتاز تشغيل [CI #39584599539](https://github.com/mosabosama2030-oss/omarai/actions/runs/39584599539) عدد 308 اختبارًا على Python 3.11 و308 على Python 3.12، وRuff، والتحقق من الفهرس، وبناء الحاوية وفحص API المحمية. يثبت ذلك نطاق هذه الفحوص فقط."`` | — |
| [SRC-89BEE4CE47-L000013](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L13) | 13 | `""` | — |
| [SRC-89BEE4CE47-L000014](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L14) | 14 | ``"لا تزال عناصر `NOT_RUN/UNKNOWN` التالية مفتوحة حتى يتوفر دليل مباشر: قبول حي لعنوان استضافة يملكه المشروع، مطابقة SHA الصورة المنشورة، نجاح البحث والنموذج من الاستضافة، دوام قاعدة البيانات والاستعادة، اختبار يدوي بالمتصفح، حمل ممثل، ومراجعة أمنية مستقلة نهائية. فرع الإغلاق الحالي منفصل وغير مدمج؛ لا تُنسب تحسيناته إلى `main` قبل الدمج."`` | — |
| [SRC-89BEE4CE47-L000015](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L15) | 15 | `""` | — |
| [SRC-89BEE4CE47-L000016](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L16) | 16 | `"## 1. دلالات الحالة"` | — |
| [SRC-89BEE4CE47-L000017](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L17) | 17 | `""` | — |
| [SRC-89BEE4CE47-L000018](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L18) | 18 | `"- **VERIFIED:** دليل مباشر محدد النطاق، مرتبط بنسخة/اختبار واضح."` | — |
| [SRC-89BEE4CE47-L000019](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L19) | 19 | `"- **INFERRED:** قرائن من الكود أو الوثائق دون إثبات كامل في بيئة التشغيل."` | — |
| [SRC-89BEE4CE47-L000020](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L20) | 20 | `"- **PARTIAL:** جزء من المتطلب مثبت، لكن بقيت فجوة مؤثرة."` | — |
| [SRC-89BEE4CE47-L000021](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L21) | 21 | `"- **UNKNOWN:** لا تكفي الأدلة للحكم."` | — |
| [SRC-89BEE4CE47-L000022](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L22) | 22 | `"- **NOT_RUN:** اختبار معروف لم يتم تشغيله في هذه الجولة."` | — |
| [SRC-89BEE4CE47-L000023](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L23) | 23 | `"- **PROPOSED:** قرار أو إجراء مقترح لم يعتمد بعد."` | — |
| [SRC-89BEE4CE47-L000024](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L24) | 24 | `"- **NOT APPLICABLE:** لا ينطبق على النطاق الحالي مع سبب واضح؛ لا يستعمل لإخفاء نقص الإثبات."` | — |
| [SRC-89BEE4CE47-L000025](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L25) | 25 | `"- **WAIVED:** استثناء صريح وافق عليه صاحب الصلاحية، مع نطاق وتعويض وشرط انتهاء/مراجعة."` | — |
| [SRC-89BEE4CE47-L000026](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L26) | 26 | `""` | — |
| [SRC-89BEE4CE47-L000027](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L27) | 27 | `"كل حالة تنطبق على الضابط المحدد والنطاق المذكور فقط، لا على المشروع كله."` | — |
| [SRC-89BEE4CE47-L000028](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L28) | 28 | `""` | — |
| [SRC-89BEE4CE47-L000029](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L29) | 29 | `"## 2. خط الأساس وسلسلة الأدلة"` | — |
| [SRC-89BEE4CE47-L000030](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L30) | 30 | `""` | — |
| [SRC-89BEE4CE47-L000031](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L31) | 31 | `"### نسخة المصدر"` | — |
| [SRC-89BEE4CE47-L000032](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L32) | 32 | `""` | — |
| [SRC-89BEE4CE47-L000033](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L33) | 33 | ``"نسخة `main` التي تمت مراجعتها في هذه الجولة: `871d2930405d164d3ae4c53f368937a4f5f01a6f`."`` | — |
| [SRC-89BEE4CE47-L000034](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L34) | 34 | `""` | — |
| [SRC-89BEE4CE47-L000035](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L35) | 35 | `"### تغييرات مدمجة ذات صلة"` | — |
| [SRC-89BEE4CE47-L000036](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L36) | 36 | `""` | — |
| [SRC-89BEE4CE47-L000037](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L37) | 37 | `"\| التغيير \| ما يثبته ضمن النطاق \| ما لا يثبته \|"` | — |
| [SRC-89BEE4CE47-L000038](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L38) | 38 | `"\|---\|---\|---\|"` | — |
| [SRC-89BEE4CE47-L000039](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L39) | 39 | `"\| [PR #44](https://github.com/mosabosama2030-oss/omarai/pull/44) \| ميزانية موارد تعاونية للطلب وحد process-local للعمليات المكلفة. \| إلغاء قاطع لكل اتصال جارٍ، أو حد موزع بين النسخ، أو سعة إنتاجية. \|"` | — |
| [SRC-89BEE4CE47-L000040](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L40) | 40 | `"\| [PR #45](https://github.com/mosabosama2030-oss/omarai/pull/45) \| تصحيح وصف التنفيذ وحدوده. \| عمل مزود حي أو نشر فعلي. \|"` | — |
| [SRC-89BEE4CE47-L000041](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L41) | 41 | `"\| [PR #46](https://github.com/mosabosama2030-oss/omarai/pull/46) \| تسوية توثيق ما بعد الدمج. \| تحقق جديد من جميع المخاطر الأمنية. \|"` | — |
| [SRC-89BEE4CE47-L000042](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L42) | 42 | `"\| [PR #47](https://github.com/mosabosama2030-oss/omarai/pull/47) \| خفض تقييم بعض الإجابات التي لا تحتوي استشهادات صالحة. \| تحقق دلالي حتمي من أن كل ادعاء مدعوم بمصدره. \|"` | — |
| [SRC-89BEE4CE47-L000043](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L43) | 43 | `"\| [PR #48](https://github.com/mosabosama2030-oss/omarai/pull/48) \| دمج حد زمني مطلق وخمول لقراءة جسم طلب API مع اختبارات stalled/slow-trickle والتحقق من طول الجسم. \| لا يثبت مهلة قراءة الرؤوس البطيئة، أو حماية شاملة من كل أنماط Slowloris، أو حدًا قاطعًا لمدة تنفيذ الوكيل كاملة. \|"` | — |
| [SRC-89BEE4CE47-L000044](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L44) | 44 | `""` | — |
| [SRC-89BEE4CE47-L000045](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L45) | 45 | `"### تغييرات وفحوص مفتوحة أو بديلة"` | — |
| [SRC-89BEE4CE47-L000046](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L46) | 46 | `""` | — |
| [SRC-89BEE4CE47-L000047](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L47) | 47 | ``"- **PR #49:** أُغلق دون دمج لتجنب تكرار الاختبارات. انتقل المسار أولًا إلى #52 ثم إلى PR #56 المبني على `main` الحالي بعد أن أصبح فرع #52 غير قابل للدمج بسبب انجراف الفرع. لا أثر لـPR #49 أو #52 على `main`."`` | — |
| [SRC-89BEE4CE47-L000048](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L48) | 48 | ``"- **PR #50:** أُغلق دون دمج لأنه اعتمد على لقطة أقدم من `main`. اختُبرت النسخة الحالية من أداة SQLite في PR #58 المبني على `main` الحالي، ونجح CI [39224536955](https://github.com/mosabosama2030-oss/omarai/actions/runs/39224536955) على HEAD `59027f44388730d34c7bd7164450abdba2f9fd0a`: Ruff، و244 اختبارًا على Python 3.11 و244 على Python 3.12، وبناء الحاوية وفحص API المحمية. **PR #58 مفتوح وغير مدمج**؛ الأدلة تخص فرع PR فقط."`` | — |
| [SRC-89BEE4CE47-L000049](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L49) | 49 | ``"- **PR #51:** أُغلق دون دمج واستُبدل بـPR #57 المبني على `main` الحالي. CI الأحدث للمصفوفة [39223782361](https://github.com/mosabosama2030-oss/omarai/actions/runs/39223782361) نجح على HEAD `f0af91c06bffdddcc3a25184754969e86d9e7f86`: Ruff و249 اختبارًا على Python 3.11 و249 على Python 3.12 وبناء الحاوية وفحص API المحمية؛ لا يثبت ذلك قبولًا حيًا."`` | — |
| [SRC-89BEE4CE47-L000050](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L50) | 50 | ``"- **PR #52:** أُغلق دون دمج لأنه اعتمد على لقطة أقدم من `main` وأصبح غير قابل للدمج بعد تغييرات `tests/test_api.py`. CI [39220318275](https://github.com/mosabosama2030-oss/omarai/actions/runs/39220318275) يثبت الرأس القديم فقط ولا يثبت اختبارات الموارد الموسعة الحالية. استُبدل بفرع PR #56 المبني على `main` الحالي."`` | — |
| [SRC-89BEE4CE47-L000051](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L51) | 51 | ``"- **PR #54:** توسيع مصفوفة اختبارات SSRF لفئات IPv4/IPv6 غير العامة — مفتوح وغير مدمج. CI run [39221649040](https://github.com/mosabosama2030-oss/omarai/actions/runs/39221649040) نجح على HEAD `c602de0d039283119236807b075953b4bcf6e89a`: Ruff و249 اختبارًا على Python 3.11 و249 على Python 3.12، وبناء الحاوية وفحص API المحمية. الاختبار حتمي بمحاكاة DNS ولا يجري اتصالًا حيًا."`` | — |
| [SRC-89BEE4CE47-L000052](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L52) | 52 | ``"- **PR #55:** إصلاح مقترح لقراءة سطر الطلب والرؤوس بموعد نهائي مطلق واختبار slow-trickle محلي. CI الأحدث [39224020934](https://github.com/mosabosama2030-oss/omarai/actions/runs/39224020934) نجح على HEAD `4604a83d760b7fe913e1a75cdec04a102c33b0d6`: Ruff، و239 اختبارًا على Python 3.11 و239 على Python 3.12، وبناء الحاوية وفحص API المحمية. يشمل الاختبار التحقق من إغلاق الطلب البطيء قبل إرسال استجابة. PR مفتوح وغير مدمج؛ الاختبار محلي ولا يثبت أداء الاستضافة الحية."`` | — |
| [SRC-89BEE4CE47-L000053](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L53) | 53 | ``"- **PR #56:** مسار M-02 الحالي، مبني على `main` عند `871d2930405d164d3ae4c53f368937a4f5f01a6f`: اختبار حد وتوقف لكل مورد (5 موارد)، وموارد معطلة، وتحرير semaphore، و100 محاولة حجز متزامنة. CI [39223310566](https://github.com/mosabosama2030-oss/omarai/actions/runs/39223310566) نجح على HEAD `0ca1b14aa1dd63bdc48a8ca73f698f7f6bc83416`: Ruff و249 اختبارًا على Python 3.11 و249 على Python 3.12 وبناء الحاوية وفحص API المحمية. هذه أدلة وحدات/تكامل محلية فقط."`` | — |
| [SRC-89BEE4CE47-L000054](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L54) | 54 | ``"- **PR #59:** اقتراح لتثبيت GitHub Actions على commit SHAs كاملة بدل وسوم major متغيرة. CI [39225038734](https://github.com/mosabosama2030-oss/omarai/actions/runs/39225038734) نجح على HEAD `2b8c3de983f09ea1a7c4ca73d4c1a09a54ab987a`: Ruff و238 اختبارًا على Python 3.11 و238 على Python 3.12 وبناء الحاوية وفحص API المحمية. PR مفتوح وغير مدمج؛ ما زالت نسخة `main` تستخدم المراجع القديمة حتى دمج التغيير بموافقة بشرية."`` | — |
| [SRC-89BEE4CE47-L000055](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L55) | 55 | ``"- **PR #43:** أُغلق دون دمج بعد استبداله بـPR #57، الذي يعيد تقديم الوثائق على أساس `main` الحالي؛ يظل التقرير الأولي عند `08319cce3652c332e414f691a71cc153dfbfd92e` لقطة تاريخية فقط."`` | — |
| [SRC-89BEE4CE47-L000056](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L56) | 56 | `""` | — |
| [SRC-89BEE4CE47-L000057](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L57) | 57 | `"## 3. تسوية أهم المتطلبات"` | — |
| [SRC-89BEE4CE47-L000058](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L58) | 58 | `""` | — |
| [SRC-89BEE4CE47-L000059](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L59) | 59 | `"\| المعرف \| الحالة الحالية في نطاق اللقطة \| الدليل والحدود \|"` | — |
| [SRC-89BEE4CE47-L000060](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L60) | 60 | `"\|---\|---\|---\|"` | — |
| [SRC-89BEE4CE47-L000061](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L61) | 61 | ``"\| `API-001` \| PARTIAL — تحسن مدمج مع فجوات متبقية \| `main` عند `871d2930405d164d3ae4c53f368937a4f5f01a6f` يتضمن PR #48: فحص Content-Length وحجم الجسم والحد الكلي ومهلة الخمول، مع اختبار stalled/slow-trickle. لا يثبت هذا مهلة قراءة الرؤوس البطيئة أو حماية شاملة من جميع هجمات Slowloris، ولا حدًا زمنيًا قاطعًا لتنفيذ الوكيل كاملًا. \|"`` | — |
| [SRC-89BEE4CE47-L000062](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L62) | 62 | ``"\| `REL-001` \| PARTIAL \| PR #44 يضيف ميزانية تعاونية تحد من العمل الجديد وتضبط مهلات العمليات الخارجية. لا توجد ضمانة hard cancellation، ولا يثبت ذلك كل مسارات التشخيص أو التشغيل الحي. \|"`` | — |
| [SRC-89BEE4CE47-L000063](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L63) | 63 | ``"\| `PER-002` \| PARTIAL \| الحد process-local للعمليات المكلفة موجود، لكنه لا يحد جميع خيوط HTTP بصورة عالمية ولا يثبت أداءً على حمل ممثل. \|"`` | — |
| [SRC-89BEE4CE47-L000064](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L64) | 64 | ``"\| `PER-003` \| VERIFIED ضمن اختبار ميزانية الوحدات \| حدود البحث/النموذج/الصفحات/الأدوات وميزانية الوقت موجودة في الكود ومغطاة باختبارات الميزانية. هذا لا يثبت سقف تكلفة مالية شاملًا أو سعة إنتاجية أو إلغاء اتصال جارٍ. \|"`` | — |
| [SRC-89BEE4CE47-L000065](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L65) | 65 | ``"\| `AIG-002` \| PARTIAL \| تخطيط البحث وعدد من الموارد محدود، والميزانية التعاونية توقف بدء أعمال جديدة عند نفاد الحد. الاختبارات العدائية لكل مسارات الإنهاك ليست مكتملة. \|"`` | — |
| [SRC-89BEE4CE47-L000066](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L66) | 66 | ``"\| `FIN-001` \| PARTIAL \| حدود لكل طلب وتحديد معدل وتزامن محلي؛ لا توجد ميزانية إنفاق عالمية مضمونة عبر عدة نسخ/مزودين. \|"`` | — |
| [SRC-89BEE4CE47-L000067](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L67) | 67 | ``"\| `EVD-001` \| PARTIAL \| فحص رقم الاستشهاد ومراجعة بمساعدة النموذج لا يثبتان دعم كل claim-source pair بصورة مستقلة. \|"`` | — |
| [SRC-89BEE4CE47-L000068](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L68) | 68 | ``"\| `SEC-001` \| INFERRED / UNKNOWN لتاريخ Git \| القراءة من متغيرات البيئة لا تثبت خلو تاريخ الالتزامات الكامل أو إعدادات الإنتاج من الأسرار. لم يُنجز هنا فحص شامل لتاريخ Git أو بيئة إنتاج حقيقية. \|"`` | — |
| [SRC-89BEE4CE47-L000069](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L69) | 69 | ``"\| `SEC-002` \| PARTIAL \| توجد حماية SSRF في الكود، لكن تغطية DNS المختلط وIPv6 والتحويل إلى عنوان محظور وسباق DNS تحتاج تدقيقًا عدائيًا مستقلًا. \|"`` | — |
| [SRC-89BEE4CE47-L000070](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L70) | 70 | ``"\| `SEC-003` و`AIE-003` \| PARTIAL \| توجد معالجة لمحتوى صفحات الويب بوصفه غير موثوق واختبارات لفصل الرسائل؛ مجموعة red-team الكاملة لكل المصادر والمسارات غير مثبتة. \|"`` | — |
| [SRC-89BEE4CE47-L000071](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L71) | 71 | ``"\| `UX-004` \| INFERRED \| توجد آليات escaping والتحقق من الروابط؛ اختبار XSS شامل على واجهة فعلية لم يُثبت في هذه اللقطة. \|"`` | — |
| [SRC-89BEE4CE47-L000072](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L72) | 72 | ``"\| `IDN-001` و`IDN-003` \| النطاق الحالي مشغّل واحد؛ تعدد المستخدمين غير مطبق \| رمز Bearer مشترك ومخزن leads مشترك. لا يدعم هذا عزل مستأجرين أو تفويضًا لكل سجل. \|"`` | — |
| [SRC-89BEE4CE47-L000073](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L73) | 73 | ``"\| `PRI-002` و`AIG-005` \| INFERRED / PARTIAL \| يرسل مسار النموذج السؤال وبعض السجل والمقتطفات إلى مزود خارجي حسب الإعداد. جرد تدفق بيانات حي شامل لكل الموصلات وشروط الاحتفاظ لم يُنجز هنا. \|"`` | — |
| [SRC-89BEE4CE47-L000074](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L74) | 74 | ``"\| `REL-005` و`EXT-002` \| UNKNOWN \| لم تُثبت استعادة SQLite على مضيف فعلي، ولا دوام التخزين بعد إعادة إنشاء الحاوية. \|"`` | — |
| [SRC-89BEE4CE47-L000075](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L75) | 75 | ``"\| `SRH-001` و`TST-005` \| UNKNOWN للتكامل الحي الشامل \| وجود موصل أو نجاح Mock لا يثبت اتصالًا حيًا بكل مزود. لم يتم تشغيل قبول حي شامل في هذه الجولة. \|"`` | — |
| [SRC-89BEE4CE47-L000076](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L76) | 76 | ``"\| `DPL-001` و`DPL-004` \| UNKNOWN للنشر الفعلي \| بناء Docker واختبار الحاوية على CI لا يثبتان وجود خدمة عامة أو تطابقها مع SHA منشور. \|"`` | — |
| [SRC-89BEE4CE47-L000077](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L77) | 77 | ``"\| `PER-004` و`REL-006` \| UNKNOWN \| لا يوجد تقرير حمل ممثل أو خط أساس SLO قابل للاعتماد في نطاق الأدلة الحالية. \|"`` | — |
| [SRC-89BEE4CE47-L000078](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L78) | 78 | ``"\| `GOV-003` \| UNKNOWN — قرار بشري مطلوب \| لا يوجد سجل استثناءات معتمد مثبت ضمن هذه اللقطة. غياب سجل بالمستودع لا يثبت عدم وجود قرار خارجي. \|"`` | — |
| [SRC-89BEE4CE47-L000079](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L79) | 79 | `""` | — |
| [SRC-89BEE4CE47-L000080](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L80) | 80 | `"## 4. ماذا أُنجز في مسار التشغيل خلال هذه الجولة؟"` | — |
| [SRC-89BEE4CE47-L000081](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L81) | 81 | `""` | — |
| [SRC-89BEE4CE47-L000082](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L82) | 82 | `"### M-01 — قراءة جسم طلب API"` | — |
| [SRC-89BEE4CE47-L000083](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L83) | 83 | `""` | — |
| [SRC-89BEE4CE47-L000084](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L84) | 84 | ``"**التنفيذ:** دُمج PR #48 وأصبح حد الجسم الزمني مطبقًا في `main` عند SHA `871d2930405d164d3ae4c53f368937a4f5f01a6f`. CI [39215710124](https://github.com/mosabosama2030-oss/omarai/actions/runs/39215710124) نجح على HEAD الخاص بالـPR: Ruff، و238 اختبارًا على Python 3.11 و238 على Python 3.12، وبناء الحاوية وفحص API المحمية."`` | — |
| [SRC-89BEE4CE47-L000085](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L85) | 85 | `""` | — |
| [SRC-89BEE4CE47-L000086](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L86) | 86 | ``"**الحالة:** الإصلاح المدمج يغطي طول الجسم وtimeout الخمول والمهلة الكلية وslow-trickle ضمن الاختبارات المضافة. CI الأحدث الخاص بـPR #55 [39224020934](https://github.com/mosabosama2030-oss/omarai/actions/runs/39224020934) نجح على رأسه الحالي `4604a83d760b7fe913e1a75cdec04a102c33b0d6`: Ruff، و239 اختبارًا على Python 3.11 و239 على Python 3.12، وبناء الحاوية وفحص API المحمية. PR #55 ما زال مفتوحًا وغير مدمج، لذا لا يدخل إصلاح الرؤوس إلى `main` بعد. يظل `API-001` جزئيًا حتى يُراجع التغيير ويُدمج بتفويض بشري، ولا يدعي أي من هذه الاختبارات حماية شاملة من كل هجمات Slowloris أو حدًا قاطعًا لتنفيذ الوكيل كاملًا."`` | — |
| [SRC-89BEE4CE47-L000087](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L87) | 87 | `""` | — |
| [SRC-89BEE4CE47-L000088](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L88) | 88 | `"### M-02 — الميزانية والتزامن"` | — |
| [SRC-89BEE4CE47-L000089](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L89) | 89 | `""` | — |
| [SRC-89BEE4CE47-L000090](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L90) | 90 | ``"أُغلق PR #49 لأنه مكرر، وأُغلق PR #52 لأن فرعه انجرف عن `main`. PR #56 هو سطح المراجعة الحالي المبني مباشرة على `main` عند SHA `871d2930405d164d3ae4c53f368937a4f5f01a6f`. أضاف/يجمع: 100 محاولة حجز مقابل سقف 5، وحدود/تجاوز وموارد معطلة لكل من الموارد الخمسة، واختبار تحرير semaphore بعد استثناء غير متوقع."`` | — |
| [SRC-89BEE4CE47-L000091](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L91) | 91 | `""` | — |
| [SRC-89BEE4CE47-L000092](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L92) | 92 | ``"**الحالة:** CI run [39223310566](https://github.com/mosabosama2030-oss/omarai/actions/runs/39223310566) نجح على الرأس `0ca1b14aa1dd63bdc48a8ca73f698f7f6bc83416`: Ruff و249 اختبارًا على Python 3.11 و249 على Python 3.12 وبناء الحاوية وفحص API المحمية. لا يزال الدليل وحدات/تكامل محليًا، وليس اختبار حمل أو ضمانًا موزعًا أو hard cancellation."`` | — |
| [SRC-89BEE4CE47-L000093](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L93) | 93 | `""` | — |
| [SRC-89BEE4CE47-L000094](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L94) | 94 | `"### M-03/M-04 — سجل الأدلة والاستثناءات"` | — |
| [SRC-89BEE4CE47-L000095](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L95) | 95 | `""` | — |
| [SRC-89BEE4CE47-L000096](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L96) | 96 | `"تحديث سجل المتطلبات وقائمة الاستثناءات مخصصان لهذا التغيير التوثيقي. ستظل الاستثناءات المقترحة غير معتمدة حتى يوافق مدير المشروع صراحة على كل قرار مطلوب. لا يعد وجود سجل دليلًا على قبول أي خطر."` | — |
| [SRC-89BEE4CE47-L000097](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L97) | 97 | `""` | — |
| [SRC-89BEE4CE47-L000098](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L98) | 98 | `"### M-05 — النسخ والاستعادة"` | — |
| [SRC-89BEE4CE47-L000099](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L99) | 99 | `""` | — |
| [SRC-89BEE4CE47-L000100](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L100) | 100 | ``"**الجزء المحلي مقترح ومثبت على فرع PR فقط؛ لم يدخل `main`.** PR #58 يضيف أداة نسخ/استعادة لا تستبدل الملفات الموجودة، وتفحص SQLite integrity وعدد السجلات، مع اختبارات round-trip والرفض الآمن. CI [39224536955](https://github.com/mosabosama2030-oss/omarai/actions/runs/39224536955) نجح على HEAD `59027f44388730d34c7bd7164450abdba2f9fd0a`: Ruff و244 اختبارًا على Python 3.11 و244 على Python 3.12 وبناء الحاوية وفحص API المحمية. PR #58 مفتوح وغير مدمج. دوام التخزين واستعادة نسخة على مضيف فعلي أو نسخة خارج المضيف: UNKNOWN/NOT_RUN."`` | — |
| [SRC-89BEE4CE47-L000101](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L101) | 101 | `""` | — |
| [SRC-89BEE4CE47-L000102](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L102) | 102 | `"### M-06 — فصل دليل الاختبارات وقبول التكامل الحي"` | — |
| [SRC-89BEE4CE47-L000103](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L103) | 103 | `""` | — |
| [SRC-89BEE4CE47-L000104](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L104) | 104 | ``"توجد مصفوفة فصل الأدلة في PR #51 على فرعه فقط، وهو مفتوح وغير مدمج. CI [39216670939](https://github.com/mosabosama2030-oss/omarai/actions/runs/39216670939) نجح على HEAD `9d1b64a982cf50f9558a4b58c3799fd4c96bd9ec`: Ruff و234 اختبارًا على كل من Python 3.11 و3.12 وبناء الحاوية وفحص API المحمية."`` | — |
| [SRC-89BEE4CE47-L000105](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L105) | 105 | `""` | — |
| [SRC-89BEE4CE47-L000106](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L106) | 106 | `"**الاختبار الحي لموفرين على استضافة محددة: NOT_RUN.** لم يُنفذ فحص حي شامل لكل موفري البحث والنموذج. إجراءات القبول الحية قد تستهلك رصيد مزود خارجي؛ لا تُشغّل دون تفويض مناسب وتحديد البيئة والهدف."` | — |
| [SRC-89BEE4CE47-L000107](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L107) | 107 | `""` | — |
| [SRC-89BEE4CE47-L000108](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L108) | 108 | `"### M-07 — قبول الاستضافة"` | — |
| [SRC-89BEE4CE47-L000109](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L109) | 109 | `""` | — |
| [SRC-89BEE4CE47-L000110](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L110) | 110 | `"**UNKNOWN / NOT_RUN.** لا يوجد في هذه اللقطة دليل مرتبط بعنوان خدمة مستضافة وSHA منشور يمكن التحقق منه. لا يُنشأ حساب أو تُمنح صلاحية GitHub أو تُنشر الخدمة ضمن هذا التقرير."` | — |
| [SRC-89BEE4CE47-L000111](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L111) | 111 | `""` | — |
| [SRC-89BEE4CE47-L000112](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L112) | 112 | `"### M-08 — مراجعة نتيجة Grok ومراجعة مصدر مستقلة مبدئية"` | — |
| [SRC-89BEE4CE47-L000113](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L113) | 113 | `""` | — |
| [SRC-89BEE4CE47-L000114](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L114) | 114 | `"**حالة مراجعة Grok: PENDING INPUT.** لم تتوفر نتيجة تدقيق Grok النهائية أو PRs الأمنية الناتجة عنه ضمن هذه اللقطة. لا يجوز اعتبار هذه المراجعة المصدرية بديلًا عن مدقق مستقل، ولا يمكن إعلان مراجعة Grok مكتملة دون تقريره الفعلي."` | — |
| [SRC-89BEE4CE47-L000115](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L115) | 115 | `""` | — |
| [SRC-89BEE4CE47-L000116](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L116) | 116 | ``"**نتيجة فحص مصدر محدود على `main` SHA `871d2930405d164d3ae4c53f368937a4f5f01a6f`:**"`` | — |
| [SRC-89BEE4CE47-L000117](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L117) | 117 | `""` | — |
| [SRC-89BEE4CE47-L000118](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L118) | 118 | `"\| المجال \| الدليل الذي شوهد \| التقييم الحالي والحد \|"` | — |
| [SRC-89BEE4CE47-L000119](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L119) | 119 | `"\|---\|---\|---\|"` | — |
| [SRC-89BEE4CE47-L000120](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L120) | 120 | ``"\| SSRF — التحقق قبل الاتصال \| `_public_http_url` يتحقق من HTTP(S)، بيانات الاعتماد، المنافذ، المضيفين المحليين وعناوين IP الحرفية غير العامة. `_public_ip_literals` يرفض فشل DNS وأي إجابة غير عامة. \| دفاع مصدر قوي ضمن المسار المفحوص، وليس شهادة لجميع تدفقات الشبكة أو لكل parser edge cases. \|"`` | — |
| [SRC-89BEE4CE47-L000121](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L121) | 121 | ``"\| SSRF — DNS pinning / redirects \| `_fetch_page` يربط الاتصال بعنوان IP تم فحصه، يحتفظ بـHost وTLS SNI المناسبين، يوقف اتباع التحويلات التلقائي، يعيد فحص كل redirect، يستخدم `verify=True` و`trust_env=False` وحد حجم/نوع محتوى. توجد اختبارات محاكاة للـIP العام المثبت، إجابات DNS المختلطة، والتحويل إلى loopback. \| اختبارات المحاكاة لا تثبت الشبكة الحية أو كل سلوك مكتبات النقل/نظام التشغيل؛ لم يُجرِ هذا التدقيق اختبار شبكة عدائيًا حيًا. \|"`` | — |
| [SRC-89BEE4CE47-L000122](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L122) | 122 | `"\| SSRF — فئات IPv4/IPv6 \| PR #54 يضيف اختبارات سلبية إضافية لنطاقات unspecified/loopback/private/link-local/shared وIPv6 ULA/link-local. \| CI run [39221649040](https://github.com/mosabosama2030-oss/omarai/actions/runs/39221649040) نجح: Ruff، و249 اختبارًا على Python 3.11 و249 على Python 3.12، وبناء الحاوية وفحص API المحمية. يثبت ذلك الاختبارات المحاكية فقط، لا اختبار شبكة حي أو شهادة شاملة. \|"` | — |
| [SRC-89BEE4CE47-L000123](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L123) | 123 | `"\| Prompt injection \| اختبارات موجودة تتحقق من بقاء محتوى الصفحة في رسائل الأدلة وعدم وضعه في رسالة النظام، للمسودّة والمراجعة. \| هذا يثبت فصلًا بنيويًا في حالات اختبار، لا مقاومة عامة لكل هجمات الحقن أو سلوك نموذج حي. \|"` | — |
| [SRC-89BEE4CE47-L000124](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L124) | 124 | ``"\| XSS / العرض \| `web/agent.html` و`web/dashboard.html` يستخدمان escaping لنصوص النتائج، والتحقق من روابط HTTP(S)، و`rel=\"noopener noreferrer\"` للروابط الخارجية في المسارات المفحوصة. \| لم يُثبت فحص XSS عبر متصفح فعلي، أو تدقيق شامل لرؤوس CSP/security headers؛ الحالة INFERRED/PARTIAL. \|"`` | — |
| [SRC-89BEE4CE47-L000125](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L125) | 125 | ``"\| الأسرار وسلسلة التوريد \| الـworkflows على `main` محدودة الصلاحية إلى `contents: read` لكنها ما زالت تستخدم مراجع Actions مثل `@v4` و`@v5`. PR #59 يقترح تثبيت checkout/setup-python على SHA كاملة؛ CI [39225038734](https://github.com/mosabosama2030-oss/omarai/actions/runs/39225038734) اجتاز Ruff و238 اختبارًا لكل إصدار Python وبناء الحاوية. \| PR #59 مفتوح وغير مدمج، لذلك الحماية المقترحة غير فعالة على `main` بعد. فحص تاريخ Git وإعدادات الاستضافة بحثًا عن الأسرار NOT_RUN؛ pinning لا يثبت أن مصدر الأكشنات خالٍ من الثغرات. \|"`` | — |
| [SRC-89BEE4CE47-L000126](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L126) | 126 | `""` | — |
| [SRC-89BEE4CE47-L000127](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L127) | 127 | `"**الخلاصة:** لا يوجد في هذه الجولة عيب SSRF مؤكد من القراءة وحدها في مسار جلب الصفحات، لكن الأدلة ليست كافية لإصدار قبول أمني شامل. تبقى مراجعة Grok المستقلة، فحص الأسرار التاريخي، واختبارات XSS الحية عناصر غير مكتملة."` | — |
| [SRC-89BEE4CE47-L000128](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L128) | 128 | `""` | — |
| [SRC-89BEE4CE47-L000129](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L129) | 129 | `"## 5. بوابات الإغلاق"` | — |
| [SRC-89BEE4CE47-L000130](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L130) | 130 | `""` | — |
| [SRC-89BEE4CE47-L000131](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L131) | 131 | `"لا تغلق النتيجة إلا إذا توفر ما ينطبق عليها من:"` | — |
| [SRC-89BEE4CE47-L000132](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L132) | 132 | `"1. SHA واضح لنسخة المصدر."` | — |
| [SRC-89BEE4CE47-L000133](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L133) | 133 | `"2. وصف قابل لإعادة إنتاج للمشكلة أو للسلوك المطلوب."` | — |
| [SRC-89BEE4CE47-L000134](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L134) | 134 | `"3. اختبار مستقل عن التنفيذ يثبت النتيجة."` | — |
| [SRC-89BEE4CE47-L000135](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L135) | 135 | `"4. نتيجة CI مرتبطة بالـSHA الحالي."` | — |
| [SRC-89BEE4CE47-L000136](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L136) | 136 | `"5. دليل على أن اختبار Mock لم يُعرض بوصفه تكاملًا حيًا."` | — |
| [SRC-89BEE4CE47-L000137](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L137) | 137 | `"6. توثيق القيد المتبقي."` | — |
| [SRC-89BEE4CE47-L000138](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L138) | 138 | `"7. موافقة بشرية مستقلة على الدمج أو الاستضافة أو قبول المخاطر عند انطباقها."` | — |
| [SRC-89BEE4CE47-L000139](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L139) | 139 | `""` | — |
| [SRC-89BEE4CE47-L000140](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L140) | 140 | `"## 6. حكم الحالة"` | — |
| [SRC-89BEE4CE47-L000141](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L141) | 141 | `""` | — |
| [SRC-89BEE4CE47-L000142](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L142) | 142 | `"توجد أدلة مهمة على تحسن ضوابط الميزانية والإبلاغ عن الاستشهادات. ومع ذلك، لا تدعم الأدلة الحالية القول إن جميع متطلبات P0 مكتملة، أو أن الخدمة منشورة ومجربة حيًا، أو أن التخزين قابل للاستعادة على المضيف الفعلي، أو أن التطبيق جاهز لخدمة عامة متعددة المستخدمين."` | — |
| [SRC-89BEE4CE47-L000143](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L143) | 143 | `""` | — |
| [SRC-89BEE4CE47-L000144](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L144) | 144 | `"**القرار الآمن الحالي:** استمرار التطوير على فروع مستقلة، مع إبقاء المخاطر غير المثبتة مفتوحة، وعدم دمج أي PR أو نشر دون موافقة مدير المشروع."` | — |
| [SRC-89BEE4CE47-L000145](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L145) | 145 | `""` | — |
| [SRC-89BEE4CE47-L000146](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L146) | 146 | `"## تسوية إضافية بعد مرشح الإغلاق الموحد — 21 أكتوبر 2026"` | — |
| [SRC-89BEE4CE47-L000147](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L147) | 147 | `""` | — |
| [SRC-89BEE4CE47-L000148](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L148) | 148 | `"لا تمحو هذه الإضافة السجل التاريخي في بداية الوثيقة؛ بل تسجل أحدث دليل متاح."` | — |
| [SRC-89BEE4CE47-L000149](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L149) | 149 | `""` | — |
| [SRC-89BEE4CE47-L000150](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L150) | 150 | `"- خط أساس main بعد #75: d46a546aba97a9ca32a32c92f1cd6d8a9db2cc81."` | — |
| [SRC-89BEE4CE47-L000151](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L151) | 151 | `"- مرشح الإصلاح الموحد: [PR #76](https://github.com/mosabosama2030-oss/omarai/pull/76)، مبني على هذا الخط الأساس، ولم يُدمج."` | — |
| [SRC-89BEE4CE47-L000152](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L152) | 152 | `"- آخر SHA للكود والوثائق الذي اجتاز CI بالكامل: 10d8a7d9f07ef3f91cbb90a5834ac6b71f963de1. [تشغيل #39650978817](https://github.com/mosabosama2030-oss/omarai/actions/runs/39650978817) سجل 380 اختبارًا ناجحًا على Python 3.11 و380 على Python 3.12، مع Ruff وبناء الحاوية واختبار API المحمي."` | — |
| [SRC-89BEE4CE47-L000153](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L153) | 153 | `"- [تشغيل فهرسة #39650974507](https://github.com/mosabosama2030-oss/omarai/actions/runs/39650974507) نجح. الرأس الحالي بعد الفهرسة هو b6aadf7ea02627bbf523501bb879b0fd6705a5c8؛ المقارنة مع 10d8a7d... تظهر ملفات فهرسة مولدة فقط. تشغيل الاختبارات المباشر على b6aadf7 رقم #39651004404 حالته action_required بلا jobs؛ لا توجد تغييرات كود/اختبارات بعد الرأس الكامل الأخضر."` | — |
| [SRC-89BEE4CE47-L000154](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L154) | 154 | `"- الإصلاحات الرئيسية في #76: توجيه الاستيضاح والمتابعة، رفع صرامة إشارة التطابق اللفظي مع إبقائها غير دلالية، CSP hash بدل unsafe-inline، رؤوس الحماية، هوية بناء موثقة، hosted smoke يقارن SHA، تشخيصات الموصلات وجلب الصفحات، مسار SQLite قابل للضبط، أداة البحث المحلي، وتحديث الوثائق."` | — |
| [SRC-89BEE4CE47-L000155](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L155) | 155 | `"- NOT_RUN/UNKNOWN: اختبار hosted smoke ضد خدمة منشورة فعلية؛ عمل كل موفر بحث/نموذج حيًا؛ تقييم الدقة الدلالية الفعلي لحالات AQ-001–045؛ Volume فعلي وبقاء SQLite والاستعادة؛ اختبار الحمل؛ red-team حي أوسع. هذه الحدود تمنع إعلان جاهزية إنتاجية عامة."` | — |
| [SRC-89BEE4CE47-L000156](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L156) | 156 | `"- نطاق التشغيل الحالي أحادي المشغّل. لا تدّعِ عزل عدة مستأجرين قبل تنفيذ الهوية والتفويض واختبارات الملكية والعزل."` | — |
| [SRC-89BEE4CE47-L000157](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L157) | 157 | `""` | — |
| [SRC-89BEE4CE47-L000158](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L158) | 158 | `""` | — |
| [SRC-89BEE4CE47-L000159](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L159) | 159 | `"## تحديث تحقق إضافي بعد إصلاح روابط البحث وفحص الفهرس — 21 أكتوبر 2026"` | — |
| [SRC-89BEE4CE47-L000160](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L160) | 160 | `""` | — |
| [SRC-89BEE4CE47-L000161](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L161) | 161 | `"هذا التحديث أحدث من ملحقات CI السابقة في هذه الوثيقة، ويجب قراءته معها دون حذف سجل النتائج التاريخية:"` | — |
| [SRC-89BEE4CE47-L000162](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L162) | 162 | `""` | — |
| [SRC-89BEE4CE47-L000163](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L163) | 163 | ``"- آخر تشغيل شامل أخضر **قبل** تغيير `docs/search_code.py` و`.github/workflows/tests.yml` هو [run #39651908777](https://github.com/mosabosama2030-oss/omarai/actions/runs/39651908777) على `5a2259ef787d4a4553a503276daf399fa6514f3f`: 380 اختبارًا لكل من Python 3.11 و3.12، وRuff، وفحص الفهرس، وبناء الحاوية واختبار API المحمي ناجحة. لا يغطي هذا التشغيل التغييرات التي أضيفت بعده."`` | — |
| [SRC-89BEE4CE47-L000164](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L164) | 164 | ``"- أُضيف إلى أداة البحث خيار `--ref`، مع `OMARAI_GITHUB_REF` والالتقاط الآمن لمرجع SHA المحلي/CI، حتى تشير الروابط إلى النسخة التي تُراجع بدل تثبيتها على `blob/main`. أضيفت اختبارات لهذه السلوكيات، لكن pytest لم يصل إليها في التشغيل الأخير."`` | — |
| [SRC-89BEE4CE47-L000165](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L165) | 165 | ``"- غُيّر CI إلى فحص الفهرس الملتزم مباشرة باستخدام `python docs/generate_index.py --check`. في [run #39652716421](https://github.com/mosabosama2030-oss/omarai/actions/runs/39652716421) نجح Ruff، لكن فحص الفهرس اكتشف ملفات مولدة قديمة في لقطة PR merge قبل تحديثها آليًا؛ لذلك توقفت pytest ولم تُشغّل."`` | — |
| [SRC-89BEE4CE47-L000166](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L166) | 166 | ``"- بعد تحديث الفهرس، ظل تشغيل [#39653239007](https://github.com/mosabosama2030-oss/omarai/actions/runs/39653239007) على رأس bot بحالة `action_required` بلا jobs. رأس PR #76 شوهد وقت إضافة هذا التحديث كـ `de619aefc8375dcfbf0d96ab32b36e156b2273cb`؛ يجب أخذ الرأس الحي من GitHub قبل قرار الدمج لأن تحديث الفهرس قد يضيف commit آخر."`` | — |
| [SRC-89BEE4CE47-L000167](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L167) | 167 | ``"- لذلك حالة التغييرات الأخيرة للبحث وفحص الفهرس هي **PARTIAL / NOT YET FULLY TESTED**، وليست `FIXED_AND_TESTED`. يلزم اعتماد وتشغيل GitHub Actions على الرأس الحالي ثم مراجعة نتائج pytest وRuff والفهرس والحاوية."`` | — |
| [SRC-89BEE4CE47-L000168](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L168) | 168 | ``"- لا يغيّر ذلك حالة الاختبارات الحية المستقلة: `NOT_RUN/UNKNOWN` ما زالت تنطبق على hosted smoke، وتوافر كل موفري البحث والنموذج، والتقييم الدلالي لـAQ-001–045، ودوام التخزين/الاستعادة على المضيف، واختبار الحمل، وعزل تعدد المستأجرين، والتقرير المستقل الكامل من Grok."`` | — |
| [SRC-89BEE4CE47-L000169](../OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md#L169) | 169 | ``"- **السجل المركزي الوحيد لجميع المعرفات ومعايير الإغلاق:** [`OMARAI_REMEDIATION_REGISTER_AR.md`](OMARAI_REMEDIATION_REGISTER_AR.md). لا تكرر بنودًا جديدة هنا دون إضافتها إلى ذلك السجل."`` | — |
## وثائق وفهرسة

### FILE-855DA3B8BC — [docs/OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-855DA3B8BC-L000001](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L1) | 1 | `"# تدقيق Omarai التأسيسي — نتائج P0 من الكود والاختبارات"` | — |
| [SRC-855DA3B8BC-L000002](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L2) | 2 | `""` | — |
| [SRC-855DA3B8BC-L000003](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L3) | 3 | ``"> **تنبيه تاريخي:** هذا التقرير لقطة تدقيق مرتبطة بالنسخة `08319cce3652c332e414f691a71cc153dfbfd92e`، قبل دمج PR #44–#47. لا يُستخدم وحده للحكم على `main` الحالي. اقرأ معه [تسوية الأدلة التشغيلية بعد الدمج](OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md)، وهي المرجع لتغييرات الموارد والاستشهادات وحالة PR #48 وطلبات التحقق المفتوحة."`` | — |
| [SRC-855DA3B8BC-L000004](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L4) | 4 | `""` | — |
| [SRC-855DA3B8BC-L000005](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L5) | 5 | `"**المعرّف:** OMARAI-AUDIT-P0-2026-10-19  "` | — |
| [SRC-855DA3B8BC-L000006](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L6) | 6 | `"**تاريخ التدقيق:** 2026-10-19  "` | — |
| [SRC-855DA3B8BC-L000007](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L7) | 7 | `"**الفرع المرجعي للكود:** main  "` | — |
| [SRC-855DA3B8BC-L000008](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L8) | 8 | `"**نسخة المصدر المدققة:** 08319cce3652c332e414f691a71cc153dfbfd92e  "` | — |
| [SRC-855DA3B8BC-L000009](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L9) | 9 | `"**نسخة التطبيق السابقة لدمج وثائق المتطلبات:** 3cad5031de3dfdea6977d2428bc00d1e8bfd1303  "` | — |
| [SRC-855DA3B8BC-L000010](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L10) | 10 | `"**نطاق التقرير:** متطلبات P0 في سجل Omarai التأسيسي، مع تركيز على سلامة السلوك، وصلاحيات الأدوات، وحدود الموارد، وأمان البحث، وصحة الاستشهادات، وعزل المستخدمين.  "` | — |
| [SRC-855DA3B8BC-L000011](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L11) | 11 | `"**الوثائق الحاكمة:** [سجل المتطلبات](OMARAI_REQUIREMENTS_REGISTER.md)، [الدستور الهندسي](OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md)، [خط الأساس الهندسي الموسع](OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md)، [نموذج التتبع والنضج](OMARAI_REQUIREMENTS_TRACEABILITY_AND_MATURITY_MODEL_AR.md)."` | — |
| [SRC-855DA3B8BC-L000012](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L12) | 12 | `""` | — |
| [SRC-855DA3B8BC-L000013](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L13) | 13 | `"---"` | — |
| [SRC-855DA3B8BC-L000014](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L14) | 14 | `""` | — |
| [SRC-855DA3B8BC-L000015](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L15) | 15 | `"## 1. الحكم التنفيذي"` | — |
| [SRC-855DA3B8BC-L000016](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L16) | 16 | `""` | — |
| [SRC-855DA3B8BC-L000017](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L17) | 17 | `"**الحكم المتوازن: اتجاه Omarai الهندسي جيد بوضوح، وتوجد بالفعل ضوابط مهمة في الكود واختبارات مناسبة لعدد من سيناريوهات الفشل؛ لكن لا يوجد حتى الآن ما يبرر القول إن جميع المتطلبات التأسيسية مستوفاة أو إن التطبيق جاهز كمنصة عامة متعددة المستخدمين.**"` | — |
| [SRC-855DA3B8BC-L000018](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L18) | 18 | `""` | — |
| [SRC-855DA3B8BC-L000019](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L19) | 19 | `"الأدلة الإيجابية الأقوى:"` | — |
| [SRC-855DA3B8BC-L000020](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L20) | 20 | `"- اجتازت نسخة main المرجعية فحوص GitHub Actions على Python 3.11 و3.12؛ نجح تثبيت الاعتماديات، وRuff، وpytest."` | — |
| [SRC-855DA3B8BC-L000021](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L21) | 21 | `"- نجح بناء حاوية Docker، ونجح smoke test يفحص الصحة، ويرفض الطلبات غير المصادق عليها إلى واجهتي الوكيل والعملاء، ويقبل بعض الطلبات المصادق عليها."` | — |
| [SRC-855DA3B8BC-L000022](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L22) | 22 | `"- توجد حدود فعلية لأحجام الأسئلة والصفحات والنتائج وعدد الاستعلامات وبعض استدعاءات الموفرين، وتوجد مهلات على كثير من الاتصالات الخارجية."` | — |
| [SRC-855DA3B8BC-L000023](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L23) | 23 | `"- جلب الصفحات يتضمن دفاعات SSRF جدية: فحص HTTP/HTTPS، ورفض عناوين محلية، وحل DNS، وتثبيت عنوان الاتصال، والتحقق من كل تحويل، والتحقق من نوع المحتوى والحجم."` | — |
| [SRC-855DA3B8BC-L000024](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L24) | 24 | `"- يوجد فصل مقصود بين تعليمات النظام ومحتوى الويب غير الموثوق، وتوجد مراجعة بمساعدة نموذج ثانٍ للادعاءات، مع إفصاح صريح بأنها ليست تحققًا مستقلًا من الحقيقة."` | — |
| [SRC-855DA3B8BC-L000025](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L25) | 25 | `"- API يتطلب Bearer token في وضع النشر العام، ويقارن الرمز بطريقة ثابتة الزمن، ويطبق تحديد معدل على مستوى عنوان العميل، ويحظر طلبات غير مصادق عليها قبل تحليل جسم الطلب."` | — |
| [SRC-855DA3B8BC-L000026](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L26) | 26 | `"- نتائج الفشل والبحث غير المكتمل ليست دائمًا مغطاة بصياغة نجاح؛ توجد اختبارات تؤكد إبقاء بعض حالات الفشل والحالة المجهولة صريحة."` | — |
| [SRC-855DA3B8BC-L000027](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L27) | 27 | `""` | — |
| [SRC-855DA3B8BC-L000028](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L28) | 28 | `"لكن توجد أربع فجوات رئيسية يجب ألا نحجبها:"` | — |
| [SRC-855DA3B8BC-L000029](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L29) | 29 | `"1. **لا تظهر في الكود ميزانية موحدة لنهاية الطلب أو حد عالمي للتوازي.** حدود كل مرحلة جيدة كبداية، لكنها لا تمنع عددًا كبيرًا من الطلبات المتزامنة من تضخيم تكلفة البحث والنماذج واستهلاك العمال."` | — |
| [SRC-855DA3B8BC-L000030](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L30) | 30 | `"2. **التطبيق الحالي يستخدم رمز وصول مشتركًا وقاعدة عملاء مشتركة.** عزل بيانات المستخدمين/المستأجرين غير مثبت ولا يوجد تصميم هوية وصلاحيات لكل مستخدم. هذا مقبول فقط إذا كان النطاق المقصود مساحة خاصة لمشغّل واحد؛ وهو مانع قبل تقديمه كخدمة متعددة المستخدمين."` | — |
| [SRC-855DA3B8BC-L000031](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L31) | 31 | `"3. **الاستشهادات لا تُتحقق دلاليًا بصورة حتمية.** فحص الكود يتأكد أساسًا من أن رقم المصدر يقع ضمن المجال، والمراجعة الدلالية مفوضة إلى نموذج لغوي آخر. هذا تحسين مفيد لكنه ليس إثباتًا مستقلًا أن كل مصدر يسند كل ادعاء."` | — |
| [SRC-855DA3B8BC-L000032](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L32) | 32 | `"4. **اختبارات SSRF وحقن التعليمات لا تغطي جميع فروع الحماية المرصودة.** التصميم المصدري أقوى من التغطية الحالية؛ لذلك نحتفظ بالحكم «جزئي/استدلالي» بدل «مثبت بالكامل»."` | — |
| [SRC-855DA3B8BC-L000033](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L33) | 33 | `""` | — |
| [SRC-855DA3B8BC-L000034](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L34) | 34 | `"**قرار الاستخدام المقترح:**"` | — |
| [SRC-855DA3B8BC-L000035](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L35) | 35 | `"- **نسخة تجريبية خاصة بمشغّل واحد:** يمكن مواصلة العمل والاختبار مع رمز قوي محفوظ كسر، وعدم إدخال معلومات سرية إلى الموفر الخارجي، وعدم الاعتماد على تخزين البيانات دون التحقق من استمراريته."` | — |
| [SRC-855DA3B8BC-L000036](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L36) | 36 | `"- **إطلاق عام أو خدمة لعدة مستخدمين:** لا أوصي باعتبارها جاهزة بعد؛ أولوية الإغلاق هي حد توازي وdeadline شامل، ثم تصميم الهوية وعزل البيانات، وتقوية اختبارات SSRF/حقن التعليمات، وتحديد حدود دلالية صادقة للاستشهادات، ومراجعة تهيئة الوكيل العكسي والتخزين الفعلي."` | — |
| [SRC-855DA3B8BC-L000037](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L37) | 37 | `""` | — |
| [SRC-855DA3B8BC-L000038](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L38) | 38 | `"هذا ليس حكمًا بأن الكود سيئ؛ بل دليل على أنه **أساس هندسي واعد يحتاج استكمال عدد محدد من ضوابط الإنتاج** قبل توسيع نطاق الثقة فيه."` | — |
| [SRC-855DA3B8BC-L000039](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L39) | 39 | `""` | — |
| [SRC-855DA3B8BC-L000040](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L40) | 40 | `"## 2. الأدلة التي تم فحصها"` | — |
| [SRC-855DA3B8BC-L000041](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L41) | 41 | `""` | — |
| [SRC-855DA3B8BC-L000042](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L42) | 42 | `"### مرجع النسخة"` | — |
| [SRC-855DA3B8BC-L000043](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L43) | 43 | `"- main: 08319cce3652c332e414f691a71cc153dfbfd92e"` | — |
| [SRC-855DA3B8BC-L000044](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L44) | 44 | `"- كود الوكيل: agents/web_agent.py، 3854 سطرًا عند النسخة المدققة."` | — |
| [SRC-855DA3B8BC-L000045](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L45) | 45 | `"- API: api/omarai.py، 329 سطرًا."` | — |
| [SRC-855DA3B8BC-L000046](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L46) | 46 | `"- التحليل/التخزين: agents/omarai.py وagents/research.py."` | — |
| [SRC-855DA3B8BC-L000047](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L47) | 47 | `"- الواجهات: web/agent.html وweb/dashboard.html."` | — |
| [SRC-855DA3B8BC-L000048](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L48) | 48 | `"- اختبارات ذات صلة: tests/test_web_agent.py، tests/test_api.py، tests/test_omarai.py، tests/test_hosted_smoke.py، tests/test_proxy_origin.py، tests/test_intent_router.py، tests/test_answer_quality_runner.py."` | — |
| [SRC-855DA3B8BC-L000049](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L49) | 49 | `"- CI: .github/workflows/tests.yml."` | — |
| [SRC-855DA3B8BC-L000050](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L50) | 50 | `"- إعداد النشر المعلن في المستودع: render.yaml وDockerfile."` | — |
| [SRC-855DA3B8BC-L000051](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L51) | 51 | `""` | — |
| [SRC-855DA3B8BC-L000052](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L52) | 52 | `"### نتائج CI المثبتة من GitHub Actions"` | — |
| [SRC-855DA3B8BC-L000053](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L53) | 53 | `"\| الفحص \| النتيجة المسجلة \| ما تثبته النتيجة وما لا تثبته \|"` | — |
| [SRC-855DA3B8BC-L000054](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L54) | 54 | `"\|---\|---\|---\|"` | — |
| [SRC-855DA3B8BC-L000055](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L55) | 55 | `"\| Python 3.11 — Ruff \| PASS \| اجتاز فحص الصياغة/النمط المحدد، وليس فحصًا أمنيًا شاملًا \|"` | — |
| [SRC-855DA3B8BC-L000056](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L56) | 56 | `"\| Python 3.11 — pytest \| PASS \| اجتازت مجموعة الاختبارات الحالية على بيئة CI \|"` | — |
| [SRC-855DA3B8BC-L000057](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L57) | 57 | `"\| Python 3.12 — Ruff \| PASS \| اجتاز فحص الصياغة/النمط المحدد \|"` | — |
| [SRC-855DA3B8BC-L000058](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L58) | 58 | `"\| Python 3.12 — pytest \| PASS \| اجتازت مجموعة الاختبارات الحالية على بيئة CI \|"` | — |
| [SRC-855DA3B8BC-L000059](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L59) | 59 | `"\| Docker build \| PASS \| أمكن بناء الصورة على CI \|"` | — |
| [SRC-855DA3B8BC-L000060](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L60) | 60 | `"\| Smoke test للحاوية \| PASS \| استجابت health، ورُفضت طلبات غير مصادق عليها، وقُبلت طلبات مصادق عليها المحددة في السكربت \|"` | — |
| [SRC-855DA3B8BC-L000061](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L61) | 61 | `""` | — |
| [SRC-855DA3B8BC-L000062](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L62) | 62 | `"روابط تشغيل CI: [Python 3.11](https://github.com/mosabosama2030-oss/omarai/actions/runs/39184807152/job/117844864363)، [Python 3.12](https://github.com/mosabosama2030-oss/omarai/actions/runs/39184807152/job/117844864528)، [Docker + protected API smoke test](https://github.com/mosabosama2030-oss/omarai/actions/runs/39184807152/job/117844864488)."` | — |
| [SRC-855DA3B8BC-L000063](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L63) | 63 | `""` | — |
| [SRC-855DA3B8BC-L000064](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L64) | 64 | `"**حدود التحقق:** لم أشغّل الاختبارات محليًا داخل بيئة مستنسخة في هذه الجولة؛ استند تأكيد نجاح الاختبارات إلى نتائج CI الفعلية أعلاه. لم أنفذ اختبار اختراق حيًا، أو اختبار حمل، أو استدعاءً فعليًا بمفاتيح المستخدم لمزودي البحث/النماذج، أو اختبارًا على نشر Render الفعلي. لا تتضمن هذه النتيجة ادعاء بأن تلك الاختبارات حدثت."` | — |
| [SRC-855DA3B8BC-L000065](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L65) | 65 | `""` | — |
| [SRC-855DA3B8BC-L000066](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L66) | 66 | `"## 3. معنى الحالات المستخدمة"` | — |
| [SRC-855DA3B8BC-L000067](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L67) | 67 | `""` | — |
| [SRC-855DA3B8BC-L000068](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L68) | 68 | `"- **VERIFIED — ضمن نطاق محدد:** توجد شواهد مباشرة من الكود و/أو اختبار تلقائي يثبت السلوك المحدد فقط؛ لا يعني ضمانًا شاملًا."` | — |
| [SRC-855DA3B8BC-L000069](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L69) | 69 | `"- **INFERRED — موجود جزئيًا/استدلالي:** توجد آلية واضحة في الكود، لكن لم يُثبت كل سلوكها باختبار مباشر أو بيئة حية."` | — |
| [SRC-855DA3B8BC-L000070](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L70) | 70 | `"- **PROPOSED / GAP — غير مستوفى حسب النطاق الحالي:** لا تظهر آلية كافية لتنفيذ المتطلب المحدد، أو ثبت أن النطاق المعلن يتطلب قدرة غير موجودة."` | — |
| [SRC-855DA3B8BC-L000071](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L71) | 71 | `"- **UNKNOWN — غير محسوم:** يلزم الاطلاع على إعداد تشغيل/استضافة أو سجل غير متاح أو إجراء اختبار إضافي."` | — |
| [SRC-855DA3B8BC-L000072](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L72) | 72 | `"- **N/A مشروط:** لا ينطبق على القدرات الحالية، لكن يجب إعادة تفعيله عندما تتغير القدرة أو نطاق المستخدمين."` | — |
| [SRC-855DA3B8BC-L000073](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L73) | 73 | `""` | — |
| [SRC-855DA3B8BC-L000074](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L74) | 74 | `"## 4. أهم نتائج المخاطر — مرتبة حسب أثرها"` | — |
| [SRC-855DA3B8BC-L000075](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L75) | 75 | `""` | — |
| [SRC-855DA3B8BC-L000076](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L76) | 76 | `"### A-01 — غياب حد عالمي للتوازي وميزانية زمنية موحدة للطلب"` | — |
| [SRC-855DA3B8BC-L000077](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L77) | 77 | `"**النتيجة:** فجوة موثقة من قراءة الكود؛ الأولوية P1 قبل إتاحة عامة، وقد تصبح P0 عند تعريض النظام لحمل غير موثوق أو تكلفة مدفوعة كبيرة."` | — |
| [SRC-855DA3B8BC-L000078](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L78) | 78 | `""` | — |
| [SRC-855DA3B8BC-L000079](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L79) | 79 | `"توجد حدود جيدة لكل مرحلة: MAX_PLAN_QUERIES=8، وMAX_RESEARCH_WORKERS=8، وMAX_FETCHED_PAGES=8، وMAX_PAGE_BYTES=1,000,000، ومهلة 8 ثوانٍ لجلب الصفحة، و10 ثوانٍ لكل موصل بحث في غلاف البحث، وحدود زمنية لاستدعاءات التخطيط والإجابة والمراجعة. كما توجد محاولة واحدة إضافية لإصلاح فجوة الأدلة، وحدود لعدد استدعاءات بعض الموفرين."` | — |
| [SRC-855DA3B8BC-L000080](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L80) | 80 | `""` | — |
| [SRC-855DA3B8BC-L000081](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L81) | 81 | `"لكن ThreadingHTTPServer ينشئ خيط معالجة لكل طلب ولا يظهر حول /api/agent حد تزامن عام أو طابور محدود. وكل طلب قد ينفذ عدة استعلامات؛ كل استعلام بدوره قد يشغّل عدة موصلات بالتوازي، ثم جلب صفحات، ثم استدعاءات نموذج رئيسية واحتياطية ومراجعة. مهلة asyncio.wait_for على to_thread لا تضمن قتل العمل المتزامن الجاري داخل الخيط عند انتهائها. ولا يظهر deadline واحد ينتقل بين كل هذه المراحل ويمنع بدء مرحلة جديدة عندما تبقى للطلب ميزانية غير كافية."` | — |
| [SRC-855DA3B8BC-L000082](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L82) | 82 | `""` | — |
| [SRC-855DA3B8BC-L000083](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L83) | 83 | `"**المطلوب:** إضافة ميزانية نهاية-إلى-نهاية باستخدام monotonic deadline، وحد تزامن عالمي للبحث/النماذج، وحد انتظار قصير يعيد استجابة ازدحام مفهومة، وميزانية استدعاءات واضحة لكل نمط، واختبار ضغط يثبت أن عدد العمال والتكلفة لا ينفلتان. يجب قياس هذه الحدود بدل تخمينها."` | — |
| [SRC-855DA3B8BC-L000084](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L84) | 84 | `""` | — |
| [SRC-855DA3B8BC-L000085](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L85) | 85 | `"### A-02 — لا يوجد عزل بيانات لكل مستخدم/مستأجر"` | — |
| [SRC-855DA3B8BC-L000086](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L86) | 86 | `"**النتيجة:** الفجوة قائمة إذا كان Omarai سيخدم عدة مستخدمين مستقلين؛ النطاق الحالي أقرب إلى تطبيق بمشغّل واحد ورمز مشترك."` | — |
| [SRC-855DA3B8BC-L000087](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L87) | 87 | `""` | — |
| [SRC-855DA3B8BC-L000088](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L88) | 88 | `"تستخدم Handler.store مخزن LeadStore واحدًا على مستوى الصنف، ويستخدم المخزن ملف SQLite واحدًا. المصادقة تعتمد على قيمة OMARAI_ACCESS_TOKEN مشتركة، لا هوية مستخدم مستقلة أو صلاحية على سجل بعينه. لا توجد في السجل الحالي مفاتيح مالك/tenant تُستخدم لتقييد list/add/update. وكل شخص يمتلك الرمز نفسه يستطيع الوصول إلى مجموعة السجلات نفسها."` | — |
| [SRC-855DA3B8BC-L000089](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L89) | 89 | `""` | — |
| [SRC-855DA3B8BC-L000090](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L90) | 90 | `"في المقابل، يُنشأ WebAgent جديد لكل طلب /api/agent وتُصفّر داخله قوائم المصادر وتشخيصات الموفر عند بدء answer()، وهذا يقلل خطر تداخل حالة البحث المحلية بين طلبين داخل عملية التطبيق. لكنه **ليس** بديلًا عن عزل بيانات العملاء."` | — |
| [SRC-855DA3B8BC-L000091](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L91) | 91 | `""` | — |
| [SRC-855DA3B8BC-L000092](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L92) | 92 | `"**المطلوب:** إما اعتماد النطاق صراحةً كأداة خاصة بمشغّل واحد مع عدم وصفها بخدمة multi-user، أو إضافة هوية وتفويض لكل مستخدم وملكية لكل سجل واختبارات سلبية تؤكد أن مستخدم A لا يستطيع رؤية أو تعديل بيانات مستخدم B. لا يكفي تغيير الواجهة أو إعطاء رموز مختلفة من دون فرض النطاق داخل API وقاعدة البيانات."` | — |
| [SRC-855DA3B8BC-L000093](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L93) | 93 | `""` | — |
| [SRC-855DA3B8BC-L000094](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L94) | 94 | `"### A-03 — فحص الاستشهادات يثبت رقم المصدر، لا دعم الادعاء بصورة مستقلة"` | — |
| [SRC-855DA3B8BC-L000095](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L95) | 95 | `"**النتيجة:** جزئي، مع شفافية جيدة حول هذا القيد."` | — |
| [SRC-855DA3B8BC-L000096](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L96) | 96 | `""` | — |
| [SRC-855DA3B8BC-L000097](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L97) | 97 | `"تزيل الدالة _remove_invalid_citations أرقام المصادر الخارجة عن نطاق المصادر المرسلة. وتسمّي _citation_validation_metadata الطريقة numeric_source_index_range_only، وتعيد claim_support بما يوضح أن المراجعة النموذجية ليست تدقيقًا مستقلًا للحقيقة. يمرر النظام الأدلة إلى نموذج الإجابة، ويطلب من نموذج المراجعة إزالة الادعاءات غير المدعومة وعدم اختراع حقائق. هذه خطوات صحيحة ومفيدة، لكنها لا تجعل فحص رقم الاستشهاد مساويًا لإثبات دلالي، كما أن نموذج المراجعة نفسه نموذج لغوي معرض للخطأ."` | — |
| [SRC-855DA3B8BC-L000098](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L98) | 98 | `""` | — |
| [SRC-855DA3B8BC-L000099](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L99) | 99 | `"**المطلوب:** الإبقاء على الوصف الصادق الحالي، ثم بناء مجموعة تقييم claim-to-source على عينات عربية/إنجليزية؛ والتحقق من الرابط والمقتطف الذي يدعم الادعاء المحدد؛ وقياس الادعاءات غير المسندة والاستشهادات الصحيحة شكليًا والخاطئة دلاليًا. لا تسمَّ الإجابة VERIFIED FACTUALITY قبل تحقق مناسب مستقل أو مرجعي."` | — |
| [SRC-855DA3B8BC-L000100](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L100) | 100 | `""` | — |
| [SRC-855DA3B8BC-L000101](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L101) | 101 | `"### A-04 — تغطية اختبار SSRF أقل من قوة التصميم"` | — |
| [SRC-855DA3B8BC-L000102](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L102) | 102 | `"**النتيجة:** التصميم يستحق التقدير؛ إثباته الاختباري غير مكتمل."` | — |
| [SRC-855DA3B8BC-L000103](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L103) | 103 | `""` | — |
| [SRC-855DA3B8BC-L000104](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L104) | 104 | `"يحتوي _public_http_url على رفض للمخططات غير HTTP(S)، والبيانات المضمنة للمصادقة، والمنافذ غير المعتمدة، وبعض المضيفين المحليين، وعناوين IP غير العامة. وتحل _public_ip_literals كل عنوان DNS وتطلب أن تكون جميع الإجابات عامة. ويثبت _fetch_page عنوان اتصال عامًّا بدل إجراء اتصال جديد باسم المضيف، ويوقف التحويلات التلقائية، ويعيد التحقق من كل وجهة redirect، ويقيد أنواع المحتوى وحجم الصفحة وعدد التحويلات."` | — |
| [SRC-855DA3B8BC-L000105](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L105) | 105 | `""` | — |
| [SRC-855DA3B8BC-L000106](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L106) | 106 | `"لكن الاختبارات الموجودة التي أمكن تحديدها في test_web_agent.py تغطي بشكل مباشر حالات URL النصية مثل 127.0.0.1 وlocalhost وبيانات المصادقة وfile://، ولا يظهر ضمن أسماء الاختبارات الحالية اختبار مباشر يثبت رفض redirect من نطاق عام إلى عنوان داخلي، أو DNS بإجابات مختلطة عامة/خاصة، أو DNS rebinding، أو IPv6 link-local/metadata، أو تجاوز حجم الصفحة مع Content-Length كاذب. عدم وجود اختبار بهذا الاسم ليس برهانًا رياضيًا على غياب أي تغطية أخرى، لكنه فجوة دليل واضحة تستحق الإغلاق."` | — |
| [SRC-855DA3B8BC-L000107](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L107) | 107 | `""` | — |
| [SRC-855DA3B8BC-L000108](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L108) | 108 | `"**المطلوب:** إضافة اختبارات حتمية بمزود DNS وHTTP وهمي (mock) تختبر كل هذه الحالات، مع اختبار أن الاتصال الفعلي لا يعيد تحليل الاسم بعد التحقق."` | — |
| [SRC-855DA3B8BC-L000109](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L109) | 109 | `""` | — |
| [SRC-855DA3B8BC-L000110](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L110) | 110 | `"### A-05 — تهيئة Origin خلف الوكيل العكسي تحتاج تأكيدًا تشغيليًا"` | — |
| [SRC-855DA3B8BC-L000111](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L111) | 111 | `"**النتيجة:** مشروطة بإعداد الاستضافة الفعلي."` | — |
| [SRC-855DA3B8BC-L000112](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L112) | 112 | `""` | — |
| [SRC-855DA3B8BC-L000113](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L113) | 113 | `"في وضع النشر العام، يضيف _allowed_origins أصولًا مشتقة من Host وX-Forwarded-Host وX-Forwarded-Proto في الطلب الوارد. ويمكن أن يكون هذا مقبولًا إذا كان الوكيل العكسي الموثوق يحذف رؤوس العميل ويعيد كتابتها بشكل صحيح؛ أما الاعتماد على رؤوس قابلة للتلاعب مباشرة دون إثبات هذا الشرط في بيئة النشر فلا يكفي. كما يعتمد rate limiting على عنوان اتصال الخادم افتراضيًا، ولا يقرأ X-Forwarded-For إلا عند تفعيل OMARAI_TRUST_PROXY_HEADERS=1؛ يجب التأكد أن الإعداد في البيئة الحقيقية لا يجعل كل العملاء خلف الوكيل يشاركون bucket واحدًا أو يجعل الترويسات القابلة للانتحال أساسًا للحدود."` | — |
| [SRC-855DA3B8BC-L000114](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L114) | 114 | `""` | — |
| [SRC-855DA3B8BC-L000115](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L115) | 115 | `"**المطلوب:** ضبط OMARAI_ALLOWED_ORIGINS صراحةً للنطاق الموثوق، والتحقق من سلوك proxy headers في الاستضافة الفعلية، واختبار الطلبات من أصول غير مسموحة ومن ترويسات مزورة."` | — |
| [SRC-855DA3B8BC-L000116](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L116) | 116 | `""` | — |
| [SRC-855DA3B8BC-L000117](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L117) | 117 | `"### A-06 — رمز Bearer مشترك محفوظ في localStorage"` | — |
| [SRC-855DA3B8BC-L000118](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L118) | 118 | `"**النتيجة:** تصميم مقبول لتجربة خاصة بسيطة، لكنه يوسّع أثر أي XSS ولا يقدم هوية أو صلاحيات فردية."` | — |
| [SRC-855DA3B8BC-L000119](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L119) | 119 | `""` | — |
| [SRC-855DA3B8BC-L000120](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L120) | 120 | `"تعالج الواجهات قدرًا كبيرًا من نصوص المستخدم والمصادر عبر escaping، وتتحقق من أن رابط المصدر HTTP(S) ولا يحتوي بيانات مصادقة. لكن صفحة الوكيل وصفحة العملاء تحفظان رمز التطبيق في localStorage؛ الرمز المشترك يعني أن أي سكربت خبيث ينجح في سياق الصفحة يمكنه نظريًا قراءته واستخدام الصلاحيات نفسها. لا توجد جلسات لكل مستخدم أو صلاحيات سجل أو انتهاء صلاحية مدمجة في الرمز."` | — |
| [SRC-855DA3B8BC-L000121](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L121) | 121 | `""` | — |
| [SRC-855DA3B8BC-L000122](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L122) | 122 | `"**المطلوب:** إبقاء الوصول خاصًا ومحدودًا حاليًا، وعدم مشاركة الرمز. إذا تحولت الخدمة إلى عدة مستخدمين، فاستبدال الرمز المشترك بهوية وجلسات أو رموز قصيرة العمر وصلاحيات مناسبة، مع مراجعة CSP واختبارات XSS. لا تُعدّ معالجة escaping وحدها شهادة أمن واجهة."` | — |
| [SRC-855DA3B8BC-L000123](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L123) | 123 | `""` | — |
| [SRC-855DA3B8BC-L000124](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L124) | 124 | `"### A-07 — استمرارية قاعدة SQLite في بيئة النشر غير مثبتة"` | — |
| [SRC-855DA3B8BC-L000125](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L125) | 125 | `"**النتيجة:** UNKNOWN تشغيليًا، وليست عيبًا مؤكدًا في الكود."` | — |
| [SRC-855DA3B8BC-L000126](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L126) | 126 | `""` | — |
| [SRC-855DA3B8BC-L000127](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L127) | 127 | `"يحدد LeadStore المسار الافتراضي تحت مجلد المنزل وينشئ الملف إن لم يوجد. يحتوي render.yaml على خدمة Docker مجانية ومفاتيح بيئة، ولا يوضح ملف الإعداد نفسه قرصًا دائمًا أو استراتيجية نسخ احتياطي واستعادة. لم يُفحص حساب الاستضافة المباشر، ولا توجد في هذه الجولة تجربة restart/redeploy تؤكد بقاء السجلات."` | — |
| [SRC-855DA3B8BC-L000128](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L128) | 128 | `""` | — |
| [SRC-855DA3B8BC-L000129](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L129) | 129 | `"**المطلوب:** تأكيد نظام ملفات الاستضافة وسياسة بقائه رسميًا، وتجربة حفظ سجل ثم إعادة تشغيل/نشر ثم التحقق من بقائه. قبل حفظ بيانات تشغيلية مهمة، إعداد قرص دائم إن كان متاحًا ضمن البيئة أو تخزين دائم بديل ونسخ احتياطي واستعادة مختبرة."` | — |
| [SRC-855DA3B8BC-L000130](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L130) | 130 | `""` | — |
| [SRC-855DA3B8BC-L000131](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L131) | 131 | `"## 5. سجل نتائج جميع متطلبات P0 (42 متطلبًا)"` | — |
| [SRC-855DA3B8BC-L000132](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L132) | 132 | `""` | — |
| [SRC-855DA3B8BC-L000133](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L133) | 133 | `"الحالة هنا تصف قوة الدليل على **تنفيذ المتطلب في النطاق المدقق**، وليست تصنيفًا نهائيًا لكل التطبيق. المراجع المحلية تشير إلى ملف/سطر أو اختبار يدعم النتيجة. وُسِمت البنود المشروطة صراحةً حتى لا تختلط جاهزية مشغّل واحد بجاهزية منصة متعددة المستخدمين."` | — |
| [SRC-855DA3B8BC-L000134](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L134) | 134 | `""` | — |
| [SRC-855DA3B8BC-L000135](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L135) | 135 | `"\| المعرف \| نتيجة التدقيق \| الدليل المرصود والحد المتبقي \|"` | — |
| [SRC-855DA3B8BC-L000136](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L136) | 136 | `"\|---\|---\|---\|"` | — |
| [SRC-855DA3B8BC-L000137](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L137) | 137 | `"\| GOV-001 \| INFERRED \| يعرض وكيل البحث حقولًا مثل search_outcome وresearch_quality_semantics وcitation_validation، وتوجد اختبارات لحفظ UNKNOWN عند فشل البحث؛ لكن لم تُراجع جميع مخرجات المشروع لإثبات أن كل تقرير مؤثر يستخدم حالات موحدة. انظر agents/web_agent.py: 3065–3251 و3583–3642، والاختبارات test_web_agent.py: 1739–1753 و1957–2046 و2310–2345. \|"` | — |
| [SRC-855DA3B8BC-L000138](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L138) | 138 | `"\| GOV-003 \| UNKNOWN \| توجد سياسة للاستثناءات في الدستور وAGENTS.md، لكن لم يُعثر ضمن نطاق ملفات التشغيل المدققة على سجل فعلي للاستثناءات المقبولة وتواريخ انتهائها. غياب السجل من الملفات المفحوصة لا يثبت عدم وجود قرار خارجي؛ يلزم تأكيد واعتماد سجل الاستثناءات. \|"` | — |
| [SRC-855DA3B8BC-L000139](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L139) | 139 | `"\| GOV-005 \| INFERRED \| سياسة عدم الدمج/النشر دون صلاحية بشرية مثبتة في AGENTS.md ووثائق الحوكمة. فُحص workflow الخاص بالاختبارات، لا إعدادات حماية الفروع أو أذونات النشر في الحساب الفعلي؛ إذن enforcement التشغيلي UNKNOWN. \|"` | — |
| [SRC-855DA3B8BC-L000140](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L140) | 140 | `"\| PRD-001 \| INFERRED \| الواجهة تعرض تحذيرًا عندما لا يؤكد النظام البحث الحي، والتشخيص يفرق بين نتائج حقيقية وتعطل الموفر؛ لكن لم تجرِ مراجعة شاملة لكل ادعاءات README والواجهة مقابل كل قدرة تشغيلية. انظر web/agent.html: 204–215 وagents/web_agent.py: 2676–2896. \|"` | — |
| [SRC-855DA3B8BC-L000141](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L141) | 141 | `"\| PRD-003 \| VERIFIED (نطاق جزئي) \| توجد حالات فشل/نقص دليل صريحة واختبارات تمنع ادعاء وجود عميل عند انقطاع البحث، وكذلك fallback للمقتطفات عند غياب النموذج. انظر tests/test_web_agent.py: 101–130 و1220–1268 و1957–2046 و2310–2345. لا يشمل ذلك جميع الموفرين الحقيقيين في الإنتاج. \|"` | — |
| [SRC-855DA3B8BC-L000142](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L142) | 142 | `"\| API-001 \| INFERRED \| API يفرض JSON، حد 200KB، وbody كائنًا، ويفحص السؤال؛ WebAgent يقيد السؤال عند 4000 حرف، والسجل يقيد النص عند 12000. لكن التحقق النوعي الصارم من كل حقول product_terms/location_terms/platform ومدة قراءة body/نهاية الطلب ليس شاملًا. انظر api/omarai.py: 164–247 وagents/web_agent.py: 35–45 وagents/omarai.py: 51–110. \|"` | — |
| [SRC-855DA3B8BC-L000143](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L143) | 143 | `"\| API-002 \| PROPOSED/GAP عند تعدد المستخدمين \| لا يوجد تفويض بحسب مالك السجل؛ كل حامل للرمز نفسه يصل إلى LeadStore واحد مشترك. مناسب فقط لنطاق مشغّل واحد، وغير كافٍ لحسابات مستقلة أو tenants. انظر api/omarai.py: 24–40 و207–240، وagents/omarai.py: 81–124. \|"` | — |
| [SRC-855DA3B8BC-L000144](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L144) | 144 | `"\| API-004 \| VERIFIED (العمليات الحالية فقط) \| LeadStore.add يستخدم fingerprint فريدًا وINSERT OR IGNORE لمنع تكرار السجل؛ ومسودات التواصل تصرح أنها لم تُرسل. لا توجد حاليًا أداة نموذجية ترسل رسائل تلقائيًا. انظر agents/omarai.py: 96–114 وapi/omarai.py: 269–304 وtests/test_omarai.py: 25–47. يجب إعادة التقييم لو أضيف إرسال خارجي. \|"` | — |
| [SRC-855DA3B8BC-L000145](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L145) | 145 | `"\| IDN-001 \| INFERRED / GAP متعدد المستخدمين \| Bearer token يتحقق على مستوى التطبيق فقط؛ لا توجد هوية فردية/أدوار أو تفويض لكل سجل. التوثيق الحالي مناسب للمدخل الخاص أكثر من خدمة متعددة المستخدمين. انظر api/omarai.py: 33–40 و164–180. \|"` | — |
| [SRC-855DA3B8BC-L000146](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L146) | 146 | `"\| IDN-002 \| INFERRED / GAP \| الرمز المشترك يمكن تغييره من إعداد البيئة، لكن لا توجد صلاحية انتهاء/إبطال فردية أو جلسات لكل مستخدم ضمن الكود المرصود. التدوير اليدوي يتطلب إجراء تشغيليًا لم يُختبر في هذه الجولة. \|"` | — |
| [SRC-855DA3B8BC-L000147](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L147) | 147 | `"\| IDN-003 \| PARTIAL \| إنشاء WebAgent مستقل لكل /api/agent مع تصفير حالته يقلل مشاركة mutable search state بين الطلبات. لكن LeadStore عالمي ومشترك ولا توجد owner/tenant keys؛ لذلك عزل بيانات المستخدمين غير متحقق. انظر api/omarai.py: 25–26 و207–213، وagents/web_agent.py: 2897–2915. \|"` | — |
| [SRC-855DA3B8BC-L000148](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L148) | 148 | `"\| IDN-004 \| VERIFIED (نطاق API الحالي) \| المصادقة مطلوبة لمسارات /api في وضع النشر العام، وGET /api/leads محمي، والـ CI smoke يثبت 401 لطلبات غير مصادق عليها. /api/health عام ويكشف بيانات حالة/إعدادات غير سرية نسبيًا؛ يجب عدم خلط ذلك مع حماية بيانات العملاء. انظر api/omarai.py: 130–162 و164–180، وCI container smoke. \|"` | — |
| [SRC-855DA3B8BC-L000149](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L149) | 149 | `"\| SEC-001 \| INFERRED \| مفاتيح النموذج تؤخذ من متغيرات البيئة، وأخطاء النموذج لا تعيد جسم استجابة المزود، و.env وSQLite ضمن .gitignore، ويوجد اختبار تنقيح السر من ناتج benchmark. لم يُنفذ secret scanning لتاريخ Git أو فحص أسرار على تشغيل إنتاج حقيقي في هذا التدقيق. انظر agents/web_agent.py: 268–310 و2150–2277، .gitignore، وtests/test_answer_quality_runner.py: 92–99. \|"` | — |
| [SRC-855DA3B8BC-L000150](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L150) | 150 | `"\| SEC-002 \| PARTIAL \| توجد حماية SSRF متعددة الطبقات في agents/web_agent.py: 183–252 و1769–1874، واختبارات URL محلية وcredentials/file scheme في tests/test_web_agent.py: 148–155. يلزم إضافة اختبارات DNS مختلط، وredirect إلى IP داخلي، وDNS rebinding وIPv6 metadata/الحجم. لا تُعلن SSRF VERIFIED بالكامل قبل هذه الاختبارات. \|"` | — |
| [SRC-855DA3B8BC-L000151](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L151) | 151 | `"\| SEC-003 \| INFERRED \| system prompts تصف نص صفحات الويب كمحتوى غير موثوق، وتفصله في رسالة user عن system policy؛ اختبارات test_web_agent.py: 1269–1337 تفحص الفصل في مسار الإجابة والمراجعة. لا توجد مجموعة red-team شاملة لكل حقن مباشر وغير مباشر أو لكل موصل. \|"` | — |
| [SRC-855DA3B8BC-L000152](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L152) | 152 | `"\| SEC-004 \| N/A مشروط للقدرات الحالية / INFERRED \| لم يظهر منفذ أدوات يمنح النموذج عمليات كتابة أو إرسال خارجية؛ OpenRouter web search اختياري ومقيد بعدد استدعاءات، وواجهات تعديل سجل العملاء تتطلب رمز التطبيق. هذا لا يغطي المستقبل: أي أداة تنفذ فعلًا خارجيًا أو عملية حساسة يجب أن تحصل على policy gate وتفويض مستقلين. انظر agents/web_agent.py: 2150–2200 وapi/omarai.py: 164–247. \|"` | — |
| [SRC-855DA3B8BC-L000153](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L153) | 153 | `"\| SEC-005 \| INFERRED \| جلب الصفحات يستخدم verify=True، والاتصالات الخارجية تستخدم عميلًا/مكتبات افتراضيها تحقق TLS؛ لم يُنفذ اختبار شهادة حية أو اختبار نشر طرف إلى طرف في هذه الجولة. انظر agents/web_agent.py: 1782–1789 و2150–2200. \|"` | — |
| [SRC-855DA3B8BC-L000154](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L154) | 154 | `"\| SEC-006 \| INFERRED \| web/agent.html وweb/dashboard.html تستخدمان escaping للنص الديناميكي والتحقق من الروابط قبل بناء HTML؛ لكن لم يُنفذ اختبار متصفح عدائي يثبت رفض XSS لجميع حقول API، ولم يظهر فحص CSP ضمن الملفات المفحوصة. انظر web/agent.html: 107–145 وweb/dashboard.html: 31–40. \|"` | — |
| [SRC-855DA3B8BC-L000155](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L155) | 155 | `"\| SEC-008 \| PARTIAL \| البحث يعتمد على موصلات محددة وبيانات اعتماد من البيئة، ولا توجد صلاحيات تعسفية يختارها النموذج؛ لكن رمز API مشترك على نطاق التطبيق، ولا توجد صلاحيات لكل مستخدم أو لكل نوع سجل، كما لا يوجد سقف توازي عام. انظر agents/web_agent.py: 1019–1125 وapi/omarai.py: 33–40. \|"` | — |
| [SRC-855DA3B8BC-L000156](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L156) | 156 | `"\| PRI-001 \| PARTIAL \| يوجد تحديد لأطوال السؤال/التاريخ/مقتطفات الصفحات والمصادر المرسلة للنموذج، وتحذير من إرسال أسرار أو بيانات عميل سرية؛ لكن لا توجد مراجعة مكتملة لخريطة الاحتفاظ/الحذف والتسجيل في كل خدمة خارجية، وحد history الكلي يمكن أن يصل إلى عدة عناصر × 4000 حرف. انظر agents/web_agent.py: 35–45 و2117–2130 و2394–2534. \|"` | — |
| [SRC-855DA3B8BC-L000157](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L157) | 157 | `"\| PRI-002 \| INFERRED \| status() يعرض إشعارًا بأن السؤال وبعض مقتطفات الصفحات تُرسل إلى مزود نموذج خارجي؛ ويستخدم fallback model عنوان base_url نفسه في التنفيذ الحالي. لم يتم التحقق من ظهور الإشعار للمستخدم قبل إدخال معلومات حساسة، ولا من شروط موفر خارجي بعينه أو طلب حي. انظر agents/web_agent.py: 311–360 و2150–2277، والواجهة web/agent.html. \|"` | — |
| [SRC-855DA3B8BC-L000158](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L158) | 158 | `"\| REL-001 \| PARTIAL \| توجد مهلات لعمليات الجلب والبحث والنماذج، لكن لا يوجد deadline شامل من بداية HTTP request حتى الرد ولا ميزانية زمنية تنتقل بين المراحل. قد تتراكم مهلات متتابعة/احتياطية مع تعدد الاستعلامات. انظر agents/web_agent.py: 35–45 و1059–1125 و1769–1874 و2150–2277 و2534–2630. \|"` | — |
| [SRC-855DA3B8BC-L000159](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L159) | 159 | `"\| REL-002 \| INFERRED \| عدد نماذج fallback محدود، وعدد استعلامات التخطيط والأدلة الإضافية محدد، ويوجد اختبار لحد طلب DeepSeek؛ لكن لا توجد سياسة backoff موحدة لكل الموفرين ولا ميزانية retry زمنية شاملة. انظر agents/web_agent.py: 997–1018 و2150–2277 و3280–3467، والاختبار test_web_agent.py: 2265–2279. \|"` | — |
| [SRC-855DA3B8BC-L000160](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L160) | 160 | `"\| REL-003 \| VERIFIED (نطاق الاختبارات الحالية) \| اختبارات موثقّة تفصل تعطل البحث عن غياب النتائج وتبقي حالة فشل البحث غير محسومة، واختبارات fallback للمقتطفات/تعذر النموذج موجودة. راجع tests/test_web_agent.py: 101–130 و874–906 و1957–2046 و2280–2299. التشغيل الحي لجميع الموفرين ما زال UNKNOWN. \|"` | — |
| [SRC-855DA3B8BC-L000161](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L161) | 161 | `"\| PER-002 \| PARTIAL \| توجد حدود للطلب والصفحات والنتائج وعدد العمال داخل عملية بحث واحدة. لا يوجد حد عالمي لعدد HTTP worker threads، ولا اختبار حمل يثبت سلوك النظام تحت آلاف الطلبات المتزامنة؛ كما لا يوجد حد إجمالي موحد لتكلفة جميع مراحل الطلب. انظر api/omarai.py: 24–30 و305–319، agents/web_agent.py: 35–45 و1893–1980. \|"` | — |
| [SRC-855DA3B8BC-L000162](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L162) | 162 | `"\| PER-003 \| PROPOSED/GAP \| توجد حدود لكل مرحلة وعدد الاستعلامات وبعض استدعاءات الموفرين، لكن لا توجد ميزانية واحدة قابلة للقياس للزمن وعدد اتصالات النموذج/البحث/جلب الصفحات عبر الطلب كاملًا. هذه الفجوة مشتركة مع A-01 وتحتاج deadline + global semaphore/queue + اختبارات إغلاق الميزانية. \|"` | — |
| [SRC-855DA3B8BC-L000163](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L163) | 163 | `"\| SRH-001 \| VERIFIED لسلوك التشخيص فقط؛ UNKNOWN للتوافر الحي الحالي \| diagnostics() تنفذ مجسات بحث عامة ولا تعتبر وجود مفتاح/اسم موصل دليلًا على نجاحه؛ توجد اختبارات تميز عدم وجود نتائج عن عطل الاتصال. لكنها لا تثبت أن البحث الحي يعمل الآن في حساب الاستضافة أو بمفاتيحك. انظر agents/web_agent.py: 2676–2896 وtests/test_web_agent.py: 826–906 و2245–2299. \|"` | — |
| [SRC-855DA3B8BC-L000164](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L164) | 164 | `"\| EVD-001 \| PARTIAL \| توجد مراجعة نموذجية تطلب دعم الادعاءات من مقتطف المصدر، وطلب إظهار نقص الأدلة، وحد لرقم الاستشهاد؛ لكن لا يوجد تحقق دلالي مستقل لكل claim-source pair. انظر agents/web_agent.py: 2394–2676 و3714–3795، والاختبارات 310–358. \|"` | — |
| [SRC-855DA3B8BC-L000165](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L165) | 165 | `"\| EVD-002 \| PARTIAL \| توجد تعليمات صريحة لاختلاق URL/التواريخ/الأرقام، وتنقية روابط المصدر، وإزالة أرقام الاستشهاد غير الصالحة. لكن لا توجد قاعدة حتمية تثبت أن كل تاريخ أو سعر أو ادعاء ظهر في النص موجود في المصدر؛ تبقى مخاطرة هلوسة غير صفرية. \|"` | — |
| [SRC-855DA3B8BC-L000166](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L166) | 166 | `"\| EVD-004 \| INFERRED \| تقارير البحث تميز بعض حالات insufficient_evidence وfailed وpartial، وتوضح أن research_quality قياس لتغطية العملية لا احتمال صحة، وتفصح أن مراجعة النموذج ليست تحققًا مستقلًا. لكن ليس كل جواب عام يضع وسومًا صريحة لكل معلوم/استنتاج/مقترح/مجهول. انظر agents/web_agent.py: 2676–2896 و3583–3848. \|"` | — |
| [SRC-855DA3B8BC-L000167](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L167) | 167 | `"\| AIG-001 \| INFERRED \| قيود الأمان موجودة في الكود وAPI، ومحتوى الويب يُفصل عن تعليمات النظام؛ لكن policy gate مستقل عن النموذج لا يغطي أفعالًا متنوعة لأن نطاق الأدوات الحالي يغلب عليه البحث فقط. يُعاد التقييم قبل إضافة أدوات ذات آثار جانبية. \|"` | — |
| [SRC-855DA3B8BC-L000168](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L168) | 168 | `"\| AIG-002 \| PARTIAL \| التخطيط bounded بثمانية استعلامات كحد، والبحث المتوازي داخل العملية بثمانية عمال، ومعالجة نقص الأدلة بمحاولة إضافية واحدة في المسار المحدد، وأداة web search الاختيارية بحد max_tool_calls=5. تبقى فجوة توازي الخادم والdeadline الشامل. انظر agents/research.py: 16–18 وagents/web_agent.py: 35–45 و2150–2200 و3280–3467. \|"` | — |
| [SRC-855DA3B8BC-L000169](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L169) | 169 | `"\| AIG-003 \| INFERRED \| المقترح التخطيطي يحلل JSON ثم يمر عبر validate_plan، ويُرفض شكل الرد غير الصالح أو المبتور من النموذج. لا توجد أداة كتابة مفعّلة عبر LLM تحتاج تنفيذ فعل حساس حاليًا؛ ينبغي اختبار schemas مباشرة عند إضافة أي أداة جديدة. انظر agents/web_agent.py: 2278–2394 و2150–2277. \|"` | — |
| [SRC-855DA3B8BC-L000170](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L170) | 170 | `"\| AIG-005 \| INFERRED \| fallback_model يتصل عبر base_url نفسه، وتوجد رسالة خصوصية على إرسال prompts ومقتطفات إلى المزود المضبوط؛ لكن لم تتم مراجعة تدفقات البيانات لكل موصل اجتماعي اختياري أو إجراء فحص حي لمحتوى الطلب المرسل. انظر agents/web_agent.py: 311–360 و2150–2277 وموصلات البحث الاختيارية. \|"` | — |
| [SRC-855DA3B8BC-L000171](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L171) | 171 | `"\| AIG-006 \| N/A مشروط للقدرات الحالية \| لم يُرصد إرسال تلقائي لرسالة أو تنفيذ خارجي على قرار LLM؛ مسودة التواصل توضح أن الإرسال لم يحدث. أي connector جديد يرسل أو يعدّل أو يشتري أو يحذف أو ينشر يجب أن يُعامل كقدرة جديدة مع تحقق صلاحيات وموافقة مناسبة. انظر api/omarai.py: 269–304. \|"` | — |
| [SRC-855DA3B8BC-L000172](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L172) | 172 | `"\| AIE-003 \| PARTIAL \| اختبارات تثبت فصل محتوى الويب غير الموثوق عن system message في مساري التوليد والمراجعة، لكن لم تُثبت بعد مجموعة red-team كاملة بهجمات injection مباشرة/غير مباشرة واختبارات انحدار لكل المصادر. انظر tests/test_web_agent.py: 1269–1337. \|"` | — |
| [SRC-855DA3B8BC-L000173](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L173) | 173 | `"\| TST-003 \| VERIFIED (سياسة اختبارات الجودة) \| test_answer_quality_runner.py يتضمن test_live_records_not_tested_not_pass؛ وسكربت القياس يرفض التشغيل الحي غير المحدود ويصنّف فشل النقل بشكل غير ناجح. أما هذا التدقيق نفسه فلم ينفذ تشغيلًا محليًا، ولذلك يذكر بوضوح أنه لم ينفذ محليًا. انظر tests/test_answer_quality_runner.py: 67–135 و191–232. \|"` | — |
| [SRC-855DA3B8BC-L000174](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L174) | 174 | `"\| SCM-002 \| PARTIAL \| workflow يحدد permissions: contents: read ولا يطلب مفاتيح موفر النموذج لتشغيل الاختبارات، وهذا جيد. لكنه يستخدم actions بالـ major tag مثل checkout@v4 وsetup-python@v5 لا SHA ثابتًا، ولم يظهر ضمن workflow فحص أسرار/ثغرات اعتماديات/CodeQL. لا تُوصف سلسلة التوريد بالمكتملة. انظر .github/workflows/tests.yml: 1–25. \|"` | — |
| [SRC-855DA3B8BC-L000175](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L175) | 175 | `"\| DPL-001 \| UNKNOWN للتوزيع الحقيقي / VERIFIED لاختبار الحاوية على CI \| بنيت الحاوية واختُبر smoke test عند نسخة معروفة من main، لكن لم يتم إثبات أن نشر الاستضافة الفعلي يطابق هذه النسخة، أو أن هناك سجل deployment/rollback يمكن ربطه بالـ commit. انظر .github/workflows/tests.yml وrender.yaml؛ تحقق النشر يحتاج منصة الاستضافة نفسها. \|"` | — |
| [SRC-855DA3B8BC-L000176](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L176) | 176 | `"\| DPL-005 \| INFERRED \| الدستور وAGENTS.md يثبتان قاعدة موافقة مدير المشروع، لكن لم تُقرأ إعدادات branch protection أو deployment protection في حساب GitHub/الاستضافة. وجود نص القاعدة لا يثبت فرضها آليًا. \|"` | — |
| [SRC-855DA3B8BC-L000177](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L177) | 177 | `"\| UX-004 \| INFERRED \| الواجهات تستخدم escapeHtml/esc وتفحص روابط HTTP(S) قبل عرضها؛ هذا يقلل خطر XSS. لم يظهر اختبار متصفح يغطي حمولة عدائية في كل حقل، ولم يظهر CSP في فحص الملفات. انظر web/agent.html: 107–145 وweb/dashboard.html: 31–40. \|"` | — |
| [SRC-855DA3B8BC-L000178](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L178) | 178 | `"\| FIN-001 \| PARTIAL / فجوة مهمة عند النشر العام \| يوجد rate limit 20 طلبًا/60 ثانية لكل عنوان عميل وحدود داخلية للبحث والنماذج، لكن لا يوجد سقف تكلفة أو توازي عالمي، والاحتياط النموذجي يمكن أن يضاعف الطلبات. لا يكفي تحديد المعدل وحده لمنع الحمل المجمع من عدد كبير من العملاء. انظر api/omarai.py: 24–115 وagents/web_agent.py: 2150–2277. \|"` | — |
| [SRC-855DA3B8BC-L000179](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L179) | 179 | `""` | — |
| [SRC-855DA3B8BC-L000180](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L180) | 180 | `"## 6. ماذا نعدّ مثبتًا حاليًا، وماذا لا نعدّه مثبتًا؟"` | — |
| [SRC-855DA3B8BC-L000181](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L181) | 181 | `""` | — |
| [SRC-855DA3B8BC-L000182](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L182) | 182 | `"### مثبت ضمن نطاق محدود"` | — |
| [SRC-855DA3B8BC-L000183](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L183) | 183 | `"1. فحوص Python/Ruff/pytest وDocker smoke test نجحت في GitHub Actions لنسخة main المسجلة."` | — |
| [SRC-855DA3B8BC-L000184](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L184) | 184 | `"2. هناك مصادقة server-side في وضع النشر العام، وحد أقصى لطول جسم الطلب، وحد معدل محلي، وخيارات آمنة افتراضية للربط المحلي."` | — |
| [SRC-855DA3B8BC-L000185](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L185) | 185 | `"3. توجد آليات واضحة للحد من SSRF، وفصل محتوى البحث غير الموثوق، وتنقية HTML في الواجهات، وإزالة أرقام الاستشهاد غير الصالحة."` | — |
| [SRC-855DA3B8BC-L000186](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L186) | 186 | `"4. توجد اختبارات انحدار مهمة للبحث الفاشل، والنقص في الأدلة، وفشل الموفر، ومجموعة من أخطاء النماذج، وفشل HTTP غير المصادق عليه."` | — |
| [SRC-855DA3B8BC-L000187](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L187) | 187 | `"5. أدوات البحث/قراءة الصفحات الحالية لا تنفذ بحد ذاتها إرسال رسائل للناس أو عمليات كتابة خارجية؛ مسودة التواصل ليست إرسالًا."` | — |
| [SRC-855DA3B8BC-L000188](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L188) | 188 | `""` | — |
| [SRC-855DA3B8BC-L000189](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L189) | 189 | `"### استدلالي أو جزئي"` | — |
| [SRC-855DA3B8BC-L000190](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L190) | 190 | `"1. القوة الفعلية لدفاعات SSRF أمام DNS/redirect adversarial inputs."` | — |
| [SRC-855DA3B8BC-L000191](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L191) | 191 | `"2. مقاومة prompt injection عبر طيف كامل من المصادر."` | — |
| [SRC-855DA3B8BC-L000192](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L192) | 192 | `"3. صحة الاستشهادات دلاليًا، لا مجرد صحة فهرس المصدر."` | — |
| [SRC-855DA3B8BC-L000193](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L193) | 193 | `"4. جودة الناتج على أسئلة فعلية متنوعة ومصادر حية عربية/إنجليزية."` | — |
| [SRC-855DA3B8BC-L000194](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L194) | 194 | `"5. متانة حدود الوقت تحت فشل مزود متكرر أو تزامن كبير."` | — |
| [SRC-855DA3B8BC-L000195](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L195) | 195 | `"6. حماية الواجهات من XSS على مستوى كل حقل؛ يوجد escaping لكن التغطية الاختبارية المباشرة محدودة."` | — |
| [SRC-855DA3B8BC-L000196](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L196) | 196 | `""` | — |
| [SRC-855DA3B8BC-L000197](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L197) | 197 | `"### غير معلوم أو غير مستوفى في النطاق الأوسع"` | — |
| [SRC-855DA3B8BC-L000198](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L198) | 198 | `"1. فصل سجلات المستخدمين: غير متاح في نموذج رمز مشترك/مخزن مشترك."` | — |
| [SRC-855DA3B8BC-L000199](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L199) | 199 | `"2. حد توازي عام وdeadline موحد: لا تظهر لهما آلية كافية في الكود الحالي."` | — |
| [SRC-855DA3B8BC-L000200](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L200) | 200 | `"3. استمرارية البيانات على الاستضافة الفعلية والنسخ الاحتياطي والاستعادة."` | — |
| [SRC-855DA3B8BC-L000201](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L201) | 201 | `"4. قواعد حساب GitHub/الاستضافة التي تفرض الموافقة البشرية عمليًا."` | — |
| [SRC-855DA3B8BC-L000202](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L202) | 202 | `"5. سلامة الاتصال الحي بمفاتيحك ومزوديك من بيئة النشر الحالية."` | — |
| [SRC-855DA3B8BC-L000203](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L203) | 203 | `"6. نتائج load test أو اختبار اختراق حي أو مراجعة قانونية/امتثال."` | — |
| [SRC-855DA3B8BC-L000204](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L204) | 204 | `""` | — |
| [SRC-855DA3B8BC-L000205](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L205) | 205 | `"## 7. خطة إغلاق بالترتيب"` | — |
| [SRC-855DA3B8BC-L000206](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L206) | 206 | `""` | — |
| [SRC-855DA3B8BC-L000207](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L207) | 207 | `"### Gate 1 — قبل توسيع الوصول العام"` | — |
| [SRC-855DA3B8BC-L000208](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L208) | 208 | `"1. إضافة global semaphore/queue محدودة لطلبات الوكيل و/أو عمليات البحث والنماذج، مع رفض ازدحام واضح."` | — |
| [SRC-855DA3B8BC-L000209](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L209) | 209 | `"2. تطبيق deadline موحد يمرر الوقت المتبقي إلى البحث وجلب الصفحة وكل استدعاء نموذج، ويمنع بدء مراحل لا يمكن إكمالها ضمن الميزانية."` | — |
| [SRC-855DA3B8BC-L000210](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L210) | 210 | `"3. وضع حدود صريحة للتوازي وعدد صفحات fetch وإجمالي model calls لكل طلب ونمط؛ توثيق سقف التكلفة والقياس."` | — |
| [SRC-855DA3B8BC-L000211](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L211) | 211 | `"4. اختبار سوء استخدام عبر طلبات متزامنة وموفر متأخر/معلق، وتأكيد أن عدد الخيوط والمهام لا يرتفع بلا سقف."` | — |
| [SRC-855DA3B8BC-L000212](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L212) | 212 | `""` | — |
| [SRC-855DA3B8BC-L000213](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L213) | 213 | `"### Gate 2 — تحديد نموذج المستخدمين"` | — |
| [SRC-855DA3B8BC-L000214](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L214) | 214 | `"1. تسجيل قرار منتج صريح: هل Omarai حاليًا تطبيق خاص بمشغّل واحد أم خدمة متعددة المستخدمين؟"` | — |
| [SRC-855DA3B8BC-L000215](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L215) | 215 | `"2. إذا خاص بمشغّل واحد: وثّق ذلك في README والواجهة وسياسة الخصوصية، واحتفظ بالرمز سرًا، ولا تفتح مشاركة السجلات."` | — |
| [SRC-855DA3B8BC-L000216](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L216) | 216 | `"3. إذا متعدد المستخدمين: إضافة user_id/tenant_id وسياق هوية في API وقاعدة البيانات، وحصر list/update لكل مالك، وتغيير الرمز المشترك لجلسات/رموز فردية، واختبار A لا يرى أو يعدّل بيانات B."` | — |
| [SRC-855DA3B8BC-L000217](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L217) | 217 | `""` | — |
| [SRC-855DA3B8BC-L000218](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L218) | 218 | `"### Gate 3 — استكمال اختبارات الأمن"` | — |
| [SRC-855DA3B8BC-L000219](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L219) | 219 | `"1. SSRF: private/mixed DNS، DNS rebinding، redirect إلى localhost/127.0.0.1/169.254.169.254 وIPv6 link-local، port/protocol variants وحجم غير محدود."` | — |
| [SRC-855DA3B8BC-L000220](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L220) | 220 | `"2. Prompt injection: تعليمات هجومية في title/snippet/full page ونتائج اجتماعية، والتأكد من أنها لا تغير policy ولا تكشف secrets ولا تتجاوز tool permissions."` | — |
| [SRC-855DA3B8BC-L000221](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L221) | 221 | `"3. XSS/HTML: حمولة عدائية في title/snippet/URL/lead text/platform/note وأخطاء API، مع اختبار في متصفح أو مختبر واجهة مناسب."` | — |
| [SRC-855DA3B8BC-L000222](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L222) | 222 | `"4. CORS/proxy: origins مزورة، Host/X-Forwarded-Host/X-Forwarded-Proto غير موثوقين، وسلوك العنوان الحقيقي تحت الوكيل العكسي."` | — |
| [SRC-855DA3B8BC-L000223](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L223) | 223 | `""` | — |
| [SRC-855DA3B8BC-L000224](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L224) | 224 | `"### Gate 4 — صدق الأدلة"` | — |
| [SRC-855DA3B8BC-L000225](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L225) | 225 | `"1. إضافة corpus مرجعي فيه ادعاء مدعوم، وادعاء غير مدعوم، ومصدر متعارض، ومصدر قديم، ورابط لا يدعم النص."` | — |
| [SRC-855DA3B8BC-L000226](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L226) | 226 | `"2. قياس precision وrecall لدعم الادعاءات والاستشهادات بدل الاعتماد على مراجعة نموذج فقط."` | — |
| [SRC-855DA3B8BC-L000227](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L227) | 227 | `"3. الحفاظ على metadata الحالية التي تفرق بين فحص index-range وبين fact check."` | — |
| [SRC-855DA3B8BC-L000228](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L228) | 228 | `"4. عدم تسمية الجودة good/excellent ضمانًا لصحة الحقيقة؛ إنها حاليًا تشير إلى تغطية عملية البحث كما تقول metadata نفسها."` | — |
| [SRC-855DA3B8BC-L000229](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L229) | 229 | `""` | — |
| [SRC-855DA3B8BC-L000230](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L230) | 230 | `"### Gate 5 — إثبات النشر والتخزين"` | — |
| [SRC-855DA3B8BC-L000231](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L231) | 231 | `"1. تشغيل live diagnostics من البيئة المنشورة مع عرض النتائج الفعلية دون كشف الأسرار."` | — |
| [SRC-855DA3B8BC-L000232](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L232) | 232 | `"2. ربط deployment بوضوح مع commit محدد."` | — |
| [SRC-855DA3B8BC-L000233](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L233) | 233 | `"3. حفظ سجل اختبار، ثم restart/redeploy، ثم التحقق من استمرار البيانات أو توثيق كونها مؤقتة."` | — |
| [SRC-855DA3B8BC-L000234](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L234) | 234 | `"4. إعداد نسخة احتياطية وتجربة استعادة إن كانت البيانات لا يمكن تعويضها."` | — |
| [SRC-855DA3B8BC-L000235](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L235) | 235 | `""` | — |
| [SRC-855DA3B8BC-L000236](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L236) | 236 | `"## 8. متى نسمح بالانتقال للمرحلة التالية؟"` | — |
| [SRC-855DA3B8BC-L000237](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L237) | 237 | `""` | — |
| [SRC-855DA3B8BC-L000238](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L238) | 238 | `"لا نعتمد التقدم على انطباع عام. شروط البوابة المقترحة:"` | — |
| [SRC-855DA3B8BC-L000239](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L239) | 239 | `"- [ ] اختبار deadline شامل يثبت توقف مراحل البحث والنموذج قبل تجاوز حد الطلب."` | — |
| [SRC-855DA3B8BC-L000240](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L240) | 240 | `"- [ ] اختبار توازٍ يثبت أن عدد الطلبات المكلفة المتزامنة محدود."` | — |
| [SRC-855DA3B8BC-L000241](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L241) | 241 | `"- [ ] قرار نطاق موثق: single-operator أو multi-user؛ وإذا multi-user، تمر جميع اختبارات العزل."` | — |
| [SRC-855DA3B8BC-L000242](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L242) | 242 | `"- [ ] نجاح اختبارات SSRF adversarial الجديدة."` | — |
| [SRC-855DA3B8BC-L000243](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L243) | 243 | `"- [ ] نجاح اختبارات prompt injection وXSS الجديدة."` | — |
| [SRC-855DA3B8BC-L000244](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L244) | 244 | `"- [ ] مجموعة تقييم citations/claim-support بنتائج مسجلة، وحدود قبول متفق عليها."` | — |
| [SRC-855DA3B8BC-L000245](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L245) | 245 | `"- [ ] مراجعة تهيئة الوكيل العكسي وOrigin وrate limit في منصة الاستضافة الفعلية."` | — |
| [SRC-855DA3B8BC-L000246](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L246) | 246 | `"- [ ] إثبات استمرارية قاعدة البيانات أو تنبيه المستخدم بوضوح أنها غير دائمة."` | — |
| [SRC-855DA3B8BC-L000247](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L247) | 247 | `"- [ ] إرفاق commit لكل تغيير، ونتائج CI لكل نسخة، وتحديث سجل المتطلبات بالحالة والدليل."` | — |
| [SRC-855DA3B8BC-L000248](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L248) | 248 | `""` | — |
| [SRC-855DA3B8BC-L000249](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L249) | 249 | `"لا تعني كل هذه البنود أن يجب بناء بنية ضخمة. يمكن معالجة كثير منها داخل التطبيق الحالي؛ المطلوب هو وضع الحدود الصحيحة، ثم اختبارها."` | — |
| [SRC-855DA3B8BC-L000250](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L250) | 250 | `""` | — |
| [SRC-855DA3B8BC-L000251](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L251) | 251 | `"## 9. الخلاصة النهائية"` | — |
| [SRC-855DA3B8BC-L000252](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L252) | 252 | `""` | — |
| [SRC-855DA3B8BC-L000253](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L253) | 253 | `"**Omarai يسير في اتجاه هندسي صحيح أكثر مما يوحي به كونه مشروعًا صغيرًا: توجد اختبارات، وإخفاقات تُعامل بصدق، وضوابط شبكة، ومراجعة للأدلة، وواجهات تُنقّي النصوص، وأساس CI جيد. وهذه نتيجة إيجابية مدعومة بدليل.**"` | — |
| [SRC-855DA3B8BC-L000254](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L254) | 254 | `""` | — |
| [SRC-855DA3B8BC-L000255](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L255) | 255 | `"لكن التأكيد الاحترافي ليس «مطابق 100%». النتيجة الأدق هي:"` | — |
| [SRC-855DA3B8BC-L000256](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L256) | 256 | `"- **مناسب للاستمرار في التطوير والاختبار كنسخة خاصة ذات نطاق محدود، بشروط واضحة.**"` | — |
| [SRC-855DA3B8BC-L000257](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L257) | 257 | `"- **غير مثبت بعد كخدمة عامة متعددة المستخدمين ذات ميزانية تشغيل شاملة واستشهادات متحققة دلاليًا.**"` | — |
| [SRC-855DA3B8BC-L000258](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L258) | 258 | `"- **الأولوية القادمة ليست إضافة مزيد من المصطلحات أو الخدمات؛ بل إغلاق A-01 وA-02 وA-03 وA-04 واختبارها، ثم تحديث حالات سجل المتطلبات من UNKNOWN إلى حالات مدعومة بالأدلة.**"` | — |
| [SRC-855DA3B8BC-L000259](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L259) | 259 | `""` | — |
| [SRC-855DA3B8BC-L000260](../OMARAI_P0_CODING_AUDIT_2026-10-19_AR.md#L260) | 260 | `"هذا التقرير لا يغيّر الكود ولا ينشر التطبيق. الغرض منه تثبيت صورة صادقة عن الوضع الحالي وتحديد أقصر مسار إلى جاهزية أعلى."` | — |
## وثائق وفهرسة

### FILE-62CE5126F9 — [docs/OMARAI_REMEDIATION_REGISTER_AR.md](../OMARAI_REMEDIATION_REGISTER_AR.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-62CE5126F9-L000001](../OMARAI_REMEDIATION_REGISTER_AR.md#L1) | 1 | `"# سجل الإغلاق الهندسي المركزي لمشروع Omarai"` | — |
| [SRC-62CE5126F9-L000002](../OMARAI_REMEDIATION_REGISTER_AR.md#L2) | 2 | `""` | — |
| [SRC-62CE5126F9-L000003](../OMARAI_REMEDIATION_REGISTER_AR.md#L3) | 3 | `"**المعرّف:** OMARAI-REMEDIATION-REGISTER-001  "` | — |
| [SRC-62CE5126F9-L000004](../OMARAI_REMEDIATION_REGISTER_AR.md#L4) | 4 | `"**تاريخ اللقطة:** 2026-10-21  "` | — |
| [SRC-62CE5126F9-L000005](../OMARAI_REMEDIATION_REGISTER_AR.md#L5) | 5 | ``"**خط أساس PR #76:** `main` عند `d46a546aba97a9ca32a32c92f1cd6d8a9db2cc81`  "`` | — |
| [SRC-62CE5126F9-L000006](../OMARAI_REMEDIATION_REGISTER_AR.md#L6) | 6 | ``"**الفرع:** `fix/audit-closure-current-main-2026-10-21`  "`` | — |
| [SRC-62CE5126F9-L000007](../OMARAI_REMEDIATION_REGISTER_AR.md#L7) | 7 | ``"**رأس الكود/Workflow اجتاز CI كاملًا:** `f2f1bb3c87c709383e0a8c18691f46cd3661e61b`. **رأس PR عند هذه اللقطة:** `b848f96ab992dd876237f399391f69996151426e`؛ ما بعد الرأس المختبَر يتكون من تغييرات توثيق التدقيق وصفحات الفهرس المولّدة فقط، بلا تغييرات لاحقة في التطبيق أو الاختبارات أو Workflow. راجع رأس PR الحي قبل القرار."`` | — |
| [SRC-62CE5126F9-L000008](../OMARAI_REMEDIATION_REGISTER_AR.md#L8) | 8 | `""` | — |
| [SRC-62CE5126F9-L000009](../OMARAI_REMEDIATION_REGISTER_AR.md#L9) | 9 | `"## دليل الاختبارات وحالة الرأس الحالي"` | — |
| [SRC-62CE5126F9-L000010](../OMARAI_REMEDIATION_REGISTER_AR.md#L10) | 10 | `""` | — |
| [SRC-62CE5126F9-L000011](../OMARAI_REMEDIATION_REGISTER_AR.md#L11) | 11 | ``"- **أحدث تشغيل PR أخضر:** [#39653079608](https://github.com/mosabosama2030-oss/omarai/actions/runs/39653079608) على `f2f1bb3c87c709383e0a8c18691f46cd3661e61b`: **384 اختبارًا ناجحًا على Python 3.11 و384 على Python 3.12**، وRuff وفحص الفهرس وبناء الحاوية واختبار API المحمي ناجحة."`` | — |
| [SRC-62CE5126F9-L000012](../OMARAI_REMEDIATION_REGISTER_AR.md#L12) | 12 | `"- **تحقق push مستقل للرأس نفسه:** [#39653072071](https://github.com/mosabosama2030-oss/omarai/actions/runs/39653072071) — وظائف Python 3.11 و3.12 وبناء الحاوية ناجحة. كما نجح نشر/تحديث الفهرس في [#39653072074](https://github.com/mosabosama2030-oss/omarai/actions/runs/39653072074)."` | — |
| [SRC-62CE5126F9-L000013](../OMARAI_REMEDIATION_REGISTER_AR.md#L13) | 13 | ``"- **سبب الفشل التاريخي وحله:** فحص الفهرس كان يتنافس مع workflow منفصل ينشر الملفات المولدة. عُدّل `.github/workflows/tests.yml` بحيث تُعاد توليدات الفهرس داخل مساحة الاختبار المؤقتة لكل مرجع غير `main` قبل فحص الاتساق؛ يظل فحص `main` صارمًا على الملفات الملتزمة. نجح مسارا push وPR بعد التعديل."`` | — |
| [SRC-62CE5126F9-L000014](../OMARAI_REMEDIATION_REGISTER_AR.md#L14) | 14 | ``"- **حدّ الدليل:** الرأس الحالي `8198aabc95ce426948d7a233e966c0bbad5e54b7` يتضمن لاحقًا تغييرات في سجل/تقرير التدقيق وفهرس مولد فقط؛ لا توجد تغييرات تطبيق/اختبارات/Workflow بعد الرأس الأخضر. لا نزعم تشغيل pytest مستقلًا على كل commit مولد لاحق."`` | — |
| [SRC-62CE5126F9-L000015](../OMARAI_REMEDIATION_REGISTER_AR.md#L15) | 15 | `"- التشغيل المستضاف الحقيقي، وعمل الموصلات الحية، والدوام/النسخ الاحتياطي والاستعادة، والحمل، والاختبار الأحمر المستقل تبقى خارج نطاق دليل CI."` | — |
| [SRC-62CE5126F9-L000016](../OMARAI_REMEDIATION_REGISTER_AR.md#L16) | 16 | `""` | — |
| [SRC-62CE5126F9-L000017](../OMARAI_REMEDIATION_REGISTER_AR.md#L17) | 17 | `"## معاني الحالات"` | — |
| [SRC-62CE5126F9-L000018](../OMARAI_REMEDIATION_REGISTER_AR.md#L18) | 18 | `""` | — |
| [SRC-62CE5126F9-L000019](../OMARAI_REMEDIATION_REGISTER_AR.md#L19) | 19 | `"- **FIXED_AND_TESTED:** الإصلاح موجود في الالتزام المذكور ونجحت اختبارات مرتبطة به على الالتزام نفسه."` | — |
| [SRC-62CE5126F9-L000020](../OMARAI_REMEDIATION_REGISTER_AR.md#L20) | 20 | `"- **PARTIAL:** يوجد تنفيذ أو اختبار أو تحديث جزئي، لكن شرط الإغلاق لم يكتمل."` | — |
| [SRC-62CE5126F9-L000021](../OMARAI_REMEDIATION_REGISTER_AR.md#L21) | 21 | `"- **NOT_RUN:** الاختبار المطلوب لم يُنفذ."` | — |
| [SRC-62CE5126F9-L000022](../OMARAI_REMEDIATION_REGISTER_AR.md#L22) | 22 | `"- **UNKNOWN:** لا توجد أدلة كافية للحكم."` | — |
| [SRC-62CE5126F9-L000023](../OMARAI_REMEDIATION_REGISTER_AR.md#L23) | 23 | `"- **PROPOSED:** فكرة أو تحسين لم يُنفذ."` | — |
| [SRC-62CE5126F9-L000024](../OMARAI_REMEDIATION_REGISTER_AR.md#L24) | 24 | `"- **NOT_REQUIRED:** ثبت عدم الحاجة إلى الوظيفة في النطاق الحالي مع توثيق السبب."` | — |
| [SRC-62CE5126F9-L000025](../OMARAI_REMEDIATION_REGISTER_AR.md#L25) | 25 | `""` | — |
| [SRC-62CE5126F9-L000026](../OMARAI_REMEDIATION_REGISTER_AR.md#L26) | 26 | `"## A. سجل الأخطاء والجذور"` | — |
| [SRC-62CE5126F9-L000027](../OMARAI_REMEDIATION_REGISTER_AR.md#L27) | 27 | `""` | — |
| [SRC-62CE5126F9-L000028](../OMARAI_REMEDIATION_REGISTER_AR.md#L28) | 28 | `"\| المعرّف \| الأصل \| الخطورة \| السبب الجذري \| موضع العمل \| الحالة الحالية والدليل \| معيار الإغلاق \|"` | — |
| [SRC-62CE5126F9-L000029](../OMARAI_REMEDIATION_REGISTER_AR.md#L29) | 29 | `"\|---\|---\|---:\|---\|---\|---\|---\|"` | — |
| [SRC-62CE5126F9-L000030](../OMARAI_REMEDIATION_REGISTER_AR.md#L30) | 30 | ``"\| OMR-E-001 \| Grok E1؛ تدقيق النواة \| P1 \| الأسئلة المرجعية القصيرة كانت تفتقر لقواعد غموض موحدة \| `agents/intent_router.py`, `agents/web_agent.py`, `tests/test_intent_router.py` \| **FIXED_AND_TESTED على رأس #76 `f2f1bb3...`** — اختبارات حالات غامضة وبدون/مع سياق ضمن 384 اختبارًا ناجحًا في كلا إصدارَي Python \| يبقى السؤال المنفرد بلا مرجع CLARIFY؛ ومع السياق الصحيح يوجه للبحث؛ ولا يُسترجع موضوع قديم بعد الشكر \|"`` | — |
| [SRC-62CE5126F9-L000031](../OMARAI_REMEDIATION_REGISTER_AR.md#L31) | 31 | ``"\| OMR-E-002 \| Grok E2 \| P1 \| منطق المتابعة كان موزعًا وقد يسترجع موضوعًا سابقًا غير صالح \| `agents/intent_router.py`, `agents/research.py`, `agents/web_agent.py` واختباراتها \| **FIXED_AND_TESTED على رأس #76 `f2f1bb3...`** — حل متابعة موحد وحدود طول/سياق واختبارات \| سعر/ضمان/مقارنة مع سياق؛ وCLARIFY عند غياب المرجع؛ ورفض السياق القديم \|"`` | — |
| [SRC-62CE5126F9-L000032](../OMARAI_REMEDIATION_REGISTER_AR.md#L32) | 32 | ``"\| OMR-E-003 \| Grok E3 \| P1 \| عرض تغطية الأدلة كدرجة رقمية يمكن فهمها خطأً كاحتمال صحة \| `web/agent.html`, `agents/web_agent.py` \| **FIXED_AND_TESTED ON MAIN** — #75 مدمج في `main` \| بقاء الوصف نوعيًا وعدم عودة مؤشر /100 \|"`` | — |
| [SRC-62CE5126F9-L000033](../OMARAI_REMEDIATION_REGISTER_AR.md#L33) | 33 | ``"\| OMR-E-004 \| Grok E4 \| P1 \| استخدام نص `deep/standard` كقيمة منطقية يجعل كلاهما truthy \| `agents/research.py`, `tests/test_research.py` \| **FIXED_AND_TESTED ON MAIN** — #75 مدمج واختبارات المستوى القياسي والعميق \| لا يستدعي السؤال القياسي زاوية عميقة بلا داعٍ \|"`` | — |
| [SRC-62CE5126F9-L000034](../OMARAI_REMEDIATION_REGISTER_AR.md#L34) | 34 | ``"\| OMR-E-005 \| Grok E5 \| P1 \| إعداد الحاوية وحده لا يربط الخدمة المنشورة بالالتزام الفعلي \| `Dockerfile`, `api/omarai.py`, `scripts/hosted_smoke_test.py`, workflow \| **CODE PATH TESTED; HOSTED NOT_RUN** — SHA مخبوز في صورة Docker ومقارن في hosted smoke؛ لا توجد خدمة فعلية اختُبرت \| نجاح hosted smoke على خدمة معتمدة ومطابقة SHA الفعلي \|"`` | — |
| [SRC-62CE5126F9-L000035](../OMARAI_REMEDIATION_REGISTER_AR.md#L35) | 35 | ``"\| OMR-E-006 \| تقرير التدقيق الموحد \| P1 \| تطابق لفظي أو رابط لا يثبت أن المصدر يستلزم الادعاء دلاليًا \| `agents/answer_validation.py`, `agents/web_agent.py`, tests \| **PARTIAL / CODE TESTED** — إشارة لفظية أكثر تحفظًا واختبارات regression؛ يصرح النظام أن entailment لم يُفحص \| تقييم دلالي مستقل للحالات المرجعية؛ لا يُعرض الفحص اللفظي كتحقق حقيقة \|"`` | — |
| [SRC-62CE5126F9-L000036](../OMARAI_REMEDIATION_REGISTER_AR.md#L36) | 36 | ``"\| OMR-E-007 \| تقرير التدقيق الموحد \| P1 \| العدادات قد تخلط النتائج ومحاولات الجلب والنص المستخرج والفشل \| `agents/web_agent.py`, `tests/test_connector_summary_counters.py` \| **FIXED_AND_TESTED على رأس #76 `f2f1bb3...`** — حالات الجلب وتشخيصات الموصلات تختبرها CI \| حالات العدادات والفشل الجزئي ممثلة في اختبارات؛ نجاح الموفر الحي يظل اختبارًا منفصلًا \|"`` | — |
| [SRC-62CE5126F9-L000037](../OMARAI_REMEDIATION_REGISTER_AR.md#L37) | 37 | ``"\| OMR-E-008 \| تقرير التدقيق الموحد \| P1 \| موفرو البحث قد يتبعون تحويلات غير آمنة \| `agents/web_agent.py`, `tests/test_web_agent.py` \| **FIXED_AND_TESTED على رأس #76 `f2f1bb3...`** — تعطيل auto-redirect لموفري DuckDuckGo/Bing/Google News واختبارات redirect \| رفض الوجهات غير العامة في كل hop؛ لا يُعمم هذا على موفر لم تختبره الاختبارات \|"`` | — |
| [SRC-62CE5126F9-L000038](../OMARAI_REMEDIATION_REGISTER_AR.md#L38) | 38 | `""` | — |
| [SRC-62CE5126F9-L000039](../OMARAI_REMEDIATION_REGISTER_AR.md#L39) | 39 | `"## B. العيوب الأمنية والتشغيلية"` | — |
| [SRC-62CE5126F9-L000040](../OMARAI_REMEDIATION_REGISTER_AR.md#L40) | 40 | `""` | — |
| [SRC-62CE5126F9-L000041](../OMARAI_REMEDIATION_REGISTER_AR.md#L41) | 41 | `"\| المعرّف \| الأصل \| الخطورة \| السبب/الأثر \| الحالة \| معيار الإغلاق \|"` | — |
| [SRC-62CE5126F9-L000042](../OMARAI_REMEDIATION_REGISTER_AR.md#L42) | 42 | `"\|---\|---\|---:\|---\|---\|---\|"` | — |
| [SRC-62CE5126F9-L000043](../OMARAI_REMEDIATION_REGISTER_AR.md#L43) | 43 | ``"\| OMR-D-001 \| Grok D1 \| P1 \| رؤوس الحماية للمتصفح لم تكن موحدة على الاستجابات \| `api/omarai.py`, `tests/test_api.py` \| **FIXED_AND_TESTED على رأس #76 `f2f1bb3...`** — CSP وX-Frame-Options وReferrer-Policy وPermissions-Policy وnosniff واختبارات على HTML/JSON \| استمرار الاختبارات وعدم تراجع أي رأس \|"`` | — |
| [SRC-62CE5126F9-L000044](../OMARAI_REMEDIATION_REGISTER_AR.md#L44) | 44 | ``"\| OMR-D-002 \| مراجعة CSP \| P1 \| `unsafe-inline` يضعف سياسة CSP \| `api/omarai.py`, `tests/test_api.py`, `web/*.html` \| **FIXED_AND_TESTED على رأس #76 `f2f1bb3...`** — hashes لمحتوى inline موثوق، مع `unsafe-hashes` لما يلزم، واختبار يرفض `unsafe-inline` \| لا تسمح السياسة بـunsafe-inline؛ كل تغيير HTML/JS/CSS يمر باختبار CSP \|"`` | — |
| [SRC-62CE5126F9-L000045](../OMARAI_REMEDIATION_REGISTER_AR.md#L45) | 45 | ``"\| OMR-D-003 \| Grok D2 \| P1 \| كشف الأسئلة الناقصة لم يكن موحدًا \| `agents/intent_router.py`, `tests/test_intent_router.py` \| **FIXED_AND_TESTED على رأس #76 `f2f1bb3...`** — مربوط بـE1 \| مصدر واحد لقواعد الغموض واختبارات regression \|"`` | — |
| [SRC-62CE5126F9-L000046](../OMARAI_REMEDIATION_REGISTER_AR.md#L46) | 46 | ``"\| OMR-D-004 \| Grok D3 \| P1 \| قد يخلط المستهلك بين الإشارات اللفظية والتحقق الدلالي \| `agents/answer_validation.py`, `agents/web_agent.py`, UI, tests \| **FIXED_AND_TESTED لحدود العرض في #76** — prompts وواجهة النتائج لا تقدمان الإشارة اللفظية كشهادة حقيقة؛ التقييم الدلالي الكامل لا يزال NOT_RUN \| لا تعرض «تحقق مستقل» دون اختبار مرجعي/مراجع مناسب \|"`` | — |
| [SRC-62CE5126F9-L000047](../OMARAI_REMEDIATION_REGISTER_AR.md#L47) | 47 | `"\| OMR-D-005 \| Grok D4 \| P1 \| توثيق النشر أحادي المشغل لم يوضح حدود الهوية بما يكفي \| README ودلائل النشر وقائمة Go-Live ونطاق التنفيذ \| **DOCUMENTED_IN #76** — النص يصرح بأن الرمز المشترك ليس هوية مستخدمين \| اتساق الوثائق وأن لا يُعلن تعدد المستأجرين \|"` | — |
| [SRC-62CE5126F9-L000048](../OMARAI_REMEDIATION_REGISTER_AR.md#L48) | 48 | `"\| OMR-D-006 \| Grok D5 \| P0 للإطلاق العام متعدد المستخدمين \| لا توجد هوية وتفويض وعزلة مثبتة لكل مستأجر \| نطاق التشغيل الحالي \| **NOT_REQUIRED للنطاق أحادي المشغل؛ BLOCKER لأي خدمة متعددة المستأجرين** \| لا تُدخل عدة عملاء/بيانات سرية قبل هوية وعزل واختباراتهما \|"` | — |
| [SRC-62CE5126F9-L000049](../OMARAI_REMEDIATION_REGISTER_AR.md#L49) | 49 | ``"\| OMR-D-007 \| تقرير التدقيق الموحد \| P1 \| مسار SQLite القابل للتعيين لا ينشئ Volume دائمًا ولا نسخة احتياطية \| `agents/omarai.py`, tests, deploy docs \| **CODE PATH TESTED; DURABILITY NOT_RUN** — `OMARAI_DB_PATH` يحدد المسار واختبار الملف ينجح؛ لم تختبر استضافة فعلية \| بقاء البيانات بعد restart/redeploy واختبار restore من نسخة احتياطية على مضيف مختار \|"`` | — |
| [SRC-62CE5126F9-L000050](../OMARAI_REMEDIATION_REGISTER_AR.md#L50) | 50 | `"\| OMR-D-008 \| تقرير التدقيق الموحد \| P1 للتوسع العام \| حدود المعدل والتزامن في الذاكرة تخص العملية الواحدة \| API/RequestBudget/وثائق النطاق \| **KNOWN LIMITATION / DOCUMENTED** — مناسب فقط للنطاق أحادي المشغل؛ لا يوجد إثبات rate-limit موزع \| قبل نشر متعدد النسخ، طبّق حدًا موزعًا واختبره؛ لا تدّع السعة دون قياس \|"` | — |
| [SRC-62CE5126F9-L000051](../OMARAI_REMEDIATION_REGISTER_AR.md#L51) | 51 | `"\| OMR-D-009 \| تقرير التدقيق الموحد \| P1 \| أخطاء مزود خارجي أو سياق إلى نموذج قد يكشف تفاصيل حساسة إن لم تُنقّح \| تشخيصات الموصلات، redaction، tests \| **PARTIAL / CODE TESTED** — تنقيح وتشخيصات per-request ضمن #76؛ يلزم استمرار تغطية جميع مسارات الأخطاء \| اختبارات تمنع ظهور API keys/Bearer tokens والبيانات السرية في الردود والسجلات \|"` | — |
| [SRC-62CE5126F9-L000052](../OMARAI_REMEDIATION_REGISTER_AR.md#L52) | 52 | ``"\| OMR-D-010 \| Grok W4 \| P1 \| تعليمات صفحات الويب غير الموثوقة قد تُعامل كتعليمات تنفيذ \| prompts، `tests/test_web_agent.py` \| **FIXED_AND_TESTED للحدود الحتمية في #76؛ RED-TEAM حي NOT_RUN** — يوجد اختبار يبقي النص الخبيث خارج system prompt \| اجتياز حالات حقن تعليمات محددة؛ مراجعة red-team أوسع تتطلب بيئة/موافقة \|"`` | — |
| [SRC-62CE5126F9-L000053](../OMARAI_REMEDIATION_REGISTER_AR.md#L53) | 53 | `""` | — |
| [SRC-62CE5126F9-L000054](../OMARAI_REMEDIATION_REGISTER_AR.md#L54) | 54 | `"## C. فجوات الاختبار والجودة"` | — |
| [SRC-62CE5126F9-L000055](../OMARAI_REMEDIATION_REGISTER_AR.md#L55) | 55 | `""` | — |
| [SRC-62CE5126F9-L000056](../OMARAI_REMEDIATION_REGISTER_AR.md#L56) | 56 | `"\| المعرّف \| الأصل \| الخطورة \| الحالة \| ما يلزم للإغلاق \|"` | — |
| [SRC-62CE5126F9-L000057](../OMARAI_REMEDIATION_REGISTER_AR.md#L57) | 57 | `"\|---\|---\|---:\|---\|---\|"` | — |
| [SRC-62CE5126F9-L000058](../OMARAI_REMEDIATION_REGISTER_AR.md#L58) | 58 | ``"\| OMR-T-001 \| تقريرا التدقيق \| P0 للإنتاج \| hosted smoke حي \| `scripts/hosted_smoke_test.py`, workflow \| **NOT_RUN** — لا توجد خدمة فعلية وأسرار اختبار معتمدة \| خدمة HTTPS يملكها المدير، أسرار آمنة، وتطابق SHA واجتياز البحث والنموذج والمصادقة \|"`` | — |
| [SRC-62CE5126F9-L000059](../OMARAI_REMEDIATION_REGISTER_AR.md#L59) | 59 | `"\| OMR-T-002 \| تقريرا التدقيق \| P1 \| مزودو البحث والنماذج الحية \| diagnostics/hosted smoke \| **NOT_RUN** لكل موفر على بيئة مستضافة؛ CI لا يثبت الإتاحة الخارجية \| اختبار كل موفر مفعّل على حدة بميزانية/وقت موثقين \|"` | — |
| [SRC-62CE5126F9-L000060](../OMARAI_REMEDIATION_REGISTER_AR.md#L60) | 60 | `"\| OMR-T-003 \| تقريرا التدقيق \| P1 \| تشغيل AQ-001–045 وتقييم الإجابات دلاليًا \| benchmark runner/fixtures/tests \| **PARTIAL / LIVE QUALITY NOT_RUN** — بنية الحالات موجودة والاختبارات الآلية تمر؛ لم يُثبت تقييم جودة إجابات حقيقية وفق مرجع بشري \| تشغيل البروتوكول على الرأس النهائي، حفظ المخرجات، ومراجعة مرجعية لكل حكم \|"` | — |
| [SRC-62CE5126F9-L000061](../OMARAI_REMEDIATION_REGISTER_AR.md#L61) | 61 | `"\| OMR-T-004 \| Grok W6 \| P1 \| اختبار الحمل \| scripts/tests \| **NOT_RUN** \| سيناريو حمل قابل للتكرار وقياس p50/p95 والأخطاء واستخدام الموارد والتزامن \|"` | — |
| [SRC-62CE5126F9-L000062](../OMARAI_REMEDIATION_REGISTER_AR.md#L62) | 62 | ``"\| OMR-T-005 \| تقريرا التدقيق \| P1 للإنتاج \| التخزين والنسخ الاحتياطي والاستعادة الحية \| `OMARAI_DB_PATH`, deploy \| **NOT_RUN على مضيف فعلي** \| إثبات Volume دائم، بقاء البيانات، وإنجاح restore \|"`` | — |
| [SRC-62CE5126F9-L000063](../OMARAI_REMEDIATION_REGISTER_AR.md#L63) | 63 | ``"\| OMR-T-006 \| PR #76 \| P1 \| صحة فحص الفهرس وتطابق رأس الاختبار \| `.github/workflows/tests.yml`, `docs/generate_index.py` \| **FIXED_AND_TESTED على `f2f1bb3`** — PR [#39653079608](https://github.com/mosabosama2030-oss/omarai/actions/runs/39653079608) وpush [#39653072071](https://github.com/mosabosama2030-oss/omarai/actions/runs/39653072071) اجتازا 384 اختبارًا لكل إصدار Python وRuff والحاوية؛ فحص الفهرس نجح بعد إصلاح سباق التوليد على المراجع غير `main` \| رأس PR الحالي يتضمن تحديث تقرير/فهرس مولد فقط؛ يعاد الاختبار لأي تغيير لاحق في الكود/الاختبارات/Workflow \|"`` | — |
| [SRC-62CE5126F9-L000064](../OMARAI_REMEDIATION_REGISTER_AR.md#L64) | 64 | ``"\| OMR-CI-001 \| مراجعة أدوات التحقق \| P1 \| كانت الاختبارات تخسر سباقًا مع workflow الفهرسة في الفروع غير main \| `.github/workflows/tests.yml`, `.github/workflows/update_index.yml`, `docs/generate_index.py` \| **FIXED_AND_TESTED** — تُحدّث فحوص المراجع غير `main` الفهرس داخل checkout المؤقت قبل فحصه؛ يبقى فحص `main` صارمًا من الملفات الملتزمة. PR [#39653079608](https://github.com/mosabosama2030-oss/omarai/actions/runs/39653079608) وpush [#39653072071](https://github.com/mosabosama2030-oss/omarai/actions/runs/39653072071) وworkflow الفهرسة [#39653072074](https://github.com/mosabosama2030-oss/omarai/actions/runs/39653072074) نجحت \| لا تتجاوز stale index على `main`؛ انشر الملفات المولدة آليًا واحتفظ بفحص `main --check` الصارم \|"`` | — |
| [SRC-62CE5126F9-L000065](../OMARAI_REMEDIATION_REGISTER_AR.md#L65) | 65 | ``"\| OMR-T-007 \| Grok / Issue #68 \| P1 \| تقرير مستقل كامل قابل للتحقق \| Issue #68 والتقرير الذي قدمه المدير \| **PARTIAL** — ملخص Grok قدمه Human Director بالمحادثة؛ لم يُثبت وجود artifact كامل في `main` بالمسار المذكور \| إرفاق التقرير الحقيقي/رابطه وSHA الذي راجعه المراجع؛ لا تدّع اكتمال مراجعة مستقلة دون ذلك \|"`` | — |
| [SRC-62CE5126F9-L000066](../OMARAI_REMEDIATION_REGISTER_AR.md#L66) | 66 | `""` | — |
| [SRC-62CE5126F9-L000067](../OMARAI_REMEDIATION_REGISTER_AR.md#L67) | 67 | `"## D. التداخلات والفروع"` | — |
| [SRC-62CE5126F9-L000068](../OMARAI_REMEDIATION_REGISTER_AR.md#L68) | 68 | `""` | — |
| [SRC-62CE5126F9-L000069](../OMARAI_REMEDIATION_REGISTER_AR.md#L69) | 69 | `"\| المعرّف \| التداخل \| السبب \| القرار الآمن والحالة \|"` | — |
| [SRC-62CE5126F9-L000070](../OMARAI_REMEDIATION_REGISTER_AR.md#L70) | 70 | `"\|---\|---\|---\|---\|"` | — |
| [SRC-62CE5126F9-L000071](../OMARAI_REMEDIATION_REGISTER_AR.md#L71) | 71 | `"\| OMR-I-001 \| #63 مع #74 و#76 \| تداخل كبير في التحقق والبحث والواجهة \| تغيرات ملفات مشتركة \| **CLOSED_AS_SUPERSEDED** — #63 و#74 أُغلقا مع تعليق يوجّه إلى #76؛ لم يدمجا \| لا دمج تاريخي؛ تُراجع أي وظيفة فريدة فقط على فرع حديث \|"` | — |
| [SRC-62CE5126F9-L000072](../OMARAI_REMEDIATION_REGISTER_AR.md#L72) | 72 | `"\| OMR-I-002 \| #74 مع #75 \| إصلاحات E3/E4 أصبحت في main وبعض باقي العمل متداخل \| #75 + #76 \| **CLOSED_AS_SUPERSEDED** — #74 أُغلق دون دمج \| لا يُفتح مجددًا إلا لدليل regression محدد \|"` | — |
| [SRC-62CE5126F9-L000073](../OMARAI_REMEDIATION_REGISTER_AR.md#L73) | 73 | `"\| OMR-I-003 \| #72 مع فهرسة main و#76 \| فهرس مولد مكرر وفرع قديم؛ أداة البحث المحلي نُقلت إلى #76 \| index workflow وsearch_code.py \| **CLOSED_AS_SUPERSEDED** — #72 أُغلق دون دمج؛ main لديه مولد/Workflow أحدث وأداة البحث أضيفت إلى #76 \| لا تُدمج ملفات الفهرس اليدوية؛ لا يعاد فتح generator إلا لخلل محدد \|"` | — |
| [SRC-62CE5126F9-L000074](../OMARAI_REMEDIATION_REGISTER_AR.md#L74) | 74 | `"\| OMR-I-004 \| #25 و#26 \| دليل SnapDeploy وGo-Live متداخلان \| وثائق النشر \| **CLOSED_AS_SUPERSEDED** — #25/#26 أُغلقا دون دمج؛ تحديث الدليل موحد في #76 \| لا فرعين قديمين لنفس الدليل \|"` | — |
| [SRC-62CE5126F9-L000075](../OMARAI_REMEDIATION_REGISTER_AR.md#L75) | 75 | `"\| OMR-I-005 \| #12 و#68 \| تكليفات تدقيق متقاربة \| Issues #12/#68 \| **PARTIAL** — #12 أُغلق باعتباره duplicate؛ #68 ما زال مفتوحًا لحفظ شرط التقرير المستقل \| تحديث #68 عند توفر تقرير كامل أو قبول حقيقي \|"` | — |
| [SRC-62CE5126F9-L000076](../OMARAI_REMEDIATION_REGISTER_AR.md#L76) | 76 | ``"\| OMR-I-006 \| مخرجات index مع تغييرات الكود \| ملفات الفهرس المولدة تزيد حجم diff \| `update_index.yml`/generator \| **FIXED_PROCESS** — المولد هو المصدر الوحيد وتنجح فحوصه؛ الرأس النهائي يختلف بملفات مولدة فقط \| تجنب تعديل outputs يدويًا وعدم تجاوز مراجعة PR \|"`` | — |
| [SRC-62CE5126F9-L000077](../OMARAI_REMEDIATION_REGISTER_AR.md#L77) | 77 | `"\| OMR-I-007 \| فروع قديمة مقابل main \| قواعد قديمة ومتباعدة \| PRs 63/72/74/25/26 \| **CLOSED_AS_SUPERSEDED**؛ #76 هو PR الوحيد المفتوح وقت آخر فحص \| أي عمل جديد يبنى من أحدث main \|"` | — |
| [SRC-62CE5126F9-L000078](../OMARAI_REMEDIATION_REGISTER_AR.md#L78) | 78 | `""` | — |
| [SRC-62CE5126F9-L000079](../OMARAI_REMEDIATION_REGISTER_AR.md#L79) | 79 | `"## E. الوثائق والمكونات غير الضرورية"` | — |
| [SRC-62CE5126F9-L000080](../OMARAI_REMEDIATION_REGISTER_AR.md#L80) | 80 | `""` | — |
| [SRC-62CE5126F9-L000081](../OMARAI_REMEDIATION_REGISTER_AR.md#L81) | 81 | `"\| المعرّف \| الأصل \| الحالة \| الإجراء ومعيار الإغلاق \|"` | — |
| [SRC-62CE5126F9-L000082](../OMARAI_REMEDIATION_REGISTER_AR.md#L82) | 82 | `"\|---\|---\|---\|---\|"` | — |
| [SRC-62CE5126F9-L000083](../OMARAI_REMEDIATION_REGISTER_AR.md#L83) | 83 | ``"\| OMR-DOC-001 \| مصفوفة أدلة الاختبار \| لقطة 19 أكتوبر تاريخية \| `docs/OMARAI_TEST_EVIDENCE_MATRIX_AR.md` \| **UPDATED_IN #76** — أضيف ملحق يربط الرأس/نتائج 380 اختبارًا وأوضح NOT_RUN \| تبقى اللقطة تاريخية ويُضاف ملحق جديد عند تغير baseline \|"`` | — |
| [SRC-62CE5126F9-L000084](../OMARAI_REMEDIATION_REGISTER_AR.md#L84) | 84 | `"\| OMR-DOC-002 \| سجل المتطلبات والتسوية التشغيلية \| ادعاءات وlinks إلى SHAs قديمة \| requirements register + operational reconciliation \| **UPDATED_IN #76** — إضافات بتاريخ 21 أكتوبر تربط الأدلة بالـSHA الحالي ومرشح #76 \| تحديث فقط بعد ظهور دليل/نسخة جديدة، لا إعادة تأريخ تاريخي \|"` | — |
| [SRC-62CE5126F9-L000085](../OMARAI_REMEDIATION_REGISTER_AR.md#L85) | 85 | `"\| OMR-DOC-003 \| README ودليل الاستضافة \| وصف وظيفة غير موجودة أو حدود تشغيل غير صريحة \| README، Go-Live، deployment docs، scope \| **UPDATED_IN #76** — search_code، SHA البناء، single-operator، وVolume/hosted smoke موضحة \| لا توثيق لوظيفة غير موجودة؛ الحفاظ على التحذير من NOT_RUN \|"` | — |
| [SRC-62CE5126F9-L000086](../OMARAI_REMEDIATION_REGISTER_AR.md#L86) | 86 | `"\| OMR-DOC-004 \| تقرير Grok داخل artifacts \| الملف الكامل غير قابل للعثور عليه في main بحسب جلب المسار \| artifact path الوارد \| **PARTIAL** — ملخص مقدم من Human Director؛ لا نختلق ملفًا أو ننسبه لـGrok GitHub \| توفير artifact قابل للوصول أو الاستمرار بتتبع الملخص بصفته user-provided \|"` | — |
| [SRC-62CE5126F9-L000087](../OMARAI_REMEDIATION_REGISTER_AR.md#L87) | 87 | ``"\| OMR-S-001 \| البحث المحلي داخل الكود \| P1 \| الأداة كانت موصوفة في README وغير موجودة في main، وكانت الروابط ثابتة على `blob/main` \| `docs/search_code.py`, `tests/test_search_code.py` \| **FIXED_AND_TESTED IN PR #76** — أضيف `--ref` و`OMARAI_GITHUB_REF` واستخراج SHA من البيئة/HEAD المحلي؛ الاختبارات ضمن 384 اختبارًا ناجحًا على كلا إصدارَي Python في [#39653079608](https://github.com/mosabosama2030-oss/omarai/actions/runs/39653079608) \| الوظيفة تدخل main بعد قرار دمج #76 فقط \|"`` | — |
| [SRC-62CE5126F9-L000088](../OMARAI_REMEDIATION_REGISTER_AR.md#L88) | 88 | ``"\| OMR-I-008 \| روابط بحث الفهرس \| P1 \| تثبيت `GITHUB_BLOB_BASE` على `blob/main` يضلل مراجع PR لأن نتيجة البحث قد تكون في commit/فرع غير main \| `docs/search_code.py`, `tests/test_search_code.py` \| **FIXED_AND_TESTED على `f2f1bb3...`** — اختبارات المرجع الصريح وبيئة SHA والـCLI اجتازت CI ضمن 384 اختبارًا على Python 3.11 و3.12 في [#39653079608](https://github.com/mosabosama2030-oss/omarai/actions/runs/39653079608). المقارنة من `f2f1bb3...` إلى رأس `b848f96...` لا تحتوي إلا وثائق وصفحات فهرس مولدة. \| عند تغيير أداة البحث، أعد الاختبارات؛ الروابط الحالية يجب أن تشير إلى المرجع المختار لا `main` دائمًا \|"`` | — |
| [SRC-62CE5126F9-L000089](../OMARAI_REMEDIATION_REGISTER_AR.md#L89) | 89 | `"\| OMR-S-002 \| Skills/Workflows الدائمة أو تعدد الوكلاء \| **PROPOSED / NOT REQUIRED FOR FOUNDATION** \| لا تُنفذ الآن دون حاجة مثبتة؛ حافظ على نواة موثوقة وعقود أدوات وWorkflows قابلة للاختبار قبل توسع الوكلاء \|"` | — |
| [SRC-62CE5126F9-L000090](../OMARAI_REMEDIATION_REGISTER_AR.md#L90) | 90 | `"\| OMR-S-003 \| موصلات بحث اختيارية \| **REVIEW REQUIRED** \| لا تحذف موصلًا بناءً على عدم استعماله في اختبار واحد؛ احتفظ به إن كان خلف إعداد اختياري وله اختبارات وحدود تكلفة واضحة؛ احذف التكرار المثبت فقط \|"` | — |
| [SRC-62CE5126F9-L000091](../OMARAI_REMEDIATION_REGISTER_AR.md#L91) | 91 | `""` | — |
| [SRC-62CE5126F9-L000092](../OMARAI_REMEDIATION_REGISTER_AR.md#L92) | 92 | `"## E1. حالة واجهة الاستخدام المستقلة"` | — |
| [SRC-62CE5126F9-L000093](../OMARAI_REMEDIATION_REGISTER_AR.md#L93) | 93 | `""` | — |
| [SRC-62CE5126F9-L000094](../OMARAI_REMEDIATION_REGISTER_AR.md#L94) | 94 | `"\| المعرّف \| الأصل \| الخطورة \| الحالة الحالية \| معيار الإغلاق \|"` | — |
| [SRC-62CE5126F9-L000095](../OMARAI_REMEDIATION_REGISTER_AR.md#L95) | 95 | `"\|---\|---\|---:\|---\|---\|"` | — |
| [SRC-62CE5126F9-L000096](../OMARAI_REMEDIATION_REGISTER_AR.md#L96) | 96 | `"\| OMR-UI-001 \| Issue #11 — حالات واجهة البحث العربية \| P2 \| **PARTIAL** — #76 يحدّث واجهة الأدلة والحالات، لكن لا يوجد إثبات اختبار متصفح/Android يدوي على الرأس المقترح \| إبقاء #11 مفتوحًا حتى التحقق من حالات التحميل/النجاح/التدهور/الفشل، الروابط، عدم عرض إجابة قديمة، RTL/عرض ضيق، ولوحة المفاتيح/التباين؛ أرفق دليلًا ولا تدّع أتمتة غير موجودة \|"` | — |
| [SRC-62CE5126F9-L000097](../OMARAI_REMEDIATION_REGISTER_AR.md#L97) | 97 | `""` | — |
| [SRC-62CE5126F9-L000098](../OMARAI_REMEDIATION_REGISTER_AR.md#L98) | 98 | `"## F. ملخص بوابات الإغلاق"` | — |
| [SRC-62CE5126F9-L000099](../OMARAI_REMEDIATION_REGISTER_AR.md#L99) | 99 | `""` | — |
| [SRC-62CE5126F9-L000100](../OMARAI_REMEDIATION_REGISTER_AR.md#L100) | 100 | `"### مغلق ومختبر على main"` | — |
| [SRC-62CE5126F9-L000101](../OMARAI_REMEDIATION_REGISTER_AR.md#L101) | 101 | `"- **E3** إزالة عرض تغطية الأدلة كنسبة ثقة."` | — |
| [SRC-62CE5126F9-L000102](../OMARAI_REMEDIATION_REGISTER_AR.md#L102) | 102 | `"- **E4** إصلاح truthiness في مستوى البحث الاحتياطي."` | — |
| [SRC-62CE5126F9-L000103](../OMARAI_REMEDIATION_REGISTER_AR.md#L103) | 103 | ``"كلاهما مرتبط بـ#75 المدمج في `main` عند `d46a546...`."`` | — |
| [SRC-62CE5126F9-L000104](../OMARAI_REMEDIATION_REGISTER_AR.md#L104) | 104 | `""` | — |
| [SRC-62CE5126F9-L000105](../OMARAI_REMEDIATION_REGISTER_AR.md#L105) | 105 | `"### منفذ ومختبر في مرشح #76"` | — |
| [SRC-62CE5126F9-L000106](../OMARAI_REMEDIATION_REGISTER_AR.md#L106) | 106 | `"- توجيه الأسئلة الناقصة إلى CLARIFY وتوحيد متابعة السياق."` | — |
| [SRC-62CE5126F9-L000107](../OMARAI_REMEDIATION_REGISTER_AR.md#L107) | 107 | `"- تشخيصات منظمة لحالات استخراج الصفحات والموصلات، مع حدود واضحة لما تثبته."` | — |
| [SRC-62CE5126F9-L000108](../OMARAI_REMEDIATION_REGISTER_AR.md#L108) | 108 | `"- منع التحويل التلقائي لموفري البحث الذين تغطيهم الاختبارات."` | — |
| [SRC-62CE5126F9-L000109](../OMARAI_REMEDIATION_REGISTER_AR.md#L109) | 109 | ``"- CSP hash ورؤوس الحماية دون `unsafe-inline`."`` | — |
| [SRC-62CE5126F9-L000110](../OMARAI_REMEDIATION_REGISTER_AR.md#L110) | 110 | `"- هوية بناء SHA واختبار مقارنة SHA في hosted smoke (الكود موجود؛ hosted smoke حي NOT_RUN)."` | — |
| [SRC-62CE5126F9-L000111](../OMARAI_REMEDIATION_REGISTER_AR.md#L111) | 111 | `"- مسار SQLite قابل للضبط، أداة البحث المحلي، وتوثيق نطاق التشغيل."` | — |
| [SRC-62CE5126F9-L000112](../OMARAI_REMEDIATION_REGISTER_AR.md#L112) | 112 | ``"- إصلاح سباق الفهرسة في CI على المراجع غير `main` مع إبقاء تحقق `main` صارمًا."`` | — |
| [SRC-62CE5126F9-L000113](../OMARAI_REMEDIATION_REGISTER_AR.md#L113) | 113 | `""` | — |
| [SRC-62CE5126F9-L000114](../OMARAI_REMEDIATION_REGISTER_AR.md#L114) | 114 | ``"**أحدث دليل:** PR [#39653079608](https://github.com/mosabosama2030-oss/omarai/actions/runs/39653079608) وpush [#39653072071](https://github.com/mosabosama2030-oss/omarai/actions/runs/39653072071) نجحا على `f2f1bb3c87c709383e0a8c18691f46cd3661e61b`: 384 اختبارًا ناجحًا على كل من Python 3.11 و3.12، وRuff وفحص الفهرس وبناء الحاوية وAPI المحمي ناجحة. [Workflow الفهرسة #39653072074](https://github.com/mosabosama2030-oss/omarai/actions/runs/39653072074) نجح كذلك. رأس PR الحالي `8198aabc95ce426948d7a233e966c0bbad5e54b7` يضم بعد ذلك تحديثات تقرير/سجل وفهرس مولد فقط؛ لا توجد تغييرات تطبيق/اختبار/Workflow لاحقة."`` | — |
| [SRC-62CE5126F9-L000115](../OMARAI_REMEDIATION_REGISTER_AR.md#L115) | 115 | `""` | — |
| [SRC-62CE5126F9-L000116](../OMARAI_REMEDIATION_REGISTER_AR.md#L116) | 116 | `"### ما يتطلب بيئة فعلية ولا يمكن إغلاقه من الكود وحده"` | — |
| [SRC-62CE5126F9-L000117](../OMARAI_REMEDIATION_REGISTER_AR.md#L117) | 117 | `"- Hosted smoke حقيقي وتوافر الموصلات/النموذج حيًا."` | — |
| [SRC-62CE5126F9-L000118](../OMARAI_REMEDIATION_REGISTER_AR.md#L118) | 118 | `"- تقييم دلالي فعلي لجميع حالات AQ-001–045."` | — |
| [SRC-62CE5126F9-L000119](../OMARAI_REMEDIATION_REGISTER_AR.md#L119) | 119 | `"- ثبات Volume فعلي ونسخ احتياطي/استعادة."` | — |
| [SRC-62CE5126F9-L000120](../OMARAI_REMEDIATION_REGISTER_AR.md#L120) | 120 | `"- red-team حي وXSS/Prompt injection على بيئة حقيقية."` | — |
| [SRC-62CE5126F9-L000121](../OMARAI_REMEDIATION_REGISTER_AR.md#L121) | 121 | `"- اختبار الحمل."` | — |
| [SRC-62CE5126F9-L000122](../OMARAI_REMEDIATION_REGISTER_AR.md#L122) | 122 | `"- عزل المستأجرين؛ غير مدعوم في النطاق أحادي المشغل."` | — |
| [SRC-62CE5126F9-L000123](../OMARAI_REMEDIATION_REGISTER_AR.md#L123) | 123 | `"- تقرير Grok المستقل الكامل القابل للتحقق."` | — |
| [SRC-62CE5126F9-L000124](../OMARAI_REMEDIATION_REGISTER_AR.md#L124) | 124 | `""` | — |
| [SRC-62CE5126F9-L000125](../OMARAI_REMEDIATION_REGISTER_AR.md#L125) | 125 | `"يلزم لكل بند بيئته ودليله الخاص؛ نجاح Pytest أو بناء Docker لا يغلق هذه البنود."` | — |
| [SRC-62CE5126F9-L000126](../OMARAI_REMEDIATION_REGISTER_AR.md#L126) | 126 | `""` | — |
| [SRC-62CE5126F9-L000127](../OMARAI_REMEDIATION_REGISTER_AR.md#L127) | 127 | `"## G. قاعدة عدم الإغلاق الشكلي"` | — |
| [SRC-62CE5126F9-L000128](../OMARAI_REMEDIATION_REGISTER_AR.md#L128) | 128 | `""` | — |
| [SRC-62CE5126F9-L000129](../OMARAI_REMEDIATION_REGISTER_AR.md#L129) | 129 | `"لا يغلق أي بند لمجرد أن ملفًا أو وظيفة أضيفت. يلزم اختبار النجاح والفشل وحدود الإدخال ذات الصلة، وسجل SHA، ورابط تشغيل CI عند انطباقه. #76 هو طلب الدمج الوحيد المقترح؛ لا يدمج تلقائيًا، ويظل قرار الدمج والنشر للمدير البشري."` | — |
| [SRC-62CE5126F9-L000130](../OMARAI_REMEDIATION_REGISTER_AR.md#L130) | 130 | `""` | — |
| [SRC-62CE5126F9-L000131](../OMARAI_REMEDIATION_REGISTER_AR.md#L131) | 131 | `"**الحالة العامة للسجل: CODE/CI FIXES TESTED; HUMAN MERGE REVIEW OPEN; LIVE OPERATIONS GATES NOT_RUN.**"` | — |
## وثائق وفهرسة

### FILE-B9C3015420 — [docs/OMARAI_REQUIREMENTS_REGISTER.md](../OMARAI_REQUIREMENTS_REGISTER.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-B9C3015420-L000001](../OMARAI_REQUIREMENTS_REGISTER.md#L1) | 1 | `"# Omarai — سجل المتطلبات الأساسية الأولي"` | — |
| [SRC-B9C3015420-L000002](../OMARAI_REQUIREMENTS_REGISTER.md#L2) | 2 | `""` | — |
| [SRC-B9C3015420-L000003](../OMARAI_REQUIREMENTS_REGISTER.md#L3) | 3 | `"**المعرّف:** OMARAI-REQ-REGISTER-001  "` | — |
| [SRC-B9C3015420-L000004](../OMARAI_REQUIREMENTS_REGISTER.md#L4) | 4 | `"**الإصدار:** 1.2.0  "` | — |
| [SRC-B9C3015420-L000005](../OMARAI_REQUIREMENTS_REGISTER.md#L5) | 5 | `"**الحالة:** مقترح للاعتماد مع طلب المراجعة PR #42  "` | — |
| [SRC-B9C3015420-L000006](../OMARAI_REQUIREMENTS_REGISTER.md#L6) | 6 | `"**الغرض:** سجل عملي مختصر يربط المتطلبات الأكثر أهمية بالاختبارات والأدلة اللازمة. التفاصيل الكاملة في الدستور الهندسي، وخط الأساس الموسع، ونموذج التتبع والنضج، و[المعمارية الحاكمة للقدرات والمهارات وسير العمل والوكلاء](OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md).  "` | — |
| [SRC-B9C3015420-L000007](../OMARAI_REQUIREMENTS_REGISTER.md#L7) | 7 | ``"**قاعدة الحالة:** هذا السجل يضم تدقيق P0 الأولي على النسخة التاريخية `08319cce3652c332e414f691a71cc153dfbfd92e`. اقرأه مع [تسوية الأدلة التشغيلية](OMARAI_OPERATIONAL_EVIDENCE_RECONCILIATION_2026-10-19_AR.md) المحدثة حتى دمج PR #48، وبقية فروع الاختبار المفتوحة. أي بند لم يُختبر بما يكفي يظل UNKNOWN/INFERRED/PARTIAL وفق نطاق الدليل؛ لا تمثل الوثيقة شهادة امتثال شامل."`` | — |
| [SRC-B9C3015420-L000008](../OMARAI_REQUIREMENTS_REGISTER.md#L8) | 8 | `""` | — |
| [SRC-B9C3015420-L000009](../OMARAI_REQUIREMENTS_REGISTER.md#L9) | 9 | `"## طريقة القراءة"` | — |
| [SRC-B9C3015420-L000010](../OMARAI_REQUIREMENTS_REGISTER.md#L10) | 10 | `""` | — |
| [SRC-B9C3015420-L000011](../OMARAI_REQUIREMENTS_REGISTER.md#L11) | 11 | `"- **P0:** حاجز سلامة/صحة أساسي، يراجع قبل إتاحة المسار المرتبط به."` | — |
| [SRC-B9C3015420-L000012](../OMARAI_REQUIREMENTS_REGISTER.md#L12) | 12 | `"- **P1:** أساس الاختبار والموثوقية والتشخيص."` | — |
| [SRC-B9C3015420-L000013](../OMARAI_REQUIREMENTS_REGISTER.md#L13) | 13 | `"- **P2:** استعداد للنمو وتشغيل أكثر نضجًا عند انطباق الحاجة."` | — |
