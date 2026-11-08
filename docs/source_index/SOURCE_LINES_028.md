# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **028**
- سجلات الأسطر: **800**
- النطاق: SRC-E73001D9AC-L000172 إلى SRC-D17CE3D12F-L000049
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## وثائق وفهرسة

### FILE-E73001D9AC — [docs/OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
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
| [SRC-E73001D9AC-L000392](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L392) | 392 | `""` | — |
| [SRC-E73001D9AC-L000393](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L393) | 393 | `"## 7. استراتيجية التحمل والسرعة"` | — |
| [SRC-E73001D9AC-L000394](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L394) | 394 | `""` | — |
| [SRC-E73001D9AC-L000395](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L395) | 395 | `"### 7.1 ميزانية لكل طلب"` | — |
| [SRC-E73001D9AC-L000396](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L396) | 396 | `"يتضمن سياق الطلب، بحسب المسار:"` | — |
| [SRC-E73001D9AC-L000397](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L397) | 397 | `"- مهلة إجمالية absolute deadline."` | — |
| [SRC-E73001D9AC-L000398](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L398) | 398 | `"- حدًا لعدد مراحل التخطيط وإعادة التخطيط."` | — |
| [SRC-E73001D9AC-L000399](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L399) | 399 | `"- حدًا لعدد استدعاءات أدوات البحث."` | — |
| [SRC-E73001D9AC-L000400](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L400) | 400 | `"- حدًا لحجم النتائج والصفحات والنص المستخرج."` | — |
| [SRC-E73001D9AC-L000401](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L401) | 401 | `"- حدًا لعدد استدعاءات النموذج وحجم المدخلات والمخرجات."` | — |
| [SRC-E73001D9AC-L000402](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L402) | 402 | `"- حدًا للتزامن لكل موفر خارجي."` | — |
| [SRC-E73001D9AC-L000403](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L403) | 403 | `"- حدًا لاستخدام الذاكرة والمهام الفرعية حيث يمكن فرضه."` | — |
| [SRC-E73001D9AC-L000404](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L404) | 404 | `"- سياسة واضحة للتوقف والإجابة الجزئية عند نفاد الميزانية."` | — |
| [SRC-E73001D9AC-L000405](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L405) | 405 | `""` | — |
| [SRC-E73001D9AC-L000406](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L406) | 406 | `"تُحدد القيم من واقع الاختبارات وإمكانات الاستضافة؛ لا توجد أرقام سحرية تصلح لجميع البيئات."` | — |
| [SRC-E73001D9AC-L000407](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L407) | 407 | `""` | — |
| [SRC-E73001D9AC-L000408](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L408) | 408 | `"### 7.2 تحسين المسارات"` | — |
| [SRC-E73001D9AC-L000409](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L409) | 409 | `"- تصنيف مبكر للسؤال: مباشر، يحتاج بحثًا، متعدد الخطوات، غير مسموح أو غير واضح."` | — |
| [SRC-E73001D9AC-L000410](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L410) | 410 | `"- عدم استدعاء النموذج للتصنيف إن أمكن حسم السؤال بقواعد بسيطة موثوقة."` | — |
| [SRC-E73001D9AC-L000411](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L411) | 411 | `"- عدم البحث في الحالات التي لا تضيف فيها المصادر قيمة."` | — |
| [SRC-E73001D9AC-L000412](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L412) | 412 | `"- البحث المتوازي فقط للمهام المستقلة وبحد تزامن معلوم."` | — |
| [SRC-E73001D9AC-L000413](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L413) | 413 | `"- إيقاف البحث عندما تتحقق تغطية كافية بحسب معايير محددة، لا بعد عدد اعتباطي من الاستدعاءات فقط."` | — |
| [SRC-E73001D9AC-L000414](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L414) | 414 | `"- منع التكرار عبر fingerprint أو مفاتيح cache مناسبة."` | — |
| [SRC-E73001D9AC-L000415](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L415) | 415 | `"- ضغط السياق المرسل إلى النموذج إلى المعلومات اللازمة، مع الحفاظ على المصادر والتحذيرات المهمة."` | — |
| [SRC-E73001D9AC-L000416](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L416) | 416 | `"- قياس فائدة كل تمريرة: التحسن في جودة الإجابة مقابل الوقت والتكلفة؛ وإزالة أي تمريرة لا تقدم فائدة مثبتة."` | — |
| [SRC-E73001D9AC-L000417](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L417) | 417 | `"- فصل زمن الخادم عن زمن المزود الخارجي حتى يُعرف مصدر البطء."` | — |
| [SRC-E73001D9AC-L000418](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L418) | 418 | `""` | — |
| [SRC-E73001D9AC-L000419](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L419) | 419 | `"### 7.3 حماية التنفيذ المتزامن"` | — |
| [SRC-E73001D9AC-L000420](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L420) | 420 | `"- عدم مشاركة كائنات الطلبات mutable بين جلسات المستخدمين."` | — |
| [SRC-E73001D9AC-L000421](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L421) | 421 | `"- تجنب متغيرات global التي تحمل تاريخ مستخدم أو ميزانية طلب."` | — |
| [SRC-E73001D9AC-L000422](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L422) | 422 | `"- فرض حدود concurrency لكل نوع مورد ومزود."` | — |
| [SRC-E73001D9AC-L000423](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L423) | 423 | `"- استخدام أقفال أو معاملات للبيانات التي قد تُعدل بالتوازي."` | — |
| [SRC-E73001D9AC-L000424](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L424) | 424 | `"- كشف تداخل الطلبات في الاختبارات باستخدام معرّفات مستخدمين وبيانات مميزة ومخرجات قابلة للتحقق."` | — |
| [SRC-E73001D9AC-L000425](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L425) | 425 | `"- التحقق من سلوك الإلغاء وانتهاء المهلة وعدم تسرب موارد التنفيذ."` | — |
| [SRC-E73001D9AC-L000426](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L426) | 426 | `""` | — |
| [SRC-E73001D9AC-L000427](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L427) | 427 | `"### 7.4 المرونة عند تعطل الموفرات"` | — |
| [SRC-E73001D9AC-L000428](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L428) | 428 | `"- timeout لكل اتصال."` | — |
| [SRC-E73001D9AC-L000429](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L429) | 429 | `"- circuit breaker مع حالة half-open لاختبار عودة الخدمة."` | — |
| [SRC-E73001D9AC-L000430](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L430) | 430 | `"- retry محدود مع backoff وjitter إذا كانت العملية آمنة للإعادة."` | — |
| [SRC-E73001D9AC-L000431](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L431) | 431 | `"- fallback محدد ومختبر، لا سلسلة مفتوحة من بدائل مجهولة."` | — |
| [SRC-E73001D9AC-L000432](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L432) | 432 | `"- تمييز الفشل الكامل من الانخفاض في مستوى الخدمة."` | — |
| [SRC-E73001D9AC-L000433](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L433) | 433 | `"- المحافظة على إجابة مفيدة مع التحذير عندما يمكن ذلك، وإبلاغ المستخدم عندما لا يتوفر دليل كافٍ."` | — |
| [SRC-E73001D9AC-L000434](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L434) | 434 | `"- عدم وصف fallback بأنه مكافئ في الجودة دون مقارنة."` | — |
| [SRC-E73001D9AC-L000435](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L435) | 435 | `"- لا يجوز أن يؤدي فشل المراجعة الاختيارية إلى محو إجابة صحيحة مكتملة تلقائيًا؛ تعتمد السياسة على المخاطر."` | — |
| [SRC-E73001D9AC-L000436](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L436) | 436 | `""` | — |
| [SRC-E73001D9AC-L000437](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L437) | 437 | `"### 7.5 التوسع"` | — |
| [SRC-E73001D9AC-L000438](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L438) | 438 | `"التدرج الموصى به:"` | — |
| [SRC-E73001D9AC-L000439](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L439) | 439 | `"1. كود منظم وحدود واضحة واختبارات تزامن."` | — |
| [SRC-E73001D9AC-L000440](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L440) | 440 | `"2. ضبط موارد العملية الواحدة والمراقبة."` | — |
| [SRC-E73001D9AC-L000441](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L441) | 441 | `"3. عزل موصلات البطء عن المسارات السريعة."` | — |
| [SRC-E73001D9AC-L000442](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L442) | 442 | `"4. إضافة طوابير وعمال للمهام الطويلة عند الحاجة."` | — |
| [SRC-E73001D9AC-L000443](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L443) | 443 | `"5. نقل البيانات إلى تخزين مناسب عند إثبات حدود المخزن الحالي."` | — |
| [SRC-E73001D9AC-L000444](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L444) | 444 | `"6. إضافة نسخ متعددة للخدمة وتخزين مشترك وموازن تحميل عندما تسمح المنصة والقياسات."` | — |
| [SRC-E73001D9AC-L000445](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L445) | 445 | `"7. اختبارات مناطق فشل ونسخ احتياطي وتعافٍ عندما تصبح متطلبات الخدمة تبررها."` | — |
| [SRC-E73001D9AC-L000446](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L446) | 446 | `""` | — |
| [SRC-E73001D9AC-L000447](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L447) | 447 | `"لا يُفترض أن الاستضافة المجانية تضمن توافرًا عاليًا أو موارد مضمونة أو توسعًا أفقيًا. يجب توثيق حدود الخطة الفعلية والقياسات بدل ادعاء مستوى مؤسسي لا تدعمه الاستضافة."` | — |
| [SRC-E73001D9AC-L000448](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L448) | 448 | `""` | — |
| [SRC-E73001D9AC-L000449](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L449) | 449 | `"## 8. مؤشرات الأداء والاعتمادية"` | — |
| [SRC-E73001D9AC-L000450](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L450) | 450 | `""` | — |
| [SRC-E73001D9AC-L000451](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L451) | 451 | `"يجب جمع هذه المقاييس بحسب المسار والموفر والإصدار، مع تجنب البيانات الحساسة:"` | — |
| [SRC-E73001D9AC-L000452](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L452) | 452 | `""` | — |
| [SRC-E73001D9AC-L000453](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L453) | 453 | `"- زمن الاستجابة p50 وp95 وp99."` | — |
| [SRC-E73001D9AC-L000454](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L454) | 454 | `"- معدل الطلبات الناجحة ومعدل 4xx و5xx والمهلات."` | — |
| [SRC-E73001D9AC-L000455](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L455) | 455 | `"- throughput بوحدة requests/second."` | — |
| [SRC-E73001D9AC-L000456](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L456) | 456 | `"- الطلبات النشطة، والانتظار، وعمق الطابور."` | — |
| [SRC-E73001D9AC-L000457](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L457) | 457 | `"- زمن البحث، وزمن جلب الصفحات، وزمن النموذج، وزمن التحقق."` | — |
| [SRC-E73001D9AC-L000458](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L458) | 458 | `"- عدد استدعاءات المزودات والصفحات والرموز عند إتاحتها."` | — |
| [SRC-E73001D9AC-L000459](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L459) | 459 | `"- معدل استخدام cache ومعدل النتائج المكررة."` | — |
| [SRC-E73001D9AC-L000460](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L460) | 460 | `"- الذاكرة والمعالج وعدد الاتصالات المفتوحة."` | — |
| [SRC-E73001D9AC-L000461](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L461) | 461 | `"- نسبة الطلبات المنفذة ضمن الميزانية."` | — |
| [SRC-E73001D9AC-L000462](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L462) | 462 | `"- نسبة نجاح الأدوات لكل موصل وتوزيع أسباب الفشل."` | — |
| [SRC-E73001D9AC-L000463](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L463) | 463 | `"- تكلفة الخدمة المقدرة لكل طلب عندما تكون هناك تكلفة قابلة للحساب."` | — |
| [SRC-E73001D9AC-L000464](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L464) | 464 | `"- مؤشرات الجودة: الدعم بالمصادر، وتغطية الاستشهادات، وأخطاء الوقائع، والتصريحات غير المدعومة."` | — |
| [SRC-E73001D9AC-L000465](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L465) | 465 | `""` | — |
| [SRC-E73001D9AC-L000466](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L466) | 466 | `"### 8.1 أهداف الخدمة (SLOs)"` | — |
| [SRC-E73001D9AC-L000467](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L467) | 467 | `"- يبدأ العمل بقياس خط الأساس على بيئة موثقة، ثم يعتمد مالك المشروع أهدافًا رقمية واقعية لكل فئة طلب."` | — |
| [SRC-E73001D9AC-L000468](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L468) | 468 | `"- يجب فصل SLO داخل سيطرة التطبيق عن زمن مزود خارجي لا يتحكم فيه التطبيق."` | — |
| [SRC-E73001D9AC-L000469](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L469) | 469 | `"- كل SLO له نافذة قياس وتعريف للنجاح ومصدر بيانات واستثناءات موثقة."` | — |
| [SRC-E73001D9AC-L000470](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L470) | 470 | `"- لا تعلن قدرة استيعاب معينة من المستخدمين إلا بعد اختبارها تحت حمل موثق مع تحديد البيئة وحجم الطلبات ونسبة الأخطاء."` | — |
| [SRC-E73001D9AC-L000471](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L471) | 471 | `"- أي هدف رقمي قبل القياس موسوم PROPOSED، وليس وعدًا للمستخدم."` | — |
| [SRC-E73001D9AC-L000472](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L472) | 472 | `""` | — |
| [SRC-E73001D9AC-L000473](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L473) | 473 | `"---"` | — |
| [SRC-E73001D9AC-L000474](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L474) | 474 | `""` | — |
| [SRC-E73001D9AC-L000475](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L475) | 475 | `"# الجزء السادس — جودة الإجابات والذكاء العملي"` | — |
| [SRC-E73001D9AC-L000476](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L476) | 476 | `""` | — |
| [SRC-E73001D9AC-L000477](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L477) | 477 | `"## 9. عقد الإجابة"` | — |
| [SRC-E73001D9AC-L000478](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L478) | 478 | `""` | — |
| [SRC-E73001D9AC-L000479](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L479) | 479 | `"يجب أن يسعى Omarai إلى:"` | — |
| [SRC-E73001D9AC-L000480](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L480) | 480 | `"1. فهم السؤال وسياقه، مع طلب توضيح فقط عند الضرورة الحقيقية."` | — |
| [SRC-E73001D9AC-L000481](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L481) | 481 | `"2. الإجابة بالعربية الواضحة افتراضيًا وباللغة المطلوبة عند طلبها."` | — |
| [SRC-E73001D9AC-L000482](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L482) | 482 | `"3. استخدام بحث حديث للمعلومات المتغيرة أو الأسئلة التي تحتاج إلى مصادر."` | — |
| [SRC-E73001D9AC-L000483](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L483) | 483 | `"4. تمييز الحقائق من الاستنتاجات والتوصيات والافتراضات."` | — |
| [SRC-E73001D9AC-L000484](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L484) | 484 | `"5. عرض روابط المصدر وسياق زمني مناسب حيثما أمكن."` | — |
| [SRC-E73001D9AC-L000485](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L485) | 485 | `"6. الإفصاح عن قصور التغطية أو تعذر الوصول أو تضارب المصادر."` | — |
| [SRC-E73001D9AC-L000486](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L486) | 486 | `"7. عدم اختلاق مصادر أو نتائج أدوات أو ملفات أو تنفيذات."` | — |
| [SRC-E73001D9AC-L000487](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L487) | 487 | `"8. عدم ادعاء استعمال أداة أو نموذج أو مصدر لم يُستخدم فعليًا."` | — |
| [SRC-E73001D9AC-L000488](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L488) | 488 | `"9. التصريح بعدم المعرفة عندما تكون الأدلة غير كافية."` | — |
| [SRC-E73001D9AC-L000489](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L489) | 489 | `"10. توضيح ما أنجز وما فشل في المهام متعددة الخطوات."` | — |
| [SRC-E73001D9AC-L000490](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L490) | 490 | `"11. صياغة إجابات عملية ومباشرة مع توسع متدرج حسب تعقيد السؤال."` | — |
| [SRC-E73001D9AC-L000491](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L491) | 491 | `"12. احترام حدود الصلاحيات والسياسات حتى لو طلبت التعليمات المسترجعة خلاف ذلك."` | — |
| [SRC-E73001D9AC-L000492](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L492) | 492 | `""` | — |
| [SRC-E73001D9AC-L000493](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L493) | 493 | `"## 10. تحقق الادعاءات وجودة المصادر"` | — |
| [SRC-E73001D9AC-L000494](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L494) | 494 | `"- المصدر الأولي الموثوق يفضّل عندما يناسب السؤال."` | — |
| [SRC-E73001D9AC-L000495](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L495) | 495 | `"- يراعى تاريخ النشر وتاريخ الحدث، خصوصًا في الأخبار والمعلومات المتغيرة."` | — |
| [SRC-E73001D9AC-L000496](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L496) | 496 | `"- أكثر من مصدر لا يعني تحققًا مستقلًا إذا كانت المصادر تنقل عن بعضها."` | — |
| [SRC-E73001D9AC-L000497](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L497) | 497 | `"- يراعى تعارض المصالح والمحتوى الآلي أو المكرر والنتائج المفبركة."` | — |
| [SRC-E73001D9AC-L000498](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L498) | 498 | `"- عند تعذر قراءة صفحة، لا يُنسب إليها محتوى لم يُفحص."` | — |
| [SRC-E73001D9AC-L000499](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L499) | 499 | `"- ينبغي أن يمكن تتبع كل ادعاء مهم إلى دليل أو وضعه كاستنتاج أو عدم يقين."` | — |
| [SRC-E73001D9AC-L000500](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L500) | 500 | `"- لا تُعرض درجة ثقة رقمية إلا بعد وجود منهج معاير وقياسات تدعمها؛ خلاف ذلك، يستخدم وصف نوعي واضح."` | — |
| [SRC-E73001D9AC-L000501](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L501) | 501 | `""` | — |
| [SRC-E73001D9AC-L000502](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L502) | 502 | `"## 11. التقييم والتحسين"` | — |
| [SRC-E73001D9AC-L000503](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L503) | 503 | `"- مجموعة اختبارات ثابتة للأسئلة العربية والفصحى والعامية والأخطاء الإملائية."` | — |
| [SRC-E73001D9AC-L000504](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L504) | 504 | `"- مجموعة أسئلة تتطلب بحثًا حديثًا وأخرى لا تحتاج إلى بحث."` | — |
| [SRC-E73001D9AC-L000505](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L505) | 505 | `"- حالات تعارض مصادر ومصادر قديمة وروابط ميتة ومعلومات ناقصة."` | — |
| [SRC-E73001D9AC-L000506](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L506) | 506 | `"- حالات prompt injection ومخرجات أدوات مشوهة وحالات timeout."` | — |
| [SRC-E73001D9AC-L000507](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L507) | 507 | `"- قياس صحة المصادر ودعم الادعاءات وتكامل الإجابة وسلامة الامتناع."` | — |
| [SRC-E73001D9AC-L000508](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L508) | 508 | `"- استخدام مراجعين بشريين للعينات المهمة عندما تسمح الموارد."` | — |
| [SRC-E73001D9AC-L000509](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L509) | 509 | `"- تتبع regression بين الإصدارات؛ التحسن في معيار واحد لا يبرر إهمال التدهور في الأمان أو السرعة."` | — |
| [SRC-E73001D9AC-L000510](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L510) | 510 | `"- عدم اعتبار تقييم نموذج لغوي واحد للحالة تقييمًا نهائيًا مستقلًا."` | — |
| [SRC-E73001D9AC-L000511](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L511) | 511 | `""` | — |
| [SRC-E73001D9AC-L000512](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L512) | 512 | `"---"` | — |
| [SRC-E73001D9AC-L000513](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L513) | 513 | `""` | — |
| [SRC-E73001D9AC-L000514](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L514) | 514 | `"# الجزء السابع — دورة التطوير والإصدارات"` | — |
| [SRC-E73001D9AC-L000515](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L515) | 515 | `""` | — |
| [SRC-E73001D9AC-L000516](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L516) | 516 | `"## 12. قواعد التطوير الآمن"` | — |
| [SRC-E73001D9AC-L000517](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L517) | 517 | `""` | — |
| [SRC-E73001D9AC-L000518](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L518) | 518 | `"- فحص حالة المستودع والفرع وHEAD قبل إجراء تعديل."` | — |
| [SRC-E73001D9AC-L000519](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L519) | 519 | `"- إنشاء فرع مستقل للتغيير، وتجنب الكتابة غير الضرورية إلى main."` | — |
| [SRC-E73001D9AC-L000520](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L520) | 520 | `"- جعل التعديل صغيرًا ومحدود الأثر متى أمكن."` | — |
| [SRC-E73001D9AC-L000521](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L521) | 521 | `"- إضافة اختبار يكشف العيب قبل أو مع إصلاحه."` | — |
| [SRC-E73001D9AC-L000522](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L522) | 522 | `"- تشغيل الفحوص ذات الصلة وتسجيل مخرجاتها الفعلية."` | — |
| [SRC-E73001D9AC-L000523](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L523) | 523 | `"- عدم الادعاء بأن الاختبارات نجحت إذا لم تُنفّذ أو لم تظهر نتيجتها."` | — |
| [SRC-E73001D9AC-L000524](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L524) | 524 | `"- مراجعة diff للتأكد من عدم وجود تغييرات جانبية."` | — |
| [SRC-E73001D9AC-L000525](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L525) | 525 | `"- تحديث التوثيق والأمثلة عندما تتغير الواجهات أو السلوك."` | — |
| [SRC-E73001D9AC-L000526](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L526) | 526 | `"- عدم دمج PR أو النشر النهائي دون تصريح صاحب المشروع."` | — |
| [SRC-E73001D9AC-L000527](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L527) | 527 | `"- حفظ النتائج برقم الالتزام والبيئة وأمر التشغيل."` | — |
| [SRC-E73001D9AC-L000528](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L528) | 528 | `""` | — |
| [SRC-E73001D9AC-L000529](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L529) | 529 | `"## 13. طبقات الاختبار المطلوبة"` | — |
| [SRC-E73001D9AC-L000530](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L530) | 530 | `""` | — |
| [SRC-E73001D9AC-L000531](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L531) | 531 | `"### T0 — فحوص محلية أساسية"` | — |
| [SRC-E73001D9AC-L000532](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L532) | 532 | `"تنسيق، lint، استيراد الوحدات، وفحوص النوع حيث تستخدم."` | — |
| [SRC-E73001D9AC-L000533](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L533) | 533 | `""` | — |
| [SRC-E73001D9AC-L000534](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L534) | 534 | `"### T1 — اختبارات الوحدة"` | — |
| [SRC-E73001D9AC-L000535](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L535) | 535 | `"التحقق من المنطق المحدد وحدود الإدخال والمخرجات والحالات الاستثنائية."` | — |
| [SRC-E73001D9AC-L000536](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L536) | 536 | `""` | — |
| [SRC-E73001D9AC-L000537](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L537) | 537 | `"### T2 — اختبارات العقود والتكامل"` | — |
| [SRC-E73001D9AC-L000538](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L538) | 538 | `"اختبار واجهات API ومخططات الأدوات وعقود موصلات البحث والنماذج."` | — |
| [SRC-E73001D9AC-L000539](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L539) | 539 | `""` | — |
| [SRC-E73001D9AC-L000540](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L540) | 540 | `"### T3 — اختبارات النظام من طرف إلى طرف"` | — |
| [SRC-E73001D9AC-L000541](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L541) | 541 | `"اختبار المسار الكامل للسؤال والبحث وتوليد الإجابة وعرض المصادر؛ باستخدام خدمات وهمية أو موفر اختباري حيث يناسب."` | — |
| [SRC-E73001D9AC-L000542](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L542) | 542 | `""` | — |
| [SRC-E73001D9AC-L000543](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L543) | 543 | `"### T4 — اختبارات التزامن والعزل"` | — |
| [SRC-E73001D9AC-L000544](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L544) | 544 | `"طلبات متزامنة ببيانات مختلفة، وإلغاء وtimeouts وأخطاء متداخلة، مع التأكد من عدم تسرب السياق."` | — |
| [SRC-E73001D9AC-L000545](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L545) | 545 | `""` | — |
| [SRC-E73001D9AC-L000546](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L546) | 546 | `"### T5 — اختبارات الأداء والحمل"` | — |
| [SRC-E73001D9AC-L000547](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L547) | 547 | `"حمل تدريجي، ذروة، زيادة مفاجئة، وتحمل مستمر. توثيق عدد العملاء ومعدل الوصول وزمن الاختبار وبيئة التنفيذ."` | — |
| [SRC-E73001D9AC-L000548](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L548) | 548 | `""` | — |
| [SRC-E73001D9AC-L000549](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L549) | 549 | `"### T6 — اختبارات الفشل والتعافي"` | — |
| [SRC-E73001D9AC-L000550](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L550) | 550 | `"تعطل موفر، تأخره، رد غير صالح، انقطاع شبكة، إعادة تشغيل عامل، نفاد حصة؛ والتحقق من التعافي وسلامة الحالة."` | — |
| [SRC-E73001D9AC-L000551](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L551) | 551 | `""` | — |
| [SRC-E73001D9AC-L000552](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L552) | 552 | `"### T7 — اختبارات الأمن والخصوصية"` | — |
| [SRC-E73001D9AC-L000553](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L553) | 553 | `"صلاحيات، جلسات، SSRF، حقن تعليمات، تسريب الأسرار، إساءة استخدام API، والتحقق من عدم اختلاط بيانات المستخدمين."` | — |
| [SRC-E73001D9AC-L000554](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L554) | 554 | `""` | — |
| [SRC-E73001D9AC-L000555](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L555) | 555 | `"### T8 — تقييم جودة الإجابة"` | — |
| [SRC-E73001D9AC-L000556](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L556) | 556 | `"صحة المصادر والاستشهادات، التغطية، وضوح عدم اليقين، والامتناع عند نقص الأدلة."` | — |
| [SRC-E73001D9AC-L000557](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L557) | 557 | `""` | — |
| [SRC-E73001D9AC-L000558](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L558) | 558 | `"لا يلزم تشغيل كل اختبار مكلف على كل تعديل صغير؛ لكن يجب أن تكون التغييرات ذات المخاطر العالية مرتبطة بمجموعة اختبار إلزامية، مع تشغيل اختبارات شاملة قبل إصدار إنتاجي."` | — |
| [SRC-E73001D9AC-L000559](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L559) | 559 | `""` | — |
| [SRC-E73001D9AC-L000560](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L560) | 560 | `"## 14. بوابات إصدار مقترحة"` | — |
| [SRC-E73001D9AC-L000561](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L561) | 561 | `"قبل وسم إصدار بأنه جاهز للإنتاج:"` | — |
| [SRC-E73001D9AC-L000562](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L562) | 562 | `"- نجاح الاختبارات الإلزامية المسجلة لهذا الإصدار."` | — |
| [SRC-E73001D9AC-L000563](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L563) | 563 | `"- عدم وجود ثغرات حرجة أو عالية غير معالجة دون استثناء مخاطر مكتوب ومقبول من المالك."` | — |
| [SRC-E73001D9AC-L000564](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L564) | 564 | `"- مراجعة الأسرار والاعتماديات وإعدادات النشر."` | — |
| [SRC-E73001D9AC-L000565](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L565) | 565 | `"- اختبارات دخان بعد النشر مع تمييز صحتها الفعلية عن فحص الإعدادات."` | — |
| [SRC-E73001D9AC-L000566](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L566) | 566 | `"- وجود خطة rollback واختبارها عندما يكون أثر النشر كبيرًا."` | — |
| [SRC-E73001D9AC-L000567](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L567) | 567 | `"- توثيق القيود المعروفة وحدود السعة والتحذيرات."` | — |
| [SRC-E73001D9AC-L000568](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L568) | 568 | `"- تفعيل المقاييس والتنبيهات الأساسية قبل استقبال حمل حقيقي."` | — |
| [SRC-E73001D9AC-L000569](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L569) | 569 | `""` | — |
| [SRC-E73001D9AC-L000570](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L570) | 570 | `"---"` | — |
| [SRC-E73001D9AC-L000571](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L571) | 571 | `""` | — |
| [SRC-E73001D9AC-L000572](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L572) | 572 | `"# الجزء الثامن — تشغيل الخدمة والتعافي"` | — |
| [SRC-E73001D9AC-L000573](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L573) | 573 | `""` | — |
| [SRC-E73001D9AC-L000574](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L574) | 574 | `"## 15. الجاهزية والتشخيص"` | — |
| [SRC-E73001D9AC-L000575](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L575) | 575 | ``"- `liveness`: هل العملية نفسها حية ويمكنها مواصلة العمل؟"`` | — |
| [SRC-E73001D9AC-L000576](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L576) | 576 | ``"- `readiness`: هل العملية جاهزة لقبول هذا النوع من الطلبات؟"`` | — |
| [SRC-E73001D9AC-L000577](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L577) | 577 | `"- حالة الموصل: إعداد موجود، اتصال فعلي ناجح، أو غير متاح."` | — |
| [SRC-E73001D9AC-L000578](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L578) | 578 | `"- حالة النموذج: إعداد، نجاح طلب تشخيص حي، أو فشل/عدم فحص."` | — |
| [SRC-E73001D9AC-L000579](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L579) | 579 | `"- يجب ألا تخلط نقطة health بين “المفتاح موجود” و“الخدمة تعمل الآن”."` | — |
| [SRC-E73001D9AC-L000580](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L580) | 580 | `"- يُذكر نطاق التحقق ووقت إجرائه والموصلات التي شملها."` | — |
| [SRC-E73001D9AC-L000581](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L581) | 581 | `"- endpoint التشخيص الذي ينفذ اتصالات خارجية يُحمى ويُحد معدل استدعائه."` | — |
| [SRC-E73001D9AC-L000582](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L582) | 582 | `""` | — |
| [SRC-E73001D9AC-L000583](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L583) | 583 | `"## 16. النسخ الاحتياطي والاستعادة"` | — |
| [SRC-E73001D9AC-L000584](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L584) | 584 | `"- تحديد البيانات التي تحتاج نسخًا احتياطيًا والبيانات التي لا ينبغي الاحتفاظ بها."` | — |
| [SRC-E73001D9AC-L000585](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L585) | 585 | `"- تحديد تواتر النسخ ومكانها وصلاحية الوصول إليها."` | — |
| [SRC-E73001D9AC-L000586](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L586) | 586 | `"- تشفير النسخ الحساسة إذا كانت خارج بيئة موثوقة."` | — |
| [SRC-E73001D9AC-L000587](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L587) | 587 | `"- منع نسخ الأسرار غير الضرورية في ملفات النسخ."` | — |
| [SRC-E73001D9AC-L000588](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L588) | 588 | `"- اختبار الاستعادة الفعلية دوريًا في بيئة معزولة."` | — |
| [SRC-E73001D9AC-L000589](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L589) | 589 | `"- تحديد هدف مقبول لفقدان البيانات (RPO) وزمن التعافي (RTO) عندما تتطلب الخدمة ذلك."` | — |
| [SRC-E73001D9AC-L000590](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L590) | 590 | `"- توثيق الخطوات اليدوية التي لا تزال ضرورية في مرحلة الاستضافة الحالية."` | — |
| [SRC-E73001D9AC-L000591](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L591) | 591 | `""` | — |
| [SRC-E73001D9AC-L000592](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L592) | 592 | `"## 17. خطة التدهور الآمن"` | — |
| [SRC-E73001D9AC-L000593](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L593) | 593 | `"عند الضغط أو تعطل خدمة خارجية، يجوز تقليل ميزات اختيارية بترتيب محدد، مثل:"` | — |
| [SRC-E73001D9AC-L000594](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L594) | 594 | `"1. إلغاء المراجعة الإضافية غير الضرورية."` | — |
| [SRC-E73001D9AC-L000595](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L595) | 595 | `"2. تقليل عدد استعلامات البحث ضمن حد يحافظ على الحد الأدنى للجودة."` | — |
| [SRC-E73001D9AC-L000596](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L596) | 596 | `"3. إيقاف موصل متدهور مؤقتًا بدائرة قاطع."` | — |
| [SRC-E73001D9AC-L000597](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L597) | 597 | `"4. إعادة إجابة جزئية موثقة بالحدود عند ملاءمتها."` | — |
| [SRC-E73001D9AC-L000598](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L598) | 598 | `"5. رفض الطلبات الجديدة المكلفة مؤقتًا مع رسالة صريحة."` | — |
| [SRC-E73001D9AC-L000599](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L599) | 599 | `""` | — |
| [SRC-E73001D9AC-L000600](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L600) | 600 | `"ولا يجوز بسبب الضغط تعطيل المصادقة أو حدود الصلاحيات أو التحقق من SSRF أو عزل بيانات المستخدمين."` | — |
| [SRC-E73001D9AC-L000601](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L601) | 601 | `""` | — |
| [SRC-E73001D9AC-L000602](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L602) | 602 | `"---"` | — |
| [SRC-E73001D9AC-L000603](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L603) | 603 | `""` | — |
| [SRC-E73001D9AC-L000604](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L604) | 604 | `"# الجزء التاسع — خارطة التنفيذ والاعتماد"` | — |
| [SRC-E73001D9AC-L000605](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L605) | 605 | `""` | — |
| [SRC-E73001D9AC-L000606](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L606) | 606 | `"## 18. ترتيب التنفيذ بحسب المخاطر والاعتماديات"` | — |
| [SRC-E73001D9AC-L000607](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L607) | 607 | `""` | — |
| [SRC-E73001D9AC-L000608](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L608) | 608 | `"**المرحلة A — جرد مثبت للحالة الحالية**"` | — |
| [SRC-E73001D9AC-L000609](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L609) | 609 | `"- تسجيل HEAD والفرع وبيئة التشغيل واعتماديات المشروع."` | — |
| [SRC-E73001D9AC-L000610](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L610) | 610 | `"- رسم دورة الطلب الحقيقية من API حتى البحث والنموذج والإجابة."` | — |
| [SRC-E73001D9AC-L000611](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L611) | 611 | `"- فهرسة نقاط الاتصال الخارجية والأدوات والبيانات الحساسة."` | — |
| [SRC-E73001D9AC-L000612](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L612) | 612 | `"- قراءة الاختبارات وتشغيلها وتسجيل النتائج؛ لا افتراض نجاحها."` | — |
| [SRC-E73001D9AC-L000613](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L613) | 613 | `"- تقرير فجوات يوسم كل نتيجة VERIFIED أو INFERRED أو PROPOSED أو UNKNOWN."` | — |
| [SRC-E73001D9AC-L000614](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L614) | 614 | `""` | — |
| [SRC-E73001D9AC-L000615](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L615) | 615 | `"**المرحلة B — حماية الأساس**"` | — |
| [SRC-E73001D9AC-L000616](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L616) | 616 | `"- عزل سياق الطلبات والذاكرة."` | — |
| [SRC-E73001D9AC-L000617](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L617) | 617 | `"- حدود الإدخال والوقت والعدد والحجم والتزامن."` | — |
| [SRC-E73001D9AC-L000618](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L618) | 618 | `"- تحقق من صلاحيات الواجهات والعمليات الحساسة."` | — |
| [SRC-E73001D9AC-L000619](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L619) | 619 | `"- مراجعة SSRF والتحويلات وDNS وأحجام الاستجابات."` | — |
| [SRC-E73001D9AC-L000620](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L620) | 620 | `"- حماية الأسرار والسجلات وواجهات التشخيص."` | — |
| [SRC-E73001D9AC-L000621](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L621) | 621 | `"- اختبارات regression لكل عيب يُصلح."` | — |
| [SRC-E73001D9AC-L000622](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L622) | 622 | `""` | — |
| [SRC-E73001D9AC-L000623](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L623) | 623 | `"**المرحلة C — مقاومة التعطل**"` | — |
| [SRC-E73001D9AC-L000624](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L624) | 624 | `"- timeouts وcancellation وretry محدود وcircuit breaker."` | — |
| [SRC-E73001D9AC-L000625](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L625) | 625 | `"- حدود التزامن والضغط والطوابير عند الحاجة."` | — |
| [SRC-E73001D9AC-L000626](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L626) | 626 | `"- سلوك واضح للموفر المتعطل."` | — |
| [SRC-E73001D9AC-L000627](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L627) | 627 | `"- اختبارات failure injection وإعادة التشغيل."` | — |
| [SRC-E73001D9AC-L000628](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L628) | 628 | `""` | — |
| [SRC-E73001D9AC-L000629](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L629) | 629 | `"**المرحلة D — القياس والأداء**"` | — |
| [SRC-E73001D9AC-L000630](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L630) | 630 | `"- إنشاء خط أساس لزمن الاستجابة والموارد وجودة النتائج."` | — |
| [SRC-E73001D9AC-L000631](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L631) | 631 | `"- إزالة التكرار وتحسين الاستعلامات والمسارات."` | — |
| [SRC-E73001D9AC-L000632](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L632) | 632 | `"- اختبارات التزامن والحمل تحت البيئة المتاحة."` | — |
| [SRC-E73001D9AC-L000633](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L633) | 633 | `"- اعتماد حدود سعة واقعية موثقة."` | — |
| [SRC-E73001D9AC-L000634](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L634) | 634 | `""` | — |
| [SRC-E73001D9AC-L000635](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L635) | 635 | `"**المرحلة E — صلابة المعرفة**"` | — |
| [SRC-E73001D9AC-L000636](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L636) | 636 | `"- قياس إسناد الادعاءات للمصادر."` | — |
| [SRC-E73001D9AC-L000637](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L637) | 637 | `"- اختبارات التواريخ والتعارض والروابط الميتة وحقن التعليمات."` | — |
| [SRC-E73001D9AC-L000638](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L638) | 638 | `"- سياسة واضحة لعدم اليقين والإجابات الجزئية."` | — |
| [SRC-E73001D9AC-L000639](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L639) | 639 | `"- مجموعة regression عربية ثابتة."` | — |
| [SRC-E73001D9AC-L000640](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L640) | 640 | `""` | — |
| [SRC-E73001D9AC-L000641](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L641) | 641 | `"**المرحلة F — الاستعداد التشغيلي**"` | — |
| [SRC-E73001D9AC-L000642](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L642) | 642 | `"- مراقبة وتنبيهات وسجلات منقحة."` | — |
| [SRC-E73001D9AC-L000643](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L643) | 643 | `"- نسخ احتياطي واستعادة عند الحاجة."` | — |
| [SRC-E73001D9AC-L000644](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L644) | 644 | `"- خطة rollback وحوادث."` | — |
| [SRC-E73001D9AC-L000645](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L645) | 645 | `"- مستند نشر يوضح الأسرار والبيئة والفحوص والقيود."` | — |
| [SRC-E73001D9AC-L000646](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L646) | 646 | `""` | — |
| [SRC-E73001D9AC-L000647](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L647) | 647 | `"**المرحلة G — التوسع**"` | — |
| [SRC-E73001D9AC-L000648](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L648) | 648 | `"- الانتقال من عملية واحدة إلى عمال أو طوابير أو نسخ أفقية فقط عندما تثبت القياسات الحاجة والجدوى."` | — |
| [SRC-E73001D9AC-L000649](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L649) | 649 | `"- ترحيل التخزين عند بلوغ حدود الأداء أو التوافر الموثقة."` | — |
| [SRC-E73001D9AC-L000650](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L650) | 650 | `"- إعادة اختبارات السعة والأمن بعد كل تغير معماري مؤثر."` | — |
| [SRC-E73001D9AC-L000651](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L651) | 651 | `""` | — |
| [SRC-E73001D9AC-L000652](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L652) | 652 | `"كل مرحلة لها معايير دخول وخروج وأدلة، ولا تُعد منجزة بمجرد كتابة خطة لها."` | — |
| [SRC-E73001D9AC-L000653](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L653) | 653 | `""` | — |
| [SRC-E73001D9AC-L000654](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L654) | 654 | `"---"` | — |
| [SRC-E73001D9AC-L000655](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L655) | 655 | `""` | — |
| [SRC-E73001D9AC-L000656](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L656) | 656 | `""` | — |
| [SRC-E73001D9AC-L000657](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L657) | 657 | `"### ترتيب توسيع القدرات والمهارات والوكلاء"` | — |
| [SRC-E73001D9AC-L000658](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L658) | 658 | `""` | — |
| [SRC-E73001D9AC-L000659](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L659) | 659 | `"المراحل A–G أعلاه تغطي الجرد والحماية والاعتمادية والقياس والمعرفة والاستعداد التشغيلي والتوسع. وداخل هذه المراحل، يكون ترتيب بناء قدرات الذكاء الاصطناعي هو: (1) إثبات الحالة والاختبارات، (2) عقود الأدوات وفرض الصلاحيات، (3) المهارات وسير العمل، (4) مواصفات المهام والتركيب المحدود من العناصر المعتمدة، (5) تقييم الحاجة إلى Meta-Agent يولد مسودات فقط، (6) دراسة توليد الكود كقرار مستقبلي اختياري. هذا ترتيب متخصص يكمّل المراحل ولا يلغيها أو يستبدل متطلبات الأمن والتشغيل."` | — |
| [SRC-E73001D9AC-L000660](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L660) | 660 | `""` | — |
| [SRC-E73001D9AC-L000661](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L661) | 661 | `"**بوابة التوسع:** لا ننتقل إلى إنشاء الوكلاء لمجرد انتهاء المرحلة السابقة؛ يلزم دليل على حاجة لا تغطيها المهارات وسير العمل بصورة مناسبة، ومقارنة مفيدة في الجودة والكلفة والصيانة والمخاطر. لا يثبت نجاح الاختبارات التي كتبها النموذج لنفسه أمان التنفيذ، ولا تُفعل قدرة جديدة دون مراجعة مستقلة مناسبة وموافقة بشرية عند اللزوم."` | — |
| [SRC-E73001D9AC-L000662](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L662) | 662 | `""` | — |
| [SRC-E73001D9AC-L000663](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L663) | 663 | `"التفصيل المرجعي وبوابات قبول كل مرحلة وارد في [المعمارية الحاكمة للقدرات والمهارات وسير العمل والوكلاء](OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md)."` | — |
| [SRC-E73001D9AC-L000664](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L664) | 664 | `""` | — |
| [SRC-E73001D9AC-L000665](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L665) | 665 | `"---"` | — |
| [SRC-E73001D9AC-L000666](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L666) | 666 | `""` | — |
| [SRC-E73001D9AC-L000667](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L667) | 667 | `"# الجزء العاشر — معمارية التوسع والتطوير المستمر"` | — |
| [SRC-E73001D9AC-L000668](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L668) | 668 | `""` | — |
| [SRC-E73001D9AC-L000669](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L669) | 669 | `"هذا الجزء متطلب تأسيسي مستقل. الغرض ليس توقع كل ميزة مستقبلية، بل بناء نظام يمكنه استيعاب التغيير بأقل كلفة ومخاطر ممكنة، مع الحفاظ على التوافق والأمان والموثوقية."` | — |
| [SRC-E73001D9AC-L000670](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L670) | 670 | `""` | — |
| [SRC-E73001D9AC-L000671](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L671) | 671 | `"## 19. النتيجة المعمارية المستهدفة"` | — |
| [SRC-E73001D9AC-L000672](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L672) | 672 | `""` | — |
| [SRC-E73001D9AC-L000673](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L673) | 673 | `"يجب أن تسمح معمارية Omarai، وفق الأدلة والموارد المتاحة، بما يلي:"` | — |
| [SRC-E73001D9AC-L000674](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L674) | 674 | `""` | — |
| [SRC-E73001D9AC-L000675](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L675) | 675 | `"- إضافة قدرات وخدمات ووكلاء وأدوات ومصادر بيانات دون إعادة كتابة النواة بالكامل."` | — |
| [SRC-E73001D9AC-L000676](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L676) | 676 | `"- رفع السعة تدريجيًا عبر تحسين المكونات، ثم زيادة الموارد، ثم إضافة عمليات أو نسخ خدمة، ثم فصل مكونات محددة عند ثبوت الحاجة."` | — |
| [SRC-E73001D9AC-L000677](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L677) | 677 | `"- تبديل موفر بحث أو نموذج أو تخزين من خلال واجهات وعقود معرفة، دون انتشار تفاصيل المورد في منطق الأعمال."` | — |
| [SRC-E73001D9AC-L000678](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L678) | 678 | `"- إصدار تغييرات للنواة والواجهة وواجهات API ومخططات البيانات بطريقة قابلة للاختبار والتراجع."` | — |
| [SRC-E73001D9AC-L000679](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L679) | 679 | `"- اختبار كل مكوّن في عزلة نسبية، واختبار الرحلات الكاملة للتأكد من التوافق."` | — |
| [SRC-E73001D9AC-L000680](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L680) | 680 | `"- ترحيل البيانات القديمة والحفاظ على سلامتها، وعدم افتراض إمكانية مسح التخزين وإعادة إنشائه في بيئة الإنتاج."` | — |
| [SRC-E73001D9AC-L000681](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L681) | 681 | `"- الحفاظ على صلاحيات واضحة وحدود ثقة عند إضافة الأدوات أو الوكلاء أو العمال."` | — |
| [SRC-E73001D9AC-L000682](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L682) | 682 | `"- اكتشاف التعقيد المعماري والاعتماديات الدائرية وتراكم الديون التقنية قبل أن تعيق التطوير."` | — |
| [SRC-E73001D9AC-L000683](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L683) | 683 | `""` | — |
| [SRC-E73001D9AC-L000684](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L684) | 684 | `"**مبدأ التصميم:** نخطط لقابلية التوسع والتغيير، ونؤجل التعقيد غير الضروري. قابلية التوسع ليست مرادفًا للخدمات المصغّرة، ولا يتطلب التطوير طويل الأمد تحويل كل وحدة برمجية إلى خدمة مستقلة."` | — |
| [SRC-E73001D9AC-L000685](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L685) | 685 | `""` | — |
| [SRC-E73001D9AC-L000686](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L686) | 686 | `"يُفهم التوسع في القدرات وفق التسلسل الحاكم: أدوات ذات عقود وصلاحيات ← مهارات قابلة لإعادة الاستخدام ← سير عمل قابل للاختبار ← تركيب مهام محدود ← وكلاء عند ثبوت الحاجة. لا يلزم إنشاء وكيل أو خدمة مستقلة لكل اختصاص. انظر [المعمارية الحاكمة للقدرات والمهارات وسير العمل والوكلاء](OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md) للتعاريف وبوابات الانتقال."` | — |
| [SRC-E73001D9AC-L000687](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L687) | 687 | `""` | — |
| [SRC-E73001D9AC-L000688](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L688) | 688 | `"## 20. نمط البداية: Modular Monolith بحدود واضحة"` | — |
| [SRC-E73001D9AC-L000689](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L689) | 689 | `""` | — |
| [SRC-E73001D9AC-L000690](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L690) | 690 | `"**الاختيار الافتراضي المقترح:** تطبيق منظم من نوع Modular Monolith عندما يناسب حجم المشروع وبيئة الاستضافة. يعني ذلك إمكان تشغيل التطبيق كوحدة نشر واحدة، مع فصل الوحدات منطقيًا ومنع تشابك مسؤولياتها."` | — |
| [SRC-E73001D9AC-L000691](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L691) | 691 | `""` | — |
| [SRC-E73001D9AC-L000692](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L692) | 692 | `"يجب أن تكون لكل وحدة:"` | — |
| [SRC-E73001D9AC-L000693](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L693) | 693 | `"- مسؤولية محددة ومحدودات ملكية واضحة."` | — |
| [SRC-E73001D9AC-L000694](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L694) | 694 | `"- واجهة عامة صغيرة ومعلومة؛ وتظل تفاصيل التنفيذ داخل الوحدة."` | — |
| [SRC-E73001D9AC-L000695](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L695) | 695 | `"- مدخلات ومخرجات قابلة للتحقق بعقود محددة."` | — |
| [SRC-E73001D9AC-L000696](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L696) | 696 | `"- اختبارات وحدة وعقود تغطي واجهاتها."` | — |
| [SRC-E73001D9AC-L000697](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L697) | 697 | `"- ملكية واضحة للبيانات التي تنشئها أو تعدلها."` | — |
| [SRC-E73001D9AC-L000698](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L698) | 698 | `"- حدود صلاحيات وموارد مناسبة لطبيعة عملها."` | — |
| [SRC-E73001D9AC-L000699](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L699) | 699 | `"- سجل اعتماديات يمنع إنشاء دورات اعتماد غير مقصودة."` | — |
| [SRC-E73001D9AC-L000700](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L700) | 700 | `""` | — |
| [SRC-E73001D9AC-L000701](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L701) | 701 | `"لا يجوز لوحدة أن تستورد التفاصيل الداخلية لوحدة أخرى أو تعدل مخازنها مباشرة بصورة تتجاوز العقد المتفق عليه. يمكن السماح باستثناءات محددة ومبررة، لكن يجب تسجيلها ومراجعتها."` | — |
| [SRC-E73001D9AC-L000702](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L702) | 702 | `""` | — |
| [SRC-E73001D9AC-L000703](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L703) | 703 | `"### متى نفصل الوحدة إلى خدمة مستقلة؟"` | — |
| [SRC-E73001D9AC-L000704](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L704) | 704 | `""` | — |
| [SRC-E73001D9AC-L000705](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L705) | 705 | `"لا يتم التفكيك لمجرد اتباع موضة معمارية. يُدرس فصل الوحدة عندما يتوفر واحد أو أكثر من الأدلة التالية:"` | — |
| [SRC-E73001D9AC-L000706](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L706) | 706 | `"- احتياج توسع مستقل واضح لا يمكن خدمته بكفاءة داخل التطبيق الحالي."` | — |
| [SRC-E73001D9AC-L000707](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L707) | 707 | `"- متطلبات عزل أمني أو صلاحيات أو موارد تختلف جذريًا عن بقية النظام."` | — |
| [SRC-E73001D9AC-L000708](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L708) | 708 | `"- اختلاف موثق في دورة النشر أو التوافر أو قيود التشغيل."` | — |
| [SRC-E73001D9AC-L000709](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L709) | 709 | `"- اختناق مقاس في الأداء أو حدود عملية تمنع التوسع المطلوب."` | — |
| [SRC-E73001D9AC-L000710](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L710) | 710 | `"- حاجة إلى فريق أو نطاق ملكية مستقل مع عقود تشغيلية واضحة."` | — |
| [SRC-E73001D9AC-L000711](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L711) | 711 | `""` | — |
| [SRC-E73001D9AC-L000712](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L712) | 712 | `"قبل الفصل، تُوثق كلفة الشبكات والكمون، وفشل الاتصال، والمصادقة بين الخدمات، والمراقبة، والنشر والتراجع، والتناسق والاتساق، والاختبارات الإضافية. إذا لم تفوق الفائدة هذه التكاليف، تبقى الوحدة داخل التطبيق معزولة منطقيًا."` | — |
| [SRC-E73001D9AC-L000713](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L713) | 713 | `""` | — |
| [SRC-E73001D9AC-L000714](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L714) | 714 | `"## 21. حدود المجال والواجهات (Domain Boundaries, Ports & Adapters)"` | — |
| [SRC-E73001D9AC-L000715](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L715) | 715 | `""` | — |
| [SRC-E73001D9AC-L000716](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L716) | 716 | `"تُحدد المجالات المنطقية بما يلائم الكود الحقيقي، وقد تشمل: واجهات الطلبات، والهوية والصلاحيات، وتنسيق المهام، والتخطيط، والبحث، وجلب الصفحات، وتنفيذ الأدوات، وتجميع الأدلة، والتحقق من الإجابات، والذاكرة والتخزين، والمراقبة."` | — |
| [SRC-E73001D9AC-L000717](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L717) | 717 | `""` | — |
| [SRC-E73001D9AC-L000718](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L718) | 718 | `"هذه قائمة مجالات محتملة وليست إلزامًا بإنشاء وحدة منفصلة لكل اسم. يتم تحديد الحدود بعد فحص تدفق البيانات والاعتماديات الفعلية."` | — |
| [SRC-E73001D9AC-L000719](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L719) | 719 | `""` | — |
| [SRC-E73001D9AC-L000720](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L720) | 720 | `"- تعتمد قواعد الأعمال على واجهات داخلية مستقرة، لا على مكتبة مورد خارجي بشكل مباشر."` | — |
| [SRC-E73001D9AC-L000721](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L721) | 721 | `"- توضع تفاصيل HTTP وSDK الخاص بالمورد وعمليات التحويل داخل Adapter مناسب."` | — |
| [SRC-E73001D9AC-L000722](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L722) | 722 | `"- تعرف العقود سلوك النجاح والفشل والمهلة والإلغاء وحدود الحجم وإعادة المحاولة."` | — |
| [SRC-E73001D9AC-L000723](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L723) | 723 | `"- تعزل صيغة رد موفر معين عن بقية النواة عبر تحويل صريح واختبارات للعقد."` | — |
| [SRC-E73001D9AC-L000724](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L724) | 724 | `"- لا تتسلل بيانات الاعتماد أو أسرار المورد إلى النماذج أو الواجهة أو سجلات المجال."` | — |
| [SRC-E73001D9AC-L000725](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L725) | 725 | `"- تُمنع الدورات بين الوحدات باستخدام اتجاه اعتماد واضح أو واجهات مشتركة صغيرة ومملوكة بوضوح."` | — |
| [SRC-E73001D9AC-L000726](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L726) | 726 | `"- لا تنشأ طبقة تجريد عامة إلا عندما توجد حاجة واقعية أو أكثر من تنفيذ حقيقي أو فائدة واضحة في الاختبار؛ لا نبني إطارات عمل داخلية ضخمة للتوقع فقط."` | — |
| [SRC-E73001D9AC-L000727](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L727) | 727 | `""` | — |
| [SRC-E73001D9AC-L000728](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L728) | 728 | `"## 22. عقود الأدوات والقدرات والمهارات وسير العمل والوكلاء والإضافات"` | — |
| [SRC-E73001D9AC-L000729](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L729) | 729 | `""` | — |
| [SRC-E73001D9AC-L000730](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L730) | 730 | `"أي مكوّن جديد يجب أن يلتزم بعقد تسجيل واضح، لكن لا يُعامل كل نوع مكوّن باعتباره شيئًا واحدًا. يُستخدم التفريق التالي مع [المعمارية الحاكمة للقدرات والمهارات وسير العمل والوكلاء](OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md):"` | — |
| [SRC-E73001D9AC-L000731](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L731) | 731 | `""` | — |
| [SRC-E73001D9AC-L000732](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L732) | 732 | `"- **Tool / الأداة:** عملية أو موصل بمدخلات ومخرجات وأخطاء وحدود معروفة."` | — |
| [SRC-E73001D9AC-L000733](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L733) | 733 | `"- **Capability / القدرة:** إذن محدد النطاق لتنفيذ نوع من الأفعال؛ لا تمنحها رسالة النموذج أو ملف التعريف لنفسه."` | — |
| [SRC-E73001D9AC-L000734](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L734) | 734 | `"- **Skill / المهارة:** وحدة قابلة لإعادة الاستخدام تجمع غرضًا ومدخلات ومخرجات وقدرات معتمدة ومعايير نجاح واختبارات."` | — |
| [SRC-E73001D9AC-L000735](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L735) | 735 | `"- **Workflow / سير العمل:** خطوات وانتقالات وحدود توقف وميزانيات محددة؛ يمكنه استدعاء مهارات وأدوات، لكنه لا يوسع الصلاحيات."` | — |
| [SRC-E73001D9AC-L000736](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L736) | 736 | `"- **Agent Profile / ملف تعريف الوكيل:** وصفة معلنة تحدد الهدف والمهارات والإصدارات والقيود وسياسة الذاكرة؛ ليست كودًا تنفيذيًا حرًا."` | — |
| [SRC-E73001D9AC-L000737](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L737) | 737 | `"- **Agent / الوكيل:** سياق تنفيذ يركب هدفًا ومهارات وأدوات ضمن السياسة؛ لا يُفترض أنه دائم أو مستقل عن ضوابط المنصة."` | — |
| [SRC-E73001D9AC-L000738](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L738) | 738 | `"- **Plugin / الإضافة:** مكون خارجي أو حزمة طرف ثالث، تؤجل إلى حين تبرير الحاجة ومراجعة المصدر وسلسلة التوريد والعزل."` | — |
| [SRC-E73001D9AC-L000739](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L739) | 739 | `""` | — |
| [SRC-E73001D9AC-L000740](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L740) | 740 | `"يتضمن عقد الأداة، بحسب الحاجة:"` | — |
| [SRC-E73001D9AC-L000741](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L741) | 741 | `"- معرفًا ثابتًا واسمًا ووصفًا وإصدارًا ومالكًا."` | — |
| [SRC-E73001D9AC-L000742](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L742) | 742 | `"- مخطط input/output صارمًا وحدودًا للأحجام والأنواع."` | — |
| [SRC-E73001D9AC-L000743](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L743) | 743 | `"- متطلبات الصلاحيات والهوية ونطاق البيانات."` | — |
| [SRC-E73001D9AC-L000744](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L744) | 744 | `"- تصنيف المخاطر: قراءة عامة، قراءة خاصة، كتابة داخلية، أو أثر خارجي حساس."` | — |
| [SRC-E73001D9AC-L000745](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L745) | 745 | `"- timeout وbudget وconcurrency limit وسياسة إلغاء."` | — |
| [SRC-E73001D9AC-L000746](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L746) | 746 | `"- سياسة retries وidempotency إن كان لها أثر متكرر."` | — |
| [SRC-E73001D9AC-L000747](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L747) | 747 | `"- تصنيفًا للأخطاء: خطأ مدخلات، رفض صلاحية، حد موارد، timeout، تعطل موفر، أو فشل داخلي."` | — |
| [SRC-E73001D9AC-L000748](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L748) | 748 | `"- شروط فحص الصحة ومعنى نتيجة الفحص وحدودها الزمنية."` | — |
| [SRC-E73001D9AC-L000749](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L749) | 749 | `"- اختبارات إيجابية وسلبية واختبارات انقطاع/بطء/ردود غير صالحة."` | — |
| [SRC-E73001D9AC-L000750](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L750) | 750 | `"- طريقة تعطيل أو إيقاف الأداة دون إيقاف غيرها متى أمكن."` | — |
| [SRC-E73001D9AC-L000751](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L751) | 751 | `"- سياسة سجلات لا تكشف الأسرار أو بيانات المستخدم غير الضرورية."` | — |
| [SRC-E73001D9AC-L000752](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L752) | 752 | `""` | — |
| [SRC-E73001D9AC-L000753](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L753) | 753 | `"ويجب أن تتضمن عقود المهارات وسير العمل، بالقدر المناسب:"` | — |
| [SRC-E73001D9AC-L000754](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L754) | 754 | `"- المدخلات والمخرجات ومعايير النجاح والفشل."` | — |
| [SRC-E73001D9AC-L000755](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L755) | 755 | `"- الأدوات والمهارات التابعة مع إصداراتها المسموح بها."` | — |
| [SRC-E73001D9AC-L000756](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L756) | 756 | `"- صلاحيات وميزانية وحدود خطوات واضحة."` | — |
| [SRC-E73001D9AC-L000757](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L757) | 757 | `"- اختبارات عربية، واختبارات فشل، واختبارات عدم تجاوز الصلاحيات."` | — |
| [SRC-E73001D9AC-L000758](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L758) | 758 | `"- حالة الاعتماد وسجل تغييرات يمكن تتبعه."` | — |
| [SRC-E73001D9AC-L000759](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L759) | 759 | `""` | — |
| [SRC-E73001D9AC-L000760](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L760) | 760 | `"تُفرض الصلاحيات عند التنفيذ، ولا يثبت التحقق من المخطط أن السلوك آمن أو صحيح. وتظل الإضافات معطلة افتراضيًا حتى اكتمال إعداداتها وفحوصها. لا يملك أي Plugin أو Agent أو Skill حق منح نفسه صلاحيات جديدة، أو تجاوز ميزانية الطلب، أو تعديل سياسات الأمان. لا يسمح بالتنفيذ الديناميكي لكود قادم من المستخدم أو النموذج دون قرار مستقل ومراجعة وعزل واختبارات أمنية ملائمة."` | — |
| [SRC-E73001D9AC-L000761](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L761) | 761 | `""` | — |
| [SRC-E73001D9AC-L000762](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L762) | 762 | `"**الترتيب الافتراضي للتوسع:** أصلح واثبت النواة الحالية أولًا، ثم وحّد عقود الأدوات والصلاحيات، ثم نظّم القدرات المتكررة كمهارات، ثم المسارات متعددة الخطوات كسير عمل. لا يُنشأ مصنع وكلاء أو Meta-Agent إلا عندما تثبت الحاجة والفائدة بالقياس. وعند إنشائه، يقتصر دوره الأولي على مسودات التعريفات؛ ولا يكتب كودًا تنفيذيًا أو يعتمد نفسه أو يفعل تعريفًا دون المرور ببوابات التحقق والموافقة."` | — |
| [SRC-E73001D9AC-L000763](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L763) | 763 | `""` | — |
| [SRC-E73001D9AC-L000764](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L764) | 764 | `"يُحافظ على سلوك الوظائف الحالية أثناء استخراج المهارات أو سير العمل، ويجب توفير اختبارات regression قبل اعتماد التغيير. لا نعيد كتابة المكونات القائمة لمجرد نقلها إلى أسماء معمارية جديدة."` | — |
| [SRC-E73001D9AC-L000765](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L765) | 765 | `" "` | — |
| [SRC-E73001D9AC-L000766](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L766) | 766 | `"## 23. إصدار واجهات API وعقود الرسائل"` | — |
| [SRC-E73001D9AC-L000767](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L767) | 767 | `""` | — |
| [SRC-E73001D9AC-L000768](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L768) | 768 | `"- تُوثق الواجهات العامة بعقود ومخططات قابلة للمراجعة، ويفضل توليد أو اختبار المخططات من مصدر واحد للحقيقة عندما يكون ذلك عمليًا."` | — |
| [SRC-E73001D9AC-L000769](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L769) | 769 | `"- الإضافات المتوافقة، مثل حقول اختيارية جديدة لا تغير المعنى، تُفضّل على تغييرات تكسر العملاء."` | — |
| [SRC-E73001D9AC-L000770](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L770) | 770 | `"- أي تغيير غير متوافق يتطلب إصدارًا أو مسار ترحيل واضحًا وفترة انتقال مناسبة."` | — |
| [SRC-E73001D9AC-L000771](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L771) | 771 | `"- لا يُحذف حقل أو يغير معناه بصمت، ولا تتحول قيمة اختيارية إلى إلزامية دون خطة."` | — |
| [SRC-E73001D9AC-L000772](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L772) | 772 | `"- يستخدم التحقق في جهة الخادم حتى عندما يتحقق العميل من نفس المخطط."` | — |
| [SRC-E73001D9AC-L000773](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L773) | 773 | `"- تُختبر العقود بأمثلة صحيحة وخاطئة وحدود وأحجام قصوى وحالات إصدار قديم."` | — |
| [SRC-E73001D9AC-L000774](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L774) | 774 | `"- عند استخدام أحداث أو رسائل طوابير، تتضمن الرسالة نوع الحدث وإصداره ومعرف تتبع وبيانات لازمة فقط، ولا تتضمن أسرارًا."` | — |
| [SRC-E73001D9AC-L000775](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L775) | 775 | `"- يجب تحمل الرسائل المكررة أو الخارجة عن الترتيب إذا كان وسيط الرسائل أو طبيعة النظام يسمحان بذلك؛ لا يُفترض تنفيذ الرسالة مرة واحدة فقط دون ضمان."` | — |
| [SRC-E73001D9AC-L000776](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L776) | 776 | `"- لا يوعد بالتوافق العكسي إلا ضمن نطاق إصدار وخطة دعم معلومة."` | — |
| [SRC-E73001D9AC-L000777](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L777) | 777 | `""` | — |
| [SRC-E73001D9AC-L000778](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L778) | 778 | `"## 24. تطور مخططات البيانات والترحيلات"` | — |
| [SRC-E73001D9AC-L000779](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L779) | 779 | `""` | — |
| [SRC-E73001D9AC-L000780](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L780) | 780 | `"يجب أن يتعامل التطوير مع البيانات على أنها أصل مستمر، لا مخزن يمكن إعادة بنائه بلا عواقب."` | — |
| [SRC-E73001D9AC-L000781](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L781) | 781 | `""` | — |
| [SRC-E73001D9AC-L000782](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L782) | 782 | `"- كل تغيير بنيوي في البيانات له ترحيل (migration) محدد وقابل للاختبار."` | — |
| [SRC-E73001D9AC-L000783](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L783) | 783 | `"- فحص أثر الترحيل على البيانات القديمة والفهارس والتنافس والقفل وزمن التوقف."` | — |
| [SRC-E73001D9AC-L000784](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L784) | 784 | `"- تفضيل نمط expand–migrate–contract عند الحاجة إلى تغيير متوافق تدريجيًا: إضافة ما يلزم أولًا، ثم نقل البيانات وقراءة/كتابة متوافقة خلال فترة الانتقال، ثم إزالة البنية القديمة بعد إثبات الاستخدام وعدم الحاجة."` | — |
| [SRC-E73001D9AC-L000785](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L785) | 785 | `"- حفظ نسخة احتياطية صالحة قبل التغييرات الخطرة عندما تنطبق الحاجة، مع اختبار استعادة لا مجرد وجود الملف."` | — |
| [SRC-E73001D9AC-L000786](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L786) | 786 | `"- منع ترحيل هدّام لا رجعة فيه دون تحذير صريح وموافقة وخطة استعادة مناسبة."` | — |
| [SRC-E73001D9AC-L000787](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L787) | 787 | `"- تضمين اختبارات للبيانات القديمة والناقصة وغير المتوقعة والتكرارات وفشل المعاملة."` | — |
| [SRC-E73001D9AC-L000788](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L788) | 788 | `"- تعريف ملكية كل جدول أو مساحة بيانات، وسياسات الحذف والاحتفاظ والخصوصية."` | — |
| [SRC-E73001D9AC-L000789](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L789) | 789 | `"- قياس حجم البيانات ومعدل الكتابة ومشكلات القفل قبل اختيار التوسع أو نقل التخزين."` | — |
| [SRC-E73001D9AC-L000790](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L790) | 790 | `"- لا تتحول قاعدة محلية إلى قاعدة موزعة لمجرد توقع نمو غير مقاس؛ يُوثق معيار الانتقال بناءً على الاستخدام الفعلي."` | — |
| [SRC-E73001D9AC-L000791](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L791) | 791 | `""` | — |
| [SRC-E73001D9AC-L000792](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L792) | 792 | `"## 25. حالة الطلب والتوزيع والتوسع الأفقي"` | — |
| [SRC-E73001D9AC-L000793](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L793) | 793 | `""` | — |
| [SRC-E73001D9AC-L000794](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L794) | 794 | `"لتشغيل عدة نسخ من Omarai، ينبغي تجنب افتراض أن ذاكرة عملية واحدة هي مصدر الحالة الوحيد."` | — |
| [SRC-E73001D9AC-L000795](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L795) | 795 | `""` | — |
| [SRC-E73001D9AC-L000796](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L796) | 796 | `"- تصنف الحالة إلى: حالة قصيرة العمر داخل الطلب، وحالة دائمة للمستخدم، وحالة مهام طويلة، وcache قابل لإعادة البناء."` | — |
| [SRC-E73001D9AC-L000797](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L797) | 797 | `"- الحالة داخل الطلب تظل محلية ما دام الطلب داخل العملية؛ أما ما يجب أن يعيش بعد إعادة التشغيل أو ينتقل بين النسخ فيحتاج تخزينًا أو وسيطًا مناسبًا."` | — |
| [SRC-E73001D9AC-L000798](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L798) | 798 | `"- لا تحفظ المحادثة أو صلاحيات المستخدم في متغير عالمي قابل للتغيير مشترك بين الطلبات."` | — |
| [SRC-E73001D9AC-L000799](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L799) | 799 | `"- مفاتيح الحالة وcache تراعي نطاق المستخدم أو المستأجر، ونوع البيانات، وإصدار المخطط، ومدة الصلاحية."` | — |
| [SRC-E73001D9AC-L000800](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L800) | 800 | `"- لا يعتمد توجيه الطلبات على sticky sessions إلا بقرار مبرر مع خطة للتعطل؛ يُفضّل وضوح مكان الحالة وإمكانية استعادتها."` | — |
| [SRC-E73001D9AC-L000801](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L801) | 801 | `"- استخدام idempotency وسجل حالات واضح عند وجود مهام قد يعاد تسليمها."` | — |
| [SRC-E73001D9AC-L000802](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L802) | 802 | `"- يجب أن تتحمل المهام الطويلة إعادة تشغيل العامل وفق سياسة واضحة، وتمنع تكرار الأثر الخارجي أو تكشفه قبل تنفيذه."` | — |
| [SRC-E73001D9AC-L000803](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L803) | 803 | `"- التوسع الأفقي يتطلب فحص اتصالات قاعدة البيانات وحدود الموفرات ومشاركة الملفات ومفاتيح cache والتوقيت وساعات النظام."` | — |
| [SRC-E73001D9AC-L000804](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L804) | 804 | `"- تحديد حدود اتصال لكل نسخة، وحدود إجمالية عند الحاجة حتى لا يؤدي عدد النسخ إلى إغراق قاعدة البيانات أو الموفر الخارجي."` | — |
| [SRC-E73001D9AC-L000805](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L805) | 805 | `"- فصل الصحة المحلية للعملية عن الجاهزية لقبول طلبات جديدة، مع سلوك سليم أثناء الإغلاق واستنزاف الطلبات (graceful shutdown)."` | — |
| [SRC-E73001D9AC-L000806](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L806) | 806 | `""` | — |
| [SRC-E73001D9AC-L000807](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L807) | 807 | `"## 26. اختبارات اللياقة المعمارية (Architecture Fitness Functions)"` | — |
| [SRC-E73001D9AC-L000808](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L808) | 808 | `""` | — |
| [SRC-E73001D9AC-L000809](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L809) | 809 | `"يجب أن تتحول القواعد المعمارية المهمة إلى فحوص تكرارية حيثما أمكن، بدل الاعتماد الكامل على ذاكرة المطور أو المراجعة اليدوية."` | — |
| [SRC-E73001D9AC-L000810](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L810) | 810 | `""` | — |
| [SRC-E73001D9AC-L000811](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L811) | 811 | `"من أمثلة الفحوص الممكنة بعد مراجعة بنية الكود:"` | — |
| [SRC-E73001D9AC-L000812](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L812) | 812 | `"- منع الاعتماديات الدائرية بين المجالات."` | — |
| [SRC-E73001D9AC-L000813](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L813) | 813 | `"- منع استيراد ملفات خاصة من وحدة أخرى خارج واجهتها المعلنة."` | — |
| [SRC-E73001D9AC-L000814](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L814) | 814 | `"- كشف الأسرار في الفروق والملفات المضافة."` | — |
| [SRC-E73001D9AC-L000815](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L815) | 815 | `"- التحقق من أن كل أداة مسجلة لها schema وحدود زمنية وصلاحيات واختبارات ذات صلة."` | — |
| [SRC-E73001D9AC-L000816](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L816) | 816 | `"- التحقق من أن كل Skill وWorkflow لها مدخلات ومخرجات وحدود ونسخة واختبارات، ولا تستدعي قدرات غير معتمدة."` | — |
| [SRC-E73001D9AC-L000817](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L817) | 817 | `"- التحقق من أن الخطط الصادرة عن النماذج تُفحص قبل التنفيذ، ولا تستطيع تغيير الميزانيات أو الصلاحيات."` | — |
| [SRC-E73001D9AC-L000818](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L818) | 818 | `"- منع تنفيذ كود عام من مخرجات النموذج في مسارات التشغيل، ما لم يعتمد قرار مستقل وآلية عزل واختبارات مناسبة."` | — |
| [SRC-E73001D9AC-L000819](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L819) | 819 | `"- التحقق من أن مسودات التعريف لا تدخل الكتالوج النشط دون اعتماد، وأن Meta-Agent لا يملك اعتماد نفسه."` | — |
| [SRC-E73001D9AC-L000820](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L820) | 820 | `"- اختبارات regression تثبت الحفاظ على السلوك القائم عند استخراج وظيفة إلى Skill أو Workflow."` | — |
| [SRC-E73001D9AC-L000821](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L821) | 821 | `"- التأكد من أن نقاط API الحساسة تخضع للمصادقة والصلاحيات المطلوبة."` | — |
| [SRC-E73001D9AC-L000822](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L822) | 822 | `"- اختبارات تزامن تمنع اختلاط سياق المستخدمين."` | — |
| [SRC-E73001D9AC-L000823](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L823) | 823 | `"- اختبارات عقود تمنع انكسار العملاء أو موصلات البحث عند تغيّر الردود."` | — |
| [SRC-E73001D9AC-L000824](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L824) | 824 | `"- اختبارات ترحيل للبيانات من إصدار سابق إلى الإصدار الجديد."` | — |
| [SRC-E73001D9AC-L000825](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L825) | 825 | `"- اختبارات أداء مرجعية للمسارات المهمة مع حدود تنبيه معقولة."` | — |
| [SRC-E73001D9AC-L000826](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L826) | 826 | `"- فحص أن التكوين الافتراضي لا يفتح الإدارة أو التشخيص للعامة بلا حماية."` | — |
| [SRC-E73001D9AC-L000827](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L827) | 827 | `""` | — |
| [SRC-E73001D9AC-L000828](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L828) | 828 | `"لا تُضاف فحوص شكلية لا تحمي خطرًا حقيقيًا، ولا تفشل خطوط البناء لأسباب غير مستقرة أو غير موثقة. لكل فحص مالك وسبب وطريقة تفسير ووسيلة استثناء مؤقت محدودة."` | — |
| [SRC-E73001D9AC-L000829](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L829) | 829 | `""` | — |
| [SRC-E73001D9AC-L000830](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L830) | 830 | `"## 27. إدارة الديون التقنية والتغيير المستمر"` | — |
| [SRC-E73001D9AC-L000831](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L831) | 831 | `""` | — |
| [SRC-E73001D9AC-L000832](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L832) | 832 | `"- الحفاظ على خريطة اعتماديات بسيطة ومحدثة للمكونات الحرجة ومزوديها ومخازنها."` | — |
| [SRC-E73001D9AC-L000833](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L833) | 833 | `"- تسجيل القرارات التي يصعب الرجوع عنها في ADR، مع البدائل والتكلفة والمخاطر وأدلة الاختيار."` | — |
| [SRC-E73001D9AC-L000834](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L834) | 834 | `"- فصل الديون التقنية المعروفة عن العيوب المثبتة والميزات المؤجلة."` | — |
| [SRC-E73001D9AC-L000835](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L835) | 835 | `"- تقييم الدين التقني وفق احتمال فشل، ونطاق أثر، وكلفة لاحقة، وتكرار لمس الوحدة، بدل التعامل معه كقائمة شكلية."` | — |
| [SRC-E73001D9AC-L000836](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L836) | 836 | `"- عدم إجراء refactor واسع أثناء إصلاح عيب أمني عاجل إلا لضرورة موثقة؛ يفصل التغيير ليسهل مراجعته واختباره."` | — |
| [SRC-E73001D9AC-L000837](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L837) | 837 | `"- تحديد سياسة lifecycle للاعتماديات: تحديثات أمنية عاجلة، وتحديثات اعتيادية، واختبارات توافق، والتخلص من المكتبات المهجورة."` | — |
| [SRC-E73001D9AC-L000838](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L838) | 838 | `"- توفير feature flags أو إعدادات إيقاف عندما تخدم تقليل مخاطر الإطلاق، مع خطة لحذف الأعلام المؤقتة بعد انتهاء الحاجة."` | — |
| [SRC-E73001D9AC-L000839](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L839) | 839 | `"- نشر التغييرات الكبيرة تدريجيًا حيث تسمح المنصة، ومراقبة النتائج، ووقف النشر أو التراجع إذا تجاوزت حدود الفشل المعتمدة."` | — |
| [SRC-E73001D9AC-L000840](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L840) | 840 | `"- الحفاظ على changelog مناسب للتغييرات التي تمس المستخدم أو API أو التشغيل."` | — |
| [SRC-E73001D9AC-L000841](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L841) | 841 | `"- عدم السماح بأن يصبح عدد التجريدات أو الخدمات أكبر من قدرة المشروع على اختبارها ومراقبتها وصيانتها."` | — |
| [SRC-E73001D9AC-L000842](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L842) | 842 | `""` | — |
| [SRC-E73001D9AC-L000843](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L843) | 843 | `"## 28. بوابة قبول التوسع والتطوير"` | — |
| [SRC-E73001D9AC-L000844](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L844) | 844 | `""` | — |
| [SRC-E73001D9AC-L000845](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L845) | 845 | `"قبل اعتماد تغيير يضيف مجالًا أو أداة أو وكيلًا أو مخزنًا أو خدمة، يجب الإجابة وتوثيق ما ينطبق:"` | — |
| [SRC-E73001D9AC-L000846](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L846) | 846 | `"1. ما المشكلة الفعلية أو الحاجة المتوقعة التي يعالجها التغيير؟"` | — |
| [SRC-E73001D9AC-L000847](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L847) | 847 | `"2. هل يوجد حل أبسط داخل البنية الحالية؟"` | — |
| [SRC-E73001D9AC-L000848](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L848) | 848 | `"3. ما الواجهة أو العقد الذي يفصل المكون عن بقية النظام؟"` | — |
| [SRC-E73001D9AC-L000849](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L849) | 849 | `"4. كيف سيُختبر النجاح والفشل وانقطاع الاتصال والمدخلات غير الصالحة؟"` | — |
| [SRC-E73001D9AC-L000850](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L850) | 850 | `"5. ما أثر التغيير على صلاحيات المستخدمين وحدود الثقة والخصوصية؟"` | — |
| [SRC-E73001D9AC-L000851](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L851) | 851 | `"6. هل يحتاج إلى بيانات أو أسرار أو موارد جديدة؟"` | — |
| [SRC-E73001D9AC-L000852](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L852) | 852 | `"7. كيف ستُدار الإصدارات والتوافق والترحيلات؟"` | — |
| [SRC-E73001D9AC-L000853](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L853) | 853 | `"8. ما الحد الأقصى للوقت والحجم والتزامن والتكلفة؟"` | — |
| [SRC-E73001D9AC-L000854](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L854) | 854 | `"9. كيف تتم المراقبة والتعطيل والتراجع؟"` | — |
| [SRC-E73001D9AC-L000855](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L855) | 855 | `"10. ما الدليل الذي يسمح بالقول إن التغيير حسّن قابلية التوسع أو التطوير؟"` | — |
| [SRC-E73001D9AC-L000856](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L856) | 856 | `"11. ما الاختبارات الحالية التي تثبت عدم كسر السلوك السابق؟"` | — |
| [SRC-E73001D9AC-L000857](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L857) | 857 | `"12. من يوافق على المخاطر المتبقية؟"` | — |
| [SRC-E73001D9AC-L000858](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L858) | 858 | `""` | — |
| [SRC-E73001D9AC-L000859](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L859) | 859 | `"**معيار القبول:** لا يلزم أن يكون كل تفصيل مثاليًا أو موزعًا على خدمات مستقلة. يلزم أن تكون الحدود مفهومة، والمخاطر المتوقعة معالجة، والتغيير قابلًا للاختبار والصيانة والتراجع بقدر يتناسب مع خطورته."` | — |
| [SRC-E73001D9AC-L000860](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L860) | 860 | `""` | — |
| [SRC-E73001D9AC-L000861](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L861) | 861 | `"---"` | — |
| [SRC-E73001D9AC-L000862](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L862) | 862 | `""` | — |
| [SRC-E73001D9AC-L000863](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L863) | 863 | `"# الجزء الحادي عشر — تعريف “مكتمل” وقرار تغيير المتطلبات"` | — |
| [SRC-E73001D9AC-L000864](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L864) | 864 | `""` | — |
| [SRC-E73001D9AC-L000865](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L865) | 865 | `"## 29. تعريف الإنجاز"` | — |
| [SRC-E73001D9AC-L000866](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L866) | 866 | `"تُعتبر القدرة منجزة فقط عندما تتوافر كل العناصر المنطبقة:"` | — |
| [SRC-E73001D9AC-L000867](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L867) | 867 | `"1. متطلب محدد يمكن فهمه واختباره."` | — |
| [SRC-E73001D9AC-L000868](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L868) | 868 | `"2. تنفيذ واضح ضمن ملفات وإصدار محددين."` | — |
| [SRC-E73001D9AC-L000869](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L869) | 869 | `"3. اختبار نجاح واختبارات فشل وحدود ذات صلة."` | — |
| [SRC-E73001D9AC-L000870](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L870) | 870 | `"4. نتيجة فعلية محفوظة."` | — |
| [SRC-E73001D9AC-L000871](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L871) | 871 | `"5. قياس أداء إذا كان الادعاء متعلقًا بالسرعة أو السعة."` | — |
| [SRC-E73001D9AC-L000872](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L872) | 872 | `"6. دليل أمني إذا كان الادعاء متعلقًا بالأمان أو العزل."` | — |
| [SRC-E73001D9AC-L000873](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L873) | 873 | `"7. توثيق للقيود والبيئة ونطاق التحقق."` | — |
| [SRC-E73001D9AC-L000874](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L874) | 874 | `"8. مراجعة أن القدرة لم تُضعف خصائص قائمة."` | — |
| [SRC-E73001D9AC-L000875](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L875) | 875 | `"9. حالة VERIFIED مرتبطة بالالتزام المحدد، لا بالمشروع كله."` | — |
| [SRC-E73001D9AC-L000876](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L876) | 876 | `""` | — |
| [SRC-E73001D9AC-L000877](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L877) | 877 | `"## 30. سجل القرارات والاستثناءات"` | — |
| [SRC-E73001D9AC-L000878](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L878) | 878 | `""` | — |
| [SRC-E73001D9AC-L000879](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L879) | 879 | `"يُسجل قرار الاتجاه Skill/Workflow-First وAgent-Later وتفصيلاته في [المعمارية الحاكمة للقدرات والمهارات وسير العمل والوكلاء](OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md)، ويظل مقترحًا حتى موافقة المدير البشري. أي تغيير لاحق يوسع الاستقلالية أو يسمح بتوليد الكود أو يغير سقف الصلاحيات يحتاج إلى ADR مستقل يوضح الحاجة والأدلة والبدائل والمخاطر والاختبارات والموافقة المطلوبة."` | — |
| [SRC-E73001D9AC-L000880](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L880) | 880 | `""` | — |
| [SRC-E73001D9AC-L000881](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L881) | 881 | `"يجب تسجيل القرارات المعمارية الكبيرة في ADR موجز يتضمن:"` | — |
| [SRC-E73001D9AC-L000882](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L882) | 882 | `"- المشكلة والسياق."` | — |
| [SRC-E73001D9AC-L000883](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L883) | 883 | `"- البدائل التي دُرست."` | — |
| [SRC-E73001D9AC-L000884](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L884) | 884 | `"- القرار وأسبابه."` | — |
| [SRC-E73001D9AC-L000885](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L885) | 885 | `"- آثار القرار على الأمان والأداء والتكلفة والاستضافة."` | — |
| [SRC-E73001D9AC-L000886](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L886) | 886 | `"- كيفية الاختبار والتراجع."` | — |
| [SRC-E73001D9AC-L000887](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L887) | 887 | `"- المخاطر المفتوحة وصاحب قبولها."` | — |
| [SRC-E73001D9AC-L000888](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L888) | 888 | `"- تاريخ القرار والمراجع/الالتزام المرتبط."` | — |
| [SRC-E73001D9AC-L000889](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L889) | 889 | `""` | — |
| [SRC-E73001D9AC-L000890](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L890) | 890 | `"أي استثناء من MUST يجب أن يكون صريحًا، محدد النطاق والمدة، مع بديل تعويضي وخطة إغلاق وموافقة صاحب المشروع؛ لا يُحوّل إلى استثناء شامل دائم."` | — |
| [SRC-E73001D9AC-L000891](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L891) | 891 | `""` | — |
| [SRC-E73001D9AC-L000892](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L892) | 892 | `"## 31. القاعدة النهائية"` | — |
| [SRC-E73001D9AC-L000893](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L893) | 893 | `""` | — |
| [SRC-E73001D9AC-L000894](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L894) | 894 | `"هذا الدستور يحكم اتجاه التطوير، لكنه لا يجيز تضخيم المعمارية بلا دليل، ولا يسمح بتسويق مزايا غير مختبرة. الأولوية هي بناء نظام **سريع بقدر ما تسمح به الأدلة والموارد، قوي أمام الأعطال، مقيد الصلاحيات، قابل للمراقبة، وصادق في حدود معرفته**."` | — |
| [SRC-E73001D9AC-L000895](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L895) | 895 | `""` | — |
| [SRC-E73001D9AC-L000896](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L896) | 896 | `"---"` | — |
| [SRC-E73001D9AC-L000897](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L897) | 897 | `""` | — |
| [SRC-E73001D9AC-L000898](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L898) | 898 | `"# مراجع معيارية خارجية للمراجعة الدورية"` | — |
| [SRC-E73001D9AC-L000899](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L899) | 899 | `""` | — |
| [SRC-E73001D9AC-L000900](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L900) | 900 | `"هذه المراجع مصادر إرشادية تُستخدم لاختيار الضوابط والاختبارات المناسبة، ولا تعني أن Omarai متوافق معها بمجرد إدراجها في الوثيقة. يجب تثبيت الإصدار المستخدم في كل تقييم أمني:"` | — |
| [SRC-E73001D9AC-L000901](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L901) | 901 | `""` | — |
| [SRC-E73001D9AC-L000902](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L902) | 902 | `"- [NIST Cybersecurity Framework (CSF) 2.0](https://www.nist.gov/cyberframework) — الحوكمة وتحديد المخاطر والحماية والكشف والاستجابة والتعافي."` | — |
| [SRC-E73001D9AC-L000903](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L903) | 903 | `"- [NIST Secure Software Development Framework (SSDF)](https://csrc.nist.gov/projects/ssdf) — ممارسات تطوير البرامج الآمنة وإدارة الثغرات."` | — |
| [SRC-E73001D9AC-L000904](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L904) | 904 | `"- [NIST AI Risk Management Framework (AI RMF)](https://www.nist.gov/itl/ai-risk-management-framework) — مخاطر الذكاء الاصطناعي وخصائص الثقة."` | — |
| [SRC-E73001D9AC-L000905](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L905) | 905 | `"- [OWASP Application Security Verification Standard (ASVS)](https://owasp.org/projects/asvs) — متطلبات قابلة للتحقق لأمن تطبيقات الويب."` | — |
| [SRC-E73001D9AC-L000906](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L906) | 906 | `"- [OWASP GenAI Security Project — LLM Top 10](https://genai.owasp.org/llm-top-10/) — مخاطر تطبيقات النماذج والوكلاء، بما فيها حقن التعليمات وإساءة استخدام الأدوات وتسريب المعلومات."` | — |
| [SRC-E73001D9AC-L000907](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L907) | 907 | `"- [OWASP Artificial Intelligence Security Verification Standard (AISVS)](https://owasp.org/projects/artificial-intelligence-security-verification-standard-aisvs-docs) — متطلبات تحقق أمنية مخصصة لأنظمة الذكاء الاصطناعي."` | — |
| [SRC-E73001D9AC-L000908](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L908) | 908 | `"- [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) — مبادئ المعمارية التشغيلية والأمان والموثوقية والأداء والتكلفة والاستدامة."` | — |
| [SRC-E73001D9AC-L000909](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L909) | 909 | `"- [Microsoft Azure Well-Architected Framework](https://learn.microsoft.com/en-us/azure/architecture/framework/) — مرجع مراجعة موثوقية وأمن وأداء وتكلفة الأنظمة."` | — |
| [SRC-E73001D9AC-L000910](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L910) | 910 | `"- [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework) — تصميم الأنظمة وتشغيلها وقياسها وتحسينها."` | — |
| [SRC-E73001D9AC-L000911](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L911) | 911 | `"- [Google SRE Books](https://sre.google/books/) — أهداف مستوى الخدمة وميزانيات الأخطاء والاستجابة للحوادث."` | — |
| [SRC-E73001D9AC-L000912](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L912) | 912 | `"- [DORA — Continuous Delivery](https://dora.dev/capabilities/continuous-delivery/) — تسليم تغييرات آمنة وقابلة للتكرار."` | — |
| [SRC-E73001D9AC-L000913](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L913) | 913 | `"- [OpenTelemetry](https://opentelemetry.io/docs/) — توحيد المقاييس والسجلات والتتبعات."` | — |
| [SRC-E73001D9AC-L000914](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L914) | 914 | `"- [OWASP API Security Top 10](https://owasp.org/www-project-api-security/) — مخاطر شائعة في واجهات API."` | — |
| [SRC-E73001D9AC-L000915](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L915) | 915 | `"- [SLSA](https://slsa.dev/) — سلامة سلسلة توريد البرمجيات وإثبات منشأ artifacts."` | — |
| [SRC-E73001D9AC-L000916](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L916) | 916 | `"- [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) — إمكانية الوصول إلى محتوى الويب."` | — |
| [SRC-E73001D9AC-L000917](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L917) | 917 | `"- [NIST Privacy Framework](https://www.nist.gov/privacy-framework) — إدارة مخاطر الخصوصية."` | — |
| [SRC-E73001D9AC-L000918](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L918) | 918 | `"- [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) — الاستعداد والاستجابة لحوادث الأمن السيبراني."` | — |
| [SRC-E73001D9AC-L000919](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L919) | 919 | `"- [FinOps Framework](https://www.finops.org/framework/) — الشفافية والمسؤولية وتحسين تكلفة استخدام التقنية."` | — |
| [SRC-E73001D9AC-L000920](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L920) | 920 | `"- [Omarai Global Platform Engineering Baseline](OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md) — المتطلبات الموسعة وعناصر المراجعة العملية."` | — |
| [SRC-E73001D9AC-L000921](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L921) | 921 | `""` | — |
| [SRC-E73001D9AC-L000922](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L922) | 922 | `"تُراجع الإصدارات الرسمية دوريًا، وتُسجل النسخة والتاريخ عند تحويل أي مرجع إلى قائمة اختبار. لا تُستخدم عبارة “متوافق مع NIST/OWASP” إلا بعد وجود تقييم نطاقي وأدلة تغطي المتطلبات المنطبقة."` | — |
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
