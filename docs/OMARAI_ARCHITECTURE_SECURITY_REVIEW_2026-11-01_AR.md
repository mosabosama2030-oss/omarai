# تدقيق معمارية Omarai والخيارات التقنية والممارسات الأمنية
**التاريخ:** 1 نوفمبر 2026  
**خط الأساس:** `main` عند `63b7dd01889de4aadd66acea90a2415b33376e2e`  
**فرع الإصلاح:** `fix/p0-core-consolidated-2026-11-01`  
**حالة الوثيقة:** مراجعة مصدرية؛ تغييرات الفرع غير مدمجة.

## 1. الخلاصة التنفيذية

**VERIFIED:** Omarai تطبيق Python modular monolith بواجهة HTTP مخصصة، ومحرك بحث/إجابة، وSQLite لتخزين العملاء، وموصلات بحث، وحدود للطلبات والموارد، واختبارات CI على Python 3.11 و3.12.

**VERIFIED:** توجد آليات SSRF قوية نسبيًا في جلب الصفحات: رفض الوجهات المحلية، حل DNS والتحقق من كل عنوان، الاتصال بعنوان IP مثبت بدل إعادة حل الاسم، تعطيل proxy من البيئة، وعدم اتباع redirects تلقائيًا؛ كل redirect يدوي يعاد التحقق منه.

**VERIFIED:** عزل العملاء يُبنى على هوية مستخرجة من credential موثوق، وليس على `tenant_id` المرسل في جسم الطلب. استعلامات leads الأساسية scoped بالـtenant، مع اختبارات تمنع تزوير tenant_id والوصول المتبادل.

**VERIFIED:** كان المتصفح يحتفظ برمز API في Web Storage. أزيل هذا المسار في الفرع واستُبدل بجلسات opaque خادمية، مع cookie محمي وCSRF Origin check. هذه خطوة أمنية مهمة، لكنها تحتاج اعتماد CI النهائي ومراجعة بشرية قبل الدمج.

**INFERRED:** أفضل خيار حالي هو الإبقاء على modular monolith منضبط بدل تفكيك الخدمات. لا توجد أدلة حمل أو فرق تشغيل أو حدود ملكية بيانات تبرر microservices الآن.

**UNKNOWN:** القبول الحي على الاستضافة، استمرار قاعدة البيانات بعد إعادة إنشاء الحاوية، النسخ الاحتياطي والاستعادة، الحمل متعدد العمليات، واتصال مزودي النماذج الفعلي.

## 2. المعمارية المرصودة

- `web/`: واجهتا Agent وDashboard.
- `api/omarai.py`: HTTP ingress، المصادقة، Origin/CORS، تحديد المعدل، حدود الجسم والمهلة، وتوجيه API.
- `agents/web_agent.py`: تنسيق البحث، جلب الصفحات، توليد الإجابة، تسجيل الأدلة، وطلبات النماذج.
- `agents/omarai.py`: تحليل أولي لإشارات الشراء وLeadStore وtenant/user/membership/token/session storage.
- `agents/semantic_claim_verifier.py`: تقييم دعم الادعاء من المصدر المحدد.
- `RequestBudget` ومحددات التزامن: ميزانية للطلب وعمليات البحث/النماذج وجلب الصفحات.
- `tests/`: اختبارات وحدات وتكامل وأمن وعقود قبول.

هذا **تطبيق أحادي العملية متعدد الوحدات**، وليس مجموعة microservices. يجب الحفاظ على حدود الوحدات وعقودها قبل التفكير في توزيعها.

## 3. قرارات الخيارات التقنية

### 3.1 Modular Monolith مقابل Microservices

**القرار — PROPOSED/اعتماد هذا المسار:** Modular monolith مع حدود واضحة بين API والسياسة ومحرك البحث والموصلات والتخزين والتحقق.

