# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **059**
- سجلات الأسطر: **300**
- النطاق: SRC-DE7EABE998-L000296 إلى SRC-A16FA6D4B5-L000074
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## واجهة الويب

### FILE-DE7EABE998 — [web/agent.html](../../web/agent.html#L1)

- النوع: **HTML**
- نطاق الفهرسة: جرد الملف + معرفات HTML والرموز داخل script/style

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-DE7EABE998-L000296](../../web/agent.html#L296) | 296 | `"  budget_exhausted:\"انتهت ميزانية النماذج قبل استكمال محور محتمل النقص.\","` | — |
| [SRC-DE7EABE998-L000297](../../web/agent.html#L297) | 297 | `"  unavailable:\"تعذرت محاولة إصلاح محور محتمل النقص.\","` | — |
| [SRC-DE7EABE998-L000298](../../web/agent.html#L298) | 298 | `"  no_change_gap_unresolved:\"لم تغيّر محاولة الإصلاح الإجابة؛ لا يزال احتمال نقص أحد المحاور قائمًا.\","` | — |
| [SRC-DE7EABE998-L000299](../../web/agent.html#L299) | 299 | `"  source_evidence_gap_unresolved:\"ذُكرت المحاور في الإجابة، لكن لم تظهر لها إشارات لفظية في المصادر؛ تظل غير محسومة.\""` | — |
| [SRC-DE7EABE998-L000300](../../web/agent.html#L300) | 300 | `" };"` | — |
| [SRC-DE7EABE998-L000301](../../web/agent.html#L301) | 301 | `" const coverageRepairHtml=coverageRepairMessages[coverageRepairStatus]?'<p class=\"warning\">حالة إصلاح التغطية: '+escapeHtml(coverageRepairMessages[coverageRepairStatus])+'</p>':\"\";"` | — |
| [SRC-DE7EABE998-L000302](../../web/agent.html#L302) | 302 | `" const criterionGapResearch=r.criterion_gap_research\|\|(result.search_report&&result.search_report.criterion_gap_research)\|\|{};"` | — |
| [SRC-DE7EABE998-L000303](../../web/agent.html#L303) | 303 | `" const criterionGapResearchStatus=criterionGapResearch.status\|\|\"\";"` | — |
| [SRC-DE7EABE998-L000304](../../web/agent.html#L304) | 304 | `" const criterionGapResearchMessages={"` | — |
| [SRC-DE7EABE998-L000305](../../web/agent.html#L305) | 305 | `"  not_needed:\"لم يرصد الفحص فجوة مصدر تستدعي بحثًا إضافيًا.\","` | — |
| [SRC-DE7EABE998-L000306](../../web/agent.html#L306) | 306 | `"  evidence_added_and_answer_regenerated:\"أضاف البحث الإضافي نص مصدر جديدًا؛ ثم أُعيد توليد الإجابة ومراجعتها.\","` | — |
| [SRC-DE7EABE998-L000307](../../web/agent.html#L307) | 307 | `"  search_completed_no_new_criterion_evidence:\"أُجري بحث إضافي للمحاور الناقصة، لكنه لم يضف نص مصدر جديدًا يمكن تمييزه.\","` | — |
| [SRC-DE7EABE998-L000308](../../web/agent.html#L308) | 308 | `"  skipped_no_reserved_search_slot:\"لم يُخصّص استعلام إضافي لهذه المهمة؛ ظلت المحاور بلا إشارة مصدر غير محسومة.\","` | — |
| [SRC-DE7EABE998-L000309](../../web/agent.html#L309) | 309 | `"  skipped_search_budget_exhausted:\"انتهت ميزانية البحث قبل إعادة البحث عن المحاور الناقصة؛ لا تُعدّ التغطية مكتملة.\","` | — |
| [SRC-DE7EABE998-L000310](../../web/agent.html#L310) | 310 | `"  search_failed:\"تعذر إكمال البحث الإضافي عن الأدلة المفقودة.\","` | — |
| [SRC-DE7EABE998-L000311](../../web/agent.html#L311) | 311 | `"  skipped_no_request_budget:\"تعذر فحص ميزانية البحث؛ لم يُنفذ بحث إضافي.\","` | — |
| [SRC-DE7EABE998-L000312](../../web/agent.html#L312) | 312 | `"  skipped_query_not_distinct:\"لم يُنفذ بحث إضافي لأن الاستعلام المقترح لم يكن مختلفًا بما يكفي.\","` | — |
| [SRC-DE7EABE998-L000313](../../web/agent.html#L313) | 313 | `"  skipped_no_valid_query:\"لم يتوفر استعلام إضافي صالح للمحاور الناقصة.\","` | — |
| [SRC-DE7EABE998-L000314](../../web/agent.html#L314) | 314 | `"  evidence_added_but_regeneration_unavailable:\"وصل نص مصدر إضافي، لكن تعذرت إعادة توليد الإجابة ومراجعتها؛ يلزم التحقق من المحاور يدويًا.\""` | — |
| [SRC-DE7EABE998-L000315](../../web/agent.html#L315) | 315 | `" };"` | — |
| [SRC-DE7EABE998-L000316](../../web/agent.html#L316) | 316 | `" const criterionGapResearchHtml=criterionGapResearchMessages[criterionGapResearchStatus]?'<p class=\"'+(criterionGapResearchStatus===\"evidence_added_and_answer_regenerated\"?\"report-note\":\"warning\")+'\">بحث فجوة الأدلة: '+escapeHtml(criterionGapResearchMessages[criterionGapResearchStatus])+'</p>':\"\";"` | — |
| [SRC-DE7EABE998-L000317](../../web/agent.html#L317) | 317 | `" const claimLedger=r.claim_evidence_ledger&&typeof r.claim_evidence_ledger===\"object\"?r.claim_evidence_ledger:null;"` | — |
| [SRC-DE7EABE998-L000318](../../web/agent.html#L318) | 318 | `" const claimSegments=claimLedger&&Array.isArray(claimLedger.segments)?claimLedger.segments:[];"` | — |
| [SRC-DE7EABE998-L000319](../../web/agent.html#L319) | 319 | `" const claimSummary=claimLedger&&claimLedger.summary&&typeof claimLedger.summary===\"object\"?claimLedger.summary:{};"` | — |
| [SRC-DE7EABE998-L000320](../../web/agent.html#L320) | 320 | `" const claimEvidenceHtml=claimLedger?'<p class=\"report-note\">سجل تتبع الاستشهادات (لا يثبت صحة الادعاء): '+escapeHtml(claimSummary.segments_with_citations??0)+' مقطعًا يحمل استشهادًا، '+escapeHtml(claimSummary.segments_without_citation_markers??0)+' بلا علامة استشهاد، '+escapeHtml(claimSummary.out_of_range_reference_count??0)+' مرجعًا خارج نطاق المصادر، '+escapeHtml(claimSummary.cited_segments_with_readable_source_evidence??0)+' مقطعًا مستشهدًا به له نص دليل قابل للقراءة.</p>'+(claimSegments.length?'<details class=\"details\"><summary>عرض سجل المقاطع والاستشهادات المرتبطة</summary><ol>'+claimSegments.map(item=>'<li><p>'+escapeHtml(item.text\|\|\"\")+'</p><p class=\"report-note\">الحالة: '+escapeHtml(item.citation_status\|\|\"غير محدد\")+' · الفحص اللفظي: '+escapeHtml(item.lexical_audit_status\|\|\"غير منفذ\")+'</p>'+(Array.isArray(item.sources)&&item.sources.length?'<ul>'+item.sources.map(source=>'<li>المصدر '+escapeHtml(source.source_index)+' · '+escapeHtml(source.title\|\|\"دون عنوان\")+' · '+escapeHtml(source.evidence_basis\|\|\"غير معروف\")+(source.url?' · <a href=\"'+escapeHtml(source.url)+'\" target=\"_blank\" rel=\"noopener noreferrer\">فتح المصدر</a>':\"\")+'</li>').join(\"\")+'</ul>':\"\")+'</li>').join(\"\")+'</ol><p class=\"report-note\">السجل يربط علامات الاستشهاد بقائمة المصادر المتاحة فقط؛ لا يُجري تحققًا دلاليًا أو مستقلًا من الحقيقة.</p></details>':\"\"):\"\";"` | — |
| [SRC-DE7EABE998-L000321](../../web/agent.html#L321) | 321 | `" const integrityHtml=integrity?'<details class=\"details\"><summary>فحص لفظي أولي: اتساق الإجابة مع الأدلة — ليس تحققًا من الحقيقة</summary><p class=\"report-note\">لا يثبت هذا الفحص صحة الوقائع أو دلالة الاستشهاد. نطاق الأدلة النصية: '+escapeHtml(integrityScope)+'.</p>'+integritySummary+taskFulfillmentHtml+claimEvidenceHtml+coverageRepairHtml+requirementEvidenceHtml+criterionGapResearchHtml+'<p class=\"report-note\">'+(integrityNumbers.length?'أرقام أو تواريخ تحتاج مراجعة لأنها لم تظهر نصيًا في المواد المتاحة: '+integrityNumbers.map(escapeHtml).join(\"، \")+'.':'لم يرصد الفحص أرقامًا محددة غائبة عن النصوص التي جمعها. هذا لا يثبت أن كل رقم صحيح أو أن المصدر يدعم الادعاء المرتبط به.')+'</p>'+citedNumberHtml+valueDiscrepancyHtml+citationAlignmentHtml+(integrityTargets.length?'<p class=\"report-note\">إشارات التغطية اللفظية لمحاور السؤال:</p><ul>'+integrityTargets.map(t=>'<li>'+escapeHtml(t.target\|\|\"محور\")+' — '+escapeHtml(t.status===\"lexical_signal_found\"?\"وُجد تطابق لفظي في الإجابة؛ ليس إثباتًا لاكتمالها\":\"قد يكون هذا المحور ناقصًا؛ لم يظهر تطابق لفظي كافٍ في الإجابة\")+' · '+escapeHtml(t.source_evidence_status===\"source_lexical_signal_found\"?\"توجد إشارة لفظية في المصادر\":\"لا توجد إشارة لفظية في المصادر\")+(Array.isArray(t.source_evidence_checks)&&t.source_evidence_checks.length?' ('+t.source_evidence_checks.map(item=>'المصدر '+escapeHtml(item.source_index)).join('، ')+')':'')+'</li>').join(\"\")+'</ul>':\"\")+'<p class=\"report-note\">المنهج: فحص لفظي حتمي محدود. لا يتحقق من معنى الادعاء أو صلة الاستشهاد به أو استقلال المصادر؛ راجع الأدلة الأصلية قبل الاعتماد.</p></details>':\"\";"` | — |
| [SRC-DE7EABE998-L000322](../../web/agent.html#L322) | 322 | `" const providerCounts=r.provider_counts&&typeof r.provider_counts===\"object\"&&!Array.isArray(r.provider_counts)?r.provider_counts:{};"` | — |
| [SRC-DE7EABE998-L000323](../../web/agent.html#L323) | 323 | `" const providerHtml=Object.entries(providerCounts).map(([p,n])=>'<span class=\"provider\">'+escapeHtml(p)+' · '+escapeHtml(n)+'</span>').join(\"\");"` | — |
| [SRC-DE7EABE998-L000324](../../web/agent.html#L324) | 324 | `" const notes=Array.isArray(e.warnings)?e.warnings:[];"` | — |
| [SRC-DE7EABE998-L000325](../../web/agent.html#L325) | 325 | `" const queryList=Array.isArray(result.search_queries)?result.search_queries:[];"` | — |
| [SRC-DE7EABE998-L000326](../../web/agent.html#L326) | 326 | `" const details=queryList.length?'<details class=\"details\"><summary>زوايا البحث المستخدمة ('+queryList.length+')</summary><ol>'+queryList.map(q=>'<li>'+escapeHtml(q)+'</li>').join(\"\")+'</ol></details>':\"\";"` | — |
| [SRC-DE7EABE998-L000327](../../web/agent.html#L327) | 327 | `" const coverageText=lead"` | — |
| [SRC-DE7EABE998-L000328](../../web/agent.html#L328) | 328 | `"  ? (leadResearchIncomplete"` | — |
| [SRC-DE7EABE998-L000329](../../web/agent.html#L329) | 329 | `"     ? \"تعطل البحث أو لم يكتمل التقرير؛ الأعداد غير المتاحة ليست صفرًا، ولا يمكن استنتاج عدم وجود عملاء.\""` | — |
| [SRC-DE7EABE998-L000330](../../web/agent.html#L330) | 330 | `"     : noQualifiedLeads"` | — |
| [SRC-DE7EABE998-L000331](../../web/agent.html#L331) | 331 | `"      ? \"لم تثبت النتائج وجود أي عميل محتمل. عدد صفحات العقارات أو النطاقات ليس عدد المشترين.\""` | — |
| [SRC-DE7EABE998-L000332](../../web/agent.html#L332) | 332 | `"      : \"الإشارات العلنية لا تثبت هوية الشخص أو استمرار رغبته في الشراء؛ راجع نص المصدر وتاريخه يدويًا.\")"` | — |
| [SRC-DE7EABE998-L000333](../../web/agent.html#L333) | 333 | `"  : researchErrorOutcome"` | — |
| [SRC-DE7EABE998-L000334](../../web/agent.html#L334) | 334 | `"   ? \"تعذر تحديد تغطية البحث لأن مسار تجميع الأدلة لم يكتمل؛ الأرقام غير المتاحة ليست صفرًا.\""` | — |
| [SRC-DE7EABE998-L000335](../../web/agent.html#L335) | 335 | `"   : \"تغطية الأدلة: \"+scoreLabel+\" — يصف هذا الوصف اتساع الأدلة المتاحة ولا يمثل احتمال صحة الإجابة.\";"` | — |
| [SRC-DE7EABE998-L000336](../../web/agent.html#L336) | 336 | `" const usableSourceCount=researchErrorOutcome?null:(r.usable_sources_after_filtering??sources.length);"` | — |
| [SRC-DE7EABE998-L000337](../../web/agent.html#L337) | 337 | `" const attemptText=result&&result.search_attempted===true"` | — |
| [SRC-DE7EABE998-L000338](../../web/agent.html#L338) | 338 | `"  ? (r.search_outcome===\"attempted_research_error\""` | — |
| [SRC-DE7EABE998-L000339](../../web/agent.html#L339) | 339 | `"     ? \"بدأت محاولة البحث، لكن تعطل مسار تجميع الأدلة قبل اكتمال التقرير؛ لم يمكن تحديد عدد المصادر القابلة للاستخدام.\""` | — |
| [SRC-DE7EABE998-L000340](../../web/agent.html#L340) | 340 | `"     : \"تمت محاولة البحث في الويب. عدد المصادر القابلة للاستخدام بعد التصفية: \"+(usableSourceCount??\"غير محدد\")+\".\")"` | — |
| [SRC-DE7EABE998-L000341](../../web/agent.html#L341) | 341 | `"  : result&&result.search_attempted===false"` | — |
| [SRC-DE7EABE998-L000342](../../web/agent.html#L342) | 342 | `"   ? \"لم تُنفّذ محاولة بحث ويب في هذه الجولة.\""` | — |
| [SRC-DE7EABE998-L000343](../../web/agent.html#L343) | 343 | `"   : r.search_outcome===\"unknown_after_research_error\""` | — |
| [SRC-DE7EABE998-L000344](../../web/agent.html#L344) | 344 | `"    ? \"تعطل مسار البحث، ولم يمكن تأكيد ما إذا كانت محاولة البحث قد بدأت أو كم مصدرًا كان قابلًا للاستخدام.\""` | — |
| [SRC-DE7EABE998-L000345](../../web/agent.html#L345) | 345 | `"    : \"حالة محاولة البحث غير موضحة في الاستجابة.\";"` | — |
| [SRC-DE7EABE998-L000346](../../web/agent.html#L346) | 346 | `" const qualityText='تصنيف جودة البحث يصف تغطية العملية والأدلة المتاحة، ولا يمثل احتمال صحة الوقائع.';"` | — |
| [SRC-DE7EABE998-L000347](../../web/agent.html#L347) | 347 | `" const reviewText=r.claim_audit_semantics==='model_assisted_not_independent_fact_check'?'مراجعة الادعاءات تمت بمساعدة نموذج لغوي؛ وهي ليست تحققًا مستقلًا من صحة الحقائق.':'لم يثبت إجراء تحقق مستقل من صحة الحقائق.';"` | — |
| [SRC-DE7EABE998-L000348](../../web/agent.html#L348) | 348 | `" const diversityText='اختلاف النطاقات المسجلة لا يثبت الاستقلال التحريري؛ فقد تنقل المواقع عن مصدر أصلي واحد.';"` | — |
| [SRC-DE7EABE998-L000349](../../web/agent.html#L349) | 349 | `" const reportNotes=[coverageText,attemptText,qualityText,reviewText,diversityText,...notes].map(n=>'<p class=\"report-note\">'+escapeHtml(n)+'</p>').join(\"\");"` | — |
| [SRC-DE7EABE998-L000350](../../web/agent.html#L350) | 350 | `" const review=r.second_pass_review===\"model_claim_audit_completed\"?\"مراجعة الادعاءات بمساعدة النموذج تمت (ليست تحققًا مستقلًا)\":r.second_pass_review===\"model_claim_audit_completed_before_coverage_repair\"?\"تمت مراجعة المسودة قبل تعديل التغطية؛ النسخة المعدلة لم تخضع لمراجعة ثانية\":r.second_pass_review===\"model_claim_audit_unavailable\"?\"تعذرت مراجعة الادعاءات بمساعدة النموذج\":\"\";"` | — |
| [SRC-DE7EABE998-L000351](../../web/agent.html#L351) | 351 | `" return '<div class=\"report-head\"><b>ملخص الأدلة وتغطية البحث</b><span class=\"coverage\">'+escapeHtml(scoreLabel)+'</span></div><div class=\"metrics\">'+metricHtml+'</div>'+completionSummary+completionDetailsHtml+operationalHtml+connectorDetails+integrityHtml+reportNotes+(providerHtml?'<div class=\"providers\">'+providerHtml+'</div>':\"\")+(review?'<p class=\"report-note\">'+escapeHtml(review)+'</p>':\"\")+details;"` | — |
| [SRC-DE7EABE998-L000352](../../web/agent.html#L352) | 352 | `"}"` | — |
| [SRC-DE7EABE998-L000353](../../web/agent.html#L353) | 353 | `"function addMessage(role,text,result,options={}){"` | — |
| [SRC-DE7EABE998-L000354](../../web/agent.html#L354) | 354 | `" const welcome=$(\"welcome\");if(welcome)welcome.remove();"` | — |
| [SRC-DE7EABE998-L000355](../../web/agent.html#L355) | 355 | `" const box=document.createElement(\"div\");box.className=\"message \"+(role===\"user\"?\"user\":\"assistant\");"` | — |
| [SRC-DE7EABE998-L000356](../../web/agent.html#L356) | 356 | `" const who=document.createElement(\"div\");who.className=\"who\";"` | — |
| [SRC-DE7EABE998-L000357](../../web/agent.html#L357) | 357 | `" who.textContent=role===\"user\"?\"أنت\":(result&&result.used_language_model?\"Omarai · بحث وتحليل توليدي\":\"Omarai · إجابة جزئية أو احتياطية\");"` | — |
| [SRC-DE7EABE998-L000358](../../web/agent.html#L358) | 358 | `" box.appendChild(who);"` | — |
| [SRC-DE7EABE998-L000359](../../web/agent.html#L359) | 359 | `" const linkedQuestion=(options&&options.question)\|\|(result&&result.question);"` | — |
| [SRC-DE7EABE998-L000360](../../web/agent.html#L360) | 360 | `" if(role===\"assistant\"&&linkedQuestion){"` | — |
| [SRC-DE7EABE998-L000361](../../web/agent.html#L361) | 361 | `"  const context=document.createElement(\"div\");context.className=\"message-context\";"` | — |
| [SRC-DE7EABE998-L000362](../../web/agent.html#L362) | 362 | `"  context.textContent=\"ردًا على السؤال: \"+linkedQuestion;box.appendChild(context);"` | — |
| [SRC-DE7EABE998-L000363](../../web/agent.html#L363) | 363 | `" }"` | — |
| [SRC-DE7EABE998-L000364](../../web/agent.html#L364) | 364 | `" const bubble=document.createElement(\"div\");bubble.className=\"bubble\";bubble.innerHTML=answerMarkup(text);box.appendChild(bubble);"` | — |
| [SRC-DE7EABE998-L000365](../../web/agent.html#L365) | 365 | `" if(result&&result.used_web_search!==true&&result.kind!==\"general_answer\"&&result.kind!==\"capability_answer\"){"` | — |
| [SRC-DE7EABE998-L000366](../../web/agent.html#L366) | 366 | `"  const notice=document.createElement(\"div\");notice.className=\"warning\";"` | — |
| [SRC-DE7EABE998-L000367](../../web/agent.html#L367) | 367 | `"  notice.textContent=result.search_attempted===true?\"نُفذت محاولة بحث، لكن لم يؤكد النظام توفر مصادر قابلة للاستخدام؛ تعامل مع الإجابة باعتبارها غير مكتملة حتى مراجعة المصادر.\":result.search_attempted===false?\"لم تُنفذ محاولة بحث ويب في هذه الجولة؛ لا تعتبر الإجابة نتيجة بحث حي.\":\"لم يؤكد النظام نجاح البحث الحي في هذه الجولة؛ تعامل مع الإجابة باعتبارها غير مكتملة حتى مراجعة المصادر.\";"` | — |
| [SRC-DE7EABE998-L000368](../../web/agent.html#L368) | 368 | `"  box.appendChild(notice);"` | — |
| [SRC-DE7EABE998-L000369](../../web/agent.html#L369) | 369 | `" }"` | — |
| [SRC-DE7EABE998-L000370](../../web/agent.html#L370) | 370 | `" if(result&&result.used_language_model!==true&&result.kind!==\"general_answer\"&&result.kind!==\"capability_answer\"){"` | — |
| [SRC-DE7EABE998-L000371](../../web/agent.html#L371) | 371 | `"  const notice=document.createElement(\"div\");notice.className=\"warning\";"` | — |
| [SRC-DE7EABE998-L000372](../../web/agent.html#L372) | 372 | `"  notice.textContent=\"لم تُستخدم استجابة مؤكدة من النموذج اللغوي؛ قد تكون الإجابة مقتطفات أو ردًا احتياطيًا وليست تحليلًا توليديًا كاملًا.\";"` | — |
| [SRC-DE7EABE998-L000373](../../web/agent.html#L373) | 373 | `"  box.appendChild(notice);"` | — |
| [SRC-DE7EABE998-L000374](../../web/agent.html#L374) | 374 | `" }"` | — |
| [SRC-DE7EABE998-L000375](../../web/agent.html#L375) | 375 | `" if(result&&result.search_report){"` | — |
| [SRC-DE7EABE998-L000376](../../web/agent.html#L376) | 376 | `"  const report=document.createElement(\"section\");report.className=\"report\";report.innerHTML=renderReport(result);box.appendChild(report);"` | — |
| [SRC-DE7EABE998-L000377](../../web/agent.html#L377) | 377 | `" }"` | — |
| [SRC-DE7EABE998-L000378](../../web/agent.html#L378) | 378 | `" if(result&&Array.isArray(result.warnings)&&result.warnings.length){"` | — |
| [SRC-DE7EABE998-L000379](../../web/agent.html#L379) | 379 | `"  const warning=document.createElement(\"div\");warning.className=\"warning\";"` | — |
| [SRC-DE7EABE998-L000380](../../web/agent.html#L380) | 380 | `"  warning.textContent=result.warnings.join(\" \");box.appendChild(warning);"` | — |
| [SRC-DE7EABE998-L000381](../../web/agent.html#L381) | 381 | `" }"` | — |
| [SRC-DE7EABE998-L000382](../../web/agent.html#L382) | 382 | `" const rawSources=result&&Array.isArray(result.sources)?result.sources:[];"` | — |
| [SRC-DE7EABE998-L000383](../../web/agent.html#L383) | 383 | `" const usableSources=rawSources.filter(s=>s&&typeof s===\"object\"&&safeSourceUrl(s.url));"` | — |
| [SRC-DE7EABE998-L000384](../../web/agent.html#L384) | 384 | `" if(usableSources.length){"` | — |
| [SRC-DE7EABE998-L000385](../../web/agent.html#L385) | 385 | `"  const sources=document.createElement(\"div\");sources.className=\"sources\";"` | — |
| [SRC-DE7EABE998-L000386](../../web/agent.html#L386) | 386 | `"  sources.innerHTML=usableSources.map((s,i)=>renderSource(s,i)).join(\"\");box.appendChild(sources);"` | — |
| [SRC-DE7EABE998-L000387](../../web/agent.html#L387) | 387 | `" }else if(role===\"assistant\"&&result&&result.kind!==\"general_answer\"&&result.kind!==\"capability_answer\"){"` | — |
| [SRC-DE7EABE998-L000388](../../web/agent.html#L388) | 388 | `"  const no=document.createElement(\"p\");no.className=\"no-sources\";"` | — |
| [SRC-DE7EABE998-L000389](../../web/agent.html#L389) | 389 | `"  no.textContent=\"لم يتم إرجاع مصدر صالح قابل للفتح في هذه الجولة. لا تعتبر الإجابة المدعومة بلا مصادر نتيجة بحث ناجحة.\";"` | — |
| [SRC-DE7EABE998-L000390](../../web/agent.html#L390) | 390 | `"  box.appendChild(no);"` | — |
| [SRC-DE7EABE998-L000391](../../web/agent.html#L391) | 391 | `" }"` | — |
| [SRC-DE7EABE998-L000392](../../web/agent.html#L392) | 392 | `" $(\"messages\").appendChild(box);box.scrollIntoView({behavior:\"smooth\",block:\"end\"});"` | — |
| [SRC-DE7EABE998-L000393](../../web/agent.html#L393) | 393 | `" return box;"` | — |
| [SRC-DE7EABE998-L000394](../../web/agent.html#L394) | 394 | `"}"` | — |
| [SRC-DE7EABE998-L000395](../../web/agent.html#L395) | 395 | `"function setBusy(on){busy=on;$(\"send\").disabled=on;$(\"send\").textContent=on?\"يبحث…\":\"ابحث ←\";$(\"question\").disabled=on;document.querySelectorAll(\".mode-btn\").forEach(b=>b.disabled=on);}"` | — |
| [SRC-DE7EABE998-L000396](../../web/agent.html#L396) | 396 | `"async function ask(value){"` | — |
| [SRC-DE7EABE998-L000397](../../web/agent.html#L397) | 397 | `" const q=(value??$(\"question\").value).trim();if(!q\|\|busy)return;"` | — |
| [SRC-DE7EABE998-L000398](../../web/agent.html#L398) | 398 | `" addMessage(\"user\",q);$(\"question\").value=\"\";setBusy(true);"` | — |
| [SRC-DE7EABE998-L000399](../../web/agent.html#L399) | 399 | `" setStatus(\"جارٍ تنفيذ البحث عن السؤال الحالي…\",\"warn\");"` | — |
| [SRC-DE7EABE998-L000400](../../web/agent.html#L400) | 400 | `" const pending=document.createElement(\"div\");pending.className=\"message assistant\";"` | — |
| [SRC-DE7EABE998-L000401](../../web/agent.html#L401) | 401 | `" pending.innerHTML='<div class=\"who\">Omarai · '+escapeHtml(modeName(activeMode))+'</div><div class=\"bubble\"><div class=\"pending\"><span class=\"spinner\"></span><span>يبحث الآن ويجمع المصادر. ستظهر نتيجة هذه الجولة مرتبطة بسؤالك أدناه.</span></div></div>';"` | — |
| [SRC-DE7EABE998-L000402](../../web/agent.html#L402) | 402 | `" $(\"messages\").appendChild(pending);pending.scrollIntoView({behavior:\"smooth\",block:\"end\"});"` | — |
| [SRC-DE7EABE998-L000403](../../web/agent.html#L403) | 403 | `" try{"` | — |
| [SRC-DE7EABE998-L000404](../../web/agent.html#L404) | 404 | `"  const response=await fetch(\"/api/agent\",{method:\"POST\",credentials:\"same-origin\",headers:apiHeaders(),body:JSON.stringify({question:q,history:history.slice(-8),mode:activeMode})});"` | — |
| [SRC-DE7EABE998-L000405](../../web/agent.html#L405) | 405 | `"  const data=await response.json().catch(()=>({}));"` | — |
| [SRC-DE7EABE998-L000406](../../web/agent.html#L406) | 406 | `"  pending.remove();"` | — |
| [SRC-DE7EABE998-L000407](../../web/agent.html#L407) | 407 | `"  if(!response.ok){"` | — |
| [SRC-DE7EABE998-L000408](../../web/agent.html#L408) | 408 | `"   if(response.status===401)throw Error(\"رمز الوصول غير صحيح أو غير محفوظ. راجع رمز التطبيق المستضاف.\");"` | — |
| [SRC-DE7EABE998-L000409](../../web/agent.html#L409) | 409 | `"   if(response.status===429)throw Error(\"تجاوز حد الطلبات المؤقت. انتظر قليلًا ثم أعد المحاولة.\");"` | — |
| [SRC-DE7EABE998-L000410](../../web/agent.html#L410) | 410 | `"   throw Error(data.error\|\|\"تعذر إكمال البحث. أعد المحاولة بعد التحقق من الاتصال.\");"` | — |
| [SRC-DE7EABE998-L000411](../../web/agent.html#L411) | 411 | `"  }"` | — |
| [SRC-DE7EABE998-L000412](../../web/agent.html#L412) | 412 | `"  addMessage(\"assistant\",data.answer\|\|\"لم يرجع الخادم نص إجابة.\",data);"` | — |
| [SRC-DE7EABE998-L000413](../../web/agent.html#L413) | 413 | `"  history.push({role:\"user\",content:q},{role:\"assistant\",content:String(data.answer\|\|\"\")});"` | — |
| [SRC-DE7EABE998-L000414](../../web/agent.html#L414) | 414 | `"  const sources=Array.isArray(data.sources)?data.sources.filter(s=>s&&safeSourceUrl(s.url)):[];"` | — |
| [SRC-DE7EABE998-L000415](../../web/agent.html#L415) | 415 | `"  if(data.kind===\"general_answer\"){"` | — |
| [SRC-DE7EABE998-L000416](../../web/agent.html#L416) | 416 | `"   setStatus(\"اكتملت إجابة المعرفة العامة دون بحث ويب\",\"ok\");"` | — |
| [SRC-DE7EABE998-L000417](../../web/agent.html#L417) | 417 | `"  }else if(data.kind===\"capability_answer\"){"` | — |
| [SRC-DE7EABE998-L000418](../../web/agent.html#L418) | 418 | `"   setStatus(\"إجابة عن قدرات Omarai وحدوده · لم يُجر بحث حي\",\"ok\");"` | — |
| [SRC-DE7EABE998-L000419](../../web/agent.html#L419) | 419 | `"  }else if(data.used_web_search===true&&data.used_language_model===true&&sources.length>0){"` | — |
| [SRC-DE7EABE998-L000420](../../web/agent.html#L420) | 420 | `"   setStatus(\"اكتمل البحث والتحليل · \"+sources.length+\" مصدرًا صالحًا\",\"ok\");"` | — |
| [SRC-DE7EABE998-L000421](../../web/agent.html#L421) | 421 | `"  }else if(data.used_web_search===true&&sources.length>0){"` | — |
| [SRC-DE7EABE998-L000422](../../web/agent.html#L422) | 422 | `"   setStatus(\"البحث أعاد مصادر، لكن التحليل غير مكتمل\",\"warn\");"` | — |
| [SRC-DE7EABE998-L000423](../../web/agent.html#L423) | 423 | `"  }else{"` | — |
| [SRC-DE7EABE998-L000424](../../web/agent.html#L424) | 424 | `"   setStatus(\"نتيجة جزئية: لا يوجد بحث حي مؤكد مع مصادر كافية\",\"bad\");"` | — |
| [SRC-DE7EABE998-L000425](../../web/agent.html#L425) | 425 | `"  }"` | — |
| [SRC-DE7EABE998-L000426](../../web/agent.html#L426) | 426 | `" }catch(error){"` | — |
| [SRC-DE7EABE998-L000427](../../web/agent.html#L427) | 427 | `"  pending.remove();"` | — |
| [SRC-DE7EABE998-L000428](../../web/agent.html#L428) | 428 | `"  const safeMessage=error&&error.message?error.message:\"تعذر إكمال الطلب.\";"` | — |
| [SRC-DE7EABE998-L000429](../../web/agent.html#L429) | 429 | `"  const box=addMessage(\"assistant\",safeMessage,null,{question:q});"` | — |
| [SRC-DE7EABE998-L000430](../../web/agent.html#L430) | 430 | `"  const actions=document.createElement(\"div\");actions.className=\"retry-row\";"` | — |
| [SRC-DE7EABE998-L000431](../../web/agent.html#L431) | 431 | `"  const retry=document.createElement(\"button\");retry.type=\"button\";retry.className=\"retry-button\";"` | — |
| [SRC-DE7EABE998-L000432](../../web/agent.html#L432) | 432 | `"  retry.textContent=\"إعادة محاولة هذا السؤال\";"` | — |
| [SRC-DE7EABE998-L000433](../../web/agent.html#L433) | 433 | `"  retry.addEventListener(\"click\",()=>ask(q));actions.appendChild(retry);box.appendChild(actions);"` | — |
| [SRC-DE7EABE998-L000434](../../web/agent.html#L434) | 434 | `"  setStatus(\"لم يكتمل الطلب؛ يمكنك إعادة محاولة السؤال نفسه\",\"bad\");"` | — |
| [SRC-DE7EABE998-L000435](../../web/agent.html#L435) | 435 | `" }finally{"` | — |
| [SRC-DE7EABE998-L000436](../../web/agent.html#L436) | 436 | `"  setBusy(false);$(\"question\").focus();"` | — |
| [SRC-DE7EABE998-L000437](../../web/agent.html#L437) | 437 | `" }"` | — |
| [SRC-DE7EABE998-L000438](../../web/agent.html#L438) | 438 | `"}"` | — |
| [SRC-DE7EABE998-L000439](../../web/agent.html#L439) | 439 | `"async function runDiagnostics(){"` | — |
| [SRC-DE7EABE998-L000440](../../web/agent.html#L440) | 440 | `" const button=$(\"runDiagnostics\"),output=$(\"diagnosticsResult\");if(button.disabled)return;"` | — |
| [SRC-DE7EABE998-L000441](../../web/agent.html#L441) | 441 | `" if(!window.confirm(\"سيجري هذا الاختبار اتصالات فعلية بمحركات البحث والنموذج، وقد يستهلك حصص الموفّرين أو يترتب عليه رسوم. هل توافق على تنفيذ هذه الاتصالات الآن؟\"))return;"` | — |
| [SRC-DE7EABE998-L000442](../../web/agent.html#L442) | 442 | `" button.disabled=true;button.textContent=\"جارٍ الاختبار الحقيقي…\";output.textContent=\"تُرسل الآن طلبات فعلية إلى موفّري البحث والنموذج بعد موافقتك.\";"` | — |
| [SRC-DE7EABE998-L000443](../../web/agent.html#L443) | 443 | `" try{"` | — |
| [SRC-DE7EABE998-L000444](../../web/agent.html#L444) | 444 | `"  const response=await fetch(\"/api/diagnostics\",{method:\"POST\",credentials:\"same-origin\",headers:apiHeaders(),body:JSON.stringify({test_model:true,test_social:$(\"diagSocial\").checked,allow_provider_usage:true})});"` | — |
| [SRC-DE7EABE998-L000445](../../web/agent.html#L445) | 445 | `"  const data=await response.json();if(!response.ok)throw Error(data.error\|\|\"فشل طلب الاختبار\");"` | — |
| [SRC-DE7EABE998-L000446](../../web/agent.html#L446) | 446 | `"  const labels={passed:\"نجح فعليًا\",degraded:\"جزئي أو بلا نتائج كافية\",failed:\"فشل\",skipped:\"لم يُختبر\",not_configured:\"غير مضبوط\"};"` | — |
| [SRC-DE7EABE998-L000447](../../web/agent.html#L447) | 447 | `"  const lines=[\"النتيجة: \"+(labels[data.overall_status]\|\|data.overall_status)];"` | — |
| [SRC-DE7EABE998-L000448](../../web/agent.html#L448) | 448 | `"  for(const [key,label] of [[\"web_search\",\"بحث الإنترنت\"],[\"language_model\",\"النموذج اللغوي\"],[\"social_search\",\"المصادر الاجتماعية\"]]){"` | — |
| [SRC-DE7EABE998-L000449](../../web/agent.html#L449) | 449 | `"   const item=(data.checks\|\|{})[key];if(!item)continue;"` | — |
| [SRC-DE7EABE998-L000450](../../web/agent.html#L450) | 450 | `"   lines.push(label+\": \"+(labels[item.status]\|\|item.status)+(item.result_count!==undefined?\" · \"+item.result_count+\" نتيجة\":\"\"));"` | — |
| [SRC-DE7EABE998-L000451](../../web/agent.html#L451) | 451 | `"   if(item.provider_counts&&Object.keys(item.provider_counts).length)lines.push(\"المصادر التي أعادت نتائج: \"+Object.entries(item.provider_counts).map(([p,n])=>p+\" (\"+n+\")\").join(\"، \"));"` | — |
| [SRC-DE7EABE998-L000452](../../web/agent.html#L452) | 452 | `"   if(item.note)lines.push(item.note);"` | — |
| [SRC-DE7EABE998-L000453](../../web/agent.html#L453) | 453 | `"   if(item.warnings&&item.warnings.length)lines.push(item.warnings.join(\"؛ \"));"` | — |
| [SRC-DE7EABE998-L000454](../../web/agent.html#L454) | 454 | `"  }"` | — |
| [SRC-DE7EABE998-L000455](../../web/agent.html#L455) | 455 | `"  if(data.model_usage&&data.model_usage.length)lines.push(\"النموذج المستخدم: \"+data.model_usage.map(x=>x.used_model).join(\"، \"));"` | — |
| [SRC-DE7EABE998-L000456](../../web/agent.html#L456) | 456 | `"  if(data.elapsed_ms!==undefined)lines.push(\"مدة الاختبار: \"+(data.elapsed_ms/1000).toFixed(1)+\" ثانية\");"` | — |
| [SRC-DE7EABE998-L000457](../../web/agent.html#L457) | 457 | `"  output.textContent=lines.join(\"\\n\");setStatus(data.overall_status===\"passed\"?\"نجح الاختبار الحي\":data.overall_status===\"failed\"?\"فشل الاختبار الحي\":\"نتيجة الاختبار جزئية\",data.overall_status===\"passed\"?\"ok\":data.overall_status===\"failed\"?\"bad\":\"warn\");"` | — |
| [SRC-DE7EABE998-L000458](../../web/agent.html#L458) | 458 | `" }catch(e){output.textContent=\"تعذّر الاختبار الحي: \"+(e&&e.message?e.message:\"خطأ غير معروف\");setStatus(\"فشل الاختبار الحي\",\"bad\");}"` | — |
| [SRC-DE7EABE998-L000459](../../web/agent.html#L459) | 459 | `" finally{button.disabled=false;button.textContent=\"إعادة الاختبار الحي\";}"` | — |
| [SRC-DE7EABE998-L000460](../../web/agent.html#L460) | 460 | `"}"` | — |
| [SRC-DE7EABE998-L000461](../../web/agent.html#L461) | 461 | `"async function checkHealth(){"` | — |
| [SRC-DE7EABE998-L000462](../../web/agent.html#L462) | 462 | `" try{"` | — |
| [SRC-DE7EABE998-L000463](../../web/agent.html#L463) | 463 | `"  const r=await fetch(\"/api/health\");const d=await r.json();const a=d.agent\|\|{};"` | — |
| [SRC-DE7EABE998-L000464](../../web/agent.html#L464) | 464 | `"  const configured=[];"` | — |
| [SRC-DE7EABE998-L000465](../../web/agent.html#L465) | 465 | `"  if(a.brave_search_api_configured)configured.push(\"Brave API\");"` | — |
| [SRC-DE7EABE998-L000466](../../web/agent.html#L466) | 466 | `"  if(a.tavily_search_api_configured)configured.push(\"Tavily API\");"` | — |
| [SRC-DE7EABE998-L000467](../../web/agent.html#L467) | 467 | `"  if(a.reddit_oauth_configured)configured.push(\"Reddit OAuth\");"` | — |
| [SRC-DE7EABE998-L000468](../../web/agent.html#L468) | 468 | `"  if(a.facebook_pages_api_configured)configured.push(\"Facebook Pages\");"` | — |
| [SRC-DE7EABE998-L000469](../../web/agent.html#L469) | 469 | `"  if(a.instagram_graph_api_configured)configured.push(\"Instagram Graph\");"` | — |
| [SRC-DE7EABE998-L000470](../../web/agent.html#L470) | 470 | `"  if(a.x_api_configured)configured.push(\"X API\");"` | — |
| [SRC-DE7EABE998-L000471](../../web/agent.html#L471) | 471 | `"  if(a.youtube_api_configured)configured.push(\"YouTube API\");"` | — |
| [SRC-DE7EABE998-L000472](../../web/agent.html#L472) | 472 | `"  const model=!!a.language_model_configured, search=!!a.web_search_ready;"` | — |
| [SRC-DE7EABE998-L000473](../../web/agent.html#L473) | 473 | `"  $(\"setupStatus\").textContent=(search?\"حزم البحث مثبتة. \":\"حزم البحث تحتاج تثبيتًا. \")+(model?\"مفتاح نموذج اللغة موجود في جلسة الخادم. \":\"النموذج التوليدي غير مضبوط بعد. \")+\"لم يتم تأكيد اتصال الإنترنت من هذه الشاشة وحدها؛ شغّل الاختبار الحي. لا تظهر هنا مفاتيح الخدمات أو قيمها.\";"` | — |
| [SRC-DE7EABE998-L000474](../../web/agent.html#L474) | 474 | `"  $(\"providerSetup\").innerHTML=configured.length?'<span class=\"config-label\">موصلات مفاتيحها مضبوطة: '+configured.map(escapeHtml).join(\" · \")+'</span>':'<p>لم تُضبط مفاتيح API البحثية الإضافية؛ يظل Omarai قادرًا على تجربة محركات البحث العامة المتاحة.</p>';"` | — |
| [SRC-DE7EABE998-L000475](../../web/agent.html#L475) | 475 | `"  setStatus(\"الإعداد ظاهر · يلزم اختبار حي\",\"warn\");"` | — |
| [SRC-DE7EABE998-L000476](../../web/agent.html#L476) | 476 | `" }catch(e){setStatus(\"تعذر فحص الإعداد\",\"bad\");$(\"setupStatus\").textContent=\"تعذر الاتصال بخادم Omarai المحلي. تأكد أن الخادم يعمل في Termux.\";}"` | — |
| [SRC-DE7EABE998-L000477](../../web/agent.html#L477) | 477 | `"}"` | — |
| [SRC-DE7EABE998-L000478](../../web/agent.html#L478) | 478 | `"document.querySelectorAll(\".mode-btn\").forEach(button=>button.addEventListener(\"click\",()=>{"` | — |
| [SRC-DE7EABE998-L000479](../../web/agent.html#L479) | 479 | `" activeMode=button.dataset.mode;"` | — |
| [SRC-DE7EABE998-L000480](../../web/agent.html#L480) | 480 | `" document.querySelectorAll(\".mode-btn\").forEach(other=>{const active=other===button;other.classList.toggle(\"active\",active);other.setAttribute(\"aria-pressed\",String(active));});"` | — |
| [SRC-DE7EABE998-L000481](../../web/agent.html#L481) | 481 | `"}));"` | — |
| [SRC-DE7EABE998-L000482](../../web/agent.html#L482) | 482 | `"$(\"send\").addEventListener(\"click\",()=>ask());"` | — |
| [SRC-DE7EABE998-L000483](../../web/agent.html#L483) | 483 | `"$(\"question\").addEventListener(\"keydown\",e=>{if(e.key===\"Enter\"&&!e.shiftKey){e.preventDefault();ask();}});"` | — |
| [SRC-DE7EABE998-L000484](../../web/agent.html#L484) | 484 | `"$(\"clear\").addEventListener(\"click\",()=>{history.length=0;$(\"messages\").innerHTML='<div class=\"welcome\" id=\"welcome\"><div class=\"welcome-icon\">⌕</div><h3>محادثة جديدة</h3><p>اكتب سؤالك واختر نمط البحث المناسب. المصادر والتغطية سيظهران أسفل الإجابة.</p></div>';$(\"question\").focus();});"` | — |
| [SRC-DE7EABE998-L000485](../../web/agent.html#L485) | 485 | `"document.querySelectorAll(\".suggestions button\").forEach(b=>b.addEventListener(\"click\",()=>ask(b.textContent)));"` | — |
| [SRC-DE7EABE998-L000486](../../web/agent.html#L486) | 486 | `"async function loginBrowserSession(){"` | — |
| [SRC-DE7EABE998-L000487](../../web/agent.html#L487) | 487 | `"  const token=$(\"accessToken\").value.trim();"` | — |
| [SRC-DE7EABE998-L000488](../../web/agent.html#L488) | 488 | `"  if(!token){$(\"authStatus\").textContent=\"أدخل رمز الوصول أولًا.\";return;}"` | — |
| [SRC-DE7EABE998-L000489](../../web/agent.html#L489) | 489 | `"  try{"` | — |
| [SRC-DE7EABE998-L000490](../../web/agent.html#L490) | 490 | `"    const response=await fetch(\"/api/session\",{method:\"POST\",credentials:\"same-origin\",headers:{\"Content-Type\":\"application/json\"},body:JSON.stringify({access_token:token})});"` | — |
| [SRC-DE7EABE998-L000491](../../web/agent.html#L491) | 491 | `"    const data=await response.json();"` | — |
| [SRC-DE7EABE998-L000492](../../web/agent.html#L492) | 492 | `"    if(!response.ok)throw new Error(data.error\|\|\"تعذر تسجيل الدخول.\");"` | — |
| [SRC-DE7EABE998-L000493](../../web/agent.html#L493) | 493 | `"    $(\"accessToken\").value=\"\";"` | — |
| [SRC-DE7EABE998-L000494](../../web/agent.html#L494) | 494 | `"    $(\"authStatus\").textContent=\"تم تسجيل الدخول بجلسة HttpOnly تنتهي خلال 8 ساعات أو عند انتهاء/إبطال الرمز.\";"` | — |
| [SRC-DE7EABE998-L000495](../../web/agent.html#L495) | 495 | `"    $(\"saveAccessToken\").textContent=\"متصل\";"` | — |
| [SRC-DE7EABE998-L000496](../../web/agent.html#L496) | 496 | `"  }catch(error){$(\"authStatus\").textContent=error.message;}"` | — |
| [SRC-DE7EABE998-L000497](../../web/agent.html#L497) | 497 | `"}"` | — |
| [SRC-DE7EABE998-L000498](../../web/agent.html#L498) | 498 | `"async function logoutBrowserSession(){"` | — |
| [SRC-DE7EABE998-L000499](../../web/agent.html#L499) | 499 | `"  try{"` | — |
| [SRC-DE7EABE998-L000500](../../web/agent.html#L500) | 500 | `"    const response=await fetch(\"/api/session/logout\",{method:\"POST\",credentials:\"same-origin\",headers:{\"Content-Type\":\"application/json\"},body:\"{}\"});"` | — |
| [SRC-DE7EABE998-L000501](../../web/agent.html#L501) | 501 | `"    const data=await response.json();"` | — |
| [SRC-DE7EABE998-L000502](../../web/agent.html#L502) | 502 | `"    if(!response.ok)throw new Error(data.error\|\|\"تعذر تسجيل الخروج.\");"` | — |
| [SRC-DE7EABE998-L000503](../../web/agent.html#L503) | 503 | `"    $(\"authStatus\").textContent=\"تم تسجيل الخروج.\";"` | — |
| [SRC-DE7EABE998-L000504](../../web/agent.html#L504) | 504 | `"    $(\"saveAccessToken\").textContent=\"تسجيل الدخول\";"` | — |
| [SRC-DE7EABE998-L000505](../../web/agent.html#L505) | 505 | `"  }catch(error){$(\"authStatus\").textContent=error.message;}"` | — |
| [SRC-DE7EABE998-L000506](../../web/agent.html#L506) | 506 | `"}"` | — |
| [SRC-DE7EABE998-L000507](../../web/agent.html#L507) | 507 | `"async function checkBrowserSession(){"` | — |
| [SRC-DE7EABE998-L000508](../../web/agent.html#L508) | 508 | `"  try{"` | — |
| [SRC-DE7EABE998-L000509](../../web/agent.html#L509) | 509 | `"    const response=await fetch(\"/api/session\",{credentials:\"same-origin\"});"` | — |
| [SRC-DE7EABE998-L000510](../../web/agent.html#L510) | 510 | `"    const data=await response.json();"` | — |
| [SRC-DE7EABE998-L000511](../../web/agent.html#L511) | 511 | `"    if(!response.ok)throw new Error(data.error\|\|\"لا توجد جلسة نشطة.\");"` | — |
| [SRC-DE7EABE998-L000512](../../web/agent.html#L512) | 512 | `"    $(\"authStatus\").textContent=\"جلسة نشطة بدور: \"+data.role;"` | — |
| [SRC-DE7EABE998-L000513](../../web/agent.html#L513) | 513 | `"    $(\"saveAccessToken\").textContent=\"متصل\";"` | — |
| [SRC-DE7EABE998-L000514](../../web/agent.html#L514) | 514 | `"  }catch(_error){$(\"authStatus\").textContent=\"أدخل رمز الوصول لبدء جلسة آمنة.\";}"` | — |
| [SRC-DE7EABE998-L000515](../../web/agent.html#L515) | 515 | `"}"` | — |
| [SRC-DE7EABE998-L000516](../../web/agent.html#L516) | 516 | `"$(\"saveAccessToken\").addEventListener(\"click\",loginBrowserSession);"` | — |
| [SRC-DE7EABE998-L000517](../../web/agent.html#L517) | 517 | `"$(\"logoutSession\").addEventListener(\"click\",logoutBrowserSession);"` | — |
| [SRC-DE7EABE998-L000518](../../web/agent.html#L518) | 518 | `"$(\"runDiagnostics\").addEventListener(\"click\",runDiagnostics);checkHealth();checkBrowserSession();"` | — |
| [SRC-DE7EABE998-L000519](../../web/agent.html#L519) | 519 | `"</script>"` | — |
| [SRC-DE7EABE998-L000520](../../web/agent.html#L520) | 520 | `"</body>"` | — |
| [SRC-DE7EABE998-L000521](../../web/agent.html#L521) | 521 | `"</html>"` | — |
## واجهة الويب

### FILE-A16FA6D4B5 — [web/dashboard.html](../../web/dashboard.html#L1)

- النوع: **HTML**
- نطاق الفهرسة: جرد الملف + معرفات HTML والرموز داخل script/style

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-A16FA6D4B5-L000001](../../web/dashboard.html#L1) | 1 | `"<!doctype html>"` | — |
| [SRC-A16FA6D4B5-L000002](../../web/dashboard.html#L2) | 2 | `"<html lang=\"ar\" dir=\"rtl\">"` | — |
| [SRC-A16FA6D4B5-L000003](../../web/dashboard.html#L3) | 3 | `"<head>"` | — |
| [SRC-A16FA6D4B5-L000004](../../web/dashboard.html#L4) | 4 | `"<meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"` | — |
| [SRC-A16FA6D4B5-L000005](../../web/dashboard.html#L5) | 5 | `"<meta name=\"theme-color\" content=\"#0b1020\"><title>Omarai \| مساعد اكتشاف العملاء</title>"` | — |
| [SRC-A16FA6D4B5-L000006](../../web/dashboard.html#L6) | 6 | `"<style>"` | — |
| [SRC-A16FA6D4B5-L000007](../../web/dashboard.html#L7) | 7 | `":root{color-scheme:dark;--bg:#080d19;--panel:#111a2d;--line:#263550;--muted:#98a9c5;--text:#edf4ff;--cyan:#57e5dc;--blue:#7b9cff;--green:#7be0a3;--amber:#ffca72;--red:#ff8494}"` | — |
| [SRC-A16FA6D4B5-L000008](../../web/dashboard.html#L8) | 8 | `"*{box-sizing:border-box}body{margin:0;background:radial-gradient(ellipse at 80% 0%,#162b4b 0,transparent 38%),var(--bg);font-family:system-ui,-apple-system,\"Segoe UI\",sans-serif;color:var(--text);min-height:100vh}"` | — |
| [SRC-A16FA6D4B5-L000009](../../web/dashboard.html#L9) | 9 | `".wrap{max-width:1180px;margin:auto;padding:22px}.top{display:flex;justify-content:space-between;align-items:center;gap:14px;flex-wrap:wrap;margin-bottom:22px}.brand{display:flex;align-items:center;gap:12px}.logo{width:48px;height:48px;border-radius:16px;background:linear-gradient(135deg,var(--cyan),var(--blue));color:#071020;display:grid;place-items:center;font-weight:900;font-size:22px;box-shadow:0 8px 28px #57e5dc30}.brand h1{margin:0;font-size:25px;letter-spacing:.2px}.brand p{margin:4px 0 0;color:var(--muted);font-size:13px}.badge{border:1px solid #2e5b62;background:#102a32;color:var(--cyan);padding:8px 12px;border-radius:99px;font-size:12px}"` | — |
| [SRC-A16FA6D4B5-L000010](../../web/dashboard.html#L10) | 10 | `".hero{display:grid;grid-template-columns:1.2fr .8fr;gap:16px;margin-bottom:16px}.card{background:linear-gradient(145deg,#131e33f2,#0d1526f2);border:1px solid var(--line);border-radius:22px;padding:20px;box-shadow:0 18px 40px #0002}.eyebrow{font-size:12px;color:var(--cyan);font-weight:700;letter-spacing:.4px}.card h2{font-size:21px;margin:8px 0}.muted{color:var(--muted);font-size:13px;line-height:1.8}.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:18px}.stat{padding:14px;border-radius:15px;background:#0a1222;border:1px solid #202f49}.stat strong{display:block;font-size:25px}.stat span{font-size:12px;color:var(--muted)}"` | — |
| [SRC-A16FA6D4B5-L000011](../../web/dashboard.html#L11) | 11 | `".layout{display:grid;grid-template-columns:1fr 1fr;gap:16px}.field{margin:13px 0}label{display:block;font-size:13px;color:#c7d4ea;margin-bottom:7px}input,textarea,select{width:100%;border:1px solid #30415e;background:#091222;color:var(--text);border-radius:12px;padding:12px;font:inherit;outline:none}input:focus,textarea:focus,select:focus{border-color:var(--cyan);box-shadow:0 0 0 3px #57e5dc15}textarea{min-height:132px;resize:vertical}button{border:0;border-radius:12px;padding:12px 16px;font:inherit;font-weight:750;cursor:pointer;transition:.15s}button:hover{transform:translateY(-1px)}.primary{background:linear-gradient(110deg,var(--cyan),#8cbdff);color:#071020}.secondary{background:#1c2a43;color:#dce8ff;border:1px solid #344664}.row{display:flex;gap:9px;flex-wrap:wrap}.result{display:none;margin-top:15px;padding:16px;border:1px solid #344664;border-radius:16px;background:#0a1324}.score{font-size:35px;font-weight:850}.pill{display:inline-block;border-radius:99px;padding:5px 10px;background:#18333b;color:var(--cyan);font-size:12px;margin:4px 0}.signal{padding:10px 0;border-bottom:1px solid #24324a;font-size:13px}.signal:last-child{border-bottom:0}.warning{font-size:12px;color:var(--amber);line-height:1.8;margin-top:12px}.leads{margin-top:16px}.lead{padding:14px;border:1px solid #263650;background:#0a1323;border-radius:15px;margin-top:10px}.leadhead{display:flex;justify-content:space-between;gap:10px;flex-wrap:wrap}.lead p{line-height:1.8;font-size:14px;white-space:pre-wrap;overflow-wrap:anywhere}.empty{text-align:center;padding:24px;color:var(--muted);border:1px dashed #33435c;border-radius:14px;margin-top:12px}.foot{text-align:center;color:#6f819e;font-size:11px;padding:24px 0 8px}"` | — |
| [SRC-A16FA6D4B5-L000012](../../web/dashboard.html#L12) | 12 | `"@media(max-width:800px){.hero,.layout{grid-template-columns:1fr}.wrap{padding:14px}.card{padding:16px}.brand h1{font-size:22px}.stats{gap:7px}.stat{padding:11px}.stat strong{font-size:21px}}"` | — |
| [SRC-A16FA6D4B5-L000013](../../web/dashboard.html#L13) | 13 | `"</style></head><body><div class=\"wrap\">"` | — |
| [SRC-A16FA6D4B5-L000014](../../web/dashboard.html#L14) | 14 | `"<header class=\"top\"><div class=\"brand\"><div class=\"logo\">O</div><div><h1>Omarai</h1><p>مساعد ذكي لتأهيل إشارات العملاء المحتملين</p></div></div><span class=\"badge\">● تشغيل محلي أو مستضاف حسب إعداد الخادم</span></header>"` | — |
| [SRC-A16FA6D4B5-L000015](../../web/dashboard.html#L15) | 15 | `"<section class=\"card\" style=\"margin-bottom:16px\">"` | — |
| [SRC-A16FA6D4B5-L000016](../../web/dashboard.html#L16) | 16 | `"  <div class=\"row\" style=\"align-items:end\">"` | — |
| [SRC-A16FA6D4B5-L000017](../../web/dashboard.html#L17) | 17 | `"    <div style=\"flex:1;min-width:220px\">"` | — |
| [SRC-A16FA6D4B5-L000018](../../web/dashboard.html#L18) | 18 | `"      <label for=\"accessToken\">رمز الوصول الخاص بالتطبيق (للاستضافة فقط)</label>"` | — |
| [SRC-A16FA6D4B5-L000019](../../web/dashboard.html#L19) | 19 | `"      <input id=\"accessToken\" type=\"password\" autocomplete=\"current-password\" placeholder=\"أدخل رمز الوصول الذي ضبطته في الاستضافة\">"` | — |
| [SRC-A16FA6D4B5-L000020](../../web/dashboard.html#L20) | 20 | `"    </div>"` | — |
| [SRC-A16FA6D4B5-L000021](../../web/dashboard.html#L21) | 21 | `"    <button class=\"secondary\" id=\"saveAccessToken\">تسجيل الدخول</button><button class=\"secondary\" id=\"logoutSession\">تسجيل الخروج</button>"` | — |
| [SRC-A16FA6D4B5-L000022](../../web/dashboard.html#L22) | 22 | `"  </div>"` | — |
| [SRC-A16FA6D4B5-L000023](../../web/dashboard.html#L23) | 23 | `"  <p id=\"authMessage\" class=\"muted\" aria-live=\"polite\">لا يُحفظ رمز الوصول في تخزين المتصفح القابل للقراءة بواسطة JavaScript. بعد تسجيل الدخول يستخدم المتصفح ملف ارتباط HttpOnly آمنًا لمدة 8 ساعات.</p>"` | — |
| [SRC-A16FA6D4B5-L000024](../../web/dashboard.html#L24) | 24 | `"</section>"` | — |
| [SRC-A16FA6D4B5-L000025](../../web/dashboard.html#L25) | 25 | `"<section class=\"hero\"><div class=\"card\"><span class=\"eyebrow\">مساحة العمل · الإصدار الأول</span><h2>حوّل الإشارات إلى فرص منظمة</h2><p class=\"muted\">أدخل نصًا من مصدر مسموح، افهم مؤشرات الاهتمام وأسبابها، ثم احفظ الإشارة وتابعها بنفسك. لا يوجد تواصل تلقائي مع أي شخص.</p><div class=\"stats\"><div class=\"stat\"><strong id=\"total\">—</strong><span>إشارة محفوظة</span></div><div class=\"stat\"><strong id=\"qualified\">—</strong><span>مؤهلة يدويًا</span></div><div class=\"stat\"><strong id=\"review\">—</strong><span>تحتاج مراجعة</span></div></div></div><div class=\"card\"><span class=\"eyebrow\">كيف يعمل Omarai؟</span><h2>القرار لك دائمًا</h2><p class=\"muted\">١. تحليل محلي قابل للتفسير<br>٢. تسجيل رابط المصدر ووقت الرصد<br>٣. منع التكرار لنفس النص والمصدر<br>٤. متابعة بشرية للحالة والخطوة التالية</p><p class=\"warning\">تنبيه: الدرجة قواعد إرشادية وليست احتمالًا إحصائيًا للشراء أو ضمانًا لجودة العميل.</p></div></section>"` | — |
| [SRC-A16FA6D4B5-L000026](../../web/dashboard.html#L26) | 26 | `"<section class=\"layout\"><div class=\"card\"><span class=\"eyebrow\">١ / تحليل إشارة</span><h2>اكتشف نية الاهتمام</h2><div class=\"field\"><label for=\"text\">النص المراد تحليله</label><textarea id=\"text\" placeholder=\"مثال: بدور على شقة في التجمع الخامس وممكن معاينة...\"></textarea></div><div class=\"field\"><label for=\"product\">نوع المنتج (اختياري)</label><input id=\"product\" placeholder=\"شقة، عقار\"></div><div class=\"field\"><label for=\"location\">المنطقة (اختياري)</label><input id=\"location\" placeholder=\"التجمع الخامس، العاصمة الإدارية\"></div><button class=\"primary\" id=\"analyze\">حلّل الإشارة ←</button><div class=\"result\" id=\"result\"></div></div>"` | — |
| [SRC-A16FA6D4B5-L000027](../../web/dashboard.html#L27) | 27 | `"<div class=\"card\"><span class=\"eyebrow\">٢ / حفظ ومتابعة</span><h2>سجّل المصدر</h2><div class=\"field\"><label for=\"source\">رابط المنشور أو المصدر</label><input id=\"source\" type=\"url\" placeholder=\"https://...\"></div><div class=\"field\"><label for=\"platform\">المنصة أو المصدر</label><select id=\"platform\"><option value=\"manual\">إدخال يدوي</option><option>Facebook</option><option>Website</option><option>OLX</option><option>Other</option></select></div><div class=\"field\"><label for=\"note\">ملاحظاتك (اختياري)</label><input id=\"note\" placeholder=\"ميزانية معلنة، موعد متابعة...\"></div><button class=\"primary\" id=\"save\">احفظ الإشارة</button><p class=\"muted\">لا تحفظ بيانات شخصية غير لازمة. أدخل فقط ما يحق لك معالجته.</p><div id=\"message\" class=\"muted\" aria-live=\"polite\"></div></div></section>"` | — |
| [SRC-A16FA6D4B5-L000028](../../web/dashboard.html#L28) | 28 | `"<section class=\"card leads\"><div class=\"leadhead\"><div><span class=\"eyebrow\">٣ / قائمة الفرص</span><h2>الإشارات المحفوظة</h2></div><button class=\"secondary\" id=\"refresh\">تحديث القائمة ↻</button></div><div id=\"leadlist\"><div class=\"empty\">جارٍ تحميل البيانات...</div></div></section><section class=\"card\" style=\"margin-top:16px\"><span class=\"eyebrow\">٤ / المساعد المحلي</span><h2>اسأل Omarai</h2><p class=\"muted\">اسأل عن عدد الإشارات، أولوية المراجعة، تفسير الدرجة، أو اطلب مسودة تواصل. الإجابات مبنية على سجلك المحلي وقواعد واضحة؛ لا يوجد نموذج سحابي ولا يتم إرسال رسائل.</p><div id=\"askMessages\" style=\"display:flex;flex-direction:column;gap:10px;margin:12px 0;max-height:270px;overflow:auto\"><div class=\"lead\">جرّب: «كام عميل عندي؟» أو «مين أفضل إشارة أراجعها؟»</div></div><div class=\"row\"><input id=\"askInput\" maxlength=\"1000\" placeholder=\"اكتب سؤالك هنا...\" style=\"flex:1;min-width:180px\"><button class=\"primary\" id=\"askBtn\">اسأل ←</button></div></section><div class=\"foot\">Omarai · Local-first · تخزين البيانات يعتمد على الخادم المستخدم · لا زحف آلي ولا رسائل تلقائية</div></div>"` | — |
| [SRC-A16FA6D4B5-L000029](../../web/dashboard.html#L29) | 29 | `"<script>"` | — |
| [SRC-A16FA6D4B5-L000030](../../web/dashboard.html#L30) | 30 | `"const $=id=>document.getElementById(id);let lastAssessment=null;let lastAnalysisInput=null;"` | — |
| [SRC-A16FA6D4B5-L000031](../../web/dashboard.html#L31) | 31 | `"const labels={high_intent:\"اهتمام قوي نسبيًا\",medium_intent:\"اهتمام متوسط\",early_research:\"استكشاف مبكر\",unclear:\"غير واضح\",not_buyer_signal:\"ليس إشارة شراء مباشرة\"};"` | — |
| [SRC-A16FA6D4B5-L000032](../../web/dashboard.html#L32) | 32 | `"const esc=s=>String(s??\"\").replace(/[&<>\"']/g,c=>({\"&\":\"&amp;\",\"<\":\"&lt;\",\">\":\"&gt;\",'\"':\"&quot;\",\"'\":\"&#39;\"}[c]));"` | — |
| [SRC-A16FA6D4B5-L000033](../../web/dashboard.html#L33) | 33 | `"function requestHeaders(extra={}){return {\"Content-Type\":\"application/json\",...extra};}"` | — |
| [SRC-A16FA6D4B5-L000034](../../web/dashboard.html#L34) | 34 | `"async function request(url,opts={}){const r=await fetch(url,{...opts,credentials:\"same-origin\",headers:requestHeaders(opts.headers\|\|{})});let d;try{d=await r.json()}catch(_error){d={error:\"استجابة غير صالحة من الخادم\"}}if(!r.ok)throw Error(d.error\|\|\"حدث خطأ\");return d}"` | — |
| [SRC-A16FA6D4B5-L000035](../../web/dashboard.html#L35) | 35 | `"function safeSourceUrl(value){try{const url=new URL(String(value??\"\"));if(![\"http:\",\"https:\"].includes(url.protocol)\|\|!url.hostname\|\|url.username\|\|url.password)return null;return url.href}catch(_error){return null}}"` | — |
| [SRC-A16FA6D4B5-L000036](../../web/dashboard.html#L36) | 36 | `"$(\"analyze\").onclick=async()=>{try{const text=$(\"text\").value;const product_terms=$(\"product\").value.split(\",\").map(x=>x.trim()).filter(Boolean);const location_terms=$(\"location\").value.split(\",\").map(x=>x.trim()).filter(Boolean);lastAssessment=await request(\"/api/analyze\",{method:\"POST\",body:JSON.stringify({text,product_terms,location_terms})});lastAnalysisInput={text,product_terms:JSON.stringify(product_terms),location_terms:JSON.stringify(location_terms)};const a=lastAssessment;$(\"result\").style.display=\"block\";$(\"result\").innerHTML='<div class=\"score\">'+a.score+'<small style=\"font-size:13px;color:#98a9c5\"> / 100 نقاط قواعد</small></div><span class=\"pill\">'+esc(labels[a.label]\|\|a.label)+'</span><p>'+esc(a.summary)+'</p><h3>لماذا؟</h3>'+(a.matched_signals.length?a.matched_signals.map(s=>'<div class=\"signal\">＋ '+esc(s.phrase)+' <span class=\"muted\">· '+esc(s.category)+' · +'+s.points+'</span></div>').join(\"\"):'<p class=\"muted\">لم تُطابق عبارة معروفة.</p>')+'<div class=\"warning\">'+a.warnings.map(esc).join(\"<br>\")+'</div>'}catch(e){$(\"message\").textContent=e.message}};"` | — |
| [SRC-A16FA6D4B5-L000037](../../web/dashboard.html#L37) | 37 | `"$(\"save\").onclick=async()=>{try{const text=$(\"text\").value;const product_terms=$(\"product\").value.split(\",\").map(x=>x.trim()).filter(Boolean);const location_terms=$(\"location\").value.split(\",\").map(x=>x.trim()).filter(Boolean);if(!lastAssessment)throw Error(\"حلّل النص أولًا قبل الحفظ.\");if(!lastAnalysisInput\|\|text!==lastAnalysisInput.text\|\|JSON.stringify(product_terms)!==lastAnalysisInput.product_terms\|\|JSON.stringify(location_terms)!==lastAnalysisInput.location_terms)throw Error(\"النص أو معايير التأهيل تغيّرت؛ أعد التحليل قبل الحفظ.\");const data=await request(\"/api/leads\",{method:\"POST\",body:JSON.stringify({text,source_url:$(\"source\").value,platform:$(\"platform\").value,note:$(\"note\").value,product_terms,location_terms})});$(\"message\").textContent=data.created?\"تم حفظ الإشارة بنجاح.\":\"الإشارة موجودة بالفعل؛ لم نكررها.\";await refresh()}catch(e){$(\"message\").textContent=e.message}};"` | — |
| [SRC-A16FA6D4B5-L000038](../../web/dashboard.html#L38) | 38 | `"async function refresh(){try{const d=await request(\"/api/leads?limit=500\");const rows=d.leads;$(\"total\").textContent=rows.length;$(\"qualified\").textContent=rows.filter(x=>[\"qualified\",\"contacted\",\"converted\"].includes(x.status)).length;$(\"review\").textContent=rows.filter(x=>x.status===\"needs_review\").length;if(!rows.length){$(\"leadlist\").innerHTML='<div class=\"empty\">لا توجد إشارات محفوظة بعد. ابدأ بتحليل إشارة ثم احفظها.</div>';return}$(\"leadlist\").innerHTML=rows.map(l=>{const sourceUrl=safeSourceUrl(l.source_url);const sourceLink=sourceUrl?'<a target=\"_blank\" rel=\"noopener noreferrer\" href=\"'+esc(sourceUrl)+'\" style=\"color:#7b9cff\">فتح الرابط</a>':'<span class=\"muted\">لا يوجد رابط HTTP(S) صالح</span>';return '<article class=\"lead\"><div class=\"leadhead\"><span class=\"pill\">'+esc(labels[l.assessment.label]\|\|l.assessment.label)+'</span><span class=\"muted\">'+esc(l.platform)+' · '+esc(l.observed_at)+'</span></div><p>'+esc(l.text)+'</p><div class=\"muted\">المصدر: '+sourceLink+' · الدرجة '+l.assessment.score+'</div><div class=\"row\" style=\"margin-top:10px\"><select aria-label=\"حالة المتابعة\" id=\"status-'+esc(l.id)+'\">'+[\"new\",\"qualified\",\"contacted\",\"converted\",\"rejected\",\"needs_review\"].map(s=>'<option value=\"'+s+'\" '+(s===l.status?\"selected\":\"\")+'>'+({new:\"جديد\",qualified:\"مؤهل\",contacted:\"تم التواصل\",converted:\"تحوّل لعميل\",rejected:\"مرفوض\",needs_review:\"مراجعة\"}[s])+'</option>').join(\"\")+'</select><button class=\"secondary\" data-action=\"save-status\" data-lead-id=\"'+esc(l.id)+'\">تحديث الحالة</button></div></article>'}).join(\"\")}catch(e){$(\"leadlist\").innerHTML='<div class=\"empty\">'+esc(e.message)+'</div>'}}"` | — |
| [SRC-A16FA6D4B5-L000039](../../web/dashboard.html#L39) | 39 | `"async function checkSession(){"` | — |
| [SRC-A16FA6D4B5-L000040](../../web/dashboard.html#L40) | 40 | `"  try{"` | — |
| [SRC-A16FA6D4B5-L000041](../../web/dashboard.html#L41) | 41 | `"    const response=await fetch(\"/api/session\",{credentials:\"same-origin\"});"` | — |
| [SRC-A16FA6D4B5-L000042](../../web/dashboard.html#L42) | 42 | `"    const data=await response.json();"` | — |
| [SRC-A16FA6D4B5-L000043](../../web/dashboard.html#L43) | 43 | `"    if(!response.ok)throw new Error(data.error\|\|\"لا توجد جلسة نشطة.\");"` | — |
| [SRC-A16FA6D4B5-L000044](../../web/dashboard.html#L44) | 44 | `"    $(\"authMessage\").textContent=\"جلسة نشطة بدور: \"+data.role;"` | — |
| [SRC-A16FA6D4B5-L000045](../../web/dashboard.html#L45) | 45 | `"    $(\"saveAccessToken\").textContent=\"متصل\";"` | — |
| [SRC-A16FA6D4B5-L000046](../../web/dashboard.html#L46) | 46 | `"  }catch(_error){$(\"authMessage\").textContent=\"أدخل رمز الوصول لبدء جلسة آمنة.\";}"` | — |
| [SRC-A16FA6D4B5-L000047](../../web/dashboard.html#L47) | 47 | `"}"` | — |
| [SRC-A16FA6D4B5-L000048](../../web/dashboard.html#L48) | 48 | `"$(\"saveAccessToken\").onclick=async()=>{"` | — |
| [SRC-A16FA6D4B5-L000049](../../web/dashboard.html#L49) | 49 | `"  const token=$(\"accessToken\").value.trim();"` | — |
| [SRC-A16FA6D4B5-L000050](../../web/dashboard.html#L50) | 50 | `"  if(!token){$(\"authMessage\").textContent=\"أدخل رمز الوصول أولًا.\";return;}"` | — |
| [SRC-A16FA6D4B5-L000051](../../web/dashboard.html#L51) | 51 | `"  try{"` | — |
| [SRC-A16FA6D4B5-L000052](../../web/dashboard.html#L52) | 52 | `"    const response=await fetch(\"/api/session\",{method:\"POST\",credentials:\"same-origin\",headers:{\"Content-Type\":\"application/json\"},body:JSON.stringify({access_token:token})});"` | — |
| [SRC-A16FA6D4B5-L000053](../../web/dashboard.html#L53) | 53 | `"    const data=await response.json();"` | — |
| [SRC-A16FA6D4B5-L000054](../../web/dashboard.html#L54) | 54 | `"    if(!response.ok)throw Error(data.error\|\|\"تعذر تسجيل الدخول.\");"` | — |
| [SRC-A16FA6D4B5-L000055](../../web/dashboard.html#L55) | 55 | `"    $(\"accessToken\").value=\"\";"` | — |
| [SRC-A16FA6D4B5-L000056](../../web/dashboard.html#L56) | 56 | `"    $(\"authMessage\").textContent=\"تم تسجيل الدخول بجلسة HttpOnly تنتهي خلال 8 ساعات أو عند انتهاء/إبطال الرمز.\";"` | — |
| [SRC-A16FA6D4B5-L000057](../../web/dashboard.html#L57) | 57 | `"    $(\"saveAccessToken\").textContent=\"متصل\";"` | — |
| [SRC-A16FA6D4B5-L000058](../../web/dashboard.html#L58) | 58 | `"    await refresh();"` | — |
| [SRC-A16FA6D4B5-L000059](../../web/dashboard.html#L59) | 59 | `"  }catch(error){$(\"authMessage\").textContent=error.message;}"` | — |
| [SRC-A16FA6D4B5-L000060](../../web/dashboard.html#L60) | 60 | `"};"` | — |
| [SRC-A16FA6D4B5-L000061](../../web/dashboard.html#L61) | 61 | `"$(\"logoutSession\").onclick=async()=>{"` | — |
| [SRC-A16FA6D4B5-L000062](../../web/dashboard.html#L62) | 62 | `"  try{"` | — |
| [SRC-A16FA6D4B5-L000063](../../web/dashboard.html#L63) | 63 | `"    const response=await fetch(\"/api/session/logout\",{method:\"POST\",credentials:\"same-origin\",headers:{\"Content-Type\":\"application/json\"},body:\"{}\"});"` | — |
| [SRC-A16FA6D4B5-L000064](../../web/dashboard.html#L64) | 64 | `"    const data=await response.json();"` | — |
| [SRC-A16FA6D4B5-L000065](../../web/dashboard.html#L65) | 65 | `"    if(!response.ok)throw Error(data.error\|\|\"تعذر تسجيل الخروج.\");"` | — |
| [SRC-A16FA6D4B5-L000066](../../web/dashboard.html#L66) | 66 | `"    $(\"authMessage\").textContent=\"تم تسجيل الخروج.\";"` | — |
| [SRC-A16FA6D4B5-L000067](../../web/dashboard.html#L67) | 67 | `"    $(\"saveAccessToken\").textContent=\"تسجيل الدخول\";"` | — |
| [SRC-A16FA6D4B5-L000068](../../web/dashboard.html#L68) | 68 | `"    await refresh();"` | — |
| [SRC-A16FA6D4B5-L000069](../../web/dashboard.html#L69) | 69 | `"  }catch(error){$(\"authMessage\").textContent=error.message;}"` | — |
| [SRC-A16FA6D4B5-L000070](../../web/dashboard.html#L70) | 70 | `"};"` | — |
| [SRC-A16FA6D4B5-L000071](../../web/dashboard.html#L71) | 71 | `"window.saveStatus=async id=>{try{const status=$(\"status-\"+id).value;await request(\"/api/leads/\"+id+\"/status\",{method:\"POST\",body:JSON.stringify({status})});await refresh()}catch(e){alert(e.message)}};"` | — |
| [SRC-A16FA6D4B5-L000072](../../web/dashboard.html#L72) | 72 | `"$(\"leadlist\").addEventListener(\"click\",event=>{const button=event.target.closest('button[data-action=\"save-status\"]');if(!button)return;const id=button.dataset.leadId;if(!/^[a-f0-9]{24}$/.test(id\|\|\"\"))return;void window.saveStatus(id)});"` | — |
| [SRC-A16FA6D4B5-L000073](../../web/dashboard.html#L73) | 73 | `"$(\"refresh\").onclick=refresh;$(\"askBtn\").onclick=askOmarai;$(\"askInput\").addEventListener(\"keydown\",e=>{if(e.key===\"Enter\"){e.preventDefault();askOmarai()}});async function askOmarai(){const question=$(\"askInput\").value.trim();if(!question)return;const box=$(\"askMessages\");const user=document.createElement(\"div\");user.className=\"lead\";user.style.borderColor=\"#2e5b62\";user.textContent=\"أنت: \"+question;box.appendChild(user);$(\"askInput\").value=\"\";$(\"askBtn\").disabled=true;try{const result=await request(\"/api/ask\",{method:\"POST\",body:JSON.stringify({question})});const answer=document.createElement(\"div\");answer.className=\"lead\";answer.textContent=\"Omarai: \"+result.answer;box.appendChild(answer)}catch(e){const answer=document.createElement(\"div\");answer.className=\"lead\";answer.textContent=\"تعذر تنفيذ السؤال: \"+e.message;box.appendChild(answer)}finally{$(\"askBtn\").disabled=false;box.scrollTop=box.scrollHeight}}checkSession().then(refresh);"` | — |
| [SRC-A16FA6D4B5-L000074](../../web/dashboard.html#L74) | 74 | `"</script></body></html>"` | — |
