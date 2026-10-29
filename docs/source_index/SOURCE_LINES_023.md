# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **023**
- سجلات الأسطر: **800**
- النطاق: SRC-E73001D9AC-L000760 إلى SRC-D17CE3D12F-L000656
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## وثائق وفهرسة

### FILE-E73001D9AC — [docs/OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
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
| [SRC-D17CE3D12F-L000253](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L253) | 253 | `"2. MUST تدوير وإبطال المفاتيح عند الاشتباه في تسربها، وتوثيق طريقة التدوير واختباره."` | — |
| [SRC-D17CE3D12F-L000254](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L254) | 254 | `"3. MUST استخدام TLS للاتصالات الشبكية التي تتطلبه وعدم تعطيل التحقق من الشهادات في الإنتاج."` | — |
| [SRC-D17CE3D12F-L000255](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L255) | 255 | `"4. SHOULD استخدام خدمات إدارة الأسرار المتاحة عند ملاءمتها، أو متغيرات بيئة محمية على الأقل في البيئات الصغيرة."` | — |
| [SRC-D17CE3D12F-L000256](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L256) | 256 | `"5. MUST تقليل صلاحيات رموز CI/CD وGitHub والوصول إلى المستودع، ومنع نشر أسرار في logs."` | — |
| [SRC-D17CE3D12F-L000257](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L257) | 257 | `"6. SHOULD استخدام صلاحيات قصيرة العمر وOIDC بدل مفاتيح نشر ثابتة عندما تدعم المنصة ذلك."` | — |
| [SRC-D17CE3D12F-L000258](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L258) | 258 | `"7. MUST عدم اعتبار تعمية السر أو ترميزه تشفيرًا، وعدم وضع أسرار حساسة في ملفات يملك المتصفح الوصول إليها."` | — |
| [SRC-D17CE3D12F-L000259](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L259) | 259 | `"8. MUST عدم تسجيل Authorization headers أو cookies أو tokens أو بيانات نموذج حساسة في telemetry."` | — |
| [SRC-D17CE3D12F-L000260](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L260) | 260 | `"9. SHOULD مراجعة تدوير الشهادات والرموز وانتهاء الصلاحية كجزء من الجاهزية التشغيلية."` | — |
| [SRC-D17CE3D12F-L000261](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L261) | 261 | `"10. MUST أن تعتمد سياسات التفويض على محرك موثوق خارج مخرجات النموذج؛ لا يستطيع النموذج أن يمنح نفسه صلاحية."` | — |
| [SRC-D17CE3D12F-L000262](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L262) | 262 | `""` | — |
| [SRC-D17CE3D12F-L000263](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L263) | 263 | `"## 18. أمن سلسلة توريد البرمجيات"` | — |
| [SRC-D17CE3D12F-L000264](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L264) | 264 | `""` | — |
| [SRC-D17CE3D12F-L000265](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L265) | 265 | `"1. MUST تثبيت إصدارات الاعتماديات المباشرة وغير المباشرة بآلية قابلة لإعادة الإنتاج حيثما أمكن."` | — |
| [SRC-D17CE3D12F-L000266](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L266) | 266 | `"2. SHOULD مراقبة الثغرات والاعتماديات المهجورة والتراخيص والتعارضات، وتحديثها باختبارات توافق."` | — |
| [SRC-D17CE3D12F-L000267](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L267) | 267 | `"3. MUST عدم تثبيت artifact أو action أو dependency مجهولة المصدر أو متغيرة بصمت في مسار إنتاج حساس."` | — |
| [SRC-D17CE3D12F-L000268](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L268) | 268 | `"4. SHOULD تثبيت GitHub Actions الخارجية على full-length commit SHA عند استخدامها، مع تقليل صلاحيات GITHUB_TOKEN إلى أدنى ما يلزم."` | — |
| [SRC-D17CE3D12F-L000269](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L269) | 269 | `"5. MUST عدم تشغيل بناء أو اختبار على كود غير موثوق مع أسرار إنتاج أو صلاحيات نشر."` | — |
| [SRC-D17CE3D12F-L000270](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L270) | 270 | `"6. SHOULD توليد SBOM وبيانات provenance لإصدارات التوزيع حين تنضج عملية البناء وتبرر الحاجة."` | — |
| [SRC-D17CE3D12F-L000271](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L271) | 271 | `"7. MUST أن تكون ملفات البناء والاعتماديات جزءًا من المراجعة، لا حاشية غير مرئية."` | — |
| [SRC-D17CE3D12F-L000272](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L272) | 272 | `"8. SHOULD فحص التسريبات والأسرار والمكونات المعروفة الضعف ضمن CI عند توفر الأدوات."` | — |
| [SRC-D17CE3D12F-L000273](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L273) | 273 | `"9. MUST توثيق كيفية إنشاء artifact ونشره والتحقق من النسخة المنشورة مقابل commit مقصود."` | — |
| [SRC-D17CE3D12F-L000274](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L274) | 274 | `"10. MUST أن تكون أذونات CI والبيئة المخصصة للنشر منفصلة، وأن يتطلب النشر الفعلي تفويضًا واضحًا."` | — |
| [SRC-D17CE3D12F-L000275](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L275) | 275 | `""` | — |
| [SRC-D17CE3D12F-L000276](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L276) | 276 | `"---"` | — |
| [SRC-D17CE3D12F-L000277](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L277) | 277 | `""` | — |
| [SRC-D17CE3D12F-L000278](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L278) | 278 | `"# القسم السادس — التسليم والتشغيل واستعادة الخدمة"` | — |
| [SRC-D17CE3D12F-L000279](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L279) | 279 | `""` | — |
| [SRC-D17CE3D12F-L000280](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L280) | 280 | `"## 19. هندسة CI/CD وإدارة الإصدارات"` | — |
| [SRC-D17CE3D12F-L000281](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L281) | 281 | `""` | — |
| [SRC-D17CE3D12F-L000282](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L282) | 282 | `"1. MUST أن يكون لكل تغيير مؤثر feedback سريع من الاختبارات والفحوص قبل الدمج."` | — |
| [SRC-D17CE3D12F-L000283](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L283) | 283 | `"2. SHOULD استخدام CI متكرر وقابل لإعادة التشغيل؛ وألا يتطلب النجاح خطوات محلية غير موثقة."` | — |
| [SRC-D17CE3D12F-L000284](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L284) | 284 | `"3. MUST فصل الاختبارات السريعة عن اختبارات التكامل والحمل والأمن التي تحتاج بيئة مختلفة، مع بيان ما تم تشغيله فعلًا."` | — |
| [SRC-D17CE3D12F-L000285](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L285) | 285 | `"4. MUST مراجعة التغيير النهائي والملفات والأذونات والفروق، وعدم الاعتماد على تقرير الوكيل وحده."` | — |
| [SRC-D17CE3D12F-L000286](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L286) | 286 | `"5. SHOULD بناء artifact مرة واحدة ثم ترقيته بين البيئات بدل إعادة البناء بطريقة قد تنتج artifact مختلفًا لكل بيئة."` | — |
| [SRC-D17CE3D12F-L000287](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L287) | 287 | `"6. SHOULD استخدام canary أو progressive rollout أو blue/green عند دعم البنية وحجم الخطر لذلك، وليس شرطًا على استضافة لا تدعمه."` | — |
| [SRC-D17CE3D12F-L000288](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L288) | 288 | `"7. MUST وجود طريقة rollback أو kill switch أو إصدار سابق صالح لكل تغيير عالي الأثر بقدر الإمكان."` | — |
| [SRC-D17CE3D12F-L000289](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L289) | 289 | `"8. MUST أن تتوافق ترحيلات قاعدة البيانات مع ترتيب الإطلاق والتراجع؛ لا تفترض أن الرجوع عن كود جديد يعكس تغيير البيانات تلقائيًا."` | — |
| [SRC-D17CE3D12F-L000290](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L290) | 290 | `"9. SHOULD إدارة feature flags بمالك وغرض وتاريخ مراجعة وخطة إزالة."` | — |
| [SRC-D17CE3D12F-L000291](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L291) | 291 | `"10. MUST عدم الدمج أو النشر للإنتاج من وكيل آلي دون تفويض صريح من مدير المشروع."` | — |
| [SRC-D17CE3D12F-L000292](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L292) | 292 | `"11. SHOULD استخدام إصدارات واضحة وchangelog للتغييرات ذات الأثر على المستخدم أو الواجهات أو البيانات."` | — |
| [SRC-D17CE3D12F-L000293](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L293) | 293 | `"12. MUST معرفة commit الذي اختُبر والذي نُشر؛ لا يساوي نجاح CI على فرع آخر دليلًا على النسخة المنشورة."` | — |
| [SRC-D17CE3D12F-L000294](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L294) | 294 | `""` | — |
| [SRC-D17CE3D12F-L000295](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L295) | 295 | `"## 20. النسخ الاحتياطي والتعافي من الكوارث"` | — |
| [SRC-D17CE3D12F-L000296](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L296) | 296 | `""` | — |
| [SRC-D17CE3D12F-L000297](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L297) | 297 | `"1. MUST تصنيف البيانات التي يمكن إعادة بنائها مقابل البيانات التي لا يمكن تعويضها."` | — |
| [SRC-D17CE3D12F-L000298](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L298) | 298 | `"2. MUST تحديد RPO (الحد المقبول لفقد البيانات) وRTO (زمن الاستعادة المستهدف) بصورة واقعية للبيانات والخدمات المهمة، أو التصريح بأنها UNKNOWN في غياب القياس."` | — |
| [SRC-D17CE3D12F-L000299](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L299) | 299 | `"3. MUST اختبار الاستعادة فعليًا للبيانات المهمة؛ وجود ملف نسخة احتياطية غير كافٍ."` | — |
| [SRC-D17CE3D12F-L000300](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L300) | 300 | `"4. SHOULD حفظ النسخ المهمة بعيدًا عن صلاحيات التطبيق التشغيلية نفسها عندما تسمح الإمكانات، لحمايتها من حذف أو اختراق واحد."` | — |
| [SRC-D17CE3D12F-L000301](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L301) | 301 | `"5. MUST حماية النسخ الاحتياطية من الوصول غير المصرح به، وتحديد التشفير وفترة الاحتفاظ والإزالة."` | — |
| [SRC-D17CE3D12F-L000302](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L302) | 302 | `"6. SHOULD إجراء تمارين استعادة أو failover عند تغير بنية التخزين أو الاستضافة أو طريقة النشر."` | — |
| [SRC-D17CE3D12F-L000303](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L303) | 303 | `"7. MUST تحديد ما لا يمكن استعادته إذا انقطع موفر مجاني أو حُذف حساب الاستضافة، وخطة نقل واقعية لتجنب الارتباط غير المدروس."` | — |
| [SRC-D17CE3D12F-L000304](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L304) | 304 | `"8. MUST توثيق خطوات إعادة إنشاء البيئة والأسرار من المصدر المعتمد دون وضع الأسرار في المستودع."` | — |
| [SRC-D17CE3D12F-L000305](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L305) | 305 | `"9. SHOULD اختبار استعادة إعدادات وبيانات المستخدم وسجلات التدقيق حسب أهمية كل فئة."` | — |
| [SRC-D17CE3D12F-L000306](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L306) | 306 | `"10. MUST عدم وصف النظام بأنه عالي التوافر إذا كان مكون حرج وحيد يشكل نقطة فشل واحدة بلا بديل."` | — |
| [SRC-D17CE3D12F-L000307](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L307) | 307 | `""` | — |
| [SRC-D17CE3D12F-L000308](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L308) | 308 | `"## 21. جاهزية التشغيل والمراقبة والتنبيه"` | — |
| [SRC-D17CE3D12F-L000309](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L309) | 309 | `""` | — |
| [SRC-D17CE3D12F-L000310](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L310) | 310 | `"1. MUST التمييز بين liveness (العملية تعمل) وreadiness (تستطيع قبول طلبات) وصحة الاعتماديات حيث تدعم البيئة ذلك."` | — |
| [SRC-D17CE3D12F-L000311](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L311) | 311 | `"2. MUST ألا يكشف health endpoint أسرارًا أو معلومات داخلية تفيد المهاجم؛ تعرض تفاصيل التشخيص للمخولين فقط."` | — |
| [SRC-D17CE3D12F-L000312](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L312) | 312 | `"3. SHOULD توحيد التنسيق بين السجلات والمقاييس والتتبعات باستخدام معايير مثل OpenTelemetry عند ملاءمة الحجم."` | — |
| [SRC-D17CE3D12F-L000313](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L313) | 313 | `"4. MUST ربط مسار الطلب بمعرّف تتبع عبر المكونات عند إمكان ذلك، دون استخدام المعرّف لإدخال معلومات شخصية حساسة."` | — |
| [SRC-D17CE3D12F-L000314](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L314) | 314 | `"5. MUST أن تكون التنبيهات قابلة للتصرف ومرتبطة بأثر المستخدم أو خطر حقيقي، لا بكل حدث عابر."` | — |
| [SRC-D17CE3D12F-L000315](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L315) | 315 | `"6. SHOULD تقليل التنبيهات المكررة وضبط الحساسية ومراجعة التنبيهات الكاذبة."` | — |
| [SRC-D17CE3D12F-L000316](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L316) | 316 | `"7. MUST تحديد حدود للاحتفاظ بالـ logs/traces وحجمها وكاردينالية المقاييس وتكلفتها."` | — |
| [SRC-D17CE3D12F-L000317](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L317) | 317 | `"8. MUST حجب أو تنقيح الأسرار والبيانات الشخصية من السجلات والتتبعات ورسائل الخطأ."` | — |
| [SRC-D17CE3D12F-L000318](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L318) | 318 | `"9. SHOULD تضمين مؤشرات تجربة المستخدم، مثل نجاح المسار وزمن الإنجاز وفشل المصادر، وليس CPU وحده."` | — |
| [SRC-D17CE3D12F-L000319](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L319) | 319 | `"10. MUST توثيق ما تستطيع لوحة القياس إثباته وما لا تستطيع إثباته."` | — |
| [SRC-D17CE3D12F-L000320](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L320) | 320 | `""` | — |
| [SRC-D17CE3D12F-L000321](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L321) | 321 | `"---"` | — |
| [SRC-D17CE3D12F-L000322](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L322) | 322 | `""` | — |
| [SRC-D17CE3D12F-L000323](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L323) | 323 | `"# القسم السابع — الواجهة وتجربة المستخدم وإمكانية الوصول"` | — |
| [SRC-D17CE3D12F-L000324](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L324) | 324 | `""` | — |
| [SRC-D17CE3D12F-L000325](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L325) | 325 | `"## 22. الوصولية Accessibility والتوافق مع المتصفحات"` | — |
| [SRC-D17CE3D12F-L000326](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L326) | 326 | `""` | — |
| [SRC-D17CE3D12F-L000327](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L327) | 327 | `"1. SHOULD استهداف WCAG 2.2 مستوى AA للواجهة العامة بدرجة تتناسب مع طبيعتها، مع تقييم عملي لا إعلان امتثال تلقائي."` | — |
| [SRC-D17CE3D12F-L000328](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L328) | 328 | `"2. MUST أن تكون الوظائف الأساسية قابلة للاستخدام بلوحة المفاتيح، مع حالات تركيز واضحة وتسلسل منطقي."` | — |
| [SRC-D17CE3D12F-L000329](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L329) | 329 | `"3. SHOULD استخدام دلالات HTML صحيحة، وتسميات واضحة لحقول الإدخال والأزرار ورسائل الأخطاء."` | — |
| [SRC-D17CE3D12F-L000330](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L330) | 330 | `"4. MUST عدم الاعتماد على اللون وحده لإظهار الحالة أو الخطأ."` | — |
| [SRC-D17CE3D12F-L000331](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L331) | 331 | `"5. SHOULD احترام تفضيل تقليل الحركة، والتباين، والتكبير، وحجم النص المناسب."` | — |
| [SRC-D17CE3D12F-L000332](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L332) | 332 | `"6. MUST اختبار التفاعل مع قارئ شاشة بصورة دورية إذا كان المنتج عامًا أو يعتمد على تفاعل معقد."` | — |
| [SRC-D17CE3D12F-L000333](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L333) | 333 | `"7. MUST ألا تخفي طبقات التحميل أو الأخطاء طريقة متابعة الاستخدام أو إعادة المحاولة."` | — |
| [SRC-D17CE3D12F-L000334](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L334) | 334 | `"8. SHOULD اختبار المتصفحات والأجهزة الواقعية التي يستهدفها المنتج، خصوصًا Android إذا كان استخدامه أساسيًا."` | — |
| [SRC-D17CE3D12F-L000335](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L335) | 335 | `"9. MUST حماية الواجهة من XSS باستخدام ترميز/تعقيم مناسب عند عرض HTML أو Markdown أو نصوص مستخرجة من صفحات خارجية."` | — |
| [SRC-D17CE3D12F-L000336](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L336) | 336 | `"10. MUST اختبار حدود الواجهة بين المحتوى الموثوق وغير الموثوق؛ النص المستخرج لا يُعرض كـ HTML موثوق تلقائيًا."` | — |
| [SRC-D17CE3D12F-L000337](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L337) | 337 | `""` | — |
| [SRC-D17CE3D12F-L000338](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L338) | 338 | `"## 23. العربية والتدويل والاتجاه من اليمين إلى اليسار"` | — |
| [SRC-D17CE3D12F-L000339](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L339) | 339 | `""` | — |
| [SRC-D17CE3D12F-L000340](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L340) | 340 | `"1. MUST الحفاظ على Unicode وإجراء normalization مناسب للبحث والمقارنة دون تغيير معنى النص الأصلي المعروض."` | — |
| [SRC-D17CE3D12F-L000341](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L341) | 341 | `"2. MUST اختبار النص المختلط عربي/إنجليزي والأرقام والروابط والكود وعناوين المصادر داخل واجهة RTL."` | — |
| [SRC-D17CE3D12F-L000342](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L342) | 342 | ``"3. SHOULD استخدام خصائص الاتجاه والعزل ثنائي الاتجاه مثل `dir` و`bdi` و`unicode-bidi` بحذر مناسب، لا حيل تنسيق عامة تكسر النصوص."`` | — |
| [SRC-D17CE3D12F-L000343](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L343) | 343 | `"4. MUST عدم تغيير ترتيب الرموز التقنية أو الروابط أو المعرفات عند عرضها داخل نص عربي."` | — |
| [SRC-D17CE3D12F-L000344](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L344) | 344 | `"5. SHOULD فصل الرسائل المرئية عن مفاتيح النصوص حتى يمكن إضافة لغة مستقبلية دون إعادة كتابة المنطق."` | — |
| [SRC-D17CE3D12F-L000345](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L345) | 345 | `"6. MUST تنسيق التواريخ والأرقام والوقت والعملات وفق locale عند عرضها، مع إظهار المنطقة الزمنية للمعلومات الحساسة للوقت."` | — |
| [SRC-D17CE3D12F-L000346](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L346) | 346 | `"7. SHOULD اختبار اختلافات همزات الألف والتاء المربوطة والياء والألف المقصورة والتشكيل في البحث العربي، مع المحافظة على النص الأصلي والتعامل مع التطبيع بوصفه أداة بحث لا دليلاً على تطابق المعنى."` | — |
| [SRC-D17CE3D12F-L000347](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L347) | 347 | `"8. MUST ألا يؤدي اتجاه RTL إلى كشف الرابط المضلل أو إخفاء نطاقه؛ اعرض النطاق بطريقة واضحة."` | — |
| [SRC-D17CE3D12F-L000348](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L348) | 348 | `"9. SHOULD أن تكون رسائل الخطأ والحالة والقيود بالعربية الواضحة للمستخدم المستهدف."` | — |
| [SRC-D17CE3D12F-L000349](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L349) | 349 | `"10. MUST اختبار النصوص الطويلة جدًا والروابط غير القابلة للكسر والتفاف الكود ومحتوى الأجهزة الصغيرة."` | — |
| [SRC-D17CE3D12F-L000350](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L350) | 350 | `""` | — |
| [SRC-D17CE3D12F-L000351](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L351) | 351 | `"## 24. أداء الواجهة وتجربة الفشل"` | — |
| [SRC-D17CE3D12F-L000352](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L352) | 352 | `""` | — |
| [SRC-D17CE3D12F-L000353](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L353) | 353 | `"1. SHOULD وضع ميزانية أداء للواجهة باستخدام مقاييس واقعية مثل Core Web Vitals عندما تنطبق."` | — |
| [SRC-D17CE3D12F-L000354](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L354) | 354 | `"2. MUST إظهار حالة الطلب بوضوح عند التنفيذ الطويل: جاري البحث، جُمعت المصادر، تعطل مصدر، أو انتهى الطلب."` | — |
| [SRC-D17CE3D12F-L000355](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L355) | 355 | `"3. SHOULD دعم إلغاء الطلب أو إعادة المحاولة دون تكرار إجراءات ضارة."` | — |
| [SRC-D17CE3D12F-L000356](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L356) | 356 | `"4. MUST ألا يفقد المستخدم نصًا كتبه بسبب فشل شبكة غير متوقع دون توضيح أو وسيلة استعادة مناسبة."` | — |
| [SRC-D17CE3D12F-L000357](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L357) | 357 | `"5. MUST التعامل مع الشبكات الضعيفة والأخطاء المؤقتة دون loops إعادة تحميل أو طلبات متكررة غير محدودة."` | — |
| [SRC-D17CE3D12F-L000358](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L358) | 358 | `"6. SHOULD إظهار حالة جزئية صادقة إن كانت مفيدة، وفصلها عن النجاح الكامل."` | — |
| [SRC-D17CE3D12F-L000359](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L359) | 359 | `"7. MUST عدم إظهار مصادر أو بيانات تجريبية وكأنها نتائج حقيقية في وضع الإنتاج."` | — |
| [SRC-D17CE3D12F-L000360](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L360) | 360 | `"8. SHOULD الحفاظ على قابلية استخدام الواجهة عند غياب JavaScript أو تعطل مكوّن بصري إذا كانت طبيعة المنتج تسمح."` | — |
| [SRC-D17CE3D12F-L000361](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L361) | 361 | `""` | — |
| [SRC-D17CE3D12F-L000362](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L362) | 362 | `"---"` | — |
| [SRC-D17CE3D12F-L000363](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L363) | 363 | `""` | — |
| [SRC-D17CE3D12F-L000364](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L364) | 364 | `"# القسم الثامن — محرك البحث والمعرفة وجودة الإجابة"` | — |
| [SRC-D17CE3D12F-L000365](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L365) | 365 | `""` | — |
| [SRC-D17CE3D12F-L000366](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L366) | 366 | `"## 25. جودة خط البحث والاسترجاع (Search/Retrieval Quality)"` | — |
| [SRC-D17CE3D12F-L000367](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L367) | 367 | `""` | — |
| [SRC-D17CE3D12F-L000368](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L368) | 368 | `"1. MUST الفصل بين سؤال المستخدم، واستعلامات البحث، والصفحات المسترجعة، والمقاطع المستخرجة، والأدلة التي دعمت الإجابة."` | — |
| [SRC-D17CE3D12F-L000369](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L369) | 369 | `"2. SHOULD قياس جودة البحث على مجموعة أسئلة تمثيلية عبر precision/recall أو مقاييس مناسبة للمهمة؛ لا تكفي مراجعة بعض النتائج يدويًا فقط."` | — |
| [SRC-D17CE3D12F-L000370](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L370) | 370 | `"3. MUST إزالة التكرارات الواضحة ومعالجة إعادة النشر، والصفحات قليلة المحتوى، وصفحات الخطأ، والإعلانات التي تتظاهر بأنها محتوى."` | — |
| [SRC-D17CE3D12F-L000371](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L371) | 371 | `"4. SHOULD تقدير حداثة المصدر وملاءمته وموثوقيته وتعارضه مع مصادر أخرى، وفق نوع الادعاء."` | — |
| [SRC-D17CE3D12F-L000372](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L372) | 372 | `"5. MUST عدم معاملة ترتيب نتيجة البحث على أنه دليل قطعي على صحتها."` | — |
| [SRC-D17CE3D12F-L000373](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L373) | 373 | `"6. MUST فصل وقت نشر المعلومة عن وقت وقوع الحدث وعن وقت جلب الصفحة عندما تتوفر هذه التواريخ، وتحديد التناقضات الزمنية."` | — |
| [SRC-D17CE3D12F-L000374](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L374) | 374 | `"7. SHOULD حفظ أقل قدر من البيانات الوصفية اللازمة لتتبع المصدر: URL النهائي، العنوان، تاريخ الجلب، حالة الاستخراج، ومؤشرات الفشل."` | — |
| [SRC-D17CE3D12F-L000375](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L375) | 375 | `"8. MUST احترام حدود الموارد وسياسات الوصول والحقوق والاستخدام المسموح للمصادر، وعدم محاولة تجاوز تسجيل الدخول أو الحماية."` | — |
| [SRC-D17CE3D12F-L000376](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L376) | 376 | `"9. SHOULD كشف النطاق النهائي والتمييز بين redirect والمصدر الأصلي، والحذر من النطاقات المشابهة أو المضللة."` | — |
| [SRC-D17CE3D12F-L000377](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L377) | 377 | `"10. MUST اختبار مسارات بحث عربية وإنجليزية وأسئلة تتطلب حداثة وأسئلة بلا إجابة موثوقة."` | — |
| [SRC-D17CE3D12F-L000378](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L378) | 378 | `"11. SHOULD قياس نجاح استخراج المحتوى لا مجرد نجاح HTTP، لأن صفحة وصلت قد تكون غير قابلة للاستخراج أو فارغة."` | — |
| [SRC-D17CE3D12F-L000379](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L379) | 379 | `"12. MUST ألا يُفهم فشل مصدر واحد على أنه دليل أن المعلومة غير موجودة في كل مكان."` | — |
| [SRC-D17CE3D12F-L000380](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L380) | 380 | `""` | — |
| [SRC-D17CE3D12F-L000381](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L381) | 381 | `"## 26. إسناد الادعاءات والمعرفة وحدود اليقين"` | — |
| [SRC-D17CE3D12F-L000382](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L382) | 382 | `""` | — |
| [SRC-D17CE3D12F-L000383](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L383) | 383 | `"1. MUST أن يكون لكل ادعاء جوهري يستند إلى الويب مسار واضح إلى المصدر أو مجموعة المصادر الداعمة."` | — |
| [SRC-D17CE3D12F-L000384](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L384) | 384 | `"2. MUST ألا تشير الإحالة إلى صفحة لم تدعم الادعاء فعليًا، وألا تُنشأ مراجع أو اقتباسات أو تواريخ غير موجودة."` | — |
| [SRC-D17CE3D12F-L000385](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L385) | 385 | `"3. SHOULD التفريق بين حقيقة موثقة، واستنتاج، ورأي، وتوقع، ومعلومة غير متاحة."` | — |
| [SRC-D17CE3D12F-L000386](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L386) | 386 | `"4. MUST التعامل مع تضارب المصادر بتوضيحه أو ترجيح الموثق مع بيان السبب؛ لا تُخفى المعارضة المهمة."` | — |
| [SRC-D17CE3D12F-L000387](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L387) | 387 | `"5. MUST أن يحدد النظام عدم اليقين والقيود، ويطلب توضيحًا عندما يغيّر الغموض الإجابة بشكل جوهري."` | — |
| [SRC-D17CE3D12F-L000388](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L388) | 388 | `"6. SHOULD بناء مجموعة تقييم عربية تغطي: صحة الحقائق، وملاءمة المصدر، وجودة الاستشهاد، واكتمال الإجابة، والتعامل مع عدم اليقين، وحداثة المعلومة."` | — |
| [SRC-D17CE3D12F-L000389](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L389) | 389 | `"7. MUST اختبار حالات لا يوجد فيها مصدر كافٍ، أو توجد مصادر متعارضة، أو الروابط ميتة، أو التاريخ قديم، أو المصدر لا يدعم الجملة."` | — |
| [SRC-D17CE3D12F-L000390](../OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md#L390) | 390 | `"8. SHOULD فصل جودة الصياغة عن صحة المحتوى؛ الإجابة الفصيحة قد تكون خاطئة."` | — |
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