الأسباب:
- التطبيق الحالي يعتمد على SQLite وعمليات Python متزامنة؛ توزيع الوحدات الآن يضيف اتصالات شبكية ومصادقة بين الخدمات وتناسقًا موزعًا دون دليل أن ذلك يحل اختناقًا مثبتًا.
- اختبارات الوحدة والتكامل الحالية تتيح تغييرًا صغيرًا وقابلًا للمراجعة.
- لا تنشأ وكلاء دائمون أو Meta-Agent أو توليد ذاتي للكود قبل استقرار السياسات والعقود.

### 3.2 HTTP Runtime

**VERIFIED:** الخادم يستخدم `http.server` / `BaseHTTPRequestHandler` مع طبقات حماية مخصصة: حدود حجم الطلب، deadline للقراءة، حد اتصالات متزامنة، معدل لكل IP، headers، وفحص Origin.

**تحذير رسمي:** وثائق Python تقول إن `http.server` ليس موصى به للإنتاج، ويطبق فحوصات أمنية أساسية فقط. وجود hardening في التطبيق لا يحول مكتبة الاختبار/الخدمة البسيطة تلقائيًا إلى خادم إنتاج مدعوم.

**PROPOSED — P1:** تقييم انتقال محدود إلى WSGI/ASGI runtime مدعوم (مثل Waitress أو Uvicorn) مع إبقاء عقود API الحالية واختبارات قبول HTTP. لا أنصح بترحيل واسع داخل حزمة P0 الحالية؛ يجب أن يكون له PR مستقل ومقارنة أداء وتوافق وTimeout/Concurrency tests.

### 3.3 SQLite مقابل PostgreSQL

**VERIFIED:**
- SQLite مناسب كبداية لنسخة واحدة وقاعدة محلية دائمة.
- كل اتصال يفعّل `PRAGMA foreign_keys=ON`.
- `sqlite3.connect(timeout=10)` يحدد انتظار القفل، وأضيف wrapper يغلق الاتصال دائمًا بعد commit/rollback.
- الجلسات والرموز وعضويات المستخدمين والـleads مرتبطة بمفاتيح وعلاقات tenant.

**PROPOSED:**
- الاستمرار على SQLite للتشغيل الأولي أحادي النسخة، مع volume دائم ونسخ احتياطي/استعادة مجربين.
- عدم تفعيل WAL أو تغيير journal mode دون اختبار backup/restore والتزامن على نفس volume.
- الانتقال إلى PostgreSQL قبل تشغيل عدة replicas أو الحاجة إلى كتابة متزامنة موزعة أو إدارة مركزية لقاعدة مشتركة. SQLite لا يقدم حدًا موزعًا لمحددات المعدل أو التزامن.

### 3.4 المصادقة والجلسات وعزل المستأجرين

**VERIFIED في فرع الإصلاح:**
- bearer token لا يُخزن في `localStorage` أو `sessionStorage`.
- POST `/api/session` يتحقق من API token ثم ينشئ session ID عشوائيًا.
- لا يُخزن session ID خامًا؛ تحفظ بصمته SHA-256 في `web_sessions`.
- cookie العام يستخدم `__Host-` مع `Secure; HttpOnly; SameSite=Strict; Path=/` ومدة 8 ساعات.
- انتهاء الجلسة مفروض على الخادم، وليس اعتمادًا على Max-Age في المتصفح فقط.
- الجلسة مرتبطة ببصمة API token؛ الإبطال/الانتهاء/تغيير shared token يبطل الجلسة.
- logout يبطل سجل الجلسة.
- POST المعتمد على cookie يتطلب Origin موثوقًا.
- لا يُقبل tenant_id من جسم الطلب كمرجع صلاحية؛ الهوية والـtenant يأتيان من principal موثوق.

