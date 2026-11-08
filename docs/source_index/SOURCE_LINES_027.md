# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **027**
- سجلات الأسطر: **800**
- النطاق: SRC-C8EA754D73-L000097 إلى SRC-E73001D9AC-L000391
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## وثائق وفهرسة

### FILE-C8EA754D73 — [docs/IMPLEMENTATION_SCOPE.md](../IMPLEMENTATION_SCOPE.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-C8EA754D73-L000097](../IMPLEMENTATION_SCOPE.md#L97) | 97 | `"- قواعد المساهمة وتنظيم المستودع: [AGENTS.md](../AGENTS.md) و[دليل الوثائق](README.md)."` | — |
| [SRC-C8EA754D73-L000098](../IMPLEMENTATION_SCOPE.md#L98) | 98 | `""` | — |
| [SRC-C8EA754D73-L000099](../IMPLEMENTATION_SCOPE.md#L99) | 99 | ``"لا تُرقَّ حالة إلى `VERIFIED` دون اختبار محدد على SHA/بيئة واضحة. لا تُحوَّل `NOT_RUN` أو `UNKNOWN` إلى نجاح لمجرد وجود كود أو إعداد أو ملف توثيق."`` | — |
| [SRC-C8EA754D73-L000100](../IMPLEMENTATION_SCOPE.md#L100) | 100 | `""` | — |
| [SRC-C8EA754D73-L000101](../IMPLEMENTATION_SCOPE.md#L101) | 101 | `"## اعتماد الاتجاه البصري — 4 نوفمبر 2026"` | — |
| [SRC-C8EA754D73-L000102](../IMPLEMENTATION_SCOPE.md#L102) | 102 | `""` | — |
| [SRC-C8EA754D73-L000103](../IMPLEMENTATION_SCOPE.md#L103) | 103 | ``"- **VERIFIED:** اعتمد المدير البشري اتجاه **03 — Neon Command** من مقترحات `docs/ui-directions/`، وتم تطبيق لغة الألوان والحواف المضيئة والأسطح الزجاجية الداكنة على `web/workspace.html` في فرع PR #151."`` | — |
| [SRC-C8EA754D73-L000104](../IMPLEMENTATION_SCOPE.md#L104) | 104 | `"- **VERIFIED:** حافظت الواجهة على تكاملات API الموجودة في الفرع؛ التغيير البصري لا يضيف موفرات أو اتصالات خارجية."` | — |
| [SRC-C8EA754D73-L000105](../IMPLEMENTATION_SCOPE.md#L105) | 105 | ``"- **VERIFIED في المصدر / NOT_RUN في المتصفح:** توجد قواعد responsive عند 1100/760/420px، وأهداف لمس أساسية على الهاتف، و`prefers-reduced-motion` و`forced-colors`. لم يُنفذ اختبار بصري فعلي عبر أجهزة/متصفحات بعد."`` | — |
| [SRC-C8EA754D73-L000106](../IMPLEMENTATION_SCOPE.md#L106) | 106 | `"- **NOT_RUN:** أضيف اختبار انحدار يثبت وجود tokens والـbreakpoints وميزات الوصولية؛ ينتظر CI."` | — |
| [SRC-C8EA754D73-L000107](../IMPLEMENTATION_SCOPE.md#L107) | 107 | `"- **NOT_DEPLOYED:** لا دمج ولا نشر. PR #151 هو مسار المراجعة والتنفيذ، وPR #152 يبقى مقترحات الاتجاهات الثلاثة منفصلًا."` | — |
## وثائق وفهرسة

### FILE-53E640B937 — [docs/OMARAI_AGENTIC_RAG_ROADMAP_AR.md](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-53E640B937-L000001](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L1) | 1 | `"# خطة تنفيذ RAG الوكيلي وسلامة الأدلة في Omarai"` | — |
| [SRC-53E640B937-L000002](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L2) | 2 | `""` | — |
| [SRC-53E640B937-L000003](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L3) | 3 | ``"**تاريخ الحالة:** 28 أكتوبر 2026. يبدأ هذا العمل من رأس `main` بعد دمج PR #113. نجاح الاختبارات الآلية لا يُعد قبولًا حيًا ولا إثباتًا لصحة الإجابات."`` | — |
| [SRC-53E640B937-L000004](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L4) | 4 | `""` | — |
| [SRC-53E640B937-L000005](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L5) | 5 | `"## تعريف النظام المستهدف"` | — |
| [SRC-53E640B937-L000006](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L6) | 6 | `""` | — |
| [SRC-53E640B937-L000007](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L7) | 7 | `"يستقبل Omarai سؤالًا، يحدد المقصد والسياق، يقرر الحاجة إلى الاسترجاع، يفكك الطلب المركب إلى محاور، يخطط لاستعلامات محدودة، يسترجع مصادر عامة آمنة أو معرفة محلية متاحة، يقرأ الصفحات، يربط المقاطع المرشحة بالاستشهادات، يصوغ الإجابة ويراجعها، ثم يكشف النقص أو يمتنع عنه. يجب أن تبقى هذه المراحل قابلة للفحص ومحدودة الزمن والموارد."` | — |
| [SRC-53E640B937-L000008](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L8) | 8 | `""` | — |
| [SRC-53E640B937-L000009](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L9) | 9 | `"## سجل البنود وحالتها"` | — |
| [SRC-53E640B937-L000010](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L10) | 10 | `""` | — |
| [SRC-53E640B937-L000011](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L11) | 11 | `"\| البند \| الحالة \| الدليل والحد المتبقي \|"` | — |
| [SRC-53E640B937-L000012](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L12) | 12 | `"\|---\|---\|---\|"` | — |
| [SRC-53E640B937-L000013](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L13) | 13 | ``"\| نموذج لغوي داخل غلاف تنفيذي \| **PARTIAL** \| `WebAgent` يضبط المهلة والميزانية والتشخيصات. وجود الاعتماديات لا يثبت أن مزود النموذج حي. \|"`` | — |
| [SRC-53E640B937-L000014](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L14) | 14 | ``"\| فهم المقصد والمتابعة والسياق \| **FIXED_AND_TESTED ضمن نطاق CI** \| `intent_router.py` و`dialogue_state.py` وحل المتابعة؛ لا توجد ذاكرة دلالية دائمة عابرة للجلسات مثبتة. \|"`` | — |
| [SRC-53E640B937-L000015](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L15) | 15 | `"\| تفكيك الأسئلة المركبة \| **FIXED_AND_TESTED على PR #113 المدمج** \| محاور المقارنة والطلبات المركبة وتخطيط استعلامات؛ المطابقة اللفظية ليست فهمًا دلاليًا كاملًا. \|"` | — |
| [SRC-53E640B937-L000016](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L16) | 16 | ``"\| RAG كأداة داخل حلقة قرار \| **PARTIAL** \| `_search_web` و`_collect_research`؛ الاسترجاع الحالي بحث ويب عام، لا قاعدة معرفة خاصة مفهرسة. \|"`` | — |
| [SRC-53E640B937-L000017](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L17) | 17 | `"\| الاسترجاع التكراري الموجه \| **ADDED IN THIS PR; CI PENDING** \| حجز عدد صغير من الاستعلامات لمحاور بلا مرشحات نصية أولية، وإعادة البحث ضمن سقف الاستعلامات والميزانية الحاليين. \|"` | — |
| [SRC-53E640B937-L000018](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L18) | 18 | `"\| سلامة الموصلات والروابط \| **EXISTING / TESTED IN CI SCOPE** \| فحوص URL العام وSSRF وقائمة الحظر والمهل والميزانية. لا يثبت CI توافر كل مزود حيًا. \|"` | — |
| [SRC-53E640B937-L000019](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L19) | 19 | ``"\| سجل مقطع ← استشهاد ← مصدر \| **ADDED IN THIS PR; CI PENDING** \| `agents/claim_evidence.py` يربط كل مقطع مرشح بالاستشهادات وعناوين المصادر وروابطها ونوع النص، ويكشف الاستشهاد الغائب أو خارج النطاق. \|"`` | — |
| [SRC-53E640B937-L000020](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L20) | 20 | `"\| الاستشهادات الإلزامية والتوليد المقيد \| **PARTIAL** \| إزالة المؤشرات خارج نطاق المصدر ومراجعة النموذج والفحص اللفظي؛ لا يثبت أي منها الاستلزام الدلالي. \|"` | — |
| [SRC-53E640B937-L000021](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L21) | 21 | `"\| كشف الهلوسة والتحقق الدلالي \| **PARTIAL / NOT INDEPENDENTLY VERIFIED** \| مراجعة بمساعدة نموذج وفحوص حتمية. لا توجد هنا مراجعة مستقلة لكل ادعاء ببيانات مرجعية. \|"` | — |
| [SRC-53E640B937-L000022](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L22) | 22 | `"\| قواعد الكتابة والطلاقة \| **IMPROVED IN THIS PR; CI PENDING** \| إضافة قواعد للإجابة المباشرة، والجمل القصيرة، وتغطية الأجزاء، والاستشهاد من المصادر المتاحة، وإظهار المجهول. أمثلة few-shot معتمدة لم تُضف بعد. \|"` | — |
| [SRC-53E640B937-L000023](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L23) | 23 | `"\| الذاكرة \| **PARTIAL** \| تاريخ محادثة محدود ومنقّى داخل الطلب؛ مخزن دائم بصلاحيات ومدة احتفاظ غير مثبت. \|"` | — |
| [SRC-53E640B937-L000024](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L24) | 24 | `"\| الوكلاء المتخصصون \| **PIPELINE STAGES EXIST** \| التوجيه والتخطيط والاسترجاع والتوليد والمراجعة مراحل/وظائف قابلة للاختبار، لا وكلاء دائمون أو Meta-Agent. \|"` | — |
| [SRC-53E640B937-L000025](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L25) | 25 | `"\| تقييم مستمر \| **PARTIAL** \| corpus من 45 حالة ومدقق بنية ومشغّل حي لا يمنح PASS تلقائيًا. الصحة الدلالية تحتاج مرجعًا ذهبيًا/تحكيمًا بشريًا. \|"` | — |
| [SRC-53E640B937-L000026](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L26) | 26 | `"\| الاسترجاع/الأمانة/الصحة/الطلاقة \| **NOT FULLY MEASURED** \| المؤشرات الحالية تقنية/لفظية. لا تُسمى دقة أو Faithfulness دلالية ولا أرقام RAGAS دون بيانات تسميات. \|"` | — |
| [SRC-53E640B937-L000027](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L27) | 27 | `"\| الضبط الدقيق SFT/RL \| **NOT RUN / DEFERRED** \| لا توجد مجموعة تدريب بشرية منقحة وتجربة مقارنة وميزانية تدريب مثبتة. \|"` | — |
| [SRC-53E640B937-L000028](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L28) | 28 | `"\| قاعدة معرفة داخلية \| **NOT IMPLEMENTED BY THIS PR** \| يلزم تحديد الوثائق المسموح بها وحدودها وتقسيمها وفهرستها وتحديثها وصلاحياتها. \|"` | — |
| [SRC-53E640B937-L000029](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L29) | 29 | `"\| اختبار الاستضافة الحي \| **NOT RUN** \| يتطلب مصادقة في البيئة، وتطابق SHA المنشور، وموافقة مستقلة؛ لم نغيّر إعداد الاستضافة. \|"` | — |
| [SRC-53E640B937-L000030](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L30) | 30 | `""` | — |
| [SRC-53E640B937-L000031](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L31) | 31 | `"## السلوك المضاف"` | — |
| [SRC-53E640B937-L000032](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L32) | 32 | `""` | — |
| [SRC-53E640B937-L000033](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L33) | 33 | `"### حلقة استرجاع محكومة"` | — |
| [SRC-53E640B937-L000034](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L34) | 34 | `""` | — |
| [SRC-53E640B937-L000035](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L35) | 35 | `"1. يقرأ المسار سقف الاستعلامات المحدد."` | — |
| [SRC-53E640B937-L000036](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L36) | 36 | `"2. يحجز حتى ثلاثة استعلامات بحسب عدد المحاور والسقف لإعادة البحث."` | — |
| [SRC-53E640B937-L000037](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L37) | 37 | `"3. يبحث أوليًا ويحسب المحاور التي لا يظهر لها أي مرشح لفظي في المصادر المبدئية."` | — |
| [SRC-53E640B937-L000038](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L38) | 38 | `"4. يعطي استعلامات إصلاح تلك المحاور الأولوية، ثم يسمح بتوسعة عامة فقط في البحث العميق وعند بقاء سعة."` | — |
| [SRC-53E640B937-L000039](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L39) | 39 | `"5. يجمع النتائج ويعيد تكوين سجل الأدلة ضمن سقف الطلب."` | — |
| [SRC-53E640B937-L000040](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L40) | 40 | `"6. إن ظلت الفجوة، تظهر للمستخدم ولا تتحول إلى تخمين."` | — |
| [SRC-53E640B937-L000041](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L41) | 41 | `""` | — |
| [SRC-53E640B937-L000042](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L42) | 42 | `"### سجل الأدلة"` | — |
| [SRC-53E640B937-L000043](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L43) | 43 | `""` | — |
| [SRC-53E640B937-L000044](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L44) | 44 | ``"لكل مقطع نصي محدود: رقم المقطع، النص، فهارس الاستشهاد، عنوان المصدر والرابط ونوع النص (صفحة مستخرجة، مقتطف، عنوان فقط)، وناتج الفحص اللفظي عند توفره. وحدة السجل «مقطع مرشح» وليست ادعاءً مصنفًا دلاليًا. يعرض السجل صراحةً `semantic_verification=false` و`claim_entailment=not_checked`."`` | — |
| [SRC-53E640B937-L000045](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L45) | 45 | `""` | — |
| [SRC-53E640B937-L000046](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L46) | 46 | `"### قواعد التوليد"` | — |
| [SRC-53E640B937-L000047](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L47) | 47 | `""` | — |
| [SRC-53E640B937-L000048](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L48) | 48 | `"النتيجة أولًا، جمل قصيرة، تقسيم الإجابة بحسب محاور الطلب، عدم إسقاط محور بصمت، الاستشهاد من قائمة المسترجع فقط، إظهار النقص وعدم اختلاق روابط أو أرقام أو تواريخ، والتعامل مع نصوص الويب باعتبارها بيانات لا تعليمات."` | — |
| [SRC-53E640B937-L000049](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L49) | 49 | `""` | — |
| [SRC-53E640B937-L000050](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L50) | 50 | `"## بوابات القبول"` | — |
| [SRC-53E640B937-L000051](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L51) | 51 | `""` | — |
| [SRC-53E640B937-L000052](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L52) | 52 | `"- **A — CI:** Ruff، واختبارات Python 3.11/3.12، واختبار الإصلاح الموجه، وسجل الادعاء/الاستشهاد، وعرض الواجهة، وبناء الحاوية وAPI smoke."` | — |
| [SRC-53E640B937-L000053](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L53) | 53 | `"- **B — Review:** مراجعة بشرية للكود والنتائج قبل اعتماد PR."` | — |
| [SRC-53E640B937-L000054](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L54) | 54 | ``"- **C — Semantic benchmark:** أسئلة حقيقية مع مصادر مرجعية؛ تسميات صلة الاسترجاع وأحكام لكل ادعاء للأمانة والصحة والأسلوب. ما لم يُختبر يبقى `NOT_TESTED`."`` | — |
| [SRC-53E640B937-L000055](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L55) | 55 | `"- **D — Hosted acceptance:** موافقة منفصلة، اختبار محدود، وعدم كشف الأسرار، وتسجيل SHA المنشور."` | — |
| [SRC-53E640B937-L000056](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L56) | 56 | `"- **E — Fine-tuning / RAGAS:** لا يبدأ قبل إعداد بيانات مرجعية وخط أساس وميزانية قابلة للقياس."` | — |
| [SRC-53E640B937-L000057](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L57) | 57 | `""` | — |
| [SRC-53E640B937-L000058](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L58) | 58 | `"## قواعد لا نتجاوزها"` | — |
| [SRC-53E640B937-L000059](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L59) | 59 | `""` | — |
| [SRC-53E640B937-L000060](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L60) | 60 | `"- لا يرفع الملف أو وجود الدالة حالة بند إلى VERIFIED وحده."` | — |
| [SRC-53E640B937-L000061](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L61) | 61 | `"- لا تُعرض تغطية المحاور على أنها نسبة ثقة."` | — |
| [SRC-53E640B937-L000062](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L62) | 62 | `"- لا يعد وجود الاستشهاد دليلًا على صحته."` | — |
| [SRC-53E640B937-L000063](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L63) | 63 | `"- لا تتجاوز الحلقة ميزانية الاستعلامات والوقت."` | — |
| [SRC-53E640B937-L000064](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L64) | 64 | `"- لا تُسجل الأسرار."` | — |
| [SRC-53E640B937-L000065](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L65) | 65 | `"- لا دمج ولا نشر مستضاف من دون قرار المدير البشري."` | — |
| [SRC-53E640B937-L000066](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L66) | 66 | `""` | — |
| [SRC-53E640B937-L000067](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L67) | 67 | `""` | — |
| [SRC-53E640B937-L000068](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L68) | 68 | `"## إضافة تالية لنظام التقييم — 28 أكتوبر 2026"` | — |
| [SRC-53E640B937-L000069](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L69) | 69 | `""` | — |
| [SRC-53E640B937-L000070](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L70) | 70 | ``"أضيف إلى الفرع سكربت محلي دون اتصال باسم `scripts/score_answer_quality_reviews.py` لاشتقاق:"`` | — |
| [SRC-53E640B937-L000071](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L71) | 71 | `"- Retrieval Precision وRecall من عدّ مرشحين ذوي صلة ومجموع المرشحين والمصادر/الحقائق ذات الصلة المتاحة."` | — |
| [SRC-53E640B937-L000072](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L72) | 72 | `"- Faithfulness من عدد الادعاءات التي حكم المراجع بأنها مسندة إلى دليل وعدد الادعاءات التي راجعها."` | — |
| [SRC-53E640B937-L000073](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L73) | 73 | `"- Correctness من الحقائق التي حكم المراجع بصحتها من مجموع الحقائق التي راجعها."` | — |
| [SRC-53E640B937-L000074](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L74) | 74 | `"- Citation Support من الاستشهادات التي وجد المراجع أنها تسند الجملة من الاستشهادات التي فحصها."` | — |
| [SRC-53E640B937-L000075](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L75) | 75 | `"- جودة الكتابة من تقييم بشري من 1 إلى 5."` | — |
| [SRC-53E640B937-L000076](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L76) | 76 | `""` | — |
| [SRC-53E640B937-L000077](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L77) | 77 | ``"يقبل السكربت أحكامًا صريحة فقط، ويرفض معرفات الحالات المجهولة والقيم غير المتسقة، ويبقي كل حالة غير مراجعة في `NOT_TESTED`. المقاييس تجميعية من تعليقات بشرية وليست درجات RAGAS أو تقييمًا آليًا. لا تُملأ أي نتائج تجريبية نيابة عن المراجع."`` | — |
| [SRC-53E640B937-L000078](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L78) | 78 | `""` | — |
| [SRC-53E640B937-L000079](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L79) | 79 | `""` | — |
| [SRC-53E640B937-L000080](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L80) | 80 | `"### قاعدة أمثلة أسلوبية موجهة"` | — |
| [SRC-53E640B937-L000081](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L81) | 81 | `"تتضمن مطالبة التوليد الآن مثالين قصيرين: استشهاد مضبوط بحدود ما يقوله المصدر، وامتناع صريح عندما لا تتضمن النتائج دليلًا كافيًا. المثال معلن على أنه توضيحي ولا يجوز نقل وقائعه للإجابة الحالية ما لم تؤيدها المصادر الفعلية؛ أضيف اختبار وحدات للتحقق من وصول القاعدة إلى مطالبة التوليد."` | — |
| [SRC-53E640B937-L000082](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L82) | 82 | `""` | — |
| [SRC-53E640B937-L000083](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L83) | 83 | `""` | — |
| [SRC-53E640B937-L000084](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L84) | 84 | `"### تشغيل التقييم البشري القابل للتكرار"` | — |
| [SRC-53E640B937-L000085](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L85) | 85 | `""` | — |
| [SRC-53E640B937-L000086](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L86) | 86 | `"أداة تجميع المقاييس لا تستدعي النموذج ولا تزعم تقييمًا تلقائيًا. ينشئ المراجع ملف JSON مستقلًا مثل المثال التالي؛ **الأرقام توضيحية وهمية لشرح المخطط فقط وليست نتائج Omarai**:"` | — |
| [SRC-53E640B937-L000087](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L87) | 87 | `""` | — |
| [SRC-53E640B937-L000088](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L88) | 88 | ````"```json"```` | — |
| [SRC-53E640B937-L000089](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L89) | 89 | `"{"` | — |
| [SRC-53E640B937-L000090](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L90) | 90 | `"  \"schema_version\": \"1.0\","` | — |
| [SRC-53E640B937-L000091](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L91) | 91 | `"  \"reviews\": ["` | — |
| [SRC-53E640B937-L000092](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L92) | 92 | `"    {"` | — |
| [SRC-53E640B937-L000093](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L93) | 93 | `"      \"case_id\": \"AQ-007\","` | — |
| [SRC-53E640B937-L000094](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L94) | 94 | `"      \"status\": \"REVIEWED\","` | — |
| [SRC-53E640B937-L000095](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L95) | 95 | `"      \"retrieval\": {"` | — |
| [SRC-53E640B937-L000096](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L96) | 96 | `"        \"relevant_retrieved\": 3,"` | — |
| [SRC-53E640B937-L000097](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L97) | 97 | `"        \"retrieved_count\": 5,"` | — |
| [SRC-53E640B937-L000098](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L98) | 98 | `"        \"relevant_available\": 4"` | — |
| [SRC-53E640B937-L000099](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L99) | 99 | `"      },"` | — |
| [SRC-53E640B937-L000100](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L100) | 100 | `"      \"faithfulness\": {"` | — |
| [SRC-53E640B937-L000101](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L101) | 101 | `"        \"supported_claims\": 4,"` | — |
| [SRC-53E640B937-L000102](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L102) | 102 | `"        \"reviewed_claims\": 5"` | — |
| [SRC-53E640B937-L000103](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L103) | 103 | `"      },"` | — |
| [SRC-53E640B937-L000104](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L104) | 104 | `"      \"correctness\": {"` | — |
| [SRC-53E640B937-L000105](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L105) | 105 | `"        \"correct_facts\": 4,"` | — |
| [SRC-53E640B937-L000106](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L106) | 106 | `"        \"reviewed_facts\": 5"` | — |
| [SRC-53E640B937-L000107](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L107) | 107 | `"      },"` | — |
| [SRC-53E640B937-L000108](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L108) | 108 | `"      \"citations\": {"` | — |
| [SRC-53E640B937-L000109](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L109) | 109 | `"        \"supported_citations\": 3,"` | — |
| [SRC-53E640B937-L000110](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L110) | 110 | `"        \"reviewed_citations\": 4"` | — |
| [SRC-53E640B937-L000111](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L111) | 111 | `"      },"` | — |
| [SRC-53E640B937-L000112](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L112) | 112 | `"      \"writing_quality\": 4"` | — |
| [SRC-53E640B937-L000113](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L113) | 113 | `"    },"` | — |
| [SRC-53E640B937-L000114](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L114) | 114 | `"    {"` | — |
| [SRC-53E640B937-L000115](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L115) | 115 | `"      \"case_id\": \"AQ-008\","` | — |
| [SRC-53E640B937-L000116](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L116) | 116 | `"      \"status\": \"NOT_TESTED\","` | — |
| [SRC-53E640B937-L000117](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L117) | 117 | `"      \"notes\": \"لم يراجع بشر الإجابة حتى الآن.\""` | — |
| [SRC-53E640B937-L000118](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L118) | 118 | `"    }"` | — |
| [SRC-53E640B937-L000119](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L119) | 119 | `"  ]"` | — |
| [SRC-53E640B937-L000120](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L120) | 120 | `"}"` | — |
| [SRC-53E640B937-L000121](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L121) | 121 | ````"```"```` | — |
| [SRC-53E640B937-L000122](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L122) | 122 | `""` | — |
| [SRC-53E640B937-L000123](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L123) | 123 | `"ثم يحسب الملخص:"` | — |
| [SRC-53E640B937-L000124](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L124) | 124 | `""` | — |
| [SRC-53E640B937-L000125](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L125) | 125 | ````"```bash"```` | — |
| [SRC-53E640B937-L000126](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L126) | 126 | `"python scripts/score_answer_quality_reviews.py --reviews reviews.json --corpus tests/fixtures/answer_quality_cases.json --out scorecard.json"` | — |
| [SRC-53E640B937-L000127](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L127) | 127 | ````"```"```` | — |
| [SRC-53E640B937-L000128](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L128) | 128 | `""` | — |
| [SRC-53E640B937-L000129](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L129) | 129 | `"- **Precision:** عدد عناصر الاسترجاع التي حكم المراجع بصِلتها ÷ إجمالي العناصر المسترجعة بعد إزالة التكرار."` | — |
| [SRC-53E640B937-L000130](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L130) | 130 | `"- **Recall:** عدد العناصر ذات الصلة المسترجعة ÷ إجمالي العناصر ذات الصلة المعروفة في مجموعة مرجعية محددة؛ إن لم يتوفر هذا المقام تبقى النتيجة غير قابلة للقياس."` | — |
| [SRC-53E640B937-L000131](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L131) | 131 | `"- **Faithfulness:** الادعاءات التي حكم المراجع بأنها مسندة إلى الدليل ÷ الادعاءات التي فحصها."` | — |
| [SRC-53E640B937-L000132](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L132) | 132 | `"- **Correctness:** الحقائق الصحيحة وفق مرجع موثوق ÷ الحقائق التي فُحصت."` | — |
| [SRC-53E640B937-L000133](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L133) | 133 | `"- **Citation Support:** الاستشهادات التي يسند مصدرها الجملة وفق المراجع ÷ الاستشهادات التي فُحصت."` | — |
| [SRC-53E640B937-L000134](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L134) | 134 | `"- **Writing quality:** متوسط تقدير بشري من 1 إلى 5."` | — |
| [SRC-53E640B937-L000135](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L135) | 135 | `""` | — |
| [SRC-53E640B937-L000136](../OMARAI_AGENTIC_RAG_ROADMAP_AR.md#L136) | 136 | ``"يجب مراجعة النص الأصلي للمصدر لا عنوانه فقط. يفضل أن يراجع شخصان عينة مشتركة وأن تتم تسوية اختلافاتهما قبل المقارنة بين الإصدارات. حالة `NOT_TESTED` لا تدخل في أي بسط أو مقام ولا تتحول إلى PASS. هذه المقاييس مراجعات بشرية مجمعة وليست تطبيقًا لـRAGAS."`` | — |
## وثائق وفهرسة

### FILE-BA40E88B07 — [docs/OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-BA40E88B07-L000001](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L1) | 1 | `"# تدقيق معمارية Omarai والخيارات التقنية والممارسات الأمنية"` | — |
| [SRC-BA40E88B07-L000002](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L2) | 2 | `"**التاريخ:** 1 نوفمبر 2026  "` | — |
| [SRC-BA40E88B07-L000003](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L3) | 3 | ``"**خط الأساس:** `main` عند `63b7dd01889de4aadd66acea90a2415b33376e2e`  "`` | — |
| [SRC-BA40E88B07-L000004](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L4) | 4 | ``"**فرع الإصلاح:** `fix/p0-core-consolidated-2026-11-01`  "`` | — |
| [SRC-BA40E88B07-L000005](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L5) | 5 | `"**حالة الوثيقة:** مراجعة مصدرية؛ تغييرات الفرع غير مدمجة."` | — |
| [SRC-BA40E88B07-L000006](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L6) | 6 | `""` | — |
| [SRC-BA40E88B07-L000007](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L7) | 7 | `"## 1. الخلاصة التنفيذية"` | — |
| [SRC-BA40E88B07-L000008](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L8) | 8 | `""` | — |
| [SRC-BA40E88B07-L000009](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L9) | 9 | `"**VERIFIED:** Omarai تطبيق Python modular monolith بواجهة HTTP مخصصة، ومحرك بحث/إجابة، وSQLite لتخزين العملاء، وموصلات بحث، وحدود للطلبات والموارد، واختبارات CI على Python 3.11 و3.12."` | — |
| [SRC-BA40E88B07-L000010](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L10) | 10 | `""` | — |
| [SRC-BA40E88B07-L000011](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L11) | 11 | `"**VERIFIED:** توجد آليات SSRF قوية نسبيًا في جلب الصفحات: رفض الوجهات المحلية، حل DNS والتحقق من كل عنوان، الاتصال بعنوان IP مثبت بدل إعادة حل الاسم، تعطيل proxy من البيئة، وعدم اتباع redirects تلقائيًا؛ كل redirect يدوي يعاد التحقق منه."` | — |
| [SRC-BA40E88B07-L000012](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L12) | 12 | `""` | — |
| [SRC-BA40E88B07-L000013](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L13) | 13 | ``"**VERIFIED:** عزل العملاء يُبنى على هوية مستخرجة من credential موثوق، وليس على `tenant_id` المرسل في جسم الطلب. استعلامات leads الأساسية scoped بالـtenant، مع اختبارات تمنع تزوير tenant_id والوصول المتبادل."`` | — |
| [SRC-BA40E88B07-L000014](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L14) | 14 | `""` | — |
| [SRC-BA40E88B07-L000015](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L15) | 15 | `"**VERIFIED:** كان المتصفح يحتفظ برمز API في Web Storage. أزيل هذا المسار في الفرع واستُبدل بجلسات opaque خادمية، مع cookie محمي وCSRF Origin check. هذه خطوة أمنية مهمة، لكنها تحتاج اعتماد CI النهائي ومراجعة بشرية قبل الدمج."` | — |
| [SRC-BA40E88B07-L000016](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L16) | 16 | `""` | — |
| [SRC-BA40E88B07-L000017](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L17) | 17 | `"**INFERRED:** أفضل خيار حالي هو الإبقاء على modular monolith منضبط بدل تفكيك الخدمات. لا توجد أدلة حمل أو فرق تشغيل أو حدود ملكية بيانات تبرر microservices الآن."` | — |
| [SRC-BA40E88B07-L000018](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L18) | 18 | `""` | — |
| [SRC-BA40E88B07-L000019](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L19) | 19 | `"**UNKNOWN:** القبول الحي على الاستضافة، استمرار قاعدة البيانات بعد إعادة إنشاء الحاوية، النسخ الاحتياطي والاستعادة، الحمل متعدد العمليات، واتصال مزودي النماذج الفعلي."` | — |
| [SRC-BA40E88B07-L000020](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L20) | 20 | `""` | — |
| [SRC-BA40E88B07-L000021](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L21) | 21 | `"## 2. المعمارية المرصودة"` | — |
| [SRC-BA40E88B07-L000022](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L22) | 22 | `""` | — |
| [SRC-BA40E88B07-L000023](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L23) | 23 | ``"- `web/`: واجهتا Agent وDashboard."`` | — |
| [SRC-BA40E88B07-L000024](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L24) | 24 | ``"- `api/omarai.py`: HTTP ingress، المصادقة، Origin/CORS، تحديد المعدل، حدود الجسم والمهلة، وتوجيه API."`` | — |
| [SRC-BA40E88B07-L000025](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L25) | 25 | ``"- `agents/web_agent.py`: تنسيق البحث، جلب الصفحات، توليد الإجابة، تسجيل الأدلة، وطلبات النماذج."`` | — |
| [SRC-BA40E88B07-L000026](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L26) | 26 | ``"- `agents/omarai.py`: تحليل أولي لإشارات الشراء وLeadStore وtenant/user/membership/token/session storage."`` | — |
| [SRC-BA40E88B07-L000027](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L27) | 27 | ``"- `agents/semantic_claim_verifier.py`: تقييم دعم الادعاء من المصدر المحدد."`` | — |
| [SRC-BA40E88B07-L000028](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L28) | 28 | ``"- `RequestBudget` ومحددات التزامن: ميزانية للطلب وعمليات البحث/النماذج وجلب الصفحات."`` | — |
| [SRC-BA40E88B07-L000029](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L29) | 29 | ``"- `tests/`: اختبارات وحدات وتكامل وأمن وعقود قبول."`` | — |
| [SRC-BA40E88B07-L000030](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L30) | 30 | `""` | — |
| [SRC-BA40E88B07-L000031](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L31) | 31 | `"هذا **تطبيق أحادي العملية متعدد الوحدات**، وليس مجموعة microservices. يجب الحفاظ على حدود الوحدات وعقودها قبل التفكير في توزيعها."` | — |
| [SRC-BA40E88B07-L000032](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L32) | 32 | `""` | — |
| [SRC-BA40E88B07-L000033](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L33) | 33 | `"## 3. قرارات الخيارات التقنية"` | — |
| [SRC-BA40E88B07-L000034](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L34) | 34 | `""` | — |
| [SRC-BA40E88B07-L000035](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L35) | 35 | `"### 3.1 Modular Monolith مقابل Microservices"` | — |
| [SRC-BA40E88B07-L000036](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L36) | 36 | `""` | — |
| [SRC-BA40E88B07-L000037](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L37) | 37 | `"**القرار — PROPOSED/اعتماد هذا المسار:** Modular monolith مع حدود واضحة بين API والسياسة ومحرك البحث والموصلات والتخزين والتحقق."` | — |
| [SRC-BA40E88B07-L000038](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L38) | 38 | `""` | — |
| [SRC-BA40E88B07-L000039](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L39) | 39 | `"الأسباب:"` | — |
| [SRC-BA40E88B07-L000040](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L40) | 40 | `"- التطبيق الحالي يعتمد على SQLite وعمليات Python متزامنة؛ توزيع الوحدات الآن يضيف اتصالات شبكية ومصادقة بين الخدمات وتناسقًا موزعًا دون دليل أن ذلك يحل اختناقًا مثبتًا."` | — |
| [SRC-BA40E88B07-L000041](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L41) | 41 | `"- اختبارات الوحدة والتكامل الحالية تتيح تغييرًا صغيرًا وقابلًا للمراجعة."` | — |
| [SRC-BA40E88B07-L000042](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L42) | 42 | `"- لا تنشأ وكلاء دائمون أو Meta-Agent أو توليد ذاتي للكود قبل استقرار السياسات والعقود."` | — |
| [SRC-BA40E88B07-L000043](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L43) | 43 | `""` | — |
| [SRC-BA40E88B07-L000044](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L44) | 44 | `"### 3.2 HTTP Runtime"` | — |
| [SRC-BA40E88B07-L000045](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L45) | 45 | `""` | — |
| [SRC-BA40E88B07-L000046](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L46) | 46 | ``"**VERIFIED:** الخادم يستخدم `http.server` / `BaseHTTPRequestHandler` مع طبقات حماية مخصصة: حدود حجم الطلب، deadline للقراءة، حد اتصالات متزامنة، معدل لكل IP، headers، وفحص Origin."`` | — |
| [SRC-BA40E88B07-L000047](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L47) | 47 | `""` | — |
| [SRC-BA40E88B07-L000048](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L48) | 48 | ``"**تحذير رسمي:** وثائق Python تقول إن `http.server` ليس موصى به للإنتاج، ويطبق فحوصات أمنية أساسية فقط. وجود hardening في التطبيق لا يحول مكتبة الاختبار/الخدمة البسيطة تلقائيًا إلى خادم إنتاج مدعوم."`` | — |
| [SRC-BA40E88B07-L000049](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L49) | 49 | `""` | — |
| [SRC-BA40E88B07-L000050](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L50) | 50 | `"**PROPOSED — P1:** تقييم انتقال محدود إلى WSGI/ASGI runtime مدعوم (مثل Waitress أو Uvicorn) مع إبقاء عقود API الحالية واختبارات قبول HTTP. لا أنصح بترحيل واسع داخل حزمة P0 الحالية؛ يجب أن يكون له PR مستقل ومقارنة أداء وتوافق وTimeout/Concurrency tests."` | — |
| [SRC-BA40E88B07-L000051](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L51) | 51 | `""` | — |
| [SRC-BA40E88B07-L000052](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L52) | 52 | `"### 3.3 SQLite مقابل PostgreSQL"` | — |
| [SRC-BA40E88B07-L000053](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L53) | 53 | `""` | — |
| [SRC-BA40E88B07-L000054](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L54) | 54 | `"**VERIFIED:**"` | — |
| [SRC-BA40E88B07-L000055](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L55) | 55 | `"- SQLite مناسب كبداية لنسخة واحدة وقاعدة محلية دائمة."` | — |
| [SRC-BA40E88B07-L000056](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L56) | 56 | ``"- كل اتصال يفعّل `PRAGMA foreign_keys=ON`."`` | — |
| [SRC-BA40E88B07-L000057](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L57) | 57 | ``"- `sqlite3.connect(timeout=10)` يحدد انتظار القفل، وأضيف wrapper يغلق الاتصال دائمًا بعد commit/rollback."`` | — |
| [SRC-BA40E88B07-L000058](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L58) | 58 | `"- الجلسات والرموز وعضويات المستخدمين والـleads مرتبطة بمفاتيح وعلاقات tenant."` | — |
| [SRC-BA40E88B07-L000059](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L59) | 59 | `""` | — |
| [SRC-BA40E88B07-L000060](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L60) | 60 | `"**PROPOSED:**"` | — |
| [SRC-BA40E88B07-L000061](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L61) | 61 | `"- الاستمرار على SQLite للتشغيل الأولي أحادي النسخة، مع volume دائم ونسخ احتياطي/استعادة مجربين."` | — |
| [SRC-BA40E88B07-L000062](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L62) | 62 | `"- عدم تفعيل WAL أو تغيير journal mode دون اختبار backup/restore والتزامن على نفس volume."` | — |
| [SRC-BA40E88B07-L000063](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L63) | 63 | `"- الانتقال إلى PostgreSQL قبل تشغيل عدة replicas أو الحاجة إلى كتابة متزامنة موزعة أو إدارة مركزية لقاعدة مشتركة. SQLite لا يقدم حدًا موزعًا لمحددات المعدل أو التزامن."` | — |
| [SRC-BA40E88B07-L000064](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L64) | 64 | `""` | — |
| [SRC-BA40E88B07-L000065](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L65) | 65 | `"### 3.4 المصادقة والجلسات وعزل المستأجرين"` | — |
| [SRC-BA40E88B07-L000066](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L66) | 66 | `""` | — |
| [SRC-BA40E88B07-L000067](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L67) | 67 | `"**VERIFIED في فرع الإصلاح:**"` | — |
| [SRC-BA40E88B07-L000068](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L68) | 68 | ``"- bearer token لا يُخزن في `localStorage` أو `sessionStorage`."`` | — |
| [SRC-BA40E88B07-L000069](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L69) | 69 | ``"- POST `/api/session` يتحقق من API token ثم ينشئ session ID عشوائيًا."`` | — |
| [SRC-BA40E88B07-L000070](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L70) | 70 | ``"- لا يُخزن session ID خامًا؛ تحفظ بصمته SHA-256 في `web_sessions`."`` | — |
| [SRC-BA40E88B07-L000071](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L71) | 71 | ``"- cookie العام يستخدم `__Host-` مع `Secure; HttpOnly; SameSite=Strict; Path=/` ومدة 8 ساعات."`` | — |
| [SRC-BA40E88B07-L000072](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L72) | 72 | `"- انتهاء الجلسة مفروض على الخادم، وليس اعتمادًا على Max-Age في المتصفح فقط."` | — |
| [SRC-BA40E88B07-L000073](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L73) | 73 | `"- الجلسة مرتبطة ببصمة API token؛ الإبطال/الانتهاء/تغيير shared token يبطل الجلسة."` | — |
| [SRC-BA40E88B07-L000074](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L74) | 74 | `"- logout يبطل سجل الجلسة."` | — |
| [SRC-BA40E88B07-L000075](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L75) | 75 | `"- POST المعتمد على cookie يتطلب Origin موثوقًا."` | — |
| [SRC-BA40E88B07-L000076](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L76) | 76 | `"- لا يُقبل tenant_id من جسم الطلب كمرجع صلاحية؛ الهوية والـtenant يأتيان من principal موثوق."` | — |
| [SRC-BA40E88B07-L000077](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L77) | 77 | `""` | — |
| [SRC-BA40E88B07-L000078](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L78) | 78 | `"**حدود باقية:**"` | — |
| [SRC-BA40E88B07-L000079](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L79) | 79 | `"- واجهة إنشاء tenants/users/memberships/tokens وإدارة الأدوار الذاتية غير مكتملة؛ provisioning برمجي."` | — |
| [SRC-BA40E88B07-L000080](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L80) | 80 | `"- viewer للقراءة فقط، وowner مطلوب لتشخيصات المزودين؛ يجب اعتماد مصفوفة أدق لأدوار admin/manager/sales_agent قبل فتح إدارة الفرق."` | — |
| [SRC-BA40E88B07-L000081](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L81) | 81 | `"- HttpOnly يمنع JavaScript من قراءة session ID، لكنه لا يمنع XSS من تنفيذ طلبات باسم المستخدم؛ تبقى CSP ومخرجات DOM الآمنة ومراجعة XSS مطلوبة."` | — |
| [SRC-BA40E88B07-L000082](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L82) | 82 | `"- لا يوجد بعد تنظيف دوري لسجلات الجلسات المنتهية؛ لا يؤثر ذلك في التحقق، لكنه دين صيانة."` | — |
| [SRC-BA40E88B07-L000083](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L83) | 83 | `""` | — |
| [SRC-BA40E88B07-L000084](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L84) | 84 | `"### 3.5 موفرو النماذج وFailover"` | — |
| [SRC-BA40E88B07-L000085](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L85) | 85 | `""` | — |
| [SRC-BA40E88B07-L000086](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L86) | 86 | `"**VERIFIED في الكود/الاختبارات:**"` | — |
| [SRC-BA40E88B07-L000087](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L87) | 87 | `"- موفر OpenAI-compatible أساسي (OpenRouter أو base URL مخصص)."` | — |
| [SRC-BA40E88B07-L000088](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L88) | 88 | `"- Gemini وMistral موفران اختياريان احتياطيان عند توافر مفاتيحهما."` | — |
| [SRC-BA40E88B07-L000089](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L89) | 89 | `"- التسلسل: النموذج المطلوب في المزود الأساسي، ثم fallback الخاص به إن ضُبط، ثم النموذج الافتراضي للمزود التالي."` | — |
| [SRC-BA40E88B07-L000090](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L90) | 90 | ``"- فشل 429 يصنف `rate_limited`، و401/403 يصنف `unauthorized`؛ لا يُسجل جسم رد المزود."`` | — |
| [SRC-BA40E88B07-L000091](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L91) | 91 | ``"- طلب semantic verifier يستخدم `allow_fallback=False` لمنع إرسال مطالبة التحقق إلى مزود آخر بصمت."`` | — |
| [SRC-BA40E88B07-L000092](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L92) | 92 | `"- OpenRouter web search لا يرسل إلى Gemini/Mistral، ويظل opt-in."` | — |
| [SRC-BA40E88B07-L000093](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L93) | 93 | `""` | — |
| [SRC-BA40E88B07-L000094](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L94) | 94 | `"**VERIFIED من وثائق الموردين:**"` | — |
| [SRC-BA40E88B07-L000095](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L95) | 95 | ``"- Google Gemini يوفر OpenAI-compatible endpoint؛ النموذج الافتراضي في الفرع `gemini-3.1-flash-lite`."`` | — |
| [SRC-BA40E88B07-L000096](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L96) | 96 | ``"- Mistral Small 4 يعلن API names `mistral-small-2603` و`mistral-small-latest`؛ الافتراضي `mistral-small-latest`."`` | — |
| [SRC-BA40E88B07-L000097](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L97) | 97 | `""` | — |
| [SRC-BA40E88B07-L000098](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L98) | 98 | `"**UNKNOWN:** صلاحية مفاتيح المستخدم الفعلية، quota، latency، أسعار الحساب، والاتصال الحي. لم تُنفذ أي مكالمة مزود حية أو مدفوعة. قد تنتقل المطالبات والمقتطفات إلى مزود احتياطي عند فشل الأساسي؛ يجب إبلاغ المستخدم بذلك وعدم إرسال أسرار أو بيانات عملاء سرية."` | — |
| [SRC-BA40E88B07-L000099](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L99) | 99 | `""` | — |
| [SRC-BA40E88B07-L000100](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L100) | 100 | `"**حد الاستقلال:** عند استخدام Gemini أو Mistral فقط، النموذج الافتراضي لمراجع الادعاءات يساوي نموذج الإجابة؛ لذلك لا توجد مراجعة مستقلة بنموذج مختلف ما لم يضبط المستخدم نموذجًا صالحًا لذلك المزود. وحتى عند اختلاف model ID، يبقى ذلك تقييم دعم من نموذج وليس إثبات حقيقة خارجية."` | — |
| [SRC-BA40E88B07-L000101](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L101) | 101 | `""` | — |
| [SRC-BA40E88B07-L000102](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L102) | 102 | `"### 3.6 البحث وSSRF وPrompt Injection"` | — |
| [SRC-BA40E88B07-L000103](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L103) | 103 | `""` | — |
| [SRC-BA40E88B07-L000104](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L104) | 104 | `"**VERIFIED في الكود:**"` | — |
| [SRC-BA40E88B07-L000105](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L105) | 105 | `"- قبول HTTP(S) فقط، رفض userinfo والمنافذ غير المعتمدة وعناوين localhost/private."` | — |
| [SRC-BA40E88B07-L000106](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L106) | 106 | `"- حل DNS والتحقق من كل العناوين العامة، ثم الاتصال بـIP مثبت مع Host/SNI الأصليين لتقليل DNS rebinding/TOCTOU."` | — |
| [SRC-BA40E88B07-L000107](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L107) | 107 | ``"- `trust_env=False` يمنع proxy غير مقصود من البيئة، و`follow_redirects=False` يمنع اتباع redirect تلقائيًا؛ كل redirect يدوي يعاد فحص وجهته."`` | — |
| [SRC-BA40E88B07-L000108](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L108) | 108 | `"- طلبات مزودي النماذج لا تتبع redirects حتى لا تنتقل Authorization إلى origin آخر."` | — |
| [SRC-BA40E88B07-L000109](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L109) | 109 | `"- محتوى الصفحات والنتائج الخارجية بيانات غير موثوقة، ولا ينبغي أن يغير تعليمات النظام أو صلاحيات الأدوات."` | — |
| [SRC-BA40E88B07-L000110](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L110) | 110 | `""` | — |
| [SRC-BA40E88B07-L000111](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L111) | 111 | `"**المتبقي:** اختبارات SSRF لا تغطي كل بيئة DNS/IPv6/proxy فعلية؛ يلزم red-team واختبار hosted network policy."` | — |
| [SRC-BA40E88B07-L000112](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L112) | 112 | `""` | — |
| [SRC-BA40E88B07-L000113](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L113) | 113 | `"### 3.7 GitHub Actions وسلسلة التوريد"` | — |
| [SRC-BA40E88B07-L000114](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L114) | 114 | `""` | — |
| [SRC-BA40E88B07-L000115](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L115) | 115 | `"**VERIFIED:** Workflow الأساسي يستخدم Python 3.11 و3.12، lint، الاختبارات، Docker build، وprotected API smoke. Actions المستخدمة في المسارات التي فُحصت مثبتة على commit SHAs، وصلاحيات الاختبار محدودة إلى القراءة حيث لا يلزم الكتابة."` | — |
| [SRC-BA40E88B07-L000116](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L116) | 116 | `""` | — |
| [SRC-BA40E88B07-L000117](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L117) | 117 | ``"**PROPOSED:** استمرار مراجعة كل workflow جديد بحثًا عن `pull_request_target`، أو أسرار في PR من fork، أو صلاحيات `contents: write` غير ضرورية. لا تستخدم secrets في اختبار pull request غير موثوق."`` | — |
| [SRC-BA40E88B07-L000118](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L118) | 118 | `""` | — |
| [SRC-BA40E88B07-L000119](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L119) | 119 | `"## 4. الإصلاحات التي نُقلت إلى حزمة #145"` | — |
| [SRC-BA40E88B07-L000120](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L120) | 120 | `""` | — |
| [SRC-BA40E88B07-L000121](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L121) | 121 | `"\| المجال \| الإصلاح \| الاختبار المضاف \|"` | — |
| [SRC-BA40E88B07-L000122](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L122) | 122 | `"\|---\|---\|---\|"` | — |
| [SRC-BA40E88B07-L000123](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L123) | 123 | `"\| SQLite \| إغلاق كل اتصال بعد transaction \| اتصال مغلق بعد النجاح والفشل + rollback \|"` | — |
| [SRC-BA40E88B07-L000124](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L124) | 124 | `"\| Browser auth \| opaque server-side sessions \| expiry، revoke، rotation، logout، cookie flags، CSRF Origin \|"` | — |
| [SRC-BA40E88B07-L000125](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L125) | 125 | `"\| Dashboard \| قبول معرف lead من 24 hex \| Regression لاختبار handler \|"` | — |
| [SRC-BA40E88B07-L000126](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L126) | 126 | `"\| Intent \| إزالة تعريفات المتابعة المكررة \| اختبار عدد التعريفات \|"` | — |
| [SRC-BA40E88B07-L000127](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L127) | 127 | `"\| Search relevance \| حد مفهومين لاستعلام من 3 مفاهيم وإزالة كلمات التنقل من topic score \| mixed official/unrelated results \|"` | — |
| [SRC-BA40E88B07-L000128](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L128) | 128 | `"\| Provider errors \| تصنيف 429 و401/403 وإخفاء body \| fallback bounded/redacted \|"` | — |
| [SRC-BA40E88B07-L000129](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L129) | 129 | `"\| Provider failover \| Gemini/Mistral defaults وfailover \| mock provider selection, failover, verifier isolation \|"` | — |
| [SRC-BA40E88B07-L000130](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L130) | 130 | `"\| Diagnostics \| إبقاء الموافقة الصريحة والـowner gate \| اختبارات HTTP موجودة \|"` | — |
| [SRC-BA40E88B07-L000131](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L131) | 131 | `"\| Tenant isolation \| tenant scope وroles وtoken revocation \| اختبارات multi-tenant الحالية \|"` | — |
| [SRC-BA40E88B07-L000132](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L132) | 132 | `""` | — |
| [SRC-BA40E88B07-L000133](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L133) | 133 | `"## 5. أولويات ما بعد هذه الحزمة"` | — |
| [SRC-BA40E88B07-L000134](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L134) | 134 | `""` | — |
| [SRC-BA40E88B07-L000135](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L135) | 135 | `"1. **P1 — HTTP runtime:** اختبار انتقال إلى WSGI/ASGI دون تغيير API."` | — |
| [SRC-BA40E88B07-L000136](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L136) | 136 | `"2. **P1 — Role matrix:** تعريف صلاحيات admin/manager/sales_agent على العمليات والموارد."` | — |
| [SRC-BA40E88B07-L000137](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L137) | 137 | `"3. **P1 — Provisioning:** أداة إدارية آمنة لإنشاء المستخدمين والعضويات والرموز، دون إظهار الأسرار في السجلات."` | — |
| [SRC-BA40E88B07-L000138](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L138) | 138 | `"4. **P1 — Hosted acceptance:** اختبار هوية البناء، volume، session cookie عبر HTTPS reverse proxy، وlogout/token revocation."` | — |
| [SRC-BA40E88B07-L000139](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L139) | 139 | `"5. **P2 — Data store:** backup/restore مجرب، ثم قرار PostgreSQL عند ظهور متطلبات multi-instance."` | — |
| [SRC-BA40E88B07-L000140](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L140) | 140 | `"6. **P2 — Model evaluation:** corpus عربي/إنجليزي موسوم بشريًا، مقارنة موفري النماذج، وقياس false positives/abstention/latency/cost."` | — |
| [SRC-BA40E88B07-L000141](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L141) | 141 | `"7. **P3 — Operations:** load/concurrency/failure tests، distributed rate limits عند تعدد النسخ، ومراقبة منزوعة الأسرار."` | — |
| [SRC-BA40E88B07-L000142](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L142) | 142 | `""` | — |
| [SRC-BA40E88B07-L000143](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L143) | 143 | `"## 6. حالة التنفيذ"` | — |
| [SRC-BA40E88B07-L000144](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L144) | 144 | `""` | — |
| [SRC-BA40E88B07-L000145](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L145) | 145 | `"- **VERIFIED:** الملفات والتغييرات موجودة في فرع الإصلاح، ولا توجد تعديلات على main."` | — |
| [SRC-BA40E88B07-L000146](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L146) | 146 | `"- **FIXED_AND_TESTED:** لا يُثبت إلا بعد نجاح CI النهائي على رأس الفرع بعد آخر تعديل."` | — |
| [SRC-BA40E88B07-L000147](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L147) | 147 | `"- **NOT_RUN:** hosted acceptance، live provider calls، paid quota checks، load test، backup/restore، independent red-team."` | — |
| [SRC-BA40E88B07-L000148](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L148) | 148 | `"- **UNKNOWN:** سلوك الاستضافة الحالي ومفاتيح الموردين الفعلية."` | — |
| [SRC-BA40E88B07-L000149](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L149) | 149 | `""` | — |
| [SRC-BA40E88B07-L000150](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L150) | 150 | `"## 7. المراجع الرسمية"` | — |
| [SRC-BA40E88B07-L000151](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L151) | 151 | `""` | — |
| [SRC-BA40E88B07-L000152](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L152) | 152 | `"- [Python 3.12 — http.server security warning](https://docs.python.org/3.12/library/http.server.html)"` | — |
| [SRC-BA40E88B07-L000153](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L153) | 153 | `"- [Python 3.12 — sqlite3 connection context manager](https://docs.python.org/3.12/library/sqlite3.html#how-to-use-the-connection-context-manager)"` | — |
| [SRC-BA40E88B07-L000154](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L154) | 154 | `"- [SQLite — foreign_keys pragma](https://www.sqlite.org/pragma.html#pragma_foreign_keys)"` | — |
| [SRC-BA40E88B07-L000155](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L155) | 155 | `"- [SQLite — busy_timeout pragma](https://www.sqlite.org/pragma.html#pragma_busy_timeout)"` | — |
| [SRC-BA40E88B07-L000156](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L156) | 156 | `"- [OWASP — Multi-Tenant Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Multi_Tenant_Security_Cheat_Sheet.html)"` | — |
| [SRC-BA40E88B07-L000157](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L157) | 157 | `"- [OWASP — Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)"` | — |
| [SRC-BA40E88B07-L000158](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L158) | 158 | `"- [OWASP — Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)"` | — |
| [SRC-BA40E88B07-L000159](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L159) | 159 | `"- [OWASP — SSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html)"` | — |
| [SRC-BA40E88B07-L000160](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L160) | 160 | `"- [GitHub — Security hardening for GitHub Actions](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions)"` | — |
| [SRC-BA40E88B07-L000161](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L161) | 161 | `"- [Google — Gemini OpenAI compatibility](https://ai.google.dev/gemini-api/docs/openai)"` | — |
| [SRC-BA40E88B07-L000162](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L162) | 162 | `"- [Google — Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite)"` | — |
| [SRC-BA40E88B07-L000163](../OMARAI_ARCHITECTURE_SECURITY_REVIEW_2026-11-01_AR.md#L163) | 163 | `"- [Mistral — Mistral Small 4 model card](https://docs.mistral.ai/models/mistral-small-4-0-26-03)"` | — |
## وثائق وفهرسة

### FILE-21D5D044E2 — [docs/OMARAI_EXCEPTIONS_REGISTER_AR.md](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-21D5D044E2-L000001](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L1) | 1 | `"# Omarai — سجل الاستثناءات والقرارات المؤجلة"` | — |
| [SRC-21D5D044E2-L000002](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L2) | 2 | `""` | — |
| [SRC-21D5D044E2-L000003](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L3) | 3 | `"**المعرف:** OMARAI-EXCEPTIONS-REGISTER-001  "` | — |
| [SRC-21D5D044E2-L000004](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L4) | 4 | `"**التاريخ:** 2026-10-19  "` | — |
| [SRC-21D5D044E2-L000005](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L5) | 5 | `"**الحالة:** مقترح للمراجعة — لم يُعتمد أي استثناء بموجب هذا الملف.  "` | — |
| [SRC-21D5D044E2-L000006](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L6) | 6 | `"**المسؤول عن القرار:** مدير المشروع البشري  "` | — |
| [SRC-21D5D044E2-L000007](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L7) | 7 | ``"**مرجع الحوكمة:** `GOV-003` و`GOV-004` و`GOV-005`"`` | — |
| [SRC-21D5D044E2-L000008](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L8) | 8 | `""` | — |
| [SRC-21D5D044E2-L000009](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L9) | 9 | `"## 1. الغرض وقواعد الاستخدام"` | — |
| [SRC-21D5D044E2-L000010](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L10) | 10 | `""` | — |
| [SRC-21D5D044E2-L000011](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L11) | 11 | ``"يوثق هذا السجل أي استثناء مطلوب من متطلب إلزامي `MUST` أو قرار بتحديد نطاق الإصدار. إعداد هذا السجل أو دمجه لا يعني قبول المخاطر المدرجة."`` | — |
| [SRC-21D5D044E2-L000012](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L12) | 12 | `""` | — |
| [SRC-21D5D044E2-L000013](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L13) | 13 | `"يجب أن يحتوي كل استثناء معتمد على: معرف المتطلب، السبب، النطاق، المخاطر والبيانات/القدرات المتأثرة، البديل التعويضي، صاحب صلاحية الموافقة، تاريخ أو شرط الانتهاء، ودليل إعادة النظر والإغلاق."` | — |
| [SRC-21D5D044E2-L000014](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L14) | 14 | `""` | — |
| [SRC-21D5D044E2-L000015](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L15) | 15 | ``"- `PROPOSED`: مقترح ينتظر قرارًا بشريًا صريحًا."`` | — |
| [SRC-21D5D044E2-L000016](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L16) | 16 | ``"- `WAIVED`: استثناء وافق عليه صاحب الصلاحية، بنطاق وحدود وموعد/شرط انتهاء."`` | — |
| [SRC-21D5D044E2-L000017](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L17) | 17 | ``"- `NOT APPLICABLE`: المتطلب لا ينطبق على نطاق محدد حاليًا مع السبب وشرط إعادة النظر."`` | — |
| [SRC-21D5D044E2-L000018](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L18) | 18 | ``"- `UNKNOWN`: الأدلة لا تكفي للحكم؛ لا يجوز استخدام استثناء لتغطية هذه الحالة."`` | — |
| [SRC-21D5D044E2-L000019](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L19) | 19 | ``"- `NOT RUN`: اختبار مطلوب لم يُنفذ."`` | — |
| [SRC-21D5D044E2-L000020](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L20) | 20 | `""` | — |
| [SRC-21D5D044E2-L000021](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L21) | 21 | `"لا توجد في هذا السجل موافقات بشرية مختلقة أو استثناءات مفتوحة إلى أجل غير محدد. **لا يُسجل أي عنصر كـWAIVED إلا بعد توثيق موافقتك الصريحة.**"` | — |
| [SRC-21D5D044E2-L000022](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L22) | 22 | `""` | — |
| [SRC-21D5D044E2-L000023](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L23) | 23 | `"## 2. سجل الاستثناءات المعتمدة"` | — |
| [SRC-21D5D044E2-L000024](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L24) | 24 | `""` | — |
| [SRC-21D5D044E2-L000025](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L25) | 25 | `"\| معرف الاستثناء \| المتطلب \| النطاق \| الموافِق \| الحالة \| الانتهاء/إعادة النظر \| دليل القرار \|"` | — |
| [SRC-21D5D044E2-L000026](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L26) | 26 | `"\|---\|---\|---\|---\|---\|---\|---\|"` | — |
| [SRC-21D5D044E2-L000027](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L27) | 27 | `"\| — \| — \| لا يوجد استثناء معتمد مسجل في هذا الملف حتى تاريخ اللقطة. \| — \| لا توجد موافقات مسجلة هنا \| — \| لا يثبت ذلك غياب قرار أو موافقة خارج المستودع. \|"` | — |
| [SRC-21D5D044E2-L000028](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L28) | 28 | `""` | — |
| [SRC-21D5D044E2-L000029](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L29) | 29 | `"## 3. مقترحات للمراجعة — ليست استثناءات معتمدة"` | — |
| [SRC-21D5D044E2-L000030](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L30) | 30 | `""` | — |
| [SRC-21D5D044E2-L000031](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L31) | 31 | `"### EX-PROP-001 — حصر النسخة على مشغّل واحد"` | — |
| [SRC-21D5D044E2-L000032](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L32) | 32 | `""` | — |
| [SRC-21D5D044E2-L000033](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L33) | 33 | ``"- **المتطلبات:** `IDN-001` و`IDN-003` ومتطلبات تعدد المستأجرين المشروطة."`` | — |
| [SRC-21D5D044E2-L000034](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L34) | 34 | `"- **المقترح:** تحديد نطاق النسخة التجريبية على أنها خدمة خاصة بمشغّل واحد بدل تقديمها كمنصة متعددة المستخدمين."` | — |
| [SRC-21D5D044E2-L000035](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L35) | 35 | `"- **السبب:** التنفيذ الحالي يستخدم رمز Bearer مشتركًا ومخزن leads مشتركًا؛ لا تظهر هوية فردية أو عزل كامل لبيانات كل مستخدم."` | — |
| [SRC-21D5D044E2-L000036](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L36) | 36 | `"- **المخاطر:** من يحصل على الرمز يحصل على الصلاحيات الممنوحة له؛ قد تختلط بيانات عدة مستخدمين إذا استُخدم النظام على نحو غير مقصود."` | — |
| [SRC-21D5D044E2-L000037](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L37) | 37 | `"- **التعويضات المطلوبة إذا وافق المدير:** إبقاء الخدمة خاصة، استخدام رمز قوي وسري، عدم مشاركة الرمز كأنه حساب مستقل، وعدم إدخال بيانات عملاء مستقلين أو بيانات حساسة."` | — |
| [SRC-21D5D044E2-L000038](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L38) | 38 | `"- **صاحب القرار:** مدير المشروع البشري."` | — |
| [SRC-21D5D044E2-L000039](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L39) | 39 | `"- **الانتهاء/إعادة النظر:** قبل أي عرض عام لعدة مستخدمين، أو تخزين بيانات مستقلة لجهات مختلفة."` | — |
| [SRC-21D5D044E2-L000040](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L40) | 40 | ``"- **الحالة:** `PROPOSED — تنتظر الموافقة`."`` | — |
| [SRC-21D5D044E2-L000041](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L41) | 41 | `""` | — |
| [SRC-21D5D044E2-L000042](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L42) | 42 | `"### EX-PROP-002 — استمرارية البيانات في بيئة تجريبية قابلة للفقد"` | — |
| [SRC-21D5D044E2-L000043](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L43) | 43 | `""` | — |
| [SRC-21D5D044E2-L000044](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L44) | 44 | ``"- **المتطلبات:** `REL-005` و`EXT-002` و`DAT-002` بحسب انطباقها على البيانات المخزنة."`` | — |
| [SRC-21D5D044E2-L000045](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L45) | 45 | `"- **المقترح:** السماح بتجربة لا تعتمد على حفظ بيانات مهمة فقط إذا كانت كل بياناتها اصطناعية أو قابلة لإعادة الإنشاء، مع إبقاء النسخ والاستعادة الدائمة خارج نطاق هذه التجربة."` | — |
| [SRC-21D5D044E2-L000046](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L46) | 46 | `"- **السبب:** النسخ الاحتياطي والاستعادة ودوام تخزين SQLite على مضيف محدد لم تثبت هنا."` | — |
| [SRC-21D5D044E2-L000047](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L47) | 47 | `"- **المخاطر:** فقدان البيانات بعد إعادة إنشاء الحاوية أو تغيير المضيف أو تلف ملف قاعدة البيانات."` | — |
| [SRC-21D5D044E2-L000048](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L48) | 48 | `"- **التعويضات المطلوبة إذا وافق المدير:** عدم إدخال بيانات لا يمكن تعويضها، والتصريح بأن الاستمرارية غير مثبتة."` | — |
| [SRC-21D5D044E2-L000049](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L49) | 49 | `"- **صاحب القرار:** مدير المشروع البشري."` | — |
| [SRC-21D5D044E2-L000050](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L50) | 50 | `"- **الانتهاء/إعادة النظر:** قبل تخزين أي بيانات عمل حقيقية يُعتمد عليها."` | — |
| [SRC-21D5D044E2-L000051](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L51) | 51 | ``"- **الحالة:** `PROPOSED — تنتظر الموافقة`."`` | — |
| [SRC-21D5D044E2-L000052](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L52) | 52 | `""` | — |
| [SRC-21D5D044E2-L000053](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L53) | 53 | `"### EX-PROP-003 — عدم إعلان سعة/توافر غير مقاس"` | — |
| [SRC-21D5D044E2-L000054](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L54) | 54 | `""` | — |
| [SRC-21D5D044E2-L000055](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L55) | 55 | ``"- **المتطلبات:** `PER-004` و`REL-006`، وأي ادعاء أداء أو توافر في `PRD-001`."`` | — |
| [SRC-21D5D044E2-L000056](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L56) | 56 | `"- **المقترح:** عدم نشر أرقام عن throughput أو عدد مستخدمين مدعوم أو نسبة توافر، إلى أن تتوفر قياسات ممثلة."` | — |
| [SRC-21D5D044E2-L000057](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L57) | 57 | `"- **الطبيعة:** هذا في الأساس قيد على الادعاءات، وليس إذنًا بتجاهل ضوابط الأمان أو حدود الموارد."` | — |
| [SRC-21D5D044E2-L000058](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L58) | 58 | `"- **المخاطر:** توقعات غير واقعية من المستخدمين أو توقف الخدمة تحت ضغط لم يُختبر."` | — |
| [SRC-21D5D044E2-L000059](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L59) | 59 | `"- **التعويض:** الإفصاح أن السعة والتوافر غير معروفين، وعدم إعطاء وعود تشغيلية رقمية."` | — |
| [SRC-21D5D044E2-L000060](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L60) | 60 | `"- **صاحب القرار:** مدير المشروع البشري."` | — |
| [SRC-21D5D044E2-L000061](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L61) | 61 | `"- **الانتهاء/إعادة النظر:** عند إجراء اختبار حمل موثق أو تقديم التزام تشغيلي."` | — |
| [SRC-21D5D044E2-L000062](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L62) | 62 | ``"- **الحالة:** `PROPOSED — تنتظر الموافقة`."`` | — |
| [SRC-21D5D044E2-L000063](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L63) | 63 | `""` | — |
| [SRC-21D5D044E2-L000064](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L64) | 64 | `"### EX-PROP-004 — الموصلات الاختيارية غير المتحققة"` | — |
| [SRC-21D5D044E2-L000065](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L65) | 65 | `""` | — |
| [SRC-21D5D044E2-L000066](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L66) | 66 | ``"- **المتطلبات:** `SRH-001` و`TST-005` و`PRD-001`."`` | — |
| [SRC-21D5D044E2-L000067](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L67) | 67 | `"- **المقترح:** عدم إعلان موصل اختياري على أنه يعمل حيًا ما لم ينجح اختبار اتصال فعلي به في بيئة محددة. يكفي توثيقه كقدرة مشروطة بتهيئة صحيحة."` | — |
| [SRC-21D5D044E2-L000068](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L68) | 68 | `"- **الطبيعة:** هذا ليس إعفاء من ضرورة الصدق؛ بل قاعدة لتحديد الادعاء المسموح."` | — |
| [SRC-21D5D044E2-L000069](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L69) | 69 | ``"- **التعويض:** عرض الحالة `NOT_RUN` أو `UNKNOWN` إلى حين إجراء الاختبار."`` | — |
| [SRC-21D5D044E2-L000070](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L70) | 70 | `"- **صاحب القرار:** مدير المشروع البشري عند اعتماد نطاق المنتج."` | — |
| [SRC-21D5D044E2-L000071](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L71) | 71 | `"- **الانتهاء/إعادة النظر:** عند تفعيل الموصل أو الإعلان عنه كقدرة متحققة."` | — |
| [SRC-21D5D044E2-L000072](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L72) | 72 | ``"- **الحالة:** `PROPOSED — تنتظر المراجعة`."`` | — |
| [SRC-21D5D044E2-L000073](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L73) | 73 | `""` | — |
| [SRC-21D5D044E2-L000074](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L74) | 74 | `"## 4. متطلبات لا يجوز اعتبارها مستثناة بهذا السجل"` | — |
| [SRC-21D5D044E2-L000075](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L75) | 75 | `""` | — |
| [SRC-21D5D044E2-L000076](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L76) | 76 | `"لا يمثل أي مقترح أعلاه موافقة على تجاوز:"` | — |
| [SRC-21D5D044E2-L000077](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L77) | 77 | `"- حماية SSRF والحدود الشبكية."` | — |
| [SRC-21D5D044E2-L000078](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L78) | 78 | `"- حماية الطلبات والمهلات الأساسية في API المعرض للإنترنت."` | — |
| [SRC-21D5D044E2-L000079](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L79) | 79 | `"- منع حقن التعليمات من تجاوز سياسة التطبيق أو تسريب الأسرار."` | — |
| [SRC-21D5D044E2-L000080](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L80) | 80 | `"- التحقق من المصادقة والتفويض الملائمين لنطاق الاستخدام."` | — |
| [SRC-21D5D044E2-L000081](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L81) | 81 | `"- الصدق في الاستشهادات وبيان عدم اليقين."` | — |
| [SRC-21D5D044E2-L000082](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L82) | 82 | `"- فحص الأسرار وحماية إعدادات CI/CD."` | — |
| [SRC-21D5D044E2-L000083](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L83) | 83 | `"- اختبار النشر الفعلي قبل الإعلان عن تشغيله."` | — |
| [SRC-21D5D044E2-L000084](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L84) | 84 | `"- اختبار النسخ والاستعادة قبل الاعتماد على بيانات لا يمكن تعويضها."` | — |
| [SRC-21D5D044E2-L000085](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L85) | 85 | `""` | — |
| [SRC-21D5D044E2-L000086](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L86) | 86 | ``"لا يستخدم `NOT APPLICABLE` بدل `UNKNOWN`، ولا يجوز ترقية `PROPOSED` إلى `WAIVED` دون موافقة صريحة قابلة للمراجعة."`` | — |
| [SRC-21D5D044E2-L000087](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L87) | 87 | `""` | — |
| [SRC-21D5D044E2-L000088](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L88) | 88 | `"## 5. سجل قرارات المدير"` | — |
| [SRC-21D5D044E2-L000089](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L89) | 89 | `""` | — |
| [SRC-21D5D044E2-L000090](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L90) | 90 | `"لم تُسجل موافقات في هذا الملف حتى تاريخ الإنشاء. تُضاف الموافقة فقط بعد صدورها صراحة، ويجب أن تتضمن معرف الاستثناء الذي وافق المدير عليه ونطاقه وشروطه. لن يُستنتج القبول من الصمت أو من اعتماد مهام التطوير."` | — |
| [SRC-21D5D044E2-L000091](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L91) | 91 | `""` | — |
| [SRC-21D5D044E2-L000092](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L92) | 92 | `"## 6. مراجعة دورية وإغلاق"` | — |
| [SRC-21D5D044E2-L000093](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L93) | 93 | `""` | — |
| [SRC-21D5D044E2-L000094](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L94) | 94 | `"عند انتهاء كل استثناء أو تغير النطاق:"` | — |
| [SRC-21D5D044E2-L000095](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L95) | 95 | `"1. أعد تشغيل اختبار القبول المناسب."` | — |
| [SRC-21D5D044E2-L000096](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L96) | 96 | `"2. سجل الدليل الجديد وربطه بالـSHA والبيئة."` | — |
| [SRC-21D5D044E2-L000097](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L97) | 97 | `"3. حدّد هل أُغلق الاستثناء أم يحتاج تجديدًا بموافقة جديدة."` | — |
| [SRC-21D5D044E2-L000098](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L98) | 98 | `"4. لا تمدد الاستثناء تلقائيًا."` | — |
| [SRC-21D5D044E2-L000099](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L99) | 99 | `"5. احتفظ بسجل القرار السابق بدل محوه."` | — |
## وثائق وفهرسة

### FILE-E73001D9AC — [docs/OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-E73001D9AC-L000001](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L1) | 1 | `"# Omarai — الدستور التأسيسي للهندسة والموثوقية والأمان والذكاء"` | — |
| [SRC-E73001D9AC-L000002](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L2) | 2 | `""` | — |
| [SRC-E73001D9AC-L000003](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L3) | 3 | `"**معرّف الوثيقة:** OMARAI-FOUNDATION-CHARTER-001  "` | — |
| [SRC-E73001D9AC-L000004](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L4) | 4 | `"**الإصدار:** 1.3.0  "` | — |
| [SRC-E73001D9AC-L000005](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L5) | 5 | `"**الحالة:** مرجع تأسيسي معتمد بعد دمج PR #42 بتاريخ 19 أكتوبر 2026؛ تضبط متطلباته اتجاه التصميم والمراجعة، ولا تثبت بمفردها أن الضوابط نُفذت أو اختُبرت  "` | — |
| [SRC-E73001D9AC-L000006](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L6) | 6 | `"**النطاق:** جميع مكونات Omarai البرمجية والتشغيلية، وواجهات API، والواجهة العربية، ومحركات البحث، والنماذج، والأدوات، والبيانات، والاستضافة، وسير التطوير والاختبار  "` | — |
| [SRC-E73001D9AC-L000007](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L7) | 7 | `"**الأولوية:** مرجع تصميم وحوكمة؛ لا يثبت بمفرده أن أي قدرة نُفّذت أو اختُبرت  "` | — |
| [SRC-E73001D9AC-L000008](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L8) | 8 | `"**اللغة:** العربية هي لغة الشرح الأساسية، مع استخدام أسماء المصطلحات التقنية الإنجليزية لتوحيد التنفيذ والمراجعة"` | — |
| [SRC-E73001D9AC-L000009](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L9) | 9 | `""` | — |
| [SRC-E73001D9AC-L000010](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L10) | 10 | `"> **القاعدة العليا:** Omarai لا يدّعي قدرة غير مثبتة. كل قدرة مهمة يجب أن تقابلها آلية تنفيذ محددة واختبار قابل لإعادة التشغيل ودليل ناتج عن بيئة معروفة. الاختبارات والقياسات الفعلية مقدّمة على الأوصاف والوعود."` | — |
| [SRC-E73001D9AC-L000011](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L11) | 11 | `""` | — |
| [SRC-E73001D9AC-L000012](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L12) | 12 | `"---"` | — |
| [SRC-E73001D9AC-L000013](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L13) | 13 | `""` | — |
| [SRC-E73001D9AC-L000014](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L14) | 14 | `"> **مراجع مكملة للمراجعات الواسعة:** تُقرأ هذه الوثيقة مع [خط الأساس الهندسي للمنصات العالمية واسعة النطاق](OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md)، ومع [سجل المتطلبات والتتبع والنضج وبوابات الاعتماد](OMARAI_REQUIREMENTS_TRACEABILITY_AND_MATURITY_MODEL_AR.md)، ومع [سجل المتطلبات الأساسية الأولي](OMARAI_REQUIREMENTS_REGISTER.md). وتُقرأ أيضًا مع [المعمارية الحاكمة للقدرات والمهارات وسير العمل والوكلاء](OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md)، التي تفصل مسار التوسع من النواة إلى المهارات وسير العمل والوكلاء. هذه الوثائق مكملة بعضها لبعض وليست بدائل متنافسة؛ لا تثبت أي وثيقة وحدها أن الضوابط نُفذت."` | — |
| [SRC-E73001D9AC-L000015](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L15) | 15 | `""` | — |
| [SRC-E73001D9AC-L000016](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L16) | 16 | `"## 0. كيف تُقرأ هذه الوثيقة؟"` | — |
| [SRC-E73001D9AC-L000017](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L17) | 17 | `""` | — |
| [SRC-E73001D9AC-L000018](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L18) | 18 | `"تستخدم الوثيقة الكلمات التالية بدقة:"` | — |
| [SRC-E73001D9AC-L000019](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L19) | 19 | `""` | — |
| [SRC-E73001D9AC-L000020](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L20) | 20 | `"- **MUST / إلزامي:** شرط لا يجوز تجاوزه في التنفيذ المستهدف أو الإصدار الذي يدّعي استيفاءه."` | — |
| [SRC-E73001D9AC-L000021](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L21) | 21 | `"- **SHOULD / مطلوب افتراضيًا:** يُطبّق ما لم يوجد سبب موثق ومراجع لاستثناء محدود."` | — |
| [SRC-E73001D9AC-L000022](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L22) | 22 | `"- **MAY / اختياري:** يُطبّق عندما يحقق قيمة مثبتة ولا يضيف مخاطر غير مقبولة."` | — |
| [SRC-E73001D9AC-L000023](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L23) | 23 | `"- **VERIFIED / متحقق:** تؤيده نتيجة فحص أو اختبار أو قياس محدد يمكن الرجوع إليه."` | — |
| [SRC-E73001D9AC-L000024](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L24) | 24 | `"- **INFERRED / مستنتج:** تفسير مرجح مبني على الأدلة المتاحة، وليس حقيقة اختبارية."` | — |
| [SRC-E73001D9AC-L000025](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L25) | 25 | `"- **PROPOSED / مقترح:** قرار تصميم أو هدف لم يُثبت تنفيذه بعد."` | — |
| [SRC-E73001D9AC-L000026](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L26) | 26 | `"- **UNKNOWN / غير معلوم:** لا تتوفر أدلة كافية للحكم."` | — |
| [SRC-E73001D9AC-L000027](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L27) | 27 | `""` | — |
| [SRC-E73001D9AC-L000028](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L28) | 28 | `"هذه الوثيقة **متطلبات مستقبلية ومعيار مراجعة**، وليست إعلانًا بأن المستودع الحالي يحققها. يجب أن يُسجّل لكل بند مهم: حالته، والدليل، والمخاطر المفتوحة، وخطة المعالجة، والمسؤول عن التحقق. لا تُحوّل كلمة PROPOSED إلى VERIFIED إلا بدليل فعلي."` | — |
| [SRC-E73001D9AC-L000029](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L29) | 29 | `""` | — |
| [SRC-E73001D9AC-L000030](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L30) | 30 | `"---"` | — |
| [SRC-E73001D9AC-L000031](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L31) | 31 | `""` | — |
| [SRC-E73001D9AC-L000032](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L32) | 32 | `"# الجزء الأول — الرسالة العليا ومبادئ التصميم"` | — |
| [SRC-E73001D9AC-L000033](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L33) | 33 | `""` | — |
| [SRC-E73001D9AC-L000034](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L34) | 34 | `"## 1. الرؤية"` | — |
| [SRC-E73001D9AC-L000035](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L35) | 35 | `""` | — |
| [SRC-E73001D9AC-L000036](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L36) | 36 | `"بناء Omarai كنواة ذكاء اصطناعي عربية عملية تستطيع استقبال الأسئلة والمهام، وفهمها، والبحث عند الحاجة، واستخدام الأدوات التي ثبت عملها، وتوليد إجابات مستندة إلى الأدلة، وإظهار حدود المعرفة بوضوح؛ مع هندسة تتيح النمو من نموذج أولي محدود إلى خدمة إنتاجية موثوقة عندما تسمح الموارد والاستضافة بذلك."` | — |
| [SRC-E73001D9AC-L000037](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L37) | 37 | `""` | — |
| [SRC-E73001D9AC-L000038](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L38) | 38 | `"الطموح هو بلوغ مستوى احترافي في الاعتمادية والأمان والكفاءة، مع الاستفادة من الممارسات الصناعية المعروفة. لا يعني ذلك ادعاء التكافؤ مع المنصات العالمية قبل وجود بنية تشغيلية وميزانية واختبارات وتدقيق خارجي مناسب."` | — |
| [SRC-E73001D9AC-L000039](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L39) | 39 | `""` | — |
| [SRC-E73001D9AC-L000040](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L40) | 40 | `"### 1.1 هوية المنتج وحدوده التجارية"` | — |
| [SRC-E73001D9AC-L000041](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L41) | 41 | `""` | — |
| [SRC-E73001D9AC-L000042](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L42) | 42 | `"**اتجاه المنتج المعتمد:** Omarai وكيل عربي أولًا لذكاء المبيعات واكتساب العملاء، متعدد المنتجات والقطاعات والأسواق. يبدأ من ملف منتج/خدمة وسوق مستهدف، ويبحث في المصادر العامة والمسموح بها عن إشارات احتياج أو طلب معلنة، ويربطها بأدلة ومصدر وتاريخ، ويفصل بين الطلب المباشر والاحتياج والمؤشرات غير المباشرة وتطابق العميل المستهدف فقط، ثم يساعد على تأهيل الفرصة واقتراح متابعة مبيعات مناسبة."` | — |
| [SRC-E73001D9AC-L000043](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L43) | 43 | `""` | — |
| [SRC-E73001D9AC-L000044](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L44) | 44 | `"هذا الاتجاه يحدد **غاية المنتج** ولا يثبت اكتمال دورة المبيعات. تظل معمارية المجال في [معمارية ذكاء المبيعات واكتساب العملاء](OMARAI_SALES_INTELLIGENCE_ARCHITECTURE_AR.md) المرجع التفصيلي للـProductProfile وMarket/ICP وتصنيف الإشارات وسجل الأدلة والتأهيل."` | — |
| [SRC-E73001D9AC-L000045](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L45) | 45 | `""` | — |
| [SRC-E73001D9AC-L000046](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L46) | 46 | `"قواعد نطاق المنتج:"` | — |
| [SRC-E73001D9AC-L000047](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L47) | 47 | `"- لا يُعتبر تطابق ICP أو تشابه اسم/نشاط شركة دليلًا على نية شراء."` | — |
| [SRC-E73001D9AC-L000048](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L48) | 48 | `"- لا تُجمع بيانات الاتصال لمجرد مطابقة ملف العميل المستهدف؛ الأولوية لإشارة الطلب ودليلها."` | — |
| [SRC-E73001D9AC-L000049](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L49) | 49 | `"- لا يتم إرسال رسائل أو عروض أو تواصل آلي في النطاق الأولي؛ أي تواصل لاحق يحتاج تفويضًا وضوابط مستقلة ومراجعة بشرية."` | — |
| [SRC-E73001D9AC-L000050](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L50) | 50 | `"- لا تتجاوز المهارات أو الموصلات تسجيل الدخول أو شروط الاستخدام أو حدود الوصول للمصدر."` | — |
| [SRC-E73001D9AC-L000051](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L51) | 51 | `"- البحث العام وRAG والنماذج والموصلات وسائل مشتركة؛ المخرج التجاري هو فرصة مفهومة ومدعومة بالدليل، لا قائمة نتائج بحث."` | — |
| [SRC-E73001D9AC-L000052](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L52) | 52 | `""` | — |
| [SRC-E73001D9AC-L000053](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L53) | 53 | `"### 1.2 قرار نموذج التشغيل متعدد المستأجرين"` | — |
| [SRC-E73001D9AC-L000054](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L54) | 54 | `""` | — |
| [SRC-E73001D9AC-L000055](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L55) | 55 | ``"**قرار معماري منفذ على main عبر PR #145:** `Multi-Tenant Architecture — Single-Tenant Initial Operation`. يبدأ التشغيل الأولي لشركة واحدة، مع وجود نموذج tenant/user/membership وربط السجلات والجلسات والصلاحيات بالمستأجر من جهة الخادم. لا يُقبل `tenant_id` من المتصفح أو جسم الطلب بوصفه مصدر صلاحية؛ يجب اشتقاق نطاق الوصول من هوية موثوقة والتحقق من الملكية عند كل عملية."`` | — |
| [SRC-E73001D9AC-L000056](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L56) | 56 | `""` | — |
| [SRC-E73001D9AC-L000057](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L57) | 57 | `"دمج نواة العزل لا يثبت وحده جاهزية SaaS متعدد الشركات: إدارة المستخدمين والعضويات الذاتية، والقبول المستضاف، ودوام التخزين والنسخ الاحتياطي والاستعادة يجب أن تثبت منفصلة قبل هذا الادعاء."` | — |
| [SRC-E73001D9AC-L000058](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L58) | 58 | `""` | — |
| [SRC-E73001D9AC-L000059](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L59) | 59 | `"## 2. المبادئ الحاكمة غير القابلة للتفاوض"` | — |
| [SRC-E73001D9AC-L000060](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L60) | 60 | `""` | — |
| [SRC-E73001D9AC-L000061](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L61) | 61 | `"1. **Evidence over assertion:** لا نعلن نجاحًا بلا دليل."` | — |
| [SRC-E73001D9AC-L000062](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L62) | 62 | `"2. **Security by design:** الأمن جزء من التصميم ودورة التطوير، لا طبقة تجميلية لاحقة."` | — |
| [SRC-E73001D9AC-L000063](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L63) | 63 | `"3. **Reliability before feature growth:** لا نضيف قدرات تُضعف الاستقرار أو تفتح صلاحيات غير مضبوطة."` | — |
| [SRC-E73001D9AC-L000064](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L64) | 64 | `"4. **Least privilege:** أقل صلاحية لازمة لكل مستخدم ومكوّن وأداة."` | — |
| [SRC-E73001D9AC-L000065](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L65) | 65 | `"5. **Fail safely, degrade gracefully:** تعطل مكوّن لا ينبغي أن يسقط النظام كله، والفشل يجب أن يكون محدود الأثر وواضحًا."` | — |
| [SRC-E73001D9AC-L000066](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L66) | 66 | `"6. **Bound every expensive operation:** كل بحث أو استدعاء نموذج أو جلب صفحة أو حلقة تخطيط أو إعادة محاولة له حدود زمنية وكمية وتكلفة."` | — |
| [SRC-E73001D9AC-L000067](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L67) | 67 | `"7. **Simple path first:** السؤال البسيط يسلك المسار الأقصر؛ لا نستدعي التخطيط العميق أو الإنترنت بلا حاجة."` | — |
| [SRC-E73001D9AC-L000068](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L68) | 68 | `"8. **Independent verification:** لا نعتبر مراجعة النموذج لنفسه تحققًا مستقلًا، ولا نعتبر اتفاق محركات البحث إثباتًا للحقيقة."` | — |
| [SRC-E73001D9AC-L000069](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L69) | 69 | `"9. **Privacy by default:** نجمع أقل بيانات لازمة، ونوضح ما يغادر النظام إلى مزودي الخدمة."` | — |
| [SRC-E73001D9AC-L000070](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L70) | 70 | `"10. **Separation of concerns:** حدود واضحة بين الطلبات، والتخطيط، والبحث، وتنفيذ الأدوات، والتحقق، والبيانات، والمراقبة."` | — |
| [SRC-E73001D9AC-L000071](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L71) | 71 | `"11. **Observable behavior:** يجب أن يمكن قياس النجاح والفشل والبطء والاستهلاك، مع حماية الخصوصية."` | — |
| [SRC-E73001D9AC-L000072](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L72) | 72 | `"12. **Reversible decisions:** التغييرات الهندسية الكبيرة تمر عبر قرارات موثقة ويمكن التراجع عنها."` | — |
| [SRC-E73001D9AC-L000073](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L73) | 73 | `"13. **Human control for consequential actions:** لا تمنح النماذج استقلالًا مفتوحًا لإجراء تغييرات حساسة أو آثار خارجية."` | — |
| [SRC-E73001D9AC-L000074](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L74) | 74 | `"14. **No “security by obscurity”:** الحماية تعتمد على ضوابط واختبارات وصلاحيات، لا على إخفاء تفاصيل التصميم."` | — |
| [SRC-E73001D9AC-L000075](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L75) | 75 | `"15. **Cost-aware engineering:** نختار التعقيد والاعتماديات وفق منفعة مقاسة وتكلفة ومخاطر حقيقية، لا لمجرد أن المعمارية تبدو أكبر."` | — |
| [SRC-E73001D9AC-L000076](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L76) | 76 | `"16. **Arabic-first quality:** دعم العربية واتجاه RTL وجودة البحث والاستشهادات جزء من الجودة الأساسية، وليس تحسينًا ثانويًا."` | — |
| [SRC-E73001D9AC-L000077](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L77) | 77 | `"17. **No false universality:** لا نقول إن الأداة تعمل دائمًا، أو إن كل موقع قابل للاستخراج، أو إن كل سؤال يمكن الإجابة عنه يقينًا."` | — |
| [SRC-E73001D9AC-L000078](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L78) | 78 | `"18. **Owner-controlled release:** لا يتم دمج تغييرات جوهرية أو إطلاقها باعتبارها معتمدة نهائيًا دون قرار صاحب المشروع."` | — |
| [SRC-E73001D9AC-L000079](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L79) | 79 | `""` | — |
| [SRC-E73001D9AC-L000080](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L80) | 80 | `"## 3. الطموح الأقصى لا يعني تعقيدًا أقصى"` | — |
| [SRC-E73001D9AC-L000081](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L81) | 81 | `""` | — |
| [SRC-E73001D9AC-L000082](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L82) | 82 | `"يُراجع Omarai بأوسع تغطية تخصصية ممكنة، لكن لا تُنشأ طبقات تشغيلية أو خدمات مستقلة لمجرد زيادة العدد. المقصود هو **أقصى تغطية مفيدة للمخاطر والتخصصات، وأقل تعقيد تشغيلي يحققها**. يبدأ المشروع بوحدات منطقية واضحة؛ ثم تُفصل الخدمات أو تُضاف البنية الموزعة عندما تثبت اختبارات الحمل أو حدود العزل أو التوافر الحاجة إلى ذلك."` | — |
| [SRC-E73001D9AC-L000083](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L83) | 83 | `""` | — |
| [SRC-E73001D9AC-L000084](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L84) | 84 | `"### 3.1 قاعدة حاكمة لتنظيم القدرات والمهارات والوكلاء"` | — |
| [SRC-E73001D9AC-L000085](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L85) | 85 | `""` | — |
| [SRC-E73001D9AC-L000086](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L86) | 86 | `"**[PROPOSED — اعتماد بشري مطلوب]** يكون الاتجاه الافتراضي لتطور القدرات هو: نواة موثوقة ← أدوات وقدرات بعقود وصلاحيات واضحة ← مهارات قابلة لإعادة الاستخدام ← سير عمل محدود وقابل للاختبار ← سياق تنفيذ مؤقت لكل مهمة ← وكلاء يُنشؤون عند ثبوت الحاجة. ولا يُنشأ وكيل مستقل لكل سؤال أو تخصص تلقائيًا."` | — |
| [SRC-E73001D9AC-L000087](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L87) | 87 | `""` | — |
| [SRC-E73001D9AC-L000088](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L88) | 88 | `"- الأداة تنفذ عملية بعقد معلوم؛ والقدرة تحدد ما يُسمح به؛ والمهارة تجمع منطقًا قابلًا لإعادة الاستخدام؛ وسير العمل يحدد ترتيب الخطوات وشروط التوقف؛ وملف تعريف الوكيل وصفة لإعادة الاستخدام، لا برنامج حر."` | — |
| [SRC-E73001D9AC-L000089](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L89) | 89 | `"- الخطة التي يقترحها النموذج بيانات غير موثوقة حتى تُفحص بنيتها وصلاحياتها وميزانيتها؛ لا تمنح أي خطة أو مهارة أو ملف تعريف صلاحيات لنفسه."` | — |
| [SRC-E73001D9AC-L000090](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L90) | 90 | `"- يكون سياق التشغيل مؤقتًا ومعزولًا افتراضيًا. لا تُضاف ذاكرة دائمة أو وكيل دائم إلا لمطلب واضح وسياسة احتفاظ وصلاحيات واختبارات مناسبة."` | — |
| [SRC-E73001D9AC-L000091](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L91) | 91 | `"- تُفصل إدارة المسودات والتعريفات والاعتماد منطقيًا عن تشغيل المهام. لا يستطيع النموذج أو Meta-Agent اعتماد نفسه أو تعديل سقف صلاحيات المنصة."` | — |
| [SRC-E73001D9AC-L000092](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L92) | 92 | `"- لا يُنشأ Meta-Agent ولا يُسمح بتوليد كود تنفيذي في المسار الأساسي قبل إثبات الحاجة بفحوص وقياسات؛ وإذا أضيف Meta-Agent مستقبلًا، يبدأ بإنتاج مسودات تعريفية فقط، تمر بالتحقق والاختبارات والموافقة."` | — |
| [SRC-E73001D9AC-L000093](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L93) | 93 | `"- تبقى مهام البحث والأدلة والأمان والتحقق في الدستور قائمة وواجبة؛ لا يستبدل التنظيم الجديد للقدرات هذه الضوابط."` | — |
| [SRC-E73001D9AC-L000094](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L94) | 94 | `""` | — |
| [SRC-E73001D9AC-L000095](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L95) | 95 | `"التفصيل التنفيذي وبوابات الانتقال موضح في [المعمارية الحاكمة للقدرات والمهارات وسير العمل والوكلاء](OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md). هذا توجيه معماري مستهدف، وليس ادعاءً بأن مكوناته كلها منفذة."` | — |
| [SRC-E73001D9AC-L000096](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L96) | 96 | `""` | — |
| [SRC-E73001D9AC-L000097](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L97) | 97 | `"---"` | — |
| [SRC-E73001D9AC-L000098](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L98) | 98 | `""` | — |
| [SRC-E73001D9AC-L000099](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L99) | 99 | `"# الجزء الثاني — حوكمة الخبراء والمراجعة متعددة التخصصات"` | — |
| [SRC-E73001D9AC-L000100](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L100) | 100 | `""` | — |
| [SRC-E73001D9AC-L000101](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L101) | 101 | `"## 4. مجالات الخبرة التي يجب تغطيتها"` | — |
| [SRC-E73001D9AC-L000102](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L102) | 102 | `""` | — |
| [SRC-E73001D9AC-L000103](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L103) | 103 | `"في القرارات المعمارية والأمنية عالية التأثير، تُراجع الآثار من زوايا التخصصات المناسبة التالية. هذه قائمة تغطية للمراجعة، وليست ادعاءً بأن مجموعة خبراء أو وكلاء آليين تعمل حاليًا داخل المستودع."` | — |
| [SRC-E73001D9AC-L000104](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L104) | 104 | `""` | — |
| [SRC-E73001D9AC-L000105](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L105) | 105 | `"1. هندسة البرمجيات والمعمارية."` | — |
| [SRC-E73001D9AC-L000106](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L106) | 106 | `"2. هندسة الأنظمة والتزامن وإدارة الموارد."` | — |
| [SRC-E73001D9AC-L000107](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L107) | 107 | `"3. SRE والاعتمادية والتعافي من الأعطال."` | — |
| [SRC-E73001D9AC-L000108](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L108) | 108 | `"4. الأمن السيبراني وهندسة التهديدات."` | — |
| [SRC-E73001D9AC-L000109](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L109) | 109 | `"5. أمن تطبيقات الويب وواجهات API."` | — |
| [SRC-E73001D9AC-L000110](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L110) | 110 | `"6. أمن تطبيقات LLM والوكلاء ومقاومة حقن التعليمات."` | — |
| [SRC-E73001D9AC-L000111](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L111) | 111 | `"7. أمن الشبكات والـ DNS وقيود الخروج إلى الإنترنت."` | — |
| [SRC-E73001D9AC-L000112](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L112) | 112 | `"8. هندسة الأداء واختبارات الحمل."` | — |
| [SRC-E73001D9AC-L000113](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L113) | 113 | `"9. هندسة البيانات وقواعد البيانات والمخططات والترحيلات."` | — |
| [SRC-E73001D9AC-L000114](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L114) | 114 | `"10. هندسة البحث والاسترجاع وترتيب النتائج."` | — |
| [SRC-E73001D9AC-L000115](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L115) | 115 | `"11. تقييم النماذج والهلوسة والتحقق من الادعاءات."` | — |
| [SRC-E73001D9AC-L000116](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L116) | 116 | `"12. الخصوصية وحوكمة البيانات والاحتفاظ بها."` | — |
| [SRC-E73001D9AC-L000117](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L117) | 117 | `"13. DevOps وسير CI/CD والتوزيع والتراجع."` | — |
| [SRC-E73001D9AC-L000118](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L118) | 118 | `"14. أمن سلسلة التوريد البرمجية والاعتماديات."` | — |
| [SRC-E73001D9AC-L000119](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L119) | 119 | `"15. ضمان الجودة والاختبارات الآلية واختبارات الفشل."` | — |
| [SRC-E73001D9AC-L000120](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L120) | 120 | `"16. التصميم وتجربة المستخدم وإمكانية الوصول وRTL."` | — |
| [SRC-E73001D9AC-L000121](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L121) | 121 | `"17. جودة اللغة العربية والتوطين واتجاهات النصوص."` | — |
| [SRC-E73001D9AC-L000122](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L122) | 122 | `"18. التكلفة والقيود التشغيلية واستهلاك حصص الخدمات المجانية."` | — |
| [SRC-E73001D9AC-L000123](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L123) | 123 | `"19. إدارة الحوادث والاستجابة الأمنية والتعافي من الكوارث."` | — |
| [SRC-E73001D9AC-L000124](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L124) | 124 | `"20. الحوكمة والتوثيق وإدارة التغيير."` | — |
| [SRC-E73001D9AC-L000125](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L125) | 125 | `""` | — |
| [SRC-E73001D9AC-L000126](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L126) | 126 | `"### 4.1 قاعدة المراجعة"` | — |
| [SRC-E73001D9AC-L000127](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L127) | 127 | `""` | — |
| [SRC-E73001D9AC-L000128](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L128) | 128 | `"- التغييرات الصغيرة منخفضة المخاطر تخضع لاختبارات الوحدة والمراجعة المعتادة."` | — |
| [SRC-E73001D9AC-L000129](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L129) | 129 | `"- التغييرات التي تمس الإنترنت أو الصلاحيات أو الذاكرة المشتركة أو التخزين أو تنفيذ الأدوات تخضع لمراجعة أمنية واختبارات فشل مناسبة."` | — |
| [SRC-E73001D9AC-L000130](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L130) | 130 | `"- التغييرات التي تمس المعمارية أو التوسع أو حدود الثقة تخضع لمراجعة معمارية، وتهديدات، وأداء، وتشغيل، وتوثيق قرار."` | — |
| [SRC-E73001D9AC-L000131](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L131) | 131 | `"- عند تعارض آراء المراجعين، يُسجّل التعارض والأدلة والبدائل والمخاطر بدل إخفائه خلف تصويت عددي أو إجابة نموذج لغوي واحدة."` | — |
| [SRC-E73001D9AC-L000132](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L132) | 132 | `"- لا تُستخدم أسماء خبراء أو مراجعات آلية مزعومة كدليل. يُذكر ما إذا كانت المراجعة بشرية أو آلية أو مجرد قائمة تحقق."` | — |
| [SRC-E73001D9AC-L000133](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L133) | 133 | `""` | — |
| [SRC-E73001D9AC-L000134](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L134) | 134 | `"---"` | — |
| [SRC-E73001D9AC-L000135](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L135) | 135 | `""` | — |
| [SRC-E73001D9AC-L000136](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L136) | 136 | `"# الجزء الثالث — المعمارية المنطقية المستهدفة"` | — |
| [SRC-E73001D9AC-L000137](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L137) | 137 | `""` | — |
| [SRC-E73001D9AC-L000138](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L138) | 138 | `"## 5. طبقات النظام وحدود الثقة"` | — |
| [SRC-E73001D9AC-L000139](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L139) | 139 | `""` | — |
| [SRC-E73001D9AC-L000140](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L140) | 140 | `"التقسيم التالي **خريطة منطقية مرجعية**. يجوز دمج طبقات عدة داخل تطبيق واحد في المراحل الأولى، بشرط الحفاظ على حدود المسؤوليات واختبارها. ولا يُشترط أن تتحول كل طبقة إلى خدمة مستقلة."` | — |
| [SRC-E73001D9AC-L000141](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L141) | 141 | `""` | — |
| [SRC-E73001D9AC-L000142](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L142) | 142 | `"### الطبقة 1 — واجهة المستخدم وقنوات الإدخال"` | — |
| [SRC-E73001D9AC-L000143](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L143) | 143 | `"- واجهة عربية RTL واضحة ومتجاوبة."` | — |
| [SRC-E73001D9AC-L000144](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L144) | 144 | `"- تمييز حالة الطلب: مستلم، قيد التنفيذ، مكتمل، متدهور، فشل."` | — |
| [SRC-E73001D9AC-L000145](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L145) | 145 | `"- عرض المصادر والتحذيرات وحدود المعرفة عند الحاجة."` | — |
| [SRC-E73001D9AC-L000146](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L146) | 146 | `"- عدم وضع مفاتيح أو أسرار أو صلاحيات خادم في كود المتصفح."` | — |
| [SRC-E73001D9AC-L000147](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L147) | 147 | `"- عدم اعتبار إخفاء زر في الواجهة وسيلة لتطبيق الصلاحيات؛ يجب فرض الصلاحيات في الخادم."` | — |
| [SRC-E73001D9AC-L000148](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L148) | 148 | `""` | — |
| [SRC-E73001D9AC-L000149](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L149) | 149 | `"### الطبقة 2 — حافة الخدمة وواجهة API"` | — |
| [SRC-E73001D9AC-L000150](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L150) | 150 | `"- التحقق الصارم من بنية الطلب وأنواعه وأحجامه."` | — |
| [SRC-E73001D9AC-L000151](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L151) | 151 | `"- حدود حجم الجسم والمهلات والاتصالات ومعدل الطلبات."` | — |
| [SRC-E73001D9AC-L000152](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L152) | 152 | `"- أخطاء واضحة لا تكشف تفاصيل داخلية أو مسارات ملفات أو أسرارًا."` | — |
| [SRC-E73001D9AC-L000153](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L153) | 153 | `"- سياسة CORS مقيدة بالنطاقات المعتمدة."` | — |
| [SRC-E73001D9AC-L000154](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L154) | 154 | `"- عند استخدام ملفات تعريف الارتباط للمصادقة، تُراجع حماية CSRF وخصائص Secure وHttpOnly وSameSite بحسب تصميم الجلسة."` | — |
| [SRC-E73001D9AC-L000155](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L155) | 155 | `"- واجهات التشخيص والإدارة لا تُعرض للعامة دون حماية مناسبة."` | — |
| [SRC-E73001D9AC-L000156](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L156) | 156 | `""` | — |
| [SRC-E73001D9AC-L000157](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L157) | 157 | `"### الطبقة 3 — الهوية والمستأجرون والصلاحيات"` | — |
| [SRC-E73001D9AC-L000158](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L158) | 158 | `"- لكل مستخدم أو جلسة أو مهمة معرف واضح ونطاق صلاحيات."` | — |
| [SRC-E73001D9AC-L000159](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L159) | 159 | `"- فصل تام بين سياق الطلبات المتزامنة ومنع مشاركة المتغيرات القابلة للتغيير بين المستخدمين."` | — |
| [SRC-E73001D9AC-L000160](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L160) | 160 | `"- تحقق من ملكية كل سجل قبل قراءته أو تعديله أو تصديره."` | — |
| [SRC-E73001D9AC-L000161](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L161) | 161 | `"- لا يكفي تخمين معرف غير قابل للتسلسل لمنع الوصول غير المصرح به؛ يجب التحقق من الصلاحية على الخادم."` | — |
| [SRC-E73001D9AC-L000162](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L162) | 162 | `"- يظل وضع الحلقة المحلية أو الاستخدام الشخصي مختلفًا عن وضع خدمة عامة متعددة المستخدمين، ويجب توثيق الوضع الفعلي لكل نشر."` | — |
| [SRC-E73001D9AC-L000163](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L163) | 163 | `""` | — |
| [SRC-E73001D9AC-L000164](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L164) | 164 | `"### الطبقة 4 — بوابة السياسات وإساءة الاستخدام"` | — |
| [SRC-E73001D9AC-L000165](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L165) | 165 | `"- تحديد أحجام الإدخال والتاريخ المرفق وعدد المصادر والصفحات وعمق المهام."` | — |
| [SRC-E73001D9AC-L000166](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L166) | 166 | `"- تحديد معدل الطلبات وفق الهوية وعنوان المصدر عند ملاءمة ذلك، مع مراعاة NAT والخصوصية."` | — |
| [SRC-E73001D9AC-L000167](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L167) | 167 | `"- فرض ميزانيات للوقت والموارد واستهلاك النموذج والبحث."` | — |
| [SRC-E73001D9AC-L000168](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L168) | 168 | `"- إرجاع 429 عند تجاوز حدود المعدل و503 عند العجز المؤقت عن القبول، مع Retry-After عند ملاءمته."` | — |
| [SRC-E73001D9AC-L000169](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L169) | 169 | `"- حماية الخدمة من حلقات الوكيل غير المنتهية، والطلبات المتضخمة، وإساءة استخدام العمليات المكلفة."` | — |
| [SRC-E73001D9AC-L000170](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L170) | 170 | `"- إضافة CAPTCHA أو تحديات إضافية فقط عند وجود دليل على إساءة استخدام، لا كبديل عن حدود موارد صحيحة."` | — |
| [SRC-E73001D9AC-L000171](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L171) | 171 | `""` | — |
| [SRC-E73001D9AC-L000172](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L172) | 172 | `"### الطبقة 5 — منسق الطلبات (Request Orchestrator)"` | — |
| [SRC-E73001D9AC-L000173](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L173) | 173 | `"- إنشاء سياق مستقل لكل طلب يتضمن deadline وميزانيات محددة وإشارة إلغاء."` | — |
| [SRC-E73001D9AC-L000174](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L174) | 174 | `"- الحفاظ على حدود واضحة لعدد خطوات التخطيط واستدعاءات الأدوات واستدعاءات النماذج والصفحات."` | — |
| [SRC-E73001D9AC-L000175](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L175) | 175 | `"- إنهاء الطلب عند بلوغ الميزانية بدل الاستمرار غير المحدود."` | — |
| [SRC-E73001D9AC-L000176](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L176) | 176 | `"- تمييز الإلغاء بسبب المستخدم من انتهاء الوقت ومن رفض السياسة ومن تعطل المزود."` | — |
| [SRC-E73001D9AC-L000177](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L177) | 177 | `"- تمكين إلغاء المهام التابعة عند إلغاء الطلب الأصلي."` | — |
| [SRC-E73001D9AC-L000178](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L178) | 178 | `"- الحفاظ على معرف تتبع واحد عبر مراحل الطلب، دون وضع أسرار أو بيانات حساسة في المعرف."` | — |
| [SRC-E73001D9AC-L000179](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L179) | 179 | `""` | — |
| [SRC-E73001D9AC-L000180](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L180) | 180 | `"ملاحظة تنفيذية حاكمة: يُنشأ سياق وميزانية منفصلان لكل طلب، ويستخدم المنسق أبسط مسار كافٍ للمهمة. تكون مطابقة المهارات وسير العمل المسجلين هي الخيار الأول قبل إنشاء تعريف وكيل جديد. لا يلزم أن يكون التخطيط مكوّنًا مستقلًا أو خدمة خارجية؛ تحفظ الواجهة والعقد وحدود الصلاحيات حتى لو نُفذت داخل وحدة واحدة."` | — |
| [SRC-E73001D9AC-L000181](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L181) | 181 | `""` | — |
| [SRC-E73001D9AC-L000182](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L182) | 182 | `"### الطبقة 6 — فهم النية والتخطيط"` | — |
| [SRC-E73001D9AC-L000183](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L183) | 183 | `"- مسار مباشر للأسئلة البسيطة التي لا تحتاج إلى بحث."` | — |
| [SRC-E73001D9AC-L000184](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L184) | 184 | `"- مسار بحث للأسئلة التي تتطلب معلومات حديثة أو مصادر."` | — |
| [SRC-E73001D9AC-L000185](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L185) | 185 | `"- مسار متعدد الخطوات للمهام المعقدة فقط."` | — |
| [SRC-E73001D9AC-L000186](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L186) | 186 | `"- مخطط بيانات صارم لخطة النموذج، مع التحقق من كل حقل قبل التنفيذ."` | — |
| [SRC-E73001D9AC-L000187](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L187) | 187 | `"- الخطة التي يصدرها النموذج اقتراح غير موثوق، وليست إذنًا لتنفيذ عملية."` | — |
| [SRC-E73001D9AC-L000188](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L188) | 188 | `"- لا يُسمح للخطة بزيادة الميزانية أو تجاوز الصلاحيات أو تعديل سياسات الأمان."` | — |
| [SRC-E73001D9AC-L000189](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L189) | 189 | `"- الحد من إعادة التخطيط وعدد الخطوات وتكرار الأدوات."` | — |
| [SRC-E73001D9AC-L000190](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L190) | 190 | `"- عند عدم الحاجة إلى بحث جديد، يُعاد استخدام سياق صالح ومحدد العمر بدل إعادة كل العمليات."` | — |
| [SRC-E73001D9AC-L000191](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L191) | 191 | `""` | — |
| [SRC-E73001D9AC-L000192](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L192) | 192 | `"تظل مخرجات التخطيط التي ينتجها النموذج **اقتراحات غير موثوقة**. عند الحاجة إلى تمثيل منظم للمهمة، تستخدم TaskSpec بمدخلات ومخرجات وقيود ومعايير قبول وقدرات مطلوبة؛ لا تمنح المواصفة صلاحيات. تُتحقق الخطة حتميًا قبل التنفيذ، وتُرفض الخطوات غير المعروفة أو المتجاوزة للحدود. الخطط المتكررة والحساسة تُفضّل لها مسارات Workflow محددة يمكن اختبارها، مع إبقاء المسار المباشر للأسئلة البسيطة."` | — |
| [SRC-E73001D9AC-L000193](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L193) | 193 | `""` | — |
| [SRC-E73001D9AC-L000194](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L194) | 194 | `"### الطبقة 7 — طبقة البحث وجلب الصفحات"` | — |
| [SRC-E73001D9AC-L000195](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L195) | 195 | `"- فصل موصلات البحث عن محرك التخطيط وعن منطق الإجابة."` | — |
| [SRC-E73001D9AC-L000196](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L196) | 196 | `"- تحديد timeout وconcurrency وresponse-size وresult-count لكل موصل."` | — |
| [SRC-E73001D9AC-L000197](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L197) | 197 | `"- عزل فشل موصل واحد؛ لا يمنع بقية المصادر من العمل إذا كان المسار يسمح بذلك."` | — |
| [SRC-E73001D9AC-L000198](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L198) | 198 | `"- تحديد تاريخ النتائج ومصدرها ووقت الاسترجاع والطلب الذي جلبها."` | — |
| [SRC-E73001D9AC-L000199](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L199) | 199 | `"- جلب المحتوى العام المسموح فقط؛ لا تجاوز لتسجيل الدخول أو paywall أو ضوابط الوصول."` | — |
| [SRC-E73001D9AC-L000200](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L200) | 200 | `"- احترام شروط استخدام المصادر وحدود الطلبات المسموحة."` | — |
| [SRC-E73001D9AC-L000201](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L201) | 201 | `"- تخزين النتائج مؤقتًا فقط مع سياسة صلاحية وتحديث وحذف مناسبة."` | — |
| [SRC-E73001D9AC-L000202](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L202) | 202 | `"- عدم افتراض استقلال المصادر لمجرد أن النتائج ظهرت في أكثر من محرك."` | — |
| [SRC-E73001D9AC-L000203](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L203) | 203 | `""` | — |
| [SRC-E73001D9AC-L000204](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L204) | 204 | `"### الطبقة 8 — بوابة الأدوات وسجل قدراتها"` | — |
| [SRC-E73001D9AC-L000205](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L205) | 205 | `"كل أداة مسجلة بوصف قابل للتحقق يشمل:"` | — |
| [SRC-E73001D9AC-L000206](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L206) | 206 | `"- الاسم والإصدار والجهة المالكة."` | — |
| [SRC-E73001D9AC-L000207](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L207) | 207 | `"- المدخلات والمخرجات والمخطط المتوقع."` | — |
| [SRC-E73001D9AC-L000208](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L208) | 208 | `"- الصلاحيات التي تحتاجها."` | — |
| [SRC-E73001D9AC-L000209](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L209) | 209 | `"- مهلة التنفيذ والميزانية والحدود القصوى."` | — |
| [SRC-E73001D9AC-L000210](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L210) | 210 | `"- ما إذا كانت للقراءة فقط أم ذات أثر خارجي."` | — |
| [SRC-E73001D9AC-L000211](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L211) | 211 | `"- طريقة فحص صحتها، وحدود الفحص، ووقت آخر تحقق."` | — |
| [SRC-E73001D9AC-L000212](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L212) | 212 | `"- مخاطرها وطريقة تعطيلها."` | — |
| [SRC-E73001D9AC-L000213](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L213) | 213 | `"- اختبارات النجاح والفشل والسلوك عند انقطاع الاتصال."` | — |
| [SRC-E73001D9AC-L000214](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L214) | 214 | `""` | — |
| [SRC-E73001D9AC-L000215](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L215) | 215 | `"لا تُظهر المنظومة الأداة على أنها جاهزة لمجرد وجود مفتاح إعداد لها. إعداد المفتاح يثبت وجود إعداد فقط، ولا يثبت الوصول أو الصلاحيات أو النجاح الفعلي."` | — |
| [SRC-E73001D9AC-L000216](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L216) | 216 | `""` | — |
| [SRC-E73001D9AC-L000217](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L217) | 217 | `"لا تساوي حالة الأداة المسجلة حالة الأداة المختبرة أو المهيأة أو المتاحة لحظيًا أو الناجحة في الطلب الحالي. يجب أن تعرض التشخيصات الحالة الدقيقة، ولا تمنح قيمة إعداد أو وجود دالة وحدهما دليلًا على نجاح التكامل."` | — |
| [SRC-E73001D9AC-L000218](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L218) | 218 | `""` | — |
| [SRC-E73001D9AC-L000219](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L219) | 219 | `"### الطبقة 9 — تنفيذ الأدوات والعزل"` | — |
| [SRC-E73001D9AC-L000220](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L220) | 220 | `"- رفض تنفيذ الأوامر الحرة التي يقدمها النموذج."` | — |
| [SRC-E73001D9AC-L000221](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L221) | 221 | `"- استخدام واجهات معرفة ومتحقق منها بدل منح النموذج وصولًا عامًا للنظام أو الشبكة أو قاعدة البيانات."` | — |
| [SRC-E73001D9AC-L000222](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L222) | 222 | `"- تطبيق allowlist للوجهات والأوامر حيث ينطبق ذلك."` | — |
| [SRC-E73001D9AC-L000223](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L223) | 223 | `"- الحد من الاتصالات الخارجة، وعدم السماح للأداة بتجاوز القيود عبر إعادة توجيه أو اسم DNS بديل."` | — |
| [SRC-E73001D9AC-L000224](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L224) | 224 | `"- عزل أدوات المعالجة غير الموثوقة عن أسرار الخدمة والملفات الحساسة."` | — |
| [SRC-E73001D9AC-L000225](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L225) | 225 | `"- إذا استُخدم sandbox في مرحلة مستقبلية، يجب اختبار حدوده وموارده ومنافذ الهروب؛ الاسم وحده لا يثبت العزل."` | — |
| [SRC-E73001D9AC-L000226](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L226) | 226 | `"- القراءة فقط هي الوضع الافتراضي."` | — |
| [SRC-E73001D9AC-L000227](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L227) | 227 | `"- أي فعل خارجي مؤثر أو غير قابل للعكس يحتاج إلى تفويض وصلاحيات وتأكيد واضح وفق مستوى المخاطر."` | — |
| [SRC-E73001D9AC-L000228](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L228) | 228 | `"- مفاتيح الخدمات لا تُمرر إلى النموذج أو المحتوى المسترجع."` | — |
| [SRC-E73001D9AC-L000229](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L229) | 229 | `"- نتائج الأدوات بيانات غير موثوقة إلى أن تتحقق سلامتها وبنيتها."` | — |
| [SRC-E73001D9AC-L000230](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L230) | 230 | `""` | — |
| [SRC-E73001D9AC-L000231](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L231) | 231 | `"تُمرّر استدعاءات الأدوات عبر بوابة أو وسيط تنفيذ مركزي يطبق قائمة السماح والتحقق من المدخلات والهوية والحدود والميزانية وسجل النتيجة. الصلاحيات الفعلية لا تستمد من system prompt أو ملف تعريف وحده. يمنع التنفيذ العام للكود المولّد، وتُعزل الموصلات التي تلمس الشبكة أو بيانات خاصة بما يتناسب مع خطرها. لا يلزم أن يكون الوسيط خدمة مستقلة في المرحلة الأولى؛ المطلوب حدّ إنفاذ يمكن اختباره."` | — |
| [SRC-E73001D9AC-L000232](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L232) | 232 | `""` | — |
| [SRC-E73001D9AC-L000233](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L233) | 233 | `"### الطبقة 10 — توحيد الأدلة والمصادر (Evidence Ledger)"` | — |
| [SRC-E73001D9AC-L000234](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L234) | 234 | `"- حفظ الرابط واسم المصدر وتوقيت الوصول والبيانات الوصفية اللازمة للتحقق."` | — |
| [SRC-E73001D9AC-L000235](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L235) | 235 | `"- تمييز الاقتباس أو المعلومة المستخرجة عن استنتاج النموذج."` | — |
| [SRC-E73001D9AC-L000236](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L236) | 236 | `"- ربط الادعاءات المهمة بمصادرها كلما أمكن."` | — |
| [SRC-E73001D9AC-L000237](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L237) | 237 | `"- اكتشاف الاقتباسات غير المدعومة أو المراجع المفقودة."` | — |
| [SRC-E73001D9AC-L000238](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L238) | 238 | `"- عرض فشل الوصول والتعارض بين المصادر وتضارب التواريخ عند تأثيره على النتيجة."` | — |
| [SRC-E73001D9AC-L000239](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L239) | 239 | `"- عدم تقديم مؤشرات اتساع التغطية على أنها احتمال إحصائي لصحة الإجابة."` | — |
| [SRC-E73001D9AC-L000240](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L240) | 240 | `"- عدم الادعاء بأن كل مصدر أصلي أو محدث دون فحص قابل للإثبات."` | — |
| [SRC-E73001D9AC-L000241](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L241) | 241 | `""` | — |
| [SRC-E73001D9AC-L000242](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L242) | 242 | `"### الطبقة 11 — التحقق من الإجابة والنتائج"` | — |
| [SRC-E73001D9AC-L000243](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L243) | 243 | `"- التحقق من شكل البيانات والمخرجات قبل عرضها أو تمريرها إلى أداة أخرى."` | — |
| [SRC-E73001D9AC-L000244](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L244) | 244 | `"- استخدام قواعد حتمية أو استعلامات مباشرة أو مصدر مستقل للتحقق عندما يكون ذلك ممكنًا."` | — |
| [SRC-E73001D9AC-L000245](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L245) | 245 | `"- المراجعة اللغوية من النموذج نفسه قد تحسن الوضوح، لكنها ليست تحققًا مستقلًا من الحقيقة."` | — |
| [SRC-E73001D9AC-L000246](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L246) | 246 | `"- عند تعارض الأدلة، يوضح Omarai التعارض بدل اختيار إجابة بثقة زائفة."` | — |
| [SRC-E73001D9AC-L000247](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L247) | 247 | `"- عند نقص الأدلة، يصرّح بما لم يتمكن من إثباته."` | — |
| [SRC-E73001D9AC-L000248](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L248) | 248 | `"- لا يُعاد البحث أو استخدام نموذج إضافي إلا عندما تكون القيمة المتوقعة أكبر من كلفته ومخاطره."` | — |
| [SRC-E73001D9AC-L000249](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L249) | 249 | `"- العمليات ذات الأثر الخارجي لا تُعتبر ناجحة لمجرد أن النموذج قال إنها نجحت؛ يجب قراءة نتيجة الأداة والتحقق منها."` | — |
| [SRC-E73001D9AC-L000250](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L250) | 250 | `""` | — |
| [SRC-E73001D9AC-L000251](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L251) | 251 | `"### الطبقة 12 — الذاكرة والتخزين المؤقت"` | — |
| [SRC-E73001D9AC-L000252](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L252) | 252 | `"- فصل ذاكرة المحادثة المؤقتة عن بيانات المستخدم الدائمة وعن cache النتائج العامة."` | — |
| [SRC-E73001D9AC-L000253](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L253) | 253 | `"- تضمين tenant/user/session في مفاتيح التخزين المناسبة لمنع التسريب بين المستخدمين."` | — |
| [SRC-E73001D9AC-L000254](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L254) | 254 | `"- عدم وضع أسرار أو بيانات شخصية في cache مشترك بلا داعٍ."` | — |
| [SRC-E73001D9AC-L000255](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L255) | 255 | `"- تحديد TTL وسبب التخزين وشروط الإبطال وتغيّر المصدر."` | — |
| [SRC-E73001D9AC-L000256](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L256) | 256 | `"- لا تُخزن إجابات حساسة في cache عام."` | — |
| [SRC-E73001D9AC-L000257](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L257) | 257 | `"- لا تُستخدم ذاكرة قديمة للإجابة عن سؤال يتطلب وضعًا حديثًا."` | — |
| [SRC-E73001D9AC-L000258](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L258) | 258 | `"- عمليات الكتابة والترحيل لها مخطط واضح، وأقفال أو معاملات عند الحاجة، وخطة استعادة."` | — |
| [SRC-E73001D9AC-L000259](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L259) | 259 | `"- الالتزام بمبدأ تقليل البيانات وسياسة احتفاظ وحذف موثقة."` | — |
| [SRC-E73001D9AC-L000260](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L260) | 260 | `"- لا يُفترض أن SQLite أو أي مخزن محلي يناسب جميع مستويات التوسع؛ يُقاس الاستخدام أولًا ويُحدد حد التحول إلى تخزين مناسب عند الحاجة."` | — |
| [SRC-E73001D9AC-L000261](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L261) | 261 | `""` | — |
| [SRC-E73001D9AC-L000262](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L262) | 262 | `"### الطبقة 13 — الطوابير والعمال والمهام الطويلة"` | — |
| [SRC-E73001D9AC-L000263](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L263) | 263 | `"- تُستخدم عندما يكون طول المهمة أو الحمل أو قيود دورة الطلب تبررها؛ ليست شرطًا لكل سؤال."` | — |
| [SRC-E73001D9AC-L000264](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L264) | 264 | `"- طوابير محدودة الحجم مع سياسة رفض أو تأخير صريحة؛ لا طوابير غير محدودة."` | — |
| [SRC-E73001D9AC-L000265](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L265) | 265 | `"- حدود تزامن مستقلة للمزودات البطيئة أو المكلفة."` | — |
| [SRC-E73001D9AC-L000266](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L266) | 266 | `"- مفاتيح idempotency أو سجل حالة للعمليات التي لا يجوز تكرار آثارها."` | — |
| [SRC-E73001D9AC-L000267](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L267) | 267 | `"- فصل حالة المهمة عن اتصال المستخدم، بحيث لا يؤدي قطع المتصفح وحده إلى فساد الحالة."` | — |
| [SRC-E73001D9AC-L000268](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L268) | 268 | `"- استرداد المهام بعد إعادة تشغيل العامل، مع تجنب تنفيذ الأثر الخارجي مرتين."` | — |
| [SRC-E73001D9AC-L000269](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L269) | 269 | `"- تحديد مدة صلاحية الرسائل وعدد محاولات المعالجة والرسائل الميتة (dead-letter) عند استخدام وسيط يدعمها."` | — |
| [SRC-E73001D9AC-L000270](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L270) | 270 | `"- حماية نظام الطوابير نفسه بالمصادقة والحدود ومراقبة التراكم."` | — |
| [SRC-E73001D9AC-L000271](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L271) | 271 | `""` | — |
| [SRC-E73001D9AC-L000272](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L272) | 272 | `"### الطبقة 14 — المراقبة والتدقيق والاستجابة للحوادث"` | — |
| [SRC-E73001D9AC-L000273](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L273) | 273 | `"- قياس latency وthroughput وerror rate وtimeouts وqueue depth وprovider failures وresource use."` | — |
| [SRC-E73001D9AC-L000274](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L274) | 274 | `"- استخدام سجلات منظمة ومعرفات ارتباط عبر مراحل الطلب."` | — |
| [SRC-E73001D9AC-L000275](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L275) | 275 | `"- عدم تسجيل مفاتيح API أو رموز جلسات أو نصوص مستخدم حساسة افتراضيًا."` | — |
| [SRC-E73001D9AC-L000276](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L276) | 276 | `"- تنقيح السجلات قبل تخزينها؛ وتحديد صلاحية الوصول إليها ومدة احتفاظها."` | — |
| [SRC-E73001D9AC-L000277](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L277) | 277 | `"- فصل readiness عن liveness، وعدم جعل فشل مزود خارجي واحد يعني بالضرورة أن الخادم لا يمكنه تقديم أي استجابة."` | — |
| [SRC-E73001D9AC-L000278](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L278) | 278 | `"- وجود إجراءات استجابة للحوادث: تحديد النطاق، العزل، تدوير الأسرار، الاستعادة، مراجعة السبب الجذري، ومنع تكرار الحادث."` | — |
| [SRC-E73001D9AC-L000279](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L279) | 279 | `"- إجراء اختبارات استعادة النسخ الاحتياطية؛ وجود ملف نسخ احتياطي لا يثبت إمكانية استعادته."` | — |
| [SRC-E73001D9AC-L000280](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L280) | 280 | `"- الإشعارات والتنبيهات يجب أن تميز بين خطأ عابر وتدهور مستمر وحادث أمني."` | — |
| [SRC-E73001D9AC-L000281](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L281) | 281 | `""` | — |
| [SRC-E73001D9AC-L000282](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L282) | 282 | `"### الطبقة 15 — التكوين والأسرار وسلسلة التوريد"` | — |
| [SRC-E73001D9AC-L000283](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L283) | 283 | `"- إدارة البيئة والإعدادات بشكل منفصل عن كود التطبيق."` | — |
| [SRC-E73001D9AC-L000284](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L284) | 284 | `"- عدم حفظ مفاتيح أو رموز أو كلمات مرور في Git، أو السجلات، أو رسائل الخطأ، أو كود الواجهة."` | — |
| [SRC-E73001D9AC-L000285](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L285) | 285 | `"- منع تسريب ملف .env الحقيقي وأسرار الاختبار إلى المستودع العام."` | — |
| [SRC-E73001D9AC-L000286](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L286) | 286 | `"- توفير .env.example بقيم وهمية فقط."` | — |
| [SRC-E73001D9AC-L000287](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L287) | 287 | `"- تدوير الأسرار عند احتمال تسربها، وإلغاء الأسرار غير الضرورية."` | — |
| [SRC-E73001D9AC-L000288](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L288) | 288 | `"- تثبيت الاعتماديات وقيود إصداراتها ضمن سياسة قابلة للصيانة، ومراجعة التنبيهات الأمنية."` | — |
| [SRC-E73001D9AC-L000289](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L289) | 289 | `"- فحص الأسرار والاعتماديات والـ license ومصدر الحزم ضمن CI بقدر ما تسمح الأدوات المتاحة."` | — |
| [SRC-E73001D9AC-L000290](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L290) | 290 | `"- إنشاء SBOM عندما يكون ذلك عمليًا وملائمًا لطبيعة الإصدار."` | — |
| [SRC-E73001D9AC-L000291](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L291) | 291 | `"- قصر صلاحيات رموز CI على الحد اللازم، وحماية فروع الإصدار ومراجعاتها."` | — |
| [SRC-E73001D9AC-L000292](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L292) | 292 | `"- لا يُستخدم dependency أو action جديد لمجرد الحداثة؛ تُراجع موثوقيته وصلاحياته وضرورة إضافته."` | — |
| [SRC-E73001D9AC-L000293](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L293) | 293 | `""` | — |
| [SRC-E73001D9AC-L000294](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L294) | 294 | `"---"` | — |
| [SRC-E73001D9AC-L000295](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L295) | 295 | `""` | — |
| [SRC-E73001D9AC-L000296](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L296) | 296 | `"# الجزء الرابع — الأمن السيبراني ونموذج التهديدات"` | — |
| [SRC-E73001D9AC-L000297](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L297) | 297 | `""` | — |
| [SRC-E73001D9AC-L000298](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L298) | 298 | `"## 6. نموذج التهديد (Threat Model)"` | — |
| [SRC-E73001D9AC-L000299](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L299) | 299 | `""` | — |
| [SRC-E73001D9AC-L000300](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L300) | 300 | `"يجب تحديث نموذج التهديد عند تغيير مسار البيانات أو صلاحيات الأدوات أو واجهات التعرض العامة. يشمل المهاجمين المحتملين: مستخدمًا مسيئًا، وعميلًا آليًا، ومصدر محتوى خبيثًا، وموردًا خارجيًا معطلًا أو مخترقًا، ومستخدمًا يحاول الوصول إلى بيانات غيره، وخطأ إعداد أو اعتماديات معرضة للخطر."` | — |
| [SRC-E73001D9AC-L000301](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L301) | 301 | `""` | — |
| [SRC-E73001D9AC-L000302](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L302) | 302 | `"### 6.1 حماية الطلبات وواجهات API"` | — |
| [SRC-E73001D9AC-L000303](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L303) | 303 | `"- تحقق من الأنواع والأطوال والقيم المسموح بها والحقول غير المتوقعة."` | — |
| [SRC-E73001D9AC-L000304](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L304) | 304 | `"- تحديد حدود واضحة للجسم والعمق وعدد عناصر القوائم والسجل التاريخي."` | — |
| [SRC-E73001D9AC-L000305](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L305) | 305 | `"- استخدام استعلامات parameterized عندما توجد قاعدة SQL."` | — |
| [SRC-E73001D9AC-L000306](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L306) | 306 | `"- ترميز مخرجات العرض حسب السياق ومنع تفسير المحتوى غير الموثوق على أنه HTML أو JavaScript."` | — |
| [SRC-E73001D9AC-L000307](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L307) | 307 | `"- المصادقة والصلاحيات تطبّقان من جانب الخادم."` | — |
| [SRC-E73001D9AC-L000308](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L308) | 308 | `"- ضبط CORS على الأصول المطلوبة فقط، مع عدم اعتبار CORS نظام مصادقة."` | — |
| [SRC-E73001D9AC-L000309](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L309) | 309 | `"- وضع حد للطلبات المكلفة، وليس فقط عدد الطلبات العامة."` | — |
| [SRC-E73001D9AC-L000310](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L310) | 310 | `"- ألا تُكشف stack traces أو الأسرار أو إعدادات التشغيل أو المسارات الداخلية في الاستجابة العامة."` | — |
| [SRC-E73001D9AC-L000311](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L311) | 311 | `""` | — |
| [SRC-E73001D9AC-L000312](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L312) | 312 | `"### 6.2 حماية وكيل البحث من SSRF والوصول إلى الشبكة الداخلية"` | — |
| [SRC-E73001D9AC-L000313](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L313) | 313 | `"لأن Omarai قد يجلب روابط من الإنترنت، تعد هذه المنطقة عالية الخطورة:"` | — |
| [SRC-E73001D9AC-L000314](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L314) | 314 | `"- السماح ببروتوكولات HTTP وHTTPS فقط بحسب الحاجة."` | — |
| [SRC-E73001D9AC-L000315](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L315) | 315 | `"- رفض localhost والشبكات الخاصة والمحجوزة وعناوين link-local وعناوين metadata الحساسة، بما يشمل IPv4 وIPv6 وصيغ العناوين الممثلة أو الملتبسة."` | — |
| [SRC-E73001D9AC-L000316](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L316) | 316 | `"- حل DNS والتحقق من جميع العناوين الناتجة، ثم منع إعادة التوجيه إلى وجهة محظورة."` | — |
| [SRC-E73001D9AC-L000317](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L317) | 317 | `"- إعادة التحقق من كل عنوان وجهة في كل خطوة تحويل؛ لا يُوثق بالعنوان الأول وحده."` | — |
| [SRC-E73001D9AC-L000318](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L318) | 318 | `"- الحماية من DNS rebinding واختلاف نتيجة DNS بين التحقق والاتصال، واستخدام ضوابط شبكة خروج عند توفرها."` | — |
| [SRC-E73001D9AC-L000319](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L319) | 319 | `"- رفض userinfo الملتبس في URL، والمنافذ غير المطلوبة، والصيغ غير القياسية التي قد تتجاوز التحقق."` | — |
| [SRC-E73001D9AC-L000320](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L320) | 320 | `"- وضع سقف لحجم البيانات بعد فك الضغط، وعدد التحويلات، ووقت القراءة، وحجم النص المستخرج."` | — |
| [SRC-E73001D9AC-L000321](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L321) | 321 | `"- التحقق من نوع المحتوى والتعامل الآمن مع HTML وXML والملفات غير المتوقعة."` | — |
| [SRC-E73001D9AC-L000322](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L322) | 322 | `"- عدم السماح لجلب الصفحة بالوصول إلى ملفات محلية أو بروتوكولات داخلية."` | — |
| [SRC-E73001D9AC-L000323](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L323) | 323 | `"- اختبار المتجهات الأمنية باستخدام خادم محلي وهمي واختبارات مضبوطة؛ لا يُنفذ اختبار هجومي ضد طرف خارجي غير مصرح به."` | — |
| [SRC-E73001D9AC-L000324](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L324) | 324 | `""` | — |
| [SRC-E73001D9AC-L000325](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L325) | 325 | `"### 6.3 حماية النماذج والوكلاء من حقن التعليمات"` | — |
| [SRC-E73001D9AC-L000326](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L326) | 326 | `"- تعليم المحتوى الخارجي بوضوح على أنه بيانات غير موثوقة لا أوامر نظام."` | — |
| [SRC-E73001D9AC-L000327](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L327) | 327 | `"- عدم تنفيذ تعليمات مستخرجة من الصفحات أو الوثائق لمجرد أنها تأمر الوكيل بذلك."` | — |
| [SRC-E73001D9AC-L000328](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L328) | 328 | `"- الفصل بين سياسة النظام، وطلب المستخدم، ونتائج الأدوات، والمحتوى المسترجع."` | — |
| [SRC-E73001D9AC-L000329](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L329) | 329 | `"- لا يمتلك النموذج مباشرة مفاتيح أو صلاحيات؛ تمر طلباته عبر طبقة سياسة وتنفيذ حتمية."` | — |
| [SRC-E73001D9AC-L000330](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L330) | 330 | `"- التحقق من arguments لكل tool call مقابل schema وallowlist وحدود الموارد."` | — |
| [SRC-E73001D9AC-L000331](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L331) | 331 | `"- منع استدعاء أدوات غير مسجلة، أو تعديل الصلاحيات والميزانيات من مخرجات النموذج."` | — |
| [SRC-E73001D9AC-L000332](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L332) | 332 | `"- استخدام اختبارات red-team لحالات prompt injection المباشرة وغير المباشرة، وتسريب الأسرار، ورفض السياسات، وتسميم السياق."` | — |
| [SRC-E73001D9AC-L000333](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L333) | 333 | `"- عدم افتراض أن تعليمات النظام وحدها تمنع الهجمات؛ يجب فرض الضوابط عند حدود التنفيذ."` | — |
| [SRC-E73001D9AC-L000334](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L334) | 334 | `""` | — |
| [SRC-E73001D9AC-L000335](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L335) | 335 | `"### 6.4 حماية البيانات والخصوصية"` | — |
| [SRC-E73001D9AC-L000336](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L336) | 336 | `"- تصنيف البيانات إلى عامة، تشغيلية، شخصية، سرية، وأسرار اعتماد."` | — |
| [SRC-E73001D9AC-L000337](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L337) | 337 | `"- عدم إرسال كلمات المرور أو المفاتيح أو بيانات خاصة إلى مزود نموذج خارجي."` | — |
| [SRC-E73001D9AC-L000338](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L338) | 338 | `"- توضيح أن الأسئلة والسياق والمقتطفات قد تغادر الخادم إلى مزود النموذج وفق الإعداد الفعلي."` | — |
| [SRC-E73001D9AC-L000339](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L339) | 339 | `"- توثيق مزود كل مرحلة: تخطيط، إجابة، مراجعة؛ وما البيانات المرسلة وحدود الاحتفاظ المعروفة."` | — |
| [SRC-E73001D9AC-L000340](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L340) | 340 | `"- إتاحة تقليل التاريخ المرسل أو تعطيله عند ملاءمة ذلك."` | — |
| [SRC-E73001D9AC-L000341](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L341) | 341 | `"- تحديد فترة احتفاظ وحذف لكل مخزن."` | — |
| [SRC-E73001D9AC-L000342](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L342) | 342 | `"- لا يُدّعى أن خدمة مجانية خارجية خاصة أو مناسبة للبيانات الحساسة دون مراجعة شروطها وسياساتها وإعداداتها."` | — |
| [SRC-E73001D9AC-L000343](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L343) | 343 | `"- إخفاء البيانات الشخصية من السجلات والتحليلات افتراضيًا."` | — |
| [SRC-E73001D9AC-L000344](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L344) | 344 | `""` | — |
| [SRC-E73001D9AC-L000345](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L345) | 345 | `"### 6.5 الصلاحيات والإجراءات ذات الأثر"` | — |
| [SRC-E73001D9AC-L000346](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L346) | 346 | `"- لا يسمح النموذج بتوسيع الصلاحيات بنفسه."` | — |
| [SRC-E73001D9AC-L000347](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L347) | 347 | `"- تصنف الأدوات حسب المخاطر: قراءة عامة، قراءة خاصة، تعديل بيانات، فعل خارجي، فعل حساس أو غير قابل للعكس."` | — |
| [SRC-E73001D9AC-L000348](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L348) | 348 | `"- تتطلب الإجراءات الأشد خطورة تأكيدًا بشريًا واضحًا، ومعاينة لما سيحدث، وإمكانية مراجعة السجل."` | — |
| [SRC-E73001D9AC-L000349](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L349) | 349 | `"- استخدام idempotency والتحقق من الحالة الحالية قبل إعادة المحاولة."` | — |
| [SRC-E73001D9AC-L000350](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L350) | 350 | `"- تطبيق فصل المهام أو موافقة إضافية عندما تستدعي المخاطر ذلك."` | — |
| [SRC-E73001D9AC-L000351](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L351) | 351 | `"- توفير kill switch لتعطيل أداة أو موصل على نحو محدد دون إيقاف التطبيق كله متى أمكن."` | — |
| [SRC-E73001D9AC-L000352](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L352) | 352 | `""` | — |
| [SRC-E73001D9AC-L000353](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L353) | 353 | `"### 6.6 التوافر ومقاومة استنزاف الموارد"` | — |
| [SRC-E73001D9AC-L000354](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L354) | 354 | `"- تحديد الوقت الأقصى لكل طلب ولكل موصل ولكل نموذج."` | — |
| [SRC-E73001D9AC-L000355](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L355) | 355 | `"- تحديد عدد النتائج والصفحات وحجم النص وعدد استدعاءات النماذج والتخطيط."` | — |
| [SRC-E73001D9AC-L000356](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L356) | 356 | `"- حدود تزامن ودوائر قاطع circuit breakers وbackpressure."` | — |
| [SRC-E73001D9AC-L000357](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L357) | 357 | `"- عدم إجراء retries غير محدودة؛ تستخدم محاولات قليلة مع exponential backoff وjitter عند ملاءمتها، وألا يعاد ما لا يصح تكراره."` | — |
| [SRC-E73001D9AC-L000358](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L358) | 358 | `"- فصل ميزانية الطلب عن ميزانية موفر بعينه حتى لا يستنزف موفر بطيء جميع موارد النظام."` | — |
| [SRC-E73001D9AC-L000359](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L359) | 359 | `"- في حال الضغط، رفض العمل الإضافي أو خفض جودة اختيارية بشكل معلن بدل انهيار كل الطلبات."` | — |
| [SRC-E73001D9AC-L000360](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L360) | 360 | `"- حماية تكاليف APIs المدفوعة بحدود صريحة وقواطع إنفاق إذا كانت المنصة تدعم ذلك."` | — |
| [SRC-E73001D9AC-L000361](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L361) | 361 | `""` | — |
| [SRC-E73001D9AC-L000362](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L362) | 362 | `"### 6.7 الاستجابة الأمنية"` | — |
| [SRC-E73001D9AC-L000363](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L363) | 363 | `"- عند اكتشاف تسرب سر: إلغاؤه/تدويره أولًا، ثم تحديد النطاق والتنظيف."` | — |
| [SRC-E73001D9AC-L000364](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L364) | 364 | `"- عند ثغرة حرجة: تقييم مدى التعرض، وتعطيل المسار المتأثر مؤقتًا عند الحاجة، وإصلاحه واختباره قبل إعادة تفعيله."` | — |
| [SRC-E73001D9AC-L000365](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L365) | 365 | `"- إعداد سجل زمني للحادث يتضمن الأثر والإجراء والاختبار اللاحق، دون نشر تفاصيل تستغل قبل الإصلاح."` | — |
| [SRC-E73001D9AC-L000366](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L366) | 366 | `"- تجنب ادعاء “غير قابل للاختراق”. الهدف خفض المخاطر، واحتواء الضرر، وسرعة الكشف والتعافي، والتحسين المستمر."` | — |
| [SRC-E73001D9AC-L000367](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L367) | 367 | `""` | — |
| [SRC-E73001D9AC-L000368](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L368) | 368 | `"---"` | — |
| [SRC-E73001D9AC-L000369](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L369) | 369 | `""` | — |
| [SRC-E73001D9AC-L000370](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L370) | 370 | `"### 6.8 ضمانات الأمن السيبراني الحاكمة للمهارات وسير العمل والوكلاء"` | — |
| [SRC-E73001D9AC-L000371](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L371) | 371 | `""` | — |
| [SRC-E73001D9AC-L000372](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L372) | 372 | `"تُقرأ ضوابط هذا القسم مع [المعمارية الحاكمة للقدرات والمهارات وسير العمل والوكلاء](OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md)، ولا تحل محل أي ضابط عام في هذا الدستور."` | — |
| [SRC-E73001D9AC-L000373](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L373) | 373 | `""` | — |
| [SRC-E73001D9AC-L000374](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L374) | 374 | `"- **الهدف الأمني:** أعلى مستوى عملي قابل للإثبات ضمن نموذج التهديد والبيئة المتاحة، دون الادعاء بأن النظام آمن 100% أو غير قابل للاختراق. يجب أن تكون المخاطر المتبقية والضوابط غير المتاحة معلومة؛ وإذا تعذر توفير حاجز أمني لازم، تُقلّص القدرة أو تُعطّل بدل نشرها على افتراض الأمان."` | — |
| [SRC-E73001D9AC-L000375](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L375) | 375 | `"- **Zero Trust وأقل صلاحية:** لا تُمنح الثقة بسبب موقع المكوّن أو ملكيته. تُفحص هوية الطلب وصلاحية المستخدم والعملية والمورد عند كل حد مناسب، وتطبق سياسة المنع الافتراضي. لا يملك LLM أو Skill أو Workflow أو Agent Profile صلاحية منح نفسه إذنًا."` | — |
| [SRC-E73001D9AC-L000376](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L376) | 376 | `"- **Tool Broker قابل للاختبار:** كل استدعاء أداة يمر عبر وسيط يفرض المصادقة والتفويض والتحقق من المخطط والميزانية والمهلة ونطاق البيانات، ويسجل نتيجة التنفيذ المنقحة. لا ينفذ النموذج أوامر shell حرة أو كودًا حرًا."` | — |
| [SRC-E73001D9AC-L000377](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L377) | 377 | `"- **حقن التعليمات:** كل محتوى مستخدم أو ويب أو ملف أو ذاكرة أو مخرجات نموذج بيانات غير موثوقة حتى التحقق. تُفصل البيانات عن سياسة النظام، وتخضع الخطط والاستدعاءات لمخططات وallowlists وحدود، ولا تكفي البرومبتات أو فلاتر الكلمات كحاجز وحيد."` | — |
| [SRC-E73001D9AC-L000378](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L378) | 378 | `"- **الشبكة وSSRF:** يجب فحص عناوين الوجهة وDNS وعناوين IPv4/IPv6 والتحويلات وإعادة التوجيه وحدود الحجم والوقت؛ تمنع الاتصالات إلى loopback والشبكات الخاصة وlink-local وmetadata والمحجوزات، مع اختبار فعلي وفق بيئة التشغيل. لا يُفترض أن الحماية موجودة أو مكتملة دون اختبار."` | — |
| [SRC-E73001D9AC-L000379](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L379) | 379 | `"- **API والواجهة:** تُفرض المصادقة وصلاحيات الكائنات على الخادم، مع ضوابط input validation وrate limiting وCORS وCSRF عندما ينطبق وoutput encoding/XSS والحماية من path traversal وأخطاء لا تكشف أسرارًا. لا تُعرض نقاط الإدارة والتشخيص علنًا بلا حماية."` | — |
| [SRC-E73001D9AC-L000380](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L380) | 380 | `"- **الأسرار والخصوصية:** لا أسرار في Git أو المتصفح أو سجلات الطلب. يُقيَّم تدفق البيانات لكل مزود نموذج وfallback، ولا تُرسل بيانات حساسة إلى مزود غير معتمد. تُنقح السجلات، وتُحدد صلاحياتها وفترات الاحتفاظ والحذف، وتُراجع النسخ الاحتياطية واستعادتها."` | — |
| [SRC-E73001D9AC-L000381](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L381) | 381 | `"- **العزل وحالة المهمة:** سياق مستقل لكل طلب؛ لا ذاكرة أو متغيرات mutable مشتركة بلا عزل مثبت. لا تُفترض حماية تعدد المستخدمين دون اختبارات تداخل وعزل. كل إجراء خارجي حساس يتطلب تفويضًا وتأكيدًا مناسبين، وidempotency عند احتمالية التكرار."` | — |
| [SRC-E73001D9AC-L000382](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L382) | 382 | `"- **سلسلة التوريد وCI/CD:** أقل صلاحيات للرموز والأكشنات، وفحص الاعتماديات والأسرار، وتثبيت إصدارات عند ملاءمة ذلك، ومنع PR غير الموثوق من الوصول إلى أسرار الإنتاج، وربط artifact بالـ commit والاختبارات التي أنتجته."` | — |
| [SRC-E73001D9AC-L000383](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L383) | 383 | `"- **توليد الكود:** لا يُشغّل كود مولد من النموذج في مسار الإنتاج. أي تجربة مستقبلية تحتاج إلى قرار مستقل، وبيئة عزل مختبرة، وشبكة مغلقة افتراضيًا، وملفات وأسرار غير متاحة للعملية، وحدود موارد، واختبارات هروب وتصعيد صلاحيات، ومراجعة بشرية."` | — |
| [SRC-E73001D9AC-L000384](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L384) | 384 | `"- **الكشف والاستجابة:** سجلات منقحة، وحدود إنذار، ووسيلة إيقاف للمسار المتأثر، وإجراء تدوير للأسرار واحتواء الحادث وتحليل السبب الجذري واختبار منع التكرار. حدود الخدمة والتكلفة جزء من الأمن ضد الإساءة والاستنزاف."` | — |
| [SRC-E73001D9AC-L000385](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L385) | 385 | `"- **بوابة القبول الأمني:** لا تُفعّل قدرة جديدة ذات خطر قبل اجتياز الاختبارات الأمنية المرتبطة بها. وجود سياسة أو sandbox أو فحص ثابت لا يثبت وحده فعالية الحماية؛ يلزم دليل على الضبط في بيئة ونطاق معروفين. تُسجّل الحالات غير المختبرة NOT_RUN/UNKNOWN ولا تُعامل كنجاح."` | — |
| [SRC-E73001D9AC-L000386](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L386) | 386 | `""` | — |
| [SRC-E73001D9AC-L000387](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L387) | 387 | `"التفاصيل التفصيلية للأصول وحدود الثقة ونموذج التهديد واختبارات الرفض والعزل وسلسلة التوريد والاستجابة للحوادث موجودة في القسم 17 من وثيقة المعمارية المرتبطة."` | — |
| [SRC-E73001D9AC-L000388](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L388) | 388 | `""` | — |
| [SRC-E73001D9AC-L000389](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L389) | 389 | `"---"` | — |
| [SRC-E73001D9AC-L000390](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L390) | 390 | `""` | — |
| [SRC-E73001D9AC-L000391](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L391) | 391 | `"# الجزء الخامس — الأداء، التزامن، السعة والتوسع"` | — |
