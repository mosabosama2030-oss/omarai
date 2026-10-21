# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **017**
- سجلات الأسطر: **800**
- النطاق: SRC-0F910493E8-L000626 إلى SRC-A8360B1B03-L000049
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## وثائق وفهرسة

### FILE-0F910493E8 — [docs/OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-0F910493E8-L000626](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L626) | 626 | `"2. تحقق من تسجيل الأداة وإصدارها وحالة إتاحتها."` | — |
| [SRC-0F910493E8-L000627](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L627) | 627 | `"3. تحقق من صلاحية العملية على موردها المحدد."` | — |
| [SRC-0F910493E8-L000628](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L628) | 628 | `"4. تحقق من صحة المخطط والأنواع والقيم والأحجام."` | — |
| [SRC-0F910493E8-L000629](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L629) | 629 | `"5. تحقق من الميزانية والوقت والتزامن والحد الأقصى للخطوات."` | — |
| [SRC-0F910493E8-L000630](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L630) | 630 | `"6. حدد هل الأداة قراءة فقط أم ذات أثر خارجي."` | — |
| [SRC-0F910493E8-L000631](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L631) | 631 | `"7. اطلب تأكيدًا بشريًا حيث تتطلب السياسة ذلك."` | — |
| [SRC-0F910493E8-L000632](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L632) | 632 | `"8. نفّذ عبر Adapter محدود."` | — |
| [SRC-0F910493E8-L000633](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L633) | 633 | `"9. تحقق من النتيجة الفعلية للأداة."` | — |
| [SRC-0F910493E8-L000634](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L634) | 634 | `"10. سجّل القرار والنتيجة دون أسرار."` | — |
| [SRC-0F910493E8-L000635](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L635) | 635 | `""` | — |
| [SRC-0F910493E8-L000636](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L636) | 636 | `"إذا استخدمت البنية رموز قدرات داخلية (capability tokens)، فلتكن قصيرة العمر، ومقيدة بالأداة والفعل والمورد والمهمة، وغير مكشوفة للنموذج أو المستخدم، وقابلة للإبطال، ولا تمنح سلطة لتوسيع نفسها. لا يلزم اعتماد بنية رموز منفصلة إذا كان التفويض داخل العملية أوضح وأقل تعقيدًا؛ المطلوب هو إنفاذ الصلاحية، لا إضافة تقنية شكلية."` | — |
| [SRC-0F910493E8-L000637](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L637) | 637 | `""` | — |
| [SRC-0F910493E8-L000638](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L638) | 638 | `"لا تُستخدم أوامر shell عامة أو eval أو exec أو استيراد ديناميكي أو عناوين/أسماء أدوات يولدها النموذج دون تحقق. لا تُبنى الأسماء أو الاستعلامات أو أوامر الملفات بسلاسل غير آمنة؛ استخدم واجهات محددة وتمرير وسائط ومخططات صريحة."` | — |
| [SRC-0F910493E8-L000639](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L639) | 639 | `""` | — |
| [SRC-0F910493E8-L000640](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L640) | 640 | `"## 17.7 مقاومة حقن التعليمات وإساءة استخدام النموذج"` | — |
| [SRC-0F910493E8-L000641](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L641) | 641 | `""` | — |
| [SRC-0F910493E8-L000642](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L642) | 642 | `"لا يُفترض أن النموذج سيقاوم كل محاولة حقن تعليمات. يجب أن يبقى ضرر النجاح في خداعه محدودًا بالتصميم."` | — |
| [SRC-0F910493E8-L000643](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L643) | 643 | `""` | — |
| [SRC-0F910493E8-L000644](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L644) | 644 | `"الضوابط:"` | — |
| [SRC-0F910493E8-L000645](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L645) | 645 | `"- فصل تعليمات النظام والسياسة عن طلب المستخدم وعن المحتوى الخارجي وعن نتائج الأدوات في تمثيل الرسائل والبيانات."` | — |
| [SRC-0F910493E8-L000646](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L646) | 646 | `"- وسم النص المسترجع والمرفقات على أنها بيانات غير موثوقة؛ لا تمنحها سلطة إصدار أوامر."` | — |
| [SRC-0F910493E8-L000647](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L647) | 647 | `"- لا يتخذ المحتوى الخارجي قرار تفويض ولا يغير أداة أو نطاقًا أو ميزانية."` | — |
| [SRC-0F910493E8-L000648](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L648) | 648 | `"- لا يسمح للنموذج بإرسال أسرار أو محتوى حساس إلى رابط أو موفر لمجرد أن صفحة طلبت ذلك."` | — |
| [SRC-0F910493E8-L000649](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L649) | 649 | `"- خطط LLM ومخرجاته هياكل بيانات غير موثوقة. تطبق عليها schema وallowlist وقواعد مجال وحدود عددية قبل التنفيذ."` | — |
| [SRC-0F910493E8-L000650](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L650) | 650 | `"- لا تمر الأداة الحساسة اعتمادًا على نية استنتجها النموذج وحده إذا كانت العملية تحتاج إلى موافقة واضحة."` | — |
| [SRC-0F910493E8-L000651](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L651) | 651 | `"- تعامل مع سياق المحادثة والذاكرة السابقة كمدخل قد يكون مزورًا أو مسمومًا؛ لا تجعل رسالة assistant المرسلة من العميل تتمتع بسلطة نظام."` | — |
| [SRC-0F910493E8-L000652](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L652) | 652 | `"- افصل نموذج قراءة المحتوى غير الموثوق عن القدرة على تنفيذ الأدوات حيث يبرر الخطر ذلك. وإذا تعذر الفصل، فعوضه بقيود تنفيذ أشد واختبارات واضحة."` | — |
| [SRC-0F910493E8-L000653](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L653) | 653 | `"- اختبر هجمات التعليمات المباشرة وغير المباشرة، وتعليمات استخراج الأسرار، وتغيير الهدف، ومحاولات طلب أدوات غير مسموحة، وتسميم الذاكرة."` | — |
| [SRC-0F910493E8-L000654](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L654) | 654 | `"- لا تستخدم «فلتر كلمات» أو System Prompt وحده باعتباره دفاعًا كاملًا."` | — |
| [SRC-0F910493E8-L000655](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L655) | 655 | `""` | — |
| [SRC-0F910493E8-L000656](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L656) | 656 | `"## 17.8 البحث والشبكة وSSRF وDNS rebinding"` | — |
| [SRC-0F910493E8-L000657](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L657) | 657 | `""` | — |
| [SRC-0F910493E8-L000658](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L658) | 658 | `"جلب الصفحات أحد أبرز حدود الخطر لأن URL قد يتحكم فيه المستخدم أو المصدر أو النموذج."` | — |
| [SRC-0F910493E8-L000659](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L659) | 659 | `""` | — |
| [SRC-0F910493E8-L000660](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L660) | 660 | `"الحد الأدنى:"` | — |
| [SRC-0F910493E8-L000661](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L661) | 661 | `"- قبول بروتوكولات معلومة فقط (HTTP/HTTPS بحسب الحاجة)، ورفض المخططات غير المطلوبة وصيغ URL الملتبسة وuserinfo غير اللازم والمنافذ غير المعتمدة."` | — |
| [SRC-0F910493E8-L000662](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L662) | 662 | `"- فحص DNS والتحقق من كل عنوان IPv4 وIPv6 الناتج؛ حظر loopback وprivate وlink-local وmulticast وreserved وmetadata addresses والتمثيلات الملتبسة."` | — |
| [SRC-0F910493E8-L000663](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L663) | 663 | `"- منع DNS rebinding وفرق الوقت بين التحقق والاتصال حيث تسمح المكتبات والبنية بذلك، وربط الاتصال بعنوان جرى التحقق منه أو استخدام شبكة خروج وسيطة موثوقة."` | — |
| [SRC-0F910493E8-L000664](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L664) | 664 | `"- التحقق من الوجهة بعد كل redirect، وتحديد عدد التحويلات؛ لا يكفي فحص الرابط الأول."` | — |
| [SRC-0F910493E8-L000665](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L665) | 665 | `"- عدم اتباع إعدادات proxy غير موثوقة بصمت لتجاوز حدود الشبكة؛ توثق سياسة proxy وتختبر."` | — |
| [SRC-0F910493E8-L000666](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L666) | 666 | `"- ضبط timeout وconnection timeout وread timeout وعمق التحويل وعدد الطلبات والتزامن والحد الأعلى للبيانات بعد فك الضغط."` | — |
| [SRC-0F910493E8-L000667](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L667) | 667 | `"- فرض allowlist للدومينات عندما تكون المهمة معروفة والمجال محدودًا. ولا تعني allowlist المفتوحة لجميع الإنترنت عدم الحاجة إلى فحوص SSRF."` | — |
| [SRC-0F910493E8-L000668](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L668) | 668 | `"- رفض الوصول إلى file:// وlocalhost وخدمات الشبكة الداخلية وقواعد البيانات وmetadata الخاصة بالاستضافة."` | — |
| [SRC-0F910493E8-L000669](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L669) | 669 | `"- التحقق من نوع المحتوى والحجم والترميز؛ وعدم فك ملفات مضغوطة أو مستندات معقدة بلا حدود موارد."` | — |
| [SRC-0F910493E8-L000670](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L670) | 670 | `"- لا ترسل Cookies أو جلسات المستخدم أو رؤوسًا حساسة لمصدر خارجي."` | — |
| [SRC-0F910493E8-L000671](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L671) | 671 | `"- تعامل مع كل محتوى جالب على أنه غير موثوق، ولا تنفذ HTML أو JavaScript أو ماكروهات أو أوامر مضمنة."` | — |
| [SRC-0F910493E8-L000672](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L672) | 672 | `"- اختبارات SSRF تجرى في بيئة محلية/اختبارية مضبوطة، تشمل redirect إلى عنوان محظور وIPv6 وDNS متغيرًا وحدود الحجم والمهلة؛ لا تجرّب على أهداف خارجية غير مصرح بها."` | — |
| [SRC-0F910493E8-L000673](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L673) | 673 | `""` | — |
| [SRC-0F910493E8-L000674](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L674) | 674 | `"إذا لم يمكن ضمان فحص عنوان الاتصال الفعلي بسبب حدود مكتبة أو استضافة، سجّل ذلك بوضوح، وقلّص وجهات الجلب أو عطّل الجلب المباشر عند الحاجة."` | — |
| [SRC-0F910493E8-L000675](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L675) | 675 | `""` | — |
| [SRC-0F910493E8-L000676](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L676) | 676 | `"## 17.9 حماية API والويب والمتصفح"` | — |
| [SRC-0F910493E8-L000677](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L677) | 677 | `""` | — |
| [SRC-0F910493E8-L000678](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L678) | 678 | `"- تحقق صارم من مدخلات API وأنواعها وأطوالها وأحجام الأجسام والحقول غير المتوقعة؛ لا تعتمد على التحقق في الواجهة فقط."` | — |
| [SRC-0F910493E8-L000679](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L679) | 679 | `"- طبّق حدود معدل وحصص على المستخدم والمسار المكلف عند الإمكان، واعزل تشخيصات الإدارة عن المسارات العامة."` | — |
| [SRC-0F910493E8-L000680](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L680) | 680 | `"- اضبط CORS بأقل مجموعة origins مطلوبة، ولا تعتبره بديلاً عن المصادقة."` | — |
| [SRC-0F910493E8-L000681](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L681) | 681 | `"- استخدم استعلامات SQL محددة المعاملات، وتحقق من قيم المسار وأسماء الملفات؛ لا تسمح بتجاوز المسارات (path traversal)."` | — |
| [SRC-0F910493E8-L000682](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L682) | 682 | `"- امنع XSS من خلال الترميز حسب سياق HTML/attribute/URL، وتنقية Markdown/HTML بروتين موثوق، ومنع HTML الخام غير اللازم."` | — |
| [SRC-0F910493E8-L000683](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L683) | 683 | `"- تحقق من الروابط المعروضة وقيّد المخططات الخطرة مثل javascript: وdata: وفق الاستخدام؛ لا تعرض روابط مولدة على أنها مصادر موثوقة."` | — |
| [SRC-0F910493E8-L000684](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L684) | 684 | `"- راجع CSP وHSTS وX-Content-Type-Options وReferrer-Policy وframe-ancestors أو X-Frame-Options، بحسب ما تسمح به الواجهة والاستضافة. لا تدّعِ وجود هذه الرؤوس قبل فحص استجابة النشر الفعلية."` | — |
| [SRC-0F910493E8-L000685](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L685) | 685 | `"- استخدم HTTPS للاتصالات الخارجية وعند تقديم خدمة عامة؛ ويُتحقق من أن proxy أو منصة الاستضافة تفرضه بصورة صحيحة."` | — |
| [SRC-0F910493E8-L000686](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L686) | 686 | `"- راجع CSRF إذا استُخدمت مصادقة cookies؛ لا تعتمد على CORS وحده."` | — |
| [SRC-0F910493E8-L000687](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L687) | 687 | `"- لا تكشف رسائل الخطأ العامة تفاصيل stack trace أو المسارات الداخلية أو أسماء الأسرار أو استعلامات حساسة."` | — |
| [SRC-0F910493E8-L000688](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L688) | 688 | `"- استخدم مصادقة وتفويضًا لعمليات الإدارة والتشخيص والتصدير، وحدودًا للأحجام والتنزيلات."` | — |
| [SRC-0F910493E8-L000689](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L689) | 689 | `"- اختبر XSS عبر مخرجات النموذج والمصادر، وتجاوز الصلاحيات الأفقية، وطلبات API المزورة، وحدود الطلبات."` | — |
| [SRC-0F910493E8-L000690](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L690) | 690 | `""` | — |
| [SRC-0F910493E8-L000691](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L691) | 691 | `"## 17.10 الأسرار وخصوصية مزودي النماذج"` | — |
| [SRC-0F910493E8-L000692](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L692) | 692 | `""` | — |
| [SRC-0F910493E8-L000693](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L693) | 693 | `"- تخزن أسرار الإنتاج في مخزن أسرار المنصة أو إعداد بيئة محمي؛ لا في Git أو الكود أو المتصفح أو سجلات الطلب."` | — |
| [SRC-0F910493E8-L000694](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L694) | 694 | ``"- استخدم `.env.example` بقيم وهمية فقط، وافحص ملفات التغيير وتاريخ المستودع على الأسرار عند الاشتباه."`` | — |
| [SRC-0F910493E8-L000695](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L695) | 695 | `"- عند الاشتباه بتسرب مفتاح، يُلغى أو يدوّر أولًا، ثم يُبحث عن نطاق التعرض؛ حذف القيمة من آخر commit لا يلغي السر المسرب."` | — |
| [SRC-0F910493E8-L000696](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L696) | 696 | `"- لا ترسل مفاتيح الخدمات أو رموز الدخول إلى النموذج أو ملف تعريف أو محتوى مسترجع."` | — |
| [SRC-0F910493E8-L000697](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L697) | 697 | `"- توثّق بيانات كل مرحلة تُرسل إلى مزود خارجي: السؤال، والسياق، والمقتطفات، والتشخيصات، والنموذج البديل."` | — |
| [SRC-0F910493E8-L000698](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L698) | 698 | `"- لا يُرسل تصنيف بيانات لا يسمح به مزود النموذج أو الإعداد أو موافقة المستخدم."` | — |
| [SRC-0F910493E8-L000699](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L699) | 699 | `"- افحص خصوصية موفري النماذج المجانية وسياسات الاحتفاظ والاستخدام والتدريب وشروط الخدمة قبل الاعتماد على معالجة بيانات حساسة؛ لا تفترض أن المجانية تعني الخصوصية."` | — |
| [SRC-0F910493E8-L000700](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L700) | 700 | `"- يكون fallback إلى مزود آخر محدودًا بمزودين معتمدين ونطاق بيانات مسموح؛ لا ينقل بيانات أكثر حساسية أو يغير سياسة الخصوصية تلقائيًا."` | — |
| [SRC-0F910493E8-L000701](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L701) | 701 | `"- إذا تعذر تأكيد أن البيانات مسموح بإرسالها إلى مزود خارجي، قللها أو احجبها أو اطلب موافقة أو عطّل ذلك المسار."` | — |
| [SRC-0F910493E8-L000702](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L702) | 702 | `"- لا تسجل محتوى المستخدم أو البيانات الشخصية كاملة افتراضيًا؛ سجّل معرفات حالة وملخصات منقحة حيث تكفي."` | — |
| [SRC-0F910493E8-L000703](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L703) | 703 | `"- حدد سياسة احتفاظ وحذف واضحة وملكية وصلاحيات للوصول إلى السجلات والنسخ الاحتياطية."` | — |
| [SRC-0F910493E8-L000704](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L704) | 704 | `""` | — |
| [SRC-0F910493E8-L000705](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L705) | 705 | `"## 17.11 الذاكرة، العزل، التزامن، وتسميم البيانات"` | — |
| [SRC-0F910493E8-L000706](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L706) | 706 | `""` | — |
| [SRC-0F910493E8-L000707](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L707) | 707 | `"- لا تُشارك كائنات mutable خاصة بطلب واحد بين الطلبات المتزامنة دون تزامن وعزل مثبتين."` | — |
| [SRC-0F910493E8-L000708](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L708) | 708 | `"- لكل طلب معرف وسياق وميزانية وإلغاء خاص به. تُمرر الحالة صراحة بدل الاعتماد على متغيرات عامة مشتركة."` | — |
| [SRC-0F910493E8-L000709](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L709) | 709 | `"- تتضمن مفاتيح الذاكرة والتخزين المؤقت نطاق المستخدم/الجلسة/المهمة عند انطباقه."` | — |
| [SRC-0F910493E8-L000710](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L710) | 710 | `"- لا تسمح للطلب بتقديم سجل محادثة مزور يمنح نفسه دور system أو صلاحية داخلية."` | — |
| [SRC-0F910493E8-L000711](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L711) | 711 | `"- كل ذاكرة مسترجعة بيانات غير موثوقة حتى لو كانت محفوظة من تشغيل سابق؛ تحمي من poisoning والتلوث بين السياقات."` | — |
| [SRC-0F910493E8-L000712](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L712) | 712 | `"- لا تحفظ إلا ما تحدده سياسة الذاكرة؛ وتوثق مدة الاحتفاظ والحذف وموافقة المستخدم عند الحاجة."` | — |
| [SRC-0F910493E8-L000713](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L713) | 713 | `"- اختبر طلبين متزامنين بمستخدمين أو سياقين مختلفين، والإلغاء أثناء تنفيذ أداة، وإعادة استخدام worker بعد الفشل، واستعادة مخزن البيانات."` | — |
| [SRC-0F910493E8-L000714](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L714) | 714 | `"- إذا لم يكن تعدد المستخدمين مدعومًا أو مختبرًا، فوثق ذلك ولا تعرض الخدمة كمنصة متعددة المستأجرين مؤكدة."` | — |
| [SRC-0F910493E8-L000715](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L715) | 715 | `""` | — |
| [SRC-0F910493E8-L000716](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L716) | 716 | `"## 17.12 سلسلة توريد البرمجيات وأمن التطوير وCI/CD"` | — |
| [SRC-0F910493E8-L000717](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L717) | 717 | `""` | — |
| [SRC-0F910493E8-L000718](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L718) | 718 | `"كل تغيير يمر بممارسات تطوير آمن متناسبة مع الخطر:"` | — |
| [SRC-0F910493E8-L000719](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L719) | 719 | `"- مراجعة diff ومصادر الاعتماديات قبل إضافتها."` | — |
| [SRC-0F910493E8-L000720](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L720) | 720 | `"- تثبيت الإصدارات في lockfiles حيث تدعم منظومة المشروع ذلك."` | — |
| [SRC-0F910493E8-L000721](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L721) | 721 | `"- تحديث الاعتماديات الأمنية وفق اختبار التوافق."` | — |
| [SRC-0F910493E8-L000722](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L722) | 722 | `"- فحص الأسرار والتبعيات المعرضة لثغرات معروفة."` | — |
| [SRC-0F910493E8-L000723](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L723) | 723 | `"- استخدام SAST وlint وفحوص نوعية أو تحليل ثابت عندما تكون مناسبة، مع مراجعة نتائجها بدل اعتبارها ضمانًا كاملًا."` | — |
| [SRC-0F910493E8-L000724](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L724) | 724 | `"- بناء اختبارات لاكتشاف أخطاء authorization وinjection وpath traversal وSSRF والتزامن بحسب تدفق التغيير."` | — |
| [SRC-0F910493E8-L000725](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L725) | 725 | `"- استخدام صلاحيات CI قليلة. يجب ألا تحصل خطوات بناء طلبات غير موثوقة على أسرار نشر أو صلاحيات كتابة غير لازمة."` | — |
| [SRC-0F910493E8-L000726](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L726) | 726 | `"- تثبيت GitHub Actions أو غيرها إلى commit SHA عند الحاجة الأمنية والعملية بدل الاعتماد على وسوم متحركة فقط، ومراجعة المصدر والصلاحيات."` | — |
| [SRC-0F910493E8-L000727](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L727) | 727 | `"- عدم تنفيذ سكربت من PR غير موثوق مع أسرار الإنتاج أو رموز امتياز."` | — |
| [SRC-0F910493E8-L000728](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L728) | 728 | `"- ربط الاختبار والإصدار والartifact بالـ commit الذي أنتجه، وحفظ سجل قابل للتحقق."` | — |
| [SRC-0F910493E8-L000729](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L729) | 729 | `"- استخدام SBOM وتوقيع artifacts/provenance عندما تسمح البيئة وتبرر المخاطر ذلك."` | — |
| [SRC-0F910493E8-L000730](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L730) | 730 | `"- فصل بيئة الاختبار عن أسرار الإنتاج والبيانات الحقيقية."` | — |
| [SRC-0F910493E8-L000731](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L731) | 731 | `"- لا يُدمج PR أو ينشر الإنتاج إلا بتفويض المدير البشري وفق سياسة المشروع."` | — |
| [SRC-0F910493E8-L000732](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L732) | 732 | `""` | — |
| [SRC-0F910493E8-L000733](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L733) | 733 | `"لا يعني عدم توافر أداة فحص مدفوعة تجاهل الخطر؛ يمكن استخدام فحوص مجانية أو يدوية مناسبة، مع بيان نطاقها وحدودها."` | — |
| [SRC-0F910493E8-L000734](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L734) | 734 | `""` | — |
| [SRC-0F910493E8-L000735](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L735) | 735 | `"## 17.13 عزل الكود المولد — عند دراسة هذه القدرة مستقبلًا فقط"` | — |
| [SRC-0F910493E8-L000736](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L736) | 736 | `""` | — |
| [SRC-0F910493E8-L000737](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L737) | 737 | `"**الوضع الافتراضي: لا يوجد تشغيل لكود تنفيذي يولده النموذج.**"` | — |
| [SRC-0F910493E8-L000738](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L738) | 738 | `""` | — |
| [SRC-0F910493E8-L000739](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L739) | 739 | `"إذا وافق المدير البشري مستقبلًا على تجربة محددة لتوليد الكود، فلا تعمل على خادم التطبيق الأساسي مباشرة. يجب أن يستخدم التنفيذ بيئة عزل مناسبة للخطر (مثل VM أو microVM أو sandbox مكافئ مثبت الحدود)، وبالحد الأدنى:"` | — |
| [SRC-0F910493E8-L000740](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L740) | 740 | `"- مستخدم غير متميز؛ لا root ولا امتيازات إدارية."` | — |
| [SRC-0F910493E8-L000741](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L741) | 741 | `"- نظام ملفات مؤقت ومحدود، وقراءة فقط للصورة الأساسية، دون mount لأسرار المضيف أو ملفات المستخدم غير اللازمة."` | — |
| [SRC-0F910493E8-L000742](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L742) | 742 | `"- شبكة مغلقة افتراضيًا؛ أي خروج شبكي عبر proxy/allowlist وموافقة واضحة."` | — |
| [SRC-0F910493E8-L000743](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L743) | 743 | `"- عدم تمرير مفاتيح النموذج أو استضافة التطبيق إلى العملية المولدة."` | — |
| [SRC-0F910493E8-L000744](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L744) | 744 | `"- تحديد CPU والذاكرة وحجم الملف والمدة وعدد العمليات والتزامن."` | — |
| [SRC-0F910493E8-L000745](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L745) | 745 | `"- عزل namespaces/cgroups/seccomp/AppArmor أو ضوابط مكافئة بحسب النظام، واختبار فعاليتها لا الاكتفاء بأسمائها."` | — |
| [SRC-0F910493E8-L000746](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L746) | 746 | `"- تثبيت الاعتماديات المسموحة وعدم تثبيت أي package عشوائي من شبكة عامة في مسار موثوق."` | — |
| [SRC-0F910493E8-L000747](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L747) | 747 | `"- عدم السماح بالوصول إلى Docker socket أو أجهزة المضيف أو ملفات الأسرار."` | — |
| [SRC-0F910493E8-L000748](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L748) | 748 | `"- بيئة مؤقتة تنظف بعد التنفيذ، مع حفظ أثر الاختبار المنقح فقط."` | — |
| [SRC-0F910493E8-L000749](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L749) | 749 | `"- اختبارات هروب وتصعيد صلاحيات وقراءة ملفات واتصال غير مصرح به واستنزاف موارد."` | — |
| [SRC-0F910493E8-L000750](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L750) | 750 | `"- اختبار مستقل عن اختبارات الكود التي أنشأها النموذج."` | — |
| [SRC-0F910493E8-L000751](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L751) | 751 | `"- مراجعة بشرية وموافقة نشر وتوقيع/تحديد إصدار وخطة rollback."` | — |
| [SRC-0F910493E8-L000752](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L752) | 752 | `""` | — |
| [SRC-0F910493E8-L000753](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L753) | 753 | `"إذا تعذّر إثبات حد العزل في منصة مجانية أو بيئة الهاتف/Termux، لا نفعّل تشغيل الكود المولد هناك. لا يغير وصف البيئة بأنها sandbox هذا الحكم."` | — |
| [SRC-0F910493E8-L000754](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L754) | 754 | `""` | — |
| [SRC-0F910493E8-L000755](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L755) | 755 | `"## 17.14 حدود الموارد ومقاومة الإساءة"` | — |
| [SRC-0F910493E8-L000756](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L756) | 756 | `""` | — |
| [SRC-0F910493E8-L000757](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L757) | 757 | `"- كل طلب له deadline وميزانية للوقت والخطوات واستدعاءات الأدوات والنماذج والصفحات والحجم."` | — |
| [SRC-0F910493E8-L000758](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L758) | 758 | `"- لكل موصل حدود مستقلة للمهلة والتزامن وعدد النتائج وحجم الاستجابة."` | — |
| [SRC-0F910493E8-L000759](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L759) | 759 | `"- إعادة المحاولة محدودة، مع منع تكرار الأثر الخارجي وتطبيق idempotency عندما يلزم."` | — |
| [SRC-0F910493E8-L000760](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L760) | 760 | `"- حدود المعدل تراعي هوية المستخدم والمسار المكلف؛ لا تعتمد على header غير موثوق أو عنوان IP يمكن تزويره عند وجود proxy."` | — |
| [SRC-0F910493E8-L000761](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L761) | 761 | `"- تستخدم semaphores/backpressure أو رفض مؤقت عند بلوغ حد التزامن."` | — |
| [SRC-0F910493E8-L000762](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L762) | 762 | `"- عند تعطل المزود، لا تستمر حلقة مفتوحة ولا يتحول الفشل إلى نجاح ظاهري."` | — |
| [SRC-0F910493E8-L000763](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L763) | 763 | `"- إذا وجدت APIs مدفوعة، تستخدم حدود إنفاق/حصص وتنبيهات وقاطع تعطيل حيث تسمح الخدمة؛ الميزانية الداخلية لكل طلب لا تثبت وحدها وجود سقف مالي شامل."` | — |
| [SRC-0F910493E8-L000764](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L764) | 764 | `"- اختبر استنفاد الميزانية والانتهاء أثناء الاتصال والفشل الجزئي وإطلاق طلبات متزامنة. لا تُدَّعى قدرة على الإلغاء الفوري إذا كانت المكتبة تنهي الاتصال بتأخير تعاوني."` | — |
| [SRC-0F910493E8-L000765](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L765) | 765 | `""` | — |
| [SRC-0F910493E8-L000766](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L766) | 766 | `"## 17.15 السجلات، المراقبة، كشف الحوادث والتعافي"` | — |
| [SRC-0F910493E8-L000767](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L767) | 767 | `""` | — |
| [SRC-0F910493E8-L000768](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L768) | 768 | `"- سجل من قام بالفعل، وما القدرة التي طُلبت، وقرار السياسة، وحالة الأداة، ومعرف المهمة، ونتيجة مختصرة منقحة."` | — |
| [SRC-0F910493E8-L000769](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L769) | 769 | `"- لا تسجل API keys أو cookies أو Authorization headers أو أسرار النموذج أو بيانات خاصة لا حاجة إليها."` | — |
| [SRC-0F910493E8-L000770](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L770) | 770 | `"- قيد الوصول إلى السجلات، وحدد مدة الاحتفاظ والحذف ومراجعة الوصول."` | — |
| [SRC-0F910493E8-L000771](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L771) | 771 | `"- افصل خطأ التطبيق العادي عن الحادث الأمني وعن فشل الموفر."` | — |
| [SRC-0F910493E8-L000772](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L772) | 772 | `"- وفر طريقة لإيقاف أداة أو موصل أو تكوين خطير بسرعة (kill switch) متى أمكن."` | — |
| [SRC-0F910493E8-L000773](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L773) | 773 | `"- وثّق إجراءً مختصرًا للتعامل مع: سر مسرب، وصول غير مصرح، ثغرة حرجة، تسريب بيانات، إساءة استهلاك، وخلل في سلسلة التوريد."` | — |
| [SRC-0F910493E8-L000774](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L774) | 774 | `"- يتضمن الإجراء الاحتواء، وإلغاء الأسرار، وحفظ أدلة مناسبة، وتقييم نطاق الأثر، وإصلاحًا واختبارًا، ومراجعة سبب جذري، واختبار منع تكرار."` | — |
| [SRC-0F910493E8-L000775](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L775) | 775 | `"- اختبر النسخ الاحتياطي والاستعادة للبيانات المهمة. وجود ملف backup غير كافٍ."` | — |
| [SRC-0F910493E8-L000776](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L776) | 776 | `"- يحدّث سجل المتطلبات والمخاطر بعد الحادث، ولا تُخفى القيود التي لم تُعالج."` | — |
| [SRC-0F910493E8-L000777](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L777) | 777 | `""` | — |
| [SRC-0F910493E8-L000778](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L778) | 778 | `"## 17.16 فحوص الأمان الإلزامية قبل اعتماد تغيير مؤثر"` | — |
| [SRC-0F910493E8-L000779](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L779) | 779 | `""` | — |
| [SRC-0F910493E8-L000780](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L780) | 780 | `"لا يلزم تشغيل كل فحص على كل تعديل توثيقي؛ لكن أي تغيير يؤثر في مسار أمني يجب أن يرتبط بالاختبارات المنطبقة، على الأقل من المجموعة التالية:"` | — |
| [SRC-0F910493E8-L000781](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L781) | 781 | `"- **AuthN/AuthZ:** رفض وصول مجهول أو غير مالك للمورد؛ اختبار BOLA/IDOR إن وجدت موارد خاصة."` | — |
| [SRC-0F910493E8-L000782](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L782) | 782 | `"- **Input validation:** الأنواع والأطوال والحقول المجهولة والحدود والمدخلات المشوهة."` | — |
| [SRC-0F910493E8-L000783](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L783) | 783 | `"- **SSRF/network:** loopback/private/IPv6/metadata/redirect/DNS changes/oversized responses/timeouts."` | — |
| [SRC-0F910493E8-L000784](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L784) | 784 | `"- **Prompt injection:** محتوى خبيث داخل صفحات أو مرفقات أو ذاكرة، مع التحقق من عدم نشوء استدعاء أداة غير مسموح."` | — |
| [SRC-0F910493E8-L000785](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L785) | 785 | `"- **Tool permissions:** أداة غير مسجلة، صلاحية مرفوضة، تجاوز budget، وسياسة تتطلب تأكيدًا بشريًا."` | — |
| [SRC-0F910493E8-L000786](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L786) | 786 | `"- **XSS/output safety:** HTML/Markdown/URL مسترجع أو مولد، وروابط ذات مخططات خطرة."` | — |
| [SRC-0F910493E8-L000787](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L787) | 787 | `"- **Secrets/privacy:** عدم تسرب الأسرار أو السياق الحساس إلى output أو logs أو PR أو مزود غير معتمد."` | — |
| [SRC-0F910493E8-L000788](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L788) | 788 | `"- **Concurrency/isolation:** طلبات متزامنة وسياقات مستخدمين مختلفين وإلغاء أو timeout."` | — |
| [SRC-0F910493E8-L000789](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L789) | 789 | `"- **Abuse/resource limits:** عدد الطلبات والخطوات والصفحات والمحاولات واستنفاد الحصة."` | — |
| [SRC-0F910493E8-L000790](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L790) | 790 | `"- **Supply chain/CI:** صلاحيات workflow، سلوك PR غير موثوق، الاعتماديات، ووجود الأسرار في التغيير."` | — |
| [SRC-0F910493E8-L000791](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L791) | 791 | `"- **Data safety:** ملكية السجل، التصدير، الترحيل، النسخ الاحتياطي والحذف بحسب المسار."` | — |
| [SRC-0F910493E8-L000792](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L792) | 792 | `"- **Regression:** كل سلوك سابق متأثر بالتغيير مع حالات النجاح والفشل."` | — |
| [SRC-0F910493E8-L000793](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L793) | 793 | `""` | — |
| [SRC-0F910493E8-L000794](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L794) | 794 | `"تُحفظ النتيجة الفعلية وبيئة التشغيل وإصدار المصدر لكل ادعاء. ويجب أن تميز التقارير بين PASS وFAIL وNOT_RUN وNOT_APPLICABLE مع سبب. لا يُعامل NOT_RUN أو اختبار mock على أنه إثبات لعمل حي."` | — |
| [SRC-0F910493E8-L000795](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L795) | 795 | `""` | — |
| [SRC-0F910493E8-L000796](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L796) | 796 | `"## 17.17 بوابات إطلاق أمنية (Security Release Gates)"` | — |
| [SRC-0F910493E8-L000797](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L797) | 797 | `""` | — |
| [SRC-0F910493E8-L000798](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L798) | 798 | `"**لا يجوز إطلاق أو تمكين مسار ذي أثر بناء على توثيق فقط.** تحدد درجة الصرامة بحسب الخطر:"` | — |
| [SRC-0F910493E8-L000799](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L799) | 799 | `""` | — |
| [SRC-0F910493E8-L000800](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L800) | 800 | `"### البوابة S0 — سلامة الأساس"` | — |
| [SRC-0F910493E8-L000801](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L801) | 801 | `"- لا أسرار معروفة مكشوفة في التغيير."` | — |
| [SRC-0F910493E8-L000802](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L802) | 802 | `"- المصادقة والتفويض مفعّلان على المسارات التي تتطلبهما."` | — |
| [SRC-0F910493E8-L000803](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L803) | 803 | `"- لا يوجد تجاوز معروف للصلاحيات في المسار المتأثر."` | — |
| [SRC-0F910493E8-L000804](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L804) | 804 | `"- مدخلات وموارد الطلب محدودة."` | — |
| [SRC-0F910493E8-L000805](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L805) | 805 | `"- الاختبارات الأساسية واختبارات الانحدار المنطبقة تعمل."` | — |
| [SRC-0F910493E8-L000806](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L806) | 806 | `""` | — |
| [SRC-0F910493E8-L000807](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L807) | 807 | `"### البوابة S1 — أدوات وشبكة وبيانات"` | — |
| [SRC-0F910493E8-L000808](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L808) | 808 | `"- اختبارات الرفض والصلاحيات وSSRF والمهل والحجم موجودة ومجتازة بحسب التغيير."` | — |
| [SRC-0F910493E8-L000809](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L809) | 809 | `"- المحتوى غير الموثوق لا يصبح تعليمات تنفيذية أو HTML نشطًا."` | — |
| [SRC-0F910493E8-L000810](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L810) | 810 | `"- الأسرار والبيانات لا تتسرب إلى سجلات أو مزود غير معتمد."` | — |
| [SRC-0F910493E8-L000811](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L811) | 811 | `"- عزل السياق مثبت للمسارات التي تتعامل مع طلبات متزامنة أو بيانات مختلفة."` | — |
| [SRC-0F910493E8-L000812](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L812) | 812 | `""` | — |
| [SRC-0F910493E8-L000813](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L813) | 813 | `"### البوابة S2 — وكيل جديد أو صلاحية جديدة"` | — |
| [SRC-0F910493E8-L000814](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L814) | 814 | `"- نموذج تهديد مختصر ومراجعة مخاطر."` | — |
| [SRC-0F910493E8-L000815](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L815) | 815 | `"- تعريف وصلاحيات ومعايير فشل واضحة."` | — |
| [SRC-0F910493E8-L000816](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L816) | 816 | `"- اختبارات وظيفية وسلبية وجودة ملائمة للمهمة."` | — |
| [SRC-0F910493E8-L000817](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L817) | 817 | `"- سجل إصدار واعتماد وتعطيل/تراجع."` | — |
| [SRC-0F910493E8-L000818](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L818) | 818 | `"- موافقة بشرية حسب الأثر."` | — |
| [SRC-0F910493E8-L000819](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L819) | 819 | `""` | — |
| [SRC-0F910493E8-L000820](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L820) | 820 | `"### البوابة S3 — تنفيذ كود مولد أو فعل خارجي عالي الأثر"` | — |
| [SRC-0F910493E8-L000821](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L821) | 821 | `"- قرار معماري مستقل ومبرر."` | — |
| [SRC-0F910493E8-L000822](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L822) | 822 | `"- عزل اختُبرت حدوده في بيئة مطابقة لمسار التشغيل."` | — |
| [SRC-0F910493E8-L000823](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L823) | 823 | `"- اختبار هروب وصلاحيات وموارد وسلسلة توريد."` | — |
| [SRC-0F910493E8-L000824](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L824) | 824 | `"- فصل أسرار الإنتاج عن بيئة الاختبار."` | — |
| [SRC-0F910493E8-L000825](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L825) | 825 | `"- مراجعة أمنية وموافقة بشرية وخطة استجابة وتراجع."` | — |
| [SRC-0F910493E8-L000826](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L826) | 826 | `"- لا يُفعّل إذا تعذر إثبات أحد المتطلبات الحرجة."` | — |
| [SRC-0F910493E8-L000827](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L827) | 827 | `""` | — |
| [SRC-0F910493E8-L000828](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L828) | 828 | `"إذا كان هناك خطر حرج معروف أو مسار يسمح بتسرب سر أو تجاوز صلاحيات أو تنفيذ كود غير موثوق خارج العزل، فالقرار الافتراضي هو تعطيل المسار المتأثر حتى المعالجة، مع توثيق السبب. لا يمنع ذلك استمرار التطوير في مسارات أخرى غير معرضة للخطر."` | — |
| [SRC-0F910493E8-L000829](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L829) | 829 | `""` | — |
| [SRC-0F910493E8-L000830](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L830) | 830 | `"## 17.18 الأمن كدورة حياة، لا كقائمة نهائية"` | — |
| [SRC-0F910493E8-L000831](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L831) | 831 | `""` | — |
| [SRC-0F910493E8-L000832](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L832) | 832 | `"تبدأ المراجعة عند تعريف المتطلب، وتستمر خلال التصميم والتنفيذ والاختبار والنشر وما بعد النشر. لكل تغيير جوهري:"` | — |
| [SRC-0F910493E8-L000833](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L833) | 833 | `"1. الحاجة والبيانات والأصول."` | — |
| [SRC-0F910493E8-L000834](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L834) | 834 | `"2. حدود الثقة ونموذج التهديد."` | — |
| [SRC-0F910493E8-L000835](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L835) | 835 | `"3. التصميم وأقل صلاحيات."` | — |
| [SRC-0F910493E8-L000836](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L836) | 836 | `"4. اختبارات الفشل والهجوم المناسبة."` | — |
| [SRC-0F910493E8-L000837](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L837) | 837 | `"5. مراجعة diff والاعتماديات والأسرار."` | — |
| [SRC-0F910493E8-L000838](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L838) | 838 | `"6. نتيجة اختبار موثقة."` | — |
| [SRC-0F910493E8-L000839](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L839) | 839 | `"7. قرار قبول المخاطر من صاحب الصلاحية."` | — |
| [SRC-0F910493E8-L000840](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L840) | 840 | `"8. مراقبة وتراجع عند الحاجة."` | — |
| [SRC-0F910493E8-L000841](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L841) | 841 | `""` | — |
| [SRC-0F910493E8-L000842](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L842) | 842 | `"الأمن المستمر لا يعني إضافة كل أداة أو إطار امتثال متاح. يعني أن كل ضابط يواجه خطرًا معروفًا، وله مالك واختبار وحدود، ويمكن تعطيله أو التراجع عنه عند ظهور خلل، ولا نضيف تعقيدًا لا يستطيع المشروع تشغيله ومراجعته."` | — |
| [SRC-0F910493E8-L000843](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L843) | 843 | `""` | — |
| [SRC-0F910493E8-L000844](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L844) | 844 | `"---"` | — |
| [SRC-0F910493E8-L000845](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L845) | 845 | `""` | — |
| [SRC-0F910493E8-L000846](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L846) | 846 | `"## الخلاصة الحاكمة"` | — |
| [SRC-0F910493E8-L000847](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L847) | 847 | `""` | — |
| [SRC-0F910493E8-L000848](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L848) | 848 | `"**ابنِ قدرات موثوقة قبل أن تبني مصنعًا لإنشاء القدرات.**"` | — |
| [SRC-0F910493E8-L000849](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L849) | 849 | `""` | — |
| [SRC-0F910493E8-L000850](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L850) | 850 | `"نواة Omarai ومسارات البحث والأدوات والأدلة الحالية هي نقطة البداية التي يجب تدقيقها والحفاظ على المفيد منها. تتطور المنظومة بإضافة عقود واضحة ومهارات وسير عمل قابلة للاختبار، ثم مواصفات وتركيب ديناميكي محدود عند الحاجة. يأتي إنشاء الوكلاء بعد ذلك، وتوليد الكود التنفيذي قرار مستقبلي مستقل."` | — |
| [SRC-0F910493E8-L000851](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L851) | 851 | `""` | — |
| [SRC-0F910493E8-L000852](../OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md#L852) | 852 | `"النجاح ليس عدد الوكلاء أو الطبقات، بل قدرة Omarai على أداء مهمة حقيقية، ضمن صلاحيات محددة، بنتيجة يمكن فحصها، مع توضيح صادق لما نجح وما فشل وما لا يزال مجهولًا."` | — |
## وثائق وفهرسة

### FILE-61B24BEFCC — [docs/OMARAI_TEST_EVIDENCE_MATRIX_AR.md](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-61B24BEFCC-L000001](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L1) | 1 | `"# Omarai — مصفوفة أدلة الاختبار: محلي، Mock، حاوية، وتكامل حي"` | — |
| [SRC-61B24BEFCC-L000002](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L2) | 2 | `""` | — |
| [SRC-61B24BEFCC-L000003](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L3) | 3 | `"**معرف الوثيقة:** OMARAI-TEST-EVIDENCE-MATRIX-001  "` | — |
| [SRC-61B24BEFCC-L000004](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L4) | 4 | `"**تاريخ اللقطة:** 2026-10-19  "` | — |
| [SRC-61B24BEFCC-L000005](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L5) | 5 | ``"**نسخة المصدر المرجعية:** `871d2930405d164d3ae4c53f368937a4f5f01a6f`  "`` | — |
| [SRC-61B24BEFCC-L000006](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L6) | 6 | `"**الغرض:** منع الخلط بين وجود الكود ونجاح اختبارات وحداته وبين إثبات الاتصال بخدمة خارجية أو تشغيل نسخة عامة."` | — |
| [SRC-61B24BEFCC-L000007](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L7) | 7 | `""` | — |
| [SRC-61B24BEFCC-L000008](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L8) | 8 | `"## 1. أنواع الدليل"` | — |
| [SRC-61B24BEFCC-L000009](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L9) | 9 | `""` | — |
| [SRC-61B24BEFCC-L000010](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L10) | 10 | `"\| النوع \| ما الذي يثبته؟ \| ما الذي لا يثبته؟ \|"` | — |
| [SRC-61B24BEFCC-L000011](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L11) | 11 | `"\|---\|---\|---\|"` | — |
| [SRC-61B24BEFCC-L000012](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L12) | 12 | `"\| Unit / deterministic \| سلوك دالة/قاعدة محددة في شروط مضبوطة. \| اتصال حي أو تكامل خارجي أو أداء إنتاجي. \|"` | — |
| [SRC-61B24BEFCC-L000013](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L13) | 13 | `"\| Mock / monkeypatch \| تعامل المكون مع استجابة/فشل اصطناعي محدد. \| صلاحية مفاتيح أو توافر موفر حقيقي أو مطابقته للسلوك الفعلي. \|"` | — |
| [SRC-61B24BEFCC-L000014](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L14) | 14 | `"\| Local HTTP integration \| تشغيل Handler/API الفعلي على loopback مع قاعدة اختبار. \| صحة TLS أو CORS عبر مضيف حقيقي أو هوية نشر عامة. \|"` | — |
| [SRC-61B24BEFCC-L000015](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L15) | 15 | `"\| Container smoke on CI \| بناء الحاوية وتشغيلها واختبار مسارات API أساسية محلية ومحمية. \| نشر فعلي أو دوام الملفات أو اتصال كل موفر خارجي. \|"` | — |
| [SRC-61B24BEFCC-L000016](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L16) | 16 | `"\| Live provider diagnostic \| موفر محدد رد في وقت الاختبار من بيئة الاختبار. \| استمرار التوافر أو دقة كل إجابة أو استقلال المصادر. \|"` | — |
| [SRC-61B24BEFCC-L000017](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L17) | 17 | `"\| Hosted acceptance smoke \| مسار مصادق عليه يعمل على عنوان الاستضافة الذي فُحص وقت التشغيل. \| توافر مستمر، حمل إنتاجي، استعادة بيانات، أو امتثال أمني شامل. \|"` | — |
| [SRC-61B24BEFCC-L000018](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L18) | 18 | `"\| Load / restore / red-team \| فقط النطاق المحدد في التقرير ونتائج الاختبار التي نُفذت. \| أي نطاق أو تهديد لم يشمله القياس أو الاختبار. \|"` | — |
| [SRC-61B24BEFCC-L000019](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L19) | 19 | `""` | — |
| [SRC-61B24BEFCC-L000020](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L20) | 20 | `"## 2. تصنيف الموجود في المستودع"` | — |
| [SRC-61B24BEFCC-L000021](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L21) | 21 | `""` | — |
| [SRC-61B24BEFCC-L000022](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L22) | 22 | `"\| المسار \| التصنيف \| الدليل الحالي \| الحالة والحدود \|"` | — |
| [SRC-61B24BEFCC-L000023](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L23) | 23 | `"\|---\|---\|---\|---\|"` | — |
| [SRC-61B24BEFCC-L000024](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L24) | 24 | ``"\| `tests/test_request_budget.py` \| Unit / deterministic \| عدادات الميزانية والحدود والساعة الوهمية، مع اختبارات حدود لكل مورد ورفض المورد المعطل والتزامن في PR #56. \| CI [39223310566](https://github.com/mosabosama2030-oss/omarai/actions/runs/39223310566) نجح على PR #56: Ruff، و249 اختبارًا على Python 3.11 و249 على Python 3.12، وبناء الحاوية وفحص API المحمية. الاختبار محلي ولا يثبت حمل الإنتاج أو hard cancellation. \|"`` | — |
| [SRC-61B24BEFCC-L000025](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L25) | 25 | ``"\| `tests/test_api.py` \| Local HTTP integration + mocks محددة \| Handler حقيقي على loopback وقاعدة SQLite مؤقتة؛ بعض مسارات الوكيل تُعزل بـmonkeypatch. \| يثبت السلوك المحلي المُمثّل فقط؛ لا يثبت عنوان استضافة عام. \|"`` | — |
| [SRC-61B24BEFCC-L000026](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L26) | 26 | ``"\| `tests/test_web_agent.py` \| Unit / mocked provider behavior غالبًا \| تهيئة موفرين ونتائج/failures اصطناعية وفحوص سلوك محلية. \| لا يُعامل كاختبار اتصال حي. يلزم فحص كل اختبار/marker قبل تصنيف كامل الملف آليًا. \|"`` | — |
| [SRC-61B24BEFCC-L000027](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L27) | 27 | ``"\| `tests/test_answer_quality_corpus.py` \| Structural corpus validation \| التحقق من الشكل والمعرفات والفئات ومعايير الحالات. \| وجود 45 حالة في corpus لا يعني أن النموذج أجاب عنها أو اجتازها حيًا. \|"`` | — |
| [SRC-61B24BEFCC-L000028](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L28) | 28 | ``"\| `tests/test_answer_quality_runner.py` \| Runner/schema/status behavior \| اختبارات لحفظ حالات مثل NOT_TESTED وعدم اعتبارها PASS. \| لا يثبت جودة إجابات نموذج لم تُشغّل عليه. \|"`` | — |
| [SRC-61B24BEFCC-L000029](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L29) | 29 | ``"\| `.github/workflows/tests.yml` \| CI + container smoke \| Ruff وPytest على Python 3.11/3.12، وبناء الحاوية واختبار API الأساسي المحمي. \| بنية الحاوية وsmoke المحلي لا يساويان خدمة منشورة. \|"`` | — |
| [SRC-61B24BEFCC-L000030](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L30) | 30 | ``"\| `scripts/hosted_smoke_test.py` \| Live hosted acceptance script \| يستهدف أصل HTTPS معلومًا، ويفحص الصحة ورفض غير المصادق، والتشخيص الحي للبحث والنموذج، ثم سؤالًا عربيًا ومصادر. \| لم يُنفذ في هذه اللقطة؛ قد يستهلك استخدام موفر النموذج/البحث. \|"`` | — |
| [SRC-61B24BEFCC-L000031](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L31) | 31 | ``"\| `.github/workflows/hosted-smoke.yml` \| Manual live workflow \| `workflow_dispatch`، ويستخدم `OMARAI_BASE_URL` و`OMARAI_ACCESS_TOKEN` كأسرار مضبوطة إداريًا، لا URL حرًا من مشغل workflow. \| لا يُشغّل دون عنوان استضافة معتمد وموافقة على الاستخدام/التكلفة. \|"`` | — |
| [SRC-61B24BEFCC-L000032](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L32) | 32 | `""` | — |
| [SRC-61B24BEFCC-L000033](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L33) | 33 | `"## 3. أمثلة تشغيل CI الحديثة وحدود الاستدلال"` | — |
| [SRC-61B24BEFCC-L000034](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L34) | 34 | `""` | — |
| [SRC-61B24BEFCC-L000035](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L35) | 35 | `"هذه نتائج فعلية مرتبطة برؤوس PR محددة. تختلف بين الفروع، ولا تثبت تشغيل خدمة عامة أو اتصالًا حيًا بمزود خارجي. الحالات أدناه تعكس حالة PRs حتى لقطة 2026-10-19."` | — |
| [SRC-61B24BEFCC-L000036](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L36) | 36 | `""` | — |
| [SRC-61B24BEFCC-L000037](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L37) | 37 | `"\| PR / run \| HEAD \| النتائج ونطاق الدليل \|"` | — |
| [SRC-61B24BEFCC-L000038](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L38) | 38 | `"\|---\|---\|---\|"` | — |
| [SRC-61B24BEFCC-L000039](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L39) | 39 | ``"\| [PR #48 — run 39215710124](https://github.com/mosabosama2030-oss/omarai/actions/runs/39215710124) — **مدمج** \| `3e2faba92f20d87db002ba3a4fe3e8ab7165a1f0` \| Ruff؛ 238 اختبارًا على كل من Python 3.11 و3.12؛ بناء الحاوية وفحص API المحمية. دُمج الإصلاح لاحقًا في `main` عند `871d2930405d164d3ae4c53f368937a4f5f01a6f`. يثبت حالات حد جسم الطلب والمهلة والـslow-trickle التي اختُبرت، لا كل صور Slowloris. \|"`` | — |
| [SRC-61B24BEFCC-L000040](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L40) | 40 | ``"\| [PR #58 — run 39224536955](https://github.com/mosabosama2030-oss/omarai/actions/runs/39224536955) — **مفتوح وغير مدمج** \| `59027f44388730d34c7bd7164450abdba2f9fd0a` \| Ruff؛ 244 اختبارًا على كل من Python 3.11 و3.12؛ بناء الحاوية وفحص API المحمية. يثبت اختبارات أداة SQLite المحلية على فرع PR الحالي، لا الاستعادة على مضيف الاستضافة. PR #50 أغلق دون دمج لأنه أقدم من `main`. \|"`` | — |
| [SRC-61B24BEFCC-L000041](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L41) | 41 | ``"\| [PR #51 — run 39223782361](https://github.com/mosabosama2030-oss/omarai/actions/runs/39223782361) — **مغلق دون دمج؛ استُبدل بـPR #57** \| `f0af91c06bffdddcc3a25184754969e86d9e7f86` \| Ruff؛ 249 اختبارًا على كل من Python 3.11 و3.12؛ بناء الحاوية وفحص API المحمية. أدلة توثيقية فقط؛ لا تثبت قبولًا حيًا. \|"`` | — |
| [SRC-61B24BEFCC-L000042](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L42) | 42 | ``"\| [PR #54 — run 39221649040](https://github.com/mosabosama2030-oss/omarai/actions/runs/39221649040) — **مفتوح وغير مدمج** \| `c602de0d039283119236807b075953b4bcf6e89a` \| Ruff؛ 249 اختبارًا على كل من Python 3.11 و3.12؛ بناء الحاوية وفحص API المحمية. الاختبارات الجديدة تستخدم DNS محاكى لتغطية فئات IPv4/IPv6 غير العامة؛ ليست اختبار شبكة حيًا أو شهادة SSRF شاملة. \|"`` | — |
| [SRC-61B24BEFCC-L000043](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L43) | 43 | ``"\| [PR #55 — run 39224020934](https://github.com/mosabosama2030-oss/omarai/actions/runs/39224020934) — **مفتوح وغير مدمج** \| `4604a83d760b7fe913e1a75cdec04a102c33b0d6` \| Ruff؛ 239 اختبارًا على كل من Python 3.11 و3.12؛ بناء الحاوية وفحص API المحمية. يشمل الاختبار التأكد من إغلاق الطلب البطيء قبل إصدار استجابة؛ لا يثبت النشر ولا كل أنواع DoS. \|"`` | — |
| [SRC-61B24BEFCC-L000044](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L44) | 44 | ``"\| [PR #56 — run 39223310566](https://github.com/mosabosama2030-oss/omarai/actions/runs/39223310566) — **مفتوح وغير مدمج** \| `0ca1b14aa1dd63bdc48a8ca73f698f7f6bc83416` \| Ruff؛ 249 اختبارًا على كل من Python 3.11 و3.12؛ بناء الحاوية وفحص API المحمية. يختبر قيود الموارد ورفض المورد المعطل والحجوزات المتزامنة وتحرير semaphore محليًا. \|"`` | — |
| [SRC-61B24BEFCC-L000045](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L45) | 45 | ``"\| [PR #59 — run 39225038734](https://github.com/mosabosama2030-oss/omarai/actions/runs/39225038734) — **مفتوح وغير مدمج** \| `2b8c3de983f09ea1a7c4ca73d4c1a09a54ab987a` \| Pinning لـ`actions/checkout` و`actions/setup-python` على SHA كاملة؛ Ruff؛ 238 اختبارًا على كل من Python 3.11 و3.12؛ بناء الحاوية وفحص API المحمية. لا يشغّل هذا workflow اختبار الاستضافة الحي. \|"`` | — |
| [SRC-61B24BEFCC-L000046](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L46) | 46 | `""` | — |
| [SRC-61B24BEFCC-L000047](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L47) | 47 | ``"أُغلق PR #49 وPR #52 دون دمج بعد أن استُبدل مسار اختبارات الميزانية بـPR #56 المبني على `main` الأحدث. لا تستخدم نتائج CI من الفروع القديمة على أنها تحقق لرؤوس PR أحدث، أو دليلًا على قدرات موجودة في `main` قبل دمجها."`` | — |
| [SRC-61B24BEFCC-L000048](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L48) | 48 | `""` | — |
| [SRC-61B24BEFCC-L000049](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L49) | 49 | `"**نطاق الأرقام:** أعداد Pytest أعلاه مأخوذة من سجلات وظائف CI الفعلية. لا تعني زيادة عدد الاختبارات تحسنًا أمنيًا بحد ذاتها، ولا تعني هذه الاختبارات اتصالًا حيًا بكل مزود أو إثباتًا لجودة الإجابات أو تحمل الضغط."` | — |
| [SRC-61B24BEFCC-L000050](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L50) | 50 | `""` | — |
| [SRC-61B24BEFCC-L000051](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L51) | 51 | `"## 4. ما الذي لا يزال NOT_RUN / UNKNOWN؟"` | — |
| [SRC-61B24BEFCC-L000052](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L52) | 52 | `""` | — |
| [SRC-61B24BEFCC-L000053](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L53) | 53 | `"حتى إعداد هذه المصفوفة:"` | — |
| [SRC-61B24BEFCC-L000054](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L54) | 54 | `""` | — |
| [SRC-61B24BEFCC-L000055](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L55) | 55 | `"- **NOT_RUN:** لم يُنفذ الاختبار الحي الشامل للموفرين عبر استضافة محددة في هذه الجولة."` | — |
| [SRC-61B24BEFCC-L000056](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L56) | 56 | `"- **NOT_RUN:** لم يُنفذ اختبار يدوي بالمتصفح على الخدمة المنشورة."` | — |
| [SRC-61B24BEFCC-L000057](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L57) | 57 | `"- **NOT_RUN:** لم يُنفذ اختبار حمل ممثل أو soak test."` | — |
| [SRC-61B24BEFCC-L000058](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L58) | 58 | `"- **NOT_RUN:** لم تُثبت استعادة نسخة SQLite على مضيف الاستضافة المستهدف."` | — |
| [SRC-61B24BEFCC-L000059](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L59) | 59 | `"- **UNKNOWN:** صلاحية مفاتيح موفري البحث/النموذج وقيود حساباتهم الفعلية، ما لم يثبتها اختبار حي منفصل."` | — |
| [SRC-61B24BEFCC-L000060](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L60) | 60 | ``"- **UNKNOWN:** ربط SHA الموجود في `main` بالـartifact الفعلي لخدمة عامة، ما لم تتوفر بيانات نشر قابلة للفحص."`` | — |
| [SRC-61B24BEFCC-L000061](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L61) | 61 | `"- **UNKNOWN:** سلوك الوكيل العكسي الحقيقي وTLS وCORS وإعداد التخزين لكل مضيف بعينه."` | — |
| [SRC-61B24BEFCC-L000062](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L62) | 62 | `""` | — |
| [SRC-61B24BEFCC-L000063](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L63) | 63 | `"## 5. طريقة تشغيل قبول حي — بعد الموافقة فقط"` | — |
| [SRC-61B24BEFCC-L000064](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L64) | 64 | `""` | — |
| [SRC-61B24BEFCC-L000065](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L65) | 65 | `"هذا الإجراء ليس جزءًا من اختبارات PR العادية، وقد يستهلك استخدامًا من مزودي النموذج أو البحث."` | — |
| [SRC-61B24BEFCC-L000066](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L66) | 66 | `""` | — |
| [SRC-61B24BEFCC-L000067](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L67) | 67 | `"المتطلبات قبل التشغيل:"` | — |
| [SRC-61B24BEFCC-L000068](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L68) | 68 | `"1. وجود خدمة Omarai منشورة يملك مدير المشروع صلاحية اختبارها."` | — |
| [SRC-61B24BEFCC-L000069](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L69) | 69 | `"2. التحقق من أن الهدف هو أصل HTTPS المقصود."` | — |
| [SRC-61B24BEFCC-L000070](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L70) | 70 | ``"3. إعداد `OMARAI_BASE_URL` و`OMARAI_ACCESS_TOKEN` في GitHub Secrets فقط، وعدم وضع الرمز في مدخلات workflow أو تعليق أو سجل."`` | — |
| [SRC-61B24BEFCC-L000071](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L71) | 71 | `"4. موافقة صريحة على إجراء اختبار حي قد يستهلك رصيدًا."` | — |
| [SRC-61B24BEFCC-L000072](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L72) | 72 | `"5. استخدام سؤال عام غير حساس، وعدم استخدام بيانات عملاء حقيقية."` | — |
| [SRC-61B24BEFCC-L000073](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L73) | 73 | `"6. تسجيل commit/نسخة الخدمة والوقت ونتيجة كل خطوة دون تسجيل أي سر."` | — |
| [SRC-61B24BEFCC-L000074](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L74) | 74 | `""` | — |
| [SRC-61B24BEFCC-L000075](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L75) | 75 | ``"يشغّل `scripts/hosted_smoke_test.py`:"`` | — |
| [SRC-61B24BEFCC-L000076](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L76) | 76 | ``"- فحص `/api/health`."`` | — |
| [SRC-61B24BEFCC-L000077](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L77) | 77 | ``"- اختبار أن `POST /api/agent` بلا رمز يرجع 401."`` | — |
| [SRC-61B24BEFCC-L000078](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L78) | 78 | ``"- فحصًا حيًا للبحث والنموذج من `/api/diagnostics`."`` | — |
| [SRC-61B24BEFCC-L000079](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L79) | 79 | `"- سؤالًا عربيًا يتطلب بحثًا ومصادر."` | — |
| [SRC-61B24BEFCC-L000080](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L80) | 80 | `"- تحققًا من أن التقرير لا يحتاج إلى كشف مفاتيح."` | — |
| [SRC-61B24BEFCC-L000081](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L81) | 81 | `""` | — |
| [SRC-61B24BEFCC-L000082](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L82) | 82 | ``"إذا لم تتوفر البيئة أو الأسرار أو الموافقة على الاستخدام، تبقى النتيجة `NOT_RUN`؛ لا يُستعاض عن ذلك بنجاح CI."`` | — |
| [SRC-61B24BEFCC-L000083](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L83) | 83 | `""` | — |
| [SRC-61B24BEFCC-L000084](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L84) | 84 | `"## 6. شروط قبول نتيجة أي اختبار"` | — |
| [SRC-61B24BEFCC-L000085](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L85) | 85 | `""` | — |
| [SRC-61B24BEFCC-L000086](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L86) | 86 | `"يجب أن يتضمن سجل النتيجة:"` | — |
| [SRC-61B24BEFCC-L000087](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L87) | 87 | `"- معرف الاختبار واسمه."` | — |
| [SRC-61B24BEFCC-L000088](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L88) | 88 | `"- نوع الاختبار (unit/mock/local/container/live/load/restore/red-team)."` | — |
| [SRC-61B24BEFCC-L000089](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L89) | 89 | `"- SHA والفرع أو النسخة المنشورة."` | — |
| [SRC-61B24BEFCC-L000090](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L90) | 90 | `"- الأمر أو workflow ورابط التشغيل."` | — |
| [SRC-61B24BEFCC-L000091](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L91) | 91 | `"- إعدادات البيئة اللازمة دون الأسرار."` | — |
| [SRC-61B24BEFCC-L000092](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L92) | 92 | `"- النتيجة الفعلية ووقت الاختبار."` | — |
| [SRC-61B24BEFCC-L000093](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L93) | 93 | `"- ما يثبته الاختبار وما لا يثبته."` | — |
| [SRC-61B24BEFCC-L000094](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L94) | 94 | `"- الحالات المستثناة أو التي لم تُنفّذ."` | — |
| [SRC-61B24BEFCC-L000095](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L95) | 95 | `"- المسؤول عن مراجعة النتيجة ومعايير الإغلاق."` | — |
| [SRC-61B24BEFCC-L000096](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L96) | 96 | `""` | — |
| [SRC-61B24BEFCC-L000097](../OMARAI_TEST_EVIDENCE_MATRIX_AR.md#L97) | 97 | ``"لا تُحوّل `NOT_RUN` إلى `PASS`، ولا تستخدم نجاح Mock دليلًا على توفر موفر حي."`` | — |
## وثائق وفهرسة

### FILE-B6BD2CE1A8 — [docs/OPERATIONS_AR.md](../OPERATIONS_AR.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-B6BD2CE1A8-L000001](../OPERATIONS_AR.md#L1) | 1 | `"# دليل تشغيل Omarai"` | — |
| [SRC-B6BD2CE1A8-L000002](../OPERATIONS_AR.md#L2) | 2 | `""` | — |
| [SRC-B6BD2CE1A8-L000003](../OPERATIONS_AR.md#L3) | 3 | `"## التشغيل"` | — |
| [SRC-B6BD2CE1A8-L000004](../OPERATIONS_AR.md#L4) | 4 | `"من مجلد المشروع شغّل:"` | — |
| [SRC-B6BD2CE1A8-L000005](../OPERATIONS_AR.md#L5) | 5 | ````"```bash"```` | — |
| [SRC-B6BD2CE1A8-L000006](../OPERATIONS_AR.md#L6) | 6 | `"python -m cli.omarai serve"` | — |
| [SRC-B6BD2CE1A8-L000007](../OPERATIONS_AR.md#L7) | 7 | ````"```"```` | — |
| [SRC-B6BD2CE1A8-L000008](../OPERATIONS_AR.md#L8) | 8 | ``"ثم افتح `http://127.0.0.1:8765` في المتصفح على الهاتف نفسه. أوقف الخادم بـ Ctrl+C."`` | — |
| [SRC-B6BD2CE1A8-L000009](../OPERATIONS_AR.md#L9) | 9 | `""` | — |
| [SRC-B6BD2CE1A8-L000010](../OPERATIONS_AR.md#L10) | 10 | `"## سير العمل"` | — |
| [SRC-B6BD2CE1A8-L000011](../OPERATIONS_AR.md#L11) | 11 | `""` | — |
| [SRC-B6BD2CE1A8-L000012](../OPERATIONS_AR.md#L12) | 12 | `"يمكنك كذلك استخدام مربع «اسأل Omarai» لطلب إحصائيات السجل المحلي أو ترشيح إشارة للمراجعة أو تفسير الدرجة أو صياغة مسودة تواصل. الإجابات مبنية على قواعد محلية وسجلات محفوظة فقط؛ لا يوجد نموذج سحابي ولا تُرسل أي رسالة تلقائيًا."` | — |
| [SRC-B6BD2CE1A8-L000013](../OPERATIONS_AR.md#L13) | 13 | `""` | — |
| [SRC-B6BD2CE1A8-L000014](../OPERATIONS_AR.md#L14) | 14 | `"1. أدخل نصًا من مصدر عام أو مصدر لديك إذن باستخدامه."` | — |
| [SRC-B6BD2CE1A8-L000015](../OPERATIONS_AR.md#L15) | 15 | `"2. اضغط «حلّل الإشارة» وافحص العبارات المطابقة وسبب النقاط."` | — |
| [SRC-B6BD2CE1A8-L000016](../OPERATIONS_AR.md#L16) | 16 | `"3. أضف رابط المصدر الحقيقي قبل الحفظ."` | — |
| [SRC-B6BD2CE1A8-L000017](../OPERATIONS_AR.md#L17) | 17 | `"4. راجع الإشارات يدويًا وغيّر الحالة إلى مؤهل أو يحتاج مراجعة أو غير ذلك."` | — |
| [SRC-B6BD2CE1A8-L000018](../OPERATIONS_AR.md#L18) | 18 | `"5. صدّر CSV عند الحاجة واحتفظ بنسخة احتياطية آمنة."` | — |
| [SRC-B6BD2CE1A8-L000019](../OPERATIONS_AR.md#L19) | 19 | `""` | — |
| [SRC-B6BD2CE1A8-L000020](../OPERATIONS_AR.md#L20) | 20 | `"## قواعد مهمة"` | — |
| [SRC-B6BD2CE1A8-L000021](../OPERATIONS_AR.md#L21) | 21 | `"- لا تدخل رسائل خاصة أو بيانات اعتماد أو أرقام هواتف غير لازمة."` | — |
| [SRC-B6BD2CE1A8-L000022](../OPERATIONS_AR.md#L22) | 22 | `"- لا تعتبر الدرجة احتمالًا للشراء."` | — |
| [SRC-B6BD2CE1A8-L000023](../OPERATIONS_AR.md#L23) | 23 | `"- لا يتصفح Omarai المنصات تلقائيًا ولا يرسل رسائل."` | — |
| [SRC-B6BD2CE1A8-L000024](../OPERATIONS_AR.md#L24) | 24 | `"- الخادم مربوط بعنوان loopback افتراضيًا، ويرفض أنواع المحتوى غير JSON والطلبات ذات Origin غير محلي. لا تكشفه للشبكة أو الإنترنت دون مصادقة واختبار أمني."` | — |
| [SRC-B6BD2CE1A8-L000025](../OPERATIONS_AR.md#L25) | 25 | ``"- قاعدة البيانات الافتراضية: `~/.omarai/omarai.sqlite3`."`` | — |
## وثائق وفهرسة

### FILE-D911B73392 — [docs/RESEARCH_CONNECTORS_AR.md](../RESEARCH_CONNECTORS_AR.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-D911B73392-L000001](../RESEARCH_CONNECTORS_AR.md#L1) | 1 | `"# دليل البحث المتقدم والموصلات الاجتماعية — Omarai"` | — |
| [SRC-D911B73392-L000002](../RESEARCH_CONNECTORS_AR.md#L2) | 2 | `""` | — |
| [SRC-D911B73392-L000003](../RESEARCH_CONNECTORS_AR.md#L3) | 3 | `"هذا الدليل يشرح ما يستطيع Omarai الوصول إليه فعلًا، وما يحتاج إلى مفاتيح وصلاحيات، وكيفية إعدادها من Termux. لا توجد طريقة شرعية أو تقنية مضمونة للوصول إلى كل منشورات كل منصة: بعض البيانات تتطلب مراجعة تطبيق وصلاحيات، وبعضها لا يظهر إلا في البحث المفهرس."` | — |
| [SRC-D911B73392-L000004](../RESEARCH_CONNECTORS_AR.md#L4) | 4 | `""` | — |
| [SRC-D911B73392-L000005](../RESEARCH_CONNECTORS_AR.md#L5) | 5 | `"## 1. كيف يجري Omarai البحث؟"` | — |
| [SRC-D911B73392-L000006](../RESEARCH_CONNECTORS_AR.md#L6) | 6 | `""` | — |
| [SRC-D911B73392-L000007](../RESEARCH_CONNECTORS_AR.md#L7) | 7 | `"1. يفهم السؤال ويخطط حتى ثمانية استعلامات بحث، باستخدام النموذج اللغوي إذا كان مفتاحه مضبوطًا؛ وإلا يستخدم خطة احتياطية محددة."` | — |
| [SRC-D911B73392-L000008](../RESEARCH_CONNECTORS_AR.md#L8) | 8 | `"2. يبحث في DuckDuckGo HTML وBing RSS لكل استعلام، ويمكنه إضافة واجهتي البحث الرسميتين Brave Search وTavily عند ضبط مفاتيحهما، ويستخدم موجز Google News للأسئلة الحديثة."` | — |
| [SRC-D911B73392-L000009](../RESEARCH_CONNECTORS_AR.md#L9) | 9 | `"3. إذا كان السؤال اجتماعيًا، يجرّب المصادر العامة المتاحة والموصلات الرسمية التي أُعدّت بياناتها."` | — |
| [SRC-D911B73392-L000010](../RESEARCH_CONNECTORS_AR.md#L10) | 10 | `"4. يزيل النتائج المكررة ويجمع تكرار ظهور المصدر عبر الاستعلامات ومحركات البحث مع الاحتفاظ باسم الموفر والاستعلام ورابط المصدر."` | — |
| [SRC-D911B73392-L000011](../RESEARCH_CONNECTORS_AR.md#L11) | 11 | `"5. يحاول قراءة النص من أفضل ثماني صفحات عامة على الأكثر، ضمن حدود زمنية وحجمية، مع اتباع عدد محدود من التحويلات العامة بشرط التحقق من كل وجهة قبل الاتصال بها."` | — |
| [SRC-D911B73392-L000012](../RESEARCH_CONNECTORS_AR.md#L12) | 12 | `"6. ينتج إجابة بلغة السؤال مع روابط قابلة للمراجعة وتقرير يوضح ما جرى فعليًا: عدد الاستعلامات، المصادر والنطاقات الفريدة، الصفحات المقروءة، تنوع المحركات، نوع المصادر، وتغطية تواريخ النشر والتحذيرات. يحتوي على أوضاع تلقائي/معمّق/الأحدث/آراء الناس. مؤشرات التغطية تقيس اتساع البحث وقابلية مراجعة الدليل، ولا تعني نسبة صحة الإجابة."` | — |
| [SRC-D911B73392-L000013](../RESEARCH_CONNECTORS_AR.md#L13) | 13 | `"7. في البحث العميق، يمرر المسودة على مراجعة ثانية للاتساق مع المصادر. هذه مراجعة من النموذج/الموفر نفسه وليست تحققًا مستقلًا من الحقيقة."` | — |
| [SRC-D911B73392-L000014](../RESEARCH_CONNECTORS_AR.md#L14) | 14 | `""` | — |
| [SRC-D911B73392-L000015](../RESEARCH_CONNECTORS_AR.md#L15) | 15 | `"لا ينبغي تفسير اتفاق نتيجتين بحثيتين على أنه تصديق مستقل، ولا اعتبار عينة من التعليقات ممثلة لكل المستخدمين."` | — |
| [SRC-D911B73392-L000016](../RESEARCH_CONNECTORS_AR.md#L16) | 16 | `""` | — |
| [SRC-D911B73392-L000017](../RESEARCH_CONNECTORS_AR.md#L17) | 17 | `"## 2.1 واجهات بحث ويب اختيارية"` | — |
| [SRC-D911B73392-L000018](../RESEARCH_CONNECTORS_AR.md#L18) | 18 | `""` | — |
| [SRC-D911B73392-L000019](../RESEARCH_CONNECTORS_AR.md#L19) | 19 | `"يمكنك إضافة فهرسين مباشرين للبحث بدل الاعتماد على استخراج صفحات نتائج محركات البحث فقط. قد يحتاج كل مزود إلى حساب أو خطة أو حصّة استخدام؛ لا تفترض أن الخدمة مجانية أو أن المفتاح صالح قبل الاختبار الحي."` | — |
| [SRC-D911B73392-L000020](../RESEARCH_CONNECTORS_AR.md#L20) | 20 | `""` | — |
| [SRC-D911B73392-L000021](../RESEARCH_CONNECTORS_AR.md#L21) | 21 | ````"```bash"```` | — |
| [SRC-D911B73392-L000022](../RESEARCH_CONNECTORS_AR.md#L22) | 22 | `"read -r -s -p \"Brave Search API key: \" BRAVE_SEARCH_API_KEY; printf '\\\\n'; export BRAVE_SEARCH_API_KEY"` | — |
| [SRC-D911B73392-L000023](../RESEARCH_CONNECTORS_AR.md#L23) | 23 | `"read -r -s -p \"Tavily API key: \" TAVILY_API_KEY; printf '\\\\n'; export TAVILY_API_KEY"` | — |
| [SRC-D911B73392-L000024](../RESEARCH_CONNECTORS_AR.md#L24) | 24 | ````"```"```` | — |
| [SRC-D911B73392-L000025](../RESEARCH_CONNECTORS_AR.md#L25) | 25 | `""` | — |
| [SRC-D911B73392-L000026](../RESEARCH_CONNECTORS_AR.md#L26) | 26 | `"يدمج Omarai النتائج من هذه الواجهات مع محركات البحث العامة عند ضبط المتغيرات. لا تُحفظ المفاتيح في المستودع أو واجهة HTML، ولا يُرجعها تقرير الصحة. إذا فشل المفتاح أو انتهت الحصة، قد تظهر نتائج من المحركات العامة الأخرى؛ افحص أسماء المحركات الفعلية في تقرير البحث لتعرف ما أعاد نتائج في هذه الجولة."` | — |
| [SRC-D911B73392-L000027](../RESEARCH_CONNECTORS_AR.md#L27) | 27 | `""` | — |
| [SRC-D911B73392-L000028](../RESEARCH_CONNECTORS_AR.md#L28) | 28 | `"## 2. المصادر والحدود"` | — |
| [SRC-D911B73392-L000029](../RESEARCH_CONNECTORS_AR.md#L29) | 29 | `""` | — |
| [SRC-D911B73392-L000030](../RESEARCH_CONNECTORS_AR.md#L30) | 30 | `"\| المصدر \| ما يستخدمه Omarai \| ما يلزم أو ما لا يمكن ضمانه \|"` | — |
| [SRC-D911B73392-L000031](../RESEARCH_CONNECTORS_AR.md#L31) | 31 | `"\| --- \| --- \| --- \|"` | — |
| [SRC-D911B73392-L000032](../RESEARCH_CONNECTORS_AR.md#L32) | 32 | `"\| صفحات الويب العامة \| DuckDuckGo HTML وBing RSS، وBrave Search API وTavily Search API عند إعداد المفاتيح، واستخراج نص الصفحات المتاحة \| قد تمنع بعض المواقع القراءة أو لا تظهر في نتائج البحث؛ لا يتم تجاوز تسجيل الدخول أو الجدران المدفوعة \|"` | — |
| [SRC-D911B73392-L000033](../RESEARCH_CONNECTORS_AR.md#L33) | 33 | `"\| الأخبار الحديثة \| Google News RSS بالإضافة إلى البحث العام \| التاريخ الذي يظهر في موجز البحث قد لا يكون تاريخ نشر الصفحة الأصلية؛ يجب فتح المصدر والتحقق \|"` | — |
| [SRC-D911B73392-L000034](../RESEARCH_CONNECTORS_AR.md#L34) | 34 | `"\| Reddit \| موجز البحث العام RSS \| قد يُحجب أو يُقيَّد أحيانًا؛ يمكن إعداد OAuth لطلب API رسمي عند توفر وصول مسموح \|"` | — |
| [SRC-D911B73392-L000035](../RESEARCH_CONNECTORS_AR.md#L35) | 35 | `"\| Bluesky \| واجهة البحث العامة للمنشورات \| بحث عام وليس بيانات خاصة أو رسائل مباشرة \|"` | — |
| [SRC-D911B73392-L000036](../RESEARCH_CONNECTORS_AR.md#L36) | 36 | `"\| Instagram \| صفحات عامة مفهرسة؛ وموصل Graph API للوسوم العامة عند إعداده \| واجهة الوسوم الرسمية ليست بحثًا شاملًا في كل المنشورات، وتتطلب حسابًا وصلاحيات وموافقة/ميزات مناسبة وحدود استخدام \|"` | — |
| [SRC-D911B73392-L000037](../RESEARCH_CONNECTORS_AR.md#L37) | 37 | `"\| Facebook \| صفحات عامة مفهرسة؛ وموصل مباشر لصفحات محددة صراحةً عند إعداده \| الموصل المباشر ليس بحثًا عالميًا في Facebook؛ يعمل فقط على Page IDs يمكن للرمز والصلاحيات قراءتها \|"` | — |
| [SRC-D911B73392-L000038](../RESEARCH_CONNECTORS_AR.md#L38) | 38 | `"\| X \| صفحات عامة مفهرسة؛ وواجهة البحث الحديث الرسمية عند إعداد Bearer Token \| يتطلب وصول API مناسبًا، ونطاق البحث والحدود تابعان لخطة X \|"` | — |
| [SRC-D911B73392-L000039](../RESEARCH_CONNECTORS_AR.md#L39) | 39 | `"\| YouTube \| صفحات الفيديو العامة المفهرسة؛ وYouTube Data API عند إعداد المفتاح \| الواجهة الرسمية لها حصص استخدام، وقد لا تعيد كل الفيديوهات \|"` | — |
| [SRC-D911B73392-L000040](../RESEARCH_CONNECTORS_AR.md#L40) | 40 | `"\| TikTok \| الصفحات العامة التي تظهر في محركات البحث \| لا يدّعي Omarai أنه يملك بحثًا رسميًا شاملًا في TikTok. أدوات Research API تتطلب الأهلية والموافقة البحثية، وهي ليست واجهة عامة تلقائية للاستخدام التجاري \|"` | — |
| [SRC-D911B73392-L000041](../RESEARCH_CONNECTORS_AR.md#L41) | 41 | `""` | — |
| [SRC-D911B73392-L000042](../RESEARCH_CONNECTORS_AR.md#L42) | 42 | `"## 3. تشغيل الطبقة التوليدية"` | — |
| [SRC-D911B73392-L000043](../RESEARCH_CONNECTORS_AR.md#L43) | 43 | `""` | — |
| [SRC-D911B73392-L000044](../RESEARCH_CONNECTORS_AR.md#L44) | 44 | ``"يقرأ Omarai مفتاح النموذج من متغيرات بيئة Termux. افتراضيًا يستخدم نموذج NVIDIA Nemotron 3 Ultra (المجاني) لتخطيط البحث، وGoogle Gemma 4 31B Instruct (المجاني) لصياغة الإجابة ومراجعة الاتساق الثانية، مع الرجوع إلى `openrouter/free` إذا أخفق النموذج المحدد. هذا يقلل تغيير النموذج عشوائيًا بين الطلبات، لكنه لا يضمن استجابة كل موفر أو إجابة صحيحة. المفتاح يتيح تخطيط البحث والإجابة التوليدية والمراجعة الثانية. لا تحفظه داخل مستودع GitHub أو ملف HTML أو المحادثة. **تنبيه خصوصية مهم:** يرسل Omarai السؤال وسياق المتابعة ومقتطفات الصفحات المختارة إلى مزود النموذج الخارجي لكي يخطط ويكتب الإجابة ويراجعها. نقطة نهاية NVIDIA Nemotron المجانية في OpenRouter توضّح أن جلسات الاستخدام قد تُسجل لأغراض الأمان وتحسين منتجات NVIDIA؛ لذلك لا تستخدم هذا الإعداد مع كلمات مرور أو مفاتيح أو معلومات سرية أو بيانات شخصية/تجارية حساسة. راجع [إشعار الخصوصية لنقطة Nemotron المجانية](https://openrouter.ai/nvidia/nemotron-3-ultra-550b-a55b:free)."`` | — |
| [SRC-D911B73392-L000045](../RESEARCH_CONNECTORS_AR.md#L45) | 45 | `""` | — |
| [SRC-D911B73392-L000046](../RESEARCH_CONNECTORS_AR.md#L46) | 46 | ````"```bash"```` | — |
| [SRC-D911B73392-L000047](../RESEARCH_CONNECTORS_AR.md#L47) | 47 | `"read -r -s -p \"OpenRouter API key: \" OPENROUTER_API_KEY"` | — |
| [SRC-D911B73392-L000048](../RESEARCH_CONNECTORS_AR.md#L48) | 48 | `"printf '\\n'"` | — |
| [SRC-D911B73392-L000049](../RESEARCH_CONNECTORS_AR.md#L49) | 49 | `"export OPENROUTER_API_KEY"` | — |
| [SRC-D911B73392-L000050](../RESEARCH_CONNECTORS_AR.md#L50) | 50 | ````"```"```` | — |
| [SRC-D911B73392-L000051](../RESEARCH_CONNECTORS_AR.md#L51) | 51 | `""` | — |
| [SRC-D911B73392-L000052](../RESEARCH_CONNECTORS_AR.md#L52) | 52 | ``"يمكن تغيير موفر النموذج المتوافق مع OpenAI عبر `OMARAI_LLM_BASE_URL`. اضبط `OMARAI_PLANNER_MODEL` و`OMARAI_ANSWER_MODEL` و`OMARAI_REVIEW_MODEL` لتغيير الأدوار كلٌ على حدة، أو `OMARAI_LLM_MODEL` لتطبيق نموذج واحد على الأدوار التي لم تُحدد لها قيمة منفصلة، و`OMARAI_LLM_FALLBACK_MODEL` لتغيير النموذج الاحتياطي. توافر النماذج المجانية وحدودها يتغير؛ لذلك لا يفترض التطبيق أن النموذج مجاني دائمًا أو أن الطلب سينجح كل مرة."`` | — |
| [SRC-D911B73392-L000053](../RESEARCH_CONNECTORS_AR.md#L53) | 53 | `""` | — |
| [SRC-D911B73392-L000054](../RESEARCH_CONNECTORS_AR.md#L54) | 54 | `"## 4. إعداد الموصلات الرسمية الاختيارية"` | — |
| [SRC-D911B73392-L000055](../RESEARCH_CONNECTORS_AR.md#L55) | 55 | `""` | — |
| [SRC-D911B73392-L000056](../RESEARCH_CONNECTORS_AR.md#L56) | 56 | `"نفّذ فقط الأجزاء التي تملك بيانات اعتمادها وصلاحيات استخدامها. الأوامر أدناه تطلب السر دون إظهاره أثناء الكتابة، لكنها تبقيه في بيئة جلسة Termux الحالية حتى توقف الخادم أو تغلق الجلسة."` | — |
| [SRC-D911B73392-L000057](../RESEARCH_CONNECTORS_AR.md#L57) | 57 | `""` | — |
| [SRC-D911B73392-L000058](../RESEARCH_CONNECTORS_AR.md#L58) | 58 | `"### Reddit OAuth"` | — |
| [SRC-D911B73392-L000059](../RESEARCH_CONNECTORS_AR.md#L59) | 59 | `""` | — |
| [SRC-D911B73392-L000060](../RESEARCH_CONNECTORS_AR.md#L60) | 60 | `"يتطلب بيانات تطبيق Reddit مع وصول API مسموحًا وفق شروط Reddit:"` | — |
| [SRC-D911B73392-L000061](../RESEARCH_CONNECTORS_AR.md#L61) | 61 | `""` | — |
| [SRC-D911B73392-L000062](../RESEARCH_CONNECTORS_AR.md#L62) | 62 | ````"```bash"```` | — |
| [SRC-D911B73392-L000063](../RESEARCH_CONNECTORS_AR.md#L63) | 63 | `"read -r -s -p \"Reddit client ID: \" REDDIT_CLIENT_ID; printf '\\n'; export REDDIT_CLIENT_ID"` | — |
| [SRC-D911B73392-L000064](../RESEARCH_CONNECTORS_AR.md#L64) | 64 | `"read -r -s -p \"Reddit client secret: \" REDDIT_CLIENT_SECRET; printf '\\n'; export REDDIT_CLIENT_SECRET"` | — |
| [SRC-D911B73392-L000065](../RESEARCH_CONNECTORS_AR.md#L65) | 65 | `"read -r -p \"Reddit User-Agent: \" REDDIT_USER_AGENT; export REDDIT_USER_AGENT"` | — |
| [SRC-D911B73392-L000066](../RESEARCH_CONNECTORS_AR.md#L66) | 66 | ````"```"```` | — |
| [SRC-D911B73392-L000067](../RESEARCH_CONNECTORS_AR.md#L67) | 67 | `""` | — |
| [SRC-D911B73392-L000068](../RESEARCH_CONNECTORS_AR.md#L68) | 68 | `"عند ضبط هذه القيم، يجرّب Omarai OAuth API. إن تعذر العثور على نتائج عبر API، فقد يحاول موجز البحث العام كبديل؛ ولا يعني ذلك أن البديل مضمون."` | — |
| [SRC-D911B73392-L000069](../RESEARCH_CONNECTORS_AR.md#L69) | 69 | `""` | — |
| [SRC-D911B73392-L000070](../RESEARCH_CONNECTORS_AR.md#L70) | 70 | `"### Instagram Graph API — وسوم عامة"` | — |
| [SRC-D911B73392-L000071](../RESEARCH_CONNECTORS_AR.md#L71) | 71 | `""` | — |
| [SRC-D911B73392-L000072](../RESEARCH_CONNECTORS_AR.md#L72) | 72 | `"يتطلب Instagram User ID ورمز وصول صالحًا، مع الأذونات/الميزات اللازمة في تطبيق Meta. يقتصر الموصل على بحث الوسوم وجلب عينة من الوسائط العامة الحديثة؛ لا يصل إلى الحسابات الخاصة ولا يبحث كل Instagram."` | — |
| [SRC-D911B73392-L000073](../RESEARCH_CONNECTORS_AR.md#L73) | 73 | `""` | — |
| [SRC-D911B73392-L000074](../RESEARCH_CONNECTORS_AR.md#L74) | 74 | ````"```bash"```` | — |
| [SRC-D911B73392-L000075](../RESEARCH_CONNECTORS_AR.md#L75) | 75 | `"read -r -p \"Instagram professional user ID: \" INSTAGRAM_USER_ID; export INSTAGRAM_USER_ID"` | — |
| [SRC-D911B73392-L000076](../RESEARCH_CONNECTORS_AR.md#L76) | 76 | `"read -r -s -p \"Instagram access token: \" INSTAGRAM_ACCESS_TOKEN; printf '\\n'; export INSTAGRAM_ACCESS_TOKEN"` | — |
| [SRC-D911B73392-L000077](../RESEARCH_CONNECTORS_AR.md#L77) | 77 | ````"```"```` | — |
| [SRC-D911B73392-L000078](../RESEARCH_CONNECTORS_AR.md#L78) | 78 | `""` | — |
| [SRC-D911B73392-L000079](../RESEARCH_CONNECTORS_AR.md#L79) | 79 | ``"يمكن ضبط إصدار Graph API الذي يطابق تطبيقك عبر `META_GRAPH_VERSION`. يبدأ Omarai بوسم واحد في الطلب لتقليل استهلاك حصة الوسوم؛ قد يظل الموصل يرفض الطلب إذا لم تكن الصلاحيات أو الحصة أو نسخة API مناسبة."`` | — |
| [SRC-D911B73392-L000080](../RESEARCH_CONNECTORS_AR.md#L80) | 80 | `""` | — |
| [SRC-D911B73392-L000081](../RESEARCH_CONNECTORS_AR.md#L81) | 81 | `"### Facebook Pages — صفحات محددة فقط"` | — |
| [SRC-D911B73392-L000082](../RESEARCH_CONNECTORS_AR.md#L82) | 82 | `""` | — |
| [SRC-D911B73392-L000083](../RESEARCH_CONNECTORS_AR.md#L83) | 83 | `"حدّد الصفحات التي لديك وصول مصرح بها. لا تضع رمزًا عامًا أو تحاول استخدام رمز لا يملك صلاحية الوصول للصفحة:"` | — |
| [SRC-D911B73392-L000084](../RESEARCH_CONNECTORS_AR.md#L84) | 84 | `""` | — |
| [SRC-D911B73392-L000085](../RESEARCH_CONNECTORS_AR.md#L85) | 85 | ````"```bash"```` | — |
| [SRC-D911B73392-L000086](../RESEARCH_CONNECTORS_AR.md#L86) | 86 | `"read -r -s -p \"Facebook Page access token: \" FACEBOOK_PAGE_ACCESS_TOKEN; printf '\\n'; export FACEBOOK_PAGE_ACCESS_TOKEN"` | — |
| [SRC-D911B73392-L000087](../RESEARCH_CONNECTORS_AR.md#L87) | 87 | `"read -r -p \"Authorized Page IDs, comma-separated: \" FACEBOOK_PAGE_IDS; export FACEBOOK_PAGE_IDS"` | — |
| [SRC-D911B73392-L000088](../RESEARCH_CONNECTORS_AR.md#L88) | 88 | ````"```"```` | — |
| [SRC-D911B73392-L000089](../RESEARCH_CONNECTORS_AR.md#L89) | 89 | `""` | — |
| [SRC-D911B73392-L000090](../RESEARCH_CONNECTORS_AR.md#L90) | 90 | `"يقرأ الموصل أحدث منشورات الصفحات المحددة وعينة محدودة من التعليقات العامة التي تسمح بها الصلاحيات. قد تفشل قراءة المنشورات أو التعليقات إذا كانت صلاحيات التطبيق لا تسمح بها."` | — |
| [SRC-D911B73392-L000091](../RESEARCH_CONNECTORS_AR.md#L91) | 91 | `""` | — |
| [SRC-D911B73392-L000092](../RESEARCH_CONNECTORS_AR.md#L92) | 92 | `"### X وYouTube"` | — |
| [SRC-D911B73392-L000093](../RESEARCH_CONNECTORS_AR.md#L93) | 93 | `""` | — |
| [SRC-D911B73392-L000094](../RESEARCH_CONNECTORS_AR.md#L94) | 94 | ````"```bash"```` | — |
| [SRC-D911B73392-L000095](../RESEARCH_CONNECTORS_AR.md#L95) | 95 | `"read -r -s -p \"X API bearer token: \" X_BEARER_TOKEN; printf '\\n'; export X_BEARER_TOKEN"` | — |
| [SRC-D911B73392-L000096](../RESEARCH_CONNECTORS_AR.md#L96) | 96 | `"read -r -s -p \"YouTube Data API key: \" YOUTUBE_API_KEY; printf '\\n'; export YOUTUBE_API_KEY"` | — |
| [SRC-D911B73392-L000097](../RESEARCH_CONNECTORS_AR.md#L97) | 97 | ````"```"```` | — |
| [SRC-D911B73392-L000098](../RESEARCH_CONNECTORS_AR.md#L98) | 98 | `""` | — |
| [SRC-D911B73392-L000099](../RESEARCH_CONNECTORS_AR.md#L99) | 99 | `"يجب أن يكون رمز X مرتبطًا بخطة وصول تشمل نقطة البحث المستخدمة. مفتاح YouTube يحتاج إلى مشروع Google Cloud تم تفعيل YouTube Data API فيه، ويخضع للحصة. لا يضمن وجود المفتاح أن الحساب يملك كل الصلاحيات أو حصة كافية."` | — |
| [SRC-D911B73392-L000100](../RESEARCH_CONNECTORS_AR.md#L100) | 100 | `""` | — |
| [SRC-D911B73392-L000101](../RESEARCH_CONNECTORS_AR.md#L101) | 101 | `"### البدء بعد الإعداد"` | — |
| [SRC-D911B73392-L000102](../RESEARCH_CONNECTORS_AR.md#L102) | 102 | `""` | — |
| [SRC-D911B73392-L000103](../RESEARCH_CONNECTORS_AR.md#L103) | 103 | `"بعد إعداد أي متغيرات اختيارية تريدها، ابدأ الخادم في **جلسة Termux نفسها**:"` | — |
| [SRC-D911B73392-L000104](../RESEARCH_CONNECTORS_AR.md#L104) | 104 | `""` | — |
| [SRC-D911B73392-L000105](../RESEARCH_CONNECTORS_AR.md#L105) | 105 | ````"```bash"```` | — |
| [SRC-D911B73392-L000106](../RESEARCH_CONNECTORS_AR.md#L106) | 106 | `"python -m cli.omarai serve"` | — |
| [SRC-D911B73392-L000107](../RESEARCH_CONNECTORS_AR.md#L107) | 107 | ````"```"```` | — |
| [SRC-D911B73392-L000108](../RESEARCH_CONNECTORS_AR.md#L108) | 108 | `""` | — |
| [SRC-D911B73392-L000109](../RESEARCH_CONNECTORS_AR.md#L109) | 109 | ``"افتح `http://127.0.0.1:8765` للمحادثة البحثية و`http://127.0.0.1:8765/api/health` لحالة الإعداد. تقرير الصحة يذكر ما إذا كانت المتغيرات موجودة فقط؛ ولا يمكنه التأكد من صلاحيتها حتى يجرب الموصل طلبًا حقيقيًا."`` | — |
| [SRC-D911B73392-L000110](../RESEARCH_CONNECTORS_AR.md#L110) | 110 | `""` | — |
| [SRC-D911B73392-L000111](../RESEARCH_CONNECTORS_AR.md#L111) | 111 | `"## 5. اختبار حي للاتصال"` | — |
| [SRC-D911B73392-L000112](../RESEARCH_CONNECTORS_AR.md#L112) | 112 | `""` | — |
| [SRC-D911B73392-L000113](../RESEARCH_CONNECTORS_AR.md#L113) | 113 | `"افتح لوحة Omarai واضغط **«اختبار حي للبحث والنموذج»**. هذا الفحص ينفّذ طلب بحث فعليًا إلى محركات البحث العامة، ويرسل طلبًا صغيرًا إلى نموذج الإجابة إذا كان المفتاح مضبوطًا. إذا فعّلت خيار اختبار المصادر الاجتماعية، فسينفّذ طلبات عامة/مصرحًا بها إلى الموصلات المناسبة. قد يستغرق فحص الشبكات الاجتماعية وقتًا أطول، وقد يستهلك حصص APIs أو يواجه حدود المعدل."` | — |
| [SRC-D911B73392-L000114](../RESEARCH_CONNECTORS_AR.md#L114) | 114 | `""` | — |
| [SRC-D911B73392-L000115](../RESEARCH_CONNECTORS_AR.md#L115) | 115 | `"يمكن تنفيذ الفحص نفسه من الطرفية أو أداة API:"` | — |
| [SRC-D911B73392-L000116](../RESEARCH_CONNECTORS_AR.md#L116) | 116 | `""` | — |
| [SRC-D911B73392-L000117](../RESEARCH_CONNECTORS_AR.md#L117) | 117 | ````"```bash"```` | — |
| [SRC-D911B73392-L000118](../RESEARCH_CONNECTORS_AR.md#L118) | 118 | `"curl -sS -X POST http://127.0.0.1:8765/api/diagnostics \\"` | — |
| [SRC-D911B73392-L000119](../RESEARCH_CONNECTORS_AR.md#L119) | 119 | `"  -H 'Content-Type: application/json' \\"` | — |
| [SRC-D911B73392-L000120](../RESEARCH_CONNECTORS_AR.md#L120) | 120 | `"  -d '{\"test_model\":true,\"test_social\":false}'"` | — |
| [SRC-D911B73392-L000121](../RESEARCH_CONNECTORS_AR.md#L121) | 121 | ````"```"```` | — |
| [SRC-D911B73392-L000122](../RESEARCH_CONNECTORS_AR.md#L122) | 122 | `""` | — |
| [SRC-D911B73392-L000123](../RESEARCH_CONNECTORS_AR.md#L123) | 123 | ``"للفحص الاجتماعي أيضًا، غيّر `test_social` إلى `true`. تعني حالة `degraded` أن الفحص لم يحصل على نتائج كافية أو أن أحد الأجزاء لم يعمل كما هو متوقع؛ ولا تثبت وحدها أن المنصة متوقفة. يظهر `/api/health` وجود إعدادات البيئة فقط، أما الفحص الحي فيختبر اتصالًا فعليًا. لا يعرض التقرير المفاتيح السرية أو يحتفظ بنص استجابة اختبار النموذج."`` | — |
| [SRC-D911B73392-L000124](../RESEARCH_CONNECTORS_AR.md#L124) | 124 | `""` | — |
| [SRC-D911B73392-L000125](../RESEARCH_CONNECTORS_AR.md#L125) | 125 | `"## 6. قراءة الأدلة والتحقق منها"` | — |
| [SRC-D911B73392-L000126](../RESEARCH_CONNECTORS_AR.md#L126) | 126 | `""` | — |
| [SRC-D911B73392-L000127](../RESEARCH_CONNECTORS_AR.md#L127) | 127 | `"- افتح المصادر الأساسية واقرأ السياق الكامل قبل اتخاذ قرار تجاري أو قانوني أو طبي."` | — |
| [SRC-D911B73392-L000128](../RESEARCH_CONNECTORS_AR.md#L128) | 128 | `"- المنشور أو التعليق قد يكون ساخرًا أو قديمًا أو ترويجيًا أو خارج السياق. يوضح Omarai المصدر والنص المتاح، لكنه لا يثبت هوية الكاتب أو صحة كلامه."` | — |
| [SRC-D911B73392-L000129](../RESEARCH_CONNECTORS_AR.md#L129) | 129 | `"- لا تستخدم بيانات شخصية غير لازمة، ولا تجمع محتوى خاصًا أو تتجاوز شروط أي منصة."` | — |
| [SRC-D911B73392-L000130](../RESEARCH_CONNECTORS_AR.md#L130) | 130 | `"- لا يرسل Omarai رسائل أو يتواصل مع أصحاب الحسابات تلقائيًا. أي تواصل أو إجراء خارجي يجب أن يبقى بقرار بشري ومراجعة منفصلة."` | — |
## ملفات أخرى

### FILE-C693279643 — [LICENSE](../../LICENSE#L1)

- النوع: **بدون امتداد**
- نطاق الفهرسة: جرد ملف نصي فقط

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-C693279643-L000001](../../LICENSE#L1) | 1 | `"MIT License"` | — |
| [SRC-C693279643-L000002](../../LICENSE#L2) | 2 | `""` | — |
| [SRC-C693279643-L000003](../../LICENSE#L3) | 3 | `"Copyright (c) 2026 Omarai contributors"` | — |
| [SRC-C693279643-L000004](../../LICENSE#L4) | 4 | `""` | — |
| [SRC-C693279643-L000005](../../LICENSE#L5) | 5 | `"Permission is hereby granted, free of charge, to any person obtaining a copy"` | — |
| [SRC-C693279643-L000006](../../LICENSE#L6) | 6 | `"of this software and associated documentation files (the \"Software\"), to deal"` | — |
| [SRC-C693279643-L000007](../../LICENSE#L7) | 7 | `"in the Software without restriction, including without limitation the rights"` | — |
| [SRC-C693279643-L000008](../../LICENSE#L8) | 8 | `"to use, copy, modify, merge, publish, distribute, sublicense, and/or sell"` | — |
| [SRC-C693279643-L000009](../../LICENSE#L9) | 9 | `"copies of the Software, and to permit persons to whom the Software is"` | — |
| [SRC-C693279643-L000010](../../LICENSE#L10) | 10 | `"furnished to do so, subject to the following conditions:"` | — |
| [SRC-C693279643-L000011](../../LICENSE#L11) | 11 | `""` | — |
| [SRC-C693279643-L000012](../../LICENSE#L12) | 12 | `"The above copyright notice and this permission notice shall be included in all"` | — |
| [SRC-C693279643-L000013](../../LICENSE#L13) | 13 | `"copies or substantial portions of the Software."` | — |
| [SRC-C693279643-L000014](../../LICENSE#L14) | 14 | `""` | — |
| [SRC-C693279643-L000015](../../LICENSE#L15) | 15 | `"THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR"` | — |
| [SRC-C693279643-L000016](../../LICENSE#L16) | 16 | `"IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,"` | — |
| [SRC-C693279643-L000017](../../LICENSE#L17) | 17 | `"FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE"` | — |
| [SRC-C693279643-L000018](../../LICENSE#L18) | 18 | `"AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER"` | — |
| [SRC-C693279643-L000019](../../LICENSE#L19) | 19 | `"LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,"` | — |
| [SRC-C693279643-L000020](../../LICENSE#L20) | 20 | `"OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE"` | — |
| [SRC-C693279643-L000021](../../LICENSE#L21) | 21 | `"SOFTWARE."` | — |
## إعدادات وتشغيل

### FILE-50C86B7ED8 — [pyproject.toml](../../pyproject.toml#L1)

- النوع: **TOML**
- نطاق الفهرسة: جرد الملف + مفاتيح إعداد ساكنة

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-50C86B7ED8-L000001](../../pyproject.toml#L1) | 1 | `"[build-system]"` | — |
| [SRC-50C86B7ED8-L000002](../../pyproject.toml#L2) | 2 | `"requires = [\"setuptools>=68\"]"` | — |
| [SRC-50C86B7ED8-L000003](../../pyproject.toml#L3) | 3 | `"build-backend = \"setuptools.build_meta\""` | — |
| [SRC-50C86B7ED8-L000004](../../pyproject.toml#L4) | 4 | `""` | — |
| [SRC-50C86B7ED8-L000005](../../pyproject.toml#L5) | 5 | `"[project]"` | — |
| [SRC-50C86B7ED8-L000006](../../pyproject.toml#L6) | 6 | `"name = \"omarai-agent\""` | — |
| [SRC-50C86B7ED8-L000007](../../pyproject.toml#L7) | 7 | `"version = \"0.2.0\""` | — |
| [SRC-50C86B7ED8-L000008](../../pyproject.toml#L8) | 8 | `"description = \"Arabic-first web research and generative Q&A agent with lead workspace\""` | — |
| [SRC-50C86B7ED8-L000009](../../pyproject.toml#L9) | 9 | `"readme = \"README.md\""` | — |
| [SRC-50C86B7ED8-L000010](../../pyproject.toml#L10) | 10 | `"requires-python = \">=3.11\""` | — |
| [SRC-50C86B7ED8-L000011](../../pyproject.toml#L11) | 11 | `"license = { text = \"MIT\" }"` | — |
| [SRC-50C86B7ED8-L000012](../../pyproject.toml#L12) | 12 | `"dependencies = ["` | — |
| [SRC-50C86B7ED8-L000013](../../pyproject.toml#L13) | 13 | `"  \"beautifulsoup4>=4.12,<5\","` | — |
| [SRC-50C86B7ED8-L000014](../../pyproject.toml#L14) | 14 | `"  \"httpx>=0.27,<1\","` | — |
| [SRC-50C86B7ED8-L000015](../../pyproject.toml#L15) | 15 | `"  \"tldextract>=5.3,<6\","` | — |
| [SRC-50C86B7ED8-L000016](../../pyproject.toml#L16) | 16 | `"]"` | — |
| [SRC-50C86B7ED8-L000017](../../pyproject.toml#L17) | 17 | `""` | — |
| [SRC-50C86B7ED8-L000018](../../pyproject.toml#L18) | 18 | `"[project.optional-dependencies]"` | — |
| [SRC-50C86B7ED8-L000019](../../pyproject.toml#L19) | 19 | `"dev = [\"pytest>=8.0\", \"ruff>=0.5\"]"` | — |
| [SRC-50C86B7ED8-L000020](../../pyproject.toml#L20) | 20 | `""` | — |
| [SRC-50C86B7ED8-L000021](../../pyproject.toml#L21) | 21 | `"[tool.pytest.ini_options]"` | — |
| [SRC-50C86B7ED8-L000022](../../pyproject.toml#L22) | 22 | `"testpaths = [\"tests\"]"` | — |
| [SRC-50C86B7ED8-L000023](../../pyproject.toml#L23) | 23 | `""` | — |
| [SRC-50C86B7ED8-L000024](../../pyproject.toml#L24) | 24 | `"[tool.setuptools.packages.find]"` | — |
| [SRC-50C86B7ED8-L000025](../../pyproject.toml#L25) | 25 | `"include = [\"agents*\", \"api*\", \"cli*\"]"` | — |
| [SRC-50C86B7ED8-L000026](../../pyproject.toml#L26) | 26 | `"exclude = [\"tests*\", \"web*\"]"` | — |
| [SRC-50C86B7ED8-L000027](../../pyproject.toml#L27) | 27 | `""` | — |
| [SRC-50C86B7ED8-L000028](../../pyproject.toml#L28) | 28 | `"[tool.ruff]"` | — |
| [SRC-50C86B7ED8-L000029](../../pyproject.toml#L29) | 29 | `"line-length = 100"` | — |
| [SRC-50C86B7ED8-L000030](../../pyproject.toml#L30) | 30 | `"target-version = \"py311\""` | — |
| [SRC-50C86B7ED8-L000031](../../pyproject.toml#L31) | 31 | `""` | — |
| [SRC-50C86B7ED8-L000032](../../pyproject.toml#L32) | 32 | `"[tool.ruff.lint]"` | — |
| [SRC-50C86B7ED8-L000033](../../pyproject.toml#L33) | 33 | `"# Keep default rules; ignore only patterns intentional in this codebase."` | — |
| [SRC-50C86B7ED8-L000034](../../pyproject.toml#L34) | 34 | `"# BLE001: broad except at API boundary to avoid leaking internals"` | — |
| [SRC-50C86B7ED8-L000035](../../pyproject.toml#L35) | 35 | `"# E501: long Arabic/English diagnostic strings"` | — |
| [SRC-50C86B7ED8-L000036](../../pyproject.toml#L36) | 36 | `"# I001: historical import order; do not block CI on style alone"` | — |
| [SRC-50C86B7ED8-L000037](../../pyproject.toml#L37) | 37 | `"# F841: unused assignment kept for clarity in some tests"` | — |
| [SRC-50C86B7ED8-L000038](../../pyproject.toml#L38) | 38 | `"# RUF100: residual noqa:BLE001 comments after BLE001 is ignored globally"` | — |
| [SRC-50C86B7ED8-L000039](../../pyproject.toml#L39) | 39 | `"ignore = [\"BLE001\", \"E501\", \"I001\", \"F841\", \"RUF100\"]"` | — |
## إعدادات وتشغيل

### FILE-115C2027D9 — [railway.json](../../railway.json#L1)

- النوع: **JSON**
- نطاق الفهرسة: جرد الملف + مفاتيح إعداد ساكنة

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-115C2027D9-L000001](../../railway.json#L1) | 1 | `"{"` | — |
| [SRC-115C2027D9-L000002](../../railway.json#L2) | 2 | `"  \"$schema\": \"https://railway.com/railway.schema.json\","` | — |
| [SRC-115C2027D9-L000003](../../railway.json#L3) | 3 | `"  \"build\": {"` | — |
| [SRC-115C2027D9-L000004](../../railway.json#L4) | 4 | `"    \"builder\": \"DOCKERFILE\","` | — |
| [SRC-115C2027D9-L000005](../../railway.json#L5) | 5 | `"    \"dockerfilePath\": \"Dockerfile\""` | — |
| [SRC-115C2027D9-L000006](../../railway.json#L6) | 6 | `"  },"` | — |
| [SRC-115C2027D9-L000007](../../railway.json#L7) | 7 | `"  \"deploy\": {"` | — |
| [SRC-115C2027D9-L000008](../../railway.json#L8) | 8 | `"    \"startCommand\": \"sh -c 'python -m cli.omarai serve --host 0.0.0.0 --port ${PORT:-8000}'\","` | — |
| [SRC-115C2027D9-L000009](../../railway.json#L9) | 9 | `"    \"healthcheckPath\": \"/api/health\","` | — |
| [SRC-115C2027D9-L000010](../../railway.json#L10) | 10 | `"    \"healthcheckTimeout\": 120,"` | — |
| [SRC-115C2027D9-L000011](../../railway.json#L11) | 11 | `"    \"restartPolicyType\": \"ON_FAILURE\","` | — |
| [SRC-115C2027D9-L000012](../../railway.json#L12) | 12 | `"    \"restartPolicyMaxRetries\": 5"` | — |
| [SRC-115C2027D9-L000013](../../railway.json#L13) | 13 | `"  }"` | — |
| [SRC-115C2027D9-L000014](../../railway.json#L14) | 14 | `"}"` | — |
## وثائق ونصوص

### FILE-B335630551 — [README.md](../../README.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-B335630551-L000001](../../README.md#L1) | 1 | `"# Omarai — Web Research & Generative Q&A Agent"` | — |
| [SRC-B335630551-L000002](../../README.md#L2) | 2 | `""` | — |
| [SRC-B335630551-L000003](../../README.md#L3) | 3 | `"> **Foundational engineering requirements:** mandatory contributor/agent rules are in [AGENTS.md](AGENTS.md). The core architecture and security charter is [OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md](docs/OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md); the expanded platform practices across reliability, security, privacy, data, SRE, AI, accessibility, supply chain, and cost are in [OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md](docs/OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md); and the requirement IDs, expert-review lenses, evidence model, risk priorities, maturity stages, and release gates are in [OMARAI_REQUIREMENTS_TRACEABILITY_AND_MATURITY_MODEL_AR.md](docs/OMARAI_REQUIREMENTS_TRACEABILITY_AND_MATURITY_MODEL_AR.md). The initial foundational requirements checklist is [OMARAI_REQUIREMENTS_REGISTER.md](docs/OMARAI_REQUIREMENTS_REGISTER.md). These documents define required direction; they do not prove every control is implemented or tested."` | — |
| [SRC-B335630551-L000004](../../README.md#L4) | 4 | `""` | — |
| [SRC-B335630551-L000005](../../README.md#L5) | 5 | `"Omarai is an Arabic-first web research agent with a responsive RTL chat UI. You can ask open-ended questions in natural language, search the public web, extract text from accessible pages, compare and summarize findings, ask follow-up questions, and inspect the source links."` | — |
| [SRC-B335630551-L000006](../../README.md#L6) | 6 | `""` | — |
| [SRC-B335630551-L000007](../../README.md#L7) | 7 | `"## What this version does"` | — |
| [SRC-B335630551-L000008](../../README.md#L8) | 8 | `""` | — |
| [SRC-B335630551-L000009](../../README.md#L9) | 9 | `"- Plans up to eight search queries from a natural-language question with a dedicated reasoning/planning model, and uses a deterministic multi-query fallback when the model is unavailable."` | — |
| [SRC-B335630551-L000010](../../README.md#L10) | 10 | `"- Uses separate model roles by default: NVIDIA Nemotron 3 Ultra (free) for query planning and Google Gemma 4 31B Instruct (free) for answer synthesis and the second-pass consistency review; retries with OpenRouter's free-model router if a chosen model fails."` | — |
| [SRC-B335630551-L000011](../../README.md#L11) | 11 | `"- Runs DuckDuckGo HTML and Bing RSS independently for every planned query; can add official Brave Search API and Tavily Search API result indexes when their environment keys are configured; uses Google News RSS for queries judged time-sensitive."` | — |
| [SRC-B335630551-L000012](../../README.md#L12) | 12 | `"- Fuses duplicate results across queries and engines using reciprocal-rank fusion, preserving provider, query, domain, platform, publication-date and page-extraction provenance."` | — |
| [SRC-B335630551-L000013](../../README.md#L13) | 13 | `"- Extracts text from up to eight accessible public pages per question with request-size and timeout bounds, following at most three individually validated public redirects."` | — |
| [SRC-B335630551-L000014](../../README.md#L14) | 14 | ``"- Searches public Reddit RSS and the Bluesky public search endpoint when social discussion is relevant; can use Reddit's OAuth API when `REDDIT_CLIENT_ID` and `REDDIT_CLIENT_SECRET` are provided."`` | — |
| [SRC-B335630551-L000015](../../README.md#L15) | 15 | `"- Searches indexed public pages on Facebook, Instagram, X, TikTok, LinkedIn, Threads and YouTube through the general web engines."` | — |
| [SRC-B335630551-L000016](../../README.md#L16) | 16 | `"- Can use the official Meta Graph API to read posts and a small sample of public comments from explicitly configured Facebook Pages when the token has suitable permissions."` | — |
| [SRC-B335630551-L000017](../../README.md#L17) | 17 | ``"- Can use Instagram Graph API hashtag search to read public hashtag media when `INSTAGRAM_USER_ID` and `INSTAGRAM_ACCESS_TOKEN` have the required permissions. It is not a global Instagram search and has platform quotas."`` | — |
| [SRC-B335630551-L000018](../../README.md#L18) | 18 | ``"- Can use the official X recent-post endpoint when `X_BEARER_TOKEN` is configured and the account/API tier permits the request; can use the official YouTube Data API when `YOUTUBE_API_KEY` is configured."`` | — |
| [SRC-B335630551-L000019](../../README.md#L19) | 19 | `"- Generates an evidence-grounded answer in the user's language, showing source links, query plan, provider coverage, direct page reads, platform mix, source/domain diversity, date coverage, and evidence-coverage warnings. Coverage indicators describe breadth and inspectability; they are not probabilities that the answer is true."` | — |
| [SRC-B335630551-L000020](../../README.md#L20) | 20 | `"- Carries up to eight recent chat messages from the current browser session into follow-up questions."` | — |
| [SRC-B335630551-L000021](../../README.md#L21) | 21 | ``"- Keeps the existing local SQLite lead workspace at `/leads`."`` | — |
| [SRC-B335630551-L000022](../../README.md#L22) | 22 | `"- Binds to loopback by default; it is not a public production deployment."` | — |
| [SRC-B335630551-L000023](../../README.md#L23) | 23 | `""` | — |
| [SRC-B335630551-L000024](../../README.md#L24) | 24 | ``"**Verification semantics:** `GET /api/health` is a configuration/dependency snapshot, not proof that search providers or the model are reachable. Check the `agent.verification_scope` field to see what is and is not verified. Use the protected `POST /api/diagnostics` endpoint for explicit live search/model probes; a passed diagnostic only verifies the specific probes run at that time, not every optional connector or answer quality."`` | — |
| [SRC-B335630551-L000025](../../README.md#L25) | 25 | `""` | — |
| [SRC-B335630551-L000026](../../README.md#L26) | 26 | `"This is a tool-using research agent built around existing language models, not a foundation model trained from scratch. The role-specific defaults aim for more consistent behaviour than using a router that selects a different free model at random on each call. Exact availability and response quality still depend on OpenRouter/provider conditions. **Privacy warning:** the user's question, conversation context and selected web excerpts are sent to the configured external language-model provider for planning/synthesis/review. OpenRouter's NVIDIA Nemotron free endpoint states that session data may be logged for security and product improvement; do not send passwords, API keys, private information or personal/confidential customer data through the free endpoint. See the [NVIDIA Nemotron free-endpoint privacy notice](https://openrouter.ai/nvidia/nemotron-3-ultra-550b-a55b:free). Its language-model planner decides how to search, but query count, URLs and result shapes are validated by deterministic code. Cross-engine agreement improves discovery and ranking but is not independent fact verification. Public social pages that require login, blocked pages and private profiles are not fetched; social search cannot promise complete coverage of any platform. Direct official-platform access varies: Reddit API access requires approved app credentials and is subject to Reddit's terms; Facebook Pages reads require a valid token, page identifiers and correct permissions; Instagram hashtag search requires a professional Instagram account token and the specific supported permissions; X API access requires an authorized bearer token and suitable access; YouTube direct API search requires a Google API key. These APIs do not grant universal access to all content, accounts or comments. Review each platform's terms, quotas and permitted use before using the agent commercially. The agent never bypasses login, paywall or access controls and does not send messages or make automated contact with people."` | — |
| [SRC-B335630551-L000027](../../README.md#L27) | 27 | `""` | — |
| [SRC-B335630551-L000028](../../README.md#L28) | 28 | `""` | — |
| [SRC-B335630551-L000029](../../README.md#L29) | 29 | `"## Living repository index"` | — |
| [SRC-B335630551-L000030](../../README.md#L30) | 30 | `""` | — |
| [SRC-B335630551-L000031](../../README.md#L31) | 31 | `"Omarai maintains a categorized master index and a paginated, line-by-line source index:"` | — |
| [SRC-B335630551-L000032](../../README.md#L32) | 32 | `""` | — |
| [SRC-B335630551-L000033](../../README.md#L33) | 33 | ``"- [MASTER INDEX](docs/MASTER_INDEX.md): file inventory with stable file IDs, Python AST definitions, static frontend/configuration symbols, and explicitly marked TODO/FIXME/BUG/HACK/XXX/REVIEW/SECURITY/DEPRECATED/ISSUE/DEFECT/REGRESSION/RISK/GAP/ERROR/WARNING/PERF/PRIVACY/DATA_LOSS/ACCESSIBILITY entries. Each review marker has an `FND-...` code and a link to the exact source line."`` | — |
| [SRC-B335630551-L000034](../../README.md#L34) | 34 | `"- [SOURCE LINES INDEX](docs/SOURCE_LINES_INDEX.md): search-friendly directory of files, page links, per-file line counts, and links to each source line."` | — |
| [SRC-B335630551-L000035](../../README.md#L35) | 35 | `"- [INDEX COVERAGE AUDIT](docs/INDEX_COVERAGE_AUDIT.md): generated evidence of line-count consistency, metadata-only files, excluded path names and their reasons, and the exact scope of any “100%” coverage statement."` | — |
| [SRC-B335630551-L000036](../../README.md#L36) | 36 | ``"- [Source line pages](docs/source_index/): small generated pages containing every logical line from eligible readable text files. Each line has a `SRC-<FILEHASH>-L000001` code, exact JSON-escaped text, and a link back to the source file at the matching line. Pages are capped at 800 line records to remain navigable on mobile and in GitHub's web view."`` | — |
| [SRC-B335630551-L000037](../../README.md#L37) | 37 | `""` | — |
| [SRC-B335630551-L000038](../../README.md#L38) | 38 | ``"The generator now refuses to publish indexes if any eligible file has missing, duplicated, or misnumbered source-line records. It still cannot infer every unmarked logical/programming defect; known issues should be recorded explicitly with a supported marker (for example, `# BUG: explain the defect`) so the generated `FND-...` register can point to the corresponding `SRC-...` line."`` | — |
| [SRC-B335630551-L000039](../../README.md#L39) | 39 | `""` | — |
| [SRC-B335630551-L000040](../../README.md#L40) | 40 | `"Regenerate and verify the indexes locally:"` | — |
| [SRC-B335630551-L000041](../../README.md#L41) | 41 | `""` | — |
| [SRC-B335630551-L000042](../../README.md#L42) | 42 | ````"```bash"```` | — |
| [SRC-B335630551-L000043](../../README.md#L43) | 43 | `"python docs/generate_index.py"` | — |
| [SRC-B335630551-L000044](../../README.md#L44) | 44 | `"python docs/generate_index.py --check"` | — |
| [SRC-B335630551-L000045](../../README.md#L45) | 45 | ````"```"```` | — |
| [SRC-B335630551-L000046](../../README.md#L46) | 46 | `""` | — |
| [SRC-B335630551-L000047](../../README.md#L47) | 47 | ``"GitHub Actions validates the generator on Python 3.11 and 3.12. The indexing workflow runs on pushes to `main` and the `feat/**`, `fix/**`, and `feature/**` branches. It regenerates and commits all indexes and generated pages only when output changes; obsolete generated pages are removed, while generated-index-only commits are ignored to avoid loops. If direct publication to `main` is rejected, it opens a pull request instead of force-updating a branch or auto-merging."`` | — |
| [SRC-B335630551-L000048](../../README.md#L48) | 48 | `""` | — |
| [SRC-B335630551-L000049](../../README.md#L49) | 49 | ``"When a known code issue is found, add a source comment using one supported marker name (TODO, FIXME, BUG, HACK, XXX, REVIEW, SECURITY, DEPRECATED, ISSUE, DEFECT, REGRESSION, RISK, GAP, ERROR, WARNING, PERF, PRIVACY, DATA_LOSS, or ACCESSIBILITY), followed by a colon and a concise description. The index assigns an `FND-...` code and links it to the exact `SRC-...` source-line record; removing or editing that source annotation updates the generated register on the next index run. Coverage includes every logical line in eligible readable text files up to 2 MiB. Known local secrets, runtime databases, dependency/build directories, binary/unreadable files and oversized files are excluded from line-level indexing by design but listed by metadata where eligible. Static review markers help track explicit findings; no source index can prove that every arbitrary logic bug has been detected or that all code is correct."`` | — |
| [SRC-B335630551-L000050](../../README.md#L50) | 50 | `""` | — |
| [SRC-B335630551-L000051](../../README.md#L51) | 51 | `"## Per-request resource budget"` | — |
| [SRC-B335630551-L000052](../../README.md#L52) | 52 | `""` | — |
| [SRC-B335630551-L000053](../../README.md#L53) | 53 | ``"Each `POST /api/agent` answer includes a `request_budget` object with elapsed and remaining time, reserved resource counts, and configured limits. The current defaults are a 90-second cooperative deadline, at most 8 search queries, 32 provider search calls, 8 model HTTP attempts, 8 page fetches, and up to 3 optional server-side search-tool calls per request. Operator limits may be lowered or raised only within hard caps: `OMARAI_REQUEST_BUDGET_SECONDS` (10–120), `OMARAI_REQUEST_MAX_SEARCH_QUERIES` (1–8), `OMARAI_REQUEST_MAX_SEARCH_CALLS` (1–40), `OMARAI_REQUEST_MAX_MODEL_CALLS` (1–12), `OMARAI_REQUEST_MAX_PAGE_FETCHES` (1–8), and `OMARAI_REQUEST_MAX_TOOL_CALLS` (0–3). Invalid numeric values fall back to the defaults; out-of-range values are clamped."`` | — |
| [SRC-B335630551-L000054](../../README.md#L54) | 54 | `""` | — |
| [SRC-B335630551-L000055](../../README.md#L55) | 55 | `"The deadline caps the timeout passed to outbound operations and prevents new work from being reserved after the deadline or a resource cap is exhausted. It is **cooperative, not hard cancellation**: a network call already in progress may overrun slightly while its client unwinds. Do not interpret this metadata as a load test, a throughput guarantee, or proof that any live provider is reachable. CI tests for budget logic are separate from live-provider validation."` | — |
| [SRC-B335630551-L000056](../../README.md#L56) | 56 | `""` | — |
| [SRC-B335630551-L000057](../../README.md#L57) | 57 | ``"The HTTP API also limits expensive `/api/agent` and `/api/diagnostics` operations to at most 4 concurrent operations per process by default. Configure `OMARAI_MAX_CONCURRENT_AGENT_REQUESTS` from 1 to 8. If all slots are occupied, the API returns HTTP 503 with a short retry hint instead of queueing unlimited expensive work. This is a **process-local** cap, not a distributed semaphore across multiple workers or replicas, and it is not a throughput/load-test claim."`` | — |
| [SRC-B335630551-L000058](../../README.md#L58) | 58 | `""` | — |
| [SRC-B335630551-L000059](../../README.md#L59) | 59 | `"## Experimental DeepSeek Search provider"` | — |
| [SRC-B335630551-L000060](../../README.md#L60) | 60 | `""` | — |
| [SRC-B335630551-L000061](../../README.md#L61) | 61 | `"Omarai can optionally compare results from DeepSeek's Search API when"` | — |
| [SRC-B335630551-L000062](../../README.md#L62) | 62 | ``"`DEEPSEEK_SEARCH_API_KEY` is configured in the host's secret settings. It is"`` | — |
| [SRC-B335630551-L000063](../../README.md#L63) | 63 | `"**disabled by default**; DuckDuckGo and Bing remain configured as before."` | — |
| [SRC-B335630551-L000064](../../README.md#L64) | 64 | `"To limit possible spend when opted in, the request budget defaults to **one"` | — |
| [SRC-B335630551-L000065](../../README.md#L65) | 65 | `"DeepSeek Search call per answer/diagnostic operation**. It can be set from 0 to 3"` | — |
| [SRC-B335630551-L000066](../../README.md#L66) | 66 | ``"using `OMARAI_DEEPSEEK_SEARCH_REQUEST_BUDGET`; invalid values fall back to 1."`` | — |
| [SRC-B335630551-L000067](../../README.md#L67) | 67 | `"DeepSeek Search is billed per successful request (currently documented at"` | — |
| [SRC-B335630551-L000068](../../README.md#L68) | 68 | `"US$0.75 per 1,000 successful searches); review the"` | — |
| [SRC-B335630551-L000069](../../README.md#L69) | 69 | `"[official Search & Fetch guide](https://api-docs.deepseek.com/guides/search/)"` | — |
| [SRC-B335630551-L000070](../../README.md#L70) | 70 | `"before enabling it. Unit tests use a mocked response; this repository change"` | — |
| [SRC-B335630551-L000071](../../README.md#L71) | 71 | `"does not claim live DeepSeek connectivity or answer-quality improvement."` | — |
| [SRC-B335630551-L000072](../../README.md#L72) | 72 | `""` | — |
| [SRC-B335630551-L000073](../../README.md#L73) | 73 | `"## Hosted deployment"` | — |
| [SRC-B335630551-L000074](../../README.md#L74) | 74 | `""` | — |
| [SRC-B335630551-L000075](../../README.md#L75) | 75 | `"A Dockerfile and Railway configuration are included for a public hosted instance. This is **deployment-ready configuration, not proof that a hosted service has already been created**: you must connect your Railway account to this GitHub repository, add secrets in the host dashboard, deploy, and run the live diagnostics."` | — |
| [SRC-B335630551-L000076](../../README.md#L76) | 76 | `""` | — |
| [SRC-B335630551-L000077](../../README.md#L77) | 77 | ``"Before public binding, set `OMARAI_PUBLIC_DEPLOYMENT=1` and a separate random `OMARAI_ACCESS_TOKEN` of at least 32 characters. The app refuses public binding without both. Set `OPENROUTER_API_KEY` in the hosting provider's secret variables for natural-language planning and synthesis. If the browser UI is served from a different origin, set `OMARAI_ALLOWED_ORIGINS` to a comma-separated allowlist of trusted origins (scheme + host + optional port, no path and no `*`). The API sends CORS headers only to allowed origins and handles preflight `OPTIONS`; when you open `/` on the same deployed service, the built-in UI uses relative `/api/...` URLs and normally needs no extra origin entry. Public API routes require the bearer token and have a default in-memory limit of 20 requests per minute per client IP. The Arabic UI provides a separate access-token field; it stores only that app token in the browser's local storage, not the provider API key."`` | — |
| [SRC-B335630551-L000078](../../README.md#L78) | 78 | `""` | — |
| [SRC-B335630551-L000079](../../README.md#L79) | 79 | ``"See the step-by-step Arabic instructions in `docs/DEPLOY_RAILWAY_AR.md`. Before treating a deployment as accepted, follow the [hosted go-live checklist](docs/GO_LIVE_CHECKLIST_AR.md) and run the manually triggered [hosted acceptance smoke workflow](.github/workflows/hosted-smoke.yml) after configuring the GitHub Actions secrets `OMARAI_ACCESS_TOKEN` and `OMARAI_BASE_URL` (the latter must be only the service's HTTPS origin). The workflow uses that administrator-configured target rather than accepting a free-form URL alongside a secret, preventing accidental or unauthorized token disclosure to arbitrary hosts. It makes real model/search requests and may incur usage charges. SQLite on ephemeral hosting is not durable storage for customer records; do not treat the lead workspace as persistent until a managed database and backups are configured."`` | — |
| [SRC-B335630551-L000080](../../README.md#L80) | 80 | `""` | — |
| [SRC-B335630551-L000081](../../README.md#L81) | 81 | `"## Free hosted deployment (SnapDeploy)"` | — |
| [SRC-B335630551-L000082](../../README.md#L82) | 82 | `""` | — |
| [SRC-B335630551-L000083](../../README.md#L83) | 83 | `"For a free alternative when Render does not work, see the step-by-step Arabic [SnapDeploy guide](docs/DEPLOY_SNAPDEPLOY_AR.md). SnapDeploy's published free tier currently has monthly container-hour limits, sleeps after inactivity, and does not provide persistent disk storage. Treat it as a demo/acceptance-test host, not durable production hosting. Confirm the current limits and charges before deploying."` | — |
| [SRC-B335630551-L000084](../../README.md#L84) | 84 | `""` | — |
| [SRC-B335630551-L000085](../../README.md#L85) | 85 | ``"The guide covers GitHub linking, `main`, the Dockerfile, runtime secrets, HTTPS, live health/model/search tests, and the limitations of the existing SQLite lead workspace. No hosted service is created automatically by this repository."`` | — |
| [SRC-B335630551-L000086](../../README.md#L86) | 86 | `""` | — |
| [SRC-B335630551-L000087](../../README.md#L87) | 87 | `"## Free hosted deployment (Render)"` | — |
| [SRC-B335630551-L000088](../../README.md#L88) | 88 | `""` | — |
| [SRC-B335630551-L000089](../../README.md#L89) | 89 | ``"A starter Render Blueprint is included in `render.yaml`, with Arabic setup notes in [docs/DEPLOY_RENDER_AR.md](docs/DEPLOY_RENDER_AR.md). The free service sleeps after inactivity and has an ephemeral filesystem; do not rely on the hosted SQLite lead database for durable storage. This is intended for a personal demo and acceptance testing, not production availability."`` | — |
| [SRC-B335630551-L000090](../../README.md#L90) | 90 | `""` | — |
| [SRC-B335630551-L000091](../../README.md#L91) | 91 | `"Before accepting the deployment, use the [Arabic go-live checklist](docs/GO_LIVE_CHECKLIST_AR.md) when that file is present on the selected branch. Never commit provider keys or the app access token."` | — |
| [SRC-B335630551-L000092](../../README.md#L92) | 92 | `""` | — |
| [SRC-B335630551-L000093](../../README.md#L93) | 93 | `"## Run on Android / Termux"` | — |
| [SRC-B335630551-L000094](../../README.md#L94) | 94 | `""` | — |
| [SRC-B335630551-L000095](../../README.md#L95) | 95 | `"From the repository directory:"` | — |
| [SRC-B335630551-L000096](../../README.md#L96) | 96 | `""` | — |
| [SRC-B335630551-L000097](../../README.md#L97) | 97 | ````"```bash"```` | — |
| [SRC-B335630551-L000098](../../README.md#L98) | 98 | `"python -m pip install -e ."` | — |
| [SRC-B335630551-L000099](../../README.md#L99) | 99 | ````"```"```` | — |
| [SRC-B335630551-L000100](../../README.md#L100) | 100 | `""` | — |
| [SRC-B335630551-L000101](../../README.md#L101) | 101 | ``"The default language-model configuration uses OpenRouter: Nemotron 3 Ultra (free) plans queries, Gemma 4 31B Instruct (free) writes the answer and performs the optional second-pass review, and `openrouter/free` is the fallback if a selected model fails. Create an OpenRouter API key, then enter it without putting the secret into a command-history entry. The model key enables both search planning and generative synthesis; general web search can still run without it, but results will not be turned into a full language-model analysis:"`` | — |
| [SRC-B335630551-L000102](../../README.md#L102) | 102 | `""` | — |
| [SRC-B335630551-L000103](../../README.md#L103) | 103 | ````"```bash"```` | — |
| [SRC-B335630551-L000104](../../README.md#L104) | 104 | `"read -r -s -p \"OpenRouter API key: \" OPENROUTER_API_KEY"` | — |
| [SRC-B335630551-L000105](../../README.md#L105) | 105 | `"printf '\\n'"` | — |
| [SRC-B335630551-L000106](../../README.md#L106) | 106 | `"export OPENROUTER_API_KEY"` | — |
| [SRC-B335630551-L000107](../../README.md#L107) | 107 | `"python -m cli.omarai serve"` | — |
| [SRC-B335630551-L000108](../../README.md#L108) | 108 | ````"```"```` | — |
| [SRC-B335630551-L000109](../../README.md#L109) | 109 | `""` | — |
| [SRC-B335630551-L000110](../../README.md#L110) | 110 | `"Keep this Termux session running and open **http://127.0.0.1:8765** in the phone's browser. The agent chat is the home screen. The existing lead workspace remains available at **http://127.0.0.1:8765/leads**."` | — |
| [SRC-B335630551-L000111](../../README.md#L111) | 111 | `""` | — |
| [SRC-B335630551-L000112](../../README.md#L112) | 112 | `"The key is held in the current shell environment and is not written into the repository. Enter it again in a new Termux session. Never commit API keys or paste them into public issues or chat."` | — |
| [SRC-B335630551-L000113](../../README.md#L113) | 113 | `""` | — |
| [SRC-B335630551-L000114](../../README.md#L114) | 114 | `"### Optional configuration"` | — |
| [SRC-B335630551-L000115](../../README.md#L115) | 115 | `""` | — |
| [SRC-B335630551-L000116](../../README.md#L116) | 116 | `"For additional live web-search indexes, configure either official search API. These keys are optional: the built-in public engines are still attempted, and each API may have its own account, quota, rate limit or cost. Do not assume an API is free or that a configured key is valid until you run the live diagnostics."` | — |
| [SRC-B335630551-L000117](../../README.md#L117) | 117 | `""` | — |
| [SRC-B335630551-L000118](../../README.md#L118) | 118 | ````"```bash"```` | — |
| [SRC-B335630551-L000119](../../README.md#L119) | 119 | `"read -r -s -p \"Brave Search API key: \" BRAVE_SEARCH_API_KEY; printf '\\\\n'; export BRAVE_SEARCH_API_KEY"` | — |
| [SRC-B335630551-L000120](../../README.md#L120) | 120 | `"read -r -s -p \"Tavily API key: \" TAVILY_API_KEY; printf '\\\\n'; export TAVILY_API_KEY"` | — |
| [SRC-B335630551-L000121](../../README.md#L121) | 121 | ````"```"```` | — |
| [SRC-B335630551-L000122](../../README.md#L122) | 122 | `""` | — |
| [SRC-B335630551-L000123](../../README.md#L123) | 123 | `""` | — |
| [SRC-B335630551-L000124](../../README.md#L124) | 124 | `"For a different OpenAI-compatible endpoint or model, set these environment variables before starting the server:"` | — |
| [SRC-B335630551-L000125](../../README.md#L125) | 125 | `""` | — |
| [SRC-B335630551-L000126](../../README.md#L126) | 126 | ````"```bash"```` | — |
| [SRC-B335630551-L000127](../../README.md#L127) | 127 | `"export OMARAI_LLM_BASE_URL=\"https://openrouter.ai/api/v1\""` | — |
| [SRC-B335630551-L000128](../../README.md#L128) | 128 | `"export OMARAI_LLM_MODEL=\"openrouter/free\""` | — |
| [SRC-B335630551-L000129](../../README.md#L129) | 129 | ````"```"```` | — |
| [SRC-B335630551-L000130](../../README.md#L130) | 130 | `""` | — |
| [SRC-B335630551-L000131](../../README.md#L131) | 131 | ``"Use `OMARAI_LLM_API_KEY` instead of `OPENROUTER_API_KEY` when you want a separate environment variable. `OMARAI_LLM_TIMEOUT` accepts a timeout in seconds from 5 to 60. To customize model roles, set `OMARAI_PLANNER_MODEL`, `OMARAI_ANSWER_MODEL`, and/or `OMARAI_REVIEW_MODEL`; `OMARAI_LLM_MODEL` remains a global override for all roles that have no role-specific override. `OMARAI_LLM_FALLBACK_MODEL` changes the default `openrouter/free` fallback. Provider pricing, model availability and rate limits can change; check the chosen provider before using a paid model. Optional social credentials may be configured in the same Termux session before starting the server: `REDDIT_CLIENT_ID` + `REDDIT_CLIENT_SECRET` (official OAuth access), `X_BEARER_TOKEN`, `YOUTUBE_API_KEY`, `INSTAGRAM_USER_ID` + `INSTAGRAM_ACCESS_TOKEN` + optional `META_GRAPH_VERSION`, and `FACEBOOK_PAGE_ACCESS_TOKEN` + `FACEBOOK_PAGE_IDS` (comma-separated Page IDs that the authorized token can access). Use `read -r -s` to enter secrets privately rather than saving them in shell history. Do not store keys in source files, HTML, commits or chat messages."`` | — |
| [SRC-B335630551-L000132](../../README.md#L132) | 132 | `""` | — |
| [SRC-B335630551-L000133](../../README.md#L133) | 133 | `"If no language-model key is configured, Omarai can still attempt web search and show source snippets, but it cannot provide the full generative understanding/synthesis layer. If search providers are temporarily unavailable, the agent reports the limitation rather than pretending that a search succeeded."` | — |
| [SRC-B335630551-L000134](../../README.md#L134) | 134 | `""` | — |
| [SRC-B335630551-L000135](../../README.md#L135) | 135 | `"For the platform boundaries, optional credentials and safe Termux setup for social connectors, see the [Arabic research connectors guide](docs/RESEARCH_CONNECTORS_AR.md)."` | — |
| [SRC-B335630551-L000136](../../README.md#L136) | 136 | `""` | — |
| [SRC-B335630551-L000137](../../README.md#L137) | 137 | `"## API"` | — |
| [SRC-B335630551-L000138](../../README.md#L138) | 138 | `""` | — |
| [SRC-B335630551-L000139](../../README.md#L139) | 139 | ``"- `GET /` — web-research chat"`` | — |
| [SRC-B335630551-L000140](../../README.md#L140) | 140 | ``"- `GET /leads` — existing lead workspace"`` | — |
| [SRC-B335630551-L000141](../../README.md#L141) | 141 | ``"- `GET /api/health` — setup and dependency status (never returns the API key)"`` | — |
| [SRC-B335630551-L000142](../../README.md#L142) | 142 | ``"- `POST /api/diagnostics` — opt-in live checks for web search and the language model; set `test_social: true` to also probe public/authorized social connectors"`` | — |
| [SRC-B335630551-L000143](../../README.md#L143) | 143 | ``"- `POST /api/agent` — open-ended question plus optional recent `history`"`` | — |
| [SRC-B335630551-L000144](../../README.md#L144) | 144 | ``"- `POST /api/analyze` — existing rule-based lead-text assessment"`` | — |
| [SRC-B335630551-L000145](../../README.md#L145) | 145 | ``"- `GET/POST /api/leads` — existing local lead records"`` | — |
| [SRC-B335630551-L000146](../../README.md#L146) | 146 | `""` | — |
| [SRC-B335630551-L000147](../../README.md#L147) | 147 | `"Example request:"` | — |
| [SRC-B335630551-L000148](../../README.md#L148) | 148 | `""` | — |
| [SRC-B335630551-L000149](../../README.md#L149) | 149 | ````"```json"```` | — |
| [SRC-B335630551-L000150](../../README.md#L150) | 150 | `"{"` | — |
| [SRC-B335630551-L000151](../../README.md#L151) | 151 | `"  \"question\": \"Compare the latest public information about two technologies\","` | — |
| [SRC-B335630551-L000152](../../README.md#L152) | 152 | `"  \"history\": []"` | — |
| [SRC-B335630551-L000153](../../README.md#L153) | 153 | `"}"` | — |
| [SRC-B335630551-L000154](../../README.md#L154) | 154 | ````"```"```` | — |
| [SRC-B335630551-L000155](../../README.md#L155) | 155 | `""` | — |
| [SRC-B335630551-L000156](../../README.md#L156) | 156 | ``"The `/api/diagnostics` response reports pass/fail/degraded states, returned result counts, provider counts, elapsed time, and the model that actually answered (including fallback use). The Arabic web UI offers automatic, deep, latest-information, and public-social research modes, plus a live-test button. The model check sends one small completion request; optional social checks perform real public/API requests and can take longer. The response from `/api/agent` includes `answer`, `sources`, `search_queries`, `research_plan`, `search_report`, `used_web_search`, `used_social_search`, `used_language_model`, and any warnings. The request can pass `mode` as `auto`, `deep`, `latest`, or `social`. The report records planned and attempted queries, unique result count, pages read, providers, platform breakdown, citation-range checks and whether an optional second-pass consistency review completed. That second pass uses the same configured model/provider and is not independent fact verification. URL syntax and resolved private/local addresses are checked before page fetches; public redirects are followed only through a small bounded loop with each destination revalidated. Search engines may still return inaccessible, stale or noisy results, which the agent must disclose."`` | — |
| [SRC-B335630551-L000157](../../README.md#L157) | 157 | `""` | — |
| [SRC-B335630551-L000158](../../README.md#L158) | 158 | `"## Existing lead workspace"` | — |
| [SRC-B335630551-L000159](../../README.md#L159) | 159 | `""` | — |
| [SRC-B335630551-L000160](../../README.md#L160) | 160 | ``"The previous local lead-intent tool is preserved at `/leads`. It stores data locally in `~/.omarai/omarai.sqlite3`. Its transparent rule score is not a statistical probability of a purchase. Process only public/authorized data, minimize personal information, and manually review business decisions."`` | — |
| [SRC-B335630551-L000161](../../README.md#L161) | 161 | `""` | — |
| [SRC-B335630551-L000162](../../README.md#L162) | 162 | `"Analyze text from the CLI:"` | — |
| [SRC-B335630551-L000163](../../README.md#L163) | 163 | `""` | — |
| [SRC-B335630551-L000164](../../README.md#L164) | 164 | ````"```bash"```` | — |
| [SRC-B335630551-L000165](../../README.md#L165) | 165 | `"python -m cli.omarai analyze --text \"بدور على شقة في التجمع الخامس وممكن معاينة\" --product \"شقة,عقار\" --location \"التجمع الخامس\""` | — |
| [SRC-B335630551-L000166](../../README.md#L166) | 166 | ````"```"```` | — |
| [SRC-B335630551-L000167](../../README.md#L167) | 167 | `""` | — |
| [SRC-B335630551-L000168](../../README.md#L168) | 168 | ``"CSV import requires `text,source_url,platform` columns:"`` | — |
| [SRC-B335630551-L000169](../../README.md#L169) | 169 | `""` | — |
| [SRC-B335630551-L000170](../../README.md#L170) | 170 | ````"```bash"```` | — |
| [SRC-B335630551-L000171](../../README.md#L171) | 171 | `"python -m cli.omarai import-csv --file leads.csv"` | — |
| [SRC-B335630551-L000172](../../README.md#L172) | 172 | `"python -m cli.omarai list --limit 50"` | — |
| [SRC-B335630551-L000173](../../README.md#L173) | 173 | `"python -m cli.omarai export-csv --file leads-export.csv"` | — |
| [SRC-B335630551-L000174](../../README.md#L174) | 174 | ````"```"```` | — |
| [SRC-B335630551-L000175](../../README.md#L175) | 175 | `""` | — |
| [SRC-B335630551-L000176](../../README.md#L176) | 176 | `"## Checks"` | — |
| [SRC-B335630551-L000177](../../README.md#L177) | 177 | `""` | — |
| [SRC-B335630551-L000178](../../README.md#L178) | 178 | ````"```bash"```` | — |
| [SRC-B335630551-L000179](../../README.md#L179) | 179 | `"python -m pip install -e \".[dev]\""` | — |
| [SRC-B335630551-L000180](../../README.md#L180) | 180 | `"ruff check agents api cli tests"` | — |
| [SRC-B335630551-L000181](../../README.md#L181) | 181 | `"python -m pytest -q"` | — |
| [SRC-B335630551-L000182](../../README.md#L182) | 182 | ````"```"```` | — |
## إعدادات وتشغيل

### FILE-A64CF250B4 — [render.yaml](../../render.yaml#L1)

- النوع: **YAML**
- نطاق الفهرسة: جرد الملف + مفاتيح إعداد ساكنة

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-A64CF250B4-L000001](../../render.yaml#L1) | 1 | `"services:"` | — |
| [SRC-A64CF250B4-L000002](../../render.yaml#L2) | 2 | `"  - type: web"` | — |
| [SRC-A64CF250B4-L000003](../../render.yaml#L3) | 3 | `"    name: omarai"` | — |
| [SRC-A64CF250B4-L000004](../../render.yaml#L4) | 4 | `"    runtime: docker"` | — |
| [SRC-A64CF250B4-L000005](../../render.yaml#L5) | 5 | `"    plan: free"` | — |
| [SRC-A64CF250B4-L000006](../../render.yaml#L6) | 6 | `"    region: frankfurt"` | — |
| [SRC-A64CF250B4-L000007](../../render.yaml#L7) | 7 | `"    dockerfilePath: ./Dockerfile"` | — |
| [SRC-A64CF250B4-L000008](../../render.yaml#L8) | 8 | `"    healthCheckPath: /api/health"` | — |
| [SRC-A64CF250B4-L000009](../../render.yaml#L9) | 9 | `"    envVars:"` | — |
| [SRC-A64CF250B4-L000010](../../render.yaml#L10) | 10 | `"      - key: OMARAI_PUBLIC_DEPLOYMENT"` | — |
| [SRC-A64CF250B4-L000011](../../render.yaml#L11) | 11 | `"        value: \"1\""` | — |
| [SRC-A64CF250B4-L000012](../../render.yaml#L12) | 12 | `"      - key: OMARAI_ACCESS_TOKEN"` | — |
| [SRC-A64CF250B4-L000013](../../render.yaml#L13) | 13 | `"        sync: false"` | — |
| [SRC-A64CF250B4-L000014](../../render.yaml#L14) | 14 | `"      - key: OPENROUTER_API_KEY"` | — |
| [SRC-A64CF250B4-L000015](../../render.yaml#L15) | 15 | `"        sync: false"` | — |
## ملفات أخرى

### FILE-64EDD7FC2B — [scripts/__init__.py](../../scripts/__init__.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-64EDD7FC2B-L000001](../../scripts/__init__.py#L1) | 1 | `"\"\"\"Operational helper scripts for Omarai.\"\"\""` | — |
## ملفات أخرى

### FILE-A8360B1B03 — [scripts/hosted_smoke_test.py](../../scripts/hosted_smoke_test.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-A8360B1B03-L000001](../../scripts/hosted_smoke_test.py#L1) | 1 | `"#!/usr/bin/env python3"` | — |
| [SRC-A8360B1B03-L000002](../../scripts/hosted_smoke_test.py#L2) | 2 | `"\"\"\"End-to-end smoke test for a deployed Omarai instance; uses only stdlib.\"\"\""` | — |
| [SRC-A8360B1B03-L000003](../../scripts/hosted_smoke_test.py#L3) | 3 | `"from __future__ import annotations"` | — |
| [SRC-A8360B1B03-L000004](../../scripts/hosted_smoke_test.py#L4) | 4 | `""` | — |
| [SRC-A8360B1B03-L000005](../../scripts/hosted_smoke_test.py#L5) | 5 | `"import argparse"` | — |
| [SRC-A8360B1B03-L000006](../../scripts/hosted_smoke_test.py#L6) | 6 | `"import json"` | — |
| [SRC-A8360B1B03-L000007](../../scripts/hosted_smoke_test.py#L7) | 7 | `"import os"` | — |
| [SRC-A8360B1B03-L000008](../../scripts/hosted_smoke_test.py#L8) | 8 | `"import sys"` | — |
| [SRC-A8360B1B03-L000009](../../scripts/hosted_smoke_test.py#L9) | 9 | `"import urllib.error"` | — |
| [SRC-A8360B1B03-L000010](../../scripts/hosted_smoke_test.py#L10) | 10 | `"import urllib.parse"` | — |
| [SRC-A8360B1B03-L000011](../../scripts/hosted_smoke_test.py#L11) | 11 | `"import urllib.request"` | — |
| [SRC-A8360B1B03-L000012](../../scripts/hosted_smoke_test.py#L12) | 12 | `"from typing import Any"` | — |
| [SRC-A8360B1B03-L000013](../../scripts/hosted_smoke_test.py#L13) | 13 | `""` | — |
| [SRC-A8360B1B03-L000014](../../scripts/hosted_smoke_test.py#L14) | 14 | `""` | — |
| [SRC-A8360B1B03-L000015](../../scripts/hosted_smoke_test.py#L15) | 15 | `"class SmokeError(RuntimeError):"` | — |
| [SRC-A8360B1B03-L000016](../../scripts/hosted_smoke_test.py#L16) | 16 | `"    \"\"\"A live acceptance check failed.\"\"\""` | — |
| [SRC-A8360B1B03-L000017](../../scripts/hosted_smoke_test.py#L17) | 17 | `""` | — |
| [SRC-A8360B1B03-L000018](../../scripts/hosted_smoke_test.py#L18) | 18 | `""` | — |
| [SRC-A8360B1B03-L000019](../../scripts/hosted_smoke_test.py#L19) | 19 | `"class _SameOriginRedirectHandler(urllib.request.HTTPRedirectHandler):"` | — |
| [SRC-A8360B1B03-L000020](../../scripts/hosted_smoke_test.py#L20) | 20 | `"    \"\"\"Never forward a bearer token to a different origin during an HTTP redirect.\"\"\""` | — |
| [SRC-A8360B1B03-L000021](../../scripts/hosted_smoke_test.py#L21) | 21 | `""` | — |
| [SRC-A8360B1B03-L000022](../../scripts/hosted_smoke_test.py#L22) | 22 | `"    @staticmethod"` | — |
| [SRC-A8360B1B03-L000023](../../scripts/hosted_smoke_test.py#L23) | 23 | `"    def _origin(url: str) -> tuple[str, str, int \| None]:"` | — |
| [SRC-A8360B1B03-L000024](../../scripts/hosted_smoke_test.py#L24) | 24 | `"        parsed = urllib.parse.urlsplit(url)"` | — |
| [SRC-A8360B1B03-L000025](../../scripts/hosted_smoke_test.py#L25) | 25 | `"        try:"` | — |
| [SRC-A8360B1B03-L000026](../../scripts/hosted_smoke_test.py#L26) | 26 | `"            port = parsed.port"` | — |
| [SRC-A8360B1B03-L000027](../../scripts/hosted_smoke_test.py#L27) | 27 | `"        except ValueError:"` | — |
| [SRC-A8360B1B03-L000028](../../scripts/hosted_smoke_test.py#L28) | 28 | `"            return \"\", \"\", None"` | — |
| [SRC-A8360B1B03-L000029](../../scripts/hosted_smoke_test.py#L29) | 29 | `"        if port is None:"` | — |
| [SRC-A8360B1B03-L000030](../../scripts/hosted_smoke_test.py#L30) | 30 | `"            port = 443 if parsed.scheme.lower() == \"https\" else 80 if parsed.scheme.lower() == \"http\" else None"` | — |
| [SRC-A8360B1B03-L000031](../../scripts/hosted_smoke_test.py#L31) | 31 | `"        return parsed.scheme.lower(), (parsed.hostname or \"\").lower(), port"` | — |
| [SRC-A8360B1B03-L000032](../../scripts/hosted_smoke_test.py#L32) | 32 | `""` | — |
| [SRC-A8360B1B03-L000033](../../scripts/hosted_smoke_test.py#L33) | 33 | `"    def redirect_request(self, req, fp, code, msg, headers, newurl):"` | — |
| [SRC-A8360B1B03-L000034](../../scripts/hosted_smoke_test.py#L34) | 34 | `"        target_url = urllib.parse.urljoin(req.full_url, newurl)"` | — |
| [SRC-A8360B1B03-L000035](../../scripts/hosted_smoke_test.py#L35) | 35 | `"        target = urllib.parse.urlsplit(target_url)"` | — |
| [SRC-A8360B1B03-L000036](../../scripts/hosted_smoke_test.py#L36) | 36 | `"        if ("` | — |
| [SRC-A8360B1B03-L000037](../../scripts/hosted_smoke_test.py#L37) | 37 | `"            self._origin(req.full_url) != self._origin(target_url)"` | — |
| [SRC-A8360B1B03-L000038](../../scripts/hosted_smoke_test.py#L38) | 38 | `"            or target.scheme.lower() not in {\"http\", \"https\"}"` | — |
| [SRC-A8360B1B03-L000039](../../scripts/hosted_smoke_test.py#L39) | 39 | `"            or target.username"` | — |
| [SRC-A8360B1B03-L000040](../../scripts/hosted_smoke_test.py#L40) | 40 | `"            or target.password"` | — |
| [SRC-A8360B1B03-L000041](../../scripts/hosted_smoke_test.py#L41) | 41 | `"        ):"` | — |
| [SRC-A8360B1B03-L000042](../../scripts/hosted_smoke_test.py#L42) | 42 | `"            raise urllib.error.HTTPError("` | — |
| [SRC-A8360B1B03-L000043](../../scripts/hosted_smoke_test.py#L43) | 43 | `"                req.full_url, code, \"Cross-origin redirect blocked\", headers, fp"` | — |
| [SRC-A8360B1B03-L000044](../../scripts/hosted_smoke_test.py#L44) | 44 | `"            )"` | — |
| [SRC-A8360B1B03-L000045](../../scripts/hosted_smoke_test.py#L45) | 45 | `"        return super().redirect_request(req, fp, code, msg, headers, target_url)"` | — |
| [SRC-A8360B1B03-L000046](../../scripts/hosted_smoke_test.py#L46) | 46 | `""` | — |
| [SRC-A8360B1B03-L000047](../../scripts/hosted_smoke_test.py#L47) | 47 | `""` | — |
| [SRC-A8360B1B03-L000048](../../scripts/hosted_smoke_test.py#L48) | 48 | `"def normalize_origin(value: str, allow_http: bool = False) -> str:"` | — |
| [SRC-A8360B1B03-L000049](../../scripts/hosted_smoke_test.py#L49) | 49 | `"    parsed = urllib.parse.urlsplit((value or \"\").strip())"` | — |