**حدود باقية:**
- واجهة إنشاء tenants/users/memberships/tokens وإدارة الأدوار الذاتية غير مكتملة؛ provisioning برمجي.
- viewer للقراءة فقط، وowner مطلوب لتشخيصات المزودين؛ يجب اعتماد مصفوفة أدق لأدوار admin/manager/sales_agent قبل فتح إدارة الفرق.
- HttpOnly يمنع JavaScript من قراءة session ID، لكنه لا يمنع XSS من تنفيذ طلبات باسم المستخدم؛ تبقى CSP ومخرجات DOM الآمنة ومراجعة XSS مطلوبة.
- لا يوجد بعد تنظيف دوري لسجلات الجلسات المنتهية؛ لا يؤثر ذلك في التحقق، لكنه دين صيانة.

### 3.5 موفرو النماذج وFailover

**VERIFIED في الكود/الاختبارات:**
- موفر OpenAI-compatible أساسي (OpenRouter أو base URL مخصص).
- Gemini وMistral موفران اختياريان احتياطيان عند توافر مفاتيحهما.
- التسلسل: النموذج المطلوب في المزود الأساسي، ثم fallback الخاص به إن ضُبط، ثم النموذج الافتراضي للمزود التالي.
- فشل 429 يصنف `rate_limited`، و401/403 يصنف `unauthorized`؛ لا يُسجل جسم رد المزود.
- طلب semantic verifier يستخدم `allow_fallback=False` لمنع إرسال مطالبة التحقق إلى مزود آخر بصمت.
- OpenRouter web search لا يرسل إلى Gemini/Mistral، ويظل opt-in.

**VERIFIED من وثائق الموردين:**
- Google Gemini يوفر OpenAI-compatible endpoint؛ النموذج الافتراضي في الفرع `gemini-3.1-flash-lite`.
- Mistral Small 4 يعلن API names `mistral-small-2603` و`mistral-small-latest`؛ الافتراضي `mistral-small-latest`.

**UNKNOWN:** صلاحية مفاتيح المستخدم الفعلية، quota، latency، أسعار الحساب، والاتصال الحي. لم تُنفذ أي مكالمة مزود حية أو مدفوعة. قد تنتقل المطالبات والمقتطفات إلى مزود احتياطي عند فشل الأساسي؛ يجب إبلاغ المستخدم بذلك وعدم إرسال أسرار أو بيانات عملاء سرية.

**حد الاستقلال:** عند استخدام Gemini أو Mistral فقط، النموذج الافتراضي لمراجع الادعاءات يساوي نموذج الإجابة؛ لذلك لا توجد مراجعة مستقلة بنموذج مختلف ما لم يضبط المستخدم نموذجًا صالحًا لذلك المزود. وحتى عند اختلاف model ID، يبقى ذلك تقييم دعم من نموذج وليس إثبات حقيقة خارجية.

### 3.6 البحث وSSRF وPrompt Injection

**VERIFIED في الكود:**
- قبول HTTP(S) فقط، رفض userinfo والمنافذ غير المعتمدة وعناوين localhost/private.
- حل DNS والتحقق من كل العناوين العامة، ثم الاتصال بـIP مثبت مع Host/SNI الأصليين لتقليل DNS rebinding/TOCTOU.
- `trust_env=False` يمنع proxy غير مقصود من البيئة، و`follow_redirects=False` يمنع اتباع redirect تلقائيًا؛ كل redirect يدوي يعاد فحص وجهته.
- طلبات مزودي النماذج لا تتبع redirects حتى لا تنتقل Authorization إلى origin آخر.
- محتوى الصفحات والنتائج الخارجية بيانات غير موثوقة، ولا ينبغي أن يغير تعليمات النظام أو صلاحيات الأدوات.

**المتبقي:** اختبارات SSRF لا تغطي كل بيئة DNS/IPv6/proxy فعلية؛ يلزم red-team واختبار hosted network policy.

### 3.7 GitHub Actions وسلسلة التوريد

**VERIFIED:** Workflow الأساسي يستخدم Python 3.11 و3.12، lint، الاختبارات، Docker build، وprotected API smoke. Actions المستخدمة في المسارات التي فُحصت مثبتة على commit SHAs، وصلاحيات الاختبار محدودة إلى القراءة حيث لا يلزم الكتابة.

