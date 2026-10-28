# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **018**
- سجلات الأسطر: **800**
- النطاق: SRC-D17CE3D12F-L000660 إلى SRC-62CE5126F9-L000232
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## وثائق وفهرسة

### FILE-D17CE3D12F — [docs/OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
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

### FILE-B2C95EAEE1 — [docs/OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-B2C95EAEE1-L000001](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L1) | 1 | `"# Omarai — تقرير التحقق الهندسي بعد دمج PR #81"` | — |
| [SRC-B2C95EAEE1-L000002](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L2) | 2 | `""` | — |
| [SRC-B2C95EAEE1-L000003](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L3) | 3 | `"## جلسة 1 — تثبيت خط الأساس بعد الدمج (23 أكتوبر 2026)"` | — |
| [SRC-B2C95EAEE1-L000004](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L4) | 4 | `""` | — |
| [SRC-B2C95EAEE1-L000005](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L5) | 5 | `"### الحالة المرجعية"` | — |
| [SRC-B2C95EAEE1-L000006](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L6) | 6 | `""` | — |
| [SRC-B2C95EAEE1-L000007](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L7) | 7 | ``"- **حالة PR #81:** `MERGED=true`. رابط PR: [#81](https://github.com/mosabosama2030-oss/omarai/pull/81)."`` | — |
| [SRC-B2C95EAEE1-L000008](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L8) | 8 | ``"- **Commit الدمج:** [`9f6674abf8679a0630d95b269b54a7ef8629c3bf`](https://github.com/mosabosama2030-oss/omarai/commit/9f6674abf8679a0630d95b269b54a7ef8629c3bf)."`` | — |
| [SRC-B2C95EAEE1-L000009](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L9) | 9 | ``"- **رأس `main` الذي قارنته GitHub مع المرجع الحالي:** [`00a3ede039922c0c24097e89f653e6d3c984435d`](https://github.com/mosabosama2030-oss/omarai/commit/00a3ede039922c0c24097e89f653e6d3c984435d). المقارنة بين `main` وهذا SHA أعادت `identical` (`ahead_by=0`, `behind_by=0`)."`` | — |
| [SRC-B2C95EAEE1-L000010](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L10) | 10 | ``"- **طبيعة الرأس الحالي:** `00a3ede...` تحديث للفهرس المولد بعد دمج #81؛ ليس تغييرًا في منطق البحث."`` | — |
| [SRC-B2C95EAEE1-L000011](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L11) | 11 | `""` | — |
| [SRC-B2C95EAEE1-L000012](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L12) | 12 | `"### نتائج الاختبار التي أمكن إثباتها"` | — |
| [SRC-B2C95EAEE1-L000013](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L13) | 13 | `""` | — |
| [SRC-B2C95EAEE1-L000014](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L14) | 14 | `"- [تشغيل CI #39955767221](https://github.com/mosabosama2030-oss/omarai/actions/runs/39955767221) على رأس PR #81 السابق للدمج نجح في الوظائف الثلاث."` | — |
| [SRC-B2C95EAEE1-L000015](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L15) | 15 | `"- Python 3.11: **384 passed**؛ Python 3.12: **384 passed**."` | — |
| [SRC-B2C95EAEE1-L000016](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L16) | 16 | `"- Ruff ناجح؛ اختبارات تصنيف ملفات الفهرس ناجحة؛ توليد الفهرس والتحقق منه ناجحان؛ بناء الحاوية واختبار API المحمي ناجحان."` | — |
| [SRC-B2C95EAEE1-L000017](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L17) | 17 | `"- PR #81 يعالج السباق السابق بين اختبار main وناشر الفهرس: عند تغييرات المصدر/الوثائق يعيد الاختبار توليد الفهرس في مساحة معزولة؛ وعند تغييرات مخرجات الفهرس وحدها يبقى الفحص الصارم قائمًا."` | — |
| [SRC-B2C95EAEE1-L000018](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L18) | 18 | `""` | — |
| [SRC-B2C95EAEE1-L000019](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L19) | 19 | `"### حالة التحقق على الرأس النهائي"` | — |
| [SRC-B2C95EAEE1-L000020](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L20) | 20 | `""` | — |
| [SRC-B2C95EAEE1-L000021](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L21) | 21 | ``"- **Push CI مباشر على `00a3ede...`: `NOT_CONFIRMED` في هذه المراجعة.** موصل GitHub المتاح يعيد هنا تشغيلات CI المرتبطة بطلبات الدمج ولا يتيح إثبات تشغيلات push النهائية المطلوبة بصورة مباشرة. لا يعني هذا فشلًا ولا نجاحًا؛ يجب فتح GitHub Actions والتحقق من التشغيل المرتبط بـ`main` وSHA الحالي."`` | — |
| [SRC-B2C95EAEE1-L000022](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L22) | 22 | ``"- فهرس `main` موجود عند SHA `00a3ede...`، لكن نجاح تشغيل CI على رأس PR قبل الدمج ليس بديلًا عن فحص التشغيل بعد الدمج."`` | — |
| [SRC-B2C95EAEE1-L000023](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L23) | 23 | `"- لا يوجد من هذا الفحص إثبات لاتصال موفري البحث والنموذج الحيين، أو جودة الإجابات الدلالية في الاستضافة، أو ثبات قاعدة البيانات والاستعادة على المضيف، أو أداء الحمل، أو قبول Android/RTL."` | — |
| [SRC-B2C95EAEE1-L000024](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L24) | 24 | `""` | — |
| [SRC-B2C95EAEE1-L000025](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L25) | 25 | `"### حكم الجلسة 1"` | — |
| [SRC-B2C95EAEE1-L000026](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L26) | 26 | `""` | — |
| [SRC-B2C95EAEE1-L000027](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L27) | 27 | `"**PARTIAL — اكتمل تحديد الرأس المرجعي، وثبت دمج #81، وثبت نجاح CI قبل الدمج، وصُححت الوثائق على فرع مراجعة.** لا تُغلق الجلسة بالكامل حتى:"` | — |
| [SRC-B2C95EAEE1-L000028](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L28) | 28 | ``"1. التحقق من تشغيل CI ناجح مرتبط بـSHA الحالي `00a3ede...` على `main`؛ أو تشغيل/إعادة تشغيل workflow المعتمد على ذلك الرأس إذا لم يوجد تشغيل صالح."`` | — |
| [SRC-B2C95EAEE1-L000029](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L29) | 29 | `"2. دمج PR توحيد الوثائق الذي يصحح حالات #81 القديمة في النطاق والسجل والتقرير."` | — |
| [SRC-B2C95EAEE1-L000030](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L30) | 30 | `""` | — |
| [SRC-B2C95EAEE1-L000031](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L31) | 31 | `"هذا التقرير لا يعلن جاهزية الإنتاج أو الإطلاق العام. المراحل التالية تبدأ بعد إغلاق الجلسة 1 بالأدلة."` | — |
| [SRC-B2C95EAEE1-L000032](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L32) | 32 | `""` | — |
| [SRC-B2C95EAEE1-L000033](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L33) | 33 | `"---"` | — |
| [SRC-B2C95EAEE1-L000034](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L34) | 34 | `""` | — |
| [SRC-B2C95EAEE1-L000035](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L35) | 35 | `"## سجل تاريخي — التحقق من PR #76 (لا يمثل رأس main الحالي)"` | — |
| [SRC-B2C95EAEE1-L000036](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L36) | 36 | `""` | — |
| [SRC-B2C95EAEE1-L000037](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L37) | 37 | `"**الحالة:** مراجعة بعد الدمج — أدلة جزئية موثقة؛ لا تمثل شهادة جاهزية إنتاجية.  "` | — |
| [SRC-B2C95EAEE1-L000038](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L38) | 38 | `"**PR #76:** [fix(foundation): close audit findings and verify evidence/runtime identity](https://github.com/mosabosama2030-oss/omarai/pull/76) — **MERGED**.  "` | — |
| [SRC-B2C95EAEE1-L000039](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L39) | 39 | `"**وقت الدمج المعلن من GitHub:** 2026-10-21 19:19:54 UTC.  "` | — |
| [SRC-B2C95EAEE1-L000040](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L40) | 40 | ``"**التزام الدمج:** [`528a2552c0cda809d6c444713466e0e075c13ed9`](https://github.com/mosabosama2030-oss/omarai/commit/528a2552c0cda809d6c444713466e0e075c13ed9).  "`` | — |
| [SRC-B2C95EAEE1-L000041](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L41) | 41 | ``"**رأس PR الذي اجتاز CI:** [`3fb02880aec9ec231d973e0b3668308d1379ee89`](https://github.com/mosabosama2030-oss/omarai/commit/3fb02880aec9ec231d973e0b3668308d1379ee89)."`` | — |
| [SRC-B2C95EAEE1-L000042](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L42) | 42 | `""` | — |
| [SRC-B2C95EAEE1-L000043](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L43) | 43 | `"## 1. الحكم التنفيذي"` | — |
| [SRC-B2C95EAEE1-L000044](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L44) | 44 | `""` | — |
| [SRC-B2C95EAEE1-L000045](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L45) | 45 | `"تم دمج الإصلاحات المجمعة في #76. تشغيل CI الأحدث الذي تمكنت من فحص وظائفه هو [run #39654908040](https://github.com/mosabosama2030-oss/omarai/actions/runs/39654908040) على رأس PR، وجميع الوظائف الثلاث فيه **SUCCESS**: الاختبارات على Python 3.11 وPython 3.12 وبناء الحاوية واختبار API المحمي. ظهر في السجل **384 اختبارًا ناجحًا على كل إصدار Python**، ونجح Ruff وفحص الفهرس وبناء الحاوية واختبار API الأساسي."` | — |
| [SRC-B2C95EAEE1-L000046](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L46) | 46 | `""` | — |
| [SRC-B2C95EAEE1-L000047](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L47) | 47 | ``"**حدّ مهم:** هذه نتيجة CI مرتبطة برأس PR قبل الدمج، وليست بحد ذاتها إثباتًا أن workflow مستقلًا اكتمل على التزام الدمج `528a255...`. استعلام حالة الالتزام الذي أتيح لي لم يُرجع عناصر status، وأداة جلب التشغيلات المتاحة هنا تعرض تشغيلات PR فقط. لذلك حالة تحقق CI على التزام `main` بعد الدمج مصنفة **NOT_CONFIRMED**، وليست PASS ولا FAIL. يجب تسجيل رابط تشغيل push/post-merge المرتبط بالـSHA نفسه، إن وجد، أو إجراء تحقق غير مدفوع من `main` وفق آلية المستودع."`` | — |
| [SRC-B2C95EAEE1-L000048](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L48) | 48 | `""` | — |
| [SRC-B2C95EAEE1-L000049](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L49) | 49 | `"نجاح CI لا يثبت تشغيل نسخة منشورة، أو الاتصال الحي بكل مزود، أو صحة كل إجابة، أو دوام قاعدة البيانات، أو أداء الإنتاج."` | — |
| [SRC-B2C95EAEE1-L000050](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L50) | 50 | `""` | — |
| [SRC-B2C95EAEE1-L000051](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L51) | 51 | `"## 2. خط أساس التحقق"` | — |
| [SRC-B2C95EAEE1-L000052](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L52) | 52 | `""` | — |
| [SRC-B2C95EAEE1-L000053](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L53) | 53 | `"\| البند \| الحالة \| الدليل أو الحد \|"` | — |
| [SRC-B2C95EAEE1-L000054](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L54) | 54 | `"\|---\|---\|---\|"` | — |
| [SRC-B2C95EAEE1-L000055](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L55) | 55 | ``"\| دمج PR #76 \| **VERIFIED** \| حالة PR هي closed/merged؛ merge commit هو `528a2552c0cda809d6c444713466e0e075c13ed9`. \|"`` | — |
| [SRC-B2C95EAEE1-L000056](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L56) | 56 | ``"\| رأس PR قبل الدمج \| **VERIFIED** \| `3fb02880aec9ec231d973e0b3668308d1379ee89`. \|"`` | — |
| [SRC-B2C95EAEE1-L000057](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L57) | 57 | ``"\| CI على رأس PR \| **PASS** \| [run #39654908040](https://github.com/mosabosama2030-oss/omarai/actions/runs/39654908040): `test (3.11)`, `test (3.12)`, `container-build` كلها SUCCESS. \|"`` | — |
| [SRC-B2C95EAEE1-L000058](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L58) | 58 | `"\| Pytest على رأس PR \| **PASS** \| 384 passed على Python 3.11 و384 passed على Python 3.12، وفق سجلات المهام. \|"` | — |
| [SRC-B2C95EAEE1-L000059](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L59) | 59 | ``"\| Ruff \| **PASS** \| خطوة `ruff check agents api cli docs tests` ناجحة في كلا مهمتي الاختبار. \|"`` | — |
| [SRC-B2C95EAEE1-L000060](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L60) | 60 | `"\| الفهرس المولّد \| **PASS** \| مزامنة الفهرس في مساحة الاختبار المؤقتة والتحقق منه نجحا في كلا مهمتي الاختبار. \|"` | — |
| [SRC-B2C95EAEE1-L000061](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L61) | 61 | ``"\| بناء الحاوية وAPI smoke \| **PASS** \| بناء الحاوية وبدء الخدمة واختبار الصحة والمسارات المحمية نجحت في وظيفة `container-build`. هذا اختبار CI محلي داخل الحاوية، وليس استضافة حية. \|"`` | — |
| [SRC-B2C95EAEE1-L000062](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L62) | 62 | ``"\| CI على merge SHA في `main` \| **NOT_CONFIRMED** \| لم أحصل على دليل مباشر قابل للفحص لتشغيل push مكتمل على `528a255...`. لا أستنتج الفشل من غياب الدليل. \|"`` | — |
| [SRC-B2C95EAEE1-L000063](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L63) | 63 | `"\| Hosted smoke \| **NOT_RUN** \| لم تُقدَّم هنا قاعدة HTTPS معتمدة وتكوين أسرار آمن؛ الاختبار الحي قد يستهلك موارد مزود النموذج/البحث. \|"` | — |
| [SRC-B2C95EAEE1-L000064](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L64) | 64 | `"\| اختبار واجهة Android/RTL يدوي \| **NOT_RUN** \| لا توجد لقطات أو قائمة قبول منفذة مرفقة. \|"` | — |
| [SRC-B2C95EAEE1-L000065](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L65) | 65 | ``"\| مراجعة Grok مستقلة على SHA الجديد \| **UNKNOWN / PENDING** \| يوجد Issue #68، لكن لم أتحقق من تقرير مستقل جديد يراجع `528a255...`. \|"`` | — |
| [SRC-B2C95EAEE1-L000066](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L66) | 66 | `""` | — |
| [SRC-B2C95EAEE1-L000067](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L67) | 67 | `"## 3. التغييرات التي أصبح وجودها على المسار المدمج مدعومًا بالأدلة"` | — |
| [SRC-B2C95EAEE1-L000068](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L68) | 68 | `""` | — |
| [SRC-B2C95EAEE1-L000069](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L69) | 69 | `"يشمل PR #76، وفق التغيير المدمج وفحوص CI:"` | — |
| [SRC-B2C95EAEE1-L000070](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L70) | 70 | `""` | — |
| [SRC-B2C95EAEE1-L000071](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L71) | 71 | `"- توحيد التعامل مع السؤال الغامض والمتابعات، مع توجيه الأسئلة القصيرة إلى الاستيضاح عند غياب مرجع صالح."` | — |
| [SRC-B2C95EAEE1-L000072](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L72) | 72 | `"- عدم إظهار تغطية المصادر كمقياس رقمي يوحي باحتمال صحة الإجابة؛ إصلاح العمق القياسي/العميق من #75 ظل قائمًا."` | — |
| [SRC-B2C95EAEE1-L000073](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L73) | 73 | `"- فحوص لفظية محافظة لسلامة الأدلة مع التصريح بأن الاستلزام الدلالي والتحقق المستقل من الحقيقة **غير مثبتين**."` | — |
| [SRC-B2C95EAEE1-L000074](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L74) | 74 | `"- تحسين حالات تشخيص جلب الصفحات والموصلات، واختبارات منع التحويل التلقائي لبعض مزودي البحث المغطّين."` | — |
| [SRC-B2C95EAEE1-L000075](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L75) | 75 | ``"- رؤوس أمان للمتصفح وسياسة CSP مع اختبارات تمنع عودة `unsafe-inline` إلى السياسة المختبرة."`` | — |
| [SRC-B2C95EAEE1-L000076](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L76) | 76 | ``"- تضمين هوية البناء في الحاوية وإتاحتها عبر `/api/health`، ودعم `OMARAI_DB_PATH` لاختيار مسار SQLite."`` | — |
| [SRC-B2C95EAEE1-L000077](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L77) | 77 | ``"- أداة بحث محلي في المصدر وروابط مرجعية قابلة للضبط، وإصلاح سباق فحص الفهرس في CI للفروع غير `main`."`` | — |
| [SRC-B2C95EAEE1-L000078](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L78) | 78 | `""` | — |
| [SRC-B2C95EAEE1-L000079](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L79) | 79 | `"هذه أدلة على وجود المسارات البرمجية واجتياز الاختبارات المحددة؛ ليست ضمانًا أمنيًا شاملًا أو شهادة صحة معرفية."` | — |
| [SRC-B2C95EAEE1-L000080](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L80) | 80 | `""` | — |
| [SRC-B2C95EAEE1-L000081](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L81) | 81 | `"## 4. المخاطر والبوابات التي لم تُغلق"` | — |
| [SRC-B2C95EAEE1-L000082](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L82) | 82 | `""` | — |
| [SRC-B2C95EAEE1-L000083](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L83) | 83 | `"\| الأولوية \| المعرف \| المجال \| الحالة الحالية \| معيار الإغلاق المطلوب \|"` | — |
| [SRC-B2C95EAEE1-L000084](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L84) | 84 | `"\|---\|---\|---\|---\|---\|"` | — |
| [SRC-B2C95EAEE1-L000085](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L85) | 85 | ``"\| P0 \| POST-001 \| CI على SHA الدمج \| **NOT_CONFIRMED** \| رابط تشغيل مكتمل على `528a255...` أو تحقق لاحق واضح على SHA أحدث في `main` مع نفس التغييرات. \|"`` | — |
| [SRC-B2C95EAEE1-L000086](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L86) | 86 | ``"\| P1 \| POST-002 \| تحديث توثيق الحالة بعد الدمج \| **OPEN — توثيقي** \| إزالة أي عبارة حالية توحي أن #76 ما زال مفتوحًا أو أن تغييرات الفرع لم تدخل `main`؛ الحفاظ على اللقطات القديمة بوصفها تاريخية. \|"`` | — |
| [SRC-B2C95EAEE1-L000087](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L87) | 87 | `"\| P1 \| POST-003 \| UI Android وRTL \| **NOT_RUN** — [Issue #11](https://github.com/mosabosama2030-oss/omarai/issues/11) \| اختبار يدوي للحالات: تحميل/نجاح/جزئي/فشل/إعادة المحاولة، مصادر حقيقية، RTL وعرض ضيق، ومنع عرض نتيجة قديمة. \|"` | — |
| [SRC-B2C95EAEE1-L000088](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L88) | 88 | ``"\| P1 \| POST-004 \| مراجعة أمنية مستقلة \| **PENDING** — [Issue #68](https://github.com/mosabosama2030-oss/omarai/issues/68) \| تقرير فعلي مرتبط بـ`528a255...` أو SHA أحدث، يحتوي ملفات/أسطر ونتائج إعادة إنتاج واختبارات وحدود ما لم يُختبر. \|"`` | — |
| [SRC-B2C95EAEE1-L000089](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L89) | 89 | `"\| P1 \| POST-005 \| مزودو البحث والنموذج الحيون \| **NOT_RUN / UNKNOWN** \| اختبار مستقل لكل مزود مفعّل في بيئة مخولة، مع تسجيل وقت الاستجابة والفشل والتكلفة المحتملة دون كشف الأسرار. \|"` | — |
| [SRC-B2C95EAEE1-L000090](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L90) | 90 | `"\| P1 \| POST-006 \| دقة AQ-001–AQ-045 دلاليًا \| **PARTIAL / LIVE NOT_RUN** \| تشغيل مجموعة مرجعية على إجابات فعلية، مع مرجع متوقع ومراجعة بشرية. وجود corpus أو اجتياز pytest لا يثبت صحة إجابات النموذج. \|"` | — |
| [SRC-B2C95EAEE1-L000091](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L91) | 91 | ``"\| P1 \| POST-007 \| استمرار SQLite والنسخ الاحتياطي والاستعادة \| **NOT_RUN** \| إثبات بقاء البيانات عبر إعادة التشغيل/النشر على المضيف الحقيقي، ثم نجاح استعادة نسخة احتياطية. `OMARAI_DB_PATH` لا ينشئ Volume ولا Backup بذاته. \|"`` | — |
| [SRC-B2C95EAEE1-L000092](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L92) | 92 | `"\| P1 \| POST-008 \| Prompt injection واختبار أمني حي \| **PARTIAL / NOT_RUN** \| مصفوفة هجمات مسموح بها، إعادة إنتاج، وفحوص سلبية على البيئة المخصصة، دون توصيل بيانات سرية غير لازمة. \|"` | — |
| [SRC-B2C95EAEE1-L000093](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L93) | 93 | `"\| P1 \| POST-009 \| الحمل والتزامن وحدود المعدل الموزعة \| **NOT_RUN** \| قياسات متكررة لزمن الاستجابة والأخطاء والموارد والتزامن؛ الحدود العملية الحالية محلية للعملية ولا تثبت السعة الإنتاجية. \|"` | — |
| [SRC-B2C95EAEE1-L000094](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L94) | 94 | `"\| P0 للتوسع متعدد العملاء \| POST-010 \| الهوية وعزل بيانات المستأجرين \| **BLOCKER للتوسع** \| لا تستخدم Omarai كخدمة عامة متعددة العملاء أو لحفظ سجلات عملاء سرية قبل تنفيذ واختبار الهوية والتفويض والعزل والتخزين الدائم. \|"` | — |
| [SRC-B2C95EAEE1-L000095](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L95) | 95 | `""` | — |
| [SRC-B2C95EAEE1-L000096](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L96) | 96 | `"## 5. الإجراءات التالية — مرتبة حسب الأولوية"` | — |
| [SRC-B2C95EAEE1-L000097](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L97) | 97 | `""` | — |
| [SRC-B2C95EAEE1-L000098](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L98) | 98 | ``"1. **P0 — إثبات CI على `main`:** التأكد من تشغيل workflow على merge commit أو SHA حالي لاحق من `main`. لا حاجة لاختبار مدفوع لهذا البند."`` | — |
| [SRC-B2C95EAEE1-L000099](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L99) | 99 | `"2. **P1 — توحيد السجلات:** تحديث سجل الإغلاق المركزي ومصفوفة الأدلة ونطاق التنفيذ لتُظهر أن #76 مدمج؛ وتحديد أن أي ادعاء أقدم هو لقطة تاريخية."` | — |
| [SRC-B2C95EAEE1-L000100](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L100) | 100 | ``"3. **P1 — مراجعة مستقلة:** طلب مراجعة Grok على SHA الحالي، لا على خط الأساس السابق `d46a546...`. يبقى الإغلاق معتمدًا على وجود التقرير وأدلته لا على مجرد إرسال الطلب."`` | — |
| [SRC-B2C95EAEE1-L000101](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L101) | 101 | `"4. **P1 — قبول الواجهة:** تنفيذ قائمة Issue #11 يدويًا على جهاز/متصفح حقيقي وتسجيل النتائج."` | — |
| [SRC-B2C95EAEE1-L000102](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L102) | 102 | `"5. **P1 — قبول التشغيل الحي:** لا يبدأ hosted smoke أو أي تشخيص يمكن أن يستهلك حصة/أموالًا إلا بعد اعتماد المضيف وإعداد الأسرار الآمن وموافقة بشرية واضحة على التنفيذ."` | — |
| [SRC-B2C95EAEE1-L000103](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L103) | 103 | `""` | — |
| [SRC-B2C95EAEE1-L000104](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L104) | 104 | `"## 6. سياسة الإغلاق"` | — |
| [SRC-B2C95EAEE1-L000105](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L105) | 105 | `""` | — |
| [SRC-B2C95EAEE1-L000106](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L106) | 106 | ``"- `FIXED_AND_TESTED` يعني أن الإصلاح اجتاز اختبارًا محددًا على SHA معين؛ لا يعني أنه صحيح لكل الحالات."`` | — |
| [SRC-B2C95EAEE1-L000107](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L107) | 107 | ``"- `NOT_CONFIRMED` تعني أن الدليل المباشر المطلوب لم يُتحقق منه في هذه المراجعة، ولا تعني أن الفحص فشل."`` | — |
| [SRC-B2C95EAEE1-L000108](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L108) | 108 | ``"- `NOT_RUN` تعني أن الاختبار لم يُنفذ."`` | — |
| [SRC-B2C95EAEE1-L000109](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L109) | 109 | `"- لا يُعلن إغلاق التأسيس أو جاهزية الإنتاج اعتمادًا على نجاح CI وحده."` | — |
| [SRC-B2C95EAEE1-L000110](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L110) | 110 | `""` | — |
| [SRC-B2C95EAEE1-L000111](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L111) | 111 | `"## الروابط المرجعية"` | — |
| [SRC-B2C95EAEE1-L000112](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L112) | 112 | `""` | — |
| [SRC-B2C95EAEE1-L000113](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L113) | 113 | `"- [PR #76](https://github.com/mosabosama2030-oss/omarai/pull/76)"` | — |
| [SRC-B2C95EAEE1-L000114](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L114) | 114 | `"- [CI على رأس PR: run #39654908040](https://github.com/mosabosama2030-oss/omarai/actions/runs/39654908040)"` | — |
| [SRC-B2C95EAEE1-L000115](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L115) | 115 | ``"- [التزام الدمج: `528a255...`](https://github.com/mosabosama2030-oss/omarai/commit/528a2552c0cda809d6c444713466e0e075c13ed9)"`` | — |
| [SRC-B2C95EAEE1-L000116](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L116) | 116 | `"- [Issue #11 — قبول الواجهة](https://github.com/mosabosama2030-oss/omarai/issues/11)"` | — |
| [SRC-B2C95EAEE1-L000117](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L117) | 117 | `"- [Issue #68 — التدقيق المستقل](https://github.com/mosabosama2030-oss/omarai/issues/68)"` | — |
| [SRC-B2C95EAEE1-L000118](../OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md#L118) | 118 | `"- [Issue #73 — خارطة الطريق المقترحة](https://github.com/mosabosama2030-oss/omarai/issues/73)"` | — |
## وثائق وفهرسة

### FILE-62CE5126F9 — [docs/OMARAI_REMEDIATION_REGISTER_AR.md](../OMARAI_REMEDIATION_REGISTER_AR.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-62CE5126F9-L000001](../OMARAI_REMEDIATION_REGISTER_AR.md#L1) | 1 | `"# سجل الإغلاق الهندسي المركزي لمشروع Omarai"` | — |
| [SRC-62CE5126F9-L000002](../OMARAI_REMEDIATION_REGISTER_AR.md#L2) | 2 | `""` | — |
| [SRC-62CE5126F9-L000003](../OMARAI_REMEDIATION_REGISTER_AR.md#L3) | 3 | `"## تحديث تشخيص البحث المعمّق — 27 أكتوبر 2026"` | — |
| [SRC-62CE5126F9-L000004](../OMARAI_REMEDIATION_REGISTER_AR.md#L4) | 4 | `""` | — |
| [SRC-62CE5126F9-L000005](../OMARAI_REMEDIATION_REGISTER_AR.md#L5) | 5 | `"- **OMR-LIVE-006 — CODE/CI FIXED_AND_TESTED; HOSTED_RETEST_PENDING:** أُنشئ PR #104 لتصحيح مطابقة النتائج متعددة اللغات وتشخيص موصل Google News. لم يُدمج ولم يُنشر."` | — |
| [SRC-62CE5126F9-L000006](../OMARAI_REMEDIATION_REGISTER_AR.md#L6) | 6 | ``"- **VERIFIED — مسار الكود:** كانت `_search_news` تطبق `_relevance_ratio` داخليًا ثم لا تعيد إلا ما اجتاز المرشح، بينما يطبق `_search_web` مرشح الصلة المركزي مرة أخرى. إذا رُفضت جميع عناصر RSS داخل الموصل، لا تصل تلك العناصر إلى عدادات الرفض المشتركة ويظهر الموصل وكأنه لم يقدم نتائج قابلة للقراءة."`` | — |
| [SRC-62CE5126F9-L000007](../OMARAI_REMEDIATION_REGISTER_AR.md#L7) | 7 | ``"- **VERIFIED — فحص RSS حي مباشر:** أعاد Google News RSS مع الإعدادات نفسها `hl=ar&gl=EG&ceid=EG:ar` أربع نتائج XML قابلة للقراءة لاستعلام `AI use cases for small businesses`، منها نتيجتا IBM بعنوان عربي عن حالات استخدام الذكاء الاصطناعي. سجل المتصفح: [فحص Google News RSS](https://agent.tinyfish.ai/runs/5559be88-c189-48c7-af78-5c02a6145e6d) و[قراءة موجز Google News بالإنجليزية/أمريكا](https://agent.tinyfish.ai/runs/1eeadc0e-906c-4ecf-96d9-811ef07bcd6e)."`` | — |
| [SRC-62CE5126F9-L000008](../OMARAI_REMEDIATION_REGISTER_AR.md#L8) | 8 | `"- **VERIFIED — Bing RSS:** فحص موجز Bing لعدة صيغ من سؤال الشركات الصغيرة أعاد نتائج عامة أو غير متصلة بالموضوع؛ لذلك لم تُخفّض عتبة الصلة البالغة 0.20 ولم تُمرر مصادر ضعيفة لمجرد إنتاج إجابة. الفحوص: [Bing RSS الأول](https://agent.tinyfish.ai/runs/a02bda48-1141-473f-b914-1245d0dc4edf)، [مقارنة الاستعلامات](https://agent.tinyfish.ai/runs/896d3c16-7601-4f47-81cd-522d8112c70d)، [استعلام العبارة المقتبسة](https://agent.tinyfish.ai/runs/b70d0c5e-e2d3-41e9-842f-1f39da5fa857)."` | — |
| [SRC-62CE5126F9-L000009](../OMARAI_REMEDIATION_REGISTER_AR.md#L9) | 9 | ``"- **PATCH داخل PR #104:** أضيفت مفردات عربية/إنجليزية محدودة لتطابق كلمات `use/use cases/business` مع عناوين عربية مقابلة، وأزيل الترشيح المكرر من موصل Google News كي تصل العناصر الآمنة القابلة للتحليل إلى المرشح المركزي وعدادات القبول/الرفض. لا تغيير في حد الصلة أو فحوص URL/SSRF."`` | — |
| [SRC-62CE5126F9-L000010](../OMARAI_REMEDIATION_REGISTER_AR.md#L10) | 10 | ``"- **FIXED_AND_TESTED — CI على SHA `222ff1096adac89b27e5dce61780743009aa68fd`:** نجح [تشغيل Actions #40479342580](https://github.com/mosabosama2030-oss/omarai/actions/runs/40479342580): `ruff check` ناجح، و**425 اختبارًا ناجحًا على Python 3.12** و**425 اختبارًا ناجحًا على Python 3.11**، ونجح بناء الحاوية وفحص API المحمي."`` | — |
| [SRC-62CE5126F9-L000011](../OMARAI_REMEDIATION_REGISTER_AR.md#L11) | 11 | ``"- **حدّ الدليل:** نجح CI على SHA `222ff1096adac89b27e5dce61780743009aa68fd` الذي احتوى الكود والاختبارات، ثم نجح أيضًا على `f90d205df806465ad94f504f67722205c22f3533` بعد تحديث سجل المعالجة: [#40479569158](https://github.com/mosabosama2030-oss/omarai/actions/runs/40479569158)، مع 425 اختبارًا على Python 3.11 و425 على Python 3.12، وRuff وبناء الحاوية وAPI smoke ناجحة. أضافت عملية الفهرسة بعد ذلك ملفات مولدة فقط؛ تشغيل PR على رأس الفهرسة كان `action_required`، وهي حالة لم تثبت نجاحًا أو فشلًا على ذلك الرأس. لم يُنشر الإصلاح ولم يُختبر المضيف بعده."`` | — |
| [SRC-62CE5126F9-L000012](../OMARAI_REMEDIATION_REGISTER_AR.md#L12) | 12 | ``"- **الإغلاق المتبقي:** مراجعة بشرية وقرار دمج PR #104، ثم نشر بإذن منفصل والتحقق من SHA البناء، وبعدها إعادة اختبار السؤال العربي نفسه في وضع `deep` والتحقق من عدد المصادر المقبولة وروابطها وتشخيص الرفض. حتى ذلك الحين تظل بوابة القبول الحي `PARTIAL`."`` | — |
| [SRC-62CE5126F9-L000013](../OMARAI_REMEDIATION_REGISTER_AR.md#L13) | 13 | `""` | — |
| [SRC-62CE5126F9-L000014](../OMARAI_REMEDIATION_REGISTER_AR.md#L14) | 14 | `"---"` | — |
| [SRC-62CE5126F9-L000015](../OMARAI_REMEDIATION_REGISTER_AR.md#L15) | 15 | `""` | — |
| [SRC-62CE5126F9-L000016](../OMARAI_REMEDIATION_REGISTER_AR.md#L16) | 16 | `"## تحديث قبول الاستضافة — 27 أكتوبر 2026، تشغيل متصفح محفوظ"` | — |
| [SRC-62CE5126F9-L000017](../OMARAI_REMEDIATION_REGISTER_AR.md#L17) | 17 | `""` | — |
| [SRC-62CE5126F9-L000018](../OMARAI_REMEDIATION_REGISTER_AR.md#L18) | 18 | ``"- **OMR-LIVE-004 — PARTIAL / BLOCKED:** أعيد اختبار المضيف عبر جلسة المتصفح [af7ebb42-e032-4321-8454-a3628432f53d](https://agent.tinyfish.ai/runs/af7ebb42-e032-4321-8454-a3628432f53d). حُمّلت الواجهة، لكن حقل `accessToken` كان فارغًا داخل ملف المتصفح الاختباري. فشل سؤال «ما عاصمة مصر؟» قبل تنفيذ البحث برسالة: «رمز الوصول غير صحيح أو غير محفوظ. راجع رمز التطبيق المستضاف»."`` | — |
| [SRC-62CE5126F9-L000019](../OMARAI_REMEDIATION_REGISTER_AR.md#L19) | 19 | `"- **حد الاستنتاج:** يثبت الاختبار عدم وجود الرمز في ملف المتصفح الاختباري فقط؛ لا يثبت أن الرمز في متصفح المستخدم غير صحيح. بيانات التخزين المحلي منفصلة بين الملفات/المتصفحات. لم يُدخل الرمز أو يُكشف ولم تُستخدم خزنة أسرار."` | — |
| [SRC-62CE5126F9-L000020](../OMARAI_REMEDIATION_REGISTER_AR.md#L20) | 20 | `"- **اختبارات لم تُنفذ:** البحث عن الموقع الرسمي لـ OpenAI في وضع «الأحدث الآن» وبحث معمّق إضافي، لأن حاجز المصادقة أوقف الطلبات."` | — |
| [SRC-62CE5126F9-L000021](../OMARAI_REMEDIATION_REGISTER_AR.md#L21) | 21 | ``"- **`GET /api/health`:** أعاد `ok=true` لكن `build.sha=unknown`, `sha_status=unknown`, `sha_source=unknown`، و`live_network_checks_performed=false`. `web_search_ready` و`language_model_configured` لا يثبتان اتصال مزودي البحث أو نجاح إكمال النموذج."`` | — |
| [SRC-62CE5126F9-L000022](../OMARAI_REMEDIATION_REGISTER_AR.md#L22) | 22 | ``"- **OMR-LIVE-005 — CODE/CI FIXED_AND_TESTED; HOST_CONFIGURATION_PENDING:** إصلاح #98 موجود في `main`، لكن المضيف لا يعلن SHA البناء بعد. يجب على مالك الاستضافة ضبط `PUBLIC_OMARAI_BUILD_SHA` على SHA الكامل النهائي المعتمد ثم إعادة البناء/النشر عبر مسار المنصة، والتحقق من التطابق. هذا العمل لم يغير إعدادات المضيف ولم ينشر."`` | — |
| [SRC-62CE5126F9-L000023](../OMARAI_REMEDIATION_REGISTER_AR.md#L23) | 23 | `"- **المتابعة المطلوبة:** أُنشئت جلسة إعداد آمنة لملف المتصفح الاختباري كي يُدخل المستخدم رمز الوصول بنفسه ويحفظه دون إرساله في المحادثة؛ بعد الحفظ يعاد اختبار الأسئلة الثلاثة وتسجيل روابط المصادر الفعلية. لا إعلان قبول نهائي قبل نجاح هذه الخطوات."` | — |
| [SRC-62CE5126F9-L000024](../OMARAI_REMEDIATION_REGISTER_AR.md#L24) | 24 | `"- **تقرير تفصيلي:** [artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md](../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md)؛ مقترح توثيقي في [PR #100](https://github.com/mosabosama2030-oss/omarai/pull/100)."` | — |
| [SRC-62CE5126F9-L000025](../OMARAI_REMEDIATION_REGISTER_AR.md#L25) | 25 | `""` | — |
| [SRC-62CE5126F9-L000026](../OMARAI_REMEDIATION_REGISTER_AR.md#L26) | 26 | `"---"` | — |
| [SRC-62CE5126F9-L000027](../OMARAI_REMEDIATION_REGISTER_AR.md#L27) | 27 | `""` | — |
| [SRC-62CE5126F9-L000028](../OMARAI_REMEDIATION_REGISTER_AR.md#L28) | 28 | `"## تحديث تنفيذي — 27 أكتوبر 2026: إصلاح مسار هوية البناء على SnapDeploy"` | — |
| [SRC-62CE5126F9-L000029](../OMARAI_REMEDIATION_REGISTER_AR.md#L29) | 29 | `""` | — |
| [SRC-62CE5126F9-L000030](../OMARAI_REMEDIATION_REGISTER_AR.md#L30) | 30 | ``"- **OMR-LIVE-005 — FIXED_AND_TESTED (الكود وCI) / HOST_CONFIGURATION_PENDING:** تأكد السبب الجذري من توثيق SnapDeploy: المتغيرات غير العامة متاحة وقت التشغيل فقط، ولا تمررها المنصة إلى بناء Docker كوسائط بناء. كانت الصورة تكتب `unknown` لأن Dockerfile كان يعتمد على `OMARAI_BUILD_SHA` وحده."`` | — |
| [SRC-62CE5126F9-L000031](../OMARAI_REMEDIATION_REGISTER_AR.md#L31) | 31 | ``"- **PR #98 — MERGED:** دمج الإصلاح في `main` عند `d9a8f83796547591d651c41ff657475bcec9b0ab`. أضاف Dockerfile دعم `PUBLIC_OMARAI_BUILD_SHA` (بيانات إصدار علنية غير سرية) مع التحقق من SHA كامل، مع الإبقاء على وسيط البناء التقليدي؛ وتم تحديث CI لاختبار المسار نفسه."`` | — |
| [SRC-62CE5126F9-L000032](../OMARAI_REMEDIATION_REGISTER_AR.md#L32) | 32 | ``"- **الاختبار الآلي:** نجح PR CI على SHA `9b97dfe9d7a996349c374134fb2ae1ebcfdcf5fa` في [#40471611641](https://github.com/mosabosama2030-oss/omarai/actions/runs/40471611641)، ونجح CI بعد الدمج على SHA `d9a8f83796547591d651c41ff657475bcec9b0ab` في [#40471732289](https://github.com/mosabosama2030-oss/omarai/actions/runs/40471732289)، كما نجح توليد الفهرس [#40471732508](https://github.com/mosabosama2030-oss/omarai/actions/runs/40471732508). تشمل الفحوص Python 3.11 و3.12 وRuff وبناء الحاوية وAPI smoke المحمي."`` | — |
| [SRC-62CE5126F9-L000033](../OMARAI_REMEDIATION_REGISTER_AR.md#L33) | 33 | ``"- **ما لم يُغلق:** فحص `/api/health` بعد الدمج ما زال يعيد `build.sha=unknown`؛ هذا متوقع ما لم يُضبط متغير البناء العام في الخدمة ثم تعاد عملية البناء. يلزم تحديد SHA النهائي بعد آخر تغييرات على `main`، وتعيين `PUBLIC_OMARAI_BUILD_SHA` إلى تلك القيمة في SnapDeploy ثم التأكد من أن `build.sha` يطابقها بالضبط. لا تضع أي رمز أو مفتاح API في هذا المتغير."`` | — |
| [SRC-62CE5126F9-L000034](../OMARAI_REMEDIATION_REGISTER_AR.md#L34) | 34 | ``"- **قبول البحث الحي:** ما زال `PARTIAL / BLOCKED` لأن جلسة المتصفح الاختبارية لا تتشارك التخزين المحلي مع متصفح المستخدم؛ يجب حفظ رمز الوصول داخل ملف المتصفح الاختباري من خلال صفحة الإعداد بنفسه، دون إرساله في المحادثة. لم ينجح أي طلب بحث حي في هذه الجلسة بعد."`` | — |
| [SRC-62CE5126F9-L000035](../OMARAI_REMEDIATION_REGISTER_AR.md#L35) | 35 | `"- **مراجع المنصة:** [SnapDeploy deployment guide](https://snapdeploy.dev/docs/deployment) و[environment variables](https://snapdeploy.dev/docs/environment-variables). لا يثبت نجاح CI اتصال موفري البحث أو صحة الإجابات الحية."` | — |
| [SRC-62CE5126F9-L000036](../OMARAI_REMEDIATION_REGISTER_AR.md#L36) | 36 | `""` | — |
| [SRC-62CE5126F9-L000037](../OMARAI_REMEDIATION_REGISTER_AR.md#L37) | 37 | `"## تحديث تنفيذي — 27 أكتوبر 2026، بعد دمج PR #95 وإعادة فحص الاستضافة"` | — |
| [SRC-62CE5126F9-L000038](../OMARAI_REMEDIATION_REGISTER_AR.md#L38) | 38 | `""` | — |
| [SRC-62CE5126F9-L000039](../OMARAI_REMEDIATION_REGISTER_AR.md#L39) | 39 | `"### الحالة المثبتة بعد الإغلاق"` | — |
| [SRC-62CE5126F9-L000040](../OMARAI_REMEDIATION_REGISTER_AR.md#L40) | 40 | ``"- **PR #95 — MERGED:** التزام الدمج `3760418b5f32294faec7e49ef2cccb006419ee27`. نجح CI على رأس PR في [#40467019476](https://github.com/mosabosama2030-oss/omarai/actions/runs/40467019476)، وعلى SHA الدمج نفسه في [#40469019954](https://github.com/mosabosama2030-oss/omarai/actions/runs/40469019954). اكتملت اختبارات Python 3.11/3.12 وبناء الحاوية وAPI smoke بنجاح."`` | — |
| [SRC-62CE5126F9-L000041](../OMARAI_REMEDIATION_REGISTER_AR.md#L41) | 41 | `"- **توليد الفهرس:** نجح [#40469019921](https://github.com/mosabosama2030-oss/omarai/actions/runs/40469019921)."` | — |
| [SRC-62CE5126F9-L000042](../OMARAI_REMEDIATION_REGISTER_AR.md#L42) | 42 | ``"- **PR #93 — CLOSED WITHOUT MERGE:** تم التحقق من أن التصحيح التوثيقي موجود في سجل المعالجة على `main` بعد دمج #95؛ لم يُدمج الفرع القديم لتجنب تكرار التغيير."`` | — |
| [SRC-62CE5126F9-L000043](../OMARAI_REMEDIATION_REGISTER_AR.md#L43) | 43 | `"- نتائج CI لا تثبت صحة التشغيل المستضاف أو نجاح مزودي البحث الحقيقيين."` | — |
| [SRC-62CE5126F9-L000044](../OMARAI_REMEDIATION_REGISTER_AR.md#L44) | 44 | `""` | — |
| [SRC-62CE5126F9-L000045](../OMARAI_REMEDIATION_REGISTER_AR.md#L45) | 45 | `"### نتيجة القبول الحي المحدود"` | — |
| [SRC-62CE5126F9-L000046](../OMARAI_REMEDIATION_REGISTER_AR.md#L46) | 46 | `"- **VERIFIED:** بعد إخراج الخدمة من الخمول، حمّلت الصفحة الرئيسية واجهة Omarai وحقل السؤال."` | — |
| [SRC-62CE5126F9-L000047](../OMARAI_REMEDIATION_REGISTER_AR.md#L47) | 47 | ``"- **FAILED — hosted query:** كان الوضع المختار `deep`; السؤال `ما عاصمة مصر؟` انتهى برسالة التطبيق: «رمز الوصول غير صحيح أو غير محفوظ. راجع رمز التطبيق المستضاف»."`` | — |
| [SRC-62CE5126F9-L000048](../OMARAI_REMEDIATION_REGISTER_AR.md#L48) | 48 | ``"- **UNKNOWN:** هل رمز الوصول مفقود أم غير مطابق، وما السبب الجذري الدقيق؛ الرسالة المرئية وحدها لا تكفي. أُجري `GET /api/health` للقراءة فقط وأعاد `ok=true`، لكن `build.sha=unknown` و`sha_status=unknown`، و`live_network_checks_performed=false`. يوضح الرد أن `web_search_ready` يعني أن الاعتماديات قابلة للاستيراد لا أن موفّر البحث متصل، وأن `language_model_configured` يعني وجود بيانات اعتماد لا أن الطلب اكتمل بنجاح. لم يُثبت تطابق البناء المستضاف مع SHA الدمج."`` | — |
| [SRC-62CE5126F9-L000049](../OMARAI_REMEDIATION_REGISTER_AR.md#L49) | 49 | `"- **لم يحدث:** لا إدخال/كشف لأسرار، ولا تغيير لإعدادات الاستضافة، ولا نشر، ولا طلب ثانٍ إلى موفر بحث/نموذج."` | — |
| [SRC-62CE5126F9-L000050](../OMARAI_REMEDIATION_REGISTER_AR.md#L50) | 50 | `""` | — |
| [SRC-62CE5126F9-L000051](../OMARAI_REMEDIATION_REGISTER_AR.md#L51) | 51 | `"### إجراء الإغلاق التالي"` | — |
| [SRC-62CE5126F9-L000052](../OMARAI_REMEDIATION_REGISTER_AR.md#L52) | 52 | ``"يلزم من مالك الاستضافة مراجعة رمز التطبيق وسجلات الخدمة داخل لوحة SnapDeploy، من دون مشاركة قيمة الرمز في المحادثة. أي تعديل إعدادات أو نشر يتطلب موافقة منفصلة. بعد ذلك، يعاد اختبار القبول المحدود وتوثق هوية `build.sha` قبل إعلان الجاهزية."`` | — |
| [SRC-62CE5126F9-L000053](../OMARAI_REMEDIATION_REGISTER_AR.md#L53) | 53 | `""` | — |
| [SRC-62CE5126F9-L000054](../OMARAI_REMEDIATION_REGISTER_AR.md#L54) | 54 | `"---"` | — |
| [SRC-62CE5126F9-L000055](../OMARAI_REMEDIATION_REGISTER_AR.md#L55) | 55 | `""` | — |
| [SRC-62CE5126F9-L000056](../OMARAI_REMEDIATION_REGISTER_AR.md#L56) | 56 | `"## تحديث تنفيذي — 26 أكتوبر 2026، بعد دمج PR #92 والتحقق من CI"` | — |
| [SRC-62CE5126F9-L000057](../OMARAI_REMEDIATION_REGISTER_AR.md#L57) | 57 | `""` | — |
| [SRC-62CE5126F9-L000058](../OMARAI_REMEDIATION_REGISTER_AR.md#L58) | 58 | `"### خط الأساس والحالة المثبتة"` | — |
| [SRC-62CE5126F9-L000059](../OMARAI_REMEDIATION_REGISTER_AR.md#L59) | 59 | `"- PR [#91 — تقليص استعلامات البحث العربية](https://github.com/mosabosama2030-oss/omarai/pull/91) **MERGED**."` | — |
| [SRC-62CE5126F9-L000060](../OMARAI_REMEDIATION_REGISTER_AR.md#L60) | 60 | ``"- PR [#92 — منع إعادة إدخال السؤال الخام في مسارات auto والأدلة](https://github.com/mosabosama2030-oss/omarai/pull/92) **MERGED** في 26 أكتوبر 2026 الساعة 20:25:10 UTC. التزام الدمج: `f5605a5072548e2de076a0527a4bcb0cc98381b4`. رأس PR: `c31bb16264368b717b0200f95f6d1a032d9b9134`."`` | — |
| [SRC-62CE5126F9-L000061](../OMARAI_REMEDIATION_REGISTER_AR.md#L61) | 61 | `"- بعد الدمج، نجح تشغيل CI على التزام الدمج: [#40395465598](https://github.com/mosabosama2030-oss/omarai/actions/runs/40395465598). كما نجح تشغيل [#40384693139](https://github.com/mosabosama2030-oss/omarai/actions/runs/40384693139) على رأس PR قبل الدمج؛ شمل نجاح Python 3.11 و3.12 وRuff وفحوص الفهرس وبناء الحاوية واختبار API المحمي. لا نخلط بين CI وsmoke البحث الحي على موفّرات خارجية."` | — |
| [SRC-62CE5126F9-L000062](../OMARAI_REMEDIATION_REGISTER_AR.md#L62) | 62 | `"- سجل المعالجة هذا كان يحتوي حالة قديمة تقول إن #92 مفتوح؛ هذا التحديث يصححها. قد تتولد تحديثات الفهرسة في التزامات docs لاحقة، ولا تُعد اختبارًا جديدًا للكود ما لم تتغير ملفات التطبيق أو الاختبارات."` | — |
| [SRC-62CE5126F9-L000063](../OMARAI_REMEDIATION_REGISTER_AR.md#L63) | 63 | `""` | — |
| [SRC-62CE5126F9-L000064](../OMARAI_REMEDIATION_REGISTER_AR.md#L64) | 64 | `"### نتائج المعالجة"` | — |
| [SRC-62CE5126F9-L000065](../OMARAI_REMEDIATION_REGISTER_AR.md#L65) | 65 | ``"- **D1 — FIXED_AND_TESTED:** أزيل الرجوع إلى `[question]` الخام في مسار auto؛ استعلامات fallback والنموذج تُضغط وتُصفّى، ولا تُنشأ استعلامات عامة عند غياب الموضوع. الروابط المباشرة الآمنة تبقى في `direct_urls` منفصلة."`` | — |
| [SRC-62CE5126F9-L000066](../OMARAI_REMEDIATION_REGISTER_AR.md#L66) | 66 | ``"- **D2 — FIXED_AND_TESTED:** تقييم `server_search_sources` يستخدم السؤال المضغوط والاستعلامات المخططة ذات الموضوع، ويمنع قبول مصدر عند غياب مرشح موضوعي."`` | — |
| [SRC-62CE5126F9-L000067](../OMARAI_REMEDIATION_REGISTER_AR.md#L67) | 67 | ``"- **D3 — FIXED_AND_TESTED:** مطابقة إصلاح الأدلة وفلترة المصادر تستخدم استعلامات مضغوطة غير فارغة فقط؛ لا تعود إلى السؤال الخام، وبيانات `search_query` لا تدّعي استعلامًا لم ينفذ."`` | — |
| [SRC-62CE5126F9-L000068](../OMARAI_REMEDIATION_REGISTER_AR.md#L68) | 68 | ``"- **R1 — FIXED_AND_TESTED:** التمريرة النهائية قبل `_collect_research` تتحقق من `compact_search_query` ومن `_relevance_query_tokens`. الاختبار `test_relevance_query_tokens_reject_site_only_and_modifier_only_queries` يغطي عامل `site:` وحده وكلمات توسعة عامة بلا موضوع."`` | — |
| [SRC-62CE5126F9-L000069](../OMARAI_REMEDIATION_REGISTER_AR.md#L69) | 69 | ``"- لم تُخفض عتبة الصلة 0.20، ولم تُضعف فحوص `_public_http_url` أو `_blocked_source_url` أو ضوابط SSRF."`` | — |
| [SRC-62CE5126F9-L000070](../OMARAI_REMEDIATION_REGISTER_AR.md#L70) | 70 | `""` | — |
| [SRC-62CE5126F9-L000071](../OMARAI_REMEDIATION_REGISTER_AR.md#L71) | 71 | `"### حدود الدليل والبوابات المفتوحة"` | — |
| [SRC-62CE5126F9-L000072](../OMARAI_REMEDIATION_REGISTER_AR.md#L72) | 72 | ``"- **CI — FIXED_AND_TESTED:** التشغيل بعد الدمج [#40395465598](https://github.com/mosabosama2030-oss/omarai/actions/runs/40395465598) ناجح على التزام الدمج `f5605a5072548e2de076a0527a4bcb0cc98381b4`. تفاصيل وظائف Python 3.11 و3.12 وcontainer-build نجحت في تشغيل PR [#40384693139](https://github.com/mosabosama2030-oss/omarai/actions/runs/40384693139)."`` | — |
| [SRC-62CE5126F9-L000073](../OMARAI_REMEDIATION_REGISTER_AR.md#L73) | 73 | `"- **Hosted live smoke للأسئلة الأربعة التمثيلية على موفّرات البحث الحقيقية: NOT_RUN.** نجاح API smoke داخل الحاوية لا يثبت توافر موفّرات البحث الخارجية أو جودة الإجابات الحية."` | — |
| [SRC-62CE5126F9-L000074](../OMARAI_REMEDIATION_REGISTER_AR.md#L74) | 74 | `"- **توافر موفّرات البحث الحية وجودة النتائج وحداثة الأخبار: PARTIAL / UNKNOWN** إلى أن يسجل اختبار حيّ معتمد نتائج فعلية."` | — |
| [SRC-62CE5126F9-L000075](../OMARAI_REMEDIATION_REGISTER_AR.md#L75) | 75 | `"- **لا نشر أو تغيير إعدادات المضيف أو أسرار أو إنفاق** ضمن هذا العمل. أي اختبار حي يتطلب تحديد المضيف المعتمد وموافقة المدير البشري."` | — |
| [SRC-62CE5126F9-L000076](../OMARAI_REMEDIATION_REGISTER_AR.md#L76) | 76 | `""` | — |
| [SRC-62CE5126F9-L000077](../OMARAI_REMEDIATION_REGISTER_AR.md#L77) | 77 | `"---"` | — |
| [SRC-62CE5126F9-L000078](../OMARAI_REMEDIATION_REGISTER_AR.md#L78) | 78 | `""` | — |
| [SRC-62CE5126F9-L000079](../OMARAI_REMEDIATION_REGISTER_AR.md#L79) | 79 | `""` | — |
| [SRC-62CE5126F9-L000080](../OMARAI_REMEDIATION_REGISTER_AR.md#L80) | 80 | `"## الحالة المرجعية بعد الجلسة 1 — 23 أكتوبر 2026"` | — |
| [SRC-62CE5126F9-L000081](../OMARAI_REMEDIATION_REGISTER_AR.md#L81) | 81 | `""` | — |
| [SRC-62CE5126F9-L000082](../OMARAI_REMEDIATION_REGISTER_AR.md#L82) | 82 | ``"- رأس `main` الذي تم التحقق من مطابقته: `00a3ede039922c0c24097e89f653e6d3c984435d`؛ والالتزام `9f6674abf8679a0630d95b269b54a7ef8629c3bf` هو دمج PR #81."`` | — |
| [SRC-62CE5126F9-L000083](../OMARAI_REMEDIATION_REGISTER_AR.md#L83) | 83 | `"- PR #81 **MERGED**، وأصلح سباق الفهرسة في CI؛ لا تغييرات في منطق البحث أو الموصلات."` | — |
| [SRC-62CE5126F9-L000084](../OMARAI_REMEDIATION_REGISTER_AR.md#L84) | 84 | `"- [CI #39955767221](https://github.com/mosabosama2030-oss/omarai/actions/runs/39955767221) على رأس PR قبل الدمج نجح: 384 اختبارًا على Python 3.11 و384 على Python 3.12، مع نجاح Ruff وتصنيف مسارات الفهرسة وتوليدها وفحصها وبناء الحاوية وAPI smoke."` | — |
| [SRC-62CE5126F9-L000085](../OMARAI_REMEDIATION_REGISTER_AR.md#L85) | 85 | ``"- **CI على رأس `main` النهائي: NOT_CONFIRMED** ضمن بيانات التشغيل التي أمكن الوصول إليها هنا؛ لا يجوز تحويل ذلك إلى FAIL أو PASS. يلزم التحقق المباشر من GitHub Actions على `00a3ede...`."`` | — |
| [SRC-62CE5126F9-L000086](../OMARAI_REMEDIATION_REGISTER_AR.md#L86) | 86 | `"- تبقى استضافة البحث الحي، جودة الإجابات الدلالية، الاختبارات الأمنية المستقلة، دوام البيانات والاستعادة، والحمل أمورًا غير مثبتة حتى تنفيذ اختبارات بيئاتها."` | — |
| [SRC-62CE5126F9-L000087](../OMARAI_REMEDIATION_REGISTER_AR.md#L87) | 87 | `""` | — |
| [SRC-62CE5126F9-L000088](../OMARAI_REMEDIATION_REGISTER_AR.md#L88) | 88 | `""` | — |
| [SRC-62CE5126F9-L000089](../OMARAI_REMEDIATION_REGISTER_AR.md#L89) | 89 | `"> **تدقيق إضافي — 23 أكتوبر 2026:** أُعيد فحص تشغيل [CI #39654908040](https://github.com/mosabosama2030-oss/omarai/actions/runs/39654908040)، وجميع وظائفه الثلاث ناجحة مع 384 اختبارًا لكل من Python 3.11 و3.12، ونجاح Ruff والفهرس وبناء Docker وAPI smoke."` | — |
| [SRC-62CE5126F9-L000090](../OMARAI_REMEDIATION_REGISTER_AR.md#L90) | 90 | `">"` | — |
| [SRC-62CE5126F9-L000091](../OMARAI_REMEDIATION_REGISTER_AR.md#L91) | 91 | ``"> مقارنة GitHub بين رأس PR المختبَر `3fb02880aec9ec231d973e0b3668308d1379ee89` وcommit الدمج `528a2552c0cda809d6c444713466e0e075c13ed9` أعادت `ahead_by=1` و`behind_by=0` بلا أي ملف مختلف؛ شجرة الملفات مطابقة. هذا يدعم أن نتائج CI تغطي محتوى الكود المدمج، لكنه لا ينشئ تشغيلًا مستقلًا مرتبطًا بحدث push على SHA الدمج. لذلك تبقى حالة تشغيل CI مستقل على SHA الدمج `NOT_CONFIRMED`، لا `FAIL`."`` | — |
| [SRC-62CE5126F9-L000092](../OMARAI_REMEDIATION_REGISTER_AR.md#L92) | 92 | `">"` | — |
| [SRC-62CE5126F9-L000093](../OMARAI_REMEDIATION_REGISTER_AR.md#L93) | 93 | ``"> لا يزال `NOT_CONFIRMED` يعني أنه لم يُثبت تشغيل منفصل على حدث `push` مرتبط مباشرة بـSHA الدمج؛ ولا يعني فشل الاختبارات. أما الشجرة البرمجية نفسها فقد ثبت تطابقها مع الرأس الذي اجتاز CI."`` | — |
| [SRC-62CE5126F9-L000094](../OMARAI_REMEDIATION_REGISTER_AR.md#L94) | 94 | `""` | — |
| [SRC-62CE5126F9-L000095](../OMARAI_REMEDIATION_REGISTER_AR.md#L95) | 95 | `""` | — |
| [SRC-62CE5126F9-L000096](../OMARAI_REMEDIATION_REGISTER_AR.md#L96) | 96 | ``"> **ملحق ما بعد الدمج — 21 أكتوبر 2026:** دُمج PR #76 في `main` عبر الالتزام `528a2552c0cda809d6c444713466e0e075c13ed9`. أحدث دليل CI متاح على رأس PR قبل الدمج هو [run #39654908040](https://github.com/mosabosama2030-oss/omarai/actions/runs/39654908040): 384 اختبارًا ناجحًا على Python 3.11 و384 على Python 3.12، وRuff وفحص الفهرس وبناء الحاوية وAPI smoke ناجحة. تحقق CI على SHA الدمج نفسه **NOT_CONFIRMED** في هذه المراجعة؛ التفاصيل والقيود في [تقرير التحقق بعد الدمج](OMARAI_POST_MERGE_VERIFICATION_2026-10-21_AR.md). المعلومات القديمة أدناه تصف لقطات عند إعدادها ولا تتقدم على هذا الملحق."`` | — |
| [SRC-62CE5126F9-L000097](../OMARAI_REMEDIATION_REGISTER_AR.md#L97) | 97 | `""` | — |
| [SRC-62CE5126F9-L000098](../OMARAI_REMEDIATION_REGISTER_AR.md#L98) | 98 | `""` | — |
| [SRC-62CE5126F9-L000099](../OMARAI_REMEDIATION_REGISTER_AR.md#L99) | 99 | `"## الحالة المرجعية بعد PR #81 — 23 أكتوبر 2026"` | — |
| [SRC-62CE5126F9-L000100](../OMARAI_REMEDIATION_REGISTER_AR.md#L100) | 100 | `""` | — |
| [SRC-62CE5126F9-L000101](../OMARAI_REMEDIATION_REGISTER_AR.md#L101) | 101 | ``"- **رأس `main`:** `00a3ede039922c0c24097e89f653e6d3c984435d`, وهو تحديث فهرسة مولّد بعد دمج PR #81 بالالتزام `9f6674abf8679a0630d95b269b54a7ef8629c3bf`."`` | — |
| [SRC-62CE5126F9-L000102](../OMARAI_REMEDIATION_REGISTER_AR.md#L102) | 102 | ``"- **منطق التطبيق:** لا يغير #81 منطق البحث أو موصلاته؛ تغييره في `.github/workflows/tests.yml` والوثائق."`` | — |
| [SRC-62CE5126F9-L000103](../OMARAI_REMEDIATION_REGISTER_AR.md#L103) | 103 | `"- **حادث OMR-CI-002:** [run #39949934192](https://github.com/mosabosama2030-oss/omarai/actions/runs/39949934192) وثّق فشل فحص الفهرس بعد #79؛ عولج السبب في #81."` | — |
| [SRC-62CE5126F9-L000104](../OMARAI_REMEDIATION_REGISTER_AR.md#L104) | 104 | `"- **دليل الإصلاح قبل الدمج:** [run #39955767221](https://github.com/mosabosama2030-oss/omarai/actions/runs/39955767221) نجح على رأس PR #81: 384 اختبارًا على Python 3.11 و384 على Python 3.12، وRuff والفهرسة والحاوية/API smoke."` | — |
| [SRC-62CE5126F9-L000105](../OMARAI_REMEDIATION_REGISTER_AR.md#L105) | 105 | ``"- **تشغيل CI مباشر على رأس main النهائي:** `NOT_CONFIRMED` في هذه المراجعة. لا يعد ذلك فشلًا؛ يلزم التحقق من GitHub Actions للحدث/الالتزام النهائي."`` | — |
| [SRC-62CE5126F9-L000106](../OMARAI_REMEDIATION_REGISTER_AR.md#L106) | 106 | ``"- **بوابات التشغيل المفتوحة:** موفرو البحث/النموذج الأحياء، جودة الإجابات الدلالية، دوام SQLite والنسخ/الاستعادة على مضيف، اختبار الحمل، قبول Android/RTL، والتقرير الأمني المستقل؛ تبقى `NOT_RUN/UNKNOWN` حتى وجود الدليل المباشر."`` | — |
| [SRC-62CE5126F9-L000107](../OMARAI_REMEDIATION_REGISTER_AR.md#L107) | 107 | `"- **حوكمة PRs:** الحالة الزمنية لطلبات الدمج تؤخذ من GitHub؛ #81 مدمج، والفروع القديمة المغلقة لا تُدمج من جديد."` | — |
| [SRC-62CE5126F9-L000108](../OMARAI_REMEDIATION_REGISTER_AR.md#L108) | 108 | `""` | — |
| [SRC-62CE5126F9-L000109](../OMARAI_REMEDIATION_REGISTER_AR.md#L109) | 109 | `""` | — |
| [SRC-62CE5126F9-L000110](../OMARAI_REMEDIATION_REGISTER_AR.md#L110) | 110 | `"**المعرّف:** OMARAI-REMEDIATION-REGISTER-001  "` | — |
| [SRC-62CE5126F9-L000111](../OMARAI_REMEDIATION_REGISTER_AR.md#L111) | 111 | `"**بيانات اللقطة الأصلية:** 21 أكتوبر 2026، قبل دمج PR #76.  "` | — |
| [SRC-62CE5126F9-L000112](../OMARAI_REMEDIATION_REGISTER_AR.md#L112) | 112 | ``"**خط أساس `main` في اللقطة الأصلية:** `d46a546aba97a9ca32a32c92f1cd6d8a9db2cc81`.  "`` | — |
| [SRC-62CE5126F9-L000113](../OMARAI_REMEDIATION_REGISTER_AR.md#L113) | 113 | ``"**فرع الإصلاح الأصلي:** `fix/audit-closure-current-main-2026-10-21`؛ لا يصف هذا السطر الفرع الحالي.  "`` | — |
| [SRC-62CE5126F9-L000114](../OMARAI_REMEDIATION_REGISTER_AR.md#L114) | 114 | ``"**آخر التزام كامل اجتاز CI:** `463f4a472728b7561f48988bc489b564ad22e1d7`؛ [run #39654530305](https://github.com/mosabosama2030-oss/omarai/actions/runs/39654530305). **رأس PR عند إعداد هذه اللقطة:** `faba1502d08da6cb6c64ba6ef05e9cb29e20ab1c`؛ المقارنة من الالتزام المختبَر إلى الرأس الحالي تُظهر commit فهرسة مولّدًا فقط. لا توجد تغييرات لاحقة في التطبيق أو الاختبارات أو Workflow. يُراجع رأس PR الحي قبل القرار."`` | — |
| [SRC-62CE5126F9-L000115](../OMARAI_REMEDIATION_REGISTER_AR.md#L115) | 115 | `""` | — |
| [SRC-62CE5126F9-L000116](../OMARAI_REMEDIATION_REGISTER_AR.md#L116) | 116 | `"## دليل الاختبارات وحالة رأس PR — لقطة تاريخية قبل الدمج"` | — |
| [SRC-62CE5126F9-L000117](../OMARAI_REMEDIATION_REGISTER_AR.md#L117) | 117 | `""` | — |
| [SRC-62CE5126F9-L000118](../OMARAI_REMEDIATION_REGISTER_AR.md#L118) | 118 | ``"- **تشغيل PR الأخضر المفحوص وقتها (قبل الدمج):** [#39654908040](https://github.com/mosabosama2030-oss/omarai/actions/runs/39654908040) على رأس PR `3fb02880aec9ec231d973e0b3668308d1379ee89`: **384 اختبارًا ناجحًا على Python 3.11 و384 على Python 3.12**، وRuff، ومزامنة/فحص الفهرس، وبناء الحاوية واختبار API المحمي ناجحة. هذا التشغيل يسبق الدمج؛ لا يثبت وحده وجود تشغيل push منفصل على `528a255...`."`` | — |
| [SRC-62CE5126F9-L000119](../OMARAI_REMEDIATION_REGISTER_AR.md#L119) | 119 | ``"- تحقق تشغيل الحاوية في الوظيفة نفسها من أن `GET /api/health` يعلن SHA البناء المخبوز المطابق لـ`GITHUB_SHA`، وأن المسارات المحمية ترفض الطلبات بلا رمز."`` | — |
| [SRC-62CE5126F9-L000120](../OMARAI_REMEDIATION_REGISTER_AR.md#L120) | 120 | ``"- **إصلاح سباق الفهرسة:** `tests.yml` يعيد توليد مخرجات الفهرس داخل مساحة الاختبار المؤقتة للمراجع غير `main` ثم يتحقق من الاتساق؛ يبقى تحقق `main` صارمًا على الملفات الملتزمة. CI اختبر ذلك بنجاح."`` | — |
| [SRC-62CE5126F9-L000121](../OMARAI_REMEDIATION_REGISTER_AR.md#L121) | 121 | ``"- **حدّ الدليل التاريخي:** رأس PR عند كتابة اللقطة الأصلية كان `faba1502d08da6cb6c64ba6ef05e9cb29e20ab1c`؛ ثم وصل الرأس إلى `3fb02880aec9ec231d973e0b3668308d1379ee89` واجتاز run #39654908040، وبعدها دُمج عبر `528a255...`. لا تُعمّم نتيجة CI على الاستضافة الحية أو على كل إجابة معرفية؛ وضع CI بعد الدمج موضح في الملحق أعلاه."`` | — |
| [SRC-62CE5126F9-L000122](../OMARAI_REMEDIATION_REGISTER_AR.md#L122) | 122 | `"- التشغيل المستضاف الحقيقي، وعمل الموصلات الحية، والدوام/النسخ الاحتياطي والاستعادة، والحمل، والاختبار الأحمر المستقل تبقى خارج نطاق دليل CI."` | — |
| [SRC-62CE5126F9-L000123](../OMARAI_REMEDIATION_REGISTER_AR.md#L123) | 123 | `""` | — |
| [SRC-62CE5126F9-L000124](../OMARAI_REMEDIATION_REGISTER_AR.md#L124) | 124 | `"## معاني الحالات"` | — |
| [SRC-62CE5126F9-L000125](../OMARAI_REMEDIATION_REGISTER_AR.md#L125) | 125 | `""` | — |
| [SRC-62CE5126F9-L000126](../OMARAI_REMEDIATION_REGISTER_AR.md#L126) | 126 | `"- **FIXED_AND_TESTED:** الإصلاح موجود في الالتزام المذكور ونجحت اختبارات مرتبطة به على الالتزام نفسه."` | — |
| [SRC-62CE5126F9-L000127](../OMARAI_REMEDIATION_REGISTER_AR.md#L127) | 127 | `"- **PARTIAL:** يوجد تنفيذ أو اختبار أو تحديث جزئي، لكن شرط الإغلاق لم يكتمل."` | — |
| [SRC-62CE5126F9-L000128](../OMARAI_REMEDIATION_REGISTER_AR.md#L128) | 128 | `"- **NOT_RUN:** الاختبار المطلوب لم يُنفذ."` | — |
| [SRC-62CE5126F9-L000129](../OMARAI_REMEDIATION_REGISTER_AR.md#L129) | 129 | `"- **UNKNOWN:** لا توجد أدلة كافية للحكم."` | — |
| [SRC-62CE5126F9-L000130](../OMARAI_REMEDIATION_REGISTER_AR.md#L130) | 130 | `"- **PROPOSED:** فكرة أو تحسين لم يُنفذ."` | — |
| [SRC-62CE5126F9-L000131](../OMARAI_REMEDIATION_REGISTER_AR.md#L131) | 131 | `"- **NOT_REQUIRED:** ثبت عدم الحاجة إلى الوظيفة في النطاق الحالي مع توثيق السبب."` | — |
| [SRC-62CE5126F9-L000132](../OMARAI_REMEDIATION_REGISTER_AR.md#L132) | 132 | `""` | — |
| [SRC-62CE5126F9-L000133](../OMARAI_REMEDIATION_REGISTER_AR.md#L133) | 133 | `"## A. سجل الأخطاء والجذور"` | — |
| [SRC-62CE5126F9-L000134](../OMARAI_REMEDIATION_REGISTER_AR.md#L134) | 134 | `""` | — |
| [SRC-62CE5126F9-L000135](../OMARAI_REMEDIATION_REGISTER_AR.md#L135) | 135 | `"\| المعرّف \| الأصل \| الخطورة \| السبب الجذري \| موضع العمل \| الحالة الحالية والدليل \| معيار الإغلاق \|"` | — |
| [SRC-62CE5126F9-L000136](../OMARAI_REMEDIATION_REGISTER_AR.md#L136) | 136 | `"\|---\|---\|---:\|---\|---\|---\|---\|"` | — |
| [SRC-62CE5126F9-L000137](../OMARAI_REMEDIATION_REGISTER_AR.md#L137) | 137 | ``"\| OMR-E-001 \| Grok E1؛ تدقيق النواة \| P1 \| الأسئلة المرجعية القصيرة كانت تفتقر لقواعد غموض موحدة \| `agents/intent_router.py`, `agents/web_agent.py`, `tests/test_intent_router.py` \| **FIXED_AND_TESTED على رأس #76 `f2f1bb3...`** — اختبارات حالات غامضة وبدون/مع سياق ضمن 384 اختبارًا ناجحًا في كلا إصدارَي Python \| يبقى السؤال المنفرد بلا مرجع CLARIFY؛ ومع السياق الصحيح يوجه للبحث؛ ولا يُسترجع موضوع قديم بعد الشكر \|"`` | — |
| [SRC-62CE5126F9-L000138](../OMARAI_REMEDIATION_REGISTER_AR.md#L138) | 138 | ``"\| OMR-E-002 \| Grok E2 \| P1 \| منطق المتابعة كان موزعًا وقد يسترجع موضوعًا سابقًا غير صالح \| `agents/intent_router.py`, `agents/research.py`, `agents/web_agent.py` واختباراتها \| **FIXED_AND_TESTED على رأس #76 `f2f1bb3...`** — حل متابعة موحد وحدود طول/سياق واختبارات \| سعر/ضمان/مقارنة مع سياق؛ وCLARIFY عند غياب المرجع؛ ورفض السياق القديم \|"`` | — |
| [SRC-62CE5126F9-L000139](../OMARAI_REMEDIATION_REGISTER_AR.md#L139) | 139 | ``"\| OMR-E-003 \| Grok E3 \| P1 \| عرض تغطية الأدلة كدرجة رقمية يمكن فهمها خطأً كاحتمال صحة \| `web/agent.html`, `agents/web_agent.py` \| **FIXED_AND_TESTED ON MAIN** — #75 مدمج في `main` \| بقاء الوصف نوعيًا وعدم عودة مؤشر /100 \|"`` | — |
| [SRC-62CE5126F9-L000140](../OMARAI_REMEDIATION_REGISTER_AR.md#L140) | 140 | ``"\| OMR-E-004 \| Grok E4 \| P1 \| استخدام نص `deep/standard` كقيمة منطقية يجعل كلاهما truthy \| `agents/research.py`, `tests/test_research.py` \| **FIXED_AND_TESTED ON MAIN** — #75 مدمج واختبارات المستوى القياسي والعميق \| لا يستدعي السؤال القياسي زاوية عميقة بلا داعٍ \|"`` | — |
| [SRC-62CE5126F9-L000141](../OMARAI_REMEDIATION_REGISTER_AR.md#L141) | 141 | ``"\| OMR-E-005 \| Grok E5 \| P1 \| إعداد الحاوية وحده لا يربط الخدمة المنشورة بالالتزام الفعلي \| `Dockerfile`, `api/omarai.py`, `scripts/hosted_smoke_test.py`, workflow \| **CODE PATH TESTED; HOSTED NOT_RUN** — SHA مخبوز في صورة Docker ومقارن في hosted smoke؛ لا توجد خدمة فعلية اختُبرت \| نجاح hosted smoke على خدمة معتمدة ومطابقة SHA الفعلي \|"`` | — |
| [SRC-62CE5126F9-L000142](../OMARAI_REMEDIATION_REGISTER_AR.md#L142) | 142 | ``"\| OMR-E-006 \| تقرير التدقيق الموحد \| P1 \| تطابق لفظي أو رابط لا يثبت أن المصدر يستلزم الادعاء دلاليًا \| `agents/answer_validation.py`, `agents/web_agent.py`, tests \| **PARTIAL / CODE TESTED** — إشارة لفظية أكثر تحفظًا واختبارات regression؛ يصرح النظام أن entailment لم يُفحص \| تقييم دلالي مستقل للحالات المرجعية؛ لا يُعرض الفحص اللفظي كتحقق حقيقة \|"`` | — |
| [SRC-62CE5126F9-L000143](../OMARAI_REMEDIATION_REGISTER_AR.md#L143) | 143 | ``"\| OMR-E-007 \| تقرير التدقيق الموحد \| P1 \| العدادات قد تخلط النتائج ومحاولات الجلب والنص المستخرج والفشل \| `agents/web_agent.py`, `tests/test_connector_summary_counters.py` \| **FIXED_AND_TESTED على رأس #76 `f2f1bb3...`** — حالات الجلب وتشخيصات الموصلات تختبرها CI \| حالات العدادات والفشل الجزئي ممثلة في اختبارات؛ نجاح الموفر الحي يظل اختبارًا منفصلًا \|"`` | — |
| [SRC-62CE5126F9-L000144](../OMARAI_REMEDIATION_REGISTER_AR.md#L144) | 144 | ``"\| OMR-E-008 \| تقرير التدقيق الموحد \| P1 \| موفرو البحث قد يتبعون تحويلات غير آمنة \| `agents/web_agent.py`, `tests/test_web_agent.py` \| **FIXED_AND_TESTED على رأس #76 `f2f1bb3...`** — تعطيل auto-redirect لموفري DuckDuckGo/Bing/Google News واختبارات redirect \| رفض الوجهات غير العامة في كل hop؛ لا يُعمم هذا على موفر لم تختبره الاختبارات \|"`` | — |
| [SRC-62CE5126F9-L000145](../OMARAI_REMEDIATION_REGISTER_AR.md#L145) | 145 | `""` | — |
| [SRC-62CE5126F9-L000146](../OMARAI_REMEDIATION_REGISTER_AR.md#L146) | 146 | `"## B. العيوب الأمنية والتشغيلية"` | — |
| [SRC-62CE5126F9-L000147](../OMARAI_REMEDIATION_REGISTER_AR.md#L147) | 147 | `""` | — |
| [SRC-62CE5126F9-L000148](../OMARAI_REMEDIATION_REGISTER_AR.md#L148) | 148 | `"\| المعرّف \| الأصل \| الخطورة \| السبب/الأثر \| الحالة \| معيار الإغلاق \|"` | — |
| [SRC-62CE5126F9-L000149](../OMARAI_REMEDIATION_REGISTER_AR.md#L149) | 149 | `"\|---\|---\|---:\|---\|---\|---\|"` | — |
| [SRC-62CE5126F9-L000150](../OMARAI_REMEDIATION_REGISTER_AR.md#L150) | 150 | ``"\| OMR-D-001 \| Grok D1 \| P1 \| رؤوس الحماية للمتصفح لم تكن موحدة على الاستجابات \| `api/omarai.py`, `tests/test_api.py` \| **FIXED_AND_TESTED على رأس #76 `f2f1bb3...`** — CSP وX-Frame-Options وReferrer-Policy وPermissions-Policy وnosniff واختبارات على HTML/JSON \| استمرار الاختبارات وعدم تراجع أي رأس \|"`` | — |
| [SRC-62CE5126F9-L000151](../OMARAI_REMEDIATION_REGISTER_AR.md#L151) | 151 | ``"\| OMR-D-002 \| مراجعة CSP \| P1 \| `unsafe-inline` يضعف سياسة CSP \| `api/omarai.py`, `tests/test_api.py`, `web/*.html` \| **FIXED_AND_TESTED على رأس #76 `f2f1bb3...`** — hashes لمحتوى inline موثوق، مع `unsafe-hashes` لما يلزم، واختبار يرفض `unsafe-inline` \| لا تسمح السياسة بـunsafe-inline؛ كل تغيير HTML/JS/CSS يمر باختبار CSP \|"`` | — |
| [SRC-62CE5126F9-L000152](../OMARAI_REMEDIATION_REGISTER_AR.md#L152) | 152 | ``"\| OMR-D-003 \| Grok D2 \| P1 \| كشف الأسئلة الناقصة لم يكن موحدًا \| `agents/intent_router.py`, `tests/test_intent_router.py` \| **FIXED_AND_TESTED على رأس #76 `f2f1bb3...`** — مربوط بـE1 \| مصدر واحد لقواعد الغموض واختبارات regression \|"`` | — |
| [SRC-62CE5126F9-L000153](../OMARAI_REMEDIATION_REGISTER_AR.md#L153) | 153 | ``"\| OMR-D-004 \| Grok D3 \| P1 \| قد يخلط المستهلك بين الإشارات اللفظية والتحقق الدلالي \| `agents/answer_validation.py`, `agents/web_agent.py`, UI, tests \| **FIXED_AND_TESTED لحدود العرض في #76** — prompts وواجهة النتائج لا تقدمان الإشارة اللفظية كشهادة حقيقة؛ التقييم الدلالي الكامل لا يزال NOT_RUN \| لا تعرض «تحقق مستقل» دون اختبار مرجعي/مراجع مناسب \|"`` | — |
| [SRC-62CE5126F9-L000154](../OMARAI_REMEDIATION_REGISTER_AR.md#L154) | 154 | `"\| OMR-D-005 \| Grok D4 \| P1 \| توثيق النشر أحادي المشغل لم يوضح حدود الهوية بما يكفي \| README ودلائل النشر وقائمة Go-Live ونطاق التنفيذ \| **DOCUMENTED_IN #76** — النص يصرح بأن الرمز المشترك ليس هوية مستخدمين \| اتساق الوثائق وأن لا يُعلن تعدد المستأجرين \|"` | — |
| [SRC-62CE5126F9-L000155](../OMARAI_REMEDIATION_REGISTER_AR.md#L155) | 155 | `"\| OMR-D-006 \| Grok D5 \| P0 للإطلاق العام متعدد المستخدمين \| لا توجد هوية وتفويض وعزلة مثبتة لكل مستأجر \| نطاق التشغيل الحالي \| **NOT_REQUIRED للنطاق أحادي المشغل؛ BLOCKER لأي خدمة متعددة المستأجرين** \| لا تُدخل عدة عملاء/بيانات سرية قبل هوية وعزل واختباراتهما \|"` | — |
| [SRC-62CE5126F9-L000156](../OMARAI_REMEDIATION_REGISTER_AR.md#L156) | 156 | ``"\| OMR-D-007 \| تقرير التدقيق الموحد \| P1 \| مسار SQLite القابل للتعيين لا ينشئ Volume دائمًا ولا نسخة احتياطية \| `agents/omarai.py`, tests, deploy docs \| **CODE PATH TESTED; DURABILITY NOT_RUN** — `OMARAI_DB_PATH` يحدد المسار واختبار الملف ينجح؛ لم تختبر استضافة فعلية \| بقاء البيانات بعد restart/redeploy واختبار restore من نسخة احتياطية على مضيف مختار \|"`` | — |
| [SRC-62CE5126F9-L000157](../OMARAI_REMEDIATION_REGISTER_AR.md#L157) | 157 | `"\| OMR-D-008 \| تقرير التدقيق الموحد \| P1 للتوسع العام \| حدود المعدل والتزامن في الذاكرة تخص العملية الواحدة \| API/RequestBudget/وثائق النطاق \| **KNOWN LIMITATION / DOCUMENTED** — مناسب فقط للنطاق أحادي المشغل؛ لا يوجد إثبات rate-limit موزع \| قبل نشر متعدد النسخ، طبّق حدًا موزعًا واختبره؛ لا تدّع السعة دون قياس \|"` | — |
| [SRC-62CE5126F9-L000158](../OMARAI_REMEDIATION_REGISTER_AR.md#L158) | 158 | `"\| OMR-D-009 \| تقرير التدقيق الموحد \| P1 \| أخطاء مزود خارجي أو سياق إلى نموذج قد يكشف تفاصيل حساسة إن لم تُنقّح \| تشخيصات الموصلات، redaction، tests \| **PARTIAL / CODE TESTED** — تنقيح وتشخيصات per-request ضمن #76؛ يلزم استمرار تغطية جميع مسارات الأخطاء \| اختبارات تمنع ظهور API keys/Bearer tokens والبيانات السرية في الردود والسجلات \|"` | — |
| [SRC-62CE5126F9-L000159](../OMARAI_REMEDIATION_REGISTER_AR.md#L159) | 159 | ``"\| OMR-D-010 \| Grok W4 \| P1 \| تعليمات صفحات الويب غير الموثوقة قد تُعامل كتعليمات تنفيذ \| prompts، `tests/test_web_agent.py` \| **FIXED_AND_TESTED للحدود الحتمية في #76؛ RED-TEAM حي NOT_RUN** — يوجد اختبار يبقي النص الخبيث خارج system prompt \| اجتياز حالات حقن تعليمات محددة؛ مراجعة red-team أوسع تتطلب بيئة/موافقة \|"`` | — |
| [SRC-62CE5126F9-L000160](../OMARAI_REMEDIATION_REGISTER_AR.md#L160) | 160 | `""` | — |
| [SRC-62CE5126F9-L000161](../OMARAI_REMEDIATION_REGISTER_AR.md#L161) | 161 | `"## C. فجوات الاختبار والجودة"` | — |
| [SRC-62CE5126F9-L000162](../OMARAI_REMEDIATION_REGISTER_AR.md#L162) | 162 | `""` | — |
| [SRC-62CE5126F9-L000163](../OMARAI_REMEDIATION_REGISTER_AR.md#L163) | 163 | `"\| المعرّف \| الأصل \| الخطورة \| الحالة \| ما يلزم للإغلاق \|"` | — |
| [SRC-62CE5126F9-L000164](../OMARAI_REMEDIATION_REGISTER_AR.md#L164) | 164 | `"\|---\|---\|---:\|---\|---\|"` | — |
| [SRC-62CE5126F9-L000165](../OMARAI_REMEDIATION_REGISTER_AR.md#L165) | 165 | ``"\| OMR-T-001 \| تقريرا التدقيق \| P0 للإنتاج \| hosted smoke حي \| `scripts/hosted_smoke_test.py`, workflow \| **NOT_RUN** — لا توجد خدمة فعلية وأسرار اختبار معتمدة \| خدمة HTTPS يملكها المدير، أسرار آمنة، وتطابق SHA واجتياز البحث والنموذج والمصادقة \|"`` | — |
| [SRC-62CE5126F9-L000166](../OMARAI_REMEDIATION_REGISTER_AR.md#L166) | 166 | `"\| OMR-T-002 \| تقريرا التدقيق \| P1 \| مزودو البحث والنماذج الحية \| diagnostics/hosted smoke \| **NOT_RUN** لكل موفر على بيئة مستضافة؛ CI لا يثبت الإتاحة الخارجية \| اختبار كل موفر مفعّل على حدة بميزانية/وقت موثقين \|"` | — |
| [SRC-62CE5126F9-L000167](../OMARAI_REMEDIATION_REGISTER_AR.md#L167) | 167 | `"\| OMR-T-003 \| تقريرا التدقيق \| P1 \| تشغيل AQ-001–045 وتقييم الإجابات دلاليًا \| benchmark runner/fixtures/tests \| **PARTIAL / LIVE QUALITY NOT_RUN** — بنية الحالات موجودة والاختبارات الآلية تمر؛ لم يُثبت تقييم جودة إجابات حقيقية وفق مرجع بشري \| تشغيل البروتوكول على الرأس النهائي، حفظ المخرجات، ومراجعة مرجعية لكل حكم \|"` | — |
| [SRC-62CE5126F9-L000168](../OMARAI_REMEDIATION_REGISTER_AR.md#L168) | 168 | `"\| OMR-T-004 \| Grok W6 \| P1 \| اختبار الحمل \| scripts/tests \| **NOT_RUN** \| سيناريو حمل قابل للتكرار وقياس p50/p95 والأخطاء واستخدام الموارد والتزامن \|"` | — |
| [SRC-62CE5126F9-L000169](../OMARAI_REMEDIATION_REGISTER_AR.md#L169) | 169 | ``"\| OMR-T-005 \| تقريرا التدقيق \| P1 للإنتاج \| التخزين والنسخ الاحتياطي والاستعادة الحية \| `OMARAI_DB_PATH`, deploy \| **NOT_RUN على مضيف فعلي** \| إثبات Volume دائم، بقاء البيانات، وإنجاح restore \|"`` | — |
| [SRC-62CE5126F9-L000170](../OMARAI_REMEDIATION_REGISTER_AR.md#L170) | 170 | ``"\| OMR-T-006 \| PR #76 \| P1 \| صحة فحص الفهرس وتطابق رأس الاختبار \| `.github/workflows/tests.yml`, `docs/generate_index.py` \| **FIXED_AND_TESTED على `463f4a4...`** — PR [#39654530305](https://github.com/mosabosama2030-oss/omarai/actions/runs/39654530305) اجتاز 384 اختبارًا لكل إصدار Python وRuff وفحص الفهرس والحاوية/API smoke؛ فحص المراجع غير `main` يولد في مساحة الاختبار قبل تحقق الاتساق \| رأس PR الحالي يتضمن تحديث تقرير/فهرس مولد فقط؛ يعاد الاختبار لأي تغيير لاحق في الكود/الاختبارات/Workflow \|"`` | — |
| [SRC-62CE5126F9-L000171](../OMARAI_REMEDIATION_REGISTER_AR.md#L171) | 171 | ``"\| OMR-CI-001 \| مراجعة أدوات التحقق \| P1 \| كانت الاختبارات تخسر سباقًا مع workflow الفهرسة في الفروع غير main \| `.github/workflows/tests.yml`, `.github/workflows/update_index.yml`, `docs/generate_index.py` \| **FIXED_AND_TESTED** — تُحدّث فحوص المراجع غير `main` الفهرس داخل checkout المؤقت قبل فحصه؛ يبقى فحص `main` صارمًا من الملفات الملتزمة. PR [#39654530305](https://github.com/mosabosama2030-oss/omarai/actions/runs/39654530305) اجتاز 384 اختبارًا بكل من Python 3.11/3.12، وRuff والفهرس والحاوية/API smoke \| لا تتجاوز stale index على `main`؛ انشر الملفات المولدة آليًا واحتفظ بفحص `main --check` الصارم \|"`` | — |
| [SRC-62CE5126F9-L000172](../OMARAI_REMEDIATION_REGISTER_AR.md#L172) | 172 | ``"\| OMR-CI-002 \| سباق ما بعد دمج تغييرات الوثائق مع تحديث الفهرس \| P1 — جودة بوابة CI \| بعد دمج #79 فشل `generate_index.py --check` لأن الفهرس لم يكن محدثًا عند بدء الاختبار. \| `.github/workflows/tests.yml`, `.github/workflows/update_index.yml` \| **FIXED_AND_TESTED على رأس PR #81 قبل الدمج** عبر [run #39955767221](https://github.com/mosabosama2030-oss/omarai/actions/runs/39955767221): 384 اختبارًا على Python 3.11 و3.12 لكل منهما، وRuff والفهرس والحاوية/API smoke. PR #81 مدمج في `9f6674a...`. **CI مباشر على رأس main النهائي: NOT_CONFIRMED** في هذه المراجعة، وليس FAIL. \| التحقق من تشغيل push CI على الرأس النهائي `00a3ede...`؛ الإبقاء على تصنيف المسارات واختبار الفهرس الصارم للتغييرات المولدة وحدها. \|"`` | — |
| [SRC-62CE5126F9-L000173](../OMARAI_REMEDIATION_REGISTER_AR.md#L173) | 173 | ``"\| OMR-T-007 \| Grok / Issue #68 \| P1 \| تقرير مستقل كامل قابل للتحقق \| Issue #68 والتقرير الذي قدمه المدير \| **PARTIAL** — ملخص Grok قدمه Human Director بالمحادثة؛ لم يُثبت وجود artifact كامل في `main` بالمسار المذكور \| إرفاق التقرير الحقيقي/رابطه وSHA الذي راجعه المراجع؛ لا تدّع اكتمال مراجعة مستقلة دون ذلك \|"`` | — |
| [SRC-62CE5126F9-L000174](../OMARAI_REMEDIATION_REGISTER_AR.md#L174) | 174 | `""` | — |
| [SRC-62CE5126F9-L000175](../OMARAI_REMEDIATION_REGISTER_AR.md#L175) | 175 | `"## D. التداخلات والفروع"` | — |
| [SRC-62CE5126F9-L000176](../OMARAI_REMEDIATION_REGISTER_AR.md#L176) | 176 | `""` | — |
| [SRC-62CE5126F9-L000177](../OMARAI_REMEDIATION_REGISTER_AR.md#L177) | 177 | `"\| المعرّف \| التداخل \| السبب \| القرار الآمن والحالة \|"` | — |
| [SRC-62CE5126F9-L000178](../OMARAI_REMEDIATION_REGISTER_AR.md#L178) | 178 | `"\|---\|---\|---\|---\|"` | — |
| [SRC-62CE5126F9-L000179](../OMARAI_REMEDIATION_REGISTER_AR.md#L179) | 179 | `"\| OMR-I-001 \| #63 مع #74 و#76 \| تداخل كبير في التحقق والبحث والواجهة \| تغيرات ملفات مشتركة \| **CLOSED_AS_SUPERSEDED** — #63 و#74 أُغلقا مع تعليق يوجّه إلى #76؛ لم يدمجا \| لا دمج تاريخي؛ تُراجع أي وظيفة فريدة فقط على فرع حديث \|"` | — |
| [SRC-62CE5126F9-L000180](../OMARAI_REMEDIATION_REGISTER_AR.md#L180) | 180 | `"\| OMR-I-002 \| #74 مع #75 \| إصلاحات E3/E4 أصبحت في main وبعض باقي العمل متداخل \| #75 + #76 \| **CLOSED_AS_SUPERSEDED** — #74 أُغلق دون دمج \| لا يُفتح مجددًا إلا لدليل regression محدد \|"` | — |
| [SRC-62CE5126F9-L000181](../OMARAI_REMEDIATION_REGISTER_AR.md#L181) | 181 | `"\| OMR-I-003 \| #72 مع فهرسة main و#76 \| فهرس مولد مكرر وفرع قديم؛ أداة البحث المحلي نُقلت إلى #76 \| index workflow وsearch_code.py \| **CLOSED_AS_SUPERSEDED** — #72 أُغلق دون دمج؛ main لديه مولد/Workflow أحدث وأداة البحث أضيفت إلى #76 \| لا تُدمج ملفات الفهرس اليدوية؛ لا يعاد فتح generator إلا لخلل محدد \|"` | — |
| [SRC-62CE5126F9-L000182](../OMARAI_REMEDIATION_REGISTER_AR.md#L182) | 182 | `"\| OMR-I-004 \| #25 و#26 \| دليل SnapDeploy وGo-Live متداخلان \| وثائق النشر \| **CLOSED_AS_SUPERSEDED** — #25/#26 أُغلقا دون دمج؛ تحديث الدليل موحد في #76 \| لا فرعين قديمين لنفس الدليل \|"` | — |
| [SRC-62CE5126F9-L000183](../OMARAI_REMEDIATION_REGISTER_AR.md#L183) | 183 | `"\| OMR-I-005 \| #12 و#68 \| تكليفات تدقيق متقاربة \| Issues #12/#68 \| **PARTIAL** — #12 أُغلق باعتباره duplicate؛ #68 ما زال مفتوحًا لحفظ شرط التقرير المستقل \| تحديث #68 عند توفر تقرير كامل أو قبول حقيقي \|"` | — |
| [SRC-62CE5126F9-L000184](../OMARAI_REMEDIATION_REGISTER_AR.md#L184) | 184 | ``"\| OMR-I-006 \| مخرجات index مع تغييرات الكود \| ملفات الفهرس المولدة تزيد حجم diff \| `update_index.yml`/generator \| **FIXED_PROCESS** — المولد هو المصدر الوحيد وتنجح فحوصه؛ الرأس النهائي يختلف بملفات مولدة فقط \| تجنب تعديل outputs يدويًا وعدم تجاوز مراجعة PR \|"`` | — |
| [SRC-62CE5126F9-L000185](../OMARAI_REMEDIATION_REGISTER_AR.md#L185) | 185 | ``"\| OMR-I-007 \| فروع قديمة مقابل main \| قواعد قديمة ومتباعدة \| PRs 63/72/74/25/26 \| **CLOSED_AS_SUPERSEDED**؛ #76 مُدمج الآن؛ أي عمل جديد يبنى من أحدث `main` \| أي عمل جديد يبنى من أحدث main \|"`` | — |
| [SRC-62CE5126F9-L000186](../OMARAI_REMEDIATION_REGISTER_AR.md#L186) | 186 | `""` | — |
| [SRC-62CE5126F9-L000187](../OMARAI_REMEDIATION_REGISTER_AR.md#L187) | 187 | `"### سجل مختصر لحالة طلبات الدمج ذات الصلة — 23 أكتوبر 2026"` | — |
| [SRC-62CE5126F9-L000188](../OMARAI_REMEDIATION_REGISTER_AR.md#L188) | 188 | `""` | — |
| [SRC-62CE5126F9-L000189](../OMARAI_REMEDIATION_REGISTER_AR.md#L189) | 189 | `"\| PR \| حالة GitHub التي تم فحصها \| المعالجة / القرار \|"` | — |
| [SRC-62CE5126F9-L000190](../OMARAI_REMEDIATION_REGISTER_AR.md#L190) | 190 | `"\|---\|---\|---\|"` | — |
| [SRC-62CE5126F9-L000191](../OMARAI_REMEDIATION_REGISTER_AR.md#L191) | 191 | ``"\| #25، #26 \| `CLOSED`, `MERGED=false` \| طلبا استضافة متداخلان؛ تاريخيان وغير مدمجين. \|"`` | — |
| [SRC-62CE5126F9-L000192](../OMARAI_REMEDIATION_REGISTER_AR.md#L192) | 192 | ``"\| #63 \| `CLOSED`, `MERGED=false` \| إصلاحات متداخلة؛ لم يُدمج. تُؤخذ الحاجة المتبقية فقط عبر PR حديث. \|"`` | — |
| [SRC-62CE5126F9-L000193](../OMARAI_REMEDIATION_REGISTER_AR.md#L193) | 193 | ``"\| #72 \| `CLOSED`, `MERGED=false` \| فرع فهرسة قديم؛ لا يدمج فوق الفهرسة الموجودة في `main`. \|"`` | — |
| [SRC-62CE5126F9-L000194](../OMARAI_REMEDIATION_REGISTER_AR.md#L194) | 194 | ``"\| #74 \| `CLOSED`, `MERGED=false` \| فرع إصلاح متداخل؛ لا يدمج لأن الإصلاحات المطلوبة أُعيد جمعها في المسار الذي انتهى إلى #76. \|"`` | — |
| [SRC-62CE5126F9-L000195](../OMARAI_REMEDIATION_REGISTER_AR.md#L195) | 195 | ``"\| #76 \| `CLOSED`, `MERGED=true` \| الإصلاح الأساسي مدمج في `main` عند `528a255...`. \|"`` | — |
| [SRC-62CE5126F9-L000196](../OMARAI_REMEDIATION_REGISTER_AR.md#L196) | 196 | `""` | — |
| [SRC-62CE5126F9-L000197](../OMARAI_REMEDIATION_REGISTER_AR.md#L197) | 197 | `"## E. الوثائق والمكونات غير الضرورية"` | — |
| [SRC-62CE5126F9-L000198](../OMARAI_REMEDIATION_REGISTER_AR.md#L198) | 198 | `""` | — |
| [SRC-62CE5126F9-L000199](../OMARAI_REMEDIATION_REGISTER_AR.md#L199) | 199 | `"\| المعرّف \| الأصل \| الحالة \| الإجراء ومعيار الإغلاق \|"` | — |
| [SRC-62CE5126F9-L000200](../OMARAI_REMEDIATION_REGISTER_AR.md#L200) | 200 | `"\|---\|---\|---\|---\|"` | — |
| [SRC-62CE5126F9-L000201](../OMARAI_REMEDIATION_REGISTER_AR.md#L201) | 201 | ``"\| OMR-DOC-001 \| مصفوفة أدلة الاختبار \| لقطة 19 أكتوبر تاريخية \| `docs/OMARAI_TEST_EVIDENCE_MATRIX_AR.md` \| **HISTORICAL + RECONCILED IN #77** — نتائج 380 اختبارًا تنتمي إلى تشغيل تاريخي؛ المرجع اللاحق بعد #76 هو 384 اختبارًا لكل إصدار Python في run #39654908040. \| تبقى النتائج السابقة تاريخية، وتُحدَّث الحالة الحالية دون محو سجل الأدلة القديمة. \|"`` | — |
| [SRC-62CE5126F9-L000202](../OMARAI_REMEDIATION_REGISTER_AR.md#L202) | 202 | `"\| OMR-DOC-002 \| سجل المتطلبات والتسوية التشغيلية \| ادعاءات وlinks إلى SHAs قديمة \| requirements register + operational reconciliation \| **UPDATED_IN #76** — إضافات بتاريخ 21 أكتوبر تربط الأدلة بالـSHA الحالي ومرشح #76 \| تحديث فقط بعد ظهور دليل/نسخة جديدة، لا إعادة تأريخ تاريخي \|"` | — |
| [SRC-62CE5126F9-L000203](../OMARAI_REMEDIATION_REGISTER_AR.md#L203) | 203 | `"\| OMR-DOC-003 \| README ودليل الاستضافة \| وصف وظيفة غير موجودة أو حدود تشغيل غير صريحة \| README، Go-Live، deployment docs، scope \| **UPDATED_IN #76** — search_code، SHA البناء، single-operator، وVolume/hosted smoke موضحة \| لا توثيق لوظيفة غير موجودة؛ الحفاظ على التحذير من NOT_RUN \|"` | — |
| [SRC-62CE5126F9-L000204](../OMARAI_REMEDIATION_REGISTER_AR.md#L204) | 204 | `"\| OMR-DOC-004 \| تقرير Grok داخل artifacts \| الملف الكامل غير قابل للعثور عليه في main بحسب جلب المسار \| artifact path الوارد \| **PARTIAL** — ملخص مقدم من Human Director؛ لا نختلق ملفًا أو ننسبه لـGrok GitHub \| توفير artifact قابل للوصول أو الاستمرار بتتبع الملخص بصفته user-provided \|"` | — |
| [SRC-62CE5126F9-L000205](../OMARAI_REMEDIATION_REGISTER_AR.md#L205) | 205 | ``"\| OMR-S-001 \| البحث المحلي داخل الكود \| P1 \| الأداة كانت موصوفة في README وغير موجودة في main، وكانت الروابط ثابتة على `blob/main` \| `docs/search_code.py`, `tests/test_search_code.py` \| **FIXED_AND_TESTED — مدمج في `main` عبر #76** — أضيف `--ref` و`OMARAI_GITHUB_REF` واستخراج SHA من البيئة/HEAD المحلي؛ الاختبارات ضمن 384 اختبارًا ناجحًا على كلا إصدارَي Python في [#39653079608](https://github.com/mosabosama2030-oss/omarai/actions/runs/39653079608) \| وظيفة البحث المحلي موجودة في `main`; اختبارات PR الأحدث موثقة في الملحق ما بعد الدمج \|"`` | — |
| [SRC-62CE5126F9-L000206](../OMARAI_REMEDIATION_REGISTER_AR.md#L206) | 206 | ``"\| OMR-I-008 \| روابط بحث الفهرس \| P1 \| تثبيت `GITHUB_BLOB_BASE` على `blob/main` يضلل مراجع PR لأن نتيجة البحث قد تكون في commit/فرع غير main \| `docs/search_code.py`, `tests/test_search_code.py` \| **FIXED_AND_TESTED على `463f4a4...`** — اختبارات المرجع الصريح وبيئة SHA والـCLI اجتازت CI ضمن 384 اختبارًا على Python 3.11 و3.12 في [#39654530305](https://github.com/mosabosama2030-oss/omarai/actions/runs/39654530305). المقارنة من `463f4a4...` إلى الرأس المولد `faba150...` لا تحتوي إلا صفحات فهرس مولدة. \| عند تغيير أداة البحث، أعد الاختبارات؛ الروابط الحالية يجب أن تشير إلى المرجع المختار لا `main` دائمًا \|"`` | — |
| [SRC-62CE5126F9-L000207](../OMARAI_REMEDIATION_REGISTER_AR.md#L207) | 207 | `"\| OMR-S-002 \| Skills/Workflows الدائمة أو تعدد الوكلاء \| **PROPOSED / NOT REQUIRED FOR FOUNDATION** \| لا تُنفذ الآن دون حاجة مثبتة؛ حافظ على نواة موثوقة وعقود أدوات وWorkflows قابلة للاختبار قبل توسع الوكلاء \|"` | — |
| [SRC-62CE5126F9-L000208](../OMARAI_REMEDIATION_REGISTER_AR.md#L208) | 208 | `"\| OMR-S-003 \| موصلات بحث اختيارية \| **REVIEW REQUIRED** \| لا تحذف موصلًا بناءً على عدم استعماله في اختبار واحد؛ احتفظ به إن كان خلف إعداد اختياري وله اختبارات وحدود تكلفة واضحة؛ احذف التكرار المثبت فقط \|"` | — |
| [SRC-62CE5126F9-L000209](../OMARAI_REMEDIATION_REGISTER_AR.md#L209) | 209 | `""` | — |
| [SRC-62CE5126F9-L000210](../OMARAI_REMEDIATION_REGISTER_AR.md#L210) | 210 | `"## E1. حالة واجهة الاستخدام المستقلة"` | — |
| [SRC-62CE5126F9-L000211](../OMARAI_REMEDIATION_REGISTER_AR.md#L211) | 211 | `""` | — |
| [SRC-62CE5126F9-L000212](../OMARAI_REMEDIATION_REGISTER_AR.md#L212) | 212 | `"\| المعرّف \| الأصل \| الخطورة \| الحالة الحالية \| معيار الإغلاق \|"` | — |
| [SRC-62CE5126F9-L000213](../OMARAI_REMEDIATION_REGISTER_AR.md#L213) | 213 | `"\|---\|---\|---:\|---\|---\|"` | — |
| [SRC-62CE5126F9-L000214](../OMARAI_REMEDIATION_REGISTER_AR.md#L214) | 214 | `"\| OMR-UI-001 \| Issue #11 — حالات واجهة البحث العربية \| P2 \| **PARTIAL** — #76 يحدّث واجهة الأدلة والحالات، لكن لا يوجد إثبات اختبار متصفح/Android يدوي على الرأس المقترح \| إبقاء #11 مفتوحًا حتى التحقق من حالات التحميل/النجاح/التدهور/الفشل، الروابط، عدم عرض إجابة قديمة، RTL/عرض ضيق، ولوحة المفاتيح/التباين؛ أرفق دليلًا ولا تدّع أتمتة غير موجودة \|"` | — |
| [SRC-62CE5126F9-L000215](../OMARAI_REMEDIATION_REGISTER_AR.md#L215) | 215 | `""` | — |
| [SRC-62CE5126F9-L000216](../OMARAI_REMEDIATION_REGISTER_AR.md#L216) | 216 | `"## F. ملخص بوابات الإغلاق"` | — |
| [SRC-62CE5126F9-L000217](../OMARAI_REMEDIATION_REGISTER_AR.md#L217) | 217 | `""` | — |
| [SRC-62CE5126F9-L000218](../OMARAI_REMEDIATION_REGISTER_AR.md#L218) | 218 | `"### مغلق ومختبر على main"` | — |
| [SRC-62CE5126F9-L000219](../OMARAI_REMEDIATION_REGISTER_AR.md#L219) | 219 | `"- **E3** إزالة عرض تغطية الأدلة كنسبة ثقة."` | — |
| [SRC-62CE5126F9-L000220](../OMARAI_REMEDIATION_REGISTER_AR.md#L220) | 220 | `"- **E4** إصلاح truthiness في مستوى البحث الاحتياطي."` | — |
| [SRC-62CE5126F9-L000221](../OMARAI_REMEDIATION_REGISTER_AR.md#L221) | 221 | ``"كلاهما مرتبط بـ#75 المدمج في `main` عند `d46a546...`."`` | — |
| [SRC-62CE5126F9-L000222](../OMARAI_REMEDIATION_REGISTER_AR.md#L222) | 222 | `""` | — |
| [SRC-62CE5126F9-L000223](../OMARAI_REMEDIATION_REGISTER_AR.md#L223) | 223 | `"### مدمج ومختبر آليًا عبر PR #76"` | — |
| [SRC-62CE5126F9-L000224](../OMARAI_REMEDIATION_REGISTER_AR.md#L224) | 224 | `"- توجيه الأسئلة الناقصة إلى CLARIFY وتوحيد متابعة السياق."` | — |
| [SRC-62CE5126F9-L000225](../OMARAI_REMEDIATION_REGISTER_AR.md#L225) | 225 | `"- تشخيصات منظمة لحالات استخراج الصفحات والموصلات، مع حدود واضحة لما تثبته."` | — |
| [SRC-62CE5126F9-L000226](../OMARAI_REMEDIATION_REGISTER_AR.md#L226) | 226 | `"- منع التحويل التلقائي لموفري البحث الذين تغطيهم الاختبارات."` | — |
| [SRC-62CE5126F9-L000227](../OMARAI_REMEDIATION_REGISTER_AR.md#L227) | 227 | ``"- CSP hash ورؤوس الحماية دون `unsafe-inline`."`` | — |
| [SRC-62CE5126F9-L000228](../OMARAI_REMEDIATION_REGISTER_AR.md#L228) | 228 | `"- هوية بناء SHA واختبار مقارنة SHA في hosted smoke (الكود موجود؛ hosted smoke حي NOT_RUN)."` | — |
| [SRC-62CE5126F9-L000229](../OMARAI_REMEDIATION_REGISTER_AR.md#L229) | 229 | `"- مسار SQLite قابل للضبط، أداة البحث المحلي، وتوثيق نطاق التشغيل."` | — |
| [SRC-62CE5126F9-L000230](../OMARAI_REMEDIATION_REGISTER_AR.md#L230) | 230 | ``"- إصلاح سباق الفهرسة في CI على المراجع غير `main` مع إبقاء تحقق `main` صارمًا."`` | — |
| [SRC-62CE5126F9-L000231](../OMARAI_REMEDIATION_REGISTER_AR.md#L231) | 231 | `""` | — |
| [SRC-62CE5126F9-L000232](../OMARAI_REMEDIATION_REGISTER_AR.md#L232) | 232 | ``"**أحدث دليل PR بعد تحديث الفهرس:** [run #39654908040](https://github.com/mosabosama2030-oss/omarai/actions/runs/39654908040) — 384 اختبارًا ناجحًا على كل من Python 3.11 و3.12، وRuff ومزامنة/فحص الفهرس وبناء الحاوية وAPI المحمي ناجحة على رأس PR `3fb028...` قبل الدمج. التزام الدمج هو `528a255...`; لا يوجد في هذه اللقطة إثبات مباشر لتشغيل push على SHA الدمج. انظر تقرير ما بعد الدمج."`` | — |