**PROPOSED:** استمرار مراجعة كل workflow جديد بحثًا عن `pull_request_target`، أو أسرار في PR من fork، أو صلاحيات `contents: write` غير ضرورية. لا تستخدم secrets في اختبار pull request غير موثوق.

## 4. الإصلاحات التي نُقلت إلى حزمة #145

| المجال | الإصلاح | الاختبار المضاف |
|---|---|---|
| SQLite | إغلاق كل اتصال بعد transaction | اتصال مغلق بعد النجاح والفشل + rollback |
| Browser auth | opaque server-side sessions | expiry، revoke، rotation، logout، cookie flags، CSRF Origin |
| Dashboard | قبول معرف lead من 24 hex | Regression لاختبار handler |
| Intent | إزالة تعريفات المتابعة المكررة | اختبار عدد التعريفات |
| Search relevance | حد مفهومين لاستعلام من 3 مفاهيم وإزالة كلمات التنقل من topic score | mixed official/unrelated results |
| Provider errors | تصنيف 429 و401/403 وإخفاء body | fallback bounded/redacted |
| Provider failover | Gemini/Mistral defaults وfailover | mock provider selection, failover, verifier isolation |
| Diagnostics | إبقاء الموافقة الصريحة والـowner gate | اختبارات HTTP موجودة |
| Tenant isolation | tenant scope وroles وtoken revocation | اختبارات multi-tenant الحالية |

## 5. أولويات ما بعد هذه الحزمة

1. **P1 — HTTP runtime:** اختبار انتقال إلى WSGI/ASGI دون تغيير API.
2. **P1 — Role matrix:** تعريف صلاحيات admin/manager/sales_agent على العمليات والموارد.
3. **P1 — Provisioning:** أداة إدارية آمنة لإنشاء المستخدمين والعضويات والرموز، دون إظهار الأسرار في السجلات.
4. **P1 — Hosted acceptance:** اختبار هوية البناء، volume، session cookie عبر HTTPS reverse proxy، وlogout/token revocation.
5. **P2 — Data store:** backup/restore مجرب، ثم قرار PostgreSQL عند ظهور متطلبات multi-instance.
6. **P2 — Model evaluation:** corpus عربي/إنجليزي موسوم بشريًا، مقارنة موفري النماذج، وقياس false positives/abstention/latency/cost.
7. **P3 — Operations:** load/concurrency/failure tests، distributed rate limits عند تعدد النسخ، ومراقبة منزوعة الأسرار.

## 6. حالة التنفيذ

- **VERIFIED:** الملفات والتغييرات موجودة في فرع الإصلاح، ولا توجد تعديلات على main.
- **FIXED_AND_TESTED:** لا يُثبت إلا بعد نجاح CI النهائي على رأس الفرع بعد آخر تعديل.
- **NOT_RUN:** hosted acceptance، live provider calls، paid quota checks، load test، backup/restore، independent red-team.
- **UNKNOWN:** سلوك الاستضافة الحالي ومفاتيح الموردين الفعلية.

## 7. المراجع الرسمية

- [Python 3.12 — http.server security warning](https://docs.python.org/3.12/library/http.server.html)
- [Python 3.12 — sqlite3 connection context manager](https://docs.python.org/3.12/library/sqlite3.html#how-to-use-the-connection-context-manager)
- [SQLite — foreign_keys pragma](https://www.sqlite.org/pragma.html#pragma_foreign_keys)
- [SQLite — busy_timeout pragma](https://www.sqlite.org/pragma.html#pragma_busy_timeout)
- [OWASP — Multi-Tenant Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Multi_Tenant_Security_Cheat_Sheet.html)
- [OWASP — Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
- [OWASP — Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)
- [OWASP — SSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html)
- [GitHub — Security hardening for GitHub Actions](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions)
- [Google — Gemini OpenAI compatibility](https://ai.google.dev/gemini-api/docs/openai)
- [Google — Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite)
- [Mistral — Mistral Small 4 model card](https://docs.mistral.ai/models/mistral-small-4-0-26-03)
